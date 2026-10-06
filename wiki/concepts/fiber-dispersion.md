---
type: concept
slug: fiber-dispersion
aliases: [fiber distribution, fiber orientation, effective fiber volume, fiber agglomeration]
tags: [variability, processing]
sources: [ranade2015-hshdc-tensile-rate-effects, ranade2017-hshdc-impact-resistance, su2023-rubber-modified-hshdc]
updated: 2026-10-06
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
- No ingested source measures dispersion in the Chinese HSHDC/UHDC mixes. → [[gaps]]

## Related
- [[fiber-bridging]] · [[fresh-properties]] · [[strain-hardening]]
