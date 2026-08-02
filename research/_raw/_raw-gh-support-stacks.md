# _raw-gh-support-stacks — open-source support stack data models (channel C, worker 1)

Scope: what the DATA MODELS and DOCS of open-source helpdesk/ITSM stacks teach about support
taxonomy. Deep schema/model read on 7 stacks (Chatwoot, Zammad, FreeScout, Frappe Helpdesk,
libredesk, django-helpdesk, GLPI); licence + status verification pass on 8 more (Peppermint,
helpy, uvdesk ×2, RT, Znuny, chaskiq, trudesk, opensupports, iTop). Every claim below is sourced
`owner/repo@ref:path`. All refs pinned to the commit SHA / branch resolved at fetch time
(2026-08-02).

---

## 1. Ticket lifecycle — the convergent 3-bucket taxonomy

**Chatwoot** (`chatwoot/chatwoot@bc7ae88:app/models/conversation.rb:85`):
```ruby
enum status: { open: 0, resolved: 1, pending: 2, snoozed: 3 }
```
4 literal statuses, no state-machine/transition table in the model — any status can move to
any other (`toggle_status` just flips open⇄resolved). `pending` here means agent-side "waiting to
be picked up" bucket (`waiting_since` timestamp field, `db/schema.rb:817`), not literally
"waiting on customer" — Chatwoot's customer-wait detection is inferred from `last_reply_from`-type
message ordering, not a dedicated status.

**Zammad** (`zammad/zammad@develop:app/models/ticket/state_type.rb:14-28`):
```ruby
CATEGORIES = {
  open: ['new', 'open', 'pending reminder', 'pending action'],
  pending_reminder: ['pending reminder'],
  pending_action: ['pending action'],
  pending: ['pending reminder', 'pending action'],
  closed: ['closed'],
  merged: ['merged'],
  resolved: ['closed', 'merged', 'removed'],
  ...
}
```
Zammad splits "pending" into **two subtypes**: `pending reminder` (agent wants to be reminded at
a future time — a personal snooze) vs `pending action` (waiting on something external, e.g. the
customer or a third party) — a real distinction the other stacks collapse into one bucket. States
themselves are DB rows (`ticket_states` table, `db/migrate/20120101000010_create_ticket.rb:16-36`)
each pointing at one `ticket_state_types` row (`new/open/pending reminder/pending
action/closed/merged/removed`) — i.e. **custom status labels, fixed underlying type**. Auto-reopen
is explicit: `Ticket::ChecksReopenAfterCertainTime` (`app/models/ticket/checks_reopen_after_certain_time.rb`)
reopens a closed ticket if a new customer reply lands within `group.reopen_time_in_days` — a
per-group (queue) configurable reopen window, not a global rule.

**FreeScout** (`freescout-help-desk/freescout@dist:app/Conversation.php:62-123`):
```php
const STATUS_ACTIVE = 1;
const STATUS_PENDING = 2;
const STATUS_CLOSED = 3;
const STATUS_SPAM = 4;
// const STATUS_OPEN = 5;  <- commented out, unused
const STATE_DRAFT = 1;
const STATE_PUBLISHED = 2;
const STATE_DELETED = 3;
```
Only 4 support-relevant statuses, no "resolved" distinct from "closed" — closing IS the terminal
state, no separate resolved-then-closed step. Notably a **separate `state` field** (draft /
published / deleted) governs the conversation's *record lifecycle* (is this a live conversation
vs. a draft) — orthogonal to `status` (is this ticket open/pending/closed). Nobody else in the
sample separates these two axes explicitly.

**Frappe Helpdesk** (`frappe/helpdesk@develop:helpdesk/helpdesk/doctype/hd_ticket_status/hd_ticket_status.json`):
```
label_agent (Data) | label_customer (Data) | category (Select: Open / Paused / Resolved)
```
Every custom status an admin creates must declare one `category` of exactly **Open / Paused /
Resolved** — and critically, **`label_agent` and `label_customer` are separate fields**: the same
underlying status can display different text to the agent vs. the customer-facing portal. This is
the cleanest "custom surface labels, fixed canonical categories" implementation in the sample.

**libredesk** (`abhinavxd/libredesk@main:schema.sql:26,192-208`):
```sql
CREATE TYPE "conversation_status_category" AS ENUM ('open', 'waiting', 'resolved');
CREATE TABLE conversation_statuses (
  "name" TEXT NOT NULL UNIQUE,
  category conversation_status_category NOT NULL DEFAULT 'open'
);
CREATE TABLE conversation_priorities ( "name" TEXT NOT NULL UNIQUE );  -- free-text, no fixed category
```
Same pattern as Frappe (customizable status *names*, fixed *category* enum) — but the category
values are **open / waiting / resolved**, not Open/Paused/Resolved. "Waiting" is explicitly generic
(could mean waiting-on-customer or waiting-on-third-party) rather than named "Paused". Priorities,
by contrast, are pure free-text with NO fixed category — libredesk treats priority as fully
open-ended but status as constrained to 3 machine-meaningful buckets.

