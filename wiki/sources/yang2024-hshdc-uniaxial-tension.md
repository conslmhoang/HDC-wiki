---
type: source
slug: yang2024-hshdc-uniaxial-tension
title: "Uniaxial tensile test of high-strength high-ductility concrete (HSHDC): Mechanical response and toughness evaluation"
authors: [Jiasheng Yang, Mingke Deng, Yitong Wang, Yangxi Zhang]
year: 2024
venue: "Journal of Building Engineering 89 (2024) 109332"
doi: "10.1016/j.jobe.2024.109332"
raw_file: raw/papers/Yang2024_Uniaxial tensile test of high-strength high-ductility concrete.pdf
material_term: "HSHDC (high-strength high-ductility concrete); HDC = high-ductility concrete, classed by the authors as SHCC; once 'UHDC' (p. 8, apparent typo)"
study_type: experimental
tags: [hshdc, pe-fiber, pva-fiber, uniaxial-tension, dogbone, fly-ash, water-binder-ratio, fiber-diameter, fiber-content, tensile-toughness, constitutive-model, standard-curing, xi-an-group]
ingested: 2026-10-06
updated: 2026-10-06
---

# HSHDC uniaxial tension and tensile toughness (Yang et al., 2024)

## One-paragraph summary
The group at Xi'an University of Architecture & Technology (Deng Mingke) tested 13 groups of
"HSHDC" thin plates (JSCE dogbone, 3 specimens per group) in uniaxial tension. Matrices were
standard-cured at 20 ± 2 °C, with **no heat curing**. The variables were fiber type (PE vs PVA),
PE content (1.5 / 2.0 / 2.5 vol.%), PE diameter (22 / 30 / 35 / 40 µm, L = 12 mm),
W/B (0.14 / 0.16 / 0.18) and fly ash share of the binder (15 / 20 / 25%).

Results:
- PE22-based mixes reached peak (tensile strain capacity at peak stress) strains of 3.6–6.5% and
  peak stresses of 5.7–7.7 MPa (28 d).
- PVA39 mixes reached only 0.23–0.30% and 4.8–5.5 MPa (Table 6).
- The tensile E1 was 33.4–46.8 GPa.
- Optimum W/B was 0.16. More fly ash raised strain and lowered σcr.

The authors also propose:
- a trilinear tensile constitutive model (Eq. 1);
- a uniaxial tensile toughness evaluation method with three indices, σe,0.85, gp and Ipost
  (Eqs. 4–6, Table 7). The maximum gp was 366.44 kJ/m³.

Matrix-only compressive strength at 60 d was about 108–110 MPa (Table 4). The 28-d cube strength
of PVA-HSHDC was 91.6–96.4 MPa (Table 5). This "HSHDC" is therefore much less strong in
compression and tension than the Michigan HSHDC (166 MPa, 14.5 MPa, as quoted in [[ranade2017-hshdc-impact-resistance]], p. 26).

## Objective / research question
- Quantify the effect of five variables on the tensile stress–strain curve, strength and strain of
  HSHDC under standard (ambient) curing:
  - fiber type (PE vs PVA)
  - PE fiber content
  - PE fiber diameter (aspect ratio)
  - W/B
  - fly ash content
- Propose a tensile toughness evaluation method based on the uniaxial tension test. Existing
  toughness indices (ASTM C1018, JSCE-SF4, ASTM C1609, etc.) are flexural only (p. 2, p. 12).

## Materials & mix design
Binder fractions are mass fractions of the total binder (b). Sand, water, SP and DA are mass
ratios to binder (Table 4).

