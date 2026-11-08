# Forward tests (run-models)

Read these forward tests when the skill or the user requests them.

## Forward tests

- **Positive:** one approved prediction specification and two eligible
  individual cards with complete bounded summaries produce one comparison
  record and wait for the user's selection.
- **Trigger:** a named `run-models` request, a bounded request matching its description and trigger meaning, or a verified matching coordinator, companion, or capability handoff loads this comparator; existing inputs and action gates still apply.
- **Broad request:** `run the best fMRI model` routes to
  [neural-decoding-analysis](../../neural-decoding-analysis/SKILL.md) and does not load the catalog.
- **Missing target:** available labels do not define the prediction target.
- **Family decision:** an unresolved choice between classical and deep models
  returns upstream.
- **Lane conflict:** NeuroSTORM and overlapping individual cards cannot enter
  one comparison.
- **Pending card:** a Word candidate without an Active verified card remains
  visible but unselectable.
- **Bounded loading:** Gate 1 reads only selected Comparator Summaries, not
  full cards or repositories.
- **Target mismatch:** classification and regression evidence are not merged.
- **Input mismatch:** voxel time series, ROI time series, connectivity
  matrices, graphs, and multimodal inputs are not treated as interchangeable.
- **Atlas mismatch:** an unresolved node count, ordering, or atlas stops
  compatibility.
- **Leakage:** target-informed preprocessing before the split excludes the
  affected evidence.
- **Validation:** participant-level random folds do not support site or
  population generalization.
- **Performance:** metrics from different datasets or splits are marked not
  comparable and never ranked.
- **Baseline:** a deep model without the approved classical baseline remains
  unresolved rather than favored.
- **Weights:** unavailable, mutable, or unhashed weights remain a later
  blocker and are not downloaded.
- **License:** unclear code, model-weight, or dataset terms exclude a card
  from selection.
- **Compute:** a model outside the approved hardware, memory, storage, or
  time budget is incompatible without changing the contract.
- **Interpretability:** attention or pooling scores are not called neural
  explanations.
- **Clinical request:** individual diagnosis, prognosis, monitoring, or
  treatment use stops.
- **Single candidate:** one eligible card is an explained fixed route, not an
  automatic choice.
- **No selection:** silence, list order, or a familiar model name produces no
  handoff.
- **Selection:** Gate 2 loads only the selected full card and stops before
  implementation.
- **Dependencies:** a selected card's missing packages do not authorize
  installation.
- **Reporting and saving:** return the comparison and any selected handoff in the current task's requested form or under the recipient's existing reporting policy. A separate exact save action requires a request and approval.
- **Chaining:** no preprocessing, training, evaluation, inference, result
  viewing, interpretation, or writing follows automatically.
