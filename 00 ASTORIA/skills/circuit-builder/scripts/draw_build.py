"""circuit-builder figure generator: plan-driven board views and labeled method illustrations.

    python3 draw_build.py plan.json outdir/
writes <prefix>_steps.png (one panel per build step, front view), <prefix>_back.png (mirrored
back view with every solder point numbered), <prefix>_tests.png (front view with the probe
points of the continuity table), plus joint_guide.png and header_jig.png. A verified diode
placement adds polarity_guide.png. Choose a destination where all these target names are
vacant, including polarity_guide.png. The batch renders all figures before writing to
the destination. Import and call the functions for finer control. Figure generation
requires Matplotlib 3.6 or newer to render plan labels literally.
Board views use board_tools.BOARDS or supplied geometry. Method illustrations are
not to scale and do not establish actual component geometry or acceptance criteria.
"""
import os
import sys
import math
import re
import shutil
import tempfile
import textwrap
import warnings
from collections.abc import Mapping
from functools import wraps

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from board_tools import (board_geometry, hole_xy, parse_hole, expand_holes,
                         order_build_steps, continuity_checks, contact_purpose_text,
                         _diode_placements, _diode_terminal_map, _finite_number,
                         _module_bounds, _validate_layout_endpoints, _validate_part_positions)

# Net identity comes from plan labels. Wire colour only improves visibility.
WIRE_COLOUR = "#d9e1ea"


def _plan_geometry(plan, board=None):
    """Require explicit board geometry for plan-driven views, never a default board."""
    choice = board if board is not None else plan.get("board")
    if choice is None:
        raise ValueError("Plan must name its verified board geometry explicitly")
    return board_geometry(choice)


def _board_axes(ax, g, mirror=False, title=None):
    """Draw the empty board: outline, every hole, row numbers and column letters.
    mirror=True draws the back view (x flipped), the way the board looks when turned over
    about its long axis, row 1 still at the top."""
    W, H = g["size_mm"]
    def X(x):
        return W - x if mirror else x
    ax.add_patch(__import__("matplotlib.patches").patches.Rectangle((0, 0), W, H, fc="#2b4c7e" if not mirror else "#1e3a5f", ec="k", lw=1.0))
    for r in range(1, g["rows"] + 1):
        y = g["row0"] + g["pitch"] * (r - 1)
        for c, x in g["columns"].items():
            ax.add_patch(__import__("matplotlib.patches").patches.Circle((X(x), y), 0.55, fc="#f3f3f3", ec="#999", lw=0.3))
        for rn, x in g["rails"].items():
            ax.add_patch(__import__("matplotlib.patches").patches.Circle((X(x), y), 0.55, fc="#f3f3f3", ec="#999", lw=0.3))
        if r == 1 or r % 5 == 0:
            ax.text(X(g["columns"]["E"]) + (2.3 if mirror else -2.3) * -1 if False else (W / 2), y, str(r), ha="center", va="center", fontsize=5.5, color="white")
    for c, x in g["columns"].items():
        ax.text(X(x), g["row0"] - 2.6, c, ha="center", va="center", fontsize=6, color="white")
    for rn, x in g["rails"].items():
        ax.text(X(x), g["row0"] - 2.6, rn, ha="center", va="center", fontsize=4.5, color="#cfd8e3")
    ax.set_xlim(-1, W + 1); ax.set_ylim(H + 1, -1)   # row 1 at the top
    ax.set_aspect("equal"); ax.axis("off")
    if title:
        ax.set_title(title, fontsize=7, loc="left")


def _hole(ax, g, hole, colour, mirror=False, r=0.9, lw=1.2, label=None, fs=5):
    W = g["size_mm"][0]
    x, y = hole_xy(hole, g)
    if mirror:
        x = W - x
    ax.add_patch(__import__("matplotlib.patches").patches.Circle((x, y), r, fc="none", ec=colour, lw=lw, zorder=5))
    if label is not None:
        ax.text(x, y, str(label), ha="center", va="center", fontsize=fs, color=colour, zorder=6, fontweight="bold")


