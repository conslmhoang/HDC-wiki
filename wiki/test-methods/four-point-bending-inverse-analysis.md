---
type: test-method
slug: four-point-bending-inverse-analysis
aliases: [4PB, four-point bending, inverse analysis, JCI-S-003-2005, UM method, moment–curvature method, FPBT, deflection hardening]
tags: [flexure, test, inverse-analysis, quality-control, standard]
sources: [kanakubo2006-dfrcc-tensile-test-method, qian2007-shcc-inverse-tensile-strain, zhang2022-hshdcc-review, chai2019-hdcc-freeze-thaw-carbonation-flexure, sui2018-uhp-ecc-flexural-fatigue, zhou2023-hsecc-elevated-temperature, gao2020-hdcc-recycled-fine-aggregate, jin2019-hvfa-shcc-structural, ozbay2013-ecc-self-healing-sustained-load, zhang2022-ecc-carbonation-sustained-load, zhong2019-ecc-freeze-thaw, wang2023-ecc-frost-damage, chavesfigueiredo2020-printed-shcc]
updated: 2026-10-21
---

# Four-Point Bending and Inverse Analysis of Tensile Properties

## Definition
An unnotched prism or plate is loaded at two points, giving a constant-moment zone. The load–deflection
(or moment–curvature) curve is either reported as such (flexural strength, deflection capacity,
"deflection hardening") or converted by **inverse analysis** into uniaxial tensile properties (σ_tu, ε_tu)
([[kanakubo2006-dfrcc-tensile-test-method]], §5; [[qian2007-shcc-inverse-tensile-strain]], p. 236).
It is used because direct tension is hard to run for quality control → [[dogbone-uniaxial-tension]].

## Why bending instead of direct tension
- The JCI round robin showed that direct-tension strain at peak changes with specimen shape, casting
  direction and end fixity: PVA-DFRCC gave 2.70% (thin plate) down to 0.071% (Ø70 dogbone), with COV up to
  127–157% ([[kanakubo2006-dfrcc-tensile-test-method]], Tables 6–9, p. 9–10).
- The JCI committee therefore standardised **only a 4-point bending moment–curvature test**. Tensile
  strength and ultimate strain evaluation is a non-mandatory appendix ([[kanakubo2006-dfrcc-tensile-test-method]], p. 14–15).
  Qian & Li identify this method as JCI-S-003-2005 ([[qian2007-shcc-inverse-tensile-strain]], p. 242).
- Direct tension needs special end fixtures, is sensitive to misalignment, takes time, and is unsuitable for
  site QC ([[qian2007-shcc-inverse-tensile-strain]], p. 236; [[kanakubo2006-dfrcc-tensile-test-method]], p. 14).

## Methods compared
| Method | Specimen / span | Measurement | Conversion | Validity / note |
|---|---|---|---|---|
| **JCI** (JCI-S-003-2005) | 100 × 100 × 400 mm, span 300 mm, 100 mm constant-moment zone | curvature from LVDTs; M_cr, M_max | Case 1: bilinear stress block (σ_cr from M_cr, σ_max from M_max); Case 2: uniform tension block; JCI solves a cubic for the neutral axis | Only when several separated cracks form in the pure-bending zone ([[kanakubo2006-dfrcc-tensile-test-method]], Fig. 6, Fig. 14, p. 14; [[qian2007-shcc-inverse-tensile-strain]], Eqs. 8–10) |
| **UM** (Michigan) | 356 × 76 × 51 mm (50 mm on p. 242 ⚠️), span 305 mm, 102 mm constant-moment zone, 0.02 mm/s | deflection from machine displacement only | **ε_tu (%) = 0.50·δ_u (mm) − 0.22**; predicted deviation PD = 0.50·SD + 0.18 | UM geometry and loading only; material must be truly strain-hardening ([[qian2007-shcc-inverse-tensile-strain]], Eqs. 4–5, Fig. 9a, p. 245) |
| UM master curve for JCI geometry | 100 × 100 × 400 mm, span 300 mm | curvature φ_u | ε_tu (%) = 0.0093·φ_u (µ/mm) − 0.24 | ([[qian2007-shcc-inverse-tensile-strain]], Eq. 6) |

