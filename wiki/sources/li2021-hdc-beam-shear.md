---
type: source
slug: li2021-hdc-beam-shear
title: "Shear behavior of high ductile fiber reinforced concrete beams"
authors: [Xuesen Li, Jie Dai, Mingke Deng]
year: 2021            # Alexandria Engineering Journal 60 (2021) 1665–1675; available online 27 Nov 2020 (received 11 Sep, accepted 12 Nov 2020)
venue: "Alexandria Engineering Journal 60 (2021) 1665–1675"
doi: "10.1016/j.aej.2020.11.017"
raw_file: raw/papers/Li2021_HDC-beam-shear.pdf
material_term: "HDC ('high ductile fiber reinforced concrete'), described as 'a member of ECC'; PVA 2 vol.% (12 mm × 39 µm), W/B 0.29, FA/B 0.50; f_cu 70.55 MPa (70.7 mm cubes, 28 d); σ_tu 5.83 MPa, tensile strain capacity 0.968% (dogbone, 28 d). Strain hardening shown (Fig. 1) but ε < 1% (passes the JC/T 2461 0.5% bar, not the ECC > 3% convention). Curing regime not reported"
study_type: experimental + analytical (shear-capacity model calibrated on 52 beams)
tags: [hdc, pva-fiber, xauat, henan-university-of-technology, reinforced-hdc-beam, shear, stirrups, three-point-bending, aci-318, eurocode-2, shear-capacity-model, ductile-shear-failure]
ingested: 2026-10-21
updated: 2026-10-21
---

# Shear behaviour of reinforced HDC beams with stirrups (Li, Dai & Deng, 2021)

## One-paragraph summary
**Experimental + analytical** study from Henan University of Technology (Zhengzhou) with Deng Mingke (XAUAT, Xi'an).
Ten shear-critical beams (120 × 180 mm, h0 150 mm), eight cast **wholly in PVA-HDC** and two RC controls (C50 commercial
concrete, f_cu 75.77 MPa), all **with stirrups**, were loaded in three-point bending at a/d = 1 (series A) and a/d = 2
(series B), varying the stirrup ratio (ρsv 0.40 / 0.59 / 0.79%) and the longitudinal ratio (§2.2, Table 4).
The HDC (W/B 0.29, FA/B 0.50, PVA 2%) had f_cu 70.55 MPa, σ_tu 5.83 MPa and ε_tu 0.968% at 28 d (§2.1).
HDC beams developed many fine diagonal cracks with visible shear slip, no crushing or spalling, and failed in direct shear
(a/d 1), shear compression or shear tension (a/d 2), while the RC controls failed in diagonal compression with crushing and
spalling (§3.1–3.2, Table 6). Peak loads of HDC beams were 471–520 kN (series A) vs 393 kN for RC, and 285–354 kN (series B)
vs 275 kN; deflection at peak was 2.72× (A) and 1.30× (B) that of RC (Table 6, §3.3). ACI 318-14 and EN 1992-1-1 were very
conservative (V_test/V_ACI 2.0–5.3 for the new beams, up to 12.9 for deep beams from earlier XAUAT tests). The authors
modified both codes with a strength coefficient η and an a/d-dependent "ductile coefficient" δ, calibrated on 8 new + 44
literature beams (mean V_M/V_test 1.008, COV 0.161 for modified ACI) (§4, Eqs. 6–9, Table 7).

> Synthesis: this is the wiki's first primary test of **reinforced HDC beams in shear** (members cast wholly in HDC, with
> stirrups). It complements [[deng2018-hdc-short-columns]] (same XAUAT-type PVA-HDC, ε ≈ 1%, columns) and contrasts with the
> strengthening studies [[wang2019-rc-beam-ecc-shear-strengthening]] and [[yuan2020-nshsdc-beam-strengthening]]. As in the
> columns, a PVA-HDC with < 1% tensile strain capacity was enough to change failure from brittle to "ductile shear".

## Objective / research question
- (i) Effectiveness of replacing ordinary concrete by HDC in beams; (ii) cracking pattern and failure mode vs stirrup ratio,
  longitudinal ratio and a/d; (iii) the HDC contribution to shear capacity; (iv) a design formula for reinforced HDC beams that
  accounts for strain hardening and multiple cracking (§1, last paragraph).
