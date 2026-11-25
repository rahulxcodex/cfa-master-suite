"""
Generate 180 CFA Level 2 Ethical and Professional Standards vignette questions
across 30 distinct institutional case vignettes (V01 to V30, 6 questions each).
Output: data/courses/l2_ethics.json
"""
import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(SCRIPT_DIR)
if SCRIPT_DIR not in sys.path:
    sys.path.insert(0, SCRIPT_DIR)

from qbank_helper import add_l2, save_validated_json

SUBJECT = "Ethical and Professional Standards"
OUTPUT_PATH = os.path.join(ROOT_DIR, "data", "courses", "l2_ethics.json")

VIGNETTES = [
    # =========================================================================
    # V01: Equity Research & Investment Banking Firewalls
    # =========================================================================
    {
        "vignette_id": "V01",
        "vignette_title": "Meridian Capital Partners: Research Firewalls and Issuer Pressure",
        "module": "Module 2: Guidance for Standards I-VII",
        "topic": "Independence, Conflicts, and Research Objectivity",
        "subtopic": "Equity Research & Investment Banking Walls",
        "vignette_text": (
            "Meridian Capital Partners is a mid-sized investment bank and institutional brokerage based in Toronto. "
            "Elena Vance, CFA, is a senior equity research analyst covering North American industrial automation firms. "
            "Meridian's investment banking (IB) division is competing to serve as lead bookrunner on a USD 650 million "
            "secondary equity offering for Borealis Robotics Inc., a firm Vance has covered for four years with a "
            "long-standing 'Hold' rating. Before pitching Borealis management, the head of IB emails Vance asking her "
            "to join a closed-door strategy meeting to discuss 'constructive valuation angles' that might help win the mandate.\n\n"
            "Vance declines the pitch meeting, citing Meridian's written firewall policy. However, two weeks later, "
            "Meridian's Head of Equities reminds Vance during her mid-year compensation review that 35% of the research "
            "department's bonus pool is funded by IB deal originations and suggests that her cautious thesis on Borealis "
            "is 'commercially unhelpful.' Meanwhile, Borealis's CFO invites Vance to visit its automated assembly plant "
            "in northern Alberta, located 300 kilometers from the nearest commercial airport, and offers to fly Vance on "
            "the company's chartered twin-engine plane from Edmonton because no commercial flights serve the airstrip. "
            "Vance accepts the flight for the single-day inspection and pays for her own hotel in Edmonton.\n\n"
            "Back in Toronto, Vance completes a separate research initiation on a small-cap firm, Solis Sensors Ltd., "
            "under a flat-fee issuer-paid research contract between Meridian and Solis. Under the contract, Meridian "
            "receives USD 45,000 annually regardless of rating or target price, and the report prominently discloses the "
            "issuer-paid arrangement on the cover page. Before publishing, Vance shares a draft containing only the "
            "historical financial tables and product descriptions with Solis's investor relations team to verify factual "
            "accuracy, withholding her valuation model, investment rating, and target price."
        ),
        "questions": [
            {
                "los": "Analyze independence and objectivity threats between investment banking and equity research under Standard I(B).",
                "question": "By inviting Vance to join the closed-door pitch meeting to discuss 'constructive valuation angles' for Borealis, the head of IB most likely asked Vance to engage in conduct that violates:",
                "options": {
                    "A": "Standard I(B) Independence and Objectivity, because participating in IB pitches with valuation messaging compromises research impartiality.",
                    "B": "Standard II(A) Material Nonpublic Information, because any internal IB pitch discussion creates MNPI for the covering analyst.",
                    "C": "Standard VI(C) Referral Fees, because the IB head is attempting to compensate research for generating an underwriting mandate."
                },
                "answer": "A",
                "explanation": "Standard I(B) Independence and Objectivity requires analysts to maintain impartiality and prohibits cross-departmental pressure where research is used to win investment banking mandates. Participating in an IB pitch to craft 'constructive valuation angles' directly undermines research independence.",
                "distractors": {
                    "B": "Internal pitch strategy discussions are not automatically MNPI about Borealis's future results unless Borealis shared confidential deal terms; the primary ethical conflict here is independence under Standard I(B).",
                    "C": "Standard VI(C) covers third-party referral compensation for client recommendations, not internal investment banking cross-selling pitches."
                }
            },
            {
                "los": "Evaluate research analyst compensation structures under Standard I(B) and Standard VI(A).",
                "question": "Regarding Meridian's bonus pool policy tying 35% of research bonuses to IB deal originations, which statement is most accurate?",
                "options": {
                    "A": "The structure is acceptable under the Code and Standards provided Vance discloses the bonus formula on the last page of her reports.",
                    "B": "Linking analyst compensation directly to IB transaction revenue violates Standard I(B) guidelines on research independence.",
                    "C": "Vance violates Standard IV(B) Additional Compensation Arrangements by accepting a firm bonus funded by IB fees."
                },
                "answer": "B",
                "explanation": "Under Standard I(B) guidance on investment banking relationships, analyst compensation must not be tied directly to specific investment banking transactions or deal origination success, as doing so creates an acute incentive to issue favorable coverage to attract or retain banking clients.",
                "distractors": {
                    "A": "Disclosure under Standard VI(A) does not cure an improper compensation structure that compromises Standard I(B) independence and objectivity.",
                    "C": "Standard IV(B) addresses outside compensation arrangements external to the employer, not internal bonus pools set by the analyst's own employer."
                }
            },
            {
                "los": "Apply Standard I(B) guidance regarding issuer-paid travel for due diligence site visits.",
                "question": "Did Vance violate Standard I(B) Independence and Objectivity by accepting Borealis's chartered flight to the northern Alberta plant?",
                "options": {
                    "A": "Yes, because analysts may never accept any form of transportation paid for by an issuer under any circumstances.",
                    "B": "Yes, because she should have also required Meridian to reimburse Borealis for the pro-rata charter fuel cost.",
                    "C": "No, because commercial transportation was unavailable to the remote facility and she paid her own commercial lodging."
                },
                "answer": "C",
                "explanation": "Under Standard I(B) guidance, members and candidates must pay for their own commercial travel and accommodations during issuer site visits; however, when commercial transportation is unavailable (such as a remote site 300 km from an airport), accepting strictly limited issuer-provided transport for the visit itself does not violate Standard I(B).",
                "distractors": {
                    "A": "Standard I(B) explicitly permits a narrow exception for remote sites where commercial transportation is unavailable, provided the trip is strictly business-focused.",
                    "B": "Reimbursement is not required when no commercial option exists and Vance already covered her own hotel expenses."
                }
            },
            {
                "los": "Assess issuer-paid research arrangements under Standard I(B) and Standard VI(A).",
                "question": "With respect to the Solis Sensors Ltd. issuer-paid research contract, Vance's actions are:",
                "options": {
                    "A": "In compliance with the Code and Standards, because the fee is flat and non-contingent and the arrangement is prominently disclosed.",
                    "B": "A violation of Standard I(B), because any research paid for by the subject issuer is inherently compromised regardless of fee structure.",
                    "C": "A violation of Standard VI(A), because disclosing the issuer-paid fee on the cover page fails to disclose the exact USD 45,000 amount."
                },
                "answer": "A",
                "explanation": "Issuer-paid research is permitted under Standards I(B) and VI(A) provided the compensation is a flat fee not linked to conclusions, recommendations, or stock performance, the analyst maintains complete editorial independence, and the relationship is prominently disclosed.",
                "distractors": {
                    "B": "The Standards do not ban issuer-paid research outright; flat-fee structures with full disclosure are explicitly acceptable when independence is preserved.",
                    "C": "Standard VI(A) requires prominent disclosure of the conflict's nature and substance (the issuer-paid arrangement), not necessarily the exact dollar contract fee unless required by local regulation."
                }
            },
            {
                "los": "Determine permissible pre-publication fact-checking with subject issuers under Standard I(B).",
                "question": "By sending Solis's investor relations team the draft containing only historical financial tables and product descriptions prior to publication, Vance:",
                "options": {
                    "A": "Violated Standard II(A), because sharing a research draft alerts the issuer to upcoming market-moving coverage.",
                    "B": "Complied with Standard I(B), because sharing factual sections without valuation models or ratings is permissible for fact-checking.",
                    "C": "Violated Standard III(B) Fair Dealing, because the issuer saw parts of the report before Meridian's institutional clients."
                },
                "answer": "B",
                "explanation": "Under Standard I(B) best practices, an analyst may allow a subject company to review factual portions of a draft report (historical data, product descriptions) to verify accuracy, provided the analyst withholds the valuation section, target price, recommendation, and summary.",
                "distractors": {
                    "A": "Standard II(A) prohibits trading or tipping on MNPI; sending factual sections to the issuer for verification is standard research practice and not an MNPI violation.",
                    "C": "Standard III(B) governs fair dealing among investment clients when disseminating recommendations; checking facts with an issuer without sharing conclusions does not violate III(B)."
                }
            },
            {
                "los": "Identify supervisory obligations of department heads regarding compliance walls under Standard IV(C).",
                "question": "By pressuring Vance during her bonus review because her Hold rating was 'commercially unhelpful' to IB, Meridian's Head of Equities most likely violated:",
                "options": {
                    "A": "Standard IV(C) Responsibilities of Supervisors and Standard I(B) Independence and Objectivity.",
                    "B": "Standard IV(A) Loyalty, by placing the IB department's revenue above Meridian's research reputation.",
                    "C": "Standard V(A) Diligence and Reasonable Basis, by failing to review Vance's discounted cash flow model."
                },
                "answer": "A",
                "explanation": "A supervisor who pressures an analyst to alter or soften an objective rating to accommodate investment banking fails both Standard I(B) (compromising independence) and Standard IV(C) (failing to enforce compliance firewalls and prevent ethical breaches among subordinates).",
                "distractors": {
                    "B": "Standard IV(A) addresses employee loyalty to the employer's legitimate interests; pressuring an analyst to breach independence harms both clients and firm integrity under I(B) and IV(C).",
                    "C": "The Head of Equities did not issue an unsupported investment recommendation; the breach is pressuring Vance's independence and failing supervisory duties."
                }
            }
        ]
    },
    # =========================================================================
    # V02: Soft Dollars, Client Brokerage & Execution
    # =========================================================================
    {
        "vignette_id": "V02",
        "vignette_title": "Crestview Asset Management: Client Brokerage and Soft-Dollar Allocation",
        "module": "Module 2: Guidance for Standards I-VII",
        "topic": "Fiduciary Duty and Brokerage Practices",
        "subtopic": "Soft Dollars & Client Brokerage",
        "vignette_text": (
            "Crestview Asset Management manages USD 4.2 billion in institutional global equity mandates. Marcus Thorne, CFA, "
            "serves as Chief Investment Officer and oversees Crestview's brokerage allocation committee. Crestview's Form ADV "
            "and client investment management agreements disclose that Crestview may use client brokerage commissions ("
            "'soft dollars') to acquire eligible research services. Over the past quarter, Crestview paid an average "
            "commission of USD 0.04 per share to Apex Execution Brokers, compared with USD 0.015 per share quoted by "
            "discount electronic execution venues.\n\n"
            "Under the arrangement with Apex, Crestview receives three items: (1) proprietary quantitative earnings-revision "
            "feeds used directly by portfolio managers to select equities, (2) a multi-purpose market data terminal whose "
            "vendor estimates 60% of its functionality supports investment research and 40% supports client billing and "
            "performance reporting, and (3) a cloud-based CRM marketing platform used by Crestview's sales team to pitch "
            "prospective endowments. Thorne approves paying 100% of all three invoices with client soft dollars generated "
            "from Crestview's flagship Global Growth Fund.\n\n"
            "Separately, one large pension client, Beacon Municipal Pension, instructs Crestview in writing to direct 75% "
            "of its equity trades to Summit Securities, a minority-owned broker-dealer charging USD 0.05 per share, in "
            "exchange for Summit providing Beacon with pension-plan consulting software. Thorne executes the directed "
            "trades as requested without sending any written notice to Beacon regarding execution costs, and decides to "
            "cross-allocate Apex's quantitative earnings feed exclusively to Global Growth Fund while using Global Growth's "
            "commissions to subsidize research applied solely to Crestview's Emerging Markets sleeve."
        ),
        "questions": [
            {
                "los": "Apply Standard III(A) Loyalty, Prudence, and Care to soft-dollar usage for non-research overhead.",
                "question": "Paying for the cloud-based CRM marketing platform with client soft dollars most directly violates:",
                "options": {
                    "A": "Standard III(A) Loyalty, Prudence, and Care, because client brokerage may only purchase goods and services that directly benefit clients.",
                    "B": "Standard VI(C) Referral Fees, because Apex is effectively paying Crestview a fee to attract new endowment prospects.",
                    "C": "Standard V(C) Record Retention, because CRM systems are not approved repositories for research records."
                },
                "answer": "A",
                "explanation": "Under Standard III(A) Loyalty, Prudence, and Care, client brokerage belongs to the client. Using soft dollars to pay for marketing or business-development tools (such as a sales CRM) benefits the investment manager rather than existing clients and violates fiduciary duty.",
                "distractors": {
                    "B": "Apex is providing a firm expense item via client commissions rather than paying a referral fee for client introductions.",
                    "C": "The violation concerns misappropriating client brokerage for firm marketing overhead, not record retention periods."
                }
            },
            {
                "los": "Evaluate mixed-use soft-dollar items under Standard III(A) and the Asset Manager Code.",
                "question": "How should Thorne properly handle the invoice for the multi-purpose market data terminal?",
                "options": {
                    "A": "Pay 100% with soft dollars because the majority (60%) of its usage supports investment research.",
                    "B": "Allocate 60% of the cost to client soft dollars and pay the remaining 40% using Crestview's own hard dollars.",
                    "C": "Pay 100% with hard dollars because mixed-use products are categorically prohibited from soft-dollar arrangements."
                },
                "answer": "B",
                "explanation": "Under Standard III(A) and CFA Institute Soft Dollar Standards, mixed-use products must be reasonably allocated based on usage: only the portion directly aiding investment decision-making (60%) may be funded with client soft dollars, while the firm-overhead/administrative portion (40%) must be paid with the firm's hard dollars.",
                "distractors": {
                    "A": "Having >50% research usage does not allow charging the administrative 40% portion to clients.",
                    "C": "Mixed-use items are permitted in soft-dollar programs so long as the manager makes a documented, good-faith cost allocation."
                }
            },
            {
                "los": "Analyze best execution obligations when paying above-minimum brokerage commissions.",
                "question": "Paying USD 0.04 per share to Apex instead of USD 0.015 per share to an electronic venue is permissible under Standard III(A) only if Thorne:",
                "options": {
                    "A": "Determines in good faith that the higher commission is reasonable relative to the value of execution quality and research benefiting clients.",
                    "B": "Discloses the USD 0.025 commission spread in the next annual client newsletter without evaluating execution quality.",
                    "C": "Obtains unanimous written approval from all Global Growth Fund investors prior to each trade."
                },
                "answer": "A",
                "explanation": "Best execution under Standard III(A) does not require always paying the lowest commission rate; higher commissions are permissible when the manager makes a good-faith determination that the total value of execution quality and eligible client-benefiting research justifies the price.",
                "distractors": {
                    "B": "Disclosure alone does not satisfy the duty of loyalty and prudence if the manager fails to evaluate execution quality and value received.",
                    "C": "Trade-by-trade unanimous investor approval is neither practical nor required when soft-dollar policies are disclosed and execution/research value is reasonably assessed."
                }
            },
            {
                "los": "Assess client-directed brokerage duties under Standard III(A).",
                "question": "With respect to Beacon Municipal Pension's directed-brokerage instruction to use Summit Securities, Thorne:",
                "options": {
                    "A": "Complied fully, because a manager must follow explicit written client directions regardless of execution cost.",
                    "B": "Should have notified Beacon in writing that directed brokerage may compromise best execution and increase transaction costs.",
                    "C": "Violated Standard III(B) Fair Dealing, because Summit's USD 0.05 commission rate differs from Crestview's USD 0.04 rate."
                },
                "answer": "B",
                "explanation": "When a client directs brokerage to a specific broker for the client's own benefit (such as pension software), the manager must follow the instruction but has a fiduciary duty under Standard III(A) and V(B) to disclose in writing that directed brokerage can hinder best execution, block order aggregation, and increase costs.",
                "distractors": {
                    "A": "Following client instructions is necessary, but omitting the written disclosure regarding best-execution compromises breaches fiduciary care.",
                    "C": "Beacon instructed its own account's brokerage; using a different rate at the client's explicit instruction does not unfairly harm other clients unless Crestview delays other clients' trades."
                }
            },
            {
                "los": "Identify improper cross-subsidization of soft-dollar research across client accounts.",
                "question": "Using Global Growth Fund's commissions to acquire research applied exclusively to the Emerging Markets sleeve violates:",
                "options": {
                    "A": "Standard III(A) Loyalty, Prudence, and Care, because Global Growth clients pay for research from which they receive no benefit.",
                    "B": "Standard III(C) Suitability, because quantitative earnings feeds are inappropriate for Emerging Markets portfolios.",
                    "C": "Standard VI(B) Priority of Transactions, because Emerging Markets trades were executed ahead of Global Growth trades."
                },
                "answer": "A",
                "explanation": "While soft-dollar research need not benefit every single client in exact proportion on every trade, intentionally using one client group's commissions solely to subsidize research used exclusively for a different client group violates Standard III(A) Loyalty, Prudence, and Care.",
                "distractors": {
                    "B": "There is no indication that earnings feeds are unsuitable for Emerging Markets; the breach is cross-subsidizing brokerage costs across separate client groups.",
                    "C": "Standard VI(B) concerns prioritizing client transactions over personal/beneficial-owner trades, not soft-dollar research cross-subsidization."
                }
            },
            {
                "los": "Apply Asset Manager Code Section C (Trading) and Section F (Disclosures) to brokerage practices.",
                "question": "Under the CFA Institute Asset Manager Code of Professional Conduct, which policy is Crestview explicitly required to maintain regarding soft dollars?",
                "options": {
                    "A": "Prohibit all soft-dollar arrangements completely across both institutional and retail strategies.",
                    "B": "Disclose its soft-dollar policies and explain how client brokerage benefits clients rather than the manager.",
                    "C": "Rebate 50% of all soft-dollar research credits directly to clients at year-end in cash."
                },
                "answer": "B",
                "explanation": "Under Asset Manager Code Section C (Trading) and Section F (Disclosures), managers do not have to ban soft dollars, but they must clearly disclose their soft-dollar policies, ensure client brokerage is used strictly for the benefit of clients, and provide transparency on broker selection and execution costs.",
                "distractors": {
                    "A": "The Asset Manager Code permits soft-dollar arrangements when strictly governed and disclosed, rather than mandating a blanket ban.",
                    "C": "There is no AMC requirement to rebate 50% of soft-dollar credits in cash; the requirement is proper client-benefit usage and transparent disclosure."
                }
            }
        ]
    },
    # =========================================================================
    # V03: Mosaic Theory, Expert Networks & Alternative Data
    # =========================================================================
    {
        "vignette_id": "V03",
        "vignette_title": "Northstar Long/Short Equity: Mosaic Theory and Alternative Data",
        "module": "Module 2: Guidance for Standards I-VII",
        "topic": "Integrity of Capital Markets",
        "subtopic": "Mosaic Theory, MNPI & Expert Networks",
        "vignette_text": (
            "Liam Chen, CFA, is a consumer-sector portfolio manager at Northstar Long/Short Equity, a hedge fund in New York. "
            "To evaluate Apex Apparel Corp. ahead of Q3 earnings, Chen purchases anonymized commercial satellite parking-lot "
            "imagery from a regulated data vendor and combines it with public retail-foot-traffic statistics and scraped "
            "e-commerce pricing data from Apex's public website. He also conducts interviews with three regional cotton "
            "suppliers who mention that Apex recently lengthened invoice payment terms from 30 to 45 days, though none "
            "of the suppliers knows Apex's consolidated revenue or earnings.\n\n"
            "Next, Chen schedules a paid 60-minute call through an expert network firm with Dr. Priya Nair, a former Vice "
            "President of Supply Chain at Apex who left the company four months ago. Before the call, the expert network "
            "confirms that Nair signed an attestation barring disclosure of confidential former-employer information. "
            "During the call, Nair discusses general industry logistics bottlenecks, but when Chen presses for Apex's "
            "unpublished Q3 markdown reserves, Nair says, 'Look, strictly between us, my successor told me last night "
            "over dinner that Q3 gross margins are coming in 400 basis points below Street consensus due to excess inventory.'\n\n"
            "Later that evening, Chen receives an automated alert from Northstar's data-scraping partner, CloudHarvest, "
            "noting that CloudHarvest accidentally gained access to a misconfigured, password-protected Apex internal "
            "staging server containing unannounced store-closure spreadsheets and forwarded a summary table to Chen. "
            "Separately, junior analyst Sarah Kim asks Chen whether she can trade on a widely circulated rumor on a public "
            "retail investor forum claiming Apex is negotiating an acquisition, despite no confirmation from either firm."
        ),
        "questions": [
            {
                "los": "Distinguish permissible mosaic theory analysis from material nonpublic information under Standard II(A).",
                "question": "Chen's integration of satellite imagery, scraped public website pricing, and supplier comments on payment terms before the expert network call represents:",
                "options": {
                    "A": "A permissible application of the mosaic theory under Standard II(A).",
                    "B": "A violation of Standard II(A), because supplier payment-term changes are nonpublic operational data.",
                    "C": "A violation of Standard V(A), because satellite imagery is an unreliable proxy for consolidated revenue."
                },
                "answer": "A",
                "explanation": "Under Standard II(A) Material Nonpublic Information, the mosaic theory permits analysts to combine material public information (public pricing, published traffic stats, observable satellite imagery) with nonmaterial nonpublic information (isolated supplier payment terms) to draw investment conclusions.",
                "distractors": {
                    "B": "Isolated supplier anecdotes regarding payment terms do not constitute material nonpublic inside corporate earnings data; combining them with public data is classic mosaic analysis.",
                    "C": "Using satellite imagery alongside website pricing and channel checks demonstrates thorough multi-source diligence under V(A), not lack of basis."
                }
            },
            {
                "los": "Identify material nonpublic information obtained via an expert network under Standard II(A).",
                "question": "When Dr. Nair reveals Apex's unpublished 400-basis-point Q3 gross margin shortfall based on her successor's comment, what is Chen's primary obligation under Standard II(A)?",
                "options": {
                    "A": "He may trade on the margin data because Nair is no longer an Apex employee and he did not pay her directly.",
                    "B": "He must not trade or cause others to trade on the margin information and must report the receipt of MNPI to Northstar's compliance officer.",
                    "C": "He may trade after 24 hours have elapsed so long as he documents his prior satellite imagery thesis."
                },
                "answer": "B",
                "explanation": "Nair transmitted material nonpublic information originating from a corporate insider (her successor) in breach of confidentiality. Under Standard II(A), Chen is prohibited from trading or tipping others on that MNPI—even if his prior mosaic pointed in a similar direction—and should promptly escalate to compliance to place Apex on the restricted list.",
                "distractors": {
                    "A": "Receiving MNPI from a former executive who obtained it from a current insider still triggers the Standard II(A) prohibition, regardless of payment intermediaries.",
                    "C": "MNPI restrictions remain until the information becomes public or loses materiality, not for an arbitrary 24-hour cooling period; prior research does not sanitize subsequent MNPI taint."
                }
            },
            {
                "los": "Assess legal and ethical risks of unlawfully obtained alternative data under Standards I(A) and II(A).",
                "question": "How should Chen respond to CloudHarvest's summary table derived from Apex's misconfigured password-protected staging server?",
                "options": {
                    "A": "Delete the email after reading it, ignore the data in his model, and execute a short position based solely on his earlier supplier checks.",
                    "B": "Immediately cease reviewing the data, notify compliance to demand CloudHarvest purge the unauthorized data, and refrain from trading on it.",
                    "C": "Use the data because it sat on an accessible server on the internet, rendering it public information."
                },
                "answer": "B",
                "explanation": "Accessing a password-protected staging server containing confidential unannounced store closures is unauthorized intrusion/misappropriation (Standards I(A) and II(A)). Chen must halt review, alert compliance to preserve records and instruct CloudHarvest to purge the illegally sourced data, and refrain from trading.",
                "distractors": {
                    "A": "Once tainted by MNPI and unauthorized internal data, executing a short trade anyway violates Standard II(A); he must restrict trading pending compliance clearance.",
                    "C": "Misconfigured security on a password-protected internal server does not convert confidential internal corporate spreadsheets into public information."
                }
            },
            {
                "los": "Evaluate due diligence requirements when using third-party alternative data vendors under Standard V(A) and I(A).",
                "question": "To prevent future alternative-data breaches, Northstar's compliance policy for onboarding vendors like CloudHarvest should primarily verify:",
                "options": {
                    "A": "That vendors exclusively use free government datasets to eliminate cost.",
                    "B": "Data provenance, web-scraping terms-of-service compliance, and exclusion of personal PII or nonpublic corporate data.",
                    "C": "That the data yields at least a 0.80 correlation with quarterly EPS surprises."
                },
                "answer": "B",
                "explanation": "Under Standards I(A), II(A), III(E), and V(A), diligence on alternative data vendors requires verifying legal provenance, absence of unauthorized scraping/trespass, removal of PII, and safeguards preventing MNPI ingestion.",
                "distractors": {
                    "A": "Paid commercial alternative datasets are widely permissible when legally sourced; cost is not the compliance test.",
                    "C": "Predictive correlation is a quantitative utility test, not an ethical or legal compliance safeguard."
                }
            },
            {
                "los": "Assess trading on unsubstantiated market rumors under Standard II(A) and V(A).",
                "question": "If junior analyst Sarah Kim initiates a position in Apex solely based on the unconfirmed acquisition rumor on the retail forum, she most likely violates:",
                "options": {
                    "A": "Standard V(A) Diligence and Reasonable Basis, because an unconfirmed forum rumor lacks adequate fundamental research support.",
                    "B": "Standard II(A) Material Nonpublic Information, because any takeover rumor posted online is inside information.",
                    "C": "Standard II(B) Market Manipulation, because buying shares on a forum rumor constitutes information-based manipulation."
                },
                "answer": "A",
                "explanation": "A widely circulated unverified public forum rumor is public (not nonpublic under II(A) unless sourced from an insider), and simply buying on a rumor does not manipulate prices under II(B). However, trading solely on an unverified rumor without independent analysis violates Standard V(A) Diligence and Reasonable Basis.",
                "distractors": {
                    "B": "Information posted on an open public retail forum is generally public, though its accuracy is unverified; the primary breach in trading solely on it is V(A).",
                    "C": "Standard II(B) prohibits fabricating or spreading false rumors to distort prices, not merely reading an existing rumor without independent verification."
                }
            },
            {
                "los": "Identify proper expert network screening controls under Standard IV(C).",
                "question": "Which supervisory control by Northstar's compliance team is most effective for preventing MNPI breaches during expert network calls?",
                "options": {
                    "A": "Banning calls with any consultant who has ever worked in the consumer apparel industry.",
                    "B": "Enforcing cooling-off periods for former employees of target companies and logging pre-call topic approvals.",
                    "C": "Allowing analysts to pay consultants directly in cash so Northstar avoids third-party vendor contracts."
                },
                "answer": "B",
                "explanation": "Effective supervisory controls under Standard IV(C) include mandatory cooling-off periods (e.g., 6–12 months) before speaking with former employees of covered issuers, pre-call topic vetting, and compliance chaperone/logging protocols.",
                "distractors": {
                    "A": "A blanket ban on all industry veterans is unnecessarily restrictive and eliminates legitimate mosaic expertise.",
                    "C": "Bypassing vetted expert network contracts with direct cash payments eliminates compliance attestations and audit trails, heightening MNPI and bribery risk."
                }
            }
        ]
    },
    # =========================================================================
    # V04: AI, LLM Governance & Social Media Communications
    # =========================================================================
    {
        "vignette_id": "V04",
        "vignette_title": "Vanguardia Quant Advisors: LLM Governance and Social Media Compliance",
        "module": "Module 2: Guidance for Standards I-VII",
        "topic": "Competence, Diligence, and Modern Communication",
        "subtopic": "AI/LLM Governance & Social Media",
        "vignette_text": (
            "Vanguardia Quant Advisors manages USD 1.8 billion in thematic technology portfolios in London. David Park, CFA, "
            "a senior technology analyst, recently adopted a publicly hosted commercial Large Language Model (LLM) to "
            "accelerate earnings-call synthesis and draft client research memos. To generate a tailored risk-factor memo "
            "for Vanguardia's largest institutional client, the Nordic Sovereign Reserve, Park pastes the Nordic Reserve's "
            "confidential internal portfolio holdings, tax-domicile identifiers, and custom ESG exclusions directly into "
            "the public LLM web interface, which retains user prompts for future model training.\n\n"
            "Later that week, Park asks the LLM to compile a comparative debt-covenant table for three European semiconductor "
            "issuers. Pressed for time before an investment committee vote, Park copies the LLM's output verbatim into his "
            "published client report without checking the primary bond indentures. Two days after distribution, a client "
            "discovers that the LLM fabricated two covenant thresholds and attributed a non-existent regulatory fine to one "
            "issuer. The report carried no disclosure that generative AI produced parts of the analysis.\n\n"
            "Simultaneously, Vanguardia's junior marketing associate, Maya Lopez, a Level II CFA candidate, operates an "
            "automated financial commentary account on a public social media platform under her personal handle 'Maya_AlphaTech.' "
            "Without pre-approval from compliance, Lopez schedules automated AI-generated posts summarizing Vanguardia's "
            "latest semiconductor buy recommendations and stating, 'Our proprietary AI signal predicts 28% upside in ChipCo "
            "over 12 months—a near-certain outperformer with zero downside risk based on backtests.' Lopez uses the handle "
            "to attract private consulting inquiries unrelated to Vanguardia."
        ),
        "questions": [
            {
                "los": "Assess client confidentiality risks when using external public LLMs under Standard III(E).",
                "question": "By pasting the Nordic Sovereign Reserve's confidential holdings, tax identifiers, and custom exclusions into a public LLM that retains prompts for training, Park most directly violated:",
                "options": {
                    "A": "Standard III(E) Preservation of Confidentiality.",
                    "B": "Standard IV(A) Loyalty, because he shared Vanguardia's proprietary ESG filter.",
                    "C": "Standard III(C) Suitability, because the LLM cannot evaluate ESG exclusions."
                },
                "answer": "A",
                "explanation": "Standard III(E) requires members to preserve the confidentiality of client information unless disclosure is required by law, concerns illegal activity, or is authorized by the client. Uploading nonpublic client holdings and tax identifiers to a third-party public AI tool that trains on user prompts breaches client confidentiality.",
                "distractors": {
                    "B": "The primary breach is exposing confidential client data (holdings, tax IDs) to an external third party without client authorization, which falls squarely under Standard III(E).",
                    "C": "Uploading confidential client details to an external model is a confidentiality violation, not an IPS suitability mismatch."
                }
            },
            {
                "los": "Evaluate AI-generated research hallucinations under Standards V(A), I(E), and I(C).",
                "question": "Publishing the LLM-generated covenant table containing fabricated thresholds and a non-existent regulatory fine without verifying primary bond indentures violates:",
                "options": {
                    "A": "Standard II(B) Market Manipulation, because an inaccurate covenant table constitutes price manipulation.",
                    "B": "Standard V(A) Diligence and Reasonable Basis and Standard I(C) Misrepresentation.",
                    "C": "Standard VI(A) Avoid or Disclose Conflicts, because Park failed to disclose Vanguardia's software vendor."
                },
                "answer": "B",
                "explanation": "Relying blindly on unverified LLM outputs violates Standard V(A) Diligence and Reasonable Basis (failing to verify secondary sources and primary indentures) and Standard I(C) Misrepresentation (disseminating false statements of fact regarding covenants and fines). It also implicates Standard I(E) Competence regarding proper AI tool governance.",
                "distractors": {
                    "A": "Negligently publishing AI hallucinations without intent to distort market prices is a diligence and misrepresentation breach, not intentional manipulation under II(B).",
                    "C": "There is no undisclosed financial conflict of interest with the software vendor; the issue is unverified false content and lack of AI disclosure/diligence."
                }
            },
            {
                "los": "Analyze disclosure duties for AI-assisted investment processes under Standard V(B).",
                "question": "If Vanguardia incorporates generative AI models meaningfully into its investment analysis and research workflow, Standard V(B) Communication with Clients and Prospective Clients requires the firm to:",
                "options": {
                    "A": "Disclose the general principles, role, and significant limitations/risks (such as hallucination or model error) of using AI in its process.",
                    "B": "Provide clients with the exact open-source Python weights and full prompt logs for every report.",
                    "C": "Obtain an independent GIPS verification certificate covering its LLM prompt engineering."
                },
                "answer": "A",
                "explanation": "Under Standard V(B), members must disclose the basic format and general principles of the investment processes used to analyze investments and select securities, along with significant risks and limitations (including model and AI limitations).",
                "distractors": {
                    "B": "Standard V(B) requires communicating process principles and risks, not exposing proprietary model code or full prompt transcripts.",
                    "C": "GIPS verification covers firm-wide historical investment performance compliance, not LLM software validation."
                }
            },
            {
                "los": "Evaluate social media performance claims and risk statements under Standards I(C) and V(B).",
                "question": "Lopez's automated social media post claiming ChipCo is a 'near-certain outperformer with zero downside risk based on backtests' violates:",
                "options": {
                    "A": "Standard I(C) Misrepresentation and Standard V(B) Communication with Clients and Prospective Clients.",
                    "B": "Standard VII(B) Reference to CFA Institute, because she posted under 'Maya_AlphaTech.'",
                    "C": "Standard VI(C) Referral Fees, because she seeks consulting inquiries on social media."
                },
                "answer": "A",
                "explanation": "Claiming an equity investment carries 'zero downside risk' and is a 'near-certain outperformer' guarantees uncertain equity outcomes in violation of Standard I(C) Misrepresentation, and fails to distinguish fact from opinion or disclose backtest/model limitations under Standard V(B).",
                "distractors": {
                    "B": "The handle 'Maya_AlphaTech' makes no reference to CFA Institute or the CFA designation, so VII(B) is not triggered by the handle itself.",
                    "C": "Soliciting general consulting inquiries via social media does not constitute undisclosed third-party referral fees under VI(C), though outside consulting would require employer consent under IV(B) and IV(A)."
                }
            },
            {
                "los": "Assess supervisory and record retention duties for employee social media use under Standards IV(C) and V(C).",
                "question": "Which governance failure does Lopez's unapproved social media posting highlight for Vanguardia's compliance leadership?",
                "options": {
                    "A": "Inadequate supervisory policies over external electronic communications under Standard IV(C) and failure to archive investment communications under Standard V(C).",
                    "B": "Breach of Standard III(B) Fair Dealing, because social media posts are accessible to everyone simultaneously.",
                    "C": "Breach of Standard I(B) Independence and Objectivity, because ChipCo may view the post favorably."
                },
                "answer": "A",
                "explanation": "Standard IV(C) requires firms to maintain and enforce compliance policies governing employee social media posts containing investment recommendations, and Standard V(C) requires retaining records of all client and public investment communications.",
                "distractors": {
                    "B": "Simultaneous public posting does not inherently violate III(B) unless clients had not yet received the underlying rating change; the core governance failure is unmonitored, unarchived posts.",
                    "C": "Issuing an overly optimistic post without issuer inducement does not breach independence under I(B)."
                }
            },
            {
                "los": "Apply Standard I(E) Competence to the deployment of AI tools in investment management.",
                "question": "Under Standard I(E) Competence, how does the adoption of LLM tools affect Park's professional obligations?",
                "options": {
                    "A": "Standard I(E) transfers responsibility for factual accuracy to the external AI vendor once a subscription is purchased.",
                    "B": "Park must understand the capabilities and failure modes of AI tools used in his work and retain human accountability for every conclusion.",
                    "C": "Standard I(E) prohibits CFA charterholders from using generative AI for any research drafting task."
                },
                "answer": "B",
                "explanation": "Standard I(E) Competence requires members and candidates to possess and maintain the knowledge and skills necessary for their tools and responsibilities. Using AI requires understanding model risks (hallucinations, stale training cutoffs, data leakage) and maintaining full professional accountability.",
                "distractors": {
                    "A": "Professional accountability cannot be outsourced to software vendors; the analyst remains fully responsible for output accuracy.",
                    "C": "The Standards do not prohibit AI tools; they require competence, diligence, confidentiality protection, and appropriate disclosure."
                }
            }
        ]
    },
    # =========================================================================
    # V05: Supervisory Responsibility & Compliance Escalation
    # =========================================================================
    {
        "vignette_id": "V05",
        "vignette_title": "Sterling Ridge Capital: Supervisory Breakdown and Escalation",
        "module": "Module 2: Guidance for Standards I-VII",
        "topic": "Duties to Employers and Supervisory Controls",
        "subtopic": "Supervisor Compliance Failures & Whistleblowing",
        "vignette_text": (
            "Sterling Ridge Capital is a multi-desk fixed-income boutique in Chicago managing USD 6.5 billion. "
            "Arthur Pendelton, CFA, is Managing Director of Credit Trading and directly supervises eight portfolio "
            "managers and traders, including senior high-yield trader Victor Gomez. Because Pendelton spends most "
            "weeks traveling to market Sterling Ridge's funds, he delegates daily compliance exception review to his "
            "executive assistant, who has no compliance training and simply files alert printouts in a binder without "
            "investigating them.\n\n"
            "Three months ago, compliance software flagged a pattern of late-day personal bond trades executed by Gomez "
            "just minutes before Sterling Ridge entered large block sell orders in the same high-yield issues. When "
            "Sterling Ridge's internal auditor brings the alert log to Pendelton, Pendelton calls Gomez into his office "
            "for an informal chat. Gomez insists the timing was coincidental and promises to 'be much more careful going "
            "forward.' Satisfied with Gomez's verbal assurance, Pendelton takes no further action, does not restrict "
            "Gomez's personal trading permissions, and fails to examine Gomez's historical trade records.\n\n"
            "Two months later, the internal auditor discovers that Gomez resumed front-running client block orders through "
            "an undisclosed brokerage account in his spouse's name, causing an estimated USD 420,000 adverse price impact "
            "to client funds. Pendelton reports the finding to Sterling Ridge's CEO, who refuses to notify affected clients "
            "or regulators, saying, 'We will quietly freeze Victor's bonus and let him resign next quarter so we avoid "
            "a headline scandal.' Horrified by the CEO's cover-up, the firm's Chief Compliance Officer, Naomi Grant, CFA, "
            "considers whether to resign or report the ongoing fraud to securities regulators."
        ),
        "questions": [
            {
                "los": "Distinguish permissible delegation from abdication of supervisory duty under Standard IV(C).",
                "question": "By delegating daily compliance exception review to an untrained executive assistant without oversight, Pendelton:",
                "options": {
                    "A": "Properly mitigated supervisory liability under Standard IV(C) by assigning monitoring tasks to a dedicated staff member.",
                    "B": "Violated Standard IV(C) Responsibilities of Supervisors, because a supervisor may delegate duties only to qualified persons and remains responsible for oversight.",
                    "C": "Violated Standard IV(A) Loyalty, because traveling for marketing distracted him from internal management."
                },
                "answer": "B",
                "explanation": "Under Standard IV(C), supervisors may delegate supervisory tasks, but doing so does not relieve them of supervisory responsibility, and they must ensure delegates are qualified and properly monitored. Assigning compliance exceptions to an untrained assistant who merely files printouts is an abdication of duty.",
                "distractors": {
                    "A": "Delegation never shifts ultimate supervisory accountability, especially when the delegate lacks training and performs no actual review.",
                    "C": "Marketing travel is part of his role; the specific ethical breach is failing to supervise compliance effectively under IV(C)."
                }
            },
            {
                "los": "Evaluate adequate supervisory response once a potential violation is detected under Standard IV(C).",
                "question": "When the internal auditor first alerted Pendelton to Gomez's suspicious late-day trades, Pendelton's informal chat and acceptance of Gomez's verbal promise:",
                "options": {
                    "A": "Satisfied Standard IV(C) because Pendelton addressed the issue promptly and privately.",
                    "B": "Violated Standard IV(C), because detecting a potential violation requires thorough investigation and heightened supervision while restricting activity.",
                    "C": "Violated Standard III(E), because Pendelton should have discussed Gomez's personal trades with all clients immediately."
                },
                "answer": "B",
                "explanation": "Once a supervisor detects or is alerted to a potential violation, simply reprimanding the employee or accepting a promise not to repeat the conduct is insufficient under Standard IV(C). The supervisor must initiate a thorough investigation, review prior trades, restrict trading privileges pending investigation, and increase surveillance.",
                "distractors": {
                    "A": "A private warning and verbal assurance fail to meet the affirmative investigative and remedial standard of IV(C).",
                    "C": "Standard III(E) protects client confidentiality, not employee discipline; premature disclosure prior to verifying facts is not required under III(E)."
                }
            },
            {
                "los": "Identify the underlying trading violations committed by Gomez.",
                "question": "By trading ahead of Sterling Ridge's client block sell orders via an undisclosed account in his spouse's name, Gomez most directly violated:",
                "options": {
                    "A": "Standard VI(B) Priority of Transactions and Standard I(D) Misconduct.",
                    "B": "Standard III(C) Suitability and Standard V(C) Record Retention.",
                    "C": "Standard VI(C) Referral Fees and Standard II(B) Market Manipulation."
                },
                "answer": "A",
                "explanation": "A spouse's account is generally a beneficial-ownership account for the member. Front-running client block orders using an undisclosed spousal account directly violates Standard VI(B) Priority of Transactions (clients must come first) and Standard I(D) Misconduct (deceitful concealment harming clients by USD 420,000).",
                "distractors": {
                    "B": "The violation involves illicit personal front-running and concealment, not unsuitable client recommendations under III(C).",
                    "C": "Front-running is governed by Standard VI(B), not referral fees under VI(C)."
                }
            },
            {
                "los": "Evaluate a supervisor's obligation when senior management blocks remediation under Standards I(A) and IV(C).",
                "question": "Faced with the CEO's refusal to notify affected clients or remedy the USD 420,000 client harm, Chief Compliance Officer Naomi Grant, CFA, must at a minimum:",
                "options": {
                    "A": "Abide by the CEO's decision out of employee loyalty under Standard IV(A) while keeping internal notes.",
                    "B": "Dissociate from the cover-up, escalate to the board/audit committee or regulators as permitted by law, and consider resignation if remediation fails.",
                    "C": "Wait until Gomez leaves next quarter so the firm can quietly recover his bonus without client disruption."
                },
                "answer": "B",
                "explanation": "Under Standards I(A), I(D), III(A), and IV(C), concealing confirmed client fraud violates fiduciary duty and securities law. Grant cannot participate in a cover-up; she must dissociate, escalate to independent governance (board/audit committee), evaluate regulatory reporting obligations under local law, and resign if the firm persists in concealing the violation.",
                "distractors": {
                    "A": "Standard IV(A) loyalty never requires covering up unlawful or unethical harm to clients; Standards I(A) and III(A) supersede silence.",
                    "C": "Delaying action while withholding restitution from harmed clients perpetuates the ethical and legal violation."
                }
            },
            {
                "los": "Determine permissible whistleblowing under Standard IV(A) Loyalty.",
                "question": "If Grant reports the concealed front-running scheme to securities regulators after internal escalation to the CEO fails, her action is:",
                "options": {
                    "A": "A violation of Standard IV(A) Loyalty, because regulatory reporting harms her employer's reputation.",
                    "B": "A violation of Standard III(E) Preservation of Confidentiality, because client trade sizes would be disclosed.",
                    "C": "Permitted under Standard IV(A) Loyalty, because whistleblowing to protect clients and market integrity is not a breach of employer loyalty."
                },
                "answer": "C",
                "explanation": "Standard IV(A) explicitly permits whistleblowing—reporting an employer's unlawful or unethical actions to external regulators—when necessary to protect the integrity of capital markets and the interests of clients, rather than for personal gain.",
                "distractors": {
                    "A": "Duty of loyalty to an employer under IV(A) never shields illegal or client-harming misconduct.",
                    "B": "Standard III(E) explicitly permits disclosures required by law or necessary to address illegal activities."
                }
            },
            {
                "los": "Assess supervisory obligations when compliance resources are systematically denied under Standard IV(C).",
                "question": "According to Standard IV(C) guidance, if a firm refuses to adopt an adequate compliance system after a supervisor repeatedly requests one, the supervisor should:",
                "options": {
                    "A": "Continue managing the desk informally using personal spreadsheets to minimize firm friction.",
                    "B": "Decline in writing to accept supervisory responsibility until the employer adopts reasonable compliance procedures.",
                    "C": "Ask subordinates to self-certify quarterly that they have followed the CFA Code of Ethics."
                },
                "answer": "B",
                "explanation": "Standard IV(C) guidance specifically directs that if a member cannot discharge supervisory responsibilities because of an absence of a compliance system or an inadequate compliance system, the member should decline in writing to accept supervisory responsibility until the employer adopts reasonable procedures.",
                "distractors": {
                    "A": "Informal personal tracking without enforceable firm systems leaves the supervisor exposed to IV(C) liability.",
                    "C": "Employee self-certification alone without surveillance systems and enforcement mechanisms is insufficient under IV(C)."
                }
            }
        ]
    },
    # =========================================================================
    # V06: Front-Running, Priority of Transactions & IPO Allocations
    # =========================================================================
    {
        "vignette_id": "V06",
        "vignette_title": "Harborview Wealth Advisors: Priority of Transactions and IPO Allocations",
        "module": "Module 2: Guidance for Standards I-VII",
        "topic": "Conflicts of Interest and Fair Dealing",
        "subtopic": "Front-Running, Family Accounts & IPO Allocations",
        "vignette_text": (
            "Harborview Wealth Advisors manages USD 2.9 billion across separately managed accounts (SMAs) and two pooled "
            "equity funds. Priya Kapoor, CFA, is a senior portfolio manager who also manages three family-related accounts "
            "held at Harborview: (1) a personal Roth IRA in her own name, (2) a joint brokerage account shared with her "
            "husband, and (3) a fee-paying discretionary account belonging to her retired uncle, Raj Kapoor, who pays "
            "Harborview's standard 1.0% management fee and in which Priya has zero beneficial interest.\n\n"
            "On Tuesday morning, Kapoor decides to upgrade MedCore Labs from 'Hold' to 'Strong Buy' and issues an internal "
            "trade ticket to purchase 150,000 shares across all growth-oriented client SMAs. Before the trading desk "
            "completes execution of the 150,000-share client block, Kapoor receives pre-clearance from Harborview's automated "
            "system—which mistakenly lacked a pending-order check—and purchases 1,500 shares in her joint spousal account. "
            "Later that day, after all non-family client orders are filled, Kapoor enters a buy order for her uncle's "
            "fee-paying account at a price 3.2% higher than the morning fill.\n\n"
            "On Thursday, Harborview is allocated 20,000 shares in a heavily oversubscribed initial public offering (IPO) "
            "of BioPulse Diagnostics, against total client demand of 100,000 shares across 40 eligible growth accounts. "
            "Rather than allocating pro rata, Kapoor allocates 12,000 shares to Harborview's five highest-fee hedge fund "
            "clients, 5,000 shares to the firm's employee pension trust, and 3,000 shares evenly across the remaining 35 "
            "small SMA accounts (leaving several too small to receive a round lot). Kapoor also skips buying BioPulse for "
            "her uncle's eligible growth account until the afternoon secondary market because she worries allocating IPO "
            "shares to a relative might look improper."
        ),
        "questions": [
            {
                "los": "Apply Standard VI(B) Priority of Transactions to joint spousal accounts.",
                "question": "By purchasing 1,500 shares of MedCore Labs in her joint spousal account before the client block order finished executing, Kapoor violated:",
                "options": {
                    "A": "Standard VI(B) Priority of Transactions, regardless of automated pre-clearance.",
                    "B": "Nothing, because automated pre-clearance shifted responsibility to Harborview's compliance system.",
                    "C": "Standard VI(C) Referral Fees, because her spouse shares in the trading upside."
                },
                "answer": "A",
                "explanation": "A joint account shared with a spouse is a beneficial-ownership account under Standard VI(B). Client transactions must have strict priority over beneficial-owner transactions, and an automated system glitch does not excuse a member who knows a 150,000-share client order is still executing.",
                "distractors": {
                    "B": "A member cannot rely on a flawed pre-clearance check to bypass Standard VI(B) when she personally entered the pending client block order.",
                    "C": "Standard VI(C) governs referral fees for client introductions, not personal front-running."
                }
            },
            {
                "los": "Distinguish fee-paying family accounts from beneficial-owner accounts under Standards III(B) and VI(B).",
                "question": "Regarding her uncle Raj Kapoor's fee-paying account, Priya Kapoor's decision to delay his MedCore purchase until after all other clients (resulting in a 3.2% higher fill price) was:",
                "options": {
                    "A": "Required by Standard VI(B), because all relatives' accounts must trade after unrelated clients.",
                    "B": "A violation of Standard III(B) Fair Dealing, because a fee-paying non-beneficial family account must be treated identically to other client accounts.",
                    "C": "A violation of Standard I(B), because managing an uncle's account compromises objectivity."
                },
                "answer": "B",
                "explanation": "Under Standard VI(B) and III(B) guidance, family accounts in which the member has NO beneficial ownership and that pay standard advisory fees are full client accounts. Excluding or delaying them behind other clients unfairly disadvantages the client and violates Standard III(B) Fair Dealing.",
                "distractors": {
                    "A": "Standard VI(B) subordinates beneficial-ownership accounts, NOT fee-paying family accounts where the member has no beneficial interest.",
                    "C": "Managing a relative's account under standard fee terms does not inherently breach I(B) independence."
                }
            },
            {
                "los": "Evaluate oversubscribed IPO allocation to an employee pension trust under Standard VI(B).",
                "question": "Allocating 5,000 shares of the oversubscribed BioPulse IPO to Harborview's employee pension trust while eligible client accounts received truncated allocations violates:",
                "options": {
                    "A": "Standard VI(B) Priority of Transactions, because employer and employee benefit accounts are subordinated to client accounts.",
                    "B": "Standard III(C) Suitability, because IPOs are inappropriate for employee retirement plans.",
                    "C": "Standard IV(B) Additional Compensation, because employees gained IPO profits."
                },
                "answer": "A",
                "explanation": "Under Standard VI(B), both client and employer transactions come ahead of personal accounts, and *client* transactions must always take priority over *employer* proprietary or employee pension accounts in oversubscribed offerings.",
                "distractors": {
                    "B": "Regardless of IPS suitability, the fundamental prohibition is placing an employer/employee account ahead of unmet client demand in a hot IPO.",
                    "C": "Allocating IPO shares internally is not an undisclosed external compensation arrangement under IV(B)."
                }
            },
            {
                "los": "Assess favoritism toward high-fee clients in IPO allocations under Standard III(B).",
                "question": "Allocating 12,000 of the 20,000 BioPulse IPO shares disproportionately to the five highest-fee hedge fund clients while giving 35 smaller suitable SMAs minimal or zero shares violates:",
                "options": {
                    "A": "Standard III(B) Fair Dealing, because oversubscribed IPO shares must be allocated pro rata across all suitable accounts regardless of fee tier.",
                    "B": "Standard VI(A) Avoid or Disclose Conflicts, unless Kapoor discloses on social media that large clients receive priority.",
                    "C": "Standard V(A) Diligence, because hedge funds require larger minimum lot sizes."
                },
                "answer": "A",
                "explanation": "Under Standard III(B) Fair Dealing, oversubscribed new issues must be allocated fairly (typically pro rata based on order size or account value, skipping small lots only under disclosed minimum-lot policies—and filling odd-lot shortages fairly over time), never favoring higher-fee accounts at the expense of smaller suitable clients.",
                "distractors": {
                    "B": "Disclosing unfair allocation practices does not cure a breach of Standard III(B) Fair Dealing in trade and IPO allocation.",
                    "C": "Lot-size rounding rules must still follow an equitable written policy rather than funneling 60% of shares to the five highest-fee accounts."
                }
            },
            {
                "los": "Determine proper handling of small-account minimum lot constraints in oversubscribed IPOs.",
                "question": "If pro-rata allocation of an oversubscribed IPO yields fractional or uneconomically tiny share lots for smaller eligible accounts, the fairest procedure under Standard III(B) is to:",
                "options": {
                    "A": "Exclude all accounts under USD 1 million permanently from every IPO allocation.",
                    "B": "Allocate on a pre-established random lottery or round-lot rotation policy disclosed to clients, or substitute a suitable pooled vehicle.",
                    "C": "Reallocate all small-account IPO shares to Harborview's proprietary trading book."
                },
                "answer": "B",
                "explanation": "When pro-rata distribution produces uneconomical odd lots, Standard III(B) permits using a documented, objective round-lot rotation or random lottery system (or pooled funds) so every suitable account has a fair chance to participate over time.",
                "distractors": {
                    "A": "Permanently excluding smaller accounts from every IPO violates Fair Dealing.",
                    "C": "Diverting client IPO shares to a firm proprietary account violates Standard VI(B) and III(B)."
                }
            },
            {
                "los": "Identify effective firm compliance controls for personal trading under Standards IV(C) and VI(B).",
                "question": "To prevent personal trading breaches like Kapoor's joint-account purchase, Harborview's compliance policy should institute:",
                "options": {
                    "A": "Voluntary quarterly employee honor-system attestations without brokerage feed links.",
                    "B": "Mandatory blackout periods around pending client orders, duplicate trade confirmations, and pre-clearance checks linked to the order management system.",
                    "C": "A rule requiring employees to wait 15 minutes after entering a client order before trading personally."
                },
                "answer": "B",
                "explanation": "Standard VI(B) and IV(C) recommended procedures include automated pre-clearance tied to active/pending OMS orders, strict blackout periods before and after client trades/research releases, and duplicate brokerage confirmations for all employee and beneficial-ownership accounts.",
                "distractors": {
                    "A": "Honor-system attestations without duplicate confirmations fail to detect undisclosed spousal or outside accounts.",
                    "C": "An arbitrary 15-minute delay does not protect clients if a large block order takes hours or days to execute."
                }
            }
        ]
    },
    # =========================================================================
    # V07: Referral Fees & Revenue-Sharing Arrangements
    # =========================================================================
    {
        "vignette_id": "V07",
        "vignette_title": "Sovereign Bridge Consulting: Referral Fees and Revenue Sharing",
        "module": "Module 2: Guidance for Standards I-VII",
        "topic": "Disclosure of Referral Arrangements",
        "subtopic": "Referral Fees & Revenue Sharing",
        "vignette_text": (
            "Sovereign Bridge Consulting is an institutional investment advisory firm advising corporate pension plans "
            "and family offices in Zurich and Frankfurt. Henrik Lindqvist, CFA, is a senior investment consultant who "
            "regularly leads manager-selection searches for clients. During a private credit search for the Alpine "
            "Manufacturing Pension Fund (EUR 400 million mandate), Lindqvist recommends Vertex Private Credit Partners.\n\n"
            "Six months earlier, Sovereign Bridge signed a strategic alliance with Vertex under which Vertex pays "
            "Sovereign Bridge a recurring placement and referral fee equal to 15% of Vertex's annual 1.50% management "
            "fee for any client referred by Sovereign Bridge. When presenting Vertex to Alpine's investment committee, "
            "Lindqvist mentions verbally during Q&A that Sovereign Bridge 'has a commercial relationship with several "
            "credit managers in the industry,' without naming Vertex specifically, stating the 15% fee share, or "
            "providing any written disclosure before Alpine signs Vertex's subscription agreement.\n\n"
            "In a separate arrangement, Lindqvist refers a wealthy private client, the Müller Family Office, to "
            "Sovereign Bridge's internal tax-structuring subsidiary, BridgeTax AG. Sovereign Bridge pays Lindqvist a "
            "standard internal annual bonus based in part on overall cross-departmental firm revenues, though no direct "
            "commission is paid per internal referral. Meanwhile, a boutique real estate fund, TerraCore, offers to "
            "pay for Lindqvist's attendance at a EUR 4,500 executive real estate symposium in London in exchange for "
            "Lindqvist placing TerraCore on Sovereign Bridge's approved-manager shortlist. Lindqvist discloses the "
            "symposium sponsorship to his employer, obtains written supervisor approval, and presents it in writing "
            "to any prospective client to whom he recommends TerraCore prior to signing an agreement."
        ),
        "questions": [
            {
                "los": "Apply Standard VI(C) Referral Fees to third-party manager placement arrangements.",
                "question": "In the Alpine Manufacturing Pension Fund mandate, Lindqvist's vague verbal remark during Q&A violated Standard VI(C) Referral Fees primarily because:",
                "options": {
                    "A": "Referral fees from private credit managers are categorically prohibited for institutional consultants.",
                    "B": "He failed to disclose the existence, nature, and estimated monetary value of the Vertex referral fee before Alpine entered into the formal agreement.",
                    "C": "He should have waited until the first quarterly fee invoice was paid before revealing the fee percentage."
                },
                "answer": "B",
                "explanation": "Under Standard VI(C) Referral Fees, members must disclose to their employer, clients, and prospective clients any compensation, consideration, or benefit received from or paid to others for recommending products or services. The disclosure must occur BEFORE entering into a formal agreement and specify both the nature of the consideration and its estimated dollar value or calculation formula.",
                "distractors": {
                    "A": "Referral fees are permissible under Standard VI(C) provided full, timely, and specific disclosure is made to all affected parties.",
                    "C": "Post-signing disclosure violates Standard VI(C); clients need full conflict information before committing capital."
                }
            },
            {
                "los": "Identify additional standard violations caused by undisclosed third-party referral fees.",
                "question": "Beyond Standard VI(C), recommending Vertex without prominently disclosing the 15% fee-sharing arrangement most directly breaches:",
                "options": {
                    "A": "Standard VI(A) Avoid or Disclose Conflicts and Standard III(A) Loyalty, Prudence, and Care.",
                    "B": "Standard II(A) Material Nonpublic Information and Standard V(C) Record Retention.",
                    "C": "Standard VII(A) Conduct as Participants and Standard IV(B) Additional Compensation."
                },
                "answer": "A",
                "explanation": "Withholding material fee-sharing incentives from a pension client compromises fiduciary loyalty under Standard III(A) and fails to disclose a significant conflict of interest under Standard VI(A), in addition to violating Standard VI(C).",
                "distractors": {
                    "B": "A fee-sharing arrangement between an advisor and a manager is a conflict disclosure issue, not corporate MNPI.",
                    "C": "The fee is paid to the employer Sovereign Bridge rather than an undisclosed external side payment to Lindqvist under IV(B), and VII(A) concerns CFA exams."
                }
            },
            {
                "los": "Distinguish intra-firm cross-selling from third-party referral fees under Standard VI(C).",
                "question": "Regarding Lindqvist's referral of the Müller Family Office to Sovereign Bridge's internal subsidiary, BridgeTax AG, which statement is most accurate?",
                "options": {
                    "A": "Internal referrals within the same corporate group where employees earn a general firm-wide performance bonus do not trigger third-party referral fee violations, though transparent disclosure of affiliated services is good practice.",
                    "B": "Lindqvist must refuse any internal bonus related to BridgeTax AG revenues under Standard IV(B).",
                    "C": "Standard VI(C) requires Lindqvist to compute and disclose his exact year-end salary bonus percentage to the Müller Family Office before their tax meeting."
                },
                "answer": "A",
                "explanation": "Standard VI(C) applies to fees received from or paid to external third parties for referrals; ordinary internal firm compensation and cross-departmental referrals within the same corporate entity generally do not constitute external referral fees, though disclosing the corporate affiliation under Standard VI(A) ensures transparency.",
                "distractors": {
                    "B": "Standard IV(B) covers compensation from parties outside the employer, not internal employer bonuses.",
                    "C": "Standard VI(C) does not require disclosing general internal salary/bonus structures for intra-firm cross-referrals unless a specific commission-like arrangement compromises client objectivity."
                }
            },
            {
                "los": "Evaluate non-monetary benefits as referral consideration under Standards VI(C) and I(B).",
                "question": "With respect to TerraCore paying EUR 4,500 for Lindqvist's London symposium in exchange for placing TerraCore on the shortlist, which statement is most accurate?",
                "options": {
                    "A": "Disclosure to his employer and clients cures the issue entirely because non-cash benefits are exempt from Standard I(B).",
                    "B": "Accepting a EUR 4,500 benefit explicitly conditioned on placing TerraCore on the shortlist impairs independence and objectivity under Standard I(B), even with disclosure.",
                    "C": "The arrangement violates only Standard V(A) because Lindqvist must pay conference travel himself."
                },
                "answer": "B",
                "explanation": "While Standard VI(C) covers non-cash benefits given for recommendations, conditioning manager shortlist placement on receiving a EUR 4,500 paid conference trip compromises objective manager due diligence under Standard I(B) Independence and Objectivity and Standard III(A) Loyalty. Disclosure under VI(C) and employer consent under IV(B) do not make a quid-pro-quo listing ethical.",
                "distractors": {
                    "A": "Non-monetary benefits are NOT exempt from Standard I(B) or VI(C); a quid-pro-quo shortlist exchange compromises objectivity regardless of disclosure.",
                    "C": "The primary breach is compromising manager selection objectivity in exchange for a financial benefit (I(B)/III(A)), not merely conference budget mechanics."
                }
            },
            {
                "los": "Determine required elements of written referral-fee disclosures under Standard VI(C).",
                "question": "To satisfy Standard VI(C) for any permissible external referral arrangement, Sovereign Bridge's written disclosure to prospective clients must state:",
                "options": {
                    "A": "Only that a referral arrangement exists, omitting dollar amounts because pricing is proprietary.",
                    "B": "The nature of the consideration (e.g., cash percentage, flat fee, or soft services) and the estimated dollar value or calculation formula.",
                    "C": "The names and fee rates of all other clients who signed up through the same referral program."
                },
                "answer": "B",
                "explanation": "Standard VI(C) explicitly requires disclosing both the nature of the referral consideration (such as 15% of the annual 1.50% management fee) and the estimated dollar value or exact calculation methodology so the client can evaluate the full cost and bias.",
                "distractors": {
                    "A": "Omitting the magnitude or calculation basis fails Standard VI(C), because clients need to gauge the materiality of the incentive.",
                    "C": "Disclosing other clients' identities and fee structures would breach Standard III(E) Preservation of Confidentiality."
                }
            },
            {
                "los": "Identify the primary purpose of Standard VI(C) Referral Fees.",
                "question": "According to the CFA Institute Standards of Practice Handbook, what is the fundamental rationale behind Standard VI(C)?",
                "options": {
                    "A": "To eliminate all revenue-sharing agreements across global asset management firms.",
                    "B": "To enable clients and employers to evaluate any partiality shown in recommendations and assess the true full cost of services.",
                    "C": "To enforce uniform advisory commission caps across member jurisdictions."
                },
                "answer": "B",
                "explanation": "Standard VI(C) ensures that employers, clients, and prospective clients have complete information to judge whether a recommendation is motivated by self-interest and to assess the full economic cost of the recommended service.",
                "distractors": {
                    "A": "Standard VI(C) permits referral arrangements when properly disclosed rather than outlawing them.",
                    "C": "CFA Institute sets ethical disclosure standards, not regulatory commission fee caps."
                }
            }
        ]
    },
    # =========================================================================
    # V08: Leaving an Employer, Proprietary Models & Client Solicitation
    # =========================================================================
    {
        "vignette_id": "V08",
        "vignette_title": "Canyon Peak Capital: Resignation, Proprietary Models, and Client Solicitation",
        "module": "Module 2: Guidance for Standards I-VII",
        "topic": "Duties to Employers",
        "subtopic": "Leaving an Employer & Client Lists",
        "vignette_text": (
            "Rachel Morales, CFA, has served for seven years as a portfolio manager at Canyon Peak Capital in Denver. "
            "Her employment contract contains no post-employment non-compete covenant, though Canyon Peak's employee "
            "handbook prohibits removing firm documents, client contact lists, or research files upon departure. "
            "Deciding to launch her own registered investment advisor, Summit Ridge Advisors, Morales takes several "
            "preparatory steps during evenings and weekends using her personal laptop: she incorporates Summit Ridge, "
            "leases office space, and establishes custodial brokerage agreements, without telling Canyon Peak yet.\n\n"
            "Two weeks before submitting her resignation, Morales exports a spreadsheet from Canyon Peak's CRM containing "
            "the names, private phone numbers, and portfolio tax bases of her 35 top clients, along with the automated "
            "Python valuation model she personally coded during work hours over the past three years. Before leaving "
            "the office on her penultimate day, she emails ten of those clients from her personal email account announcing "
            "her upcoming launch and inviting them to transfer their accounts to Summit Ridge once she exits.\n\n"
            "After her employment officially ends, Morales realizes she should not use the exported spreadsheet, so she "
            "deletes it without importing it, reconstructs a new valuation script from memory using general financial "
            "principles, and looks up the names of several former clients on public LinkedIn profiles and state business "
            "registries to invite them to an introductory meeting at Summit Ridge. Meanwhile, her former junior associate "
            "at Canyon Peak, who did not resign, secretly forwards Morales a newly updated Canyon Peak macroeconomic "
            "strategy slide deck out of friendship."
        ),
        "questions": [
            {
                "los": "Distinguish permissible resignation preparations from disloyal conduct under Standard IV(A).",
                "question": "Incorporating Summit Ridge Advisors, leasing office space, and arranging custodial agreements on weekends using her personal laptop before resigning was:",
                "options": {
                    "A": "A violation of Standard IV(A) Loyalty, because employees must notify their employer before registering any competing entity.",
                    "B": "Permissible under Standard IV(A) Loyalty, because preparations on personal time that do not compete or use employer resources do not harm the employer.",
                    "C": "A violation of Standard VI(A), because she failed to disclose the new firm to her Canyon Peak clients while still employed."
                },
                "answer": "B",
                "explanation": "Under Standard IV(A) Loyalty, departing employees may make preparations to establish a new firm (incorporating, leasing space, arranging custodial accounts) on their own time and with personal resources, provided they do not solicit clients, divert business, or use employer assets prior to termination.",
                "distractors": {
                    "A": "Preparatory administrative steps conducted off-hours without soliciting clients or competing do not violate IV(A).",
                    "C": "Disclosing an unannounced future competing venture to clients while still employed could itself become improper pre-departure solicitation."
                }
            },
            {
                "los": "Apply Standard IV(A) and Standard V(C) to taking self-built models and client records upon departure.",
                "question": "Exporting the CRM client spreadsheet and the Python valuation model she personally coded during work hours at Canyon Peak violated:",
                "options": {
                    "A": "Standard IV(A) Loyalty only regarding the CRM spreadsheet, because she owns the Python model she authored.",
                    "B": "Standard IV(A) Loyalty regarding both items, because work product and client records created during employment belong to the employer.",
                    "C": "Nothing, because she deleted the CRM spreadsheet after her departure without importing it."
                },
                "answer": "B",
                "explanation": "Under Standards IV(A) and V(C), all records, models, research files, and client contact databases created or maintained during employment are the property of the employer—even if the departing employee personally wrote the code or built the client relationships. Taking them without express permission violates Standard IV(A) (and III(E) regarding client tax/contact records).",
                "distractors": {
                    "A": "Code and valuation models developed during employment using firm resources belong to the employer unless a written agreement states otherwise.",
                    "C": "Unauthorized removal of confidential client data and firm property is a violation when taken, even if later deleted; furthermore, she did not delete the stolen Python model."
                }
            },
            {
                "los": "Evaluate pre-resignation client solicitation under Standard IV(A).",
                "question": "Emailing ten Canyon Peak clients from her personal email on her penultimate day of employment to invite them to transfer accounts to Summit Ridge violated:",
                "options": {
                    "A": "Standard IV(A) Loyalty, because soliciting an employer's clients while still employed is prohibited.",
                    "B": "Standard VII(B), because she used a personal email domain.",
                    "C": "Standard I(B) Independence and Objectivity, because offering to manage their money compromises advice."
                },
                "answer": "A",
                "explanation": "Standard IV(A) requires employees to remain loyal until employment officially terminates. Soliciting the employer's clients to follow the employee to a new venture before the final day of employment directly harms the employer and violates Standard IV(A).",
                "distractors": {
                    "B": "Standard VII(B) governs references to CFA Institute and the CFA designation, not personal email domains.",
                    "C": "Pre-departure client solicitation is an employer-loyalty offense (IV(A)), not an objectivity breach (I(B))."
                }
            },
            {
                "los": "Assess post-departure use of memory and public directories under Standard IV(A).",
                "question": "After her employment ends (and in the absence of any non-compete covenant), reconstructing a valuation script from general knowledge and contacting former clients found via LinkedIn and public registries is:",
                "options": {
                    "A": "A violation of Standard IV(A), because CFA charterholders may never contact former clients after leaving a firm.",
                    "B": "Permissible under Standard IV(A), because she is no longer employed by Canyon Peak and used public sources and her own skills rather than stolen firm property.",
                    "C": "A violation of Standard I(C) Misrepresentation, because recreating a model from memory equals copying Canyon Peak's script."
                },
                "answer": "B",
                "explanation": "Once employment terminates—and assuming no binding legal non-compete or non-solicitation agreement prohibits it under Standard I(A)—a former employee may compete freely, use skills and general knowledge retained in memory, and contact former clients using public directories or memory without breaching Standard IV(A).",
                "distractors": {
                    "A": "Standard IV(A) duty of loyalty to a former employer does not impose a perpetual ban on competing or contacting former clients post-departure absent legal restrictions.",
                    "C": "Rebuilding a model from general financial principles and memory is permissible and does not constitute plagiarism or misrepresentation."
                }
            },
            {
                "los": "Evaluate receiving confidential materials from a former colleague post-departure.",
                "question": "When her former junior associate secretly forwards Canyon Peak's newly updated macroeconomic strategy slide deck after Morales leaves, Morales should:",
                "options": {
                    "A": "Incorporate the macro projections into Summit Ridge's client newsletters without citing Canyon Peak.",
                    "B": "Delete the file without using it and notify the associate not to send confidential Canyon Peak materials.",
                    "C": "Keep the file as benchmark reference only, since she did not solicit the associate to send it."
                },
                "answer": "B",
                "explanation": "Accepting and using proprietary research stolen from a former employer by a current employee breaches ethical standards (Standards IV(A), I(A), and I(D) misconduct/misappropriation). Even though unsolicited, Morales must refuse to use it, delete it, and instruct the associate to stop.",
                "distractors": {
                    "A": "Using another firm's proprietary presentation without permission compounds misappropriation with plagiarism (Standard I(C)).",
                    "C": "Retaining unauthorized proprietary research from a competitor still compromises integrity even if unsolicited."
                }
            },
            {
                "los": "Determine the interplay between local non-compete contracts and Standard I(A).",
                "question": "If Morales's employment contract had contained a legally enforceable 12-month non-solicitation clause under Colorado law, contacting former clients via LinkedIn two weeks after leaving would violate:",
                "options": {
                    "A": "Standard I(A) Knowledge of the Law and Standard I(D) Misconduct, in addition to potential contractual liability.",
                    "B": "Standard III(E) Preservation of Confidentiality only.",
                    "C": "Nothing in the Code and Standards, because CFA Institute rules supersede employment contracts."
                },
                "answer": "A",
                "explanation": "Under Standard I(A) and Standard IV(A) guidance, members must abide by all valid legal and contractual obligations, including enforceable non-compete or non-solicitation agreements. Deliberately breaching a valid legal obligation violates Standard I(A) (and I(D) if deceptive).",
                "distractors": {
                    "B": "While using stolen lists violates III(E), looking up names on LinkedIn violates an enforceable non-solicitation contract under I(A), not confidentiality.",
                    "C": "The Code and Standards require obeying applicable laws and valid contracts (Standard I(A)); they never authorize breaching enforceable legal restrictions."
                }
            }
        ]
    },
    # =========================================================================
    # V09: GIPS Composite Construction & Fee Policies
    # =========================================================================
    {
        "vignette_id": "V09",
        "vignette_title": "Boreal Global Investments: GIPS Composite Construction and Return Policies",
        "module": "Module 4: Global Investment Performance Standards (GIPS)",
        "topic": "GIPS Compliance and Composite Management",
        "subtopic": "Composite Construction & Fee Policies",
        "vignette_text": (
            "Boreal Global Investments is an institutional asset manager in Montreal preparing to claim compliance with "
            "the Global Investment Performance Standards (GIPS) for the first time across its operations. Boreal "
            "manages 24 segregated equity accounts and one non-discretionary advisory account for a religious foundation "
            "that requires pre-approval on every single trade. Boreal's head of performance, Celine Tremblay, CFA, "
            "defines the firm broadly as 'Boreal Global Investments, excluding its newly acquired Canadian Small-Cap "
            "division, which will adopt GIPS next year.'\n\n"
            "For Boreal's flagship North American Core Equity Composite, Tremblay sets a written minimum asset threshold "
            "of USD 2 million to avoid managing administrative noise from tiny accounts. Two portfolios fall below "
            "USD 2 million solely due to market depreciation in Q2, and Tremblay immediately removes them from the "
            "composite for Q2 while keeping them out when they recover above USD 2 million in Q4. Meanwhile, a new "
            "discretionary USD 10 million account is funded on 12 January; Tremblay includes it in the composite "
            "starting 1 February (the first full month under management) per firm policy. For the non-discretionary "
            "religious foundation account, Tremblay excludes it from both the Core Equity Composite and Total Firm Assets.\n\n"
            "Finally, Boreal also markets a Balanced Growth Carve-Out taken from multi-asset accounts by extracting "
            "only the equity portion of balanced mandates for periods beginning in 2021. Because cash is held centrally "
            "at the total-portfolio level, Boreal assigns zero cash to the equity carve-out and calculates carve-out "
            "returns solely on invested equities. For composite fee reporting, Boreal presents gross-of-fees returns "
            "alongside a model management fee schedule, without showing net-of-fees returns, for institutional clients."
        ),
        "questions": [
            {
                "los": "Evaluate firm definition and firm-wide compliance requirements under GIPS.",
                "question": "Tremblay's decision to define the firm as excluding its Canadian Small-Cap division while claiming GIPS compliance for Boreal Global Investments is:",
                "options": {
                    "A": "Permissible during a 12-month onboarding grace period for acquired divisions.",
                    "B": "A violation of GIPS, because GIPS compliance must be achieved on a firm-wide basis across the distinctly defined business entity.",
                    "C": "Permissible provided the Canadian Small-Cap division has fewer than five portfolios."
                },
                "answer": "B",
                "explanation": "GIPS compliance is strictly firm-wide; a firm cannot claim partial GIPS compliance or exclude an internal investment division that is held out to the public under the same distinct firm brand unless it meets the definition of a separate distinct business entity.",
                "distractors": {
                    "A": "GIPS does not grant a selective exclusion grace period for an integrated division when claiming firm-wide compliance.",
                    "C": "Composite portfolio counts affect dispersion reporting (<= 5 portfolios), not the firm-wide compliance scope."
                }
            },
            {
                "los": "Apply GIPS rules for non-discretionary portfolios in composites vs. total firm assets.",
                "question": "How did Tremblay handle the non-discretionary religious foundation account relative to GIPS requirements?",
                "options": {
                    "A": "Correctly excluded it from the composite AND correctly excluded it from Total Firm Assets.",
                    "B": "Correctly excluded it from the composite, but erred by excluding it from Total Firm Assets.",
                    "C": "Erred by excluding it from the composite, because all fee-paying accounts must enter a composite."
                },
                "answer": "B",
                "explanation": "Under GIPS, non-discretionary portfolios MUST be excluded from composites (because the firm does not control investment decisions), but Total Firm Assets MUST include all discretionary and non-discretionary assets managed by the firm (excluding only advisory-only assets if not managed or simulated/model assets).",
                "distractors": {
                    "A": "Total Firm Assets must include both discretionary and non-discretionary fee-paying and non-fee-paying assets under management.",
                    "C": "Composites include only actual, fee-paying, *discretionary* portfolios; non-discretionary accounts are barred from composites."
                }
            },
            {
                "los": "Assess minimum asset level rules for composite inclusion and exclusion under GIPS.",
                "question": "Removing two portfolios from the Core Equity Composite in Q2 when market depreciation dropped them below the USD 2 million threshold was:",
                "options": {
                    "A": "Appropriate, because portfolios below the stated composite minimum must be removed immediately regardless of cause.",
                    "B": "Improper if not applied consistently per documented policy, and excluding portfolios solely because market depreciation caused them to fall below minimum distorts historical returns unless the documented policy specifies consistent removal/re-entry criteria applied across all accounts.",
                    "C": "Required only for terminated accounts, not active accounts."
                },
                "answer": "B",
                "explanation": "Under GIPS, if a firm sets a composite minimum asset size, it must document and apply removal and re-entry rules *consistently*—removing accounts that drop below minimum only at defined periods or not selectively keeping out recovering accounts (and never cherry-picking removals during downturns while failing to re-include them upon recovery in Q4).",
                "distractors": {
                    "A": "Selectively removing accounts during Q2 depreciation and failing to re-add them when they recover above USD 2 million in Q4 violates consistent composite policy application.",
                    "C": "Active portfolios can be removed for falling below minimums only under strict, consistently applied documented policies."
                }
            },
            {
                "los": "Evaluate new-portfolio inclusion timing under GIPS.",
                "question": "Including the new USD 10 million account funded on 12 January in the Core Equity Composite starting 1 February is:",
                "options": {
                    "A": "Compliant with GIPS, provided Boreal applies its documented new-account inclusion policy consistently across all accounts.",
                    "B": "A violation of GIPS, because new accounts must enter the composite on the exact funding date of 12 January.",
                    "C": "A violation of GIPS, because new accounts must wait at least one full calendar quarter before inclusion."
                },
                "answer": "A",
                "explanation": "Under GIPS, new portfolios must be included in a composite on a timely and consistent basis after coming under management—typically at the start of the next full performance measurement period (such as the first full month, 1 February) following funding.",
                "distractors": {
                    "B": "Mid-month funding does not force exact-day inclusion unless specified in firm policy; next full month is standard.",
                    "C": "Waiting a full calendar quarter would violate the GIPS timely-inclusion requirement."
                }
            },
            {
                "los": "Apply GIPS 2020 carve-out rules regarding cash allocation.",
                "question": "For periods beginning in 2021, presenting the Balanced Growth equity carve-out without allocating any cash to the carve-out:",
                "options": {
                    "A": "Complies with GIPS 2020, because zero-cash carve-outs isolate pure equity selection alpha.",
                    "B": "Violates GIPS, because carve-out returns included in a composite must include cash and any related income, whether accounted for separately or allocated synthetically on a timely and consistent basis.",
                    "C": "Complies with GIPS provided Boreal labels the carve-out as supplemental information only."
                },
                "answer": "B",
                "explanation": "Under GIPS 2020, carve-outs included in composites MUST include cash (either held in a dedicated sub-account or synthetically allocated using a documented, consistent methodology). Presenting zero-cash equity carve-outs as composite performance violates GIPS (and since Jan 1, 2010–2019 carve-outs required separate cash, GIPS 2020 reinstated synthetic cash allocation with mandatory cash inclusion and clear disclosure).",
                "distractors": {
                    "A": "Zero-cash carve-outs overstate or distort total-return volatility and cannot represent standalone composite performance under GIPS.",
                    "C": "Tremblay is marketing it as a composite strategy rather than clearly separated supplemental info, and cashless carve-outs cannot be included in GIPS-compliant composites."
                }
            },
            {
                "los": "Evaluate gross-of-fees vs. net-of-fees presentation requirements under GIPS 2020.",
                "question": "In presenting GIPS Reports to prospective institutional clients with only gross-of-fees returns and a model fee schedule, Boreal:",
                "options": {
                    "A": "Complies with GIPS 2020, because institutional GIPS Reports only require gross-of-fees returns alongside the fee schedule.",
                    "B": "Violates GIPS 2020, because every GIPS Report must show net-of-fees returns exclusively and prohibit gross returns.",
                    "C": "Violates Standard III(D) only if actual fees exceed 2%."
                },
                "answer": "A",
                "explanation": "Under GIPS 2020 (Provisions 4.A.1 and 4.A.4), firms must present EITHER gross-of-fees OR net-of-fees returns in a GIPS Composite Report (or both), and must disclose the fee schedule appropriate for prospective clients. Presenting gross-of-fees returns plus the fee schedule complies with GIPS (whereas GIPS advertisements or specific pooled-fund/retail rules may require net returns depending on context).",
                "distractors": {
                    "B": "GIPS 2020 allows presenting gross-of-fees, net-of-fees, or both in a Composite Report, provided fees are clearly disclosed and the fee schedule is shown.",
                    "C": "There is no 2% threshold governing GIPS fee-presentation rules."
                }
            }
        ]
    },
    # =========================================================================
    # V10: GIPS Portability, Verification & Advertising Guidelines
    # =========================================================================
    {
        "vignette_id": "V10",
        "vignette_title": "Oakridge Capital Partners: GIPS Portability, Verification, and Advertising",
        "module": "Module 4: Global Investment Performance Standards (GIPS)",
        "topic": "GIPS Portability, Verification, and Marketing",
        "subtopic": "Portability, Verification & Advertising",
        "vignette_text": (
            "Oakridge Capital Partners, a GIPS-compliant firm in Boston, acquires the entire three-person European Value "
            "team from bankrupt rival Helios Asset Management on 1 March 2025. All three investment decision-makers "
            "join Oakridge immediately, and Oakridge brings over the complete historical custodial statements, daily "
            "valuation records, and client account ledgers supporting the team's 8-year European Value Composite track "
            "record at Helios through 28 February 2025. The team continues applying the exact same bottom-up valuation "
            "process independently at Oakridge starting 1 March 2025, with zero gap in performance history.\n\n"
            "Simultaneously, Oakridge launches a marketing campaign in institutional trade magazines. One full-page "
            "advertisement presents Oakridge's 5-year annualized return for its US Mid-Cap Growth Composite alongside "
            "a footnote stating: 'Oakridge's US Mid-Cap Growth Composite has been independently verified for the period "
            "2020–2024 by Apex Audit LLP. Oakridge claims compliance with GIPS.' The advertisement omits 1-year and "
            "10-year annualized returns (even though the composite has a 12-year history), omits the benchmark's 5-year "
            "return, and fails to state whether returns are gross or net of fees.\n\n"
            "Two months later, during an internal audit, Oakridge's performance analyst discovers a pricing error in the "
            "2023 return of the US Mid-Cap Growth Composite that overstated the annual return by 1.40% (140 bps), "
            "exceeding Oakridge's written 50 bps materiality threshold. Oakridge corrects the GIPS Report immediately, "
            "includes an error-correction disclosure in the updated report, and distributes the corrected GIPS Report "
            "to all current and prospective clients who received the erroneous version."
        ),
        "questions": [
            {
                "los": "Apply GIPS portability requirements for linking historical track records from a prior firm.",
                "question": "May Oakridge link the Helios European Value team's 8-year historical track record (through 28 Feb 2025) to Oakridge's ongoing European Value Composite starting 1 Mar 2025?",
                "options": {
                    "A": "No, because performance from a bankrupt firm cannot be ported under GIPS.",
                    "B": "Yes, because substantially all decision-makers joined Oakridge, the decision process remains intact, complete supporting records exist, and there is no break in track record.",
                    "C": "Only if at least 75% of Helios's former clients transfer their assets to Oakridge."
                },
                "answer": "B",
                "explanation": "Under GIPS portability provisions, performance from a past firm MUST/MAY be linked to ongoing performance at the new firm when all portability tests are met: (1) substantially all investment decision-makers are employed by the new firm, (2) the decision-making process remains substantially intact and independent, (3) supporting records exist to document the performance, and (4) there is no break in the track record.",
                "distractors": {
                    "A": "Bankruptcy or acquisition of the prior employer does not bar portability so long as supporting records are intact and the three substantive criteria plus continuity are met.",
                    "C": "Client asset transfer is not a mandatory GIPS portability prerequisite; decision-maker continuity, process integrity, and records are."
                }
            },
            {
                "los": "Identify what happens under GIPS if there is a break in track record during a team lift-out.",
                "question": "If there had been a four-month break between leaving Helios and resuming strategy management at Oakridge, how would GIPS treat the 8-year Helios track record?",
                "options": {
                    "A": "Oakridge could link the two periods seamlessly by assuming cash returns during the four-month gap.",
                    "B": "Oakridge could still port and present the Helios historical record if all three substantive tests hold, provided there is no linking across the break.",
                    "C": "Oakridge could drop the Helios track record entirely and delete it from all files."
                },
                "answer": "B",
                "explanation": "Under GIPS 2020 portability rules, if there is a break in the track record between the prior firm and the acquiring firm, the prior track record may still be presented alongside new performance (if the three substantive tests—decision-makers, process, and records—are satisfied), but the periods MUST NOT be linked across the break.",
                "distractors": {
                    "A": "Synthesizing hypothetical cash returns to bridge a multi-month performance gap and link records violates GIPS.",
                    "C": "A break does not prevent showing the unlinked prior track record separately with full disclosure."
                }
            },
            {
                "los": "Assess GIPS verification scope and prohibited verification wording.",
                "question": "The statement in Oakridge's advertisement that 'Oakridge's US Mid-Cap Growth Composite has been independently verified' violates GIPS because:",
                "options": {
                    "A": "GIPS verification is conducted on a firm-wide basis, never on a single specific composite.",
                    "B": "Verification must be performed by CFA Institute rather than an accounting firm like Apex Audit LLP.",
                    "C": "Firms are barred from mentioning verification in any external advertisement."
                },
                "answer": "A",
                "explanation": "Under GIPS, verification applies strictly to the *entire firm* (assessing firm-wide compliance policies and composite construction procedures), never to an individual composite. Claiming a specific composite is verified is misleading and violates GIPS (and Standard I(C) Misrepresentation). Note: a separate *performance examination* can be performed on a specific composite, but only after firm-wide verification, and must not be mislabeled as composite verification.",
                "distractors": {
                    "B": "Verification is performed by qualified independent third-party verifiers (such as audit or GIPS verification firms), not by CFA Institute.",
                    "C": "Firms are permitted to state they have been verified on a firm-wide basis in GIPS Reports and compliant advertisements."
                }
            },
            {
                "los": "Apply GIPS Advertising Guidelines requirements to marketing materials.",
                "question": "In addition to the improper verification phrasing, Oakridge's magazine advertisement violated the GIPS Advertising Guidelines by:",
                "options": {
                    "A": "Failing to include 1-, 5-, and 10-year (or since-inception) annualized returns, benchmark returns, and whether returns are gross or net of fees.",
                    "B": "Including a 5-year annualized return instead of quarterly cumulative returns.",
                    "C": "Publishing a GIPS-compliant advertisement in a print magazine rather than an electronic PDF."
                },
                "answer": "A",
                "explanation": "Under the GIPS Advertising Guidelines, any advertisement claiming GIPS compliance and showing performance must include specific required elements: standardized 1-, 5-, and 10-year annualized returns (or since inception if shorter), equivalent benchmark returns, clear indication of gross-of-fees or net-of-fees, currency, and the official GIPS Advertising Guidelines compliance statement.",
                "distractors": {
                    "B": "Annualized multi-year returns (1-, 5-, and 10-year) are specifically required rather than quarterly cumulative snapshots.",
                    "C": "Print magazines, websites, and PDFs are all valid media under the GIPS Advertising Guidelines."
                }
            },
            {
                "los": "Evaluate material error correction procedures under GIPS.",
                "question": "Regarding Oakridge's handling of the 140 bps pricing error in the 2023 US Mid-Cap Growth Composite return, Oakridge's response:",
                "options": {
                    "A": "Violated GIPS, because Oakridge failed to report the error to CFA Institute within 10 business days.",
                    "B": "Complied with GIPS Error Correction policies, because the material error was corrected, disclosed in the revised report, and distributed to current and prospective recipients.",
                    "C": "Violated GIPS, because historical GIPS Reports may never be restated retroactively once distributed."
                },
                "answer": "B",
                "explanation": "When a material error (above the firm's pre-established error-correction threshold) is discovered in a GIPS Report, GIPS requires correcting the report, adding a clear error disclosure explaining the change, and making every reasonable effort to provide the corrected report to all current clients, prospective clients, and verifiers who received the erroneous report.",
                "distractors": {
                    "A": "GIPS requires notifying verifiers and recipients of the erroneous report, not filing error notifications directly with CFA Institute.",
                    "C": "GIPS explicitly requires restating and disclosing material errors retroactively rather than leaving incorrect figures in circulation."
                }
            },
            {
                "los": "Identify the proper official GIPS compliance statement format.",
                "question": "To comply with GIPS, the official GIPS compliance statement in Oakridge's full GIPS Composite Report must specify:",
                "options": {
                    "A": "Only that 'Oakridge claims compliance with GIPS' in bold text.",
                    "B": "The exact prescribed GIPS compliance wording naming the firm, stating whether the firm has been independently verified and for what periods, and noting that verification does not ensure accuracy of any specific composite report.",
                    "C": "That CFA Institute endorses Oakridge's investment performance calculations."
                },
                "answer": "B",
                "explanation": "GIPS mandates verbatim or prescribed claim-of-compliance wording defining the firm, stating compliance with GIPS, confirming whether the firm is verified (and periods covered), and clarifying that verification assesses firm-wide policies rather than certifying the accuracy of any single composite report.",
                "distractors": {
                    "A": "Truncating the compliance statement to a single summary sentence omits mandatory verification and firm-definition disclaimers.",
                    "C": "CFA Institute never endorses or guarantees any firm's investment performance under GIPS or Standard VII(B)."
                }
            }
        ]
    }
]

