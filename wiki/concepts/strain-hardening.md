---
type: concept
slug: strain-hardening
aliases: [pseudo strain-hardening, PSH, tensile strain-hardening, strain-hardening criteria, PSH index]
tags: [micromechanics, design-theory]
sources: [kanda2006-psh-design-criteria, li1992-steady-state-multiple-cracking, li2002-pva-ecc-interface-tailoring, ranade2015-hshdc-tensile-rate-effects, su2023-rubber-modified-hshdc, yang2024-hshdc-uniaxial-tension, he2024-hdc-research-advances, ye2021-uhdc-flexural-size-effect, zhang2022-hshdcc-review, jin2019-hvfa-shcc-structural, kanda2003-sprayed-ecc, deng2018-hdc-short-columns, shumuye2022-slag-fa-pe-ecc, chavesfigueiredo2020-printed-shcc, gao2020-hdcc-recycled-fine-aggregate, kunieda2010-uhp-shcc-steel-reinforcement, qian2007-shcc-inverse-tensile-strain, mechtcherine2011-shcc-high-strain-rate, homma2009-frcc-self-healing, tabrizikahou2022-masonry-ecc-sma-retrofit, choi2016-pe-alkali-activated-slag-composite, deng2017-rc-column-hdc-jacket, deng2019-urm-shaking-table-hdc, zhang2022-hdc-basalt-textile-tension, yang2009-ecc-self-healing-wet-dry, yun2013-shcc-freeze-thaw, pourfalah2018-ecc-high-temperature, hieu2023-aas-extremely-ductile-22pct, huy2023-egc-activator-pretreatment, huy2023-egc-pe-pva-hybrid-healing]
updated: 2026-10-26
---

# Tensile Strain-Hardening & the PSH Criteria

## Definition
After first cracking, the composite carries **rising** tensile stress while forming
[[multiple-cracking]]. Micromechanics gives two necessary conditions
([[kanda2006-psh-design-criteria]], Eqs. 1–4, p. 60–61).

**Strength criterion:** (σ_fc)_i < σ_peak on every crack plane i
- PSH_strength = σ_peak/(σ_fc)_i, where σ_peak is the peak fiber-bridging stress. The test form is
  σ_peak^test/σ_fc^test, i.e. σ_tu/σ_fc at composite level.

**Energy criterion:** J_tip < J′b = σ_peak·δ_peak − ∫₀^δpeak σ(δ)dδ
- PSH_energy = J′b/J_tip.

**Thresholds** ([[kanda2006-psh-design-criteria]], p. 60, 69–70):

| Condition | PSH_strength | PSH_energy | Applies to |
|---|---|---|---|
| Strain hardening at all | > 1 | > 1 | any |
| Saturated multiple cracking, fiber **pull-out** type | > 1.2 | > 3 | Kanda & Li 1998b, as cited p. 69 |
| Saturated multiple cracking, fiber **rupture** type (e.g. PVA-ECC) | **> 1.3** (test-based > 1.35) | **> 2.7** | Kanda & Li 2006 |

The margins above 1 cover material variability. Both indices must be met at once. The 2006 values
rest on only 4–5 composites (p. 70).

J_tip ≈ Km²/E is the form used by later papers; Kanda & Li 2006 give K_tip = Km·Ec/Em instead.
Both later sources compute J_tip with the composite modulus Ec ([[ranade2015-hshdc-tensile-rate-effects]], p. 103;
[[su2023-rubber-modified-hshdc]], p. 9). → [[fiber-bridging]], [[matrix-fracture-toughness]]

He et al. describe HDC design as based on micromechanics and fracture mechanics with fiber bridging
([[he2024-hdc-research-advances]], p. 2).

**Origin of the criteria:** Li & Leung 1992 stated the steady-state cracking condition as
G_r ≥ 10·G_tip (G_r = area *under* the pre-peak σ–δ curve), together with σ_fc ≤ g·σ0 and a
**flaw-size condition** (c̃ > c̃_mc) ([[li1992-steady-state-multiple-cracking]], Eqs. 14–25). The J′b form
and the saturation thresholds came later: 1.2 / 3 (Kanda & Li 1998b, pull-out type), then 1.3 / 2.7
(Kanda & Li 2006, rupture type). Do not merge the two forms.
→ [[steady-state-cracking]]

