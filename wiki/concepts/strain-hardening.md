---
type: concept
slug: strain-hardening
aliases: [pseudo strain-hardening, PSH, tensile strain-hardening, strain-hardening criteria, PSH index]
tags: [micromechanics, design-theory]
sources: [kanda2006-psh-design-criteria, li1992-steady-state-multiple-cracking, li2002-pva-ecc-interface-tailoring, ranade2015-hshdc-tensile-rate-effects, su2023-rubber-modified-hshdc, yang2024-hshdc-uniaxial-tension, he2024-hdc-research-advances, ye2021-uhdc-flexural-size-effect, zhang2022-hshdcc-review]
updated: 2026-10-20
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

## Conflicts & open questions
- ⚔️ The PSH criteria do not fully predict the brittle failure of short-fiber mixes → [[gaps]]
- Papers in the corpus quote "1.2 and 3" for all fiber types. Kanda & Li 2006 restrict those to
  pull-out type fibers. Check which set a paper uses before comparing.
- Kanda & Li 1998b (the pull-out thresholds) has not been ingested.

## Related
- [[multiple-cracking]] · [[fiber-bridging]] · [[tensile-strain-capacity]] · [[micromechanical-parameters]]
