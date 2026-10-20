---
type: source
slug: deng2017-rc-column-hdc-jacket
title: "Cyclic loading tests of RC columns strengthened with high ductile fiber reinforced concrete jacket"
authors: [Mingke Deng, Yangxi Zhang]
year: 2017            # vol. 153 (2017); received 31 Mar 2017, available online 31 Jul 2017
venue: "Construction and Building Materials, vol. 153, pp. 986–995 (Elsevier)"
doi: "10.1016/j.conbuildmat.2017.07.175"
raw_file: raw/papers/Deng2017_RC-column-HDC-jacket.pdf
material_term: "HDC = high ductile fiber reinforced concrete (FRCC 'like' ECC and HPFRCC)"
study_type: experimental (structural, constant axial + reversed cyclic lateral load; jacket retrofit)
tags: [structural, seismic, column, jacketing, retrofit, cyclic-loading, pva, xauat, deng-group, bar-mesh]
ingested: 2026-10-21
updated: 2026-10-21
---

# RC columns strengthened with HDC jackets (Deng & Zhang, 2017)

## One-paragraph summary
XAUAT tested eight identical 250 × 250 mm RC columns (C40 target concrete, H = 750 mm to the load point) under
constant axial load (573–1174 kN) and reversed cyclic lateral load (Table 3, Fig. 2). Two were controls; six got
a **30 mm four-sided jacket** cast after the cover was gouged off (Fig. 3):
- **BMRM**: bar-mesh (Ø6 @ 80 mm) reinforced mortar (C-5, C-8);
- **HDC-0**: plain PVA-HDC, no mesh (C-2 Japanese PVA; C-3 Chinese PVA, "HDC-2");
- **HDC-B**: PVA-HDC with the same bar mesh (C-4, C-7).

The controls failed in brittle bend-shear with cover spalling. HDC-0 columns failed in bend-shear with
"moderate ductility" and no jacket spalling. **HDC-B columns formed a plastic hinge at the foot and failed in
flexure** with no diagonal cracks (Table 6, Fig. 7). HDC-B gave the largest ductility factor (7.9 and 6.3 vs 3.3
and 2.9 for the controls) and ultimate drift (4.7% and 4.2% vs 2.2%) (Table 7), and 8–10× the controls' cumulative
energy at ultimate (Table 8). Replacing mortar by HDC in a mesh-reinforced jacket cut peak load 5–10% but raised μ
by about 80% (Table 7, p. 7). **The HDC itself strain-hardens in direct tension** (Fig. 1a), with the strain
capacity strongly fiber-dependent (Japanese vs Chinese PVA).

## Objective / research question
- Can an HDC jacket (with or without bar mesh) turn the brittle bend-shear failure of seismically deficient RC
  columns into a ductile one, and how does it compare with a bar-mesh mortar (ferrocement-type) jacket?
- Effect of axial load level and of PVA fiber origin (p. 1–2).

## Terminology (rule §3)
- Authors' exact term: **"High ductile fiber reinforced concrete (HDC)"**, "a class of fiber reinforced cementitious
  composite like ... ECC ... and HPFRCC, which exhibits strain-hardening behavior in tension and high toughness in
  compression" (p. 2). Cited HDC refs: Kou, Deng & Liang 2013 (Build. Struct., in Chinese), Deng et al. 2015 (Indus.
  Constr., in Chinese), [[deng2015-hdc-compressive-toughness]].
- **Tensile strain hardening is measured** (Fig. 1a, one curve per fiber type shown):
  - HDC (Japanese PVA): first cracking at about 5.3 MPa, rising with load drops to about 6.2 MPa; curve ends at
    about 3.0% strain at about 5.1 MPa (read from figure ⚠️). Table 5: tensile strength 6.12 MPa.
  - HDC-2 (Chinese PVA): first cracking at about 4.0–4.5 MPa, peak about 4.8 MPa, curve ends at about 1.2%
    (read from figure ⚠️). Table 5: 4.84 MPa.
  - Text: Japanese-fiber HDC has 26.4% higher tensile strength and "about 150%" higher **ultimate tensile strain**
    (p. 2, p. 8). The strain is "ultimate", i.e. end of curve, not strain at peak stress.
- So the Japanese-fiber HDC reaches roughly ECC-level ultimate strain (about 3%), the Chinese-fiber HDC only about 1.2%.
  See [[terminology-hdc-ecc-shcc]].

