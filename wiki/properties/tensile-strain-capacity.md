---
type: property
slug: tensile-strain-capacity
aliases: [tensile ductility, ε_tu, εp, ε_cu, strain capacity, peak strain]
tags: [tension, ductility, key-property]
sources: [ranade2015-hshdc-tensile-rate-effects, ranade2017-hshdc-impact-resistance, su2023-rubber-modified-hshdc, yang2024-hshdc-uniaxial-tension, ye2021-uhdc-flexural-size-effect, he2024-hdc-research-advances]
updated: 2026-10-06
---

# Tensile Strain Capacity (ε_tu)

## Definition
The tensile strain at **peak** stress in direct uniaxial tension (dogbone). Sources name it
differently: ε_tu, εp, ε_cu. Some sources do not say whether the value is at peak or at failure,
so check this before comparing. → [[dogbone-uniaxial-tension]]

## Quantitative evidence (ranges; full rows in [[mechanical-results]])
| Source | Material | Curing | ε_tu (%) | σ_tu (MPa) | Note |
|---|---|---|---|---|---|
| [[ranade2015-hshdc-tensile-rate-effects]] | Michigan HSHDC, 10⁻⁴ s⁻¹ | 90 °C | **4.2** ⚔️ | 14.5 | 6 dogbones, 90 mm gauge |
| [[ranade2017-hshdc-impact-resistance]] (quoted from earlier work) | Michigan HSHDC | 90 °C | **3.4** ⚔️ | 14.5 | same mix |
| [[su2023-rubber-modified-hshdc]] | GDUT R-HSHDC, PE 12–18 mm | ambient | 2.9–5.7 | 16.1–19.6 | strain basis not stated ⚠️ |
| same | PE 6 mm | ambient | 0.3–0.5 | 8.9–10.4 | brittle |
| [[yang2024-hshdc-uniaxial-tension]] | Xi'an HSHDC, PE22 | 20 °C | 3.56–6.48 | 5.7–7.7 | at peak |
| same | Xi'an HSHDC, PVA39 | 20 °C | 0.23–0.30 | 4.8–5.5 | — |
| [[ye2021-uhdc-flexural-size-effect]] | Tongji UHDC 1% / 2% PE | ambient | 4.31 / **9.45** | about 7 / about 9.5 ⚠️ (Fig. 4b) | 80 mm gauge |
| [[he2024-hdc-research-advances]] p. 20 | "ordinary HDC" | — | 3–5 | 3–7 | uncited ⚠️ |
| [[ranade2017-hshdc-impact-resistance]] | Cor-Tuf FR-UHPC | 90 °C | 0.12 | 11.2 | tension-softening |

## Influencing factors
- **Fiber type:** PE far outperforms PVA in high-strength matrices. → [[pe-fiber]], [[pva-fiber]]
- **Fiber length and diameter:** very short PE (6 mm) is brittle; a finer diameter raises ε about 10×.
  → [[fiber-geometry]]
- **Matrix:** more FA (+68.9%), the optimum W/B (0.16), and rubber (up to +71.6%) all raise ε.
  → [[fly-ash]], [[water-binder-ratio]], [[crumb-rubber]]
- **Strain rate:** ε falls from 4.2% to about 2.9% between 10⁻⁴ and 0.1 s⁻¹, then plateaus. It
  tracks crack width. → [[strain-rate-effects]]
- **Freeze–thaw:** ε_tu drops more than σ_tu (Yun 2013, as cited in [[he2024-hdc-research-advances]],
  p. 13). → [[durability]]

> Synthesis: Across sources, ε_tu falls as matrix strength rises:
> - UHDC (f'c about 37 MPa): up to 9.45%
> - Xi'an HSHDC (about 100 MPa): up to 6.5%
> - GDUT (about 120–157 MPa): up to 5.7%
> - Michigan (166 MPa): 3.4–4.2%
>
> This is a strength–ductility trade-off that the review can show in one chart.
> He et al. argue that 3–5% is not enough for unreinforced structural use
> ([[he2024-hdc-research-advances]], p. 20).

## Conflicts
- ⚔️ Michigan HSHDC quasi-static ε_tu: 3.4% vs 4.2%, same mix and about the same rate. Report the range. → [[gaps]]

## Related
- [[strain-hardening]] · [[crack-width]] · [[tensile-toughness]] · [[mechanical-results]]
