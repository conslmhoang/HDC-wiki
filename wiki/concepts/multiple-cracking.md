---
type: concept
slug: multiple-cracking
aliases: [multiple microcracking, saturated cracking, crack number, crack density]
tags: [mechanism]
sources: [ranade2015-hshdc-tensile-rate-effects, ranade2017-hshdc-impact-resistance, su2023-rubber-modified-hshdc, yang2024-hshdc-uniaxial-tension, ye2021-uhdc-flexural-size-effect, li1992-steady-state-multiple-cracking, li2002-pva-ecc-interface-tailoring, zhang2022-hshdcc-review, kanda2006-psh-design-criteria, yang2008-ecc-fiber-bridging-law, kunieda2010-uhp-shcc-steel-reinforcement, kunieda2006-hpfrcc-japan-applications, mechtcherine2011-shcc-high-strain-rate, deng2018-hdc-short-columns, gao2020-hdcc-recycled-fine-aggregate, qian2007-shcc-inverse-tensile-strain, shumuye2022-slag-fa-pe-ecc, sui2018-uhp-ecc-flexural-fatigue, wang2019-rc-beam-ecc-shear-strengthening, xue2023-shcc-structural-review, zhao2022-ecc-tension-damage-model, yun2013-shcc-freeze-thaw, pourfalah2018-ecc-high-temperature, choi2016-pe-alkali-activated-slag-composite, lepech2009-ecc-water-permeability, yang2009-ecc-self-healing-wet-dry, zhang2022-hdc-basalt-textile-tension, hieu2023-aas-extremely-ductile-22pct, huy2023-egc-activator-pretreatment, huy2023-egc-pe-pva-hybrid-healing]
updated: 2026-10-26
---

# Multiple Cracking

## Definition
The formation of many fine, closely spaced cracks instead of one localized crack. It is the
physical mechanism behind [[strain-hardening]].

## Key points
- **nth-crack condition** (Kanda & Li, as cited): each new crack forms at the next-largest flaw
  while bridging capacity at the existing cracks is not exceeded ([[su2023-rubber-modified-hshdc]], p. 6).
- **Fracture stages in notched beams** ([[ye2021-uhdc-flexural-size-effect]], §3.1):
  - NC: a single brittle crack.
  - UHDC-1 (1% PE): "weak fracture-hardening", ending in one critical crack.
  - UHDC-2 (2% PE): "strong fracture-hardening", with multiple cracks and no localization.
  - All end in fracture-softening.
- **Four-zone fracture model** with a "quasi-plastic zone" ([[yang2024-hshdc-uniaxial-tension]], Fig. 12).
- **Under impact:**
  - HSHDC slabs show fine radial cracks and almost no spalling. Cor-Tuf forms 4 yield-line macro-cracks
    and breaks apart ([[ranade2017-hshdc-impact-resistance]], p. 30–31).
  - FE gives back-face principal strain below 1% everywhere in HSHDC, against localised strain up to
    3% in Cor-Tuf (Fig. 11).
- **Under strain rate:** σ_tu/σ_fc stays about constant, so the crack count stays about the same
  ([[ranade2015-hshdc-tensile-rate-effects]], p. 97). → [[strain-rate-effects]]

## Quantitative evidence
| Source | Mix | No. of cracks | Crack density | Note |
|---|---|---|---|---|
| [[su2023-rubber-modified-hshdc]] Table 3 | PE18-PR20 | 31 | 0.45 mm⁻¹ | DIC: a crack is counted above a 9 µm displacement jump |
| same | PE6 group | 1 | — | brittle |
| same | 12 mm group | rises with PR | — | ⚠️ the text range (8–17) conflicts with the table (23) |

Crack number rises with fiber length and rubber content ([[su2023-rubber-modified-hshdc]], Table 3). → [[crack-width]]

## Mechanism and crack saturation (2026-10-16 ingest)
- **Mechanism** ([[li1992-steady-state-multiple-cracking]], p. 2255):
  - After the first crack, the fibers must carry the total load.
  - If they can, they transfer load back to the matrix by shear, and a new crack forms.
  - This repeats into periodic sub-parallel cracks until σ0 is reached.
  - Multiple cracking also needs a flaw size c̃ > c̃_mc. → [[steady-state-cracking]]
