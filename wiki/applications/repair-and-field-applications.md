---
type: application
slug: repair-and-field-applications
aliases: [link slab, bridge deck, repair, field application, sprayed ECC, sprayed HPFRCC, surface protection, overlay]
tags: [application, field, repair]
sources: [li2003-ecc-review, chai2023-hdc-ambient-temperature, kunieda2006-hpfrcc-japan-applications, kanda2003-sprayed-ecc, wang2019-rc-beam-ecc-shear-strengthening, kunieda2010-uhp-shcc-steel-reinforcement, xue2023-shcc-structural-review, chai2019-hdcc-freeze-thaw-carbonation-flexure, yuan2020-nshsdc-beam-strengthening, lee2021-hsdc-wall-emi-impact]
updated: 2026-10-20
---

# Repair, Link Slabs and Field Use

> Status (2026-10-20): field projects **with measured data** now enter the corpus, but only second-hand:
> [[kunieda2006-hpfrcc-japan-applications]] reports crack widths over 24 months on a field retaining wall (from
> Rokugo 2005). Spraying processing data are primary ([[kanda2003-sprayed-ecc]]). Correction: the earlier line
> "No ingested paper reports a field project with measured data" no longer holds.

## Field projects (Japan, as reported in [[kunieda2006-hpfrcc-japan-applications]])
| Project | Year | Use | Placement | Measured / reported outcome | Location |
|---|---|---|---|---|---|
| ASR-damaged retaining wall, Gifu (18 × 5 m) | 2003 | surface repair | sprayed 50–70 mm, with/without mesh | HPFRCC uncracked to 7 months, cracks **≤ 50 µm at 10 months, ≤ 120 µm at 24 months**; repair mortar 30 / 200 / **300 µm** at 3 / 10 / 24 months (Rokugo 2005, as cited) | p. 29, Table 3, Fig. 16 |
| Mitaka Dam, Hiroshima | 2003 | upstream face repair | 30 m³ sprayed 30 mm thick over 500 m²; anchors every 1.5 m² | no performance data | p. 27, Fig. 13 |
| Mihara Bridge, Hokkaido (972 m; 340 m span) | 2004 | steel-deck overlay | 40 mm HPFRCC replacing half the asphalt; plate dowels; ready-mixed about 30 m³/day, about 800 m³ total | no performance data | p. 26, Fig. 11 |
| Irrigation channels (Shiga, Toyama) | 2005 | lining repair | 6 mm walls / 10 mm slabs; spraying 2–3× faster than troweling | reference mortars cracked within 1 month, HPFRCC did not | p. 27 |
| Railway viaduct | 2005 | surface protection | 10 mm sprayed HPFRCC | lab RC beams: 0.13 vs 0.25 mm crack width after 17 million cycles; carbonation suppressed in accelerated test | p. 30 |
| ECC coupling-beam dampers, Tokyo / Yokohama | 2004 / 2005 | high-rise RC buildings | precast | 1/2.5-scale tests: cracks < 0.3 mm after cyclic loading | p. 26, Fig. 12 → [[rc-member-strengthening]] |

- The retaining-wall repair materials were premixed: A = polymer cement mortar with PVA + high-strength PE (1.5%);
  B = cement mortar with high-strength PVA (2.1%); C = no fibre (Table 3). Products not identified.
- In 2006 only a few companies could supply HPFRCC from ready-mixed plants (p. 31).
- The dam and bridge-deck applications listed as "planned" in 2003 ([[li2003-ecc-review]], p. 225) are reported as
  completed here (Mitaka 2003, Mihara 2004).
- **China (as cited):** HDCC is used in bridge-deck link slabs and monitoring met design requirements (Guo et al. 2016,
  as cited in [[chai2019-hdcc-freeze-thaw-carbonation-flexure]], p. 126).

## Sprayed ECC (primary processing data)
[[kanda2003-sprayed-ecc]] (Kajima/Kuraray; ECC, PVA 2.1 vol.%, W/B 0.32, 30% FA):
- First wet-process sprayed ECC with clear pseudo strain hardening. Pump 6 m³/h, 40 mm × 10 m hose, 8 mm nozzle,
  3 L/min (p. 271, 274). About 10 mm per pass at about 10 min intervals, up to about 80 mm overhead (p. 271).
- An ordinary concrete mixer works if mortar mixing is extended to 15 min with staged water (p. 274).
- Air falls from 12.5–25% after mixing to 6.6–8.4% after spraying (Table 5). → [[fresh-properties]]
- Sprayed specimens exceed 2% ultimate strain and beat placed specimens (2-D fibre orientation) (Fig. 8a, Fig. 10 ⚠️ read).
- **vs repair mortar:** ECC 5.8 MPa / 4.4% vs SBR polymer cement mortar (PCM, the dominant Japanese repair material)
  3.74 MPa / 0.016% at similar f'c (59 vs 53 MPa) (Table 7).
