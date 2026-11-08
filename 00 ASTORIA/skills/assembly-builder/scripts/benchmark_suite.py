"""Prepare blind build packets; independently compare saved geometry and wiring.

Runtime: engineering Python environment (CadQuery, numpy, trimesh).
Reports and generated fixtures belong outside the vault. Reference data must
not be supplied to a holdout builder. Retuning a failed case makes it development.
"""
import argparse
import copy
import hashlib
import itertools
import json
import math
import shutil
import subprocess
import urllib.request
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
SOURCES = {
    "cadquery_axis": "https://raw.githubusercontent.com/CadQuery/cadquery/b94a06799ab36d62f9faa20021ddba3d1d4a2ecb/doc/assy.rst",
    "arduino_button": "https://raw.githubusercontent.com/arduino/docs-content/5ab38b1532ab85f805ce7842a9f97e95eeff7a05/content/built-in-examples/02.digital/Button/Button.md",
    "arduino_sketch": "https://raw.githubusercontent.com/arduino/arduino-examples/1447c5b5706415aedcda0b6d0c13f26cfde7c220/examples/02.Digital/Button/Button.ino",
}


def save(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2) + "\n")


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def prepare(out):
    import cadquery as cq
    inputs, refs = out / "inputs", out / "reference"
    if out.exists():
        raise SystemExit("Use a fresh output directory to freeze a new run.")
    inputs.mkdir(parents=True)
    refs.mkdir()
    source_index = {}
    for name, url in SOURCES.items():
        target = inputs / "sources" / (name + (".ino" if name.endswith("sketch") else ".txt"))
        target.parent.mkdir(exist_ok=True)
        target.write_bytes(urllib.request.urlopen(url, timeout=45).read())
        source_index[name] = {"url": url, "sha256": digest(target)}
    save(inputs / "source_index.json", source_index)
    parts = inputs / "parts"
    parts.mkdir()
    shapes = {
        "cube": cq.Workplane().box(20, 20, 20),
        "plate": cq.Workplane().box(10, 10, 1).faces(">Z").workplane().hole(2),
        "cone": cq.Solid.makeCone(0.8, 0, 4),
    }
    for name, shape in shapes.items():
        cq.exporters.export(shape, str(parts / (name + ".step")))
        cq.exporters.export(shape, str(parts / (name + ".stl")), tolerance=0.001, angularTolerance=0.02)
    (inputs / "BUILD.txt").write_text(
        "Build these three independent reference cases with the assembly and 3D skills.\n"
        "Do not read the sibling reference directory or evaluator. Use mm engineering data.\n"
        "Output each case under cube/, axis/, button/ with manifest.json and assembly.blend,\n"
        "assembly.glb plus overview/exploded/step images. Keep editable build code.\n"
        "Use the frozen source files, not a solved placement or reference image.\n\n"
        "CUBE (custom calibration fixture): use the supplied unchanged 20 mm cube.\n"
        "Make three copies with IDs cube0, cube45, cube90, centered respectively at\n"
        "(0,0,0), (40,0,0), (80,0,0) mm and rotated about global Z by 0,45,90 degrees.\n"
        "Declare this axis/travel as a synthetic regression study, not device motion.\n"
        "Sample the travel at 0,45,90 degrees and report clearance to a fixed obstacle\n"
        "with bounds X=[15,25], Y=[-5,5], Z=[-10,10] mm, relative to the first cube center.\n"
        "Use oriented geometry, not bounding-box overlap alone. No force claims.\n\n"
        "AXIS: use supplied plate and cone unchanged. Follow the self-contained\n"
        "plate/cone Axis example in sources/cadquery_axis.txt (the second Axis example).\n"
        "Coincide plate upper-face center with cone base-face center using Point.\n"
        "Constrain those face outward normals to the same direction (Axis param=0).\n"
        "Do not infer a new pose from how a cone normally stands. Preserve native origins.\n\n"
        "BUTTON: follow sources/arduino_button.txt and arduino_sketch.ino, choosing Uno R3.\n"
        "Represent board/button/breadboard/resistor as dimensionally approximate proxies.\n"
        "The fixture has one Uno, one breadboard, one momentary button, one external\n"
        "10 kohm resistor, and hookup wire, all available for this synthetic case.\n"
        "Logical switch terminals A1/A2 are internally joined; B1/B2 are internally\n"
        "joined; pressing connects groups A and B. Choose either group for supply.\n"
        "Write circuit.json: bom list of {id,kind,quantity,value_ohm if resistor};\n"
        "nets list of terminal-string lists (UNO.5V, UNO.GND, UNO.D2, SW1.A1/A2/B1/B2,\n"
        "R1.1/R1.2); states {released:{D2:LOW,LED13:OFF},pressed:{D2:HIGH,LED13:ON}}.\n"
        "Write a concise OFFICIAL STEP then ALTERNATIVES guide; do not add an external\n"
        "LED for the Uno built-in LED path. Report actual inventory gaps if any.\n"
    )
    ref = {"units": "mm", "position_tolerance_mm": 0.01, "angle_tolerance_deg": 0.1,
           "cube_centers": [[0, 0, 0], [40, 0, 0], [80, 0, 0]],
           "cube_extents": [[20, 20, 20], [20 * math.sqrt(2), 20 * math.sqrt(2), 20], [20, 20, 20]],
           "axis_plate_top_local_mm": [0, 0, .5], "axis_cone_base_local_mm": [0, 0, 0],
           "axis_plate_normal": [0, 0, 1], "axis_cone_base_normal": [0, 0, -1],
           "source_hashes": {str(p.relative_to(inputs)): digest(p) for p in inputs.rglob("*") if p.is_file()}}
    save(refs / "expected.json", ref)
    print(json.dumps({"builder_inputs": str(inputs), "references": str(refs), "files_frozen": len(ref["source_hashes"])}))


