---
type: property
slug: tensile-strain-capacity
aliases: [tensile ductility, ε_tu, εp, ε_cu, strain capacity, peak strain]
tags: [tension, ductility, key-property]
sources: [li2002-pva-ecc-interface-tailoring, ranade2015-hshdc-tensile-rate-effects, ranade2017-hshdc-impact-resistance, su2023-rubber-modified-hshdc, yang2024-hshdc-uniaxial-tension, ye2021-uhdc-flexural-size-effect, he2024-hdc-research-advances, yu2018-ecc-direct-tensile-review, zhang2022-hshdcc-review, chai2023-hdc-ambient-temperature, kanda2006-psh-design-criteria, yang2008-ecc-fiber-bridging-law, kanakubo2006-dfrcc-tensile-test-method, kunieda2010-uhp-shcc-steel-reinforcement, chavesfigueiredo2020-printed-shcc, ivaniuk2022-printable-shcc-design, gao2020-hdcc-recycled-fine-aggregate, zhao2022-ecc-tension-damage-model, deng2018-hdc-short-columns, jin2019-hvfa-shcc-structural, qian2007-shcc-inverse-tensile-strain, mechtcherine2011-shcc-high-strain-rate, sun2019-modified-pva-fiber-ecc, wang2023-ecc-frost-damage, xue2023-shcc-structural-review, shumuye2022-slag-fa-pe-ecc, paul2014-r-shcc-chloride-corrosion, kanda2003-sprayed-ecc, sui2018-uhp-ecc-flexural-fatigue, deng2017-rc-column-hdc-jacket, deng2019-urm-shaking-table-hdc, deng2020-aac-wall-hdc-retrofit, li2021-hdc-beam-shear, zhang2022-hdc-basalt-textile-tension, choi2016-pe-alkali-activated-slag-composite, yang2009-ecc-self-healing-wet-dry, yun2013-shcc-freeze-thaw, pourfalah2018-ecc-high-temperature, hieu2023-aas-extremely-ductile-22pct, huy2023-egc-activator-pretreatment, huy2023-egc-pe-pva-hybrid-healing]
updated: 2026-10-26
---

# Tensile Strain Capacity (ε_tu)

## Definition
The tensile strain at **peak** stress in direct uniaxial tension (dogbone). Sources name it
differently: ε_tu, εp, ε_cu. Some sources do not say whether the value is at peak or at failure,
so check this before comparing. → [[dogbone-uniaxial-tension]]

## Quantitative evidence (ranges; full rows in [[mechanical-results]])
| Source | Material | Curing | ε_tu (%) | σ_tu (MPa) | Note |
|---|---|---|---|---|---|
| [[ranade2015-hshdc-tensile-rate-effects]] | Michigan HSHDC, 10⁻⁴ s⁻¹ | 90 °C | **4.2** ⚔️ | 14.5 | 6 dogbones, 90 mm gauge |
| [[ranade2017-hshdc-impact-resistance]] (quoted from earlier work) | Michigan HSHDC | 90 °C | **3.4** ⚔️ | 14.5 | same mix |
| [[su2023-rubber-modified-hshdc]] | GDUT R-HSHDC, PE 12–18 mm | ambient | 2.9–5.7 | 16.1–19.6 | strain basis not stated ⚠️ |
| same | PE 6 mm | ambient | 0.3–0.5 | 8.9–10.4 | brittle |
| [[yang2024-hshdc-uniaxial-tension]] | Xi'an HSHDC, PE22 | 20 °C | 3.56–6.48 | 5.7–7.7 | at peak |
| same | Xi'an HSHDC, PVA39 | 20 °C | 0.23–0.30 | 4.8–5.5 | — |
| [[ye2021-uhdc-flexural-size-effect]] | Tongji UHDC 1% / 2% PE | ambient | 4.31 / **9.45** | about 7 / about 9.5 ⚠️ (Fig. 4b) | 80 mm gauge |
| [[he2024-hdc-research-advances]] p. 20 | "ordinary HDC" | — | 3–5 | 3–7 | uncited ⚠️ |
| [[ranade2017-hshdc-impact-resistance]] | Cor-Tuf FR-UHPC | 90 °C | 0.12 | 11.2 | tension-softening |
| [[li2002-pva-ecc-interface-tailoring]] | Michigan PVA-ECC, oil 0 → 1.2% | water, about 14 d | 0.99 → **4.88** | 4.89 → 4.41 | coupon, about 185 mm gauge |
| [[yu2018-ecc-direct-tensile-review]] Table 1, p. 347 | ECC (range) / UHP-SHCC / HSHDC / UHDCC | — | 3–12 / 2.8 / 3–4 / 8–13 | 4–20 / — / — / — | review ranges, uncited |
| [[yu2018-ecc-direct-tensile-review]] Fig. 2 | Tongji PE-ECC, Vf·Lf/df 7.5 → 18 | — | 2.20 → 7.91 | 10.29 → 17.86 | 15 cases |
| [[zhang2022-hshdcc-review]] (as cited) | HSHDCC: Huang 2021 / Li Y 2020 / Yu K 2017 | 90 °C / ambient | > 5 / 11 / 8.5 | about 16 / 12.1 / 18.2 | f'c > 210 / 115–131 / 122 MPa |

