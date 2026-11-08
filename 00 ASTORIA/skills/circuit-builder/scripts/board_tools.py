"""circuit-builder helpers: hole geometry, wire lengths, build order, continuity checks, layout check.

Import from Python (sys.path.insert(0, '<skill>/scripts'); from board_tools import *) or run
    python3 board_tools.py plan.json
where plan.json holds {board, parts, wires, rails, pins, components, joins, polarised, headers}
to print the build steps, the continuity table and the layout-check findings as Markdown.
"""
import math
import re

# Board geometries in mm. Rows: y = row0 + pitch*(row-1). Columns: letter -> x.
# Rails: name -> x (holes at every row y). Hole notation: "C14", "R2@28", "L1@15".
BOARDS = {
    "electrocookie_half": {
        "size_mm": (52.07, 88.90), "rows": 30, "row0": 7.60, "pitch": 2.54,
        "columns": {"A": 12.16, "B": 14.69, "C": 17.24, "D": 19.77, "E": 22.31,
                    "F": 29.94, "G": 32.47, "H": 35.02, "I": 37.55, "J": 40.09},
        "strips": (("A", "B", "C", "D", "E"), ("F", "G", "H", "I", "J")),
        "rails": {"L1": 2.64, "L2": 5.18, "R1": 47.09, "R2": 49.63},
        "rail_names": {"L1": "left outer", "L2": "left inner", "R1": "right inner", "R2": "right outer"},
        "taps": "pairs at each end of the centre channel: top left = L1, top right = R1, bottom left = L2, bottom right = R2",
        "tap_holes": {"TL": (24.86, 2.52, "L1"), "TR": (27.40, 2.52, "R1"), "BL": (24.86, 86.34, "L2"), "BR": (27.40, 86.34, "R2")},
        "mount_holes": "M3 on the centre line at rows 1 and 30",
    },
    "permaproto_half": {
        "size_mm": (55.9, 81.3), "rows": 30, "row0": 6.35, "pitch": 2.54,
        "columns": {"A": 13.97, "B": 16.51, "C": 19.05, "D": 21.59, "E": 24.13,
                    "F": 31.75, "G": 34.29, "H": 36.83, "I": 39.37, "J": 41.91},
        "strips": (("A", "B", "C", "D", "E"), ("F", "G", "H", "I", "J")),
        "rails": {"L1": 3.81, "L2": 6.35, "R1": 49.53, "R2": 52.07},
        "rail_names": {"L1": "left outer", "L2": "left inner", "R1": "right inner", "R2": "right outer"},
        "taps": "none; rails are plain strips",
        "mount_holes": "four corner holes, M2.5",
    },
}

def _finite_number(value):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return False
    try:
        return math.isfinite(value)
    except OverflowError:
        return False


def _validate_custom_geometry(geometry):
    prefix = "Invalid custom board geometry: "
    required = {"size_mm", "rows", "row0", "pitch", "columns", "strips", "rails"}
    missing = sorted(required - geometry.keys())
    if missing:
        raise ValueError(prefix + "supply " + ", ".join(missing))

    size = geometry["size_mm"]
    if not isinstance(size, (list, tuple)) or len(size) != 2 or not all(
            _finite_number(value) and value > 0 for value in size):
        raise ValueError(prefix + "size_mm must contain two positive finite dimensions")
    width, height = size
    rows = geometry["rows"]
    if isinstance(rows, bool) or not isinstance(rows, int) or rows < 1:
        raise ValueError(prefix + "rows must be a positive integer")
    row0, pitch = geometry["row0"], geometry["pitch"]
    if not _finite_number(row0) or not 0 <= row0 <= height:
        raise ValueError(prefix + "row0 must be a finite position within the board height")
    if not _finite_number(pitch) or pitch <= 0:
        raise ValueError(prefix + "pitch must be positive and finite")
    if rows - 1 > (height - row0) / pitch + 1e-9:
        raise ValueError(prefix + "the final row exceeds the board height")

    columns, rails = geometry["columns"], geometry["rails"]
    if not isinstance(columns, dict) or not columns or any(
            not isinstance(label, str) or not re.fullmatch(r"[A-Z]", label)
            or not _finite_number(x) or not 0 <= x <= width for label, x in columns.items()):
        raise ValueError(prefix + "columns must map A-Z labels to finite positions within the board width")
    if not isinstance(rails, dict) or any(
            label not in {"L1", "L2", "R1", "R2"} or not _finite_number(x)
            or not 0 <= x <= width for label, x in rails.items()):
        raise ValueError(prefix + "rails must map L1, L2, R1 or R2 to finite positions within the board width")
    strips = geometry["strips"]
    if not isinstance(strips, (list, tuple)):
        raise ValueError(prefix + "strips must be a list of column groups")
    joined_columns = set()
    for strip in strips:
        if not isinstance(strip, (list, tuple)) or not strip or any(
                not isinstance(column, str) or column not in columns for column in strip):
            raise ValueError(prefix + "each strip must name existing columns")
        group = set(strip)
        if len(group) != len(strip) or joined_columns & group:
            raise ValueError(prefix + "a column may occur only once across strips")
        joined_columns.update(group)

    taps = geometry.get("tap_holes", {})
    if not isinstance(taps, dict):
        raise ValueError(prefix + "tap_holes must map tap labels to x, y and an existing rail")
    for label, location in taps.items():
        if label not in {"TL", "TR", "BL", "BR"} or not isinstance(location, (list, tuple)) or len(location) != 3:
            raise ValueError(prefix + "a tap needs TL, TR, BL or BR and an x, y, rail triple")
        x, y, rail = location
        if not (_finite_number(x) and 0 <= x <= width and _finite_number(y) and 0 <= y <= height
                and isinstance(rail, str) and rail in rails):
            raise ValueError(prefix + "tap positions must be on the board and reference an existing rail")
    lanes_by_x = {}
    for label, x in (*columns.items(), *rails.items()):
        if x in lanes_by_x:
            raise ValueError(prefix + f"lanes {lanes_by_x[x]} and {label} share a physical hole position")
        lanes_by_x[x] = label

    tap_positions = {}
    for label, (x, y, _) in taps.items():
        if (x, y) in tap_positions:
            raise ValueError(prefix + f"taps {tap_positions[x, y]} and {label} share a physical hole position")
        tap_positions[x, y] = label

    grid_taps = [(lanes_by_x[x], y, label) for (x, y), label in tap_positions.items() if x in lanes_by_x]
    try:
        last_y = row0 + pitch * (rows - 1)
    except OverflowError:
        raise ValueError(prefix + "row coordinates must be representable") from None
    if not _finite_number(last_y):
        raise ValueError(prefix + "row coordinates must be representable")

    previous_y = None
    for row in range(1, rows + 1):
        y = row0 + pitch * (row - 1)
        if y == previous_y:
            raise ValueError(prefix + f"rows {row - 1} and {row} share a physical hole position")
        previous_y = y
        for lane, tap_y, label in grid_taps:
            # Allow only arithmetic roundoff when comparing a tap to a calculated row.
            if math.isclose(y, tap_y, rel_tol=1e-15, abs_tol=0.0):
                hole = f"{lane}{row}" if lane in columns else f"{lane}@{row}"
                raise ValueError(prefix + f"tap {label} and {hole} share a physical hole position")
    return geometry