- Motivation: earlier work gave only empirical equations without a consistent design approach, and data for high
  reinforcement ratios are scarce (§1).

## Materials & mix design
| Mix ID | Cement | Fly ash | Slag/other | Sand (type, max size) | W/B | SP | Fiber type | L (mm) | d (µm) | Vf (vol.%) |
|---|---|---|---|---|---|---|---|---|---|---|
| HDC | 1 (P·O 42.5) | 1 (Grade I, Henan) | none | river sand (Shaanxi), ≤ 1.18 mm; S/B 0.36 | 0.29 | not reported | PVA (σ_f 1600 MPa, E 40 GPa, elong. 7.0%, density "1.3 g/mm³" ⚠️ = g/cm³) | 12 | 39 | 2.0 |
| RC control | commercial C50 concrete | — | — | — | not reported | not reported | none | — | — | 0 |

Units of binder quantities: mass ratio. Text gives cement : FA : sand : water = 1 : 1 : 0.72 : 0.58, which matches Table 1
(W/B 0.29, S/B 0.36, FA/B 0.50, all by mass of binder; binder = cement + FA) (§2.1, Tables 1–2). FA/C = 1.0 (by mass).
Cement "specific surface area 4.41 m²/kg" as printed ⚠️ (implausible unit; probably 441 m²/kg or 4.41 × 10² m²/kg).

Reinforcement (Table 3): stirrups φ6 (f_y 392, f_u 581 MPa); longitudinal C18 / C20 / C22 / C25 (f_y 443 / 423 / 445 / 437 MPa;
f_u 595 / 585 / 613 / 605 MPa); two D8 hanger bars; longitudinal bars end in 90° hooks.

## Test methods
- **Material:** per batch, 3 dogbones (uniaxial tension) and 3 × 70.7 mm cubes, tested at 28 d (§2.1). Dogbone drawing (Fig. 2):
  15 mm thick, 50 mm narrow width, ends 80 mm wide; a "150" dimension appears to be the narrow (gauge) length and the overall
  length is labelled "1000" ⚠️ (drawing illegible/implausible). The section (50 × 15 mm, 80 mm ends) matches the XAUAT
  350 mm dogbone used in [[zhang2022-hdc-basalt-textile-tension]] (Fig. 2) and [[yang2024-hshdc-uniaxial-tension]].
  Loading rate and strain measurement not reported.
  RC control: 3 × 100 mm cubes at 28 d.
- **Beams:** 10 simply supported beams, b × h = 120 × 180 mm, h0 150 mm, cover to bar centre 30 mm, overhang 125 mm;
  a/d = 1 (series A, shear span 150 mm ⚠️ "flexural-shear length" 300 mm) and a/d = 2 (series B, 600 mm) (§2.2, Table 4, Fig. 3).
  RC beams designed to ACI 318-14 to fail in shear.
  | ID | Material | a/d | Longitudinal | Stirrups |
  |---|---|---|---|---|
  | SE-1a / SE-1 / SE-1b | HDC | 1 | 2C20 | φ6@80 / @60 / @120 |
  | SE-1c | HDC | 1 | 2C22 | φ6@80 |
  | SC1 | RC | 1 | 2C20 | φ6@80 |
  | SE-2a / SE-2 / SE-2b | HDC | 2 | 2C25 | φ6@80 / @60 / @120 |
  | SE-2c | HDC | 2 | 2C25 + 1C18 | φ6@80 |
  | SC2 | RC | 2 | 2C25 | φ6@80 |
  - Stated ratios: ρsv = 0.79 / 0.59 / 0.40% (@60 / @80 / @120; consistent with 2φ6 / (b·s), computed); ρ = 4.55% (series B)
    and 5.73% (SE-2c) (§2.2). These equal A_s/(b·h) (computed: 2C25 → 4.55%, 2C25+1C18 → 5.72%, 2C20 → 2.91%, 2C22 → 3.52%),
    not A_s/(b·h0).
