---
name: horizon-runtime
description: Operate Horizon Business Data and execute runtime Actions and Process runs through Discovery. Use authorized Dashboard inspection, listing, reading, creating, updating, deleting, restoring, relating, querying, exporting, following, acting on Business Instances, starting published Process Definitions, listing and inspecting Process Instances, answering assigned Human Interactions, reassigning pending requests, inspecting response deadlines, or configuring and testing Installation SMTP servers.
compatibility: Requires Horizon CLI 1.x and Horizon Discovery contract v1.
metadata:
  author: hrz-digital
  version: "1.5.1"
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
3. Follow authorized runtime affordance for Business Instance CRUD, Relations, Assets, Data Sources, recovery, following, notifications, Installation email settings, assigned Human Interactions, Actions, or Process starts. Concrete Business Instance affordances determine Action availability; never infer it by scanning definitions.
4. Read linked JSON Schema before constructing request. Use stable codes and runtime-provided links; never infer URL, payload, Relation Edge storage, or task implementation.

Completion: target Business Instance, Process Definition, or Process Instance, current runtime affordance, required context, linked schema, and request links identified.

## Inspect Dashboards

Follow current Discovery to inspect the requested Dashboard or the Installation default. Dashboard read authority is independent from source Structure authority; neither implies the other. If the configured default is unavailable, report that state without silently selecting another Dashboard. Missing and inaccessible definitions must remain indistinguishable in user-facing recovery.

A Dashboard identity does not represent Business Data. Route changes to its Package-owned identity or Installation-default proposal through Metadata authoring and the Workspace lifecycle. Discover each source's current authority when source data is requested; do not invent additional Data Source read grants.

Follow the Dashboard's current Page and source affordances rather than constructing links or selecting the first Page. Query sources independently under current User authority and the requested Metadata context. A refused source is a contained failure: keep unrelated authorized content available, report the refusal honestly, and never retry through a Relation context to widen the source's Access Scope.

Completion: only the requested authorized Dashboard is inspected, unavailable default behavior is reported honestly, and source authority is considered independently.

## Inspect Process Instances

For reassignment, cancellation, schedule review or purge, follow only current executable administrative affordances. If Discovery hides the control or exposes an unavailable reason without a link, explain the limit and hand off to an eligible human. Owner User privilege, launch authority, assignment and summary visibility do not independently establish Agent authority. Publication always remains a human decision under the authoring workflow.

Follow the current execution catalog or a returned execution reference and its linked summary contract. Inspect only what current Discovery exposes. Initiation or delegated read-all grants summary visibility, not launch, editing, cancellation, cleanup, diagnostics, or arbitrary linked Business Data access. Use richer administrative detail only when current Discovery exposes it for this caller. Retrieve linked Business Data through its own current affordance under the actual caller's authority.

Keep the selected Metadata Context when following links and paging. A grant does not expand context visibility; a denied reference is not permission to switch context or infer whether someone else's execution exists. Visibility through recipients or assignees is usable only when current Discovery exposes the persisted relationship.

Refresh the durable list or detail after a missed live notice, and distinguish pending, completed, failed, and skipped progress. For conditional composition, use current Discovery to distinguish a false condition from evaluation failure, inspect authorized skip reasons and dependencies, and report earlier committed effects when later work fails. Recover accepted work through the discovered engine semantics; starting again may repeat previously committed effects. Live notices are hints rather than durable execution history. For query and transformation runs, distinguish an empty selection from unavailable inputs or failed work using the current contract. Inspect authorized persisted results and bounded failures; resume through discovered recovery rather than rerunning completed transformations against changed upstream data. The definition snapshot alone does not freeze referenced Metadata or Business Data.

For mutations consuming transformed results, inspect the authorized committed Business Instance identities and intended Relations through their current affordances. Distinguish operation recovery from a fresh process start when an outcome is uncertain. Check for an earlier committed effect before proposing another start; a later failure does not imply that earlier creation or linking was undone. Report which effects committed, which operation was refused, and what remains to recover. Keep automation provenance separate from initiating business attribution and preserve the selected Data Scope throughout inspection.

