---
type: material
slug: hybrid-fiber
aliases: [hybrid fiber reinforcement, steel + PE hybrid, PVA + steel hybrid, PVA + PE hybrid, HFRCC, HB, HECC, steel fiber, steel cord]
tags: [fiber, steel, hybrid]
sources: [homma2009-frcc-self-healing, kanakubo2006-dfrcc-tensile-test-method, yuan2020-nshsdc-beam-strengthening, lee2021-hsdc-wall-emi-impact, zhou2023-hsecc-elevated-temperature, mechtcherine2011-shcc-high-strain-rate, zhang2022-hshdcc-review, pourfalah2018-ecc-high-temperature, yun2013-shcc-freeze-thaw, zhang2022-hdc-basalt-textile-tension, huy2023-egc-pe-pva-hybrid-healing]
updated: 2026-10-26
---

# Hybrid Fiber Systems (steel + polymer, polymer + polymer)

## Definition
A composite that combines a stiff, strong steel fiber with a fine synthetic fiber (PE or PVA). The stated aim is steel for
strength (and electrical conductivity), and the polymer fiber for multiple cracking and ductility
([[lee2021-hsdc-wall-emi-impact]], §1, §3.1). Scope widened 2026-10-21 to polymer–polymer hybrids (PVA + PE,
[[yun2013-shcc-freeze-thaw]]). Textile grid + short PVA fibre ("hybrid reinforcement", [[zhang2022-hdc-basalt-textile-tension]])
is covered in [[textile-reinforced-hdc]]. A hybrid is **not** HDC/ECC/SHCC by default. Tensile strain hardening must
be shown in the source (CLAUDE.md §3).

## Key points
- Seven hybrid systems are in the wiki. Steel + PE (Japan, Korea), PVA + steel (China; UK "HECC"), PVA + PE (Korea, two:
  cement-based SHCC and the cementless HSUD-EGC), and one hybrid in the JCI round robin.
- Until round 4, no primary hybrid paper clearly showed tensile strain hardening in a coupon test, except the modest JCI
  result. **Updated 2026-10-21**: SH is now shown for PVA + steel HECC (dog-bones, ε at peak 2.5–3.0%,
  [[pourfalah2018-ecc-high-temperature]], Table 4) and for PVA + PE SHCC (JSCE dumbbells, [[yun2013-shcc-freeze-thaw]], Fig. 8).
- **Updated 2026-10-26**: a polymer–polymer (PE + PVA, no steel) hybrid in a **cementless** high-strength matrix strain-hardened
  to 6.79–11.99% at peak with f'c 50.4–86.5 MPa ([[huy2023-egc-pe-pva-hybrid-healing]], Table 5, Fig. 3); the highest hybrid
  strain in the wiki.

## Quantitative evidence
### Mix and fibers
| Source | Term (authors) | Polymer fiber | Steel fiber | Total Vf (%) | W/B | f'c (MPa) |
|---|---|---|---|---|---|---|
| [[homma2009-frcc-self-healing]] Tables 1–2 | HFRCC ("FRCC", not called SHCC) | PE 6 mm × 12 µm, 2580 MPa, 73 GPa, 0.75% | steel cord 32 mm × 400 µm, 2850 MPa, 200 GPa, 0.75% | 1.5 | 0.45 | n.r. |
| [[kanakubo2006-dfrcc-tensile-test-method]] Table 4 | DFRCC "HB" | PE 15 mm × 12 µm, 1.0% | steel 32 mm × 405 µm, 1.0% | 2.0 | 0.45 | 43.6 |
| [[yuan2020-nshsdc-beam-strengthening]] Tables 2, 4, 5 | NSHSDC (Korea Univ.) | PE 12 mm × 31 µm, 2900 MPa, 100 GPa, 0.5% | straight steel 19.5 mm × 200 µm, 1.0% | 1.5 | 0.172 | 123.4 (room-cured) |
| [[lee2021-hsdc-wall-emi-impact]] Tables 1, 3 | HSDC (same mix as above) | same | same | 1.5 | 0.172 | 122.3 |
| [[pourfalah2018-ecc-high-temperature]] Tables 2–3, 5 | HECC: H6ECC / H13ECC (Heriot-Watt) | PVA 12 mm × 40 µm, 1.75% | straight steel 6 or 13 mm × 150 µm, 3000 MPa, 210 GPa, 0.75% | 2.5 | 0.28 (derived) | 40.1 / 45 (ECC 38.8; 50 mm cubes, 28 d) |
| [[yun2013-shcc-freeze-thaw]] Tables 1, 3 | SHCC (Chungnam) | PVA 12 mm × 40 µm + PE 12 mm × 12 µm: 1.30 + 0.20 or 0.75 + 0.75 | none | 1.5 | 0.45 / 0.55 | 35.73–48.80 (before F-T) |
| [[zhou2023-hsecc-elevated-temperature]] Tables 2–3 | HSECC PS-I / PS-II (Guangzhou) | PVA 12 mm, 1.5% / 1.0% | Cu-coated steel 13 mm × 220 µm, 2800 MPa, 200 GPa, 0.5% / 1.0% | 2.0 | 0.20 | 75.1 / 93.8 (PVA-only 83.1) |
| [[huy2023-egc-pe-pva-hybrid-healing]] Tables 1, 3; Fig. 3 | HSUD-EGC (Chonnam; cementless GGBS/FA/SF geopolymer) | PE 18 mm × 12 µm (3030 MPa, 88 GPa) + PVA 12 mm × 40 µm (1560 MPa, 41 GPa): 1.0 + 0.5 or 0.5 + 1.0 | none | 1.5 | n.r. (≈ 0.38 total water/precursor, computed) | 84.3–86.5 (GGBS:FA 5.5:4) / 50.4–51.9 (3:6.5); ≈ 35 d ⚠️ |

