---
name: matlab
description: >-
  Implements and verifies one already approved numerical operation through an
  available, licensed, version-verified MATLAB runtime and exact toolbox set.
  Use when the request names this skill or a verified Active method or execution
  skill routes an exact function, script, input, numerical tolerance, seed, and
  output specification. It audits release, license, path, shadowing, startup
  state, toolboxes, data types, dimensions, numerical conditioning, randomness,
  parallel or GPU use, tests, batch invocation, and writes. It does not choose
  the scientific method, install or update MATLAB, obtain licenses, add
  toolboxes, substitute Octave, change paths persistently, run unapproved code,
  or interpret results. Triggers: run this in MATLAB, MATLAB numerical
  operation.
metadata:
  level: skill
  system: Research Assistant System
  part: "4"
  family: computing
  modality: any
  dependencies: ""
  requires: licensed MATLAB and the needed toolboxes
  gates: running on real data
  created: "2026-07-23"
  updated: "2026-10-29"
---

# MATLAB

Implement and verify one approved MATLAB computation in an already available
licensed environment.

## Purpose

`matlab` owns:

- release, license, path, toolbox, and API preflight for one computation;
- implementation of one approved MATLAB function or script;
- dimension, datatype, numerical, seed, and side-effect checks;
- bounded fixture tests and one approved batch execution;
- controlled artifact export;
- a MATLAB Execution Record.

The user owns the scientific method, equations, algorithm, parameters, data
inclusion, tolerances, toolbox choice, compute, output, interpretation, and
claims.

[statistical-analysis](../../skills/statistical-analysis/SKILL.md) owns general statistical execution and verification.

Use this skill when the user names it, the bounded request matches its
frontmatter description and trigger meaning, or a verified matching coordinator,
companion, or capability handoff selects it.

Do not trigger from `matrix`, `signal`, `image`, `ODE`, `optimization`,
`statistics`, `plot`, `.m file`, or `Octave` alone.

Do not use this skill to choose a method, install or update MATLAB, obtain or
renew a license, add a toolbox, substitute GNU Octave, modify startup files or
the persistent path, enable parallel or GPU execution, or write outputs
without approval.

## Inputs

Obtain or mark missing:

- approved computation and mathematical or procedural specification;
- exact source data or fixture, variables, shapes, types, units, and
  missing-value behavior;
- selected MATLAB function, script, class, Live Script, or project boundary;
- required MATLAB release and exact toolbox functions;
- parameters, solvers, tolerances, stopping rules, seeds, and numerical
  invariants;
- expected warnings, errors, diagnostics, tests, and reference outputs;
- current folder, project, MATLAB path, `startup.m`, `pathdef.m`, environment,
  and shadowing policy;
- parallel pool, thread, process, cluster, GPU, external library, Java,
  Python, MEX, or system-command boundary;
- input reads, network activity, temporary files, side effects, exports,
  overwrite, and destination;
- installed release, update, architecture, license state, toolbox versions,
  and compute limits.

If the computation, input shape, toolbox, path state, numerical criterion,
license, side effect, or output boundary is unresolved, stop with **MATLAB
execution specification incomplete**.

## Steps

### 1. Preflight the exact runtime

Record:

- MATLAB release, update, architecture, Java state, and executable path;
- base MATLAB and required toolbox versions and license tests;
- current folder, project, `path`, `which -all` results for selected
  functions, startup files, and environment variables;
- solver and function signatures, defaults, release changes, randomness, and
  deprecations;
- parallel, GPU, external-language, MEX, and system-command state.

MATLAB `R2026a` was current on 2026-07-23. Verify the participant's actual MATLAB release, shell path and applicable license. A dated release review is not a participant runtime or license guarantee. Every use rechecks the exact release, license, path, and
toolboxes.

### 2. Gate 1: approve the MATLAB Execution Contract

Show:

- computation, variables, shapes, types, units, and numerical invariants;
- exact functions, parameters, solver options, tolerances, and seeds;
- release, license, toolbox, path, startup, and shadowing state;
- fixture tests, expected outputs, warnings, and failure criteria;
- parallel, GPU, external-language, MEX, system-command, and network boundary;
- planned reads, temporary files, writes, compute, and cleanup.

Gate 1 authorizes only static code review and a bounded synthetic or approved
fixture test with no external side effects. It does not authorize observed
data, a full run, toolbox or path changes, parallel pools, clusters, GPU,
external commands, network access, writes, overwrites, or installation.

### 3. MATLAB forms for the approved calculation

Where applicable, compare only valid user-supplied forms such as:

- one explicit vectorized or matrix operation;
- one approved loop or chunked implementation;
- one approved built-in solver or function route.

For each show mathematical equivalence, numerical stability, memory, toolbox
and release requirements, side effects, testability, visible output, benefit,
tradeoff, and limitation. Do not choose a method because MATLAB provides it.

### 4. Build and test the bounded function

Before creating a new MATLAB source file, read and adapt the vault-root `00 ASTORIA/templates/code_template.md` to MATLAB comments and the selected script/function structure.

Prefer an explicit function with declared inputs and outputs over a
base-workspace script. Verify:

| Check | Approved invariant | Fixture result | Status |
|---|---|---|---|
| Input shapes, types, and units | | | |
| Output shapes and types | | | |
| Known reference case | | | |
| Edge, missing, and nonfinite values | | | |
| Numerical tolerance and conditioning | | | |
| Random stream and seed | | | |
| Warnings, errors, and side effects | | | |

Use MATLAB unit tests or exact assertions appropriate to the bounded
computation. Preserve failures rather than suppressing warnings or changing
parameters automatically.

