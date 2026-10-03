# -*- coding: utf-8 -*-
"""
Module 4: Introduction to Asset-Backed Securities (Q45-Q56)
CFA Level 1 Fixed Income Question Bank
"""

M4_QUESTIONS = [
    {
        "id": "L1-FI-045",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Introduction to Asset-Backed Securities",
        "los": "Explain benefits of securitization for the financial system and alternative structures",
        "question": "In a typical securitization transaction, transferring loans from the originating bank to a Special Purpose Entity (SPE) achieves which of the following primary legal objectives?",
        "options": {
            "A": "It eliminates the need for credit rating agencies to assess the transaction.",
            "B": "It establishes bankruptcy remoteness, isolating the collateral assets from the originator's financial distress.",
            "C": "It removes the requirement to pay loan servicing and administrative fees."
        },
        "answer": "B",
        "explanation": "The creation of an SPE (or SPV) achieves bankruptcy remoteness. When the originator sells loans to the SPE via a legally valid 'true sale', the assets are separated from the originator's balance sheet. If the originator enters bankruptcy or liquidation, creditors of the originator have no claim against the assets held by the SPE, allowing the issued securities to achieve higher credit ratings than the originator itself.",
        "distractor_analysis": {
            "A": "Incorrect because securitizations heavily rely on credit rating agencies to evaluate credit enhancements and assign tranche ratings.",
            "C": "Incorrect because the servicer must still be compensated for collecting payments and administering the loans."
        }
    },
    {
        "id": "L1-FI-046",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Introduction to Asset-Backed Securities",
        "los": "Describe types and characteristics of residential mortgage loans",
        "question": "A homebuyer purchases a residential property appraised at USD 500,000 using a USD 100,000 cash down payment and taking out a USD 400,000 mortgage loan. The loan-to-value (LTV) ratio of this mortgage is closest to:",
        "options": {
            "A": "20.0%.",
            "B": "25.0%.",
            "C": "80.0%."
        },
        "answer": "C",
        "explanation": "The loan-to-value (LTV) ratio measures the amount of the loan relative to the appraised value of the underlying collateral property: $$\\text{LTV} = \\frac{\\text{Loan Amount}}{\\text{Appraised Property Value}} = \\frac{\\text{USD } 400{,}000}{\\text{USD } 500{,}000} = 80.0\\%$$ A lower LTV ratio indicates greater homeowner equity and lower credit risk for the mortgage lender.",
        "distractor_analysis": {
            "A": "Incorrect because 20.0% is the down payment percentage ($100{,}000 / 500{,}000 = 0.20$), which equals $1 - \\text{LTV}$.",
            "B": "Incorrect because 25.0% calculates the down payment relative to the loan amount ($100{,}000 / 400{,}000 = 0.25$)."
        }
    },
    {
        "id": "L1-FI-047",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Introduction to Asset-Backed Securities",
        "los": "Describe characteristics and risks of mortgage-backed securities",
        "question": "In an agency residential mortgage pass-through security, the pass-through coupon rate paid to investors is strictly less than the weighted average coupon (WAC) of the underlying mortgage pool because of:",
        "options": {
            "A": "Servicing, guarantee, and administrative fees deducted from cash flows.",
            "B": "Scheduled principal prepayments retained by the government sponsor.",
            "C": "Subordination losses absorbed by the senior pass-through tranche."
        },
        "answer": "A",
        "explanation": "The pass-through rate (net interest rate received by investors) is lower than the mortgage coupon rate (WAC paid by homeowners) because servicing fees (paid to the loan servicer) and guarantee fees (paid to the agency guarantor like Fannie Mae or Freddie Mac) are subtracted from the gross interest collections before funds are distributed to investors.",
        "distractor_analysis": {
            "B": "Incorrect because all scheduled principal and prepayments are passed through to the investors, not retained by the agency.",
            "C": "Incorrect because agency mortgage pass-through securities do not use subordination; they carry credit guarantees from the sponsoring agency."
        }
    },
    {
        "id": "L1-FI-048",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Introduction to Asset-Backed Securities",
        "los": "Describe characteristics and risks of mortgage-backed securities",
        "question": "When market mortgage rates decline sharply, holders of fixed-rate mortgage pass-through securities are most exposed to:",
        "options": {
            "A": "Extension risk.",
            "B": "Contraction risk.",
            "C": "Credit default risk."
        },
        "answer": "B",
        "explanation": "When interest rates decline, homeowners have an economic incentive to refinance their mortgages at lower rates, resulting in a surge in prepayments. This shortens the effective life of the MBS, forcing investors to receive their principal back earlier than anticipated and reinvest it at prevailing lower market yields. This form of prepayment risk is termed contraction risk. Extension risk, conversely, occurs when interest rates rise and prepayments slow down.",
        "distractor_analysis": {
            "A": "Incorrect because extension risk occurs when interest rates rise and mortgage prepayments decelerate, extending bond life.",
            "C": "Incorrect because agency pass-throughs carry negligible default risk due to explicit or implicit government guarantees."
        }
    },
    {
        "id": "L1-FI-049",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Introduction to Asset-Backed Securities",
        "los": "Describe characteristics and risks of mortgage-backed securities",
        "question": "An MBS collateral pool is projected to prepay at 150% PSA. If the standard 100% PSA benchmark specifies a conditional prepayment rate (CPR) of 4.00% at month 20, the projected CPR under 150% PSA for month 20 is closest to:",
        "options": {
            "A": "2.67%.",
            "B": "4.00%.",
            "C": "6.00%."
        },
        "answer": "C",
        "explanation": "The Public Securities Association (PSA) benchmark scales the standard CPR curve proportionally: $$\\text{Projected CPR} = \\text{PSA Multiplier} \\times \\text{Benchmark CPR}$$ For 150% PSA: $$\\text{Projected CPR} = 1.50 \\times 4.00\\% = 6.00\\%$$ A PSA speed above 100% indicates prepayments faster than the historical baseline.",
        "distractor_analysis": {
            "A": "Incorrect because 2.67% divides the benchmark CPR by 1.50 ($4.00\\% / 1.50 = 2.67\\%$) instead of multiplying.",
            "B": "Incorrect because 4.00% represents the baseline 100% PSA speed without scaling."
        }
    },
    {
        "id": "L1-FI-050",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Introduction to Asset-Backed Securities",
        "los": "Describe characteristics and risks of collateralized mortgage obligations",
        "question": "In a sequential-pay Collateralized Mortgage Obligation (CMO) with tranches A, B, and C, all principal payments (scheduled principal and prepayments) are initially directed entirely to:",
        "options": {
            "A": "Tranche A until it is completely retired.",
            "B": "Tranches A, B, and C pro-rata according to their initial par values.",
            "C": "Tranche C to insulate the senior tranches from prepayment risk."
        },
        "answer": "A",
        "explanation": "In a sequential-pay CMO structure, tranches are retired in sequential order. All tranches receive interest periodically based on their outstanding principal balances, but all principal cash flows (both scheduled repayments and prepayments) are directed exclusively to the shortest tranche (Tranche A) until it is fully paid off. Only then does Tranche B begin receiving principal, followed by Tranche C. This structure redistributes contraction risk primarily to Tranche A and extension risk primarily to Tranche C.",
        "distractor_analysis": {
            "B": "Incorrect because pro-rata distribution describes a plain pass-through structure, not a sequential-pay CMO.",
            "C": "Incorrect because Tranche C is the longest tranche and receives principal only after Tranches A and B have been retired."
        }
    },
    {
        "id": "L1-FI-051",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Introduction to Asset-Backed Securities",
        "los": "Describe characteristics and risks of collateralized mortgage obligations",
        "question": "In a CMO structure featuring Planned Amortization Class (PAC) tranches and support (companion) tranches, the support tranches protect the PAC tranches from prepayment risk by:",
        "options": {
            "A": "Absorbing excess prepayments when rates fall and forgoing principal when rates rise, as long as prepayments remain within the PAC collar.",
            "B": "Guaranteeing credit default losses through third-party letters of credit.",
            "C": "Receiving all interest payments before any interest is distributed to the PAC tranches."
        },
        "answer": "A",
        "explanation": "PAC tranches offer predictable principal repayment schedules as long as actual prepayment speeds remain within a pre-specified initial collar (e.g., 100% to 250% PSA). The support (companion) tranches provide this stability by acting as shock absorbers: if prepayments accelerate, the support tranches absorb the extra principal (protecting PAC against contraction risk); if prepayments slow down, principal payments to support tranches are deferred to satisfy the PAC schedule (protecting PAC against extension risk).",
        "distractor_analysis": {
            "B": "Incorrect because support tranches redistribute prepayment risk, not credit default protection via letters of credit.",
            "C": "Incorrect because interest is paid concurrently to all outstanding tranches based on their respective coupon rates; companion tranches do not take priority over PAC interest."
        }
    },
    {
        "id": "L1-FI-052",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Introduction to Asset-Backed Securities",
        "los": "Describe types and characteristics of non-mortgage asset-backed securities",
        "question": "Which of the following methods of credit enhancement in a non-agency asset-backed security is classified as an external credit enhancement?",
        "options": {
            "A": "Subordination (credit tranching).",
            "B": "Overcollateralization.",
            "C": "A financial guarantee from a monoline bond insurer."
        },
        "answer": "C",
        "explanation": "External credit enhancements rely on third-party financial institutions to guarantee or reimburse losses, such as monoline insurance wrap policies, letters of credit from commercial banks, or corporate parent guarantees. In contrast, subordination (senior/subordinated credit tranching), overcollateralization (pledging more assets than the debt issued), and excess spread (interest margin) are internal credit enhancements built into the cash flow structure itself.",
        "distractor_analysis": {
            "A": "Incorrect because subordination is an internal credit enhancement mechanism established via the structural waterfall.",
            "B": "Incorrect because overcollateralization is an internal credit enhancement created by issuing debt with face value lower than the underlying collateral."
        }
    },
    {
        "id": "L1-FI-053",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Introduction to Asset-Backed Securities",
        "los": "Describe characteristics and risks of commercial mortgage-backed securities",
        "question": "A commercial real estate property generates an annual net operating income (NOI) of USD 1,800,000. The annual debt service on the underlying commercial mortgage is USD 1,200,000, and the current property valuation is USD 15,000,000 with an outstanding mortgage balance of USD 9,000,000. The Debt Service Coverage Ratio (DSCR) and Loan-to-Value (LTV) ratio are closest to:",
        "options": {
            "A": "DSCR = 1.20; LTV = 80.0%.",
            "B": "DSCR = 1.50; LTV = 60.0%.",
            "C": "DSCR = 1.50; LTV = 80.0%."
        },
        "answer": "B",
        "explanation": "The Debt Service Coverage Ratio (DSCR) is defined as: $$\\text{DSCR} = \\frac{\\text{Net Operating Income}}{\\text{Annual Debt Service}} = \\frac{\\text{USD } 1{,}800{,}000}{\\text{USD } 1{,}200{,}000} = 1.50$$ The Loan-to-Value (LTV) ratio is defined as: $$\\text{LTV} = \\frac{\\text{Mortgage Balance}}{\\text{Property Value}} = \\frac{\\text{USD } 9{,}000{,}000}{\\text{USD } 15{,}000{,}000} = 60.0\\%$$ A DSCR $> 1.0$ indicates that property cash flows are sufficient to service the debt.",
        "distractor_analysis": {
            "A": "Incorrect because DSCR is 1.50, not 1.20, and LTV is 60%, not 80%.",
            "C": "Incorrect because LTV is computed as $9{,}000{,}000 / 15{,}000{,}000 = 0.60$ (60%), not 80%."
        }
    },
    {
        "id": "L1-FI-054",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Introduction to Asset-Backed Securities",
        "los": "Describe characteristics and risks of commercial mortgage-backed securities",
        "question": "In commercial mortgage-backed securities (CMBS), which loan-level call protection mechanism requires the borrower to replace the mortgaged commercial property with a portfolio of sovereign government bonds replicating the remaining mortgage cash flows?",
        "options": {
            "A": "Defeasance.",
            "B": "Prepayment penalty points.",
            "C": "Yield maintenance."
        },
        "answer": "A",
        "explanation": "Defeasance is a common loan-level call protection clause in commercial mortgages. Instead of prepaying cash to retire the loan, the borrower purchases and pledges a dedicated portfolio of default-free government securities (such as US Treasuries) whose cash flows exactly replicate the remaining principal and interest payments of the mortgage. This eliminates prepayment disruption and elevates the credit quality of the underlying collateral.",
        "distractor_analysis": {
            "B": "Incorrect because prepayment penalty points are pre-agreed percentage fees (e.g., 2% of prepaid balance) charged directly to the borrower upon early repayment.",
            "C": "Incorrect because yield maintenance requires the borrower to pay a penalty equal to the present value of the lost spread so the lender maintains their contractual yield."
        }
    },
    {
        "id": "L1-FI-055",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Introduction to Asset-Backed Securities",
        "los": "Describe types and characteristics of non-mortgage asset-backed securities",
        "question": "Auto loan-backed securities typically differ from residential mortgage-backed securities in that auto loan ABS:",
        "options": {
            "A": "Are backed by non-amortizing, revolving consumer receivables.",
            "B": "Have substantially shorter collateral maturities and lower prepayment sensitivity to interest rates.",
            "C": "Do not require internal credit enhancements such as reserve accounts or subordination."
        },
        "answer": "B",
        "explanation": "Auto loans are fully amortizing loans with relatively short original maturities (typically 36 to 72 months). Because auto loan balances are smaller and vehicles depreciate rapidly, borrowers rarely refinance auto loans simply because market interest rates drop. Prepayments on auto loans occur primarily due to trade-ins, sales, wrecks, or payoffs, making them far less sensitive to interest rate fluctuations than home mortgages.",
        "distractor_analysis": {
            "A": "Incorrect because credit card receivables are non-amortizing and revolving; auto loans are fully amortizing installment contracts.",
            "C": "Incorrect because auto loan ABS rely heavily on internal credit enhancement, including subordination, reserve funds, and excess spread."
        }
    },
    {
        "id": "L1-FI-056",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Introduction to Asset-Backed Securities",
        "los": "Describe types and characteristics of non-mortgage asset-backed securities",
        "question": "During the lockout (revolving) period of a credit card asset-backed security (ABS):",
        "options": {
            "A": "Principal payments made by cardholders are distributed sequentially to bondholders.",
            "B": "Principal payments made by cardholders are reinvested by the trustee in new receivables.",
            "C": "No interest payments are made to investors, with interest compounding until maturity."
        },
        "answer": "B",
        "explanation": "Credit card ABS are backed by revolving debt. During the initial lockout or revolving period (which may last 1 to 5 years), no principal is returned to investors. Instead, principal collections from cardholders are used by the trust to purchase newly originated credit card receivables, keeping the pool balance stable. Investors receive only contractual interest. Principal repayment occurs only after the revolving period ends (during the accumulation or amortization period).",
        "distractor_analysis": {
            "A": "Incorrect because principal is not returned to investors during the revolving lockout phase.",
            "C": "Incorrect because investors receive regular monthly or quarterly coupon interest throughout the lockout period."
        }
    }
]
