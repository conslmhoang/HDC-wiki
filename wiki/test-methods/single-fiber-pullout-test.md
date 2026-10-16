---
type: test-method
slug: single-fiber-pullout-test
aliases: [SFP test, fiber pullout test]
tags: [micromechanics, interface, test]
sources: [ranade2015-hshdc-tensile-rate-effects, li2002-pva-ecc-interface-tailoring, yu2018-ecc-direct-tensile-review]
updated: 2026-10-16
---

# Single-Fiber Pullout Test

## Definition
A single fiber is pulled out of a matrix block while the load–slip curve is recorded. The interface
parameters are fitted from that curve → [[fiber-matrix-interface]].

## Key points
Michigan HSHDC, 6 rates from 9 µm/s to 0.9 m/s, 25 specimens per rate (150 in total)
([[ranade2015-hshdc-tensile-rate-effects]], p. 95–99):
- Specimen types per rate:
  - 10 aligned fibers;
  - 5 at 27° and 5 at 45°;
  - 5 with **Le > 15 mm**, so the fiber ruptures before debonding and gives its in-situ strength and modulus.
- 10 kN system, with a lost-motion grip at the two fastest rates.
- The scatter of the fitted properties grows with rate (lower R², Fig. 12).

## Conflicts & open questions
- No pullout data for the GDUT, Xi'an or Tongji matrices. → [[gaps]]

## PVA setup (Li 2002)
- Saw-cut single-fiber specimen, embedment 0.56–0.71 mm, 10 N load cell, 0.02 mm/s, free length
  ≤ 1 mm, 21 d. The about 0.1 mm displacement at the peak debonding load is subtracted before β is
  computed ([[li2002-pva-ecc-interface-tailoring]], p. 466–467).
- **High-rate pullout** (Curosu 2016, 2 mm embedment, 0.0025 vs 25 s⁻¹, as cited in
  [[yu2018-ecc-direct-tensile-review]], p. 351):
  - PVA in a 24 MPa matrix mostly ruptured;
  - PE in an about 140 MPa matrix plateaued or hardened.
  - Direct single-fiber tension DIFs exceed in-situ pull-out DIFs.

## Related
- [[fiber-matrix-interface]] · [[pe-fiber]] · [[strain-rate-effects]]
