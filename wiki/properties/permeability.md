---
type: property
slug: permeability
aliases: [water permeability, transport properties, chloride diffusion, capillary absorption, sorptivity]
tags: [durability, transport]
sources: [ma2021-ecc-durability-review, homma2009-frcc-self-healing, vanzijl2010-shcc-durability, wang2023-ecc-frost-damage, zhang2022-ecc-carbonation-sustained-load, bu2022-ecc-chloride-crack-width, paul2014-r-shcc-chloride-corrosion, kanda2003-sprayed-ecc, chai2019-hdcc-freeze-thaw-carbonation-flexure, lepech2009-ecc-water-permeability, yang2009-ecc-self-healing-wet-dry]
updated: 2026-10-21
---

# Permeability and Transport in Cracked ECC

Part of the [[durability]] hub. Chloride-specific data: [[chloride-and-corrosion]]. CO₂: [[carbonation]].

## Quantitative evidence
### Water permeability vs pre-strain (primary since 2026-10-21)
[[lepech2009-ecc-water-permeability]] (ECC M45, PVA 39 µm × 12 mm at 26 kg/m³ (vol.% not given), FA/C 1.20, W/B 0.25 computed; pre-strained in
tension at 14 d, constant-head permeation; Table 5). Values were first quoted second-hand via
[[ma2021-ecc-durability-review]] (Table 2, p. 5) and are **confirmed** by the primary paper:

| Pre-strain | Crack width (unloaded) | No. of cracks | k (m/s) | k per crack (m/s) |
|---|---|---|---|---|
| 0 (uncracked) | — | — | 8.18 × 10⁻¹² | — |
| 1.5% | 50 ± 10 µm | 47 | 1.95 × 10⁻¹⁰ | 4.15 × 10⁻¹² |
| 2% | 52 µm | 59 | 3.00 × 10⁻¹⁰ | 5.08 × 10⁻¹² |
| 3% | 63 ± 10 µm | 87 | 7.74 × 10⁻¹⁰ (± 1.9 × 10⁻¹⁰) | 8.90 × 10⁻¹² |

- Correction: the widths were labelled "Avg crack width" on this page (following ma2021); the primary paper
  does not say whether they are averages or maxima (Fig. 5 axis says "maximum") ⚠️ unverified.
- **These are post-healing asymptotes.** Initial k of cracked ECC was ≈ 10⁻⁸–10⁻⁷ m/s, about 2 orders higher,
  and fell over ≈ 20–30 d of flow by self-healing ([[lepech2009-ecc-water-permeability]], Fig. 7 ⚠️ read). → [[self-healing]]
- Per crack, k stays about 10⁻¹² m/s (≈ uncracked), so the pre-strain level has little effect (Table 5, Fig. 6).
  Divide k by crack number to compare with single-crack data (p. 749).
- **Steel-mesh reinforced mortar control** (w/c 0.35, ρ 1.9–2.9%) (Table 5):

  | Crack width | k (m/s) |
  |---|---|
  | uncracked | 4.58 × 10⁻¹¹ |
  | 150 µm | 3.02 × 10⁻⁸ |
  | 240 µm | 7.97 × 10⁻⁶ |
  | 300 µm | 2.58 × 10⁻⁵ |
  | 500 ± 50 µm | **4.46 × 10⁻⁴** |

  ⚔️ Correction: this page earlier said (via [[ma2021-ecc-durability-review]], p. 5) "10⁻¹¹ to 10⁻⁵ m/s from 0 to
  500 µm". The primary value at ≈ 500 µm is 4.46 × 10⁻⁴ m/s; 10⁻⁵ is the 300 µm value. Either ma2021 misreported or
  the wiki misread. → [[gaps]]
- ECC at 1.5% strain is ≈ 5 orders below mortar with 300–350 µm cracks (the ACI / AASHTO service range) (p. 750).
- Permeation needs a constant head, so it matters mainly for deep underwater or water-retaining structures;
  absorption and diffusion were not studied (p. 744).
- **The "100 µm threshold".** Lepech & Li 2009 take 100 µm as a *design target* from Wang et al. 1997 (single
  cracks in concrete: k ≈ sound concrete below 100 µm; 1.0 × 10⁻¹¹ → 1.0 × 10⁻⁴ m/s from 100 to 500 µm, as cited,
  p. 745) and set δ0 < 100 µm in ECC design (p. 746). It was **not measured on ECC**, which was tested only at 50–63 µm.
  Cracks < 100 µm have little effect on permeability (Wang 1997, also as cited in [[ma2021-ecc-durability-review]], p. 3).
- ⚔️ "Water-permeability threshold 0.10–0.15 mm (Lepech & Li 2009, as cited in [[paul2014-r-shcc-chloride-corrosion]],
  p. 341)": the 0.10–0.15 mm range is **not found** in the primary paper, which gives 100 µm (from Wang 1997); its
  reinforced mortar at 150 ± 15 µm already has k = 3.02 × 10⁻⁸ m/s, ≈ 3 orders above uncracked. Treat 0.15 mm as
  a mis-citation. → [[gaps]]
