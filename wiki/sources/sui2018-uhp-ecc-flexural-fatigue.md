---
type: source
slug: sui2018-uhp-ecc-flexural-fatigue
title: "Flexural Fatigue Properties of Ultra-High Performance Engineered Cementitious Composites (UHP-ECC) Reinforced by Polymer Fibers"
authors: [Lili Sui, Qianli Zhong, Kequan Yu, Feng Xing, Pengda Li, Yingwu Zhou]
year: 2018   # Polymers 10(8), article 892; published 9 Aug 2018 (received 21 Jun, accepted 7 Aug 2018)
venue: "Polymers (Basel) 10(8), 892 (2018), MDPI; open access CC BY"
doi: "10.3390/polym10080892"
raw_file: raw/papers/Sui2018_UHP-ECC-flexural-fatigue.xml
material_term: "UHP-ECC (ultra-high performance engineered cementitious composite), PE fibre; f'c about 120 MPa, σ_tu up to 12 MPa, ε > 8% (abstract)"
study_type: "experimental (four-point bending static + constant-amplitude flexural fatigue, DIC, ESEM) + empirical S–N model"
tags: [uhp-ecc, pe-fiber, fatigue, four-point-bending, s-n-curve, dic, crack-width, ggbs, silica-fume, limestone-powder]
ingested: 2026-10-20
updated: 2026-10-20
---

# Flexural Fatigue of PE UHP-ECC (Sui et al., 2018)

## One-paragraph summary
Shenzhen University / HK PolyU test a PE-fibre UHP-ECC (2 vol.% PE, OPC + GGBS + SF + limestone powder,
W/B about 0.14) in four-point bending on 100 × 100 × 400 mm beams at fatigue stress levels S = 0.5, 0.65, 0.8 and
0.9 (σ_min/σ_max = 0.2, 8 Hz, run-out at 2 × 10⁶ cycles; 3 beams per level) after 90 d curing (Sect. 2.2–2.4).
Static flexural strength is about 22 MPa with > 10 mm mid-span deflection. Fatigue lives (Table 6): all S = 0.5
beams survive 2 × 10⁶ cycles; S = 0.65 → 155,075–308,691; S = 0.8 → 21,852–29,565; S = 0.9 → 1271–1876.
After 2 × 10⁶ cycles at S = 0.5, residual flexural strength is 86% of static and initial stiffness falls
130.01 → 108.12 kN/mm (Table 4). A continuous S–N law is fitted: **S = 1 − 5.75 × 10⁻³ (lg N)^2.43** (Eq. 2).
The pull-out/rupture area ratio on fracture surfaces rises with S. The authors conclude the high-strength matrix
does not reduce fatigue life. → [[fatigue]]

## Objective / research question
- Determine the flexural fatigue life of UHP-ECC at four stress levels; the fatigue of high-strength/high-ductility
  ECC had not been studied (Introduction).
- Monitor mid-span deflection, bottom COD, crack width and number, dissipated energy; observe fibre morphology (ESEM).
- Establish an S–N equation without the inflection point of existing bilinear models (Sect. 4).

## Materials & mix design
Table 1 (kg/m³):

| Mix ID | Cement | Fly ash | Slag/other | Sand (type, max size) | W/B | SP | Fiber type | L (mm) | d (µm) | Vf (vol.%) |
|---|---|---|---|---|---|---|---|---|---|---|
| UHP-ECC | 700 (OPC 52.5R) | 0 | GGBS 750; SF 150; limestone powder 100 | quartz sand 500, mean 100 µm, max 181 µm | 0.144 by mass excl. LP (230/1600), 0.135 incl. LP (computed here) | HRWR (PCE, liquid) 30 | UHMWPE | 12 (computed here from aspect ratio 480 × 25 µm) | 25 | 2 (20 kg/m³) |

Units: kg/m³. Water 230 kg/m³. PE fibre (Table 3): d 25 µm, aspect ratio 480, σ_f 2.9 GPa, E 116 GPa, rupture
elongation 2.42%, density 970 kg/m³. Cement 28 d strength 61.9 MPa, Blaine 380 m²/kg (Table 2). LP acts as filler and
is said to accelerate C₃S hydration and form carboaluminates (Sect. 2.1). → [[pe-fiber]], [[ggbfs]], [[silica-fume]]

