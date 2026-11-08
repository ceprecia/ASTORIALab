#!/usr/bin/env python3
"""install_specialized.py: choose specialized research skills from the catalog and install them.

Purpose: on a starter vault, 00 ASTORIA/specialized_skills/ holds every
specialized research skill (modality coordinators, method guides, software
and model adapters, datasets, acquisition, computing). setup-my-vault asks the
user which groups they want, then this script moves the chosen folders into
00 ASTORIA/skills/, regenerates the Skill Map and the coordinator catalogs,
lints, and removes the catalog folder.

Language: Python 3 and PyYAML for the YAML vocabulary.
Author: ASTORIA System Builder. Date: 2026-09-24.

Usage:
    python3 install_specialized.py --list
        Print the groups the catalog offers, with the skills in each.
    python3 install_specialized.py --groups fmri,eeg,general,behavior [--names a,b] [--no-multimodal]
        Print the installation plan (dry run): chosen skills, coordinators and
        dependencies pulled in, and what stays in the catalog.
    python3 install_specialized.py --groups ... --apply
        Move the chosen folders, rebuild the views, run the lint.
    python3 install_specialized.py --groups ... --apply --remove-catalog
        Also delete 00 ASTORIA/specialized_skills/ when the lint passes.
    python3 install_specialized.py --none [--apply --remove-catalog]
        Keep the core skills only; preview first, then remove the unused catalog.
    Add --vault PATH when running from outside the vault.

    An interrupted selected install can be retried with the same approved
    options while its moved folders and pre-link identities and bytes verify.
    List and preview stop during recovery. Keep the temporary install state
    and catalog until the checks succeed.

Groups are modality values from the vocabulary plus "general" (modality any).
Choosing an imaging modality also installs its modality coordinator and, unless
--no-multimodal is given, the multimodal skills that apply to any imaging work.
"""
import hashlib
import json
import os
from pathlib import Path
import shutil
import stat
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import skillkit as sk

# Toggles
DEFAULT_INCLUDE_MULTIMODAL = True   # multimodal skills follow any imaging modality
GENERAL_GROUP_NAME = "general"      # the name users see for modality "any"


def argument(argv, flag, default=None):
    """Return the value after a flag, or the default."""
    if flag in argv:
        i = argv.index(flag)
        if i + 1 >= len(argv) or argv[i + 1].startswith("--"):
            raise ValueError("%s needs a value" % flag)
        return argv[i + 1]
    return default


def catalog_groups(catalog, vocab):
    """Map each group name to the sorted skill names in it."""
    groups = {}
    for name, skill in catalog.items():
        modality = skill.meta.get("modality", "") or ""
        for value in [m.strip() for m in modality.split(",") if m.strip()] or ["any"]:
            key = GENERAL_GROUP_NAME if value == "any" else value
            groups.setdefault(key, set()).add(name)
    return {k: sorted(v) for k, v in groups.items()}


def plan(catalog, vocab, chosen_groups, extra_names, include_multimodal):
    """Compute the set of catalog skills to install and why each one is included."""
    groups = catalog_groups(catalog, vocab)
    imaging = set((vocab.get("starter") or {}).get("imaging_modalities") or [])
    reasons = {}

    # Step 1: every skill in a chosen group
    for g in chosen_groups:
        for name in groups.get(g, []):
            reasons.setdefault(name, "group %s" % g)

    # Step 2: the multimodal group follows any imaging modality
    if include_multimodal and any(g in imaging for g in chosen_groups):
        for name in groups.get("multimodal", []):
            reasons.setdefault(name, "multimodal, follows the imaging modalities chosen")

    # Step 3: names the user added directly
    for name in extra_names:
        if name in catalog:
            reasons.setdefault(name, "named directly")
        else:
            reasons.setdefault(name, "NOT IN CATALOG")

    # Step 4: modality coordinators for every modality present in the selection
    for name, skill in catalog.items():
        if skill.family == "modality-coordinator":
            modality = skill.meta.get("modality", "")
            if any(catalog[n].meta.get("modality", "") == modality for n in list(reasons) if n in catalog):
                reasons.setdefault(name, "coordinator for modality %s" % modality)

    # Step 5: declared dependencies that live in the catalog
    changed = True
    while changed:
        changed = False
        for name in list(reasons):
            if name not in catalog:
                continue
            for dep in catalog[name].dependencies:
                if dep in catalog and dep not in reasons:
                    reasons[dep] = "dependency of %s" % name
                    changed = True
    return reasons, groups


