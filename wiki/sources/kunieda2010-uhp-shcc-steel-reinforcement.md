---
type: source
slug: kunieda2010-uhp-shcc-steel-reinforcement
title: "Enhancement of Crack Distribution of UHP-SHCC under Axial Tension Using Steel Reinforcement"
authors: [Minoru Kunieda, Mohamed Hussein, Naoshi Ueda, Hikaru Nakamura]
year: 2010            # JACT Vol. 8, No. 1, February 2010; received 24 Jul 2009, accepted 15 Dec 2009
venue: "Journal of Advanced Concrete Technology (Japan Concrete Institute) 8(1): 49–57"
doi: "not printed in the PDF; probably 10.3151/jact.8.49 ⚠️ unverified"
raw_file: raw/papers/Kunieda2010_UHP-SHCC-steel-reinforcement.pdf
material_term: "UHP-SHCC (Ultra High Performance-Strain Hardening Cementitious Composites), Nagoya University (Kunieda et al. 2007). PE fiber 1.5 vol.% (6 mm × 12 µm); low-heat Portland cement + 15% silica fume, W/B 0.20; f'c 95 MPa; cured under wet towels for 4 weeks (ambient, no heat). Dumbbell specimens show strain hardening with multiple cracking (σ_tu 6.5 MPa, ε_u 1.5%); unreinforced 50 mm-thick members do NOT (brittle, ε 0.23–0.24%)."
study_type: "experimental (uniaxial tension of dumbbell specimens and practical-size R/UHP-SHCC tension members)"
tags: [uhp-shcc, shcc, pe-fiber, size-effect, fiber-orientation, steel-reinforcement, tension-stiffening, multiple-cracking, crack-spacing, surface-protection, repair]
ingested: 2026-10-20
updated: 2026-10-20
---

# Steel reinforcement to restore crack distribution in thick UHP-SHCC (Kunieda et al., 2010)