## Test methods
- **Uniaxial tension:** 3 dog-bones (dimensions only in Fig. 3), 2 LVDTs over the gauge; crack widths by crack-width
  gauge at set displacements (Sect. 2.2, Fig. 3–5). Loading rate not reported in text. → [[dogbone-uniaxial-tension]]
- **Compression:** 100 mm cubes, 6 per batch, 28 d and 90 d (Sect. 2.2). → [[compressive-strength]]
- **Flexure / fatigue:** 15 beams 100 × 100 × 400 mm; four-point bending, support span 300 mm, load points 100 mm apart;
  250 kN MTS; static at 1 mm/min (displacement control); fatigue load-controlled sinusoid 8 Hz, σ_min = 0.2 σ_max;
  S = σ_max / f_a (mean static flexural strength); stopped at failure or 2 × 10⁶ cycles; 3 LVDTs for deflection,
  1 LVDT for bottom COD over the pure-bending zone; crack observation microscope (Sect. 2.3–2.4, Fig. 6).
- **DIC:** VIC-3D on static beam U-1.0-3 and fatigue at S = 0.8 (Fig. 9, 14). → [[digital-image-correlation]]
- **ESEM** of fibres from pull-out and rupture zones; samples oven-dried 50 °C for 2 d (Sect. 3.2.1).
- **Curing & test age:** demould at 1 d ("second day"), standard room 95% RH, 20 ± 2 °C, **90 d** for all beams.

## Key results
| Mix ID | f'c (MPa) | First-crack stress (MPa) | Tensile strength (MPa) | Tensile strain capacity (%) | Crack width (µm) | Other |
|---|---|---|---|---|---|---|
| UHP-ECC | 102.8 (28 d, SD 1.1); 120.7 (90 d, SD 0.75), 100 mm cubes | not reported | "up to 12" (abstract; Fig. 4 only) | "> 8" (abstract; Fig. 4 only; age not stated) | < 160 in tension (Fig. 5) | static flexural strength about 22 MPa, mid-span deflection > 10 mm (90 d) |

Table 6 fatigue results (90 d):

| S | Fatigue life N | Max mid-span deflection (mm) | Max bottom deformation (mm) |
|---|---|---|---|
| 0.5 | > 2,000,000 (×3, run-out) | 0.98–1.03 | 1.61–1.96 |
| 0.65 | 308,691 / 155,075 / 277,386 | 1.41–1.86 | 2.64–2.83 |
| 0.8 | 29,565 / 26,291 / 21,852 | 3.02–3.68 | 3.13–3.97 |
| 0.9 | 1569 / 1876 / 1271 | 4.81–4.94 | 4.37–5.21 |

Table 5 average crack count: static 45; S = 0.9 → 30; 0.8 → 20; 0.65 → 6; 0.5 → 5 before, 25 after static reloading.

Table 4 initial stiffness (secant to 40% of ultimate load): static U-1.0 mean 130.01 kN/mm (115.00–145.45);
after 2 × 10⁶ cycles at S = 0.5 mean 108.12 kN/mm (98.26–117.76).

Main findings:
- Static DIC (U-1.0-3): first crack at 58% of ultimate (40 kN), 18 cracks at 72% (50 kN), peak 69 kN, saturation
  near deflection/span 1/30 (62 kN post-peak) (Fig. 9).
- Fatigue at S = 0.8 (DIC): first cracks at 30 cycles, 9 cracks at 200 cycles and no further growth in number; main
  crack later (Fig. 14; caption says 20,000 cycles, text says 200,000 ⚠️).
- Deflection/COD evolve in 2 stages at S = 0.5 and 3 stages (rapid, stable, unstable) at S ≥ 0.65; fatigue life is
  governed by the length of stage II (Fig. 13, Sect. 3.2.2).
- Dissipated energy per cycle rises slowly with cycle ratio, slightly faster at higher S (Fig. 18).
- Residual flexural strength after 2 × 10⁶ cycles at S = 0.5 is 86% of static; authors state the specimens "can still
  have a tensile strain capacity of more than 3%" (Sect. 3.1) ⚠️ (inferred from a flexural test).
