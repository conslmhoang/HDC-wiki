---
type: property
slug: durability
aliases: [sulfate attack, wet-dry cycles, acid attack, abrasion, leaching, ageing, durability hub]
tags: [durability, hub]
sources: [ma2021-ecc-durability-review, he2024-hdc-research-advances, yu2018-ecc-direct-tensile-review, li2021-hdc-sulfate-dry-wet, li2003-ecc-review, chai2023-hdc-ambient-temperature, vanzijl2010-shcc-durability, zhong2019-ecc-freeze-thaw, wang2023-ecc-frost-damage, chai2019-hdcc-freeze-thaw-carbonation-flexure, zhang2022-ecc-carbonation-sustained-load, bu2022-ecc-chloride-crack-width, paul2014-r-shcc-chloride-corrosion, kanda2003-sprayed-ecc, kunieda2006-hpfrcc-japan-applications, homma2009-frcc-self-healing, herbert2013-ecc-self-healing-natural-environment, ozbay2013-ecc-self-healing-sustained-load, zhou2023-hsecc-elevated-temperature, mohammed2020-cr-ecc-elevated-temperature, sun2019-modified-pva-fiber-ecc, yang2009-ecc-self-healing-wet-dry, lepech2009-ecc-water-permeability, yun2013-shcc-freeze-thaw, pourfalah2018-ecc-high-temperature]
updated: 2026-10-21
---

# Durability (hub)

> Restructured 2026-10-20. The wiki now has primary studies for most exposures; earlier this page relied
> mostly on three reviews. Second-hand values stay marked "as cited". Freeze–thaw, carbonation and chloride
> content moved to their own pages (unchanged, with new primary data added there).

## Why ECC/HDC is expected to be durable
- ECC keeps average crack widths below about 100 µm even at 3–12% strain (Fig. 5 compilation in
  [[ma2021-ecc-durability-review]], p. 2–4). Many fine cracks let water and chloride in only slowly,
  and fine cracks heal. → [[crack-width]], [[permeability]], [[self-healing]]
- SHCC durability rests on **crack control**; UHPFRC durability rests on a **dense matrix**
  ([[vanzijl2010-shcc-durability]], p. 261). → [[uhpc-vhsc]]
- Caveats from primary data: *maximum* crack width (300–400 µm at 3% strain) far exceeds the average
  (50–65 µm) ([[vanzijl2010-shcc-durability]], Fig. 4b ⚠️ read); cracks under sustained load are about 2×
  the unloaded width ([[ozbay2013-ecc-self-healing-sustained-load]], Table 3). Design should use the crack-width
  distribution, not the average ([[vanzijl2010-shcc-durability]], p. 269).

## Exposure hub
| Exposure | Primary sources (term) | Key finding | Page |
|---|---|---|---|
| Freeze–thaw (rapid) | [[zhong2019-ecc-freeze-thaw]] (ECC); [[wang2023-ecc-frost-damage]] (ECC); [[yun2013-shcc-freeze-thaw]] (SHCC, hybrid PVA+PE; ASTM C666 B; **tension after 300 cycles**) | PVA-ECC survives 300–500 cycles; plain concrete/mortar fails at 25–84 cycles; W/B is the dominant mix factor; hybrid SHCC keeps σ_tu and SH but loses some strain capacity and flexural multiple cracking | [[freeze-thaw]] |
| Freeze–thaw + carbonation (coupled) | [[chai2019-hdcc-freeze-thaw-carbonation-flexure]] (Eco-HDCC) | flexural strength −19 to −33%, deflection −24 to −50% after 15 coupled cycles; deflection hardening kept | [[freeze-thaw]], [[carbonation]] |
| Salt scaling | none (as cited in [[vanzijl2010-shcc-durability]]) | RILEM CDF 2.2 kg/m² > 1.5 limit (fails); ASTM C672 acceptable | [[freeze-thaw]] |
| Carbonation | [[zhang2022-ecc-carbonation-sustained-load]] (ECC); [[wang2023-ecc-frost-damage]] | 4.8 mm (unloaded) to 9.9 mm (δ_T 0.6) at 28 d, 20% CO₂; ⚔️ vs ≈13 mm and 0.8 mm (as cited) | [[carbonation]] |
| Chloride ingress | [[bu2022-ecc-chloride-crack-width]] (ECC); [[paul2014-r-shcc-chloride-corrosion]] (SHCC) | immersion: ≤ 100 µm ≈ uncracked; wet–dry: even 20–50 µm avg cracks carry Cl⁻ to rebar in hours | [[chloride-and-corrosion]] |
| Rebar corrosion / spalling | [[paul2014-r-shcc-chloride-corrosion]]; [[kanda2003-sprayed-ecc]] (ECC, tapered-pin test) | corrosion rate ≈ mortar but localised pitting; corrosion cracks much finer, no spalling | [[chloride-and-corrosion]] |
| Sulfate + dry–wet | [[li2021-hdc-sulfate-dry-wet]] (HDC); [[mohammed2020-cr-ecc-elevated-temperature]] (CR-ECC) | HDC loses 50% f_cu vs concrete 76% (saturated, 150 cycles) | this page |
| Acid | [[mohammed2020-cr-ecc-elevated-temperature]] (CR-ECC) | 5% H₂SO₄: slight weight gain (gypsum / ettringite) | this page |
| Water / capillary transport | [[lepech2009-ecc-water-permeability]] (ECC M45); [[homma2009-frcc-self-healing]] (FRCC); [[wang2023-ecc-frost-damage]] | cracked ECC (1.5–3%) k 1.95–7.74 × 10⁻¹⁰ m/s after healing vs 4.46 × 10⁻⁴ m/s for 500 µm mortar cracks; k ∝ w³; F-T raises capillary coefficient | [[permeability]] |
| Self-healing (incl. wet–dry) | [[yang2009-ecc-self-healing-wet-dry]] (ECC); [[homma2009-frcc-self-healing]]; [[herbert2013-ecc-self-healing-natural-environment]]; [[ozbay2013-ecc-self-healing-sustained-load]] (ECC) | CaCO₃ seals fine cracks; wet–dry RF recovery 87–100% (air dry) / 77–90% (55 °C dry); outdoor RF 90–96% in 1 week; sustained load cuts healing | [[self-healing]] |
| Elevated temperature / fire | [[pourfalah2018-ecc-high-temperature]] (ECC/HECC, **hot** tests to 600 °C); [[zhou2023-hsecc-elevated-temperature]] (HSECC); [[mohammed2020-cr-ecc-elevated-temperature]] (CR-ECC); [[chai2023-hdc-ambient-temperature]] (HDC, −30 to 60 °C) | ductility rises to 60–100 °C, PVA pull-out from 150 °C; PVA melts from 230 °C; no explosive spalling to 600–1000 °C | [[high-temperature-behaviour]] |
| Shrinkage | none primary (all as cited) | ECC 1200–1800 µε at 28 d | [[shrinkage]] |
| Fatigue | see page | — | [[fatigue]] |

