---
type: property
slug: matrix-fracture-toughness
aliases: [Km, K_IC, matrix toughness, J_tip, crack tip toughness]
tags: [fracture, matrix]
sources: [ranade2015-hshdc-tensile-rate-effects, su2023-rubber-modified-hshdc, ye2021-uhdc-flexural-size-effect, li2002-pva-ecc-interface-tailoring, li1992-steady-state-multiple-cracking]
updated: 2026-10-16
---

# Matrix Fracture Toughness (Km) & J_tip

## Definition
Km is the fracture toughness of the fiber-free matrix. J_tip ≈ Km²/E, the left-hand side of the
energy criterion. A higher Km raises the first-crack strength and makes strain hardening harder
→ [[strain-hardening]].

## Quantitative evidence
| Source | Matrix | Km (MPa√m) | Method |
|---|---|---|---|
| [[ranade2015-hshdc-tensile-rate-effects]] | Michigan HSHDC, 0.02 / 10 mm/s | 1.10 / 1.31 | notched beam |
| same (Orange 2000; Yang 2008, as cited) | UHPC / ECC | 1.31 / about 0.5 | — |
| [[su2023-rubber-modified-hshdc]] Fig. 7 | GDUT matrix, PR 0 / 10 / 20 / 35% | 0.787 / 0.772 / 0.740 / 0.671 | 40×40×160 mm notched beam |
| [[ye2021-uhdc-flexural-size-effect]] Table 4 | NC / UHDC-1 / UHDC-2 (**composite**, apparent K_IC) | 0.62–0.86 / 2.81–4.94 / 3.41–10.08 | double-K, notched 3PB |

Ye's K_IC is an apparent toughness of the fiber-reinforced composite, not the matrix Km. Do not mix
the two. On an Ashby chart UHDC sits near metals, bamboo and wood
([[ye2021-uhdc-flexural-size-effect]], Fig. 12).

## Key points
- **Rate:** Km rises with loading rate, and σ_fc follows it (Irwin criterion)
  ([[ranade2015-hshdc-tensile-rate-effects]], Fig. 16). → [[strain-rate-effects]]
- **Rubber** lowers Km, which lowers σ_fc and raises PSH_strength ([[su2023-rubber-modified-hshdc]]).
  → [[crumb-rubber]]

> Synthesis: matrix Km ranks about ECC (0.5) < GDUT HSHDC (0.79) < Michigan HSHDC (1.10) ≈ UHPC (1.31).
> This order matches the inverse ductility trend in [[tensile-strain-capacity]].

## Further data (2026-10-16 ingest)
- PVA-ECC matrix (w/c 0.45): measured J_tip = 4.5–7.2 J/m², with 5 J/m² assumed in the analysis
  ([[li2002-pva-ecc-interface-tailoring]], p. 470).
- **Theory:**
  - K_tip = Km at low Vf, otherwise (Ec/Em)Km.
  - A higher Gm needs a proportionally higher V_f^crit.
  - The design lever is Gm/(g·τ·df) ([[li1992-steady-state-multiple-cracking]], p. 2250–2259).
  → [[steady-state-cracking]]

## Related
- [[strain-hardening]] · [[fracture-process-zone]] · [[micromechanical-parameters]]
