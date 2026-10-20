---
type: material
slug: pva-fiber
aliases: [polyvinyl alcohol fiber, PVA]
tags: [fiber, synthetic, hydrophilic]
sources: [li2002-pva-ecc-interface-tailoring, yang2024-hshdc-uniaxial-tension, he2024-hdc-research-advances, ranade2015-hshdc-tensile-rate-effects, yu2018-ecc-direct-tensile-review, zhang2022-hshdcc-review, ma2021-ecc-durability-review, yang2008-ecc-fiber-bridging-law, li2021-hdc-sulfate-dry-wet, chai2023-hdc-ambient-temperature, li2003-ecc-review, kanda2006-psh-design-criteria, chai2019-hdcc-freeze-thaw-carbonation-flexure, deng2015-hdc-compressive-toughness, deng2018-hdc-compressive-constitutive, deng2018-hdc-short-columns, gao2020-hdcc-recycled-fine-aggregate, herbert2013-ecc-self-healing-natural-environment, jin2019-hvfa-shcc-structural, kanda2003-sprayed-ecc, kanakubo2006-dfrcc-tensile-test-method, mechtcherine2011-shcc-high-strain-rate, mohammed2020-cr-ecc-elevated-temperature, ozbay2013-ecc-self-healing-sustained-load, paul2014-r-shcc-chloride-corrosion, qian2007-shcc-inverse-tensile-strain, sun2019-modified-pva-fiber-ecc, vanzijl2010-shcc-durability, wang2019-rc-beam-ecc-shear-strengthening, wang2023-ecc-frost-damage, zhao2022-ecc-tension-damage-model, zhong2019-ecc-freeze-thaw, zhou2023-hsecc-elevated-temperature, chavesfigueiredo2020-printed-shcc, bu2022-ecc-chloride-crack-width]
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
  - **Update (round 4):** primary TG data show that PVA **starts to melt at 230 °C**, with thermal instability at
    220–420 °C ([[zhou2023-hsecc-elevated-temperature]], Fig. 4). [[mohammed2020-cr-ecc-elevated-temperature]] also
    states 230 °C (as cited, §3.3), and [[vanzijl2010-shcc-durability]] gives decomposition at 263 °C (p. 266).
    The 230 °C onset is now confirmed; "273 °C" has no primary support. Melting onset and decomposition are
    different quantities, so this is not a conflict.
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


## Further PVA data (2026-10-20, round 4 ingest)

### Fiber properties reported
| Source | Product | d (µm) | L (mm) | σ_f (MPa) | E (GPa) | Elong. (%) | Note |
|---|---|---|---|---|---|---|---|
| [[deng2015-hdc-compressive-toughness]] Table 1; [[deng2018-hdc-compressive-constitutive]] Table 1 | n.r. (XAUAT) | 39 | 12 | 1600 | 40 | 7 | ρ 1.3 g/cm³ |
| [[chai2019-hdcc-freeze-thaw-carbonation-flexure]] Table 1 | domestic "normal" PVA | 39 | 12 | ≥ 1250 | 30 | 5–8 | chosen with river sand to cut cost to ⅓ of Kuraray K-II + quartz sand (p. 127) |
| [[gao2020-hdcc-recycled-fine-aggregate]] Table 2 | domestic, n.r. | 40 | 12 | ≥ 1250 | > 30 | ≥ 6 | density printed "1.3 g/m³" (typo) |
| [[sun2019-modified-pva-fiber-ecc]] Table 3 | Sinopec SVW (domestic) | 31 | 12 | 1400 | 35 | 6.5 | AR 387 |
| same | Kuraray REC-15 | 40 | 12 | 1560 | 42 | 7.0 | AR 300 |
| [[jin2019-hvfa-shcc-structural]] Table 4 | Kuraray REC-15 | 39 | 12 | 1620 | 42.8 (printed "MPa" ⚠️) | 7 | 1.3 g/cm³ |
| [[kanda2003-sprayed-ecc]] Tables 1–2 | Kuraray REC | 39 | 12 | 1620 (1070 apparent in matrix) | 43 | 6 | SG 1.3 |
| [[mechtcherine2011-shcc-high-strain-rate]] Table 3 | Kuraray K-II REC15 | 40 nominal (38.0 measured) | 12 | 1456 → 1674 (8.3·10⁻⁴ → 1.5 s⁻¹) | — | failure strain 27.4–27.5 ⚠️ | failure strain rate-independent |
| [[mohammed2020-cr-ecc-elevated-temperature]] Table 2 | Kuraray REC(S)15, 1.2% oil | 40 | 12 | 1600 | 41 | — | SG 1.3 |
| [[herbert2013-ecc-self-healing-natural-environment]] §2.1 | Kuraray-type, 1.2% oil | 39 | 12 | 1600 | 42.8 | — | |
| [[ozbay2013-ecc-self-healing-sustained-load]] p. 169 | 1.2% oil | 39 | **8** ⚠️ | 1620 | 42.8 | — | 8 mm is unusual |
| [[wang2023-ecc-frost-damage]] Table 3 | Kuraray | 39 | 8 | 1600 | 42 | — | |
| [[zhong2019-ecc-freeze-thaw]] Table 2 | Kuraray | 39 | 13 | 1600 | 42 | — | |
| [[zhao2022-ecc-tension-damage-model]] Table 2 | Kuraray | 40 | 12 | 1560 | 41 | 6.5 | 1.3 g/cm³ |
| [[zhou2023-hsecc-elevated-temperature]] Table 2 | Kuraray | 15 ⚠️ (printed 0.015 mm) | 12 | 1780 | 39 | 7.0 | 1300 kg/m³ |
| [[kanakubo2006-dfrcc-tensile-test-method]] Table 4 | n.r. (JCI round robin) | 40 | 12 | 1600 | 40 | — | 1.9 vol.% |
| [[bu2022-ecc-chloride-crack-width]] Table 1 | Kuraray | 40 | 12 | 1560 | 41 | — | 26 kg/m³ ≈ 2.0 vol.% (converted with ρ 1.3 g/cm³) |

