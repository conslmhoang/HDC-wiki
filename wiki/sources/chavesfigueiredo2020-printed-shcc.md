---
type: source
slug: chavesfigueiredo2020-printed-shcc
title: "Mechanical Behavior of Printed Strain Hardening Cementitious Composites"
authors: [Stefan Chaves Figueiredo, Claudia Romero Rodríguez, Zeeshan Y. Ahmed, Derk H. Bos, Yading Xu, Theo M. Salet, Oğuzhan Çopuroğlu, Erik Schlangen, Freek P. Bos]
year: 2020            # Materials 13(10), 2253; received 3 Apr, accepted 8 May, published 14 May 2020 (p. 1)
venue: "Materials (MDPI) 13(10) (2020) 2253"
doi: "10.3390/ma13102253"
raw_file: raw/papers/ChavesFigueiredo2020_printed-SHCC.pdf
material_term: "SHCC (strain hardening cementitious composites), 'in literature also referred to as ECC' (Section 1, p. 2). Printable PVA-SHCC (Kuraray PVA, 2 vol.%), normal/low-strength matrix (f'c 15–44 MPa printed cubes, 28 d), standard water curing (20 °C, 98% RH). Not called HDC."
study_type: experimental
tags: [shcc, ecc, 3d-printing, extrusion, pva-fiber, hpmc, ggbfs, fly-ash, limestone-powder, anisotropy, fiber-orientation, interlayer-bond, x-ray-ct, dic, uniaxial-tension, four-point-bending, notched-beam, tu-delft, tu-eindhoven]
ingested: 2026-10-20
updated: 2026-10-21
---

# Mechanical behaviour of printed SHCC (Chaves Figueiredo et al., 2020)

> Re-checked against the publisher PDF (23 pp.) on 2026-10-21: page numbers added, figure values read off
> (marked ≈), all table values confirmed.

## One-paragraph summary
TU Delft (Microlab) and TU Eindhoven printed two previously developed PVA-SHCC mixes
(XVA3PVA20: slag + limestone powder, no sand; YVA4PVA20-S05: fly ash + sand ≤ 0.5 mm) on the
TU/e gantry printer (10 × 50 mm layers, 100 mm/s) and characterised them in several directions
relative to the print path (Sections 2.1–2.2, pp. 3–7). Compressive strength was nearly isotropic (5–15%
difference, Table 2, p. 8). In direct tension both mixes cracked multiply **parallel** to the print direction
(LPA); X also strain-hardened **perpendicular** in-plane (LPE), but tensile strain at peak stress
was low (0.15–0.31%, Table 5, p. 12), below the cast-SHCC values of the original mixes (Section 3.4.1, p. 14).
Pulling two layers apart gave brittle failure, yet interface strength (≈1.2–2.4 MPa, read from Fig. 14, p. 16)
was comparable to or above the bulk first-crack strength, so the interlayer was **not** the weak zone (Section 3.5).
X-ray CT showed the interface had the **lowest** air-void content, and fibres were oriented mainly
**diagonally** (peaks ≈40° and ≈170° to the print path) rather than parallel (Figs. 15–17, pp. 17–19).
Four-point bending ductility (deflection at peak) fell as the number of layers (thickness) rose (Fig. 6, p. 11).

> Synthesis: the printed material is a genuine SHCC (multiple cracking, strain hardening in LPA),
> but its strain capacity (≤ 0.3% at peak stress) is an order of magnitude below the ECC convention
> (> 3%) and below the Chinese HDC bar (≥ 0.5%, see [[terminology-hdc-ecc-shcc]]).

## Objective / research question
- Evaluate physical and mechanical properties of SHCC tailored for 3D printing at a larger scale
  than earlier work (Section 1, p. 3).
- Quantify anisotropy: loading direction vs print path, layer interval time (3 vs 36 min), and number of
  layers (1–4) in flexure (Section 1, p. 3).
- Relate mechanics to air voids and fibre orientation by X-ray µCT (Section 2.3, p. 7).

