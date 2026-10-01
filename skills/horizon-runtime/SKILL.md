---
name: horizon-runtime
description: Operate Horizon Business Data and execute runtime Actions and Process runs through Discovery. Use listing, reading, creating, updating, deleting, restoring, relating, querying, exporting, following, acting on Business Instances, starting published Process Definitions, or listing and inspecting Process Instances.
compatibility: Requires Horizon CLI 1.x and Horizon Discovery contract v1.
metadata:
  author: hrz-digital
  version: "1.5.0"
---

# Horizon Runtime

Agent Credential acts only on behalf of Owner User. Apply the [interview and plan gates](../horizon-interview/SKILL.md#planning-gates) before mutation; every Business Data mutation requires explicit confirmation. Resume written plans through `horizon`'s [approved-plan procedure](../horizon/SKILL.md#implement-approved-plan). Runtime-only work needs no Workspace:

```text
Agent authority = Owner User current effective authority ∩ Agent governance
```

Never impersonate another User or evaluate authorization locally.

## Enter

Run `horizon` bootstrap. Continue only with explicit live-valid Connection Profile; pass its label through `--connection` on every Discovery and runtime request.

Completion: compatible CLI and Discovery confirmed, customer Installation explicitly selected, profile status `valid`.

## Resolve operation

1. Open current runtime Discovery entry and select Published Metadata context it exposes for ordinary runtime work. Keep authoring Workspace context out of ordinary runtime requests, except for the Workspace feature validation in `horizon-metadata-authoring`.
2. For Business Data or an Action, select Structure from compact Semantic summaries, then follow detail link. For a direct Process run, follow the Process Definition catalog and detail instead; execution inspection follows **Inspect Process Instances** below without selecting a Structure.
3. Follow authorized runtime affordance for Business Instance CRUD, Relations, Assets, Data Sources, recovery, following, notifications, Actions, or Process starts. Concrete Business Instance affordances determine Action availability; never infer it by scanning definitions.
4. Read linked JSON Schema before constructing request. Use stable codes and runtime-provided links; never infer URL, payload, Relation Edge storage, or task implementation.

Completion: target Business Instance, Process Definition, or Process Instance, current runtime affordance, required context, linked schema, and request links identified.

## Inspect Process Instances

Follow the current execution catalog or a returned execution reference and its linked summary contract. Inspect only what current Discovery exposes. Initiation or delegated read-all grants summary visibility, not launch, editing, cancellation, cleanup, diagnostics, or arbitrary linked Business Data access. Use richer administrative detail only when current Discovery exposes it for this caller. Retrieve linked Business Data through its own current affordance under the actual caller's authority.

Keep the selected Metadata Context when following links and paging. A grant does not expand context visibility; a denied reference is not permission to switch context or infer whether someone else's execution exists. Visibility through recipients or assignees is usable only when current Discovery exposes the persisted relationship.

Refresh the durable list or detail after a missed live notice, and distinguish pending, completed, and failed progress. Live notices are hints rather than durable execution history.

Completion: authorized execution state reported from a fresh read; context and caller authority preserved; unsupported participation and sensitive diagnostics never inferred.

## Execute

1. Fetch current Business Instance state when a mutation targets existing Business Data.
2. For Action, use current runtime availability and concrete execution href. Metadata Action existence does not prove availability. For a process-backed Action, supply only caller-owned inputs from its linked contract; runtime binds the Business Instance and contextual inputs. An Action grant delegates that process's declared effects, not general Business Data editing.
3. Explain material effect and obtain explicit User intent when current affordance declares destructive impact, irreversible behavior, external side effect, or confirmation requirement.
4. Respect concurrency, idempotency, atomicity, and retry declarations.
5. Send request once through Horizon CLI with selected `--connection`. On stale state, refetch and reassess; never silently overwrite. Authentication and token refresh belong CLI transport, not skill.
6. For any Process start, direct or Action-backed, distinguish accepted start from completed work. Follow returned execution state links and report pending or failed work truthfully. When resuming after an ambiguous start response, inspect available execution references before retrying; a new start may duplicate work unless current Discovery promises admission idempotency. Verify confirmed business values and provenance, keeping actual requesting Actor, Process Initiator, and automation Actor distinct; business attribution does not rewrite audit identity. Read the current execution contract rather than assuming accepted work depends on the initiator's continuing session or authority.
7. When Discovery reports a protection blocker or you resume after an active-execution conflict, report that equivalent work is still unfinished and use current Discovery guidance to decide the next step. Inspect only execution references the caller may read. Preserve the intended inputs and context; changing formatting, switching context, or publishing a revision is not a reason to assume overlap is safe. Distinguish a new start from recovery within an admitted Process Instance, and retry only as the current lifecycle contract permits. Terminal settlement may permit the same inputs again; it does not establish a permanent business uniqueness rule.
8. Report Business Data results using Business Instance Display Label and stable instance code; report Process runs using the definition code, returned execution reference, and current state. For changes, follow [Execution and User testing](../horizon-interview/SKILL.md#execution-and-user-testing) for safe manual checks and requested adjustments; do not repeat the operation as a test.

Workspace context is where proposed Metadata gets tested. Current Discovery reports the effective Data Scope, so creation there produces Test Business Instances while Real ones stay read-only, and it publishes the supported Test operations, scope rules, and Data Scope selections: read them instead of learning them by submitting a Real identifier. Follow `horizon-metadata-authoring`'s [test scenarios](../horizon-metadata-authoring/SKILL.md#test-scenarios) for feature validation; its fixture set is confirmed like any other Business Data mutation, and it is the fallback-free path when a Test operation is unsupported or denied.

## Independent Action starts for a selection

1. Confirm the explicitly selected Business Instances and intended effect using the existing plan and mutation gates. Discover each Business Instance's current Action availability and linked input contract separately; availability on one item says nothing about another.
2. Dispatch one call per eligible Business Instance through its runtime link, sequentially or with a small bounded number of concurrent requests. Supply only caller-owned inputs. Associate each accepted Process Instance reference and returned state link with its selected Business Instance.
3. Handle each denial, changed availability, invalid input, or admission conflict independently. Report unavailable items and rejected starts separately and continue eligible starts under the approved intent. Accepted starts remain valid: this sequence has neither an all-or-nothing outcome nor a hidden parent Process Instance.
4. Report accepted starts as started or pending, with individual rejections and any uncertain outcomes. Acceptance is not completion. For requested progress or outcomes, follow each returned state link under current caller authority; retrieve Business Data separately when needed.
5. On a User request to stop dispatch, send no further start requests. In-flight calls may still be accepted and accepted processes continue. Cancelling those processes requires a separate explicit request and current runtime support.
6. When a start response is lost, mark that item's acceptance unknown and avoid automatic retry. Consult current Discovery's admission idempotency declaration: another call may create another Process Instance. Active-execution protection is not a general retry guarantee. Apply **Execute** for inspection and any deliberate retry decision.
7. If the User needs one coordinated process over a collection, use an appropriate available Process Definition with explicit fan-out. Confirm that intent rather than silently replacing independent starts with a collection process; use current Discovery to establish support.

Completion: every selected Business Instance has an accepted reference, a rejection/unavailability reason, an uncertain acceptance, or a not-dispatched result; acceptance and completion remain distinct, and a stop request ends further dispatch.

## Process runs

Start published Process Definitions and track Process Instances through live runtime Discovery.

1. Start only a published definition through its current runtime detail links and linked start schema. Confirm target, inputs, and intended business effect explicitly before starting, as with any Business Data mutation. Invalid inputs create no instance; report the stable reason and stop that attempt.
2. Apply **Execute** above for admission, ambiguous-start retry safety, tracking, and business-value and provenance verification; never report business effects until runtime confirms them.
3. Keep the accepted Data Scope. Run under Published context unless current Discovery explicitly offers another scope. On a scope, target, or launch refusal, report the stable reason and stop; never fall back to other data or guess an alternate route.
4. A missing executable link means no launch authority; report the stable reason and stop.
5. A running instance keeps its original definition snapshot across later Publications; re-reading the definition never rewrites running state.

Completion: launch confirmation obtained, accepted instance tracked through returned state links to runtime-confirmed completion or stable failure, committed values and provenance verified, and refusals reported without fallback or guessed routes.

Completion: current runtime result returned or current stable denial/unavailability reason reported; required confirmation obtained; every request used explicit selected profile; no route, payload, availability, or authorization guessed; no identity impersonated.
