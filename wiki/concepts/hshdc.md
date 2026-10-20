---
type: concept
slug: hshdc
aliases: [HSHDC, high-strength high-ductility concrete, high strength-high ductility concrete, R-HSHDC, HS-ECC, PE-HSHDC, PVA-HSHDC, HSDC, NSHSDC, UHP-ECC, UHP-SHCC]
tags: [material-family, high-strength]
sources: [ranade2015-hshdc-tensile-rate-effects, ranade2017-hshdc-impact-resistance, su2023-rubber-modified-hshdc, yang2024-hshdc-uniaxial-tension, he2024-hdc-research-advances, zhang2022-hshdcc-review, yu2018-ecc-direct-tensile-review, yuan2020-nshsdc-beam-strengthening, lee2021-hsdc-wall-emi-impact, sui2018-uhp-ecc-flexural-fatigue, kunieda2010-uhp-shcc-steel-reinforcement, zhou2023-hsecc-elevated-temperature, choi2016-pe-alkali-activated-slag-composite]
updated: 2026-10-21
---

# HSHDC: High-Strength High-Ductility Concrete (four lineages)

## Definition
A strain-hardening cementitious composite that targets **high compressive strength and high tensile
ductility together**. Three research groups use the name "HSHDC" for different materials, and a fourth
(Korea Univ.) uses "HSDC/NSHSDC" for a steel + PE hybrid (added 2026-10-20, see below).
⚔️ See [[terminology-hdc-ecc-shcc]].

## Lineages compared
| | Michigan / ERDC | GDUT (Guangzhou) | Xi'an (Deng) |
|---|---|---|---|
| Sources | [[ranade2015-hshdc-tensile-rate-effects]], [[ranade2017-hshdc-impact-resistance]] | [[su2023-rubber-modified-hshdc]] | [[yang2024-hshdc-uniaxial-tension]] |
| Binder | Class H cement + SF + silica flour; w/cm 0.15 | cement + ultra-fine GGBFS + SF; quartz powder; W/B about 0.155 (computed) | P·O 52.5R + 15–25% FA + 15% SF; W/B 0.14–0.18 |
| Fiber | UHMWPE 2%, 12.7 mm × 28 µm | UHMWPE 2%, 6/12/18 mm × 20 µm | PE 1.5–2.5% (12 mm × 22–40 µm) or PVA 2% (12 mm × 39 µm) |
| Curing | **90 °C** water and air → [[heat-curing]] | 24 h covered + 28 d water, room temperature | standard 20 °C, 95% RH |
| f'c | 166 MPa (51 mm cube), 159 MPa (76 mm cube) | about 86–157 MPa (Ø50 cylinders, read from a chart ⚠️) | matrix about 108–110 MPa at 60 d; PVA-HSHDC 91.6–96.4 MPa at 28 d (100 mm cube) |
| σ_tu | 14.5 MPa | 16.1–19.6 MPa (12–18 mm fiber) | 4.5–7.7 MPa (PE) |
| ε_tu | 3.4% (as quoted in 2017) or 4.2% (2015, 10⁻⁴ s⁻¹) ⚔️ | 2.9–5.7% (12–18 mm fiber) | 3.6–6.5% (PE22); 0.23–0.30% (PVA39) |

Values: [[ranade2017-hshdc-impact-resistance]] p. 26; [[ranade2015-hshdc-tensile-rate-effects]] Table 2;
[[su2023-rubber-modified-hshdc]] Table 4, Fig. 6a; [[yang2024-hshdc-uniaxial-tension]] Tables 4–6.
Full rows are in [[mix-designs]] and [[mechanical-results]].

## Key points
- **Heat curing is not necessary.** GDUT reaches up to about 157 MPa and 3.8% at room temperature
  ([[su2023-rubber-modified-hshdc]]). → [[heat-curing]]
- **PE beats PVA in a high-strength matrix.** In the Xi'an matrix, PVA-HSHDC reaches only
  0.23–0.30% strain, against up to 6.48% for PE ([[yang2024-hshdc-uniaxial-tension]], Table 6).
  → [[pe-fiber]], [[pva-fiber]]