- **Basis of the UM method:** SHCC has a high f'c/σ_t (about 10). The neutral axis shifts towards the
  compression face and plateaus at 0.86–0.91 of the depth (from the tension face) once ε_t > 1%, so
  deflection scales linearly with extreme-fibre tensile strain ([[qian2007-shcc-inverse-tensile-strain]], Fig. 8, p. 240).
  It rests on the Maalej & Li (1994) sectional model with bilinear tension and compression (§3.1). → [[tensile-constitutive-model]]
- The UM method separates ε_tu from moment capacity; the JCI method needs both curvature and M_max
  ([[qian2007-shcc-inverse-tensile-strain]], conclusion 2).

## Validation data
| Source | Material (authors' term) | Direct tension ε_tu (%) | Inverse ε_tu (%) | Note |
|---|---|---|---|---|
| [[qian2007-shcc-inverse-tensile-strain]] Table 7 | PVA-ECC 1 (FA/C 1.2), 28 d | 2.1 ± 1.1 | 2.4 ± 0.8 (UM, +14%) | Eq. 4 gives 2.68% ⚠️ internal |
| same | PVA-ECC 2 (FA/C 2.0), 28 d | 3.5 ± 0.3 | 3.3 ± 0.5 (UM, −6%) | δ_u 7.0 mm |
| same | PVA-ECC 3 (FA/C 2.8), 28 d | 3.7 ± 0.4 | 4.4 ± 0.1 (UM, +19%) | δ_u 9.3 mm |
| [[qian2007-shcc-inverse-tensile-strain]] Table 8 (JCI data) | PVA-ECC 4 = JCI "PVA" (DFRCC) | 2.7 (T1 thin plate) | 3.0 (UM) / 3.1 (JCI) | ⚠️ reference choice, see below |
| same | Ductal = JCI "DCT" (UFC, **not HDC**) | 0.5 | 0.5 (UM) / 0.6 (JCI) | authors call it SHCC; see [[uhpc-vhsc]] |
| [[kanakubo2006-dfrcc-tensile-test-method]] Table 11 (Case 1, H) | PVA / PE / HB / DCT | T2-H: 2.38 / 0.018 / 0.217 / — | 3.07 / 2.36 / 1.79 / 1.19 (ultimate, back-calculated) | differences from T2 within scatter (Fig. 16) |

- Casting direction matters in bending too: B-H gives a slightly larger M_max and a much larger curvature
  at M_max than B-V ([[kanakubo2006-dfrcc-tensile-test-method]], p. 11).
- PVA-ECC MOR of 10–12 MPa is 2.4–3.0× the first-crack strength, close to the about 2.7 expected for an
  elastic–perfectly plastic tension material (Maalej & Li 1994, as cited in [[qian2007-shcc-inverse-tensile-strain]], p. 243).

## ⚠️ Deflection hardening ≠ tensile strain hardening
- All four JCI DFRCCs deflection-harden in 4PB, but strain-hardening and softening DFRCC **cannot be told
  apart from bending results alone** ([[kanakubo2006-dfrcc-tensile-test-method]], Table 10, p. 14).
- The UM method assumes strain hardening; a few direct-tension checks are needed at trial mixing
  ([[qian2007-shcc-inverse-tensile-strain]], p. 236, 245).
- Flexural deflection hardening does not prove tensile strain hardening ([[zhang2022-hshdcc-review]], p. 9–10).
- Example: [[zhou2023-hsecc-elevated-temperature]] calls its material HSECC but reports no tension test, and
  its 40 × 40 × 160 mm prism curves soften right after peak (Fig. 10). The span and the three- vs four-point
  arrangement are not stated.

> Synthesis: several wiki sources (Chai 2019, Zhou 2023, Wang 2023, Zhong 2019, Zhang 2022 carbonation,
> Ozbay 2013) characterise "HDC/ECC" ductility only by bending. Their materials should be recorded as
> deflection-hardening (or not), never relabelled as strain-hardening, unless a tension test is reported.

## Four-point bending setups in the corpus (no inverse analysis)
| Source | Term | Specimen / span | Rate | Main output |
|---|---|---|---|---|
| [[chai2019-hdcc-freeze-thaw-carbonation-flexure]] | Eco-HDCC | 100 × 100 × 400 mm prism, CECS 13-2009 (span 300 mm computed, not stated ⚠️) | 0.2 mm/min | 14.31 MPa, δ_u 2.70 mm at 0 cycles; four-stage deflection-hardening curve kept after 150 F–T cycles + carbonation (Table 4, Figs. 6–7) → [[freeze-thaw]], [[carbonation]] |
| [[sui2018-uhp-ecc-flexural-fatigue]] | UHP-ECC (PE) | 100 × 100 × 400 mm, span 300 mm, load points 100 mm apart | 1 mm/min static; 8 Hz fatigue | about 22 MPa (≈ 21–22 at ≈ 9–11 mm, read from Fig. 7), deflection > span/30; DIC: first crack at 58% of peak (Figs. 6–7, 9; pp. 5–8) → [[fatigue]] |
| [[gao2020-hdcc-recycled-fine-aggregate]] | HDCC | 400 × 100 × 15 mm plate, span 300 mm, loads 100 mm apart, 50 mm overhangs (Fig. 3a, p. 5) | 0.1 mm/min | σ_bp up to 11.89 MPa (RFA, 2%); deflection hardening at Vf ≥ 1% (Table 5) → [[recycled-fine-aggregate]] |
| [[jin2019-hvfa-shcc-structural]] | SHCC | 350 × 50 × 15 mm coupon, span 300 mm, thirds of 100 mm (Fig. 11, p. 13) | — | 7 and 90 d only; cracking strength falls with FA (7 d 7.2 → 4.8 MPa); flexural strength 9.8–13.6 (7 d) / 13.1–16.8 MPa (90 d) (Fig. 14, p. 15) |
| [[ozbay2013-ecc-self-healing-sustained-load]] | ECC | 360 × 50 × 75 mm, span 304 mm | — | MOR 12.4 / 10.1 MPa (FA/C 1.2 / 2.2), 28 d (Table 3) |
| [[zhang2022-ecc-carbonation-sustained-load]] | ECC | 400 × 100 × 50 mm, span 300 mm | — | first crack 7.41, ultimate 11.41 MPa, 28 d (p. 3, §2.2); third-point loading, loads 100 mm apart (Fig. 1, p. 4) |
| [[zhong2019-ecc-freeze-thaw]] | ECC | 100 × 100 × 400 mm | 0.02 mm/s | flexure every 25 F–T cycles (§2.3); 0-cycle peak loads ≈ 12.5–31 kN across 25 mixes (read from Fig. 7, p. 6) |
| [[wang2023-ecc-frost-damage]] | ECC | 40 × 40 × 160 mm | — | 18.6 MPa at 28 d; −11% after 300 F–T cycles (§3.2) |
| [[chavesfigueiredo2020-printed-shcc]] | printed SHCC | printed beams (Figs. 4–6) | 1 mm/s | flexural hardening in all series; more layers → fewer cracks |

> Synthesis: spans of 300–305 mm dominate, but sections range from 15 mm plates to 100 mm prisms. Because
> deflection capacity scales with geometry (Qian & Li's master curves are geometry-specific), flexural
> strengths and deflections from different setups are not comparable without the inverse model.

## Conflicts & open questions
- ⚔️ **Which tension test is the reference?** The UM/JCI agreement for PVA-ECC 4 uses the JCI thin plate T1
  (2.7%), while the same-section T2 dogbone gave 2.38% (H) and 0.77% (V)
  ([[qian2007-shcc-inverse-tensile-strain]], Table 8; [[kanakubo2006-dfrcc-tensile-test-method]], Table 7).
- The relation between uniaxial and bending-derived properties differs between DFRCCs; more data are needed
  ([[kanakubo2006-dfrcc-tensile-test-method]], p. 15).
- A standard beam geometry agreed by the user community is still needed; new master curves are required
  for any other geometry or longer fibres ([[qian2007-shcc-inverse-tensile-strain]], p. 239, 241, 245).
- No Chinese HDC standard bending-inverse method is in the corpus. JC/T 2461-2018 (as cited in
  [[chai2023-hdc-ambient-temperature]]) uses a dogbone.
- Bending inverse methods are validated only on PVA-ECC (Michigan HVFA, JCI) and UFC; none on PE-HSHDC.

## Related
- [[dogbone-uniaxial-tension]] · [[notched-beam-three-point-bending]] · [[flexural-strength]] ·
  [[tensile-strain-capacity]] · [[tensile-constitutive-model]] · [[strain-hardening]] · [[digital-image-correlation]]
