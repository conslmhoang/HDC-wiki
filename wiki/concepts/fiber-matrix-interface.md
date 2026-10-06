---
type: concept
slug: fiber-matrix-interface
aliases: [interfacial bond, frictional bond, chemical bond, snubbing, slip hardening, inclination hardening, fiber pullout model]
tags: [micromechanics, interface]
sources: [ranade2015-hshdc-tensile-rate-effects, yang2024-hshdc-uniaxial-tension, su2023-rubber-modified-hshdc]
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
- **SEM evidence:**
  - PE pull-out holes and scratched fiber ends ([[yang2024-hshdc-uniaxial-tension]], Fig. 11).
  - A gap at the rubber–matrix interface ([[su2023-rubber-modified-hshdc]], Fig. 8).

## Conflicts & open questions
- Only the Michigan matrix has measured τ0, β, f and µ. GDUT and Xi'an HSHDC lack pullout data.
  → [[gaps]]

## Related
- [[fiber-bridging]] · [[single-fiber-pullout-test]] · [[pe-fiber]] · [[pva-fiber]]
