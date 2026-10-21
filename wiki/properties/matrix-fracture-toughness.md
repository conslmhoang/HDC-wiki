---
type: property
slug: matrix-fracture-toughness
aliases: [Km, K_IC, matrix toughness, J_tip, crack tip toughness]
tags: [fracture, matrix]
sources: [ranade2015-hshdc-tensile-rate-effects, su2023-rubber-modified-hshdc, ye2021-uhdc-flexural-size-effect, li2002-pva-ecc-interface-tailoring, li1992-steady-state-multiple-cracking, kanda2006-psh-design-criteria, kanda2003-sprayed-ecc, jin2019-hvfa-shcc-structural, chavesfigueiredo2020-printed-shcc, mechtcherine2011-shcc-high-strain-rate, lepech2009-ecc-water-permeability, choi2016-pe-alkali-activated-slag-composite]
updated: 2026-10-21
---

# Matrix Fracture Toughness (Km) & J_tip

## Definition
Km is the fracture toughness of the fiber-free matrix. J_tip ≈ Km²/E, the left-hand side of the
energy criterion. A higher Km raises the first-crack strength and makes strain hardening harder
→ [[strain-hardening]].

## Quantitative evidence
| Source | Matrix | Km (MPa√m) | Method |
|---|---|---|---|
| [[ranade2015-hshdc-tensile-rate-effects]] | Michigan HSHDC, 0.02 / 10 mm/s | 1.10 / 1.31 | notched beam |
| same (Orange 2000; Yang 2008, as cited) | UHPC / ECC | 1.31 / about 0.5 | — |
| [[su2023-rubber-modified-hshdc]] Fig. 7 | GDUT matrix, PR 0 / 10 / 20 / 35% | 0.787 / 0.772 / 0.740 / 0.671 | 40×40×160 mm notched beam |
| [[ye2021-uhdc-flexural-size-effect]] Table 4 | NC / UHDC-1 / UHDC-2 (**composite**, apparent K_IC) | 0.62–0.86 / 2.81–4.94 / 3.41–10.08 | double-K, notched 3PB |

Ye's K_IC is an apparent toughness of the fiber-reinforced composite, not the matrix Km. Do not mix
the two. On an Ashby chart UHDC sits near metals, bamboo and wood
([[ye2021-uhdc-flexural-size-effect]], Fig. 12).

## Key points
- **Rate:** Km rises with loading rate, and σ_fc follows it (Irwin criterion)
  ([[ranade2015-hshdc-tensile-rate-effects]], Fig. 16). → [[strain-rate-effects]]
- **Rubber** lowers Km, which lowers σ_fc and raises PSH_strength ([[su2023-rubber-modified-hshdc]]).
  → [[crumb-rubber]]

> Synthesis: matrix Km ranks about ECC (0.5) < GDUT HSHDC (0.79) < Michigan HSHDC (1.10) ≈ UHPC (1.31).
> This order matches the inverse ductility trend in [[tensile-strain-capacity]].

## Further data (2026-10-16 ingest)
- PVA-ECC matrix (w/c 0.45): measured J_tip = 4.5–7.2 J/m², with 5 J/m² assumed in the analysis
  ([[li2002-pva-ecc-interface-tailoring]], p. 470).
- **Theory:**
  - K_tip = Km at low Vf, otherwise (Ec/Em)Km.
  - A higher Gm needs a proportionally higher V_f^crit.
  - The design lever is Gm/(g·τ·df) ([[li1992-steady-state-multiple-cracking]], p. 2250–2259).
  → [[steady-state-cracking]]

## Flaw size (2026-10-20 ingest)
- Representative flaw c_m = (√π/2 · Km/σ_mu)², about 33 mm for both paste matrices (computed here from
  Km 0.33 / 0.23 MPa√m and σ_mu 1.60 / 1.12 MPa). It is "too large": uncorrected σ_fc is 45% too high,
  and a 0.8 factor brings the error within 10% ([[kanda2006-psh-design-criteria]], Eq. 12, Fig. 12, p. 67–70).
- No flaw-size distribution is measured; a random, interacting-flaw model is needed (p. 68). → [[gaps]]

## Round-4 additions (2026-10-20)
| Source | Matrix | Km (MPa√m) | Note |
|---|---|---|---|
| [[kanda2003-sprayed-ecc]] Table 2 | sprayable ECC matrices, w/c 0.27 / 0.42 / 0.62 | 0.33 / 0.23 / 0.13 (**assumed**, not measured) | Em 23 / 15.9 / 9.4 GPa |
| [[chavesfigueiredo2020-printed-shcc]] Table 3 | printed PVA-SHCC X / Y (flexural-CMOD method) | — | J_tip 16.37 / 7.11 and J_b 430.74 / 260.94, printed as "kJ/m²" (confirmed in PDF Table 3, p. 9) ⚠️ (probably J/m²); J_b > J_tip in both; J_tip 16.37 exceeds LOP × CMOD_LOP ≈ 11.7, so the values are internally inconsistent ⚠️ |

- **Model trend:** J′b/J_tip falls parabolically as Km rises ([[jin2019-hvfa-shcc-structural]], Fig. 1g, Yang 2008
  bridging model with assumed inputs). Raising W/B and FA/C is claimed to lower Km and bond (§2.2, not measured).
  → [[fly-ash]]
- Chaves Figueiredo's J values come from notched-beam flexural stress–CMOD integrals, not the standard
  single-crack J′b, so they are not comparable with [[micromechanical-parameters]] rows.
- **Artificial flaws:** superabsorbent polymer (2.02 kg/m³) is added to TU Dresden SHCC partly to introduce
  micro-defects that trigger multiple cracking ([[mechtcherine2011-shcc-high-strain-rate]], p. 52). This is a
  flaw-size lever, not a Km lever. → [[multiple-cracking]]

## Round-5 additions (2026-10-21)
- **ECC M45 (14 d)**: Km was measured but its value is not given; the energy margin J′b/J_tip ≈ 1.08 is stated as a
  **lower bound**, because the pull-out model behind σ(δ) ignores two-way pull-out and matrix spalling
  ([[lepech2009-ecc-water-permeability]], p. 749). → [[micromechanical-parameters]]
- **No aggregate to keep Km low**: the cementless alkali-activated slag + PE composite uses no sand at all
  ([[choi2016-pe-alkali-activated-slag-composite]], §2.1); Km not measured. Lower W/B (0.26) still gave the highest ε
  (7.50%) and σ_fc (4.87 MPa), so the strength–toughness penalty of a denser matrix was outweighed by bridging
  (Table 7). → [[alkali-activated-binder]], [[water-binder-ratio]]

## Related
- [[strain-hardening]] · [[fracture-process-zone]] · [[micromechanical-parameters]]
