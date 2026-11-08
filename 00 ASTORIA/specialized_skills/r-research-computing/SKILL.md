---
name: r-research-computing
description: >-
  Implements and verifies one already approved research-computing task in an
  available, version-verified R environment. Use when the request names this
  skill or a verified Active method or execution skill routes an exact R task
  specification. It audits R, packages, libraries, startup state, namespaces,
  locale, encoding, RNG, parallelism, inputs, script, command, outputs, and
  tests, then runs the approved entry point once and returns an R Research
  Computing Record. It does not choose the scientific question or method, install or
  update R or packages, create or restore environments, absorb package-specific
  or R-neuroimaging ownership, hide failures, or interpret results. Triggers:
  run this in R, R analysis script.
metadata:
  level: skill
  system: Research Assistant System
  part: "4"
  family: computing
  modality: any
  dependencies: ""
  requires: R with the needed packages
  gates: running on real data
  created: "2026-07-23"
  updated: "2026-10-29"
---

# R Research Computing

Implement and verify one bounded, approved R task in an already available
environment.

## Purpose

`r-research-computing` owns:

- executable, version, package, library, startup, locale, encoding, and RNG
  preflight for one R task;
- translation of an approved task into one R entry point and its verified
  source dependencies within the selected project structure;
- explicit namespace, input, operation, output, and side-effect records;
- bounded fixture testing and one approved `Rscript` execution;
- failure-preserving output verification;
- an R Research Computing Record.

The user owns the research question, estimand, scientific method, model, packages,
parameters, thresholds, exclusions, confirmatory status, interpretation, and
claims.

[cogsci-statistics](../cogsci-statistics/SKILL.md) owns statistical method-family comparison.
[statistical-analysis](../../skills/statistical-analysis/SKILL.md) owns general cross-software statistical execution.

Use this skill when the user names it, the bounded request matches its
frontmatter description and trigger meaning, or a verified matching coordinator,
companion, or capability handoff selects it.

Do not trigger from `R`, `R code`, `RStudio`, `tidyverse`, `statistics`,
`analyze`, `run this`, or a package name alone.

Do not use this skill to select a method or package, install or update R,
install or restore packages, create an environment, absorb a package-specific
adapter, expand into the deferred R neuroimaging gap, retry automatically, or
write outputs without approval.

## Inputs

Obtain or mark missing:

- approved bounded computing task and its scientific owner;
- confirmatory, preregistered, deviated, exploratory, or noninferential status
  when applicable;
- exact source inputs, hashes, schema, observation grain, encoding, and access
  boundary;
- approved operations, parameters, package APIs, and acceptance criteria;
- exact R executable and required R version;
- package names, versions, build state, library locations, namespaces, and
  relevant licenses;
- an existing entry point or authorization for a new one, the applicable
  project structure, and the source dependency boundary;
- working directory and path-resolution rules;
- `.Renviron`, `.Rprofile`, `.RData`, inherited `R_LIBS*`, and startup policy;
- locale, time zone, encoding, decimal, factor, contrast, and date assumptions;
- seed, `RNGkind`, `RNGversion`, parallel backend, workers, threads, and
  nondeterminism;
- memory, time, network, credential, compiler, system-library, external-process,
  and compiled-code boundaries;
- output destination, overwrite policy, artifact list, and source-preservation
  rule;
- synthetic or approved fixture and expected invariants.

If the task, method ownership, executable, package API, library path, startup
state, locale, RNG, input, acceptance criterion, or output boundary is
unresolved, stop with **R computing specification incomplete**.

## Steps

### 1. Preflight the exact R environment

Record:

- executable path, `R.version`, platform, `R.home()`, and command-line flags;
- `.libPaths()`, every inherited `R_LIBS*`, package versions, build state,
  load paths, namespaces, masking, and `sessionInfo()`;
- `.Renviron`, `.Rprofile`, `.RData`, working directory, locale, time zone,
  encoding, BLAS, LAPACK, and compiler state;
- `RNGkind`, `RNGversion`, seed, parallel backend, workers, and thread limits;
- package APIs, defaults, deprecations, system commands, network calls, and
  side effects.

R `4.6.1`, Happy Hop, was current on 2026-07-23. Inspect the participant's selected R version, inherited `R_LIBS` and effective `.libPaths()`, including the chosen `Rscript --vanilla` behavior. These are runtime facts to verify, not paths to hard-code or silently change. Live execution verifies
the exact environment and stops on incompatibility.

