# Surface: Mobile Subscription

Purpose: Apply this pack's support and retention-execution work inside the constraints unique to a
native iOS/Android subscription — a store-review-response channel, a cancellation path the developer
does not control, and billing recovery the platform runs itself.

Read when:
- Responding to App Store or Google Play reviews.
- Designing an in-app pause/downgrade/save prompt for a native subscription product.
- A churn or billing question is specific to store-managed in-app purchases (IAP).

Skip when:
- The question is store-listing copy, keywords, or a store-experiment (Custom Product Pages,
  Product Page Optimization) → `marketing`'s `references/app-store-optimization.md` — that file
  cedes app-review-*response* handling to this pack at `app-store-optimization.md:18` but keeps the
  listing itself.
- The question is the churn-save flow's structure, ethics test, or reason taxonomy in general →
  [retention-execution](retention-execution.md) — this file only adds what's different on a native
  store surface.
- The question is uninstall rate as a metric → `product/references/surface-mobile.md:35-36` already
  places it in the metric tree alongside in-app activation/retention; this pack doesn't own the
  metric, only the review-response relationship and the pre-cancel prompt.

Inputs: the product's store listing (for consistency, not to edit it), current app-review response
practice if any, and whether the subscription is sold as a native IAP or a web-based subscription
surfaced in-app.

Produces: a review-response practice folded into the existing support taxonomy, a pre-cancel in-app
prompt that respects store cancellation constraints, and an explicit statement of what this pack does
not control on a native subscription.

## 1. App-review responses are a support workflow, not ASO copy

Marketing owns the store listing; this pack owns the reply to a review once one is posted. Treat an
App Store or Play Store review the way any other support channel is treated — apply
[support-process-design](support-process-design.md)'s taxonomy and escalation discipline to it,
rather than writing review replies as a separate, ad hoc copywriting exercise. A review response is
customer-facing, public, and unresponsive to a discount or pause offer the customer already stopped
paying for — it is closer to an incident comms reply than a sales reply.

## 2. Pause-instead-of-cancel does not fully transfer

On iOS and Android, subscription cancellation is processed through the platform's own subscription-
management surface (Settings on iOS, the Play Store's subscription screen on Android), not inside the
app. A developer cannot intercept that flow with a save offer the way a web checkout portal can — by
the time a user reaches the OS surface to cancel, the app has no further chance to act.

What transfers from [retention-execution](retention-execution.md)'s reason→offer structure is the
**timing**, not the interception: offer a pause, downgrade, or discount *inside the app*, before the
user leaves it to open the platform's cancellation surface — never as a gate that blocks or delays
reaching that surface. The same one-click-reachable ethics test retention-execution.md applies to a
web cancel flow applies here with more force, because the OS itself guarantees the cancellation path
exists regardless of what the app does; an app that tries to obstruct it is fighting a path it cannot
actually close.

## 3. Store-constrained comms

App-review responses, in-app messages, and push notifications are all bounded by store review policy
and the user's OS-level notification permission. There is no channel here that behaves like an owned
email list or a persistent in-app web banner — a win-back or renewal-risk message may never reach a
user who has already decided to leave, because reaching them depends on a permission or a channel the
platform, not this pack, controls.

## 4. Involuntary churn on app stores is the platform's mechanism

Apple and Google each run their own billing-retry and grace-period logic when a native subscription's
renewal payment fails — this is a stricter version of `product`'s dunning ownership
(`marketing/assets/email-compliance-checklist.md:82`), because on a native IAP the platform, not the
product, executes the retry. This pack's job is to know that mechanism exists and design nothing that
duplicates or contradicts it — do not propose a custom dunning cadence for a native subscription; the
store already runs one, on a schedule this pack does not set.

## Validation

- Review responses follow the same taxonomy and escalation discipline as any other support channel.
- Any in-app pause/discount prompt runs before the user reaches the platform's cancellation surface,
  never as a gate on top of it.
- No custom billing-retry or dunning cadence is proposed for a native IAP subscription.

## Failure modes and handoff

- **Writing app-review replies as ASO copy** — route content decisions here; listing copy stays
  `marketing`'s.
- **Assuming an in-app flow can intercept an iOS/Android cancellation the way a web portal can** — it
  cannot; reposition any save offer earlier, before the user leaves the app (§2).
- **Proposing a custom billing-recovery flow for a native subscription** — the store already runs
  one; state that plainly rather than designing around it (§4).
- **Treating uninstall rate as this pack's metric to own** — it is `product`'s
  (`surface-mobile.md:35-36`); this pack owns the relationship response, not the number.