- S–N: Eq. 2, S = 1 − 5.75 × 10⁻³ (lg N)^2.43 (gives S ≈ 0.50 at 2 × 10⁶, computed here). The inflection stress level
  of existing bilinear models (about 0.9, N 10²–10⁴) matches the inflection of the tensile crack-width-vs-strain curve,
  i.e. a critical crack width (Fig. 19–20).
- UHP-ECC fatigue performance is "not inferior" to ordinary ECC (Fig. 19).

## Mechanisms / explanations offered by authors
- **Fracture surface zoning:** pull-out zone (A1) near the compression side, rupture zone (A2) near the tension face;
  A1/A2 rises with S → high fatigue stress mainly degrades the bond, low fatigue stress mainly damages fibres
  (Fig. 10). → [[fiber-matrix-interface]], [[fiber-bridging]]
- Pulled-out PE fibres become scratched and flattened (round → flat) as S rises (plastic deformation); ruptured fibres
  show tearing and "wire drawing" (Fig. 11–12).
- Stiffness loss after fatigue: tension-zone fibre failure shifts from rupture (static) to pull-out (bond-slip) (Sect. 3.2.2).
- **PVA vs PE (literature comparison):** PVA-ECC has longer life at high S (stronger bond, better crack-width control),
  PE-ECC longer at low S where fibre rupture dominates and PE has better fatigue resistance (Sect. 4, Conclusion 3).

## Limitations (stated + observed)
- Stated: very limited data to quantify the S–N inflection point (Sect. 4).
- Observed: 3 beams per level, one mix; tensile properties only as figures (no tabulated σ_tu/ε_tu, no test age for
  tension); dog-bone dimensions only in a figure; no tensile fatigue; frequency fixed at 8 Hz, R = 0.2.
- Observed: Table 6 labels all three S = 0.65 beams "U-0.65-1" (typo); Fig. 14 caption (20,000 cycles) vs text
  (200,000 cycles) disagree; "tensile strain capacity > 3%" after fatigue is not measured directly.
- Observed: the paper does not state how the S = 0.5 run-outs (no failure at 2 × 10⁶) enter the Eq. 2 regression ⚠️.

## Relation to other work
- Agrees with: Suthiwarapirak et al. 2004 (as cited, Table 7): PVA-ECC better than PE-ECC at high S, worse at low S.
  The S–N law is the "Sui 2018" model tabulated in [[ma2021-ecc-durability-review]] (Table 4) — same equation.
- Contradicts: ⚔️ none found. Crack width < 160 µm in tension matches the 80–200 µm range of PE-based HSHDC in
  [[crack-width]] / [[gaps]], i.e. above the < 100 µm quoted for PVA-ECC (Introduction, as cited).
- Extends: first primary fatigue data in the wiki and the first for a high-strength PE ECC; f'c 120.7 MPa places it
  in the HSHDCC class of [[zhang2022-hshdcc-review]] (> 100 MPa, > 3%), which lists UHP-ECC as a member ([[hshdc]]).
  Co-author K.Q. Yu belongs to the UHDC/UHP-ECC lineage ([[uhdc]]) ⚠️ affiliation link not stated in this paper.

## Pages updated from this source
- [[fatigue]] · [[pe-fiber]] · [[hshdc]] · [[uhdc]] · [[flexural-strength]] · [[crack-width]] · [[multiple-cracking]] ·
  [[fiber-matrix-interface]] · [[fiber-bridging]] · [[digital-image-correlation]] · [[compressive-strength]] ·
  [[ggbfs]] · [[silica-fume]] · [[mix-designs]] · [[mechanical-results]] · [[terminology-hdc-ecc-shcc]]

## To verify
- [ ] Tensile σ_tu (about 12 MPa) and ε_tu (> 8%) are only in the abstract and Fig. 4; test age for the dog-bones not stated ⚠️ unverified.
- [ ] Dog-bone geometry and tensile loading rate (Fig. 3 only).
- [ ] Fig. 14 caption 20,000 vs text 200,000 cycles for main-crack formation at S = 0.8.
- [ ] How run-out specimens (S = 0.5) were treated in the Eq. 2 regression.
- [ ] Fibre length 12 mm is computed from aspect ratio 480 and d = 25 µm, not stated.
- [ ] Whether W/B includes limestone powder (not defined by the authors).
