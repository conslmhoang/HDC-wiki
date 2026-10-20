---
type: property
slug: tensile-toughness
aliases: [tensile energy absorption, specific energy, toughness index, gp, Ipost, equivalent tensile strength, tensile fracture energy, G_f]
tags: [tension, energy]
sources: [yang2024-hshdc-uniaxial-tension, zhao2022-ecc-tension-damage-model, mechtcherine2011-shcc-high-strain-rate]
updated: 2026-10-20
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
| [[mechtcherine2011-shcc-high-strain-rate]] Table 2 | PVA-SHCC dumbbell | work of fracture | 8.04 J (10⁻⁵ s⁻¹) → 5.25 J (10⁻² s⁻¹) → 20.03 J (50 s⁻¹) |

- Units differ (energy density in kJ/m³ vs fracture energy per crack area in kJ/m² vs total work in J);
  do not compare across rows without normalising. Zhao's gauge length used for G_f is ⚠️ unverified.
- The work of fracture is non-monotonic with strain rate, like ε at peak. → [[strain-rate-effects]]

## Related
- [[tensile-strain-capacity]] · [[tensile-constitutive-model]] · [[dogbone-uniaxial-tension]] · [[compressive-constitutive-model]]