## Sulfate attack with dry–wet cycles: primary data ([[li2021-hdc-sulfate-dry-wet]])
- **Protocol**: 0 / 5 / 10% / saturated Na₂SO₄; one cycle = 48 h immersion + 1 h air + 23 h oven at 50 °C;
  up to 150 cycles; XUT PVA-HDC (FA/C 1.0, 90 d) vs ordinary concrete (28 d) (§2.1, §2.3.2).
- **f_cu at 150 cycles** (initial 45.8 MPa): water 58.3, 5% 50.1, 10% 37.9, saturated 28.9 MPa (Table 4).
- **Loss relative to the water control** at 150 cycles in saturated solution: HDC 50.3% vs concrete 76.3%;
  in 5% solution HDC loses 4.7% at 90 cycles and 14.0% at 150 (§3.2). Corrosion coefficient K_f = 1.09
  (5%, 150 cycles).
- **Mechanism**: drying micro-cracks, Na₂SO₄·10H₂O crystallisation, ettringite and gypsum filling pores
  then cracking; PVA fibers slow crack growth (§4.2).
- **Refines the He 2024 summary** ("rises to 30 cycles, falls after 105"): this fits the 5% series only;
  at 10% f_cu dips at 60 and peaks at 105 cycles; in saturated solution it falls from 60 cycles.
- **Not tested**: tension, crack width, mass or XRD after exposure. The strain-hardening of this "HDC" is not shown.
- CR-ECC in 5% Na₂SO₄: crumb rubber reduces length change; several specimens shrank
  ([[mohammed2020-cr-ecc-elevated-temperature]], Fig. 10; SH not shown). → [[crumb-rubber]]

## Sulfate, acid, abrasion, leaching, ASR (mostly second-hand)
- **Sulfate (as cited):**
  - 200 d in sulfate or sulfate+chloride: tensile strength rose, ε stayed > 2%, cracks stayed < 50 µm
    (Liu 2017, as cited in [[ma2021-ecc-durability-review]], p. 5).
  - f'c rises up to 30 sulfate wet–dry cycles, then falls (Li L. 2021, as cited in [[he2024-hdc-research-advances]], p. 11–12).
  - Sulfate attack on SHCC had not been studied experimentally as of 2010 ([[vanzijl2010-shcc-durability]], p. 266).
- **Acid:**
  - acid mine drainage: first-crack strength −23.7%, σ_tu −17.8%, ε −36.5% (Wu 2020, as cited in [[ma2021-ecc-durability-review]], p. 7);
  - 3% H₂SO₄ for 6 weeks: mass loss > 8% (Turk 2017, as cited);
  - 5% H₂SO₄, 1 month: slight weight *gain* in CR-ECC; largest loss at 2.5% CR + 1% PVA
    ([[mohammed2020-cr-ecc-elevated-temperature]], Sections 3.4, Fig. 9) — primary, compression-type specimens only.
- **Abrasion (as cited, p. 7–8):** metakaolin is the best binder substitute; fiber ranking steel > PVA 8 mm >
  PVA 12 mm; PE does not help.
- **Leaching** (NH₄NO₃ 3–6 mol/L, 70 d): matrix toughness and MOR down almost 50% (as cited in
  [[vanzijl2010-shcc-durability]], p. 265–266).
