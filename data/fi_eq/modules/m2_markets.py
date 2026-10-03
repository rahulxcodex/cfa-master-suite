# -*- coding: utf-8 -*-
"""
Module 2: Fixed-Income Markets: Issuance, Trading, and Funding (Q15-Q26)
CFA Level 1 Fixed Income Question Bank
"""

M2_QUESTIONS = [
    {
        "id": "L1-FI-015",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Fixed-Income Markets: Issuance, Trading, and Funding",
        "los": "Describe classifications of fixed-income markets",
        "question": "A regional transportation authority with independent revenue-generating assets issues bonds that are not backed by the taxing power of the national government. These bonds are most accurately classified as:",
        "options": {
            "A": "Sovereign bonds.",
            "B": "Non-sovereign government bonds.",
            "C": "Quasi-government (agency) bonds."
        },
        "answer": "C",
        "explanation": "Quasi-government or agency bonds are issued by entities established or sponsored by governments, such as postal agencies, power authorities, or transportation financing agencies. While established by the government, they typically rely on specific operational enterprise revenues rather than direct national taxing power. In contrast, sovereign bonds are issued by central national governments, and non-sovereign government bonds are issued by state, provincial, or municipal political subdivisions.",
        "distractor_analysis": {
            "A": "Incorrect because sovereign bonds are issued by the central national government backed by its full faith and credit and national taxing power.",
            "B": "Incorrect because non-sovereign government bonds are issued by political subdivisions (provinces, states, municipalities) rather than standalone specialized authorities/agencies."
        }
    },
    {
        "id": "L1-FI-016",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Fixed-Income Markets: Issuance, Trading, and Funding",
        "los": "Describe the issuance of fixed-income securities",
        "question": "In an underwritten offering of corporate bonds (firm commitment), the primary underwriting risk is borne by:",
        "options": {
            "A": "The investment bank syndicate.",
            "B": "The issuing corporation.",
            "C": "The purchasing institutional investors."
        },
        "answer": "A",
        "explanation": "In an underwritten offering (also called a firm commitment offering), the investment bank or syndicate guarantees the sale of the bond issue at an agreed-upon offering price. The syndicate buys the entire issue from the issuer and re-sells it to the public. If market conditions deteriorate and the bonds cannot be sold at the offering price, the syndicate must absorb the financial loss. In a best-efforts offering, by contrast, the issuer bears the risk of unsold securities.",
        "distractor_analysis": {
            "B": "Incorrect because the issuing corporation is guaranteed proceeds in an underwritten offering; the issuer bears unsold risk in a best-efforts offering.",
            "C": "Incorrect because institutional investors only bear investment price risk after purchasing, not underwriting distribution risk."
        }
    },
    {
        "id": "L1-FI-017",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Fixed-Income Markets: Issuance, Trading, and Funding",
        "los": "Describe the issuance of fixed-income securities",
        "question": "A sovereign treasury conducts a single-price (Dutch) auction for USD 10 billion par value of 10-year bonds. Competitive bids are received as follows:\n- Bidder 1: USD 3 billion at 4.10%\n- Bidder 2: USD 4 billion at 4.15%\n- Bidder 3: USD 5 billion at 4.20%\n- Bidder 4: USD 2 billion at 4.25%\nWhich statement regarding the auction outcome is most accurate?",
        "options": {
            "A": "All winning bidders receive bonds at a clearing yield of 4.20%, with Bidder 3 receiving a partial allocation of USD 3 billion.",
            "B": "Bidder 1 receives bonds at 4.10%, Bidder 2 at 4.15%, and Bidder 3 at 4.20%.",
            "C": "The clearing yield is 4.25%, and all four bidders receive full allocations."
        },
        "answer": "A",
        "explanation": "In a single-price auction, bids are ranked from lowest yield (highest price) to highest yield until cumulative demand fulfills the offering amount:\n- Bidder 1: USD 3 billion (cumulative USD 3 billion)\n- Bidder 2: USD 4 billion (cumulative USD 7 billion)\n- Bidder 3: needs USD 3 billion out of USD 5 billion to hit USD 10 billion.\nThe highest accepted yield that clears the USD 10 billion offering is 4.20% (the stop-out or clearing yield). In a single-price auction, all winning competitive bidders (Bidders 1, 2, and the allocated portion of 3) pay the same price corresponding to the stop-out yield of 4.20%.",
        "distractor_analysis": {
            "B": "Incorrect because charging each bidder their specific bid yield describes a multiple-price auction, not a single-price (Dutch) auction.",
            "C": "Incorrect because the USD 10 billion offering is fully exhausted at 4.20%; Bidder 4 bid 4.25%, which is above the stop-out yield and receives zero allocation."
        }
    },
    {
        "id": "L1-FI-018",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Fixed-Income Markets: Issuance, Trading, and Funding",
        "los": "Describe fixed-income trading and settlement",
        "question": "Which of the following characteristics best describes the secondary market for most corporate and municipal bonds?",
        "options": {
            "A": "Continuous order-driven auctions on centralized public exchanges with tight bid-ask spreads.",
            "B": "Over-the-counter (OTC) quote-driven dealer markets with principal trading and variable liquidity.",
            "C": "Automated matching engines operating under strict T+0 instantaneous settlement."
        },
        "answer": "B",
        "explanation": "Unlike major equity markets, the vast majority of fixed-income trading occurs over the counter (OTC) in quote-driven dealer markets. Dealers trade for their own accounts (as principals) rather than merely acting as brokers. They provide liquidity by committing capital and quoting bid and ask prices. Due to the high number of unique bond issues, secondary trading in most corporate and municipal bonds is infrequent, leading to wider bid-ask spreads and lower liquidity relative to equities.",
        "distractor_analysis": {
            "A": "Incorrect because order-driven centralized exchanges are typical of public equities and exchange-traded derivatives, not corporate bonds.",
            "C": "Incorrect because standard bond settlement conventions are typically $T+1$ or $T+2$; instantaneous $T+0$ settlement is not standard practice."
        }
    },
    {
        "id": "L1-FI-019",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Fixed-Income Markets: Issuance, Trading, and Funding",
        "los": "Describe fixed-income trading and settlement",
        "question": "In government bond markets, an 'on-the-run' Treasury security typically trades at a lower yield than an otherwise identical 'off-the-run' Treasury security because the on-the-run security:",
        "options": {
            "A": "Possesses greater secondary market liquidity.",
            "B": "Carries zero exposure to inflation risk.",
            "C": "Has a significantly shorter remaining maturity."
        },
        "answer": "A",
        "explanation": "On-the-run securities are the most recently auctioned sovereign benchmark bonds of a given maturity. They are heavily traded by primary dealers, repo counterparties, and institutional investors, giving them superior liquidity and narrower bid-ask spreads. Investors are willing to pay a premium (resulting in a slightly lower yield) for this superior liquidity. Older issues with similar maturities are termed off-the-run and trade at a liquidity discount (higher yield).",
        "distractor_analysis": {
            "B": "Incorrect because on-the-run nominal Treasuries carry standard purchasing power and inflation risk.",
            "C": "Incorrect because an on-the-run 10-year Treasury has a slightly longer (full 10 years) maturity than off-the-run bonds issued earlier."
        }
    },
    {
        "id": "L1-FI-020",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Fixed-Income Markets: Issuance, Trading, and Funding",
        "los": "Describe sovereign, non-sovereign, and agency debt",
        "question": "Which of the following bonds typically carries an explicit guarantee of repayment from the national government?",
        "options": {
            "A": "A general obligation municipal bond issued by a city government.",
            "B": "A bond issued by a sovereign-guaranteed export-import bank.",
            "C": "A commercial paper note issued by a state-owned industrial enterprise without statutory backing."
        },
        "answer": "B",
        "explanation": "Certain government agency or quasi-government bonds, such as official export-import banks or multilateral development agencies, are backed by an explicit statutory sovereign guarantee. This means the national treasury is legally obligated to service the debt if the issuer defaults. General obligation municipal bonds (Option A) are backed solely by the local tax revenue of the city, not the national government. State-owned enterprises without explicit backing (Option C) carry only implicit support.",
        "distractor_analysis": {
            "A": "Incorrect because municipal GO bonds are backed by local municipal taxing authority, not the national government.",
            "C": "Incorrect because state-owned enterprises without statutory guarantees have only implicit government support, not an explicit legal guarantee."
        }
    },
    {
        "id": "L1-FI-021",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Fixed-Income Markets: Issuance, Trading, and Funding",
        "los": "Describe supranational debt securities",
        "question": "Which of the following institutions is most accurately classified as an issuer of supranational bonds?",
        "options": {
            "A": "The Federal National Mortgage Association (Fannie Mae).",
            "B": "The International Bank for Reconstruction and Development (World Bank).",
            "C": "The Bank of England."
        },
        "answer": "B",
        "explanation": "Supranational organizations are international entities established by multi-country treaties, such as the World Bank (IBRD), European Investment Bank (EIB), and Asian Development Bank (ADB). Bonds issued by these multilateral development institutions are supranational bonds, typically carrying high credit quality (AAA) and strong liquidity. Fannie Mae (Option A) is a US government-sponsored enterprise (agency). The Bank of England (Option C) is a central bank.",
        "distractor_analysis": {
            "A": "Incorrect because Fannie Mae is a national government-sponsored enterprise (GSE/agency), not an international supranational entity.",
            "C": "Incorrect because the Bank of England is a national central bank representing a single sovereign jurisdiction."
        }
    },
    {
        "id": "L1-FI-022",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Fixed-Income Markets: Issuance, Trading, and Funding",
        "los": "Describe corporate debt securities",
        "question": "Commercial paper (CP) issuers typically maintain a backup line of credit with commercial banks primarily to mitigate:",
        "options": {
            "A": "Interest rate duration risk.",
            "B": "Rollover (refinancing) risk.",
            "C": "Foreign exchange translation risk."
        },
        "answer": "B",
        "explanation": "Commercial paper is an unsecured, short-term promissory note issued by highly rated corporations, typically maturing within 1 to 270 days. Because issuers rely on continuously issuing new CP notes to pay off maturing notes (rolling over the debt), they face rollover risk if market liquidity abruptly freezes. Rating agencies therefore require CP issuers to maintain backup bank credit facilities (standby lines of credit) to guarantee repayment if rollover fails.",
        "distractor_analysis": {
            "A": "Incorrect because commercial paper has very short maturities, making interest rate duration risk negligible.",
            "C": "Incorrect because backup lines of credit provide immediate domestic cash liquidity, not foreign exchange currency hedging."
        }
    },
    {
        "id": "L1-FI-023",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Fixed-Income Markets: Issuance, Trading, and Funding",
        "los": "Describe corporate debt securities",
        "question": "A key distinction between a Medium-Term Note (MTN) program and a standard underwritten corporate bond issue is that MTNs:",
        "options": {
            "A": "Are offered continuously through dealers over time in customized maturities and sizes.",
            "B": "Must have an original maturity strictly between 5 and 10 years.",
            "C": "Are exempt from all securities registration and credit rating requirements."
        },
        "answer": "A",
        "explanation": "Under an MTN shelf registration program, issuers continuously offer debt securities through designated dealers with maturities ranging from months to decades. This allows the issuer to tailor maturities and coupon structures (including structured notes) to match investor demand on a reverse-inquiry basis. In contrast, standard corporate bonds are discrete, large one-off syndicated offerings.",
        "distractor_analysis": {
            "B": "Incorrect because despite the name 'medium-term', MTNs can have maturities ranging from 9 months to 30 years or more.",
            "C": "Incorrect because MTNs require shelf registration and are subject to securities regulation and rating agency scrutiny."
        }
    },
    {
        "id": "L1-FI-024",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Fixed-Income Markets: Issuance, Trading, and Funding",
        "los": "Describe short-term funding alternatives available to banks",
        "question": "A financial instrument created when a commercial bank guarantees payment on a commercial invoice or international trade draft is known as a:",
        "options": {
            "A": "Negotiable certificate of deposit.",
            "B": "Banker's acceptance.",
            "C": "Syndicated revolving credit facility."
        },
        "answer": "B",
        "explanation": "A banker's acceptance (BA) is a short-term promissory note representing a promised future payment by a bank, commonly used in international trade to finance import/export transactions. When the bank stamps 'accepted' on the trade draft, it becomes an unconditional liability of the bank and can be traded as a money market discount instrument.",
        "distractor_analysis": {
            "A": "Incorrect because a negotiable CD is a deposit receipt issued by a bank to raise wholesale funding, not an international trade draft guarantee.",
            "C": "Incorrect because a syndicated revolving facility is a committed credit line provided by a group of lenders to a corporate borrower."
        }
    },
    {
        "id": "L1-FI-025",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Fixed-Income Markets: Issuance, Trading, and Funding",
        "los": "Describe repurchase agreements (repos) and their uses",
        "question": "A securities dealer sells a government bond currently worth USD 10,000,000 to an institutional investor under a repurchase agreement with a 2.00% repo margin (haircut). The initial cash amount borrowed by the dealer is closest to:",
        "options": {
            "A": "USD 9,800,000.",
            "B": "USD 10,000,000.",
            "C": "USD 10,200,000."
        },
        "answer": "A",
        "explanation": "The repo margin (or haircut) is the percentage difference between the market value of the collateral security and the cash amount loaned: $$\\text{Cash Loaned} = \\text{Collateral Value} \\times (1 - \\text{Haircut})$$ $$\\text{Cash Loaned} = \\text{USD } 10{,}000{,}000 \\times (1 - 0.02) = \\text{USD } 9{,}800{,}000$$ This protective cushion shields the cash lender against adverse price movements in the collateral security.",
        "distractor_analysis": {
            "B": "Incorrect because USD 10,000,000 provides zero margin (0% haircut) to protect the lender against collateral price drops.",
            "C": "Incorrect because USD 10,200,000 mistakenly adds the haircut to the collateral value ($10{,}000{,}000 \\times 1.02$)."
        }
    },
    {
        "id": "L1-FI-026",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Fixed-Income Markets: Issuance, Trading, and Funding",
        "los": "Describe repurchase agreements (repos) and their uses",
        "question": "Which of the following factors will most likely result in a lower repurchase agreement (repo) rate for a borrower of funds?",
        "options": {
            "A": "The underlying collateral consists of low-liquidity corporate junk bonds.",
            "B": "The underlying collateral is an on-the-run Treasury note that is in extremely high demand ('on special').",
            "C": "The term of the repo agreement is extended from overnight to 90 days during a period of rising interest rates."
        },
        "answer": "B",
        "explanation": "When a specific security is in exceptionally high demand in the borrowing/financing market (described as trading 'on special'), lenders of cash are willing to accept an unusually low repo rate to obtain that specific collateral security. High-quality sovereign collateral already lowers repo rates relative to riskier collateral, and 'special' status lowers it even further.",
        "distractor_analysis": {
            "A": "Incorrect because lower-quality, illiquid collateral increases credit and liquidity risk for the cash lender, driving the repo rate higher.",
            "C": "Incorrect because longer terms generally carry higher repo rates due to greater term premium and rate uncertainty."
        }
    }
]
