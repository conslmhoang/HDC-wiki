---
type: material
slug: alkali-activated-binder
aliases: [alkali-activated slag, AAS, cementless binder, geopolymer, alkali-activated SHCC, EGC, engineered geopolymer composite]
tags: [binder, cementless, sustainability, slag, geopolymer, fly-ash, egc]
sources: [choi2016-pe-alkali-activated-slag-composite, hieu2023-aas-extremely-ductile-22pct, huy2023-egc-activator-pretreatment, huy2023-egc-pe-pva-hybrid-healing]
updated: 2026-10-26
---

# Alkali-Activated (Cementless) Binders

## Definition
A binder made without Portland cement, in which an aluminosilicate precursor (here ground granulated blast-furnace
slag, GGBS, or fly ash) is activated by alkaline or sulfate compounds. All four primary sources in the wiki come from the
same Chonnam National University group (B.Y. Lee), and all use 18 mm × 12 µm PE fibre and the JSCE dumbbell:
- **Alkali-activated slag (AAS) with Ca-based powder activators:** GGBS + powdered Ca(OH)₂ (8.38%) + Na₂SO₄ (3.35%), no
  aggregate ([[choi2016-pe-alkali-activated-slag-composite]], §2.1, Table 1); GGBS 0.90 + Ca(OH)₂ powder 0.10 only (no Na₂SO₄),
  with silica sand/binder 0.8 and 5% crumb rubber ([[hieu2023-aas-extremely-ductile-22pct]], Lương et al. 2023, §2.1, Table 1).
- **Fly-ash geopolymer ("engineered geopolymer composite", EGC):** FA 0.7 + sodium hydroxide (SH) 0.1 + sodium metasilicate
  powder (SMP) 0.2, water/binder 0.345, no aggregate ([[huy2023-egc-activator-pretreatment]], Nguyễn et al. 2023, Table 1).
- **GGBS + FA + 5% SF geopolymer EGC**, NaOH flakes + water glass, silica sand 1.0, PE + PVA hybrid fibre
  ([[huy2023-egc-pe-pva-hybrid-healing]], Nguyễn et al. 2023, Table 1).

**Terminology (as used by each source; none calls its material HDC, ECC or SHCC):**

| Term | Source |
|---|---|
| "ultra-high-ductile polyethylene fiber-reinforced alkali-activated slag-based composite" | [[choi2016-pe-alkali-activated-slag-composite]] |
| "extremely-ductile alkali-activated slag-based composite" (ED-AASC), a sub-class of "highly-ductile alkali-activated slag-based composites" (HD-AASC) | [[hieu2023-aas-extremely-ductile-22pct]], abstract |
| "extremely ductile engineered geopolymer composites" (ED-EGC) | [[huy2023-egc-activator-pretreatment]], abstract |
| "high-strength and ultra-ductility engineered geopolymer composites" (HSUD-EGC) | [[huy2023-egc-pe-pva-hybrid-healing]], title, §1 |

EGC is described as a cement-free composite in which a geopolymer (FA, slag or metakaolin) replaces Portland cement in an
ECC-type design ([[huy2023-egc-activator-pretreatment]], §1; [[huy2023-egc-pe-pva-hybrid-healing]], §1). All four are in the
wiki scope because they show tensile strain hardening with multiple cracking (CLAUDE.md §3). No separate EGC page is
created; this page covers both AAS and geopolymer composites.
→ [[terminology-hdc-ecc-shcc]]

## Key points
- **Ductility does not need cement or a high-strength matrix**: with 1.75 vol.% PE (18 mm × 12 µm, 2700 MPa, 88 GPa),
  the best mix (M26, W/B 0.26) reached ε **7.50%** and σ_tu **13.06 MPa** at f'c **54.8 MPa** (50 mm cubes, 28 d, JSCE
  dogbone, 80 mm gauge) ([[choi2016-pe-alkali-activated-slag-composite]], Tables 5, 7). → [[pe-fiber]], [[tensile-strain-capacity]]
- **No aggregate**, to keep matrix toughness low and favour multiple cracking (§2.1). → [[matrix-fracture-toughness]]
- **Viscosity control** (HRWRA + VMA tuned per W/B, after Li & Li 2013) was used to disperse PE; hardened densities were
  within 0.5% of theoretical (§2.1, §3.1). → [[viscosity-modifying-admixtures]], [[fiber-dispersion]]
- **Curing**: 2 d sealed in air, then water at 23 ± 3 °C; tested at 28 d ⚠️ (whether "28 d" counts from casting is
  unclear, see source page). No heat curing. → [[heat-curing]]
