# Gate 3 — Prior-art novelty audit of P1 (theorem-level, adversarial)

**Date:** 2026-11-08. **Decision:** P1 is a mathematically sharp **conditional existence result**; it is **not yet confirmed to be a first-in-literature or IJIO/RIO-level novel theorem**. A novel analytical formula is not automatically a novel economic mechanism. This audit is bounded by the accessible full text, original abstracts, and source excerpts listed below.

## 1. Exact candidate result to be tested for novelty

In a 4-firm Salop–Bertrand international market with a 3-firm existing compatible group, increasing network quality increment \(d\) can cause **two countries to cease supporting full interoperability**, even though:
- every brand's compatible-brand gross utility weakly rises, strictly for the entrant;
- total world welfare from implementation (net of real cost) remains positive;
- the cost-window condition makes voluntary entrant adoption privately optimal if the standard is issued, and nonadoption privately optimal if it is not;
- the candidate post-ballot states are strict Nash equilibria of their respective finite adoption subgames.

The specific population threshold and closed-form price/Nash proof are
\[
w_i\ge \tau(d)=\frac{4(d+6)}{216-13d},
\qquad d^*(w)=\frac{216w-24}{13w+4},
\]
with \(d^*=48/139\) at \(w=3/25\).

**Economic channel:** a small country's home-market consumer surplus rises in proportion to its population, while the world-market profit of its incumbent exporter falls when the entrant joins and removes part of its relative network advantage. A national-body vote weights countries equally, not proportionally to the welfare or consumer population affected.

## 2. Head-to-head comparison

| Paper / exact claim checked | Already known | Does P1 evade direct subsumption? | Remaining novelty danger |
|---|---|---|---|
| **Gandal & Shy (2001), JIE**, introduction, §§3–4 | Governments' foreign-standard recognition and trade-diverting standardization unions; section 3.3 explicitly discusses **different population sizes** (as acknowledged in the journal article). | The benchmark does **not** model a 4-country ISO final ballot followed by individual firms' voluntary interoperation. | **Size asymmetry and protection of domestic profits are already in the baseline.** No claim that size or world-profit capture is discovered here. |
| **Barrett & Yang (2001), JIE**, abstract/confirmed publication | Incumbent firms may rationally remain incompatible with international standards; the host government may value their deviation despite consumer network effects. | P1's distinctive object is the **comparative static of votes and a sufficient coalition size**, given market-wide consumer network gains; not merely a refusal to adopt. | This is still conceptually very close to rational standard incompatibility, so exact formal results in full text must be compared before asserting novelty. |
| **Klimenko (2009), JIE**, publisher abstract | Government strategic compatibility policies can yield excessive compatibility or very low compatibility and trade, depending on network strength. | P1 is a discrete international committee approval game with 1-state-1-vote vs different country market sizes; Klimenko's central model is strategic compatibility policy, not the same four-voter game. | Welfare divergence and strategic compatibility effects are well known; a threshold-crossing example alone may be seen as minor. |
| **Goerke & Holler (1995), Public Choice**, abstract | Farrell–Saloner coordination problem, welfare of majority/supermajority voting rules under network effects; decision rules can prevent worst outcomes. | P1 has explicit horizontally differentiated international product-market Bertrand pricing **after** voting and uneven national appropriation of profits; not only buyer voting in a coordination game. | Generic supermajority inefficiency is known; cannot claim novelty from the ISO threshold alone. |
| **Spulber (2019), Economic Journal, Proposition 6 and Corollary 2 (full-text HTML)** | In his model without SEPs, each **vertically related** adopter group elects the efficient standard by majority, and votes for efficient innovation are nondecreasing in **quality**; voting power and market power can counterbalance. | P1's voters are **countries**, maximizing national consumer surplus plus export profits from **horizontal** product differentiation and price competition. All consumer mass is inelastically served, so prices reallocate profits without Spulber's vertical short-side-of-market mechanism. P1 is **not a counterexample to Spulber's theorem**, whose assumptions differ. | The general proposition “a standard vote can disagree with social efficiency” is not novel. Need show a new mechanism beyond a simple change of voter types and rent distribution. |
| **Fu, Tan & Wang (2023), IJIO**, publisher article | Competing SSOs, royalty-based technical choices, network effects and coalition formation. | P1 does not endogenise SEP royalty portfolios or competing SSO technology packages; instead it studies international government votes and exporter-profit externalities. | An added endogenised proposal alone would also risk overlap with this paper. |
| **Balzer & Schneider (2021), IJIO**, abstract | SSO participation refusal can itself be strategic; information disclosure and participation affect standard-setting coordination. | P1 fixes voting participation and does not assert participation/refusal novelty. | Extending NP participation or signaling later must cite this paper. |

