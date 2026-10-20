---
type: hub
updated: 2026-10-21
---

# Research Gaps, Conflicts & Open Questions

This page feeds the "Research gaps and future directions" chapter of [[review-outline]].
Corpus: 50 source pages (round 4, 2026-10-21). 51 conflict rows below, grouped by theme.

## ⚔️ Conflicts between sources
| Topic | Source A says | Source B says | Possible reason | Status |
|---|---|---|---|---|
| **Terminology & classification** | | | | |
| Meaning of "HDC" / "HSHDC" | HSHDC = Michigan PE + VHSC matrix, 166 MPa, heat-cured ([[ranade2017-hshdc-impact-resistance]]) | HSHDC = Xi'an ambient-cured, about 100 MPa ([[yang2024-hshdc-uniaxial-tension]]); GDUT ([[su2023-rubber-modified-hshdc]]); umbrella HSHDCC > 100 MPa and > 3% ([[zhang2022-hshdcc-review]]); Korea Univ. HSDC/NSHSDC = 1.0% steel + 0.5% PE hybrid, ≈ 122–123 MPa ([[yuan2020-nshsdc-beam-strengthening]]; [[lee2021-hsdc-wall-emi-impact]]) | Same name used by different groups (now 4 lineages) | open: always state the lineage, see [[terminology-hdc-ecc-shcc]], [[hshdc]] |
| Class thresholds | HSHDCC: > 100 MPa, > 3% ([[zhang2022-hshdcc-review]]) | > 55 MPa and > 4%, or > 80 MPa and > 2% (other reviews, as cited there); normal HDC 30–80 MPa ([[su2023-rubber-modified-hshdc]]) vs normal ECC 40–70 MPa ([[zhang2022-hshdcc-review]]) | Chinese standard JC/T 2461-2018 sets only ≥ 0.5% and ≤ 200 µm (as cited in [[chai2023-hdc-ambient-temperature]]) | open: two bars, ECC convention vs HDC standard |
| Origin of the 0.5% / 200 µm HDC(C) definition | JSCE 2008 ([[chai2019-hdcc-freeze-thaw-carbonation-flexure]], p. 126) | JC/T 2461-2018 ([[chai2023-hdc-ambient-temperature]], §1); same group, same numbers | Chinese standard may have adopted the JSCE values; neither document ingested | verify |
| HDC vs ECC | "HDC stands for ECC" (p. 2) | "HDC developed on the basis of ECC" (p. 10), both in [[he2024-hdc-research-advances]] | Internal inconsistency | treat HDC ≈ ECC/SHCC |
| Definition of "ε_tu" | strain at peak stress (wiki convention, [[tensile-strain-capacity]]) | Gao 2020 "ε_tu" = post-peak maximum strain, up to 11.73% (ε_tp at peak 1.68–4.76%) ([[gao2020-hdcc-recycled-fine-aggregate]]); Zhao 2022 ε_u post-peak 1.9–4.1% vs ε_p 0.5–2.0% ([[zhao2022-ecc-tension-damage-model]], Table 3) | Inconsistent naming | resolved: compare strain at peak only |
| "ECC" in FE models | ECC = strain hardening, σ_tu ≈ 3–5 MPa (e.g. 4.84 MPa, [[wang2019-rc-beam-ecc-shear-strengthening]]) | Abaqus CDP input softening from σ_t 1.45 MPa ([[tabrizikahou2022-masonry-ecc-sma-retrofit]], Table 5) | Borrowed non-hardening input | open: flag FE studies whose "ECC" is not strain-hardening → [[tensile-constitutive-model]] |
| **Design theory & micromechanics** | | | | |
| Quasi-static ε_tu of Michigan HSHDC | 3.4% (as quoted in [[ranade2017-hshdc-impact-resistance]]) | 4.2% ([[ranade2015-hshdc-tensile-rate-effects]]); 3.5% for the 2011 version ([[zhang2022-hshdcc-review]]) | Batch and fiber version (38 vs 28 µm) | open: report 3.4–4.2% |
| Strength–ductility trade-off | ε_tu falls as f'c rises across the primary sources (UHDC 9.45% → Michigan 3.4–4.2%) | f'c > 210 MPa with ε > 5%, and 122 MPa with 8.5% (as cited in [[zhang2022-hshdcc-review]]) | Interface and fiber design, not f'c alone | resolved: the trade-off is **not fundamental** |
| PSH thresholds | "> 1.2 and > 3" quoted for all fibers (Su 2023, Ranade 2015, Zhang 2022) | 1.2 / 3 apply to pull-out type; fiber-rupture type needs > 1.3 and > 2.7 ([[kanda2006-psh-design-criteria]], p. 69–70); a third value σ0/σ_fc > 1.45 for PVA-SHCC, attributed to Kanda & Li 1998 ([[jin2019-hvfa-shcc-structural]], §2.2) | Papers quote the 1998 set; 1.45 may be a mis-quote or a different index (Kanda & Li 1998 not ingested) | partly resolved: check which set applies; verify 1.45 |
| PSH criteria vs behaviour | 6 mm PE mixes meet the 1998 thresholds but fail brittle ([[su2023-rubber-modified-hshdc]]) | In PVA-ECC the energy index (> 3) predicts saturation well ([[li2002-pva-ecc-interface-tailoring]]) | PE6 fails the 2006 strength threshold (1.2 < 1.3); flaw-size and embedment terms missing ([[li1992-steady-state-multiple-cracking]]) | partly resolved |
| Does the stress index separate ductile from brittle PVA mixes? | no: 1.5–1.8 for all ([[li2002-pva-ecc-interface-tailoring]]) | yes: 1.14–1.16 → 0.3–0.6%, 1.31–1.32 → 1.0–1.5% ([[kanda2006-psh-design-criteria]]) | Different matrices (mortar vs paste) | open |
| β of oiled PVA | 0.58–0.63 in the M45 fly-ash matrix ([[yang2008-ecc-fiber-bridging-law]]) | 1.15 in a w/c 0.45 matrix without fly ash ([[li2002-pva-ecc-interface-tailoring]]) | Matrix and fly ash | resolved: matrix-dependent |
| Bond vs ductility (recycled fine aggregate) | Lower PVA bond (oiling) → ε 0.99 → 4.88% ([[li2002-pva-ecc-interface-tailoring]]; Li & Leung argument in [[chai2019-hdcc-freeze-thaw-carbonation-flexure]]) | RFA raises bond (inferred from SEM) and ε_tp 1.68 → 4.76% at 2% PVA ([[gao2020-hdcc-recycled-fine-aggregate]], Table 6, Fig. 16) | N-HDCC bond (unoiled domestic PVA, W/B 0.45) may be below the optimum; RFA may act via flaws ("crack trapping"); no pull-out data | open → [[recycled-fine-aggregate]], [[interface-bond]] |
| Vf vs tensile peak stress | σ0 ∝ Vf in bridging models ([[yang2008-ecc-fiber-bridging-law]]; [[jin2019-hvfa-shcc-structural]], Fig. 1a) | σ_p flat (3.10 / 2.96 / 3.23 MPa) for 1 / 1.5 / 2% PVA ([[zhao2022-ecc-tension-damage-model]], Table 3) | Matrix; flaw- or rupture-controlled peak | open → [[fiber-geometry]] |
| PVA-ECC σ_tu "3–8 MPa" | attributed to Li 2003 in [[yu2018-ecc-direct-tensile-review]] | not in [[li2003-ecc-review]] (only ε ≈ 5%) | Probably another Li 2003 paper | verify |
| **Constituents & mix design** | | | | |
| Slag/FA effect on PE-ECC ductility | Text: all-FA mix SF-0-60 had the highest tensile capacity; slag reduces strain ([[shumuye2022-slag-fa-pe-ecc]], Sect. 3.2) | Same paper's data: ε ≈ 2.0% (SF-0-60) < 2.9% (SF-10-50) < 3.5% (SF-5-55) (Fig. 5) | Internal text vs data inconsistency; strain definition unclear | open: verify Fig. 5 → [[fly-ash]], [[ggbfs]] |
| W/B and PVA-ECC ductility | Lower W/B more ductile: 0.30 → 3.79% vs 0.35 → 3.21% at 7 d ([[sun2019-modified-pva-fiber-ecc]], Table 10) | Higher W/B more ductile: 0.24 → 0.28 gives ε_p ×4 ([[zhao2022-ecc-tension-damage-model]], Table 3); W/B 0.31 → 0.20 lowers ε_tu ([[chai2023-hdc-ambient-temperature]]) | Different ranges, ages (7 d vs ≥ 28 d), matrices | open → [[water-binder-ratio]] |
| Short (6 mm) PE fiber | 6 mm × 12 µm PE at 1.5% → strain softening, W/B 0.45 ([[homma2009-frcc-self-healing]], p. 224); 6 mm × 20 µm PE brittle ([[su2023-rubber-modified-hshdc]]) | Same 6 mm × 12 µm at 1.5% strain-hardens in W/B 0.20 UHP-SHCC ([[kunieda2010-uhp-shcc-steel-reinforcement]]) and in printed SHCC ([[ivaniuk2022-printable-shcc-design]]) | Aspect ratio and matrix strength, not length alone | open → [[fiber-geometry]], [[pe-fiber]] |
| PVA fiber length effect (as cited) | longer gives lower ductility (Feng 2022) | 18 mm better than 12 mm (Lee 2023), both in [[su2023-rubber-modified-hshdc]] | Matrix and test | open |
| PVA-ECC ductility vs age | REC-15 ECC 3.21% (7 d) → 1.39% (28 d) ([[sun2019-modified-pva-fiber-ecc]], Table 11) | Michigan PVA-ECC ≈ 4–5% at 28 d ([[li2002-pva-ecc-interface-tailoring]]); ≈ 3% at 180 d (Lepech & Li 2006, as cited in [[yu2018-ecc-direct-tensile-review]]) | Different matrix (FA content unknown), curing, coating | open → [[pva-fiber]], [[heat-curing]] |
| Fiber orientation in printed SHCC | Mainly diagonal to the print path, measured by µCT ([[chavesfigueiredo2020-printed-shcc]], Fig. 17) | Assumed aligned with the print direction (citing Li et al. 2020) ([[ivaniuk2022-printable-shcc-design]]) | Measured vs assumed; PVA vs PE; nozzles and mixes | open → [[fiber-dispersion]], [[3d-printed-hdc]] |
| **Tension, compression, flexure, fatigue** | | | | |
| Specimen thickness / geometry effect in direct tension | 13 / 30 / 50 mm thickness negligible for PVA-ECC (Rokugo 2007, as cited in [[yu2018-ecc-direct-tensile-review]], p. 348) | Same PVA-DFRCC: 2.70% thin plate (T1), 2.38 / 0.77% dogbone H/V, 0.07% Ø70 dogbone, 0.32% Ø100 cylinder, CV > 100% ([[kanakubo2006-dfrcc-tensile-test-method]], Tables 6–9); 50 × 200 mm unreinforced UHP-SHCC members 0.23% vs 1.5% in 13 mm dumbbells ([[kunieda2010-uhp-shcc-steel-reinforcement]], Table 3) | Shape, casting direction, end fixity, fiber type, 2-D vs 3-D orientation | open: always record geometry, casting direction and grips with ε_tu → [[tensile-strain-capacity]], [[size-effect]], [[dogbone-uniaxial-tension]] |
| Reference test for bending inverse methods | UM/JCI inverse ε 3.0 / 3.1% matches "UTT" 2.7% for JCI PVA ([[qian2007-shcc-inverse-tensile-strain]], Table 8) | That 2.7% is the thin-plate T1; the same-section T2 dogbone gave 2.38% (H) / 0.77% (V) ([[kanakubo2006-dfrcc-tensile-test-method]], Table 7) | Agreement depends on the chosen tension reference | open → [[four-point-bending-inverse-analysis]] |
| XAUAT HDC compressive peak strains | mixes 1–4: 0.22 / 0.74 / 0.67 / 0.80%, matrix 640.45 kN ([[deng2015-hdc-compressive-toughness]], Table 3) | same peak loads, 0.213 / 0.569 / 0.601 / 0.672%, matrix 630.55 kN ([[deng2018-hdc-compressive-constitutive]], Table 3) | Same tests reprocessed? Fig. 7a peak near 0.7% | verify → [[compressive-constitutive-model]] |
| ECC flexural S–N shape | Bilinear with inflection at S ≈ 0.9, N 10²–10⁴ (Matsumoto 2003 via [[kunieda2006-hpfrcc-japan-applications]]; Suthiwarapirak 2004, Liu 2017 via [[sui2018-uhp-ecc-flexural-fatigue]]) | Continuous, no inflection: S = 1 − 5.75×10⁻³(lg N)^2.43 for PE UHP-ECC ([[sui2018-uhp-ecc-flexural-fatigue]], Eq. 2) | PVA vs PE, matrix strength, small data set (3 beams/level) | open → [[fatigue]] |
| UHPC flexural size effect (as cited) | significant | reduced, both in [[ye2021-uhdc-flexural-size-effect]] | Size range and method | open |
| **Dynamic behaviour** | | | | |
| PVA-ECC ε vs strain rate | decreases (Yang & Li 2014; Mechtcherine, as cited in [[yu2018-ecc-direct-tensile-review]]); no significant change (Boshoff & van Zijl 2007, as cited there) | Primary: ε 1.49 → 0.82% up to 10⁻² s⁻¹, then 0.68 → 1.79% at 10–50 s⁻¹ ([[mechtcherine2011-shcc-high-strain-rate]], Table 2) | Rate range explains part of the disagreement | partly resolved: non-monotonic → [[strain-rate-effects]] |
| PVA failure mode at high rate | pull-out dominates in composite tests; rupture dominates in single-fiber tests ([[yu2018-ecc-direct-tensile-review]], p. 350) | In one composite: rupture ≤ 10⁻² s⁻¹, pull-out ≥ 10 s⁻¹ ([[mechtcherine2011-shcc-high-strain-rate]], Fig. 10) | Rate-dependent switch, plus scale effect | refined: mode switches with rate; cause still open |
| PVA-ECC DIF 6.7 attribution | Curosu 2016, about 150 s⁻¹ (as cited in [[yu2018-ecc-direct-tensile-review]]) | Millon et al. 2010, 140–180 s⁻¹ (as cited in [[mechtcherine2011-shcc-high-strain-rate]], p. 58) | Possible misattribution in the review | verify |
| **Cracking & durability** | | | | |
| Chloride crack-width threshold | 55–80 µm (Jang 2011) and ≥ 90 µm (Wu 2017), as cited in [[he2024-hdc-research-advances]], p. 10; ≈ 100 µm (Sahmaran 2007, as cited in [[vanzijl2010-shcc-durability]], p. 264; figure plots deformation) | Immersion, cast notches: 100 µm ≈ uncracked, significant ≥ 200 µm ([[bu2022-ecc-chloride-crack-width]]); wet–dry capillary: 50–100 µm (and < 50 µm) cracks carry Cl⁻ to rebar within hours, no correlation with width ([[paul2014-r-shcc-chloride-corrosion]], Table 5, Fig. 10) | Transport mode (diffusion vs capillary suction), notch vs real crack, matrix porosity (w/c 1.0 in Paul) | refined: threshold is **exposure-dependent**; treat 55–80 µm as second-hand → [[chloride-and-corrosion]], [[crack-width]] |
| Corrosion rate R/SHCC vs R/mortar | Similar, ≈ 0.003–0.02 mm/yr; localised pitting in R/SHCC ([[paul2014-r-shcc-chloride-corrosion]], Fig. 8, Table 4) | Slower in R/SHCC (Miyazato & Hiraishi 2005; Sahmaran 2008; Kobayashi 2010, as cited in [[vanzijl2010-shcc-durability]], p. 265) | Pre-crack deflection, measurement start time, porous w/c 1.0 matrix in Paul | open → [[chloride-and-corrosion]] |
| Crack width loaded vs residual | Under sustained flexural load ≈ 2× unloaded (60 → 115, 40 → 85 µm); healing reduced (stiffness 76 vs 87%, 83 vs 95%) ([[ozbay2013-ecc-self-healing-sustained-load]], Tables 3–4) | ≈ 15% larger under load (Yang 2009, as cited in [[herbert2013-ecc-self-healing-natural-environment]]) | Loading mode (flexural pre-deflection vs tension); all wiki thresholds use residual widths | open → [[crack-width]], [[self-healing]] |
| Carbonation depth, unloaded ECC, 28 d at ~20% CO₂ | 4.78 mm ([[zhang2022-ecc-carbonation-sustained-load]], Table 4) | ≈ 13 mm ([[wang2023-ecc-frost-damage]], Fig. 15a, read from figure); ≈ 0.8 mm (Zhang W. 2018, PP+PVA ECC, as cited in [[ma2021-ecc-durability-review]], p. 9) | Two primary mixes almost identical (PVA, FA/C 1.18–1.20, W/B 0.30–0.33, GB/T 50082) yet differ ≈ 2.7×; preconditioning, specimen size, figure reading; the 0.8 mm mix has PP fiber | open → [[carbonation]] |
| Freeze–thaw citation | Yun 2013, hybrid PVA+PE ([[he2024-hdc-research-advances]]) | Yun 2011, PVA loses more ε than PE ([[ma2021-ecc-durability-review]]) | Possibly two papers or a mis-citation; no primary study in the corpus measures tension after F-T, so it cannot be checked internally | verify |
| F-T durability factor of non-air-entrained concrete (as cited) | 20 (Li 2008, as cited in [[ma2021-ecc-durability-review]], p. 4) | 10 (Li et al. 2003, as cited in [[vanzijl2010-shcc-durability]], p. 267) | ECC/SHCC = 100 and concrete removed at 110 cycles in both; probably the same test reported differently | verify → [[freeze-thaw]] |
| Self-healing under freeze–thaw | ≈ 100% recovery at 0.5–1% pre-strain (Zhu 2012, as cited in [[ma2021-ecc-durability-review]], p. 5) | 20–30 µm cracks widened under coupled F-T + carbonation + 60 °C drying ([[chai2019-hdcc-freeze-thaw-carbonation-flexure]], §3.1) | Exposure type (drying, CO₂) | refinement → [[self-healing]] |
| Healing crack-width threshold | < 60 µm for fast permeability recovery (Reinhardt & Jooss, as cited in [[ma2021-ecc-durability-review]], p. 3) | < 100 µm sealed by CaCO₃ in 28 d water, FRCC ([[homma2009-frcc-self-healing]], Fig. 6); 10–40 µm full, > 60 µm partial ([[ozbay2013-ecc-self-healing-sustained-load]], Fig. 7) | Different measures (permeability time vs crystal thickness vs stiffness) | refinement → [[self-healing]] |
| "PE heals poorly" (earlier wiki synthesis) | PE-HSHDC 80–200 µm cracks lie above the healing range (earlier wiki synthesis) | Fine PE fibers promote CaCO₃ deposition at equal width; partial healing above 100 µm ([[homma2009-frcc-self-healing]], FRCC, not SH) | The limitation is crack width, not PE | resolved: a crack-width issue → [[self-healing]] |
| Self-healing vs age | Declines with age (pozzolanic reaction) ([[ma2021-ecc-durability-review]], p. 9) | Recovery rose over 12 months outdoors ([[herbert2013-ecc-self-healing-natural-environment]], Fig. 6) | Herbert cracked at 7 d; late-age cracking untested | refinement |
| Sulfate + dry–wet trend of HDC | "rises to 30 cycles, falls after 105" ([[he2024-hdc-research-advances]]) | holds for 5% Na₂SO₄ only; 10% peaks at 105, saturated falls from 60 ([[li2021-hdc-sulfate-dry-wet]], Table 4) | Review simplified the primary data | refinement |
| Shrinkage vs W/B (as cited) | rises with W/B (Gao 2018) | falls with W/B (Ye 2019), both in [[ma2021-ecc-durability-review]] | Strength class | open |
| **Temperature** | | | | |
| Temperature effect on HDC (−30 to 60 °C) | PVA-HDC (residual, 8 h): σ_tu and f_cu rise from −30 to 60 °C, ε_tu peaks at 0 °C ([[chai2023-hdc-ambient-temperature]]) | PE-HDC (Dong 2022, as cited there): f'c and σ_tu fall, ε_tu rises steadily | Fiber type, residual vs in-situ testing | open |
| Residual f'c of PVA-ECC at 400–500 °C | Rises at 400 °C (84.2 vs 72.7 MPa at 200 °C), HSECC W/B 0.20 ([[zhou2023-hsecc-elevated-temperature]], Table 5) | Drops 34% between 400 and 500 °C, CR-ECC 0% CR ([[mohammed2020-cr-ecc-elevated-temperature]], Fig. 3) | Matrix strength, temperature steps | minor, open → [[high-temperature-behaviour]] |
| Hybrid steel + polymer at high temperature | Steel raises residual f_f above 400 °C (PS-II 6.6 vs PO 2.1 MPa at 800 °C) ([[zhou2023-hsecc-elevated-temperature]], Table 5) | Same paper: steel brings spalling at 800 °C and thermal cracks up to 271 µm vs ≤ 19.6 µm without | Trade-off within one study | note → [[hybrid-fiber]] |
| PVA melting point | 230 °C onset by TG, instability 220–420 °C ([[zhou2023-hsecc-elevated-temperature]], Fig. 4) | Decomposition 263 °C (as cited in [[vanzijl2010-shcc-durability]], p. 266); 235 / 250 °C (as cited in Zhou 2023); old wiki "230–273 °C ⚠️" | Onset vs decomposition; 273 °C not supported by any ingested source | partly resolved: use 230 °C onset → [[pva-fiber]], [[high-temperature-behaviour]] |
| PE fiber melting point | about 150 °C ([[ranade2017-hshdc-impact-resistance]]; [[yu2018-ecc-direct-tensile-review]]) | 124–138 °C ([[he2024-hdc-research-advances]]); 135–145 °C ([[su2023-rubber-modified-hshdc]]) | Different products | minor |
| **Structures, interfaces & printing** | | | | |
| ECC overlays / repairs and delamination | ECC repairs avoid delamination (Lim & Li 1997, as cited in [[li2003-ecc-review]], p. 225) | All 40 mm sprayed layers debonded ([[wang2019-rc-beam-ecc-shear-strengthening]]); 10 / 30 mm SHCC layers debonded (as cited in [[xue2023-shcc-structural-review]]); chiselled NSHSDC jackets did not ([[yuan2020-nshsdc-beam-strengthening]]) | Shrinkage-driven repair vs structural loading; thickness; surface roughness | open → [[interface-bond]] |
| Thickness of strengthening layers | Thicker SHCC layers give more gain and less delamination: 50 mm +61% (as cited in [[xue2023-shcc-structural-review]]) | 40 mm sprayed ECC no better than 20 mm at a/d 3, worse in SA-40-2; all 40 mm layers debonded ([[wang2019-rc-beam-ecc-shear-strengthening]], Table 3) | Cast vs sprayed, interface preparation, shear vs flexure, over-strengthening | open → [[rc-member-strengthening]] |
| Interlayer strength of printed SHCC | Interface ≥ bulk first-crack strength, lowest void content ([[chavesfigueiredo2020-printed-shcc]], §3.5) | Flexure across the interlayer lower (18.5 vs 22.0 MPa) ([[ivaniuk2022-printable-shcc-design]], Table 3); Wolfs 2019 and Feng 2015 weaker (as cited there) | Mix, fiber (PVA vs PE), nozzle, test (direct tension vs 3PB) | open → [[3d-printed-hdc]] |
| "Deng & Zhang 2018" column study | HDC **jacketing** of cross-shaped short columns (as cited in [[he2024-hdc-research-advances]], p. 6) | Whole-HDC **square** short columns, no jacketing ([[deng2018-hdc-short-columns]]) | Another paper or mis-citation | verify → [[shear-behaviour]] |
| "Yuan 2020" beam strengthening | "steel wire plus ECC" ([[he2024-hdc-research-advances]], p. 19–20) | No-slump steel-fiber + PE NSHSDC jackets ([[yuan2020-nshsdc-beam-strengthening]]) | Another Yuan 2020 or mis-description | verify |

