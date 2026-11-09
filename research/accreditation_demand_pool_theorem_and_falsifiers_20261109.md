# Cost-recovery accreditation demand pooling: formal falsification screen (2026-11-09)
**EDITORIAL: WITHIN-MODEL THEOREM PROVED; N3 NOVELTY NOT ESTABLISHED (N1–N2 at best). DO NOT ADVERTISE AS DISCOVERED ORIGINAL PROPOSITION.**

## Distinct source-grounded institutions, not conflations
2026-11-05 OECD Trade Policy Paper 307 separates technical document harmonization, public-law MRA obligations, transnational accreditation and the commercial role of CABs. A transnational accreditation network does NOT automatically oblige national border regulators to accept certificates. OECD additionally recognizes some procedures as alternatives, rather than exclusive barriers, and says indirect network/bridge effects warrant further investigation.
Primary OECD: https://www.oecd.org/en/publications/the-evolving-role-of-mutual-recognition-instruments-in-a-trade-facilitation-context_56f2cfc7-en/full-report/component-7.html ; https://www.oecd.org/en/publications/the-evolving-role-of-mutual-recognition-instruments-in-a-trade-facilitation-context_56f2cfc7-en/full-report/component-10.html .
New Zealand MBIE's evaluation says many goods-sector MRAs had *limited use*, with manufacturers instead self-declaring or using other accredited labs; pharmaceuticals-GMP arrangement did see large use. This is a direct institutional reality check against claiming a single captive CAB for every standard: https://www.mbie.govt.nz/business-and-employment/business/trade-and-tariffs/trade-agreements-and-partnerships/conformity-assessment-mutual-recognition-arrangements .
The illustrative model below takes ONE product with a particular mandatory CAB pathway and is not generally true of all certification or export products.

## Minimal game and timing (no political vote or Cournot claim)
Destination A has a specialized domestic CAB with fixed real operating cost F>0 and zero variable cost; the accredited CAB serves foreign producers from countries B and C. There are masses b>0 and c>0 of prospective firms. Each has a privately observed operating gross export payoff u independently distributed Uniform[0,1]. The firm exports iff u>=p, where p is the authorized destination-A CAB's per-certificate price. These private payoffs are treated as reduced-form operating margins, not solved downstream Cournot/Bertrand competition.
The CAB is a *nonprofit cost-recovery provider*, choosing the **lowest nonnegative fee that covers its fixed cost** from actual customers. Thus for mass M of firms who must use it, revenue equilibrium is
M p(1-p)=F,  M>4F,
p(M)=(1-sqrt(1-4F/M))/2 in (0,1/2), quantity of exporting firms using the CAB is
E(M)=M(1-p(M))=[M+sqrt(M(M-4F))]/2.
The smaller root is an institutional selection rule of the cost-recovery provider, NOT a free-entry private-certifier competitive equilibrium. Its possibility is not claimed in all jurisdictions.

Initially both B and C must use A's specialized CAB and so M0=b+c. New B-A mutual recognition allows B exporters to use a *pre-existing*, zero marginal-fee recognized home testing route. All b prospective B exporters enter; C has no alternative recognized route and continues to use A's CAB; remaining CAB market mass is M1=c. The A-C legal arrangement is unchanged and the A CAB continues to operate: assume c>4F. No government switches its own approval standards or restricts C.

## Exact conditional negative-total-entry result
**Lemma (conditional cost-recovery diversion):** For every b>0, c>4F>0,
E(b+c)>b+E(c).
Thus introducing cheaper recognition for B alone decreases the total mass of exporting firms to A. The increase in B's entry is outweighed by the rise of the shared fee p(c)>p(c+b) which eliminates some C entrants.

**Proof**: E'(M)=1/2+(M-2F)/[2sqrt(M(M-4F))]. For M>4F,
(M-2F)^2-M(M-4F)=4F^2>0,
so E'(M)>1. Integrating from c to c+b yields E(c+b)-E(c)>b. QED.
Open parameter set b>0,c>4F>0, no numerical corner case or discontinuous exit necessary. Relative to the separable-market baseline, the sign reversal is induced by **endogenous shared certification costs** and the endogenous price p(M).

**Worked, fully checked numerical example**: b=1,c=2,F=.45:
CAB price p0=0.18377223398316206, p1=0.34188611699158106;
all exporters initially E(3)=2.4486832980505135;
after B-A recognition b+E(2)=2.316227766016838;
change = -0.13245553203367555.
These are CONTINUUM MASSES, not observed exporters or observed country trade flows. Do not claim any welfare sign: gross revenue and consumer surplus are not modelled, and B's foreign zero-price certification has its own public or sunk cost.

