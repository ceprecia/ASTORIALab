"""Read actual saved/exported Blender geometry for the independent evaluator."""
import argparse
import json
import sys
from pathlib import Path

import bpy
from mathutils import Vector

p = argparse.ArgumentParser()
p.add_argument("--output", required=True)
p.add_argument("--glb")
args = p.parse_args(sys.argv[sys.argv.index("--") + 1:])
if args.glb:
    bpy.ops.wm.read_factory_settings(use_empty=True)
    bpy.ops.import_scene.gltf(filepath=str(Path(args.glb).resolve()))

result = {}
for obj in bpy.data.objects:
    if obj.type != "MESH":
        continue
    cid = obj.get("component_id")
    parent = obj.parent
    while not cid and parent:
        cid = parent.get("component_id")
        parent = parent.parent
    cid = str(cid or obj.name)
    points = [list(obj.matrix_world @ vertex.co) for vertex in obj.data.vertices]
    if not points:
        continue
    entry = result.setdefault(cid, {"vertices_mm": [], "objects": []})
    entry["vertices_mm"].extend([[1000 * c for c in pt] for pt in points])
    entry["objects"].append(obj.name)
for cid, entry in result.items():
    pts = entry["vertices_mm"]
    entry["bounds_mm"] = [[min(p[i] for p in pts) for i in range(3)],
                          [max(p[i] for p in pts) for i in range(3)]]
    root = bpy.data.objects.get(cid)
    if root:
        entry["matrix_world_m"] = [list(row) for row in root.matrix_world]
    entry["vertex_count"] = len(pts)
Path(args.output).write_text(json.dumps(result, indent=2))