- **PVA-ECC crack spacing** with oil 0 / 0.3 / 0.5 / 0.8 / 1.2%: 27 / 7.5 / 3.5 / 2.5 / 2.8 mm
  ([[li2002-pva-ecc-interface-tailoring]], Table 4).
  - From 0.3% to 0.5% oil, ductility comes from **more** cracks.
  - Above that, it comes from **wider** cracks. Saturation is reached at about 0.8% oil.
  - Saturated specimens have more than 60 cracks in 150 mm (p. 467–471).
- In HSHDCC, adding SF from 0 to 40% raised the crack count and lowered crack width
  (Lei 2019, as cited in [[zhang2022-hshdcc-review]], p. 12).

## Saturation (2026-10-20 ingest)
- **Saturation index** = x_d^test / x_d, where x_d is the Wu & Li 1995 saturated spacing and x_d^test is
  inferred as δ_peak/ε_cu. A ratio > 2 means saturated cracking is "rarely expected" ([[kanda2006-psh-design-criteria]], Eqs. 15–16, p. 69).
- M45 PVA-ECC: average crack spacing about 1 mm, crack width constant at about 60 µm after 1% strain ([[yang2008-ecc-fiber-bridging-law]], p. 181, 188).

## Material-level observations (2026-10-20 ingest)
- **Rate:** in PVA-SHCC, crack density falls as the rate rises to 10⁻² s⁻¹; at ≥ 10 s⁻¹ there is **no visible
  multiple cracking** although strain rises again ([[mechtcherine2011-shcc-high-strain-rate]], p. 58–59). This
  contrasts with Michigan PE-HSHDC, where crack count stays about constant ([[ranade2015-hshdc-tensile-rate-effects]]).
  → [[strain-rate-effects]]
- **Fiber content:** at 0.5% PVA, bridging is below cracking strength and no multiple cracking forms
  ([[gao2020-hdcc-recycled-fine-aggregate]], §3.3). The authors claim finer recycled-sand particles promote
  multiple cracking by "crack trapping" (CT shows smaller, narrower void sizes, Fig. 14). → [[recycled-fine-aggregate]]
- **Fly ash:** crack saturation in bending increases with FA/C ([[qian2007-shcc-inverse-tensile-strain]], Fig. 12).
  Artificial flaws of prescribed size give more saturated cracking (Wang & Li 2004, as cited there, p. 235). → [[fly-ash]]
- **Slag:** σ_tu/σ_fc 2.02–4.23 in slag/FA PE-ECC; more slag and longer curing reduce hardening and widen cracks
  ([[shumuye2022-slag-fa-pe-ecc]], Table 4, §3.2). → [[ggbfs]]
- **Flexure (DIC):** UHP-ECC beams show the first crack at 58% of peak, 18 cracks at 72%, and saturation near span/30
  ([[sui2018-uhp-ecc-flexural-fatigue]], Fig. 9). → [[fatigue]]
- **Damage stages in tension:** elastic → hardening with dispersed stable damage → softening with unstable damage;
  the main crack forms near the grips ([[zhao2022-ecc-tension-damage-model]], §3.2, Fig. 4). → [[tensile-constitutive-model]]
- **XAUAT PVA-HDC:** serrated hardening plateau with multiple parallel cracks in direct tension
  ([[deng2018-hdc-short-columns]], Fig. 1).

## Member-level multiple cracking (2026-10-20 ingest)
Multiple cracking at member scale is generally **less** than in dogbone tests.

| Source | Member | Observation |
|---|---|---|
| [[kunieda2010-uhp-shcc-steel-reinforcement]], Table 3 | UHP-SHCC tension members 50 × 200 × 900 mm | unreinforced: 43 cracks, spacing 12 mm, ε 0.24%; with D6 bars (ρs 0.3%): 119 cracks, spacing 4.6 mm, ε 1.58% |
| same, Figs. 15–17, §4.4 | same | above ρs 0.6% crack number and spacing hardly change; distributed cracking needs P_u ≥ about 1.5 P_cr; steel carries 18.5% (ρs 0.3%) to 49.8% (1.2%) of load at yield |
| [[xue2023-shcc-structural-review]], §3.1, 4.1.2 | SHCC beams and strengthening layers | fewer cracks than in dogbones; thin layers crack only over the existing RC crack ("zero-span" mode), 50 mm layers show distributed bending cracks |
| [[kunieda2006-hpfrcc-japan-applications]], p. 22–23, Fig. 9 | HPFRCC repair over a substrate crack | bonding to the substrate constrains the overlay and may concentrate cracking; an unbonded zone widens the cracked region (Kunieda 2004, as cited) → [[interface-bond]] |
| [[deng2018-hdc-short-columns]], Fig. 6 | XAUAT HDC short columns in shear | dense network of fine diagonal cracks instead of X-shaped macro-cracks → [[shear-behaviour]] |
| [[wang2019-rc-beam-ecc-shear-strengthening]], Fig. 7 | RC beams with sprayed ECC side layers | more, closer-spaced cracks than RC controls; no widths given → [[rc-member-strengthening]] |

