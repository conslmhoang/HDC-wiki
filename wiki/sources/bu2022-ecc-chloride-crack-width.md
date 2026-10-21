---
type: source
slug: bu2022-ecc-chloride-crack-width
title: "Time and Crack Width Dependent Model of Chloride Transportation in Engineered Cementitious Composites (ECC)"
authors: [Linglai Bu, Lei Qiao, Renjuan Sun, Wei Lu, Yanhua Guan, Nan Gao, Xinlei Hu, Zhenhuan Li, Lin Wang, Yuhe Tian, Yu Qin]
year: 2022   # Materials 15(16), 5611; received 26 May 2022, accepted 11 Aug 2022, published 16 Aug 2022 (p. 1)
venue: "Materials (MDPI), Vol. 15, Issue 16, Article 5611 (2022), 13 pp. Affiliations: School of Qilu Transportation, Shandong University (corresponding: R. Sun, Y. Guan); Shandong High-Speed Engineering Construction Group; Jining Construction Project Quality and Safety Technology Center; Chongqing Luneng Development (Group). Funding: Natural Science Foundation of Shandong Province ZR2021ME215 (p. 11)"
doi: "10.3390/ma15165611"
raw_file: raw/papers/Bu2022_ECC-chloride-crack-width.pdf
material_term: "ECC (engineered cementitious composites), PVA fibre (Kuraray), 2.0 vol.% (26 kg/m³ at 1.3 g/cm³), FA/C 1.2, W/B 0.26. No tensile, compressive or crack-width-under-load test reported, so strain hardening of this mix is not shown. Curing: 95% RH, 20 ± 2 °C, 28 d."
study_type: "experimental + empirical modelling (immersion of artificially notched ECC prisms in 3.5% NaCl for 30-120 d; free-chloride profiles; regression model on Fick's second law)"
tags: [experimental, model, ecc, pva-fiber, fly-ash, chloride, diffusion, crack-width, fick-second-law, surface-chloride, time-dependent-diffusion]
ingested: 2026-10-20
updated: 2026-10-21
---

# Time- and crack-width-dependent chloride transport model for ECC (Bu et al., 2022)

> Re-checked against the publisher PDF on 2026-10-21 (page numbers added; per-mix fit constants and
> figure read-offs added from Figs. 2, 4, 7, 8).

## One-paragraph summary
Shandong University study of chloride ingress in PVA-**ECC** with **artificial cracks** (notches 25 mm deep
cast with thin steel sheets) of width **0, 0.1, 0.2 and 0.3 mm**, in 53 × 40 × 35 mm prisms immersed in 3.5%
NaCl for 30, 60, 90 and 120 d (48 specimens) (pp. 2–3, Table 3). Free chloride profiles to 30 mm depth were
measured with an ion-selective electrode and fitted with the erf solution of Fick's second law. **0.1 mm
(100 µm) notches gave no significant difference from uncracked ECC**; the crack effect became significant
**at ≥ 0.2 mm**: surface free chloride (0–2 mm) +8.7% / +14.9% (0.2 / 0.3 mm) at 30 d and +17.4% / +29.4% at
120 d vs uncracked (p. 4, Sect. 3). Surface chloride follows C_s = a(1 − e^(−bt)) with b ≈ 0.03375 (t in d)
and a = 0.49359w + 0.47297 (Eqs. 6–8, pp. 6–7); apparent D follows D(t′) = D28(28/t′)^n with D28 ≈ 35.5 ×
10⁻¹² m²/s (independent of crack width) and n = −1.0976w + 1.8948 (Eqs. 10–12, pp. 8–9). Per the text, D fell
about 50% from 30 to 60 d, 30% from 60 to 90 d and 5% from 90 to 120 d (p. 8). The combined model predicts
most data within 20%, but over-predicts beyond about 22.5 mm depth for 0.2–0.3 mm cracks (p. 10, Sect. 3.1.4).

## Objective / research question
- Build a chloride transport model for ECC that accounts for both exposure time and crack width
  (p. 1, Abstract), focusing on crack widths > 0.1 mm, which are less studied (p. 2, Sect. 1).

## Materials & mix design
Table 1 (kg/m³) and Table 2 (fibre), p. 2.

