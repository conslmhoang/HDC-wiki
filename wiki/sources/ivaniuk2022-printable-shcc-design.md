---
type: source
slug: ivaniuk2022-printable-shcc-design
title: "Application-Driven Material Design of Printable Strain Hardening Cementitious Composites (SHCC)"
authors: [Egor Ivaniuk, Irina Ivanova, Dmitrii Sokolov, Zlata Tošić, Martin Friedrich Eichenauer, Daniel Lordick, Viktor Mechtcherine]
year: 2022            # Materials 15(5), 1631 (March 2022 issue); published online 22 Feb 2022 (received 2 Feb, accepted 17 Feb 2022) (p. 1)
venue: "Materials (MDPI) 15(5) (2022) 1631"
doi: "10.3390/ma15051631"
raw_file: raw/papers/Ivaniuk2022_printable-SHCC-design.pdf
material_term: "SHCC (Strain Hardening Cementitious Composite), 'also known as ECC' (Section 1, p. 3). Printable PE-SHCC (Dyneema SK60, 6 mm, 1.5 vol.%), high-strength matrix (f'c about 73–83 MPa printed 40 mm cubes, 28 d), cured wrapped at 20 °C / 65% RH. Not called HDC."
study_type: experimental
tags: [shcc, ecc, 3d-printing, pe-fiber, fly-ash, silica-fume, cellulose-ether, starch-ether, viscosity-modifying-admixture, water-retention, adhesiveness, surface-roughness, anisotropy, shell-modules, acdc, tu-dresden]
ingested: 2026-10-20
updated: 2026-10-21
---

# Application-driven design of printable SHCC (Ivaniuk et al., 2022)

> Re-checked against the publisher PDF (18 pp.) on 2026-10-21: page numbers added, figure values read off
> (marked ≈), all table values confirmed.

## One-paragraph summary
TU Dresden (Mechtcherine group) developed a printable PE-SHCC for the outer contours of prefabricated
shell modules in the DFG "Adaptive Concrete Diamond Construction" (ACDC) project (Section 1, p. 2, Fig. 1).
Starting from the Ogura et al. (2018) printable SHCC (reference "Ref", W/B 0.212), they added starch
ether (SE, W/B 0.220) and starch + cellulose ether (SE-CE, W/B 0.250, more cement) to extend open
time, shape stability and surface quality (Section 2.1, pp. 4–5, Table 1). SE-CE kept workability longest
(spread loss 5.5% vs 12.7% for Ref after 3 h, p. 9) and retained most water (Figs. 8, 10, pp. 9–10), and its printed
surface was smoother (Sa 411 vs 772 µm, p. 13, Fig. 15). Compressive strength (about 73–83 MPa at 28 d)
and flexural strength (17–22 MPa) were similar to Ref (Tables 2–3, p. 14). Both mixes strain-hardened with
strain capacity 2–3%, but σ_tu fell from 5.4 (Ref) to 4.1 MPa (SE-CE, −24%), attributed to the higher
W/B (Section 3.2.3, pp. 14–15, Fig. 17). Three adhesiveness tests (tack, cylinder pull, inclined table) failed
to reproduce the observed ranking because of bleed water (Section 3.1.3, pp. 11–12).

## Objective / research question
- Develop a printable SHCC meeting ACDC requirements: mechanical performance, shape stability,
  smooth surface (for direct module-to-module contact without milling) and low shrinkage (Section 1, pp. 2–3).
- Test whether starch ether and cellulose ether achieve this, and evaluate tests for fresh-state
  adhesiveness (Sections 2.2, 3.1).

## Materials & mix design
Constituents (Section 2.1, pp. 4–5): CEM I 52.5 R (Holcim); fly ash Steament H-4; microsilica Emsac 500E
(suspension); quartz sand 0.06–0.2 mm (30 vol.% of sand) and 0–1 mm (70 vol.%), total sand 11.3 vol.%
of concrete; superplasticizer MasterGlenium SKY 593 (same dosage by binder mass); starch ether Starvis
SE 35 F (0.023% by binder mass); cellulose ether Tylose MH 300 P2 (0.075% by binder mass); PE fiber
**Dyneema SK60, L = 6 mm, 1.5 vol.%** (diameter not reported).

