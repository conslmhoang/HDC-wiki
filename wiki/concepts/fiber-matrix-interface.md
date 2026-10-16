---
type: concept
slug: fiber-matrix-interface
aliases: [interfacial bond, frictional bond, chemical bond, snubbing, slip hardening, inclination hardening, fiber pullout model]
tags: [micromechanics, interface]
sources: [li1992-steady-state-multiple-cracking, li2002-pva-ecc-interface-tailoring, ranade2015-hshdc-tensile-rate-effects, yang2024-hshdc-uniaxial-tension, su2023-rubber-modified-hshdc, zhang2022-hshdcc-review, yu2018-ecc-direct-tensile-review]
updated: 2026-10-06
---

# Fiber/Matrix Interface Properties

## Definition
| Symbol | Meaning |
|---|---|
| τ0 | frictional bond |
| Gd | chemical debonding energy |
| β | slip hardening |
| f | snubbing coefficient |
| µ | inclination hardening |

These parameters govern single-fiber pullout and therefore [[fiber-bridging]].

## Key points
- **Hydrophilic fibers** (PVA) form both chemical and frictional bonds. **Hydrophobic fibers** (PE)
  and steel form friction only ([[ranade2015-hshdc-tensile-rate-effects]], p. 94–95;
  [[yang2024-hshdc-uniaxial-tension]], p. 5).
- **W/B and FA tune the bond** ([[yang2024-hshdc-uniaxial-tension]], p. 10–11):
  - A lower W/B raises Gd and τ0. Too much bond ruptures fibers; too little lets them slip.
  - FA lowers the bond.
  → [[water-binder-ratio]], [[fly-ash]]
- **Inclination hardening µ** is specific to the very-high-strength Michigan matrix
  (Ranade et al. 2013, as cited in [[ranade2015-hshdc-tensile-rate-effects]], p. 98).
- **Rate dependence** (Michigan HSHDC, 0.009 → 900 mm/s; [[ranade2015-hshdc-tensile-rate-effects]], Fig. 8–9):

  | Parameter | Quasi-static | 900 mm/s | Change |
  |---|---|---|---|
  | τ0 | — | — | +14% |
  | β | 0.003 | 0.006 | ×2 |
  | f | 0.59 | 0.75 | +27% |
  | µ (N/(m·rad)) | 386 | 553 | +43% |

  The interface is fairly rate-insensitive because PE has no chemical bond. → [[strain-rate-effects]]
- β for ECC is about 0.6 (Wang & Li 2007, as cited in [[ranade2015-hshdc-tensile-rate-effects]], p. 98).
  Li 2002 measured **β = 1.15–2.31** for PVA in a w/c 0.45 matrix. This is a refinement, since
  fiber, oiling and matrix differ.
- **PVA interface tailoring** ([[li2002-pva-ecc-interface-tailoring]], Table 3):
  - Oiling from 0 to 1.2% gives τ0 2.44 → 1.11 MPa, Gd 4.71 → 1.61 J/m², β 2.21 → 1.15.
  - Design targets (Wu 2001, as cited): Gd < 2.2 J/m², τ0 1.0–2.1 MPa, β < 1.5.
  - Non-oiled fibers delaminate and rupture with a "pencil-sharpened" end; oiled fibers slide out (Fig. 8–9).
  → [[fiber-surface-treatment]]
- **PE interface in HSHDCC** ([[zhang2022-hshdcc-review]], Table 4):
  - Uncoated PE τ0 ranges 0.42–2.68 MPa and rises with matrix f'c.
  - Coatings raise the bond, but too much bond causes fiber rupture and loss of ε_tu.
- **Classic pullout model** (friction only; [[li1992-steady-state-multiple-cracking]], Eqs. 1–2):
  - debonding: P = (π/2)√((1+η)Ef·df³·τ·δ)·e^{fφ}
  - slippage: P = πτl·df(1 − δ/l)e^{fφ}
  - The snubbing coefficient f is measured at 0.5–1 for fibers in cement (as cited).
- **Rate effects for PVA**: from 10⁻⁵ to 10⁻¹ s⁻¹, bond, matrix toughness and fiber E/strength all
  rise. The PSH energy index falls about 50% (as cited in [[yu2018-ecc-direct-tensile-review]], p. 350).
- **SEM evidence:**
  - PE pull-out holes and scratched fiber ends ([[yang2024-hshdc-uniaxial-tension]], Fig. 11).
  - A gap at the rubber–matrix interface ([[su2023-rubber-modified-hshdc]], Fig. 8).

## Conflicts & open questions
- Measured interface data now exist for PE in the Michigan matrix
  ([[ranade2015-hshdc-tensile-rate-effects]]) and for PVA in a normal matrix
  ([[li2002-pva-ecc-interface-tailoring]]). GDUT, Xi'an and Tongji HSHDC/UHDC still lack pullout data. → [[gaps]]

## Related
- [[fiber-bridging]] · [[single-fiber-pullout-test]] · [[pe-fiber]] · [[pva-fiber]]
