---
type: source
slug: li2002-pva-ecc-interface-tailoring
title: "Interface Tailoring for Strain-Hardening Polyvinyl Alcohol-Engineered Cementitious Composite (PVA-ECC)"
authors: [Victor C. Li, Cynthia Wu, Shuxin Wang, Atsuhisa Ogawa, Tadashi Saito]
year: 2002
venue: "ACI Materials Journal, V. 99, No. 5, September-October 2002, pp. 463-472 (Title no. 99-M47)"
doi: "not reported in PDF"
raw_file: raw/papers/Li2002_Interface Tailoring for Strain-Hardening Polyvinyl AlcoholEngineered Cementitious Composite (PVA-ECC).pdf
material_term: "ECC (Engineered Cementitious Composite); PVA-ECC; 'strain-hardening cementitious composites' used generically (p. 463)"
study_type: experimental + analytical (micromechanics-guided design)
tags: [ecc, pva-ecc, pva-fiber, oil-coating, fiber-matrix-interface, single-fiber-pullout, chemical-bond, slip-hardening, strain-hardening, psh-index, multiple-cracking, crack-width, coupon-tension, normal-strength-matrix, michigan-group, kuraray]
ingested: 2026-10-16
updated: 2026-10-16
---

# PVA-ECC interface tailoring by fiber oil coating (Li et al., 2002)

## One-paragraph summary
University of Michigan (V.C. Li) and Kuraray Co. show that untreated PVA fiber bonds too strongly to
a cement matrix (high chemical bond Gd and strong slip hardening β). The fiber therefore ruptures
instead of pulling out, which limits the composite strain capacity. Micromechanics (the model of
Lin, Kanda & Li 1999, as cited) gave target ranges for the interface (p. 466). The fiber surface was
then coated with a proprietary oiling agent at five levels: **0, 0.3, 0.5, 0.8 and 1.2%** (oil mass /
fiber mass). The matrix was one cement–fine-sand mortar (w/c 0.45, s/c 0.6, no fly ash) with
2 vol.% PVA (39 µm, 12 mm) (Tables 1–2).

Results:
- Single-fiber pullout at 21 d: τ0 fell from 2.44 to 1.11 MPa, Gd from 4.71 to 1.61 J/m², and β from
  about 2.2–2.3 to 1.15 as oiling rose from 0 to 1.2% (Table 3, Fig. 7).
- The computed PSH index J′b/Jtip rose from 0.73–1.33 to 4.84–7.62 (Table 3).
- Coupon tension at about 14 d: tensile strain capacity rose from 0.99% to **4.88%**, with
  saturated multiple cracking. Crack spacing fell from 27 to about 2.5–2.8 mm, and crack width
  rose from 43 to 88 µm (Table 4).
- The transition to saturated cracking occurred at about 0.8% oiling, where J′b/Jtip reaches
  about 3. This is consistent with the Kanda & Li (1998) criterion (p. 471).

This is the foundational primary source on **classic normal-strength PVA-ECC** in the wiki.

## Objective / research question
- Lower and control the PVA/matrix bond (Gd, τ0, β) so that it falls in micromechanically optimal
  ranges, using an oil coating on the fiber (p. 464).
- Verify at composite level that the tailored interface gives tensile strain hardening with
  > 4% strain capacity at low fiber content (2 vol.%) (p. 463–464).
- Background: off-the-shelf PVA gave only about 0.5–1.0% strain capacity even at up to 4 vol.%
  fiber (refs 15–16, as cited, p. 463).

## Materials & mix design
| Mix ID | Cement | Fly ash | Slag/other | Sand (type, max size) | W/B | SP | Fiber type | L (mm) | d (µm) | Vf (vol.%) |
|---|---|---|---|---|---|---|---|---|---|---|
| PVA-ECC, oil 0 / 0.3 / 0.5 / 0.8 / 1.2% | 1 (Type I portland) | 0 | none; methyl cellulose viscosity agent 0.15; defoamer 0.05% | F110 silica sand, 50–150 µm (max 0.15 mm); s/c = 0.6 | 0.45 (w/c; no SCM, so W/B = w/c) | HRWR 2.0% | PVA (Kuraray), oil-coated | 12 | 39 | 2 |

