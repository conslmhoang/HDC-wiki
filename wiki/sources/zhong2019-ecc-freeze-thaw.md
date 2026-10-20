---
type: source
slug: zhong2019-ecc-freeze-thaw
title: "Investigation on the Failure Behavior of Engineered Cementitious Composites under Freeze-Thaw Cycles"
authors: [Junfei Zhong, Jun Shi, Jiyang Shen, Guangchun Zhou, Zonglin Wang]
year: 2019   # Materials vol. 12 (2019); received 1 May 2019, accepted 30 May 2019, published 4 Jun 2019 (XML front matter)
venue: "Materials (MDPI) 2019, 12(11), 1808. Open access, CC BY 4.0. PMCID PMC6600782, PMID 31167358. Harbin Institute of Technology (corresponding author Jun Shi)"
doi: "10.3390/ma12111808"
raw_file: raw/papers/Zhong2019_ECC-freeze-thaw.xml
material_term: "ECC: 'engineered cementitious composites reinforced with PVA fibers' (authors' term). 25 Taguchi mixes span Vf 0–2 vol.% PVA, so 5 mixes have NO fiber and are not ECC. Tensile strain hardening is NOT tested; only four-point flexure is reported."
study_type: "experimental (rapid freeze–thaw in water, GB/T 50082-2009 / ASTM C666; dynamic modulus; four-point flexure; embedded strain gauge; Taguchi L25 design, S/N ratio, ANOVA; Mann–Kendall trend test)"
tags: [ecc, pva-fiber, fly-ash, ground-fly-ash, durability, freeze-thaw, dynamic-modulus, flexural-strength, taguchi, anova, mann-kendall, water-binder-ratio, harbin-institute-of-technology]
ingested: 2026-10-20
updated: 2026-10-20
---

# ECC failure behaviour under freeze–thaw cycles (Zhong et al., 2019)

## One-paragraph summary
Harbin Institute of Technology tested 25 PVA-fiber / ground-fly-ash mixes (Taguchi L25 array over four
factors at five levels: FA replacement 0–70%, S/B 0.25–0.75, W/B 0.25–0.50, V_PVA 0–2 vol.%; Table 3)
under rapid freeze–thaw in water on 100 × 100 × 400 mm prisms until final failure (§2.3). Every 25 cycles
they measured the dynamic modulus of elasticity (DME) and four-point flexural strength. Applying the
**Mann–Kendall (M-K) trend-mutation test** to the loss-vs-cycle curves, they define two "working state
leaps" before ultimate failure (UF): **initial frost-induced failure (IF)** = onset of micro-cracking and
**progressive frost-induced failure (PF)** = micro-cracks joining into macro-cracks (§3.3–3.4). This gives
three stages (stable, unstable, yield) and a **three-level design model** (IF for critical infrastructure,
PF for less important, UF for common construction; §3.4). Indices range from IF/PF/UF = 25/50/75 cycles
(plain mixes 1, 6, 16, 21) to 225/350/475 cycles (Mix 13; Table 4). ANOVA: V_PVA, W/B and FA are
significant, S/B is not (Tables 5–8). The Taguchi optimum A3B3C1D4 (FA 35%, S/B 0.5, W/B 0.25, V_PVA 1.5%)
reached IF/PF/UF = 225/375/500 cycles in the confirmation test (Table 9). No tensile, crack-width or
compressive data are given, so the strain-hardening of these "ECC" mixes is not shown.

## Objective / research question
- Study the whole freeze–thaw process of PVA-ECC (not only its terminal state) and identify
  failure-state "leaps" with a statistical criterion (§1, last para).
- Quantify the effect of FA, S/B, W/B and V_PVA on flexural strength and frost-failure indices, and
  find an optimum mix (§1; §3.5–3.7). Motivation: cold regions of north-east China (§1).

## Materials & mix design
- Binder: P.O. 42.5 cement + **ground** local fly ash (milled finer for early pozzolanic reactivity);
  oxide analysis in Table 1 (FA: SiO₂ 55.70%, Al₂O₃ 25.63%, CaO 6.93%). FA class not stated.
- Silica sand, max particle size **0.150 mm** (§2.1). Polycarboxylate SP (Table 3).
- Fiber: Kuraray PVA, L **13 mm**, d **39 µm**, density 1.3 g/cm³, tensile strength 1.6 GPa,
  modulus 42 GPa, elongation 7% (Table 2). Oil coating not stated.
