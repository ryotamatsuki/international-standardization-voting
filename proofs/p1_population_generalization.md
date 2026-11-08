# P1 generalization: arbitrary national population shares and median-pivot voting rule

**Date:** 2026-11-08. **Status:** closed-form theorem for the specified 4-country Salop–Bertrand continuation, conditional on ISO publication changing voluntary implementation cost. Does **not** establish novelty beyond prior standard-setting/game-theoretic work.

## Baseline

Countries \(i=0,1,2,3\) have arbitrary populations \(n_i>0\), total \(N=\sum_i n_i\), and national weights \(w_i=n_i/N\), with
\[
w_i>0,\qquad \sum_{i=0}^{3}w_i=1.
\]

Three incumbents (0,1,2) have interoperable standard \(L\), and firm 3 is alone on \(M\). ISO-style approval requires 3 of 4 valid yes votes and, if passed, reduces firm 3's real implementation cost from \(k_H\) to \(k_L\), where
\[
0\le k_L<G_3(d)=\frac{Nd(60-25d)}{144}<k_H.
\]
The 16-profile voluntary adoption game and Bertrand price-game global-best-response proof are described in the companion Gate 1 and Gate 2 notes. The price equilibrium is guaranteed in the baseline for \(0<d<6/7\); all 16 candidate adoption-continuation price profiles have the closed-form sufficient conditions on \([1/5,4/5]\) (regression check in the companion Python test).

## Welfare and voting thresholds — no particular weight vector

Let \(\Delta CS_{\rm circle}=d(216-13d)/36\) be the increase in consumer surplus per unit-density national circle, and \(\Delta\pi_i^{\rm circle}=p_i^{1\,2}-p_i^{0\,2}\) the per-market operating-profit increment for firm \(i\).

Country \(i\)'s gross welfare difference is
\[
\Delta W_i^{gross}=
\frac N4\left[w_i\Delta CS_{\rm circle}+\Delta\pi_i^{\rm circle}\right].
\]
Specifically:
\[
\boxed{
\begin{aligned}
\Delta W_0^{gross} &= \frac{Nd}{144}\{w_0(216-13d)-4(d+6)\},\\
\Delta W_1^{gross} &= \frac{Nd}{144}\{w_1(216-13d)-(d+12)\},\\
\Delta W_2^{gross} &= \frac{Nd}{144}\{w_2(216-13d)-4(d+6)\},\\
\Delta W_3^{net} &= \frac{Nd}{144}\{w_3(216-13d)+60-25d\}-k_L.
\end{aligned}
}
\]

For \(0<d<6/7\), \(k_L<G_3(d)\) guarantees \(\Delta W_3^{net}>0\), so country 3 always votes yes.

The incumbent support tests are
\[
\boxed{
w_0,w_2\ge \tau_o(d)=\frac{4(d+6)}{216-13d},\qquad
w_1\ge \tau_c(d)=\frac{d+12}{216-13d}.
}
\]
The thresholds strictly increase with network intensity:
\[
\tau'_o(d)=\frac{1176}{(216-13d)^2}>0,\qquad
\tau'_c(d)=\frac{372}{(216-13d)^2}>0.
\]

Thus national support among the three incumbents is weakly decreasing in \(d\), because the decrease in global operating profit can dominate the domestic consumer gain.

## Theorem: median-pivotal ISO ballot threshold

Define individual critical network effects
\[
\boxed{
d_0^*=\frac{216w_0-24}{13w_0+4},\quad
d_1^*=\frac{216w_1-12}{13w_1+1},\quad
d_2^*=\frac{216w_2-24}{13w_2+4}.
}
\]
When national bodies use sincere voting, with indifferent voters voting yes, and firm 3 is a strict adopter following acceptance but strict non-adopter following rejection, for every valid \(d\) in the equilibrium/adoption-cost region,
\[
\boxed{
\text{ISO proposal accepted}
\quad\Longleftrightarrow\quad
d\le\operatorname{median}\{d_0^*,d_1^*,d_2^*\}.
}
\]

Proof: approval after firm 3's yes requires at least two of the three incumbents' yes votes. For any incumbent \(i\), its positive welfare condition is equivalent to \(d\le d_i^*\) (provided \(d>0\) and \(216-13d>0\)). At least two inequalities hold exactly when \(d\) is not greater than the **median** of three critical values. This is a complete closed-form characterization of the voting outcome, not a theorem of uniqueness of all strategic-ballot Nash equilibria.

**Economic interpretation**: the pivotal threshold belongs to the *median incumbent standard owner*, not the median consumer; each country has one vote regardless of population, and firm profit accrues from the world market.

### Reversal existence over an open subset of the simplex

