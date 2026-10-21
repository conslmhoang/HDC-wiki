---
type: source
slug: lee2021-hsdc-wall-emi-impact
title: "Shielding Effectiveness and Impact Resistance of Concrete Walls Strengthened by High-Strength High-Ductility Concrete"
authors: [Jae-Hoon Lee, Jin-Seok Choi, Tian-Feng Yuan, Young-Soo Yoon]
year: 2021            # Materials 14(24), article 7773; received 22 Oct 2021, accepted 13 Dec 2021, published 16 Dec 2021 (p. 1)
venue: "Materials (MDPI) 14(24): 7773"
doi: "10.3390/ma14247773"
raw_file: raw/papers/Lee2021_HSHDC-wall-impact.pdf
material_term: "HSDC (high-strength high-ductility concrete; also typo 'HDSC' in §3.1, p. 6). Same Korea University (Yoon) hybrid mix as the NSHSDC of [[yuan2020-nshsdc-beam-strengthening]]: 1.0 vol.% straight steel + 0.5 vol.% PE, W/B 0.172, f'c 122.3 MPa (28 d), cured 20 °C, 60% RH. The authors state PE gives 'strain hardening in the post-cracking zone' (§1, p. 2), but this paper shows no tensile stress–strain curve; ductility is not demonstrated here."
study_type: "experimental (EMI shielding effectiveness + low-velocity drop-weight impact on strengthened NC wall panels)"
tags: [hsdc, hshdc-korea, hybrid-fiber, steel-fiber, pe-fiber, emi-shielding, impact, drop-weight, strengthening, protective-structures]
ingested: 2026-10-20
updated: 2026-10-21
---

# EMI shielding and impact resistance of NC walls strengthened with HSDC (Lee et al., 2021)

> Re-checked against the publisher PDF (14 pp.) on 2026-10-21: page numbers added; Figs. 5–12 read
> (values marked ≈ are read from figures); several earlier readings corrected (see "To verify" →
> resolved).