- Factor levels (Table 3): FA = 0, 0.175, 0.350, 0.525, 0.700 ("fly ash content, by weight"; text treats
  it as cement replacement "up to 35%", §3.5); S/B = 0.25, 0.375, 0.5, 0.625, 0.75; W/B = 0.25, 0.3125,
  0.375, 0.4375, 0.50; V_PVA = 0, 0.005, 0.010, 0.015, 0.020 (= 0–2 vol.%). Ratios by mass (assumed for
  S/B, W/B ⚠️ unverified).

| Mix ID | Cement | Fly ash | Slag/other | Sand (type, max size) | W/B | SP | Fiber type | L (mm) | d (µm) | Vf (vol.%) |
|---|---|---|---|---|---|---|---|---|---|---|
| L25 Mix 1–25 (Table 3) | 1 − FA (binder fraction) | 0–0.70 of binder | none | silica sand, 0.150 mm; S/B 0.25–0.75 | 0.25–0.50 | 0–1.52% (Table 3) | PVA (Kuraray) | 13 | 39 | 0, 0.5, 1.0, 1.5, 2.0 |
| Mix 9 (A2B3C3D4) | 0.825 | 0.175 | none | S/B 0.5 | 0.375 | 0.30% | PVA | 13 | 39 | 1.5 |
| Mix 13 (A3B3C2D3), best of L25 | 0.65 | 0.35 | none | S/B 0.5 | 0.3125 | 0.48% | PVA | 13 | 39 | 1.0 |
| Optimum A3B3C1D4 (§3.7) | 0.65 | 0.35 | none | S/B 0.5 | 0.25 | not reported | PVA | 13 | 39 | 1.5 |

Units of binder quantities: mass fraction of binder (FA) and mass ratios to binder (S/B, W/B); SP as "%" (mass
fraction, basis not stated ⚠️). No kg/m³ given.

## Test methods
- Specimen geometry: 100 × 100 × 400 mm prisms for both freeze–thaw and flexure (§2.3).
- Freeze–thaw: rapid cycles in water (rubber sleeves), TDR-1 apparatus, GB/T 50082-2009 and ASTM C666;
  specimen-centre temperature printed as "highest −18 ± 2 °C, lowest 4 ± 2 °C" (§2.3) ⚠️ wording
  inverted as printed. Cycle duration not reported. Tested until final degradation.
- Loading / rate: four-point bending, servo-hydraulic, **0.02 mm/s** displacement (§2.3, Fig. 5); span not reported.
- Measurement: fundamental transverse frequency → DME every 25 cycles; embedded strain gauge in an extra
  specimen per mix, logged every 10 min, temperature-compensated (Fig. 6).
- Curing & test age: 24 d at 20 ± 2 °C, 95% RH, then 4 d vacuum water saturation → F-T start at 28 d (§2.3).
- Analysis: M-K statistics UF_k/UB_k (Eqs. 1–8); water-freezing parameter η = ∫ε(t)dt / V (Eq. 9);
  Taguchi larger-the-better S/N (Eq. 10); ANOVA, Minitab 17, 95% (Eqs. 11–13); confirmation estimate and
  CI (Eqs. 14–15).
→ [[durability]] · [[flexural-strength]]

## Key results
| Mix ID | f'c (MPa) | First-crack stress (MPa) | Tensile strength (MPa) | Tensile strain capacity (%) | Crack width (µm) | Other |
|---|---|---|---|---|---|---|
| All 25 mixes | not reported | not reported | not reported | not reported | not reported | flexural strength only in Fig. 7 / Fig. 16 (S/N), no tabulated values |
| Mix 1, 6, 16, 21 (Vf 0) | not reported | not reported | not reported | not reported | not reported | IF/PF/UF = 25/50/75 cycles (Table 4) |
| Mix 11 (Vf 0, FA 0.35) | not reported | not reported | not reported | not reported | not reported | 75/125/175 (Table 4) |
| Mix 9 (Vf 1.5) | not reported | not reported | not reported | not reported | not reported | 200/300/400 (Table 4) |
| Mix 13 (Vf 1.0) | not reported | not reported | not reported | not reported | not reported | 225/350/475, highest in L25 (Table 4) |
| Optimum A3B3C1D4 | not reported | not reported | not reported | not reported | not reported | measured 225/375/500 vs estimated 222 ± 19.77 / 337 ± 44.84 / 456 ± 74.93 (Table 9) |