### Tension and flexure
| Source | Result | Location |
|---|---|---|
| [[kanakubo2006-dfrcc-tensile-test-method]] | HB strain at peak 0.705% (thin plate T1), 0.217 / 0.017% (100 × 60 dogbone H / V), 0.122% (Ø70); deflection hardening in 4-pt bending; inverse analysis gives 1.79% ultimate strain | Tables 6–11 |
| [[yuan2020-nshsdc-beam-strengthening]] | σ_t 9.7 MPa (JSCE dogbone); strain not reported. ε > 2.9% claimed from refs 12–13 ⚠️; MOR 21.9 MPa | Table 5, §1 |
| [[homma2009-frcc-self-healing]] | ductile response, σ about 3.3–3.6 MPa read from Fig. 2 ⚠️ (PE-only mix softened) | Fig. 2, p. 224 |
| [[zhou2023-hsecc-elevated-temperature]] | flexural softening at every temperature; no tension test | Fig. 10 |
| [[pourfalah2018-ecc-high-temperature]] | dog-bone (80 mm gauge, 30 × 13 mm), 28 d: σ_tu 3.85 / 4.36 / 4.71 MPa and ε at peak 3.5 / 3.0 / 2.5% for ECC / H6ECC / H13ECC; longer steel → fewer cracks, lower strain, higher strength | Table 4, §4.1, Fig. 4 |
| [[yun2013-shcc-freeze-thaw]] | JSCE dumbbells strain-harden; σ_tu 2.35–3.77 MPa before F-T; more PE (0.75/0.75) → more fine cracks, lower f'c, more air | Table 3, Figs. 8, 11 |
| [[huy2023-egc-pe-pva-hybrid-healing]] | JSCE dumbbell (80 mm gauge): σ_tu 4.60–6.64 MPa, ε at peak 6.79–11.99%, 61–84 cracks, avg width 83–136 µm; PE-rich > PVA-rich in σ_tu and ε | Tables 5–6 |

### Behaviour after exposure
| Source | Exposure | PVA- or PE-only | Hybrid |
|---|---|---|---|
| [[zhou2023-hsecc-elevated-temperature]] Table 5 | residual f_f after 1 h at 30 / 200 / 400 / 600 / 800 °C | PO 15.8 / 13.1 / 5.9 / 3.2 / 2.1 MPa | PS-II 15.9 / 15.4 / 13.9 / 10.9 / 6.6 MPa |
| same | spalling; thermal crack width | none at any temperature; ≤ 19.6 µm | slight spalling at 800 °C; PS-I cracks up to 271.1 µm at 800 °C |
| same, Fig. 12 | steel above 750 °C | — | oxide film forms; steel pulls out and bridging is nearly lost |
| [[homma2009-frcc-self-healing]] Fig. 15, 6b | healing in water, 28 d | PE: strength recovery 0–100% | hybrid > 100% recovery at residual elongation < 2 mm; steel-cord-only ≈ 0 or negative (corrosion) |
| same, Fig. 16 | corrosion | — | in the hybrid, steel corrosion stayed on the outer face |
| [[pourfalah2018-ecc-high-temperature]] | **hot** tests 20–600 °C | ECC: brittle from 200 °C; 30% debris at 600 °C; crack width hundreds of µm at 60–100 °C | HECC: ≈ 2× ECC bending peak load at 100–600 °C; crack width ≈ 5× smaller at 60–100 °C; 8.5% debris; no spalling; steel pulls out to 400 °C, ruptures at 600 °C; steel length does not change debris (Figs. 7, 10, 14) |
| [[yun2013-shcc-freeze-thaw]] | 300 F-T cycles (ASTM C666 B) | — | σ_tu kept, strain capacity slightly lower; larger loss with more PVA and W/B 0.55 (Concl. 3) |
| [[huy2023-egc-pe-pva-hybrid-healing]] Figs. 10, 12; Table 8 | 3% pre-strain at 7 d, 28 d in water | — | crack healing rate 26.78 / 31.40 / 7.36 / 12.48% and RF recovery +15.63 / +24.16 / −9.58 / −6.59 %-points (S-PE / S-PVA / F-PE / F-PVA); PVA-rich heals better; reloaded σ_tu +3.7%, ε −6.1% on average |

