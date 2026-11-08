# Gate 1 — Closed-form global Bertrand equilibrium for P1

**Date:** 2026-11-08. **Status:** a full unilateral-price-deviation proof for the specified Salop game, conditional on the stated market primitives. This is a pure-strategy Nash equilibrium **existence** proof, not a uniqueness theorem.

## Set-up

Four firms at \(0,1,2,3\) on a circle of circumference \(4\). Each country's mass of consumers is uniformly distributed on the circle; per-circle density normalisation gives total circle demand \(4\). Marginal cost is zero and the market is fully covered (take base utility \(V\) sufficiently high). Utility from firm \(j\) at location \(y\):
\[
U_j(y)=V+a_j-p_j-\operatorname{dist}(y,j)^2.
\]
Each firm can choose any **nonnegative** price. Legacy network qualities \(a=(2d,2d,2d,0)\) and \(d\in(0,6/7)\). The candidate equilibrium prices are
\[
p^*=(1+d/3,\ 1+d/6,\ 1+d/3,\ 1-5d/6).
\]
They are all positive and have unit-density sales \(q_i^*=p_i^*\) under locally adjacent shopping boundaries.

### Lemma 1 (price deviation upper bound)

Holding \(p_{-i}=p_{-i}^*\) fixed, **every** price \(z\ge0\) chosen by firm \(i\) satisfies
\[
q_i(z)\le \max\{0,2p_i^*-z\}.
\]
At \(z=p_i^*\), equality holds.

#### Proof

Define \(b_j=p_j^*-a_j\) for all other firms, and let \(y\in[-2,2]\) measure a consumer's clockwise coordinate relative to firm \(i\).

For the right-hand arc \(0\le y\le 3/2\), the neighbor \(i+1\) is at distance \(|y-1|\), so a necessary condition for buying \(i\) rather than \(i+1\) is
\[
z-a_i+y^2\le b_{i+1}+(y-1)^2
\iff y\le R_i(z):=\frac{1+b_{i+1}+a_i-z}{2}.
\]
For the left-hand arc \(-3/2\le y\le0\), a necessary condition for buying \(i\) rather than \(i-1\) is
\[
y\ge-L_i(z),\qquad
L_i(z):=\frac{1+b_{i-1}+a_i-z}{2}.
\]
Substituting the candidate prices yields the following zero-price bounds:
\[
\begin{array}{c|cc|c}
i&R_i(0)&L_i(0)&b_{i+2}+a_i\\ \hline
0&1+d/12&1+7d/12&1+d/3\\
1&1+d/6&1+d/6&1+7d/6\\
2&1+7d/12&1+d/12&1+d/3\\
3&1-5d/6&1-5d/6&1-11d/6
\end{array}
\]
For \(0<d<6/7\), all these \(R_i(0)\) and \(L_i(0)\) are between \(0\) and \(3/2\), and \(b_{i+2}+a_i<2\).

For \(|y|\ge3/2\), the opposite firm \(i+2\) is strictly cheaper in delivered cost:
\[
\underbrace{b_{i+2}+(2-|y|)^2}_{\text{opponent delivered cost}}
-\underbrace{(z-a_i+y^2)}_{\text{deviator delivered cost}}
=b_{i+2}+a_i-z+4-4|y|
\le b_{i+2}+a_i-2<0.
\]
Hence nobody outside \([-3/2,3/2]\) buys from \(i\).

For \(0\le z\le 2p_i^*\), define \(R_i(z)=R_i(0)-z/2\) and \(L_i(z)=L_i(0)-z/2\); note that
\[
R_i(z)+L_i(z)=2p_i^*-z.
\]
If both are nonnegative, the necessary left- and right-neighbor inequalities bound the buyer arc's length by \(R_i(z)+L_i(z)\). If \(R_i(z)<0<L_i(z)\), the only potentially buying consumers are on the left arc, where \(L_i(z)<L_i(0)-R_i(0)\le d/2<1\). The right-neighbor inequality also holds there (distances remain \(1-y\) in that local region), so the candidate buying arc is contained in \([-L_i(z),R_i(z)]\) and again has length at most \(R_i+L_i\). The case \(L_i(z)<0<R_i(z)\) is symmetric. Both cannot be negative when \(z\le2p_i^*\).

At \(z=2p_i^*\) the above bounding arc has zero length. Higher prices cannot increase individual demand. This proves the bound for all \(z\ge0\).

