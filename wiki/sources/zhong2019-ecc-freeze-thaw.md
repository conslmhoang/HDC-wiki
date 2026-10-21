---
type: source
slug: zhong2019-ecc-freeze-thaw
title: "Investigation on the Failure Behavior of Engineered Cementitious Composites under Freeze-Thaw Cycles"
authors: [Junfei Zhong, Jun Shi, Jiyang Shen, Guangchun Zhou, Zonglin Wang]
year: 2019   # Materials 12, 1808; received 1 May 2019, accepted 30 May 2019, published 4 Jun 2019 (p. 1)
venue: "Materials (MDPI) 2019, 12(11), 1808, 23 pp. Open access, CC BY 4.0. PMCID PMC6600782, PMID 31167358 (from the Europe PMC record). Harbin Institute of Technology (corresponding author Jun Shi). Funding: NSFC 51608069 (p. 21)"
doi: "10.3390/ma12111808"
raw_file: raw/papers/Zhong2019_ECC-freeze-thaw.pdf
material_term: "ECC: 'engineered cementitious composites (ECC) reinforced with polyvinyl alcohol (PVA) fibers' (authors' term, p. 1). 25 Taguchi mixes span Vf 0–2 vol.% PVA, so 5 mixes have NO fiber and are not ECC. Tensile strain hardening is NOT tested; only four-point flexure is reported (several fibre mixes show deflection hardening, Fig. 7)."
study_type: "experimental (rapid freeze–thaw in water, GB/T 50082-2009 / ASTM C666; dynamic modulus; four-point flexure; embedded strain gauge; Taguchi L25 design, S/N ratio, ANOVA; Mann–Kendall trend test)"
tags: [ecc, pva-fiber, fly-ash, ground-fly-ash, durability, freeze-thaw, dynamic-modulus, flexural-strength, taguchi, anova, mann-kendall, water-binder-ratio, harbin-institute-of-technology]
ingested: 2026-10-20
updated: 2026-10-21
---

# ECC failure behaviour under freeze–thaw cycles (Zhong et al., 2019)

> Re-checked against the publisher PDF on 2026-10-21 (page numbers added; Fig. 7 peak loads, Fig. 8 losses,
> Fig. 10 cycle/temperature data, Fig. 11 η and Fig. 14 flexural stresses read from figures; figure numbers
> of the surface photos corrected to the published version).

## One-paragraph summary
Harbin Institute of Technology tested 25 PVA-fiber / ground-fly-ash mixes (Taguchi L25 array over four
factors at five levels: FA 0–70% of binder, S/B 0.25–0.75, W/B 0.25–0.50, V_PVA 0–2 vol.%; Table 3, p. 4)
under rapid freeze–thaw in water on 100 × 100 × 400 mm prisms until final failure (p. 5, §2.3). Every 25 cycles
they measured the dynamic modulus of elasticity (DME) and four-point flexural strength. Applying the
**Mann–Kendall (M-K) trend-mutation test** to the loss-vs-cycle curves, they define two "working state
leaps" before ultimate failure (UF): **initial frost-induced failure (IF)** = onset of micro-cracking and
**progressive frost-induced failure (PF)** = micro-cracks joining into macro-cracks (pp. 8–14, §3.3–3.4). This
gives three stages (stable, unstable, yield) and a **three-level design model** (IF for critical
infrastructure, PF for less important, UF for common construction; p. 14). Indices range from IF/PF/UF =
25/50/75 cycles (plain mixes 1, 6, 16, 21) to 225/350/475 cycles (Mix 13; Table 4, p. 9). ANOVA: V_PVA, W/B
and FA are significant, S/B is not (Tables 5–8, pp. 17–18). The Taguchi optimum A3B3C1D4 (FA 35%, S/B 0.5,
W/B 0.25, V_PVA 1.5%) reached IF/PF/UF = 225/375/500 cycles in the confirmation test (Table 9, p. 20). Unfrozen
peak flexural loads range ≈ 12.5–31 kN (Fig. 7); Mix 9 flexural stress fell from ≈ 12.2 MPa (0 cycles) to
≈ 2.3 MPa at UF (Fig. 14). No tensile, crack-width or compressive data are given, so strain hardening of these
"ECC" mixes is not shown.

## Objective / research question
- Study the whole freeze–thaw process of PVA-ECC (not only its terminal state) and identify
  failure-state "leaps" with a statistical criterion (p. 2, §1, last para).
- Quantify the effect of FA, S/B, W/B and V_PVA on flexural strength and frost-failure indices, and
  find an optimum mix (p. 2; pp. 15–20, §3.5–3.7). Motivation: cold regions of north-east China (p. 2).