## One-paragraph summary
UHP-SHCC (PE 1.5 vol.%, 6 mm × 12 µm; W/B 0.20; f'c 95 MPa) is intended for thin surface-protection
repair layers (30–70 mm). Small dumbbell specimens (13 × 30 mm section) give σ_tu 6.5 MPa and ultimate
strain 1.5% at 28 d (§3.2). But **practical-size members (50 × 200 mm section, 900 mm long) without
reinforcement lose most of this ductility**: average ultimate strain 0.23–0.24% (about 85% lower) and
stress about 30% lower, with only 43–45 cracks and a near-brittle response (Table 3, Fig. 5, §4.1). The
authors attribute this to fiber orientation: 2-D in the 13 mm dumbbells vs 3-D in the 50 mm members.
Adding a **small amount of deformed steel (D6 bars, ρs 0.3–1.2%)** restores strain hardening with
multiple cracking in every reinforced member: with ρs 0.3%, average ultimate strain is 1.58% (6.6× the
unreinforced), cracks rise to 119 (2.76×), average crack spacing falls from 12–14 mm to 4.5–4.6 mm,
and the strain scatter along the member halves (Table 3, Figs. 10–16). Above ρs 0.6% the crack count
and spacing hardly change (Conclusion 3). The ultimate load must be at least about 1.5× the cracking
load to form distributed cracks (§4.4). → [[size-effect]], [[fiber-dispersion]], [[multiple-cracking]]

## Objective / research question
- Provide tension data for UHP-SHCC members of practical thickness for surface-protection repair (§1).
- Compare crack distribution and strain capacity of small dumbbell vs practical-size specimens (§1).
- Find the minimum steel reinforcement that ensures crack distribution and strain capacity (not strengthening) in thick members (§1–2).

## Materials & mix design
Table 2 (kg/m³), §3.2.

| Mix ID | Cement | Fly ash | Slag/other | Sand (type, max size) | W/B | SP | Fiber type | L (mm) | d (µm) | Vf (vol.%) |
|---|---|---|---|---|---|---|---|---|---|---|
| UHP-SHCC | 1243 (low-heat Portland, 3.14 g/cm³) | 0 | silica fume 223 (15% of design cement replaced); expansion agent 20; air reducer 2.98 | quartz sand 149, < 0.2 mm | 0.20 (by mass; 292 / (1243 + 223 + 20) = 0.196, computed) | 14.9 | high-strength PE | 6 | 12 | 1.5 (14.6 kg/m³) |

Units of binder quantities: kg/m³.
- Reinforcement: deformed D6 bars (31.67 mm² each), f_y 320 MPa, f_u 529 MPa, E 200 GPa; yield load per bar 10.13 kN (§3.2, Fig. 3, §4.5). D13 bars at the ends as grips (3, or 4 for S-4).
- PE fiber strength and modulus: not reported.

## Test methods
- Specimen geometry:
  - Dumbbell ("small-size"): tested section 13 × 30 mm, 10 specimens (gauge length not reported) → [[dogbone-uniaxial-tension]].
  - Large-size members: 50 × 200 mm section, 900 mm long (500 mm test zone between 200 mm end zones), ρs 0 / 0.3 / 0.6 / 0.9 / 1.2% (0–4 D6), 2 per case (Table 1, Fig. 4).
  - Compression: six Ø50 × 100 mm cylinders.
- Loading / rate: 2000 kN tensile machine, load control, gripping the D13 bars; loaded to localized fracture (§3.3). Rate not reported.
- Measurement: ten Pi-shaped displacement transducers, gauge length 100 mm, accuracy 0.0005 mm, on all faces (§3.3). Crack spacing counted after test (Fig. 14).
- Curing & test age: covered with wet towels in a curing room for 4 weeks; material properties at 28 d (§3.2).
→ [[dogbone-uniaxial-tension]]

## Key results
| Mix ID | f'c (MPa) | First-crack stress (MPa) | Tensile strength (MPa) | Tensile strain capacity (%) | Crack width (µm) | Other |
|---|---|---|---|---|---|---|
| UHP-SHCC dumbbell (28 d) | 95 (Ø50 × 100) | not reported | 6.5 | 1.5 (strain at ultimate load, average of 10) | not reported | — |
| S-0 (unreinforced 50 × 200, ρs 0) | — | 3.9–4.2 (P_cr/A, computed) | 4.7–5.0 (P_u/A, computed) | 0.23–0.24 avg (max local 0.72–0.85) | not reported | 43–45 cracks; spacing 12–14 mm |
| S-1 (ρs 0.3%) | — | 4.1–4.2 (computed, incl. bar) | 6.4–6.5 nominal incl. bar (computed) | 1.58–1.60 avg (max 2.30–2.38) | not reported | 118–119 cracks; spacing 4.5–4.6 mm |

Full Table 3 (two specimens per case):

| Specimen | ρs (%) | P_cr (kN) | P_u (kN) | S_r-av (mm) | S_r-max (mm) | N cracks | ε_u-av (%) | ε_u-max (%) | ε_u-av/ε_cr-av | ε_u-av/ε_u-av-D |
|---|---|---|---|---|---|---|---|---|---|---|
| S-0-1 / S-0-2 | 0 | 42 / 39 | 50 / 47 | 12.0 / 14.0 | 176 / 185 | 43 / 45 | 0.24 / 0.23 | 0.717 / 0.851 | 14 / 13 | 0.16 / 0.15 |
| S-1-1 / S-1-2 | 0.3 | 42 / 41 | 64 / 65 | 4.6 / 4.5 | 40 / 42 | 119 / 118 | 1.58 / 1.60 | 2.377 / 2.301 | 102 / 101 | 1.05 / 1.06 |
| S-2-1 / S-2-2 | 0.6 | 40 / 40 | 74 / 73 | 4.0 / 4.0 | 10 / 10 | 128 / 130 | 1.49 / 1.50 | 2.276 / 2.266 | 103 / 106 | 0.99 / 1.00 |
| S-3-1 / S-3-2 | 0.9 | 38 / 37 | 85 / 85 | 3.6 / 3.6 | 10 / 10 | 136 / 140 | 1.51 / 1.51 | 2.882 / 2.652 | 104 / 106 | 1.01 / 1.00 |
| S-4-1 / S-4-2 | 1.2 | 36 / 36 | 104 / 103 | 3.4 / 3.3 | 10 / 9 | 152 / 156 | 1.82 / 1.80 | 2.451 / 2.401 | 130 / 128 | 1.21 / 1.20 |

Main findings (with Table/Fig. location):
- **Thickness/size effect:** unreinforced 50 mm members lose about 85% of ultimate strain and about 30% of stress vs 13 mm dumbbells; the response changes from strain hardening with multiple cracking to brittle failure (§4.1, Fig. 5). Last crack formed at 1.05× the cracking load; no new cracks above 90% of P_u (§4.4).
- More than 90% of ultimate strain develops after first cracking (§4.1).
- **ρs 0.3% is enough** to match or exceed the dumbbell strain and strength (ε_u-av/ε_u-av-D 1.05–1.06) (Table 3, Figs. 7–8, 12).
- Strain scatter (max − min along the axis) falls by about 50% at ρs 0.3% (Fig. 11, Conclusion 2).
- Beyond ρs 0.6%, crack spacing and number change little; minimum strain does not rise further (Figs. 11, 15–16).
- Ultimate load rises with ρs: +40% (S-1-2), +60% (S-2-1), +80% (S-3-1), +126% (S-4-1) vs S-0-1 (§4.3); the increase ≈ steel contribution (Fig. 6).
- Cracking load falls slightly with ρs (42 → 36 kN), attributed to restrained shrinkage; only about 3% drop at 0.6% (§4.3). → [[shrinkage]]
- Steel carries 18.5% (S-1-1) to 49.8% (S-4-1) of the load at bar yield (Fig. 17).
- Cracking strain ≈ 8% of rebar yield strain, so UHP-SHCC carries the load until first cracking (§4.5).
- Rule of thumb: P_u ≥ about 1.5 P_cr to obtain distributed transverse cracks (S-1-1, §4.4).

## Mechanisms / explanations offered by authors
- Strain capacity depends on the margin between the distribution of matrix cracking strength and the distribution of fiber-bridging strength along the member (Fig. 2). Larger specimens widen the bridging-strength distribution and lower its mean, reducing strain capacity (§2). → [[fiber-bridging]], [[strain-hardening]]
- Fiber orientation: nearly 2-D in 13 mm dumbbells, more 3-D in 50 mm members, lowering bridging capacity (§4.1; citing Torigoe 2003, Kanakubo 2006, Kunieda 2008). → [[fiber-dispersion]]
- Steel bars "support" fiber bridging: per D6 bar, about +1.01 MPa nominal bridging strength (at yield) vs only about +0.07 MPa cracking strength (at 100 µε), so cracks spread (§2, Fig. 3).
- High-modulus steel lowers the fiber stress after cracking and raises axial stiffness at cracks, allowing more cracks (§4.3–4.4).
- Strain-hardening condition: post-cracking strength > cracking strength (Matsumoto & Mihashi 2002, as cited, §1).
- SHCC cracks < 40 µm resist water, CO₂, O₂ penetration and change corrosion from macro-cell to micro-cell (JSCE 2004, as cited, §1). → [[crack-width]], [[durability]]

## Limitations (stated + observed)
- Crack widths were not measured; only spacing and number (observed).
- Only one thickness (50 mm) of large member; the size effect is not separated from fiber-orientation effects by direct measurement (observed).
- Fig. 5 dumbbell curves continue to about 2.5–3% strain, while the text gives 1.5% "strain at ultimate load" ⚠️ (observed).
- Loading rate, dumbbell gauge length and PE fiber properties not reported (observed).
- Concept ("UHP") with f'c 95 MPa and σ_tu 6.5 MPa sits below current HSHDCC thresholds (> 100 MPa) — see [[terminology-hdc-ecc-shcc]] (observed).

## Relation to other work
- Agrees with: [[li2003-ecc-review]] (R/steel–ECC deformation compatibility, Fischer & Li 2002, as cited there); Kesner 2003 and Mechtcherine 2011 (as cited in [[yu2018-ecc-direct-tensile-review]], p. 348–350): larger/cylindrical specimens give lower strain capacity, attributed to fiber orientation.
- Contradicts: ⚔️ Rokugo 2007 (as cited in [[yu2018-ecc-direct-tensile-review]], p. 348–350): thickness 13/30/50 mm had a negligible effect on PVA-ECC σ_tu, ε and cracking; here 13 → 50 mm thickness cuts ε by about 85% in PE UHP-SHCC (6 mm fibers, dense matrix). Possible reasons: fiber type/length, matrix strength, member length (900 mm vs dogbone), end/grip conditions.
- Contradicts (refinement): ⚔️ [[size-effect]] currently records "no size effect in UHDC-2" (flexure, notched beams, [[ye2021-uhdc-flexural-size-effect]]); here a strong thickness effect is found in direct tension (ε −85% from 13 mm to 50 mm thickness). Different loading mode, fiber length and matrix — refinement rather than direct conflict.
- Extends: dogbone-derived ε_tu can strongly overestimate member ductility in thick sections → caution for all dogbone values in [[mechanical-results]].

## Pages updated from this source
- [[size-effect]]
- [[fiber-dispersion]]
- [[multiple-cracking]]
- [[tensile-strain-capacity]]
- [[dogbone-uniaxial-tension]]
- [[repair-and-field-applications]]
- [[pe-fiber]]
- [[shrinkage]]
- [[terminology-hdc-ecc-shcc]]
- [[crack-width]]

## To verify
- [ ] DOI (not printed; probably 10.3151/jact.8.49).
- [ ] Dumbbell ε_u 1.5% vs Fig. 5 curves extending to about 2.5–3%.
- [ ] Dumbbell gauge length and loading rate (perhaps in Kunieda et al. 2007, RILEM HPFRCC5).
- [ ] PE fiber tensile strength and modulus.
- [ ] Test age of the large members (only material properties are stated at 28 d).