## Influencing factors / relationships
- **Steel content is capped to keep PE in control.** Korea Univ. limits steel to 1.0 vol.% so that PE drives strain
  hardening, in contrast to UHPFRC with > 1.5 vol.% steel ([[lee2021-hsdc-wall-emi-impact]], §1).
- **EMI shielding:** steel fibers above the percolation threshold form a conductive network; PE is non-conductive
  ([[lee2021-hsdc-wall-emi-impact]], §2.2, §3.1). Longer steel fibers (35 mm) shield better than 19.5 mm (as cited, Fig. 5).
  Read from Fig. 5 (p. 7): full-depth HSDC panels ≈ 16 → 43 dB (100 mm) and ≈ 20 → 50 dB (200 mm) over 400–1400 MHz, vs
  steel-FRC references ≈ 40–57 dB; a 20 mm HSDC skin raised a 100 mm NC panel from ≈ 4.6 to ≈ 35 dB (single) / ≈ 48.5 dB
  (double) at 1400 MHz (Fig. 6, p. 8).
  → [[extreme-loading-applications]]
- **Rate:** a steel/PE hybrid roughly doubled strength at high rate with unchanged ε (Maalej 2005, as cited in
  [[mechtcherine2011-shcc-high-strain-rate]], p. 51). → [[strain-rate-effects]]
- **Review data:** at 2% total fiber, 2% PE gives 23× the ε_tu of 2% steel; adding steel narrows cracks and raises f'c by
  up to 51% (as cited in [[zhang2022-hshdcc-review]], p. 9–14). → [[fiber-geometry]]
- **PE:PVA ratio (polymer hybrid):** PE-rich (2:1) gives higher σ_tu and ε, PVA-rich (1:2) heals better; hybridisation is
  motivated by cost (PVA ≈ 1/5 of PE price) ([[huy2023-egc-pe-pva-hybrid-healing]], Table 5, Table 7, Figs. 10, 12).

- **Recommended dosage (author)**: 6 mm steel for elements exposed to ≤ 100 °C or blast, at "0.5 vol.%" although 0.75% was
  tested ⚠️ ([[pourfalah2018-ecc-high-temperature]], p. 929–930).

> Synthesis: hybrids trade ductility for strength, crack-width control at high temperature, and conductivity. Steel
> helps residual flexure above 400 °C ([[zhou2023-hsecc-elevated-temperature]]) and strength recovery after healing
> ([[homma2009-frcc-self-healing]]). The tensile-strain evidence was weak until round 5 (JCI HB at most 0.7% at peak;
> Korea Univ. claims of more than 2.9% are second-hand). PVA + 0.75% steel HECC now shows 2.5–3.0% at peak, so a modest
> steel share costs only part of the PVA-ECC ductility (3.5%) and buys about 2× hot bending capacity
> ([[pourfalah2018-ecc-high-temperature]]). Steel did not cause spalling up to 600 °C there, while 1.0% steel did slightly
> at 800 °C ([[zhou2023-hsecc-elevated-temperature]]). Treat hybrids as HDC only where the source shows tensile strain hardening.

## Conflicts & open questions
- ⚔️ Steel helps fire residual strength but raises spalling and thermal crack width ([[zhou2023-hsecc-elevated-temperature]],
  Table 5). Whether the net effect is positive depends on the criterion.
- ⚔️ (minor) Spalling of PVA + steel hybrids: none to 600 °C ([[pourfalah2018-ecc-high-temperature]]) vs slight at 800 °C
  ([[zhou2023-hsecc-elevated-temperature]]); ranges do not overlap.
- Optional new page: steel-fiber (steel fibres now used in zhou2023, pourfalah2018, homma2009, kanakubo2006, yuan2020).
- The tensile strain capacity of the Korea Univ. NSHSDC/HSDC mix is not shown in [[yuan2020-nshsdc-beam-strengthening]] or
  [[lee2021-hsdc-wall-emi-impact]]. → [[gaps]]
- How steel content changes PVA/steel bridging efficiency at elevated temperature is unknown (stated gap,
  [[zhou2023-hsecc-elevated-temperature]], p. 749).

## Related
- [[pe-fiber]] · [[pva-fiber]] · [[hshdc]] · [[high-temperature-behaviour]] · [[self-healing]] · [[rc-member-strengthening]] · [[four-point-bending-inverse-analysis]] · [[freeze-thaw]] · [[textile-reinforced-hdc]] · [[alkali-activated-binder]]
