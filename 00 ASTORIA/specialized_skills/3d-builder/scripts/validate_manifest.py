#!/usr/bin/env python3
"""Check a component/step manifest without changing it or its source models.

Requirements: Python 3 standard library. Author: Codex, 2026-10-25.
Usage: python validate_manifest.py /absolute/path/assembly_manifest.json
Reports source, units, geometry and interface uncertainty; does not establish fit.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
import re

PROVENANCE = {"source", "measured", "approximate", "local_alternative"}
INVENTORY = {"confirmed_available", "confirmed_missing", "unconfirmed"}
KINDS = {"mesh", "box", "cylinder", "polyline"}


def finite_vector(value, length=3):
    return (isinstance(value, list) and len(value) == length and
            all(isinstance(x, (int, float)) and not isinstance(x, bool) and
                math.isfinite(x) for x in value))


def validate_manifest(path):
    path = Path(path).resolve()
    errors, uncertainty, source_files = [], [], []
    try:
        manifest = json.loads(path.read_text())
    except (OSError, json.JSONDecodeError) as error:
        return {"ok": False, "errors": [str(error)], "uncertainty": [], "sources": []}
    if not isinstance(manifest, dict):
        return {"ok": False, "errors": ["Manifest must be an object"], "uncertainty": [], "sources": []}
    if manifest.get("version") != 1:
        errors.append("version must be 1")
    if manifest.get("units") != "mm":
        errors.append("Engineering manifest units must be mm")
    if not isinstance(manifest.get("title"), str) or not manifest["title"].strip():
        errors.append("A nonempty title is required")
    components = manifest.get("components")
    if not isinstance(components, list) or not components:
        errors.append("components must be a nonempty list")
        components = []
    identifiers = set()
    variants = {"baseline"}
    for number, component in enumerate(components, 1):
        if not isinstance(component, dict):
            errors.append(f"Component {number} must be an object")
            continue
        cid = component.get("id", f"component {number}")
        prefix = str(cid) + ": "
        if not isinstance(cid, str) or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.-]*", cid):
            errors.append(prefix + "id must use letters, digits, underscore, dot or hyphen")
        if str(cid) in identifiers:
            errors.append(prefix + "duplicate id")
        identifiers.add(str(cid))
        if not isinstance(component.get("name"), str) or not component["name"].strip():
            errors.append(prefix + "name is required")
        kind = component.get("kind")
        if not isinstance(kind, str) or kind not in KINDS:
            errors.append(prefix + "unsupported geometry kind")
        if not isinstance(component.get("provenance"), str) or component.get("provenance") not in PROVENANCE:
            errors.append(prefix + "explicit geometry provenance is required")
        if not isinstance(component.get("inventory_status"), str) or component.get("inventory_status") not in INVENTORY:
            errors.append(prefix + "explicit inventory_status is required")
        for field in ("source_status", "group"):
            if field in component and (not isinstance(component[field], str) or not component[field].strip()):
                errors.append(prefix + field + " must be a nonempty string")
        for field in ("position_mm", "rotation_deg"):
            if not finite_vector(component.get(field)):
                errors.append(prefix + field + " must contain three finite numbers")
        if not isinstance(component.get("step"), int) or isinstance(component.get("step"), bool) or component["step"] < 0:
            errors.append(prefix + "step must be a nonnegative integer")
        variant = component.get("variant", "baseline")
        if not isinstance(variant, str) or not variant:
            errors.append(prefix + "variant must be a nonempty string")
        else:
            variants.add(variant)
        if "explode_mm" in component and not finite_vector(component["explode_mm"]):
            errors.append(prefix + "explode_mm must contain three finite numbers")
        if "color" in component and (not finite_vector(component["color"], 4) or
                                      not all(0 <= c <= 1 for c in component["color"])):
            errors.append(prefix + "color must contain four values from 0 to 1")
        if kind == "box":
            if not finite_vector(component.get("size_mm")) or not all(x > 0 for x in component.get("size_mm", [])):
                errors.append(prefix + "size_mm must contain three positive dimensions")
        elif kind == "cylinder":
            for field in ("radius_mm", "depth_mm"):
                x = component.get(field)
                if not isinstance(x, (int, float)) or isinstance(x, bool) or not math.isfinite(x) or x <= 0:
                    errors.append(prefix + field + " must be positive and finite")
        elif kind == "polyline":
            points = component.get("points_mm")
            if not isinstance(points, list) or len(points) < 2 or not all(finite_vector(p) for p in points):
                errors.append(prefix + "points_mm requires at least two finite 3D points")
            x = component.get("radius_mm")
            if not isinstance(x, (int, float)) or isinstance(x, bool) or not math.isfinite(x) or x <= 0:
                errors.append(prefix + "radius_mm must be positive and finite")
        elif kind == "mesh":
            source = component.get("source_file")
            if not isinstance(source, str) or not source:
                errors.append(prefix + "source_file is required")
            else:
                source_path = (path.parent / source).resolve()
                if not source_path.is_file():
                    errors.append(prefix + "source file is missing: " + str(source_path))
                elif source_path.suffix.lower() not in {".stl", ".glb", ".gltf", ".obj"}:
                    errors.append(prefix + "mesh source must be STL, OBJ or glTF; tessellate STEP explicitly first")
                else:
                    digest = hashlib.sha256(source_path.read_bytes()).hexdigest()
                    expected = component.get("source_sha256")
                    if expected is not None and expected != digest:
                        errors.append(prefix + "source hash differs")
                    source_files.append({"id": cid, "path": str(source_path), "sha256": digest})
            if not isinstance(component.get("source_units"), str) or component.get("source_units") not in {"mm", "m"}:
                errors.append(prefix + "source_units must explicitly be mm or m")
            if isinstance(source, str) and Path(source).suffix.lower() in {".glb", ".gltf"} and component.get("source_units") != "m":
                errors.append(prefix + "glTF coordinates are meters; source_units must be m")
        if component.get("provenance") == "approximate":
            uncertainty.append(prefix + "approximate geometry; no measured fit claim")
        if component.get("inventory_status") == "confirmed_missing":
            uncertainty.append(prefix + "part is missing; render is a placeholder")
        elif component.get("inventory_status") == "unconfirmed":
            uncertainty.append(prefix + "physical availability is unconfirmed")
        if component.get("source_status", "unspecified") == "unspecified":
            uncertainty.append(prefix + "official/local source status is unspecified")
    names = set()
    views = manifest.get("views", [{"name": "overview", "mode": "assembled"}])
    if not isinstance(views, list) or not views:
        errors.append("views must be a nonempty list when supplied")
        views = []
    for view in views:
        if not isinstance(view, dict):
            errors.append("Each view must be an object")
            continue
        name = view.get("name", "")
        if not isinstance(name, str) or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_-]*", name):
            errors.append("View name must be a simple filename stem")
        if str(name) in names:
            errors.append("Duplicate view name: " + str(name))
        names.add(str(name))
        if not isinstance(view.get("mode"), str) or view.get("mode") not in {"assembled", "exploded", "step"}:
            errors.append(str(name) + ": unsupported view mode")
        if view.get("mode") == "step" and (not isinstance(view.get("step"), int) or isinstance(view.get("step"), bool) or view["step"] < 0):
            errors.append(str(name) + ": step view requires a nonnegative step")
        selected = view.get("variants", ["baseline"])
        if not isinstance(selected, list) or not selected or any(not isinstance(v, str) or v not in variants for v in selected):
            errors.append(str(name) + ": variants must select existing variants")
        if not isinstance(view.get("camera", "iso"), str) or view.get("camera", "iso") not in {"iso", "top", "front"}:
            errors.append(str(name) + ": camera must be iso, top or front")
        if "focus_ids" in view and (not isinstance(view["focus_ids"], list) or
                                     any(not isinstance(cid, str) or cid not in identifiers for cid in view["focus_ids"])):
            errors.append(str(name) + ": focus_ids must name existing components")
        if "caption" in view and not isinstance(view["caption"], str):
            errors.append(str(name) + ": caption must be a string")
    if "notes" in manifest and (not isinstance(manifest["notes"], list) or
                                any(not isinstance(note, str) for note in manifest["notes"])):
        errors.append("notes must be a list of strings")
    return {"ok": not errors, "errors": errors, "uncertainty": uncertainty,
            "sources": source_files, "component_count": len(components),
            "view_count": len(views), "units": manifest.get("units")}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path)
    args = parser.parse_args()
    result = validate_manifest(args.manifest)
    print(json.dumps(result, indent=2))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