def resolve_blender(selected=None):
    """Use an explicitly selected executable or standard PATH discovery."""
    command = str(Path(selected).expanduser().resolve()) if selected is not None else "blender"
    executable = shutil.which(command)
    if executable is None:
        raise SystemExit("Blender executable unavailable. Verify the executable and pass --blender PATH, or put blender on PATH.")
    return Path(executable).resolve()


def inspect(path, output, glb=False, *, blender=None):
    cmd = [str(resolve_blender(blender)), "--background"]
    if not glb:
        cmd.append(str(path))
    cmd += ["--python", str(HERE / "inspect_benchmark_scene.py"), "--", "--output", str(output)]
    if glb:
        cmd += ["--glb", str(path)]
    run = subprocess.run(cmd, capture_output=True, text=True)
    if run.returncode or not output.exists():
        raise RuntimeError(run.stdout[-1500:] + run.stderr[-1500:])
    return json.loads(output.read_text())


def component(data, key):
    if key in data:
        return data[key]
    # GLB round trips may carry only the root name, including Blender suffixes.
    matches = [v for k, v in data.items() if k.split(".")[0] == key]
    if len(matches) == 1:
        return matches[0]
    raise KeyError(key)


def cube_check(data, ref):
    # Align one global rigid frame, allowing each cube's 24 proper symmetries.
    symmetries = []
    for permutation in itertools.permutations(range(3)):
        for signs in itertools.product((-1,1), repeat=3):
            s = np.eye(3)[:,permutation] @ np.diag(signs)
            if np.linalg.det(s) > 0:
                symmetries.append(s)
    comps = [component(data,k) for k in ("cube0","cube45","cube90")]
    matrices = [np.array(c["matrix_world_m"]) for c in comps]
    rotations = [m[:3,:3]/np.linalg.norm(m[:3,:3],axis=0) for m in matrices]
    points = [np.array(c["vertices_mm"]) for c in comps]
    centers = [np.array(c["bounds_mm"]).mean(axis=0) for c in comps]
    best = None
    for symmetry in symmetries:
        frame = rotations[0] @ symmetry
        errors = []
        for i, (pts, center, angle) in enumerate(zip(points,centers,(0,45,90))):
            key = ("cube0","cube45","cube90")[i]
            relative = frame.T @ (center-centers[0])
            if np.max(np.abs(relative-ref["cube_centers"][i])) > .01:
                errors.append(key+" relative translation")
            local = (frame.T @ (pts-centers[0]).T).T
            if np.max(np.abs(np.ptp(local,axis=0)-ref["cube_extents"][i])) > .01:
                errors.append(key+" scale/orientation")
            a = math.radians(angle)
            expected = frame @ np.array([[math.cos(a),-math.sin(a),0],[math.sin(a),math.cos(a),0],[0,0,1]])
            delta = min(math.degrees(math.acos(float(np.clip((np.trace(expected.T@rotations[i]@s)-1)/2,-1,1)))) for s in symmetries)
            if delta > .1:
                errors.append(key+" rotation")
        if best is None or len(errors)<len(best):
            best = errors
    return best