## Under-studied areas
Updated for the 50-source corpus (2026-10-21).

**Durability**
- **Tension after exposure.** Primary durability data now exist for freeze–thaw ([[wang2023-ecc-frost-damage]];
  [[zhong2019-ecc-freeze-thaw]]; [[chai2019-hdcc-freeze-thaw-carbonation-flexure]]), carbonation
  ([[zhang2022-ecc-carbonation-sustained-load]]), chloride ([[bu2022-ecc-chloride-crack-width]];
  [[paul2014-r-shcc-chloride-corrosion]]), sulfate ([[li2021-hdc-sulfate-dry-wet]]) and fire
  ([[zhou2023-hsecc-elevated-temperature]]; [[mohammed2020-cr-ecc-elevated-temperature]]). But none measures uniaxial
  ε_tu or crack width after exposure, and several of these "ECC" papers never demonstrate strain hardening
  (Zhong 2019, Zhang 2022, Bu 2022, Zhou 2023, Mohammed 2020). → [[durability]]
- **Durability of HSHDC/UHDC** is still missing: every primary durability study uses normal-strength PVA-ECC/HDCC.
  Reviews flag the same gap ([[ma2021-ecc-durability-review]], p. 9–10). → [[durability]], [[hshdc]]
- **Tolerable crack width per exposure.** Thresholds depend on transport mode: under immersion 100 µm ≈ uncracked
  ([[bu2022-ecc-chloride-crack-width]]); under wet–dry cycles even 22–38 µm average cracks let chloride reach steel
  ([[paul2014-r-shcc-chloride-corrosion]]). Durability thresholds use residual average widths, yet maximum widths in
  PVA-SHCC reach 290–420 µm at 3% strain ([[vanzijl2010-shcc-durability]]) and loaded widths are ≈ 2× residual
  ([[ozbay2013-ecc-self-healing-sustained-load]]). Limit strains, crack-width distributions and time-dependent widths
  under sustained load are needed for service-life design ([[vanzijl2010-shcc-durability]], p. 263–269).
  → [[crack-width]], [[chloride-and-corrosion]]
