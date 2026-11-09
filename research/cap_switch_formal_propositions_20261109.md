# Technical harmonization with endogenous conformity-assessment regimes: two rigorous propositions
Date 2026-11-09 JST. **NOT A JOURNAL-READY NOVEL THEORY.** Purpose: characterize exact conditions that make a trade-reversing standards result logically possible versus impossible, following prior-art-first rejection of generic H5.

## Economic motivation and admissible interpretation
Technical standards document harmonization (h) reduces exporter redesign/setup costs. Separately, an importer may accept partner conformity test results, or may require additional domestic assessments. A country's choice among accredited/approved CAP systems can be discrete in administrative reality. This must not be conflated with unilateral ISO technical voting or arbitrary tariffs; WTO TBT constraints and assurance quality apply. The research tests only whether a separately-governed discrete CAP menu can change the **direction** of the extensive-margin response to harmonization. It does **not** model network externalities, SSO country voting, quality testing accuracy, or prices explicitly.

## Proposition 0: continuous additive CAP burden cannot overcompensate standard harmonization
Let h increase exogenously and reduce an exporter’s effective market-entry cost from g(h)+t, with g(h)=c0−h, t>=0. Importing authority chooses t in the unrestricted continuum [0,infinity) to maximize
V(h,t)=W(g(h)+t)−C(t)
where W is continuous and arbitrary, and C is strictly convex. Assume finite unique global maximizers t*(h) and no *direct* appearance of h in W or C. Then
c*(h2) <= c*(h1) for h2>h1.
Hence under any exporter entry decision weakly decreasing in c, realized exporter entry is weakly increasing in h. This does not say t*(h) itself falls. No concavity of W is required. No direct confidence or regulatory objective benefit of h; bounded CAP controls would violate the premises.

**Proof (revealed preference)**: Let d=h2−h1>0, b_i=c0−h_i; c_i=b_i+t_i. Assume c2>c1; then t2>t1+d. At h1 the authority can replace t1 by t2−d>=0 to replicate c2; at h2 it can replace t2 by t1+d>=0 to replicate c1. Optimality implies
C(t2)−C(t1+d) <= W(c2)−W(c1) <= C(t2−d)−C(t1).
But strict convexity and t2−d>t1 imply
C(t2)−C(t2−d) > C(t1+d)−C(t1),
which is algebraically equivalent to
C(t2)−C(t1+d) > C(t2−d)−C(t1).
Contradiction. Therefore c2<=c1. QED. This is a standard monotone comparative-statics argument, not a claimed new generic theorem.

## A minimal exporter-entry and national-policy environment
There is mass 1 of potential foreign exporters with independently drawn fixed market-entry costs z~Uniform[0,1]. Gross benefit net of the technical document-matching and duplicate assessment costs is A+h−t. Exports occur if z<=A+h−t. In the interior region 0<A+h−t<1, the realized measure of exporting firms is
n(h,t)=A+h−t.
Choose A>0, h>=0, t>=0. This is an exporter fixed-cost threshold, not a solved model of strategic price competition.

Importing country's reduced-form valuation over resulting competitive access:
U(n)=a*n−(b/2)*n², a>0, b>0.
The linear part can represent importing-consumer variety gains net of first-order costs; b term represents diminishing benefits and/or increasing local incumbent competitive loss. This is a **primitive assumption**, not a result from solved Cournot/Bertrand competition. The admissible n domain is [0,1].

The public authority chooses one of two procedural regimes:
- Accept foreign conformity-assessment results: t=0, administrative cost 0.
- Require a separate domestic verification regime: t=T>0, domestic regulatory resource cost K>0.
The effect T is the extra fixed cost for foreign exporters who already certified at home (not necessarily formally different rules applied to like domestic goods). This choice is politically/institutionally meaningful only if legitimate assurance difference or feasible regulator discretion is documented. Timing: h fixed -> authority chooses regime -> firms observe choice and decide entry. Strictly interior cases only.

## Proposition 1: discrete CAP switch creates an open region of declining trade after harmonization
Define
h* = a/b + T/2 + K/(b*T) − A.
Suppose h*>0 and for h in a neighborhood of h* both counts n(h,0), n(h,T) lie strictly between 0 and 1. If h<h*, importing country strictly selects **accept**; if h>h*, it strictly selects **domestic verify**. This equilibrium is unique off the threshold. At h=h*, both regimes are optimal.
Take h1=h*−eps and h2=h*+eps, 0<2eps<T, preserving the interior conditions. Then
h2>h1 but n(h2,t*(h2))−n(h1,t*(h1))=2eps−T<0.
This failure of monotonic entry holds throughout a nonempty OPEN set of parameters satisfying the strict interior and threshold inequalities.

**Proof**: Write x=A+h. The difference in regulator payoff between domestic retesting and acceptance equals
Delta(h)=[a(x−T)−b/2*(x−T)²−K]−[a*x−b/2*x²]
=b*T*(A+h−a/b−T/2)−K
=b*T*(h−h*).
Since bT>0, single crossing yields policy threshold. The entry discontinuity is immediate. QED.

