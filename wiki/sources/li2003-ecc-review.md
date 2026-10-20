---
type: source
slug: li2003-ecc-review
title: "On Engineered Cementitious Composites (ECC): A Review of the Material and Its Applications"
authors: [Victor C. Li]
year: 2003   # Vol. 1, No. 3, November 2003; received 25 Apr 2003, revised 14 Aug 2003
venue: "Journal of Advanced Concrete Technology (Japan Concrete Institute), Vol. 1, No. 3, pp. 215-230, November 2003 (Invited Paper; based on a keynote at the JCI DFRCC Workshop, Takayama, Oct 2002)"
doi: "not printed in the PDF (⚠️ unverified: likely 10.3151/jact.1.215)"
raw_file: raw/papers/Li2003_On-ECC-review.pdf
material_term: "ECC (Engineered Cementitious Composites); PVA-ECC; R/ECC for reinforced ECC members; cited works also use 'pseudo strain hardening cementitious composites', 'DFRCC', 'HPFRCC' and 'highly ductile fiber-reinforced cement-based composites'"
study_type: review (narrative, author-centred; few new data)
tags: [ecc, pva-ecc, review, design-philosophy, micromechanics, steady-state-cracking, critical-fiber-volume, isdm, pdda, r-ecc, shear, link-slab, repair, seismic, damper, crack-width, cost, standardisation, michigan-group, kuraray, rec15]
ingested: 2026-10-20
updated: 2026-10-20
---

# On ECC: review of the material and its applications (Li, 2003)

## One-paragraph summary
An invited 16-page review by V.C. Li (Univ. of Michigan, ACE-MRL) of the first decade of ECC
(invented "early 1990's", p. 215). It argues that ECC is defined by a **micromechanics-based design
method**, not by a recipe: the fiber-bridging σ–δ curve must satisfy a **strength criterion**
(cracking strength < σcu) and an **energy criterion** (complementary energy large relative to crack-tip
toughness, giving flat steady-state cracks) (p. 217, Figs. 3–5). Micromechanics is used to minimise
the **critical fiber volume fraction** for cost and processability; for PVA this was done by oil
coating, giving Kuraray's **REC15** fiber and about 5% tensile strain at 2 vol.% (p. 219–220,
Figs. 7–8, reproduced from Li et al. 2002b = [[li2002-pva-ecc-interface-tailoring]]). Sections 4–5
review, **all as cited**, why ductility rather than compressive strength governs structural strength,
and the behaviour of reinforced ECC (R/ECC): reduced shear reinforcement, deformation compatibility
with steel, synergy with FRP bars, damage tolerance and tight crack width (< 100 µm with PVA;
about 80 µm, Fig. 15). Section 5.2 lists the early **target applications**: seismic elements (beams,
columns, hybrid joints, self-centring frames, infill panels, bridge piers, dampers) and **repairs in
Japan, Korea, Switzerland and the US**. Sections 6–8 cover cost, the ECC Technology Network, and ten
R&D needs (standard mix, pre-mix, performance specifications, standard tension test, etc.). The
paper gives **no mix proportions and no data tables**.

## Objective / research question
Survey ECC R&D "over the last decade", from materials design theory to commercial application
(Fig. 1), stress the role of micromechanics, and set out future challenges (Abstract; p. 215).

## Materials & mix design
**Not reported.** The paper gives no mix proportions, no W/B, no binder or sand data, and does not
mention any "M45" mix. Fiber information only:

| Mix ID | Cement | Fly ash | Slag/other | Sand (type, max size) | W/B | SP | Fiber type | L (mm) | d (µm) | Vf (vol.%) |
|---|---|---|---|---|---|---|---|---|---|---|
| PVA-REC15 ECC (Figs. 2, 7b, 8, 15) | not reported | not reported | not reported | not reported | not reported | not reported | PVA (Kuraray "KII", oil-coated → REC15; coating 1.2% in Figs. 7–8, 0.8% in Fig. 15) | not reported | not reported | 2 |

Units of binder quantities: n/a (no quantities given).
- General statement: ECC uses a "moderately low fiber volume fraction less than 2-3%" with a suitable
  matrix design (p. 216).