- **Crack width of PE-based HSHDC** (80–200 µm) vs PVA-ECC (about 22–90 µm average residual) is less clear-cut than
  before: under immersion the chloride threshold is 100–200 µm ([[bu2022-ecc-chloride-crack-width]]), and PE itself
  promotes healing at equal width ([[homma2009-frcc-self-healing]]); under wet–dry exposure no width is safe
  ([[paul2014-r-shcc-chloride-corrosion]]). → [[crack-width]], [[self-healing]]
- **Chloride and corrosion:** calibrated half-cell criteria for SHCC, pitting models, and free vs total chloride in
  high-FA matrices ([[paul2014-r-shcc-chloride-corrosion]]); chloride deeper than 30 mm for wide cracks
  ([[bu2022-ecc-chloride-crack-width]]); direct corrosion tests on sprayed ECC overlays ([[kanda2003-sprayed-ecc]],
  p. 279). → [[chloride-and-corrosion]]
- **Carbonation of high-FA ECC** is faster than reviews suggest (4.8–13 mm at 28 d, 20% CO₂;
  [[zhang2022-ecc-carbonation-sustained-load]]; [[wang2023-ecc-frost-damage]]); no plain-concrete control under the
  same exposure; carbonation of cracked ECC under sustained load is untested. → [[carbonation]]
