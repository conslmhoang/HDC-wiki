---
type: material
slug: hybrid-fiber
aliases: [hybrid fiber reinforcement, steel + PE hybrid, PVA + steel hybrid, HFRCC, HB, steel fiber, steel cord]
tags: [fiber, steel, hybrid]
sources: [homma2009-frcc-self-healing, kanakubo2006-dfrcc-tensile-test-method, yuan2020-nshsdc-beam-strengthening, lee2021-hsdc-wall-emi-impact, zhou2023-hsecc-elevated-temperature, mechtcherine2011-shcc-high-strain-rate, zhang2022-hshdcc-review]
updated: 2026-10-20
---

# Hybrid Fiber Systems (steel + polymer)

## Definition
A composite that combines a stiff, strong steel fiber with a fine synthetic fiber (PE or PVA). The stated aim is steel for
strength (and electrical conductivity), and the polymer fiber for multiple cracking and ductility
([[lee2021-hsdc-wall-emi-impact]], §1, §3.1). A hybrid is **not** HDC/ECC/SHCC by default. Tensile strain hardening must
be shown in the source (CLAUDE.md §3).

## Key points
- Four hybrid systems are in the wiki so far. Two use steel + PE (Japan, Korea), one uses PVA + steel (China), and one
  is a hybrid in the JCI round robin.
- In **none** of the primary hybrid papers below is tensile strain hardening clearly shown with a coupon test, except the
  modest JCI result.

## Quantitative evidence
### Mix and fibers
| Source | Term (authors) | Polymer fiber | Steel fiber | Total Vf (%) | W/B | f'c (MPa) |
|---|---|---|---|---|---|---|
| [[homma2009-frcc-self-healing]] Tables 1–2 | HFRCC ("FRCC", not called SHCC) | PE 6 mm × 12 µm, 2580 MPa, 73 GPa, 0.75% | steel cord 32 mm × 400 µm, 2850 MPa, 200 GPa, 0.75% | 1.5 | 0.45 | n.r. |
| [[kanakubo2006-dfrcc-tensile-test-method]] Table 4 | DFRCC "HB" | PE 15 mm × 12 µm, 1.0% | steel 32 mm × 405 µm, 1.0% | 2.0 | 0.45 | 43.6 |
| [[yuan2020-nshsdc-beam-strengthening]] Tables 2, 4, 5 | NSHSDC (Korea Univ.) | PE 12 mm × 31 µm, 2900 MPa, 100 GPa, 0.5% | straight steel 19.5 mm × 200 µm, 1.0% | 1.5 | 0.172 | 123.4 (room-cured) |
| [[lee2021-hsdc-wall-emi-impact]] Tables 1, 3 | HSDC (same mix as above) | same | same | 1.5 | 0.172 | 122.3 |
| [[zhou2023-hsecc-elevated-temperature]] Tables 2–3 | HSECC PS-I / PS-II (Guangzhou) | PVA 12 mm, 1.5% / 1.0% | Cu-coated steel 13 mm × 220 µm, 2800 MPa, 200 GPa, 0.5% / 1.0% | 2.0 | 0.20 | 75.1 / 93.8 (PVA-only 83.1) |

### Tension and flexure
| Source | Result | Location |
|---|---|---|
| [[kanakubo2006-dfrcc-tensile-test-method]] | HB strain at peak 0.705% (thin plate T1), 0.217 / 0.017% (100 × 60 dogbone H / V), 0.122% (Ø70); deflection hardening in 4-pt bending; inverse analysis gives 1.79% ultimate strain | Tables 6–11 |
| [[yuan2020-nshsdc-beam-strengthening]] | σ_t 9.7 MPa (JSCE dogbone); strain not reported. ε > 2.9% claimed from refs 12–13 ⚠️; MOR 21.9 MPa | Table 5, §1 |
| [[homma2009-frcc-self-healing]] | ductile response, σ about 3.3–3.6 MPa read from Fig. 2 ⚠️ (PE-only mix softened) | Fig. 2, p. 224 |
| [[zhou2023-hsecc-elevated-temperature]] | flexural softening at every temperature; no tension test | Fig. 10 |

