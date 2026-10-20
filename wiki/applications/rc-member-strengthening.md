---
type: application
slug: rc-member-strengthening
aliases: [column jacketing, beam strengthening, slab strengthening, TR-HDC, HSHD-ECC, shear strengthening, ECC layer, NSHSDC jacket]
tags: [application, strengthening, seismic]
sources: [he2024-hdc-research-advances, yang2024-hshdc-uniaxial-tension, li2003-ecc-review, wang2019-rc-beam-ecc-shear-strengthening, yuan2020-nshsdc-beam-strengthening, xue2023-shcc-structural-review, deng2018-hdc-short-columns, deng2015-hdc-compressive-toughness, kunieda2006-hpfrcc-japan-applications, kanakubo2006-dfrcc-tensile-test-method, lee2021-hsdc-wall-emi-impact, paul2014-r-shcc-chloride-corrosion, zhao2022-ecc-tension-damage-model, tabrizikahou2022-masonry-ecc-sma-retrofit]
updated: 2026-10-20
---

# Strengthening of RC Members with HDC

> Status (2026-10-20): **two primary experimental strengthening studies** now exist
> ([[wang2019-rc-beam-ecc-shear-strengthening]]; [[yuan2020-nshsdc-beam-strengthening]]). Everything else
> below is second-hand (review) unless marked primary.