def board_geometry(name=None):
    """Resolve a selected preset name or an explicitly supplied verified geometry."""
    if name is None:
        raise ValueError("Explicit verified board geometry is required. Select electrocookie_half, permaproto_half, or supply a verified geometry dict.")
    if isinstance(name, dict):
        return _validate_custom_geometry(name)
    if not isinstance(name, str):
        raise ValueError("Explicit verified board geometry must be a supported preset name or a verified geometry dict.")
    if name not in BOARDS:
        raise KeyError("unknown board %r; known: %s" % (name, sorted(BOARDS)))
    return BOARDS[name]

def parse_hole(hole):
    """'C14' -> ('col','C',14); 'R2@28' -> ('rail','R2',28); 'TL' -> ('tap','TL',0) (ElectroCookie rail taps)."""
    h = hole.strip().upper().replace(" ", "")
    if h in ("TL", "TR", "BL", "BR"):
        return ("tap", h, 0)
    m = re.fullmatch(r"([A-Z])(\d+)", h)
    if m:
        return ("col", m.group(1), int(m.group(2)))
    m = re.fullmatch(r"([LR][12])@(\d+)", h)
    if m:
        return ("rail", m.group(1), int(m.group(2)))
    raise ValueError("hole %r: use 'C14' or 'R2@28'" % hole)

def hole_xy(hole, board=None):
    """(x, y) in mm of a hole, origin at the board's top-left corner, row 1 at the top."""
    g = board_geometry(board)
    kind, name, row = parse_hole(hole)
    if kind == "tap":
        x, y, _ = g["tap_holes"][name]
        return (x, y)
    if not 1 <= row <= g["rows"]:
        raise ValueError("row %d outside 1..%d" % (row, g["rows"]))
    x = g["columns"][name] if kind == "col" else g["rails"][name]
    return (x, g["row0"] + g["pitch"] * (row - 1))

def same_node(a, b, board=None):
    """True if two holes are already joined by the board's copper (same strip or same rail)."""
    g = board_geometry(board)
    ka, na, ra = parse_hole(a)
    kb, nb, rb = parse_hole(b)
    if ka == "tap":
        ka, na = "rail", g["tap_holes"][na][2]
    if kb == "tap":
        kb, nb = "rail", g["tap_holes"][nb][2]
    if ka == "rail" and kb == "rail":
        return na == nb
    if ka == "col" and kb == "col" and ra == rb:
        return any(na in s and nb in s for s in g["strips"])
    return False

def wire_length_mm(a, b, board=None, slack=8.0):
    """Bare-to-bare cut length for a flat wire between two holes: straight distance plus slack
    for the two 3 mm legs that go through the board."""
    (x1, y1), (x2, y2) = hole_xy(a, board), hole_xy(b, board)
    return round(math.hypot(x2 - x1, y2 - y1) + slack)

def _module_bounds(covers, geometry):
    """Resolve either supported cover form against the verified board."""
    if not isinstance(covers, dict):
        raise ValueError("module cover must be an object")
    margin = covers.get("margin_mm", 3.0)
    if not _finite_number(margin) or margin < 0:
        raise ValueError("module cover margin_mm must be finite and nonnegative")
    if "holes" in covers:
        holes = covers["holes"]
        if not isinstance(holes, (list, tuple)) or not holes:
            raise ValueError("module cover holes must be a nonempty list of board holes")
        xs, ys = zip(*(_require_layout_hole("module cover", hole, geometry) for hole in holes))
        x1, x2, y1, y2 = min(xs), max(xs), min(ys), max(ys)
    else:
        rows, cols = covers.get("rows"), covers.get("cols")
        if (not isinstance(rows, (list, tuple)) or len(rows) != 2
                or any(not re.fullmatch(r"\d+", str(row).strip()) for row in rows)):
            raise ValueError("module cover rows must name two board rows")
        row1, row2 = (int(str(row).strip()) for row in rows)
        if not 1 <= row1 <= row2 <= geometry["rows"]:
            raise ValueError("module cover rows must be ordered and within the verified board")
        lanes = {**geometry["columns"], **geometry["rails"]}
        if (not isinstance(cols, (list, tuple)) or len(cols) != 2
                or any(not isinstance(col, str) or col not in lanes for col in cols)):
            raise ValueError("module cover cols must name two verified board columns or rails")
        x1, x2 = sorted(lanes[col] for col in cols)
        y1, y2 = (geometry["row0"] + geometry["pitch"] * (row - 1) for row in (row1, row2))
    return x1 - margin, x2 + margin, y1 - margin, y2 + margin