def axis_check(data, ref):
    errors = []
    a, b = component(data, "plate"), component(data, "cone")
    ma, mb = np.array(a["matrix_world_m"]), np.array(b["matrix_world_m"])
    # Normalize the actual basis: mesh imports may carry the .001 conversion
    # on their root while primitive geometry already uses meter coordinates.
    ra = ma[:3, :3] / np.linalg.norm(ma[:3, :3], axis=0)
    rb = mb[:3, :3] / np.linalg.norm(mb[:3, :3], axis=0)
    top = (ma[:3, 3] + ra @ np.array([0, 0, .0005])) * 1000
    base = mb[:3, 3] * 1000
    na, nb = ra @ [0, 0, 1], rb @ [0, 0, -1]
    na, nb = na / np.linalg.norm(na), nb / np.linalg.norm(nb)
    angle = math.degrees(math.acos(float(np.clip(na @ nb, -1, 1))))
    if np.linalg.norm(top - base) > .01:
        errors.append("face centers differ")
    if angle > .1:
        errors.append("face normals reversed/misaligned")
    # Check transformed geometric extents in the part's own frame, independently
    # of candidate dimension metadata. Equivalent global pose is allowed.
    for cid, comp, mat, expected in (("plate", a, ma, [10, 10, 1]), ("cone", b, mb, [1.6, 1.6, 4])):
        world = np.array(comp["vertices_mm"]) / 1000
        rot = mat[:3, :3] / np.linalg.norm(mat[:3, :3], axis=0)
        local = (rot.T @ (world - mat[:3, 3]).T).T * 1000
        if np.max(np.abs(np.ptp(local, axis=0) - expected)) > .01:
            errors.append(cid + " source scale")
    return errors


def source_shape_check(data, case, inputs):
    """Compare actual native-frame vertex clouds to independent supplied STLs.

    This bounds surface sampling identity; it is not a proof of solid topology.
    The renderer separately retains every STL facet without repairing sources.
    """
    import trimesh
    from scipy.spatial import cKDTree
    errors = []
    ids = ("cube0", "cube45", "cube90") if case == "cube" else ("plate", "cone")
    for cid in ids:
        comp = component(data, cid)
        mat = np.array(comp["matrix_world_m"])
        rot = mat[:3, :3] / np.linalg.norm(mat[:3, :3], axis=0)
        world = np.array(comp["vertices_mm"]) / 1000
        local = (rot.T @ (world - mat[:3, 3]).T).T * 1000
        source = inputs / "parts" / (("cube" if case == "cube" else cid) + ".stl")
        expected = np.array(trimesh.load(source, process=False).vertices)
        distance = max(cKDTree(expected).query(local)[0].max(), cKDTree(local).query(expected)[0].max())
        if distance > .01 or len(local) != len(expected):
            errors.append(cid + " sampled source geometry/facet vertices")
    return errors


def globally_reposition(data):
    """A non-symmetric rigid pose for acceptance-equivalence controls."""
    result = copy.deepcopy(data)
    a, b = math.radians(17), math.radians(23)
    rz = np.array([[math.cos(a),-math.sin(a),0],[math.sin(a),math.cos(a),0],[0,0,1]])
    rx = np.array([[1,0,0],[0,math.cos(b),-math.sin(b)],[0,math.sin(b),math.cos(b)]])
    matrix = np.eye(4)
    matrix[:3,:3] = rz @ rx
    matrix[:3,3] = [.031,-.027,.013]
    for comp in result.values():
        vertices = np.array(comp["vertices_mm"])
        vertices = (matrix[:3,:3] @ vertices.T).T + matrix[:3,3]*1000
        comp["vertices_mm"] = vertices.tolist()
        comp["bounds_mm"] = [vertices.min(axis=0).tolist(),vertices.max(axis=0).tolist()]
        if "matrix_world_m" in comp:
            comp["matrix_world_m"] = (matrix @ np.array(comp["matrix_world_m"])).tolist()
    return result


