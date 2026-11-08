---
name: teaching-assistant-builder
description: >-
  Creates or refreshes a college teaching area and one course offering from
  approved sources, preserving existing notes and resources. Owns teaching setup
  and syllabus updates. Triggers: set up a teaching course, import my teaching
  syllabus, organize my teaching classes.
metadata:
  level: skill
  system: Teaching Assistant System
  dependencies: ""
  created: "2026-10-20"
  updated: "2026-10-29"
---

# Teaching Assistant Builder

Set up one teaching home and each college course offering without duplicating notes, policies, or files.

## Purpose

Own first setup of the teaching area, adding a course from a syllabus, refreshing the same offering, and an explicitly requested migration of existing teaching materials. Support professors, instructors, and TAs. Student coursework belongs to class-builder; research mentorship is not automatically a teaching course.

## Inputs

- The user's request, root `me.md`, layout reference, and existing area instructions if present.
- Read the Teaching MOC Template for an authorized Area MOC creation and the Teaching Class Template for an offering note. Use the configured templates directory.
- Settled setup answers. For offering work, use the supplied syllabus, approved instructor decisions, and any existing course note and folder.
- For offering-dependent writes, verify exact course identity: code, title, term, section when distinguishing offerings, instructor, and the user's role. A course code alone does not identify an offering.
- The operation mode and authorization: plan, simulation, or local setup. Preserve narrower scope through every handoff.

## Steps

1. **Resolve the existing owner.** Inspect bounded teaching navigation and candidate course notes. Reuse a matching populated note even if its directory entry is absent. Read a candidate fully before editing. If the Area does not exist, start from root instructions and templates. Treat missing Area or course files as proposed work and verify their scope in preflight.
2. **Ask only unanswered setup questions.** Read the existing configuration and any supplied syllabus relevant to an offering in scope. For independently authorized Area-only setup, limit questions to the Area and standing teaching preferences. Ask at most three consequential questions in one batch; continue independent inspection while awaiting a required answer. Never ask again for information already supplied.
   - First area setup: teaching role and preferred help; teaching/feedback style; existing folders to preserve; default platforms and communication channels; desired response/grading turnaround and reminder arrangements.
   - Each course: term/section and role; teaching-team responsibilities; platforms used for content, submissions, quizzes, grades, and email; approved reference set and precedence decisions; assignment-specific grading and exception authority; technical support route.
   - Ask about prospective reminders as a preference only. Creating a course does not create a scheduled task. Missing platform links or unstated deadline times remain unspecified.
   - After preflight, record only the recipient's verified standing teaching preferences in the Area AGENTS.md when its creation or edit is authorized, including the applicable Area layout and offering-placement convention. Keep course-specific answers and the verified destination for this offering in its course note. Reuse existing instructions. Do not personalize this skill or create an interview transcript.