## Materials & mix design
- Binder: P.O. 42.5 cement + **ground** local fly ash (milled finer for early pozzolanic reactivity; p. 2);
  oxide analysis in Table 1 (p. 3): cement SiO₂ 21.08, Al₂O₃ 5.47, Fe₂O₃ 3.96, CaO 62.28%; FA SiO₂ 55.70%,
  Al₂O₃ 25.63%, Fe₂O₃ 5.65%, CaO 6.93%, MgO 2.25%, SO₃ 0.58%, R₂O 0.60%. FA class not stated. Particle
  size distributions in Fig. 1 (p. 3).
- Silica sand, max particle size **0.150 mm** (p. 2, §2.1). Polycarboxylate SP (Table 3).
- Fiber: Kuraray PVA, L **13 mm**, d **39 µm**, density 1.3 g/cm³, tensile strength 1.6 GPa,
  modulus 42 GPa, elongation 7% (Table 2, p. 3). Oil coating not stated.
- Factor levels (Fig. 3 and Table 3, p. 4): FA = 0, 0.175, 0.350, 0.525, 0.700 ("fly ash content, by weight";
  Fig. 3 pairs these with cement 1.000, 0.825, 0.650, 0.475, 0.300, so FA is the **mass fraction of binder**);
  S/B = 0.25, 0.375, 0.5, 0.625, 0.75; W/B = 0.25, 0.3125, 0.375, 0.4375, 0.50; V_PVA = 0, 0.005, 0.010,
  0.015, 0.020 (= 0–2 vol.%). SP is a "mass fraction" (p. 4; basis not stated). S/B and W/B assumed by mass ⚠️.

| Mix ID | Cement | Fly ash | Slag/other | Sand (type, max size) | W/B | SP | Fiber type | L (mm) | d (µm) | Vf (vol.%) |
|---|---|---|---|---|---|---|---|---|---|---|
| L25 Mix 1–25 (Table 3) | 1 − FA (binder fraction) | 0–0.70 of binder | none | silica sand, 0.150 mm; S/B 0.25–0.75 | 0.25–0.50 | 0–1.52% (Table 3) | PVA (Kuraray) | 13 | 39 | 0, 0.5, 1.0, 1.5, 2.0 |
| Mix 9 (A2B3C3D4) | 0.825 | 0.175 | none | S/B 0.5 | 0.375 | 0.30% | PVA | 13 | 39 | 1.5 |
| Mix 13 (A3B3C2D3), best of L25 | 0.65 | 0.35 | none | S/B 0.5 | 0.3125 | 0.48% | PVA | 13 | 39 | 1.0 |
| Optimum A3B3C1D4 (§3.7) | 0.65 | 0.35 | none | S/B 0.5 | 0.25 | not reported | PVA | 13 | 39 | 1.5 |

Units of binder quantities: mass fraction of binder (FA) and ratios to binder (S/B, W/B); SP as "%" (mass
fraction, basis not stated ⚠️). No kg/m³ given.

## Test methods
- Specimen geometry: 100 × 100 × 400 mm prisms for both freeze–thaw and flexure (p. 5, §2.3).
- Freeze–thaw: rapid cycles in water (rubber sleeves, Fig. 4), TDR-1 apparatus, GB/T 50082-2009 and ASTM C666;
  specimen-centre temperature printed as "highest −18 ± 2 °C, lowest 4 ± 2 °C" (p. 5), i.e. inverted; Fig. 10
  (p. 12) shows the centre between ≈ −18 °C and ≈ +4 °C and the fluid between ≈ −23 °C and ≈ +14 °C, with one
  cycle lasting **≈ 240 min** (read from Fig. 10 time axis). Tested until final degradation.
- Loading / rate: four-point bending, servo-hydraulic, **0.02 mm/s** displacement (p. 5, Fig. 5); span not reported.
- Measurement: fundamental transverse frequency → DME every 25 cycles; embedded strain gauge (DH3816 logger)
  in an extra specimen per mix, logged every 10 min, temperature-compensated with a dried specimen (pp. 5–6, Fig. 6).
- Curing & test age: 24 d at 20 ± 2 °C, 95% RH, then 4 d vacuum water saturation → F-T start at 28 d (p. 5).
- Analysis: M-K statistics UF_k/UB_k (Eqs. 1–8, pp. 8–9); water-freezing parameter η = ∫ε(t)dt / V (Eq. 9,
  p. 10); Taguchi larger-the-better S/N (Eq. 10, p. 15); ANOVA, Minitab 17, 95% (Eqs. 11–13, p. 17);
  confirmation estimate and CI (Eqs. 14–15, p. 20).
→ [[durability]] · [[flexural-strength]] · [[freeze-thaw]]

