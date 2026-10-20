---
type: property
slug: chloride-and-corrosion
aliases: [chloride ingress, chloride diffusion, reinforcement corrosion, rebar corrosion, R/SHCC, anti-spalling, corrosion cracking]
tags: [durability, chloride, corrosion, transport]
sources: [bu2022-ecc-chloride-crack-width, paul2014-r-shcc-chloride-corrosion, vanzijl2010-shcc-durability, kanda2003-sprayed-ecc, kunieda2006-hpfrcc-japan-applications, kunieda2010-uhp-shcc-steel-reinforcement, wang2023-ecc-frost-damage, homma2009-frcc-self-healing, ma2021-ecc-durability-review, he2024-hdc-research-advances, li2003-ecc-review]
updated: 2026-10-20
---

# Chloride Ingress and Reinforcement Corrosion

Part of the [[durability]] hub. Related: [[permeability]] (transport), [[crack-width]], [[carbonation]], [[self-healing]].

## Definition
Penetration of chloride ions into (cracked) HDC/ECC/SHCC by diffusion (saturated exposure) or capillary
suction (wet–dry exposure), and the resulting corrosion of embedded steel. "R/SHCC" = steel-reinforced SHCC.

## Key points
- **Transport mode matters more than a single crack-width threshold.**
  - Immersion (diffusion), cast notches: 100 µm ≈ uncracked; effect significant at ≥ 200 µm
    ([[bu2022-ecc-chloride-crack-width]], Sect. 3).
  - Wet–dry (capillary suction), real flexural cracks: 50–100 µm cracks carried chloride 65–89 mm deep
    within 1–6 h vs 4.5–8 mm uncracked ([[paul2014-r-shcc-chloride-corrosion]], Table 5); per a companion
    paper, cracks < 50 µm also reach the rebar "within hours" (Abstract, citing Paul & van Zijl 2013a).
- **Uncracked ECC is not exceptionally dense**: D28 ≈ 35.5 × 10⁻¹² m²/s for a W/B 0.26, FA/C 1.2 PVA-ECC
  ([[bu2022-ecc-chloride-crack-width]], Eqs. 10–12, unit printed m/s² ⚠️); D falls with age about 50%
  (30→60 d), 30% (60→90 d), 5% (90→120 d) (Sect. 3.1.3), via hydration, FA reaction and chloride binding.
  As cited there: ECC D ≈ 10–35% of same-strength concrete (Sahmaran 2011).
- **Multiple fine cracks vs one wide crack**: chloride diffusion rises linearly with pre-deformation in ECC
  but exponentially in mortar (Sahmaran 2007, as cited in [[ma2021-ecc-durability-review]], Fig. 11, and in
  [[vanzijl2010-shcc-durability]], Fig. 5b). → [[permeability]]
- **Fine cracks do not prevent corrosion initiation** in R/SHCC under wet–dry chloride; corrosion becomes
  **localised pitting** rather than distributed ([[paul2014-r-shcc-chloride-corrosion]], Fig. 13, p. 348).
  This refines the older statement that tight cracks "may delay corrosion" but need confirmation
  ([[li2003-ecc-review]], p. 225).
- **Corrosion-induced cracking and spalling are strongly reduced**: in the tapered-pin (1/50 taper)
  expansion test, ECC first-crack COD was 24–49 µm (mean 36) vs 50–78 µm (mean 67) for SBR polymer-cement
  mortar (PCM); at 10 mm pin displacement ECC COD < 0.3 mm vs 0.5–1 mm for PCM, and ECC kept carrying load
  ([[kanda2003-sprayed-ecc]], Table 8, Figs. 13–14). Cover spalling in R/SHCC is "highly unlikely"
  ([[vanzijl2010-shcc-durability]], p. 265).