Binder by mass: Ref and SE = 60% CEM I + 25% FA + 15% microsilica (solids); SE-CE = 70 / 15 / 15 (p. 4).

| Mix ID | Cement | Fly ash | Slag/other | Sand (type, max size) | W/B | SP | Fiber type | L (mm) | d (µm) | Vf (vol.%) |
|---|---|---|---|---|---|---|---|---|---|---|
| Ref | 907 | 378 | microsilica suspension 454 | quartz 91 (0.06–0.2) + 213 (0–1 mm); max 1 mm | 0.212 (stated) | 29.77 | PE (Dyneema SK60) | 6 | not reported | 1.5 (15.46 kg/m³) |
| SE | 895 | 373 | microsilica susp. 448; starch ether 0.34 | same | 0.220 | 29.37 | same | 6 | not reported | 1.5 |
| SE-CE | 1013 | 217 | microsilica susp. 434; starch ether 0.33; cellulose ether 1.09 | same | 0.250 | 28.50 | same | 6 | not reported | 1.5 |

Units of binder quantities: kg/m³ (Table 1, p. 5). Added water: Ref 74, SE 84, SE-CE 125 kg/m³.
- The stated W/B evidently includes the water of the microsilica suspension: Ref binder =
  907/0.60 ≈ 1512 kg/m³, so microsilica solids ≈ 227 kg/m³ and the suspension ≈ 50% solids (computed
  here; same 50% for SE and SE-CE). Computed check: (added water + suspension water + ≈70% of SP mass) / binder
  = 0.212 / 0.220 / 0.250 for Ref / SE / SE-CE, matching the stated W/B; without SP water it would be
  0.199 / 0.206 / 0.236. So W/B probably also counts the SP water (SP solids content not stated) ⚠️ unverified.
  FA/C by mass: Ref 0.42, SE 0.42, SE-CE 0.21 (computed).
- Reference mix based on Ogura et al. 2018 (ref. 23): σ_tu about 5 MPa, strain capacity about 3%
  (as cited, Section 2.1, p. 3).

## Test methods
- **Fresh:**
  - flow table EN 1015-3 every 20 min up to 3 h (remixed 30 s every 10 min), spread before and after 15 strokes (p. 5);
  - water retention DIN 18555-7 (filter paper, 5–20 min, Eq. 1, p. 5);
  - adhesiveness: tack test (50 mm steel cylinder, 6 mm immersion, 30 mm/min, n = 8), cylinder pull
    test (25 mm, 20 mm immersion, 150 mm/min, n = 6), inclined table test (sliding angle on steel plate) (pp. 6–7).
- **Printing:** gantry printer 1.4 × 1.0 × 1.2 m; 50 mm/s; vertical nozzle 55 × 25 mm with side and top
  steel trowels; 1- and 2-layer filaments (Section 2.2.4, p. 7).
- **Surface:** laser profilometer Keyence LJ-V7300; CON-Print3D software; Sa per DIN EN ISO 25178 over
  50 cm²; five 400 mm 2-layer specimens per mix (Section 2.3.1, p. 8).
- **Compression:** 40 mm cubes cut from 2-layer prints, directions D1, D2 (∥ print direction), D3; 1 mm/min (p. 8, Fig. 7).
- **Bending:** 3PB, 160 × 40 × 40 mm, span 120 mm, directions D1 and D3; 1 mm/min (p. 8).
- **Tension:** 600 × 40 × 20 mm prisms cut from 1-layer prints, set in a dumbbell formwork with
  fresh SHCC cast at both ends, polished; 1 mm/min; LVDT; GOM ARAMIS Adjustable 12M DIC (Section 2.3.3, p. 9).
  Gauge length not reported; 3 curves per mix shown in Fig. 17 (p. 15).
- **Curing & test age:** wrapped in film the day after printing, 20 °C and 65% RH; compression and
  bending at 2, 7 and 28 d (p. 8); tension age **not reported** (confirmed in PDF).

→ [[dogbone-uniaxial-tension]] · [[digital-image-correlation]] · [[fresh-properties]]