### 2. Gate 1: approve the R Computing Contract

Show:

- task held invariant and its canonical scientific owner;
- input metadata, privacy boundary, operations, packages, and APIs;
- R executable, versions, libraries, namespaces, startup state, locale,
  encoding, RNG, and parallel state;
- script construction or audit plan;
- fixture, assertions, warnings, errors, and acceptance criteria;
- reads, writes, side effects, resources, artifacts, and destination.

Gate 1 authorizes read-only environment and code inspection plus one bounded
synthetic or approved fixture test. It does not authorize observed-data
execution, installation, package restoration, network access, credentials,
external processes, writes, overwrites, retries, or interpretation.

### 3. R routes for the approved computation

Where applicable, compare only:

- an existing verified entry point with its source dependencies;
- a new implementation using the structure selected for the task, then the
  applicable verified project convention. Use one minimal self-contained
  script as a fallback when neither resolves the structure;
- one already Active package-specific adapter route.

For each show task equivalence, package and API state, hidden-session risk,
clarity, testability, resource needs, visible output, benefit, tradeoff, and
limitation. Do not broaden the scientific method or package set.

### 4. Build or audit the implementation

Use the approved structure and confirm the scope of any source write before creating files. Use the vault-root `00 ASTORIA/templates/code_template.md` as an optional scaffold when it fits the task. In a modular implementation, verify each sourced file, its path, hash and load order. Keep one entry point for the approved command.

Use descriptive objects, explicit package namespaces, explicit paths, visible
parameters, source-preserving reads, explicit outputs, and inspectable
assertions. Show an Exact Operation Table:

| Step | Object and grain | Exact operation or API | Defaults and assumptions | Expected invariant | Side effect |
|---|---|---|---|---|---|
| Read or parse | | | | | |
| Filter, recode, or join | | | | | |
| Transform or compute | | | | | |
| Model or package call | | | | | |
| Validate | | | | | |
| Write | | | | | |

`Rscript --vanilla` is a defensible default proposal, but it is not a clean
environment guarantee. Record inherited environment variables and
`.libPaths()` after process startup.

### 5. Review the exact script and session state

Show:

- full entry point and all sourced files, their hashes and source order,
  command, arguments, and working directory;
- input paths, hashes, schema, grain, encoding, and access boundary;
- R, package, library, namespace, startup, locale, BLAS, and LAPACK state;
- every operation, default, factor level, contrast, missing-value rule,
  timezone, seed, RNG, parallel setting, and tolerance;
- network, compiler, system command, external process, temporary-file, and
  write behavior;
- fixture results, expected warnings, errors, failure policy, and resources.

An available package does not determine the method. A successful R run does
not validate the statistical model, scientific interpretation, or claims.

### 6. Gate 2: approve one exact R execution

Ask the user to approve the exact:

- entry point and sourced files with hashes, `Rscript` command, inputs and
  hashes, package and library paths, startup policy, parameters, seed, RNG,
  threads, and resources;
- observed-data access and one-run, no-repair policy;
- outputs, destination, overwrite, partial-artifact, and cleanup behavior.

Reopen Gate 2 before changing any entry point, sourced file, package, library
path, startup state, locale, input, operation, parameter, seed, parallel plan,
command, output, retry, or destination.

### 7. Run once and verify the approved R script

Run only the approved command once. Capture:

- script, source, input, environment, and version hashes;
- executable, R and package versions, libraries, namespaces, startup state,
  locale, BLAS, LAPACK, RNG, and parallel state;
- stdout, stderr, messages, warnings, errors, exit status, and duration;
- row, object, schema, factor, missingness, numerical, and fixture invariants;
- output manifests, hashes, partial artifacts, overwrite state, and cleanup;
- specification deviations and confirmatory or exploratory labels.

Return:

```text
R Research Computing Record
Approved task and scientific owner:
R executable, version, and platform:
Packages, libraries, namespaces, and licenses:
Startup, locale, encoding, BLAS, and LAPACK:
Inputs, schema, grain, and hashes:
Script, command, parameters, and operations:
RNG, parallelism, and resources:
Fixture and assertion results:
Observed-data execution, if approved:
Messages, warnings, errors, and exit status:
Output verification and partial artifacts:
Deviations and analysis-status labels:
Specification-conformance check:
What execution does not establish:
Artifacts and hashes:
user-owned interpretation and claims:
```