- **Salt scaling:** SHCC fails the RILEM CDF criterion (2.2 > 1.5 kg/m²) ([[vanzijl2010-shcc-durability]], p. 267).
  → [[freeze-thaw]]
- **Self-healing under service load and repeated damage:** unloaded tests overestimate healing
  ([[ozbay2013-ecc-self-healing-sustained-load]]); 100% recovery after repeated damage is not reached
  ([[herbert2013-ecc-self-healing-natural-environment]]). → [[self-healing]]
- **Long-term ageing:** most mechanical data are at 28 d; the longest field-exposure set is 12 months
  ([[herbert2013-ecc-self-healing-natural-environment]]). Ductility may fall with age (⚔️ row "PVA-ECC ductility vs age").
  → [[durability]]
- **Shrinkage:** no primary shrinkage measurement in the corpus; the effect of cellulose/starch ethers on shrinkage of
  printed SHCC is untested ([[ivaniuk2022-printable-shcc-design]]). → [[shrinkage]]
- **Recycled-fine-aggregate HDCC** (absorption 6.72%) has no durability data ([[gao2020-hdcc-recycled-fine-aggregate]]).
  → [[recycled-fine-aggregate]]
- **Interface drift in service:** chloride cycling lowers and hot water raises the PVA chemical bond (as cited in
  [[vanzijl2010-shcc-durability]]); the durability of oil/VAE coatings is unknown ([[sun2019-modified-pva-fiber-ecc]]).
  → [[fiber-matrix-interface]]