For coordinated fan-out, inspect selected membership and per-item progress through current execution detail. Distinguish complete success, partial failure and remaining work; an empty selection is a separate explicit outcome. Do not let a later Data Source change redefine the admitted selection or completion denominator. Preserve completed effects when reporting failure or stopped scheduling, and distinguish unstarted items from already admitted sequences still finishing.

Follow the execution's currently available recovery affordance only within the agreed mutation scope and caller authority. Resume failed or remaining work in the same Process Instance, check that earlier completed operations are retained, and preserve its definition snapshot and Data Scope. A new start is new work and may repeat committed effects. Rediscover progress after recovery; keep configured iteration concurrency distinct from the Installation's overall worker bound, and never infer completion from the recovery request being accepted.

For response waits, inspect the exact selected request set only through authorized detail and use discovered safe response counts for ordinary reporting. Keep generation progress, outstanding responses and final Process Instance completion separate: generated requests can await people after automated work finishes. A received answer, including a negative decision, is not evidence of final completion or approval. Verify the configured completion meaning and continuation from fresh durable state. After reconnecting or restarting, retain the admitted membership and early accepted responses; recover through the existing execution rather than generating another request set. Treat empty, unavailable and partial-generation outcomes according to the current contract, and preserve earlier committed effects in the report.

For cancellation, discover whether the acting identity actually holds the administrative privilege that current Discovery requires; launch authority, delegated read-all oversight and the initiating User's own identity do not grant it, and a refusal is a stable reason rather than a defect to work around. Confirm the intent with the User before stopping queued work or invalidating pending requests, and name the execution being stopped. Cancellation stops future work only: already committed Business Data, delivered notifications and any operation that was already running are not undone, so report stopping and finished separately and never describe a still-running effect as prevented. Treat an accepted cancellation as a state to read back, not proof that every effect ended; the execution may still be stopping while one operation finishes, and only then becomes terminal. After reconnecting or restart, expect cancellation to persist, expect no new operation to start, and expect a stale work claim to settle rather than revive cancelled work. Never start a replacement execution to obtain the effect cancellation deliberately stopped, and never widen equivalent-work exclusion by starting again while cancelled work may still be in flight.

For permanent Test execution cleanup, use current Discovery to distinguish execution-history purge from cancellation and fixture removal. Confirm the exact execution and permanent deletion intent with the User, explaining that reusable Test Business Instances, Relation Edges, ordinary Mutation History, Assets and committed changes remain. Discover the administrative privilege, selected context, current terminal state and work-in-flight refusals before using the linked request schema; launch, initiation and delegated oversight are not cleanup authority. A fresh read does not reserve deletion: honor a race refusal, let existing work settle through its ordinary recovery, then rediscover availability rather than forcing completion or starting replacement work. After success, verify the compact administrative Actor, time, target and outcome audit, and confirm execution and request lists contain no usable stale links. In an authorized test, attempt delayed worker, response and notification work and verify it cannot restore purged history or create later effects; inspect retained fixtures through their own affordances. Report an uncertain deletion by checking durable audit and lists before retrying, and leave fixture deletion to separately confirmed normal operations.

Completion: authorized execution state reported from a fresh read; context and caller authority preserved; unsupported participation and sensitive diagnostics never inferred.

## Notifications and delivery outcomes

Discover the current inbox and delivery affordances before inspecting notifications. Operate only the acting User's inbox in its selected Data Scope and Metadata Context. Read, unread and deletion changes affect that User's item; deletion preserves process history and other recipients' items. Receiving a notification does not itself require login authority or grant access to its referenced Business Data.