- **Loading / rate:** three-point bending, 1000 kN MTS servo-hydraulic frame; steel plates 200 × 120 × 10 mm on fine sand at
  supports and load point (§2.3, Fig. 4). Loading rate not reported.
- **Measurement:** mid-span displacement transducer; strain gauges on longitudinal bars and at mid-height of selected stirrups;
  first flexural and first inclined cracks by naked eye (§2.3). No crack-width measurement.
- **Curing & test age:** 28 d for material tests; curing regime and beam test age not reported.
→ [[dogbone-uniaxial-tension]] · [[shear-behaviour]]

## Key results
| Mix ID | f'c (MPa) | First-crack stress (MPa) | Tensile strength (MPa) | Tensile strain capacity (%) | Crack width (µm) | Other |
|---|---|---|---|---|---|---|
| HDC (PVA 2%) | f_cu 70.55 (70.7 mm cube, 28 d) | not reported (Fig. 1 shows first crack ≈ 4.5–5 MPa ⚠️ read) | 5.83 (§2.1); "5.68" in Conclusion 1 ⚔️ | 0.968 (§2.1, Conclusion 1; basis — peak or ultimate — not stated ⚠️) | not reported | Fig. 1: three curves end at ≈ 0.75–0.97% strain (read) |
| RC control (C50) | f_cu 75.77 (100 mm cube, 28 d) | — | — | — | — | — |