Units of binder quantities: mass ratio to cement (Table 2). The paper gives `w/c` and `s/c` without
saying "by mass", and gives the SP, viscosity-agent and defoamer dosages without saying what they are
a percentage of. ⚠️ unverified: assumed by mass of cement. The viscosity agent value 0.15 has no unit in Table 2.
No kg/m³ quantities are reported.

**Fiber properties** (Table 1, p. 466):

| Property | Value |
|---|---|
| Nominal strength | 1620 MPa |
| Apparent strength (embedded in matrix) | 1092 MPa |
| Diameter | 39 µm |
| Length | 12 mm (continuous fiber in pullout tests) |
| Young's modulus | 42.8 GPa |
| Elongation | 6.0% |
| Density | not reported |

**Oil coating** (p. 466): proprietary oiling agent that reduces the hydrophilicity of the fiber
surface. Levels are 0, 0.3, 0.5, 0.8 and 1.2% (oil mass / fiber mass). The manufacturer states the
layer is about 100 nm thick and adheres strongly, so little coating should be lost in mixing.

**Mixing** (p. 466–467): planetary mixer. The order is:
1. Dry-mix cement, sand and defoamer for 1–2 min.
2. Add water and mix for 2 min.
3. Add the methyl-cellulose solution and mix for about 10 min.
4. Add the HRWR and mix at high speed for 1–2 min.
5. Add the fibers by hand.

## Test methods
- **Specimen geometry:**
  - Composite: rectangular coupon 304.8 × 76.2 × 12.7 mm (L × W × H), gauge length about
    185 mm, 3–4 specimens per mix (p. 466).
  - Interface: single continuous fiber cast in matrix, then saw-cut to the embedment length
    (Fig. 4; method of Katz & Li 1996, as cited). Embedment 0.56–0.71 mm (Fig. 3 caption), free
    fiber length ≤ 1 mm (p. 467).
- **Loading / rate:**
  - Tension: 25 kN frame, fixed hydraulic grips, epoxy-glued aluminium end plates,
    0.0025 mm/s displacement control throughout (p. 467).
  - Pullout: 10 N load cell (1.97 N range), 0.02 mm/s (p. 467). The displacement at peak
    debonding load Pa (about 0.1 mm) was subtracted from slip when computing β.
- **Measurement:**
  - Two LVDTs over about 185 mm (p. 467).
  - Crack width measured after unloading with an optical microscope at 200×; the final failure
    crack was excluded (p. 467).
  - Crack spacing x_d = 150 mm / number of cracks in the central 150 mm. More than 60 cracks
    were counted in saturated specimens (p. 467).
  - τ0, Gd and β were extracted from the pullout curves per Lin, Kanda & Li 1999 (as cited, p. 467).
- **Curing & test age:**
  - Composite: demoulded at 24 h, water tank at room temperature for about 14 d, out of water 1 d
    before testing. The authors cite that tensile properties change little after 7 d (ref 24,
    as cited, p. 467).
  - Pullout: demoulded at 48 h, wrapped in wet cloth at 50–60% RH, tested at 21 d after 1 d of
    drying (p. 466).
  - The two test ages differ (about 14–15 d vs 21 d).
- The specimen thickness (12.7 mm) is about the fiber length (12 mm). Fiber orientation may
  cluster in-plane, so the authors restrict their strain values to this specimen configuration (p. 469).

→ [[single-fiber-pullout-test]], [[dogbone-uniaxial-tension]] (this study uses a rectangular coupon, not a dogbone)

