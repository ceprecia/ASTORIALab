# The setup interview

Read this only in new-vault mode, when [setup-my-vault](../../setup-my-vault/SKILL.md) is collecting the answers that become the first `me.md`. Every app asks the same questions in the same order.

## How to ask

- Ask each question as a choice: the options below plus "other" (free text). Use the app's option prompt when it has one (Cowork's question widget, Codex's plan-mode choices). In plain chat, print the question and a numbered list, and read the number or the text back.
- Ask one round at a time: a handful of questions per message, never the whole interview at once and never one question per message.
- Multi-select questions say so; the user can pick several.
- A question already answered earlier in the conversation is not asked again.
- Apply the listed default for a skipped answer when one is supplied. Leave omitted or unspecified preferences out of `me.md` and distinguish them from applied defaults in the read-back.
- No question here asks for health, religion, politics, family, or finances. If the user volunteers such a fact, it goes in `me.md` only where they put it, in their words.

## Round 1: who you are

| id | Feeds | Question | Options | Default |
| --- | --- | --- | --- | --- |
| name | Preferences, Summary | What should I call you? | free text | the vault owner's name from the system if known, else ask |
| role | Summary, Career Direction | Where are you in your research life? | undergraduate or master's student; PhD student; postdoc or early-career researcher; faculty or established researcher; researcher outside academia | leave unspecified; do not infer |
| field | Research Interests | Which field is closest to your work? | cognitive science or psychology; neuroscience or neuroimaging; biology or medicine; social or behavioral science; computational or data science; other | ask |
| subfields | Research Interests | Name up to five topics you work on (free text, comma separated). | free text | none |
| methods | Research Interests, toolkit seed | Which methods and data do you use? (multi-select) | behavioral experiments; questionnaires and surveys; fMRI; structural MRI or DWI; EEG or MEG; PET or ASL; electrophysiology or calcium imaging; genomics; pathology or histology; computational modeling; public datasets; none yet | none yet |
| institution | Summary | Institution or lab, if you want it in the file. | free text | omitted |

## Round 2: how the assistant should behave

| id | Feeds | Question | Options | Default |
| --- | --- | --- | --- | --- |
| tone | Preferences, AI Personality | Which tone do you want from me? | cheery and warm; friendly and clear; professional and direct; blunt and terse | friendly and clear |
| initiative | Preferences | When a request leaves a small decision open, should I: | ask before acting; make a reasonable choice and say so; make the choice silently; omit this preference | omitted |
| startup_disclosure | Rules | At the start of a fresh session, when should I describe which context I can access? | at the start of each fresh session; when I ask; omit this preference | omitted |
| emoji_prose | Rules | Emoji in my replies and in notes I write? | none; sparingly; freely | leave unspecified; follow the selected document format |
| emoji_headings | Rules, templates | Emoji in headings and callouts of notes? | none; keep the template's; freely | leave unspecified; follow the selected document format |
| emoji_folders | Structure (Stage 3) | Emoji in folder names? | keep the default emoji; no emoji | keep the default emoji |
| format | Preferences | How should replies be shaped? | prose paragraphs; short bullets; summaries first, then detail on request; omit this preference | omitted |
| dashes | Rules | Em dashes in generated prose? | never; allowed | leave unspecified; follow the selected document format |
| language | Preferences | Which language for replies and notes? | English; another language (name it) | English |

## Round 3: how you work

| id | Feeds | Question | Options | Default |
| --- | --- | --- | --- | --- |
| devices | Current Tools | Where do you use this vault? (multi-select) | Mac; Windows; Linux; iPhone or iPad; Android | ask |
| ai_app | Current Tools, shims | Which AI app are you setting this up with? | Claude Cowork; Claude Code; Codex; Antigravity; another app that reads AGENTS.md | detected from the session when possible |
| references | Current Tools | Reference manager? | Zotero; Mendeley or EndNote; Paperpile or ReadCube; none | none |
| code | Current Tools, Code Preferences | Do you write analysis code, and in what? (multi-select) | Python; R; MATLAB; Julia; shell; I do not write code | I do not write code |
| software | toolkit seed | Which analysis software do you use? (multi-select, shown only when code is not "I do not write code" or methods include imaging) | fMRIPrep; FSL; FreeSurfer; SPM; AFNI; nilearn; MNE; EEGLAB; scikit-learn; PyMC or Stan; none of these | none of these |
| external_folder | Working Locations | Do you keep research files in a folder outside this vault? | yes; no | no |

## Round 4: what you want from the vault

| id | Feeds | Question | Options | Default |
| --- | --- | --- | --- | --- |
| goals | Summary, Skills | What should this vault mainly help with? (multi-select) | studying and learning; reading and organizing papers; designing studies; analyzing data; writing papers and grants; planning and tracking projects | all of them |
| capture | Notes and MOCs | How do you want progress recorded? | inline in each project's log when I ask; also a dated calendar log; I will write my own notes; omit this preference | omitted |

## Read-back

After round 4, restate every answer and applied default for the proposed `me.md` in the current task's requested form or under the recipient's existing reporting policy. Preserve the user's wording for free-text answers. Identify omitted or unspecified preferences separately as choices that stay out of the file. Wait for one yes or corrections. Apply corrections in place and keep the other answers.

## What the answers become

- `Me Summary Statement`: two or three sentences in the third person from name, role, field, subfields, methods, goals. No inference beyond the answers.
- `Preferences`: confirmed address, tone, initiative, format and language choices; leave unanswered tastes unspecified.
- `AI Personality`: the tone option expanded into two or three guide lines.
- `Rules`: the confirmed emoji and dash choices, plus the standing vault rules from the template. Use `{{startup_disclosure_line}}` only for a confirmed startup disclosure preference. Report material access limits when they affect the current task.
- `Notes and MOCs`: fill `{{capture_line}}` only from a confirmed capture preference. Saving follows the current request and authorization.
- `Current Research Interests`: field and subfields as a list.
- `Career Direction`: the role option as one sentence; no goal is invented.
- `Current Tools`: devices, AI app, reference manager, code, software.
- `Working Locations`: the vault path; the external folder path is added in setup Stage 4 once the user has pointed to it.
- `Current Projects and Areas`: written in setup Stage 4 from the accepted PARA list; left as a heading with one line until then.
- `Writing Standards` and `Code Preferences`: recipient-supplied choices and applicable project requirements. Do not turn inherited examples into personal preferences. Omit Code Preferences when the recipient does not write code. Research integrity requirements remain in force.

## Greeting

After the file is written, read `me.md` back (not the chat) and greet the user in the chosen tone and address form, in one or two sentences: who they are, what they work on, and one thing about how the assistant will behave. Then hand back to setup-my-vault.