## Key results
| Mix ID | f'c (MPa) | First-crack stress (MPa) | Tensile strength (MPa) | Tensile strain capacity (%) | Crack width (µm) | Other |
|---|---|---|---|---|---|---|
| Ref | 83.2 / 73.0 / 82.2 (D1/D2/D3, 28 d) | ≈3 (read from Fig. 17; not stated) | 5.4 (mean, p. 14) | 2–3 (text, p. 14); ≈2.0–3.0 at onset of softening (read from Fig. 17) | not reported | f_flex 22.0 (D1) / 18.5 (D3) MPa, 28 d; Sa 772 µm |
| SE-CE | 80.9 / 80.1 / 79.5 | ≈3 (read from Fig. 17) | 4.1 (−24%) | 2–3 (text); ≈2.0–2.6 at onset of softening (Fig. 17) | not reported | f_flex 21.4 / 17.4 MPa; Sa 411 µm |

Compression of printed cubes (Table 2, p. 14), MPa (SD):

| Dir. | Ref 2 d | SE-CE 2 d | Ref 7 d | SE-CE 7 d | Ref 28 d | SE-CE 28 d |
|---|---|---|---|---|---|---|
| D1 | 66.5 (1.1) | 65.5 (3.2) | 82.1 (1.4) | 71.4 (2.7) | 83.2 (6.5) | 80.9 (2.4) |
| D2 (∥ print) | 60.2 (1.5) | 58.6 (1.9) | 63.8 (2.8) | 64.7 (8.3) | 73.0 (11.7) | 80.1 (4.7) |
| D3 | 68.4 (3.6) | 70.0 (4.4) | 79.1 (9.8) | 76.5 (5.0) | 82.2 (11.8) | 79.5 (9.3) |

Flexure 3PB (Table 3, p. 14), MPa (SD):

| Dir. | Ref 2 d | SE-CE 2 d | Ref 7 d | SE-CE 7 d | Ref 28 d | SE-CE 28 d |
|---|---|---|---|---|---|---|
| D1 | 18.0 (0.6) | 16.4 (1.5) | 21.9 (1.2) | 17.9 (1.6) | 22.0 (1.2) | 21.4 (1.0) |
| D3 | 16.4 (0.8) | 14.9 (2.0) | 17.1 (0.4) | 15.2 (0.5) | 18.5 (1.7) | 17.4 (1.0) |

Fresh-state values read from figures (all ≈):

| Quantity | Ref | SE | SE-CE | Location |
|---|---|---|---|---|
| Spread after strokes, ≈20 min → 180 min (cm) | ≈14.2 → ≈12.4 | ≈14.7 → ≈13.1 | ≈11.8 → ≈11.1 | Fig. 8, p. 9 |
| Spread before strokes (cm) | ≈10.3–11.1 | ≈10.4–10.8 | ≈10.0–10.3 | Fig. 8 |
| Demoulded cone, top / base (mm) | 90 / 104 | — | 70 / 100 | Fig. 9 (photo labels), p. 10 |
| Water retention at 5 → 20 min (%) | ≈98.9 → ≈98.3 | ≈99.2 → ≈98.4 | ≈99.2 → ≈98.6 | Fig. 10, p. 10 |
| Tack test force (N) | ≈3.0 | — | ≈3.4 | Fig. 11b, p. 11 |
| Cylinder pull test force (N) | ≈5.6 | — | ≈9.6 | Fig. 11b |
| Inclined table sliding angle (°) | ≈11 | — | ≈21 | Fig. 12b, p. 12 |

Main findings (with location):
- **Workability over time:** spread loss after 3 h: Ref 12.7%, SE 10.9%, SE-CE 5.5%; for Ref and SE the
  reduction was already noticeable after 2 h; SE-CE barely spread before strokes and kept its cone shape
  (shape stability) (Section 3.1.1, pp. 9–10, Figs. 8–9).
- **Water retention:** SE-CE highest throughout 20 min; SE fell to Ref level by 20 min → SE dropped from
  further testing (Section 3.1.2, pp. 10–11, Fig. 10). Note: all values lie within ≈98.3–99.2%.
- **Adhesiveness tests:** tack test forces 1–7 N with wide scatter (unreliable); CPT and ITT ranked SE-CE
  **more** adhesive than Ref, contrary to handling and flow-table observations; bleed water on Ref acts
  as lubricant (Section 3.1.3, pp. 11–12, Figs. 11–12).
