---
type: property
slug: freeze-thaw
aliases: [frost resistance, frost damage, freeze-thaw cycles, salt scaling, F-T]
tags: [durability, freeze-thaw]
sources: [zhong2019-ecc-freeze-thaw, wang2023-ecc-frost-damage, chai2019-hdcc-freeze-thaw-carbonation-flexure, vanzijl2010-shcc-durability, ma2021-ecc-durability-review, he2024-hdc-research-advances, herbert2013-ecc-self-healing-natural-environment, mechtcherine2011-shcc-high-strain-rate]
updated: 2026-10-20
---

# Freeze–Thaw Resistance

Part of the [[durability]] hub. Related: [[carbonation]] (coupled exposure), [[self-healing]], [[permeability]].

## Definition
Resistance to repeated freezing and thawing of pore water, measured by relative dynamic modulus (RDEM),
mass loss / scaling, and residual mechanical properties after cycling. Standard rapid tests in the
wiki: ASTM C666 (procedure A, in water), GB/T 50082 (China), ASTM C672 and RILEM CDF (de-icing salt scaling).

## Key points
- **ECC/SHCC/HDCC far outlast plain concrete and fibre-free mortar in rapid F-T tests**, in every primary
  study in the wiki (table below). No primary study reports early failure of a PVA-ECC.
- **Damage is a process, not an end state**: two statistically detected "leaps" precede final failure,
  IF (micro-crack initiation) and PF (macro-crack network); stages stable → unstable → yield
  ([[zhong2019-ecc-freeze-thaw]], §3.3–3.4, Mann–Kendall test).
- **Fibres change the failure mode**: fibre-free mortar scaled at IF; PVA mixes did not scale until PF
  ([[zhong2019-ecc-freeze-thaw]], Figs. 12–13). Proposed mechanism: microcracks relieve ice-expansion stress
  and fibres bridge them (as cited in [[ma2021-ecc-durability-review]], p. 4).
- **Fibre–matrix bond is the weak link after F-T**: F-T is said to lower PVA–matrix bond, giving more
  pull-out and fewer fibre ruptures ([[wang2023-ecc-frost-damage]], §3.2, inferred, not measured) and to
  scratch PVA fibre surfaces ([[chai2019-hdcc-freeze-thaw-carbonation-flexure]], p. 132–133, citing Chai & Xu 2018).
  → [[fiber-matrix-interface]]
- **Salt scaling is the exception**: by RILEM CDF, SHCC scaled 2.2 kg/m² after 28 cycles, above the
  1.5 kg/m² limit, i.e. "insufficient" by this method; by ASTM C672 SHCC (FA/C up to 2.2, also pre-cracked)
  was acceptable after 50 cycles (both in [[vanzijl2010-shcc-durability]], p. 267).
- **No primary tensile data after F-T**: all primary studies here measure flexure, RDEM, mass or bond.
  The claim that PVA-ECC loses ε_tu after F-T remains second-hand only (see below).

## Quantitative evidence: primary studies
| Source (term) | Protocol | Plain reference | Fibre composite | Note |
|---|---|---|---|---|
| [[zhong2019-ecc-freeze-thaw]] (ECC, PVA 13 mm; Taguchi L25) | GB/T 50082 / ASTM C666 in water, 100×100×400 prisms, to final failure | fibre-free mixes: IF/PF/UF = 25/50/75 cycles | best L25 mix 225/350/475; optimum (FA 35%, S/B 0.5, W/B 0.25, PVA 1.5 vol.%) measured 225/375/500 cycles | Table 4, Table 9; no tension test, SH not shown |
| [[wang2023-ecc-frost-damage]] (ECC, PVA 8 mm, 2 vol.%, FA/C 1.18, W/B 0.33; σ_tu 4.21 MPa, ε 5.24% at 28 d) | GB/T 50082, −18 to +5 °C, 300 cycles | W/C 0.5 concrete failed (RDEM 60%) at 42 cycles; ECC matrix at 84 | RDEM > 95%, mass loss < 2% after 300 cycles; 4-pt bending 18.6 → 16.6 MPa (−11%) | §3.1–3.2, Figs. 5–7 |
| [[chai2019-hdcc-freeze-thaw-carbonation-flexure]] (Eco-HDCC, domestic PVA 12 mm, FA/C 1.50, W/B 0.30) | coupled: 1 cycle = 4 d water + 10 F-T (+4/−18 °C) + 2 d at 60 °C + 9.7 h at 20% CO₂; 15 cycles (= 150 F-T) | not tested | flexural strength −19 to −33%, ultimate deflection −24 to −50% after 15 cycles; deflection hardening kept but shortened | Table 4, Figs. 6–7; age confounded (0 cycles ≈ 28 d, 15 cycles ≈ 148 d) |

Rebar bond after F-T ([[wang2023-ecc-frost-damage]], Tables 6–7): rebar–ECC 18.22 → 16.14 MPa after 300
cycles (pull-out failure); rebar–concrete 14.38 → 6.51 MPa after 50 cycles (splitting). ⚠️ The text gives
ECC bond losses of −19.1% / −24.5%, Table 7 gives −5.0% / −11.4% (internal inconsistency). → [[interface-bond]]

## Quantitative evidence: second-hand (as cited)
Moved here from [[durability]] (2026-10-20), unchanged:
- Durability factor > 100 for ECC vs **20** for non-air-entrained concrete (Li 2008, as cited in
  [[ma2021-ecc-durability-review]], p. 4).
- ASTM C666A: concrete removed at 110 cycles; SHCC survived 300 cycles with no loss of dynamic modulus,
  durability factor 100 vs **10**; ε_tu about 3% retained (Li et al. 2003, as cited in
  [[vanzijl2010-shcc-durability]], p. 267). ⚔️ see Conflicts.
