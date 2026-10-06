---
type: source
slug: ye2021-uhdc-flexural-size-effect
title: "Flexural size effect of ultra-high ductile concrete under different damage and ductility levels"
authors: [Junhong Ye, Jiangtao Yu, Can Cui, Yichao Wang]
year: 2021   # volume year (Cem. Concr. Compos. 115, 2021); online 21 Oct 2020
venue: "Cement and Concrete Composites, 115 (2021) 103852"
doi: "10.1016/j.cemconcomp.2020.103852"
raw_file: raw/papers/Ye2020_Flexural size effect of ultra-high ductile concrete under different damage.pdf
material_term: "UHDC (ultra-high ductile concrete); authors describe it as a PE-fiber ECC"
study_type: experimental (+ analytical size-effect fitting)
tags: [size-effect, flexure, notched-beam, three-point-bending, fracture-toughness, fpz, pe-fiber, fly-ash, uhdc, ecc, tongji]
ingested: 2026-10-06
updated: 2026-10-06
---

# Flexural size effect of UHDC (Ye et al., 2020)

## One-paragraph summary
Tongji University (Shanghai) group. 64 geometrically similar notched beams (depth 40–150 mm,
d/s = 0.44) were tested in three-point bending. The test matrix had three materials: a plain
fly-ash mortar "NC" reference (0% fiber), UHDC-1 (1 vol.% PE) and UHDC-2 (2 vol.% PE), and two
notch/depth ratios ("damage levels", α = 0.10 and 0.23). The NC and UHDC-1 nominal flexural
strengths fall as size increases, and their data follow Bažant's size effect law (SEL). UHDC-2
keeps about 20 MPa at every size and notch depth. Its K_IC rises with size (about 3.4–10.1 MPa·m^1/2),
and the fitted D0 and β are negative, so SEL does not apply to it. The authors explain this
with an enlarged fracture process zone: D_pz is 1.79–24.48 mm for UHDC and below 0.1 mm for NC.
They conclude that a Type-I (strength-based, Weibull) size-effect approach suits UHDC-2 better
(Abstract; Tables 3–5; Conclusions, p. 9).

## Objective / research question
Find out how specimen size, initial notch depth ("damage level") and ductility level (fiber
content 0/1/2 vol.%) affect the flexural (Type-II) size effect of UHDC. Then explain the result
with fracture toughness and FPZ size (p. 3, end of §1).

## Materials & mix design
| Mix ID | Cement | Fly ash | Slag/other | Sand (type, max size) | W/B | SP | Fiber type | L (mm) | d (µm) | Vf (vol.%) |
|---|---|---|---|---|---|---|---|---|---|---|
| NC | 711.6 (P·II 52.5) | 853.9 (Class F) | none | 569.3, silica sand, mean 0.11 mm, max 0.25 mm | 0.252 (394.5/1565.5, by mass; computed by wiki) | HRWR 4.8 | none | n/a | n/a | 0 |
| UHDC-1 | 711.6 | 853.9 | none | 569.3, same | 0.252 (computed) | 4.8 | PE (high-modulus, high-strength) | not reported (see Yu et al. 2017, ref. [26]) | not reported (ref. [26]) | 1 (10 kg/m³) |
| UHDC-2 | 711.6 | 853.9 | none | 569.3, same | 0.252 (computed) | 4.8 | PE | not reported | not reported | 2 (20 kg/m³) |

Units of binder quantities: kg/m³ (Table 1, p. 3). Derived mass ratios (computed by the wiki, not
stated by the authors): FA/C = 1.20, sand/binder = 0.36, water/cement = 0.554,
HRWR/binder = 0.0031. Fibers were dosed "by volume fraction" (p. 3). 10 kg/m³ ↔ 1 vol.% implies an
assumed fiber density of about 1000 kg/m³ (inference).
- **"NC" is not normal concrete in the usual sense.** It is the same fly-ash/silica-sand
  mortar matrix with no fiber and no coarse aggregate (Table 1). The authors call it "normal concrete".
- The mix comes from the authors' earlier work (Yu et al. 2017, "SHCC with tensile capacity up to
  8%", ref. [26]) (p. 3).
- Mixing: 20 L mixer. Dry powders 2 min, then water + HRWR, then fibers added by hand and mixed
  3 min. Cast by hand without vibration (p. 3).

