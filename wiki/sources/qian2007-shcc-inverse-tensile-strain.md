---
type: source
slug: qian2007-shcc-inverse-tensile-strain
title: "Simplified Inverse Method for Determining the Tensile Strain Capacity of Strain Hardening Cementitious Composites"
authors: [Shunzhi Qian, Victor C. Li]
year: 2007   # JACT Vol. 5, No. 2, June 2007; received 11 Dec 2006, accepted 27 Apr 2007
venue: "Journal of Advanced Concrete Technology 5 (2) (2007) 235–246 (Japan Concrete Institute)"
doi: "not printed in the PDF ⚠️ unverified (see To verify)"
raw_file: raw/papers/Qian2007_SHCC-inverse-method-tensile-strain.pdf
material_term: "SHCC (strain hardening cementitious composites), 'also referred to as' HPFRCC (Naaman & Reinhardt 1996); ECC is 'a unique representative of SHCCs'. Tested materials: PVA-ECC 0–3 (Michigan, high-volume fly ash), plus PVA-ECC 4 and Ductal (UFC) data re-used from the JCI round robin (Kanakubo 2006). Ductal is grouped with 'SHCCs' by the authors although its strain capacity is 0.5% ⚠️."
study_type: "analytical (parametric flexural model) + experimental validation"
tags: [test-method, four-point-bending, inverse-analysis, quality-control, shcc, ecc, pva-fiber, fly-ash, hvfa, tensile-strain-capacity, jci-standard, michigan, uhpc]
ingested: 2026-10-20
updated: 2026-10-20
---

# Simplified Inverse Method for SHCC Tensile Strain Capacity (Qian & Li, 2007)

