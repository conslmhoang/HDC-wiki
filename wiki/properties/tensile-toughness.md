---
type: property
slug: tensile-toughness
aliases: [tensile energy absorption, specific energy, toughness index, gp, Ipost, equivalent tensile strength]
tags: [tension, energy]
sources: [yang2024-hshdc-uniaxial-tension]
updated: 2026-10-06
---

# Tensile Toughness Indices

## Definition
Existing toughness indices (ASTM C1018, JSCE-SF4, ASTM C1609) are flexural only. Yang et al. propose
three indices based on the uniaxial tension curve ([[yang2024-hshdc-uniaxial-tension]], Eqs. 4–6, Fig. 14):

| Index | Formula | Meaning |
|---|---|---|
| σe,k | ∫₀^εk σ dε / εk | equivalent tensile strength up to εk |
| gp | ∫₀^εp σ dε | energy density to peak |
| Ipost | ∫εp^εk σ dε / ∫₀^εk σ dε | post-peak share of energy |

εk is the post-peak strain where σ = 0.85σp (⚠️ definition read from Fig. 14).

## Quantitative evidence
| Source | Material | gp (kJ/m³) | σe,0.85 (MPa) | Ipost |
|---|---|---|---|---|
| [[yang2024-hshdc-uniaxial-tension]] Table 7 | Xi'an HSHDC, 13 mixes | 9.26–366.44 | 4.08–6.55 | 0.049–0.459 |
| same (Wille 2014, as cited) | UHPC | about 50 ⚠️ | — | — |

## Related
- [[tensile-strain-capacity]] · [[tensile-constitutive-model]] · [[dogbone-uniaxial-tension]]
