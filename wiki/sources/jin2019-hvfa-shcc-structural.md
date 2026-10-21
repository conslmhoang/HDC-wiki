---
type: source
slug: jin2019-hvfa-shcc-structural
title: "Mechanical Properties of High-Volume Fly Ash Strain Hardening Cementitious Composite (HVFA-SHCC) for Structural Application"
authors: [Chenhua Jin, Chang Wu, Chengcheng Feng, Qingfang Zhang, Ziheng Shangguan, Zuanfeng Pan, Shaoping Meng]
year: 2019   # Materials 12(16), article 2607; received 27 Jul, accepted 14 Aug, published 16 Aug 2019
venue: "Materials (MDPI), Vol. 12, No. 16, Article 2607 (18 pp.)"
doi: "10.3390/ma12162607"
raw_file: raw/papers/Jin2019_HVFA-SHCC-structural.pdf
material_term: "SHCC; HVFA-SHCC (high-volume fly ash SHCC); ECC used for the parent class in the introduction"
study_type: experimental + analytical (micromechanics and particle-packing guided mix design)
tags: [shcc, hvfa, fly-ash, pva-fiber, kuraray, mix-design, particle-size-distribution, andreasen-andersen, psh-index, dumbbell-tension, compression, elastic-modulus, four-point-bending, age-effect, southeast-university]
ingested: 2026-10-20
updated: 2026-10-21
---

# HVFA-SHCC for structural application (Jin et al., 2019)

> Re-checked against the publisher PDF on 2026-10-21 (page numbers added; Fig. 8, 9, 14 values read from the PDF).

## One-paragraph summary
Southeast University (Nanjing) with Tongji designed six PVA-SHCC mixes with **very high fly ash**:
FA/C = 2.4–4.4 by mass, i.e. fly ash ≥ 70% of binder (Table 2, p. 7; abstract, p. 1). The design combined a
micromechanics parametric study (Yang et al. 2008 bridging model, coded in MATLAB; Table 1, p. 3; Fig. 1, p. 4–5)
with particle-packing optimisation to the modified Andreasen & Andersen curve (q = 0.25; Eq. 3, p. 6; Fig. 3, p. 7).
All mixes used W/B 0.25, S/B 0.36 and 2 vol.% Kuraray REC-15 PVA (39 µm, 12 mm). At 28 d:
- Direct tension (dumbbell, 80 mm gauge): ε_tu 1.92% (FA2.4), **3.42% (FA3.2)**, 3.07% (FA4.4); σ_tp 3.97–4.10 MPa;
  first-crack strength falls from 3.67 to 3.26 MPa as FA rises (Table 5, p. 10).
- Compression (100 × 100 × 300 mm prisms): f'c falls from 46.7 MPa (FA2.4) to 32.5 MPa (FA4.4); E from 22.2 to 15.7 GPa;
  peak strain rises from 0.52 to 0.69% (Fig. 8a–c, p. 11–12, bar labels).
- Four-point bending (coupon 350 × 50 × 15 mm, 300 mm span), at 7 and 90 d: flexural cracking strength falls almost
  linearly with FA (7 d: 7.2 → 4.8 MPa); flexural strength is not monotonic (7 d peak 13.6 MPa for FA3.2); mid-span
  deflection rises with FA and is smaller at 90 d than at 7 d (Fig. 14, p. 15).
The authors recommend **FA3.2** (FA/B ≈ 76%) for structural use (§3.4.2, p. 15; Conclusion 6, p. 16).

## Objective / research question
- Develop a sustainable SHCC with FA ≥ 70% of binder that meets three goals (§2.1, p. 2):
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

Units of binder quantities: Table 2 (p. 7) header says "Cement (kg)", "FA (kg)", "SP (kg)", i.e. mass proportions
relative to cement = 1 (no kg/m³ given). S/B and W/B are ratios to binder (cement + FA); "by mass" is implied
by the kg header but not stated ⚠️ (the abstract, p. 1, gives FA content "by weight"). FA/B computed here: 70.6% (FA2.4)
to 81.5% (FA4.4); FA3.2 = 76.2% (paper: "about 76%", p. 15). Mixing: dry 1.5 min, then water + SP 3 min, then fibers;
about 10 min total (§3.1, p. 8).

