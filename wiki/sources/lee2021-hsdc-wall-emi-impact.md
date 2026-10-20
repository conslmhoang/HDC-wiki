---
type: source
slug: lee2021-hsdc-wall-emi-impact
title: "Shielding Effectiveness and Impact Resistance of Concrete Walls Strengthened by High-Strength High-Ductility Concrete"
authors: [Jae-Hoon Lee, Jin-Seok Choi, Tian-Feng Yuan, Young-Soo Yoon]
year: 2021            # Materials 14(24), article 7773; received 22 Oct 2021, accepted 13 Dec 2021, published 16 Dec 2021
venue: "Materials (MDPI) 14(24): 7773"
doi: "10.3390/ma14247773"
raw_file: raw/papers/Lee2021_HSHDC-wall-impact.xml
material_term: "HSDC (high-strength high-ductility concrete; also typo 'HDSC' in §3.1). Same Korea University (Yoon) hybrid mix as the NSHSDC of [[yuan2020-nshsdc-beam-strengthening]]: 1.0 vol.% straight steel + 0.5 vol.% PE, W/B 0.172, f'c 122.3 MPa (28 d), room-cured (20 °C, 60% RH). The authors state PE gives 'strain hardening in the post-cracking zone' (§1), but this paper shows no tensile stress–strain curve; ductility is not demonstrated here."
study_type: "experimental (EMI shielding effectiveness + low-velocity drop-weight impact on strengthened NC wall panels)"
tags: [hsdc, hshdc-korea, hybrid-fiber, steel-fiber, pe-fiber, emi-shielding, impact, drop-weight, strengthening, protective-structures]
ingested: 2026-10-20
updated: 2026-10-20
---

# EMI shielding and impact resistance of NC walls strengthened with HSDC (Lee et al., 2021)

