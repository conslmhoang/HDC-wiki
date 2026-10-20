---
type: property
slug: tensile-strain-capacity
aliases: [tensile ductility, ε_tu, εp, ε_cu, strain capacity, peak strain]
tags: [tension, ductility, key-property]
sources: [li2002-pva-ecc-interface-tailoring, ranade2015-hshdc-tensile-rate-effects, ranade2017-hshdc-impact-resistance, su2023-rubber-modified-hshdc, yang2024-hshdc-uniaxial-tension, ye2021-uhdc-flexural-size-effect, he2024-hdc-research-advances, yu2018-ecc-direct-tensile-review, zhang2022-hshdcc-review, chai2023-hdc-ambient-temperature, kanda2006-psh-design-criteria, yang2008-ecc-fiber-bridging-law]
updated: 2026-10-20
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
| [[li2002-pva-ecc-interface-tailoring]] | Michigan PVA-ECC, oil 0 → 1.2% | water, about 14 d | 0.99 → **4.88** | 4.89 → 4.41 | coupon, about 185 mm gauge |
| [[yu2018-ecc-direct-tensile-review]] Table 1, p. 347 | ECC (range) / UHP-SHCC / HSHDC / UHDCC | — | 3–12 / 2.8 / 3–4 / 8–13 | 4–20 / — / — / — | review ranges, uncited |
| [[yu2018-ecc-direct-tensile-review]] Fig. 2 | Tongji PE-ECC, Vf·Lf/df 7.5 → 18 | — | 2.20 → 7.91 | 10.29 → 17.86 | 15 cases |
| [[zhang2022-hshdcc-review]] (as cited) | HSHDCC: Huang 2021 / Li Y 2020 / Yu K 2017 | 90 °C / ambient | > 5 / 11 / 8.5 | about 16 / 12.1 / 18.2 | f'c > 210 / 115–131 / 122 MPa |

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
> This looks like a strength–ductility trade-off **within the primary sources**.
>
> ⚔️ **However**, the review [[zhang2022-hshdcc-review]] compiles HSHDCC that break this trend:
> f'c > 210 MPa with ε_tu > 5% (Huang 2021), and 122 MPa with 8.5% (Yu K 2017). The trade-off is
> therefore **not fundamental**. It reflects the matrix, fiber and interface design of each group.
> The better framing for the review is "ductility is governed by interface and fiber tailoring, not
> by f'c alone". → [[fiber-matrix-interface]]
>
> He et al. argue that 3–5% is not enough for unreinforced structural use
> ([[he2024-hdc-research-advances]], p. 20).

## Conflicts
- ⚔️ Michigan HSHDC quasi-static ε_tu: 3.4% vs 4.2%, same mix and about the same rate. Report the range. → [[gaps]]
- ⚔️ The strength–ductility "trade-off" is contradicted by the compiled HSHDCC data in
  [[zhang2022-hshdcc-review]]. → [[gaps]]
- Specimen shape matters: cylinders give lower σ and ε than dogbones (Kesner 2003; Mechtcherine 2011),
  while thickness (13 / 30 / 50 mm) does not (Rokugo 2007), as cited in
  [[yu2018-ecc-direct-tensile-review]], p. 348. → [[dogbone-uniaxial-tension]]

## Further evidence (2026-10-20 ingest)
| Source | Material | Curing / age | ε_tu (%) | σ_tu (MPa) | Note |
|---|---|---|---|---|---|
| [[chai2023-hdc-ambient-temperature]] Tables 4, 6 | Chinese PVA-HDC C40 (FA/C 0.88) | 28 d std + 8 h exposure | 1.15 at 20 °C; 1.15–1.46 over −30 to 60 °C | 3.74–4.80 | dogbone, 100 mm gauge; strain basis n.s. ⚠️ |
| same | screening W/B 0.31 / 0.25 / 0.20 | 28 d | 0.64 / 0.55 / 0.42 | 4.47 / 4.22 / 4.83 | f_cu 47.8 / 50.2 / 59.0 MPa |
| [[kanda2006-psh-design-criteria]] Table 4 | paste + SF, PVA 14 / 40 µm, PE 14 µm | n.s. | 0.26–1.50 (PVA); 5.10 (PE) | 2.43–4.62 | coupon, 205 mm gauge; ultimate strain |
| [[yang2008-ecc-fiber-bridging-law]] Fig. 1 | M45 PVA-ECC 2% | n.s. | ≈4–4.5 ⚠️ (read) | about 5 | reference mix |

- **Chinese PVA-HDC reaches only about 1.2–1.5%**, far below ECC's > 3% but above the 0.5% HDC
  standard ([[chai2023-hdc-ambient-temperature]]). Lower W/B raises strength and lowers ε_tu in the same mixes (Table 4). → [[water-binder-ratio]]

## Related
- [[strain-hardening]] · [[crack-width]] · [[tensile-toughness]] · [[mechanical-results]]