- **ASR**: ASTM C1260, no expansion of an M45-type SHCC after 30 d; high FA makes ASR unlikely (as cited,
  p. 266). PVA keeps nearly full strength after 14 d in 80 °C alkaline water and loses ≤ 5% after > 1 yr in
  dilute acids (p. 266). → [[pva-fiber]]
- **Field (as cited in [[kunieda2006-hpfrcc-japan-applications]], p. 29)**: sprayed HPFRCC on an ASR-damaged
  retaining wall stayed uncracked to 7 months, cracks ≤ 0.05 mm at 10 months and ≤ 0.12 mm at 24 months vs
  repair mortar 0.2 / 0.3 mm. → [[repair-and-field-applications]]

## Combined mechanical + environmental loading
- Sustained flexural load (60% of ultimate, 90 d) leaves *uncracked* ECC flexural properties unchanged
  ([[ozbay2013-ecc-self-healing-sustained-load]], Table 4, p. 178), but on pre-cracked ECC it doubles crack
  width and cuts healing → [[self-healing]].
- Sustained stress accelerates carbonation even below first cracking ([[zhang2022-ecc-carbonation-sustained-load]]) → [[carbonation]].
- Combined loads (frost + chloride, mechanical + chemical) accelerate deterioration and were not studied for
  SHCC as of 2010; only a fraction of ε_tu should be used in service-life design in aggressive environments
  ([[vanzijl2010-shcc-durability]], p. 268–269, Table 2).

## Long-term ageing
- Ductility and self-healing decline with age because of the continuing pozzolanic reaction
  ([[ma2021-ecc-durability-review]], p. 9).
- PVA-ECC ε peaks early, then falls to about 3% at 180 d. PE-ECC shows no ε loss from 28 d to 1 yr
  ([[yu2018-ecc-direct-tensile-review]], p. 352).
- Hot-water ageing 26 wk: ε_tu about 4.5 → 2.75%, σ_tu up, chemical bond about +50%; claimed equivalent to
  > 70 yr service (as cited in [[vanzijl2010-shcc-durability]], p. 268). → [[fiber-matrix-interface]]
- PVA-ECC strain at 28 d is 43–54% of the 7-d value; a peak "at about 10 d" is claimed without citation
  ([[sun2019-modified-pva-fiber-ecc]], §3.2).
- Refinement: in 12 months outdoors, healing recovery *increased* for cracks made at 7 d
  ([[herbert2013-ecc-self-healing-natural-environment]]); ECC M45 cracked at ≈ 6 months still recovered 87–100%
  resonant frequency under wet–dry cycles ([[yang2009-ecc-self-healing-wet-dry]], Fig. 7).

## Other durability notes
- Wide, widely spaced cracks in RC promote macro-cell corrosion (Raupach 2001, as cited in
  [[lepech2009-ecc-water-permeability]], p. 749). → [[chloride-and-corrosion]]
- Tight cracks may delay corrosion, but "further research is needed to directly confirm" it ([[li2003-ecc-review]], p. 225).
  Primary tests now exist → [[chloride-and-corrosion]].
- Chinese PVA-HDC pore structure refines after 8 h at 60 °C: critical pore 62.4 → 50.3 nm ([[chai2023-hdc-ambient-temperature]], Fig. 18).

> Synthesis: primary studies confirm the reviews' headline (PVA-ECC/HDC far outlasts plain concrete under
> freeze–thaw and sulfate) but add three cautions: (1) carbonation of high-FA ECC is faster than the
> reviews suggested; (2) under wet–dry chloride, fine cracks do not stop chloride reaching steel — the
> benefit is in corrosion *cracking* and spalling, not initiation; (3) few studies measure uniaxial
> tension after exposure, so retention of strain hardening is rarely shown (exceptions: healed ECC reloaded
> in tension, [[yang2009-ecc-self-healing-wet-dry]]; hybrid SHCC after F-T, [[yun2013-shcc-freeze-thaw]]). Many "ECC" in durability papers
> do not demonstrate strain hardening at all (Zhong 2019, Zhang 2022, Bu 2022, Zhou 2023, Mohammed 2020).

## Gaps
Stated in [[ma2021-ecc-durability-review]], p. 9–10:
- Almost all data are at 28 d; long-age data are missing.
- Very little durability data exist for **high-strength / high-ductility ECC**, i.e. HSHDC and UHDC. Still
  true: all new primary studies concern PVA-ECC/HDC with f'c ≤ about 90 MPa.
- Coupled exposures, fiber durability, field validation and the ECC–substrate interface need study.
Stated in [[vanzijl2010-shcc-durability]], p. 263–269: tolerable crack-width distribution per environment;
time-dependent crack width under sustained load; limit strains for service-life design; early-age cracking
of large elements. → [[gaps]]

## Related
- [[freeze-thaw]] · [[carbonation]] · [[chloride-and-corrosion]] · [[crack-width]] · [[permeability]] · [[self-healing]] · [[shrinkage]] · [[fatigue]] · [[high-temperature-behaviour]] · [[repair-and-field-applications]]
