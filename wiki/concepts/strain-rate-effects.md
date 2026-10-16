---
type: concept
slug: strain-rate-effects
aliases: [rate effects, dynamic behaviour, dynamic increase factor, DIF, high strain rate, loading rate]
tags: [dynamic, tension, extreme-loading]
sources: [ranade2015-hshdc-tensile-rate-effects, ranade2017-hshdc-impact-resistance, yu2018-ecc-direct-tensile-review]
updated: 2026-10-16
---

# Strain-Rate Effects (Dynamic Tension)

## Definition
How mechanical properties change with loading or strain rate. This matters for impact, blast,
earthquake and hurricane loading. It is often expressed as a dynamic increase factor
(dynamic/quasi-static ratio).

## Key points
- **Plain concrete** (as cited in [[ranade2015-hshdc-tensile-rate-effects]], p. 94):
  - Tensile strength increases with log(rate) 2–3× faster than compressive strength, usually
    modelled as bilinear (CEB-FIP / MC2010).
  - High-strength concrete shows smaller increases than normal concrete.
  - Proposed mechanisms span several scales:
    - macro: crack velocity vs Rayleigh wave speed;
    - meso: cracks cutting through aggregates;
    - micro/nano: thermal inertia of bond breaking.
- **In FRCC**, rate effects also depend on the fiber/matrix bond and the fiber's own rate sensitivity:
  - **The chemical bond** of hydrophilic fibers (e.g. PVA) is highly rate-sensitive, while friction
    is less so.
  - **Polymer fibers** are viscoelastic, so their strength and modulus rise with rate. Steel fibers
    are largely rate-insensitive.
- **HSHDC** (PE fiber, no chemical bond) shows a distinctive pattern: strength up, ductility down
  but still high, as the table below shows.

## Quantitative evidence
| Source | Material | Rate range | Δσ_fc | Δσ_tu | ε_tu | Crack width | Note |
|---|---|---|---|---|---|---|---|
| [[ranade2015-hshdc-tensile-rate-effects]] | HSHDC (PE 2%) | 10⁻⁴ → 10 s⁻¹ | +53% (8.1 → 12.4 MPa) | +42% (14.5 → 20.6 MPa) | 4.2 → 2.9% at 0.1 s⁻¹, then plateau (2.7% at 10 s⁻¹) | 160 → 120 µm at 0.1 s⁻¹, then plateau (110) | σ_tu/σ_fc about 1.8 constant; min single-specimen ε_tu 1.7% |

Micro-scale drivers in HSHDC (0.009 → 900 mm/s) ([[ranade2015-hshdc-tensile-rate-effects]]):

| Quantity | Change |
|---|---|
| PE fiber modulus | +85% (most important for crack width) |
| PE fiber strength | +21% (most important for σ_tu) |
| f | +27% |
| µ | +43% |
| τ0 | +14% |
| β | ×2 |
| Km | +19% at up to about 0.05 s⁻¹ |

## Influencing factors / relationships
- Crack width is set by fiber-bridging *stiffness*, which depends on fiber modulus and τ0. A stiffer
  σ–δ curve gives narrower cracks and therefore lower ε_tu at a constant crack count. → [[crack-width]]
- σ_tu is set by fiber-bridging *capacity* (fiber strength). σ_fc follows Km. → [[fiber-bridging]], [[matrix-fracture-toughness]]
- J′b falls (969 → about 600 J/m²) while J_tip rises (25 → ≤ 100 J/m²), so the energy margin
  shrinks from about 39 (computed here: 969/25) to about 6 (stated), but strain hardening survives. → [[strain-hardening]]

> Synthesis: for PE-based HSHDC, rate sensitivity is governed by the *fiber* (viscoelastic PE),
> not the *interface*. PVA-based HDC/ECC should behave differently because of the rate-sensitive
> chemical bond. A primary PVA source is needed to confirm this. → [[pva-fiber]], [[gaps]]

## Link to impact
- Moderate-velocity drop-weight impact is stated to produce strain rates of about 0.1–10 s⁻¹,
  i.e. the range tested in [[ranade2015-hshdc-tensile-rate-effects]]. The FE impact model uses those
  tensile rate effects and assumes compressive rate effects equal to UHPC
  ([[ranade2017-hshdc-impact-resistance]], p. 26). → [[impact-resistance]]

## Conflicts & open questions
- Rates above 10 s⁻¹ (impact or blast range, typically 10²–10³ s⁻¹ [general knowledge — needs
  source]) have not been tested for HSHDC.
- Compressive rate effects in HSHDC: not yet studied (as of this source).

## ECC literature on rate effects ([[yu2018-ecc-direct-tensile-review]], p. 348–351)
- **Reference rate ranges** (Eibl, as cited):

  | Load case | Strain rate (s⁻¹) |
  |---|---|
  | seismic | 10⁻³–10⁻¹ |
  | aircraft landing | 10⁻²–1 |
  | hard impact | 1–50 |
  | hyper-velocity | > 10² |

- **Strength DIF** rises nearly linearly between 1 and 10 s⁻¹, then much more steeply. PVA-ECC is
  more rate-sensitive than PE-ECC. The **ε DIF decreases** for both (Fig. 12).
- **Impact at about 150 s⁻¹** (Curosu 2016, as cited):

  | Material | σ DIF | Fracture-energy DIF |
  |---|---|---|
  | PVA-ECC | 6.7 | 2.4 |
  | moderate-strength PE-ECC | 5.4 | 3.3 |
  | high-strength PE-ECC | 3.12 | 4.2 |

- PVA-ECC at 25–50 s⁻¹: hardening with a single crack.
- S/PE hybrid: negligible ε rate effect from 10⁻⁶ to 10⁻¹ s⁻¹ (Maalej 2005).
- High-volume FA stabilises ε across rates (Yang & Li 2012).
- ⚔️ PVA-ECC ε vs rate: a decrease (Yang & Li 2014; Mechtcherine) vs no significant change
  (Boshoff & van Zijl 2007). → [[gaps]]
- ⚔️ PVA failure at high rate: composite tests show pull-out dominating, while single-fiber tests show
  more rupture (p. 350). → [[gaps]]
- The review restates the Michigan HSHDC rate results of [[ranade2015-hshdc-tensile-rate-effects]] exactly.

## Related
- [[hshdc]] · [[pe-fiber]] · [[extreme-loading-applications]] · [[tensile-strain-capacity]]