- **Macro-cell → micro-cell**: in finely cracked HPFRCC/SHCC, rebar corrosion is micro-cell (slow) rather than
  macro-cell (fast) (Hiraishi 2005, as cited in [[kunieda2006-hpfrcc-japan-applications]], p. 24; JSCE 2004 for
  cracks < 40 µm, as cited in [[kunieda2010-uhp-shcc-steel-reinforcement]], §1).
- **Steel fibres corrode at cracks**: steel cords on crack faces corroded within 3 d of water immersion;
  in PE + steel hybrid FRCC corrosion stayed at the outer face ([[homma2009-frcc-self-healing]], Fig. 16).
  → [[hybrid-fiber]]
- **Chloride binding / effect on interface**: accelerated chloride (10 × [5 d sat. NaCl + 2 d 50 °C]) cut PVA
  chemical bond, raised frictional bond slightly, left matrix toughness unchanged (Kabele 2006/2007, as cited
  in [[vanzijl2010-shcc-durability]], p. 265); chloride lowers first-crack strength and interface bond
  (Li & Li 2011, as cited in [[ma2021-ecc-durability-review]], p. 5). → [[fiber-matrix-interface]]

## Quantitative evidence
### Chloride ingress
| Source (term) | Exposure | Cracks | Result | Note |
|---|---|---|---|---|
| [[bu2022-ecc-chloride-crack-width]] (ECC, PVA 2 vol.%, W/B 0.26, FA/C 1.2) | 3.5% NaCl immersion, 30–120 d | cast notches 0 / 100 / 200 / 300 µm, 25 mm deep | 100 µm ≈ uncracked; surface free Cl⁻ +8.7 / +14.9% (200 / 300 µm) at 30 d, +17.4 / +29.4% at 120 d | Sect. 3; notches are smooth, single, unbridged; SH not shown |
| [[paul2014-r-shcc-chloride-corrosion]] (SHCC, PVA, w/c 1.0, FA/C 1.72; ε 1.5–2.9% at 14 d) | 3.5% NaCl, 4 d dry / 3 d wet, up to 620 d | R/SHCC 5–18 cracks, avg 22–38 µm, max 50–120 µm; R/mortar avg 139, max 250 µm | rebar Cl⁻ 0.17–0.59% by binder mass at covers 15–35 mm; no correlation with cover, crack width or crack number | Table 3, Figs. 10, 17 |
| [[wang2023-ecc-frost-damage]] (ECC, PVA) | 3% NaCl 14 d after F-T | uncracked, frost-damaged | surface Cl⁻ ≈0.5% → ≈0.7% (0 → 300 F-T cycles); matrix ≈0.65% → ≈0.9% (0 → 75) | Figs. 13–14, read ⚠️ → [[freeze-thaw]] |
| Liu 2017, as cited in [[ma2021-ecc-durability-review]] | 200 d sulfate + chloride | — | σ_tu rose, ε > 2%, cracks < 50 µm | p. 5 (moved from [[durability]]) |

Model ([[bu2022-ecc-chloride-crack-width]], Eqs. 8, 10–12; w = notch width, mm assumed ⚠️):
C_s = (0.49359w + 0.47297)(1 − e^(−0.03375t)); D(t′) = D28(28/t′)^n with n = −1.0976w + 1.8948.
Error mostly < 20%; over-predicts beyond 22.5 mm depth for 0.2–0.3 mm notches (Fig. 11).

### Reinforcement corrosion (primary: [[paul2014-r-shcc-chloride-corrosion]])
| Quantity | R/SHCC | R/mortar | Location |
|---|---|---|---|
| Corrosion rate | ≈0.003–0.02 mm/yr | similar | Fig. 8, read ⚠️ |
| Corrosion form | localised pitting; avg pit 0.2–0.3 mm, max 0.3–0.6 mm | distributed | Table 4, Fig. 13 |
| Yield-force loss after 560–610 d | up to 13.2% | — | Table 4 |
| Cover beyond which corrosion depth no longer falls | 15–25 mm | — | Fig. 11, p. 350 |
| Half-cell potential | < −350 mV in most specimens; ASTM C876 criteria may not apply to SHCC | — | p. 346 |