**Economic interpretation**: As harmonization makes entry easier, national marginal valuation U'(n)=a−b*n declines; if entry is already high, a discrete, costly change of the conformity-assessment regime becomes nationally preferred. Unlike a continuously adjustable t, choosing the only available strict regime adds a lumpy fixed burden T, and can cause exporter exit in a narrow region around the policy threshold. This is a general *regime-discreteness* mechanism, not evidence that countries empirically retaliate via arbitrary testing or that the choice is WTO-compliant.

### Computed illustration (not calibrated to any sector)
a=0.30, b=1, A=0.35, T=0.20, K=0.005 => h*=0.075.
At h1=0.065, acceptance yields n1=0.415 and domestic verification would give n=0.215; regulator chooses acceptance (U_accept=0.0383875 > U_verify=0.0363875).
At h2=0.085, acceptance would yield n=0.435, verification yields n2=0.235; regulator chooses verification (U_verify=0.0378875 > U_accept=0.0358875).
Thus a 0.020 technical-cost reduction induces a 0.180 fall in exporter mass in this illustrative model. No empirical calibration; 0.415 is a share of a continuum, not 415 real firms.

## Corollary 1: continuous-test alternative restores monotone entry
Replace binary t in {0,T} with a full continuous t>=0, administrative resource cost (k/2)t², k>0, and the same U(n). In the region where the optimal t is interior,
t*(h)=[b(A+h)−a]/(b+k),
n*(h)=[a+k(A+h)]/(b+k),
dn*/dh=k/(b+k)>0.
When b(A+h)<=a, t*=0 and dn*/dh=1. Proof: unique strict concavity of the regulator's objective and first-order condition −a+b(A+h−t)−k t=0. This result is NOT a claim continuous CAPs are practically attainable or legally unconstrained.

## Boundary conditions and compulsory counterfactuals
- If the CAP mode is exogenous (fixed t=0 or t=T), n rises one-for-one with h: the paradox vanishes.
- If the regulator has fine-grained continuous policy discretion with convex adjustment costs, no cost over-offset occurs: the paradox vanishes.
- If there is no domestic preference for moderating foreign entry (b=0), Delta does not rise with h and no switch of the proposed type occurs.
- If h changes directly the regime's safety/evidence value, other outcomes are possible; current results cannot predict their sign.
- If foreign verification can be performed at home through legal MRA at the same assurance, T may drop to 0 and the two regimes collapse.
- If exporters can evade/restructure CAP costs or trade volumes have nonuniform dependence on entry costs, exact linear n need not survive; a qualitative jump remains possible whenever mode changes cause positive fixed-cost shock larger than h change, but that is not independent novelty.

## Relationship to 2024 NBER WP Proposition 5
Maggi & Mrázová's Proposition 5 says an *international agreement*, in its particular one-way-trade standards-regime model, never reduces the extensive margin. Our result changes a distinct experiment: h is an exogenous technical-harmonization shock and the importing body makes a later binary choice on conformity-assessment recognition. These **are not nested** without a common embedded game. Neither is a logical contradiction of the other. Journal-level claim requires embedding CAP choice in the original rigorous competitive setting and obtaining non-containment.

## Proof status and novelty
- Proposition 0: analytically established generally within its assumptions, **N1 generic comparative statics**.
- Proposition 1 and Corollary: symbolic derivation and independently evaluated examples, proof valid under listed conditions; **N2 at most; academic novelty UNVERIFIED**.
- A numerical open-parameter stress test supports algebra but cannot validate economic institutions or prior-art independence.
- Do not rename P1 as an ISO international-voting theorem. No nation votes, international treaty choice, direct network externality, endogenous design or pricing in this model.
- Strategic and legal authenticity, published full theorem collision, and downstream market-price/welfare validation are NOT complete.

**Editorial decision: RESEARCH (narrow conditional proposition only); NO-GO for immediate journal submission.**

## Proposition 2: the binary-switch sign is not dependent on quadratic U
Retain importer modes t∈{0,T}, exporter entry n=A+h−t, and a regime cost K>0. Replace quadratic U by **any C1 strictly concave** importer objective U(n) on a feasible open interval containing both n and n−T. Define
D(h)=U(A+h−T)−K−U(A+h).
Then
D'(h)=U'(A+h−T)−U'(A+h)>0.
If D(h_L)<0 and D(h_H)>0 for an interior h_L<h_H, there is a unique crossing h*∈(h_L,h_H), and the equilibrium regime switches from foreign test acceptance (below h*) to domestic duplicate verification (above h*). The exporter entry mass has a downward jump of exactly T at h*, despite the exogenous increase in h. A sufficiently small perturbation h2−h1<T around h* therefore decreases exporter entry. Proof follows from strict concavity, continuity and the intermediate value theorem; no quadratic special functional form is needed.

**Necessary economic content:** A crossing is impossible if U is increasing over the whole relevant interval, because strict duplicate verification reduces n and costs K. A national/SSO preference for limiting entrants at the relevant state must be **microfounded**, not postulated as automatic benevolent government behavior. Strict concavity alone does not guarantee a crossing; the inequalities D(h_L)<0<D(h_H) are substantive and must be empirically/structurally justified.

**Failure modes:** With multiple intermediate testing modes or endogenous foreign-recognition equivalences, jumps may shrink or disappear; with a smooth continuum the no-over-offset P0 applies. Nor does this generic single-crossing result establish novel economics: discrete choice and concavity are classical.
