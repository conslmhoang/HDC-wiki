---
type: concept
slug: fiber-bridging
aliases: [crack bridging, σ-δ relation, bridging law, scale-linking model, complementary energy]
tags: [micromechanics, constitutive]
sources: [ranade2015-hshdc-tensile-rate-effects, su2023-rubber-modified-hshdc, yang2024-hshdc-uniaxial-tension, he2024-hdc-research-advances]
updated: 2026-10-06
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

## Related
- [[strain-hardening]] · [[fiber-matrix-interface]] · [[fiber-dispersion]] · [[fiber-geometry]] · [[single-crack-test]]