Treat live notices as refresh hints. Refetch the authorized durable inbox and unread state after reconnecting, returning focus, or missing a notice; preserve context and let transport handle authentication. Inspect process summaries through discovered persisted participation, and retrieve linked Business Data under current caller authority.

Report committed business effects separately from each recipient's channel outcome. A failed supplementary summary does not reverse business completion. Provider acceptance is evidence of acceptance, not confirmed external delivery; use discovered attempts and recovery semantics, and report ambiguous transport outcomes honestly. Recover within the admitted execution instead of starting another process to resend a message; a distinct Process Instance can intentionally notify the same User again.

Completion: authorized inbox state and independent business/delivery outcomes are freshly verified, context is preserved, and external delivery is claimed only with supporting evidence.

## Configure and test an SMTP server

Treat SMTP setup as Installation System Settings, separate from Business Data and Metadata authoring. Discover current email configuration management, schemas, authority and test availability first. With no authorized affordance, report the limit and hand off to an eligible administrator; an installed skill grants no authority.

1. Establish the intended server, sender, authentication values and test recipient. Reuse the User's settled choices and authorization. A request to configure and test to an explicit recipient authorizes that check; otherwise clarify the recipient and external-send intent before sending. Use a trusted secret-input channel for the password and keep it out of conversational feedback, logs, artifacts and URLs. If none is available, let the User enter the password through the settings UI, then resume verification. Discover supported credential forms rather than inventing environment-variable references.
2. Read saved definitions and preserve their values. Add the new named definition to the intended configuration collection through the current discovered save semantics; never assume an array replacement or resend every existing definition. Update only the agreed definition, preserve omitted secrets according to the contract, and verify the canonical redacted result. A stored-secret indicator is evidence of storage, not a password or proof of successful authentication.
3. Test the saved configuration using its discovered affordance and linked schema, with the agreed recipient and message behavior. Use the Installation-wide saved settings through the currently authorized administrative check regardless of the author’s selected Workspace when Discovery exposes that capability. A configuration check can send real external email even though its purpose is testing; it is not a Workspace Process exercise. Keep Process testing restrictions separate from System Settings administration. Keep unsaved proposals separate from the saved definition being tested. No new Process Definition is needed merely to verify SMTP setup.
4. Give the User feedback on the saved configuration identity, recipient and actual test result without credentials. Distinguish provider acceptance, confirmed inbox receipt and the wider Process notification flow. After a successful send, ask the User to confirm that the recipient received the test email and the configuration is working; wait for that explicit confirmation before saving acknowledgment. Authorization to register and send a test does not establish receipt. The SMTP check verifies the shared email sender and settings; it does not establish Process recipient resolution, queueing or worker completion. On failure or transport uncertainty, stop under the shared error rule and report what was saved and what remains unverified. Check for receipt before proposing another send; an uncertain result can already have sent the email.
5. After the User explicitly confirms successful receipt, persist the receipt acknowledgment using current Discovery semantics. Update only the unchanged tested definition while preserving secrets, verify the canonical saved result, and tell the User whether confirmation was saved. Provider acceptance alone is insufficient. If settings or credentials change, treat earlier confirmation as stale and test the saved configuration again before asking for a new acknowledgment.

Completion: register the agreed definition, test the saved configuration, give feedback and ask for receipt confirmation, then save acknowledgment only after the User confirms success. Preserve other definitions and secrets throughout. If testing is unavailable, receipt is unconfirmed or acknowledgment cannot be saved, report the precise remaining step instead of claiming completion.

## Assigned Human Interactions

Discover the acting User's assigned requests and read the selected request's current response contract before proposing an answer. Preserve the selected Metadata Context and Data Scope. Treat assignment as authority over that exact request; inspect contextual Business Data only through its separately authorized affordances. A request reference or notification does not authorize acting for another User.

Confirm the User's intended response and submit only the declared response values through the current affordance. Let authenticated transport determine the acting identity. Keep the responsible User separate from Agent Credential provenance, and verify the accepted response and actual responder from a fresh read. If Login Access or assignment is unavailable, report that condition instead of proposing a general grant or substituting another identity.