INSTALL_STATE = ".toolkit-install-in-progress.json"


def directory_identity(path):
    info = path.lstat()
    if not stat.S_ISDIR(info.st_mode):
        raise ValueError("Expected an actual directory at %s" % path)
    return [info.st_dev, info.st_ino]


def digest_entries(entries):
    return hashlib.sha256(json.dumps(entries, sort_keys=True).encode("utf-8")).hexdigest()


def tree_digest(root, ignore=()):
    entries = {}
    for path in root.rglob("*"):
        relative = path.relative_to(root)
        if relative.parts[0] in ignore:
            continue
        info = path.lstat()
        if stat.S_ISDIR(info.st_mode):
            entries[relative.as_posix()] = None
        elif stat.S_ISREG(info.st_mode):
            if path.suffix.lower() == ".md" and info.st_nlink != 1:
                raise ValueError("Cannot verify a hard-linked Markdown file at %s" % path)
            entries[relative.as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
        else:
            raise ValueError("Cannot verify non-regular catalog or skill entry at %s" % path)
    return digest_entries(entries)


def relocation_map(names):
    return {os.path.join(sk.CATALOG_REL, name): os.path.join(sk.SKILLS_REL, name)
            for name in sorted(names)}


def document_digest(vault, relocations, unavailable):
    """Hash the pre-repair Markdown at its projected final paths."""
    links = sk.PortableLinks(vault, relocations, unavailable)
    if links.problems:
        raise ValueError("\n".join(links.problems))
    entries = {}
    for relative in sorted(links.files):
        target = links._relocate(relative)
        if target in entries:
            raise ValueError("Two documents resolve to the same install path: %s" % target)
        original = links.read_markdown(relative)
        entries[target] = [links.identities[relative], hashlib.sha256(original).hexdigest()]
    return digest_entries(entries)


def state_record(path):
    info = path.lstat()
    if not stat.S_ISREG(info.st_mode) or info.st_nlink != 1:
        raise ValueError("The install-state path is not a regular file without aliases")
    return json.loads(path.read_text(encoding="utf-8")), [info.st_dev, info.st_ino]


def write_state(path, data):
    flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL
    with os.fdopen(os.open(path, flags, 0o600), "w", encoding="utf-8") as handle:
        json.dump(data, handle, sort_keys=True)
        handle.flush()
        os.fsync(handle.fileno())
    return state_record(path)[1]


def verify_state(data, request, catalog_dir, live_dir, vault):
    if (not isinstance(data, dict) or data.get("version") != 2
            or data.get("request") != request or not isinstance(data.get("selected"), dict)):
        raise ValueError("Retry requires the exact originally approved selection and options")
    selected = data["selected"]
    if not selected or any(not name or name.startswith(".") or "/" in name or "\\" in name
                           for name in selected):
        raise ValueError("The recorded skill names are invalid")
    relocations = relocation_map(selected)
    if relocations != data.get("relocations"):
        raise ValueError("The recorded relocations are invalid")
    if (directory_identity(catalog_dir) != data.get("catalog_dir")
            or directory_identity(live_dir) != data.get("live_dir")):
        raise ValueError("The catalog or live directory identity changed")
    if tree_digest(catalog_dir, selected) != data.get("catalog_remaining"):
        raise ValueError("The remaining catalog changed since the approved move plan")

    moved = set()
    for name, expected in selected.items():
        src, dst = catalog_dir / name, live_dir / name
        candidates = [path for path in (src, dst) if os.path.lexists(path)]
        if len(candidates) != 1:
            raise ValueError("Expected exactly one catalog or live folder for %s" % name)
        path = candidates[0]
        actual = [directory_identity(path), tree_digest(path)]
        if actual != expected:
            raise ValueError("Folder identity or content changed for %s" % name)
        if path == dst:
            moved.add(name)
    if document_digest(vault, relocations, data["unavailable"]) != data.get("documents"):
        raise ValueError("Pre-link document identity or bytes changed; verify the install state")
    return moved


def start_state(path, request, catalog_dir, live_dir, vault, install, unavailable):
    # Verify all selected destinations before recording or moving any folder.
    catalog_identity = directory_identity(catalog_dir)
    live_identity = directory_identity(live_dir)
    if any(name.startswith('.') for name in install):
        raise ValueError("Hidden catalog folders cannot be selected")
    live_names = {entry.name.casefold() for entry in live_dir.iterdir()}
    for name in install:
        if name.casefold() in live_names or os.path.lexists(live_dir / name):
            raise ValueError("Live destination is already occupied for %s" % name)
    selected = {name: [directory_identity(catalog_dir / name), tree_digest(catalog_dir / name)]
                for name in install}
    relocations = relocation_map(install)
    data = {"version": 2, "request": request, "selected": selected,
            "catalog_dir": catalog_identity, "live_dir": live_identity,
            "catalog_remaining": tree_digest(catalog_dir, selected), "relocations": relocations,
            "unavailable": unavailable,
            "documents": document_digest(vault, relocations, unavailable)}
    return data, write_state(path, data)


def stop_install(error):
    print("Toolkit installation stopped: %s" % error)
    print("Keep the catalog and existing files. Retry only with the exact approved options "
          "and verified install state, or use manual recovery after inspecting the files.")
    return 1


def main(argv):
    # Validate explicit choices before any installation or catalog removal.
    try:
        chosen_groups = [g.strip() for g in (argument(argv, "--groups") or "").split(",") if g.strip()]
        extra_names = [n.strip() for n in (argument(argv, "--names") or "").split(",") if n.strip()]
        assume_notes = argument(argv, "--assume-notes")
        argument(argv, "--vault")
    except ValueError as error:
        print(error)
        return 1
    core_only = "--none" in argv
    if core_only and ("--groups" in argv or "--names" in argv):
        print("--none cannot be combined with --groups or --names")
        return 1
    if "--list" not in argv and not core_only and not chosen_groups and not extra_names:
        print("Choose --groups or --names, or use --none to keep the core skills only.")
        return 1

    vault = sk.vault_from_argv(argv)
    vocab = sk.load_vocab(vault)
    catalog_dir = Path(vault) / sk.CATALOG_REL
    live_dir = Path(vault) / sk.SKILLS_REL
    state_path = catalog_dir.parent / INSTALL_STATE
    apply = "--apply" in argv and "--list" not in argv
    include_multimodal = DEFAULT_INCLUDE_MULTIMODAL and "--no-multimodal" not in argv
    request = {"groups": chosen_groups, "names": extra_names, "core_only": core_only,
               "include_multimodal": include_multimodal, "remove_catalog": "--remove-catalog" in argv,
               "assume_notes": assume_notes, "portable": sk.portable_links_enabled(vocab)}
    state = identity = None
    moved = set()
    if os.path.lexists(state_path):
        if not apply:
            return stop_install("An interrupted install is recorded; the remaining catalog cannot supply a fresh preview")
        try:
            state, identity = state_record(state_path)
            moved = verify_state(state, request, catalog_dir, live_dir, vault)
        except (OSError, ValueError, KeyError, TypeError, RuntimeError) as error:
            return stop_install(error)

    if not catalog_dir.is_dir():
        print("no catalog at %s; nothing to install" % sk.CATALOG_REL)
        return 0
    if apply and core_only and request["remove_catalog"]:
        try:
            directory_identity(catalog_dir)
            tree_digest(catalog_dir)
        except (OSError, ValueError, RuntimeError) as error:
            return stop_install(error)
    catalog = sk.load_skills(vault, sk.CATALOG_REL)
    if moved:
        live = sk.load_skills(vault)
        for name in moved:
            if name not in live:
                return stop_install("Verified moved folder lacks an active skill: %s" % name)
            catalog[name] = live[name]

    if "--list" in argv:
        groups = catalog_groups(catalog, vocab)
        print("Catalog: %d specialized skills in %d groups\n" % (len(catalog), len(groups)))
        for g in sorted(groups):
            print("%s (%d): %s" % (g, len(groups[g]), ", ".join(groups[g])))
        return 0

    reasons, groups = plan(catalog, vocab, chosen_groups, extra_names, include_multimodal)
    unknown_groups = [g for g in chosen_groups if g not in groups]
    missing = [n for n, r in reasons.items() if r == "NOT IN CATALOG"]
    if unknown_groups or missing:
        if unknown_groups:
            print("unknown groups (not in the catalog): %s" % ", ".join(unknown_groups))
        if missing:
            print("names not in the catalog: %s" % ", ".join(missing))
        return stop_install("The requested selection cannot be established from the catalog")
    install = sorted(n for n in reasons if n in catalog)
    staying = sorted(set(catalog) - set(install))
    unavailable = staying if request["remove_catalog"] else []
    if state is not None and (set(install) != set(state["selected"]) or unavailable != state["unavailable"]):
        return stop_install("The approved selection or catalog membership changed")

    if apply and state is None and not core_only:
        # Without the record, live folders cannot prove an earlier selected move.
        index = set((vocab.get("starter") or {}).get("catalog_index") or ())
        live_optional = {name: skill for name, skill in sk.load_skills(vault).items()
                         if name in index and name not in catalog}
        if live_optional:
            broader_plan, _ = plan({**catalog, **live_optional}, vocab, chosen_groups,
                                   extra_names, include_multimodal)
            if set(broader_plan) & set(live_optional):
                return stop_install("The selection includes already-live catalog names without verified state")

    print("Installation plan: %d of %d catalog skills" % (len(install), len(catalog)))
    if core_only:
        print("Core only: keep the existing live skills and install no optional toolkit.")
    for name in install:
        print("  + %-40s %s" % (name, reasons[name]))
    print("staying in the catalog: %d" % len(staying))

    if "--apply" not in argv:
        print("\ndry run; add --apply to install")
        return 0

    relocations = relocation_map(install)
    if install:
        try:
            if state is None:
                state, identity = start_state(state_path, request, catalog_dir, live_dir, vault,
                                              install, unavailable)
            for name in install:
                if name in moved:
                    continue
                src, dst = catalog_dir / name, live_dir / name
                if os.path.lexists(dst):
                    raise ValueError("Live destination is already occupied for %s" % name)
                # Rename retains the recorded directory identity on the same filesystem.
                src.rename(dst)
            if verify_state(state, request, catalog_dir, live_dir, vault) != set(install):
                raise ValueError("The selected folders did not all reach the live directory")
        except (OSError, ValueError, KeyError, TypeError, RuntimeError) as error:
            return stop_install(error)
    print("verified %d skill folders in %s" % (len(install), sk.SKILLS_REL))

    if not request["portable"] and not install:
        try:
            document_digest(vault, relocations, unavailable)
        except (OSError, ValueError, RuntimeError) as error:
            return stop_install(error)

    if request["portable"]:
        try:
            changed, problems = sk.portable_vault_links(vault, relocations, unavailable)
        except (OSError, ValueError) as error:
            return stop_install(error)
        if problems:
            print("Portable link repair needs review; the catalog folder was kept:")
            print("\n".join(problems))
            return 1
        print("updated portable links in %d documents" % len(changed))

    # Rebuild the views and lint
    here = os.path.dirname(os.path.abspath(__file__))
    views = subprocess.run([sys.executable, os.path.join(here, "build_views.py"), "--vault", vault], check=False)
    if views.returncode != 0:
        print("view generation failed; the catalog folder was kept")
        return 1
    lint = subprocess.run([sys.executable, os.path.join(here, "lint.py"), "--vault", vault] + (
        ["--assume-notes", assume_notes] if assume_notes else []),
        capture_output=True, text=True)
    print(lint.stdout.strip().splitlines()[0] if lint.stdout.strip() else "lint produced no output")
    if lint.returncode != 0:
        print(lint.stdout)
        print("lint reported errors; the catalog folder was kept")
        return 1

    try:
        if state is not None and state_record(state_path) != (state, identity):
            raise ValueError("The install-state record changed during the installation")
        if request["remove_catalog"]:
            if state is not None and (directory_identity(catalog_dir) != state["catalog_dir"]
                    or any(os.path.lexists(catalog_dir / name) for name in install)
                    or tree_digest(catalog_dir) != state["catalog_remaining"]):
                raise ValueError("The remaining catalog changed before cleanup")
            shutil.rmtree(catalog_dir)
            print("removed %s (%d unselected skills remain available in the ASTORIA repository)" % (sk.CATALOG_REL, len(staying)))
        if state is not None:
            state_path.unlink()
    except (OSError, ValueError) as error:
        return stop_install(error)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