**Fire and temperature**
- **No fire design data and no in-situ (hot) tension data** for HDC. PE-ECC loses strain hardening between 100 and
  140 °C, PVA-ECC at about 150–200 °C (reviews, see [[high-temperature-behaviour]]); PVA melts from 230 °C
  ([[zhou2023-hsecc-elevated-temperature]], Fig. 4). Steel-fiber hybrids raise residual strength but re-introduce
  spalling ([[zhou2023-hsecc-elevated-temperature]]). → [[high-temperature-behaviour]], [[hybrid-fiber]]

**Chinese HDC and the XAUAT (Deng) group**
- Three Deng (XAUAT) papers are now ingested ([[deng2015-hdc-compressive-toughness]];
  [[deng2018-hdc-compressive-constitutive]]; [[deng2018-hdc-short-columns]]), but they report no curing regime or test
  age in the material sections, and the Deng 2019 masonry shake-table test is still known only second-hand
  (via [[he2024-hdc-research-advances]]). → [[masonry-wall-retrofit]], [[heat-curing]]
- **Compression models** exist only for XAUAT PVA-HDC (one group, one fiber); none for PE-HSHDC.
  → [[compressive-constitutive-model]]
- **Labelled but untested materials:** many papers call their material HDC/HDCC/ECC/SHCC without a tension test
  (Chai 2019, Deng 2015 / 2018a, Zhou 2023, Yuan 2020, Lee 2021, Mohammed 2020, Bu 2022, Zhong 2019; see their source
  pages). Several report only bending; deflection hardening ≠ tensile hardening ([[zhang2022-hshdcc-review]], p. 9–10;
  [[kanakubo2006-dfrcc-tensile-test-method]], p. 14). → [[terminology-hdc-ecc-shcc]]
