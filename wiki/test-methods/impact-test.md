---
type: test-method
slug: impact-test
aliases: [drop-weight test, drop hammer, repeated impact test, incremental drop-weight test]
tags: [dynamic, test]
sources: [ranade2017-hshdc-impact-resistance, lee2021-hsdc-wall-emi-impact, mechtcherine2011-shcc-high-strain-rate]
updated: 2026-10-20
---

# Drop-Weight Impact Test

## Setups compared
| Source | Material (authors' term) | Specimen | Impactor | Drop height | Supports | Instrumentation | Failure criterion |
|---|---|---|---|---|---|---|---|
| [[ranade2017-hshdc-impact-resistance]] (p. 28–29, Figs. 3–4) | HSHDC (Michigan), unreinforced | slab 300 × 300 × 25 mm, 2 per case | 16.04 kg, 75 mm (instrumented) or 50 mm hemispherical head | 0.35 / 0.70 / 1.40 m (2.30 / 3.25 / 4.60 m/s), fixed, up to 20 blows | shown only in Fig. 3c ⚠️ | 3 × 44.5 kN load cells, 2 accelerometers (±1500 g), 200 kHz, displacement by double integration, 30 fps video | almost zero rebound |
| [[lee2021-hsdc-wall-emi-impact]] (§2.3, Fig. 4) | HSDC (Korea Univ., 1.0% steel + 0.5% PE) skins on NC | panel 300 × 300 mm, 100–300 mm thick, HSDC 5/10/20 mm on one or both faces; 1 panel per case | 100 kg, 70 mm cylinder-frustum head | 200 mm, **+100 mm per blow** until failure | clear span 250 mm, all edges fixed | 2 support load cells, laser displacement sensor at bottom centre, 200 kHz | failure (scabbing / perforation); crack count and max width per blow (method not stated) |

## Key points
- Ranade 2017: a single impact runs in three stages S1–S3, with peak contact force (PCF) at about 0.04 ms.
  PCF is sensitive to surface roughness and sampling rate ([[ranade2017-hshdc-impact-resistance]], p. 29, 31).
- Lee 2021 uses an **incremental-height** protocol, so the output is total imparted energy to failure rather
  than blows at a fixed energy. H20D (20 mm on both faces) took > 5× the energy of H5S
  ([[lee2021-hsdc-wall-emi-impact]], Fig. 11). Results are not directly comparable with fixed-height tests.
- Lee 2021 combines impact with EMI shielding measured before and after impact (§3.2.2). → [[extreme-loading-applications]]
- Hopkinson-bar spallation of SHCC at 140–180 s⁻¹ gave a strength DIF of 6.7 (Millon et al. 2010, as cited in
  [[mechtcherine2011-shcc-high-strain-rate]], p. 58). → [[strain-rate-effects]]

> Synthesis: the two primary drop-weight studies differ in mass (16 vs 100 kg), head shape, protocol
> (fixed vs incremental height), specimen (thin unreinforced slab vs composite NC panel) and n (2 vs 1).
> Only qualitative comparison is possible.

## Conflicts & open questions
- Higher sampling rates are recommended. The 50 mm-head series in Ranade 2017 had no instrumentation.
- Lee 2021: one panel per configuration, small 250 mm span; panel test age not stated ⚠️.
- No standard impact test for HDC in the corpus.

## Related
- [[impact-resistance]] · [[strain-rate-effects]] · [[extreme-loading-applications]] · [[hybrid-fiber]]