## Key results
| Mix ID | f'c (MPa) | First-crack stress (MPa) | Tensile strength (MPa) | Tensile strain capacity (%) | Crack width (µm) | Other |
|---|---|---|---|---|---|---|
| All 25 mixes | not reported | not reported | not reported | not reported | not reported | flexural peak loads only as curves (Fig. 7) and S/N (Fig. 16a); no tabulated strengths |
| Mix 1, 6, 16, 21 (Vf 0) | not reported | not reported | not reported | not reported | not reported | IF/PF/UF = 25/50/75 cycles (Table 4); peak load ≈ 13.5 / 13 / 12.8 / 12.5 kN, brittle (Fig. 7) |
| Mix 11 (Vf 0, FA 0.35) | not reported | not reported | not reported | not reported | not reported | 75/125/175 (Table 4); ≈ 15.5 kN (Fig. 7c) |
| Mix 9 (Vf 1.5) | not reported | not reported | not reported | not reported | not reported | 200/300/400 (Table 4); ≈ 30.8 kN, plateau to > 6 mm (Fig. 7c); flexural stress ≈ 12.2 → 11.7 (IF) → 9.8 (PF) → 2.3 MPa (UF) (Fig. 14) |
| Mix 13 (Vf 1.0) | not reported | not reported | not reported | not reported | not reported | 225/350/475, highest in L25 (Table 4); ≈ 30.5 kN (Fig. 7d) |
| Optimum A3B3C1D4 | not reported | not reported | not reported | not reported | not reported | measured 225/375/500 vs estimated 222 ± 19.77 / 337 ± 44.84 / 456 ± 74.93 (Table 9, p. 20) |

Peak flexural loads before F-T, read from Fig. 7 (p. 6), kN: Mix 1 ≈ 13.5, 2 ≈ 15.8, 3 ≈ 16.0, 4 ≈ 24.3,
5 ≈ 17.8, 6 ≈ 13, 7 ≈ 16.5, 8 ≈ 26.8, 9 ≈ 30.8, 10 ≈ 16.2, 11 ≈ 15.5, 12 ≈ 15.5, 13 ≈ 30.5, 14 ≈ 20.8,
15 ≈ 31.0, 16 ≈ 12.8, 17 ≈ 26.0, 18 ≈ 23.6, 19 ≈ 24.0, 20 ≈ 28.7, 21 ≈ 12.5, 22 ≈ 20.8, 23 ≈ 21.5,
24 ≈ 26.4, 25 ≈ 21.5. Conversion to stress is not given (span not reported); Mix 9 ≈ 30.8 kN ↔ ≈ 12.2 MPa in
Fig. 14 implies ≈ 0.40 MPa/kN (computed here, interpretation).

Main findings (with page/Table/Fig. location):
- Fibrous mixes (e.g. 9, 13, 15) show higher load capacity and post-cracking response than plain ones
  (1, 6, 11) (p. 7, §3.1, Fig. 7).
- Fiber mixes 2, 4, 9, 13, 15 reached UF after ≥ 300 cycles; plain Mix 6 lost DME and flexural strength sharply
  (p. 7, §3.2, Fig. 8). At the last recorded cycle (Fig. 8, p. 7, read): flexural-strength loss ≈ 68% (Mix 6,
  75 cycles) and ≈ 75–85% for the fibre mixes; DME loss ≈ 60% (Mix 6) and ≈ 44–54% for the fibre mixes
  (e.g. Mix 13 ≈ 51% at 475, Mix 9 ≈ 46% at 400).
- IF and PF from flexural loss data were identical to those from DME loss data (p. 9, §3.3).
- At IF: residual strain grows and η jumps (more freezable water), attributed to micro-crack initiation
  (pp. 10–13, Figs. 10a, 11). Mix 9 η (Fig. 11, p. 13, read): ≈ 5.1 (198 cycles) → 6.1 (200, IF) → 8.2 (202);
  ≈ 13.7 (298) → 18 (300, PF) → 33 (302). Peak strain per cycle (Fig. 10, p. 12, read) ≈ 145–185 µm/m around IF,
  ≈ 1,070–1,480 µm/m around PF, ≈ 8,000–16,800 µm/m around UF.
- Plain Mix 6 scaled at IF; fibre Mixes 4 and 9 did not (Fig. 15, p. 14 — photos after 25 / 175 / 200 cycles).
- At PF: second η inflexion; surface scaling also in fibre mixes, less than in Mix 6 (Fig. 13, p. 13); flexural
  strength and energy dissipation drop (Fig. 14, p. 14). Surface at UF in Fig. 12 (p. 13: Mix 6 after 75, Mix 4
  after 350, Mix 9 after 400 cycles). After PF: brittle flexural behaviour by UF (Fig. 14).
- S/N (Fig. 16, pp. 15–16): best levels A3, B3, C1, D4 for flexural strength and all three indices. Flexural
  strength rises with V_PVA up to 1.5% and falls at 2.0%; moderate FA (≈0.35) and S/B (≈0.5) best; higher W/B
  harmful (p. 15, Fig. 16a).
