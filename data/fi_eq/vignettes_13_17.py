"""
Vignettes 13 to 17 for CFA Level 2 Fixed Income Question Bank.
Each vignette contains exactly 5 exam-grade clinical questions.
"""

VIGNETTES_13_17 = [
    # -------------------------------------------------------------------------
    # VIGNETTE 13
    # -------------------------------------------------------------------------
    {
        "id": "L2-FI-V13-Q1",
        "level": 2,
        "topic": "Fixed Income",
        "subtopic": "CDS Trading Strategies and Basis Trading",
        "vignette_id": "V13",
        "vignette_title": "Relative Value CDS Trading: Curve Steepeners, Flatteners, and Negative Basis Trades",
        "vignette_text": "Quantitative credit trader Maya Lin manages a long/short credit derivatives portfolio. She evaluates three distinct market opportunities: (1) an anticipated credit curve shift for Sovereign Tech, whose 1-year CDS trades at 80 bps and 5-year CDS trades at 220 bps, (2) a basis trade on Zenith Industrial, whose 5-year cash corporate bond trades at an asset swap spread (bond spread over swap) of 210 bps while its 5-year CDS spread is 160 bps, and (3) an index-to-single-name arbitrage between CDX IG and its underlying constituent single-name CDS.",
        "los": "Describe how credit default swaps are used to execute curve trades (curve steepeners and curve flatteners).",
        "question": "Maya expects Sovereign Tech's credit spread curve to flatten significantly over the next quarter due to near-term liquidity tightening. To execute a duration-neutral credit curve flattener trade, Maya should:",
        "options": {
            "A": "Buy short-term CDS protection and sell long-term CDS protection.",
            "B": "Sell short-term CDS protection and buy long-term CDS protection.",
            "C": "Sell both short-term and long-term CDS protection."
        },
        "answer": "A",
        "explanation": "A credit curve flattener profits when the spread difference between long-term and short-term credit spreads narrows (either short-term spreads widen faster, or long-term spreads tighten):\n- Buying short-term protection (long CDS) profits if short-term credit spreads widen.\n- Selling long-term protection (short CDS) profits if long-term credit spreads tighten or widen less.\nBy sizing the notional positions so that their spread durations offset (duration-neutral), the trader isolates the curve flattening movement while immunizing against parallel shifts in credit spreads.",
        "distractor_analysis": {
            "B": "Incorrect. Selling short-term protection and buying long-term protection creates a curve steepener trade, which profits if the curve steepens.",
            "C": "Incorrect. Selling protection across both maturities creates an outright long credit risk position (short spread duration), not a curve trade."
        }
    },
    {
        "id": "L2-FI-V13-Q2",
        "level": 2,
        "topic": "Fixed Income",
        "subtopic": "CDS Trading Strategies and Basis Trading",
        "vignette_id": "V13",
        "vignette_title": "Relative Value CDS Trading: Curve Steepeners, Flatteners, and Negative Basis Trades",
        "vignette_text": "Quantitative credit trader Maya Lin manages a long/short credit derivatives portfolio. She evaluates three distinct market opportunities: (1) an anticipated credit curve shift for Sovereign Tech, whose 1-year CDS trades at 80 bps and 5-year CDS trades at 220 bps, (2) a basis trade on Zenith Industrial, whose 5-year cash corporate bond trades at an asset swap spread (bond spread over swap) of 210 bps while its 5-year CDS spread is 160 bps, and (3) an index-to-single-name arbitrage between CDX IG and its underlying constituent single-name CDS.",
        "los": "Explain the concept of CDS basis and describe how to execute a negative basis trade.",
        "question": "The CDS basis is defined as $\\text{Basis} = \\text{CDS Spread} - \\text{Bond Spread}$. For Zenith Industrial, the CDS basis is $-50 \\text{ bps}$ ($160 - 210$). To exploit this negative basis, Maya should construct a trade that:",
        "options": {
            "A": "Sells the cash corporate bond short and sells CDS protection.",
            "B": "Buys the cash corporate bond and buys CDS protection.",
            "C": "Buys the cash corporate bond and sells CDS protection."
        },
        "answer": "B",
        "explanation": "The CDS-cash basis is defined as:\n$$\\text{Basis} = \\text{CDS Spread} - \\text{Bond Spread}$$\nFor Zenith Industrial, $\\text{Basis} = 160 \\text{ bps} - 210 \\text{ bps} = -50 \\text{ bps}$ (negative basis).\nA negative basis means the cash bond spread (210 bps) is higher than the CDS spread (160 bps); the cash bond is 'too cheap' relative to CDS protection. To exploit this:\n1. Buy the cash corporate bond (earning +210 bps over swap).\n2. Buy CDS protection (paying -160 bps).\nNet carry earned is $+210 \\text{ bps} - 160 \\text{ bps} = +50 \\text{ bps}$.\nDefault risk on the cash bond is hedged by the purchased CDS protection, creating an arbitrage-like positive net carry that profits as the basis converges toward zero.",
        "distractor_analysis": {
            "A": "Incorrect. Shorting the cash bond and selling CDS is a positive basis trade, used when the CDS spread exceeds the bond spread.",
            "C": "Incorrect. Buying both the cash bond and selling CDS doubles credit risk exposure rather than creating a hedged relative value trade."
        }
    },
    {
        "id": "L2-FI-V13-Q3",
        "level": 2,
        "topic": "Fixed Income",
        "subtopic": "CDS Trading Strategies and Basis Trading",
        "vignette_id": "V13",
        "vignette_title": "Relative Value CDS Trading: Curve Steepeners, Flatteners, and Negative Basis Trades",
        "vignette_text": "Quantitative credit trader Maya Lin manages a long/short credit derivatives portfolio. She evaluates three distinct market opportunities: (1) an anticipated credit curve shift for Sovereign Tech, whose 1-year CDS trades at 80 bps and 5-year CDS trades at 220 bps, (2) a basis trade on Zenith Industrial, whose 5-year cash corporate bond trades at an asset swap spread (bond spread over swap) of 210 bps while its 5-year CDS spread is 160 bps, and (3) an index-to-single-name arbitrage between CDX IG and its underlying constituent single-name CDS.",
        "los": "Describe the risks involved in negative basis trading.",
        "question": "Which of the following is a significant real-world risk that can prevent a negative basis trade from generating expected arbitrage profits?",
        "options": {
            "A": "Counterparty risk on the CDS protection seller and financing (repo) haircuts on the cash bond.",
            "B": "A parallel downward shift in benchmark government bond yields.",
            "C": "Failure of the corporate bond issuer to call its debt at par."
        },
        "answer": "A",
        "explanation": "Although a negative basis trade appears arbitrage-like on paper, it entails significant market and structural risks:\n1. Counterparty Risk: If the reference entity defaults, the CDS protection seller might also default or fail to honor collateral calls.\n2. Funding / Financing Risk: The cash bond is typically financed via repo. If lenders widen repo haircuts or increase repo borrowing rates, funding costs can exceed the positive basis carry.\n3. Restructuring / Contract Mismatch: Cash bond default terms may differ from ISDA credit event definitions or maturity dates.\n4. Mark-to-Market Liquidity Risk: The negative basis may widen further before converging, triggering margin calls.",
        "distractor_analysis": {
            "B": "Incorrect. Parallel shifts in benchmark yields affect both the cash bond and the swap hedge identically, leaving credit basis unaffected.",
            "C": "Incorrect. Straight bonds have fixed maturities; the absence of a call option does not impair the basis hedge."
        }
    },
    {
        "id": "L2-FI-V13-Q4",
        "level": 2,
        "topic": "Fixed Income",
        "subtopic": "CDS Trading Strategies and Basis Trading",
        "vignette_id": "V13",
        "vignette_title": "Relative Value CDS Trading: Curve Steepeners, Flatteners, and Negative Basis Trades",
        "vignette_text": "Quantitative credit trader Maya Lin manages a long/short credit derivatives portfolio. She evaluates three distinct market opportunities: (1) an anticipated credit curve shift for Sovereign Tech, whose 1-year CDS trades at 80 bps and 5-year CDS trades at 220 bps, (2) a basis trade on Zenith Industrial, whose 5-year cash corporate bond trades at an asset swap spread (bond spread over swap) of 210 bps while its 5-year CDS spread is 160 bps, and (3) an index-to-single-name arbitrage between CDX IG and its underlying constituent single-name CDS.",
        "los": "Describe the relationship between credit default swap indices and single-name credit default swaps.",
        "question": "Maya evaluates an index-to-single-name trade where the market-quoted spread of the CDX IG index is lower than the weighted average spread of its 125 individual single-name constituents (intrinsic index spread). To exploit this skew, Maya should:",
        "options": {
            "A": "Sell protection on the CDX IG index and buy protection on the individual constituents.",
            "B": "Buy protection on the CDX IG index and sell protection on the individual constituents.",
            "C": "Sell protection on both the index and the single-name constituents."
        },
        "answer": "B",
        "explanation": "When the quoted CDX index spread is less than the theoretical intrinsic spread (the weighted average of single-name spreads):\n$$\\text{Quoted Index Spread} < \\text{Intrinsic Index Spread}$$\n- The index protection is 'cheap' (undervalued spread).\n- Single-name protection is 'expensive' (overvalued spread).\nTo capture the spread differential (index skew arbitrage):\n1. Buy protection on the cheaper CDX IG index (paying the lower quoted spread).\n2. Sell protection on the basket of 125 single-name constituents (receiving the higher intrinsic spread).\nAs index pricing converges to intrinsic single-name pricing, the trader earns the positive net spread carry.",
        "distractor_analysis": {
            "A": "Incorrect. Selling index protection and buying single-name protection would pay the higher spread and receive the lower spread, incurring negative carry.",
            "C": "Incorrect. Selling protection on both creates unhedged systemic credit exposure."
        }
    },
    {
        "id": "L2-FI-V13-Q5",
        "level": 2,
        "topic": "Fixed Income",
        "subtopic": "CDS Trading Strategies and Basis Trading",
        "vignette_id": "V13",
        "vignette_title": "Relative Value CDS Trading: Curve Steepeners, Flatteners, and Negative Basis Trades",
        "vignette_text": "Quantitative credit trader Maya Lin manages a long/short credit derivatives portfolio. She evaluates three distinct market opportunities: (1) an anticipated credit curve shift for Sovereign Tech, whose 1-year CDS trades at 80 bps and 5-year CDS trades at 220 bps, (2) a basis trade on Zenith Industrial, whose 5-year cash corporate bond trades at an asset swap spread (bond spread over swap) of 210 bps while its 5-year CDS spread is 160 bps, and (3) an index-to-single-name arbitrage between CDX IG and its underlying constituent single-name CDS.",
        "los": "Describe how a synthetic corporate bond is created using credit default swaps and risk-free debt.",
        "question": "Which of the following portfolios synthetically replicates the cash flows and credit exposure of a fixed-rate corporate bond with par value USD 10 million?",
        "options": {
            "A": "Buying USD 10 million of risk-free Treasury bonds and buying USD 10 million of CDS protection on the corporate issuer.",
            "B": "Buying USD 10 million of risk-free Treasury bonds and selling USD 10 million of CDS protection on the corporate issuer.",
            "C": "Selling short USD 10 million of risk-free Treasury bonds and buying USD 10 million of CDS protection."
        },
        "answer": "B",
        "explanation": "A synthetic corporate bond is created by combining:\n1. A long position in a default-risk-free government bond (yielding the risk-free rate $r_f$).\n2. Selling CDS protection on the corporate issuer (receiving the CDS premium $s$).\nTotal cash flow earned:\n$$\\text{Synthetic Yield} = r_f + s$$\nIf the corporate entity defaults, the investor pays the default loss under the CDS contract ($1 - R$), exactly matching the default loss suffered on a cash corporate bond. Thus, investing in risk-free debt plus selling CDS protection perfectly replicates a long corporate bond.",
        "distractor_analysis": {
            "A": "Incorrect. Buying CDS protection eliminates credit risk, leaving the investor with an entirely risk-free return minus the CDS fee.",
            "C": "Incorrect. Shorting Treasuries and buying CDS creates a net short credit and liability position."
        }
    },

    # -------------------------------------------------------------------------
    # VIGNETTE 14
    # -------------------------------------------------------------------------
    {
        "id": "L2-FI-V14-Q1",
        "level": 2,
        "topic": "Fixed Income",
        "subtopic": "Collateralized Debt Obligations (CDOs)",
        "vignette_id": "V14",
        "vignette_title": "Cash Flow vs. Synthetic CDO Structuring, Subordination, and Correlation Sensitivity",
        "vignette_text": "Structured finance analyst Harrison Wells evaluates a USD 1 billion Collateralized Loan Obligation (CLO) backed by a diversified portfolio of leveraged corporate syndicated loans. The CLO structure consists of Senior AAA tranches (75% or USD 750 million), Mezzanine BBB tranches (15% or USD 150 million), and an unrated Subordinated Equity/First-Loss tranche (10% or USD 100 million). Harrison analyzes cash flow waterfall priority, overcollateralization (OC) and interest coverage (IC) coverage tests, and the sensitivity of tranche values to default correlation among collateral assets.",
        "los": "Describe the cash flow waterfall structure of a collateralized debt obligation.",
        "question": "In the standard cash flow waterfall of Harrison's CLO, how are principal losses and interest cash flows distributed across tranches?",
        "options": {
            "A": "Interest flows top-down (Senior $\\to$ Mezzanine $\\to$ Equity); default losses flow bottom-up (Equity $\\to$ Mezzanine $\\to$ Senior).",
            "B": "Interest flows bottom-up (Equity $\\to$ Mezzanine $\\to$ Senior); default losses flow top-down (Senior $\\to$ Mezzanine $\\to$ Equity).",
            "C": "Both interest flows and default losses are distributed pro-rata across all tranches."
        },
        "answer": "A",
        "explanation": "Structured credit products rely on subordination:\n1. Cash Flow / Interest Waterfall: Proceeds from the collateral pool are distributed strictly from top to bottom (Senior first, then Mezzanine, with residual excess spread flowing to Equity).\n2. Loss Allocation / Subordination Waterfall: Default losses are absorbed strictly from the bottom up. The Equity tranche (first-loss tranche) absorbs all losses up to its 10% subordination. Once equity is fully wiped out, the Mezzanine tranche absorbs further losses up to its 15% layer. Senior AAA tranches suffer losses only after cumulative collateral losses exceed 25% (10% + 15%).",
        "distractor_analysis": {
            "B": "Incorrect. Reverses the waterfall mechanics entirely; senior notes have legal priority on cash flows.",
            "C": "Incorrect. Pro-rata distribution describes a pass-through structure, not a tranched structured credit instrument."
        }
    },
    {
        "id": "L2-FI-V14-Q2",
        "level": 2,
        "topic": "Fixed Income",
        "subtopic": "Collateralized Debt Obligations (CDOs)",
        "vignette_id": "V14",
        "vignette_title": "Cash Flow vs. Synthetic CDO Structuring, Subordination, and Correlation Sensitivity",
        "vignette_text": "Structured finance analyst Harrison Wells evaluates a USD 1 billion Collateralized Loan Obligation (CLO) backed by a diversified portfolio of leveraged corporate syndicated loans. The CLO structure consists of Senior AAA tranches (75% or USD 750 million), Mezzanine BBB tranches (15% or USD 150 million), and an unrated Subordinated Equity/First-Loss tranche (10% or USD 100 million). Harrison analyzes cash flow waterfall priority, overcollateralization (OC) and interest coverage (IC) coverage tests, and the sensitivity of tranche values to default correlation among collateral assets.",
        "los": "Describe the effect of default correlation among collateral assets on the value of senior and equity tranches of a CDO.",
        "question": "If default correlation among the underlying leveraged loans in the collateral pool increases significantly, what is the expected impact on the values of the Senior AAA tranche and the Subordinated Equity tranche?",
        "options": {
            "A": "Senior AAA tranche value increases; Equity tranche value decreases.",
            "B": "Senior AAA tranche value decreases; Equity tranche value increases.",
            "C": "Both Senior and Equity tranche values decrease."
        },
        "answer": "B",
        "explanation": "Default correlation dictates the probability distribution of portfolio losses:\n- Low Correlation: Defaults are independent. It is very likely that a few loans will default, which wipes out the first-loss Equity tranche, but virtually impossible that enough loans default simultaneously to penetrate senior subordination. Thus, low correlation hurts Equity but protects Senior.\n- High Correlation: Assets default together in an 'all-or-nothing' cluster. With high correlation, there is a higher probability of zero defaults (which delivers maximum leveraged cash flows to Equity), while there is also a higher probability of catastrophic catastrophic default levels that breach subordination and destroy the Senior AAA tranche.\nTherefore, an increase in default correlation benefits the Equity tranche (call option on portfolio assets) and hurts the Senior AAA tranche.",
        "distractor_analysis": {
            "A": "Incorrect. Inverts correlation sensitivity; senior tranches lose value when correlation rises due to tail-risk contagion.",
            "C": "Incorrect. Equity tranche behaves like an option and gains value from the higher dispersion of extreme outcomes."
        }
    },
    {
        "id": "L2-FI-V14-Q3",
        "level": 2,
        "topic": "Fixed Income",
        "subtopic": "Collateralized Debt Obligations (CDOs)",
        "vignette_id": "V14",
        "vignette_title": "Cash Flow vs. Synthetic CDO Structuring, Subordination, and Correlation Sensitivity",
        "vignette_text": "Structured finance analyst Harrison Wells evaluates a USD 1 billion Collateralized Loan Obligation (CLO) backed by a diversified portfolio of leveraged corporate syndicated loans. The CLO structure consists of Senior AAA tranches (75% or USD 750 million), Mezzanine BBB tranches (15% or USD 150 million), and an unrated Subordinated Equity/First-Loss tranche (10% or USD 100 million). Harrison analyzes cash flow waterfall priority, overcollateralization (OC) and interest coverage (IC) coverage tests, and the sensitivity of tranche values to default correlation among collateral assets.",
        "los": "Describe the function of coverage tests (overcollateralization and interest coverage) in CDO structures.",
        "question": "What occurs within the CLO waterfall if the Overcollateralization (OC) test for the Senior tranche fails due to excessive loan defaults or CCC downgrades?",
        "options": {
            "A": "The CLO immediately enters bankruptcy liquidation and sells all collateral assets at market prices.",
            "B": "Cash flows normally destined for the subordinated equity tranche are diverted to pay down senior tranche principal until the test is cured.",
            "C": "Senior noteholders are required to inject additional equity capital into the Special Purpose Vehicle (SPV)."
        },
        "answer": "B",
        "explanation": "Overcollateralization (OC) and Interest Coverage (IC) tests are built-in credit enhancement mechanisms designed to protect senior noteholders. If loan collateral defaults or experiences deep market-value haircuts such that the OC test triggers a breach:\n1. Residual interest and principal distributions to junior/equity tranches are immediately shut off (cash flow diversion).\n2. These trapped funds are diverted to amortize and pay down the senior-most notes outstanding until the required OC test ratio is restored.\nThis deleverages the vehicle and fortifies the protection for senior noteholders.",
        "distractor_analysis": {
            "A": "Incorrect. An OC failure does not trigger liquidation; it redirects cash flows to pay down senior debt.",
            "C": "Incorrect. Debt noteholders never inject equity capital; their claims are non-recourse debt claims against the SPV."
        }
    },
    {
        "id": "L2-FI-V14-Q4",
        "level": 2,
        "topic": "Fixed Income",
        "subtopic": "Collateralized Debt Obligations (CDOs)",
        "vignette_id": "V14",
        "vignette_title": "Cash Flow vs. Synthetic CDO Structuring, Subordination, and Correlation Sensitivity",
        "vignette_text": "Structured finance analyst Harrison Wells evaluates a USD 1 billion Collateralized Loan Obligation (CLO) backed by a diversified portfolio of leveraged corporate syndicated loans. The CLO structure consists of Senior AAA tranches (75% or USD 750 million), Mezzanine BBB tranches (15% or USD 150 million), and an unrated Subordinated Equity/First-Loss tranche (10% or USD 100 million). Harrison analyzes cash flow waterfall priority, overcollateralization (OC) and interest coverage (IC) coverage tests, and the sensitivity of tranche values to default correlation among collateral assets.",
        "los": "Distinguish between cash flow CDOs and synthetic CDOs.",
        "question": "In contrast to a cash flow CLO that buys actual physical loans, a Synthetic CDO gains credit exposure to the reference portfolio by:",
        "options": {
            "A": "Selling credit protection via credit default swaps (CDS) and investing cash proceeds in high-quality sovereign collateral.",
            "B": "Purchasing call options on the equity shares of the reference corporations.",
            "C": "Issuing unsecured commercial paper without collateral backstops."
        },
        "answer": "A",
        "explanation": "A Synthetic CDO does not purchase physical cash bonds or syndicated loans. Instead:\n1. The Special Purpose Vehicle (SPV) sells credit protection on a selected portfolio of corporate reference entities via CDS to a financial institution, receiving CDS premium payments.\n2. The SPV issues notes to investors and invests the cash proceeds into high-quality, virtually risk-free collateral (such as Treasury bills or AAA sovereign bonds).\n3. If a credit event occurs in the reference portfolio, the SPV liquidates a portion of the sovereign collateral to pay the CDS protection buyer.\nThis allows the sponsor to transfer credit risk synthetically without financing physical asset purchases.",
        "distractor_analysis": {
            "B": "Incorrect. Synthetic CDOs reference debt credit risk via CDS, not equity call options.",
            "C": "Incorrect. Synthetic CDOs are heavily collateralized structured entities, not unsecured commercial paper."
        }
    },
    {
        "id": "L2-FI-V14-Q5",
        "level": 2,
        "topic": "Fixed Income",
        "subtopic": "Collateralized Debt Obligations (CDOs)",
        "vignette_id": "V14",
        "vignette_title": "Cash Flow vs. Synthetic CDO Structuring, Subordination, and Correlation Sensitivity",
        "vignette_text": "Structured finance analyst Harrison Wells evaluates a USD 1 billion Collateralized Loan Obligation (CLO) backed by a diversified portfolio of leveraged corporate syndicated loans. The CLO structure consists of Senior AAA tranches (75% or USD 750 million), Mezzanine BBB tranches (15% or USD 150 million), and an unrated Subordinated Equity/First-Loss tranche (10% or USD 100 million). Harrison analyzes cash flow waterfall priority, overcollateralization (OC) and interest coverage (IC) coverage tests, and the sensitivity of tranche values to default correlation among collateral assets.",
        "los": "Describe the economic characteristics and risk-return profile of the equity tranche in a CDO.",
        "question": "The Subordinated Equity tranche of Harrison's CLO is best characterized economically as:",
        "options": {
            "A": "A low-risk, fixed-annuity stream with senior bankruptcy priority.",
            "B": "A highly leveraged position that earns the excess spread between collateral interest and debt tranche coupons, with high sensitivity to first-loss defaults.",
            "C": "A zero-coupon bond that guarantees repayment of principal at maturity."
        },
        "answer": "B",
        "explanation": "The equity tranche represents the residual equity of the SPV. Because it is funded with only 10% capital while the vehicle holds 100% assets funded by 90% debt notes, the equity tranche achieves substantial financial leverage (~10:1). It captures the entire 'excess spread' (the difference between loan interest income and the lower interest paid to senior debt notes, minus fees). However, it bears 100% of all initial collateral default losses until its capital is exhausted, making it highly volatile and akin to an out-of-the-money call option.",
        "distractor_analysis": {
            "A": "Incorrect. The equity tranche has the lowest priority (first to lose, last to get paid) and is high risk, not low risk.",
            "C": "Incorrect. The equity tranche has no guaranteed principal and does not pay a zero-coupon fixed return."
        }
    },

    # -------------------------------------------------------------------------
    # VIGNETTE 15
    # -------------------------------------------------------------------------
    {
        "id": "L2-FI-V15-Q1",
        "level": 2,
        "topic": "Fixed Income",
        "subtopic": "Mortgage-Backed Securities and Prepayment Dynamics",
        "vignette_id": "V15",
        "vignette_title": "Agency CMO Tranches, Prepayment Speed (CPR/PSA), and Negative Convexity",
        "vignette_text": "Fixed-income strategist Evelyn Reed is modeling Agency Collateralized Mortgage Obligations (CMOs) backed by 30-year fixed-rate residential mortgages. She assesses prepayment dynamics using the Public Securities Association (PSA) benchmark. A mortgage pool with an outstanding balance of USD 50 million at the beginning of Month 20 experiences prepayments at 150% PSA. Evelyn models cash flow distributions across Sequential-Pay tranches, a Planned Amortization Class (PAC) tranche with companion support notes, and Interest-Only (IO) versus Principal-Only (PO) mortgage strips.",
        "los": "Calculate the single monthly mortality rate (SMM) from the conditional prepayment rate (CPR), and describe the PSA prepayment benchmark.",
        "question": "Under the standard 100% PSA benchmark, CPR begins at 0.2% in Month 1 and increases by 0.2% per month until reaching 6.0% at Month 30. For Evelyn's pool in Month 20 at 150% PSA, the annualized Constant Prepayment Rate (CPR) is closest to:",
        "options": {
            "A": "4.00%",
            "B": "6.00%",
            "C": "9.00%"
        },
        "answer": "B",
        "explanation": "1. At Month 20 under 100% PSA:\n$$\\text{CPR}_{100\\%} = 0.2\\% \\times 20 = 4.00\\%$$\n2. Under 150% PSA:\n$$\\text{CPR}_{150\\%} = 1.50 \\times 4.00\\% = 6.00\\%$$\n(Note: The single monthly mortality rate SMM is derived from CPR via $SMM = 1 - (1 - CPR)^{1/12} = 1 - (1 - 0.06)^{1/12} = 0.514\\%$.)",
        "distractor_analysis": {
            "A": "Incorrect. 4.00% is the CPR under the baseline 100% PSA benchmark ($0.2\\% \\times 20$).",
            "C": "Incorrect. 9.00% is computed using the terminal 30-month CPR ($1.50 \\times 6.0\\% = 9.0\\%$), but Month 20 is still in the ramp-up phase."
        }
    },
    {
        "id": "L2-FI-V15-Q2",
        "level": 2,
        "topic": "Fixed Income",
        "subtopic": "Mortgage-Backed Securities and Prepayment Dynamics",
        "vignette_id": "V15",
        "vignette_title": "Agency CMO Tranches, Prepayment Speed (CPR/PSA), and Negative Convexity",
        "vignette_text": "Fixed-income strategist Evelyn Reed is modeling Agency Collateralized Mortgage Obligations (CMOs) backed by 30-year fixed-rate residential mortgages. She assesses prepayment dynamics using the Public Securities Association (PSA) benchmark. A mortgage pool with an outstanding balance of USD 50 million at the beginning of Month 20 experiences prepayments at 150% PSA. Evelyn models cash flow distributions across Sequential-Pay tranches, a Planned Amortization Class (PAC) tranche with companion support notes, and Interest-Only (IO) versus Principal-Only (PO) mortgage strips.",
        "los": "Distinguish between contraction risk and extension risk in mortgage-backed securities.",
        "question": "When mortgage interest rates decline significantly, mortgage pass-through securities and sequential CMO tranches suffer predominantly from:",
        "options": {
            "A": "Contraction risk, because homeowners refinance early, accelerating principal repayments when reinvestment rates are low.",
            "B": "Extension risk, because homeowners delay prepayments, extending the life of the security.",
            "C": "Credit default risk, because lower interest rates increase homeowner default rates."
        },
        "answer": "A",
        "explanation": "Prepayment risks in mortgage-backed securities:\n1. Contraction Risk: Occurs when interest rates decline. Homeowners refinance their mortgages at lower rates, accelerating prepayments. The MBS investor receives principal back much faster than expected and must reinvest that cash at prevailing lower interest rates. This shortens the security's average life and truncates upside price appreciation.\n2. Extension Risk: Occurs when interest rates rise. Homeowners stop refinancing, prepayments plummet, and the average life of the MBS extends exactly when interest rates are high, causing substantial price declines.",
        "distractor_analysis": {
            "B": "Incorrect. Extension risk occurs when rates rise, not when rates fall.",
            "C": "Incorrect. Lower rates improve homeowner debt affordability; Agency MBS carry explicit or implicit sovereign guarantees against credit default."
        }
    },
    {
        "id": "L2-FI-V15-Q3",
        "level": 2,
        "topic": "Fixed Income",
        "subtopic": "Mortgage-Backed Securities and Prepayment Dynamics",
        "vignette_id": "V15",
        "vignette_title": "Agency CMO Tranches, Prepayment Speed (CPR/PSA), and Negative Convexity",
        "vignette_text": "Fixed-income strategist Evelyn Reed is modeling Agency Collateralized Mortgage Obligations (CMOs) backed by 30-year fixed-rate residential mortgages. She assesses prepayment dynamics using the Public Securities Association (PSA) benchmark. A mortgage pool with an outstanding balance of USD 50 million at the beginning of Month 20 experiences prepayments at 150% PSA. Evelyn models cash flow distributions across Sequential-Pay tranches, a Planned Amortization Class (PAC) tranche with companion support notes, and Interest-Only (IO) versus Principal-Only (PO) mortgage strips.",
        "los": "Describe the characteristics of planned amortization class (PAC) tranches and support/companion tranches.",
        "question": "A Planned Amortization Class (PAC) tranche is structured with an initial PAC collar of 100% to 250% PSA. If actual prepayments remain strictly within this collar over the life of the deal, which of the following statements is most accurate?",
        "options": {
            "A": "The PAC tranche's principal repayment schedule is perfectly maintained, while the companion/support tranches absorb all prepayment variability.",
            "B": "The companion tranches experience zero prepayments until the PAC tranche is completely retired.",
            "C": "The PAC tranche assumes all contraction risk, while companion tranches assume all extension risk."
        },
        "answer": "A",
        "explanation": "PAC tranches offer protection against both contraction risk and extension risk within a defined prepayment boundary (the PAC collar, e.g., 100%-250% PSA). The companion (support) tranches serve as shock absorbers: if prepayments surge, companion tranches absorb excess principal; if prepayments drop, companion tranches forego principal to keep the PAC principal amortization strictly on its predetermined schedule. Only when prepayments breach the collar bands (or companion tranches are completely paid off) does the PAC schedule break.",
        "distractor_analysis": {
            "B": "Incorrect. Companion tranches receive principal repayments to absorb excess prepayments while the PAC is being amortized.",
            "C": "Incorrect. The PAC tranche is protected from both contraction and extension risk; the companion tranches bear both risks."
        }
    },
    {
        "id": "L2-FI-V15-Q4",
        "level": 2,
        "topic": "Fixed Income",
        "subtopic": "Mortgage-Backed Securities and Prepayment Dynamics",
        "vignette_id": "V15",
        "vignette_title": "Agency CMO Tranches, Prepayment Speed (CPR/PSA), and Negative Convexity",
        "vignette_text": "Fixed-income strategist Evelyn Reed is modeling Agency Collateralized Mortgage Obligations (CMOs) backed by 30-year fixed-rate residential mortgages. She assesses prepayment dynamics using the Public Securities Association (PSA) benchmark. A mortgage pool with an outstanding balance of USD 50 million at the beginning of Month 20 experiences prepayments at 150% PSA. Evelyn models cash flow distributions across Sequential-Pay tranches, a Planned Amortization Class (PAC) tranche with companion support notes, and Interest-Only (IO) versus Principal-Only (PO) mortgage strips.",
        "los": "Describe the price sensitivity and effective duration characteristics of interest-only (IO) and principal-only (PO) mortgage strips.",
        "question": "When mortgage rates increase, what are the expected price movements of an Interest-Only (IO) strip and a Principal-Only (PO) strip derived from the same mortgage pool?",
        "options": {
            "A": "IO strip price decreases; PO strip price increases.",
            "B": "IO strip price increases (negative duration); PO strip price decreases (high positive duration).",
            "C": "Both IO and PO strip prices decrease because higher discount rates reduce present values."
        },
        "answer": "B",
        "explanation": "Mortgage strips have opposing cash flow reactions to interest rates:\n1. Interest-Only (IO) Strip: Receives only interest cash flows on the remaining pool balance. When interest rates rise, mortgage prepayments slow down dramatically, preserving the outstanding mortgage principal for a longer time. Because total interest collected is proportional to the outstanding balance, the total cash flows received by the IO investor increase significantly. This cash flow expansion outweighs the discount rate effect, causing the price of an IO strip to RISE when rates rise (giving IO strips negative effective duration).\n2. Principal-Only (PO) Strip: Receives principal repayments. When rates rise, prepayments slow and principal repayments are delayed further into the future, while discount rates rise. The PO strip suffers dual punishment and its price drops sharply (high positive duration).",
        "distractor_analysis": {
            "A": "Incorrect. Reverses the relationship; PO falls and IO rises when rates rise.",
            "C": "Incorrect. Fails to recognize that for an IO strip, the cash flow growth from slower prepayments dominates the discount rate increase."
        }
    },
    {
        "id": "L2-FI-V15-Q5",
        "level": 2,
        "topic": "Fixed Income",
        "subtopic": "Mortgage-Backed Securities and Prepayment Dynamics",
        "vignette_id": "V15",
        "vignette_title": "Agency CMO Tranches, Prepayment Speed (CPR/PSA), and Negative Convexity",
        "vignette_text": "Fixed-income strategist Evelyn Reed is modeling Agency Collateralized Mortgage Obligations (CMOs) backed by 30-year fixed-rate residential mortgages. She assesses prepayment dynamics using the Public Securities Association (PSA) benchmark. A mortgage pool with an outstanding balance of USD 50 million at the beginning of Month 20 experiences prepayments at 150% PSA. Evelyn models cash flow distributions across Sequential-Pay tranches, a Planned Amortization Class (PAC) tranche with companion support notes, and Interest-Only (IO) versus Principal-Only (PO) mortgage strips.",
        "los": "Explain why mortgage pass-through securities exhibit negative convexity.",
        "question": "The underlying structural cause of negative convexity in residential mortgage pass-through securities is that:",
        "options": {
            "A": "Homeowners hold an embedded American-style call option to prepay their mortgage at par value at any time.",
            "B": "Mortgage servicers hold a put option to force investors to buy back delinquent mortgages.",
            "C": "Agency MBS investors are granted a prepayment penalty fee when loans refinance early."
        },
        "answer": "A",
        "explanation": "A residential mortgage gives the homeowner the unrestricted legal right (an embedded call option) to prepay the outstanding loan principal at par value at any time without penalty. As mortgage interest rates drop, the homeowner's incentive to exercise this call option and refinance increases. For the MBS investor, who is short this prepayment call option ($V_{\\text{MBS}} = V_{\\text{bond}} - V_{\\text{prepayment call}}$), the bond's price appreciation is compressed near par, creating the classic negative convexity phenomenon.",
        "distractor_analysis": {
            "B": "Incorrect. Servicers do not hold put options on conforming mortgages.",
            "C": "Incorrect. Agency residential mortgages in the US typically carry zero prepayment penalties, which maximizes borrower prepayment optionality."
        }
    },

    # -------------------------------------------------------------------------
    # VIGNETTE 16
    # -------------------------------------------------------------------------
    {
        "id": "L2-FI-V16-Q1",
        "level": 2,
        "topic": "Fixed Income",
        "subtopic": "International Fixed Income Portfolio Management",
        "vignette_id": "V16",
        "vignette_title": "Cross-Border Bond Investing, Covered Interest Parity, and Hedged Returns",
        "vignette_text": "Global fixed-income portfolio manager Carlos Mendoza manages a EUR-denominated institutional fund investing in sovereign debt across the US, UK, and Eurozone. Carlos evaluates an investment in a 1-year US Treasury bill yielding 5.00% (USD). The current spot exchange rate is $S_{\\text{USD/EUR}} = 0.9200$ (meaning 1 USD = 0.9200 EUR). The 1-year forward exchange rate is $F_{\\text{USD/EUR}} = 0.9050$. Concurrently, a 1-year German Bund yields 3.30% (EUR). Carlos analyzes covered interest rate parity, currency hedging costs, and hedged versus unhedged return dynamics.",
        "los": "Calculate the hedged return on a foreign bond investment.",
        "question": "The fully hedged return in EUR of Carlos investing in the 1-year US Treasury bill is closest to:",
        "options": {
            "A": "3.29%",
            "B": "5.00%",
            "C": "6.74%"
        },
        "answer": "A",
        "explanation": "To calculate the fully currency-hedged return in the base currency (EUR):\n1. Investor starts with EUR and converts to USD at the spot rate $S_{\\text{USD/EUR}} = 0.9200$ (EUR per USD).\n2. Invests in US Treasury bill earning local return $R_{\\text{USD}} = 5.00\\%$.\n3. Simultaneously enters a forward contract to sell USD and buy EUR at the 1-year forward rate $F_{\\text{USD/EUR}} = 0.9050$.\nThe exact hedged return formula is:\n$$1 + R_{\\text{hedged, EUR}} = (1 + R_{\\text{USD}}) \\times \\frac{F_{\\text{USD/EUR}}}{S_{\\text{USD/EUR}}}$$\nSubstitute values:\n$$1 + R_{\\text{hedged, EUR}} = (1 + 0.05) \\times \\frac{0.9050}{0.9200} = 1.05 \\times 0.983696 = 1.03288$$\n$$R_{\\text{hedged, EUR}} = 1.03288 - 1 = 0.03288 = 3.29\\%$$\nNotice that because the USD trades at a forward discount against EUR ($F < S$, currency hedging cost of $\\approx -1.63\\%$), the hedged US Treasury return is 3.29%, which is virtually identical to the German Bund yield of 3.30% under covered interest parity.",
        "distractor_analysis": {
            "B": "Incorrect. 5.00% is the unhedged USD return, which completely ignores the currency hedging cost.",
            "C": "Incorrect. 6.74% results from mistakenly inverting the exchange rate fraction ($1.05 \\times \\frac{0.92}{0.905} - 1 = 6.74\\%$)."
        }
    },
    {
        "id": "L2-FI-V16-Q2",
        "level": 2,
        "topic": "Fixed Income",
        "subtopic": "International Fixed Income Portfolio Management",
        "vignette_id": "V16",
        "vignette_title": "Cross-Border Bond Investing, Covered Interest Parity, and Hedged Returns",
        "vignette_text": "Global fixed-income portfolio manager Carlos Mendoza manages a EUR-denominated institutional fund investing in sovereign debt across the US, UK, and Eurozone. Carlos evaluates an investment in a 1-year US Treasury bill yielding 5.00% (USD). The current spot exchange rate is $S_{\\text{USD/EUR}} = 0.9200$ (meaning 1 USD = 0.9200 EUR). The 1-year forward exchange rate is $F_{\\text{USD/EUR}} = 0.9050$. Concurrently, a 1-year German Bund yields 3.30% (EUR). Carlos analyzes covered interest rate parity, currency hedging costs, and hedged versus unhedged return dynamics.",
        "los": "Explain covered interest rate parity (CIRP) and the forward premium or discount.",
        "question": "Based on the exchange rates provided, the forward discount on the USD relative to EUR is approximately $-1.63\\%$. Under Covered Interest Rate Parity (CIRP), this forward discount approximates:",
        "options": {
            "A": "The foreign interest rate minus the domestic base interest rate ($r_{\\text{EUR}} - r_{\\text{USD}}$).",
            "B": "The domestic base interest rate minus the foreign interest rate ($r_{\\text{USD}} - r_{\\text{EUR}}$).",
            "C": "The expected inflation differential between the Eurozone and the United States."
        },
        "answer": "A",
        "explanation": "Under Covered Interest Rate Parity (CIRP), where exchange rates are expressed as Price/Base (here, EUR per 1 USD):\n$$\\frac{F - S}{S} \\approx r_{\\text{price}} - r_{\\text{base}} = r_{\\text{EUR}} - r_{\\text{USD}}$$\nHere, $r_{\\text{EUR}} - r_{\\text{USD}} = 3.30\\% - 5.00\\% = -1.70\\% \\approx -1.63\\%$.\nThe currency with the higher interest rate (USD at 5.00%) must trade at a forward discount relative to the currency with the lower interest rate (EUR at 3.30%) to eliminate riskless cross-border arbitrage.",
        "distractor_analysis": {
            "B": "Incorrect. Reverses the difference; the higher-yielding currency trades at a forward discount ($F < S$), not a forward premium.",
            "C": "Incorrect. The expected inflation differential represents Relative Purchasing Power Parity (RPPP), not Covered Interest Rate Parity."
        }
    },
    {
        "id": "L2-FI-V16-Q3",
        "level": 2,
        "topic": "Fixed Income",
        "subtopic": "International Fixed Income Portfolio Management",
        "vignette_id": "V16",
        "vignette_title": "Cross-Border Bond Investing, Covered Interest Parity, and Hedged Returns",
        "vignette_text": "Global fixed-income portfolio manager Carlos Mendoza manages a EUR-denominated institutional fund investing in sovereign debt across the US, UK, and Eurozone. Carlos evaluates an investment in a 1-year US Treasury bill yielding 5.00% (USD). The current spot exchange rate is $S_{\\text{USD/EUR}} = 0.9200$ (meaning 1 USD = 0.9200 EUR). The 1-year forward exchange rate is $F_{\\text{USD/EUR}} = 0.9050$. Concurrently, a 1-year German Bund yields 3.30% (EUR). Carlos analyzes covered interest rate parity, currency hedging costs, and hedged versus unhedged return dynamics.",
        "los": "Decompose the unhedged return on a foreign bond investment into local currency bond return and currency return.",
        "question": "If Carlos holds the 1-year US Treasury unhedged and over the 1-year horizon the USD depreciates by 4.00% against the EUR ($R_{\\text{FX}} = -4.00\\%$), Carlos's total return in EUR is closest to:",
        "options": {
            "A": "+0.80%",
            "B": "+1.00%",
            "C": "+9.00%"
        },
        "answer": "A",
        "explanation": "The exact total return in base currency (EUR) of an unhedged foreign bond investment is:\n$$R_{\\text{base}} = (1 + R_{\\text{local}}) \\times (1 + R_{\\text{FX}}) - 1$$\nGiven local return $R_{\\text{local}} = +5.00\\%$ and currency return $R_{\\text{FX}} = -4.00\\%$:\n$$R_{\\text{base}} = (1 + 0.05) \\times (1 - 0.04) - 1 = 1.05 \\times 0.96 - 1 = 1.008 - 1 = +0.008 = +0.80\\%$$\n(Using the linear approximation: $R_{\\text{base}} \\approx R_{\\text{local}} + R_{\\text{FX}} = 5.00\\% - 4.00\\% = +1.00\\%$; however, the exact compounding formula gives +0.80%).",
        "distractor_analysis": {
            "B": "Incorrect. +1.00% is the linear approximation ($5\\% - 4\\%$), which ignores the cross-product term ($0.05 \\times -0.04 = -0.20\\%$).",
            "C": "Incorrect. +9.00% assumes the USD appreciated by 4% rather than depreciated ($5\\% + 4\\% = 9\\%$)."
        }
    },
    {
        "id": "L2-FI-V16-Q4",
        "level": 2,
        "topic": "Fixed Income",
        "subtopic": "International Fixed Income Portfolio Management",
        "vignette_id": "V16",
        "vignette_title": "Cross-Border Bond Investing, Covered Interest Parity, and Hedged Returns",
        "vignette_text": "Global fixed-income portfolio manager Carlos Mendoza manages a EUR-denominated institutional fund investing in sovereign debt across the US, UK, and Eurozone. Carlos evaluates an investment in a 1-year US Treasury bill yielding 5.00% (USD). The current spot exchange rate is $S_{\\text{USD/EUR}} = 0.9200$ (meaning 1 USD = 0.9200 EUR). The 1-year forward exchange rate is $F_{\\text{USD/EUR}} = 0.9050$. Concurrently, a 1-year German Bund yields 3.30% (EUR). Carlos analyzes covered interest rate parity, currency hedging costs, and hedged versus unhedged return dynamics.",
        "los": "Describe the cross-currency basis spread and explain why covered interest rate parity fails in practice.",
        "question": "In global funding markets, the cross-currency basis spread measures deviations from covered interest parity. A persistently negative USD cross-currency basis spread indicates that:",
        "options": {
            "A": "Non-US market participants must pay a premium to borrow USD synthetically through FX swaps relative to direct interbank USD rates.",
            "B": "US Treasuries are trading at a lower yield than German Bunds.",
            "C": "Global banks have excess supply of USD cash looking for lending opportunities."
        },
        "answer": "A",
        "explanation": "A negative cross-currency basis spread (e.g., EUR/USD cross-currency basis) indicates that borrowing USD cash synthetically via FX swaps costs more than borrowing directly in the domestic cash market. This persistent deviation from Covered Interest Rate Parity reflects:\n1. Imbalances in global structural demand for USD assets.\n2. Regulatory leverage constraints and capital balance sheet costs that prevent global dealer banks from engaging in riskless CIP arbitrage.\nThus, non-US financial institutions pay a premium to borrow USD synthetically.",
        "distractor_analysis": {
            "B": "Incorrect. Cross-currency basis is an FX swap pricing spread, not a direct measure of sovereign yields.",
            "C": "Incorrect. A shortage of USD funding relative to heavy global demand causes the negative basis, not an excess supply of USD."
        }
    },
    {
        "id": "L2-FI-V16-Q5",
        "level": 2,
        "topic": "Fixed Income",
        "subtopic": "International Fixed Income Portfolio Management",
        "vignette_id": "V16",
        "vignette_title": "Cross-Border Bond Investing, Covered Interest Parity, and Hedged Returns",
        "vignette_text": "Global fixed-income portfolio manager Carlos Mendoza manages a EUR-denominated institutional fund investing in sovereign debt across the US, UK, and Eurozone. Carlos evaluates an investment in a 1-year US Treasury bill yielding 5.00% (USD). The current spot exchange rate is $S_{\\text{USD/EUR}} = 0.9200$ (meaning 1 USD = 0.9200 EUR). The 1-year forward exchange rate is $F_{\\text{USD/EUR}} = 0.9050$. Concurrently, a 1-year German Bund yields 3.30% (EUR). Carlos analyzes covered interest rate parity, currency hedging costs, and hedged versus unhedged return dynamics.",
        "los": "Evaluate the risk-return characteristics of currency hedging in international fixed-income portfolios.",
        "question": "For institutional investors holding high-quality global sovereign bond portfolios, empirical research demonstrates that fully currency hedging foreign bond exposures typically:",
        "options": {
            "A": "Substantially reduces portfolio volatility with minimal reduction in long-term expected returns.",
            "B": "Increases portfolio volatility because exchange rate volatility is lower than bond price volatility.",
            "C": "Completely eliminates sovereign duration risk."
        },
        "answer": "A",
        "explanation": "In sovereign fixed-income portfolios, foreign currency exchange rate volatility is typically 8% to 12% per year, which is significantly larger than the yield-driven price volatility of high-quality short-to-intermediate government bonds. Therefore, an unhedged international bond portfolio's total volatility is dominated by currency fluctuations. Fully hedging currency risk eliminates this massive FX volatility component while leaving the sovereign diversification benefits intact, resulting in a significantly higher Sharpe ratio over long horizons.",
        "distractor_analysis": {
            "B": "Incorrect. Currency volatility is far higher than high-quality bond volatility; hedging decreases overall portfolio volatility.",
            "C": "Incorrect. Currency hedging eliminates foreign exchange risk, but does not alter or eliminate the sovereign duration risk of the underlying bonds."
        }
    },

    # -------------------------------------------------------------------------
    # VIGNETTE 17
    # -------------------------------------------------------------------------
    {
        "id": "L2-FI-V17-Q1",
        "level": 2,
        "topic": "Fixed Income",
        "subtopic": "Active Fixed Income Portfolio Strategies",
        "vignette_id": "V17",
        "vignette_title": "Yield Curve Positioning, Barbell vs. Bullet, Butterfly Trades, and Riding the Curve",
        "vignette_text": "Chief Investment Officer Natasha Romanova oversees an active core-plus bond portfolio. Her research team forecasts that benchmark yield curves will experience high volatility and an increase in curvature (belly yields rise while wing yields fall) accompanied by a flattening slope. Natasha explores duration-neutral active strategies: comparing a Bullet portfolio (concentrated entirely in 5-year bonds) against a Barbell portfolio (split between 2-year and 10-year bonds) having identical effective duration and yield, and constructing a Butterfly spread trade.",
        "los": "Compare the convexity and performance of a barbell portfolio versus a bullet portfolio.",
        "question": "Given that Natasha's Barbell portfolio and Bullet portfolio have identical effective duration and yield to maturity, which of the following statements regarding their convexity and performance under large parallel yield shifts is most accurate?",
        "options": {
            "A": "The Barbell portfolio has higher convexity and will outperform the Bullet portfolio during large yield shifts in either direction.",
            "B": "The Bullet portfolio has higher convexity and will outperform the Barbell portfolio during large yield shifts in either direction.",
            "C": "Both portfolios have identical convexity because their effective durations are identical."
        },
        "answer": "A",
        "explanation": "Convexity is a function of the dispersion of cash flows around the portfolio duration. Because the Barbell portfolio has cash flows distributed far apart in the 2-year and 10-year maturities (high cash flow dispersion) compared to the Bullet portfolio whose cash flows are concentrated in the 5-year maturity (low cash flow dispersion), the Barbell portfolio strictly has HIGHER convexity than the Bullet portfolio for the same duration.\nDue to the convexity effect ($\\% \\Delta P \\approx -D \\Delta y + \\frac{1}{2} C (\\Delta y)^2$), the portfolio with higher convexity gains more when yields fall and loses less when yields rise. Therefore, the Barbell portfolio outperforms the Bullet portfolio during large yield shifts in either direction.",
        "distractor_analysis": {
            "B": "Incorrect. Bullet portfolios have lower dispersion of cash flows and consequently lower convexity than barbells.",
            "C": "Incorrect. Identical duration does not mean identical convexity; convexity depends on the second moment (dispersion) of cash flow timing."
        }
    },
    {
        "id": "L2-FI-V17-Q2",
        "level": 2,
        "topic": "Fixed Income",
        "subtopic": "Active Fixed Income Portfolio Strategies",
        "vignette_id": "V17",
        "vignette_title": "Yield Curve Positioning, Barbell vs. Bullet, Butterfly Trades, and Riding the Curve",
        "vignette_text": "Chief Investment Officer Natasha Romanova oversees an active core-plus bond portfolio. Her research team forecasts that benchmark yield curves will experience high volatility and an increase in curvature (belly yields rise while wing yields fall) accompanied by a flattening slope. Natasha explores duration-neutral active strategies: comparing a Bullet portfolio (concentrated entirely in 5-year bonds) against a Barbell portfolio (split between 2-year and 10-year bonds) having identical effective duration and yield, and constructing a Butterfly spread trade.",
        "los": "Construct and evaluate a butterfly trade based on expected changes in yield curve curvature.",
        "question": "To profit from an anticipated increase in yield curve curvature (where the 5-year belly yield rises relative to the 2-year and 10-year wing yields), Natasha should execute which duration-neutral butterfly trade?",
        "options": {
            "A": "Short the wings (Short 2-year, Short 10-year) and Long the belly (Long 5-year).",
            "B": "Long the wings (Long 2-year, Long 10-year) and Short the belly (Short 5-year).",
            "C": "Long 2-year bonds and Short 10-year bonds only."
        },
        "answer": "B",
        "explanation": "A butterfly trade consists of a barbell (the 'wings') and a bullet (the 'body' or 'belly'):\n- When curvature increases (the yield curve becomes more humped; belly yields rise relative to wing yields):\n  - 5-year bond prices fall relative to 2-year and 10-year bond prices.\n  - To profit, the manager shorts the underperforming belly (Short 5-year) and goes long the outperforming wings (Long 2-year, Long 10-year).\nThis is a 'Long Butterfly' (Long Wings, Short Belly) position. Position sizes are weighted so money duration equals zero (duration-neutral).",
        "distractor_analysis": {
            "A": "Incorrect. Shorting the wings and longing the belly is a Short Butterfly, which profits from decreasing curvature (flattening of the hump).",
            "C": "Incorrect. Long 2-year and Short 10-year is a 2s/10s curve flattener, not a 3-legged butterfly trade."
        }
    },
    {
        "id": "L2-FI-V17-Q3",
        "level": 2,
        "topic": "Fixed Income",
        "subtopic": "Active Fixed Income Portfolio Strategies",
        "vignette_id": "V17",
        "vignette_title": "Yield Curve Positioning, Barbell vs. Bullet, Butterfly Trades, and Riding the Curve",
        "vignette_text": "Chief Investment Officer Natasha Romanova oversees an active core-plus bond portfolio. Her research team forecasts that benchmark yield curves will experience high volatility and an increase in curvature (belly yields rise while wing yields fall) accompanied by a flattening slope. Natasha explores duration-neutral active strategies: comparing a Bullet portfolio (concentrated entirely in 5-year bonds) against a Barbell portfolio (split between 2-year and 10-year bonds) having identical effective duration and yield, and constructing a Butterfly spread trade.",
        "los": "Explain the carry and roll-down components of expected bond returns.",
        "question": "A 5-year annual-coupon bond has a coupon of 4.50% and trades at par. If the yield curve is upward sloping and the 4-year benchmark spot rate is 4.00%, assuming the yield curve remains completely unchanged over the next 12 months, the roll-down return (capital gain from rolling down the curve) is closest to:",
        "options": {
            "A": "+0.00%",
            "B": "+1.81%",
            "C": "+4.50%"
        },
        "answer": "B",
        "explanation": "Total expected return under an unchanged yield curve consists of carry (coupon income) plus roll-down return:\n1. Initial purchase price at $t = 0$: $P_0 = \\text{USD } 100.00$ (trades at par, yield = 4.50%).\n2. At $t = 1$, the bond becomes a 4-year bond. Because the yield curve is unchanged, the bond is priced at the 4-year rate of 4.00%:\n$$P_1 = \\sum_{t=1}^4 \\frac{4.50}{(1.04)^t} + \\frac{100}{(1.04)^4}$$\nUsing financial calculator / formula:\n$$P_1 = 4.50 \\times \\left[\\frac{1 - (1.04)^{-4}}{0.04}\\right] + \\frac{100}{(1.04)^4} = 4.50 \\times 3.629895 + 85.4804 = 16.3345 + 85.4804 = \\text{USD } 101.8149$$\n3. The roll-down return (capital appreciation due to aging down the upward sloping curve) is:\n$$\\text{Roll-down Return} = \\frac{P_1 - P_0}{P_0} = \\frac{101.8149 - 100.00}{100.00} = +1.8149\\% \\approx +1.81\\%$$\nTotal 1-year holding return would be $4.50\\% \\text{ (carry)} + 1.81\\% \\text{ (roll-down)} = 6.31\\%$.",
        "distractor_analysis": {
            "A": "Incorrect. +0.00% assumes zero roll-down return, which only occurs if the yield curve is perfectly flat.",
            "C": "Incorrect. +4.50% is the coupon carry return, not the roll-down capital appreciation."
        }
    },
    {
        "id": "L2-FI-V17-Q4",
        "level": 2,
        "topic": "Fixed Income",
        "subtopic": "Active Fixed Income Portfolio Strategies",
        "vignette_id": "V17",
        "vignette_title": "Yield Curve Positioning, Barbell vs. Bullet, Butterfly Trades, and Riding the Curve",
        "vignette_text": "Chief Investment Officer Natasha Romanova oversees an active core-plus bond portfolio. Her research team forecasts that benchmark yield curves will experience high volatility and an increase in curvature (belly yields rise while wing yields fall) accompanied by a flattening slope. Natasha explores duration-neutral active strategies: comparing a Bullet portfolio (concentrated entirely in 5-year bonds) against a Barbell portfolio (split between 2-year and 10-year bonds) having identical effective duration and yield, and constructing a Butterfly spread trade.",
        "los": "Describe the risks of riding the yield curve strategy.",
        "question": "What is the primary risk of an active strategy that rides an upward-sloping yield curve by purchasing bonds with longer maturities than the investment horizon?",
        "options": {
            "A": "Interest rates rise by more than implied by forward rates, causing capital losses that erase the excess carry and roll-down return.",
            "B": "The yield curve inverts overnight, which automatically triggers early redemption of all straight sovereign bonds.",
            "C": "Counterparty credit default risk on benchmark sovereign debt."
        },
        "answer": "A",
        "explanation": "Riding the yield curve generates excess returns if the yield curve is upward-sloping and rates remain static or rise by less than implied by the forward curve. However, if interest rates increase by more than the forward rates imply, the price decline of the longer-maturity bond over the holding period will exceed the extra carry and roll-down return, leading to underperformance relative to a maturity-matched risk-free zero.",
        "distractor_analysis": {
            "B": "Incorrect. Curve inversion does not trigger early redemption of straight sovereign debt.",
            "C": "Incorrect. Benchmark sovereign debt of major reserve currency issuers is assumed default-free; the risk is interest rate/duration risk, not default."
        }
    },
    {
        "id": "L2-FI-V17-Q5",
        "level": 2,
        "topic": "Fixed Income",
        "subtopic": "Active Fixed Income Portfolio Strategies",
        "vignette_id": "V17",
        "vignette_title": "Yield Curve Positioning, Barbell vs. Bullet, Butterfly Trades, and Riding the Curve",
        "vignette_text": "Chief Investment Officer Natasha Romanova oversees an active core-plus bond portfolio. Her research team forecasts that benchmark yield curves will experience high volatility and an increase in curvature (belly yields rise while wing yields fall) accompanied by a flattening slope. Natasha explores duration-neutral active strategies: comparing a Bullet portfolio (concentrated entirely in 5-year bonds) against a Barbell portfolio (split between 2-year and 10-year bonds) having identical effective duration and yield, and constructing a Butterfly spread trade.",
        "los": "Construct a duration-neutral yield curve steepener and flattener trade.",
        "question": "If Natasha anticipates a bear steepening of the yield curve (where yields rise across the curve, but long-term yields rise faster than short-term yields), which duration-neutral positioning using interest rate swaps is most appropriate?",
        "options": {
            "A": "Receive fixed in short-tenor swaps and pay fixed in long-tenor swaps, weighted to achieve zero net DV01.",
            "B": "Pay fixed in short-tenor swaps and receive fixed in long-tenor swaps, weighted to achieve zero net DV01.",
            "C": "Receive fixed across all tenors simultaneously."
        },
        "answer": "A",
        "explanation": "In an interest rate swap:\n- Paying fixed is equivalent to a short bond (profits when swap rates rise).\n- Receiving fixed is equivalent to a long bond (profits when swap rates fall).\nIn a steepener trade, long-term rates rise relative to short-term rates:\n1. Pay fixed in long-tenor swaps (profiting as long rates rise).\n2. Receive fixed in short-tenor swaps (profiting if short rates fall or rise less).\nBy weighting the notional amounts so that the dollar duration (DV01) of the short swap leg exactly cancels the DV01 of the long swap leg, the position is immunized against parallel curve shifts and generates net profits from curve steepening.",
        "distractor_analysis": {
            "B": "Incorrect. Paying fixed in short-tenor and receiving fixed in long-tenor creates a curve flattener trade.",
            "C": "Incorrect. Receiving fixed across all tenors is an outright bullish duration bet, not a duration-neutral curve trade."
        }
    }
]
