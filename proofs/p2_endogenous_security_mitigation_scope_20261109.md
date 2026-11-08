# P2 Gate: endogenous legacy-network security loss from voluntary interoperability
Date: 2026-11-09 JST. Research branch: research/p1-proof-novelty-gate-20261108.
STATUS: exact conditional constructive model, not an unconditional unique SPNE and **not a novelty proof**. The four-firm product market retains the **weighted-brand** P2 formulation rather than the KS fulfilled-expectations current-user model.

## 1. Why the original c0*x² had insufficient foundations
The prior minimal P2 unanimity-vs-3/4 scope model charged country 0 a quadratic adjustment cost even though adoption was voluntary. A voluntary new option cannot simply impose a mandatory country fee; a credible mechanism must specify an unavoidable **third-party harm** from other firms' voluntary implementation, and explain how affected residents could or could not escape it.

We examine an external network-security incident. Four Salop firms occupy a length-4 circle, three legacy products 0,1,2 remain L-compatible, and firm 3 may implement a gateway with partial connection intensity x in [0,1] if the standard is published. Approval does not compel any firm to adopt. Country 1 proposes x in anticipation of a q-of-4 vote, firm adoption, price competition, and network exposure. Publication is *assumed* to reduce entrant technical adaptation costs / enable the published interface; the institutional mechanism for publication is not yet endogenized.

## 2. Optimizing hacker: the quadratic harm is an equilibrium result
A hacker targets the voluntarily connected gateway. The actor chooses attack effort e in [0,1], receives reward v for a successful attack, and faces effort cost (mu/2)*e². Breach probability P(x,e)=x*e, and payoff
\[
U_A(e;x)=vxe-\frac{\mu}{2}e^2.
\]
For v/mu<=1,
\[
e^*(x)=vx/\mu,\qquad P^*(x)=(v/\mu)x^2.
\]
The attacked firm 3 bears real expected damage D3*P; connected legacy endpoints in country 0 can simultaneously suffer a separate real loss D0*P even when country 0 casts No. Legacy devices preexist, and **the same country0 additive expected loss applies regardless of which Salop-brand product its current consumers choose**. Thus relative product demand and price best responses remain unchanged. The legacy risk is not a compulsory ISO-compliance fee; it is a cross-network externality from firm3's voluntary join. The model maintains that this third-party loss is not privately internalized by the original four operating-product firms.

The owner of legacy endpoints may alternatively isolate/re-engineer its network for a real fixed resource cost F0 to avoid the legacy loss, without eliminating the attack on firm3. Rational expected national cost is min{D0(v/mu)x²,F0}. The original unmitigated c0*x² term, c0=D0*v/mu, is therefore endogenous behavior on [0,1] if F0>=c0. If safe isolation is freely available, F0=0 and the original voting distortion disappears.

**Social accounting:** the attacker is a harmful actor outside the four participating jurisdictions. The objective called W below is total welfare of the **four participating national economies**, NOT all of humanity including the attacker's utility. Robustness to counting its private equilibrium surplus as welfare is checked separately; criminal proceeds and breach-related transfers require careful normative treatment.

## 3. Exact four-firm continuation; voluntary adoption is now binding
Use d=1/3, w=(11/50,2/5,7/50,6/25), N=1, technical cost k*x² with k=1/100. From the preexisting four-firm Salop global price-Nash existence construction,
\[
p_{0,2}=1+\frac{d(1-x)}3,\qquad p_1=1+\frac{d(1-x)}6,\qquad p_3=1-\frac{5d(1-x)}6.
\]
The existing global-price-deviation lemma is supported by 896 exact geometric sufficient conditions (16 adoption states x 4 firms x 14) for all x in [0,1]. The current cyber loss is country-uniform for legacy users and a fixed technology-contingent liability for firm3, *not a per-unit price cost*, so these price Nash best-response inequalities are unchanged.

