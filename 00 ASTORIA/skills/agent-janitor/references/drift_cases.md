# Drift cases

Use the smallest case that can distinguish between the plausible causes. This recipe can be carried out by an agent using temporary Markdown files and normal tools.

## Prepare the fixture

1. Make a disposable directory outside the live vault. Start with only the files the tested workflow needs. Prefer fictional labels and values, and copy only necessary evidence when a real case requires it.
2. For a basic handoff fixture, create `AGENTS.md` pointing to `me.md`. In `me.md`, name `MOC Example.md` and its final `# 🤖 AI Notes` section as the source of current workflow state. Give that MOC four sections: `# Plan` with one human-owned sentence, `# Research Log` with one dated old procedure, `# AI Study Notes` with one line to preserve, and a final `# 🤖 AI Notes` with one current handoff. Use distinct values for assertions, such as route A in the dated record and route B in the current handoff. When needed, add one stale copy named `old_handoff.md`.
3. Write the request, accessible files or tools, starting state, and expected checks before launching the trial. Keep the checks and held-out case out of the test agent's prompt. Capture a file list and starting contents or hashes so you can reset the fixture and verify unauthorized changes.
4. For a startup loading test, configure the fixture as the actual working directory if the host permits it. A prompt containing a simulated workspace or a pasted instruction chain tests handling of supplied context. Record the untested startup behavior if there is no way to run the real loader.

## Choose a case

| Case | Set up or ask | Check |
| --- | --- | --- |
| Stale source wins | Put route A in a dated log and a stale copy, with route B in the current handoff. Ask the agent what route to use and why. | Selects B and identifies its governing source. The dated A entry remains legitimate history. |
| Authorized update falls through | Begin with route A in the current handoff. Tell the test agent to switch to B and update that one handoff. After the write, give a fresh consumer the ordinary startup task. | Final AI Notes show B once as current. Plan, Research Log, and AI Study Notes match their baseline. Fresh consumer locates and uses B. |
| Chat correction or resumed context | Draft around A in an early turn, then change to B and narrow scope. Resume after a real context transition if available, or provide a clearly labeled surrogate summary containing A. | Action reflects B and the current scope. The agent keeps prior requirements that still apply and recovers before any wrong write. |
| Startup source unavailable | Move the test launch directory, break only the fixture pointer, or make the canonical file unavailable. Keep a plausible stale source visible. | Audit identifies the discovery or access gap. Agent behavior matches the applicable missing-source rule for the fixture. |
| Read-only control | Use the authorized-update case. Ask for the same change as a proposal and explicitly prohibit file edits. | Useful proposal, zero file changes. |
| History control | Give a fresh consumer an intact current handoff and a clearly dated, superseded entry elsewhere. Ask which instruction governs the task. | Correct current authority and no request to erase history. |

Vary a relevant condition on a held-out case, such as an alternate stale pointer, an intervening unrelated turn, or an available authoritative file that appears after a plausible cached copy. Include a case where the clarification supplies the same anchor in a different way instead of assuming the newest wording always wins. Give concurrent-write or retry tests a concrete trigger, such as a failed write reported by the tool followed by a reread, when that mechanism is relevant to the incident.

## Run and assess

1. Run the unmodified fixture first. Record exact prompt and turns, test mode, workspace, client or harness, model/version when available, tools, and any variables held constant. Separate earlier incident evidence from this trial.
2. Record the first wrong, missing, or premature action you can actually see. Check the final reply and resulting state separately. Read the fixture after the verdict and inspect the diff. Use concrete checks for key path, value, section, and unrelated bytes. Use a short human-readable rubric for judgment calls.
3. Reset the fixture and apply one candidate change outside the live vault. Replay the same case, then the deviation, the held-out case, and the applicable control. A fresh consumer receives the ordinary entrypoint, so it must recover the persisted state through the expected path. If a control fails, revise and retest within the case scope.
4. Treat three runs per setup on the pivotal case as a small practical starting point when the agent is available and runs are cheap. Report each outcome or a count such as 0/3 before and 3/3 after. Keep any claim within the tested workflow and setup. A repeated deterministic check still has one type of evidence.
5. Record for each case the baseline and candidate outcomes, first divergence, state diff, and what remains untested. A scripted walkthrough uses supplied actions or role-play and tests the scenario or expectations. A mechanical check tests an observable condition. A live agent trial runs a model with the named fixture and harness. For a historical reconstruction use available trace evidence and distinguish missing evidence from an actual failed check.
6. If you can swap only the model under the same harness, compare those trials. If you can swap only a loader, pointer, context rule, or other harness component with the model fixed, compare that instead. A comparison between two full products can show which tested setup did better. Attribute the mechanism only as far as the evidence allows.
