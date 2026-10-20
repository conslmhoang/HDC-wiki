---
type: hub
updated: 2026-10-20
---

# Research Gaps, Conflicts & Open Questions

This page feeds the "Research gaps and future directions" chapter of [[review-outline]].

## ⚔️ Conflicts between sources
| Topic | Source A says | Source B says | Possible reason | Status |
|---|---|---|---|---|
| Meaning of "HDC" / "HSHDC" | HSHDC = Michigan PE + VHSC matrix, 166 MPa, heat-cured ([[ranade2017-hshdc-impact-resistance]]) | HSHDC = Xi'an ambient-cured, about 100 MPa ([[yang2024-hshdc-uniaxial-tension]]); GDUT ([[su2023-rubber-modified-hshdc]]); umbrella HSHDCC > 100 MPa and > 3% ([[zhang2022-hshdcc-review]]) | Same name used by different groups | open: always state the lineage, see [[terminology-hdc-ecc-shcc]] |
| Class thresholds | HSHDCC: > 100 MPa, > 3% ([[zhang2022-hshdcc-review]]) | > 55 MPa and > 4%, or > 80 MPa and > 2% (other reviews, as cited there); normal HDC 30–80 MPa ([[su2023-rubber-modified-hshdc]]) vs normal ECC 40–70 MPa ([[zhang2022-hshdcc-review]]) | Chinese standard JC/T 2461-2018 sets only ≥ 0.5% and ≤ 200 µm (as cited in [[chai2023-hdc-ambient-temperature]]) | open: two bars, ECC convention vs HDC standard |
| HDC vs ECC | "HDC stands for ECC" (p. 2) | "HDC developed on the basis of ECC" (p. 10), both in [[he2024-hdc-research-advances]] | Internal inconsistency | treat HDC ≈ ECC/SHCC |
| Quasi-static ε_tu of Michigan HSHDC | 3.4% (as quoted in [[ranade2017-hshdc-impact-resistance]]) | 4.2% ([[ranade2015-hshdc-tensile-rate-effects]]); 3.5% for the 2011 version ([[zhang2022-hshdcc-review]]) | Batch and fiber version (38 vs 28 µm) | open: report 3.4–4.2% |
| Strength–ductility trade-off | ε_tu falls as f'c rises across the primary sources (UHDC 9.45% → Michigan 3.4–4.2%) | f'c > 210 MPa with ε > 5%, and 122 MPa with 8.5% (as cited in [[zhang2022-hshdcc-review]]) | Interface and fiber design, not f'c alone | resolved: the trade-off is **not fundamental** |
| PSH thresholds | "> 1.2 and > 3" quoted for all fibers (Su 2023, Ranade 2015, Zhang 2022) | 1.2 / 3 apply to pull-out type; fiber-rupture type needs > 1.3 and > 2.7 ([[kanda2006-psh-design-criteria]], p. 69–70) | Papers quote the 1998 set | resolved: check which set applies |
| PSH criteria vs behaviour | 6 mm PE mixes meet the 1998 thresholds but fail brittle ([[su2023-rubber-modified-hshdc]]) | In PVA-ECC the energy index (> 3) predicts saturation well ([[li2002-pva-ecc-interface-tailoring]]) | PE6 fails the 2006 strength threshold (1.2 < 1.3); flaw-size and embedment terms missing ([[li1992-steady-state-multiple-cracking]]) | partly resolved |
| Does the stress index separate ductile from brittle PVA mixes? | no: 1.5–1.8 for all ([[li2002-pva-ecc-interface-tailoring]]) | yes: 1.14–1.16 → 0.3–0.6%, 1.31–1.32 → 1.0–1.5% ([[kanda2006-psh-design-criteria]]) | different matrices (mortar vs paste) | open |
| β of oiled PVA | 0.58–0.63 in the M45 fly-ash matrix ([[yang2008-ecc-fiber-bridging-law]]) | 1.15 in a w/c 0.45 matrix without fly ash ([[li2002-pva-ecc-interface-tailoring]]) | Matrix and fly ash | resolved: matrix-dependent |
| Temperature effect on HDC | PVA-HDC (residual, 8 h): σ_tu and f_cu rise from −30 to 60 °C, ε_tu peaks at 0 °C ([[chai2023-hdc-ambient-temperature]]) | PE-HDC (Dong 2022, as cited there): f'c and σ_tu fall, ε_tu rises steadily | Fiber type, residual vs in-situ testing | open |
| "PVA-ECC σ_tu 3–8 MPa" | attributed to Li 2003 in [[yu2018-ecc-direct-tensile-review]] | not in [[li2003-ecc-review]] (only ε ≈ 5%) | Probably another Li 2003 paper | verify |
| Sulfate + dry–wet trend of HDC | "rises to 30 cycles, falls after 105" ([[he2024-hdc-research-advances]]) | holds for 5% Na₂SO₄ only; 10% peaks at 105, saturated falls from 60 ([[li2021-hdc-sulfate-dry-wet]], Table 4) | Review simplified the primary data | refinement |
| PVA-ECC ε vs strain rate (as cited) | decreases (Yang & Li 2014; Mechtcherine) | no significant change (Boshoff & van Zijl 2007), both in [[yu2018-ecc-direct-tensile-review]] | Test method and rate range | open |
| PVA failure mode at high rate (as cited) | pull-out dominates in composite tests | rupture dominates in single-fiber tests ([[yu2018-ecc-direct-tensile-review]], p. 350) | Scale effect | open |
| Shrinkage vs W/B (as cited) | rises with W/B (Gao 2018) | falls with W/B (Ye 2019), both in [[ma2021-ecc-durability-review]] | Strength class | open |
| Freeze–thaw citation | Yun 2013, hybrid PVA+PE ([[he2024-hdc-research-advances]]) | Yun 2011, PVA loses more ε than PE ([[ma2021-ecc-durability-review]]) | Possibly two papers or a mis-citation | verify |
| PE fiber melting point | about 150 °C ([[ranade2017-hshdc-impact-resistance]]; [[yu2018-ecc-direct-tensile-review]]) | 124–138 °C ([[he2024-hdc-research-advances]]); 135–145 °C ([[su2023-rubber-modified-hshdc]]) | Different products | minor |
| PVA fiber length effect (as cited) | longer gives lower ductility (Feng 2022) | 18 mm better than 12 mm (Lee 2023), both in [[su2023-rubber-modified-hshdc]] | Matrix and test | open |
| UHPC flexural size effect (as cited) | significant | reduced, both in [[ye2021-uhdc-flexural-size-effect]] | Size range and method | open |

