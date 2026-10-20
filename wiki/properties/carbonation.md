---
type: property
slug: carbonation
aliases: [accelerated carbonation, carbonation depth, CO2 ingress]
tags: [durability, carbonation, transport]
sources: [zhang2022-ecc-carbonation-sustained-load, wang2023-ecc-frost-damage, chai2019-hdcc-freeze-thaw-carbonation-flexure, ma2021-ecc-durability-review, kunieda2006-hpfrcc-japan-applications, kunieda2010-uhp-shcc-steel-reinforcement]
updated: 2026-10-20
---

# Carbonation

Part of the [[durability]] hub. Related: [[freeze-thaw]] (coupled exposure), [[permeability]], [[chloride-and-corrosion]].

## Definition
Reaction of atmospheric CO₂ with Ca(OH)₂ and C-S-H, which lowers pore-solution pH and can depassivate
reinforcement. Measured in the wiki sources by the phenolphthalein front after accelerated exposure at
about 20% CO₂ (GB/T 50082 conditions: 20 ± 3 °C, 70 ± 5% RH, 20 ± 3% CO₂).

## Key points
- **High-FA ECC carbonates faster than its strength suggests**: FA/C ≈ 1.2 lowers portlandite, which the
  authors expected to worsen carbonation ([[zhang2022-ecc-carbonation-sustained-load]], §1). Both primary
  studies use FA/C 1.18–1.20 PVA-ECC.
- **Sustained flexural stress accelerates carbonation, even below first cracking**: δ_T = 0.075 nearly
  doubles 7-d depth (+94%) and adds +41% at 28 d ([[zhang2022-ecc-carbonation-sustained-load]], §3.1, Table 4).
- **The stress effect fades with time** (pores fill with CaCO₃): K_ks at δ_T 0.6 falls from 3.135 (7 d) to
  2.075 (28 d) ([[zhang2022-ecc-carbonation-sustained-load]], Table 4).
- **K_ks rises sub-linearly with δ_T** in ECC (fibre bridging limits load-induced pore growth), unlike the
  linear law for plain concrete ([[zhang2022-ecc-carbonation-sustained-load]], §3.2, Fig. 4).
- **Carbonation densifies ECC**: 0.1–10 µm porosity fell more than 2×; zone-I porosity 8.70% (carbonated)
  vs 11.57% (uncarbonated); microhardness > 100 HV in the carbonated skin vs 60–80 HV inside
  ([[zhang2022-ecc-carbonation-sustained-load]], §3.4–3.5). Carbonation also densifies the HDCC matrix and is
  said to raise fibre bond ([[chai2019-hdcc-freeze-thaw-carbonation-flexure]], p. 127, 131–133).
- **Phenolphthalein under-reads**: TG shows partial carbonation to ≈16 mm vs the ≈10 mm colour front
  ([[zhang2022-ecc-carbonation-sustained-load]], §3.3, Fig. 7).
- **Frost damage and drying accelerate carbonation**: see [[freeze-thaw]] and table below.

## Quantitative evidence
Unloaded vs loaded PVA-ECC (W/B 0.30, FA/C 1.20), 20% CO₂ ([[zhang2022-ecc-carbonation-sustained-load]], Table 4):

| Load level | δ_T | 7 d (mm) | 14 d (mm) | 28 d (mm) | K_ks 28 d |
|---|---|---|---|---|---|
| unloaded | 0 | 2.30 | 3.37 | 4.78 | 1 |
| 0.3 | 0.075 | 4.47 | 5.16 | 6.75 | 1.412 |
| 0.3 | 0.300 | 6.47 | 6.86 | 7.73 | 1.617 |
| 0.6 | 0.300 | 6.50 | 7.32 | 8.82 | 1.845 |
| 0.6 | 0.600 | 7.21 | 8.16 | 9.92 | 2.075 |

Unloaded carbonation rate K_0 ≈ 0.87–0.90 mm/d^0.5 (units inferred ⚠️) (§3.2). Uncracked specimens only;
cracked ECC under load + carbonation was not tested.

