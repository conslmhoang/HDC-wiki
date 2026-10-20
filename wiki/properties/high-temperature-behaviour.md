---
type: property
slug: high-temperature-behaviour
aliases: [fire resistance, elevated temperature, residual strength after heating, spalling]
tags: [durability, fire]
sources: [ma2021-ecc-durability-review, yu2018-ecc-direct-tensile-review, he2024-hdc-research-advances, ranade2017-hshdc-impact-resistance, chai2023-hdc-ambient-temperature, zhou2023-hsecc-elevated-temperature, mohammed2020-cr-ecc-elevated-temperature, vanzijl2010-shcc-durability]
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
  - PVA: **melting onset 230 °C by TG, thermal instability 220–420 °C** (primary,
    [[zhou2023-hsecc-elevated-temperature]], Fig. 4); 230 °C also stated (as cited) in
    [[mohammed2020-cr-ecc-elevated-temperature]], §3.3; decomposition 263 °C (PP 271 °C) as cited in
    [[vanzijl2010-shcc-durability]], p. 266; 235 and 250 °C cited in Zhou 2023. The earlier "230–273 °C ⚠️"
    range is now anchored at its low end (230 °C onset); 273 °C is not supported by any ingested source.
    → [[pva-fiber]]

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
> Primary residual tests (2026-10-20) agree: PVA-ECC flexural capacity collapses between 200 and 400 °C
> as PVA melts from 230 °C ([[zhou2023-hsecc-elevated-temperature]]). The same melting is the benefit
> for spalling: melt channels release vapour, so PVA-ECC did not spall explosively up to 800–1000 °C in two
> independent studies, whereas partial steel-fibre replacement brought slight spalling back.

## Elevated temperature: primary data (residual tests)
Neither primary study below reports a tension test, so retention of **strain hardening** after heating is
not shown; Zhou 2023's prisms soften after peak even at 30 °C (Fig. 10).

**[[zhou2023-hsecc-elevated-temperature]]** — "HSECC", W/B 0.20, FA/C 1.2, 2.0 vol.% fibre; 20 °C/min, 1 h hold,
cooled, 100 mm cubes and 40×40×160 prisms (Table 5):

| Mix | Property | 30 °C | 200 °C | 400 °C | 600 °C | 800 °C |
|---|---|---|---|---|---|---|
| PO (2.0% PVA) | f_c (MPa) | 83.1 | 72.7 | 84.2 | 63.7 | 41.8 |
| PO | f_f (MPa) | 15.8 | 13.1 | 5.9 | 3.2 | 2.1 |
| PO | mass loss (%) | — | 5.43 | 7.43 | 9.56 | 11.22 |
| PS-II (1.0% PVA + 1.0% steel) | f_c (MPa) | 93.8 | 85.6 | 99.3 | 68.4 | 39.0 |
| PS-II | f_f (MPa) | 15.9 | 15.4 | 13.9 | 10.9 | 6.6 |

- PVA turns black at 200–400 °C, melts completely by 400 °C leaving channels up to 21.5 µm wide, and is
  gone at 600 °C (Figs. 3, 11). PO flexural capacity collapses between 200 and 400 °C (−63% vs 30 °C).
- f_c rebound at 400 °C attributed to further hydration and pozzolanic FA reaction (p. 754).
- **Spalling**: none in PVA-only ECC up to 800 °C; replacing 0.5–1.0% PVA by copper-coated steel caused
  slight spalling at 800 °C and wider thermal surface cracks (up to 271.1 µm, PS-I), attributed to fewer PVA
  melt channels for vapour release (p. 752). Steel fibre nevertheless raises residual f_c and f_f above 400 °C
  (f_f/f_c PS-II 0.14–0.18 vs PO 0.05 at 800 °C); its oxide film at ≈750–800 °C lets it pull out (Fig. 12).
  → [[hybrid-fiber]]

**[[mohammed2020-cr-ecc-elevated-temperature]]** — "CR-ECC", oiled Kuraray PVA, FA/C 1.2, crumb rubber 0–5% of
sand; 15 °C/min to 100–1000 °C, 1 h, natural cooling, 50 mm cubes, pre-dried 24 h at 60 °C:
- **No explosive spalling in any mix up to 1000 °C**; visible deterioration only above 600 °C (Section 3.3).
- 0% CR mix gains f'c at 100 °C, drops 34% between 400 and 500 °C; all mixes ≈11 MPa (≈20% of room
  temperature) at 1000 °C (Section 3.2, Fig. 3 ⚠️ values from figure).
- Crumb rubber lowers residual f'c at all temperatures but reduces visible cracking at 900 °C; CR said to
  melt at 170 °C (uncited ⚠️) and open vapour paths. → [[crumb-rubber]]
- Caveat: pre-drying and small cubes both lower spalling risk.

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

## Conflicts & open questions
- ⚔️ (minor) Residual f'c of PVA-ECC at 400–500 °C: rises at 400 °C ([[zhou2023-hsecc-elevated-temperature]], HSECC W/B 0.20)
  vs drops 34% between 400 and 500 °C ([[mohammed2020-cr-ecc-elevated-temperature]], normal-strength CR-ECC).
  Different matrices and temperature steps; not a direct contradiction.
- ⚠️ Mohammed 2020's introduction attributes "SH lost beyond 200 °C, σ_t −40%" to a reference that appears mis-cited.
- Open: in-situ (hot) tension of HDC; fire tests on members; heat-retardation by polymer-fibre melting
  ([[vanzijl2010-shcc-durability]], p. 266); any fire data for PE-HSHDC.

## Related
- [[pe-fiber]] · [[pva-fiber]] · [[hybrid-fiber]] · [[crumb-rubber]] · [[durability]] · [[gaps]]
