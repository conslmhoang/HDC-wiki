---
type: concept
slug: fiber-dispersion
aliases: [fiber distribution, fiber orientation, effective fiber volume, fiber agglomeration]
tags: [variability, processing]
sources: [ranade2015-hshdc-tensile-rate-effects, ranade2017-hshdc-impact-resistance, su2023-rubber-modified-hshdc, chai2023-hdc-ambient-temperature, yang2008-ecc-fiber-bridging-law, kanda2003-sprayed-ecc, kunieda2006-hpfrcc-japan-applications, kunieda2010-uhp-shcc-steel-reinforcement, kanakubo2006-dfrcc-tensile-test-method, chavesfigueiredo2020-printed-shcc, ivaniuk2022-printable-shcc-design, zhong2019-ecc-freeze-thaw, shumuye2022-slag-fa-pe-ecc, choi2016-pe-alkali-activated-slag-composite, yun2013-shcc-freeze-thaw, hieu2023-aas-extremely-ductile-22pct]
updated: 2026-10-26
---

# Fiber Dispersion & Orientation

## Definition
How evenly fibers are distributed (fibers per section) and how they are oriented. Together these
set the section-to-section variation in bridging capacity, and therefore min(σ0).

## Key points
- **Minimum effective Vf:** the scale-linking analysis uses min(Vf) = 0.80 × 2%. This comes from
  fluorescence microscopy (mean minus 2 SD) ([[ranade2015-hshdc-tensile-rate-effects]], p. 101).
- **Thin elements give 2-D orientation.** Thin slabs likely produce a 2-D fiber orientation,
  which bridges cracks better than the 3-D orientation in beams or columns. Casting in layers can
  leave fiber-poor interlayers ([[ranade2017-hshdc-impact-resistance]], p. 30–31).
  FE input data should come from specimens sawn out of the actual element (p. 35).
- **Agglomeration at high rubber content.** Above about 35 vol.% powder rubber, excessive plastic
  viscosity causes fibers to clump and ductility drops. Moderate rubber content may help
  dispersion ([[su2023-rubber-modified-hshdc]], p. 7, 9). → [[crumb-rubber]], [[fresh-properties]]

## Conflicts & open questions
- Chinese PVA-HDC: dispersion coefficient α = 0.91 from 60 fluorescence images ([[chai2023-hdc-ambient-temperature]], §3.2, Eq. 1).
  No ingested source measures dispersion in the Chinese HSHDC/UHDC mixes. → [[gaps]]

## Plane-to-plane variation
- Yang et al. infer ±25% variation of bridging Vf from σ_tu, without measuring it; 2-D random
  orientation is justified when specimen thickness (13 mm) ≈ fiber length (12 mm) ([[yang2008-ecc-fiber-bridging-law]], p. 187, 191).


## Round 4 evidence (2026-10-20)
### Element thickness, placement and casting direction
- **Spraying:** thin sprayed layers give 2-D orientation and higher σ_tu and ε than placed specimens; the effect is weak in
  thick sprays ([[kanda2003-sprayed-ecc]], p. 276–277). Fiber balls jamming the pump were the barrier to wet-spraying ECC
  at 1–2 vol.% (p. 269); a concrete-mixer route gave low viscosity and fiber balls until mixing was changed (p. 274).
- **Thin vs thick members:** about 2-D orientation in 13 mm dumbbells vs 3-D in 50 mm members, which lowers bridging
  capacity ([[kunieda2010-uhp-shcc-steel-reinforcement]], §4.1). Thin sections, spraying and extrusion give 2-D orientation;
  design tensile properties should reflect actual placement ([[kunieda2006-hpfrcc-japan-applications]], p. 21).
- **Casting direction (JCI round robin):** horizontal casting gave higher σ and ε than vertical for PVA and the PE–steel
  hybrid, but the reverse for PE ([[kanakubo2006-dfrcc-tensile-test-method]], p. 8–9, Table 7). The same PVA-DFRCC gave
  2.70% (thin plate) vs 0.07% (Ø70 dogbone) strain at peak (Tables 6, 8).