Entrant3's gross operating-profit gain from joining the old three firms at a published x is
\[
G_3(x)=5x(5x+26)/1296.
\]
With v=1,mu=10,D3=2, the optimizing hacker supplies e*=x/10 and incident probability x²/10 (at most 0.1). Firm3 bears x²/5 and technical adaptation x²/100. Its exact **private net adoption gain** is
\[
\boxed{\Delta\Pi_3^{adopt}(x)=x(3250-6179x)/32400}.
\]
Therefore the maximum implementable scope is \(x^A=3250/6179\approx0.52597508\): strict adoption below it, strict refusal above it. At x=xA entrant3 is indifferent, so the exact upper-bound outcome requires an explicitly assumed **adopt-at-indifference tie rule**, or can be approximated by xA-epsilon. Unrefined multiple equilibria remain. For incumbents 0,1,2 the private L incentive remains unchanged; the original finite adoption game has 21 strictly profitable unilateral joins for x>0 and 3 identically indifferent cases across all 16 state configurations. At x=0, some of those 21 gains vanish; all reversal results here use x>0.

## 4. Exact nation-voting and welfare solutions
Define c0=D0/10, c3=D3/10=1/5. If legacy mitigation is too costly to undertake, F0>=c0, all national changes relative to the rejected old state O, *conditional on voluntary gateway implementation*, are
\[
\begin{aligned}
\Delta W_0(x)&=\frac{x[2842+(343-64800c_0)x]}{64800},\\
\Delta W_1(x)&=\frac{31x(x+34)}{6480}>0,\\
\Delta W_2(x)&=\frac{x(97x+118)}{21600}>0,\\
\Delta W_3(x)&=\frac{x(6982-6101x)}{32400}>0.
\end{aligned}
\]
The four-country total incremental welfare is
\[
W(x)=\frac{13850x-\{32400(c_0+1/5)-851\}x^2}{32400}.
\]
Country 1 (the nationally self-interested proposer) strictly prefers higher **actually implemented** x. Country0 votes Yes iff x <= xU where
\[
x^U=\frac{2842}{64800c_0-343}.
\]
A strict hypothetical unanimity (q=4) proposer selects xU; the simplified q=3 majority proposer selects the largest *privately implementable* xQ=xA, ignoring country0's No. The socially efficient **implementable** choice is
\[
x^W=\frac{6925}{32400c_0+5629}.
\]
For **all c0 in [0.3,0.7]**, strict exact rational inequalities prove
\[
\boxed{0<x^U<x^W<x^Q=x^A<1}.
\]
The exact gaps are:
\[
x^W-x^U=\frac{356659200c_0-18372893}
{(32400c_0+5629)(64800c_0-343)}>0,
\]
\[
x^Q-x^W=\frac{25(4212000c_0-979813)}
{6179(32400c_0+5629)}>0.
\]
At D0=3 (c0=.3): xU=.14881919, xW=.45116946, xQ=.52597508; W(xU)=+.05312374, W(xW)=+.09643051, W(xQ)=+.09377955.
At D0=7 (c0=.7): xU=.06313171, xW=.24462185, xQ=.52597508; W(xU)=+.02350449, W(xW)=+.05228415, W(xQ)=-.01688037.

Within this calibration:
- The majority rule's four-country welfare exceeds unanimity **iff c0<about .52698384244** in the interval [.3,.7], and is lower when c0 exceeds this level. This is the relevant root of polynomial 3411720000000*c0²-1913606078400*c0+60964001161=0, NOT a universal law.
- The majority-adopted proposal even **reduces** four-country welfare relative to rejection iff c0>74761/117000≈.63898291.
- Strict implementability (avoid the knife-edge xA): with allowed proposals {0, .05, .10, .45, .50}, the majority proposer chooses x=.50<xA, the entrant strictly joins; unanimity proposer chooses .10 at D0=3 and .05 at D0=7. The social planner's best choice *within that proposal menu* is .45 at D0=3 and .10 at D0=7. The finite menu is a robustness comparison, not an endogenous range of possible technologies.

## 5. Robustness to cost avoidance and accounting

