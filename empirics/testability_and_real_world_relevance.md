# Empirical feasibility and real-world relevance
2026-11-09. Distinguish observable **adoption/profiles** from unobserved interoperability and distinguish published institutions from research conjectures.

## A. Feasible primary data
| Source | Actually exposed | Outcome legitimately measurable | Not observed / warning | Link |
|---|---|---|---|---|
| ISO Open Data: deliverables | standard ID, publication date, current stage, editions, replaces, ICS, committee, scope; daily update (first published 2025-03-05) | new/revised standard publication, replacement events and specification timing | no project-level national DIS/FDIS votes, national adoption, vendor implementation or actual product compatibility | https://www.iso.org/open-data.html |
| ISO Open Data: committees | secretariat, P/O national members, scope, committee age; weekly update | prospective committee membership and composition | not historic membership panel before snapshots, no votes; national body not a national welfare-maximizing government | same URL |
| Open Charge Alliance certified products | vendor, country, product, software version, registration date, certification type, optional functionality flags, export to Excel | vendor/product optional profile take-up, breadth by year and generation | cross-vendor pairwise functional test success and unit shipment share NOT inferred from certificate record | https://openchargealliance.org/certified-companies/ |
| OCA certification specification | required Core vs optional Advanced Security, Smart Charging, ISO 15118 Support; OCPP 1.6→2.0.1 compatibility break and OCPP 2.1 backward compatibility | defined certification heterogeneity and revision regimes | conformance of optional feature not market popularity; OCA is not ISO government balloting | https://openchargealliance.org/certificationocpp/certification-ocpp-2-0-1/ ; https://openchargealliance.org/faq/ |
| OECD 2026 MRI mapping | types, sectors, cross-border conformity acceptance legal frameworks, operational features; 112 mapped instruments in sample? **Do not assert full coverage without source table check** | cross-national/cross-sector mutual recognition indicators subject to manual coding | agreement text does not certify implementation; sample selection; absence cannot automatically mean nonrecognition | https://doi.org/10.1787/56f2cfc7-en |
| WTO ePing TBT/SPS; WTO Specific Trade Concerns | notifications and cross-national expressed regulatory concerns | regulation changes and disputes | does NOT measure ISO negative votes, fine-grained laboratory test decisions, actual exporter-level entry | https://data.wto.org/en/dataset/ext_eping ; https://tradeconcerns.wto.org/ |
| METI mutual recognition | government-agreement scope by partner and sector, conceptual classifications | policy dates/scope if specific implementing source available | accreditation-body MRA is not legal import acceptance by itself | https://www.meti.go.jp/policy/economy/hyojun-kijun/mr/mr.html |

## B. Pilot 1: document convergence versus conformity-recognition in one product sector (preferred theory H5)
- Stage A: choose ONE sector with identifiable technical standard identifiers/revision dates and one MRA affecting *acceptance of test reports*, not merely laboratories' accredited status.
- Stage B: classify legal adoption, certificate acceptance and concrete customs/regulator procedures separately.
- Stage C: link product-by-origin trade or registered approved model counts to recognition and standard events, harmonized HS and technical standard crosswalk, and dates of operational launch.
- Stage D: compare exporting firms/varieties entering before/after MRA among categories with different prior certification burden, using an event-study or staggered DiD ONLY when plausibly exogenous treatment timing and clean controls exist. Do not infer causality from two aggregate time series.
- Strategic hypothesis needs specific prior protective rents: domestic producer market share or local certification-provider rents. The same observed testing friction may arise for legitimate quality assurance, not strategic exclusion.
- Killer data risk: public MRA metadata show legal frameworks but not actual second tests, rejections, fees or processing time. If these are unavailable, report only the *legal adoption* and trade association, not the behavioral mechanism.
- New source dated 2026-11-05: OECD explicitly distinguishes regulatory text from operational acceptance at borders; this validates question importance, not causal theory novelty.

## C. Pilot 2: OCPP optional-profile adoption (H6, H9)
1. Download OCA certified product list as a snapshot and archive retrieval date; record fields, distinct vendor and products; do not claim any numbers before the data have actually been fetched.
2. Parse mandatory Core, optional ISO15118, Smart Charging and Advanced Security by version, certification date and vendor-country.
3. If panel versions exist, estimate within-vendor optional profile entry/exit after certification program expansions (e.g. Apr 2025 additional OCPP2.0.1 profiles).
4. Outcome remains certified functionality; DO NOT declare pairwise actual interoperability. To obtain actual interoperability outcomes, seek documented raw independent charging-vendor plug-fest or laboratory pairwise data; as of this audit raw machine-readable market-representative outcomes are **not verified**.
5. Separate protocol families: OCPP connects charger/backend and ISO15118 covers EV/charger communication, so a single “same standard” flag is insufficient.
6. Distinguish product count from physical installed charger share (latter unavailable here).

## D. Pilot 3: smart-home protocols as portfolios (H9)
2026 Research Policy paper follows 97 platforms; its constructed dataset/published counts are empirical evidence of combined platform modes. For independent tests, code device support for Zigbee, Z-Wave, Matter, vendor proprietary protocols, software updates and complements per platform-year; verify historical code dates and coverage. Pairwise service quality, price/entry, and forced updates are harder. Avoid treating 97 observations as an exogenous experiment. Source https://doi.org/10.1016/j.respol.2026.105609

## E. Pilot 4: 3GPP disclosure restrictions (H12)
Chen & Xiao 2026 study U.S. sanctions, sanctioned-firm interactions and standards proposal approvals; data availability statement indicates embargo before open release, meaning independent replication now is limited. Its outcome is influence, not final compatibility/trade. Supplemental public SSO documents may not yield market outcomes. https://doi.org/10.1057/s41267-026-00856-9

## F. Sharp falsifiers
- H5: changes in foreign certificate acceptance do not alter retesting and entry, even in high-duplicate-cost sectors; change in strategic barriers fully accounted for by legitimate safety thresholds; uniform independent CAP rules.
- H9: introduction of shared third-party interfaces is followed by monotonic reduction in private interfaces and does not affect cross-platform complement breadth or price competition.
- H12: technology contribution restrictions affect only name attribution of approved proposals, not downstream feature quality/adoption or vendor entry, conditional on prior trends.

## G. Identification and legal guardrails
ISO-issued text and test reports may have licensing restrictions; ISO Open Data ODC-By covers specified metadata, not paid full standard texts. National standard catalogs have heterogeneous licensing. OECD mapping is a purposive documentation sample, not necessarily the universe. ISO/IEC voting's dual threshold and technical-comments regime must not be replaced by country-government utility without justification. WTO TBT separates voluntary standards, mandatory regulations, and conformity assessment. OECD 2026 MRIs distinguish government, accreditation-body and conformity-body arrangements.
