# Component and step manifest

Use one JSON manifest for an assembly scene. It references the existing electrical plan by path rather than repeating its netlist. Each component entry is one placed instance; repeated parts get separate stable instance IDs. Keep official BOM quantities in the owning build guide and compare them with the modeled instances explicitly. Decorative hole markers and wire paths are geometry, not additional purchased parts.

## Coordinates and evidence

- Engineering values are millimeters. The renderer converts them to Blender meters with `0.001`; glTF coordinates are meters.
- `position_mm` translates the source origin, followed by intrinsic XYZ `rotation_deg` in Blender's XYZ Euler convention. Imported meshes are never recentered. Include any source-origin compensation explicitly in the placement.
- Box and cylinder primitives are centered on their local origin. A cylinder's axis is local Z. Polyline points are local millimeter coordinates with a circular bevel.
- STL facets are read without welding, triangle removal, repair or recentering. Source files are never written. OBJ and glTF use Blender's importer; their import processing is disclosed in the summary.
- `provenance` describes geometry evidence. `source_status` describes official versus local origin. Neither establishes physical availability.
- Placement illustrates the declared transform. A plausible picture is not evidence of fit, connector mating, clearance or motion. Declare unknowns in `notes` and the written step.
- Use `relationships` and `notes` to identify each mounted part's support, separate retention method, fastener/counterpart, engagement and installation state. Missing required hardware remains an explicit incomplete interface. Include relevant heads, nuts/inserts and inserted contacts in the occupied geometry; a hole marker is not a fastener.
- Distinguish empty routing/bend/tool reservations from hardware by object name, notes and visible outline/transparency or a separate view. Include a view exposing otherwise hidden support and retention. A space budget is not an installed harness or a measured minimum clearance.

## Minimal example

```json
{
  "version": 1,
  "title": "Calibration assembly",
  "units": "mm",
  "electrical_plan": "../build_plan.json",
  "notes": ["CUSTOM DESIGN; dimensions are nominal until measured."],
  "components": [{
    "id": "calibration_cube",
    "name": "20 mm cube",
    "kind": "box",
    "size_mm": [20, 20, 20],
    "position_mm": [0, 0, 10],
    "rotation_deg": [0, 0, 0],
    "provenance": "approximate",
    "source_status": "custom",
    "inventory_status": "unconfirmed",
    "group": "calibration",
    "step": 1,
    "variant": "baseline",
    "explode_mm": [0, 0, 10]
  }],
  "views": [
    {"name": "overview", "mode": "assembled"},
    {"name": "exploded", "mode": "exploded"},
    {"name": "step_1", "mode": "step", "step": 1}
  ]
}
```

## Fields

| Field | Meaning |
| --- | --- |
| `id`, `name` | Unique simple ID and human-readable label. IDs remain stable through scene edits. |
| `kind` | `mesh`, `box`, `cylinder`, or `polyline`. |
| `provenance` | `source`, `measured`, `approximate`, or `local_alternative`. Describe the evidence in the owning guide. |
| `source_status` | Descriptive origin such as `official`, `custom`, or `local_alternative`; omission is reported as unspecified. |
| `inventory_status` | `confirmed_available`, `confirmed_missing`, or `unconfirmed`. Downloads and purchase history do not prove availability. |
| `position_mm`, `rotation_deg` | Required finite 3-vectors; unknown critical placement must be resolved or explicitly modeled as an illustration. |
| `group`, `step` | Assembly grouping and nonnegative integer introduction step. |
| `variant` | Defaults to `baseline`. Use a named alternative for proposed connectors or mounts. |
| `explode_mm` | Optional additional translation in exploded views; default zero. |
| `color` | Optional RGBA values from 0 to 1. Missing inventory always overrides this with orange transparency. |
| `mesh` fields | `source_file` relative to the manifest, `source_units` (`mm` or `m`), optional `source_sha256`. glTF requires `m`. STEP must be explicitly tessellated first. |
| `box` fields | Three positive `size_mm` values. |
| `cylinder` fields | Positive `radius_mm` and `depth_mm`. |
| `polyline` fields | At least two 3D `points_mm` and positive `radius_mm`. |
| `notes`, `relationships` | Unresolved facts and mating annotations. Retained as native scene metadata. Relationships are annotations, not solved constraints. |

Views have a filename-safe `name`, `mode` (`assembled`, `exploded`, `step`), optional `caption`, `camera` (`iso`, `top`, `front`), exact `variants` list (default `baseline`), and optional `focus_ids`. Focused views isolate and frame those components; the complete native scene remains intact. A step view requires `step`; later parts are hidden, the current step is gold, and earlier parts are faded. Assembled and step views share framing unless focused explicitly. Exploded views are reframed. Framing reserves clear header/footer bands. Named variants are included only when the view selects them; include `baseline` alongside an additive alternative when needed.

The saved scene and GLB use an assembled view selecting only `baseline` without `focus_ids` (prefer `overview`), or a generated full baseline overview. When an existing `overview` selects additional context, the generated canonical PNG is named `baseline_overview.png`. Alternative geometry remains editable but hidden in the native scene. GLB contains the complete baseline. Make a separately named export when an alternative must be shared. Rendered notes show up to four wrapped lines; the complete notes remain in scene metadata and summary. No fit, motion or wiring solver is implied by this renderer.

## Commands and outputs

Set `BLENDER_EXECUTABLE` to the verified executable on the current host. Check its version before rendering. The bundled renderer targets Blender 4.5 LTS.

```sh
python3 scripts/validate_manifest.py /absolute/path/assembly_manifest.json
"$BLENDER_EXECUTABLE" --background --python scripts/render_scene.py -- --manifest /absolute/path/assembly_manifest.json --output-dir /absolute/path/model_3d
```

Run from this skill directory or use absolute script paths. Optional `--samples 16`, `--resolution 900` (width; height is 80%), and `--only-view overview` control rendering. Rendering uses CPU Cycles with a fixed seed. Reopening the saved file reproduces the canonical view:

```sh
"$BLENDER_EXECUTABLE" --background /absolute/path/model_3d/assembly.blend --render-output /tmp/reopened --render-format PNG --render-frame 1
```

Outputs are editable `assembly.blend`, portable `assembly.glb`, view PNGs and `model_summary.json`. The summary records actual evaluated world-space geometry bounds in mm, actual Blender root matrices in meters, source hashes, import processing, uncertainty and rendered view membership. Each root is named by its ID; roots and geometry carry `component_id`, `provenance`, `inventory_status`, and `source_status`. Roots retain the full component entry, including optional `guide_step_refs`; step references also appear in the summary. These are model metadata, not a physical acceptance certificate. Keep temporary test reports outside the vault.