## Materials & mix design
Constituents (Table 1, p. 4; physical data in ref. 41, not in this paper): CEM I 42.5, blast furnace slag,
fly ash, limestone powder, quartz sand, PVA fibre (Kuraray, Acknowledgments p. 20), HPMC viscosity modifier,
superplasticizer. Fibre length, diameter and strength are **not reported** for this study's mixes. (The
Introduction, p. 2, says the printable SHCC of the cited ref. 7 used PVA 12 mm × 40 µm at 2 vol.%; this is
not stated for the present mixes.)

| Mix ID | Cement | Fly ash | Slag/other | Sand (type, max size) | W/B | SP | Fiber type | L (mm) | d (µm) | Vf (vol.%) |
|---|---|---|---|---|---|---|---|---|---|---|
| XVA3PVA20 | 259.2 | 0 | slag 604.9; limestone powder 864.1; HPMC 5.1 | none (limestone powder only) | 0.40 (authors, Section 3.2, p. 8; 345.6/864.1 computed = 0.40) | 17.3 | PVA (Kuraray) | not reported | not reported | 2 (26 kg/m³; "2 vol.%" stated in Conclusions, p. 19) |
| YVA4PVA20-S05 | 480.2 | 567.6 | limestone powder 109.1; HPMC 6.5 | quartz sand 125–250 µm 186.3 + 250–500 µm 294; max 0.5 mm | 0.50 counting only 30% of FA as binder (authors, Section 3.2, p. 8); 0.31 with all FA (computed) | 13.0 | PVA (Kuraray) | not reported | not reported | 2 (26 kg/m³; mix name "PVA20") |

Units of binder quantities: kg/m³ (Table 1, p. 4). Water: X 345.6, Y 327.4 kg/m³.
- Computed here (by mass): Y FA/C = 1.18; X slag/C = 2.33.
- HPMC: Conclusions (p. 19) state 0.3 wt.% for X (name "XVA3"). Basis not stated by the authors. Computed
  here: HPMC / all dry solids (binder + limestone powder + sand, excl. fibres) = 5.1/1728.2 = 0.30% (X) and
  6.5/1637.2 = 0.40% (Y), which matches "VA3"/"VA4"; so the basis is probably total dry solids (interpretation).
- Fresh state (Section 2.1, pp. 3–4): initial bulk / shear yield stress X 34.74 ± 5.20 / 4.41 ± 0.18 kPa;
  Y 34.26 ± 1.98 / 2.49 ± 0.08 kPa (from ram-extruder + Benbow–Bridgwater, ref. 41).

Production (p. 4): 50 L as 2 × 25 L batches in a 75 L planetary pan mixer (TMV 75, 2.2 kW; dry 2 min, then
water + SP within 1 min, then mixing to homogeneity). Printed at TU/e; layer 10 mm thick × 50 mm wide; nozzle
speed 100 mm/s; layer intervals 3 min (2 L), 2 min (3 L), 4.5 min (4 L), plus one 2-layer element at 36 min.
Curing (p. 5): under plastic foil with wet fabric for 24 h, sawn, then 27 d at 20 ± 2 °C and 98 ± 2% RH.

## Test methods
- **Specimen geometry:**
  - compression: 35 mm cubes sawn (after 7 d) from the centre of 4-layer beams, loaded perpendicular (dir. I) and parallel (dir. II) to the print plane (Section 2.2.1, p. 5);
  - notched 3PB "fracture toughness": 30 × 40 × 160 mm, notch 4.5 mm wide, 7 mm (X) / 10 mm (Y) deep; 2 LVDTs at mid-span (Section 2.2.2, p. 5); n = 3 per mix (Fig. 3, p. 9);
  - 4PB: about 40 mm wide × 150 mm long, 1–4 layers (10–40 mm deep), span 120 mm, load points 40 mm apart, loaded perpendicular to the print plane; Instron 8872 (Section 2.2.3, p. 6); n = 5–6 per series (Figs. 4–5, p. 10);
  - direct tension: 1-layer sawn plates, LPA 40 mm wide × 150 mm long, LPE 35 mm wide × 30 mm long, glued ends (Section 2.2.4, p. 6); n = 5 per series (Figs. 7, 12);
  - interlayer tension: 10 × 10 × 20 mm prisms across the interface of 2-layer elements (2T = 3 min, 2TT = 36 min) (Section 2.2.5, p. 7); n = 6 / 4 / 5 / 5 for X2T / X2TT / Y2T / Y2TT (Fig. 13, p. 15).
