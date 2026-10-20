---
type: source
slug: wang2023-ecc-frost-damage
title: "Influence of Frost Damage on Performance of Engineered Cementitious Composites"
authors: [Lanqin Wang, Xiaofeng Han, Li Tian, Penggang Wang, Xiaoguang Sun]
year: 2023   # J. Adv. Concr. Technol. vol. 21 (Dec 2023); received 4 Sep 2023, accepted 16 Nov 2023 (p. 971)
venue: "Journal of Advanced Concrete Technology (Japan Concrete Institute) 21, 971–982, December 2023. Shandong Jianzhu University; Qingdao University of Technology (corresponding author P. Wang); Shandong Chambroad Ecofriendly Materials Co."
doi: "10.3151/jact.21.971"
raw_file: raw/papers/Wang2023_ECC-frost-damage.pdf
material_term: "ECC (engineered cementitious composites; SHCC also named in the introduction). PVA-ECC with 28-d tensile strength 4.21 MPa and ultimate tensile strain 5.24% (Table 4; tension test method not described). Comparison: the same mix without fiber ('matrix', also called 'mortar') and a W/C 0.5 normal concrete."
study_type: "experimental (rapid freeze–thaw GB/T 50082-2009; RDEM, mass loss; four-point bending; capillary absorption; chloride profile; accelerated carbonation; rebar pull-out bond)"
tags: [ecc, pva-fiber, fly-ash, durability, freeze-thaw, capillary-absorption, chloride, carbonation, rebar-bond, pull-out, flexural-strength, qingdao-university-of-technology]
ingested: 2026-10-20
updated: 2026-10-20
---

# Frost damage and ECC performance (Wang et al., 2023)

