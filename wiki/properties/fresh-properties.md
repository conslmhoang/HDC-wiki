---
type: property
slug: fresh-properties
aliases: [rheology, workability, slump, plastic viscosity, yield stress]
tags: [fresh, processing]
sources: [ranade2017-hshdc-impact-resistance, su2023-rubber-modified-hshdc, zhang2022-hshdcc-review, chavesfigueiredo2020-printed-shcc, ivaniuk2022-printable-shcc-design, sun2019-modified-pva-fiber-ecc, kanda2003-sprayed-ecc, yuan2020-nshsdc-beam-strengthening]
updated: 2026-10-20
---

# Fresh Properties & Rheology

## Quantitative evidence
| Source | Matrix | Plastic viscosity (Pa·s) | Yield stress (Pa) | Slump |
|---|---|---|---|---|
| [[ranade2017-hshdc-impact-resistance]] p. 25 | Michigan HSHDC | 6.0 | 186.2 | about 190 mm |
| same | Cor-Tuf | 5.5 | 170 | about 190 mm |

## Key points
- Too much powder rubber (about 35 vol.% or more) raises plastic viscosity so much that fibers
  agglomerate; above 40% the mix is unworkable ([[su2023-rubber-modified-hshdc]], p. 3, 7, 9).
  No rheology was measured in that study. → [[fiber-dispersion]]

## HSHDCC workability ([[zhang2022-hshdcc-review]], Table 5, p. 6–7)
- Mini-slump is typically 145–200 mm: coarse sand gives 160–180 mm, fine sand 145 mm.
- LC³ raises flow, and grafted SF gave a matrix mini-slump of 335 mm. Porous aggregates should be pre-wetted.


## Round 4 evidence (2026-10-20)
| Source | Material | Measure | Value |
|---|---|---|---|
| [[chavesfigueiredo2020-printed-shcc]] Sect. 2.1 | printable PVA-SHCC X / Y | bulk / shear yield stress (ram extruder, Benbow–Bridgwater) | 34.74 / 4.41 kPa (X); 34.26 / 2.49 kPa (Y) |
| [[ivaniuk2022-printable-shcc-design]] Sect. 3.1.1 | printable PE-SHCC | flow-table spread loss after 3 h (EN 1015-3) | Ref 12.7%, starch ether 10.9%, starch + cellulose ether 5.5% |
| [[sun2019-modified-pva-fiber-ecc]] Tables 6–7 | PVA-ECC | spread; thixotropy | 1.8% PCE + HPMC (5 × 10⁴ mPa·s): 325 mm and lowest thixotropy (9911 Pa·s⁻¹ at 1 min) |
| [[kanda2003-sprayed-ecc]] Table 5 | sprayed ECC | table flow; air content | 174–183 mm after mixing, 162–174 mm after spraying; air 12.5–25% → 6.6–8.4% (pumping squeezes out air) |
| [[yuan2020-nshsdc-beam-strengthening]] | NSHSDC | slump | "no-slump", shape-holding for in-situ jacketing (§1) |

- **Admixtures:** cellulose ether (0.075% of binder) gave the highest water retention and longest open time; starch ether
  alone lost retention within 20 min; adding ethers forced W/B up from 0.212 to 0.250 ([[ivaniuk2022-printable-shcc-design]],
  Fig. 10, Sect. 2.1). More or higher-viscosity HPMC raises initial viscosity; shear breaks HPMC chains
  ([[sun2019-modified-pva-fiber-ecc]], §3.1). A urethane moisturizing agent (0.8% of binder) aided anti-segregation and flow
  in sprayed ECC but entrained > 20% air ([[kanda2003-sprayed-ecc]], p. 272). → [[viscosity-modifying-admixtures]]
- **Test-method caution:** tack, cylinder-pull and inclined-table tests misranked adhesiveness of printable SHCC because of
  bleed water ([[ivaniuk2022-printable-shcc-design]], Sect. 3.1.3).
- **Air voids:** HPMC may raise air voids in printed SHCC, and high air content lowers ductility
  ([[chavesfigueiredo2020-printed-shcc]], Sects. 3.5–3.6). → [[fiber-dispersion]], [[3d-printed-hdc]]

> Synthesis: no round-4 source links a measured rheological parameter to fiber dispersion or ε_tu. The fresh-state data
> are process-specific (spraying, printing) and use different tests, so they cannot be compared directly.

## Related
- [[fiber-dispersion]] · [[mix-designs]] · [[viscosity-modifying-admixtures]] · [[3d-printed-hdc]]
