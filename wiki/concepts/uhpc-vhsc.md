---
type: concept
slug: uhpc-vhsc
aliases: [UHPC, UHPFRC, FR-UHPC, Cor-Tuf, VHSC, very-high-strength concrete]
tags: [comparison-family, high-strength]
sources: [ranade2017-hshdc-impact-resistance, yang2024-hshdc-uniaxial-tension, ranade2015-hshdc-tensile-rate-effects, he2024-hdc-research-advances, kanakubo2006-dfrcc-tensile-test-method, qian2007-shcc-inverse-tensile-strain, kunieda2010-uhp-shcc-steel-reinforcement, vanzijl2010-shcc-durability, lee2021-hsdc-wall-emi-impact]
updated: 2026-10-20
---

# UHPC / FR-UHPC (comparison family)

## Definition
High-compressive-strength concretes with very dense matrices. They are **not** HDC unless tensile
strain hardening is shown. → [[terminology-hdc-ecc-shcc]]

## Key points
- **Cor-Tuf** (ERDC FR-UHPC) has the same binder as Michigan HSHDC but contains 3.26% hooked steel
  fiber (30 mm × 550 µm) and more sand. It is tension-softening and deflection-hardening
  ([[ranade2017-hshdc-impact-resistance]], Tables 1–2).
- The authors list four limits of tension-softening FR-UHPC under impact
  ([[ranade2017-hshdc-impact-resistance]], p. 25):
  1. back-face spalling and scabbing;
  2. damage localises along yield lines;
  3. it needs at least 3% fibers and high f'c;
  4. strain incompatibility with rebar.
- UHPC has no weak ITZ. Its freeze–thaw resistance is governed by W/C
  ([[he2024-hdc-research-advances]], p. 14, 18).

## Quantitative evidence
| Source | Material | f'c (MPa) | σ_tu (MPa) | ε_tu (%) | Note |
|---|---|---|---|---|---|
| [[ranade2017-hshdc-impact-resistance]] | Cor-Tuf | 201 (51 mm cube) | 11.2 | 0.12 | softens beyond about 0.15% strain |
| same | Cor-Tuf, large 76 × 76 mm dogbone | — | 7.6 | 0.09 | size effect |
| [[yang2024-hshdc-uniaxial-tension]], p. 8, 13 (Wille 2014 as cited) | UHPC | — | — | < 0.5 | energy g about 50 kJ/m³ ⚠️ (Conclusion 2 says < 100) |
| [[ranade2015-hshdc-tensile-rate-effects]] (Orange 2000 as cited) | UHPC matrix | — | — | — | Km 1.31 MPa√m |
| [[kanakubo2006-dfrcc-tensile-test-method]], Tables 5, 6, 9 | UFC (Ductal), 2% steel, W/B 0.22 | 198 | 15.27 (JCI T1 thin plate) / 7.18 (Ø100 cylinder) | 0.53 / 0.045 | strain depends strongly on specimen type |

## Placement in the HPFRCC family (2026-10-20 ingest)
- **Two HPFRCC classes** (RILEM TC 208-HFC view): SHCC with f'c 25–60 MPa and ε > 3%, whose durability comes from
  crack control; UHPFRC with f'c 180–240 MPa and low–moderate strain, whose durability comes from a dense matrix.
  Both use 1–3% fiber ([[vanzijl2010-shcc-durability]], p. 261).
- **UHP-SHCC** is positioned between ordinary SHCC and ordinary UHPFRC ([[kunieda2010-uhp-shcc-steel-reinforcement]], Fig. 1).
  → [[hshdc]]
- Korea Univ. HSDC keeps steel at 1.0 vol.% so that PE drives hardening, whereas UHPFRC typically uses > 1.5% steel
  ([[lee2021-hsdc-wall-emi-impact]], §1). → [[hybrid-fiber]]
- UFC beams reach 1.7× the shear capacity of PVA-ECC beams with the same reinforcement, with similar crack patterns
  ([[kanakubo2006-dfrcc-tensile-test-method]], Fig. 1, p. 3–4). → [[shear-behaviour]]
- ⚠️ [[qian2007-shcc-inverse-tensile-strain]] groups Ductal (strain capacity about 0.5%) with "SHCCs". Following
  the wiki rule, Ductal stays on this page; it is a DFRCC/UHPFRC, not HDC. → [[terminology-hdc-ecc-shcc]]

> Synthesis: Ductal's tensile "strain capacity" ranges from 0.045% to 0.53% with specimen type alone
> ([[kanakubo2006-dfrcc-tensile-test-method]]), so a single UHPC strain value should never be compared with HDC
> without stating the test geometry. → [[dogbone-uniaxial-tension]]

## Related
- [[hshdc]] · [[impact-resistance]] · [[compressive-strength]] · [[terminology-hdc-ecc-shcc]]