- **Printing:** both Ref and SE-CE extruded without ruptures or noticeable layer deformation (p. 12, Fig. 13).
- **Surface roughness:** Sa 772 µm (Ref) vs 411 µm (SE-CE) (Section 3.2.1, p. 13, Fig. 15).
- **Anisotropy:** compression lowest in D2 (parallel to print direction, where fibres are predominantly
  oriented, ref. 27); flexure lower in D3 than D1, attributed to the weaker interlayer bond (Section 3.2.2, p. 14).
- **Tension:** both strain-hardened, ε about 2–3%; σ_tu 5.4 → 4.1 MPa; DIC showed evenly distributed
  cracks (Section 3.2.3, pp. 14–15, Figs. 17–18). Curves in Fig. 17 reach ≈5.3–5.5 MPa (Ref) and ≈4.3–4.6 MPa
  (SE-CE) peaks; one SE-CE curve has a long softening tail to 5% strain.

## Mechanisms / explanations offered by authors
- Poor surface of earlier printable SHCC: fibre clumping at high fibre content, and adhesiveness to tools
  from excess water in a very fine mix; lowering water + more SP would worsen shape stability and
  stickiness (Section 2.1, p. 4, ref. 29).
- Cellulose ether raises water retention and retards early hydration (Mueller et al., ref. 42) → longer
  open time; starch ether reduces adhesiveness in dry-mix mortars (ref. 35) (pp. 4, 9).
- Higher W/B needed because both ethers thicken → lower σ_tu (Section 3.2.3, p. 14; Conclusions, p. 16).
- D2 compression reduction linked to fibres aligned with print direction (refs. 26, 27) (p. 14).

## Limitations (stated + observed)
- Stated: adhesiveness tests inadequate; shrinkage effect of SE/CE not yet tested (Conclusions, p. 16).
- Observed: only two printed layers (buildability not tested); fibre diameter not given; tension age,
  gauge length, first-crack stress and crack widths not reported; strain capacity only as a 2–3% range
  in text; specimen counts for compression and bending not stated; SE-CE changes three variables at once
  (ethers, W/B, cement/FA ratio), so the effect of each is confounded.

## Relation to other work
- Agrees with: [[chavesfigueiredo2020-printed-shcc]] (ref. 26) — compressive strength anisotropy of printed SHCC is small; authors cite it for lower strength in the print direction (p. 14).
- Contradicts: ⚔️ ref. 27 (Li et al. 2020, as cited) — fibres "predominantly oriented" in the print direction —
  vs [[chavesfigueiredo2020-printed-shcc]] µCT showing mainly diagonal PVA orientation (different fibre and nozzle).
  ⚔️ Flexure lower across the interlayer (D3) here vs strong interface in [[chavesfigueiredo2020-printed-shcc]].
- Extends: Ogura et al. 2018 printable SHCC (as cited, not ingested); adds surface quality and open time as design targets.

## Pages updated from this source
- [[3d-printed-hdc]] · [[fresh-properties]] · [[fiber-dispersion]] · [[pe-fiber]] · [[silica-fume]] · [[fly-ash]]
- [[compressive-strength]] · [[flexural-strength]] · [[tensile-strain-capacity]] · [[water-binder-ratio]]
- [[dogbone-uniaxial-tension]] · [[digital-image-correlation]] · [[terminology-hdc-ecc-shcc]] · [[mix-designs]] · [[mechanical-results]]

## To verify
- [ ] PE fibre diameter (Dyneema SK60) — not given (confirmed absent in PDF).
- [ ] Age of tension tests and gauge length (600 mm prism; measuring length not stated; confirmed absent in PDF).
- [ ] W/B definition: computed check suggests it includes microsilica-suspension water (≈50% solids) and ≈70% of
  the SP mass as water; SP solids content not stated ⚠️ unverified.
- [ ] Whether "strain capacity 2–3%" is at peak stress or ultimate (text does not say; Fig. 17 suggests strain at
  the onset of softening).
- [ ] Specimen counts for compression and bending (not stated; tension: 3 curves per mix shown in Fig. 17).
