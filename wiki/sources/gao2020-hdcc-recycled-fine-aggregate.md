---
type: source
slug: gao2020-hdcc-recycled-fine-aggregate
title: "Experimental Study of Utilizing Recycled Fine Aggregate for the Preparation of High Ductility Cementitious Composites"
authors: [Danying Gao, Mingyan Lv, Lin Yang, Jiyu Tang, Gang Chen, Yang Meng]
year: 2020            # Materials 13(3), Feb 2020 issue; published 3 Feb 2020 (received 7 Jan, accepted 1 Feb 2020)
venue: "Materials (MDPI) 13(3) (2020) 679"
doi: "10.3390/ma13030679"
raw_file: raw/papers/Gao2020_HDCC-recycled-fine-aggregate.xml
material_term: "HDCC (high ductility cementitious composite); R-HDCC = with 100% recycled fine aggregate (RFA), N-HDCC = with natural river sand (NFA). Authors describe HDCC as strain-hardening with 'strain capacity of 3–5%' (§1, uncited range). PVA fiber 0–2 vol.%, Class I FA 30% of binder, water-cured 28 d. Evident tensile strain hardening reported only for R-HDCC at 1.5–2.0% fiber; N-HDCC showed only fluctuations (§3.4)"
study_type: experimental
tags: [hdcc, pva-fiber, fly-ash, recycled-fine-aggregate, sustainability, construction-waste, fiber-content, uniaxial-tension, dogbone, four-point-bending, thin-plate, three-point-bending, compression, ct-scan, sem, xrd, fiber-matrix-interface, prediction-model, zhengzhou-university]
ingested: 2026-10-20
updated: 2026-10-20
---

# Recycled fine aggregate in PVA-HDCC (Gao et al., 2020)

## One-paragraph summary
Zhengzhou University (Gao Danying group) replaced river sand **fully (100%) with recycled fine aggregate (RFA)**
from crushed waste concrete, sieved with a single 1.18 mm screen (no Fuller-curve regrading), in a PVA-fiber
HDCC with 0–2 vol.% fiber (§1, §2.1). RFA is finer, rougher and more absorptive than river sand (water absorption
6.72% vs 1.18%; 4.86× more crush dust < 0.075 mm) (Table 4, §3.1). The authors find a **denser matrix and a
stronger fiber/matrix bond** with RFA, giving higher compressive, flexural, bending and tensile strengths, and —
counter to the usual ECC rule that lower bond favours ductility — **more multiple cracking and higher ductility**:
at 2% fiber, tensile peak strain 4.76% vs 1.68% (+183%) and four-point bending peak deflection +183% at 1% fiber
(Tables 5–6). Only R-HDCC with 1.5–2.0% fiber showed evident tensile strain hardening. Linear models relate
σ_bp/f_c and σ_tp/f_c to Vf (Eqs. 5–7).

> Synthesis: a **third Chinese HDCC lineage** in the wiki (Zhengzhou), distinct from Southeast Univ. / Taiyuan
> ([[chai2023-hdc-ambient-temperature]], [[chai2019-hdcc-freeze-thaw-carbonation-flexure]]) and the Xi'an groups.
> Note that the tensile series uses **W/B 0.45 without superplasticizer** and reaches only σ_tp 1.1–2.8 MPa — far
> weaker than typical PVA-ECC (≈ 4–5 MPa). The bending/compression series uses W/B 0.25. Tension and bending
> results therefore come from **different matrices** and should not be combined.

## Objective / research question
- Can RFA with its original grading (single 1.18 mm screen) fully replace river sand in HDCC while keeping good
  bending and tensile behaviour (§1)?
- How do RFA and NFA differ physically, mineralogically and in their ITZ, and how does Vf (0–2%) interact (§1, §3)?
- Stated gap: bending and tension of HDCC with **100% RFA** "has not been studied in detail" (§1).

## Materials & mix design
Constituents (§2.1, Tables 1–2, 4):
- **Cement:** ordinary Portland cement 42.5R (CaO 63.42%, SiO₂ 18.77%).
- **Fly ash:** Grade I (Hejin power plant, Shanxi); CaO 4.2%, SiO₂ 54.45%, Al₂O₃ 28.37% (Table 1).
- **RFA:** waste concrete → jaw crusher → hammer crusher → sieve ≤ 1.18 mm. Apparent density 2536 kg/m³, bulk
  1309 kg/m³, water absorption 6.72%, crushing index 18.3% (Table 4). Contains SiO₂, CaCO₃, dolomite (XRD, Fig. 8);
  heterogeneous (old paste + natural sand + coarse-aggregate fragments, CT Fig. 7).