| Mix ID | Cement | Fly ash | Slag/other | Sand (type, max size) | W/B | SP | Fiber type | L (mm) | d (µm) | Vf (vol.%) |
|---|---|---|---|---|---|---|---|---|---|---|
| M1-0.16-PE22–1.5 | 0.70 b (P·O 52.5R) | 0.15 b (Class F) | SF 0.15 b; DA 3.0% b | graded quartz sand, s/b 0.36, max 0.5 mm | 0.16 | 2.0% b | PE | 12 | 22 | 1.5 |
| M1-0.16-PE22–2.0 | 0.70 | 0.15 | SF 0.15 | same | 0.16 | 2.0% | PE | 12 | 22 | 2.0 |
| M1-0.16-PE22–2.5 | 0.70 | 0.15 | SF 0.15 | same | 0.16 | 2.0% | PE | 12 | 22 | 2.5 |
| M1-0.16-PE30–2.0 | 0.70 | 0.15 | SF 0.15 | same | 0.16 | 2.0% | PE | 12 | 30 | 2.0 |
| M1-0.16-PE35–2.0 | 0.70 | 0.15 | SF 0.15 | same | 0.16 | 2.0% | PE | 12 | 35 | 2.0 |
| M1-0.16-PE40–2.0 | 0.70 | 0.15 | SF 0.15 | same | 0.16 | 2.0% | PE | 12 | 40 | 2.0 |
| M1-0.14-PE22–2.0 | 0.70 | 0.15 | SF 0.15 | same | 0.14 | 2.0% ⚠️ | PE | 12 | 22 | 2.0 |
| M1-0.18-PE22–2.0 | 0.70 | 0.15 | SF 0.15 | same | 0.18 | 2.0% ⚠️ | PE | 12 | 22 | 2.0 |
| M1-0.16-PVA39–2.0 | 0.70 | 0.15 | SF 0.15 | same | 0.16 | 2.0% | PVA | 12 | 39 | 2.0 |
| M2-0.16-PE22–2.0 | 0.65 | 0.20 | SF 0.15 | same | 0.16 | 2.0% | PE | 12 | 22 | 2.0 |
| M2-0.16-PVA39–2.0 | 0.65 | 0.20 | SF 0.15 | same | 0.16 | 2.0% | PVA | 12 | 39 | 2.0 |
| M3-0.16-PE22–2.0 | 0.60 | 0.25 | SF 0.15 | same | 0.16 | 2.0% | PE | 12 | 22 | 2.0 |
| M3-0.16-PVA39–2.0 | 0.60 | 0.25 | SF 0.15 | same | 0.16 | 2.0% | PVA | 12 | 39 | 2.0 |

Units of binder quantities: mass fraction of total binder (OPC + SF + FA = 1), with
s/b, w/b, SP/b and DA/b as mass ratios (Table 4). No kg/m³ values are reported. Table 4 tabulates
only W/B = 0.16. The 0.14 and 0.18 mixes come from Table 1, and their SP dosage is not stated
separately (⚠️).

Constituents (Section 2.2, Tables 2–3, p. 3–5):
- **Cement:** P·O 52.5R OPC (GB 175-2020), density 3.12 g/cm³.
- **Silica fume:** mean size about 0.1 µm; specific surface 20,000–28,000 m²/kg; SiO₂ 95.80%;
  density 1.70 g/cm³.
- **Fly ash:** Class F; 16% residue on the 5 µm sieve; activity index 92%; density 1.12 g/cm³
  (as printed, ⚠️ low for FA).
- **Admixtures:** polycarboxylate SP (40% water reduction) and a defoaming agent (DA).
- **Fibers** (Wuhe Civil Engineering New Materials Co., Ltd.), all 12 mm long:

| Fiber | d (µm) | Aspect ratio | σ_f (MPa) | E_f (GPa) | Elongation (%) | Density (g/cm³) |
|---|---|---|---|---|---|---|
| PE22 | 22 | 545 | 2300 | 90 | 2.9 | 0.97 |
| PE30 | 30 | 400 | 2300 | 90 | 2.9 | 0.97 |
| PE35 | 35 | 343 | 2300 | 90 | 2.9 | 0.97 |
| PE40 | 40 | 300 | 2300 | 90 | 2.9 | 0.97 |
| PVA39 | 39 | 308 | 1600 | 40 | 7 | 1.30 |

- **Matrix design:** closest packing theory plus least squares, set by trial tests (p. 4).
- **Matrix apparent density / 60-d matrix compressive strength:** M1 2.31 g/cm³ / 110.3 MPa;
  M2 2.26 / 107.5; M3 2.24 / 108.2 (Table 4).