## Key results
### Interface properties vs oiling (Table 3, Fig. 7, p. 468; mean ± SD)
| Oiling (%) | τ0 (MPa) | Gd (J/m²) | β | J′b (J/m², computed) | J′b/Jtip (Jtip = 5 J/m² assumed) |
|---|---|---|---|---|---|
| 0.0 | 2.44 ± 0.49 | 4.71 ± 0.58 | 2.21 ± 0.71 | 3.64–6.63 | 0.73–1.33 |
| 0.3 | 2.15 ± 0.19 | 3.16 ± 0.66 | 2.31 ± 0.19 | 5.17–13.8 | 1.03–2.76 |
| 0.5 | 2.14 ± 0.15 | 2.96 ± 0.75 | 1.82 ± 0.23 | 7.68–13.6 | 1.54–2.72 |
| 0.8 | 1.98 ± 0.13 | 2.18 ± 0.39 | 1.18 ± 0.34 | 12.5–20.7 | 2.50–4.14 |
| 1.2 | 1.11 ± 0.13 | 1.61 ± 0.60 | 1.15 ± 0.17 | 24.2–38.1 | 4.84–7.62 |

Targets from micromechanics (Wu 2001 thesis, as cited, p. 466): **Gd < 2.2 J/m²; τ0 = 1.0–2.1 MPa; β < 1.5**,
for Jtip = 5 J/m². Only the 0.8% and 1.2% oiling levels meet the Gd and β targets (Fig. 7).

### Composite tension vs oiling (Table 4, Figs. 10–12, p. 469; mean ± SD; age about 14 d)
| Mix ID | f'c (MPa) | First-crack stress (MPa) | Tensile strength (MPa) | Tensile strain capacity (%) | Crack width (µm) | Other |
|---|---|---|---|---|---|---|
| Oil 0.0% | not reported | 3.11 ± 0.23 | 4.89 ± 0.07 | 0.99 ± 0.57 | 43 ± 20 | spacing 27.00 ± 12.00 mm (15–40 mm); few cracks |
| Oil 0.3% | not reported | 2.63 ± 0.43 | 4.72 ± 0.17 | 1.55 ± 0.33 | 44 ± 7 | spacing 7.50 ± 2.80 mm; unsaturated cracking |
| Oil 0.5% | not reported | 2.35 ± 0.21 | 4.09 ± 0.22 | 2.73 ± 0.78 | 52 ± 10 | spacing 3.50 ± 1.10 mm; one specimen 3.8% |
| Oil 0.8% | not reported | 2.90 ± 0.10 | 4.62 ± 0.36 | 3.81 ± 1.14 | 71 ± 9 | spacing 2.50 ± 0.33 mm; one specimen > 5%; near-saturated |
| Oil 1.2% | not reported | 2.92 ± 0.06 | 4.41 ± 0.15 | **4.88 ± 0.59** | 88 ± 12 | spacing 2.80 ± 0.52 mm; most consistent |

Notes on Table 4:
- The tensile-strength column is labelled "First tensile strength σcu". It is read here as the
  ultimate tensile strength. ⚠️ unverified wording.
- The strain capacity εcu is not explicitly defined as being at peak stress or at failure.
  ⚠️ unverified (Fig. 10 suggests it is near the end of the hardening branch).
- The spacing column is mislabelled "Crack opening x_d, mm". The text (p. 467) defines x_d as crack spacing.
- Crack width is the residual width, measured after testing (p. 467).

Computed here (σ_tu/σ_fc): 1.57 / 1.79 / 1.74 / 1.59 / 1.51 for 0 / 0.3 / 0.5 / 0.8 / 1.2% oiling.

Main findings (with Table/Fig. location):
- Oiling reduces all three interface parameters. The drop is largest for Gd (−66%, 4.71 → 1.61 J/m²)
  (Table 3, p. 468).
- Non-oiled PVA fibers show severe delamination and rupture with a "pencil-sharpened" end. At 0.8%
  oiling, delamination nearly disappears and the fiber slides out with little damage (Fig. 8, p. 468; Fig. 3, p. 465).
