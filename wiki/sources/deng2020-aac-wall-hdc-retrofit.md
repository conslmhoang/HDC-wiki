---
type: source
slug: deng2020-aac-wall-hdc-retrofit
title: "In-plane seismic behavior of autoclaved aerated concrete block masonry walls retrofitted with high ductile fiber-reinforced concrete"
authors: [Mingke Deng, Wei Zhang, Shuo Yang]
year: 2020            # vol. 219 (2020); received 24 Nov 2019, available online 5 Jun 2020
venue: "Engineering Structures, vol. 219, Article 110854 (Elsevier)"
doi: "10.1016/j.engstruct.2020.110854"
raw_file: raw/papers/Deng2020_AAC-wall-HDC-retrofit.pdf
material_term: "HDC = high ductile fiber-reinforced concrete, 'also referred to as' ECC"
study_type: experimental (structural, in-plane reversed cyclic load on masonry walls) + analytical capacity formulas
tags: [structural, seismic, masonry, aac, urm, in-plane, retrofit, overlay, strips, pva, xauat, deng-group]
ingested: 2026-10-21
updated: 2026-10-21
---

# AAC block masonry walls retrofitted with HDC (Deng, Zhang & Yang, 2020)

## One-paragraph summary
XAUAT tested five half-scale **autoclaved aerated concrete (AAC) block** walls (2400 × 1400 × 190 mm) under 0.3 MPa
vertical stress and in-plane reversed cyclic lateral load (Table 1, Fig. 1): an unreinforced reference (W-1), a
confined wall with RC tie-columns (CW-1), and three HDC retrofits:
- **W-2**: 15 mm HDC strips (300 mm vertical, 250 mm horizontal) on both faces at the wall edges;
- **W-3**: the same strips with built-in steel bars anchored into the wall and foundation;
- **W-4**: a 15 mm single-sided HDC layer over the whole face.

Average peak load rose 17% (W-2), 28% (W-3) and 31% (W-4) over W-1 (Table 4). W-2's strips **debonded** at the wall
base and its ductility did not improve. W-3 reached the confined wall's ultimate displacement (+75% vs W-1) and
ductility (2.05× W-1), with 32% more strength and 125% more energy than CW-1. W-4 changed the failure from diagonal
shear to **bed-joint sliding**, with the highest energy (+308%) and little post-peak degradation (§3–4, Concl.).
The HDC strain-hardens in direct tension (Fig. 3): first crack about 3.25 MPa, f_tu 3.89 MPa, failure at about 1.24%.

## Objective / research question
- Can HDC strips, bar-reinforced HDC strips or an HDC layer turn the brittle in-plane failure of unconfined AAC
  masonry walls into a ductile one, reaching the deformation capacity of a confined wall? (§1–2)
- Analytical lateral-resistance formulas for each failure mode (§5).

## Terminology (rule §3)
- Authors' exact term: **"high ductile fiber-reinforced concrete (HDC)"**; "HDC, also referred to as engineered
  cementitious composite (ECC) [Li 2001], is a type of cement composite reinforced with synthetic fibers", with strain
  hardening and multiple cracking in tension (p. 1).
- The same group calls its masonry retrofit material "ECC" in the cited Deng & Yang papers (CBM 2018;177:395–408;
  Eng. Struct. 2020;207:110249), i.e. XAUAT uses **HDC and ECC interchangeably** for one material family.
- **Tensile strain hardening is measured** (Fig. 3, one curve shown): linear to about 3.25 MPa at about 0.09%, then a
  rising serrated curve to about 4.0 MPa near 1.2%, failure at about 1.24% (read from figure ⚠️). Table 3:
  f_tu,HDC 3.89 MPa (number of specimens not stated).
- Strain capacity (about 1.2%) is above the 0.5% HDC threshold but well below the ECC convention (> 3%).
  See [[terminology-hdc-ecc-shcc]].

## Materials & mix design
| Mix ID | Cement | Fly ash | Slag/other | Sand (type, max size) | W/B | SP | Fiber type | L (mm) | d (µm) | Vf (vol.%) |
|---|---|---|---|---|---|---|---|---|---|---|
| HDC | 593 | 593 (FA/C 1.0 by mass) | none | fine silica sand 427; max size not reported | 0.29 (computed: 344/1186, by mass) | water reducer 8 | PVA (properties not reported) | not reported | not reported | 1.7 |

Units of binder quantities: kg/m³ (Table 2). Same matrix as the XAUAT base mix in [[deng2017-rc-column-hdc-jacket]]
and [[deng2019-urm-shaking-table-hdc]], but with **1.7 vol.% PVA instead of 2%**. Fiber product, length and diameter
not given.

Other materials (Table 3): AAC block 600 × 240 × 190 mm, f1 = 3.5 MPa; mortar f2 = 3.1 MPa (30 cubes 70.7 mm);
masonry f_m = 1.78 MPa (computed, Eq. 1); tie-column concrete f_cu 14.9 MPa, f_t 1.74 MPa (Eq. 2); steel f_y 375 MPa,
f_u 510 MPa.

