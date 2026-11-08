# Forward tests (netneurotools-guide)

Read this reference when the skill or the user asks for it.

## Forward tests

- **Positive:** one approved stable-public-API operation with fixed inputs,
  parameters, version, side effects, and fresh destination produces one
  Operation Record and stops.
- **Trigger:** Load for the explicit `netneurotools-guide` skill name, a bounded request such as `network null models with netneurotools`, or an exact netneurotools handoff from a verified active method skill.
- **Routing:** `which communication metric should I use?` returns to
  [brain-connectivity-modeler](../../brain-connectivity-modeler/SKILL.md).
- **Inference:** `what permutation design is valid?` returns to
  [statistical-analysis](../../../skills/statistical-analysis/SKILL.md).
- **Environment:** missing netneurotools stops without installation or source
  cloning.
- **Version:** development HEAD, a `0.2.x` API assumed under `0.3.0`, or a
  post-release documentation signature not present in the selected source
  stops.
- **API:** candidate functions absent from the exact stable public API stop
  rather than being synthesized from memory.
- **Plot API drift:** stable `0.3.0` rejects development-only plotting
  functions and `panel_size` or `show_silhouette` arguments.
- **Experimental:** an alpha `experimental` function stops for a separate
  nonstable design decision.
- **Alignment:** equal-size adjacency and distance matrices with different
  node orders stop.
- **Signed graph:** negative edges are not set to zero to satisfy an
  implementation.
- **Transform:** the candidate's logarithmic weight transform is rejected
  without an approved domain and disconnected-edge policy.
- **Null:** a degree-preserving function does not earn a strength, distance,
  signedness, connectedness, or mixing claim without measured evidence.
- **Randomness:** an arbitrary `nodes * 20` swap count or unrecorded seed
  stops.
- **Partial randomization:** a reported achieved swap count below the
  approved request is incomplete and does not trigger an automatic retry.
- **Modularity:** one resolution, one stochastic solution, or high Q does not
  establish a unique or true community structure.
- **Spatial:** unrestricted label shuffling does not replace an approved
  spatially constrained null.
- **Permutation:** the minimum attainable p-value and multiplicity remain
  visible.
- **Fetch:** an atlas request stops before network access, home-directory
  cache use, directory creation, download, extraction, or replacement until
  Gate 2.
- **Force:** `force=True` stops without a separately approved exact
  replacement action.
- **Surface:** equal vertex counts with different template, density, or
  hemisphere order stop.
- **Plot:** a hidden template fetch, private plotting helper, or unapproved
  deprecated PySurfer route stops; automatic color limits remain an explicit
  approved policy.
- **Failure:** warnings, failed rewires, incomplete downloads, and partial
  temporary outputs are preserved without retry or cleanup.
- **QC:** a valid matrix, low p-value, high modularity, or attractive surface
  is not labeled scientifically valid or accepted.
- **Chaining:** no second metric, null, statistic, plot, export, or
  interpretation runs automatically.
