import React from "react";
import {
  AbsoluteFill,
  Easing,
  interpolate,
  Sequence,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";
import { themes, MONO, SANS, type ThemeName, type Theme } from "./theme";

// Hero: the through-line of `success` — a gate BEFORE a playbook, then a faceted router, then the
// flagship's honesty layer. Success asks first whether a distinct customer-success function is even
// worth building yet (the Existence Gate, tested against one attributed sentence: does the
// customer's growth change what they pay you), naming a sibling pack for the gap when the answer is
// "not yet." Once the gate opens, one primary job of ten composes with at most one base surface of
// three, plus an additive agentic overlay for when a model runs support or retention with no human
// reviewing each instance. The flagship, health-and-risk-signals, shows a circulated 93-94% churn-
// prediction accuracy headline collapsing into two honest numbers once checked: an 85.5% majority-
// class baseline that just guesses nobody churns, and a clean, independently reproduced ceiling of
// 78-81% accuracy — because five named CS vendors, the entire open-source ecosystem, and even the
// most transparent public CS program in the research disclose zero accuracy figures against real
// outcomes. The Observability Question separates a contractual subscription (churn observed on a
// known day) from a non-contractual, usage-based product (churn never observed at all) — a
// distinction the CS canon never draws. The handoff carries a gate verdict, every claim's evidence
// grade, and a named seam to marketing, growth, and ai, while success ships no production code.
// ~48s, loops (opens/closes empty).
//
// Pacing model (reader-first): every scene animates its content IN, then HOLDS fully still for a
// reading beat (~2.3-3.6s) before the container fades OUT. The fade-out begins at dur - hold, so each
// scene's dur = content-in-end + reading-hold + fade. Never let the next scene start before this one
// has been readable at rest.
//
// Scene map (30fps):
//   S1 gate          0-220        the existence gate: does the customer's growth change what they pay
//   S2 router        220-560      the faceted router: one job of 10 x one surface of 3 + agentic overlay
//   S3 flagship      560-900      THE centerpiece: a headline number, checked — 93-94% collapses to two honest figures
//   S4 observability 900-1180     the Observability Question: contractual vs non-contractual churn
//   S5 handoff       1180-1420    gate verdict, graded claims, named seam — and what this cannot prove

const EASE = Easing.bezier(0.16, 1, 0.3, 1);

function envelope(frame: number, dur: number, hold = 26) {
  const opIn = interpolate(frame, [0, hold], [0, 1], { extrapolateLeft: "clamp", extrapolateRight: "clamp", easing: EASE });
  const opOut = interpolate(frame, [dur - hold, dur], [1, 0], { extrapolateLeft: "clamp", extrapolateRight: "clamp", easing: EASE });
  const y = interpolate(frame, [0, hold], [14, 0], { extrapolateLeft: "clamp", extrapolateRight: "clamp", easing: EASE });
  return { opacity: Math.min(opIn, opOut), y };
}

const step = (frame: number, a: number, b: number, ease = false) =>
  interpolate(frame, [a, b], [0, 1], { extrapolateLeft: "clamp", extrapolateRight: "clamp", easing: ease ? EASE : undefined });

const SceneTitle: React.FC<{ t: Theme; kicker: string; title: string; accent?: string }> = ({ t, kicker, title, accent }) => (
  <div style={{ textAlign: "center", marginBottom: 30 }}>
    <div style={{ fontFamily: SANS, textTransform: "uppercase", letterSpacing: "0.18em", fontWeight: 600, fontSize: 17, color: accent ?? t.accent, marginBottom: 12 }}>
      {kicker}
    </div>
    <div style={{ fontFamily: MONO, fontSize: 38, color: t.ink, letterSpacing: "-0.02em" }}>{title}</div>
  </div>
);

// -- S1 . the existence gate ----------------------------------------------------------
const ClaimLine: React.FC<{ t: Theme; text: string; frame: number; from: number; color?: string }> = ({ t, text, frame, from, color }) => {
  const chars = Math.floor(interpolate(frame, [from, from + 50], [0, text.length], { extrapolateLeft: "clamp", extrapolateRight: "clamp" }));
  const typed = text.slice(0, chars);
  const caretOn = Math.floor(frame / 8) % 2 === 0 && chars < text.length && frame > from;
  const op = step(frame, from - 4, from + 6);
  return (
    <div style={{ opacity: op, color: color ?? t.ink }}>
      {typed}
      <span style={{ opacity: caretOn ? 1 : 0, color: t.accent }}>▋</span>
    </div>
  );
};

const VerdictRow: React.FC<{ t: Theme; label: string; body: string; tag: string; color: string; appear: number }> = ({ t, label, body, tag, color, appear }) => (
  <div style={{ opacity: appear, translate: `0 ${interpolate(appear, [0, 1], [10, 0])}px`, display: "grid", gridTemplateColumns: "150px 1fr 150px", gap: 16, alignItems: "center", padding: "10px 0", borderTop: `1px solid ${t.line}` }}>
    <div style={{ fontFamily: MONO, fontSize: 14, fontWeight: 700, color }}>{label}</div>
    <div style={{ fontFamily: SANS, fontSize: 13, color: t.ink, lineHeight: 1.4 }}>{body}</div>
    <div style={{ fontFamily: MONO, fontSize: 11.5, color: t.muted, textAlign: "right" }}>{tag}</div>
  </div>
);

const SceneGate: React.FC<{ t: Theme; dur: number }> = ({ t, dur }) => {
  const frame = useCurrentFrame();
  const { opacity, y } = envelope(frame, dur, 22);
  const r1 = step(frame, 108, 130, true);
  const r2 = step(frame, 124, 146, true);
  const r3 = step(frame, 140, 162, true);

  return (
    <AbsoluteFill style={{ alignItems: "center", justifyContent: "center", opacity }}>
      <div style={{ translate: `0 ${y}px`, width: 1000 }}>
        <div style={{ fontFamily: SANS, textTransform: "uppercase", letterSpacing: "0.18em", fontWeight: 600, fontSize: 16, color: t.muted, marginBottom: 20, textAlign: "center" }}>
          before a single health score or playbook exists
        </div>
        <div style={{ background: t.codeBg, border: `1px solid ${t.line}`, borderRadius: 12, padding: "26px 32px", fontFamily: MONO, fontSize: 19, lineHeight: 1.8, color: t.ink, textAlign: "center" }}>
          <ClaimLine t={t} text="the existence gate" frame={frame} from={8} color={t.accent} />
          <ClaimLine t={t} text="does the customer's growth change what they pay you?" frame={frame} from={64} />
        </div>
        <div style={{ marginTop: 22, background: t.panel, border: `1px solid ${t.line}`, borderRadius: 12, padding: "6px 20px" }}>
          <VerdictRow t={t} label="yes" body="seat expansion, usage-based pricing, revenue share — a bigger customer is a better customer" tag="applies" color={t.good} appear={r1} />
          <VerdictRow t={t} label="flat-rate" body="the customer's success doesn't change the bill — optional until it visibly earns its cost" tag="lighter-weight" color={t.amber} appear={r2} />
          <VerdictRow t={t} label="unsettled" body='"not yet" is a real verdict — named, with whichever sibling covers the gap meanwhile' tag="not-yet" color={t.bad} appear={r3} />
        </div>
      </div>
    </AbsoluteFill>
  );
};

// -- S2 . the faceted router -----------------------------------------------------------
const Chip: React.FC<{ t: Theme; label: string; on?: boolean; star?: boolean; dim?: boolean; appear: number }> = ({ t, label, on, star, dim, appear }) => {
  const bg = star || on ? t.accent : dim ? "transparent" : t.codeBg;
  const border = dim ? t.dim : star || on ? t.accent : t.line;
  const color = star || on ? t.accentInk : dim ? t.dim : t.muted;
  return (
    <div style={{ opacity: appear, scale: String(interpolate(appear, [0, 1], [0.9, 1])), fontFamily: MONO, fontSize: 11.5, padding: "6px 10px", borderRadius: 8, background: bg, border: `1px solid ${border}`, color, fontWeight: star || on || dim ? 700 : 400, whiteSpace: "nowrap" }}>
      {label}
    </div>
  );
};

const RLane: React.FC<{ t: Theme; label: string; sub: string; children: React.ReactNode; appear: number }> = ({ t, label, sub, children, appear }) => (
  <div style={{ opacity: appear, display: "grid", gridTemplateColumns: "170px 1fr", gap: 18, alignItems: "center", marginTop: 15 }}>
    <div style={{ textAlign: "right" }}>
      <div style={{ fontFamily: SANS, textTransform: "uppercase", letterSpacing: "0.09em", fontWeight: 700, fontSize: 12.5, color: t.muted }}>{label}</div>
      <div style={{ fontFamily: MONO, fontSize: 10.5, color: t.glyph, marginTop: 2 }}>{sub}</div>
    </div>
    <div style={{ display: "flex", flexWrap: "wrap", gap: 7 }}>{children}</div>
  </div>
);

const JOBS = [
  "when-success-applies",
  "onboarding-and-adoption",
  "education-and-knowledge-base",
  "support-process-design",
  "ai-support-policy",
  "health-and-risk-signals ⭐",
  "voice-of-customer",
  "retention-execution",
  "renewals-and-expansion",
  "incident-and-account-comms",
];
const SURFACES = ["self-serve solo", "B2B high-touch", "mobile subscription"];

const SceneRoute: React.FC<{ t: Theme; dur: number }> = ({ t, dur }) => {
  const frame = useCurrentFrame();
  const { opacity, y } = envelope(frame, dur, 24);
  const l1 = step(frame, 20, 40);
  const l2 = step(frame, 150, 170);
  const l3 = step(frame, 194, 214);
  const compose = step(frame, 244, 268, true);
  const readset = step(frame, 266, 290, true);

  return (
    <AbsoluteFill style={{ alignItems: "center", justifyContent: "center", opacity }}>
      <div style={{ translate: `0 ${y}px`, width: 1060 }}>
        <SceneTitle t={t} kicker="SKILL.md is a router, not a script" title="one job × one surface + an agentic overlay" />
        <RLane t={t} label="① primary job" sub="exactly one, of 10" appear={l1}>
          {JOBS.map((j, i) => {
            const ap = step(frame, 40 + i * 10, 58 + i * 10, true);
            return <Chip key={j} t={t} label={j} star={j.includes("⭐")} appear={ap} />;
          })}
        </RLane>
        <RLane t={t} label="② base surface" sub="at most one, of 3" appear={l2}>
          {SURFACES.map((s, i) => {
            const ap = step(frame, 170 + i * 10, 190 + i * 10, true);
            return <Chip key={s} t={t} label={s} on={i === 0} appear={ap} />;
          })}
          <div style={{ opacity: step(frame, 200, 218, true), fontFamily: MONO, fontSize: 11, color: t.muted }}>
            self-serve solo assumed when unstated — and said out loud
          </div>
        </RLane>
        <RLane t={t} label="③ additive overlay" sub="stacks on, never instead" appear={l3}>
          <Chip t={t} label="overlay-agentic" dim appear={step(frame, 214, 234, true)} />
          <div style={{ opacity: step(frame, 228, 246, true), fontFamily: MONO, fontSize: 11, color: t.muted, border: `1px dashed ${t.line}`, borderRadius: 8, padding: "6px 11px" }}>
            a model decides and acts on support, health, or retention — no per-instance review
          </div>
        </RLane>
        <div style={{ marginTop: 24, display: "flex", alignItems: "center", gap: 12, opacity: compose }}>
          <div style={{ flex: 1, height: 1, background: t.line }} />
          <div style={{ fontFamily: MONO, fontSize: 12.5, color: t.muted }}>compose →</div>
          <div style={{ flex: 1, height: 1, background: t.line }} />
        </div>
        <div style={{ marginTop: 16, display: "flex", justifyContent: "center", gap: 10, opacity: readset, alignItems: "center" }}>
          <div style={{ fontFamily: MONO, fontSize: 13, color: t.accent, background: t.codeBg, border: `1px solid ${t.accent}`, borderRadius: 8, padding: "7px 14px" }}>when-success-applies.md</div>
          <div style={{ fontFamily: MONO, fontSize: 13, color: t.accent, background: t.codeBg, border: `1px solid ${t.accent}`, borderRadius: 8, padding: "7px 14px" }}>surface-selfserve-solo.md</div>
          <div style={{ fontFamily: MONO, fontSize: 12, color: t.muted }}><b style={{ color: t.ink }}>2 of 15</b> loaded · read fully</div>
        </div>
      </div>
    </AbsoluteFill>
  );
};

// -- S3 . the flagship: a headline number, checked -------------------------------------
const SceneFlagship: React.FC<{ t: Theme; dur: number }> = ({ t, dur }) => {
  const frame = useCurrentFrame();
  const { opacity, y } = envelope(frame, dur, 24);
  const headline = step(frame, 10, 40, true);
  const strike = step(frame, 66, 92, true);
  const label1 = step(frame, 78, 100, true);
  const row1 = step(frame, 118, 144, true);
  const row2 = step(frame, 152, 178, true);
  const caption = step(frame, 244, 272, true);

  return (
    <AbsoluteFill style={{ alignItems: "center", justifyContent: "center", opacity }}>
      <div style={{ translate: `0 ${y}px`, display: "flex", flexDirection: "column", alignItems: "center", width: 1040 }}>
        <SceneTitle t={t} kicker="health-and-risk-signals · the flagship" title="a headline number, checked" />
        <div style={{ position: "relative", opacity: headline, marginBottom: 14 }}>
          <div style={{ fontFamily: MONO, fontSize: 64, fontWeight: 700, color: t.bad, letterSpacing: "-0.02em" }}>93–94% accuracy</div>
          <div
            style={{
              position: "absolute",
              left: 0,
              top: "50%",
              height: 4,
              background: t.bad,
              borderRadius: 2,
              width: `${strike * 100}%`,
              transform: "translateY(-50%)",
            }}
          />
        </div>
        <div style={{ opacity: label1, fontFamily: SANS, fontSize: 13.5, color: t.muted, marginBottom: 22, textAlign: "center" }}>
          the number that circulates for churn-prediction accuracy — traced to resampling before the train/test split, or a baseline dressed as a result
        </div>
        <div style={{ width: 860, display: "flex", flexDirection: "column", gap: 12 }}>
          <div style={{ opacity: row1, translate: `0 ${interpolate(row1, [0, 1], [10, 0])}px`, display: "flex", alignItems: "center", gap: 16, border: `1px solid ${t.amber}`, background: t.amberBg, borderRadius: 10, padding: "14px 20px" }}>
            <div style={{ fontFamily: MONO, fontSize: 26, fontWeight: 700, color: t.amber, width: 130 }}>85.5%</div>
            <div style={{ fontFamily: SANS, fontSize: 13.5, color: t.ink, lineHeight: 1.4 }}>majority-class baseline — what "nobody churns" already scores, no model required</div>
          </div>
          <div style={{ opacity: row2, translate: `0 ${interpolate(row2, [0, 1], [10, 0])}px`, display: "flex", alignItems: "center", gap: 16, border: `1px solid ${t.good}`, background: `color-mix(in srgb, ${t.good} 9%, ${t.panel})`, borderRadius: 10, padding: "14px 20px" }}>
            <div style={{ fontFamily: MONO, fontSize: 26, fontWeight: 700, color: t.good, width: 130 }}>78–81%</div>
            <div style={{ fontFamily: SANS, fontSize: 13.5, color: t.ink, lineHeight: 1.4 }}>the clean, independently reproduced ceiling · AUC 0.83–0.85 — what a churn model honestly achieves</div>
          </div>
        </div>
        <div style={{ marginTop: 24, opacity: caption, fontFamily: MONO, fontSize: 14.5, color: t.ink, textAlign: "center", maxWidth: 880, lineHeight: 1.5 }}>
          <b style={{ color: t.accent }}>"Not published, never not measured."</b> Five named CS vendors, the entire open-source corpus, and even GitLab's own in-house data-science team disclose zero accuracy figures against real outcomes.
        </div>
      </div>
    </AbsoluteFill>
  );
};

// -- S4 . the Observability Question -----------------------------------------------------
const ObsCol: React.FC<{ t: Theme; label: string; sub: string; body: string; ok: boolean; appear: number }> = ({ t, label, sub, body, ok, appear }) => {
  const color = ok ? t.good : t.bad;
  return (
    <div style={{ opacity: appear, translate: `0 ${interpolate(appear, [0, 1], [12, 0])}px`, border: `1px solid ${color}`, background: ok ? `color-mix(in srgb, ${t.good} 8%, ${t.panel})` : `color-mix(in srgb, ${t.bad} 8%, ${t.panel})`, borderRadius: 12, padding: "20px 22px", width: 400 }}>
      <div style={{ fontFamily: MONO, fontSize: 15, fontWeight: 700, color, marginBottom: 4 }}>{label}</div>
      <div style={{ fontFamily: SANS, fontSize: 12, color: t.muted, marginBottom: 12 }}>{sub}</div>
      <div style={{ fontFamily: SANS, fontSize: 13.5, color: t.ink, lineHeight: 1.5 }}>{body}</div>
      <div style={{ marginTop: 14, fontFamily: MONO, fontSize: 22, color }}>{ok ? "✓ observed" : "✗ unobserved"}</div>
    </div>
  );
};

const SceneObservability: React.FC<{ t: Theme; dur: number }> = ({ t, dur }) => {
  const frame = useCurrentFrame();
  const { opacity, y } = envelope(frame, dur, 24);
  const q = step(frame, 10, 34, true);
  const c1 = step(frame, 66, 90, true);
  const c2 = step(frame, 86, 110, true);
  const caption = step(frame, 176, 202, true);

  return (
    <AbsoluteFill style={{ alignItems: "center", justifyContent: "center", opacity }}>
      <div style={{ translate: `0 ${y}px`, display: "flex", flexDirection: "column", alignItems: "center", width: 1040 }}>
        <SceneTitle t={t} kicker="before scoring anything" title="is your churn event even observable?" />
        <div style={{ opacity: q, fontFamily: SANS, fontSize: 13.5, color: t.muted, marginBottom: 22, textAlign: "center", maxWidth: 780 }}>
          a distinction the CS canon never draws — Fader, Hardie &amp; Lee, <i>"Counting Your Customers" the Easy Way</i>, Marketing Science 2005
        </div>
        <div style={{ display: "flex", gap: 22 }}>
          <ObsCol t={t} label="contractual" sub="subscription · a renewal date" body="churn happens on a known day — the cancellation event is directly observable." ok appear={c1} />
          <ObsCol t={t} label="non-contractual" sub="usage-based · self-serve" body="the point a customer goes inactive is unobserved — 'there is no way for an outside observer to know for sure.'" ok={false} appear={c2} />
        </div>
        <div style={{ marginTop: 26, opacity: caption, fontFamily: MONO, fontSize: 14, color: t.ink, textAlign: "center", maxWidth: 860, lineHeight: 1.5 }}>
          GitLab's own health-score model is built for the contractual case and applied to both — a self-serve reader is most likely handed the <span style={{ color: t.accent, fontWeight: 700 }}>wrong instrument</span>.
        </div>
      </div>
    </AbsoluteFill>
  );
};

// -- S5 . the handoff --------------------------------------------------------------------
const NextSkillCol: React.FC<{ t: Theme; label: string; body: string; appear: number }> = ({ t, label, body, appear }) => (
  <div style={{ opacity: appear, translate: `0 ${interpolate(appear, [0, 1], [10, 0])}px`, border: `1px solid ${t.line}`, background: t.panel, borderRadius: 10, padding: "12px 16px", width: 270 }}>
    <div style={{ fontFamily: MONO, fontSize: 13.5, fontWeight: 700, color: t.ink, marginBottom: 5 }}>{label}</div>
    <div style={{ fontFamily: SANS, fontSize: 12, color: t.muted, lineHeight: 1.45 }}>{body}</div>
  </div>
);

const SceneHandoff: React.FC<{ t: Theme; dur: number }> = ({ t, dur }) => {
  const frame = useCurrentFrame();
  const { opacity, y } = envelope(frame, dur, 22);
  const build = step(frame, 16, 38);
  const arrow = step(frame, 60, 80);
  const cols = step(frame, 78, 100);
  const cap = step(frame, 156, 182, true);

  const emitted: [string, string][] = [
    ["gate_verdict", ": applies / lighter-weight / not-yet"],
    ["claims", ": [claim, source, evidence tier]"],
    ["seam", ": sibling pack + filename"],
    ["cannot_support", ": what it does not prove"],
  ];

  return (
    <AbsoluteFill style={{ alignItems: "center", justifyContent: "center", opacity }}>
      <div style={{ translate: `0 ${y}px`, display: "flex", flexDirection: "column", alignItems: "center", width: 1060 }}>
        <div style={{ display: "flex", alignItems: "center", gap: 26 }}>
          <div style={{ opacity: build, border: `1px solid ${t.accent}`, background: t.codeBg, borderRadius: 10, padding: "16px 20px", fontFamily: MONO, fontSize: 12, color: t.muted, width: 420 }}>
            <div style={{ color: t.accent, fontWeight: 700, marginBottom: 8 }}>success writes</div>
            {emitted.map(([k, v], i) => {
              const op = step(frame, 32 + i * 9, 48 + i * 9);
              return (
                <div key={k} style={{ opacity: op, whiteSpace: "nowrap" }}>
                  <span style={{ color: t.accent }}>{k}</span><span style={{ color: t.ink }}>{v}</span>
                </div>
              );
            })}
          </div>
          <div style={{ fontFamily: MONO, fontSize: 30, color: t.accent, opacity: arrow }}>→</div>
          <div style={{ display: "flex", flexDirection: "column", gap: 9, opacity: cols }}>
            <NextSkillCol t={t} label="marketing" body="retention/churn signal feeding messaging — success owns onboarding education and retention comms, marketing stops at acquisition" appear={cols} />
            <NextSkillCol t={t} label="growth (provisional)" body="a validated retention motion, sent — growth owns whether it works, success owns running it as a relationship" appear={cols} />
            <NextSkillCol t={t} label="ai" body="policy artifacts — escalation, resolution definition — ai owns the turn-loop mechanics underneath them" appear={cols} />
          </div>
        </div>
        <div style={{ marginTop: 30, fontFamily: MONO, fontSize: 18, color: t.ink, opacity: cap, textAlign: "center", maxWidth: 920, lineHeight: 1.5 }}>
          a gate verdict and a graded score — never a color <span style={{ color: t.accent }}>trusted on its own</span>
        </div>
      </div>
    </AbsoluteFill>
  );
};

// -- persistent chrome + master timeline ------------------------------------------------
const BOUNDS = [220, 560, 900, 1180, 1420];
const LABELS = ["gate", "router", "flagship", "observability", "handoff"];

const PhaseBar: React.FC<{ t: Theme; frame: number }> = ({ t, frame }) => {
  const active = Math.max(0, BOUNDS.findIndex((b) => frame < b));
  return (
    <div style={{ position: "absolute", bottom: 34, left: 0, right: 0, display: "flex", justifyContent: "center", gap: 15 }}>
      {LABELS.map((l, i) => (
        <div key={l} style={{ display: "flex", alignItems: "center", gap: 7 }}>
          <div style={{ width: 8, height: 8, borderRadius: "50%", background: i === active ? t.accent : t.line, scale: String(i === active ? 1.3 : 1) }} />
          <div style={{ fontFamily: SANS, textTransform: "uppercase", letterSpacing: "0.09em", fontSize: 12, fontWeight: 600, color: i === active ? t.ink : t.muted, opacity: i === active ? 1 : 0.55 }}>{l}</div>
        </div>
      ))}
    </div>
  );
};

export const HeroAnimation: React.FC<{ theme: ThemeName }> = ({ theme }) => {
  const frame = useCurrentFrame();
  const { durationInFrames } = useVideoConfig();
  const t = themes[theme];

  const intro = step(frame, 0, 14);
  const outro = interpolate(frame, [durationInFrames - 16, durationInFrames], [1, 0], { extrapolateLeft: "clamp", extrapolateRight: "clamp" });
  const master = Math.min(intro, outro);
  const glow = interpolate(Math.sin(frame / 90), [-1, 1], [0.5, 1]);

  return (
    <AbsoluteFill style={{ backgroundColor: t.bg, fontFamily: SANS }}>
      <AbsoluteFill style={{ background: `radial-gradient(circle at 82% 16%, color-mix(in srgb, ${t.accent} 13%, transparent), transparent 44%), radial-gradient(circle at 8% 92%, color-mix(in srgb, ${t.dim} 10%, transparent), transparent 48%)`, opacity: glow }} />
      <AbsoluteFill style={{ opacity: master }}>
        <Sequence durationInFrames={220}><SceneGate t={t} dur={220} /></Sequence>
        <Sequence from={220} durationInFrames={340}><SceneRoute t={t} dur={340} /></Sequence>
        <Sequence from={560} durationInFrames={340}><SceneFlagship t={t} dur={340} /></Sequence>
        <Sequence from={900} durationInFrames={280}><SceneObservability t={t} dur={280} /></Sequence>
        <Sequence from={1180} durationInFrames={240}><SceneHandoff t={t} dur={240} /></Sequence>
        <PhaseBar t={t} frame={frame} />
      </AbsoluteFill>
    </AbsoluteFill>
  );
};