- **Dynamic and impact behaviour** (Michigan HSHDC):
  - From 10⁻⁴ to 10 s⁻¹, σ_tu rises 42% and ε_tu falls to about 2.7–2.9%
    ([[ranade2015-hshdc-tensile-rate-effects]]).
  - Slabs survive 20 drop-weight impacts without punching, where FR-UHPC fails
    ([[ranade2017-hshdc-impact-resistance]]).
  → [[strain-rate-effects]], [[impact-resistance]]
- **Modification with waste rubber** (powder rubber replacing quartz powder, ≤ 20 vol.%) raises
  ε_tu up to 5.7% while keeping f'c above about 100 MPa ([[su2023-rubber-modified-hshdc]]).
  → [[crumb-rubber]]

## The wider HSHDCC field ([[zhang2022-hshdcc-review]])
- The review defines HSHDCC as SHCC with **f'c > 100 MPa and ε_tu > 3%**. It treats HSHDC,
  UHP-ECC, HS-SHCC, HS-ECC, SHUHPC, UHS-UHDCC and others as members (p. 1–2).
- The first HSHDCC credited is Ranade et al. 2011 (Michigan): 14-d f'c 160 MPa, ε_tu 3.5%, PE with
  L/d 334 (38 µm) (as cited, p. 2). The Michigan PE was later changed to 28 µm (L/d 454).
- The field is now dominated by Chinese groups (Yu KQ, Tongji/PolyU; Huang BT; Lei & Guo,
  Southeast Univ.). Notable results (as cited):

  | Study | f'c | ε_tu | Note |
  |---|---|---|---|
  | Huang 2021 | > 210 MPa | > 5% | 90 °C water curing |
  | Li Y 2020 | 115–131 MPa | 11% | river sand |
  | Yu K 2017 | 122 MPa | 8.5% | σ_tu 18.2 MPa |

- There is **no field deployment** yet (p. 2).
- **PE is "mandatory"** in HSHDCC; PVA bonds too strongly and ruptures (p. 4, 16). → [[pe-fiber]]

> Synthesis:
> - The Michigan lineage gets strength through heat curing and a dense VHSC matrix.
> - The Chinese lineages use ambient-curable binders (FA, GGBFS) and finer PE fibers.
> - Xi'an "HSHDC" sits closer to normal HDC in tensile strength (≤ 7.7 MPa) but has higher ε_tu.
>
> Report the lineage whenever you quote HSHDC values.

## Fourth lineage: Korea University (Yoon) HSDC / NSHSDC (2026-10-20 ingest)
| | Korea Univ. (Yoon) |
|---|---|
| Sources | [[yuan2020-nshsdc-beam-strengthening]] ("NSHSDC", no-slump); [[lee2021-hsdc-wall-emi-impact]] ("HSDC", same mix) |
| Binder | cement + SF + silica filler + silica sand; W/B 0.172 |
| Fiber | **hybrid**: 1.0 vol.% straight steel (19.5 mm × 0.2 mm) + 0.5 vol.% PE (12 mm × 31 µm) → [[hybrid-fiber]], [[pe-fiber]] |
| Curing | room temperature (20 °C, 60% RH), no heat |
| f'c | 123.4 MPa ([[yuan2020-nshsdc-beam-strengthening]], Table 5); 122.3 MPa ([[lee2021-hsdc-wall-emi-impact]]), 28 d |
| σ_t | 9.7 MPa direct tension ([[yuan2020-nshsdc-beam-strengthening]], Table 5) |
| ε_tu | **not reported** in either paper; "> 2.9%" quoted from the group's earlier papers ([[yuan2020-nshsdc-beam-strengthening]], §1) ⚠️ |

- Steel is kept at 1.0 vol.% so that PE drives strain hardening; UHPFRC typically uses > 1.5% steel
  ([[lee2021-hsdc-wall-emi-impact]], §1).
- The authors claim about 76% higher σ_t and 53.7% lower ε than typical PVA-ECC (Li et al. 2001, as cited in
  [[yuan2020-nshsdc-beam-strengthening]], §1).