## One-paragraph summary
The Korea University (Yoon) group (p. 1) strengthens 300 × 300 mm normal-concrete (NC, f'c 44.6 MPa) wall
panels, 100/200/300 mm thick, with **HSDC** layers of 5, 10 or 20 mm on one face (single layer) or both
faces (double layer). HSDC is the group's hybrid fiber mix (1.0 vol.% straight steel 19.5 mm × 0.2 mm +
0.5 vol.% PE 12 mm × 31 µm; f'c 122.3 MPa, direct tensile strength 9.7 MPa; Tables 1, 3, 4, p. 3). The twelve
specimens of Table 5 (p. 4) are **two full-depth HSDC panels (D1-HSDC 100 mm, D2-HSDC 200 mm) and ten
strengthened NC panels**; unstrengthened NC references (D1/D2/D3-NN, "T1-NN") appear only in the figures.
Panels are tested for electromagnetic interference (EMI) shielding effectiveness (SE, 400–1400 MHz,
near-field method), then under repeated low-velocity drop-weight impact (100 kg, 70 mm frustum head,
drop height 200 mm rising by 100 mm per blow to 1100 mm, then held; Fig. 9), then for SE again. SE rises with HSDC thickness and is
higher for double layers; a 5 mm single layer on a 100 mm panel shields more than a 200 mm plain panel
(§3.1, Fig. 6a, p. 8). An exponential model fits SE vs thickness (R² 0.989 single, 0.944 double; Eq. 1, p. 7;
a = 3.45, b = 0.08 single, a = 3.23, b = 0.13 double, Fig. 7b). Under
impact, double-layer panels outperform single-layer ones; the 20 mm double layer (H20D) survives 6 blows, absorbs
≈ 115 J (vs ≈ 87 J for H5D and 19 J for H5S; Fig. 11, p. 12) and gives the highest total reaction force (2.2× H5D, 1.6× H10D),
smallest deflection and best crack control among strengthened panels (Figs. 8–9, pp. 9–10). The full-depth 100 mm HSDC panel survives 16 blows (≈ 515 J).
After impact, SE fell by ≈ 7% (H20S) to ≈ 44% (H5S) (Fig. 12, p. 12). Steel fibers, not PE, give the conductivity.
→ [[impact-resistance]], [[extreme-loading-applications]]

## Objective / research question
- Evaluate HSDC strengthening as a combined method for EMI shielding and physical (impact) protection
  of existing concrete walls (§1, p. 2).
- Variables: NC thickness (100, 200, 300 mm), HSDC thickness (5, 10, 20 mm), layer type (single or double) (§1, p. 2; Table 5, p. 4).
- Evaluate SE of impact-damaged walls vs damage area ratio (§3.2.2, p. 12).

## Materials & mix design
Table 1 (by weight, ratio to cement, p. 3); fiber Table 3 (steel only; PE properties in text, §2.1, p. 3).

| Mix ID | Cement | Fly ash | Slag/other | Sand (type, max size) | W/B | SP | Fiber type | L (mm) | d (µm) | Vf (vol.%) |
|---|---|---|---|---|---|---|---|---|---|---|
| HSDC | 1.00 (Type I) | 0 | silica fume 0.25; silica filler 0.30 | silica sand 1.10, 0.08–0.30 mm | 0.172 (by mass; labelled "W/C" in Table 1, but 0.215/(1 + 0.25) = 0.172, so W/B) | 3.0% (polycarboxylate; basis not stated) | hybrid: straight high-strength steel + high-strength PE | steel 19.5; PE 12 | steel 200; PE 31 | steel 1.0 + PE 0.5 = 1.5 |
| NC (substrate) | 1.00 (Type I) | 0 | none | crushed fine agg. 2.15 + coarse agg. 2.42 (max 18 mm) | 0.43 (w/c) | 0.8% | none | n/a | n/a | 0 |

Units of binder quantities: mass ratio to cement (Table 1, p. 3).
- Steel fiber: 2650 MPa, 200 GPa, 7.8 g/cm³, L/d 97.5 (Table 3, p. 3). PE: 2900 MPa, 100 GPa (§2.1, p. 3).
- Silica fume 2.20 g/cm³, 200,000 cm²/g; silica filler "0.75 g/cm³ and 2.65 cm²/g" as printed (p. 3; values look swapped or mistyped ⚠️). Cement specific surface 3413 cm²/g in the text vs 3492 cm²/g in Table 2 (pp. 2–3).
- NC aggregates: fineness modulus 2.88 (fine) and 6.63 (coarse) in the text (p. 2–3), but Fig. 1 (p. 4) labels F.M. = 2.82 and 6.73.
- The authors limit steel fiber to 1.0 vol.% "to secure higher tensile strain capacity and toughness through PE"; UHPFRC typically uses > 1.5 vol.% steel (§1, p. 2).
- Matrix designed by dense packing at low W/B (§1, p. 2). Material properties are taken from previous work (refs 13–15) (§2.1, p. 3). Slant-shear bond HSDC/NC conforms to ACI 546 (14–21 MPa at 28 d) (§1, p. 2).

## Test methods
- Specimen geometry: 300 × 300 mm panels, total thickness 100/200/300 mm fixed regardless of HSDC; NC surfaces chiselled (high roughness) then HSDC cast on (§2.1, p. 3; Table 5 and Fig. 2, p. 4). Material tests: as in refs 13–15 (compression, flexure, direct tension on dog-bones; geometry not given).
- EMI SE: near-field method, 400–1400 MHz, wide-band log-spiral antennas 20 mm from the specimen, 5–6 repeats averaged; claimed equivalent to MIL-STD-285 far-field results (§2.2, pp. 4–5, Fig. 3).
- Impact: drop weight 100 kg, 70 mm cylinder-frustum head, first drop 200 mm, +100 mm each blow up to 1100 mm (step 10), then repeated at 1100 mm (Fig. 9 x-axis, p. 10); clear span 250 mm, all edges fixed; 2 load cells on supports; laser displacement sensor (KL4-120NV) at bottom centre; logger DEWE-43V at 200 kHz (§2.3, p. 5, Fig. 4, p. 6). → [[impact-test]]
- Crack counts and maximum crack widths (mm, per figure axes) per blow recorded (Figs. 8–9; method not stated).
- "Strengthening area ratio" (Fig. 7b) is not defined; its data points at 5/10/20/40% match total HSDC thickness ÷ panel thickness (inferred here) ⚠️.
- Curing & test age: 20 ± 1 °C, 60 ± 5% RH until test (p. 3); material properties at 28 d (Table 4); panel test age not stated ⚠️.

## Key results
| Mix ID | f'c (MPa) | First-crack stress (MPa) | Tensile strength (MPa) | Tensile strain capacity (%) | Crack width (µm) | Other |
|---|---|---|---|---|---|---|
| HSDC (28 d) | 122.3 (CV 0.1) | not reported | 9.7 direct tension (CV 1.6) | not reported | not reported (material) | flexural strength 22.9 MPa (CV 6.5), Table 4, p. 3 |
| NC (28 d) | 44.6 (CV 0.2) | n/a | 3.9 splitting | n/a | n/a | flexural strength 25.7 MPa (CV 0.4) ⚠️ implausible for NC |

**EMI SE (dB), 100 mm panels, read from Fig. 6a–b (p. 8), ≈ values:**

| Specimen | 400 MHz | 700 MHz | 1000 MHz | 1300 MHz | 1400 MHz |
|---|---|---|---|---|---|
| D1-NN (100 mm plain) | 1.3 | 1.3 | 3.8 | 5.0 | 4.6 |
| D2-NN (200 mm plain) | 4 | 6 | 7 | 8.5 | 10 |
| D3-NN (300 mm plain) | 7.5 | 9 | 13.5 | 15.5 | 16 |
| D1-H5S | 4 | 7 | 12.5 | 17 | 16 |
| D1-H10S | 9 | 9.5 | 13 | 20 | 24 |
| D1-H20S | 10.5 | 11 | 17 | 32 | 35 |
| D1-H5D | 4 | 14 | 20 | 40.5 (resonance peak) | 27 |
| D1-H10D | 21.5 | 16 | 24.5 | 36.5 | 36.5 |
| D1-H20D | 24 | 20 | 26.5 | 48.5 | 48.5 |

- Full-depth HSDC panels (Fig. 5, p. 7): D1-HSDC ≈ 16 dB at 400 MHz rising to ≈ 43 dB at 1300–1400 MHz (dip ≈ 35 dB at 1200 MHz);
  D2-HSDC ≈ 20 → ≈ 46 dB at 850–900 MHz and ≈ 49–51 dB above 1100 MHz (read from Fig. 5).
- Steel-fiber concrete from refs 5–6 (0.75 and 1.50 vol.% steel, l_f 35 mm): ≈ 40–43 dB (100 mm) and ≈ 48–57 dB (200 mm) above 600 MHz (Fig. 5).
- 200 and 300 mm panels with 20 mm HSDC: single ≈ 9–12 → ≈ 40 dB, double ≈ 12–24 → ≈ 47–48 dB at 1400 MHz (Fig. 6c–d).

**SE vs strengthening area ratio (Fig. 7b, p. 8; ≈ values, presumably averaged over frequency):** plain ≈ 3.8 dB;
single layer ≈ 12–13 (5%), ≈ 13.5–15 (10%), ≈ 16–17.5 dB (20%); double layer ≈ 20–21 (10%), ≈ 24–25 (20%), ≈ 26.5–27.5 dB (40%).
Fitted Eq. 1 coefficients printed on Fig. 7b: single a = 3.45, b = 0.08; double a = 3.23, b = 0.13.

**Impact (Figs. 8–9, pp. 9–10; Fig. 11, p. 12), ≈ values per blow (1, 2, 3, …):**

| Specimen | Max. reaction force (kN) | Max. deflection (mm) | Crack number | Max. crack width (mm) | Total imparted energy (J), blows (#) |
|---|---|---|---|---|---|
| T1-NN (plain 100 mm) | ≈ 15.5 (blow 1 only) | n.r. | n.r. | n.r. | n.r. |
| H5S | 16.2, 10.3 | 2.35, 4.8 | 5 | 6.0 | 19.0 (#1) |
| H10S | 14.4, 14.5, 14.4, 15.0, 13.6 | 2.0, 1.75, 2.85, 2.65, 3.1 | 5, 6, 8, 9 | 1.0, 2.3, 3.2, 4.5 | 68.3 (#4) |
| H20S | 11.9, 14.7, 16.2, 18.8, 18.9, 15.3 | 2.1, 1.85, 2.55, 2.3, 3.05, 4.2 | 5, 8, 9, 11, 12 | 0.8, 1.4, 2.15, 3.4, 4.7 | 96.8 (#5) |
| H5D | 19.7, 23, 24, 26, 18.5 | 1.05, 1.55, 2.2, 2.5, 4.6 | 4, 6, 9, 9 | 0.45, 1.1, 2.0, 5.0 | 86.7 (#4) |
| H10D | 22.5, 24.5, 24.5, 25.5, 28, 21.5 | 0.7, 1.05, 1.9, 1.65, 1.75, 3.7 | 5, 11, 14, 16, 26 | 0.2, 1.35, 2.0, 4.5, 5.5 | 90.2 (#5) |
| H20D | 23, 29, 32, 36.5, 38.5, 38.5, 31 | 0.5, 0.7, 1.0, 1.15, 1.5, 1.8, 3.05 | 5, 8, 13, 21, 29, 29 | 0.05, 0.2, 0.4, 0.7, 1.1, 2.0 | **114.9 (#6)** |
| HSDC (D1-HSDC, full 100 mm; "HD100") | rises to ≈ 57 at blow 10, ≈ 53–55 to blow 17 | ≈ 0.5 → ≈ 1.5 (blows 1–16), 2.0 at 17 | 5 → 28 | ≈ 0.05 → 2.0 | ≈ 515 (#16) |

Energies are the printed bar labels (Fig. 11; HSDC bar read off); other values read from Figs. 8–9.

**Post-impact SE (Fig. 12, p. 12), SE decrease ratio / damage area ratio (%), ≈:** H5S 44.2 / 18.3; H10S 16.1 / 9.3;
H20S 7.2 / 9.3; H5D 28.1 / 10.4; H10D 25.7 / 9.0; H20D 24.7 / 8.0; HSDC 7.9 / 6.3.

Main findings (with Table/Fig. location):
- **SE vs thickness:** SE rises with HSDC thickness; gains of 2.4–35.3, 7.0–31.9 and 6.9–43.8 dB over unstrengthened panels (Conclusion 1, p. 13). The abstract instead says SE "increased by approximately 35.6–46.2%" (p. 1) ⚠️.
  > Interpreted: Fig. 6a–b read-offs reproduce these three ranges as the 5, 10 and 20 mm HSDC panels (single and
  > double together) relative to D1-NN (e.g. H5D − D1-NN ≈ 35.5 dB and H20D − D1-NN ≈ 43.5 dB at 1300 MHz).
- A single 5 mm HSDC layer on a 100 mm panel gives higher SE than a 200 mm plain NC panel, similar to 300 mm (§3.1, p. 7; Fig. 6a).
- Double layer of the same total thickness: +1.5–9.1 dB over single layer at 600–1400 MHz (§3.1, p. 7; Fig. 7a); +35.4–65.7% by the fitted model (§3.1, pp. 7–8).
- Resonance peaks appear in double-layer panels and shift to lower frequency with thicker HSDC, attributed to quarter-wavelength reflection cancellation (§3.1, p. 7). Example: D1-H5D ≈ 40.5 dB at 1300 MHz but ≈ 27 dB at 1400 MHz (Fig. 6b).
- SE > 20 dB needs strengthening area ratio > 40% (single) and ≥ 10% (double) per the abstract (p. 1); Fig. 7b supports this (double ≈ 20 dB at 10%; single fit reaches 20 dB only near 40%). Conclusion 1 (p. 13) says "> 40%" for both.
- Steel-fiber concrete (0.75 and 1.50 vol.% steel fibers, l_f 35 mm, Yuan et al. 2021, as cited) shields better (40–50 dB at 500–1400 MHz) than HSDC, attributed to longer fibers (35 vs 19.5 mm) (§3.1, p. 6; Fig. 5, p. 7).
- **Impact, single layer:** text says H5S failed at blow 2 and H10S and H20S at blows 4 and 5; the unstrengthened bottom face scabbed (§3.2.1, p. 9; Fig. 8). Figure blow counts differ: Fig. 8 plots H10S to blow 5 and H20S to blow 6; Fig. 11 labels #1/#4/#5; Fig. 12 labels #1/#5/#6 ⚠️.
- **Impact, double layer:** total reaction force of H20D = 2.2× H5D and 1.6× H10D (p. 10; summing Fig. 9a read-offs gives ≈ 2.1× and ≈ 1.6×); H20D tracks the full HSDC panel up to the fourth blow (p. 10, Fig. 9a); deflection falls with thickness (§3.2.1, Fig. 9b).
- Crack widths after the first blow: text says "0.05 to 0.15 m" (p. 10). The Fig. 9d axis is in **mm**, and H5D reads ≈ 0.45 mm at blow 1, so the range is not exact. 5.00 mm and 5.50 mm in H5D and H10D at blows 4–5; H20D bottom face ≈ 0.05 mm after blow 1, 0.70 and 1.10 mm after blows 4 and 5 (p. 10–11; Fig. 9d confirms).
- Total imparted energy to failure rises with thickness: H20D 114.9 J vs H5S 19.0 J (6.0×, "more than five times") and H5D 86.7 J (+32.5%; the text's "3.5% larger" is evidently a typo) (§3.2.1, p. 11; Fig. 11, p. 12).
- **Post-impact SE decrease:** the "7.1%" and "24.7%" in the text (p. 12) and Conclusion 3 (p. 13) correspond in Fig. 12 to **H20S (≈ 7.2%) and H20D (24.7%)**, the two 20 mm specimens, not to the 5–10 mm panels. Thinner panels lost more: H5S ≈ 44%, H5D ≈ 28%, H10D ≈ 26%; H10S ≈ 16%. At similar damage area, single-layer panels lost less SE than double-layer ones (§3.2.2, p. 12).

## Mechanisms / explanations offered by authors
- Randomly dispersed steel fibers form a continuous conductive network above the percolation threshold, which absorbs/reflects EM waves (§3.1, p. 6).
- Fiber length and aspect ratio govern SE; shorter HSDC steel fibers give lower SE than 35 mm fibers (§3.1, p. 6, ref 17).
- Steel fibers reduce maximum and residual displacement and raise energy dissipation under impact (§3.2.1, p. 10).
- SE after impact is governed by loss of effective thickness (cracking, scabbing, spalling) (§3.2.2, p. 12).

## Limitations (stated + observed)
- One panel per configuration; small panels (300 mm, 250 mm span) (observed).
- No tensile stress–strain or strain capacity data for HSDC; strain hardening is asserted from earlier papers only (observed).
- Almost all quantitative SE and impact results are given only as curves or bars (Figs. 5–12). The values above are ≈ read-offs, except the printed energy labels in Fig. 11 (observed).
- Inconsistencies (observed):
  - between abstract and conclusions (SE gain in % vs dB; area-ratio thresholds);
  - blow counts differ across Figs. 8, 11 and 12, and from the text;
  - wording of the 7.1% / 24.7% statement;
  - aggregate fineness modulus differs between text and Fig. 1;
  - typos ("HDSC", "HD100", crack widths in "m", "3.5%").
- Plain NC reference panels (D1/D2/D3-NN, T1-NN) are not listed in Table 5 (observed).
- "Total imparted energy" is not defined. H5S's 19 J is far below the ≈ 196 J potential energy of the first 200 mm drop (computed here), so it is not the drop energy (observed).
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
- [ ] Abstract "35.6–46.2%" SE increase: not reproducible from the figures.
- [ ] Definition of "strengthening area ratio" (inferred = HSDC thickness / panel thickness) and of the frequency averaging in Fig. 7b.
- [ ] Blow counts to failure: text vs Figs. 8, 11, 12.
- [ ] Definition of "total imparted energy" (Fig. 11).
- [ ] NC flexural strength 25.7 MPa (Table 4, p. 3) — confirmed as printed; implausible.
- [ ] Silica filler density/specific surface (0.75 g/cm³, 2.65 cm²/g, p. 3) — likely mistyped.
- [ ] Panel test age (not stated in the PDF).

Resolved on 2026-10-21 (PDF check):
- [x] Which groups the 2.4–35.3 / 7.0–31.9 / 6.9–43.8 dB ranges belong to — matches 5 / 10 / 20 mm HSDC on 100 mm panels vs D1-NN (Fig. 6a–b read-off; interpretation, the authors do not say).
- [x] Area-ratio thresholds — Fig. 7b supports the abstract (single ≈ 40%, double ≈ 10%).
- [x] Crack-width units — mm (Fig. 8d, 9d axes); "m" is a typo.
- [x] "More than five times and 3.5% larger" — Fig. 11 labels give 114.9/19.0 = 6.0× and 114.9/86.7 = +32.5%; "3.5%" is a typo.
- [x] Post-impact SE decrease 7.1% vs 24.7% — these are H20S and H20D (Fig. 12); the earlier wiki reading ("24.7% for 5–10 mm") was wrong.
- [x] Composition of the 12 specimens — Table 5 includes two full-depth HSDC panels; plain NC references are extra (figures only).
