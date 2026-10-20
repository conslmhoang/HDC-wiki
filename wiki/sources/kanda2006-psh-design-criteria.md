---
type: source
slug: kanda2006-psh-design-criteria
title: "Practical Design Criteria for Saturated Pseudo Strain Hardening Behavior in ECC"
authors: [Tetsushi Kanda, Victor C. Li]
year: 2006            # J. Adv. Concr. Technol. 4(1), February 2006; received 14 Oct 2005, accepted 5 Dec 2005
venue: "Journal of Advanced Concrete Technology, Vol. 4, No. 1, pp. 59-72 (Japan Concrete Institute)"
doi: "not printed in the PDF (⚠️ unverified; commonly given as 10.3151/jact.4.59)"
raw_file: raw/papers/Kanda2006_PSH-design-criteria.pdf
material_term: "ECC (Engineered Cementitious Composites); 'fiber rupture type' vs 'fiber pull-out type' PSH composites"
study_type: "analytical + experimental (uniaxial tension, 5 composites)"
tags: [psh-criteria, strain-hardening, first-cracking-strength, flaw-size, saturated-multiple-cracking, pva-fiber, pe-fiber, micromechanics]
ingested: 2026-10-20
updated: 2026-10-20
---

# PSH design criteria for saturated strain hardening (Kanda & Li, 2006)

## One-paragraph summary
Kanda & Li extend the two micromechanical **performance indices** of pseudo strain hardening (PSH),
the stress index σ_peak/(σ_fc)_i and the energy index J′b/J_tip, from fiber pull-out type ECC to
**fiber rupture type ECC** (PVA fibers that break during bridging). They propose a new first-cracking
strength theory (penny-shaped flaw bridged by fibers, with fiber rupture, and an empirical
**reduction factor 0.8**), with the flaw size taken from matrix toughness and matrix tensile strength.
Five paste-matrix composites (40 µm PVA, 14 µm PVA, 14 µm PE; w/c 0.27 and 0.42) are tested in
uniaxial tension (ε_cu 0.26–5.10%, Table 4). PSH saturation is measured by a **saturation index**
x_d^test/x_d (observed / theoretical crack spacing), with saturation taken as x_d^test/x_d ≤ 2.
The proposed practical criteria for **saturated** PSH are **(σ_peak/σ_fc)^est > 1.3** (test-based
> 1.35) and **J′b/J_tip > 2.7**, both to be met at the same time (p. 69–70). These are compared with
the pull-out-type criteria of Kanda & Li 1998b: **> 1.2 and > 3** (p. 69).

## Objective / research question
Provide practical micromechanics-based design criteria that ensure **saturated** PSH (saturated
multiple cracking) in fiber rupture type ECC, which needs a first-cracking strength theory that
includes fiber rupture and chemical bond (p. 59–60).

## Materials & mix design
Matrix = cement paste (no sand), Table 2. Fibers and composites: Tables 1 and 3.

| Mix ID | Cement | Fly ash | Slag/other | Sand (type, max size) | W/B | SP | Fiber type | L (mm) | d (µm) | Vf (vol.%) |
|---|---|---|---|---|---|---|---|---|---|---|
| 40PVA-27 (ref., Kanda & Li 1999) | 0.8 | 0 | SF 0.2 (included in "cement" weight) | none | 0.27 (w/c, SF counted in c) | 0.040 | PVA (hydrophilic) | 12 | 40 | 2 |
| 40PVA-42 | 1.0 | 0 | none; viscous agent 0.0015 | none | 0.42 | 0.007 | PVA | 12 | 40 | 2 |
| 14PVA-27 (ref., Kanda & Li 1999) | 0.8 | 0 | SF 0.2 | none | 0.27 | 0.040 | PVA | 6 | 14 | 1.5 |
| 14PVA-42 | 1.0 | 0 | viscous agent 0.0015 | none | 0.42 | 0.007 | PVA | 6 | 14 | 1.5 |
| 14PE-27 | 0.8 | 0 | SF 0.2 | none | 0.27 | 0.040 | PE (hydrophobic, no chemical bond) | 6 | 14 | 2 |

