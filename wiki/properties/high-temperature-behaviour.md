---
type: property
slug: high-temperature-behaviour
aliases: [fire resistance, elevated temperature, residual strength after heating, spalling]
tags: [durability, fire]
sources: [ma2021-ecc-durability-review, yu2018-ecc-direct-tensile-review, he2024-hdc-research-advances, ranade2017-hshdc-impact-resistance, chai2023-hdc-ambient-temperature]
updated: 2026-10-20
---

# High-Temperature Behaviour

## Quantitative evidence
PE-ECC tension (Luo 2019, as cited in [[ma2021-ecc-durability-review]], Table 1, p. 4):

| T (°C) | 20 | 50 | 100 | 140 | 200 |
|---|---|---|---|---|---|
| ε_tu (%) | 9.08 | 10.74 | 9.32 | **1.61** | **0.021** |
| σ_tu (MPa) | 9.46 | 10.65 | 8.68 | 8.10 | 6.84 |

Whether these are hot or residual tests is not stated ⚠️.

**PVA-ECC** (as cited in [[ma2021-ecc-durability-review]] and [[yu2018-ecc-direct-tensile-review]], p. 352–353):
- Mechtcherine 2012 (in situ): ε rises at 60 °C; strain hardening is lost at 150 °C.
- Bhat 2014:
  - still strain-hardening at 100 °C;
  - 0.5–0.8% strain at 200 °C;
  - brittle at 300 °C;
  - fibers decomposed at 400–600 °C.
- Yu J. 2015 (high-volume FA): σ and ε rise at 50–100 °C (stronger interface), then fall at 200 °C.

## Key points
- **Melting fibers set the limit:**
  - PE melts at about 124–150 °C → [[pe-fiber]];
  - PVA melts at about 230–273 °C ⚠️ (values vary between sources) → [[pva-fiber]].

  This explains the loss of strain hardening between 100 and 200 °C.
- **Spalling:**
  - PVA fibers eliminate explosive spalling, and more fly ash helps further (Sahmaran 2011, as cited, p. 3).
  - Ordinary concrete spalls at 200–350 °C (Naus 2006, as cited).
  - PVA-ECC produces 4× the debris of steel-fiber ECC at 600 °C (Pourfalah 2018, as cited).
- **Compression:** f'c and stiffness stay about constant up to 200 °C, then fall linearly by
  more than 75% at 800 °C (Shang & Lu 2014, as cited).
- **HDC:** the cooling method has a negligible effect at 200 °C, but resting time matters at
  400 °C (Deng 2020, as cited in [[he2024-hdc-research-advances]], p. 7).
- PE melting is flagged as a concern for blast and fire ([[ranade2017-hshdc-impact-resistance]], p. 31).

> Synthesis: ECC/HDC ductility is a **low-temperature property**. Above about 150 °C (PE) or about
> 200 °C (PVA), the material loses strain hardening. Fire is therefore a key limit for PE-based HSHDC.

## Low and moderate temperatures: primary data ([[chai2023-hdc-ambient-temperature]])
Chinese PVA-HDC, 28 d standard cure, then 8 h at the test temperature, 1 h at 20 °C (residual tests):

| T (°C) | −30 | 0 | 20 | 40 | 60 |
|---|---|---|---|---|---|
| f_cu (MPa) | 46.7 | 47.1 | 48.0 | 50.9 | 52.7 |
| σ_tu (MPa) | 3.74 | 3.99 | 4.23 | 4.46 | 4.80 |
| ε_tu (%) | 1.34 | 1.46 | 1.15 | 1.23 | 1.31 |
| Flexural strength (MPa) | 12.23 | 13.08 | 14.08 | 14.65 | 15.64 |

Tables 5–8. Strain hardening is kept at every temperature; ε_tu peaks at 0 °C.

- ⚔️ Dong et al. 2022 (PE-HDC, −20 to 90 °C, as cited in [[chai2023-hdc-ambient-temperature]]) found f'c and σ_tu *falling* with
  temperature and ε_tu rising steadily. Fiber type and in-situ vs residual testing may explain it. → [[gaps]]
- Only 8 h exposure was tested; years of service are not represented (§3.6).

## Related
- [[pe-fiber]] · [[pva-fiber]] · [[durability]] · [[gaps]]
