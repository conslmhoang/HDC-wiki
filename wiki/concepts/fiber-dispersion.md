---
type: concept
slug: fiber-dispersion
aliases: [fiber distribution, fiber orientation, effective fiber volume, fiber agglomeration]
tags: [variability, processing]
sources: [ranade2015-hshdc-tensile-rate-effects, ranade2017-hshdc-impact-resistance, su2023-rubber-modified-hshdc, chai2023-hdc-ambient-temperature, yang2008-ecc-fiber-bridging-law, kanda2003-sprayed-ecc, kunieda2006-hpfrcc-japan-applications, kunieda2010-uhp-shcc-steel-reinforcement, kanakubo2006-dfrcc-tensile-test-method, chavesfigueiredo2020-printed-shcc, ivaniuk2022-printable-shcc-design, zhong2019-ecc-freeze-thaw, shumuye2022-slag-fa-pe-ecc]
updated: 2026-10-20
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
  is no strain hardening across layers ([[chavesfigueiredo2020-printed-shcc]], Sects. 3.5–3.6, Figs. 17–18).
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

## Related
- [[fiber-bridging]] · [[fresh-properties]] · [[strain-hardening]] · [[3d-printed-hdc]] · [[viscosity-modifying-admixtures]] · [[dogbone-uniaxial-tension]]