- Fly ash is suggested for cost reduction, with a warning that it changes interface and matrix
  properties (p. 226).
- Fiber and matrix data for REC15 are in [[li2002-pva-ecc-interface-tailoring]] (Table 1 there).

## Test methods
- Specimen geometry: not reported for the ECC curves (Figs. 2, 8, 15). Fig. 12: concrete–ECC–concrete
  sandwich in uniaxial tension (geometry not reported).
- Loading / rate: uniaxial tension (Figs. 2, 8, 12, 15); single-fiber pull-out (Fig. 7a, as cited);
  structural tests are all as cited (fully reversed cyclic loading).
- Measurement (LVDT, DIC, ...): not reported.
- Curing & test age: not reported, except Fig. 12b "water curing 28 days".
→ [[dogbone-uniaxial-tension]] · [[single-fiber-pullout-test]]

## Key results
"Own" = Michigan/ACE-MRL figures shown in this paper (mostly reproduced from earlier Li-group papers);
"as cited" = attributed to other authors.

| Mix ID | f'c (MPa) | First-crack stress (MPa) | Tensile strength (MPa) | Tensile strain capacity (%) | Crack width (µm) | Other |
|---|---|---|---|---|---|---|
| 2% PVA-REC15 (Fig. 2; Fig. 8b, 1.2% coating) | not reported | ≈ 3–3.5 (read from Fig. 2/8b) | ≈ 4–4.5 (read from figure) | "about 5%" (ultimate; curves end ≈ 4.3–5.3%) | — | Fig. 2 text cites Li et al. 2001; Fig. 8b is from Li et al. 2002b |
| 2% PVA, 0% coating (Fig. 8a) | not reported | — | ≈ 4.5–5 (read from figure) | ≈ 0.5–1.7 (curves); "1%" (Fig. 7b) | — | fiber rupture; from Li et al. 2002b |
| 2% REC15, 0.8% coating (Fig. 15) | not reported | — | — | specimen to ≈ 4.4% | "about 80" steady state beyond ≈ 1% strain (data points read ≈ 70–76) | crack width vs strain |
| ECC strip in concrete sandwich (Fig. 12b) | not reported | ≈ 2.5 (read) | ≈ 3.5 (read) | overall 1.3% with no cracks in the concrete | — | 28 d water curing; Zhang et al. 2002 (Li co-author) |

Main findings (with Table/Fig. location):
- ECC tensile strain capacity of 5% is "approximately 500 times" that of normal concrete or FRC
  (p. 215, Fig. 2).
- Optimal frictional bond τ0 for PVA "KII" at 2% fiber is **1–2 MPa**; this needs a coating content of
  0.6–1.2% (Fig. 7a caption) or 0.8–1.2% (text, p. 219) ⚠️ internal inconsistency. With 0.8–1.2%
  coating the **critical fiber volume fraction falls to a minimum of about 2%** (p. 219).
- ε rises from 1 to 5% as coating rises from 0 to 1.2% (Fig. 7b); untreated fibers are damaged by
  delamination during pull-out, while coated fibers are protected (Fig. 9).
- Crack width is "generally less than 100 micron when PVA fiber is used" and stabilises at about
  80 µm beyond about 1% strain (p. 224, Fig. 15).
