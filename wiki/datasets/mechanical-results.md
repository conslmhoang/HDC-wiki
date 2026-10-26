---
type: dataset
slug: mechanical-results
updated: 2026-10-26
---

# Mechanical Results — Master Table

One row per mix and condition. Link the Mix ID to [[mix-designs]].
**Tension setups differ between sources** (see [[dogbone-uniaxial-tension]]).
n.s. = not stated; ≈ = read from a figure.
The [[huy2023-egc-pe-pva-hybrid-healing]] "healed" rows give ε including the 3% pre-strain; virgin rows of that source are at ≈ 35 d (inferred).
Member, field and fatigue data are kept on the source pages, not here: column tests in [[deng2018-hdc-short-columns]] (Table 5), field crack widths in [[kunieda2006-hpfrcc-japan-applications]], S–N data in [[sui2018-uhp-ecc-flexural-fatigue]] (Table 6). The FE input values of [[tabrizikahou2022-masonry-ecc-sma-retrofit]] are not measurements and are omitted.

| Source | Mix ID | Age (d) | f'c (MPa) | Specimen (tension) | First-crack σ (MPa) | σ_tu (MPa) | ε_tu (%) | Avg crack width (µm) | Flexural strength (MPa) | Location (Table/Fig) |
|---|---|---|---|---|---|---|---|---|---|---|
| [[ranade2015-hshdc-tensile-rate-effects]] | HSHDC @10⁻⁴ s⁻¹ | n.s. | — | dogbone, 90 mm gauge | 8.1 | 14.5 | 4.2 | 160 (residual) | — | Table 2 |
| same | HSHDC @10⁻³ s⁻¹ | n.s. | — | same | 7.6 | 15.3 | 3.9 | 150 | — | Table 2 |
| same | HSHDC @10⁻² s⁻¹ | n.s. | — | same | 8.9 | 16.3 | 3.3 | 140 | — | Table 2 |
| same | HSHDC @10⁻¹ s⁻¹ | n.s. | — | same | 9.7 | 17.5 | 2.9 | 120 | — | Table 2 |
| same | HSHDC @1 s⁻¹ | n.s. | — | same | 11.1 | 19.3 | 2.9 | 110 | — | Table 2 |
| same | HSHDC @10 s⁻¹ | n.s. | — | same | 12.4 | 20.6 | 2.7 | 110 | — | Table 2 |
| [[ranade2017-hshdc-impact-resistance]] | HSHDC (quoted from earlier work) | n.s. | 166 (51 mm cube); 159 (76 mm cube) | dogbone, 90 mm gauge | — | 14.5 | 3.4 | — | — | p. 26, Fig. 1 |
| same | Cor-Tuf | n.s. | 201 (51 mm cube) | same | — | 11.2 | 0.12 | 1–2 macro-cracks | — | p. 26–27 |
| same | Cor-Tuf, large dogbone | n.s. | — | 76 × 76 mm section | — | 7.6 | 0.09 | — | — | p. 27 |
| [[su2023-rubber-modified-hshdc]] | PE6-PR0 / PR10 / PR20 / PR35 | 28 | ≈128 / ≈115 / ≈119 / ≈86 | JSCE dumbbell | 7.3 / 8.2 / 7.4 / 6.2 | 10.2 / 10.4 / 10.3 / 8.9 | 0.4 / 0.3 / 0.5 / 0.4 | single crack | — | Table 4; Fig. 6a |
| same | PE12-PR0 | 28 | ≈121 | same | 10.7 | 17.6 | 2.9 | 198 | — | Tables 3–4 |
| same | PE12-PR10 | 28 | ≈115 | same | 9.3 | 17.3 | 3.4 | 174 | — | Tables 3–4 |
| same | PE12-PR20 | 28 | ≈112 | same | 7.4 | 17.3 | 4.9 | 107 | — | Tables 3–4 |
| same | PE12-PR35 | 28 | ≈72 | same | 8.4 | 16.1 | 3.8 | 79 | — | Tables 3–4 |
| same | PE18-PR0 | 28 | ≈157 | same | 8.8 | 19.3 | 3.8 | 116 | — | Tables 3–4 |
| same | PE18-PR10 | 28 | ≈99 | same | 8.7 | 19.6 | 4.6 | 130 | — | Tables 3–4 |
| same | PE18-PR20 | 28 | ≈116 | same | 7.3 | 19.4 | 5.7 | 88 | — | Tables 3–4 |
| [[yang2024-hshdc-uniaxial-tension]] | M1-0.16-PE22–1.5 | 28 | — | dogbone, 150 mm gauge | 3.06 | 6.06 | 3.561 | — | — | Table 6 |
| same | M1-0.16-PE22–2.0 | 28 | — | same | 3.52 | 6.99 | 3.839 | — | — | Table 6 |
| same | M1-0.16-PE22–2.5 | 28 | — | same | 3.96 | 7.69 | 4.647 | — | — | Table 6 |
| same | M1-0.16-PE30–2.0 | 28 | — | same | 3.60 | 6.73 | 3.156 | — | — | Table 6 |
| same | M1-0.16-PE35–2.0 | 28 | — | same | 3.36 | 5.11 | 2.294 | — | — | Table 6 |
| same | M1-0.16-PE40–2.0 | 28 | — | same | 3.15 | 4.52 | 0.345 | — | — | Table 6 |
| same | M1-0.14-PE22–2.0 | 28 | — | same | 3.58 | 5.94 | 0.811 | — | — | Table 6 |
| same | M1-0.18-PE22–2.0 | 28 | — | same | 3.09 | 5.72 | 1.888 | — | — | Table 6 |
| same | M1-0.16-PVA39–2.0 | 28 | 96.4 (100 mm cube) | same | 3.53 | 4.78 | 0.228 | — | f_f 20.5 (3-pt); f_b 16.33 (4-pt) | Tables 5–6 |
| same | M2-0.16-PE22–2.0 | 28 | — | same | 2.83 | 6.45 | 4.853 | — | — | Table 6 |
| same | M2-0.16-PVA39–2.0 | 28 | 91.6 | same | 3.48 | 5.28 | 0.250 | — | f_f 20.2; f_b 14.63 | Tables 5–6 |
| same | M3-0.16-PE22–2.0 | 28 | — | same | 2.77 | 6.76 | 6.483 | — | — | Table 6 |
| same | M3-0.16-PVA39–2.0 | 28 | 94.0 | same | 3.32 | 5.54 | 0.300 | — | f_f 18.4; f_b 13.06 | Tables 5–6 |
| [[ye2021-uhdc-flexural-size-effect]] | NC | 28 | 45.2 (as cited) | — | — | — | — | — | f_n 3.65–7.13 (notched 3-pt) | Table 3 |
| same | UHDC-1 | 28 | 37.7 (as cited) | JSCE dogbone, 80 mm gauge | ≈4–5 | ≈7 | 4.31 | — | f_n 10.00–21.56 | p. 3; Fig. 4b; Table 3 |
| same | UHDC-2 | 28 | 36.4 (as cited) | same | ≈4–5 | ≈9.5 | 9.45 | — | f_n 18.27–22.11 | p. 3; Fig. 4b; Table 3 |
| [[li2002-pva-ecc-interface-tailoring]] | PVA-ECC oil 0% | about 14 | — | coupon 304.8×76.2×12.7, about 185 mm gauge | 3.11 | 4.89 | 0.99 | 43 (residual) | — | Table 4; crack spacing 27 mm |
| same | PVA-ECC oil 0.3% | about 14 | — | same | 2.63 | 4.72 | 1.55 | 44 | — | Table 4; spacing 7.5 mm |
| same | PVA-ECC oil 0.5% | about 14 | — | same | 2.35 | 4.09 | 2.73 | 52 | — | Table 4; spacing 3.5 mm |
| same | PVA-ECC oil 0.8% | about 14 | — | same | 2.90 | 4.62 | 3.81 | 71 | — | Table 4; spacing 2.5 mm |
| same | PVA-ECC oil 1.2% | about 14 | — | same | 2.92 | 4.41 | 4.88 | 88 | — | Table 4; spacing 2.8 mm |
| [[zhang2022-hshdcc-review]] | Ranade 2011 (as cited) | 14 | 160 | JSCE dogbone | n.s. | ≈12–13 | 3.5 | n.s. | — | p. 2, 7; Fig. 9 |
| same | Yu K 2017 (as cited) | n.s. | 122 | n.s. | n.s. | 18.2 | 8.5 | n.s. | — | p. 10; Table 10 |
| same | Huang 2021, 90 °C water 9 d (as cited) | 12 | > 210 | n.s. | n.s. | ≈16 | > 5 | n.s. | — | p. 2, 7–8 |
| same | Yu KQ 2019, 45% GGBS + 10% RFP (as cited) | 28 | 102.5 | n.s. | n.s. | n.s. | 7.8 | n.s. | — | p. 2 |
| same | Li Y 2020, river sand (as cited) | n.s. | 115–131 | n.s. | n.s. | 12.1 | 11.0 | n.s. | — | p. 10; Table 10 |
| same | Lei 2019, SF 0 → 40% (as cited) | n.s. | ≈55 → ≈145 | n.s. | 2.8 → 3.9 | 4.9 → 6.6 | 2.5 → 4.7 | 82.6 → 69.3 | 15 → 31 | Figs. 10, 12, 15 |
| [[yu2018-ecc-direct-tensile-review]] | Tongji PE-ECC, Vf·Lf/df 7.5 → 18 (range) | n.s. | — | n.s. | — | 10.29 → 17.86 | 2.20 → 7.91 | narrowing | — | Fig. 2 |
| [[kanda2006-psh-design-criteria]] | 40PVA-27 / 40PVA-42 | n.s. | — | coupon, 205 mm gauge | 2.47 / 1.85 | 3.25 / 2.43 | 1.03 / 1.50 (ultimate) | — | — | Table 4 |
| same | 14PVA-27 / 14PVA-42 | n.s. | — | same | 3.99 / 2.92 | 4.62 / 3.32 | 0.26 / 0.55 | — | — | Table 4 |
| same | 14PE-27 | n.s. | — | same | 2.25 | 3.25 | 5.10 | — | — | Table 4 |
| [[yang2008-ecc-fiber-bridging-law]] | M45 2% PVA | n.r. | — | n.r. | ≈4 ⚠️ | about 5 | ≈4–4.5 ⚠️ | about 60 | — | Fig. 1 |
| [[chai2023-hdc-ambient-temperature]] | HDC-1 @20 °C | 28 | 48.0 (100 mm cube) | dogbone, 100 mm gauge | 2.86 | 4.23 | 1.15 (at peak, Fig. 1 p. 2) | n.r. | 14.08 (4-pt plate, Fig. 6b) | Tables 4–8, pp. 6–14 |
| same | HDC-1 @−30 / 0 / 40 / 60 °C (8 h) | 28 + exposure | 46.7 / 47.1 / 50.9 / 52.7 | same | 2.79 / 1.56 / 3.28 / 2.92 | 3.74 / 3.99 / 4.46 / 4.80 | 1.34 / 1.46 / 1.23 / 1.31 (at peak) | n.r. | 12.23 / 13.08 / 14.65 / 15.64 | Tables 5–8, pp. 8–14 |
| same | HDC-2 / HDC-3 / HDC-4 | 28 | 47.8 / 50.2 / 59.0 | same | n.r. | 4.47 / 4.22 / 4.83 | 0.64 / 0.55 / 0.42 (at peak) | n.r. | — | Table 4, p. 6 |
| [[li2021-hdc-sulfate-dry-wet]] | HDC, 0 cycles | 90 | 45.8 (100 mm cube) | not tested | — | — | — | — | — | Table 4, p. 6 |
| same | HDC, 150 dry–wet cycles: water / 5% / 10% / sat. Na₂SO₄ | 90 + exposure | 58.3 / 50.1 / 37.9 / 28.9 | not tested | — | — | — | — | — | Table 4, p. 6 |
| [[deng2015-hdc-compressive-toughness]] | 1 (matrix) | ≈300 (10 months) | 64.0 prism 100×100×300 (computed from 640.45 kN); authors' mean 63.06 | — | — | — | — | — | — | Table 3; p. 6; peak strain 0.22% |
| same | 2 (1.0% PVA) | ≈300 | 50.3 prism (computed) | — | — | — | — | — | — | Table 3; peak compressive strain 0.74%; W_cu^0.85 0.187 N/mm² |
| same | 3 (1.5% PVA) | ≈300 | 56.9 prism (computed) | — | — | — | — | — | — | Table 3; 0.67%; W_cu^0.85 0.198 |
| same | 4 (2.0% PVA) | ≈300 | 62.3 prism (computed) | method n.r. | — | 5.7 (mean, method n.r.) | n.r. | — | — | Table 3; p. 5; 0.80%; W_cu^0.85 0.266 |
| [[deng2018-hdc-compressive-constitutive]] | 1 (matrix) | n.s. | 63.06 (prism 100×100×300) | — | — | — | — | — | — | Table 3; ε0 0.213% |
| same | 2 / 3 / 4 (PVA 1 / 1.5 / 2%) | n.s. | 50.28 / 56.85 / 62.25 | — | — | — | — | — | — | Table 3; ε0 0.569 / 0.601 / 0.672% |
| same | 5 / 6 (W/B 0.26 / 0.32) | n.s. | 56.04 / 52.84 | — | — | — | — | — | — | Table 3; ε0 0.633 / 0.652% |
| same | 7 / 8 (FA 60 / 40%) | n.s. | 53.64 / 64.43 | — | — | — | — | — | — | Table 3; ε0 0.634 / 0.561% |
| same | 9 / 10 (S/B 0.24 / 0.48) | n.s. | 51.96 / 56.01 | — | — | — | — | — | — | Table 3; ε0 0.648 / 0.556% |
| [[deng2018-hdc-short-columns]] | HDC (2% PVA) | n.s. | 65.7 (f_cu, 100 mm cube) | direct tension, geometry n.s. ⚠️ | 5.73 | 6.14 | ≈1.0 | — (multiple cracks, Fig. 1b) | — | p. 2, Fig. 1, Table 4 |
| same | Concrete (RC1 control) | n.s. | 68.9 (f_cu, 100 mm cube) | — | — | — | — | — | — | Table 4 |
| [[deng2017-rc-column-hdc-jacket]] | HDC (Japanese PVA) | n.r. | f_cu 60.35 (100 mm cube) | not reported | ≈ 5.3 (Fig. ⚠️) | 6.12 | ≈ 3.0 ultimate (end of curve, Fig. ⚠️); peak strain n.r. | n.r. | — | Table 5, Fig. 1a |
| same | HDC-2 (Chinese PVA) | n.r. | f_cu 61.29 (100 mm cube) | not reported | ≈ 4.0–4.5 (Fig. ⚠️) | 4.84 | ≈ 1.2 ultimate (Fig. ⚠️) | n.r. | — | Table 5, Fig. 1a |
| [[deng2019-urm-shaking-table-hdc]] | HDC (overlay) | 28 (cubes); tension age n.r. | f_cu 61.15 (100 mm cube) | 15 mm plate, DBJ61/T112-2016, n = 3 | ≈ 5.2–5.8 (Fig. ⚠️) | 5.83 (mean) | 1.0 ultimate (curves end 0.86–1.0%, Fig. ⚠️) | n.r. | — | p. 3, Table 3, Fig. 6a |
| [[deng2020-aac-wall-hdc-retrofit]] | HDC (1.7% PVA) | ≈ 60 ("two months"), air-cured | f_cu 49.80 (100 mm cube) | dogbone, 15 × 50 mm section | ≈ 3.25 (Fig. ⚠️) | 3.89 | ≈ 1.2 at peak; failure ≈ 1.24 (Fig. ⚠️) | n.r. | — | Table 3, Fig. 3 |
| [[li2021-hdc-beam-shear]] | HDC (PVA 2%) | 28 | 70.55 (f_cu, 70.7 mm cube) | dogbone, 15 mm thick, 50 mm wide (Fig. 2, geometry ⚠️) | n.r. (≈ 4.5–5 from Fig. 1 ⚠️) | 5.83 (5.68 in Concl. 1 ⚔️) | 0.968 (basis n.s. ⚠️) | — | — | §2.1, Fig. 1 |
| same | RC control C50 (concrete, not HDC) | 28 | 75.77 (f_cu, 100 mm cube) | — | — | — | — | — | — | §2.1 |
| [[zhang2022-hdc-basalt-textile-tension]] | M1-1.5 (plain HDC) | 28 | 56.2 (f_cu, 100 mm cube) | XAUAT dogbone 350 mm, 50 × 15 mm | 3.07 | 3.89 | 0.12 (peak) | — | — | Tables 3, 8 |
| same | M1-2 | 28 | 52.0 (f_cu) | same | 4.35 | 5.44 | 0.34 (peak) | — | — | Tables 3, 8 |
| same | M2-1 | 28 | 32.0 (f_cu) | same | 2.04 | 2.35 | 0.29 (peak) | — | — | Tables 3, 8 |
| same | M2-1.5 | 28 | 38.1 (f_cu) | same | 2.75 | 3.45 | 0.28 (peak) | — | — | Tables 3, 8 |
| same | M2-2 | 28 | 33.3 (f_cu) | same | 3.10 | 4.23 | 0.45 (peak) | — | — | Tables 3, 8 |
| same | B1M1-2 (TR-HDC, 1 basalt layer) | 28 | 52.0 (f_cu) | same + basalt grid ν 0.42% | 4.43 | 6.11 | 1.51 (peak) | — | — | Table 8 |
| same | B3M1-2 (3 layers) | 28 | 52.0 | same + grid ν 1.26% | 4.36 | 9.73 | 2.13 (peak) | — | — | Table 8 |
| same | B1M2-2 | 28 | 33.3 | same + grid ν 0.42% | 3.75 | 5.83 | 1.64 (peak) | — | — | Table 8 |
| same | B3M2-2 | 28 | 33.3 | same + grid ν 1.26% | 2.67 | 10.02 | 2.48 (peak) | — | — | Table 8 |
| same | B3M2-0 (TRC, no PVA; not HDC) | 28 | 30.2 | same + grid ν 1.26% | 2.19 | 6.82 | 3.79 (textile slip) | — | — | Table 8 |
| [[chai2019-hdcc-freeze-thaw-carbonation-flexure]] | Eco-HDCC, 0 cycles | 28 | 43.4 (100 mm cube; age assumed ⚠️) | not tested | — | — | — | — | 14.31 (4-pt, 100×100×400 prism; δ_u 2.70 mm) | §2.1, Table 4 |
| same | preload 0, 15 F–T+carb. cycles | ≈148 (28 + 120 d exposure) | — | not tested | — | — | — | no crack | 11.55 (−19.3%; δ_u 2.01 mm) | Table 4 |
| same | preload 0.3, 15 cycles | ≈148 | — | not tested | — | — | — | no crack | 11.52 (−19.5%; δ_u 2.05) | Table 4 |
| same | preload 0.5, 15 cycles | ≈148 | — | not tested | — | — | — | 28 (single crack, surface; 20 at 5 cycles) | 11.01 (−23.1%; δ_u 1.83) | Table 4, §3.1 |
| same | preload 0.7, 15 cycles | ≈148 | — | not tested | — | — | — | 30 (28 after preload) | 9.63 (−32.7%; δ_u 1.36) | Table 4, §3.1 |
| [[gao2020-hdcc-recycled-fine-aggregate]] | 45R05 (RFA, 0.5%) | 28 | n.r. (W/B 0.45 series; ≈39–43 implied by Fig. 19, computed, not reported) | dogbone 160 mm long, 40×40 mm section, 50 mm gauge (Fig. 1, p. 4) | 1.14 | 1.51 | 1.32 (max 5.08) | n.r. | — | Table 6 |
| same | 45N05 (NFA, 0.5%) | 28 | n.r. | same | 1.02 | 1.12 | 0.41 (max 4.58) | n.r. | — | Table 6 |
| same | 45R10 | 28 | n.r. | same | 1.75 | 2.16 | 1.69 (max 9.10) | n.r. | — | Table 6 |
| same | 45N10 | 28 | n.r. | same | 1.63 | 1.69 | 1.54 (max 5.83) | n.r. | — | Table 6 |
| same | 45R15 | 28 | n.r. | same | 1.82 | 2.61 | 2.48 (max 10.02) | n.r. | — | Table 6; SH |
| same | 45N15 | 28 | n.r. | same | 1.70 | 1.99 | 1.64 (max 7.60) | n.r. | — | Table 6 |
| same | 45R20 | 28 | n.r. | same | 2.38 | 2.84 | 4.76 (max 11.73) | n.r. | — | Table 6; SH |
| same | 45N20 | 28 | n.r. | same | 1.57 | 2.75 | 1.68 (max 10.72) | n.r. | — | Table 6; no clear SH |
| same | 25R20 (RFA, 2%) | 28 | 83.8 (40 mm prism halves, Fig. 9a) | — | σ_bc 8.11 (bending) | — | — | n.r. | σ_bp 11.89 (4-pt, 15 mm plate, 300 mm span); δ_bp 7.67 mm; 3-pt 40 mm prism 34.3 (Fig. 9b) | Table 5, p. 11; Fig. 9, p. 9 |
| same | 25N20 (NFA, 2%) | 28 | 70.9 (Fig. 9a) | — | σ_bc 7.97 | — | — | n.r. | σ_bp 9.41; δ_bp 5.12 mm; 3-pt prism 28.0 | Table 5, p. 11; Fig. 9, p. 9 |
| same | 25R10 / 25N10 | 28 | 84.9 / 73.5 (Fig. 9a) | — | 6.57 / 5.58 | — | — | n.r. | 9.33 / 6.54; δ_bp 6.22 / 2.20 mm; 3-pt prism 18.0 / 15.9 | Table 5, p. 11; Fig. 9, p. 9 |
| same | 25R15 / 25N15 | 28 | 84.1 / 71.0 (Fig. 9a) | — | 6.78 / 6.06 | — | — | n.r. | 10.43 / 7.02; δ_bp 7.58 / 4.90 mm; 3-pt prism 26.8 / 22.3 | Table 5, p. 11; Fig. 9, p. 9 |
| same | 25R05 / 25N05 | 28 | 83.2 / 78.0 (Fig. 9a) | — | 6.25 / 4.78 | — | — | n.r. | 6.47 / 4.84; δ_bp 0.12 / 0.22 mm; 3-pt prism 12.4 / 11.2 | Table 5, p. 11; Fig. 9, p. 9 |
| same | 25R00 / 25N00 (plain mortar, no fiber) | 28 | 83.6 / 75.6 (Fig. 9a) | — | 6.19 / 4.87 | — | — | n.r. | σ_bc only (no deflection hardening); 3-pt prism 9.4 / 9.2 | Table 5, p. 11; Fig. 9, p. 9 |
| [[yuan2020-nshsdc-beam-strengthening]] | NSHSDC | 28 | 123.4 (ASTM C39 cylinder) | JSCE dogbone (geometry n.s.) | — | 9.7 | — (> 2.9 quoted from refs 12–13, §1) | — | 21.9 (ASTM C1609 4-pt) | Table 5, p. 3; §1, p. 2 |
| [[lee2021-hsdc-wall-emi-impact]] | HSDC | 28 | 122.3 (CV 0.1) | direct tension (dogbone per refs 13–15; geometry n.r.) | — | 9.7 (CV 1.6) | n.r. ⚠️ | — | 22.9 (CV 6.5) | Table 4, p. 3 |
| [[kanda2003-sprayed-ecc]] | A sprayed | 28 | — | coupon 80 mm gauge, 30 × 13 mm | about 4.7 | about 6.7 | about 3.1 (ultimate) | — | MOR ≈12–17 (range over all specimens; per-mix values not tabulated) ⚠️ | Fig. 10, 11 (read off ⚠️) |
| same | A placed | 28 | — | same | about 4.2 | about 5.0 | about 1.2 | — | within ≈12–17 range ⚠️ | Fig. 10, 11 ⚠️ |
| same | B sprayed | 28 | — | same | about 4.4 | about 6.8 | about 2.4 | — | within ≈12–17 range ⚠️ | Fig. 10, 11 ⚠️ |
| same | B placed | 28 | — | same | about 3.5 | about 4.1 | about 1.2 | — | within ≈12–17 range ⚠️ | Fig. 10, 11 ⚠️ |
| same | C sprayed | 28 | — | same | about 4.6 | about 6.3 | about 4.2 | — | within ≈12–17 range ⚠️ | Fig. 10, 11 ⚠️ |
| same | C placed | 28 | — | same | about 3.6 | about 4.0 | about 1.6 | — | within ≈12–17 range ⚠️ | Fig. 10, 11 ⚠️ |
| same | D sprayed | 28 | — | same | about 5.2 | about 7.2 | about 3.8 | — | — | Fig. 10 ⚠️ |
| same | B sprayed (anti-spalling batch) | 50–52 | 59 | same | — | 5.8 | 4.4 | first-crack COD 36 (pin test) | — | Table 7, 8 |
| same | PCM (comparison, not HDC) | 50–52 | 53 | same | — | 3.74 | 0.016 | first-crack COD 67 (pin test) | — | Table 7, 8 |
| [[kanakubo2006-dfrcc-tensile-test-method]] | PVA T1 | n.s. | 31.3 | plate dogbone 30 × 13 mm (≈80 mm gauge), pin–fix | 3.72 | 5.00 | 2.697 (peak; COV 24%) | — | — | Tables 5, 6 |
| same | PVA T2-H / T2-V | n.s. | 31.3 | dogbone 100 × 60 mm, H / V cast | 2.47 / 2.51 | 4.18 / 2.87 | 2.380 / 0.769 | — | — | Table 7 |
| same | PVA T3 / T4 | n.s. | 31.3 | Ø70 dogbone / Ø100 cylinder fix–fix | 3.17 / — | 3.38 / 1.78 | 0.071 / 0.320 | — | — | Tables 8, 9 |
| same | PE T1 | n.s. | 67.3 | plate dogbone | 3.01 | 4.85 | 1.283 | — | — | Table 6 |
| same | PE T2-H / T2-V | n.s. | 67.3 | 100 × 60 dogbone | 3.86 / 5.02 | 3.86 / 5.06 | 0.018 / 0.253 | — | — | Table 7 |
| same | PE T3 / T4 | n.s. | 67.3 | Ø70 / Ø100 | 5.08 / — | 5.56 / 4.18 | 0.196 / 0.833 | — | — | Tables 8, 9 |
| same | HB T1 | n.s. | 43.6 | plate dogbone | 2.32 | 4.37 | 0.705 | — | — | Table 6 |
| same | HB T2-H / T2-V | n.s. | 43.6 | 100 × 60 dogbone | 3.42 / 2.51 | 3.54 / 2.51 | 0.217 / 0.017 | — | — | Table 7 |
| same | HB T3 / T4 | n.s. | 43.6 | Ø70 / Ø100 | 2.70 / — | 2.84 / 2.15 | 0.122 / 0.437 | — | — | Tables 8, 9 |
| same | DCT (UFC) T1 | n.s. | 198.0 | plate dogbone | 13.69 | 15.27 | 0.528 | — | — | Table 6 |
| same | DCT T3 / T4 | n.s. | 198.0 | Ø70 / Ø100 | 9.38 / — | 12.41 / 7.18 | 0.089 / 0.045 | — | — | Tables 8, 9 |
| same | PVA / PE / HB / DCT bending inverse (Case 1, H) | n.s. | — | 100 × 100 × 400 4-pt bending | 2.65 / 3.11 / 2.40 / 12.92 | 3.75 / 5.82 / 4.16 / 8.62 | 3.07 / 2.36 / 1.79 / 1.19 (ultimate, back-calculated) | — | M_max 1.535 / 2.212 / 1.531 / 4.518 kN·m | Tables 10, 11 |
| [[qian2007-shcc-inverse-tensile-strain]] | PVA-ECC 0 | n.s. | 50.7 | n.s. | 5.1 | 5.7 | 2.0 ± 1.0 | — | — | Table 1 |
| same | PVA-ECC 1 (FA/C 1.2) | 28 | 54.6 | coupon 304.8 × 76.2 × 12.7, ~180 mm gauge | 4.6 | 5.3 | 2.1 ± 1.1 (peak) | — | MOR 10–12 (range for ECC 1–3); δ_u 5.8 mm | Tables 6, 7 |
| same | PVA-ECC 2 (FA/C 2.0) | 28 | 46.0 | same | 3.9 | 4.6 | 3.5 ± 0.3 | — | δ_u 7.0 mm | Tables 6, 7 |
| same | PVA-ECC 3 (FA/C 2.8) | 28 | 37.5 | same | 4.0 | 4.9 | 3.7 ± 0.4 | — | δ_u 9.3 mm | Tables 6, 7 |
| [[homma2009-frcc-self-healing]] | FRCC(SC) | 7 | — | plate 25×75×75 mm, M6 bars | about 2.5–3 ≈ | about 2.5–3.2 ≈ | n.r. (elongation mm) | max 35–757 (single largest crack) | — | Fig. 2, Table 3 |
| same | FRCC(PE) | 7 | — | same | about 2.5–2.8 ≈ | = first crack (softening) | n/a | max 19–368 | — | Fig. 2, Table 3, p. 224 |
| same | HFRCC | 7 | — | same | about 2.5–3 ≈ | about 3.3–3.6 ≈ | n.r. | max 17–710 | — | Fig. 2, Table 3 |
| [[kunieda2010-uhp-shcc-steel-reinforcement]] | UHP-SHCC dumbbell | 28 | 95 (Ø50 × 100) | dumbbell 13 × 30 mm section | — | 6.5 | 1.5 (at ultimate load) | — | — | §3.2 |
| same | S-0 unreinforced member, ρs 0 | 28+ ⚠️ | — | prism 50 × 200 × 900 mm, 100 mm Pi-gauges | 3.9–4.2 (computed P_cr/A) | 4.7–5.0 (computed P_u/A) | 0.23–0.24 (avg) | — (spacing 12–14 mm) | — | Table 3, Fig. 5 |
| same | S-1, ρs 0.3% (D6) | 28+ ⚠️ | — | same, reinforced | 4.1–4.2 (computed, incl. bar) | 6.4–6.5 (nominal incl. bar, computed) | 1.58–1.60 (avg) | — (spacing 4.5–4.6 mm) | — | Table 3 |
| same | S-2…S-4, ρs 0.6–1.2% | 28+ ⚠️ | — | same | 3.6–4.0 (computed) | 7.3–10.4 nominal incl. steel (computed) | 1.49–1.82 | — (spacing 3.3–4.0 mm) | — | Table 3 |
| [[lepech2009-ecc-water-permeability]] | ECC M45 pre-strained 3% | 14 | — | plate 300 × 75 × 12 mm, 180 mm gauge | ≈ 3.8 (Fig. ⚠️) | ≈ 4.7 (Fig. ⚠️; test stopped at 3%) | > 3 (capacity not reached) | 63 ± 10 (unloaded; avg/max undefined); loaded 40–70 | — | Table 5; Fig. 3c; p. 749 |
| same | PVA-ECC M45 (Fig. 1) | n.s. | — | n.s. | ≈ 3.5 (⚠️) | ≈ 5 (⚠️) | ≈ 4 (⚠️; abstract "> 4%") | ≈ 50–60 plateau (⚠️) | — | Fig. 1 |
| [[yang2009-ecc-self-healing-wet-dry]] | ECC M45, virgin | f'c at 28; tension at ≈ 180 | ≈ 60 | coupon 230 × 76 × 13 mm, 0.0025 mm/s | ≈ 3.5–4 (Fig. ⚠️) | ≈ 4.0–4.4 (Fig. ⚠️) | ≈ 3 (stated "about 3%") | ≈ 60 (steady state, stated); max residual 50–90 | — | p. 384–385; Table 2; Figs. 9–10 |
| same | ECC M45, healed 10 × CR1 | ≈ 180 + 20 | — | same | < virgin | ≈ virgin (Fig. ⚠️) | 1.7–3.1 (reload, residual strain excluded) | — | — | p. 388; Fig. 9 |
| same | ECC M45, healed 10 × CR2 | ≈ 180 + 20 | — | same | < virgin | up to ≈ 5.3 (Fig. ⚠️) | 0.8–2.2 (reload) | — | — | p. 388; Fig. 10 |
| [[vanzijl2010-shcc-durability]] | Ref.1 PVA (Adendorff) | n.r. | — | n.r. | — | 4.26 ± 0.42 | 4.70 ± 0.65 | 50 ± 14 (at 3%, 0.001/s) | — | Table 1 |
| same | Ref.2 PE (Kobayashi) | n.r. | — | n.r. | 3.0 | 4.3 | 4.3 | 28 ± 18 | — | Table 1 |
| same | Ref.3 PVA oil 0.5% | n.r. | — | n.r. | 3.45 ± 0.14 | 3.92 ± 0.15 | 1.64 ± 0.60 | 45 ± 19 | — | Table 1 |
| same | Ref.4 PVA oil 0.8% | n.r. | — | n.r. | 2.63 ± 0.32 | 4.28 ± 0.17 | 2.48 ± 1.04 | 50 ± 9 | — | Table 1 |
| same | Ref.5 PVA oil 0.8%, 2.5% | n.r. | — | n.r. | 3.39 ± 0.09 | 5.00 ± 0.52 | 4.59 ± 0.36 | 58 ± 10 | — | Table 1 |
| same | Ref.6 PVA oil 1.2% | n.r. | — | n.r. | — | 4.5 | 3.2 | 56 | — | Table 1 |
| [[mechtcherine2011-shcc-high-strain-rate]] | SHCC @10⁻⁵ s⁻¹ | n.s. | — | dumbbell 40×24 mm, 100 mm gauge | — | 4.54 | 1.49 | — | — | Table 2 |
| same | SHCC @10⁻⁴ s⁻¹ | n.s. | — | same | — | 5.28 | 1.28 | — | — | Table 2 |
| same | SHCC @10⁻³ s⁻¹ | n.s. | — | same | — | 5.37 | 0.93 | — | — | Table 2 |
| same | SHCC @10⁻² s⁻¹ | n.s. | — | same | — | 5.51 | 0.82 | — | — | Table 2 |
| same | SHCC @10 s⁻¹ | n.s. | — | same, high-rate MTS | — | 7.81 | 0.68 | — | — | Table 2 |
| same | SHCC @25 s⁻¹ | n.s. | — | same | — | 12.08 | 0.86 | — | — | Table 2 |
| same | SHCC @50 s⁻¹ | n.s. | — | same | — | 11.93 | 1.79 (no multiple cracking) | — | — | Table 2 |
| [[yun2013-shcc-freeze-thaw]] | 45-PVA1.30+PE0.20 (0 F-T) | 39 ⚠️ (14 per text); air-cured 65% RH | 48.80 | JSCE dumbbell | 1.68 | 3.77 | ≈ 0.4–0.65 at peak (Fig. 9b ⚠️; text Fig. 10: SH to ≈ 2.4) | n.r. | 11.25 | Table 3; Figs. 9b, 10 |
| same | 45-PVA1.30+PE0.20 (300 F-T) | 151 | 46.73 | JSCE dumbbell | 1.85 | 4.68 | ≈ 0.85 (Fig. 9b ⚠️) | n.r. | 12.44 | Table 3; Figs. 9b, 10 |
| same | 45-PVA0.75+PE0.75 (0 F-T) | 39 ⚠️ | 43.95 | JSCE dumbbell | n.r. | 2.35 | ≈ 0.47 (Fig. 8a ⚠️) | n.r. | 15.39 | Table 3; Fig. 8a |
| same | 45-PVA0.75+PE0.75 (300 F-T) | 151 | 46.73 | JSCE dumbbell | n.r. | 3.16 | n.r. | n.r. | 13.44 | Table 3 |
| same | 55-PVA1.30+PE0.20 (0 F-T) | 39 ⚠️ | 39.94 | JSCE dumbbell | n.r. | 2.89 | n.r. | n.r. | 12.36 | Table 3 |
| same | 55-PVA1.30+PE0.20 (300 F-T) | 151 | 45.80 | JSCE dumbbell | n.r. | 3.55 | n.r. | n.r. | 12.38 | Table 3 |
| same | 55-PVA0.75+PE0.75 (0 F-T) | 39 ⚠️ | 35.73 | JSCE dumbbell | n.r. | 2.95 | n.r. | n.r. | 12.16 | Table 3 |
| same | 55-PVA0.75+PE0.75 (300 F-T) | 151 | 34.08 | JSCE dumbbell | n.r. | 3.57 | n.r. | n.r. | 10.80 | Table 3 |
| [[ozbay2013-ecc-self-healing-sustained-load]] | ECC-1 | 28 | 69.3 (50 mm cube) | none (4-pt bending 360×50×75, span 304) | — | — | — | about 60 unloaded / about 115 loaded (at 2.5 mm defl.) | 12.40 (MOR; defl. 4.95 mm) | Table 3 |
| same | ECC-2 | 28 | 46.1 | same | — | — | — | about 40 unloaded / about 85 loaded | 10.07 (defl. 6.01 mm) | Table 3 |
| same | ECC-1 pre-cracked, 90 d water, no load / sustained 60% | 28+90 | — | same | — | — | — | n.r. (5–11 / 7–14 cracks left) | 12.1 / 11.8 | Table 4 |
| same | ECC-2 pre-cracked, 90 d water, no load / sustained | 28+90 | — | same | — | — | — | n.r. (2–7 / 4–11 cracks) | 11.3 / 11.1 | Table 4 |
| [[paul2014-r-shcc-chloride-corrosion]] | FS-SHCC | 14 (tension); 28 (f_cu) | 24 (100 mm cube) | dumbbell 30×16 mm, 80 mm gauge | 2.04 | 2.67 | 2.93 (ultimate) | 24–36 (R/SHCC beams, Table 3) | — | Table 2, Table 3, p. 344 |
| same | CS-SHCC | 14; 28 | 23 (cube) | same | 2.46 | 2.76 | 1.52 (CoV 103.7%) | 22–38 (beams) | — | Table 2, Table 3 |
| [[choi2016-pe-alkali-activated-slag-composite]] | M26 | 28 | 54.8 (50 mm cube) | JSCE dogbone 30 × 13 mm, 80 mm gauge | 4.87 | 13.06 | 7.50 | 88.9 (computed, at end of loading) | — | Tables 5, 7, 8 |
| same | M30 | 28 | 49.0 | same | 4.61 | 11.46 | 6.33 | 106.9 | — | Tables 5, 7, 8 |
| same | M34 | 28 | 42.3 | same | 3.92 | 7.64 | 5.35 | 109.8 | — | Tables 5, 7, 8 |
| same | M38 | 28 | 36.3 | same | 3.37 | 5.06 | 4.58 | 99.3 | — | Tables 5, 7, 8 |
| [[hieu2023-aas-extremely-ductile-22pct]] | R5-S8-M0 | 28 | 54.6 (50 mm cube) | JSCE dumbbell, 13 mm thick, 80 mm gauge | 5.08 | 7.92 | 9.81 (at peak) | 117.2 (computed, at peak) | — | Fig. 7; Tables 4, 6 |
| same | R5-S8-M1 | 28 | 53.6 (53.4 in Table 7 ⚠️) | same | 4.70 | 7.63 | **22.34** (at peak) | 212.0 | — (103 mm deflection, Fig. 12) | Fig. 7; Tables 4, 6 |
| same | R5-S8-M2 | 28 | 52.2 | same | 4.12 | 8.19 | 20.89 (at peak) | 204.0 | — | Fig. 7; Tables 4, 6 |
| [[huy2023-egc-activator-pretreatment]] | ED-EGC-WP | 28 | 31.1 (50 mm cube) | JSCE dogbone 30 × 13 mm, 80 mm gauge | 4.67 | 8.72 | 10.97 (at peak) | 171.8 (computed, at peak) | — | Tables 4–5, Fig. 8 |
| same | ED-EGC-CP | 28 | 20.7 | same | 3.40 | 5.54 | 18.62 (at peak) | 199.3 (computed) | — | Tables 4–5, Fig. 8 |
| [[huy2023-egc-pe-pva-hybrid-healing]] | S-PE | ≈ 35 ⚠️ (7 d + 28 d water) | 84.3 (50 mm cube, Fig. 3) | JSCE dumbbell 30 × 13 mm, 80 mm gauge | 3.70 | 6.64 | 10.51 (at peak) | 100.3 (computed, at peak) | — | Fig. 3; Tables 5–6 |
| same | S-PVA | ≈ 35 ⚠️ | 86.5 | same | 3.84 | 6.04 | 6.79 (at peak) | 83.2 | — | Fig. 3; Tables 5–6 |
| same | F-PE | ≈ 35 ⚠️ | 50.4 | same | 2.70 | 5.18 | 11.99 (at peak) | 128.4 | — | Fig. 3; Tables 5–6 |
| same | F-PVA | ≈ 35 ⚠️ | 51.9 | same | 2.84 | 4.60 | 10.35 (at peak) | 136.1 | — | Fig. 3; Tables 5–6 |
| same | S-PE healed (3% pre-strain at 7 d, 28 d water, reloaded) | 35 | — | same | 3.76 | 7.53 | 9.45 (incl. 3% pre-strain) | — | — | Table 8 |
| same | S-PVA healed | 35 | — | same | 4.21 | 6.33 | 6.29 (incl. 3% pre-strain) | — | — | Table 8 |
| same | F-PE healed | 35 | — | same | 3.81 | 5.23 | 11.97 (incl. 3% pre-strain) | — | — | Table 8 |
| same | F-PVA healed | 35 | — | same | 3.21 | 4.40 | 9.67 (incl. 3% pre-strain) | — | — | Table 8 |
| [[pourfalah2018-ecc-high-temperature]] | ECC @20 °C | 28 | 38.8 (50 mm cube) | dogbone, 80 mm gauge, 30 × 13 mm | 2.75 | 3.85 | 3.5 (at peak) | ≈ 50 (bending) | n.r. (load only, ≈ 1300–1400 N peak, Fig. 10b ⚠️) | Tables 4–5; §4.3 |
| same | H6ECC @20 °C | 28 | 40.1 | same | 2.89 | 4.36 | 3.0 | ≈ 40 (bending) | n.r. | Tables 4–5 |
| same | H13ECC @20 °C | 28 | 45 | same | 3.32 | 4.71 | 2.5 | ≈ 40 (bending) | n.r. | Tables 4–5 |
| [[wang2023-ecc-frost-damage]] | ECC, 0 F-T cycles | 28 | 46.8 | not described | — | 4.21 | 5.24 ("ultimate") | — | 18.6 (4-pt, 40×40×160) | Table 4; §3.2 |
| same | ECC, 300 F-T cycles | 28 + F-T | — | — | — | — | — | — | 16.6 | §3.2, Fig. 7 |
| same | Normal concrete W/C 0.5 | 28 | 42.92 | not described | — | 2.98 | 0.01 | — | — | Table 4 |
| [[zhou2023-hsecc-elevated-temperature]] | PO @30 / 200 / 400 / 600 / 800 °C | 28 | 83.1 / 72.7 / 84.2 / 63.7 / 41.8 | not tested | — | — | — | thermal surface cracks: none / none / 18.2 / 18.9 / 19.6 | 15.8 / 13.1 / 5.9 / 3.2 / 2.1 | Table 5 |
| same | PS-I @30 / 200 / 400 / 600 / 800 °C | 28 | 75.1 / 86.8 / 73.8 / 58.3 / 32.7 | not tested | — | — | — | none / 17.2 / 213.0 / ≈90 ⚠️ / 271.1 | 14.3 / 15.6 / 11.8 / 6.4 / 3.9 | Table 5 |
| same | PS-II @30 / 200 / 400 / 600 / 800 °C | 28 | 93.8 / 85.6 / 99.3 / 68.4 / 39.0 | not tested | — | — | — | none / none / 22.3 / 68.5 / 74.4 | 15.9 / 15.4 / 13.9 / 10.9 / 6.6 | Table 5 |
| [[herbert2013-ecc-self-healing-natural-environment]] | ECC HVFA @0.5% pre-strain | 7 | — | coupon 200×76×12.5 mm | n.r. | n.r. | ≥ 0.5 (pre-strain, not capacity) | 24 (residual; sentence cites ref. [29], possibly not measured here ⚠️) | — | §2.1, p. 2834 |
| same | ECC HVFA @1.0% pre-strain | 7 | — | same | n.r. | n.r. | ≥ 1.0 (pre-strain) | 30 (residual; as above ⚠️) | — | §2.1, p. 2834 |
| [[sui2018-uhp-ecc-flexural-fatigue]] | UHP-ECC | 28 | 102.8 (100 mm cube) | — | — | — | — | — | — | Sect. 2.2, p. 4 |
| same | UHP-ECC | 90 (tension age n.s. ⚠️) | 120.7 (100 mm cube) | dog-bone 330 mm, gauge 80 × 30 × 13 mm (Fig. 3a), 2 LVDTs | ≈ 8–9.5 (at ≈ 0.3–0.5% strain) | ≈ 11.1 (avg curve; specimens ≈ 11.5 / 11.6 / 12.4) | ≈ 8.3 (avg curve; specimens ≈ 7.9 / 8.8 / 6.9; end of hardening) | < 160 (≈ 80 at 0.5%, ≈ 140 at 3–4%, ≈ 160 at 7–8%) | about 22 (4-pt, 100 × 100 × 400, span 300; peak ≈ 21–22 at ≈ 9–11 mm) | pp. 4–7; Figs. 3–5, 7 (read-off) |
| same | UHP-ECC after 2 × 10⁶ cycles at S = 0.5 | 90 | — | — | — | — | — | — | 86% of static (about 19, computed; Fig. 7 post-fatigue static ≈ 18–20) | Sect. 3.1, p. 6; Fig. 7 |
| [[jin2019-hvfa-shcc-structural]] | FA2.4 | 28 (flexure 7 / 90) | 46.7 (E 22.2 GPa; Fig. 8a, c) | dumbbell 30 × 30 mm, 80 mm gauge | 3.67 | 3.97 | 1.92 (≈ at peak, Fig. 7) | n.r. | 11.6 / 16.8 (7 / 90 d; coupon 350 × 50 × 15, span 300); cracking 7.2 / 9.6 | Table 5, p. 10; Figs. 8, 14, pp. 11–15 |
| same | FA2.8 | 28 (flexure 7 / 90) | 41.2 (E 20.6 GPa) | not tested in tension | — | — | — | n.r. | 11.1 / 14.4; cracking 6.6 / 9.2 | Figs. 8, 14 |
| same | FA3.2 | 28 (flexure 7 / 90) | 39.9 (E 20.3 GPa) | same as FA2.4 | 3.34 | 4.10 | 3.42 (≈ at peak) | n.r. | 13.6 / 16.7; cracking 5.5 / 9.1 | Table 5; Figs. 8, 14 |
| same | FA3.6 | 28 (flexure 7 / 90) | 38.8 (E 19.1 GPa) | not tested in tension | — | — | — | n.r. | 9.8 / 14.5; cracking 5.2 / 8.7 | Figs. 8, 14 |
| same | FA4.0 | 28 (flexure 7 / 90) | 37 (E 17.5 GPa) | not tested in tension | — | — | — | n.r. | 11.1 / 13.9; cracking 4.9 / 8.3 | Figs. 8, 14 |
| same | FA4.4 | 28 (flexure 7 / 90) | 32.5 (E 15.7 GPa) | same as FA2.4 | 3.26 | 3.99 | 3.07 (≈ at peak; high scatter) | n.r. | 10.2 / 13.1; cracking 4.8 / 8.2 | Table 5; Figs. 8, 14 |
| same | FA3.2 compression vs age | 7 / 28 / 90 | ≈ 18.5 / ≈ 40 / ≈ 45 (7 d = 46.6% of 28 d; 90 d ≈ +12%) | — | — | — | — | — | — | Fig. 9, p. 12; §3.3.2 |
| [[sun2019-modified-pva-fiber-ecc]] | C0 / C1 / C2 / C3 | 28 | 44.4 / 40.6 / 42.6 / 34.2 | — | — | — | — | — | 5.7 / 18.2 / 19.1 / 12.5 (ISO 679 mortar prism) | Table 8, p. 11 |
| same | S1 (W/B 0.30) | 7 | 33.0 | JSCE dumbbell 330 mm, 30 mm × (13 or 30) mm section, 80 mm gauge (Fig. 1, p. 7) | 2.67 | 3.52 | 3.79 (end of curve incl. softening, not peak; Fig. 6 bar ≈ 2.3–5.25) | n.r. | ≈ 9.7 (7 d, Fig. 5) | Table 10, p. 13; Figs. 5–6, p. 13 |
| same | S4 (untreated REC-15) | 7 / 28 | ≈ 26.3 (7 d, Fig. 5) / n.r. | same | 2.63 / 3.2 | 3.3 / 3.3 | 3.21 / 1.39 (end of curve; 7-d peak ≈ 2.9) | n.r. | ≈ 9.3 (7 d) | Table 11, p. 16; Fig. 5 |
| same | S2 (VAE REC-15) | 7 / 28 | ≈ 30.3 (7 d, Fig. 5) / n.r. | same | 2.67 / 3.4 | 3.33 / 3.4 | 4.05 / 2.18 (end of curve) | n.r. | ≈ 10.9 (7 d) | Table 11, p. 16; Fig. 5 |
| same | S3 (boric + SB) | 7 | ≈ 23.7 (Fig. 5) | same | 2.5 | 2.83 | 2.02 (end of softening; peak ≈ 1.0) | n.r. | ≈ 9.4 (7 d) | Table 10, p. 13; Figs. 5, 9 |
| same | G1 / G2 (domestic PVA) | 7 | n.r. | same | 2.22 / 2.26 | 2.86 / 2.79 | 0.46 / 0.97 (end of curve) | n.r. | — | Table 10, p. 13 |
| [[wang2019-rc-beam-ecc-shear-strengthening]] | ECC PVA 1.5% | 28 | 55.9 (100 mm cube) | dogbone, gauge 13 × 30 × 80 mm, 0.2 mm/min | 4.05 | 4.84 (curve peaks ≈ 4.6–5.1) | ≈ 0.9–1.9 at peak (3 curves); ultimate ≈ 2.6–3.45 (read from Fig. 2) | n.r. | — | Sect. 2.1–2.2, p. 3; Fig. 2, p. 3; Table 1, p. 4 (E 24.9 GPa) |
| [[chavesfigueiredo2020-printed-shcc]] | XVA3PVA20 printed, LPA | 35 (tension); 28 (f'c) | 44.09 (35 mm cube, load ⟂ layers); 41.93 (∥) | 1-layer sawn plate 10 × 40 × 150 mm, glued, load ∥ print path | 1.53 | 2.4 | 0.26 (at peak) | n.s. | MOR 1.84 (notched 3PB); 4PB MOR ≈ 7.0–7.5 (28 d, Fig. 6) | Tables 2–5, pp. 8–12; Fig. 6, p. 11 |
| same | XVA3PVA20 printed, LPE | 35 | same | 10 × 35 × 30 mm, load ⟂ print path in-plane | 1.84 | 2.41 | 0.31 (at peak) | n.s. | — | Tables 4–5, p. 12 |
| same | YVA4PVA20-S05 printed, LPA | 35; 28 | 17.66 (⟂); 15.02 (∥) | as X-LPA | 1.28 | 1.64 | 0.15 (at peak) | n.s. | MOR 0.97 (notched 3PB); 4PB MOR ≈ 3.3–3.9 (28 d, Fig. 6) | Tables 2–5, pp. 8–12; Fig. 6, p. 11 |
| same | YVA4PVA20-S05 printed, LPE | 35 | same | as X-LPE | 1.15 | 1.65 | 0.29 (at peak) | n.s. | — | Tables 4–5, p. 12 |
| [[mohammed2020-cr-ecc-elevated-temperature]] | M6 (0% CR) @24 / 100 / 400 / 500 / 800 / 900 / 1000 °C | 28 (+ 24 h 60 °C) | ≈ 75 / ≈ 79 / ≈ 69 / ≈ 45 / ≈ 25 / 20 / ≈ 16 (50 mm cube, residual) | not tested | — | — | — | — | — | Fig. 3, p. 7 (read-off); 900 °C text p. 7 |
| same | M3 (2.5% CR) @24 / 100 / 400 / 500 / 800 / 1000 °C | 28 (+ 24 h 60 °C) | ≈ 58 / 47.66 / ≈ 42 / 39.81 / ≈ 24 / ≈ 13 | not tested | — | — | — | — | — | Fig. 3, p. 7 (read-off); bold values text p. 7 |
| same | M4 (5% CR) @24 / 100 / 400 / 500 / 800 / 1000 °C | 28 (+ 24 h 60 °C) | ≈ 46 / 41.7 / ≈ 39 / ≈ 38 / ≈ 21 / ≈ 11 | not tested | — | — | — | — | — | Fig. 3, p. 7 (read-off); 41.7 text p. 7 |
| same | RSM mixes @24 °C | 28 | 30–75 (range) | not tested | — | — | — | — | — | Fig. 2, p. 6 |
| [[ivaniuk2022-printable-shcc-design]] | Ref (printed) | 28 (f'c, flex); tension n.s. | 83.2 / 73.0 / 82.2 (D1/D2/D3, 40 mm cube) | 600 × 40 × 20 mm prism from 1 printed layer, cast dumbbell ends, 1 mm/min | ≈ 3 (Fig. 17) | 5.4 (curve peaks ≈ 5.3–5.5) | ≈ 2.0–3.0 (onset of softening, Fig. 17; peak vs ultimate n.s. ⚠️) | n.s. | 22.0 (D1) / 18.5 (D3), 3PB 160×40×40 | Tables 2–3, p. 14; Fig. 17, p. 15 |
| same | SE-CE (printed) | same | 80.9 / 80.1 / 79.5 | same | ≈ 3 (Fig. 17) | 4.1 (curve peaks ≈ 4.3–4.6) | ≈ 2.0–2.6 (onset of softening, Fig. 17) | n.s. | 21.4 / 17.4 | Tables 2–3, p. 14; Fig. 17, p. 15 |
| [[shumuye2022-slag-fa-pe-ecc]] | SF-0-60 | 28 | 40.79 (100 mm cube) | dogbone 330 mm, gauge zone 80 × 30 × 13 mm (Fig. 1, p. 5), 0.4 mm/min | 2.25 | 5.35 | ≈ 2.0 at peak (text; Fig. 5b ≈ 1.9) | ≈ 100 (radar Fig. 10) | ult. load 403.48 "kN" as printed ⚠️ (3PB span 240 mm; probably N → ≈ 14–20 MPa, computed) | Table 4, p. 8; Sect. 3.1–3.2; Figs. 4–5, 10 |
| same | SF-5-55 | 28 | 42.23 (Fig. 4) | same | 1.23 | 5.20 | 3.5 at peak (Fig. 5b ≈ 3.45) | ≈ 105 (Fig. 10) | 438.00 ⚠️ | same |
| same | SF-10-50 | 28 | 52.44 (Fig. 4) | same | 2.51 | 5.70 | ≈ 2.9 at peak (Fig. 5b ≈ 3.0) | ≈ 110 (Fig. 10) | 553.48 ⚠️ | same |
| same | SF-15-45 | 28 | 55.05 | same | 2.57 | 5.18 | ≈ 2.2 at peak (Fig. 5b read-off; text "similar") | ≈ 130, largest (Fig. 10) | 543.12 ⚠️ | same |
| same | SF-0-60 / 5-55 / 10-50 / 15-45 | 7 | 29.03 / 36.88 / 45.6 / 51.48 (Fig. 4; +0 / +27.0 / +57.0 / +77.3%) | same | 2.21 / 1.42 / 1.88 / 1.29 | 6.57 / 4.48 / 6.59 / 5.26 | ≈ 1.85 / 0.75 / 1.25 / 1.5 at peak (Fig. 5a, low precision) | n.r. | 445.70 / 411.30 / 531.90 / 561.50 ⚠️ | Table 4, p. 8; Sect. 3.1; Figs. 4–5 |
| [[zhang2022-ecc-carbonation-sustained-load]] | ECC (SDU) | 28 | — | none (4-pt flexure 400×100×50, span 300) | 7.41 (flexural first crack) | — | — | — | 11.41 | §2.2, p. 3 |
| [[zhao2022-ecc-tension-damage-model]] | V1R3 (1%, 0.28) | ≥ 35 ⚠️ | n.r. | plate 280 × 40 × 13 mm, CFRP tabs, 120 mm gauge | 1.976 | 3.104 | 0.511 (peak); 1.895 (rupture) | n.r. | — | Table 3 |
| same | V2R3 (1.5%, 0.28) | ≥ 35 | n.r. | same | 2.020 | 2.959 | 0.796; 2.539 | n.r. | — | Table 3 |
| same | V3R1 (2%, 0.24) | ≥ 35 | n.r. | same | 3.440 | 4.572 | 0.503; 2.230 | n.r. | — | Table 3 (n = 3) |
| same | V3R2 (2%, 0.25) | ≥ 35 | n.r. | same | 2.665 | 3.787 | 1.071; 2.975 | n.r. | — | Table 3 |
| same | V3R3 (2%, 0.28) | ≥ 35 | n.r. | same | 2.447 | 3.234 | 2.000; 4.077 | n.r. | — | Table 3 |
| same | V-V1R3 / V-V2R3 / V-V3R2 / V-V3R3 (ref 43 validation set) | n.s. | n.r. | n.s. | 2.165 / 2.483 / 2.518 / 2.542 | 2.760 / 3.063 / 3.712 / 3.349 | 0.474 / 0.864 / 1.371 / 2.010 (peak) | n.r. | — | Table 5 (data of Li K. et al. 2022, as cited) |
| [[xue2023-shcc-structural-review]] | PE-SHCC (as cited) | n.s. | — | dumbbell 13 × 30 mm, 100 mm gauge | 4.2 | 7–8 | 1.5–2.2 (at peak; Fig. 1 B2 marker ≈ 2.6% vs text 2.2% ⚠️) | n.s. | — | Section 2, p. 3; Fig. 1 |

Related: [[mix-designs]], [[tensile-strain-capacity]], [[review-outline]]
