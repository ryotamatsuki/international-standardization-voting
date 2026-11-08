# P1-KS research decision after four-paper literature audit and arbitrary-K quota extension
Date: 2026-11-09 JST
Branch: research/p1-proof-novelty-gate-20261108
Status: independent analytical recommendation; not referee acceptance forecast.

## What changed

1. [Exact general-h/population proof](../proofs/p1_ks_general_installed_base_population_20261109.md) moved from a single h=1/p=example to a 2-D interval of historical installed bases and an open simplex of nation populations. It proves \(\partial_\beta\tau_o,\partial_\beta\tau_c,\partial_h\tau_o>0\) on that rectangle, conditional on selected interior FE pricing.
2. [New K-country and ownership theorem](../proofs/p1_ks_K_country_ownership_quota_20261109.md) derives arbitrary national payoff thresholds with four global firms and arbitrary K countries, shows world efficiency plus exact ownership/population alignment implies unanimous support, and constructs a world-welfare-improving approval-to-rejection reversal for any K>=2, any quota 2<=q<=K through divisible ownership of incumbent firms. The exact proof is conditional on selected price continuations and uses a deliberately constructed equity distribution. q=1 cannot reject world-welfare-positive F under sincere votes if national payoffs sum to world welfare.
3. [Four paper audit](../literature/p1_ks_four_paper_theorem_crosswalk_20261109.md) substantially narrows plausible novelty. Barrett & Yang WP propositions 1,3,4,6,7 cover major installed-base/government-opposition mechanisms; Klimenko already studies network-intensity-dependent protectionist compatibility and inefficient trade outcomes; Cheng & Huang study incompatibility with strong network effects under firm veto; Bertoletti shows complete market coverage is crucial for compatibility welfare.
4. New nearby prior art Geng (2019) and standards coalitions Casella (1996/2001) must be part of final draft's literature mapping, though not a current audited theorem-level overlap.

## Editorial assessment

- **Don't continue generalizing K or q alone**. Their solution here is a simple composition of existing firm-level operating-profit changes and elementary quota arithmetic. Formal generality does NOT imply a genuinely new economic mechanism.
- The pricing model still has only 4 firms, identical per-capita consumers across countries and a full-market-coverage assumption. "General market competition structure" has NOT been solved.
- The current strongest comparison-static statement remains \(h,\beta,\omega,w\) dependent cross-country political opposition despite positive global gain, but prior work directly threatens the installed-base/government-preservation part. The K construction itself does not resolve this.
- Mathematical soundness of full SPNE still conditional on chosen interior-price candidates' unproved nonlocal global price Nash; refrain from unconditional SPNE claims.
- Scope of four-paper audit: the public WP of Barrett-Yang and Bertoletti were inspected; publisher's abstract/intro of Klimenko and publisher preview/appendix of Cheng-Huang were inspected; exact full published theorem noncontainment cannot be certified for the latter two. Do not equate access gaps with novelty.

## Recommended next decisive research fork

**Gate A (novelty, first):** finish unavailable Klimenko/Cheng-Huang public-version comparison if legally accessible, and explicitly test the most relevant existing results against the national-size/ownership threshold family. If all economics follows from standard installed-base rent shifting plus vote counting, abandon novelty claims for K-country generalization.

**Gate B (single substantive mechanism, only if Gate A leaves promise):** rather than increase firm count, examine a small endogenous institutional choice that changes market payoffs and adoption, e.g. a proposer chooses compatibility *scope* \(x\) before national voting (P2) and after which firms voluntarily join. Check that outcome isn't mechanically a cheap voting constraint or a restatement of Farrell-Simcoe/Spulber; no blank check to build arbitrary new stages.

**Gate C (minimum mathematical validity):** prove selected FE price candidate is a global best reply in the relevant adopted outcome technology profiles plus any unilateral technology-deviation profiles needed to establish stage-2 Nash. All sixteen price equilibria may be needed if a full subgame-perfect plan is asserted; **price uniqueness of all arbitrary price equilibria is NOT necessary**.

**Submission strategy:** If the resulting difference from prior art is narrow but real, favor a focused theoretical submission emphasizing country-size / equity incidence of standards, with K theorem as a short robustness corollary/appendix. Review Journal of Economics, Research in Economics and Journal of Industry, Competition and Trade for editorial fit; do not assume a lower-tier venue ignores novelty. For IJIO-level ambition the present generalization alone is insufficient, absent new non-obvious economic mechanism.

**Stop rule:** Do not invest in general M-firm Salop, arbitrary demand families, free-form international bargaining or full ISO procedure until there is a precise economics question whose answer changes, and a named prior-art theorem against which the change can be assessed.

## Reproduction

[Code](../code/verify_ks_K_country_quota_20261109.py) certifies main voter, world gain and blocker threshold interval inequalities using exact rational bivariate Bernstein coefficients and verifies K=2,4,5,6,8,12,20 with q variants. The broader h rectangle and 16 adoption states were separately checked in [previous code](../code/verify_ks_general_hw_20261109.py).
