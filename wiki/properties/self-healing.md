---
type: property
slug: self-healing
aliases: [autogenous healing, crack healing, recovery]
tags: [durability, cracking]
sources: [ma2021-ecc-durability-review, homma2009-frcc-self-healing, herbert2013-ecc-self-healing-natural-environment, ozbay2013-ecc-self-healing-sustained-load, chai2019-hdcc-freeze-thaw-carbonation-flexure, li2002-pva-ecc-interface-tailoring]
updated: 2026-10-20
---

# Self-Healing (autogenous crack healing)

> Until 2026-10-20 all data here were second-hand via [[ma2021-ecc-durability-review]]. Three primary
> studies are now ingested: [[homma2009-frcc-self-healing]] (FRCC, **not** strain-hardening),
> [[herbert2013-ecc-self-healing-natural-environment]] (ECC, outdoors) and
> [[ozbay2013-ecc-self-healing-sustained-load]] (ECC, sustained load).

## Mechanism (primary)
- **Main product is CaCO₃** (Raman, [[homma2009-frcc-self-healing]], Fig. 12; EDX at 30 d,
  [[ozbay2013-ecc-self-healing-sustained-load]], Fig. 8). C–S–H-like gel bridged < 50 µm cracks at 90 d
  ([[ozbay2013-ecc-self-healing-sustained-load]], Fig. 8).
- **Further hydration is not the main source**: hydration degree ≈ 65% in all three FRCC mixes, yet
  healing differed strongly ([[homma2009-frcc-self-healing]], Fig. 18).
- **Fibres act as nucleation sites**: crystal thickness ranks with fibre count per m³ — steel cord
  (187 × 10⁴) ≈ 20 µm < hybrid (111 × 10⁸) ≈ 65 µm < PE (221 × 10⁸) ≈ 98 µm at 28 d
  ([[homma2009-frcc-self-healing]], Fig. 5, Table 2 ⚠️ read from figure). Smooth crack faces with no fibres
  carry thinner deposits (Fig. 9).
- **Ca²⁺ supply**: high-FA ECC still had 3.55–4.91% CH at 28 d, so calcite could form
  ([[ozbay2013-ecc-self-healing-sustained-load]], Table 5). Outdoors, Ca(OH)₂ may wash out in rain and
  re-form ([[herbert2013-ecc-self-healing-natural-environment]], §3.1.1).
- **Water is required**: no stiffness gain in air at 50% RH ([[ozbay2013-ecc-self-healing-sustained-load]], Fig. 6a).

## Quantitative evidence
### Crack-width thresholds for healing
| Source | Condition | Threshold / finding |
|---|---|---|
| [[homma2009-frcc-self-healing]] (FRCC) | 28 d water, cracked at 7 d | < 100 µm sealed in all fibre systems (crystal ≈ crack width); > 100 µm partial: slope 0.367 (PE) > 0.104 (hybrid) > 0.029 (steel cord) (Fig. 6) |
| [[ozbay2013-ecc-self-healing-sustained-load]] (ECC) | 90 d water | 10–40 µm healed fully; < 30 µm totally closed; > 60 µm only partly (Fig. 7) |
| Reinhardt & Jooss, as cited in [[ma2021-ecc-durability-review]] | permeability | stabilises in 3–4 d for < 60 µm; 7–10 d or more for > 100 µm (p. 3) |
| Heide & Schlangen 2007; Li & Yang 2007, as cited in [[ozbay2013-ecc-self-healing-sustained-load]] | — | below 100 µm, preferably < 50 µm (p. 167) |
| Zhu 2012/2016, as cited in [[chai2019-hdcc-freeze-thaw-carbonation-flexure]] | under F-T | obvious healing for cracks < 43 µm (p. 127) |
| Yıldırım 2018, as cited there | crack < 100 µm, 90 d | healing rate 80% in water, 40% in CO₂-air (p. 127) |

### Recovery of properties
| Source (term) | Exposure | Recovery |
|---|---|---|
| [[herbert2013-ecc-self-healing-natural-environment]] (HVFA PVA-ECC, FA/C 2.2; residual crack 24 / 30 µm at 0.5 / 1.0% pre-strain) | outdoors, Ann Arbor, 12 months, −11.7 to +32.8 °C | normalised resonant frequency 90–96% after **1 week**, then stable 95–105% for a year (Fig. 4); stiffness 62% at 3 months (0.5% pre-strain), often > 100% after 6 months; first-crack strength ≈80% at 3 months, 116% at 12 months (Fig. 6) |
| same, repeated damage | reloaded 3× | RF after 3rd reloading 88% (0.5%) and 84% (1.0%); stiffness recovery 62→10% (0.5%), 37→3% (1.0%) — repeatable but decaying (Figs. 5, 7) |
| [[ozbay2013-ecc-self-healing-sustained-load]] (PVA-ECC, FA/C 1.2 and 2.2) | 90 d water, unloaded vs 60% sustained flexural load | stiffness 87 vs 76% (ECC-1) and 95 vs 83% (ECC-2) of uncracked (Table 4, ratios computed); MOR and deflection almost fully recovered in 30 d unloaded |
| [[homma2009-frcc-self-healing]] (FRCC) | 28 d water | strength recovery: steel cord ≈ 0 or negative (corrosion); PE 0–100%; hybrid > 100% at residual elongation < 2 mm (Eq. 6, Fig. 15) |
| [[homma2009-frcc-self-healing]] | permeability, 28 d | small cracks return to uncracked k (≈10⁻¹¹ m/s); cracks ≥ ≈370 µm stay nearly constant after 3 d; most deposition in first 3 d (Figs. 5, 10) |

