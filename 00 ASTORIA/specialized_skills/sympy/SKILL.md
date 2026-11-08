---
name: sympy
description: >-
  Represents, manipulates, solves, or translates one user-specified symbolic
  problem through an available, version-verified SymPy API. Use when the request
  names this skill or a verified Active method or execution skill routes an
  exact expression, operation, domain, assumption, result-form, and verification
  specification. It preserves exact versus approximate inputs, branches,
  singularities, unresolved conditions, solver completeness, expression
  provenance, numerical bridges, and neutral outputs. It does not choose the
  scientific model, install packages, force assumptions or simplification, trust
  arbitrary strings, execute unapproved lambdify or code generation, claim a
  complete solution when SymPy does not, or interpret results. Triggers: solve
  this symbolically, symbolic math in SymPy.
metadata:
  level: skill
  system: Research Assistant System
  part: "4"
  family: computing
  modality: any
  dependencies: ""
  requires: Python, SymPy
  gates: running on real data
  created: "2026-07-23"
  updated: "2026-10-29"
---

# SymPy

Implement and verify one bounded symbolic computation with explicit domains,
assumptions, and completeness limits.

## Purpose

`sympy` owns:

- version and API preflight for one selected symbolic operation;
- explicit symbol, function, matrix, domain, and assumption construction;
- exact manipulation, solving, differentiation, integration, limits, series,
  or translation as approved;
- branch, singularity, completeness, and exact-to-numeric review;
- independent residual, substitution, equivalence, or bounded numerical
  verification;
- a SymPy Computation Record.

The user owns the scientific model, equations, variables, domains, assumptions,
operation, acceptable result form, numerical bridge, interpretation, and
claims.

[statistical-analysis](../../skills/statistical-analysis/SKILL.md) owns general scientific computation and result
verification.

Use this skill when the user names it, the bounded request matches its
frontmatter description and trigger meaning, or a verified matching coordinator,
companion, or capability handoff selects it.

Do not trigger from `solve`, `simplify`, `integrate`, `differentiate`,
`equation`, `symbolic`, `algebra`, `calculus`, `matrix`, or `LaTeX` alone.

Do not use this skill to formulate a scientific model, invent assumptions,
install SymPy, parse untrusted expressions, select a solver automatically,
force a simplification, call numerical backends, generate or compile code, or
write outputs without approval.

## Inputs

Obtain or mark missing:

- exact expression, equation, inequality, matrix, recurrence, or system;
- expression provenance and whether any string input is trusted;
- intended symbolic operation;
- symbol, function, index, matrix, unit, and dimension definitions;
- domain and assumptions for every consequential object;
- exact versus approximate constants and requested precision;
- branch, singularity, boundary, initial, and completeness requirements;
- selected solver or bounded valid route set;
- acceptable result class and representation;
- residual, substitution, equivalence, domain, or numerical verification plan;
- optional `lambdify`, NumPy, mpmath, SciPy, code-generation, compiler, or
  export boundary;
- installed Python, SymPy, and mpmath versions and resource limit.

If the expression, domain, assumptions, exactness, operation, result class,
trusted-input status, or verification criterion is unresolved, stop with
**Symbolic problem specification incomplete**.

## Steps

### 1. Preflight the exact API

Record:

- Python, SymPy, mpmath, and any separately approved backend versions;
- symbol constructors, expression forms, solver, transformation, printer,
  numerical, and code-generation APIs;
- default domains, output types, automatic evaluation, assumptions,
  deprecations, and resource behavior;
- installed versus documented version mismatch.

SymPy `1.14.0` was current on 2026-07-23. Verify SymPy in the participant's selected interpreter. Absence does not authorize installation. Live execution
stops unless an already available compatible environment is selected.

### 2. Gate 1: approve the Symbolic Problem Contract

Show:

- normalized expression or system and provenance;
- symbol table, domains, assumptions, units, and dimensions;
- exact and approximate constants;
- branch, singularity, initial, boundary, and completeness requirements;
- valid candidate operations or solvers and expected result classes;
- resource cap, verification plan, numerical bridge, and output boundary.

Gate 1 authorizes only explicit symbolic construction and a bounded
structure-only inspection. It does not authorize solving, forced
transformation, numerical evaluation, `lambdify`, code generation,
compilation, external backends, writes, installation, or scientific
interpretation.

### 3. Symbolic forms for the approved operation

Where applicable, compare only valid user-supplied routes such as:

- a targeted algebraic transformation;
- one domain-explicit symbolic solver;
- one approved exact-to-numeric route.

For each show domain coverage, assumptions, output form, branch and singularity
handling, completeness, expression-growth risk, verification, visible output,
benefit, tradeoff, and limitation. Do not create a scientific model or choose
an assumption for convenience.

### 4. Construct the exact symbolic problem

Build objects explicitly rather than through arbitrary string parsing:

| Object | Definition | Domain and assumptions | Exact or approximate | Provenance |
|---|---|---|---|---|
| Symbol or function | | | | |
| Constant or parameter | | | | |
| Expression or equation | | | | |
| Boundary or initial condition | | | | |
| Matrix, unit, or dimension | | | | |

Record automatic evaluation and preserve an unevaluated or source form when it
is needed to audit singularities or transformations.

### 5. Review the exact computation and domain

Show:

- exact SymPy code and object construction;
- selected operation or solver, options, and explicit domain;
- assumptions and every unresolved tri-state query;
- exact-to-approximate conversion point and requested precision;
- branch cuts, excluded points, singularities, conditions, free parameters,
  and solution-set form;
