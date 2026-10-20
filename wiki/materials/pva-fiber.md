---
type: material
slug: pva-fiber
aliases: [polyvinyl alcohol fiber, PVA]
tags: [fiber, synthetic, hydrophilic]
sources: [li2002-pva-ecc-interface-tailoring, yang2024-hshdc-uniaxial-tension, he2024-hdc-research-advances, ranade2015-hshdc-tensile-rate-effects, yu2018-ecc-direct-tensile-review, zhang2022-hshdcc-review, ma2021-ecc-durability-review, yang2008-ecc-fiber-bridging-law, li2021-hdc-sulfate-dry-wet, chai2023-hdc-ambient-temperature, li2003-ecc-review, kanda2006-psh-design-criteria]
updated: 2026-10-20
---

# PVA Fiber

## Definition
Polyvinyl alcohol fiber. It is hydrophilic: its hydroxyl groups form a strong chemical bond plus
friction with the matrix. Untreated PVA tends to rupture rather than pull out
([[li2002-pva-ecc-interface-tailoring]], p. 463–464). The chemical bond is highly rate-sensitive
([[ranade2015-hshdc-tensile-rate-effects]], p. 94–95).

## Quantitative evidence
| Source | d (µm) | L (mm) | σ_f (MPa) | E (GPa) | Elong. (%) | ρ (g/cm³) |
|---|---|---|---|---|---|---|
| [[li2002-pva-ecc-interface-tailoring]] Table 1 (Kuraray) | 39 | 12 | 1620 nominal (1092 apparent, embedded) | 42.8 | 6.0 | — |
| [[yu2018-ecc-direct-tensile-review]] Table 2 | 39 | 12 | 1620 | 42.8 | 6–8 | — |
| [[yang2024-hshdc-uniaxial-tension]] Table 3 | 39 | 12 | 1600 | 40 | 7 | 1.30 |
| [[he2024-hdc-research-advances]] Table 1 (generic) | 12–39 | 3–15 | 1600–2500 | 40–80 | — | 1.32 |

**PVA in a normal-strength matrix vs a high-strength matrix:**

| Matrix | Treatment | ε_tu | σ_tu | Crack width | Source |
|---|---|---|---|---|---|
| w/c 0.45, no SCM (≈14 d) | oil 0% | 0.99% | 4.89 MPa | 43 µm | [[li2002-pva-ecc-interface-tailoring]] Table 4 |
| same | **oil 1.2%** | **4.88%** | 4.41 MPa | 88 µm | same |
| Xi'an W/B 0.16, 15–25% FA (28 d) | n.s. | 0.23–0.30% | 4.78–5.54 MPa | — | [[yang2024-hshdc-uniaxial-tension]] Table 6 |

## Key points
- **Oil coating is what makes PVA-ECC work.** It weakens Gd and τ0 so the fibers pull out instead of
  rupturing. → [[fiber-surface-treatment]]
- Typical PVA-ECC reaches σ_tu 3–8 MPa and ε up to 5% (Li 2003, as cited in
  [[yu2018-ecc-direct-tensile-review]], p. 347), or 3–5% ([[ma2021-ecc-durability-review]], p. 1).
- In **high-strength matrices PVA fails**: it bonds too strongly and ruptures
  ([[yang2024-hshdc-uniaxial-tension]], p. 8; [[zhang2022-hshdcc-review]], p. 4). → [[hshdc]]
- **Ageing:** ε peaks early, then falls to about 3% at 180 d (Lepech & Li 2006, as cited in
  [[yu2018-ecc-direct-tensile-review]], p. 352). The durability of the oil coating is unknown.
- **High temperature:** strain hardening is lost at about 150 °C in situ (Mechtcherine 2012); PVA-ECC is
  brittle at 300 °C (Bhat 2014). The melting point is given as 273 °C (uncited) or "255~230 °C"
  ⚠️. → [[high-temperature-behaviour]]
- Uses reported in the review: 2% PVA in a URM overlay (Deng 2019); an optimum of 1.5 vol.%
  (Said 2020) ([[he2024-hdc-research-advances]], p. 2, 9). → [[masonry-wall-retrofit]]

## Conflicts & open questions
- ⚔️ PVA-ECC ε rate sensitivity: a decrease (Yang & Li 2014; Mechtcherine) vs no significant change
  (Boshoff & van Zijl 2007), as cited in [[yu2018-ecc-direct-tensile-review]], p. 349. → [[gaps]]
- Chinese PVA-HDC primary data now exist from two groups outside Deng's: [[chai2023-hdc-ambient-temperature]] (tension,
  compression, flexure) and [[li2021-hdc-sulfate-dry-wet]] (compression only). The Deng (XAUAT) PVA-HDC papers are still missing.

## Further PVA data (2026-10-20 ingest)
| Source | Product | d (µm) | L (mm) | σ_f (MPa) | E (GPa) | Note |
|---|---|---|---|---|---|---|
| [[yang2008-ecc-fiber-bridging-law]] Table 2 | Kuraray REC-15, 1.2% oil | 39 | 12 | 1600 nominal, 1060 in situ | 22 (in situ) | M45 PVA-ECC |
| [[li2021-hdc-sulfate-dry-wet]] Table 1 | Kuraray K-II | 39 | 12 | 1620 | 42.8 | XUT PVA-HDC |
| [[chai2023-hdc-ambient-temperature]] §2.1 | domestic (oiling n.r.) | 39 | 12 | 1250 | 30 | C40 PVA-HDC |

- **Chinese PVA-HDC tension** (C40, FA/C 0.88, about 2 vol.% assumed): ε_tu 1.15% and σ_tu 4.23 MPa at 20 °C;
  1.15–1.46% across −30 to 60 °C ([[chai2023-hdc-ambient-temperature]], Tables 4, 6). This sits between oiled Michigan PVA-ECC (4.88%)
  and Xi'an PVA-HSHDC (0.23–0.30%).
- **Oiled PVA interface in the M45 FA matrix**: τ0 1.31 MPa, Gd 1.08 J/m², β 0.58 at 2% fiber ([[yang2008-ecc-fiber-bridging-law]], Table 3).
- Optimal τ0 for PVA at 2% is about 1–2 MPa; coating of 0.8–1.2% lowers the critical Vf to about 2%
  ([[li2003-ecc-review]], p. 219, Fig. 7). ⚠️ Fig. 7a caption says 0.6–1.2%.
- PVA is a fiber-**rupture** type composite, so the 2006 PSH thresholds (1.3 / 2.7) apply ([[kanda2006-psh-design-criteria]]).
- ⚔️ [[yu2018-ecc-direct-tensile-review]] attributes "PVA-ECC σ_tu 3–8 MPa" to Li 2003, but [[li2003-ecc-review]] gives
  only ε ≈ 5% and no stress range. Probably a different Li 2003 paper.

## Related
- [[pe-fiber]] · [[fiber-matrix-interface]] · [[fiber-surface-treatment]] · [[terminology-hdc-ecc-shcc]]