3. **Read the sources for an offering in scope.** Extract supported identity, learning objectives, meetings, office hours, assessments, grading rules, deadlines/windows, required materials, and responsibilities. Distinguish approved policy, proposal, historical material, and unresolved conflict. Check date/weekday/term consistency; retain tentative dates and source timezones. A newer approved decision updates only its applicable scope and effective period. Do not infer a midnight deadline, final grade weight, or instructor approval from a draft.
4. **Preflight the authorized scope.** Confirm the operation mode before any write. When the plan includes creating a direct Teaching MOC or changing its role, verify the intended role and check for conflicting properties and competing direct markers before applying dependent writes. For independently authorized Area-only setup, verify the owning Area and resolved layout, the exact eligible paths for the scoped Area folder, Teaching MOC, AGENTS.md and any local working folder actions, conflicts at those paths, and authority for each proposed creation or edit. Limit this route to the authorized Area work. End plan-only work with the plan. Keep simulation within its designated temporary fixture. Once this Area-only preflight passes, apply only the authorized Area actions in step 5, verify the affected files, and return the result. Skip the offering steps and leave the timeline free of placeholders.
   For offering-dependent setup, verify the exact offering identity independently from its approved records. Keep each offering's course note and supporting files together. Use the verified eligible folder selected for the offering. If no folder is selected, apply the verified placement policy for this offering, then use the verified owner working location when the policy leaves placement open. The default local arrangement is an offering folder under the Teaching Area’s `files/`. Honor a documented external workspace or existing operational layout. Use term/course nesting only when it serves the confirmed convention. Resolve actual roots and placement rules from `me.md`, the layout reference, and applicable Area instructions. Report an unresolved or ineligible selected destination before writing. For the same offering, reuse its verified existing folder and name unless an authorized move covers a change. Follow the move rules below for any relocation. For a new note, use an explicitly selected eligible filename once the offering identity is independently verified from its records. If no name was selected, use the applicable verified naming convention. As a fallback, include the term and add a section suffix when needed to distinguish offerings. Verify each required path is available for the intended action and resolve collisions before applying the setup. Use actual semester chronology rather than alphabetical season sorting. Check the shared destination before writing links. A repeat offering gets its own record and cannot overwrite an earlier term. Verify the scope of each proposed write before creating any dependent Area or course files or folders. Distinguish creation or updates of the Area MOC and AGENTS.md, the course note and source copies or moves, the MOC timeline link and any current-term shortcut, and any affected links or instructions. Record the course files covered by the offering-save authorization. Verify authority for Area files, index edits, and other writes separately, reusing authorization already given for each exact action. If identity, an eligible destination, or a required write remains unresolved or outside scope, report the blocker before starting dependent writes. Omit optional edits outside scope. End plan-only work with the plan. Keep simulated writes inside the designated temporary fixture.
5. **Apply the authorized Area setup.** After preflight passes, create or update only the Area files authorized for this setup. Reuse existing verified paths. For a course-only request, omit Area work outside its scope. Use the eligible Area arrangement selected for the task, then the applicable verified layout policy. Reuse the existing Teaching MOC and one short AGENTS.md when present. An authorized new Area AGENTS.md points directly to root `me.md` and the verified MOC. When local working files are in scope and the layout remains open, use the Area’s single `files/` folder or the verified equivalent. A documented external workspace can satisfy the working-files requirement. Report an unavailable workspace separately from a missing local entry. Preserve other existing files unless an authorized change includes them. Apply the Teaching MOC Template when creating an authorized MOC. For a direct Teaching MOC, keep the template's top-level `astoria_role: area_moc` and verify that no competing direct note carries the role. Reuse existing MOCs and preserve their frontmatter unless the exact property edit is authorized. Report any conflicting role and preserve existing notes. If an authorized MOC location lies outside direct Area discovery, report the discovery limit. Maintain actual term order in any authorized timeline change. For both notes, follow the selected navigation and link form, then an applicable verified convention. Use plain Markdown links and simple lists where the form is open. Use callouts only when the selected or configured form supports them, and omit optional navigation when the selected form leaves it out. Preserve existing navigation unless its change is in scope. Reuse existing files on every later run. Do not create per-course AGENTS, README files or dashboards. Keep source materials in the owning course's configured location.
6. **Preserve or migrate the materials.** Keep incoming filenames and existing inner organization. Add subfolders only when actual material calls for them. Reuse identical existing files; preserve different same-name versions without silent replacement. An authorized move includes a pre-move file inventory/content check, collision check, exact move, and post-move comparison. Keep temporary checks outside the vault. Before an authorized move, verify that its required active link and instruction repairs, including encoded folder URLs, are within scope. Complete those repairs with the move and preserve historical logs and published exports. Never merge similarly named archives by name alone.
7. **Create or update the course note.** Apply the Teaching Class Template to a new or empty note using the resolved navigation and link form. Add a local folder shortcut only when the user selects one and the receiving app supports it, after verifying the exact offering folder. Make targeted updates to populated notes, preserving user prose, useful properties, files, prior decisions, and logs. Keep course details in properties, approved source pointers and responsibilities in their relevant sections, actual resources under Course Files, and authorized technical continuity at the selected or configured continuity location. Use AI Notes when the chosen template or applicable policy selects it. Remove only empty student-study scaffolding when adapting an existing teaching note. Do not copy student correspondence, rosters, or gradebooks into general navigation.
8. **Connect the offering when authorized.** Reuse an existing verified course-note link if one already resolves under the offering's actual term. Add or update the MOC timeline link only when that edit was authorized in preflight. Add or update a current-term shortcut only for an active offering when the selected or configured navigation includes it and the shortcut edit is authorized. Otherwise return the verified course-note location for any omitted index edits. Keep the directory in that MOC, not a second course list in AGENTS. For an approved move from another area, update the old owner pointer and routing/template rules only where those changes are in the verified move scope. Preserve meaningful degree-history links when appropriate.
9. **Check the affected references.** Verify source attribution and course identity, any included navigation anchors or shortcuts, and preservation of populated notes. When Area setup is in scope, verify the single owning MOC and AGENTS.md and the configured local working folder or documented workspace. When an offering is in scope, verify course-note and supporting-file colocation in its resolved folder. Check student coursework still routes to class-builder. Leave unspecified course facts open.
10. **Return a bounded result.** For Area-only work, return the verified Area paths and scoped actions. For offering work, provide the verified course-note location, any verified MOC link, and filed materials. Include settled answers, omitted edits, unresolved choices and what was actually verified. Return to the invoking companion's original task without another intake.

