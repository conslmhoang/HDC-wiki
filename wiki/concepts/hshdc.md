---
type: concept
slug: hshdc
aliases: [HSHDC, high-strength high-ductility concrete, high strength-high ductility concrete, R-HSHDC, HS-ECC, PE-HSHDC, PVA-HSHDC]
tags: [material-family, high-strength]
sources: [ranade2015-hshdc-tensile-rate-effects, ranade2017-hshdc-impact-resistance, su2023-rubber-modified-hshdc, yang2024-hshdc-uniaxial-tension, he2024-hdc-research-advances, zhang2022-hshdcc-review, yu2018-ecc-direct-tensile-review]
updated: 2026-10-06
---

# HSHDC: High-Strength High-Ductility Concrete (three lineages)

## Definition
A strain-hardening cementitious composite that targets **high compressive strength and high tensile
ductility together**. Three research groups use the name for different materials.
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

## Conflicts & open questions
- ⚔️ Quasi-static ε_tu of Michigan HSHDC: 3.4% vs 4.2%, plus 3.5% at 14 d in the 2011 version
  (as cited in [[zhang2022-hshdcc-review]]) → [[tensile-strain-capacity]], [[gaps]]
- No study compares the three lineages directly, or tests their durability.

## Related
- [[terminology-hdc-ecc-shcc]] · [[uhdc]] · [[uhpc-vhsc]] · [[mix-designs]] · [[mechanical-results]]