- **Korean HSDC/NSHSDC tensile ductility** is not shown in the ingested papers ([[yuan2020-nshsdc-beam-strengthening]];
  [[lee2021-hsdc-wall-emi-impact]]); the > 2.9% claim is second-hand. → [[hshdc]], [[hybrid-fiber]]

**Test methods**
- **Standard test methods:** JCI standardised a four-point-bending moment–curvature method (JCI-S-003-2005) because direct
  tension was too scattered ([[kanakubo2006-dfrcc-tensile-test-method]]; [[qian2007-shcc-inverse-tensile-strain]]).
  No inverse method is validated for PE-HSHDC or Chinese PVA-HDC, beam geometry is not agreed, and JC/T 2461-2018
  (cited in [[chai2023-hdc-ambient-temperature]]) is still not ingested. Already an R&D need in 2003
  ([[li2003-ecc-review]], Sect. 8). → [[dogbone-uniaxial-tension]], [[four-point-bending-inverse-analysis]]
- **Member-scale vs dogbone ductility:** dogbone ε_tu does not transfer to thick members (0.23% vs 1.5%,
  [[kunieda2010-uhp-shcc-steel-reinforcement]]) or thin bonded layers that crack only over the substrate crack
  ([[xue2023-shcc-structural-review]]). A zero-span test is called for ([[kunieda2006-hpfrcc-japan-applications]], p. 23),
  and the minimum reinforcement to secure material ductility is not established
  ([[kunieda2010-uhp-shcc-steel-reinforcement]], §1). → [[size-effect]], [[multiple-cracking]]
