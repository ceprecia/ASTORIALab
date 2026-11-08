#!/usr/bin/env python3
"""Build an editable Blender scene and render component/assembly-step views.

Run with Blender 4.5 LTS, not the engineering environment's Python:
  blender --background --python render_scene.py -- --manifest MODEL.json --output-dir OUT
Requirements: Blender bpy, the neighboring stdlib manifest validator.
Author: Codex, 2026-10-25. All engineering lengths are mm; Blender/glTF use m.
Imported sources are never recentered, repaired or written back by this script.
"""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
import math
from pathlib import Path
import struct
import sys
import textwrap

import bpy
from mathutils import Vector

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
from validate_manifest import validate_manifest

MM = 0.001
roots = {}
specs = {}
base_materials = {}
helpers = []


def material(name, rgba):
    mat = bpy.data.materials.new(name)
    mat.diffuse_color = rgba
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes.get("Principled BSDF")
    bsdf.inputs["Base Color"].default_value = rgba
    bsdf.inputs["Roughness"].default_value = 0.65
    bsdf.inputs["Alpha"].default_value = rgba[3]
    if hasattr(mat, "surface_render_method"):
        mat.surface_render_method = "DITHERED"
    return mat


def component_color(component):
    if component["inventory_status"] == "confirmed_missing":
        return (0.95, 0.32, 0.08, 0.25)
    if "color" in component:
        return tuple(component["color"])
    if component["provenance"] == "approximate":
        return (0.56, 0.64, 0.70, 0.4)
    if component["provenance"] == "local_alternative":
        return (0.77, 0.50, 0.22, 1.0)
    return (0.18, 0.48, 0.60, 1.0)


def descendants(root):
    result = [root]
    for child in root.children:
        result.extend(descendants(child))
    return result


def import_stl_unchanged(source):
    """Read every source facet without welding, removing or recentering it."""
    data = source.read_bytes()
    count = struct.unpack_from("<I", data, 80)[0] if len(data) >= 84 else 0
    if len(data) == 84 + count * 50:
        vertices = [tuple(struct.unpack_from("<3f", data, 84 + face * 50 + 12 + vertex * 12))
                    for face in range(count) for vertex in range(3)]
    else:
        vertices = []
        for line in data.decode("ascii").splitlines():
            fields = line.split()
            if fields and fields[0].lower() == "vertex":
                vertices.append(tuple(float(value) for value in fields[1:4]))
    if not vertices or len(vertices) % 3:
        raise ValueError(str(source) + ": STL must contain complete triangles")
    faces = [(index, index + 1, index + 2) for index in range(0, len(vertices), 3)]
    mesh = bpy.data.meshes.new(source.stem)
    mesh.from_pydata(vertices, [], faces)
    mesh.update()
    obj = bpy.data.objects.new(source.stem, mesh)
    bpy.context.scene.collection.objects.link(obj)
    obj["source_triangle_count"] = len(faces)
    obj["import_processing"] = "Every STL triangle retained; no welding, repair or recentering"