Units of binder quantities: mass ratio (Table 2); the footnote says silica fume is included in the
cement weight, so W/B = w/c as printed. Curing regime and age: **not reported** in this paper
(the two reference composites come from Kanda & Li 1999).

Fiber and micromechanical inputs (Table 3; footnotes give the source of each value):
- Ef: 21.8 GPa (40 µm PVA), 60 GPa (14 µm PVA), 63 GPa (14 µm PE).
- Nominal fiber strength σ_fu^n: 806 / 1666 / 1400 MPa (PE value **assumed**).
- Matrix: Em 23 GPa (w/c 0.27) and 15.9 GPa (w/c 0.42, after Hirsch 1962); Km 0.33 and 0.23 MPa√m
  (0.23 after Ogishi); σ_mu 1.60 and 1.12 MPa (after Li et al. 1995).
- τ_i (frictional bond): 2.21 / 2.21 (40 µm PVA, w/c 0.27 / 0.42); 4.35 / 4.25 (14 µm PVA); 0.66 (PE).
- τ_s (chemical bond strength, MPa): 31.3 / 31.3 (40 µm PVA); 33.6 / 29.1 (14 µm PVA); none (PE).
- Snubbing f = 0.5 and fiber strength reduction factor f′ = 0.3 for all.
- All five composites satisfy Lr < Lf, i.e. they are designed to have fiber rupture (Eq. 14, p. 64).

## Test methods
- Specimen geometry: coupon 305 mm long × 76.2 mm wide × 12.7 mm thick, glued aluminium end plates (Fig. 3).
- Loading / rate: uniaxial tension; rate **not reported**.
- Measurement (LVDT, DIC, ...): two LVDTs over a 205 mm gauge length (Fig. 3).
- Curing & test age: not reported.
- Definitions (p. 64): (σ_fc)_i^test = first inflection point of σ–ε curve (Fig. 7); σ_peak^test = peak
  stress; ε_cu^test = strain beyond which continuous stress drop starts. Averages of 3 specimens.
→ [[dogbone-uniaxial-tension]]

## Key results
| Mix ID | f'c (MPa) | First-crack stress (MPa) | Tensile strength (MPa) | Tensile strain capacity (%) | Crack width (µm) | Other |
|---|---|---|---|---|---|---|
| 40PVA-27 | not reported | 2.47 | 3.25 | 1.03 (ultimate, ε_cu) | not reported | σ_peak/σ_fc test = 1.32 (computed here) |
| 40PVA-42 | not reported | 1.85 | 2.43 | 1.50 | not reported | 1.31 (computed here) |
| 14PVA-27 | not reported | 3.99 | 4.62 | 0.26 | not reported | 1.16 (computed here) |
| 14PVA-42 | not reported | 2.92 | 3.32 | 0.55 | not reported | 1.14 (computed here); excluded from criteria (plug pull-out) |
| 14PE-27 | not reported | 2.25 | 3.25 | 5.10 | not reported | 1.44 (computed here); saturated PSH |

All from Table 4 (p. 65). Stress-index values are Table 4 ratios computed here; they match the test
points in Fig. 14 (≈ 1.16, 1.31, 1.32, 1.44).

Energy index values are **not tabulated**. Read from Figs. 15–16 (≈): 14PVA-27 ≈ 1.1; 40PVA-27 ≈ 2.4–2.5;
40PVA-42 ≈ 3.0; 14PE-27 ≈ 3.0 (⚠️ read from figure). Saturation index x_d^test/x_d (Fig. 16, ≈):
≈ 14 (14PVA-27), ≈ 3 (40PVA-27 and 40PVA-42), ≈ 0.5–1 (14PE-27, the only point below the
saturation line of 2).

Main findings (with Table/Fig. location):
- **Index definitions** (p. 60–61, Eqs. 1–4):
  - Strength condition (σ_fc)_i < σ_peak; energy condition J_tip < J′b.
  - J′b = σ_peak·δ_peak − ∫₀^δpeak σ_c(δ) dδ (complementary energy, Marshall & Cox 1988), Eq. 4.
  - Stress performance index = σ_peak/(σ_fc)_i; energy performance index = J′b/J_tip.
  - σ_peak is the peak **fiber bridging** stress; (σ_fc)_i is the first-cracking strength, which
    varies from one potential crack plane to another (subscript i). The test version uses the
    composite peak stress σ_peak^test over the first-crack stress.
  - "Both these performance indices must exceed unity for realizing PSH behavior" (p. 60). Values
    above 1 are **margins** for matrix and bridging variability; higher margins give more saturated
    multiple cracking.
