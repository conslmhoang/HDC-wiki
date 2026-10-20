---
type: source
slug: wang2019-rc-beam-ecc-shear-strengthening
title: "Shear Behaviors of RC Beams Externally Strengthened with Engineered Cementitious Composite Layers"
authors: [Guan Wang, Caiqian Yang, Yong Pan, Fawang Zhu, Kai Jin, Kefeng Li, Antonio Nanni]
year: 2019            # Materials 12(13), July 2019 issue; published online 5 Jul 2019 (received 16 Jun, accepted 4 Jul 2019)
venue: "Materials (MDPI) 12(13) (2019) 2163"
doi: "10.3390/ma12132163"
raw_file: raw/papers/Wang2019_RC-beam-ECC-shear-strengthening.xml
material_term: "ECC (engineered cementitious composite), PVA fiber 1.5 vol.%, sprayed. Normal-strength (f_cu 55.9 MPa, σ_tu 4.84 MPa). Authors claim 'remarkable tensile strain hardening' (Fig. 2) but give no numerical strain capacity"
study_type: experimental
tags: [ecc, pva-fiber, sprayed-ecc, shear-strengthening, rc-beam, no-stirrups, four-point-bending, fbg-sensor, truss-arch-model, debonding, interface-agent, southeast-university, university-of-miami]
ingested: 2026-10-20
updated: 2026-10-20
---

# Shear strengthening of RC beams with sprayed side ECC layers (Wang et al., 2019)

## One-paragraph summary
**Experimental** study from Southeast University (Nanjing), Xiangtan University and the University of
Miami (Nanni).

**Specimens and loading:**
- Twelve 150 × 300 × 2100 mm RC beams (span 1800 mm) with **no stirrups in the shear span**. Four
  Ø10 stirrups at 50 mm sit at each end only.
- Tested in four-point bending under load control (Sects. 3.1–3.2, Table 2).
- **Variables:** sprayed PVA-ECC layer thickness on each side t = 0 / 20 / 40 mm; tension steel 2Ø16
  (type A, ρ 0.89%) or 2Ø25 (type B, ρ 2.18%); shear span-to-depth ratio a/d = 2 or 3.
- **Instrumentation:** FBG strain rosettes (gauge 15 cm) recorded the shear strain on the beam sides.

**Material:** the ECC (PVA 1.5 vol.%) had f_cu = 55.9 MPa (100 mm cubes, 28 d), first-crack tensile
stress 4.05 MPa and tensile strength 4.84 MPa (dogbones) (Sects. 2.1–2.2).

**Results:**
- **Ultimate load:** rose by 20–89%. The best case was SB-40-2: 185 → 350 kN, +89% (Table 3).
- **Thicker is not always better:**
  - All 40 mm layers **debonded**.
  - Type A beams with 40 mm layers fell below the code minimum reinforcement ratio (ρ 0.58% < 0.65%) once
    the ECC width is counted. SA-40-2 (190 kN) then carried less than SA-20-2 (250 kN) (Sect. 3.3.1).
- **Model:** a truss (ECC tensile strength as the tension tie) plus arch (only at a/d < 2.5) model predicts
  the ECC contribution:
  - a/d = 3: 68–100% of the test value;
  - a/d = 2: about 45–52% (conservative);
  - SA-40-2: 172% (unconservative) (Table 4).

> Synthesis: this is the wiki's **first primary experimental structural study** of RC strengthening with
> ECC. Until now [[rc-member-strengthening]] was second-hand only. Three things stand out:
> - Strengthening works with **normal-strength PVA-ECC** (σ_tu < 5 MPa).
> - The **ECC–concrete bond limits thick layers**.
> - Two of its strengthened specimens failed with *smaller* gains than the 20 mm specimens. Structural
>   detailing (minimum ρ, bond), not ECC ductility, governs.

## Objective / research question
- Quantify the shear strengthening effect of ECC layers sprayed on both beam sides, as a function of layer
  thickness, longitudinal reinforcement ratio and a/d (Sect. 1, last paragraph).
- Check whether FBG rosettes can monitor the development of shear strain (Sects. 1, 3.3.2).
- Build a truss-and-arch evaluation of the ECC shear contribution (Sect. 4).

