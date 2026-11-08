# P1-KS | Main contribution selection and research-gate review
Date: 2026-11-09 | branch: `research/p1-proof-novelty-gate-20261108`
Initial audited HEAD: `0db722d8526bb864bc9f32f0155feb1759f740c6`.
Status: **independent mock editorial decision, not author claim of proven new theorem; no changes to existing proofs or inventory**.

## 1. Main decision: what to write, and what not to claim
**Do not submit a 41-proposition catalogue.** After compressing 41 records, there are 6 analytic/economic clusters, of which 3 have economics to discuss and only 1 joint comparative-static cluster warrants a main-result investigation. **Tier A unconditional = 0.**

Selected central research question:
> Under installed-base user-count network externalities, when can strengthening the network effect increase the *global* gains from standardization while **reducing the number of nation-state votes in favour**, despite firms being able to choose adoption voluntarily?

Candidate not-yet-verified main statement (propose, do not present as unconditional theorem):
> For selected interior fulfilled-expectations price continuations O=1110 (after no publication) and F=1111 (after publication), h=1 and β∈[.1,.5], the existing-country cutoffs `τ_o(β),τ_c(β)` are increasing while global net welfare of F relative to O is strictly positive and increasing. A nonempty open set of country sizes therefore yields a 3/4-vote reversal from acceptance to rejection as β rises, given `kL<G3<kH` and sincere voting. This result does NOT assert a unique SPNE and is CONDITIONAL on global price-Nash and selection.

Economic mechanism: O has asymmetric installed-base network memberships (3 incumbent brands and 1 isolated entrant); moving to F eliminates an existing rent advantage of firms 0–2. Domestic consumer CS rises with β, but firms' worldwide rent loss weighs equally at the national level regardless of domestic size. Smaller incumbent countries can therefore cross the support threshold. A larger world gain is fully consistent with more national vetoes.

### Why this is not yet an independent IJIO contribution
1. Katz–Shapiro (1985), Proposition 7/8: inefficiently weak private compatibility incentives are long known.
2. Gandal–Shy (2001), §2.6 Eq. 11: national welfare = own CS + own firm's worldwide profits; §3.3 population asymmetry. §4 Prop.4/5 network recognition positive all countries in their different benchmark, so **not a literal theorem subsumption**, but exact sign reversal requires examining which extra primitive matters and why.
3. Stadler et al. (2022), §3: user network + historical base + quadratic location + pricing + compatibility already integrated at firm level.
4. Klimenko (2009) and Cheng–Huang (2025): high β can lead to low compatibility or veto-induced incompatibility. Only abstracts confirmed, propositions unavailable.
5. The author's old *brand-count P1* already contains 4 Yes→2 Yes, so this isn't a new qualitative prediction relative to the previous version. Need demonstrate new insight from **endogenous current-user network and historical installed base**, not merely algebraically change parameter labels.
6. Main β-reversal still conditional on 16-price-subgame global best responses; finite-stage trembling-hand perfection does not prove full game.

## 2. Main result architecture (lean paper)
| Manuscript location | Retain | Function |
|---|---|---|
| Model and market stage | L01–L02, L04–L06, L11 | define user-count FE and prove selected pricing equilibrium; no novelty advertisement |
| Lemma on O and F prices | L07, L09–L10; L08 only appendix | explicit continuous price continuation; q_i need not equal p_i |
| Proposition 1, market redistribution | L12–L15, optionally L14 | ΔCS>0, incumbent loses and entrant gains; precise h conditional |
| Lemma 2, voluntary adoption | P01,P03–P06, L15 | implement O or F; distinguish reduced adoption-game perfection and full extensive form |
| Main Proposition 2 (conditional candidate) | L16,P07–P09,L17 | country support cutoff, β derivative, world gain |
| Example/Corollary | P10–P11,C04; P12 optional | exhibits threshold and nonempty population set |
| Mechanism/robustness | C01–C03,C05,C07 | h=0 fails, h-profit vs h-vote threshold, equal populations |
| Appendix or omit | L03,L19,P02,P13,P14,P15,C06 | technical checks and game-selection caveats; paper presentation not centered on 45 voting Nash counts |

**Keep full original 41-record inventory intact.** Never translate 41 into 41 manuscript propositions.