def make_component(component, directory):
    cid = component["id"]
    root = bpy.data.objects.new(cid, None)
    bpy.context.scene.collection.objects.link(root)
    geometry = []
    kind = component["kind"]
    if kind == "mesh":
        source = (directory / component["source_file"]).resolve()
        before = set(bpy.data.objects)
        if source.suffix.lower() == ".stl":
            import_stl_unchanged(source)
        elif source.suffix.lower() == ".obj":
            bpy.ops.wm.obj_import(filepath=str(source))
        else:
            bpy.ops.import_scene.gltf(filepath=str(source))
        added = set(bpy.data.objects) - before
        geometry = [obj for obj in added if obj.type in {"MESH", "CURVE"}]
        if not geometry:
            raise ValueError(cid + ": import produced no mesh geometry")
        # Keep the source hierarchy/local origins. Only attach imported root nodes.
        for obj in added:
            if obj.parent not in added:
                matrix = obj.matrix_world.copy()
                obj.parent = root
                obj.matrix_world = matrix
        root.scale = (MM, MM, MM) if component["source_units"] == "mm" else (1, 1, 1)
        for obj in list(added):
            if obj.type in {"CAMERA", "LIGHT"}:
                bpy.data.objects.remove(obj, do_unlink=True)
    elif kind == "box":
        bpy.ops.mesh.primitive_cube_add(size=1)
        obj = bpy.context.object
        obj.dimensions = Vector(component["size_mm"]) * MM
        bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
        obj.parent = root
        geometry = [obj]
    elif kind == "cylinder":
        bpy.ops.mesh.primitive_cylinder_add(vertices=48,
            radius=component["radius_mm"] * MM, depth=component["depth_mm"] * MM)
        obj = bpy.context.object
        obj.parent = root
        geometry = [obj]
    else:
        curve = bpy.data.curves.new(cid + "_path", "CURVE")
        curve.dimensions = "3D"
        curve.resolution_u = 2
        curve.bevel_depth = component["radius_mm"] * MM
        curve.bevel_resolution = 2
        spline = curve.splines.new("POLY")
        spline.points.add(len(component["points_mm"]) - 1)
        for point, xyz in zip(spline.points, component["points_mm"]):
            point.co = (*[x * MM for x in xyz], 1)
        obj = bpy.data.objects.new(cid + "_wire", curve)
        bpy.context.scene.collection.objects.link(obj)
        obj.parent = root
        geometry = [obj]
    mat = material(cid + "_material", component_color(component))
    for index, obj in enumerate(geometry):
        obj.name = cid + "_geometry_" + str(index)
        obj.data.materials.clear()
        obj.data.materials.append(mat)
    root.location = Vector(component["position_mm"]) * MM
    root.rotation_euler = [math.radians(a) for a in component["rotation_deg"]]
    for key in ("name", "provenance", "inventory_status", "source_status", "group", "step", "variant"):
        root[key] = component.get(key, "baseline" if key == "variant" else "unspecified")
    root["engineering_units"] = "mm"
    root["component_manifest"] = json.dumps(component)
    root["guide_step_refs"] = json.dumps(component.get("guide_step_refs", []))
    if component.get("source_file"):
        root["source_file"] = component["source_file"]
    for obj in descendants(root):
        obj["component_id"] = cid
        for key in ("provenance", "inventory_status", "source_status"):
            obj[key] = component.get(key, "unspecified")
    roots[cid] = root
    specs[cid] = component
    base_materials[cid] = mat


def visible_geometry(root):
    return [obj for obj in descendants(root) if obj.type in {"MESH", "CURVE"}]


def world_corners(root):
    points = []
    for obj in visible_geometry(root):
        points.extend(obj.matrix_world @ Vector(corner) for corner in obj.bound_box)
    return points


def world_geometry_points(root):
    points = []
    graph = bpy.context.evaluated_depsgraph_get()
    for obj in visible_geometry(root):
        evaluated = obj.evaluated_get(graph)
        mesh = evaluated.to_mesh()
        if mesh:
            points.extend(evaluated.matrix_world @ vertex.co for vertex in mesh.vertices)
            evaluated.to_mesh_clear()
    return points


def bounds(points):
    return ([min(point[i] for point in points) for i in range(3)],
            [max(point[i] for point in points) for i in range(3)])


