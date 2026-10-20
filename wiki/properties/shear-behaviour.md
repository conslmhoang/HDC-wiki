---
type: property
slug: shear-behaviour
aliases: [shear strength, shear capacity, diagonal cracking, shear strengthening, truss-arch model]
tags: [structural, shear, members]
sources: [deng2018-hdc-short-columns, wang2019-rc-beam-ecc-shear-strengthening, xue2023-shcc-structural-review, yuan2020-nshsdc-beam-strengthening, kanakubo2006-dfrcc-tensile-test-method, deng2015-hdc-compressive-toughness]
updated: 2026-10-20
---

# Shear Behaviour of HDC / ECC / SHCC Members

## Definition
Shear response of members made of, or strengthened with, strain-hardening composites: diagonal cracking,
shear capacity, failure mode, and design formulas. Material-level tension is on [[tensile-strain-capacity]].

## Key points
- Fiber bridging across diagonal cracks carries shear after cracking and slows stiffness degradation
  ([[deng2018-hdc-short-columns]], p. 8, Conclusion 5). → [[fiber-bridging]]
- Members made of these materials show a **dense network of fine diagonal cracks** instead of a few
  X-shaped macro-cracks, and no cover spalling ([[deng2018-hdc-short-columns]], Figs. 6–7).
- Tensile deformation capacity is "not an important factor" for member shear; confinement and cover
  retention matter (JCI view, [[kanakubo2006-dfrcc-tensile-test-method]], p. 3).
- The bridging stress of PVA-HDC (5.7 MPa) is equivalent to a stirrup ratio of 3.03% in a 500 mm column
  ([[deng2015-hdc-compressive-toughness]], Eqs. 7–9). → [[compressive-constitutive-model]]

## Quantitative evidence
### Members cast in HDC / SHCC
| Source | Member | Result |
|---|---|---|
| [[deng2018-hdc-short-columns]] Tables 5–7 | 6 square 250 mm XAUAT PVA-HDC short columns vs 1 RC column, reversed cyclic load | HDC3 vs RC1 (same N, ρ_sv): P_m +24%, ductility μ 2.32 vs 1.69, ultimate drift 1/32 vs 1/55; cracking load 120–150 vs 80 kN; energy 2.8–4.4× |
| same, p. 8 | stirrup ratio cut by 20 / 33% | P_m only −4.4 / −6.6% → HDC can replace part of the stirrups |
| same, Table 7 | code check | P_m / V_n = 1.08–1.26 with GB 50010-2010; 1.40–2.08 with ACI 318-05 (both conservative) |
| [[xue2023-shcc-structural-review]] Section 3.2, Fig. 3 | SHCC beam without stirrups (25 mm bar) | sudden diagonal shear failure at nominal 9.8 MPa (a/d 2) and 7.0 MPa (a/d 3); crack angle 33.5° / 28°; smooth fracture surface |
| [[kanakubo2006-dfrcc-tensile-test-method]] Fig. 1 | UFC (Ductal) vs PVA-ECC beams, same reinforcement | UFC shear capacity 1.7× the PVA-ECC beam; similar crack pattern |

- RC1 failed in brittle shear at about 1.8% drift with cover crushing; HDC columns failed in "ductile shear"
  ([[deng2018-hdc-short-columns]], p. 4–5).
- XAUAT PVA-HDC in these columns has only ε_tu ≈ 1.0% (σ_tu 6.14 MPa), so good shear behaviour does not
  require ECC-level tensile ductility ([[deng2018-hdc-short-columns]], Fig. 1).

### Shear strengthening of RC beams without stirrups
| Source | Strengthening | Result |
|---|---|---|
| [[wang2019-rc-beam-ecc-shear-strengthening]] Table 3 | sprayed PVA-ECC (σ_tu 4.84 MPa) side layers 20 / 40 mm, 150 × 300 mm beams | ultimate load +20–89%; best +89% (185 → 350 kN) at a/d 2, ρ 2.18%; +40–89% at a/d 2 vs +20–41% at a/d 3 |
| same, Sect. 3.3 | failure | still shear or debonding, never flexure; all 40 mm layers debonded; at a/d 3, 20 and 40 mm gave the same capacity |
| same, Sect. 3.3.1 | over-strengthening | counting the ECC width lowered the effective ρ to 0.58%, below the code minimum ("0.65%" ⚠️): SA-40-2 190 kN vs SA-20-2 250 kN |
| [[xue2023-shcc-structural-review]] Section 4.2 (as cited) | 3 mm SHCC on both sides, a/d 3 | "significant" increase (no value); contact stress plus bridging on layer cracks |
| [[yuan2020-nshsdc-beam-strengthening]] Table 8 | Korea Univ. NSHSDC jackets (steel + PE hybrid) on 125 × 250 mm NSC beams without stirrups | bottom only: no gain (74.04 vs 75.93 kN), web failed in shear first; top + bottom +8%; 3 sides +29% (concrete crushing, no rebar yield); 4 sides +40% with **flexural** failure, energy 7.11 vs 5.73 kN·m for a stirrup-reinforced beam |

### Design model: truss + arch ([[wang2019-rc-beam-ecc-shear-strengthening]], Eqs. 1, 10–11, Table 4)
- V = 2(η·β·σ_t·h·t + arch term), with the ECC post-cracking tensile strength σ_t acting as a 45° tension tie
  over layer height h and thickness t. → [[tensile-constitutive-model]]
- η = 0.6 (20 mm) or 0.4 (40 mm), an empirical bond-efficiency factor; β = −23.04ρ + 1.00 (units of ρ ⚠️);
  concrete softening ν = 0.6; φ = 45°.
- Prediction/test = 68–100% at a/d 3 but only 45–52% at a/d 2 (conservative where arching dominates).
- The authors call ν = 0.6 too conservative for ECC under biaxial tension–compression and list it as a research need.

> Synthesis: across the four primary studies, strain-hardening composites raise shear capacity and change
> brittle diagonal failure into a distributed-cracking, more ductile mode. The gain depends on a/d, the
> number of sides covered, and **bond to the substrate**: side layers alone (Wang 2019) never moved failure to
> flexure and thick layers debonded, whereas a four-side jacket (Yuan 2020) did. Code formulas (GB 50010,
> ACI 318) are conservative for HDC members, and no formula yet credits the composite's tension explicitly
> except Wang's empirical truss–arch model. → [[interface-bond]], [[rc-member-strengthening]]

## Conflicts & open questions
- ⚔️ [[he2024-hdc-research-advances]] cites "Deng & Zhang 2018" for HDC jacketing of cross-shaped short columns;
  [[deng2018-hdc-short-columns]] tests whole-HDC square columns. Possibly another paper. → [[gaps]]
- Applicability of RC shear formulas to HDC is unknown ([[deng2018-hdc-short-columns]], p. 10).
- Softening coefficient of ECC under biaxial tension–compression is unmeasured ([[wang2019-rc-beam-ecc-shear-strengthening]]).
- One beam per case in Yuan 2020; no shear tests on PE-HSHDC members.

## Related
- [[rc-member-strengthening]] · [[unreinforced-hdc-structures]] · [[interface-bond]] · [[fiber-bridging]] · [[compressive-constitutive-model]]
