---
type: source
slug: jin2019-hvfa-shcc-structural
title: "Mechanical Properties of High-Volume Fly Ash Strain Hardening Cementitious Composite (HVFA-SHCC) for Structural Application"
authors: [Chenhua Jin, Chang Wu, Chengcheng Feng, Qingfang Zhang, Ziheng Shangguan, Zuanfeng Pan, Shaoping Meng]
year: 2019   # Materials 12(16), article 2607; published 16 Aug 2019
venue: "Materials (MDPI), Vol. 12, No. 16, Article 2607"
doi: "10.3390/ma12162607"
raw_file: raw/papers/Jin2019_HVFA-SHCC-structural.xml
material_term: "SHCC; HVFA-SHCC (high-volume fly ash SHCC); ECC used for the parent class in the introduction"
study_type: experimental + analytical (micromechanics and particle-packing guided mix design)
tags: [shcc, hvfa, fly-ash, pva-fiber, kuraray, mix-design, particle-size-distribution, andreasen-andersen, psh-index, dumbbell-tension, compression, elastic-modulus, four-point-bending, age-effect, southeast-university]
ingested: 2026-10-20
updated: 2026-10-20
---

# HVFA-SHCC for structural application (Jin et al., 2019)

## One-paragraph summary
Southeast University (Nanjing) with Tongji designed six PVA-SHCC mixes with **very high fly ash**:
FA/C = 2.4–4.4 by mass, i.e. fly ash ≥ 70% of binder (Table 2; abstract). The design combined a
micromechanics parametric study (Yang et al. 2008 bridging model, coded in MATLAB; Table 1, Fig. 1)
with particle-packing optimisation to the modified Andreasen & Andersen curve (q = 0.25; Eq. 3, Fig. 3).
All mixes used W/B 0.25, S/B 0.36 and 2 vol.% Kuraray REC-15 PVA (39 µm, 12 mm). At 28 d:
- Direct tension (dumbbell, 80 mm gauge): ε_tu 1.92% (FA2.4), **3.42% (FA3.2)**, 3.07% (FA4.4); σ_tp 3.97–4.10 MPa;
  first-crack strength falls from 3.67 to 3.26 MPa as FA rises (Table 5).
- Compression (100 × 100 × 300 mm prisms): all mixes > 30 MPa at 28 d, falling with FA; peak strain about
  0.5–0.7% (Fig. 8, values not tabulated).
- Four-point bending (coupon 350 × 50 × 15 mm): flexural cracking strength falls almost linearly with FA,
  deflection rises with FA up to FA3.2 then plateaus (Fig. 14).
The authors recommend **FA3.2** (FA/B ≈ 76%) for structural use.

## Objective / research question
- Develop a sustainable SHCC with FA ≥ 70% of binder that meets three goals (§2.1):
  1. tensile strain hardening and multiple cracking, target ε_tu > 2%;
  2. acceptable flowability, homogeneity, fiber dispersion;
  3. f'c > 30 MPa at 28 d, the minimum for most structural uses per GB50010-2010 (as cited).
- Quantify how FA/C (2.4–4.4) affects tension, compression and flexure.

## Materials & mix design
| Mix ID | Cement | Fly ash | Slag/other | Sand (type, max size) | W/B | SP | Fiber type | L (mm) | d (µm) | Vf (vol.%) |
|---|---|---|---|---|---|---|---|---|---|---|
| FA2.4 | 1.0 (P.II 42.5) | 2.4 (Grade I) | none | silica sand, avg 110 µm, max 0.3 mm; S/B 0.36 | 0.25 | 0.0082 (polycarboxylate) | PVA, Kuraray K-II REC-15 | 12 | 39 | 2.0 |
| FA2.8 | 1.0 | 2.8 | none | same | 0.25 | 0.0062 | same | 12 | 39 | 2.0 |
| FA3.2 | 1.0 | 3.2 | none | same | 0.25 | 0.0071 | same | 12 | 39 | 2.0 |
| FA3.6 | 1.0 | 3.6 | none | same | 0.25 | 0.0068 | same | 12 | 39 | 2.0 |
| FA4.0 | 1.0 | 4.0 | none | same | 0.25 | 0.0047 | same | 12 | 39 | 2.0 |
| FA4.4 | 1.0 | 4.4 | none | same | 0.25 | 0.0042 | same | 12 | 39 | 2.0 |