- **Anti-spalling (tapered-pin corrosion simulation):** ECC first-crack COD 24–49 µm (mean 36) vs PCM 50–78 µm (mean 67)
  (Table 8); at 10 mm pin displacement ECC COD < 0.3 mm vs PCM 0.5–1 mm, and ECC keeps carrying load (Figs. 13–14).
  Corrosion cracking at about 3.2–3.6 mm pin displacement vs 0.5–1 mm estimated for normal concrete (Table 8, p. 279).
  → [[chloride-and-corrosion]]
- Recommends testing sprayed ECC on specimens sprayed in 10 mm layers, not cut-outs from massive blocks (Conclusion 3).

Sprayed ECC in structural tests: [[wang2019-rc-beam-ecc-shear-strengthening]] sprayed PVA-ECC in 20–40 mm layers onto
chiselled, saturated-surface-dry RC over an interface agent (0.85 cement + 0.05 SF + 0.1 expansive agent + 0.3 water, by
mass) (Sect. 3.1). Sprayed ECC strain-hardens comparably to cast ECC (Kim et al. 2004, as cited there; not verified in
that paper). → [[rc-member-strengthening]]

## Repair layers: design notes
- UHP-SHCC is aimed at thin surface-protection repair layers 30–70 mm deep (Kunieda & Rokugo 2006; JSCE 2007, as cited in
  [[kunieda2010-uhp-shcc-steel-reinforcement]], abstract, §3.1). Small reinforcement ratios (≤ 1%) are suggested to
  ensure crack distribution in such layers, not to strengthen (§1–2): unreinforced 50 mm members lost strain hardening,
  while D6 bars at ρs 0.3% restored it (Table 3). → [[dogbone-uniaxial-tension]]
- A zero-span (crack-elongation) test should be developed for HPFRCC repair layers ([[kunieda2006-hpfrcc-japan-applications]], p. 23).
  → [[single-crack-test]]
- No-slump HSHDC (NSHSDC) is room-cured and holds its shape, suited to in-situ casting around existing members, unlike
  heat-cured UHPC ([[yuan2020-nshsdc-beam-strengthening]], §1).
- HSDC skins of 5–20 mm cast on chiselled NC walls ([[lee2021-hsdc-wall-emi-impact]], §2.1). → [[extreme-loading-applications]]
- Applications in [[xue2023-shcc-structural-review]] Table 1 (as cited): sprayed ECC repair (Kim 2004), PP-ECC in railway
  beam–column joints (Zhang 2015), ECC layer improves fatigue life (Leung & Zhang 2007), SHCC layer improves RC slab impact
  resistance (Mahmoud 2020), permanent formwork PDCC (Leung & Cao 2010), roughened interface and thicker layer reduce
  delamination (Wang 2020).

## Earlier points (2003 review and Chinese design work)
- **Bridge-deck link slab:** an ECC strip in a concrete sandwich reached 1.3% overall tensile strain while the concrete
  stayed uncracked (Zhang et al. 2002, as cited in [[li2003-ecc-review]], Fig. 12); a full-scale test showed feasibility
  (Kim et al. 2003b, as cited, p. 222).
- Chinese PVA-HDC is designed with link slabs in mind, giving a temperature-specific bilinear tension model
  ([[chai2023-hdc-ambient-temperature]], Fig. 2, Table 7). → [[tensile-constitutive-model]]
- **Repairs avoid delamination and spalling** because ECC's tensile strain capacity accommodates shrinkage mismatch
  (Lim & Li 1997, as cited in [[li2003-ecc-review]], p. 225).
  - Refinement: 10 and 30 mm SHCC strengthening layers ended in debonding ([[xue2023-shcc-structural-review]], Section 4.1,
    as cited), and all 40 mm sprayed ECC layers debonded ([[wang2019-rc-beam-ecc-shear-strengthening]]). Delamination is
    avoided under shrinkage but not necessarily under structural load. → [[interface-bond]]
- **Processing routes:** sprayed, extruded and self-compacting ECC ([[li2003-ecc-review]], p. 216, 226).

> Synthesis: the only quantitative field record (Gifu wall, second-hand) shows sprayed HPFRCC keeping cracks at
> ≤ 120 µm after 24 months vs 300 µm for repair mortar. This is above the < 100 µm ECC convention and above the
> 50–60 µm self-healing range, so field crack widths grow with time and should not be assumed equal to lab values.
> → [[crack-width]], [[self-healing]]

## Conflicts & open questions
- No primary field monitoring paper is in the corpus; long-term field data (> 24 months) are missing. → [[gaps]]
- Experimental proof that ECC's smaller COD slows rebar corrosion is lacking; larger-scale tests of sprayed ECC retrofit
  are needed ([[kanda2003-sprayed-ecc]], p. 279, 281).
- Gaps stated by [[kunieda2006-hpfrcc-japan-applications]] (§4): quantitative required performance (how much ductility
  structures need), supply capacity and QC for in-situ HPFRCC, prediction tools, cost and life-cycle costing.

## Related
- [[rc-member-strengthening]] · [[durability]] · [[extreme-loading-applications]] · [[crack-width]] ·
  [[interface-bond]] · [[freeze-thaw]] · [[carbonation]]
