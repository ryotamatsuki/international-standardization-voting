# Three-round economics-first gap discovery, 2026-11-09

Exploration runs from documented 1985–2026 literature to industry observations to model-boundary checks. **12 distinct research ideas**, not 12 theorems. Assessment N0–N4 follows prior-art gate and editorial significance: reject algebraic novelty without new economic behavior.

| Round | Hypothesis (economic question, not assumed conclusion) | Prior-art collision | Empirical outcome | Gate |
|---|---|---|---|---|
| 1 | R1: Stronger network effects cause fewer governments to approve beneficial standards | Klimenko 2009; Cheng–Huang 2025; repo P1-KS result | Unobservable ISO project national votes | N1/N2 reject |
| 1 | R2: Different national market sizes / worldwide profit ownership changes committee acceptance | G&S 2001; Spulber 2019; repo K/q quota arithmetic | TC membership is observable, votes not; payoff weights hard | N2 reject as stand-alone |
| 1 | R3: Voluntary private adoption after formal approval leaves network fragmented | Barrett–Yang 2001; Zhao et al 2007 | Certification/actual implementation more feasible | N1 reject |
| 1 | R4: Post-policy private product redesign reverses national consent | Boom 2001; Ruiz 2004; GMS 2021; already JPET Theorem3 | Redesign variable hard to identify | N2 old baseline, no new N3 |
| 2 | R5: Broader technical/certification profile deters marginal implementation enough to LOWER pairwise functional interoperability | Adoption/friction theories, Zhao 2007, 2023 adoption review; direct identical theorem unverified | OCA OCPP 2.0.1 mandatory Core vs optional ISO 15118, smart charge, security; vendor/country/product/version/date fields | **Best mathematical diagnostic**, N2 at most |
| 2 | R6: Version migration/backward compatibility changes which firms actively implement standards | Farrell–Saloner installed bases; Belleflamme; OCPP 1.6/2.0.1/2.1 actual breaks | OCA version/certification years; distinct cross-generation test requires data | N2/U promising but two-period extension |
| 2 | R7: Formally certified product groups retain cross-vendor interoperability defects | Information, implementation heterogeneity, ISO 15118-23 2026 conformance/interop distinction, actual industry tests | VOLTS reports event but **not verified pairwise pass/fail microdata** | Descriptive known, exclude until strategic mechanism |
| 2 | R8: Underinvestment by complement makers changes success of formally open standards | Rosero–Bekkers–Raiteri 2026; Miller–Toh complement work; Zhao 2007 | EV charger+EV maker or smart-home complements; difficult matching | N1/N2 reject by itself |
| 3 | R9: Patent standard inclusion and national institution composition alter innovation direction | Spulber 2019; Bonani 2026; Bergeaud et al 2026; governance selection | patent-to-standard NLP and TC leadership data | N2, extra patent politics needed |
| 3 | R10: Market coverage switches consumer-optimal compatibility network | Bertoletti 2026; Bianchi et al 2026; Huang et al 2026 | Coverage adoption vs local market size | N1/N2, already core of new 2026 work |
| 3 | R11: Firms deploy third-party and proprietary standards simultaneously; formal technical scope may change multi-homing | 2026 Research Policy 97 smart-home platforms, classic standards coalition models | version/third-party interface adoption by firm; some raw firm data may be restricted | **Open research question**, theorem U |
| 3 | R12: Time-to-standard revision and installed-base upgrade investment cause commitment/innovation distortions | Farrell–Simcoe 2012; Simcoe 2012; Belleflamme 2002; Farrell–Saloner 1986 | ISO project stage and revision metadata; product versions | **Open research question**, theorem U |

## Independent narrow theoretical check selected from R5
A continuum of heterogeneous optional-profile implementers choose whether to support an advanced technical profile of breadth s. Benefit s(b+theta*a), implementation cost c*s^2, c~Uniform[0,1], where a is others' adoption fraction. Effective *pairwise optional-module compatibility* is I=s*a^2, not mere standard publication. Exact equilibrium:
- a=1 if 0<s<=b+theta;
- a=b/(s-theta) if b+theta<s<=1 (assume 0<b, theta>=0, b+theta<1).
Effective I rises to b+theta, then **falls** after that threshold; summed welfare with a separate consumer-value factor V>=0 has same peak. Full detail, assumptions and non-originality gate: proofs/new_main_theorem.md and code/verify_optional_profile_scope.py.
**Caution:** This is a voluntary-adoption reduced-form game with no solved Cournot/Salop price competition, no national ISO decision and no rigorous N3 noncontainment. It is *not* a complete new international-standardization paper.

## Null mechanisms and why R5 is NOT yet the headline
- Freeze a=1: I=s is increasing; endogenously costly implementation is necessary.
- Set theta=0: peak remains at s=b for positive b. **Network effects are NOT necessary**, so calling it a new network-externalities theorem is incorrect.
- Delete national voting: result unchanged. **ISO government/committee interaction is NOT necessary**, so calling it a G&S+ISO theorem is incorrect.
- Change heterogeneous cost density: qualitative decline condition depends on upper-tail cutoff elasticity; not universal without conditions.
- Actual adoption certification profile is NOT the same as a continuous technical scope s, and vendor engineering costs may differ greatly from certification prices.

## Follow-up scientific choice
Do not automatically add a committee game to rescue N3; it would be precisely the failed combination-of-known-mechanisms pattern. If two prior-art screens are completed, develop R11 or R12 only if a jointly necessary committee/design/implementation interaction implies a genuinely new empirical prediction. Otherwise STOP theorem proliferation and refine the original JPET paper as a separate research project.