- Strain capacity rises almost linearly with oiling, from about 1.5% to almost 5% (p. 469; Fig. 12a).
- Between 0.3% and 0.5% oiling, the gain comes from more cracks (spacing 7.5 → 3.5 mm).
  Between 0.5% and 0.8%, it comes mainly from wider cracks (52 → 71 µm).
  From 0.8% to 1.2%, spacing no longer falls, so saturation is reached at about 0.8% (p. 469–471).
- J′b/Jtip reaches about 3 at about 0.8% oiling, which coincides with crack saturation. This
  supports the Kanda & Li (1998, ref 25) criterion J′b/Jtip > 3 for saturated cracking. That
  criterion had been derived from PE-ECC (p. 471).
- The measured Jtip of this matrix is **4.5–7.2 J/m²** (p. 470). The analysis assumed 5 J/m².
- Computed J′b falls almost linearly with Gd, by 54% from Gd = 1 to 5 J/m² (Wu 2001, as cited; Fig. 2b, p. 465).
- Pulled-out fiber length on the fracture surface averages about 2 mm at 1.2% oiling. In the
  non-oiled composite most fibers are below 1 mm. Complete pullout would average 3 mm for 12 mm
  random fibers, so some rupture still occurs at 1.2% (Fig. 13, p. 471).
- Lower Gd, τ0 and β reduce the bridging stiffness, which explains the larger crack widths at
  higher oiling (p. 471; Fig. 12c).
- Earlier PVA single-fiber pullout gave Gd = 3–5 J/m² (Lin, Kanda & Li, as cited). PP fiber has
  Gd = 0 (p. 465).

## Mechanisms / explanations offered by authors
- **Hydroxyl groups** in PVA give a strong chemical bond with cement hydrates. The high debonding
  load raises the fiber stress and causes rupture. Gd also shifts the start of the σ(δ) curve
  upward, which reduces J′b (p. 464–465).
- **Slip hardening:** surface fibrillation and jamming during pullout raise J′b when moderate.
  When excessive, fiber delamination ("shaving") causes premature rupture. Rupture can occur even
  after full debonding (Redon et al. 2001, as cited; Fig. 9, p. 465–468).
- **Energy criterion:** steady-state flat cracking needs Jtip ≈ Km²/Em ≤ J′b = σ0δ0 − ∫₀^δ0 σ(δ)dδ
  (Eqs. 1–2, p. 464–465). The fiber/interface properties control the shape of σ(δ) and therefore J′b.
- **Oil coating** reduces surface hydrophilicity and so lowers all three bond parameters (p. 466, 468).
- **Holistic tailoring:** the optimal sand content depends on the oiling level, through Km and the
  flaw distribution (Li, Wang & Wu 2001, as cited, p. 472).
- Extrusion would give a denser interphase and need more oiling. Fly ash may also change the PVA
  interface; combined use of oil and fly ash needs study (p. 472).

## Limitations (stated + observed)
- Stated:
  - The strain values apply only to this coupon geometry (12.7 mm thick, close to L_f) (p. 469).
  - Material variability is important for this fiber (0.5% oiling: one specimen 3.8% vs mean 2.7%) (p. 469).
  - The optimal oiling depends on the processing route (p. 472).
  - Only one matrix was used. Fly ash was not studied (p. 472).
- Observed:
  - No compressive strength, Km or Em is reported for the matrix. Jtip is given only as a range (4.5–7.2 J/m², p. 470).
  - σ0 and δ0 are not reported. J′b is a computed range, not measured from single-crack tests.
  - Small sample size (3–4 coupons per mix). The test ages differ (composite about 14 d, pullout 21 d).
  - Internal inconsistencies:
    - β of non-oiled fiber: "as high as 2.9" (p. 468) vs Table 3 mean 2.21 ± 0.71.
    - τ0 target range: 1.0–2.1 MPa (p. 466) vs 1.0–2.0 MPa (p. 471).
    - Crack spacing: text gives 8 mm and 4 mm for 0.3/0.5% (p. 469), while Table 4 and p. 469–470 give 7.5 and 3.5 mm.
    - Fig. 11 caption strains (0.9/1.9/2.8/3.6/4.7%) are for individual specimens and differ from the Table 4 means.
  - The SEM labels in Fig. 8 read "w/c=0.38" and "w/c=0.32", not the 0.45 matrix of Table 2. The
    images may come from other tests. ⚠️ unverified.
  - The oiling agent is proprietary (composition not given). DOI not printed.
  - No durability, long-term or rate data.

