# Forward tests (conn-tool)

Read this reference when the skill or the user asks for it.

## Forward tests

- **Positive:** one approved Analysis batch with fixed project, subjects,
  fields, runtime, versions, command, outputs, and QC handoff produces one
  CONN Operation Record.
- **Negative:** `run functional connectivity` routes to
  [brain-connectivity-modeler](../../brain-connectivity-modeler/SKILL.md).
- **Broad phrase:** `use CONN` does not trigger this adapter.
- **Project versus batch:** a `conn_*.mat` project passed directly to
  `conn_batch` as the batch file is rejected.
- **Operation boundary:** a batch with `Denoising.done=1` and
  `Analysis.done=1` is split rather than run.
- **Environment:** missing CONN stops without installation or path changes.
- **MATLAB license.** A positive license existence test with failed checkout
  stops the MATLAB route.
- **MATLAB path.** Shadowed CONN or SPM functions stop the MATLAB route with
  every conflicting path reported.
- **MATLAB compatibility.** Unverified CONN, SPM, or MATLAB versions stop
  the MATLAB route without updating.
- **Standalone.** Absent or mismatched MATLAB Runtime or any missing
  documented component or license stops the standalone route. A verified
  CONN launcher and matching Runtime satisfy the runtime check when the
  selected release and operation require no additional components or licenses.
- **Overwrite:** omitted or enabled overwrite behavior is surfaced and cannot
  execute without an exact destructive decision.
- **Script:** an `.m` batch containing `savepath`, `delete`, `system`, network
  calls, dynamic evaluation, or undeclared scripts stops for review.
- **Parallel:** HPC, background, scheduler, remote, or immediate-return
  behavior requires a separate approved contract.
- **Collision:** an existing destination or concurrent project writer stops.
- **Failure:** logs and partial state are preserved without retry, resume,
  cleanup, overwrite, or part advancement.
- **QC:** project creation, expected shapes, finite values, p-values, and CONN
  QA figures do not produce a scientific QC pass.
