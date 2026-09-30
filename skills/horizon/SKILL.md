---
name: horizon
description: Coordinate Horizon work through Discovery. Use to select Installation, route runtime or Metadata work, resume Workspace, or execute an agreed summary or saved plan when User says "implement plan" or "Executar o plano".
compatibility: Requires Horizon CLI 1.x and Horizon Discovery contract v1.
metadata:
  author: hrz-digital
  version: "1.4.0"
---

# Horizon

Treat CLI as authenticated transport and Discovery as platform contract. Skills supply workflow, never endpoint memory. Every Business Data mutation needs explicit confirmation; planning and persistence follow the gates below.

Select Installation and inspect Discovery and relevant Metadata before applying the [interview and plan gates](../horizon-interview/SKILL.md#planning-gates). `horizon-interview` owns clarification, plan summaries, and the exceptional plan-file gate; the selected execution skill owns implementation, validation, and User-requested adjustments. For "implement plan" / "Executar o plano", use the procedure below instead of starting another interview or asking for a path.

## Implement approved plan

For an agreed summary in the current session, treat User's execution request as approval of that summary and continue through the appropriate execution skill without looking for a file. Required target, decisions, and mutation effects must already be explicit; clarify any ambiguity first. If several summaries could match, ask which one. Use the file procedure below only for an explicitly requested saved plan or when no current-session summary is available.

1. In the current project, look only under `.hrz/<customer>/<installation>/<feature>/implementation-plan.md` for plans with `Status: approved-to-implement` (or an already-started plan recorded as `in-progress`). These local plans describe intent, not routes or executable instructions. With none, report that no approved or in-progress plan was found and stop. With multiple, list each plan's Customer, Installation, Goal, status, and path as numbered choices and wait for User selection; never choose silently. With one, use it without asking for its path.
2. Read the selected plan and follow the [plan lifecycle](../horizon-interview/references/implementation-plan.md#lifecycle). Run normal bootstrap below. Compare the explicitly selected live-valid profile label and checked API URL to the plan's Connection and API URL; confirm Customer and Installation with User. If an older plan lacks connection details, record them after confirmation. Stop if target identity cannot be verified.
3. Re-read current Discovery and evidence relevant to the remaining steps. For Metadata work, verify the recorded Workspace's identity, scope, progress, and review state; reuse it when User approved or previously selected it through this plan. Otherwise use normal Workspace selection below. Runtime-only work does not require a Workspace or authoring access.
4. Compare current evidence with approved scope and recorded progress, using the lifecycle's drift rule. Execute only remaining approved steps through the appropriate authoring/runtime skill and current Discovery. Update Resume notes and lifecycle state as work proceeds; never replay completed mutations. Plan approval does not authorize Workspace acknowledgement, human review approval, or Publication.

## Errors

The normal scenario has no errors. On any HTTP error status or CLI failure, report status and message to User and stop all Horizon requests for this run, including diagnostic reads. Never retry with a guessed variant or continue elsewhere after an error.

## Bootstrap

1. Read and follow shared [CLI installation](references/cli-installation.md) guidance. Verify compatible `horizon` before platform work.
2. Read and follow shared [Connection Profile](references/connections.md) guidance. Run checked JSON listing, obtain explicit customer Installation choice when absent, and require selected status `valid`.
3. Request Discovery through `horizon request --connection "<selected label>" GET /discovery`. Confirm current contract major version. If unsupported, stop and report mismatch. For authoring, follow the returned `authoring.href`, then the returned `structures` and `workspaces` method/href values. Copy hrefs verbatim, including their `/discovery` prefix; `/discovery/catalogs` lists catalogs, not authoring paths. If an affordance is absent, stop and report it instead of constructing a route. Use Architecture Analysis links only for an architecture audit or Ticket workflow, not to inspect existing Structures for ordinary authoring.

Completion: compatible CLI 1.x and Discovery v1 confirmed, selected Connection Profile is explicit and live-valid, current identity known, available Metadata Context and Discovery roots recorded. Selected label remains current session context and every later request carries it explicitly.

## Classify

- "implement plan" / "Executar o plano" → follow **Implement approved plan** above; no path required.
- Business Data, Action, or Process run work → follow `horizon-runtime`.
- Published Metadata architecture audit or post-Publication AMT verification → follow `horizon-architecture-analysis`.
- Structure, Field, Relation, Expression, Action definition, Data Source, Page, View, Widget, or other Metadata proposal, including implementation of selected AMT → follow `horizon-metadata-authoring`.
- Architecture guidance or explanation of configured Installation Metadata → ask User to invoke `horizon-ask-for-guidance`.

Completion: request classified, next skill selected, User has clear instruction when router is needed.

## Workspace selection

Workspace lifetime follows one coherent review and Publication outcome, not one chat session. Before creating Workspace:

1. Follow authoring affordance listing open Workspaces.
2. Inspect likely matches through changes, Activity, diff, review state, and label.
3. If an existing Workspace may own the outcome, ask whether to continue it unless User named it or approved/previously selected it through the current plan. Verify that choice against current evidence.
4. Create Workspace only when no suitable Workspace exists or User chooses separation. Before creating its label, follow [Localized text and codes](references/authoring-conventions.md).
5. Record meaningful label and initial Activity comment describing requested outcome.

For Agent Credentials, pass selected Connection Profile on every CLI request and Workspace context required by current Discovery on every Workspace-resolved request. With no Workspace selected, use context current Discovery identifies as Published Metadata. Resolve context explicitly; re-discover after synchronization, conflict, Publication, or contract-version change.

Use Workspace Activity for cross-session and cross-Agent handoff: intent, decisions, exceptional placement rationale, test Business Instances, evidence, remaining work. Treat runtime and authoring authority separately; authoring availability never implies Business Data authority.

Completion: after any listed event, current context is synchronized and handoff Activity records intent, decisions, evidence, remaining work.

Overall completion: request routed, decisions and required approvals are settled, Connection Profile and Metadata Context explicit, and next skill has current Discovery links rather than guessed routes; a local file is not a routine prerequisite.