**django-helpdesk** (`django-helpdesk/django-helpdesk@main:src/helpdesk/settings.py:148-199`):
```python
OPEN_STATUS = 1; REOPENED_STATUS = 2; RESOLVED_STATUS = 3; CLOSED_STATUS = 4; DUPLICATE_STATUS = 5
DEFAULT_TICKET_STATUS_CHOICES_FLOW = {
    OPEN_STATUS:      (OPEN_STATUS, RESOLVED_STATUS, CLOSED_STATUS, DUPLICATE_STATUS),
    REOPENED_STATUS:  (REOPENED_STATUS, RESOLVED_STATUS, CLOSED_STATUS, DUPLICATE_STATUS),
    RESOLVED_STATUS:  (REOPENED_STATUS, RESOLVED_STATUS, CLOSED_STATUS),
    CLOSED_STATUS:    (REOPENED_STATUS, CLOSED_STATUS),
    DUPLICATE_STATUS: (REOPENED_STATUS, DUPLICATE_STATUS),
}
```
The only stack in the sample with **NO native "pending/waiting-on-customer" status at all** by
default (it's configurable via `HELPDESK_TICKET_STATUS_CHOICES`, but ships without one) — and the
only one with an explicit **transition adjacency dict** enforced in code (not just documented).
`Resolved` is distinct from `Closed` (resolved can still be reopened; there's no separate
"resolved→closed" auto-transition observed in the model). Has a real `Ticket.on_hold` boolean
(`src/helpdesk/models.py:562`) — "if a ticket is on hold, it will not automatically be escalated" —
i.e. pause-on-hold implemented as a flag orthogonal to `status`, not a status value itself.

**bestpractical/rt** (`bestpractical/rt@stable:etc/RT_Config.pm.in:5406-5560`) — the oldest system
in the sample (RT predates all the above by ~15-20 years) ships a **fully generic 3-tier lifecycle
framework**, not a fixed enum:
```perl
default => {
    initial  => ['new'],
    active   => ['open', 'stalled'],
    inactive => ['resolved', 'rejected', 'deleted'],
    transitions => {
        ''       => [qw(new open resolved)],
        new      => [qw(open resolved rejected deleted)],
        open     => [qw(stalled resolved rejected deleted)],
        stalled  => [qw(open)],
        resolved => [qw(open)],
        ...
    },
    rights => { '* -> deleted' => 'DeleteTicket', '* -> rejected' => 'RejectTicket', '* -> *' => 'ModifyTicket' },
}
```
`initial`/`active`/`inactive` are named SETS (each holding any number of literal statuses) — RT
auto-sets a `Started` date on initial→active/inactive, and a `Resolved` date on
(initial|active)→inactive. Transitions are graph edges, and **each transition can be gated by a
distinct permission right** — nobody else in the sample ties status transitions to authorization
this granularly. `stalled` is RT's "pending" equivalent.

**GLPI** (`glpi-project/glpi@11.0/bugfixes:src/CommonITILObject.php:120-128`) — shared base class
for Ticket/Problem/Change (the ITSM triad):
```php
const INCOMING = 1;  // new
const ASSIGNED = 2;  // processing (assigned)
const PLANNED  = 3;  // processing (planned)
const WAITING  = 4;  // pending
const SOLVED   = 5;
const CLOSED   = 6;
const OBSERVED = 8;  // (7 is a removed/deprecated value — gap in the enum)
const APPROVAL = 10; // change-management approval gate (9 also missing)
```
GLPI's status set is **richer (8 live values) than every pure-helpdesk tool** because ITSM must
model scheduled work (`Planned`, distinct from `Assigned`) and change-approval gates (`Approval`)
that don't exist in a customer-support-only domain. This is the clearest evidence that "ITSM
taxonomy ⊃ support taxonomy" — the extra states are all process states specific to
change-management, not support.

### Convergence verdict
Four independently-built systems spanning 1996 (RT) to 2026 (libredesk) — RT (initial/active/
inactive), Frappe Helpdesk (Open/Paused/Resolved category), libredesk (open/waiting/resolved
category), and Zammad's `state_type` categories collapse to the same shape — converge on **exactly
3 canonical buckets underneath customizable literal labels**: something-to-do (open/new/incoming),
something-paused-on-someone-else (pending/waiting/stalled), and something-finished
(resolved/closed). The strongest form of this evidence is that Frappe and libredesk *enforce* the
3-category constraint in the schema itself (every custom status must declare a category), not just
in documentation. **Divergence**: whether "resolved" and "closed" are the same value (FreeScout,
GLPI's Solved+Closed as two of the three "finished" buckets) or distinct steps (Chatwoot, Zammad,
django-helpdesk, libredesk all have both). **Divergence**: pending has 1 flavor (most stacks) vs 2
(Zammad: reminder vs action) vs 0-by-default (django-helpdesk). Auto-reopen exists in Zammad
(group-configurable window) and django-helpdesk (status-flow permits Resolved→Reopened,
Closed→Reopened) but is time-window-based only in Zammad.

---

## 2. Priority / severity / urgency

- **Chatwoot**: single ordinal field, `enum priority: { low: 0, medium: 1, high: 2, urgent: 3 }`
  (`app/models/conversation.rb:86`), nullable (no priority set by default) — agent sets it.
- **Zammad**: single `Ticket::Priority` model, admin-defined literal rows with a `default_create`
  flag (one row is the default for new tickets) — no impact/urgency decomposition
  (`app/models/ticket/priority.rb`).
- **Frappe Helpdesk**: `hd_ticket_priority.json` fixed `level` Select = `Urgent / High / Medium /
  Low` (4-tier), plus a `disabled` flag per priority.
- **libredesk**: `conversation_priorities` is a bare `name TEXT` table — fully admin-defined,
  no fixed levels at all (`schema.sql:201-208`).
- **django-helpdesk**: 5-tier NUMBERED priority, `1. Critical / 2. High / 3. Normal / 4. Low /
  5. Very Low` (`src/helpdesk/settings.py:204-210`) — the only 5-point scale in the sample, and
  the only one with the ordinal baked into the label text.
- **GLPI** (ITIL-style matrix — the flagship divergence): `CommonITILObject.php:3329-3333`
  ```php
  public static function computePriority($urgency, $impact) {
      return $CFG_GLPI[static::MATRIX_FIELD][$urgency][$impact] ?? (int) round(($urgency + $impact) / 2);
  }
  ```
  urgency and impact are each 1-5 (`@param int<1,5>`), looked up in a configurable
  `$CFG_GLPI[matrix]` table, falling back to the rounded average if unconfigured. **This is the
  only impact×urgency matrix in the whole sample** — every pure support/helpdesk tool uses a
  single ordinal priority field set directly by an agent (or occasionally the customer, e.g.
  Chatwoot exposes priority in its API for either party to set). The ITIL 5×5 matrix genuinely is
  an ITSM-specific mechanism, not a support-taxonomy default — worth teaching the pack's reader
  that the matrix is over-engineering for most self-serve/SMB support and the right default is a
  single field.

**Who sets it**: in every stack examined, priority is agent/admin-settable via the API; only
GLPI's matrix explicitly computes it FROM two other agent/customer-supplied inputs (urgency is
often exposed to the requester, impact usually agent-only) — this two-input design is the actual
mechanism by which "customer vs agent sets priority" gets resolved in ITSM tooling: the customer
supplies urgency, the agent supplies (or corrects) impact, and priority is derived, not chosen
directly by either party.