## Test methods
- **HDC tension:** dogbone, 15 mm thick, 50 mm wide in the measured region (method from Deng & Yang 2018) (p. 2).
  Gauge length, rate and specimen count not reported ⚠️. f_cu,HDC from six 100 mm cubes.
- **Curing & test age:** retrofitted walls water-sprayed twice a day for one week; all material samples air-cured
  beside the walls; walls and materials tested after **two months** (p. 2).
- **Walls** (Table 1, Fig. 1): 2400 × 1400 × 190 mm AAC panels on RC foundation, RC loading beam; CW-1 tie-columns
  190 × 120 mm with 4 Φ6 plain bars, Φ6 stirrups @ 200 mm. W-3 strip bars listed as "12 Φ6" vertical and "6 Φ6"
  horizontal (garbled in text ⚠️), anchored in drilled holes.
- **Loading** (Fig. 4–6): 0.3 MPa vertical stress by two jacks via a rigid beam (simulating 2–3 storeys); lateral
  actuator; force control in 10 kN steps (one cycle each, 0.05 mm/s) to cracking, then displacement multiples of
  Δcr, three cycles each (0.5 mm/s), until load < 85% of peak.
- **Measurement:** 7 LVDTs (top, base and mid-height displacement; corner rotation; two diagonals).
- **Indices:** μ = Δd/Δe from a bilinear idealisation (Δd at 80% of P_max; K_e = P_cr/Δcr) (Eq. 3, Fig. 10);
  cumulative energy; equivalent viscous damping ξ = E_diss/(2π E_inp) (Eq. 4); secant stiffness K_i/K (Fig. 15).
→ [[masonry-wall-retrofit]], [[dogbone-uniaxial-tension]]

## Key results
| Mix ID | f'c (MPa) | First-crack stress (MPa) | Tensile strength (MPa) | Tensile strain capacity (%) | Crack width (µm) | Other |
|---|---|---|---|---|---|---|
| HDC (1.7% PVA) | f_cu 49.80 (100 mm cube, ≈ 2 months, air-cured) | about 3.25 (Fig. 3 ⚠️) | 3.89 (Table 3) | about 1.2 at peak; failure about 1.24 (Fig. 3 ⚠️) | not reported | — |

Wall results (Table 4; push / pull):

| Wall | Retrofit | P_cr (kN) | P_u (kN) | Δ_u (mm) | Δ_f (mm) | Failure | Gain in mean P_u vs W-1 |
|---|---|---|---|---|---|---|---|
| W-1 | none | 100 / −90 | 134.40 / −101.25 | 3.99 / −4.06 | 8.05 / −8.00 | diagonal shear | — |
| W-2 | HDC strips, both faces | 120 / −110 | 145.59 / −130.67 | 4.30 / −4.13 | 8.05 / −8.04 | diagonal shear, strip debonding | +17% |
| W-3 | HDC strips + steel bars | 132 / −110 | 165.34 / −136.88 | 4.05 / −4.04 | 13.99 / −13.99 | diagonal shear | +28% |
| W-4 | 15 mm single-sided HDC layer | 145 / −100 | 173.61 / −134.69 | 4.03 / −6.01 | 13.70 / −13.96 (test stopped) | **sliding** (bed joint) | +31% |
| CW-1 | RC tie-columns | 100 / −90 | 122.14 / −107.50 | 3.87 / −4.03 | 14.01 / −13.98 | diagonal shear | (−3%, computed) |

Gains use the mean of push and pull (computed here: 117.8 / 138.1 / 151.1 / 154.2 / 114.8 kN, consistent with the
stated 17 / 28 / 31%).

Main findings (with Table/Fig. location):
- **Deformation:** ultimate displacement +75% for W-3 and CW-1; W-4 test stopped at 13.83 mm = 1.72× W-1 while still
  above 85% of peak; W-2 not improved (§4.1). Conclusion 2 says "75%" for both W-3 and W-4.
- **Ductility** (Fig. 11): W-3 = 2.05× W-1, same level as CW-1; W-4 +53% (underestimated, test stopped); W-2 slightly
  lower than W-1 (§4.2).
- **Energy** (Fig. 12): total +41% (W-2), +238% (W-3), +308% (W-4) vs W-1; W-3 +125% vs CW-1 (§4.3).
- **Damping:** W-2 highest ξ, similar to W-1 and W-4 (heavy panel damage or sliding); CW-1 below W-3 (Fig. 14).
- **Stiffness:** W-4 lowest degradation, W-3 highest; W-2 coincides with W-1 after debonding (Fig. 15).
- **Cracking:** W-3 and CW-1 had narrower diagonal cracks than W-1; W-3 cracks narrower than CW-1 (no widths given)
  (p. 4–5). W-4: no diagonal cracks on panel or HDC layer; horizontal crack along the bottom bed joint (p. 4).