## Materials & mix design
The ECC was "prepared by the procedure suggested by Zhou [43]" (Zhou et al. 2012, CCC, mixing sequence).
**The mix proportions are not reported.**

| Mix ID | Cement | Fly ash | Slag/other | Sand (type, max size) | W/B | SP | Fiber type | L (mm) | d (µm) | Vf (vol.%) |
|---|---|---|---|---|---|---|---|---|---|---|
| ECC (sprayed) | not reported | not reported | not reported | not reported | not reported | not reported | PVA | not reported | not reported | 1.5 |

Units of binder quantities: n/a (not reported)

Other materials (Table 1; Sect. 3.1):
- **Concrete:** commercial; f_c (cube) 32 MPa; f_t 2.6 MPa; E 30.0 GPa. Demoulded at 10 d. Age at test
  not reported.
- **ECC:** f_c (cube) 56 MPa; f_t 4.0 MPa (≈ first-crack; text gives 4.05 MPa); E 24.9 GPa.
- **Rebar** (f_y / f_u in MPa; E in GPa):

  | Bar | f_y | f_u | E |
  |---|---|---|---|
  | Ø10 | 259 | 329 | 212.3 |
  | Ø16 | 386 | 478 | 203.8 |
  | Ø25 | 374 | 439 | 201.6 |

- **Interface agent:** 0.85 cement + 0.05 silica fume + 0.1 expansive agent + 0.3 water, by mass. Applied
  to chiselled, cleaned, saturated-surface-dry beam sides before spraying (Sect. 3.1, step 3).
- **Curing of the layers:** under a polyethylene sheet with water spraying, 28 d at room temperature
  (Sect. 3.1, step 5).
- **Sprayed vs cast:** the authors rely on Kim et al. 2004 (ref. 45, as cited): sprayed ECC strain-hardens
  with strain capacity comparable to cast ECC. **Sprayed ECC itself was not tensile-tested here.** The
  dogbones were presumably cast (not stated ⚠️).

## Test methods
- **ECC compression:** 3 cubes, 100 mm, 28 d, MTS 1000 kN (Sect. 2.1).
- **ECC direct tension:** 3 dogbones; gauge section 13 × 30 × 80 mm (t × w × L); 0.2 mm/min, Shimadzu
  AG-Xplus 10 kN; 2 LVDTs over the middle part; fixed ends (Sect. 2.2, Fig. 1).
  → [[dogbone-uniaxial-tension]]
- **Beams:**
  - 150 × 300 mm; L = 2100 mm; simply supported span 1800 mm.
  - Loading span 772 / 258 mm (type A) or 790 / 285 mm (type B) for a/d = 2 / 3.
  - Load control, MTS 1000 kN (Sect. 3.2, Table 2, Fig. 3).
- **Measurement:**
  - 3 LVDTs: mid-span and the two load points.
  - One strain gauge on each main bar at mid-span.
  - Two FBG rosettes per beam (3 FBGs each, 15 cm gauge) on the side in the shear span.
  - Visual crack observation.
- **Curing & test age:** ECC material tests at 28 d. Strengthening layers cured 28 d before testing.
  Concrete age not reported.
→ [[rc-member-strengthening]]

## Key results
| Mix ID | f'c (MPa) | First-crack stress (MPa) | Tensile strength (MPa) | Tensile strain capacity (%) | Crack width (µm) | Other |
|---|---|---|---|---|---|---|
| ECC (PVA 1.5%) | 55.9 (100 mm cube, 28 d, CoV 4.20%) | 4.05 (CoV 6.67%) | 4.84 (CoV 5.28%) | not reported numerically (Fig. 2 shows hardening) | not reported | E = 24.9 GPa (Table 1) |

Beam results (Tables 2–4):

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
- **Strength gain:** ultimate load rose by 20–89% (Table 3). The gain is large at a/d = 2 (40–89%) and
  small at a/d = 3 (20–41%).
- **a/d = 3 is thickness-insensitive:** SA-40-3 ≈ SA-20-3 (120 vs 117 kN) and SB-40-3 ≈ SB-20-3 (151 vs
  150 kN) (Sect. 3.3.1).