def _wire(ax, g, a, b, colour, mirror=False, lw=2.0, alpha=1.0, z=4):
    W = g["size_mm"][0]
    (x1, y1), (x2, y2) = hole_xy(a, g), hole_xy(b, g)
    if mirror:
        x1, x2 = W - x1, W - x2
    ax.plot([x1, x2], [y1, y2], color=colour, lw=lw, alpha=alpha, solid_capstyle="round", zorder=z)
    for x, y in ((x1, y1), (x2, y2)):
        ax.add_patch(__import__("matplotlib.patches").patches.Circle((x, y), 0.7, fc=colour, ec="k", lw=0.3, alpha=alpha, zorder=z + 1))


def _module(ax, g, covers, name, mirror=False, alpha=0.25):
    W = g["size_mm"][0]
    x1, x2, y1, y2 = _module_bounds(covers, g)
    if mirror:
        x1, x2 = W - x2, W - x1
    ax.add_patch(__import__("matplotlib.patches").patches.Rectangle((x1, y1), x2 - x1, y2 - y1, fc="#222", ec="k", lw=0.8, alpha=alpha, zorder=3))
    ax.text((x1 + x2) / 2, (y1 + y2) / 2, name, ha="center", va="center", fontsize=6, color="k", zorder=7,
            bbox=dict(fc="white", ec="none", alpha=0.7, pad=1))


def _header_holes(ax, g, holes, colour, mirror=False, done=False):
    for h in holes:
        _hole(ax, g, h, colour, mirror, r=0.95, lw=1.4 if not done else 0.8)


def _literal_figure(renderer):
    """Render plan text literally and restore Matplotlib settings on exit."""
    @wraps(renderer)
    def render(*args, **kwargs):
        import matplotlib
        if "text.parse_math" not in matplotlib.rcParams:
            raise RuntimeError("Figure generation requires Matplotlib 3.6 or newer.")
        with matplotlib.rc_context({"text.parse_math": False, "text.usetex": False}):
            return renderer(*args, **kwargs)
    return render


