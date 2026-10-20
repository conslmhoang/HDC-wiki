---
type: test-method
slug: dogbone-uniaxial-tension
aliases: [direct tension test, uniaxial tension, JSCE dogbone, dumbbell]
tags: [tension, test, standard]
sources: [ranade2015-hshdc-tensile-rate-effects, ranade2017-hshdc-impact-resistance, su2023-rubber-modified-hshdc, yang2024-hshdc-uniaxial-tension, ye2021-uhdc-flexural-size-effect, he2024-hdc-research-advances, li2002-pva-ecc-interface-tailoring, yu2018-ecc-direct-tensile-review, zhang2022-hshdcc-review, kanda2006-psh-design-criteria, chai2023-hdc-ambient-temperature, li2003-ecc-review]
updated: 2026-10-20
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

## Additional setups and evidence (2026-10-16 ingest)
- **JSCE (2008) dogbone geometry:**
  - total length 330 mm (85 + 40 + 80 + 40 + 85);
  - ends 60 mm wide;
  - gauge section 30 mm wide, **80 mm long**, 13 mm thick
  ([[yu2018-ecc-direct-tensile-review]], Fig. 3, p. 349).
  This matches the Su 2023 gauge (80 × 30 × 13 mm), so that ⚠️ flag can probably be cleared.
- It is the most common HSHDCC setup (≥ 5 specimens), with loading rates of 0.02–3 mm/min across studies
  ([[zhang2022-hshdcc-review]], Table 7).
- **Thick vs thin specimens:** thick dogbones (60 × 100 mm section) give more stable curves than thin
  ones (20 × 30 mm). The conversion coefficient for σ_tu is 0.69 ⚠️ (as cited, p. 10–11).
- **Michigan PVA-ECC coupon** (not a dogbone):
  - 304.8 × 76.2 × 12.7 mm;
  - aluminium plates epoxied on, fixed hydraulic grips;
  - 0.0025 mm/s;
  - 2 LVDTs over about 185 mm.
  A thickness close to the fiber length may bias fiber orientation
  ([[li2002-pva-ecc-interface-tailoring]], p. 466–469).
- **Shape effect** (as cited in [[yu2018-ecc-direct-tensile-review]], p. 348):
  - cylinders give lower σ and ε than dogbones (Kesner 2003; Mechtcherine 2011);
  - thickness of 13 / 30 / 50 mm has a negligible effect (Rokugo 2007).
- At impact rates, if only one crack forms, ε depends on the gauge length (p. 349).

## Further setups (2026-10-20 ingest)
- Kanda & Li: coupon 305 × 76.2 × 12.7 mm, glued Al plates, 2 LVDTs over 205 mm; first crack = first
  inflection of the σ–ε curve; ε_cu = onset of continuous stress drop ([[kanda2006-psh-design-criteria]], Fig. 3, Fig. 7, p. 64).
- Chinese PVA-HDC: dogbone with a 13 × 30 mm section and 100 mm LVDT gauge ([[chai2023-hdc-ambient-temperature]], §2).
- A standard uniaxial tension test that accounts for size and geometry was already listed as an R&D need
  in 2003 ([[li2003-ecc-review]], Sect. 8). It is still missing.

## Related
- [[tensile-strain-capacity]] · [[tensile-constitutive-model]] · [[tensile-toughness]] · [[single-crack-test]]
