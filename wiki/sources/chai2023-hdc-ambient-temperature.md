---
type: source
slug: chai2023-hdc-ambient-temperature
title: "Effect of Ambient Temperature on the Mechanical Properties of High Ductility Concrete"
authors: [Lijuan Chai, Bo Chen, Liping Guo, Biaokun Ren, Zhichun Chen, Tianyong Huang]
year: 2023            # Materials 16(6), March 2023 issue; published online 20 Mar 2023 (received 22 Feb, revised 17 Mar, accepted 18 Mar 2023; p. 1)
venue: "Materials (MDPI) 16(6) (2023) 2465"
doi: "10.3390/ma16062465"
raw_file: raw/papers/Chai2023_HDC-ambient-temperature.pdf
material_term: "HDC (high ductility concrete), PVA-fiber, C40 design grade. The cited group work also uses 'HDCC' / 'ecological high ductility cementitious composites' (refs 6, 15, 20, 27–29). Defined per JC/T 2461-2018: ultimate tensile strain ≥ 0.50% and average crack width ≤ 200 µm (p. 1, Section 1, ref. 1; Fig. 1, p. 2)"
study_type: experimental
tags: [hdc, pva-fiber, fly-ash, normal-strength, temperature, low-temperature, sub-elevated-temperature, compression, uniaxial-tension, flexure, tensile-constitutive-model, pore-structure, mip, fiber-dispersion, bridge-deck-link-slab, southeast-university-group, taiyuan]
ingested: 2026-10-20
updated: 2026-10-21
---

# Ambient temperature (−30 to 60 °C) and PVA-HDC mechanics (Chai et al., 2023)

> Re-checked against the publisher PDF (19 pp.) on 2026-10-21: page numbers added, Fig. 18 values
> read off, every tabulated number confirmed.

## One-paragraph summary
The authors are from Taiyuan University of Technology, the Nanjing Hydraulic Research Institute and Southeast University
(the Guo Liping / Chen Bo group) (p. 1). They designed a **normal-strength PVA-fiber HDC** (C40 grade,
f_cu 48.0 MPa) for **bridge-deck link slabs**. After 28 d of standard curing they held the specimens
for **8 h at −30, 0, 20, 40 or 60 °C**, let them rest 1 h at 20 ± 2 °C, and then tested them
(Section 2.3.3, p. 5).

The mix was chosen from four candidates. HDC-1 has the highest fly-ash share (W/B 0.30 and FA/C 0.88
by mass, both computed here from Table 1, p. 3) and the highest ultimate tensile strain, 1.15% (Table 4, p. 6).

Results relative to 20 °C:
- **Strength:** compressive, tensile and flexural strength fall after −30 and 0 °C and rise after
  40 and 60 °C (Table 5, p. 8; Table 6, p. 10; Table 8, p. 14).
- **Deformation:** ultimate tensile strain and ultimate deflection rise at **both** low and high
  temperatures. The largest gains are at 0 °C: ε_tu 1.46% and deflection 5.01 mm.
- **Behaviour:** every condition kept multiple cracking and strain or deflection hardening
  (Figs. 11–12, p. 10; Figs. 15–16, pp. 13–14).
- **Model:** the authors propose a bilinear (two-stage) tensile model and fit it at each temperature
  (Eqs. 2–3, p. 12; Table 7, p. 13).
- **Pores:** MIP shows that harmful pores (> 50 nm) turn into finer pores as temperature rises
  (Fig. 18, p. 16).

