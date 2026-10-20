---
type: test-method
slug: single-crack-test
aliases: [notched dumbbell test, grooved specimen, crack bridging test, σ-δ test]
tags: [bridging, test]
sources: [su2023-rubber-modified-hshdc, yang2008-ecc-fiber-bridging-law, kunieda2006-hpfrcc-japan-applications, xue2023-shcc-structural-review, chavesfigueiredo2020-printed-shcc, yang2009-ecc-self-healing-wet-dry, lepech2009-ecc-water-permeability]
updated: 2026-10-21
---

# Single-Crack Tension Test

## Definition
A tension test on a grooved or notched specimen that forces **one** crack, so the bridging stress
against crack opening (σ–δ) curve can be measured directly → [[fiber-bridging]].

## Key points
- GDUT: grooved dumbbell, opening measured over 20 mm, 0.5 mm/min. The notch depth could not be
  read from the paper ⚠️ ([[su2023-rubber-modified-hshdc]], p. 3).
- The results (σ0, J′b) feed the PSH indices → [[strain-hardening]].

## Yang et al. 2008 setup
- Notched coupon 13 × 76 × 90 mm, 6 mm lateral and 2 mm face notches, 0.0001 mm/s, two 5 mm
  extensometers; fiber content cut to 0.1% and 0.5% so only one crack forms ([[yang2008-ecc-fiber-bridging-law]], p. 188, Figs. 10–12).

## Single cracks for durability tests
- Self-healing thresholds from single-crack specimens: a 0.5 vol.% PVA **tension-softening mortar** (not ECC) was cracked
  to a controlled width; after 10 wet–dry cycles, cracks < 50 µm recovered fully (resonant frequency and permeability),
  50–150 µm partly, > 150 µm not at all ([[yang2009-ecc-self-healing-wet-dry]], Figs. 4–5, p. 385–387). → [[self-healing]]
- To compare multiply-cracked ECC with single-crack permeability data, divide k by the number of cracks
  ([[lepech2009-ecc-water-permeability]], p. 749). → [[permeability]]

## Related crack-based tests
- **Zero-span tension test** (JSCE K-532-1999, 40 × 120 mm, artificial crack) exists for coatings; Kunieda &
  Rokugo say it should be developed for HPFRCC repair layers ([[kunieda2006-hpfrcc-japan-applications]], p. 23, Fig. 10).
  Thin SHCC strengthening layers crack over the substrate crack in this way ([[xue2023-shcc-structural-review]], Section 4.1.2).
  → [[repair-and-field-applications]]
- PSH energy terms (J_tip, J_b) can also be taken from a notched 3PB test ([[chavesfigueiredo2020-printed-shcc]], Table 3)
  → [[notched-beam-three-point-bending]].

## Related
- [[fiber-bridging]] · [[dogbone-uniaxial-tension]] · [[notched-beam-three-point-bending]] · [[self-healing]] · [[permeability]]