## Relation to other work
- Agrees with:
  - [[yang2024-hshdc-uniaxial-tension]] (p. 8): untreated or strongly bonded PVA in a dense
    matrix tends to rupture, which gives low strain capacity. Here an untreated PVA-ECC gives 0.99%;
    Xi'an PVA-HSHDC (W/B 0.16) gives 0.23–0.30%.
  - [[ranade2015-hshdc-tensile-rate-effects]]: PVA has a chemical bond (Gd > 0), while PE has
    friction only (Gd ≈ 0).
  - [[strain-hardening]]: J′b/Jtip > 3 for saturated cracking (Kanda & Li 1998) is confirmed here
    for PVA-ECC (p. 471).
- Contradicts: ⚔️
  - β ≈ 0.6 "for ECC" (Wang & Li 2007, as cited in [[ranade2015-hshdc-tensile-rate-effects]], p. 98)
    vs β = 1.15–2.31 measured here (Table 3). This is probably a different fiber/oiling/matrix,
    so it is a refinement rather than a true conflict.
  - Composite-level σ_tu/σ_fc is about 1.5–1.6 even for the 0% oiled mix, which reaches only 0.99%.
    The strength ratio alone did not predict ductility here; the energy index separated the mixes.
- Extends:
  - First primary interface data (τ0, Gd, β) for **PVA**, and for a **normal-strength ECC matrix**,
    in the wiki. Until now only the Michigan PE-HSHDC had pullout data.
  - Fills the "classic normal-strength PVA-ECC" gap on [[pva-fiber]] and [[gaps]]. Note that it is
    ECC (Michigan), not Chinese "HDC".

## Pages updated from this source
Proposed for update (by the ingest orchestrator):
- [[pva-fiber]] · [[fiber-matrix-interface]] · [[strain-hardening]] · [[multiple-cracking]] ·
  [[fiber-bridging]] · [[crack-width]] · [[tensile-strain-capacity]] · [[single-fiber-pullout-test]] ·
  [[dogbone-uniaxial-tension]] · [[terminology-hdc-ecc-shcc]] · [[matrix-fracture-toughness]] ·
  [[mix-designs]] · [[mechanical-results]] · [[micromechanical-parameters]] · [[gaps]]

## To verify
- [ ] DOI is not printed in the PDF. Look it up (ACI Materials Journal 99(5), 463–472, Title no. 99-M47).
- [ ] Whether w/c and s/c are by mass, and what SP 2.0%, viscosity agent 0.15 and defoamer 0.05% are percentages of (Table 2).
- [ ] Whether εcu is at peak stress or at failure, and whether "First tensile strength σcu" means ultimate strength (Table 4).
- [ ] β of non-oiled fiber: 2.9 (text, p. 468) vs 2.21 ± 0.71 (Table 3). Possibly a maximum vs a mean.
- [ ] τ0 target 1.0–2.1 MPa (p. 466) vs 1.0–2.0 MPa (p. 471).
- [ ] Crack spacing for 0.3/0.5% oiling: 8 / 4 mm (text p. 469) vs 7.5 / 3.5 mm (Table 4).
- [ ] The Fig. 8 SEM labels show w/c = 0.38 / 0.32, not 0.45. Check which matrix these images represent.
- [ ] Exact composite test age: "approximately 14 days" water curing plus 1 d out of water (p. 467).