## Test methods
- **Specimen geometry:** JSCE-recommended dogbone thin plate (Fig. 1a).
  - Total length 350 mm (100 + 150 + 100). Gauge length 150 mm.
  - Gauge section 50 mm wide × 15 mm thick (A = 750 mm²). Grip ends 80 mm wide (15 + 50 + 15).
  - Side-view dimensions are 55 / 5 / 230 / 5 / 55 mm.
  - Grip ends are reinforced with 50 mm × 100 mm carbon fiber cloth to avoid failure outside the
    gauge (p. 3).
  - 3 specimens per group (p. 2).
- **Gripping / boundary:**
  - Wedge-type upper and lower grips on the carbon-cloth ends. The lower grip is connected to a
    rigid base (Fig. 1b).
  - The rotational restraint (fixed vs pinned) is not stated (⚠️).
- **Loading / rate:**
  - MTS universal testing machine, 100 kN.
  - Displacement control at 0.2 mm/min, which is about 2.2 × 10⁻⁵ s⁻¹ over the 150 mm gauge
    (my conversion, not stated).
- **Measurement:**
  - One U-shaped clip-on extensometer at mid-specimen over the 150 mm gauge length (p. 3, p. 4).
  - σ = F/A with A = 15 × 50 mm. ε = l/L with L = 150 mm.
  - No LVDT, DIC or crack-width measurement.
- **Other tests (PVA-HSHDC only, Table 5):**
  - f_c on 100 mm cubes at 7, 28 and 60 d.
  - Three-point (f_f) and four-point (f_b) bending on 40 × 40 × 160 mm prisms. Equivalent bending
    toughness W_e^u from the four-point load–deflection curve (per ref. [19], printed as "DBJ 60/T 112–2021").
  - Standards cited: ASTM C1609 and JC/T 2461-2018 (p. 4).
- **Microscopy:** SEM of M3-0.16-PE22–2.0 after tension (Fig. 11).
- **Curing & test age:**
  - Plastic film at room temperature for 24 h, then demoulding.
  - Standard curing room at 20 ± 2 °C and 95% RH for 28 d (p. 4, Fig. 2).
  - Tension tested at 28 d.
- **Mixing:** 5 L planetary mixer. Dry materials 1 min, then water + SP 2 min, then fibers
  "manually dispersed" and mixed 3 min. Cast, then 60 s on a shaking table (Fig. 2, p. 4).

→ [[dogbone-uniaxial-tension]]

## Key results
28 d, n = 3 per group. COV (%) in parentheses (Table 6). Tensile strain = εp, the strain at peak
stress. f'c was not measured for the PE mixes.

