---
type: property
slug: high-temperature-behaviour
aliases: [fire resistance, elevated temperature, residual strength after heating, spalling]
tags: [durability, fire]
sources: [ma2021-ecc-durability-review, yu2018-ecc-direct-tensile-review, he2024-hdc-research-advances, ranade2017-hshdc-impact-resistance, chai2023-hdc-ambient-temperature, zhou2023-hsecc-elevated-temperature, mohammed2020-cr-ecc-elevated-temperature, vanzijl2010-shcc-durability, pourfalah2018-ecc-high-temperature]
updated: 2026-10-21
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
  - Debris at 600 °C (hot test): PVA-ECC 30% of cube mass vs **hybrid PVA + steel** HECC 8.5% (≈ 3.5×;
    "4×" in the Conclusions) ([[pourfalah2018-ecc-high-temperature]], Fig. 7b). Correction: the earlier
    second-hand wording "steel-fiber ECC" was imprecise — the comparison is with a PVA + 0.75% steel hybrid.
- **Compression:** f'c and stiffness stay about constant up to 200 °C, then fall linearly by
  more than 75% at 800 °C (Shang & Lu 2014, as cited).
- **HDC:** the cooling method has a negligible effect at 200 °C, but resting time matters at
  400 °C (Deng 2020, as cited in [[he2024-hdc-research-advances]], p. 7).
- PE melting is flagged as a concern for blast and fire ([[ranade2017-hshdc-impact-resistance]], p. 31).

> Synthesis: ECC/HDC ductility is a **low-temperature property**. Above about 150 °C (PE) or about
> 200 °C (PVA), the material loses strain hardening. Fire is therefore a key limit for PE-based HSHDC.
> Hot tests ([[pourfalah2018-ecc-high-temperature]]) confirm the window: ductility first *rises* to 60–100 °C,
> then PVA pulls out from 150 °C and ECC is brittle from 200 °C, matching Mechtcherine 2012 (as cited).
> Primary residual tests (2026-10-20) agree: PVA-ECC flexural capacity collapses between 200 and 400 °C
> as PVA melts from 230 °C ([[zhou2023-hsecc-elevated-temperature]]). The same melting is the benefit
> for spalling: melt channels release vapour, so PVA-ECC did not spall explosively up to 800–1000 °C in two
> independent studies, whereas partial steel-fibre replacement brought slight spalling back.

## Elevated temperature: primary data (hot / in-situ tests)
**[[pourfalah2018-ecc-high-temperature]]** — first primary **hot** tests in the wiki. "ECC" (PVA 12 mm × 40 µm,
2.0 vol.% derived from 26 kg/m³, FA/C 1.80, W/B 0.28 derived) and "HECC" (H6ECC / H13ECC: PVA 1.75% + straight
steel 6 or 13 mm × 150 µm, 0.75%). Strain hardening shown at 20 °C (dog-bones: ε at peak 3.5 / 3.0 / 2.5%,
Table 4). Heated at 10 °C/min, 30 min hold, tested inside the chamber (§3.4). 50 mm cubes and 170×40×20 mm
prisms in four-point bending.

| Mix | Property | 20 °C | 200 °C | 400 °C | 600 °C |
|---|---|---|---|---|---|
| ECC | hot f'c (MPa) | 38.8 | 36.15 | 35.1 | 29.2 |
| H6ECC | hot f'c (MPa) | 40.1 | 38.45 | 32 | 27.2 |
| H13ECC | hot f'c (MPa) | 45 | 38.5 | 32.8 | 29.5 |

Table 5. Compressive modulus of ECC 40.2 → 19.4 GPa at 600 °C (Table 5).

- **No spalling** of ECC or HECC up to 600 °C (§4.2). Mass loss ≈ 10 / 12 / 14% at 200 / 400 / 600 °C (Fig. 7a).
- **Ductility rises first, then collapses**: bending deflection capacity rises up to 60–100 °C (ECC ≈ 3× at
  60 °C), then deflection-softening from 150 °C; ECC is brittle from 200 °C (Fig. 10c, Conclusions). Crack count
  drops from ≈ 15–23 at 20 °C to one crack from 150 °C (Fig. 10d).
- Bending crack width: ECC ≈ 50 µm at 20 °C but hundreds of µm at 60–100 °C (text 400 / 750 µm; Fig. 10e
  ≈ 570–1070 µm ⚠️); HECC 40 → 70 → 200 µm (§4.3, Fig. 10e). → [[crack-width]]
