# P1-KS: general K-country, ownership, and supermajority quota — existence and no-go results

Date: 2026-11-09 JST
Branch: research/p1-proof-novelty-gate-20261108
**Proof status:** EXACT algebraic voting/ownership aggregation and EXACT SymPy interval sign checks **conditional on the selected interior fulfilled-expectations (FE) price continuation for the four-firm product market**. **NOT** a proof of global nonlocal differentiated-price Bertrand optimality or unconditional full-game SPNE. **NOT** a first-in-literature claim.

## 1. Honest scope

- Keep **exactly four production firms** at Salop points 0,1,2,3, and all sixteen voluntary standard-adoption states.
- Allow **K arbitrary national markets and national standardization bodies**, K>=2, with total demand N and positive national population shares w_i summing to 1. Consumers in all countries have the same per-capita circular preferences.
- Allow every firm j's **worldwide residual profit** to be held by national investors with nonnegative shares omega_{ij}, summing to one across all K countries **for every firm**: sum_i omega_{ij}=1. These are national claims to profits (fractional cross-border ownership is explicitly allowed); a country may hold zero equity. This is a new ownership primitive compared with "one country owns one firm."
- All national bodies have one valid yes/no ballot. Publication needs q votes, q integer in {1,...,K}. This generalizes 3-out-of-4, *not* the full ISO abstention/technical-vote rule.
- The entrant's real joining fee k_L after publication and k_H after rejection remains an **exogenous** institutional input. When borne proportionally by entrant owners, the national fee of state i is omega_{i3}*k_L after approved F and 0 in rejected O.
- Common installed base is B_j=hN per firm, with beta in [0.1,0.5] and h in [0.75,1.25]. Use N=1, k_L=0.01, k_H=0.4 for the exact constructive theorem.

The old selected product-market continuation has in the old O=1110 state gross **per-N** profits pi_o^O for outer firms (0,2), pi_c^O for central firm 1 and pi_e^O for entrant 3, and per-circular-consumer surplus C_O. At approved F=1111 every firm has gross per-N profit 1/4. Define:

\[
d(\beta,h)=[C_F-C_O]/4>0,\quad
\ell_o=\pi_o^O-1/4>0,\quad
\ell_c=\pi_c^O-1/4>0,\quad
g=1/4-\pi_e^O>0.
\]

The normalized world gain (N=1) when publication induces F and rejection preserves O is
\[
S=d-2\ell_o-\ell_c+g-k_L>0.
\]
The exact source formulas and certified two-dimensional signs are in [general-h population theorem](p1_ks_general_installed_base_population_20261109.md).

## 2. Theorem K1 — general national-payoff representation

For each voting country \(i\in\{1,\ldots,K\}\),
\[
\boxed{\Delta W_i
=w_i d-(\omega_{i0}+\omega_{i2})\ell_o-\omega_{i1}\ell_c+
\omega_{i3}(g-k_L).}
\]
For general N, replace d, l_o, l_c, g by their N-scaled flow amounts and leave real k_L outside the N factor.

This formula reflects domestic per capita consumer-surplus improvement, worldwide profits flowing to national owners, and each entrant owner's share of real adaptation costs. Since \(\sum_i w_i=1\) and \(\sum_i\omega_{ij}=1\), \(\sum_i \Delta W_i=S\). In contrast, a single nation does not internalize worldwide consumer benefits or other nations' firm profits.

Define the critical national-population share
\[
\boxed{T_i(\beta,h,\omega_i)
=\frac{(\omega_{i0}+\omega_{i2})\ell_o+
\omega_{i1}\ell_c-\omega_{i3}(g-k_L)}{d}.}
\]
With sincere ballots and indifference-to-Yes convention, country i votes Yes iff \(w_i\ge T_i\). T_i can be **negative** if country i chiefly owns the benefiting entrant.

## 3. Proposition K2 — monotone support for incumbent owners (structurally restricted)

