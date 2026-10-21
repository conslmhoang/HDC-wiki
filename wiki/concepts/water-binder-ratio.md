---
type: concept
slug: water-binder-ratio
aliases: [W/B, w/cm, water-cement ratio]
tags: [design-variable]
sources: [yang2024-hshdc-uniaxial-tension, he2024-hdc-research-advances, kanda2006-psh-design-criteria, chai2023-hdc-ambient-temperature, zhao2022-ecc-tension-damage-model, deng2015-hdc-compressive-toughness, deng2018-hdc-compressive-constitutive, sun2019-modified-pva-fiber-ecc, ivaniuk2022-printable-shcc-design, zhong2019-ecc-freeze-thaw, gao2020-hdcc-recycled-fine-aggregate, jin2019-hvfa-shcc-structural, zhou2023-hsecc-elevated-temperature, yuan2020-nshsdc-beam-strengthening, lee2021-hsdc-wall-emi-impact, sui2018-uhp-ecc-flexural-fatigue, mohammed2020-cr-ecc-elevated-temperature, choi2016-pe-alkali-activated-slag-composite, yun2013-shcc-freeze-thaw, deng2017-rc-column-hdc-jacket, li2021-hdc-beam-shear, yang2009-ecc-self-healing-wet-dry, lepech2009-ecc-water-permeability, pourfalah2018-ecc-high-temperature]
updated: 2026-10-21
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
  [[he2024-hdc-research-advances]], p. 13). Now primary: W/B 0.45 → 0.55 lowers f'c ≈ 19% and increases the ductility
  loss after 300 F-T cycles ([[yun2013-shcc-freeze-thaw]], §3.1, Conclusion 3). ⚠️ The paper's text says higher W/B gave
  higher tensile strength (Fig. 7), but its Table 3 shows the reverse at 0 cycles (3.77 vs 2.89 MPa). → [[freeze-thaw]]

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
| [[sun2019-modified-pva-fiber-ecc]] Table 10, p. 13 | PVA-ECC 2% | 0.30 vs 0.35 | ε 3.79 vs 3.21% (strain at end of curve incl. softening, not at peak), σ 3.52 vs 3.3 MPa; difference lies within the Fig. 6 error bars (S1 ≈ 2.3–5.25%, S4 ≈ 2.6–3.8%; p. 13); 0.35 chosen for fluidity | 7 d |
| [[ivaniuk2022-printable-shcc-design]] §3.2.3, Table 2, p. 14 | printable PE-SHCC 1.5% | 0.212 → 0.250 (with more cement, needed after adding ethers); W/B is reproduced only if microsilica-suspension water and ≈ 70% of the SP mass are counted (computed; 0.199 → 0.236 without SP water) ⚠️ | σ_tu −24%; strain capacity and f'c unchanged | 28 d |
| [[zhong2019-ecc-freeze-thaw]] Fig. 16, p. 16; Table 8, p. 18 | PVA "ECC" (flexure only) | 0.25 → 0.50 | all frost-failure indices fall as W/B rises; W/B is the largest factor for UF (38.47%); Taguchi optimum W/B 0.25 | F–T |
| [[gao2020-hdcc-recycled-fine-aggregate]] Table 3 | PVA-HDCC | 0.25 (bending, compression) / 0.45, no SP (tension) | two different matrices; f_c of the 0.45 tension series not reported (≈ 39–43 MPa implied by the Eq. 6 normalisation in Fig. 19, p. 15, computed); the 0.25 bending series has f_c 70.9–84.9 MPa (Fig. 9a, p. 9) | 28 d |

- Other matrices: Deng XAUAT PVA-HDC W/B 0.29 ([[deng2015-hdc-compressive-toughness]], Table 2, "water-cement" ⚠️);
  Jin HVFA PVA-SHCC 0.25 ([[jin2019-hvfa-shcc-structural]]); Guangzhou HSECC 0.20 ([[zhou2023-hsecc-elevated-temperature]]);
  Korea Univ. NSHSDC/HSDC 0.172 ([[yuan2020-nshsdc-beam-strengthening]]; [[lee2021-hsdc-wall-emi-impact]]);
  UHP-ECC 0.135–0.144 ([[sui2018-uhp-ecc-flexural-fatigue]]).