- **Loading / rate:**
  - compression 2 kN/s (p. 5);
  - 3PB CMOD control 0.8 µm/s to first crack, then 3.3 µm/s (p. 5);
  - 4PB 1 mm/s deflection (as printed, p. 6; unusually fast, but confirmed in PDF);
  - tension: 1 µm/s (LPA) and 0.2 µm/s (LPE), both 6.67 µstrain/s (p. 6); interlayer 0.1 µm/s (5 µstrain/s) (p. 7).
- **Measurement:** LVDTs; DIC (Ncorr2, subset radius 57, about 48 µm/pixel, Canon EOS 6D, frame every 2 s; p. 6) for crack patterns;
  X-ray µCT (Phoenix Nanotom, 7.5 µm/pixel, VG Studio 3.3) + Trainable Weka Segmentation in FIJI for voids and fibre
  imprints (Feret angle, 0/180° = print direction; fibre imprints ≥ 10 px², circularity 0–0.3) (Section 2.3, pp. 7–8).
- **Curing & test age:** compression 14 and 28 d; 3PB 28 d; 4PB 14 and 28 d; tension 35 d; interlayer 28 d.

→ [[dogbone-uniaxial-tension]] · [[notched-beam-three-point-bending]] · [[digital-image-correlation]]

## Key results
Compression of printed cubes (Table 2, p. 8), MPa:

| Mix | 14 d, layers ⟂ load | 28 d, layers ⟂ load | 14 d, layers ∥ load | 28 d, layers ∥ load |
|---|---|---|---|---|
| XVA3PVA20 | 37.63 ± 3.8 | 44.09 ± 4.33 | 34.98 ± 1 | 41.93 ± 1.88 |
| YVA4PVA20-S05 | 14.57 ± 0.39 | 17.66 ± 0.24 | 12.03 ± 1.04 | 15.02 ± 0.52 |

Direct tension at 35 d (Tables 4–5, p. 12); strain at peak stress = "deformation at maximum tensile strength".

| Mix ID | f'c (MPa) | First-crack stress (MPa) | Tensile strength (MPa) | Tensile strain capacity (%) | Crack width (µm) | Other |
|---|---|---|---|---|---|---|
| X-LPA | 44.09 (28 d, ⟂) | 1.53 ± 0.23 | 2.4 ± 0.26 | 0.26 ± 0.08 (at peak) | not reported | ε at first crack 0.023 ± 0.006%; strain hardening |
| X-LPE | same | 1.84 ± 0.47 | 2.41 ± 0.36 | 0.31 ± 0.26 (at peak) | not reported | 0.017 ± 0.003%; strain hardening retained |
| Y-LPA | 17.66 (28 d, ⟂) | 1.28 ± 0.33 | 1.64 ± 0.23 | 0.15 ± 0.12 (at peak) | not reported | 0.022 ± 0.017%; only a few specimens strain-hardened |
| Y-LPE | same | 1.15 ± 0.2 | 1.65 ± 0.27 | 0.29 ± 0.26 (at peak) | not reported | 0.012 ± 0.003%; "high ductility" but large scatter |

Notched 3PB (Table 3, p. 9), 28 d, flexural stress vs CMOD:

| Mix | LOP (MPa) | CMOD at LOP (µm) | MOR (MPa) | CMOD at MOR (µm) | J_tip (kJ/m² as printed ⚠️) | J_b (kJ/m² as printed ⚠️) |
|---|---|---|---|---|---|---|
| XVA3PVA20 | 1.10 ± 0.17 | 10.60 ± 1.29 | 1.84 ± 0.09 | 341.99 ± 4.00 | 16.37 ± 4.51 | 430.74 ± 14.62 |
| YVA4PVA20-S05 | 0.56 ± 0.04 | 9.49 ± 0.93 | 0.97 ± 0.10 | 545.06 ± 112.15 | 7.11 ± 1.51 | 260.94 ± 67.97 |

Four-point bending summary (all values ≈, read from Fig. 6, p. 11; 28 d, 14 d in brackets):

