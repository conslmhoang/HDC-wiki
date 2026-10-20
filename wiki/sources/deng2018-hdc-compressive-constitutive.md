---
type: source
slug: deng2018-hdc-compressive-constitutive
title: "Uniaxial Compressive Test of High Ductile Fiber-Reinforced Concrete and Damage Constitutive Model"
authors: [Mingke Deng, Jiaojiao Pan, Xingwen Liang]
year: 2018            # vol. 2018; received 5 Aug 2017, published 25 Feb 2018
venue: "Advances in Civil Engineering, vol. 2018, Article ID 4308084, 12 pp. (Hindawi)"
doi: "10.1155/2018/4308084"
raw_file: raw/papers/Deng2018_HDC-compressive-constitutive.pdf
material_term: "HDC = high ductile fiber-reinforced concrete (an HPFRCC 'just like' ECC)"
study_type: experimental + analytical (uniaxial compression; damage constitutive model)
tags: [compression, constitutive-model, damage-mechanics, pva, xauat, deng-group, fly-ash, water-binder-ratio]
ingested: 2026-10-20
updated: 2026-10-20
---

# Compressive stress–strain and damage constitutive model of PVA-HDC (Deng et al., 2018)

## One-paragraph summary
The XAUAT (Deng) group tested 100 × 100 × 300 mm prisms in uniaxial compression, 3 per mix
(Table 2). The 10 mixes were one mortar matrix and nine PVA-HDC mixes, varying:
- PVA content: 1, 1.5, 2 vol.%;
- W/B: 0.26, 0.29, 0.32;
- fly ash: 40, 50, 60%;
- sand/binder: 0.24, 0.36, 0.48.

Results (Table 3; p. 3, Fig. 2):
- **Matrix:** σ0 = 63.06 MPa at ε0 = 0.213%. It fails in brittle splitting into several columns.
- **HDC:** σ0 = 50.3–64.4 MPa, with peak strain 2.61–3.15× the matrix. It fails through one inclined
  shear crack, stays intact, and keeps 10–20% residual capacity.

**Optima:** the authors find W/B 0.29, fly ash 50% and sand/binder 0.36 best for combined strength and
strain (Sect. 3.3, Fig. 5).

**Model.** The authors propose a Weibull-type damage constitutive model with two damage thresholds:
γ ≈ 0.8ε0, where damage starts, and β ≈ 1.3ε0, where the residual plateau starts (Eqs. 6–10, Table 4).
Damage at β is D ≈ 0.85, so damage never reaches 1. The model fits the test curves (R about 0.98) as well as
the earlier Li and Xu models and better than Xu's. Unlike them, it reproduces the residual plateau.

**Data overlap:** mixes 1–4 appear to be the same tests as [[deng2015-hdc-compressive-toughness]]
(identical peak loads for mixes 2–4), but the reported peak strains differ ⚔️.

## Objective / research question
- Measure the effect of PVA content, W/B, fly ash content and sand/binder ratio on the characteristic points
  of the HDC compressive stress–strain curve (p. 2).
- Build a damage constitutive model that captures initial damage, damage evolution and the residual
  capacity due to fiber bridging. The aim is nonlinear analysis and ductility design of members (p. 1–2).

## Terminology (rule §3)
- The authors' exact term is **"high ductile fiber-reinforced concrete (HDC)"**. They describe it as, "just like"
  ECC, a kind of HPFRCC, designed on micromechanics and fracture mechanics (p. 1). They cite
  [[deng2015-hdc-compressive-toughness]] as ref. [1] for the term.
- **Tensile strain hardening:** stated as a general property: HDC "can be characterized by pseudo
  strain hardening and multiple cracking behaviors when subjected to tensile loading" (p. 1). Some
  explanations also refer to the "ultimate tensile strain of HDC" (p. 3). However, **no tensile test is
  reported** in this paper.

## Materials & mix design
| Mix ID | Cement | Fly ash | Slag/other | Sand (type, max size) | W/B | SP | Fiber type | L (mm) | d (µm) | Vf (vol.%) |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 (matrix) | P·O 42.5R | 50% | "mineral admixtures" (type and amount n.r.) | fine river sand; S/B 0.36; max size n.r. | 0.29 | used, dosage n.r. | none | — | — | 0 |
| 2 / 3 / 4 | P·O 42.5R | 50% | same | S/B 0.36 | 0.29 | n.r. | PVA | 12 | 39 | 1.0 / 1.5 / 2.0 |
| 5 / 6 | same | 50% | same | S/B 0.36 | **0.26 / 0.32** | n.r. | PVA | 12 | 39 | 2.0 |
| 7 / 8 | same | **60% / 40%** | same | S/B 0.36 | 0.29 | n.r. | PVA | 12 | 39 | 2.0 |
| 9 / 10 | same | 50% | same | **S/B 0.24 / 0.48** | 0.29 | n.r. | PVA | 12 | 39 | 2.0 |

