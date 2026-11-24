# Install, repair, share, and update

Use this reference when installation, repair, relocation, sharing, or an update is
part of the request. Routine analysis uses the installed runtime and never
downloads software or changes the installation.

## What lives where

The skill folder carries instructions, the runtime manager, a pinned source
specification, the filtered build recipe, and its regression fixtures. The
executable, installation metadata, acquisition files, build dependencies, and
package caches stay outside the vault. Acquisition and build staging are removed
after both successful and failed builds.

The default runtime directory is `~/.local/share/rea-local`. A chosen external
directory can be supplied with `--runtime-root` to every command. Do not insert a
username, a particular vault path, or a build machine's temporary path into the
skill, recipe, or runtime. The manager locates its assets relative to its own
file. Its installed metadata records version, policy, and file integrity; it
does not record invocations, targets, durations, or usage.

The current platform is macOS. Python 3.9 or newer, Node.js at the version named
in `assets/runtime_spec.json`, npm, and `sandbox-exec` must be available. Check
these local programs first. On an unsupported platform, report the missing
platform adapter. Do not silently substitute an isolation method that permits
listeners. A future adapter needs the same deletion checks and whole-process
network and listener tests before that platform is supported.

## Install or reinstall

Resolve `REA_SKILL_DIR` to the actual canonical skill folder. Choose the default
external directory or set `REA_RUNTIME_ROOT` to the intended external location.
The examples below assume those two shell variables have already been set from
the verified locations.

```sh
python3 "$REA_SKILL_DIR/scripts/manage_runtime.py" install --runtime-root "$REA_RUNTIME_ROOT"
python3 "$REA_SKILL_DIR/scripts/manage_runtime.py" verify --runtime-root "$REA_RUNTIME_ROOT"
python3 "$REA_SKILL_DIR/scripts/manage_runtime.py" run --runtime-root "$REA_RUNTIME_ROOT" -- --version
python3 "$REA_SKILL_DIR/scripts/manage_runtime.py" run --runtime-root "$REA_RUNTIME_ROOT" -- --help
```

`install` checks a matching existing installation instead of replacing it.
`reinstall` forces a fresh build of the pinned version:

```sh
python3 "$REA_SKILL_DIR/scripts/manage_runtime.py" reinstall --runtime-root "$REA_RUNTIME_ROOT"
```

The manager checks the recipe and its inputs, downloads the exact source
archive, checks its digest, and refuses unsafe archive entries. It runs the
filtered build in an external staging directory. The candidate must pass source
and bundle policy checks plus functional verification with network access and
listeners denied. Installation and verification also test TCP listener binding,
Unix socket listener binding, and outbound localhost connections in both a
parent process and its child. Each must receive an OS permission denial. A
successful bind is closed immediately and makes the self-test fail. Only then
is the candidate activated as `current`. A previous filtered
runtime is retained for replacement recovery. A failed build or verification
leaves the working installation active.

The manager refuses unmanaged destination contents and symbolic links in managed
paths. Choose a fresh directory when another program owns the destination. Do
not delete an unrelated directory to make installation proceed. An OS file lock
prevents an installation from replacing a running analysis. It clears when the
process exits and requires no invocation or PID history.

The source specification and removal recipe define the installed program. Do
not replace it with an upstream setup command, a global package, an unmodified
package downloaded on demand, or an unpinned version. No MCP configuration is
needed or written.

## Verify or repair

`verify` checks the current skill specification, installed file hashes, expected
runtime contents, policy checks, and functional examples. `run` checks the
installed file manifest and matching specification before executing an allowed
command. Missing or changed installations return a nonzero error; analysis does
not trigger an automatic reinstall.

When a repair is requested, use `reinstall` and repeat `verify` and one bounded
analysis. If the source, dependencies, or build recipe changed, treat that as an
update instead of weakening a check. Report test results in the current task's requested form or under the recipient's existing reporting policy. Any saved report requires explicit authorization and an owning destination. The manager does not save build or analysis logs.

## Relocate or install into another vault

For relocation on the same supported platform, copy the complete managed runtime
directory to a fresh external location. Run `verify --runtime-root` against the
new location before selecting it for analysis. Its metadata and executable use
relative paths, so no runtime rebuild is required merely because its directory
changed. Alternatively, reinstall directly into the new external location.

For a recipient vault, read that vault's own agent instructions, standing
preferences, layout, skill schema, and mounting procedure first. Use its normal
skill creation or import workflow to place the complete `rea` folder in its
canonical skill location. Keep it in Engineering System where that system
exists; otherwise use the recipient's corresponding engineering section and
schema. Rebuild the recipient's generated registry and mount the canonical
skill through its own tools. Do not copy another person's personal instructions
or machine configuration.

Build a fresh external runtime with the recipient's copy of this manager, then
run verification and a small supplied fixture. The skill requires no original
vault path and no installed files from the sender. When the sender requests a
share package, use the vault's export workflow for the complete skill and its
setup assets. Installed runtimes, dependencies, caches, personal notes, and test
outputs are not the share package.

## Update a source version or its dependencies

An update is an explicit maintenance task. There are no automatic checks,
self-update commands, update timestamps, or background refresh processes.

1. Work on a copy of the complete skill outside the vault. Select an exact
   upstream version or commit and record its archive URL and SHA-256 digest.
   Inspect the source and dependency changes. Refresh the pinned dependency
   specification, the selected source closure and its `source.files` paths and
   digests, and the version-specific filtering recipe together. Keep the source
   and local version constants in the recipe, entrypoint, and specification in
   agreement.
2. Physically remove telemetry, usage tracking, invocation metrics, updater
   machinery, server entrypoints, listener paths, and their callers/imports from
   the executable closure. Keep only the supported local commands and required
   error handling. Check both source selection and built output. Do not replace
   a failed deletion with an environment toggle.
3. Recompute the recipe digest and the digests of every declared recipe input in
   the proposed `runtime_spec.json`. Build and test that skill copy into a fresh
   external runtime directory. Run the manager lifecycle tests, policy tests,
   functional fixture tests, and network/listener denial tests. Check that the
   runtime contains no build dependencies, source checkout, or machine paths.
4. Keep the current canonical skill recipe and specification available outside
   the vault while replacing them with the verified proposal. Use `update` to
   rebuild and activate the matching version at the active runtime directory:

   ```sh
   python3 "$REA_SKILL_DIR/scripts/manage_runtime.py" update --runtime-root "$REA_RUNTIME_ROOT"
   python3 "$REA_SKILL_DIR/scripts/manage_runtime.py" verify --runtime-root "$REA_RUNTIME_ROOT"
   ```

5. If activation fails, the old runtime remains active. Restore the old canonical
   specification and recipe so they continue to match it, and resolve the
   reported incompatibility. Do not leave the old runtime paired with a new
   specification or silently install unfiltered upstream software.
6. After success, revise affected command instructions and generated vault views
   together. Follow the vault's normal system change logging instruction. Report
   the installed version, verified behavior, and any remaining capability gap
   in the current task's requested form or under the recipient's existing reporting policy.
   Do not create a usage ledger as part of the update.

`--spec /path/to/runtime_spec.json` selects a complete reviewed specification for
an isolated trial installation. Its recipe and declared inputs resolve relative
to that specification. This does not rewrite the canonical skill. Normal use
returns to the canonical `assets/runtime_spec.json`, and its digest must match
the active runtime.