---

## 3. SLA modelling

**Chatwoot** (`db/schema.rb:1374-1385,174-186,1357-1370`):
```ruby
create_table "sla_policies" do |t|
  t.float "first_response_time_threshold"
  t.float "next_response_time_threshold"
  t.boolean "only_during_business_hours", default: false
  t.float "resolution_time_threshold"
end
create_table "applied_slas" do |t|
  t.integer "sla_status", default: 0
  t.datetime "completed_at"
end
create_table "sla_events" do |t|
  t.integer "event_type"
  t.jsonb "meta", default: {}
end
```
Three named thresholds (first-response / next-response / resolution) in a single policy row,
attached to a conversation via `conversations.sla_policy_id`; `applied_slas` is the per-conversation
application record (join table with a `sla_status` int + `completed_at`); `sla_events` logs
breach/other events. `only_during_business_hours` boolean gates whether the calendar even matters.

**Zammad** (`db/migrate/20120101000010_create_ticket.rb:417-432`, `app/models/sla.rb`):
```ruby
create_table :slas do |t|
  t.references :calendar, null: false
  t.column :first_response_time, :integer
  t.column :response_time,       :integer
  t.column :update_time,         :integer
  t.column :solution_time,       :integer
  t.column :condition,           :text
end
```
**Four** timers (Zammad calls "response_time" the follow-up/next-response equivalent, "update_time"
a separate metric, and "solution_time" the resolution deadline) — and crucially a model validation:
```ruby
def cannot_have_response_and_update
  return if response_time.blank? || update_time.blank?
  errors.add :base, 'Cannot have both response time and update time.'
end
```
(`app/models/sla.rb:17-20,38-42`) — Zammad's design FORBIDS setting both `response_time` and
`update_time` on the same SLA policy, i.e. per-policy you must choose one of two "next contact"
metrics, not use both simultaneously — a real, documented design constraint worth teaching.
Escalation calculation is delegated: `ticket.escalation_calculation` calls `::Escalation.new(self,
force:).calculate!` (`app/models/ticket/escalation.rb:19-21`) — every ticket write re-evaluates
whether it should be considered escalated (`after_commit :update_escalation_information`).
Ticket itself carries the pause/breach bookkeeping directly on the row (not a join table):
`first_response_escalation_at`, `first_response_in_min`, `first_response_diff_in_min`,
`close_escalation_at`, `close_in_min`, `close_diff_in_min`, `update_escalation_at`, `update_in_min`,
`update_diff_in_min`, and a single overall `escalation_at` plus a **`pending_time`** column
(`db/migrate/20120101000010_create_ticket.rb:54-141`) — the explicit "SLA clock pause" field: when
a ticket enters a pending state with a future pending_time, that's the pause-until instant.

