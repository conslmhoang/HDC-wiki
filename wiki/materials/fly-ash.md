---
type: material
slug: fly-ash
aliases: [FA, Class F fly ash, high-volume fly ash, HVFA]
tags: [binder, pozzolan, sustainability]
sources: [yang2024-hshdc-uniaxial-tension, ye2021-uhdc-flexural-size-effect, ma2021-ecc-durability-review, yu2018-ecc-direct-tensile-review, yang2008-ecc-fiber-bridging-law, chai2023-hdc-ambient-temperature, li2021-hdc-sulfate-dry-wet, jin2019-hvfa-shcc-structural, qian2007-shcc-inverse-tensile-strain, ozbay2013-ecc-self-healing-sustained-load, deng2015-hdc-compressive-toughness, deng2018-hdc-compressive-constitutive, shumuye2022-slag-fa-pe-ecc, zhong2019-ecc-freeze-thaw, herbert2013-ecc-self-healing-natural-environment, zhang2022-ecc-carbonation-sustained-load, chai2019-hdcc-freeze-thaw-carbonation-flexure, mohammed2020-cr-ecc-elevated-temperature, zhou2023-hsecc-elevated-temperature, gao2020-hdcc-recycled-fine-aggregate, kanda2003-sprayed-ecc, mechtcherine2011-shcc-high-strain-rate, paul2014-r-shcc-chloride-corrosion, wang2023-ecc-frost-damage, zhao2022-ecc-tension-damage-model, bu2022-ecc-chloride-crack-width, ivaniuk2022-printable-shcc-design, chavesfigueiredo2020-printed-shcc]
updated: 2026-10-20
---

# Fly Ash

## Quantitative evidence
| Source | Mix | FA dosage | Effect |
|---|---|---|---|
| [[yang2024-hshdc-uniaxial-tension]] | Xi'an HSHDC M1 / M2 / M3 | 15 / 20 / 25% of binder (Class F, activity index 92%) | 15 → 25%: σcr −21.3%, σp −3.3%, **εp +68.9%** (p. 11) |
| [[ye2021-uhdc-flexural-size-effect]] | Tongji UHDC | FA/C = 1.20 by mass (Class F) | matrix f'c about 36–38 MPa |

## Key points
- FA lowers the fiber/matrix bond and the matrix cracking strength, which raises the PSH margin
  and ductility ([[yang2024-hshdc-uniaxial-tension]], p. 11). → [[strain-hardening]], [[fiber-matrix-interface]]
- FA above 25% was not studied in HSHDC, because f'c would fall below 100 MPa (p. 11).
- ⚠️ The FA density of 1.12 g/cm³ in [[yang2024-hshdc-uniaxial-tension]] looks low. Verify it.

## Durability-related effects (as cited in [[ma2021-ecc-durability-review]])
- More FA lowers chloride permeability. Water absorption is lowest at 40% FA (Arun Kumar 2018, p. 9).
- More FA reduces explosive spalling in PVA-ECC (Sahmaran 2011, p. 3). Shrinkage falls with FA. → [[shrinkage]]
- High-volume FA stabilises ε across strain rates (Yang & Li 2012, as cited in
  [[yu2018-ecc-direct-tensile-review]], p. 349).

## Further FA dosages (2026-10-20 ingest)
| Source | Mix | FA/C (mass) | Note |
|---|---|---|---|
| [[yang2008-ecc-fiber-bridging-law]] Table 1 | M45 PVA-ECC | 1.20 (Class F, 685 kg/m³) | reference ECC mix |
| [[chai2023-hdc-ambient-temperature]] Table 1 | Chinese PVA-HDC C40 | 0.88 (selected mix) | highest-FA mix gave the best ε_tu (§3.1) |
| [[li2021-hdc-sulfate-dry-wet]] Table 2 | XUT PVA-HDC | 1.0 | sulfate study |

- FA in M45 lowers PVA slip hardening (β 0.58 vs 1.15 without FA) → [[fiber-matrix-interface]]


