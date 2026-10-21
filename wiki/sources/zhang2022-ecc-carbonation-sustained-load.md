---
type: source
slug: zhang2022-ecc-carbonation-sustained-load
title: "Carbonation Behavior of Engineered Cementitious Composites under Coupled Sustained Flexural Load and Accelerated Carbonation"
authors: [Hongzhi Zhang, Yingxuan Shao, Ning Zhang, Abdullah M. Tawfek, Yanhua Guan, Renjuan Sun, Changjin Tian, Branko Šavija]
year: 2022   # Materials 15, 6192; received 26 Jul 2022, accepted 30 Aug 2022, published 6 Sep 2022 (p. 1)
venue: "Materials (MDPI) 2022, 15(18), 6192, 16 pp. Open access, CC BY 4.0. PMCID PMC9504410, PMID 36143512 (from the Europe PMC record). Shandong University (corresponding authors Y. Guan, R. Sun); TU Delft Microlab (B. Šavija). Funding: NSFC 52008234, 51978387; Taishan Scholars tsqn201909032; NSF Jiangsu BK20200235; NSF Shandong ZR2021QE174, ZR2021ME215 (p. 13)"
doi: "10.3390/ma15186192"
raw_file: raw/papers/Zhang2022_ECC-carbonation-sustained-load.pdf
material_term: "ECC (engineered cementitious composites; authors note the synonyms SHCC and UHTCC, p. 1). PVA-ECC mix from earlier Shandong University work (refs. 11, 25: Guan et al. 2021 KSCE J. Civ. Eng.; Sun et al. 2020 Constr. Build. Mater.). Tensile strain hardening is NOT tested here; only 'typically beyond 3%' is stated generically (Abstract, p. 1). Measured: 4-pt flexural first-cracking 7.41 MPa and ultimate 11.41 MPa (p. 3, §2.2)."
study_type: "experimental (accelerated carbonation GB/T 50082-2009 under sustained four-point flexural load; phenolphthalein depth; TG/DTG; XRD; MIP; Vickers microhardness; empirical carbonation-depth model)"
tags: [ecc, pva-fiber, fly-ash, durability, carbonation, sustained-load, coupled-loading, mip, tga, xrd, microhardness, carbonation-model, shandong-university]
ingested: 2026-10-20
updated: 2026-10-21
---

# ECC carbonation under sustained flexural load (Zhang et al., 2022)

> Re-checked against the publisher PDF on 2026-10-21 (page numbers added; per-period Fig. 4 fits, Fig. 7
> CO₂ values, Fig. 10 pore-class values and Fig. 11 microhardness read-offs added; Eq. 7 typo resolved by
> computation).

## One-paragraph summary
Shandong University and TU Delft carbonated 400 × 100 × 50 mm PVA-ECC prisms (C 563, FA 676, W/B 0.30,
PVA 26 kg/m³; Table 1, p. 3) for 7, 14 and 28 d at 20% CO₂ while holding them under sustained four-point
bending at 30% or 60% of the ultimate flexural load (11.41 MPa), i.e. below the first-cracking stress
(7.41 MPa) (pp. 3–4, §2.2–2.4). Cutting at four positions along the span gave flexural tensile stress levels
δ_T = 0–0.6 of flexural strength (Table 3, p. 4). Unstressed carbonation depth was **2.30 / 3.37 / 4.78 mm**
at 7 / 14 / 28 d; at δ_T = 0.6 it was **7.21 / 8.16 / 9.92 mm** (Table 4, p. 7). The stress influence
coefficient K_ks (= x_σ / x_0) rose with δ_T but at a **decreasing rate** (not linear as for plain concrete),
and fell with exposure time (3.135 at 7 d → 2.075 at 28 d for δ_T 0.6). The authors fit K_ks = 1 + y_a·δ_T^{y_b}
with time-dependent y_a, y_b (Eqs. 5–9, pp. 7–8). TG/DTG/XRD show CH consumed first, then ettringite and C-S-H;
CO₂ bound ≈16 wt.% in the outer 0–4 mm (Fig. 7, p. 10). MIP: carbonation refined 0.1–10 µm pores; sustained
load added only a few > 10 µm pores, attributed to fiber bridging (pp. 10–12, §3.4). Microhardness was
> 100 HV in the carbonated skin vs 60–80 HV inside (p. 12, §3.5).

## Objective / research question
- Quantify how sustained flexural tensile stress changes ECC carbonation depth with time, and propose a
  depth model that includes stress level (p. 2, §1, last para).
- Explain the change via phase assemblage, pore structure and micro-hardness along the carbonation profile (p. 2).
- Motivation: little is known about carbonation of hardened ECC (most work is carbonation curing), and
  high-FA binders have less portlandite (p. 2, §1).