## Quantitative evidence
| Source | Mix | σ0 (MPa) | σ_fc (MPa) | PSH_strength | J′b (J/m²) | PSH_energy | Strain hardening? |
|---|---|---|---|---|---|---|---|
| [[ranade2015-hshdc-tensile-rate-effects]] | HSHDC (Michigan), 10⁻⁴ s⁻¹ | — | 8.1 | 1.8 (σ_tu/σ_fc) | 969 | about 39 (computed here: 969/25) | yes, 4.2% |
| same | HSHDC, 10 s⁻¹ | — | 12.4 | 1.71 | about 600 | about 6 or more (stated) | yes, 2.7% |
| [[su2023-rubber-modified-hshdc]] Table 5 | PE6-PR0 (6 mm PE) | 8.5 | 7.3 | 1.2 | 423 | 26.8 | **no**, single crack ⚔️ |
| same | PE12-PR0 | 16.9 | 10.7 | 1.6 | 1761 | 120 | yes, 2.9% |
| same | PE12-PR20 | 19.6 | 7.4 | 2.7 | 2267 | 153 | yes, 4.9% |
| same | PE18-PR0 | 20.7 | 8.8 | 2.1 | 2395 | 155 | yes, 3.8% |
| same | PE18-PR20 | 22.7 | 7.3 | 3.3 | 3110 | 201 | yes, 5.7% |
| [[yang2024-hshdc-uniaxial-tension]] Table 6 | 13 mixes | — | 2.77–3.96 | 1.35–2.44 (σp/σcr) | — | — | PE yes, PVA marginal |
| [[li2002-pva-ecc-interface-tailoring]] Table 4, Fig. 7 | PVA-ECC, oil 0% | — | 3.11 | 1.57 (σ_tu/σ_fc, computed here) | 3.64–6.63 | 0.73–1.33 | weak, 0.99% |
| same | PVA-ECC, oil 0.8% | — | 2.90 | 1.59 (computed here) | 12.5–20.7 | 2.50–4.14 | yes, 3.81%; crack saturation |
| same | PVA-ECC, oil 1.2% | — | 2.92 | 1.51 (computed here) | 24.2–38.1 | 4.84–7.62 | yes, 4.88% |
| [[kanda2006-psh-design-criteria]] Table 4, Figs. 15–16 | 14PVA-27 / 14PVA-42 (14 µm PVA) | — | 3.99 / 2.92 | 1.16 / 1.14 (test) | — | ≈1.1 / n.r. | unsaturated, 0.26 / 0.55% |
| same | 40PVA-27 / 40PVA-42 (40 µm PVA) | — | 2.47 / 1.85 | 1.32 / 1.31 (test) | — | ≈2.4–2.5 / ≈3.0 | 1.03 / 1.50% |
| same | 14PE-27 (PE) | — | 2.25 | 1.44 (test) | — | ≈3.0 | saturated, 5.10% |

- **In the Michigan PVA-ECC the energy index works.** Crack saturation starts as J′b/J_tip reaches
  about 3 (0.8% oil), consistent with the 2.7 rupture-type threshold. The strength ratio (about 1.5–1.8)
  does not separate brittle from ductile mixes there ([[li2002-pva-ecc-interface-tailoring]], p. 471).
- ⚔️ **In Kanda & Li's paste-matrix composites the stress index does separate them:** 1.14–1.16 gives
  0.26–0.55%, 1.31–1.32 gives 1.0–1.5%, and 1.44 gives 5.1% ([[kanda2006-psh-design-criteria]], Table 4).
  Keep both observations; the matrices and fibers differ.
- When f'c rises, J_tip can rise faster than J′b and ductility is lost
  ([[zhang2022-hshdcc-review]], p. 6).
- Flexural deflection-hardening does **not** prove tensile strain-hardening
  ([[zhang2022-hshdcc-review]], p. 9–10).

## Key points
- **The 6 mm PE mixes of Su 2023 fail brittle** although they meet the 1998 thresholds (strength
  1.2–1.5, energy 27–32). The authors attribute this to the short embedment length (maximum
  L/2 = 3 mm) ([[su2023-rubber-modified-hshdc]], p. 10). → [[fiber-geometry]]
  Against the stricter 2006 strength threshold (> 1.3), PE6-PR0 (1.2) **fails**, which partly explains it.
- **Flaw size is not measured anywhere.** Kanda & Li back-calculate a single flaw of about 33 mm that is
  "too large" and use a 0.8 factor on σ_fc; they call for a random, interacting-flaw model
  ([[kanda2006-psh-design-criteria]], p. 67–68). → [[matrix-fracture-toughness]]
- PSH_strength correlates positively with ε_tu for individual specimens at every strain rate
  ([[ranade2015-hshdc-tensile-rate-effects]], Fig. 6).
