---
type: test-method
slug: dogbone-uniaxial-tension
aliases: [direct tension test, uniaxial tension, JSCE dogbone, dumbbell]
tags: [tension, test, standard]
sources: [ranade2015-hshdc-tensile-rate-effects, ranade2017-hshdc-impact-resistance, su2023-rubber-modified-hshdc, yang2024-hshdc-uniaxial-tension, ye2021-uhdc-flexural-size-effect, he2024-hdc-research-advances, li2002-pva-ecc-interface-tailoring, yu2018-ecc-direct-tensile-review, zhang2022-hshdcc-review, kanda2006-psh-design-criteria, chai2023-hdc-ambient-temperature, li2003-ecc-review, kanakubo2006-dfrcc-tensile-test-method, kunieda2010-uhp-shcc-steel-reinforcement, qian2007-shcc-inverse-tensile-strain, mechtcherine2011-shcc-high-strain-rate, xue2023-shcc-structural-review, kunieda2006-hpfrcc-japan-applications, kanda2003-sprayed-ecc, wang2019-rc-beam-ecc-shear-strengthening, gao2020-hdcc-recycled-fine-aggregate, jin2019-hvfa-shcc-structural, shumuye2022-slag-fa-pe-ecc, sun2019-modified-pva-fiber-ecc, zhao2022-ecc-tension-damage-model, chavesfigueiredo2020-printed-shcc, ivaniuk2022-printable-shcc-design, deng2018-hdc-short-columns]
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

## JCI round robin: geometry, casting and end fixity (Kanakubo 2006)
Four tension methods on the same four DFRCCs ([[kanakubo2006-dfrcc-tensile-test-method]], Table 3, Fig. 3):
T1 = 30 × 13 mm plate dogbone (gauge about 80 mm ⚠️ read from drawing), pin–fix, cast horizontally (H);
T2 = 100 × 60 mm dogbone, pin–fix, H or V; T3 = Ø70 dogbone, pin–fix, V; T4 = Ø100 × 200 cylinder, fix–fix, V.