- Ratios σ_tu/f'c 23.8% (M26) and 19.8% on average, about double normal concrete; first-crack/f'c ≈ 9.2% (§3.3).
- **Highest strain in the wiki:** ED-AASC R5-S8-M1 reached ε **22.34 ± 0.48% at peak stress**, with σ_tu 7.63 MPa and f'c 53.6 MPa
  (28 d, JSCE dumbbell, 80 mm gauge) ([[hieu2023-aas-extremely-ductile-22pct]], Table 4, Fig. 7).
- **Mixing procedure alone** changed ε from 9.81 ± 2.92% (M0) to 22.34% (M1) and 20.89% (M2) at identical proportions; f'c
  (52.2–54.6 MPa) was insensitive (COV 1.83%) ([[hieu2023-aas-extremely-ductile-22pct]], Table 4, Fig. 7). → [[fiber-dispersion]]
- **Sand is compatible with very high ε** when crumb rubber is added: S/B 0.8 + 5% CR (vs 0–0.4 S/B in earlier AAS
  composites) ([[hieu2023-aas-extremely-ductile-22pct]], §1, §2.1). → [[crumb-rubber]]
- **A high SP dose delayed hydration**, so demoulding was only possible at 11 d ([[hieu2023-aas-extremely-ductile-22pct]], §2.2.2).
- **Activator pretreatment** (fly-ash EGC): warming the activator solution (5 min, 50 °C, liquid; WP) gave f'c 31.1 MPa and
  ε 10.97%; cooling it for 24 h at 23 °C (SMP partly re-solidified; CP) gave 20.7 MPa and **18.62 ± 1.59%** (28 d, at peak)
  ([[huy2023-egc-activator-pretreatment]], Fig. 8, Table 4). CP halved the matrix Km (0.11 → 0.06 MPa√m) (Table 6).
  → [[matrix-fracture-toughness]]
- **Lightweight**: ED-EGC densities ≈ 1.7 (WP) and ≈ 1.5 g/cm³ (CP) without lightweight fillers
  ([[huy2023-egc-activator-pretreatment]], Fig. 8, §3.1).
- **Reaction products**: N-A-S-H is the main gel in ED-EGC-CP (EDS ternary plot) ([[huy2023-egc-activator-pretreatment]],
  Fig. 14); healing products in the GGBS/FA EGC plot in the C-(N)-A-S-H field ([[huy2023-egc-pe-pva-hybrid-healing]], Table 9, Fig. 15).
- **High strength without cement**: the GGBS:FA 5.5:4 HSUD-EGC reached f'c 84.3–86.5 MPa with ε 10.51% (S-PE) / 6.79% (S-PVA);
  GGBS:FA 3:6.5 gave 50.4–51.9 MPa with ε 10.35–11.99% (≈ 35 d ⚠️; [[huy2023-egc-pe-pva-hybrid-healing]], Fig. 3, Table 5).
  → [[hshdc]]
- **Heat curing** is used in all three 2023 sources: 24 h at 80 °C after 11 d air + 12 d water
  ([[hieu2023-aas-extremely-ductile-22pct]], §2.2.2); 2 d at 80 °C after 5 d at 23 °C ([[huy2023-egc-activator-pretreatment]], §2.2);
  24 h at 100 °C after 2 d sealed ([[huy2023-egc-pe-pva-hybrid-healing]], §2.2). None of them isolates the effect of the heat step.
  → [[heat-curing]]
- **Sustainability**: ED-AASC M1 had −30.1 / −34.3% embodied energy, −39.1 / −38.2% carbon footprint and −13.9 / −3.7% material
  cost per m³ vs an HS-ECC (Luo 2019, as cited) and the earlier CR-AAS composite S-CR5 ([[hieu2023-aas-extremely-ductile-22pct]],
  §4, Fig. 16). The cost of HSUD-EGC S-PE per unit performance was 91 $/(MPa·m³) vs 124–133 for HSUD-ECCs (as cited)
  ([[huy2023-egc-pe-pva-hybrid-healing]], Fig. 7).

## Quantitative evidence
| Mix (W/B, mass) | f'c (MPa) | First-crack σ (MPa) | σ_tu (MPa) | ε_tu (%) | Avg crack width (µm, computed) | Source |
|---|---|---|---|---|---|---|
| M26 (0.26) | 54.8 | 4.87 | 13.06 | 7.50 | 88.9 | [[choi2016-pe-alkali-activated-slag-composite]] Tables 5, 7, 8 |
| M30 (0.30) | 49.0 | 4.61 | 11.46 | 6.33 | 106.9 | same |
| M34 (0.34) | 42.3 | 3.92 | 7.64 | 5.35 | 109.8 | same |
| M38 (0.38) | 36.3 | 3.37 | 5.06 | 4.58 | 99.3 | same |

- Strain basis (at peak vs ultimate) not stated ⚠️; crack width = gauge elongation / crack count at end of loading.

