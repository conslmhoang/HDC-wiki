---
type: property
slug: shrinkage
aliases: [drying shrinkage, autogenous shrinkage, chemical shrinkage, restrained shrinkage]
tags: [durability, volume-stability]
sources: [ma2021-ecc-durability-review, vanzijl2010-shcc-durability, kunieda2006-hpfrcc-japan-applications, kunieda2010-uhp-shcc-steel-reinforcement, mechtcherine2011-shcc-high-strain-rate, ivaniuk2022-printable-shcc-design]
updated: 2026-10-20
---

# Shrinkage

Part of the [[durability]] hub. No primary shrinkage *measurement* study is ingested yet; the values below
are second-hand, except the restrained-shrinkage effect in [[kunieda2010-uhp-shcc-steel-reinforcement]].

## Key points (as cited in [[ma2021-ecc-durability-review]], p. 6–7)
- **ECC shrinks more than concrete.** 28-d shrinkage is 1200–1800 µε for ECC vs 400–800 µε for
  plain concrete (Yang 2007). The cause is the high binder content and the absence of coarse aggregate.
- **Low-shrinkage ECC** reaches 109–242 µε at about 2.5% strain (Zhang 2013).
- **Effect of composition** (Gao 2018): shrinkage rises with W/B, falls with sand/binder ratio and
  FA, and shows no clear effect of fiber volume. → [[fly-ash]], [[water-binder-ratio]]
- In high-strength ECC, chemical shrinkage dominates (Ye 2019, Fig. 12).
- **Mitigation:**
  - 20% saturated lightweight aggregate: autogenous shrinkage −67%, drying −37%, but lower ductility (Sahmaran 2009).
  - Zeolite: drying shrinkage −55% or more (Wang 2020).

## Further evidence (other sources)
| Source | Condition | Value / finding | Note |
|---|---|---|---|
| Wang & Li 2006, as cited in [[vanzijl2010-shcc-durability]] | restrained SHCC drying at 40–60% RH | shrinkage strains SHCC into multiple cracking (fine cracks rather than one wide crack) | Fig. 6, p. 267 |
| as cited in [[vanzijl2010-shcc-durability]] | autogenous, sealed | 0.033% at 2 d, 0.072% at 47 d; setting ≈11 h | p. 267 |
| [[kunieda2010-uhp-shcc-steel-reinforcement]] (UHP-SHCC, reinforced members) | internal steel bars restrain shrinkage | cracking load 42 → 36 kN as ρs rises 0 → 1.2%; only ≈3% loss at 0.6% | §4.3, primary |
| [[kunieda2006-hpfrcc-japan-applications]] (HPFRCC) | composite repair systems | restrained shrinkage may lower usable tensile capacity even if cracks stay fine; low-shrinkage materials recommended | p. 24 |
| [[kunieda2006-hpfrcc-japan-applications]] (field, as cited) | irrigation channels, 6–10 mm sprayed HPFRCC | reference mortars cracked within 1 month, HPFRCC did not | p. 27 → [[repair-and-field-applications]] |
| [[mechtcherine2011-shcc-high-strain-rate]] (SHCC, TU Dresden) | SAP 2.02 kg/m³ | added to reduce autogenous shrinkage (and as frost / crack-initiating micro-defects); shrinkage not measured | p. 52 |
| [[ivaniuk2022-printable-shcc-design]] (printable SHCC) | cellulose / starch ethers as VMAs | lower shrinkage *expected*; not measured — stated as future work | Sections 2.1, 4 → [[viscosity-modifying-admixtures]] |

> Synthesis: in ECC/SHCC, restrained shrinkage turns into distributed fine cracking rather than a single
> wide crack, but it consumes part of the tensile strain capacity before any mechanical load. For thin
> repair overlays and reinforced members, the strain budget left for service loads is therefore smaller than
> the dogbone ε_tu. → [[tensile-strain-capacity]], [[repair-and-field-applications]]

## Conflicts
- ⚔️ Effect of W/B (both as cited, p. 6): Gao 2018 finds shrinkage *rises* with W/B; Ye 2019 finds
  total shrinkage *falls* as W/B and s/b rise. → [[gaps]]
- Open: no primary shrinkage data for Chinese HDC, PE-HSHDC or printed SHCC; early-age cracking of large
  SHCC elements ([[vanzijl2010-shcc-durability]], p. 267).

## Related
- [[durability]] · [[water-binder-ratio]] · [[fly-ash]] · [[crack-width]] · [[repair-and-field-applications]]