- **NFA:** river sand ≤ 1.18 mm; apparent 2593 kg/m³, bulk 1460 kg/m³, absorption 1.18%, crushing index 12.8% (Table 4).
- **SP:** polycarboxylate water reducer (Subote).
- **Fiber:** PVA, L 12 mm, d 40 µm, σ_f ≥ 1250 MPa, E > 30 GPa, elongation ≥ 6%, density "1.3 g/m³" (typo for
  g/cm³; 26 kg/m³ ↔ 2.0 vol.% is consistent) (Table 2). Manufacturer and oil coating: not reported.

| Mix ID | Cement | Fly ash | Slag/other | Sand (type, max size) | W/B | SP | Fiber type | L (mm) | d (µm) | Vf (vol.%) |
|---|---|---|---|---|---|---|---|---|---|---|
| 25R00 / 05 / 10 / 15 / 20 | 831.6 | 356.4 | none | 475.2, RFA, 1.18 mm | 0.25 | 12.1 | PVA | 12 | 40 | 0 / 0.5 / 1.0 / 1.5 / 2.0 (fiber 0 / 6.5 / 13 / 19.5 / 26 kg/m³) |
| 25N00 … 25N20 | 831.6 | 356.4 | none | 475.2, river sand, 1.18 mm | 0.25 | 12.1 | PVA | 12 | 40 | 0–2.0 (same) |
| 45R00 … 45R20 | 626.9 | 268.6 | none | 358.2, RFA, 1.18 mm | 0.45 | 0 | PVA | 12 | 40 | 0–2.0 (same) |
| 45N00 … 45N20 | 626.9 | 268.6 | none | 358.2, river sand, 1.18 mm | 0.45 | 0 | PVA | 12 | 40 | 0–2.0 (same) |

Units of binder quantities: kg/m³ (Table 3). Water 297 (W/B 0.25) and 403 (W/B 0.45) kg/m³.
Ratios (Table 3, checked here by mass): aggregate/binder R/B = 0.4; FA = 30% of binder → FA/C = 0.43 (computed).
The 25-series is used for compression, 3-pt flexure and 4-pt bending; the 45-series **only** for tension (§2.2).

- Mixing (§2.2): dry solids ≈ 2 min → water + SP slowly → fibers 2 min → high-speed mixing → 30 s vibration.
- Curing: 24 h in the mould at 20 °C, RH ≥ 98%, then water at 20 °C to 28 d (§2.2).

## Test methods
- **Compression / 3-pt flexure:** 40 × 40 × 160 mm prisms, 100 mm span, 50 N/s; compression on the halves
  (40 × 40 mm platen), 2.4 kN/s; GB/T 17671-1999; n = 3 (§2.3.1). Results only in Fig. 9 (no table).
- **4-pt bending:** thin plates 400 × 100 × 15 mm, span 300 mm, third-point loading, 0.1 mm/min, two mid-span LVDTs;
  σ = PL/(bd²) per ASTM C1018 / C78; n = 3 (§2.3.2). σ_bc = onset of non-linearity, σ_bp = peak, δ_bu = maximum
  deflection, G_b = area under the **whole** load–deflection curve (unit not stated ⚠️).
- **Uniaxial tension:** dogbones (Fig. 1, dimensions in the figure only), central section 40 × 40 mm; MTS,
  0.001 mm/s; four clip extensometers, longitudinal gauge 50 mm, transverse 25 mm (§2.3.3). σ_tc = first stress drop,
  σ_tp / ε_tp = peak, **ε_tu = maximum strain (post-peak, not at peak)**, G_t = area under the whole curve (unit not stated ⚠️),
  ν_t = Poisson's ratio. Only specimens failing in the gauge length without eccentricity kept; ≥ 2 valid, deviation < 30%.
- **Microstructure:** XRD (aggregates), X-ray CT (aggregates, post-test dogbones), SEM (ITZ and pulled-out fibers) (§2.3.4).
- **Curing & test age:** 28 d (water curing).
→ [[dogbone-uniaxial-tension]] · [[flexural-strength]] · [[compressive-strength]]

## Key results
Uniaxial tension, W/B 0.45 series, 28 d (Table 6). "Tensile strain capacity" = ε_tp (at peak); ε_tu (maximum strain) in "Other".