## Outputs

- Reuse the existing Teaching MOC and one Area AGENTS.md. Limit new files and edits to the authorized scope.
- For an offering, return its verified note and supporting-file location and any verified Teaching MOC link already present or added within scope under its actual term.
- A concise setup or migration result in the current task's requested form or under the recipient's existing reporting policy. A separate saved report requires authorization; do not create a standing task database.
- During simulation, create or edit only the explicitly designated temporary fixture tree. A simulated success is not a live course or platform change.

## Boundaries

- Resolve current permissions from the user and standing instructions; local setup never implies email, LMS, grading, assignment publication, calendar, or reminder writes.
- Preserve populated notes and incoming originals. Review each deletion in the diff. Unclear content is meaningful until shown otherwise.
- Old correspondence can supply examples of situations and tone; current approved sources determine current policy.
- Term rollover may reuse selected teaching material. Do not carry forward students, accommodations, individual exceptions, unconfirmed policies, or unresolved tasks as if they belong to the new offering.
- Do not keep a second copy of global organization rules or personal preferences in skill text. Resolve renamed roots and destinations from current configuration.
- Preserve plan-only, review-only, and simulation modes when invoking any supporting skill.

## Handoffs

- Accept direct requests or a bounded task from teaching-companion through teaching-coordinator. No companion invocation is required for an explicit setup request.
- Return `{offering, owner_paths, source_paths, settled_answers, actions_completed, verification, unresolved, next_owner}` to the invoker.
- Route coursework the user takes or audits to class-builder. If the user both studies and teaches the same course, resolve the requested role before changing either owner's records.
- For requested reminder setup, use the existing scheduling capability with the confirmed course dates and user's authorization; do not build a parallel scheduler.
- Content review belongs to teaching-lecture-review or teaching-assessment; operational platform checks belong to teaching-platform.

## Checks

- Running the same syllabus import again produces no duplicate MOC, AGENTS, course note, folder, source copy, timeline entry, or shortcut.
- A new term or distinct section cannot overwrite the existing offering.
- Only unresolved questions are asked; source facts and previously settled preferences are reused.
- Active paths and encoded links agree with actual destinations. Course resources outside the area's ancestry still resolve its AGENTS through the MOC/course-owner link.
- Original file contents survive migration; intentionally edited notes preserve unrelated content.
- The Area follows its verified layout. The default owner structure uses its MOC, one AGENTS.md and a single local files folder or documented external workspace. Course-specific policies stay with the offering.
- Setup and all simulations leave external course systems untouched unless a separate live action is authorized.

## Modular Plugin Support

No service is required for local setup. Use existing document, PDF, or presentation capabilities to read supplied files when necessary, preserving the reference and operation boundaries. A missing platform connection leaves platform facts unverified; it does not prevent useful local organization. Consult configured institutional support when a platform access problem is in scope.