| Mix ID | Cement | Fly ash | Slag/other | Sand (type, max size) | W/B | SP | Fiber type | L (mm) | d (µm) | Vf (vol.%) |
|---|---|---|---|---|---|---|---|---|---|---|
| ECC | 568 (P.O. 42.5) | 682 (Class F) | HPMC 0.5 | 455, quartz sand 120–180 µm | 0.26 (325/(568+682), computed here; by mass) | 10 (polycarboxylate) | PVA (Kuraray), 1.56 GPa, 41 GPa, elongation 6.5%, 1.3 g/cm³ | 12 | 40 | 2.0 (26 kg/m³ ÷ 1.3 g/cm³, computed here) |

Units of binder quantities: kg/m³. FA/C = 1.20 by mass (computed). Fresh density 2066.57 kg/m³ (Table 1 total,
p. 2; equals the sum of the listed ingredients).

## Test methods
- Specimen geometry: 53 × 40 × 35 mm prisms; one artificial crack along the centre line of the
  53 × 40 mm face, 25 mm deep, made by inserting a thin steel sheet into fresh ECC (pp. 2–3, Sect. 2.2, Fig. 1).
  Five faces epoxy-coated; cracked face exposed.
- Loading / rate: none (no mechanical pre-cracking).
- Measurement: specimens cut, sliced (slices about 10 mm wide, 2 mm thick) at 0–2, 2–4, 4–7, 7–10, 10–15,
  15–20, 20–25, 25–30 mm along the crack depth; powder < 0.3 mm, oven-dried 60 °C 24 h, 2 g in 200 mL water,
  30 min stirring; free chloride by NELD-CL420 ion-selective electrode (p. 3, Sect. 2.3). Three specimens per
  case; mean used. ANOVA F-test (p. 4, Sect. 2.4).
- Exposure: full immersion in 3.5% (by mass) NaCl, 30 / 60 / 90 / 120 d (p. 3, Table 3).
- Curing & test age: 28 d at 95% RH, 20 ± 2 °C before exposure (pp. 2–3, Sect. 2.2).
→ [[chloride-and-corrosion]]

## Key results
| Mix ID | f'c (MPa) | First-crack stress (MPa) | Tensile strength (MPa) | Tensile strain capacity (%) | Crack width (µm) | Other |
|---|---|---|---|---|---|---|
| CW-0 | not reported | not reported | not reported | not reported | 0 (uncracked) | reference profile; C_s fit a = 0.48272, b = 0.03431; D28 = 37.71, n = 1.894 |
| CW-1 | not reported | not reported | not reported | not reported | 100 (artificial notch) | profile ≈ CW-0 ("no significant difference"); a = 0.50458, b = 0.03455; D28 = 35.09, n = 1.791 |
| CW-2 | not reported | not reported | not reported | not reported | 200 (notch) | C at 0–2 mm +8.7% (30 d), +17.4% (120 d) vs CW-0; a = 0.57796, b = 0.03309; D28 = 33.76, n = 1.665 |
| CW-3 | not reported | not reported | not reported | not reported | 300 (notch) | C at 0–2 mm +14.9% (30 d), +29.4% (120 d); +66.9% at 0–2 mm and +46.9% at 2–4 mm from 30 to 120 d; a = 0.62279, b = 0.03355; D28 = 35.45, n = 1.571 |

a, b: Fig. 4 legend (p. 6); D28 (10⁻¹² m²/s) and n: Fig. 8 legend (p. 9). Mean of the four D28 values = 35.50,
matching the stated 35.5 (computed here).

Main findings (with page/Table/Fig. location):
- Free chloride falls steeply in the first 10 mm and gently beyond 15 mm; rises with time at every depth
  (p. 4, Sect. 3; Fig. 2, p. 5). Read from Fig. 2 (p. 5), free chloride (% — basis not stated) in the 0–2 mm
  slice: 30 d CW-0 ≈ 0.30, CW-1 ≈ 0.31, CW-2 ≈ 0.33, CW-3 ≈ 0.35; 120 d CW-0 ≈ 0.45, CW-1 ≈ 0.46,
  CW-2 ≈ 0.53, CW-3 ≈ 0.58. At 25–30 mm: ≈ 0.04–0.05 for all at 30 d; at 120 d CW-0/CW-1 ≈ 0.04,
  CW-2 ≈ 0.06, CW-3 ≈ 0.09.
- **Crack-width threshold for immersion**: CW-1 (0.1 mm) ≈ CW-0; effect "significant … when it is above
  0.2 mm" (p. 1, Abstract; p. 4, Sect. 3; p. 11, Conclusions). → [[crack-width]]