- All failure indices fall with W/B; PVA 0.5–2.0% delays IF/PF/UF, with a small drop at 2.0% (dispersion);
  FA best up to 35% (pp. 15–17, Fig. 16b–d). Text says PF and UF show an "obvious rise" at FA 0.525 (p. 16);
  Fig. 16c–d show A4 below A3 but above A2 and A5 (e.g. UF S/N ≈ 50.6 vs ≈ 51.1 at A3, read) ⚠️.
- ANOVA contributions (Tables 5–8, pp. 17–18): flexural strength V_PVA 45.15%, W/B 30.01%, FA 12.65%, S/B 7.96%;
  IF V_PVA 39.02%, W/B 35.64%, FA 14.68%, S/B 6.84%; PF V_PVA 48.60%, W/B 21.88%, FA 19.87%, S/B 5.23%;
  UF W/B 38.47%, V_PVA 32.70%, FA 21.63%, S/B 2.10%.

## Mechanisms / explanations offered by authors
- Freezing builds hydraulic pressure (ice expansion) and osmotic pressure (supercooled gel water moving
  to ice) (pp. 9–10, §3.4, refs. 39–42).
- PVA fibers entrain air and release pressure, delaying micro-crack formation, and bridge micro-cracks in
  the unstable stage — a freeze–thaw "toughness" (p. 14; p. 15, §3.5).
- Excess fiber (2%) disperses poorly and reduces density (p. 15, §3.5).
- Ground FA refines capillary pores via pozzolanic reaction; too much FA (0.70) leaves insufficient
  Ca(OH)₂ (pp. 16–17, §3.5).
- Higher W/B worsens porosity; higher S/B lowers paste fraction (p. 17, §3.5).
- Damage proceeds from the inside out: micro-cracks → macro-cracks → destruction (p. 13, §3.4).

## Limitations (stated + observed)
- Stated: IF/PF are estimates because data are collected only every 25 cycles (p. 9, §3.3).
- Observed: no direct tension, crack width, compressive strength, mass loss or air-void data; strain
  hardening never demonstrated, and 5 of 25 mixes are fiber-free mortar.
- Observed: flexural strengths are not tabulated (Fig. 7 gives loads only); span and specimen count not given.
- Observed: definition of UF (terminal cycle) criterion not stated; at the last points of Fig. 8 the DME loss
  is ≈ 44–60%, i.e. beyond the usual 40% loss limit of GB/T 50082 [general knowledge — needs source].
- Observed: ANOVA text says S/B p-values are "lower than 0.05" (p. 18), but S/B is insignificant
  (p = 0.0424 for flexure in Table 5 is < 0.05 yet marked X; F 3.76 < 3.84) ⚠️ inconsistent as printed.
- Observed: in the published PDF the surface-photo figure numbers are swapped relative to their content in
  places (text cites Fig. 15 for IF and Fig. 12 for UF; captions confirm 25/175/200 cycles = Fig. 15).
- Observed: SP % basis not stated; one cement, one FA, one fiber; Taguchi assumes no factor interactions.

## Relation to other work
- Agrees with: PVA-ECC survives ≥ 300 cycles while fiber-free mortar fails early (Sahmaran 2012, as cited
  in [[ma2021-ecc-durability-review]], p. 4); mechanism "fibers relieve ice-expansion stress"
  ([[ma2021-ecc-durability-review]], p. 4).
- Contradicts: none directly. Partial tension with the claim that FA may hinder frost resistance
  (refs. 18–21 in this paper, p. 2) — here ground FA ≤ 35% helps most.
- Extends: first primary freeze–thaw source in the wiki; adds a statistical (M-K) staging of frost damage
  and a W/B–V_PVA–FA ranking. → [[durability]]

## Pages updated from this source
- [[durability]] · [[freeze-thaw]] · [[pva-fiber]] · [[fly-ash]] · [[water-binder-ratio]] · [[flexural-strength]] · [[mix-designs]]

## To verify
- [ ] S/B and W/B by mass (assumed; not stated).
- [ ] UF (ultimate failure) criterion not stated.
- [ ] ANOVA S/B p-value statement vs Table 5 (p = 0.0424 marked insignificant).
- [ ] FA 0.525 "obvious rise" in PF/UF (p. 16) vs Fig. 16c–d (A4 below A3).
- [ ] Whether the PVA fiber is oil-coated (not stated).
- [x] Temperature wording: Fig. 10 (p. 12) confirms the centre cycles between ≈ −18 °C (lowest) and ≈ +4 °C (highest); the printed text is inverted.
- [x] FA level meaning: Fig. 3 (p. 4) pairs FA levels with cement 1.000–0.300, so FA is the mass fraction of binder.
- [x] Flexural data: peak loads read from Fig. 7 (p. 6) and Mix 9 stresses from Fig. 14 (p. 14).
