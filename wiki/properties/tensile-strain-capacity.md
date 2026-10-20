---
type: property
slug: tensile-strain-capacity
aliases: [tensile ductility, ε_tu, εp, ε_cu, strain capacity, peak strain]
tags: [tension, ductility, key-property]
sources: [li2002-pva-ecc-interface-tailoring, ranade2015-hshdc-tensile-rate-effects, ranade2017-hshdc-impact-resistance, su2023-rubber-modified-hshdc, yang2024-hshdc-uniaxial-tension, ye2021-uhdc-flexural-size-effect, he2024-hdc-research-advances, yu2018-ecc-direct-tensile-review, zhang2022-hshdcc-review, chai2023-hdc-ambient-temperature, kanda2006-psh-design-criteria, yang2008-ecc-fiber-bridging-law, kanakubo2006-dfrcc-tensile-test-method, kunieda2010-uhp-shcc-steel-reinforcement, chavesfigueiredo2020-printed-shcc, ivaniuk2022-printable-shcc-design, gao2020-hdcc-recycled-fine-aggregate, zhao2022-ecc-tension-damage-model, deng2018-hdc-short-columns, jin2019-hvfa-shcc-structural, qian2007-shcc-inverse-tensile-strain, mechtcherine2011-shcc-high-strain-rate, sun2019-modified-pva-fiber-ecc, wang2023-ecc-frost-damage, xue2023-shcc-structural-review, shumuye2022-slag-fa-pe-ecc, paul2014-r-shcc-chloride-corrosion, kanda2003-sprayed-ecc, sui2018-uhp-ecc-flexural-fatigue]
updated: 2026-10-20
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
  p. 13). → [[durability]]