Units of binder quantities: ratios only (Table 2). "Fly ash content (%)" is presumably a share of
binder; its mass or volume basis is not stated ⚠️. Table 2 here labels the ratio "water-binder", while
the same mixes were labelled "water-cement ratio" in [[deng2015-hdc-compressive-toughness]].

PVA (Table 1): L 12 mm, d 39 µm, L/d about 310 (0.31 × 10³), σ_f 1600 MPa, E 40 GPa, elongation 7%,
density 1.3 g/cm³. Manufacturer and oiling not reported.

## Test methods
- Specimen geometry: prisms 100 × 100 × 300 mm, 3 per mix (p. 2).
- Loading / rate: 500 t microcomputer-controlled electro-hydraulic servo machine, displacement control
  0.5 mm/min (p. 2–3, Fig. 1).
- Measurement: LVDTs between the specimen ends (whole-specimen deformation), TDS602 data logger (p. 2–3).
- Curing & test age: **not reported** ⚠️. If mixes 1–4 are the 2015 tests, they were tested at 10 months.
- Characteristic points (Table 3 notes):
  - σ0, ε0 = peak stress and strain;
  - σ0.2 = 0.2σ0;
  - ε0.85, ε0.5, ε0.2 = post-peak strains at 85/50/20% of σ0.
→ see [[compressive-strength]]

## Key results
| Mix ID | f'c (MPa) | First-crack stress (MPa) | Tensile strength (MPa) | Tensile strain capacity (%) | Crack width (µm) | Other |
|---|---|---|---|---|---|---|
| 1 matrix | 63.06 (prism, σ0) | n/a | not reported | not reported | n/a | ε0 0.213%; no post-peak branch |
| 2 (1% PVA) | 50.28 | n/a | not reported | not reported | n/a | ε0 0.569%; ε0.85/0.5/0.2 0.602/0.667/0.864% |
| 3 (1.5%) | 56.85 | n/a | not reported | not reported | n/a | ε0 0.601%; 0.666/0.695/1.128% |
| 4 (2%, ref.) | 62.25 | n/a | not reported | not reported | n/a | ε0 0.672%; 0.801/0.932/1.407% |
| 5 (W/B 0.26) | 56.04 | n/a | not reported | not reported | n/a | ε0 0.633%; 0.705/0.769/1.116% |
| 6 (W/B 0.32) | 52.84 | n/a | not reported | not reported | n/a | ε0 0.652%; 0.788/0.952/1.276% |
| 7 (FA 60%) | 53.64 | n/a | not reported | not reported | n/a | ε0 0.634%; 0.790/0.947/1.380% |
| 8 (FA 40%) | 64.43 | n/a | not reported | not reported | n/a | ε0 0.561%; 0.641/0.694/0.887% |
| 9 (S/B 0.24) | 51.96 | n/a | not reported | not reported | n/a | ε0 0.648%; 0.814/0.923/1.357% |
| 10 (S/B 0.48) | 56.01 | n/a | not reported | not reported | n/a | ε0 0.556%; 0.605/0.666/0.810% |

All values are means of 3 prisms (Table 3). Peak loads P_m range from 502.78 to 644.32 kN. Age not reported.

Main findings (with Table/Fig. location):
- **Failure mode:** matrix = brittle splitting into several columns. HDC = intact, with one major
  inclined shear crack and slip ("dislocation") across it, plus residual capacity (p. 3, Fig. 2).
  This agrees with Zhou, Pan & Leung 2015 (as cited, ref. [28]).
- **Deformability:** HDC peak strain is 2.61–3.15× the matrix (Table 3: 0.556–0.672% vs 0.213%).
  10–20% residual capacity remains at large strain, while the matrix "immediately loses" capacity (p. 3).
- **Fiber content 1 → 2%:** σ0 rises (50.3 → 62.3 MPa). ε0.85, ε0.5 and ε0.2 rise by 33.06%, 39.73% and
  62.85% (p. 5, Fig. 5a).
  - None of the HDC mixes exceeds the matrix strength except mix 8 (FA 40%, 64.43 MPa).
- **W/B:** strength and ultimate strain both peak at W/B 0.29: 62.25 MPa vs 56.04 at 0.26 and 52.84 at 0.32
  (p. 5, Fig. 5b). The authors attribute the gain from 0.26 to 0.29 to better workability and fiber
  dispersion. → [[water-binder-ratio]]
- **Fly ash 40 → 50 → 60%:** σ0 falls (64.43 → 62.25 → 53.64 MPa). Peak strain rises sharply from 40% to 50%,
  then falls slightly at 60% (p. 5, Fig. 5c).
  - The authors say FA improves the fiber–matrix interface and prevents excessive fiber rupture. They
    recommend a limit to keep strength. → [[fly-ash]]
- **Sand/binder 0.24 → 0.36 → 0.48:** S/B 0.36 is best for both strength and deformability (p. 5, Fig. 5d).
  The authors blame the drop at 0.48 on higher fiber–matrix friction, which ruptures fibers and lowers the
  tensile deformability.