## Materials & mix design
- OPC 42.5 I; Class F fly ash (oxides Table 2, p. 3: cement CaO 63.21, SiO₂ 18.48, Al₂O₃ 6.74 wt.%; fly ash
  SiO₂ 49.66, Al₂O₃ 35.97, Fe₂O₃ 5.77, CaO 3.43 wt.%); quartz sand 125–180 µm; Kuraray PVA (dimensions and
  properties not reported); PCE superplasticizer; VMA (pp. 2–3, §2.1).

| Mix ID | Cement | Fly ash | Slag/other | Sand (type, max size) | W/B | SP | Fiber type | L (mm) | d (µm) | Vf (vol.%) |
|---|---|---|---|---|---|---|---|---|---|---|
| ECC (SDU mix, refs. 11, 25) | 563 | 676 | VMA 4.50 | quartz sand 450, 125–180 µm (0.18 mm max) | 0.30 (water 372) | 5.58 | PVA (Kuraray) | not reported | not reported | 26 kg/m³ (≈ 2.0 if ρ = 1.3 g/cm³ — density not given in this paper ⚠️) |

Units of binder quantities: kg/m³ (Table 1, p. 3). FA/C = 676/563 = 1.20 by mass (computed here);
372/(563 + 676) = 0.300 (computed) matches the stated W/B 0.30.

## Test methods
- Specimen geometry: prisms 400 × 100 × 50 mm; four-point bending, span 300 mm, loading points 100 mm
  apart (third-point; Fig. 1, p. 4) (pp. 2–3, §2.1–2.2).
- Loading / rate: flexural capacity on a 10 kN machine at 0.4 mm/min, LVDT mid-span, mean of 3 (p. 3, §2.2).
  Sustained load in a bolted three-specimen rig (plates 30 mm, threaded pillars Ø20 mm, steel cylinders Ø20 mm)
  with load cell, re-tightened every 24 h, laid horizontally in the chamber; side faces epoxy-sealed (p. 3,
  §2.3; Fig. 1, p. 4). Load levels 0.3 and 0.6 of ultimate: max stress 3.42 and 6.84 MPa, stated loads
  4.11 and 8.22 kN; "no obvious crack" (p. 3, §2.3). 6 groups × 3 = 18 loaded prisms (p. 3).
- Carbonation: GB/T 50082-2009, 20% CO₂, 70% RH, 20 °C, 7/14/28 d; sections A–D at 0, 0.25, 0.5 and 1.0 of
  the maximum moment; depth on the max-tension side; 1% phenolphthalein, mean of 10 points per section,
  3 specimens per condition (p. 4, §2.4).
- Microstructure: Vickers microhardness (HXD-1000TMC; 20 × 20 × 20 mm samples; 60 indents at 20 µm spacing;
  printed "200 N", 10 s) (pp. 4–5, §2.5); MIP (Autopore II 9220, 130°, 4.00 × 10⁻³–413 MPa; ≈2 g samples,
  isopropanol 3 d, vacuum 45 °C 48 h) on 60%-load specimens after 28 d: L60-I-C 0–6 mm, L60-I-U 6–12 mm
  (zone I, unloaded), L60-II-C 0–10 mm, L60-II-U 10–15 mm (zone II, max moment) (p. 5, §2.6); TG/DTG
  (SDT Q600, 20–1000 °C, 10 °C/min, N₂ 100 mL/min) and XRD (Rigaku Miniflex 600, Cu-Kα, 10–90° 2θ) at 4 mm
  depth steps (p. 5, §2.7).
- Curing & test age: 28 d at 20 ± 2 °C, 95% RH, then 7/14/28 d carbonation (p. 2, §2.1).
→ [[durability]] · [[flexural-strength]] · [[permeability]] · [[carbonation]]

## Key results
| Mix ID | f'c (MPa) | First-crack stress (MPa) | Tensile strength (MPa) | Tensile strain capacity (%) | Crack width (µm) | Other |
|---|---|---|---|---|---|---|
| ECC, 28 d | not reported | 7.41 (flexural first cracking, 4-pt; 6.18 kN) | not reported | not reported | not reported (no visible cracks under sustained load) | ultimate flexural strength 11.41 MPa (9.51 kN) (p. 3, §2.2) |

Carbonation depth (mm) and K_ks (Table 4, p. 7; δ_T and specimen names as in Table 3, p. 4):