Other sources:
| Source (term) | Condition | Value | Note |
|---|---|---|---|
| [[wang2023-ecc-frost-damage]] (ECC, PVA, FA/C 1.18, W/B 0.33) | 20 ± 3% CO₂, 28 d, after 0 / 300 F-T cycles | ≈13 / ≈15 mm; coefficient ≈2.6 → ≈3.1 mm/d^0.5 (linear with cycles); unaffected below 100 cycles; matrix affected from 50 cycles (≈2.4 → ≈3.55 over 0–75) | Figs. 15–16, read from figure ⚠️ |
| [[chai2019-hdcc-freeze-thaw-carbonation-flexure]] (Eco-HDCC, FA/C 1.50) | coupled F-T + 60 °C drying + 9.7 h at 20% CO₂ per cycle, 15 cycles | front 22 mm (preload 0 / 0.3) and 28 mm (preload 0.5 / 0.7); fast over 1–5 cycles, slower 10–15 | Fig. 4; cracks (20–30 µm) add 5–6 mm |
| Zhang W. 2018, as cited in [[ma2021-ecc-durability-review]] (PP + PVA ECC) | 20 ± 3% CO₂ | 0.40 / 0.56 / 0.58 / 0.80 mm at ≈3 / 7 / 14 / 28 d | p. 9, Fig. 18; moved here from [[durability]] |
| Railway viaduct overlay, as cited in [[kunieda2006-hpfrcc-japan-applications]] | accelerated test on sprayed HPFRCC | carbonation "suppressed" | p. 30; no numbers |
| JSCE 2004, as cited in [[kunieda2010-uhp-shcc-steel-reinforcement]] | SHCC cracks < 40 µm | resist water / CO₂ / O₂ ingress | §1; no data |

- The review claim "ECC carbonation resistance much better than plain concrete" rests on references about
  ordinary concrete ([[ma2021-ecc-durability-review]], p. 9 ⚠️). Neither primary study includes a
  plain-concrete control under the same exposure.

## Influencing factors / relationships
- Sustained stress level δ_T and exposure time (above). → [[crack-width]]
- Pre-cracking: preload ≥ 0.5 adds 5–6 mm at 15 coupled cycles ([[chai2019-hdcc-freeze-thaw-carbonation-flexure]], Fig. 4b).
- Prior frost damage: linear increase of the carbonation coefficient with F-T cycles ([[wang2023-ecc-frost-damage]], Fig. 16).
- Fly ash content (lower CH) ([[zhang2022-ecc-carbonation-sustained-load]], §1). → [[fly-ash]]

> Synthesis: carbonation is a real weakness of high-FA PVA-ECC rather than a strength. Two primary 28-d
> values at ~20% CO₂ (4.8 and ≈13 mm) are 6–16× the second-hand 0.8 mm that the wiki previously quoted.
> Carbonation also *densifies* the skin, so its net effect on fibre bridging may be mixed. For HDC used as
> a cover or overlay over steel, carbonation depth vs cover (often 15–35 mm) is an open design question.

## Conflicts & open questions
- ⚔️ **Carbonation depth of unloaded ECC after 28 d at ~20% CO₂**: 4.78 mm ([[zhang2022-ecc-carbonation-sustained-load]], Table 4)
  vs ≈13 mm ([[wang2023-ecc-frost-damage]], Fig. 15a, read ⚠️) vs ≈0.8 mm (Zhang W. 2018, as cited in
  [[ma2021-ecc-durability-review]], p. 9). The two primary mixes are almost identical (PVA, FA/C 1.18–1.20,
  W/B 0.30–0.33, GB/T 50082), yet differ ≈2.7×. Possible reasons: preconditioning (drying), specimen size,
  curing age, reading from figure; the 0.8 mm mix contains PP fibre. Not averaged. → [[gaps]]
- Open: carbonation of cracked ECC under sustained load; carbonation-induced corrosion in R/ECC; PE-based HSHDC.
- ⚠️ Zhang 2022 Eq. (7) does not reproduce its own Table 4 K_ks values.

## Related
- [[durability]] · [[freeze-thaw]] · [[chloride-and-corrosion]] · [[permeability]] · [[crack-width]] · [[fly-ash]] · [[gaps]]
