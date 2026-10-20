---
type: property
slug: flexural-strength
aliases: [MOR, nominal flexural strength, f_n, bending]
tags: [flexure]
sources: [ye2021-uhdc-flexural-size-effect, yang2024-hshdc-uniaxial-tension, zhang2022-hshdcc-review, chai2023-hdc-ambient-temperature, chai2019-hdcc-freeze-thaw-carbonation-flexure, chavesfigueiredo2020-printed-shcc, gao2020-hdcc-recycled-fine-aggregate, ivaniuk2022-printable-shcc-design, jin2019-hvfa-shcc-structural, kanakubo2006-dfrcc-tensile-test-method, kanda2003-sprayed-ecc, ozbay2013-ecc-self-healing-sustained-load, qian2007-shcc-inverse-tensile-strain, shumuye2022-slag-fa-pe-ecc, sui2018-uhp-ecc-flexural-fatigue, sun2019-modified-pva-fiber-ecc, wang2023-ecc-frost-damage, zhang2022-ecc-carbonation-sustained-load, zhong2019-ecc-freeze-thaw, zhou2023-hsecc-elevated-temperature]
updated: 2026-10-20
---

# Flexural Strength

Always state the test type: notched or unnotched, and three- or four-point loading.

## Quantitative evidence
| Source | Material | Test | Strength (MPa) |
|---|---|---|---|
| [[ye2021-uhdc-flexural-size-effect]] Table 3 | NC / UHDC-1 / UHDC-2 | **notched** 3-pt bending, d 40–150 mm, α 0.10 / 0.23 | f_n 3.65–7.13 / 10.00–21.56 / 18.27–22.11 |
| [[yang2024-hshdc-uniaxial-tension]] Table 5 | PVA-HSHDC (M1 / M2 / M3) | 3-pt f_f; 4-pt f_b | 20.5 / 20.2 / 18.4; 16.33 / 14.63 / 13.06 |

## Key points
- UHDC-2 f_n is insensitive to size and notch depth (about 20 MPa). → [[size-effect]]
- CTOD at peak ([[ye2021-uhdc-flexural-size-effect]], Table 3):

  | Material | CTOD at peak (mm) |
  |---|---|
  | NC | 0.02 |
  | UHDC-1 | about 0.8–1.4 |
  | UHDC-2 | 3.5–6.8 |

## HSHDCC flexure ([[zhang2022-hshdcc-review]], p. 9–10, Table 6)
- Flexural strength ranges 15.5–33.5 MPa, with an optimum W/B of 0.19 (Lei 2019, as cited).
- With 2% fiber, PE gives 88% more flexural strength than steel (Zhou 2018, as cited).
- Deflection-hardening in bending does **not** prove tensile strain-hardening. → [[strain-hardening]]
- There are no uniform flexural test methods; specimen sizes vary widely (Table 6).

## Chinese PVA-HDC thin plates ([[chai2023-hdc-ambient-temperature]], Table 8)
- 15 × 75 × 300 mm plates: 12.23 / 13.08 / 14.08 / 14.65 / 15.64 MPa at −30 / 0 / 20 / 40 / 60 °C;
  deflection-hardening with multiple cracks; deflection peaks at 0 °C (5.01 mm). Span not stated ⚠️.