def hole_under_module(hole, module, board=None):
    """Test a board hole against a module cover specified by rows/cols or holes."""
    g = board_geometry(board)
    x1, x2, y1, y2 = _module_bounds(module, g)
    x, y = hole_xy(hole, g)
    return x1 <= x <= x2 and y1 <= y <= y2

def contact_purpose_rows(part, connectors=None):
    """Describe every header/lead hole without guessing its device or pin order.

    A part's optional contacts list contains {pin, hole, device, function}, plus
    net, controller_endpoint, voltage and no_connect when applicable. Matching
    plan connectors can supply pin/net identity; generic names such as GND do
    not supply the missing device or branch purpose. This reads annotations,
    never changes electrical connections. Missing semantics remain UNRESOLVED.
    """
    reference = part.get("ref") or part.get("name")
    if not isinstance(reference, str) or not reference.strip():
        raise ValueError("A contact map needs its component ref or name")
    ref = reference.strip()
    holes = [hole.split()[0] for hole in part.get("holes", [])]
    if len(holes) != len(set(holes)):
        raise ValueError("Repeated hole in " + ref)
    matched = [c for c in connectors or [] if str(c.get("ref", c.get("name", ""))) == ref]
    if len(matched) > 1:
        raise ValueError("Repeated connector reference: " + ref)

    def indexed(entries, label):
        if not isinstance(entries, list):
            raise ValueError(label + " must be a list of contact dictionaries")
        result, pin_ids = {}, set()
        for item in entries:
            if not isinstance(item, dict) or not isinstance(item.get("hole"), str):
                raise ValueError(label + " needs a named hole for every contact")
            hole = item["hole"]
            pin = item.get("pin")
            if hole not in holes or hole in result:
                raise ValueError(label + " has duplicate or unrelated hole " + hole)
            if pin is not None:
                if isinstance(pin, bool) or not isinstance(pin, (str, int)) or not str(pin).strip():
                    raise ValueError(label + " has an invalid contact index at " + hole)
                if str(pin).strip() in pin_ids:
                    raise ValueError(label + " has duplicate contact index " + str(pin))
                pin_ids.add(str(pin).strip())
            result[hole] = dict(item)
        return result

    baseline = indexed(matched[0].get("pins", []), ref + " connector") if matched else {}
    supplied = indexed(part["contacts"], ref + " contacts") if "contacts" in part else {}
    rows = []
    pin_holes = {}
    for hole in holes:
        item = dict(baseline.get(hole, {}))
        annotation = supplied.get(hole, {})
        for field in ("pin", "net"):
            if field in item and field in annotation and str(item[field]) != str(annotation[field]):
                raise ValueError(ref + " annotation changes " + field + " at " + hole)
        item.update(annotation)
        for field in ("device", "function", "controller_endpoint", "voltage", "net"):
            value = item.get(field)
            if value is not None and (not isinstance(value, str) or not value.strip()):
                raise ValueError(ref + " needs nonempty text for " + field + " at " + hole)
        no_connect = item.get("no_connect", False)
        if not isinstance(no_connect, bool):
            raise ValueError(ref + " no_connect must be true or false at " + hole)
        if no_connect and item.get("net") not in (None, "NC"):
            raise ValueError(ref + " cannot mark an electrically assigned net unused at " + hole)
        missing = [field for field in ("pin", "device", "function")
                   if item.get(field) is None or not str(item[field]).strip()]
        pin = str(item["pin"]).strip() if item.get("pin") is not None else ""
        if pin:
            if pin in pin_holes:
                raise ValueError(f"{ref} has duplicate contact index {pin} at {pin_holes[pin]} and {hole}")
            pin_holes[pin] = hole
        rows.append({
            "contact": ref + ("." + pin if pin else " at " + hole),
            "pin": pin, "hole": hole,
            "device": item.get("device") or "UNRESOLVED device",
            "function": item.get("function") or "UNRESOLVED function",
            "net": "NC (no added connection)" if no_connect else item.get("net") or "",
            "controller_endpoint": item.get("controller_endpoint") or "",
            "voltage": item.get("voltage") or "",
            "status": "unresolved" if missing else "resolved", "missing": missing,
        })
    return rows


def contact_purpose_text(row):
    """One complete endpoint label, reused by the step table and figures."""
    text = "%s / %s: %s; %s" % (row["contact"], row["hole"], row["device"], row["function"])
    for field in ("voltage", "net", "controller_endpoint"):
        if row[field]:
            text += "; " + row[field]
    if row["missing"]:
        text += "; UNRESOLVED " + ", ".join(row["missing"])
    return text


