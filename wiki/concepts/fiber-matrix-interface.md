---
type: concept
slug: fiber-matrix-interface
aliases: [interfacial bond, frictional bond, chemical bond, snubbing, slip hardening, inclination hardening, fiber pullout model]
tags: [micromechanics, interface]
sources: [li1992-steady-state-multiple-cracking, li2002-pva-ecc-interface-tailoring, ranade2015-hshdc-tensile-rate-effects, yang2024-hshdc-uniaxial-tension, su2023-rubber-modified-hshdc, zhang2022-hshdcc-review, yu2018-ecc-direct-tensile-review, yang2008-ecc-fiber-bridging-law, kanda2006-psh-design-criteria, chai2023-hdc-ambient-temperature, mechtcherine2011-shcc-high-strain-rate, kanda2003-sprayed-ecc, jin2019-hvfa-shcc-structural, gao2020-hdcc-recycled-fine-aggregate, shumuye2022-slag-fa-pe-ecc, sun2019-modified-pva-fiber-ecc, vanzijl2010-shcc-durability, wang2023-ecc-frost-damage, yun2013-shcc-freeze-thaw, pourfalah2018-ecc-high-temperature, lepech2009-ecc-water-permeability, huy2023-egc-activator-pretreatment, huy2023-egc-pe-pva-hybrid-healing]
updated: 2026-10-26
---

# Fiber/Matrix Interface Properties

## Definition
| Symbol | Meaning |
|---|---|
| τ0 | frictional bond |
| Gd | chemical debonding energy |
| β | slip hardening |
| f | snubbing coefficient |
| µ | inclination hardening |

These parameters govern single-fiber pullout and therefore [[fiber-bridging]].

## Key points
- **Hydrophilic fibers** (PVA) form both chemical and frictional bonds. **Hydrophobic fibers** (PE)
  and steel form friction only ([[ranade2015-hshdc-tensile-rate-effects]], p. 94–95;
  [[yang2024-hshdc-uniaxial-tension]], p. 5).
- **W/B and FA tune the bond** ([[yang2024-hshdc-uniaxial-tension]], p. 10–11):
  - A lower W/B raises Gd and τ0. Too much bond ruptures fibers; too little lets them slip.
  - FA lowers the bond.
  → [[water-binder-ratio]], [[fly-ash]]
- **Inclination hardening µ** is specific to the very-high-strength Michigan matrix
  (Ranade et al. 2013, as cited in [[ranade2015-hshdc-tensile-rate-effects]], p. 98).
- **Rate dependence** (Michigan HSHDC, 0.009 → 900 mm/s; [[ranade2015-hshdc-tensile-rate-effects]], Fig. 8–9):

  | Parameter | Quasi-static | 900 mm/s | Change |
  |---|---|---|---|
  | τ0 | — | — | +14% |
  | β | 0.003 | 0.006 | ×2 |
  | f | 0.59 | 0.75 | +27% |
  | µ (N/(m·rad)) | 386 | 553 | +43% |

  The interface is fairly rate-insensitive because PE has no chemical bond. → [[strain-rate-effects]]
- β for ECC is about 0.6 (Wang & Li 2007, as cited in [[ranade2015-hshdc-tensile-rate-effects]], p. 98),
  now confirmed primarily: β 0.58–0.63 for 1.2%-oiled PVA in the M45 fly-ash matrix ([[yang2008-ecc-fiber-bridging-law]], Table 3).
  Li 2002 measured **β = 1.15–2.31** for PVA in a w/c 0.45 matrix. This is a refinement, since
  fiber, oiling and matrix differ.
- **PVA interface tailoring** ([[li2002-pva-ecc-interface-tailoring]], Table 3):
  - Oiling from 0 to 1.2% gives τ0 2.44 → 1.11 MPa, Gd 4.71 → 1.61 J/m², β 2.21 → 1.15.
  - Design targets (Wu 2001, as cited): Gd < 2.2 J/m², τ0 1.0–2.1 MPa, β < 1.5.
  - Non-oiled fibers delaminate and rupture with a "pencil-sharpened" end; oiled fibers slide out (Fig. 8–9).
  → [[fiber-surface-treatment]]
- **PE interface in HSHDCC** ([[zhang2022-hshdcc-review]], Table 4):
  - Uncoated PE τ0 ranges 0.42–2.68 MPa and rises with matrix f'c.
  - Coatings raise the bond, but too much bond causes fiber rupture and loss of ε_tu.
- **Classic pullout model** (friction only; [[li1992-steady-state-multiple-cracking]], Eqs. 1–2):
  - debonding: P = (π/2)√((1+η)Ef·df³·τ·δ)·e^{fφ}
  - slippage: P = πτl·df(1 − δ/l)e^{fφ}
  - The snubbing coefficient f is measured at 0.5–1 for fibers in cement (as cited).
