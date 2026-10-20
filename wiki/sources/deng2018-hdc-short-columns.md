---
type: source
slug: deng2018-hdc-short-columns
title: "Seismic Performance of High-Ductile Fiber-Reinforced Concrete Short Columns"
authors: [Mingke Deng, Yangxi Zhang]
year: 2018            # vol. 2018; received 30 Aug 2017, published 28 Feb 2018
venue: "Advances in Civil Engineering, vol. 2018, Article ID 3542496, 11 pp. (Hindawi)"
doi: "10.1155/2018/3542496"
raw_file: raw/papers/Deng2018_HDC-short-columns.pdf
material_term: "HDC = high-ductile fiber-reinforced concrete (FRCC 'like' ECC and HPFRCC)"
study_type: experimental (structural, reversed cyclic lateral load) + code-based shear analysis
tags: [structural, seismic, short-column, shear, cyclic-loading, pva, xauat, deng-group]
ingested: 2026-10-20
updated: 2026-10-20
---

# Seismic performance of HDC short columns (Deng & Zhang, 2018)

## One-paragraph summary
XAUAT tested seven 250 × 250 mm short columns under constant axial load and reversed cyclic lateral
load: one RC control and six columns cast **entirely in PVA-HDC** (2 vol.% PVA) instead of concrete
(Table 3, Fig. 2). The variables were axial load (343.7–687.5 kN), stirrup ratio (0.84–1.26%) and shear-span
ratio (2 vs 1.5).

**The HDC itself strain-hardens** in direct tension (Fig. 1, p. 2):
- cracking strength 5.73 MPa, tensile strength 6.14 MPa;
- ultimate tensile strain about 1.0%, with multiple cracking.

**Brittle vs ductile shear.** The RC column failed in brittle shear at about 1.8% drift, with cover
crushing. The HDC columns failed in "relatively ductile" shear: a dense network of fine diagonal cracks,
no cover spalling (p. 4–5, Figs. 6–7).

**Gains over RC** (Table 5):
- cracking load at least 50% higher;
- peak load 12.6–30.2% higher at λ = 2, and 53% higher at λ = 1.5 (HDC7, computed here);
- ultimate drift 1/35–1/27 vs 1/55;
- ductility factor 2.14–2.75 vs 1.69.

Cumulative energy at ultimate was 2.8–4.4× that of RC (Table 6). Cutting the stirrups by 20–33% cost only
4.4–6.6% of peak load (p. 8). GB 50010-2010 predicts the shear strength conservatively (P_m/V_n 1.08–1.26);
ACI 318 underestimates it by at least 40% (Table 7).

## Objective / research question
- Can replacing concrete with HDC in RC short columns turn brittle shear failure into a more ductile one?
- How do axial load, stirrup ratio and shear-span ratio affect HDC short columns?
- Can existing RC shear-strength models (ACI 318-05, GB 50010-2010) be used for HDC columns? (p. 1–2, 9)

## Terminology (rule §3)
- The authors' exact term is **"high-ductile fiber-reinforced concrete (HDC)"**, "a kind of fiber-reinforced cement
  composites like … ECC … and HPFRCCs, which shows steady propagation of multiple fine cracks and excellent
  tensile strain-hardening behavior" (p. 1). They cite Kou, Deng & Liang 2013 and
  [[deng2015-hdc-compressive-toughness]] for HDC.
- **Tensile strain hardening is reported, with data** (Fig. 1a):
  - three direct-tension curves rise from first cracking at about 5.5–6 MPa to a peak of about 6.1–6.6 MPa,
    with stress drops at each crack;
  - multiple parallel cracks are visible (Fig. 1b);
  - ε_tu is about 1.0%.
- Strain capacity: about 1.0%, above the 0.5% of JC/T 2461-2018 but well below the ECC convention (> 3%).
  See [[terminology-hdc-ecc-shcc]].

## Materials & mix design
| Mix ID | Cement | Fly ash | Slag/other | Sand (type, max size) | W/B | SP | Fiber type | L (mm) | d (µm) | Vf (vol.%) |
|---|---|---|---|---|---|---|---|---|---|---|
| HDC | binder (cement + fly ash) 1186 kg/m³; split not reported | in binder, share not reported | none | river sand 427 kg/m³; max size n.r. | 0.29 (computed: 344/1186) | water reducer 8 kg/m³ | PVA | 12 | 39 (printed "0.39 µm" ⚠️) | 2.0 (26 kg/m³; 26/1300 = 2.0% computed with ρ 1.3 g/cm³ from [[deng2015-hdc-compressive-toughness]]) |
| Concrete (RC1) | not reported | not reported | not reported | not reported | not reported | not reported | none | — | — | 0 |

Units of binder quantities: kg/m³ (Table 1). Sand/binder = 0.36 (computed), consistent with the XAUAT
base mix in [[deng2018-hdc-compressive-constitutive]].

PVA (Table 2): L 12 mm, d "0.39 µm" (sic; presumably 39 µm ⚠️), σ_f 1600 MPa, E 40 GPa.