- Fibre-free mortar failed at 210 cycles (10.7% mass loss); 2% PVA-ECC survived 300 cycles with 8% mass
  loss (Sahmaran 2012, as cited in [[ma2021-ecc-durability-review]], p. 4).
- PVA-ECC loses more ε than PE-ECC after 200 cycles (Yun 2011, as cited, p. 4).
- Hybrid PVA+PE SHCC loses more ε_tu than σ_tu (Yun 2013, as cited in [[he2024-hdc-research-advances]], p. 13).
- With de-icing salt, ECC keeps ε > 3% after 50 cycles (Sahmaran & Li 2007, as cited in
  [[ma2021-ecc-durability-review]], p. 5).
- Silica fume and slag improve frost resistance of high-volume FA ECC (Liu 2018; Özbay 2013, as cited
  in [[ma2021-ecc-durability-review]]). Note: this "Özbay 2013" is an ACI Mater. J. paper, **not**
  [[ozbay2013-ecc-self-healing-sustained-load]].
- Single F-T (Chai & Fei 2018, as cited in [[chai2019-hdcc-freeze-thaw-carbonation-flexure]]): HDCC
  deflection rose over 0–150 cycles and fell over 200–300; under coupled F-T + carbonation it fell monotonically.

## Influencing factors / relationships
- **W/B** is the largest factor for ultimate F-T failure (38.47% of variance), then V_PVA (32.70%) and FA
  (21.63%); S/B insignificant. All indices fall as W/B rises 0.25 → 0.50 ([[zhong2019-ecc-freeze-thaw]],
  Table 8, Fig. 16). → [[water-binder-ratio]]
- **PVA content**: 0.5–2.0 vol.% delays all failure indices, with a slight drop at 2.0% blamed on poor
  dispersion; V_PVA explains 39.02% (IF) and 48.60% (PF) of variance ([[zhong2019-ecc-freeze-thaw]],
  §3.5, Tables 6–7). → [[pva-fiber]], [[fiber-dispersion]]
- **Fly ash**: ground FA up to 35% of binder is best; PF/UF rise again at 52.5% and fall at 70% (too little
  CH) ([[zhong2019-ecc-freeze-thaw]], §3.5). The paper notes that other studies found FA can hinder frost
  resistance; fineness may explain the difference. → [[fly-ash]]
- **Pre-cracking** (preload 0.5–0.7 of peak) widens cracks to 20–30 µm and increases the flexural loss
  under coupled exposure; preload ≤ 0.3 differs little from unloaded ([[chai2019-hdcc-freeze-thaw-carbonation-flexure]], Table 4, §3.4).
- **Pore structure**: harmless pores (< 20 nm) vanish and 50–200 nm and > 200 nm pores grow with coupled
  cycles ([[chai2019-hdcc-freeze-thaw-carbonation-flexure]], Fig. 5); freezable water η jumps at IF and PF
  ([[zhong2019-ecc-freeze-thaw]], Figs. 10–11).
- **Transport after F-T**: capillary coefficient, chloride and carbonation rise with cycles, less in ECC than
  in the matrix ([[wang2023-ecc-frost-damage]], §3.3–3.5). → [[permeability]], [[carbonation]], [[chloride-and-corrosion]]
- **SAP** is used in one SHCC partly to improve frost resistance ([[mechtcherine2011-shcc-high-strain-rate]], p. 52); not tested there.
- **Self-healing under natural frost**: outdoor PVA-ECC (winter to −11.7 °C) kept healing, though recovery
  was lowest after autumn–winter exposure ([[herbert2013-ecc-self-healing-natural-environment]], Figs. 7–8). → [[self-healing]]

> Synthesis: three independent primary studies (HIT, Qingdao, Southeast University) agree that PVA-ECC/HDCC
> survives 300+ rapid F-T cycles where plain concrete fails at 40–110 cycles. What is still missing is
> **tensile** evidence: no primary study measures ε_tu or crack width in uniaxial tension after F-T, so the
> key HDC property (strain hardening) after frost is known only second-hand (Yun 2011; Li 2003 as cited).
> Coupled exposures (F-T + carbonation + drying) are more damaging than F-T alone.

## Conflicts & open questions
- ⚔️ **Durability factor of non-air-entrained concrete**: 20 (Li 2008, as cited in [[ma2021-ecc-durability-review]], p. 4)
  vs 10 (Li et al. 2003, as cited in [[vanzijl2010-shcc-durability]], p. 267). ECC/SHCC = 100 in both;
  concrete removed at 110 cycles in both. Probably the same underlying test reported differently. → [[gaps]]
- ⚔️ (minor) Effect of F-T on HDCC deflection: rises up to 150 cycles (single F-T, Chai & Fei 2018 as cited) vs
  falls monotonically (coupled exposure, [[chai2019-hdcc-freeze-thaw-carbonation-flexure]]); [[wang2023-ecc-frost-damage]]
  reports larger mid-span deflection after 300 cycles. Exposure-type dependent.
- Open: ε_tu and crack width in direct tension after F-T; F-T of PE-based HSHDC; salt scaling (CDF fails).
- ⚠️ Zhong 2019 prints the F-T temperatures inverted ("highest −18 °C, lowest 4 °C"); UF criterion undefined.

## Related
- [[durability]] · [[carbonation]] · [[chloride-and-corrosion]] · [[permeability]] · [[self-healing]] · [[flexural-strength]] · [[pva-fiber]] · [[fly-ash]] · [[gaps]]