- Nominal Kuraray REC-15 strength is printed as 1560, 1600 or 1620 MPa and E as 39–43 GPa in different papers.
  These are product-sheet variants, not test results.

### Tensile performance of PVA composites (strain at peak stress unless noted)
| Source | Term | Matrix | Vf (%) | ε at peak (%) | σ_tu (MPa) | Age |
|---|---|---|---|---|---|---|
| [[jin2019-hvfa-shcc-structural]] Table 5 | PVA-SHCC | FA/C 2.4 / 3.2 / 4.4, W/B 0.25 | 2 | 1.92 / **3.42** / 3.07 | 3.97–4.10 | 28 d |
| [[qian2007-shcc-inverse-tensile-strain]] Table 6 | PVA-ECC (SHCC) | FA/C 1.2 / 2.0 / 2.8 | n.r. | 2.1 / 3.5 / 3.7 (COV 52 / 9 / 11%) | 5.3 (FA/C 1.2) / 4.9 (2.8) | 28 d |
| [[gao2020-hdcc-recycled-fine-aggregate]] Table 6 | R-HDCC / N-HDCC | W/B 0.45, FA 30% | 0.5–2.0 | 1.32–4.76 (R) / 0.41–1.68 (N) | 1.51–2.84 / 1.12–2.75 | 28 d |
| [[zhao2022-ecc-tension-damage-model]] Table 3 | ECC | FA/C 2.0, W/B 0.24–0.28 | 1–2 | 0.50–2.00 | 2.96–4.57 | ≥ 35 d ⚠️ |
| [[sun2019-modified-pva-fiber-ecc]] Tables 10–11 | ECC | W/B 0.35 | 2 | REC-15 3.21 (7 d) → 1.39 (28 d); domestic 0.46 (7 d) | about 3.3–3.5 | 7 / 28 d |
| [[deng2018-hdc-short-columns]] Fig. 1 | HDC (XAUAT) | FA 50%, W/B 0.29 | 2 | ≈ 1.0 | — | n.r. |
| [[kanakubo2006-dfrcc-tensile-test-method]] Tables 6–9 | DFRCC | W/B 0.46 | 1.9 | 2.70 (thin plate) → 0.07 (Ø70 dogbone) | 5.00 → 3.38 | n.r. |
| [[mechtcherine2011-shcc-high-strain-rate]] Table 2 | SHCC | FA/C 1.21, SAP | 2.2 | 1.49 (10⁻⁵ s⁻¹) | — | n.r. |
| [[paul2014-r-shcc-chloride-corrosion]] Tables 1–2 | SHCC | FA/C 1.72, w/c 1.0 | n.r. | 1.5–2.9 | — | n.r. |
| [[chavesfigueiredo2020-printed-shcc]] Table 5 | printed SHCC | slag + LP, or FA | n.r. | 0.15–0.31 | 1.64–2.41 | 35 d |