- **Surface chloride**: C_s = (0.49359w + 0.47297)(1 − e^(−0.03375t)); fitted b 0.033–0.035 (per-mix
  0.03309–0.03455, Fig. 4 legend), mean 0.03375 used; per-mix fits R² 0.961–0.999 (Fig. 4, p. 6); a vs w linear,
  R² 0.9642 (Eq. 7, Fig. 5, p. 7). w in mm (Fig. 5 axis), t in days (Fig. 4 axis). Fitted C_s (Fig. 4, p. 6,
  read): CW-0 ≈ 0.33 (30 d) → ≈ 0.48 (120 d); CW-3 ≈ 0.40 → ≈ 0.63. ANOVA: time F = 73.6, crack width F = 32.4,
  p ≈ 1.2 × 10⁻⁶ and 3.8 × 10⁻⁶ (Table 4, p. 7). C_s unit is "%"; basis (binder or powder mass) not stated ⚠️.
- **Apparent D**: decreases with time; text: about −50% 30→60 d, −30% 60→90 d, −5% 90→120 d (p. 8,
  Sect. 3.1.3). Read from Fig. 7 (p. 8), D (10⁻¹² m²/s): 30 d CW-0 ≈ 9.6, CW-1 ≈ 9.7, CW-2 ≈ 10.2, CW-3 ≈ 11.5;
  60 d ≈ 3.8 / 3.9 / 4.4 / 5.3; 90 d ≈ 2.5 / 2.7 / 3.1 / 3.7; 120 d ≈ 1.9 / 2.0 / 2.4 / 2.9.
  ⚠️ These bars imply ≈ −45 to −60% (30→60 d), ≈ −30% (60→90 d) and ≈ −20 to −25% (90→120 d), so the
  text's "5%" for 90→120 d does not match Fig. 7 (observed; see Limitations).
- D28 not significantly affected by crack width; average 35.5 × 10⁻¹² (printed "m/s²", p. 8; figure axes
  give 10⁻¹² m²/s, so m²/s is meant). n decreases with crack width by 5.4% / 12.1% / 17.1% (0.1 / 0.2 / 0.3 mm)
  relative to CW-0 (Fig. 8 legend values 1.894 → 1.791 / 1.665 / 1.571 reproduce these percentages),
  fit n = −1.0976w + 1.8948, R² 0.9971 (Eq. 11, p. 8; Fig. 9, p. 9). ANOVA: time F = 1487, crack width F = 44.8
  (Table 5, p. 10). Predicted vs measured D agree closely (Fig. 10, p. 10).
- t′ in Eqs. 9–12 is concrete **age**: Fig. 8 data sit at 28/t′ ≈ 0.48, 0.32, 0.24, 0.19, i.e. t′ ≈ 58, 88,
  118, 148 d = exposure + 28 d curing (interpreted from Fig. 8, p. 9).
- **Model** (Eq. 13, p. 10): most predictions within ±20%; good when C > 0.15%; over-predicts at > 22.5 mm depth
  for 0.2–0.3 mm cracks because profiles had not reached the asymptote at 30 mm (p. 10, Sect. 3.1.4; Fig. 11,
  p. 11, where many points below ≈ 0.1% fall outside the −20% line).

Second-hand statements in the Introduction (as cited):
- ECC crack width "generally not exceeding 80 µm" (refs. [7,8], p. 1, Sect. 1).
- D of ECC is about 10–35% of that of concrete of the same strength (Sahmaran 2011, ref. [13], p. 1).
- Average crack width should be < 100 µm for durability (Ma et al. 2021 = [[ma2021-ecc-durability-review]], p. 2).
- No significant difference in effective D for crack widths 10–50 µm (Şahmaran & Li 2009, ref. [28], p. 2).
- Resistance of cracked ECC to chloride is governed by **accumulated** (total) crack width rather than the
  maximum one (refs. [29,30], p. 2 — Samaha & Hover 1992, ACI Mater. J.; Wang et al. 1997, Cem. Concr. Res.;
  both are concrete papers, per the reference list p. 12).
- Upper and lower crack-width thresholds exist for chloride ingress in concrete (refs. [29–32], p. 3); values not given.

## Mechanisms / explanations offered by authors
- C_s growth slows with time because of continued hydration, fly ash pozzolanic reaction and chloride
  binding densifying pores (p. 6, Sect. 3.1.2).
