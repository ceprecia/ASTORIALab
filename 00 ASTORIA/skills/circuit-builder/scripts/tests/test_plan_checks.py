"""Test plan-driven circuit checks and figure labels; no physical validation."""
import json
import subprocess
import sys
import tempfile
import unittest
from copy import deepcopy
from pathlib import Path
from unittest.mock import patch

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from board_tools import (continuity_checks, run_plan, contact_purpose_rows,
                         connection_purpose_findings, order_build_steps)
import board_tools
import draw_build


class PlanChecks(unittest.TestCase):
    def setUp(self):
        self.board = "permaproto_half"
        self.rails = {"L1": "SUPPLY", "R1": "RETURN"}
        self.headers = [{"name": "J1", "holes": ["A1", "A2", "A3", "A4"]}]
        self.polarised = [{"name": "D1", "anode_hole": "A6", "cathode_hole": "F6", "vf": "from supplied part"}]

    def checks(self, expectations=None):
        return continuity_checks([], self.rails, self.polarised, self.headers,
                                 board=self.board, test_expectations=expectations)

    def test_imported_helpers_require_explicit_board_geometry(self):
        wire = {"no": 1, "net": "A", "frm": "A1", "to": "F1"}
        calls = [
            (board_tools.board_geometry, ()),
            (board_tools.hole_xy, ("A1",)),
            (board_tools.same_node, ("A1", "A2")),
            (board_tools.wire_length_mm, ("A1", "A2")),
            (board_tools.hole_under_module, ("A1", {"holes": ["A1"]})),
            (order_build_steps, ([], [])),
            (continuity_checks, ([], {})),
            (continuity_checks, ([wire], {})),
            (board_tools.layout_check, ([], [], {})),
            (board_tools.row_spacing_from_columns, ("A", "H")),
            (board_tools.columns_for_spacing, (25.4,)),
        ]
        for helper, args in calls:
            with self.subTest(helper=helper.__name__, args=args):
                with self.assertRaisesRegex(ValueError, "verified board geometry"):
                    helper(*args)

    def test_explicit_presets_and_custom_geometry_drive_probe_locations(self):
        presets = [
            ("electrocookie_half", (12.16, 7.60)),
            ("permaproto_half", (13.97, 6.35)),
        ]
        for board, coordinates in presets:
            with self.subTest(board=board):
                self.assertEqual(board_tools.hole_xy("A1", board), coordinates)
                self.assertEqual(continuity_checks([], self.rails, board=board)[0]["_holes"],
                                 ["L1@15", "R1@15"])
                self.assertIn("## Continuity table",
                              run_plan({"board": board, "parts": [], "wires": [], "rails": self.rails}))
        custom = deepcopy(board_tools.board_geometry(self.board))
        custom["rows"] = 10
        self.assertEqual(continuity_checks([], self.rails, None, None, custom)[0]["_holes"],
                         ["L1@5", "R1@5"])
        self.assertIn("L1 rail (SUPPLY)", run_plan({"board": custom, "parts": [], "wires": [], "rails": self.rails}))
        custom["rows"] = 1
        self.assertEqual(continuity_checks([], self.rails, board=custom)[0]["_holes"],
                         ["L1@1", "R1@1"])
        self.assertTrue(board_tools.same_node("A1", "B1", custom))
        self.assertFalse(board_tools.same_node("A1", "F1", custom))

    def test_invalid_geometry_fails_before_plan_or_drawing_output(self):
        valid = board_tools.board_geometry(self.board)
        invalid = [{}, {"rows": 2}]
        invalid.extend(dict(valid, **change) for change in [
            {"size_mm": [55.9, float("inf")]}, {"size_mm": [55.9, 0]},
            {"rows": True}, {"rows": 0}, {"rows": 1.5}, {"rows": 200},
            {"row0": -1}, {"pitch": 0}, {"columns": {}}, {"columns": {"B": 99}},
            {"rails": {"OTHER": 3}}, {"strips": [("UNKNOWN",)]},
            {"strips": [("A", "B"), ("B", "C")]}, {"tap_holes": {"TL": [1, 2, "L9"]}},
        ])
        wire = {"no": 1, "net": "SIGNAL", "frm": "A1", "to": "F1"}
        with tempfile.TemporaryDirectory() as temp:
            out = Path(temp) / "not_created"
            for geometry in invalid:
                with self.subTest(geometry=geometry):
                    for wires in ([], [wire]):
                        with self.assertRaisesRegex(ValueError, "Invalid custom board geometry"):
                            continuity_checks(wires, {}, board=geometry)
                    plan = {"board": geometry, "parts": [], "wires": [], "rails": {}, "pins": []}
                    with self.assertRaisesRegex(ValueError, "Invalid custom board geometry"):
                        run_plan(plan)
                    with self.assertRaisesRegex(ValueError, "Invalid custom board geometry"):
                        draw_build.draw_all(plan, out)
                    self.assertFalse(out.exists())

    def test_layout_rejects_invalid_endpoints_before_reports_or_drawings(self):
        ordinary = {"board": self.board, "pins": [], "wires": [], "parts": [], "rails": {}}
        cases = [
            ({"pins": [{"hole": "A99", "net": "N"}]}, "pin has invalid hole 'A99'"),
            ({"pins": [{"hole": "Z1", "net": "N"}]}, "pin has invalid hole 'Z1'"),
            ({"pins": [{"hole": "TL", "net": "N"}]}, "pin has invalid hole 'TL'"),
            ({"pins": [{"hole": None, "net": "N"}]}, "pin must name a board hole"),
            ({"wires": [{"frm": "invalid", "to": "A1", "net": "N"}]}, "wire start has invalid hole"),
            ({"wires": [{"frm": "A1", "to": "R1@0", "net": "N"}]}, "wire end has invalid hole"),
            ({"rails": {"L9": "N"}}, "rail has invalid hole"),
            ({"components": [{"name": "D1", "holes": ["A1", "B999"]}]}, "component has invalid hole"),
            ({"components": [{"name": "D1", "holes": "A1"}]}, "component holes must be a list"),
            ({"joins": [("A1", "A99")]}, "join has invalid hole"),
            ({"joins": [("A1",)]}, "join must name two board holes"),
        ]
        with tempfile.TemporaryDirectory() as temp:
            output = Path(temp) / "uncreated"
            for change, message in cases:
                with self.subTest(change=change):
                    plan = {**ordinary, **change}
                    with self.assertRaisesRegex(ValueError, message):
                        board_tools.layout_check(plan["pins"], plan["wires"], plan["rails"],
                                                 plan["board"], plan.get("components"),
                                                 plan.get("joins"))
                    with self.assertRaisesRegex(ValueError, message):
                        run_plan(plan)
                    with self.assertRaisesRegex(ValueError, message):
                        draw_build.draw_all(plan, output)
                    self.assertFalse(output.exists())
            bad_plan = Path(temp) / "invalid.json"
            bad_plan.write_text(json.dumps({**ordinary, **cases[0][0]}), encoding="utf-8")
            for module, extra in ((board_tools, []), (draw_build, [str(output)])):
                result = subprocess.run([sys.executable, "-B", module.__file__, str(bad_plan), *extra],
                                        capture_output=True, text=True)
                self.assertNotEqual(result.returncode, 0)
                self.assertEqual(result.stdout, "")
                self.assertIn(cases[0][1], result.stderr)
            self.assertFalse(output.exists())

    def test_layout_endpoint_validation_preserves_board_specific_connectivity(self):
        pins = [{"hole": "A1", "net": "N"}, {"hole": "B1", "net": "N"}]
        for board in ("permaproto_half", "electrocookie_half"):
            self.assertTrue(board_tools.layout_check(pins, [], {}, board)["ok"])
        custom = {"size_mm": [12, 12], "rows": 2, "row0": 2, "pitch": 3,
                  "columns": {"A": 2, "B": 5}, "rails": {"L1": 1},
                  "strips": [("A", "B")], "tap_holes": {"TL": (1, 1, "L1")}}
        self.assertTrue(board_tools.layout_check(pins, [], {}, custom)["ok"])
        tap = [{"hole": "TL", "net": "N"}]
        self.assertTrue(board_tools.layout_check(tap, [], {"L1": "N"}, custom)["ok"])
        self.assertFalse(board_tools.layout_check(tap, [], {"L1": "OTHER"}, custom)["ok"])
        no_pins = {"board": custom, "parts": [], "wires": [], "rails": {"R1": "N"}}
        with self.assertRaisesRegex(ValueError, "rail has invalid hole"):
            run_plan(no_pins)

    def test_layout_occupancy_counts_aliases_by_physical_hole(self):
        pins = [{"hole": "A1", "net": "N"}, {"hole": "B1", "net": "N"}]
        wires = [{"no": 1, "frm": "A01", "to": "F1", "net": "N"}]
        components = [{"name": "R1", "holes": [" a 1 ", "F2"]}]
        for board in ("permaproto_half", "electrocookie_half"):
            with self.subTest(board=board):
                findings = board_tools.layout_check(pins, wires, {}, board, components)["findings"]
                self.assertEqual(findings, ["hole A1 used 3 times: N, R1, wire 1"])
                self.assertTrue(board_tools.layout_check(pins, [], {}, board)["ok"])
        rail_pins = [{"hole": "L1@01", "net": "N"}, {"hole": " l1 @ 1 ", "net": "N"}]
        result = board_tools.layout_check(rail_pins, [], {}, self.board)
        self.assertEqual(result["findings"], ["hole L1@1 used 2 times: N, N"])

    def test_consumed_part_positions_fail_before_report_or_drawing_output(self):
        ordinary = {"board": self.board, "parts": [], "wires": [], "rails": {}}
        header = {"name": "J1", "kind": "header", "holes": ["A1 contact", "A2 contact"]}
        diode = {"name": "D1", "kind": "polarised", "holes": ["A1", "F1"], "polarity_mark": "band"}
        module = {"name": "M1", "kind": "module", "holes": []}
        cases = [
            ({"parts": [{**header, "holes": ["A99 labelled"]}]}, "part J1 has invalid hole"),
            ({"parts": [{**header, "holes": ["A1-A2"]}]}, "part J1 has invalid hole"),
            ({"parts": [{**header, "holes": "A1"}]}, "part J1 holes must be a list"),
            ({"parts": [{**header, "holes": ["A1 first", "a01 second"]}]}, "part J1 repeats a physical hole"),
            ({"parts": [{**header, "holes": []}]}, "part J1 must name its board holes"),
            ({"parts": [{**diode, "marked_hole": "F999"}]}, "part D1 marked_hole has invalid hole"),
            ({"parts": [{**diode, "marked_hole": "F2"}]}, "part D1 marked_hole must match"),
            ({"parts": [{**module, "covers": {"holes": ["A1", "F99"]}}]}, "module cover has invalid hole"),
            ({"parts": [{**module, "covers": {"rows": [1, 99], "cols": ["A", "F"]}}]},
             "module cover rows must be ordered and within"),
            ({"parts": [{**module, "covers": {"rows": [1, 2], "cols": ["A", "Z"]}}]},
             "module cover cols must name"),
            ({"parts": [{**module, "covers": {"holes": ["A1"], "margin_mm": float("inf")}}]},
             "module cover margin_mm must be finite"),
            ({"parts": [header], "connectors": [{"name": "J1", "pins": [{"hole": "A99"}]}]},
             "J1 connector has duplicate or unrelated hole"),
            ({"polarised": [{"name": "D1", "holes": ["A1", "F1", "Z9"]}]},
             "polarised:D1 has invalid hole"),
            ({"polarised": [{"name": "D1", "kind": "diode", "holes": ["A1", "F1"], "anode": "Z9 label"}]},
             "polarised:D1 anode has invalid hole"),
            ({"headers": [{"name": "J1", "holes": "A1"}]}, "header:J1 holes must be a list"),
        ]
        with tempfile.TemporaryDirectory() as temp:
            output = Path(temp) / "uncreated"
            for change, message in cases:
                with self.subTest(change=change):
                    plan = {**ordinary, **change}
                    with self.assertRaisesRegex(ValueError, message):
                        run_plan(plan)
                    with self.assertRaisesRegex(ValueError, message):
                        draw_build.draw_all(plan, output)
                    self.assertFalse(output.exists())
                    if "parts" in change:
                        image = Path(temp) / "uncreated.png"
                        for draw in (draw_build.draw_steps, draw_build.draw_back):
                            with self.assertRaisesRegex(ValueError, message):
                                draw(plan, image)
                            self.assertFalse(image.exists())

    def test_continuity_rejects_absent_board_holes_or_rails(self):
        geometry = {"size_mm": [12, 12], "rows": 2, "row0": 2, "pitch": 3,
                    "columns": {"A": 2, "B": 5}, "rails": {"L1": 1},
                    "strips": [("A", "B")]}
        for kwargs, message in (
            ({"rails": {"L1": "N", "R1": "M"}}, "rail has invalid hole 'R1@1'"),
            ({"wires": [{"frm": "A1", "to": "A99", "net": "N"}]}, "wire end has invalid hole"),
            ({"headers": [{"name": "J1", "holes": ["B99"]}]}, "header:J1 has invalid hole"),
            ({"polarised": [{"name": "D1", "holes": ["A1", "B99"]}]}, "polarised:D1 has invalid hole"),
        ):
            arguments = {"wires": [], "rails": {}, "board": geometry, **kwargs}
            with self.subTest(arguments=arguments), self.assertRaisesRegex(ValueError, message):
                continuity_checks(**arguments)
        unresolved = continuity_checks([], {}, [{"name": "D1"}], board=geometry)
        self.assertEqual(unresolved[0]["status"], "unresolved")

    def test_distinct_hole_identities_cannot_claim_the_same_position(self):
        valid = {"size_mm": [20, 20], "rows": 3, "row0": 0.1, "pitch": 0.2,
                 "columns": {"A": 2, "B": 4}, "rails": {"L1": 1, "R1": 8},
                 "strips": [("A", "B")],
                 "tap_holes": {"TL": (1, 1.2, "L1"), "TR": (8, 1.2, "R1")}}
        collisions = [
            ({"columns": {"A": 2, "B": 2}}, "lanes A and B"),
            ({"rails": {"L1": 2, "R1": 8}}, "lanes A and L1"),
            ({"rails": {"L1": 1, "R1": 1}}, "lanes L1 and R1"),
            ({"tap_holes": {"TL": (1, 1.2, "L1"), "TR": (1, 1.2, "R1")}}, "taps TL and TR"),
            ({"tap_holes": {"TL": (2, 0.3, "L1")}}, "tap TL and A2"),
            ({"tap_holes": {"TL": (1, 0.3, "L1")}}, "tap TL and L1@2"),
            ({"row0": 10.0, "pitch": 1e-18}, "rows 1 and 2"),
        ]
        for change, message in collisions:
            with self.subTest(collision=message):
                geometry = dict(valid, **change)
                with self.assertRaisesRegex(ValueError, message + " share a physical hole position"):
                    board_tools.layout_check([], [], {}, geometry)
        geometry = {"size_mm": [12, 12], "rows": 2, "row0": 2, "pitch": 3,
                    "columns": {"B": 3, "C": 3}, "rails": {}, "strips": []}
        with self.assertRaisesRegex(ValueError, "lanes B and C share a physical hole position"):
            board_tools.hole_xy("B1", geometry)
        wire = {"no": 1, "net": "SIGNAL", "frm": "B1", "to": "C1"}
        for wires in ([], [wire]):
            plan = {"board": geometry, "parts": [], "wires": wires, "rails": {}, "pins": []}
            with self.subTest(wires=wires), self.assertRaisesRegex(ValueError, "share a physical hole position"):
                run_plan(plan)
        with tempfile.TemporaryDirectory() as temp:
            out = Path(temp) / "not_created"
            with self.assertRaisesRegex(ValueError, "share a physical hole position"):
                draw_build.draw_all(plan, out)
            self.assertFalse(out.exists())

    def test_distinct_hole_positions_can_share_electrical_nodes(self):
        geometry = {"size_mm": [20, 20], "rows": 3, "row0": 0.1, "pitch": 0.2,
                    "columns": {"A": 2, "B": 4}, "rails": {"L1": 1, "R1": 8},
                    "strips": [("A", "B")],
                    "tap_holes": {"TL": (1, 1.2, "L1"), "TR": (8, 1.2, "R1"),
                                  "BL": (5, 0.3, "L1")}}
        for first, second in (("A1", "B1"), ("TL", "L1@2")):
            self.assertNotEqual(board_tools.hole_xy(first, geometry), board_tools.hole_xy(second, geometry))
            self.assertTrue(board_tools.same_node(first, second, geometry))
        self.assertFalse(board_tools.same_node("A1", "B2", geometry))
        self.assertTrue(board_tools.layout_check([], [], {}, geometry)["ok"])
        for name in ("electrocookie_half", "permaproto_half"):
            preset = board_tools.board_geometry(name)
            self.assertEqual(board_tools.board_geometry(deepcopy(preset)), preset)

    def test_missing_criteria_are_unresolved_for_all_pairs(self):
        rows = self.checks()
        self.assertEqual([row["_check_id"] for row in rows], [
            "rail:L1:R1", "polarised:D1", "header:J1:A1:A2",
            "header:J1:A2:A3", "header:J1:A3:A4"])
        self.assertTrue(all(row["status"] == "unresolved" for row in rows))
        self.assertTrue(all("UNRESOLVED" in row["expect"] for row in rows))
        self.assertIn("Supplied forward value: from supplied part", rows[1]["expect"])
        self.assertNotIn(" OL", rows[1]["expect"])

    def test_complete_plan_criterion_is_preserved(self):
        spec = {"mode": "resistance", "expect": "verified range", "basis": "plan section 4"}
        row = self.checks({"rail:L1:R1": spec})[0]
        for key, value in spec.items():
            self.assertEqual(row[key], value)
        self.assertEqual(row["status"], "plan-supplied criterion")

    def test_invalid_expectations_fail_instead_of_being_dropped(self):
        for value in [{"unknown": {}}, {"rail:L1:R1": {"mode": "voltage"}},
                      {"rail:L1:R1": {"expect": 0}}, {1: {}}, []]:
            with self.subTest(value=value), self.assertRaises(ValueError):
                self.checks(value)

    def test_verified_probe_assignment_matches_physical_endpoints(self):
        check_id = "polarised:D1"
        criterion = "Reading >= -600 mV and <= -300 mV"
        spec = {"mode": "diode", "source": {"reference": 4, "section": 2},
                "measurement": {"unit": "mV", "at_least": -600, "at_most": -300},
                "probes": {"red": "f06", "black": " a6 ", "verified": True}}
        row = self.checks({check_id: spec})[1]
        self.assertEqual(row["_holes"], ["A6", "F6"])
        self.assertEqual(row["_probes"], {"red": "F6", "black": "A6"})
        self.assertEqual((row["mode"], row["expect"], row["basis"]),
                         (spec["mode"], criterion, "Plan source 4, section 2"))
        self.assertIn("red lead: F6, black lead: A6", row["touch"])
        with self.assertRaisesRegex(ValueError, "require mode, probes, measurement and source"):
            self.checks({check_id: {key: value for key, value in spec.items() if key != "source"}})

    def test_conflicting_probe_assignments_are_rejected(self):
        check_id = "polarised:D1"
        probes = {"red": "F6", "black": "A6", "verified": True}
        spec = {"mode": "diode", "source": {"reference": 4, "page": 2}, "probes": probes,
                "measurement": {"unit": "V", "below": 1}}
        invalid = [
            {**spec, "probes": None},
            {**spec, "probes": {"red": "F6", "black": "A6"}},
            {**spec, "probes": {**probes, "verified": 1}},
            {**spec, "probes": {**probes, "verified": False}},
            {**spec, "probes": {**probes, "black": ""}},
            {**spec, "probes": {**probes, "black": "f06"}},
            {**spec, "probes": {**probes, "black": "B6"}},
            {**spec, "probes": {**probes, "red": "F999"}},
            {**spec, "probes": {**probes, "other": "B6"}},
            {**spec, "mode": "visual"},
        ]
        for bad in invalid:
            with self.subTest(bad=bad), self.assertRaisesRegex(ValueError, check_id):
                self.checks({check_id: bad})
        with self.assertRaisesRegex(ValueError, "ambiguous check ID"):
            continuity_checks([], {}, self.polarised * 2, board=self.board,
                              test_expectations={check_id: spec})
        with tempfile.TemporaryDirectory() as temp:
            output = Path(temp) / "uncreated"
            plan = {"board": self.board, "parts": [], "wires": [], "rails": {},
                    "polarised": self.polarised, "test_expectations": {check_id: invalid[-1]}}
            with self.assertRaisesRegex(ValueError, check_id):
                draw_build.draw_all(plan, output)
            self.assertFalse(output.exists())

    def test_structured_probes_reject_every_free_text_criterion(self):
        check_id = "polarised:D1"
        expectation = {"mode": "diode", "source": {"reference": 4, "section": 2},
                       "measurement": {"unit": "V", "above": -0.6},
                       "probes": {"red": "F6", "black": "A6", "verified": True}}
        directions = (
            "Red A6 and black F6. The indicated drop stays within the plan's range.",
            "Red F6 and black A6. The indicated drop stays within the plan's range.",
            "HI on A6 and LO on F6. Reading < 0.4 V.",
            "Channel Zulu goes at the first connection, Tango at the second.",
            "The red meter indicator illuminates.",
            "Reading < 0.4 V.",
            "",
            None,
        )
        message = check_id + ": free-text expect or basis cannot be combined"
        for holes in (["A6", "F6"], ["F6", "A6"]):
            plan = {"board": self.board, "parts": [], "wires": [], "rails": {},
                    "polarised": [{"name": "D1", "holes": holes}],
                    "test_expectations": {check_id: expectation}}
            checked = continuity_checks([], {}, plan["polarised"], board=self.board,
                                        test_expectations=plan["test_expectations"])
            self.assertEqual(checked[0]["expect"], "Reading > -0.6 V")
            with tempfile.TemporaryDirectory() as temp:
                output = Path(temp) / "uncreated"
                figure = Path(temp) / "check.png"
                for field in ("expect", "basis"):
                    for criterion in directions:
                        with self.subTest(field=field, criterion=criterion, holes=holes):
                            mixed = {**expectation, field: criterion}
                            conflicting_plan = {**plan, "test_expectations": {check_id: mixed}}
                            with self.assertRaisesRegex(ValueError, message):
                                run_plan(conflicting_plan)
                            with self.assertRaisesRegex(ValueError, message):
                                draw_build.draw_all(conflicting_plan, output)
                            with self.assertRaisesRegex(ValueError, message):
                                draw_build.draw_tests(conflicting_plan, checked, figure)
                            if isinstance(criterion, str) and criterion:
                                legacy = {"mode": "diode", "expect": "Reading < 0.4 V.",
                                          "basis": "Verified plan section 4", field: criterion}
                                rows = continuity_checks([], {}, plan["polarised"], board=self.board,
                                                        test_expectations={check_id: legacy})
                                self.assertEqual(rows[0][field], criterion)
                                self.assertNotIn("_probes", rows[0])
                self.assertFalse(output.exists())
                self.assertFalse(figure.exists())

    def test_structured_measurements_require_explicit_finite_compatible_limits(self):
        check_id = "polarised:D1"
        probe = {"red": "F6", "black": "A6", "verified": True}
        spec = {"mode": "diode", "source": {"reference": 4, "section": 2}, "probes": probe}
        valid = (
            ("diode", {"unit": "V", "below": -0.3}, "Reading < -0.3 V"),
            ("resistance", {"unit": "kΩ", "at_most": 4.5}, "Reading <= 4.5 kΩ"),
            ("continuity", {"unit": "Ω", "at_least": 0, "at_most": 0},
             "Reading >= 0 Ω and <= 0 Ω"),
        )
        for mode, measurement, label in valid:
            with self.subTest(mode=mode, measurement=measurement):
                rows = self.checks({check_id: {**spec, "mode": mode, "measurement": measurement}})
                self.assertEqual(rows[1]["expect"], label)
                self.assertEqual(rows[1]["_probes"], {"red": "F6", "black": "A6"})
        for measurement in (
            None,
            {},
            {"unit": "V"},
            {"unit": "V", "below": None},
            {"unit": "V", "at_most": True},
            {"unit": "V", "above": "HI"},
            {"unit": "V", "below": float("inf")},
            {"unit": "V", "at_least": float("nan")},
            {"unit": ["V"], "below": 1},
            {"unit": "Ω", "below": 1},
            {"unit": "V with HI on A6", "below": 1},
            {"unit": "V", "below": 1, "aliases": "HI and LO"},
            {"unit": "V", "at_least": -1, "above": 0},
            {"unit": "V", "at_least": 3, "at_most": 2},
            {"unit": "V", "above": 1, "at_most": 1},
        ):
            with self.subTest(measurement=measurement), self.assertRaisesRegex(ValueError, check_id):
                self.checks({check_id: {**spec, "measurement": measurement}})
        for source in (
            "Verified plan section 4",
            {"reference": 4, "section": "2 HI on SUPPLY"},
            {"reference": "4", "section": 2},
            {"reference": 4, "section": True},
            {"reference": 4, "section": 2, "page": 5},
            {"reference": 4, "step": 0},
            {"reference": 1000000, "step": 2},
            {"reference": 4, "locator": 2},
            {"reference": 4},
        ):
            with self.subTest(source=source), self.assertRaisesRegex(ValueError, check_id):
                self.checks({check_id: {**spec, "source": source,
                                       "measurement": {"unit": "V", "below": 1}}})
        with self.assertRaisesRegex(ValueError, "require mode, probes, measurement and source"):
            self.checks({check_id: spec})
        with self.assertRaisesRegex(ValueError, "require mode, probes, measurement and source"):
            self.checks({check_id: {"mode": "diode", "source": spec["source"],
                                   "measurement": {"unit": "V", "below": 1}}})

    def test_markdown_table_escapes_cell_delimiters_without_changing_criterion(self):
        criterion = "Reading | stable\r\n" + r"Literal \| observation" + "\\\rLast line\nDone"
        spec = {"mode": "resistance", "expect": criterion, "basis": "Plan | criterion"}
        expectations = {"rail:L1:R1": spec}
        rows = self.checks(expectations)
        original = deepcopy(rows)
        table = board_tools.markdown_table(rows)
        rendered = r"Reading \| stable<br>Literal \\\| observation\\<br>Last line<br>Done"
        self.assertEqual(len(table.splitlines()), len(rows) + 2)
        self.assertIn(f"| {rendered} | Plan \\| criterion |", table.splitlines()[2])
        self.assertEqual(rows, original)
        self.assertEqual(rows[0]["expect"], criterion)
        self.assertEqual(expectations["rail:L1:R1"]["expect"], criterion)
        plan = {"board": self.board, "parts": [], "wires": [], "rails": self.rails,
                "polarised": self.polarised, "headers": self.headers,
                "test_expectations": expectations}
        self.assertIn(table, run_plan(plan))

        heading = "First | second\r\nThird"
        self.assertEqual(board_tools.markdown_table([{heading: "Value"}], [heading]),
                         r"| First \| second<br>Third |" + "\n| --- |\n| Value |")

    def test_direct_wire_connection_retains_a_bounded_check(self):
        row = continuity_checks([{"no": 1, "net": "A", "frm": "A1", "to": "F1"}],
                                {}, board=self.board)[0]
        self.assertEqual(row["mode"], "continuity")
        self.assertIn("intended direct connection", row["expect"])
        self.assertIn("alternate paths", row["means"])


