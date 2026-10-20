---
type: property
slug: fatigue
aliases: [cyclic loading, fatigue life, S-N curve, tension-compression cycling, flexural fatigue]
tags: [durability, cyclic]
sources: [ma2021-ecc-durability-review, yu2018-ecc-direct-tensile-review, sui2018-uhp-ecc-flexural-fatigue, kunieda2006-hpfrcc-japan-applications, kanakubo2006-dfrcc-tensile-test-method, xue2023-shcc-structural-review]
updated: 2026-10-20
---

# Fatigue & Cyclic Loading

## Primary data: flexural fatigue of PE UHP-ECC ([[sui2018-uhp-ecc-flexural-fatigue]])
PE "UHP-ECC" (cube f'c 102.8 MPa at 28 d), 100 × 100 × 400 mm prisms, 4-pt bending, span 300 mm, static
MOR about 22 MPa (Fig. 7), 3 beams per stress level S = σ_max/static strength:

| S | Fatigue life N (cycles) | Cracks at failure | Deformation stages |
|---|---|---|---|
| static | — | 45 | — |
| 0.9 | 1271–1876 | 30 | 3 |
| 0.8 | 21,852–29,565 | 20 | 3 |
| 0.65 | 155,075–308,691 | 6 | 3 |
| 0.5 | run-out at 2 × 10⁶ | 5 | 2 |

(Table 6, Table 5, Fig. 13)

- **S–N law:** S = 1 − 5.75 × 10⁻³ (lg N)^2.43, continuous, **no inflection point** (Eq. 2). This is the
  primary source of the "Sui 2018" model tabulated in [[ma2021-ecc-durability-review]] (Table 4). How run-outs
  enter the regression is ⚠️ unverified.
- After 2 × 10⁶ cycles at S = 0.5: residual flexural strength 86%; initial stiffness 130.01 → 108.12 kN/mm
  (Sect. 3.1, Table 4).
- Fatigue life is governed by the length of the stable stage II of deflection growth (Fig. 13).
- **Mechanism:** high S degrades the bond (more pull-out); low S damages the fibers (rupture) (Fig. 10).
- Fatigue crack widths grow with cycles and are larger at S = 0.8 than at 0.5 (Fig. 16). → [[crack-width]]
- A high-strength matrix does **not** reduce fatigue life compared with ordinary ECC (Conclusion 1, Fig. 19).
- Existing bilinear S–N models (Liu 2017 PVA; Suthiwarapirak 2004 PVA and PE) have an inflection at S ≈ 0.9,
  N 10²–10⁴ (as cited, Table 7). The authors link this to the inflection of the tensile crack-width vs strain
  curve, i.e. a critical crack width (Fig. 20).

## Comparison with FRC (as cited)
- Flexural S–N of PVA-ECC and PE-ECC is **bilinear** on a semi-log plot; HPFRCC has longer lives than FRC at
  high stress but shorter at low stress, because few cracks propagate (Matsumoto 2003, as cited in
  [[kunieda2006-hpfrcc-japan-applications]], p. 21). Fatigue design data are listed as a need (p. 21).
- PVA-ECC outlives PE-ECC at high S, PE-ECC outlives PVA at low S (Suthiwarapirak 2004, as cited in
  [[sui2018-uhp-ecc-flexural-fatigue]], Sect. 4).
- RC beams with 10 mm sprayed HPFRCC: 130 vs 250 µm crack width after 17 million cycles (railway viaduct
  background tests, [[kunieda2006-hpfrcc-japan-applications]], p. 30). An ECC layer improves fatigue life
  (Leung & Zhang 2007, as cited in [[xue2023-shcc-structural-review]], Table 1).
- Slab strengthening by spraying requires tensile capacity **and** fatigue resistance
  ([[kanakubo2006-dfrcc-tensile-test-method]], Table 1).

## Key points (reviews)
- ECC fatigue life is orders of magnitude above that of concrete. S–N models (Sui 2018,
  Liu 2017, Suthiwarapirak 2004, with separate PVA and PE models) are tabulated in
  [[ma2021-ecc-durability-review]] (Table 4, p. 8–9).
- Crack growth follows da/dN = c·ΔK_tip^m (Qiu & Yang 2017, as cited, Eqs. 5–6).
- In tensile fatigue, bridging stress drops within the first 600–1000 cycles (Huang 2017, as cited, p. 9).
  → [[fiber-bridging]]
- **Cyclic tension–compression** does not reduce ε_tu as long as f'c is not exceeded
  (Kesner 2003; Jun 2010, as cited in [[yu2018-ecc-direct-tensile-review]], p. 355–357).
  Fatigue life falls with a higher upper stress level and with tension–compression loading (Müller 2017).
- Quasi-static cyclic results may overestimate the response at seismic rates
  ([[yu2018-ecc-direct-tensile-review]], p. 357). → [[strain-rate-effects]]

> Synthesis: ⚔️ the S–N shape is disputed. Earlier PVA/PE-ECC models are bilinear with an inflection near
> S ≈ 0.9 (Matsumoto; Suthiwarapirak; Liu), whereas the only primary PE UHP-ECC data in the wiki fit a
> continuous curve without inflection (Sui 2018). Sui's own data set is small (3 beams per level, one mix),
> and the authors say there are too few data to locate an inflection. → [[gaps]]

## Related
- [[durability]] · [[self-healing]] · [[strain-rate-effects]] · [[flexural-strength]]
