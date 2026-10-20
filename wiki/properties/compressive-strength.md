---
type: property
slug: compressive-strength
aliases: [f'c, fc, uniaxial compression]
tags: [compression]
sources: [ranade2017-hshdc-impact-resistance, su2023-rubber-modified-hshdc, yang2024-hshdc-uniaxial-tension, ye2021-uhdc-flexural-size-effect, he2024-hdc-research-advances, zhang2022-hshdcc-review, ma2021-ecc-durability-review, chai2023-hdc-ambient-temperature, li2021-hdc-sulfate-dry-wet, deng2015-hdc-compressive-toughness, deng2018-hdc-compressive-constitutive, deng2018-hdc-short-columns, chavesfigueiredo2020-printed-shcc, ivaniuk2022-printable-shcc-design, gao2020-hdcc-recycled-fine-aggregate, jin2019-hvfa-shcc-structural, mohammed2020-cr-ecc-elevated-temperature, ozbay2013-ecc-self-healing-sustained-load, shumuye2022-slag-fa-pe-ecc, sui2018-uhp-ecc-flexural-fatigue, sun2019-modified-pva-fiber-ecc, wang2019-rc-beam-ecc-shear-strengthening, wang2023-ecc-frost-damage, zhou2023-hsecc-elevated-temperature, kunieda2010-uhp-shcc-steel-reinforcement]
updated: 2026-10-20
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
| [[chai2023-hdc-ambient-temperature]] Table 5 | Chinese PVA-HDC C40 | 100 mm cube / prism | 28 d | f_cu 48.0; prism 43.1 (f_c/f_cu 0.90 vs 0.76 for concrete); E 23.2–24.1 GPa |
| [[li2021-hdc-sulfate-dry-wet]] Table 4 | XUT PVA-HDC (FA/C 1.0) | 100 mm cube | 90 d | 45.8; drum-shaped failure (cracked, not scattered) |

- 8 h exposure at −30 to 60 °C changes f_cu only −2.7% to +9.8% ([[chai2023-hdc-ambient-temperature]], Table 5). → [[high-temperature-behaviour]]
- Under sulfate plus dry–wet cycles, f_cu first rises then falls; the water control also rises 39%
  (45.8 → 63.6 MPa), so part of the early gain is continued hydration ([[li2021-hdc-sulfate-dry-wet]], Table 4). → [[durability]]

## Round-4 evidence (2026-10-20, 34-source ingest)
| Source | Material (authors' term) | Specimen | Age | f'c (MPa) |
|---|---|---|---|---|
| [[deng2015-hdc-compressive-toughness]] Table 3 | XAUAT matrix / PVA-HDC 1.0 / 1.5 / 2.0% | 100 × 100 × 300 prism | about 10 months | 64.0 (computed from 640.45 kN; text 63.06) / 50.3 / 56.9 / 62.3 (computed) |
| [[deng2018-hdc-compressive-constitutive]] Table 3 | XAUAT matrix / 9 PVA-HDC mixes | 100 × 100 × 300 prism | n.r. ⚠️ | 63.06 / 50.3–64.4 |
| [[deng2018-hdc-short-columns]] Table 4 | XAUAT PVA-HDC 2% vs companion concrete | 100 mm cube | n.r. | 65.7 vs 68.9 |
| [[wang2019-rc-beam-ecc-shear-strengthening]] Table 1 | PVA-ECC 1.5% | 100 mm cube | 28 d | 55.9 (CoV 4.2%); E 24.9 GPa |
| [[ozbay2013-ecc-self-healing-sustained-load]] Table 3 | PVA-ECC FA/C 1.2 / 2.2 | 50 mm cube | 28 d | 69.3 / 46.1 |
| [[wang2023-ecc-frost-damage]] Table 4 | PVA-ECC vs W/C 0.5 concrete | n.r. | 28 d | 46.8 vs 42.92 |
| [[sun2019-modified-pva-fiber-ecc]] Table 8 | WUT matrix → 2% PVA | n.r. | 28 d | 44.4 → 40.6 |
| [[jin2019-hvfa-shcc-structural]] Fig. 8a | HVFA-SHCC, 6 mixes | 100 × 100 × 300 prism | 28 d | all > 30; falls with FA/C; +12% at 90 d |
| [[shumuye2022-slag-fa-pe-ecc]] Sect. 3.1 | PE-ECC, slag 0 / 15% | n.r. | 28 d | 40.79 / 55.05 (+34.9%) |
| [[mohammed2020-cr-ecc-elevated-temperature]] Fig. 2 | crumb-rubber PVA-ECC (RSM) | n.r. | 28 d | 30–75 |
| [[sui2018-uhp-ecc-flexural-fatigue]] Sect. 2.2 | PE UHP-ECC | cube | 28 d / 90 d | 102.8 / 120.7 |
| [[kunieda2010-uhp-shcc-steel-reinforcement]] Table 2 | UHP-SHCC (PE) | n.r. | 28 d | 95 |
| [[zhou2023-hsecc-elevated-temperature]] Table 5 | "HSECC" PVA + steel (no strain hardening shown) | 100 mm cube | at 30 °C | 75–94 |
| [[ivaniuk2022-printable-shcc-design]] Tables 2–3 | printed PE-SHCC | 40 mm cube | 28 d | 73–83 |
| [[chavesfigueiredo2020-printed-shcc]] Table 2 | printed PVA-SHCC, mixes X / Y; loaded ⟂ / ∥ to layers | 35 mm cube | 28 d | X 44.09 / 41.93; Y 17.66 / 15.02 |
| [[gao2020-hdcc-recycled-fine-aggregate]] Fig. 9a | HDCC with recycled vs river fine aggregate | n.r. | 28 d | RFA +6.67 to +18.45%; absolute values not in text ⚠️ |

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
- **Slag** raises PE-ECC f'c (28 d +3.5 / +28.5 / +34.9% for 5 / 10 / 15%) ([[shumuye2022-slag-fa-pe-ecc]]). → [[ggbfs]]
- **HVFA:** 28 d f'c underestimates later strength (+12% at 90 d), and E is lower than ordinary concrete
  ([[jin2019-hvfa-shcc-structural]], Fig. 8). XAUAT HDC also has a lower E than concrete, which lowers the initial
  stiffness of HDC columns ([[deng2018-hdc-short-columns]], Fig. 10).
- **Recycled fine aggregate** raises f'c by 6.67–18.45% at W/B 0.25; Vf 0–2% has little effect
  ([[gao2020-hdcc-recycled-fine-aggregate]], §3.2). → [[recycled-fine-aggregate]]
- **Printing:** direction effect on f'c is small (5–15%) in [[chavesfigueiredo2020-printed-shcc]], although
  [[ivaniuk2022-printable-shcc-design]] cites it for "reduced strength in the printing direction". → [[3d-printed-hdc]]
- **Rubber:** crumb rubber lowers f'c in normal PVA-ECC too; optimum 2.5% CR + 2% PVA
  ([[mohammed2020-cr-ecc-elevated-temperature]]). → [[crumb-rubber]]

> Synthesis: XAUAT PVA-HDC prism strength (50–64 MPa) sits in the same band as other Chinese PVA-HDC
> (Chai 2023 prism 43.1 MPa; Li 2021 cube 45.8 MPa) and normal PVA-ECC (40–70 MPa). Fibers add compressive
> **deformability and residual capacity**, not strength.

## Related
- [[hshdc]] · [[uhpc-vhsc]] · [[mechanical-results]] · [[compressive-constitutive-model]]
