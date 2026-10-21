---
type: source
slug: zhao2022-ecc-tension-damage-model
title: "An Experimental and Analytical Study on a Damage Constitutive Model of Engineered Cementitious Composites under Uniaxial Tension"
authors: [Dapeng Zhao, Changjun Wang, Ke Li, Pengbo Zhang, Lianyou Cong, Dazhi Chen]
year: 2022   # Materials 15(17), article 6063; received 28 Jul, accepted 30 Aug, published 1 Sep 2022
venue: "Materials (MDPI), Vol. 15, No. 17, Article 6063 (18 pp.)"
doi: "10.3390/ma15176063"
raw_file: raw/papers/Zhao2022_ECC-tension-damage-model.pdf
material_term: "ECC (engineered cementitious composites); PVA-ECC"
study_type: experimental + analytical (damage constitutive model) + numerical (ABAQUS FE validation)
tags: [ecc, pva-ecc, pva-fiber, kuraray, uniaxial-tension, thin-plate-coupon, fiber-volume-fraction, water-binder-ratio, fracture-energy, damage-mechanics, constitutive-model, trilinear-model, abaqus, cdp, hsswr, zhengzhou-university]
ingested: 2026-10-20
updated: 2026-10-21
---

# Damage constitutive model of PVA-ECC in uniaxial tension (Zhao et al., 2022)

> Re-checked against the publisher PDF on 2026-10-21 (page numbers added; Table 3–6 verified; model units verified by recomputing Table 4).

## One-paragraph summary
Zhengzhou University tested five PVA-ECC groups in monotonic uniaxial tension on CFRP-tabbed thin plates
(280 × 40 × 13 mm, 120 mm extensometer gauge), varying fiber content **v = 1, 1.5, 2 vol.%** (at W/B 0.28)
and **W/B r = 0.24, 0.25, 0.28** (at 2%) (Table 1, p. 2; Table 3, p. 3–4). The matrix is cement : silica sand : FA : silica fume
= 1 : 1.5 : 2.0 : 0.073 by mass (FA/C 2.0). Raising v or W/B raised peak strain, ultimate (post-peak rupture)
strain and tensile fracture energy; raising W/B lowered first-crack and peak stress, while v hardly changed peak stress
(Table 3). The best group V3R3 (2%, W/B 0.28) gave σ_p 3.23 MPa, **ε_p 2.00%**, ε_u 4.08%, G_f 11.1 kJ/m².
The authors define a damage factor from the **secant angle**: d = 1 − θ/θ0, θ = arctan(σ/ε) (Eqs. 5–8, p. 9), with
d = 0 (elastic), a power law (hardening) and a quadratic (softening) (Eq. 9, p. 10). Two free coefficients (b, A) are
fitted linearly to v and r (Eqs. 16–17, p. 10, R² 0.989 / 0.994). The model was checked against the group's earlier
tests (Table 5, p. 11) and used in ABAQUS (CDP) for ECC reinforced with high-strength stainless steel wire rope (HSSWR):
peak-load ratio 1.042 vs 1.123 for the classic trilinear model; displacement-at-peak ratio 0.964 vs 0.574 (§5.2, p. 14–15).

## Objective / research question
1. Effects of PVA content and W/B on ECC tensile properties (§1, p. 2).
2. Damage evolution law of ECC in uniaxial tension (§1).
3. A damage constitutive model with parameters expressed in v and r (§4, p. 9–12).
4. Validation by FE analysis of HSSWR-reinforced ECC vs the trilinear model (§5, p. 12–15).