- **Damage constitutive model** (Eqs. 6–10):
  - D = 0 for ε < γ;
  - D = 1 − exp[−((ε − γ)/η)^m] for γ ≤ ε ≤ β;
  - D = D_u for ε > β.
  - σ = E(1 − D)ε, with a constant residual (1 − D_u)σ0 beyond β.
  - m and η come from the boundary conditions (Eqs. 8–9).
- **Fitted parameters** (Table 4, 9 HDC mixes):
  - γ/ε0 = 0.80–0.84 (mean 0.83, CV 0.013);
  - β/ε0 = 1.20–1.43 (mean 1.30, CV 0.060);
  - D at ε0 = 0.03–0.06; D at β = 0.79–0.89 (mean 0.85);
  - m = 2.56–5.78; η = 0.19–0.38 (×10⁻³).
  - Recommended simplification: γ = 0.8ε0 and β = 1.3ε0 (Eq. 10).
- **Fit quality** (Table 4, mean R): new model 0.984, Li & Liu 2014 rational model 0.983,
  Xu et al. 2009 polynomial model 0.958. Fitting coefficients A, B, C1–C4 per specimen are in Table 5.
  - The Li and Xu models decay to zero and miss the residual plateau (Fig. 7).
- **Effect of fiber on the parameters:** as fiber content rises, m falls (5.78 → 2.56) and η rises
  (0.26 → 0.38 ×10⁻³), i.e. more enclosed energy (Table 4, p. 9).

## Mechanisms / explanations offered by authors
- **Lateral restraint by fiber bridging** delays longitudinal cracks (p. 3, Fig. 3). The authors' sequence:
  - once the lateral tensile strain exceeds the ultimate tensile strain of HDC, fibers pull out or rupture;
  - a longitudinal crack then forms at the weakest section and becomes the major (inclined) crack.
- Bridging also delays damage propagation, so D saturates at about 0.85 rather than 1 (p. 9).
- **Fly ash** improves the fiber–matrix interface (less fiber rupture) but lowers strength (p. 5).
- **High sand content** raises fiber–matrix friction, so more fibers rupture (p. 5).

## Limitations (stated + observed)
- Stated: none explicitly.
- Observed:
  - Curing and test age not reported.
  - Fly ash basis and "mineral admixtures" not specified.
  - 3 specimens per mix; one-factor-at-a-time design around mix 4.
  - No tensile test, so the "ultimate tensile strain" explanations are untested here.
  - The model's residual plateau is a constant and the descending branch is very steep (Fig. 7).
  - Mixes 1–4 appear to reuse the 2015 data set. Their peak strains in Table 3 are lower than the 2015
    values: 0.569/0.601/0.672% here vs 0.74/0.67/0.80% in 2015 ⚔️.
  - The matrix peak load is 630.55 kN here vs 640.45 kN in 2015.
  - Fig. 7 curves (e.g. HDC 2-2, peak at about 0.7%) look closer to the 2015 strains than to Table 3 ⚠️.

## Relation to other work
- Agrees with:
  - [[deng2015-hdc-compressive-toughness]]: about 3× peak strain, 10–20% residual capacity, confinement by
    bridging.
  - [[li2021-hdc-sulfate-dry-wet]]: intact, cracked HDC in compression.
- Contradicts:
  - ⚔️ [[deng2015-hdc-compressive-toughness]]: same peak loads for mixes 2–4 but different peak strains
    and matrix load (see Limitations).
  - Here fiber raises σ0 (1 → 2%), but all fiber mixes stay at or below the fiber-free matrix. So the
    statement "σ0 increases with fiber content" holds only within HDC.
- Extends:
  - first compressive constitutive model for HDC in the wiki; complements the tensile models in
    [[tensile-constitutive-model]];
  - first data on W/B, fly ash and sand/binder effects for XAUAT PVA-HDC.

## Pages updated from this source
- [[compressive-strength]]
- [[fly-ash]]
- [[water-binder-ratio]]
- [[pva-fiber]]
- [[fiber-bridging]]
- [[tensile-constitutive-model]]
- [[terminology-hdc-ecc-shcc]]
- [[mix-designs]]
- [[mechanical-results]]

## To verify
- [ ] Curing regime and test age (not stated). Are mixes 1–4 the same specimens as in [[deng2015-hdc-compressive-toughness]] (10 months)? ⚠️ unverified
- [ ] ⚔️ Peak strains of mixes 1–4 differ from the 2015 paper (e.g. mix 2: 0.569% here vs 0.74% there) despite identical peak loads; Fig. 7a shows a peak near 0.7%.
- [ ] Matrix peak load 630.55 kN (here) vs 640.45 kN (2015); σ0 63.06 MPa matches 630.55 kN / 10⁴ mm².
- [ ] Basis of "fly ash content (%)" (share of binder by mass?) and identity and amount of "mineral admixtures".
- [ ] The damage threshold appears as "c" in the extracted text and as "γ" in the conclusions; γ is used here.
- [ ] Units of η: Table 4 header "η (×10⁻³)" (strain units assumed).