> Synthesis: Across sources, ε_tu falls as matrix strength rises:
> - UHDC (f'c about 37 MPa): up to 9.45%
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
- ⚔️ Definition: some papers report a post-peak "ultimate" strain as ε_tu (Gao 2020, Zhao 2022, Kunieda 2010);
  these are not comparable with strain at peak. See below.

## Further evidence (2026-10-20 ingest)
| Source | Material | Curing / age | ε_tu (%) | σ_tu (MPa) | Note |
|---|---|---|---|---|---|
| [[chai2023-hdc-ambient-temperature]] Tables 4, 6 | Chinese PVA-HDC C40 (FA/C 0.88) | 28 d std + 8 h exposure | 1.15 at 20 °C; 1.15–1.46 over −30 to 60 °C | 3.74–4.80 | dogbone, 100 mm gauge; strain basis n.s. ⚠️ |
| same | screening W/B 0.31 / 0.25 / 0.20 | 28 d | 0.64 / 0.55 / 0.42 | 4.47 / 4.22 / 4.83 | f_cu 47.8 / 50.2 / 59.0 MPa |
| [[kanda2006-psh-design-criteria]] Table 4 | paste + SF, PVA 14 / 40 µm, PE 14 µm | n.s. | 0.26–1.50 (PVA); 5.10 (PE) | 2.43–4.62 | coupon, 205 mm gauge; ultimate strain |
| [[yang2008-ecc-fiber-bridging-law]] Fig. 1 | M45 PVA-ECC 2% | n.s. | ≈4–4.5 ⚠️ (read) | about 5 | reference mix |

- **Chinese PVA-HDC reaches only about 1.2–1.5%**, far below ECC's > 3% but above the 0.5% HDC
  standard ([[chai2023-hdc-ambient-temperature]]). Lower W/B raises strength and lowers ε_tu in the same mixes (Table 4). → [[water-binder-ratio]]

## Round-4 evidence (2026-10-20, 34-source ingest)
| Source | Material (authors' term) | Curing / age | ε (%) | σ_tu (MPa) | Note |
|---|---|---|---|---|---|
| [[deng2018-hdc-short-columns]] p. 2, Fig. 1 | XAUAT PVA-HDC, 2%, W/B 0.29 | n.r. | ≈1.0 | 6.14 (first crack 5.73) | σ_tu/σ_fc ≈ 1.07 (computed); geometry n.r. ⚠️ |
| [[jin2019-hvfa-shcc-structural]] Table 5 | Southeast HVFA-SHCC, PVA 2%, FA/C 2.4 / 3.2 / 4.4 | 28 d std | 1.92 / 3.42 / 3.07 | 3.97–4.10 | FA optimum ≈ 3.2; peak vs ultimate ⚠️ |
| [[qian2007-shcc-inverse-tensile-strain]] Table 6 | HVFA PVA-ECC, FA/C 1.2 / 2.0 / 2.8 | 28 d | 2.1 / 3.5 / 3.7 | — | COV 52 / 9 / 11% |
| [[zhao2022-ecc-tension-damage-model]] Table 3 | PVA-ECC (FA/C 2.0, SF), Vf 1 → 2% at W/B 0.28 | ≥ 35 d ⚠️ | ε_p 0.51 → 2.00 | about flat | ε_u (post-peak) 1.9–4.1% |
| same | W/B 0.24 → 0.28 at 2% PVA | same | ε_p 0.50 → 2.00 | — | — |
| [[gao2020-hdcc-recycled-fine-aggregate]] Table 6 | N-HDCC / R-HDCC (recycled fine aggregate), PVA 2%, W/B 0.45 | 28 d | **ε_tp 1.68 / 4.76** | 2.75 / 2.84 | "ε_tu" 10.72 / 11.73% is post-peak maximum strain (50 mm gauge) — **not** tensile strain capacity |
| [[mechtcherine2011-shcc-high-strain-rate]] Table 2 | PVA-SHCC (high FA, SAP) | n.r. | 1.49 at 10⁻⁵ s⁻¹ → 0.82 (10⁻²) → 0.68 (10) → 1.79 (50 s⁻¹) | 4.54 → 11.93 | at peak; non-monotonic with rate → [[strain-rate-effects]] |
| [[sun2019-modified-pva-fiber-ecc]] Table 11 | WUT PVA-ECC, untreated / VAE-coated REC-15 | 7 d → 28 d | 3.21 → 1.39 / 4.05 → 2.18 | — | ε −46 to −57% while first-crack strength +22–27% |
| [[wang2023-ecc-frost-damage]] Table 4 | PVA-ECC (FA/C 1.18, 8 mm PVA 2%) | 28 d | 5.24 | 4.21 | test method not described ⚠️ |
| [[shumuye2022-slag-fa-pe-ecc]] Sect. 3.2 | PE-ECC, slag 0 / 5 / 10% | 28 d | ≈2.0 / 3.5 / ≈2.9 | 5.35 / 5.20 / 5.70 | "average ultimate strain"; text says slag lowers ε, numbers disagree ⚠️ |
| [[paul2014-r-shcc-chloride-corrosion]] Table 2 | PVA-SHCC, fine vs coarse (≤ 1.7 mm) sand | n.r. | 2.93 vs 1.52 | — | coarse sand localises earlier |
| [[kanda2003-sprayed-ecc]] Fig. 10–11 | sprayed / placed PVA-ECC | n.r. | about 1.2–1.6 ⚠️ (read) | — | high air content |
| [[chavesfigueiredo2020-printed-shcc]] Table 5 | 3D-printed PVA-SHCC | 35 d | **0.15–0.31** | — | below JC/T 2461's 0.5% → [[3d-printed-hdc]] |
| [[ivaniuk2022-printable-shcc-design]] | printed PE-SHCC | n.r. | 2–3 | — | peak vs ultimate ⚠️ |
| [[kunieda2010-uhp-shcc-steel-reinforcement]] §3.2, Table 3 | UHP-SHCC (PE 6 mm × 12 µm, 1.5%; f'c 95 MPa), 13 × 30 mm dumbbell | 28 d | 1.5 (ultimate) | about 6.5 | reference for the members below |
| [[xue2023-shcc-structural-review]] Fig. 1 (as cited) | PE-SHCC with SF, W/B 0.22 | — | 1.5–2.2 | 7–8 | basis ⚠️ |
| [[sui2018-uhp-ecc-flexural-fatigue]] abstract, Fig. 4 | PE UHP-ECC | n.r. | > 8 ⚠️ | up to 12 | figure only |

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
- **Age:** ε fell by about half from 7 to 28 d in WUT PVA-ECC ([[sun2019-modified-pva-fiber-ecc]], Table 11);
  7-d values overstate ductility.

> Synthesis: "tensile strain capacity" is a test-dependent number, not a material constant. The same PVA mix
> spans 0.07–2.70% across specimen types (Kanakubo), and a PE UHP-SHCC loses about 85% of its dumbbell strain
> in a 50 mm thick member (Kunieda). Thin-coupon values (13–15 mm, horizontally cast) are upper bounds.
> ⚔️ This contradicts "thickness negligible" (Rokugo 2007, as cited in [[yu2018-ecc-direct-tensile-review]]).
> Chinese and other "HDC/HDCC/SHCC" mixes measured with ordinary materials (Deng 2018 ≈ 1.0%, N-HDCC 1.68%,
> Sun 2019 1.39%, printed SHCC 0.15–0.31%) fall well below the ECC "> 3%" convention but above the 0.5% HDC bar
> (except printed SHCC). → [[terminology-hdc-ecc-shcc]]

## Related
- [[strain-hardening]] · [[crack-width]] · [[tensile-toughness]] · [[mechanical-results]] · [[four-point-bending-inverse-analysis]] · [[recycled-fine-aggregate]]