## Influencing factors
- **Fiber type:** PE far outperforms PVA in high-strength matrices. → [[pe-fiber]], [[pva-fiber]]
- **Fiber length and diameter:** very short PE (6 mm) is brittle; a finer diameter raises ε about 10×.
  → [[fiber-geometry]]
- **Matrix:** more FA (+68.9%), the optimum W/B (0.16), and rubber (up to +71.6%) all raise ε.
  → [[fly-ash]], [[water-binder-ratio]], [[crumb-rubber]]
- **Strain rate:** ε falls from 4.2% to about 2.9% between 10⁻⁴ and 0.1 s⁻¹, then plateaus. It
  tracks crack width. → [[strain-rate-effects]]
- **Freeze–thaw:** ε_tu drops more than σ_tu (Yun 2013, as cited in [[he2024-hdc-research-advances]],
  p. 13). Now primary: hybrid PVA+PE SHCC dumbbells still strain-harden after 300 ASTM C666 (B) cycles; σ_t shows no
  distinct change, ε "slightly decreases", more at W/B 0.55 and higher PVA share ([[yun2013-shcc-freeze-thaw]],
  Figs. 8–9, Concl. 3; values only as scatter points, 2 specimens). → [[freeze-thaw]], [[durability]]
- **Fibre origin:** same XAUAT mix, Japanese vs Chinese PVA: ≈ 3.0 vs ≈ 1.2% ultimate
  ([[deng2017-rc-column-hdc-jacket]], Fig. 1a). → [[pva-fiber]]
- **Hybrid steel fibre:** replacing part of the PVA with steel lowers ε at peak (3.5 → 3.0 / 2.5%) and raises σ_tu
  ([[pourfalah2018-ecc-high-temperature]], Table 4). → [[hybrid-fiber]]