## Under-studied areas
- **Durability of HSHDC/UHDC.** All durability data concern normal ECC or PVA-HDC. Reviews explicitly flag that
  high-strength / high-ductility ECC lacks data ([[ma2021-ecc-durability-review]], p. 9–10). The one primary
  HDC durability study tests compression only, never tension or crack width ([[li2021-hdc-sulfate-dry-wet]]).
  → [[durability]]
- **Crack width of PE-based HSHDC** (80–200 µm) exceeds the thresholds for chloride (55–90 µm) and
  fast self-healing (< 60 µm). PVA-ECC (43–88 µm) does not. → [[crack-width]], [[self-healing]]
- **Fire:** PE-ECC loses strain hardening between 100 and 140 °C; PVA-ECC at about 150–200 °C. No fire design data. → [[high-temperature-behaviour]]
- **Chinese PVA-HDC primary data** now exist from Southeast/Taiyuan ([[chai2023-hdc-ambient-temperature]]) and
  XUT ([[li2021-hdc-sulfate-dry-wet]]), but the Deng (XAUAT) papers are not ingested. PVA-HDC reaches only
  about 1.2–1.5% strain, and no Chinese HDC paper reports crack width. → [[pva-fiber]]
- **No standard test method** for HDC tension and flexure ([[zhang2022-hshdcc-review]];
  [[yu2018-ecc-direct-tensile-review]]); already an R&D need in 2003 ([[li2003-ecc-review]], Sect. 8). The
  definition standard JC/T 2461-2018 exists but has not been ingested. → [[dogbone-uniaxial-tension]]
- **No field deployment** of HSHDCC ([[zhang2022-hshdcc-review]], p. 2). Structural applications are
  known only second-hand. → [[masonry-wall-retrofit]], [[rc-member-strengthening]]
- **Long-term ageing:** almost all data are at 28 d. Ductility and self-healing fall with age.
  → [[durability]]
- **Extreme rates** above 10 s⁻¹ for HSHDC, and reinforced members under impact. → [[strain-rate-effects]], [[impact-resistance]]
- **Interface data** exist only for Michigan PE-HSHDC and Michigan PVA-ECC (two matrices). → [[fiber-matrix-interface]]
- **Flaw size** is never measured; Kanda & Li call for a random, interacting-flaw model ([[kanda2006-psh-design-criteria]], p. 68). → [[matrix-fracture-toughness]]
- **Effect of curing regime** on PSH indices and ductility is unclear ([[zhang2022-hshdcc-review]]). → [[heat-curing]]
- **Size-independent tensile constitutive model** ([[yu2018-ecc-direct-tensile-review]]). → [[size-effect]]

## Open questions
- Can PSH indices be extended to include embedment length and flaw size (as in Li & Leung 1992)?
- Can PE-HSHDC crack widths be brought below 60–80 µm, e.g. with hybrid steel, SF or rubber, to gain
  self-healing and chloride resistance?
- Does ambient-cured HSHDC keep its ductility after long-term ageing?
