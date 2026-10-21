---
type: source
slug: wang2019-rc-beam-ecc-shear-strengthening
title: "Shear Behaviors of RC Beams Externally Strengthened with Engineered Cementitious Composite Layers"
authors: [Guan Wang, Caiqian Yang, Yong Pan, Fawang Zhu, Kai Jin, Kefeng Li, Antonio Nanni]
year: 2019            # Materials 12(13), July 2019 issue; published online 5 Jul 2019 (received 16 Jun, accepted 4 Jul 2019)
venue: "Materials (MDPI) 12(13) (2019) 2163"
doi: "10.3390/ma12132163"
raw_file: raw/papers/Wang2019_RC-beam-ECC-shear-strengthening.pdf
material_term: "ECC (engineered cementitious composite), PVA fiber 1.5 vol.%, sprayed. Normal-strength (f_cu 55.9 MPa, σ_tu 4.84 MPa). Authors claim 'remarkable tensile strain hardening'; Fig. 2 (p. 3) shows 3 hardening curves with strain at peak stress ≈ 0.9–1.9% and ultimate strain ≈ 2.6–3.45% (read from figure; no numbers in text)"
study_type: experimental
tags: [ecc, pva-fiber, sprayed-ecc, shear-strengthening, rc-beam, no-stirrups, four-point-bending, fbg-sensor, truss-arch-model, debonding, interface-agent, southeast-university, university-of-miami]
ingested: 2026-10-20
updated: 2026-10-21
---

# Shear strengthening of RC beams with sprayed side ECC layers (Wang et al., 2019)

> Re-checked against the publisher PDF (16 pp.) on 2026-10-21; locations now give PDF page numbers.

## One-paragraph summary
**Experimental** study from Southeast University (Nanjing), Xiangtan University and the University of
Miami (Nanni).

**Specimens and loading:**
- Twelve 150 × 300 × 2100 mm RC beams (span 1800 mm) with **no stirrups in the shear span**. Four
  Ø10 stirrups at 50 mm sit at each end only.
- Tested in four-point bending under load control (Sects. 3.1–3.2, p. 4–5, Table 2, p. 5).
- **Variables:** sprayed PVA-ECC layer thickness on each side t = 0 / 20 / 40 mm; tension steel 2Ø16
  (type A, ρ 0.89%) or 2Ø25 (type B, ρ 2.18%); shear span-to-depth ratio a/d = 2 or 3.
- **Instrumentation:** FBG strain rosettes (gauge 15 cm) recorded the shear strain on the beam sides.

**Material:** the ECC (PVA 1.5 vol.%) had f_cu = 55.9 MPa (100 mm cubes, 28 d), first-crack tensile
stress 4.05 MPa and tensile strength 4.84 MPa (dogbones) (Sects. 2.1–2.2, p. 3). Fig. 2 (p. 3) shows strain
hardening to ≈ 0.9–1.9% at peak stress (read from Fig. 2).

**Results:**
- **Ultimate load:** rose by 20–89%. The best case was SB-40-2: 185 → 350 kN, +89% (Table 3, p. 7).
- **Thicker is not always better:**
  - All 40 mm layers **debonded**.
  - Type A beams with 40 mm layers fell below the code minimum reinforcement ratio (ρ 0.58% < 0.65%) once
    the ECC width is counted. SA-40-2 (190 kN) then carried less than SA-20-2 (250 kN) (Sect. 3.3.1, p. 7).
- **Model:** a truss (ECC tensile strength as the tension tie) plus arch (only at a/d < 2.5) model predicts
  the ECC contribution:
  - a/d = 3: 68–100% of the test value;
  - a/d = 2: about 45–52% (conservative);
  - SA-40-2: 172% (unconservative) (Table 4, p. 13).

> Synthesis: this is the wiki's **first primary experimental structural study** of RC strengthening with
> ECC. Until now [[rc-member-strengthening]] was second-hand only. Three things stand out:
> - Strengthening works with **normal-strength PVA-ECC** (σ_tu < 5 MPa).
> - The **ECC–concrete bond limits thick layers**.
> - Two of its strengthened specimens failed with *smaller* gains than the 20 mm specimens. Structural
>   detailing (minimum ρ, bond), not ECC ductility, governs.

