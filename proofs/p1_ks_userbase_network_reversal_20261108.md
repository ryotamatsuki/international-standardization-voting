# User-count network effects in P1: independent reversal check (2026-11-08)

**Status: constructive, analytically verified reversal in the selected interior-price continuation; NOT a proof of global price-Nash uniqueness or an unconditional full-game SPNE theorem.**

## Primitive changes relative to P1

Keep four countries/one national firm per country, national weights \(w=(3/25,1/2,3/25,13/50)\), total current-market population \(N=1\), length-4 quadratic Salop circle, one valid Yes/No ballot per country (three Yes required), and 16 simultaneous voluntary technology adoption choices after publication.

Replace the old exogenous brand-count quality bonus by endogenous user counts:

\[
u_j^k(x)=V-p_j^k-\operatorname{dist}(x,j)^2+\beta\left(\sum_{l\in g(j)} B_l/N+\sum_{l\in g(j)} Q_l/N\right).
\]

The old three firms \(0,1,2\) share \(L\); firm 3 starts with distinct \(M\). An incumbent declining \(L\) uses a private singleton \(X_i\). In this existence example each firm's **installed base** is \(B_j=N\), so pre-publication legacy \(L\) has \(3N\) previously installed users while \(M\) has \(N\). Installing \(L\) merges the installed bases; this assumes legacy users remain interoperable or are supported by the implementation. The actual current network size \(Q_l\) is endogenous and includes each firm's sales worldwide. The strong brand-count assumption of the old P1 is absent (\(\theta=0\)).

Implementation costs for firm 3: \(k_L=1/100\) after publication; \(k_H=2/5\) if unpublished. Existing firms' continuation costs remain zero. A public standard reduces implementation cost **exogenously**; no institutional microfoundation has been proved.

## Rational-expectations product-market pricing (interior continuation)

With \(L\) the length-four circle Laplacian (diagonal 1, adjacent -1/2), and \(H(s)\) the same-compatible-network membership matrix, define the world-average demand-density vector \(\bar q=\sum_k w_k q^k\) and installed base vector \(B/N={\bf1}\). Under adjacent boundaries,

\[
q^k={\bf1}-Lp^k+L a,\quad
a=\beta H({\bf1}+\bar q/4),\quad
C=I-\beta LH/4,\quad T=C^{-1}L.
\]

Demand/network expectations are fulfilled by solving the fixed point. In the differentiated-price game, the cross-country demand feedback is internalized in each firm's **worldwide** payoff. First-order conditions, for any destination \(k\), are

\[
q_i^k-p_i^k-(T_{ii}-1)\bar p_i=0,\qquad \bar p_i=\sum_k w_k p_i^k.
\]

Subtracting market \(k\) and market \(\ell\) FOCs and the associated demand equations yields \((I+L)(p^k-p^\ell)=0\), hence **all price candidates coincide across countries** despite feasible destination price discrimination. In the common-price continuation,

\[
p=(T+\operatorname{diag}(T_{ii}))^{-1}C^{-1}({\bf1}+\beta LH{\bf1}),\qquad
q=C^{-1}({\bf1}-Lp+\beta LH{\bf1}).
\]

This is a **verified interior price FOC solution**, not yet proof of the only global Bertrand Nash equilibrium for every adoption state.

For the 3+1 state \(O=(L,L,L,M)\):

\[
\begin{aligned}
p_0^O=p_2^O&=(12-\beta)/[4(3-\beta)],\\
p_1^O&=(24-5\beta)/[8(3-\beta)],\\
p_3^O&=(12\beta^2-41\beta+24)/[8(3-\beta)],\\
q_0^O=q_2^O&=(8-3\beta)(12-\beta)/[16(3-\beta)(2-\beta)],\\
q_1^O&=p_1^O,\qquad
q_3^O=(12\beta^2-41\beta+24)/[4(3-\beta)(2-\beta)].
\end{aligned}
\]

For all-compatible \(F=(L,L,L,L)\), all \(p_i=q_i=1\), and the network utility bonus is \(5\beta\) for each product.

The source-checking script tested **all 16 adoption profiles at \(\beta=1/10,1/2\) with exact rational arithmetic**, verifying prices positive and neighboring consumer boundaries strictly inside \((0,1)\). Separate symbolic Bernstein-basis tests certify interior-price positivity and boundary regularity throughout \(\beta\in[1/10,1/2]\) for the six rotation classes.

## National preferences and exact sign reversal

Let \(C(s)\) denote per-circle consumer surplus with the common \(4V\) term omitted, and \(\Pi_i(s)=p_i(s)q_i(s)/4\) worldwide operating profit for \(N=1\). Governments maximize \(W_i=w_i C(s)/4+\Pi_i(s)-{\bf1}_{i=3,s_3=1}k_A\).