| Series | First-crack flexural stress (MPa) | Deflection at first crack (mm) | MOR (MPa) | Deflection at MOR (mm) |
|---|---|---|---|---|
| X 1L | ≈3.5 (≈4.0) | ≈0.25 (≈0.33) | ≈7.2 (≈6.9) | ≈2.75 (≈2.1) |
| X 2L | ≈4.2 (≈3.1) | ≈0.41 (≈0.37) | ≈7.4 (≈6.5) | ≈1.8 (≈1.6) |
| X 3L | ≈5.6 (≈2.8) | ≈0.60 (≈0.52) | ≈7.0 (≈6.6) | ≈0.97 (≈1.3) |
| X 4L | ≈6.1 (≈4.1) | ≈0.75 (≈0.76) | ≈7.5 (≈7.6) | ≈1.0 (≈1.4) |
| Y 1L | ≈2.3 (≈2.4) | ≈0.27 (≈0.32) | ≈3.5 (≈3.3) | ≈1.6 (≈1.6) |
| Y 2L | ≈2.4 (≈2.0) | ≈0.38 (≈0.31) | ≈3.3 (≈3.2) | ≈1.3 (≈1.1) |
| Y 3L | ≈2.3 (≈2.4) | ≈0.48 (≈0.59) | ≈3.6 (≈3.3) | ≈0.98 (≈1.05) |
| Y 4L | ≈2.6 (≈2.2) | ≈0.72 (≈0.71) | ≈3.9 (≈3.7) | ≈1.25 (≈1.3) |

Interlayer tensile bond strength, 28 d (≈, read from Fig. 14, p. 16): X2T ≈2.4, X2TT ≈1.9, Y2T ≈1.4,
Y2TT ≈1.2 MPa; strain at failure mostly < 0.1% (Fig. 13, p. 15).

Main findings (with location):
- **Compression nearly isotropic:** 5–15% difference between directions; for X within one SD.
  Printed f'c close to cast f'c of the same mixes (ref. 41) (Section 3.1, p. 8, Table 2).
- **J_b > J_tip** for both mixes, satisfying the authors' PSH condition (Section 3.2, p. 8, Table 3).
  X has a stiffer post-crack response (stronger bond inferred). ⚠️ These "J" values come from flexural
  stress–CMOD integrals (Eqs. 1–2, p. 5), not from single-crack σ–δ tests.
- **Flexure (4PB):** flexural hardening in all specimens on average at 14 and 28 d; a few Y specimens
  did not harden. 1-layer printed ≈ cast (ref. 41). **More layers → fewer cracks and lower deflection at
  peak** (X at 28 d: ≈2.75 mm for 1L vs ≈1.0 mm for 3–4L), i.e. less ductility in thicker elements, while
  MOR stayed roughly constant (X ≈7–7.5, Y ≈3.3–3.9 MPa) (Section 3.3, pp. 9–11, Figs. 4–6).
- **Tension LPA:** X strain-hardened; only a few Y specimens did; multiple cracking (DIC) in all but
  Y specimen 4 (Section 3.4.1, pp. 11–14, Figs. 7–11). Strain capacity lower than the cast originals (refs. 33–34).
- **Tension LPE:** X still strain-hardened; Y ductile but large scatter → high anisotropy (Section 3.4.2, p. 14, Fig. 12, Table 5).
- **Interlayer tension:** little ductility, no strain hardening (few fibres cross the interface); 3 vs
  36 min interval had a small, not significant effect (X ≈2.4 vs ≈1.9 MPa); interface strength comparable to or
  slightly above bulk LPA/LPE strength; Conclusions (p. 20) say "in the same range" as first-crack strength
  (Section 3.5, pp. 15–16, Figs. 13–14).
- **µCT:** total air-void content "significantly higher" than usual for SHCC (p. 16; no single number given).
  Void area per slice ≈12–14% in the X layers and ≈10% at the X interface (read from Fig. 15, p. 17); ≈2–7% in Y
  (read from Fig. 16, p. 18; legend colours in Fig. 16 appear swapped). The **interface is the lowest-void zone**,
  with higher voids just above and below it (p. 17).
- **Fibre orientation:** histogram peaks at ≈40° (≈9% X, ≈8% Y) and ≈170° (≈7–8%); minima at ≈90° (≈1.5–2%) and
  low at 0–10°/180° (≈2.5–3.5%) — i.e. mainly **diagonal**, few fibres parallel or perpendicular to the print
  direction (read from Fig. 17, p. 19).