## Objective / research question
- Quantify the shear strengthening effect of ECC layers sprayed on both beam sides, as a function of layer
  thickness, longitudinal reinforcement ratio and a/d (Sect. 1, last paragraph, p. 2).
- Check whether FBG rosettes can monitor the development of shear strain (Sects. 1, 3.3.2, p. 2, 7–8).
- Build a truss-and-arch evaluation of the ECC shear contribution (Sect. 4, p. 9–13).

## Materials & mix design
The ECC was "prepared by the procedure suggested by Zhou [43]" (Zhou et al. 2012, Cem Concr Compos 34:342–348, mixing
sequence) (Sect. 2.1, p. 3). **The mix proportions are not reported** (confirmed in the PDF).

| Mix ID | Cement | Fly ash | Slag/other | Sand (type, max size) | W/B | SP | Fiber type | L (mm) | d (µm) | Vf (vol.%) |
|---|---|---|---|---|---|---|---|---|---|---|
| ECC (sprayed) | not reported | not reported | not reported | not reported | not reported | not reported | PVA | not reported | not reported | 1.5 |

Units of binder quantities: n/a (not reported)

Other materials (Table 1, p. 4; Sect. 3.1, p. 4):
- **Concrete:** commercial; f_c (cube) 32 MPa; f_t 2.6 MPa; E 30.0 GPa. Demoulded at 10 d. Age at test
  not reported.
- **ECC:** f_c (cube) 56 MPa; f_t 4.0 MPa (≈ first-crack; text gives 4.05 MPa); E 24.9 GPa.
- **Rebar** (f_y / f_u in MPa; E in GPa):

  | Bar | Net area (mm²) | f_y | ε_y | f_u | ε_u | E |
  |---|---|---|---|---|---|---|
  | Ø10 | 50.27 | 259 | 0.00122 | 329 | 0.012 | 212.3 |
  | Ø16 | 201.06 | 386 | 0.00189 | 478 | 0.013 | 203.8 |
  | Ø25 | 490.87 | 374 | 0.00186 | 439 | 0.011 | 201.6 |

- **Interface agent:** 0.85 cement + 0.05 silica fume + 0.1 expansive agent + 0.3 water, by mass. Applied
  to chiselled, cleaned, saturated-surface-dry beam sides before spraying (Sect. 3.1, step 3, p. 4).
- **Curing of the layers:** under a polyethylene sheet with water spraying, 28 d at room temperature
  (Sect. 3.1, step 5, p. 4).
- **Sprayed vs cast:** the authors rely on Kim et al. 2004 (ref. 45, as cited): sprayed ECC strain-hardens
  with strain capacity comparable to cast ECC (Sect. 3.1, p. 4). **Sprayed ECC itself was not tensile-tested here.** The
  dogbones were "fabricated and cured according to the standard" (GB 50010 cited as ref. 44, p. 3); whether they were cast or
  sprayed is not stated ⚠️.

## Test methods
- **ECC compression:** 3 cubes, 100 mm, 28 d, MTS 1000 kN (Sect. 2.1, p. 3).
- **ECC direct tension:** 3 dogbones; gauge section 13 × 30 × 80 mm (t × w × L); 0.2 mm/min, Shimadzu
  AG-Xplus 10 kN; 2 LVDTs over the middle part; fixed ends (Sect. 2.2, p. 3, Fig. 1, p. 3).
  → [[dogbone-uniaxial-tension]]
- **Beams:**
  - 150 × 300 mm; L = 2100 mm; simply supported span 1800 mm. Effective depth d = 257 mm (type A) and 252.5 mm
    (type B) (Fig. 3, p. 5). ρ in Table 2 is computed on the gross section b × h (e.g. 2 × 201.06 / (150 × 300) = 0.89%;
    after strengthening b = 190 or 230 mm).
  - Loading span 772 / 258 mm (type A) or 790 / 285 mm (type B) for a/d = 2 / 3.
  - Load control, MTS 1000 kN (Sect. 3.2, p. 4–5, Table 2, Fig. 3, p. 5).