## Primary experimental evidence
| Source | Material (authors' term) | Member | Strengthening | Result | Failure / note |
|---|---|---|---|---|---|
| [[wang2019-rc-beam-ecc-shear-strengthening]] | ECC (PVA 1.5 vol.%, **sprayed**, f_cu 55.9 MPa, σ_tu 4.84 MPa) | 12 RC beams 150 × 300 mm, no stirrups in shear span, 4-point bending, a/d 2 and 3 | 20 or 40 mm layers on both sides, over an interface agent on chiselled SSD substrate | ultimate load **+20–89%**; best SB-40-2 185 → 350 kN (a/d 2, ρ 2.18%) (Table 3) | still shear or debonding, never flexure; **all 40 mm layers debonded** (Sect. 3.3.3, Fig. 7) |
| [[yuan2020-nshsdc-beam-strengthening]] | NSHSDC (no-slump, 1.0% steel + 0.5% PE, f'c 123.4 MPa, room-cured; strain hardening not shown here) | 6 NSC beams 125 × 250 × 2222 mm, 2 D19, no stirrups | jackets cast in a mould on chiselled substrate (40 mm bottom, 20 mm sides/top) | peak **+8%** (top + bottom), **+29%** (3 sides), **+40%** (4 sides) vs B-NN; bottom-only −2.5% (74.04 vs 75.93 kN) (Table 8, Fig. 12) | 4-side: flexural failure, energy 7.11 vs 5.73 kN·m for a stirrup beam; 3-side: concrete crushing, poor post-peak; no jacket delaminated (§3.2) |

Details:
- **a/d effect** (Wang 2019): gains are 40–89% at a/d = 2 vs 20–41% at a/d = 3; at a/d = 3, 20 and 40 mm layers
  gave the same capacity (120 vs 117 kN; 151 vs 150 kN) ([[wang2019-rc-beam-ecc-shear-strengthening]], Table 3, Sect. 3.3.1).
- **Over-strengthening** (Wang 2019): counting the ECC width lowers the effective ρ to 0.58%, below the GB 50010
  minimum ("0.65%" ⚠️ cannot be reproduced); SA-40-2 then carried 190 kN vs 250 kN for SA-20-2 (Sect. 3.3.1).
- **Design model** (Wang 2019): truss + arch, V = 2(ηβσ_t·h·t + arch term), η = 0.6 (20 mm) / 0.4 (40 mm),
  β = −23.04ρ + 1.00, ν = 0.6, φ = 45°; prediction/test 68–100% at a/d 3 but 45–52% at a/d 2 (Eqs. 10–11, Table 4).
  The softening coefficient of ECC under tension–compression (0.6 for concrete) needs study (Sect. 4.4). → [[shear-behaviour]]
- **Monitoring** (Wang 2019): FBG rosettes (15 cm gauge) detected debonding as a sudden strain release (Fig. 5).
- **Bond** (Yuan 2020): slant shear τ up to 21.4 MPa (45HS) and 20.9 MPa (30HS) at 28 d; chiselling +27%; high-roughness
  interfaces meet ACI 546 (14–21 MPa) except at 75°; codes conservative (mean τ/τ_pred 22.5 ACI 318-19, 1.5 AASHTO,
  3.6 CSA, 1.7 MC2010) ([[yuan2020-nshsdc-beam-strengthening]], Table 7, Fig. 7, §3.1.1). → [[interface-bond]]
- Yuan 2020's motivation: UHPC jackets reduce member ductility and need heat curing; no-slump HDC is room-cured and
  shape-holding for in-situ casting (§1).
- **Walls** (primary): NC panels chiselled and cast with 5–20 mm HSDC on one or both faces for impact and EMI
  protection ([[lee2021-hsdc-wall-emi-impact]], §2.1, Fig. 2). → [[extreme-loading-applications]]

## Columns cast wholly in HDC (not jacketing)
- [[deng2018-hdc-short-columns]] (primary, XAUAT): 6 square 250 mm short columns cast **entirely** in PVA-HDC
  (ε_tu ≈ 1.0%, σ_tu 6.14 MPa) vs 1 RC column, reversed cyclic load. HDC3 vs RC1: P_m +24%, μ 2.32 vs 1.69 (+37%),
  θ_u 1/32 vs 1/55 (Table 5); cracking load 120–150 vs 80 kN; energy at Δu 2.8–4.4× (Table 6); ductile shear
  failure with dense fine cracks and no spalling (Figs. 6–7). Stirrups cut by 20% / 33% lowered P_m only 4.4% / 6.6% (p. 8).
  GB 50010-2010 is conservative (P_m/V_n 1.08–1.26), ACI 318-05 more so (1.40–2.08) (Table 7). → [[unreinforced-hdc-structures]], [[shear-behaviour]]
- [[deng2015-hdc-compressive-toughness]]: a bridging stress of 5.7 MPa equals a stirrup ratio ρ_v = 3.03% (500 mm column,
  HRB400 Ø10 at 23 mm); HDC is proposed for plastic-hinge regions to reduce ties (Eqs. 7–9, p. 6–7). → [[compressive-constitutive-model]]
- ⚔️ **Citation conflict:** [[he2024-hdc-research-advances]] (p. 6) cites "Deng & Zhang 2018" for **HDC jacketing of
  cross-shaped short columns**. The Deng & Zhang 2018 paper in the corpus tests **whole-HDC square** columns, not
  jacketing. Either another paper or a mis-citation. → [[gaps]]

## Reviews and second-hand evidence
### As cited in [[he2024-hdc-research-advances]]
- **Columns:** HDC jacketing of cross-shaped short columns (Wang 2023; Deng & Zhang 2018 ⚔️ see above) (p. 6).
- **Beams and slabs** (p. 19–20):
  - HSHD-ECC (Qin 2020);
  - steel wire plus ECC (Yuan 2020) — ⚔️ the Yuan 2020 paper in the corpus uses steel **fibre** + PE no-slump
    HSHDC jackets, not steel wire; either a different paper or a mis-description (verify). High-strength steel wire
    rope (HSSWR) reinforced ECC plates are modelled in [[zhao2022-ecc-tension-damage-model]] (ρ 0.28–0.48%, Table 6, §5);
  - textile-reinforced HDC (TR-HDC) slabs (Song 2023/2024);
  - sprayable high-ductility FRCC (Huang 2019).
- **Why TR-HDC:** textile-reinforced mortar has low matrix elongation and large cracks, and stops carrying load
  after cracking (p. 20).

### As cited in [[xue2023-shcc-structural-review]] (corresponding author's earlier tests)
- Tension-side SHCC layer on RC beams (4PB): 40.8 kN (control) → 48.9 / 55 / 65.7 kN for **10 / 30 / 50 mm** layers
  (+16.5 / 34.8 / 61.0%); initial stiffness rises with thickness (Section 4.1.1, Fig. 6).
- Failure by crack localisation in the layer, then debonding (10 and 30 mm) (Section 4.1).
- Thin layers: cracks concentrate over the existing RC crack ("zero-span tension"); 50 mm: evenly distributed bending
  cracks. Dogbone ductility is not fully realised in thin layers (Section 4.1.2, Figs. 7–8). → [[dogbone-uniaxial-tension]]
- 3 mm SHCC on both sides of a beam without stirrups (a/d 3) "significantly" increased shear capacity (no value) (Section 4.2, Fig. 9).
- Substrate roughened by retarder wash-out (Section 4.2).

### Japan (as cited in [[kunieda2006-hpfrcc-japan-applications]])
- ECC coupling-beam dampers in high-rise RC buildings (Tokyo 2004, Yokohama 2005); 1/2.5-scale shear tests gave crack
  widths < 0.3 mm after cyclic loading (p. 26, Fig. 12).
- HPFRCC beams dissipate more cyclic energy than RC beams (Fukuyama 1999, as cited, Fig. 6).
- Bonded HPFRCC / ribbed steel pipe: narrower crack spacing and higher capacity (Rokugo 2002, as cited, Fig. 8).
- Railway viaduct lab RC beams with 10 mm sprayed HPFRCC: crack width 0.13 vs 0.25 mm after 17 million cycles (p. 30). → [[fatigue]]

### Other
- DFRCC demands by application (JCI): slab strengthening by spraying (tensile capacity, fatigue); surface protection
  (crack width < 0.1 mm); seismic strengthening (strength, confinement). Tensile deformation capacity is "not such an
  important factor" for member shear; confinement and cover retention matter
  ([[kanakubo2006-dfrcc-tensile-test-method]], Table 1, p. 3).
- ECC columns vs RC columns under cyclic load: +110% stiffness, +65% strength, +45% ductility, +100% energy
  (Gencturk & Hosseini 2015, as cited in [[tabrizikahou2022-masonry-ecc-sma-retrofit]], Sect. 1).
- R/SHCC beams 100 × 100 × 500 mm with Y10 bars: peak about 45–55 kN (2 bars) and 30–44 kN (1 bar) at 3.5 mm deflection
  ([[paul2014-r-shcc-chloride-corrosion]], Fig. 4 ⚠️ read from figure). → [[chloride-and-corrosion]]

## Early structural evidence (as cited in [[li2003-ecc-review]], p. 221–224)
- R/ECC beams without stirrups beat R/C beams with stirrups in capacity and energy absorption, with no
  spalling at 10% drift (Fischer & Li 2002b).
- Steel and ECC deform compatibly: no shear lag, low bond stress, no bond splitting (Fischer & Li 2002a).
- GFRP bars in ECC avoid premature FRP failure (Fischer & Li 2003a).
- Hybrid steel-beam / RC-column joints with ECC need no stirrups (Parra-Montesinos & Wight 2000).
- Precast ECC infill panels: 56 kN vs 38 kN for concrete panels in cyclic shear (Kesner & Billington 2002).

> Synthesis: both primary beam studies used beams **without stirrups**, so most configurations still failed in
> shear or by debonding; gains (+8% to +89%) depend more on a/d, wrap configuration and bond than on the
> composite's tensile ductility. Thicker layers are not always better: 40 mm sprayed ECC layers all debonded
> (Wang 2019), while Xue's 50 mm cast SHCC layer gave the largest gain (as cited). Interface preparation is a
> first-order design variable. The dogbone ε_tu overstates what a thin layer delivers (zero-span effect).

## Conflicts & open questions
- ⚔️ "Deng & Zhang 2018" jacketing (He 2024) vs whole-HDC columns (primary). → [[gaps]]
- ⚔️ "steel wire plus ECC (Yuan 2020)" (He 2024) vs steel-fibre/PE NSHSDC jackets (primary). → [[gaps]]
- Refinement of "repairs avoid delamination" (Lim & Li 1997, via [[li2003-ecc-review]]): 10, 30 and 40 mm layers
  debonded in Xue (as cited) and Wang 2019. → [[repair-and-field-applications]]
- **Bond to existing concrete:** Yang 2024 stated it was unstudied for HSHDC ([[yang2024-hshdc-uniaxial-tension]], p. 14).
  Now partly addressed: slant shear for NSHSDC at 28 d only ([[yuan2020-nshsdc-beam-strengthening]]); no bond
  tests for normal ECC layers in the corpus. → [[interface-bond]], [[gaps]]
- Applicability of RC shear formulas to HDC members is unknown ([[deng2018-hdc-short-columns]], p. 10).
- One beam per configuration in Yuan 2020; no Chinese PVA-HDC jacketing test in the corpus.

## Related
- [[masonry-wall-retrofit]] · [[unreinforced-hdc-structures]] · [[repair-and-field-applications]] ·
  [[shear-behaviour]] · [[interface-bond]] · [[hybrid-fiber]] · [[four-point-bending-inverse-analysis]]
