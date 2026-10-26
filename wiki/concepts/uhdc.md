---
type: concept
slug: uhdc
aliases: [UHDC, ultra-high ductile concrete, UHDCC, ultra-high ductility cementitious composites]
tags: [material-family, pe-fiber, tongji]
sources: [ye2021-uhdc-flexural-size-effect, he2024-hdc-research-advances, sui2018-uhp-ecc-flexural-fatigue, choi2016-pe-alkali-activated-slag-composite, hieu2023-aas-extremely-ductile-22pct, huy2023-egc-pe-pva-hybrid-healing]
updated: 2026-10-26
---

# UHDC: Ultra-High Ductile Concrete

## Definition
An ECC with "specially-chosen" PE fibers, developed by the Tongji group (Yu Jiangtao, Yu Kequan).
It has tensile strain capacity "up to 12%", and the name reflects deformability comparable to steel
bars under ISO and Chinese codes ([[ye2021-uhdc-flexural-size-effect]], p. 2).

## Key points
- The matrix is a high-volume fly ash mortar:
  - FA/C = 1.20 (Class F)
  - W/B about 0.25 (computed by the wiki from Table 1)
  - silica sand (max 0.25 mm)
  - f'c about 36–38 MPa
  ([[ye2021-uhdc-flexural-size-effect]], Table 1, p. 7). → [[fly-ash]]
- No heat curing.
- ε_tu = 4.31% (UHDC-1, 1% PE) and **9.45%** (UHDC-2, 2% PE), from JSCE dogbones with an 80 mm
  gauge ([[ye2021-uhdc-flexural-size-effect]], p. 3). → [[tensile-strain-capacity]]
- UHDC-2 shows **no flexural size effect** over beam depths of 40–150 mm. → [[size-effect]]
- Uses reported in the review ([[he2024-hdc-research-advances]]):
  - 3D-printed UHDC, with 1.5% PE best (p. 4–5) → [[3d-printed-hdc]]
  - steel-free UHDCC frames and an unreinforced UHDC pavilion (2021 China Flora Expo) (p. 20)
    → [[unreinforced-hdc-structures]]

> Synthesis: UHDC shows that PE fiber in a **low-strength, high-FA** matrix gives much higher
> ductility (9.45%) than PE in the very-high-strength Michigan matrix (3.4–4.2%). This fits the
> micromechanics view that a lower matrix toughness makes the energy criterion easier to satisfy.
> → [[strain-hardening]]

## Comparable ultra-ductile PE composites (2026-10-20 ingest)
- **UHP-ECC** (Shenzhen / PolyU): PE 2 vol.% in a GGBS + SF + limestone-powder matrix, W/B about 0.14,
  f'c 120.7 MPa (90 d), σ_tu up to 12 MPa and ε > 8% (abstract and Fig. 4 only; test age not stated ⚠️)
  ([[sui2018-uhp-ecc-flexural-fatigue]], Table 1, abstract). It reaches UHDC-level strain in a matrix about
  3× stronger than UHDC (36–38 MPa). → [[hshdc]], [[fatigue]]

> Synthesis: UHP-ECC weakens the earlier synthesis that very high ductility needs a low-strength, high-FA
> matrix. High strain (> 8%) is also reported in a very-high-strength PE matrix, consistent with the "trade-off
> is not fundamental" row in [[gaps]]. Fiber and interface design, not f'c alone, controls ε_tu.

- **Cementless alkali-activated slag + PE** (Chonnam / Michigan): 1.75 vol.% PE 18 mm × 12 µm, no aggregate, W/B 0.26,
  f'c 54.8 MPa, σ_tu 13.06 MPa and ε 7.50% at 28 d (JSCE dogbone) ([[choi2016-pe-alkali-activated-slag-composite]], Tables 5, 7). Not called UHDC
  or ECC by the authors. Like UHDC, it combines a moderate-strength matrix with fine PE, but its σ_tu is far higher.
  → [[alkali-activated-binder]]

> Synthesis (round 5): three PE composites now reach ≥ 7.5% at very different f'c: UHDC (≈ 37 MPa), alkali-activated
> slag (≈ 55 MPa, [[choi2016-pe-alkali-activated-slag-composite]]) and UHP-ECC (≈ 121 MPa). Matrix strength alone does not set the ductility class.

## UHDC is no longer the strain maximum (2026-10-26)
- Tongji UHDCC as cited by [[hieu2023-aas-extremely-ductile-22pct]] (Table 7; Yu et al. 2018): UB f'c 12.9 MPa / ε 13.55% /
  σ_tu 4.97 MPa; UA 45.9 / 11.98 / 6.07. These second-hand values exceed the primary 9.45% of [[ye2021-uhdc-flexural-size-effect]].
- The CNU cementless PE composites now exceed UHDC: ED-AASC 22.34% at peak (f'c 53.6 MPa;
  [[hieu2023-aas-extremely-ductile-22pct]], Table 4) and fly-ash ED-EGC 18.62% (f'c 20.7 MPa; [[huy2023-egc-activator-pretreatment]],
  Table 4). Both authors compare ε with minimum steel-bar elongation (ASTM A615 9%, A706 14%, ISO 6935-2 14/17%), the same
  "steel-like deformability" argument as the UHDC name, but with a different gauge and definition (strain at peak over 80 mm
  vs elongation at fracture) ([[hieu2023-aas-extremely-ductile-22pct]], Fig. 15; [[huy2023-egc-activator-pretreatment]], Fig. 11).
- Cited as a benchmark for a cementless high-strength EGC: Yu 2018 UHP-ECC f'c × ε = 10.0 MPa vs 8.8 MPa for HSUD-EGC S-PE
  ([[huy2023-egc-pe-pva-hybrid-healing]], Fig. 6). → [[hshdc]]

> Synthesis: "ultra-high ductility" (> 6%, as cited in [[huy2023-egc-pe-pva-hybrid-healing]] §1) is now reached by several
> PE composite families; the top values (18.6–22.3%) are in cementless matrices with wide cracks (≈ 200 µm).

## Related
- [[terminology-hdc-ecc-shcc]] · [[hshdc]] · [[alkali-activated-binder]] · [[pe-fiber]] · [[size-effect]]
