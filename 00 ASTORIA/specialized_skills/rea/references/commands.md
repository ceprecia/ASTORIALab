# REA commands

Use the runtime manager next to the loaded skill. Set `REA_SKILL_DIR` to the absolute directory containing that `SKILL.md`, `REA_RUNTIME_ROOT` to the installed external runtime directory, and `REA_TARGET` to the exact application tree or ASAR supplied for the task. Use the runtime directory returned by installation, including when a custom location was selected. The examples below use those explicit values.

The installed build supports only:

- `analyze-javascript-application ABSOLUTE_TARGET_PATH --json`
- `inspect-analysis-view INPUT_JSON_OR_FILE --json`
- `--help`
- `--version`

Use `install_update.md` for runtime setup, repair, updates, and installation into another vault. Do not invoke a full vendor setup or update command.

## Analyze and save the complete Evidence

Create a temporary working directory outside the vault and redirect the JSON result into it:

```bash
REA_WORK_DIR="$(mktemp -d "${TMPDIR:-/tmp}/rea_analysis.XXXXXX")"
python3 "$REA_SKILL_DIR/scripts/manage_runtime.py" run --runtime-root "$REA_RUNTIME_ROOT" -- \
  analyze-javascript-application "$REA_TARGET" --json \
  > "$REA_WORK_DIR/evidence.json"
```

Check the command's exit status before using the output. A failed command is not completed Evidence. Preserve its reported error and resolve that specific failure.

## Read a summary

Build the view input from the saved complete Evidence without loading that full record into the conversation:

```bash
python3 - "$REA_WORK_DIR/evidence.json" "$REA_WORK_DIR/view_input.json" <<'PY'
import json
import sys

with open(sys.argv[1], encoding="utf-8") as evidence_file:
    evidence = json.load(evidence_file)

request = {
    "source": {"kind": "inline", "evidence": evidence},
    "view": {"kind": "summary"},
}

with open(sys.argv[2], "w", encoding="utf-8") as request_file:
    json.dump(request, request_file)
PY

python3 "$REA_SKILL_DIR/scripts/manage_runtime.py" run --runtime-root "$REA_RUNTIME_ROOT" -- \
  inspect-analysis-view "$REA_WORK_DIR/view_input.json" --json \
  > "$REA_WORK_DIR/summary.json"
```

Read the summary first. It describes the parent analysis's identity, counts, coverage, limitations, and unknowns. It does not establish runtime behavior.

## Select a small module view

Keep the same `source` object and replace only `view` in the input file. To page module identities:

```json
{"kind":"page","collection":"modules","offset":0,"limit":16}
```

To inspect one module, use a path copied exactly from a returned module page:

```json
{"kind":"item","collection":"modules","selector":{"path":"EXACT_RECORDED_MODULE_PATH"}}
```

When a path is ambiguous or unavailable, copy its exact returned `node_id` instead:

```json
{"kind":"item","collection":"modules","selector":{"node_id":"EXACT_RETURNED_NODE_ID"}}
```

Run `inspect-analysis-view` again against the modified input file and save its result to a distinct external view file. Select additional pages or source ranges only when the feature question needs them. Page exhaustion does not prove absence when the parent coverage is incomplete.

Every view request contains the original complete Evidence in `source.evidence`. Do not substitute a summary, a prior view, or a server-retained Evidence ID. Creating a new view does not require rerunning the application analysis.
