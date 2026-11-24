---
name: phd-opportunity-scout
description: >-
  Discovers exact career and funding opportunities, screens their current
  eligibility and manages bounded watch or deadline checks from local settings.
  Use for opportunity evidence and return decisions to PhD Companion; actual
  scheduling and applications stay separate. Triggers: find eligible career
  opportunities, watch funding and postdoc openings, review opportunity deadlines.
metadata:
  level: skill
  system: PhD and Career System
  dependencies: ""
  created: "2026-10-31"
  updated: "2026-10-31"
---

# PhD Opportunity Scout

Find exact openings and notify only when the configured evidence calls for it.

## Purpose

Own bounded discovery and screening of funding, fellowships, postdocs, jobs,
training, travel or other career opportunities, plus configured watch and deadline
checks. Use the existing local profile and return fit/eligibility evidence to PhD
Companion. Opportunity selection, application development, CV tailoring and
recurring-task creation have separate owners.

## Inputs

- Requested mode: one-time discovery/screening, watch check or deadline check.
- The chosen existing MOC's current opportunity profile, source scope and settings.
- For watch/deadline mode: enabled state, cadence/time zone, notification and
  reminder thresholds, chosen destination, state location and delivery capability.
- Current official opportunity sources and prior per-item check/notification state.
  Simulations use supplied synthetic source and delivery fixtures only.

## Steps

1. Read `me.md`, the current request and current settings in the existing owner.
   Reuse supplied preferences and eligibility facts. Distinguish mandatory
   eligibility from preferences and scientific/career fit. Ask only for missing
   facts needed to screen the exact opportunity; unknown eligibility can remain
   uncertain. Return substantial configuration work to phd-career-builder.
2. For one-time discovery, search within the requested profile and identify exact
   opportunities rather than generic sponsor homepages. Verify the current cycle
   from official sources. For a supplied opportunity, inspect its actual notice
   and application instructions. Label program/cycle, sponsor, source, status,
   eligibility criteria, relevant support, closing date/time zone and source gaps.
   A prior cycle's deadline or a search snippet is not current verification.
3. Screen each mandatory criterion against sourced or user-confirmed profile
   facts. Use **eligible** only when all applicable mandatory criteria are supported,
   **ineligible** when a mandatory criterion fails and **uncertain** when a needed
   criterion or fact is missing/conflicting. Show the decisive reason and missing
   confirmation. Rank preference/fit separately; an attractive fit cannot reverse
   ineligibility. Do not silently discard uncertain opportunities.
4. In a watch or deadline check, apply the watch protocol below. If current profile,
   required source or delivery capability is unavailable, report the affected
   capability gap and preserve the last notification state. For a missing profile,
   name the configured path and ask for its current location or restoration
   without recreating it or restarting intake. Do not report a fresh
   successful check or “nothing new” from an old result. Continue independent
   one-time work where possible.
5. Return a short, evidence-linked shortlist or the configured notification result
   to the invoking owner, normally PhD Companion. A requested saved result or state update belongs in the
   existing configured owner sections; preserve their prose and dated history.

## Watch and deadline protocol

1. **Read settings each invocation.** If disabled, produce no notifications and do
   not advance notification state. A direct one-time question can still receive
   an answer. If unconfigured, state the missing fields and offer configuration;
   do not create default notifications or a recurring job. Use the chosen cadence,
   time zone, profile and source scope. An early scheduled check remains quiet;
   an explicitly requested manual check may run immediately.
   Use the invocation's fixed clock in a simulation; use the current check time
   and configured time zone in live work. Do not substitute a stale prior run date.
2. **Obtain current evidence.** Check the current profile and exact official source
   for each relevant opportunity. Track checked-at time, source status and cycle
   separately from last successful notification. A source failure is a failed or
   partial check, even when prior evidence remains available for context.