## Materials & mix design
| Mix ID | Cement | Fly ash | Slag/other | Sand (type, max size) | W/B | SP | Fiber type | L (mm) | d (µm) | Vf (vol.%) |
|---|---|---|---|---|---|---|---|---|---|---|
| HDC (Japanese PVA) | 593 | 593 (FA/C 1.0 by mass) | none | river sand 427; max size not reported | 0.29 (computed: 344/1186, by mass) | HRWR 8 | PVA (Japan): σ_f 1600 MPa, E 40 GPa, elong. 7% | 12 | 39 (printed "Diameter/mm 39"; µm assumed ⚠️) | 2 (stated; 26 kg/m³ ÷ 1.3 g/cm³ = 2.0%, computed) |
| HDC-2 (Chinese PVA) | 593 | 593 | none | river sand 427 | 0.29 | HRWR 8 | PVA (China): σ_f 1200 MPa, E 32 GPa, elong. 8% | 12 | 39 (⚠️ as above) | 2 |
| Mortar (BMRM jacket) | not reported | not reported | not reported | not reported | not reported | not reported | none | — | — | 0 |
| Concrete (columns) | not reported (target C40) | not reported | not reported | not reported | not reported | not reported | none | — | — | 0 |

Units of binder quantities: kg/m³ (Table 1). Sand/binder 0.36 (computed). Fiber data: Table 2 (specific gravity 1.3 for both).
This is the same proportion as [[deng2018-hdc-short-columns]] (binder 1186 kg/m³ there, split not given); this
paper gives the split: cement 593 + FA 593.

Steel (Table 4): HRB400 Ø6 f_y 493.84 MPa (bar mesh); HPB300 Ø8 f_y 428.62 MPa (hoops); HRB400 Ø16 f_y 498.03 MPa (longitudinal).

## Test methods
- **Material tests:** 100 mm cubes (3 per material) for f_cu (Table 5); uniaxial tension and compression
  stress–strain curves of HDC and HDC-2 (Fig. 1). Tension specimen geometry, gauge length, rate and number of
  specimens **not reported** ⚠️.
- **Columns** (Fig. 2, Table 3): inverted-T specimens, column 250 × 250 × 850 mm, H = 750 mm; 6 Ø16 longitudinal,
  Ø8 hoops @ 100 mm; foundation 400 × 400 × 1200 mm.
- **Jackets:** 30 mm on four sides; vertical bar mesh Ø6 @ 80 mm (BMRM and HDC-B) anchored 150 mm into the
  foundation. Surface preparation: cover gouged off, debris cleaned, surface wetted, formwork, cast (p. 2, Fig. 3).
- **Axial load** (constant, jack): 573 kN (C-1), 764 kN (C-6), 881 kN (C-2 to C-5), 1174 kN (C-7, C-8) (Table 3).
  The axial load *ratio* is not stated numerically.
- **Lateral load:** force control in 20 kN steps to first yield of longitudinal bars, then displacement steps of
  4 mm, three cycles each, until failure or load < 85% of peak (p. 2, Fig. 5).
- **Measurement:** LVDT at loading point; LVDT for foundation slip; two LVDTs over the plastic-hinge region
  (curvature, Eq. 1); 12 strain gauges on bars and stirrups (Fig. 6).
- **Indices:** yield by Mahin–Bertero energy method; ultimate at 85% of peak; μ = Δu/Δy; θu = Δu/H; values are
  the average of push and pull (p. 6).
- Curing & test age: concrete target 28-d cube strength about 40 MPa (p. 2); HDC/mortar curing and age at test
  **not reported** ⚠️.
→ [[rc-member-strengthening]], [[dogbone-uniaxial-tension]]

## Key results
| Mix ID | f'c (MPa) | First-crack stress (MPa) | Tensile strength (MPa) | Tensile strain capacity (%) | Crack width (µm) | Other |
|---|---|---|---|---|---|---|
| HDC (Japanese PVA) | f_cu 60.35 (100 mm cube; age n.r.) | about 5.3 (Fig. 1a ⚠️) | 6.12 (Table 5) | ultimate about 3.0 (end of curve, Fig. 1a ⚠️); peak-stress strain not stated | not reported | compressive peak strain about 0.6% (p. 2); prism peak ≈ 59 MPa (Fig. 1b ⚠️) |
| HDC-2 (Chinese PVA) | f_cu 61.29 | about 4.0–4.5 (Fig. 1a ⚠️) | 4.84 (Table 5) | ultimate about 1.2 (Fig. 1a ⚠️) | not reported | compressive peak strain about 0.6% |
| Mortar | f_cu 66.68 | n/a | not reported | n/a | n/a | — |
| Concrete | f_cu 45.40 | n/a | not reported | n/a | n/a | — |

Column results (Table 3 for N, Table 7, Table 8 energy at ultimate, Table 9 hinge rotation at ultimate):