- Single-crack **tension-softening** PVA mortar (0.5 vol.%) after 10 wet–dry cycles: ≈ 10⁻¹⁰ m/s uncracked,
  ≈ 10⁻⁸ at 100 µm, ≈ 10⁻⁶ at 200 µm, ≈ 3 × 10⁻⁶ m/s at 300 µm; < 50 µm cracks return to ≈ uncracked k
  ([[yang2009-ecc-self-healing-wet-dry]], Fig. 5 ⚠️ read). Not ECC.

### Water permeability vs crack width (primary, [[homma2009-frcc-self-healing]], FRCC, not strain-hardening)
- Falling-head plate test: k broadly follows the parallel-plate cube law k ∝ a·w³, but scatters below
  0.1 mm because of multiple cracking (Eq. 6, Fig. 8). Max crack width, not residual elongation, governs k (Fig. 7).
- At w ≈ 81 µm, hybrid FRCC k fell from about 10⁻⁸ to about 10^−11.5 m/s in 28 d of water; steel-cord
  FRCC at 88 µm fell much less (Fig. 11 ⚠️ read). → [[self-healing]]
- Water flow through a crack ∝ COD³ (Tsukamoto 1990, as cited in [[kanda2003-sprayed-ecc]], p. 279).

### Capillary absorption
- Cracks well below 100 µm are water-filled within a few minutes (neutron radiography, Zhang 2010a, as
  cited in [[vanzijl2010-shcc-durability]], p. 264). So "< 100 µm has little effect" refers to **flow
  permeability**, not capillary uptake.
- Silane / integral water repellent practically suppresses capillary absorption of SHCC, including through
  cracks ([[vanzijl2010-shcc-durability]], p. 264).
- Capillary suction through flexural cracks is the dominant fast path for chloride under wet–dry exposure;
  penetration widens along the crack height with time ([[paul2014-r-shcc-chloride-corrosion]], Fig. 16, p. 349).
- After freeze–thaw: initial capillary coefficient A_i of PVA-ECC ×1.14 after 200 cycles (linear with
  cycles); ECC matrix ×1.26 after only 75 cycles ([[wang2023-ecc-frost-damage]], §3.3, Fig. 12). The
  coefficient is time-dependent, fitted W = a(1 − exp(−b√t)) (Eqs. 5–7). → [[freeze-thaw]]

### Chloride diffusion
- Effective diffusion rises *linearly* with pre-load deformation in ECC, but *exponentially* in mortar
  (Sahmaran 2007, as cited in [[ma2021-ecc-durability-review]], Fig. 11, p. 6). Fits reproduced in
  [[vanzijl2010-shcc-durability]], Fig. 5b: ECC (M45) D_eff = 24.87x + 2.04 (×10⁻¹² m²/s, x = deformation in mm);
  mortar ln D = 2.31 + 5.19x³.
- Uncracked PVA-ECC D28 ≈ 35.5 × 10⁻¹² m²/s, decreasing with age; 100 µm notches ≈ uncracked under
  immersion ([[bu2022-ecc-chloride-crack-width]], Eqs. 10–12, pp. 8–9; Sect. 3, p. 4). → [[chloride-and-corrosion]]

### Pore structure
- Carbonation reduced 0.1–10 µm porosity "more than 2×" per the text (zone-I porosity 8.70% carbonated vs 11.57%;
  p. 10), but Fig. 10a shows only ≈ 1.4× in zone I (≈ 2.5 vs ≈ 3.4% for L60-I-C vs L60-I-U, read-off) ⚠️;
  sustained load on uncracked ECC adds only a small > 10 µm fraction (1.28 → 1.51%; the text's "> 100 µm" means > 10 µm
  per the Fig. 10 classes), limited by fibres ([[zhang2022-ecc-carbonation-sustained-load]], §3.4, pp. 10–12). → [[carbonation]]
- Coupled F-T + carbonation: pores < 20 nm vanish, 50–200 nm and > 200 nm pores grow
  ([[chai2019-hdcc-freeze-thaw-carbonation-flexure]], Fig. 5).

> Synthesis: keeping many fine cracks rather than a few wide ones is what keeps cracked ECC
> nearly as watertight as uncracked concrete under **pressure-driven flow** and **diffusion**. Capillary
> suction is different: sub-100 µm cracks fill within minutes, so in wet–dry exposure fine cracks are
> still fast paths unless the surface is hydrophobised. → [[multiple-cracking]], [[crack-width]]

## Conflicts & open questions
- Transport-mode-dependent crack-width thresholds: see ⚔️ in [[chloride-and-corrosion]] and [[gaps]].
- ⚔️ Reinforced-mortar k at 500 µm: 10⁻⁵ (ma2021) vs 4.46 × 10⁻⁴ m/s (primary). ⚔️ 0.10–0.15 mm threshold
  (paul2014) not in the cited paper. Both above.
- Open: is the "100 µm" threshold valid for multiple fine cracks in ECC? No ECC was tested between 63 and 100 µm
  ([[lepech2009-ecc-water-permeability]]). Codes set no permeability or loaded-crack-width limits (p. 745, 749).
- Open: permeability of cracked PE-HSHDC/UHDC; permeability under sustained load (cracks ≈2× wider,
  [[ozbay2013-ecc-self-healing-sustained-load]]).

## Related
- [[durability]] · [[self-healing]] · [[crack-width]] · [[chloride-and-corrosion]] · [[carbonation]] · [[freeze-thaw]]