- **Rate effects for PVA**: from 10⁻⁵ to 10⁻¹ s⁻¹, bond, matrix toughness and fiber E/strength all
  rise. The PSH energy index falls about 50% (as cited in [[yu2018-ecc-direct-tensile-review]], p. 350).
- **SEM evidence:**
  - PE pull-out holes and scratched fiber ends ([[yang2024-hshdc-uniaxial-tension]], Fig. 11).
  - A gap at the rubber–matrix interface ([[su2023-rubber-modified-hshdc]], Fig. 8).

## Conflicts & open questions
- Measured interface data now exist for PE in the Michigan matrix
  ([[ranade2015-hshdc-tensile-rate-effects]]) and for PVA in a normal matrix
  ([[li2002-pva-ecc-interface-tailoring]]). GDUT, Xi'an and Tongji HSHDC/UHDC still lack pullout data. → [[gaps]]

## Further interface data (2026-10-20 ingest)
- **Same fiber, different matrix** (1.2%-oiled PVA, 2%): M45 with FA/C 1.2 gives τ0 1.31, Gd 1.08, β 0.58
  ([[yang2008-ecc-fiber-bridging-law]]); w/c 0.45 without FA gives τ0 1.11, Gd 1.61, β 1.15 ([[li2002-pva-ecc-interface-tailoring]]).
  Fly ash and matrix change β by about 2×.
- **Bond falls as Vf rises** in M45 (0.1 → 0.5 → 2%: τ0 1.91 → 1.58 → 1.31 MPa), attributed to air content ([[yang2008-ecc-fiber-bridging-law]], Table 3).
- PVA slip hardening comes from abrasion and jamming in the matrix tunnel, so fibers debond from both
  sides (two-way pull-out). PE, PP and smooth steel have β ≈ 0 or < 0 ([[yang2008-ecc-fiber-bridging-law]], p. 184).
- Too much bond causes rupture: τ_i 4.25–4.35 MPa with 14 µm PVA gave only 0.26–0.55% strain;
  plug pull-out (fiber leaves with a matrix block) is not covered by theory ([[kanda2006-psh-design-criteria]], Table 3, p. 66).
- Chinese HDC papers claim temperature exposure lowers chemical bond and raises friction, but cite a
  thesis rather than measuring it ([[chai2023-hdc-ambient-temperature]], §3.4.3).

## Round-4 interface evidence (2026-10-20 ingest)
**Measured or model-input values**

| Source | Fiber / matrix | Frictional bond | Chemical bond | Other | Note |
|---|---|---|---|---|---|
| [[kanda2003-sprayed-ecc]], Table 2 (after Kiyota et al. 2002) | PVA 12 mm × 40 µm in cement, w/c 0.27 / 0.42 / 0.62 | τi 3.14 / 3.31 / 2.63 MPa | τs 21.6 / 20.7 / 4.55 MPa (a bond **strength**, not Gd) | f 0.5, f′ 0.39, apparent fiber strength 1070 MPa | chemical bond falls sharply at high w/c |
| [[jin2019-hvfa-shcc-structural]], Table 1 | generic PVA-SHCC model | τ0 1.0 MPa (assumed) | Gd 1.5 J/m² (assumed) | — | parametric only |

**Effects on bond (mostly inferred, not measured)**

| Factor | Effect on bond | Evidence | Source |
|---|---|---|---|
| Strain rate (PVA) | pull-out peak force about ×2 from 10⁻⁵ to 10 s⁻¹ (1 mm embedment); failure shifts from adhesive to partly cohesive in the interphase | measured, single-fiber pull-out | [[mechtcherine2011-shcc-high-strain-rate]], Figs. 13–15 |
| W/B and FA/C ↑ | bond and Km ↓ | authors' claim, not measured | [[jin2019-hvfa-shcc-structural]], §2.2 |
| Recycled fine aggregate | bond ↑ (fiber surface filaments stripped vs smooth in N-HDCC) | SEM only | [[gao2020-hdcc-recycled-fine-aggregate]], Fig. 16 → [[recycled-fine-aggregate]] |
| Slag (PE-ECC) | bond ↑, more hydrates adhered to PE, possible rupture | SEM only | [[shumuye2022-slag-fa-pe-ecc]], §3.5.1 → [[ggbfs]] |
| VAE emulsion on PVA | bond ↓ (acidic film retards hydration near fiber, weaker ITZ); slip scratches on fibers | SEM + composite tests | [[sun2019-modified-pva-fiber-ecc]], §3.2, Figs. 11–12 → [[fiber-surface-treatment]] |
| Boric anhydride on PVA | bond ↓ too far; long intact pull-out | SEM + composite tests | [[sun2019-modified-pva-fiber-ecc]], Figs. 11–12 |
| Chloride cycling (10 × [5 d sat. NaCl + 2 d 50 °C]) | PVA chemical bond significantly ↓, frictional slightly ↑; Km unchanged | measured (Kabele 2006/2007, as cited) | [[vanzijl2010-shcc-durability]], p. 265 → [[chloride-and-corrosion]] |
| Hot water | chemical bond about +50%, frictional unchanged | measured (Li 2004a, as cited) | [[vanzijl2010-shcc-durability]], p. 268 |
| Freeze–thaw (300 cycles) | PVA bond ↓ → more pull-out, fewer ruptures | inferred from flexure | [[wang2023-ecc-frost-damage]], §3.2 → [[freeze-thaw]] |