- **Structural results, all as cited:**
  - Precast infill panels under cyclic shear: concrete panel (f'c 50 MPa) 38 kN vs ECC panel
    (f'c 41 MPa) 56 kN, a gain of "over 35%" (Kesner & Billington 2002, as cited, p. 221).
    ⚠️ (56−38)/38 = 47%, so "over 35%" is an under-statement or uses another basis.
  - FE analysis: an ECC wall panel had 3× the structural strength of an FRC panel with the same
    tensile and compressive strengths (Kabele 2001, as cited, p. 221).
  - R/ECC flexural members **without stirrups** exceeded R/C **with stirrups** in load capacity and
    energy absorption under cyclic loading; no ECC spalling at 10% drift (Fischer & Li 2002b, as
    cited, p. 222, Figs. 10–11).
  - ECC beams without shear reinforcement outperformed HSC beams with closely spaced stirrups
    (Li & Wang 2002, as cited, p. 222).
  - Steel-beam/RC-column hybrid joint: no fracture with ECC despite removal of all stirrups; severe
    spalling with concrete (Parra-Montesinos & Wight 2000, as cited, p. 224, Fig. 14).
  - GFRP-reinforced ECC beams: better ductility, capacity, shear resistance and damage control than
    HSC counterparts (Li & Wang 2002, as cited, p. 223–224).
  - ECC is "remarkably notch insensitive" in tension (Li 1997, as cited, p. 224).
  - ECC fatigue resistance is "significantly higher" than polymer repair mortars (Suthiwarapirak
    et al. 2002, as cited, p. 225).
  - Full-scale test showed the ECC **link-slab** is feasible (Kim et al. 2003b, as cited, p. 222).
  - Energy absorption of R/ECC comes mainly from longer plastic yielding of the steel and more
    stable hysteresis, not from ECC ductility directly (Fischer & Li 2002a, as cited, p. 225).

### Early applications listed (p. 225, Sect. 5.2) — names and locations only, no details given
| Class | Application | Country / place | Citation in paper |
|---|---|---|---|
| Repair (planned) | Dam repair | Japan | none given |
| Repair (planned) | Bridge underdeck | Japan | none given |
| Repair (planned) | Sewage line | Korea | none given |
| Repair (planned) | Tunnel linings | Switzerland | none given |
| Repair (planned) | Concrete bridge decks | US | none given (Lepech et al. 2003 on bridge deck repair is in the reference list, p. 228) |
| Seismic | Beam elements | — | Fukuyama et al. 1999; Kanda et al. 1998 |
| Seismic | Column members | — | Fischer et al. 2002 |
| Seismic | Hybrid steel beam–RC column connections | — | Parra-Montesinos & Wight 2000 |
| Seismic | Self-centring "smart" / auto-adaptive frames (steel + FRP R/ECC) | — | Fischer & Li 2003b |
| Seismic retrofit | Precast infill panels for open frames | — | Kanda et al. 1998; Kesner & Billington 2002; Horii et al. 1998 |
| Seismic | Precast segmental bridge piers (unbonded post-tensioned, ECC hinge zones) | — | Yoon & Billington 2002 |
| Seismic | Damping elements ("HPFRCC damper") | — | Fukuyama et al. 2002 |
| Durability | Bridge-deck link slabs replacing joints | US (MDOT-funded) | Zhang et al. 2002; Kim et al. 2003b; Li et al. 2002a |
| Productivity | Spraying (repair, tunnel lining), extrusion, self-compacting ECC | — | Kanda et al. 2001; Kim et al. 2003a; Stang & Li 1999; Takashima et al. 2003; Kong et al. 2003 |

- Countries named as nearing commercialisation: Japan, Korea, Australia, Switzerland, US (p. 216).
- ECC is "finding its way into precast plants, construction sites, and repair and retrofitting jobs"
  (p. 215).

## Mechanisms / explanations offered by authors
- **σ–δ curve** is the most fundamental property; its shape depends on fiber Vf, d, L, strength,
  modulus and interface chemical/frictional bond (p. 217–218).
- **Strength criterion:** matrix cracking strength (governed by flaw size) < σcu.
  **Energy criterion:** complementary energy C (area left of the σ–δ curve, Fig. 4) must be large
  relative to crack-tip toughness, giving a flat steady-state crack with δss < δp (Li & Leung 1992;
  Fig. 5). Too weak an interface → pull-out with low σcu; too strong → rupture with small δp; both
  give small C (p. 217).
- **Critical fiber volume fraction:** the minimum Vf that switches tension-softening FRC to
  strain-hardening ECC; use Vf just above it for optimum cost, performance and processability
  (p. 218–219).
- **Design philosophy:** Performance Driven Design Approach (PDDA, Li 1992a) + Performance Based Design
  Concept (PBDC, SEAOC 1995) = **Integrated Structures and Materials Design (ISMD)** (Li & Fischer 2002),
  with the σ–δ curve and σ–ε law as the interface (Fig. 6). "Engineered" refers to deliberate
  tailoring, not to a fixed composition (p. 216, 220).
- **Strength vs ductility:** if tensile fracture governs, a ductile lower-strength material can give
  a higher structural strength (p. 220–221).
- **Deformation compatibility:** steel and ECC both deform plastically, so there is no shear lag, low
  interfacial bond stress, and no bond splitting or cover spalling (p. 222, Fig. 13).
- **Durability:** 100 µm is a threshold above which water flow through cracks becomes appreciable
  (Tsukamoto 1990; Wang et al. 1997; Lawler et al. 2002, as cited, p. 225). ECC can stay below it, so
  it may act as a durable cover, but "further research is needed to directly confirm" reduced steel
  corrosion (p. 225).
- **Repair:** ECC absorbs interface defects without spalling or delamination (Lim & Li 1997, as cited,
  p. 225).
- **Cost:** extra cost comes from fibers and high cement content; PVA is dearer per kg than steel but
  6–7× less dense, and performance depends on fiber volume, not mass (p. 226).

## Limitations (stated + observed)
- Stated: durability benefit of tight cracks for corrosion not yet confirmed (p. 225); no standard
  mix, performance specification or tension test method (p. 227); specimen size and geometry
  effects on tension results need study (p. 227).
- Observed: narrative review centred on the author's own group; **no mix designs, no tables, no
  compressive strengths, no test ages** for the ECC curves.
- Observed: Fig. 2 (cited to Li et al. 2001) shows curves that appear identical to Fig. 8b (from
  Li et al. 2002b) ⚠️.
- Observed: applications are listed without project names, dates, quantities or performance data.
- Observed: the 2003 statements on freeze–thaw, shrinkage, fatigue and creep are claims with
  citations only; no values.

## Relation to other work
- Agrees with: [[li2002-pva-ecc-interface-tailoring]] (oil coating 0 → 1.2% raises ε about 1 → 5%;
  the same Figs. 7–8 are reproduced). [[li1992-steady-state-multiple-cracking]] (steady-state
  flat-crack criterion, critical Vf). [[ma2021-ecc-durability-review]] (crack width < 100 µm).
- Contradicts: ⚔️ none in values. Refinement: the wiki's "Li 2003 as cited, σ_tu 3–8 MPa and ε up
  to 5%" in [[yu2018-ecc-direct-tensile-review]] — this paper states ε "about 5%" (Fig. 2) but gives
  **no 3–8 MPa range**; that range may come from another Li 2003 paper ⚠️.
- Extends: the wiki's application pages, with the earliest list of ECC structural and repair uses
  (Sect. 5.2) and the ten R&D needs of 2003 (Sect. 8).

## Pages updated from this source
- [[terminology-hdc-ecc-shcc]]
- [[strain-hardening]]
- [[steady-state-cracking]]
- [[fiber-bridging]]
- [[fiber-surface-treatment]]
- [[pva-fiber]]
- [[crack-width]]
- [[durability]]
- [[fatigue]]
- [[rc-member-strengthening]]
- [[extreme-loading-applications]]
- [[review-outline]]

## To verify
- [ ] DOI (not printed in the PDF; likely 10.3151/jact.1.215) ⚠️ unverified.
- [ ] Required coating content: 0.6–1.2% (Fig. 7a caption) vs 0.8–1.2% (text, p. 219).
- [ ] Panel strength gain: 38 → 56 kN is +47%, but the text says "over 35%" (p. 221).
- [ ] Fig. 2 (attributed to Li et al. 2001) looks identical to Fig. 8b (Li et al. 2002b).
- [ ] Fig. 15 crack width: text says "about 80 micron"; plotted points read ≈ 70–76 µm.
- [ ] Source of the "σ_tu 3–8 MPa" range attributed to Li 2003 in [[yu2018-ecc-direct-tensile-review]].
- [ ] Fiber L and d of REC15 are not given here; values in the wiki come from [[li2002-pva-ecc-interface-tailoring]].
- [ ] Field applications (dam, bridge underdeck, sewage line, tunnel lining, bridge decks) are "planned repairs" with no references; obtain primary reports.