- **No tensile strain hardening shown** (do not use as HDC tension evidence): [[zhou2023-hsecc-elevated-temperature]]
  ("HSECC", flexural softening), [[mohammed2020-cr-ecc-elevated-temperature]] (compression only),
  [[zhong2019-ecc-freeze-thaw]] (flexure only), [[deng2015-hdc-compressive-toughness]] and
  [[deng2018-hdc-compressive-constitutive]] (compression only), [[wang2019-rc-beam-ecc-shear-strengthening]]
  (1.5% PVA-ECC, σ_tu 4.84 MPa, strain hardening stated but strain not quantified, Sect. 2).

### Surface modification and bond
- **VAE emulsion coating** on REC-15 (10 min ultrasonic soak) raised 7-d ε 3.21 → 4.05% (+26.2%) at unchanged σ.
  The weakly acidic film (pH 4.0–6.5) retards hydration near the fiber and weakens the ITZ, so fibers pull out
  ([[sun2019-modified-pva-fiber-ecc]], Table 11, §3.2). Treated domestic PVA rose 0.46 → 0.97% (Table 10).
  Boric-anhydride coatings over-weakened the bond (ε 2.02% with softening). → [[fiber-surface-treatment]]
- **Rate:** PVA pull-out peak force about ×2 from 10⁻⁵ to 10 s⁻¹, with matrix residue on high-rate fibers
  ([[mechtcherine2011-shcc-high-strain-rate]], Figs. 13–15). → [[strain-rate-effects]]
- In-cement PVA bond (after Kiyota 2002, as cited): frictional τi 2.63–3.31 MPa, chemical τs 4.55–21.6 MPa, f 0.5
  ([[kanda2003-sprayed-ecc]], Table 2). → [[fiber-matrix-interface]]
- High sand content (S/B 0.48) raises friction, so PVA ruptures and compressive deformability falls
  ([[deng2018-hdc-compressive-constitutive]], p. 5).
- Recycled fine aggregate appears to raise PVA bond (SEM: pulled-out fibers stripped of surface filaments)
  ([[gao2020-hdcc-recycled-fine-aggregate]], Fig. 16). → [[recycled-fine-aggregate]]

### Durability of the fiber
- PVA keeps nearly full strength after 14 d in 80 °C alkaline water; ≤ 5% loss after > 1 yr in dilute acids
  ([[vanzijl2010-shcc-durability]], p. 266).
- Freeze–thaw scratches PVA surfaces and is said to lower bond (Chai & Xu 2018, as cited in
  [[chai2019-hdcc-freeze-thaw-carbonation-flexure]], p. 132–133; inferred, not measured, in [[wang2023-ecc-frost-damage]], §3.2).
  → [[freeze-thaw]]
- PVA content explains 39.02% (IF) and 48.60% (PF) of the variance of frost-failure indices; 2.0 vol.% (13 mm) did
  slightly worse than 1.5% because of dispersion ([[zhong2019-ecc-freeze-thaw]], Tables 6–7, §3.5).
- High temperature: PVA turns black from 200 to 400 °C and is gone by 600 °C; melt channels up to 21.5 µm at 400 °C
  ([[zhou2023-hsecc-elevated-temperature]], Figs. 3, 11). PVA + steel hybrids: see [[hybrid-fiber]].

> Synthesis: the round-4 data widen the gap between Michigan oiled-PVA ECC (> 3%) and most Chinese PVA-HDC/HDCC/ECC
> (about 0.5–2% at peak: [[zhao2022-ecc-tension-damage-model]], [[deng2018-hdc-short-columns]], the N-series of
> [[gao2020-hdcc-recycled-fine-aggregate]]). Two levers close the gap in primary data: a high FA/C (≥ 2)
> ([[jin2019-hvfa-shcc-structural]], [[qian2007-shcc-inverse-tensile-strain]]) and a bond-weakening coating
> ([[sun2019-modified-pva-fiber-ecc]]). Fiber product and test geometry ([[kanakubo2006-dfrcc-tensile-test-method]])
> confound cross-paper comparison.

- ⚔️ Age effect: REC-15 ECC fell from 3.21 to 1.39% between 7 and 28 d ([[sun2019-modified-pva-fiber-ecc]], Table 11), far
  below Michigan PVA-ECC at 28 d (about 4–5%). The matrix and curing differ, so this is not a direct conflict. → [[gaps]]

## Related
- [[pe-fiber]] · [[hybrid-fiber]] · [[fiber-matrix-interface]] · [[fiber-surface-treatment]] · [[terminology-hdc-ecc-shcc]] · [[recycled-fine-aggregate]] · [[freeze-thaw]]