@_literal_figure
def draw_steps(plan, out_png, board=None, ncols=3):
    """One panel per build step (front view). Finished steps stay drawn in faded colour;
    the current step is bright with its holes ringed and named."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    g = _plan_geometry(plan, board)
    placements = _diode_placements(plan.get("polarised"), plan["parts"], g)
    steps = [s for s in order_build_steps(plan["parts"], plan["wires"], g, plan.get("connectors"))
             if "_action" in s]
    import textwrap as _tw
    # A separate caption area grows with the contact list; never truncate pins
    # or hide later contacts to fit the old two-line generic note.
    captions = []
    for step in steps:
        lines = _tw.wrap(step.get("operation_note", step.get("detail", "")), 52)
        for row in step.get("contacts", []):
            lines.extend(_tw.wrap(contact_purpose_text(row), 52, subsequent_indent="  "))
        captions.append(lines)
    n = len(steps); nrows = max(1, math.ceil(n / ncols))
    caption_heights = [max([0.10 * (len(lines) + 1) for lines in captions[r*ncols:(r+1)*ncols]] or [0.3])
                       for r in range(nrows)]
    heights = [4.7 + height for height in caption_heights]
    fig = plt.figure(figsize=(ncols * 3.3, sum(heights)))
    grid = fig.add_gridspec(nrows, ncols, height_ratios=heights)
    axes = []
    for index in range(nrows * ncols):
        row_no = index // ncols
        panel = grid[row_no, index % ncols].subgridspec(2, 1, height_ratios=[4.7, caption_heights[row_no]])
        axes.append(fig.add_subplot(panel[0]))
        legend_ax = fig.add_subplot(panel[1]); legend_ax.axis("off")
        if index < n:
            legend_ax.text(0, 1, "\n".join(captions[index]), fontsize=6.2, va="top",
                           transform=legend_ax.transAxes, linespacing=1.15)
    done_wires, done_parts = [], []
    modules = [p for p in plan["parts"] if p.get("kind") == "module" and p.get("covers")]
    for i, s in enumerate(steps):
        ax = axes[i]
        kind, source_index = s["_action"]
        head = s["step"] if kind == "wire" else plan["parts"][source_index]["name"]
        ttl = "Step %d. %s" % (i + 1, head)
        _board_axes(ax, g, title="\n".join(_tw.wrap(ttl, 44)))
        for w in done_wires:
            _wire(ax, g, w["frm"], w["to"], WIRE_COLOUR, alpha=0.35)
        for p in done_parts:
            _header_holes(ax, g, [h.split()[0] for h in p["holes"]], "#bbb", done=True)
        if kind == "wire":
            w = plan["wires"][source_index]
            col = WIRE_COLOUR
            _wire(ax, g, w["frm"], w["to"], col)
            _hole(ax, g, w["frm"], "white", r=1.3, lw=1.0); _hole(ax, g, w["to"], "white", r=1.3, lw=1.0)
            x1, y1 = hole_xy(w["frm"], g); x2, y2 = hole_xy(w["to"], g)
            ax.annotate(w["frm"], (x1, y1), xytext=(0, 8), textcoords="offset points", fontsize=6, color="white", ha="center", va="bottom", fontweight="bold")
            ax.annotate(w["to"], (x2, y2), xytext=(0, -8), textcoords="offset points", fontsize=6, color="white", ha="center", va="top", fontweight="bold")
            done_wires.append(w)
        elif kind == "module":
            for m in modules:
                _module(ax, g, m["covers"], m["name"], alpha=0.6)
        else:
            p = plan["parts"][source_index]
            if p:
                holes = [h.split()[0] for h in p["holes"]]
                col = "#ff7f0e" if p.get("kind") == "polarised" else ("#2ca02c" if p.get("kind") == "header" else "#e377c2")
                if p.get("kind") == "polarised" and len(holes) == 2:
                    _wire(ax, g, holes[0], holes[1], "#222", lw=4)
                    roles = placements.get(p["name"])
                    mark = p.get("polarity_mark")
                    marked_hole = p.get("marked_hole")
                    if roles is not None:
                        complete = roles["anode"] is not None and roles["cathode"] is not None
                        terminal = roles["marked_terminal"] if complete else None
                        mark = terminal.capitalize() + " mark" if terminal else None
                        marked_hole = roles[terminal] if terminal else None
                        if not complete:
                            ax.text(.5, .04, "Orientation unresolved", transform=ax.transAxes,
                                    ha="center", fontsize=7, color="white")
                    if mark and marked_hole is not None:
                        xb, yb = hole_xy(marked_hole, g)
                        ax.annotate(str(mark), (xb, yb), xytext=(0, -9), textcoords="offset points", fontsize=6, color="white", ha="center", va="top", fontweight="bold")
                elif p.get("kind") == "pigtail":
                    # Hole identity is known; wire colors/polarity are not inferred.
                    for h in holes:
                        _hole(ax, g, h, "#888", r=1.2, lw=2.0)
                        x, y = hole_xy(h, g)
                        ax.plot([x, x + (4 if x > g["size_mm"][0] / 2 else -4)], [y, y + 6], color="#888", lw=2.0)
                        ax.annotate(h, (x, y), xytext=(0, 9), textcoords="offset points", fontsize=6, color="white", ha="center", va="bottom", fontweight="bold")
                _header_holes(ax, g, holes, col)
                if p.get("kind") != "pigtail":
                    for h, dy in ((holes[0], 8), (holes[-1], -8)):
                        x, y = hole_xy(h, g)
                        ax.annotate(h, (x, y), xytext=(0, dy), textcoords="offset points", fontsize=6, color="white", ha="center", va="bottom" if dy > 0 else "top", fontweight="bold")
                done_parts.append(p)
    for ax in axes[n:]:
        ax.axis("off")
    figure_title = _tw.fill(plan.get("title", "Build steps") + "; front view, parts enter this side",
                            width=max(30, int(ncols * 3.3 * 12)))
    fig.suptitle(figure_title, fontsize=9, x=0.02, y=0.995, ha="left", va="top")
    title_height = 0.15 * (figure_title.count("\n") + 1) + 0.12
    fig.tight_layout(rect=(0, 0, 1, 1 - title_height / sum(heights)))
    fig.savefig(out_png, dpi=200); plt.close(fig)
    return out_png


@_literal_figure
def draw_back(plan, out_png, board=None):
    """Mirrored back view: every point to be soldered, numbered in build order, with a legend."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    g = _plan_geometry(plan, board)
    _validate_layout_endpoints((), (), plan.get("rails", {}), None, None, g)
    _diode_placements(plan.get("polarised"), plan["parts"], g)
    steps = order_build_steps(plan["parts"], plan["wires"], g, plan.get("connectors"))
    fig, ax = plt.subplots(figsize=(5.6, 9.0))
    _board_axes(ax, g, mirror=True, title="BACK of the board (turned over left-to-right; row 1 still at the top)")
    legend = []
    k = 0
    nbig = 0
    for step in steps:
        kind, source_index = step.get("_action", (None, None))
        if kind not in ("wire", "part"):
            continue
        if kind == "wire":
            w = plan["wires"][source_index]
            holes = (w["frm"], w["to"])
            _wire(ax, g, *holes, WIRE_COLOUR, mirror=True, lw=1.4, alpha=0.5)
            label = "wire %s (%s): %s to %s" % (w.get("no"), w["net"], *holes)
        else:
            p = plan["parts"][source_index]
            holes = [h.split()[0] for h in p["holes"]]
            label = "%s: %s" % (p["name"], ", ".join(p["holes"]))
        if not holes:
            continue
        k0 = k + 1
        for h in holes:
            k += 1
            _hole(ax, g, h, "#ffd54f", mirror=True, r=1.25, lw=1.4,
                  label=k if len(holes) <= 3 else None, fs=4.5)
        if len(holes) > 3:
            x, y = hole_xy(holes[len(holes) // 2], g); x = g["size_mm"][0] - x
            ax.annotate("%d-%d" % (k0, k), (x, y), xytext=(g["size_mm"][0] / 2, y + 2 * g["pitch"] * nbig), textcoords="data",
                        fontsize=6.5, color="#ffd54f", ha="center", va="center", fontweight="bold",
                        bbox=dict(fc="#1e3a5f", ec="none", pad=0.6), arrowprops=dict(arrowstyle="-", color="#ffd54f", lw=0.7))
            nbig += 1
        legend.append("%d-%d  %s" % (k0, k, label))
        legend.extend(contact_purpose_text(row) for row in step.get("contacts", []))
    for rn, net in plan.get("rails", {}).items():
        x = g["size_mm"][0] - hole_xy(rn + "@1", g)[0]
        ax.text(x, g["size_mm"][1] - 1.0, net, rotation=90, fontsize=6, color="#ffd54f", ha="center", va="bottom", fontweight="bold")
    import textwrap as _tw
    leg = "\n".join(_tw.fill(l, 78, subsequent_indent="       ") for l in legend)
    nl = leg.count("\n") + 1
    legend_height = 0.10 * (nl + 2)
    total_height = 9.0 + legend_height
    fig.set_size_inches(6.4, total_height)
    fig.text(0.04, 0.012, leg, fontsize=6, va="bottom", family="monospace")
    fig.tight_layout(rect=(0, (legend_height + 0.2) / total_height, 1, 1))
    fig.savefig(out_png, dpi=200); plt.close(fig)
    return out_png


def _check_probe_assignments(plan, checks, geometry):
    """Bind any displayed probe roles to the verified entries in the actual plan."""
    expectations = plan.get("test_expectations")
    plan_has_structured_checks = isinstance(expectations, dict) and any(
        isinstance(spec, dict) and ("probes" in spec or "measurement" in spec)
        for spec in expectations.values())
    if not plan_has_structured_checks and not any("_probes" in check for check in checks):
        return
    plan_geometry = _plan_geometry(plan)
    if geometry != plan_geometry:
        raise ValueError("Figure board geometry conflicts with the verified probe plan")
    planned = continuity_checks(plan["wires"], plan.get("rails", {}), plan.get("polarised"),
                                plan.get("headers"), plan_geometry, expectations)
    mapped = {check["_check_id"]: check for check in planned if "_probes" in check}
    for check in checks:
        check_id = check.get("_check_id")
        expected = mapped.get(check_id)
        if expected is None and "_probes" not in check:
            continue
        fields = ("_holes", "_probes", "mode", "expect", "basis", "status")
        if expected is None or any(check.get(field) != expected[field] for field in fields):
            raise ValueError(f"{check_id or 'unidentified check'}: figure probe assignment conflicts with the verified plan")


@_literal_figure
def draw_tests(plan, checks, out_png, board=None):
    """Show verified probe roles or neutral locations and the complete criterion."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    g = _plan_geometry(plan, board)
    _diode_placements(plan.get("polarised"), plan.get("parts", ()), g)
    _check_probe_assignments(plan, checks, g)
    tests = []
    for i, check in enumerate(checks):
        holes = [h for h in (check.get("_holes") or []) if h]
        if len(holes) < 2:
            continue
        a, b = holes[:2]
        mode = check.get("mode", "not specified")
        resolved = check.get("status") != "unresolved" and mode != "not specified"
        setting = mode if resolved else "UNRESOLVED; do not select a meter setting"
        criterion = textwrap.fill("expect: " + check["expect"], width=38)
        title = f"Check {i + 1}: {setting}\n{a} / {b}\n{criterion}"
        if "_probes" in check:
            title += "\n" + textwrap.fill(check["basis"], width=38)
        tests.append((a, b, check, title))
    n = len(tests)
    ncols, nrows = 4, max(1, math.ceil(n / 4))
    title_lines = max((title.count("\n") + 1 for _, _, _, title in tests), default=3)
    fig, axes = plt.subplots(nrows, ncols, figsize=(ncols * 2.4, nrows * (4.2 + .16 * (title_lines - 3))))
    axes = axes.ravel()
    for ax, (a, b, check, title) in zip(axes, tests):
        _board_axes(ax, g, title=title)
        for w in plan["wires"]:
            _wire(ax, g, w["frm"], w["to"], WIRE_COLOUR, lw=1.2, alpha=0.45)
        probes = check.get("_probes", {})
        markers = {probes.get("red"): ("Red lead", "#d62728"),
                   probes.get("black"): ("Black lead", "#111111")}
        for h, dy in ((a, 10), (b, -10)):
            label, colour = markers.get(h, ("location", "#d9e1ea"))
            _hole(ax, g, h, colour, r=1.5, lw=2.2)
            x, y = hole_xy(h, g)
            ax.annotate(label, (x, y), xytext=(0, dy), textcoords="offset points", fontsize=6, color="#333333", ha="center",
                        va="bottom" if dy > 0 else "top", fontweight="bold", bbox=dict(fc="white", ec="none", alpha=0.85, pad=0.5))
    for ax in axes[n:]:
        ax.axis("off")
    if not tests:
        fig.text(.5, .5, "No probe locations supplied; resolve the verified plan first.", ha="center")
    fig.suptitle("Unpowered checks: use each plan-specified mode; the table retains all unresolved criteria", fontsize=9, x=.02, ha="left")
    fig.text(.02, .01, "%d of %d checks have displayed locations. Follow the verified table for meter mode, criterion and lead orientation.\nNo physical safety or powered-function certification." % (n, len(checks)), fontsize=7)
    fig.tight_layout(rect=(0, .06, 1, 1 - .42 / fig.get_figheight()))
    fig.savefig(out_png, dpi=200); plt.close(fig)
    return out_png


@_literal_figure
def draw_joint_guide(out_png):
    """Cross-sections: good joint, cold ball, starved joint, bridge. Schematic, not to scale."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.patches import Rectangle, Circle, Polygon
    fig, axes = plt.subplots(1, 4, figsize=(10, 3))
    titles = ["GOOD: wets pad and leg; finish varies", "INCOMPLETE WETTING: ball sits on top\nFix: follow the specified rework process",
              "STARVED: pad bare, only leg wetted\nFix: add a touch of solder", "BRIDGE: two pads joined\nFix: clean tip between them, drag away"]
    for ax, t in zip(axes, titles):
        ax.add_patch(Rectangle((0, 0), 10, 1.2, fc="#2b4c7e", ec="k"))          # board
        for xc in (3.5, 6.5) if "BRIDGE" in t else (5.0,):
            ax.add_patch(Rectangle((xc - 1.1, 1.2), 2.2, 0.25, fc="#d4a017", ec="k", lw=0.5))   # pad (copper ring)
            ax.add_patch(Rectangle((xc - 0.25, -0.6), 0.5, 4.6, fc="#999", ec="k", lw=0.5))     # leg
        if t.startswith("GOOD"):
            ax.add_patch(Polygon([[3.9, 1.45], [4.75, 3.0], [5.25, 3.0], [6.1, 1.45]], closed=True, fc="#c9c9c9", ec="k", lw=0.6))
        elif t.startswith("INCOMPLETE WETTING"):
            ax.add_patch(Circle((5.0, 2.6), 1.0, fc="#9a9a9a", ec="k", lw=0.6))
        elif t.startswith("STARVED"):
            ax.add_patch(Polygon([[4.7, 2.0], [4.75, 3.2], [5.25, 3.2], [5.3, 2.0]], closed=True, fc="#c9c9c9", ec="k", lw=0.6))
        else:
            ax.add_patch(Polygon([[2.4, 1.45], [3.2, 2.6], [6.8, 2.6], [7.6, 1.45]], closed=True, fc="#c9c9c9", ec="k", lw=0.6))
        ax.set_xlim(0, 10); ax.set_ylim(-1, 4.5); ax.set_aspect("equal"); ax.axis("off")
        ax.set_title(t, fontsize=7.5)
    fig.text(0.5, 0.02, "Method illustration, not to scale. Check wetting and joint geometry against the solder/component process; surface shine alone is not acceptance.", ha="center", fontsize=7)
    fig.tight_layout(rect=(0, 0.06, 1, 1))
    fig.savefig(out_png, dpi=200); plt.close(fig)
    return out_png


def _validate_header_jig(config):
    if not isinstance(config, Mapping):
        raise ValueError("header_jig must be a mapping")
    unknown = config.keys() - {"pitch_mm", "module", "orientation_note"}
    if unknown:
        raise ValueError("Unknown header_jig fields: " + ", ".join(sorted(map(repr, unknown))))
    pitch_mm = config.get("pitch_mm")
    if pitch_mm is not None and (not _finite_number(pitch_mm) or pitch_mm <= 0):
        raise ValueError("Header pitch must be a positive finite measurement")
    if "module" in config and not isinstance(config["module"], str):
        raise ValueError("header_jig.module must be a string")
    note = config.get("orientation_note")
    if note is not None and not isinstance(note, str):
        raise ValueError("header_jig.orientation_note must be a string or null")


@_literal_figure
def draw_header_jig(out_png, pitch_mm=None, module="Module example", orientation_note=None):
    """Side view of the header-as-jig method: sockets on the module's pins, the sandwich in the board,
    one end pin soldered, check square, then the rest."""
    _validate_header_jig({"pitch_mm": pitch_mm, "module": module, "orientation_note": orientation_note})
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.patches import Rectangle
    pitch_note = "Use the measured spacing from the verified plan." if pitch_mm is None else "Plan-reported pitch: %.2f mm; schematic only." % pitch_mm
    fig, axes = plt.subplots(1, 3, figsize=(10, 3.2))
    orientation_note = orientation_note or "Match the orientation in the verified plan."
    captions = ["1. Push both sockets onto the module's pins.\n" + pitch_note,
                "2. Put the sandwich into the board.\n" + orientation_note + "\nFlip; solder ONE end pin.",
                "3. Check both sockets sit flat and upright.\nSolder within the specified process limits.\nThen pull the module out."]
    for i, (ax, cap) in enumerate(zip(axes, captions)):
        if i > 0:
            ax.add_patch(Rectangle((0, 0), 40, 1.6, fc="#2b4c7e", ec="k"))        # board
        for x in (7.3, 32.7):                                                      # illustrative socket positions; not actual geometry
            ax.add_patch(Rectangle((x - 1.3, 1.6 if i > 0 else 4.0), 2.6, 8.5, fc="#222", ec="k"))   # socket body
            ax.add_patch(Rectangle((x - 0.3, (1.6 if i > 0 else 4.0) - 3.0), 0.6, 3.0, fc="#aaa", ec="k", lw=0.4))  # socket pin
            ax.add_patch(Rectangle((x - 0.3, (1.6 if i > 0 else 4.0) + 8.5), 0.6, 2.5, fc="#aaa", ec="k", lw=0.4))  # module pin
        y0 = (1.6 if i > 0 else 4.0) + 11.0
        ax.add_patch(Rectangle((4.5, y0), 31, 2.2, fc="#2d5f2d", ec="k"))        # module board
        ax.text(20, y0 + 1.1, module, ha="center", va="center", fontsize=7, color="white")
        if i == 1:
            ax.plot([7.3], [1.3], marker="o", color="#c9c9c9", ms=9, mec="k"); ax.annotate("solder this one pin first", (7.3, 1.3), xytext=(12.0, -2.6), fontsize=6.5, arrowprops=dict(arrowstyle="->", lw=0.7))
        if i == 2:
            for x in (7.3, 32.7):
                ax.plot([x], [1.3], marker="o", color="#c9c9c9", ms=9, mec="k")
            ax.annotate("", xy=(32.7, -0.5), xytext=(7.3, -0.5), arrowprops=dict(arrowstyle="<->", lw=0.8))
            ax.text(20, -2.4, "measured plan spacing" if pitch_mm is None else "%.2f mm (plan)" % pitch_mm, ha="center", fontsize=6.5)
        ax.set_xlim(0, 40); ax.set_ylim(-4, 19); ax.set_aspect("equal"); ax.axis("off"); ax.set_title(cap, fontsize=7.5)
    fig.text(.5, .015, "METHOD ILLUSTRATION; not to scale. Actual geometry, orientation and soldering limits come from the verified plan.", ha="center", fontsize=7)
    fig.tight_layout(rect=(0, .06, 1, 1)); fig.savefig(out_png, dpi=200); plt.close(fig)
    return out_png


@_literal_figure
def draw_polarity_guide(out_png, cathode_hole=None, anode_hole=None, diode="Diode example", vf=None,
                        *, board=None):
    """Draw a terminal map for two explicit holes on the verified board."""
    if anode_hole is None or cathode_hole is None:
        raise ValueError(f"UNRESOLVED diode placement for {diode}. Supply both terminal holes.")
    geometry = board_geometry(board)
    roles = _diode_terminal_map({"name": diode, "anode_hole": anode_hole,
                                "cathode_hole": cathode_hole}, geometry)
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.patches import Rectangle
    cathode_hole = roles["cathode"]
    anode_hole = roles["anode"]
    test_note = "No meter acceptance criterion supplied; use the verified plan." if vf is None else "Plan-supplied forward value: " + str(vf) + "; reverse test and meter capability require the plan."
    fig, ax = plt.subplots(figsize=(7, 2.6))
    ax.plot([0.5, 9.5], [1.5, 1.5], color="#777", lw=3)                            # legs
    ax.add_patch(Rectangle((3.2, 0.9), 3.6, 1.2, fc="#111", ec="k"))              # body
    ax.annotate("", xy=(8.6, 2.6), xytext=(1.4, 2.6), arrowprops=dict(arrowstyle="->", lw=1.6, color="#c0392b"))
    ax.text(5.0, 2.85, "conventional forward-current direction", ha="center", fontsize=8, color="#c0392b")
    ax.text(1.0, 0.3, "ANODE end\nVerified hole: %s" % anode_hole, ha="center", va="top", fontsize=8)
    ax.text(9.0, 0.3, "CATHODE end\nVerified hole: %s" % cathode_hole, ha="center", va="top", fontsize=8, fontweight="bold")
    ax.text(5.0, 1.5, diode, ha="center", va="center", fontsize=7, color="white")
    ax.set_xlim(-0.5, 10.5); ax.set_ylim(-1.8, 3.3); ax.set_aspect("equal"); ax.axis("off")
    title = "DIODE TERMINAL MAP, not to scale. Verify the package's terminal markings from its documentation. " + test_note
    # Wrap the literal caption before Matplotlib measures it.
    ax.set_title(textwrap.fill(title, width=96, break_long_words=False, break_on_hyphens=False), fontsize=7.5)
    fig.tight_layout(); fig.savefig(out_png, dpi=200); plt.close(fig)
    return out_png


def _check_figure_targets(targets):
    # Reserve all known names, including a guide this run might omit.
    occupied = [path for path in targets if os.path.lexists(path)]
    if occupied:
        raise FileExistsError("Use a fresh output destination. Generated figure targets already exist: "
                              + ", ".join(occupied))


def draw_all(plan, outdir, prefix="board"):
    if not isinstance(prefix, str) or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_-]*", prefix):
        raise ValueError("prefix must be a simple filename stem using letters, digits, underscore or hyphen")
    g = _plan_geometry(plan)
    _validate_layout_endpoints(plan.get("pins") or (), plan["wires"], plan["rails"],
                               plan.get("components"), plan.get("joins"), g)
    _validate_part_positions(plan["parts"], plan.get("connectors"), g)
    placements = _diode_placements(plan.get("polarised"), plan["parts"], g)
    checks = continuity_checks(plan["wires"], plan["rails"], plan.get("polarised"), plan.get("headers"), g, plan.get("test_expectations"))
    names = (prefix + "_steps.png", prefix + "_back.png", prefix + "_tests.png",
             "joint_guide.png", "header_jig.png", "polarity_guide.png")
    targets = [os.path.join(outdir, name) for name in names]
    _check_figure_targets(targets)

    header_config = plan.get("header_jig", {})
    _validate_header_jig(header_config)
    for name, roles in placements.items():
        if roles["anode"] is None or roles["cathode"] is None:
            warnings.warn(f"UNRESOLVED diode placement for {name}. Verify both terminals before soldering.",
                          stacklevel=2)

    with tempfile.TemporaryDirectory(prefix="circuit-figures-") as staging:
        steps, back, tests, joint, header, polarity = [os.path.join(staging, name) for name in names]
        rendered = [draw_steps(plan, steps), draw_back(plan, back), draw_tests(plan, checks, tests),
                    draw_joint_guide(joint), draw_header_jig(header, **header_config)]
        for name, roles in placements.items():
            if roles["anode"] is not None and roles["cathode"] is not None:
                rendered.append(draw_polarity_guide(polarity,
                                                    cathode_hole=roles["cathode"], anode_hole=roles["anode"],
                                                    diode=name, vf=roles["vf"], board=g))
                break
        _check_figure_targets(targets)
        os.makedirs(outdir, exist_ok=True)
        for source, target in zip(rendered, targets):
            with open(source, "rb") as image, open(target, "xb") as destination:
                shutil.copyfileobj(image, destination)
    return targets[:len(rendered)]


if __name__ == "__main__":
    import json
    if len(sys.argv) < 3:
        print(__doc__); sys.exit(1)
    plan = json.load(open(sys.argv[1]))
    for p in draw_all(plan, sys.argv[2], plan.get("prefix", "board")):
        print(p)