After an uncertain submission, read the durable request before retrying and follow the current repeat/stale-response contract. Preserve an already accepted response and its audit; reassess a stale rejection rather than sending a different answer as recovery. A contextual status change is a separate Business Data mutation and does not substitute for answering. Request creation, accepted response and subsequent process progress are separate facts; discover explicit continuation support before claiming that an answer resumed work.

### Reassignment and deadline recovery

An unavailable responsible User is not evidence that a request has resolved. Discover administrative reassignment support before offering that recovery. When Discovery withholds an executable affordance, report its reason and hand off to an eligible human; a notification, assignment, initiation or read-all summary never grants administrative control. Otherwise, confirm the intended responsibility change, and verify replacement eligibility in the execution's current context. Follow only the authorized affordance, then verify responsibility and audit through fresh permitted reads. Keep former-assignee access and linked Business Data authority separate; a request reference or historical assignment is not continuing permission. On denial, report the condition rather than substituting an identity or proposing a broad grant.

Treat overdue work as waiting for durable settlement, not as an answer inferred from a clock. Distinguish a User's accepted response from a configured non-response outcome, and distinguish request resolution from an execution wait's outcome. Route a new or changed silence policy through Metadata authoring: agree its business meaning and discover supported timing and outcomes before configuring it. Missing input is never evidence of approval. After restart, a race or an ambiguous intervention, inspect current durable state and preserve the authoritative winner; recovering uncertainty does not justify reopening or replacing completed requests.

Completion: the intended response, responsibility change or explicit non-response outcome is durably verified through authorized state and audit; responder/provenance, linked Business Data authority and process progress remain separately verified.

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

