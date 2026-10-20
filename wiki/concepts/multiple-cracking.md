---
type: concept
slug: multiple-cracking
aliases: [multiple microcracking, saturated cracking, crack number, crack density]
tags: [mechanism]
sources: [ranade2015-hshdc-tensile-rate-effects, ranade2017-hshdc-impact-resistance, su2023-rubber-modified-hshdc, yang2024-hshdc-uniaxial-tension, ye2021-uhdc-flexural-size-effect, li1992-steady-state-multiple-cracking, li2002-pva-ecc-interface-tailoring, zhang2022-hshdcc-review, kanda2006-psh-design-criteria, yang2008-ecc-fiber-bridging-law]
updated: 2026-10-20
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

## Mechanism and crack saturation (2026-10-16 ingest)
- **Mechanism** ([[li1992-steady-state-multiple-cracking]], p. 2255):
  - After the first crack, the fibers must carry the total load.
  - If they can, they transfer load back to the matrix by shear, and a new crack forms.
  - This repeats into periodic sub-parallel cracks until σ0 is reached.
  - Multiple cracking also needs a flaw size c̃ > c̃_mc. → [[steady-state-cracking]]
- **PVA-ECC crack spacing** with oil 0 / 0.3 / 0.5 / 0.8 / 1.2%: 27 / 7.5 / 3.5 / 2.5 / 2.8 mm
  ([[li2002-pva-ecc-interface-tailoring]], Table 4).
  - From 0.3% to 0.5% oil, ductility comes from **more** cracks.
  - Above that, it comes from **wider** cracks. Saturation is reached at about 0.8% oil.
  - Saturated specimens have more than 60 cracks in 150 mm (p. 467–471).
- In HSHDCC, adding SF from 0 to 40% raised the crack count and lowered crack width
  (Lei 2019, as cited in [[zhang2022-hshdcc-review]], p. 12).

## Saturation (2026-10-20 ingest)
- **Saturation index** = x_d^test / x_d, where x_d is the Wu & Li 1995 saturated spacing and x_d^test is
  inferred as δ_peak/ε_cu. A ratio > 2 means saturated cracking is "rarely expected" ([[kanda2006-psh-design-criteria]], Eqs. 15–16, p. 69).
- M45 PVA-ECC: average crack spacing about 1 mm, crack width constant at about 60 µm after 1% strain ([[yang2008-ecc-fiber-bridging-law]], p. 181, 188).

## Related
- [[strain-hardening]] · [[crack-width]] · [[fiber-bridging]] · [[digital-image-correlation]]
