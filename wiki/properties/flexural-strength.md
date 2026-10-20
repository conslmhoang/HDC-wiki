---
type: property
slug: flexural-strength
aliases: [MOR, nominal flexural strength, f_n, bending]
tags: [flexure]
sources: [ye2021-uhdc-flexural-size-effect, yang2024-hshdc-uniaxial-tension, zhang2022-hshdcc-review, chai2023-hdc-ambient-temperature]
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

## Related
- [[notched-beam-three-point-bending]] · [[size-effect]] · [[tensile-strain-capacity]]