Main findings (with Table/Fig. location):
- Fiber mixes 2, 4, 9, 13, 15 reached UF after ≥ 300 cycles; plain Mix 6 lost DME and flexural strength sharply (§3.2, Fig. 8).
- IF and PF from flexural loss data were identical to those from DME loss data (§3.3).
- At IF: residual strain grows and η jumps (more freezable water), attributed to micro-crack initiation
  (Figs. 10a, 11). Plain Mix 6 scaled at IF; fiber mixes did not (Fig. 12).
- At PF: second η inflexion; surface scaling also in fiber mixes; flexural strength and energy
  dissipation drop (Figs. 10b, 11, 13, 14). After PF: brittle flexural behaviour by UF (Fig. 14).
- S/N: flexural strength rises with V_PVA 0.5–1.5% and falls beyond 1.5%; moderate FA (≈0.35) and S/B
  (≈0.5) best; higher W/B harmful (§3.5, Fig. 16a).
- All failure indices fall with W/B; PVA 0.5–2.0% delays IF/PF/UF, with a small drop at 2.0% (dispersion);
  FA best up to 35%, PF and UF rise again at 0.525, decline at 0.70 (§3.5, Fig. 16b–d).
- ANOVA contributions (Tables 5–8): flexural strength V_PVA 45.15%, W/B 30.01%, FA 12.65%, S/B 7.96%;
  IF V_PVA 39.02%, W/B 35.64%, FA 14.68%; PF V_PVA 48.60%, W/B 21.88%, FA 19.87%; UF W/B 38.47%,
  V_PVA 32.70%, FA 21.63%, S/B 2.10%.

## Mechanisms / explanations offered by authors
- Freezing builds hydraulic pressure (ice expansion) and osmotic pressure (supercooled gel water moving
  to ice) (§3.4, refs. 39–42).
- PVA fibers entrain air and release pressure, delaying micro-crack formation, and bridge micro-cracks in
  the unstable stage — a freeze–thaw "toughness" (§3.4–3.5).
- Excess fiber (2%) disperses poorly and reduces density (§3.5).
- Ground FA refines capillary pores via pozzolanic reaction; too much FA (0.70) leaves insufficient
  Ca(OH)₂ (§3.5).
- Higher W/B worsens porosity; higher S/B lowers paste fraction (§3.5).
- Damage proceeds from the inside out: micro-cracks → macro-cracks → destruction (§3.4).

## Limitations (stated + observed)
- Stated: IF/PF are estimates because data are collected only every 25 cycles (§3.3).
- Observed: no direct tension, crack width, compressive strength, mass loss or air-void data; strain
  hardening never demonstrated, and 5 of 25 mixes are fiber-free mortar.
- Observed: flexural strength values are not tabulated (figures only); span and specimen count not given.
- Observed: definition of UF (terminal cycle) criterion not stated (e.g. DME 60% or flexural loss).
- Observed: ANOVA text says S/B p-values are "lower than 0.05", but S/B is insignificant
  (p = 0.0424 for flexure is < 0.05 yet marked X; F 3.76 < 3.84) ⚠️ inconsistent as printed.
- Observed: FA "by weight" not explicitly defined as fraction of binder; SP % basis not stated.
- Observed: one cement, one FA, one fiber; Taguchi assumes no factor interactions.

## Relation to other work
- Agrees with: PVA-ECC survives ≥ 300 cycles while fiber-free mortar fails early (Sahmaran 2012, as cited
  in [[ma2021-ecc-durability-review]], p. 4); mechanism "fibers relieve ice-expansion stress"
  ([[ma2021-ecc-durability-review]], p. 4).
- Contradicts: none directly. Partial tension with the review claim that FA may hinder frost resistance
  (refs. 18–21 in this paper) — here ground FA ≤ 35–52.5% helps.
- Extends: first primary freeze–thaw source in the wiki; adds a statistical (M-K) staging of frost damage
  and a W/B–V_PVA–FA ranking. → [[durability]]

## Pages updated from this source
- [[durability]] · [[pva-fiber]] · [[fly-ash]] · [[water-binder-ratio]] · [[flexural-strength]] · [[mix-designs]]

## To verify
- [ ] Temperature wording: "highest temperature at the center −18 ± 2 °C, lowest 4 ± 2 °C" (§2.3) — inverted as printed.
- [ ] FA level meaning (fraction of binder vs FA/C); S/B and W/B by mass (assumed).
- [ ] UF (ultimate failure) criterion not stated.
- [ ] ANOVA S/B p-value statement vs Table 5 (p = 0.0424 marked insignificant).
- [ ] Flexural strength values readable only from Fig. 7 (PDF figure not inspected; XML has no data).
- [ ] Whether the PVA fiber is oil-coated (not stated).
