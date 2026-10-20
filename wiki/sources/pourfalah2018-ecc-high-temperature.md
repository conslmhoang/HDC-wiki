---
type: source
slug: pourfalah2018-ecc-high-temperature
title: "Behaviour of engineered cementitious composites and hybrid engineered cementitious composites at high temperatures"
authors: [S. Pourfalah]
year: 2018            # Construction and Building Materials 158 (2018); received 21 Apr 2017, accepted 18 Oct 2017, online 5 Nov 2017
venue: "Construction and Building Materials 158 (2018) 921–937"
doi: "10.1016/j.conbuildmat.2017.10.077"
raw_file: raw/papers/Pourfalah2018_ECC-high-temperature.pdf
material_term: "ECC (PVA only) and HECC = hybrid ECC (H6ECC, H13ECC: PVA + 6 mm or 13 mm straight steel fibre). Tensile strain hardening IS shown at 20 °C in JSCE-type dog-bones (Fig. 3, Table 4: strain at peak 2.5–3.5%). Tension was tested only at 20 °C; compression and four-point bending were tested HOT (in situ) at 20–600 °C."
study_type: experimental + numerical (FE, ADINA)
tags: [ecc, hecc, hybrid-fiber, pva-fiber, steel-fiber, fly-ash, high-temperature, in-situ-hot-testing, spalling, debris, compression, four-point-bending, dog-bone-tension, crack-width, fe-model, heriot-watt]
ingested: 2026-10-21
updated: 2026-10-21
---

# ECC and hybrid PVA/steel ECC tested hot at 20–600 °C (Pourfalah, 2018)

## One-paragraph summary
A single-author study (Heriot-Watt University; tests at the Edinburgh University fire laboratory) compared
a PVA-ECC (2.0 vol.% PVA, derived) with two hybrid ECCs (1.75 vol.% PVA + 0.75 vol.% straight steel fibre,
6 mm or 13 mm long) (Table 2). At 20 °C all three strain-harden in dog-bone tension: ECC σ_tu 3.85 MPa at
3.5% strain, H6ECC 4.36 MPa at 3.0%, H13ECC 4.71 MPa at 2.5% (Table 4). Cubes (50 mm) and small prisms
(170 × 40 × 20 mm) were heated at 10 °C/min, held 30 min, and **tested at temperature** inside the heating
chamber (§3.4). Hot compressive strength of ECC fell 6/10/25% at 200/400/600 °C (Table 5, §4.2). **No
spalling up to 600 °C** in any mix; but ECC cubes shed 30% of their mass as debris at 600 °C vs 8.5% for
both HECCs (Fig. 7b). In bending, deflection capacity rose up to 60–100 °C with fewer but much wider cracks
(ECC ≈ 50 µm at 20 °C to several hundred µm at 60–100 °C); from 150 °C PVA pulled out without rupture
and all mixes became deflection-softening; ECC was brittle from 200 °C, while steel kept HECC
softening-ductile up to 600 °C with about twice the ECC load (§4.3, Figs. 9–12; Conclusions). An FE
model (ADINA, smeared crack) back-fitted tensile curves at each temperature (Table 6).

> Synthesis: this is the wiki's **first primary in-situ (hot) test on ECC** and the primary source behind the
> "4× debris" statement previously known only as cited. It shows bending ductility is lost at about 150 °C
> when tested hot, i.e. ≈ 80 °C below the 230 °C PVA melting onset measured by TG in
> [[zhou2023-hsecc-elevated-temperature]] — consistent with Mechtcherine 2012 (in situ, SH lost at 150 °C,
> as cited in [[high-temperature-behaviour]]).

## Objective / research question
- How do ECC and hybrid PVA/steel ECC behave in compression and flexure at 20–600 °C, and can steel fibres
  improve integrity and ductility at high temperature (§1, p. 922)?
- Effect of steel-fibre length (6 vs 13 mm) at 0.75 vol.% (§1).
- 600 °C was the furnace limit (p. 922).

## Materials & mix design
Constituents (§2, Tables 2–3):
- **Cement:** Type I 52.5 N. **Fly ash:** SV80. **Sand:** fine silica sand, average particle size 120 µm
  (text prints "120 mm"; extraction/print artefact ⚠️).