- D falls with time due to densification by chloride reaction products and continued hydration; fewer
  reactive phases remain later (p. 8, Sect. 3.1.3).
- D28 independent of crack width because early ingress is driven by capillary suction (p. 8, ref. [38]).
- Wider cracks lower the ageing exponent n, i.e., D decreases more slowly with time (Eq. 11, p. 8).

## Limitations (stated + observed)
- Stated: depth beyond 30 mm not measured; model over-predicts deep chloride for 0.2–0.3 mm cracks (p. 10).
- Observed: **cracks are cast notches** (smooth, straight, fixed width, fully open, no fibre bridging,
  no tortuosity, no self-healing of fresh fracture surfaces), not mechanically induced multiple cracks;
  single crack per specimen. Results may not transfer to real ECC crack patterns.
- Observed: no mechanical data; strain-hardening of the mix is not demonstrated.
- Observed: only one crack width ≤ 0.1 mm tested, so the threshold lies somewhere between 0.1 and 0.2 mm;
  sub-100 µm behaviour (the typical ECC range) is untested.
- Observed: immersion only (diffusion-dominated); no wet–dry cycling.
- Observed: n values 1.57–1.89 (Fig. 8 legend, p. 9) are unusually high for the ageing exponent (typical
  concrete values are well below 1 [general knowledge — needs source]); fitted over only 4 ages (58–148 d).
- Observed: unit typo "m/s²" for D28 (p. 8); text says "Compared with CW-1, the value of n for specimen
  CW-1…" (p. 8), which from the Fig. 8 values means CW-0; "PVC fiber" typo for PVA (p. 2, Sect. 2.1);
  "JP-0…JP-3" legend remnants in Fig. 7 (p. 8).
- Observed: text decline rates of D (50 / 30 / 5%) do not match the Fig. 7 bars for 90→120 d (≈ 20–25%).
- Observed: chloride content reported as "%" without stating the mass basis.

## Relation to other work
- Agrees with: [[vanzijl2010-shcc-durability]] ("about 100 µm" chloride threshold, as cited there from
  Sahmaran 2007): here ≤ 0.1 mm ≈ uncracked under immersion. Agrees with Şahmaran & Li 2009 (as cited) that
  10–50 µm makes no significant difference.
- Contradicts: ⚔️ the wiki threshold "55–80 µm: chloride ingress becomes significant (Jang 2011)" as cited in
  [[he2024-hdc-research-advances]] — here 100 µm notches were not significant, threshold 100–200 µm (immersion,
  artificial cracks). ⚔️ [[paul2014-r-shcc-chloride-corrosion]] (wet–dry capillary exposure, real flexural
  cracks): 50–100 µm cracks carried chloride 65–89 mm deep in hours. Likely reason: transport mode (diffusion
  under immersion vs capillary suction under wet–dry) and crack type (cast notch vs real crack).
- Extends: first wiki source with a quantitative time- and crack-width-dependent chloride model for ECC.

## Pages updated from this source
- [[crack-width]] · [[durability]] · [[permeability]] · [[chloride-and-corrosion]] · [[fly-ash]] · [[pva-fiber]] · [[ma2021-ecc-durability-review]] · [[gaps]]

## To verify
- [ ] Mass basis of C and C_s ("%", p. 6) — not stated in the PDF.
- [ ] Text "5%" decrease of D from 90 to 120 d (p. 8) vs ≈ 20–25% read from Fig. 7.
- [ ] n = 1.57–1.89: very high for an ageing exponent (values confirmed from Fig. 8 legend; physical plausibility open).
- [x] Unit of w = mm: confirmed by Fig. 5 and Fig. 9 axes "Crack width (mm)" (pp. 7, 9).
- [x] D28 = 35.5 × 10⁻¹² m²/s: printed "m/s²" (p. 8) but Figs. 7–8 axes are 10⁻¹² m²/s; mean of the four Fig. 8 D28 values = 35.50.
- [x] "Compared with CW-1" (p. 8) means CW-0: n from Fig. 8 legend gives −5.4 / −12.1 / −17.1% relative to CW-0 (1.89419).
- [x] Vf 2.0 vol.% computed from 26 kg/m³ and 1.3 g/cm³ (both in Tables 1–2, p. 2).
- [x] Refs. [29,30] are concrete papers (reference list, p. 12).