### Behaviour after exposure
| Source | Exposure | PVA- or PE-only | Hybrid |
|---|---|---|---|
| [[zhou2023-hsecc-elevated-temperature]] Table 5 | residual f_f after 1 h at 30 / 200 / 400 / 600 / 800 °C | PO 15.8 / 13.1 / 5.9 / 3.2 / 2.1 MPa | PS-II 15.9 / 15.4 / 13.9 / 10.9 / 6.6 MPa |
| same | spalling; thermal crack width | none at any temperature; ≤ 19.6 µm | slight spalling at 800 °C; PS-I cracks up to 271.1 µm at 800 °C |
| same, Fig. 12 | steel above 750 °C | — | oxide film forms; steel pulls out and bridging is nearly lost |
| [[homma2009-frcc-self-healing]] Fig. 15, 6b | healing in water, 28 d | PE: strength recovery 0–100% | hybrid > 100% recovery at residual elongation < 2 mm; steel-cord-only ≈ 0 or negative (corrosion) |
| same, Fig. 16 | corrosion | — | in the hybrid, steel corrosion stayed on the outer face |

## Influencing factors / relationships
- **Steel content is capped to keep PE in control.** Korea Univ. limits steel to 1.0 vol.% so that PE drives strain
  hardening, in contrast to UHPFRC with > 1.5 vol.% steel ([[lee2021-hsdc-wall-emi-impact]], §1).
- **EMI shielding:** steel fibers above the percolation threshold form a conductive network; PE is non-conductive
  ([[lee2021-hsdc-wall-emi-impact]], §2.2, §3.1). Longer steel fibers (35 mm) shield better than 19.5 mm (as cited, Fig. 5).
  → [[extreme-loading-applications]]
- **Rate:** a steel/PE hybrid roughly doubled strength at high rate with unchanged ε (Maalej 2005, as cited in
  [[mechtcherine2011-shcc-high-strain-rate]], p. 51). → [[strain-rate-effects]]
- **Review data:** at 2% total fiber, 2% PE gives 23× the ε_tu of 2% steel; adding steel narrows cracks and raises f'c by
  up to 51% (as cited in [[zhang2022-hshdcc-review]], p. 9–14). → [[fiber-geometry]]

> Synthesis: hybrids trade ductility for strength, crack-width control at high temperature, and conductivity. Steel
> helps residual flexure above 400 °C ([[zhou2023-hsecc-elevated-temperature]]) and strength recovery after healing
> ([[homma2009-frcc-self-healing]]). The tensile-strain evidence is weak: the one coupon dataset (JCI HB) gives at most
> 0.7% at peak, and the Korea Univ. claims of > 2.9% are second-hand. Treat hybrids as HDC only where the source shows
> tensile strain hardening.

## Conflicts & open questions
- ⚔️ Steel helps fire residual strength but raises spalling and thermal crack width ([[zhou2023-hsecc-elevated-temperature]],
  Table 5). Whether the net effect is positive depends on the criterion.
- The tensile strain capacity of the Korea Univ. NSHSDC/HSDC mix is not shown in [[yuan2020-nshsdc-beam-strengthening]] or
  [[lee2021-hsdc-wall-emi-impact]]. → [[gaps]]
- How steel content changes PVA/steel bridging efficiency at elevated temperature is unknown (stated gap,
  [[zhou2023-hsecc-elevated-temperature]], p. 749).

## Related
- [[pe-fiber]] · [[pva-fiber]] · [[hshdc]] · [[high-temperature-behaviour]] · [[self-healing]] · [[rc-member-strengthening]] · [[four-point-bending-inverse-analysis]]