## Fly ash and ductility, strength (2026-10-20, round 4 ingest)
| Source | Term / fiber | FA level (by mass) | Effect | Age |
|---|---|---|---|---|
| [[jin2019-hvfa-shcc-structural]] Table 5, Fig. 8 | PVA-SHCC, W/B 0.25 | FA/C 2.4 → 3.2 → 4.4 | ε_tu 1.92 → **3.42** → 3.07% (more scatter at 4.4); f'c and E fall, peak compressive strain 0.5–0.7% rises. Recommended optimum FA/C ≈ 3.2 (FA/B ≈ 76%) (§3.4.2) | 28 d |
| [[qian2007-shcc-inverse-tensile-strain]] Table 6 | PVA-ECC | FA/C 1.2 → 2.0 → 2.8 | ε_tu 2.1 → 3.5 → 3.7% (COV 52 → 9 → 11%); f'c 54.6 → 46.0 → 37.5 MPa; beam deflection capacity 5.8 → 9.3 mm | 28 d |
| [[ozbay2013-ecc-self-healing-sustained-load]] Table 3 | PVA-ECC, W/B 0.27 | FA/C 1.2 → 2.2 | f'c 69.3 → 46.1 MPa; MOR 12.40 → 10.07 MPa; deflection capacity 4.95 → 6.01 mm | 28 d |
| [[deng2018-hdc-compressive-constitutive]] Table 3, Fig. 5c | PVA-HDC, 2%, W/B 0.29 | FA 40 / 50 / 60% (basis ⚠️) | prism σ0 64.43 / 62.25 / 53.64 MPa; peak compressive strain highest at 50% | n.r. |
| [[shumuye2022-slag-fa-pe-ecc]] Table 4 | PE-ECC, W/B 0.30 | FA/C 1.50 (60% FA) | f'c 40.79 MPa, σ_tu 5.35 MPa, ε ≈ 2.0%; slag replacing FA raises f'c (→ [[ggbfs]]) | 28 d |
| [[zhong2019-ecc-freeze-thaw]] Fig. 16, Tables 6–8 | PVA "ECC" (flexure only) | ground FA 0–70% of cement | frost resistance best up to 35%; PF/UF rise again at 52.5% and fall at 70% (too little CH). FA explains 14.68 / 19.87 / 21.63% of IF / PF / UF variance | F–T |