| Load level | Name | δ_T | 7 d | K_ks 7 d | 14 d | K_ks 14 d | 28 d | K_ks 28 d |
|---|---|---|---|---|---|---|---|---|
| 0 | Reference | 0.000 | 2.30 | 1.000 | 3.37 | 1.000 | 4.78 | 1.000 |
| 0.3 | S3-PB | 0.075 | 4.47 | 1.943 | 5.16 | 1.531 | 6.75 | 1.412 |
| 0.3 | S3-PC | 0.150 | 5.48 | 2.382 | 5.82 | 1.727 | 7.05 | 1.475 |
| 0.3 | S3-PD | 0.300 | 6.47 | 2.813 | 6.86 | 2.036 | 7.73 | 1.617 |
| 0.6 | S6-PB | 0.150 | 5.54 | 2.409 | 6.40 | 1.899 | 7.94 | 1.661 |
| 0.6 | S6-PC | 0.300 | 6.50 | 2.826 | 7.32 | 2.172 | 8.82 | 1.845 |
| 0.6 | S6-PD | 0.600 | 7.21 | 3.135 | 8.16 | 2.421 | 9.92 | 2.075 |

Main findings (with page/Table/Fig. location):
- Unloaded carbonation rate K_0 = 0.869 / 0.901 / 0.903 at 7 / 14 / 28 d (p. 7, §3.2). These equal
  x_0/√t with t in **days** (2.30/√7 = 0.869; computed here), i.e. mm/d^0.5, although Eq. 2 states K in mm/s^0.5.
- S3-PB (δ_T 0.075): depth +≈100% at 7 d, +53.1% at 14 d, +41.2% at 28 d (p. 6, §3.1).
- Same δ_T but from the 0.6-load specimen (nearer the support) carbonated deeper at 14–28 d than from the
  0.3-load specimen (equal at 7 d); attributed to shear (p. 6, §3.1).
- Per-period fits of Eq. 5 (Fig. 4, p. 8): **7 d K_ks = 1 + 2.662 δ_T^0.351 (R² 0.98751); 14 d
  1 + 1.812 δ_T^0.433 (R² 0.97647); 28 d 1 + 1.331 δ_T^0.463 (R² 0.93359)**. Combined model: y_a = 2.903 −
  0.059t (Eq. 6), y_b printed 0.010·exp(t^0.132) (Eq. 7), p. 8. Model R² 0.98753 / 0.97645 / 0.93357 for
  7 / 14 / 28 d (Fig. 5, p. 8).
- TG/DTG (Fig. 6, p. 9; 60% load, zone II, 28 d): DTG peaks at 100–125 °C (ettringite/C-S-H), ≈240 °C
  (PVA fibre), ≈450 °C (CH); CH absent above ≈12 mm depth (p. 9, §3.3).
- CO₂ bound (550–900 °C mass loss; Fig. 7, p. 10): ≈16 wt.% (0–4 mm), 15.4 wt.% (4–8 mm), then a ≈18% drop to
  ≈12.6 wt.% (8–12 mm), ≈11.9 (12–16 mm), ≈11.7 (16–20 mm) (latter three read from Fig. 7); text sets the
  asymptote beyond 16 mm vs the phenolphthalein front ≈10 mm (p. 9). Fig. 7 draws region boundaries at 6 and
  10 mm, whereas the text names 0–8 mm as regime I (observed).
- XRD (Fig. 8, p. 10): more calcite, no portlandite, less ettringite at 0–4 mm vs 16–20 mm.
- MIP porosity (p. 10, §3.4): zone I 8.70% (L60-I-C) vs 11.57% (L60-I-U); zone II 9.33% (L60-II-C) vs 9.38%
  (L60-II-U) (p. 11). Pore classes read from Fig. 10 (p. 11), % by volume, <0.1 / 0.1–10 / >10 µm:
  L60-I-C ≈ 4.7 / 2.5 / 1.3; L60-I-U ≈ 6.4 / 3.4 / 1.4; L60-II-C ≈ 6.2 / 1.6 / 1.5; L60-II-U ≈ 5.5 / 2.9 / 1.0.
  Text: > 10 µm fraction 1.42 → 1.28% with carbonation (zone I) and 1.28 → 1.51% from zone I to zone II
  carbonated (p. 10–11; the latter printed "> 100 µm", but Fig. 10 classes show > 10 µm is meant).
  Text claims 0.1–10 µm porosity "reduced more than 2-fold after carbonation" (p. 10); Fig. 10a shows
  ≈3.4 → ≈2.5% in zone I (≈1.4×) ⚠️.
- Critical pore diameters (pp. 10–11): first paragraph (zone I discussion) gives 88.38 nm "L60-II-C" vs
  26.12 nm "L60-II-U"; second paragraph gives 77.68 nm (L60-II-C) and 62.59 nm (L60-II-U). The Fig. 9b peak of
  L60-I-C sits near 100 nm, so the first pair most likely refers to L60-I-C / L60-I-U (interpreted).