- ⚠️ [[mohammed2020-cr-ecc-elevated-temperature]] states W/B 0.32 (text, pp. 4–5), but its Table 3 (p. 5) gives 0.146
  (0.32 is w/c); both are printed in the PDF, so this stays unresolved.

> Synthesis: in normal-strength PVA systems a higher W/B usually raises ductility ([[zhao2022-ecc-tension-damage-model]],
> [[kanda2006-psh-design-criteria]], [[chai2023-hdc-ambient-temperature]]). It lowers frost resistance
> ([[zhong2019-ecc-freeze-thaw]]) and compressive strength, so ductility and durability pull W/B in opposite directions.
> In compression the Deng series shows an interior optimum (0.29), as the Xi'an HSHDC does in tension (0.16).

- ⚔️ (weakened 2026-10-21) [[sun2019-modified-pva-fiber-ecc]] reports the *lower* W/B (0.30) as more ductile than 0.35 at
  7 d (3.79 vs 3.21%). This runs against the trend in [[zhao2022-ecc-tension-damage-model]] (0.24 → 0.28: ε ×4) and
  [[chai2023-hdc-ambient-temperature]]. But the PDF re-check shows (i) Sun's "ultimate strain" is the strain at the end
  of the curve including the softening branch, not at peak, and (ii) the 0.58-point difference lies inside the Fig. 6
  error bars (p. 13). So Sun's result is better read as "no significant W/B effect" than as a counter-trend. Ranges and
  ages also differ (7 d vs ≥ 28 d). → [[gaps]]

## Round 5 evidence (2026-10-21)
| Source | Term / fiber | W/B (mass) | Effect | Age |
|---|---|---|---|---|
| [[choi2016-pe-alkali-activated-slag-composite]] Table 7 | cementless alkali-activated slag + 1.75% PE, no aggregate | 0.26 → 0.30 → 0.34 → 0.38 | f'c 54.8 → 36.3 MPa; σ_tu 13.06 → 5.06 MPa (−61.3%); ε 7.50 → 4.58% (−38.9%); **lower W/B more ductile**, most and narrowest cracks at 0.26 | 28 d |
| [[yun2013-shcc-freeze-thaw]] Table 3 | hybrid PVA + PE SHCC 1.5% | 0.45 vs 0.55 | f'c −19%; more ductility loss after F-T | 14–39 d ⚠️ / 151 d |

- Other matrices: XAUAT PVA-HDC W/B 0.29 with FA/C 1.0 ([[deng2017-rc-column-hdc-jacket]], Table 1; [[li2021-hdc-beam-shear]],
  Table 1); Michigan M45 0.25 computed ([[yang2009-ecc-self-healing-wet-dry]]; [[lepech2009-ecc-water-permeability]]);
  Heriot-Watt ECC 0.28 derived ([[pourfalah2018-ecc-high-temperature]]).
- ⚔️ Choi 2016 joins [[sun2019-modified-pva-fiber-ecc]] (weak, within scatter — see above) on the "lower W/B is more ductile" side, against
  [[zhao2022-ecc-tension-damage-model]] and [[chai2023-hdc-ambient-temperature]]. The Choi matrix is cementless, has no
  aggregate and uses PE (no chemical bond), so the bond-weakening argument for high W/B in PVA systems does not apply; a
  stronger matrix there raises PE friction and bridging strength (σ_tu ×2.6). → [[alkali-activated-binder]], [[gaps]]

> Synthesis (round 5): the W/B effect on ductility depends on the fibre–matrix pair. With hydrophilic PVA, a higher W/B
> weakens an over-strong bond and helps (Zhao, Chai, Kanda). With hydrophobic PE in a toughness-limited matrix (no sand),
> a lower W/B helps (Choi). Optima appear where both effects meet (Xi'an HSHDC 0.16).

## Related
- [[mix-designs]] · [[fly-ash]] · [[strain-hardening]] · [[freeze-thaw]] · [[compressive-constitutive-model]] · [[viscosity-modifying-admixtures]] · [[alkali-activated-binder]]
