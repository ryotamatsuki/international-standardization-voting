# P2 one-friction gate — decision after endogenous cyber-spillover microfoundation
Date: 2026-11-09 JST. Branch: research/p1-proof-novelty-gate-20261108.

## The task
Test whether the earlier exogenously imposed c0*x² cost can emerge from plausible economics while respecting voluntary international standard adoption, Gandal–Shy-style Salop pricing, national 3-of-4 and hypothetical unanimity, and whether the scope ordering is preserved.

## Verified findings
- Mechanism: a hacker maximizes v*x*e-(mu/2)*e², success probability x*e. This yields e*=v*x/mu and equilibrium damage proportional to x². Target is the voluntary entrant gateway; a preexisting country's installed legacy endpoints suffer unintended cross-platform spillover independently of current consumers' brand purchase choice. Attack liability also affects the entrant's own decision.
- With v=1,mu=10 and damages D0=3 or 7; D3=2, xA=3250/6179 is the *maximum voluntarily implemented* interoperability. This is a binding adoption cap, unlike the previous P2 example, and therefore committee proposals cannot be evaluated as if a published standard were necessarily implemented.
- Fixed country population weights w=(.22,.4,.14,.24), d=1/3, adaptation cost .01*x² and costly old-network mitigation F0>=D0/10. Under hypothetical unanimity xU=2842/(64800c0-343), socially preferred xW=6925/(32400c0+5629), simplified three-vote proposer xQ=xA (adopt-on-indifference).
- Exact algebra proves xU<xW<xQ for every c0 in [.3,.7]. With D0=3, four-country welfare W(xU)=+.053124 vs W(xQ)=+.093780. With D0=7, W(xU)=+.023504 vs W(xQ)=-.016880. Majority overcompatibility and whether majority is welfare-superior are **not** the same claim.
- At xQ firm3 is indifferent, so a precise equilibrium requires a stated tie convention; a finite proposal menu {0,.05,.10,.45,.50} instead gives **strict** implementation at x=.50 and qualitative under/over ordering with no adoption tie.
- Free or inexpensive old-network segregation removes the original vote distortion: F0=0 means national0 never bears the harm; F0=.01 suffices to make national0 support xA. This avoids assuming compulsory ISO compliance, but makes clear that costly nonparticipation/mitigation is **essential**.
- Under the alternate convention of adding hacker net surplus x²/20 to four-country total, qualitative xU<xW<xQ persists at D0=3 and 7; qualified-majority welfare remains negative at D0=7. But criminal earnings raise normative counting issues.
- The original geometric sufficient-condition program checks 896 exact inequalities spanning all 16 Salop technology configurations and four firms on x in [0,1]. The new compact verified script reproduces market pricing and national welfare. There is no proof that these are *all* possible price Nash equilibria or that the complete continuous extensive game has a unique SPNE.

## Very close directly observed 2026 prior art
Comino, Fedele & Manenti (2026), *The Journal of Industrial Economics*, **Cyber(in)security and Interoperability in Digital Services**, https://doi.org/10.1111/joie.70041 (published 12 August 2026, open-access full text). They already model interoperability changing hackers' incentives, network-wide cyber security externalities, firms' security investment and pricing, and private/social divergence in compatibility. This **eliminates any reasonable claim that adding a hacker microfoundation alone is a novel theoretical contribution**. The distinct ISO-style national proposal/voting and voluntary adoption cutoff must do the work and be tested against Goerke-Holler (1995), Farrell-Simcoe (2012), Spulber (2019), and the new 2026 paper.

UK NCSC guidance (2026) says novel third-party connections may increase legacy network attack surface, but also calls for safeguards and segregation. The observed mechanism is plausible, **not** universally unavoidable: https://www.ncsc.gov.uk/collection/operational-technology/secure-connectivity/principle-3.

## Independent research verdict
**Microfoundation feasibility: conditional PASS.** The external loss is no longer merely a compulsory national standard-adoption fee. The same attack probability endogenously raises an entrant's adoption expense; mandatory standardization is not assumed.

**Simplicity target: MIXED.** Added an attacker, two incidence parameters and a costly protection/segregation assumption. The original clean four-country market remains but the standards economics is now entangled with a recently published cybersecurity-interoperability model.

**Novelty gate: FAIL TO ESTABLISH.** The exact institutional voting/adoption scope condition may be a new *specific construction*, but no published prior-art noncontainment is proven and strong close literature exists.

**Suggested stop rule:** Do **not** elaborate to general hackers, heterogeneous threats, security effort, multistage ISO bargaining or more competing platforms merely to make the model elaborate. First test whether a single proposition on **endogenous proposal scope under binding voluntary implementation and national negative externalities** differs *qualitatively* from an established SSO voting result. If not, retain this as a verified diagnostic/robustness appendix and focus publishing a simpler model rather than developing a second, derivative security economics paper.

**Evidence:** [full note](../proofs/p2_endogenous_security_mitigation_scope_20261109.md), [new verifier](../code/verify_p2_security_externality_20261109.py), [previous 896 pricing tests](../code/p2_unanimity_vs_majority_20261109.py).