- **Measurement:**
  - 3 LVDTs: mid-span and the two load points.
  - One strain gauge on each main bar at mid-span.
  - Two FBG rosettes per beam (3 FBGs each, 15 cm gauge) on the side in the shear span.
  - Visual crack observation (all p. 6).
- **Curing & test age:** ECC material tests at 28 d. Strengthening layers cured 28 d before testing.
  Concrete age not reported.
→ [[rc-member-strengthening]]

## Key results
| Mix ID | f'c (MPa) | First-crack stress (MPa) | Tensile strength (MPa) | Tensile strain capacity (%) | Crack width (µm) | Other |
|---|---|---|---|---|---|---|
| ECC (PVA 1.5%) | 55.9 (100 mm cube, 28 d, CoV 4.20%) | 4.05 (CoV 6.67%) | 4.84 (CoV 5.28%); individual curve peaks ≈ 4.6 / 4.85 / 5.1 (read from Fig. 2) | at peak stress ≈ 0.9 / 1.9 / 1.4 (three curves, read from Fig. 2, p. 3); ultimate (end of curve) ≈ 3.3 / 3.45 / 2.6 | not reported | E = 24.9 GPa (Table 1, p. 4); text p. 3 |

Beam results (Table 2, p. 5; Table 3, p. 7; Table 4, p. 13; failure modes Sect. 3.3.3, p. 9–10):

| Specimen | ρ before → after (%) | P_u (kN) | y, ultimate mid-span deflection (mm) | ΔP_u (kN) / S (%) | τ (MPa) | Failure | Model / test (%) |
|---|---|---|---|---|---|---|---|
| CA-2 | 0.89 | 136 | 8.51 | — | 1.44 | brittle shear | — |
| CA-3 | 0.89 | 85 | 6.68 | — | 0.90 | brittle shear | — |
| CB-2 | 2.18 | 185 | 9.60 | — | 1.83 | brittle shear | — |
| CB-3 | 2.18 | 125 | 7.09 | — | 1.23 | brittle shear | — |
| SA-20-2 | 0.89 → 0.71 | 250 | 7.44 | 114 / 84 | 2.18 | shear; layer peeled after failure | 47 |
| SA-20-3 | 0.89 → 0.71 | 117 | 8.60 | 32 / 38 | 1.02 | shear; one main crack in ECC | 75 |
| SB-20-2 | 2.18 → 1.72 | 290 | 8.38 | 105 / 57 | 2.39 | shear; no debonding, most cracks | 45 |
| SB-20-3 | 2.18 → 1.72 | 150 | 4.53 | 25 / 20 | 1.24 | shear; layer peeled after failure | 68 |
| SA-40-2 | 0.89 → 0.58 | 190 | 9.18 | 54 / 40 | 1.41 | debonding | 172 |
| SA-40-3 | 0.89 → 0.58 | 120 | 9.86 | 35 / 41 | 0.89 | debonding | 94 |
| SB-40-2 | 2.18 → 1.42 | 350 | 9.14 | 165 / 89 | 2.48 | debonding | 52 |
| SB-40-3 | 2.18 → 1.42 | 151 | 6.30 | 26 / 21 | 1.06 | debonding | 100 |

Main findings (with Table/Fig. location):
- **Strength gain:** ultimate load rose by 20–89% (Table 3, p. 7). The gain is large at a/d = 2 (40–89%) and
  small at a/d = 3 (20–41%).
- **a/d = 3 is thickness-insensitive:** SA-40-3 ≈ SA-20-3 (120 vs 117 kN) and SB-40-3 ≈ SB-20-3 (151 vs
  150 kN) (Sect. 3.3.1, p. 7).
- **SB-40-2 vs SB-20-2:** +21% (350 vs 290 kN) (Sect. 3.3.1, p. 7).
- **Over-strengthening:** SA-40-2 (190 kN) carried less than SA-20-2 (250 kN). Its effective ρ (0.58%) fell
  below the GB 50010-2010 minimum of 0.65% ("max of 0.20% and 45 f_t/f_y"), and dowel action was
  insufficient (Sect. 3.3.1, p. 7) ⚠️ the 0.65% cannot be reproduced from Table 1 values.