def summary():
    bpy.context.view_layer.update()
    items = []
    for cid, root in roots.items():
        low, high = bounds(world_geometry_points(root))
        component = specs[cid]
        item = {"id": cid, "name": component["name"],
                "position_mm": [x / MM for x in root.matrix_world.translation],
                "rotation_deg": [math.degrees(x) for x in root.rotation_euler],
                "matrix_world_m": [list(row) for row in root.matrix_world],
                "root_scale": list(root.scale),
                "bbox_min_mm": [x / MM for x in low],
                "bbox_max_mm": [x / MM for x in high],
                "bounds_mm": [(b - a) / MM for a, b in zip(low, high)],
                "provenance": component["provenance"],
                "inventory_status": component["inventory_status"],
                "source_status": component.get("source_status", "unspecified"),
                "variant": component.get("variant", "baseline"),
                "group": component.get("group", "assembly"),
                "step": component["step"]}
        item["guide_step_refs"] = component.get("guide_step_refs", [])
        if "source_file" in component:
            item["source_file"] = component["source_file"]
            item["import_processing"] = ("STL facets retained without welding, repair or recentering"
                if Path(component["source_file"]).suffix.lower() == ".stl"
                else "Blender importer; source file unchanged; native local coordinates retained")
        meshes = [obj.data for obj in visible_geometry(root) if obj.type == "MESH"]
        for mesh in meshes:
            mesh.calc_loop_triangles()
        item["mesh_triangle_count"] = sum(len(mesh.loop_triangles) for mesh in meshes)
        items.append(item)
    return {"engineering_units": "mm", "blender_units": "m", "components": items,
            "provenance_counts": dict(Counter(x["provenance"] for x in items)),
            "inventory_counts": dict(Counter(x["inventory_status"] for x in items)),
            "meaning": "Saved model geometry/placement only; not physical fit or function."}


def set_view(view):
    selected = set(view.get("variants", ["baseline"]))
    mode = view["mode"]
    current_step = view.get("step", 10**9)
    shown = []
    for cid, root in roots.items():
        component = specs[cid]
        visible = component.get("variant", "baseline") in selected
        if "focus_ids" in view:
            visible = visible and cid in view["focus_ids"]
        if mode == "step":
            visible = visible and component["step"] <= current_step
        for obj in descendants(root):
            obj.hide_render = not visible
            obj.hide_viewport = not visible
        location = Vector(component["position_mm"])
        if mode == "exploded":
            location += Vector(component.get("explode_mm", [0, 0, 0]))
        root.location = location * MM
        mat = base_materials[cid]
        rgba = component_color(component)
        if visible and mode == "step" and component["step"] == current_step and component["inventory_status"] != "confirmed_missing":
            rgba = (0.96, 0.67, 0.10, 1)
        elif visible and mode == "step" and component["step"] < current_step:
            rgba = (rgba[0], rgba[1], rgba[2], min(rgba[3], 0.28))
        mat.diffuse_color = rgba
        mat.node_tree.nodes.get("Principled BSDF").inputs["Base Color"].default_value = rgba
        mat.node_tree.nodes.get("Principled BSDF").inputs["Alpha"].default_value = rgba[3]
        if visible:
            shown.append(cid)
    bpy.context.view_layer.update()
    return shown


def caption_lines(manifest, view):
    notes = ([view["caption"]] if view.get("caption") else []) + manifest.get("notes", [])
    return [line for note in notes for line in textwrap.wrap(note, width=105)][:4]


def caption_bottom(manifest, view):
    maximum_lines = max([len(caption_lines(manifest, candidate))
                         for candidate in manifest.get("views", [])] +
                        [len(caption_lines(manifest, view))])
    return .38 - maximum_lines * .025 - .015