## Strong and very damaging alternative-model counterexamples
### General firm-profit distribution breaks the universal sign
If survival distribution is q(p)=1-p^alpha, alpha>0, CAB price is the smaller root of M*p*q(p)=F. At b=.1, c=1, F=c*.1*(1-.1^alpha), the numerical signs:
alpha=.4: entry rises +.0180
alpha=.5: entry rises +.010974
alpha=.75: entry rises +.00193
alpha=1: entry falls -.00111
alpha=2: entry falls -.00094
alpha=3: entry falls -.00017
All satisfy a viable lower-price branch, and are computed independently by scipy root finding. **Thus the sign is not distribution-free.**
For a general survival demand q, the infinitesimal harm condition for removal of B with zero-cost outside testing is
q(p)^2 / [q(p)+p*q'(p)] > q(0),
where p is the initial equilibrium fee in the limit b→0; this follows from differentiating CAB breakeven M p q(p)=F. The inequality needs verification of denominator positive, the **lower-revenue-root branch**. Some distributions satisfy it, others do not.

### CAB organizational form breaks the sign
If the CAB is instead a **profit-maximizing monopolist**, zero variable cost, symmetric Uniform[0,1] willingness and fixed F below its *post-MRA* operating profit c/4, the unconstrained optimal testing fee is p=1/2 before and after (market size scales profit but not the argmax). B's shift to free home tests raises TOTAL exporter entry by b/2; C is unaffected. Example b=1,c=2,F=.45 with c/4=.5>F, entry rises from 1.5 to 2.0. This single natural alternative REVERSES the result.
If F lies between c/4 and (b+c)/4, the monopoly CAB may *exit* after the MRA, causing C exclusion. This is an ordinary fixed-cost exit threshold, not an independently novel mechanism. Beware plausible alternate approved CAB pathways.
If there is no common CAB fixed operating cost F, the harmful effect disappears. International recognition itself is not enough.

## Exact closest-original-text collisions and quality gate
**Baller (2007), World Bank Policy Research Working Paper 4124**, original full PDF inspected: https://documents1.worldbank.org/curated/en/620221468337797645/pdf/WP04124.pdf . Theoretical Section III models MRA of testing procedures as a cut in exporter fixed cost F_X; also empirically examines standards effects on excluded countries. It DOES NOT characterize this shared CAB fee revenue model in the sections read. Thus our example is not simply Baller's independent-export-cost formula, but her literature/estimation has already studied MRA and third-country trade. It is a *working paper*, not a journal theorem.
**Choi & Mukherjee (2020), RAND Journal of Economics 51:989–1013**, author full PDF inspected https://jaypilchoi.com/wp-content/uploads/2021/06/Rand-2020.pdf . **Proposition 1, original print p.996**: profit-maximizing certifier's fee distorts firm entry iff entry costs are sufficiently large; see also Props 2–6 on disclosure, quality investment and welfare. A certification fee changing exporter entry is old. This paper's certifier maximizes profit and quality information, unlike nonprofit cost recovery and cross-country accreditation pool in our formula; result is not nested on currently read grounds, but nonequivalence is **insufficient for N3**.
**Decker (2016), Journal of Regulatory Economics 49:344–370, full article read**, https://link.springer.com/article/10.1007/s11149-016-9300-z . Section 4.1 describes **death spiral** when incumbent network fixed costs are recovered from a shrinking client base, raising captive users' prices and worsening the demand shrinkage. Its references point to Hotelling (1938) in railroad context. Thus our effect is largely known network utility cost-recovery externality applied to CABs, and is plausibly **relabeling rather than novel economics**.
**OECD (2026-11-05) official policy report**, primary https://doi.org/10.1787/56f2cfc7-en, motivates possible cross-border effects but explicitly does not claim the lab-demand-pool formal result.
**New Zealand MBIE**, real-world evaluation noted above: weak compulsory CAB assumption for many goods MRAs.

**N3 Gate**:
- Algebra: PASS in model.
- Nonempty open parameter region: PASS.
- Python/SymPy reproducibility and numerical stress: PASS.
- Microfounded regulator objective and market price: FAIL (not solved product-market competition).
- Robustness to profit-maximizing CAB: FAIL.
- Robustness to heterogeneity distribution: FAIL.
- Closest economic mechanism novel relative to Decker/Hotelling: FAIL; cost-recovery death spiral established.
- Robust, independently causal international standard-setting/vote institution: FAIL.
- Empirical test of real CAB legal-access scarcity, fees and third-country exporter exits: NOT DOCUMENTED.
**Final N3=NO.** Do NOT call this an original theorem. It is a **conditional illustrative proposition** and a useful explicit falsification of overly broad claims.

## Second distinct frontier: protocol ossification rejected without fabricating an economic result
**IETF/IAB RFC 9413 (June 2023), Informational** https://datatracker.ietf.org/doc/html/rfc9413 is NOT an official normative internet standard, but it describes technically observed protocol decay from permissive handling of nonconformant implementations and feedback from entrenched buggy implementations. Particularly §§4.1–4.2 contain the *exact claimed dynamic* of excessive leniency causing harder future interoperability, and §5 advocates active maintenance.
2026-09-29 IETF Internet-Draft catalogues ossification in TCP, TLS1.3, QUIC: https://datatracker.ietf.org/doc/html/draft-yuki-ossification-cases-00 . Internet-Draft is not an approved final RFC, nor a theoretical proof.
Economic overlaps: **Kristiansen (1998), RAND Journal of Economics**, R&D timing and compatibility with network externalities https://ideas.repec.org/a/rje/randje/v29y1998iautumnp531-547.html ; **Costinot, Gandal & Shy** and **Stadler et al. (2022)** endogenous compatibility, installed base and pricing https://doi.org/10.1007/s11067-022-09572-x; **Simcoe (2014) J Law & Economics** standards maintenance/testing organization https://www.journals.uchicago.edu/doi/full/10.1086/674022.
Simply re-describing protocol decay in economic vocabulary is **NOT N3**. Need independent, strict result for price/entry/R&D in a solved dynamic product market plus exact noncontainment of nearest three full theorems, not provided.

## Third frontier screen: standardization inside firms vs public ISO/SSO
Argente, Moreira, Oberfield & Venkateswaran (2025), NBER WP34160 https://www.nber.org/papers/w34160 shows **within-firm product similarity** affects multiproduct firm scope, quality, marginal increasing returns and response to demand shifts. This is a different kind of standardization from **cross-firm technical interoperability standards**; cannot borrow their results as though direct ISO evidence. Nonetheless “standardization facilitates scale, scope and product portfolio innovation” is not a newly observed economic phenomenon.

## Honest final assessment
This pass made one theorem-with-counterexamples and checked a second institutional frontier. **No N3-confirmed novel economic proposition.** The valuable advancement is a reproducible negative screen ruling out an intuitively attractive but structurally fragile MRA partner–outsider trade-reversal claim, and preventing protocol-ossification relabeling. Another direction is required; stop treating it as a publishable theory.

## New robustness result added after further analytic verification: Increasing hazard rate
The initial exact theorem for uniform exporter-profit distributions extends to a large economically natural class **IFR** (increasing failure/hazard rate). This is a condition-dependent, proved **extension of the diagnostic lemma**, NOT a newly certified N3 result.

Let each potential exporter have independently distributed gross operating surplus v≥0, with differentiable survival q(p)=Pr(v≥p), q(0)=1, 0<q(p)<1, q'(p)<0. Define the hazard rate λ(p)=−q'(p)/q(p) and cumulative hazard Λ(p)=−log q(p). Assume λ(p) is **nondecreasing**, p λ(p)<1, and the CAB picks the low-price/stable cost-recovery solution of M p q(p)=F. Post-MRA C retains this root and B can use the zero-price home CAB. Then
E(M)=M q(p(M)),
dE/dM = q(p)^2/[q(p)+p q'(p)]=q(p)/[1−p λ(p)].
Because nondecreasing hazard implies
pλ(p) ≥ ∫₀ᵖ λ(s)ds=−ln q(p)>1−q(p)
for p>0, we have dE/dM>1 wherever the admissible stable root exists.
Integrating from c to c+b shows E(c+b)>b+E(c), as in the uniform case. This provides an open range of distributions covering **uniform, exponential and Weibull with shape≥1** (with the correct fee branch), not just a knife-edge density.

This conclusion STILL FAILS if the hazard decreases rapidly. Example q(p)=1−sqrt(p), b=.2,c=2,p_C=.2,F=c*.2*q(.2), yields:
- before b+c exporters 1.2887192534196465
- after B recognition 1.305572808999546
- sign of change +0.016853555579899426, **opposite to the theorem**.
For comparison with same b,c,p_C=.2: exp survival gives change −0.00412122431922235; Weibull shape2 −0.00792088649131939; uniform −0.011336769750681874.
These checks were run in a separate Python session. This is a genuine **distribution-class robustness improvement**, but it does not cure the most damaging CAB-form ablation: a profit-maximizing monopolist picks constant p=0.5 for these uniform types and may yield increased aggregate entry after liberalization. It also does not prove national welfare effects, real-world use of shared non-profit CABs, or economic originality beyond Decker (2016) decline-network cost-recovery logic.

**Revised audit:** algebraic and standard IFR distribution robustness PASS, organization-form robustness FAIL; no independent price-competition downstream microfoundation or original network-standardization mechanism proven. **N3 NOT VERIFIED.**
