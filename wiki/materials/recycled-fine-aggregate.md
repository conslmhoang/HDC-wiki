---
type: material
slug: recycled-fine-aggregate
aliases: [RFA, recycled sand, recycled concrete fines, alternative fine aggregate, sand type]
tags: [aggregate, sustainability, construction-waste]
sources: [gao2020-hdcc-recycled-fine-aggregate, deng2018-hdc-compressive-constitutive, chai2019-hdcc-freeze-thaw-carbonation-flexure, zhong2019-ecc-freeze-thaw, mohammed2020-cr-ecc-elevated-temperature]
updated: 2026-10-20
---

# Recycled Fine Aggregate (and other sand choices)

## Definition
Fine aggregate made by crushing waste concrete. In [[gao2020-hdcc-recycled-fine-aggregate]] it is jaw- and hammer-crushed
and sieved with a single 1.18 mm screen, with no Fuller-curve regrading (§1, §2.1). This page also collects other sand
variables reported for HDC (sand/binder ratio, river vs quartz sand).

## Key points
- Gao et al. (Zhengzhou Univ.) replaced river sand **fully (100%)** with RFA in PVA "HDCC" (R-HDCC vs N-HDCC)
  ([[gao2020-hdcc-recycled-fine-aggregate]]).
- The authors report a denser matrix, a stronger fiber/matrix bond, higher strengths, and much higher tensile strain at
  Vf ≥ 1.5%. Tensile strain hardening appeared **only in the RFA mixes** at 1.5–2.0% PVA (§3.4).

## Quantitative evidence
### RFA vs river sand properties ([[gao2020-hdcc-recycled-fine-aggregate]], Table 4, §3.1)
| Property | RFA | River sand (NFA) |
|---|---|---|
| Max size | 1.18 mm | 1.18 mm |
| Apparent density | 2536 kg/m³ | 2593 kg/m³ |
| Bulk density | 1309 kg/m³ (−10.34%) | 1460 kg/m³ |
| Water absorption | 6.72% (5.69×) | 1.18% |
| Crushing index | 18.3% (1.43×) | 12.8% |
| Crush dust < 0.075 mm | 4.86× NFA | — |
| 0.075–0.15 / 0.15–0.3 mm fractions | 20.94 / 23.31% | 372.69 / 69.53% lower |

### Composite performance (28 d, PVA 12 mm × 40 µm)
| Property | RFA effect | Location |
|---|---|---|
| f_c (W/B 0.25 series) | +6.67 to +18.45% over river sand; Vf 0–2% has little effect on f_c | §3.2, Fig. 9a (absolute values not tabulated ⚠️) |
| 3-pt flexure (40 mm prisms) | +2.17 to +22.5% | §3.2, Fig. 9b |
| 4-pt bending, 15 mm plates, 2% PVA | σ_bp 11.89 vs 9.41 MPa; deflection 7.67 vs 5.12 mm | Table 5 |
| Tension, W/B 0.45, 2% PVA | ε at peak 4.76% (σ 2.84 MPa) vs 1.68% (2.75 MPa) | Table 6 |
| Tension, 0.5% PVA | ε at peak 1.32 vs 0.41% | Table 6 |

- Gao's "ε_tu" is the **maximum post-peak strain** (up to 11.73%); the values above are strain at peak stress (§2.3.3).
- Tensile strengths are low (σ_tp ≤ 2.84 MPa) compared with PVA-ECC.

## Influencing factors / relationships
- **Mechanisms given by the authors** ([[gao2020-hdcc-recycled-fine-aggregate]], §3.2–3.3):
  - reactive old-paste crumbs and crush dust;
  - better particle packing and a tighter ITZ (RFA absorbs surface water);
  - finer, rougher particles that promote multiple cracking by "crack trapping";
  - a lower aggregate modulus.
  - SEM: fibers pulled out of R-HDCC are rough and stripped of filaments; those from N-HDCC are smooth (Fig. 16). → [[fiber-matrix-interface]]
- **Sand/binder ratio** (XAUAT PVA-HDC, compression): S/B 0.24 / 0.36 / 0.48 gave σ0 51.96 / 62.25 / 56.01 MPa. At
  S/B 0.48 the higher friction made PVA rupture and lowered compressive deformability
  ([[deng2018-hdc-compressive-constitutive]], Table 3, p. 5). → [[compressive-constitutive-model]]
- S/B 0.25–0.75 was **not** significant for frost resistance in the Taguchi study ([[zhong2019-ecc-freeze-thaw]], Tables 5–8). → [[freeze-thaw]]
- **Cost:** domestic PVA with river sand cut HDCC cost to about one third of Kuraray K-II fiber with ground quartz sand
  ([[chai2019-hdcc-freeze-thaw-carbonation-flexure]], p. 127).
- **Rubber as sand replacement:** crumb rubber replacing 2.5–5% of river sand by mass → [[crumb-rubber]]
  ([[mohammed2020-cr-ecc-elevated-temperature]]).
- As cited: ECC with recycled concrete fines reaches "several percent" tensile strain, but the Fuller-curve treatment
  needs multiple screens and more crushing (Li & Yang 2017, as cited in [[gao2020-hdcc-recycled-fine-aggregate]], §1).

> Synthesis: RFA is the only route in the wiki where a **stronger** bond came with **more** ductility. This runs against
> the oiling logic of [[li2002-pva-ecc-interface-tailoring]]. A likely reading is that the N-HDCC bond (unoiled domestic
> PVA, W/B 0.45, no SP) was below the optimum, so raising it helped. No pull-out data exist to test this.

## Conflicts & open questions
- ⚔️ Bond vs ductility: higher (inferred) bond → higher ductility at Vf ≥ 1% ([[gao2020-hdcc-recycled-fine-aggregate]]) vs
  lower bond → higher ductility ([[li2002-pva-ecc-interface-tailoring]]; Li & Leung argument in
  [[chai2019-hdcc-freeze-thaw-carbonation-flexure]]). → [[gaps]]
- ⚔️ Internal: Gao §3.3 says RFA lowers ductility at 0.5% fiber (rupture), but Table 6 shows 45R05 at 1.32% vs 45N05 at 0.41%
  in tension. The statement may refer to the bending series ⚠️.
- Tension (W/B 0.45, no SP) and bending/compression (W/B 0.25) use **different matrices**, so f_c-normalised tension
  models (Eq. 6) are uncertain ⚠️.
- RFA durability (freeze–thaw, chloride, shrinkage with 6.72% absorption) is not studied. → [[gaps]]

## Related
- [[pva-fiber]] · [[fly-ash]] · [[crumb-rubber]] · [[tensile-strain-capacity]] · [[mix-designs]] · [[terminology-hdc-ecc-shcc]]
