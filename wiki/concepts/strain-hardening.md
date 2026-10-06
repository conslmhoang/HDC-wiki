---
type: concept
slug: strain-hardening
aliases: [pseudo strain-hardening, PSH, tensile strain-hardening, strain-hardening criteria, PSH index]
tags: [micromechanics, design-theory]
sources: [ranade2015-hshdc-tensile-rate-effects, su2023-rubber-modified-hshdc, yang2024-hshdc-uniaxial-tension, he2024-hdc-research-advances, ye2021-uhdc-flexural-size-effect]
updated: 2026-10-06
---

# Tensile Strain-Hardening & the PSH Criteria

## Definition
After first cracking, the composite carries **rising** tensile stress while forming
[[multiple-cracking]]. Micromechanics gives two necessary conditions (Kanda & Li 1998, as cited in
[[ranade2015-hshdc-tensile-rate-effects]], p. 97, and [[su2023-rubber-modified-hshdc]], p. 6).

**Strength criterion:** σ_fc ≤ min(σ0)
- PSH_strength = σ0/σ_fc, or σ_tu/σ_fc at composite level.
- Robust cracking needs **> 1.2** (as cited in [[su2023-rubber-modified-hshdc]]).

**Energy criterion:** J_tip ≈ Km²/E ≤ J′b = σ0·δ0 − ∫₀^δ0 σ(δ)dδ
- PSH_energy = J′b/J_tip.
- Robust cracking needs **> 3**.

Both sources compute J_tip with the composite modulus Ec ([[ranade2015-hshdc-tensile-rate-effects]], p. 103;
[[su2023-rubber-modified-hshdc]], p. 9). → [[fiber-bridging]], [[matrix-fracture-toughness]]

He et al. describe HDC design as based on micromechanics and fracture mechanics with fiber bridging
([[he2024-hdc-research-advances]], p. 2).

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

## Key points
- **The PSH indices are necessary but not sufficient.** The 6 mm PE mixes meet both thresholds
  (1.2–1.5 and 27–32) yet fail at the first crack. The authors attribute this to the short embedment
  length (maximum L/2 = 3 mm) ([[su2023-rubber-modified-hshdc]], p. 10). → [[fiber-geometry]]
- PSH_strength correlates positively with ε_tu for individual specimens at every strain rate
  ([[ranade2015-hshdc-tensile-rate-effects]], Fig. 6).
- Rubber or fly ash that lowers σ_fc (Km) raises PSH_strength and ε_tu
  ([[su2023-rubber-modified-hshdc]]; [[yang2024-hshdc-uniaxial-tension]], p. 11). → [[crumb-rubber]], [[fly-ash]]

> Synthesis: In all lineages, ductility is gained by **lowering matrix cracking resistance**
> (rubber, FA, small aggregate) or **raising bridging** (longer or finer PE fiber). The
> very large PSH_energy values (> 100) in the GDUT mixes suggest that the strength criterion and the
> embedment length are the real controls on PE-based HSHDC.

## Conflicts & open questions
- ⚔️ The PSH criteria do not predict the brittle failure of short-fiber mixes → [[gaps]]
- The thresholds (1.2 and 3) come from Kanda & Li 1998, which has not been ingested.

## Related
- [[multiple-cracking]] · [[fiber-bridging]] · [[tensile-strain-capacity]] · [[micromechanical-parameters]]
