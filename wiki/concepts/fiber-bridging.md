---
type: concept
slug: fiber-bridging
aliases: [crack bridging, σ-δ relation, bridging law, scale-linking model, complementary energy]
tags: [micromechanics, constitutive]
sources: [ranade2015-hshdc-tensile-rate-effects, su2023-rubber-modified-hshdc, yang2024-hshdc-uniaxial-tension, he2024-hdc-research-advances, li1992-steady-state-multiple-cracking, li2002-pva-ecc-interface-tailoring, yang2008-ecc-fiber-bridging-law, li2003-ecc-review]
updated: 2026-10-20
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

## Related
- [[strain-hardening]] · [[fiber-matrix-interface]] · [[fiber-dispersion]] · [[fiber-geometry]] · [[single-crack-test]]