- **Flaw size** is never measured; Kanda & Li call for a random, interacting-flaw model
  ([[kanda2006-psh-design-criteria]], p. 68). → [[matrix-fracture-toughness]]
- **Size-independent tensile constitutive model** ([[yu2018-ecc-direct-tensile-review]]) and a **cyclic tension damage
  model** ([[zhao2022-ecc-tension-damage-model]], Concl. 5). → [[tensile-constitutive-model]]

**Micromechanics and constituents**
- **Interface data** (pull-out) exist only for Michigan PE-HSHDC and Michigan PVA-ECC. Round-4 bond claims for Chinese
  HDC rest on SEM only ([[gao2020-hdcc-recycled-fine-aggregate]]; [[shumuye2022-slag-fa-pe-ecc]];
  [[wang2023-ecc-frost-damage]]). → [[fiber-matrix-interface]]
- **Curing regime:** its effect on PSH indices and ductility is unclear ([[zhang2022-hshdcc-review]]). → [[heat-curing]]
- **FA optimum depends on the property:** ductility peaks near FA/C ≈ 3 ([[jin2019-hvfa-shcc-structural]]), frost
  resistance near 35% replacement ([[zhong2019-ecc-freeze-thaw]]); no study optimises both. → [[fly-ash]]
- **Slag:** no source measures its effect on PSH indices or bond; slag widens cracks (qualitative,
  [[shumuye2022-slag-fa-pe-ecc]]). → [[ggbfs]]
