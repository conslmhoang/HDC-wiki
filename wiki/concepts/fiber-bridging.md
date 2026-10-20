---
type: concept
slug: fiber-bridging
aliases: [crack bridging, σ-δ relation, bridging law, scale-linking model, complementary energy]
tags: [micromechanics, constitutive]
sources: [ranade2015-hshdc-tensile-rate-effects, su2023-rubber-modified-hshdc, yang2024-hshdc-uniaxial-tension, he2024-hdc-research-advances, li1992-steady-state-multiple-cracking, li2002-pva-ecc-interface-tailoring, yang2008-ecc-fiber-bridging-law, li2003-ecc-review, jin2019-hvfa-shcc-structural, zhao2022-ecc-tension-damage-model, kunieda2010-uhp-shcc-steel-reinforcement, deng2015-hdc-compressive-toughness, deng2018-hdc-compressive-constitutive, deng2018-hdc-short-columns, mechtcherine2011-shcc-high-strain-rate, li2021-hdc-beam-shear, pourfalah2018-ecc-high-temperature, zhang2022-hdc-basalt-textile-tension]
updated: 2026-10-21
---

# Fiber Bridging & the σ–δ Relation

## Definition
The bridging stress σ that fibers carry across a crack, as a function of the crack opening δ.
- Peak = **bridging capacity σ0**, at opening δ0.
- The area *above* the curve up to δ0 = **complementary energy J′b**, which enters the energy
  criterion → [[strain-hardening]].

## Key points
- **Statistical scale-linking model** (Li, Wang & Backer 1991, as cited as Eq. 1 in
  [[ranade2015-hshdc-tensile-rate-effects]]):

  σ(δ) = (Vf/Af) ∫₀^{π/2} ∫₀^{(Lf/2)cosφ} P(u) p(z) p(φ) dz dφ

  P(u) is the single-fiber pullout law → [[fiber-matrix-interface]]. p(φ) and p(z) are the
  orientation and embedment distributions → [[fiber-dispersion]].
- **Estimating composite properties** from the average σ–δ curve (Yang et al. 2008, as cited):
  - σ_tu ≈ min(σ0) = σ0 × min(Vf)/Vf;
  - average crack width ≈ δ at min(σ0).

  Example at 0.9 mm/s: σ0 = 15.2 MPa, min(Vf) = 0.80 × 2%, so min(σ0) = 12.2 MPa at δ = 112 µm
  ([[ranade2015-hshdc-tensile-rate-effects]], p. 101).
- **Bridging stiffness** (rising slope) is set by fiber modulus and τ0, and controls crack width.
  **Bridging capacity** is set by fiber strength and controls σ_tu (p. 101–102).
  → [[strain-rate-effects]]
- **Measured directly** with a grooved dumbbell (single-crack) test ([[su2023-rubber-modified-hshdc]], p. 3).
  → [[single-crack-test]]

## Quantitative evidence
| Source | Material | σ0 (MPa) | J′b (J/m²) | Note |
|---|---|---|---|---|
| [[ranade2015-hshdc-tensile-rate-effects]] | Michigan HSHDC, quasi-static (analytical) | 11.3 (min σ0) | 969 | about 600 at 900 mm/s |
| [[su2023-rubber-modified-hshdc]] Table 5 | PE6 / PE12 / PE18, PR0 | 8.5 / 16.9 / 20.7 | 423 / 1761 / 2395 | σ0 rises with fiber length |
| same | PE18-PR20 | 22.7 | 3110 | rubber slightly raises σ0 |

## Classic bridging law and the chemical bond (2026-10-16 ingest)
- **Pre-peak law** ([[li1992-steady-state-multiple-cracking]], Eq. 4): σ̃_B = g[2(δ̃/δ̃*)^{1/2} − δ̃/δ̃*],
  with σ0 = Vf·τ·(Lf/df)/2 and the peak at g·σ0. G_r ∝ Vf·g·τ²·(Lf/df)³ (p. 2252). → [[steady-state-cracking]]
- **The chemical bond Gd shifts σ(δ) upward at the start and lowers J′b.** J′b falls by 54% from
  Gd = 1 to 5 J/m² (Lin, Kanda & Li 1999 model, as cited in [[li2002-pva-ecc-interface-tailoring]],
  Fig. 2, p. 465). → [[fiber-surface-treatment]]
- Protruding fiber length on the fracture surface rises from below 1 mm (no oil) to about 2 mm
  (1.2% oil); full pull-out would average 3 mm (p. 471).

## Yang et al. 2008 bridging law (2026-10-20 ingest)
- Adds **two-way pull-out**, **matrix micro-spalling** and the **Cook–Gordon effect** to the 1991 model
  ([[yang2008-ecc-fiber-bridging-law]], Eqs. 3–31). For M45 at 2% PVA the peak changes from 6.2 MPa / 93 µm (one-way) to
  6.3 / 130 (two-way), 6.7 / 131 (+ spalling) and 6.7 / 133 µm (+ Cook–Gordon) (Fig. 14).
  Two-way pull-out raises δ0; spalling raises σ0; Cook–Gordon is negligible for PVA (α = 2df).