- **Shear stress:** τ of SA-20-2 is 51.9% higher than CA-2 (Fig. 6, p. 9; Table 3 values give 2.18/1.44 = +51.4%)
  (Sect. 3.3.2, p. 8). τ = average shear stress between support and nearer load point at P_u (p. 6).
- **Ductility:** all control beams failed brittle with no yielding stage. All strengthened beams still
  failed in shear (20 mm) or by debonding (40 mm). The FBGs captured a short "yielding stage" in the shear
  strain only for SA-20-2 and SB-20-2 (Fig. 5, p. 8; Sect. 3.3.2, p. 7–8).
- **Cracking:** strengthened beams showed more cracks at narrower spacing than control beams (Fig. 7b, p. 9; p. 10). No
  crack widths were reported. In 40 mm beams, partial debonding preceded failure, after which few new cracks formed
  in the ECC (p. 10).
- **Deflection claim:** the text says ultimate deflections of 20 mm beams exceed those of the controls
  (Sect. 3.3.1, p. 7), but Table 3 (p. 7) shows lower y for SA-20-2 (7.44 vs 8.51) and SB-20-3 (4.53 vs 7.09)
  (confirmed as printed in the PDF).
- **Debonding:** the 40 mm FBG rosettes show a sharp drop in shear strain before failure as debonding
  released the strain (Fig. 5c, p. 8; p. 7). Applies to SA-40-2, SA-40-3, SB-40-2; SB-40-3 instead formed a visible
  large crack within the FBG gauge.
- **Truss + arch model** (Eq. 10, p. 11):

  V = 2(V_t + V_a), with V_t = ηβσ_t·h·t (φ = 45°).

  - η = 0.6 for 20 mm layers and 0.4 for 40 mm (bond reduction).
  - β = −23.04ρ + 1.00 (Eq. 11, p. 12), with ρ as a **decimal** (after-strengthening ρ). Verified by back-calculating
    the a/d = 3 rows of Table 4 with σ_t = 4.0 MPa (Table 1 f_t), h = 300 mm: e.g. SA-20-3: 2 × 0.6 × (1 − 23.04 × 0.0071)
    × 4.0 × 300 × 20 = 24 kN (Table 4: 24); SB-40-3: 2 × 0.4 × 0.673 × 4.0 × 300 × 40 = 26 kN (Table 4: 26).
  - Crack angle φ = 45° (Sect. 4.3.3, p. 12). Arch softening coefficient ν = 0.6 (ACI value for concrete; the JSCE
    0.7 − f_c/200 and Eurocode 0.6(1 − f_c/250) forms are also cited), with arch action only at a/d < 2.5 (Kani) (p. 11–13).
  - Accuracy (Table 4, p. 13), calculated / experimental ΔP (kN): SA-20-2 54/114; SA-20-3 24/32; SB-20-2 47/105;
    SB-20-3 17/25; SA-40-2 93/54; SA-40-3 33/35; SB-40-2 86/165; SB-40-3 26/26. a/d = 3 gives 68–100%; a/d = 2 gives
    45–52%; SA-40-2 gives 172%.

## Mechanisms / explanations offered by authors
- **Truss tie:** ECC's tensile strength after cracking (strain hardening, fiber bridging) acts as a
  distributed tension tie that replaces the stirrups. ECC between cracks acts as the compression strut
  (Sect. 4.1, p. 9–10).
- **Arch action** adds capacity only for short shear spans (a/d < 2.5, after Kani) (Sect. 4.2, p. 10–11).
- **Thick layers debond:** bond risk rises with thickness, hence the lower η (Sect. 4.3.1, p. 12).
- **Minimum reinforcement:** adding ECC width lowers the effective longitudinal ρ. Below the minimum,
  dowel action is inadequate and the ECC is not fully used (Sect. 3.3.1, p. 7).
- **Conservative arch prediction:** the concrete softening coefficient is too conservative for ECC under
  biaxial tension–compression, because fiber bridging is ignored (Sect. 4.4, p. 13).