| Mix | f'c (MPa) | First-crack σ (MPa) | σ_tu (MPa) | ε_tu at peak (%) | Avg crack width (µm, computed at peak) | Source |
|---|---|---|---|---|---|---|
| ED-AASC R5-S8-M0 (28 d) | 54.6 | 5.08 | 7.92 | 9.81 | 117.2 | [[hieu2023-aas-extremely-ductile-22pct]] Fig. 7, Tables 4, 6 |
| ED-AASC R5-S8-M1 | 53.6 (53.4 in Table 7 ⚠️) | 4.70 | 7.63 | **22.34** | 212.0 | same |
| ED-AASC R5-S8-M2 | 52.2 | 4.12 | 8.19 | 20.89 | 204.0 | same |
| ED-EGC-WP (FA, 28 d) | 31.1 | 4.67 | 8.72 | 10.97 | 171.8 | [[huy2023-egc-activator-pretreatment]] Tables 4–5, Fig. 8 |
| ED-EGC-CP | 20.7 | 3.40 | 5.54 | 18.62 | 199.3 | same |
| HSUD-EGC S-PE (≈ 35 d ⚠️) | 84.3 | 3.70 | 6.64 | 10.51 | 100.3 | [[huy2023-egc-pe-pva-hybrid-healing]] Fig. 3, Tables 5–6 |
| HSUD-EGC S-PVA | 86.5 | 3.84 | 6.04 | 6.79 | 83.2 | same |
| HSUD-EGC F-PE | 50.4 | 2.70 | 5.18 | 11.99 | 128.4 | same |
| HSUD-EGC F-PVA | 51.9 | 2.84 | 4.60 | 10.35 | 136.1 | same |

### Earlier alkali-activated / geopolymer SHCC (as cited in [[choi2016-pe-alkali-activated-slag-composite]], §1)
| Material | Fiber | f'c (MPa) | σ_tu (MPa) | ε (%) | Original study |
|---|---|---|---|---|---|
| Alkali-activated slag mortar | PVA | 19.4–30.6 | 2.83–4.69 | 1.53–4.48 | Lee et al. 2012 |
| FA geopolymer | PVA | 27.6 | 3.4 | 4.3 | Ohno & Li 2014 |
| Engineered geopolymer composite (EGC) | PVA | 63.7 | 4.7 | 4.3 | Nematollahi 2015 |

### Further earlier composites as cited by the 2023 CNU sources (not primary data)
| Material | f'c (MPa) | σ_tu (MPa) | ε (%) | Original study (as cited) | Cited in |
|---|---|---|---|---|---|
| PE-AAS | — | — | 8.8 | Nguyễn 2019 | [[hieu2023-aas-extremely-ductile-22pct]] §1 |
| CR-AAS S-CR5 | 39.4 | 9.48 | 10.67 | Lương 2021 | [[hieu2023-aas-extremely-ductile-22pct]] Table 7 |
| UD-EGC15 (lightweight FA EGC, PE) | 19.3 | 6.79 | 13.68 | Nguyễn 2021 | [[hieu2023-aas-extremely-ductile-22pct]] Table 7; [[huy2023-egc-pe-pva-hybrid-healing]] §1 (13.7%) |
| One-part EGC, PVA | > 60 | — | ≈ 5 | Nematollahi 2016–17 | [[huy2023-egc-activator-pretreatment]] §1 |
| Slag/FA EGC (described as PVA ⚠️) | 48.7 | — | 4.2 | Nematollahi 2017 | [[huy2023-egc-pe-pva-hybrid-healing]] §1 |
| Metakaolin PVA-EGC | 33.1 | — | 5.2 | Kan 2020 | [[huy2023-egc-pe-pva-hybrid-healing]] §1 |
| PE-EGC | 93 | — | 3.9 | Zhao 2021 | [[huy2023-egc-activator-pretreatment]] §1 |
| PE-EGC | up to 180 | — | 9 | Lao 2023 | [[huy2023-egc-activator-pretreatment]] §1 |

- Evolution of the CNU AAS composites (Fig. 14 of [[hieu2023-aas-extremely-ductile-22pct]]): ε 4.5% (PVA, 2012) → 7.5% (PE, 2016)
  → 10.7% (PE + CR, 2021) → 22.3% (2023).
- ⚔️ Ohno & Li 2014 ε: 4.3% in the text of [[choi2016-pe-alkali-activated-slag-composite]] and of
  [[huy2023-egc-activator-pretreatment]] (§1), but Fig. 11 of the latter plots 3.40% (probably σ_tu 3.4 MPa plotted as ε) ⚠️.
  → [[gaps]]

## Influencing factors / relationships
- **W/B**: raising W/B from 0.26 to 0.38 lowered σ_tu by 61.3% and ε by 38.9%; the lowest W/B gave the most cracks
  (67.3) and the narrowest cracks (Tables 7–8, §3.3). ⚔️ Same direction as [[sun2019-modified-pva-fiber-ecc]] (whose W/B difference lies within scatter, Fig. 6), opposite to
  [[zhao2022-ecc-tension-damage-model]] and [[chai2023-hdc-ambient-temperature]]. → [[water-binder-ratio]], [[gaps]]