- **HRWR:** 4.5 kg/m³ (type not reported).
- **PVA:** L 12 mm, d 40 µm (0.04 mm), σ_f 1600 MPa, **E 14 GPa** ⚠️ (as printed; other wiki PVA entries ≈ 40 GPa),
  ρ 1300 kg/m³. Maker and oiling not stated.
- **Steel (straight):** St 6: L 6 mm; St 13: L 13 mm; both d 150 µm, σ_f 3000 MPa, E 210 GPa, ρ 7800 kg/m³.

| Mix ID | Cement | Fly ash | Slag/other | Sand (type, max size) | W/B | SP | Fiber type | L (mm) | d (µm) | Vf (vol.%) |
|---|---|---|---|---|---|---|---|---|---|---|
| ECC | 454 | 817 | none | silica sand 273 (avg 120 µm; max n.r.) | 0.28 (356/1271, derived) | HRWR 4.5 | PVA | 12 | 40 | 2.0 (26 kg/m³ ÷ 1300, derived) |
| H6ECC | 451 | 817 | none | silica sand 273 | 0.28 (354/1268, derived) | HRWR 4.5 | PVA + steel St 6 | 12 / 6 | 40 / 150 | 1.75 PVA + 0.75 steel (stated §2; = 22.75/1300 and 58.86/7800) |
| H13ECC | 451 | 817 | none | silica sand 273 | 0.28 (derived) | HRWR 4.5 | PVA + steel St 13 | 12 / 13 | 40 / 150 | 1.75 PVA + 0.75 steel |

Units of binder quantities: kg/m³ (Table 2). FA/C = 1.80 by mass (derived); sand/binder ≈ 0.21 by mass (derived).
Water 356 / 354 kg/m³.

## Test methods
- Specimen geometry: dog-bone 330 mm long, 80 mm central gauge, 30 × 13 mm narrow section, 60 mm wide ends
  (Fig. 1a; dimensions read from drawing ⚠️); compression 50 mm cubes (BS 1881-116); bending prisms
  170 × 40 × 20 mm, four-point, clear span 150 mm, 40 mm between load points, 55 mm shear spans (§3.3).
- Loading / rate: all tests displacement-controlled at 1 mm/min; cubes loaded to 6% strain (§3.1–3.3).
- Measurement (LVDT, DIC, ...): tension — two LVDTs over 80 mm gauge, 100 kN Instron (§3.1); compression and
  bending — crosshead of a 600 kN Instron with integrated heating chamber, plus digital camera (§3.2–3.3).
- Heating: 10 °C/min to target, 30 min hold, then tested **at temperature** (in situ) (§3.4, Fig. 2b).
  Schedule (Table 1): tension 20 °C only; compression 20, 200, 400, 600 °C; flexure 20, 60, 100, 150, 200, 400, 600 °C.
- Curing & test age: tension specimens 24 h under film, then water at 20 ± 3 °C for 28 d; compression and
  bending specimens 21 d in water + 7 d lab air (20 ± 3 °C, 60% RH) to reduce spalling risk (§2). Test age ≈ 28 d.
→ [[dogbone-uniaxial-tension]], [[high-temperature-behaviour]]

## Key results
| Mix ID | f'c (MPa) | First-crack stress (MPa) | Tensile strength (MPa) | Tensile strain capacity (%) | Crack width (µm) | Other |
|---|---|---|---|---|---|---|
| ECC, 20 °C | 38.8 (50 mm cube) | 2.75 (ε 0.018%) | 3.85 | 3.5 (at max stress) | ≈ 50 (bending, §4.3) | E_t 15.4 GPa; E_c 40.2 GPa |
| H6ECC, 20 °C | 40.1 | 2.89 (ε 0.019%) | 4.36 | 3.0 | ≈ 40 (bending) | E_t 15.1 GPa |
| H13ECC, 20 °C | 45 | 3.32 (ε 0.018%) | 4.71 | 2.5 | ≈ 40 (bending) | E_t 18.5 GPa |