- Recovery > 100% includes bulk hydration; healed specimens never exceeded uncracked controls of equal
  exposure ([[herbert2013-ecc-self-healing-natural-environment]], §3.2.1).
- Outdoor healing tracks mean temperature more closely than precipitation; recovery lowest after
  autumn–winter exposure (Figs. 7–8). → [[freeze-thaw]]

### Second-hand (as cited in [[ma2021-ecc-durability-review]])
- **Wet–dry cycles:** relative water permeability fell to 0 after 10 cycles (Ma 2014, p. 3).
- **Freeze–thaw with pre-strain** (Zhu 2012, p. 5):

  | Pre-strain | Recovery |
  |---|---|
  | 0.5–1% | about 100% |
  | 1.5–2% | limited |
  | > 2.5% | not obvious |

- A 2% pre-strained ECC recovered its stiffness fully after 50 salt-frost cycles (Sahmaran & Li 2007, p. 5).
- Healing is faster in sulfate solution (Liu 2017, p. 5).
- Healing of low pre-damage improves later fatigue life (Qiu 2018, p. 9). → [[fatigue]]
- **Ageing reduces healing.** Self-healing and ductility both decline with age because of the
  long-term pozzolanic reaction (p. 9).

## Influencing factors / relationships
- **Crack width under load, not residual width**: sustained load roughly doubles average crack width
  (ECC-1 ≈115 vs 60 µm; ECC-2 ≈85 vs 40 µm) and cuts healing; unloaded tests may overestimate in-service
  healing ([[ozbay2013-ecc-self-healing-sustained-load]], Table 3, Conclusions). → [[crack-width]]
- **Fly ash**: FA/C 2.2 gives more, narrower cracks and better healing than 1.2
  ([[ozbay2013-ecc-self-healing-sustained-load]], Table 3; [[herbert2013-ecc-self-healing-natural-environment]], §2.1). → [[fly-ash]]
- **Fibre count / fineness**: more, finer fibres → thicker deposits ([[homma2009-frcc-self-healing]]). → [[pe-fiber]]
- **Exposure**: continuous water > wet–dry > CO₂-air > dry air. Under coupled F-T + carbonation + 60 °C
  drying, 20–30 µm cracks in Eco-HDCC **widened** instead of healing
  ([[chai2019-hdcc-freeze-thaw-carbonation-flexure]], §3.1).
- **Steel fibres** corrode on crack faces and can give negative recovery ([[homma2009-frcc-self-healing]], Fig. 16). → [[hybrid-fiber]], [[chloride-and-corrosion]]

> Synthesis (revised 2026-10-20): the earlier wiki statement "PE-based HSHDC (80–200 µm cracks) heals
> poorly" should be read as a **crack-width** problem, not a PE problem: at equal width, fine PE fibres
> *promote* CaCO₃ deposition, and cracks up to about 100 µm seal in 28 d of water
> ([[homma2009-frcc-self-healing]], FRCC not strain-hardening). The practical limits for ECC/HDC are
> (1) the crack width **under service load** (about 2× residual), (2) the availability of water, and
> (3) exposure that dries or carbonates the crack. PVA-ECC reaches 24–60 µm residual widths
> ([[herbert2013-ecc-self-healing-natural-environment]]; [[li2002-pva-ecc-interface-tailoring]] 43–88 µm), so
> it heals well in wet conditions; PE-HSHDC widths remain above the < 60 µm fast-healing range. → [[gaps]]

## Conflicts & open questions
- ⚔️ (refinement) Healing under F-T: ≈100% recovery at 0.5–1% pre-strain (Zhu 2012, as cited in
  [[ma2021-ecc-durability-review]]) vs 20–30 µm cracks widening under F-T + carbonation + 60 °C drying
  ([[chai2019-hdcc-freeze-thaw-carbonation-flexure]]). Different exposure. → [[gaps]]
- Refinement: "self-healing declines with age" ([[ma2021-ecc-durability-review]], p. 9) vs recovery rising over
  12 months outdoors ([[herbert2013-ecc-self-healing-natural-environment]]) — but the latter cracked at 7 d.
- Note: the "Özbay 2013" cited in [[ma2021-ecc-durability-review]] for slag-ECC frost resistance is a
  different paper, not [[ozbay2013-ecc-self-healing-sustained-load]].
- Open: 100% recovery after repeated damage; healing of cracks made at late age; healing in HSHDC/UHDC.

## Related
- [[crack-width]] · [[durability]] · [[permeability]] · [[freeze-thaw]] · [[carbonation]] · [[chloride-and-corrosion]] · [[fly-ash]] · [[pe-fiber]]