## Test methods
- **Uniaxial tension:** JSCE dogbone. Fig. 4a shows a total length of 330 mm, end width 60 mm,
  thickness 13 mm and an 80 mm gauge (core) length. 2 LVDTs, MTS CMT4204 (300 kN), 2 mm/min
  (§2.3, p. 3; Fig. 4, p. 4). → [[dogbone-uniaxial-tension]]
- **Flexure:** three-point bending of **notched** beams (Type-II size effect).
  - b × d × s = 40×40×91, 70×70×159, 100×100×227 and 150×150×341 mm, d/s = 0.44 for all.
  - Saw-cut mid-span notch, α = a/d = 0.10 or 0.23.
  - n = 2–3 per series, 64 beams in total (Table 2, p. 5). NC was not tested at 70 mm according to Table 2.
  - Same MTS machine, 2 mm/min.
  - CTOD measured with a clip gauge on L-shaped steel sheets across the notch tip.
  - DIC used for crack observation (§2.4, p. 3; Figs. 5–6, p. 4).
  - The cast bottom face was the tension face (p. 3).
  → NEW [[notched-beam-three-point-bending]] (compare [[flexural-strength]])
- **Data reduction:**
  - Nominal flexural strength f_n = c_n·P/(bd), with c_n = 3s/[2d(1−α/d)²] as printed
    (from ref. [42]; p. 5). ⚠️ unverified: the printed expression is dimensionally odd, and it
    probably means (1−α)².
  - K_IC from Xu & Reinhardt's simplified double-K method (Eqs. 3–7), with f(V_h) adjusted for
    d/s = 0.44 using Wallin's correction (Eq. 8) (pp. 6–7).
  - FPZ diameter D_pz ≈ K_IC²/(π σ_f²), with σ_f = **compressive** strength, following the
    Ashby approach (p. 7).
  - Bažant SEL fitted by linear regression of (f′t/σ_n)² against D (Eqs. 9–11, p. 8).
- **Measurement:** LVDTs (tension), clip gauge (CTOD), DIC.
- **Curing & test age:** 1 d in air in the moulds, then "cured for another 27 days before
  testing" (conditions not reported), so the test age is 28 d (p. 3).

## Key results
| Mix ID | f'c (MPa) | First-crack stress (MPa) | Tensile strength (MPa) | Tensile strain capacity (%) | Crack width (µm) | Other |
|---|---|---|---|---|---|---|
| NC | 45.2 (from Wang & Yu 2019, ref. [34]; specimen not reported) | not reported | not reported | not reported ("two orders" lower than UHDC, p. 3) | not reported | f_n 3.65–7.13 MPa; K_IC 0.62–0.86 MPa·m^1/2; D_pz 0.06–0.12 mm |
| UHDC-1 | 37.7 (ref. [34]) | not reported (Fig. 4b, about 4–5 ⚠️ unverified, read from graph) | about 7 (read from Fig. 4b ⚠️ unverified) | **4.31** (strain capacity; text, p. 3) | not reported | f_n 10.00–21.56 MPa; K_IC 2.81–4.94; D_pz 1.78–5.51 mm |
| UHDC-2 | 36.4 (ref. [34]) | not reported (about 4–5 from Fig. 4b ⚠️) | about 9.5–9.7 (read from Fig. 4b ⚠️ unverified) | **9.45** (text, p. 3) | not reported | f_n 18.27–22.11 MPa; K_IC 3.41–10.08; D_pz 2.83–24.48 mm |

Strain values in Fig. 4b are plotted as decimals (0.1 = 10%). Whether 4.31% and 9.45% are taken at
peak stress or at ultimate is not stated. From the curves, they appear to be at peak stress
(⚠️ unverified).

