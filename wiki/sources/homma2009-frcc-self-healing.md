---
type: source
slug: homma2009-frcc-self-healing
title: "Self-Healing Capability of Fibre Reinforced Cementitious Composites"
authors: [Daisuke Homma, Hirozo Mihashi, Tomoya Nishiwaki]
year: 2009   # JACT Vol. 7, No. 2, June 2009; received 23 Feb 2009, accepted 8 May 2009
venue: "Journal of Advanced Concrete Technology 7(2), 217–228 (Japan Concrete Institute). Affiliations: Tohoku University (Homma, Mihashi); Yamagata University (Nishiwaki)"
doi: "not printed in the PDF; probably 10.3151/jact.7.217 ⚠️ unverified"
raw_file: raw/papers/Homma2009_FRCC-self-healing.pdf
material_term: "FRCC (fibre reinforced cementitious composites): FRCC(PE), FRCC(SC) and HFRCC (hybrid PE + steel cord). SHCC/ECC is mentioned only as related work (p. 217). The authors do NOT call these mixes SHCC/ECC/HDC, and FRCC(PE) is reported as strain-softening (p. 224, Fig. 2, 13)."
study_type: "experimental"
tags: [self-healing, autogenous-healing, frcc, pe-fiber, steel-cord, hybrid-fiber, water-permeability, calcium-carbonate, crack-width, strength-recovery, raman, bse-image]
ingested: 2026-10-20
updated: 2026-10-20
---

# Self-healing of PE, steel-cord and hybrid FRCC (Homma et al., 2009)

## One-paragraph summary
Tohoku University study of autogenous healing in three fibre-reinforced mortars sharing one
silica-fume matrix (W/B 0.45): **FRCC(PE)** with 1.5 vol.% micro-PE (12 µm × 6 mm), **FRCC(SC)** with
0.75 vol.% steel cord (0.4 mm × 32 mm), and **HFRCC** with 0.75% PE + 0.75% SC (Table 2). Plates
25 × 75 × 75 mm were cured 7 d, cracked in direct tension to different elongations (max crack width
17–757 µm, Table 3), then kept 28 d in 20 °C water. Healing was tracked by microscope (thickness of
crystals), water permeability (falling head, at 0/3/14/28 d), re-tension after 28 d, Raman spectroscopy
and BSE image analysis. Healing products were **calcium carbonate** (Raman, Fig. 12). Product thickness
ranked SC < HFRCC < PE, the same order as **fibre count per m³** (187×10⁴, 111×10⁸, 221×10⁸; Table 2;
Fig. 5); the many fine PE fibres act as nucleation sites. Cracks < 100 µm healed in all series
(Fig. 6a); above 100 µm healing was partial, best in FRCC(PE) (slope 0.367 vs 0.104 HFRCC vs 0.029 SC,
Fig. 6b). Permeability fell mostly in the first 3 d; small cracks reached uncracked values by 28 d
(Fig. 10). Strength recovery: SC ≈ 0 or negative (steel-cord corrosion), PE 0–100%, HFRCC > 100%
(Fig. 15). Hydration degree was about 65% in all mixes, so further hydration was not the cause (Fig. 18).
**Note:** these are not strain-hardening composites: FRCC(PE) softens after first crack (p. 224).

## Objective / research question
- Evaluate the self-healing capability of FRCC by microscope, water permeability, tension and BSE
  image analysis (p. 218), and identify how fibre type and number affect healing.

## Materials & mix design
Binder = cement + silica fume. High-early-strength Portland cement (ρ 3.14); silica sand No. 7
(ρ 2.61, "diameter 180 µm"); silica fume (ρ 2.2, 0.15 µm); water-soluble cellulose viscous agent;
polycarboxylate SP (Table 1). PE fibre: L 6 mm, d 12 µm, E 73 GPa, σ_f 2580 MPa, ρ 0.97. Steel cord:
L 32 mm, d 400 µm, E 200 GPa, σ_f 2850 MPa, ρ 7.84 (Table 1).

| Mix ID | Cement | Fly ash | Slag/other | Sand (type, max size) | W/B | SP | Fiber type | L (mm) | d (µm) | Vf (vol.%) |
|---|---|---|---|---|---|---|---|---|---|---|
| FRCC(SC) | 0.85 of binder (by difference) | 0 | SF/B 0.15 | silica sand No. 7, S/B 0.45; "diameter 180 µm" | 0.45 | none ("-") | steel cord | 32 | 400 | 0.75 (187×10⁴ pieces/m³) |
| FRCC(PE) | same | 0 | SF/B 0.15 | same | 0.45 | SP/B 0.09 | PE | 6 | 12 | 1.5 (221×10⁸ pieces/m³) |
| HFRCC | same | 0 | SF/B 0.15 | same | 0.45 | SP/B 0.09 | PE + steel cord | 6 / 32 | 12 / 400 | 0.75 + 0.75 (111×10⁸ pieces/m³) |

