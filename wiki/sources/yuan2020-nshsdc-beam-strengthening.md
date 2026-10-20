---
type: source
slug: yuan2020-nshsdc-beam-strengthening
title: "Bond Strength and Flexural Capacity of Normal Concrete Beams Strengthened with No-Slump High-Strength, High-Ductility Concrete"
authors: [Tian-Feng Yuan, Se-Hee Hong, Hyun-Oh Shin, Young-Soo Yoon]
year: 2020            # Materials 13(19), article 4218; received 21 Jul 2020, accepted 21 Sep 2020, published 23 Sep 2020
venue: "Materials (MDPI) 13(19): 4218"
doi: "10.3390/ma13194218"
raw_file: raw/papers/Yuan2020_HSHDC-beam-strengthening.xml
material_term: "NSHSDC (no-slump, high-strength, high-ductility concrete); Table 5 also labels it 'NSHDC'. Hybrid fiber: 1.0 vol.% high-strength straight steel + 0.5 vol.% high-strength PE. Matrix f'c 123.4 MPa (28 d). Room-cured (20 °C, 60% RH), no heat treatment. Korea University (Yoon group). Tensile strain hardening is NOT shown in this paper; only direct tensile strength (9.7 MPa) is reported, and ε > 2.9% is quoted from the group's earlier papers (refs 12–13)."
study_type: "experimental (slant shear bond tests + 3-point bending of strengthened RC beams)"
tags: [nshsdc, hshdc-korea, hybrid-fiber, steel-fiber, pe-fiber, strengthening, jacketing, rc-beam, interface-bond, slant-shear]
ingested: 2026-10-20
updated: 2026-10-20
---

# NSC beams strengthened with no-slump HSHDC jackets (Yuan et al., 2020)

## One-paragraph summary
The Korea University (Yoon) group strengthens normal-strength concrete (NSC, f'c 46.2 MPa) with a
**no-slump high-strength, high-ductility concrete (NSHSDC)**: cement + silica fume + silica filler +
fine silica sand, W/B 0.172, and a **hybrid of 1.0 vol.% straight steel fiber and 0.5 vol.% PE fiber**
(28-d f'c 123.4 MPa, direct tensile strength 9.7 MPa; Table 5). Slant shear tests (100 × 100 × 300 mm
prisms, interface at 30–75°, as-cast vs chiselled substrate) show that chiselling raises slant shear
strength by about 27%, and that high-roughness interfaces meet the ACI 546 bond range (14–21 MPa at 28 d)
except at 75° (p. 3.1.2, Fig. 7). Six RC beams (125 × 250 × 2222 mm, 2 D19 bottom bars, no stirrups
except the reference B-SR) are tested in 3-point bending. Jacketing with NSHSDC raises peak load by
about 8% (top + bottom), 29% (three sides) and 40% (four sides) relative to the unstrengthened beam
B-NN (Table 8, Fig. 12). Bottom-only and top + bottom jackets do not prevent brittle shear failure;
the three-side jacket fails by concrete crushing with poor post-peak ductility; the four-side jacket
fails in flexure like the stirrup-reinforced beam, with the largest energy absorption (7.11 kN·m).
No jacket debonded from the NSC. → [[rc-member-strengthening]]

## Objective / research question
- Evaluate the interface bond (slant shear) between NSC substrate and NSHSDC overlay for two surface
  roughnesses and four interface angles (§1, §2.2.1).
- Evaluate the individual (bottom) and combined (top + bottom, three sides, four sides) contributions
  of NSHSDC jacketing to the flexural capacity of NSC beams; the authors state no earlier work had
  separated the longitudinal side contributions (§1).
- Motivation: UHPC jackets raise strength but reduce member ductility (over-reinforced behaviour) and
  need heat curing; NSHSDC is proposed as a room-cured, shape-holding alternative (§1).

## Materials & mix design
Table 2 (NSHSDC; mass ratio to cement, fibers in vol.%) and Table 1 (NSC substrate; kg/m³). Fibers: Table 4.

| Mix ID | Cement | Fly ash | Slag/other | Sand (type, max size) | W/B | SP | Fiber type | L (mm) | d (µm) | Vf (vol.%) |
|---|---|---|---|---|---|---|---|---|---|---|
| NSHSDC | 1.00 (Type I) | 0 | silica fume 0.25; silica filler 0.30 | silica sand 1.10, 0.08–0.30 mm | 0.172 (by mass; water 0.215 / (cement + SF) 1.25) | 3.0% (basis not stated ⚠️) | hybrid: straight high-strength steel + high-strength PE | steel 19.5; PE 12 | steel 200; PE 31 | steel 1.0 + PE 0.5 = 1.5 |
| NSC (substrate) | 380 kg/m³ (Type I) | 0 | none | crushed fine agg. 818 + coarse agg. 921 kg/m³ (max size not reported) | 0.43 (w/c) | 0.8% | none | n/a | n/a | 0 |

Units of binder quantities: NSHSDC = mass ratio to cement; NSC = kg/m³.
- Fiber properties (Table 4): steel 2650 MPa, 200 GPa, 7.8 g/cm³, L/d 97.5; PE 2900 MPa, 100 GPa,
  0.97 g/cm³, L/d 387. Table 4 also lists a hooked-end steel fiber (0.55 mm × 35 mm, 1400 MPa); the text
  never says where it is used ⚠️.
- Mix taken from the group's earlier papers (refs 12–13: Yuan et al. 2019 Int J Polym Sci; Yuan, Lee &
  Yoon 2020 Cem Concr Compos 106:103458), not wiki sources.