> Synthesis: three independent observations (Kunieda 2010 thickness, Xue 2023 thin layers, Kunieda 2006 substrate
> restraint) show that dogbone crack counts overstate member-level multiple cracking. Steel reinforcement or a
> debonded zone restores distributed cracking. Use dogbone ε_tu only as an upper bound for members. → [[size-effect]]

## Round-5 evidence (2026-10-21)
| Source | Condition | Cracks | Note |
|---|---|---|---|
| [[choi2016-pe-alkali-activated-slag-composite]] Table 8 | alkali-activated slag + 1.75% PE, W/B 0.26–0.38, 80 mm gauge | 46–67 cracks; spacing 1.20–2.25 mm; computed avg width 88.9–109.8 µm | most and narrowest cracks at lowest W/B |
| [[lepech2009-ecc-water-permeability]] Tables 3, 5 | ECC M45 at 1.5 / 2 / 3% | 47 / 59 / 87 cracks; spacing 2–5 mm; 50–63 µm unloaded | typical ≈ 60 µm width reached at ≈ 1% strain, then new cracks form (p. 745, Fig. 1) |
| [[yang2009-ecc-self-healing-wet-dry]] Table 2 | ECC M45 at 0.3–3% | 5–39 cracks per 100 mm; residual max 50–90 µm | after healing, re-cracks follow healed paths and some form beside them (Figs. 15–17) |
| [[yun2013-shcc-freeze-thaw]] Figs. 6, 11 | hybrid PVA + PE SHCC, 300 F-T cycles | fewer, less spread cracks in tension; **single crack** in flexure after F-T | more PE → more fine cracks before F-T |
| [[pourfalah2018-ecc-high-temperature]] Fig. 10d | PVA-ECC, hot bending | ≈ 15–23 cracks at 20 °C → one crack from 150 °C | steel hybrid limits crack width |
| [[zhang2022-hdc-basalt-textile-tension]] §3.1 | basalt textile + PVA-HDC | crack spacing ≈ grid spacing (25 mm); with ≥ 1.5% PVA multiple cracking up to peak, no spalling | → [[textile-reinforced-hdc]] |

## Round-7 evidence (2026-10-26)
| Source | Condition | Cracks | Note |
|---|---|---|---|
| [[hieu2023-aas-extremely-ductile-22pct]] Table 6 | ED-AASC, 1.75% PE, 3 mixing procedures, 80 mm gauge | 66.5 / 86.4 / 81.8 cracks; spacing 1.27 / 0.95 / 0.98 mm; computed avg width 117 / 212 / 204 µm at peak | more cracks ↔ higher ε (M1, 22.34%); saturated |
| [[huy2023-egc-activator-pretreatment]] Table 5 | fly-ash ED-EGC, 1.75% PE | 50.0 (WP) / 72.8 (CP); spacing 1.57 / 1.07 mm; avg width 171.8 / 199.3 µm | weaker matrix → more and wider cracks |
| [[huy2023-egc-pe-pva-hybrid-healing]] Table 6 | HSUD-EGC, 1.5% PE + PVA | 61.0–84.3 cracks; spacing 0.96–1.31 mm; avg width 83–136 µm | GGBS-rich (S) mixes: more, narrower cracks; reloaded after healing 52–66 cracks (Table 8) |

> Synthesis (round 7): in the cementless CNU composites ε rises mainly through **wider** cracks at a ≈ 1 mm spacing rather
> than through more cracks: 22% strain over 80 mm needs ≈ 200 µm per crack even with ≈ 86 cracks. Crack spacing appears
> to saturate near 1 mm in all three sources. → [[crack-width]]

> Synthesis: exposure (frost, heat) removes multiple cracking before it removes strength: F-T and 150 °C both reduce the
> crack count while σ_tu or load is largely kept. Crack count is therefore a sensitive damage indicator. → [[durability]]

## Related
- [[strain-hardening]] · [[crack-width]] · [[fiber-bridging]] · [[digital-image-correlation]] · [[interface-bond]] · [[durability]] · [[textile-reinforced-hdc]]