To verify **equality at the candidate price**, calculate the adjacent boundary distances
\[
\begin{array}{c|cc}
i&R_i(p_i^*)&L_i(p_i^*)\\\hline
0&1/2-d/12&1/2+5d/12\\
1&1/2+d/12&1/2+d/12\\
2&1/2+5d/12&1/2-d/12\\
3&1/2-5d/12&1/2-5d/12
\end{array}
\]
All lie strictly inside \((0,1)\). Thus the two adjacent rivals generate exactly the interval \([-L_i(p_i^*),R_i(p_i^*)]\). The nonadjacent rival does not undercut the candidate firm on this interval: the minimal delivered-cost advantage of the opposite firm over \(i\), evaluated at the farthest endpoint, equals \(2-5d/3\) for \(i=0,2\), and \(2+2d/3\) for \(i=1,3\); both are positive for \(0<d<6/7\). Hence \(q_i(p_i^*)=R_i(p_i^*)+L_i(p_i^*)=p_i^*\). QED.

### Proposition 1 (global price best response)

For any nonnegative unilateral price deviation,
\[
\pi_i(z)=zq_i(z)\le z(2p_i^*-z)_+\le(p_i^*)^2=\pi_i(p_i^*).
\]
The final inequality follows by completing the square:
\[
z(2p_i^*-z)=(p_i^*)^2-(z-p_i^*)^2
\]
when demand is positive; zero demand is worse than the strictly positive candidate profit. The optimum is uniquely \(z=p_i^*\) **against the fixed other firms' prices**.

Hence \(p^*\) is a pure-strategy Nash equilibrium on \(0<d<6/7\). This does **not** prove that no other price equilibria exist.

### Fully compatible configuration

When all four qualities equal \(3d\), the candidate prices \(p_i^*=1\) and market shares \(q_i^*=1\) form a global Bertrand equilibrium by the identical argument, with neighbor bounds \(R_i(z)=L_i(z)=1-z/2\). The opposite firm undercuts any deviator for \(|y|\ge3/2\), and the at-equilibrium candidate interval \([-1/2,1/2]\) is not constrained by the opposite firm.

## 2. Welfare and voting

At each country's consumer density \(n_i/4\), define \(N=\sum_i n_i\) and \(w_i=n_i/N\). Price identities yield
\[
\Delta CS_{\rm circle}=\frac{d(216-13d)}{36},\qquad
\Delta\pi_0^{\rm circle}=\Delta\pi_2^{\rm circle}=-\frac{d(d+6)}9.
\]
Thus governments 0 and 2 have gross national welfare gains
\[
\Delta W_i^{gross}=\frac{Nd}{144}\left[w_i(216-13d)-4(d+6)\right].
\]

The marginal size ratio for support is
\[
\tau(d)=\frac{4(d+6)}{216-13d}, \quad
\tau'(d)=\frac{1176}{(216-13d)^2}>0.
\]
Fixing \(w_0=w_2=w\), the sign-switching network intensity solves
\[
d^*(w)=\frac{216w-24}{13w+4}.
\]
For \(w=3/25\) this is \(48/139\), strictly between \(1/3\) and \(3/8\).
The density thresholds bracketing the original interval are
\[
\tau(1/3)=\frac{76}{635},\qquad
\tau(3/8)=\frac{68}{563}.
\]
Since \(76/635<3/25<68/563\), the vote reversal occurs in the closed interval used in the original assessment.

World welfare increase from full compatibility before implementation cost:
\[
\Delta W^{gross}_{world}=\frac{Nd(216-47d)}{144}>0
\quad\text{for }0<d<6/7.
\]
It rises in \(d\) throughout the same region.

**Important interpretation:** price Nash existence is now closed-form within this model. The formulas alone do not establish uniqueness of all market equilibria, ISO's full multi-stage governance, or novelty relative to earlier theory.

## 3. What this Gate does *not* prove

- No general theorem for arbitrary numbers of firms/countries, transport costs, or true installed-base user-count effects.
- Not a global unique Nash equilibrium statement across all price profiles.
- It does not establish that ISO approval changes implementation costs; that belongs to Gate 2.
- It does not establish a first-in-literature theorem; that belongs to Gate 3.

Reproduction: [gate test script](../code/test_gate123_closed_form.py), [baseline scripts](../code/p1_iso_verification.py).