- Rubber or fly ash that lowers σ_fc (Km) raises PSH_strength and ε_tu
  ([[su2023-rubber-modified-hshdc]]; [[yang2024-hshdc-uniaxial-tension]], p. 11). → [[crumb-rubber]], [[fly-ash]]

> Synthesis: The two PSH indices fail in opposite cases.
> - In PVA-ECC ([[li2002-pva-ecc-interface-tailoring]]) the energy index predicts ductility and the
>   strength ratio does not.
> - In short-PE HSHDC ([[su2023-rubber-modified-hshdc]]) both indices pass the 1998 thresholds, yet
>   the mix is brittle.
>
> Two reasons are plausible: the wrong threshold set was applied (the 2006 strength threshold of 1.3
> would flag PE6), and the flaw-size and fiber-length terms of
> [[li1992-steady-state-multiple-cracking]] are missing from the indices.
>
> Synthesis: In all lineages, ductility is gained by **lowering matrix cracking resistance**
> (rubber, FA, small aggregate) or **raising bridging** (longer or finer PE fiber). The
> very large PSH_energy values (> 100) in the GDUT mixes suggest that the strength criterion and the
> embedment length are the real controls on PE-based HSHDC.

## Round-4 evidence (2026-10-20 ingest)
| Source | Material | Index / criterion | Value | Strain hardening? |
|---|---|---|---|---|
| [[deng2018-hdc-short-columns]], p. 2 | XAUAT PVA-HDC | σ_tu/σ_fc | 6.14/5.73 ≈ 1.07 (computed by the ingest) | yes, serrated plateau at 5.5–6.6 MPa, but "ultimate tensile strain" only ≈ 1% (Fig. 1) |
| [[shumuye2022-slag-fa-pe-ecc]], Table 4, p. 8 | slag/FA PE-ECC, 28 d | σ_tu/σ_fc | 2.02–4.23 | yes, ε about 1.9–3.5% at peak (Fig. 5b) |
| [[kanda2003-sprayed-ecc]], Fig. 2, p. 270–271 | sprayed PVA-ECC design, w/c 0.32 | J′b/J_tip (model) | about 2.0 (≥ 2.7 needs w/c ≥ 0.44) | yes, still strain-hardened |
| [[chavesfigueiredo2020-printed-shcc]], Table 3 | printed PVA-SHCC | J_b > J_tip (flexural-CMOD method) | satisfied for both mixes (units ⚠️) | weak: ε 0.15–0.31% at peak (35 d) |
| [[gao2020-hdcc-recycled-fine-aggregate]], §3.3 | HDCC, 0.5% PVA | first-cracking strength criterion (Li 2001, as cited) | bridging < cracking strength | **no** multiple cracking |
| [[kunieda2010-uhp-shcc-steel-reinforcement]], §1 | UHP-SHCC | post-cracking strength > cracking strength (Matsumoto & Mihashi 2002, as cited) | met in dumbbells | yes in dumbbells; **no** in unreinforced 50 mm members |

- ⚔️ **A third strength threshold.** [[jin2019-hvfa-shcc-structural]] (§2.2) quotes PSH targets of
  **σ0/σ_fc > 1.45** and J′b/J_tip > 3 for PVA-SHCC, attributed to Kanda & Li 1998. The wiki records 1.2
  (Kanda & Li 1998b, pull-out type) and 1.3 (Kanda & Li 2006, rupture type) from [[kanda2006-psh-design-criteria]].
  Jin's 1.45 may be a mis-quote or a different index; the original 1998 paper is not ingested ⚠️. Jin does not
  compute the indices for his own mixes. → [[gaps]]
- **Energy margin 2.7 confirmed independently:** Kanda & Li 2002 (Japanese, as cited in
  [[kanda2003-sprayed-ecc]], p. 270) suggest J′b/J_tip ≈ 2.7 for "matured" PSH, the same as the 2006 rupture-type
  threshold. Kanda 2003 nevertheless chose w/c 0.32 at about 2.0 for sprayability and still got strain hardening.
- **XAUAT PVA-HDC sits just above 1.** Its stress index (≈ 1.07, below every published threshold) is consistent
  with its modest ε_tu ≈ 1% ([[deng2018-hdc-short-columns]]).
- **Meeting J_b > J_tip is not enough in printed SHCC:** both printed mixes pass the energy check yet reach only
  0.15–0.31% strain. The authors blame air voids, less water and HPMC ([[chavesfigueiredo2020-printed-shcc]],
  §3.4.1, 3.6). → [[3d-printed-hdc]], [[viscosity-modifying-admixtures]]