Steel (Table 4): HRB400 f_y 439 MPa; HPB235 315 MPa.

## Test methods
- **Material tests:**
  - cube f_cu, three 100 mm cubes each for concrete and HDC (p. 2, Table 4);
  - direct tension on HDC, 3 specimens (Fig. 1). Specimen geometry, gauge length and rate not reported ⚠️.
- **Columns** (Table 3, Fig. 2):
  - 250 × 250 mm section, H = 500 mm (λ = 2) or 375 mm (λ = 1.5);
  - longitudinal 6 HRB400 Ø22 (ρ_s 3.65%, p. 10); hoops Ø8 at s = 80/100/120 mm (ρ_sv 1.26/1.01/0.84%);
  - foundation beam 450 × 450 × 1200 mm; HDC also cast in the column–foundation connection to avoid
    interface failure.
- **Axial load N** (constant, hydraulic jack): 515.6 kN reference; 343.7 kN (HDC2) and 687.5 kN (HDC4).
- **Loading:** lateral cyclic load by a 1000 kN MTS actuator, per JGJ/T 101-2015 (p. 2–3, Fig. 4):
  - force control in 20 kN steps up to first yield of the longitudinal bars;
  - then displacement control in 2 mm steps, 3 cycles each, until the load fell below 85% of the peak.
- **Measurement:** LVDT at the loading point, LVDT for foundation slip, crossed dial gauges at mid-height
  (shear deformation), 24 strain foils on bars and hoops (p. 3, Fig. 5).
- **Indices:** P_y by the Mahin–Bertero energy method; P_u = 0.85 P_m; μ = Δu/Δy; θ_u = Δu/H; secant
  stiffness K_i (Eq. 1).
- Curing & test age: **not reported** ⚠️.
→ [[rc-member-strengthening]] (no dedicated cyclic-test page yet)

## Key results
| Mix ID | f'c (MPa) | First-crack stress (MPa) | Tensile strength (MPa) | Tensile strain capacity (%) | Crack width (µm) | Other |
|---|---|---|---|---|---|---|
| HDC | f_cu 65.7 (100 mm cube; age n.r.) | 5.73 (mean) | 6.14 (mean) | about 1.0 ("ultimate tensile strain", Fig. 1) | not reported | E lower than concrete (stated, p. 8) |
| Concrete | f_cu 68.9 (100 mm cube) | n/a | not reported | n/a | n/a | — |

Column results (Table 5; energy from Table 6):

| Specimen | λ | ρ_sv | N (kN) | P_cr (kN) | P_y (kN) | P_m (kN) | Δ_m (mm) | Δ_u (mm) | θ_u | μ | E_u (kN·mm) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| RC1 | 2 | 1.26% | 515.6 | 80 | 240.05 | 289.49 | 8.51 | 9.17 | 1/55 | 1.69 | 3547.57 |
| HDC2 | 2 | 1.26% | 343.7 | 120 | 268.51 | 326.05 | 13.65 | 17.29 | 1/29 | 2.42 | 15 494.21 |
| HDC3 | 2 | 1.26% | 515.6 | 130 | 270.62 | 358.20 | 11.23 | 15.43 | 1/32 | 2.32 | 13 868.88 |
| HDC4 | 2 | 1.26% | 687.5 | 150 | 318.83 | 376.85 | 13.06 | 16.20 | 1/31 | 2.26 | 12 331.63 |
| HDC5 | 2 | 1.01% | 515.6 | 130 | 279.74 | 342.39 | 11.55 | 14.39 | 1/35 | 2.14 | 12 158.34 |
| HDC6 | 2 | 0.84% | 515.6 | 140 | 261.31 | 334.26 | 11.71 | 14.48 | 1/35 | 2.27 | 11 981.61 |
| HDC7 | 1.5 | 1.26% | 515.6 | 150 | 394.01 | 443.92 | 7.37 | 13.89 | 1/27 | 2.75 | 9997.16 |

Main findings (with Table/Fig. location):
- **Cracking and failure (HDC3 vs RC1, same N and ρ_sv)** (p. 3–5, Figs. 6–7):
  - first cracking at 130 vs 80 kN (+62.5%); all HDC columns crack at least 50% higher than RC1;
  - RC1 forms X-shaped diagonal cracks, then brittle shear at about 1.8% drift with crushed cover and exposed bars;
  - HDC columns form a dense network of fine diagonal cracks with no cover spalling. Even HDC6 (lowest ρ_sv)
    reaches 2.8% drift.
- **HDC3 vs RC1** (Table 5, p. 7): P_m +24%, μ +37%, θ_u +72%.
  - This holds although the HDC cube strength is lower than the concrete's (65.7 vs 68.9 MPa).
- **Axial load** (HDC2–4): P_m rises with N, while θ_u and μ hardly change (p. 7).
- **Stirrups** (HDC5, HDC6 vs HDC3): 20% and 33% fewer stirrups cost only 4.4% and 6.6% of P_m and 7.7% and 2.1% of μ.
  HDC6 still beats RC1 by +15.5% P_m, +34.3% μ and +57.9% θ_u (p. 7–8).
  - The authors conclude that HDC can reduce the stirrup ratio.
