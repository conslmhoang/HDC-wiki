---
type: application
slug: extreme-loading-applications
aliases: [blast resistance, impact resistance, protective structures, resilient infrastructure, EMI shielding, protective walls]
tags: [application]
sources: [ranade2017-hshdc-impact-resistance, ranade2015-hshdc-tensile-rate-effects, su2023-rubber-modified-hshdc, li2003-ecc-review, lee2021-hsdc-wall-emi-impact, mechtcherine2011-shcc-high-strain-rate, kunieda2006-hpfrcc-japan-applications]
updated: 2026-10-20
---

# Extreme-Loading Applications (impact, blast, seismic devices)

## Key points
- **Unreinforced slabs:** HSHDC slabs survive 20 repeated drop-weight impacts without punching or spalling, while
  FR-UHPC fails ([[ranade2017-hshdc-impact-resistance]]). → [[impact-resistance]]
- **Dynamic tension:** HSHDC keeps about 2.7–2.9% ductility up to 10 s⁻¹
  ([[ranade2015-hshdc-tensile-rate-effects]]). → [[strain-rate-effects]]
- **PVA-SHCC at high rate** (TU Dresden): ε at peak falls from 1.49% to 0.82% (10⁻⁵ → 10⁻² s⁻¹), then rises to 1.79% at
  50 s⁻¹, with σ_t 11.93 MPa but **no multiple cracking** at ≥ 10 s⁻¹ ([[mechtcherine2011-shcc-high-strain-rate]], Table 2,
  p. 58–59). Strain rates of load cases: earthquake 5·10⁻³–5·10⁻¹ s⁻¹, pile driving 10⁻²–1 s⁻¹, aircraft landing
  5·10⁻²–2 s⁻¹ (Banthia 2004, as cited there, p. 51).
- SHCC under projectile impact shows almost no scabbing or spalling and absorbs more energy than NSC/HSC (Maalej 2005,
  as cited in [[mechtcherine2011-shcc-high-strain-rate]], p. 52).
- The GDUT group claims R-HSHDC is suitable for seismic, impact, blast and military use, but did not test any of these
  ([[su2023-rubber-modified-hshdc]], p. 12).

## Protective walls: HSDC skins for impact + EMI shielding (Lee 2021, primary)
Korea Univ. HSDC (1.0% steel + 0.5% PE, f'c ≈ 122 MPa, room-cured; strain hardening asserted, not shown) cast as 5/10/20 mm
skins on one (S) or both (D) faces of 100 mm NC panels ([[lee2021-hsdc-wall-emi-impact]]). → [[hybrid-fiber]]

| Outcome | Result | Location |
|---|---|---|
| EMI shielding (400–1400 MHz) | a 5 mm single HSDC layer on 100 mm NC shields more than a 200 mm plain NC panel; SE rises with thickness; double layers +1.5–9.1 dB over single at 600–1400 MHz | §3.1, Figs. 6a, 7a |
| SE source | steel fibres form the conductive network; PE is non-conductive | §3.1 |
| Impact, single layer | H5S failed at blow 2, H10S and H20S at blows 4–5, by scabbing of the unstrengthened face | Fig. 8 |
| Impact, double layer | H20D total reaction force 2.2× H5D and 1.6× H10D; energy to failure of H20D > 5× H5S | Figs. 9, 11 |
| Crack width | H20D bottom about 0.05 mm after blow 1, 0.70 / 1.10 mm after blows 4 / 5; H5D, H10D 5.0 / 5.5 mm | §3.2.1 |
| Post-impact SE loss | about 7.1% (20 mm) vs 24.7% (thinner layers, spalling) | §3.2.2, Fig. 12 |

- Test: incremental-height drop weight, 100 kg → [[impact-test]]. One panel per configuration.
- These are NC panels with HSDC skins, not reinforced members, so the gap "reinforced HSHDC members under impact" is
  only partly addressed.

## Gaps stated by [[ranade2017-hshdc-impact-resistance]] (p. 35)
- Kolsky bar and shock-tube tests at rates 2–3 orders of magnitude higher.
- Reinforced HSHDC members, assessed by penetration, crater, perforation, mass loss and frangibility.
- HSHDC vs ECC under impact, to separate the role of f'c.
- High temperature and PE melting under blast. → [[high-temperature-behaviour]]

Further stated gaps: SHCC data above 1 s⁻¹ are scarce, and why PVA-SHCC switches back to pull-out at very high rates is
unexplained ([[mechtcherine2011-shcc-high-strain-rate]], p. 51, 60–61); combined EMI-shielding and impact evaluation of
strengthened structures is lacking ([[lee2021-hsdc-wall-emi-impact]], §1).

## Seismic devices
- As cited in [[li2003-ecc-review]] (p. 224–225): coupling beams and dampers (Fukuyama 1999, 2002), self-centring frames
  (Fischer & Li 2003b), and unbonded post-tensioned bridge piers with ECC hinges (Yoon & Billington 2002).
- Built: ECC coupling-beam dampers in high-rise RC buildings in Tokyo (2004) and Yokohama (2005); 1/2.5-scale tests gave
  cracks < 0.3 mm after cyclic loading ([[kunieda2006-hpfrcc-japan-applications]], p. 26, Fig. 12). → [[rc-member-strengthening]]

> Synthesis: PE-based HSHDC keeps multiple cracking up to 10 s⁻¹ (Ranade 2015), whereas PVA-SHCC loses it at ≥ 10 s⁻¹
> while still gaining strength and strain (Mechtcherine 2011). For impact-resistant skins, Lee 2021 shows that layer
> thickness and placing the HSDC on the **rear (tension) face** matter more than the material alone: single front-face
> layers fail by rear-face scabbing.

## Related
- [[impact-resistance]] · [[hshdc]] · [[strain-rate-effects]] · [[impact-test]] · [[hybrid-fiber]]