- **Slag and age reduce the hardening margin** in PE-ECC (more slag, longer curing → less strain hardening, except
  SF-5-55) ([[shumuye2022-slag-fa-pe-ecc]], §3.2). ⚠️ The text and the reported strains disagree on which mix is most
  ductile (see that source page). → [[ggbfs]]
- **Conceptual statistical model** ([[kunieda2010-uhp-shcc-steel-reinforcement]], Fig. 2): strain capacity is set by
  the overlap of the matrix-cracking-strength and bridging-strength distributions along the member. Distributed
  cracking needs P_u ≥ about 1.5 P_cr (§4.4). Light steel (ρs 0.3%) restores hardening in thick members
  (ε 1.58 vs 0.24%, Table 3). → [[multiple-cracking]], [[size-effect]]
- **Artificial flaws** with a prescribed size distribution give more saturated cracking and more consistent ε_tu
  (Wang & Li 2004, as cited in [[qian2007-shcc-inverse-tensile-strain]], p. 235). This is the practical form of
  the flaw-size condition of [[steady-state-cracking]].
- ⚔️ **Bond vs ductility (recycled fine aggregate).** Gao 2020 infers *higher* PVA bond in R-HDCC (SEM: stripped
  fiber surfaces, Fig. 16) together with *higher* ductility (ε_tp 4.76% vs 1.68% at 2% PVA, Table 6), against the
  low-bond rule of [[li2002-pva-ecc-interface-tailoring]] (oiling lowers bond and raises ε 0.99 → 4.88%). No
  pull-out data exist; a possible reason is that the river-sand N-HDCC has bond *below* the optimum, or that RFA
  acts through finer flaws ("crack trapping") rather than bond ([[gao2020-hdcc-recycled-fine-aggregate]], §3.3, Fig. 14).
  → [[recycled-fine-aggregate]], [[fiber-matrix-interface]], [[gaps]]
- **Strain hardening can vanish at high rate.** PVA-SHCC shows no visible multiple cracking at ≥ 10 s⁻¹
  ([[mechtcherine2011-shcc-high-strain-rate]], p. 58–59). → [[strain-rate-effects]]
- **Materials that do not strain-harden:** FRCC(PE) in [[homma2009-frcc-self-healing]] is strain-softening; the
  "ECC" in the FE model of [[tabrizikahou2022-masonry-ecc-sma-retrofit]] softens from 1.45 MPa (Table 5). Do not
  use them as HDC evidence. → [[terminology-hdc-ecc-shcc]]

> Synthesis: the strength index now has three quoted thresholds (1.2, 1.3, 1.45), and the measured values span
> 1.07 (XAUAT PVA-HDC, ≈ 1%) to 4.2 (slag/FA PE-ECC, 2–3.5%). Across the round-4 sources, higher σ_tu/σ_fc goes
> with higher strain, but processing (printing, spraying, member thickness, strain rate) can remove hardening even
> when the micromechanical indices pass. The PSH indices are necessary, not sufficient, at member scale.

## Round-5 evidence (2026-10-21)
- **"Stress performance index" ≠ PSH strength index.** [[choi2016-pe-alkali-activated-slag-composite]] reports σ_tu/σ_fc 1.50–2.68 (rising with
  crack count, 46–67 cracks) and calls it a "stress performance index", but it uses the measured peak tensile stress, not
  the bridging capacity σ0 (Kanda & Li). Values are not comparable with σ0/σ_fc rows in [[micromechanical-parameters]].
  No aggregate was used, to keep matrix toughness low (§2.1). → [[alkali-activated-binder]]
- **Strain hardening survives some exposures but not others**: kept after 300 F-T cycles in hybrid PVA + PE SHCC, with
  slightly lower strain and loss of flexural multiple cracking ([[yun2013-shcc-freeze-thaw]], Figs. 6, 8); kept on
  reloading after wet–dry self-healing (ε 1.7–3.1% / 0.8–2.2%, [[yang2009-ecc-self-healing-wet-dry]], p. 388); lost in hot
  bending from 150 °C (one crack, PVA pull-out) ([[pourfalah2018-ecc-high-temperature]], Fig. 10d). → [[freeze-thaw]],
  [[self-healing]], [[high-temperature-behaviour]]
- **Fiber grade switches the ductility class** in the same XAUAT HDC mix: ≈ 3.0% (Japanese PVA, 1600 MPa) vs ≈ 1.2%
  (Chinese PVA, 1200 MPa) ([[deng2017-rc-column-hdc-jacket]], Fig. 1a ⚠️ read). XAUAT tests HDC tension per the Shaanxi
  standard DBJ61/T112-2016 ([[deng2019-urm-shaking-table-hdc]], p. 3). → [[pva-fiber]]