For any country **without entrant equity**, omega_{i3}=0, define \(\rho_i=\omega_{i0}+\omega_{i2}\), \(\sigma_i=\omega_{i1}\). Then
\[
T_i=\rho_i\tau_o+\sigma_i\tau_c,\qquad
\tau_o=\ell_o/d,\qquad\tau_c=\ell_c/d.
\]
The previous exact bivariate interval certificates show \(\partial_\beta\tau_o>0,\partial_\beta\tau_c>0\) over the tested rectangle. Hence \(\partial_\beta T_i>0\) whenever \(\rho_i+\sigma_i>0\). Such a country may cross from Yes to No **at most once** over the beta interval. Countries holding only entrant shares strictly vote Yes (because d>0,g>k_L), as do countries with no ownership.

If *every* voting country either owns only incumbents, owns only the entrant, or owns no firm, the sincere Yes count is weakly decreasing in beta over the tested rectangle, and approval is a lower interval or empty/full interval. Its critical threshold is an **order statistic** of individual beta crossing values, conditional on fixed q and fixed no-reversal always-Yes voters. This is vote arithmetic built upon the product-market sign result, NOT itself a novel voting theorem.

**Important caution:** If countries hold a mixture of incumbent and entrant shares, the above monotone-support result is **not automatic**. The ratio (g-k_L)/d is not globally monotone even for h=1; its derivative is positive at beta=.1 and negative at beta=.5. Therefore do not assert a global monotone voting result for unrestricted ownership matrices.

## 4. Proposition K3 — exact no-go benchmark with aligned interests

Suppose **every firm** is owned internationally in the same proportions as national consumer market shares: \(\omega_{ij}=w_i\) for all i,j, and the entrant's resource cost is borne in the same ownership proportions. Then
\[
\boxed{\Delta W_i=w_i S.}
\]
Since S>0 over the rectangle and w_i>0, **every country strictly supports approval**. Under any valid q<=K the standard passes when voters vote sincerely.

This establishes that ownership–market-size nonalignment is **necessary within this aligned benchmark** for inefficient rejection. It is **not** a general characterization saying that nonalignment is sufficient or that exact proportionality is the only way to avoid rejection.

## 5. Proposition K4 — constructive family for ALL K>=2 and q>=2

Fix any integers K>=2 and 2<=q<=K. Let r=K-q+1>=1 be the **minimum number of No votes needed to fail approval**.

Hold the same four-firm Salop/FE candidate continuation and common installed base h in [3/4,5/4]. Allocate firm-0 ownership equally among **r distinct small-population countries**, each owning omega_{i0}=1/r and no other firm. Give each of these countries population w_i=(3/25)/r, so the total population of prospective opponents is exactly 0.12.

Give one remaining country ownership of **all of firms 1,2,3**, including firm3's k_L resource cost. If q>2, give it population 0.87 and distribute population 0.01 among q-2 additional *consumer-only* countries; if q=2, give it population 0.88 (no extra consumer-only countries).

This fully specifies K positive country masses, normalized four-firm national profit shares, and 1 vote per country.

Each of the r prospective opponents has welfare change
\[
\Delta W_i=(0.12\,d-\ell_o)/r
=\frac{d}{r}(0.12-\tau_o(\beta,h)).
\]
Exact certificates from the general-h P1 analysis verify, **uniformly in h in [0.75,1.25]**,
\[
\tau_o(0.1,h)<0.104<0.12<0.125<\tau_o(0.5,h).
\]
Therefore each opponent votes YES at beta=.1 but NO at beta=.5.

Every consumer-only country has positive welfare change (since d>0). The one country owning firms 1,2,3 has at least
\[
\Delta W_{\mathrm{main}}\ge
0.87d-\ell_o-\ell_c+g-k_L>0
\]
throughout the entire beta-h rectangle. An independent bivariate Bernstein certificate verifies its positive numerator **and denominator** throughout the rectangle; no endpoint interpolation guess is used.

