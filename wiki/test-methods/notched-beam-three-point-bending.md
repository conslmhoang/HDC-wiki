---
type: test-method
slug: notched-beam-three-point-bending
aliases: [notched 3PB, three-point bending, double-K fracture test, CTOD]
tags: [flexure, fracture, test]
sources: [ye2021-uhdc-flexural-size-effect, su2023-rubber-modified-hshdc, ranade2015-hshdc-tensile-rate-effects]
updated: 2026-10-06
---

# Notched Beam Three-Point Bending

## Setups compared
| Source | Purpose | Specimen | Notch | Rate | Output |
|---|---|---|---|---|---|
| [[ye2021-uhdc-flexural-size-effect]] | size effect, composite K_IC | b = d = 40 / 70 / 100 / 150 mm, d/s = 0.44 | saw-cut, α = 0.10 / 0.23 | 2 mm/min | f_n, CTOD (clip gauge), DIC; K_IC by double-K (Xu & Reinhardt) with Wallin correction |
| [[su2023-rubber-modified-hshdc]] | matrix Km | 40 × 40 × 160 mm, span 100 mm | 12 mm | — | Km (Eqs. 1–3) |
| [[ranade2015-hshdc-tensile-rate-effects]] | matrix Km at rate | span 254 mm, depth 46.2 mm (as given for strain-rate conversion) | — | 20 µm/s – 10 mm/s | Km |

## Conflicts & open questions
- ⚠️ In Ye et al., the NC beam sizes differ between tables: 40/70/100 in Tables 3/4 vs 40/100/150 in
  Tables 2/5. The c_n formula may be misprinted.
- LEFM/double-K methods are applied to strain-hardening composites. Their validity is questionable.

## Related
- [[size-effect]] · [[matrix-fracture-toughness]] · [[flexural-strength]]
