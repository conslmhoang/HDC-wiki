---
type: concept
slug: tensile-constitutive-model
aliases: [tensile stress-strain model, trilinear model, constitutive law]
tags: [modelling, tension]
sources: [yang2024-hshdc-uniaxial-tension, ranade2017-hshdc-impact-resistance, chai2023-hdc-ambient-temperature]
updated: 2026-10-20
---

# Tensile Constitutive Models

## Key points
- **Trilinear model** for HSHDC ([[yang2024-hshdc-uniaxial-tension]], Eq. 1, Fig. 5):
  - σ = E1·ε for ε ≤ εcr
  - σ = σcr + E2(ε − εcr) for εcr < ε ≤ εp
  - σ = σp − E3(ε − εp) for ε > εp
- Reported E1 is 33.4–46.8 GPa. E2 and E3 are **not reported**, and the model is not validated.
  ⚠️ In Table 6, E1·εcr ≠ σcr (a 4–7× mismatch).
- **For FE impact simulation:** LS-Dyna with a plasticity-based model; HSHDC tensile rate effects
  taken from [[ranade2015-hshdc-tensile-rate-effects]]; compressive rate effects assumed equal to
  UHPC ([[ranade2017-hshdc-impact-resistance]], p. 26, 31–32). → [[impact-resistance]]

## Bilinear model for PVA-HDC ([[chai2023-hdc-ambient-temperature]], Eqs. 2–3, Table 7)
- σ = E_tc·ε up to the nominal first crack ε_ntc; then σ = σ_ntc + E_tu(ε − ε_ntc) up to ε_tu.
- E_tu is fitted to the "valleys" of the hardening branch, by analogy with the lower yield point of mild steel.
- Parameters over −30 to 60 °C: E_tc 10.2–16.8 GPa, E_tu 57.8–95.4 MPa, σ_ntc 1.56–3.28 MPa.
- Intended for link-slab design: ignore temperature in compression, use temperature-specific tension parameters.

## Related
- [[dogbone-uniaxial-tension]] · [[tensile-strain-capacity]] · [[tensile-toughness]]