VIGNETTES.extend([
    # =========================================================================
    # V11: Asset Manager Code: Loyalty, Trading & Risk/Compliance
    # =========================================================================
    {
        "vignette_id": "V11",
        "vignette_title": "Kestrel Institutional Partners: Asset Manager Code Governance and Trading",
        "module": "Module 5: Asset Manager Code of Professional Conduct",
        "topic": "Asset Manager Code Principles and Functional Areas",
        "subtopic": "Loyalty, Trading, Valuation & Compliance",
        "vignette_text": (
            "Kestrel Institutional Partners manages EUR 3.4 billion across European corporate credit funds and claims "
            "compliance with the CFA Institute Asset Manager Code of Professional Conduct (AMC). Kestrel's Chief "
            "Compliance Officer (CCO), Ingrid Bauer, reports directly to the Head of Sales and lacks independent "
            "access to Kestrel's Board of Directors or Audit Committee. Furthermore, Kestrel has not updated or "
            "tested its business continuity and disaster recovery plan in four years following a core cloud migration.\n\n"
            "During a volatile Tuesday trading session, Kestrel's head trader accidentally enters a buy order for "
            "EUR 12 million instead of EUR 1.2 million of an illiquid high-yield bond for the Euro Income Fund. "
            "Before the trader can cancel the excess EUR 10.8 million fill, prices drop 2.5%, creating an immediate "
            "EUR 270,000 loss. Rather than absorbing the loss with Kestrel's own firm capital, Bauer and the trading "
            "desk decide to cover the error by reallocating half of the excess bonds into Kestrel's larger Global "
            "Opportunities Fund (whose clients did not need the bond) and instructing a preferred broker to absorb "
            "the remaining loss in exchange for future high-commission trades from Euro Income Fund.\n\n"
            "At month-end, Kestrel holds a EUR 45 million distressed private loan whose external pricing service quotes "
            "74 cents on the euro. Believing the external mark reflects temporary market illiquidity, Kestrel's "
            "portfolio manager overrides the vendor mark internally to 88 cents on the euro without documented "
            "board/valuation-committee approval or disclosure in the fund's quarterly client report, noting that "
            "Kestrel's fee schedule is disclosed on its website."
        ),
        "questions": [
            {
                "los": "Apply Asset Manager Code Section D (Risk Management, Compliance, and Support) to CCO reporting independence.",
                "question": "CCO Ingrid Bauer reporting solely to the Head of Sales without direct access to Kestrel's Board or Audit Committee violates which AMC principle?",
                "options": {
                    "A": "AMC Section D (Risk Management, Compliance, and Support), which requires an independent compliance officer with direct access to senior leadership and the board.",
                    "B": "AMC Section B (Investment Process), because the Head of Sales should not approve bond durations.",
                    "C": "AMC Section C (Trading), because sales executives must sign off on best-execution reports."
                },
                "answer": "A",
                "explanation": "Under Asset Manager Code Section D (Risk Management, Compliance, and Support), managers must appoint a qualified compliance officer with sufficient authority, independence, and direct access to senior management and the governing board, insulated from commercial revenue pressures such as sales.",
                "distractors": {
                    "B": "CCO structural independence is governed by Section D (Risk Management, Compliance, and Support), not Section B (Investment Process).",
                    "C": "Section C governs trading integrity and allocation, whereas compliance governance structure falls under Section D."
                }
            },
            {
                "los": "Evaluate business continuity and disaster recovery obligations under AMC Section D.",
                "question": "Failing to update or test its business continuity plan for four years following a cloud migration causes Kestrel to violate:",
                "options": {
                    "A": "AMC Section D (Risk Management, Compliance, and Support), which requires maintaining and periodically testing a current business continuity plan.",
                    "B": "AMC Section A (Loyalty to Clients), because clients must host backup servers.",
                    "C": "AMC Section E (Performance and Valuation), because cloud outages affect net asset value timing."
                },
                "answer": "A",
                "explanation": "AMC Section D explicitly requires investment managers to establish, maintain, and periodically test a business continuity plan appropriate to the firm's size and operational complexity—especially after material infrastructure changes.",
                "distractors": {
                    "B": "Operational resilience and continuity planning are firm obligations under Section D, not client infrastructure duties.",
                    "C": "The direct compliance failure of an outdated, untested continuity plan falls under Section D Risk Management and Support."
                }
            },
            {
                "los": "Apply AMC Section C (Trading) to trade error resolution.",
                "question": "Handling the EUR 270,000 trade error by shifting excess bonds into an unrelated fund and compensating a broker with future client commissions violates:",
                "options": {
                    "A": "AMC Section C (Trading) and Section A (Loyalty to Clients), because trade errors caused by the firm must be resolved using firm capital without harming any client.",
                    "B": "AMC Section F (Disclosures) only, provided the error is mentioned in the next annual Form ADV.",
                    "C": "Nothing, provided the Global Opportunities Fund had excess cash available."
                },
                "answer": "A",
                "explanation": "Under AMC Section C (Trading) and Standard III(A)/III(B), clients must be made whole from manager-caused trade errors using firm capital. Shifting unwanted losing positions onto another client fund or using future client brokerage commissions to reimburse a broker violates both Section C and Section A.",
                "distractors": {
                    "B": "Disclosure does not cure misappropriating client funds or shifting firm losses onto unaffected clients.",
                    "C": "Having excess cash does not justify dumping an erroneous losing position onto a fund that had no investment rationale for buying it."
                }
            },
            {
                "los": "Evaluate fair valuation overrides for illiquid assets under AMC Section E (Performance and Valuation).",
                "question": "Unilaterally overriding an independent external mark from 74 to 88 on the private loan without valuation-committee governance or disclosure violates:",
                "options": {
                    "A": "AMC Section E (Performance and Valuation), which requires fair, objective valuations using independent pricing sources where possible and transparent fair-value policies.",
                    "B": "AMC Section C (Trading), because distressed loans must trade on public exchanges.",
                    "C": "GIPS Advertising Guidelines, because vendor prices must match historical cost."
                },
                "answer": "A",
                "explanation": "AMC Section E mandates that managers value client assets fairly and accurately using independent third-party pricing sources whenever available, and apply documented, unbiased fair-value policies overseen independently when overrides occur.",
                "distractors": {
                    "B": "Distressed private loans frequently trade over the counter; the breach is the arbitrary, undocumented valuation override under Section E.",
                    "C": "GIPS requires fair value rather than historical cost, and this scenario concerns portfolio NAV valuation under AMC Section E."
                }
            },
            {
                "los": "Identify fee and cost transparency duties under AMC Section F (Disclosures).",
                "question": "Under AMC Section F (Disclosures), what must Kestrel provide to prospective and current clients regarding fees and conflicts?",
                "options": {
                    "A": "Only the base management fee rate on its public website, omitting trading costs and soft-dollar policies.",
                    "B": "Clear, prominent, and timely disclosures of all fee schedules, actual or estimated fees charged, soft-dollar policies, valuation policies, and material conflicts of interest.",
                    "C": "Fee disclosures only when requested in writing by institutional regulators."
                },
                "answer": "B",
                "explanation": "AMC Section F requires managers to communicate truthfully and prominently with clients, disclosing complete fee structures and actual/estimated fees paid, brokerage/soft-dollar practices, valuation override policies, regulatory actions, and material conflicts.",
                "distractors": {
                    "A": "Posting only a base management fee omits essential disclosures on expenses, performance fees, soft dollars, and valuation methods.",
                    "C": "Disclosure obligations under Section F apply proactively to clients and prospective clients, not only upon regulatory audit."
                }
            },
            {
                "los": "Distinguish the scope of the Asset Manager Code from the Code of Ethics and Standards of Professional Conduct.",
                "question": "How does the Asset Manager Code of Professional Conduct primarily differ in applicability from the CFA Institute Code and Standards?",
                "options": {
                    "A": "The AMC is a voluntary firm-level code adopted by investment management organizations, whereas the Code and Standards bind individual CFA Institute members and candidates.",
                    "B": "The AMC applies only to retail mutual funds, while the Code and Standards apply only to institutional hedge funds.",
                    "C": "The AMC supersedes national securities laws whenever a firm registers with CFA Institute."
                },
                "answer": "A",
                "explanation": "The CFA Institute Code of Ethics and Standards of Professional Conduct apply to *individuals* (members and candidates), whereas the Asset Manager Code is a voluntary *firm-level* ethical framework designed for investment management organizations to adopt and claim compliance with.",
                "distractors": {
                    "B": "Both frameworks apply across retail and institutional asset management contexts.",
                    "C": "Neither the AMC nor the Code and Standards supersedes stricter applicable national laws or regulations."
                }
            }
        ]
    },
    # =========================================================================
    # V12: CFA Designation Misuse & Exam Integrity
    # =========================================================================
    {
        "vignette_id": "V12",
        "vignette_title": "Apex CFA Capital Advisors: Designation Rules and Exam Integrity",
        "module": "Module 2: Guidance for Standards I-VII",
        "topic": "Responsibilities as a CFA Institute Member or Candidate",
        "subtopic": "CFA Designation Misuse & Exam Confidentiality",
        "vignette_text": (
            "Marcus Reed recently passed Level II of the CFA Program and has registered for the upcoming Level III exam. "
            "To impress prospective wealth-management clients in Singapore, Reed prints new business cards reading "
            "'Marcus Reed, CFA Level II' and adds 'CFA Candidate, Expected 2026' to his email signature. Reed also "
            "co-founds a boutique advisory partnership with two charterholders named 'Apex CFA Wealth Management Pte Ltd' "
            "and writes on the firm's homepage: 'As CFAs, our team consistently delivers superior risk-adjusted alpha "
            "compared with non-chartered advisors.'\n\n"
            "One of the co-founders, Evelyn Tan, CFA, earned her charter in 2019, though she let her annual CFA Institute "
            "membership dues lapse two years ago and failed to submit her required annual Professional Conduct Statement "
            "(PCS). Despite her lapsed status, Tan continues signing client letters as 'Evelyn Tan, CFA' and displays "
            "the CFA trademark logo in a font twice as large as her own name on marketing brochures.\n\n"
            "Meanwhile, after sitting for the Level III exam, Reed logs into an anonymous online finance forum and posts: "
            "'Just finished Level III. Be aware that the morning essay section tested private wealth tax-location "
            "strategies and currency hedging extensively, while fixed income immunizations were barely weighted this year.' "
            "Reed does not disclose exact numerical figures from any question, believing general topic weightings help "
            "future candidates study efficiently."
        ),
        "questions": [
            {
                "los": "Evaluate proper reference to CFA candidacy under Standard VII(B).",
                "question": "Printing 'Marcus Reed, CFA Level II' on business cards and 'CFA Candidate, Expected 2026' in his email signature:",
                "options": {
                    "A": "Complies with Standard VII(B), because Reed accurately passed Level II and registered for Level III.",
                    "B": "Violates Standard VII(B), because there is no partial designation such as 'CFA Level II' and candidates must not imply an expected completion date.",
                    "C": "Violates Standard VII(B) only with respect to the business cards, while 'Expected 2026' is permitted."
                },
                "answer": "B",
                "explanation": "Standard VII(B) Reference to CFA Institute, the CFA Designation, and the CFA Program prohibits partial designations like 'CFA Level II' (which imply holding a credential). While Reed may state factually that he is a 'Candidate in the CFA Program' or 'Passed Level II of the CFA Program,' claiming an 'Expected 2026' charter date or appending 'CFA Level II' after his name violates VII(B).",
                "distractors": {
                    "A": "Passing Level II does not confer a partial 'CFA Level II' credential, and implying a future charter award date violates VII(B).",
                    "C": "Both 'CFA Level II' and implying an expected charter date violate Standard VII(B)."
                }
            },
            {
                "los": "Identify prohibited firm names and noun usage under Standard VII(B).",
                "question": "Naming the firm 'Apex CFA Wealth Management Pte Ltd' and writing 'As CFAs, our team consistently delivers superior risk-adjusted alpha' violates Standard VII(B) in how many distinct ways?",
                "options": {
                    "A": "One way only, because using 'CFA' as a plural noun is prohibited while firm names may include 'CFA' if partners hold the charter.",
                    "B": "Three distinct ways: incorporating 'CFA' into a firm name, using 'CFAs' as a plural noun instead of an adjective, and claiming charterholders deliver superior performance.",
                    "C": "Zero ways, because two founders hold the CFA charter and risk-adjusted alpha is an objective historical claim."
                },
                "answer": "B",
                "explanation": "Standard VII(B) strictly prohibits (1) altering or using the CFA mark in a company or product name, (2) using 'CFA' as a noun or plural ('CFAs' instead of 'CFA charterholders'), and (3) exaggerating the meaning of the designation by claiming charterholders achieve superior investment performance.",
                "distractors": {
                    "A": "Company names may NEVER include 'CFA' or 'Chartered Financial Analyst' even if all partners are charterholders.",
                    "C": "All three practices explicitly breach CFA Institute's Standard VII(B) trademark and representation guidelines."
                }
            },
            {
                "los": "Assess active charter status requirements (dues and PCS) under Standard VII(B).",
                "question": "By continuing to sign client letters as 'Evelyn Tan, CFA' while her membership dues and annual Professional Conduct Statement are lapsed, Tan:",
                "options": {
                    "A": "Complies with Standard VII(B), because once earned, the CFA designation is permanent for life regardless of annual dues.",
                    "B": "Violates Standard VII(B), because the right to use the CFA designation requires maintaining active membership via annual dues and the Professional Conduct Statement.",
                    "C": "Violates Standard IV(B) Additional Compensation only."
                },
                "answer": "B",
                "explanation": "Under Standard VII(B), an individual's right to display the CFA designation is contingent upon maintaining active regular membership by paying annual dues and submitting the annual Professional Conduct Statement. Continuing to use 'CFA' while lapsed misrepresents active charterholder standing.",
                "distractors": {
                    "A": "Although the underlying exam completion is permanent, active use of the 'CFA' letters requires current membership and PCS compliance.",
                    "C": "Using a lapsed designation concerns Standard VII(B) (and I(C) Misrepresentation), not external compensation under IV(B)."
                }
            },
            {
                "los": "Apply Standard VII(B) visual formatting rules for the CFA trademark.",
                "question": "Displaying the CFA logo in a font twice as large as Evelyn Tan's name on marketing brochures:",
                "options": {
                    "A": "Violates Standard VII(B), because the CFA mark must not appear larger or more prominent than the individual's name.",
                    "B": "Complies with Standard VII(B), provided the trademark symbol accompanies the logo.",
                    "C": "Violates Standard III(D) Performance Presentation."
                },
                "answer": "A",
                "explanation": "Standard VII(B) trademark guidelines specify that the CFA designation or mark must never be displayed in a font larger or bolder than the charterholder's own name, nor used as a corporate logo.",
                "distractors": {
                    "B": "Adding a trademark symbol does not override the size and prominence restriction.",
                    "C": "Visual formatting of the CFA mark falls under Standard VII(B), not Performance Presentation III(D)."
                }
            },
            {
                "los": "Evaluate post-exam forum posts about tested curriculum areas under Standard VII(A).",
                "question": "By posting on an online forum that the Level III morning exam tested private wealth tax-location and currency hedging extensively while fixed-income immunization had low weight, Reed:",
                "options": {
                    "A": "Complied with Standard VII(A), because he avoided sharing specific numerical figures from any question.",
                    "B": "Violated Standard VII(A) Conduct as Participants in CFA Institute Programs, because disclosing specific topics tested or excluded compromises exam confidentiality.",
                    "C": "Violated Standard III(E) Preservation of Confidentiality."
                },
                "answer": "B",
                "explanation": "Standard VII(A) strictly prohibits sharing confidential exam content, including *which specific topics, sub-areas, or formulas were tested or omitted/lightly weighted* on a given sitting, even without quoting exact numbers. Candidates may express only broad opinions on overall exam difficulty or curriculum fairness.",
                "distractors": {
                    "A": "Topic presence, absence, and relative weighting on a specific exam sitting are confidential exam details protected under Standard VII(A).",
                    "C": "Standard III(E) protects client confidentiality, whereas CFA exam security is governed by Standard VII(A)."
                }
            },
            {
                "los": "Identify permissible public commentary by candidates following a CFA exam under Standard VII(A).",
                "question": "Which post by Reed on the online forum after sitting for Level III would be permissible under Standard VII(A)?",
                "options": {
                    "A": "'I felt the morning constructed-response section was time-pressured and challenging overall.'",
                    "B": "'Make sure you memorize the exact swap-duration formula because Question 4 tested it heavily.'",
                    "C": "'They didn't test alternative investments at all in the afternoon session.'"
                },
                "answer": "A",
                "explanation": "Under Standard VII(A), candidates are free to express general personal opinions about overall exam difficulty, time management, or curriculum breadth ('the morning session felt challenging and time-pressured') provided they disclose zero specific topics, formulas, or question details.",
                "distractors": {
                    "B": "Revealing that a specific formula appeared in Question 4 violates exam confidentiality under VII(A).",
                    "C": "Revealing that alternative investments were omitted in the afternoon session leaks protected exam weighting information under VII(A)."
                }
            }
        ]
    },
    # =========================================================================
    # V13: Knowledge of the Law & Cross-Border Regulatory Conflicts
    # =========================================================================
    {
        "vignette_id": "V13",
        "vignette_title": "Meridian Macro Fund: Cross-Border Legal Conflicts and Dissociation",
        "module": "Module 2: Guidance for Standards I-VII",
        "topic": "Professionalism and Legal Compliance",
        "subtopic": "Knowledge of the Law & Cross-Border Rules",
        "vignette_text": (
            "Nadia Al-Mansoor, CFA, is a global macro portfolio manager employed by Atlas Horizon Asset Management, "
            "headquartered in London, with trading desks in Dubai and Country X. In Country X, local securities laws "
            "contain no statutory prohibition against trading ahead of institutional client block orders by proprietary "
            "accounts, and local regulations allow investment advisors to accept cash gifts up to USD 5,000 from "
            "corporate bond issuers without disclosure. Atlas Horizon's Country X desk head instructs Al-Mansoor to "
            "adopt Country X's looser local standards when managing portfolios booked through the Country X subsidiary "
            "so the firm remains competitive with local banks.\n\n"
            "Simultaneously, a newly onboarded ultra-high-net-worth client in Dubai asks Al-Mansoor to route EUR 8 million "
            "through three offshore shell companies in a manner designed to evade his home country's statutory capital-gains "
            "tax reporting and obscure the beneficial owner's identity from sanctions screening. When Al-Mansoor checks "
            "with Atlas Horizon's regional legal counsel, counsel admits the offshore routing is likely illegal tax "
            "evasion in the client's domicile, yet advises Al-Mansoor to process the transfer anyway because 'Dubai law "
            "does not require us to enforce foreign tax codes.'\n\n"
            "Separately, Al-Mansoor discovers that an Atlas Horizon colleague in London, Tom Bennett, routinely places "
            "his personal name on quarterly sovereign-debt macro reports whose quantitative regressions were lifted "
            "verbatim from an external IMF working paper without attribution. When Al-Mansoor raises the plagiarism "
            "with London compliance, compliance takes no action. Al-Mansoor asks that her own name be removed from "
            "the co-authored sovereign-debt distribution list."
        ),
        "questions": [
            {
                "los": "Apply Standard I(A) Knowledge of the Law to conflicts between local laws and the Code and Standards.",
                "question": "Regarding the Country X desk head's instruction to follow Country X's looser rules on proprietary front-running and USD 5,000 issuer gifts, Al-Mansoor must:",
                "options": {
                    "A": "Follow Country X law because local statutory law always overrides the CFA Institute Code and Standards.",
                    "B": "Follow the stricter rule—the CFA Institute Code and Standards—which prohibit front-running and undisclosed/impairing issuer gifts.",
                    "C": "Follow Country X law only for domestic Country X clients while applying the Code and Standards to London clients."
                },
                "answer": "B",
                "explanation": "Under Standard I(A) Knowledge of the Law, when applicable local law and the Code and Standards conflict, members and candidates must comply with the MORE STRICT standard. Since the Code and Standards (I(B) and VI(B)) are stricter than Country X's permissive rules, Al-Mansoor must abide by the Code and Standards.",
                "distractors": {
                    "A": "Local law overrides the Code and Standards ONLY when local law is MORE strict (e.g., mandating conduct or imposing tighter limits); it never excuses failing to meet stricter ethical standards.",
                    "C": "The Code and Standards apply universally to all CFA members regardless of client domicile."
                }
            },
            {
                "los": "Evaluate participation in cross-border tax evasion and sanctions avoidance under Standards I(A) and I(D).",
                "question": "If Al-Mansoor processes the Dubai client's EUR 8 million offshore shell routing designed to evade taxes and obscure sanctions screening, she violates:",
                "options": {
                    "A": "Standards I(A) Knowledge of the Law and I(D) Misconduct, because knowingly participating in or assisting illegal tax evasion or sanctions circumvention is prohibited.",
                    "B": "Nothing, because regional legal counsel advised that Dubai does not enforce foreign tax codes.",
                    "C": "Standard III(A) only if the shell companies charge high administration fees."
                },
                "answer": "A",
                "explanation": "Standard I(A) prohibits knowingly participating in or assisting any violation of laws, rules, or regulations of any government or regulatory body governing professional activities, and Standard I(D) prohibits dishonest or fraudulent conduct. Relying on a narrow jurisdictional excuse from internal counsel does not justify facilitating illegal tax evasion or sanctions evasion.",
                "distractors": {
                    "B": "Incorrect or self-serving internal legal advice does not immunize a member who knows the structure is designed to facilitate illegal tax evasion and evade sanctions.",
                    "C": "Fiduciary loyalty to a client under Standard III(A) never requires executing illegal transactions."
                }
            },
            {
                "los": "Determine client confidentiality exceptions regarding illegal client activity under Standard III(E).",
                "question": "If local anti-money-laundering law requires Atlas Horizon to file a suspicious transaction report on the Dubai client's shell routing, how does Standard III(E) Preservation of Confidentiality apply?",
                "options": {
                    "A": "Standard III(E) bars filing the report unless the client provides written permission.",
                    "B": "Standard III(E) permits disclosure because the information concerns illegal activities by the client and disclosure is required by applicable law.",
                    "C": "Standard III(E) applies only to current accounts, so Al-Mansoor must first terminate the client before reporting."
                },
                "answer": "B",
                "explanation": "Standard III(E) mandates confidentiality EXCEPT in three defined circumstances: (1) the information concerns illegal activities on the part of the client, (2) disclosure is required by law, or (3) the client permits disclosure.",
                "distractors": {
                    "A": "Client consent is not required when an exception for illegal activity or statutory AML reporting applies.",
                    "C": "Standard III(E) protects current, prospective, and former clients alike, and its legal/illegal-activity exceptions apply immediately without needing termination first."
                }
            },
            {
                "los": "Assess dissociation obligations when an employer ignores ongoing plagiarism under Standard I(A) and I(C).",
                "question": "When London compliance takes no action on Tom Bennett's verbatim plagiarism from an IMF working paper, Al-Mansoor's decision to remove her name from the co-authored report distribution list:",
                "options": {
                    "A": "Is an appropriate first step toward dissociation under Standard I(A), though she should also document her objection and refrain from distributing or endorsing the plagiarized report.",
                    "B": "Violates Standard IV(A) Loyalty by refusing to support a colleague's research output.",
                    "C": "Is unnecessary because IMF working papers are public domain statistics exempt from attribution."
                },
                "answer": "A",
                "explanation": "Under Standard I(A), when a member is aware of ongoing ethical/legal violations (such as Standard I(C) plagiarism) and internal compliance fails to act, the member must dissociate from the violation—starting with removing their name from the tainted report, documenting the objection, and not distributing it.",
                "distractors": {
                    "B": "Standard IV(A) does not require remaining associated with a colleague's plagiarism; Standard I(A) mandates dissociation.",
                    "C": "While recognized public factual data from standard statistical agencies can be cited briefly, lifting entire quantitative regressions verbatim without attribution is plagiarism under Standard I(C)."
                }
            },
            {
                "los": "Evaluate whether Standard I(A) mandates regulatory whistleblowing for all observed violations.",
                "question": "With respect to Tom Bennett's unaddressed plagiarism, does Standard I(A) strictly require Al-Mansoor to report Atlas Horizon to UK financial regulators?",
                "options": {
                    "A": "Yes, Standard I(A) mandates reporting every unaddressed internal violation to external regulators within 30 days.",
                    "B": "No, Standard I(A) requires dissociation from the violation; reporting to external regulators is not automatically required unless mandated by applicable local law, though it may be prudent in severe client-harm cases.",
                    "C": "Yes, unless the IMF grants retroactive copyright clearance."
                },
                "answer": "B",
                "explanation": "According to Standard I(A) guidance, dissociation is mandatory, whereas reporting violations to governmental or regulatory authorities is NOT strictly required by the Code and Standards unless local law mandates reporting—though CFA Institute encourages reporting where permitted and prudent.",
                "distractors": {
                    "A": "The Code and Standards require dissociation, not automatic external regulatory reporting, unless local law requires it.",
                    "C": "Retroactive clearance does not dictate regulatory reporting duties under Standard I(A)."
                }
            },
            {
                "los": "Identify the obligation regarding maintaining current knowledge of applicable laws under Standard I(A).",
                "question": "If Atlas Horizon expands trading into a fourth jurisdiction with unfamiliar short-selling disclosure rules, what does Standard I(A) require of Al-Mansoor?",
                "options": {
                    "A": "Rely exclusively on general London trading rules until local regulators send a warning notice.",
                    "B": "Understand and comply with the applicable securities laws and regulations of every jurisdiction governing her professional activities before trading.",
                    "C": "Delegate all foreign compliance awareness solely to junior operations clerks."
                },
                "answer": "B",
                "explanation": "Standard I(A) requires members and candidates to understand and comply with all applicable laws, rules, and regulations of any government, regulatory organization, licensing agency, or professional association governing their professional activities—including new foreign jurisdictions where they trade.",
                "distractors": {
                    "A": "Ignorance of local securities rules is not an excuse under Standard I(A).",
                    "C": "While members may consult legal/compliance teams for guidance, personal responsibility to follow applicable laws remains with the member."
                }
            }
        ]
    },
    # =========================================================================
    # V14: Independence, Objectivity & Corporate Hospitality
    # =========================================================================
    {
        "vignette_id": "V14",
        "vignette_title": "Granite Peak Credit: Corporate Hospitality, Shelf-Space Fees, and Board Seats",
        "module": "Module 2: Guidance for Standards I-VII",
        "topic": "Independence, Gifts, and Third-Party Incentives",
        "subtopic": "Corporate Hospitality & Distribution Payments",
        "vignette_text": (
            "Julian Mercer, CFA, is a senior high-yield credit analyst at Granite Peak Credit in Houston covering metals "
            "and mining issuers. Prior to a major USD 1.2 billion bond refinancing by Aurum Minerals Corp., Aurum's CFO "
            "invites Mercer and four competing buy-side analysts to tour Aurum's copper mine in Chile. Aurum flies the "
            "analysts on commercial business-class tickets from Houston to Santiago, puts them up for three nights at a "
            "five-star luxury ski resort outside Santiago after the mine inspection, and provides a chartered helicopter "
            "transfer for an afternoon glacier sightseeing excursion. Mercer accepts the commercial flights, resort stay, "
            "and sightseeing tour, reasoning that 'everyone else on the trip accepted it too.'\n\n"
            "Back in Houston, Granite Peak's institutional sales partner, Horizon Distribution Partners, offers to promote "
            "Granite Peak's Flagship High-Yield Fund on Horizon's preferred platform only if Granite Peak pays an annual "
            "'shelf-space marketing support fee' of 20 basis points on assets placed through Horizon. Granite Peak agrees "
            "to pay the 20 bps fee from its own firm revenue without modifying fund expense ratios, and prominently "
            "discloses the arrangement in the fund's prospectus and client onboarding documents.\n\n"
            "Two weeks later, a satisfied long-term corporate pension client whose portfolio outperformed its benchmark by "
            "450 bps sends Mercer two complimentary tickets (face value USD 900 total) to a sold-out championship basketball "
            "game as a thank-you gift for past performance. Mercer immediately reports the gift in writing to Granite Peak's "
            "compliance officer and receives written permission to attend. Meanwhile, Mercer also serves as an unpaid "
            "independent director on the board of a publicly traded regional steel producer whose bonds Granite Peak "
            "holds in client portfolios, without disclosing his board role to Granite Peak's clients."
        ),
        "questions": [
            {
                "los": "Evaluate lavish issuer-paid travel and entertainment under Standard I(B).",
                "question": "By accepting Aurum's business-class commercial flights, three-night luxury ski resort stay, and helicopter glacier tour, Mercer violated:",
                "options": {
                    "A": "Standard I(B) Independence and Objectivity, because issuers should not pay for commercial airfare or luxury non-business hospitality.",
                    "B": "Nothing, because competing analysts also accepted the package and industry custom permits it.",
                    "C": "Standard IV(B) Additional Compensation only, because he failed to get Aurum's written approval."
                },
                "answer": "A",
                "explanation": "Under Standard I(B), analysts must reject lavish hospitality, commercial airfare, luxury resort stays, and recreational excursions paid for by an issuer, as such perks compromise perceived and actual objectivity. Only strictly necessary transport to remote sites lacking commercial access is permitted.",
                "distractors": {
                    "B": "Peer custom ('everyone else accepted it') never excuses a breach of Standard I(B) Independence and Objectivity.",
                    "C": "Standard IV(B) requires employer and payer written consent for external compensation arrangements, whereas lavish issuer gifts/travel directly breach Standard I(B) regardless of consent."
                }
            },
            {
                "los": "Assess client-paid thank-you gifts for past performance under Standards I(B) and IV(B).",
                "question": "Accepting the USD 900 championship basketball tickets from the pension client as thanks for past performance—after disclosing to and receiving written permission from Granite Peak's compliance officer—is:",
                "options": {
                    "A": "A violation of Standard I(B), because any gift above USD 100 impairs objectivity.",
                    "B": "Permissible under Standard I(B) and Standard IV(B), because modest client gifts for past performance (unlike issuer gifts or future contingent incentives) are allowed with employer disclosure and consent.",
                    "C": "A violation of Standard VI(C) Referral Fees."
                },
                "answer": "B",
                "explanation": "The Code and Standards draw an important distinction between gifts from *issuers/vendors* (which threaten objectivity) and gifts from *clients* rewarding past performance. Modest client gifts for past performance do not impair independence, and disclosing/obtaining employer permission satisfies Standards I(B) and IV(B) (provided local/firm gift caps are respected).",
                "distractors": {
                    "A": "CFA Institute sets no rigid USD 100 ceiling; compliance depends on materiality, source (client vs. issuer), past vs. future contingency, and employer disclosure/limits.",
                    "C": "A thank-you gift from an existing client is not a third-party referral fee."
                }
            },
            {
                "los": "Distinguish past-performance client gifts from future performance-bonus offers under Standard IV(B).",
                "question": "If the pension client had instead promised Mercer an extra USD 25,000 personal cash bonus *if* Granite Peak outperformed its benchmark by 400 bps next year, Mercer could accept it ONLY if:",
                "options": {
                    "A": "He discloses it verbally to his desk head after year-end.",
                    "B": "He obtains prior written consent from BOTH Granite Peak (his employer) and the pension client under Standard IV(B) (and satisfies firm conflict rules under VI(A)).",
                    "C": "He splits the USD 25,000 bonus equally with Granite Peak's research team."
                },
                "answer": "B",
                "explanation": "A forward-looking performance incentive from a client creates an additional compensation arrangement that competes with employer duties and could bias portfolio attention toward one client over others. Standard IV(B) strictly requires prior *written consent from all parties involved* (both employer and outside payer), plus fair-dealing safeguards.",
                "distractors": {
                    "A": "Standard IV(B) requires prior written consent from all parties, not post-hoc verbal notice.",
                    "C": "Sharing an unauthorized side payment with teammates does not satisfy Standard IV(B) consent requirements."
                }
            },
            {
                "los": "Evaluate platform shelf-space distribution payments under Standards VI(A) and I(B).",
                "question": "Granite Peak paying Horizon Distribution Partners a 20 bps 'shelf-space marketing support fee' out of firm revenue with full prominent prospectus and onboarding disclosure is:",
                "options": {
                    "A": "Permissible under the Code and Standards, provided Horizon also clearly discloses the conflict to its platform investors and Granite Peak's disclosures are prominent.",
                    "B": "Automatically prohibited under Standard VI(C) Referral Fees, even when fully disclosed.",
                    "C": "A violation of Standard III(A), because shelf-space fees always raise fund expense ratios."
                },
                "answer": "A",
                "explanation": "Revenue-sharing and shelf-space arrangements are permissible under Standards VI(A) and VI(C) when paid transparently by the manager (not hidden in brokerage) and prominently disclosed to prospective investors before purchase so clients understand the distribution incentive.",
                "distractors": {
                    "B": "Standards VI(A) and VI(C) require disclosure of referral/marketing arrangements rather than imposing a blanket ban.",
                    "C": "The vignette states Granite Peak pays the 20 bps from its own firm revenue without modifying fund expense ratios."
                }
            },
            {
                "los": "Analyze undisclosed outside corporate board memberships under Standard VI(A).",
                "question": "Serving as an unpaid director on the board of the regional steel producer whose bonds Granite Peak holds in client portfolios—without telling clients—most directly violates:",
                "options": {
                    "A": "Standard VI(A) Avoid or Disclose Conflicts, because a board directorship creates material fiduciary, access, and objectivity conflicts requiring disclosure.",
                    "B": "Standard IV(B) Additional Compensation, because unpaid directorships constitute monetary compensation.",
                    "C": "Standard III(C) Suitability, because steel bonds are unsuitable for pension funds."
                },
                "answer": "A",
                "explanation": "Serving on a portfolio company's board creates substantial conflicts of interest (fiduciary duties to the issuer's shareholders vs. bondholder clients, plus MNPI access restrictions) even when unpaid. Under Standard VI(A), Mercer must fully disclose the directorship to both his employer and affected clients (and manage MNPI walls under II(A)).",
                "distractors": {
                    "B": "Because the board role is unpaid, Standard IV(B) Additional Compensation is not triggered, whereas Standard VI(A) Disclosure of Conflicts clearly applies.",
                    "C": "Holding a steel bond does not violate Suitability without IPS mismatch; the breach is failing to disclose the dual-role conflict."
                }
            },
            {
                "los": "Identify the specific MNPI risk arising from Mercer's steel-producer board seat.",
                "question": "In addition to conflict disclosure under Standard VI(A), what ongoing operational compliance risk does Mercer's board seat create for Granite Peak's credit trading?",
                "options": {
                    "A": "Mercer regularly receives MNPI in board meetings, requiring Granite Peak to restrict trading or enforce strict information barriers under Standard II(A).",
                    "B": "Granite Peak must liquidate all steel producer bonds immediately regardless of price.",
                    "C": "Mercer cannot vote proxies on any other industrial bonds."
                },
                "answer": "A",
                "explanation": "Corporate directors routinely receive nonpublic earnings, restructuring, and covenant information. Under Standard II(A), Granite Peak must either place the issuer on a restricted list during blackout/MNPI windows or isolate Mercer behind strict information barriers.",
                "distractors": {
                    "B": "Mandatory forced liquidation is neither required nor beneficial to clients if proper information barriers or restricted lists are maintained.",
                    "C": "A board seat at one company does not bar proxy voting across unrelated industrial issuers."
                }
            }
        ]
    },
    # =========================================================================
    # V15: Misrepresentation & Performance Attribution Claims
    # =========================================================================
    {
        "vignette_id": "V15",
        "vignette_title": "Cascade Quantitative Advisors: Misrepresentation and Performance Marketing",
        "module": "Module 2: Guidance for Standards I-VII",
        "topic": "Misrepresentation and Performance Presentation",
        "subtopic": "Misrepresentation & Survivorship Bias",
        "vignette_text": (
            "Cascade Quantitative Advisors is a Seattle-based registered investment advisor marketing a new multi-factor "
            "US equity strategy to institutional consultants. Cascade's marketing director, Trevor Hall, CFA, prepares "
            "a 20-page pitchbook highlighting the strategy's track record. On Slide 4, Hall displays a chart comparing "
            "Cascade's factor returns from 2021 to 2023—the three strongest consecutive years since launch—while omitting "
            "the strategy's severe underperformance in 2019 and 2020. Slide 4 contains no footnote indicating that "
            "earlier periods exist or that five terminated low-performing client accounts were dropped from the composite "
            "series shown.\n\n"
            "On Slide 9, Hall includes a macroeconomic yield-curve regression chart originally published by a prominent "
            "Wall Street investment bank strategist, removing the investment bank's watermark and adding Cascade's "
            "logo in the corner without attributing the source. Elsewhere in the pitchbook, Hall describes Cascade's "
            "short-term US Treasury money-market sleeve as offering 'a guaranteed 4.85% total return over the next 12 "
            "months' and states that Cascade's internal compliance software is 'approved and registered with CFA Institute.'\n\n"
            "During a live finalist pitch with the Pacific Northwest Nurses' Pension, Hall presents an academic credentials "
            "bio claiming he graduated 'Summa Cum Laude in Financial Engineering' when he actually graduated with general "
            "honors (Cum Laude), and orally states that Cascade's live 10-year backtest represents 'actual live client "
            "capital compounded over a full market cycle,' even though the first seven years of the 10-year series were "
            "simulated backtest returns."
        ),
        "questions": [
            {
                "los": "Identify selective time-period cherry-picking and survivorship bias under Standard III(D).",
                "question": "Showing only 2021–2023 returns and omitting five terminated underperforming client accounts on Slide 4 most directly violates:",
                "options": {
                    "A": "Standard III(D) Performance Presentation and Standard I(C) Misrepresentation.",
                    "B": "Standard III(C) Suitability and Standard V(C) Record Retention.",
                    "C": "Standard VI(B) Priority of Transactions."
                },
                "answer": "A",
                "explanation": "Standard III(D) requires performance presentations to be fair, accurate, and complete. Cherry-picking a favorable 3-year window while hiding negative earlier years and stripping terminated underperforming accounts (survivorship bias) misleads prospective clients in violation of Standard III(D) and Standard I(C).",
                "distractors": {
                    "B": "The issue is deceptive historical performance reporting, not individual client IPS suitability or missing records.",
                    "C": "Standard VI(B) governs trade ordering between client and personal accounts, not marketing track records."
                }
            },
            {
                "los": "Apply Standard I(C) Misrepresentation to plagiarism of third-party research charts.",
                "question": "Removing the Wall Street investment bank's watermark from its yield-curve regression chart and adding Cascade's logo without attribution violates:",
                "options": {
                    "A": "Standard I(C) Misrepresentation, because presenting another party's analytical chart as Cascade's own work constitutes plagiarism.",
                    "B": "Standard II(A) Material Nonpublic Information, because bank strategist reports are proprietary inside data.",
                    "C": "Nothing, provided the bank strategist published the chart on a public client portal."
                },
                "answer": "A",
                "explanation": "Under Standard I(C) Misrepresentation, plagiarism—copying or presenting research, charts, or analytical models created by others without explicit attribution—is strictly prohibited, even if the material is publicly available or purchased by subscription.",
                "distractors": {
                    "B": "Published strategist research distributed to clients is not MNPI; the breach is failing to attribute authorship.",
                    "C": "Public availability does not remove the obligation to cite the original author or source of analytical work."
                }
            },
            {
                "los": "Distinguish fixed promised cash flows from guaranteed investment returns under Standard I(C).",
                "question": "Claiming that Cascade's short-term US Treasury money-market sleeve offers 'a guaranteed 4.85% total return over the next 12 months' violates Standard I(C) primarily because:",
                "options": {
                    "A": "Even Treasury-backed funds experience net-asset-value fluctuations, reinvestment rate uncertainty, and expense drag, making a guaranteed 12-month total return misleading.",
                    "B": "US Treasury securities carry substantial credit default risk.",
                    "C": "CFA charterholders are prohibited from quoting any current yield figures in marketing."
                },
                "answer": "A",
                "explanation": "Under Standard I(C), members must not guarantee returns on any investment whose return is inherently uncertain. While an individual US Treasury bill held directly to maturity has fixed nominal promised principal and interest (backed by US government credit), a managed money-market sleeve experiences daily inflows, reinvestment yield changes, fee deductions, and mark-to-market price changes—so guaranteeing a 12-month 'total return' is a misrepresentation.",
                "distractors": {
                    "B": "US Treasuries are backed by full faith and credit; the issue is market/reinvestment/fund-level return uncertainty rather than sovereign credit default.",
                    "C": "Quoting current SEC 7-day yield or yield-to-maturity with proper disclaimers is completely acceptable; guaranteeing future total return is not."
                }
            },
            {
                "los": "Identify misrepresentation of CFA Institute endorsement or registration under Standard VII(B) and I(C).",
                "question": "Stating that Cascade's internal compliance software is 'approved and registered with CFA Institute' violates:",
                "options": {
                    "A": "Standard VII(B) Reference to CFA Institute and Standard I(C) Misrepresentation, because CFA Institute does not approve or register third-party commercial software.",
                    "B": "Standard IV(C) Responsibilities of Supervisors only.",
                    "C": "Standard III(E) Preservation of Confidentiality."
                },
                "answer": "A",
                "explanation": "CFA Institute never endorses, approves, or registers commercial software, investment firms, or investment products. Claiming software is 'approved and registered with CFA Institute' exaggerates and misrepresents CFA Institute's role under Standards VII(B) and I(C).",
                "distractors": {
                    "B": "Making false statements about CFA Institute registration is a direct misrepresentation and VII(B) violation, not merely a supervisory lapse.",
                    "C": "Client data privacy is unrelated to falsely claiming CFA Institute approval."
                }
            },
            {
                "los": "Assess academic credential inflation and simulated-return labeling under Standard I(C) and III(D).",
                "question": "In the live finalist pitch, Hall's claim of graduating 'Summa Cum Laude' instead of 'Cum Laude' and his statement that the 10-year series reflects 'actual live client capital' violate:",
                "options": {
                    "A": "Standard I(C) Misrepresentation regarding both claims, and Standard III(D) Performance Presentation regarding the simulated backtest.",
                    "B": "Standard I(D) Misconduct only, because academic honors do not affect portfolio management.",
                    "C": "Standard V(B) only, because simulated returns may be presented as live once 3 years of live data exist."
                },
                "answer": "A",
                "explanation": "Standard I(C) prohibits any knowing misrepresentation of academic or professional qualifications (inflating Cum Laude to Summa Cum Laude) and misrepresenting simulated backtests as live client track records. Standard III(D) specifically requires distinguishing clearly between simulated/hypothetical backtest results and actual live performance.",
                "distractors": {
                    "B": "Credential falsification in professional marketing is an explicit Standard I(C) Misrepresentation (and also raises I(D) honesty concerns), not solely I(D).",
                    "C": "Simulated returns must always be clearly labeled and separated from actual live returns regardless of how many live years have elapsed."
                }
            },
            {
                "los": "Identify an acceptable practice when presenting composite performance under Standard III(D).",
                "question": "To properly present Cascade's 3-year live history alongside its 7-year backtest in compliance with Standard III(D) and V(B), Hall should:",
                "options": {
                    "A": "Blend the backtest and live series seamlessly into one 10-year cumulative line so consultants see a full cycle.",
                    "B": "Present the 3-year actual composite separately from any backtested model simulation, include all terminated accounts, and disclose simulation assumptions and limitations.",
                    "C": "Delete the 2019–2020 live period and display only simulated returns for those two years."
                },
                "answer": "B",
                "explanation": "Under Standards III(D) and V(B), actual performance must include all fee-paying discretionary accounts (including terminated accounts up to their final full period) and must be presented separately from simulated/model performance, with clear labeling and disclosure of model assumptions and limitations.",
                "distractors": {
                    "A": "Linking or blending hypothetical backtest data into actual live returns without separation misleads investors.",
                    "C": "Replacing actual live loss years (2019–2020) with simulated results is fraudulent cherry-picking."
                }
            }
        ]
    },
    # =========================================================================
    # V16: Market Manipulation & Information-Based Spoofing
    # =========================================================================
    {
        "vignette_id": "V16",
        "vignette_title": "Blackstone-Gate Proprietary Desk: Spoofing, Wash Trades, and Information Manipulation",
        "module": "Module 2: Guidance for Standards I-VII",
        "topic": "Integrity of Capital Markets",
        "subtopic": "Market Manipulation & Trading Practices",
        "vignette_text": (
            "Devon Brooks, CFA, heads algorithmic trading at Horizon Gate Markets, a proprietary trading and quantitative "
            "execution firm in New York. To capture favorable benchmark fills during the final ten minutes before the "
            "4:00 p.m. closing auction in small-cap equities, Brooks configures an automated algorithm to submit stacked, "
            "large-size limit buy orders across multiple price levels just below the best bid, creating the illusion of "
            "deep institutional buying interest. Immediately as retail and momentum algorithms lift offers higher, Brooks's "
            "algorithm cancels 98% of the stacked buy orders within 40 milliseconds and sells short into the elevated price.\n\n"
            "Simultaneously, Horizon Gate's credit trader, Victor Hsu, manages two affiliated internal accounts (Account X "
            "and Account Y) that hold illiquid corporate notes. To make Account X's holdings appear actively traded before "
            "quarter-end auditor valuations, Hsu executes pre-arranged matching buy and sell trades between Account X and "
            "Account Y through an interdealer broker, shifting zero net economic ownership.\n\n"
            "Earlier that week, Brooks published a pseudonymous bearish note on a popular financial blog claiming that "
            "a mid-cap biotech firm, Helix Therapeutics, had failed its Phase III FDA clinical trial—a fabrication Brooks "
            "invented while holding short call spreads on Helix. By contrast, one of Brooks's junior quants, Maya Chen, "
            "systematically executes legitimate tax-loss harvesting trades in December across taxable client accounts "
            "by selling losing ETFs and rotating into non-identical broad index ETFs, and executes cross-exchange "
            "statistical arbitrage trades capturing genuine 3-cent mispricings between dual-listed shares."
        ),
        "questions": [
            {
                "los": "Identify transaction-based spoofing and layering under Standard II(B).",
                "question": "Brooks's closing-auction algorithm that places large stacked buy orders only to cancel 98% within 40 milliseconds to induce higher prices for short selling violates:",
                "options": {
                    "A": "Standard II(B) Market Manipulation, because layering/spoofing orders with intent to cancel misleads market participants regarding supply and demand.",
                    "B": "Nothing, because limit orders carry valid execution risk during those 40 milliseconds.",
                    "C": "Standard III(B) Fair Dealing, because retail traders lost money to an institutional desk."
                },
                "answer": "A",
                "explanation": "Standard II(B) Market Manipulation prohibits practices that distort prices or artificially inflate trading volume with the intent to mislead market participants. Layering/spoofing—entering non-bona fide limit orders to create false order-book depth and cancelling them within milliseconds—is classic transaction-based market manipulation.",
                "distractors": {
                    "B": "Submitting orders specifically engineered for immediate 98% cancellation without genuine intent to trade constitutes illegal spoofing/layering regardless of brief exposure.",
                    "C": "Horizon Gate is a proprietary desk trading against the market rather than allocating trades among its own clients; the breach is market manipulation under II(B) and I(A)."
                }
            },
            {
                "los": "Evaluate pre-arranged wash trades between affiliated accounts under Standard II(B).",
                "question": "Victor Hsu's pre-arranged trades between Account X and Account Y involving zero change in beneficial ownership violate:",
                "options": {
                    "A": "Standard II(B) Market Manipulation and Standard I(C) Misrepresentation, by fabricating artificial trading liquidity and distorted quarter-end valuation marks.",
                    "B": "Standard VI(C) Referral Fees, because an interdealer broker collected commissions.",
                    "C": "Nothing, provided the trades cleared at prevailing mid-market quotes."
                },
                "answer": "A",
                "explanation": "Executing pre-arranged wash trades with no change in beneficial ownership to create the false appearance of liquidity and influence quarter-end valuations violates Standard II(B) Market Manipulation (and Standard I(C)/I(D) by misleading auditors and investors).",
                "distractors": {
                    "B": "Standard VI(C) concerns referral payments, not wash-trade manipulation.",
                    "C": "Wash trades with no economic transfer of risk are manipulative under II(B) regardless of the price level used."
                }
            },
            {
                "los": "Assess information-based market manipulation under Standard II(B).",
                "question": "Publishing a fabricated rumor under a pseudonym claiming Helix Therapeutics failed an FDA clinical trial while holding short call spreads violates:",
                "options": {
                    "A": "Standard II(B) Market Manipulation, Standard I(D) Misconduct, and Standard I(A) Knowledge of the Law.",
                    "B": "Standard II(A) Material Nonpublic Information only.",
                    "C": "Standard V(B), because pseudonyms omit the author's credentials."
                },
                "answer": "A",
                "explanation": "Standard II(B) prohibits both transaction-based manipulation and *information-based manipulation*—disseminating false or misleading rumors to induce buying or selling by others and distort security prices. Fabricating false FDA trial failure news to profit from short positions violates II(B), I(D), and securities fraud laws (I(A)).",
                "distractors": {
                    "B": "Because the claim was entirely fabricated rather than true confidential corporate information, it is false rumor manipulation (II(B)), not true insider MNPI (II(A)).",
                    "C": "The core violation is securities fraud and market manipulation via false rumors, not merely using a pseudonym."
                }
            },
            {
                "los": "Distinguish legitimate tax-loss harvesting from market manipulation under Standard II(B).",
                "question": "Maya Chen's December tax-loss harvesting sales rotating taxable clients into non-identical broad index ETFs represent:",
                "options": {
                    "A": "A violation of Standard II(B), because tax-motivated trades depress year-end ETF prices.",
                    "B": "Permissible trading under Standard II(B), because legitimate tax-strategy trades lacking intent to mislead market participants do not constitute market manipulation.",
                    "C": "A violation of Standard III(A), because selling at a loss harms client returns."
                },
                "answer": "B",
                "explanation": "Standard II(B) expressly notes that transaction-based manipulation requires intent to mislead market participants or distort prices artificially. Bona fide trades executed for legitimate tax-loss harvesting, liquidity management, or portfolio rebalancing do NOT violate Standard II(B).",
                "distractors": {
                    "A": "Executing genuine economic sales to capture legitimate tax losses for clients is sound portfolio management, not manipulation.",
                    "C": "Tax-loss harvesting into non-identical substitute ETFs enhances after-tax client wealth in full alignment with Standard III(A) Loyalty, Prudence, and Care."
                }
            },
            {
                "los": "Distinguish genuine cross-exchange arbitrage from market manipulation under Standard II(B).",
                "question": "Executing cross-exchange statistical arbitrage trades to capture genuine 3-cent price discrepancies between dual-listed shares is:",
                "options": {
                    "A": "A violation of Standard II(B), because exploiting cross-exchange price gaps distorts market pricing.",
                    "B": "Permissible under Standard II(B), because genuine arbitrage aligns prices across venues and improves market efficiency without deceptive intent.",
                    "C": "A violation of Standard VI(B), because high-frequency desks trade faster than retail clients."
                },
                "answer": "B",
                "explanation": "Capturing genuine price discrepancies across exchanges through bona fide trades improves price discovery and market liquidity. Standard II(B) does not prohibit legitimate arbitrage strategies.",
                "distractors": {
                    "A": "Arbitrage eliminates mispricing rather than artificially distorting prices.",
                    "C": "Standard VI(B) governs prioritizing client trades ahead of personal/proprietary trades within a firm serving clients, not executing proprietary market arbitrage."
                }
            },
            {
                "los": "Evaluate supervisory duties regarding algorithmic trading surveillance under Standard IV(C).",
                "question": "What supervisory failure enabled Brooks's spoofing algorithm to operate undetected in the closing auction?",
                "options": {
                    "A": "Failure to implement order-to-trade ratio alerts, pre-trade compliance controls, and algorithmic audit logging under Standard IV(C).",
                    "B": "Failure to prohibit all automated execution algorithms across equity desks.",
                    "C": "Failure to obtain client sign-off for closing-auction participation."
                },
                "answer": "A",
                "explanation": "Under Standard IV(C) Responsibilities of Supervisors, firms running algorithmic trading strategies must maintain robust automated surveillance—monitoring order-to-trade cancellation ratios, layering patterns, and code deployment reviews—to detect and prevent market manipulation.",
                "distractors": {
                    "B": "Algorithmic execution itself is standard and efficient when properly governed; a blanket ban is not required.",
                    "C": "Horizon Gate is a proprietary desk, and closing-auction participation is routine rather than requiring special client sign-off."
                }
            }
        ]
    },
    # =========================================================================
    # V17: Fiduciary Duty, Proxy Voting & Client Confidentiality
    # =========================================================================
    {
        "vignette_id": "V17",
        "vignette_title": "Ironwood Fiduciary Trust: Pension Proxy Voting and Client Confidentiality",
        "module": "Module 2: Guidance for Standards I-VII",
        "topic": "Duties to Clients",
        "subtopic": "Fiduciary Duty, Proxy Voting & Confidentiality",
        "vignette_text": (
            "Ironwood Fiduciary Trust serves as external discretionary investment manager for the EUR 1.1 billion "
            "defined-benefit pension plan of Veridian Industrial Corp. Clara Vance, CFA, manages the equity sleeve "
            "of the Veridian Pension Plan, which owns 3.2% of an industrial supplier, Kestrel Controls. Kestrel Controls "
            "is also Veridian Industrial's largest strategic machinery customer. Ahead of Kestrel Controls' annual "
            "shareholder meeting, an activist investor proposes a proxy resolution that Kestrel's board replace its "
            "poison-pill takeover defense and evaluate a premium cash buyout offer worth 28% above market price.\n\n"
            "Two days before the proxy vote deadline, Veridian Industrial's CFO telephones Vance and urges her to vote "
            "all pension shares AGAINST the activist proposal and in favor of Kestrel's incumbent management, explaining "
            "that a takeover of Kestrel could jeopardize Veridian Industrial's commercial supplier discounts. Vance's "
            "internal investment analysis concludes that the buyout proposal is clearly in the economic best interest "
            "of Veridian's pension beneficiaries, yet she capitulates to the CFO's request to protect Ironwood's "
            "mandate relationship with Veridian Industrial.\n\n"
            "Separately, Ironwood's private wealth unit terminates its relationship with a former high-net-worth client, "
            "Arthur Sterling, after Sterling moves his assets elsewhere. Six months later, Ironwood's marketing team "
            "shares Sterling's historical portfolio balances and private email address with an unaffiliated estate-planning "
            "partner for a co-branded newsletter campaign without Sterling's consent. Meanwhile, CFA Institute's "
            "Professional Conduct Program (PCP) requests confidential client file records from Ironwood regarding an "
            "unrelated compliance inquiry into a former Ironwood portfolio manager."
        ),
        "questions": [
            {
                "los": "Identify the true fiduciary beneficiary in corporate pension management under Standard III(A).",
                "question": "In managing the Veridian Industrial defined-benefit pension plan, to whom does Clara Vance owe her primary fiduciary duty of loyalty, prudence, and care under Standard III(A)?",
                "options": {
                    "A": "Veridian Industrial Corp.'s corporate management and CFO, because the company sponsors and funds the plan.",
                    "B": "The Veridian Pension Plan's participants and beneficiaries.",
                    "C": "Kestrel Controls' shareholders, to maximize market takeover efficiency."
                },
                "answer": "B",
                "explanation": "Under Standard III(A) Loyalty, Prudence, and Care, when managing a corporate pension trust or employee benefit plan, the investment manager's fiduciary duty is owed exclusively to the plan participants and beneficiaries—NOT to the sponsoring corporation's management.",
                "distractors": {
                    "A": "Even though corporate officers appoint the asset manager, corporate commercial interests cannot override pension beneficiaries' retirement security.",
                    "C": "Vance owes fiduciary duty to the pension plan's beneficiaries, not directly to outside issuers' shareholders."
                }
            },
            {
                "los": "Evaluate proxy voting conflicts under Standard III(A) and Standard I(B).",
                "question": "By voting the pension shares against the 28%-premium buyout proposal at the Veridian CFO's request—contrary to her own economic valuation—Vance violated:",
                "options": {
                    "A": "Standard III(A) Loyalty, Prudence, and Care and Standard I(B) Independence and Objectivity.",
                    "B": "Nothing, because proxy voting is a corporate governance matter outside fiduciary investment management.",
                    "C": "Standard III(C) Suitability, because activist proposals alter portfolio beta."
                },
                "answer": "A",
                "explanation": "Proxy voting is an integral part of managing client assets under Standard III(A). Managers must vote proxies in an informed and responsible manner strictly in the best economic interest of beneficiaries (and disclose proxy policies). Yielding to corporate sponsor pressure sacrifices beneficiary value and violates Standards III(A) and I(B).",
                "distractors": {
                    "B": "CFA Institute explicitly recognizes proxy votes as client assets carrying full fiduciary care obligations under Standard III(A).",
                    "C": "The breach is subordinating beneficiary economic interests to corporate politics (III(A) and I(B)), not IPS beta alignment."
                }
            },
            {
                "los": "Determine required proxy voting disclosures under Standard III(A) and AMC Section F.",
                "question": "To properly discharge proxy voting duties for institutional clients like the Veridian Pension Plan, Ironwood should:",
                "options": {
                    "A": "Abstain from voting on all contested corporate proxies to remain neutral.",
                    "B": "Adopt written proxy voting policies, disclose them to clients, vote consistently in beneficiaries' economic interest, and retain voting records.",
                    "C": "Always vote automatically with incumbent corporate management unless directed otherwise by regulators."
                },
                "answer": "B",
                "explanation": "Standard III(A) and Asset Manager Code Section F require managers to establish clear proxy voting policies, disclose those policies to clients, analyze material proposals independently (using cost-benefit judgment for non-routine votes), and keep voting records.",
                "distractors": {
                    "A": "Blanket abstention on material economic proposals (such as a 28% buyout offer) abdicates fiduciary responsibility.",
                    "C": "Automatically rubber-stamping incumbent management ignores fiduciary analysis of shareholder/beneficiary value."
                }
            },
            {
                "los": "Apply Standard III(E) Preservation of Confidentiality to former clients and marketing partners.",
                "question": "Sharing former client Arthur Sterling's historical portfolio balances and private email address with an unaffiliated estate-planning partner without his consent violates:",
                "options": {
                    "A": "Nothing, because Sterling ceased to be an Ironwood client six months ago.",
                    "B": "Standard III(E) Preservation of Confidentiality, which protects former, current, and prospective clients alike.",
                    "C": "Standard IV(A) Loyalty, because Ironwood lost a wealth client."
                },
                "answer": "B",
                "explanation": "Standard III(E) protects the confidentiality of information regarding current, *former*, and *prospective* clients. Sharing a former client's financial details and contact data with an unaffiliated third party for marketing without client consent violates Standard III(E).",
                "distractors": {
                    "A": "Confidentiality duties persist indefinitely after a client terminates the advisory relationship.",
                    "C": "Standard IV(A) governs employee loyalty to the employer, not firm protection of former client data."
                }
            },
            {
                "los": "Evaluate the Standard III(E) exception for CFA Institute PCP investigations.",
                "question": "When CFA Institute's Professional Conduct Program (PCP) requests confidential client files during an investigation into a former portfolio manager, how does Standard III(E) apply?",
                "options": {
                    "A": "Ironwood must refuse the PCP's request unless every client signs a waiver.",
                    "B": "Ironwood may share the relevant records with the PCP without violating Standard III(E), as PCP investigations are an explicit permitted exception (and PCP preserves strict confidentiality).",
                    "C": "Ironwood may share records only if local criminal courts issue a subpoena."
                },
                "answer": "B",
                "explanation": "Under Standard III(E) guidance, sharing confidential client records with the CFA Institute Professional Conduct Program (PCP) in connection with a disciplinary investigation is explicitly permitted and does NOT violate client confidentiality, because the PCP treats all such records confidentially.",
                "distractors": {
                    "A": "Requiring client waivers before cooperating with a CFA Institute PCP investigation is not required under Standard III(E) guidance.",
                    "C": "A court subpoena is not required for cooperating with CFA Institute's PCP under Standard III(E)."
                }
            },
            {
                "los": "Identify steps to manage sponsor-related proxy conflicts under Standard VI(A) and III(A).",
                "question": "When facing a conflict where voting a proxy could harm a commercial relationship of the corporate plan sponsor, Ironwood's governance best practice is to:",
                "options": {
                    "A": "Follow a pre-established written proxy policy or delegate the conflicted vote to an independent proxy fiduciary/committee insulated from commercial pressure.",
                    "B": "Call the sponsor's CFO to negotiate a compromise split vote.",
                    "C": "Sell the entire Kestrel Controls stake two days before the record date to avoid voting."
                },
                "answer": "A",
                "explanation": "Establishing objective written proxy voting guidelines or utilizing an independent fiduciary committee/proxy advisor ensures voting decisions are insulated from commercial retaliation and strictly reflect beneficiary economic interests under Standards III(A) and VI(A).",
                "distractors": {
                    "B": "Negotiating voting compromises with the sponsor's CFO compromises fiduciary independence.",
                    "C": "Liquidating a fundamentally attractive holding purely to dodge a governance vote harms pension returns."
                }
            }
        ]
    },
    # =========================================================================
    # V18: Fair Dealing & Research Dissemination
    # =========================================================================
    {
        "vignette_id": "V18",
        "vignette_title": "Kensington Equity Research: Dissemination Tiers, Embargoes, and Trade Rotation",
        "module": "Module 2: Guidance for Standards I-VII",
        "topic": "Duties to Clients",
        "subtopic": "Fair Dealing & Research Dissemination",
        "vignette_text": (
            "Kensington Equity Research is a London-based institutional broker-dealer offering two disclosed client "
            "service tiers: 'Platinum Advisory' (for institutional clients paying GBP 150,000 annually, who receive live "
            "analyst phone briefings after a research report publishes) and 'Standard Research' (for institutional clients "
            "paying GBP 35,000 annually, who receive email and portal access). Both service tiers and their differences "
            "are clearly disclosed in Kensington's client engagement agreements.\n\n"
            "On Wednesday at 7:00 a.m., senior telecom analyst Owen Patel, CFA, finalizes a major downgrade of EuroTel "
            "Group from 'Buy' to 'Sell' due to an unsustainable dividend payout. Before releasing the report electronically "
            "to the portal at 9:00 a.m., Patel telephones Kensington's five largest Platinum clients at 7:30 a.m. to warn "
            "them of the impending 'Sell' rating so they can begin reducing positions at the London open. At 8:15 a.m., "
            "Kensington's proprietary trading desk—notified internally by compliance of the upcoming downgrade—sells "
            "100,000 shares of EuroTel out of the firm's inventory to reduce market exposure ahead of the 9:00 a.m. release.\n\n"
            "Meanwhile, in Kensington's separate discretionary SMA division, portfolio manager Hannah Brooks manages 60 "
            "discretionary accounts following the same UK Large-Cap strategy. When executing multi-day portfolio rebalances "
            "across custodial platforms that cannot be aggregated into one single block trade, Brooks routinely executes "
            "the 15 accounts belonging to Kensington's founding partners and highest-fee clients on Day 1, and places the "
            "remaining 45 accounts on Days 2 and 3. Also, during a separate research quiet period before publishing an "
            "earnings preview on NovaBank, a Platinum client calls Patel unsolicited asking what he thinks of NovaBank's "
            "valuation; Patel refuses to disclose any pending rating change before simultaneous public release."
        ),
        "questions": [
            {
                "los": "Distinguish fair dealing from equal dealing across disclosed service tiers under Standard III(B).",
                "question": "How does Standard III(B) Fair Dealing apply to Kensington offering 'Platinum Advisory' phone briefings versus 'Standard Research' portal access?",
                "options": {
                    "A": "Offering differentiated service levels is permissible if disclosed to all clients AND all tiers receive material recommendation changes simultaneously before privileged tiers can trade.",
                    "B": "Different service tiers are strictly prohibited under Standard III(B), which requires identical service for all clients regardless of fee.",
                    "C": "Platinum clients may receive rating downgrades 90 minutes early because they pay GBP 150,000 annually."
                },
                "answer": "A",
                "explanation": "Standard III(B) requires dealing with clients *fairly*, not *equally*. Firms may offer premium tiers (such as live analyst Q&A calls) if fully disclosed, PROVIDED that premium clients do not receive material investment recommendation changes ahead of other clients in a way that disadvantages lower-tier clients.",
                "distractors": {
                    "B": "Differentiated service tiers are allowed under Standard III(B) when transparently disclosed and when actionable rating changes are disseminated simultaneously.",
                    "C": "Higher annual fees never justify selective advance tipping of an impending downgrade before general client dissemination."
                }
            },
            {
                "los": "Identify selective advance dissemination violations under Standard III(B).",
                "question": "By telephoning five Platinum clients at 7:30 a.m. with the EuroTel 'Sell' downgrade 90 minutes before releasing the report to Standard clients at 9:00 a.m., Patel violated:",
                "options": {
                    "A": "Standard III(B) Fair Dealing, because Standard clients were unfairly disadvantaged by delayed receipt of an actionable rating change.",
                    "B": "Standard II(A) Material Nonpublic Information, because an analyst's downgrade opinion is inside corporate data.",
                    "C": "Standard VI(C) Referral Fees."
                },
                "answer": "A",
                "explanation": "Giving select clients a 90-minute head start on a material 'Buy' to 'Sell' downgrade allows them to sell into unaffected market liquidity while Standard clients suffer price deterioration upon the 9:00 a.m. release. This directly violates Standard III(B) Fair Dealing.",
                "distractors": {
                    "B": "An analyst's own published opinion/rating is generally not corporate insider MNPI under II(A) (unless based on corporate MNPI); the violation of tipping select clients ahead of others is Standard III(B) Fair Dealing.",
                    "C": "No third-party referral payment is involved."
                }
            },
            {
                "los": "Apply Standard VI(B) Priority of Transactions to proprietary desk trading ahead of research release.",
                "question": "When Kensington's proprietary trading desk sold 100,000 shares of EuroTel at 8:15 a.m. ahead of the 9:00 a.m. client report release, the firm violated:",
                "options": {
                    "A": "Standard VI(B) Priority of Transactions and Standard III(B) Fair Dealing, because proprietary firm trading took priority over client dissemination and action.",
                    "B": "Nothing, because the proprietary desk had an obligation to manage firm balance-sheet risk.",
                    "C": "Standard IV(A) Loyalty."
                },
                "answer": "A",
                "explanation": "Under Standard VI(B) and III(B) guidance, a firm's proprietary trading accounts must NOT trade ahead of client dissemination of a material research recommendation change. Clients must have a fair opportunity to act on the research before the firm trades for its own account.",
                "distractors": {
                    "B": "Firm risk-management desires never justify front-running impending client research releases.",
                    "C": "The desk traded ahead of clients (VI(B)/III(B)), rather than harming its own employer (IV(A))."
                }
            },
            {
                "los": "Evaluate trade rotation across non-aggregable SMAs under Standard III(B).",
                "question": "Hannah Brooks's habit of consistently executing Day 1 trades for founding partners and highest-fee accounts while pushing the remaining 45 accounts to Days 2 and 3 violates Standard III(B). What is the proper alternative?",
                "options": {
                    "A": "Use an objective, documented random or sequential trade-rotation schedule across custodians, and subordinate founding-partner beneficial accounts until all client accounts are completed.",
                    "B": "Execute the highest-fee clients on Day 1 in even months and Day 3 in odd months, while always putting founding partners first.",
                    "C": "Refuse to accept SMA accounts held at external custodians."
                },
                "answer": "A",
                "explanation": "When orders across custodial platforms cannot be aggregated into a single block, Standard III(B) requires an objective, fair trade-rotation system (rotating order sequence systematically or randomly across cycles) so no client group is systematically disadvantaged—and under Standard VI(B), any beneficial-owner/partner accounts must trade *after* all client accounts.",
                "distractors": {
                    "B": "Putting founding partners' beneficial accounts ahead of client accounts violates Standard VI(B) regardless of month.",
                    "C": "External custodians are routine in SMA management; fair trade rotation resolves non-aggregability without rejecting clients."
                }
            },
            {
                "los": "Assess handling unsolicited client inquiries before research publication under Standard III(B).",
                "question": "When a Platinum client calls Patel unsolicited during the quiet period asking about NovaBank's valuation, Patel's refusal to preview the pending rating change is:",
                "options": {
                    "A": "Proper under Standard III(B), because analysts must not leak pending material rating changes in response to unsolicited calls prior to simultaneous dissemination.",
                    "B": "A violation of Standard III(A), because Platinum clients pay for direct analyst phone access.",
                    "C": "A violation of Standard V(B), because withholding views conceals investment processes."
                },
                "answer": "A",
                "explanation": "Under Standard III(B), an analyst may discuss previously published research or general public facts in response to an unsolicited client inquiry, provided the analyst NEVER reveals an unreleased rating change or pending new research conclusion prior to simultaneous client dissemination.",
                "distractors": {
                    "B": "Paying for direct phone access entitles clients to discuss published work, not to receive advance tips on unreleased changes.",
                    "C": "Standard V(B) does not authorize selective early disclosure of pending rating updates."
                }
            },
            {
                "los": "Determine appropriate dissemination controls across global time zones under Standard III(B).",
                "question": "If Kensington distributes research to clients in London, New York, and Tokyo, what satisfies Standard III(B) Fair Dealing regarding timing of dissemination?",
                "options": {
                    "A": "Release simultaneously across all global clients electronically (e.g., via portal/email blast), regardless of local market opening hours.",
                    "B": "Email Tokyo clients 8 hours earlier so they receive it at Tokyo morning open, then London and New York at their local opens.",
                    "C": "Mail printed hardcopies to Standard clients while emailing Platinum clients instantaneously."
                },
                "answer": "A",
                "explanation": "Standard III(B) recommends simultaneous electronic dissemination of material investment recommendations to all clients globally—not staggered delivery by local market open, which would give Asian clients an unfair advance trading window on global securities or ADRs.",
                "distractors": {
                    "B": "Staggering releases by time zone creates arbitrage and disadvantages later-notified clients on dual-listed or global equities.",
                    "C": "Using slow physical mail for lower-tier clients while electronically alerting premium clients creates systemic unfair timing advantages."
                }
            }
        ]
    },
    # =========================================================================
    # V19: Suitability, IPS Updates & Concentrated Stock Risk
    # =========================================================================
    {
        "vignette_id": "V19",
        "vignette_title": "Ashford Private Wealth: IPS Updates, Concentrated Risk, and Total Portfolio Suitability",
        "module": "Module 2: Guidance for Standards I-VII",
        "topic": "Duties to Clients",
        "subtopic": "Suitability & Investment Policy Statements",
        "vignette_text": (
            "Elena Rostova, CFA, is a private wealth advisor at Ashford Private Wealth managing portfolios for high-net-worth "
            "families. One long-standing client, 74-year-old retired surgeon Dr. Martin Vance, holds a USD 6 million "
            "balanced portfolio whose written Investment Policy Statement (IPS)—last updated four years ago—sets a "
            "capital-preservation objective with a 40% equity / 60% investment-grade bond target and requires USD 240,000 "
            "in annual living withdrawals.\n\n"
            "Six months ago, Dr. Vance underwent a costly divorce settlement that reduced his outside cash reserves to zero "
            "and required him to begin supporting an adult disabled dependent, increasing his required annual cash draw to "
            "USD 400,000. Dr. Vance informs Rostova of these changes over lunch, yet Rostova makes no revisions to his IPS "
            "and leaves his portfolio unchanged. Separately, Dr. Vance's brother passes away and leaves him USD 2.5 million "
            "in restricted shares of a single volatile biotech stock, representing nearly 30% of his new total wealth. "
            "Rostova leaves the concentrated biotech stake unhedged and undiversified because 'it had strong momentum.'\n\n"
            "Meanwhile, another Ashford client, wealthy entrepreneur Samir Patel (net worth USD 45 million, aggressive risk "
            "tolerance, multi-decade horizon), asks Rostova to invest 5% (USD 2.25 million) of his total wealth into an "
            "illiquid distressed-venture fund. Rostova evaluates the 5% venture allocation in light of Patel's overall "
            "diversified balance sheet and approves it. However, one week later, a conservative retiree client with a "
            "low risk tolerance calls Rostova with an unsolicited order to invest 35% of her retirement account into "
            "leveraged 3x inverse semiconductor ETFs after watching a television segment."
        ),
        "questions": [
            {
                "los": "Apply Standard III(C) Suitability to IPS update requirements after material life changes.",
                "question": "Following Dr. Vance's divorce, depleted outside reserves, and jump in annual cash needs from USD 240,000 to USD 400,000, Rostova's failure to update his IPS and rebalance his portfolio violated:",
                "options": {
                    "A": "Standard III(C) Suitability, because an advisor must review and update the IPS at least annually and promptly whenever a client experiences a material change in financial circumstances.",
                    "B": "Nothing, because Dr. Vance did not send a notarized written request to amend his IPS.",
                    "C": "Standard III(E) Preservation of Confidentiality."
                },
                "answer": "A",
                "explanation": "Under Standard III(C) Suitability, members in an advisory relationship must update the client's IPS regularly (at least annually) and *promptly* upon learning of material changes in client circumstances, constraints, or liquidity needs—not wait passively for formal client paperwork.",
                "distractors": {
                    "B": "Once an advisor learns of major changes affecting liquidity and obligations, the advisor has an affirmative duty under III(C) to initiate an IPS review and adjustment.",
                    "C": "Failing to update an IPS concerns Suitability (III(C)), not Confidentiality (III(E))."
                }
            },
            {
                "los": "Assess concentrated single-stock inheritance risk under Standard III(C) and III(A).",
                "question": "Leaving the inherited USD 2.5 million volatile biotech stake (nearly 30% of Dr. Vance's wealth) unhedged and undiversified based solely on 'strong momentum' violates:",
                "options": {
                    "A": "Standard III(C) Suitability and Standard III(A) Loyalty, Prudence, and Care, because extreme single-stock concentration conflicts with a 74-year-old retiree's capital-preservation and elevated liquidity needs.",
                    "B": "Standard II(A) Material Nonpublic Information.",
                    "C": "Standard VI(A) Avoid or Disclose Conflicts."
                },
                "answer": "A",
                "explanation": "Standard III(C) requires managing total portfolio risk and diversification appropriately for the client's risk tolerance and liquidity needs. Retaining an unhedged 30% concentrated volatile biotech position for a liquidity-constrained 74-year-old retiree breaches both Suitability (III(C)) and Prudence (III(A)).",
                "distractors": {
                    "B": "There is no nonpublic inside information involved in the inherited stock.",
                    "C": "There is no external conflict of interest motivating the inaction; it is an imprudent suitability failure."
                }
            },
            {
                "los": "Apply the total portfolio context principle under Standard III(C) to high-risk satellite investments.",
                "question": "Rostova's approval of a 5% illiquid distressed-venture fund allocation for entrepreneur Samir Patel (USD 45 million net worth, aggressive profile) was:",
                "options": {
                    "A": "A violation of Standard III(C), because illiquid distressed venture funds are inherently unsuitable for private wealth clients.",
                    "B": "Compliant with Standard III(C), because suitability is evaluated in the context of the client's *total portfolio* rather than viewing an asset class in isolation.",
                    "C": "A violation of Standard V(A), unless Patel also holds 50% in cash."
                },
                "answer": "B",
                "explanation": "Standard III(C) explicitly instructs managers to judge the suitability of investments in the context of the client's *total portfolio*—considering diversification benefits, liquidity capacity, and overall risk-return alignment. A 5% venture stake fits well within an aggressive USD 45 million portfolio.",
                "distractors": {
                    "A": "High-risk or illiquid assets are not per se unsuitable; suitability depends on total portfolio size, diversification, horizon, and client constraints.",
                    "C": "No arbitrary 50% cash requirement applies under Standard V(A)."
                }
            },
            {
                "los": "Determine when mandate-level suitability overrides total portfolio diversification under Standard III(C).",
                "question": "If Rostova instead managed a dedicated, narrowly defined 'US Municipal Bond Income Fund' with a strict prospectus mandate, how would Standard III(C) govern adding high-yield equity warrants to boost yield?",
                "options": {
                    "A": "Permissible if the warrants lower the fund's overall beta.",
                    "B": "Prohibited under Standard III(C), because for a specific pooled fund or narrow mandate, suitability requires adhering strictly to the fund's stated mandate and constraints.",
                    "C": "Permissible provided they represent under 10% of assets."
                },
                "answer": "B",
                "explanation": "While private wealth suitability applies in a *total portfolio* context, managers of pooled funds or narrow-mandate strategies fulfill Standard III(C) by ensuring every security aligns with the fund's *stated investment mandate, objectives, and constraints* (also reinforced by Asset Manager Code Section B).",
                "distractors": {
                    "A": "Equity warrants contradict an investment-grade municipal bond mandate regardless of statistical correlation.",
                    "C": "There is no 10% exemption allowing style drift outside a fund's stated investment mandate."
                }
            },
            {
                "los": "Evaluate proper handling of an unsolicited, materially unsuitable trade request under Standard III(C).",
                "question": "When the conservative retiree calls with an unsolicited instruction to put 35% of her retirement account into 3x inverse leveraged semiconductor ETFs, what is Rostova's best initial course of action?",
                "options": {
                    "A": "Execute the trade immediately without comment because unsolicited client orders bypass Standard III(C).",
                    "B": "Refuse to execute immediately, explain the extreme compounding/leverage risks and IPS mismatch clearly to the client, and follow firm policy (declining the trade or requiring documented IPS review/waiver—or ending the relationship if materially harmful).",
                    "C": "Buy 35% in regular 1x semiconductor ETFs instead without telling the client."
                },
                "answer": "B",
                "explanation": "Under Standard III(C) guidance on unsolicited unsuitable trades, an advisor must NOT blindly execute a potentially devastating trade. The advisor must educate the client on why the trade contradicts the IPS and risk capacity, follow firm procedures (either requiring formal written acknowledgment/IPS update if minor/informed, or refusing execution in discretionary accounts and considering terminating the relationship if the client insists on a materially destructive action).",
                "distractors": {
                    "A": "Blindly executing a 35% 3x inverse leveraged ETF trade for a conservative retiree without consultation violates fiduciary care and Standard III(C) guidance.",
                    "C": "Substituting an unauthorized security without client consent violates Standard III(A) and V(B)."
                }
            },
            {
                "los": "Identify required IPS components under Standard III(C) planning standards.",
                "question": "In revising Dr. Vance's IPS under Standard III(C), which combination of elements must Rostova document?",
                "options": {
                    "A": "Only his desired annual return target and benchmark index.",
                    "B": "Return objectives, risk tolerance, and all five constraints (time horizon, liquidity needs, tax concerns, legal/regulatory factors, and unique circumstances such as his disabled dependent).",
                    "C": "Only his custodian account number and brokerage commission schedule."
                },
                "answer": "B",
                "explanation": "A complete IPS under Standard III(C) documents the client's return objectives, risk tolerance (willingness and ability), and the key constraints: liquidity needs, time horizon, tax considerations, legal/regulatory restrictions, and unique circumstances.",
                "distractors": {
                    "A": "Focusing solely on return targets without risk capacity and liquidity/unique constraints produces an incomplete, non-compliant IPS.",
                    "C": "Administrative custody and commission details do not constitute an Investment Policy Statement."
                }
            }
        ]
    },
    # =========================================================================
    # V20: Diligence, Reasonable Basis & Sub-Advisor Selection
    # =========================================================================
    {
        "vignette_id": "V20",
        "vignette_title": "Northbridge Endowment Office: Manager Due Diligence and Committee Dissent",
        "module": "Module 2: Guidance for Standards I-VII",
        "topic": "Investment Analysis, Recommendations, and Actions",
        "subtopic": "Diligence, Reasonable Basis & Sub-Advisors",
        "vignette_text": (
            "David Okafor, CFA, is Chief Investment Officer at Northbridge University Endowment (USD 2.2 billion). "
            "Seeking higher fixed-income yields, Okafor considers allocating USD 120 million to QuantPulse Credit, an "
            "emerging quantitative credit hedge fund launched 14 months ago. During a single 45-minute meeting, QuantPulse "
            "presents a glossy pitchbook showing a 2.9 annualized Sharpe ratio over 14 months. Pressed by an upcoming "
            "board meeting deadline, Okafor recommends hiring QuantPulse without verifying QuantPulse's independent "
            "fund administrator, auditing its prime brokerage custody, checking background litigation history, or "
            "stress-testing how its credit spread model behaves during illiquid market drawdowns.\n\n"
            "Simultaneously, Northbridge's senior equities director, Sarah Lin, CFA, asks junior analyst Leo Gomez to "
            "update a discounted cash flow (DCF) valuation on Apex Semiconductor. Gomez downloads a consensus spreadsheet "
            "from an external boutique research firm and submits the final target price to Lin without inspecting the "
            "boutique's discount rate, terminal growth assumption, or revenue drivers. Lin presents the valuation to "
            "Northbridge's four-member Investment Committee as 'our thoroughly vetted internal DCF.'\n\n"
            "During the Investment Committee vote on Apex Semiconductor, three members vote to buy a USD 60 million "
            "position based on solid semiconductor cycle data and reasonable valuation checks. The fourth committee "
            "member, Priya Shah, CFA, disagrees with the consensus view because she expects slower foundry utilization. "
            "However, Shah acknowledges that the committee's majority analysis was thorough, unbiased, and well-supported "
            "by credible research. Shah asks whether Standard V(A) compels her to resign from the committee or remove "
            "her name from the committee record."
        ),
        "questions": [
            {
                "los": "Apply Standard V(A) Diligence and Reasonable Basis to sub-advisor and external manager selection.",
                "question": "Recommending a USD 120 million allocation to QuantPulse Credit based solely on a glossy pitchbook and 14-month Sharpe ratio without operational, background, or stress-test diligence violates:",
                "options": {
                    "A": "Standard V(A) Diligence and Reasonable Basis (and Standard III(A) Prudence), because selecting external managers requires thorough investment AND operational due diligence.",
                    "B": "Standard VI(C) Referral Fees, because QuantPulse is an emerging manager.",
                    "C": "Standard III(D) Performance Presentation, because 14 months is too short to cite a Sharpe ratio."
                },
                "answer": "A",
                "explanation": "Under Standard V(A) Diligence and Reasonable Basis, selecting external managers or sub-advisors demands the same thorough diligence as selecting individual securities—verifying strategy risk, tail-liquidity stress behavior, independent administration, custody, regulatory history, and organizational controls. Relying on a 45-minute pitch and unverified 14-month Sharpe ratio fails V(A) and III(A).",
                "distractors": {
                    "B": "No referral payment is mentioned; the failure is inadequate investment and operational due diligence.",
                    "C": "While 14 months is short, the violation is Okafor's failure to verify controls, custody, and model stress assumptions before allocating USD 120 million."
                }
            },
            {
                "los": "Evaluate reliance on third-party/secondary research under Standard V(A).",
                "question": "By submitting the boutique research firm's DCF target price without inspecting its discount rate, terminal growth, or revenue assumptions, Leo Gomez violated:",
                "options": {
                    "A": "Standard V(A) Diligence and Reasonable Basis, because relying on secondary or third-party research requires verifying the soundness and reasonableness of underlying inputs and methodology.",
                    "B": "Standard II(A) Material Nonpublic Information, because consensus spreadsheets come from external vendors.",
                    "C": "Nothing, because boutique research providers assume sole ethical liability for their spreadsheets."
                },
                "answer": "A",
                "explanation": "Under Standard V(A), members may use secondary or third-party research only if they exercise reasonable diligence to determine that the research is sound, independent, and built on reasonable assumptions and methodologies. Blindly adopting a target price without checking WACC or terminal growth violates V(A).",
                "distractors": {
                    "B": "External consensus models are not inside corporate MNPI.",
                    "C": "Analysts can never outsource Standard V(A) reasonable-basis accountability to third-party vendors."
                }
            },
            {
                "los": "Identify misrepresentation of secondary research authorship under Standard I(C) and V(A).",
                "question": "When Sarah Lin presents the unverified external boutique DCF to the Investment Committee as 'our thoroughly vetted internal DCF,' she violates:",
                "options": {
                    "A": "Standard I(C) Misrepresentation (plagiarism and false claim of internal vetting) and Standard V(A) (lack of supervisory diligence over Gomez's model).",
                    "B": "Standard VI(B) Priority of Transactions.",
                    "C": "Standard VII(B) Reference to CFA Institute."
                },
                "answer": "A",
                "explanation": "Claiming an external research firm's spreadsheet is Northbridge's 'thoroughly vetted internal DCF' misrepresents both authorship (plagiarism under Standard I(C)) and the rigor of internal due diligence (Standards I(C) and V(A)).",
                "distractors": {
                    "B": "No personal or proprietary trade priority conflict exists here.",
                    "C": "No reference to CFA Institute or the CFA designation occurred."
                }
            },
            {
                "los": "Apply Standard V(A) guidance on group consensus and minority dissent.",
                "question": "Regarding Priya Shah's disagreement with the Investment Committee's majority decision to buy Apex Semiconductor, what does Standard V(A) require of Shah?",
                "options": {
                    "A": "Shah must resign from the Investment Committee immediately whenever she disagrees with a majority vote.",
                    "B": "Because the majority's consensus conclusion has a reasonable and adequate basis in thorough research, Shah does NOT have to dissociate or remove her name from the committee record, though she may document her dissent internally.",
                    "C": "Shah must send an anonymous letter to the university board overriding the committee vote."
                },
                "answer": "B",
                "explanation": "Standard V(A) guidance explicitly addresses group research/investment committee consensus: a member who disagrees with a group recommendation does NOT have to ask for their name to be removed or resign PROVIDED the group's conclusion has a reasonable and adequate basis supported by thorough research. (If the member believes the consensus lacks a reasonable basis, then they must dissociate.)",
                "distractors": {
                    "A": "Good-faith professional disagreement over foundry utilization does not require resignation when the committee process is rigorous and evidence-based.",
                    "C": "Anonymous board sabotage is unnecessary when the majority decision meets Standard V(A) diligence."
                }
            },
            {
                "los": "Contrast dissenting on a well-supported consensus vs. dissenting on an unsubstantiated recommendation.",
                "question": "Under what condition would Standard V(A) instead obligate Priya Shah to demand her name be removed from an Investment Committee report?",
                "options": {
                    "A": "Whenever her quantitative valuation estimate differs by more than 10% from the committee average.",
                    "B": "If she determines the committee's recommendation lacks a reasonable and adequate basis (e.g., driven by unverified inputs, manipulation, or management pressure).",
                    "C": "Whenever the position size exceeds 2% of endowment assets."
                },
                "answer": "B",
                "explanation": "Under Standard V(A), if a group consensus lacks a reasonable and adequate basis—such as relying on fabricated assumptions, pressure, or absent diligence—a dissenting member cannot lend their name to it and must dissociate by having their name removed from the report.",
                "distractors": {
                    "A": "Reasonable differences in valuation assumptions (even >10%) are normal in investing and do not imply lack of reasonable basis.",
                    "C": "Position size alone does not trigger mandatory dissociation if sizing complies with IPS constraints and diligence."
                }
            },
            {
                "los": "Determine appropriate operational due diligence factors for hedge fund onboarding under Standard V(A) and I(E).",
                "question": "Which checklist item is critical for Okafor to verify before recommending QuantPulse Credit to Northbridge's board?",
                "options": {
                    "A": "Confirmation of independent fund administrator, audited financial statements, third-party prime/custody separation, and liquidity gate/redemption mismatch stress tests.",
                    "B": "Verification that QuantPulse's office uses modern interior architecture and expensive risk software brands.",
                    "C": "Guaranteeing QuantPulse generates at least 12% positive return every calendar year."
                },
                "answer": "A",
                "explanation": "Robust operational and investment due diligence under Standard V(A) and Standard I(E) Competence requires verifying independent valuation/administration, custody segregation, audited financials, legal/regulatory compliance records, and stress-testing liquidity mismatch under crisis scenarios.",
                "distractors": {
                    "B": "Surface impressions and software branding are not substitutes for independent operational verification.",
                    "C": "No hedge fund can guarantee positive returns, and demanding return guarantees contradicts Standard I(C)."
                }
            }
        ]
    }
])