## One-paragraph summary
University of Michigan paper that proposes the **"UM method"**: a quality-control test in which the
**deflection capacity** (load-point deflection at modulus of rupture) of a small four-point bending
beam (356 × 76 × 51 mm, span 305 mm) is converted **linearly** into the uniaxial **tensile strain
capacity** through a "master curve". A flexural model (Maalej & Li 1994; bilinear tension and
compression) and a 20-case parametric study (σ_fc 2.5–13 MPa, σ_tu 4–16 MPa, ε_tu 0–5%, E 12–53 GPa,
f'c 31–200 MPa) show that deflection capacity depends almost only on ε_tu, because the neutral axis
quickly moves to about **0.86–0.91 of the depth from the tension face** once ε_t > 1% (Fig. 8). The
conversion is ε′_tu = 0.50·δ_u − 0.22 (Eq. 4). Validation on three high-volume fly-ash PVA-ECCs
(FA/C 1.2 / 2.0 / 2.8) gives predictions within **−6% to +19%** of coupon tests (Table 7). Applied to
JCI round-robin data (curvature version, Eq. 6), the UM method matches the JCI method (JCI-S-003-2005)
with similar accuracy but without LVDTs or solving a cubic equation (Table 8).

## Objective / research question
Develop a simple, reasonably accurate inverse method for site quality control of SHCC tensile strain
capacity from a beam bending test, and validate it against uniaxial tension and the JCI method (p. 236).

## Materials & mix design
Table 1 (p. 238) and Table 5 (p. 242). Proportions by weight relative to cement, except fiber by volume
(note to Table 1; Table 5 basis assumed the same ⚠️).

| Mix ID | Cement | Fly ash | Slag/other | Sand (type, max size) | W/B | SP | Fiber type | L (mm) | d (µm) | Vf (vol.%) |
|---|---|---|---|---|---|---|---|---|---|---|
| PVA-ECC 0 | 1 | 0 | 0 | 1 (type n.r.) | 0.44 (water/cement) | 0.007 | PVA | not reported | not reported | 2 |
| PVA-ECC 1 | 1 | 1.2 | 0 | 0.8 (type n.r.) | 0.27 (water/cementitious) | 0.013 | PVA | 8 (p. 242) ⚠️ | not reported | 2 |
| PVA-ECC 2 | 1 | 2.0 | 0 | 1.1 | 0.26 | 0.014 | PVA | 8 ⚠️ | not reported | 2 |
| PVA-ECC 3 | 1 | 2.8 | 0 | 1.4 | 0.26 | 0.016 | PVA | 8 ⚠️ | not reported | 2 |
| PVA-ECC 4 (JCI "PVA") | not reported | not reported | not reported | not reported | 0.46 | not reported | PVA | 12 (per [[kanakubo2006-dfrcc-tensile-test-method]]) | 40 (same) | 1.9 |
| Ductal (JCI "DCT") | not reported | not reported | not reported | not reported | 0.22 | not reported | steel | 15 (same) | 200 (same) | 2.0 |

Units of binder quantities: mass ratios to cement. FA/C = 1.2 / 2.0 / 2.8 by mass (p. 242).
Fiber diameter and fiber product not reported; fiber length 8 mm is stated on p. 242 only.

## Test methods
- Specimen geometry:
  - **UM four-point bending (FPBT)**: 356 mm long, 50 mm high (51 mm on p. 238 and Table 2 ⚠️), 76 mm deep;
    span 305 mm, constant-moment span 102 mm; all dimensions > 5× fiber length (p. 242, Fig. 9a).
  - **JCI method** (JCI-S-003-2005): 100 × 100 × 400 mm, span 300 mm, curvature by LVDTs (Fig. 9b; Eqs. 8–10).
  - **Uniaxial tension (UTT)**: coupon 304.8 × 76.2 × 12.7 mm, glued aluminium end plates, fixed ends (Fig. 10).
  - Compression: cylinders (size n.r.), cast vertically.
- Loading / rate: FPBT displacement control 0.02 mm/s (MTS 810); UTT 0.0025 mm/s (MTS 810, 25 kN).
- Measurement: FPBT deflection = machine displacement (initial low-stiffness seating < 0.2 mm, < 5% of
  deflection capacity, removed, Fig. 11); UTT 2 LVDTs, gauge about 180 mm.
- Curing & test age: sealed container, about 99% RH, room temperature, **28 d** (p. 242). Hobart 12 L mixer;
  beams and coupons cast horizontally from the same batch; ≥ 3 specimens per test.
→ [[dogbone-uniaxial-tension]], [[flexural-strength]], [[kanakubo2006-dfrcc-tensile-test-method]]

## Key results
Table 6 (p. 243), Table 7 (p. 243), Table 8 (p. 245). ε_tu = strain at ultimate tensile strength (peak), mean ± SD (COV).

| Mix ID | f'c (MPa) | First-crack stress (MPa) | Tensile strength (MPa) | Tensile strain capacity (%) | Crack width (µm) | Other |
|---|---|---|---|---|---|---|
| PVA-ECC 0 (Table 1) | 50.7 ± 5.3 | 5.1 ± 0.2 | 5.7 ± 0.5 | 2.0 ± 1.0 | not reported | E assumed 18 GPa |
| PVA-ECC 1 (FA/C 1.2), 28 d | 54.6 ± 6.5 | 4.6 ± 0.3 | 5.3 ± 0.6 | 2.1 ± 1.1 (52%) | not reported | δ_u 5.8 ± 1.6 mm; predicted 2.4 ± 0.8% (+14%) |
| PVA-ECC 2 (FA/C 2.0), 28 d | 46.0 ± 3.8 | 3.9 ± 0.5 | 4.6 ± 0.2 | 3.5 ± 0.3 (9%) | not reported | δ_u 7.0 ± 1.3 mm; predicted 3.3 ± 0.5% (−6%) |
| PVA-ECC 3 (FA/C 2.8), 28 d | 37.5 ± 1.7 | 4.0 ± 0.2 | 4.9 ± 0.1 | 3.7 ± 0.4 (11%) | not reported | δ_u 9.3 ± 0.9 mm; predicted 4.4 ± 0.1% (+19%) |
| PVA-ECC 4 (JCI data) | 31.3 ± 0.8 | 3.7 ± 0.8 | 5.0 ± 0.5 | 2.7 ± 0.7 (26%) | not reported | φ_u 349.2 µ/mm; JCI 3.1%, UM 3.0% |
| Ductal (JCI data) | 198.0 ± 3.7 | 13.7 ± 0.9 | 15.3 ± 1.0 | 0.5 ± 0.3 (60%) | not reported | φ_u 85.0 µ/mm (2 beams); JCI 0.6%, UM 0.5% |

Main findings (with Table/Fig. location):
- **Deflection–strain relation** (Eqs. 1–3, p. 237–238): u = 15φL²/162 + (φL²/4)(h/L)²; for the UM beam the shear
  term is an order of magnitude smaller, so u ≈ 0.1·φ·L².
- **Master curve** (Fig. 6, Eqs. 4–5): ε′_tu (%) = 0.50·δ_u (mm) − 0.22; predicted deviation PD = 0.50·SD + 0.18.
  Upper edge of the band chosen for conservativeness. Valid only for the UM geometry and loading.
- **JCI-geometry master curve** (Fig. 7, Eqs. 6–7): ε_tu,c (%) = 0.0093·φ_u,c (µ/mm) − 0.24; PD_c = 0.0093·SD_c + 0.19.
- **Neutral axis** (Fig. 8, Table 4): normalised distance from tension face plateaus at 0.86–0.91 for f'c/σ_avg
  of 8.6–18.3; higher ratio → higher value. Linear behaviour holds for ε_t > 1%.
- **Validation** (Table 7, Fig. 13): UM predictions within 20% of UTT for PVA-ECC 1–3.
- **Fly ash**: f'c falls from 54.6 to 37.5 MPa as FA/C rises from 1.2 to 2.8, while ε_tu rises 2.1 → 3.7% and its
  COV falls from 52% to 9–11% (Table 6); attributed to HVFA robustness (Wang 2005, as cited, p. 243).
- **Scatter**: COV of first-crack and ultimate strength < 15%, COV of ε_tu 26–60% (except HVFA mixes) — supports
  quality control on strain rather than strength (p. 243), as also in [[kanakubo2006-dfrcc-tensile-test-method]].
- **MOR** of PVA-ECC 1–3: 10–12 MPa, 2.4–3.0× first-cracking strength; consistent with the ratio about 2.7 for an
  elastic–perfectly plastic tension material (Maalej & Li 1994, as cited, p. 243).
- Crack saturation in the constant-moment zone increases from PVA-ECC 1 to 3 (Fig. 12).

## Mechanisms / explanations offered by authors
- Because SHCC f'c/σ_t is high (about 10), the neutral axis shifts close to the compression face and stabilises,
  so curvature and deflection scale linearly with the extreme-fiber tensile strain; deflection capacity is then
  insensitive to f'c, E and σ_tu (p. 240, conclusions 3–4).
- The UM method decouples ε_tu from moment capacity; the JCI method needs both curvature and M_max (conclusion 2).
- HVFA lowers matrix toughness and chemical bond, improving tensile ductility robustness (Wang 2005, as cited, p. 243).

## Limitations (stated + observed)
- Stated: assumes the material is truly strain-hardening (bending cannot tell, so a few UTT checks are needed at
  trial mixing); quality-control target is ductility only; equations valid only for the stated geometry and
  loading; a standard beam must be agreed (p. 237, 241, 245).
- Observed:
  - Validation on only three mixes (one family, HVFA PVA-ECC) plus two re-used JCI data points.
  - The "UTT" for PVA-ECC 4 is the JCI **thin-plate T1** result (2.7%), while the JCI bending beams were
    100 × 100 mm. The T2 dogbone with the same section gave 2.38% (H) and 0.77% (V) in
    [[kanakubo2006-dfrcc-tensile-test-method]], so the agreement depends on which tension test is the reference.
  - PVA-ECC 1: Eq. 4 with δ_u 5.8 mm gives 2.68%, but Table 7 lists 2.4% ⚠️ (probably averaged per specimen).
  - Ductal curvature 85.0 µ/mm ("two specimens") matches neither B-H (141.2) nor B-V (72.0) in Kanakubo Table 10 ⚠️.
  - Beam height given as 50 and 51 mm; PVA fiber length 8 mm is unusual for PVA-ECC ⚠️.
  - Ductal (ε_tu 0.5%) is called an SHCC; under this wiki's rules it is UHPC, not HDC.
  - Crack widths are not measured.

## Relation to other work
- Agrees with:
  - [[kanakubo2006-dfrcc-tensile-test-method]]: bending-based inverse analysis is a practical alternative to
    uniaxial tension; ε_tu scatter ≫ strength scatter; JCI values re-used directly (Table 6 = Kanakubo Tables 5–6).
  - [[li2002-pva-ecc-interface-tailoring]]: same Michigan coupon (304.8 × 76.2 × 12.7 mm, Al plates, 0.0025 mm/s).
  - [[zhang2022-hshdcc-review]]: deflection hardening alone does not prove tensile strain hardening (here: stated
    assumption (a)).
- Contradicts: ⚔️ none directly. Refinement: ECC crack width "less than 80 µm" (Li 2003, as cited, p. 235) vs
  "< 100 µm" in [[ma2021-ecc-durability-review]] and [[yu2018-ecc-direct-tensile-review]].
- Extends: first simple QC conversion (deflection → ε_tu) in the wiki; HVFA PVA-ECC data with FA/C up to 2.8.

## Pages updated from this source
Proposed only; this ingest wrote the source page alone. The caller will update:
- [[tensile-strain-capacity]] · [[flexural-strength]] · [[dogbone-uniaxial-tension]] · [[tensile-constitutive-model]]
- [[fly-ash]] · [[pva-fiber]] · [[strain-hardening]] · [[multiple-cracking]] · [[uhpc-vhsc]]
- [[terminology-hdc-ecc-shcc]] · [[mechanical-results]] · [[mix-designs]] · [[gaps]]

## To verify
- [ ] DOI not printed in the PDF; check J-STAGE.
- [ ] PVA fiber length "8 mm" (p. 242), fiber diameter and product not reported.
- [ ] Table 5 proportion basis (mass) assumed from the Table 1 note.
- [ ] PVA-ECC 1 predicted ε_tu 2.4% vs 2.68% from Eq. 4 with the mean δ_u.
- [ ] Ductal curvature capacity 85.0 µ/mm vs Kanakubo Table 10 values (141.2 H / 72.0 V).
- [ ] Beam height 50 mm (p. 242) vs 51 mm (p. 238, Table 2).
- [ ] Table 1 "ultimate compressive strain 0.005" vs Table 2 compressive strain capacity "0.5~1%" (estimated range); Table 3 lists 0.005 under a % column.