def connection_purpose_findings(parts, connectors=None):
    """Validate contact identities and report missing purpose separately from layout."""
    findings = []
    pin_holes = {}
    for part in parts:
        if part.get("kind") in ("header", "pigtail", "panel"):
            ref = part.get("ref")
            for row in contact_purpose_rows(part, connectors):
                pin, hole = row["pin"], row["hole"]
                if ref and pin:
                    identity = (ref.strip(), pin)
                    previous = pin_holes.setdefault(identity, hole)
                    if previous != hole and parse_hole(previous) != parse_hole(hole):
                        raise ValueError(f"{identity[0]} has duplicate contact index {pin} at {previous} and {hole}")
                if row["missing"]:
                    findings.append(row["contact"] + " / " + row["hole"] + ": UNRESOLVED " + ", ".join(row["missing"]))
    return findings


def _part_hole_token(role, value):
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{role} must name a board hole, got {value!r}")
    return value.split()[0]


def _validate_part_positions(parts, connectors, geometry):
    """Validate positions consumed by the walkthrough and the board views."""
    for part in parts:
        if not isinstance(part, dict) or not isinstance(part.get("name"), str) or not part["name"].strip():
            raise ValueError("each build part must have a name")
        role = "part " + part["name"]
        placements = part.get("holes", ())
        if not isinstance(placements, (list, tuple)):
            raise ValueError(f"{role} holes must be a list of board holes")
        holes = [_part_hole_token(role, placement) for placement in placements]
        kind = part.get("kind")
        if (not holes and kind in ("header", "panel", "polarised")
                or kind == "pigtail" and "holes" not in part):
            raise ValueError(f"{role} must name its board holes")
        for hole in holes:
            _require_layout_hole(role, hole, geometry)
        identities = {parse_hole(hole) for hole in holes}
        if len(identities) != len(holes):
            raise ValueError(f"{role} repeats a physical hole")
        if kind == "polarised" and part.get("marked_hole") is not None:
            marked = part["marked_hole"]
            _require_layout_hole(role + " marked_hole", marked, geometry)
            if parse_hole(marked) not in identities:
                raise ValueError(f"{role} marked_hole must match one of its board holes")
        if kind == "module" and part.get("covers"):
            _module_bounds(part["covers"], geometry)
    connection_purpose_findings(parts, connectors)


def order_build_steps(parts, wires, board=None, connectors=None):
    """Sort a build into phases a beginner can follow.

    parts: list of dicts {name, kind, holes:[...], covers: {rows, cols} (optional, for plug-in modules),
           note, contacts (optional)}; kind in 'module' (plugs in, never soldered), 'header', 'polarised',
           'pigtail', 'panel'.
    wires: list of dicts {no, net, frm, to, what}.
    Returns a list of {phase, step, detail} in order: hidden wires, polarised parts, headers,
    other wires, pigtails/panel leads, trim and inspect, plug in modules.
    Figure actions also carry a private (kind, source index) pair for the input lists.
    """
    g = board_geometry(board)
    _validate_part_positions(parts, connectors, g)
    _validate_layout_endpoints((), wires, {}, None, None, g)
    modules = [(index, part) for index, part in enumerate(parts)
               if part.get("kind") == "module" and part.get("covers")]
    hidden, open_ = [], []
    for index, w in enumerate(wires):
        under = any(parse_hole(w[k])[0] == "col" and hole_under_module(w[k], m["covers"], g)
                    for _, m in modules for k in ("frm", "to"))
        (hidden if under else open_).append(index)
    steps = []
    def connection_step(index, part, phase):
        contacts = contact_purpose_rows(part, connectors)
        detail = part.get("note", "")
        labels = "; ".join(contact_purpose_text(row) for row in contacts)
        steps.append({"phase": phase,
                      "step": "%s in %s" % (part["name"], ", ".join(part["holes"])),
                      "detail": (detail + "; " if detail else "") + labels,
                      "part_name": part["name"], "contacts": contacts,
                      "operation_note": detail, "_action": ("part", index)})
    def wire_step(index, phase):
        w = wires[index]
        steps.append({"phase": phase, "step": "Wire %s, %s: %s to %s (%d mm)" % (
            w.get("no", "?"), w["net"], w["frm"], w["to"], wire_length_mm(w["frm"], w["to"], g)),
            "detail": w.get("what", ""), "_action": ("wire", index)})
    for index in hidden:
        wire_step(index, "1 hidden wires (under a module, before its headers)")
    for index, p in enumerate(parts):
        if p.get("kind") == "polarised":
            steps.append({"phase": "2 polarised parts (check the mark before heat)",
                          "step": "%s in %s" % (p["name"], ", ".join(p["holes"])),
                          "detail": p.get("note", ""), "_action": ("part", index)})
    for index, p in enumerate(parts):
        if p.get("kind") == "header":
            connection_step(index, p, "3 headers (module as jig, one end pin first, check square, then the rest)")
    for index in open_:
        wire_step(index, "4 remaining wires")
    for index, p in enumerate(parts):
        if p.get("kind") in ("pigtail", "panel"):
            connection_step(index, p, "5 leads leaving the board (strain relief)")
    steps.append({"phase": "6 trim and inspect", "step": "trim leads as specified; verify pad/lead wetting and no unintended bridges",
                  "detail": "hold the back to the light; drag a clean tip between bridged pins"})
    for index, p in modules:
        steps.append({"phase": "7 plug in modules (after the continuity table passes)",
                      "step": p["name"], "detail": p.get("note", ""), "_action": ("module", index)})
    return steps