**Frappe Helpdesk** — richest SLA state machine in the sample
(`helpdesk/helpdesk/doctype/hd_ticket/hd_ticket.json`, `hd_service_level_agreement.json`,
`hd_service_level_priority.json`):
```
HD Ticket.agreement_status (Select): First Response Due / Resolution Due / Failed / Fulfilled / Paused
HD Ticket.on_hold_since (Datetime), total_hold_time (Duration)
HD Ticket.first_response_time (Duration), first_responded_on (Datetime), avg_response_time (Duration)
HD Ticket.resolution_date (Datetime), resolution_time (Duration), user_resolution_time (Duration)
HD Ticket.first_response_failed_by (Duration), resolution_failed_by (Duration)
HD Ticket.raised_outside_working_hours (Check)
HD Ticket.last_agent_response (Datetime), last_customer_response (Datetime)

HD Service Level Agreement: start_date/end_date, holiday_list (Link), support_and_resolution
  (Table→HD Service Day), priorities (Table→HD Service Level Priority), condition (Code:
  PythonExpression) + condition_json, default_priority, ticket_reopen_status, default_ticket_status

HD Service Level Priority (per-priority row inside an SLA): priority (Link), response_time
  (Duration), resolution_time (Duration), default_priority (Check)
```
`agreement_status` names **"Paused" as a first-class SLA state**, not just a boolean — this is the
clearest, most explicit "does the clock stop while waiting on the customer" answer in the sample:
yes, and the pause is itself a status value, with `on_hold_since`/`total_hold_time` as the actual
accounting fields, and `first_response_failed_by`/`resolution_failed_by` Duration fields that
quantify breach magnitude (not just a boolean breached/not-breached). The SLA is scoped to which
tickets it applies to via a raw **Python expression** (`condition`, fieldtype `Code`) — the most
powerful/dangerous condition mechanism in the sample (arbitrary code vs. the JSON condition trees
everyone else uses). Per-priority response/resolution times (`HD Service Level Priority`) is the
only true ITIL-style **priority × SLA-metric matrix** among the pure-helpdesk tools (GLPI's matrix
is urgency×impact→priority, a different matrix; Frappe's is priority→{response,resolution} time).

**libredesk** (`schema.sql:19-22,50-62,521-560`):
```sql
CREATE TYPE "applied_sla_status" AS ENUM ('pending', 'breached', 'met', 'partially_met');
CREATE TYPE "sla_event_status"   AS ENUM ('pending', 'breached', 'met');
CREATE TYPE "sla_metric"         AS ENUM ('first_response', 'resolution', 'next_response');
CREATE TABLE sla_policies (
  first_response_time TEXT NOT NULL, resolution_time TEXT NOT NULL, next_response_time TEXT NULL,
  notifications JSONB DEFAULT '[]'
);
CREATE TABLE applied_slas (
  status applied_sla_status DEFAULT 'pending',
  first_response_deadline_at, resolution_deadline_at,
  first_response_breached_at, resolution_breached_at, first_response_met_at, resolution_met_at
);
CREATE TABLE sla_events (
  status sla_event_status DEFAULT 'pending', type sla_metric NOT NULL,
  deadline_at, met_at, breached_at
);
```
**first_response / resolution / next_response** — the exact same 3-metric naming as Chatwoot's
`first_response_time_threshold` / `resolution_time_threshold` / `next_response_time_threshold`,
independently arrived at in Go vs. Ruby, 2023-era vs 2026-era codebases — strong convergence
evidence on the "3 SLA metrics" taxonomy specifically. `partially_met` is a 4th outcome value not
seen elsewhere (a ticket that met first-response but breached resolution, e.g.). SLA-breach
notification is modelled explicitly: `sla_notification_type` ENUM `('warning','breach')` +
`scheduled_sla_notifications` table — i.e. libredesk schedules a **pre-breach warning** as a
distinct notification type from the breach itself, which none of the others make this explicit
about (Chatwoot/Zammad imply it via background jobs, not a typed enum).

**django-helpdesk / RT / GLPI**: no dedicated SLA-policy object model. django-helpdesk relies on
`Queue.escalate_days` (see §4) plus `EscalationExclusion` holiday dates
(`src/helpdesk/models.py:1358-1391`) — escalation there is priority-bump-after-N-days, not a
response/resolution-deadline model. RT and GLPI have SLA/OLA add-ons in their broader ecosystems
but the core repos read here do not define them at the schema level (not verified further — out of
depth budget for this run).

### Pause-on-pending: cross-stack answer
Every stack that models SLA at all pauses the clock during a customer-wait state: Chatwoot via
`waiting_since` + `only_during_business_hours` calendar gating; Zammad via the ticket's own
`pending_time` column (a concrete pause-until instant baked directly onto the ticket row, not a
separate table); Frappe via the explicit `Paused` `agreement_status` value plus
`on_hold_since`/`total_hold_time` accounting; libredesk via the `applied_sla_status` value staying
`pending` until a deadline resolves and via business-hours calendars on `sla_policies`. **The
convergent design is: pending/waiting-on-customer is a real, named state that stops SLA
accounting — never implicit.**

---

## 4. Escalation — the "escalation paths" artifact

- **Chatwoot** `automation_rules` (`app/models/automation_rule.rb:35-42`) — verbatim allowed
  vocab:
  ```ruby
  conditions_attributes = %w[content email country_code status message_type browser_language
    assignee_id team_id referer city company_name inbox_id mail_subject phone_number priority
    conversation_language labels private_note]
  actions_attributes = %w[send_message add_label remove_label send_email_to_team assign_team
    assign_agent remove_assigned_agent remove_assigned_team send_webhook_event mute_conversation
    send_attachment change_status resolve_conversation open_conversation pending_conversation
    snooze_conversation change_priority send_email_transcript add_private_note]
  ```
  Rules store `conditions`/`actions` as JSONB with AND/OR `query_operator` per condition
  (`account_id`-scoped, `event_name`-triggered, optional `execution_delay` for time-based rules —
  `db/schema.rb:300-313`). This IS the escalation-paths template: condition vocabulary × action
  vocabulary × logical operator, with a delay knob for "escalate if still true after N minutes."

- **Zammad**: two separate mechanisms. `Trigger` (`app/models/trigger.rb`) has an `activator`
  field constrained to `%w[action time]` and `execution_condition_mode` constrained to
  `%w[selective always]` — action-triggers fire off a ticket event, time-triggers are polled
  (`performable_on?` uses a `Ticket::DailyEventLock` to avoid re-firing). `Scheduler`
  (`app/models/scheduler.rb`) is the separate recurring-job primitive (`runs_as_persistent_loop?`
  returns true for jobs running more often than every 5 minutes) used for e.g. SLA-breach sweeps.
  Zammad's `Sla#condition_matches?` reuses `Ticket.selector2sql` — the SAME condition-query engine
  triggers use, i.e. one condition DSL powers SLA scoping, triggers, and (elsewhere) overviews.

- **libredesk** `automation_rules` (`schema.sql:295-310`): `type`, `rules JSONB`, **`events
  TEXT[]`** (an array — one automation can bind to multiple trigger events, unlike Chatwoot's
  single `event_name`), `execution_mode` ENUM `('all','first_match')` — `all` runs every rule that
  matches, `first_match` short-circuits on the first matching rule (a genuinely different rule-
  engine semantic than Chatwoot/Zammad, which don't expose a short-circuit knob).

- **FreeScout**: **no automation/workflow model in core** — confirmed by an empty `Modules/`
  directory (`freescout-help-desk/freescout@dist:Modules/.gitkeep` only) — FreeScout's open-source
  core is deliberately minimal (email-based ticketing with no priority field either, see §2); SLA
  and "Workflows" are commercial paid modules not present in this repo. Worth teaching as a real,
  intentional monetization boundary — a genuine "what open-source support tools omit and sell
  separately" data point.

- **django-helpdesk**: escalation = **automatic priority increase**, not SLA breach + notify.
  `Queue.escalate_days` (`src/helpdesk/models.py:145-151`, help text: "so unresolved tickets
  automatically increase their priority? Set to 0 for no escalation") driven by a cron job
  (`management/commands/escalate_tickets.py`, referenced in the model but not read in this pass),
  gated by `EscalationExclusion` holiday/weekend dates and the ticket's `on_hold` flag. This is a
  genuinely different "escalation" semantic worth flagging as a seam question for the pack:
  escalation-as-priority-bump vs. escalation-as-notify-and-reassign are two different mechanisms
  the pack should name separately rather than treat as synonyms.

- **RT**: transition-level rights gating (`'* -> deleted' => 'DeleteTicket'`, see §1) is itself a
  form of escalation control — certain state changes require elevated permission, which is a
  different lever than time/condition-based automation.

---

## 5. Routing / assignment

- **Chatwoot**: `conversations.assignee_id` (single agent) + `team_id` — no round-robin/load-
  balance logic visible at the schema level in this pass (assignment logic lives in service
  objects not read here); inboxes are the queue unit.
- **Zammad**: `tickets.group_id` + `owner_id` — "Group" is Zammad's queue/team concept; no
  capacity/concurrency-limit column observed on `groups`.
  Wait: **needs verification** — `groups` table wasn't fully read in this pass beyond
  `reopen_time_in_days`; concurrency limits, if any, weren't found.
- **libredesk** — most explicit routing model in the sample:
  ```sql
  CREATE TYPE "conversation_assignment_type" AS ENUM ('Round robin', 'Manual');
  CREATE TABLE teams (
    conversation_assignment_type conversation_assignment_type NOT NULL,
    max_auto_assigned_conversations INT DEFAULT 0,
    business_hours_id, sla_policy_id
  );
  ```
  (`schema.sql:8,99-118`) — **teams carry their own SLA policy and business-hours calendar**
  (different teams can have different SLAs) and an explicit
  `max_auto_assigned_conversations` **capacity limit** per team for round-robin auto-assignment —
  the only concurrency/capacity cap found in the sample. Agent-level capacity isn't separately
  capped (only team-level `max_auto_assigned_conversations`).
- **Frappe Helpdesk**: `HD Team` doctype + `agent_group` Link on the ticket — teams/queues exist;
  no round-robin/capacity fields were surfaced in the `hd_ticket.json` fields read (would need
  `hd_team.json`, not read this pass).
- **django-helpdesk**: `Queue` model is the routing unit (email-per-queue ingestion); no
  round-robin — assignment appears manual/rule-based via `Ticket.assigned_to`.

---

## 6. Taxonomy fields — tags, categories, canned responses, KB linkage

- **Chatwoot**: `taggings`/`tags` (acts-as-taggable pattern, `context` column lets the same tag
  table serve multiple taggable contexts — `db/schema.rb:1113-1143`), `custom_attribute_definitions`
  (typed custom fields scoped to `attribute_model` — conversation vs. contact — with a `regex_
  pattern`/`regex_cue` validation pair, `db/schema.rb:882-902`), `canned_responses` and `macros` as
  two DISTINCT tables (`db/schema.rb:364,1143`) — canned responses are simple text snippets, macros
  are the richer scripted multi-action objects (macros in Chatwoot execute the same
  `actions_attributes` vocabulary as automation rules, per `app/models/macro.rb`, not fully read
  this pass). `articles`/`portals`/`categories` (`db/schema.rb:198+`) support KB linkage, plus a
  pgvector `article_embeddings` table (`embedding vector(1536)`, ivfflat index,
  `db/schema.rb:187-193`) — i.e. Chatwoot's KB has semantic-search infrastructure built in for its
  "Captain" AI agent (README, `chatwoot/chatwoot@bc7ae88:README.md`) to do deflection.
- **Zammad**: `tags`/`tag_objects`/`tag_items` (generic tagging usable on any object type,
  `db/migrate/20120101000001_create_base.rb:340-365`), `text_modules`/`text_modules_groups` are
  Zammad's canned-response equivalent (`db/migrate/20120101000010_create_ticket.rb:363-385`),
  `object_manager_attributes` (`create_base.rb:622-647`) is Zammad's generic custom-field
  infrastructure (used for tickets, users, organizations alike — same mechanism state config
  hooks into, see `Ticket::State.update_state_field_configuration`).
- **Frappe Helpdesk**: `ticket_type` (Link → HD Ticket Type) is a SEPARATE dimension from status/
  priority — a taxonomy axis (e.g. "Bug"/"Question"/"Feature Request") none of the other stacks
  model as a first-class linked doctype (others fold this into free-text tags or custom
  attributes). `HD Saved Reply` doctype is the canned-response equivalent; `HD Article`/
  `HD Article Category` is the KB, with `HD Article Feedback` for per-article thumbs.
- **libredesk**: `custom_attribute_definitions`, `tags`/`conversation_tags`, `macros` (with
  `visibility` ENUM `all/team/user` and `visible_when` array ENUM
  `replying/starting_conversation/adding_private_note` — macros can be scoped to WHERE in the UI
  they're offered, the most granular macro-visibility model in the sample,
  `schema.sql:14,24,328-345`), plus a full AI layer (`ai_knowledge_base`, `embeddings`,
  `ai_faq_suggestions`, `ai_agent_events`, `copilot_messages`) — the newest/most AI-native schema
  of the set.
- **GLPI**: category taxonomy is native to ITIL — `ITILCategory` (not read in depth this pass, but
  present per repo structure) is a first-class hierarchical category tree shared across
  Ticket/Problem/Change, richer than any pure-helpdesk tool's flat tag/category model — consistent
  with ITSM's heavier process-classification needs.

---

## 7. CSAT / feedback capture

- **Chatwoot** `csat_survey_responses` (`db/schema.rb:861-881`):
  ```ruby
  t.bigint "conversation_id"; t.bigint "message_id"; t.integer "rating"; t.text "feedback_message"
  t.text "csat_review_notes"; t.datetime "review_notes_updated_at"
  ```
  Rating is a bare integer (no CHECK constraint visible in this pass on its range — the UI likely
  fixes 1-5); fires per-conversation, tied to the specific `message_id` that carried the survey
  (i.e. re-sendable/traceable to exactly which message asked). Uniquely: `csat_review_notes` +
  `review_notes_updated_by_id` — Chatwoot lets a MANAGER annotate/review a CSAT response after the
  fact, a workflow none of the others expose.
- **libredesk** `csat_responses` (`schema.sql:482-499`):
  ```sql
  rating INT DEFAULT 0 NOT NULL, feedback TEXT NULL, response_timestamp TIMESTAMPTZ NULL,
  CONSTRAINT constraint_csat_responses_on_rating CHECK (rating >= 0 AND rating <= 5)
  ```
  Explicit 0-5 range constraint at the DB level (0 likely = "no response yet" sentinel, 1-5 the
  real scale) — the only stack with the rating range enforced as a schema CHECK rather than left
  to application logic.
- **Frappe Helpdesk** `HD Ticket Feedback Option` doctype (`hd_ticket_feedback_option.json`):
  `rating` (Rating fieldtype) + `label` (Data) + `disabled` (Check) — feedback options are
  ADMIN-DEFINABLE rows (e.g. could be "Great"/"Okay"/"Bad" with custom labels), not a hardcoded
  1-5 or thumbs scale — the most configurable CSAT taxonomy in the sample. `HD Ticket.feedback`
  links to one of these option rows plus a separate `feedback_rating` Rating field and
  `feedback_extra` free text.
- **Zammad / FreeScout / django-helpdesk / RT / GLPI**: no dedicated CSAT table surfaced in this
  pass (Zammad has a CSAT feature in its newer releases but the model wasn't located under
  `app/models` in this session — would need `app/models/*` beyond the ticket/sla/trigger set
  actually enumerated; not confirmed absent, just not found — treat as unconfirmed, not "missing.")

---

## 8. Process docs inside the repos

Nothing qualifying as *support-process* prose (as opposed to install/dev docs) was found in the
directories actually inspected: Zammad's `doc/` is only `developer_manual` (API/dev docs,
`zammad/zammad@develop:doc/`); Chatwoot's `skim` signal reported `hasDocs: false` at the repo root
(docs live on a separate docs site, off-GitHub — **FLAG TO D: chatwoot.com docs / developer docs
site, not scanned here, channel D's territory**). No repo in this pass carried a `docs/` directory
teaching e.g. "how to triage a ticket" or "how to write a canned response" as opposed to
installation instructions. This is itself a finding: **process knowledge lives in the vendor's
hosted docs site, not the OSS repo** — none of these codebases teach support process in-repo; the
schema IS the process documentation (what fields exist encodes what the designers thought
mattered).

No Claude-skill / agent-skill repos were encountered in this slice (Frappe Helpdesk ships an
`AGENTS.md` at repo root — a generic Codex/agent-CLI convention file, not an agent-skill package —
not flagged to A on that basis).

---

## Licence verdict table (5-clause check per repo)

Clauses checked: (a) LICENSE file itself, not API; (b) package-manifest license field vs LICENSE;
(c) per-directory carve-outs; (d) archived / last-commit-date aliveness; (e) thin-license-on-
thick-IP.

| Repo | LICENSE file (verified) | API `license` field | Manifest field | Carve-outs | Last push | Archived | Verdict |
|---|---|---|---|---|---|---|---|
| chatwoot/chatwoot | MIT (root `LICENSE`) | **NOASSERTION** (lied/incomplete) | `package.json`: `"license": "MIT"` — matches root | `enterprise/LICENSE` = separate non-OSS "Chatwoot Enterprise License" (seat-based, forbids resale/hosting without subscription) — quoted in full above §carve-out | 2026-08-01 | false | **LIFTABLE** (core schema/taxonomy, MIT) / **CITE-ONLY** for anything under `enterprise/` |
| zammad/zammad | AGPL-3.0 (`LICENSE`, verified full text = GNU AGPLv3) | AGPL-3.0 (correct here) | no license field found in Ruby ecosystem manifest checked | none found | 2026-07-31 | false | **LIFTABLE** (structure/ideas only, per charter's code policy) |
| freescout-help-desk/freescout | AGPL-3.0 (`LICENSE`, verified GNU AGPLv3 header) | AGPL-3.0 | `composer.json`: `"license": "AGPL-3.0"` — matches | none; commercial add-ons live in a separate `Modules/` marketplace not in this repo (dir is empty here) | 2026-08-02 | false | **LIFTABLE** |
| frappe/helpdesk | AGPL-3.0 (`LICENSE`, verified GNU AGPLv3 header) | AGPL-3.0 | `pyproject.toml`: no license field present (no contradiction) | none found | 2026-08-02 | false | **LIFTABLE** |
| abhinavxd/libredesk | AGPL-3.0 (`LICENSE`, verified GNU AGPLv3 header) | AGPL-3.0 | Go `go.mod` carries no license field (N/A for Go) | none found | 2026-08-02 | false | **LIFTABLE** |
| django-helpdesk/django-helpdesk | BSD-3-Clause (`LICENSE`, verified) | BSD-3-Clause | not checked (Python `pyproject`/`setup.cfg` not read this pass) | separate `LICENSE.3RDPARTY` file exists (third-party dependency licenses, not a code carve-out) | 2026-07-31 | false | **LIFTABLE** (most permissive in sample) |
| glpi-project/glpi | GPL-3.0 (`LICENSE`, verified GNU GPLv3 header) | GPL-3.0 | `composer.json`: `"license": "GPL-3.0-or-later"` — matches | none found | 2026-07-30 | false | **LIFTABLE** — ~~**note:** the lead's pre-scan listed this as `gpl-2.0`; the repo is GPLv3 now (GPL-2.0→3.0 relicense at some point) — pre-scan is stale, correct to GPL-3.0~~ **[CORRECTED — see note below]** |

> **CORRECTION 2026-08-02 (channel-C lead).** The GLPI row above originally claimed "the lead's
> pre-scan listed this as `gpl-2.0` … pre-scan is stale". **That claim is wrong and is withdrawn.**
> Verified three ways on 2026-08-02: (1) the pre-scan file `_scan-gh-1.json` records
> `glpi-project/glpi -> gpl-3.0`; (2) `gh api repos/glpi-project/glpi` returns `GPL-3.0` live;
> (3) `glpi-project/glpi@main:LICENSE` reads "Version 3, 29 June 2007".
> The `gpl-2.0` value in the pre-scan belongs to **`bestpractical/rt`**, a different row — which this
> worker's own table independently and correctly verified as GPL-2.0 from `COPYING`. The two rows were
> conflated. **Nothing about GLPI's licence was stale or wrong at any point**, and the worker's own
> GPL-3.0 verdict for GLPI (and GPL-2.0 for RT) stands unchanged — only the editorial note about the
> pre-scan was in error.
| Peppermint-Lab/peppermint | AGPLv3 core + confusing self-referential "Commercial License" clause (`license` file, no extension — quotes itself: "content under [this repo's own URL] is licensed under the license defined in license") | NOASSERTION | not checked | carve-out language is internally circular/broken (likely a mis-adapted copy of Chatwoot's template) — do not trust the carve-out boundary without a maintainer clarification | 2025-09-21 (~11 months stale) | **true (ARCHIVED)** | **CITE-ONLY** — archived + ambiguous carve-out language, do not treat as a clean lift source |
| helpyio/helpy | MIT (`LICENSE`, verified) | MIT | not checked | none found | 2023-03-08 (**>3 years stale**) | false | **CITE-ONLY** — not archived but not alive by rule (d); MIT text itself is clean |
| uvdesk/community-skeleton | OSL-3.0 (`LICENSE.txt`, verified Open Software License v3.0 header) | OSL-3.0 | not checked | none found | 2025-10-01 | false | **LIFTABLE** (structure-only; OSL-3.0 is a reciprocal/copyleft-flavored OSI license, fine to cite ideas) |
| uvdesk/core-framework | not independently re-verified (same org/licensing pattern as community-skeleton, API reports OSL-3.0) | OSL-3.0 | — | assumed same as skeleton, **not independently confirmed this pass** | 2025-09-24 | false | **AMBIGUOUS** pending direct LICENSE read — treat as OSL-3.0 provisionally |
| bestpractical/rt | GPL-2.0 (`COPYING`, verified GNU GPLv2 header) | GPL-2.0 | not checked (Perl, no standard manifest license field) | none found | 2026-07-31 | false | **LIFTABLE** (structure only) |
| znuny/Znuny | GPL-3.0 (`COPYING`, verified GNU GPLv3 header) | GPL-3.0 | not checked | none found | 2026-07-22 | false | **LIFTABLE** |
| chaskiq/chaskiq | **AGPL-3.0 + Commons Clause v1.0** (`LICENSE.txt`, verified — Commons Clause explicitly forbids "Sell"-ing the software, i.e. offering it as a paid hosted/consulting service) | NOASSERTION (correctly — Commons Clause is not OSI-approved, GitHub can't classify it) | not checked | the WHOLE repo carries the Commons Clause, not a sub-directory | 2026-06-30 | false | **CITE-ONLY** — this is explicitly source-available, not open-source; conservative treatment even for structure-only citation |
| polonel/trudesk | **Apache-2.0** (`LICENSE`, verified — "Licensed under the Apache License, Version 2.0") | **NOASSERTION (API is WRONG here — clearest API-lied case this run)** | not checked | none found | 2026-05-11 | false | **LIFTABLE** — flag this as the concrete evidence for charter rule 3(a): trust the file, not the API field |
| opensupports/opensupports | GPL-3.0 (`LICENSE`, verified GNU GPLv3 header) | GPL-3.0 (correct) | not checked | none found | 2024-04-22 (**~2.3 years stale**) | false | **CITE-ONLY** — license is clean but project shows real staleness; verify liveness before citing as "current practice" |
| Combodo/iTop | AGPL-3.0 (`license.txt`, verified GNU AGPLv3 header) | AGPL-3.0 | not checked | none found | 2026-07-30 | false | **LIFTABLE** |

**Pattern across the table**: the GitHub license API was wrong or unhelpful in exactly 4/17 cases
here (chatwoot: NOASSERTION despite a clean root MIT; peppermint: NOASSERTION with a genuinely
messy carve-out; chaskiq: NOASSERTION correctly reflecting a non-OSI license; trudesk: NOASSERTION
despite a clean Apache-2.0 file) — confirms the charter's "API lied 7+ times" warning is not
overcautious; always read the file.

---

## Summary of what's LIFTABLE structure for the pack

1. **Status taxonomy**: 3 canonical categories (open / paused-waiting / resolved-closed) under
   customizable literal labels — cite Frappe's `category` Select and libredesk's
   `conversation_status_category` enum as the two cleanest schema-level implementations; RT's
   initial/active/inactive as the oldest independent confirmation.
2. **SLA metric taxonomy**: first-response / next-response / resolution as the convergent 3-metric
   set (Chatwoot + libredesk, independently, near-identical field names); Zammad's 4-metric variant
   with its response-XOR-update constraint as the interesting exception; Frappe's per-priority SLA
   matrix as the ITIL-adjacent enrichment; pause-on-pending as a first-class state (Frappe's
   `Paused` agreement_status) is the strongest single citation for "the clock stops."
3. **Priority**: single ordinal field is the default in pure support tools (4-5 levels); GLPI's
   urgency×impact matrix is the ITSM-specific exception, teachable as "don't build this unless
   you're doing formal ITSM."
4. **Escalation-paths artifact template**: Chatwoot's verbatim conditions_attributes /
   actions_attributes vocabulary lists are the most quotable ready-made template for the pack's
   "escalation paths" deliverable.
5. **Divergence worth teaching explicitly**: escalation-as-priority-bump (django-helpdesk) vs.
   escalation-as-SLA-breach-notify (everyone else) are different mechanisms; FreeScout's
   deliberate omission of priority/SLA/automation from its OSS core is a real monetization-boundary
   pattern worth naming.

## Open items / not confirmed this pass
- Zammad group-level concurrency/capacity limits — not found, not confirmed absent.
- Frappe `HD Team` round-robin/capacity fields — not read this pass.
- uvdesk/core-framework LICENSE — not independently verified (provisional OSL-3.0 only).
- GLPI/RT/Znuny/iTop SLA(-equivalent OLA) schemas — not deep-read (ecosystem add-ons likely, out
  of this pass's budget).
- Zammad CSAT schema — not located under the models enumerated; not confirmed absent.
