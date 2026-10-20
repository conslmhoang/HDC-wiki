---
type: source
slug: zhang2022-ecc-carbonation-sustained-load
title: "Carbonation Behavior of Engineered Cementitious Composites under Coupled Sustained Flexural Load and Accelerated Carbonation"
authors: [Hongzhi Zhang, Yingxuan Shao, Ning Zhang, Abdullah M. Tawfek, Yanhua Guan, Renjuan Sun, Changjin Tian, Branko Šavija]
year: 2022   # Materials vol. 15 (2022); received 26 Jul 2022, accepted 30 Aug 2022, published 6 Sep 2022 (XML front matter)
venue: "Materials (MDPI) 2022, 15(18), 6192. Open access, CC BY 4.0. PMCID PMC9504410, PMID 36143512. Shandong University (corresponding authors Y. Guan, R. Sun); TU Delft Microlab (B. Šavija)"
doi: "10.3390/ma15186192"
raw_file: raw/papers/Zhang2022_ECC-carbonation-sustained-load.xml
material_term: "ECC (engineered cementitious composites; authors note the synonyms SHCC and UHTCC). PVA-ECC mix from earlier Shandong University work (refs. 11, 25). Tensile strain hardening is NOT tested here; only 'typically beyond 3%' is stated generically (Abstract). Measured: 4-pt flexural first-cracking 7.41 MPa and ultimate 11.41 MPa (§2.2)."
study_type: "experimental (accelerated carbonation GB/T 50082-2009 under sustained four-point flexural load; phenolphthalein depth; TG/DTG; XRD; MIP; Vickers microhardness; empirical carbonation-depth model)"
tags: [ecc, pva-fiber, fly-ash, durability, carbonation, sustained-load, coupled-loading, mip, tga, xrd, microhardness, carbonation-model, shandong-university]
ingested: 2026-10-20
updated: 2026-10-20
---

# ECC carbonation under sustained flexural load (Zhang et al., 2022)

## One-paragraph summary
Shandong University and TU Delft carbonated 400 × 100 × 50 mm PVA-ECC prisms (C 563, FA 676, W/B 0.30,
PVA 26 kg/m³; Table 1) for 7, 14 and 28 d at 20% CO₂ while holding them under sustained four-point bending
at 30% or 60% of the ultimate flexural load (11.41 MPa), i.e. below the first-cracking stress (7.41 MPa)
(§2.2–2.4). Cutting at four positions along the span gave flexural tensile stress levels δ_T = 0–0.6 of
flexural strength (Table 3). Unstressed carbonation depth was **2.30 / 3.37 / 4.78 mm** at 7 / 14 / 28 d;
at δ_T = 0.6 it was **7.21 / 8.16 / 9.92 mm** (Table 4). The stress influence coefficient K_ks
(= x_σ / x_0) rose with δ_T but at a **decreasing rate** (not linear as for plain concrete), and fell with
exposure time (3.135 at 7 d → 2.075 at 28 d for δ_T 0.6). The authors fit K_ks = 1 + y_a·δ_T^{y_b} with
time-dependent y_a, y_b (Eqs. 5–9). TG/DTG/XRD show CH consumed first, then ettringite and C-S-H; CO₂ bound
≈16 wt.% in the outer 0–4 mm (Fig. 7). MIP: carbonation refined 0.1–10 µm pores; sustained load added only
a few > 10 µm pores, attributed to fiber bridging (§3.4). Microhardness was > 100 HV in the carbonated
skin vs 60–80 HV inside (§3.5).

## Objective / research question
- Quantify how sustained flexural tensile stress changes ECC carbonation depth with time, and propose a
  depth model that includes stress level (§1, last para).
- Explain the change via phase assemblage, pore structure and micro-hardness along the carbonation profile (§1).
- Motivation: little is known about carbonation of hardened ECC (most work is carbonation curing), and
  high-FA binders have less portlandite (§1).