## Materials & mix design
| Mix ID | Cement | Fly ash | Slag/other | Sand (type, max size) | W/B | SP | Fiber type | L (mm) | d (µm) | Vf (vol.%) |
|---|---|---|---|---|---|---|---|---|---|---|
| V1R3 | 1.000 ("ordinary silicate", grade n.r.) | 2.000 | micro-silica fume 0.073 | silica sand 1.500 (size n.r.) | 0.28 (water 0.860) | 0.041 | PVA (Kuraray) | 12 | 40 | 1 (PVA mass 0.029) |
| V2R3 | 1.000 | 2.000 | SF 0.073 | 1.500 | 0.28 (0.860) | 0.041 | PVA | 12 | 40 | 1.5 (0.044) |
| V3R1 | 1.000 | 2.000 | SF 0.073 | 1.500 | 0.24 (0.738) | 0.041 | PVA | 12 | 40 | 2 (0.057) |
| V3R2 | 1.000 | 2.000 | SF 0.073 | 1.500 | 0.25 (0.768) | 0.041 | PVA | 12 | 40 | 2 (0.057) |
| V3R3 | 1.000 | 2.000 | SF 0.073 | 1.500 | 0.28 (0.860) | 0.041 | PVA | 12 | 40 | 2 (0.057) |

Units of binder quantities: ratio to cement (Table 1, p. 2; no unit printed, "by mass" implied, not stated ⚠️). W/B computed here as
water / (cement + FA + SF) = 0.860 / 3.073 = 0.280, 0.738 / 3.073 = 0.240, 0.768 / 3.073 = 0.250, matching the r values in Table 3.
FA/C = 2.0 by mass; sand/binder ≈ 0.49 (computed). FA class and SF/FA properties not reported.
- W/B window: < 0.24 too dry to mix, > 0.30 too dilute (pre-test, §2.1, p. 2–3).
- **PVA fiber** (Table 2, p. 2, Kuraray): 12 mm, 40 µm, 1560 MPa, 41 GPa, 6.5% elongation, 1.3 g/cm³. Product grade / oiling not stated.
- Mixing: dry 3 min → water + SP 3 min → fibers 3 min (§2.1, p. 3).

## Test methods
- Specimen geometry: thin plate 280 × 40 × 13 mm, 5 per group (V3R1: 2 excluded for deviation → 3) (§2.1, p. 2; §3.1, p. 4).
  Ends sanded, bonded with one CFRP layer (0.111 mm; 4150 MPa, 225 GPa) and 0.8 mm aluminium tabs with epoxy
  (epoxy 47.2 MPa, 2860 MPa per manufacturer) (p. 3; Fig. 1, p. 4).
- Loading / rate: 10 t electro-hydraulic servo machine (Jinan Sans), displacement control 0.2 mm/min, monotonic; lab 298.15 K, RH 95% (§2.2, p. 4).
- Measurement: strain gauge at the centre (pre-cracking); extensometer over 120 mm (post-cracking) (§2.2, p. 4). First crack = first drop on the σ–ε curve (§3.1.1, p. 5).
- Fracture energy: G_f,N = G_f,A,N (hardening energy minus elastic part, × L_g) + G_f,B,N (softening σ–δ area) (Eqs. 1–4, p. 6, after ref 41, as cited).
- Curing & test age: 28 d in saturated lime water, then dried and 7 d for epoxy cure → tested at ≥ 35 d (computed; exact age not stated ⚠️) (p. 3).
- FE: ABAQUS CDP for ECC (C3D8R, 10 mm mesh; dilation 35°, eccentricity 0.1, fb0/fc0 1.07, K 0.6667, viscosity 0.0005); HSSWR as T3D2 truss, embedded,
  von Mises with y = 3.33x + 3.66x² + 1.33x³ (Eq. 21, x = ε_s/ε_st, y = σ_s/σ_st); CFRP shell, tied (§5.1, p. 13–14).
→ [[dogbone-uniaxial-tension]] · [[tensile-constitutive-model]]

## Key results
| Mix ID | f'c (MPa) | First-crack stress (MPa) | Tensile strength (MPa) | Tensile strain capacity (%) | Crack width (µm) | Other |
|---|---|---|---|---|---|---|
| V1R3 (1%, 0.28) | not reported | 1.976 (ε_k 0.025%) | 3.104 | ε_p 0.511; ε_u 1.895 | not reported | G_f 3.513 kJ/m² (Table 3, p. 3) |
| V2R3 (1.5%, 0.28) | not reported | 2.020 (0.048%) | 2.959 | ε_p 0.796; ε_u 2.539 | not reported | G_f 5.216 |
| V3R1 (2%, 0.24) | not reported | 3.440 (0.041%) | 4.572 | ε_p 0.503; ε_u 2.230 | not reported | G_f 7.420; n = 3 |
| V3R2 (2%, 0.25) | not reported | 2.665 (0.067%) | 3.787 | ε_p 1.071; ε_u 2.975 | not reported | G_f 9.415 |
| V3R3 (2%, 0.28) | not reported | 2.447 (0.069%) | 3.234 | **ε_p 2.000**; ε_u 4.077 | not reported | G_f 11.144 (Table 3, p. 4) |
| HSSWR-ECC matrix (from ref 44) | not reported | 2.45 (0.02%) | 3.53 | ε_p 2.79; ε_u 4 | not reported | 2%, W/B 0.28 (§5.1, p. 13) |

