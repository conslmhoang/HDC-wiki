---
type: concept
slug: heat-curing
aliases: [curing regime, elevated temperature curing, standard curing, ambient curing]
tags: [curing, processing]
sources: [ranade2017-hshdc-impact-resistance, ranade2015-hshdc-tensile-rate-effects, su2023-rubber-modified-hshdc, yang2024-hshdc-uniaxial-tension, ye2021-uhdc-flexural-size-effect, zhang2022-hshdcc-review, yuan2020-nshsdc-beam-strengthening, lee2021-hsdc-wall-emi-impact, kunieda2010-uhp-shcc-steel-reinforcement, sui2018-uhp-ecc-flexural-fatigue, mechtcherine2011-shcc-high-strain-rate, zhao2022-ecc-tension-damage-model, gao2020-hdcc-recycled-fine-aggregate, chai2019-hdcc-freeze-thaw-carbonation-flexure, kanda2003-sprayed-ecc, bu2022-ecc-chloride-crack-width, herbert2013-ecc-self-healing-natural-environment, deng2015-hdc-compressive-toughness, deng2018-hdc-compressive-constitutive, sun2019-modified-pva-fiber-ecc, shumuye2022-slag-fa-pe-ecc, jin2019-hvfa-shcc-structural, vanzijl2010-shcc-durability, chavesfigueiredo2020-printed-shcc, yang2009-ecc-self-healing-wet-dry, choi2016-pe-alkali-activated-slag-composite]
updated: 2026-10-21
---

# Curing Regimes (heat vs ambient)

## Quantitative evidence
| Source | Material | Regime | Test age |
|---|---|---|---|
| [[ranade2017-hshdc-impact-resistance]], p. 27 | Michigan HSHDC, Cor-Tuf | demould at 2 d → 7 d water at room temperature → **5 d water at 90 °C → 3 d air at 90 °C** → air | not stated (the regime ends about 17 d) |
| [[ranade2015-hshdc-tensile-rate-effects]] | Michigan HSHDC | same regime (as cited) | not stated |
| [[su2023-rubber-modified-hshdc]], p. 3 | GDUT R-HSHDC | 24 h under film → 28 d water, room temperature | 28 d |
| [[yang2024-hshdc-uniaxial-tension]], p. 4 | Xi'an HSHDC | standard 20 ± 2 °C, 95% RH | 28 d (60 d for f'c) |
| [[ye2021-uhdc-flexural-size-effect]] | Tongji UHDC | air-cured 1 d, then 27 d (conditions not reported) | 28 d |

## Key points
- **Heat curing is not required for HSHDC-level performance.** GDUT reaches about 157 MPa and
  3.8%, and Xi'an reaches up to 6.48% strain, both at ambient temperature.
- Heat curing limits cast-in-place use. He et al. note that on-site HDC quality is hard to
  guarantee and propose factory production ([[he2024-hdc-research-advances]], p. 20).

## Review view ([[zhang2022-hshdcc-review]])
- Heat curing is a strength lever: the record is 210 MPa after 9 d in 90 °C water (Huang 2021,
  as cited, p. 8). Most compiled HSHDCC are ambient-cured.
- The effect of curing regime on the PSH indices and ductility is **unclear** (outlook, p. 17). → [[gaps]]


