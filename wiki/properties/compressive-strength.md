---
type: property
slug: compressive-strength
aliases: [f'c, fc, uniaxial compression]
tags: [compression]
sources: [ranade2017-hshdc-impact-resistance, su2023-rubber-modified-hshdc, yang2024-hshdc-uniaxial-tension, ye2021-uhdc-flexural-size-effect, he2024-hdc-research-advances, zhang2022-hshdcc-review, ma2021-ecc-durability-review, chai2023-hdc-ambient-temperature, li2021-hdc-sulfate-dry-wet, deng2015-hdc-compressive-toughness, deng2018-hdc-compressive-constitutive, deng2018-hdc-short-columns, chavesfigueiredo2020-printed-shcc, ivaniuk2022-printable-shcc-design, gao2020-hdcc-recycled-fine-aggregate, jin2019-hvfa-shcc-structural, mohammed2020-cr-ecc-elevated-temperature, ozbay2013-ecc-self-healing-sustained-load, shumuye2022-slag-fa-pe-ecc, sui2018-uhp-ecc-flexural-fatigue, sun2019-modified-pva-fiber-ecc, wang2019-rc-beam-ecc-shear-strengthening, wang2023-ecc-frost-damage, zhou2023-hsecc-elevated-temperature, kunieda2010-uhp-shcc-steel-reinforcement, deng2017-rc-column-hdc-jacket, deng2019-urm-shaking-table-hdc, deng2020-aac-wall-hdc-retrofit, li2021-hdc-beam-shear, zhang2022-hdc-basalt-textile-tension, choi2016-pe-alkali-activated-slag-composite, yun2013-shcc-freeze-thaw, pourfalah2018-ecc-high-temperature]
updated: 2026-10-21
---

# Compressive Strength

Always record the specimen type and size and the age.

## Quantitative evidence
| Source | Material | Specimen | Age | f'c (MPa) |
|---|---|---|---|---|
| [[ranade2017-hshdc-impact-resistance]] p. 26 | Michigan HSHDC | 51 mm cube (n = 8) / 76 mm cube (n = 6) | n.s. | 166 (CV 6.1%) / 159 |
| same | Cor-Tuf FR-UHPC | 51 mm cube | n.s. | 201 (CV 3.7%) |
| [[su2023-rubber-modified-hshdc]] Fig. 6a | GDUT R-HSHDC | Ø50 × 100 mm cylinder | 28 d | about 72–157 ⚠️ (read from a chart) |
| [[yang2024-hshdc-uniaxial-tension]] Tables 4–5 | Xi'an matrix only | — | 60 d | about 108–110 |
| same | PVA-HSHDC | 100 mm cube | 28 d | 91.6–96.4 |
| [[ye2021-uhdc-flexural-size-effect]] p. 7 (Wang & Yu 2019, as cited) | NC / UHDC-1 / UHDC-2 | — | 28 d | 45.2 / 37.7 / 36.4 |

## Key points
- **Rubber** lowers f'c by up to 33.2%, which the authors attribute to bubbles, a weak interface and
  low-modulus particles. Fiber length has no significant effect ([[su2023-rubber-modified-hshdc]], p. 4–5).
  → [[crumb-rubber]]
- **Adding fiber** slightly lowers f'c in UHDC ([[ye2021-uhdc-flexural-size-effect]]).
- **Reported in the review** ([[he2024-hdc-research-advances]]):
  - Coarse aggregate at 0–28% raises strength and 38% lowers it (Xu 2019, as cited, p. 6).
  - Under sulfate plus wet–dry cycles, f'c rises up to 30 cycles and then falls (p. 11–12).
  - f'c falls with temperature (p. 7).
  → [[durability]], [[high-temperature-behaviour]]

## HSHDCC strategies ([[zhang2022-hshdcc-review]], p. 7–9)
- Five strategies are named:
  1. particle packing;
  2. hydration and pozzolanic reaction (SF 0 → 10% gave +71% ⚠️);
  3. smaller aggregate (124 → 132 MPa);
  4. heat curing (record 210 MPa after 9 d in 90 °C water);
  5. steel fiber (+51%).
- Compressive strain capacity is 2.8–4.1‰. LC³ lowers f'c by 13.3%.
- Under heat, f'c stays about constant up to 200 °C, then falls by more than 75% at 800 °C
  (as cited in [[ma2021-ecc-durability-review]]). → [[high-temperature-behaviour]]

## Further evidence (2026-10-20 ingest)
| Source | Material | Specimen | Age | f'c (MPa) |
|---|---|---|---|---|
| [[chai2023-hdc-ambient-temperature]] Table 5, p. 8 | Chinese PVA-HDC C40 | 100 mm cube / prism | 28 d | f_cu 48.0; prism 43.1 (f_c/f_cu 0.90 vs 0.76 for concrete); E 23.2–24.1 GPa |
| [[li2021-hdc-sulfate-dry-wet]] Table 4, p. 6 | XUT PVA-HDC (FA/C 1.0) | 100 mm cube | 90 d | 45.8; drum-shaped failure (cracked, not scattered) |

- 8 h exposure at −30 to 60 °C changes f_cu only −2.7% to +9.8% ([[chai2023-hdc-ambient-temperature]], Table 5). → [[high-temperature-behaviour]]
- Under sulfate plus dry–wet cycles, f_cu first rises then falls; the water control also rises 39%
  (45.8 → 63.6 MPa), so part of the early gain is continued hydration ([[li2021-hdc-sulfate-dry-wet]], Table 4). → [[durability]]

## Round-4 evidence (2026-10-20, 34-source ingest)
| Source | Material (authors' term) | Specimen | Age | f'c (MPa) |
|---|---|---|---|---|
| [[deng2015-hdc-compressive-toughness]] Table 3 | XAUAT matrix / PVA-HDC 1.0 / 1.5 / 2.0% | 100 × 100 × 300 prism | about 10 months | 64.0 (computed from 640.45 kN; text 63.06) / 50.3 / 56.9 / 62.3 (computed) |
| [[deng2018-hdc-compressive-constitutive]] Table 3 | XAUAT matrix / 9 PVA-HDC mixes | 100 × 100 × 300 prism | n.r. ⚠️ | 63.06 / 50.3–64.4 |
| [[deng2018-hdc-short-columns]] Table 4 | XAUAT PVA-HDC 2% vs companion concrete | 100 mm cube | n.r. | 65.7 vs 68.9 |
| [[wang2019-rc-beam-ecc-shear-strengthening]] Table 1, p. 4 | PVA-ECC 1.5% | 100 mm cube | 28 d | 55.9 (CoV 4.2%); E 24.9 GPa |
| [[ozbay2013-ecc-self-healing-sustained-load]] Table 3 | PVA-ECC FA/C 1.2 / 2.2 | 50 mm cube | 28 d | 69.3 / 46.1 |
| [[wang2023-ecc-frost-damage]] Table 4 | PVA-ECC vs W/C 0.5 concrete | n.r. | 28 d | 46.8 vs 42.92 |
| [[sun2019-modified-pva-fiber-ecc]] Table 8 | WUT matrix → 2% PVA | n.r. | 28 d | 44.4 → 40.6 |
| same, Fig. 5, p. 13 | WUT PVA-ECC S1–S4 | n.r. | 7 d | S1 33.0; S2 ≈ 30.3, S3 ≈ 23.7, S4 ≈ 26.3 (read from Fig. 5) |
| [[jin2019-hvfa-shcc-structural]] Fig. 8a, p. 11 | HVFA-SHCC, 6 mixes FA/C 2.4 → 4.4 | 100 × 100 × 300 prism | 28 d | 46.7 / 41.2 / 39.9 / 38.8 / 37 / 32.5 (bar labels); E 22.2 → 15.7 GPa, E = 490 f_c (Fig. 8c–d, p. 12); FA3.2 ≈ 18.5 / 40 / 45 MPa at 7 / 28 / 90 d (read from Fig. 9, p. 12) |
| [[shumuye2022-slag-fa-pe-ecc]] §3.1; Fig. 4, p. 7 | PE-ECC, slag 0 / 5 / 10 / 15% | 100 mm cube | 28 d | 40.79 / 42.23 / 52.44 / 55.05 (+34.9% at 15%; bar labels); 7 d 29.03 / 36.88 / 45.6 / 51.48 |
| [[mohammed2020-cr-ecc-elevated-temperature]] Fig. 2, p. 6; Fig. 3, p. 7 | crumb-rubber PVA-ECC (RSM) | 50 mm cube | 28 d | 30–75; 2% PVA mixes 0 / 2.5 / 5% CR ≈ 75 / 58 / 46 (24 °C controls after 60 °C drying, read from Fig. 3) |
| [[sui2018-uhp-ecc-flexural-fatigue]] Sect. 2.2 | PE UHP-ECC | cube | 28 d / 90 d | 102.8 / 120.7 |
| [[kunieda2010-uhp-shcc-steel-reinforcement]] Table 2 | UHP-SHCC (PE) | n.r. | 28 d | 95 |
| [[zhou2023-hsecc-elevated-temperature]] Table 5 | "HSECC" PVA + steel (no strain hardening shown) | 100 mm cube | at 30 °C | 75–94 |
| [[ivaniuk2022-printable-shcc-design]] Tables 2–3 | printed PE-SHCC | 40 mm cube | 28 d | 73–83 |
| [[chavesfigueiredo2020-printed-shcc]] Table 2 | printed PVA-SHCC, mixes X / Y; loaded ⟂ / ∥ to layers | 35 mm cube | 28 d | X 44.09 / 41.93; Y 17.66 / 15.02 |
| [[gao2020-hdcc-recycled-fine-aggregate]] Fig. 9a, p. 9 | HDCC with recycled vs river fine aggregate, W/B 0.25, Vf 0–2% | 40 mm cube halves of prisms | 28 d | **R-HDCC 83.6 / 83.2 / 84.9 / 84.1 / 83.8; N-HDCC 75.6 / 78.0 / 73.5 / 71.0 / 70.9** (Vf 0 / 0.5 / 1 / 1.5 / 2%; printed bar labels); RFA +6.67 to +18.45%. The tension series (W/B 0.45) f_c is not reported |

### Key points
- **Fiber does not raise f'c above the fiber-free matrix** in XAUAT PVA-HDC: matrix 63.06 MPa vs 50.3–62.3 MPa
  for 1–2% PVA; within HDC, f'c rises with fiber content (1 → 2%: 50.3 → 62.3 MPa)
  ([[deng2018-hdc-compressive-constitutive]], Table 3). The same small loss appears in WUT ECC (44.4 → 40.6 MPa,
  [[sun2019-modified-pva-fiber-ecc]]) and in UHDC ([[ye2021-uhdc-flexural-size-effect]]).
- **Compressive deformability:** HDC peak strain 0.56–0.80%, about 3× the matrix (0.21–0.22%), with 10–20%
  residual capacity and an inclined shear crack instead of columnar splitting
  ([[deng2015-hdc-compressive-toughness]]; [[deng2018-hdc-compressive-constitutive]]). Full stress–strain
  models and the toughness index are on [[compressive-constitutive-model]].
- **Mix variables** (XAUAT PVA-HDC, [[deng2018-hdc-compressive-constitutive]], Fig. 5): W/B optimum 0.29;
  FA 40 → 60% lowers f'c 64.4 → 53.6 MPa; S/B optimum 0.36. → [[water-binder-ratio]], [[fly-ash]]
- **Slag** raises PE-ECC f'c (28 d +3.5 / +28.5 / +34.9% for 5 / 10 / 15%; 40.79 → 55.05 MPa) ([[shumuye2022-slag-fa-pe-ecc]], Fig. 4, p. 7). → [[ggbfs]]
- **HVFA:** 28 d f'c underestimates later strength (+12% at 90 d), and E is lower than ordinary concrete
  (22.2 → 15.7 GPa as FA/C rises 2.4 → 4.4; E = 490 f_c) ([[jin2019-hvfa-shcc-structural]], Fig. 8, pp. 11–12). XAUAT HDC also has a lower E than concrete, which lowers the initial
  stiffness of HDC columns ([[deng2018-hdc-short-columns]], Fig. 10).
- **Recycled fine aggregate** raises f'c by 6.67–18.45% at W/B 0.25; Vf 0–2% has little effect
  (83.2–84.9 vs 70.9–78.0 MPa) ([[gao2020-hdcc-recycled-fine-aggregate]], §3.2, p. 8; Fig. 9a, p. 9). → [[recycled-fine-aggregate]]
- **Printing:** direction effect on f'c is small (5–15%) in [[chavesfigueiredo2020-printed-shcc]], although
  [[ivaniuk2022-printable-shcc-design]] cites it for "reduced strength in the printing direction". → [[3d-printed-hdc]]
- **Rubber:** crumb rubber lowers f'c in normal PVA-ECC too; optimum 2.5% CR + 2% PVA
  ([[mohammed2020-cr-ecc-elevated-temperature]], p. 6); with 2% PVA, ≈ 75 / 58 / 46 MPa for 0 / 2.5 / 5% CR (Fig. 3, p. 7). → [[crumb-rubber]]

## Round-5 evidence (2026-10-21)
| Source | Material (authors' term) | Specimen | Age | f'c (MPa) |
|---|---|---|---|---|
| [[deng2017-rc-column-hdc-jacket]] Table 5 | XAUAT HDC, Japanese / Chinese PVA; bar-mesh mortar; column concrete | 100 mm cube | n.r. | 60.35 / 61.29; mortar 66.68; concrete 45.40 |
| [[deng2019-urm-shaking-table-hdc]] Table 3 | XAUAT HDC, 2% PVA | 100 mm cube | 28 d | 61.15 |
| [[deng2020-aac-wall-hdc-retrofit]] Table 3 | XAUAT HDC, 1.7% PVA, air-cured | 100 mm cube | ≈ 60 d | 49.80 |
| [[li2021-hdc-beam-shear]] §2.1 | HDC 2% PVA (FA/C 1.0) / C50 concrete | 70.7 mm cube / 100 mm cube | 28 d | 70.55 / 75.77 |
| [[zhang2022-hdc-basalt-textile-tension]] Table 3 | XAUAT HDC Type I (FA/C 1.1) / Type II (HVFA, FA/C 3.25), 0–2% PVA | 100 mm cube | 28 d | 52–58 / 30–38 |
| [[choi2016-pe-alkali-activated-slag-composite]] Table 5 | cementless AAS + 1.75% PE, W/B 0.26 → 0.38 | 50 mm cube | 28 d | 54.8 → 36.3; first-crack/f'c ≈ 9.2% |
| [[pourfalah2018-ecc-high-temperature]] Table 5 | PVA-ECC / H6ECC / H13ECC (PVA + steel), **tested hot** at 20 / 200 / 400 / 600 °C | 50 mm cube | 28 d | ECC 38.8 / 36.15 / 35.1 / 29.2; H6 40.1 / 38.45 / 32 / 27.2; H13 45 / 38.5 / 32.8 / 29.5 |
| [[yun2013-shcc-freeze-thaw]] Table 3, Fig. 4 | hybrid PVA+PE SHCC, W/B 0.45 (PVA/PE 1.30/0.20 vs 0.75/0.75) | n.r. | 39 d ⚠️ | 48.80 vs 43.95; ratio after 300 F-T cycles ≥ 1 in 3 of 4 mixes (ageing to 151 d confounded) |

- **Fibre origin** does not change f_cu (60.35 vs 61.29 MPa, Japanese vs Chinese PVA) ([[deng2017-rc-column-hdc-jacket]], Table 5).
- **HVFA** (FA/C 3.25) lowers f_cu to 30–38 MPa vs 52–58 MPa at FA/C 1.1 ([[zhang2022-hdc-basalt-textile-tension]], Table 3). → [[fly-ash]]
- **More PE** in a PVA+PE hybrid lowers f'c (−10%) and raises air content (13.1 vs 10.4%); W/B 0.45 → 0.55 lowers f'c
  ≈ 19% ([[yun2013-shcc-freeze-thaw]], Table 3, §3.1). → [[hybrid-fiber]]
- **Hot (in-situ) compression:** f'c −10% (ECC) at 400 °C and −25 to −35% at 600 °C; compressive E 40.2 → 19.4 GPa
  (ECC); no spalling to 600 °C ([[pourfalah2018-ecc-high-temperature]], Table 5, §4.2). → [[high-temperature-behaviour]]
- **Cementless binder:** alkali-activated GGBS + PE reaches 54.8 MPa without cement ([[choi2016-pe-alkali-activated-slag-composite]]). → [[alkali-activated-binder]]
- **Same XAUAT matrix, different results:** f_cu 61.15 MPa (2% PVA, 28 d) vs 49.80 MPa (1.7% PVA, air-cured ≈ 2 months)
  ([[deng2019-urm-shaking-table-hdc]]; [[deng2020-aac-wall-hdc-retrofit]]) — different Vf and curing, not a conflict.

> Synthesis: XAUAT PVA-HDC prism strength (50–64 MPa) sits in the same band as other Chinese PVA-HDC
> (Chai 2023 prism 43.1 MPa; Li 2021 cube 45.8 MPa) and normal PVA-ECC (40–70 MPa). Fibers add compressive
> **deformability and residual capacity**, not strength.

## Related
- [[hshdc]] · [[uhpc-vhsc]] · [[mechanical-results]] · [[compressive-constitutive-model]] · [[alkali-activated-binder]] · [[high-temperature-behaviour]]