- **Shear span** (HDC7, λ 1.5 vs HDC3): +23.9% shear strength, +18.5% θ_u and +18.5% μ (p. 8).
- **Energy** (Table 6, p. 8):
  - HDC cumulative energy exceeds RC1 by 109–239% at Δy, 134–247% at Δm and 181–337% at Δu;
  - HDC3 is 2.39×, 2.02× and 2.9× RC1 at these points;
  - energy falls with axial load and rises with stirrup ratio.
- **Stiffness** (Fig. 10, p. 8–9):
  - HDC3 has a lower initial stiffness than RC1 because HDC has a lower E;
  - HDC columns then degrade much more slowly, which the authors credit to strain hardening and bridging
    across diagonal cracks;
  - smaller λ gives higher initial stiffness but faster degradation.
- **Shear-strength prediction** (Table 7, p. 9–10):
  - ACI 318-05: P_m/V_n 1.40–2.08. It is at least 40% below the test because it ignores shear span and fiber
    bridging.
  - GB 50010-2010: P_m/V_n 1.08–1.26 (8–26% below the test). The authors attribute the gap to ignoring
    dowel action (ρ_s 3.65%).
  - The authors recommend GB 50010-2010 as a safe estimate for HDC short columns.
  - Note: in both models the HDC's f_cu enters as if it were concrete.

## Mechanisms / explanations offered by authors
- Fiber bridging lets HDC carry tension across cracks up to its ultimate tensile strain. This gives
  multiple fine cracking instead of localised diagonal cracks, keeps the section intact, and slows stiffness
  degradation (p. 4–5, 8).
- The high compressive toughness of HDC (cf. [[deng2015-hdc-compressive-toughness]]) means axial load and
  stirrups have little effect on degradation rate (p. 8–9).
- "The ductility of the HDC material achieves the ductility of the structural members" (p. 8).

## Limitations (stated + observed)
- Stated: existing RC shear models were not developed for HDC; their applicability was unknown (p. 10).
- Observed:
  - One specimen per configuration; only one RC control (λ 2), so HDC7 (λ 1.5) has no RC companion.
  - All columns failed in shear, so flexural ductility of HDC columns is not tested.
  - Concrete mix, curing and test age not reported. The tension specimen geometry is not given.
  - The fiber diameter is misprinted (0.39 µm). The fly ash share of the binder is not given.
- **Internal inconsistencies:**
  - The abstract's ranges (shear +12.6–30.2%, drift +56.9–88.5%, energy +237.7–336.7%) exclude HDC7.
    Sect. 3.5 gives energy +181–337% including HDC7.
  - The narrative peak loads (RC1 299 kN, HDC3 366 kN, p. 3–4) differ from Table 5 (289.49 and 358.20 kN),
    probably one loading direction vs average ⚠️.
- No crack widths reported.

## Relation to other work
- Agrees with:
  - [[li2003-ecc-review]]: R/ECC members without or with fewer stirrups beat RC in shear and in energy
    absorption, with no spalling (Fischer & Li, as cited).
  - Wu et al. 2016 on steel-reinforced ECC short columns (as cited, ref. [18]).
- Contradicts: ⚔️ [[he2024-hdc-research-advances]] (as summarised in [[rc-member-strengthening]]) cites
  "Deng & Zhang 2018" for HDC **jacketing of cross-shaped short columns**. This paper instead tests square
  250 × 250 mm columns cast **entirely in HDC**, with no jacketing. Possibly a different Deng & Zhang 2018
  paper, or a mis-citation ⚠️.
- Extends:
  - first primary structural (member-level) HDC data in the wiki;
  - first XAUAT tensile curve for normal-strength PVA-HDC (ε_tu about 1%). This sits between Chai 2023
    PVA-HDC (1.15%) and Xi'an PVA-HSHDC (0.23–0.30%).

## Pages updated from this source
- [[rc-member-strengthening]]
- [[terminology-hdc-ecc-shcc]]
- [[tensile-strain-capacity]]
- [[compressive-strength]]
- [[pva-fiber]]
- [[multiple-cracking]]
- [[fiber-bridging]]
- [[strain-hardening]]
- [[mix-designs]]
- [[mechanical-results]]

## To verify
- [ ] Direct-tension specimen geometry, gauge length and loading rate (not given; Fig. 1 only). ⚠️ unverified
- [ ] PVA diameter printed "0.39 µm" in Table 2; 39 µm assumed (same product as the 2015 and 2018 XAUAT papers).
- [ ] Fly ash share in the 1186 kg/m³ binder (not given); probably 50% as in [[deng2018-hdc-compressive-constitutive]].
- [ ] Curing and age at material and column tests.
- [ ] Abstract ranges vs tables (HDC7 excluded from the abstract ranges).
- [ ] Narrative peak loads (299 / 366 kN) vs Table 5 (289.49 / 358.20 kN).
- [ ] Whether [[he2024-hdc-research-advances]]'s "Deng & Zhang 2018, HDC jacketing of cross-shaped short columns" refers to this paper.