## Materials & mix design
- OPC 42.5 I; Class F fly ash (oxides Table 2); quartz sand 125–180 µm; Kuraray PVA (dimensions and
  properties not reported); PCE superplasticizer; VMA (§2.1).

| Mix ID | Cement | Fly ash | Slag/other | Sand (type, max size) | W/B | SP | Fiber type | L (mm) | d (µm) | Vf (vol.%) |
|---|---|---|---|---|---|---|---|---|---|---|
| ECC (SDU mix, refs. 11, 25) | 563 | 676 | VMA 4.50 | quartz sand 450, 125–180 µm (0.18 mm max) | 0.30 (water 372) | 5.58 | PVA (Kuraray) | not reported | not reported | 26 kg/m³ (≈ 2.0 if ρ = 1.3 g/cm³ — density not given in this paper ⚠️) |

Units of binder quantities: kg/m³ (Table 1). FA/C = 676/563 = 1.20 by mass (computed here).

## Test methods
- Specimen geometry: prisms 400 × 100 × 50 mm; four-point bending, span 300 mm (§2.1–2.2).
- Loading / rate: flexural capacity at 0.4 mm/min, LVDT mid-span, mean of 3 (§2.2). Sustained load in a
  bolted three-specimen rig with load cell, re-tightened every 24 h, laid horizontally in the chamber; side
  faces epoxy-sealed (§2.3, Fig. 1). Load levels 0.3 and 0.6 of ultimate: max stress 3.42 and 6.84 MPa
  (4.11 and 8.22 kN); "no obvious crack" (§2.3).
- Carbonation: GB/T 50082-2009, 20% CO₂, 70% RH, 20 °C, 7/14/28 d; sections at 0, 0.25, 0.5 and 1.0 of the
  maximum moment; 1% phenolphthalein, mean of 10 points per section, 3 specimens per condition (§2.4).
- Microstructure: Vickers microhardness (HXD-1000TMC; 60 indents at 20 µm spacing; "200 N", 10 s) (§2.5);
  MIP (Autopore II 9220, 130°) on 60%-load specimens after 28 d (§2.6); TG/DTG (20–1000 °C, 10 °C/min, N₂) and
  XRD at 4 mm depth steps (§2.7).
- Curing & test age: 28 d at 20 ± 2 °C, 95% RH, then 7/14/28 d carbonation (§2.1).
→ [[durability]] · [[flexural-strength]] · [[permeability]]

## Key results
| Mix ID | f'c (MPa) | First-crack stress (MPa) | Tensile strength (MPa) | Tensile strain capacity (%) | Crack width (µm) | Other |
|---|---|---|---|---|---|---|
| ECC, 28 d | not reported | 7.41 (flexural first cracking, 4-pt) | not reported | not reported | not reported (no visible cracks under sustained load) | ultimate flexural strength 11.41 MPa (9.51 kN) (§2.2) |

Carbonation depth (mm) and K_ks (Table 4):

| Load level | δ_T | 7 d | K_ks 7 d | 14 d | K_ks 14 d | 28 d | K_ks 28 d |
|---|---|---|---|---|---|---|---|
| 0 | 0.000 | 2.30 | 1.000 | 3.37 | 1.000 | 4.78 | 1.000 |
| 0.3 | 0.075 | 4.47 | 1.943 | 5.16 | 1.531 | 6.75 | 1.412 |
| 0.3 | 0.150 | 5.48 | 2.382 | 5.82 | 1.727 | 7.05 | 1.475 |
| 0.3 | 0.300 | 6.47 | 2.813 | 6.86 | 2.036 | 7.73 | 1.617 |
| 0.6 | 0.150 | 5.54 | 2.409 | 6.40 | 1.899 | 7.94 | 1.661 |
| 0.6 | 0.300 | 6.50 | 2.826 | 7.32 | 2.172 | 8.82 | 1.845 |
| 0.6 | 0.600 | 7.21 | 3.135 | 8.16 | 2.421 | 9.92 | 2.075 |

