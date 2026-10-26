---
type: test-method
slug: notched-beam-three-point-bending
aliases: [notched 3PB, three-point bending, double-K fracture test, CTOD, CMOD]
tags: [flexure, fracture, test]
sources: [ye2021-uhdc-flexural-size-effect, su2023-rubber-modified-hshdc, ranade2015-hshdc-tensile-rate-effects, kanakubo2006-dfrcc-tensile-test-method, chavesfigueiredo2020-printed-shcc, ivaniuk2022-printable-shcc-design, kanda2003-sprayed-ecc, huy2023-egc-activator-pretreatment]
updated: 2026-10-26
---

# Notched Beam Three-Point Bending

## Setups compared
| Source | Purpose | Specimen | Notch | Rate | Output |
|---|---|---|---|---|---|
| [[ye2021-uhdc-flexural-size-effect]] | size effect, composite K_IC | b = d = 40 / 70 / 100 / 150 mm, d/s = 0.44 | saw-cut, α = 0.10 / 0.23 | 2 mm/min | f_n, CTOD (clip gauge), DIC; K_IC by double-K (Xu & Reinhardt) with Wallin correction |
| [[su2023-rubber-modified-hshdc]] | matrix Km | 40 × 40 × 160 mm, span 100 mm | 12 mm | — | Km (Eqs. 1–3) |
| [[ranade2015-hshdc-tensile-rate-effects]] | matrix Km at rate | span 254 mm, depth 46.2 mm (as given for strain-rate conversion) | — | 20 µm/s – 10 mm/s | Km |
| [[chavesfigueiredo2020-printed-shcc]] (Table 3) | "fracture toughness" of printed SHCC, J_tip and J_b | 30 × 40 × 160 mm | 4.5 mm wide; 7 mm (X) / 10 mm (Y) deep | CMOD control 0.8 µm/s to first crack, then 3.3 µm/s | LOP 1.10 / 0.56 MPa, MOR 1.84 / 0.97 MPa (X / Y, 28 d); J_b > J_tip for both (J units printed kJ/m² ⚠️) |
| [[huy2023-egc-activator-pretreatment]] (Fig. 6, §2.5) | matrix Km of fly-ash geopolymer (no fibre) | 90 × 90 × 400 mm, span 360 mm | 45 mm cast notch (α = 0.5) | n.r. | peak load 0.29 / 0.17 kN → Km 0.11 / 0.06 MPa√m (ASTM E399, Eq. 3) |

## Unnotched three-point bending (for comparison)
- Printed PE-SHCC: 160 × 40 × 40 mm, span 120 mm, 1 mm/min; flexure 22.0 (D1) vs 18.5 MPa (D3, across the
  layers), 28 d Ref mix ([[ivaniuk2022-printable-shcc-design]], Table 3). → [[3d-printed-hdc]]
- Sprayed PVA-ECC: 40 × 40 × 160 mm, centre-point load, 100 mm span; MOR about 12–17 MPa; cut-outs from 150 mm
  sprays lose deflection capacity ([[kanda2003-sprayed-ecc]], Fig. 11 ⚠️ read).
- For four-point bending and inverse analysis → [[four-point-bending-inverse-analysis]].

## Key points
- JCI/JSCE already had a notched-beam bending standard for the fracture toughness of FRC before the DFRCC
  bending standard ([[kanakubo2006-dfrcc-tensile-test-method]], p. 5).

## Conflicts & open questions
- ⚠️ In Ye et al., the NC beam sizes differ between tables: 40/70/100 in Tables 3/4 vs 40/100/150 in
  Tables 2/5. The c_n formula may be misprinted.
- LEFM/double-K methods are applied to strain-hardening composites. Their validity is questionable.
- Chaves Figueiredo derive J_tip and J_b (PSH energy terms) from a notched 3PB rather than from a
  [[single-crack-test]]; the equivalence of the two routes is not shown in the corpus.

## Related
- [[size-effect]] · [[matrix-fracture-toughness]] · [[alkali-activated-binder]] · [[flexural-strength]] · [[four-point-bending-inverse-analysis]]