Tables 4–5. Hot compression (Table 5, f'c MPa at 20 / 200 / 400 / 600 °C; strain at peak; E):
- ECC: 38.8 / 36.15 / 35.1 / 29.2 MPa; E 40.2 / 37.6 / 27.0 / 19.4 GPa.
- H6ECC: 40.1 / 38.45 / 32 / 27.2 MPa; E 40.1 / 38.4 / 24.6 / 20.1 GPa.
- H13ECC: 45 / 38.5 / 32.8 / 29.5 MPa; E 38.1 / 32.0 / 21.2 / 17.5 GPa.

Main findings (with Table/Fig. location):
- Tension (20 °C): HECC strain capacity 16% (H6) and 40% (H13) lower, peak stress 13% and 22% higher than ECC;
  crack number ECC > H6ECC > H13ECC (§4.1, Fig. 4). (Note: Table 4 gives 3.0/3.5 = −14% and 2.5/3.5 = −29%.)
- Hot f'c reduction vs 20 °C: ECC 6/10/25%, H6ECC 6/11/33%, H13ECC 14/27/35% at 200/400/600 °C (§4.2, Fig. 6a);
  E falls with temperature in all mixes (Fig. 6b). Conclusions state "14% and 25%" at 400/600 °C ⚠️.
- Mass loss ≈ 10% at 200 °C (moisture), ≈ 12% at 400 °C and ≈ 14% at 600 °C (PVA burning) (Fig. 7a, §4.2).
- Debris from cubes: ECC 2 / 21 / 30% at 200 / 400 / 600 °C vs 2 / 3 / 8.5% for both HECCs; steel length
  irrelevant (Fig. 7b). Conclusions: "4 times less" at 600 °C (30/8.5 ≈ 3.5×).
- **No spalling or explosive spalling in any specimen up to 600 °C**, credited to PVA pore network (§4.2, p. 926).
- Bending deflection capacity ×3 / ×1.5 / ×2 at 60 °C and ×1.5 / ×1.2 / ×1.5 at 100 °C (ECC / H6ECC / H13ECC)
  vs 20 °C (Conclusions; Fig. 10c).
- First-crack and peak bending loads fall up to 100 °C, then are roughly constant to 600 °C; HECC peak load ≈ 2×
  ECC at 100–600 °C (Fig. 10a–b; Conclusions). ECC peak ≈ 1300–1400 N at 20 °C to ≈ 420–460 N at 150–400 °C
  (Fig. 10b ⚠️ read from figure).
- Crack number: ECC ≈ 15–23 at 20 °C, falls with temperature; one crack in all mixes from 150 °C (Fig. 10d, Fig. 11).
- Average crack width (text): ECC 50 → 400 µm (60 °C) → 750 µm (100 °C); HECC 40 → 70 → 200 µm (§4.3). Fig. 10e
  plots ECC ≈ 570–770 µm at 60 °C and ≈ 940–1070 µm at 100 °C ⚠️; p. 930 text says ≈ 1 mm (ECC) vs 0.2 mm (HECC)
  at 60 °C.
- PVA pull-out length at failure: ≈ 500 µm (20 °C), 3000 µm (60 °C), 5000 µm (100 °C), up to 6000 µm (150 °C);
  PVA ruptures below 150 °C, pulls out completely at 150 °C with reduced diameter; dark/burned at 200 °C; absent at
  400 °C (Fig. 12, §4.3).
- Steel fibres pull out up to 400 °C and **rupture at 600 °C** (pull-out ≈ 0.5 mm for 6 mm, ≈ 0.2 mm for 13 mm before
  rupture) (Fig. 14).
- FE back-fitted tensile curves: ECC max strain 3.5 (20 °C), 12 (60 °C), 6 (100 °C) %; strain-softening from 150 °C
  (Table 6). These are fitted inputs, not measurements ⚠️ (see To verify).

## Mechanisms / explanations offered by authors
- Up to 100 °C: lower PVA modulus and lower PVA–matrix chemical bond → longer debonded length, wider cracks, more
  deflection, lower bridging peak (§4.3). States that 60 °C is the glass-transition temperature of PVA, where 80%
  of its modulus is lost (p. 928; no citation ⚠️).
- At 150 °C: PVA loses bridging ability and pulls out → deflection softening; 200 °C: fibres burn → ECC brittle (§4.3).
- Steel fibres limit crack width (≈ 5× smaller at 60–100 °C) and carry load after PVA loss; thermal expansion of
  steel (higher CTE than matrix) raises bond so fibres rupture at 600 °C, where steel yield strength also drops (p. 929).
- Longer steel (13 mm) bonds better → less ductility, more strength; recommends 6 mm steel (p. 929–930).
- PVA prevents spalling by creating vapour-release pores (§4.2).

## Limitations (stated + observed)
- Stated: 600 °C furnace limit; FE elastic branch stiffer than experiments (rough faces, air bubbles) (§5.2).
- Observed: tension tested only at 20 °C; hot strain hardening is inferred from bending and FE fitting.
- Observed: very small bending prisms (20 mm deep) and 50 mm cubes; specimen counts mostly 1–2 per temperature
  (Figs. 5, 9 legends).
- Observed: 30 min hold may not give uniform temperature in 50 mm cubes (no thermocouple data reported).
- Observed: internal inconsistencies ⚠️ — crack widths text vs Fig. 10e; "6 times" for 50 → 400 µm; Conclusions'
  14%/25% f'c loss vs §4.2 values; text reading of Table 6 as "% increases" while Table 6 lists absolute strains;
  §4.1 percentage reductions vs Table 4; recommendation of 0.5 vol.% 6 mm steel (p. 929) although 0.75% was tested;
  Fig. 9b/16b axis "Load (kN)" but values in N.
- Observed: PVA E = 14 GPa (Table 3) is unusually low.

## Relation to other work
- Agrees with: [[zhou2023-hsecc-elevated-temperature]] and [[mohammed2020-cr-ecc-elevated-temperature]] (no spalling of
  PVA-ECC; PVA burns out by 400 °C; steel hybrid helps residual load). Mechtcherine 2012 and Bhat 2014 (as cited
  in [[high-temperature-behaviour]]): ductility rises to ≈ 60–100 °C and is lost by ≈ 150–200 °C.
- Contradicts: ⚔️ (minor) f'c at 400 °C: −10 to −27% here (hot test) vs a rise at 400 °C in
  [[zhou2023-hsecc-elevated-temperature]] (residual, W/B 0.20); hot vs residual, matrix strength differ.
  ⚔️ (minor) Hybrid steel + PVA: no spalling up to 600 °C here vs slight spalling at 800 °C in
  [[zhou2023-hsecc-elevated-temperature]] — temperature ranges differ, so not a direct conflict.
  ⚔️ (minor) PVA "burned" at 200 °C in hot test vs TG melting onset 230 °C ([[zhou2023-hsecc-elevated-temperature]], Fig. 4).
  ⚔️ (minor) [[chai2023-hdc-ambient-temperature]]: PVA-HDC flexural strength rises 20 → 60 °C (residual, 8 h) vs
  falling bending peak load at 60 °C here (hot).
- Extends: is the primary source of the "4× debris" claim cited in [[high-temperature-behaviour]]; adds a
  PVA + steel hybrid with demonstrated tensile strain hardening to [[hybrid-fiber]].

## Pages updated from this source
- [[high-temperature-behaviour]]
- [[hybrid-fiber]]
- [[pva-fiber]]
- [[durability]]
- [[crack-width]]
- [[compressive-strength]]
- [[flexural-strength]]
- [[dogbone-uniaxial-tension]]
- [[fiber-matrix-interface]]
- [[fly-ash]]
- [[gaps]]

## To verify
- [ ] Crack widths at 60 / 100 °C: text 400 / 750 µm vs Fig. 10e ≈ 570–770 / 940–1070 µm vs p. 930 "≈ 1 mm".
- [ ] Conclusions' f'c loss "14% and 25%" at 400/600 °C vs §4.2 per-mix values (ECC 10/25%).
- [ ] Table 6 strains (e.g. ECC 12% at 60 °C) are FE inputs; §5.2 text reads them as "% increases" — clarify.
- [ ] PVA modulus 14 GPa (Table 3).
- [ ] "60 °C glass transition, 80% modulus loss" claim — uncited.
- [ ] Dog-bone dimensions read from Fig. 1a; sand "120 mm" read as 120 µm.
- [ ] ECC PVA Vf 2.0% derived from 26 kg/m³ and ρ 1300 kg/m³ (not stated in text).
