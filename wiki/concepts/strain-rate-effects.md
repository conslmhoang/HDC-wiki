---
type: concept
slug: strain-rate-effects
aliases: [rate effects, dynamic behaviour, dynamic increase factor, DIF, high strain rate, loading rate]
tags: [dynamic, tension, extreme-loading]
sources: [ranade2015-hshdc-tensile-rate-effects, ranade2017-hshdc-impact-resistance, yu2018-ecc-direct-tensile-review, mechtcherine2011-shcc-high-strain-rate]
updated: 2026-10-20
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
> *(2026-10-20: confirmed by [[mechtcherine2011-shcc-high-strain-rate]]; see the section below.)*

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

## Primary PVA-SHCC data: Mechtcherine et al. 2011 (2026-10-20 ingest)
PVA-SHCC (2.2 vol.% PVA, high FA, SAP; TU Dresden), dumbbells, 6 specimens per rate
([[mechtcherine2011-shcc-high-strain-rate]], Table 2):

| Strain rate (s⁻¹) | σ_t (MPa) | ε at peak (%) | Work of fracture (J) | Cracking / failure |
|---|---|---|---|---|
| 10⁻⁵ | 4.54 | 1.49 | 8.04 | multiple cracking |
| 10⁻⁴ | 5.28 | 1.28 | 7.69 | fewer cracks |
| 10⁻³ | 5.37 | 0.93 | 6.71 | fewer cracks |
| 10⁻² | 5.51 | 0.82 | 5.25 | fiber **rupture**, pull-out < 0.5 mm (mode A) |
| 10 | 7.81 | 0.68 | 9.86 | no visible multiple cracking |
| 25 | 12.08 | 0.86 | 10.51 | — |
| 50 | 11.93 | 1.79 | 20.03 | fiber **pull-out**, about 2.5 mm, plastic fiber deformation (mode B) |

- **Non-monotonic:** ε falls up to 10⁻² s⁻¹ and rises again at 10–50 s⁻¹ (Fig. 10, p. 58–59).
- **Strength DIF** about 1.2 at 10⁻⁴ s⁻¹ and about 2.5 at 50 s⁻¹ (stated, Fig. 9; 11.93/4.54 = 2.63 computed from
  Table 2), with a steep rise above about 1–10 s⁻¹.
- **Micro-scale drivers:** single PVA fiber strength rises only 1456 → 1674 MPa (8.3·10⁻⁴ → 1.5 s⁻¹) and fiber strain at
  failure is rate-insensitive (27.4–27.5%) (Table 3), but the pull-out peak force about doubles from 10⁻⁵ to 10 s⁻¹
  (Fig. 13). Mode A is explained by bond rising faster than fiber strength → rupture → fewer cracks (p. 56–60).
  Why mode B returns to pull-out is left open (p. 60–61). → [[fiber-matrix-interface]]
- **Earlier SHCC data (as cited, p. 51):** Yang & Li 2005: strength ×2, ε 3 → 0.5% (10⁻⁵–10⁻¹ s⁻¹); Douglas & Billington
  2005: ε −53%, strength +12% at 0.2 s⁻¹; Maalej 2005 steel/PE hybrid: strength about ×2, ε unchanged.
- **Spallation** (Hopkinson bar) at 140–180 s⁻¹: strength DIF 6.7 (Millon et al. 2010, as cited, p. 58).
  ⚠️ [[yu2018-ecc-direct-tensile-review]] attributes a PVA-ECC DIF of 6.7 at about 150 s⁻¹ to Curosu 2016 (table
  above). Possible misattribution in the review; verify.
- **Load-case strain rates** (Banthia 2004, as cited, p. 51): traffic 10⁻⁶–5·10⁻⁴, gas explosion 5·10⁻⁵–5·10⁻⁴,
  earthquake 5·10⁻³–5·10⁻¹, pile driving 10⁻²–1, aircraft landing 5·10⁻²–2 s⁻¹. These differ from the Eibl ranges
  quoted above; both are second-hand.

**Refinement of the two open conflicts:**
- PVA-ECC ε vs rate: the "decrease" side holds only up to 10⁻² s⁻¹; at ≥ 10 s⁻¹ ε rises again. Part of the
  disagreement with Boshoff & van Zijl 2007 is the rate range. Status: partly resolved, non-monotonic. → [[gaps]]
- PVA failure mode at high rate: in this composite both occur, depending on rate (rupture ≤ 10⁻² s⁻¹, pull-out
  ≥ 10 s⁻¹). → [[gaps]]

> Synthesis: the earlier synthesis on this page is now confirmed by a primary PVA source. PVA-SHCC is
> **interface-governed** (pull-out force ×2, fiber strength +15%) and loses multiple cracking at high rate,
> whereas PE-HSHDC is **fiber-governed** (PE modulus +85%, τ0 +14%) and keeps its crack count
> ([[ranade2015-hshdc-tensile-rate-effects]]). The two fiber systems should not share one DIF model.

## Related
- [[hshdc]] · [[pe-fiber]] · [[pva-fiber]] · [[extreme-loading-applications]] · [[tensile-strain-capacity]] · [[multiple-cracking]]