VIGNETTES.extend([
    # =========================================================================
    # V21: Client Communication, Process Changes & Record Retention
    # =========================================================================
    {
        "vignette_id": "V21",
        "vignette_title": "Redwood Fundamental Equity: Strategy Drift, Fact vs. Opinion, and Record Retention",
        "module": "Module 2: Guidance for Standards I-VII",
        "topic": "Investment Communication and Recordkeeping",
        "subtopic": "Process Changes, Fact vs. Opinion & Record Retention",
        "vignette_text": (
            "Daniel Choi, CFA, manages the Redwood Value Dividend Fund (USD 950 million), whose prospectus and quarterly "
            "client letters state that the fund invests strictly in profitable, dividend-paying mature cash-flow "
            "equities using low leverage. Frustrated by three quarters of relative underperformance against growth "
            "indices, Choi quietly shifts 38% of the fund into non-dividend-paying early-stage software stocks and "
            "adds 1.25x gross equity index futures leverage, intending to disclose the shift only if it underperforms "
            "at the annual shareholder review.\n\n"
            "In his Q3 client update letter regarding a core industrial holding, FerroCorp, Choi writes: 'FerroCorp "
            "reported Q2 EBITDA of USD 310 million and currently trades at 8.5x trailing EV/EBITDA. Because FerroCorp "
            "will generate 18% annual free-cash-flow growth through 2028, its share price will double within 24 months.' "
            "The letter presents the 18% cash-flow growth and doubling projection without distinguishing them as analyst "
            "estimates or explaining key commodity-input assumptions and recession sensitivity.\n\n"
            "Meanwhile, Redwood's analysts conduct active investment thesis debates over encrypted messaging apps "
            "configured to auto-delete messages after 30 days, and Choi stores all of his quantitative spreadsheet "
            "backups solely on an unbacked personal cloud drive. When junior analyst Priya Nair leaves Redwood later "
            "that year, she attempts to take her five-year handwritten research notebooks containing proprietary "
            "Redwood management-meeting notes, claiming they are her personal property under Standard V(C)."
        ),
        "questions": [
            {
                "los": "Apply Standard V(B) Communication with Clients and Prospective Clients to material strategy changes.",
                "question": "Quietly shifting 38% of the Redwood Value Dividend Fund into non-dividend software stocks and adding 1.25x futures leverage without informing investors violates:",
                "options": {
                    "A": "Standard V(B) Communication with Clients and Prospective Clients (as well as III(C) mandate adherence), because managers must promptly disclose material changes in investment process and risk.",
                    "B": "Nothing, provided the shift does not increase the fund's stated expense ratio.",
                    "C": "Standard VI(C) Referral Fees."
                },
                "answer": "A",
                "explanation": "Standard V(B) explicitly requires members to disclose to clients and prospective clients the basic format and general principles of the investment process AND promptly disclose any changes that might materially affect those processes—alongside significant risks like futures leverage. Shifting 38% out of dividend value into growth and adding leverage also breaches Standard III(C) mandate adherence.",
                "distractors": {
                    "B": "Investment process transparency under V(B) and mandate fidelity under III(C) apply regardless of expense ratios.",
                    "C": "No referral payment is involved."
                }
            },
            {
                "los": "Distinguish fact from opinion in client research communications under Standard V(B).",
                "question": "In Choi's Q3 client letter on FerroCorp, how does Standard V(B) require him to handle the historical EBITDA figure versus the 18% FCF growth and price-doubling claim?",
                "options": {
                    "A": "Both can be stated identically as objective valuation facts because they derive from a discounted cash flow model.",
                    "B": "He must clearly distinguish between established facts (Q2 EBITDA of USD 310 million and 8.5x trailing multiple) and analyst opinion/estimates (18% FCF growth and projected price doubling), while disclosing key assumptions and limitations.",
                    "C": "He must omit all historical financial numbers to avoid anchoring client expectations."
                },
                "answer": "B",
                "explanation": "Standard V(B) explicitly requires members to distinguish clearly between *fact* and *opinion* in presenting investment analyses and recommendations. Historical reported financials are facts; future FCF growth rates and target prices are inherently uncertain opinions/projections that must be labeled as estimates alongside key risks and assumptions.",
                "distractors": {
                    "A": "Model projections are opinions, not facts, and stating that a stock 'will double' without qualification also borders on Standard I(C) misrepresentation.",
                    "C": "Reporting verified historical financial data is valuable and standard when clearly separated from forward-looking estimates."
                }
            },
            {
                "los": "Apply Standard V(C) Record Retention regarding electronic communication deletion and recommended duration.",
                "question": "Allowing investment thesis debates on messaging apps to auto-delete after 30 days—with no archiving—violates Standard V(C) Record Retention. Absent stricter local regulations, what retention period does CFA Institute recommend?",
                "options": {
                    "A": "1 year.",
                    "B": "3 years.",
                    "C": "At least 7 years."
                },
                "answer": "C",
                "explanation": "Under Standard V(C) Record Retention, members must develop and maintain appropriate records (including electronic communications, research notes, and trade rationale) supporting investment analyses, recommendations, and actions. In the absence of specific regulatory mandates, CFA Institute recommends retaining records for at least **7 years**.",
                "distractors": {
                    "A": "A 1-year retention period is far shorter than regulatory norms and CFA Institute's 7-year standard.",
                    "B": "CFA Institute explicitly recommends at least 7 years (not 3 years) when local laws do not impose a specific retention period."
                }
            },
            {
                "los": "Determine record ownership between employer and employee under Standard V(C) and IV(A).",
                "question": "Regarding departing analyst Priya Nair's claim that her five-year handwritten research notebooks containing Redwood management-meeting notes are her personal property under Standard V(C), which statement is correct?",
                "options": {
                    "A": "Handwritten physical notebooks belong to the analyst who wrote them, whereas digital spreadsheets belong to the firm.",
                    "B": "All research records created during employment—whether electronic or handwritten—are the property of the employer (Redwood), not the departing analyst.",
                    "C": "She may take the notebooks provided she emails copies to Redwood's compliance officer."
                },
                "answer": "B",
                "explanation": "Under Standard V(C) and Standard IV(A) Loyalty, records supporting investment recommendations and analyses created during employment belong to the *firm* (employer), regardless of medium (electronic files or handwritten notebooks). If a departing employee later needs access for regulatory defense, the firm retains the official records.",
                "distractors": {
                    "A": "Medium (paper vs. digital) does not alter employer ownership of work product produced during employment.",
                    "C": "Even leaving copies behind does not permit taking proprietary management-meeting notes belonging to the employer without express written authorization."
                }
            },
            {
                "los": "Assess risk disclosure obligations for leveraged strategies under Standard V(B).",
                "question": "Had Redwood's prospectus originally authorized 1.25x futures leverage, what would Standard V(B) still require Choi to communicate to investors?",
                "options": {
                    "A": "Nothing, because prospectus authorization removes ongoing communication duties.",
                    "B": "Clear explanation of the significant risks and limitations of futures leverage (e.g., amplified drawdowns, margin calls, and tracking basis risk) in plain language.",
                    "C": "A guarantee that futures leverage reduces portfolio volatility."
                },
                "answer": "B",
                "explanation": "Under Standard V(B), members must communicate the significant risks and limitations associated with an investment process—especially structural leverage, liquidity constraints, and derivative basis risks—in clear, comprehensible language.",
                "distractors": {
                    "A": "Prospectus authorization is necessary, not sufficient; ongoing risk limitations must still be communicated clearly under V(B).",
                    "C": "Claiming leverage guarantees lower volatility is false and violates Standard I(C)."
                }
            },
            {
                "los": "Identify firm responsibility for personal-drive storage of official investment records under Standard V(C).",
                "question": "Storing quantitative valuation backups solely on Choi's personal cloud drive rather than Redwood's centralized compliance archive creates what primary hazard under Standard V(C)?",
                "options": {
                    "A": "The firm loses auditability and continuity of required 7-year investment records if Choi leaves, deletes files, or suffers a personal account breach.",
                    "B": "Personal cloud drives violate Standard VII(B).",
                    "C": "It forces Redwood to adopt GIPS money-weighted returns."
                },
                "answer": "A",
                "explanation": "Standard V(C) places primary recordkeeping responsibility on the investment firm (and individual compliance). Storing firm investment records solely on an unbacked personal cloud account compromises firm ownership, audit trails, cybersecurity (Standard III(E)), and continuity upon employee departure.",
                "distractors": {
                    "B": "Standard VII(B) applies exclusively to references to CFA Institute and the CFA designation.",
                    "C": "Cloud storage practices have no bearing on GIPS time-weighted vs. money-weighted return selection."
                }
            }
        ]
    },
    # =========================================================================
    # V22: Conflicts of Interest, Cross-Trading & Dual Roles
    # =========================================================================
    {
        "vignette_id": "V22",
        "vignette_title": "Bayside Municipal Advisors: Cross-Trading, Dual Roles, and Family Broker Ownership",
        "module": "Module 2: Guidance for Standards I-VII",
        "topic": "Conflicts of Interest",
        "subtopic": "Avoid or Disclose Conflicts & Cross-Trading",
        "vignette_text": (
            "Marcus Bennett, CFA, manages tax-exempt municipal bond SMAs and two municipal mutual funds at Bayside "
            "Municipal Advisors in Philadelphia. To raise cash for a retiring SMA client's USD 5 million withdrawal "
            "without paying dealer bid-ask spreads, Bennett executes an internal cross-trade selling USD 5 million of "
            "an illiquid local transit authority bond from the liquidating SMA directly to Bayside's flagship Municipal "
            "Income Fund. Rather than using an independent third-party market valuation or mid-market quotes from "
            "unaffiliated dealers, Bennett prices the cross-trade at his internal model price of 103.50, even though "
            "external bond dealers quote the issue at 99.75 bid / 100.50 ask—effectively shielding the exiting SMA "
            "client at the mutual fund's expense.\n\n"
            "Separately, Bennett's brother-in-law owns 40% of Liberty Municipal Securities, a small regional broker-dealer. "
            "Over the past year, Bennett routed 30% of Bayside's secondary municipal bond volume to Liberty Securities "
            "without disclosing his brother-in-law's ownership stake to Bayside's compliance officer or to clients. "
            "Bennett argues that Liberty's execution prices were competitive with other regional dealers.\n\n"
            "Additionally, Bennett personally holds vested employee stock options worth USD 350,000 in FinGrid Analytics, "
            "a municipal credit data vendor whose enterprise software Bayside is currently evaluating for a multi-year "
            "contract on Bennett's recommendation. Finally, Bennett manages both a long-only conservative municipal "
            "fund and a higher-fee leveraged municipal arbitrage hedge fund that occasionally shorts long-dated municipal "
            "ETFs and lower-tier revenue bonds held in the long-only fund."
        ),
        "questions": [
            {
                "los": "Evaluate internal cross-trading practices under Standards III(A), III(B), and AMC Section C.",
                "question": "Pricing the internal cross-trade at 103.50 when independent external dealers quote 99.75/100.50 violates:",
                "options": {
                    "A": "Nothing, because internal cross-trades are exempt from market pricing when eliminating dealer spreads.",
                    "B": "Standard III(A) Loyalty, Prudence, and Care and Standard III(B) Fair Dealing, because cross-trades must occur at fair independent market prices and never favor one client at another's expense.",
                    "C": "Standard VI(C) Referral Fees."
                },
                "answer": "B",
                "explanation": "Internal cross-trades between client accounts are permissible only when consistent with both clients' IPS, documented as achieving best execution, and executed at an objective, independently verified market price (such as independent bid-ask midpoint). Pricing at an inflated 103.50 transfers value unfairly from the buying fund to the exiting SMA, violating Standards III(A) and III(B).",
                "distractors": {
                    "A": "Cross-trades must still reflect genuine fair market prices verified independently; saving spreads cannot justify a 300+ bps off-market transfer.",
                    "C": "No external referral fee was paid."
                }
            },
            {
                "los": "Identify undisclosed family broker ownership conflicts under Standard VI(A).",
                "question": "Routing 30% of Bayside's trading volume to Liberty Municipal Securities without disclosing his brother-in-law's 40% ownership stake violates:",
                "options": {
                    "A": "Standard VI(A) Avoid or Disclose Conflicts, even if Liberty's execution prices were competitive.",
                    "B": "Nothing, because a brother-in-law is not an immediate spouse or dependent child.",
                    "C": "Standard VII(A) Conduct as Participants."
                },
                "answer": "A",
                "explanation": "Under Standard VI(A), members must disclose all matters—including material family business relationships—that could reasonably be expected to impair independence or create the appearance of partiality in broker selection. Even if Liberty offered competitive execution, failing to disclose the 40% family ownership to employer and clients breaches Standard VI(A).",
                "distractors": {
                    "B": "A 40% ownership stake held by a close relative such as a brother-in-law is a classic material conflict requiring prominent disclosure under VI(A).",
                    "C": "Standard VII(A) applies exclusively to CFA Program exam conduct."
                }
            },
            {
                "los": "Assess vendor ownership conflicts during software procurement under Standard VI(A).",
                "question": "When Bennett recommends that Bayside sign a multi-year software contract with FinGrid Analytics while holding USD 350,000 of FinGrid stock options, what does Standard VI(A) require?",
                "options": {
                    "A": "He must exercise the options immediately before recommending the software.",
                    "B": "He must fully and prominently disclose his USD 350,000 FinGrid option stake to Bayside's compliance/procurement decision-makers and recuse himself from vendor selection if required.",
                    "C": "No disclosure is needed because FinGrid is a software vendor rather than a municipal bond issuer."
                },
                "answer": "B",
                "explanation": "Standard VI(A) covers conflicts affecting duties to an *employer* as well as clients. Holding USD 350,000 in FinGrid options creates a clear financial stake in FinGrid winning Bayside's contract, requiring prompt, full disclosure to Bayside and recusal from selection/negotiation.",
                "distractors": {
                    "A": "Exercising options into shares leaves the financial ownership conflict intact; disclosure (and recusal) is required.",
                    "C": "Conflicts of interest with vendors affecting employer procurement decisions squarely trigger Standard VI(A)."
                }
            },
            {
                "los": "Evaluate managing side-by-side long-only and leveraged long/short funds under Standard VI(A) and III(B).",
                "question": "Managing both a standard-fee long-only municipal fund and a higher-fee leveraged hedge fund that occasionally shorts securities held by the long-only fund requires Bayside to:",
                "options": {
                    "A": "Prohibit Bennett from buying any bond in the long-only fund if any hedge fund anywhere shorts it.",
                    "B": "Implement strict conflict disclosures under Standard VI(A), fair trade allocation/short-selling guardrails under III(B), and ensure hedge fund short sales do not disadvantage long-only clients.",
                    "C": "Charge the same performance fee on the long-only fund so incentives match."
                },
                "answer": "B",
                "explanation": "Side-by-side management of higher-fee hedge funds alongside long-only funds creates acute conflicts over best investment ideas, trade priority, and opposing positions. Under Standards VI(A), III(A), and III(B), the firm must prominently disclose the conflict, maintain robust trade-allocation and short-sale approval controls, and ensure long-only clients are never harmed or subordinated.",
                "distractors": {
                    "A": "Market-wide hedge fund shorting cannot dictate long-only management, though internal side-by-side conflicts require strict controls and disclosures.",
                    "C": "Equalizing fees across different vehicle structures is neither required nor practical; transparent governance and conflict controls are."
                }
            },
            {
                "los": "Identify qualities of an effective conflict disclosure under Standard VI(A).",
                "question": "Under Standard VI(A) guidance, for a conflict disclosure to be considered effective, it must be:",
                "options": {
                    "A": "Buried in small print in an annual custodian privacy notice sent two years after onboarding.",
                    "B": "Prominent, delivered in plain language, and communicate the specific substance of the conflict clearly before the client acts or contracts.",
                    "C": "Delivered orally during casual hallway conversations."
                },
                "answer": "B",
                "explanation": "Standard VI(A) specifically stipulates that disclosures must be *prominent*, stated in *plain language*, and convey the *substance* and potential impact of the conflict clearly so clients and employers can make informed decisions.",
                "distractors": {
                    "A": "Fine-print boilerplate or delayed post-hoc notices fail the prominence and plain-language requirements of VI(A).",
                    "C": "Casual undocumented oral remarks fail to ensure clear, verifiable conflict communication."
                }
            },
            {
                "los": "Determine preferred hierarchy between avoiding vs. disclosing conflicts under Standard VI(A).",
                "question": "According to Standard VI(A) Avoid or Disclose Conflicts, when a conflict of interest cannot be adequately managed or neutralized through disclosure alone (such as an acute off-market cross-trade), the member's best course of action is to:",
                "options": {
                    "A": "Avoid the conflicted transaction altogether.",
                    "B": "Proceed with the transaction anyway so long as a footnote appears in Form ADV.",
                    "C": "Split the 300 bps price difference 50/50 between the two client funds."
                },
                "answer": "A",
                "explanation": "Standard VI(A) is titled *Avoid or Disclose Conflicts*: while many conflicts can be managed through full and fair disclosure, certain conflicts (such as off-market cross-trades that inherently transfer wealth from one client to another) are fundamentally inconsistent with fiduciary loyalty and must be *avoided* altogether.",
                "distractors": {
                    "B": "Disclosing an inherently unfair, value-transferring trade does not authorize breaching Standard III(A) and III(B).",
                    "C": "Arbitrarily splitting an off-market valuation error still deviates from true independent market pricing."
                }
            }
        ]
    },
    # =========================================================================
    # V23: Additional Compensation, Side Hustles & Whistleblowing
    # =========================================================================
    {
        "vignette_id": "V23",
        "vignette_title": "Sovereign Horizon Fund: External Consulting, Verbal Consents, and Whistleblowing",
        "module": "Module 2: Guidance for Standards I-VII",
        "topic": "Duties to Employers",
        "subtopic": "Additional Compensation & Side Activities",
        "vignette_text": (
            "Tariq Hassan, CFA, is a quantitative risk analyst employed full-time by the Sovereign Horizon Fund, a "
            "national investment authority. On weekends, Hassan builds macroeconomic visualization dashboards as an "
            "independent contractor for Meridian Fintech Labs, a software firm seeking to sell risk analytics tools "
            "to Sovereign Horizon and competing sovereign funds. Meridian Fintech pays Hassan USD 4,000 per month "
            "for his weekend consulting. Hassan verbally mentions his weekend coding to his immediate supervisor over "
            "coffee, and the supervisor nods approvingly, saying 'Just don't do it on work hours.' Neither Hassan nor "
            "his supervisor obtains written consent from Sovereign Horizon or Meridian Fintech.\n\n"
            "Separately, an outside sub-advised pension client impressed by Hassan's custom currency-hedging report "
            "offers Hassan a personal USD 15,000 cash bonus if Sovereign Horizon's currency overlay outperforms its "
            "benchmark over the next fiscal year. Hassan obtains written consent from his Sovereign Horizon HR director "
            "and compliance officer, though he neglects to get written acknowledgment from the pension client's board, "
            "believing only employer consent is necessary since the client initiated the offer.\n\n"
            "Meanwhile, Hassan also runs a free personal weekend podcast explaining basic compounding and bond math "
            "to university students, generating zero revenue and involving zero investment recommendations. Finally, "
            "two weeks later, Hassan uncovers evidence that Sovereign Horizon's Chief Investment Officer is falsifying "
            "private-infrastructure cash flow inputs to conceal USD 180 million in valuation write-downs prior to an "
            "external bond issuance. After internal audit ignores Hassan's documented memo, Hassan considers reporting "
            "the fraud to the national financial regulator."
        ),
        "questions": [
            {
                "los": "Apply Standard IV(B) Additional Compensation Arrangements to external consulting with a potential vendor/competitor.",
                "question": "Hassan's USD 4,000/month weekend consulting arrangement with Meridian Fintech Labs—supported only by his supervisor's casual verbal nod—violates:",
                "options": {
                    "A": "Standard IV(B) Additional Compensation Arrangements, because external compensation creating potential conflicts requires prior *written consent* from all parties involved.",
                    "B": "Nothing, because weekend work outside office hours is exempt from Standard IV(B).",
                    "C": "Standard VI(C) Referral Fees, unless Meridian Fintech sells software directly to Sovereign Horizon."
                },
                "answer": "A",
                "explanation": "Under Standard IV(B), members must not accept gifts, benefits, compensation, or consideration that competes with or might reasonably be expected to create a conflict of interest with their employer's interest unless they obtain **written consent from all parties involved**. Because Meridian Fintech sells tools to competing funds and potentially to Sovereign Horizon, verbal supervisor approval is insufficient.",
                "distractors": {
                    "B": "Work performed on weekends does not exempt an employee from Standard IV(B) when the external payer operates in a competing or vendor capacity.",
                    "C": "This is an outside compensation/consulting arrangement (IV(B)), not a client referral fee (VI(C))."
                }
            },
            {
                "los": "Identify the 'all parties involved' written consent rule under Standard IV(B).",
                "question": "Regarding the pension client's offer of a conditional USD 15,000 bonus for future currency-overlay outperformance, why is Hassan's written consent from Sovereign Horizon alone insufficient under Standard IV(B)?",
                "options": {
                    "A": "Because Standard IV(B) requires written consent from BOTH the employer AND the outside party providing the compensation (here, the pension client's governing body), ensuring full mutual clarity of terms.",
                    "B": "Because CFA charterholders can never accept bonuses under any circumstances.",
                    "C": "Because the bonus amount is below USD 50,000."
                },
                "answer": "A",
                "explanation": "Standard IV(B) requires written consent from **all parties involved**—including both the employer and the party offering the outside compensation (ensuring the outside payer knows the employer approved and knows all terms/conditions, preventing hidden side arrangements). Moreover, prioritizing one client's return for a bonus risks breaching Standard III(B) Fair Dealing.",
                "distractors": {
                    "B": "Performance-based arrangements can be permitted if written consent is obtained from all parties and fair dealing across clients is protected.",
                    "C": "Standard IV(B) contains no USD 50,000 safe harbor."
                }
            },
            {
                "los": "Distinguish non-conflicting unpaid educational side activities from Standard IV(A)/IV(B) violations.",
                "question": "Hassan's free weekend educational podcast explaining basic compounding and bond math to university students with zero revenue and no investment recommendations:",
                "options": {
                    "A": "Violates Standard IV(B) Additional Compensation because it takes up weekend mental energy.",
                    "B": "Does not violate Standard IV(A) or Standard IV(B), as unpaid, non-competing personal educational activities outside work hours do not harm the employer or create conflicts (subject to firm social-media policy).",
                    "C": "Violates Standard VII(B) unless he removes all references to bond duration."
                },
                "answer": "B",
                "explanation": "Standard IV(A) and IV(B) do not prevent employees from pursuing outside hobbies, charitable activities, or unpaid general financial education on personal time, provided the activity does not compete with the employer, compromise work duties, use employer resources, or offer investment recommendations/solicitation.",
                "distractors": {
                    "A": "There is zero compensation and zero conflict of interest, so Standard IV(B) is not triggered.",
                    "C": "Teaching standard fixed-income concepts publicly does not implicate Standard VII(B)."
                }
            },
            {
                "los": "Evaluate whistleblowing vs. employer loyalty when senior leaders falsify financial valuations.",
                "question": "If Hassan reports the CIO's USD 180 million private-infrastructure valuation fraud to the national financial regulator after internal audit fails to act, his conduct:",
                "options": {
                    "A": "Violates Standard IV(A) Loyalty, because Sovereign Horizon is a national authority whose bond issuance could be disrupted.",
                    "B": "Is justified and permitted under Standard IV(A) Loyalty and supports Standards I(A) and I(D), because protecting market integrity and investors against ongoing fraud overrides employer secrecy.",
                    "C": "Violates Standard III(E) Preservation of Confidentiality regarding infrastructure partners."
                },
                "answer": "B",
                "explanation": "Under Standard IV(A) Loyalty, employee loyalty never requires concealing employer fraud. Whistleblowing to appropriate authorities to halt ongoing USD 180 million valuation fraud ahead of a public bond issuance protects market integrity and investors, aligning with the Code of Ethics and Standards I(A) and I(D).",
                "distractors": {
                    "A": "Disrupting a fraudulent bond offering protects capital markets—a core Code of Ethics mandate—rather than breaching legitimate employer loyalty.",
                    "C": "Standard III(E) permits disclosures concerning illegal activities or required by law."
                }
            },
            {
                "los": "Identify what constitutes valid 'written consent' under Standard IV(B).",
                "question": "According to Standard IV(B) guidance, which format qualifies as acceptable 'written consent'?",
                "options": {
                    "A": "Any form of written communication that can be documented and retained, including formal letters or official emails from authorized signatories.",
                    "B": "Strictly notarized paper affidavits signed in front of a judge.",
                    "C": "A casual verbal nod followed by a calendar invite."
                },
                "answer": "A",
                "explanation": "Under Standard IV(B), 'written consent' includes any documented, retrievable form of written communication (including email from authorized compliance/employer representatives and the outside party), not merely formal notarized contracts—while verbal nods never qualify.",
                "distractors": {
                    "B": "Notarized court affidavits are not required; documented emails or letters suffice.",
                    "C": "Verbal consent fails the explicit written-consent requirement of Standard IV(B)."
                }
            },
            {
                "los": "Explain why Standard IV(B) requires employer awareness of external compensation terms.",
                "question": "Why does Standard IV(B) require the member to disclose the exact terms and value of external compensation to their employer before accepting?",
                "options": {
                    "A": "So the employer can evaluate potential conflicts of interest, monitor time/independence compromises, and adjust supervisory oversight accordingly.",
                    "B": "So the employer can automatically confiscate 50% of the outside fee.",
                    "C": "So CFA Institute can tax the outside consulting income."
                },
                "answer": "A",
                "explanation": "Employer consent under Standard IV(B) allows the employer to evaluate whether the external compensation competes with firm interests, biases recommendations (e.g., favoring one client or vendor), or consumes excessive time/focus, and to institute supervisory safeguards.",
                "distractors": {
                    "B": "Standard IV(B) aims to manage conflicts and preserve independence, not confiscate employee fees.",
                    "C": "CFA Institute does not tax or collect members' external income."
                }
            }
        ]
    },
    # =========================================================================
    # V24: Professional Misconduct, Competence & Personal Integrity
    # =========================================================================
    {
        "vignette_id": "V24",
        "vignette_title": "Barrow & Finch Advisors: Misconduct, Competence, and Personal Integrity",
        "module": "Module 2: Guidance for Standards I-VII",
        "topic": "Professionalism",
        "subtopic": "Misconduct (I(D)) & Competence (I(E))",
        "vignette_text": (
            "Barrow & Finch Advisors is a multi-asset wealth management firm in Chicago employing three CFA charterholders: "
            "Kevin Walsh, CFA; Laura Diaz, CFA; and Samuel Grant, CFA. Last month, Walsh was arrested on a Saturday night "
            "for a first-time misdemeanor reckless driving offense after speeding on a rural highway; no one was injured, "
            "the case involved no dishonesty, fraud, or substance impairment during work hours, and Walsh promptly disclosed "
            "it on his annual compliance attestation.\n\n"
            "By contrast, Laura Diaz regularly submits falsified restaurant and hotel receipts totaling USD 6,800 on her "
            "corporate expense reports—claiming client entertainment dinners that were actually personal family vacations—and "
            "on two occasions executed client equity rebalance trades on a Friday afternoon while visibly intoxicated after "
            "a three-hour alcohol lunch, causing mistaken order quantities.\n\n"
            "Meanwhile, Samuel Grant, a career municipal-bond specialist with zero training in digital assets, options "
            "volatility surfaces, or smart-contract custody, accepts a new mandate to manage a USD 40 million decentralized "
            "finance (DeFi) yield-farming and crypto-perpetuals portfolio for a family office without taking training, "
            "studying protocol mechanics, or partnering with a qualified specialist. Within three weeks, Grant loses "
            "USD 7.5 million after misunderstanding perpetual funding rates and sending collateral to an unverified bridge."
        ),
        "questions": [
            {
                "los": "Distinguish non-dishonest personal infractions from Standard I(D) Misconduct.",
                "question": "Walsh's Saturday-night first-time misdemeanor speeding infraction—involving no dishonesty, fraud, client harm, or workplace impairment—most likely:",
                "options": {
                    "A": "Violates Standard I(D) Misconduct, because any misdemeanor conviction automatically triggers CFA Institute revocation.",
                    "B": "Does NOT violate Standard I(D) Misconduct, because I(D) targets conduct involving dishonesty, fraud, deceit, or acts reflecting adversely on professional reputation, integrity, or competence.",
                    "C": "Violates Standard III(A) Loyalty, Prudence, and Care."
                },
                "answer": "B",
                "explanation": "Standard I(D) Misconduct prohibits behavior involving dishonesty, fraud, or deceit or committing any act that reflects adversely on professional reputation, integrity, or competence. An isolated minor personal speeding/traffic infraction unrelated to professional duties and devoid of deceit or client impact generally does not violate Standard I(D).",
                "distractors": {
                    "A": "CFA Institute distinguishes minor personal traffic/regulatory infractions without moral turpitude from acts involving fraud, dishonesty, or professional incompetence.",
                    "C": "Weekend personal driving has no connection to client portfolio loyalty or care."
                }
            },
            {
                "los": "Apply Standard I(D) Misconduct to expense-report falsification and impaired trading.",
                "question": "Laura Diaz's falsification of USD 6,800 in corporate expense receipts and execution of client trades while intoxicated violate:",
                "options": {
                    "A": "Standard I(D) Misconduct (both dishonesty/fraud in expense falsification and severe professional incompetence/impairment while trading) and Standard IV(A) / III(A).",
                    "B": "Standard IV(B) Additional Compensation only.",
                    "C": "Nothing regarding the expense reports, because expense reimbursement is an HR matter unrelated to investing."
                },
                "answer": "A",
                "explanation": "Submitting falsified expense receipts is deliberate fraud/dishonesty against the employer (Standard I(D) Misconduct and Standard IV(A) Loyalty), while executing client trades while intoxicated directly jeopardizes client assets and reflects adversely on professional competence and integrity (Standards I(D), I(E), and III(A)).",
                "distractors": {
                    "B": "Fraudulent expense reimbursement is theft/dishonesty under I(D) and IV(A), not an external compensation agreement under IV(B).",
                    "C": "Acts of fraud or dishonesty even in internal expense reporting directly reflect on professional integrity and violate Standard I(D)."
                }
            },
            {
                "los": "Apply Standard I(E) Competence to accepting mandates outside one's technical expertise.",
                "question": "Accepting the USD 40 million DeFi yield-farming and crypto-perpetuals mandate without relevant knowledge, training, or specialist collaboration—leading to a USD 7.5 million operational loss—most directly violates:",
                "options": {
                    "A": "Standard I(E) Competence (and Standard V(A) Diligence and Reasonable Basis / Standard III(A) Prudence).",
                    "B": "Standard VI(C) Referral Fees.",
                    "C": "Standard VII(B) Reference to CFA Institute."
                },
                "answer": "A",
                "explanation": "Standard I(E) Competence explicitly requires members and candidates to act with and maintain the competence necessary to fulfill their professional responsibilities. Taking on an unfamiliar, complex crypto-perpetuals/DeFi mandate without acquiring the necessary expertise or engaging qualified specialists breaches Standard I(E), as well as Standards III(A) and V(A).",
                "distractors": {
                    "B": "No referral fee arrangement existed.",
                    "C": "No misuse of CFA designation occurred."
                }
            },
            {
                "los": "Determine compliant actions when asked to perform duties outside one's current competence under Standard I(E).",
                "question": "Before accepting the DeFi and crypto-perpetuals mandate, what should Samuel Grant have done to comply with Standard I(E) Competence?",
                "options": {
                    "A": "Decline the mandate, or transparently disclose his current lack of DeFi specialization and partner with/hire qualified technical specialists while completing rigorous training prior to investing client funds.",
                    "B": "Invest 10% of the portfolio immediately as a live 'learning experiment' with client capital.",
                    "C": "Have the family office sign a waiver stating Grant knows nothing about crypto."
                },
                "answer": "A",
                "explanation": "Under Standard I(E), when faced with responsibilities beyond current expertise, a member must either decline the engagement, obtain the requisite skills and knowledge before acting, or partner with/supervise demonstrably competent specialists—while communicating truthfully under Standard I(C) and V(B).",
                "distractors": {
                    "B": "Using USD 4 million of client funds as a live trial-and-error experiment violates Competence (I(E)), Prudence (III(A)), and Diligence (V(A)).",
                    "C": "A waiver does not absolve a fiduciary manager from the affirmative professional duty to act competently."
                }
            },
            {
                "los": "Evaluate personal bankruptcy vs. fraud under Standard I(D).",
                "question": "If a wealth manager experiences personal bankruptcy solely due to unforeseeable medical bills—with zero fraud, misappropriation of client money, or unlawful behavior—how does Standard I(D) view it?",
                "options": {
                    "A": "Personal bankruptcy resulting strictly from honest medical misfortune (without fraud or deceit) does not automatically violate Standard I(D), though transparent client/employer disclosure may be warranted if it affects duties.",
                    "B": "Any personal bankruptcy automatically constitutes Standard I(D) Misconduct.",
                    "C": "Personal bankruptcy violates Standard II(B) Market Manipulation."
                },
                "answer": "A",
                "explanation": "Standard I(D) focuses on dishonesty, fraud, deceit, or conduct demonstrating unfitness or reckless disregard in professional life. Honest financial hardship from unforeseen medical events—absent fraud, deceit, or mismanagement of client funds—does not per se constitute Standard I(D) misconduct.",
                "distractors": {
                    "B": "CFA Institute evaluates the circumstances surrounding bankruptcy; honest misfortune is distinct from fraudulent or deceitful insolvency.",
                    "C": "Personal medical bankruptcy has no relation to distorting securities markets under Standard II(B)."
                }
            },
            {
                "los": "Identify firm-wide supervisory responsibilities regarding impaired employees under Standard IV(C).",
                "question": "Upon learning that Laura Diaz traded client accounts while intoxicated and submitted falsified expense receipts, what is Barrow & Finch's management obligation under Standard IV(C)?",
                "options": {
                    "A": "Quietly subtract USD 6,800 from her paycheck and keep her on the trading desk.",
                    "B": "Immediately suspend Diaz's trading authority, audit all trades executed under impairment to make clients whole, conduct a full expense investigation, and enforce disciplinary termination/reporting per firm and regulatory policy.",
                    "C": "Ignore the expense fraud since clients were unaffected by the restaurant receipts."
                },
                "answer": "B",
                "explanation": "Under Standard IV(C), supervisors detecting serious dishonesty and impaired trading must take decisive immediate steps: suspend trading privileges, review and remediate any client harm, audit expense records thoroughly, and impose appropriate disciplinary and regulatory reporting actions.",
                "distractors": {
                    "A": "Leaving an impaired, dishonest trader on the desk exposes clients to continuing risk and violates Standard IV(C).",
                    "C": "Ignoring internal fraud tolerates a culture of noncompliance in direct violation of Standard IV(C)."
                }
            }
        ]
    },
    # =========================================================================
    # V25: Private Equity, Valuation Overrides & GIPS Private Markets
    # =========================================================================
    {
        "vignette_id": "V25",
        "vignette_title": "Ironbridge Growth Equity: Private Market Valuations and GIPS Reporting",
        "module": "Module 4: Global Investment Performance Standards (GIPS)",
        "topic": "Private Markets Valuation and GIPS",
        "subtopic": "PE Valuations, IRR/Multiples & AMC Section E",
        "vignette_text": (
            "Ironbridge Growth Equity is a GIPS-compliant private equity firm in London preparing to raise Ironbridge "
            "Fund IV (target GBP 800 million). Ahead of launching the Fund IV data room, Managing Partner Alistair Finch, "
            "CFA, reviews the Q4 valuations of Ironbridge Fund III (vintage 2021). An independent third-party valuation "
            "advisor valued Fund III's largest portfolio company, CloudRail Logistics, at 9.5x EBITDA based on depressed "
            "public logistics peers. Concerned that a flat mark will stall Fund IV marketing, Finch directs his valuation "
            "analyst to switch the valuation methodology mid-cycle to a 14.0x revenue multiple anchored to two high-flying "
            "US AI software firms, boosting Fund III's unrealized net IRR from 11.2% to 19.4%, without disclosing the "
            "methodology change or valuation override in the Q4 LP report.\n\n"
            "In Fund IV's marketing presentation, Ironbridge displays Fund III's 19.4% net since-inception IRR in large "
            "bold type on Slide 3, while completely omitting Fund III's Paid-In Capital (PIC), Distributed to Paid-In "
            "Capital (DPI), Residual Value to Paid-In Capital (RVPI), Total Value to Paid-In Capital (TVPI), and "
            "committed capital figures—and failing to distinguish realized distributions from unrealized paper marks. "
            "Additionally, Fund III's GIPS Report presents only time-weighted returns (TWR) calculated without external "
            "cash-flow timing adjustments, even though Ironbridge controls the timing of all LP capital calls and "
            "distributions in the closed-end illiquid fund.\n\n"
            "Finally, Ironbridge includes a separate 'Opportunistic Credit Carve-Out' table showing simulated levered "
            "deals alongside actual Fund II returns without labeling the simulation, and charges a monitoring fee from "
            "CloudRail directly to the portfolio company without offsetting it against Fund III's management fee or "
            "disclosing the fee retention to Fund III LPs."
        ),
        "questions": [
            {
                "los": "Apply Asset Manager Code Section E (Performance and Valuation) and Standard I(C) to valuation overrides.",
                "question": "Switching CloudRail Logistics from an independent 9.5x EBITDA mark to an unsubstantiated 14.0x US AI software multiple ahead of Fund IV fundraising without disclosure violates:",
                "options": {
                    "A": "AMC Section E (Performance and Valuation), Standard I(C) Misrepresentation, and Standard III(D) Performance Presentation.",
                    "B": "Nothing, because private equity GP committees retain absolute discretion over Level 3 fair value marks.",
                    "C": "Standard VI(C) Referral Fees."
                },
                "answer": "A",
                "explanation": "Under AMC Section E, GIPS Valuation Principles, and Standards I(C) and III(D), private market investments must be valued in good faith at fair value using objective, consistent methodologies. Arbitrarily swapping valuation multiples to inflate paper IRR ahead of new fundraising—without independent justification or disclosure—is fraudulent performance misrepresentation.",
                "distractors": {
                    "B": "GP valuation judgment must be objective, consistent, and grounded in fair value principles—never manipulated for marketing optics.",
                    "C": "No third-party referral payment is involved."
                }
            },
            {
                "los": "Identify required private-market return metrics and multiples under GIPS 2020.",
                "question": "For a closed-end private equity fund like Fund III where the firm controls cash flows, what return methodology and supplemental multiples does GIPS require in a GIPS Report?",
                "options": {
                    "A": "Time-weighted returns (TWR) only, with IRR optional.",
                    "B": "Since-inception money-weighted return (SI-MWR / IRR), alongside committed capital, paid-in capital (PIC), DPI, RVPI, TVPI, and public-market equivalent or since-inception benchmark metrics as applicable.",
                    "C": "Gross arithmetic average annual return without cash-flow multiples."
                },
                "answer": "B",
                "explanation": "Under GIPS 2020, when a firm controls external cash flows AND the strategy is closed-end, fixed-life, illiquid, or has a fixed commitment, the firm MUST present since-inception money-weighted returns (SI-MWR, i.e., net/gross IRR) and mandatory private-market multiples (PIC, DPI, RVPI, TVPI, committed capital) so LPs can see how much return is realized cash (DPI) versus unrealized paper marks (RVPI).",
                "distractors": {
                    "A": "TWR ignores capital-call timing controlled by the GP and is inappropriate as the sole return metric for closed-end private equity under GIPS.",
                    "C": "Arithmetic averages omit compounding and capital-call timing entirely."
                }
            },
            {
                "los": "Assess the omission of DPI and TVPI alongside headline IRR under Standard III(D) and I(C).",
                "question": "Displaying Fund III's inflated 19.4% net IRR in bold print while omitting DPI, RVPI, and TVPI misleads prospective LPs primarily because:",
                "options": {
                    "A": "LPs cannot determine whether the 19.4% IRR reflects actual realized cash distributions (DPI) or subjective, unrealized paper write-ups (RVPI), nor assess total cash-on-cash capital efficiency (TVPI).",
                    "B": "IRR must always be expressed on a monthly non-annualized basis.",
                    "C": "GIPS requires private equity funds to use Sharpe ratios instead of IRR."
                },
                "answer": "A",
                "explanation": "An early-life IRR can be heavily distorted by small early realizations or aggressive unrealized markups (RVPI). Presenting IRR without DPI, RVPI, and TVPI conceals the critical distinction between cash returned to LPs and subjective unrealized marks, violating GIPS and Standards I(C) and III(D).",
                "distractors": {
                    "B": "Since-inception IRR is annualized by standard convention.",
                    "C": "Sharpe ratios are unsuitable for illiquid private equity due to smoothed appraisal valuations."
                }
            },
            {
                "los": "Evaluate undisclosed portfolio-company monitoring fees under Standard VI(A), III(A), and AMC Section F.",
                "question": "Charging CloudRail a monitoring fee retained by Ironbridge without management-fee offset or disclosure to Fund III LPs violates:",
                "options": {
                    "A": "Standard VI(A) Avoid or Disclose Conflicts, Standard III(A) Loyalty, and AMC Section F (Disclosures), because hidden portfolio-company fees extract undisclosed economic value from LP equity.",
                    "B": "Standard VII(A) Conduct as Participants.",
                    "C": "Nothing, because CloudRail is a separate corporate entity outside Fund III."
                },
                "answer": "A",
                "explanation": "Monitoring fees charged to a fund's portfolio company reduce the enterprise value belonging to Fund III's LPs. Retaining such fees without explicit LPA disclosure and transparent fee-offset accounting creates an undisclosed double-dipping conflict violating Standards VI(A), III(A), and AMC Section F.",
                "distractors": {
                    "B": "Standard VII(A) relates strictly to CFA Program exam integrity.",
                    "C": "Because Fund III owns CloudRail, fees extracted by the GP from the portfolio company directly reduce LP investment returns."
                }
            },
            {
                "los": "Assess GIPS requirements regarding valuation frequency and hierarchy for private equity.",
                "question": "Under GIPS Valuation Principles for private market investments, how must Ironbridge value Fund III's underlying investments?",
                "options": {
                    "A": "At historical acquisition cost indefinitely until an exit occurs.",
                    "B": "In accordance with fair value principles at least annually (and for any period-end presented in the GIPS Report), applying a documented, consistent valuation hierarchy maximizing observable market inputs.",
                    "C": "Using whatever multiple the Managing Partner selects each quarter."
                },
                "answer": "B",
                "explanation": "GIPS requires all investments in GIPS-compliant portfolios to be valued at **fair value** (not historical cost) at least annually and at any period end for which performance is calculated, using consistent, documented valuation policies grounded in observable market inputs where available.",
                "distractors": {
                    "A": "Valuing private investments perpetually at historical cost violates GIPS fair value requirements.",
                    "C": "Arbitrary quarter-to-quarter multiple shifts violate valuation consistency and fair value integrity."
                }
            },
            {
                "los": "Identify the violation in mixing simulated deals with actual Fund II returns.",
                "question": "Including an unlabeled simulated 'Opportunistic Credit Carve-Out' table alongside actual Fund II performance violates:",
                "options": {
                    "A": "GIPS (prohibiting inclusion of model/hypothetical returns in GIPS-compliant composites/reports unless strictly separated as clearly labeled supplemental information) and Standard III(D)/I(C).",
                    "B": "Standard IV(B) Additional Compensation.",
                    "C": "Standard III(E) Preservation of Confidentiality."
                },
                "answer": "A",
                "explanation": "GIPS strictly forbids presenting simulated or hypothetical performance as actual GIPS-compliant performance; simulated results may only appear as clearly labeled supplemental information outside the compliant report table. Failing to label the simulation also violates Standards III(D) and I(C).",
                "distractors": {
                    "B": "No outside compensation arrangement is involved.",
                    "C": "Presenting simulated returns does not breach client data privacy."
                }
            }
        ]
    },
    # =========================================================================
    # V26: Fixed-Income Trading, New Issue Allocation & Soft-Dollar Abuse
    # =========================================================================
    {
        "vignette_id": "V26",
        "vignette_title": "Crescent Fixed Income Partners: New Issue Quid-Pro-Quo and Window Dressing",
        "module": "Module 2: Guidance for Standards I-VII",
        "topic": "Trading Integrity and Fiduciary Conduct",
        "subtopic": "Quid-Pro-Quo IPO Perks, Window Dressing & Timestamps",
        "vignette_text": (
            "Crescent Fixed Income Partners manages USD 5.1 billion across institutional bond funds and high-net-worth "
            "fixed-income SMAs in Boston. Senior corporate bond PM Victor Reyes, CFA, routinely directs USD 400 million "
            "of monthly investment-grade secondary bond orders to Titan Global Markets, even though Titan's bid-ask "
            "spreads are typically 3 to 5 basis points wider than competing electronic bond platforms. In return, Titan's "
            "equity syndicate desk silently allocates Reyes 1,000 shares of hot, oversubscribed tech IPOs into Reyes's "
            "personal brokerage account held outside Crescent, which Reyes flips on opening day for USD 65,000 in "
            "personal profits over the year.\n\n"
            "At the end of Q3, Crescent's flagship High-Income Corporate Fund lags its peer group median due to heavy "
            "exposure to distressed retail bonds. On September 29—one business day before Q3 holdings snapshots are "
            "published to institutional consultants—Reyes sells USD 80 million of distressed retail bonds and buys "
            "USD 80 million of AAA-rated sovereigns and blue-chip Apple corporate bonds, only to reverse the exact trades "
            "back into distressed retail bonds on October 2, incurring USD 480,000 in unnecessary transaction costs.\n\n"
            "Meanwhile, Crescent's fixed-income trading desk receives a scarce primary allocation of an oversubscribed "
            "new-issue investment-grade utility bond that trades up 1.8 points immediately on break. Rather than "
            "allocating the bonds pro rata across all suitable bond accounts, Reyes directs 100% of the allocation to "
            "Crescent's Flagship Fund (which charges a 15% performance fee) while giving zero bonds to Crescent's "
            "flat-fee SMA clients. Order allocation tickets are entered manually at the end of the day without "
            "pre-trade order timestamps."
        ),
        "questions": [
            {
                "los": "Evaluate quid-pro-quo personal IPO allocations from a broker under Standards I(B), III(A), and IV(B).",
                "question": "By paying Titan Global Markets wider spreads on client bond trades in exchange for personal hot-IPO equity allocations, Victor Reyes most directly violated:",
                "options": {
                    "A": "Standards I(B) Independence and Objectivity, III(A) Loyalty, Prudence, and Care, IV(B) Additional Compensation, and I(D) Misconduct.",
                    "B": "Standard VI(C) Referral Fees only.",
                    "C": "Nothing, because equity IPOs do not compete with corporate bond mandates."
                },
                "answer": "A",
                "explanation": "Directing client bond flow at worse execution (3–5 bps wider spreads) to secure USD 65,000 in personal equity IPO windfalls is classic commercial bribery/kickback abuse—compromising broker-selection objectivity (I(B)), breaching best-execution fiduciary duty (III(A)), taking undisclosed outside benefits (IV(B)), and engaging in dishonest conduct (I(D)).",
                "distractors": {
                    "B": "This is a hidden execution kickback rather than a disclosed client referral arrangement under VI(C).",
                    "C": "Personal enrichment paid in equity IPOs at the expense of client bond execution directly harms bond clients regardless of asset class."
                }
            },
            {
                "los": "Assess quarter-end 'window dressing' trades under Standards I(C), III(A), and II(B).",
                "question": "Executing the September 29 / October 2 round-trip bond swap costing clients USD 480,000 strictly to disguise distressed holdings on Q3 quarter-end snapshots constitutes:",
                "options": {
                    "A": "Permissible quarter-end portfolio rebalancing.",
                    "B": "Window dressing, which violates Standard I(C) Misrepresentation (deceiving consultants/clients about actual risk profile) and Standard III(A) Loyalty, Prudence, and Care (wasting USD 480,000 of client capital).",
                    "C": "Standard VII(A) Conduct as Participants."
                },
                "answer": "B",
                "explanation": "Quarter-end window dressing—temporarily dumping distressed assets right before a reporting snapshot and immediately repurchasing them afterward—deceives investors about true portfolio risk (Standard I(C)) and wastes USD 480,000 in needless transaction costs against clients' best interest (Standard III(A)).",
                "distractors": {
                    "A": "Genuine rebalancing reflects an updated investment outlook, whereas an immediately reversed round-trip trade serves solely deceptive cosmetic reporting.",
                    "C": "Standard VII(A) applies exclusively to CFA Program exam integrity."
                }
            },
            {
                "los": "Apply Standard III(B) Fair Dealing to allocating profitable new-issue bonds toward performance-fee accounts.",
                "question": "Allocating 100% of the oversubscribed utility bond issue to the 15%-performance-fee Flagship Fund while giving zero allocation to suitable flat-fee SMA clients violates:",
                "options": {
                    "A": "Standard III(B) Fair Dealing and Standard VI(A) Avoid or Disclose Conflicts.",
                    "B": "Standard III(E) Preservation of Confidentiality.",
                    "C": "Standard II(A) Material Nonpublic Information."
                },
                "answer": "A",
                "explanation": "Funneling profitable, oversubscribed primary issues exclusively to performance-fee accounts to boost firm incentive fees while starving flat-fee clients violates Standard III(B) Fair Dealing (which mandates pro-rata or objective fair allocation across all suitable accounts) and reveals an unmanaged fee-structure conflict under Standard VI(A).",
                "distractors": {
                    "B": "No client data confidentiality breach occurred.",
                    "C": "Allocating a public syndicate new issue does not involve inside corporate MNPI."
                }
            },
            {
                "los": "Evaluate the compliance failure of missing pre-trade allocation timestamps under Standard V(C) and III(B).",
                "question": "Entering fixed-income allocation tickets manually at end-of-day without pre-trade timestamps impairs compliance primarily because it:",
                "options": {
                    "A": "Allows portfolio managers to 'cherry-pick' winners retroactively after intraday price movement, preventing audit verification under Standard V(C) and Standard III(B).",
                    "B": "Prevents GIPS from calculating arithmetic returns.",
                    "C": "Violates Standard VII(B) trademark display rules."
                },
                "answer": "A",
                "explanation": "Pre-trade order specification and immutable timestamps (Standard V(C) and Standard III(B) / AMC Section C) are critical controls ensuring managers cannot wait until market close to steer intraday winners (like a +1.8 point new issue) into favored or performance-fee funds.",
                "distractors": {
                    "B": "Pre-trade timestamps govern allocation fairness and auditability, not GIPS arithmetic formulas.",
                    "C": "Order ticketing has no link to CFA trademark usage."
                }
            },
            {
                "los": "Identify supervisory controls needed to detect external brokerage accounts and kickbacks under Standard IV(C).",
                "question": "Which supervisory policy by Crescent's compliance department would most effectively prevent Reyes's concealed outside IPO account abuse?",
                "options": {
                    "A": "Requiring annual disclosure of all employee and beneficial brokerage accounts with duplicate trade confirmations, strict prohibition on personal IPO participation, and periodic best-execution TCA reviews.",
                    "B": "Allowing PMs to open outside equity accounts without reporting them since Crescent trades only fixed income.",
                    "C": "Asking Titan Global Markets verbally once a year whether they treat Crescent fairly."
                },
                "answer": "A",
                "explanation": "Under Standard IV(C) and VI(B), effective compliance requires full disclosure and duplicate statements of ALL employee brokerage accounts (regardless of asset class), strict bans or pre-clearance on personal hot-IPO participation (protecting against broker kickbacks), and independent Transaction Cost Analysis (TCA) monitoring spreads across brokers.",
                "distractors": {
                    "B": "Exempting equity accounts for bond PMs creates the exact blind spot Reyes exploited for USD 65,000 in kickbacks.",
                    "C": "Relying on the conflicted broker's verbal assurance fails independent supervisory verification."
                }
            },
            {
                "los": "Analyze best execution remedies when wider spreads lack research justification under Standard III(A).",
                "question": "When TCA reveals Crescent paid Titan 3–5 bps wider spreads on USD 400 million monthly volume without receiving superior liquidity or eligible client research, what fiduciary duty applies under Standard III(A)?",
                "options": {
                    "A": "Redirect flow to competitive electronic venues or dealers providing best execution and evaluate client restitution for unjustified execution drag.",
                    "B": "Continue using Titan to preserve relationship stability for another two years.",
                    "C": "Disclose the wider spreads in fine print without changing broker routing."
                },
                "answer": "A",
                "explanation": "Under Standard III(A) and AMC Section C (Trading), fiduciaries must seek best execution—maximizing client economic value—and immediately cease routing to a high-cost broker when wider spreads confer zero legitimate client benefit (while making clients whole for misconduct-related execution harm).",
                "distractors": {
                    "B": "Maintaining suboptimal execution for broker relationship convenience violates fiduciary duty.",
                    "C": "Disclosure does not excuse failing to seek best execution when personal kickbacks motivate worse fills."
                }
            }
        ]
    },
    # =========================================================================
    # V27: ESG & Impact Investing Claims, Greenwashing & Diligence
    # =========================================================================
    {
        "vignette_id": "V27",
        "vignette_title": "Verdant Impact Partners: ESG Greenwashing, Model Overrides, and Mandate Fidelity",
        "module": "Module 2: Guidance for Standards I-VII",
        "topic": "ESG Governance, Misrepresentation, and Investment Process",
        "subtopic": "Greenwashing, ESG Scoring & AMC Disclosures",
        "vignette_text": (
            "Verdant Impact Partners launches the 'Verdant Net-Zero Climate Transition Fund' (EUR 700 million) marketed "
            "to European pension plans. The fund's prospectus and sales brochures prominently state that the fund "
            "'excludes all companies deriving more than 5% of revenue from fossil-fuel extraction and applies a strict "
            "quantitative ESG threshold requiring every holding to score in the top quartile (75th percentile+) of "
            "Verdant's proprietary ESG scoring model.'\n\n"
            "Six months after launch, Verdant's Chief Investment Officer, Clara Holm, CFA, wants to buy a 4% position "
            "in PetroNord ASA, an oil and gas producer deriving 62% of revenue from offshore crude extraction, because "
            "she expects crude prices to rally. PetroNord scores in the 38th percentile on Verdant's proprietary ESG "
            "model. Rather than changing the prospectus or abstaining, Holm instructs her junior ESG analyst to adjust "
            "the weights of Verdant's ESG scoring rubric retroactively for the energy sector—boosting 'board diversity' "
            "and reducing 'Scope 1–3 carbon intensity' weight from 50% to 5%—until PetroNord's recalculated score clears "
            "the 76th percentile. Holm omits mentioning the 62% fossil-fuel revenue share in client materials.\n\n"
            "In Verdant's quarterly impact report, marketing presents a 'Portfolio Carbon Footprint 45% Below Benchmark' "
            "chart without disclosing that the metric excludes Scope 3 supply-chain emissions and substitutes estimated "
            "industry averages for 40% of holdings that do not report emissions data. Additionally, Verdant fails to "
            "explain in its risk disclosures how strict fossil-fuel exclusions alter sector weights and expose the fund "
            "to elevated tracking error during commodity inflation spikes."
        ),
        "questions": [
            {
                "los": "Identify ESG 'greenwashing' and mandate breaches under Standards I(C), III(C), and V(B).",
                "question": "Buying PetroNord ASA (62% fossil-fuel revenue) for a fund whose prospectus strictly bans >5% fossil-fuel revenue issuers violates:",
                "options": {
                    "A": "Standard I(C) Misrepresentation, Standard III(C) Suitability (adherence to stated fund mandate), and AMC Section B (Investment Process).",
                    "B": "Nothing, provided PetroNord outperforms the benchmark.",
                    "C": "Standard VI(C) Referral Fees."
                },
                "answer": "A",
                "explanation": "Buying an issuer deriving 62% of revenue from fossil-fuel extraction directly violates the fund's binding >5% exclusion limit—breaching mandate suitability (Standard III(C) / AMC Section B) and rendering the prospectus and marketing claims false (Standard I(C) Misrepresentation / greenwashing).",
                "distractors": {
                    "B": "Short-term positive performance never justifies breaching explicit binding prospectus exclusions and misleading investors.",
                    "C": "No referral fee arrangement is involved."
                }
            },
            {
                "los": "Evaluate post-hoc manipulation of proprietary ESG scoring models under Standards I(C), I(D), and V(A).",
                "question": "Retroactively re-weighting the ESG rubric to slash carbon-intensity weight from 50% to 5% solely so PetroNord reaches the 76th percentile violates:",
                "options": {
                    "A": "Standards I(C) Misrepresentation, I(D) Misconduct, V(A) Diligence and Reasonable Basis, and V(B) Communication with Clients.",
                    "B": "Standard VII(A) Conduct as Participants.",
                    "C": "Nothing, because proprietary ESG weights are non-public intellectual property that managers may tune daily."
                },
                "answer": "A",
                "explanation": "Manipulating a quantitative scoring model after the fact to force a desired stock purchase undermines objective diligence (V(A)), constitutes deceptive manipulation of stated ESG methodology (I(C) and I(D)), and fails to promptly disclose material changes to the investment process (V(B)).",
                "distractors": {
                    "B": "Standard VII(A) applies solely to CFA exam integrity.",
                    "C": "While legitimate model refinements are permitted with proper research and client disclosure under V(B), ad-hoc weight rigging to bypass an explicit mandate constraint is deceptive greenwashing."
                }
            },
            {
                "los": "Apply Standard V(B) and Standard I(C) to incomplete ESG data and Scope 3 omissions.",
                "question": "Advertising 'Portfolio Carbon Footprint 45% Below Benchmark' without disclosing the exclusion of Scope 3 emissions and the use of proxy estimates for 40% of holdings violates:",
                "options": {
                    "A": "Standard I(C) Misrepresentation and Standard V(B) Communication with Clients (omitting material methodological limitations and data-estimation assumptions).",
                    "B": "Standard II(A) Material Nonpublic Information.",
                    "C": "Standard IV(B) Additional Compensation."
                },
                "answer": "A",
                "explanation": "Under Standards I(C), V(A), and V(B), presenting ESG metrics requires transparent disclosure of scope boundaries (Scope 1/2 vs. Scope 3) and material reliance on estimated proxy data (40% of holdings) so institutional investors are not misled regarding data precision.",
                "distractors": {
                    "B": "Carbon footprint reporting methodologies do not involve corporate inside MNPI.",
                    "C": "No external employee compensation arrangement is involved."
                }
            },
            {
                "los": "Assess risk-disclosure obligations for ESG-constrained mandates under Standard V(B) and AMC Section F.",
                "question": "Failing to explain how strict sector exclusions increase tracking error relative to broad benchmarks during commodity inflation spikes breaches:",
                "options": {
                    "A": "Standard V(B) Communication with Clients and Prospective Clients and AMC Section F (Disclosures), which require disclosing significant risks and limitations of the investment process.",
                    "B": "Standard VI(B) Priority of Transactions.",
                    "C": "Standard III(E) Preservation of Confidentiality."
                },
                "answer": "A",
                "explanation": "Both Standard V(B) and Asset Manager Code Section F require managers to disclose significant investment process constraints and resulting portfolio risks—including sector concentration, benchmark tracking error, and factor biases produced by ESG screens.",
                "distractors": {
                    "B": "Tracking error disclosure does not involve personal vs. client trade priority.",
                    "C": "Disclosing strategy tracking-error risk exposes no confidential client information."
                }
            },
            {
                "los": "Identify the junior analyst's ethical duty when instructed to manipulate the ESG score under Standard I(A).",
                "question": "When ordered by CIO Clara Holm to alter the ESG model weights purely to qualify PetroNord for purchase, what must the junior ESG analyst do to comply with the Code and Standards?",
                "options": {
                    "A": "Follow Holm's order silently because a junior analyst owes obedience to the CIO under Standard IV(A).",
                    "B": "Refuse to manipulate the score or participate in deceptive reporting, escalate the issue to Verdant's Chief Compliance Officer, and dissociate from the PetroNord recommendation if management overrides controls.",
                    "C": "Quietly change the weightings for all energy firms equally so PetroNord appears less conspicuous."
                },
                "answer": "B",
                "explanation": "Under Standard I(A) Knowledge of the Law and Standard I(C) Misrepresentation, subordinates may never participate in unethical or unlawful deception on a superior's orders. The analyst must refuse the manipulative override, alert compliance, and dissociate from any false ESG report.",
                "distractors": {
                    "A": "Standard IV(A) employer loyalty never excuses participating in misrepresentation or mandate fraud.",
                    "C": "Disguising a manipulative override across an entire sector worsens the deception rather than fixing it."
                }
            },
            {
                "los": "Evaluate competence requirements in ESG integration under Standard I(E).",
                "question": "Under Standard I(E) Competence, if a generalist equity team launches a specialized Net-Zero Climate Transition product, what is required of the investment team?",
                "options": {
                    "A": "Possess or acquire substantive competence in climate-metric methodology, carbon accounting limits, and ESG data reliability—or partner with qualified ESG specialists.",
                    "B": "Purchase any commercial third-party ESG rating feed without understanding how scores are computed.",
                    "C": "Avoid reading corporate sustainability filings altogether."
                },
                "answer": "A",
                "explanation": "Standard I(E) requires investment professionals managing specialized ESG/climate mandates to maintain genuine technical competence in the analytical tools, emissions scopes, and data quality limitations underpinning their claims.",
                "distractors": {
                    "B": "Blindly relying on unexamined third-party ESG ratings violates both Standard I(E) Competence and Standard V(A) Diligence.",
                    "C": "Ignoring primary disclosures runs counter to V(A) thoroughness."
                }
            }
        ]
    },
    # =========================================================================
    # V28: Digital Assets, Algo Trading Failures & Error Handling
    # =========================================================================
    {
        "vignette_id": "V28",
        "vignette_title": "Helios Digital Asset Strategies: Algo Failure, Affiliate Liquidity, and Cyber Breach",
        "module": "Module 5: Asset Manager Code of Professional Conduct",
        "topic": "Technology Governance, Trading Errors, and Risk Controls",
        "subtopic": "Algo Risk, Cyber PII & AMC Section D",
        "vignette_text": (
            "Helios Digital Asset Strategies manages USD 600 million in institutional digital-asset and multi-asset SMA "
            "mandates in Singapore, claiming compliance with the CFA Institute Asset Manager Code (AMC). Portfolio manager "
            "and quant lead Nathan Vance, CFA, writes a new automated smart-order-routing execution script for tokenized "
            "treasury and ether liquidity pools. Eager to capture an arbitrage spread before the weekend, Vance deploys "
            "the script directly into live client SMA accounts without staging-environment testing, fat-finger order-size "
            "circuit breakers, or independent code review.\n\n"
            "Within twenty minutes, a decimal-place bug in Vance's routing script triggers oversized market orders across "
            "shallow decentralized liquidity pools, inflicting USD 920,000 in immediate slippage losses across 12 client "
            "SMAs. Panicking, Vance conceals the coding error from Helios's CCO and quietly re-allocates the worst "
            "USD 400,000 fills into two non-participating endowment accounts while labeling the remaining USD 520,000 "
            "loss on client statements as 'unexpected macro market volatility.'\n\n"
            "During the subsequent forensic audit, compliance discovers two more issues: (1) Helios routed 45% of its "
            "client over-the-counter digital-asset trades through Zenith Liquidity Ltd., an off-exchange market maker "
            "60%-owned by Helios's parent holding company, without disclosing the affiliation or comparing quotes from "
            "unaffiliated desks; and (2) three weeks earlier, an unencrypted laptop stolen from a Helios analyst exposed "
            "the unredacted KYC passports, bank routing numbers, and portfolio balances of 85 clients, which management "
            "decided not to disclose to affected clients or regulators to avoid bad press."
        ),
        "questions": [
            {
                "los": "Evaluate untested algorithmic deployment under Standards I(E), V(A), and AMC Section D.",
                "question": "Deploying the smart-order-routing script directly into live client SMAs without staging tests, circuit breakers, or peer review violates:",
                "options": {
                    "A": "Standard I(E) Competence, Standard V(A) Diligence, Standard III(A) Prudence, and AMC Section D (Risk Management, Compliance, and Support).",
                    "B": "Standard VII(B) Reference to CFA Institute.",
                    "C": "Nothing, because fast-moving digital arbitrage opportunities preclude pre-deployment testing."
                },
                "answer": "A",
                "explanation": "Releasing untested execution code lacking circuit breakers directly onto live client capital violates fiduciary care (III(A)), technical diligence/competence (V(A), I(E)), and AMC Section D operational risk-management controls.",
                "distractors": {
                    "B": "No reference to CFA Institute or the CFA designation occurred.",
                    "C": "Speed of market opportunities never justifies bypassing basic risk controls and staging tests with client assets."
                }
            },
            {
                "los": "Apply AMC Section C (Trading) and Standard I(D) to concealing coding losses and shifting trades.",
                "question": "Concealing the USD 920,000 coding loss by shifting USD 400,000 of bad fills onto two non-participating endowment accounts and mislabeling USD 520,000 as 'macro market volatility' violates:",
                "options": {
                    "A": "AMC Section C (Trading), Standard I(D) Misconduct, Standard I(C) Misrepresentation, and Standard III(A)/III(B).",
                    "B": "Standard VI(C) Referral Fees only.",
                    "C": "Standard IV(B) Additional Compensation."
                },
                "answer": "A",
                "explanation": "Under AMC Section C and Standards I(C), I(D), III(A), and III(B), trading/coding errors must be transparently reported, absorbed by the manager's own firm capital so clients are made whole, and NEVER concealed through fabricated statement explanations or dumped onto unaffected client accounts.",
                "distractors": {
                    "B": "No client referral payment is involved.",
                    "C": "Covering up firm coding losses is fraud and trading-error abuse, not external employee compensation."
                }
            },
            {
                "los": "Assess undisclosed affiliate liquidity routing under Standards VI(A), III(A), and AMC Sections C and F.",
                "question": "Routing 45% of OTC digital-asset trades through Zenith Liquidity Ltd. (60%-owned by Helios's parent) without disclosure or competitive quote checks violates:",
                "options": {
                    "A": "Standard VI(A) Avoid or Disclose Conflicts, Standard III(A) Best Execution, and AMC Sections C (Trading) and F (Disclosures).",
                    "B": "Standard II(A) Material Nonpublic Information.",
                    "C": "Nothing, provided Zenith Liquidity operates as a separate legal entity."
                },
                "answer": "A",
                "explanation": "Routing client orders to an affiliated market maker without competitive best-execution price checks (III(A) / AMC Section C) and without prominently disclosing the 60% parent-company ownership conflict (VI(A) / AMC Section F) breaches fiduciary care and conflict transparency.",
                "distractors": {
                    "B": "Affiliated routing is a conflict-of-interest and best-execution failure, not insider MNPI.",
                    "C": "Separate corporate incorporation does not erase an obvious parent-affiliate financial conflict of interest."
                }
            },
            {
                "los": "Evaluate cybersecurity breach and client PII concealment under Standard III(E), I(A), and AMC Section D.",
                "question": "Storing unencrypted client KYC passports and bank details on a laptop and concealing the theft from affected clients and regulators violates:",
                "options": {
                    "A": "Standard III(E) Preservation of Confidentiality, Standard I(A) Knowledge of the Law (applicable breach-notification rules), Standard I(D) Misconduct, and AMC Section D (Risk Management & Operational Controls).",
                    "B": "Standard III(D) Performance Presentation.",
                    "C": "Standard VI(B) Priority of Transactions."
                },
                "answer": "A",
                "explanation": "Standard III(E) and AMC Section D require robust cybersecurity controls (such as encryption) to safeguard client records, and concealing an unauthorized exposure of client passports and banking details violates confidentiality protection, applicable data-breach notification laws (Standard I(A)), and professional honesty (Standard I(D)).",
                "distractors": {
                    "B": "Client PII data breaches do not concern investment performance returns.",
                    "C": "No personal trading ahead of client orders occurred in the laptop theft."
                }
            },
            {
                "los": "Identify proper firm-level remediation for the USD 920,000 algorithmic trading error.",
                "question": "What immediate remediation must Helios execute to bring itself into compliance with AMC Section C and Standard III(A) regarding the USD 920,000 routing bug?",
                "options": {
                    "A": "Reverse the improper transfers out of the two endowment accounts, reimburse all 12 affected SMAs in full using Helios's firm capital, notify affected clients transparently, and suspend the routing script pending independent audit.",
                    "B": "Waive management fees for two months for the 12 SMAs while keeping the USD 400,000 allocation inside the endowment accounts.",
                    "C": "Amortize the USD 920,000 loss across all firm clients proportionally over 12 quarters."
                },
                "answer": "A",
                "explanation": "When a manager causes a trade or technology execution error, clients must be restored to the financial position they would have held absent the error, funded strictly from firm capital (never shifted onto other clients or smoothed silently via fee discounts that leave clients short).",
                "distractors": {
                    "B": "Leaving erroneous losing positions inside non-participating endowment accounts perpetuates unfair client harm.",
                    "C": "Spreading an internal firm coding loss across unrelated firm clients breaches fiduciary loyalty."
                }
            },
            {
                "los": "Determine Asset Manager Code Section D (Support) requirements for operational controls.",
                "question": "Under AMC Section D, which operational safeguard directly addresses the root cause of BOTH the unreviewed algo deployment and the stolen unencrypted laptop?",
                "options": {
                    "A": "Maintaining adequate operational, technological, and compliance resources—including written change-management, access-control, encryption, and periodic independent risk-control testing.",
                    "B": "Requiring all analysts to use personal smartphones for KYC verification.",
                    "C": "Outlawing OTC digital asset trading entirely."
                },
                "answer": "A",
                "explanation": "AMC Section D obligates managers to maintain sufficient operational and technological controls—including software change-management governance, cybersecurity/encryption standards, and periodic control testing—to protect client assets and confidential data.",
                "distractors": {
                    "B": "Personal devices heighten data leakage risk rather than establishing enterprise security.",
                    "C": "AMC Section D requires effective risk governance over authorized strategies rather than prohibiting specific asset classes."
                }
            }
        ]
    },
    # =========================================================================
    # V29: Outsourced CIO (OCIO), Endowment Governance & Fee Transparency
    # =========================================================================
    {
        "vignette_id": "V29",
        "vignette_title": "Meridian OCIO Services: Endowment Governance, Double Fees, and Rebates",
        "module": "Module 2: Guidance for Standards I-VII",
        "topic": "Fiduciary Duty, Fee Transparency, and Conflicts",
        "subtopic": "OCIO Governance, Layered Fees & Rebates",
        "vignette_text": (
            "Meridian OCIO Services acts as Outsourced Chief Investment Officer (OCIO) for the USD 1.5 billion "
            "Westfield University Endowment. Under Meridian's contract, Meridian charges a flat 35 bps advisory fee "
            "for managing asset allocation and external manager selection. Seeking to boost its operating margins, "
            "Meridian's managing director, Thomas Gray, CFA, recommends moving 30% (USD 450 million) of the endowment "
            "into 'Meridian Multi-Manager Alternatives LP,' an affiliated fund-of-funds managed by Meridian's own "
            "subsidiary. The affiliated fund-of-funds layers an additional 75 bps internal fund-of-funds management fee "
            "plus underlying hedge fund fees of 1.5%/20% on top of Meridian's 35 bps OCIO fee.\n\n"
            "In presenting the allocation to Westfield's Investment Committee, Gray omits the affiliated 75 bps layered "
            "fee from his headline fee summary slide, showing only the 35 bps OCIO fee and stating verbally that "
            "'external alternatives always carry underlying manager expenses.' Furthermore, for the endowment's remaining "
            "external credit managers hosted on the NovaPlatform custodial marketplace, NovaPlatform quietly pays "
            "Meridian a 12 bps administrative 'platform rebate' based on endowment assets held on NovaPlatform, which "
            "Meridian retains as corporate revenue without disclosing to Westfield's board.\n\n"
            "Two months later, Westfield's University Board Chair (who sits on the endowment committee) calls Gray "
            "privately and instructs him to divest all holdings in three local media companies critical of university "
            "administration immediately, even though the endowment's official IPS states that investment restrictions "
            "require a formal written resolution approved by the full Investment Committee."
        ),
        "questions": [
            {
                "los": "Apply Standard VI(A), III(A), and AMC Section F to affiliated fund-of-funds layered fees.",
                "question": "Moving USD 450 million into Meridian's own affiliated fund-of-funds while omitting the extra 75 bps internal layered fee from the headline OCIO fee presentation violates:",
                "options": {
                    "A": "Standard VI(A) Avoid or Disclose Conflicts, Standard III(A) Loyalty, Prudence, and Care, Standard I(C) Misrepresentation, and AMC Section F (Disclosures).",
                    "B": "Nothing, because underlying fund-of-funds expenses are legally distinct from the OCIO advisory fee.",
                    "C": "Standard VII(B) Reference to CFA Institute."
                },
                "answer": "A",
                "explanation": "Allocating OCIO client capital into an affiliated fund-of-funds creates a severe self-dealing fee conflict (more than tripling Meridian's direct fee from 35 bps to 110 bps before underlying manager fees). Omitting the affiliated 75 bps fee from the summary violates Standards VI(A), I(C), III(A), and AMC Section F fee transparency.",
                "distractors": {
                    "B": "A fiduciary OCIO cannot hide affiliated layered fees behind legal-entity separation when presenting total client fee burdens.",
                    "C": "No misuse of CFA designation occurred."
                }
            },
            {
                "los": "Evaluate undisclosed platform administrative rebates under Standards VI(C), VI(A), and III(A).",
                "question": "Accepting and retaining the undisclosed 12 bps platform rebate from NovaPlatform based on Westfield's endowment assets violates:",
                "options": {
                    "A": "Standards VI(A) Avoid or Disclose Conflicts, VI(C) Referral Fees, and III(A) Loyalty, Prudence, and Care.",
                    "B": "Standard II(B) Market Manipulation.",
                    "C": "Nothing, because NovaPlatform is a custodian rather than an investment manager."
                },
                "answer": "A",
                "explanation": "Receiving a 12 bps payment tied to directing client assets onto NovaPlatform is a direct financial conflict (VI(A)) and referral/placement compensation (VI(C)) that must be disclosed in nature and dollar/bps value before contracting—and under strict fiduciary OCIO duty (III(A)), hidden custodial rebates generally belong to the client or must be waived/credited back.",
                "distractors": {
                    "B": "Undisclosed platform rebates do not manipulate security market prices under II(B).",
                    "C": "Payments from custodians, platforms, or service providers tied to client asset placement trigger full disclosure duties under VI(A) and VI(C)."
                }
            },
            {
                "los": "Determine who holds legal/fiduciary authority to direct IPS changes in an institutional endowment under Standard III(A).",
                "question": "When Westfield's University Board Chair calls privately ordering immediate divestment of three media stocks—contrary to the IPS rule requiring a formal full Investment Committee resolution—Gray must:",
                "options": {
                    "A": "Execute the divestment immediately because the Board Chair holds top administrative seniority.",
                    "B": "Refuse to act on the unilateral private instruction, explain that the governing IPS requires formal Investment Committee approval, and bring any proposed restriction before the full committee.",
                    "C": "Sell half the shares quietly to appease the Chair partially."
                },
                "answer": "B",
                "explanation": "Under Standard III(A) Loyalty, Prudence, and Care, an institutional advisor's client is the *endowment entity itself as governed by its formal IPS and authorized Investment Committee*—NOT an individual board officer acting unilaterally outside governance rules for personal or political reasons.",
                "distractors": {
                    "A": "Executing an unauthorized political divestment on one individual's private phone call breaches IPS governance and fiduciary duty to the endowment.",
                    "C": "A partial unauthorized sale still violates IPS governance and fiduciary care."
                }
            },
            {
                "los": "Assess proper benchmark and fee-comparison transparency under Standard III(D) and V(B).",
                "question": "To fairly evaluate the affiliated fund-of-funds in compliance with Standard III(D) and V(B), Meridian's presentation to Westfield's Investment Committee must present:",
                "options": {
                    "A": "Only gross-of-all-fees returns compared against a 3-month Treasury bill index.",
                    "B": "Returns net of ALL fee layers (OCIO fee, affiliated 75 bps fund-of-funds fee, and underlying 1.5%/20% manager fees) compared against an appropriate risk-matched alternatives benchmark, alongside explicit total expense ratio projections.",
                    "C": "Gross returns before fees alongside a note that fees vary year to year."
                },
                "answer": "B",
                "explanation": "Standards III(D), V(B), and AMC Section F require fair, complete cost and performance comparison—showing the true all-in fee stack and net-of-all-fees impact against an appropriate risk/strategy benchmark so the Investment Committee can assess whether the affiliated product adds net alpha over direct manager selection.",
                "distractors": {
                    "A": "Comparing gross returns of illiquid alternatives to T-bills hides both fee drag and systematic equity/credit risk.",
                    "C": "Showing only gross returns without detailing the total layered fee drag conceals the true cost of the affiliated vehicle."
                }
            },
            {
                "los": "Identify best practice for mitigating OCIO self-dealing conflicts when recommending affiliated funds.",
                "question": "Under Standard VI(A) and AMC Section A/F, if an OCIO firm believes its own affiliated fund is genuinely superior for an endowment client, what governance safeguard is recommended?",
                "options": {
                    "A": "Fee waiver or dollar-for-dollar credit of the OCIO advisory fee on assets invested in affiliated vehicles, full written conflict/fee-stack disclosure, and explicit independent Investment Committee ratification.",
                    "B": "Requiring the endowment to sign a 10-year lockup before revealing the affiliated nature of the fund.",
                    "C": "Renaming the affiliated fund to remove 'Meridian' from its title."
                },
                "answer": "A",
                "explanation": "Best-practice OCIO fiduciary governance under Standards III(A) and VI(A) eliminates double-charging by waiving/crediting the base OCIO fee on affiliated sleeves, providing full written conflict and fee-stack disclosure, and securing informed ratification by the client's independent committee.",
                "distractors": {
                    "B": "Concealing affiliation prior to lockup commits severe misrepresentation and self-dealing.",
                    "C": "Disguising corporate ownership by stripping the firm's name worsens deception."
                }
            },
            {
                "los": "Apply the CFA Code of Ethics principle on placing client interests above personal/firm interests.",
                "question": "Across both the hidden 75 bps affiliated fee and the 12 bps NovaPlatform rebate, Gray's conduct most broadly violates which core principle of the CFA Institute Code of Ethics?",
                "options": {
                    "A": "Place the integrity of the investment profession and the interests of clients above their own personal (or firm) interests.",
                    "B": "Participate in local CFA society networking events annually.",
                    "C": "Encourage clients to adopt passive indexing."
                },
                "answer": "A",
                "explanation": "The CFA Institute Code of Ethics explicitly requires members to place the integrity of the investment profession and the *interests of clients* above their own personal or commercial self-interest—a foundational duty violated by concealed double-fee layering and secret rebates.",
                "distractors": {
                    "B": "Society event attendance is not a component of the Code of Ethics.",
                    "C": "The Code of Ethics is strategy-neutral (neither favoring active nor passive management)."
                }
            }
        ]
    },
    # =========================================================================
    # V30: Comprehensive Capstone: Multi-Standard Investment Firm Crisis
    # =========================================================================
    {
        "vignette_id": "V30",
        "vignette_title": "Vanguard Crest Capital: Integrated Multi-Standard Compliance Crisis",
        "module": "Module 3: Application of the Code and Standards: Level II",
        "topic": "Integrated Ethics Case Study",
        "subtopic": "Comprehensive Multi-Standard Capstone",
        "vignette_text": (
            "Vanguard Crest Capital (VCC) is a global multi-strategy asset manager with USD 8 billion in AUM claiming "
            "compliance with GIPS. During a tumultuous Q4 compliance audit triggered by an anonymous whistleblower, "
            "newly hired Chief Compliance Officer Maya Kapoor, CFA, uncovers five interconnected issues across VCC's "
            "divisions:\n\n"
            "First, star healthcare PM Lucas Meyer, CFA, who resigned on Friday to join a rival hedge fund, spent Thursday "
            "night downloading VCC's confidential client fee schedules and proprietary biotech clinical-trial database "
            "onto an encrypted USB drive. Second, healthcare analyst Nora Lin used an unvetted commercial AI chatbot "
            "to summarize an FDA advisory panel transcript and pasted a hallucinated survival-rate statistic into a live "
            "client note without reading the primary transcript; meanwhile, Lin also overheard a neighbor—who is general "
            "counsel at BioGenex—say on his patio telephone that BioGenex's board just approved an unannounced emergency "
            "USD 400 million dilutive equity raise, prompting Lin to short BioGenex immediately in her own personal IRA "
            "before issuing a downgrade.\n\n"
            "Third, VCC's Head of Equities, Grant Ellis, CFA, noticed automated pre-trade alerts showing Meyer repeatedly "
            "buying stocks in his spouse's account 20 minutes before VCC block buys over the prior six months, yet Ellis "
            "dismissed the alerts without inquiry because Meyer generated 40% of VCC's performance fees. Fourth, VCC's "
            "marketing head changed the start date of VCC's Global Healthcare GIPS Composite forward by nine months to "
            "drop a negative launch period and added the tagline 'VCC: Leading CFAs Delivering Guaranteed Outperformance.' "
            "Kapoor compiles a remediation plan for VCC's Board of Directors."
        ),
        "questions": [
            {
                "los": "Identify multiple Code and Standards violations committed by departing PM Lucas Meyer.",
                "question": "Lucas Meyer's Thursday-night download of VCC's confidential client fee schedules and proprietary biotech database onto a USB drive prior to Friday's resignation violates:",
                "options": {
                    "A": "Standard IV(A) Loyalty, Standard III(E) Preservation of Confidentiality, and Standard V(C) Record Retention (firm ownership of research records).",
                    "B": "Standard VII(A) Conduct as Participants.",
                    "C": "Nothing, because Meyer built the biotech database during his tenure at VCC."
                },
                "answer": "A",
                "explanation": "Taking an employer's confidential client fee schedules and proprietary biotech research database upon departure violates Standard IV(A) Loyalty (duty not to harm employer or misappropriate firm property), Standard III(E) (exposing confidential client fee data), and Standard V(C) (employer ownership of work-product records).",
                "distractors": {
                    "B": "Standard VII(A) governs CFA exam administration, not employer departure.",
                    "C": "Research models and databases built during employment belong to the employer, not the departing employee."
                }
            },
            {
                "los": "Distinguish analyst AI diligence errors from insider MNPI trading under Standards V(A), I(C), II(A), and VI(B).",
                "question": "Which statement accurately classifies Nora Lin's two distinct actions (pasting an AI-hallucinated FDA statistic AND shorting BioGenex in her personal IRA after overhearing BioGenex's general counsel)?",
                "options": {
                    "A": "The AI error violates Standard V(A)/I(C)/I(E), while shorting BioGenex on the overheard unannounced USD 400 million dilutive equity raise violates Standard II(A) MNPI (and Standard VI(B) Priority of Transactions).",
                    "B": "Overhearing a neighbor on his private patio renders the BioGenex equity raise public information exempt from Standard II(A).",
                    "C": "Neither violates the Standards because Lin acted hastily rather than intentionally."
                },
                "answer": "A",
                "explanation": "Publishing an unverified AI-fabricated FDA statistic breaches diligence (V(A)), AI governance competence (I(E)), and factual accuracy (I(C)). Overhearing confidential corporate inside information (an unannounced dilutive equity raise discussed by BioGenex's general counsel) is clearly MNPI under Standard II(A)—overhearing inadvertently never makes corporate inside news 'public'—and shorting personally ahead of any client downgrade also violates VI(B).",
                "distractors": {
                    "B": "Inadvertently overhearing confidential insider phone calls does NOT make the information public; Standard II(A) strictly prohibits trading on inadvertently received MNPI.",
                    "C": "Negligent failure to verify primary FDA sources breaches V(A), and intentional personal shorting on MNPI breaches II(A) and VI(B)."
                }
            },
            {
                "los": "Evaluate supervisory abdication driven by commercial revenue incentives under Standard IV(C).",
                "question": "Head of Equities Grant Ellis's dismissal of six months of pre-trade alerts showing Meyer front-running via his spouse's account because Meyer generated 40% of performance fees violates:",
                "options": {
                    "A": "Standard IV(C) Responsibilities of Supervisors (and Standard I(D) by enabling ongoing client harm for commercial gain).",
                    "B": "Standard VI(C) Referral Fees.",
                    "C": "Nothing, because spouses are separate taxpayers."
                },
                "answer": "A",
                "explanation": "Ignoring clear compliance alerts showing a star PM front-running client blocks via a spousal account—solely to protect 40% of firm fees—is an egregious failure of supervisory investigation and enforcement under Standard IV(C).",
                "distractors": {
                    "B": "No third-party referral fees are involved.",
                    "C": "Spousal accounts generally represent beneficial-ownership accounts under Standard VI(B), and separate tax status never excuses ignoring front-running alerts."
                }
            },
            {
                "los": "Identify GIPS, Misrepresentation, and CFA Designation violations in VCC's marketing tagline and composite revision.",
                "question": "Shifting the GIPS composite start date forward by nine months to hide an early loss and publishing 'VCC: Leading CFAs Delivering Guaranteed Outperformance' violates:",
                "options": {
                    "A": "GIPS composite-history rules, Standard III(D) Performance Presentation, Standard I(C) Misrepresentation, and Standard VII(B) Reference to the CFA Designation.",
                    "B": "Only Standard VII(B), because the tagline used 'CFAs' as a plural noun.",
                    "C": "Standard III(C) Suitability."
                },
                "answer": "A",
                "explanation": "Manipulating a GIPS composite inception date forward to drop negative performance violates GIPS rules and Standard III(D)/I(C). Meanwhile, the tagline violates Standard VII(B) twice ('CFAs' as a plural noun and claiming charterholders deliver superior performance) AND Standard I(C) ('Guaranteed Outperformance' guarantees inherently uncertain returns).",
                "distractors": {
                    "B": "Multiple distinct violations occurred across GIPS, III(D), I(C), and VII(B), not solely VII(B) noun usage.",
                    "C": "Marketing claims and composite inception manipulation do not involve client IPS suitability."
                }
            },
            {
                "los": "Prioritize CCO Maya Kapoor's crisis remediation sequence under Standards I(A), III(A), IV(C), and GIPS.",
                "question": "In presenting her remediation plan to VCC's Board of Directors, which immediate set of actions is highest priority for Kapoor to fulfill fiduciary and regulatory duties?",
                "options": {
                    "A": "Wait until annual external verification next spring to address all five items together.",
                    "B": "Freeze BioGenex trading and isolate Lin; quantify client slippage harm from Meyer's spousal front-running to make affected clients whole from firm capital; demand legal action/return of Meyer's stolen client/research data and notify affected clients of any confidentiality breach; retract and correct the altered GIPS report and marketing tagline immediately; and place Ellis under formal supervisory review/discipline.",
                    "C": "Fire the whistleblower first to preserve workplace morale."
                },
                "answer": "B",
                "explanation": "Effective crisis governance under Standards I(A), III(A), III(E), IV(C), VI(B), VII(B), and GIPS requires immediate containment (trading restrictions, retracting false marketing/GIPS reports, securing stolen client data), transparent remediation (reimbursing front-run clients from firm capital, correcting AI hallucinations), and supervisory accountability (disciplining Ellis and Meyer).",
                "distractors": {
                    "A": "Delaying remediation until next spring perpetuates ongoing fraud, MNPI exposure, and GIPS violations.",
                    "C": "Retaliating against a whistleblower violates integrity, ethical culture, and frequently whistleblower protection laws (I(A))."
                }
            },
            {
                "los": "Assess Kapoor's personal ethical mandate if VCC's Board refuses to remediate the crisis.",
                "question": "If VCC's Board of Directors rejects Kapoor's remediation plan and instructs her to leave the altered GIPS start date and unaddressed front-running losses concealed, what must Kapoor do under Standards I(A), I(D), and IV(C)?",
                "options": {
                    "A": "Document her dissent silently in a locked drawer and stay as CCO for another two years.",
                    "B": "Dissociate immediately from the ongoing violations (including refusing to sign regulatory compliance attestations covering the false GIPS/trading records), evaluate mandatory regulatory reporting under local law, and resign if the firm refuses to cure the fraud.",
                    "C": "Issue a public press release posting all client account numbers and balances."
                },
                "answer": "B",
                "explanation": "Under Standards I(A), I(D), and IV(C), a compliance officer cannot acquiesce in ongoing securities fraud, unaddressed client harm, or falsified GIPS records. Kapoor must refuse to sign off on tainted attestations, dissociate from the violations, fulfill applicable regulatory reporting obligations, and resign if the Board refuses remediation.",
                "distractors": {
                    "A": "Remaining as CCO while presiding over active fraud and false claims makes her complicit under Standards I(A) and IV(C).",
                    "C": "Publishing confidential client account numbers and balances publicly violates Standard III(E); disclosures must go only to authorized regulators/affected parties as appropriate."
                }
            }
        ]
    }
])


