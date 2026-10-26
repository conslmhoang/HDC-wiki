---
type: property
slug: tensile-toughness
aliases: [tensile energy absorption, specific energy, toughness index, gp, Ipost, equivalent tensile strength, tensile fracture energy, G_f]
tags: [tension, energy]
sources: [yang2024-hshdc-uniaxial-tension, zhao2022-ecc-tension-damage-model, mechtcherine2011-shcc-high-strain-rate, choi2016-pe-alkali-activated-slag-composite, hieu2023-aas-extremely-ductile-22pct, huy2023-egc-activator-pretreatment]
updated: 2026-10-26
---

# Tensile Toughness Indices

## Definition
Existing toughness indices (ASTM C1018, JSCE-SF4, ASTM C1609) are flexural only. Yang et al. propose
three indices based on the uniaxial tension curve ([[yang2024-hshdc-uniaxial-tension]], Eqs. 4–6, Fig. 14):

| Index | Formula | Meaning |
|---|---|---|
| σe,k | ∫₀^εk σ dε / εk | equivalent tensile strength up to εk |
| gp | ∫₀^εp σ dε | energy density to peak |
| Ipost | ∫εp^εk σ dε / ∫₀^εk σ dε | post-peak share of energy |

εk is the post-peak strain where σ = 0.85σp (⚠️ definition read from Fig. 14).

**Tensile fracture energy** (Zhao et al.): G_f split into a hardening part G_f,A (to peak) and a softening
part G_f,B (peak to rupture) ([[zhao2022-ecc-tension-damage-model]], Eqs. 1–4).

For the compression counterpart (equivalent compressive toughness W_cu) see [[compressive-constitutive-model]].

## Quantitative evidence
| Source | Material | Index | Value |
|---|---|---|---|
| [[yang2024-hshdc-uniaxial-tension]] Table 7 | Xi'an HSHDC, 13 mixes | gp / σe,0.85 / Ipost | 9.26–366.44 kJ/m³ / 4.08–6.55 MPa / 0.049–0.459 |
| same (Wille 2014, as cited) | UHPC | gp | about 50 kJ/m³ ⚠️ |
| [[zhao2022-ecc-tension-damage-model]] Table 3 | PVA-ECC (FA/C 2.0, SF), Vf 1–2%, W/B 0.24–0.28 | G_f,N | 3.5–11.1 kJ/m² (computed from Table 3); +217% for Vf 1 → 2%; +50% for W/B 0.24 → 0.28 |
| [[choi2016-pe-alkali-activated-slag-composite]] Table 6 | cementless AAS + 1.75% PE (M26) vs PVA-ECC (Li 2001), PVA-AAS (Lee 2012), HSHDC (Ranade 2013), as cited | "tensile toughness" to end of hardening | 0.0067 vs 0.0025 / 0.0019 / 0.0038 "MPa·mm/mm" ⚠️ (units/magnitude doubtful: area under a 13 MPa × 7.5% curve is ≈ 0.6 MPa) |
| [[mechtcherine2011-shcc-high-strain-rate]] Table 2 | PVA-SHCC dumbbell | work of fracture | 8.04 J (10⁻⁵ s⁻¹) → 5.25 J (10⁻² s⁻¹) → 20.03 J (50 s⁻¹) |
| [[hieu2023-aas-extremely-ductile-22pct]] Table 4 | ED-AASC M0 / M1 / M2 (1.75% PE, 28 d) | E_t = area to peak stress ("MPa·m/m" = MJ/m³) | 0.64 / 1.38 / 1.29 |
| [[huy2023-egc-activator-pretreatment]] Table 4 | fly-ash ED-EGC WP / CP (28 d) | Ut = area to fts / ε_sc ("MPa·m/m") | 0.73 / 0.83 |

- Units differ (energy density in kJ/m³ vs fracture energy per crack area in kJ/m² vs total work in J);
  do not compare across rows without normalising. Zhao's gauge length used for G_f is ⚠️ unverified.
- Choi 2016's ratios (2.7× PVA-ECC, 1.8× HSHDC) are internally consistent but the absolute values cannot be used until
  the unit is verified ([[choi2016-pe-alkali-activated-slag-composite]], To verify). → [[alkali-activated-binder]]
- The CNU 2023 values (0.64–1.38 MJ/m³) are consistent with ≈ 5.5–8 MPa × 10–22% strain (computed check) and so are in the
  same unit family as Yang 2024's gp (kJ/m³ ×1000); they are ≈ 200× Choi 2016's printed numbers, which supports the doubt about
  that unit ([[choi2016-pe-alkali-activated-slag-composite]]).
- The work of fracture is non-monotonic with strain rate, like ε at peak. → [[strain-rate-effects]]

## Related
- [[tensile-strain-capacity]] · [[alkali-activated-binder]] · [[tensile-constitutive-model]] · [[dogbone-uniaxial-tension]] · [[compressive-constitutive-model]]
