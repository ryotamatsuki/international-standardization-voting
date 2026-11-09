# Research proposal: Reference-test architecture and realized cross-vendor interoperability
Date 2026-11-09 JST. Economics-first research hypotheses and a **proved conditional minimal-model comparative static**. Not a certified new N3/N4 theorem.

## Executive summary
**Main research proposition RT1** (Japanese):
「国際標準の認証試験が単一の基準実装への接続を中心に構成され、実装企業のエンジニアリング資源に制約がある場合、基準実装との接続価値の上昇は、認証可能性を高める一方で、独立した他社製品同士の相互運用性を低下させ得る。企業間の技術的補完性が強いほど、後者の低下が増幅されることがある。」

**Do not claim** the industry currently exhibits this distortion, that it is an ISO government vote, that all reference implementations work this way, or that the result is journal-novel. The test scheme must allow individually certified implementations that are not functionally interoperable with every other vendor. ISO 15118-21:2025 states conformance testing does NOT guarantee interworking; ETSI differentiates QE reference interoperability testing from pairwise vendor testing. These are factual motivation, not economic evidence of strategic investment crowd-out.

## Historical and technical evidence, verified sources
- ETSI, interoperability testing architecture: EUT × Qualified Equipment (QE), multi-QE protocols preferred if possible. https://portal.etsi.org/Services/Centre-for-Testing-Interoperability/ETSI-Approach/Interoperability-Testing
- ISO 15118-21:2025 preview: protocol conformance tests are a prerequisite for downstream interoperability; suite cannot guarantee interworking. https://www.iso.org/cms/%20render/live/en/sites/isoorg/contents/data/standard/08/41/84170.html ; preview https://cdn.standards.iteh.ai/samples/iso/iso-15118-21-2025/8f069b9a67814d32b62a0a104d7652fa/iso-15118-21-2025.pdf
- Open Geospatial Consortium 2022 Test Program §§7.1–7.2: certified reference implementations and class/extension variation. https://docs.ogc.org/pol/08-134r11.html
- NIST: conformance and peer-to-peer interoperability testing are different categories. https://www.nist.gov/itl/testing-environments
- ITU C&I: interop requires practical cross-vendor tests in addition to conformance. https://www.itu.int/en/ITU-T/C-I/pages/default.aspx
- OTT et al 2026 already discuss deliberate standards dilution, **different** mechanism. https://doi.org/10.1093/joclec/nhag023
- Simcoe 2014, *Governing the Anticommons: Institutional Design for Standard-Setting Organizations*, describes SSO test suite/certification/reference implementations. https://www.journals.uchicago.edu/doi/full/10.1086/674022
- DeMarzo, Kremer, Skrzypacz 2019, AER *Test Design and Minimum Standards*, strategic seller quality certification. https://doi.org/10.1257/aer.20171722 — **high novelty threat to test-incentive-distortion**.
- Doganoglu & Wright (2006 IJIO), incompatible networks with multihoming; Liu et al (2010/11 ISR), strategic cross-platform conversion; similarly near but no verified theorem-level noncontainment. https://doi.org/10.1016/j.ijindorg.2005.07.004 ; https://doi.org/10.1287/isre.1090.0255
- *The Perpetual Trouble with Network Products Why IT Firms Choose Partial Compatibility* (2022/23), explicitly characterizes endogenous partial compatibility in prices and market size. https://doi.org/10.1007/s11067-022-09572-x
- Berends, Deken, Hummel (2026), Research Policy, 97 smart-home platforms using combinations of third-party and proprietary interfaces. https://doi.org/10.1016/j.respol.2026.105609
- OECD 2026 data spaces policy explicitly discusses reference implementation, common semantic models, and government anchors; a distinct governance setting. https://www.oecd.org/en/publications/data-spaces-between-co-ordination-challenges-financial-viability-and-public-policy_0066f11b-en/full-report/multi-party-co-ordination-as-the-distinctive-value-proposition-and-challenge-of-data-spaces_906f89dd.html

## Conditional microscopic feasibility test: 2 firms with distinct engineering tasks
Stage only: each firm i chooses two continuous nonnegative efforts: r_i = quality of integration with common reference implementation, e_i = generalizable interoperability with independent competing vendors. The realized other-vendor match quality can be locally approximated by e_i e_j, **NOT** assumed directly from “ISO certified.” Benchmark scheme market size/private financial value H>0 rewards reference integration; v>0 rewards general cross-vendor capabilities; beta >=0 is reciprocal network-investment complementarity. Engineering resources have shared cost
C_i = (u/2)(r_i+e_i)^2 + (d/2)(r_i^2+e_i^2),
u>0, d>0. Cross term u*r_i*e_i **is microfounded by competing for a common engineering capacity** rather than arbitrary negative network benefits. Define A=u+d, c=u. Net payoff for each firm:
pi_i=H*r_i + v*e_i + beta*e_i*e_j - (A/2)(r_i^2+e_i^2) - c*r_i*e_i.
No price competition and no standards committee vote are claimed in this diagnostic model.

