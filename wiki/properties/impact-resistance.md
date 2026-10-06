---
type: property
slug: impact-resistance
aliases: [drop-weight impact, repeated impact, punching resistance, peak contact force, PCF]
tags: [dynamic, extreme-loading]
sources: [ranade2017-hshdc-impact-resistance, he2024-hdc-research-advances]
updated: 2026-10-06
---

# Impact Resistance

## Quantitative evidence
Unreinforced 300 × 300 × 25 mm slabs, 16.04 kg drop weight, 75 mm head, up to 20 impacts,
2 slabs per case ([[ranade2017-hshdc-impact-resistance]], Table 3–4, p. 28–31):

| Velocity (m/s) | HSHDC | Cor-Tuf (FR-UHPC) | First-impact PCF (kN), HSHDC / Cor-Tuf |
|---|---|---|---|
| 2.30 | survived 20 impacts | survived | 57 / 64 |
| 3.25 | survived 20; PCF about constant | flexural failure before 20 (one slab survived with low PCF) | 77 / 87 |
| 4.60 | survived 20 | flexural failure | 103 (the text says about 110 ⚠️) / 105 |

- **50 mm head:** Cor-Tuf failed by punching shear at impact 15. HSHDC showed no punching (p. 30).
- **Damage pattern:** HSHDC showed fine radial cracks and almost no spalling. Cor-Tuf formed 4
  yield-line cracks, spalled, and broke into 4 pieces. → [[multiple-cracking]]
- **FE model** (LS-Dyna): displacement error below 13%; PCF over-predicted by 34–75%; impulse matches
  (Table 4). → [[tensile-constitutive-model]]
- **Moderate-velocity impact** gives strain rates of about 0.1–10 s⁻¹ (stated, not measured, p. 26).
  → [[strain-rate-effects]]
- **EDGC tensile impact:** 8 mm PVA outperformed 13 mm PVA (as cited in
  [[he2024-hdc-research-advances]], p. 9).

> Synthesis: In these tests, the first-impact peak force is similar for both materials, but
> **damage tolerance** (repeated impacts, no punching or spalling) comes from tensile ductility,
> not from compressive strength.

## Conflicts & open questions
- No energy-absorption value is quantified. Only 2 slabs per case. Slabs are unreinforced.
- Strain rates of 10²–10³ s⁻¹ (blast, projectiles) are untested. → [[gaps]]

## Related
- [[impact-test]] · [[extreme-loading-applications]] · [[uhpc-vhsc]] · [[hshdc]]
