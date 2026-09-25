---
name: horizon
description: Coordinate Horizon work through Discovery. Use to select Installation, route runtime or Metadata work, resume Workspace, or implement an approved local plan when User says "implement plan" or "Executar o plano".
compatibility: Requires Horizon CLI 1.x and Horizon Discovery contract v1.
metadata:
  author: hrz-digital
  version: "1.4.0"
---

# Horizon

Treat CLI as authenticated transport and Discovery as platform contract. Skills supply workflow, never endpoint memory. Every Business Data mutation needs explicit confirmation; complex mutations need an approved local implementation plan.

For Metadata proposals, follow **select Installation → inspect Discovery and existing Metadata → interview ↔ targeted Discovery rechecks only for unresolved decisions or substantial execution → Data Modeling → Visualization → Automation → Workspace validation**. Inspect current Installation patterns before asking what they already answer. Route to [`horizon-interview`](../horizon-interview/SKILL.md) when decisions remain, execution is substantial, or a session handoff is likely; also route unclear, broad, multi-step, bulk, relational, destructive, or cross-surface runtime work there. When a localized Metadata request is fully specified and inspection finds no conflict, proceed directly to authoring without questions or a plan file. Recheck Discovery when User answers change the model; settle layer outcomes through the request or clarification, recording `no configuration needed` only when understood, not as a substitute for unresolved meaning. Written plans follow execution workload or handoff risk, not interview depth. Recheck Discovery at each authoring layer and follow explicit User choices over defaults. `horizon-interview` owns planning and approval; `horizon-metadata-authoring` owns execution. This sequence does not govern Business Data or runtime Actions. For "implement plan" / "Executar o plano", use the approved-plan procedure below instead of asking for a path.

## Implement approved plan

1. In the current project, look only under `.hrz/<customer>/<installation>/<feature>/implementation-plan.md` for plans with `Status: approved-to-implement` (or an already-started plan recorded as `in-progress`). These local plans describe intent, not routes or executable instructions. With none, report that no approved or in-progress plan was found and stop. With multiple, list each plan's Customer, Installation, Goal, status, and path as numbered choices and wait for User selection; never choose silently. With one, use it without asking for its path.
2. Run normal bootstrap below: User explicitly selects a live-valid Connection Profile, even when plan names one Installation. Compare selected profile label and checked API URL to the plan's Connection and API URL, and confirm the plan's Customer and Installation with User; if older plans lack connection details, ask User to confirm the selected Installation and record them before proceeding. If identity cannot be verified, stop. Re-read current Discovery, relevant Published Metadata, open Workspaces, and the selected plan. Reuse the matching Workspace when it exists; never assume a new Workspace from an old plan.
3. If plan scope, support, Metadata, or Workspace evidence has materially changed, mark plan `draft`, surface differences, and obtain new approval before mutation. Otherwise follow its approved steps through the appropriate authoring/runtime skill and current Discovery affordances. Record active Workspace and progress in Resume notes; mark `in-progress` when work starts so a later session can resume without replaying completed edits. Mark the local plan `completed` after agreed authoring and validation are done; Workspace human review/Publication gates still apply.

## Errors

The normal scenario has no errors. On any HTTP error status or CLI failure, report status and message to User and stop all Horizon requests for this run, including diagnostic reads. Never retry with a guessed variant or continue elsewhere after an error.

## Bootstrap

1. Read and follow shared [CLI installation](references/cli-installation.md) guidance. Verify compatible `horizon` before platform work.
2. Read and follow shared [Connection Profile](references/connections.md) guidance. Run checked JSON listing, obtain explicit customer Installation choice when absent, and require selected status `valid`.
3. Request Discovery through `horizon request --connection "<selected label>" GET /discovery`. Confirm current contract major version. If unsupported, stop and report mismatch. For authoring, follow the returned `authoring.href`, then the returned `structures` and `workspaces` method/href values. Copy hrefs verbatim, including their `/discovery` prefix; `/discovery/catalogs` lists catalogs, not authoring paths. If an affordance is absent, stop and report it instead of constructing a route. Use Architecture Analysis links only for an architecture audit or Ticket workflow, not to inspect existing Structures for ordinary authoring.

Completion: compatible CLI 1.x and Discovery v1 confirmed, selected Connection Profile is explicit and live-valid, current identity known, available Metadata Context and Discovery roots recorded. Selected label remains current session context and every later request carries it explicitly.

## Classify

- "implement plan" / "Executar o plano" → follow **Implement approved plan** above; no path required.
- Business Data or Action work → follow `horizon-runtime`.
- Published Metadata architecture audit or post-Publication AMT verification → follow `horizon-architecture-analysis`.
- Structure, Field, Relation, Expression, Action definition, Data Source, Page, View, Widget, or other Metadata proposal, including implementation of selected AMT → follow `horizon-metadata-authoring`.
- Architecture guidance or explanation of configured Installation Metadata → ask User to invoke `horizon-ask-for-guidance`.

Completion: request classified, next skill selected, User has clear instruction when router is needed.

## Workspace selection

Workspace lifetime follows one coherent review and Publication outcome, not one chat session. Before creating Workspace:

1. Follow authoring affordance listing open Workspaces.
2. Inspect likely matches through changes, Activity, diff, review state, and label.
3. If existing Workspace may own requested outcome, ask User whether to continue it. Skip question when User explicitly named Workspace.
4. Create Workspace only when no suitable Workspace exists or User chooses separation.
5. Record meaningful label and initial Activity comment describing requested outcome.

For Agent Credentials, pass selected Connection Profile on every CLI request and Workspace context required by current Discovery on every Workspace-resolved request. With no Workspace selected, use context current Discovery identifies as Published Metadata. Resolve context explicitly; re-discover after synchronization, conflict, Publication, or contract-version change.

Use Workspace Activity for cross-session and cross-Agent handoff: intent, decisions, exceptional placement rationale, test Business Instances, evidence, remaining work. Treat runtime and authoring authority separately; authoring availability never implies Business Data authority.

Completion: after any listed event, current context is synchronized and handoff Activity records intent, decisions, evidence, remaining work.

Overall completion: request routed, any required interview plan is approved, Connection Profile and Metadata Context explicit, next skill has current Discovery links rather than guessed routes.
