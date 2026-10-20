---
type: material
slug: viscosity-modifying-admixtures
aliases: [VMA, HPMC, hydroxypropyl methylcellulose, cellulose ether, starch ether, viscosity agent, SAP, superabsorbent polymer]
tags: [admixture, fresh, printing, processing]
sources: [chavesfigueiredo2020-printed-shcc, ivaniuk2022-printable-shcc-design, sun2019-modified-pva-fiber-ecc, bu2022-ecc-chloride-crack-width, homma2009-frcc-self-healing, mechtcherine2011-shcc-high-strain-rate, kanda2003-sprayed-ecc, choi2016-pe-alkali-activated-slag-composite]
updated: 2026-10-21
---

# Viscosity-Modifying Admixtures (HPMC, cellulose and starch ethers; SAP)

## Definition
Water-soluble polymers, mainly cellulose ethers such as HPMC, and starch ethers. They raise paste viscosity and water
retention so that fibers stay suspended and the mix holds its shape (printing, spraying). Superabsorbent polymer (SAP) is
listed here as a related polymer admixture with a different purpose (internal curing, flaws).

## Key points
- VMAs appear in most PVA- and PE-SHCC mixes in round 4, but **no source varies the VMA dose and measures ε_tu**.

## Quantitative evidence
| Source | Material | Admixture and dosage | Reported effect |
|---|---|---|---|
| [[ivaniuk2022-printable-shcc-design]] Sects. 2.1, 3.1, 3.2.3 | printable PE-SHCC | cellulose ether 0.075% of binder; starch ether | spread loss after 3 h: Ref 12.7%, starch ether 10.9%, starch + cellulose ether 5.5%; cellulose ether gave the highest water retention and longest open time; starch ether alone lost retention by 20 min; surface roughness Sa 772 → 411 µm (Fig. 15); ethers forced W/B 0.212 → 0.250, which lowered σ_tu by 24% |
| [[chavesfigueiredo2020-printed-shcc]] Sects. 3.5–3.6 | printed PVA-SHCC | HPMC about 0.3–0.4 wt.% (basis ⚠️) | may raise air voids and act as internal curing; authors blame air voids, low water and HPMC for the strain loss of printed vs cast SHCC (0.15–0.31%) |
| [[sun2019-modified-pva-fiber-ecc]] Tables 6–7, §3.1 | PVA-ECC | HPMC 5 × 10⁴ mPa·s (dosage unclear ⚠️) + 1.8% PCE | spread 325 mm, lowest thixotropy (9911 Pa·s⁻¹ at 1 min); more or higher-viscosity HPMC raises initial viscosity; shear breaks HPMC chains |
| [[bu2022-ecc-chloride-crack-width]] Table 1 | PVA-ECC | HPMC 0.5 kg/m³ | mix ingredient only |
| [[homma2009-frcc-self-healing]] Tables 1–2 | FRCC | cellulose VMA | mix ingredient only |
| [[mechtcherine2011-shcc-high-strain-rate]] Table 1, p. 52 | PVA-SHCC | viscosity agent 3.20 kg/m³; **SAP 2.02 kg/m³** | SAP used to reduce autogenous shrinkage, improve frost resistance and introduce micro-defects that trigger multiple cracking |
| [[kanda2003-sprayed-ecc]] p. 272 | sprayed ECC | urethane moisturizing agent 0.8% of binder | aids anti-segregation and flow but entrains > 20% air |

## Influencing factors / relationships
- **Water demand:** thickening ethers raise water demand, and the extra water can cost tensile strength
  ([[ivaniuk2022-printable-shcc-design]]). → [[water-binder-ratio]]
- **Air:** both HPMC ([[chavesfigueiredo2020-printed-shcc]]) and urethane agents ([[kanda2003-sprayed-ecc]]) entrain air.
  In printing, high air content hinders fiber orientation and lowers ductility. → [[fiber-dispersion]]
- **Artificial flaws:** SAP voids act as deliberate flaws (Mechtcherine), the same idea as flaw tailoring for
  [[multiple-cracking]]. → [[matrix-fracture-toughness]]
- As cited: printable ECC with about 4% strain using HPMC and calcium aluminate cement (Soltan & Li 2018, as cited in
  [[chavesfigueiredo2020-printed-shcc]], Sect. 1). → [[3d-printed-hdc]]

> Synthesis: VMAs are an enabling admixture for spraying and printing HDC, but every source that reports a side effect
> points the same way: more air and/or more water, which costs strength or ductility. The dose–ductility relation is an
> open question.

## Conflicts & open questions
- Effect of starch and cellulose ethers on the shrinkage of printed SHCC is unknown (stated gap,
  [[ivaniuk2022-printable-shcc-design]], Conclusions). → [[shrinkage]], [[gaps]]
- HPMC dosage bases are unclear in [[chavesfigueiredo2020-printed-shcc]] and [[sun2019-modified-pva-fiber-ecc]] ⚠️.

## Alkali-activated binder (2026-10-21)
- In a cementless alkali-activated slag + 1.75% PE composite, VMA (0–0.0003) and HRWRA (0.024 → 0.002, by binder mass)
  were tuned per W/B (0.26–0.38) after the Li & Li 2013 viscosity-control approach, to keep PE uniformly dispersed;
  hardened densities were within 0.5% of theoretical ([[choi2016-pe-alkali-activated-slag-composite]], Table 1, §2.1, §3.1).
  → [[alkali-activated-binder]], [[fiber-dispersion]]

## Related
- [[fresh-properties]] · [[fiber-dispersion]] · [[3d-printed-hdc]] · [[water-binder-ratio]] · [[heat-curing]] · [[mix-designs]]