- **SB-40-2 vs SB-20-2:** +21% (350 vs 290 kN) (Sect. 3.3.1).
- **Over-strengthening:** SA-40-2 (190 kN) carried less than SA-20-2 (250 kN). Its effective ρ (0.58%) fell
  below the GB 50010-2010 minimum of 0.65% ("max of 0.20% and 45 f_t/f_y"), and dowel action was
  insufficient (Sect. 3.3.1) ⚠️ the 0.65% cannot be reproduced from Table 1 values.
- **Shear stress:** τ of SA-20-2 is 51.9% higher than CA-2 (Fig. 6; Table 3 values give 2.18/1.44 = +51%)
  (Sect. 3.3.2).
- **Ductility:** all control beams failed brittle with no yielding stage. All strengthened beams still
  failed in shear (20 mm) or by debonding (40 mm). The FBGs captured a short "yielding stage" in the shear
  strain only for SA-20-2 and SB-20-2 (Figs. 5, 7).
- **Cracking:** strengthened beams showed more cracks at narrower spacing than control beams (Fig. 7b). No
  crack widths were reported.
- **Deflection claim:** the text says ultimate deflections of 20 mm beams exceed those of the controls
  (Sect. 3.3.1), but Table 3 shows lower y for SA-20-2 (7.44 vs 8.51) and SB-20-3 (4.53 vs 7.09) ⚠️.
- **Debonding:** the 40 mm FBG rosettes show a sharp drop in shear strain before failure as debonding
  released the strain (Fig. 5c).
- **Truss + arch model** (Eq. 10):

  V = 2(V_t + V_a), with V_t = ηβσ_t·h·t (φ = 45°).

  - η = 0.6 for 20 mm layers and 0.4 for 40 mm (bond reduction).
  - β = −23.04ρ + 1.00 (ρ presumably as a decimal ⚠️) (Eq. 11).
  - Arch softening coefficient ν = 0.6 (ACI value for concrete), with arch action only at a/d < 2.5.
  - Accuracy (Table 4): a/d = 3 gives 68–100%; a/d = 2 gives 45–52%; SA-40-2 gives 172%.

## Mechanisms / explanations offered by authors
- **Truss tie:** ECC's tensile strength after cracking (strain hardening, fiber bridging) acts as a
  distributed tension tie that replaces the stirrups. ECC between cracks acts as the compression strut
  (Sect. 4.1).
- **Arch action** adds capacity only for short shear spans (a/d < 2.5, after Kani) (Sect. 4.2).
- **Thick layers debond:** bond risk rises with thickness, hence the lower η (Sect. 4.3.1).
- **Minimum reinforcement:** adding ECC width lowers the effective longitudinal ρ. Below the minimum,
  dowel action is inadequate and the ECC is not fully used (Sect. 3.3.1).
- **Conservative arch prediction:** the concrete softening coefficient is too conservative for ECC under
  biaxial tension–compression, because fiber bridging is ignored (Sect. 4.4).

## Limitations (stated + observed)
- **Stated:**
  - The softening coefficient of ECC under biaxial tension–compression is unknown (Sect. 4.4, Conclusions).
  - η and β are empirical, fitted to this test series (Sect. 4.3).
- **Observed: one specimen per configuration**, with no repeats.
- **Observed: ECC tensile behaviour under-reported.**
  - The ECC mix proportions are not reported.
  - The tensile strain capacity and crack width of the ECC are not reported numerically.
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
- [ ] ECC tensile strain capacity: read from Fig. 2 (not stated in the text).
- [ ] Whether the dogbones were cast or sprayed.
- [ ] Minimum reinforcement 0.65% (Sect. 3.3.1): which f_t and f_y give "45 f_t/f_y = 0.65%"? Table 1 values give about 0.30% (concrete f_t) or about 0.47–0.52% (ECC f_t).
- [ ] β = −23.04ρ + 1.00 (Eq. 11): is ρ a decimal? With ρ in % the formula gives negative β.
- [ ] Text "deflections larger than control" vs Table 3 (SA-20-2, SB-20-3).
- [ ] τ increase "51.9%" vs 51.4% computed from Table 3.
- [ ] Fiber length, diameter and brand of the PVA fiber (not reported; maybe in Zhou 2012, ref. 43).