## 3. Prioritized gates and a stop rule
### Gate 0: correct the equilibrium assertion before making a new claim
**Required**: show the selected price vector in each of the 16 adoption states is a *global* price Nash equilibrium allowing firm i an arbitrary destination-specific nonlocal price deviation `(p_i^0,...,p_i^3)`, with fulfilled-expectations consumer response fully re-solved. Local positive adjacent boundaries and FOCs do not suffice. A **sufficient nonlocal best-response inequality** is acceptable; no need to prove uniqueness of every possible price-Nash/FE branch if claiming selected-SPNE existence only.

**Stop condition:** if any one of the 16 intended price continuations fails even as a Nash profile under a permitted deviation, re-solve the price stage and recompute adoption/welfare/votes. Do not rely on the present threshold values as full-game results.

### Gate 1: decisive novelty test (obtain full published text)
Check the exact propositions and comparative statics in:
- Barrett & Yang (2001) JIE 54:171–191 DOI 10.1016/S0022-1996(00)00082-9, especially incumbent government response with installed users;
- Klimenko (2009) JIE 77:151–166 DOI 10.1016/j.jinteco.2008.08.005, especially sign of country policy responses to β;
- Cheng & Huang (2025) J Econ 145:31–57 DOI 10.1007/s00712-024-00896-5, especially why high β prevents compatibility with veto;
- If necessary Toshimitsu published 2026 and Economides (1989).
For each closest theorem: transcribe mathematical primitives, choice sets, comparative-static derivatives, welfare condition and exact theorem/page, then try parameter restrictions or player/payoff transformations. **If all candidate comparative statics reduce to these results without a genuine new condition, stop upgrading the claim and choose a short technical paper or redesign.** Absence of online final PDF means **unverified**, not “novel”.

### Gate 2: find the smallest new theorem
**Primary attempt**: common historic base `h` but arbitrary population vector `w`. Derive country opposition threshold in h, compare to corporate profit-loss thresholds analytically, and a necessary and sufficient criterion for `dτ_o/dβ>0` on a nontrivial two-dimensional (β,h) set. Then show the set where (i) world gain increases, (ii) at least 2 incumbents switch votes, (iii) entrant joins only if approved and (iv) interior pricing is valid is open and nonempty.

**Independent sample exact facts** (selected interior continuation only):
- Corporate profit-loss threshold outer `h_o^{profit}(1/2)≈0.0538446`.
- Corporate profit-loss threshold center `h_c^{profit}=1/4`.
- **Country 0 with w0=.12 at β=.5** welfare flips at about `h_o^{vote}≈0.65029236`; the country accepts for `h=.5` despite incumbent lost profit. This separation is more economically informative than the raw quartic `β*=.3496702833`.
- At h=0 all incumbents profit from O→F in checked interval; at h=1, β rise .1→.5 flips the outside countries; at equal w_i=.25 the benchmark reversal fails.
- Price candidates may cease to be globally best responses or interior outside calibrated range; do not make universal h claim on endpoint arithmetic.

### Gate 3: institutional consistency and a minimal sensitivity
Clarify why “publication” lowers firm3's cost from `kH=.4` to `kL=.01`. A single-page microfoundation (recognition eliminates duplicated conformity certification or grants network access on fixed licence) is sufficient if it honestly reproduces primitives. Avoid building a new huge toolkit market unless necessary.
2026 ISO/IEC Directives Part 1 §§2.6.3,2.7.3 include **two conditions** (2/3 yes among P members and <=1/4 valid negative), abstentions excluded, technical justification for negative votes. This benchmark is precisely **4 mandatory valid Yes/No ballots** only, not an exact general ISO voting protocol.

