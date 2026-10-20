---
type: concept
slug: water-binder-ratio
aliases: [W/B, w/cm, water-cement ratio]
tags: [design-variable]
sources: [yang2024-hshdc-uniaxial-tension, he2024-hdc-research-advances, kanda2006-psh-design-criteria, chai2023-hdc-ambient-temperature, zhao2022-ecc-tension-damage-model, deng2015-hdc-compressive-toughness, deng2018-hdc-compressive-constitutive, sun2019-modified-pva-fiber-ecc, ivaniuk2022-printable-shcc-design, zhong2019-ecc-freeze-thaw, gao2020-hdcc-recycled-fine-aggregate, jin2019-hvfa-shcc-structural, zhou2023-hsecc-elevated-temperature, yuan2020-nshsdc-beam-strengthening, lee2021-hsdc-wall-emi-impact, sui2018-uhp-ecc-flexural-fatigue, mohammed2020-cr-ecc-elevated-temperature]
updated: 2026-10-20
---

# Water/Binder Ratio

## Key points
- **Xi'an HSHDC, W/B 0.14 / 0.16 / 0.18** ([[yang2024-hshdc-uniaxial-tension]], Table 6, p. 10):

  | W/B | εp (%) |
  |---|---|
  | 0.14 | 0.811 |
  | **0.16** | **3.839** (optimum) |
  | 0.18 | 1.888 |

  Explanation: a W/B that is too low raises the bond (Gd, τ0) so fibers rupture; one that is too high
  weakens the bond so fibers slip. From 0.14 to 0.18, σcr falls 13.7%. → [[fiber-matrix-interface]]
- High vs low W/B affects the freeze–thaw response of hybrid SHCC (Yun 2013, as cited in
  [[he2024-hdc-research-advances]], p. 13). → [[durability]]

## Further evidence (2026-10-20 ingest)
- Paste + SF composites: w/c 0.27 → 0.42 raises ε_cu from 0.26 to 0.55% (14 µm PVA) and from 1.03 to
  1.50% (40 µm PVA), by lowering σ_fc and J_tip while J′b stays about the same ([[kanda2006-psh-design-criteria]], Table 4, Figs. 8–9).
- Chinese PVA-HDC: W/B 0.31 → 0.20 raises f_cu 47.8 → 59.0 MPa and lowers ε_tu 0.64 → 0.42% ([[chai2023-hdc-ambient-temperature]], Table 4).

> Synthesis: in PVA systems a *higher* W/B tends to help ductility (weaker matrix, weaker bond), whereas
> the Xi'an PE/PVA HSHDC showed an optimum at 0.16. Matrix strength class matters.


## Round 4 evidence (2026-10-20)
| Source | Term / fiber | W/B (mass) | Effect | Age |
|---|---|---|---|---|
| [[zhao2022-ecc-tension-damage-model]] Table 3 | PVA-ECC 2%, FA/C 2.0 | 0.24 → 0.25 → 0.28 | σ_k 3.44 → 2.67 → 2.45 MPa; σ_p 4.57 → 3.79 → 3.23 MPa; ε_p 0.50 → 1.07 → 2.00% (×4). Workable window 0.24–0.30 (§2.1) | ≥ 35 d ⚠️ |
| [[deng2018-hdc-compressive-constitutive]] Table 3, Fig. 5b | PVA-HDC 2%, FA 50% (compression) | 0.26 / **0.29** / 0.32 | prism σ0 56.04 / **62.25** / 52.84 MPa; 0.29 gives the highest strength and strain | n.r. |
| [[sun2019-modified-pva-fiber-ecc]] Table 10 | PVA-ECC 2% | 0.30 vs 0.35 | ε 3.79 vs 3.21%, σ 3.52 vs 3.3 MPa; 0.35 chosen for fluidity | 7 d |
| [[ivaniuk2022-printable-shcc-design]] §3.2.3, Table 2 | printable PE-SHCC 1.5% | 0.212 → 0.250 (with more cement, needed after adding ethers) | σ_tu −24%; strain capacity and f'c unchanged | 28 d |
| [[zhong2019-ecc-freeze-thaw]] Fig. 16, Table 8 | PVA "ECC" (flexure only) | 0.25 → 0.50 | all frost-failure indices fall as W/B rises; W/B is the largest factor for UF (38.47%); Taguchi optimum W/B 0.25 | F–T |
| [[gao2020-hdcc-recycled-fine-aggregate]] Table 3 | PVA-HDCC | 0.25 (bending, compression) / 0.45, no SP (tension) | two different matrices; f_c of the tension series not reported | 28 d |

- Other matrices: Deng XAUAT PVA-HDC W/B 0.29 ([[deng2015-hdc-compressive-toughness]], Table 2, "water-cement" ⚠️);
  Jin HVFA PVA-SHCC 0.25 ([[jin2019-hvfa-shcc-structural]]); Guangzhou HSECC 0.20 ([[zhou2023-hsecc-elevated-temperature]]);
  Korea Univ. NSHSDC/HSDC 0.172 ([[yuan2020-nshsdc-beam-strengthening]]; [[lee2021-hsdc-wall-emi-impact]]);
  UHP-ECC 0.135–0.144 ([[sui2018-uhp-ecc-flexural-fatigue]]).
- ⚠️ [[mohammed2020-cr-ecc-elevated-temperature]] states W/B 0.32, but its Table 3 gives 0.146 (0.32 is w/c).

> Synthesis: in normal-strength PVA systems a higher W/B usually raises ductility ([[zhao2022-ecc-tension-damage-model]],
> [[kanda2006-psh-design-criteria]], [[chai2023-hdc-ambient-temperature]]). It lowers frost resistance
> ([[zhong2019-ecc-freeze-thaw]]) and compressive strength, so ductility and durability pull W/B in opposite directions.
> In compression the Deng series shows an interior optimum (0.29), as the Xi'an HSHDC does in tension (0.16).

- ⚔️ [[sun2019-modified-pva-fiber-ecc]] found the *lower* W/B (0.30) more ductile than 0.35 at 7 d (3.79 vs 3.21%). This runs
  against the trend in [[zhao2022-ecc-tension-damage-model]] (0.24 → 0.28: ε ×4) and [[chai2023-hdc-ambient-temperature]].
  The ranges and ages differ (7 d vs ≥ 28 d). → [[gaps]]

## Related
- [[mix-designs]] · [[fly-ash]] · [[strain-hardening]] · [[freeze-thaw]] · [[compressive-constitutive-model]] · [[viscosity-modifying-admixtures]]