- If old-country endpoints can securely opt out at zero cost (F0=0), country0 has positive payoff for any actually implemented scope and **strict unanimity can also select xA**. Therefore the old voting conflict cannot be asserted merely because a new optional standard is published.
- At xA, country0's gross national gain before cyber loss is exactly 11239865/458160492 ≈ .02453259. A perfect fixed-cost retrofit F0=.01 is privately preferred to incident damage; country0 strictly supports xA, and the unanimity/majority scope gap vanishes. Large legacy retrofit cost, not mandatory adoption, is the necessary economic restriction.
- If one *additionally counts* the optimally attacking outsider's private surplus x²/20 as part of aggregate welfare, the welfare-maximizing x is approximately .504407 at c0=.3 and .259470 at c0=.7, still less than xA. At c0=.7, majority welfare remains negative (~-.003048). This is **not** an ethical endorsement of criminal earnings as a social benefit; the point is accounting robustness.
- If D0=0 and firm3 pays the only externality/technical cost, the previous P2 "no overcompatibility under voluntary adoption" lemma still blocks an interior socially inefficient overshoot; the external burden on legacy third parties is necessary for this construction.
- If an attacker does NOT respond optimally to interoperability strength, incident probability may be linear rather than quadratic, and the particular quadratic welfare ordering does not follow automatically.
- The new cost remains independent of *current sales quantities and price*, and underlying national ownership/homogeneous Salop demand assumptions remain. This is a tractability restriction. The entrant's vulnerability is a second incidence of the **same cyber event**, not a second unrelated mechanism.

## 6. Prior art and editorial assessment: critical novelty limitation

**Most important newly discovered published study:** Comino, Stefano; Fedele, Alessandro; Manenti, Fabio M. (12 Aug 2026), "Cyber(in)security and Interoperability in Digital Services," The Journal of Industrial Economics, DOI https://doi.org/10.1111/joie.70041. **Open-access full text examined.** It models a hacker optimizing reward proportional to connected user mass minus quadratic attack effort, interoperability g, horizontal price competition, platform security investment, induced cybersecurity externalities and private-versus-social adoption incentives. Its exact game is different (duopoly platforms, no national ISO ballot) but **the cyber-interoperability microfoundation itself is established prior art**, including endogenous attack incentives and spillovers.

Other relevant prior art: Kunreuther & Heal (2003), "Interdependent Security," Journal of Risk and Uncertainty 26:231–249, https://ideas.repec.org/a/kap/jrisku/v26y2003i2-3p231-49.html; Farrell & Simcoe (2012), RAND Journal of Economics, DOI https://doi.org/10.1111/j.1756-2171.2012.00164.x; Spulber (2019), Economic Journal, DOI https://doi.org/10.1111/ecoj.12606; Goerke & Holler (1995), Public Choice, https://ideas.repec.org/a/kap/pubcho/v83y1995i3-4p337-51.html. UK NCSC 2026 secure OT connectivity guidance https://www.ncsc.gov.uk/collection/operational-technology/secure-connectivity/principle-3 documents expanded attack surfaces from additional interfaces and emphasizes secure isolation options. It does not prove the attack probability formula.

**Verdict:** The formerly arbitrary c0*x² cost now has a coherent source: attacker's optimizing behavior, externally borne unmitigated legacy losses, and a credible high-cost avoidance condition. The same event also *endogenously limits a firm's voluntary adoption*, affecting what gets implemented under 3-of-4 voting. The theorem's numerical/interval algebra is solid under stated primitives, but the general cyber-security mechanism is very close to Comino et al. (2026), so this is **not yet independent N3/N4 journal novelty**. The new paper would need a genuinely nontrivial interaction between SSO proposal rules, nationally allocated security liability and binding voluntary implementation (not just adding a 3-of-4 vote after calculating security costs), validated against the complete closest voting/market literatures.

## 7. Reproducibility and proof constraints
- Verified standalone exact SymPy code in conversation: verify_p2_security_externality_20261109.py. It re-solves prices from the Salop operator and checks 896 strict geometric sufficient conditions for all 16 standards configurations, 21 incumbent joining advantages and 3 equalities, hacker optimum, private participation ceiling, voting thresholds, social optimum and retrofit counterfactuals.
- Keep distinction between **global Nash existence for the selected price profile** and uniqueness among all possible noninterior price equilibria. All-equilibrium SPNE uniqueness has NOT been shown.
- Restrict the ISO interpretation to four valid Yes/No ballots and distinguish hypothetical q=4 unanimity from actual ISO "consensus"; ISO standards' adoption remains voluntary.