| Mix ID | f'c (MPa) | First-crack stress (MPa) | Tensile strength (MPa) | Tensile strain capacity (%) | Crack width (µm) | Other |
|---|---|---|---|---|---|---|
| 45R00 | not reported (45 series) | 1.15 | — (brittle) | — | not reported | E_t 11.49 GPa; G_t 12.54; ν 0.18 |
| 45N00 | not reported | 0.98 | — | — | not reported | 6.49 GPa; 18.47; 0.12 |
| 45R05 | not reported | 1.14 | 1.51 | 1.32 | not reported | ε_tu 5.08; 12.82 GPa; G_t 2033.34 |
| 45N05 | not reported | 1.02 | 1.12 | 0.41 | not reported | ε_tu 4.58; 7.76 GPa; 1634.00 |
| 45R10 | not reported | 1.75 | 2.16 | 1.69 | not reported | ε_tu 9.10; 13.29 GPa; 4796.38 |
| 45N10 | not reported | 1.63 | 1.69 | 1.54 | not reported | ε_tu 5.83; 10.66 GPa; 3872.03 |
| 45R15 | not reported | 1.82 | 2.61 | 2.48 | not reported | ε_tu 10.02; 16.01 GPa; 11002.04; **SH + multiple cracking** |
| 45N15 | not reported | 1.70 | 1.99 | 1.64 | not reported | ε_tu 7.60; 11.38 GPa; 6263.50 |
| 45R20 | not reported | 2.38 | **2.84** | **4.76** | not reported | ε_tu 11.73; 20.35 GPa; 18805.06; **SH + multiple cracking** |
| 45N20 | not reported | 1.57 | 2.75 | 1.68 | not reported | ε_tu 10.72; 12.97 GPa; 10143.70; fluctuations only |

Four-point bending, 15 mm plates, W/B 0.25 series, 28 d (Table 5): σ_bc / σ_bp (MPa); δ_bc / δ_bp / δ_bu (mm); G_b.

| Mix | σ_bc | δ_bc | σ_bp | δ_bp | δ_bu | G_b |
|---|---|---|---|---|---|---|
| 25R00 / 25N00 | 6.19 / 4.87 | 0.09 / 0.10 | — | — | — | 35.20 / 35.01 |
| 25R05 / 25N05 | 6.25 / 4.78 | 0.11 / 0.21 | 6.47 / 4.84 | 0.12 / 0.22 | 1.76 / 5.30 | 373.17 / 720.10 |
| 25R10 / 25N10 | 6.57 / 5.58 | 0.20 / 0.08 | 9.33 / 6.54 | 6.22 / 2.20 | 8.17 / 7.86 | 4308.87 / 2562.66 |
| 25R15 / 25N15 | 6.78 / 6.06 | 0.23 / 0.18 | 10.43 / 7.02 | 7.58 / 4.90 | 10.53 / 9.81 | 6738.25 / 3451.62 |
| 25R20 / 25N20 | 8.11 / 7.97 | 0.42 / 0.21 | **11.89** / 9.41 | **7.67** / 5.12 | 17.26 / 11.28 | 10090.39 / 5403.01 |

Main findings (with Table/Fig. location):
- **RFA properties:** 0.075–0.15 and 0.15–0.3 mm fractions 20.94% and 23.31% (372.69% and 69.53% above NFA);
  4.86× crush dust; bulk density −10.34%; absorption 5.69× and crushing index 1.43× those of NFA (§3.1, Fig. 6, Table 4).
- **Compression (40 mm cubes from prisms, W/B 0.25):** R-HDCC 6.67–18.45% higher than N-HDCC across Vf; Vf has little
  effect on f_c (Fig. 9a, §3.2). Absolute values only in the figure — not available in the XML ⚠️.
- **3-pt flexure:** R-HDCC 2.17–22.5% higher; 0 → 2% fiber raises flexural strength by 264.89% (R) vs 204.35% (N) (§3.2, Fig. 9b).
- **4-pt bending:** at 0.5% fiber, no deflection hardening (fibers ruptured; bridging < cracking strength), and R-HDCC
  is *less* deformable than N-HDCC (δ_bu 1.76 vs 5.30 mm). At ≥ 1% fiber, R-HDCC shows multiple cracking and clear
  deflection hardening; N-HDCC less so (§3.3, Table 5, Figs. 10–11).
- **Tension:** at 0.5–1.0% both mixes soften after a few fluctuations; at 1.5–2.0% only R-HDCC strain-hardens with
  multiple cracking (Fig. 12–14). From 0.5 to 2.0% fiber, R-HDCC σ_tp +88.08%, ε_tp +260.60%, ε_tu +130.91%,
  E_t +58.74%, G_t +824.84% (§3.4).
- **CT:** R-HDCC voids smaller and narrower in size distribution (Fig. 14).
- **SEM:** tight RFA/paste ITZ vs a visible gap at NFA; fibers pulled from R-HDCC are rough, coated with hydrates and
  stripped of surface filaments; those from N-HDCC smooth (Figs. 15–16).
- **Models** (R-HDCC; Vf presumably in %): σ_bp/f_c = 0.036 Vf + 0.069 (R² 0.948); σ_tp/f_c = 0.025 Vf + 0.026
  (R² 0.967); σ_tp/f_c = 0.668 σ_bp/f_c − 0.02 (R² 0.966) (Eqs. 5–7, Figs. 18–20).

## Mechanisms / explanations offered by authors
- Denser matrix with RFA from: reactive old-paste crumbs and crush dust; better particle packing/filling of the ITZ;
  finer, rougher particles; absorption of surface water by RFA → thinner water film and tighter ITZ (§3.2).