### Gate 4: journal benchmark
Before submitting, compare one related theoretical proposition with recent IJIO articles *on their actual contribution* (e.g. Lu, Matsushima & Shekhar (2025), IJIO 103, 103200, https://doi.org/10.1016/j.ijindorg.2025.103200: network expectations and private personalized pricing cause non-obvious new fee response). Look for an additional endogenous channel of comparable specificity, not longer proofs or extra cosmetic robustness tables.

## 4. Explicit false leads (negative results)
- **“User-count externalities are new in differentiated product market”: FALSE.** Stadler §3 uses installed bases + current customers and quadratic Hotelling.
- **“Interoperability raises CS while firms lose, novel paradox”: FALSE as general idea.** Katz–Shapiro already establishes private/social wedge.
- **“World welfare gain with political opposition cannot be in existing international standardization research”: UNJUSTIFIED.** Barrett–Yang, G&S conversion-cost unions, Klimenko show international policy conflict; exact inclusion not checked.
- **“4-firm 3/4 ISO median cutoff is a new voting theorem”: FALSE.** Generic order statistic; also ISO validity is restrictive.
- **“Voluntary adoption necessary for ballot reversal”: FALSE.** Once O and F are imposed, the same conditional threshold voting result obtains. Adoption is needed to endogenize *implementation feasibility*, not its vote arithmetic.
- **“Publishing ISO standard automatically implements standard”: FALSE by model design.** Adoption is voluntary; actual ISO publication never mechanically changes technical costs without assumed mechanism.
- **“Existing installed base must be positive in all network games for policy reversal”: NOT PROVED.** C01 only for this particular 4x4 setting and range.
- **“Price FE local Nash proves the full extensive-form game”: FALSE.** Nonlocal, segmented, noninterior alternatives need attention.
- **“The new KS model necessarily dominates the old P1”: NOT ESTABLISHED.** KS variant increases realism of installed-user channels and gives distinct h thresholds; it also adds hard price-game gaps and no demonstrably new overarching vote reversal.

## 5. Journal editing judgment (no fabricated percentages)
| Target | Current | If price+prior-art+new general result pass |
|---|---|---|
| International Journal of Industrial Organization | Not yet journal-independent contribution; high desk risk | Consider only if general h/β comparative-static or institution interaction is clearly more than existing mechanisms |
| Journal of Industrial Economics | Not yet; stronger IO policy/empirical meaning necessary | Plausible if economic mechanism and generality convincingly developed |
| Journal of International Economics | Not suited to present 4x4 calibration; trade/policy content needs genuine new generalization | Ambitious even after gates, no current recommendation |
| Journal of Economics | More plausible for compact analytic extension, but directly adjacent to Buccella(2023), Cheng–Huang(2025) | Best realistic exploratory target only if clearly differentiated theorem |
| Research in Economics | Potential applied theory note after full price proof and rigorous novelty | Consider, verify current editorial scope and accepted comparators |
| other | Network and Spatial Economics if spatial comparative statics becomes dominant | Needs a real spatial position novelty rather than national-ballot arithmetic |

**Three separate stages:** (1) “formally submit-able”: a polished manuscript is possible but formal submission should await mathematical gap closure; (2) “peer-review defensible”: global price continuation plus exact prior-art crosswalk; (3) “publishable independent contribution”: genuine new economic comparative-static/general threshold theorem recognized by reviewers. Stages (2) and (3) not yet satisfied.

## 6. Decisions Q1–Q6
**Q1**: no completed Tier A/IJIO-level main result yet; conditional P09+P11 merits exploration.  
**Q2**: main candidate β increases opposition threshold of small incumbent countries despite increasing world benefit; G&S benchmark §4 gives different national sign, but installed-base/publication initial partition is essential and novelty over other papers not established.  
**Q3**: not yet proven to exceed combination of known installed-base, rents, national welfare wedge and majority rule.  
**Q4**: KS user-count yields endogenous sales feedback + historical h counterfactual, more theoretically plausible; not demonstrated to be more journal-worthy than simpler old P1; old P1 already has reversal.  
**Q5**: retain in text L12–L17/P07–P09, possibly P11 and C01–C03; technical support P01–P06 and FE pricing lemmas; relocate P10,P12,P13,P15,C04,C05,C07 to figures/appendix; P14/C06 are game/institution caveats not novelty.  
**Q6**: **additional minimal theorem and price Nash completion**, not immediate submission, not wholesale redesign (unless Gates 0/1 fail).

## 7. Source-of-truth and reproduction ledger
Read on specified branch: `proofs/p1_ks_complete_result_inventory_20261109.md` (blob `e8d799f7be3e9238cad224b67c02548fa421c6b6`), `proofs/p1_ks_userbase_network_reversal_20261108.md` (blob `23f5d2d7246480b71e69cdcc418c2374f3fe0e17`), `proofs/p1_complete_backward_induction_gameform_20261108.md`, `literature/independent_adversarial_novelty_audit_20261108.md`, `code/verify_ks_userbase_vote_reversal_20261109.py`, `code/test_ks_inventory_extra_20261109.py`. Independently recomputed welfare thresholds `τ_o(.1)≈.099055`, `τ_o(.5)≈.137588`, `τ_c(.1)≈.038924`, `τ_c(.5)≈.049484`, `β*=.349670283323` using separate SymPy expressions; existing code treated as verification reference not accepted as global equilibrium proof.
Published source provenance and proposition-level overlaps are recorded in `literature/ks_prior_art_proposition_crosswalk_20261109.md`. The full 41-record assessments are in `literature/ks_independent_theorem_level_novelty_audit_20261109.md`. These records deliberately do not overwrite any model proof, inventory or prior audit.