| Mix ID | f'c (MPa) | First-crack stress (MPa) | Tensile strength (MPa) | Tensile strain capacity (%) | Crack width (µm) | Other |
|---|---|---|---|---|---|---|
| M1-0.16-PE22–1.5 | not reported | 3.06 (6.22) | 6.06 (0.52) | 3.561 (3.69) | not reported | E1 34.8 GPa; εcr 0.039%; εp/εcr 91.31; σp/σcr 1.98; σe,0.85 4.97 MPa; gp 173.17 kJ/m³; Ipost 0.165 |
| M1-0.16-PE22–2.0 | not reported | 3.52 (4.36) | 6.99 (12.97) | 3.839 (10.55) | not reported | E1 43.8; εcr 0.016; 232.89; 1.99; 5.78; 219.05; 0.156 |
| M1-0.16-PE22–2.5 | not reported | 3.96 (14.94) | 7.69 (5.62) | 4.647 (4.30) | not reported | E1 45.1; εcr 0.021; 221.29; 2.18; 6.55; 303.48; 0.149 |
| M1-0.16-PE30–2.0 | not reported | 3.60 (14.29) | 6.73 (0.65) | 3.156 (7.65) | not reported | E1 40.9; εcr 0.023; 137.22; 1.87; 5.35; 165.73; 0.095 |
| M1-0.16-PE35–2.0 | not reported | 3.36 (6.29) | 5.11 (4.75) | 2.294 (5.62) | not reported | E1 33.4; εcr 0.036; 63.72; 1.52; 4.26; 96.35; 0.131 |
| M1-0.16-PE40–2.0 | not reported | 3.15 (19.71) | 4.52 (7.82) | 0.345 (2.94) | not reported | E1 43.5; εcr 0.016; 21.56; 1.43; 4.10; 15.00; 0.459 |
| M1-0.14-PE22–2.0 | not reported | 3.58 (5.73) | 5.94 (2.23) | 0.811 (13.78) | not reported | E1 46.8; εcr 0.011; 73.73; 1.66; 5.06; 33.17; 0.083 |
| M1-0.18-PE22–2.0 | not reported | 3.09 (7.36) | 5.72 (4.45) | 1.888 (17.99) | not reported | E1 35.4; εcr 0.046; 41.04; 1.85; 4.83; 71.05; 0.286 |
| M1-0.16-PVA39–2.0 | 96.4 (28 d cube; 85.9 / 114.5 at 7 / 60 d) | 3.53 (9.14) | 4.78 (6.13) | 0.228 (8.42) | not reported | E1 39.2; εcr 0.021; 10.86; 1.35; 4.08; 9.26; 0.049; f_f 20.5 MPa (28 d); f_b 16.33 MPa; W_e^u 35.40 kJ/m³ |
| M2-0.16-PE22–2.0 | not reported | 2.83 (5.68) | 6.45 (2.20) | 4.853 (9.63) | not reported | E1 41.1; εcr 0.036; 134.81; 2.28; 4.87; 234.76; 0.105 |
| M2-0.16-PVA39–2.0 | 91.6 (28 d; 85.1 / 108.6 at 7 / 60 d) | 3.48 (2.36) | 5.28 (9.88) | 0.250 (14.77) | not reported | E1 38.8; εcr 0.026; 9.62; 1.52; 4.18; 10.54; 0.136; f_f 20.2; f_b 14.63; W_e^u 36.04 |
| M3-0.16-PE22–2.0 | not reported | 2.77 (1.32) | 6.76 (3.94) | **6.483** (10.78) | not reported | E1 40.0; εcr 0.046; 140.93; **2.44**; 4.80; **366.44**; 0.076 |
| M3-0.16-PVA39–2.0 | 94.0 (28 d; 84.0 / 100.8 at 7 / 60 d) | 3.32 (1.61) | 5.54 (10.58) | 0.300 (9.49) | not reported | E1 38.1; εcr 0.021; 14.29; 1.67; 4.99; 14.69; 0.188; f_f 18.4; f_b 13.06; W_e^u 29.05 |

Main findings (with Table/Fig. location):

**Curve shape and ranges (Fig. 3; Tables 6–7, p. 7–8)**
- All 13 groups failed in a ductile way with multiple cracking (Fig. 3–4).
- Three stages: elastic, strain-hardening (sawtooth) and softening (p. 4).
- Across all groups: σp/σcr ≥ 1.35 (max 2.44); εp/εcr ≥ 9.62 (max 232.89) (Table 6, p. 7).
- εp range 0.2–6.5%, max 6.483%. The authors compare this with about 0.01% for normal concrete
  and < 0.50% for UHPC (citing Wille et al. 2014) (p. 8).
- E1 range 33.4–46.8 GPa, above the about 30 GPa of NC. They attribute this to the low W/B and
  graded quartz sand (p. 8).

**Fiber type (p. 8, p. 13–14)**
- PE40 vs PVA39, similar d: σp is 5.4% lower and εp is 51.3% higher for PE (p. 8).
- PE22 vs PVA39 across M1–M3:
  - σp 6.45–6.99 vs 4.78–5.54 MPa;
  - εp 3.839–6.483% vs 0.228–0.298% (as printed; Table 6 gives 0.300 for M3-PVA), i.e.
    16.8–21.8× (p. 8).
- Toughness, PE40 vs PVA39: σe,0.85 +0.49%, gp +62.0%, Ipost +836.7% (p. 14).

**Fiber content (Fig. 6, p. 8)**
- From 1.5 to 2.5 vol.% (PE22, M1, W/B 0.16): σcr +29.4%; σp +26.9%; εp +30.5%; σp/σcr +10.1%;
  εp/εcr +142.3%.
- Toughness: σe,0.85 +31.8%; gp +75.2% (p. 14).
- Workability falls as fiber content rises, so 2.0% is recommended (p. 8).

**Fiber diameter (Figs. 7–8, p. 8–10)**
- From 40 to 22 µm (fiber reinforcement index Vf·Lf/df 6.00 → 10.91, Vf in %): σcr +11.7%;
  σp +54.6%; εp +1012.8%; σp/σcr +39.2%; εp/εcr +980.2%.