### Second-hand (as cited)
- R/SHCC vs R/mortar beams under load + wet–dry chloride: several 0.1 mm cracks vs one 0.3 mm crack; lower
  penetration and corrosion rate (Miyazato & Hiraishi 2005, as cited in [[vanzijl2010-shcc-durability]], p. 265).
- Accelerated electrochemical corrosion: SHCC extends the propagation period and keeps load capacity
  (Sahmaran 2008, as cited, p. 265).
- Thresholds for significant chloride ingress: 55–80 µm (Jang 2011) and ≥ 90 µm (Wu 2017), as cited in
  [[he2024-hdc-research-advances]], p. 10; ≈100 µm (Sahmaran 2007, as cited in [[vanzijl2010-shcc-durability]], p. 264,
  but the reproduced figure plots deformation, not crack width ⚠️); no difference in D_eff for 10–50 µm cracks
  (Şahmaran & Li 2009, as cited in [[bu2022-ecc-chloride-crack-width]], Sect. 1).
- Corrosion cracking: ECC/PCM at pin displacement ≈3.2–3.6 mm vs 0.5–1 mm estimated for normal concrete
  ([[kanda2003-sprayed-ecc]], Table 8, p. 279).

## Influencing factors / relationships
- Exposure mode (immersion vs wet–dry), crack width (average vs maximum, loaded vs unloaded → [[crack-width]]),
  cover depth, matrix porosity (w/c 1.0 in Paul 2014), FA content and chloride binding → [[fly-ash]].
- Total (accumulated) crack width, not maximum, is said to govern chloride resistance (concrete papers, as cited in [[bu2022-ecc-chloride-crack-width]], Sect. 1).

> Synthesis: the wiki's earlier single threshold (55–80 µm) is too simple. Under saturated diffusion,
> cracks ≤ about 100 µm behave almost like uncracked ECC; under wet–dry capillary suction, even cracks of
> 20–50 µm average carry chloride to the steel within hours. What fine cracking clearly *does* deliver is
> resistance to corrosion-induced cracking and spalling, and probably micro-cell rather than macro-cell
> corrosion. For PE-based HSHDC (80–200 µm cracks) the picture is less clear-cut than before: perhaps
> acceptable in submerged exposure, not in splash or wet–dry zones.

## Conflicts & open questions
- ⚔️ **Chloride crack-width threshold**: 55–80 µm (Jang 2011) / ≥ 90 µm (Wu 2017), both second-hand via
  [[he2024-hdc-research-advances]] p. 10; ≈100 µm (Sahmaran 2007 as cited in [[vanzijl2010-shcc-durability]]);
  100–200 µm under immersion with notches ([[bu2022-ecc-chloride-crack-width]]); < 100 µm (even < 50 µm) still
  harmful under wet–dry ([[paul2014-r-shcc-chloride-corrosion]]). Transport-mode dependent. → [[gaps]]
- ⚔️ **Corrosion rate R/SHCC vs R/mortar**: similar ([[paul2014-r-shcc-chloride-corrosion]], Fig. 8) vs slower in
  R/SHCC (Miyazato 2005; Sahmaran 2008; Kobayashi 2010, as cited in [[vanzijl2010-shcc-durability]], p. 265).
  Different pre-crack deflections and measurement start times. → [[gaps]]
- Open: direct corrosion tests on sprayed ECC overlays ([[kanda2003-sprayed-ecc]], p. 279); calibrated
  half-cell criteria for SHCC; models for localised (pitting) corrosion; chloride deeper than 30 mm for wide
  cracks ([[bu2022-ecc-chloride-crack-width]]); free vs total chloride in high-FA matrices.

## Related
- [[durability]] · [[permeability]] · [[crack-width]] · [[carbonation]] · [[freeze-thaw]] · [[self-healing]] · [[repair-and-field-applications]] · [[rc-member-strengthening]] · [[gaps]]