## One-paragraph summary
A Shandong / Qingdao study exposed one PVA-ECC mix (C 550, FA 650, W/B 0.33, PVA 26 kg/m³ ≈ 2.0 vol.%;
f'c 46.8 MPa, σ_tu 4.21 MPa, ε_tu 5.24%; Tables 1, 4), its fiber-free matrix and a W/C 0.5 concrete
(f'c 42.92 MPa) to rapid freeze–thaw (GB/T 50082-2009) and then measured relative dynamic elastic
modulus (RDEM), mass loss, four-point bending, capillary absorption, chloride ingress (3% NaCl, 14 d),
accelerated carbonation (20% CO₂) and rebar pull-out bond. Failure (RDEM 60%) came at **42 cycles for
concrete and 84 for the matrix**, while ECC kept **RDEM > 95% and mass loss < 2% after 300 cycles**
(§3.1, Figs. 5–6). ECC bending strength fell from **18.6 to 16.6 MPa** after 300 cycles while mid-span
deflection rose (§3.2, Fig. 7). The initial capillary coefficient A_i rose only 1.14× after 200 cycles in
ECC vs 1.26× after 75 cycles in the matrix (§3.3). Chloride and carbonation rose less in ECC than in the
matrix (Figs. 13–16). Rebar–ECC bond fell from **18.22 to 16.14 MPa** after 300 cycles with pull-out
failure, while rebar–concrete bond fell from 14.38 to 6.51 MPa after only 50 cycles with splitting
(Tables 6–7). The authors conclude frost damage has little effect on ECC durability.

## Objective / research question
- Does ECC performance change markedly under freeze–thaw, including its transport properties and its
  bond to steel bars, which are less studied (§1)? Motivation: cold high-latitude regions (§1).

## Materials & mix design
- PO 42.5 cement; Class F fly ash (oxides in Table 2); sand max 0.3 mm; Kuraray PVA (Table 3).
- Concrete: W/C 0.5, coarse aggregate max 20 mm, river sand max 5 mm (§2.1).

| Mix ID | Cement | Fly ash | Slag/other | Sand (type, max size) | W/B | SP | Fiber type | L (mm) | d (µm) | Vf (vol.%) |
|---|---|---|---|---|---|---|---|---|---|---|
| ECC | 550 | 650 | none | sand 550, 0.3 mm | 0.33 (water 395) | not reported | PVA (Kuraray; 1600 MPa, 42 GPa, 7%) | 8 | 39 | 26 kg/m³ → **2.0** (converted here with ρ = 1.3 g/cm³, Table 3) |
| Matrix | 550 | 650 | none | sand 550, 0.3 mm | 0.33 | not reported | none | n/a | n/a | 0 |
| Concrete | 320 | none | none | river sand 653 (5 mm) + aggregate 1267 (20 mm) | 0.5 (W/C) | not reported | none | n/a | n/a | 0 |

Units of binder quantities: kg/m³ (Table 1). FA/C = 650/550 = 1.18 by mass (computed here).

## Test methods
- Specimen geometry: F-T prisms 100 × 100 × 400 mm; bending prisms 40 × 40 × 160 mm; 100 mm cubes cut in
  half for absorption, chloride and carbonation; central pull-out with HRB335 Ø12 mm bar, bond length 7d
  (84 mm), unbonded 50 mm (free end) and 30 mm (loaded end) (§2.2–2.6, Fig. 3, Table 5).
- Freeze–thaw: GB/T 50082-2009 rapid method (~3 h cycle: ~2 h freeze, ~1 h thaw), specimen-centre
  temperature −18 ± 2 °C to 5 ± 2 °C (printed "5±22°C" ⚠️); stop at RDEM 60% or mass loss > 5% (§2.2).
- Loading / rate: four-point bending 0.3 mm/min with extensometers each side, after 0/100/200/300 cycles
  and natural drying (§2.3); pull-out 0.5 mm/min, free-end slip by extensometer (§2.6). Bending span not reported.
- Transport: capillary suction 14 d (sealed sides, 5 ± 1 mm water), fitted W = a(1 − exp(−b√t)) (Eqs. 3–7);
  chloride 3% NaCl 14 d, layer milling + titration; carbonation 20 ± 3 °C, RH 70 ± 5%, CO₂ 20 ± 3%,
  x = k√t (Eq. 8) (§2.4–2.5, §3.3–3.5).
- Measurement: transverse frequency (RDEM, Eq. 1); mass (Eq. 2); extensometers.
- Curing & test age: 1 d in mould, 23 d at 20 °C / RH > 95%, 4 d in water → F-T start at 28 d (§2.1).
  f'c and tension at 28 d (Table 4). Direct tension test setup not described.
→ [[durability]] · [[flexural-strength]] · [[permeability]]

## Key results
| Mix ID | f'c (MPa) | First-crack stress (MPa) | Tensile strength (MPa) | Tensile strain capacity (%) | Crack width (µm) | Other |
|---|---|---|---|---|---|---|
| ECC, 0 cycles (28 d) | 46.8 | not reported | 4.21 | 5.24 ("ultimate tensile strain") | not reported | bending 18.6 MPa (§3.2); bond τu 18.22 MPa, slip 0.665 mm (Table 7) |
| ECC, 100 cycles | not reported | not reported | not reported | not reported | not reported | bond 17.30 MPa, slip 0.569 mm, pull-out (Table 7) |
| ECC, 300 cycles | not reported | not reported | not reported | not reported | not reported | bending 16.6 MPa; RDEM > 95% (4% loss); mass loss < 2%; bond 16.14 MPa, slip 0.387 mm (§3.1–3.2, Table 7, Concl. 1) |
| Matrix | not reported | not reported | not reported | not reported | not reported | RDEM 55.1% at 100 cycles; 40% loss at 84 cycles (§3.1) |
| Normal concrete | 42.92 | not reported | 2.98 | 0.01 | not reported | RDEM 45.2% at 50 cycles; 40% loss at 42 cycles (§3.1); bond 14.38 → 9.03 → 6.51 MPa at 0/25/50 cycles, split (Table 6) |

Main findings (with Table/Fig. location):
- Bending stress–deflection curves show multiple-cracking fluctuations; deflection at peak 3–3.5 mm and
  rising with cycles (§3.2, Fig. 7).
- A_i: ECC rises linearly with cycles (fit printed "y = 805.96 − 0.89x", R² 0.9261, Fig. 12 ⚠️ sign); ECC
  1.14× after 200 cycles; matrix 1.26× after 75 cycles (§3.3).
- Chloride surface content (read from Figs. 13–14 ≈): ECC ~0.5% (0 cycles) → ~0.7% (300 cycles); matrix
  ~0.65% (0) → ~0.9% (75) ⚠️ read from figure.
- Carbonation: ECC unaffected below 100 cycles; matrix affected from 50 cycles (§3.5, Fig. 15). Carbonation
  coefficient ECC ≈2.6 → ≈3.1 mm/d^0.5 over 0 → 300 cycles (linear); matrix ≈2.4 → ≈3.55 over 0 → 75
  (Fig. 16, read ⚠️). 28-d carbonation depth ≈13 mm (ECC, 0 cycles) and ≈15 mm (300 cycles) (Fig. 15a, read ⚠️).
- Rebar–concrete bond: −37.2% (25 cycles), −54.7% (50 cycles); peak slip +26.3% / +83.5%; τu = −0.16N + 13.91
  (R² 0.9589, Fig. 20; printed "1391") (§3.6, Table 6).
- Rebar–ECC bond: text says −19.1% (100) and −24.5% (300), but Table 7 gives −5.0% and −11.4%
  (computed here) ⚠️ internal inconsistency. Peak slip decreases with cycles (Table 7).
- ECC pull-out specimens shed only surface paste and fiber "fluff" after 300 cycles (Fig. 17).

## Mechanisms / explanations offered by authors
- Fibers introduce microbubbles that relieve freezing pressure; dispersed fibers spread F-T stress; fiber
  bridging reduces surface peeling (§3.1, citing Li 2019).
- F-T lowers PVA–matrix bond, so more fibers pull out instead of rupturing: bending strength falls but
  deflection ("toughness") rises (§3.2). ⚠️ inferred, interface not measured.
- F-T enlarges pores → higher capillary suction, chloride and carbonation; PVA bridging limits micro-cracking (§3.3–3.5).
- In concrete, F-T micro-cracks concentrate stress at the bar → splitting; ECC's tensile capacity and fiber
  load transfer give ductile pull-out (§3.6, Concl. 4).

## Limitations (stated + observed)
- Stated: none explicitly.
- Observed: single ECC mix; no tension, crack width or f'c after F-T (only bending), so the effect of F-T on
  ε_tu is not measured; the tension test for Table 4 is not described.
- Observed: F-T of matrix and concrete stopped early (failure), so comparisons at equal cycles are limited.
- Observed: text–table mismatch on ECC bond loss; Fig. 12 fit sign and x-axis label ("contact time") wrong;
  Fig. 20 equation garbled; Fig. 7 legend labels overlap; temperature "5±22°C".
- Observed: specimen counts and scatter not reported; SP not reported.
- Observed: ECC carbonation depths (~13 mm at 28 d in 20% CO₂) are large for a W/B 0.33 high-FA mix.

## Relation to other work
- Agrees with: ECC durable under F-T where plain matrix/concrete fail (Sahmaran 2012; Li 2008, as cited in
  [[ma2021-ecc-durability-review]], p. 4); PVA mixes outlasting plain mixes in [[zhong2019-ecc-freeze-thaw]].
- Contradicts: ⚔️ carbonation depth ≈13 mm after 28 d at 20% CO₂ here vs ≈0.8 mm for PP+PVA ECC at 20 ± 3%
  CO₂ (Zhang W. 2018, as cited in [[ma2021-ecc-durability-review]], p. 9). Different mixes/conditioning;
  flag for check.
- Extends: first wiki data on rebar–ECC bond after F-T and on transport properties (absorption,
  chloride, carbonation) after F-T. → [[durability]], [[permeability]]

## Pages updated from this source
- [[durability]] · [[permeability]] · [[flexural-strength]] · [[pva-fiber]] · [[fly-ash]] · [[tensile-strain-capacity]] · [[mix-designs]] · [[mechanical-results]]

## To verify
- [ ] ECC bond loss: text −19.1% / −24.5% vs Table 7 values (−5.0% / −11.4% computed).
- [ ] Fig. 12 fit "y = 805.96 − 0.89x" although A_i rises (probably +0.89x); x-axis mislabelled.
- [ ] Fig. 20 fit printed "τu = −0.16N + 1391" (probably 13.91).
- [ ] F-T upper temperature printed "5±22°C" (probably 5 ± 2 °C).
- [ ] Tensile test method and specimen for Table 4 (σ_tu 4.21 MPa, ε 5.24%) not described; "ultimate" vs at-peak strain.
- [ ] Values read from Figs. 13–16 (chloride, carbonation) are approximate.
- [ ] Vf 2.0 vol.% computed from 26 kg/m³ and ρ = 1.3 g/cm³.
- [ ] Carbonation depth ≈13 mm at 28 d (Fig. 15a) vs 0.8 mm in Zhang W. 2018 (as cited by Ma 2021).