Thus, for any such K,q, and **any h in [0.75,1.25]**:
- at beta=.1 all **K** nations vote Yes, and approval passes;
- at beta=.5 exactly **q-1** nations vote Yes, and the standard fails;
- world welfare when approval induces F relative to rejection O remains **strictly positive**, across the rectangle;
- the incumbent adoption profiles O (rejection) and F (approval) are strict adoption equilibria **conditional on the same selected price continuation** as in the preceding common-h model. For the voting conclusion apply sincere voting / a finite-game weak-dominance refinement.

This is a constructive existence theorem, **not** the assertion that every arbitrary ownership distribution or quota generates reversal. It uses divisible cross-border equity and permits national voters with no company ownership, which become especially salient for large K. Treat these assumptions as an economic limitation rather than hide them.

**Limit q=1:** Since world gain \(\sum_i\Delta W_i=S>0\), at least one country has positive approval gains; hence with q=1 a welfare-improving standard **cannot be rejected under sincere voting**. This proves the lower quota boundary. It does not rule out unrefined nonpivotal voting Nash equilibria.

Numerical exact rational checks of the construction:

| K | quota q | required blocking No r=K-q+1 | Yes at beta=.1 | Yes at beta=.5 |
|---|---|---|---|---|
| 2 | 2 | 1 | 2 | 1 |
| 4 | 3 | 2 | 4 | 2 |
| 5 | 4 | 2 | 5 | 3 |
| 6 | 5 | 2 | 6 | 4 |
| 8 | 6 | 3 | 8 | 5 |
| 12 | 9 | 4 | 12 | 8 |
| 20 | 15 | 6 | 20 | 14 |
| 20 | 20 | 1 | 20 | 19 |

The world normalized welfare differences at h=1 are +0.17159203635 at beta=.1 and +0.73577256944 at beta=.5 for every K,q, because the **same four-firm global product market** and full allocation of world ownership/costs are retained.

## 6. What is and is not economically substantive

Strongest result is the **conditional national support threshold**, with the proof that \(\tau_o,\tau_c\) rise in beta under KS market feedback. The K,q construction shows that rejection is **not an artifact of exactly four countries or the original one-firm-one-country mapping**, but the proof mostly distributes the existing four-firm payoff differences across additional voters. That is economically transparent **but not automatically a nontrivial new economic mechanism**.

The aligned-ownership no-go illustrates why national voting rights might diverge from consumer-market size and worldwide profit entitlements. This is elementary welfare accounting and must **not** be independently advertised as an original discovery.

The literature remains an obstacle: Barrett–Yang already identifies installed-base/standards resistance, Klimenko considers network-effect-induced strategic compatibility policy, Cheng–Huang shows veto-driven incompatibility, and Bertoletti shows market coverage alters compatibility welfare conclusions. See [four-paper crosswalk](../literature/p1_ks_four_paper_theorem_crosswalk_20261109.md). Do NOT turn a lack of full published theorem access into a novelty assertion.

## 7. Reproducibility and limits

- Reproducible stand-alone SymPy script: [code/verify_ks_K_country_quota_20261109.py](../code/verify_ks_K_country_quota_20261109.py).
- It checks six exact bivariate/endpoint Bernstein positivity conditions, arbitrary K,q ownership-share accounting, exact vote counts for K=2,4,5,6,8,12,20 and multiple common h levels.
- Previous exact [common installed-base and population analysis](p1_ks_general_installed_base_population_20261109.md) checks sixteen standard-adoption configurations and incumbent adoption incentives.
- **No nonlocal global price-Best-Response proof** for the underlying rational-expectations 4-firm pricing; no unconditional full-SPNE statement.
- **No theorem claiming a general M-firm Salop price market** or market-coverage robustness: the product market still has exactly four firms; only the ownership/national voting game was generalized.
- **No proof of universal prior-art noncontainment**, in particular because the complete published propositions of Klimenko (2009) and Cheng–Huang (2025) were not accessible.