**Fly ash and cement** (Table 3, p. 7): FA SiO₂ 49.29%, Al₂O₃ 27.8%, Fe₂O₃ 6.63%, CaO 7.22%, LOI 3.99%; cement CaO 63.85%,
SiO₂ 20.35%. Fly-ash class (ASTM C/F) not stated; "Grade I" (Chinese grading), Nanjing Thermal Power Plant (p. 7).

**PVA fiber** (Table 4, p. 7): 39 µm, 12 mm, elongation 7%, density 1.3 g/cm³, nominal strength 1620 MPa,
elastic modulus printed "42.8" with unit "(MPa)" in the PDF ⚠️ (unit evidently GPa, as in [[li2002-pva-ecc-interface-tailoring]] Table 1).
Oil coating not stated (REC-15 is the oiled ECC grade per other sources).

**Model inputs for the parametric study** (Table 1, p. 3, after Li et al. 2002 [ref 29]): d_f 39 µm, L_f 12 mm,
E_f 22 GPa, Vf 2.0%, τ0 1.0 MPa, Gd 1.5 J/m², f_f 1092 MPa. These are assumed, not measured on the HVFA matrix.
Ranges swept in Fig. 1 (p. 4–5): Vf 0.5–2.5%, Gd 1–8 J/m², τ0 1–5 MPa, Km ≈ 8–20 MPa·mm^0.5 (x-axis of Fig. 1g).

## Test methods
- Specimen geometry:
  - Tension: dumbbell, 30 × 30 mm middle section, ≥ 6 per mix; only FA2.4, FA3.2, FA4.4 tested (§3.2.1, p. 8). Overall length not reported; Fig. 7 (p. 10) plots 3 curves per mix after excluding misaligned specimens.
  - Compression / modulus: prisms 100 × 100 × 300 mm, 3 + 3 per mix (§3.3.1, p. 10).
  - Flexure: coupon 350 × 50 × 15 mm, four-point, support span 300 mm divided into three 100 mm thirds (Fig. 11, p. 13), ≥ 6 per group (§3.4.1, p. 12). σ_f = FL/(bh²) (Eq. 4, p. 14).
- Loading / rate: tension 0.2 mm/min displacement control (30 kN servo); compression 0.3 mm/min (3000 kN servo) after three
  preloads to 5 MPa; modulus at 0.3 MPa/s to about 1/3 f'c per GB/T 50081-2002; bending 0.5 mm/min (p. 8, 10, 12).
- Measurement: tension 2 LVDTs on an aluminium frame, 80 mm gauge (Fig. 5, p. 9); compression 2 strain gauges; bending 1 mid-span LVDT.
  Misaligned tension specimens were excluded (§3.2.2, p. 8–9).
- Curing & test age: demould 24 h, standard room 23 ± 2 °C, RH 95 ± 5%; tension at 28 d; compression 28 d (all), plus 7 / 28 / 90 d for FA3.2;
  bending at **7 and 90 d** (Fig. 14 and text, p. 14–15). (Earlier version of this page said 7, 28 and 90 d; corrected from the PDF.)
→ [[dogbone-uniaxial-tension]] · [[flexural-strength]] · [[compressive-strength]] · [[four-point-bending-inverse-analysis]]

## Key results
| Mix ID | f'c (MPa) | First-crack stress (MPa) | Tensile strength (MPa) | Tensile strain capacity (%) | Crack width (µm) | Other |
|---|---|---|---|---|---|---|
| FA2.4 | 46.7 | 3.67 (ε_fc 0.019%) | 3.97 | 1.92 | not reported | E 22.2 GPa; ε_c,peak 0.52%; 28 d (Table 5; Fig. 8) |
| FA2.8 | 41.2 | not tested in tension | — | — | — | E 20.6 GPa; ε_c,peak 0.56% |
| FA3.2 | 39.9 | 3.34 (ε_fc 0.020%) | 4.10 | 3.42 | not reported | E 20.3 GPa; ε_c,peak 0.59%; 7-d f'c = 46.6% of 28-d; 90-d ≈ +12% |
| FA3.6 | 38.8 | not tested in tension | — | — | — | E 19.1 GPa; ε_c,peak 0.62% |
| FA4.0 | 37 | not tested in tension | — | — | — | E 17.5 GPa; ε_c,peak 0.66% |
| FA4.4 | 32.5 | 3.26 (ε_fc 0.022%) | 3.99 | 3.07 (more scatter) | not reported | E 15.7 GPa; ε_c,peak 0.69% |