| DFRCC | T1 | T2-H | T2-V | T3 | T4 | Location |
|---|---|---|---|---|---|---|
| PVA (1.9%, f'c 31.3) σ_tu / ε at peak | 5.00 MPa / 2.70% | 4.18 / 2.38% | 2.87 / 0.77% | 3.38 / 0.071% | 1.78 / 0.32% | Tables 6–9 |
| PE (1.5%, f'c 67.3) | 4.85 / 1.28% | 3.86 / 0.018% | 5.06 / 0.25% | 5.56 / 0.20% | 4.18 / 0.83% | Tables 6–9 |
| HB (PE + steel, f'c 43.6) | 4.37 / 0.71% | 3.54 / 0.22% | 2.51 / 0.017% | 2.84 / 0.12% | 2.15 / 0.44% | Tables 6–9 |

- σ_tu ranks T1 > T2-H > T2-V ≈ T3 > T4 (except PE); strain at peak is largest for T1 and T2-H (Fig. 12, p. 9).
- **Casting direction:** H > V for PVA and HB, the reverse for PE (p. 8–9). → [[fiber-dispersion]]
- COV of strain at peak reached 127–157%. The author concludes that strain at maximum stress is "not
  suitable" for DFRCC deformation capacity (p. 9–10).
- Fix–fix cylinders (T4): the first crack cannot be identified because of the bending moment (p. 8).
- Bias sources listed: end-shape stress concentration, pin vs fix ends, secondary moment after one-sided
  cracking, specimen size, fibre length / specimen ratio (p. 4–5, Table 2).
- JCI therefore standardised a 4-point bending test instead → [[four-point-bending-inverse-analysis]].
- ⚔️ Rokugo 2007 (as cited in [[yu2018-ecc-direct-tensile-review]]) found thickness 13/30/50 mm negligible for
  PVA-ECC. Here shape + casting + fixity changed PVA strain at peak by > 30× (2.70% vs 0.071%). The variables
  differ only partly, but the magnitudes disagree. → [[gaps]]

## Thin dumbbell vs member thickness (Kunieda 2010)
- UHP-SHCC (PE 1.5 vol.%, f'c 95 MPa): dumbbell 13 × 30 mm gives ε_tu 1.5% at 28 d; unreinforced 50 × 200 × 900 mm
  tension members reach only 0.23–0.24% (ratio 0.15–0.16, i.e. about 6× overestimate) and stress about 30% lower;
  strain hardening turns into brittle failure ([[kunieda2010-uhp-shcc-steel-reinforcement]], Table 3, §4.1, Fig. 5).
- Explanation offered: 2-D fibre orientation in 13 mm dumbbells vs 3-D in 50 mm members, and a wider, lower
  bridging-strength distribution in larger volumes (weakest link) (§2, §4.1). → [[size-effect]]
- Member test: D13 grip bars, ten 100 mm Pi-gauges, load control (§3.3, Fig. 4).
- D6 bars at ρs 0.3% restore distributed cracking (ε 1.58% vs 0.24%) (Table 3).
- ⚔️ Same conflict with Rokugo 2007 "thickness negligible" (PVA-ECC) as above; this is PE UHP-SHCC. → [[gaps]]
- Similarly, thin strengthening layers do not realise dogbone ductility because cracks concentrate over the
  substrate crack ("zero-span" effect) ([[xue2023-shcc-structural-review]], Section 4.1.2). Kunieda 2006 notes that
  thin sections, spraying and extrusion give 2-D orientation, so design values should reflect actual placement,
  and calls for a zero-span test (JSCE K-532-1999, 40 × 120 mm) for HPFRCC ([[kunieda2006-hpfrcc-japan-applications]], p. 21, 23).
- Sprayed specimens (10 mm layers) exceed 2% ultimate strain and beat placed specimens (about 1.2–1.6%, Fig. 10 ⚠️ read);
  Kanda et al. recommend sprayed 10 mm-layer specimens over cut-outs from massive blocks ([[kanda2003-sprayed-ecc]], Fig. 8, 10, Conclusion 3).

> Synthesis: three primary sources (Kanakubo 2006, Kunieda 2010, Kanda 2003) show that specimen thickness,
> casting/placing method and end fixity change ε_tu by factors of 2–30. A dogbone ε_tu is a material index for a
> stated geometry, not a member property. Always record geometry, casting direction and grip type with ε_tu.

## More setups (2026-10-20, round 4)
| Source | Term | Specimen / gauge | Grips | Rate | Strain measurement |
|---|---|---|---|---|---|
| [[qian2007-shcc-inverse-tensile-strain]] | ECC/SHCC | coupon 304.8 × 76.2 × 12.7 mm, gauge about 180 mm | glued Al plates, fixed | 0.0025 mm/s | 2 LVDTs |
| [[mechtcherine2011-shcc-high-strain-rate]] | SHCC | dumbbell, 40 × 24 mm narrow section, 40 × 40 mm ends, 100 mm gauge | glued, fixed–fixed | 10⁻⁵ – 50 s⁻¹ | 2 LVDTs; high rate: slack adaptor, piezo force link, 250 kHz; ringing at 10 s⁻¹ (p. 52–53) |
| [[xue2023-shcc-structural-review]] | SHCC | dumbbell 13 × 30 mm, 100 mm gauge (as JC/T 2461 per Chai 2023) | — | — | — |
| [[wang2019-rc-beam-ecc-shear-strengthening]] | ECC (Southeast Univ.) | gauge 13 × 30 × 80 mm, n = 3 | fixed | 0.2 mm/min | 2 LVDTs |
| [[gao2020-hdcc-recycled-fine-aggregate]] | HDCC (Zhengzhou) | dogbone, 40 × 40 mm middle section | — | 0.001 mm/s | 50 mm long. / 25 mm transv. extensometers; valid if ≥ 2 valid, deviation < 30%; Poisson 0.10–0.30 (§2.3.3, Table 6) |
| [[jin2019-hvfa-shcc-structural]] | SHCC | dumbbell, 30 × 30 mm section, 80 mm gauge | — | 0.2 mm/min | LVDT |
| [[shumuye2022-slag-fa-pe-ecc]] | PE-ECC | dogbone 80 × 30 × 13 mm | — | 0.4 mm/min | LVDTs |
| [[sun2019-modified-pva-fiber-ecc]] | ECC | JSCE-type dumbbell, geometry n.s. | — | 0.4 mm/min | — |
| [[zhao2022-ecc-tension-damage-model]] | ECC | plate 280 × 40 × 13 mm | CFRP + Al tabs | 0.2 mm/min | 120 mm extensometer + strain gauge; failure mostly near grips (§3.2) |
| [[chavesfigueiredo2020-printed-shcc]] | printed SHCC | sawn 1-layer plates; LPA 40 × 150 mm, LPE 35 × 30 mm (not dogbones) | glued | 6.67 µstrain/s | DIC; 30 mm LPE length → gauge-length dependence |
| [[ivaniuk2022-printable-shcc-design]] | printed SHCC | printed prisms embedded in dumbbell formwork with freshly cast ends | — | 1 mm/min | — |
| [[deng2018-hdc-short-columns]] | HDC (XAUAT) | direct tension, geometry n.s. ⚠️ | — | — | σ_tu 6.14 MPa, ε_tu ≈ 1.0% (Fig. 1) |

- Uniaxial tension is impractical for plant QC: special jigs, labour, alignment sensitivity
  ([[kanakubo2006-dfrcc-tensile-test-method]], p. 14; [[qian2007-shcc-inverse-tensile-strain]], p. 236).
- COV of ε_tu is 26–60% vs < 15% for strengths in Michigan PVA-ECC, so QC should target strain
  ([[qian2007-shcc-inverse-tensile-strain]], p. 243).

## Related
- [[tensile-strain-capacity]] · [[tensile-constitutive-model]] · [[tensile-toughness]] · [[single-crack-test]] ·
  [[four-point-bending-inverse-analysis]] · [[size-effect]] · [[fiber-dispersion]] · [[strain-rate-effects]]