| Specimen | Jacket | N (kN) | P_y (kN) | P_m (kN) | Δ_m (mm) | Δ_u (mm) | μ | θ_u (%) | E at Δu (kN·m) | φ_u (×10⁻³) | Failure (Table 6) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| C-1 | none | 573 | 153.1 | 178.7 | 11.3 | 16.2 | 3.3 | 2.2 | 16.72 | 15.9 | bend-shear, severe spalling |
| C-2 | HDC-0 (Jpn) | 881 | 225.1 | 268.6 | 14.2 | 23.7 | 5.3 | 3.2 | 68.69 | 21.1 | bend-shear, wide diagonal cracks |
| C-3 | HDC-0 (Chn) | 881 | 234.0 | 280.6 | 14.7 | 20.8 | 4.5 | 2.8 | 46.81 | 19.7 | bend-shear, wide diagonal cracks |
| C-4 | HDC-B | 881 | 228.2 | 276.2 | 13.3 | 35.1 | 7.9 | 4.7 | 163.99 | 49.8 | **bend (flexure)**, tiny flexural cracks |
| C-5 | BMRM | 881 | 254.6 | 302.5 | 10.2 | 20.2 | 4.4 | 2.7 | 46.20 | 19.4 | bend-shear, mortar spalling, mesh buckling |
| C-6 | none | 764 | 161.2 | 194.8 | 11.2 | 16.2 | 2.9 | 2.2 | 16.08 | 15.3 | bend-shear, bond-slip cracks, spalling |
| C-7 | HDC-B | 1174 | 272.2 | 320.4 | 12.6 | 31.8 | 6.3 | 4.2 | 130.55 | 42.1 | **bend (flexure)** |
| C-8 | BMRM | 1174 | 284.5 | 336.5 | 10.4 | 17.1 | 3.5 | 2.3 | 33.88 | 15.2 | bend-shear, mortar spalling, mesh buckling |

Note: the jacketed columns carried higher axial loads than their nominal controls (881 vs 573 kN for C-1;
1174 vs 764 kN for C-6), so the "vs control" gains mix jacket and axial-load effects.

Main findings (with Table/Fig. location):
- **HDC-0 vs control** (C-2, C-3 vs C-1): P_m +50.3% / +57%, μ +60% / +36%, θ_u +46% / +28% (p. 6–7, Table 7).
  No jacket spalling and no interface bond failure before peak (p. 3).
- **Fiber origin** (C-2 vs C-3): Japanese-fiber jacket cracked 20 kN later and dissipated 45% more energy at Δu
  (68.69 vs 46.81 kN·m; computed +47%), attributed to its ≈150% higher ultimate tensile strain (p. 3, 8, Table 8).
  P_m was slightly lower (268.6 vs 280.6 kN).
- **Bar mesh in HDC** (C-4 vs C-2): P_m only +2.8%, μ +49.1%; the mesh "affected the continuity of the jacket",
  weakening the HDC's shear contribution (p. 7).
- **HDC vs mortar matrix** (C-4 vs C-5; C-7 vs C-8): P_m −9.5% / −5.0% (mortar stronger in compression), but μ
  +79.5% / +80% and θ_u +73.7% / +85.9% (p. 7). Recomputed from Table 7: θ_u +74% / +83%.
- **Post-peak decay** (push): C-2, C-4, C-5 lost 6.3%, 5.9%, 2.7% of peak per cycle (p. 5).
  ⚠️ The text then calls HDC-B the best for strength retention, which the 2.7% for BMRM C-5 does not support
  (possibly mislabelled).
- **High axial load** (C-7 vs C-6): μ +117%, θ_u +96.3% (§4.5) or +92% (Conclusion 3); recomputed 4.2/2.2 → +91%.
- **Energy** (Table 8, p. 8): HDC-B dissipated 8.81× (C-4 vs C-1) and 7.12× (C-7 vs C-6) more than controls
  ("times higher"; ratios 9.81 and 8.12); C-7 vs C-8: 2.87× higher (ratio 3.85).
- **Cracks:** HDC-B: only fine flexural cracks within 400 mm of the foot at about 80 mm mean spacing; flexural crack
  width within 1 mm throughout (p. 3). HDC-0: multiple fine flexural cracks in the hinge region, but diagonal cracks
  widened continuously (p. 3).
- **Stirrups:** control stirrups yielded before peak; none yielded before peak in HDC-jacketed columns (Fig. 10, p. 7).
- **Hinge curvature** at Δu: C-4 2.13× higher than C-1; C-7 1.75× higher than C-6; C-8 below C-6 (Table 9, p. 9).
  BMRM is "not applicable" for high-axial-load columns (Conclusion 5).