class ConnectionPurposeChecks(unittest.TestCase):
    def setUp(self):
        self.part = {"ref": "J1", "name": "Instrument controls", "kind": "header",
                     "holes": ["A10", "A11", "A12"], "contacts": [
                         {"pin": "3", "hole": "A12", "device": "Chamber valve", "function": "command", "net": "CMD_VALVE"},
                         {"pin": "1", "hole": "A10", "device": "Indicator lamp", "function": "command", "net": "CMD_LAMP", "controller_endpoint": "Controller D7"},
                         {"pin": "2", "hole": "A11", "device": "Service switch", "function": "pressed input", "net": "SERVICE"}]}

    def test_physical_hole_order_does_not_invent_device_order(self):
        original = deepcopy(self.part)
        rows = contact_purpose_rows(self.part)
        self.assertEqual([(r["contact"], r["hole"], r["device"]) for r in rows], [
            ("J1.1", "A10", "Indicator lamp"), ("J1.2", "A11", "Service switch"),
            ("J1.3", "A12", "Chamber valve")])
        self.assertTrue(all(r["status"] == "resolved" for r in rows))
        self.assertEqual(rows[0]["controller_endpoint"], "Controller D7")
        self.assertEqual(self.part, original)
        text = order_build_steps([self.part], [], "permaproto_half")[0]["detail"]
        for row in rows:
            for value in (row["contact"], row["hole"], row["device"], row["function"]):
                self.assertIn(value, text)

    def test_reference_only_annotations_do_not_require_a_display_name(self):
        part = deepcopy(self.part)
        del part["name"]
        self.assertEqual(contact_purpose_rows(part)[0]["contact"], "J1.1")
        self.assertEqual(connection_purpose_findings([part]), [])
        duplicate = deepcopy(part)
        duplicate["holes"].append(duplicate["holes"][0])
        with self.assertRaisesRegex(ValueError, "Repeated hole in J1"):
            contact_purpose_rows(duplicate)
        del part["ref"]
        with self.assertRaisesRegex(ValueError, "ref or name"):
            contact_purpose_rows(part)

    def test_shared_ground_and_generic_note_cannot_hide_missing_purpose(self):
        part = {"ref": "J2", "name": "Ground", "kind": "header", "holes": ["A1", "A2"],
                "note": "Ground connections"}
        connectors = [{"ref": "J2", "pins": [
            {"pin": "1", "hole": "A1", "name": "GND", "net": "GND"},
            {"pin": "2", "hole": "A2", "name": "GND", "net": "GND"}]}]
        findings = connection_purpose_findings([part], connectors)
        self.assertEqual(len(findings), 2)
        self.assertIn("J2.1 / A1: UNRESOLVED device, function", findings)
        self.assertIn("J2.2 / A2: UNRESOLVED device, function", findings)
        part["contacts"] = [{"pin": "1", "hole": "A1", "device": "Sensor alpha", "function": "ground return"}]
        self.assertEqual(len(connection_purpose_findings([part], connectors)), 1)
        part["contacts"].append({"pin": "2", "hole": "A2", "device": "Service switch", "function": "ground side"})
        self.assertEqual(connection_purpose_findings([part], connectors), [])
        self.assertEqual([row["net"] for row in contact_purpose_rows(part, connectors)], ["GND", "GND"])

    def test_legacy_missing_metadata_is_explicit_without_altering_layout(self):
        plan = {"board": "permaproto_half", "parts": [
            {"name": "J1", "kind": "header", "holes": ["A1", "A2"]}], "wires": [], "rails": {}}
        text = run_plan(plan)
        self.assertIn("Connection purposes: UNRESOLVED", text)
        self.assertIn("J1 at A1 / A1: UNRESOLVED", text)
        self.assertIn("J1 at A2 / A2: UNRESOLVED", text)

    def test_conflicting_holes_indices_and_nets_are_rejected(self):
        for edit in [lambda p: p["contacts"].append(dict(p["contacts"][0])),
                     lambda p: p["contacts"][0].update(hole="F20"),
                     lambda p: p["contacts"][0].update(pin="1")]:
            part = deepcopy(self.part); edit(part)
            with self.assertRaises(ValueError):
                contact_purpose_rows(part)
        with self.assertRaisesRegex(ValueError, "changes net"):
            contact_purpose_rows(self.part, [{"ref": "J1", "pins": [
                {"pin": "1", "hole": "A10", "net": "WRONG_NET"}]}])

    def test_sparse_connector_merge_rejects_pin_reused_at_another_hole(self):
        part = deepcopy(self.part)
        del part["contacts"][1]["pin"]
        part["contacts"][2]["pin"] = " 1 "
        connectors = [{"ref": "J1", "pins": [{"pin": 1, "hole": "A10", "net": "CMD_LAMP"}]}]
        plan = {"board": "permaproto_half", "parts": [part], "wires": [], "rails": {},
                "connectors": connectors}
        message = "J1 has duplicate contact index 1 at A10 and A11"
        with self.assertRaisesRegex(ValueError, message):
            contact_purpose_rows(part, connectors)
        with self.assertRaisesRegex(ValueError, message):
            run_plan(plan)
        with tempfile.TemporaryDirectory() as temp:
            folder = Path(temp)
            plan_path = folder / "plan.json"
            plan_path.write_text(json.dumps(plan), encoding="utf-8")
            cli = subprocess.run([sys.executable, board_tools.__file__, str(plan_path)],
                                 capture_output=True, text=True)
            self.assertNotEqual(cli.returncode, 0)
            self.assertEqual(cli.stdout, "")
            self.assertIn(message, cli.stderr)
            outdir = folder / "figures"
            with self.assertRaisesRegex(ValueError, message):
                draw_build.draw_all(plan, outdir)
            self.assertFalse(outdir.exists())

    def test_connector_merge_keeps_valid_sparse_complete_and_unannotated_rows(self):
        part = deepcopy(self.part)
        del part["contacts"][1]["pin"]
        complete = [{key: item[key] for key in ("pin", "hole", "net")}
                    for item in self.part["contacts"]]
        for pins in ([complete[1]], complete):
            with self.subTest(connector_pins=pins):
                rows = contact_purpose_rows(part, [{"ref": "J1", "pins": pins}])
                self.assertEqual([(row["pin"], row["hole"], row["status"]) for row in rows], [
                    ("1", "A10", "resolved"), ("2", "A11", "resolved"), ("3", "A12", "resolved")])
        other = {"ref": "J2", "name": "Second connector", "kind": "header", "holes": ["F10"],
                 "contacts": [{"hole": "F10", "device": "Service lamp", "function": "return"}]}
        connectors = [{"ref": "J1", "pins": complete},
                      {"ref": "J2", "pins": [{"pin": 1, "hole": "F10", "net": "GND"}]}]
        self.assertEqual(connection_purpose_findings([part, other], connectors), [])
        self.assertEqual(contact_purpose_rows(other, connectors)[0]["contact"], "J2.1")
        del other["contacts"]
        row = contact_purpose_rows(other, connectors)[0]
        self.assertEqual((row["contact"], row["net"], row["status"]), ("J2.1", "GND", "unresolved"))

    def test_explicit_unused_contact_and_zero_index_are_supported(self):
        part = {"name": "U1", "holes": ["A1"], "contacts": [
            {"pin": 0, "hole": "A1", "device": "Module D0", "function": "no added external connection",
             "no_connect": True, "net": None}]}
        row = contact_purpose_rows(part)[0]
        self.assertEqual(row["status"], "resolved")
        self.assertEqual(row["net"], "NC (no added connection)")
        part["contacts"][0]["net"] = "ASSIGNED"
        with self.assertRaisesRegex(ValueError, "electrically assigned"):
            contact_purpose_rows(part)

    def test_explicit_connector_pin_must_identify_one_hole_across_parts(self):
        first = {"ref": "J1", "name": "Connector section", "kind": "header", "holes": ["A10"],
                 "contacts": [{"hole": "A10", "pin": 1}]}
        second = {"ref": " J1 ", "name": "Connector section", "kind": "pigtail", "holes": ["A11"],
                  "contacts": [{"hole": "A11", "pin": "1"}]}
        parts = [first, second]
        plan = {"board": "permaproto_half", "parts": parts, "wires": [], "rails": {}}
        message = "J1 has duplicate contact index 1 at A10 and A11"
        with self.assertRaisesRegex(ValueError, message):
            connection_purpose_findings(parts)
        with self.assertRaisesRegex(ValueError, message):
            run_plan(plan)
        with tempfile.TemporaryDirectory() as temp:
            outdir = Path(temp) / "figures"
            with self.assertRaisesRegex(ValueError, message):
                draw_build.draw_all(plan, outdir)
            self.assertFalse(outdir.exists())

        second["contacts"][0]["pin"] = "2"
        self.assertEqual(len(connection_purpose_findings(parts)), 2)
        second["holes"] = ["a010"]
        second["contacts"] = [{"hole": "a010", "pin": "1"}]
        self.assertEqual(len(connection_purpose_findings(parts)), 2)

        del first["ref"], second["ref"]
        second["holes"] = ["A11"]
        second["contacts"] = [{"hole": "A11", "pin": "1"}]
        self.assertEqual(len(connection_purpose_findings(parts)), 2)