- **Weakest-plane method (original)**: the mean curve over-predicts σ_tu by 25%, so bridging Vf is
  taken to vary ±25% between planes (inferred, not measured). σ_tu = the weakest plane; crack width is δ
  read at σ = σ_tu, 37–133 µm, "mean" 62 µm vs about 60 µm measured ([[yang2008-ecc-fiber-bridging-law]], Fig. 13).
  Ranade 2015 adapted this with a *measured* min(Vf) = 0.80·Vf and δ at min(σ0).
- Validated with single-crack tests at 0.1% and 0.5% fiber, assuming 2-D orientation ([[yang2008-ecc-fiber-bridging-law]], Fig. 12).
- The σ–δ curve is "the most fundamental property" linking material and structural design ([[li2003-ecc-review]], p. 217–218).

## Parametric trends and member effects (2026-10-20 ingest)
- **Model sensitivities** (Yang 2008 model with assumed τ0 1.0 MPa, Gd 1.5 J/m², PVA 2%;
  [[jin2019-hvfa-shcc-structural]], Fig. 1): J′b/J_tip falls linearly with Gd, falls steeply then gently with τ0,
  and falls parabolically with Km; σ0 is nearly insensitive to Gd. → [[fiber-matrix-interface]]
- ⚔️ **Vf vs peak stress.** The bridging models give σ0 ∝ Vf ([[yang2008-ecc-fiber-bridging-law]]; [[jin2019-hvfa-shcc-structural]], Fig. 1a),
  but in a FA-rich PVA-ECC σ_p stayed flat (3.10 / 2.96 / 3.23 MPa) from 1% to 2% PVA while ε_p rose 0.51 → 2.00%
  ([[zhao2022-ecc-tension-damage-model]], Table 3). The matrix differs; σ_p may be flaw- or rupture-controlled
  there. → [[gaps]]
- **Rate:** PVA pull-out peak force roughly doubles from 10⁻⁵ to 10 s⁻¹, while single-fiber strength rises only
  1456 → 1674 MPa ([[mechtcherine2011-shcc-high-strain-rate]], Fig. 13, Table 3). Bridging in PVA composites is
  therefore interface-limited at high rate. → [[strain-rate-effects]]
- **Steel reinforcement adds to bridging, not to cracking:** one D6 bar in a 50 × 200 mm UHP-SHCC section adds about
  1.01 MPa to the nominal bridging strength but only about 0.07 MPa to the cracking strength
  ([[kunieda2010-uhp-shcc-steel-reinforcement]], Fig. 3). This raises the strength margin and restores multiple
  cracking in thick members. → [[multiple-cracking]]

## Bridging under compression and shear (XAUAT HDC)
- Bridging across vertical splitting cracks acts as **lateral confinement**. A Mander-type model with
  σ_t = f_t = 5.7 MPa predicts a peak strain of 0.0079 vs 0.0080 measured ([[deng2015-hdc-compressive-toughness]], Eqs. 5–6, p. 5–6).
- Lateral restraint delays longitudinal cracks; once the lateral strain exceeds the HDC ultimate tensile strain,
  fibers pull out or rupture and a major crack forms ([[deng2018-hdc-compressive-constitutive]], p. 3, Fig. 3).
  → [[compressive-constitutive-model]]
- Bridging across diagonal cracks sustains the shear strength of cracked HDC columns and slows stiffness
  degradation ([[deng2018-hdc-short-columns]], p. 8, Conclusion 5). → [[shear-behaviour]]

> Synthesis: the same σ–δ law that governs tensile hardening also explains the compressive toughness and
> shear-crack control of HDC. The tensile strain capacity becomes the limit on confinement
> ([[deng2018-hdc-compressive-constitutive]]), which links compressive design models to the PSH indices.

## Round-5 evidence (2026-10-21)
- **Shear in reinforced HDC beams**: fibre bridging across inclined cracks keeps beams carrying load after the critical
  crack and lets stirrups yield fully ([[li2021-hdc-beam-shear]], §3.3–3.4). → [[shear-behaviour]]
- **Temperature**: bridging switches from PVA rupture (< 150 °C) to pull-out (150 °C) and is gone by 400 °C; steel in HECC
  keeps bridging to 600 °C, ≈ 2× ECC bending load ([[pourfalah2018-ecc-high-temperature]], Figs. 12, 14). → [[high-temperature-behaviour]]
- **Short fibres + textile**: in basalt-textile HDC with 2% PVA, the efficiency factor α > 1 (1.10 / 1.07) at one layer
  suggests that short fibres carry load in addition to the grid ([[zhang2022-hdc-basalt-textile-tension]], Table 8).
  → [[textile-reinforced-hdc]]

## Related
- [[strain-hardening]] · [[fiber-matrix-interface]] · [[fiber-dispersion]] · [[fiber-geometry]] · [[single-crack-test]] · [[compressive-constitutive-model]] · [[textile-reinforced-hdc]]