def button_check(data):
    errors = []
    bom = data.get("bom", [])
    def kind_of(p):
        value = str(p.get("kind", "")).lower().replace(" ", "_").replace("-", "_")
        if "uno" in value:
            return "arduino_uno"
        if "button" in value or "switch" in value:
            return "button"
        if "wire" in value:
            return "hookup_wire"
        return value
    resistors = [p for p in bom if kind_of(p) == "resistor"]
    if len(resistors) != 1 or resistors[0].get("id") != "R1" or resistors[0].get("value_ohm") != 10000 or resistors[0].get("quantity") != 1:
        errors.append("external 10 kohm resistor BOM")
    for kind in ("arduino_uno", "breadboard", "button", "hookup_wire"):
        # Normalize textual kinds while requiring the documented quantities.
        normalized = [part for part in bom if kind_of(part) == kind]
        count = sum(p.get("quantity", 0) for p in normalized)
        if (count < 1 if kind == "hookup_wire" else count != 1):
            errors.append("BOM quantity " + kind)
    terminals = ["UNO.5V", "UNO.GND", "UNO.D2", "SW1.A1", "SW1.A2", "SW1.B1", "SW1.B2", "R1.1", "R1.2"]
    observations = {}
    for state in ("released", "pressed"):
        parent = {t: t for t in terminals}
        def find(t):
            if t not in parent:
                parent[t] = t
            while parent[t] != t:
                t = parent[t]
            return t
        def union(a, b):
            parent[find(a)] = find(b)
        for net in data.get("nets", []):
            for t in net[1:]:
                union(net[0], t)
        union("SW1.A1", "SW1.A2")
        union("SW1.B1", "SW1.B2")
        if state == "pressed":
            union("SW1.A1", "SW1.B1")
        signal, high, ground = map(find, ("UNO.D2", "UNO.5V", "UNO.GND"))
        if high == ground:
            observations[state] = "SUPPLY_SHORT"
        elif signal == high:
            observations[state] = "HIGH"
        elif signal == ground:
            observations[state] = "LOW"
        elif resistors and {find("R1.1"), find("R1.2")} == {signal, ground}:
            observations[state] = "LOW"
        else:
            observations[state] = "FLOATING"
        expected = "LOW" if state == "released" else "HIGH"
        if observations[state] != expected:
            errors.append(state + " actual D2 " + observations[state])
        expected_led = "OFF" if expected == "LOW" else "ON"
        if data.get("states", {}).get(state) != {"D2": expected, "LED13": expected_led}:
            errors.append(state + " stated behavior")
    return errors, observations


