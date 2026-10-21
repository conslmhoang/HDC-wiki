---
type: log
---

# Log

Append-only. Format: `## YYYY-MM-DD — <operation> — <subject>`, followed by bullet points.

## 2026-10-06 — setup — wiki skeleton
- Created the schema (`CLAUDE.md`), templates, hub pages, and empty dataset tables.
- No sources ingested yet.

## 2026-10-06 — ingest — Ranade et al. 2013a, Micromechanics of HSHDC
- Raw file: `raw/papers/Ravi2013_Micromechanics of High Strength, HDC.pdf` (14 pp. incl. appendix)
- Created (15 pages):
  - source: ranade2013-hshdc-micromechanics
  - concepts: hshdc, strain-hardening, multiple-cracking, fiber-bridging, fiber-matrix-interface,
    fiber-dispersion, heat-curing
  - materials: pe-fiber, pva-fiber (stub), silica-fume
  - properties: matrix-fracture-toughness
  - test methods: single-fiber-pullout-test, single-crack-test
  - dataset: micromechanical-parameters
- Updated: terminology-hdc-ecc-shcc (two meanings of HDC), mix-designs (+1 row), gaps, index
- Conflicts: HDC terminology ambiguity; microspalling vs clamping (matrix-dependent)
- µm/mm extraction errors resolved (page image confirms "600 µm"; µ glyph was lost in text extraction)
- Still to verify: τ0 1.52 vs 1.53 MPa; DOI missing

## 2026-10-06 — schema — added "ingest new" command (CLAUDE.md §5.1b)
- Requested by the human: batch-ingest all unprocessed raw files with one message.

## 2026-10-06 — ingest — Ranade et al. 2013b, Composite Properties of HSHDC
- Raw file: `raw/papers/Ravi2013_Composite Properties of Hight-Strength, HDC.pdf` (10 pp.)
- Created (10 pages):
  - source: ranade2013-hshdc-composite-properties
  - properties: tensile-strain-capacity, compressive-strength, crack-width, flexural-strength,
    fresh-properties
  - concepts: uhpc-vhsc
  - test methods: dogbone-uniaxial-tension, split-tension-test, third-point-flexure-test
- Updated: hshdc, fiber-dispersion, multiple-cracking, strain-hardening, heat-curing,
  matrix-fracture-toughness, mix-designs (+6 rows), mechanical-results (+6), gaps
- Conflicts: σ_fc 8.3 (primary) vs 8.4 MPa (quoted in the companion paper)
- To verify: HRWRA basis (1.8% of cement vs 1.26% of cementitious); DOI missing

## 2026-10-06 — ingest — Ranade, Li & Heard 2015, Tensile Rate Effects in HSHDC
- Raw file: `raw/papers/Ravi2014_Tensile Rate Effects in High Strength-HDC.pdf` (11 pp.)
- Slug uses the publication year 2015 (CCR 68). Replaced the placeholder link
  `ranade2014-...` in ranade2013-hshdc-micromechanics.
- Created (3 pages):
  - source: ranade2015-hshdc-tensile-rate-effects
  - concept: strain-rate-effects
  - application: extreme-loading-applications
- Updated: hshdc, pe-fiber, fiber-matrix-interface, matrix-fracture-toughness, strain-hardening,
  tensile-strain-capacity, crack-width, fiber-dispersion, dogbone-uniaxial-tension,
  single-fiber-pullout-test, mix-designs (+1), mechanical-results (+6),
  micromechanical-parameters (+2), gaps, index
- Conflicts:
  - quasi-static ε_tu 4.2% vs 3.4% (2013)
  - J′b 969 vs 682 J/m²
  - min Vf 1.6% vs 1.7%
- To verify: test age not stated; absolute τ0 and fiber properties only in figures

## 2026-10-06 — maintenance — raw folder changed by the human
- Renamed raw file: `Ravi2014_...` → `Ranade2014_...` (text identical); raw_file path updated.
- **Removed at the human's request:** Ranade et al. 2013 (Micromechanics; Composite Properties).
  - Deleted both source pages and all dataset rows (14).
  - Rewrote every topic page from the remaining sources.
  - Deleted the pages split-tension-test and third-point-flexure-test (no remaining source).
  - Links to them inside other source pages were converted to plain "as cited" text.

## 2026-10-06 — ingest new — 5 sources (parallel drafting of source pages, sequential integration)
- New sources:
  - he2024-hdc-research-advances
  - ranade2017-hshdc-impact-resistance
  - su2023-rubber-modified-hshdc
  - yang2024-hshdc-uniaxial-tension
  - ye2021-uhdc-flexural-size-effect (raw file "Ye2020"; slug uses volume year 2021)
