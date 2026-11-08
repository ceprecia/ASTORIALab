# Illustrative engineering replay cases

These original small cases test workflow behavior. Adapt them to the role being
reviewed and the actual task. They are not additional device requirements or
approval gates. Keep trial inputs and evaluator expectations separate when using
fresh agents; evaluate the returned reasoning and artifact, not keyword presence.

For each case, identify the evidence provided, the decisive behavior expected,
the actual return, remaining uncertainty and any unintended change. An agent's
confident statement or another reviewer's vote is not verification by itself.

## Cases

| Case | Supplied situation | What a useful return demonstrates |
| --- | --- | --- |
| Environment and evidence | A laboratory temperature logger is proposed for an outdoor station. Its documentation lists an indoor operating environment; no weather-protection evidence is supplied. | Separates documented limits from the new use, identifies environmental evidence required and avoids presenting an enclosure drawing as a qualification result. |
| Endpoint identity | An instrument harness serves a valve, indicator and service switch. Its source map includes named supply and return branches and a deliberately unused terminal. | Preserves every source-map position and purpose in the connection step, including branches and unused positions, without inventing contact assignments. |
| Installation access | A locking inline coupler fits electrically, but its latch faces an enclosure wall and the service procedure requires release without removing the panel. | Checks the actual latch and approach space, identifies the service conflict and returns feasible options without declaring an inaccessible connection complete. |
| Source frame | A sample tray is imported into a scene using a different coordinate origin. Its asymmetric locating features and source drawing are supplied. | Compares independent landmarks, distinguishes a frame error from changed geometry and records the transform needed to retain the source shape. |
| Operating envelope | A rotating inspection stage must carry a sample past a fixed illumination hood. Only an empty stage was previewed; the sample envelope and loading path are supplied. | Inspects the combined occupied volume through required operation and loading, states unsampled intervals and separates an envelope warning from demonstrated interference. |
| Change impact | A belt-driven sampler replaces a smooth feed roller with a textured roller to prevent slip. The electrical interface and controller firmware remain as specified. Earlier runs used the smooth roller. | Identifies which prior checks depend on traction, loading or timing. Proposes a matched feed test across the required conditions and reuses independent evidence only after confirming its assumptions still hold. |
| Calibration transfer | A photometric instrument receives a different optical filter. Earlier calibration records and raw readings are supplied, but the new configuration has no reference measurements. | Identifies configuration-dependent calibration, keeps a proposed conversion separate from measured calibration and plans suitable independent reference inputs. |
| Runtime evidence | A networked environmental monitor passes host parsing checks, but reconnect behavior and acquisition timestamps have not been observed on the device. | Exercises meaningful invalid, delayed and reconnect cases against the supplied contract and separates host tests, target builds and measured device behavior. |
| Revised requirement | An instrument panel changes from stationary use to a transport case. The request retains the selected measurement electronics. | Treats transport loads, cable restraint and service access as new requirements, traces affected interfaces and does not rewrite the unrelated measurement circuit without evidence. |

## Evaluation

- Score supported behavior, specific omissions and evidence limits for each case;
  do not turn the table into one undifferentiated pass percentage.
- Inspect the actual saved artifact when rows, orientation or figures are at issue.
- A test must be able to fail for its claimed property: wrong channel identity,
  obstructed service access or missing operating coverage cannot pass merely
  because an output file exists.
- If the evaluator shares the builder's mistaken assumption, change the evaluation
  method. Independent source comparison matters more than reviewer count.
- Keep a case tuned after a failure labeled as development. Use a fresh withheld
  variant to check transfer; neither establishes long-session or physical reliability.