Units of binder quantities: ratios to binder (Table 2; mass basis implied, not stated); kg/m³ not
reported. W/B, S/B and SF/B are shared by all three mixes; SP/B 0.09 applies to FRCC(PE) and HFRCC only
(checked on the page image). Fresh: table flow 16.3×16.0 / 13.6×13.8 / 14.7×14.7 cm, air
0.90 / 5.13 / 3.36% for SC / PE / HFRCC (Table 2). Mortar without fibre used as a reference (Fig. 2).

## Test methods
- Specimen geometry: plates 25 × 75 × 75 mm, four per series; loaded through embedded M6 screw bars
  (Fig. 1). Gauge length not reported; response given as stress vs elongation (mm).
- Loading / rate: uni-axial tension to different elongations to get different max crack widths;
  rate not reported. Re-tension after 28 d of healing.
- Measurement: digital microscope (crack width, crystal thickness on both faces); falling-head water
  permeability through the plate (Darcy, Eqs. 1–5; Nishiwaki & Mihashi 2003 set-up, Fig. 3); parallel-plate
  law k ∝ a·w³ (Eq. 6); Raman spectroscopy; backscattered-electron image analysis of hydration degree
  (Eq. 7).
- Curing & test age: 7 d standard curing before cracking; healing 28 d in 20 °C water; checks at 3, 14,
  28 d.
→ [[dogbone-uniaxial-tension]] (non-standard plate test) · [[permeability]]

## Key results
| Mix ID | f'c (MPa) | First-crack stress (MPa) | Tensile strength (MPa) | Tensile strain capacity (%) | Crack width (µm) | Other |
|---|---|---|---|---|---|---|
| Mortar | not reported | about 2 ≈ (Fig. 2) | about 2 ≈ | not reported (brittle) | — | Fig. 2 |
| FRCC(SC) | not reported | about 2.5–3 ≈ | about 2.5–3.2 ≈ (Fig. 2) | not reported (elongation 1–2.5 mm; localises) | max 35 / 76 / 88 / 757 (Table 3) | crystal thickness about 20 µm at 28 d (Fig. 5); recovery c ≈ 0 or < 0 (Fig. 15) |
| FRCC(PE) | not reported | about 2.5–2.8 ≈ | = first crack; softening after (Fig. 2, p. 224) | n/a (strain softening) | max 19 / 38 / 119 / 368 (Table 3) | about 98 µm crystals at 28 d (Fig. 5); c 0–100%, max about 60% (Fig. 15) |
| HFRCC | not reported | about 2.5–3 ≈ | about 3.3–3.6 ≈ (Fig. 2) | not reported ("very ductile", then localises) | max 17 / 81 / 407 / 710 (Table 3) | about 65 µm crystals at 28 d (Fig. 5); c about 60–320% (Fig. 15) |

Values marked ≈ are read from figures.

Main findings (with Table/Fig. location):
- **Healing product = CaCO₃** (Raman peaks of the cracked area match pure calcium carbonate, Fig. 12, p. 223).
- **Crystal thickness ranks with fibre count per volume**: SC < HFRCC < PE (Fig. 5; Table 2, p. 220).
  Deposition is fastest in the first 3 d (to about 60 µm in PE), then slows, attributed to the crystal
  layer limiting Ca²⁺ diffusion (p. 220).
- **100 µm threshold**: cracks < 100 µm sealed (attachment thickness ≈ crack width, slope ≈ 1) in all
  series; above 100 µm slopes 0.3673 (PE), 0.1037 (HFRCC), 0.0287 (SC) (Fig. 6, p. 220–221). In FRCC(PE)
  a 100 µm crack was repaired via crystals on bridging fibres (p. 220).
- **Permeability**: k dropped in all cracked specimens until 3 d, then slowed; wide cracks stayed
  almost constant after 3 d; small cracks kept decreasing and some reached the uncracked value (about
  10⁻¹¹ m/s ≈) by 28 d (Fig. 10, p. 223). At similar w ≈ 80–120 µm, PE and HFRCC fell more than SC
  (Fig. 11; HFRCC2 w = 81 µm from about 10⁻⁸ to about 10⁻¹¹·⁵ m/s ≈).
