---
type: property
slug: permeability
aliases: [water permeability, transport properties, chloride diffusion, capillary absorption, sorptivity]
tags: [durability, transport]
sources: [ma2021-ecc-durability-review, homma2009-frcc-self-healing, vanzijl2010-shcc-durability, wang2023-ecc-frost-damage, zhang2022-ecc-carbonation-sustained-load, bu2022-ecc-chloride-crack-width, paul2014-r-shcc-chloride-corrosion, kanda2003-sprayed-ecc, chai2019-hdcc-freeze-thaw-carbonation-flexure]
updated: 2026-10-20
---

# Permeability and Transport in Cracked ECC

Part of the [[durability]] hub. Chloride-specific data: [[chloride-and-corrosion]]. CO₂: [[carbonation]].

## Quantitative evidence
### Water permeability vs pre-strain
Lepech & Li 2009, as cited in [[ma2021-ecc-durability-review]] (Table 2, p. 5):

| Pre-strain | Avg crack width | No. of cracks | k (m/s) |
|---|---|---|---|
| 0 (uncracked) | — | — | 8.18 × 10⁻¹² |
| 1.5% | 50 ± 10 µm | 47 | 1.95 × 10⁻¹⁰ |
| 2% | 52 µm | 59 | 3 × 10⁻¹⁰ |
| 3% | 63 µm | 87 | 7.74 × 10⁻¹⁰ |

- Per crack, permeability stays about 10⁻¹² m/s, so the pre-strain level has little effect.
- Reinforced mortar goes from 10⁻¹¹ to 10⁻⁵ m/s as cracks widen from 0 to 500 µm (p. 5).
- Cracks < 100 µm have little effect on permeability (Wang 1997, as cited, p. 3); water-permeability threshold
  0.10–0.15 mm (Lepech & Li 2009, as cited in [[paul2014-r-shcc-chloride-corrosion]], p. 341).

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
  immersion ([[bu2022-ecc-chloride-crack-width]], Eqs. 10–12, Sect. 3). → [[chloride-and-corrosion]]

### Pore structure
- Carbonation reduced 0.1–10 µm porosity more than 2× (zone-I porosity 8.70% carbonated vs 11.57%);
  sustained load on uncracked ECC adds only a small > 10 µm fraction (1.28 → 1.51%), limited by fibres
  ([[zhang2022-ecc-carbonation-sustained-load]], §3.4). → [[carbonation]]
- Coupled F-T + carbonation: pores < 20 nm vanish, 50–200 nm and > 200 nm pores grow
  ([[chai2019-hdcc-freeze-thaw-carbonation-flexure]], Fig. 5).

> Synthesis: keeping many fine cracks rather than a few wide ones is what keeps cracked ECC
> nearly as watertight as uncracked concrete under **pressure-driven flow** and **diffusion**. Capillary
> suction is different: sub-100 µm cracks fill within minutes, so in wet–dry exposure fine cracks are
> still fast paths unless the surface is hydrophobised. → [[multiple-cracking]], [[crack-width]]

## Conflicts & open questions
- Transport-mode-dependent crack-width thresholds: see ⚔️ in [[chloride-and-corrosion]] and [[gaps]].
- Open: permeability of cracked PE-HSHDC/UHDC; permeability under sustained load (cracks ≈2× wider,
  [[ozbay2013-ecc-self-healing-sustained-load]]).

## Related
- [[durability]] · [[self-healing]] · [[crack-width]] · [[chloride-and-corrosion]] · [[carbonation]] · [[freeze-thaw]]