Assume beta>=0, A>c>0, D=A*(A-beta)-c^2>0 and interior positive r,e; in any parametric range satisfying these inequalities the symmetric Nash equilibrium is unique under joint-player contraction:
r*=[(A-beta)*H-c*v]/D;
e*=[A*v-c*H]/D.
Comparative statics:
∂r*/∂H=(A-beta)/D > 0;
∂e*/∂H=-c/D < 0;
∂ |∂e*/∂H| / ∂beta=A*c/D^2 >0.
If realized pairwise quality is Q=e*^2, ∂Q/∂H=2e*(−c/D)<0. This **is an analytically verified conditional proposition in the proposed game, not an independently proved new general law**. Main nontrivial causal driver is **test/reference-oriented investment substituting for generalizable cross-vendor investment**; complementarity beta amplifies, rather than eliminates, the negative sensitivity.

Concrete interior feasibility: A=2, c=0.8, beta=0.4, v=0.6 gives D=2.56. At H=0.5: r*=0.125, e*=0.3125, Q=0.09765625. At H=1.3: r*=0.625, e*=0.0625, Q=0.00390625. Values are effort units and illustrative probabilities only if efforts are scaled to [0,1]; NOT calibrated to an actual sector.

**Null checks**: u=0 => c=0, e* independent of H (crowding out vanishes); if standard-compliance guarantees all-to-all interoperability, r and e cannot vary independently, hence model inapplicable; if H is a pure subsidy with no product-market demand, policy welfare conclusions cannot be drawn; beta=0 negative derivative persists (no network effects required for the basic effect), so do NOT claim a novel network-effect theorem based on this derivative alone; heterogeneous firms, price competition, entry and welfare remain unsolved.

## Stronger, not-yet-proved headline research hypotheses
### RT2 — network topology and market contestability
A standard-setting program that certifies each product's connectivity to ONE reference implementation can support a hub-and-spoke implementation graph in which the reference is reachable from every certified product but cross-vendor complement providers face high bilateral connection cost. **Hypothesis to prove, not established**: when switching costs/data/control accumulate at the reference hub, a shift from pairwise cross-vendor testing to single-reference-only certification increases certified vendor counts while raising the hub's profit share and lowering effective customer multi-sourcing; a diversification of QEs can reverse this, provided the underlying technical protocol is not perfectly transitive. Simply observing a star graph is geometry, not new IO economics. Requires actual price/entry/substitution stages and competing technical architectures.
### RT3 — institutional composition and national spillovers
**Hypothesis, not established**: for standards with mandatory core plus optional extensions, national/industry SSO stakeholders may support the *same technical text* but differ on reference test suites; a transnational independent multiple-reference testing rule might prevent path-dependent allocation of cross-border complement investment even if the text is unchanged. However standard-setting committee votes on actual test architecture are not necessarily country-body ballots; demonstrate one real institution before modeling any vote. Need endogenous standard/testing design, competitor entry and national welfare incidence to reach international-economics scope.

## Empirical falsifiability
- Required novel measurable object: a **vendor × vendor × protocol-version pairwise interoperability graph** over time, combined with (i) which reference QEs each vendor passed, (ii) suite/test architecture changes, (iii) vendor update and product deployment, (iv) cross-vendor compatibility failures and their commercial costs.
- Sharp RT1 test: after a change favoring central reference certification (controlling for standard version), first-party reference pass rate rises but new non-reference pairwise pass rate falls, especially for firms with scarce engineering capacity and stronger cross-firm network linkages.
- Counterexample: if all certified products using one reference pass random peer-to-peer tests independent of their integration choices, mechanism invalid. Similarly if vendor broad compatibility effort never responds to reference testing incentives, no causal RT1.
- Sources: ETSI Plugtests; ISO15118/OCA documentation, industry QA labs and Open RAN multi-vendor tests. Public pairwise **microdata have not been verified**. Do not claim OCA certification flags measure realized success.

## Prior-art verdict and stopping conditions
Closest economic papers on partial compatibility, strategic certification, endogenously designed standards, and multihoming could already imply RT1. Thus assign **RESEARCH, N2/U pending direct published proposition comparison**; despite analytic feasibility, it is not a verified N3 contribution. If RT1 is merely generic budget crowd-out with a technology label, abandon this exact sign and require RT2's market price/entry/network topology effect to be genuinely non-contained. A standalone formula for a negative cross partial is not enough for IJIO/Journal of Economics.