## Boundaries

- Never install or update R or packages, run `install.packages()`, restore an
  environment, or initiate a Bioconductor operation.
- Never treat `--vanilla` as sufficient isolation without checking `R_LIBS*`,
  `.libPaths()`, loaded namespaces, and inherited environment variables.
- Never load `.RData`, hidden startup configuration, or a masked function
  silently.
- Use explicit namespaces for consequential package functions.
- Never infer locale, encoding, decimal mark, timezone, factor levels,
  contrasts, missing-value rules, seed, RNG, or parallel plan.
- Do not use a network, credential, compiler, system library, external process,
  or compiled code without separate authority.
- Preserve warnings, errors, exit status, and partial artifacts. Do not repair
  and rerun without a new Gate 2.
- Stop on unresolved method ownership, unavailable or incompatible R, missing
  package, ambiguous libraries, package masking, hidden startup state,
  encoding or locale ambiguity, unseeded stochastic work, unavailable external
  resource, failed fixture, unexpected object changes, source mutation,
  output collision, outcome-dependent changes, or requested interpretation.

## R execution and reproduction records

Use the records that apply to the approved operation. Follow its existing approval, stop, and verification requirements.

- **R Computing Decision Record.** Show the R Computing Contract, library and namespace audit, operation table, startup state, RNG, and output risks. This makes hidden R session state visible. This requires detailed environment inspection. Runtime conditions can still change.
- **R Implementation Route Cards.** Assess the existing entry point, a new implementation in the selected structure, or an exact Active-adapter route when applicable. Use the single-file fallback only when no applicable structure is selected. Preserve the approved packages and scientific method.
- **R Research Computing Record.** Execute the approved command once through its exact entry point. Verify the local source dependencies, inputs, outputs, tests, warnings, and session state. Preserve failure evidence. Repairs require another approval. One execution does not establish robustness.

Use an additional check below only when it addresses a specific uncertainty and its scope and approvals are in place.

- **Implementation Equivalence Matrix.** Compare two user-approved equivalent R implementations on a synthetic or approved fixture. This exposes package or API-specific behavior. This adds code and testing. Fixture equivalence does not establish scientific validity.
- **R Reproduction Bundle.** Add a separately approved clean-session replay on synthetic or approved fixture data. This tests reproducibility against hidden session state. This adds compute and artifact review. This does not validate the method or observed-data inference.
- **Reproducibility and License Matrix.** Add a second fresh-session fixture reproduction and package-license review. This detects hidden state and selected reuse restrictions. This adds review time and another run. Same-machine agreement is not independent replication.

## Checks

- **Positive:** an approved R data or model implementation produces the
  contract, exact script, fixture, approved command, and verified record.
- **Method:** `Which model should I use in R?` routes to
  [cogsci-statistics](../cogsci-statistics/SKILL.md).
- **Overlap:** cross-software execution stays with [statistical-analysis](../../skills/statistical-analysis/SKILL.md);
  this skill owns only R-specific runtime and code semantics.
- **Missing package:** reports an implementation gap without installation.
- **Library drift:** detects duplicate or older user libraries and requires an
  explicit package path.
- **Startup:** detects `.RData`, `.Rprofile`, `.Renviron`, and inherited
  `R_LIBS*` rather than claiming a clean session.
- **Failure:** preserves warnings, error state, and partial artifacts without a
  retry.

## References

- R Core Team. (n.d.-a). *An introduction to R* (Version 4.6.1). https://cran.r-project.org/doc/manuals/r-release/R-intro.html
- R Core Team. (n.d.-b). *libPaths*. https://search.r-project.org/R/refmans/base/html/libPaths.html
- R Core Team. (n.d.-c). *R data import/export*. https://cran.r-project.org/doc/manuals/r-release/R-data.html
- R Core Team. (n.d.-d). *R installation and administration*. https://cran.r-project.org/doc/manuals/r-release/R-admin.html
- R Core Team. (n.d.-e). *Random*. https://search.r-project.org/R/refmans/base/html/Random.html
- R Core Team. (n.d.-f). *sessionInfo*. https://search.r-project.org/R/refmans/utils/html/sessionInfo.html
- R Core Team. (n.d.-g). *Startup*. https://search.r-project.org/R/refmans/base/html/Startup.html
- R Core Team. (2026). *R* (Version 4.6.1) [Computer software]. R Project. https://www.r-project.org/