### Table 3 (p. 6): mean ± SD of peak load P, CTOD at peak, f_n, energy dissipated in stage 2
| Series | d (mm) | P (kN) | CTOD (mm) | f_n (MPa) | E_2nd (kN·mm) |
|---|---|---|---|---|---|
| NC α=0.23 | 40 / 70* / 100* | 1.88 / 7.73 / 15.04 | 0.02 | 6.66 / 4.52 / 3.65 | – |
| NC α=0.10 | 40 / 70* / 100* | 2.71 / 15.22 / 27.93 | 0.02 | 7.13 / 6.34 / 4.99 | – |
| UHDC-1 α=0.23 | 40/70/100/150 | 4.73 / 11.93 / 18.68 / 43.93 | 0.77 / 0.83 / 0.81 / 1.40 | 16.81 / 13.94 / 10.91 / 10.68 | 4.77 / 16.66 / 25.53 / 111.07 |
| UHDC-1 α=0.10 | 40/70/100/150 | 8.19 / 14.05 / 23.99 / 63.12 | 0.83 / 0.81 / 0.83 / 0.87 | 21.56 / 12.06 / 10.00 / 11.27 | 7.74 / 18.74 / 28.92 / 145.05 |
| UHDC-2 α=0.23 | 40/70/100/150 | 5.23 / 15.63 / 37.83 / 82.38 | 3.54 / 3.67 / 5.31 / 5.42 | 18.56 / 18.27 / 22.11 / 20.02 | 22.67 / 118.75 / 339.97 / 824.61 |
| UHDC-2 α=0.10 | 40/70/100/150 | 7.25 / 24.29 / 50.09 / 117.96 | 5.54 / 5.66 / 6.61 / 6.81 | 19.09 / 20.85 / 20.87 / 21.06 | 38.91 / 246.77 / 448.12 / 801.71 |

\* ⚠️ The NC sizes in Table 3 (40/70/100) do not match Table 2 and Table 5 (40/100/150).
A wiki back-calculation with f_n = c_n·P/(bd) reproduces the NC f_n values only if the
"70" and "100" rows are really the 100 and 150 mm beams. For example, NC α=0.23 with P = 7.73 kN
and d = 100 gives about 4.4 MPa, against 4.52 reported. Treat the NC sizes as 40/100/150 (⚠️ unverified).
SDs are omitted here for brevity; see Table 3.

### Table 4 (p. 7): K_IC (MPa·m^1/2) and D_pz (mm) by d = 40 / 70 / 100 / 150
| Series | K_IC | D_pz |
|---|---|---|
| NC α=0.23 (sizes as printed: 40/70/100) | 0.63 / 0.68 / 0.67 | 0.06 / 0.07 / 0.07 |
| NC α=0.10 (as printed) | 0.62 / 0.86 / 0.75 | 0.06 / 0.12 / 0.09 |
| UHDC-1 α=0.23 | 2.92 / 3.14 / 2.81 / 3.37 | 1.92 / 2.24 / 1.78 / 2.54 |
| UHDC-1 α=0.10 | 4.67 / 3.82 / 3.49 / 4.94 | 5.03 / 3.30 / 2.75 / 5.51 |
| UHDC-2 α=0.23 | 3.41 / 4.25 / 6.06 / 7.28 | 2.83 / 4.34 / 8.85 / 12.79 |
| UHDC-2 α=0.10 | 4.67 / 6.25 / 7.56 / 10.08 | 5.30 / 9.54 / 13.85 / 24.48 |

Average effective crack lengths a_c are also given in Table 4: 4–30 mm for NC and 25.7–116.6 mm for UHDC.

### Table 5 (p. 8): Bažant SEL fit, σ_n = B f′t / √(1 + D/D0), β = D/D0
| Series | B | D0 (mm) | β at D = 40 / 70 / 100 / 150 |
|---|---|---|---|
| NC α=0.23 | 18.57 | 5.80 | 6.90 / – / 17.24 / 25.86 |
| NC α=0.10 | 9.76 | 52.50 | 0.76 / – / 1.90 / 2.86 |
| UHDC-1 α=0.23 | 35.36 | 11.40 | 3.50 / 6.13 / 8.75 / 13.13 |
| UHDC-1 α=0.10 | 18.90 | 70.00 | 0.57 / 1.00 / 1.43 / 2.14 |
| UHDC-2 α=0.23 | 17.96 | −620.00 | −0.06 / −0.11 / −0.16 / −0.24 (SEL equation not given) |
| UHDC-2 α=0.10 | 19.25 | −675.00 | −0.06 / −0.06 / −0.10 / −0.22 |

The value of f′t used in the fit is not reported (⚠️). Bažant thresholds as quoted by the
authors: β < 0.1 means ductile (strength criterion governs), and β > 10 means brittle (LEFM governs)
(p. 1).

Main findings (with Table/Fig. location):
- **Failure modes (§3.1, Figs. 7–9, p. 3–4):**
  - NC: brittle single crack.
  - UHDC-1: several fine cracks at the notch tip, then one critical crack. The authors call this
    "weak fracture-hardening".
  - UHDC-2: multiple fine cracks around the notch tip, with load rising as the cracks spread.
    The authors call this "strong fracture-hardening".
  - All three types end with a fracture-softening stage.