## Mechanisms / explanations offered by authors
- **Thickness effect in flexure:** geometric — higher tensile force in the tension zone pulls fibres out
  promptly; plus layer interfaces stronger than the bulk lower ductility (ref. 59) (Section 3.3, pp. 9–11).
- **Reduced ductility vs cast originals:** printable mix changes (less water, HPMC → stronger matrix
  via lower capillary porosity and internal curing), casting/mixing, and especially high air-void
  content that hinders fibre orientation (Sections 3.4.1, 3.6, pp. 14, 16).
- **Strong interlayer:** each layer is extruded against the previous one (compaction under nozzle
  pressure, cf. ref. 45); HPMC water reservoir / internal curing (Section 3.5, p. 16).
- **Diagonal fibres:** flexible PVA under high extrusion force; mainly the shear from pressing a layer
  onto the previous one, combined with nozzle movement and flow-speed differences (Section 3.6, p. 18, Fig. 18).
- **X vs Y:** differences in maximum aggregate size and W/B (0.4 vs 0.5) (Section 3.2, p. 8).

## Limitations (stated + observed)
- Stated: thick elements fail to deliver high ductility; further research needed (Conclusions, pp. 19–20).
- Observed: fibre length and diameter not reported; HPMC dosage basis not stated; LPE specimens very short
  (30 mm) compared with LPA (150 mm), so strains are not directly comparable; 4PB and interlayer values
  given only in figures; void content given only as profiles (no single number); n = 5 tensile specimens per
  series; crack widths not reported; single printer/nozzle setup; 4PB rate 1 mm/s unusually high.
- Observed: "fracture toughness" J values from flexural CMOD are an unconventional use of J_tip / J_b.

## Relation to other work
- Agrees with: Ogura et al. 2018 and Yu & Leung 2019 (as cited, Sections 1, pp. 2–3): strain hardening survives
  printing; interlayer direction is weakest in ductility.
- Contradicts: ⚔️ "interlayer is usually weaker than bulk" (Wolfs 2019; Feng 2015, as cited, p. 16); here interface
  strength ≥ bulk first-crack. Also ⚔️ the common report of fibres aligned with the print direction
  (refs. 22, 23, 27, as cited, p. 2) — here mainly diagonal.
- Extends: the authors' earlier rheology-based design of printable SHCC (Chaves Figueiredo et al. 2019,
  Mater. Des., ref. 41, not ingested); Kanda & Li 2006 J_b > J_tip criterion (ref. 56) → [[kanda2006-psh-design-criteria]].

## Pages updated from this source
- [[3d-printed-hdc]] · [[fiber-dispersion]] · [[fresh-properties]] · [[pva-fiber]] · [[strain-hardening]]
- [[tensile-strain-capacity]] · [[compressive-strength]] · [[flexural-strength]] · [[ggbfs]] · [[fly-ash]]
- [[dogbone-uniaxial-tension]] · [[digital-image-correlation]] · [[terminology-hdc-ecc-shcc]] · [[mix-designs]] · [[mechanical-results]]

## To verify
- [ ] J_tip and J_b units: the PDF prints "kJ/m²" (Table 3, p. 9; confirmed). 16–430 kJ/m² is implausibly large
  for J_tip (usually ~10 J/m²); the magnitudes match J/m² (MPa·µm) instead. But J_tip (16.37) even exceeds
  LOP × CMOD_LOP ≈ 1.10 × 10.60 ≈ 11.7 J/m², which the complementary-energy definition (Eq. 1) cannot exceed,
  so the values are internally inconsistent whatever the unit ⚠️ unverified.
- [ ] PVA fibre length, diameter and grade for these mixes (not in this paper; check ref. 41).
- [ ] Original cast strain capacity of these mixes (refs. 33, 34, 41) to quantify the loss due to printing.
- Resolved 2026-10-21: 4PB loading rate 1 mm/s confirmed as printed (p. 6). HPMC basis: not stated, but the
  computed HPMC/total-dry-solids ratios (0.30% X, 0.40% Y) match the mix names (see Materials).
