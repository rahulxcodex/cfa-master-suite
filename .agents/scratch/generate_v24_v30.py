# -*- coding: utf-8 -*-
"""
generate_v24_v30.py
Generates Vignettes 24 through 30 (42 questions) for Topic 16: Analysis of Financial Institutions.
Strict currency compliance: USD, EUR, GBP, CHF, NOK, SGD, ZAR, ARS, LC.
Math equations use KaTeX delimiters. No bare dollar signs before digits.
"""

def get_vignettes_24_to_30():
    vignettes = []

    # =========================================================================
    # VIGNETTE 24: CAMELS Framework & Basel III Capital Adequacy
    # =========================================================================
    v24_text = (
        "Crestview Bancorp is a large commercial banking organization headquartered in Charlotte, "
        "North Carolina. Bank equity analyst Julian Mercer, CFA, is conducting a thorough analysis "
        "of Crestview's capital structure and regulatory solvency in accordance with the Basel III framework.\n\n"
        "Exhibit 1: Crestview Bancorp Capital & Balance Sheet Components (in billions of USD)\n"
        "Common stock and paid-in surplus: 22.0 billion USD\n"
        "Retained earnings: 18.0 billion USD\n"
        "Accumulated other comprehensive income (AOCI): 2.0 billion USD\n"
        "Goodwill and intangible assets: 4.0 billion USD\n"
        "Deferred tax assets exceeding regulatory deduction threshold: 1.0 billion USD\n"
        "Non-cumulative perpetual preferred stock (qualifying AT1): 5.0 billion USD\n"
        "Subordinated debt (original maturity > 5 years, qualifying Tier 2): 7.0 billion USD\n"
        "Qualifying general loan loss allowance includable in Tier 2: 3.0 billion USD\n\n"
        "Exhibit 2: Asset Portfolio & Basel III Risk Weights\n"
        "- Cash and central bank reserves: 50.0 billion USD (Risk Weight = 0%)\n"
        "- AAA-rated sovereign bonds: 80.0 billion USD (Risk Weight = 0%)\n"
        "- Qualifying residential mortgages: 120.0 billion USD (Risk Weight = 35%)\n"
        "- Commercial and industrial loans: 250.0 billion USD (Risk Weight = 100%)\n"
        "- Off-balance sheet trade letters of credit (credit conversion equivalent): 40.0 billion USD (Risk Weight = 50%)\n"
        "- Operational Risk RWA equivalent: 40.0 billion USD\n"
        "- Market Risk RWA equivalent: 48.0 billion USD\n\n"
        "Exhibit 3: Leverage Ratio Data\n"
        "- Total on-balance sheet accounting assets: 500.0 billion USD\n"
        "- Off-balance sheet regulatory exposure add-on: 60.0 billion USD\n"
        "- Total leverage exposure measure: 560.0 billion USD\n\n"
        "Mercer also reviews the minimum regulatory capital ratios under Basel III: Common Equity Tier 1 (CET1) "
        "minimum of 4.5%, Tier 1 Capital minimum of 6.0%, and Total Capital minimum of 8.0%, alongside a "
        "mandatory Capital Conservation Buffer of 2.5%."
    )

    v24_questions = [
        {
            "id": "L2-V24-Q1",
            "level": 2,
            "module": "m16-financial-institutions",
            "topic": "Analysis of Financial Institutions",
            "vignette_id": "V24",
            "vignette_title": "Crestview Bancorp: Basel III Capital Ratios & Capital Adequacy Analysis",
            "vignette_text": v24_text,
            "los": "LOS 16.a: Describe the CAMELS framework used to analyze financial institutions.",
            "question": "What is Crestview Bancorp's Common Equity Tier 1 (CET1) capital after regulatory deductions?",
            "options": {
                "A": "37.0 billion USD.",
                "B": "42.0 billion USD.",
                "C": "40.0 billion USD."
            },
            "answer": "A",
            "explanation": (
                "Common Equity Tier 1 (CET1) Capital consists of common stock plus paid-in surplus, retained earnings, "
                "and qualifying AOCI, minus mandatory regulatory deductions (such as goodwill, other intangibles, and disallowed deferred tax assets):\n"
                "$\\text{Gross Common Equity} = 22.0 + 18.0 + 2.0 = 42.0$ billion USD.\n"
                "$\\text{Regulatory Deductions} = \\text{Goodwill (4.0)} + \\text{Disallowed DTA (1.0)} = 5.0$ billion USD.\n"
                "$\\text{CET1 Capital} = 42.0 - 5.0 = 37.0$ billion USD.\n\n"
                "Distractor B (42.0 billion USD) fails to deduct goodwill and disallowed deferred tax assets.\n"
                "Distractor C (40.0 billion USD) deducts only AOCI."
            )
        },
        {
            "id": "L2-V24-Q2",
            "level": 2,
            "module": "m16-financial-institutions",
            "topic": "Analysis of Financial Institutions",
            "vignette_id": "V24",
            "vignette_title": "Crestview Bancorp: Basel III Capital Ratios & Capital Adequacy Analysis",
            "vignette_text": v24_text,
            "los": "LOS 16.b: Describe the Basel III regulatory capital requirements and calculate regulatory capital ratios.",
            "question": "Crestview Bancorp's total Risk-Weighted Assets (RWA) under Basel III is closest to:",
            "options": {
                "A": "312.0 billion USD.",
                "B": "400.0 billion USD.",
                "C": "540.0 billion USD."
            },
            "answer": "B",
            "explanation": (
                "Total Risk-Weighted Assets (RWA) equals Credit Risk RWA plus Operational Risk RWA plus Market Risk RWA:\n\n"
                "1. Credit Risk RWA:\n"
                "- Cash & central bank: $50.0 \\times 0\\% = 0.0$ billion USD.\n"
                "- Sovereign bonds: $80.0 \\times 0\\% = 0.0$ billion USD.\n"
                "- Residential mortgages: $120.0 \\times 35\\% = 42.0$ billion USD.\n"
                "- Commercial loans: $250.0 \\times 100\\% = 250.0$ billion USD.\n"
                "- Off-balance sheet commitments: $40.0 \\times 50\\% = 20.0$ billion USD.\n"
                "Total Credit Risk RWA = $0 + 0 + 42.0 + 250.0 + 20.0 = 312.0$ billion USD.\n\n"
                "2. Total RWA:\n"
                "$\\text{Total RWA} = \\text{Credit Risk RWA (312.0)} + \\text{Operational Risk (40.0)} + \\text{Market Risk (48.0)} = 400.0$ billion USD.\n\n"
                "Distractor A (312.0 billion USD) omits Operational Risk and Market Risk RWA."
            )
        },
        {
            "id": "L2-V24-Q3",
            "level": 2,
            "module": "m16-financial-institutions",
            "topic": "Analysis of Financial Institutions",
            "vignette_id": "V24",
            "vignette_title": "Crestview Bancorp: Basel III Capital Ratios & Capital Adequacy Analysis",
            "vignette_text": v24_text,
            "los": "LOS 16.b: Describe the Basel III regulatory capital requirements and calculate regulatory capital ratios.",
            "question": "Crestview Bancorp's CET1 Ratio, Tier 1 Capital Ratio, and Total Capital Ratio are closest to:",
            "options": {
                "A": "CET1: 9.25%; Tier 1: 10.50%; Total Capital: 13.00%.",
                "B": "CET1: 7.40%; Tier 1: 8.40%; Total Capital: 10.40%.",
                "C": "CET1: 9.25%; Tier 1: 10.50%; Total Capital: 11.75%."
            },
            "answer": "A",
            "explanation": (
                "With CET1 Capital = 37.0 billion USD and Total RWA = 400.0 billion USD:\n"
                "- $\\text{CET1 Ratio} = 37.0 / 400.0 = 9.25\\%$.\n\n"
                "Tier 1 Capital = CET1 (37.0) + AT1 (5.0) = 42.0 billion USD.\n"
                "- $\\text{Tier 1 Ratio} = 42.0 / 400.0 = 10.50\\%$.\n\n"
                "Tier 2 Capital = Subordinated debt (7.0) + Qualifying loan loss allowance (3.0) = 10.0 billion USD.\n"
                "Total Capital = Tier 1 (42.0) + Tier 2 (10.0) = 52.0 billion USD.\n"
                "- $\\text{Total Capital Ratio} = 52.0 / 400.0 = 13.00\\%$.\n\n"
                "Distractor B divides by total assets ($500.0$) instead of RWA ($400.0$).\n"
                "Distractor C omits the qualifying loan loss allowance from Tier 2."
            )
        },
        {
            "id": "L2-V24-Q4",
            "level": 2,
            "module": "m16-financial-institutions",
            "topic": "Analysis of Financial Institutions",
            "vignette_id": "V24",
            "vignette_title": "Crestview Bancorp: Basel III Capital Ratios & Capital Adequacy Analysis",
            "vignette_text": v24_text,
            "los": "LOS 16.b: Describe the Basel III regulatory capital requirements and calculate regulatory capital ratios.",
            "question": "Comparing Crestview's capital ratios against Basel III minimums plus the Capital Conservation Buffer, Crestview is:",
            "options": {
                "A": "Non-compliant on Total Capital because the requirement is 14.0%.",
                "B": "Fully compliant across all three capital tiers, exceeding the buffered requirements for CET1 (7.0%), Tier 1 (8.5%), and Total Capital (10.5%).",
                "C": "Deficient on CET1 Capital because the minimum required with buffer is 10.0%."
            },
            "answer": "B",
            "explanation": (
                "Under Basel III, the minimum required ratios plus the 2.5% Capital Conservation Buffer are:\n"
                "- CET1: $4.5\\% + 2.5\\% = 7.0\\%$. (Crestview achieves 9.25% - Compliant)\n"
                "- Tier 1: $6.0\\% + 2.5\\% = 8.5\\%$. (Crestview achieves 10.50% - Compliant)\n"
                "- Total Capital: $8.0\\% + 2.5\\% = 10.5\\%$. (Crestview achieves 13.00% - Compliant)\n\n"
                "Crestview comfortably surpasses all three regulatory capital minimums including the full conservation buffer."
            )
        },
        {
            "id": "L2-V24-Q5",
            "level": 2,
            "module": "m16-financial-institutions",
            "topic": "Analysis of Financial Institutions",
            "vignette_id": "V24",
            "vignette_title": "Crestview Bancorp: Basel III Capital Ratios & Capital Adequacy Analysis",
            "vignette_text": v24_text,
            "los": "LOS 16.b: Describe the Basel III regulatory capital requirements and calculate regulatory capital ratios.",
            "question": "What mandatory operational restriction applies if a bank's capital ratios satisfy the minimum standards but dip into the Capital Conservation Buffer?",
            "options": {
                "A": "Immediate mandatory liquidation of subordinated debt.",
                "B": "Increasingly stringent percentage restrictions on discretionary distributions, including dividends, share repurchases, and discretionary staff bonuses.",
                "C": "Revocation of the bank's federal deposit insurance charter."
            },
            "answer": "B",
            "explanation": (
                "Under Basel III, if a bank's CET1 ratio dips below the 7.0% threshold (i.e. falls into the 2.5% conservation buffer zone above "
                "the 4.5% absolute minimum), the bank does NOT face immediate receivership or closure. Instead, regulators impose automatic, "
                "progressively severe statutory payout caps on discretionary capital distributions, restricting dividend payments, share buybacks, "
                "and executive bonus pools to force the retention of earnings."
            )
        },
        {
            "id": "L2-V24-Q6",
            "level": 2,
            "module": "m16-financial-institutions",
            "topic": "Analysis of Financial Institutions",
            "vignette_id": "V24",
            "vignette_title": "Crestview Bancorp: Basel III Capital Ratios & Capital Adequacy Analysis",
            "vignette_text": v24_text,
            "los": "LOS 16.b: Describe the Basel III regulatory capital requirements and calculate regulatory capital ratios.",
            "question": "Crestview's Basel III Leverage Ratio is closest to:",
            "options": {
                "A": "7.50%, which easily exceeds the Basel III minimum requirement of 3.0%.",
                "B": "6.61%, which is below the Basel III minimum requirement of 8.0%.",
                "C": "8.40%, which exactly matches the minimum requirement of 8.4%."
            },
            "answer": "A",
            "explanation": (
                "The Basel III Leverage Ratio is a non-risk-weighted backstop metric defined as:\n"
                "$\\text{Leverage Ratio} = \\frac{\\text{Tier 1 Capital}}{\\text{Total Leverage Exposure}}$\n\n"
                "- Tier 1 Capital = 42.0 billion USD.\n"
                "- Total Leverage Exposure = 560.0 billion USD.\n"
                "$\\text{Leverage Ratio} = 42.0 / 560.0 = 7.50\\%$.\n\n"
                "The minimum Basel III Leverage Ratio standard is 3.0% (with higher surcharges for G-SIBs). Crestview's 7.50% "
                "exceeds the 3.0% regulatory floor.\n\n"
                "Distractor B divides CET1 by total exposure ($37 / 560 = 6.61\\%$) and cites an incorrect requirement."
            )
        }
    ]
    vignettes.append((v24_text, v24_questions))

    # =========================================================================
    # VIGNETTE 25: Asset Quality & Credit Risk Analysis
    # =========================================================================
    v25_text = (
        "Apex Commercial Bank is a regional lender with extensive exposure to commercial real estate (CRE) "
        "and middle-market commercial loans. CFA charterholder Kendra Hall is analyzing Apex's asset quality, "
        "provisioning practices, and allowance adequacy across the past three fiscal years.\n\n"
        "Exhibit 1: Apex Commercial Bank Loan Portfolio Data (in millions of USD)\n"
        "Metric | Year 1 | Year 2 | Year 3\n"
        "Gross loans: 18,000 USD | 20,000 USD | 22,000 USD\n"
        "Non-performing loans (NPLs): 360 USD | 450 USD | 660 USD\n"
        "Allowance for loan losses (beginning): 420 USD | 450 USD | 495 USD\n"
        "Provision for loan losses (P&L): 120 USD | 145 USD | 133 USD\n"
        "Gross charge-offs: 100 USD | 112 USD | 235 USD\n"
        "Recoveries on loans previously charged off: 10 USD | 12 USD | 15 USD\n"
        "Allowance for loan losses (ending): 450 USD | 495 USD | 408 USD\n\n"
        "Exhibit 2: Additional Portfolio Breakdown in Year 3\n"
        "- Commercial real estate (CRE) loans: 7,500 million USD\n"
        "- Total Tier 1 regulatory capital: 2,500 million USD\n"
        "- Restructured and forbearance loans: 320 million USD (currently classified as performing)\n\n"
        "Hall also compares US GAAP's Current Expected Credit Losses (CECL) methodology with IFRS 9's "
        "three-stage expected credit loss model."
    )

    v25_questions = [
        {
            "id": "L2-V25-Q1",
            "level": 2,
            "module": "m16-financial-institutions",
            "topic": "Analysis of Financial Institutions",
            "vignette_id": "V25",
            "vignette_title": "Apex Commercial Bank: Loan Quality, Provisioning, and Allowance for Credit Losses",
            "vignette_text": v25_text,
            "los": "LOS 16.c: Describe the factors to consider when analyzing asset quality and credit risk for a bank.",
            "question": "What is Apex's Non-Performing Loan (NPL) ratio and Coverage ratio at the end of Year 3?",
            "options": {
                "A": "NPL ratio: 3.00%; Coverage ratio: 61.82%.",
                "B": "NPL ratio: 2.25%; Coverage ratio: 110.00%.",
                "C": "NPL ratio: 3.00%; Coverage ratio: 125.00%."
            },
            "answer": "A",
            "explanation": (
                "1. Non-Performing Loan (NPL) Ratio:\n"
                "$$\\text{NPL Ratio} = \\frac{\\text{Non-Performing Loans}}{\\text{Gross Loans}} = \\frac{660}{22,000} = 3.00\\%$$\n"
                "(Rising from Year 1: $360 / 18,000 = 2.00\\%$ to Year 2: $450 / 20,000 = 2.25\\%$ to Year 3: $3.00\\%$).\n\n"
                "2. Coverage Ratio:\n"
                "$$\\text{Coverage Ratio} = \\frac{\\text{Allowance for Loan Losses}}{\\text{Non-Performing Loans}} = \\frac{408}{660} = 61.82\\%$$\n"
                "(Substantially deteriorated from Year 1: $450 / 360 = 125.0\\%$ and Year 2: $495 / 450 = 110.0\\%$ down to $61.82\\%$).\n\n"
                "Distractor B reflects Year 2 metrics. Distractor C reflects Year 1 coverage."
            )
        },
        {
            "id": "L2-V25-Q2",
            "level": 2,
            "module": "m16-financial-institutions",
            "topic": "Analysis of Financial Institutions",
            "vignette_id": "V25",
            "vignette_title": "Apex Commercial Bank: Loan Quality, Provisioning, and Allowance for Credit Losses",
            "vignette_text": v25_text,
            "los": "LOS 16.c: Describe the factors to consider when analyzing asset quality and credit risk for a bank.",
            "question": "What were Apex's Net Charge-Offs (NCOs) in Year 3, and what was the ratio of Provision for Loan Losses to NCOs?",
            "options": {
                "A": "Net Charge-Offs: 220 million USD; Provision-to-NCO ratio: 0.605.",
                "B": "Net Charge-Offs: 235 million USD; Provision-to-NCO ratio: 0.566.",
                "C": "Net Charge-Offs: 220 million USD; Provision-to-NCO ratio: 1.000."
            },
            "answer": "A",
            "explanation": (
                "1. Net Charge-Offs (NCOs) = Gross Charge-offs - Recoveries:\n"
                "$$\\text{NCOs in Year 3} = 235 - 15 = 220 \\text{ million USD}$$\n\n"
                "2. Ratio of Provision for Loan Losses to Net Charge-Offs:\n"
                "$$\\text{Provision / NCO} = 133 / 220 = 0.6045 \\approx 0.605$$\n\n"
                "This indicates that the provision recognized in the income statement (133 million USD) was significantly less than "
                "actual net loans written off (220 million USD), causing the allowance for loan losses to deplete substantially from "
                "495 million USD down to 408 million USD ($495 + 133 - 220 = 408$)."
            )
        },
        {
            "id": "L2-V25-Q3",
            "level": 2,
            "module": "m16-financial-institutions",
            "topic": "Analysis of Financial Institutions",
            "vignette_id": "V25",
            "vignette_title": "Apex Commercial Bank: Loan Quality, Provisioning, and Allowance for Credit Losses",
            "vignette_text": v25_text,
            "los": "LOS 16.c: Describe the factors to consider when analyzing asset quality and credit risk for a bank.",
            "question": "Which of the following signals potential earnings manipulation by Apex in Year 3?",
            "options": {
                "A": "Setting the loan loss provision well below net charge-offs during a period of rapidly rising NPLs to bolster reported earnings.",
                "B": "Recognizing loan recoveries in cash flow from financing activities.",
                "C": "Increasing the gross loan portfolio faster than deposit liabilities."
            },
            "answer": "A",
            "explanation": (
                "In Year 3, Non-Performing Loans surged from 450 to 660 million USD (+46.7%), and Net Charge-Offs spiked from 100 to "
                "220 million USD (+120%). Despite this sharp deterioration in asset quality, Apex REDUCED its Provision for Loan Losses "
                "from 145 million USD in Year 2 to 133 million USD in Year 3. By under-provisioning relative to actual charge-offs "
                "(Provision / NCO ratio of only 0.605), management cushioned reported net income at the direct expense of balance sheet "
                "loss reserves."
            )
        },
        {
            "id": "L2-V25-Q4",
            "level": 2,
            "module": "m16-financial-institutions",
            "topic": "Analysis of Financial Institutions",
            "vignette_id": "V25",
            "vignette_title": "Apex Commercial Bank: Loan Quality, Provisioning, and Allowance for Credit Losses",
            "vignette_text": v25_text,
            "los": "LOS 16.c: Describe the factors to consider when analyzing asset quality and credit risk for a bank.",
            "question": "Under IFRS 9's three-stage expected credit loss (ECL) model, when a loan experiences a 'significant increase in credit risk' (SICR) since initial recognition, it moves from:",
            "options": {
                "A": "Stage 1 (12-month ECL) to Stage 2 (Lifetime ECL), with interest revenue recognized on gross carrying amount.",
                "B": "Stage 2 to Stage 3, with interest revenue recognized on net carrying amount.",
                "C": "Stage 1 directly to charge-off status."
            },
            "answer": "A",
            "explanation": (
                "Under IFRS 9:\n"
                "- Stage 1 (Performing): Loans with no significant increase in credit risk since origination; loss allowance equals 12-month ECL; "
                "interest revenue is calculated on gross carrying amount.\n"
                "- Stage 2 (Underperforming): Loans that have experienced a Significant Increase in Credit Risk (SICR) but are not yet credit-impaired; "
                "loss allowance jumps to full LIFETIME ECL; interest revenue is still calculated on gross carrying amount.\n"
                "- Stage 3 (Non-performing / Credit-impaired): Objective evidence of impairment; lifetime ECL; interest revenue is calculated on "
                "NET carrying amount (gross loan less allowance)."
            )
        },
        {
            "id": "L2-V25-Q5",
            "level": 2,
            "module": "m16-financial-institutions",
            "topic": "Analysis of Financial Institutions",
            "vignette_id": "V25",
            "vignette_title": "Apex Commercial Bank: Loan Quality, Provisioning, and Allowance for Credit Losses",
            "vignette_text": v25_text,
            "los": "LOS 16.c: Describe the factors to consider when analyzing asset quality and credit risk for a bank.",
            "question": "Evaluating Apex's Commercial Real Estate (CRE) concentration risk in Year 3:",
            "options": {
                "A": "CRE loans represent 150% of Tier 1 capital, well below regulatory alert levels.",
                "B": "CRE loans represent 300% of Tier 1 capital ($7,500 / 2,500$), indicating extreme vulnerability to property market downturns.",
                "C": "CRE concentration cannot be evaluated without factoring in Tier 2 subordinated debt."
            },
            "answer": "B",
            "explanation": (
                "Regulatory bank supervision guidelines (such as US interagency CRE guidelines) identify CRE loan concentrations exceeding "
                "300% of total risk-based capital (or Tier 1 capital) as a heightened risk indicator requiring enhanced supervisory scrutiny.\n\n"
                "$\\text{CRE Concentration Ratio} = \\frac{\\text{CRE Loans}}{\\text{Tier 1 Capital}} = \\frac{7,500}{2,500} = 300\\%$.\n\n"
                "This indicates severe exposure to commercial real estate collateral values and refinancing stress."
            )
        },
        {
            "id": "L2-V25-Q6",
            "level": 2,
            "module": "m16-financial-institutions",
            "topic": "Analysis of Financial Institutions",
            "vignette_id": "V25",
            "vignette_title": "Apex Commercial Bank: Loan Quality, Provisioning, and Allowance for Credit Losses",
            "vignette_text": v25_text,
            "los": "LOS 16.c: Describe the factors to consider when analyzing asset quality and credit risk for a bank.",
            "question": "Regarding Apex's 320 million USD of restructured and forbearance loans classified as performing:",
            "options": {
                "A": "Analysts should accept management's classification because loan modifications legally extinguish credit risk.",
                "B": "Analysts should scrutinize modified loans because forbearance often delays default recognition, artificially understating true NPLs.",
                "C": "Restructured loans must automatically be written off under IFRS and US GAAP."
            },
            "answer": "B",
            "explanation": (
                "Loan forbearance, modifications, and restructuring ('troubled debt restructurings' or modified loans) often allow banks to avoid "
                "classifying distressed borrowers as Non-Performing Loans (NPLs). Prudent financial statement analysts adjust reported asset quality "
                "metrics by treating modified and forbearance loans as non-performing or high-risk loans, as economic default has merely been postponed."
            )
        }
    ]
    vignettes.append((v25_text, v25_questions))

    # =========================================================================
    # VIGNETTE 26: Liquidity Analysis & Basel III Standards (LCR & NSFR)
    # =========================================================================
    v26_text = (
        "Vanguard Trust & Savings is an international banking group subject to Basel III liquidity regulations. "
        "Treasury risk officer Nathan Drake, CFA, is responsible for assessing Vanguard's compliance with the "
        "Liquidity Coverage Ratio (LCR) and Net Stable Funding Ratio (NSFR).\n\n"
        "Exhibit 1: Liquid Asset Holdings for LCR Calculation (in billions of USD)\n"
        "- Central bank cash reserves: 30.0 billion USD (Haircut = 0%)\n"
        "- 0% risk-weight AAA sovereign government bonds: 50.0 billion USD (Haircut = 0%)\n"
        "- Qualifying 20% risk-weight government agency bonds (Level 2A): 20.0 billion USD (Haircut = 15%)\n"
        "- Qualifying investment-grade BBB corporate bonds (Level 2B): 10.0 billion USD (Haircut = 50%)\n\n"
        "Note: Basel III rules require that total Level 2 assets (Level 2A + Level 2B) comprise no more than "
        "40% of total High-Quality Liquid Assets (HQLA), and Level 2B assets cannot exceed 15% of total HQLA.\n\n"
        "Exhibit 2: 30-Day Stress Scenario Cash Outflow Parameters (in billions of USD)\n"
        "- Stable retail demand deposits: 200.0 billion USD (Run-off rate = 5%)\n"
        "- Less stable retail deposits: 80.0 billion USD (Run-off rate = 10%)\n"
        "- Non-operational unsecured wholesale funding: 60.0 billion USD (Run-off rate = 100%)\n"
        "- Operational deposits from commercial clients: 40.0 billion USD (Run-off rate = 25%)\n"
        "- Committed credit facilities extended to corporate clients: 30.0 billion USD (Drawdown rate = 20%)\n\n"
        "Exhibit 3: Stress Scenario Cash Inflow Data\n"
        "- Contractual performing inflows from fully performing retail and commercial loans over 30 days: 16.0 billion USD\n"
        "- Regulatory cap on cash inflows: Cash inflows cannot exceed 75% of total expected cash outflows.\n\n"
        "Exhibit 4: Structural Balance Sheet Data for NSFR\n"
        "- Available Stable Funding (ASF): 320.0 billion USD\n"
        "- Required Stable Funding (RSF): 280.0 billion USD"
    )

    v26_questions = [
        {
            "id": "L2-V26-Q1",
            "level": 2,
            "module": "m16-financial-institutions",
            "topic": "Analysis of Financial Institutions",
            "vignette_id": "V26",
            "vignette_title": "Vanguard Trust: Basel III Liquidity Coverage Ratio & Net Stable Funding Ratio",
            "vignette_text": v26_text,
            "los": "LOS 16.d: Describe the factors to consider when analyzing liquidity for a bank, including the Liquidity Coverage Ratio and Net Stable Funding Ratio.",
            "question": "What is Vanguard's total qualifying High-Quality Liquid Assets (HQLA) after applying regulatory haircuts and asset category caps?",
            "options": {
                "A": "102.0 billion USD.",
                "B": "110.0 billion USD.",
                "C": "95.0 billion USD."
            },
            "answer": "A",
            "explanation": (
                "1. Level 1 Assets (0% haircut):\n"
                "$\\text{Level 1} = 30.0 \\text{ (cash)} + 50.0 \\text{ (sovereigns)} = 80.0$ billion USD.\n\n"
                "2. Level 2A Assets (15% haircut):\n"
                "$\\text{Level 2A} = 20.0 \\times (1 - 0.15) = 17.0$ billion USD.\n\n"
                "3. Level 2B Assets (50% haircut):\n"
                "$\\text{Level 2B} = 10.0 \\times (1 - 0.50) = 5.0$ billion USD.\n\n"
                "4. Check Level 2 Caps:\n"
                "- Total Level 2 assets after haircuts = $17.0 + 5.0 = 22.0$ billion USD.\n"
                "- Total HQLA before cap = $80.0 + 22.0 = 102.0$ billion USD.\n"
                "- Maximum allowable Level 2 assets: Level 2 cannot exceed 40% of total HQLA (i.e. $\\text{Level 2} \\le \\frac{2}{3} \\times \\text{Level 1} = \\frac{2}{3} \\times 80.0 = 53.33$ billion USD).\n"
                "Since $22.0 < 53.33$, the 40% cap is not binding.\n"
                "- Maximum allowable Level 2B: Level 2B cannot exceed 15% of total HQLA ($5.0 / 102.0 = 4.90\\% < 15\\%$), not binding.\n\n"
                "$\\text{Total HQLA} = 80.0 + 17.0 + 5.0 = 102.0$ billion USD.\n\n"
                "Distractor B (110.0 billion USD) is the unadjusted face value before haircuts ($30 + 50 + 20 + 10$)."
            )
        },
        {
            "id": "L2-V26-Q2",
            "level": 2,
            "module": "m16-financial-institutions",
            "topic": "Analysis of Financial Institutions",
            "vignette_id": "V26",
            "vignette_title": "Vanguard Trust: Basel III Liquidity Coverage Ratio & Net Stable Funding Ratio",
            "vignette_text": v26_text,
            "los": "LOS 16.d: Describe the factors to consider when analyzing liquidity for a bank, including the Liquidity Coverage Ratio and Net Stable Funding Ratio.",
            "question": "What is Vanguard's Total Net Cash Outflows over the 30-day stress scenario?",
            "options": {
                "A": "94.0 billion USD.",
                "B": "78.0 billion USD.",
                "C": "62.0 billion USD."
            },
            "answer": "B",
            "explanation": (
                "1. Total Expected Cash Outflows:\n"
                "- Stable retail deposits: $200.0 \\times 5\\% = 10.0$ billion USD.\n"
                "- Less stable retail deposits: $80.0 \\times 10\\% = 8.0$ billion USD.\n"
                "- Wholesale non-operational: $60.0 \\times 100\\% = 60.0$ billion USD.\n"
                "- Operational deposits: $40.0 \\times 25\\% = 10.0$ billion USD.\n"
                "- Committed facilities: $30.0 \\times 20\\% = 6.0$ billion USD.\n"
                "Total Cash Outflows = $10.0 + 8.0 + 60.0 + 10.0 + 6.0 = 94.0$ billion USD.\n\n"
                "2. Total Contractual Inflows:\n"
                "Contractual Inflows = 16.0 billion USD.\n"
                "Cap check: Inflows capped at 75% of outflows ($0.75 \\times 94.0 = 70.5$ billion USD). 16.0 is below cap.\n\n"
                "3. Total Net Cash Outflows:\n"
                "$\\text{Net Outflows} = \\text{Outflows} - \\text{Inflows} = 94.0 - 16.0 = 78.0$ billion USD.\n\n"
                "Distractor A (94.0 billion USD) fails to subtract cash inflows."
            )
        },
        {
            "id": "L2-V26-Q3",
            "level": 2,
            "module": "m16-financial-institutions",
            "topic": "Analysis of Financial Institutions",
            "vignette_id": "V26",
            "vignette_title": "Vanguard Trust: Basel III Liquidity Coverage Ratio & Net Stable Funding Ratio",
            "vignette_text": v26_text,
            "los": "LOS 16.d: Describe the factors to consider when analyzing liquidity for a bank, including the Liquidity Coverage Ratio and Net Stable Funding Ratio.",
            "question": "Vanguard's Liquidity Coverage Ratio (LCR) and its regulatory compliance status are closest to:",
            "options": {
                "A": "130.8%; Compliant (exceeds the 100% regulatory minimum).",
                "B": "108.5%; Non-compliant (below the 115% minimum).",
                "C": "83.0%; Non-compliant (below the 100% minimum)."
            },
            "answer": "A",
            "explanation": (
                "The Liquidity Coverage Ratio is defined as:\n"
                "$\\text{LCR} = \\frac{\\text{Total HQLA}}{\\text{Total Net Cash Outflows over 30 Days}} = \\frac{102.0}{78.0} = 130.77\\% \\approx 130.8\\%$.\n\n"
                "Under Basel III, the regulatory minimum for LCR is 100%. Vanguard's ratio of 130.8% comfortably exceeds the requirement."
            )
        },
        {
            "id": "L2-V26-Q4",
            "level": 2,
            "module": "m16-financial-institutions",
            "topic": "Analysis of Financial Institutions",
            "vignette_id": "V26",
            "vignette_title": "Vanguard Trust: Basel III Liquidity Coverage Ratio & Net Stable Funding Ratio",
            "vignette_text": v26_text,
            "los": "LOS 16.d: Describe the factors to consider when analyzing liquidity for a bank, including the Liquidity Coverage Ratio and Net Stable Funding Ratio.",
            "question": "What is Vanguard's Net Stable Funding Ratio (NSFR), and what structural time horizon does it govern?",
            "options": {
                "A": "114.3%; it ensures structural liquidity and funding stability over an extended one-year horizon.",
                "B": "87.5%; it governs intra-day clearing and settlement liquidity.",
                "C": "114.3%; it measures short-term 30-day liquidity stress."
            },
            "answer": "A",
            "explanation": (
                "The Net Stable Funding Ratio (NSFR) measures structural, longer-term funding stability:\n"
                "$\\text{NSFR} = \\frac{\\text{Available Stable Funding (ASF)}}{\\text{Required Stable Funding (RSF)}} = \\frac{320.0}{280.0} = 114.29\\% \\approx 114.3\\%$.\n\n"
                "Under Basel III, the NSFR minimum is 100%. Whereas the LCR focuses on a 30-day acute liquidity stress horizon, "
                "the NSFR requires banks to maintain a stable funding profile in relation to the composition of their assets and off-balance "
                "sheet activities over a one-year structural horizon.\n\n"
                "Distractor C incorrectly attributes a 30-day horizon to the NSFR."
            )
        },
        {
            "id": "L2-V26-Q5",
            "level": 2,
            "module": "m16-financial-institutions",
            "topic": "Analysis of Financial Institutions",
            "vignette_id": "V26",
            "vignette_title": "Vanguard Trust: Basel III Liquidity Coverage Ratio & Net Stable Funding Ratio",
            "vignette_text": v26_text,
            "los": "LOS 16.d: Describe the factors to consider when analyzing liquidity for a bank, including the Liquidity Coverage Ratio and Net Stable Funding Ratio.",
            "question": "Why does the Basel III LCR assign a 100% run-off rate to non-operational wholesale funding compared to only 5% for stable retail deposits?",
            "options": {
                "A": "Wholesale counterparties are strictly regulated by central banks.",
                "B": "Unsecured wholesale deposits are highly credit-sensitive and quickly flee during stress, whereas insured retail deposits are sticky and relationship-driven.",
                "C": "Wholesale funding is backed by government deposit insurance guarantees."
            },
            "answer": "B",
            "explanation": (
                "Institutional and wholesale counterparties monitor bank credit spreads continuously and will immediately withdraw uncollateralized "
                "deposits or decline to roll over commercial paper at the first hint of distress (100% run-off). In contrast, consumer retail deposits "
                "are fully covered by government deposit insurance schemes (e.g. FDIC), making retail depositors inattentive to short-term solvency "
                "rumors and rendering the deposits highly sticky (5% run-off)."
            )
        },
        {
            "id": "L2-V26-Q6",
            "level": 2,
            "module": "m16-financial-institutions",
            "topic": "Analysis of Financial Institutions",
            "vignette_id": "V26",
            "vignette_title": "Vanguard Trust: Basel III Liquidity Coverage Ratio & Net Stable Funding Ratio",
            "vignette_text": v26_text,
            "los": "LOS 16.d: Describe the factors to consider when analyzing liquidity for a bank, including the Liquidity Coverage Ratio and Net Stable Funding Ratio.",
            "question": "How do off-balance sheet committed credit facilities affect bank liquidity during financial market turmoil?",
            "options": {
                "A": "They act as liquid assets that the bank can sell for cash.",
                "B": "They create severe contingent liquidity drains because distressed corporate clients draw down pre-committed credit lines.",
                "C": "They are completely ignored in regulatory liquidity stress tests."
            },
            "answer": "B",
            "explanation": (
                "Committed credit and liquidity facilities represent contingent liquidity commitments. When credit markets freeze, corporate "
                "borrowers who can no longer issue commercial paper immediately tap their backup credit lines at commercial banks, causing "
                "sudden, massive cash outflows just when the bank itself is experiencing funding stress. This is why Basel III mandates specific "
                "stress drawdown assumptions for off-balance sheet commitments."
            )
        }
    ]
    vignettes.append((v26_text, v26_questions))

    # =========================================================================
    # VIGNETTE 27: Sensitivity to Market Risk & Fair Value Hierarchy
    # =========================================================================
    v27_text = (
        "Meridian Capital Bank is a large money-center financial institution with active global trading "
        "and retail lending operations. Risk analyst Gabriel Thorne is assessing the bank's market risk "
        "exposure, balance sheet interest rate duration gap, and valuation transparency.\n\n"
        "Exhibit 1: Balance Sheet Duration Profile (in billions of USD)\n"
        "- Total Accounting Assets (A): 500.0 billion USD\n"
        "- Modified Duration of Assets ($D_A$): 4.50 years\n"
        "- Total Accounting Liabilities (L): 450.0 billion USD\n"
        "- Modified Duration of Liabilities ($D_L$): 1.80 years\n"
        "- Total Shareholders' Equity (E): 50.0 billion USD\n\n"
        "Exhibit 2: Trading Book Value-at-Risk (VaR) & Backtesting\n"
        "- 1-day 95% Daily Trading VaR: 25.0 million USD\n"
        "- 10-day 99% Regulatory VaR: 80.0 million USD\n"
        "- Number of daily trading losses exceeding the 95% VaR threshold over the last 250 trading days: 8 exceptions\n"
        "- Basel Traffic Light Framework: 0 to 4 exceptions = Green zone; 5 to 9 exceptions = Yellow zone; 10+ exceptions = Red zone\n\n"
        "Exhibit 3: Fair Value Hierarchy of Total Assets\n"
        "- Level 1 Assets (quoted prices in active markets): 180.0 billion USD\n"
        "- Level 2 Assets (observable market inputs): 280.0 billion USD\n"
        "- Level 3 Assets (unobservable inputs / internal models): 40.0 billion USD\n"
        "- Common Equity Tier 1 (CET1) Capital: 45.0 billion USD"
    )

    v27_questions = [
        {
            "id": "L2-V27-Q1",
            "level": 2,
            "module": "m16-financial-institutions",
            "topic": "Analysis of Financial Institutions",
            "vignette_id": "V27",
            "vignette_title": "Meridian Capital Bank: Value at Risk (VaR), Duration Gap, and Fair Value Hierarchy",
            "vignette_text": v27_text,
            "los": "LOS 16.e: Describe the factors to consider when analyzing sensitivity to market risk for a bank.",
            "question": "What is Meridian Capital Bank's balance sheet Duration Gap ($DG$)?",
            "options": {
                "A": "2.88 years.",
                "B": "2.70 years.",
                "C": "3.12 years."
            },
            "answer": "A",
            "explanation": (
                "The bank balance sheet duration gap ($DG$) measures the interest rate sensitivity mismatch between assets and liabilities:\n"
                "$$DG = D_A - \\left(\\frac{L}{A}\\right) D_L$$\n\n"
                "- $D_A = 4.50$ years\n"
                "- $D_L = 1.80$ years\n"
                "- $L / A = 450.0 / 500.0 = 0.90$\n"
                "$$DG = 4.50 - (0.90 \\times 1.80) = 4.50 - 1.62 = 2.88 \\text{ years}$$\n\n"
                "Distractor B (2.70 years) simply calculates $D_A - D_L = 4.50 - 1.80 = 2.70$, ignoring the leverage adjustment ($L/A$).\n"
                "Distractor C incorrectly adds the liabilities duration."
            )
        },
        {
            "id": "L2-V27-Q2",
            "level": 2,
            "module": "m16-financial-institutions",
            "topic": "Analysis of Financial Institutions",
            "vignette_id": "V27",
            "vignette_title": "Meridian Capital Bank: Value at Risk (VaR), Duration Gap, and Fair Value Hierarchy",
            "vignette_text": v27_text,
            "los": "LOS 16.e: Describe the factors to consider when analyzing sensitivity to market risk for a bank.",
            "question": "If market interest rates experience an immediate parallel upward shift of 100 basis points (+1.00%), the estimated percentage change in the economic value of Meridian's equity ($\\Delta E / E$) is closest to:",
            "options": {
                "A": "-28.8%.",
                "B": "-14.4%.",
                "C": "+28.8%."
            },
            "answer": "A",
            "explanation": (
                "The approximate percentage change in the economic value of equity for a parallel yield change ($\\Delta y$) is given by:\n"
                "$$\\frac{\\Delta E}{E} \\approx - DG \\times \\left(\\frac{A}{E}\\right) \\times \\Delta y$$\n\n"
                "- $DG = 2.88$ years\n"
                "- Leverage multiplier: $A / E = 500.0 / 50.0 = 10.0$\n"
                "- Rate change: $\\Delta y = +0.0100$ (+100 bps)\n\n"
                "$$\\frac{\\Delta E}{E} \\approx - 2.88 \\times 10.0 \\times 0.0100 = - 0.288 = - 28.8\\%$$\n\n"
                "In dollar terms, economic equity declines by: $28.8\\% \\times 50.0 \\text{ billion} = 14.4$ billion USD.\n\n"
                "Distractor B (-14.4%) confuses the dollar change in equity ($14.4$ billion) with the percentage change ($28.8\\%$)."
            )
        },
        {
            "id": "L2-V27-Q3",
            "level": 2,
            "module": "m16-financial-institutions",
            "topic": "Analysis of Financial Institutions",
            "vignette_id": "V27",
            "vignette_title": "Meridian Capital Bank: Value at Risk (VaR), Duration Gap, and Fair Value Hierarchy",
            "vignette_text": v27_text,
            "los": "LOS 16.e: Describe the factors to consider when analyzing sensitivity to market risk for a bank.",
            "question": "What is the regulatory consequence of Meridian experiencing 8 backtesting exceptions over the past 250 trading days?",
            "options": {
                "A": "No consequence, because 8 exceptions is completely normal for a 95% confidence level.",
                "B": "The bank is placed in the Basel 'Yellow Zone', triggering an automatic supervisory increase in its market risk regulatory capital multiplier.",
                "C": "The bank must immediately shut down all proprietary trading operations."
            },
            "answer": "B",
            "explanation": (
                "Under the Basel backtesting framework for 250 trading days:\n"
                "- Green zone (0 to 4 exceptions): Model deemed accurate; minimum capital multiplier ($k = 3.0$).\n"
                "- Yellow zone (5 to 9 exceptions): Model accuracy questioned; supervisors impose an automatic scaling penalty ('plus factor') "
                "that increases the capital multiplier progressively above 3.0 (up to $3.85$ for 8 exceptions), requiring the bank to hold more capital.\n"
                "- Red zone (10+ exceptions): Model presumed fundamentally flawed; supervisory intervention required."
            )
        },
        {
            "id": "L2-V27-Q4",
            "level": 2,
            "module": "m16-financial-institutions",
            "topic": "Analysis of Financial Institutions",
            "vignette_id": "V27",
            "vignette_title": "Meridian Capital Bank: Value at Risk (VaR), Duration Gap, and Fair Value Hierarchy",
            "vignette_text": v27_text,
            "los": "LOS 16.e: Describe the factors to consider when analyzing sensitivity to market risk for a bank.",
            "question": "Evaluating Meridian's Level 3 assets relative to its Common Equity Tier 1 (CET1) capital:",
            "options": {
                "A": "Level 3 assets represent 88.9% of CET1 capital, indicating substantial valuation risk and potential vulnerability to aggressive marking.",
                "B": "Level 3 assets represent 8.0% of CET1 capital, posing negligible solvency threat.",
                "C": "Level 3 assets represent 100% of regulatory capital."
            },
            "answer": "A",
            "explanation": (
                "Level 3 assets rely on unobservable inputs and internal pricing models ('mark-to-model'), making them highly subjective "
                "and prone to aggressive valuation assumptions or unexpected illiquidity markdowns during crisis periods.\n\n"
                "$\\text{Level 3 / CET1 Capital} = \\frac{40.0}{45.0} = 88.89\\% \\approx 88.9\\%$.\n\n"
                "Because illiquid Level 3 assets equal nearly 89% of the bank's core CET1 capital, a modest 10% writedown in Level 3 valuations "
                "would erase 4.0 billion USD—nearly 9% of Meridian's total common equity capital."
            )
        },
        {
            "id": "L2-V27-Q5",
            "level": 2,
            "module": "m16-financial-institutions",
            "topic": "Analysis of Financial Institutions",
            "vignette_id": "V27",
            "vignette_title": "Meridian Capital Bank: Value at Risk (VaR), Duration Gap, and Fair Value Hierarchy",
            "vignette_text": v27_text,
            "los": "LOS 16.e: Describe the factors to consider when analyzing sensitivity to market risk for a bank.",
            "question": "How does the Repricing Gap differ conceptually from the Duration Gap when analyzing bank interest rate risk?",
            "options": {
                "A": "The Repricing Gap measures short-term Net Interest Income sensitivity, whereas the Duration Gap measures long-term economic value of equity (EVE) sensitivity.",
                "B": "The Repricing Gap applies only to trading assets, while the Duration Gap applies only to liabilities.",
                "C": "The Duration Gap measures cash flows, while the Repricing Gap measures market value changes."
            },
            "answer": "A",
            "explanation": (
                "The Repricing Gap (Rate-Sensitive Assets minus Rate-Sensitive Liabilities over specific time buckets, e.g. 30, 90, 360 days) "
                "evaluates the impact of interest rate changes on near-term Net Interest Income (NII) in the income statement. "
                "In contrast, the Duration Gap measures the sensitivity of the market/economic value of the bank's total assets and liabilities, "
                "quantifying the net change in the Economic Value of Equity (EVE) on the balance sheet."
            )
        },
        {
            "id": "L2-V27-Q6",
            "level": 2,
            "module": "m16-financial-institutions",
            "topic": "Analysis of Financial Institutions",
            "vignette_id": "V27",
            "vignette_title": "Meridian Capital Bank: Value at Risk (VaR), Duration Gap, and Fair Value Hierarchy",
            "vignette_text": v27_text,
            "los": "LOS 16.e: Describe the factors to consider when analyzing sensitivity to market risk for a bank.",
            "question": "Under IFRS 9 and US GAAP, how are financial assets held in the trading book versus the banking book accounted for?",
            "options": {
                "A": "Trading book assets are marked to market through Net Income (FVTPL); banking book loans are held at amortized cost.",
                "B": "Both trading book and banking book assets are held at historical amortized cost.",
                "C": "Trading book assets are carried at Fair Value through OCI (FVOCI), while banking book assets are at FVTPL."
            },
            "answer": "A",
            "explanation": (
                "Trading book assets are held for trading purposes and actively managed for short-term profits. Under IFRS 9 and US GAAP, "
                "they are classified at Fair Value through Profit or Loss (FVTPL), with all mark-to-market valuation swings recognized immediately "
                "in Net Income. Banking book assets (such as customer commercial loans held to collect contractual cash flows) are accounted "
                "for at amortized cost net of credit loss allowances."
            )
        }
    ]
    vignettes.append((v27_text, v27_questions))

    # =========================================================================
    # VIGNETTE 28: Property & Casualty (P&C) Insurance Analysis
    # =========================================================================
    v28_text = (
        "Beacon Property & Casualty Reinsurance Corp is a major US insurer providing commercial property "
        "and liability coverage. Insurance analyst Cynthia Boyd, CFA, is conducting a detailed examination "
        "of Beacon's underwriting profitability, loss reserve development, and investment yield.\n\n"
        "Exhibit 1: Beacon P&C Financial Summary for Year 2 (in millions of USD)\n"
        "Gross written premiums: 1,200 million USD\n"
        "Net written premiums: 1,000 million USD\n"
        "Net earned premiums: 950 million USD\n"
        "Losses and loss adjustment expenses (LAE) incurred: 665 million USD\n"
        "Underwriting expenses incurred: 285 million USD\n"
        "Net investment income: 95 million USD\n"
        "Average invested assets: 1,900 million USD\n\n"
        "Exhibit 2: Historical Loss Development Triangle for Accident Year 1 (in millions of USD)\n"
        "Development Stage | Reported Loss Reserves & Cumulative Incurred Claims\n"
        "- At end of Accident Year 1 (initial estimate): 500 million USD\n"
        "- One year later (end of Year 2): 540 million USD\n"
        "- Two years later (end of Year 3): 570 million USD\n\n"
        "Accident Year 2 was initially estimated at 480 million USD and developed to 510 million USD at the end of Year 3.\n\n"
        "Boyd notes that the property and casualty sector is currently transitioning from a 'soft market' "
        "to a 'hard market' after a series of severe hurricane and convective storm seasons."
    )

    v28_questions = [
        {
            "id": "L2-V28-Q1",
            "level": 2,
            "module": "m16-financial-institutions",
            "topic": "Analysis of Financial Institutions",
            "vignette_id": "V28",
            "vignette_title": "Beacon Property & Casualty Reinsurance: Underwriting Performance & Loss Reserves",
            "vignette_text": v28_text,
            "los": "LOS 16.f: Describe the factors to consider when analyzing property and casualty insurance companies.",
            "question": "What are Beacon's Loss Ratio and Expense Ratio for Year 2?",
            "options": {
                "A": "Loss Ratio: 70.0%; Expense Ratio: 28.5%.",
                "B": "Loss Ratio: 66.5%; Expense Ratio: 28.5%.",
                "C": "Loss Ratio: 70.0%; Expense Ratio: 30.0%."
            },
            "answer": "A",
            "explanation": (
                "In Property and Casualty insurance:\n"
                "1. Loss Ratio (including Loss Adjustment Expenses - LAE):\n"
                "$$\\text{Loss Ratio} = \\frac{\\text{Losses and LAE Incurred}}{\\text{Net Earned Premiums}} = \\frac{665}{950} = 70.0\\%$$\n\n"
                "2. Expense Ratio (Underwriting Expenses):\n"
                "$$\\text{Expense Ratio} = \\frac{\\text{Underwriting Expenses}}{\\text{Net Written Premiums}} = \\frac{285}{1,000} = 28.5\\%$$\n"
                "(Note: Underwriting expenses are incurred at policy inception and are traditionally scaled by Net Written Premiums under US statutory accounting).\n\n"
                "Distractor B divides losses by Net Written Premiums ($665 / 1,000 = 66.5\\%$), which is incorrect.\n"
                "Distractor C divides expenses by Net Earned Premiums ($285 / 950 = 30.0\\%$)."
            )
        },
        {
            "id": "L2-V28-Q2",
            "level": 2,
            "module": "m16-financial-institutions",
            "topic": "Analysis of Financial Institutions",
            "vignette_id": "V28",
            "vignette_title": "Beacon Property & Casualty Reinsurance: Underwriting Performance & Loss Reserves",
            "vignette_text": v28_text,
            "los": "LOS 16.f: Describe the factors to consider when analyzing property and casualty insurance companies.",
            "question": "What is Beacon's Combined Ratio for Year 2, and what does it indicate regarding underwriting operations?",
            "options": {
                "A": "98.5%; indicates profitable underwriting operations before considering investment income.",
                "B": "100.0%; indicates break-even underwriting operations.",
                "C": "104.5%; indicates an underwriting loss that must be covered by investment yield."
            },
            "answer": "A",
            "explanation": (
                "The Combined Ratio is the sum of the Loss Ratio and the Expense Ratio:\n"
                "$$\\text{Combined Ratio} = \\text{Loss Ratio} + \\text{Expense Ratio} = 70.0\\% + 28.5\\% = 98.5\\%$$\n\n"
                "- A Combined Ratio below 100% indicates an UNDERWRITING PROFIT (here, an underwriting margin of $100\\% - 98.5\\% = 1.5\\%$).\n"
                "- A Combined Ratio above 100% indicates an underwriting loss, meaning premium income alone is insufficient to cover claims "
                "and operating expenses, requiring investment income to achieve overall profitability."
            )
        },
        {
            "id": "L2-V28-Q3",
            "level": 2,
            "module": "m16-financial-institutions",
            "topic": "Analysis of Financial Institutions",
            "vignette_id": "V28",
            "vignette_title": "Beacon Property & Casualty Reinsurance: Underwriting Performance & Loss Reserves",
            "vignette_text": v28_text,
            "los": "LOS 16.f: Describe the factors to consider when analyzing property and casualty insurance companies.",
            "question": "Beacon's Investment Income Ratio and Operating Ratio for Year 2 are closest to:",
            "options": {
                "A": "Investment Income Ratio: 10.0%; Operating Ratio: 88.5%.",
                "B": "Investment Income Ratio: 5.0%; Operating Ratio: 93.5%.",
                "C": "Investment Income Ratio: 10.0%; Operating Ratio: 108.5%."
            },
            "answer": "A",
            "explanation": (
                "1. Investment Income Ratio:\n"
                "$$\\text{Investment Income Ratio} = \\frac{\\text{Net Investment Income}}{\\text{Net Earned Premiums}} = \\frac{95}{950} = 10.0\\%$$\n"
                "(Investment portfolio yield on invested assets is $95 / 1,900 = 5.0\\%$).\n\n"
                "2. Operating Ratio:\n"
                "$$\\text{Operating Ratio} = \\text{Combined Ratio} - \\text{Investment Income Ratio} = 98.5\\% - 10.0\\% = 88.5\\%$$\n\n"
                "The Operating Ratio evaluates overall pre-tax operational performance. An Operating Ratio well below 100% confirms strong "
                "total profitability combining underwriting margin with investment returns."
            )
        },
        {
            "id": "L2-V28-Q4",
            "level": 2,
            "module": "m16-financial-institutions",
            "topic": "Analysis of Financial Institutions",
            "vignette_id": "V28",
            "vignette_title": "Beacon Property & Casualty Reinsurance: Underwriting Performance & Loss Reserves",
            "vignette_text": v28_text,
            "los": "LOS 16.f: Describe the factors to consider when analyzing property and casualty insurance companies.",
            "question": "Based on the loss development triangle in Exhibit 2, what pattern does Cynthia Boyd identify regarding Beacon's loss reserves?",
            "options": {
                "A": "Conservative over-reserving, with cumulative claims being consistently revised downwards over time.",
                "B": "Adverse loss development (under-reserving), indicating that initial reserve estimates were inadequate and artificially boosted prior reported earnings.",
                "C": "Perfect actuarial precision with zero reserve drift."
            },
            "answer": "B",
            "explanation": (
                "Examining the loss development schedule:\n"
                "- Accident Year 1 was initially set at 500 million USD, then revised upward to 540 million USD, and then to 570 million USD (+70 million USD adverse development).\n"
                "- Accident Year 2 was initially set at 480 million USD and developed upward to 510 million USD (+30 million USD adverse development).\n\n"
                "Consistent upward revisions indicate adverse loss development (under-reserving). When an insurer sets initial reserves too low, "
                "incurred losses are understated and net income is artificially inflated in the accident year. In later years, the insurer must "
                "record additional loss provisions, depressing future earnings."
            )
        },
        {
            "id": "L2-V28-Q5",
            "level": 2,
            "module": "m16-financial-institutions",
            "topic": "Analysis of Financial Institutions",
            "vignette_id": "V28",
            "vignette_title": "Beacon Property & Casualty Reinsurance: Underwriting Performance & Loss Reserves",
            "vignette_text": v28_text,
            "los": "LOS 16.f: Describe the factors to consider when analyzing property and casualty insurance companies.",
            "question": "How do underwriting conditions typically shift as the P&C insurance market transitions from a 'soft market' to a 'hard market'?",
            "options": {
                "A": "Premium rates increase, underwriting standards tighten, and combined ratios generally improve.",
                "B": "Premium rates plunge due to excess capital, policy terms expand, and combined ratios rise above 100%.",
                "C": "Regulators cap premium rates, forcing insurers to exit commercial lines."
            },
            "answer": "A",
            "explanation": (
                "The P&C underwriting cycle consists of:\n"
                "- Soft Market: Excess capital, aggressive price competition, declining premium rates, relaxed underwriting terms, and combined ratios rising above 100%.\n"
                "- Hard Market: Triggered by large catastrophe losses or capital depletion; industry capital contracts, insurers cut capacity, premium rates "
                "surge sharply, underwriting criteria tighten, and combined ratios decline below 100%, restoring strong underwriting profitability."
            )
        },
        {
            "id": "L2-V28-Q6",
            "level": 2,
            "module": "m16-financial-institutions",
            "topic": "Analysis of Financial Institutions",
            "vignette_id": "V28",
            "vignette_title": "Beacon Property & Casualty Reinsurance: Underwriting Performance & Loss Reserves",
            "vignette_text": v28_text,
            "los": "LOS 16.f: Describe the factors to consider when analyzing property and casualty insurance companies.",
            "question": "Why do Property & Casualty insurers maintain shorter asset duration and higher portfolio liquidity compared to Life & Health insurers?",
            "options": {
                "A": "P&C claim frequencies and settlement timing are unpredictable and subject to catastrophic lump-sum cash payouts.",
                "B": "Statutory accounting prohibits P&C insurers from owning municipal or corporate bonds.",
                "C": "P&C policies provide lifetime guaranteed income annuities."
            },
            "answer": "A",
            "explanation": (
                "P&C insurance liabilities are predominantly short-to-medium tail (property damage, auto claims, catastrophe losses) "
                "with high volatility in claim timing and severity. An insurer must be prepared to liquidate invested assets quickly to satisfy "
                "multimillion-dollar claims following unexpected disasters. Therefore, P&C investment portfolios are heavily concentrated in high-quality, "
                "short-to-intermediate duration bonds and liquid securities, in contrast to the long-duration asset-liability matching of life insurers."
            )
        }
    ]
    vignettes.append((v28_text, v28_questions))

    # =========================================================================
    # VIGNETTE 29: Life & Health (L&H) Insurance Analysis
    # =========================================================================
    v29_text = (
        "Aethelgard Life Assurance is a global life, annuity, and health insurer. Financial analyst "
        "Dr. Danielle Morales, CFA, is evaluating Aethelgard's earnings sources, mortality experience, "
        "asset-liability management (ALM), and capital adequacy.\n\n"
        "Exhibit 1: Aethelgard Operating and Margin Data for the Year (in millions of USD)\n"
        "- Average policy reserves: 8,000 million USD\n"
        "- Total invested assets backing reserves: 8,600 million USD\n"
        "- Weighted average guaranteed credited interest rate on policy liabilities: 3.50%\n"
        "- Actual net investment yield earned on invested assets: 4.80%\n"
        "- Expected actuarial mortality claims: 180 million USD\n"
        "- Actual mortality claims incurred: 162 million USD\n"
        "- Premium loading for operational expenses: 90 million USD\n"
        "- Actual administrative expenses incurred: 84 million USD\n"
        "- Total policy surrender values paid: 300 million USD\n"
        "- Carrying value of policy reserves released upon surrender: 325 million USD\n\n"
        "Exhibit 2: Asset-Liability Duration Matching Profile\n"
        "- Effective duration of policy liabilities: 14.50 years\n"
        "- Effective duration of invested asset portfolio: 11.00 years\n"
        "- Convexity of liabilities: 240; Convexity of assets: 150\n\n"
        "Morales also reviews the US NAIC Risk-Based Capital (RBC) requirements, specifically C-1 (asset risk), "
        "C-2 (insurance/underwriting risk), C-3 (interest rate and market risk), and C-4 (general business risk)."
    )

    v29_questions = [
        {
            "id": "L2-V29-Q1",
            "level": 2,
            "module": "m16-financial-institutions",
            "topic": "Analysis of Financial Institutions",
            "vignette_id": "V29",
            "vignette_title": "Aethelgard Life Assurance: Mortality, Surrender Margin, and Asset-Liability Matching",
            "vignette_text": v29_text,
            "los": "LOS 16.g: Describe the factors to consider when analyzing life and health insurance companies.",
            "question": "What are Aethelgard's Investment Margin, Mortality Margin, and Expense Margin for the year?",
            "options": {
                "A": "Investment: 104 million USD; Mortality: 18 million USD; Expense: 6 million USD.",
                "B": "Investment: 111.8 million USD; Mortality: -18 million USD; Expense: -6 million USD.",
                "C": "Investment: 104 million USD; Mortality: 162 million USD; Expense: 84 million USD."
            },
            "answer": "A",
            "explanation": (
                "Life insurer profitability is analyzed across core operational margins:\n"
                "1. Investment (Interest) Margin:\n"
                "$$\\text{Investment Margin} = (\\text{Actual Return Rate} - \\text{Guaranteed Credited Rate}) \\times \\text{Policy Reserves}$$\n"
                "$$\\text{Investment Margin} = (4.80\\% - 3.50\\%) \\times 8,000 = 1.30\\% \\times 8,000 = 104.0 \\text{ million USD}$$\n\n"
                "2. Mortality Margin (favorable experience):\n"
                "$$\\text{Mortality Margin} = \\text{Expected Claims} - \\text{Actual Claims} = 180 - 162 = +18.0 \\text{ million USD}$$\n\n"
                "3. Expense Margin (favorable loading):\n"
                "$$\\text{Expense Margin} = \\text{Expense Loading} - \\text{Actual Expenses} = 90 - 84 = +6.0 \\text{ million USD}$$\n\n"
                "All three margins are positive and contributed favorably to pre-tax earnings."
            )
        },
        {
            "id": "L2-V29-Q2",
            "level": 2,
            "module": "m16-financial-institutions",
            "topic": "Analysis of Financial Institutions",
            "vignette_id": "V29",
            "vignette_title": "Aethelgard Life Assurance: Mortality, Surrender Margin, and Asset-Liability Matching",
            "vignette_text": v29_text,
            "los": "LOS 16.g: Describe the factors to consider when analyzing life and health insurance companies.",
            "question": "What was Aethelgard's Surrender Margin, and what risk does surrender activity pose in a rising interest rate environment?",
            "options": {
                "A": "Surrender Margin is 25 million USD; rising rates create disintermediation risk as policyholders surrender policies to seek higher market yields.",
                "B": "Surrender Margin is -25 million USD; rising rates force insurers to increase guaranteed crediting rates.",
                "C": "Surrender Margin is zero; surrenders only affect balance sheet cash."
            },
            "answer": "A",
            "explanation": (
                "1. Surrender Margin = Reserves Released - Surrender Values Paid:\n"
                "$$\\text{Surrender Margin} = 325 - 300 = +25 \\text{ million USD}$$\n"
                "Surrender charges assessed on departing policyholders retained 25 million USD of reserves.\n\n"
                "2. Disintermediation Risk:\n"
                "When market interest rates rise rapidly, competing investment vehicles (such as Treasury bills and bank CDs) offer attractive yields. "
                "Policyholders may surrender life and annuity contracts to reinvest elsewhere. If mass surrenders occur, the insurer is forced "
                "to sell long-term bonds at substantial unrealized capital losses to meet cash redemptions (disintermediation risk)."
            )
        },
        {
            "id": "L2-V29-Q3",
            "level": 2,
            "module": "m16-financial-institutions",
            "topic": "Analysis of Financial Institutions",
            "vignette_id": "V29",
            "vignette_title": "Aethelgard Life Assurance: Mortality, Surrender Margin, and Asset-Liability Matching",
            "vignette_text": v29_text,
            "los": "LOS 16.g: Describe the factors to consider when analyzing life and health insurance companies.",
            "question": "Evaluating Aethelgard's duration mismatch ($D_A = 11.0$ years vs $D_L = 14.5$ years), what happens to Aethelgard's capital surplus if market interest rates decline by 100 bps?",
            "options": {
                "A": "Surplus increases because bond values rise.",
                "B": "Surplus decreases because the present value of liabilities increases by more than the market value of assets.",
                "C": "Surplus remains unchanged because life insurance policy reserves are fixed by statute."
            },
            "answer": "B",
            "explanation": (
                "Here, the asset duration (11.0 years) is shorter than the liability duration (14.5 years), creating a negative duration gap ($D_A < D_L$).\n"
                "When interest rates fall:\n"
                "- Asset values rise by approximately $11.0\\% \\times \\text{Assets}$.\n"
                "- Present value of liabilities rises by approximately $14.5\\% \\times \\text{Liabilities}$.\n\n"
                "Because liabilities expand significantly faster than assets, the insurer's net equity/surplus (Assets minus Liabilities) "
                "shrinks, eroding regulatory capital solvency. Life insurers must match both duration and convexity to protect surplus."
            )
        },
        {
            "id": "L2-V29-Q4",
            "level": 2,
            "module": "m16-financial-institutions",
            "topic": "Analysis of Financial Institutions",
            "vignette_id": "V29",
            "vignette_title": "Aethelgard Life Assurance: Mortality, Surrender Margin, and Asset-Liability Matching",
            "vignette_text": v29_text,
            "los": "LOS 16.g: Describe the factors to consider when analyzing life and health insurance companies.",
            "question": "How does the investment asset allocation of a Life insurer differ from that of a Property & Casualty (P&C) insurer?",
            "options": {
                "A": "Life insurers hold substantially longer-duration bonds, private corporate debt, and commercial real estate mortgages to match predictable multi-decade liabilities.",
                "B": "Life insurers hold predominantly short-term Treasury bills and liquid cash.",
                "C": "Life insurers invest exclusively in high-beta equity securities."
            },
            "answer": "A",
            "explanation": (
                "Life insurance and annuity liabilities have very long horizons (spanning 20 to 40+ years) and predictable actuarial payout schedules. "
                "Consequently, life insurers have low immediate liquidity needs and can capture liquidity and duration premiums by allocating heavily "
                "to long-term corporate bonds, direct private placements, and commercial mortgage loans. P&C insurers, facing volatile and unpredictable "
                "claims, invest in shorter-duration, highly liquid securities."
            )
        },
        {
            "id": "L2-V29-Q5",
            "level": 2,
            "module": "m16-financial-institutions",
            "topic": "Analysis of Financial Institutions",
            "vignette_id": "V29",
            "vignette_title": "Aethelgard Life Assurance: Mortality, Surrender Margin, and Asset-Liability Matching",
            "vignette_text": v29_text,
            "los": "LOS 16.g: Describe the factors to consider when analyzing life and health insurance companies.",
            "question": "Under IFRS 17 (Insurance Contracts), how are life insurance contract liabilities valued on the balance sheet?",
            "options": {
                "A": "At unadjusted historical cost locked in at policy inception.",
                "B": "At current fulfillment cash flows (discounted present value of probability-weighted future cash flows plus risk adjustment) and Contractual Service Margin (CSM).",
                "C": "At undiscounted face value of the policy death benefit."
            },
            "answer": "B",
            "explanation": (
                "Under IFRS 17, insurance contract liabilities are valued using current measurement models:\n"
                "1. Fulfillment Cash Flows: Current discounted present value of expected future cash flows (premiums minus claims and expenses) "
                "discounted at current market rates, plus an explicit Risk Adjustment for non-financial risk.\n"
                "2. Contractual Service Margin (CSM): Represents unearned profit from the contract, recognized into earnings over the coverage period "
                "as insurance services are delivered.\n\n"
                "This replaces legacy accounting where discount rates were locked in at policy inception."
            )
        },
        {
            "id": "L2-V29-Q6",
            "level": 2,
            "module": "m16-financial-institutions",
            "topic": "Analysis of Financial Institutions",
            "vignette_id": "V29",
            "vignette_title": "Aethelgard Life Assurance: Mortality, Surrender Margin, and Asset-Liability Matching",
            "vignette_text": v29_text,
            "los": "LOS 16.g: Describe the factors to consider when analyzing life and health insurance companies.",
            "question": "In the NAIC Risk-Based Capital (RBC) framework for life insurers, which risk component captures bond default risk and equity market declines?",
            "options": {
                "A": "C-1 Risk (Asset Risk).",
                "B": "C-2 Risk (Insurance / Underwriting Risk).",
                "C": "C-3 Risk (Interest Rate Risk)."
            },
            "answer": "A",
            "explanation": (
                "In NAIC Life Risk-Based Capital (RBC):\n"
                "- C-1 Risk: Asset Risk (risk of asset default or market value depreciation on bonds, mortgages, and equities).\n"
                "- C-2 Risk: Insurance / Underwriting Risk (risk that actual mortality/morbidity claims exceed pricing assumptions).\n"
                "- C-3 Risk: Interest Rate Risk (risk of losses arising from asset-liability duration mismatch and disintermediation).\n"
                "- C-4 Risk: Business Risk (general litigation, fraud, guarantee fund assessments, and regulatory risks)."
            )
        }
    ]
    vignettes.append((v29_text, v29_questions))

    # =========================================================================
    # VIGNETTE 30: Comprehensive Financial Institution Evaluation & Conglomerate Analysis
    # =========================================================================
    v30_text = (
        "St. Jude Financial Holdings is a diversified financial conglomerate operating two core businesses: "
        "St. Jude Commercial Bank and St. Jude Life & Casualty Assurance. Equity research director "
        "Theresa Sterling, CFA, is conducting an integrated solvency, efficiency, and double-leverage "
        "assessment of the holding company and its regulated operating subsidiaries.\n\n"
        "Exhibit 1: St. Jude Commercial Bank Financial Profile (in billions of USD)\n"
        "- Total assets: 300.0 billion USD\n"
        "- Average interest-earning assets: 280.0 billion USD\n"
        "- Total gross loans: 200.0 billion USD\n"
        "- Non-performing loans (NPLs): 4.0 billion USD\n"
        "- Total interest income: 14.0 billion USD\n"
        "- Total interest expense: 7.0 billion USD\n"
        "- Non-interest income (fees & advisory): 3.0 billion USD\n"
        "- Non-interest expense (operating costs): 5.5 billion USD\n"
        "- Net income: 3.2 billion USD\n"
        "- CET1 Capital Ratio: 11.20%\n"
        "- Liquidity Coverage Ratio (LCR): 125.0%\n\n"
        "Exhibit 2: St. Jude Life & Casualty Assurance Profile (in billions of USD)\n"
        "- Invested assets: 80.0 billion USD\n"
        "- Net earned premiums: 12.0 billion USD\n"
        "- Incurred losses and LAE: 8.4 billion USD\n"
        "- Underwriting expenses: 3.24 billion USD\n"
        "- Net income: 1.4 billion USD\n"
        "- NAIC RBC Ratio: 340.0% (Company Action Level = 200%)\n\n"
        "Exhibit 3: Holding Company Standalone Capital & Debt (in billions of USD)\n"
        "- Standalone equity of parent holding company: 32.0 billion USD\n"
        "- Total equity investment in operating subsidiaries (Bank + Insurance): 40.0 billion USD\n"
        "- Standalone senior parent debt issued to fund subsidiary equity: 8.0 billion USD"
    )

    v30_questions = [
        {
            "id": "L2-V30-Q1",
            "level": 2,
            "module": "m16-financial-institutions",
            "topic": "Analysis of Financial Institutions",
            "vignette_id": "V30",
            "vignette_title": "St. Jude Financial Holdings: Integrated Bank and Insurance Group Valuation & Regulatory Assessment",
            "vignette_text": v30_text,
            "los": "LOS 16.a: Describe the CAMELS framework used to analyze financial institutions.",
            "question": "What are St. Jude Bank's Net Interest Margin (NIM) and Efficiency Ratio?",
            "options": {
                "A": "NIM: 2.50%; Efficiency Ratio: 55.0%.",
                "B": "NIM: 2.33%; Efficiency Ratio: 65.0%.",
                "C": "NIM: 2.50%; Efficiency Ratio: 45.0%."
            },
            "answer": "A",
            "explanation": (
                "1. Net Interest Margin (NIM):\n"
                "$$\\text{Net Interest Income (NII)} = \\text{Interest Income (14.0)} - \\text{Interest Expense (7.0)} = 7.0 \\text{ billion USD}$$\n"
                "$$\\text{NIM} = \\frac{\\text{Net Interest Income}}{\\text{Average Earning Assets}} = \\frac{7.0}{280.0} = 2.50\\%$$\n\n"
                "2. Efficiency Ratio:\n"
                "$$\\text{Total Revenue} = \\text{Net Interest Income (7.0)} + \\text{Non-Interest Income (3.0)} = 10.0 \\text{ billion USD}$$\n"
                "$$\\text{Efficiency Ratio} = \\frac{\\text{Non-Interest Expense}}{\\text{Total Revenue}} = \\frac{5.5}{10.0} = 55.0\\%$$\n\n"
                "A lower efficiency ratio indicates superior operating efficiency (spending 55 cents to generate one dollar of revenue).\n\n"
                "Distractor B divides NII by total assets ($7.0 / 300.0 = 2.33\\%$)."
            )
        },
        {
            "id": "L2-V30-Q2",
            "level": 2,
            "module": "m16-financial-institutions",
            "topic": "Analysis of Financial Institutions",
            "vignette_id": "V30",
            "vignette_title": "St. Jude Financial Holdings: Integrated Bank and Insurance Group Valuation & Regulatory Assessment",
            "vignette_text": v30_text,
            "los": "LOS 16.b: Describe the Basel III regulatory capital requirements and calculate regulatory capital ratios.",
            "question": "What is the Holding Company's Double Leverage Ratio, and what risk does it present to bondholders?",
            "options": {
                "A": "Double Leverage Ratio is 125.0%; indicates that parent debt funds subsidiary equity, subjecting parent debt service to subsidiary regulatory dividend capacity.",
                "B": "Double Leverage Ratio is 80.0%; indicates strong conservative capitalization.",
                "C": "Double Leverage Ratio is 100.0%; indicates zero holding company debt."
            },
            "answer": "A",
            "explanation": (
                "The Double Leverage Ratio measures the extent to which a holding company finances its equity investments in regulated "
                "operating subsidiaries with parent-level debt:\n"
                "$$\\text{Double Leverage Ratio} = \\frac{\\text{Holding Company Equity Investment in Subsidiaries}}{\\text{Holding Company Standalone Equity}} = \\frac{40.0}{32.0} = 125.0\\%$$\n\n"
                "A ratio greater than 100% means the parent issued 8.0 billion USD of debt to inject equity into its subsidiaries. "
                "Because parent debt service depends entirely on upstream dividends from regulated subsidiaries—which bank and insurance regulators "
                "can freeze during stress ('ring-fencing')—double leverage creates structural subordination and debt service vulnerability."
            )
        },
        {
            "id": "L2-V30-Q3",
            "level": 2,
            "module": "m16-financial-institutions",
            "topic": "Analysis of Financial Institutions",
            "vignette_id": "V30",
            "vignette_title": "St. Jude Financial Holdings: Integrated Bank and Insurance Group Valuation & Regulatory Assessment",
            "vignette_text": v30_text,
            "los": "LOS 16.f: Describe the factors to consider when analyzing property and casualty insurance companies.",
            "question": "What is the Combined Ratio of St. Jude Life & Casualty Assurance?",
            "options": {
                "A": "97.0%, indicating an underwriting profit of 3.0%.",
                "B": "103.5%, indicating an underwriting loss.",
                "C": "70.0%, indicating exceptional underwriting profit."
            },
            "answer": "A",
            "explanation": (
                "1. Loss Ratio = $\\frac{\\text{Losses & LAE}}{\\text{Net Earned Premiums}} = \\frac{8.4}{12.0} = 70.0\\%$.\n"
                "2. Expense Ratio = $\\frac{\\text{Underwriting Expenses}}{\\text{Net Earned Premiums}} = \\frac{3.24}{12.0} = 27.0\\%$.\n"
                "3. Combined Ratio = $\\text{Loss Ratio} + \\text{Expense Ratio} = 70.0\\% + 27.0\\% = 97.0\\%$.\n\n"
                "Because the Combined Ratio is below 100%, the insurance operation generates an underwriting profit of $100\\% - 97.0\\% = 3.0\\%$."
            )
        },
        {
            "id": "L2-V30-Q4",
            "level": 2,
            "module": "m16-financial-institutions",
            "topic": "Analysis of Financial Institutions",
            "vignette_id": "V30",
            "vignette_title": "St. Jude Financial Holdings: Integrated Bank and Insurance Group Valuation & Regulatory Assessment",
            "vignette_text": v30_text,
            "los": "LOS 16.a: Describe the CAMELS framework used to analyze financial institutions.",
            "question": "What is the primary diversification benefit of combining commercial banking and insurance operations within a financial holding company?",
            "options": {
                "A": "Complete exemption from Basel III capital regulations.",
                "B": "Uncorrelated revenue streams, where banking earnings (driven by credit spreads and interest cycles) offset insurance underwriting results (driven by weather and actuarial loss cycles).",
                "C": "Ability to freely commingle customer deposits with insurance policy reserves."
            },
            "answer": "B",
            "explanation": (
                "Commercial banking earnings are driven by credit cycles, interest rate yield curves, and loan origination volume. "
                "In contrast, property and casualty insurance underwriting profits are driven by natural catastrophe events, weather patterns, "
                "and insurance pricing cycles, which exhibit low correlation with macroeconomic credit cycles. Combining them dampens consolidated "
                "earnings volatility."
            )
        },
        {
            "id": "L2-V30-Q5",
            "level": 2,
            "module": "m16-financial-institutions",
            "topic": "Analysis of Financial Institutions",
            "vignette_id": "V30",
            "vignette_title": "St. Jude Financial Holdings: Integrated Bank and Insurance Group Valuation & Regulatory Assessment",
            "vignette_text": v30_text,
            "los": "LOS 16.b: Describe the Basel III regulatory capital requirements and calculate regulatory capital ratios.",
            "question": "What does the regulatory concept of 'capital and liquidity ring-fencing' imply for holding company creditors during a financial crisis?",
            "options": {
                "A": "Holding company debt is guaranteed by the federal central bank.",
                "B": "Bank and insurance regulators have statutory power to block dividends or capital transfers from the operating subsidiaries to the parent, trapping cash at the operating level.",
                "C": "All subsidiary assets are automatically liquidated to pay parent bondholders."
            },
            "answer": "B",
            "explanation": (
                "Prudential bank supervisors and insurance regulators prioritize policyholder and depositor protection over parent holding company "
                "bondholders. Under ring-fencing rules, regulators can restrict or prohibit regulated operating entities from distributing dividends, "
                "granting intercompany loans, or transferring liquidity to the parent company. Consequently, a parent holding company may default "
                "on its standalone debt even while its underlying subsidiaries remain adequately capitalized."
            )
        },
        {
            "id": "L2-V30-Q6",
            "level": 2,
            "module": "m16-financial-institutions",
            "topic": "Analysis of Financial Institutions",
            "vignette_id": "V30",
            "vignette_title": "St. Jude Financial Holdings: Integrated Bank and Insurance Group Valuation & Regulatory Assessment",
            "vignette_text": v30_text,
            "los": "LOS 16.a: Describe the CAMELS framework used to analyze financial institutions.",
            "question": "Synthesizing the overall financial health of St. Jude's operating units across capital adequacy, asset quality, and liquidity:",
            "options": {
                "A": "Both the bank (CET1 11.2%, LCR 125%, NPL 2.0%) and insurer (RBC 340%, Combined Ratio 97%) exhibit strong standalone solvency and operating profitability.",
                "B": "The bank is severely undercapitalized and violates minimum LCR standards.",
                "C": "The insurance subsidiary is insolvent because its RBC ratio is below the 200% Company Action Level."
            },
            "answer": "A",
            "explanation": (
                "Synthesizing the key indicators:\n"
                "- Bank: CET1 Ratio of 11.20% (vs 7.0% buffered requirement), LCR of 125.0% (vs 100% floor), and NPL ratio of $4.0 / 200.0 = 2.00\\%$ "
                "reflect excellent capital strength, strong short-term liquidity, and sound asset quality.\n"
                "- Insurer: NAIC RBC Ratio of 340.0% is well above the 200.0% Company Action Level, and Combined Ratio of 97.0% confirms underwriting profitability.\n"
                "Both operating units demonstrate robust standalone solvency."
            )
        }
    ]
    vignettes.append((v30_text, v30_questions))

    return vignettes

if __name__ == "__main__":
    vigs = get_vignettes_24_to_30()
    total_q = sum(len(q_list) for _, q_list in vigs)
    print(f"Generated {len(vigs)} vignettes with {total_q} questions for Topic 16.")