class FigureChecks(unittest.TestCase):
    def stub_batch_figures(self):
        def write(path):
            Path(path).write_bytes(b"test figure")
            return path

        return patch.multiple(draw_build,
                              draw_steps=lambda _plan, path: write(path),
                              draw_back=lambda _plan, path: write(path),
                              draw_tests=lambda _plan, _checks, path: write(path),
                              draw_joint_guide=write,
                              draw_header_jig=lambda path, **_settings: write(path))

    def capture(self, draw, *args, check_purpose_bounds=False, check_probe_bounds=False, **kwargs):
        import matplotlib.pyplot as plt
        from matplotlib.figure import Figure
        captured = []
        def savefig(figure, *_args, **_kwargs):
            captured.append(figure)
        with patch.object(Figure, "savefig", savefig):
            draw(*args, **kwargs)
        if check_purpose_bounds or check_probe_bounds:
            from matplotlib.backends.backend_agg import FigureCanvasAgg
            for fig in captured:
                canvas = FigureCanvasAgg(fig)
                canvas.draw()
                for item in fig.findobj():
                    label = item.get_text() if hasattr(item, "get_text") else ""
                    if (check_purpose_bounds and "J1." in label
                            or check_probe_bounds and (label.startswith("Check ") or label in ("Red lead", "Black lead"))):
                        bounds = item.get_window_extent(canvas.get_renderer())
                        if check_probe_bounds and label.startswith("Check "):
                            heading = next(t for t in fig.texts if t.get_text().startswith("Unpowered checks:"))
                            self.assertLess(bounds.y1 + 4, heading.get_window_extent(canvas.get_renderer()).y0)
                        self.assertGreaterEqual(bounds.x0, fig.bbox.x0)
                        self.assertGreaterEqual(bounds.y0, fig.bbox.y0)
                        self.assertLessEqual(bounds.x1, fig.bbox.x1)
                        self.assertLessEqual(bounds.y1, fig.bbox.y1)
        text = "\n".join(item.get_text() for fig in captured for item in fig.findobj()
                         if hasattr(item, "get_text"))
        plt.close("all")
        return text

    def test_modes_and_unresolved_locations_are_labeled(self):
        rows = [
            {"mode": "diode", "status": "plan-supplied criterion", "expect": "specified test", "_holes": ["A1", "F1"]},
            {"mode": "resistance", "status": "plan-supplied criterion", "expect": "specified test", "_holes": ["A2", "F2"]},
            {"mode": "not specified", "status": "unresolved", "expect": "UNRESOLVED", "_holes": ["A3", "F3"]},
        ]
        text = self.capture(draw_build.draw_tests, {"board": "permaproto_half", "wires": []}, rows, "unused.png")
        self.assertIn("Check 1: diode", text)
        self.assertIn("Check 2: resistance", text)
        self.assertIn("Check 3: UNRESOLVED; do not select a meter setting", text)
        self.assertIn("3 of 3 checks", text)

    def test_empty_test_locations_render_an_explanation(self):
        text = self.capture(draw_build.draw_tests, {"board": "permaproto_half", "wires": []}, [], "unused.png")
        self.assertIn("No probe locations supplied", text)

    def test_every_header_contact_purpose_survives_step_and_back_figures(self):
        holes = ["A" + str(n) for n in range(1, 13)]
        contacts = [{"pin": str(n), "hole": hole, "device": "Assigned device " + str(n),
                     "function": "independent sensor supply branch", "net": "SHARED_SUPPLY",
                     "voltage": "3.3 V"} for n, hole in enumerate(holes, 1)]
        part = {"name": "Supply branches", "ref": "J1", "kind": "header", "holes": holes, "contacts": contacts}
        plan = {"board": "permaproto_half", "parts": [part], "wires": [], "rails": {}}
        for draw in [draw_build.draw_steps, draw_build.draw_back]:
            text = self.capture(draw, plan, "unused.png", check_purpose_bounds=True)
            text = " ".join(text.split())
            for n, hole in enumerate(holes, 1):
                self.assertIn("J1." + str(n) + " / " + hole, text)
                self.assertIn("Assigned device " + str(n), text)
            self.assertIn("independent sensor supply branch", text)
            self.assertIn("3.3 V", text)

    def test_rear_solder_points_follow_shared_actions_and_keep_exact_references(self):
        shared_name = "Wire fitting in frame"
        header_holes = ["A5", "A6", "A7", "A8"]
        plan = {
            "board": "permaproto_half", "rails": {},
            "wires": [{"no": 4, "net": "EXPOSED", "frm": "A10", "to": "F10"},
                      {"no": 4, "net": "UNDER", "frm": "A1", "to": "F1"}],
            "parts": [
                {"name": shared_name, "ref": "P1", "kind": "panel", "holes": ["A12", "F12"]},
                {"name": "Plug-in sample", "kind": "module", "holes": ["A2", "F2"],
                 "covers": {"rows": [1, 2], "cols": ["A", "F"], "margin_mm": 0}},
                {"name": "Socket in cradle", "ref": "J1", "kind": "header", "holes": header_holes,
                 "contacts": [{"pin": str(i), "hole": h, "device": "Indicator " + str(i),
                               "function": "supply branch"} for i, h in enumerate(header_holes, 1)]},
                {"name": shared_name, "kind": "polarised", "holes": ["A3", "F3"]},
                {"name": "Loose fixture", "kind": "fixture", "holes": ["A14", "F14"]},
            ],
        }
        original = deepcopy(plan)
        steps = order_build_steps(plan["parts"], plan["wires"], plan["board"])
        self.assertEqual([step.get("_action") for step in steps],
                         [("wire", 1), ("part", 3), ("part", 2), ("wire", 0),
                          ("part", 0), None, ("module", 1)])
        with patch.object(draw_build, "_wire", wraps=draw_build._wire) as wire:
            front = self.capture(draw_build.draw_steps, plan, "unused.png")
        self.assertEqual([call.args[2:4] for call in wire.call_args_list if "alpha" not in call.kwargs],
                         [("A1", "F1"), ("A3", "F3"), ("A10", "F10")])
        self.assertIn("Socket in cradle", front)

        numbered = []
        draw_hole = draw_build._hole

        def record_hole(ax, geometry, hole, colour, **kwargs):
            draw_hole(ax, geometry, hole, colour, **kwargs)
            self.assertTrue(kwargs.get("mirror"))
            x, y = board_tools.hole_xy(hole, geometry)
            self.assertEqual(ax.patches[-1].center, (geometry["size_mm"][0] - x, y))
            numbered.append((hole, kwargs.get("label")))

        with patch.object(draw_build, "_hole", side_effect=record_hole):
            back = self.capture(draw_build.draw_back, plan, "unused.png", check_purpose_bounds=True)
        self.assertEqual(numbered, [("A1", 1), ("F1", 2), ("A3", 3), ("F3", 4),
                                    *[(h, None) for h in header_holes],
                                    ("A10", 9), ("F10", 10), ("A12", 11), ("F12", 12)])
        self.assertIn("\n5-8\n", back)
        back = " ".join(back.split())
        for label in ("1-2 wire 4 (UNDER): A1 to F1", "3-4 Wire fitting in frame: A3, F3",
                      "5-8 Socket in cradle: A5, A6, A7, A8",
                      "9-10 wire 4 (EXPOSED): A10 to F10", "11-12 Wire fitting in frame: A12, F12"):
            self.assertIn(label, back)
        for i, hole in enumerate(header_holes, 1):
            self.assertIn(f"J1.{i} / {hole}: Indicator {i}; supply branch", back)
        self.assertNotIn("Plug-in sample", back)
        self.assertNotIn("Loose fixture", back)
        self.assertEqual(plan, original)

    def test_neutral_wire_strokes_keep_net_labels_and_location_markers(self):
        plan = {"board": "permaproto_half", "parts": [], "rails": {"L1": "SUPPLY", "R1": "RETURN"},
                "wires": [{"no": 1, "net": "GND", "frm": "A1", "to": "F1"},
                          {"no": 2, "net": "SIGNAL_A", "frm": "A2", "to": "F2"}]}
        for draw in [draw_build.draw_steps, draw_build.draw_back]:
            with self.subTest(draw=draw.__name__), patch.object(draw_build, "_wire", wraps=draw_build._wire) as wire:
                text = self.capture(draw, plan, "unused.png")
                self.assertIn("GND", text)
                self.assertIn("SIGNAL_A", text)
                self.assertEqual({call.args[4] for call in wire.call_args_list}, {"#d9e1ea"})
        checks = continuity_checks(plan["wires"], plan["rails"], board=plan["board"])
        with patch.object(draw_build, "_wire", wraps=draw_build._wire) as wire, \
             patch.object(draw_build, "_hole", wraps=draw_build._hole) as hole:
            self.capture(draw_build.draw_tests, plan, checks, "unused.png")
            self.assertEqual({call.args[4] for call in wire.call_args_list}, {"#d9e1ea"})
            self.assertEqual([call.args[3] for call in hole.call_args_list],
                             ["#d9e1ea"] * 6)

    def test_reverse_criterion_does_not_colour_markers_by_hole_order(self):
        criterion = "Red F6 cathode, black A6 anode"
        spec = {"mode": "diode", "expect": criterion, "basis": "Verified plan section 4"}
        plan = {"board": "permaproto_half", "wires": [], "rails": {}, "parts": [],
                "polarised": [{"name": "D1", "holes": ["A6", "F6"]}],
                "test_expectations": {"polarised:D1": spec}}
        checks = continuity_checks([], {}, plan["polarised"], board=plan["board"],
                                   test_expectations=plan["test_expectations"])
        original = deepcopy(checks)
        self.assertEqual(checks[0]["_holes"], ["A6", "F6"])
        with patch.object(draw_build, "_hole", wraps=draw_build._hole) as hole:
            text = self.capture(draw_build.draw_tests, plan, checks, "unused.png")
        self.assertEqual([(call.args[2], call.args[3]) for call in hole.call_args_list],
                         [("A6", "#d9e1ea"), ("F6", "#d9e1ea")])
        self.assertIn(criterion, text)
        self.assertIn("Follow the verified table for meter mode, criterion and lead orientation.", text)
        self.assertIn(criterion, board_tools.markdown_table(checks))
        self.assertEqual(checks, original)

    def test_verified_probe_figure_reverses_hole_order_and_keeps_exact_criterion(self):
        measurement = {"unit": "V", "at_least": -0.6543210987654321,
                       "below": -0.3456789012345678}
        criterion = "Reading >= -0.6543210987654321 V and < -0.3456789012345678 V"
        check_id = "polarised:D1"
        plan = {"board": "permaproto_half", "parts": [], "rails": {},
                "wires": [{"no": 1, "net": "RETURN", "frm": "A1", "to": "F1"}],
                "polarised": [{"name": "D1", "holes": ["A6", "F6"]}],
                "test_expectations": {check_id: {
                    "mode": "diode", "measurement": measurement, "source": {"reference": 4, "section": 2},
                    "probes": {"red": "F6", "black": "A6", "verified": True}}}}
        rows = continuity_checks(plan["wires"], {}, plan["polarised"], board=plan["board"],
                                 test_expectations=plan["test_expectations"])
        original = deepcopy(rows)
        with patch.object(draw_build, "_hole", wraps=draw_build._hole) as hole:
            with patch.object(draw_build, "_wire", wraps=draw_build._wire) as wire:
                text = self.capture(draw_build.draw_tests, plan, rows, "unused.png",
                                    check_probe_bounds=True)
        self.assertEqual([(call.args[2], call.args[3]) for call in hole.call_args_list], [
            ("A1", "#d9e1ea"), ("F1", "#d9e1ea"), ("A6", "#111111"), ("F6", "#d62728")])
        self.assertEqual({call.args[4] for call in wire.call_args_list}, {"#d9e1ea"})
        self.assertIn("Red lead", text)
        self.assertIn("Black lead", text)
        self.assertIn(criterion, " ".join(text.split()))
        self.assertIn("Plan source 4, section 2", " ".join(text.split()))
        table = run_plan(plan)
        self.assertIn(criterion, table)
        self.assertIn("Plan source 4, section 2", table)
        self.assertIn("red lead: F6, black lead: A6", table)
        self.assertEqual(rows, original)

        conflicting = deepcopy(rows)
        conflicting[1]["_probes"] = {"red": "A6", "black": "F6"}
        without_map = deepcopy(rows)
        del without_map[1]["_probes"]
        changed_criterion = deepcopy(rows)
        changed_criterion[1]["expect"] = "Different criterion"
        without_plan_map = dict(plan, test_expectations={})
        changed_plan = deepcopy(plan)
        changed_plan["test_expectations"][check_id]["measurement"]["below"] = -0.25
        changed_source = deepcopy(plan)
        changed_source["test_expectations"][check_id]["source"]["section"] = 3
        for supplied_plan, supplied_rows in [(plan, conflicting), (plan, without_map),
                                             (plan, changed_criterion), (without_plan_map, rows),
                                             (changed_plan, rows), (changed_source, rows)]:
            with self.subTest(rows=supplied_rows), self.assertRaisesRegex(ValueError, check_id):
                self.capture(draw_build.draw_tests, supplied_plan, supplied_rows, "unused.png")
        with self.assertRaisesRegex(ValueError, "board geometry conflicts"):
            self.capture(draw_build.draw_tests, plan, rows, "unused.png", board="electrocookie_half")

    def test_custom_geometry_draws_without_preset_columns_or_rails(self):
        geometry = {"size_mm": [12, 12], "rows": 2, "row0": 2, "pitch": 3,
                    "columns": {"B": 3, "C": 6}, "strips": [("B", "C")], "rails": {}}
        module = {"name": "Verified module", "kind": "module", "holes": [],
                  "covers": {"rows": [1, 2], "cols": ["B", "C"]}}
        plan = {"board": geometry, "parts": [module], "wires": [], "rails": {}}
        self.assertEqual(board_tools.hole_xy("B2", geometry), (3, 5))
        self.assertTrue(board_tools.same_node("B1", "C1", geometry))
        self.assertFalse(board_tools.same_node("B1", "C2", geometry))
        self.assertTrue(board_tools.hole_under_module("B2", module["covers"], geometry))
        self.assertIn("Verified module", self.capture(draw_build.draw_steps, plan, "unused.png"))

    def test_accepted_labels_ranges_and_covers_reach_the_figures(self):
        board = "permaproto_half"
        module = {"name": "Plug-in board", "kind": "module", "holes": []}
        diode = {"name": "Part D1", "kind": "polarised", "holes": ["A1 silk label", "F1 keyed edge"],
                 "marked_hole": "f01", "polarity_mark": "Band mark"}
        self.assertEqual(board_tools.expand_holes("a01-a03"), ["A1", "A2", "A3"])
        covers = ({"rows": ["01", 2], "cols": ["L1", "F"], "margin_mm": 0},
                  {"holes": ["L1@1", "F2"], "margin_mm": 0})
        for cover in covers:
            with self.subTest(cover=cover):
                self.assertTrue(board_tools.hole_under_module("A1", cover, board))
                plan = {"board": board, "parts": [diode, {**module, "covers": cover}],
                        "wires": [], "rails": {"l1": "SUPPLY"}}
                self.assertIn("A1 silk label, F1 keyed edge", run_plan(plan))
                front = self.capture(draw_build.draw_steps, plan, "unused.png")
                self.assertIn("Band mark", front)
                self.assertIn("Plug-in board", front)
                back = self.capture(draw_build.draw_back, plan, "unused.png")
                self.assertIn("SUPPLY", back)

    def test_header_method_displays_only_supplied_spacing(self):
        text = self.capture(draw_build.draw_header_jig, "unused.png")
        self.assertIn("Use the measured spacing from the verified plan.", text)
        self.assertIn("measured plan spacing", text)
        self.assertIn("not to scale", text)
        self.assertNotIn("Plan-reported pitch:", text)
        self.assertNotRegex(text, r"\d+(?:\.\d+)? mm")

        geometry = {"size_mm": [28, 17], "rows": 2, "row0": 3, "pitch": 4,
                    "columns": {"B": 3, "D": 11, "G": 22}, "strips": [], "rails": {}}
        samples = [(("B", "D"), 8.0), (("D", "G"), 11.0)]
        for columns, expected in samples:
            with self.subTest(columns=columns):
                spacing = board_tools.row_spacing_from_columns(*columns, board=geometry)
                self.assertEqual(spacing, expected)
                self.assertEqual(board_tools.columns_for_spacing(spacing, board=geometry), [columns])
                text = self.capture(draw_build.draw_header_jig, "unused.png", pitch_mm=spacing)
                self.assertIn(f"Plan-reported pitch: {expected:.2f} mm; schematic only.", text)
                self.assertIn(f"{expected:.2f} mm (plan)", text)
        for value in [str(samples[0][1]), 0, True, float("nan")]:
            with self.subTest(value=value), self.assertRaises(ValueError):
                draw_build.draw_header_jig("unused.png", pitch_mm=value)

    def test_header_jig_preflight_rejects_bad_config_before_any_writer(self):
        plan = {"board": "permaproto_half", "wires": [], "rails": {}, "parts": []}
        cases = [
            (None, "header_jig must be a mapping"),
            ([], "header_jig must be a mapping"),
            ("2.54 mm", "header_jig must be a mapping"),
            ({"out_png": "unexpected.png"}, "Unknown header_jig fields"),
            ({"pitch_mm": 0}, "Header pitch must be a positive finite measurement"),
            ({"pitch_mm": "2.54"}, "Header pitch must be a positive finite measurement"),
            ({"pitch_mm": True}, "Header pitch must be a positive finite measurement"),
            ({"pitch_mm": -1}, "Header pitch must be a positive finite measurement"),
            ({"pitch_mm": float("inf")}, "Header pitch must be a positive finite measurement"),
            ({"pitch_mm": 10**309}, "Header pitch must be a positive finite measurement"),
            ({"module": ["Module"]}, "header_jig.module must be a string"),
            ({"orientation_note": 1}, "header_jig.orientation_note must be a string or null"),
        ]
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            fresh = root / "fresh"
            existing = root / "existing"
            existing.mkdir()
            unrelated = existing / "note.txt"
            unrelated.write_bytes(b"keep")
            with patch.object(draw_build, "draw_steps") as first_writer:
                for config, error in cases:
                    for out in (fresh, existing):
                        with self.subTest(config=config, destination=out.name):
                            with self.assertRaisesRegex(ValueError, error):
                                draw_build.draw_all({**plan, "header_jig": config}, out)
                first_writer.assert_not_called()
            self.assertFalse(fresh.exists())
            self.assertEqual(list(existing.iterdir()), [unrelated])
            self.assertEqual(unrelated.read_bytes(), b"keep")

    def test_draw_cli_retries_header_jig_plan_after_preflight_failure(self):
        plan = {"board": "permaproto_half", "wires": [], "rails": {}, "parts": [],
                "header_jig": {"pitch_mm": 0}}
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            source = root / "plan.json"
            output = root / "figures"
            source.write_text(json.dumps(plan))
            command = [sys.executable, "-B", draw_build.__file__, str(source), str(output)]
            rejected = subprocess.run(command, capture_output=True, text=True)
            self.assertNotEqual(rejected.returncode, 0)
            self.assertIn("Header pitch must be a positive finite measurement", rejected.stderr)
            self.assertFalse(output.exists())

            settings = {"pitch_mm": 8.0, "module": "Selected module",
                        "orientation_note": "Match the verified mating mark."}
            source.write_text(json.dumps({**plan, "header_jig": settings}))
            accepted = subprocess.run(command, capture_output=True, text=True)
            self.assertEqual(accepted.returncode, 0, accepted.stderr)
            expected = ["board_steps.png", "board_back.png", "board_tests.png",
                        "joint_guide.png", "header_jig.png"]
            self.assertEqual([Path(line).name for line in accepted.stdout.splitlines()], expected)
            snapshot = {path.name: path.read_bytes() for path in output.iterdir()}
            self.assertEqual(set(snapshot), set(expected))
            self.assertTrue(all(data.startswith(b"\x89PNG") for data in snapshot.values()))

            occupied = subprocess.run(command, capture_output=True, text=True)
            self.assertNotEqual(occupied.returncode, 0)
            self.assertIn("Use a fresh output destination", occupied.stderr)
            self.assertEqual({path.name: path.read_bytes() for path in output.iterdir()}, snapshot)

    def test_direct_header_jig_validates_labels_and_preserves_supplied_text(self):
        with tempfile.TemporaryDirectory() as temp:
            output = Path(temp) / "header.png"
            with self.assertRaisesRegex(ValueError, "header_jig.module must be a string"):
                draw_build.draw_header_jig(output, module=None)
            with self.assertRaisesRegex(ValueError, "header_jig.orientation_note must be a string or null"):
                draw_build.draw_header_jig(output, orientation_note=0)
            self.assertFalse(output.exists())

        text = self.capture(draw_build.draw_header_jig, "unused.png", pitch_mm=8.0,
                            module="Selected module", orientation_note="Match the verified mating mark.")
        self.assertIn("Selected module", text)
        self.assertIn("Match the verified mating mark.", text)
        self.assertIn("8.00 mm (plan)", text)
        self.assertIn("not to scale", text)

    def test_cli_renders_mathlike_plan_labels_as_literal_text(self):
        label = r"$\UnknownPin$"
        criterion = r"$\UnknownCriterion$"
        plan = {"board": "permaproto_half", "wires": [], "parts": [],
                "rails": {"L1": label, "R1": "RETURN"},
                "header_jig": {"module": label},
                "test_expectations": {"rail:L1:R1": {"mode": "resistance", "expect": criterion,
                                                      "basis": "Verified plan reference"}}}
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            source = root / "plan.json"
            source.write_text(json.dumps(plan))
            out = root / "figures"
            result = subprocess.run([sys.executable, "-B", draw_build.__file__, str(source), str(out)],
                                    capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            expected = ["board_steps.png", "board_back.png", "board_tests.png",
                        "joint_guide.png", "header_jig.png"]
            self.assertEqual(result.stdout.splitlines(), [str(out / name) for name in expected])
            self.assertEqual({p.name for p in out.iterdir()}, set(expected))
            self.assertTrue(all((out / name).read_bytes().startswith(b"\x89PNG") for name in expected))

    def test_direct_renderers_preserve_literal_text_and_restore_caller_settings(self):
        import matplotlib

        label = r"$\UnknownPin$"
        criterion = r"$\UnknownCriterion$"
        plan = {"board": "permaproto_half", "wires": [], "parts": [], "title": label,
                "rails": {"L1": label, "R1": "RETURN"}}
        expectation = {"rail:L1:R1": {"mode": "resistance", "expect": criterion,
                                      "basis": "Verified plan reference"}}
        checks = continuity_checks([], plan["rails"], board=plan["board"],
                                   test_expectations=expectation)
        cases = [
            (draw_build.draw_steps, (plan, "unused.png"), {}, label),
            (draw_build.draw_back, (plan, "unused.png"), {}, label),
            (draw_build.draw_tests, (plan, checks, "unused.png"), {}, criterion),
            (draw_build.draw_header_jig, ("unused.png",),
             {"module": label, "orientation_note": criterion}, label),
            (draw_build.draw_polarity_guide, ("unused.png",),
             {"board": plan["board"], "anode_hole": "A1", "cathode_hole": "F1",
              "diode": label, "vf": criterion}, criterion),
        ]
        with matplotlib.rc_context({"text.parse_math": True, "text.usetex": True}):
            for render, args, kwargs, expected in cases:
                with self.subTest(renderer=render.__name__):
                    self.assertIn(expected, self.capture(render, *args, **kwargs))
                    self.assertTrue(matplotlib.rcParams["text.parse_math"])
                    self.assertTrue(matplotlib.rcParams["text.usetex"])

    def test_late_render_failure_never_writes_to_destination(self):
        plan = {"board": "permaproto_half", "wires": [], "rails": {}, "parts": [],
                "polarised": [{"name": "D1", "kind": "diode", "holes": ["A1", "F1"],
                               "anode_hole": "A1", "cathode_hole": "F1"}]}
        staged = []

        def fail_after_five_figures(path, **_details):
            scratch = Path(path).parent
            staged.append(scratch)
            self.assertEqual({p.name for p in scratch.iterdir()},
                             {"board_steps.png", "board_back.png", "board_tests.png",
                              "joint_guide.png", "header_jig.png"})
            Path(path).write_bytes(b"incomplete staged image")
            raise RuntimeError("forced last-render failure")

        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            fresh = root / "new" / "figures"
            existing = root / "existing"
            existing.mkdir()
            sentinel = existing / "unrelated.txt"
            sentinel.write_bytes(b"keep me")
            with self.stub_batch_figures(), \
                 patch.object(draw_build, "draw_polarity_guide", side_effect=fail_after_five_figures):
                for out in (fresh, existing):
                    with self.subTest(destination=out):
                        with self.assertRaisesRegex(RuntimeError, "forced last-render failure"):
                            draw_build.draw_all(plan, out)
            self.assertFalse(fresh.parent.exists())
            self.assertEqual(list(existing.iterdir()), [sentinel])
            self.assertEqual(sentinel.read_bytes(), b"keep me")
            self.assertEqual(len(staged), 2)
            self.assertTrue(all(not scratch.exists() for scratch in staged))

    def test_target_added_during_rendering_is_preserved(self):
        plan = {"board": "permaproto_half", "wires": [], "rails": {}, "parts": []}
        with tempfile.TemporaryDirectory() as temp:
            out = Path(temp)
            added = out / "polarity_guide.png"

            def add_reserved_target(path, **_settings):
                Path(path).write_bytes(b"completed staged image")
                added.write_bytes(b"preserve this image")
                return path

            with self.stub_batch_figures(), \
                 patch.object(draw_build, "draw_header_jig", side_effect=add_reserved_target):
                with self.assertRaisesRegex(FileExistsError, "fresh output destination"):
                    draw_build.draw_all(plan, out)
            self.assertEqual(list(out.iterdir()), [added])
            self.assertEqual(added.read_bytes(), b"preserve this image")

    def test_filename_prefix_cannot_escape_the_output_directory(self):
        with tempfile.TemporaryDirectory() as temp:
            output = Path(temp) / "not_created"
            for prefix in ["../escape", "/absolute", "a/b", "a\\b", "", "."]:
                with self.subTest(prefix=prefix), self.assertRaises(ValueError):
                    draw_build.draw_all({}, output, prefix)
                self.assertFalse(output.exists())

    def test_plan_geometry_is_required_before_output_is_created(self):
        with tempfile.TemporaryDirectory() as temp:
            output = Path(temp) / "not_created"
            with self.assertRaisesRegex(ValueError, "verified board geometry"):
                draw_build.draw_all({}, output)
            self.assertFalse(output.exists())
        with self.assertRaisesRegex(ValueError, "verified board geometry"):
            run_plan({})

    def test_diode_without_terminal_mapping_reports_unresolved_and_skips_guide(self):
        plan = {"board": "permaproto_half", "wires": [], "rails": {},
                "parts": [{"name": "D1", "kind": "polarised", "holes": ["A1", "F1"],
                           "marked_hole": "F1", "polarity_mark": "Unverified package mark"}],
                "polarised": [{"name": "D1", "kind": "diode", "holes": ["A1", "F1"]}],
                "test_expectations": {"polarised:D1": {"mode": "diode", "expect": "Legacy criterion",
                                                        "basis": "Verified plan reference"}}}
        report = run_plan(plan)
        self.assertIn("UNRESOLVED diode placement for D1", report)
        self.assertIn("Legacy criterion", report)
        front = self.capture(draw_build.draw_steps, plan, "unused.png")
        self.assertIn("Orientation unresolved", front)
        self.assertNotIn("Unverified package mark", front)
        with tempfile.TemporaryDirectory() as temp:
            with self.stub_batch_figures(), \
                 patch.object(draw_build, "draw_polarity_guide") as guide:
                with self.assertWarnsRegex(UserWarning, "UNRESOLVED diode placement for D1"):
                    paths = draw_build.draw_all(plan, temp)
                self.assertEqual([Path(path).name for path in paths],
                                 ["board_steps.png", "board_back.png", "board_tests.png",
                                  "joint_guide.png", "header_jig.png"])
                guide.assert_not_called()
            with self.assertRaisesRegex(ValueError, "UNRESOLVED diode placement"):
                draw_build.draw_polarity_guide(Path(temp) / "unused.png", board=plan["board"])
            self.assertFalse((Path(temp) / "unused.png").exists())

    def test_diode_contradictions_fail_before_reports_or_drawing_output(self):
        diode = {"name": "D1", "kind": "diode", "holes": ["A1", "F1"],
                 "anode_hole": "A1", "cathode_hole": "F1"}
        part = {"name": "D1", "kind": "polarised", "holes": ["A1 keyed", "F1"]}
        base = {"board": "permaproto_half", "wires": [], "rails": {}, "parts": [part],
                "polarised": [diode]}
        cases = [
            ({"polarised": [{**diode, "cathode_hole": "A01"}]}, "two distinct physical holes"),
            ({"polarised": [{**diode, "anode_hole": "A2", "cathode_hole": "F2"}]},
             "terminal mapping conflicts with declared holes"),
            ({"polarised": [{**diode, "anode": "A2"}]}, "conflicting anode hole aliases"),
            ({"parts": [{**part, "holes": ["A2", "F2"]}]}, "conflicting or non-distinct declared holes"),
            ({"parts": [{**part, "marked_hole": "A1", "marked_terminal": "cathode"}]},
             "marked hole conflicts with the declared terminal"),
            ({"parts": [part, part]}, "ambiguous matching plan entries"),
            ({"polarised": [{"name": "D1", "kind": "diode", "holes": ["A1", "F1"],
                             "anode_hole": "A1", "marked_hole": "A01",
                             "marked_terminal": "cathode"}]},
             "two distinct physical holes"),
            ({"polarised": [{"name": "D1", "kind": "diode", "holes": ["A1", "F1"],
                             "anode_hole": "A1", "marked_hole": "F2",
                             "marked_terminal": "cathode"}]},
             "terminal mapping conflicts with declared holes"),
        ]
        with tempfile.TemporaryDirectory() as temp:
            output = Path(temp) / "uncreated"
            for change, message in cases:
                with self.subTest(change=change):
                    plan = {**base, **change}
                    with self.assertRaisesRegex(ValueError, message):
                        run_plan(plan)
                    with self.assertRaisesRegex(ValueError, message):
                        draw_build.draw_all(plan, output)
                    with self.assertRaisesRegex(ValueError, message):
                        draw_build.draw_steps(plan, output / "front.png")
                    with self.assertRaisesRegex(ValueError, message):
                        draw_build.draw_back(plan, output / "rear.png")
                    self.assertFalse(output.exists())
            guide = Path(temp) / "guide.png"
            with self.assertRaisesRegex(ValueError, "two distinct physical holes"):
                draw_build.draw_polarity_guide(guide, anode_hole="A1", cathode_hole="A01",
                                               board=base["board"])
            self.assertFalse(guide.exists())

    def test_consistent_mark_does_not_supply_a_missing_terminal_location(self):
        plan = {"board": "permaproto_half", "wires": [], "rails": {}, "parts": [],
                "polarised": [{"name": "D1", "kind": "diode", "holes": ["A1", "F1"],
                               "anode_hole": "A1", "marked_hole": "F1",
                               "marked_terminal": "cathode"}]}
        self.assertIn("UNRESOLVED diode placement for D1", run_plan(plan))
        with tempfile.TemporaryDirectory() as temp:
            with self.stub_batch_figures(), \
                 patch.object(draw_build, "draw_polarity_guide") as guide:
                with self.assertWarnsRegex(UserWarning, "UNRESOLVED diode placement for D1"):
                    paths = draw_build.draw_all(plan, temp)
                self.assertEqual([Path(path).name for path in paths],
                                 ["board_steps.png", "board_back.png", "board_tests.png",
                                  "joint_guide.png", "header_jig.png"])
                guide.assert_not_called()

    def test_explicit_diode_mapping_preserves_roles_without_assuming_package_marks(self):
        diode = {"name": "D1", "kind": "diode", "holes": ["F1", "A1"],
                 "anode_hole": "A1", "anode": "a01", "cathode": "F1"}
        part = {"name": "D1", "kind": "polarised", "holes": ["A1 keyed", "F1"],
                "marked_hole": "f01", "marked_terminal": "cathode",
                "polarity_mark": "Arbitrary package legend"}
        plan = {"board": "permaproto_half", "wires": [], "rails": {}, "parts": [part],
                "polarised": [diode]}
        self.assertNotIn("UNRESOLVED diode placement", run_plan(plan))
        front = self.capture(draw_build.draw_steps, plan, "unused.png")
        self.assertIn("Cathode mark", front)
        self.assertNotIn("Arbitrary package legend", front)
        with tempfile.TemporaryDirectory() as temp:
            with self.stub_batch_figures():
                paths = draw_build.draw_all(plan, temp)
            guide = Path(temp) / "polarity_guide.png"
            self.assertIn(str(guide), paths)
            self.assertTrue(guide.is_file())
        text = self.capture(draw_build.draw_polarity_guide, "unused.png", cathode_hole="F1",
                            anode_hole="A1", diode="D1", board=plan["board"])
        self.assertIn("ANODE end\nVerified hole: A1", text)
        self.assertIn("CATHODE end\nVerified hole: F1", text)
        self.assertNotIn("silver", text.casefold())
        self.assertNotIn("no band", text.casefold())

    def test_draw_all_rejects_existing_figures_and_uses_a_fresh_unresolved_destination(self):
        verified = {"board": "permaproto_half", "wires": [], "rails": {}, "parts": [],
                    "polarised": [{"name": "D1", "kind": "diode", "holes": ["A1", "F1"],
                                   "anode_hole": "A1", "cathode_hole": "F1"}]}
        unresolved = {**verified, "polarised": [{"name": "D1", "kind": "diode",
                                                  "holes": ["A1", "F1"]}]}
        with tempfile.TemporaryDirectory() as temp:
            first = Path(temp) / "verified"
            prior = draw_build.draw_all(verified, first, "revision")
            self.assertEqual([Path(path).name for path in prior],
                             ["revision_steps.png", "revision_back.png", "revision_tests.png",
                              "joint_guide.png", "header_jig.png", "polarity_guide.png"])
            unrelated = first / "existing note.md"
            unrelated.write_text("Keep my note", encoding="utf-8")
            snapshot = {path.name: path.read_bytes() for path in first.iterdir()}
            with self.assertRaisesRegex(FileExistsError, "fresh output destination.*polarity_guide.png"):
                draw_build.draw_all(unresolved, first, "revision")
            self.assertEqual({path.name: path.read_bytes() for path in first.iterdir()}, snapshot)

            second = Path(temp) / "unresolved"
            second.mkdir()
            (second / "existing note.md").write_bytes(unrelated.read_bytes())
            with self.assertWarnsRegex(UserWarning, "UNRESOLVED diode placement for D1"):
                fresh = draw_build.draw_all(unresolved, second, "revision")
            self.assertEqual([Path(path).name for path in fresh],
                             [Path(path).name for path in prior[:-1]])
            self.assertEqual({path.name for path in second.iterdir()},
                             {Path(path).name for path in fresh} | {"existing note.md"})
            self.assertEqual((second / "existing note.md").read_bytes(), snapshot[unrelated.name])

    def test_draw_all_checks_all_target_names_before_calling_writers(self):
        plan = {"board": "permaproto_half", "wires": [], "rails": {}, "parts": []}
        names = ("revision_steps.png", "revision_back.png", "revision_tests.png",
                 "joint_guide.png", "header_jig.png", "polarity_guide.png")
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            for i, name in enumerate(names):
                with self.subTest(target=name):
                    output = root / str(i)
                    output.mkdir()
                    occupant = output / name
                    if name == "polarity_guide.png":
                        occupant.symlink_to("absent")
                    elif name == "header_jig.png":
                        occupant.mkdir()
                    else:
                        occupant.write_bytes(b"previous figure")
                    with patch.object(draw_build, "draw_steps") as first_writer:
                        with self.assertRaises(FileExistsError) as error:
                            draw_build.draw_all(plan, output, "revision")
                        self.assertIn(name, str(error.exception))
                        first_writer.assert_not_called()
                    self.assertEqual(list(output.iterdir()), [occupant])
                    if name == "polarity_guide.png":
                        self.assertTrue(occupant.is_symlink())
                        self.assertEqual(occupant.readlink(), Path("absent"))
                    elif name == "header_jig.png":
                        self.assertTrue(occupant.is_dir())
                    else:
                        self.assertEqual(occupant.read_bytes(), b"previous figure")

    def test_non_diode_part_does_not_generate_a_diode_guide(self):
        plan = {"board": "permaproto_half", "wires": [], "rails": {}, "parts": [],
                "polarised": [{"name": "C1", "kind": "capacitor", "holes": ["A1", "F1"]}]}
        with tempfile.TemporaryDirectory() as temp:
            with self.stub_batch_figures(), \
                 patch.object(draw_build, "draw_polarity_guide") as polarity:
                draw_build.draw_all(plan, temp, "valid_stem-1")
                polarity.assert_not_called()


if __name__ == "__main__":
    unittest.main()