Main findings (with Table/Fig. location):
- Unloaded carbonation rate K_0 = 0.869 / 0.901 / 0.903 (mm/d^0.5, units inferred) at 7 / 14 / 28 d (§3.2).
- Same δ_T but from the 0.6-load specimen (nearer the support) carbonated deeper at 14–28 d than from the
  0.3-load specimen; attributed to shear (§3.1).
- Model fit R² > 0.9 for all periods (Fig. 5).
- CH disappears above ≈12 mm depth (TG/DTG, Fig. 6); CO₂ ≈16 wt.% (0–4 mm), 15.4 wt.% (4–8 mm), sharp drop
  (~18%) at 8–12 mm, asymptote beyond 16 mm vs phenolphthalein depth ≈10 mm (§3.3, Fig. 7).
- XRD: more calcite, no portlandite, less ettringite at 0–4 mm vs 16–20 mm (Fig. 8).
- MIP porosity: zone I (no stress) 8.70% carbonated vs 11.57% uncarbonated; zone II (max moment) 9.33% vs
  9.38%; 0.1–10 µm porosity reduced > 2× by carbonation (§3.4, Figs. 9–10).
- Microhardness > 100 HV at 2 mm depth vs 60–80 HV in the interior; large scatter (§3.5, Fig. 11).

## Mechanisms / explanations offered by authors
- Sustained load causes short-term creep and micro-cracks → more connected porosity → faster CO₂ ingress;
  CaCO₃ then fills small pores and micro-cracks, so the rate falls with time (§3.1).
- Fiber bridging limits load-induced pore growth, so K_ks rises sub-linearly with δ_T (§3.2, §3.4).
- Carbonation sequence: CH first, then ettringite and C-S-H (§3.3).
- Carbonation densifies the matrix and raises microhardness even under high sustained stress (§3.5).

## Limitations (stated + observed)
- Stated: one indentation is not statistically representative; larger dataset needed (§3.5).
- Observed: single mix; no tensile test, crack width, or f'c; strain hardening not shown for this batch.
- Observed: loads below first cracking only — no cracked-ECC carbonation data.
- Observed: position labels differ between Table 3 (reference = A; B–D loaded) and Table 4 (unloaded = C;
  A–C loaded) ⚠️.
- Observed: MIP text first gives critical pore diameters 88.38 nm (L60-II-C) vs 26.12 nm (L60-II-U), then
  62.59 nm (L60-II-U) and 77.68 nm (L60-II-C) ⚠️; pore-size class names (">10 µm mesopore", ">100 µm") inconsistent.
- Observed: microhardness load printed "200 N" (likely 200 gf) ⚠️.
- Observed: Eq. (7) y_b = 0.010·exp(t^0.132) (MathML) gives y_b ≈ 0.036 at 7 d, which does not reproduce
  Table 4 K_ks (a fit to Table 4 at 7 d needs an exponent ≈ 0.4; computed here) ⚠️.
- Observed: PVA fiber geometry and Vf in vol.% not given; specimen side sealing but top/bottom exposure not fully described.

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
- [[durability]] · [[permeability]] · [[flexural-strength]] · [[fly-ash]] · [[pva-fiber]] · [[mix-designs]] · [[mechanical-results]]

## To verify
- [ ] Table 3 vs Table 4 position labels (A/B/C/D) mismatch.
- [ ] MIP critical pore diameters: 88.38/26.12 nm vs 62.59/77.68 nm statements.
- [ ] Microhardness load "200 N" (likely 200 gf ≈ 1.96 N).
- [ ] Eq. (7) form: y_b = 0.010·exp(t^0.132) does not reproduce Table 4 — check the PDF/figure 4 fit values.
- [ ] K_0 units (mm/d^0.5 inferred from 2.30/√7 = 0.869).
- [ ] PVA fiber length, diameter and density (not in this paper; refs. 11, 25); Vf ≈ 2.0 vol.% assumes 1.3 g/cm³.
- [ ] Whether the mix shows tensile strain hardening (only claimed generically).