- Microhardness (Fig. 11, pp. 12–13; Reference, S6-PB, S6-PC, S6-PD): ≈ 120–160 HV within 1 mm of the surface,
  ≈ 60–80 HV beyond ≈ 8–10 mm at all three ages (read from Fig. 11); text: > 100 HV at 2 mm vs 60–80 HV inside
  (p. 12, §3.5). At 28 d the S6-PD profile stays ≈ 75–85 HV at 8–14 mm, above the reference (≈ 65–70 HV) (read).

## Mechanisms / explanations offered by authors
- Sustained load causes short-term creep and micro-cracks → more connected porosity → faster CO₂ ingress;
  CaCO₃ then fills small pores and micro-cracks, so the rate falls with time (p. 6, §3.1).
- Fiber bridging limits load-induced pore growth, so K_ks rises sub-linearly with δ_T (p. 7, §3.2; p. 12, §3.4).
- Carbonation sequence: CH first, then ettringite and C-S-H (p. 9, §3.3).
- Carbonation densifies the matrix and raises microhardness even under high sustained stress (p. 12, §3.5).

## Limitations (stated + observed)
- Stated: one indentation is not statistically representative; larger dataset needed (p. 12, §3.5).
- Observed: single mix; no tensile test, crack width, or f'c; strain hardening not shown for this batch.
- Observed: loads below first cracking only — no cracked-ECC carbonation data.
- Observed: position letters differ between Table 3 (reference = A; loaded B–D, p. 4) and Table 4 (unloaded = C;
  loaded A–C, p. 7); δ_T values agree, so Table 4 letters appear shifted (the table above uses the Table 3 names).
- Observed: stated sustained loads 4.11 / 8.22 kN (p. 3) are not 0.3 / 0.6 × 9.51 kN (= 2.85 / 5.71 kN; computed
  here), although the stresses 3.42 / 6.84 MPa are 0.3 / 0.6 × 11.41 MPa ⚠️.
- Observed: microhardness load printed "200 N" (p. 5; likely 200 gf) ⚠️.
- Observed: Eq. 7 as printed, y_b = 0.010·exp(t^0.132), gives 0.036 at 7 d, far from the Fig. 4 exponents
  (0.351 / 0.433 / 0.463). With coefficient **0.10** it gives 0.364 / 0.412 / 0.473 at 7 / 14 / 28 d, matching
  Fig. 4 (computed here) — the printed 0.010 is most likely a typo for 0.10. Eq. 9 also has a misplaced
  bracket (p. 8).
- Observed: abstract calls the K_ks–δ_T law "exponential"; Eq. 5 is a power law.
- Observed: PVA fiber geometry and Vf in vol.% not given; exposed faces other than the sealed sides not fully described.

## Relation to other work
- Agrees with: ECC carbonation resistance discussed only second-hand so far (Zhang W. 2018, as cited in
  [[ma2021-ecc-durability-review]], p. 9); load-accelerated deterioration consistent with coupled-exposure
  gap stated there.
- Contradicts: ⚔️ unstressed 28-d carbonation depth at 20% CO₂: **4.78 mm** here vs ≈0.8 mm (Zhang W. 2018,
  as cited in [[ma2021-ecc-durability-review]], p. 9) vs ≈13 mm in [[wang2023-ecc-frost-damage]] (Fig. 15a,
  read). Similar test standard, different mixes and preconditioning.
- Extends: first primary carbonation data in the wiki; first coupled load + environment durability data;
  first stress-dependent carbonation model for ECC. → [[durability]]

## Pages updated from this source
- [[durability]] · [[carbonation]] · [[permeability]] · [[flexural-strength]] · [[fly-ash]] · [[pva-fiber]] · [[mix-designs]] · [[mechanical-results]]

## To verify
- [ ] Table 3 vs Table 4 position letters (A/B/C/D) mismatch (confirmed in PDF; δ_T values consistent).
- [ ] Critical pore diameters: 88.38/26.12 nm pair probably mislabelled (zone I samples), per Fig. 9b.
- [ ] "0.1–10 µm porosity reduced more than 2-fold" (p. 10) vs ≈1.4× read from Fig. 10a.
- [ ] Microhardness load "200 N" (printed so in PDF p. 5; likely 200 gf ≈ 1.96 N).
- [ ] Sustained loads 4.11 / 8.22 kN vs 0.3 / 0.6 × 9.51 kN.
- [ ] PVA fiber length, diameter and density (not in this paper; refs. 11, 25); Vf ≈ 2.0 vol.% assumes 1.3 g/cm³.
- [ ] Whether the mix shows tensile strain hardening (only claimed generically).
- [x] Eq. 7 form: printed 0.010 does not reproduce Fig. 4; 0.10 does (computed against the Fig. 4 exponents, p. 8).
- [x] K_0 units: values reproduce x_0/√t with t in days → mm/d^0.5 (computed from Table 4).