def camera_for_view(view, shown, manifest):
    # Step views share a frame with their assembled view unless explicitly focused.
    selected = set(view.get("variants", ["baseline"]))
    frame_ids = [cid for cid, component in specs.items()
                 if component.get("variant", "baseline") in selected]
    focus = view.get("focus_ids", frame_ids)
    points = [point for cid in focus if cid in frame_ids for point in world_corners(roots[cid])]
    if not points:
        raise ValueError(view["name"] + ": no visible geometry to frame")
    low, high = bounds(points)
    center = (Vector(low) + Vector(high)) / 2
    radius = max((Vector(high) - Vector(low)).length, 0.005)
    direction = {"iso": Vector((1.35, -1.8, 1.5)),
                 "top": Vector((0, 0, 2)), "front": Vector((0, -2, 0.5))}[view.get("camera", "iso")]
    camera = bpy.data.objects.get("_model_camera")
    if camera is None:
        bpy.ops.object.camera_add()
        camera = bpy.context.object
        camera.name = "_model_camera"
    camera.location = center + direction.normalized() * radius * 2.5
    camera.rotation_euler = (center - camera.location).to_track_quat("-Z", "Y").to_euler()
    camera.data.type = "ORTHO"
    local = camera.rotation_euler.to_matrix().inverted()
    projected = [local @ (point - center) for point in points]
    aspect = bpy.context.scene.render.resolution_x / bpy.context.scene.render.resolution_y
    span_x = max(point.x for point in projected) - min(point.x for point in projected)
    span_y = max(point.y for point in projected) - min(point.y for point in projected)
    # Reserve annotation bands, then center the geometry in the remaining image.
    body_top = caption_bottom(manifest, view) - .02
    body_bottom = -.37
    body_height = body_top - body_bottom
    camera.data.ortho_scale = max(span_x / .9, span_y * aspect / body_height, .01) * 1.08
    projected_x = (max(point.x for point in projected) + min(point.x for point in projected)) / 2
    projected_y = (max(point.y for point in projected) + min(point.y for point in projected)) / 2
    body_center_y = (body_top + body_bottom) / 2 * camera.data.ortho_scale / aspect
    orientation = camera.rotation_euler.to_matrix()
    camera.location += orientation @ Vector((projected_x, projected_y - body_center_y, 0))
    camera.data.clip_start = min(0.001, radius / 100)
    camera.data.clip_end = radius * 50 + 10
    bpy.context.scene.camera = camera
    return camera, center, radius


def make_text(camera, body, y_fraction, size_fraction, color):
    data = bpy.data.curves.new("_caption_font", "FONT")
    data.body = body
    data.align_x = "LEFT"
    data.align_y = "TOP_BASELINE"
    data.size = camera.data.ortho_scale * size_fraction
    obj = bpy.data.objects.new("_caption", data)
    bpy.context.scene.collection.objects.link(obj)
    obj.parent = camera
    aspect = bpy.context.scene.render.resolution_x / bpy.context.scene.render.resolution_y
    obj.location = (-camera.data.ortho_scale * 0.47,
                    camera.data.ortho_scale / aspect * y_fraction, -0.01)
    mat = bpy.data.materials.new("_caption_emission")
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    nodes.clear()
    output = nodes.new("ShaderNodeOutputMaterial")
    emission = nodes.new("ShaderNodeEmission")
    emission.inputs["Color"].default_value = (*color, 1)
    mat.node_tree.links.new(emission.outputs[0], output.inputs["Surface"])
    data.materials.append(mat)
    helpers.append(obj)


def caption_panel(camera, bottom, top):
    """Keep annotations legible when focused geometry extends behind them."""
    width = camera.data.ortho_scale
    height = width * bpy.context.scene.render.resolution_y / bpy.context.scene.render.resolution_x
    bpy.ops.mesh.primitive_plane_add(size=1)
    panel = bpy.context.object
    panel.name = "_caption_panel"
    panel.parent = camera
    panel.location = (0, (bottom + top) * height / 2, -0.011)
    panel.scale = (width, (top - bottom) * height, 1)
    mat = bpy.data.materials.new("_caption_panel_white")
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    nodes.clear()
    output = nodes.new("ShaderNodeOutputMaterial")
    emission = nodes.new("ShaderNodeEmission")
    emission.inputs["Color"].default_value = (1, 1, 1, 1)
    mat.node_tree.links.new(emission.outputs[0], output.inputs["Surface"])
    panel.data.materials.append(mat)
    for visibility in ("visible_diffuse", "visible_glossy", "visible_transmission", "visible_shadow"):
        if hasattr(panel, visibility):
            setattr(panel, visibility, False)
    helpers.append(panel)


