---
type: material
slug: alkali-activated-binder
aliases: [alkali-activated slag, AAS, cementless binder, geopolymer, alkali-activated SHCC, EGC, engineered geopolymer composite]
tags: [binder, cementless, sustainability, slag]
sources: [choi2016-pe-alkali-activated-slag-composite]
updated: 2026-10-21
---

# Alkali-Activated (Cementless) Binders

## Definition
A binder made without Portland cement, in which an aluminosilicate precursor (here ground granulated blast-furnace
slag, GGBS) is activated by alkaline or sulfate compounds. In the wiki, the only primary example is a GGBS paste
activated by **powdered** Ca(OH)₂ (8.38% of GGBS mass) and Na₂SO₄ (3.35%), with no cement and no aggregate
([[choi2016-pe-alkali-activated-slag-composite]], §2.1, Table 1). Geopolymers (fly-ash based) belong to the same
family but appear here only as cited.

**Terminology:** the authors call their material an "ultra-high-ductile polyethylene fiber-reinforced alkali-activated
slag-based composite" and place it among HPFRCC/ECC-type composites; they do **not** call it HDC, ECC or SHCC. It is in
the wiki scope because it shows tensile strain hardening with multiple cracking (CLAUDE.md §3).
→ [[terminology-hdc-ecc-shcc]]

## Key points
- **Ductility does not need cement or a high-strength matrix**: with 1.75 vol.% PE (18 mm × 12 µm, 2700 MPa, 88 GPa),
  the best mix (M26, W/B 0.26) reached ε **7.50%** and σ_tu **13.06 MPa** at f'c **54.8 MPa** (50 mm cubes, 28 d, JSCE
  dogbone, 80 mm gauge) ([[choi2016-pe-alkali-activated-slag-composite]], Tables 5, 7). → [[pe-fiber]], [[tensile-strain-capacity]]
- **No aggregate**, to keep matrix toughness low and favour multiple cracking (§2.1). → [[matrix-fracture-toughness]]
- **Viscosity control** (HRWRA + VMA tuned per W/B, after Li & Li 2013) was used to disperse PE; hardened densities were
  within 0.5% of theoretical (§2.1, §3.1). → [[viscosity-modifying-admixtures]], [[fiber-dispersion]]
- **Curing**: 2 d sealed in air, then water at 23 ± 3 °C; tested at 28 d ⚠️ (whether "28 d" counts from casting is
  unclear, see source page). No heat curing. → [[heat-curing]]
- Ratios σ_tu/f'c 23.8% (M26) and 19.8% on average, about double normal concrete; first-crack/f'c ≈ 9.2% (§3.3).

## Quantitative evidence
| Mix (W/B, mass) | f'c (MPa) | First-crack σ (MPa) | σ_tu (MPa) | ε_tu (%) | Avg crack width (µm, computed) | Source |
|---|---|---|---|---|---|---|
| M26 (0.26) | 54.8 | 4.87 | 13.06 | 7.50 | 88.9 | [[choi2016-pe-alkali-activated-slag-composite]] Tables 5, 7, 8 |
| M30 (0.30) | 49.0 | 4.61 | 11.46 | 6.33 | 106.9 | same |
| M34 (0.34) | 42.3 | 3.92 | 7.64 | 5.35 | 109.8 | same |
| M38 (0.38) | 36.3 | 3.37 | 5.06 | 4.58 | 99.3 | same |

- Strain basis (at peak vs ultimate) not stated ⚠️; crack width = gauge elongation / crack count at end of loading.

### Earlier alkali-activated / geopolymer SHCC (as cited in [[choi2016-pe-alkali-activated-slag-composite]], §1)
| Material | Fiber | f'c (MPa) | σ_tu (MPa) | ε (%) | Original study |
|---|---|---|---|---|---|
| Alkali-activated slag mortar | PVA | 19.4–30.6 | 2.83–4.69 | 1.53–4.48 | Lee et al. 2012 |
| FA geopolymer | PVA | 27.6 | 3.4 | 4.3 | Ohno & Li 2014 |
| Engineered geopolymer composite (EGC) | PVA | 63.7 | 4.7 | 4.3 | Nematollahi 2015 |

## Influencing factors / relationships
- **W/B**: raising W/B from 0.26 to 0.38 lowered σ_tu by 61.3% and ε by 38.9%; the lowest W/B gave the most cracks
  (67.3) and the narrowest cracks (Tables 7–8, §3.3). ⚔️ Same direction as [[sun2019-modified-pva-fiber-ecc]], opposite to
  [[zhao2022-ecc-tension-damage-model]] and [[chai2023-hdc-ambient-temperature]]. → [[water-binder-ratio]], [[gaps]]
- **Fiber type**: PE (hydrophobic, no chemical bond) replaced PVA because PVA-AAS stayed at ≤ 4.5% (as cited, §1).
- **Slag**: in cement-based PE-ECC, slag raises strength but widens cracks ([[shumuye2022-slag-fa-pe-ecc]]); the AAS
  composite's ≈ 100 µm average width is consistent with that, qualitatively. → [[ggbfs]]

> Synthesis: this cementless composite sits with Tongji [[uhdc]] (PE, moderate-strength matrix, very high ε) rather than
> with Michigan [[hshdc]] (166 MPa, 3.4–4.2%). Together they show that a high ε and a high σ_tu can be reached in a
> ≈ 40–55 MPa matrix with fine PE fibres. It is the only alkali-activated SHCC with primary data in the wiki; no durability,
> shrinkage or structural data exist for it.

## Conflicts & open questions
- ⚔️ W/B direction (see above and [[water-binder-ratio]]).
- Open (stated, §3.3): mechanical, physical, chemical and rheological properties must be studied before use as a
  construction material. Literature with fibres other than PVA is limited (§1).
- Open: durability (carbonation of AAS, shrinkage, self-healing) of alkali-activated SHCC — none in the corpus.
- To verify: Conclusion 1 σ_tu range "5.06–7.5 MPa" vs Table 7 (5.06–13.06); whether activator powders count in the binder for W/B.

## Related
- [[ggbfs]] · [[pe-fiber]] · [[fly-ash]] · [[uhdc]] · [[hshdc]] · [[water-binder-ratio]] · [[terminology-hdc-ecc-shcc]] · [[strain-hardening]] · [[mix-designs]]