- New pages:
  - concepts: uhdc, fiber-geometry, water-binder-ratio, size-effect, fracture-process-zone,
    tensile-constitutive-model
  - materials: fly-ash, crumb-rubber, ggbfs
  - properties: impact-resistance, tensile-toughness, durability, high-temperature-behaviour
  - test methods: impact-test, notched-beam-three-point-bending, digital-image-correlation
  - applications: masonry-wall-retrofit, rc-member-strengthening, unreinforced-hdc-structures,
    3d-printed-hdc
- Rewritten: all remaining concept, material, property, test-method and application pages;
  the datasets; gaps; review-outline; index.
- Key findings:
  - "HSHDC" has 3 lineages (Michigan, GDUT, Xi'an).
  - HDC ≈ ECC/SHCC in the Chinese usage; fiber type does not define it.
  - Heat curing is not required.
  - There is a strength–ductility trade-off across lineages.

## 2026-10-16 — ingest new — 5 sources (parallel source drafting, sequential integration)
- New sources: li1992-steady-state-multiple-cracking, li2002-pva-ecc-interface-tailoring,
  yu2018-ecc-direct-tensile-review (raw "Yu2017"), ma2021-ecc-durability-review (raw "Ma2020"),
  zhang2022-hshdcc-review. Slug years use the journal volume year.
- New pages:
  - concepts: steady-state-cracking, fiber-surface-treatment
  - properties: self-healing, permeability, shrinkage, fatigue
- Rewritten: pva-fiber, durability, high-temperature-behaviour, crack-width, gaps, review-outline.
- Updated about 20 topic pages; datasets +20 rows.
- Key changes:
  - The PVA gap is filled (Li 2002).
  - The strength–ductility trade-off is revised: it is not fundamental (Zhang 2022).
  - The two PSH indices fail in opposite cases (Li 2002 vs Su 2023).
  - There are two crack-width families: PVA about 40–90 µm, PE about 80–200 µm.
- The human decided the corpus (11 papers) is sufficient.

## 2026-10-20 — ingest — 5 sources (downloaded by the LLM; 13 more still to obtain)
- Downloaded: Kanda 2006, Yang 2008, Li 2003 (J-STAGE PDFs); Chai 2023 and Li 2021 sulfate (Europe PMC
  full-text XML, CC BY, because MDPI/NCBI block scripted PDF download). Hindawi, ScienceDirect and ACI
  blocked automated download; the 13 remaining papers need the human's browser or library access.
- New sources: kanda2006-psh-design-criteria, yang2008-ecc-fiber-bridging-law, li2003-ecc-review,
  chai2023-hdc-ambient-temperature, li2021-hdc-sulfate-dry-wet.
- New page: repair-and-field-applications.
- Corrected: PSH thresholds (1.2 / 3 = pull-out type, Kanda & Li 1998b; 1.3 / 2.7 = rupture type, 2006)
  on strain-hardening and steady-state-cracking; "no standard" → JC/T 2461-2018 (≥ 0.5%, ≤ 200 µm);
  "no primary durability study" and "no Chinese PVA-HDC primary data" statements.
- Updated about 20 topic pages and 3 datasets (+18 rows); gaps: 3 conflicts resolved or refined, 4 new.


## 2026-10-21 — ingest new — 34 sources (round 4, toward the 50-paper target)
- **How sources were obtained:**
  - Wiley/Hindawi PDFs (incl. the 3 Deng/XAUAT papers) downloaded through the human's Chrome with university access.
  - 13 JACT PDFs from J-STAGE.
  - 18 MDPI papers as full-text XML from Europe PMC (CC BY).
  - ScienceDirect was blocked by a CAPTCHA loop (not bypassed), so the 10 ScienceDirect/ACI papers on the reading
    list are still missing.
- **New sources (34):**
  - Chinese HDC/HDCC and XAUAT: deng2015-hdc-compressive-toughness, deng2018-hdc-compressive-constitutive,
    deng2018-hdc-short-columns, chai2019-hdcc-freeze-thaw-carbonation-flexure, gao2020-hdcc-recycled-fine-aggregate.
  - Korea Univ. HSDC/NSHSDC: yuan2020-nshsdc-beam-strengthening, lee2021-hsdc-wall-emi-impact.
  - JACT: kanda2003-sprayed-ecc, kanakubo2006-dfrcc-tensile-test-method, kunieda2006-hpfrcc-japan-applications,
    qian2007-shcc-inverse-tensile-strain, homma2009-frcc-self-healing, kunieda2010-uhp-shcc-steel-reinforcement,
    vanzijl2010-shcc-durability, mechtcherine2011-shcc-high-strain-rate, ozbay2013-ecc-self-healing-sustained-load,
    paul2014-r-shcc-chloride-corrosion, wang2023-ecc-frost-damage, zhou2023-hsecc-elevated-temperature.
  - MDPI and others: herbert2013-ecc-self-healing-natural-environment, sui2018-uhp-ecc-flexural-fatigue,
    jin2019-hvfa-shcc-structural, sun2019-modified-pva-fiber-ecc, wang2019-rc-beam-ecc-shear-strengthening,
    zhong2019-ecc-freeze-thaw, chavesfigueiredo2020-printed-shcc, mohammed2020-cr-ecc-elevated-temperature,
    bu2022-ecc-chloride-crack-width, ivaniuk2022-printable-shcc-design, shumuye2022-slag-fa-pe-ecc,
    tabrizikahou2022-masonry-ecc-sma-retrofit, zhang2022-ecc-carbonation-sustained-load,
    zhao2022-ecc-tension-damage-model, xue2023-shcc-structural-review.
- **New pages (10):**
  - properties: freeze-thaw, carbonation, chloride-and-corrosion, compressive-constitutive-model, shear-behaviour
  - materials: recycled-fine-aggregate, hybrid-fiber, viscosity-modifying-admixtures
  - test methods: four-point-bending-inverse-analysis
  - concepts: interface-bond
- **Restructured/rewritten:** durability (now a hub), crack-width; about 40 other topic pages updated by the
  theory, materials, mechanical, durability and tests-apps integration groups.
- **Key corrections:**
  - Chloride crack-width threshold is **exposure-dependent**: 100 µm ≈ uncracked under immersion (Bu 2022), but
    50–100 µm (and < 50 µm) cracks carry chloride to rebar within hours under wet–dry cycles (Paul 2014); the
    55–80 µm value is second-hand.
  - Repair page: field crack-width data now exist, but only second-hand (Kunieda & Rokugo 2006: ≤ 50 µm at
    10 months, ≤ 120 µm at 24 months on an ASR wall).
  - PVA melting: onset 230 °C by primary TG (Zhou 2023); "273 °C" has no support.
  - Fourth HSHDC-type lineage: Korea Univ. steel + PE hybrid (HSDC/NSHSDC, ≈ 122–123 MPa); its tensile ductility
    is not shown in the ingested papers.
  - Kanakubo 2006 JCI round robin: the same PVA-DFRCC gives 2.70% strain at peak (thin plate) down to 0.07%
    (Ø70 dogbone); thickness effects conflict with Rokugo 2007 (as cited). Bending inverse methods depend on the
    chosen tension reference.
  - "ε_tu" naming: some papers report post-peak strain; the wiki compares strain at peak only.
  - Several "ECC/HDC" papers report no tension test (labelled on their source pages, not relabelled).
- **Datasets:** +202 rows: mix-designs 22 → 91 (+69), mechanical-results 54 → 180 (+126),
  micromechanical-parameters 17 → 24 (+7). Fatigue S–N, field crack widths and member results stay on source pages.
- **gaps:** 51 conflict rows (was 19): 32 new after merging duplicates across groups (e.g. chloride threshold,
  Kanakubo vs Rokugo thickness effect, JSCE 2008 vs JC/T 2461, delamination, printed SHCC interlayer and fiber
  orientation); 3 rows refined (strain-rate ε and failure mode by mechtcherine2011; F-T citation note); PVA
  melting partly resolved. Under-studied areas rewritten for the 50-source corpus.
- Updated index (34 sources + 10 pages, grouped by lineage) and review-outline (scope 50 papers).

## 2026-10-21 — ingest new — 10 sources (round 5, reaching 60)
- **How sources were obtained:** the human downloaded 9 ScienceDirect PDFs by hand (a CAPTCHA blocked automated
  download and was not bypassed). Choi 2016 was added as a replacement for Wang 2007 (ACI), which is paywalled.
- **New sources (10):**
  - XAUAT structures and TR-HDC: deng2017-rc-column-hdc-jacket, deng2019-urm-shaking-table-hdc,
    deng2020-aac-wall-hdc-retrofit, li2021-hdc-beam-shear, zhang2022-hdc-basalt-textile-tension.
  - Durability and temperature: yang2009-ecc-self-healing-wet-dry, lepech2009-ecc-water-permeability,
    yun2013-shcc-freeze-thaw, pourfalah2018-ecc-high-temperature.
  - Cementless composite: choi2016-pe-alkali-activated-slag-composite.
- **New pages (2):** materials/textile-reinforced-hdc, materials/alkali-activated-binder.
- **Updated:** about 40 topic pages by the structures and durability-materials integration groups (applications,
  shear, tension, crack width, self-healing, permeability, freeze–thaw, high temperature, fibres, binders, W/B).
- **Key corrections:**
  - Permeability: reinforced mortar at ≈ 500 µm is **4.46 × 10⁻⁴ m/s** (Lepech & Li 2009, Table 5), not 10⁻⁵ m/s as
    quoted via ma2021; 10⁻⁵ (2.58 × 10⁻⁵) is the 300 µm value. The "0.10–0.15 mm" threshold attributed to Lepech & Li
    2009 is a mis-citation; their 100 µm is a design target from concrete (Wang 1997), not measured on ECC.
  - Healing thresholds: Yang 2009's < 50 / 50–150 / > 150 µm limits were measured on a 0.5% PVA tension-softening
    mortar, not ECC; the "< 60 µm" value is Reinhardt & Jooss (via ma2021), not Yang 2009.
  - Yun citation resolved: Yun 2013 (Compos. B 52) and Yun 2011 (Cold Reg. Sci. Technol. 67) are two different papers.
  - "Deng & Zhang 2018" row: he2024 most likely refers to Deng, Zhang & Li 2018 (Eng. Struct. 160, ECC-jacketed short
    columns, not ingested), not to deng2018-hdc-short-columns; probably resolved.
  - XAUAT PVA-HDC strain spread: ≈ 3.0% (Japanese PVA, Deng 2017) vs ≈ 1.0% (Deng 2018, 2019; Li 2021) vs
    0.34–0.45% (plain HDC in Zhang 2022, below the 0.5% bar), same nominal fibre; raised by both groups, merged into
    one conflict row.
  - Deng 2019 shake-table test is now primary; masonry retrofit and RC column jacketing now have primary data.
- **Datasets:** +60 rows: mix-designs 91 → 113 (+22), mechanical-results 180 → 216 (+36),
  micromechanical-parameters 24 → 26 (+2). Dataset conflicts: M45 HRWR 7.51 (lepech2009) vs 17 kg/m³ (yang2009);
  li2021 σ_tu 5.83 vs 5.68 MPa (internal).
- **gaps:** 64 conflict rows (was 51): 13 new after merging duplicates (XAUAT strain spread, permeability at 500 µm,
  0.10–0.15 mm mis-citation, origin of 100 µm, static vs flowing water, ε_tu and stiffness after F-T, code
  conservatism, shear design philosophy, PVA modulus, PVA at 200 °C, M45 HRWR, li2021 σ_tu); 12 rows updated, incl.
  Yun 2011/2013 resolved and Deng & Zhang 2018 probably resolved. Under-studied areas updated for the 60-source corpus.
- Updated index (10 sources + 2 pages; new groups for XAUAT structures and cementless composites) and review-outline
  (scope 60 papers; applications chapter now ✅).

## 2026-10-21 — re-ingest — 20 sources from PDF (XML replaced)
- **Why:** the human asked for the publisher PDFs. The 20 sources had been ingested from Europe PMC XML, which has no
  page numbers and no figure data (values printed only in figures, bar labels and legends were missing).
- **How:** PDFs fetched with Europe PMC's getPdf service; each title checked against its source page; the old XML files
  moved to `raw/xml-archive/` (superseded copies, not used as sources); `raw_file:` now points to the PDF. Each source page
  was re-checked line by line against its PDF.
- **Sources (20):** chai2023-hdc-ambient-temperature, li2021-hdc-sulfate-dry-wet, gao2020-hdcc-recycled-fine-aggregate,
  lee2021-hsdc-wall-emi-impact, bu2022-ecc-chloride-crack-width, zhang2022-ecc-carbonation-sustained-load,
  zhong2019-ecc-freeze-thaw, herbert2013-ecc-self-healing-natural-environment, chavesfigueiredo2020-printed-shcc,
  ivaniuk2022-printable-shcc-design, xue2023-shcc-structural-review, tabrizikahou2022-masonry-ecc-sma-retrofit,
  jin2019-hvfa-shcc-structural, sun2019-modified-pva-fiber-ecc, zhao2022-ecc-tension-damage-model,
  shumuye2022-slag-fa-pe-ecc, yuan2020-nshsdc-beam-strengthening, wang2019-rc-beam-ecc-shear-strengthening,
  sui2018-uhp-ecc-flexural-fatigue, mohammed2020-cr-ecc-elevated-temperature.
- **Results:** no tabulated value on any of the 20 pages was wrong. Page numbers were added throughout, and about 300
  values were added from figures (marked ≈ / read), e.g. Jin 2019 f'c, E and flexural data (Figs. 8, 14), Mohammed 2020
  residual f'c 24–1000 °C (Fig. 3), Sui 2018 tension curves (Fig. 4), Lee 2021 EMI SE and impact data (Figs. 5–12),
  Gao 2020 f_c and 3-pt flexural strength (Fig. 9), Tabrizikahou 2022 peak forces (Fig. 25).
- **Corrections:**
  - Lee 2021: post-impact SE loss 7.1% / 24.7% are H20S / H20D (both 20 mm skins); thinner skins lost more
    (H5S ≈ 44%), not less; "3.5%" is 32.5%; crack widths in mm.
  - Mohammed 2020: at 1000 °C the 0% CR mix keeps ≈ 16 MPa (only CR mixes ≈ 11–13 MPa); the claimed acid weight gain
    is contradicted by Fig. 8 (losses 0.2–7.3% in 12 of 13 mixes).
  - Sui 2018: the tension data are at 90 d (ε ≈ 6.9–8.8%, σ_tu ≈ 11.1–12.4 MPa, read from Fig. 4).
  - Yuan 2020: Table 7 failure modes are primary / secondary, the same for LS and HS at each angle (not LS / HS).
  - Chai 2023: "ultimate tensile strain" is strain at peak stress (Fig. 1).
  - Sun 2019: "ultimate tensile strain" is strain at the end of the curve incl. softening; the VAE and W/B effects lie
    within the Fig. 6 scatter.
  - Jin 2019: bending tests at 7 and 90 d only (not 7 / 28 / 90 d).
  - Zhong 2019: surface scaling at IF is Fig. 15 (not Fig. 12); the "rise at FA 0.525" claim is not borne out by Fig. 16.
  - Herbert 2013: the 24 / 30 µm crack widths carry ref. [29] (Sahmaran & Li 2009) and may not be measured on these
    specimens; fibre manufacturer not named.
  - Also: Li 2021 saturated sulfate HDC falls after 30 cycles (not 60); Shumuye 2022 strain at peak (28 d), flexural
    "kN" almost certainly N; Wang 2019 ε ≈ 0.9–1.9% at peak and truss model uses σ_t 4.0 MPa; Zhao 2022 damage-model
    units confirmed (MPa, %).
- **Propagated pages** (topic and dataset updates by the parallel integration groups, per the per-source reports):
  extreme-loading-applications, impact-resistance, impact-test, crack-width, high-temperature-behaviour, durability,
  crumb-rubber, compressive-strength, flexural-strength, tensile-strain-capacity, tensile-constitutive-model,
  shear-behaviour, interface-bond, rc-member-strengthening, masonry-wall-retrofit, 3d-printed-hdc, fiber-dispersion,
  self-healing, freeze-thaw, carbonation, permeability, chloride-and-corrosion, fly-ash, pva-fiber, water-binder-ratio,
  fiber-geometry, fiber-surface-treatment, dogbone-uniaxial-tension, four-point-bending-inverse-analysis,
  mechanical-results, mix-designs.
- **gaps:** 73 conflict rows (was 64): 9 new — 8 internal inconsistencies of single sources (Mohammed acid weight,
  Zhang ">2-fold" pore reduction ≈ 1.4× and sustained-load values, Zhong FA 0.525, Shumuye kN vs N, Zhao V3R2
  constants, Xue Fig. 1 vs text, Tabrizikahou energy ≈ 500× too large, Bu D decline 5% vs ≈ 20–25%) and 1 resolved
  wiki misreading (Lee SE loss vs skin thickness); 13 rows updated (ε naming, FE "ECC", PSH 1.45, Shumuye slag now a
  confirmed text–data conflict, W/B–ductility weakened, ductility vs age, printed fibre orientation and interlayer,
  carbonation, healing vs age, sulfate trend, Chai and Mohammed temperature rows).
- **index:** gaps count; one-liners of sun2019 and shumuye2022 (strain basis). review-outline unchanged (no chapter's
  evidence status changed). `raw/README.md`: one line on `raw/xml-archive/`.