def _measurement_text(measurement, mode, check_id):
    """Render a closed numeric criterion without accepting instructions."""
    resistance_units = {"mΩ", "Ω", "kΩ", "MΩ"}
    units_by_mode = {"continuity": resistance_units, "resistance": resistance_units,
                     "diode": {"mV", "V"}}
    operators = {"at_least": ">=", "above": ">", "at_most": "<=", "below": "<"}
    if not isinstance(measurement, dict) or set(measurement) - {"unit", *operators}:
        raise ValueError(check_id + ": measurement must contain a unit and numeric limits only")
    unit = measurement.get("unit")
    if not isinstance(unit, str) or unit not in units_by_mode.get(mode, ()):
        raise ValueError(check_id + ": measurement unit is unsupported for the selected meter mode")
    lower = [name for name in ("at_least", "above") if name in measurement]
    upper = [name for name in ("at_most", "below") if name in measurement]
    limits = lower + upper
    if not limits or len(lower) > 1 or len(upper) > 1:
        raise ValueError(check_id + ": measurement needs one or two limits, with at most one per side")
    if not all(_finite_number(measurement[name]) for name in limits):
        raise ValueError(check_id + ": measurement limits must be finite numbers")
    if lower and upper:
        low, high = (measurement[name] for name in limits)
        if low > high or (low == high and limits != ["at_least", "at_most"]):
            raise ValueError(check_id + ": measurement limits describe an empty interval")
    return "Reading " + " and ".join(
        f"{operators[name]} {measurement[name]} {unit}" for name in limits
    )


def _measurement_source_text(source, check_id):
    """Use a numbered plan citation that cannot encode placement prose."""
    locators = {"page", "section", "step"}
    if (not isinstance(source, dict) or len(source) != 2 or "reference" not in source
            or set(source) - {"reference", *locators}):
        raise ValueError(check_id + ": source requires a plan reference and one page, section or step")
    if any(type(value) is not int or not 1 <= value <= 999999 for value in source.values()):
        raise ValueError(check_id + ": source identifiers must be integers from 1 through 999999")
    locator, = source.keys() & locators
    return f"Plan source {source['reference']}, {locator} {source[locator]}"


def _verified_probe_assignment(probes, holes, geometry, check_id):
    """Validate explicitly verified lead roles for the two physical check holes."""
    if (not isinstance(probes, dict) or set(probes) != {"red", "black", "verified"}
            or probes["verified"] is not True):
        raise ValueError(check_id + ": probes must supply red, black and verified: true")
    roles = ("red", "black")
    if any(not isinstance(probes[role], str) or not probes[role].strip() for role in roles):
        raise ValueError(check_id + ": probe endpoints must be nonempty hole identifiers")
    if len(holes) != 2 or any(not isinstance(hole, str) or not hole.strip() for hole in holes):
        raise ValueError(check_id + ": probe assignment requires two physical check holes")
    try:
        expected = {parse_hole(hole): hole for hole in holes}
        assigned = {role: parse_hole(probes[role]) for role in roles}
        for role in roles:
            hole_xy(probes[role], geometry)
    except (KeyError, ValueError) as err:
        raise ValueError(check_id + ": invalid probe endpoint for the verified board") from err
    if len(expected) != 2 or set(assigned.values()) != set(expected):
        raise ValueError(check_id + ": red and black must match the two distinct physical check holes")
    return {role: expected[assigned[role]] for role in roles}


def _is_diode_placement(entry):
    kind = entry.get("kind")
    return kind == "diode" or (kind is None and any(
        entry.get(key) is not None for key in ("anode", "anode_hole", "cathode", "cathode_hole")
    ))


def _diode_terminal_map(entry, geometry, part=None):
    """Reconcile explicit placement claims by physical hole identity."""
    label = "diode " + entry["name"]
    check_id = "polarised:" + entry["name"]

    def hole(value, field):
        token = _part_hole_token(f"{check_id} {field}", value)
        _require_layout_hole(f"{check_id} {field}", token, geometry)
        return parse_hole(token), token

    claims = {}
    selected = {}
    declared = None
    marked = None
    marked_terminal = None
    for record in (entry,) if part is None else (entry, part):
        holes = record.get("holes", ())
        if not isinstance(holes, (list, tuple)):
            raise ValueError(f"{label}: declared holes must be a list")
        if holes:
            pair = {hole(value, "placement")[0] for value in holes}
            if len(holes) != 2 or len(pair) != 2 or (declared is not None and pair != declared):
                raise ValueError(f"{label}: conflicting or non-distinct declared holes")
            declared = pair
        for terminal in ("anode", "cathode"):
            for key in (terminal + "_hole", terminal):
                value = record.get(key)
                if value is None:
                    continue
                identity, token = hole(value, key)
                if terminal in claims and identity != claims[terminal]:
                    raise ValueError(f"{label}: conflicting {terminal} hole aliases")
                claims[terminal] = identity
                if record is entry:
                    selected.setdefault(terminal, token)
        if record.get("marked_hole") is not None:
            mark, _ = hole(record["marked_hole"], "marked_hole")
            if marked is not None and mark != marked:
                raise ValueError(f"{label}: conflicting marked holes")
            marked = mark
        if record.get("marked_terminal") is not None:
            terminal = record["marked_terminal"]
            if terminal not in ("anode", "cathode") or (marked_terminal is not None and terminal != marked_terminal):
                raise ValueError(f"{label}: conflicting or invalid marked_terminal")
            marked_terminal = terminal

    if marked_terminal is not None:
        if marked is None or (marked_terminal in claims and marked != claims[marked_terminal]):
            raise ValueError(f"{label}: marked hole conflicts with the declared terminal")
        # Use the mark role to check consistency. Placement still needs both terminal fields.
        claims[marked_terminal] = marked
    identities = set(claims.values())
    if len(identities) != len(claims):
        raise ValueError(f"{label}: anode and cathode must be two distinct physical holes")
    if declared is not None and not identities <= declared:
        raise ValueError(f"{label}: terminal mapping conflicts with declared holes")
    placement = declared if declared is not None else identities
    if marked is not None and len(placement) == 2 and marked not in placement:
        raise ValueError(f"{label}: marked hole conflicts with the diode placement")
    return {
        "anode": selected.get("anode"),
        "cathode": selected.get("cathode"),
        "marked_terminal": marked_terminal,
        "vf": entry.get("vf"),
    }