- Silica-fume surface area 200,000 cm²/g, cement 3492 cm²/g (Table 3).
- Fresh state: "no-slump", high shape-holding ability (§1); no slump/flow value given for NSHSDC. NSC slump 175 mm (Table 1).

## Test methods
- Specimen geometry:
  - Compression: ASTM C39 cylinders (size not reported); flexure: ASTM C1609 four-point (size not reported).
  - Tension: NSC by splitting (ASTM C496); NSHSDC by direct tension on dog-bone specimens per JSCE
    recommendations (geometry not reported here; refs 12–13). → [[dogbone-uniaxial-tension]]
  - Slant shear: ASTM C882, 100 × 100 × 300 mm prisms, interface at 30°, 45°, 60°, 75° to the vertical;
    low roughness = as cast (NSC cleaned after 24 h); high roughness = chiselled with an electric breaker (Table 6, Fig. 1).
  - Beams: 125 × 250 mm, 2222 mm long, 2 D19 bottom bars; B-SR adds Ø8 smooth U-stirrups at 101 mm
    (ACI 318-14 minimum). Jackets: substrate chiselled to 40 mm depth at the bottom and 20 mm on sides
    and top, then NSHSDC cast in a mould (Fig. 2–3). Configurations: B-NN, B-SR, B-BJ (bottom), B-2J (top + bottom),
    B-3J (two sides + bottom), B-4J (four sides).
- Loading / rate: slant shear on a 2500 kN UTM; beams in 3-point bending on a 1000 kN MTS 815 UTM, displacement
  control 0.25 mm/min.
- Measurement: load cell; 2 LVDTs (slant shear); mid-span LVDTs and rebar strain gauges (beams, Fig. 4).
- Curing & test age: all specimens room-cured at 20 ± 1 °C, 60 ± 5% RH; 28 d for material and slant shear
  tests; beam test age not stated ⚠️.
→ [[dogbone-uniaxial-tension]], [[flexural-strength]]

## Key results
| Mix ID | f'c (MPa) | First-crack stress (MPa) | Tensile strength (MPa) | Tensile strain capacity (%) | Crack width (µm) | Other |
|---|---|---|---|---|---|---|
| NSHSDC (28 d) | 123.4 (CV 0.3) | not reported | 9.7 direct tension (CV 1.6) | not reported here; "> 2.9%" (ε_c) quoted from refs 12–13 (§1) | not reported | flexural strength 21.9 MPa (CV 8.5), Table 5 |
| NSC (28 d) | 46.2 (CV 0.1) | n/a | 3.9 splitting | n/a | n/a | flexural strength 26.5 MPa (CV 0.6) ⚠️ (higher than NSHSDC; implausible for plain NSC) |

Slant shear (28 d, mean of 3; Table 7):

| Specimen | Failure (primary / secondary) | f_ck,s (MPa) | Norm. to NSC prism (48.6 MPa) | σ (MPa) | τ (MPa) |
|---|---|---|---|---|---|
| 30LS / 30HS | CC / – | 37.9 / 48.2 | 0.78 / 0.99 | 28.4 / 36.2 | 16.4 / 20.9 |
| 45LS / 45HS | NI / CC | 29.1 / 42.9 | 0.60 / 0.88 | 14.6 / 21.5 | 14.5 / 21.4 |
| 60LS / 60HS | NI / IS | 14.0 / 30.4 | 0.29 / 0.63 | 3.5 / 7.6 | 6.1 / 13.2 |
| 75LS / 75HS | NI / IS | 10.4 / 17.7 | 0.21 / 0.36 | 1.0 / 1.7 | 3.1 / 5.3 |

CC = total concrete crushing; NI = near-interface concrete cracking; IS = interface sliding.

Beams (Table 8):