- **Fiber type**: PE (hydrophobic, no chemical bond) replaced PVA because PVA-AAS stayed at ≤ 4.5% (as cited, §1).
  In the hybrid EGC, PE-rich (1.0 PE + 0.5 PVA) mixes gave higher σ_tu and ε than PVA-rich ones, but PVA-rich mixes healed
  better ([[huy2023-egc-pe-pva-hybrid-healing]], Table 5, Figs. 10, 12). → [[hybrid-fiber]]
- **GGBS:FA ratio** (geopolymer EGC): moving from 5.5:4 to 3:6.5 lowered f'c by ≈ 40% and density by ≈ 3.8%, raised ε (PE-rich
  10.51 → 11.99%), widened cracks (100 → 128 µm) and reduced healing ([[huy2023-egc-pe-pva-hybrid-healing]], Tables 4–6, Figs. 3, 10, 12).
  → [[fly-ash]]
- **Matrix weakening** (within one study): the CP activator pretreatment lowered f'c from 31.1 to 20.7 MPa and Km by ≈ 45%,
  while ε rose from 10.97 to 18.62% and σ0 (single-crack, 0.2% PE) fell only 12% ([[huy2023-egc-activator-pretreatment]], Tables 4, 6, 7).
- **Slag**: in cement-based PE-ECC, slag raises strength but widens cracks ([[shumuye2022-slag-fa-pe-ecc]]); the AAS
  composite's ≈ 100 µm average width is consistent with that, qualitatively. → [[ggbfs]]

> Synthesis: the cementless composites sit with Tongji [[uhdc]] (PE, moderate-strength matrix, very high ε) rather than
> with Michigan [[hshdc]] (166 MPa, 3.4–4.2%). With four primary sources (all from one group), the alkali-activated family
> now holds the two highest strain capacities in the wiki (22.34% and 18.62%, both at peak) and a cementless high-strength
> composite (84.3 MPa, 10.51%). The extreme strains come with **wide cracks (170–212 µm)** and, for ED-EGC-CP, a weak
> matrix (20.7 MPa); the high-strength EGC keeps cracks ≈ 100 µm at ≈ 10% strain. Self-healing data now exist (one source);
> durability, shrinkage and structural data still do not.

## Conflicts & open questions
- ⚔️ W/B direction (see above and [[water-binder-ratio]]).
- Open (stated, §3.3): mechanical, physical, chemical and rheological properties must be studied before use as a
  construction material. Literature with fibres other than PVA is limited (§1).
- Open: durability (carbonation of AAS, shrinkage) of alkali-activated SHCC — none in the corpus. Self-healing: one source
  ([[huy2023-egc-pe-pva-hybrid-healing]]) found **limited** autogenous healing in water (crack healing rate 7.4–31.4%) with
  C-(N)-A-S-H as the healing product; sodium-silicate activators seemed unhelpful for healing (p. 8). → [[self-healing]]
- Open (stated): fly-ash ED-EGC has a moderate f'c; adding slag, SF or metakaolin while keeping ductility is left for future work
  ([[huy2023-egc-activator-pretreatment]], Conclusions). Crack widths > 200 µm in ED-AASC ([[hieu2023-aas-extremely-ductile-22pct]],
  Conclusion 2). The effects of sand, CR, the 80 °C step and mixing are not separated in [[hieu2023-aas-extremely-ductile-22pct]].
- ⚔️ Crack width: 172–212 µm in ED-AASC/ED-EGC vs ≈ 100 µm in [[choi2016-pe-alkali-activated-slag-composite]] and the ECC norm.
  → [[crack-width]], [[gaps]]
- PE strength for apparently the same 12 µm × 18 mm fibre: 2700 MPa ([[choi2016-pe-alkali-activated-slag-composite]],
  [[hieu2023-aas-extremely-ductile-22pct]], [[huy2023-egc-activator-pretreatment]]) vs 3030 MPa ([[huy2023-egc-pe-pva-hybrid-healing]],
  Table 3) ⚠️ (different batch or product?).
- To verify: Conclusion 1 σ_tu range "5.06–7.5 MPa" vs Table 7 (5.06–13.06); whether activator powders count in the binder for W/B.

## Related
- [[ggbfs]] · [[pe-fiber]] · [[pva-fiber]] · [[hybrid-fiber]] · [[crumb-rubber]] · [[self-healing]] · [[heat-curing]] · [[fly-ash]] · [[uhdc]] · [[hshdc]] · [[water-binder-ratio]] · [[terminology-hdc-ecc-shcc]] · [[strain-hardening]] · [[mix-designs]]