## One-paragraph summary
The Korea University (Yoon) group strengthens 300 × 300 mm normal-concrete (NC, f'c 44.6 MPa) wall
panels, 100/200/300 mm thick, with **HSDC** layers of 5, 10 or 20 mm on one face (single layer) or both
faces (double layer). HSDC is the group's hybrid fiber mix (1.0 vol.% straight steel 19.5 mm × 0.2 mm +
0.5 vol.% PE 12 mm × 31 µm; f'c 122.3 MPa, direct tensile strength 9.7 MPa; Tables 1, 3, 4). Twelve
panels are tested for electromagnetic interference (EMI) shielding effectiveness (SE, 400–1400 MHz,
near-field method), then under repeated low-velocity drop-weight impact (100 kg, 70 mm frustum head,
drop height 200 mm rising by 100 mm per blow), then for SE again. SE rises with HSDC thickness and is
higher for double layers; a 5 mm single layer on a 100 mm panel shields more than a 200 mm plain panel
(§3.1, Fig. 6). An exponential model fits SE vs thickness (R² 0.989 single, 0.944 double; Eq. 1). Under
impact, double-layer panels outperform single-layer ones; the 20 mm double layer (H20D) gives the
highest reaction force (2.2× H5D, 1.6× H10D), smallest deflection and best crack control, and the
lowest post-impact SE loss (Figs. 8–12). Steel fibers, not PE, give the conductivity. Most numbers are
read only from figures, which are not available in the raw XML. → [[impact-resistance]], [[extreme-loading-applications]]

## Objective / research question
- Evaluate HSDC strengthening as a combined method for EMI shielding and physical (impact) protection
  of existing concrete walls (§1).
- Variables: NC thickness (100, 200, 300 mm), HSDC thickness (5, 10, 20 mm), layer type (single or double) (§1, Table 5).
- Evaluate SE of impact-damaged walls vs damage area ratio (§3.2.2).

## Materials & mix design
Table 1 (by weight, ratio to cement); fiber Table 3 (steel only; PE properties in text, §2.1).

| Mix ID | Cement | Fly ash | Slag/other | Sand (type, max size) | W/B | SP | Fiber type | L (mm) | d (µm) | Vf (vol.%) |
|---|---|---|---|---|---|---|---|---|---|---|
| HSDC | 1.00 (Type I) | 0 | silica fume 0.25; silica filler 0.30 | silica sand 1.10, 0.08–0.30 mm | 0.172 (by mass; labelled "W/C" in Table 1, but 0.215/(1 + 0.25) = 0.172, so W/B) | 3.0% (polycarboxylate; basis not stated) | hybrid: straight high-strength steel + high-strength PE | steel 19.5; PE 12 | steel 200; PE 31 | steel 1.0 + PE 0.5 = 1.5 |
| NC (substrate) | 1.00 (Type I) | 0 | none | crushed fine agg. 2.15 + coarse agg. 2.42 (max 18 mm) | 0.43 (w/c) | 0.8% | none | n/a | n/a | 0 |

Units of binder quantities: mass ratio to cement (Table 1).
- Steel fiber: 2650 MPa, 200 GPa, 7.8 g/cm³, L/d 97.5 (Table 3). PE: 2900 MPa, 100 GPa (§2.1).
- The authors limit steel fiber to 1.0 vol.% "to secure higher tensile strain capacity and toughness through PE"; UHPFRC typically uses > 1.5 vol.% steel (§1).
- Matrix designed by dense packing at low W/B (§1). Material properties are taken from previous work (refs 13–15) (§2.1).

## Test methods
- Specimen geometry: 300 × 300 mm panels, total thickness 100/200/300 mm fixed regardless of HSDC; NC surfaces chiselled (high roughness) then HSDC cast on (Table 5, Fig. 2). Material tests: as in refs 13–15 (compression, flexure, direct tension on dog-bones; geometry not given).
- EMI SE: near-field method, 400–1400 MHz, log-spiral antennas 20 mm from the specimen, 5–6 repeats averaged; claimed equivalent to MIL-STD far-field results (§2.2, Fig. 3).
- Impact: drop weight 100 kg, 70 mm cylinder-frustum head, first drop 200 mm, +100 mm each blow until failure; clear span 250 mm, all edges fixed; 2 load cells on supports; laser displacement sensor at bottom centre; logger 200 kHz (§2.3, Fig. 4). → [[impact-test]]
- Crack counts and maximum crack widths per blow recorded (Figs. 8–9; method not stated).
- Curing & test age: 20 ± 1 °C, 60 ± 5% RH until test; material properties at 28 d (Table 4); panel test age not stated ⚠️.

## Key results
| Mix ID | f'c (MPa) | First-crack stress (MPa) | Tensile strength (MPa) | Tensile strain capacity (%) | Crack width (µm) | Other |
|---|---|---|---|---|---|---|
| HSDC (28 d) | 122.3 (CV 0.1) | not reported | 9.7 direct tension (CV 1.6) | not reported | not reported (material) | flexural strength 22.9 MPa (CV 6.5), Table 4 |
| NC (28 d) | 44.6 (CV 0.2) | n/a | 3.9 splitting | n/a | n/a | flexural strength 25.7 MPa (CV 0.4) ⚠️ implausible for NC |

Main findings (with Table/Fig. location):
- **SE vs thickness:** SE rises with HSDC thickness; gains of 2.4–35.3, 7.0–31.9 and 6.9–43.8 dB over unstrengthened panels (Conclusion 1; which three groups these ranges belong to is not stated ⚠️). The abstract instead says SE "increased by approximately 35.6–46.2%" ⚠️.
- A single 5 mm HSDC layer on a 100 mm panel gives higher SE than a 200 mm plain NC panel, similar to 300 mm (§3.1, Fig. 6a).
- Double layer of the same total thickness: +1.5–9.1 dB over single layer at 600–1400 MHz (§3.1, Fig. 7a); +35.4–65.7% by the fitted model (§3.1).
- Resonance peaks appear in double-layer panels and shift to lower frequency with thicker HSDC, attributed to quarter-wavelength reflection cancellation (§3.1).
- SE > 20 dB needs strengthening area ratio > 40% (single) and > 10% (double) per the abstract; > 40% for both per Conclusion 1 ⚠️.
- Steel-fiber concrete (0.75 and 1.50 vol.% steel fibers, l_f 35 mm, Yuan et al. 2021, as cited) shields better (40–50 dB at 500–1400 MHz) than HSDC, attributed to longer fibers (35 vs 19.5 mm) (§3.1, Fig. 5).
- **Impact, single layer:** H5S failed at blow 2; H10S and H20S at blows 4 and 5; the unstrengthened bottom face scabbed (§3.2.1, Fig. 8).
- **Impact, double layer:** total reaction force of H20D = 2.2× H5D and 1.6× H10D; deflection falls with thickness (§3.2.1, Fig. 9).
- Crack widths after the first blow 0.05–0.15 (unit printed as "m"; mm intended ⚠️); 5.00 mm and 5.50 mm in H5D and H10D at blows 4–5; H20D bottom face about 0.05 mm after blow 1, 0.70 and 1.10 mm after blows 4 and 5 (§3.2.1).
- Total imparted energy to failure rises with thickness; H20D > 5× H5S (and "3.5% larger" than H5D, likely garbled ⚠️) (§3.2.1, Fig. 11).
- Post-impact SE decrease: about 7.1% for 20 mm HSDC vs 24.7% for 5–10 mm (wording ambiguous ⚠️) due to spalling of the thin layers (§3.2.2, Fig. 12, Conclusion 3).

## Mechanisms / explanations offered by authors
- Randomly dispersed steel fibers form a continuous conductive network above the percolation threshold, which absorbs/reflects EM waves (§3.1).
- Fiber length and aspect ratio govern SE; shorter HSDC steel fibers give lower SE than 35 mm fibers (§3.1, ref 17).
- Steel fibers reduce maximum and residual displacement and raise energy dissipation under impact (§3.2.1).
- SE after impact is governed by loss of effective thickness (cracking, scabbing, spalling) (§3.2.2).

## Limitations (stated + observed)
- One panel per configuration; small panels (300 mm, 250 mm span) (observed).
- No tensile stress–strain or strain capacity data for HSDC; strain hardening is asserted from earlier papers only (observed).
- Almost all quantitative impact and SE results are only in figures, unavailable in the XML text (observed).
- Inconsistencies between abstract and conclusions (SE gain in % vs dB; area-ratio thresholds) and typos ("HDSC", "HD100", crack widths in "m") (observed).
- Low-velocity impact only; no strain rate reported (observed).

## Relation to other work
- Agrees with: [[ranade2017-hshdc-impact-resistance]] — high-strength ductile layers improve multi-blow impact damage tolerance (different material: Michigan PE-only HSHDC, unreinforced slabs).
- Contradicts: ⚔️ none directly. Note: Korean "HSDC/NSHSDC" is a fourth "HSHDC"-type lineage, hybrid steel + PE (0.5% PE only); see [[hshdc]], [[terminology-hdc-ecc-shcc]].
- Extends: first wiki source on EMI shielding of HDC-type materials and on HDC-strengthened walls under impact; uses the bond method from [[yuan2020-nshsdc-beam-strengthening]].

## Pages updated from this source
- [[impact-resistance]]
- [[impact-test]]
- [[extreme-loading-applications]]
- [[rc-member-strengthening]]
- [[hshdc]]
- [[terminology-hdc-ecc-shcc]]
- [[crack-width]]

## To verify
- [ ] Whether HSDC shows tensile strain hardening and its ε_tu (refs 13–14: Yuan et al. 2019 Int J Polym Sci; Yuan, Lee & Yoon 2020 CCC 106:103458).
- [ ] Abstract "35.6–46.2%" vs conclusion dB ranges; to which groups 2.4–35.3 / 7.0–31.9 / 6.9–43.8 dB belong.
- [ ] Area-ratio thresholds for SE > 20 dB (abstract 40%/10% vs conclusion 40%).
- [ ] Crack-width units in §3.2.1 ("0.05 to 0.15 m").
- [ ] "More than five times and 3.5% larger" (Fig. 11) — read from the figure.
- [ ] Post-impact SE decrease 7.1% vs 24.7%: which specimens.
- [ ] NC flexural strength 25.7 MPa (Table 4).
- [ ] Panel test age.