## Round-4 evidence (2026-10-20, 34-source ingest)
| Source | Material (authors' term) | Test / specimen | Age | Strength (MPa) | Note |
|---|---|---|---|---|---|
| [[chai2019-hdcc-freeze-thaw-carbonation-flexure]] Table 4 | Eco-HDCC (PVA) | 4-pt, 100 × 100 × 400 prism, CECS 13-2009 | n.r. | 14.31; δ_u 2.70 mm | span not stated ⚠️ |
| [[gao2020-hdcc-recycled-fine-aggregate]] Table 5 | R-HDCC / N-HDCC, 2% PVA | 4-pt, 400 × 100 × 15 plate, span 300 | 28 d | 11.89 / 9.41 | deflection hardening at Vf ≥ 1% (R) |
| [[jin2019-hvfa-shcc-structural]] Fig. 14 | HVFA-SHCC | 4-pt, 350 × 50 × 15 coupon | 7 / 28 d | peak at FA/C 3.2 | cracking strength falls with FA; deflection plateaus beyond FA/C ≈ 3.6 |
| [[ozbay2013-ecc-self-healing-sustained-load]] Table 3 | PVA-ECC FA/C 1.2 / 2.2 | 4-pt, span 304 mm | 28 d | 12.4 / 10.1 | pre-loading to 2.5 mm cut MOR by about 17 / 10% |
| [[qian2007-shcc-inverse-tensile-strain]] p. 243, Table 7 | HVFA PVA-ECC | 4-pt, 51 mm deep beams | 28 d | 10–12 = 2.4–3.0× first-crack strength | deflection 5.8 / 7.0 / 9.3 mm at FA/C 1.2 / 2.0 / 2.8 |
| [[kanda2003-sprayed-ecc]] Fig. 11 | sprayed PVA-ECC | 40 × 40 × 160, span 100 mm | n.r. | about 12–17 ⚠️ (read) | cut-outs from 150 mm sprays lose deflection |
| [[zhang2022-ecc-carbonation-sustained-load]] §2.2 | SDU PVA-ECC | 4-pt, 400 × 100 × 50, span 300 | 28 d | first crack 7.41; ultimate 11.41 | — |
| [[wang2023-ecc-frost-damage]] §3.2 | PVA-ECC | 4-pt, 40 × 40 × 160 | 28 d | 18.6; −11% after 300 F-T cycles | → [[freeze-thaw]] |
| [[zhong2019-ecc-freeze-thaw]] Fig. 16a, Table 5 | PVA-ECC | 4-pt, 100 × 100 × 400 | — | peaks at V_PVA 1.5% | V_PVA explains 45% and W/B 30% of variance; brittle at final F-T failure |
| [[sun2019-modified-pva-fiber-ecc]] Table 8 | WUT matrix → 2% PVA | ISO mortar prism | 28 d | 5.7 → 18.2 | — |
| [[sui2018-uhp-ecc-flexural-fatigue]] Fig. 7 | PE UHP-ECC | 4-pt, 100 × 100 × 400, span 300 | n.r. | about 22; deflection > 10 mm (> span/30) | static reference for [[fatigue]] |
| [[ivaniuk2022-printable-shcc-design]] Tables 2–3 | printed PE-SHCC | 3-pt | 28 d | 17.4–22.0 | interlayer weaker → [[3d-printed-hdc]] |
| [[chavesfigueiredo2020-printed-shcc]] Table 3 | printed PVA-SHCC X / Y | notched 3-pt | n.r. | MOR 1.84 / 0.97 | 4-pt flexural hardening in all series (Figs. 4–5) |
| [[shumuye2022-slag-fa-pe-ecc]] Table 4 | PE-ECC + slag | 3-pt, 320 × 60 × 13 plate | 28 d | "load" 403–553 (units kN as printed ⚠️) | 10% slag best |
| [[zhou2023-hsecc-elevated-temperature]] Table 5 | "HSECC" PVA + steel, no strain hardening shown | prism | at 30 °C | 14.3–15.9 | softening; not HDC evidence |

### Key points
- **Bending does not prove tensile strain hardening:** strain-hardening and softening DFRCC cannot be
  distinguished from bending alone; all four round-robin DFRCC deflection-hardened in 4-pt bending
  ([[kanakubo2006-dfrcc-tensile-test-method]], p. 14, Table 10). Horizontal casting gave a larger M_max and
  about 2× curvature at M_max vs vertical (p. 9–11). This confirms the HSHDCC note above.
- **MOR / first-crack ratio** 2.4–3.0, vs a theoretical ≈ 2.7 for elastic–perfectly plastic tension
  (Maalej & Li 1994, as cited in [[qian2007-shcc-inverse-tensile-strain]], p. 243).
- **Bending → tension conversion:** σ_tp/f_c = 0.668·σ_bp/f_c − 0.02 (R² 0.966)
  ([[gao2020-hdcc-recycled-fine-aggregate]], Eq. 7); inverse methods are on [[four-point-bending-inverse-analysis]].
- **Exposure and pre-damage:** pre-loading to 0.5 (first crack) or 0.7 (multiple cracking) of peak lowers
  stiffness and shortens deflection hardening after freeze–thaw + carbonation; the authors recommend the
  15-cycle / preload-0.5 curve for link-slab design ([[chai2019-hdcc-freeze-thaw-carbonation-flexure]], §3.4).
  Flexural toughness fell from about 92 to 33–61 kN·mm after 15 cycles (Fig. 8 ⚠️ read). → [[carbonation]]
- **Recycled fine aggregate** raises flexural strength (+2.17 to +22.5% in 3-pt; 11.89 vs 9.41 MPa in plates)
  ([[gao2020-hdcc-recycled-fine-aggregate]], §3.2, Table 5). → [[recycled-fine-aggregate]]

## Related
- [[notched-beam-three-point-bending]] · [[size-effect]] · [[tensile-strain-capacity]] · [[four-point-bending-inverse-analysis]] · [[fatigue]]