For assignment or recipient testing, follow [Test User fixtures](../horizon-metadata-authoring/SKILL.md#test-user-fixtures). Use current Discovery eligibility rather than inferring authority or deliverability from a User's testing designation.

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

### Scheduled starts

Inspect scheduled start intent through current Discovery under the caller's administrative authority and Data Scope. Read intended time, definition, parameters and the latest start outcome; treat an accepted Process Instance as a separate execution whose state and business result require following its returned links. Verify System initiation and schedule/occurrence provenance from authorized detail rather than borrowing the schedule author's identity.

A blocked start remains a reported refusal. Discover its current reason and the protected business grouping; preserve that boundary instead of launching equivalent work manually or changing inputs to bypass it. An overdue occurrence requiring review is unresolved intent, not permission to replay stale work. Explain the intended business effect and follow only currently available recovery controls after the User confirms that intent. If those controls are absent, report the limitation and leave the occurrence visible.

For uncertain acceptance or a worker restart, inspect durable occurrence and execution state before considering another start. Distinguish recovery of admitted work from a deliberate additional execution, and discover identity/republication semantics before treating an edited definition as a repeat request. Report intended time separately from actual admission; make no real-time dispatch promise.

For recurring schedules, read the saved timezone and next local occurrence from current Discovery. Inspect older unresolved occurrences separately from newer planned work; determine their relationship from the live policy before claiming that one delays another. On an edit, verify retained history and existing accepted snapshots alongside the replacement plan. On restart or concurrent retry, use durable occurrence identities and execution references to establish whether advancement preserved work without duplicates. Discover missed-run handling rather than inventing a catch-up queue or treating recurrence as permission to replay overdue intent.

For missed and blocked work, inspect the discovered lateness tolerance and the schedule's explicit recovery policy before recommending action. Distinguish ordinary dispatch delay from missed intent, and explain whether the business choice retains work for review, catches up only the latest missed intent, or deliberately omits missed work. Preserve each intended time and report actual admission separately. An older unresolved occurrence is not evidence that newer eligible work must wait.

Before an administrative Run now or Skip, confirm the selected occurrence and intended effect with the User, then follow the current authorized control. Re-read its durable outcome and administrative Actor audit: a Run refusal can leave work blocked because inputs, current start eligibility, Data Scope or active-execution protection changed. For a race or uncertain response, inspect the committed winner rather than repeating the command blindly. An accepted occurrence whose Process Instance later fails remains accepted start intent; follow that execution's recovery evidence instead of launching it through a start-problem control. Delegated summary oversight alone supplies no administrative recovery authority.

Completion: intended time and current start outcome are reported, any accepted execution is tracked through its returned links, provenance is verified, and blocked, overdue or uncertain work remains explicit without unauthorized replay.

### Event-triggered process inspection

Discover current trigger outcomes and authorized execution links before explaining why a Business Data change did or did not start work. Keep the committed event, admission outcome and eventual business completion separate. Match the outcome to the original Mutation and Actor, and verify the responsible User initiator only where one actually exists; System-caused changes never justify inventing a User.

For delayed processing or restart, inspect the original transition evidence and persisted definition snapshot available through the current contract. A later Business Instance value is not evidence of what the earlier event contained. Refresh durable outcomes after uncertain transport or missed live notices before proposing repetition, and track any accepted Process Instance through completion or its stable failure. Inspect unqualified, blocked and stopped outcomes as distinct results; a causal safeguard stop preserves earlier effects and calls for a business-policy review, not blind replay. Keep notification channel retries separate from repeating business work.

In a Workspace, prepare an authorized committed Test transition and use the discovered trigger exercise explicitly. Verify matching and retry outcomes in that Workspace while preserving shared fixtures and fixed Test scope. An exercise is not a subscription, and a shared Test mutation is not evidence that another Workspace automatically ran its draft.

Completion: original-event provenance, durable admission and execution outcome are reported separately, uncertain or stopped work remains explicit, and any Workspace verification uses current explicit Test affordances.

### Workspace process exercise

Exercise a Workspace draft against Test fixtures before Publication, using the same engine that runs published work — never a mock, a clone, or a copied data set.

1. Discover which definitions the Workspace makes effective and which Users are currently eligible test participants; prepare fixtures and a valid initiator from that evidence rather than assumptions. For assignment or recipient testing, follow [Test User fixtures](../horizon-metadata-authoring/SKILL.md#test-user-fixtures).
2. Start the effective definition explicitly in the Workspace and keep the fixed Test scope for the whole run: queries, mutations, fan-out items, retries, and resumes all stay inside it. A refusal means stop, never a silent switch to published definitions or Real data. Discover each Test effect separately: supported in-platform notifications can be exercised, while unavailable external effects remain explicitly suppressed or untested. Testing designation alone promises no channel support.
3. When business logic should see someone other than the configurator, select a currently eligible Test User as the logical initiator. Audit still names the actual requester; the selection grants no login, borrows no authority, and cannot reach Real data.
4. Deliver only to currently eligible test participants through contained in-app means and recheck eligibility at delivery time. Requests that need a human answer additionally require current authentication, Login Access, response eligibility, and Workspace access; plain notification recipients need none of that.
5. Leave automatic schedules and event subscriptions off while exercising. Use explicit runs or discovered trigger exercises against committed Test transitions; neither subscribes the Workspace globally. Fixtures outlive the run for reuse.
6. Report real failures as failures: a failed item, a refused recipient, or an ineligible participant is evidence, never a silent success. Restart mid-wait and retry failed items to confirm durable progress and continued containment before calling the exercise complete.

Completion: effective definition and eligible participants discovered; explicit Test run tracked to completion or stable failure; Real data, audit, and other inboxes untouched; provenance distinguishes requester from logical initiator; refusals and failures reported as such.

Completion: current runtime result returned or current stable denial/unavailability reason reported; required confirmation obtained; every request used explicit selected profile; no route, payload, availability, or authorization guessed; no identity impersonated.