Strain basis: **ε_p = strain at peak stress** (comparable with ε_tu in the wiki); **ε_u = strain at rupture**, on the softening branch (§3.1.3, p. 6).
Values are group averages of individual specimens listed in Table 3 (p. 3–4); standard deviations e.g. ε_p SD 0.083–0.351%, ε_u SD up to 0.734% (V3R1).

Main findings (with Table/Fig. location):
- The percentages in §3.1 (p. 5–7) are **step-wise** (1 → 1.5% and then 1.5 → 2%; 0.24 → 0.25 and then 0.25 → 0.28), checked here against Table 3,
  though the text reads as if both are relative to the base. Overall (computed from Table 3):
  - v 1 → 2% (W/B 0.28): ε_p 0.511 → 2.000% (×3.9), ε_u 1.895 → 4.077%, G_f 3.51 → 11.14 kJ/m², σ_p 3.10 → 3.23 MPa (≈ unchanged).
  - W/B 0.24 → 0.28 (2%): σ_k 3.44 → 2.45 MPa, σ_p 4.57 → 3.23 MPa, ε_p 0.503 → 2.000%, G_f 7.42 → 11.14 kJ/m².
- Peak stress is governed by W/B, not by v (1–2%) (§3.1.2, p. 6).
- Three damage stages (§3.2, p. 7–8; Fig. 4, p. 9): elastic, no damage → hardening with stable, dispersed damage (rate minimal at peak) → softening with unstable damage. Main crack mostly formed near the grips (p. 8).
- Damage coefficients (Table 4, p. 10): b 0.784–0.997, A 0.067–0.214, both falling with v and r; k 0.127–0.203; B −0.090 to 0.138; C −0.030 to 0.252.
- Fits: b = (1.206 − 0.213v)(2.061r + 0.436); A = (0.358 − 0.147v)(2.842r + 0.247), v in %, for v 1–2% and r 0.24–0.28 (Eqs. 16–17, p. 10–11).
- **Units of the damage factor (verified here):** recomputing k, B and C from Eqs. 13–15 with Table 3 means and Table 4 b, A reproduces
  Table 4 to three decimals only when σ is in **MPa**, ε in **%** and angles in radians. Exception: for V3R2 the recomputed B = −0.171
  and C = 0.172, vs printed −0.090 and 0.108 ⚠️ (V3R2's printed B equals V3R3's; possibly a copy error in Table 4).
- Validation on 4 groups of ref 43 (same group; Table 5, p. 11): e.g. V-V3R3 σ_p 3.349 MPa, ε_p 2.010%, ε_u 4.018%; b_expt/b_calc mean 0.971 (CoV 0.023); A 1.155 (CoV 0.208).
- FE of HSSWR-ECC (Table 6, p. 14: TC1–TC4, test-section width 80 / 70 / 60 / 47 mm, rope spacing 50 / 40 / 30 / 20 mm, rope Ø 2.4 mm,
  σ_st 1573 MPa at ε_st 2.99%; reinforcement ratio 0.28–0.48%): peak load / test 1.042 (proposed) vs 1.123 (trilinear) (CoV 0.026 given once);
  displacement at peak / test 0.964 vs 0.574 (CoV 0.028 / 0.076) (§5.2, p. 14–15; Fig. 8, p. 15). The trilinear model in Fig. 8 is labelled "Meng et al., 2017".

