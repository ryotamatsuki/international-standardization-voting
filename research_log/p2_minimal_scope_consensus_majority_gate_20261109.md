# P2 / original candidate ③: editorial go/no-go after minimal ISO-style proposal-scope model
Date: 2026-11-09 JST
Branch: research/p1-proof-novelty-gate-20261108

## Research question
Does a 'consensus-like' strict unanimity requirement induce undershooting while 3-of-4 qualified voting induces overshooting of the world-welfare-maximizing interoperability scope, *after Gandal–Shy style four-firm price competition and firms' voluntary standard adoption are solved*?

## Actual results obtained
1. Exogenous installed-compatibility-brand benefits and a **continuous new gateway strength x**. The entire 4-firm price vector, firm profit vector and nation consumer surplus are analytically derived.
2. **No-go result** under **only entrant's privately borne quadratic joining cost**: if entrant chooses to join, world net welfare is strictly increasing at x. The original reduced-form "unanimity under, majority over" cannot simply be imported into this minimal product-market/adoption game. Incumbent nation support also has no upper-x participation cutoff absent country-specific costs.
3. **Constructive positive result with a national external adjustment expense**: add an unavoidable c0*x² cost to nation0, outside four firms' private optimization. With d=1/3, w=(.22,.40,.14,.24), entrant joining cost .01*x², c0=.30*x² and nation1 as the agenda setter maximizing its own national payoff:
   - strict unanimity q=4 -> xU=2842/19097≈.148819;
   - unconstrained world optimum -> xW=6925/8869≈.780810;
   - q=3 with nation1 as proposer -> xQ=1;
   - world gains at xU,xW,xQ respectively 0.0575532,0.1668860,0.1537346.
   Changing only c0 to .50 gives xU=.0886546, xW=.4511695, and net welfare under q=3 at x=1 is **negative** (-.0462654), versus +.0341737 under strict unanimity.
4. **Pricing proof upgraded beyond previous KS-FE limitation for this new *brand-weighted* P2 game**. A geometric global Bertrand best-response lemma and 896 exact strict affine interval inequalities demonstrate the selected price vector is globally optimal against each unilateral price deviation in all sixteen adoption technology subgames for d=1/3, x in [0,1]. Price-game existence is established, not uniqueness of all equilibria.
5. All 16 adoption states: 21 strict/3 indifferent incumbent L actions; entrant strictly chooses gateway when all three incumbents use L and x>0. The finite adoption-stage trembling-hand refinement selects F_x under approval (subject to named low-cost published interface) and O under rejection (subject to unavailable/high-cost private adapter). Full game has other unrefined equilibrium outcomes.

## Economics / novelty assessment

- The exact scope *inequality* \(x^U<x^W<x^Q\) is real and market-grounded but mechanically enabled by an added uncompensated high adjustment cost imposed on country0, not something Gandal–Shy competition or voluntary adoption alone generates.
- **Major caveat:** Country 0's c0*x² cost must remain unavoidable even though ISO standards and firm technology adoption are voluntary, requiring credible economic microfoundation (e.g. adverse effects on existing infrastructure through competitors' integration), rather than an assumed mandatory compliance fee. If citizens could just opt out and avoid it, the construction needs to be recomputed.
- A national agenda-setter who strictly wants maximal x was obtained from its **endogenous national payoff**, but proposer identity and exclusive proposal right are exogenous. Welfare-maximizing proposer need not produce overcompatibility.
- The firm adoption stage is **not binding** on the realized approved path; the same x-choice would follow with automatic implementation. Thus the core result doesn't yet identify an interaction where ISO approval and voluntary adoption create a genuinely new distortion.
- **Prior art:** Goerke & Holler (1995) specifically study how majority rules alter welfare in standards with network externalities; Farrell & Simcoe (2012) study consensus governance and delay without substantive compromise; Spulber (2019), *Economic Journal* Proposition 6, proves market/SSO voting efficiency with appropriate incidence conditions. Our departure from Spulber is different country-specific real costs and proposal agenda, not a contradiction.
- **Institution:** 2026 ISO/IEC consensus explicitly need not imply unanimity; q=4 is a benchmark, q=3 a four-valid-ballot FDIS simplification. The two are not a faithful description of a *sequential* technical consensus plus FDIS stage.

## Editorial decision
**Do NOT claim a new journal-ready result from candidate③ yet.** Mathematically the conditional model has a sound scope counterexample, but the key national adjustment cost is a delicate new assumption and the central mechanism resembles known veto/majoritarian external-cost logic.

Recommend a strictly limited **one-microfoundation gate**:
- Try to explain c0*x² as a *real and unavoidable consequence of foreign companies' voluntary interoperability investment*, with country0's domestic users or complementors not able to opt out at zero cost. Model that mechanism explicitly and check that both strict adopter equilibrium and the triple ordering survive.
- Compare the resulting mechanism to Goerke–Holler and Spulber's exact published propositions. If it reduces to an exogenous country's veto loss, do not keep expanding.
- If there is no credible microfoundation within one extra primitive, retain P2 as a **negative/diagnostic research note**, and prioritize the earlier P1/KS manuscript's most distinctive economically significant comparison statistic.

**Files:** [proof](../proofs/p2_minimal_scope_unanimity_majority_20261109.md); [verifier](../code/p2_unanimity_vs_majority_20261109.py); literature sources:
Goerke-Holler 1995 https://ideas.repec.org/a/kap/pubcho/v83y1995i3-4p337-51.html ;
Farrell-Simcoe 2012 https://doi.org/10.1111/j.1756-2171.2012.00164.x ;
Spulber 2019 https://doi.org/10.1111/ecoj.12606 ;
ISO Directives 2026 https://www.iso.org/sites/directives/current/consolidated/