- **Crumb rubber:** only one source with tension data ([[su2023-rubber-modified-hshdc]]); [[mohammed2020-cr-ecc-elevated-temperature]]
  is compression-only. → [[crumb-rubber]]
- **VMA dosage** (HPMC, cellulose, starch ether) is never varied against ε_tu ([[ivaniuk2022-printable-shcc-design]]).
  → [[viscosity-modifying-admixtures]]

**Structures and applications**
- **Structural data are now partly primary:** beam shear strengthening ([[wang2019-rc-beam-ecc-shear-strengthening]];
  [[yuan2020-nshsdc-beam-strengthening]]), whole-HDC short columns ([[deng2018-hdc-short-columns]]), reinforced UHP-SHCC
  members ([[kunieda2010-uhp-shcc-steel-reinforcement]]) and HSDC-skinned panels under impact
  ([[lee2021-hsdc-wall-emi-impact]]). Masonry retrofit is still numerical only
  ([[tabrizikahou2022-masonry-ecc-sma-retrofit]]) or second-hand (Deng 2019). → [[rc-member-strengthening]], [[masonry-wall-retrofit]]
- **Shear design of HDC members:** applicability of RC shear formulas unknown ([[deng2018-hdc-short-columns]], p. 10);
  ECC softening coefficient under tension–compression unmeasured ([[wang2019-rc-beam-ecc-shear-strengthening]], Sect. 4.4);
  no shear tests on PE-HSHDC members. → [[shear-behaviour]]
- **Bond to existing concrete:** slant-shear data exist for one Korean steel + PE mix at 28 d
  ([[yuan2020-nshsdc-beam-strengthening]], Table 7); no pull-off or direct-shear tests for PVA-ECC/HDC layers; layer
  thickness and roughness are never varied together; the FE interface law changes dissipated energy about 2×
  ([[tabrizikahou2022-masonry-ecc-sma-retrofit]], Table 8). A rebar bond-slip law for ECC/HDC is missing
  ([[wang2023-ecc-frost-damage]], §1). → [[interface-bond]]
- **Field performance:** field crack widths exist only second-hand: sprayed HPFRCC on an ASR wall ≤ 50 µm (10 months) and
  ≤ 120 µm (24 months) vs 300 µm for repair mortar (Rokugo 2005, as cited in [[kunieda2006-hpfrcc-japan-applications]],
  p. 29). No primary field-monitoring paper, nothing beyond 24 months, no performance data for Mihara Bridge or Mitaka
  Dam, and no field deployment of HSHDCC ([[zhang2022-hshdcc-review]], p. 2). → [[repair-and-field-applications]]
- **Fatigue:** one primary data set only (PE UHP-ECC flexure, one mix; [[sui2018-uhp-ecc-flexural-fatigue]]); no PVA-HDC
  or tensile fatigue primary data. → [[fatigue]]
- **Extreme loading:** no data above 10 s⁻¹ for HSHDC; one primary PVA-SHCC study up to 50 s⁻¹
  ([[mechtcherine2011-shcc-high-strain-rate]]) leaves open why PVA switches back to pull-out above 10 s⁻¹ (p. 60–61).
  Reinforced HSHDC members under impact are untested; HSDC skins on concrete panels were tested one panel per case
  ([[lee2021-hsdc-wall-emi-impact]]). → [[strain-rate-effects]], [[impact-resistance]]
- **Sprayed ECC:** proof that small COD slows rebar corrosion and larger-scale retrofit tests are needed
  ([[kanda2003-sprayed-ecc]], p. 279, 281). → [[repair-and-field-applications]]
- **3D printing:** ductile composites for thick printed elements and 3DCP-compatible reinforcement
  ([[chavesfigueiredo2020-printed-shcc]]); adhesiveness tests free of bleeding effects
  ([[ivaniuk2022-printable-shcc-design]]). → [[3d-printed-hdc]]

**Corpus gaps (not research gaps)**
- 10 ScienceDirect/ACI papers on the reading list are still missing (download blocked; see [[log]], 2026-10-21).
  Kanda & Li 1998, JSCE 2008 and JC/T 2461-2018 are cited but not ingested.

## Open questions
- Can PSH indices be extended to include embedment length and flaw size (as in Li & Leung 1992)?
- Can PE-HSHDC crack widths be brought below 60–80 µm, e.g. with hybrid steel, SF or rubber, to gain
  self-healing and chloride resistance — and does that matter under immersion, where 100 µm ≈ uncracked?
- Does ambient-cured HSHDC keep its ductility after long-term ageing?
- Why does PVA-SHCC switch back to fiber pull-out above 10 s⁻¹ ([[mechtcherine2011-shcc-high-strain-rate]])?
- Does recycled fine aggregate raise ductility through bond or through flaws ([[gao2020-hdcc-recycled-fine-aggregate]])?
- What minimum reinforcement ratio secures dogbone-level ductility in thick members
  ([[kunieda2010-uhp-shcc-steel-reinforcement]])?
