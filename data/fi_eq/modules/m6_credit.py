# -*- coding: utf-8 -*-
"""
Module 6: Fundamentals of Credit Analysis (Q73-Q85)
CFA Level 1 Fixed Income Question Bank
"""

M6_QUESTIONS = [
    {
        "id": "L1-FI-073",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Fundamentals of Credit Analysis",
        "los": "Describe credit risk and explain its components: probability of default and loss given default",
        "question": "A portfolio manager holds a corporate bond with an estimated 1-year probability of default (PD) of 2.50%. If the anticipated recovery rate in default is 40.0%, the expected loss percentage for the coming year is closest to:",
        "options": {
            "A": "1.00%.",
            "B": "1.50%.",
            "C": "2.50%."
        },
        "answer": "B",
        "explanation": "Expected loss is calculated as the probability of default (PD) multiplied by the loss severity (loss given default, LGD): $$\\text{LGD} = 1 - \\text{Recovery Rate} = 1 - 0.40 = 0.60 = 60.0\\%$$ $$\\text{Expected Loss} = \\text{PD} \\times \\text{LGD} = 2.50\\% \\times 60.0\\% = 1.50\\%$$",
        "distractor_analysis": {
            "A": "Incorrect because 1.00% is computed by multiplying PD by the recovery rate ($2.50\\% \\times 0.40 = 1.00\\%$), representing the expected recovery rather than expected loss.",
            "C": "Incorrect because 2.50% is the probability of default, assuming 0% recovery (100% loss severity)."
        }
    },
    {
        "id": "L1-FI-074",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Fundamentals of Credit Analysis",
        "los": "Describe seniority rankings and priority of claims in bankruptcy",
        "question": "In a corporate liquidation bankruptcy proceeding governed by the absolute priority rule, which of the following creditor classes has the highest priority of claim?",
        "options": {
            "A": "Senior unsecured debt.",
            "B": "First lien senior secured debt.",
            "C": "Subordinated (junior) debt."
        },
        "answer": "B",
        "explanation": "Under the absolute priority rule, claims are satisfied in order of seniority: (1) First lien secured debt (backed by specific pledged collateral assets), (2) Second lien secured debt, (3) Senior unsecured debt, (4) Subordinated debt, (5) Preferred equity, and (6) Common equity. Therefore, first lien senior secured debt holds the highest claim on the pledged collateral and bankruptcy proceeds.",
        "distractor_analysis": {
            "A": "Incorrect because senior unsecured debt ranks below secured debt claims up to the value of pledged collateral.",
            "C": "Incorrect because subordinated debt is junior to both secured and senior unsecured debt."
        }
    },
    {
        "id": "L1-FI-075",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Fundamentals of Credit Analysis",
        "los": "Describe seniority rankings and priority of claims in bankruptcy",
        "question": "A holding company owns 100% of an operating company subsidiary. The operating subsidiary has its own outstanding senior debt. If the parent holding company issues senior unsecured debt, the parent debt is best described as being:",
        "options": {
            "A": "Structurally subordinated to the operating company debt.",
            "B": "Senior in claim to all operating company debt under the pari passu doctrine.",
            "C": "Fully collateralized by the operating company's tangible fixed assets."
        },
        "answer": "A",
        "explanation": "Structural subordination arises when debt is issued by a parent holding company while debt is also issued by operating subsidiaries. Because the operating company owns the revenue-generating operating assets, its operating cash flows must first satisfy operating subsidiary creditors. The parent holding company's only claim is as an equity shareholder of the operating company (residual claim). Thus, parent debt is effectively subordinated to subsidiary debt, even if both are titled 'senior unsecured'.",
        "distractor_analysis": {
            "B": "Incorrect because pari passu applies only to debt at the same legal entity level; parent debt does not rank equally with operating company debt.",
            "C": "Incorrect because parent unsecured debt has no direct lien or collateral claim on the subsidiary's physical assets."
        }
    },
    {
        "id": "L1-FI-076",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Fundamentals of Credit Analysis",
        "los": "Describe rating agencies and credit ratings",
        "question": "A corporate bond currently rated BBB- by S&P and Baa3 by Moody's is downgraded by one notch by both agencies. Following the downgrade, the bond is classified as:",
        "options": {
            "A": "Investment grade.",
            "B": "High yield (non-investment grade).",
            "C": "Defaulted debt."
        },
        "answer": "B",
        "explanation": "The boundary between investment grade and high yield (speculative/junk) is BBB- (S&P/Fitch) and Baa3 (Moody's). A one-notch downgrade drops the rating to BB+ (S&P) and Ba1 (Moody's). This crosses the threshold into high yield (non-investment grade). Bonds that cross from investment grade down into high yield are termed 'fallen angels'.",
        "distractor_analysis": {
            "A": "Incorrect because BBB-/Baa3 was the lowest investment grade notch; any downgrade drops the security into speculative grade.",
            "C": "Incorrect because default classification (D or C) only occurs upon non-payment or formal bankruptcy filing, not at BB+/Ba1."
        }
    },
    {
        "id": "L1-FI-077",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Fundamentals of Credit Analysis",
        "los": "Describe rating agencies and credit ratings",
        "question": "The risk that a bond's credit rating will be lowered, causing its credit spread to widen and its market price to decline prior to any actual default, is best termed:",
        "options": {
            "A": "Insolvency risk.",
            "B": "Rating migration (downgrade) risk.",
            "C": "Loss given default risk."
        },
        "answer": "B",
        "explanation": "Credit rating migration risk (downgrade risk) is the probability that an issuer's credit rating will deteriorate (migrate downward) across credit rating categories over time. When an issuer is downgraded, market participants demand a wider credit spread to hold the debt, leading to an immediate decline in bond market value even if no cash flow default has occurred.",
        "distractor_analysis": {
            "A": "Incorrect because insolvency refers to total inability to service debt obligations or liabilities exceeding assets.",
            "C": "Incorrect because loss given default (LGD) measures the percentage severity of loss realized only after a default occurs."
        }
    },
    {
        "id": "L1-FI-078",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Fundamentals of Credit Analysis",
        "los": "Describe the 4 Cs of credit analysis",
        "question": "An analyst reviewing a corporate issuer's indenture notes covenants requiring a minimum interest coverage ratio and restricting additional debt incurrence. Under the '4 Cs of Credit Analysis' framework, this examination relates to:",
        "options": {
            "A": "Capacity.",
            "B": "Collateral.",
            "C": "Covenants."
        },
        "answer": "C",
        "explanation": "The 4 Cs of credit analysis are Capacity (ability of the borrower to service debt from cash flows), Collateral (quality and value of assets pledged), Covenants (contractual terms and legal protections in the indenture), and Character (management integrity, track record, and governance). Indenture terms restricting debt incurrence and establishing financial coverage thresholds belong strictly to Covenants.",
        "distractor_analysis": {
            "A": "Incorrect because capacity examines industry structure, operating margins, cash flow generation, and financial statement ratios.",
            "B": "Incorrect because collateral evaluates the market value, liquidity, and depreciation of physical or financial assets pledged as security."
        }
    },
    {
        "id": "L1-FI-079",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Fundamentals of Credit Analysis",
        "los": "Describe the 4 Cs of credit analysis",
        "question": "When assessing the 'Capacity' of a corporate borrower, an industry characterized by high barriers to entry, low operating leverage, and stable pricing power is generally viewed by credit analysts as having:",
        "options": {
            "A": "Lower credit risk and higher business profile strength.",
            "B": "Higher exposure to cyclical cash flow volatility.",
            "C": "Greater threat of substitute products eroding operating margins."
        },
        "answer": "A",
        "explanation": "In evaluating borrower capacity, industry fundamentals heavily influence business risk. High barriers to entry protect existing firms from new entrants; low operating leverage reduces sensitivity of operating income to sales fluctuations; and stable pricing power enables firms to pass cost increases to customers. These characteristics provide consistent, predictable cash flow generation, resulting in a stronger business profile and lower credit risk.",
        "distractor_analysis": {
            "B": "Incorrect because low operating leverage and high entry barriers dampen cyclical cash flow volatility.",
            "C": "Incorrect because strong pricing power and entry barriers indicate low threat of substitutes and stable margins."
        }
    },
    {
        "id": "L1-FI-080",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Fundamentals of Credit Analysis",
        "los": "Calculate and interpret financial ratios used in credit analysis",
        "question": "A corporate borrower reports the following financial data for the most recent year:\n- Operating Income (EBIT): USD 120,000,000\n- Depreciation & Amortization: USD 30,000,000\n- Gross Interest Expense: USD 25,000,000\n- Total Debt: USD 450,000,000\nThe issuer's EBITDA interest coverage ratio and Debt-to-EBITDA ratio are closest to:",
        "options": {
            "A": "EBITDA Coverage = 4.8x; Debt/EBITDA = 3.75x.",
            "B": "EBITDA Coverage = 6.0x; Debt/EBITDA = 3.00x.",
            "C": "EBITDA Coverage = 6.0x; Debt/EBITDA = 3.75x."
        },
        "answer": "B",
        "explanation": "First, calculate EBITDA: $$\\text{EBITDA} = \\text{EBIT} + \\text{D\\&A} = \\text{USD } 120{,}000{,}000 + \\text{USD } 30{,}000{,}000 = \\text{USD } 150{,}000{,}000$$ Next, compute the EBITDA interest coverage ratio: $$\\text{EBITDA Interest Coverage} = \\frac{\\text{EBITDA}}{\\text{Interest Expense}} = \\frac{\\text{USD } 150{,}000{,}000}{\\text{USD } 25{,}000{,}000} = 6.0\\text{x}$$ Finally, compute the Debt-to-EBITDA leverage ratio: $$\\frac{\\text{Total Debt}}{\\text{EBITDA}} = \\frac{\\text{USD } 450{,}000{,}000}{\\text{USD } 150{,}000{,}000} = 3.00\\text{x}$$",
        "distractor_analysis": {
            "A": "Incorrect because 4.8x is the EBIT interest coverage ($120 / 25 = 4.8\\text{x}$), and 3.75x is Debt/EBIT ($450 / 120 = 3.75\\text{x}$).",
            "C": "Incorrect because Debt/EBITDA is 3.00x ($450 / 150 = 3.00\\text{x}$), not 3.75x."
        }
    },
    {
        "id": "L1-FI-081",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Fundamentals of Credit Analysis",
        "los": "Describe factors that influence the level and volatility of yield spreads",
        "question": "A corporate bond yield spread over benchmark government bonds primarily compensates investors for:",
        "options": {
            "A": "Default risk, liquidity risk, and tax differentials.",
            "B": "Only the expected loss from default, with zero premium for secondary market illiquidity.",
            "C": "Expected changes in the real risk-free rate of interest."
        },
        "answer": "A",
        "explanation": "The yield spread on a corporate bond over a risk-free benchmark bond of matching maturity reflects three primary components: (1) credit risk (both expected loss and a risk premium for unexpected default loss), (2) liquidity risk premium (corporate bonds trade less frequently and carry higher transaction costs than sovereign debt), and (3) tax considerations (e.g., differential tax treatment between municipal, corporate, and sovereign issues).",
        "distractor_analysis": {
            "B": "Incorrect because credit spreads include substantial compensation for liquidity risk and unexpected default risk.",
            "C": "Incorrect because changes in the benchmark real risk-free rate are already embedded within the underlying government benchmark yield, not the spread."
        }
    },
    {
        "id": "L1-FI-082",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Fundamentals of Credit Analysis",
        "los": "Describe factors that influence the level and volatility of yield spreads",
        "question": "During a severe macroeconomic recession accompanied by market-wide risk aversion and a contraction in dealer balance sheet capacity, corporate credit spreads will most likely:",
        "options": {
            "A": "Narrow due to falling benchmark interest rates.",
            "B": "Widen due to rising default probabilities and increased liquidity premiums.",
            "C": "Remain unchanged because duration offsets credit spread changes."
        },
        "answer": "B",
        "explanation": "During economic downturns, corporate operating cash flows decline, increasing leverage and default risk. Simultaneously, market liquidity dries up and dealer risk appetite shrinks, driving liquidity risk premiums higher. Both effects compound to cause corporate credit spreads to widen significantly. High-yield spreads typically widen by substantially more than investment-grade spreads.",
        "distractor_analysis": {
            "A": "Incorrect because even though benchmark risk-free rates often decline during recessions due to central bank easing, credit spreads widen dramatically.",
            "C": "Incorrect because duration measures price sensitivity to interest rate changes and does not prevent credit spreads from widening."
        }
    },
    {
        "id": "L1-FI-083",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Fundamentals of Credit Analysis",
        "los": "Describe special considerations when analyzing high-yield bonds",
        "question": "When conducting credit analysis on high-yield corporate issuers, an analyst must place disproportionate emphasis on:",
        "options": {
            "A": "Long-term macroeconomic cycles rather than short-term liquidity.",
            "B": "Short-term liquidity, near-term debt maturity schedules, and covenant headroom.",
            "C": "Accounting earnings (net income) rather than cash flow generation."
        },
        "answer": "B",
        "explanation": "High-yield issuers carry speculative credit profiles with elevated default risk. In high-yield analysis, immediate survival is paramount; thus, analysts focus intensely on short-term liquidity (cash balances, working capital, undrawn revolving bank lines), upcoming debt maturities ('maturity walls' over the next 12-24 months), covenant cushion/headroom, and collateral values. Long-term forecasting is less reliable if the issuer cannot survive near-term refinancing pressures.",
        "distractor_analysis": {
            "A": "Incorrect because high-yield issuers frequently default due to short-term liquidity crunches rather than multi-decade macro cycles.",
            "C": "Incorrect because non-cash accounting net income can easily obscure impending liquidity failure; free cash flow is far more critical."
        }
    },
    {
        "id": "L1-FI-084",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Fundamentals of Credit Analysis",
        "los": "Describe sovereign credit analysis and non-sovereign credit analysis",
        "question": "In sovereign credit analysis, which of the following characteristics provides the greatest flexibility for a government to service its sovereign debt during a fiscal crisis?",
        "options": {
            "A": "Denominating debt primarily in foreign currencies with short maturities.",
            "B": "Having an independent central bank with the authority to issue the currency in which the debt is denominated.",
            "C": "Relying heavily on foreign capital inflows to finance current account deficits."
        },
        "answer": "B",
        "explanation": "A sovereign government that issues debt in its own domestic currency and possesses monetary independence (via its own central bank) has the theoretical ability to print currency to service its debt obligations. While monetary expansion carries inflation and currency depreciation risks, outright legal default is far less likely than for a sovereign that borrows in foreign currency (which cannot be printed by the domestic central bank).",
        "distractor_analysis": {
            "A": "Incorrect because foreign currency debt exposes the sovereign to foreign exchange risk and cannot be serviced by domestic money printing.",
            "C": "Incorrect because dependence on external financing leaves the country vulnerable to sudden stops in foreign capital flows."
        }
    },
    {
        "id": "L1-FI-085",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Fundamentals of Credit Analysis",
        "los": "Describe sovereign credit analysis and non-sovereign credit analysis",
        "question": "A key difference between municipal General Obligation (GO) bonds and municipal Revenue bonds is that Revenue bonds are:",
        "options": {
            "A": "Backed by the full taxing authority of the issuing municipality.",
            "B": "Serviced solely from cash flows generated by a designated public enterprise or project.",
            "C": "Exempt from all credit rating analysis due to statutory sovereign immunity."
        },
        "answer": "B",
        "explanation": "Municipal bonds generally fall into two broad categories: General Obligation (GO) bonds and Revenue bonds. GO bonds are backed by the 'full faith, credit, and taxing power' of the issuing municipality, giving them access to broad ad valorem property and income taxes. In contrast, Revenue bonds are backed exclusively by revenues generated by a specific commercial project (such as toll roads, airports, or water utilities). If project cash flows prove insufficient, the municipality is typically not legally obligated to draw on general tax revenues to service the debt.",
        "distractor_analysis": {
            "A": "Incorrect because full taxing authority backs General Obligation (GO) bonds, not project revenue bonds.",
            "C": "Incorrect because Revenue bonds undergo rigorous credit ratings and financial analysis (e.g., debt service coverage ratios)."
        }
    }
]
