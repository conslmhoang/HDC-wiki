---
type: concept
slug: multiple-cracking
aliases: [multiple microcracking, saturated cracking, crack number, crack density]
tags: [mechanism]
sources: [ranade2015-hshdc-tensile-rate-effects, ranade2017-hshdc-impact-resistance, su2023-rubber-modified-hshdc, yang2024-hshdc-uniaxial-tension, ye2021-uhdc-flexural-size-effect]
updated: 2026-10-06
---

# Multiple Cracking

## Definition
The formation of many fine, closely spaced cracks instead of one localized crack. It is the
physical mechanism behind [[strain-hardening]].

## Key points
- **nth-crack condition** (Kanda & Li, as cited): each new crack forms at the next-largest flaw
  while bridging capacity at the existing cracks is not exceeded ([[su2023-rubber-modified-hshdc]], p. 6).
- **Fracture stages in notched beams** ([[ye2021-uhdc-flexural-size-effect]], §3.1):
  - NC: a single brittle crack.
  - UHDC-1 (1% PE): "weak fracture-hardening", ending in one critical crack.
  - UHDC-2 (2% PE): "strong fracture-hardening", with multiple cracks and no localization.
  - All end in fracture-softening.
- **Four-zone fracture model** with a "quasi-plastic zone" ([[yang2024-hshdc-uniaxial-tension]], Fig. 12).
- **Under impact:**
  - HSHDC slabs show fine radial cracks and almost no spalling. Cor-Tuf forms 4 yield-line macro-cracks
    and breaks apart ([[ranade2017-hshdc-impact-resistance]], p. 30–31).
  - FE gives back-face principal strain below 1% everywhere in HSHDC, against localised strain up to
    3% in Cor-Tuf (Fig. 11).
- **Under strain rate:** σ_tu/σ_fc stays about constant, so the crack count stays about the same
  ([[ranade2015-hshdc-tensile-rate-effects]], p. 97). → [[strain-rate-effects]]

## Quantitative evidence
| Source | Mix | No. of cracks | Crack density | Note |
|---|---|---|---|---|
| [[su2023-rubber-modified-hshdc]] Table 3 | PE18-PR20 | 31 | 0.45 mm⁻¹ | DIC: a crack is counted above a 9 µm displacement jump |
| same | PE6 group | 1 | — | brittle |
| same | 12 mm group | rises with PR | — | ⚠️ the text range (8–17) conflicts with the table (23) |

Crack number rises with fiber length and rubber content ([[su2023-rubber-modified-hshdc]], Table 3). → [[crack-width]]

## Related
- [[strain-hardening]] · [[crack-width]] · [[fiber-bridging]] · [[digital-image-correlation]]
