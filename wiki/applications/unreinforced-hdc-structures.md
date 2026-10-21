---
type: application
slug: unreinforced-hdc-structures
aliases: [steel-free structures, UHDCC frames, reinforcement-free, whole-HDC members, R/SHCC members]
tags: [application]
sources: [he2024-hdc-research-advances, ye2021-uhdc-flexural-size-effect, xue2023-shcc-structural-review, deng2018-hdc-short-columns, kunieda2010-uhp-shcc-steel-reinforcement, li2021-hdc-beam-shear]
updated: 2026-10-21
---

# Unreinforced (Steel-Free) and Whole-HDC Members

This page covers members made **entirely of HDC** — without steel (steel-free) or with reduced steel — as opposed
to HDC layers on existing members ([[rc-member-strengthening]]).

## Steel-free structures
- Examples cited in [[he2024-hdc-research-advances]] (p. 20):
  - steel-free UHDCC frames (Yu 2018);
  - an unreinforced UHDC pavilion at the 2021 China Flora Expo.
- The review's authors argue that 3–5% ductility is not enough for unreinforced structural use,
  which motivates UHDC (p. 20). → [[uhdc]]
- UHDC is named for steel-like deformability ([[ye2021-uhdc-flexural-size-effect]], p. 2).
  It shows no flexural size effect up to 150 mm. → [[size-effect]]
- **Unreinforced SHCC beam** (1800 mm, 150 × 200 mm, 4PB): multiple cracking then localisation, with fewer cracks
  than in dogbone tension; first cracking ≈ 15 kN, peak ≈ 19 kN at ≈ 4 mm, span 1600 mm, load points 300 mm apart
  (read from Fig. 2, p. 4; as cited in [[xue2023-shcc-structural-review]], Section 3.1).
- **Unreinforced UHP-SHCC tension members** (50 × 200 × 900 mm; PE 1.5 vol.%, f'c 95 MPa): ultimate strain 0.23–0.24%
  vs 1.5% in 13 mm dumbbells, and brittle failure — strain hardening is lost at practical thickness
  ([[kunieda2010-uhp-shcc-steel-reinforcement]], Table 3, §4.1). → [[dogbone-uniaxial-tension]]

## Members cast wholly in HDC with (reduced) steel
| Source | Material (authors' term) | Member | Key result | Location |
|---|---|---|---|---|
| [[deng2018-hdc-short-columns]] | HDC (XAUAT, 2% PVA, ε_tu ≈ 1.0%) | 6 square 250 mm short columns, longitudinal bars + stirrups, reversed cyclic load | vs RC: P_m +24%, μ +37%, θ_u +72%; ductile shear failure, no spalling; stirrups −20% / −33% cost only 4.4% / 6.6% of P_m | Tables 5–6, p. 8 |
| [[li2021-hdc-beam-shear]] | HDC (Henan / XAUAT, 2% PVA, ε_tu 0.968%, f_cu 70.55 MPa) | 8 beams 120 × 180 mm with longitudinal bars and stirrups (ρ_sv 0.40–0.79%), a/d 1 and 2, vs 2 RC beams | peak 471–520 vs 393 kN (a/d 1), 285–354 vs 275 kN (a/d 2); ductile shear failure (direct shear, shear compression or shear tension) without spalling; RC failed by diagonal compression with crushing; ACI 318 / EN 1992 underestimate capacity 2.0–5.3× / 1.8–4.0× | Tables 4, 6–7, §3.1–3.2 |
| [[kunieda2010-uhp-shcc-steel-reinforcement]] | UHP-SHCC (PE 1.5 vol.%) | 50 × 200 × 900 mm tension members with D6 bars, ρs 0.3–1.2% | ρs 0.3% restores strain hardening: 119 vs 43 cracks, spacing 4.6 vs 12 mm, ε 1.58 vs 0.24%; little change beyond ρs 0.6%; distributed cracking needs P_u ≥ about 1.5 P_cr | Table 3, Figs. 15–16, §4.4 |
| [[xue2023-shcc-structural-review]] (as cited) | SHCC | beam without stirrups, 25 mm bar | sudden diagonal shear failure at 9.8 MPa (a/d 2) and 7.0 MPa (a/d 3) nominal shear stress; crack angle 33.5° / 28°; smooth fracture surface; displacement at peak ≈ 4 mm (2-100) / ≈ 7 mm (3-100) (read from Fig. 3); overall depth 200 mm | Section 3.2, p. 5; Figs. 3–5 |

- Kunieda 2010 load–strain response has three stages: uncracked; cracking with steel activation; steel yielded and fibres
  carry the increase (Fig. 9). Steel share of load at yield 18.5% (ρs 0.3%) to 49.8% (1.2%) (Fig. 17).
- → [[shear-behaviour]] for the shear mechanisms of HDC members.

> Synthesis: in tension members of practical thickness, a small amount of steel (ρs ≈ 0.3%) is what lets PE UHP-SHCC
> realise its dumbbell ductility (Kunieda 2010). In shear-critical members, HDC partly replaces stirrups (Deng 2018)
> and HDC beams with stirrups fail in a ductile shear mode without spalling (Li 2021), but SHCC beams with no stirrups
> still fail suddenly in shear (Xue 2023, as cited). Both XAUAT-lineage member studies use an HDC with only ≈ 1% ε_tu. Truly steel-free structural use
> is so far reported only for UHDC (second-hand).

## Conflicts & open questions
- Minimum reinforcement needed to secure material-level ductility in members is not established
  ([[kunieda2010-uhp-shcc-steel-reinforcement]], §1). → [[gaps]]
- Applicability of RC shear-strength formulas to HDC: ACI/EN are 2–5× conservative for HDC beams; modified empirical
  formulas proposed ([[li2021-hdc-beam-shear]], Eqs. 6–9). → [[shear-behaviour]]

## Related
- [[uhdc]] · [[3d-printed-hdc]] · [[rc-member-strengthening]] · [[size-effect]] · [[multiple-cracking]] · [[shear-behaviour]]
