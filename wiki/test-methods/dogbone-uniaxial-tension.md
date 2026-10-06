---
type: test-method
slug: dogbone-uniaxial-tension
aliases: [direct tension test, uniaxial tension, JSCE dogbone, dumbbell]
tags: [tension, test, standard]
sources: [ranade2015-hshdc-tensile-rate-effects, ranade2017-hshdc-impact-resistance, su2023-rubber-modified-hshdc, yang2024-hshdc-uniaxial-tension, ye2021-uhdc-flexural-size-effect, he2024-hdc-research-advances]
updated: 2026-10-06
---

# Dogbone (Dumbbell) Uniaxial Tension Test

## Definition
A direct tension test on a specimen with a reduced gauge section, commonly the JSCE (2008) HPFRCC
recommendation. It gives σ_fc, σ_tu and ε_tu → [[tensile-strain-capacity]].

## Setups compared
| Source | Specimen / gauge | Grips | Rate | Strain measurement | n |
|---|---|---|---|---|---|
| [[ranade2015-hshdc-tensile-rate-effects]] | dogbone, 90 mm gauge | lost-motion grip above 1 mm/s | 9 µm/s – 0.9 m/s (10⁻⁴ – 10 s⁻¹) | 2 LVDTs | 6 per rate |
| [[ranade2017-hshdc-impact-resistance]] | same dogbone (caption misprinted "980 mm"); large 76 × 76 mm variant | — | quasi-static | LVDTs | — |
| [[su2023-rubber-modified-hshdc]] | JSCE dumbbell, gauge 80 × 30 × 13 mm ⚠️ | — | 0.5 mm/min | LVDT + DIC (0.03 mm/px) | n.r. |
| [[yang2024-hshdc-uniaxial-tension]] | 350 mm long, **150 mm gauge**, 50 × 15 mm section, ends wrapped in CFRP | MTS 100 kN | 0.2 mm/min | 1 clip-on extensometer | 3 |
| [[ye2021-uhdc-flexural-size-effect]] | JSCE dogbone, 13 mm thick, 80 mm gauge | — | 2 mm/min | 2 LVDTs | — |
| [[he2024-hdc-research-advances]] Fig. 6 | dumbbell 330 mm, 60/30 mm wide, 30 mm thick | — | — | — | uncited ⚠️ |

## Key points
- **High-rate testing** ([[ranade2015-hshdc-tensile-rate-effects]]):
  - A lost-motion grip lets the actuator reach speed before engaging the specimen.
  - Stress oscillations from ringing at ≥ 0.01 s⁻¹ are removed by local averaging.
  - The modulus from LVDTs is underestimated.
  → [[strain-rate-effects]]
- **Specimen size matters.** Cor-Tuf in a large dogbone gave lower σ_tu and ε
  ([[ranade2017-hshdc-impact-resistance]], p. 27). → [[size-effect]]
- Crack counting by DIC ([[su2023-rubber-modified-hshdc]]) → [[digital-image-correlation]]

> Synthesis: gauge lengths (80–150 mm), section sizes, rates (0.2–2 mm/min) and strain sensors differ
> between groups. **ε_tu values are not strictly comparable across sources**, so note the setup in
> the review.

## Related
- [[tensile-strain-capacity]] · [[tensile-constitutive-model]] · [[tensile-toughness]] · [[single-crack-test]]