f'c, E and ε_c,peak are 28-d means printed as bar labels in Fig. 8a–c (p. 11–12), not tabulated in the text.
Tension values: Table 5 (p. 10), 28 d.

Strain basis: Table 5 labels it "ultimate tensile strain ε_tu" next to peak stress σ_tp; the test stopped at onset of
softening (§3.2.1, p. 8). In Fig. 7 (p. 10) the curves reach their maximum stress just before the drop, so ε_tu
corresponds closely to the strain at peak stress / onset of softening (interpretation from the figure; the paper
does not define it explicitly).

**Flexure, coupon 350 × 50 × 15 mm** (Fig. 14, p. 15; bar labels, MPa and mm):

| Mix | Flex. cracking strength 7 d / 90 d | Flexural strength 7 d / 90 d | Ultimate mid-span deflection 7 d / 90 d |
|---|---|---|---|
| FA2.4 | 7.2 / 9.6 | 11.6 / 16.8 | 20.4 / 13.9 |
| FA2.8 | 6.6 / 9.2 | 11.1 / 14.4 | 24.8 / 12.9 |
| FA3.2 | 5.5 / 9.1 | 13.6 / 16.7 | 33.8 / 23 |
| FA3.6 | 5.2 / 8.7 | 9.8 / 14.5 | 31.3 / 25.9 |
| FA4.0 | 4.9 / 8.3 | 11.1 / 13.9 | 36.1 / 27.7 |
| FA4.4 | 4.8 / 8.2 | 10.2 / 13.1 | 36.2 / 27.6 |

Note: the y-axis of Fig. 14b is printed "Flexural cracking strength" but the caption and text identify it as flexural strength.

Main findings (with Table/Fig. location):
- FA/C 2.4 → 3.2 raised ε_tu by 78%; 3.2 → 4.4 lowered it by 10% and reduced stability (Table 5, p. 10; Conclusion 3, p. 15–16).
- First-crack strength falls with FA (3.67 → 3.26 MPa), σ_tp roughly constant 3.97–4.10 MPa (Table 5, p. 10).
- f'c falls 46.7 → 32.5 MPa and E 22.2 → 15.7 GPa as FA/C rises 2.4 → 4.4; peak compressive strain rises 0.52 → 0.69% (Fig. 8a–c, p. 11–12).
  E is fitted as **E = 490 f_c** (E and f_c in MPa; Fig. 8d, p. 12). E lower than ordinary concrete (no coarse aggregate) (§3.3.2, p. 11).
- FA3.2 strength gain: 7 d = 46.6% of 28 d; 90 d ≈ 12% above 28 d (text p. 11). Fig. 9 (p. 12): peaks ≈ 18.5 MPa (7 d), ≈ 40 MPa (28 d),
  ≈ 45 MPa (90 d), read from Fig. 9; strain at peak falls with age (≈ 0.70% → ≈ 0.61% → ≈ 0.55%, read from Fig. 9).
- Flexure (Fig. 14, p. 15): cracking strength falls nearly linearly with FA at 7 d (7.2 → 4.8 MPa) and less steeply at 90 d (9.6 → 8.2 MPa).
  Flexural strength highest for FA3.2 at 7 d (13.6 MPa). Text (p. 14) says FA3.2's 90-d flexural strength "was close to that of the FA2.8
  specimens and higher than others"; the figure labels give FA3.2 16.7 ≈ **FA2.4 16.8** > FA3.6 14.5 ≈ FA2.8 14.4 ⚠️ (text/figure mismatch inside the paper).
- Deflection grows with FA (7 d: 20.4 → 36.2 mm) and is smaller at 90 d than at 7 d for every mix (e.g. FA3.2 33.8 → 23 mm) (Fig. 14c, p. 15).
  Authors: no significant gain once FA replacement exceeds ≈ 76% (FA3.6–4.4 similar) (p. 14; Conclusion 5, p. 16). The text also cites an
  exception "FA3.2 at 28 days", although no 28-d bending data are shown (p. 14).
- Parametric model (Fig. 1, p. 4–5): σ0 and J′b/J_tip rise linearly with Vf; J′b/J_tip falls linearly with Gd, falls sharply then gently with τ0,
  and falls parabolically with Km.
- PSD (Fig. 3, p. 7): deviation from the A&A curve < 10% and flattens for FA/C > 2.4; minimum at S/B ≈ 0.4 (p. 6).