- Toughness: σe,0.85 +41.0%; gp +1360.3% (p. 14).
- Linear fits on all data points (Fig. 8):
  - σp = 0.50 (Vf·Lf/df) + 1.90, R² = 0.770
  - εp = 0.61 (Vf·Lf/df) − 2.45, R² = 0.750
  - In words: +0.50 MPa and +0.61% per unit index (p. 8).

**W/B (Fig. 9, p. 10)**
- From 0.14 to 0.18: σcr −13.7%.
- σp, εp, σp/σcr and εp/εcr all peak at W/B 0.16, so 0.16 is the stated optimum.
- εp is 0.811 / 3.839 / 1.888% at 0.14 / 0.16 / 0.18 (Table 6).
- Ipost "decreases by 244.6%" from W/B 0.18 to 0.14 (0.286 → 0.083; the percentage is computed
  relative to the lower value) (p. 14).

**Fly ash (Fig. 10, p. 11)**
- From 15 to 25% FA (PE22-2.0): σcr −21.3%; σp −3.3%; εp +68.9%.
- For PE-HSHDC, σe,0.85 and Ipost fall and gp rises. For PVA-HSHDC all three toughness indices
  rise (p. 14).
- A higher FA content was not studied because f_c would fall below 100 MPa (p. 11).

**Toughness and SEM (Table 7; Fig. 11; p. 11, p. 13)**
- gp range 9.26–366.44 kJ/m³. PE-HSHDC is generally > 50 kJ/m³; the cited strain-hardening UHPC
  value is 50 kJ/m³ (p. 13).
- SEM (Fig. 11): many PE fibers pulled out, leaving pull-out holes. Wear and scratches on the
  fiber ends. FA particles embedded in the matrix (p. 11).

**Constitutive model (Eq. 1, Fig. 5, p. 4–5): trilinear**

| Range | Stress |
|---|---|
| 0 < ε ≤ εcr | σ = E1·ε |
| εcr < ε ≤ εp | σ = σcr + E2(ε − εcr) |
| ε > εp | σ = σp − E3(ε − εp) |

- E1, E2 and E3 are the elastic, hardening and softening moduli.
- Only E1, σcr, εcr, σp and εp are tabulated (Table 6). E2 and E3 values are not reported.
- Fig. 5 illustrates the model on one M3-0.16-PE22–2.0 curve.

**Tensile toughness indices (Eqs. 4–6, Fig. 14, p. 12)**
- Equivalent tensile strength: σe,k = ∫₀^εk σ dε / εk.
- Pre-peak ("initial") strain energy density: gp = ∫₀^εp σ dε.
- Residual toughness index: Ipost = ∫εp^εk σ dε / ∫₀^εk σ dε.
- k = 0.85. From Fig. 14, ε0.85 is the post-peak strain at the "ultimate point" Fu where stress has
  dropped to 0.85 of the peak (my reading of the figure).

## Mechanisms / explanations offered by authors
- **PE vs PVA.** PE has a higher strength and modulus. It is hydrophobic, so its chemical bond is
  weaker and the fibers pull out instead of rupturing. Pull-out friction dissipates more energy
  than fiber fracture. The weaker bond also gives somewhat lower strength (p. 5).
  - The authors state that a high-strength matrix needs hydrophobic, high-strength, high-modulus
    fibers with a high reinforcement index (p. 8).
- **Fiber content.** More fibers fill a 3-D fiber network, which restrains microcrack initiation
  and growth (p. 8).
- **Fiber diameter.** At constant L and Vf, a smaller d gives more fibers and so a higher bridging
  stress (p. 10).
- **W/B.** A lower W/B raises matrix strength and the interface parameters Gd and τ0.
  - If the bond is too high, fibers rupture and are under-used. If it is too low, they slip.
  - 0.16 balances the two (p. 10).
  - The fall in Ipost at a low W/B is attributed to more fiber rupture (p. 14).
- **Fly ash.** FA lowers Km and the interface bond, which lowers J_tip and raises J′b, so the PSH
  index rises. FA thus favours pull-out over rupture, citing Li 2019 and Yang et al. 2007 (p. 11).
  FA also lowers cost and shrinkage (p. 11).
  - It has opposite effects on toughness for hydrophobic PE and hydrophilic PVA. The lower bond
    reduces PE bridging stress but helps PVA pull out (p. 14).