- **Mechanisms stated by authors:**
  - FA gives a more porous matrix and a weaker PE friction bond, which favours ductility; spherical FA aids fiber
    dispersion ([[shumuye2022-slag-fa-pe-ecc]], Sect. 3.5.1).
  - Raising FA/C (and W/B) lowers bond and Km (authors' claim, not measured) ([[jin2019-hvfa-shcc-structural]], §2.2).
    FA/C > 2.4 brings the particle-size distribution within 10% of the Andreasen & Andersen optimum (Fig. 3a).
  - Higher FA lowers chemical bond and matrix toughness but raises frictional bond (as cited in
    [[ozbay2013-ecc-self-healing-sustained-load]], p. 171). → [[fiber-matrix-interface]]
  - FA improves the fiber–matrix interface and prevents excessive fiber rupture; the authors still recommend limiting FA
    for strength ([[deng2018-hdc-compressive-constitutive]], p. 5).
- **Strength development:** HVFA PVA-SHCC (FA/C 3.2) reaches only 46.6% of its 28-d f'c at 7 d, and gains about 12% from
  28 to 90 d ([[jin2019-hvfa-shcc-structural]], Fig. 9). → [[heat-curing]]
- **Durability links:**
  - FA/C 2.2 chosen deliberately to get smaller crack widths for self-healing; slow pozzolanic reaction may leave
    soluble Ca(OH)₂ that rain washes out ([[herbert2013-ecc-self-healing-natural-environment]], §2.1, §3.1.1). → [[self-healing]]
  - High FA lowers portlandite, which the authors expect to worsen carbonation ([[zhang2022-ecc-carbonation-sustained-load]], §1). → [[carbonation]]
  - Continued pozzolanic reaction partly offsets freeze–thaw and carbonation damage over the first cycles (authors'
    explanation, [[chai2019-hdcc-freeze-thaw-carbonation-flexure]], p. 132). → [[freeze-thaw]]
  - High temperature: residual f'c rises at 100 °C ([[mohammed2020-cr-ecc-elevated-temperature]], §3.2) and rebounds at
    400 °C ([[zhou2023-hsecc-elevated-temperature]], p. 754); both attribute it to further FA reaction. → [[high-temperature-behaviour]]

### Further FA dosages (round 4)
| Source | Term | FA/C (mass) | W/B | Note |
|---|---|---|---|---|
| [[deng2015-hdc-compressive-toughness]] Table 2; [[deng2018-hdc-compressive-constitutive]] Table 2 | HDC (XAUAT) | FA 50% (basis ⚠️, "by volume" in 2015) | 0.29 | PVA 2 vol.%, sand/binder 0.36 |
| [[chai2019-hdcc-freeze-thaw-carbonation-flexure]] Table 2 | Eco-HDCC | 1.50 (60% of binder) | 0.30 | domestic PVA, river sand |
| [[gao2020-hdcc-recycled-fine-aggregate]] Table 3 | HDCC | 0.43 (30%, Grade I) | 0.25 / 0.45 | recycled fine aggregate |
| [[kanda2003-sprayed-ecc]] p. 272 | sprayed ECC | C:FA 7:3 (0.43) | 0.32 | JIS type II FA |
| [[mechtcherine2011-shcc-high-strain-rate]] Table 1 | SHCC | 1.21 (computed) | 0.29 (computed) | with SAP |
| [[mohammed2020-cr-ecc-elevated-temperature]] Table 3 | CR-ECC | 1.20 | stated 0.32 (= w/c); 0.146 computed ⚠️ | crumb rubber |
| [[paul2014-r-shcc-chloride-corrosion]] Table 1 | SHCC | 1.72 | w/c 1.0 | f_cu 23–24 MPa |
| [[wang2023-ecc-frost-damage]] Table 1 | ECC | 1.18 (Class F) | 0.33 | |
| [[zhang2022-ecc-carbonation-sustained-load]] Table 1 | ECC | 1.20 (Class F) | n.r. here | |
| [[zhao2022-ecc-tension-damage-model]] Table 1 | ECC | 2.0 (+ SF 0.073) | 0.24–0.28 | |
| [[zhou2023-hsecc-elevated-temperature]] Table 3 | HSECC (SH not shown) | 1.2 | 0.20 | f_c 83.1 MPa |
| [[bu2022-ecc-chloride-crack-width]] Table 1 | ECC | 1.20 (Class F) | 0.26 (computed) | |
| [[ivaniuk2022-printable-shcc-design]] §2.1 | printable SHCC | CEM I/FA/microsilica 60/25/15 and 70/15/15 | 0.212–0.250 | |
| [[chavesfigueiredo2020-printed-shcc]] | printed SHCC, mix Y | 30% FA | 0.50 | the FA mix was outperformed by the slag mix X |

> Synthesis: two independent PVA datasets ([[jin2019-hvfa-shcc-structural]], [[qian2007-shcc-inverse-tensile-strain]]) show
> ε_tu rising from about 2% to about 3.5% as FA/C goes from about 1.2–2.4 to about 3, with f'c falling about 30%.
> Jin's FA/C 4.4 suggests the gain levels off or reverses above about 3. The frost optimum is lower (35% replacement,
> [[zhong2019-ecc-freeze-thaw]]), so the "best" FA level depends on the target property.

- ⚔️ [[shumuye2022-slag-fa-pe-ecc]]: the text says the all-FA mix (SF-0-60) had the highest tensile capacity, but the
  reported strains are about 2.0% (SF-0-60) < 2.9% (SF-10-50) < 3.5% (SF-5-55) (Sect. 3.2, Fig. 5). The paper does not
  clearly support "FA raises ductility" for PE-ECC. → [[gaps]]

## Related
- [[silica-fume]] · [[ggbfs]] · [[uhdc]] · [[mix-designs]] · [[water-binder-ratio]] · [[freeze-thaw]] · [[carbonation]]