## Mechanisms / explanations offered by authors
- More FA lowers fiber/matrix bond (Gd, τ0) and matrix toughness Km, so the energy criterion is satisfied more easily → higher ε_tu (§3.2.2, p. 9).
- Too much FA reduces mix stability/uniformity → scatter and slightly lower ε_tu at FA4.4 (§3.2.2, p. 9).
- FA is mainly a filler early (slow pozzolanic reaction) → low 7-d strength, strong later gain (§3.3.2, p. 11).
- Flexural strength depends on matrix strength and on deformation capacity (longer hardening stage), so it does not fall monotonically with FA (§3.4.2, p. 14).
- Raising W/B and FA/C lowers bond and Km, but raising W/B costs strength, so water is controlled (§2.2, p. 4).
- PSD continuous grading improves packing and workability; FA fills the fine fraction (§2.3, p. 5–6).

## Limitations (stated + observed)
- Stated: low elastic modulus is a drawback for deflection control and seismic resistance; further work should raise E (§3.3.2, p. 11).
- Observed:
  - Only 3 of 6 mixes tested in tension; no crack width or crack count reported.
  - f'c, E, flexural values are given only as bar labels in figures; no standard deviations in numbers.
  - No measured micromechanical parameters on the HVFA matrix; model inputs are borrowed from Li 2002.
  - PSH thresholds quoted as J′b/J_tip > 3 and σ0/σfc > 1.45 (Kanda & Li 1998 [ref 28], as cited, p. 3), not computed for the actual mixes.
  - Tension at 28 d only; no long-term ageing of ε_tu despite slow FA reaction. Bending deflection drops from 7 to 90 d, which
    suggests ductility loss with age, but no 90-d tension test was run.
  - Fiber modulus unit error in Table 4 (MPa vs GPa).
  - Text/figure mismatch on 90-d flexural strength ranking (p. 14 vs Fig. 14b).

## Relation to other work
- Agrees with: [[yang2024-hshdc-uniaxial-tension]] (more FA → higher strain, lower first-crack strength); [[chai2023-hdc-ambient-temperature]] (highest-FA mix best ε_tu); FA lowers bond ([[fiber-matrix-interface]]).
- Contradicts: ⚔️ PSH strength threshold quoted as σ0/σfc > 1.45 for PVA (Kanda & Li 1998, "Multiple cracking sequence and saturation…", Concr. Res. Technol. JCI 9, as cited, p. 3), whereas the wiki records 1.2 (1998) and 1.3 (2006, fiber rupture) ([[kanda2006-psh-design-criteria]]).
- Extends: pushes FA/C to 4.4 (FA/B 81.5%), above M45 (FA/C 1.2, [[yang2008-ecc-fiber-bridging-law]]) and shows a ductility plateau/optimum at FA/C ≈ 3.2.

## Pages updated from this source
- [[fly-ash]] · [[pva-fiber]] · [[fiber-matrix-interface]] · [[tensile-strain-capacity]] · [[strain-hardening]]
- [[compressive-strength]] · [[flexural-strength]] · [[dogbone-uniaxial-tension]] · [[matrix-fracture-toughness]]
- [[mix-designs]] · [[mechanical-results]] · [[li2002-pva-ecc-interface-tailoring]] · [[yang2008-ecc-fiber-bridging-law]]

## To verify
- [x] f'c, E and peak compressive strain per mix — resolved 2026-10-21: bar labels in Fig. 8a–c (p. 11–12) of the PDF.
- [x] Flexural cracking strength, flexural strength and deflection per mix and age — resolved 2026-10-21: bar labels in Fig. 14 (p. 15); ages are 7 and 90 d only.
- [x] Whether Table 5 ε_tu is strain at peak stress or at end of test — partly resolved: Fig. 7 (p. 10) shows the drop immediately after peak, so ε_tu ≈ strain at peak; the paper itself does not define it.
- [ ] Table 4 fiber modulus "42.8 MPa" — PDF confirms the printed unit is MPa; assumed to mean GPa (typo in paper).
- [ ] PSH threshold σ0/σfc > 1.45 attributed to Kanda & Li 1998 (JCI Concr. Res. Technol. 9:19–33) — check against the original.
- [ ] Mass basis of S/B and W/B (implied by "kg" header and "by weight" in abstract); SP basis (kg per unit cement).
- [ ] Oil coating level of the REC-15 fibers (not stated in paper).
- [ ] 90-d flexural strength ranking: text (p. 14) vs Fig. 14b labels disagree; figure values used here.