## Round 4 evidence (2026-10-20)
| Source | Material | Regime | Note |
|---|---|---|---|
| [[yuan2020-nshsdc-beam-strengthening]] Table 2; [[lee2021-hsdc-wall-emi-impact]] | NSHSDC / HSDC (steel + PE hybrid) | room-cured, 20 °C, 60% RH | f'c 123.4 / 122.3 MPa without heat treatment; authors cite heat curing as a drawback of UHPC jackets (§1) |
| [[kunieda2010-uhp-shcc-steel-reinforcement]] | UHP-SHCC (PE) | wet towels, 4 weeks | f'c 95 MPa, W/B 0.20 |
| [[sui2018-uhp-ecc-flexural-fatigue]] | UHP-ECC (PE) | 20 °C / 95% RH, 90 d | 120 MPa class |
| [[mechtcherine2011-shcc-high-strain-rate]] | SHCC (PVA) | sealed, room temperature | with SAP |
| [[zhao2022-ecc-tension-damage-model]] | ECC (PVA) | saturated lime water, 28 d | test ≥ 35 d ⚠️ |
| [[gao2020-hdcc-recycled-fine-aggregate]] | HDCC (PVA) | water, 28 d | |
| [[chai2019-hdcc-freeze-thaw-carbonation-flexure]] | Eco-HDCC | standard curing, 28 d | exposure age confounded with curing age (p. 132) |
| [[kanda2003-sprayed-ecc]] | sprayed ECC | 20 °C, 28 d | |
| [[bu2022-ecc-chloride-crack-width]] | ECC | 95% RH, 28 d | |
| [[herbert2013-ecc-self-healing-natural-environment]] | ECC | air-cured; cracked at 7 d | outdoor exposure |
| [[deng2015-hdc-compressive-toughness]], [[deng2018-hdc-compressive-constitutive]] | HDC (XAUAT) | **not reported** | test age also n.r. |

### Age and curing effects on ductility and strength
- **Ductility falls with age in PVA systems:** REC-15 ECC 3.21% at 7 d → 1.39% at 28 d ([[sun2019-modified-pva-fiber-ecc]], Table 11).
  Strain hardening weakened with longer curing in slag PE-ECC (except SF-5-55) ([[shumuye2022-slag-fa-pe-ecc]], Sect. 3.2).
  This agrees with the earlier note that PVA-ECC ε falls to about 3% at 180 d (Lepech & Li 2006, as cited in [[pva-fiber]]).
- **Slow strength gain with high FA:** FA/C 3.2 SHCC reaches 46.6% of 28-d f'c at 7 d and about +12% at 90 d
  ([[jin2019-hvfa-shcc-structural]], Fig. 9). → [[fly-ash]]
- **Hot water and bond:** hot-water exposure raised PVA chemical bond by about 50% with frictional bond unchanged
  (Li 2004a, as cited in [[vanzijl2010-shcc-durability]], p. 268). → [[fiber-matrix-interface]]
- **Internal curing:** HPMC may act as internal curing in printed SHCC ([[chavesfigueiredo2020-printed-shcc]], Sects. 3.5–3.6);
  SAP is used for shrinkage control ([[mechtcherine2011-shcc-high-strain-rate]], p. 52). → [[viscosity-modifying-admixtures]]

> Synthesis: round 4 adds a fourth lineage (Korea Univ. steel + PE hybrid) that reaches about 120 MPa at room temperature.
> Heat curing therefore remains unnecessary for strength. Age matters for ductility, though: the 7-d to 28-d loss in
> [[sun2019-modified-pva-fiber-ecc]] means ε_tu values must always be read with their curing age.

## Round-5 evidence (2026-10-21)
- **Hot drying in wet–dry cycles (not curing)**: 55 °C oven drying (CR2) raised the ultimate strength but lowered the strain
  capacity of healed ECC M45 compared with room-air drying (CR1), and gave less self-healing (RF 77–90% vs 87–100%); the
  authors suggest extra hydration and a stronger bond ([[yang2009-ecc-self-healing-wet-dry]], p. 388–389, Fig. 7).
  This mirrors the bond-strengthening effect of heat curing on PVA. → [[self-healing]]
- **No heat curing needed** for a 7.5% / 13 MPa PE composite: the cementless alkali-activated slag composite was cured 2 d
  sealed and then in water at 23 ± 3 °C ([[choi2016-pe-alkali-activated-slag-composite]], §2.1). → [[alkali-activated-binder]]

## Related
- [[hshdc]] · [[mix-designs]] · [[fly-ash]] · [[hybrid-fiber]] · [[pva-fiber]] · [[self-healing]]