- **Strip debonding (W-2):** compressive stress concentration at the wall base caused debonding; the spalled face
  shell carried AAC fragments, so the HDC–AAC bond exceeded the block's tensile strength (p. 4). Anchored bars (W-3)
  prevented it.
- **Capacity formulas** (§5, Fig. 16): diagonal shear (Eq. 5–6, b = 1.2); W-2/W-3: V_u = V_m + V_s + V_HDC with
  V_s = 0.1 Σ A_y f_y and V_HDC = 0.44 α_HDC f_tu t′ x, α_HDC = 0.53 (= 0.6 × 0.896); sliding (W-4):
  V = µN + µ f_tu t (0.5 l), µ = 0.7. Predictions are "conservative" for all walls (values only in a bar chart).

## Mechanisms / explanations offered by authors
- Strain hardening and multiple cracking of HDC raise energy dissipation and limit crack width (p. 1–2).
- HDC strips act as confining boundary elements like tie-columns, but only if anchored; bars embedded in HDC have
  higher bond than in concrete (citing Deng, Pan & Sun 2018), so W-3 pinches less than CW-1 (p. 5).
- The HDC layer raises diagonal shear capacity above the bed-joint sliding capacity, moving failure to sliding,
  which is "more ductile" (§3.1, Concl. 3). Its sliding resistance includes a clamping term µ f_tu t x_cr (Eq. 13).

## Limitations (stated + observed)
- Stated: limited number of specimens; more data and better analytical models needed (§5, Concl. 5).
- Observed:
  - One wall per configuration; W-1 was stronger than CW-1 (material scatter, p. 5).
  - W-4 test stopped at 14 mm before failure, so its ductility and drift are lower bounds.
  - PVA fiber properties, length and diameter not given; one tension curve shown; tension gauge length not given.
  - Strength gains are means of push and pull (single-sided W-4 is asymmetric: 173.61 vs 134.69 kN).
  - No bond test of HDC on AAC; no crack widths; out-of-plane behaviour not tested.
  - Fig. 15 text mentions drift "0.25" and "0.53" without unit; axis is in % ⚠️.

## Relation to other work
- Agrees with:
  - [[deng2019-urm-shaking-table-hdc]] (same group): a 15 mm HDC overlay limits diagonal cracking of masonry.
  - [[tabrizikahou2022-masonry-ecc-sma-retrofit]] (FE): interface behaviour controls the overlay benefit; here W-2's
    strips debonded and gave little benefit until anchored.
- Contradicts / refines: ⚔️
  - Same nominal XAUAT matrix, but 1.7% PVA and air curing give f_cu 49.80 MPa and f_tu 3.89 MPa, vs 61.15 MPa and
    5.83 MPa with 2% PVA in [[deng2019-urm-shaking-table-hdc]] and 6.12 MPa in [[deng2017-rc-column-hdc-jacket]].
    Lower fiber content, curing and fiber product differ; not a direct conflict.
  - Refines [[interface-bond]]: a well-bonded overlay on a weak substrate fails **inside the substrate** (AAC face
    shell), so bond strength is bounded by the masonry unit, not by the HDC.
- Extends:
  - First AAC-masonry data in the wiki; first in-plane cyclic wall tests of HDC retrofit (strips vs full layer).
  - Provides design formulas for HDC strip and layer contributions (Eqs. 12–14).
  - Not cited by [[he2024-hdc-research-advances]] as far as its page records (its "Deng 2020" entries concern cube
    compression and elevated temperature, i.e. other papers).

## Pages updated from this source
- [[masonry-wall-retrofit]]
- [[interface-bond]]
- [[terminology-hdc-ecc-shcc]]
- [[tensile-strain-capacity]]
- [[dogbone-uniaxial-tension]]
- [[shear-behaviour]]
- [[deng2019-urm-shaking-table-hdc]]
- [[deng2017-rc-column-hdc-jacket]]
- [[mix-designs]]
- [[mechanical-results]]
- [[gaps]]

## To verify
- [ ] Fig. 3 readings (first crack ≈ 3.25 MPa at ≈ 0.09%; peak ≈ 4.0 MPa near 1.2%; failure ≈ 1.24%) ⚠️ unverified; f_tu 3.89 MPa vs curve peak ≈ 4.0 MPa (mean of several specimens?).
- [ ] PVA fiber product, length, diameter (not reported).
- [ ] W-3 bar layout "12 Φ66 Φ6" in Table 1 (garbled; read as 12Φ6 vertical, 6Φ6 horizontal?).
- [ ] Ductility values (Fig. 11) and calculated capacities (Fig. 16) are only in charts.
- [ ] W-4 displacement gain: 1.72× (§4.1) vs "75%" (Concl. 2).
- [ ] Drift values "0.25" and "0.53" in §4.4 (units).