## Mechanisms / explanations offered by authors
- Jacket confinement plus fiber bridging restrains diagonal cracking in the core, delays concrete softening and
  slows strength degradation (p. 4).
- Bar mesh restrains crack opening in the HDC jacket, giving stronger confinement and a flexural hinge (p. 4).
- The high compressive strain capacity of HDC (peak strain about 0.6%) raises the ultimate curvature compared with
  mortar or concrete (p. 4, 9).
- Strain hardening and high compressive strain "are responsible" for the ductility gain of HDC-B over BMRM (p. 7).

## Limitations (stated + observed)
- Stated: earlier ferrocement studies were small-scale; mortar matrix is brittle (p. 2).
- Observed:
  - One specimen per configuration; controls tested at lower axial loads than the jacketed columns.
  - No tension specimen geometry, gauge length or rate; tensile strain only as a figure; HDC curing and test age
    not given.
  - Fiber diameter unit printed as "mm"; concrete and mortar mixes not given.
  - No crack-width measurements beyond "within 1 mm"; no interface bond test.
  - Shear-span ratio 3 (750/250, computed): these are not short columns.
- Internal inconsistencies: C-7 vs C-6 drift gain 96.3% (§4.5) vs 92% (Concl. 3) vs 91% recomputed; post-peak decay
  ranking vs text (above).

## Relation to other work
- Agrees with:
  - [[deng2018-hdc-short-columns]] (same group, same mix proportion): HDC turns brittle shear into a more ductile
    response and prevents cover spalling.
  - [[li2003-ecc-review]]: R/ECC without spalling at large drift (as cited there).
- Contradicts / refines: ⚔️
  - **Tensile strain of the same nominal mix:** about 3.0% ultimate (Japanese PVA, Fig. 1a) here vs about 1.0%
    "ultimate tensile strain" in [[deng2018-hdc-short-columns]] (Fig. 1), with similar σ_tu (6.12 vs 6.14 MPa).
    Fiber source in the 2018 paper is not stated; σ_f 1600 MPa / E 40 GPa there matches the Japanese fiber here.
    Possible reasons: batch, specimen, end-of-curve definition.
  - **He 2024 citation:** [[he2024-hdc-research-advances]] (p. 6) credits "Deng & Zhang 2018" with HDC jacketing of
    **cross-shaped short** columns. This paper is a Deng & Zhang HDC **jacketing** study, but dated 2017, with
    square columns on an inverted-T specimen and shear span ratio 3, so it does not match. A better candidate is
    cited in [[deng2019-urm-shaking-table-hdc]] (ref. [17]): Deng, Zhang & Li 2018, "Shear strengthening of RC short
    columns with ECC jacket: cyclic behavior tests", Eng. Struct. 160:535–45 (not ingested; "cross-shaped" unverified ⚠️).
- Extends:
  - First primary **HDC jacketing** data in the wiki (Chinese PVA-HDC); first comparison of HDC with a
    ferrocement-type (bar-mesh mortar) jacket.
  - First direct evidence in the wiki that the PVA fiber product (Japanese vs Chinese) changes HDC tensile
    strain by about 2.5× in an otherwise identical mix.

## Pages updated from this source
- [[rc-member-strengthening]]
- [[shear-behaviour]]
- [[interface-bond]]
- [[pva-fiber]]
- [[tensile-strain-capacity]]
- [[terminology-hdc-ecc-shcc]]
- [[deng2018-hdc-short-columns]]
- [[he2024-hdc-research-advances]]
- [[mix-designs]]
- [[mechanical-results]]
- [[gaps]]

## To verify
- [ ] Tensile first-crack stress (≈ 5.3 / 4.0–4.5 MPa) and ultimate strains (≈ 3.0 / 1.2%) read from Fig. 1a ⚠️ unverified.
- [ ] Strain at peak tensile stress (not stated; Fig. 1a peak region roughly 1–2% for HDC) ⚠️ unverified.
- [ ] Fiber diameter unit ("mm" printed; 39 µm assumed).
- [ ] Tension specimen geometry, gauge length, number of specimens, rate; HDC curing and test age.
- [ ] Axial load ratios (only forces given; concrete f_c 45.4 MPa cube).
- [ ] Post-peak decay rates 6.3 / 5.9 / 2.7% (C-2 / C-4 / C-5) vs the text's ranking.
- [ ] Whether He 2024's "Deng & Zhang 2018, cross-shaped short columns" is Deng, Zhang & Li 2018 (Eng. Struct. 160:535–45, cited in [[deng2019-urm-shaking-table-hdc]]) rather than this 2017 paper.
- [ ] Whether the 2018 short-column HDC used the Japanese fiber (property values match) and why ε differs (≈ 1.0 vs ≈ 3.0%).