- **Mechanism of the PVA chemical bond:** PVA –C–OH groups hydrogen-bond with matrix –OH; untreated PVA fibers
  carry hydrates and neck at break ([[sun2019-modified-pva-fiber-ecc]], §3.2, Fig. 11).
- **Model sensitivities:** J′b/J_tip falls linearly with Gd and steeply, then gently, with τ0
  ([[jin2019-hvfa-shcc-structural]], Fig. 1c–f). → [[fiber-bridging]]
- ⚔️ **Higher bond, higher ductility?** RFA raised the (inferred) bond and also ε_tp at Vf ≥ 1%, but at 0.5% fiber the
  higher bond coincided with fiber rupture and lower ductility ([[gao2020-hdcc-recycled-fine-aggregate]], §3.3).
  This runs against the low-bond rule of [[li2002-pva-ecc-interface-tailoring]]; see [[strain-hardening]] and [[gaps]].

> Synthesis: the PVA rate sensitivity now has a primary measurement ([[mechtcherine2011-shcc-high-strain-rate]]),
> confirming that PVA composites are interface-governed at high rate, whereas PE-HSHDC is fiber-governed
> ([[ranade2015-hshdc-tensile-rate-effects]]). Durability exposures move the PVA chemical bond in both directions
> (chloride ↓, hot water ↑), so the "just right" interface of a new ECC may drift in service. Almost all round-4
> bond claims rest on SEM, not on pull-out tests. → [[single-fiber-pullout-test]]

## Round-5 interface evidence (2026-10-21)
- **Freeze–thaw**: SEM shows F-T microcracks in the fibre–matrix ITZ of hybrid PVA + PE SHCC frozen from 14 d; the ITZ was
  still porous at 14 d and dense at 28 d, so hydraulic pressure in a young ITZ is blamed ([[yun2013-shcc-freeze-thaw]],
  Fig. 13, §3.5). First primary image of the F-T interface damage that [[wang2023-ecc-frost-damage]] inferred. → [[freeze-thaw]]
- **Moderate heat**: up to 100 °C, lower PVA modulus and weaker chemical bond are said to lengthen debonding and widen cracks
  (mechanism inferred); PVA switches from rupture to full pull-out at 150 °C (pull-out length 500 → 6000 µm); steel bond
  rises with thermal expansion up to 400 °C ([[pourfalah2018-ecc-high-temperature]], §4.3, Figs. 12, 14).
  → [[high-temperature-behaviour]]
- **M45 bond model limits**: the pull-out model behind σ(δ) ignores two-way pull-out and matrix spalling, so J′b is
  underestimated; J′b/J_tip ≈ 1.08 is a lower bound ([[lepech2009-ecc-water-permeability]], p. 749).

## Round-7 interface evidence (2026-10-26): PE/PVA in geopolymer matrices
- **PE in fly-ash ED-EGC**: SEM shows reaction products agglomerated on PE surfaces and both pull-out and rupture failure modes
  (Fig. 12); BSE shows voids at the PE/matrix interface, attributed to drying (Fig. 13), so a strong bond is not confirmed
  ([[huy2023-egc-activator-pretreatment]], p. 13). τ0 and Gd were not measured.
- **Hybrid PE + PVA in GGBS/FA EGC**: GGBS-rich (S) mixes had more, narrower cracks, which the authors read as a stronger
  fibre–matrix bond (not measured); hydrophilic PVA attracts healing products, hydrophobic PE does not
  ([[huy2023-egc-pe-pva-hybrid-healing]], §3.1.2, §3.2.1). After healing, the authors claim a better-bonded interface (σ_tu
  +3.7%, ε −6.1% on reloading, Table 8). → [[self-healing]], [[hybrid-fiber]]

## Related
- [[fiber-bridging]] · [[single-fiber-pullout-test]] · [[pe-fiber]] · [[pva-fiber]] · [[fiber-surface-treatment]] · [[interface-bond]] · [[high-temperature-behaviour]] · [[alkali-activated-binder]]