## 3. Most important specific novelty caveats

1. **The benchmark already discusses population asymmetry.** Gandal & Shy explicitly write that §3.3 investigates how differing population sizes affect standardization-union incentives. P1 should not be framed as the first examination of size asymmetry.
2. **Spulber is not disproved.** His efficiency result relies on vertically complementary adopter groups, market-clearing output and specific distributional conditions. Here the consumer market is fully covered and firms are horizontally competitive. Reversing votes with the network parameter is not formally the same comparative static as Spulber's innovation-quality parameter.
3. **The ISO-specific content is modest at present.** A 3-of-4 binary approval vote is equivalent to a generic 75% supermajority in this restricted environment. ISO's dual criterion, NP admission conditions, CD consensus and post-rejection revision have not created a new theorem.
4. **The implementation channel is assumed.** Publication-induced cost reduction \(k_H\to k_L\) is plausible, but it is not a novel endogenous economic mechanism unless information production, tool provision, participation or licensing is explicitly modeled and constrained.
5. **The effect may be narrow in parameter space.** With \(w_0=w_2=.12\) and original \(d\in[1/3,3/8]\), a sign change requires \(w\in(76/635,68/563)\), a relatively narrow share band. The global price proof extends much further, to \(0<d<6/7\), permitting a wider but still economically specific parameter region. Importance depends on an economically motivated interpretation of the asymmetry.
6. **Network quality is compatible brand count, not user-base size.** That parameterization is inherited from the project baseline but may be considered a limited representation of true scale-dependent network effects. This should be stated rather than claimed as generic.

## 4. Independent theoretical contribution: provisional tiers

- **IJIO:** No. The current work proves a sharp existence/threshold result in a stylized institutional environment; it does not yet have a broad, non-obvious IO mechanism shown to survive general country counts, user-base effects, endogenous proposals, and sophisticated voting.
- **Review of Industrial Organization:** Conditional. Possible if the P1 mechanism is shown to be more than a routine combination of existing voting and lock-in results, and is complemented by a useful endogenous proposal or institution-design theorem that makes the ISO procedure matter.
- **Journal of Economics / relevant specialist journal:** Plausible research target, not an acceptance forecast. A fully audited strict-subgame equilibrium, a concise threshold theorem and meaningful welfare/robustness could form an independently publishable applied theory note **if** no stronger formal prior art subsumes it.
- **Immediate submission:** Not recommended. The extra normative/institutional results and theorem-level novelty comparison are not yet finished.

## 5. Sources actually inspected

1. [Gandal & Shy (2001), original publisher abstract and introduction](https://www.sciencedirect.com/science/article/pii/S0022199600000672). The publisher-hosted introduction explicitly mentions section 3.3 on population sizes. The full JIE propositions were not fully rederived in this Gate.
2. [Spulber (2019), full HTML, §3 Proposition 6 and Corollary 2](https://onlinelibrary.wiley.com/doi/full/10.1111/ecoj.12606). We compare the verified theorem statements and assumptions, not merely the abstract.
3. [Barrett & Yang (2001), publisher abstract](https://www.sciencedirect.com/science/article/pii/S0022199600000829). Full proposition-level proof mapping remains outstanding because the full text was not accessible in this session.
4. [Klimenko (2009), publisher abstract](https://www.sciencedirect.com/science/article/pii/S0022199608001244). Full proposition-level proof mapping remains outstanding.
5. [Goerke & Holler (1995), abstract and bibliographic record](https://ideas.repec.org/a/kap/pubcho/v83y1995i3-4p337-51.html). Full theory mapping not yet completed.
6. [Fu, Tan & Wang (2023), IJIO](https://doi.org/10.1016/j.ijindorg.2023.102952).
7. [Balzer & Schneider (2021), IJIO](https://www.sciencedirect.com/science/article/pii/S0167718721000576).

## 6. Gate 3 verdict

**Passed a weaker test:** P1 is not literally the same theorem as Spulber's Proposition 6, and the Gandal–Shy model lacks its specific post-vote adoption structure.

**Not passed a stronger test:** Given the prior results on rational incumbent incompatibility and strategic government compatibility policy, the claim that P1 is a first-in-literature economic mechanism cannot yet be established. Treat “novelty” as **promising but unverified**, not confirmed.

**Next most productive task:** (i) obtain and carefully compare full Barrett–Yang and Klimenko propositions; (ii) demonstrate one additional implication specific to institutional **vote versus voluntary adoption** or an endogenous *technology proposal*, not just adding complexity; (iii) stress-test alternative network externality definitions and larger country sets. Do not proceed to IJIO manuscript drafting based solely on P1.