- **Fibre failure mode**: PVA ruptures below 150 °C, pulls out fully at 150 °C (pull-out length 500 → 6000 µm),
  is dark/burned at 200 °C and absent at 400 °C (Fig. 12). Steel pulls out up to 400 °C and ruptures at 600 °C
  (Fig. 14). → [[pva-fiber]], [[fiber-matrix-interface]]
- **Steel hybrid** keeps ≈ 2× the ECC peak bending load at 100–600 °C and limits crack width ≈ 5× at 60–100 °C
  (Conclusions). Bending peak load of ECC falls from 20 to 60 °C (Fig. 10b). → [[hybrid-fiber]]
- ⚠️ The author's claim of a PVA glass transition at 60 °C with 80% modulus loss is uncited (p. 928); not adopted.

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
- **No explosive spalling in any mix up to 1000 °C**; visible deterioration only above 600 °C (Section 3.3, p. 8).
- Residual f'c (MPa, M6 0% / M3 2.5% / M4 5% CR; ≈ read from Fig. 3, p. 7, ±1 MPa, except values stated in the text):
  24 °C ≈ 75 / 58 / 46; 100 °C ≈ 79 / 47.66 / 41.7; 400 °C ≈ 69 / 42 / 39; 500 °C ≈ 45 / 39.81 / 38;
  800 °C ≈ 25 / 24 / 21; 1000 °C ≈ 16 / 13 / 11.
- 0% CR mix gains f'c at 100 °C (≈ 75 → 79 MPa), drops 34% between 400 and 500 °C (text, p. 7). At 1000 °C the **CR mixes**
  are ≈ 11–13 MPa (text: "approximately 11") and the **0% CR mix ≈ 16 MPa** — ≈ 21–24% of the 24 °C strength (text:
  "about 20%") (Section 3.2, pp. 6–7; Fig. 3). (Corrected 2026-10-21: earlier text said "all mixes ≈ 11 MPa".)
- Not stated in the text: both CR mixes *lose* ≈ 17% and ≈ 10% between 24 and 100 °C; the authors' 83% / 91% retention at
  500 °C is relative to 100 °C (vs 24 °C ≈ 69% / ≈ 83%). Above ≈ 500 °C the three curves converge, so the CR penalty
  largely disappears (Fig. 3, p. 7).
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
- ⚔️ (minor) 20 → 60 °C: hot bending peak load of PVA-ECC **falls** ([[pourfalah2018-ecc-high-temperature]], Fig. 10b)
  vs residual flexural strength of PVA-HDC **rises** 14.08 → 15.64 MPa ([[chai2023-hdc-ambient-temperature]]).
  Supports "in-situ strength falls, residual strength rises"; in-situ vs residual testing is the likely reason. → [[gaps]]

## Conflicts & open questions
- ⚔️ (minor) Residual f'c of PVA-ECC at 400–500 °C: rises at 400 °C ([[zhou2023-hsecc-elevated-temperature]], HSECC W/B 0.20)
  vs drops 34% between 400 and 500 °C ([[mohammed2020-cr-ecc-elevated-temperature]], p. 7; normal-strength CR-ECC).
  Different matrices and temperature steps; not a direct contradiction.
- Hot vs residual f'c at 400 °C: hot f'c of normal-strength ECC −10% at 400 °C and −25% at 600 °C
  ([[pourfalah2018-ecc-high-temperature]], Table 5) — a third data point for the row above; test mode is an
  extra variable.
- ⚔️ (minor) PVA "burned" at 200 °C in a hot test ([[pourfalah2018-ecc-high-temperature]], Fig. 12) vs TG melting
  onset 230 °C ([[zhou2023-hsecc-elevated-temperature]]). Consistent with in-situ loss of SH at 150 °C.
- Spalling of steel hybrids: none to 600 °C ([[pourfalah2018-ecc-high-temperature]]) vs slight at 800 °C
  ([[zhou2023-hsecc-elevated-temperature]]); temperature ranges do not overlap.
- ⚠️ Mohammed 2020's introduction attributes "SH lost beyond 200 °C, σ_t −40%" to a reference that appears mis-cited.
- To verify ([[pourfalah2018-ecc-high-temperature]]): crack widths at 60/100 °C (text vs figure); "14% and 25%"
  f'c loss in Conclusions vs per-mix values.
- Open: in-situ (hot) **tension** of HDC (Pourfalah tested hot compression and bending only); fire tests on members; heat-retardation by polymer-fibre melting
  ([[vanzijl2010-shcc-durability]], p. 266); any fire data for PE-HSHDC.

## Related
- [[pe-fiber]] · [[pva-fiber]] · [[hybrid-fiber]] · [[crumb-rubber]] · [[durability]] · [[crack-width]] · [[fiber-matrix-interface]] · [[gaps]]