For any \(0<d_L<d_H<6/7\), suppose
\[
\boxed{
\tau_o(d_L)<w_0,w_2<\tau_o(d_H),\quad
w_1>\tau_c(d_H),\quad
w_3=1-w_0-w_1-w_2>0.
}
\]
Assume further that \(k_L<G_3(d)<k_H\) at all \(d\in[d_L,d_H]\), and the specified continuation equilibria and market price equilibria exist on this interval.

Then at \(d_L\) all four countries strictly favor the compatible standard (4 yes), while at \(d_H\) countries 0 and 2 strictly oppose and countries 1 and 3 strictly support (2 yes). Approval flips to rejection in between. This is an **open parameter region**, rather than a knife-edge symmetric population pair. The two pivotal countries need not be identical.

World welfare gain, **conditional on compatible implementation**:
\[
\Delta W_{\rm World}=\frac{Nd(216-47d)}{144}-k_L>0,
\]
because
\[
\left[\frac{Nd(216-47d)}{144}\right]-G_3(d)
=\frac{Nd(156-22d)}{144}>0
\]
on \(0<d<6/7\) and \(k_L<G_3(d)\). Therefore a welfare-improving standard can lose formal approval when \(d\) rises.

## Asymmetric population-share example (not the theorem's assumption)

Take
\[
(w_0,w_1,w_2,w_3)=(3/25,21/50,13/100,33/100)
=(.12,.42,.13,.33),
\quad N=1,\quad k_L=1/20,\quad k_H=3/10.
\]
All positive, with \(w_0\ne w_2\).

Then
\[
d_0^*=\frac{48}{139},\quad
d_1^*=\frac{3936}{323},\quad
d_2^*=\frac{408}{569}.
\]
The median is \(d^{ISO}=408/569\), whereas \(48/139\) is now only the *first* incumbent defection threshold.

The exact voting profiles and hypothetical post-implementation welfare gains are:

| \(d\) | votes in order 0,1,2,3 | ISO vote | \(\Delta W_{\rm World}\) if approved |
|---|---|---|---|
| \(1/5\) | Y,Y,Y,Y | approved (4:0) | \(853/3600>0\) |
| \(2/5\) | N,Y,Y,Y | approved (3:1) | \(112/225>0\) |
| \(4/5\) | N,Y,N,Y | rejected (2:2) | \(847/900>0\) |

The interim realization of a higher network effect changes support first from 4 to 3, without losing ISO approval, and later from 3 to 2, causing rejection.

The adoption condition holds throughout \([1/5,4/5]\) since
\[
\frac1{20}<G_3(1/5)=\frac{11}{144}
<G_3(4/5)=\frac29<\frac3{10},
\]
and \(G_3(d)\) strictly increases on this domain.

We checked all 16 possible adoption profiles \(\times\) four firms \(\times\) 12 sufficient-condition margins at both endpoints of \([1/5,4/5]\) using exact rational SymPy arithmetic. The **smallest margin is \(1/30>0\)**. Each margin is affine or a concave combination of affine terms, so positivity at the two endpoints ensures positivity throughout.

## How restricted is the reversal region?

For the incumbents at opposite positions 0 and 2:
\[
\tau_o(0^+)=1/9,\qquad
\tau_o((6/7)^-)=32/239\approx0.1339.
\]
For incumbent 1:
\[
\tau_c(0^+)=1/18,\qquad
\tau_c((6/7)^-)=15/239\approx0.0628.
\]
Thus a positive-to-negative switch within the price-proof domain requires \(w_i\) in these bands. This is **not** a generic reversal for all countries or for symmetric market populations; with \(w_i=1/4\) for all countries, none of the incumbents switches within the current proven \(d\)-domain.

It is an economically interpretable restriction: at least two nationally pivotal incumbent standard holders must be small relative to the size of the export market from which their own firms earn profit. **Open-set existence is weaker than broad quantitative importance.**

## Research and publication significance

- **Math gain:** all four \(w_i\) are arbitrary; the vote rule has a complete median-critical-threshold characterization and the nonmonotonic acceptance outcome occurs on a nonempty open set. No requirement \(w_0=w_2\).
- **Limits:** four countries and one firm per country, fully covered circular demand, compatible-brand-count rather than installed-base scale effects, exogenous cost response to ISO issuance, and a selected continuation equilibrium.
- **Novelty limits:** a median-pivotal vote threshold is a familiar order-statistic result; the contribution cannot be attributed to the median formula alone. The substantive candidate is the exact origin of the individual critical values in world-profit versus national-consumer competition.
- **Next gate:** preserve proof under \(n\)-country voting and alternative demand systems, or derive the institution-to-implementation-cost channel endogenously; then compare Barrett–Yang, Klimenko, and Spulber at theorem level. Current IJIO/RIO editorial fit remains unproven.

Reproducible checks: [test population generalization](../code/test_p1_population_generalization.py).