Units of binder quantities: Table 2 header says "Cement (kg)", "FA (kg)", "SP (kg)", i.e. mass proportions
relative to cement = 1 (no kg/m³ given). S/B and W/B are ratios to binder (cement + FA); "by mass" is implied
by the kg header but not stated ⚠️. FA/B computed here: 70.6% (FA2.4) to 81.5% (FA4.4); FA3.2 = 76.2%
(paper: "about 76%", §3.4.2). Mixing: dry 1.5 min, then water + SP 3 min, then fibers; about 10 min total (§3.1).

**Fly ash and cement** (Table 3): FA SiO₂ 49.29%, Al₂O₃ 27.8%, CaO 7.22%, LOI 3.99%; cement CaO 63.85%.
Fly-ash class (ASTM C/F) not stated; "Grade I" (Chinese grading), Nanjing Thermal Power Plant.

**PVA fiber** (Table 4): 39 µm, 12 mm, elongation 7%, density 1.3 g/cm³, nominal strength 1620 MPa,
elastic modulus "42.8 MPa" ⚠️ (unit evidently GPa, as in [[li2002-pva-ecc-interface-tailoring]] Table 1).
Oil coating not stated (REC-15 is the oiled ECC grade per other sources).

**Model inputs for the parametric study** (Table 1, after Li et al. 2002 [ref 29]): d_f 39 µm, L_f 12 mm,
E_f 22 GPa, Vf 2.0%, τ0 1.0 MPa, Gd 1.5 J/m², f_f 1092 MPa. These are assumed, not measured on the HVFA matrix.

## Test methods
- Specimen geometry:
  - Tension: dumbbell, 30 × 30 mm middle section, ≥ 6 per mix; only FA2.4, FA3.2, FA4.4 tested (§3.2.1). Overall length not reported.
  - Compression / modulus: prisms 100 × 100 × 300 mm, 3 + 3 per mix (§3.3.1).
  - Flexure: coupon 350 × 50 × 15 mm, four-point, third-point loading (load span = shear span), ≥ 6 per group (§3.4.1). Span not reported.
- Loading / rate: tension 0.2 mm/min displacement control (30 kN servo); compression 0.3 mm/min after three
  preloads to 5 MPa; modulus at 0.3 MPa/s to about 1/3 f'c per GB/T 50081-2002; bending 0.5 mm/min.
- Measurement: tension 2 LVDTs on an aluminium frame, 80 mm gauge (Fig. 5); compression 2 strain gauges; bending 1 mid-span LVDT.
  Misaligned tension specimens were excluded (§3.2.2).
- Curing & test age: demould 24 h, standard room 23 ± 2 °C, RH 95 ± 5%; tension at 28 d; compression 28 d (all), plus 7 / 28 / 90 d for FA3.2;
  bending at 7, 28 and 90 d (Fig. 14).
→ [[dogbone-uniaxial-tension]] · [[flexural-strength]] · [[compressive-strength]]

## Key results
| Mix ID | f'c (MPa) | First-crack stress (MPa) | Tensile strength (MPa) | Tensile strain capacity (%) | Crack width (µm) | Other |
|---|---|---|---|---|---|---|
| FA2.4 | > 30 (Fig. 8a, value not tabulated) | 3.67 (ε_fc 0.019%) | 3.97 | 1.92 | not reported | Table 5, 28 d |
| FA3.2 | > 30 (Fig. 8a) | 3.34 (ε_fc 0.020%) | 4.10 | 3.42 | not reported | Table 5, 28 d; 7-d f'c = 46.6% of 28-d; 90-d ≈ +12% |
| FA4.4 | > 30 (Fig. 8a) | 3.26 (ε_fc 0.022%) | 3.99 | 3.07 (more scatter) | not reported | Table 5, 28 d |
| FA2.8 / 3.6 / 4.0 | > 30 (Fig. 8a) | not tested in tension | — | — | — | bending and compression only |

Strain basis: Table 5 labels it "ultimate tensile strain ε_tu" next to peak stress σ_tp; whether it is the
strain at peak or at test end is not stated ⚠️ (test stopped at onset of softening, §3.2.1).

Main findings (with Table/Fig. location):
- FA/C 2.4 → 3.2 raised ε_tu by 78%; 3.2 → 4.4 lowered it by 10% and reduced stability (Table 5; Conclusion 3).
- First-crack strength falls with FA (3.67 → 3.26 MPa), σ_tp roughly constant 3.97–4.10 MPa (Table 5).
- f'c and E fall with FA/C; E is almost linear in f'c (Fig. 8d fit, coefficients not given in text). Peak compressive strain
  0.5–0.7%, rising with FA (Fig. 8b). E lower than ordinary concrete (no coarse aggregate) (§3.3.2).
