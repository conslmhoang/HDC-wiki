---
type: concept
slug: tensile-constitutive-model
aliases: [tensile stress-strain model, trilinear model, bilinear model, constitutive law, damage model, JSCE HPFRCC model]
tags: [modelling, tension]
sources: [yang2024-hshdc-uniaxial-tension, ranade2017-hshdc-impact-resistance, chai2023-hdc-ambient-temperature, zhao2022-ecc-tension-damage-model, kanakubo2006-dfrcc-tensile-test-method, kunieda2006-hpfrcc-japan-applications, qian2007-shcc-inverse-tensile-strain, wang2019-rc-beam-ecc-shear-strengthening, tabrizikahou2022-masonry-ecc-sma-retrofit, deng2018-hdc-compressive-constitutive]
updated: 2026-10-20
---

# Tensile Constitutive Models

## Model families
Kanakubo lists six σ–ε forms by number of unknowns ([[kanakubo2006-dfrcc-tensile-test-method]], Fig. 15, p. 13):

| Form | Unknowns | Note |
|---|---|---|
| rigid-plastic | 2 | adequate for structural design |
| elastic-plastic | 3 | adequate for structural design |
| bilinear | 4 | adequate for structural design |
| trilinear | 5 | adds softening |
| multi-linear / multi-function | any | — |

- σ–ε models cannot give crack width (p. 13). → [[crack-width]]

## Trilinear model for HSHDC ([[yang2024-hshdc-uniaxial-tension]], Eq. 1, Fig. 5)
- σ = E1·ε for ε ≤ εcr
- σ = σcr + E2(ε − εcr) for εcr < ε ≤ εp
- σ = σp − E3(ε − εp) for ε > εp
- Reported E1 is 33.4–46.8 GPa. E2 and E3 are **not reported**, and the model is not validated.
  ⚠️ In Table 6, E1·εcr ≠ σcr (a 4–7× mismatch).

## Bilinear model for PVA-HDC ([[chai2023-hdc-ambient-temperature]], Eqs. 2–3, Table 7)
- σ = E_tc·ε up to the nominal first crack ε_ntc; then σ = σ_ntc + E_tu(ε − ε_ntc) up to ε_tu.
- E_tu is fitted to the "valleys" of the hardening branch, by analogy with the lower yield point of mild steel.
- Parameters over −30 to 60 °C: E_tc 10.2–16.8 GPa, E_tu 57.8–95.4 MPa, σ_ntc 1.56–3.28 MPa.
- Intended for link-slab design: ignore temperature in compression, use temperature-specific tension parameters.

## JSCE draft design model for HPFRCC ([[kunieda2006-hpfrcc-japan-applications]], p. 21, Fig. 4–5)
- Bilinear σ–ε defined by initial cracking strength, tensile strength and ultimate strain.
- The initial cracking strength is divided by a **material factor of 1.3**. The final JSCE recommendation
  values are ⚠️ unverified (the 1.3 is from the 2006 draft).
- Section analysis includes HPFRCC tension, both for HPFRCC members and for repair overlays.
- Design tensile properties should reflect the actual placement (thin, sprayed or extruded sections give
  2-D fiber orientation) (p. 21). → [[fiber-dispersion]]

## Damage model: secant-angle damage factor ([[zhao2022-ecc-tension-damage-model]])
- θ = arctan(σ/ε), θ0 = arctan(σ_k/ε_k); damage d = 1 − θ/θ0; σ = tan[(1 − d)·arctan(E0)]·ε (Eqs. 5–8).
  Units inside arctan ⚠️ unverified.
- Damage evolution (Eq. 9):
  - d = 0 for ε ≤ ε_k (elastic);
  - d = k(ε − ε_k)^b on the hardening branch;
  - d = Aε² + Bε + C on the softening branch, with d = 1 at ε_u.
- Calibrated for PVA-ECC with Vf v = 1–2% and W/B r = 0.24–0.28:
  b = (1.206 − 0.213v)(2.061r + 0.436); A = (0.358 − 0.147v)(2.842r + 0.247) (Eqs. 16–17).
- Compared with a trilinear model (elastic – linear hardening – linear softening, Eq. 20), which misses the
  nonlinear hardening (Fig. 6).
- FE check (ABAQUS CDP, high-strength steel wire mesh + ECC member, §5.2):

  | Model | Peak load / test | Displacement at peak / test |
  |---|---|---|
  | damage model | 1.042 | 0.964 |
  | trilinear | 1.123 | 0.574 |

- CDP parameters used for ECC: dilation 35°, eccentricity 0.1, f_b0/f_c0 1.07, K 0.6667, viscosity 0.0005 (§5.1).
- The model is for monotonic tension; a cyclic version is listed as future work (Concl. 5).

## Sectional and design uses
- **Inverse analysis:** the Maalej & Li (1994) sectional model with bilinear tension and compression underlies
  Qian's master curve; the neutral axis settles at 0.86–0.91 of the depth from the tension face once
  ε_t > 1% ([[qian2007-shcc-inverse-tensile-strain]], §3.1, Fig. 8). → [[four-point-bending-inverse-analysis]]
- **Shear design:** ECC's post-cracking tensile strength is used directly as the truss tension tie
  (σ_t × h × t at 45°) for side layers on RC beams ([[wang2019-rc-beam-ecc-shear-strengthening]], Eq. 1).
  → [[shear-behaviour]]
- **For FE impact simulation:** LS-Dyna with a plasticity-based model; HSHDC tensile rate effects
  taken from [[ranade2015-hshdc-tensile-rate-effects]]; compressive rate effects assumed equal to
  UHPC ([[ranade2017-hshdc-impact-resistance]], p. 26, 31–32). → [[impact-resistance]]
- **Caveat — non-hardening ECC inputs in FE:** a masonry-retrofit study modelled ECC in Abaqus CDP with
  E = 17,500 MPa and tension **softening** 1.45 → 1.06 → 0.43 MPa at cracking strain 0 / 0.0057 / 0.0138
  ([[tabrizikahou2022-masonry-ecc-sma-retrofit]], Tables 4–5). This ignores the strain-hardening branch that
  the models above capture. ⚔️ with the material definition of ECC (σ_tu about 3–5 MPa with hardening). → [[masonry-wall-retrofit]]

> Synthesis: design codes (JSCE draft) and most FE studies use simple bilinear or trilinear laws, which are
> enough for strength but under-predict deformation at peak (Zhao: 0.57× with trilinear). Because measured
> ε_tu itself depends strongly on the test specimen ([[tensile-strain-capacity]]), the ultimate-strain
> parameter of any model inherits that uncertainty.

## Compression counterpart
- The Weibull damage model for HDC in compression ([[deng2018-hdc-compressive-constitutive]], Eqs. 6–10) is on
  [[compressive-constitutive-model]].

## Related
- [[dogbone-uniaxial-tension]] · [[tensile-strain-capacity]] · [[tensile-toughness]] · [[compressive-constitutive-model]]
