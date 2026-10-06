---
type: test-method
slug: single-fiber-pullout-test
aliases: [SFP test, fiber pullout test]
tags: [micromechanics, interface, test]
sources: [ranade2015-hshdc-tensile-rate-effects]
updated: 2026-10-06
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

## Related
- [[fiber-matrix-interface]] · [[pe-fiber]] · [[strain-rate-effects]]