- FA3.2 strength gain: 7 d = 46.6% of 28 d; 90 d ≈ 12% above 28 d (Fig. 9, §3.3.2).
- Flexure: cracking strength falls nearly linearly with FA at 7 d, less steeply at 90 d; flexural strength highest for FA3.2 at 7 d,
  and at 90 d FA3.2 ≈ FA2.8 > others; deflection grows with FA, no significant gain beyond FA3.6–4.4 (Fig. 14).
- Parametric model (Fig. 1): σ0 and J′b/J_tip rise linearly with Vf; J′b/J_tip falls linearly with Gd, falls sharply then gently with τ0,
  and falls parabolically with Km.
- PSD (Fig. 3): deviation from the A&A curve < 10% and flattens for FA/C > 2.4; minimum at S/B ≈ 0.4.

## Mechanisms / explanations offered by authors
- More FA lowers fiber/matrix bond (Gd, τ0) and matrix toughness Km, so the energy criterion is satisfied more easily → higher ε_tu (§3.2.2).
- Too much FA reduces mix stability/uniformity → scatter and slightly lower ε_tu at FA4.4 (§3.2.2).
- FA is mainly a filler early (slow pozzolanic reaction) → low 7-d strength, strong later gain (§3.3.2).
- Flexural strength depends on matrix strength and on deformation capacity (longer hardening stage), so it does not fall monotonically with FA (§3.4.2).
- Raising W/B and FA/C lowers bond and Km, but raising W/B costs strength, so water is controlled (§2.2).
- PSD continuous grading improves packing and workability; FA fills the fine fraction (§2.3).

## Limitations (stated + observed)
- Stated: low elastic modulus is a drawback for deflection control and seismic resistance; further work should raise E (§3.3.2).
- Observed:
  - Only 3 of 6 mixes tested in tension; no crack width or crack count reported.
  - f'c, E, flexural values are only in figures; no numbers in text or tables.
  - No measured micromechanical parameters on the HVFA matrix; model inputs are borrowed from Li 2002.
  - PSH thresholds quoted as σ0/σfc > 1.45 (Kanda & Li 1998, as cited), not computed for the actual mixes.
  - Tension at 28 d only; no long-term ageing of ε_tu despite slow FA reaction.
  - Fiber modulus unit error in Table 4 (MPa vs GPa).

## Relation to other work
- Agrees with: [[yang2024-hshdc-uniaxial-tension]] (more FA → higher strain, lower first-crack strength); [[chai2023-hdc-ambient-temperature]] (highest-FA mix best ε_tu); FA lowers bond ([[fiber-matrix-interface]]).
- Contradicts: ⚔️ PSH strength threshold quoted as σ0/σfc > 1.45 for PVA (Kanda & Li 1998, as cited, §2.2), whereas the wiki records 1.2 (1998) and 1.3 (2006, fiber rupture) ([[kanda2006-psh-design-criteria]]).
- Extends: pushes FA/C to 4.4 (FA/B 81.5%), above M45 (FA/C 1.2, [[yang2008-ecc-fiber-bridging-law]]) and shows a ductility plateau/optimum at FA/C ≈ 3.2.

## Pages updated from this source
- [[fly-ash]] · [[pva-fiber]] · [[fiber-matrix-interface]] · [[tensile-strain-capacity]] · [[strain-hardening]]
- [[compressive-strength]] · [[flexural-strength]] · [[dogbone-uniaxial-tension]] · [[matrix-fracture-toughness]]
- [[mix-designs]] · [[mechanical-results]] · [[li2002-pva-ecc-interface-tailoring]] · [[yang2008-ecc-fiber-bridging-law]]

## To verify
- [ ] f'c, E and peak compressive strain per mix: read Fig. 8 from the PDF/figure images (not in text).
- [ ] Flexural cracking strength, flexural strength and deflection per mix and age: read Fig. 14.
- [ ] Whether Table 5 ε_tu is strain at peak stress or at end of test.
- [ ] Table 4 fiber modulus "42.8 MPa" — assumed GPa.
- [ ] PSH threshold σ0/σfc > 1.45 attributed to Kanda & Li 1998 — check against the original.
- [ ] Mass basis of S/B and W/B (implied by "kg" header only); SP basis (kg per unit cement).
- [ ] Oil coating level of the REC-15 fibers (not stated in paper).