- **First-cracking strength theory** (p. 61–63, Eqs. 5–13):
  - K_L + K_B = K_tip for a penny-shaped flaw of radius c, with K_tip = Km(Ec/Em) (after Marshall et al. 1985).
  - Bridging closure integrated over a half-parabolic crack profile (Eq. 8); fibers inside radius Ru
    have ruptured (Eqs. 9–10).
  - Flaw size c_m = (√π/2 · Km/σ_mu)² (Eq. 12), from plain-matrix tensile strength.
  - Without correction, σ_fc(c_m) overestimates the test first-crack strength by **45% on average**
    (Fig. 12, p. 67). Two reasons: extra air-void flaws from fiber mixing, and the assumed crack
    profile (up to 20% overestimate per Marshall et al. 1985).
  - With the reduction factor **0.8** (Eq. 13), prediction matches tests **within 10%** (p. 70).
  - The c_m from Eq. 12 is "too large" compared with flaw sizes observed in composites (Kanda & Li
    2000), because a single non-interacting flaw is assumed (p. 67–68). (Computed here: c_m ≈ 33 mm
    for both matrices, from Table 3 values.)
- **Effects of the two design levers** (p. 64–66, Figs. 4–9):
  - Raising w/c 0.27 → 0.42: ε_cu 0.26 → 0.55% (14 µm PVA) and 1.03 → 1.50% (40 µm PVA). It lowers
    σ_fc (Fig. 8a) and J_tip (about 30% lower, after Ogishi & Ono 1987), while J′b of 14 µm PVA is
    almost unchanged (Fig. 9).
  - Using 14 µm PE (no chemical bond): much lower σ_fc (Fig. 8b) and much higher J′b (Fig. 9);
    ε_cu > 5%. Even at Vf 1.5%, PE gives about **twice** the J′b/J_tip of 14 µm PVA (calculation, p. 66).
- **σ_peak prediction** (Fig. 10): consistent with tests except 14PVA-42 (> 50% error), attributed to
  **plug pull-out** (fibers pulled out with a matrix plug in the weaker w/c 0.42 matrix, Fig. 11);
  this mix is excluded from the criteria (p. 66–67).
- **Indices vs ε_cu** (Figs. 14–15, p. 68): ε_cu rises steeply with both indices. The theoretical
  stress index is about 10% higher than the test index at the same ε_cu.
- **Saturation index** (p. 69, Eqs. 15–16):
  - x_d = theoretical saturated crack spacing (Wu & Li 1995), neglecting chemical bond, so an upper bound.
  - x_d^test = δ_peak/ε_cu^test (crack spacing inferred, **not counted**).
  - x_d^test/x_d = 2 is the design limit "above which saturated PSH behavior is rarely expected"
    (Kanda & Li 1998b).
- **Criteria derived** (p. 69–70):
  - Energy: the fitted curve in Fig. 16 crosses x_d^test/x_d = 2 near **J′b/J_tip = 2.7**.
    The pull-out type criterion was **> 3** (Kanda & Li 1998b).
  - Stress: test data (Fig. 17) need **(σ_peak/σ_fc)^test > 1.35**; theory slightly underestimates,
    so **(σ_peak/σ_fc)^est > 1.3** is the practical criterion. The pull-out type value was **> 1.2**
    (Kanda & Li 1998b).
  - Both criteria must be satisfied **simultaneously**: small flaws (small c_m) raise σ_fc and can
    violate the stress criterion even if J′b/J_tip > 2.7; large flaws can satisfy the stress criterion
    but without J′b/J_tip > 2.7 steady-state cracking may not occur on each crack plane.
  - The authors suggest the criteria may apply to various composites "independent of existing fiber
    rupture and chemical bond" (p. 70).

## Mechanisms / explanations offered by authors
- Fiber rupture type ECC (PVA: moderate fiber strength, small diameter, strong chemical bond) has
  lower complementary energy J′b than pull-out type (PE) ECC, which explains unsaturated PSH (p. 59).