> Synthesis: this is the wiki's **first primary study of a normal-strength (about 48 MPa)
> Chinese "high ductility concrete" made with PVA fiber**. The other Chinese primary sources are
> HSHDC (Xi'an [[yang2024-hshdc-uniaxial-tension]]; GDUT [[su2023-rubber-modified-hshdc]]) or PE-UHDC
> (Tongji [[ye2021-uhdc-flexural-size-effect]]). The lineage is **Southeast University / Taiyuan**
> ("ecological HDCC"), **not** the Xi'an Deng group.

## Objective / research question
- How does a short exposure (8 h) to regional ambient temperatures in China (−30 °C in the
  north-east, 0 °C in the centre, up to 60 °C deck temperature in the south) change the compressive,
  tensile and flexural properties of PVA-HDC (Section 1, p. 2)?
- Which design parameters should be used for HDC bridge-deck link slabs (Section 3.3.3, p. 9;
  Section 3.4.5, p. 13; Section 3.5.3, p. 15)?
- The authors state that PVA-HDC between −30 and 60 °C is "rarely reported" (Section 1, p. 3).

## Materials & mix design
Constituents (Section 2.1, p. 3):
- **Cement:** P.II 42.5R.
- **Fly ash:** Class II.
- **Sand:** river sand, maximum size 1.18 mm, fineness modulus 1.68, "particle density" 1605 kg/m³ ⚠️
  (this looks like a bulk density).
- **Superplasticizer:** powdered polycarboxylate (PS).
- **Water:** tap water.
- **Fiber:** domestic PVA, L 12 mm, d 39 µm, E 30 GPa, elongation 5–8%, tensile strength 1250 MPa
  (ref. 15). No oil coating or surface treatment is reported.

| Mix ID | Cement | Fly ash | Slag/other | Sand (type, max size) | W/B | SP | Fiber type | L (mm) | d (µm) | Vf (vol.%) |
|---|---|---|---|---|---|---|---|---|---|---|
| **HDC-1** (selected) | 680 | 600 | none | 384, river sand, 1.18 mm | 0.300 (384/1280, computed) | 1.01 | PVA (domestic) | 12 | 39 | 26 kg/m³; vol.% not reported ⚠️ |
| HDC-2 | 768 | 512 | none | 384, same | 0.310 (397/1280, computed) | 1.54 | same | 12 | 39 | 26 kg/m³ |
| HDC-3 | 768 | 512 | none | 384, same | 0.252 (323/1280, computed) | 1.31 | same | 12 | 39 | 26 kg/m³ |
| HDC-4 | 768 | 512 | none | 384, same | 0.198 (253/1280, computed) | 1.92 | same | 12 | 39 | 26 kg/m³ |

Units of binder quantities: kg/m³ (Table 1, p. 3).

Ratios computed here (by mass) from Table 1:
- HDC-1: FA/C 0.88, FA 46.9% of binder, sand/binder 0.30.
- HDC-2 to HDC-4: FA/C 0.67 (40% FA).
- PVA fiber density is not given, so vol.% is **not converted**. If ρ were 1.30 g/cm³ (the value
  for another PVA in [[yang2024-hshdc-uniaxial-tension]], Table 3), 26 kg/m³ would be about 2.0 vol.%
  ⚠️ unverified.

Mixing (Section 2.2, p. 3; Fig. 3, p. 4), in a 60 L mixer:
1. dry solids (cement, FA, powdered SP, sand) for 90 s;
2. water added, then 240 s;
3. fibers added, then 120 s.

Curing: under plastic film at 20 ± 2 °C for 1 d, then 27 d at 20 ± 2 °C (p. 3). The humidity is not stated ⚠️.

## Test methods
- **Specimen geometry** (Table 2, p. 4; Table 3, p. 5; per JC/T 2461-2018):
  - 100 mm cubes (n = 3);
  - 100 × 100 × 300 mm prisms for axial compression (n = 3);
  - dogbones with a 13 × 30 × 100 mm pure-tension zone (n = 6);
  - thin plates 15 × 75 × 300 mm for flexure (n = 3). The span is not stated in the text. The photo
    in Fig. 6b (p. 6) shows **four-point bending** (two loading rollers, two supports); the scales in the
    photo suggest loading points ≈ 80 mm apart on a span of ≈ 240 mm (read from Fig. 6b photo,
    tentative ⚠️).
- **Loading and rate:**
  - cubes: load control at 0.5 MPa/s (p. 4);
  - prisms: displacement control at 0.3 mm/min (p. 5);
  - tension: MTS-810, displacement control at 0.2 mm/min (p. 4);
  - flexure: INSTRON 8802 at 0.2 mm/min (p. 5).
- **Measurement:**
  - tension: LVDT over the central 100 mm gauge (Fig. 4, p. 4);
  - compression: BX120-50AA strain gauges in the middle third, giving E and ν (p. 5);
  - flexure: mid-span deflection by LVDT (p. 5);
  - pores: MIP (Autopore IV 9510) (Section 2.3.4, p. 6);
  - fiber dispersion: a 13 × 30 × 10 mm slice cut from the centre of a tensile specimen, sprayed with
    fluorescent liquid, 60 images per specimen under UV light; α by Eq. 1 (Section 2.3.2, pp. 4–5; Eq. 1, p. 7).
- **Temperature treatment:** 8 h at a constant −30 / 0 / 20 / 40 / 60 °C after 28 d of curing, then
  1 h at 20 ± 2 °C before testing (p. 5).
  - This is a **residual (post-exposure) test, not an in-situ hot or cold test**.
  - The abstract and Section 1 call it "curing at" these temperatures (p. 3), but the method is an 8 h exposure.
  - The moisture state during exposure is not reported ⚠️.
- **Curing and test age:** 28 d standard curing, then exposure. Testing is at about 28 d plus 9 h.
- **Definition of ultimate tensile strain:** strain at **peak tensile stress**. Fig. 1 (p. 2) marks the
  "ultimate tensile strain" at the peak of the hardening curve, and in Fig. 7 (p. 6) the HDC-2 and HDC-4
  curves peak at ≈ 0.65% and ≈ 0.40% (read from Fig. 7), matching their Table 4 values (0.64%, 0.42%).

→ [[dogbone-uniaxial-tension]] · [[compressive-strength]] · [[flexural-strength]]

## Key results
Mix screening at 28 d and 20 °C (Table 4, p. 6):

| Mix ID | f'c (MPa) | First-crack stress (MPa) | Tensile strength (MPa) | Tensile strain capacity (%) | Crack width (µm) | Other |
|---|---|---|---|---|---|---|
| HDC-1 | 48.0 ± 0.99 (100 mm cube) | not reported | 4.23 ± 0.09 | 1.15 ± 0.05 (at peak stress) | not reported | selected mix |
| HDC-2 | 47.8 ± 2.4 | not reported | 4.47 ± 0.15 | 0.64 ± 0.07 | not reported | — |
| HDC-3 | 50.2 ± 3.2 | not reported | 4.22 ± 0.23 | 0.55 ± 0.04 | not reported | — |
| HDC-4 | 59.0 ± 1.9 | not reported | 4.83 ± 0.17 | 0.42 ± 0.05 | not reported | — |

HDC-1 after 8 h exposure, tested about 1 h after returning to 20 °C (Table 5, p. 8; Table 6, p. 10;
Table 7, p. 13; Table 8, p. 14). σ_ntc is the nominal first-crack stress of the bilinear model (Table 7).
It is not a measured first-crack stress.

| Mix ID | f'c (MPa) | First-crack stress (MPa) | Tensile strength (MPa) | Tensile strain capacity (%) | Crack width (µm) | Other |
|---|---|---|---|---|---|---|
| HDC-1 @ −30 °C | f_cu 46.7 ± 1.02 (−2.71%); f_c prism 42.0 ± 1.11 | σ_ntc 2.79 | 3.74 ± 0.08 (−11.58%) | 1.34 ± 0.06 (+16.52%) | not reported | E_c 23.2 GPa; f_flex 12.23 MPa; δ_u 4.75 mm; strain energy 4.42 ⚠️; E_abs 3.45 J |
| HDC-1 @ 0 °C | 47.1 ± 1.13 (−1.88%); 42.5 ± 1.23 | 1.56 | 3.99 ± 0.10 (−5.67%) | **1.46 ± 0.08 (+26.96%)** | not reported | 23.5 GPa; 13.08 MPa; **5.01 mm**; 4.76; 3.95 J |
| HDC-1 @ 20 °C (ref.) | 48.0 ± 0.99; 43.1 ± 0.98 | 2.86 | 4.23 ± 0.09 | 1.15 ± 0.05 | not reported | 23.8 GPa; 14.08 MPa; 3.55 mm; 4.14; 2.75 J |
| HDC-1 @ 40 °C | 50.9 ± 1.15 (+6.04%); 45.7 ± 1.18 | 3.28 | 4.46 ± 0.08 (+5.44%) | 1.23 ± 0.07 (+6.96%) | not reported | 24.0 GPa; 14.65 MPa; 3.82 mm; 4.76; 3.25 J |
| HDC-1 @ 60 °C | **52.7 ± 1.19 (+9.79%)**; 47.6 ± 1.32 | 2.92 | **4.80 ± 0.09 (+13.48%)** | 1.31 ± 0.06 (+13.91%) | not reported | 24.1 GPa; **15.64 MPa**; 4.19 mm; 5.14; 3.52 J |

How to read the table:
- f_cu is the 100 mm cube strength; f_c is the 100 × 100 × 300 mm prism strength.
- Percentages are changes relative to 20 °C, as printed in the tables.
- Strain energy is in "J/m³ × 10⁶" as printed (Table 6, p. 10) ⚠️; see "To verify".
- Flexural values (f_flex, ultimate deflection δ_u, energy absorption E_abs) are from Table 8 (p. 14).

Bilinear model parameters (Table 7, p. 13):

| T (°C) | E_tc (MPa) | R² | E_tu (MPa) | R² | σ_ntc (MPa) | ε_ntc (%) |
|---|---|---|---|---|---|---|
| −30 | 11.16 × 10³ | 0.94 | 79.91 | 0.94 | 2.79 | 0.025 |
| 0 | 16.76 × 10³ | 0.98 | 69.55 | 0.84 | 1.56 | 0.014 ⚠️ |
| 20 | 10.21 × 10³ | 0.99 | 60.70 | 0.81 | 2.86 | 0.028 |
| 40 | 15.62 × 10³ | 0.99 | 57.82 | 0.80 | 3.28 | 0.021 |
| 60 | 13.89 × 10³ | 0.99 | 95.43 | 0.88 | 2.92 | 0.021 |

Flexural ultimate load (kN), Table 8 (p. 14): −30 °C 0.86, 0 °C 0.92, 20 °C 0.99, 40 °C 1.03, 60 °C 1.10.

MIP results (Fig. 18, p. 16):

| T (°C) | Total intrusion (mL/g) ≈ | < 20 nm (%) ≈ | 20–50 nm (%) ≈ | 50–200 nm (%) ≈ | > 200 nm (%) ≈ | Critical pore size (nm) | Most probable pore size (nm) |
|---|---|---|---|---|---|---|---|
| −30 | 0.28 | 4.7 | 18.4 | 16.4 | 60.3 | ≈ 62.4 ("no significant change") | 50.3 |
| 0 | 0.30 | 9.9 | 18.6 | 12.9 | 58.5 | ≈ 62.4 | 50.3 |
| 20 | 0.26 | 14.2 | 20.5 | 14.0 | 51.2 | 62.4 | 50.3 |
| 40 | 0.26 | 18.5 | 19.3 | 12.5 | 49.4 | ≈ 62.4 | 50.3 |
| 60 | 0.24 | 18.7 | 30.8 | 5.0 | 45.3 | 50.3 | 40.3 |

- Total intrusion is read from Fig. 18a; pore-class values from Fig. 18c; pore sizes are stated in the text (p. 16).
- The Fig. 18c axis is labelled "Porosity /%", but each temperature's four classes sum to ≈ 100%,
  so the bars are **shares of total intruded pore volume**, not porosity of the specimen (observed here).
- The trend is not strictly monotonic: 20–50 nm at 40 °C (≈ 19.3%) is below 20 °C (≈ 20.5%), and
  total intrusion is highest at 0 °C, not −30 °C (read from Fig. 18).

Main findings (with location):
- **Mix screening:**
  - HDC-1, with the most fly ash, gave the highest ε_tu (1.15%) and the authors ranked it best
    overall (Table 4, p. 6; Section 3.1, pp. 6–7).
  - Across HDC-2 → HDC-4 (W/B falling from 0.31 to 0.20, computed), f_cu rose from 47.8 to 59.0 MPa
    while ε_tu fell from 0.64 to 0.42% (Table 4, p. 6).
  - HDC-1 and HDC-2 differ in both FA and water, so the FA effect is confounded (observed here).
  - The authors write that HDC-1 has "the best compressive and tensile performance" (p. 6), although
    its f_cu and σ_tu are the lowest or near-lowest of the four in Table 4 (observed here).
- **Fiber dispersion:** α = 0.91 for HDC-1. The authors credit FA (higher ζ-potential) and the 1.18 mm
  maximum sand size (Section 3.2, Fig. 8, Eq. 1, p. 7).
- **Compression** (Table 5, p. 8; Fig. 10, p. 9):
  - Changes are small: −2.7% at −30 °C and +9.8% at 60 °C (cube).
  - E_c is 23.2–24.1 GPa.
  - ν = 0.23 and f_c/f_cu = 0.90 at every temperature. The 0.90 ratio compares with 0.76 for
    ordinary concrete (GB 50010, ref. 26) (p. 9). The authors attribute this to the absence of coarse aggregate.
  - Failure was a single main diagonal crack through the section in every case (Fig. 9, pp. 7–8).
  - Design advice: ignore the temperature effect on compression and use the 20 °C values. The
    authors give the reduction as "less than 3%" (Section 3.3.3, p. 9).
- **Tension** (Table 6, p. 10; Table 7, p. 13; Figs. 11–13, pp. 10–11):
  - Multiple cracking and strain hardening occurred at every temperature.
  - From 0 to 60 °C the hardening branch shows strong "down–up–down" stress oscillation; at −30 °C it
    is smooth (Fig. 12, Section 3.4.2, p. 10).
  - σ_tu ranged from 3.74 to 4.80 MPa, rising monotonically with temperature.
  - ε_tu rose relative to 20 °C at **every** other temperature, with a maximum at 0 °C (Table 6, p. 10).
  - Strain energy is largest at 60 °C (p. 12).
- **Flexure** (Table 8, Fig. 16, p. 14; Figs. 15, 17, pp. 13, 15):
  - Multiple cracking and deflection hardening at every temperature.
  - Flexural strength ranged from 12.23 to 15.64 MPa, rising with temperature.
  - Ultimate deflection and energy absorption rose at every non-reference temperature, with the
    maximum at 0 °C (5.01 mm, 3.95 J).
  - Flexure therefore mirrors tension.
- **Pore structure** (Fig. 18, p. 16; values in the MIP table above):
  - Critical pore size was 62.4 nm at 20 °C, about unchanged at −30, 0 and 40 °C, and 50.3 nm at 60 °C.
  - The most probable pore size was 50.3 nm, falling to 40.3 nm at 60 °C.
  - As temperature rises, the share of pores < 20 nm and 20–50 nm rises and that of pores
    50–200 nm and > 200 nm falls (Fig. 18c; classes from ref. 34). Pores > 200 nm fall from ≈ 60% at −30 °C
    to ≈ 45% at 60 °C (read from Fig. 18c).
- **Design parameters:** use the bilinear tensile model with temperature-specific parameters
  (Table 7, Section 3.4.5, p. 13). Temperature effects on flexure must also be considered (Section 3.5.3, p. 15).

## Mechanisms / explanations offered by authors
- **Low temperature lowers strength:**
  - freezing water slows hydration and enlarges large pores, loosening the matrix (Section 3.3.2, p. 8, ref. 12);
  - at −30 °C, internal damage also lowers matrix and fiber strength, which removes the
    stress oscillation (Section 3.4.2, p. 11).
- **High temperature raises strength:** 40–60 °C speeds the hydration of unhydrated cement and FA
  and densifies the pore structure (Section 3.3.2, p. 8; Section 3.6, p. 16; refs. 24–25, 35).
- **Ductility rises at both ends:**
  - after low- or high-temperature treatment, the **chemical bond** at the fiber/matrix interface
    falls and **frictional stress** rises;
  - both favour fiber pull-out and raise bridging capacity, and ductility depends more on bridging
    than strength does;
  - the chemical bond falls most at 0 °C, which explains the largest ε_tu there (Section 3.4.3, pp. 11–12).
  - These interface claims rest on a master's thesis (ref. 29, Yang Y.N. 2017) and are **not measured
    in this paper** (no single-fiber pull-out test). → [[fiber-matrix-interface]]
- **Fly ash** lowers matrix toughness and interfacial bond, so more fibers pull out and
  saturated strain hardening follows ("traditional HDC design theory", Section 3.1, p. 7).
  → [[fly-ash]], [[strain-hardening]]
- They also state that PVA fiber strength falls after both 40–60 °C and 0 °C treatment
  (Section 3.4.2, p. 11). No fiber test supports this ⚠️.

## Limitations (stated + observed)
- **Stated:**
  - only 8 h of exposure;
  - longer exposure representing years of service is left for future work (Section 3.6, pp. 16–17).
- **Observed (exposure):**
  - Testing is residual, about 1 h after returning to 20 °C. Specimen core temperature at test is
    not reported, so these are **not** in-situ properties at −30 or 60 °C.
  - Moisture condition and cooling/heating rates are not reported.
  - There is no freeze–thaw cycling; a single exposure at −30 °C is not frost durability.
- **Observed (mechanism):**
  - The interface mechanism is asserted from earlier work, with no pull-out or SEM evidence here.
  - A 9.8% strength gain from 8 h at 60 °C attributed to extra hydration is plausible but untested.
    Drying could also contribute (observed here, not in the source).
- **Observed (data reporting):**
  - Crack width and crack number are not reported, although the HDC definition requires ≤ 200 µm.
  - Fiber vol.% is not given.
  - The flexural span is not given in the text (only the Fig. 6b photo).
  - Table 8 (p. 14) lists identical ± values for ultimate load and flexural strength, which suggests copied
    standard deviations ⚠️.
  - Strain-energy units appear inconsistent with the stress–strain values ⚠️.
  - MIP bars in Fig. 18c are labelled "porosity" but are pore-volume shares (observed here).
- **Observed (statistics):**
  - n = 3–6 per group.
  - The representative curves were chosen as those closest to the mean ε_tu (p. 6, p. 10) or mean
    deflection (p. 14).

## Relation to other work
- **Agrees with:**
  - Yu J. et al. 2015 (ref. 10): PVA/HVFA-ECC σ_tu and ε_tu rise after 50–100 °C (1 h exposure, p. 2). Also cited in
    [[ma2021-ecc-durability-review]] and [[high-temperature-behaviour]].
  - Li L.L. et al. 2023 (ref. 12): f_cu and splitting tensile strength rise with curing temperature
    (−20, 15, 20 °C; p. 3).
- **Contradicts** ⚔️ (different fiber, so a probable fiber effect rather than a true conflict):
  - Dong et al. 2022 (ref. 11), PE-HDC tested at −20 to 90 °C (p. 2): f'c, peak compressive strain and σ_tu **fell** as temperature
    rose, while ε_tu rose. Here (PVA) σ_tu and f_cu **rose** from 20 to 60 °C.
  - Dong et al. also report monotonic ε_tu growth with temperature. Here ε_tu peaks at 0 °C and is
    non-monotonic. The test modes probably differ ("performed compressive and tensile tests at" these
    temperatures, i.e. probably in-situ ⚠️).
- **Extends:**
  - First sub-zero (−30, 0 °C) residual data in the wiki. → [[high-temperature-behaviour]]
  - First normal-strength PVA-HDC primary data in the wiki. ε_tu is 1.15%, well below the 4.88% of the
    oil-coated Michigan PVA-ECC ([[li2002-pva-ecc-interface-tailoring]]) and well above the 0.23–0.30%
    of PVA in the Xi'an HSHDC matrix ([[yang2024-hshdc-uniaxial-tension]]). → [[pva-fiber]]
  - Gives a Chinese standard definition of HDC (JC/T 2461-2018: ε_tu ≥ 0.50%, crack width ≤ 200 µm; p. 1).
    → [[terminology-hdc-ecc-shcc]]
  - Bridge-deck link slab application, following Lepech & Li 2009 (ref. 5).

## Pages updated from this source
- [[high-temperature-behaviour]] · [[compressive-strength]] · [[tensile-strain-capacity]] · [[flexural-strength]]
- [[pva-fiber]] · [[fly-ash]] · [[fiber-dispersion]] · [[fiber-matrix-interface]] · [[water-binder-ratio]]
- [[tensile-constitutive-model]] · [[multiple-cracking]] · [[strain-hardening]] · [[dogbone-uniaxial-tension]]
- [[terminology-hdc-ecc-shcc]] · [[durability]] · [[mix-designs]] · [[mechanical-results]] · [[gaps]]

## To verify
- [ ] **Strain-energy units (Table 6, p. 10).** The PDF prints 4.14 "J/m³ × 10⁶" at 20 °C. The area under
  the 20 °C curve in Fig. 12 (about 3.7 MPa × 1.15%) is about 0.04 × 10⁶ J/m³. The printed value matches
  stress (MPa) × strain in **%**, so the true value is probably about 100× smaller. 0 °C and 40 °C both
  read 4.76. Confirmed as printed in the PDF; still unresolved.
- [ ] **ε_ntc at 0 °C (Table 7, p. 13).** σ_ntc/E_tc = 1.56/16 760 = 0.0093%, not the 0.014% printed
  (PDF value confirmed). The other rows are self-consistent (computed here).
- [ ] **Table 8 standard deviations (p. 14).** Ultimate load and flexural strength carry identical ± values
  (e.g. 0.86 ± 0.32 kN vs 12.23 ± 0.32 MPa) in the PDF too. For the load, ± 0.32 kN would be a CV of about 37%,
  which is implausible.
- [ ] **Flexural span.** Four-point bending is confirmed by the Fig. 6b photo (p. 6); the span ≈ 240 mm with
  loading points ≈ 80 mm apart is read from the photo scales only. Back-calculating with f = PL/(bh²)
  also gives L ≈ 240 mm (computed here, assumes third-point loading).
- [ ] **PVA dosage.** Fiber density and vol.% (26 kg/m³ is about 2.0 vol.% only if ρ = 1.30 g/cm³). Not in the PDF.
- [ ] **PVA product.** Is the domestic fiber oil-coated? The manufacturer is not named in the PDF.
- [ ] **Sand "particle density" of 1605 kg/m³ (p. 3).** Bulk density?

Resolved on 2026-10-21 (PDF check):
- [x] **Definition of "ultimate tensile strain"** — strain at peak stress: Fig. 1 (p. 2) marks it at the
  curve peak, and Fig. 7 (p. 6) peaks for HDC-2/HDC-4 (≈ 0.65%, ≈ 0.40%) match Table 4.
- [x] **Abstract wording** — the abstract (p. 1) says strength "decreased after treatment at low
  temperatures"; Section 3.3.3 (p. 9) gives "< 3%" for compression, consistent with −2.71% (Table 5, p. 8). No conflict.
- [x] **Fig. 18c porosity values** — read from the figure (MIP table above); they are pore-volume shares.
