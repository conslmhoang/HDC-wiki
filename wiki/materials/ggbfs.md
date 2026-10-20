---
type: material
slug: ggbfs
aliases: [GGBFS, slag, ground granulated blast-furnace slag]
tags: [binder, sustainability]
sources: [su2023-rubber-modified-hshdc, zhang2022-hshdcc-review, ma2021-ecc-durability-review, shumuye2022-slag-fa-pe-ecc, chavesfigueiredo2020-printed-shcc, sui2018-uhp-ecc-flexural-fatigue, choi2016-pe-alkali-activated-slag-composite]
updated: 2026-10-21
---

# GGBFS (Ground Granulated Blast-Furnace Slag)

## Key points
- GDUT R-HSHDC uses ultra-fine GGBFS at 648 kg/m³, with cement at 887 kg/m³ and SF at 133 kg/m³.
  This lets the mix reach HSHDC-level strength without heat curing
  ([[su2023-rubber-modified-hshdc]], Table 2). → [[heat-curing]]

## Sustainability and durability
- Mixes with high GGBS (GGBS/C 1.07) and 1.5% PE had the lowest CO₂ emissions and cost among the
  compiled HSHDCC ([[zhang2022-hshdcc-review]], p. 15).
- Slag-ECC loses less mass and UPV than FA-ECC under freeze–thaw (Özbay 2013, as cited in
  [[ma2021-ecc-durability-review]], p. 4). → [[durability]]


## Primary slag data (2026-10-20, round 4 ingest)
- **Slag replacing FA in PE-ECC** (W/B 0.30, 40% cement, 60% FA + slag) ([[shumuye2022-slag-fa-pe-ecc]]):

  | Slag (% of binder) | 28 d f'c change | 7 d f'c change | First-crack σ (28 d) |
  |---|---|---|---|
  | 0 (SF-0-60) | 40.79 MPa (reference) | — | 2.25 MPa |
  | 5 | +3.5% | +27.0% | — |
  | 10 | +28.5% | +57.0% | 2.51–2.57 MPa (10–15%) |
  | 15 | **+34.9%** (55.05 MPa) | +77.3% | same |

  - σ_tu stayed about 5.2–5.7 MPa (Table 4). More slag gave more and **wider** cracks; SF-15-45 had the worst crack
    control (Sect. 3.4, Fig. 9). EDS Ca/Si fell 4.27 → 2.46 from 0 to 15% slag at 7 d (Sect. 3.5.1).
  - Motivation: shrinking FA supply, stable slag supply (Sect. 1).
  - ⚔️ Text vs data on ductility: see [[fly-ash]] and [[gaps]].
- **Printed SHCC:** a slag + limestone-powder mix (X, W/B 0.40) outperformed an FA + sand mix (Y, W/B 0.50) in every
  test ([[chavesfigueiredo2020-printed-shcc]], Sects. 3.2–3.4). → [[3d-printed-hdc]]
- **UHP-ECC binder:** OPC 700 + GGBS 750 + SF 150 + limestone powder 100 kg/m³ (GGBS above cement) in a 120 MPa PE-ECC
  ([[sui2018-uhp-ecc-flexural-fatigue]], Table 1).

## Alkali-activated (cementless) slag (2026-10-21)
- First cementless GGBS composite in the wiki: GGBS (Blaine 4320 cm²/g, CaO 44.6%) activated by Ca(OH)₂ 8.38% +
  Na₂SO₄ 3.35% of GGBS mass (powders), no cement, no aggregate, 1.75% PE 18 mm × 12 µm
  ([[choi2016-pe-alkali-activated-slag-composite]], §2.1, Tables 1–2).
- Strain hardening: f'c 36.3–54.8 MPa, σ_tu 5.06–13.06 MPa, ε 4.58–7.50% at W/B 0.38–0.26, 28 d (Tables 5, 7).
- Computed average crack width 88.9–109.8 µm (Table 8), wider than typical PVA-ECC; qualitatively consistent with
  "slag widens cracks" ([[shumuye2022-slag-fa-pe-ecc]]). Different binders and fibres, so not a direct comparison.
- As cited there: PVA + alkali-activated slag mortar (Lee et al. 2012) f'c 19.4–30.6 MPa, ε 1.53–4.48%; FA geopolymer +
  PVA (Ohno & Li 2014) 27.6 MPa / 4.3%; EGC (Nematollahi 2015) 63.7 MPa / 4.3% (§1).
  Full page: [[alkali-activated-binder]].

> Synthesis: in the round-4 primary data, slag is a strength lever (+35% f'c at 15%) with a cost in crack width.
> No source measures slag's effect on the PSH indices.

## Related
- [[fly-ash]] · [[silica-fume]] · [[pe-fiber]] · [[mix-designs]] · [[alkali-activated-binder]]