def build_questions() -> list[dict]:
    questions = []
    assert len(VIGNETTES) == 30, f"Expected 30 vignettes, got {len(VIGNETTES)}"
    seen_vids = set()
    for v_idx, v in enumerate(VIGNETTES, start=1):
        expected_vid = f"V{v_idx:02d}"
        vid = v["vignette_id"]
        assert vid == expected_vid, f"Expected {expected_vid}, got {vid}"
        assert vid not in seen_vids, f"Duplicate vignette {vid}"
        seen_vids.add(vid)
        gvid = f"ETH-{vid}"
        paras = [p.strip() for p in v["vignette_text"].split("\n\n") if p.strip()]
        assert 2 <= len(paras) <= 4, f"{vid}: Expected 2-4 paragraphs, got {len(paras)}"
        qs = v["questions"]
        assert len(qs) == 6, f"{vid}: Expected 6 questions, got {len(qs)}"
        for q_idx, q in enumerate(qs, start=1):
            qid = f"L2-ETH-{vid}-Q{q_idx}"
            # Deterministically balance answer choices evenly across A, B, and C
            target_ans = ("A", "B", "C")[(v_idx + q_idx) % 3]
            orig_ans = q["answer"]
            if target_ans != orig_ans and not any(
                w in q["options"][k] for k in ("A", "B", "C") for w in ("1 year.", "3 years.", "One way only", "Zero ways")
            ):
                rem_orig = [k for k in ("A", "B", "C") if k != orig_ans]
                rem_targ = [k for k in ("A", "B", "C") if k != target_ans]
                mapping = {orig_ans: target_ans, rem_orig[0]: rem_targ[0], rem_orig[1]: rem_targ[1]}
                options = {mapping[k]: q["options"][k] for k in ("A", "B", "C")}
                options = {k: options[k] for k in ("A", "B", "C")}
                distractors = {mapping[k]: q["distractors"][k] for k in rem_orig}
                answer = target_ans
            else:
                options = q["options"]
                distractors = q["distractors"]
                answer = orig_ans
            # Verify zero bare or stray dollar signs anywhere
            for field_name, val in [
                ("vignette_text", v["vignette_text"]),
                ("question", q["question"]),
                ("explanation", q["explanation"]),
                ("optA", options["A"]),
                ("optB", options["B"]),
                ("optC", options["C"]),
            ] + [(f"dist_{k}", val_d) for k, val_d in distractors.items()]:
                assert "$" not in val, f"{qid}.{field_name} contains disallowed '$'"
            add_l2(
                out=questions,
                qid=qid,
                subject=SUBJECT,
                module=v["module"],
                topic=v["topic"],
                subtopic=v["subtopic"],
                vignette_id=vid,
                global_vignette_id=gvid,
                vignette_title=v["vignette_title"],
                vignette_text=v["vignette_text"],
                los=q["los"],
                question=q["question"],
                options=options,
                answer=answer,
                explanation=q["explanation"],
                distractors=distractors,
            )
    return questions


def main():
    questions = build_questions()
    ans_counts = {k: sum(1 for q in questions if q["answer"] == k) for k in ("A", "B", "C")}
    print(f"Built {len(questions)} questions across {len(VIGNETTES)} vignettes (answers: {ans_counts})")
    save_validated_json(questions, OUTPUT_PATH)


if __name__ == "__main__":
    main()