Relative to rejection/three-compatible \(O\), the acceptance/fully-compatible \(F\) payoff is

\[
\Delta W_i=w_i \Delta C/4+(\Pi_i^F-\Pi_i^O)-{\bf1}_{i=3}k_L,\quad
\Delta C=C(F)-C(O).
\]

Key closed forms:

\[
\Delta C=\frac{\beta(7\beta-16)(128\beta^3-1023\beta^2+2556\beta-1944)}
{128(\beta-3)^2(\beta-2)^2},
\]

\[
\Delta \Pi_0=\Delta \Pi_2=
\frac{\beta(61\beta^2-432\beta+720)}{256(\beta-3)^2(\beta-2)}<0.
\]

With \(w_0=w_2=3/25\),

\[
\boxed{\Delta W_0=\Delta W_2=
\frac{\beta(2688\beta^4-24577\beta^3+75080\beta^2-84312\beta+21312)}
{12800(\beta-3)^2(\beta-2)^2}.}
\]

The unique internal root in \([1/10,1/2]\) is \(\beta^*\approx0.349670283323148\). Exact polynomial positivity in a Bernstein basis proves that the population support threshold

\[
\tau(\beta)=-4\Delta\Pi_0/\Delta C
=-\frac{2(\beta-2)(61\beta^2-432\beta+720)}
{(7\beta-16)(128\beta^3-1023\beta^2+2556\beta-1944)}
\]

has \(\tau'(\beta)>0\) on the entire interval. Thus the two small countries switch from Yes to No, while countries 1 and 3 strictly support approval throughout.

**Exact endpoints, \(k_L=0.01\) included:**

| beta | Delta W0=Delta W2 | Delta W1 | Delta W3 | World net gain | Sincere votes |
|---|---:|---:|---:|---:|---|
| 1/10 | 0.00350153548 | 0.07708268251 | 0.08750628289 | 0.17159203635 | YYYY (approve) |
| 1/2 | -0.01382812500 | 0.35421440972 | 0.40921440972 | 0.73577256944 | NYNY (reject) |

The symbolic country-1, country-3 and world-welfare payoff differences are strictly positive on the entire interval. Network intensity raises potential worldwide gains from full interoperability but can block approval under country-equal voting.

## Endogenous voluntary adoption

At both endpoints \(\beta=1/10\) and \(\beta=1/2\), exact-rational enumeration of all 16 adoption-state continuation payoffs finds the following *pure* Nash equilibria for the specified implementation-cost regimes:
- reject, cost \(k_H=2/5\): \(\{0000,1110\}\);
- approve, cost \(k_L=1/100\): \(\{0000,1111\}\).

The 1110 and 1111 profiles are **strict** equilibria in their respective subgames. On the whole interval, symbolic positivity checks confirm that incumbent firms strictly prefer not to exit those profiles, and entrant 3 prefers joining after approval, not joining after rejection. For the symmetric installed bases, each incumbent L action is strictly preferred whenever any other firm chooses L; it is weakly preferred when nobody else joins (checked exactly at both endpoints). The all-private \(0000\) Nash equilibrium remains unrefined, as in old P1.

The existence of the two strict continuation profiles and sincere national voting, conditional on the selected interior price solutions, recovers the claimed reversal. A full proof of all-price-subgame global Nash equilibrium and uniqueness/refinement of fulfilled-expectations demand equilibria is outstanding.

## Nonlocal price deviation diagnostic

An independent exact-circle Voronoi demand calculator coupled with iterative fulfilled-expectations fixed points sampled **2,928 unilateral uniform-price deviations** for six adoption rotation classes, at \(\beta=1/10,1/2\) and installed base \(B_j=N\). No profitable deviation was found. The 16 selected stage-3 price candidates have strict positive prices and adjacent boundary positions. This numerical diagnostic is **not** an exhaustive continuous-strategy global proof. Nonuniform cross-country price vectors and alternative fulfilled-expectations branches remain to be addressed analytically.

## Comparison with prior art

Katz & Shapiro (1985), *AER*, give the user-based network-effects/compatibility foundation. Stadler, Tobler Trexler & Unsorg (2022), *Networks and Spatial Economics* 22:903–913, explicitly use Hotelling quadratic losses and installed base plus current sales, with partial compatibility. The P1 user-based extension is therefore **not novel merely because it adds user-based externalities**. A new contribution would need to reside in the national-voting/worldwide-profits comparative statics and be checked for theorem-level overlap with Gandal–Shy, Barrett–Yang, Klimenko, Spulber and recent compatibility economics.

## Reproducibility

Exact standalone verifier generated in this session: \`verify_ks_userbase_vote_reversal.py\` (SymPy exact-rational 16-profile checks and Bernstein sign certificates). The script was successfully executed locally on 2026-11-08. Do not conflate finite exact verifications with full pricing Nash global-deviation verification.