## Mechanisms / explanations offered by authors
- Higher W/B lowers the fiber/matrix bond and friction → more slip, lower cracking and peak stress, higher strain (§3.1.1–3.1.2, p. 5–6; §3.2, p. 7).
- Lower W/B raises bond → fibers rupture rather than pull out → less ductility (§3.2, p. 7, citing Li 2002/2003/2004).
- More fibers spread cracks to more sections → more slip → higher strain; fibers mainly improve ductility, not peak stress (§3.1.2, §3.2).
- Damage: fibers bridge cracks so the damage rate falls during hardening (d′ > 0, d″ < 0) and rises during softening (d′ > 0, d″ > 0) (§4.2, p. 11).

## Limitations (stated + observed)
- Stated: few specimens and narrow parameter ranges; model needs repeated/cyclic loading; application to real structures needed (Conclusion 5, p. 16).
- Observed:
  - No f'c, no crack width, no crack count reported.
  - Damage factor uses arctan of a dimensional quantity (σ/ε), so its value depends on units. The paper does not state them; the recomputation above shows MPa and % were used. The coefficients only apply in those units.
  - Eq. 19 (p. 11) printed as kb(b−1)(ε−ε_k), apparently missing the exponent (b−2) ⚠️ (confirmed in the PDF).
  - Table 4 V3R2 B and C do not follow from Eqs. 14–15 (see above).
  - Model is empirical, fitted to one matrix and to v 1–2%, W/B 0.24–0.28; validation uses the same group's tests.
  - V3R1 has only 3 specimens; high scatter in ε_p (SD up to 0.35%).
  - §3.1.4 (p. 7) contradicts itself on PE-ECC ("unlike PE-ECC (whose energy dissipation capacity increased with increasing water-binder ratio)") — confirmed in the PDF.
  - Test age not stated exactly (≥ 35 d).

## Relation to other work
- Agrees with: higher W/B → lower strength, higher ε_tu ([[chai2023-hdc-ambient-temperature]] W/B 0.20–0.31 screening; [[water-binder-ratio]]); bond too strong → rupture ([[li2002-pva-ecc-interface-tailoring]]).
- Contradicts: ⚔️ fiber content barely changes σ_p (3.10 / 2.96 / 3.23 MPa at 1 / 1.5 / 2%), whereas bridging models predict σ0 rising linearly with Vf ([[jin2019-hvfa-shcc-structural]], Fig. 1a; [[yang2008-ecc-fiber-bridging-law]]). Possibly first-crack/flaw-controlled or partial rupture; not explained by the authors.
- Extends: [[tensile-constitutive-model]] — a continuous nonlinear (damage-based) alternative to the trilinear model of [[yang2024-hshdc-uniaxial-tension]] and the bilinear model of [[chai2023-hdc-ambient-temperature]], with a measured advantage in FE.

## Pages updated from this source
- [[tensile-constitutive-model]] · [[tensile-strain-capacity]] · [[tensile-toughness]] · [[water-binder-ratio]] · [[fiber-geometry]]
- [[pva-fiber]] · [[fly-ash]] · [[dogbone-uniaxial-tension]] · [[multiple-cracking]] · [[rc-member-strengthening]]
- [[mix-designs]] · [[mechanical-results]] · [[li2002-pva-ecc-interface-tailoring]]

## To verify
- [x] Units used in θ = arctan(σ/ε) — resolved 2026-10-21 by recomputing Table 4 from Eqs. 13–15: σ in MPa, ε in %, radians.
- [ ] Table 4 V3R2 B (−0.090) and C (0.108) vs recomputed −0.171 / 0.172.
- [ ] Eq. 19 exponent (b−1 vs b−2) — PDF confirms the printed form; likely typo.
- [ ] Exact test age (28 d lime water + drying + 7 d epoxy cure).
- [ ] Cement grade, FA class, sand size, SP basis (confirmed not reported in the PDF).
- [ ] Whether Table 1 ratios are by mass (no unit printed).
- [ ] Text in §3.1.4 on PE-ECC W/B effect (self-contradictory sentence, confirmed in PDF).
- [ ] Gauge length L_g used in G_f (assumed 120 mm extensometer; Eq. 2 defines L_g only as "gauge length").