def evaluate(run, candidate, *, blender=None):
    blender = resolve_blender(blender)
    ref = json.loads((run / "reference/expected.json").read_text())
    previous = run / "comparison.json"
    report = {"status": "holdout_first_comparison" if not previous.exists() else "holdout_repeat_evaluation",
              "cases": {}, "negative_controls": {}, "positive_controls": {}}
    candidate_hashes = {str(p.relative_to(candidate)):digest(p) for p in candidate.rglob("*") if p.is_file()}
    report["candidate_sha256"] = hashlib.sha256(json.dumps(candidate_hashes,sort_keys=True).encode()).hexdigest()
    if previous.exists():
        old = json.loads(previous.read_text())
        if old.get("candidate_sha256") and old["candidate_sha256"] != report["candidate_sha256"]:
            report["status"] = "development_candidate_changed_after_comparison"
        first = run / "comparison.first.json"
        if not first.exists():
            first.write_bytes(previous.read_bytes())
    report["inputs_unchanged"] = all(digest(run / "inputs" / p) == h for p, h in ref["source_hashes"].items())
    for case, checker in (("cube", cube_check), ("axis", axis_check)):
        saved = inspect(candidate / case / "assembly.blend", run / (case + "_scene.json"), blender=blender)
        exported = inspect(candidate / case / "assembly.glb", run / (case + "_glb.json"), True, blender=blender)
        errors = checker(saved, ref) + source_shape_check(saved, case, run / "inputs")
        report["positive_controls"][case+"_equivalent_global_pose"] = not checker(globally_reposition(saved),ref)
        if case == "cube":
            errors += ["GLB " + e for e in checker(exported, ref)]
        else:
            # glTF axes differ from Blender's; compare reimported world geometry
            # after Blender's own importer, not raw glTF node matrices.
            for cid in ("plate", "cone"):
                sb, eb = np.array(component(saved, cid)["bounds_mm"]), np.array(component(exported, cid)["bounds_mm"])
                if np.max(np.abs(sb - eb)) > .01:
                    errors.append("GLB geometry " + cid)
        report["cases"][case] = {"pass": not errors, "mismatches": errors}
        if case == "cube":
            wrong = copy.deepcopy(saved)
            wrong["cube0"]["bounds_mm"] = (np.array(wrong["cube0"]["bounds_mm"]) * 1000).tolist()
            wrong["cube0"]["vertices_mm"] = (np.array(wrong["cube0"]["vertices_mm"]) * 1000).tolist()
            report["negative_controls"]["cube_1000_scale_detected"] = bool(checker(wrong, ref))
            wrong = copy.deepcopy(saved)
            wrong["cube45"]["bounds_mm"] = [[30,-10,-10],[50,10,10]]
            a = -math.pi/4
            rotation = np.array([[math.cos(a),-math.sin(a),0],[math.sin(a),math.cos(a),0],[0,0,1]])
            wrong["cube45"]["vertices_mm"] = ((rotation @ (np.array(wrong["cube45"]["vertices_mm"])-[40,0,0]).T).T+[40,0,0]).tolist()
            m = np.array(wrong["cube45"]["matrix_world_m"])
            m[:3,:3] = rotation @ m[:3,:3]
            wrong["cube45"]["matrix_world_m"] = m.tolist()
            report["negative_controls"]["cube_wrong_rotation_detected"] = bool(checker(wrong, ref))
        else:
            wrong = copy.deepcopy(saved)
            m = np.array(wrong["cone"]["matrix_world_m"]) @ np.diag([1,-1,-1,1])
            wrong["cone"]["matrix_world_m"] = m.tolist()
            report["negative_controls"]["cone_reversed_detected"] = bool(checker(wrong, ref))
    circuit = json.loads((candidate / "button/circuit.json").read_text())
    errors, states = button_check(circuit)
    report["cases"]["button"] = {"pass": not errors, "mismatches": errors, "derived_D2": states}
    motion = json.loads((candidate / "cube/motion.json").read_text())
    # Independent analytic distance for the declared cube and obstacle. At the
    # three sampled angles, the cube's rightmost support lies inside Y=[-5,5].
    expected_clearance = [15 - 10 * (abs(math.cos(math.radians(a))) + abs(math.sin(math.radians(a))))
                          for a in (0, 45, 90)]
    motion_errors = []
    if motion.get("angles_deg") != [0,45,90] or motion.get("axis") != [0,0,1]:
        motion_errors.append("declared motion samples/axis")
    if len(motion.get("clearance_mm", [])) != 3 or np.max(np.abs(np.array(motion["clearance_mm"]) - expected_clearance)) > .01:
        motion_errors.append("oriented clearance")
    if motion.get("interference") != [False,False,False]:
        motion_errors.append("sampled interference")
    report["cases"]["cube_motion"] = {"pass": not motion_errors, "mismatches": motion_errors,
                                     "reference_clearance_mm": expected_clearance,
                                     "scope": "three samples of declared synthetic motion; no continuous or force claim"}
    for name in ("missing_resistor", "wrong_pin", "wrong_switch_group", "supply_short"):
        wrong = copy.deepcopy(circuit)
        if name == "missing_resistor":
            wrong["bom"] = [x for x in wrong["bom"] if x.get("kind") != "resistor"]
        elif name == "wrong_pin":
            wrong["nets"] = [["UNO.D3" if t == "UNO.D2" else t for t in net] for net in wrong["nets"]]
        elif name == "wrong_switch_group":
            wrong["nets"] = [[t.replace("SW1.B", "SW1.A") for t in net] for net in wrong["nets"]]
        else:
            wrong["nets"].append(["UNO.5V", "UNO.GND"])
        report["negative_controls"][name + "_detected"] = bool(button_check(wrong)[0])
    report["pass"] = report["inputs_unchanged"] and all(x["pass"] for x in report["cases"].values()) and all(report["negative_controls"].values()) and all(report["positive_controls"].values())
    save(run / "comparison.json", report)
    print(json.dumps(report, indent=2))


def main():
    p = argparse.ArgumentParser(description=__doc__)
    sub = p.add_subparsers(dest="command", required=True)
    a = sub.add_parser("prepare")
    a.add_argument("--output-dir", type=Path, required=True)
    b = sub.add_parser("evaluate")
    b.add_argument("--run", type=Path, required=True)
    b.add_argument("--candidate", type=Path, required=True)
    b.add_argument("--blender", type=Path, metavar="PATH",
                   help="verified Blender executable (default: discover blender on PATH)")
    args = p.parse_args()
    if args.command == "prepare":
        prepare(args.output_dir.resolve())
    else:
        evaluate(args.run.resolve(), args.candidate.resolve(), blender=args.blender)


if __name__ == "__main__":
    main()
