---
type: dataset
slug: micromechanical-parameters
updated: 2026-10-16
---

# Micromechanical Parameters — Master Table

Links: [[fiber-matrix-interface]], [[strain-hardening]], [[fiber-bridging]].

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

The full Table 5 (11 mixes) is on the source page [[su2023-rubber-modified-hshdc]].

Related: [[mix-designs]], [[mechanical-results]]