### 3D printing
- Printed PVA-SHCC: µCT shows mainly **diagonal** fiber orientation, attributed to layer-pressing shear and nozzle
  movement; high air-void content hinders orientation and lowers ductility; few fibers cross the layer interface, so there
  is no strain hardening across layers ([[chavesfigueiredo2020-printed-shcc]], Sects. 3.5–3.6, Figs. 17–18). Read from the
  Fig. 17 histogram (p. 19): peaks at ≈ 40° (≈ 9% X, ≈ 8% Y) and ≈ 170°, minimum at ≈ 90° (≈ 1.5–2%), ≈ 2.5–3.5% at 0/180°.
  Void area ≈ 12–14% in X layers, ≈ 10% at the X interface, ≈ 2–7% in Y (Figs. 15–16, pp. 17–18).
- Printed PE-SHCC: high fiber content raises clumping risk and surface unevenness, partly solved by the mixing procedure
  and a trowelled nozzle; DIC crack patterns were read as good distribution along the print direction
  ([[ivaniuk2022-printable-shcc-design]], Sect. 2.1, Fig. 18).
- ⚔️ Print orientation: Ivaniuk et al. assume fibers align with the print direction (citing Li et al. 2020), while
  Chaves Figueiredo et al. measured mainly diagonal orientation. Different fibers (PE vs PVA), nozzles and mixes. → [[gaps]], [[3d-printed-hdc]]

### Mix effects
- 2.0 vol.% PVA (13 mm) lowered density and frost indices relative to 1.5%, attributed to dispersion
  ([[zhong2019-ecc-freeze-thaw]], §3.5).
- Spherical fly ash aids fiber dispersion (authors' claim, [[shumuye2022-slag-fa-pe-ecc]], Sect. 3.5.1). → [[fly-ash]]
- Viscosity-modifying admixtures are used partly to keep fibers suspended → [[viscosity-modifying-admixtures]].

## Round-5 evidence (2026-10-21)
- **Viscosity control for PE**: HRWRA and VMA tuned per W/B after Li & Li 2013 in a cementless alkali-activated slag
  paste; measured densities within 0.5% of theoretical → no unintended pores; all four mixes strain-hardened
  ([[choi2016-pe-alkali-activated-slag-composite]], §2.1, §3.1). → [[alkali-activated-binder]], [[viscosity-modifying-admixtures]]
- **PE multifilament** is hard to disperse in PVA + PE hybrids, raising air content (up to 13.1%) and lowering f'c
  ([[yun2013-shcc-freeze-thaw]], p. 13–14, Table 3). → [[hybrid-fiber]]

## Round-7 evidence (2026-10-26): mixing procedure as the only variable
- [[hieu2023-aas-extremely-ductile-22pct]] made one ED-AASC mix (1.75% PE, 18 L planetary mixer) with three procedures (Fig. 3):
  - **M0** (earlier procedure): dry 1 min 90 rpm → liquids 1 min 90 + 3 min 180 rpm → PE 15 min 270 rpm → ε **9.81 ± 2.92%**.
  - **M1**: dry 3 min 180 rpm → liquids 3 min 270 + 7 min 360 rpm → PE 3 min 270 + 15 min 360 rpm (≈ 31 min) → **22.34 ± 0.48%**.
  - **M2**: solids + PE dry-mixed 5 min 180 rpm → liquids 3 min 270 + 20 min 360 rpm → **20.89 ± 2.13%**.
  (all at peak, 28 d; Table 4). f'c (52.2–54.6 MPa) and density (2.25–2.26 g/cm³) were unchanged (Fig. 7).
- The authors attribute the 2.2–2.3× gain and the lower COV to better homogeneity and fibre distribution (citing Li & Li 2013
  on dispersion and COV), but **dispersion was not measured** (no image analysis or rheology) (§3.1).
- A high SP dose (0.106 liquid PCE) was needed for rheology and dispersion; it delayed hydration (demoulding at 11 d) (§2.1, §2.2.2).

> Synthesis: this is the clearest evidence in the wiki that processing alone can more than double ε at fixed proportions.
> Reported ε values from different labs may therefore differ through mixing energy as much as through mix design;
> mixing procedures should be recorded with any tensile result. → [[tensile-strain-capacity]], [[gaps]]

## Related
- [[fiber-bridging]] · [[fresh-properties]] · [[strain-hardening]] · [[3d-printed-hdc]] · [[viscosity-modifying-admixtures]] · [[dogbone-uniaxial-tension]] · [[alkali-activated-binder]]