- possible `ConditionSet`, unevaluated result, heuristic simplification, or
  incomplete solver state;
- verification method, resource estimate, and any backend or execution risk.

An assumptions result of `None` is unresolved, not false. Generic
`simplify()` is heuristic, not a proof. A closed form is a mathematical
representation under stated assumptions, not evidence that a scientific model
is true.

### 6. Gate 2: approve one bounded symbolic operation

Ask the user to approve the exact:

- expression, symbols, domains, assumptions, solver or transformation,
  options, resource cap, and verification;
- one manipulation, solve, evaluate, `lambdify`, print, or code-generation
  action;
- backend, trusted-input, output, and destination boundary.

Reopen Gate 2 before changing a domain, assumption, expression, solver,
transformation, precision, branch policy, backend, numerical bridge,
code-generation target, compiler, or output destination.

### 7. Run and verify the approved symbolic operation

Run only the approved operation. Capture:

- expression, code, environment, and version hashes;
- symbol table, domains, assumptions, exactness, and source form;
- solver or transformation, options, warnings, duration, and resource use;
- exact result, result class, branches, conditions, singularities, and
  unresolved objects;
- substitution, residual, equivalence, domain, or high-precision spot checks;
- numerical-backend or generated-code state only when approved;
- deviations and artifacts.

Return:

```text
SymPy Computation Record
Approved symbolic problem:
Versions and APIs:
Expression provenance:
Symbols, domains, assumptions, units, and dimensions:
Exact and approximate boundary:
Operation, solver, and options:
Branches, singularities, and conditions:
Exact result and completeness state:
Verification and numerical spot checks:
Backend or code-generation state, if approved:
Warnings, resource limits, and deviations:
Specification-conformance check:
What the result does not establish:
Artifacts and hashes:
user-owned interpretation and claims:
```

## Boundaries

- Never invent a domain, assumption, boundary condition, initial condition, or
  scientific equation.
- Use exact SymPy numbers when exactness is intended; do not silently preserve
  Python floating-point contamination as exact.
- Pass an explicit domain to domain-sensitive solvers when the problem
  requires it.
- Preserve `ConditionSet`, unevaluated integrals, unresolved assumptions,
  conditional expressions, and incomplete solution states.
- Never use `force=True` or another assumption-forcing transformation without
  explicit approval and verification.
- Do not treat simplification as proof or a solver result as complete unless
  the documented result and checks support that claim.
- `lambdify` uses dynamic code execution. Never pass untrusted input or invoke
  it without an approved backend and trust boundary.
- Do not generate, compile, import, or run code without separate authority.
- Stop on missing domains, untrusted input, inconsistent units, unresolved
  completeness when completeness is required, unverifiable transformation,
  expression swell beyond the cap, missing optional backend, or assumptions
  selected to obtain a desired result.

## Symbolic computation and precision checks

Use the records that apply to the approved operation. Follow its existing approval, stop, and verification requirements.

- **Symbolic Problem Decision Record.** Show expressions, domains, assumptions, branches, completeness, exactness, and verification. This prevents hidden assumptions and false completeness. This requires precise mathematical specification. SymPy may still return unresolved forms.
- **Symbolic route cards.** Compare only user-approved targeted transformation, solver, or exact-to-numeric routes. This exposes domain and completeness differences without model selection. This requires an explicit candidate set. Unproposed routes remain outside scope.
- **SymPy Computation Record.** Execute one approved symbolic operation and record exact result and completeness. This preserves mathematical and provenance control. This adds a gate before computation. Verification covers declared invariants only.

Use an additional check below only when it addresses a specific uncertainty and its scope and approvals are in place.

- **Extended domain-validity matrix.** Add singularity, branch-cut, and adversarial substitution checks. This exposes selected edge cases. This adds mathematical review and compute. This cannot exhaust every domain pathology.
- **Symbolic verification matrix.** Add one prespecified independent symbolic or high-precision verification route. This tests selected algebraic and numerical consistency. This adds computation and branch review. Agreement does not prove model validity.
- **Verified symbolic-computation bundle.** Execute the prespecified independent verification and precision checks. This documents selected robustness. This adds backend or compute requirements. Robust algebra does not establish scientific truth.

## Checks

- **Positive:** an approved real-domain equation produces explicit symbols,
  domain, exact solution set, residual checks, and completeness state.
- **Negative:** `derive the right model for my data` does not generate an
  equation or choose a solver.
- **Domain:** an unspecified real-versus-complex problem stops before solving.
- **Completeness:** `ConditionSet` is preserved rather than called a complete
  solution.
- **Security:** untrusted text cannot flow into `lambdify` or dynamic parsing.
- **Handoff:** general scientific execution and neutral result verification
  may return to [statistical-analysis](../../skills/statistical-analysis/SKILL.md).

## References

- Adapted from: K-Dense Inc. (2026). *scientific-agent-skills* [Computer software]. GitHub. https://github.com/K-Dense-AI/scientific-agent-skills (MIT License)
- SymPy. (n.d.). *Assumptions guide*. https://docs.sympy.org/latest/guides/assumptions.html
- SymPy. (n.d.). *Best practices* (Version 1.14.0). https://docs.sympy.org/latest/explanation/best-practices.html
- SymPy. (n.d.). *lambdify*. https://docs.sympy.org/latest/modules/utilities/lambdify.html
- SymPy. (n.d.). *solveset*. https://docs.sympy.org/latest/modules/solvers/solveset.html
- SymPy. (n.d.). *SymPy* (Version 1.14.0) [Computer software]. GitHub. https://github.com/sympy/sympy/releases/tag/1.14.0