| Beam | P_cr (kN) | P_p (kN) | δ_p (mm) | δ_f (mm) | Ductility δ_p/δ_cr | Energy (kN·m) | Failure |
|---|---|---|---|---|---|---|---|
| B-NN | 11.81 | 75.93 | 10.17 | 10.17 | 7.82 | 0.39 | shear |
| B-SR | 12.88 | 91.58 | 55.08 | 62.40 | 38.82 | 5.73 | rebar yield then concrete crushing |
| B-BJ | 12.37 | 74.04 | 9.48 | 9.48 | 6.63 | 0.35 | shear |
| B-2J | 13.41 | 82.19 | 11.21 | 11.21 | 7.14 | 0.46 | shear |
| B-3J | 13.67 | 97.71 | 15.36 | 41.43 | 9.91 | 3.32 | concrete crushing, no rebar yield, softening |
| B-4J | 13.70 | 106.12 | 18.80 | 79.24 | 12.45 | 7.11 | flexure, cracks over 1610 mm |

Main findings (with Table/Fig. location):
- Chiselling raises slant shear strength by about 27% over as-cast interfaces (§3.1.1, Fig. 6).
- Interface shear strength rises as the interface angle falls; 30° specimens fail by total crushing of the NSC (Table 7, Fig. 5).
- High-roughness interfaces meet ACI 546 (14–21 MPa at 28 d) except at 75°; low-roughness ones meet it only at 30–45° (Fig. 7, Conclusion 1).
- Design codes (ACI 318-19, AASHTO-LRFD, CSA, MC2010) under-predict τ: mean τ/τ_pred 22.5 (ACI), 1.5 (AASHTO), 3.6 (CSA), 1.7 (fib) (Table 7). ⚠️ The conclusion gives 1.27–2.17, which does not match Table 7.
- Peak-load gains vs B-NN: +8% (B-2J), +29% (B-3J), +40% (B-4J); vs B-SR: +6.7% (B-3J), +15.9% (B-4J) (§3.2.3, Fig. 12). B-BJ: −2.5% (74.04 vs 75.93 kN, computed from Table 8).
- No jacket delaminated from the NSC substrate (§3.2.1, Conclusion 2). Fiber pull-out "sound" was heard in B-BJ (§3.2.1).
- B-3J crushed in compression without rebar yielding, with "a considerable loss of ductility"; B-4J reached rebar strain similar to B-SR (§3.2.2).

## Mechanisms / explanations offered by authors
- Roughness increases mechanical interlock between NSC and NSHSDC, raising slant shear strength (§3.1.1).
- Bottom and top + bottom jackets cannot work at full capacity because the unstrengthened NSC web cracks in shear at low load (§3.2.3).
- Adding more jacketed sides moves the beam toward over-reinforced behaviour (stiffer, compression-controlled) (§3.2.3, citing ref 2).
- Four-side confinement plus the top jacket allows flexural failure with wide crack distribution (§3.2.1).

## Limitations (stated + observed)
- One beam per configuration; no repeat specimens (observed).
- The paper reports no tensile stress–strain curve, strain capacity, crack width or crack count for NSHSDC; ductility is only quoted from earlier papers (observed).
- Reported rebar strains are inconsistent in magnitude (e.g. "0.77 × 10⁻⁶ mm/mm" at shear failure; 0.04771 mm/mm for B-4J) ⚠️ (§3.2.2).
- Beam test age and NSHSDC jacket curing age not stated (observed).
- NSC flexural strength (26.5 MPa) is implausibly high for a 46 MPa concrete ⚠️ (Table 5).
- The beams lack stirrups, so most configurations fail in shear; this limits conclusions on flexural strengthening (observed).

## Relation to other work
- Agrees with: [[rc-member-strengthening]] (He 2024 review lists Korean steel + PE strengthening work; this may be the "Yuan 2020" cited there ⚠️); [[hshdc]] in that heat curing is not required for > 120 MPa.
- Contradicts: ⚔️ none directly; but "HSHDC/NSHSDC" here is a **fourth lineage** (Korea Univ., hybrid steel + PE, 1.5 vol.%) beside Michigan, GDUT and Xi'an — see [[terminology-hdc-ecc-shcc]].
- Extends: first primary source in the wiki on NSC–HDC interface bond (cf. the open bond issue in [[yang2024-hshdc-uniaxial-tension]], p. 14).

## Pages updated from this source
- [[rc-member-strengthening]]
- [[hshdc]]
- [[terminology-hdc-ecc-shcc]]
- [[pe-fiber]]
- [[repair-and-field-applications]]

## To verify
- [ ] Tensile strain capacity of NSHSDC (> 2.9% quoted from refs 12–13); obtain Yuan, Lee & Yoon 2020 (CCC 106:103458) to confirm strain hardening and multiple cracking.
- [ ] SP 3.0%: basis (binder or cement mass) not stated.
- [ ] Use of the hooked-end steel fiber listed in Table 4.
- [ ] Rebar strain magnitudes in §3.2.2 (likely unit errors).
- [ ] NSC flexural strength 26.5 MPa in Table 5.
- [ ] Conclusion τ/τ_pred range 1.27–2.17 vs Table 7 means 1.5–22.5.
- [ ] Whether this is the "Yuan 2020 (steel wire + ECC)" cited in [[he2024-hdc-research-advances]], p. 19–20.
- [ ] Beam test age.