## Limitations (stated + observed)
- **Stated:**
  - The softening coefficient of ECC under biaxial tension–compression is unknown (Sect. 4.4, p. 13; Conclusion 6, p. 14).
  - η and β are empirical, fitted to this test series (Sect. 4.3).
- **Observed: one specimen per configuration**, with no repeats.
- **Observed: ECC tensile behaviour under-reported.**
  - The ECC mix proportions are not reported.
  - The tensile strain capacity is shown only graphically (Fig. 2) and crack width is not reported.
  - Sprayed ECC was not tested itself.
- **Observed: model is not independent.** The truss–arch model is calibrated on the same tests (η, β), and
  its accuracy is poor at a/d = 2 (about 50%).
- **Observed: bond not characterised.** No bond or pull-off tests of the interface agent were done, and
  debonding governed every 40 mm beam.
- **Observed: monotonic loading only**, under load control, so the post-peak response is not captured.
- **Observed: internal inconsistencies.**
  - The text calls ECC "ultra-high tensile strength" while measuring 4.84 MPa.
  - Deflection statement vs Table 3.
  - The "0.65%" minimum ρ cannot be reproduced from the data.
  - "51.9%" vs 51.4% computed.
  - The truss model uses σ_t = 4.0 MPa (Table 1), not the 4.84 MPa peak tensile strength of Sect. 2.2 (found by back-calculation).

## Relation to other work
- **Agrees with:** early structural ECC evidence that ECC can replace stirrups in shear (Fischer & Li,
  as cited in [[li2003-ecc-review]], p. 221–224; see [[rc-member-strengthening]]).
- **Extends:**
  - First primary data in the wiki on ECC used as an **external strengthening layer** on existing RC.
  - First use in the wiki of **sprayed** ECC on a structural member (sprayed ECC was listed only as a
    processing route in [[li2003-ecc-review]]; see [[repair-and-field-applications]]).
  - The material is a normal-strength PVA-ECC (f_cu ≈ 56 MPa, σ_tu 4.84 MPa). This fits the normal
    ECC/HDC class (compare [[chai2023-hdc-ambient-temperature]], also Southeast University, PVA-HDC
    f_cu 48 MPa).
- **Contradicts:** ⚔️ none at the measured-value level. The finding that the **interface** governs thick
  layers sharpens an existing gap: the bond between HDC and existing concrete is unstudied
  ([[yang2024-hshdc-uniaxial-tension]], p. 14; see [[gaps]]).

## Pages updated from this source
- [[rc-member-strengthening]]
- [[repair-and-field-applications]]
- [[dogbone-uniaxial-tension]]
- [[pva-fiber]]
- [[compressive-strength]]
- [[tensile-constitutive-model]]
- [[multiple-cracking]]
- [[mechanical-results]]
- [[mix-designs]]
- [[gaps]]

## To verify
- [x] ECC tensile strain capacity: read from Fig. 2 (p. 3) on 2026-10-21 — strain at peak stress ≈ 0.9–1.9%, ultimate ≈ 2.6–3.45% (≈ values).
- [ ] Whether the dogbones were cast or sprayed (still not stated in the PDF).
- [ ] Minimum reinforcement 0.65% (Sect. 3.3.1, p. 7): which f_t and f_y give "45 f_t/f_y = 0.65%"? Table 1 values give about 0.30% (concrete f_t) or about 0.47–0.58% (ECC f_t 4.0–4.84 MPa, f_y 374–386 MPa). Confirmed as printed.
- [x] β = −23.04ρ + 1.00 (Eq. 11): ρ is a decimal — verified by back-calculating the a/d = 3 rows of Table 4 (see Key results).
- [ ] Text "deflections larger than control" vs Table 3 (SA-20-2, SB-20-3): confirmed as printed; an author inconsistency.
- [x] τ increase "51.9%" (p. 8) vs 51.4% computed from Table 3: confirmed as printed (rounding of τ in Table 3 likely).
- [ ] Fiber length, diameter and brand of the PVA fiber (not reported in the PDF; maybe in Zhou 2012, ref. 43).