Beam results (Table 6; loads are total applied loads, V = P/2):
| Beam | First crack (kN) | Long. yield (kN) | Stirrup yield (kN) | P_max (kN) | δ at P_max (mm) | V/(√f'c·bd) | V/V_ACI | V/V_EN | Mode |
|---|---|---|---|---|---|---|---|---|---|
| SE-1a | 119 | 172 | 187 | 497 | 2.48 | 1.91 | 3.93 | 2.14 | DS |
| SE-1 | 140 | 369 | 459 | 519 | 2.70 | 2.00 | 3.37 | 1.84 | DS |
| SE-1b | 130 | 497 | 373 | 520 | 3.92 | 2.00 | 5.27 | 2.85 | DS |
| SE-1c | 165 | 500 | 419 | 471 | 2.42 | 1.82 | 3.75 | 2.04 | DS |
| SC1 (RC) | 149 | 343 | 373 | 393 | 0.99 | 1.41 | 3.04 | 1.67 | DC |
| SE-2a | 131 | 189 | 146 | 285 | 4.02 | 1.12 | 2.30 | 2.51 | SC |
| SE-2 | 157 | – | 234 | 326 | 5.30 | 1.28 | 2.16 | 2.36 | SC |
| SE-2b | 91 | 269 | 196 | 354 | 4.29 | 1.39 | 3.66 | 3.97 | ST |
| SE-2c | 89 | 242 | 273 | 352 | 4.97 | 1.39 | 2.87 | 3.12 | SC |
| SC2 (RC) | 89 | 143 | 148 | 275 | 3.09 | 0.94 | 2.01 | 1.87 | DC |

DS = direct shear, DC = diagonal compression, SC = shear compression, ST = shear tension.

Main findings (with Table/Fig. location):
- **Failure mode:** RC controls failed in diagonal compression with crushing and spalling; HDC beams failed in DS (a/d 1),
  SC (a/d 2) or ST (SE-2b, fewest stirrups), with many fine cracks near the inclined crack, visible shear slip, no crushing or
  spalling, higher residual capacity and "better integrity" (§3.1–3.2, Figs. 5–6, Table 6).
- **Cracking vs peak:** HDC first flexural/diagonal cracking occurred at about 70–80% of the RC cracking load, but peak load
  was 1.85–3.18× the first inclined-cracking load (§3.1). SC1: first flexural 86 kN, inclined 149 kN, peak 393 kN (+164%).
- **Peak load and stiffness:** HDC beams had 7–60% higher yield loads and 11–38% higher peak load than the controls (§3.3) ⚠️
  (Table 6 gives +20–32% for series A and +4–29% for series B, computed). Pre-cracking stiffness rose with stirrups and fell
  with a/d (§3.3, Fig. 7).
- **Deformation:** deflection at peak ≥ 2.70 mm (A) and ≥ 4.02 mm (B), 2.72× and 1.30× the RC beams (§3.3) ⚠️ (SE-1a 2.48 and
  SE-1c 2.42 mm are below 2.70, Table 6). Conclusion 2 gives +30–172%.
- **Reinforcement yielding:** HDC beams reached rebar yield at loads 12–84% higher than RC, even with fewer stirrups, and gained
  > 25% load after yielding (§3.4). Almost all stirrups crossing the critical crack yielded in series A (§3.2).
- **Normalised shear stress:** series A stayed ≈ 1.82–2.00 regardless of stirrups or longitudinal steel → the authors infer the
  section-size upper limit was reached (§3.5, §3.2). Series B: −14% then +24% as ρsv rose 0.40 → 0.79%; +24% when ρ rose
  2.91 → 5.73% (§3.5) ⚠️ (series B nominal ρ is 4.55%, Fig. 8 labels mix 2.91%). Overall "11–38% higher" than RC (§3.5);
  abstract: average +19%, maximum +40%.
- **Stirrups:** more stirrups did not always give more capacity (SE-2b with φ6@120 carried 354 kN vs 285 kN for SE-2a @80)
  (Table 6, Conclusion 2).
- **Code checks** (new beams + 44 earlier beams from Deng et al., Zhang, Lu, Yang, Hou; Table 6 "prior tests", Table 7):
  ACI 318 and EN 1992 test/model ratios mostly > 2.0; ACI up to 12.88 for deep HDC beams (Deng et al. E-75); EN "more stable"
  but highly redundant (§4.2, Fig. 9). Test/model ratios rise with ρ → longitudinal steel contributes more in HDC than RC beams.
  Beams without stirrups had higher ratios than beams with stirrups.
- **Modified models** (§4.3, Eqs. 6–9):
  - V_M,ACI = 0.166·η·δ_ACI·√f'c·b·d + f_yv·A_sv·d/s, with δ_ACI = 0.61λ² − 4.56λ + 10.23;
  - V_M,EN = C_Rd,c·k·η·δ_EN·(100ρf_ck)^(1/3)·b·d + 0.9·A_sv·f_yv·d/s, with δ_EN = −0.27λ² + 0.58λ + 3.16;
  - η = (f_t^H/f_c^H)/(f_t^C/f_c^C) (ratio of tension/compression strength ratios of HDC and concrete); λ = a/d (printed as
    "k" in the extracted text ⚠️); f'c = 0.79 f_cu,k (ACI), f_ck = f_cu,k/1.226 (EN).
  - Accuracy: V_M,ACI/V_test within ±20%, mean 1.008, COV 0.161; V_M,EN/V_test within ±30%, mean 0.969, COV 0.168 (§4.3,
    Fig. 11). Conclusion 3 merges these as "within 30%, 1.008, 0.168".

## Mechanisms / explanations offered by authors
- Tensile strain hardening and fibre bridging across inclined cracks carry tension in the web, so the beam keeps load after
  the critical crack and the stirrups are used more fully ("tight bearing system") (§3.1, §3.3–3.4).
- Series A capacity is governed by the composite strength of HDC under shear + compression; deformability by the ultimate
  tensile and compressive strains of HDC. Shear-tension (SE-2b) capacity is governed by HDC tensile strength and ultimate strain (§3.2).
- Stirrups confine diagonal cracks, so beams without web reinforcement gain relatively more from HDC (§4.2).
- Cited (not tested here): ECC shear strength exceeds its direct tensile strength by up to 50% (refs 29–30, as cited, §1);
  HDC with "slightly lower tensile strain" is desirable for cost in reinforced members (refs 35–38, as cited, §1).

## Limitations (stated + observed)
- Stated: a larger database is needed to quantify trends with a/d, ρ and ρsv (§4.2).
- One beam per configuration; only two RC controls; RC concrete (f_cu 75.77 MPa, 100 mm cubes) and HDC (70.55 MPa, 70.7 mm
  cubes) were tested on different cube sizes.
- Several internal inconsistencies: σ_tu 5.83 (§2.1) vs 5.68 MPa (Concl. 1); SE-1a peak "519 kN" in §3.1 vs 497 kN in Table 6
  (519 kN is SE-1); "7–60%" and "11–38%" gains not reproducible from Table 6; Fig. 8 beam labels (RD1-x, ρL 2.91%) do not match
  Table 4 IDs or the stated series-B ρ (4.55%); Table 5 is cited but the failure modes appear in Table 6; two tables are numbered 6.
- Tensile strain basis (peak vs ultimate), dogbone geometry, loading rate and curing regime not reported; no crack widths.
- The ductile coefficient δ is a pure regression on a/d (Fig. 10) and partly calibrated on the authors' own group's tests
  (16 "Deng et al." beams), so the model is not independently validated.
- The literature beams cover f_c 45.7–70.6 MPa and f_t 3.55–6.34 MPa (Table 6 "prior tests"); the source materials of the
  44 beams (fibre, Vf) are not given.

## Relation to other work
- Agrees with: [[deng2018-hdc-short-columns]] — same type of XAUAT PVA-HDC (W/B 0.29, 2% PVA, ε ≈ 1.0%, σ_tu 6.14 MPa there vs
  0.968% and 5.83 MPa here); both report dense fine diagonal cracking, no spalling, "ductile shear" failure and very conservative
  codes (there GB 50010 1.08–1.26, ACI 1.40–2.08; here ACI 2.0–5.3, EN 1.8–4.0 for the new beams). Good member shear does not
  require ECC-level (> 3%) tensile ductility.
- Agrees with: [[wang2019-rc-beam-ecc-shear-strengthening]] and [[yuan2020-nshsdc-beam-strengthening]] that strain-hardening
  composites raise shear capacity and change failure mode; differs in that here the whole beam is HDC and stirrups are present.
- Contradicts: ⚔️ "stirrup ratio has little influence" (series A) and the non-monotonic series B trend sit against the
  conventional additive stirrup term V_s used in their own modified models (Eqs. 6, 8) — internal tension, not a cross-source conflict.
- Extends: [[shear-behaviour]] with the first reinforced-HDC beam data set (a/d 1–2, ρsv 0.40–0.79%) and a modified ACI/EN
  formula; [[kanakubo2006-dfrcc-tensile-test-method]]'s JCI remark that tensile deformation capacity is "not an important factor"
  for member shear is consistent with good shear performance at ε < 1%.

## Pages updated from this source
- [[shear-behaviour]] · [[rc-member-strengthening]] · [[unreinforced-hdc-structures]] · [[tensile-strain-capacity]] ·
  [[dogbone-uniaxial-tension]] · [[pva-fiber]] · [[fly-ash]] · [[terminology-hdc-ecc-shcc]] · [[fiber-bridging]] ·
  [[mix-designs]] · [[mechanical-results]] · [[deng2018-hdc-short-columns]]

## To verify
- [ ] σ_tu: 5.83 MPa (§2.1) vs 5.68 MPa (Conclusion 1); and whether 0.968% is strain at peak or ultimate (Fig. 1 curves end ≈ 0.75–0.97%).
- [ ] Dogbone geometry in Fig. 2 (overall length printed "1000"; gauge 150 mm?; section 50 × 15 mm?).
- [ ] SE-1a peak: 497 kN (Table 6) vs 519 kN (§3.1 text).
- [ ] "7–60% higher yield loads" and "11–38% higher peak load / normalised stress" (§3.3, §3.5, Concl. 2) vs Table 6 (computed +4–32% peak; normalised +19–48%).
- [ ] Series-B longitudinal ratio: 4.55% (§2.2) vs ρL = 2.91% labels in Fig. 8; Fig. 8 IDs (RD/LRD) vs Table 4 IDs (SE).
- [ ] Curing regime and age at beam testing (not reported).
- [ ] Cement specific surface "4.41 m²/kg" (unit).
- [ ] Symbol of a/d in Eqs. 7 and 9 (extracted as "k"; assumed λ = a/d per Fig. 10 axis).