- **Fracture model (Fig. 12, p. 11–12).** Four zones:
  - I: linear elastic;
  - II: initial cracking (fibers arrest microcracks until the first through-crack);
  - III: multiple cracking (stress transfer through the interface induces new cracks);
  - IV: main crack, where fibers pull out.
  - Zones II–IV form a "quasi-plastic zone". Vf sets the saturation of the network and Lf/df sets
    the bridging efficiency; together they define an "optimal fiber reinforcement index".
- **Why a uniaxial toughness method.**
  - ASTM C1018 depends on locating the first crack, and its 10.5δ limit is too small for HDC.
  - JSCE-SF4 uses an arbitrary L/150, gives a single index, and is size-dependent.
  - JSCE (2008) and JC/T 2461-2018 give tensile test methods but no toughness index (p. 12).

## Limitations (stated + observed)
**Stated:**
- Single-variable design. The authors recommend orthogonal experiments on fiber type, diameter,
  content and other admixtures (p. 14).
- The bond between HSHDC and existing concrete still needs study (p. 14).

**Observed:**
- n = 3 per group. Some COVs are high: εcr up to 59.93%, σcr up to 19.71%.
- Only one extensometer, with no crack-width or crack-count measurement. Multiple cracking is
  inferred from stress drops on the curve (p. 4).
- Compressive strength was measured only for PVA-HSHDC (Table 5) and for the plain matrix
  (60 d, Table 4). No f'c is reported for the PE mixes, which are the "high-strength high-ductility"
  ones.
  - The 28-d cube f_c of PVA-HSHDC is 91.6–96.4 MPa, below the 100 MPa the authors cite as a
    requirement (p. 11).
- The PVA39 mixes (εp 0.23–0.30%) and PE40 (0.345%) show very limited strain capacity. They are
  still labelled "HSHDC".
- **⚠️ Internal inconsistency in E1 vs εcr.** E1 × εcr does not equal σcr in Table 6. For example,
  for M3-PE22-2.0: 40.0 GPa × 0.046% ≈ 18 MPa, against the reported σcr of 2.77 MPa. The other
  rows are off by a similar factor of about 4–7.
  - The Fig. 5 curve reaches about 4 MPa only at a strain of roughly 0.1–0.2%.
  - So E1 (about 40 GPa) seems inconsistent with the extensometer-based εcr.
  - The paper does not say how E1 was obtained.
- Trilinear model: E2 and E3 are not reported, and no calibration or validation against data is
  given beyond one illustrative curve (Fig. 5).
- Minor text inconsistencies:
  - The PVA εp range is printed as 0.228–0.298%, but Table 6 gives 0.300.
  - The UHPC pre-peak energy is given as 50 kJ/m³ (p. 13) but as "less than 100 kJ/m³" in
    Conclusion 2 (p. 14).
  - "UHDC" is used once (p. 8).
- The 0.2 mm/min rate over a 150 mm gauge is slower than Ranade 2013 (0.5 mm/min). Rate effects
  are small at quasi-static rates, but the difference should be noted.
- Data are available only on request (p. 15).

## Relation to other work
- **Agrees with:**
  - Ranade et al. 2013 "Composite properties of HSHDC" (ACI MJ 110(4); not a wiki source) cites ref. [5]. That study gives a specific energy
    above 300 kJ/m³ for Michigan HSHDC. Here the maximum gp is 366.44 kJ/m³ (M3-PE22), the same
    order. The energy measures may be defined differently (⚠️).
  - Finer PE (higher Vf·Lf/df) improves σp and εp, consistent with Yu et al. 2020 and Li et al.
    2019, as cited (p. 8).
  - More FA favours strain hardening, consistent with Yang, Yang & Li 2007 (ACI MJ), as cited
    (p. 11).
