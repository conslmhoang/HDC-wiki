---
type: property
slug: fresh-properties
aliases: [rheology, workability, slump, plastic viscosity, yield stress]
tags: [fresh, processing]
sources: [ranade2017-hshdc-impact-resistance, su2023-rubber-modified-hshdc, zhang2022-hshdcc-review, chavesfigueiredo2020-printed-shcc, ivaniuk2022-printable-shcc-design, sun2019-modified-pva-fiber-ecc, kanda2003-sprayed-ecc, yuan2020-nshsdc-beam-strengthening, choi2016-pe-alkali-activated-slag-composite, yun2013-shcc-freeze-thaw, hieu2023-aas-extremely-ductile-22pct, huy2023-egc-activator-pretreatment]
updated: 2026-10-26
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
| [[ivaniuk2022-printable-shcc-design]] Sect. 3.1.1, p. 9 | printable PE-SHCC | flow-table spread loss after 3 h (EN 1015-3) | Ref 12.7%, starch ether 10.9%, starch + cellulose ether 5.5%; spread after strokes ≈ 20 → 180 min: Ref ≈ 14.2 → 12.4, SE ≈ 14.7 → 13.1, SE-CE ≈ 11.8 → 11.1 cm (read from Fig. 8, p. 9) |
| same, Figs. 9–12, pp. 10–12 | Ref / SE / SE-CE | shape retention; water retention; adhesiveness | demoulded cone top/base Ref 90/104 vs SE-CE 70/100 mm (Fig. 9 labels); water retention 5 → 20 min Ref ≈ 98.9 → 98.3, SE ≈ 99.2 → 98.4, SE-CE ≈ 99.2 → 98.6% (Fig. 10); tack ≈ 3.0 / 3.4 N, cylinder pull ≈ 5.6 / 9.6 N, inclined table ≈ 11° / 21° (Ref / SE-CE; Fig. 11b, p. 11; Fig. 12b, p. 12) — read-offs |
| [[sun2019-modified-pva-fiber-ecc]] Tables 6–7 | PVA-ECC | spread; thixotropy | 1.8% PCE + HPMC (5 × 10⁴ mPa·s): 325 mm and lowest thixotropy (9911 Pa·s⁻¹ at 1 min) |
| [[kanda2003-sprayed-ecc]] Table 5 | sprayed ECC | table flow; air content | 174–183 mm after mixing, 162–174 mm after spraying; air 12.5–25% → 6.6–8.4% (pumping squeezes out air) |
| [[yuan2020-nshsdc-beam-strengthening]] | NSHSDC | slump | "no-slump", shape-holding for in-situ jacketing (§1) |

- **Admixtures:** cellulose ether (0.075% of binder) gave the highest water retention and longest open time; starch ether
  alone lost retention within 20 min; adding ethers forced W/B up from 0.212 to 0.250 ([[ivaniuk2022-printable-shcc-design]],
  Fig. 10, p. 10; Sect. 2.1, p. 5). These W/B values are reproduced only if suspension water and ≈ 70% of the SP are
  counted as water (computed in the source page; SP solids not stated ⚠️). More or higher-viscosity HPMC raises initial viscosity; shear breaks HPMC chains
  ([[sun2019-modified-pva-fiber-ecc]], §3.1). A urethane moisturizing agent (0.8% of binder) aided anti-segregation and flow
  in sprayed ECC but entrained > 20% air ([[kanda2003-sprayed-ecc]], p. 272). → [[viscosity-modifying-admixtures]]
- **Test-method caution:** tack, cylinder-pull and inclined-table tests misranked adhesiveness of printable SHCC because of
  bleed water ([[ivaniuk2022-printable-shcc-design]], Sect. 3.1.3, pp. 10–11).
- **Air voids:** HPMC may raise air voids in printed SHCC, and high air content lowers ductility
  ([[chavesfigueiredo2020-printed-shcc]], Sects. 3.5–3.6). → [[fiber-dispersion]], [[3d-printed-hdc]]

## Round 5 evidence (2026-10-21)
- **Viscosity control for PE in an alkali-activated slag paste**: HRWRA 0.024 → 0.002 and VMA 0 → 0.0003 (by binder
  mass) as W/B rose 0.26 → 0.38, tuned after Li & Li 2013; hardened densities within 0.5% of theoretical, so no
  unintended pores ([[choi2016-pe-alkali-activated-slag-composite]], Table 1, §2.1, §3.1). No rheology numbers given.
  → [[alkali-activated-binder]], [[viscosity-modifying-admixtures]]
- **Air content in hybrid PVA+PE SHCC**: 10.0–13.1% without deliberate air entrainment; the mix with more PE (0.75%)
  had 13.1% vs 10.4% at W/B 0.45, with lower f'c; PE multifilament is hard to disperse
  ([[yun2013-shcc-freeze-thaw]], Table 3, p. 13–14). → [[pe-fiber]], [[hybrid-fiber]]

## Round 7 evidence (2026-10-26)
- **SP dose vs setting in AAS**: ED-AASC needed 0.106 liquid PCE (0.031 solids) per binder for rheology and PE dispersion; the
  high dose delayed hydration so that demoulding was possible only at 11 d ([[hieu2023-aas-extremely-ductile-22pct]], §2.1,
  §2.2.2). Mini-slump flow is shown (Fig. 5) but no value is reported. The ED-EGC authors likewise call for optimising SP to
  shorten setting before demoulding ([[huy2023-egc-activator-pretreatment]], Conclusions). → [[alkali-activated-binder]]
- **Mixing energy** (time and speed) changed ε 2.3× at fixed proportions, with no fresh-state measurement to explain it
  ([[hieu2023-aas-extremely-ductile-22pct]], Fig. 3, Table 4). → [[fiber-dispersion]]

> Synthesis: no round-4 source links a measured rheological parameter to fiber dispersion or ε_tu. The fresh-state data
> are process-specific (spraying, printing) and use different tests, so they cannot be compared directly.

## Related
- [[fiber-dispersion]] · [[mix-designs]] · [[viscosity-modifying-admixtures]] · [[3d-printed-hdc]] · [[alkali-activated-binder]]
