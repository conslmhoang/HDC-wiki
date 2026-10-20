---
type: property
slug: shear-behaviour
aliases: [shear strength, shear capacity, diagonal cracking, shear strengthening, truss-arch model, modified ACI formula, HDC beam shear]
tags: [structural, shear, members]
sources: [deng2018-hdc-short-columns, wang2019-rc-beam-ecc-shear-strengthening, xue2023-shcc-structural-review, yuan2020-nshsdc-beam-strengthening, kanakubo2006-dfrcc-tensile-test-method, deng2015-hdc-compressive-toughness, li2021-hdc-beam-shear, deng2017-rc-column-hdc-jacket, deng2020-aac-wall-hdc-retrofit, deng2019-urm-shaking-table-hdc]
updated: 2026-10-21
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
- Fibre bridging across inclined cracks keeps HDC beams carrying load after the critical crack and lets stirrups
  yield fully ([[li2021-hdc-beam-shear]], §3.3–3.4).
- As cited: ECC shear strength exceeds its direct tensile strength by up to 50% (Li et al. 1994, refs 29–30 in
  [[li2021-hdc-beam-shear]], §1).
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
| [[li2021-hdc-beam-shear]] Table 4, Table 6 | 8 PVA-HDC (ε_tu 0.968%, f_cu 70.55 MPa) + 2 RC beams 120 × 180 mm **with stirrups**, a/d 1 and 2, ρ_sv 0.40–0.79% | peak 471–520 vs RC 393 kN (a/d 1); 285–354 vs 275 kN (a/d 2); V/(√f'c·bd) 1.82–2.00 vs 1.41 (a/d 1) and 1.12–1.39 vs 0.94 (a/d 2) |
| same, Table 6, Figs. 5–6 | failure modes | HDC: direct shear (a/d 1), shear compression or shear tension (a/d 2); RC: diagonal compression with crushing and spalling |
| same, §3.1–3.4 | cracking, deflection, steel | HDC first cracking at 70–80% of the RC cracking load; peak 1.85–3.18× the first inclined-cracking load; deflection at peak 2.72× (a/d 1) and 1.30× (a/d 2) of RC; rebar yielded at loads 12–84% higher than in RC, then > 25% further load gain |
| same, §3.2, §3.5, Table 6 | reinforcement effect | at a/d 1, stirrup and longitudinal ratios barely changed capacity (section upper limit); more stirrups did not always help: SE-2b (φ6@120) 354 kN > SE-2a (φ6@80) 285 kN |
| [[kanakubo2006-dfrcc-tensile-test-method]] Fig. 1 | UFC (Ductal) vs PVA-ECC beams, same reinforcement | UFC shear capacity 1.7× the PVA-ECC beam; similar crack pattern |

- RC1 failed in brittle shear at about 1.8% drift with cover crushing; HDC columns failed in "ductile shear"
  ([[deng2018-hdc-short-columns]], p. 4–5).
- XAUAT PVA-HDC in these columns has only ε_tu ≈ 1.0% (σ_tu 6.14 MPa), so good shear behaviour does not
  require ECC-level tensile ductility ([[deng2018-hdc-short-columns]], Fig. 1). The beams of
  [[li2021-hdc-beam-shear]] (ε_tu 0.968%, §2.1) support the same reading.

### Shear-critical RC columns with HDC jackets
| Source | Jacket | Result |
|---|---|---|
| [[deng2017-rc-column-hdc-jacket]] Tables 6–7 | 30 mm four-sided plain HDC (HDC-0), 250 mm square columns, shear-span ratio 3 | P_m +50–57% vs control, but **still bend-shear** with widening diagonal cracks |
| same, Table 6, Fig. 7 | 30 mm HDC + Ø6@80 bar mesh (HDC-B) | diagonal cracking suppressed; flexural plastic hinge; μ 7.9 / 6.3 vs 3.3 / 2.9 (⚠️ higher axial load on jacketed columns) |
| same, Fig. 10 | stirrup strain | control stirrups yielded before peak; none did in HDC-jacketed columns |

### Masonry walls with HDC layers
- A 15 mm single-sided HDC layer raised the diagonal-shear capacity of AAC walls above their sliding capacity, so the
  governing mode changed to bed-joint sliding ([[deng2020-aac-wall-hdc-retrofit]], §3.1). Design: V_HDC =
  0.44·α_HDC·f_tu·t′·x (α_HDC 0.53); sliding V = µN + µ f_tu t (0.5 l), µ = 0.7 (Eqs. 12–14).
- Shake-table URM model: V = V_ME + 0.7 f_dt·b·h, i.e. 0.7 × HDC tensile strength × overlay section added to the URM
  capacity ([[deng2019-urm-shaking-table-hdc]], Eq. 8). → [[masonry-wall-retrofit]]

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

### Code checks and modified formulas for HDC beams ([[li2021-hdc-beam-shear]], Tables 6–7, Eqs. 6–9, Fig. 9–11)
| Approach | V_test / V_code (new beams) | Note |
|---|---|---|
| ACI 318-14 | **2.0–5.3** (up to 12.88 for deep HDC beams in the database) | strongly conservative |
| EN 1992 | **1.8–4.0** | strongly conservative |
| Modified ACI: V = 0.166·η·δ·√f'c·bd + f_yv·A_sv·d/s; δ_ACI = 0.61λ² − 4.56λ + 10.23; η = (f_t/f_c)_HDC / (f_t/f_c)_concrete | mean V_M/V_test 1.008, COV 0.161, all within ±20% (52 beams) | empirical; λ = a/d |
| Modified EN: δ_EN = −0.27λ² + 0.58λ + 3.16 | mean 0.969, COV 0.168, within ±30% | empirical |

- Database: 44 earlier HDC beams (Deng et al. 16, Zhang 7, Lu 2, Yang 2, Hou 17), f_c 45.7–70.6 MPa, f_t 3.55–6.34 MPa,
  a/d 0.75–4, plus the 8 new beams (Table 6 "prior tests").
- Test/model ratios rise with ρ: longitudinal steel contributes more to shear in HDC beams than in RC (§4.2).

> Synthesis: code conservatism is member-dependent — GB 50010 1.08–1.26 and ACI 318-05 1.40–2.08 for XAUAT short
> columns ([[deng2018-hdc-short-columns]], Table 7) versus ACI 2.0–5.3 and EN 1.8–4.0 for HDC beams
> ([[li2021-hdc-beam-shear]]). Not a conflict (different members, a/d and code editions), but no single "safety
> margin" can be quoted for HDC.

> Synthesis: two design philosophies now coexist. Wang 2019 credits the composite through its tensile strength as an
> explicit truss tie (η·β·σ_t·h·t); Li 2021 credits it only through an empirical strength-ratio factor η and an a/d
> function δ fitted to a database, without σ_tu directly. Deng 2019/2020 use the HDC tensile strength times overlay
> area for masonry. Neither approach has been validated outside its own data set.

> Synthesis: across the primary studies, strain-hardening composites raise shear capacity and change
> brittle diagonal failure into a distributed-cracking, more ductile mode. The gain depends on a/d, the
> number of sides covered, reinforcement and **bond to the substrate**: side layers alone (Wang 2019) never moved
> failure to flexure and thick layers debonded, whereas a four-side jacket (Yuan 2020) did; in columns a plain HDC
> jacket did not, but HDC with bar mesh did (Deng 2017). Code formulas (GB 50010, ACI 318, EN 1992) are conservative
> for HDC members. → [[interface-bond]], [[rc-member-strengthening]]

## Conflicts & open questions
- [[he2024-hdc-research-advances]] cites "Deng & Zhang 2018" for HDC jacketing of cross-shaped short columns;
  [[deng2018-hdc-short-columns]] tests whole-HDC square columns. Very likely the review means Deng, Zhang & Li 2018,
  Eng. Struct. 160:535–45 (ECC-jacketed short columns; cited in [[deng2019-urm-shaking-table-hdc]], ref. [17]) — a
  different, not-ingested paper, not a mis-citation. → [[gaps]], [[rc-member-strengthening]]
- Applicability of RC shear formulas to HDC: partly answered — ACI/EN are 2–5× conservative for HDC beams and
  modified empirical formulas exist ([[li2021-hdc-beam-shear]]); a larger database is needed to fix trends with a/d,
  ρ and ρ_sv (§4.2). Reinforced HDC elements with high reinforcement ratios are little studied (§1).
- Internal inconsistencies in Li 2021: σ_tu 5.83 vs 5.68 MPa; SE-1a 497 vs 519 kN; stated gains "11–38%" vs Table 6
  ([[li2021-hdc-beam-shear]], To verify).
- Softening coefficient of ECC under biaxial tension–compression is unmeasured ([[wang2019-rc-beam-ecc-shear-strengthening]]).
- One beam per case in Yuan 2020; no shear tests on PE-HSHDC members.

## Related
- [[rc-member-strengthening]] · [[unreinforced-hdc-structures]] · [[masonry-wall-retrofit]] · [[interface-bond]] ·
  [[fiber-bridging]] · [[compressive-constitutive-model]]