- **Load–CTOD curves (Fig. 10, p. 6):** three parts (elastic, fracture-hardening,
  fracture-softening). The elastic part is very short. NC curves were not recorded because
  NC failed abruptly.
- **CTOD at peak:** 0.02 mm (NC), 0.77–1.40 mm (UHDC-1) and 3.54–6.81 mm (UHDC-2) (Table 3).
- **Size effect on f_n (Table 3, Fig. 11, p. 5):**
  - NC: f_n falls with size.
  - UHDC-1: f_n falls with size, from 16.81 to 10.68 MPa at α = 0.23.
  - UHDC-2: f_n stays at about 20 MPa (18.27–22.11) and rises slightly with size.
  - The authors conclude that UHDC-2 is "insensitive to specimen size and pre-damage" (p. 5).
- **Notch depth ("damage level"):**
  - UHDC-2: little effect on f_n.
  - NC and UHDC-1: a deeper notch lowers f_n (Table 3).
  - K_IC of UHDC-1 and UHDC-2 is slightly lower at α = 0.23. NC is unaffected (p. 7).
- **Fracture toughness (Table 4, p. 7):**
  - UHDC-2 K_IC is about an order of magnitude higher than NC.
  - For NC and UHDC-1, K_IC does not depend on size.
  - For UHDC-2, K_IC **increases** with size, from 4.67 to 10.08 MPa·m^1/2 at α = 0.10.
- **FPZ:**
  - D_pz is below 0.1 mm for NC and 1.79 (as written in the text; Table 4 minimum 1.78) to
    24.48 mm for UHDC (p. 7).
  - On an Ashby K_IC–strength chart, UHDC plots in the overlap of metals, polymers and natural
    materials (bamboo, wood) (Fig. 12, p. 8).
- **SEL (Table 5, Figs. 13–14, p. 8):**
  - NC and UHDC-1 follow Bažant SEL (one point deviates). NC plots on the LEFM side and UHDC-1
    in the transition zone.
  - UHDC-2 gives negative D0 and β, so log β is undefined and the data lie near the horizontal
    (strength-criterion) asymptote.
  - The authors suggest using Type-I (Weibull) size effect for UHDC-2.
- **Energy:** energy dissipated in stage 2 is much larger for UHDC-2. At 150 mm, α = 0.23, it is
  824.61 kN·mm, against 111.07 kN·mm for UHDC-1 (Table 3).

## Mechanisms / explanations offered by authors
- Fiber bridging by PE fibers causes multiple cracking at the notch tip, which spreads damage
  over a wider zone. The "localized failure mode was avoided" in UHDC-2 (p. 4).
- The FPZ (macro-crack zone plus micro-crack zone) grows by orders of magnitude with fibers.
  When D_pz is no longer negligible against the structural size, the energy-based (Type-II)
  size effect fades. Larger D_pz goes with smaller β (pp. 7–8).
- The authors attribute the higher K_IC to energy absorbed by multiple cracks (p. 7).
- Using a K_IC–strength (Ashby) argument, the authors support the idea from refs. [31, 32] that
  UHDC "with sufficient strength" could be used without steel reinforcement (p. 7).
- Stated by the authors: matrix strength, not fiber bridging, controls the end of the elastic
  stage (p. 3).

## Limitations (stated + observed)
- **Stated:** the size range is only 40–150 mm. At "extremely large" sizes, UHDC may again
  show a size effect. The authors call for meter-scale tests and Type-I/Weibull studies (p. 9).
- **Observed (wiki):**
  - "NC" is a fiber-free mortar (no coarse aggregate), so it is not representative normal concrete.
  - f′c values come from another paper (ref. [34]), not from this test programme.
  - Fiber geometry and properties are not reported (they are in ref. [26]).
  - Curing conditions after demoulding are not reported.
  - Tensile strength and first-crack strength are shown only graphically (Fig. 4b, n = 2 per mix).
  - The NC size labels are inconsistent between Tables 2/5 and Tables 3/4 (see ⚠️ above).
  - The c_n expression as printed looks garbled.
  - Notched three-point bending of a strain-hardening material does not satisfy the LEFM
    assumptions behind the K_IC (double-K) method and Ashby's D_pz. The K_IC values are
    "apparent" toughness, not material constants. This is also why UHDC-2's K_IC depends on size.
  - D_pz is computed from compressive strength, not tensile strength.
  - Unvibrated hand casting with trapped air (p. 3) may add scatter.
  - 2–3 specimens per series.