- k vs max crack width follows the cube law broadly, but scatters below 0.1 mm because of multiple
  cracking (Fig. 8, p. 222–223). k vs residual elongation is scattered (Fig. 7).
- Smoother crack surfaces (no fibres left) carried thinner deposits (Fig. 9, p. 223).
- **Strength recovery** c = (σ2 − σ0)/(σ1 − σ0) × 100 (Eq. 6, p. 224): SC ≈ 0 or negative (crystals
  absent, cords corroded); PE between 0 and 100 (reaches the unloading stress, not the original peak),
  higher at smaller residual elongation; HFRCC > 100 for residual elongation < 2 mm (Fig. 15, p. 225).
- Steel cords corroded on crack surfaces after 3 d (SC and HFRCC); in HFRCC corrosion stayed on the outer
  surface, not inside the crack, attributed to CaCO₃ covering the cords (Fig. 16, p. 225).
- Hydration degree α ≈ 63.2 / 65.3 / 65.4% (SC / PE / HFRCC, Fig. 18), no difference, so CaCO₃
  crystallisation, not further hydration, dominated (p. 226).

## Mechanisms / explanations offered by authors
- CO₂ dissolves in water; Ca²⁺ from the matrix reacts to CaCO₃ (pH-dependent, Eqs. 1–3 after
  Edvardsen 1999); crystals attach to crack faces and fibres (p. 218).
- Many very fine PE fibres bridging the crack give "tight space between fibres" and nucleation sites, so
  crystals can bridge wider cracks (Conclusion 2, p. 226).
- In HFRCC, healing products may restore the damaged steel-cord bond, explaining c > 100% (p. 225).
- FRCC(PE) is quasi-brittle because the 6 mm PE fibres are short (p. 224).

## Limitations (stated + observed)
- Observed: none of the mixes is a strain-hardening composite in the ECC sense: FRCC(PE) softens; HFRCC
  and SC localise after limited multiple cracking (p. 224). Results on "FRCC" may not transfer directly to ECC/HDC.
- Observed: four specimens per series, each at a different crack width, so no replication per width.
- Observed: healing in continuous water only (20 °C); no wet–dry or natural exposure.
- Observed: first-crack and peak stresses only in figures; no compressive strength; age at cracking 7 d
  (early age favours healing by further hydration, but BSE showed no α difference).
- Observed: SP/B 0.09 is high for a polycarboxylate; possibly a solution dosage (not stated).

## Relation to other work
- Agrees with: the ≈ 100 µm healing limit and fast early healing (first 3 d) reported as cited in
  [[ma2021-ecc-durability-review]] (< 60 µm: 3–4 d; > 100 µm: 7–10 d or more). Here, sealing was
  achieved up to about 100 µm (somewhat wider than 60 µm), and is fibre-count dependent.
- Agrees with: Li et al. 1998 (as cited, p. 218) that SHCC cracks heal with deposits and stiffness recovery.
- Contradicts: ⚔️ (partial) the wiki synthesis that PE-based composites heal poorly because their cracks are
  wider ([[self-healing]], [[crack-width]]): at equal crack width, fine PE fibres **promote** healing.
  The issue for PE-HSHDC is crack width, not the fibre itself.
- Extends: first primary self-healing source in the wiki; first data on steel-cord / hybrid fibres and
  CaCO₃ identification.

## Pages updated from this source
- [[self-healing]] · [[permeability]] · [[crack-width]] · [[pe-fiber]] · [[durability]] · [[ma2021-ecc-durability-review]]

## To verify
- [ ] DOI not printed (probably 10.3151/jact.7.217).
- [ ] SP/B 0.09 (Table 2): solid content or solution? Mass basis of ratios not stated.
- [ ] Sand "diameter 180 µm": mean or max size?
- [ ] First-crack and peak stresses read from Fig. 2 (≈ 2–3.6 MPa).
- [ ] Crystal thickness at 28 d read from Fig. 5 (≈ 98 / 65 / 20 µm).
- [ ] Fig. 6 regression slopes: refer to the full data in Fig. 6(b) (cracks up to about 3000 µm).
- [ ] Table 4 lists FRCC(SC) No. 2 crack width 1.976 mm and HFRCC No. 1 1.532 mm, unlike Table 3 (76 and 17 µm); authors say Table 4 uses both faces (p. 220).