> Synthesis: Across sources, ε_tu falls as matrix strength rises:
> - UHDC (f'c about 37 MPa): up to 9.45% (superseded as the wiki maximum on 2026-10-26 by cementless ED-AASC, 22.34%; see Round-7 below)
> - Xi'an HSHDC (about 100 MPa): up to 6.5%
> - GDUT (about 120–157 MPa): up to 5.7%
> - Michigan (166 MPa): 3.4–4.2%
>
> This looks like a strength–ductility trade-off **within the primary sources**.
>
> ⚔️ **However**, the review [[zhang2022-hshdcc-review]] compiles HSHDCC that break this trend:
> f'c > 210 MPa with ε_tu > 5% (Huang 2021), and 122 MPa with 8.5% (Yu K 2017). The trade-off is
> therefore **not fundamental**. It reflects the matrix, fiber and interface design of each group.
> The better framing for the review is "ductility is governed by interface and fiber tailoring, not
> by f'c alone". → [[fiber-matrix-interface]]
>
> He et al. argue that 3–5% is not enough for unreinforced structural use
> ([[he2024-hdc-research-advances]], p. 20).

## Conflicts
- ⚔️ Michigan HSHDC quasi-static ε_tu: 3.4% vs 4.2%, same mix and about the same rate. Report the range. → [[gaps]]
- ⚔️ The strength–ductility "trade-off" is contradicted by the compiled HSHDCC data in
  [[zhang2022-hshdcc-review]]. → [[gaps]]
- Specimen shape matters: cylinders give lower σ and ε than dogbones (Kesner 2003; Mechtcherine 2011),
  while thickness (13 / 30 / 50 mm) does not (Rokugo 2007), as cited in
  [[yu2018-ecc-direct-tensile-review]], p. 348. → [[dogbone-uniaxial-tension]]
  - ⚔️ The primary data below (Kanakubo 2006 round robin; Kunieda 2010 members) show large shape, casting and
    thickness effects, against "negligible thickness effect" (Rokugo 2007, as cited). → [[gaps]]
- ⚔️ Definition: some papers report a post-peak "ultimate" strain as ε_tu (Gao 2020, Zhao 2022, Kunieda 2010, Sun 2019);
  these are not comparable with strain at peak. See below.

## Further evidence (2026-10-20 ingest)
| Source | Material | Curing / age | ε_tu (%) | σ_tu (MPa) | Note |
|---|---|---|---|---|---|
| [[chai2023-hdc-ambient-temperature]] Tables 4, 6 (pp. 6, 10) | Chinese PVA-HDC C40 (FA/C 0.88) | 28 d std + 8 h exposure | 1.15 at 20 °C; 1.15–1.46 over −30 to 60 °C | 3.74–4.80 | dogbone, 100 mm gauge; strain **at peak stress** (Fig. 1, p. 2; Fig. 7, p. 6) |
| same | screening W/B 0.31 / 0.25 / 0.20 | 28 d | 0.64 / 0.55 / 0.42 | 4.47 / 4.22 / 4.83 | f_cu 47.8 / 50.2 / 59.0 MPa; at peak (Table 4, p. 6) |
| [[kanda2006-psh-design-criteria]] Table 4 | paste + SF, PVA 14 / 40 µm, PE 14 µm | n.s. | 0.26–1.50 (PVA); 5.10 (PE) | 2.43–4.62 | coupon, 205 mm gauge; ultimate strain |
| [[yang2008-ecc-fiber-bridging-law]] Fig. 1 | M45 PVA-ECC 2% | n.s. | ≈4–4.5 ⚠️ (read) | about 5 | reference mix |

- **Chinese PVA-HDC reaches only about 1.2–1.5%**, far below ECC's > 3% but above the 0.5% HDC
  standard ([[chai2023-hdc-ambient-temperature]]). Lower W/B raises strength and lowers ε_tu in the same mixes (Table 4). → [[water-binder-ratio]]

## Round-4 evidence (2026-10-20, 34-source ingest)
| Source | Material (authors' term) | Curing / age | ε (%) | σ_tu (MPa) | Note |
|---|---|---|---|---|---|
| [[deng2018-hdc-short-columns]] p. 2, Fig. 1 | XAUAT PVA-HDC, 2%, W/B 0.29 | n.r. | ≈1.0 | 6.14 (first crack 5.73) | σ_tu/σ_fc ≈ 1.07 (computed); geometry n.r. ⚠️ |
| [[jin2019-hvfa-shcc-structural]] Table 5 | Southeast HVFA-SHCC, PVA 2%, FA/C 2.4 / 3.2 / 4.4 | 28 d std | 1.92 / 3.42 / 3.07 | 3.97–4.10 | FA optimum ≈ 3.2; labelled "ultimate" but ≈ strain at peak (curves drop right after peak, Fig. 7, p. 10; not defined in the paper) |
| [[qian2007-shcc-inverse-tensile-strain]] Table 6 | HVFA PVA-ECC, FA/C 1.2 / 2.0 / 2.8 | 28 d | 2.1 / 3.5 / 3.7 | — | COV 52 / 9 / 11% |
| [[zhao2022-ecc-tension-damage-model]] Table 3 | PVA-ECC (FA/C 2.0, SF), Vf 1 → 2% at W/B 0.28 | ≥ 35 d ⚠️ | ε_p 0.51 → 2.00 | about flat | ε_u (post-peak) 1.9–4.1% |
| same | W/B 0.24 → 0.28 at 2% PVA | same | ε_p 0.50 → 2.00 | — | — |
| [[gao2020-hdcc-recycled-fine-aggregate]] Table 6 | N-HDCC / R-HDCC (recycled fine aggregate), PVA 2%, W/B 0.45 | 28 d | **ε_tp 1.68 / 4.76** | 2.75 / 2.84 | "ε_tu" 10.72 / 11.73% is post-peak maximum strain (50 mm gauge) — **not** tensile strain capacity |
| [[mechtcherine2011-shcc-high-strain-rate]] Table 2 | PVA-SHCC (high FA, SAP) | n.r. | 1.49 at 10⁻⁵ s⁻¹ → 0.82 (10⁻²) → 0.68 (10) → 1.79 (50 s⁻¹) | 4.54 → 11.93 | at peak; non-monotonic with rate → [[strain-rate-effects]] |
| [[sun2019-modified-pva-fiber-ecc]] Table 11 | WUT PVA-ECC, untreated / VAE-coated REC-15 | 7 d → 28 d | 3.21 → 1.39 / 4.05 → 2.18 | — | ε −46 to −57% while first-crack strength +22–27%. "Ultimate tensile strain" = strain at **end of test incl. the softening branch**, not at peak (e.g. S4 7-d peak ≈ 2.9% vs 3.21%; S3 ≈ 1.0% vs 2.02%; Figs. 8–9, p. 15). Fig. 6 scatter is large (S4 ≈ 2.6–3.8%, S2 ≈ 2.8–5.3%), so the VAE gain lies within it (Fig. 6, p. 13) |
| [[wang2023-ecc-frost-damage]] Table 4 | PVA-ECC (FA/C 1.18, 8 mm PVA 2%) | 28 d | 5.24 | 4.21 | test method not described ⚠️ |
| [[shumuye2022-slag-fa-pe-ecc]] §3.2, p. 8; Fig. 5b | PE-ECC, slag 0 / 5 / 10 / 15% | 28 d | ≈2.0 / 3.5 / ≈2.9 / ≈2.2 (15%: read from Fig. 5b) | 5.35 / 5.20 / 5.70 / — | "average ultimate strain" = 28-d strain **at peak stress** (Fig. 5b, p. 8); post-peak end strains ≈ 4.4–5.0%. Text says slag lowers ε, numbers disagree ⚠️ |
| [[paul2014-r-shcc-chloride-corrosion]] Table 2 | PVA-SHCC, fine vs coarse (≤ 1.7 mm) sand | n.r. | 2.93 vs 1.52 | — | coarse sand localises earlier |
| [[kanda2003-sprayed-ecc]] Fig. 10–11 | sprayed / placed PVA-ECC | n.r. | about 1.2–1.6 ⚠️ (read) | — | high air content |
| [[chavesfigueiredo2020-printed-shcc]] Table 5 | 3D-printed PVA-SHCC | 35 d | **0.15–0.31** | — | below JC/T 2461's 0.5% → [[3d-printed-hdc]] |
| [[ivaniuk2022-printable-shcc-design]] p. 14; Fig. 17, p. 15 | printed PE-SHCC (Ref / SE-CE) | n.r. | 2–3 (text); ≈ 2.0–3.0 / ≈ 2.0–2.6 at **onset of softening** (read from Fig. 17) | 5.4 / 4.1 | first crack ≈ 3 MPa (Fig. 17); 2–3% appears to be strain at onset of softening ≈ peak; not defined ⚠️ |
| [[kunieda2010-uhp-shcc-steel-reinforcement]] §3.2, Table 3 | UHP-SHCC (PE 6 mm × 12 µm, 1.5%; f'c 95 MPa), 13 × 30 mm dumbbell | 28 d | 1.5 (ultimate) | about 6.5 | reference for the members below |
| [[xue2023-shcc-structural-review]] Fig. 1 (as cited) | PE-SHCC with SF, W/B 0.22 | — | 1.5–2.2 | 7–8 | basis ⚠️ |
| [[sui2018-uhp-ecc-flexural-fatigue]] Fig. 4, p. 5 | PE UHP-ECC (f'c 120.7 MPa at 90 d) | presumably 90 d | ≈ 6.9–8.8 at end of hardening (specimens 1–3 ≈ 7.9 / 8.8 / 6.9; average curve ≈ 8.3), read from Fig. 4; abstract "> 8" | ≈ 11.5 / 11.6 / 12.4 (average curve ≈ 11.1), read from Fig. 4; abstract "up to 12" | first crack ≈ 8–9.5 MPa at ≈ 0.3–0.5% (read); dog-bone 330 mm, gauge 80 × 30 × 13 mm (Fig. 3a, p. 4) |

As cited: ECC typically > 3%, "300 times" normal concrete (Li & Kanda 1998; Li 2001, in
[[qian2007-shcc-inverse-tensile-strain]], p. 235); PVA-ECC with 2% fiber "almost 2%" (Shimizu 2005, in
[[kanakubo2006-dfrcc-tensile-test-method]], p. 3).

### Test method changes the number (Kanakubo 2006 JCI round robin)
Same PVA-DFRCC mix, four tension methods ([[kanakubo2006-dfrcc-tensile-test-method]], Tables 6–9, Fig. 3):

| Method | Specimen | Casting | ε at peak (%) |
|---|---|---|---|
| T1 | 30 × 13 mm thin plate (pin–fix) | horizontal | **2.70** |
| T2-H / T2-V | 100 × 60 mm dogbone (pin–fix) | horizontal / vertical | 2.38 / 0.77 |
| T3 | Ø70 mm dogbone (pin–fix) | vertical | **0.07** |
| T4 | Ø100 × 200 mm cylinder (fix–fix) | vertical | 0.32 |

- The COV of strain at peak reaches 127–157% (CV > 100%). The authors conclude strain at maximum stress is
  "not suitable" to describe DFRCC deformation capacity (p. 9–10).
- Thin sections give 2-D fiber orientation and higher σ and ε; casting direction changes orientation
  (p. 8–9). → [[fiber-dispersion]], [[dogbone-uniaxial-tension]]
- The bending-based inverse alternative is on [[four-point-bending-inverse-analysis]]; Qian's reference UTT
  was the T1 plate (2.7%) rather than T2 (2.38 / 0.77%).

### Member size and thickness (Kunieda 2010)
- Unreinforced 50 × 200 mm UHP-SHCC tension members reached only **0.23–0.24%** vs 1.5% for the 13 × 30 mm
  dumbbell: ultimate strain about **85% lower** and stress about 30% lower; strain hardening turned into brittle
  failure ([[kunieda2010-uhp-shcc-steel-reinforcement]], §4.1, Fig. 5, Table 3).
- Explanations: 2-D fiber orientation in 13 mm dumbbells vs 3-D in 50 mm members, and a weakest-link widening of
  the bridging-strength distribution in larger volumes (§2, §4.1, Fig. 2). → [[size-effect]]
- Small steel reinforcement restores it: D6 at ρs 0.3% gives 1.58% (119 vs 43 cracks); 1.49–1.82% for
  ρs 0.3–1.2% (Table 3).
- Dogbone ductility is also not realised in thin strengthening layers bonded over a substrate crack
  ("zero-span" tension) ([[xue2023-shcc-structural-review]], Section 4.1.2). → [[rc-member-strengthening]]

### Definition traps
- **Post-peak "ultimate" strains:** Gao's "ε_tu" (up to 11.73%) and Zhao's ε_u (1.9–4.1%) are on the
  softening branch. Use ε_tp / ε_p (strain at peak) for comparison ([[gao2020-hdcc-recycled-fine-aggregate]],
  §2.3.3; [[zhao2022-ecc-tension-damage-model]], §3.1.3).
- **Scatter:** COV of ε_tu is 26–60% vs < 15% for strengths, so quality control should target strain
  ([[qian2007-shcc-inverse-tensile-strain]], p. 243).
- **Age:** ε fell by about half from 7 to 28 d in WUT PVA-ECC ([[sun2019-modified-pva-fiber-ecc]], Table 11, p. 16;
  "ultimate" strain includes the softening branch, Figs. 8–9, p. 15);
  7-d values overstate ductility.

> Synthesis: "tensile strain capacity" is a test-dependent number, not a material constant. The same PVA mix
> spans 0.07–2.70% across specimen types (Kanakubo), and a PE UHP-SHCC loses about 85% of its dumbbell strain
> in a 50 mm thick member (Kunieda). Thin-coupon values (13–15 mm, horizontally cast) are upper bounds.
> ⚔️ This contradicts "thickness negligible" (Rokugo 2007, as cited in [[yu2018-ecc-direct-tensile-review]]).
> Chinese and other "HDC/HDCC/SHCC" mixes measured with ordinary materials (Deng 2018 ≈ 1.0%, N-HDCC 1.68%,
> Sun 2019 1.39% incl. softening branch, printed SHCC 0.15–0.31%) fall well below the ECC "> 3%" convention but above the 0.5% HDC bar
> (except printed SHCC). → [[terminology-hdc-ecc-shcc]]

## Round-5 evidence (2026-10-21, 10-source ingest)
| Source | Material (authors' term) | Curing / age | ε (%) | σ_tu (MPa) | Note |
|---|---|---|---|---|---|
| [[deng2017-rc-column-hdc-jacket]] Table 5, Fig. 1a | XAUAT HDC, 2% **Japanese** PVA (1600 MPa, 40 GPa), FA/C 1.0, W/B 0.29 | n.r. | **≈ 3.0 ultimate** ⚔️ (end of curve, read ⚠️) | 6.12 | strain at peak n.r.; specimen geometry n.r. |
| same | same mix, 2% **Chinese** PVA (1200 MPa, 32 GPa) | n.r. | ≈ 1.2 ultimate (read ⚠️) | 4.84 | "about 150% higher" strain with Japanese fibre |
| [[deng2019-urm-shaking-table-hdc]] Table 3, Fig. 6a | XAUAT HDC, 2% PVA, same proportions | 28 d cubes; tension age n.r. | ≈ 1.0 ultimate (curves end 0.86–1.0%, read ⚠️) | 5.83 (mean of 3) | 15 mm plates, DBJ61/T112-2016; curves may reuse [[deng2018-hdc-short-columns]] data ⚠️ |
| [[deng2020-aac-wall-hdc-retrofit]] Table 3, Fig. 3 | XAUAT HDC ("also referred to as ECC"), 1.7% PVA | air-cured ≈ 2 months | ≈ 1.2 at peak (read ⚠️) | 3.89 | dogbone 15 × 50 mm |
| [[li2021-hdc-beam-shear]] §2.1, Fig. 1 | HDC (Henan / XAUAT), 2% PVA, FA/C 1.0, W/B 0.29 | 28 d | 0.968 (basis n.s. ⚠️) | 5.83 (5.68 in Concl. 1 ⚠️) | dogbone 15 × 50 mm |
| [[zhang2022-hdc-basalt-textile-tension]] Tables 3, 8 | plain XAUAT HDC M1 (FA/C 1.1, SF + "mineral powder"), 1.5 / 2% PVA | 28 d std | **0.12 / 0.34** at peak ⚔️ | 3.89 / 5.44 | below the JC/T 2461 0.5% bar |
| same | plain HDC M2 (HVFA, FA/C 3.25), 1 / 1.5 / 2% PVA | 28 d std | 0.29 / 0.28 / **0.45** at peak | 2.35 / 3.45 / 4.23 | — |
| same, Table 8 | TR-HDC: + 1–3 basalt grid layers (ν 0.42–1.26%), 2% PVA | 28 d | 1.51–2.48 at peak | 5.83–10.02 | textile-governed → [[textile-reinforced-hdc]] |
| [[choi2016-pe-alkali-activated-slag-composite]] Tables 5, 7 | cementless alkali-activated GGBS + 1.75% PE (18 mm × 12 µm), W/B 0.26 → 0.38 | 28 d ⚠️ | **7.50** → 4.58 (basis n.s. ⚠️) | 13.06 → 5.06 | f'c 54.8 → 36.3 MPa; JSCE dogbone, 80 mm gauge → [[alkali-activated-binder]] |
| [[pourfalah2018-ecc-high-temperature]] Table 4 | Heriot-Watt PVA-ECC / HECC (1.75% PVA + 0.75% steel 6 / 13 mm) | 28 d | 3.5 / 3.0 / 2.5 at peak | 3.85 / 4.36 / 4.71 | JSCE dogbone, 80 mm gauge |
| [[yang2009-ecc-self-healing-wet-dry]] p. 388 | M45 PVA-ECC pre-strained 2–3%, healed by wet–dry cycles | 6 months + cycles | 1.7–3.1 (room-air drying) / 0.8–2.2 (55 °C drying) on reloading | — | healed ECC regains strain hardening → [[self-healing]] |
| [[yun2013-shcc-freeze-thaw]] Fig. 9b | hybrid PVA+PE SHCC (1.5% total), 0 vs 300 F-T cycles | 14 d start | ≤ ≈ 1 (scatter points ⚠️; Fig. 10 shows ≈ 2.4–2.6% for a virgin mix) | no distinct change | JSCE dumbbell, n = 2 |

- ⚔️ **XAUAT PVA-HDC, same nominal mix (593 C / 593 FA / 427 sand / 2% PVA 12 mm × 39 µm):** ≈ 3.0% ultimate
  ([[deng2017-rc-column-hdc-jacket]], Japanese PVA) vs ≈ 1.0% ([[deng2018-hdc-short-columns]], Fig. 1;
  [[deng2019-urm-shaking-table-hdc]], Fig. 6a) and 0.968% ([[li2021-hdc-beam-shear]]), with nearly equal σ_tu
  (6.12 vs 6.14 / 5.83 MPa). The 2018 fibre properties (1600 MPa, 40 GPa) match the Japanese fibre. Reason not
  given (batch, specimen geometry, strain definition). → [[gaps]]
- ⚔️ **Plain XAUAT PVA-HDC with SF + "mineral powder" matrix:** 0.34–0.45% at peak at 2% PVA
  ([[zhang2022-hdc-basalt-textile-tension]], Table 8) vs ≈ 1.0% for the FA-only matrix above. Matrix (W/B ≈ 0.30–0.32
  computed, SF), strain basis (peak vs ultimate) and specimen all may differ. Another "HDC" below the JC/T 2461 0.5% bar,
  like printed SHCC (0.15–0.31%). → [[terminology-hdc-ecc-shcc]], [[gaps]]
- **Cementless AAS-PE (Choi 2016)** reaches 7.50% with σ_tu 13.06 MPa at only f'c 54.8 MPa (σ_tu/f'c 23.8%), and lower
  W/B is more ductile (W/B 0.26 → 0.38: ε −38.9%, σ_tu −61.3%) ([[choi2016-pe-alkali-activated-slag-composite]],
  §3.3, Table 7). → [[water-binder-ratio]]
- In textile composites, adding PVA reduces peak strain (B3M1: 2.65 → 1.96–2.13%) by suppressing textile slip
  ([[zhang2022-hdc-basalt-textile-tension]], §4.2).

> Synthesis: the XAUAT "HDC" family now spans ≈ 0.3% to ≈ 3.0% for nominally similar 2% PVA mixes across five
> papers. Values cluster at ≈ 1.0% (Deng 2018, Deng 2019, Li 2021, Deng 2020 ≈ 1.2%), with one high outlier
> (Deng 2017, Japanese PVA ≈ 3.0%) and one low set (Zhang 2022, 0.34–0.45%). Fibre origin is the only stated
> variable (Deng 2017). Because most XAUAT strains are figure-read and their basis (peak vs end of curve) is not
> always stated, "≈ 1% for Chinese PVA-HDC" is a cluster, not a material constant. The Choi 2016 AAS-PE result adds
> to the evidence that the strength–ductility "trade-off" is not fundamental.

## Round-7 evidence (2026-10-26): new maximum strains (Chonnam cementless composites)
| Source | Material (authors' term) | Curing / age | ε at peak (%) | σ_tu (MPa) | Note |
|---|---|---|---|---|---|
| [[hieu2023-aas-extremely-ductile-22pct]] Table 4 | ED-AASC R5-S8-M1 (GGBS + Ca(OH)₂, sand S/B 0.8, 5% CR, 1.75% PE) | air + water + 24 h 80 °C; 28 d | **22.34 ± 0.48** | 7.63 | **highest in the wiki**; f'c 53.6 MPa; JSCE dumbbell, 80 mm gauge, 5 specimens |
| same | R5-S8-M2 / R5-S8-M0 (same proportions, other mixing procedures) | 28 d | 20.89 ± 2.13 / 9.81 ± 2.92 | 8.19 / 7.92 | mixing alone: 2.2–2.3× |
| [[huy2023-egc-activator-pretreatment]] Table 4 | ED-EGC-CP / ED-EGC-WP (fly-ash geopolymer, 1.75% PE) | 5 d 23 °C + 2 d 80 °C; 28 d | **18.62 ± 1.59** / 10.97 ± 1.31 | 5.54 / 8.72 | f'c 20.7 / 31.1 MPa |
| [[huy2023-egc-pe-pva-hybrid-healing]] Table 5 | HSUD-EGC S-PE / S-PVA / F-PE / F-PVA (GGBS/FA/SF geopolymer, 1.5% PE + PVA) | 24 h 100 °C + 28 d water; ≈ 35 d ⚠️ | 10.51 / 6.79 / 11.99 / 10.35 | 6.64 / 6.04 / 5.18 / 4.60 | f'c 84.3 / 86.5 / 50.4 / 51.9 MPa |
| same, Table 8 | the same after 3% pre-strain + 28 d water healing, reloaded | 35 d | 9.45 / 6.29 / 11.97 / 9.67 (incl. 3% pre-strain) | 7.53 / 6.33 / 5.23 / 4.40 | on average σ_tu +3.7%, ε −6.1% vs virgin |

- **New maximum**: 22.34% at peak (previous primary maximum: UHDC 9.45%, [[ye2021-uhdc-flexural-size-effect]]; Choi 2016
  7.50%). All values above 10% in the wiki now come from one group (Chonnam National University), the same 18 mm × 12 µm PE,
  thin (13 mm) JSCE dumbbells with an 80 mm gauge, and heat-cured cementless matrices.
- **Mixing procedure** alone moved ε from 9.81 to 22.34% at identical proportions and cut the COV (2.92 → 0.48 %-points)
  ([[hieu2023-aas-extremely-ductile-22pct]], Table 4, §3.1). → [[fiber-dispersion]]
- **Matrix weakening** (activator cooling pretreatment) raised ε from 10.97 to 18.62% while f'c fell from 31.1 to 20.7 MPa
  ([[huy2023-egc-activator-pretreatment]], Table 4).
- **GGBS:FA ratio**: more FA (3:6.5) raised ε (10.51 → 11.99%, PE-rich) and lowered f'c by ≈ 40%
  ([[huy2023-egc-pe-pva-hybrid-healing]], Table 5, Fig. 3). → [[fly-ash]]
- **Steel-bar comparison**: both ED papers compare ε with minimum rebar elongation (ASTM A615 9%, A706 14%, ISO 6935-2 14 /
  17%) ([[hieu2023-aas-extremely-ductile-22pct]], Fig. 15; [[huy2023-egc-activator-pretreatment]], Fig. 11). Caution: composite
  strain at peak over 80 mm vs steel elongation at fracture over a different gauge.
- **Index values**: f'c × ε 11.9 MPa and σ_tu × ε 1.70 MPa for ED-AASC M1, the highest of the composites compared there
  ([[hieu2023-aas-extremely-ductile-22pct]], Table 7); 8.8 MPa for HSUD-EGC S-PE ([[huy2023-egc-pe-pva-hybrid-healing]], Fig. 6).

> Synthesis (round 7): the record strains are an upper bound on **thin-specimen, heat-cured, single-lab** data. They come
> with wide cracks (≈ 170–212 µm average at peak), low-to-moderate σ_tu (5.5–8.2 MPa) and, for ED-EGC-CP, a weak matrix
> (20.7 MPa). Thickness and size effects ([[kunieda2010-uhp-shcc-steel-reinforcement]]; [[kanakubo2006-dfrcc-tensile-test-method]])
> suggest lower values in members. Within one study, a weaker matrix gave more strain ([[huy2023-egc-activator-pretreatment]]),
> which supports a trade-off locally; across studies, HSUD-EGC at 84 MPa with 10.5% supports "the trade-off is not fundamental".
> The review should cite "> 20% at peak in a cementless PE composite" with these qualifiers. → [[gaps]]

## Related
- [[alkali-activated-binder]] · [[textile-reinforced-hdc]] · [[strain-hardening]] · [[crack-width]] · [[tensile-toughness]] · [[mechanical-results]] · [[four-point-bending-inverse-analysis]] · [[recycled-fine-aggregate]]