## Relation to other work
- **Agrees with:** Lepech & Li (2004, as cited, ref. [43]), who found an inappreciable size
  effect in unnotched PVA-ECC beams (Type-I) (p. 3).
- **Contradicts:** ⚔️ Kim et al. and Reineck & Frettlöhr (refs. [38, 39], as cited) report a
  significant flexural size effect in UHPC. Spasojevic, Wille & Parra-Montesinos and Mahmud et al.
  (refs. [40–42], as cited) report a reduced one (p. 3). The authors attribute this disagreement
  to differences in size range, ductility, and test method (3- vs 4-point, notched vs unnotched).
- **Extends:** Wiki cross-reference.
  - This is the first wiki source on **size effect** and on **notched-beam fracture** of a
    strain-hardening composite.
  - Like [[hshdc]] (Ranade et al. 2013 "Composite properties of HSHDC" (ACI MJ 110(4); not a wiki source)), it uses PE fiber at 2 vol.%.
    However, it uses a normal-strength, high-volume fly ash matrix with f'c about 36 MPa
    (vs 166 MPa) and no heat curing.
  - Its reported ε_tu of 9.45% is much higher than the 3.4–4.2% reported for HSHDC.
  - Its flexural test (notched three-point bending, nominal f_n) is not comparable with the
    unnotched ASTM C1609 MOR of HSHDC (31.8 MPa).
- Terminology: the authors present UHDC as an ECC made with "specially-chosen" PE fibers by
  Yu et al., with tensile strain capacity "up to 12%" (refs. [26–34], p. 2). They give it the
  name "ultra-high ductile concrete" because its deformability reaches the steel-bar level of
  ISO and Chinese codes (p. 2). This is a third Chinese lineage (Tongji, PE-based). It is
  distinct from Xi'an "HDC" (PVA) and from Michigan "HSHDC" (PE + VHSC).

## Pages updated from this source
- [[flexural-strength]] (add notched 3PB nominal strength, size-insensitivity of UHDC-2)
- [[tensile-strain-capacity]] (4.31% / 9.45% at 1 / 2 vol.% PE)
- [[compressive-strength]] (36.4–45.2 MPa, cited from ref. [34])
- [[terminology-hdc-ecc-shcc]] (add UHDC, Tongji PE lineage)
- [[pe-fiber]] · [[multiple-cracking]] · [[fiber-bridging]] · [[strain-hardening]]
- [[matrix-fracture-toughness]] (K_IC of NC vs UHDC)
- [[dogbone-uniaxial-tension]] (JSCE dogbone, 80 mm gauge, 2 mm/min)
- [[flexural-strength]] (cross-link to notched 3PB)
- NEW [[size-effect]] (Weibull, Bažant SEL, Type-I/II, FPZ)
- NEW [[uhdc]] (ultra-high ductile concrete, Tongji PE-ECC)
- NEW [[fracture-process-zone]]
- NEW [[notched-beam-three-point-bending]]
- NEW [[fly-ash]] (high-volume FA, FA/C 1.2)
- [[mix-designs]] · [[mechanical-results]] · [[gaps]]

## To verify
- [ ] NC beam sizes: Table 3/4 rows labelled 70 and 100 mm vs Table 2/5 sizes 100 and 150 mm.
      The back-calculation suggests 100/150 (pp. 5–8).
- [ ] The printed c_n = 3s/[2d(1−α/d)²] (p. 5). It probably means (1−α)². The wiki
      back-calculation with (1−α)² reproduces most f_n values to within about 5%.
- [ ] Tensile strength and first-crack stress of UHDC-1 (about 7 / 4–5 MPa) and UHDC-2
      (about 9.5–9.7 / 4–5 MPa), read from Fig. 4b only.
- [ ] Is ε_tu (4.31%, 9.45%) at peak stress or at ultimate? Not stated.
- [ ] PE fiber L, d, strength and modulus are not in this paper. Check Yu et al. 2017 (CBM 137:410–419, ref. [26]).
- [ ] Curing conditions for days 2–28 are not reported. Tension test age is assumed to be 28 d.
- [ ] f′t value used in the SEL fit (Eq. 9) is not reported.
- [ ] Year convention: online 2020, issue 2021 (vol. 115). The slug uses 2020 to match the raw file name.
- [ ] Fiber density implied by 10 kg/m³ = 1 vol.% (about 1000 kg/m³) vs the typical PE value of about 970 kg/m³.
