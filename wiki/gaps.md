---
type: hub
updated: 2026-10-26
---

# Research Gaps, Conflicts & Open Questions

This page feeds the "Research gaps and future directions" chapter of [[review-outline]].
Corpus: 63 source pages (round 7, 2026-10-26: three Chonnam National University alkali-activated / geopolymer composites
added to the 60 of round 5). 80 conflict rows below, grouped by theme (51 after round 4; 64 after round 5, which added
13 rows, updated 12 and resolved or probably resolved 4; the PDF re-ingest added 9 rows — 8 internal inconsistencies of
single sources and 1 corrected wiki reading, already resolved — and updated 13; round 7 added 7 rows and updated 3).

## ⚔️ Conflicts between sources
| Topic | Source A says | Source B says | Possible reason | Status |
|---|---|---|---|---|
| **Terminology & classification** | | | | |
| Meaning of "HDC" / "HSHDC" | HSHDC = Michigan PE + VHSC matrix, 166 MPa, heat-cured ([[ranade2017-hshdc-impact-resistance]]) | HSHDC = Xi'an ambient-cured, about 100 MPa ([[yang2024-hshdc-uniaxial-tension]]); GDUT ([[su2023-rubber-modified-hshdc]]); umbrella HSHDCC > 100 MPa and > 3% ([[zhang2022-hshdcc-review]]); Korea Univ. HSDC/NSHSDC = 1.0% steel + 0.5% PE hybrid, ≈ 122–123 MPa ([[yuan2020-nshsdc-beam-strengthening]]; [[lee2021-hsdc-wall-emi-impact]]) | Same name used by different groups (now 4 lineages) | open: always state the lineage, see [[terminology-hdc-ecc-shcc]], [[hshdc]] |
| Class thresholds | HSHDCC: > 100 MPa, > 3% ([[zhang2022-hshdcc-review]]) | > 55 MPa and > 4%, or > 80 MPa and > 2% (other reviews, as cited there); normal HDC 30–80 MPa ([[su2023-rubber-modified-hshdc]]) vs normal ECC 40–70 MPa ([[zhang2022-hshdcc-review]]) | Chinese standard JC/T 2461-2018 sets only ≥ 0.5% and ≤ 200 µm (as cited in [[chai2023-hdc-ambient-temperature]]) | open: two bars, ECC convention vs HDC standard |
| Origin of the 0.5% / 200 µm HDC(C) definition | JSCE 2008 ([[chai2019-hdcc-freeze-thaw-carbonation-flexure]], p. 126) | JC/T 2461-2018 ([[chai2023-hdc-ambient-temperature]], §1); same group, same numbers | Chinese standard may have adopted the JSCE values; neither document ingested. XAUAT also cites an earlier Shaanxi standard DBJ61/T112-2016 ([[deng2019-urm-shaking-table-hdc]], ref. [20]), not ingested | verify |
| HDC vs ECC | "HDC stands for ECC" (p. 2) | "HDC developed on the basis of ECC" (p. 10), both in [[he2024-hdc-research-advances]] | Internal inconsistency | treat HDC ≈ ECC/SHCC |
| Definition of "ε_tu" | strain at peak stress (wiki convention, [[tensile-strain-capacity]]) | Gao 2020 "ε_tu" = post-peak maximum strain, up to 11.73% (ε_tp at peak 1.68–4.76%) ([[gao2020-hdcc-recycled-fine-aggregate]]); Zhao 2022 ε_u post-peak 1.9–4.1% vs ε_p 0.5–2.0% ([[zhao2022-ecc-tension-damage-model]], Table 3); Sun 2019 "ultimate tensile strain" = end of curve incl. softening (S3 peak ≈ 1.0% vs 2.02% reported; [[sun2019-modified-pva-fiber-ecc]], Figs. 8–9, p. 15); Wang 2019 ≈ 0.9–1.9% at peak vs ≈ 2.6–3.45% at end of curve ([[wang2019-rc-beam-ecc-shear-strengthening]], Fig. 2, p. 3, read). Chai 2023 and Shumuye 2022 report strain **at peak** ([[chai2023-hdc-ambient-temperature]], Fig. 1, p. 2; [[shumuye2022-slag-fa-pe-ecc]], Fig. 5b, p. 8) | Inconsistent naming | resolved: compare strain at peak only |
| "ECC" in FE models | ECC = strain hardening, σ_tu ≈ 3–5 MPa (e.g. 4.84 MPa, [[wang2019-rc-beam-ecc-shear-strengthening]]) | Abaqus CDP input softening from σ_t 1.45 MPa ([[tabrizikahou2022-masonry-ecc-sma-retrofit]], Table 5); Wang 2019's own truss model reproduces its Table 4 only with σ_t = 4.0 MPa (Table 1 f_t), not the 4.84 MPa peak ([[wang2019-rc-beam-ecc-shear-strengthening]], pp. 4, 13, computed) | Borrowed non-hardening input | open: flag FE studies whose "ECC" is not strain-hardening → [[tensile-constitutive-model]] |
| **Design theory & micromechanics** | | | | |
| Quasi-static ε_tu of Michigan HSHDC | 3.4% (as quoted in [[ranade2017-hshdc-impact-resistance]]; quoted again from Ranade et al. 2013 in [[choi2016-pe-alkali-activated-slag-composite]], §1, with first crack 8.3 vs 8.1 MPa elsewhere — minor) | 4.2% ([[ranade2015-hshdc-tensile-rate-effects]]); 3.5% for the 2011 version ([[zhang2022-hshdcc-review]]) | Batch and fiber version (38 vs 28 µm) | open: report 3.4–4.2% |
| Strength–ductility trade-off | ε_tu falls as f'c rises across the primary sources (UHDC 9.45% → Michigan 3.4–4.2%) | f'c > 210 MPa with ε > 5%, and 122 MPa with 8.5% (as cited in [[zhang2022-hshdcc-review]]); primary: 7.50% at σ_tu 13.06 MPa and f'c 54.8 MPa, cementless, no heat curing ([[choi2016-pe-alkali-activated-slag-composite]], Tables 5, 7); (2026-10-26) cementless HSUD-EGC 10.51% at f'c 84.3 MPa ([[huy2023-egc-pe-pva-hybrid-healing]], Table 5, Fig. 3). Within one study, however, a weaker matrix still gave more strain: ED-EGC 31.1 MPa / 10.97% → 20.7 MPa / 18.62% ([[huy2023-egc-activator-pretreatment]], Table 4), and the 22.34% maximum is at only 7.63 MPa σ_tu ([[hieu2023-aas-extremely-ductile-22pct]]) | Interface and fiber design, not f'c alone; within a fixed system, matrix weakening still trades strength for strain | resolved: the trade-off is **not fundamental** (across systems); it persists locally within one system |
| PSH thresholds | "> 1.2 and > 3" quoted for all fibers (Su 2023, Ranade 2015, Zhang 2022) | 1.2 / 3 apply to pull-out type; fiber-rupture type needs > 1.3 and > 2.7 ([[kanda2006-psh-design-criteria]], p. 69–70); a third value σ0/σ_fc > 1.45 for PVA-SHCC, attributed to Kanda & Li 1998, together with J′b/J_tip > 3 ([[jin2019-hvfa-shcc-structural]], §2.2, p. 3) | Papers quote the 1998 set; 1.45 may be a mis-quote or a different index (Kanda & Li 1998 not ingested) | partly resolved: check which set applies; verify 1.45 |
| PSH criteria vs behaviour | 6 mm PE mixes meet the 1998 thresholds but fail brittle ([[su2023-rubber-modified-hshdc]]) | In PVA-ECC the energy index (> 3) predicts saturation well ([[li2002-pva-ecc-interface-tailoring]]) | PE6 fails the 2006 strength threshold (1.2 < 1.3); flaw-size and embedment terms missing ([[li1992-steady-state-multiple-cracking]]) | partly resolved |
| Scaling single-crack bridging to full Vf | J′b and σ0 measured at 0.2 vol.% PE scaled ×8.75 to 1.75 vol.%, assuming proportionality (citing Yang 2008) → PSH_E 452 / 817 ([[huy2023-egc-activator-pretreatment]], §3.2, Table 7) | The scaled σ0 (12.7 / 11.2 MPa) exceeds the measured composite fts (8.72 / 5.54 MPa) of the same paper (Table 4); all other PSH_E rows in [[micromechanical-parameters]] are ≤ ≈ 200 | Fibre interaction, dispersion and orientation at high Vf make bridging less than proportional | open: treat the scaled PSH_E as an upper bound → [[strain-hardening]], [[single-crack-test]] |
| Does the stress index separate ductile from brittle PVA mixes? | no: 1.5–1.8 for all ([[li2002-pva-ecc-interface-tailoring]]) | yes: 1.14–1.16 → 0.3–0.6%, 1.31–1.32 → 1.0–1.5% ([[kanda2006-psh-design-criteria]]) | Different matrices (mortar vs paste) | open |
| β of oiled PVA | 0.58–0.63 in the M45 fly-ash matrix ([[yang2008-ecc-fiber-bridging-law]]) | 1.15 in a w/c 0.45 matrix without fly ash ([[li2002-pva-ecc-interface-tailoring]]) | Matrix and fly ash | resolved: matrix-dependent |
| Bond vs ductility (recycled fine aggregate) | Lower PVA bond (oiling) → ε 0.99 → 4.88% ([[li2002-pva-ecc-interface-tailoring]]; Li & Leung argument in [[chai2019-hdcc-freeze-thaw-carbonation-flexure]]) | RFA raises bond (inferred from SEM) and ε_tp 1.68 → 4.76% at 2% PVA ([[gao2020-hdcc-recycled-fine-aggregate]], Table 6, Fig. 16) | N-HDCC bond (unoiled domestic PVA, W/B 0.45) may be below the optimum; RFA may act via flaws ("crack trapping"); no pull-out data | open → [[recycled-fine-aggregate]], [[interface-bond]] |
| Vf vs tensile peak stress | σ0 ∝ Vf in bridging models ([[yang2008-ecc-fiber-bridging-law]]; [[jin2019-hvfa-shcc-structural]], Fig. 1a) | σ_p flat (3.10 / 2.96 / 3.23 MPa) for 1 / 1.5 / 2% PVA ([[zhao2022-ecc-tension-damage-model]], Table 3) | Matrix; flaw- or rupture-controlled peak | open → [[fiber-geometry]] |
| PVA-ECC σ_tu "3–8 MPa" | attributed to Li 2003 in [[yu2018-ecc-direct-tensile-review]] | not in [[li2003-ecc-review]] (only ε ≈ 5%) | Probably another Li 2003 paper | verify |
| **Constituents & mix design** | | | | |
| Slag/FA effect on PE-ECC ductility | Text: all-FA mix SF-0-60 had the highest tensile capacity; slag reduces strain ([[shumuye2022-slag-fa-pe-ecc]], Sect. 3.2) | Same paper's data, strain **at peak, 28 d** (basis confirmed from the PDF): ε ≈ 2.0% (SF-0-60) < 2.2% (SF-15-45, read) < 2.9% (SF-10-50) < 3.5% (SF-5-55) (Fig. 5b, p. 8); crack width ≈ 100 → 130 µm from 0 to 15% slag (radar Fig. 10, p. 12, read) | Internal text vs data inconsistency; strain basis now known, so the inconsistency is real | open (Fig. 5 checked 2026-10-21: data contradict the text) → [[fly-ash]], [[ggbfs]] |
| W/B and PVA-ECC ductility | Lower W/B more ductile: 0.30 → 3.79% vs 0.35 → 3.21% at 7 d ([[sun2019-modified-pva-fiber-ecc]], Table 10) — but these are end-of-curve strains and lie **within the scatter** of Fig. 6 (S1 ≈ 2.3–5.25%, S4 ≈ 2.6–3.8%; p. 13), so Sun 2019 is weak evidence; cementless alkali-activated slag + PE, W/B 0.26 → 0.38: ε 7.50 → 4.58%, σ_tu 13.06 → 5.06 MPa ([[choi2016-pe-alkali-activated-slag-composite]], Table 7) | Higher W/B more ductile: 0.24 → 0.28 gives ε_p ×4 ([[zhao2022-ecc-tension-damage-model]], Table 3); W/B 0.31 → 0.20 lowers ε_tu at peak ([[chai2023-hdc-ambient-temperature]]) | Different ranges, ages (7 d vs ≥ 28 d), matrices; fibre–matrix pair (PE without chemical bond, no aggregate, vs PVA); strain basis (end of curve in Sun) | open, weakened (Sun's effect is within scatter; side A now rests mainly on Choi 2016) → [[water-binder-ratio]], [[alkali-activated-binder]] |
| Short (6 mm) PE fiber | 6 mm × 12 µm PE at 1.5% → strain softening, W/B 0.45 ([[homma2009-frcc-self-healing]], p. 224); 6 mm × 20 µm PE brittle ([[su2023-rubber-modified-hshdc]]) | Same 6 mm × 12 µm at 1.5% strain-hardens in W/B 0.20 UHP-SHCC ([[kunieda2010-uhp-shcc-steel-reinforcement]]) and in printed SHCC ([[ivaniuk2022-printable-shcc-design]]) | Aspect ratio and matrix strength, not length alone | open → [[fiber-geometry]], [[pe-fiber]] |
| PVA fiber length effect (as cited) | longer gives lower ductility (Feng 2022) | 18 mm better than 12 mm (Lee 2023), both in [[su2023-rubber-modified-hshdc]] | Matrix and test | open |
| PVA-ECC ductility vs age | REC-15 ECC 3.21% (7 d) → 1.39% (28 d), end-of-curve strain; the drop exceeds the scatter (S4 7 d ≈ 2.6–3.8% vs C1 28 d ≈ 0.95–1.8%) ([[sun2019-modified-pva-fiber-ecc]], Table 11, Fig. 6, pp. 13, 16) | Michigan PVA-ECC ≈ 4–5% at 28 d ([[li2002-pva-ecc-interface-tailoring]]); ≈ 3% at 180 d (Lepech & Li 2006, as cited in [[yu2018-ecc-direct-tensile-review]]) | Different matrix (FA content unknown), curing, coating | open → [[pva-fiber]], [[heat-curing]] |
| Fiber orientation in printed SHCC | Mainly diagonal to the print path, measured by µCT: peaks ≈ 40° and ≈ 170°, minimum ≈ 90° ([[chavesfigueiredo2020-printed-shcc]], Fig. 17, p. 19, read) | Assumed aligned with the print direction (citing Li et al. 2020) ([[ivaniuk2022-printable-shcc-design]]) | Measured vs assumed; PVA vs PE; nozzles and mixes | open → [[fiber-dispersion]], [[3d-printed-hdc]] |
| PVA modulus, same 1600 MPa grade (minor) | 40 GPa ([[deng2017-rc-column-hdc-jacket]]; [[li2021-hdc-beam-shear]]; [[zhang2022-hdc-basalt-textile-tension]]) | 32 GPa ([[deng2019-urm-shaking-table-hdc]], Table 2); 14 GPa ⚠️ ([[pourfalah2018-ecc-high-temperature]], Table 3) | Typo or different product | verify → [[pva-fiber]] |
| HRWR in "M45" ECC (minor) | 17 kg/m³ ([[yang2009-ecc-self-healing-wet-dry]], Table 1) | 7.51 kg/m³ ([[lepech2009-ecc-water-permeability]], Table 1), same other proportions | Different HRWR products or batches; cross-referenced in both rows of [[mix-designs]] | note → [[mix-designs]] |
| PE fibre strength, same 12 µm × 18 mm product line (minor) | 2700 MPa, 88 GPa ([[choi2016-pe-alkali-activated-slag-composite]]; [[hieu2023-aas-extremely-ductile-22pct]]; [[huy2023-egc-activator-pretreatment]], Table 3 each) | 3030 MPa, 88 GPa ([[huy2023-egc-pe-pva-hybrid-healing]], Table 3), same group | Different product or batch, or updated datasheet | verify → [[pe-fiber]] |
| **Tension, compression, flexure, fatigue** | | | | |
| Specimen thickness / geometry effect in direct tension | 13 / 30 / 50 mm thickness negligible for PVA-ECC (Rokugo 2007, as cited in [[yu2018-ecc-direct-tensile-review]], p. 348) | Same PVA-DFRCC: 2.70% thin plate (T1), 2.38 / 0.77% dogbone H/V, 0.07% Ø70 dogbone, 0.32% Ø100 cylinder, CV > 100% ([[kanakubo2006-dfrcc-tensile-test-method]], Tables 6–9); 50 × 200 mm unreinforced UHP-SHCC members 0.23% vs 1.5% in 13 mm dumbbells ([[kunieda2010-uhp-shcc-steel-reinforcement]], Table 3) | Shape, casting direction, end fixity, fiber type, 2-D vs 3-D orientation | open: always record geometry, casting direction and grips with ε_tu → [[tensile-strain-capacity]], [[size-effect]], [[dogbone-uniaxial-tension]] |
| XAUAT PVA-HDC tensile strain capacity (same nominal mix and fibre) | ≈ 3.0% ultimate with Japanese PVA (1600 MPa, 40 GPa), σ_tu 6.12 MPa; ≈ 1.2% with Chinese PVA, 4.84 MPa ([[deng2017-rc-column-hdc-jacket]], Fig. 1a ⚠️ read) | ≈ 1.0% at σ_tu 6.14 MPa ([[deng2018-hdc-short-columns]], Fig. 1); ≈ 1.0% at 5.83 MPa ([[deng2019-urm-shaking-table-hdc]], Fig. 6a); 0.968% at 5.83 MPa ([[li2021-hdc-beam-shear]], §2.1); ≈ 1.24% at 1.7% PVA ([[deng2020-aac-wall-hdc-retrofit]], Fig. 3); plain HDC only **0.34% (M1-2) / 0.45% (M2-2)** at peak, 2% PVA, 28 d — below the JC/T 0.5% bar ([[zhang2022-hdc-basalt-textile-tension]], Table 8) | Batch, specimen geometry (mostly not reported), strain basis (end of curve vs at peak), figure reading; the 2018 fibre properties match the Japanese fibre; possible reuse of curves (Deng 2019 vs Deng 2018); Zhang 2022 matrix differs (SF + undefined "mineral powder", W/B ≈ 0.30–0.32 computed vs 0.29) and uses a 230 mm narrow length. Chinese vs Japanese PVA is the only controlled comparison | open → [[tensile-strain-capacity]], [[pva-fiber]], [[terminology-hdc-ecc-shcc]] |
| σ_tu of the li2021 HDC (internal) | 5.83 MPa (§2.1) | 5.68 MPa (Conclusion 1), same paper ([[li2021-hdc-beam-shear]]) | Typo in one location; both kept in [[mechanical-results]] | verify |
| XAUAT HDC compressive peak strains | mixes 1–4: 0.22 / 0.74 / 0.67 / 0.80%, matrix 640.45 kN ([[deng2015-hdc-compressive-toughness]], Table 3) | same peak loads, 0.213 / 0.569 / 0.601 / 0.672%, matrix 630.55 kN ([[deng2018-hdc-compressive-constitutive]], Table 3) | Same tests reprocessed? Fig. 7a peak near 0.7% | verify → [[compressive-constitutive-model]] |
| Reference test for bending inverse methods | UM/JCI inverse ε 3.0 / 3.1% matches "UTT" 2.7% for JCI PVA ([[qian2007-shcc-inverse-tensile-strain]], Table 8) | That 2.7% is the thin-plate T1; the same-section T2 dogbone gave 2.38% (H) / 0.77% (V) ([[kanakubo2006-dfrcc-tensile-test-method]], Table 7) | Agreement depends on the chosen tension reference | open → [[four-point-bending-inverse-analysis]] |
| ECC flexural S–N shape | Bilinear with inflection at S ≈ 0.9, N 10²–10⁴ (Matsumoto 2003 via [[kunieda2006-hpfrcc-japan-applications]]; Suthiwarapirak 2004, Liu 2017 via [[sui2018-uhp-ecc-flexural-fatigue]]) | Continuous, no inflection: S = 1 − 5.75×10⁻³(lg N)^2.43 for PE UHP-ECC ([[sui2018-uhp-ecc-flexural-fatigue]], Eq. 2) | PVA vs PE, matrix strength, small data set (3 beams/level) | open → [[fatigue]] |
| UHPC flexural size effect (as cited) | significant | reduced, both in [[ye2021-uhdc-flexural-size-effect]] | Size range and method | open |
| **Dynamic behaviour** | | | | |
| PVA-ECC ε vs strain rate | decreases (Yang & Li 2014; Mechtcherine, as cited in [[yu2018-ecc-direct-tensile-review]]); no significant change (Boshoff & van Zijl 2007, as cited there) | Primary: ε 1.49 → 0.82% up to 10⁻² s⁻¹, then 0.68 → 1.79% at 10–50 s⁻¹ ([[mechtcherine2011-shcc-high-strain-rate]], Table 2) | Rate range explains part of the disagreement | partly resolved: non-monotonic → [[strain-rate-effects]] |
| PVA failure mode at high rate | pull-out dominates in composite tests; rupture dominates in single-fiber tests ([[yu2018-ecc-direct-tensile-review]], p. 350) | In one composite: rupture ≤ 10⁻² s⁻¹, pull-out ≥ 10 s⁻¹ ([[mechtcherine2011-shcc-high-strain-rate]], Fig. 10) | Rate-dependent switch, plus scale effect | refined: mode switches with rate; cause still open |
| PVA-ECC DIF 6.7 attribution | Curosu 2016, about 150 s⁻¹ (as cited in [[yu2018-ecc-direct-tensile-review]]) | Millon et al. 2010, 140–180 s⁻¹ (as cited in [[mechtcherine2011-shcc-high-strain-rate]], p. 58) | Possible misattribution in the review | verify |
| **Cracking & durability** | | | | |
| Chloride crack-width threshold | 55–80 µm (Jang 2011) and ≥ 90 µm (Wu 2017), as cited in [[he2024-hdc-research-advances]], p. 10; ≈ 100 µm (Sahmaran 2007, as cited in [[vanzijl2010-shcc-durability]], p. 264; figure plots deformation) | Immersion, cast notches: 100 µm ≈ uncracked, significant ≥ 200 µm ([[bu2022-ecc-chloride-crack-width]]); wet–dry capillary: 50–100 µm (and < 50 µm) cracks carry Cl⁻ to rebar within hours, no correlation with width ([[paul2014-r-shcc-chloride-corrosion]], Table 5, Fig. 10) | Transport mode (diffusion vs capillary suction), notch vs real crack, matrix porosity (w/c 1.0 in Paul) | refined: threshold is **exposure-dependent**; treat 55–80 µm as second-hand → [[chloride-and-corrosion]], [[crack-width]] |
| Corrosion rate R/SHCC vs R/mortar | Similar, ≈ 0.003–0.02 mm/yr; localised pitting in R/SHCC ([[paul2014-r-shcc-chloride-corrosion]], Fig. 8, Table 4) | Slower in R/SHCC (Miyazato & Hiraishi 2005; Sahmaran 2008; Kobayashi 2010, as cited in [[vanzijl2010-shcc-durability]], p. 265) | Pre-crack deflection, measurement start time, porous w/c 1.0 matrix in Paul | open → [[chloride-and-corrosion]] |
| Crack width loaded vs residual | Under sustained flexural load ≈ 2× unloaded (60 → 115, 40 → 85 µm); healing reduced (stiffness 76 vs 87%, 83 vs 95%) ([[ozbay2013-ecc-self-healing-sustained-load]], Tables 3–4) | Tension, short-term: ≈ 15% closure on unloading, now **primary** ([[yang2009-ecc-self-healing-wet-dry]], p. 385; earlier known via [[herbert2013-ecc-self-healing-natural-environment]]); ≈ 10% (5–10 µm) closure ([[lepech2009-ecc-water-permeability]], p. 749) | Loading mode (flexure vs tension) and duration (sustained vs short-term); all wiki thresholds use residual widths | open → [[crack-width]], [[self-healing]] |
| Permeability at ≈ 500 µm (reinforced mortar) | "10⁻¹¹ to 10⁻⁵ m/s from 0 to 500 µm" (Lepech & Li 2009, as cited in [[ma2021-ecc-durability-review]], p. 5; earlier wiki wording) | Primary: 4.58 × 10⁻¹¹ (uncracked) → 2.58 × 10⁻⁵ (300 µm) → **4.46 × 10⁻⁴ m/s (500 ± 50 µm)** ([[lepech2009-ecc-water-permeability]], Table 5) | Review misreported or wiki misread; 10⁻⁵ is the 300 µm value | resolved: use the primary value → [[permeability]] |
| "Water-permeability threshold 0.10–0.15 mm" | Attributed to Lepech & Li 2009 in [[paul2014-r-shcc-chloride-corrosion]], p. 341 | Primary gives only 100 µm, from Wang et al. 1997 (concrete); its mortar at 150 µm already has k 3.02 × 10⁻⁸ m/s, ≈ 3 orders above uncracked ([[lepech2009-ecc-water-permeability]], p. 745, Table 5) | Mis-citation in Paul 2014 | resolved: mis-citation → [[permeability]] |
| Origin of the "100 µm permeability threshold" | ≈ 100 µm credited to Lepech & Li 2005 ([[vanzijl2010-shcc-durability]]) and used across the wiki for ECC | In Lepech & Li 2009 it is a **design target** from single cracks in concrete (Wang 1997, as cited); ECC was tested only at 50–63 µm ([[lepech2009-ecc-water-permeability]], p. 745–746) | Lepech & Li 2005 not ingested; threshold not measured on ECC | refinement: cite as "Wang 1997, adopted by Lepech & Li" → [[permeability]], [[crack-width]] |
| Carbonation depth, unloaded ECC, 28 d at ~20% CO₂ | 4.78 mm ([[zhang2022-ecc-carbonation-sustained-load]], Table 4, p. 7) | ≈ 13 mm ([[wang2023-ecc-frost-damage]], Fig. 15a, read from figure); ≈ 0.8 mm (Zhang W. 2018, PP+PVA ECC, as cited in [[ma2021-ecc-durability-review]], p. 9) | Two primary mixes almost identical (PVA, FA/C 1.18–1.20, W/B 0.30–0.33, GB/T 50082) yet differ ≈ 2.7×; preconditioning, specimen size, figure reading; the 0.8 mm mix has PP fiber | open → [[carbonation]] |
| Freeze–thaw citation (Yun 2013 vs Yun 2011) | Yun 2013, hybrid PVA+PE ([[he2024-hdc-research-advances]]) | Yun 2011, PVA loses more ε than PE ([[ma2021-ecc-durability-review]]) | Two different papers: Yun 2013 = [[yun2013-shcc-freeze-thaw]] (Compos. Part B 52:11–20); Yun 2011 = Yun, Kim, Lee & Rokugo, Cold Reg. Sci. Technol. 67:49–57 (ref. [24] there; not ingested). he2024's summary is supported by the primary paper | **resolved**: two papers → [[freeze-thaw]] |
| ε_tu after freeze–thaw | ε_tu ≈ 3% retained after 300 cycles, PVA-ECC, ASTM C666 A (Li et al. 2003, as cited in [[vanzijl2010-shcc-durability]], p. 267) | Hybrid PVA + PE SHCC: σ_tu kept, ε at peak ≤ ≈ 1% and "slightly decreased", flexural multiple cracking lost (single crack) after 300 cycles, ASTM C666 B ([[yun2013-shcc-freeze-thaw]], Figs. 6, 8–9) | Material (PVA vs hybrid, W/B 0.45–0.55), procedure A vs B, ageing confounded (39 → 151 d); Yun's Fig. 9b (≤ 1%) vs Fig. 10 (≈ 2.5%) inconsistent | refinement → [[freeze-thaw]] |
| Flexural stiffness after 300 F-T cycles (minor) | Ascending branch steeper, lower deflection at peak (hybrid PVA + PE SHCC, ASTM C666 B; [[yun2013-shcc-freeze-thaw]], Fig. 5) | Larger mid-span deflection after 300 cycles ([[wang2023-ecc-frost-damage]]); lower stiffness (Sahmaran 2012, as cited by Yun, p. 15–16) | Material and procedure (B vs A), ageing confounded (39 → 151 d in Yun) | open → [[freeze-thaw]], [[flexural-strength]] |
| F-T durability factor of non-air-entrained concrete (as cited) | 20 (Li 2008, as cited in [[ma2021-ecc-durability-review]], p. 4) | 10 (Li et al. 2003, as cited in [[vanzijl2010-shcc-durability]], p. 267) | ECC/SHCC = 100 and concrete removed at 110 cycles in both; probably the same test reported differently | verify → [[freeze-thaw]] |
| Crack width of cementless AAS/EGC + PE composites | ≈ 89–110 µm computed average for AAS + 1.75% PE, no aggregate ([[choi2016-pe-alkali-activated-slag-composite]], Table 8); ECC norm < 100 µm ([[ma2021-ecc-durability-review]]) | **172–212 µm** computed average at peak for ED-EGC (171.8 / 199.3 µm, [[huy2023-egc-activator-pretreatment]], Table 5) and ED-AASC M1/M2 (212.0 / 204.0 µm, [[hieu2023-aas-extremely-ductile-22pct]], Table 6); the authors themselves note > 2× earlier composites | Much higher ε (11–22% vs ≤ 7.5%) at the same ≈ 1 mm spacing; weaker or rubberised matrices; all computed (elongation / crack count), loaded | open: very high ε is bought with crack width; ED-AASC M1/M2 exceed the 200 µm JC/T 2461 limit → [[crack-width]], [[alkali-activated-binder]] |
| Self-healing product | CaCO₃ is the main healing product (Raman/EDX/ESEM: [[homma2009-frcc-self-healing]]; [[ozbay2013-ecc-self-healing-sustained-load]]; [[yang2009-ecc-self-healing-wet-dry]]; [[lepech2009-ecc-water-permeability]]) | **C-(N)-A-S-H** gel (SEM/EDS ternary diagram) in a cementless GGBS/FA/SF geopolymer EGC ([[huy2023-egc-pe-pva-hybrid-healing]], Table 9, Fig. 15) | Binder chemistry (Portlandite and Ca supply vs residual alkali and unreacted precursors) | refinement: binder-dependent → [[self-healing]] |
| PE vs PVA for healing | Fine PE fibres promote CaCO₃ deposition; PE > hybrid > steel cord at equal width ([[homma2009-frcc-self-healing]], FRCC, cement) | PE-rich EGC healed **less** than PVA-rich EGC: crack healing rate 26.78 vs 31.40%, RF_r +15.63 vs +24.16 %-points ([[huy2023-egc-pe-pva-hybrid-healing]], Figs. 10, 12) | Matrix and product differ (cement/CaCO₃ vs geopolymer/C-(N)-A-S-H); hydrophilic PVA attracts products (authors); fibre count not compared | open → [[self-healing]], [[pe-fiber]], [[pva-fiber]] |
| Fly ash and healing | Higher FA/C (2.2 vs 1.2) → narrower cracks and better healing in PVA-ECC ([[ozbay2013-ecc-self-healing-sustained-load]], Tables 3–4) | FA-rich EGC (GGBS:FA 3:6.5) healed worst (crack healing rate 7.36 / 12.48%) and **lost** stiffness in water (RF_r −9.58 / −6.59 %-points) ([[huy2023-egc-pe-pva-hybrid-healing]], Figs. 10, 12) | Cement vs geopolymer; in EGC more FA also widened cracks (128–136 vs 83–100 µm) and made the matrix "chemically less stable" in water | open → [[fly-ash]], [[self-healing]] |
| Self-healing under freeze–thaw | ≈ 100% recovery at 0.5–1% pre-strain (Zhu 2012, as cited in [[ma2021-ecc-durability-review]], p. 5) | 20–30 µm cracks widened under coupled F-T + carbonation + 60 °C drying ([[chai2019-hdcc-freeze-thaw-carbonation-flexure]], §3.1) | Exposure type (drying, CO₂) | refinement → [[self-healing]] |
| Healing crack-width threshold | < 60 µm for fast permeability recovery (Reinhardt & Jooss, as cited in [[ma2021-ecc-durability-review]], p. 3) — this value is **not** from Yang 2009 | < 100 µm sealed by CaCO₃ in 28 d water, FRCC ([[homma2009-frcc-self-healing]], Fig. 6); 10–40 µm full, > 60 µm partial ([[ozbay2013-ecc-self-healing-sustained-load]], Fig. 7); < 50 µm full RF and permeability recovery, 50–150 µm partial, > 150 µm none after 10 wet–dry cycles, measured on a **0.5% PVA tension-softening mortar, not ECC** ([[yang2009-ecc-self-healing-wet-dry]], Figs. 4–5); (2026-10-26) the same bands — a few < 50 µm cracks fully healed, 50–150 µm partly or little — observed in a strain-hardening cementless EGC ([[huy2023-egc-pe-pva-hybrid-healing]], Fig. 9) | Different measures (permeability time vs crystal thickness vs stiffness vs RF) and materials | refinement → [[self-healing]], [[crack-width]] |
| Static immersion vs flowing water for healing | No visible healing after 14 d static water saturation; healing after ≈ 3 d of flowing water; partly submerged specimens healed only near the water line ([[lepech2009-ecc-water-permeability]], p. 752) | Healing in plain water immersion over 28–90 d ([[homma2009-frcc-self-healing]]; [[ozbay2013-ecc-self-healing-sustained-load]]) | Carbonate/bicarbonate supply; duration (14 d vs 28–90 d); water renewal not reported in B | open → [[self-healing]] |
| "PE heals poorly" (earlier wiki synthesis) | PE-HSHDC 80–200 µm cracks lie above the healing range (earlier wiki synthesis) | Fine PE fibers promote CaCO₃ deposition at equal width; partial healing above 100 µm ([[homma2009-frcc-self-healing]], FRCC, not SH) | The limitation is crack width, not PE | resolved for cement-based matrices: a crack-width issue → [[self-healing]]; see the new row "PE vs PVA for healing" for geopolymer EGC |
| Self-healing vs age | Declines with age (pozzolanic reaction) ([[ma2021-ecc-durability-review]], p. 9) | Recovery rose over 12 months outdoors: stiffness 62 → ≈ 116% (0.5% pre-strain) and ≈ 36 → ≈ 150% (1.0%) from 3 to 12 months ([[herbert2013-ecc-self-healing-natural-environment]], Fig. 6a, p. 2840, read; cracked at 7 d; hydration alone raised control RF to ≈ 112–119%, Fig. 3); ECC M45 cracked at ≈ 6 months still recovered 87–100% RF under CR1 ([[yang2009-ecc-self-healing-wet-dry]], Fig. 7) | Age at cracking; late-age (> 6 months) cracking untested | refinement: weakens "declines with age" up to 6 months |
| Sulfate + dry–wet trend of HDC | "rises to 30 cycles, falls after 105" ([[he2024-hdc-research-advances]]) | holds for 5% Na₂SO₄ only; 10% peaks at 105; saturated **falls after 30** (49.2 MPa at 30 → 44.6 MPa at 60 cycles, below the initial 45.8 MPa) ([[li2021-hdc-sulfate-dry-wet]], Table 4, p. 6); loss-rate δ definition confirmed by Fig. 2 (p. 7) | Review simplified the primary data | refinement (the wiki's earlier "falls from 60" corrected 2026-10-21) |
| Shrinkage vs W/B (as cited) | rises with W/B (Gao 2018) | falls with W/B (Ye 2019), both in [[ma2021-ecc-durability-review]] | Strength class | open |
| **Temperature** | | | | |
| Temperature effect on HDC (−30 to 60 °C) | PVA-HDC (residual, 8 h): σ_tu and f_cu rise from −30 to 60 °C, flexural strength 14.08 → 15.64 MPa, ε_tu (at peak, Fig. 1, p. 2) peaks at 0 °C ([[chai2023-hdc-ambient-temperature]]) | PE-HDC (Dong 2022, as cited there): f'c and σ_tu fall, ε_tu rises steadily; hot (in-situ) PVA-ECC bending peak load falls from 20 to 60 °C while deflection capacity rises ≈ 3× ([[pourfalah2018-ecc-high-temperature]], Fig. 10) | Fiber type, residual vs in-situ testing | open: data support "in-situ strength falls, residual rises" → [[high-temperature-behaviour]], [[flexural-strength]] |
| f'c of PVA-ECC at 400–600 °C | Residual f'c rises at 400 °C (84.2 vs 72.7 MPa at 200 °C), HSECC W/B 0.20 ([[zhou2023-hsecc-elevated-temperature]], Table 5) | Residual drops 34% between 400 and 500 °C, CR-ECC 0% CR (≈ 69 → 45 MPa; ≈ 75 MPa at 24 °C, ≈ 16 MPa at 1000 °C; CR mixes ≈ 11–13 MPa at 1000 °C) ([[mohammed2020-cr-ecc-elevated-temperature]], Fig. 3, p. 7, read); **hot** f'c −10% at 400 °C, −25% at 600 °C (38.8 → 35.1 → 29.2 MPa) ([[pourfalah2018-ecc-high-temperature]], Table 5) | Matrix strength, temperature steps, hot vs residual testing | minor, open → [[high-temperature-behaviour]] |
| Hybrid steel + polymer at high temperature | Steel raises residual f_f above 400 °C (PS-II 6.6 vs PO 2.1 MPa at 800 °C) ([[zhou2023-hsecc-elevated-temperature]], Table 5); PVA + 0.75% steel HECC: no spalling to 600 °C, debris 8.5% vs 30% for ECC, ≈ 2× hot bending load ([[pourfalah2018-ecc-high-temperature]], Fig. 7b) | Same Zhou paper: steel brings spalling at 800 °C and thermal cracks up to 271 µm vs ≤ 19.6 µm without | Trade-off within one study; temperature range (≤ 600 vs 800 °C). The wiki's old "4× debris vs steel-fiber ECC" was second-hand and imprecise (≈ 3.5×, vs a hybrid) | note → [[hybrid-fiber]] |
| PVA melting point | 230 °C onset by TG, instability 220–420 °C ([[zhou2023-hsecc-elevated-temperature]], Fig. 4) | Decomposition 263 °C (as cited in [[vanzijl2010-shcc-durability]], p. 266); 235 / 250 °C (as cited in Zhou 2023); old wiki "230–273 °C ⚠️" | Onset vs decomposition; 273 °C not supported by any ingested source | partly resolved: use 230 °C onset → [[pva-fiber]], [[high-temperature-behaviour]] |
| PVA state at 200 °C (minor) | "Burned" at 200 °C in a hot test; full pull-out from 150 °C ([[pourfalah2018-ecc-high-temperature]], Fig. 12) | TG melting onset 230 °C ([[zhou2023-hsecc-elevated-temperature]], Fig. 4) | In-situ vs residual; visual vs TG | minor → [[high-temperature-behaviour]] |
| PE fiber melting point | about 150 °C ([[ranade2017-hshdc-impact-resistance]]; [[yu2018-ecc-direct-tensile-review]]) | 124–138 °C ([[he2024-hdc-research-advances]]); 135–145 °C ([[su2023-rubber-modified-hshdc]]) | Different products | minor |
| **Structures, interfaces & printing** | | | | |
| ECC overlays / repairs and delamination | ECC repairs avoid delamination (Lim & Li 1997, as cited in [[li2003-ecc-review]], p. 225) | All 40 mm sprayed layers debonded ([[wang2019-rc-beam-ecc-shear-strengthening]]); 10 / 30 mm SHCC layers debonded (as cited in [[xue2023-shcc-structural-review]]); chiselled NSHSDC jackets did not ([[yuan2020-nshsdc-beam-strengthening]]) | Shrinkage-driven repair vs structural loading; thickness; surface roughness | open → [[interface-bond]] |
| Thickness of strengthening layers | Thicker SHCC layers give more gain and less delamination: 50 mm +61% (as cited in [[xue2023-shcc-structural-review]]) | 40 mm sprayed ECC no better than 20 mm at a/d 3, worse in SA-40-2; all 40 mm layers debonded ([[wang2019-rc-beam-ecc-shear-strengthening]], Table 3) | Cast vs sprayed, interface preparation, shear vs flexure, over-strengthening | open → [[rc-member-strengthening]] |
| Code conservatism for HDC shear members | GB 50010 1.08–1.26; ACI 318-05 1.40–2.08 (columns, [[deng2018-hdc-short-columns]], Table 7) | ACI 318-14 2.0–5.3 (up to 12.88 for deep beams); EN 1992 1.8–4.0 (beams, [[li2021-hdc-beam-shear]], Tables 6–7) | Member type, a/d, code editions; not a true contradiction | note → [[shear-behaviour]] |
| Shear design philosophy for HDC | Composite σ_t as an explicit truss tie, empirical η ([[wang2019-rc-beam-ecc-shear-strengthening]]) | Empirical (f_t/f_c) ratio η and a/d function δ, no σ–ε law ([[li2021-hdc-beam-shear]], Eqs. 6–9); σ_tu × overlay area for masonry ([[deng2019-urm-shaking-table-hdc]]; [[deng2020-aac-wall-hdc-retrofit]]) | Different members and databases | open → [[shear-behaviour]] |
| Interlayer strength of printed SHCC | Interface ≥ bulk first-crack strength ("comparable to or slightly more", §3.5; "in the same range", p. 20), lowest void content; interlayer bond ≈ 1.2–2.4 MPa ([[chavesfigueiredo2020-printed-shcc]], Fig. 14, p. 16, read) | Flexure across the interlayer lower (18.5 vs 22.0 MPa) ([[ivaniuk2022-printable-shcc-design]], Table 3); Wolfs 2019 and Feng 2015 weaker (as cited there) | Mix, fiber (PVA vs PE), nozzle, test (direct tension vs 3PB) | open → [[3d-printed-hdc]] |
| "Deng & Zhang 2018" column study | HDC **jacketing** of cross-shaped short columns (as cited in [[he2024-hdc-research-advances]], p. 6) | Whole-HDC **square** short columns, no jacketing ([[deng2018-hdc-short-columns]]); [[deng2017-rc-column-hdc-jacket]] is a jacketing study but 2017, square columns, shear-span ratio 3 | Very likely a **different, not-ingested paper**: Deng M, Zhang Y, Li Q. "Shear strengthening of RC short columns with ECC jacket: cyclic behavior tests", Eng. Struct. 2018;160:535–45 (ref. [17] in [[deng2019-urm-shaking-table-hdc]]; ref. [20] in [[deng2020-aac-wall-hdc-retrofit]]); not a mis-citation | **probably resolved**: obtain the Eng. Struct. 160 paper to confirm "cross-shaped" → [[rc-member-strengthening]] |
| "Yuan 2020" beam strengthening | "steel wire plus ECC" ([[he2024-hdc-research-advances]], p. 19–20) | No-slump steel-fiber + PE NSHSDC jackets ([[yuan2020-nshsdc-beam-strengthening]]) | Another Yuan 2020 or mis-description | verify |
| **Internal inconsistencies of single sources (found in the 2026-10-21 PDF re-ingest; one row added 2026-10-26)** | | | | |
| Acid resistance of CR-PVA "ECC" | Text: slight weight **gain** after acid exposure ([[mohammed2020-cr-ecc-elevated-temperature]], text) | Same paper's Fig. 8 (p. 10): weight **loss** of 0.2–7.3% at 28 d in 12 of 13 mixes; only M4 (5% CR, 2% PVA) gains ≈ 0.15% (read); Table 5 weight-loss mean −3.11 vs positive bars | Text vs figure; sign convention of Table 5 | open: cite Fig. 8, not the text → [[durability]], [[crumb-rubber]] |
| Carbonation effect on 0.1–10 µm pores | Text: 0.1–10 µm porosity reduced "more than 2×" by carbonation ([[zhang2022-ecc-carbonation-sustained-load]], p. 10) | Same paper's Fig. 10a (p. 11): ≈ 3.4 → 2.5%, i.e. ≈ 1.4× in zone I (read); also sustained loads 4.11 / 8.22 kN vs 0.3 / 0.6 × 9.51 kN = 2.85 / 5.71 kN (p. 3, computed) | Text vs figure; load basis unclear | open → [[carbonation]], [[permeability]] |
| FA level for frost resistance | Text: PF and UF cycle counts show an "obvious rise" again at FA 0.525 ([[zhong2019-ecc-freeze-thaw]], p. 16) | Same paper's Fig. 16c–d: level A4 (0.525) lies **below** A3 and above only A2 and A5 | Text over-states the figure | open: the ≈ 35% optimum stands; the second rise is not supported → [[freeze-thaw]], [[fly-ash]] |
| Units of PE-ECC flexural loads | Table 4, Fig. 8 and Fig. 10 print "kN" ([[shumuye2022-slag-fa-pe-ecc]], pp. 8–12) | With span 240 mm and section 60 × 13 mm (Fig. 2a, p. 5), N gives σ ≈ 14–20 MPa; kN gives ≈ 14,000–20,000 MPa (computed) | Unit error in the paper (loads almost certainly in N) | ⚠️ open: use only as N, flagged → [[flexural-strength]] |
| Damage-model constants (V3R2) | Table 4 prints B −0.090, C 0.108 for V3R2 ([[zhao2022-ecc-tension-damage-model]], p. 10) | Recomputing Eqs. 13–15 from the Table 3 means gives −0.171, 0.172; all other rows reproduce to 3 decimals (σ in MPa, ε in %) | Copy error (printed B equals V3R3's) | minor, open → [[tensile-constitutive-model]] |
| PE-SHCC strain of mix B2 (review) | Text: 2.2% at 8 MPa ([[xue2023-shcc-structural-review]], p. 3) | Same paper's Fig. 1: B2 marker at ≈ 2.6% / ≈ 7.7 MPa (read); Figs. 3 and 9 drawings show one central load while the text says four-point bending | Text vs figure; strain basis (peak vs ultimate) not stated | minor, open → [[tensile-strain-capacity]] |
| Hysteretic energy of the FE URM wall | 1.52 × 10⁷ J (URM) and 4.74 × 10⁷ J reported ([[tabrizikahou2022-masonry-ecc-sma-retrofit]], p. 20) | The loading history of Fig. 1b (amplitudes ≤ 15 mm, cumulative ≈ 0.37 m) with the URM peak force 72.7 kN (Fig. 25) allows ≈ 3 × 10⁴ J at most, ≈ 500× less (computed); "+116/117%" means ≈ 117% **of** (≈ +17%) | Unit or scaling error; ratios between models still usable | open: use only energy ratios → [[masonry-wall-retrofit]] |
| Decline of chloride diffusivity with age | Text: D falls ≈ 5% from 90 to 120 d ([[bu2022-ecc-chloride-crack-width]], p. 8) | Same paper's Fig. 7: ≈ 20–25% (90 → 120 d) and ≈ 45–60% (30 → 60 d) (read); the ageing exponent n 1.57–1.89 (Fig. 8, p. 9) is unusually high | Text vs figure; short exposure (concrete age 58–148 d) | minor, open → [[chloride-and-corrosion]] |
| Ohno & Li 2014 FA-EGC strain | 4.3% (text, §1, of [[huy2023-egc-activator-pretreatment]]; also [[choi2016-pe-alkali-activated-slag-composite]], §1; [[hieu2023-aas-extremely-ductile-22pct]], §1) | 3.40% plotted in Fig. 11 of [[huy2023-egc-activator-pretreatment]] and used for its "5.4×" ratio | Fig. 11 probably plots σ_tu (3.4 MPa) as ε | open: use 4.3% (as cited) → [[alkali-activated-binder]] |
| Post-impact EMI shielding loss vs skin thickness | Earlier wiki reading: ≈ 7.1% for 20 mm HSDC vs 24.7% for thinner (5–10 mm) skins | PDF: 7.1% ≈ H20S (single 20 mm) and 24.7% = H20D (double 20 mm); thinner skins lost more: H5S ≈ 44%, H5D ≈ 28%, H10D ≈ 26%, H10S ≈ 16%; full HSDC panel ≈ 8% ([[lee2021-hsdc-wall-emi-impact]], Fig. 12, p. 12, read). Blow counts still differ between the text and Figs. 8, 11, 12 | The wiki misread the XML text (no figures) | **resolved** 2026-10-21 → [[extreme-loading-applications]], [[impact-resistance]] |

## Under-studied areas
Updated for the 63-source corpus (2026-10-26, round 7).

**Durability**
- **Tension after exposure.** Primary durability data exist for freeze–thaw ([[wang2023-ecc-frost-damage]];
  [[zhong2019-ecc-freeze-thaw]]; [[chai2019-hdcc-freeze-thaw-carbonation-flexure]]; [[yun2013-shcc-freeze-thaw]]),
  carbonation ([[zhang2022-ecc-carbonation-sustained-load]]), chloride ([[bu2022-ecc-chloride-crack-width]];
  [[paul2014-r-shcc-chloride-corrosion]]), permeability ([[lepech2009-ecc-water-permeability]]), sulfate
  ([[li2021-hdc-sulfate-dry-wet]]) and fire ([[zhou2023-hsecc-elevated-temperature]];
  [[mohammed2020-cr-ecc-elevated-temperature]]; [[pourfalah2018-ecc-high-temperature]]). Only **one** primary study now
  measures uniaxial tension after exposure ([[yun2013-shcc-freeze-thaw]]), and only for **hybrid PVA + PE** SHCC with
  2 dumbbells per point; uniaxial tension after F-T for PVA-only ECC/HDC is missing (Yun 2011, Cold Reg. Sci. Technol.
  67:49–57, should be obtained). Several "ECC" durability papers never demonstrate strain hardening (Zhong 2019,
  Zhang 2022, Bu 2022, Zhou 2023, Mohammed 2020). → [[durability]], [[freeze-thaw]]
- **Durability of HSHDC/UHDC and alkali-activated SHCC** is still missing: every primary durability study uses
  normal-strength PVA-ECC/HDCC (or hybrid PVA + PE). Reviews flag the same gap ([[ma2021-ecc-durability-review]],
  p. 9–10). No durability, shrinkage or carbonation data exist for the cementless PE/AAS composites
  ([[choi2016-pe-alkali-activated-slag-composite]], §3.3; [[hieu2023-aas-extremely-ductile-22pct]]; [[huy2023-egc-activator-pretreatment]]).
  The only alkali-activated durability-type data are water healing of HSUD-EGC, which was **limited** (crack healing rate
  7.4–31.4%) ([[huy2023-egc-pe-pva-hybrid-healing]]). → [[durability]], [[hshdc]], [[alkali-activated-binder]]
- **Record strains with wide cracks.** The two highest strains in the wiki (22.34% and 18.62% at peak) come with
  computed average crack widths of ≈ 200 µm ([[hieu2023-aas-extremely-ductile-22pct]]; [[huy2023-egc-activator-pretreatment]]).
  Crack-width control at very high ε, the durability of such cracks, and whether these strains survive in thick members
  (all data from 13 mm dumbbells, one lab) are untested. → [[crack-width]], [[tensile-strain-capacity]]
- **Tolerable crack width per exposure.** Thresholds depend on transport mode: under immersion 100 µm ≈ uncracked
  ([[bu2022-ecc-chloride-crack-width]]); under wet–dry cycles even 22–38 µm average cracks let chloride reach steel
  ([[paul2014-r-shcc-chloride-corrosion]]). Durability thresholds use residual average widths, yet maximum widths in
  PVA-SHCC reach 290–420 µm at 3% strain ([[vanzijl2010-shcc-durability]]) and loaded widths are ≈ 2× residual under
  sustained flexure ([[ozbay2013-ecc-self-healing-sustained-load]]). Limit strains, crack-width distributions and
  time-dependent widths under sustained load are needed for service-life design ([[vanzijl2010-shcc-durability]],
  p. 263–269). → [[crack-width]], [[chloride-and-corrosion]]
- **Permeability:** the "100 µm" threshold is a design target from concrete (Wang 1997), never measured on ECC; ECC
  permeability is known only for 50–63 µm cracks, so the 63–100 µm range is untested. Absorption and diffusion are not
  studied together with permeation, and service-life models (e.g. Life-365) assume uncracked concrete
  ([[lepech2009-ecc-water-permeability]]). Lepech & Li 2005 (cited for the threshold by [[vanzijl2010-shcc-durability]])
  should be obtained. → [[permeability]]
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
- **Self-healing under service load, repeated damage, temperature and water supply:** unloaded tests overestimate
  healing ([[ozbay2013-ecc-self-healing-sustained-load]]); 100% recovery after repeated damage is not reached
  ([[herbert2013-ecc-self-healing-natural-environment]]); hot drying (55 °C) reduces healing
  ([[yang2009-ecc-self-healing-wet-dry]]); healing appears under flowing but not static water, so carbonate supply may
  limit it ([[lepech2009-ecc-water-permeability]]). The healing crack-width limits of [[yang2009-ecc-self-healing-wet-dry]]
  come from a tension-softening mortar and are not yet confirmed on ECC. → [[self-healing]]
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
- **No fire design data and no in-situ (hot) tension data** for HDC. The first primary hot tests on ECC cover
  compression and bending only: bending ductility is lost from about 150 °C and PVA-ECC becomes brittle from 200 °C,
  while PVA + steel HECC stays softening-ductile to 600 °C ([[pourfalah2018-ecc-high-temperature]]). HECC under fire
  had not been studied before (§1 there). PE-ECC loses strain hardening between 100 and 140 °C (reviews, see
  [[high-temperature-behaviour]]); PVA melts from 230 °C ([[zhou2023-hsecc-elevated-temperature]], Fig. 4). Steel-fiber
  hybrids raise residual strength but re-introduce spalling at 800 °C ([[zhou2023-hsecc-elevated-temperature]]).
  → [[high-temperature-behaviour]], [[hybrid-fiber]]

**Chinese HDC and the XAUAT (Deng) group**
- Eight papers from or with the Deng (XAUAT) group are now ingested: materials ([[deng2015-hdc-compressive-toughness]];
  [[deng2018-hdc-compressive-constitutive]]; [[zhang2022-hdc-basalt-textile-tension]]) and members
  ([[deng2017-rc-column-hdc-jacket]]; [[deng2018-hdc-short-columns]]; [[deng2019-urm-shaking-table-hdc]];
  [[deng2020-aac-wall-hdc-retrofit]]; [[li2021-hdc-beam-shear]]). The Deng 2019 shake-table test is now primary.
  The material sections still report little on curing and on the dogbone geometry, gauge and rate.
  → [[masonry-wall-retrofit]], [[heat-curing]]
- **Strain capacity of the "same" XAUAT PVA-HDC** ranges from ≈ 3.0% to ≈ 1.0% and, in a modified matrix, 0.34–0.45%
  (⚔️ row above). Chinese vs Japanese PVA is the only controlled comparison ([[deng2017-rc-column-hdc-jacket]]).
  The Shaanxi HDC standard **DBJ61/T112-2016** (XAUAT tension method; predates JC/T 2461-2018), cited in
  [[deng2019-urm-shaking-table-hdc]], ref. [20], should be obtained. → [[tensile-strain-capacity]], [[dogbone-uniaxial-tension]]
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
  (cited in [[chai2023-hdc-ambient-temperature]]) and DBJ61/T112-2016 are still not ingested. Already an R&D need in 2003
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
- **Interface data** (pull-out) exist only for Michigan PE-HSHDC and Michigan PVA-ECC. Bond claims for Chinese HDC rest on
  SEM only ([[gao2020-hdcc-recycled-fine-aggregate]]; [[shumuye2022-slag-fa-pe-ecc]]; [[wang2023-ecc-frost-damage]]).
  → [[fiber-matrix-interface]]
- **Curing regime:** its effect on PSH indices and ductility is unclear ([[zhang2022-hshdcc-review]]). All three 2023 CNU
  cementless composites use 80–100 °C heat steps without an ambient control ([[hieu2023-aas-extremely-ductile-22pct]];
  [[huy2023-egc-activator-pretreatment]]; [[huy2023-egc-pe-pva-hybrid-healing]]). → [[heat-curing]]
- **Processing (mixing procedure):** mixing alone changed ε 9.81 → 22.34% at identical proportions
  ([[hieu2023-aas-extremely-ductile-22pct]]), but dispersion was not measured and no other source records mixing energy.
  → [[fiber-dispersion]]
- **Micromechanics of alkali-activated / geopolymer composites:** one source measures Km, σ0 and J′b (fly-ash ED-EGC,
  [[huy2023-egc-activator-pretreatment]]); no τ0/Gd pull-out data and no Km for AAS or GGBS/FA EGC exist.
  → [[micromechanical-parameters]], [[fiber-matrix-interface]]
- **FA optimum depends on the property:** ductility peaks near FA/C ≈ 3 ([[jin2019-hvfa-shcc-structural]]), frost
  resistance near 35% replacement ([[zhong2019-ecc-freeze-thaw]]; its claimed second rise at 52.5% is not borne out by
  Fig. 16); no study optimises both. → [[fly-ash]]
- **Slag:** no source measures its effect on PSH indices or bond in cement-based ECC; slag widens cracks (qualitative,
  [[shumuye2022-slag-fa-pe-ecc]]). Cementless alkali-activated slag + PE reaches 7.50% ([[choi2016-pe-alkali-activated-slag-composite]]),
  but its physical, chemical and rheological behaviour still needs study (§3.3 there). Later cementless slag composites reach
  22.34% ([[hieu2023-aas-extremely-ductile-22pct]]) and, with FA, 84.3 MPa at 10.51% ([[huy2023-egc-pe-pva-hybrid-healing]]); all four
  alkali-activated sources come from one group (Chonnam National University). → [[ggbfs]], [[alkali-activated-binder]]
- **Crumb rubber:** only one source with tension data in which rubber is varied ([[su2023-rubber-modified-hshdc]]);
  [[hieu2023-aas-extremely-ductile-22pct]] uses 5% CR at a fixed dose; [[mohammed2020-cr-ecc-elevated-temperature]]
  is compression-only. → [[crumb-rubber]]
- **VMA dosage** (HPMC, cellulose, starch ether) is never varied against ε_tu ([[ivaniuk2022-printable-shcc-design]]).
  → [[viscosity-modifying-admixtures]]

**Structures and applications**
- **Structural data are now largely primary:** beam shear strengthening ([[wang2019-rc-beam-ecc-shear-strengthening]];
  [[yuan2020-nshsdc-beam-strengthening]]), RC column jackets ([[deng2017-rc-column-hdc-jacket]]), whole-HDC short columns
  ([[deng2018-hdc-short-columns]]) and beams with stirrups ([[li2021-hdc-beam-shear]]), masonry retrofit by shake table
  ([[deng2019-urm-shaking-table-hdc]]) and in-plane cyclic tests ([[deng2020-aac-wall-hdc-retrofit]]), reinforced UHP-SHCC
  members ([[kunieda2010-uhp-shcc-steel-reinforcement]]), TR-HDC in tension ([[zhang2022-hdc-basalt-textile-tension]]) and
  HSDC-skinned panels under impact ([[lee2021-hsdc-wall-emi-impact]]). → [[rc-member-strengthening]], [[masonry-wall-retrofit]]
- **Masonry:** no virgin-specimen comparison of HDC vs other overlays on identical walls (the shake table re-tested one
  damaged model; retrofit areas unequal); no bond test of HDC on brick or AAC; no overlay crack widths; no out-of-plane test
  with HDC; serious-damage and near-collapse drift limits for HDC-overlaid masonry undetermined
  ([[deng2019-urm-shaking-table-hdc]]; [[deng2020-aac-wall-hdc-retrofit]]). → [[masonry-wall-retrofit]]
- **Column jackets:** one specimen per case, unequal axial load between controls and jacketed columns, no jacket-thickness
  variation, no crack widths, jacket–concrete bond untested ([[deng2017-rc-column-hdc-jacket]]). → [[rc-member-strengthening]]
- **HDC beams:** a larger database is needed to fix trends with a/d, ρ and ρ_sv; highly reinforced HDC members are little
  studied ([[li2021-hdc-beam-shear]], §1, §4.2). → [[unreinforced-hdc-structures]], [[shear-behaviour]]
- **TR-HDC:** no member test; the empirical α and σ–ε model are limited to 25 mm basalt grids; no yarn pull-out in HDC; no
  durability data ([[zhang2022-hdc-basalt-textile-tension]]). → [[textile-reinforced-hdc]]
- **Shear design of HDC members:** RC code formulas are conservative by different margins (⚔️ row "Code conservatism");
  ECC softening coefficient under tension–compression unmeasured ([[wang2019-rc-beam-ecc-shear-strengthening]], Sect. 4.4);
  no shear tests on PE-HSHDC members. → [[shear-behaviour]]
- **Bond to existing concrete and masonry:** slant-shear data exist for one Korean steel + PE mix at 28 d
  ([[yuan2020-nshsdc-beam-strengthening]], Table 7). All XAUAT structural studies (columns, brick, AAC) report bond only
  visually; no pull-off or direct-shear tests of PVA-HDC/ECC on concrete, brick or AAC exist; on AAC the substrate, not the
  interface, limits bond ([[deng2020-aac-wall-hdc-retrofit]]). Layer thickness and roughness are never varied together;
  the FE interface law changes dissipated energy about 2× ([[tabrizikahou2022-masonry-ecc-sma-retrofit]], Table 8; absolute
  energies there are ≈ 500× too large, ⚔️ row above, so only the ratio is usable).
  A rebar bond-slip law for ECC/HDC is missing ([[wang2023-ecc-frost-damage]], §1). → [[interface-bond]]
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
- Round 5 closed the ScienceDirect gap: 9 papers were downloaded by hand, and Wang 2007 (ACI, paywalled) was replaced by
  Choi 2016 (see [[log]], 2026-10-21).
- Cited but not ingested: Kanda & Li 1998, JSCE 2008, JC/T 2461-2018, DBJ61/T112-2016, Lepech & Li 2005, Yun 2011
  (Cold Reg. Sci. Technol. 67:49–57) and Deng, Zhang & Li 2018 (Eng. Struct. 160:535–45).

## Open questions
- Do the > 18% strains of cementless PE composites survive in thicker specimens and without heat curing, and can their
  ≈ 200 µm cracks be narrowed without losing ductility ([[hieu2023-aas-extremely-ductile-22pct]]; [[huy2023-egc-activator-pretreatment]])?
- Which activator and precursor mix gives effective self-healing in EGC, given limited healing with sodium silicate and
  negative stiffness recovery in FA-rich mixes ([[huy2023-egc-pe-pva-hybrid-healing]])?
- Can PSH indices be extended to include embedment length and flaw size (as in Li & Leung 1992)?
- Can PE-HSHDC crack widths be brought below 60–80 µm, e.g. with hybrid steel, SF or rubber, to gain
  self-healing and chloride resistance — and does that matter under immersion, where 100 µm ≈ uncracked?
- Does ambient-cured HSHDC keep its ductility after long-term ageing?
- Why does PVA-SHCC switch back to fiber pull-out above 10 s⁻¹ ([[mechtcherine2011-shcc-high-strain-rate]])?
- Does recycled fine aggregate raise ductility through bond or through flaws ([[gao2020-hdcc-recycled-fine-aggregate]])?
- What minimum reinforcement ratio secures dogbone-level ductility in thick members
  ([[kunieda2010-uhp-shcc-steel-reinforcement]])?
- Why does the nominally identical XAUAT PVA-HDC give ≈ 1% in most papers but ≈ 3% in [[deng2017-rc-column-hdc-jacket]]:
  fibre grade, batch, or strain basis?
- Do the healing crack-width limits from tension-softening mortar (< 50 µm full, > 150 µm none;
  [[yang2009-ecc-self-healing-wet-dry]]) hold for multiple-cracking ECC? (Partly observed in a cementless strain-hardening
  EGC, [[huy2023-egc-pe-pva-hybrid-healing]], Fig. 9; still untested on cement-based ECC.)