3. **Identify and deduplicate.** Use sponsor/program's stable official identifier
   or canonical notice URL plus explicit cycle as the item key. Reconcile aliases
   and tracking URLs to that key; a renamed page in the same cycle is not a new
   opportunity. A new cycle is a separate item. Unknown cycle stays explicit and
   is not silently merged with an older cycle. Compare material fields as well as
   identity: eligibility, open/closed status, deadline, support and application
   requirements.
4. **Select changes.** Compare current evidence with the last successfully
   notified material version. Notify for a newly qualifying opportunity, a
   configured meaningful change or a newly crossed reminder threshold. Keep
   eligible, uncertain and ineligible results distinct in any notification;
   follow the user's selection of which states to include. Unknown/changed
   eligibility receives its own explanation rather than an eligible label.
   Repeated unchanged checks produce no notification. A deadline reminder needs
   a verified current-cycle deadline, its date/time zone and a configured
   threshold; do not invent a date or default reminder interval.
   Identify a delivered threshold by item, cycle, verified deadline and threshold,
   so later checks do not repeat the same reminder.
5. **Prepare and deliver once.** Build a concise payload with exact opportunity,
   cycle, eligibility status/reason, material change or reminder basis, verified
   deadline and official link. Deliver only through the user-selected destination
   and authorized mechanism. Configuration alone supplies neither an actual job
   nor authorization to create one. In a simulation, use only the supplied mock
   delivery result and never contact a service.
6. **Commit notification state after delivery.** On explicit successful delivery,
   update last-notified time, material version and any crossed threshold, retaining
   the successful delivery identifier/result. A successful mock delivery advances
   the corresponding mock state. On failed or unconfirmed delivery, keep
   last-notified fields and threshold state unchanged, record the pending/failed
   attempt, and retry the still-relevant notification on the next authorized
   check. Revalidate current evidence before retrying. A prepared payload, attempt
   or scheduler run is not delivery success.
   If a pending notice is no longer applicable, clear that pending attempt with
   its reason while preserving the last successful notification record.

Keep state compact in the configured existing owner: stable item/cycle key,
current source/check result, material comparison, last successful notification and
notified threshold identifiers, plus a pending failure when needed. Do not save
every search hit, source dump or unchanged check as a new note or log entry.

## Outputs

- One-time work: exact opportunities with current-cycle source, eligibility
  classification/reason, preference fit, deadline basis and next action in the current task's requested form or under the recipient's existing reporting policy.
- Watch/deadline work: due notification, quiet unchanged result, disabled result
  or explicit capability gap, with delivery and state updates reported accurately.
- Only requested results and configured compact state are saved in the existing
  owner. No parallel watch dashboard, profile or search archive is created.

## Boundaries

- Do not infer citizenship, degree status, career stage or other eligibility facts.
- Never present stale-cycle details, missing-source checks or an undelivered
  notification as current success.
- Store configured cadence separately from actual scheduling. Create or change a
  recurring job only through a separate user-selected scheduling action.
- Screening does not apply, contact a program, nominate, enroll or submit.
  Follow `me.md` and current authorization for any later external action.

## Handoffs

- Return selection and mentoring tradeoffs to the invoking owner, normally
  PhD Companion; preserve an assigned service's original return point.
- Use phd-career-builder for missing or changed support settings.
- Use research-cv-builder for a chosen opportunity's CV/resume and research-grant-advisor for a selected application, preserving the exact canonical skill and return owner. Consult Research Companion for scientific strategy beyond that service; do not invoke its internal Coordinator directly.

## Checks

- Exact identity and current cycle are verified or explicitly unknown.
- Every eligibility label follows the mandatory criteria and profile evidence.
- Cadence, reminder thresholds and delivery destination came from current settings.
- Same-item/cycle aliases and unchanged checks do not duplicate notifications.
- Failed delivery preserves last-notified state; successful delivery advances it.
- Disabled watches and missing capabilities are never described as active success.