- Overly strong bond (τ_i, τ_s) causes severe fiber rupture, lowering J′b and J′b/J_tip; chemical bond
  stiffens the bridging curve and lowers J′b (p. 63, citing Kanda 1998 and Kanda & Li 1999).
- Higher w/c weakens the PVA bond and lowers J_tip and σ_fc, but also lowers matrix shear strength,
  which can trigger plug pull-out (p. 66–67).
- The stress criterion depends on the **flaw size**: larger flaws lower σ_fc (Eq. 13, Fig. 8).

## Limitations (stated + observed)
- Stated: the criteria rest on "limited test data"; further investigation is needed (p. 70).
- Stated: flaw size is not measured; c_m from Eq. 12 is unrealistically large; a model with random
  interacting flaws is needed (p. 68).
- Stated: x_d neglects chemical bond (upper bound); the 0.8 factor is empirical.
- Observed: only **4** composites define the criteria (14PVA-42 excluded), and only **one** (14PE-27)
  falls below the saturation line, so both thresholds are read from fitted curves through few points.
- Observed: J′b/J_tip is not measured, only computed from the bridging model; numerical J′b and
  J_tip values are not tabulated.
- Observed: paste matrix without sand, low strength (σ_fc 1.85–3.99 MPa); no curing age or
  loading rate; crack spacing inferred from δ_peak/ε_cu, not counted.
- Observed: Fig. 16 text writes the ratio once as "xd/xd^test" (typo; the axis is x_d^test/x_d).

## Relation to other work
- Agrees with: [[li2002-pva-ecc-interface-tailoring]]: crack saturation begins near J′b/J_tip ≈ 3 in
  PVA-ECC, close to the 2.7 criterion here.
- Contradicts: ⚔️ The wiki (via [[su2023-rubber-modified-hshdc]] and [[ranade2015-hshdc-tensile-rate-effects]])
  cites "Kanda & Li 1998" for > 1.2 and > 3. This paper attributes 1.2 / 3 to Kanda & Li 1998b for
  **pull-out type** composites and proposes **1.3 / 2.7** for fiber rupture type. Not a true conflict,
  but the thresholds depend on fiber type and on whether the stress index is from theory (1.3) or tests (1.35).
  ⚔️ The 6 mm PE mixes of [[su2023-rubber-modified-hshdc]] pass both indices but fail brittle; this paper
  says only that both criteria must hold together and depend on flaw size.
- Extends: [[li1992-steady-state-multiple-cracking]] (first-crack theory for pull-out fibers) to fiber
  rupture and chemical bond; J-integral energy condition after Marshall & Cox 1988.

## Pages updated from this source
- [[strain-hardening]]
- [[steady-state-cracking]]
- [[multiple-cracking]]
- [[matrix-fracture-toughness]]
- [[fiber-matrix-interface]]
- [[pva-fiber]]
- [[pe-fiber]]
- [[tensile-strain-capacity]]
- [[water-binder-ratio]]
- [[micromechanical-parameters]]
- [[mechanical-results]]
- [[mix-designs]]
- [[dogbone-uniaxial-tension]]
- [[gaps]]

## To verify
- [ ] DOI (not printed in the PDF; 10.3151/jact.4.59 is from general knowledge).
- [ ] Energy-index values per mix (≈ 1.1, 2.4–2.5, 3.0, 3.0) and saturation-index values are read from Figs. 15–16, not tabulated.
- [ ] Which mix is which point in Figs. 15–16 (the PE point is labelled; the others are inferred from ε_cu in Table 4).
- [ ] Table 3 footnote cites "Ogishi 1997" for Km = 0.23, but the reference list has Ogishi & Ono 1987.
- [ ] Unit of τ_s (chemical bond "strength", 29–34 MPa) differs from the Gd (J/m²) used elsewhere in the wiki; conversion not given.
- [ ] Curing regime, test age and loading rate (not reported here; may be in Kanda & Li 1999).
- [ ] Exact citation behind "Kanda & Li 1998b" (> 1.2, > 3): "Multiple Cracking Sequence and Saturation in Fiber Reinforced Cementitious Composites", Concrete Research and Technology (JCI) 9(2), 1–15 (reference list, p. 70).