### 5. Review the script, path, and exact execution

Show:

- complete function or script and exact input bindings;
- release, toolbox, path, shadowing, project, and startup provenance;
- solver, algorithm, options, tolerances, datatypes, dimensions, and seeds;
- vectorization, broadcasting, transposition, indexing, sparse, complex, and
  table behavior where relevant;
- numerical conditioning, reference values, warnings, and failure criteria;
- batch command, working folder, environment, timeout, compute, side effects,
  and output writes.

Matrix multiplication and element-wise multiplication are distinct. A
successful function call does not establish numerical stability, scientific
validity, or agreement with another MATLAB release.

### 6. Gate 2: approve one bounded operation

Ask the user to approve the exact:

- code, input, release, toolboxes, path state, parameters, tolerances, seeds,
  command, resources, and failure behavior;
- one fixture test, observed-data run, or export operation;
- destination, overwrite, temporary-file, and cleanup plan.

Reopen Gate 2 before changing code, inputs, parameters, solver, tolerance,
seed, release, toolbox, path, startup state, parallelism, GPU, external
language, command, output, or destination.

### 7. Run and verify the approved MATLAB command

Run only the approved command. Capture:

- source, code, input, environment, and version hashes;
- release, update, license result, toolboxes, path, `which -all`, and startup
  state;
- exact command, working folder, parameters, tolerances, seeds, and resources;
- test results, numerical checks, warnings, errors, exit status, and duration;
- output shapes, dtypes, counts, reference reconciliation, and checksums;
- writes, overwrite state, temporary artifacts, cleanup, and deviations.

Return:

```text
MATLAB Execution Record
Approved computation:
Release, update, architecture, and license:
Toolboxes, path, startup, and shadowing:
Inputs, shapes, types, units, and hashes:
Code, functions, parameters, and solver:
Tolerances, seeds, and resources:
Fixture and unit-test results:
Approved execution and exit status:
Neutral numerical outputs:
Warnings, errors, and deviations:
Output verification and side effects:
Specification-conformance check:
What execution does not establish:
Artifacts and hashes:
user-owned interpretation and claims:
```

## Boundaries

- Never install, update, license, activate, or add a MATLAB product.
- Never substitute Octave or claim MATLAB compatibility without an approved,
  version-specific equivalence test.
- Never persistently alter the MATLAB path, `startup.m`, `pathdef.m`, project,
  preferences, or environment.
- Check function shadowing and exact toolbox ownership before execution.
- Never infer a solver, tolerance, seed, datatype, transpose, missing-value
  rule, or output format.
- Do not start a parallel pool, cluster job, GPU operation, external-language
  bridge, MEX build, network call, or system command without separate
  authority.
- Stop on unavailable or expiring license that cannot cover the run,
  unavailable toolbox, release mismatch, shadowed function, failed fixture,
  ill-conditioning beyond tolerance, dimension mismatch, nonfinite
  propagation, unapproved side effect, or output collision.

## MATLAB calculation and runtime checks

Use the records that apply to the approved operation. Follow its existing approval, stop, and verification requirements.

- **Labeled implementation cards.** Compare only user-approved MATLAB implementation forms for the same computation. This exposes numerical and toolbox consequences without method selection. This requires an approved mathematical operation. Unproposed implementations remain outside scope.
- **MATLAB Execution Decision Record.** Show release, license, path, toolbox, code, tolerances, seed, side effects, and fixture tests. This makes environment and numerical drift visible. This requires detailed runtime inspection. Proprietary runtime behavior can still vary by platform.
- **MATLAB Execution Record.** Execute one approved batch command and reconcile declared invariants. This preserves code, runtime, and output control. This adds a gate before execution. Verification covers only declared invariants.

Use an additional check below only when it addresses a specific uncertainty and its scope and approvals are in place.

- **Extended numerical-validity matrix.** Add cross-release or independent reference comparisons when already available. This detects selected release and implementation drift. This requires another approved runtime or reference. Agreement does not establish scientific validity.
- **Numerical sensitivity grid.** Add a prespecified solver, precision, or chunking sensitivity. This tests selected implementation dependence. This adds compute and review. This cannot resolve a wrong scientific model.
- **Verified MATLAB computation bundle.** Execute prespecified cross-release or precision tests before the full run. This documents selected numerical robustness. This adds licenses, compute, and maintenance. Robustness does not validate interpretation.

## Checks

- **Positive:** an approved linear-algebra function produces version, toolbox,
  path, dimension, conditioning, fixture, and output records.
- **Negative:** `analyze this in MATLAB` does not select an analysis or run.
- **Toolbox:** an unavailable licensed function stops before execution.
- **Shadowing:** a project function that masks a selected built-in is reported
  through `which -all`.
- **Octave:** an unavailable MATLAB runtime is not silently replaced with
  Octave.
- **Handoff:** statistical method choice and neutral result verification return
  to [statistical-analysis](../../skills/statistical-analysis/SKILL.md).

## References

- Adapted from: K-Dense Inc. (2026). *scientific-agent-skills* [Computer software]. GitHub. https://github.com/K-Dense-AI/scientific-agent-skills (MIT License)
- MathWorks. (n.d.). *MATLAB release notes*. https://www.mathworks.com/help/matlab/release-notes.html
- MathWorks. (n.d.). *MATLAB testing workflows*. https://www.mathworks.com/help/matlab/matlab_prog/run-tests-for-various-workflows.html
- MathWorks. (n.d.). *rng*. https://www.mathworks.com/help/matlab/ref/rng.html
- MathWorks. (n.d.). *version*. https://www.mathworks.com/help/matlab/ref/version.html
