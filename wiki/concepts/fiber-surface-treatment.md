---
type: concept
slug: fiber-surface-treatment
aliases: [oil coating, oiling agent, fiber coating, plasma treatment, interface tailoring, VAE emulsion, polymer emulsion coating, boric anhydride treatment]
tags: [interface, design-variable]
sources: [li2002-pva-ecc-interface-tailoring, zhang2022-hshdcc-review, yu2018-ecc-direct-tensile-review, sun2019-modified-pva-fiber-ecc, vanzijl2010-shcc-durability]
updated: 2026-10-20
---

# Fiber Surface Treatment (interface tailoring)

## Key points
- **PVA needs its bond weakened.** Its hydroxyl groups bond so strongly that the fibers rupture.
  Off-the-shelf PVA gave only 0.5–1.0% strain even at 4% fiber (as cited in
  [[li2002-pva-ecc-interface-tailoring]], p. 463–464).
- **Oil coating** (about 100 nm thick) from 0 to 1.2% by fiber mass
  ([[li2002-pva-ecc-interface-tailoring]], Tables 3–4):

  | Oil (%) | τ0 (MPa) | Gd (J/m²) | ε_tu (%) | Crack width (µm) |
  |---|---|---|---|---|
  | 0 | 2.44 | 4.71 | 0.99 | 43 |
  | 0.3 | 2.15 | 3.16 | 1.55 | 44 |
  | 0.5 | 2.14 | 2.96 | 2.73 | 52 |
  | 0.8 | 1.98 | 2.18 | 3.81 | 71 |
  | 1.2 | 1.11 | 1.61 | **4.88** | 88 |

  Commercial PVA for ECC uses 0.8–1.2% oil ([[yu2018-ecc-direct-tensile-review]], p. 347).
  The durability of the oil coating is unknown (p. 359).
- **PE needs its bond strengthened.** It has almost zero chemical bond. Coatings raise bond
  strength: CNF +22%, GO +71.2%, PDA +90%. Chromic-acid, plasma and ozone treatments lower fiber
  strength (as cited in [[zhang2022-hshdcc-review]], p. 5–6).
- **Too much bond backfires:** in HSHDCC the highest σ_tu came with the lowest ε_tu and about twice
  as many ruptured fibers ([[zhang2022-hshdcc-review]], p. 12).

## Polymer-emulsion and boric treatments of PVA (2026-10-20 ingest)
Wuhan Univ. of Technology tested three post-treatments of PVA fibers in a W/B 0.35 PVA-ECC (2 vol.%, 12 mm)
([[sun2019-modified-pva-fiber-ecc]], §2.2, Tables 8, 10, 11):

| Mix | Fiber / treatment | σ_tu (MPa) | ε (%) | f'c 28 d (MPa) | Note |
|---|---|---|---|---|---|
| S4 / C1 | REC-15 (Kuraray), untreated | 3.3 (7 d) / 3.3 (28 d) | 3.21 (7 d) / 1.39 (28 d) | 40.6 | reference |
| S2 / C2 | REC-15 + **VAE emulsion** (50 g diluted to 400 mL, 10 min ultrasonic soak, dried) | 3.33 / 3.4 | **4.05** (7 d, +26.2%) / 2.18 (28 d) | 42.6 | best |
| C3 | REC-15 + boric anhydride + cement slurry | — | — | **34.2** | matrix weakened |
| S3 | REC-15 + boric anhydride + SB emulsion | 2.83 (7 d) | 2.02, **softening** | — | bond too weak |
| G1 → G2 | domestic PVA (31 µm), untreated → treated | 2.86 → 2.79 | 0.46 → 0.97 (7 d) | — | treatment type: VAE (Table 10) or boric/SB (text) ⚠️ |

- **Mechanism:** the VAE film is weakly acidic (pH 4.0–6.5), retards hydration next to the fiber and weakens the
  ITZ, so fibers pull out instead of rupturing (§3.2, Table 4). VAE-treated fibers show slip scratches; boric-treated
  fibers pull out long and intact (Figs. 11–12). → [[fiber-matrix-interface]]
- **Over-treatment backfires:** boric anhydride weakens both bond and matrix (S3 softens; C3 f'c −16% vs C1).
- **Early-age loss:** strain falls sharply from 7 to 28 d for both untreated and VAE fibers (Table 11). The
  durability of the VAE film is not studied. ⚠️ Strain basis (peak vs ultimate) is not stated.
- **Exposure can re-tune the interface:** chloride cycling lowers the PVA chemical bond, hot water raises it by about
  50% (as cited in [[vanzijl2010-shcc-durability]], p. 265, 268). Oil and polymer coatings are therefore not
  guaranteed to keep their effect in service. → [[chloride-and-corrosion]]

> Synthesis: VAE coating is a second, independent route (after oiling, [[li2002-pva-ecc-interface-tailoring]]) to
> lower PVA chemical bond, and it reproduces the same trend: less bond, more pull-out, more strain, until bond
> becomes too weak (boric treatments → softening). The "just right" window is confirmed from both sides.

> Synthesis: the interface must be "just right". PVA is detuned with oil, and PE is enhanced by
> matrix densification or coatings. This is the central design lever across all lineages.
> → [[fiber-matrix-interface]]

## Related
- [[fiber-matrix-interface]] · [[pva-fiber]] · [[pe-fiber]] · [[strain-hardening]]
