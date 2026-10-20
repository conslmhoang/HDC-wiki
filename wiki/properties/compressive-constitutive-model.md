---
type: property
slug: compressive-constitutive-model
aliases: [compressive stress-strain curve, compressive toughness, W_cu, compressive damage model, Weibull damage model, compressive deformability]
tags: [compression, modelling, toughness]
sources: [deng2015-hdc-compressive-toughness, deng2018-hdc-compressive-constitutive, deng2018-hdc-short-columns, zhang2022-hshdcc-review, chai2023-hdc-ambient-temperature, tabrizikahou2022-masonry-ecc-sma-retrofit]
updated: 2026-10-20
---

# Compressive Stress–Strain Behaviour, Toughness and Constitutive Models

## Definition
The full uniaxial compressive stress–strain curve of HDC, including the post-peak branch, and the indices
and models that describe it. Peak strength alone is on [[compressive-strength]].

## Key points
- **Failure mode:** the fiber-free matrix splits into columns and loses capacity at once; PVA-HDC fails
  through one inclined shear crack, stays intact, and keeps **10–20% residual capacity** at large
  deformation ([[deng2015-hdc-compressive-toughness]], p. 2, 4; [[deng2018-hdc-compressive-constitutive]], p. 3, Fig. 2).
- **Damage stages:** micro-cracks at 50–60% of peak, a main crack at ≥ 80%, slow post-peak decay
  ([[deng2015-hdc-compressive-toughness]], p. 2).
- **Mechanism:** fiber bridging across longitudinal splitting cracks acts as lateral confinement. With a
  Mander model and σ_t = f_t = 5.7 MPa, the predicted peak strain 0.0079 matches 0.0080 measured
  ([[deng2015-hdc-compressive-toughness]], Eqs. 5–6). Once the lateral strain exceeds the HDC ultimate tensile
  strain, fibers pull out or rupture and a major crack forms ([[deng2018-hdc-compressive-constitutive]], Fig. 3).
  → [[fiber-bridging]]

## Quantitative evidence
XAUAT PVA-HDC (PVA 12 mm × 39 µm), 100 × 100 × 300 mm prisms, W/B 0.29, FA 50% unless noted:

| Source | Mix | σ0 (MPa) | ε0 (%) | Post-peak | Note |
|---|---|---|---|---|---|
| [[deng2015-hdc-compressive-toughness]] Table 3 | matrix / 1.0 / 1.5 / 2.0% PVA | 64.0 / 50.3 / 56.9 / 62.3 (computed from loads) | 0.22 / 0.74 / 0.67 / 0.80 | W_cu^0.85 0.065 / 0.187 / 0.198 / 0.266 N/mm² | about 10 months |
| [[deng2018-hdc-compressive-constitutive]] Table 3 | matrix / 1.0 / 1.5 / 2.0% PVA | 63.06 / 50.28 / 56.85 / 62.25 | 0.213 / 0.569 / 0.601 / 0.672 | ε0.2 — / 0.864 / 1.128 / 1.407% | age n.r. ⚠️ |
| same | W/B 0.26 / 0.32 (2%) | 56.04 / 52.84 | 0.633 / 0.652 | ε0.2 1.116 / 1.276% | optimum W/B 0.29 |
| same | FA 40 / 60% (2%) | 64.43 / 53.64 | 0.561 / 0.634 | ε0.2 0.887 / 1.380% | peak strain highest at 50% |
| same | S/B 0.24 / 0.48 (2%) | 51.96 / 56.01 | 0.648 / 0.556 | ε0.2 1.357 / 0.810% | optimum S/B 0.36 |
| [[zhang2022-hshdcc-review]] p. 7–9 (as cited) | HSHDCC | > 100 | 0.28–0.41 | — | compressive strain capacity 2.8–4.1‰ |

- Fiber 1 → 2%: ε0.85 / ε0.5 / ε0.2 rise by 33.06 / 39.73 / 62.85% ([[deng2018-hdc-compressive-constitutive]], Fig. 5a).
- HDC peak strain is about 3× the matrix (2.61–3.15× in 2018; "3.41–3.67×" stated in 2015, which does not match
  its own Table 3 ⚠️).

## Equivalent compressive toughness index ([[deng2015-hdc-compressive-toughness]])
- W_cu = Ω_u / (A·l), the area under the load–deformation curve up to the post-peak point where load falls to
  u·P_max, per unit volume; u = 0.85 / 0.50 / 0.20 (Eqs. 2–3).
- W_cu^0.85 rises 2.88–4.09× over the matrix (Table 4) and is linear in fiber content:
  W_cu^0.85 = W_cu,0^0.85 + 0.10φ, φ in vol.% (Eq. 4, Fig. 6).
- Design idea: the bridging stress of 5.7 MPa is equivalent to a stirrup ratio of 3.03% in a 500 mm column, so
  HDC is proposed for plastic-hinge regions to reduce ties (Eqs. 7–9). → [[rc-member-strengthening]], [[shear-behaviour]]

## Weibull damage constitutive model ([[deng2018-hdc-compressive-constitutive]], Eqs. 6–10)
- σ = E(1 − D)ε with
  - D = 0 for ε < γ;
  - D = 1 − exp[−((ε − γ)/η)^m] for γ ≤ ε ≤ β;
  - D = D_u (constant) for ε > β, giving a residual plateau (1 − D_u)σ0.
- Fitted over 9 HDC mixes (Table 4): γ/ε0 0.80–0.84; β/ε0 1.20–1.43; D at β 0.79–0.89 (mean 0.85);
  m 2.56–5.78; η 0.19–0.38 (×10⁻³, units ⚠️). Simplified: **γ = 0.8ε0, β = 1.3ε0** (Eq. 10).
- More fiber lowers m and raises η (more enclosed energy).
- Fit (mean R): new model 0.984; Li & Liu 2014 rational model 0.983; Xu 2009 polynomial 0.958. Only the new
  model reproduces the residual plateau; the others decay to zero (Fig. 7).

## Other uses in the wiki
- FE input for ECC in Abaqus CDP: compression to 62.78 MPa at inelastic strain 0.017
  ([[tabrizikahou2022-masonry-ecc-sma-retrofit]], Tables 4–5).
- Link-slab design for PVA-HDC: ignore temperature effects in compression ([[chai2023-hdc-ambient-temperature]]).
- HDC columns have lower initial stiffness than RC because E_HDC < E_concrete ([[deng2018-hdc-short-columns]], Fig. 10).

> Synthesis: in compression, PVA fibers trade a little peak strength (matrix 63 MPa vs 50–62 MPa) for about
> 3× peak strain, 3–4× toughness and a residual plateau. This compressive ductility, not tensile strain
> capacity, is what the XAUAT group exploits in columns and plastic hinges.

## Conflicts & open questions
- ⚔️ Same peak loads but different peak strains for mixes 1–4 in [[deng2015-hdc-compressive-toughness]]
  (0.22 / 0.74 / 0.67 / 0.80%) and [[deng2018-hdc-compressive-constitutive]] (0.213 / 0.569 / 0.601 / 0.672%);
  matrix load 640.45 vs 630.55 kN. → [[gaps]]
- Curing and test age are not reported in the 2018 paper; all data come from one group and one PVA fiber.
- No compression stress–strain models for PE-based HSHDC in the wiki.

## Related
- [[compressive-strength]] · [[tensile-constitutive-model]] · [[tensile-toughness]] · [[shear-behaviour]] · [[fiber-bridging]]
