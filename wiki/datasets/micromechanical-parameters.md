---
type: dataset
slug: micromechanical-parameters
updated: 2026-10-20
---

# Micromechanical Parameters — Master Table

Links: [[fiber-matrix-interface]], [[strain-hardening]], [[fiber-bridging]].
Rows marked "assumed" or "model input" are analysis inputs, not measurements. The [[chavesfigueiredo2020-printed-shcc]] J values come from a flexural stress–CMOD method and are not comparable with single-crack J′b.

| Source | Material | Fiber | τ0 (MPa) | Gd (J/m²) | β | f | µ (N/(m·rad)) | Km (MPa√m) | J_tip (J/m²) | σ0 (MPa) | σ_fc (MPa) | J′b (J/m²) | PSH_strength | PSH_energy | Location |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [[ranade2015-hshdc-tensile-rate-effects]] | Michigan HSHDC @0.009 mm/s | PE 28 µm, 2% | about 1.5 (Fig. 8) | ≈0 | 0.003 | 0.59 | 386 | 1.10 | 25 | 11.3 (analytical min σ0) | 8.1 | 969 | 1.8 (σ_tu/σ_fc) | about 39 (computed here) | p. 97–103 |
| same | Michigan HSHDC @900 mm/s | same | +14% | ≈0 | 0.006 | 0.75 | 553 | 1.31 (at 10 mm/s) | ≤ 100 (assumed) | — | 12.4 | about 600 | 1.71 | about 6 or more | p. 98–103 |
| [[su2023-rubber-modified-hshdc]] | PE6-PR0 | PE 20 µm, 2% | not measured | — | — | — | — | 0.787 | — | 8.5 | 7.3 | 423 | 1.2 | 26.8 | Table 5 |
| same | PE12-PR0 | same | not measured | — | — | — | — | 0.787 | — | 16.9 | 10.7 | 1761 | 1.6 | 120 | Table 5 |
| same | PE12-PR20 | same | not measured | — | — | — | — | 0.740 | — | 19.6 | 7.4 | 2267 | 2.7 | 153 | Table 5 |
| same | PE18-PR0 | same | not measured | — | — | — | — | 0.787 | — | 20.7 | 8.8 | 2395 | 2.1 | 155 | Table 5 |
| same | PE18-PR20 | same | not measured | — | — | — | — | 0.740 | — | 22.7 | 7.3 | 3110 | 3.3 | 201 | Table 5 |
| [[li2002-pva-ecc-interface-tailoring]] | PVA-ECC oil 0% | PVA 39 µm, 2% | 2.44 | 4.71 | 2.21 | — | — | — | 5 (assumed; 4.5–7.2 measured) | — | 3.11 (composite) | 3.64–6.63 | 1.57 (σ_tu/σ_fc, computed here) | 0.73–1.33 | Table 3; Fig. 7 |
| same | PVA-ECC oil 0.3% | same | 2.15 | 3.16 | 2.31 | — | — | — | 5 | — | 2.63 | 5.17–13.8 | 1.79 (computed here) | 1.03–2.76 | same |
| same | PVA-ECC oil 0.5% | same | 2.14 | 2.96 | 1.82 | — | — | — | 5 | — | 2.35 | 7.68–13.6 | 1.74 (computed here) | 1.54–2.72 | same |
| same | PVA-ECC oil 0.8% | same | 1.98 | 2.18 | 1.18 | — | — | — | 5 | — | 2.90 | 12.5–20.7 | 1.59 (computed here) | 2.50–4.14 | same |
| same | PVA-ECC oil 1.2% | same | 1.11 | 1.61 | 1.15 | — | — | — | 5 | — | 2.92 | 24.2–38.1 | 1.51 (computed here) | 4.84–7.62 | same |
| [[li1992-steady-state-multiple-cracking]] | model: OPC matrix (Em 20 GPa) | steel / glass / carbon / PP | 7 / 0.3 / 8 / 0.7 | n/a | n/a | — | n/a | — | 100 (Gm) | — | — | — | — | — | Table 1; V_f^crit 3.6 / 0.4 / 0.6 / 2.9% ⚠️ |
| same | Spectra PE in HS concrete (Green 1989 data) | PE, Vf 0.6% | 1.0 (assumed) | n/a | n/a | — | n/a | 0.63 (assumed) | 20 | — | — | — | — | — | Table 2; mode A, no multiple cracking |
| [[yang2008-ecc-fiber-bridging-law]] | M45 + 0.1 / 0.5 / 2% PVA | PVA 39 µm, 1.2% oil | 1.91 / 1.58 / 1.31 | 1.24 / 1.13 / 1.08 | 0.63 / 0.60 / 0.58 | 0.2 (assumed) | — | n.r. | n.r. | model ≈0.35 / ≈1.7 / 6.7 (≈5 weakest plane) | — | n.r. | — | — | Tables 2–3; Figs. 12–14 |
| [[kanda2006-psh-design-criteria]] | 40PVA-27 / 40PVA-42 | PVA 40 µm, 2% | 2.21 | — (τs 31.3 MPa) | — | 0.5 | — | 0.33 / 0.23 | n.r. | n.r. | 2.47 / 1.85 | n.r. | 1.32 / 1.31 (test) | ≈2.4–2.5 / ≈3.0 | Tables 3–4; Figs. 15–16 |
| same | 14PVA-27 / 14PE-27 | PVA 14 µm 1.5% / PE 14 µm 2% | 4.35 / 0.66 | — (τs 33.6) / 0 | — | 0.5 | — | 0.33 | n.r. | n.r. | 3.99 / 2.25 | n.r. | 1.16 / 1.44 (test) | ≈1.1 / ≈3.0 | same |
| [[kanda2003-sprayed-ecc]] | PVA-ECC model, w/c 0.27 | PVA 12 mm, 40 µm, 2%; σ_fu,n 1070 MPa, Ef 40.6 GPa, f′ 0.39 | 3.14 (frictional τi) | n.r. (chemical bond strength τs 21.6 MPa) | n.r. | 0.5 | n.r. | 0.33 | — (Fig. 2 only) | — | — | — | — | Fig. 2 | Table 2 |
| same | PVA-ECC model, w/c 0.42 | same | 3.31 | n.r. (τs 20.7 MPa) | n.r. | 0.5 | n.r. | 0.23 | — | — | — | — | — | Fig. 2 | Table 2 |
| same | PVA-ECC model, w/c 0.62 | same | 2.63 | n.r. (τs 4.55 MPa) | n.r. | 0.5 | n.r. | 0.13 | — | — | — | — | — | Fig. 2 | Table 2 |
| same | chosen design, w/c 0.32 | same | — | — | — | — | — | — | — | — | — | — | — | about 2.0 (J′b/J_tip; ≥ 2.7 needs w/c ≥ 0.44) | p. 270–271, Fig. 2 |
| [[jin2019-hvfa-shcc-structural]] | parametric model input (generic SHCC, Yang 2008 model) | PVA 39 µm, 12 mm, 2%, E_f 22 GPa, f_f 1092 MPa | 1.0 (assumed) | 1.5 (assumed) | n.r. | n.r. | — | varied (Fig. 1g) | n.r. | Fig. 1 | n.r. | Fig. 1 | target > 1.45 (as cited) | target > 3 | Table 1; Fig. 1 |
| [[chavesfigueiredo2020-printed-shcc]] | printed XVA3PVA20 (notched-beam stress–CMOD integrals, not single-crack J′b; units suspect ⚠️) | PVA 2% | — | — | — | — | — | — | 16.37 "kJ/m²" as printed ⚠️ | — | — | J_b 430.74 "kJ/m²" ⚠️ | — | ≈26 (J_b/J_tip, computed) | Table 3 |
| same | printed YVA4PVA20-S05 (same method ⚠️) | PVA 2% | — | — | — | — | — | — | 7.11 ⚠️ | — | — | J_b 260.94 ⚠️ | — | ≈37 (computed) | Table 3 |

The full Table 5 (11 mixes) is on the source page [[su2023-rubber-modified-hshdc]].

Related: [[mix-designs]], [[mechanical-results]]