- **Short fibres + textile**: with ≥ 1.5% PVA, basalt-textile-reinforced HDC shows multiple cracking up to peak, although
  plain HDC dogbones reach only 0.12–0.45% ([[zhang2022-hdc-basalt-textile-tension]], §3.1, Table 8). → [[textile-reinforced-hdc]]

## Round-7 evidence (2026-10-26): cementless CNU composites
- **First measured PSH indices for a geopolymer composite**: fly-ash ED-EGC, Km 0.11 / 0.06 MPa√m, J_tip 1.25 / 0.62 J/m²,
  J′b 64.8 / 57.5 J/m² at 0.2 vol.% PE (single-crack test) ([[huy2023-egc-activator-pretreatment]], Tables 6–7).
  - PSH_E = J′b/J_tip after scaling J′b by ×8.75 (1.75/0.2 vol.%) = **452 (WP) / 817 (CP)**, far above the 2.7 threshold quoted
    from Kanda & Li 2006 and out of scale with every other row in [[micromechanical-parameters]] (≤ ≈ 200). ⚠️ The ×8.75
    proportional scaling is inconsistent with the measured composite: scaled σ0 (12.7 / 11.2 MPa) exceeds fts (8.72 / 5.54 MPa),
    so the PSH_E values are likely inflated (§3.2).
  - PSH_S is taken as fts/fcs (σ0 set = fts), i.e. a macroscopic ratio as in [[choi2016-pe-alkali-activated-slag-composite]]:
    1.87 / 1.63 (computed here). The authors state that PSH_E tracks ε better than PSH_S (§3.2, Table 7).
- **Macroscopic SPI in HSUD-EGC**: σ_tu/σ_fc 1.79 / 1.57 / 1.92 / 1.62 (S-PE / S-PVA / F-PE / F-PVA, computed from Table 5);
  F mixes slightly higher ([[huy2023-egc-pe-pva-hybrid-healing]], §3.1.2). EPI not measured.
- **Minimum condition fts > fcr** with saturated multiple cracking (66–86 cracks in 80 mm) gives 22.34% at peak in ED-AASC;
  more cracks ↔ higher ε ([[hieu2023-aas-extremely-ductile-22pct]], Table 6, §3.1). fts/fcr is 1.56 / 1.62 / 1.99 for M0 / M1 / M2
  (computed from Table 4), so the mix with the highest ε (M1) does not have the highest ratio.
- **Processing, not only design**: identical ED-AASC proportions gave 9.81% (M0) or 22.34% (M1) depending on mixing
  ([[hieu2023-aas-extremely-ductile-22pct]], Table 4). → [[fiber-dispersion]]
- **Trade-off within one study**: weakening the ED-EGC matrix (CP pretreatment) lowered f'c 31.1 → 20.7 MPa and raised ε
  10.97 → 18.62% ([[huy2023-egc-activator-pretreatment]], Table 4); a GGBS-rich HSUD-EGC keeps 10.51% at 84.3 MPa
  ([[huy2023-egc-pe-pva-hybrid-healing]], Table 5, Fig. 3). → [[gaps]]

## Conflicts & open questions
- ⚔️ The PSH criteria do not fully predict the brittle failure of short-fiber mixes → [[gaps]]
- ⚔️ PSH strength threshold: 1.2 (1998b) / 1.3 (2006) vs 1.45 (as quoted by [[jin2019-hvfa-shcc-structural]]) → [[gaps]]
- ⚔️ Higher bond with higher ductility in R-HDCC ([[gao2020-hdcc-recycled-fine-aggregate]]) vs the low-bond design rule → [[gaps]]
- Papers in the corpus quote "1.2 and 3" for all fiber types. Kanda & Li 2006 restrict those to
  pull-out type fibers. Check which set a paper uses before comparing.
- Kanda & Li 1998b (the pull-out thresholds) has not been ingested.
- ⚠️ PSH_E 452–817 in [[huy2023-egc-activator-pretreatment]] rests on proportional scaling of single-crack J′b from 0.2 to
  1.75 vol.%; treat as an upper bound. → [[single-crack-test]]

## Related
- [[multiple-cracking]] · [[alkali-activated-binder]] · [[fiber-bridging]] · [[tensile-strain-capacity]] · [[micromechanical-parameters]] · [[steady-state-cracking]] · [[recycled-fine-aggregate]]