- Higher fiber/matrix bond → higher bridging stress and more multiple cracking under SH conditions; lower elastic
  modulus of RFA adds deformation; finer RFA means less crack detour, promoting multiple cracking via "crack trapping"
  (§3.3, citing ref. 23 ⚠️).
- At 0.5% fiber the higher bond makes fibers rupture more easily, so RFA lowers ductility at low Vf (§3.3).

## Limitations (stated + observed)
- Observed: tension (W/B 0.45, no SP) and bending/compression (W/B 0.25) use **different matrices**; f_c of the
  tension series is not reported, so the normalisation σ_tp/f_c (Eq. 6) uses an unspecified f_c ⚠️.
- Observed: **ε_tu here is the maximum (post-peak) strain** over a 50 mm gauge (up to 11.73%), which includes
  localisation; the wiki's tensile strain capacity is ε_tp (≤ 4.76%).
- Observed: very low tensile strengths (σ_tc 0.98–2.38 MPa, σ_tp ≤ 2.84 MPa) compared with PVA-ECC.
- Observed: crack width and crack number not measured; strain hardening judged from curves and CT only.
- Observed: no interface test (pull-out) — "higher bond" is inferred from SEM and strength.
- Observed: two percentage statements do not match the tables: σ_tp 45R15 vs 45N15 "34.82% higher" (Table 6 gives
  31.2%); G_b 25R20 vs 25N20 "95.22% higher" (Table 5 gives 86.8%) ⚠️.
- Observed: citation numbering slips (Lederer cited as [23] in §3.2 but listed as ref. 19; ref. 23 is Li 1992 on
  compressive strength, also cited for "crack trapping") ⚠️.
- Observed: G_b and G_t units missing; compression/flexure values only in figures; durability not tested.
- Stated: Fuller-curve treatment (Li & Yang 2017, as cited) needs multiple screens and more crushing; this study avoids it (§1).

## Relation to other work
- Agrees with: Li & Yang 2017 (as cited, §1): ECC with recycled concrete fines reaches "several percent" tensile strain.
- Contradicts: ⚔️ The ECC design rule that **lower** bond raises ductility ([[li2002-pva-ecc-interface-tailoring]]:
  oil coating cuts τ0/Gd, ε 0.99 → 4.88%; Li & Leung 1992 as invoked in [[chai2019-hdcc-freeze-thaw-carbonation-flexure]],
  p. 127). Here a **higher** bond (inferred) coincides with **more** ductility at Vf ≥ 1%, while at 0.5% the same
  higher bond reduces ductility. Consistent with an optimum-bond view only if N-HDCC's bond is below the optimum
  (not measured). See [[fiber-matrix-interface]].
- Extends: [[fiber-geometry]] (Vf 0–2% series; strain hardening needs ≥ 1.5% here).
- Contrast: [[chai2023-hdc-ambient-temperature]] and [[chai2019-hdcc-freeze-thaw-carbonation-flexure]] use the same
  class of domestic 12 mm / ≈ 40 µm / ≥ 1250 MPa PVA at 26 kg/m³ (2 vol.%) with river sand ≤ 1.18 mm. Chai 2023 at
  W/B 0.30 and FA/C 0.88 reached ε_tu 1.15% at 4.23 MPa; Gao's N-HDCC at W/B 0.45 reached ε_tp 1.68% at 2.75 MPa.

## Pages updated from this source
- [[tensile-strain-capacity]] · [[flexural-strength]] · [[compressive-strength]] · [[fiber-matrix-interface]]
- [[fiber-geometry]] · [[pva-fiber]] · [[fly-ash]] · [[multiple-cracking]] · [[strain-hardening]]
- [[dogbone-uniaxial-tension]] · [[terminology-hdc-ecc-shcc]] · [[mix-designs]] · [[mechanical-results]] · [[gaps]]

## To verify
- [ ] Absolute compressive and 3-pt flexural strengths (Fig. 9 only; not in the XML text) — read from the PDF figure if obtained.
- [ ] Dogbone geometry (Fig. 1 only) and whether the 40 × 40 mm "middle" section is the gauge section.
- [ ] Units of G_b and G_t (not stated; likely N·mm ⚠️).
- [ ] Which f_c normalises σ_tp in Eq. 6 (the tension series W/B 0.45 has no reported f_c).
- [ ] Vf units in Eqs. 5–6 (% assumed).
- [ ] Mismatched percentages: σ_tp 45R15/45N15 (34.82% stated vs 31.2% from Table 6); G_b 25R20/25N20 (95.22% vs 86.8%).
- [ ] PVA manufacturer and oiling (not reported); fiber density "1.3 g/m³" typo.
- [ ] Why W/B 0.45 with no SP was used for tension (not explained).