- Uses: room-cured, shape-holding jackets for NSC beams (+8% to +40% peak load; no jacket delaminated)
  ([[yuan2020-nshsdc-beam-strengthening]], Table 8) → [[rc-member-strengthening]], [[interface-bond]]; 5–20 mm
  skins on NC panels for impact and EMI shielding ([[lee2021-hsdc-wall-emi-impact]]) → [[impact-resistance]].
- Partly closes the "bond to existing concrete" gap: slant shear τ up to 21.4 MPa at 28 d
  ([[yuan2020-nshsdc-beam-strengthening]], Table 7). → [[interface-bond]]

## Other high-strength strain-hardening composites (not called HSHDC)
| Term | Group | f'c (MPa) | σ_tu (MPa) | ε (%) | Fiber | Meets HSHDCC bar (> 100 MPa, > 3%)? | Source |
|---|---|---|---|---|---|---|---|
| UHP-ECC | Shenzhen / PolyU | 102.8 (28 d) / 120.7 (90 d), 100 mm cube | up to 12 | > 8 (abstract) | PE | yes | [[sui2018-uhp-ecc-flexural-fatigue]], abstract, Fig. 4 |
| UHP-SHCC | Nagoya (Kunieda) | 95 (Ø50 cylinder, 28 d) | 6.5 | 1.5 (dumbbell, at ultimate load) | PE 1.5%, 6 mm × 12 µm | no | [[kunieda2010-uhp-shcc-steel-reinforcement]], §2, Table 3 |
| HSECC | Zhou 2023 | 83.1 | not tested | not tested; softens in bending | PVA + steel | no (not strain hardening) | [[zhou2023-hsecc-elevated-temperature]] |

- UHP-SHCC loses strain hardening in unreinforced 50 mm-thick tension members (ε about 85% lower than dumbbells),
  and light steel reinforcement (ρs 0.3%) restores it ([[kunieda2010-uhp-shcc-steel-reinforcement]], Table 3).
  → [[multiple-cracking]], [[size-effect]]
- UHP-ECC crack width < 160 µm in tension ([[sui2018-uhp-ecc-flexural-fatigue]], Fig. 5), within the
  80–200 µm band noted for PE-based HSHDC. → [[crack-width]], [[fatigue]]

> Synthesis: the four lineages now differ in **fiber system** as well as curing: Michigan, GDUT and Xi'an use
> mono-PE (or PVA), Korea Univ. uses steel + PE. Only Michigan, GDUT and Xi'an report tensile strain capacity in
> the ingested papers; the Korean HSDC must be cited as "ductility claimed, not shown" until refs 12–13 of
> [[yuan2020-nshsdc-beam-strengthening]] are ingested.

## Comparison with a cementless PE composite (2026-10-21)
- [[choi2016-pe-alkali-activated-slag-composite]] (co-authored by Ranade and Li) quotes Michigan HSHDC as f'c 166 MPa, first crack 8.3 MPa, σ_tu
  14.5 MPa, ε 3.4% (Ranade et al. 2013, as cited, §1), and compares σ_tu/f'c: 23.8% for its alkali-activated slag + PE
  composite (M26) vs 8.7% for HSHDC (§3.3). The AAS composite (55 MPa) is **not** high-strength; it shows that HSHDC-level
  σ_tu (13 MPa) does not need an HSHDC-level matrix. → [[alkali-activated-binder]], [[uhdc]]
- First-crack 8.3 MPa here vs 8.1 MPa in [[ranade2015-hshdc-tensile-rate-effects]] (Table 2): minor.

## Conflicts & open questions
- ⚔️ Quasi-static ε_tu of Michigan HSHDC: 3.4% vs 4.2%, plus 3.5% at 14 d in the 2011 version
  (as cited in [[zhang2022-hshdcc-review]]); 3.4% is quoted again in [[choi2016-pe-alkali-activated-slag-composite]] (via Ranade 2013) → [[tensile-strain-capacity]], [[gaps]]
- No study compares the four lineages directly, or tests their durability.
- Tensile strain capacity of the Korean HSDC/NSHSDC is not shown in the ingested papers.

## Related
- [[terminology-hdc-ecc-shcc]] · [[uhdc]] · [[uhpc-vhsc]] · [[hybrid-fiber]] · [[interface-bond]] · [[mix-designs]] · [[mechanical-results]]