def setup_lighting(center, radius):
    for obj in list(bpy.data.objects):
        if obj.type == "LIGHT":
            bpy.data.objects.remove(obj, do_unlink=True)
    for direction, power in [((1, -1.5, 2.5), 1.2), ((-2, 1, 1.5), 0.7)]:
        bpy.ops.object.light_add(type="AREA", location=center + Vector(direction) * radius)
        light = bpy.context.object
        light.data.energy = power * max(radius / 0.15, 0.1)**2
        light.data.shape = "DISK"
        light.data.size = radius * 2
        light.rotation_euler = (center - light.location).to_track_quat("-Z", "Y").to_euler()


def add_captions(camera, manifest, view):
    for obj in helpers:
        bpy.data.objects.remove(obj, do_unlink=True)
    helpers.clear()
    lines = caption_lines(manifest, view)
    caption_panel(camera, caption_bottom(manifest, view), .5)
    caption_panel(camera, -.5, -.39)
    make_text(camera, "MODEL RENDER | " + view["name"].replace("_", " "), .46, .027, (.05, .09, .12))
    make_text(camera, manifest["title"][:80], .42, .018, (.15, .20, .24))
    for index, line in enumerate(lines):
        make_text(camera, line, .38 - index * .025, .013, (.15, .20, .24))
    make_text(camera, "Gray: approximate | Orange ghost: missing | Fit/function remain unverified", -.42, .015, (.15, .20, .24))