- **Contradicts: ⚔️**
  - Ranade 2013 found that a higher Lf/df (PE28 vs PE38) raised σtu but **lowered** εtu because of
    poor dispersion. Here, decreasing d from 40 to 22 µm raised εp by about 10× (p. 8).
    > Synthesis: probably not a true conflict. The matrices, W/B and curing differ, and dispersion
    > was not measured here.
  - Absolute performance under the same "HSHDC" name differs greatly:
    - Michigan HSHDC (heat-cured at 90 °C): f'c 166 MPa, σtu 14.5 MPa, Et 48.4 GPa
      (Ranade et al. 2013 "Composite properties of HSHDC" (ACI MJ 110(4); not a wiki source));
    - Xi'an HSHDC (20 °C standard cure): σp ≤ 7.69 MPa, PVA-HSHDC f_c 28 d ≤ 96.4 MPa, E1 about
      40 GPa.
    - These are different materials under one acronym (terminology conflict; see
      [[terminology-hdc-ecc-shcc]]).
  - Kamal et al. (2008, as cited) reported more cracks and higher strength as PE content rose;
    this study agrees (p. 2).
- **Extends:**
  - First ingested source from the Chinese (Xi'an University of Architecture & Technology) group.
    Here "HDC" means *high-ductility* concrete, classed as SHCC.
  - First ingested HSHDC tested under **ambient/standard curing**, which partly addresses the
    heat-curing gap.
  - First direct PE vs PVA comparison in one matrix.
  - First FA-content and W/B series for HSHDC in the wiki.
  - First uniaxial-tension toughness indices (σe,0.85, gp, Ipost).
  - First trilinear tensile constitutive model in the wiki.

## Pages updated from this source
- [[dogbone-uniaxial-tension]]: 350 mm JSCE dogbone, 150 mm gauge, 50 × 15 mm section, carbon
  cloth tabs, 0.2 mm/min, clip-on extensometer
- [[tensile-strain-capacity]]
- [[hshdc]]
- [[pe-fiber]]
- [[pva-fiber]]: first primary data
- [[silica-fume]]
- [[strain-hardening]]
- [[multiple-cracking]]
- [[fiber-bridging]]
- [[fiber-matrix-interface]]
- [[heat-curing]]: ambient-cured counterexample
- [[matrix-fracture-toughness]]
- [[compressive-strength]]
- [[flexural-strength]]
- [[terminology-hdc-ecc-shcc]]
- [[uhpc-vhsc]]
- [[mix-designs]]
- [[mechanical-results]]
- [[gaps]]
- NEW [[tensile-constitutive-model]]: trilinear model
- NEW [[tensile-toughness]]: σe,0.85, gp, Ipost, vs ASTM C1018 / JSCE-SF4 / C1609
- NEW [[fly-ash]]
- NEW [[water-binder-ratio]]
- NEW [[fiber-geometry]]: Vf·Lf/df
- NEW [[tensile-toughness]]: optional; strain energy density

## To verify
- [ ] How E1 was obtained (tangent of the extensometer curve?), given that E1·εcr ≠ σcr in Table 6
      (factor about 4–7). Check Fig. 3 curves against E1 ⚠️ unverified.
- [ ] SP dosage (and any sand ratio change) for the W/B 0.14 and 0.18 mixes. Table 4 lists only
      W/B 0.16 ⚠️ unverified.
- [ ] FA density 1.12 g/cm³ (Table 2) seems low for Class F fly ash (typically about 2.2–2.4
      g/cm³) [general knowledge — needs source]. Possibly a bulk density or a misprint
      ⚠️ unverified.
- [ ] DA/b = 3.0% (Table 4) is unusually high for a defoamer; confirm it is not 0.3% or a
      different basis ⚠️ unverified.
- [ ] The definition of ε0.85 is read from Fig. 14: the post-peak strain where σ = 0.85σp.
      The figure axis label reads "σu (0.85σu)" ⚠️ unverified.
- [ ] Rotational boundary condition of the grips (fixed vs pinned) is not stated; Fig. 1b shows
      wedge-type grips ⚠️ unverified.
- [ ] The PVA εp range is printed as 0.228–0.298% on p. 8, but Table 6 gives 0.300% for
      M3-PVA39-2.0 (minor).
- [ ] UHPC pre-peak energy: 50 kJ/m³ (p. 13) vs "less than 100 kJ/m³" (Conclusion 2, p. 14).
- [ ] Whether the Table 6 tension specimens were all tested at 28 d. Section 2.4 says "other
      mechanical parameters only at 28-day", and Fig. 2 says "28 d → Testing".