def _diode_placements(polarised, parts, geometry):
    """Resolve diode placement before issuing any plan output."""
    placements = {}
    for entry in polarised or ():
        if not _is_diode_placement(entry):
            continue
        name = entry["name"]
        matching = [part for part in parts if isinstance(part, dict) and part.get("name") == name]
        if name in placements or len(matching) > 1:
            raise ValueError(f"diode {name}: ambiguous matching plan entries")
        placements[name] = _diode_terminal_map(entry, geometry, matching[0] if matching else None)
    return placements


def continuity_checks(wires, rails, polarised=None, headers=None, board=None,
                      test_expectations=None):
    """Build unpowered checks without inventing electrical acceptance criteria.

    The optional test_expectations map uses stable check IDs: rail:L1:R1,
    polarised:D1 and header:J1:A1:A2. General entries supply mode, expect
    and basis from the verified plan. Colored entries replace expect with a
    numeric measurement, numbered source and verified red and black probe holes.
    Missing criteria in general checks stay unresolved.
    Header holes are listed in physical adjacency order. A supplied Vf alone
    remains visible but cannot establish a reverse test or meter capability.
    """
    geometry = board_geometry(board)
    _validate_layout_endpoints((), wires, rails, None, None, geometry)
    expectations = {} if test_expectations is None else test_expectations
    if not isinstance(expectations, dict) or any(not isinstance(key, str) for key in expectations):
        raise ValueError("test_expectations must be an object keyed by string check IDs")
    rows, used = [], set()
    modes = {"continuity", "resistance", "diode", "visual"}

    def planned_row(check_id, touch, holes, note, supplied_forward=None):
        for hole in holes:
            if hole is not None:
                _require_layout_hole(check_id, hole, geometry)
        spec = expectations.get(check_id, {})
        if not isinstance(spec, dict):
            raise ValueError(check_id + ": expectation must be an object")
        if "probes" in spec and check_id in used:
            raise ValueError(check_id + ": probe assignment has an ambiguous check ID")
        used.add(check_id)
        structured = "probes" in spec or "measurement" in spec
        if structured and ("expect" in spec or "basis" in spec):
            raise ValueError(check_id + ": free-text expect or basis cannot be combined with a colored check")
        for key in ("mode", "expect", "basis"):
            if key in spec and not isinstance(spec[key], str):
                raise ValueError(check_id + ": " + key + " must be text")
        mode = spec.get("mode", "not specified")
        if spec.get("mode") and mode not in modes:
            raise ValueError(check_id + ": mode must be continuity, resistance, diode or visual")

        basis = spec.get("basis", "not supplied")
        assignment = None
        if structured:
            if set(spec) != {"mode", "probes", "measurement", "source"}:
                raise ValueError(check_id + ": colored checks require mode, probes, measurement and source only")
            if mode not in {"continuity", "resistance", "diode"}:
                raise ValueError(check_id + ": colored checks require a meter mode")
            assignment = _verified_probe_assignment(spec["probes"], holes, geometry, check_id)
            expectation = _measurement_text(spec["measurement"], mode, check_id)
            basis = _measurement_source_text(spec["source"], check_id)
            missing = []
        else:
            missing = [key for key in ("mode", "expect", "basis")
                       if not isinstance(spec.get(key), str) or not spec[key].strip()]
            expectation = spec.get("expect", "")
            if missing:
                detail = " Supplied target: " + expectation if expectation else ""
                if supplied_forward is not None:
                    detail += " Supplied forward value: " + str(supplied_forward) + "."
                expectation = "UNRESOLVED: plan must supply " + ", ".join(missing) + "." + detail

        row = {"touch": touch, "mode": mode, "expect": expectation, "basis": basis,
               "status": "unresolved" if missing else "plan-supplied criterion",
               "means": note, "_check_id": check_id, "_holes": holes}
        if assignment is not None:
            row["_probes"] = assignment
            row["touch"] += " (red lead: {red}, black lead: {black})".format(**assignment)
        rows.append(row)

    for w in wires:
        check_id = "wire:" + str(w.get("no", "?"))
        rows.append({"touch": "%s and %s" % (w["frm"], w["to"]),
                     "mode": "continuity", "expect": "beep for the intended direct connection",
                     "basis": "wire list supplied in the verified plan", "status": "plan-supplied connection",
                     "means": "Check wire %s (%s); alternate paths can also conduct, so this alone does not prove the joint or physical safety." % (w.get("no", "?"), w["net"]),
                     "_check_id": check_id, "_holes": [w["frm"], w["to"]]})
    rail_items = list(rails.items())
    for i in range(len(rail_items)):
        for j in range(i + 1, len(rail_items)):
            (ra, na), (rb, nb) = rail_items[i], rail_items[j]
            if na != nb:
                mid = max(1, geometry["rows"] // 2)
                planned_row("rail:" + ":".join(sorted((ra, rb))),
                            "%s rail (%s) and %s rail (%s)" % (ra, na, rb, nb),
                            ["%s@%d" % (ra, mid), "%s@%d" % (rb, mid)],
                            "Compare with the plan; components, parallel paths and capacitor charging may affect this reading.")
    for p in polarised or []:
        name = p["name"]
        role = "polarised:" + name
        if _is_diode_placement(p):
            terminals = _diode_terminal_map(p, geometry)
            holes = p.get("holes", [terminals["anode"], terminals["cathode"]])
        else:
            holes = p.get("holes", [p.get("anode_hole"), p.get("cathode_hole")])
        if not isinstance(holes, (list, tuple)):
            raise ValueError(f"{role} holes must be a list of board holes")
        for hole in holes:
            if hole is not None:
                _require_layout_hole(role, hole, geometry)
        for terminal in ("anode", "cathode"):
            label = p.get(terminal + "_hole", p.get(terminal))
            if label is not None:
                terminal_role = role + " " + terminal
                _require_layout_hole(terminal_role, _part_hole_token(terminal_role, label), geometry)
        planned_row(role, "Plan-identified terminals or polarity marks of " + name,
                    list(holes)[:2], "Use the applicable component test and the specified probe orientation; a generic diode drop does not apply to all polarized parts.",
                    supplied_forward=p.get("vf"))
    for h in headers or []:
        holes = h.get("holes")
        if not isinstance(holes, (list, tuple)):
            raise ValueError("header:" + h["name"] + " holes must be a list of board holes")
        for hole in holes:
            _require_layout_hole("header:" + h["name"], hole, geometry)
        for left, right in zip(holes, holes[1:]):
            check_id = "header:" + h["name"] + ":" + left + ":" + right
            planned_row(check_id, "%s neighboring pins %s and %s" % (h["name"], left, right),
                        [left, right], "Compare with the net table: neighboring pins may intentionally share a net.")
    unknown = set(expectations) - used
    if unknown:
        raise ValueError("Unknown test expectation IDs: " + ", ".join(sorted(unknown)))
    return rows

def markdown_table(rows, columns=None):
    """Render rows as a Markdown table while keeping cell delimiters literal."""
    if not rows:
        return ""

    def escape_delimiter(match):
        backslashes, delimiter = match.groups()
        # Preserve literal backslashes before the escaped pipe or line break.
        return backslashes * 2 + (r"\|" if delimiter == "|" else "<br>")

    def cell(value):
        return re.sub(r"(?<!\\)(\\*)(\||\r\n?|\n)", escape_delimiter, str(value))

    cols = columns or [k for k in rows[0].keys() if not k.startswith("_")]
    out = ["| " + " | ".join(cell(c) for c in cols) + " |",
           "| " + " | ".join("---" for _ in cols) + " |"]
    for r in rows:
        out.append("| " + " | ".join(cell(r.get(c, "")) for c in cols) + " |")
    return "\n".join(out)

def expand_holes(spec):
    """'A1-A15' -> ['A1', ..., 'A15']; 'A19-A21' -> ['A19','A20','A21']."""
    m = re.fullmatch(r"([A-Z])(\d+)-([A-Z])(\d+)", spec.replace(" ", "").upper())
    if not m or m.group(1) != m.group(3):
        return [spec]
    return ["%s%d" % (m.group(1), r) for r in range(int(m.group(2)), int(m.group(4)) + 1)]


def _require_layout_hole(role, hole, geometry):
    if not isinstance(hole, str):
        raise ValueError(f"{role} must name a board hole, got {hole!r}")
    try:
        return hole_xy(hole, geometry)
    except (KeyError, ValueError) as error:
        raise ValueError(f"{role} has invalid hole {hole!r}: {error}") from None


def _validate_layout_endpoints(pins, wires, rails, components, joins, geometry):
    """Require every endpoint to identify a physical hole on the selected board."""
    for pin in pins:
        _require_layout_hole("pin", pin.get("hole"), geometry)
    for wire in wires:
        _require_layout_hole("wire start", wire.get("frm"), geometry)
        _require_layout_hole("wire end", wire.get("to"), geometry)
    for rail in rails:
        if not isinstance(rail, str):
            raise ValueError(f"rail must have a board label, got {rail!r}")
        _require_layout_hole("rail", rail + "@1", geometry)
    for component in components or ():
        holes = component.get("holes")
        if not isinstance(holes, (list, tuple)):
            raise ValueError("component holes must be a list of board holes")
        for hole in holes:
            _require_layout_hole("component", hole, geometry)
    for join in joins or ():
        if not isinstance(join, (list, tuple)) or len(join) != 2:
            raise ValueError("join must name two board holes")
        for hole in join:
            _require_layout_hole("join", hole, geometry)


def layout_check(pins, wires, rails, board=None, components=None, joins=None):
    """Engineer's pre-solder check of a perfboard layout: finds shorts, opens, double-used holes
    and redundant wires by joining holes the way the copper and the wires do (union-find).

    pins:  [{net, hole, name}]  every module/header pin that carries a net (skip no-connects)
    wires: [{no, net, frm, to}]
    rails: {rail: net}  e.g. {'L1': 'SUPPLY', 'R1': 'RETURN'}
    components: [{name, holes:[h1, h2]}]  two-leg parts (diode, resistor) that intentionally join two nets
    joins: [(h1, h2)]  holes joined inside a plug-in module (e.g. a DevKit's two GND pins)
    Returns {'ok': bool, 'findings': [str], 'nodes': {node_id: sorted(nets)}}.
    """
    g = board_geometry(board)
    _validate_layout_endpoints(pins, wires, rails, components, joins, g)
    parent = {}
    def key(h):
        kind, nm, row = parse_hole(h)
        if kind == "tap":
            return "rail:" + g["tap_holes"][nm][2]
        if kind == "rail":
            return "rail:" + nm
        for s in g["strips"]:
            if nm in s:
                return "strip:%s%d" % (s[0], row)
        return "hole:" + nm + str(row)
    def find(k):
        parent.setdefault(k, k)
        while parent[k] != k:
            parent[k] = parent[parent[k]]
            k = parent[k]
        return k
    def union(a, b):
        parent[find(a)] = find(b)
    findings = []
    used = {}
    def occupy(hole, owner):
        kind, lane, row = parse_hole(hole)
        address = lane if kind == "tap" else f"{lane}{'@' if kind == 'rail' else ''}{row}"
        used.setdefault(address, []).append(owner)

    for p in pins:
        occupy(p["hole"], p.get("name", p["net"]))
    for c in components or []:
        for h in c["holes"]:
            occupy(h, c["name"])
    for w in wires:
        for h in (w["frm"], w["to"]):
            occupy(h, "wire %s" % w.get("no", "?"))
    for h, who in used.items():
        if len(who) > 1:
            findings.append("hole %s used %d times: %s" % (h, len(who), ", ".join(who)))
    for w in wires:
        if same_node(w["frm"], w["to"], g):
            findings.append("wire %s (%s) joins %s and %s, which the copper already joins" % (
                w.get("no", "?"), w["net"], w["frm"], w["to"]))
        union(key(w["frm"]), key(w["to"]))
    for a, b in joins or []:
        union(key(a), key(b))
    nets_on = {}
    def tag(h, net):
        nets_on.setdefault(find(key(h)), set()).add(net)
    for r, net in rails.items():
        tag(r + "@1", net)
    for p in pins:
        tag(p["hole"], p["net"])
    for w in wires:
        tag(w["frm"], w["net"]); tag(w["to"], w["net"])
    comp_pairs = set()
    for c in components or []:
        comp_pairs.add(frozenset(find(key(h)) for h in c["holes"]))
    for node, nets in nets_on.items():
        if len(nets) > 1:
            findings.append("SHORT: node %s carries nets %s" % (node, ", ".join(sorted(nets))))
    by_net = {}
    for node, nets in nets_on.items():
        for n in nets:
            by_net.setdefault(n, set()).add(node)
    for n, nodes in by_net.items():
        if len(nodes) > 1:
            findings.append("OPEN: net %s is split across %d unconnected nodes: %s" % (
                n, len(nodes), ", ".join(sorted(nodes))))
    for pair in comp_pairs:
        if len(pair) == 1:
            findings.append("component bridges one node (its two legs are already joined)")
    return {"ok": not findings, "findings": findings,
            "nodes": {k: sorted(v) for k, v in nets_on.items()}}


def row_spacing_from_columns(col_a, col_b, board=None):
    """Pin-row spacing (mm) of a module whose two pin rows drop into these two columns of the board."""
    g = board_geometry(board)
    return round(abs(g["columns"][col_b.upper()] - g["columns"][col_a.upper()]), 2)


def columns_for_spacing(spacing_mm, board=None, tol=0.4):
    """Column pairs of the board that a module with this pin-row spacing can occupy."""
    g = board_geometry(board)
    cols = sorted(g["columns"].items(), key=lambda kv: kv[1])
    out = []
    for i, (ca, xa) in enumerate(cols):
        for cb, xb in cols[i + 1:]:
            if abs((xb - xa) - spacing_mm) <= tol:
                out.append((ca, cb))
    return out


def parts_check_table(parts):
    """Gate 0b checklist rows from a list of {name, assumes, look_at, if_differs} dicts (Markdown-ready)."""
    rows = []
    for p in parts:
        rows.append({"part": p["name"], "the plan assumes": p.get("assumes", ""), "look at / photograph": p.get("look_at", ""),
                     "if it differs": p.get("if_differs", ""), "verified": p.get("verified", "")})
    return rows


def run_plan(plan):
    """Build steps, continuity table and layout findings from one plan dict; returns Markdown."""
    board = plan.get("board")
    if board is None:
        raise ValueError("Plan must name its verified board geometry explicitly")
    geometry = board_geometry(board)
    placements = _diode_placements(plan.get("polarised"), plan["parts"], geometry)
    pins = plan.get("pins")
    wires, rails = plan["wires"], plan["rails"]
    components, joins = plan.get("components"), plan.get("joins")
    layout = None
    if pins is None:
        _validate_layout_endpoints((), wires, rails, components, joins, geometry)
    else:
        layout = layout_check(pins, wires, rails, geometry, components, joins)
    out = ["## Build steps", markdown_table(order_build_steps(plan["parts"], wires, geometry, plan.get("connectors")),
                                            ["phase", "step", "detail"])]
    unresolved = [name for name, roles in placements.items()
                  if roles["anode"] is None or roles["cathode"] is None]
    if unresolved:
        out += ["", "## Diode placement"]
        out += [f"- UNRESOLVED diode placement for {name}. Verify both terminals before soldering."
                for name in unresolved]
    findings = connection_purpose_findings(plan["parts"], plan.get("connectors"))
    out += ["", "## Connection purposes: " + ("UNRESOLVED" if findings else "complete")]
    out += ["- " + finding for finding in findings]
    out += ["", "## Continuity table", markdown_table(continuity_checks(
        wires, rails, plan.get("polarised"), plan.get("headers"), geometry,
        plan.get("test_expectations")))]
    if layout is not None:
        out += ["", "## Layout check: %s" % ("ok" if layout["ok"] else "FINDINGS")]
        out += ["- " + f for f in layout["findings"]]
    return "\n".join(out)

if __name__ == "__main__":
    import json, sys
    sys.dont_write_bytecode = True
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(1)
    try:
        with open(sys.argv[1], encoding="utf-8") as plan_file:
            report = run_plan(json.load(plan_file))
    except ValueError as error:
        raise SystemExit(str(error)) from None
    print(report)