def main():
    argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", required=True, type=Path)
    parser.add_argument("--output-dir", required=True, type=Path)
    parser.add_argument("--resolution", type=int, default=900)
    parser.add_argument("--samples", type=int, default=16)
    parser.add_argument("--only-view", help="Render one named view; scene/GLB still saved")
    args = parser.parse_args(argv)
    if args.samples < 1 or args.resolution < 64:
        parser.error("samples must be positive and resolution must be at least 64 pixels")
    report = validate_manifest(args.manifest)
    if not report["ok"]:
        raise ValueError(json.dumps(report, indent=2))
    manifest_path = args.manifest.resolve()
    manifest = json.loads(manifest_path.read_text())
    out = args.output_dir.resolve()
    views = manifest.get("views", [{"name": "overview", "mode": "assembled"}])
    if args.only_view and args.only_view not in {view["name"] for view in views}:
        parser.error("only-view must name a declared view")
    output_paths = {out / name for name in ("assembly.blend", "assembly.glb", "model_summary.json")}
    output_paths.update(out / (view["name"] + ".png") for view in views)
    protected = {Path(item["path"]) for item in report["sources"]} | {manifest_path}
    if output_paths & protected:
        raise ValueError("Output paths overlap a source or the manifest; use another output directory")
    out.mkdir(parents=True, exist_ok=True)
    bpy.context.preferences.filepaths.save_version = 0
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete(use_global=False)
    scene = bpy.context.scene
    scene.unit_settings.system = "METRIC"
    scene.unit_settings.scale_length = 1.0
    scene.render.engine = "CYCLES"
    scene.cycles.device = "CPU"
    scene.cycles.samples = args.samples
    scene.cycles.seed = 0
    scene.cycles.use_denoising = False
    scene.render.resolution_x = args.resolution
    scene.render.resolution_y = round(args.resolution * 0.8)
    scene.render.resolution_percentage = 100
    scene.render.image_settings.file_format = "PNG"
    scene.render.film_transparent = False
    # A white camera background and dimmer ambient illumination preserve part colors.
    scene.world.use_nodes = True
    nodes = scene.world.node_tree.nodes
    nodes.clear()
    output = nodes.new("ShaderNodeOutputWorld")
    ambient = nodes.new("ShaderNodeBackground")
    ambient.inputs["Color"].default_value = (.7, .8, 1, 1)
    ambient.inputs["Strength"].default_value = .3
    white = nodes.new("ShaderNodeBackground")
    white.inputs["Color"].default_value = (1, 1, 1, 1)
    rays = nodes.new("ShaderNodeLightPath")
    mix = nodes.new("ShaderNodeMixShader")
    scene.world.node_tree.links.new(rays.outputs["Is Camera Ray"], mix.inputs[0])
    scene.world.node_tree.links.new(ambient.outputs[0], mix.inputs[1])
    scene.world.node_tree.links.new(white.outputs[0], mix.inputs[2])
    scene.world.node_tree.links.new(mix.outputs[0], output.inputs[0])
    scene.view_settings.view_transform = "Standard"
    scene.view_settings.look = "None"
    for component in manifest["components"]:
        make_component(component, manifest_path.parent)
    model_data = summary()
    model_data["title"] = manifest["title"]
    model_data["manifest_sha256"] = hashlib.sha256(manifest_path.read_bytes()).hexdigest()
    model_data["sources"] = report["sources"]
    model_data["uncertainty"] = report["uncertainty"]
    model_data["notes"] = manifest.get("notes", [])
    model_data["relationships"] = manifest.get("relationships", [])
    scene["model_manifest_sha256"] = model_data["manifest_sha256"]
    scene["model_render_note"] = "Geometry illustration; unknown fit/forces remain unverified"
    scene["model_notes"] = json.dumps(manifest.get("notes", []))
    scene["model_relationships"] = json.dumps(manifest.get("relationships", []))
    full_baseline_views = [view for view in views if view["mode"] == "assembled" and
                           view.get("variants", ["baseline"]) == ["baseline"] and
                           "focus_ids" not in view]
    baseline = next((view for view in full_baseline_views if view["name"] == "overview"),
                    full_baseline_views[0] if full_baseline_views else
                    {"name": "baseline_overview" if any(view["name"] == "overview" for view in views)
                     else "overview", "mode": "assembled", "variants": ["baseline"]})
    if baseline not in views:
        occupied = {view["name"] for view in views}
        stem = baseline["name"]
        suffix = 2
        while baseline["name"] in occupied:
            baseline["name"] = stem + "_" + str(suffix)
            suffix += 1
        if out / (baseline["name"] + ".png") in protected:
            raise ValueError("Canonical render would overwrite a source; use another output directory")
        views = views + [baseline]
    shown = set_view(baseline)
    camera, center, radius = camera_for_view(baseline, shown, manifest)
    setup_lighting(center, radius)
    add_captions(camera, manifest, baseline)
    scene.render.filepath = str(out / (baseline["name"] + ".png"))
    scene["canonical_view"] = json.dumps(baseline)
    bpy.ops.wm.save_as_mainfile(filepath=str(out / "assembly.blend"))
    bpy.ops.object.select_all(action="DESELECT")
    for cid in shown:
        for obj in descendants(roots[cid]):
            obj.select_set(True)
    bpy.ops.export_scene.gltf(filepath=str(out / "assembly.glb"), export_format="GLB",
                              use_selection=True, export_apply=True, export_extras=True)
    (out / "model_summary.json").write_text(json.dumps(model_data, indent=2) + "\n")
    view_results = []
    for view in views:
        if args.only_view and view["name"] != args.only_view:
            continue
        shown = set_view(view)
        camera, center, radius = camera_for_view(view, shown, manifest)
        setup_lighting(center, radius)
        add_captions(camera, manifest, view)
        scene.render.filepath = str(out / (view["name"] + ".png"))
        bpy.ops.render.render(write_still=True)
        view_results.append({"name": view["name"], "mode": view["mode"], "components": shown,
                             "caption": view.get("caption", ""),
                             "guide_step_refs": view.get("guide_step_refs", []),
                             "camera_matrix_world_m": [list(row) for row in camera.matrix_world],
                             "camera_ortho_scale_m": camera.data.ortho_scale})
    model_data["views"] = view_results
    (out / "model_summary.json").write_text(json.dumps(model_data, indent=2) + "\n")
    print(json.dumps({"ok": True, "components": len(roots), "views": view_results,
                      "output_dir": str(out), "source_files_unchanged":
                      all(hashlib.sha256(Path(item["path"]).read_bytes()).hexdigest() == item["sha256"]
                          for item in report["sources"])}))


if __name__ == "__main__":
    main()
