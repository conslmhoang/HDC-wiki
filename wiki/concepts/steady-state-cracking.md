---
type: concept
slug: steady-state-cracking
aliases: [flat crack, Griffith vs steady-state crack, notch insensitivity, failure mechanism map, K-tilde]
tags: [micromechanics, theory, history]
sources: [li1992-steady-state-multiple-cracking]
updated: 2026-10-16
---

# Steady-State (Flat) Cracking: the 1992 foundation

## Definition
A crack that extends at a constant ambient stress σ_ss with a **flat** opening, instead of a
Griffith crack whose opening grows with its length. Li & Leung (1992) state that steady-state
cracking is a prerequisite of multiple cracking and pseudo strain-hardening
([[li1992-steady-state-multiple-cracking]], p. 2247). → [[strain-hardening]]

## Key equations ([[li1992-steady-state-multiple-cracking]])
- **Bridging law** (pre-peak, Eq. 4): σ̃_B = g[2(δ̃/δ̃*)^{1/2} − δ̃/δ̃*], with
  - σ0 = Vf·τ·(Lf/df)/2
  - δ̃* = [2τ/((1+η)Ef)]·(Lf/df)
  - snubbing factor g = 2(1 + e^{πf/2})/(4 + f²)
- **Steady-state condition:** K̃ ≤ K̃_crit = 1/(3√π) ≈ 0.188 (Eq. 14), with
  K̃ = [10/(3√π)]·(G_tip/G_r) (Eq. 15). Equivalently **G_r ≥ 10·G_tip** (Eq. 16), where
  G_r is the area *under* the pre-peak σ–δ curve.
- **Critical fiber volume** (Eq. 17): V_f^crit = 48·G_tip / [g·τ·df·(Lf/df)²·δ̃*]. This gives
  V_f^crit ∝ (Lf/df)⁻³, so **doubling Lf cuts the required fiber by 87.5%** (p. 2259).
  → [[fiber-geometry]]
- **Multiple cracking** also needs a flaw size c̃ > c̃_mc (Eq. 24). This is a flaw-size condition
  that later PSH indices leave out (p. 2255, 2260).

## Failure mechanism map (Fig. 7)
| Mode | Behaviour | Example (Table 2) |
|---|---|---|
| D | steady-state cracking at σ_ss, then multiple cracking up to σ0 | glass / OPC paste |
| C | initial load drop, then multiple cracking | PP / lightweight mortar |
| A | first-crack drop, then a small rise | Spectra PE / HS concrete (Vf 0.6%) |
| B | Griffith-type catastrophic failure | steel / mortar |

## Quantitative evidence
Table 1 model cases (OPC, Gm = 100 J/m²), V_f^crit:

| Fiber | V_f^crit |
|---|---|
| steel | 3.6% |
| glass | 0.4% |
| carbon | 0.6% |
| PP | 2.9% |

⚠️ These values could not be reproduced from Eq. 17 with the stated inputs (see the source page).

> Synthesis: Li & Leung's flaw-size condition and the strong (Lf/df)³ dependence of G_r may
> explain why the 6 mm PE mixes of [[su2023-rubber-modified-hshdc]] fail brittle despite meeting
> the later PSH indices. This is an interpretation, not stated by either paper.

## Historical line
Li & Leung 1992 (K̃–c̃ framework, G_r ≥ 10 G_tip) → Kanda & Li 1998 (J-integral form,
J_tip ≤ J′b, thresholds of 1.2 and 3) → used in all ingested ECC/HDC papers. → [[strain-hardening]]

## Related
- [[strain-hardening]] · [[fiber-bridging]] · [[multiple-cracking]] · [[size-effect]]
