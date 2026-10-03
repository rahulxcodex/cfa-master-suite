r"""
CFA Level 2 Equity Valuation Vignette Question Generator
Generates exactly 85 questions across 17 clinical item sets (V01 to V17, 5 questions each).
Strict rule compliance:
- No '$' symbol used for currency (uses USD, EUR, GBP, CAD, JPY or escaped '\$').
- '$' strictly reserved for LaTeX math mode ($...$ or $$...$$).
- JSON output validated for schema, question counts, and math delimiter integrity.
"""

import json
import re
import sys
from pathlib import Path

def get_vignettes():
    vignettes = []

    # =========================================================================
    # Vignette 1: V01
    # =========================================================================
    v01_text = (
        "Marc Durand and Elena Rostova are senior equity research analysts at Apex Asset Management in Geneva. "
        "Durand covers European Capital Goods and Industrial Machinery, while Rostova specializes in Consumer Cyclicals. "
        "During an investment committee review, Durand presents an initiation report on Nexo Dynamics, an industrial "
        "automation firm whose shares are currently trading on Euronext at 84.00 EUR. Durand calculates an estimated "
        "intrinsic value ($V_0$) of 96.00 EUR per share, concluding that the stock is undervalued by 12.00 EUR.\n\n"
        "Rostova scrutinizes Nexo's recent disclosures and highlights two aggressive accounting choices made in the latest fiscal year. "
        "First, Nexo capitalized 45 million EUR of internal software development expenditures that had historically been expensed as R&D. "
        "Second, Nexo reclassified 18 million EUR of routine equipment maintenance costs from cost of goods sold into non-operating other expenses.\n\n"
        "Meanwhile, the committee is debating asset allocation strategies. Rostova advocates a top-down macroeconomic framework "
        "starting with global GDP forecasts, interest rates, and yield curve shifts, whereas Durand insists on a pure bottom-up "
        "security selection approach based on microeconomic firm fundamentals. Lastly, Durand evaluates a takeover bid from an activist "
        "private equity fund seeking a 51% controlling interest in Nexo Dynamics."
    )
    v01_title = "Apex Asset Management: Valuation Frameworks, Quality of Disclosures, & Forecasting Approaches"
    v01_los_base = "Analyze the role of equity valuation, evaluate the quality of financial disclosures, and contrast top-down versus bottom-up forecasting."

    v01_questions = [
        {
            "id": "L2-EQ-V01-Q1",
            "level": 2,
            "topic": "Equity Valuation",
            "subtopic": "Valuation Applications & Mispricing Decomposition",
            "vignette_id": "V01",
            "vignette_title": v01_title,
            "vignette_text": v01_text,
            "los": "Describe the components of perceived mispricing and evaluate sources of perceived alpha.",
            "question": "Durand estimates perceived mispricing for Nexo Dynamics as $V - P = 12.00\\text{ EUR}$. If $V^*$ represents the true unobservable intrinsic value, $V$ represents the analyst's estimate, and $P$ represents the market price, Durand's perceived mispricing is most accurately decomposed into:",
            "options": {
                "A": "True mispricing $(V^* - P)$ plus analyst valuation error $(V - V^*)$.",
                "B": "Analyst valuation error $(V^* - V)$ plus market convergence error $(P - V^*)$.",
                "C": "Market efficiency error $(V - P)$ minus execution slippage $(V^* - P)$."
            },
            "answer": "A",
            "explanation": "Perceived mispricing is algebraically defined as $V - P = (V - V^*) + (V^* - P)$, where $(V^* - P)$ is the true mispricing (the actual difference between true intrinsic value and the current market price) and $(V - V^*)$ is the analyst's valuation error (the discrepancy between the analyst's estimate and the true intrinsic value). An active investor only earns abnormal returns (alpha) to the extent that true mispricing exists and market price converges toward $V^*$.",
            "distractor_analysis": {
                "B": "Incorrectly reverses the terms and labels convergence as an error component rather than the fundamental difference $(V^* - P)$.",
                "C": "Incorrectly introduces execution slippage into the theoretical decomposition of perceived mispricing."
            }
        },
        {
            "id": "L2-EQ-V01-Q2",
            "level": 2,
            "topic": "Equity Valuation",
            "subtopic": "Top-Down vs. Bottom-Up Forecasting",
            "vignette_id": "V01",
            "vignette_title": v01_title,
            "vignette_text": v01_text,
            "los": "Contrast top-down and bottom-up approaches to forecasting and security selection.",
            "question": "In comparing Rostova's top-down valuation methodology with Durand's bottom-up approach, which of the following statements is most accurate?",
            "options": {
                "A": "Top-down forecasting begins with individual company microeconomic fundamentals before aggregating to industry trends.",
                "B": "Bottom-up forecasting starts with macroeconomic growth projections and interest rates before screening company metrics.",
                "C": "Top-down forecasting establishes macroeconomic scenarios and industry sector allocations prior to individual stock selection, whereas bottom-up forecasting focuses primarily on company-specific fundamentals."
            },
            "answer": "C",
            "explanation": "Top-down forecasting begins with broad macroeconomic expectations (GDP growth, monetary policy, inflation, exchange rates), evaluates industry sector attractiveness within that macroeconomic context, and then selects individual securities. In contrast, bottom-up forecasting analyzes individual company microeconomic drivers (product positioning, unit margins, managerial quality, competitive advantages) independently of broader macroeconomic sector allocations.",
            "distractor_analysis": {
                "A": "Describes a bottom-up approach, not a top-down approach.",
                "B": "Describes a top-down approach, not a bottom-up approach."
            }
        },
        {
            "id": "L2-EQ-V01-Q3",
            "level": 2,
            "topic": "Equity Valuation",
            "subtopic": "Quality of Financial Disclosures & Accounting Choices",
            "vignette_id": "V01",
            "vignette_title": v01_title,
            "vignette_text": v01_text,
            "los": "Evaluate how accounting choices regarding capitalization versus expensing distort cash flows and earnings quality.",
            "question": "Regarding Nexo's decision to capitalize 45 million EUR of development expenditures rather than expensing them, which of the following best describes the immediate financial statement impact in the current period?",
            "options": {
                "A": "Lower reported Net Income and higher Cash Flow from Operations (CFO).",
                "B": "Higher reported Net Income, higher Cash Flow from Operations (CFO), and higher cash outflows in Cash Flow from Investing (CFI).",
                "C": "Higher reported Net Income, lower Cash Flow from Operations (CFO), and higher Cash Flow from Financing (CFF)."
            },
            "answer": "B",
            "explanation": "Capitalizing development expenditures avoids an operating charge on the income statement, immediately increasing current-period pre-tax income and Net Income. The associated cash outflow is classified as capital expenditure under Cash Flow from Investing (CFI), which removes it from operating expenses and artificially elevates reported Cash Flow from Operations (CFO).",
            "distractor_analysis": {
                "A": "Net Income increases, rather than decreases, because the expense is deferred to future periods via amortization.",
                "C": "CFO increases because the cash outflow is shifted to CFI, and CFF is completely unaffected by this accounting choice."
            }
        },
        {
            "id": "L2-EQ-V01-Q4",
            "level": 2,
            "topic": "Equity Valuation",
            "subtopic": "Quality of Disclosures & Operating Classification",
            "vignette_id": "V01",
            "vignette_title": v01_title,
            "vignette_text": v01_text,
            "los": "Analyze the effect of non-operating reclassifications on core operating profitability metrics.",
            "question": "Nexo's reclassification of 18 million EUR of routine equipment maintenance costs from COGS to non-operating other expenses most likely results in:",
            "options": {
                "A": "An artificial increase in operating profit (EBIT) while leaving pre-tax income unchanged.",
                "B": "An increase in pre-tax income and an increase in Cash Flow from Operations (CFO).",
                "C": "A decrease in gross profit margin but an increase in operating profit (EBIT)."
            },
            "answer": "A",
            "explanation": "Routine maintenance is an ordinary, necessary operating expense. Reclassifying 18 million EUR out of operating expenses (COGS) into non-operating items reduces operating expenses, which artificially boosts operating income (EBIT) and operating margin. However, because the item is still deducted as a non-operating expense before calculating pre-tax income, pre-tax income, taxes, Net Income, and CFO remain entirely unchanged.",
            "distractor_analysis": {
                "B": "Pre-tax income and CFO are unaffected because total expenses and total cash outflows remain identical.",
                "C": "Gross profit margin increases (or remains higher) when expenses are removed from COGS; it does not decrease."
            }
        },
        {
            "id": "L2-EQ-V01-Q5",
            "level": 2,
            "topic": "Equity Valuation",
            "subtopic": "Ownership Perspective & Control Premium",
            "vignette_id": "V01",
            "vignette_title": v01_title,
            "vignette_text": v01_text,
            "los": "Explain the differences in valuation perspective between minority shareholders and controlling acquirers.",
            "question": "When valuing Nexo Dynamics from the perspective of the private equity fund seeking a 51% controlling interest compared to a passive public minority shareholder, the acquirer's valuation should most appropriately:",
            "options": {
                "A": "Apply a discount for lack of control (DLOC) to reflect the execution risk of restructuring.",
                "B": "Incorporate discretionary cash flow enhancements, operational restructuring synergies, and capital structure optimization available through control.",
                "C": "Rely strictly on historical dividend distributions rather than free cash flow to the firm."
            },
            "answer": "B",
            "explanation": "A controlling shareholder possesses the legal power to replace ineffective management, optimize capital structure, renegotiate related-party agreements, eliminate non-operating waste, and redirect free cash flows. Consequently, a controlling valuation reflects control-adjusted cash flows and potential synergies, whereas a minority valuation must reflect the status quo cash flows accessible to non-controlling investors.",
            "distractor_analysis": {
                "A": "A discount for lack of control is applied when valuing minority shares, not when valuing a controlling interest.",
                "C": "Controlling investors evaluate free cash flow to the firm (FCFF) or free cash flow to equity (FCFE), as they have the power to extract all cash flows regardless of dividend policy."
            }
        }
    ]
    vignettes.append((v01_title, v01_text, v01_questions))

    # =========================================================================
    # Vignette 2: V02
    # =========================================================================
    v02_text = (
        "Caledonia Utilities (CU) is a regulated electric and water utility operating in the United Kingdom. "
        "Senior equity analyst Ian MacIntyre is assessing CU's common stock for an income-focused institutional mandate. "
        "CU recently distributed an annual dividend of $D_0 = 3.20\\text{ GBP}$ per share. Ian estimates Caledonia's "
        "required rate of return on equity at $r = 8.50\\%$.\n\n"
        "Under the current multi-year regulatory tariff, Ian initially models CU using the constant growth Gordon Growth Model, "
        "assuming dividends will grow indefinitely at a mature long-term rate of $g = 3.50\\%$.\n\n"
        "However, management has announced a capital investment initiative for offshore grid integration that will temporarily "
        "accelerate regulatory asset base growth. Ian revises his forecast using the H-Model: the dividend growth rate is projected "
        "to start at $g_S = 7.50\\%$ in year 1 and then decline linearly over a 10-year transition period ($2H = 10\\text{ years}$, "
        "so the half-life $H = 5\\text{ years}$) to a terminal perpetual growth rate of $g_L = 3.50\\%$.\n\n"
        "Caledonia's shares are currently trading on the London Stock Exchange at $P_0 = 78.00\\text{ GBP}$. "
        "Ian expects consensus forecasted earnings per share for next year ($E_1$) to be $5.00\\text{ GBP}$."
    )
    v02_title = "Caledonia Utilities: Gordon Growth, H-Model, & Implied Return Dynamics"

    v02_questions = [
        {
            "id": "L2-EQ-V02-Q1",
            "level": 2,
            "topic": "Equity Valuation",
            "subtopic": "Gordon Growth Model",
            "vignette_id": "V02",
            "vignette_title": v02_title,
            "vignette_text": v02_text,
            "los": "Calculate the intrinsic value of a common stock using the Gordon Growth Model.",
            "question": "Under the baseline constant growth Gordon Growth Model assumption, the intrinsic value of Caledonia Utilities per share is closest to:",
            "options": {
                "A": "64.00 GBP.",
                "B": "66.24 GBP.",
                "C": "68.64 GBP."
            },
            "answer": "B",
            "explanation": "First, calculate expected dividend for Year 1: $D_1 = D_0 \\times (1 + g) = 3.20 \\times (1 + 0.035) = 3.312\\text{ GBP}$. Applying the Gordon Growth Model formula: $$V_0 = \\frac{D_1}{r - g} = \\frac{3.312}{0.085 - 0.035} = \\frac{3.312}{0.050} = 66.24\\text{ GBP}$$.",
            "distractor_analysis": {
                "A": "Incorrectly uses $D_0$ in the numerator without growing it: $3.20 / 0.050 = 64.00\\text{ GBP}$.",
                "C": "Incorrectly compounds growth twice or uses an erroneous spread of $4.75\\%$."
            }
        },
        {
            "id": "L2-EQ-V02-Q2",
            "level": 2,
            "topic": "Equity Valuation",
            "subtopic": "H-Model Valuation",
            "vignette_id": "V02",
            "vignette_title": v02_title,
            "vignette_text": v02_text,
            "los": "Calculate the intrinsic value of a common stock using the H-Model.",
            "question": "Using the H-Model with a 10-year transition period ($H = 5$), the intrinsic value of Caledonia Utilities per share is closest to:",
            "options": {
                "A": "72.64 GBP.",
                "B": "79.04 GBP.",
                "C": "85.44 GBP."
            },
            "answer": "B",
            "explanation": "The H-Model decomposes intrinsic value into a baseline perpetual growth component and an excess growth transition component: $$V_0 = \\frac{D_0 (1 + g_L)}{r - g_L} + \\frac{D_0 \\times H \\times (g_S - g_L)}{r - g_L}$$ Baseline component: $$\\frac{3.20 \\times 1.035}{0.085 - 0.035} = \\frac{3.312}{0.050} = 66.24\\text{ GBP}$$ Transition component: $$\\frac{3.20 \\times 5 \\times (0.075 - 0.035)}{0.085 - 0.035} = \\frac{16.00 \\times 0.040}{0.050} = \\frac{0.640}{0.050} = 12.80\\text{ GBP}$$ Total intrinsic value: $$V_0 = 66.24 + 12.80 = 79.04\\text{ GBP}$$.",
            "distractor_analysis": {
                "A": "Uses $H = 2.5$ instead of $H = 5$ ($66.24 + 6.40 = 72.64\\text{ GBP}$).",
                "C": "Uses the full transition length $2H = 10$ instead of the half-life $H = 5$ ($66.24 + 25.60 = 91.84\\text{ GBP}$ or erroneous arithmetic)."
            }
        },
        {
            "id": "L2-EQ-V02-Q3",
            "level": 2,
            "topic": "Equity Valuation",
            "subtopic": "Implied Required Return",
            "vignette_id": "V02",
            "vignette_title": v02_title,
            "vignette_text": v02_text,
            "los": "Calculate the implied expected rate of return for a common stock using the Gordon Growth Model.",
            "question": "Given Caledonia's current market price of $78.00\\text{ GBP}$ and assuming a constant growth rate of $3.50\\%$, the implied expected rate of return on CU's equity is closest to:",
            "options": {
                "A": "7.60%.",
                "B": "7.75%.",
                "C": "8.10%."
            },
            "answer": "B",
            "explanation": "Under the Gordon Growth Model, the implied expected return equals the dividend yield plus the capital gains growth rate: $$r = \\frac{D_1}{P_0} + g$$ Given $D_1 = 3.20 \\times 1.035 = 3.312\\text{ GBP}$: $$r = \\frac{3.312}{78.00} + 0.0350 = 0.04246 + 0.0350 = 0.07746 \\approx 7.75\\%$$.",
            "distractor_analysis": {
                "A": "Incorrectly uses $D_0$ instead of $D_1$: $3.20 / 78.00 + 0.0350 = 4.10\\% + 3.50\\% = 7.60\\%$.",
                "C": "Uses an erroneous forward growth rate of $4.60\\%$."
            }
        },
        {
            "id": "L2-EQ-V02-Q4",
            "level": 2,
            "topic": "Equity Valuation",
            "subtopic": "Present Value of Growth Opportunities (PVGO)",
            "vignette_id": "V02",
            "vignette_title": v02_title,
            "vignette_text": v02_text,
            "los": "Calculate and interpret the present value of growth opportunities (PVGO).",
            "question": "Assuming a required return of $8.50\\%$, forecasted EPS of $E_1 = 5.00\\text{ GBP}$, and the current market price of $P_0 = 78.00\\text{ GBP}$, the Present Value of Growth Opportunities (PVGO) and its percentage of share price are closest to:",
            "options": {
                "A": "PVGO of 19.18 GBP, representing 24.59% of share price.",
                "B": "PVGO of 24.18 GBP, representing 31.00% of share price.",
                "C": "PVGO of 14.18 GBP, representing 18.18% of share price."
            },
            "answer": "A",
            "explanation": "Share price can be partitioned into the value of assets in place (no-growth value) and the present value of growth opportunities: $$P_0 = \\frac{E_1}{r} + \\text{PVGO}$$ The no-growth value per share is: $$\\frac{E_1}{r} = \\frac{5.00\\text{ GBP}}{0.085} = 58.824\\text{ GBP}$$ Solving for PVGO: $$\\text{PVGO} = P_0 - \\frac{E_1}{r} = 78.00 - 58.824 = 19.176\\text{ GBP} \\approx 19.18\\text{ GBP}$$ Percentage of price: $$\\frac{19.176}{78.00} = 24.585\\% \\approx 24.59\\%$$.",
            "distractor_analysis": {
                "B": "Uses $D_1$ instead of $E_1$ in the no-growth formula ($3.312 / 0.085 = 38.96\\text{ GBP}$, resulting in PVGO $= 39.04\\text{ GBP}$).",
                "C": "Uses $r = 9.5\\%$ to compute no-growth value ($5.00 / 0.095 = 52.63\\text{ GBP}$, PVGO $= 25.37\\text{ GBP}$) or computational error."
            }
        },
        {
            "id": "L2-EQ-V02-Q5",
            "level": 2,
            "topic": "Equity Valuation",
            "subtopic": "Dividend Discount Model Applicability",
            "vignette_id": "V02",
            "vignette_title": v02_title,
            "vignette_text": v02_text,
            "los": "Explain the conditions under which the Gordon Growth Model is suitable and identify its primary limitations.",
            "question": "Which of the following conditions is most essential for the Gordon Growth Model to provide a valid and economically meaningful intrinsic value estimate?",
            "options": {
                "A": "The firm must finance capital expenditures exclusively with newly issued debt.",
                "B": "The required return on equity ($r$) must strictly exceed the perpetual dividend growth rate ($g$).",
                "C": "The firm's return on equity (ROE) must be identical to its cost of equity ($r$)."
            },
            "answer": "B",
            "explanation": "A fundamental mathematical and economic requirement of the Gordon Growth Model is that $r > g$. If $g \\ge r$, the denominator $(r - g)$ becomes zero or negative, yielding a nonsensical infinite or negative valuation. Furthermore, in perpetuity, a company cannot grow faster than the macroeconomic economy without eventually becoming the entire economy.",
            "distractor_analysis": {
                "A": "Capital expenditure financing structure does not invalidate the Gordon model as long as dividends reflect sustainable growth.",
                "C": "If $\\text{ROE} = r$, the firm has zero growth opportunities (PVGO $= 0$), but this is not a prerequisite for applying the model."
            }
        }
    ]
    vignettes.append((v02_title, v02_text, v02_questions))

    # =========================================================================
    # Vignette 3: V03
    # =========================================================================
    v03_text = (
        "Astrid Lindholm is evaluating Nordic Health AB, a specialty pharmaceutical company listed in Stockholm. "
        "Astrid is constructing a multistage Dividend Discount Model (DDM) to capture Nordic Health's patent protection "
        "cycle and eventual patent expiration transition.\n\n"
        "To establish the required return on equity ($r$), Astrid calculates the unadjusted historical beta using 60 monthly returns "
        "against the local index, obtaining $\\beta_{\\text{raw}} = 1.45$. Because historical beta estimates regress toward the market "
        "mean over time, she applies the Blume adjustment: $$\\beta_{\\text{adj}} = \\frac{2}{3}\\beta_{\\text{raw}} + \\frac{1}{3}(1.0)$$ "
        "The current risk-free rate is $3.00\\%$, and the equity risk premium is $5.00\\%$.\n\n"
        "Nordic Health's financial disclosures indicate a net profit margin of $8.0\\%$, total asset turnover of $1.00$, "
        "a financial leverage ratio (Assets/Equity) of $1.50$, and a dividend payout ratio of $60.0\\%$ (earnings retention ratio $b = 0.40$). "
        "Astrid models the terminal growth rate using the sustainable growth formula ($g = b \\times \\text{ROE}$).\n\n"
        "Nordic Health just paid an annual dividend of $D_0 = 2.50\\text{ EUR}$. In the high-growth stage (years 1 and 2), "
        "dividends are projected to grow at $12.00\\%$ per annum. Beginning in Year 3, the company will enter its mature stage, "
        "growing at the sustainable growth rate ($g$) in perpetuity."
    )
    v03_title = "Nordic Health: Multistage DDM, Blume Beta, & Sustainable Growth Dynamics"

    v03_questions = [
        {
            "id": "L2-EQ-V03-Q1",
            "level": 2,
            "topic": "Equity Valuation",
            "subtopic": "Blume Beta Adjustment & CAPM",
            "vignette_id": "V03",
            "vignette_title": v03_title,
            "vignette_text": v03_text,
            "los": "Calculate and interpret Blume's adjusted beta and estimate the cost of equity using the CAPM.",
            "question": "Using the Blume adjustment formula and the Capital Asset Pricing Model (CAPM), Nordic Health's adjusted beta and required return on equity ($r$) are closest to:",
            "options": {
                "A": "Adjusted beta of 1.30 and required return of 9.50%.",
                "B": "Adjusted beta of 1.30 and required return of 10.25%.",
                "C": "Adjusted beta of 1.25 and required return of 9.25%."
            },
            "answer": "A",
            "explanation": "Blume's adjusted beta is computed as: $$\\beta_{\\text{adj}} = \\frac{2}{3}(1.45) + \\frac{1}{3}(1.0) = 0.9667 + 0.3333 = 1.300$$ Applying the CAPM: $$r = R_f + \\beta_{\\text{adj}} \\times \\text{ERP} = 3.00\\% + (1.30 \\times 5.00\\%) = 3.00\\% + 6.50\\% = 9.50\\%$$.",
            "distractor_analysis": {
                "B": "Uses the unadjusted beta of 1.45 in the CAPM formula: $3.00\\% + (1.45 \\times 5.00\\%) = 10.25\\%$.",
                "C": "Incorrectly weights beta as $0.50(1.45) + 0.50(1.0) = 1.225$ or calculation error."
            }
        },
        {
            "id": "L2-EQ-V03-Q2",
            "level": 2,
            "topic": "Equity Valuation",
            "subtopic": "DuPont Sustainable Growth Rate",
            "vignette_id": "V03",
            "vignette_title": v03_title,
            "vignette_text": v03_text,
            "los": "Calculate the sustainable growth rate using DuPont components (PRAT model).",
            "question": "Nordic Health's sustainable growth rate ($g = b \\times \\text{ROE}$) based on DuPont analysis is closest to:",
            "options": {
                "A": "4.80%.",
                "B": "7.20%.",
                "C": "12.00%."
            },
            "answer": "A",
            "explanation": "Using DuPont decomposition, $\\text{ROE} = \\text{Net Profit Margin} \\times \\text{Asset Turnover} \\times \\text{Financial Leverage}$: $$\\text{ROE} = 0.08 \\times 1.00 \\times 1.50 = 0.1200 = 12.00\\%$$ Given a dividend payout ratio of $60.0\\%$, the retention ratio is $b = 1 - 0.60 = 0.40$. The sustainable growth rate is: $$g = b \\times \\text{ROE} = 0.40 \\times 12.00\\% = 4.80\\%$$.",
            "distractor_analysis": {
                "B": "Uses the payout ratio instead of the retention ratio: $0.60 \\times 12.00\\% = 7.20\\%$.",
                "C": "Reports ROE ($12.00\\%$) without multiplying by the retention ratio."
            }
        },
        {
            "id": "L2-EQ-V03-Q3",
            "level": 2,
            "topic": "Equity Valuation",
            "subtopic": "Multistage DDM Valuation",
            "vignette_id": "V03",
            "vignette_title": v03_title,
            "vignette_text": v03_text,
            "los": "Calculate the intrinsic value of a stock using a multistage dividend discount model.",
            "question": "Based on a two-year high-growth period of $12.00\\%$, followed by perpetual growth at the sustainable growth rate of $4.80\\%$, and a required return of $9.50\\%$, the intrinsic value of Nordic Health per share is closest to:",
            "options": {
                "A": "58.45 EUR.",
                "B": "63.50 EUR.",
                "C": "69.93 EUR."
            },
            "answer": "B",
            "explanation": "Step 1: Forecast explicit dividends for Year 1 and Year 2: $$D_1 = D_0 \\times 1.12 = 2.50 \\times 1.12 = 2.800\\text{ EUR}$$ $$D_2 = D_1 \\times 1.12 = 2.80 \\times 1.12 = 3.136\\text{ EUR}$$ Step 2: Forecast Year 3 dividend entering perpetual growth: $$D_3 = D_2 \\times (1 + g) = 3.136 \\times (1 + 0.048) = 3.28653\\text{ EUR}$$ Step 3: Calculate terminal price at $t = 2$: $$P_2 = \\frac{D_3}{r - g} = \\frac{3.28653}{0.095 - 0.048} = \\frac{3.28653}{0.047} = 69.926\\text{ EUR}$$ Step 4: Discount cash flows to $t = 0$: $$\\text{PV}(D_1) = \\frac{2.800}{1.095} = 2.5571\\text{ EUR}$$ $$\\text{PV}(D_2 + P_2) = \\frac{3.136 + 69.926}{(1.095)^2} = \\frac{73.062}{1.199025} = 60.9345\\text{ EUR}$$ $$V_0 = 2.5571 + 60.9345 = 63.4916\\text{ EUR} \\approx 63.50\\text{ EUR}$$.",
            "distractor_analysis": {
                "A": "Forgets to include $D_2$ in the terminal year discounting numerator ($69.926 / 1.199025 + 2.557 = 60.88\\text{ EUR}$) or misapplies discount factors.",
                "C": "Reports the un-discounted terminal value $P_2 = 69.93\\text{ EUR}$ without discounting back to present value."
            }
        },
        {
            "id": "L2-EQ-V03-Q4",
            "level": 2,
            "topic": "Equity Valuation",
            "subtopic": "PRAT Model Dynamics",
            "vignette_id": "V03",
            "vignette_title": v03_title,
            "vignette_text": v03_text,
            "los": "Analyze the impact of financial policy and operational changes on the sustainable growth rate.",
            "question": "If Nordic Health's board increases the dividend payout ratio from $60.0\\%$ to $75.0\\%$ while profit margin, asset turnover, and leverage remain unchanged, the sustainable growth rate will:",
            "options": {
                "A": "Decrease from 4.80% to 3.00%.",
                "B": "Increase from 4.80% to 9.00%.",
                "C": "Remain unchanged at 4.80% because operating profitability is unaltered."
            },
            "answer": "A",
            "explanation": "The retention ratio decreases from $b = 1 - 0.60 = 0.40$ to $b' = 1 - 0.75 = 0.25$. With ROE remaining constant at $12.00\\%$, the new sustainable growth rate is: $$g' = b' \\times \\text{ROE} = 0.25 \\times 12.00\\% = 3.00\\%$$ Sustainable growth decreases because retaining fewer earnings restricts internally financed asset expansion.",
            "distractor_analysis": {
                "B": "Incorrectly calculates $0.75 \\times 12.00\\% = 9.00\\%$, confusing payout ratio with retention ratio.",
                "C": "Fails to recognize that dividend policy directly dictates internal capital accumulation and growth."
            }
        },
        {
            "id": "L2-EQ-V03-Q5",
            "level": 2,
            "topic": "Equity Valuation",
            "subtopic": "Multistage DDM vs. FCF Selection",
            "vignette_id": "V03",
            "vignette_title": v03_title,
            "vignette_text": v03_text,
            "los": "Evaluate the strengths and limitations of DDM compared to Free Cash Flow models.",
            "question": "In which of the following scenarios is a Dividend Discount Model (DDM) least appropriate compared to a Free Cash Flow (FCF) model?",
            "options": {
                "A": "A mature commercial bank with stable dividend payouts reflecting regulatory capital constraints.",
                "B": "A regulated water utility with long-term dividend growth anchored to regulated rate-of-return tariffs.",
                "C": "A rapidly growing company with volatile earnings, reinvestment exceeding operating cash flows, and dividends paid significantly below free cash flow capacity."
            },
            "answer": "C",
            "explanation": "DDMs are least appropriate for companies that pay zero or negligible dividends, or where dividend distributions bear little relationship to firm profitability and cash generation capacity (e.g., high-growth firms reinvesting all cash flows). In such cases, free cash flow models (FCFF/FCFE) accurately reflect intrinsic economic value creation independently of arbitrary managerial distribution policies.",
            "distractor_analysis": {
                "A": "Commercial banks are classic candidates for DDM because financial firms cannot easily calculate standard operating FCF due to debt being an operational input.",
                "B": "Regulated utilities with stable dividend payout policies are ideal candidates for DDM."
            }
        }
    ]
    vignettes.append((v03_title, v03_text, v03_questions))

    # =========================================================================
    # Vignette 4: V04
    # =========================================================================
    v04_text = (
        "Meridian Aerospace Corp (MAC) manufactures commercial avionics and flight-control systems. "
        "Senior valuation analyst David Zhang is constructing an equity valuation for MAC for the fiscal year just ended. "
        "David extracts the following financial statement data from MAC's annual report (all monetary figures in millions of USD):\n\n"
        "- Net Income (NI): 480.0 USD\n"
        "- Non-cash charges (Depreciation and Amortization): 160.0 USD\n"
        "- Interest expense: 70.0 USD\n"
        "- Marginal corporate tax rate: 25.0%\n"
        "- Capital expenditures on fixed capital (FCInv): 230.0 USD\n"
        "- Net increase in working capital (WCInv): 40.0 USD\n"
        "- Net borrowing (debt issues minus debt repayments): 50.0 USD\n"
        "- Cash dividends paid to common shareholders: 120.0 USD\n"
        "- Common share repurchases: 60.0 USD\n\n"
        "Under US GAAP, MAC classifies interest expense in operating activities. "
        "Reported Cash Flow from Operations (CFO) is: "
        "$$\\text{CFO} = \\text{NI} + \\text{NCC} - \\text{WCInv} = 480.0 + 160.0 - 40.0 = 600.0\\text{ USD million}$$ "
        "David reviews the relationship between Free Cash Flow to the Firm (FCFF), Free Cash Flow to Equity (FCFE), and corporate dividend capacity."
    )
    v04_title = "Meridian Aerospace: FCFF and FCFE Reconciliation from Net Income and CFO"

    v04_questions = [
        {
            "id": "L2-EQ-V04-Q1",
            "level": 2,
            "topic": "Equity Valuation",
            "subtopic": "FCFF from Net Income",
            "vignette_id": "V04",
            "vignette_title": v04_title,
            "vignette_text": v04_text,
            "los": "Calculate Free Cash Flow to the Firm (FCFF) starting from Net Income.",
            "question": "Starting from Net Income, Meridian Aerospace's Free Cash Flow to the Firm (FCFF) for the year just ended is closest to:",
            "options": {
                "A": "370.0 USD million.",
                "B": "422.5 USD million.",
                "C": "475.0 USD million."
            },
            "answer": "B",
            "explanation": "The formula for FCFF starting from Net Income is: $$\\text{FCFF} = \\text{NI} + \\text{NCC} + [\\text{Interest} \\times (1 - t)] - \\text{FCInv} - \\text{WCInv}$$ After-tax interest expense is: $$70.0 \\times (1 - 0.25) = 70.0 \\times 0.75 = 52.5\\text{ USD million}$$ Substituting the figures: $$\\text{FCFF} = 480.0 + 160.0 + 52.5 - 230.0 - 40.0 = 692.5 - 270.0 = 422.5\\text{ USD million}$$.",
            "distractor_analysis": {
                "A": "Omits the after-tax interest expense add-back: $480.0 + 160.0 - 230.0 - 40.0 = 370.0\\text{ USD million}$.",
                "C": "Adds back pre-tax interest expense ($70.0\\text{ USD}$) without tax-shield adjustment: $480 + 160 + 70 - 230 - 40 = 440.0\\text{ USD}$ or arithmetic error."
            }
        },
        {
            "id": "L2-EQ-V04-Q2",
            "level": 2,
            "topic": "Equity Valuation",
            "subtopic": "FCFF from CFO",
            "vignette_id": "V04",
            "vignette_title": v04_title,
            "vignette_text": v04_text,
            "los": "Calculate Free Cash Flow to the Firm (FCFF) starting from Cash Flow from Operations (CFO).",
            "question": "Starting from reported Cash Flow from Operations (CFO), Meridian Aerospace's Free Cash Flow to the Firm (FCFF) is closest to:",
            "options": {
                "A": "422.5 USD million.",
                "B": "440.0 USD million.",
                "C": "475.0 USD million."
            },
            "answer": "A",
            "explanation": "Starting from CFO under US GAAP (where interest expense is deducted in CFO): $$\\text{FCFF} = \\text{CFO} + [\\text{Interest} \\times (1 - t)] - \\text{FCInv}$$ Substituting reported values: $$\\text{FCFF} = 600.0 + [70.0 \\times (1 - 0.25)] - 230.0 = 600.0 + 52.5 - 230.0 = 422.5\\text{ USD million}$$ This reconciles with the Net Income derivation.",
            "distractor_analysis": {
                "B": "Adds back full pre-tax interest expense: $600.0 + 70.0 - 230.0 = 440.0\\text{ USD million}$.",
                "C": "Forgets to subtract capital expenditures (FCInv): $600.0 + 52.5 - 177.5 = 475.0\\text{ USD million}$."
            }
        },
        {
            "id": "L2-EQ-V04-Q3",
            "level": 2,
            "topic": "Equity Valuation",
            "subtopic": "FCFE from Net Income",
            "vignette_id": "V04",
            "vignette_title": v04_title,
            "vignette_text": v04_text,
            "los": "Calculate Free Cash Flow to Equity (FCFE) starting from Net Income.",
            "question": "Starting from Net Income, Meridian Aerospace's Free Cash Flow to Equity (FCFE) is closest to:",
            "options": {
                "A": "370.0 USD million.",
                "B": "420.0 USD million.",
                "C": "472.5 USD million."
            },
            "answer": "B",
            "explanation": "The formula for FCFE starting from Net Income is: $$\\text{FCFE} = \\text{NI} + \\text{NCC} - \\text{FCInv} - \\text{WCInv} + \\text{Net Borrowing}$$ Substituting the given figures: $$\\text{FCFE} = 480.0 + 160.0 - 230.0 - 40.0 + 50.0 = 640.0 - 270.0 + 50.0 = 420.0\\text{ USD million}$$.",
            "distractor_analysis": {
                "A": "Omits net borrowing: $480.0 + 160.0 - 230.0 - 40.0 = 370.0\\text{ USD million}$.",
                "C": "Incorrectly adds after-tax interest expense to FCFE: $420.0 + 52.5 = 472.5\\text{ USD million}$."
            }
        },
        {
            "id": "L2-EQ-V04-Q4",
            "level": 2,
            "topic": "Equity Valuation",
            "subtopic": "FCFE from FCFF",
            "vignette_id": "V04",
            "vignette_title": v04_title,
            "vignette_text": v04_text,
            "los": "Calculate Free Cash Flow to Equity (FCFE) starting from FCFF.",
            "question": "Starting from FCFF of $422.5\\text{ USD million}$, Meridian Aerospace's Free Cash Flow to Equity (FCFE) is closest to:",
            "options": {
                "A": "402.5 USD million.",
                "B": "420.0 USD million.",
                "C": "442.5 USD million."
            },
            "answer": "B",
            "explanation": "The formula linking FCFE to FCFF is: $$\\text{FCFE} = \\text{FCFF} - [\\text{Interest} \\times (1 - t)] + \\text{Net Borrowing}$$ Substituting the figures: $$\\text{FCFE} = 422.5 - 52.5 + 50.0 = 420.0\\text{ USD million}$$.",
            "distractor_analysis": {
                "A": "Deducts full pre-tax interest: $422.5 - 70.0 + 50.0 = 402.5\\text{ USD million}$.",
                "C": "Adds after-tax interest instead of subtracting it: $422.5 + 52.5 - 32.5 = 442.5\\text{ USD million}$."
            }
        },
        {
            "id": "L2-EQ-V04-Q5",
            "level": 2,
            "topic": "Equity Valuation",
            "subtopic": "Dividend Capacity & FCFE Interpretation",
            "vignette_id": "V04",
            "vignette_title": v04_title,
            "vignette_text": v04_text,
            "los": "Explain the concept of dividend capacity and evaluate how FCFE compares to dividends paid.",
            "question": "MAC distributed $120.0\\text{ USD million}$ in dividends and spent $60.0\\text{ USD million}$ on share repurchases during the year. In evaluating MAC's dividend capacity, Zhang should conclude that:",
            "options": {
                "A": "MAC paid out more than its dividend capacity, necessitating immediate external equity financing.",
                "B": "MAC generated $420.0\\text{ USD million}$ of dividend capacity (FCFE), indicating that total shareholder distributions of $180.0\\text{ USD million}$ were fully covered, with the remaining $240.0\\text{ USD million}$ increasing corporate cash balances.",
                "C": "Dividend capacity equals reported Net Income ($480.0\\text{ USD million}$), meaning MAC distributed exactly 37.5% of its capacity."
            },
            "answer": "B",
            "explanation": "FCFE represents the firm's true dividend capacity: the cash flow generated by operations after meeting all capital reinvestment needs (FCInv and WCInv) and satisfying debt obligations (principal and interest). MAC generated $420.0\\text{ USD million}$ of FCFE and distributed only $180.0\\text{ USD million}$ ($120.0\\text{ dividends} + 60.0\\text{ buybacks}$), leaving $240.0\\text{ USD million}$ of surplus liquidity on the balance sheet.",
            "distractor_analysis": {
                "A": "Total distributions ($180.0\\text{ USD million}$) are well below FCFE ($420.0\\text{ USD million}$), meaning distributions were fully covered without external financing.",
                "C": "Net Income is an accrual metric, not a cash metric; capital expenditures and working capital investments absorb cash before distributions can be paid."
            }
        }
    ]
    vignettes.append((v04_title, v04_text, v04_questions))

    # =========================================================================
    # Vignette 5: V05
    # =========================================================================
    v05_text = (
        "Helios Industrial (HI) is an infrastructure equipment manufacturer. "
        "Financial analyst Clara Becker is valuing HI using operating earnings metrics. "
        "HI reported the following financial information for the most recent year (monetary values in millions of USD):\n\n"
        "- Operating Income (EBIT): 500.0 USD\n"
        "- EBITDA: 720.0 USD\n"
        "- Depreciation and Amortization expense: 220.0 USD\n"
        "- Marginal corporate income tax rate: 30.0%\n"
        "- Capital expenditures on fixed assets (FCInv): 260.0 USD\n"
        "- Working capital investment (WCInv): 35.0 USD\n"
        "- Interest expense: 60.0 USD\n\n"
        "HI maintains a stable target debt-to-capital ratio (debt ratio, $\\text{DR} = \\text{Debt}/[\\text{Debt} + \\text{Equity}]$) of $35.0\\%$. "
        "Management plans to fund future capital expenditures and working capital additions consistently with this target leverage ratio.\n\n"
        "In addition to core manufacturing operations, HI holds non-operating assets consisting of excess marketable securities "
        "valued at $140.0\\text{ USD million}$ and a 25% non-controlling equity investment in an unlisted logistics affiliate valued at $85.0\\text{ USD million}$. "
        "HI's total market value of interest-bearing debt is $750.0\\text{ USD million}$, and preferred stock is valued at $50.0\\text{ USD million}$. "
        "There are 100.0 million common shares outstanding. Clara estimates the present value of core operating FCFF at $3,200.0\\text{ USD million}$."
    )
    v05_title = "Helios Industrial: FCFF from EBIT/EBITDA, Target Debt Ratio, & Non-Operating Assets"

    v05_questions = [
        {
            "id": "L2-EQ-V05-Q1",
            "level": 2,
            "topic": "Equity Valuation",
            "subtopic": "FCFF from EBIT",
            "vignette_id": "V05",
            "vignette_title": v05_title,
            "vignette_text": v05_text,
            "los": "Calculate Free Cash Flow to the Firm (FCFF) starting from EBIT.",
            "question": "Starting from Operating Income (EBIT), Helios Industrial's Free Cash Flow to the Firm (FCFF) is closest to:",
            "options": {
                "A": "275.0 USD million.",
                "B": "350.0 USD million.",
                "C": "495.0 USD million."
            },
            "answer": "A",
            "explanation": "The formula for FCFF starting from EBIT is: $$\\text{FCFF} = \\text{EBIT} \\times (1 - t) + \\text{Dep} - \\text{FCInv} - \\text{WCInv}$$ Calculate after-tax EBIT: $$\\text{EBIT}(1 - t) = 500.0 \\times (1 - 0.30) = 350.0\\text{ USD million}$$ Adding depreciation and subtracting investments: $$\\text{FCFF} = 350.0 + 220.0 - 260.0 - 35.0 = 570.0 - 295.0 = 275.0\\text{ USD million}$$.",
            "distractor_analysis": {
                "B": "Forgets to add depreciation and subtract working capital investment ($350.0\\text{ USD million}$).",
                "C": "Omits the tax adjustment on EBIT: $500.0 + 220.0 - 260.0 - 35.0 = 425.0\\text{ USD million}$ or calculation error."
            }
        },
        {
            "id": "L2-EQ-V05-Q2",
            "level": 2,
            "topic": "Equity Valuation",
            "subtopic": "FCFF from EBITDA",
            "vignette_id": "V05",
            "vignette_title": v05_title,
            "vignette_text": v05_text,
            "los": "Calculate Free Cash Flow to the Firm (FCFF) starting from EBITDA.",
            "question": "Starting from EBITDA, Helios Industrial's Free Cash Flow to the Firm (FCFF) is closest to:",
            "options": {
                "A": "209.0 USD million.",
                "B": "275.0 USD million.",
                "C": "341.0 USD million."
            },
            "answer": "B",
            "explanation": "The formula for FCFF starting from EBITDA is: $$\\text{FCFF} = \\text{EBITDA} \\times (1 - t) + (\\text{Dep} \\times t) - \\text{FCInv} - \\text{WCInv}$$ Calculate terms: $$\\text{EBITDA}(1 - t) = 720.0 \\times (1 - 0.30) = 504.0\\text{ USD million}$$ $$\\text{Dep} \\times t = 220.0 \\times 0.30 = 66.0\\text{ USD million}$$ Combining: $$\\text{FCFF} = 504.0 + 66.0 - 260.0 - 35.0 = 570.0 - 295.0 = 275.0\\text{ USD million}$$ This reconciles with the EBIT formula.",
            "distractor_analysis": {
                "A": "Omits the depreciation tax shield $(\\text{Dep} \\times t)$: $504.0 - 260.0 - 35.0 = 209.0\\text{ USD million}$.",
                "C": "Adds full depreciation rather than the depreciation tax shield: $504.0 + 220.0 - 260.0 - 35.0 = 429.0\\text{ USD million}$."
            }
        },
        {
            "id": "L2-EQ-V05-Q3",
            "level": 2,
            "topic": "Equity Valuation",
            "subtopic": "FCFE with Target Debt Financing Ratio",
            "vignette_id": "V05",
            "vignette_title": v05_title,
            "vignette_text": v05_text,
            "los": "Calculate FCFE assuming financing of investments at a target debt ratio.",
            "question": "Assuming HI maintains its target debt ratio of $\\text{DR} = 35.0\\%$ to finance net capital expenditures and working capital, and given interest expense of $60.0\\text{ USD million}$, FCFE is closest to:",
            "options": {
                "A": "233.25 USD million.",
                "B": "259.25 USD million.",
                "C": "285.25 USD million."
            },
            "answer": "B",
            "explanation": "Step 1: Calculate Net Income (NI): $$\\text{EBT} = \\text{EBIT} - \\text{Interest} = 500.0 - 60.0 = 440.0\\text{ USD million}$$ $$\\text{NI} = \\text{EBT} \\times (1 - t) = 440.0 \\times (1 - 0.30) = 308.0\\text{ USD million}$$ Step 2: Under target leverage $\\text{DR}$, net borrowing is $\\text{DR} \\times (\\text{FCInv} - \\text{Dep} + \\text{WCInv})$. Therefore: $$\\text{FCFE} = \\text{NI} - (1 - \\text{DR}) \\times (\\text{FCInv} - \\text{Dep}) - (1 - \\text{DR}) \\times \\text{WCInv}$$ Calculate net investment terms: $$\\text{FCInv} - \\text{Dep} = 260.0 - 220.0 = 40.0\\text{ USD million}$$ Equity-financed net fixed investment: $$(1 - 0.35) \\times 40.0 = 0.65 \\times 40.0 = 26.0\\text{ USD million}$$ Equity-financed working capital investment: $$(1 - 0.35) \\times 35.0 = 0.65 \\times 35.0 = 22.75\\text{ USD million}$$ Total FCFE: $$\\text{FCFE} = 308.0 - 26.0 - 22.75 = 259.25\\text{ USD million}$$.",
            "distractor_analysis": {
                "A": "Deducts 100% of investments without debt financing: $308.0 - 40.0 - 35.0 = 233.0\\text{ USD million}$.",
                "C": "Applies DR of 50% or miscalculates net income."
            }
        },
        {
            "id": "L2-EQ-V05-Q4",
            "level": 2,
            "topic": "Equity Valuation",
            "subtopic": "Non-Operating Assets & Equity Value Bridge",
            "vignette_id": "V05",
            "vignette_title": v05_title,
            "vignette_text": v05_text,
            "los": "Calculate firm and common equity value incorporating non-operating assets.",
            "question": "Given the present value of core operating FCFF of $3,200.0\\text{ USD million}$, the intrinsic value of Helios Industrial's common equity per share is closest to:",
            "options": {
                "A": "24.00 USD.",
                "B": "26.25 USD.",
                "C": "28.50 USD."
            },
            "answer": "B",
            "explanation": "Step 1: Compute total firm value by adding non-operating assets to operating enterprise value: $$\\text{Total Firm Value} = \\text{Operating Value} + \\text{Excess Securities} + \\text{Affiliate Investment}$$ $$\\text{Total Firm Value} = 3,200.0 + 140.0 + 85.0 = 3,425.0\\text{ USD million}$$ Step 2: Compute common equity value by subtracting debt and preferred equity claims: $$\\text{Common Equity Value} = \\text{Total Firm Value} - \\text{Debt} - \\text{Preferred Stock}$$ $$\\text{Common Equity Value} = 3,425.0 - 750.0 - 50.0 = 2,625.0\\text{ USD million}$$ Step 3: Compute per share value: $$\\text{Value per share} = \\frac{2,625.0\\text{ USD million}}{100.0\\text{ million shares}} = 26.25\\text{ USD}$$.",
            "distractor_analysis": {
                "A": "Omits non-operating assets: $(3,200.0 - 750.0 - 50.0) / 100 = 2,400.0 / 100 = 24.00\\text{ USD}$.",
                "C": "Forgets to deduct preferred stock ($50.0\\text{ USD million}$): $2,675.0 / 100 = 26.75\\text{ USD}$ or arithmetic error."
            }
        },
        {
            "id": "L2-EQ-V05-Q5",
            "level": 2,
            "topic": "Equity Valuation",
            "subtopic": "Lease Accounting & Free Cash Flow Adjustments",
            "vignette_id": "V05",
            "vignette_title": v05_title,
            "vignette_text": v05_text,
            "los": "Explain adjustments to operating income and cash flows for operating leases and employee compensation.",
            "question": "Under IFRS 16 / ASC 842, operating leases are capitalized onto the balance sheet as right-of-use assets and lease liabilities. Relative to legacy operating lease accounting where rent was expensed in COGS/SG&A, this standard:",
            "options": {
                "A": "Decreases EBITDA, decreases Cash Flow from Operations (CFO), and increases financing cash outflows.",
                "B": "Increases EBITDA, increases Cash Flow from Operations (CFO), and increases Cash Flow from Financing (CFF) outflows.",
                "C": "Leaves EBITDA unchanged but decreases Net Income in the early years of the lease."
            },
            "answer": "B",
            "explanation": "Under right-of-use lease accounting, lease expense is split into amortization (non-cash operating) and interest expense (financing or separate line). Because rental expense is removed from operating costs, EBITDA increases. On the cash flow statement, principal lease repayment is classified as a financing outflow (CFF), which shifts cash outflows out of operating activities and elevates reported CFO.",
            "distractor_analysis": {
                "A": "EBITDA and CFO increase, rather than decrease, under lease capitalization.",
                "C": "EBITDA increases significantly because lease expense is replaced with depreciation and interest."
            }
        }
    ]
    vignettes.append((v05_title, v05_text, v05_questions))

    # =========================================================================
    # Vignette 6: V06
    # =========================================================================
    v06_text = (
        "Valera Logistics (VL) is a multinational freight forwarding and intermodal transportation company. "
        "Financial analyst Liam O'Connor is conducting a comprehensive two-stage Free Cash Flow to the Firm (FCFF) valuation of VL. "
        "Liam calculates Valera's Weighted Average Cost of Capital (WACC) at $8.00\\%$ and its cost of equity at $10.50\\%$.\n\n"
        "Over the three-year explicit forecast horizon (Stage 1), Liam projects the following annual FCFF amounts (in millions of USD):\n"
        "- Year 1 FCFF: 180.0 USD\n"
        "- Year 2 FCFF: 215.0 USD\n"
        "- Year 3 FCFF: 250.0 USD\n\n"
        "To estimate the terminal value at the end of Year 3 ($t = 3$), Liam compares two standard valuation methods:\n"
        "- Method 1 (Perpetual Growth Model): Beyond Year 3, FCFF will grow indefinitely at a constant sustainable rate of $g = 3.00\\%$.\n"
        "- Method 2 (Exit Multiple Method): Enterprise Value at $t = 3$ is estimated based on an exit EV/EBITDA multiple of $9.00\\times$. "
        "Year 3 EBITDA is forecasted to be $380.0\\text{ USD million}$.\n\n"
        "Valera's balance sheet reports interest-bearing debt with a fair market value of $600.0\\text{ USD million}$ and "
        "cash and marketable securities of $120.0\\text{ USD million}$. Valera has 50.0 million common shares outstanding."
    )
    v06_title = "Valera Logistics: Two-Stage FCF Valuation & Terminal Value via Perpetuity vs. Multiple"

    v06_questions = [
        {
            "id": "L2-EQ-V06-Q1",
            "level": 2,
            "topic": "Equity Valuation",
            "subtopic": "Present Value of Explicit Forecast FCFF",
            "vignette_id": "V06",
            "vignette_title": v06_title,
            "vignette_text": v06_text,
            "los": "Calculate the cumulative present value of operating free cash flows over the explicit forecast horizon.",
            "question": "The cumulative present value of Valera's explicit FCFF for Years 1 through 3, discounted at WACC ($8.00\\%$), is closest to:",
            "options": {
                "A": "549.46 USD million.",
                "B": "586.25 USD million.",
                "C": "645.00 USD million."
            },
            "answer": "A",
            "explanation": "Discount each projected FCFF at WACC ($8.00\\%$): $$\\text{PV}(\\text{FCFF}_1) = \\frac{180.0}{1.08} = 166.667\\text{ USD million}$$ $$\\text{PV}(\\text{FCFF}_2) = \\frac{215.0}{(1.08)^2} = \\frac{215.0}{1.1664} = 184.328\\text{ USD million}$$ $$\\text{PV}(\\text{FCFF}_3) = \\frac{250.0}{(1.08)^3} = \\frac{250.0}{1.259712} = 198.458\\text{ USD million}$$ Cumulative PV of Stage 1: $$166.667 + 184.328 + 198.458 = 549.453\\text{ USD million} \\approx 549.46\\text{ USD million}$$.",
            "distractor_analysis": {
                "B": "Discounts using cost of equity ($10.50\\%$) instead of WACC ($8.00\\%$).",
                "C": "Sums the un-discounted nominal cash flows: $180.0 + 215.0 + 250.0 = 645.0\\text{ USD million}$."
            }
        },
        {
            "id": "L2-EQ-V06-Q2",
            "level": 2,
            "topic": "Equity Valuation",
            "subtopic": "Terminal Value via Perpetual Growth",
            "vignette_id": "V06",
            "vignette_title": v06_title,
            "vignette_text": v06_text,
            "los": "Calculate terminal value using the perpetual growth Gordon method.",
            "question": "Under Method 1 (Perpetual Growth with $g = 3.00\\%$), the undiscounted terminal value at $t = 3$ and its present value at $t = 0$ are closest to:",
            "options": {
                "A": "Terminal value at t=3 of 5,000.00 USD million; PV of terminal value of 3,969.16 USD million.",
                "B": "Terminal value at t=3 of 5,150.00 USD million; PV of terminal value of 4,088.24 USD million.",
                "C": "Terminal value at t=3 of 5,304.50 USD million; PV of terminal value of 4,210.88 USD million."
            },
            "answer": "B",
            "explanation": "Step 1: Calculate FCFF for Year 4 ($t = 4$): $$\\text{FCFF}_4 = \\text{FCFF}_3 \\times (1 + g) = 250.0 \\times (1 + 0.03) = 257.50\\text{ USD million}$$ Step 2: Calculate terminal value at $t = 3$: $$\\text{TV}_3 = \\frac{\\text{FCFF}_4}{\\text{WACC} - g} = \\frac{257.50}{0.08 - 0.03} = \\frac{257.50}{0.05} = 5,150.00\\text{ USD million}$$ Step 3: Discount $\\text{TV}_3$ back to $t = 0$ over 3 years at WACC: $$\\text{PV}(\\text{TV}_3) = \\frac{5,150.00}{(1.08)^3} = \\frac{5,150.00}{1.259712} = 4,088.236\\text{ USD million} \\approx 4,088.24\\text{ USD million}$$.",
            "distractor_analysis": {
                "A": "Uses $\\text{FCFF}_3$ in the numerator without growing it: $250.0 / 0.05 = 5,000.00\\text{ USD million}$; $\\text{PV} = 3,969.16\\text{ USD million}$.",
                "C": "Compounds growth twice or uses $g = 3.5\\%$."
            }
        },
        {
            "id": "L2-EQ-V06-Q3",
            "level": 2,
            "topic": "Equity Valuation",
            "subtopic": "Per-Share Equity Value under Perpetual Growth",
            "vignette_id": "V06",
            "vignette_title": v06_title,
            "vignette_text": v06_text,
            "los": "Calculate enterprise value and per-share equity value using a two-stage FCFF model.",
            "question": "Using Method 1 (Perpetual Growth), the estimated intrinsic value of Valera's common equity per share is closest to:",
            "options": {
                "A": "73.55 USD.",
                "B": "83.15 USD.",
                "C": "92.75 USD."
            },
            "answer": "B",
            "explanation": "Step 1: Calculate total Enterprise Value (EV): $$\\text{EV} = \\text{PV}(\\text{Stage 1}) + \\text{PV}(\\text{TV}_3) = 549.46 + 4,088.24 = 4,637.70\\text{ USD million}$$ Step 2: Calculate total common equity value: $$\\text{Equity Value} = \\text{EV} - \\text{Debt} + \\text{Cash} = 4,637.70 - 600.0 + 120.0 = 4,157.70\\text{ USD million}$$ Step 3: Calculate value per share: $$\\text{Value per share} = \\frac{4,157.70\\text{ USD million}}{50.0\\text{ million shares}} = 83.154\\text{ USD} \\approx 83.15\\text{ USD}$$.",
            "distractor_analysis": {
                "A": "Deducts cash instead of adding it: $(4,637.70 - 600 - 120) / 50 = 3,917.70 / 50 = 78.35\\text{ USD}$ or forgets to add cash.",
                "C": "Omits debt subtraction entirely: $4,637.70 / 50 = 92.75\\text{ USD}$."
            }
        },
        {
            "id": "L2-EQ-V06-Q4",
            "level": 2,
            "topic": "Equity Valuation",
            "subtopic": "Terminal Value via Exit Multiple",
            "vignette_id": "V06",
            "vignette_title": v06_title,
            "vignette_text": v06_text,
            "los": "Calculate terminal value and per-share equity value using an exit multiple approach.",
            "question": "Under Method 2 (Exit Multiple of $9.00\\times$ Year 3 EBITDA), the estimated intrinsic value of Valera's common equity per share is closest to:",
            "options": {
                "A": "55.69 USD.",
                "B": "65.29 USD.",
                "C": "74.89 USD."
            },
            "answer": "A",
            "explanation": "Step 1: Calculate terminal value at $t = 3$ using exit multiple: $$\\text{TV}_3 = 9.00 \\times 380.0 = 3,420.00\\text{ USD million}$$ Step 2: Discount $\\text{TV}_3$ to present value at WACC ($8.00\\%$): $$\\text{PV}(\\text{TV}_3) = \\frac{3,420.00}{(1.08)^3} = \\frac{3,420.00}{1.259712} = 2,714.906\\text{ USD million}$$ Step 3: Compute total Enterprise Value: $$\\text{EV} = \\text{PV}(\\text{Stage 1}) + \\text{PV}(\\text{TV}_3) = 549.46 + 2,714.91 = 3,264.37\\text{ USD million}$$ Step 4: Compute common equity value and share price: $$\\text{Equity Value} = 3,264.37 - 600.0 + 120.0 = 2,784.37\\text{ USD million}$$ $$\\text{Value per share} = \\frac{2,784.37}{50.0} = 55.687\\text{ USD} \\approx 55.69\\text{ USD}$$.",
            "distractor_analysis": {
                "B": "Forgets to subtract debt: $(3,264.37 + 120.0) / 50 = 67.69\\text{ USD}$ or forgets to add cash.",
                "C": "Discounts TV over 2 years instead of 3 years or arithmetic error."
            }
        },
        {
            "id": "L2-EQ-V06-Q5",
            "level": 2,
            "topic": "Equity Valuation",
            "subtopic": "Terminal Value Method Comparison & Biases",
            "vignette_id": "V06",
            "vignette_title": v06_title,
            "vignette_text": v06_text,
            "los": "Contrast the Gordon Growth and market multiple approaches to estimating terminal value.",
            "question": "Which of the following criticisms most accurately highlights a fundamental risk when combining a discounted cash flow model with a market exit multiple to estimate terminal value?",
            "options": {
                "A": "Market exit multiples violate the assumption that operating cash flows are discounted at WACC.",
                "B": "Market exit multiples can introduce circularity and market irrationality by anchoring the DCF to potentially overvalued or depressed peer multiples rather than fundamental cash generation.",
                "C": "Exit multiples can only be applied to Net Income, making them incompatible with FCFF Enterprise Value models."
            },
            "answer": "B",
            "explanation": "A primary analytical vulnerability of the exit multiple method is circularity and vulnerability to market bubbles or distress: if the current market multiple is distorted by broad market sentiment, applying that multiple to terminal EBITDA imports that exact distortion into an otherwise rigorous discounted cash flow model.",
            "distractor_analysis": {
                "A": "Discounting the resulting terminal enterprise value at WACC is mathematically and theoretically consistent.",
                "C": "Exit multiples (especially EV/EBITDA and EV/EBIT) are designed specifically for Enterprise Value and FCFF models."
            }
        }
    ]
    vignettes.append((v06_title, v06_text, v06_questions))

    # =========================================================================
    # Vignette 7: V07
    # =========================================================================
    v07_text = (
        "Synthex Pharmaceuticals (SP) is an oncology-focused biotechnology and commercial therapeutics company. "
        "Senior equity research analyst Maya Patel is evaluating Synthex's relative valuation using P/E multiples and the PEG ratio. "
        "Synthex's common shares currently trade at $P_0 = 64.00\\text{ USD}$.\n\n"
        "Financial data for Synthex reveals:\n"
        "- Trailing 12-month diluted EPS ($E_0$): 3.20 USD\n"
        "- Consensus forward 12-month forecasted EPS ($E_1$): 4.00 USD\n"
        "- Expected 5-year annualized EPS growth rate ($g_{\\text{EPS}}$): 10.00%\n"
        "- Dividend payout ratio ($1 - b$): 45.0% (retention ratio $b = 55.0\\%$)\n"
        "- Cost of equity ($r$): 9.50%\n"
        "- Long-term sustainable dividend growth rate ($g$): 5.50%\n\n"
        "Patel also monitors Synthex's peer group, where the median forward P/E is $18.50\\times$ and the median PEG ratio is $1.60$. "
        "In addition, the investment committee discusses cyclical earnings distortions and the Molodovsky effect."
    )
    v07_title = "Synthex Pharmaceuticals: Trailing vs. Forward P/E, Justified P/E, & PEG Analysis"

    v07_questions = [
        {
            "id": "L2-EQ-V07-Q1",
            "level": 2,
            "topic": "Equity Valuation",
            "subtopic": "Trailing and Forward P/E Calculation",
            "vignette_id": "V07",
            "vignette_title": v07_title,
            "vignette_text": v07_text,
            "los": "Calculate and contrast trailing and forward price-to-earnings (P/E) ratios.",
            "question": "Synthex's trailing P/E and forward P/E ratios are closest to:",
            "options": {
                "A": "Trailing P/E of 20.00x; Forward P/E of 16.00x.",
                "B": "Trailing P/E of 16.00x; Forward P/E of 20.00x.",
                "C": "Trailing P/E of 21.33x; Forward P/E of 17.50x."
            },
            "answer": "A",
            "explanation": "Trailing P/E uses trailing EPS: $$\\text{Trailing P/E} = \\frac{P_0}{E_0} = \\frac{64.00}{3.20} = 20.00\\times$$ Forward P/E uses consensus next-year forecasted EPS: $$\\text{Forward P/E} = \\frac{P_0}{E_1} = \\frac{64.00}{4.00} = 16.00\\times$$.",
            "distractor_analysis": {
                "B": "Inverts the definitions of trailing and forward P/E.",
                "C": "Applies incorrect EPS inputs."
            }
        },
        {
            "id": "L2-EQ-V07-Q2",
            "level": 2,
            "topic": "Equity Valuation",
            "subtopic": "Justified P/E Multiples from Fundamentals",
            "vignette_id": "V07",
            "vignette_title": v07_title,
            "vignette_text": v07_text,
            "los": "Calculate justified forward and trailing P/E ratios based on fundamentals.",
            "question": "Based on the Gordon Growth Model fundamentals ($r = 9.50\\%$, $g = 5.50\\%$, payout $= 45.0\\%$), Synthex's justified forward P/E and justified trailing P/E are closest to:",
            "options": {
                "A": "Justified Forward P/E of 10.66x; Justified Trailing P/E of 11.25x.",
                "B": "Justified Forward P/E of 11.25x; Justified Trailing P/E of 11.87x.",
                "C": "Justified Forward P/E of 12.50x; Justified Trailing P/E of 13.19x."
            },
            "answer": "B",
            "explanation": "Step 1: Calculate justified forward P/E: $$\\frac{P_0}{E_1} = \\frac{1 - b}{r - g} = \\frac{0.450}{0.095 - 0.055} = \\frac{0.450}{0.040} = 11.25\\times$$ Step 2: Calculate justified trailing P/E: $$\\frac{P_0}{E_0} = \\frac{(1 - b) \\times (1 + g)}{r - g} = \\frac{0.450 \\times (1 + 0.055)}{0.040} = \\frac{0.47475}{0.040} = 11.86875\\times \\approx 11.87\\times$$.",
            "distractor_analysis": {
                "A": "Divides by $r$ alone rather than $(r - g)$ or calculation error.",
                "C": "Uses retention ratio $b = 55\\%$ instead of payout ratio $(1 - b) = 45\\%$ in the numerator: $0.55 / 0.040 = 13.75\\times$."
            }
        },
        {
            "id": "L2-EQ-V07-Q3",
            "level": 2,
            "topic": "Equity Valuation",
            "subtopic": "PEG Ratio Calculation and Valuation Assessment",
            "vignette_id": "V07",
            "vignette_title": v07_title,
            "vignette_text": v07_text,
            "los": "Calculate and interpret the price-to-earnings-to-growth (PEG) ratio.",
            "question": "Synthex's PEG ratio based on its forward P/E and expected 5-year growth rate, and its valuation relative to peers (peer median PEG $= 1.60$), are closest to:",
            "options": {
                "A": "PEG of 1.60; trading exactly at fair value relative to peers.",
                "B": "PEG of 2.00; overvalued relative to peers.",
                "C": "PEG of 1.25; undervalued relative to peers."
            },
            "answer": "A",
            "explanation": "The PEG ratio is calculated as forward P/E divided by the expected earnings growth rate (expressed as a whole percentage): $$\\text{PEG} = \\frac{\\text{Forward P/E}}{g_{\\text{EPS}}} = \\frac{16.00}{10.0} = 1.60$$ Because Synthex's PEG of 1.60 matches the peer median PEG of 1.60 exactly, the stock is trading in line with peers on a growth-adjusted basis.",
            "distractor_analysis": {
                "B": "Calculates PEG using trailing P/E: $20.00 / 10.0 = 2.00$, concluding overvaluation.",
                "C": "Uses an erroneous forward growth rate of $12.8\\%$."
            }
        },
        {
            "id": "L2-EQ-V07-Q4",
            "level": 2,
            "topic": "Equity Valuation",
            "subtopic": "Comparative Multiples & Fundamental Valuation",
            "vignette_id": "V07",
            "vignette_title": v07_title,
            "vignette_text": v07_text,
            "los": "Evaluate stock valuation by comparing market multiples with justified multiples derived from fundamentals.",
            "question": "Comparing Synthex's actual market forward P/E ($16.00\\times$) with its fundamentally justified forward P/E ($11.25\\times$), Patel should conclude that Synthex shares are:",
            "options": {
                "A": "Undervalued because its actual market forward P/E is lower than peer median P/E (18.50x).",
                "B": "Overvalued relative to its fundamental drivers because the market forward P/E exceeds the justified forward P/E.",
                "C": "Fairly valued because justified P/E multiples reflect accounting distortions rather than investor requirements."
            },
            "answer": "B",
            "explanation": "When an analyst compares actual market multiples to fundamentally justified multiples, if the actual market multiple ($16.00\\times$) is higher than the fundamentally justified multiple ($11.25\\times$), the stock is overvalued based on its own underlying fundamentals (growth, payout, and risk). Comparing strictly against peer medians ($18.50\\times$) is dangerous because peers may have higher growth or lower risk.",
            "distractor_analysis": {
                "A": "Relying blindly on peer multiples ignores the firm's fundamental growth and cost of equity characteristics.",
                "C": "Fundamentally justified multiples directly incorporate investor required return and cash flow growth."
            }
        },
        {
            "id": "L2-EQ-V07-Q5",
            "level": 2,
            "topic": "Equity Valuation",
            "subtopic": "Molodovsky Effect & Normalized Earnings",
            "vignette_id": "V07",
            "vignette_title": v07_title,
            "vignette_text": v07_text,
            "los": "Explain the Molodovsky effect and evaluate methods of normalizing earnings.",
            "question": "Which of the following observations most accurately describes the Molodovsky effect in cyclical industry valuation?",
            "options": {
                "A": "P/E ratios tend to be countercyclical: artificially high at cyclical troughs due to depressed earnings, and low at cyclical peaks due to peak earnings.",
                "B": "P/E ratios tend to be procyclical: reaching their highest values at cyclical peaks when sentiment is euphoric.",
                "C": "Normalizing earnings by averaging historical EPS over an entire cycle eliminates the need to adjust for business size expansion."
            },
            "answer": "A",
            "explanation": "The Molodovsky effect refers to the countercyclical behavior of P/E ratios for cyclical companies: at the trough of a business cycle, earnings collapse toward zero, causing the P/E ratio to spike to exceptionally high levels despite depressed share prices. Conversely, at cyclical peaks, earnings are inflated, causing the P/E ratio to look deceptively low. Normalizing earnings (via average EPS or average ROE multiplied by current book value) corrects for this phenomenon.",
            "distractor_analysis": {
                "B": "Directly contradicts the Molodovsky effect, which demonstrates countercyclical P/E multiples.",
                "C": "The average EPS method fails to adjust for changes in firm size; the average ROE method is preferred when book value per share has grown."
            }
        }
    ]
    vignettes.append((v07_title, v07_text, v07_questions))

    # =========================================================================
    # Vignette 8: V08
    # =========================================================================
    v08_text = (
        "Sterling Consumer Brands (SCB) is a branded packaged food manufacturer and distributor. "
        "Portfolio manager Henrik Larsson is evaluating SCB's valuation multiples across Price-to-Book (P/B), "
        "Price-to-Sales (P/S), and Enterprise Value-to-EBITDA (EV/EBITDA).\n\n"
        "Per-share financial metrics for SCB include:\n"
        "- Current market price per share ($P_0$): 42.00 USD\n"
        "- Book value per share ($B_0$): 28.00 USD\n"
        "- Sales per share ($S_0$): 70.00 USD\n"
        "- Trailing net profit margin ($\\text{PM}_0 = E_0 / S_0$): 6.00%\n"
        "- Return on Equity (ROE): 14.00%\n"
        "- Required return on equity ($r$): 10.00%\n"
        "- Dividend payout ratio: 50.0% (earnings retention ratio $b = 50.0\\%$)\n"
        "- Sustainable growth rate: $g = b \\times \\text{ROE} = 0.50 \\times 14.00\\% = 7.00\\%$\n\n"
        "Corporate balance sheet and operational figures:\n"
        "- Total common shares outstanding: 50.0 million shares\n"
        "- Total debt (interest-bearing, fair value): 500.0 USD million\n"
        "- Cash and cash equivalents: 80.0 USD million\n"
        "- Trailing EBITDA: 320.0 USD million\n\n"
        "Larsson investigates the impact of intangible assets, share buybacks, and inventory accounting methods on asset-based multiples."
    )
    v08_title = "Sterling Consumer Brands: P/B, P/S, & EV/EBITDA Calibration and Distortions"

    v08_questions = [
        {
            "id": "L2-EQ-V08-Q1",
            "level": 2,
            "topic": "Equity Valuation",
            "subtopic": "Justified Price-to-Book Ratio",
            "vignette_id": "V08",
            "vignette_title": v08_title,
            "vignette_text": v08_text,
            "los": "Calculate and interpret the justified price-to-book (P/B) ratio based on fundamentals.",
            "question": "Sterling's fundamentally justified Price-to-Book (P/B) ratio and actual market P/B ratio are closest to:",
            "options": {
                "A": "Justified P/B of 2.33x; Actual P/B of 1.50x.",
                "B": "Justified P/B of 1.50x; Actual P/B of 2.33x.",
                "C": "Justified P/B of 1.75x; Actual P/B of 1.50x."
            },
            "answer": "A",
            "explanation": "Step 1: Calculate justified P/B using the Gordon Growth framework: $$\\frac{P_0}{B_0} = \\frac{\\text{ROE} - g}{r - g} = \\frac{0.14 - 0.07}{0.10 - 0.07} = \\frac{0.07}{0.03} = 2.333\\times \\approx 2.33\\times$$ Step 2: Calculate actual market P/B: $$\\text{Actual P/B} = \\frac{P_0}{B_0} = \\frac{42.00}{28.00} = 1.50\\times$$ Because actual P/B ($1.50\\times$) is less than justified P/B ($2.33\\times$), SCB appears undervalued on a book value basis.",
            "distractor_analysis": {
                "B": "Inverts actual and justified P/B multiples.",
                "C": "Calculates justified P/B using $\\text{ROE}/r = 0.14 / 0.10 = 1.40\\times$ or arithmetic error."
            }
        },
        {
            "id": "L2-EQ-V08-Q2",
            "level": 2,
            "topic": "Equity Valuation",
            "subtopic": "Justified Price-to-Sales Ratio",
            "vignette_id": "V08",
            "vignette_title": v08_title,
            "vignette_text": v08_text,
            "los": "Calculate and interpret the justified price-to-sales (P/S) ratio based on fundamentals.",
            "question": "Sterling's fundamentally justified Price-to-Sales (P/S) ratio is closest to:",
            "options": {
                "A": "0.60x.",
                "B": "1.07x.",
                "C": "1.43x."
            },
            "answer": "B",
            "explanation": "The justified Price-to-Sales formula derived from the Gordon Growth Model is: $$\\frac{P_0}{S_0} = \\frac{\\text{PM}_0 \\times (1 - b) \\times (1 + g)}{r - g}$$ Given $\\text{PM}_0 = 0.06$, payout $(1 - b) = 0.50$, $g = 0.07$, and $r = 0.10$: $$\\text{Numerator} = 0.06 \\times 0.50 \\times (1 + 0.07) = 0.03 \\times 1.07 = 0.0321$$ $$\\text{Denominator} = 0.10 - 0.07 = 0.030$$ $$\\frac{P_0}{S_0} = \\frac{0.0321}{0.030} = 1.070\\times$$.",
            "distractor_analysis": {
                "A": "Represents the actual market P/S ratio ($42.00 / 70.00 = 0.60\\times$).",
                "C": "Omits the dividend payout ratio $(1 - b)$ in the numerator: $0.06 \\times 1.07 / 0.03 = 2.14\\times$."
            }
        },
        {
            "id": "L2-EQ-V08-Q3",
            "level": 2,
            "topic": "Equity Valuation",
            "subtopic": "EV/EBITDA Multiple Calculation",
            "vignette_id": "V08",
            "vignette_title": v08_title,
            "vignette_text": v08_text,
            "los": "Calculate enterprise value (EV) and the EV/EBITDA multiple.",
            "question": "Sterling Consumer Brands' Enterprise Value (EV) and EV/EBITDA multiple are closest to:",
            "options": {
                "A": "EV of 2,100.0 USD million; EV/EBITDA of 6.56x.",
                "B": "EV of 2,520.0 USD million; EV/EBITDA of 7.88x.",
                "C": "EV of 2,680.0 USD million; EV/EBITDA of 8.38x."
            },
            "answer": "B",
            "explanation": "Step 1: Calculate Market Capitalization: $$\\text{Market Cap} = 42.00\\text{ USD} \\times 50.0\\text{ million shares} = 2,100.0\\text{ USD million}$$ Step 2: Calculate Enterprise Value: $$\\text{EV} = \\text{Market Cap} + \\text{Total Debt} - \\text{Cash} = 2,100.0 + 500.0 - 80.0 = 2,520.0\\text{ USD million}$$ Step 3: Compute EV/EBITDA: $$\\frac{\\text{EV}}{\\text{EBITDA}} = \\frac{2,520.0}{320.0} = 7.875\\times \\approx 7.88\\times$$.",
            "distractor_analysis": {
                "A": "Uses market cap alone without adjusting for debt and cash: $2,100.0 / 320.0 = 6.56\\times$.",
                "C": "Adds cash instead of subtracting cash: $(2,100.0 + 500.0 + 80.0) / 320.0 = 2,680.0 / 320.0 = 8.38\\times$."
            }
        },
        {
            "id": "L2-EQ-V08-Q4",
            "level": 2,
            "topic": "Equity Valuation",
            "subtopic": "Accounting Distortions in Book Value",
            "vignette_id": "V08",
            "vignette_title": v08_title,
            "vignette_text": v08_text,
            "los": "Explain how accounting methods and corporate actions distort Price-to-Book ratios.",
            "question": "Which of the following corporate actions or accounting choices most significantly distorts book value of equity downward, artificially inflating a company's Price-to-Book (P/B) ratio?",
            "options": {
                "A": "Aggressive capitalization of operating development costs onto the balance sheet.",
                "B": "Substantial common share repurchases executed at market prices significantly exceeding book value per share.",
                "C": "Revaluing property, plant, and equipment upward to fair market value under IFRS revaluation model."
            },
            "answer": "B",
            "explanation": "When a company repurchases common shares at a market price exceeding book value per share, total shareholders' equity is reduced by the full market cost of the buyback. This reduces book value per share disproportionately relative to market price, thereby artificially inflating the reported P/B ratio (in extreme cases, resulting in negative book value).",
            "distractor_analysis": {
                "A": "Capitalizing development costs creates assets and increases book value of equity, which lowers P/B.",
                "C": "Upward revaluation of PP&E creates a revaluation surplus in equity, increasing book value and lowering P/B."
            }
        },
        {
            "id": "L2-EQ-V08-Q5",
            "level": 2,
            "topic": "Equity Valuation",
            "subtopic": "EV/EBITDA Advantages over P/E",
            "vignette_id": "V08",
            "vignette_title": v08_title,
            "vignette_text": v08_text,
            "los": "Evaluate the rationale for using EV/EBITDA rather than P/E multiples across capital-intensive industries.",
            "question": "In capital-intensive industries with cross-border operations, EV/EBITDA is generally preferred over P/E because EV/EBITDA:",
            "options": {
                "A": "Is unaffected by differences in capital structure, depreciation methods, and marginal tax rates.",
                "B": "Includes working capital investments, making it an exact surrogate for free cash flow to equity.",
                "C": "Is always lower than P/E, providing a more conservative intrinsic valuation."
            },
            "answer": "A",
            "explanation": "EV/EBITDA evaluates pre-interest, pre-tax operating performance relative to the entire enterprise capital base. Consequently, it removes distortions arising from differing degrees of financial leverage (interest expense), differing depreciation and amortization policies (capital intensity age and accounting discretion), and differing statutory corporate tax rates across international jurisdictions.",
            "distractor_analysis": {
                "B": "EBITDA does not subtract capital expenditures or working capital investments; it is not a direct measure of free cash flow.",
                "C": "Whether EV/EBITDA is numerically lower than P/E is mathematically irrelevant to valuation quality."
            }
        }
    ]
    vignettes.append((v08_title, v08_text, v08_questions))

    # =========================================================================
    # Vignette 9: V09
    # =========================================================================
    v09_text = (
        "Orion Cloud Technologies is a high-growth provider of enterprise cybersecurity software. "
        "Lead technology analyst Chloe Bennett is performing a cross-sectional comparable company analysis for Orion. "
        "Chloe gathers valuation multiples from three closely matched publicly traded SaaS peers:\n\n"
        "- Peer A: EV/EBITDA of 12.00x\n"
        "- Peer B: EV/EBITDA of 15.00x\n"
        "- Peer C: EV/EBITDA of 20.00x\n\n"
        "Chloe considers using the harmonic mean rather than the simple arithmetic mean of the peer group multiples to avoid "
        "upward skewness caused by large valuation outliers.\n\n"
        "Financial data for Orion Cloud Technologies:\n"
        "- Trailing EBITDA: 85.0 USD million\n"
        "- Interest-bearing debt (market value): 220.0 USD million\n"
        "- Cash and marketable securities: 60.0 USD million\n"
        "- Non-controlling interest on the balance sheet: 30.0 USD million\n"
        "- Common shares outstanding: 25.0 million shares\n\n"
        "Additionally, Chloe examines whether Enterprise Value-to-Sales (EV/S) should be used for early-stage unprofitable peers, "
        "and reviews common screening biases including survivorship bias and look-ahead bias."
    )
    v09_title = "Orion Cloud Technologies: EV Multiples, Harmonic Mean, & Peer Comparables Analysis"

    v09_questions = [
        {
            "id": "L2-EQ-V09-Q1",
            "level": 2,
            "topic": "Equity Valuation",
            "subtopic": "Harmonic Mean of Price Multiples",
            "vignette_id": "V09",
            "vignette_title": v09_title,
            "vignette_text": v09_text,
            "los": "Calculate and explain the rationale for using the harmonic mean of valuation multiples.",
            "question": "The harmonic mean of the peer group EV/EBITDA multiples (12.00x, 15.00x, 20.00x) is closest to:",
            "options": {
                "A": "15.00x.",
                "B": "15.67x.",
                "C": "16.25x."
            },
            "answer": "A",
            "explanation": "The harmonic mean of $n$ observations is given by: $$\\bar{x}_H = \\frac{n}{\\sum_{i=1}^n \\frac{1}{x_i}}$$ Substituting the peer multiples: $$\\sum \\frac{1}{x_i} = \\frac{1}{12.0} + \\frac{1}{15.0} + \\frac{1}{20.0} = 0.08333 + 0.06667 + 0.05000 = 0.2000$$ $$\\bar{x}_H = \\frac{3}{0.2000} = 15.00\\times$$ Note that the simple arithmetic mean is $(12 + 15 + 20) / 3 = 15.67\\times$. The harmonic mean mitigates the upward bias caused by high multiple outliers.",
            "distractor_analysis": {
                "B": "Represents the simple arithmetic mean: $(12.0 + 15.0 + 20.0) / 3 = 15.67\\times$.",
                "C": "Represents an unweighted median midpoint or arithmetic error."
            }
        },
        {
            "id": "L2-EQ-V09-Q2",
            "level": 2,
            "topic": "Equity Valuation",
            "subtopic": "Implied Equity Value via Peer Multiple",
            "vignette_id": "V09",
            "vignette_title": v09_title,
            "vignette_text": v09_text,
            "los": "Calculate implied enterprise value and per-share equity value using peer multiples.",
            "question": "Using the peer harmonic mean EV/EBITDA multiple of $15.00\\times$ and adjusting for debt, cash, and non-controlling interest, the implied value of Orion Cloud's common stock per share is closest to:",
            "options": {
                "A": "39.40 USD.",
                "B": "43.40 USD.",
                "C": "45.80 USD."
            },
            "answer": "B",
            "explanation": "Step 1: Calculate implied Enterprise Value: $$\\text{Implied EV} = 15.00 \\times 85.0\\text{ USD million} = 1,275.0\\text{ USD million}$$ Step 2: Compute implied common equity value: $$\\text{Equity Value} = \\text{EV} - \\text{Debt} - \\text{Non-controlling Interest} + \\text{Cash}$$ $$\\text{Equity Value} = 1,275.0 - 220.0 - 30.0 + 60.0 = 1,085.0\\text{ USD million}$$ Step 3: Compute implied price per share: $$\\text{Value per share} = \\frac{1,085.0\\text{ USD million}}{25.0\\text{ million shares}} = 43.40\\text{ USD}$$.",
            "distractor_analysis": {
                "A": "Forgets to add cash back to enterprise value: $(1,275.0 - 220.0 - 30.0) / 25.0 = 1,025.0 / 25.0 = 41.00\\text{ USD}$ or treats non-controlling interest as an asset.",
                "C": "Omits non-controlling interest deduction: $(1,275.0 - 220.0 + 60.0) / 25.0 = 1,115.0 / 25.0 = 44.60\\text{ USD}$."
            }
        },
        {
            "id": "L2-EQ-V09-Q3",
            "level": 2,
            "topic": "Equity Valuation",
            "subtopic": "Enterprise Value Adjustments for Balance Sheet Claims",
            "vignette_id": "V09",
            "vignette_title": v09_title,
            "vignette_text": v09_text,
            "los": "Explain appropriate balance sheet adjustments when calculating enterprise value.",
            "question": "In reconciling Enterprise Value to common equity value, non-controlling interest (minority interest) and pension fund deficits should most appropriately be treated as:",
            "options": {
                "A": "Additions to Enterprise Value because they represent capital provided to the consolidated entity.",
                "B": "Deductions from Enterprise Value because they represent senior non-common equity claims against total firm assets.",
                "C": "Ignored entirely because they do not represent third-party interest-bearing debt."
            },
            "answer": "B",
            "explanation": "Enterprise Value represents the total value of the firm's core operating assets. In a consolidated balance sheet, 100% of the operating assets and operating earnings (EBITDA) of controlled subsidiaries are included. Non-controlling interests represent the equity claim of outside shareholders on those assets. Similarly, underfunded pension deficits represent debt-like senior liabilities. Therefore, both must be deducted from Enterprise Value to arrive at common equity value.",
            "distractor_analysis": {
                "A": "Adding non-controlling interests would double count claims and overstate common equity.",
                "C": "Failing to deduct minority claims and pension liabilities artificially inflates the value of common stock."
            }
        },
        {
            "id": "L2-EQ-V09-Q4",
            "level": 2,
            "topic": "Equity Valuation",
            "subtopic": "EV/Sales Multiple Applicability",
            "vignette_id": "V09",
            "vignette_title": v09_title,
            "vignette_text": v09_text,
            "los": "Evaluate the strengths and limitations of the Enterprise Value-to-Sales (EV/S) multiple.",
            "question": "For high-growth enterprise SaaS companies that generate negative Net Income and negative EBITDA, the Enterprise Value-to-Sales (EV/S) multiple is advantageous primarily because:",
            "options": {
                "A": "Sales are positive and less susceptible to distortion from accounting policies than earnings, although EV/S ignores differences in operating cost structures.",
                "B": "EV/S directly incorporates gross margin and customer acquisition cost efficiency.",
                "C": "Sales multiples are mathematically immune to revenue recognition distortions."
            },
            "answer": "A",
            "explanation": "EV/S is meaningful even when earnings and EBITDA are negative. Furthermore, top-line revenue is generally less vulnerable to accounting distortion than bottom-line earnings. However, the primary limitation of EV/S is that it ignores differences in cost structures, operating margins, and capital requirements between competing firms.",
            "distractor_analysis": {
                "B": "EV/S does not capture operating margins or customer acquisition costs without external adjustments.",
                "C": "Sales multiples are definitely vulnerable to aggressive revenue recognition (e.g., upfront recognition of multi-year SaaS contracts)."
            }
        },
        {
            "id": "L2-EQ-V09-Q5",
            "level": 2,
            "topic": "Equity Valuation",
            "subtopic": "Screening Biases in Comparables Analysis",
            "vignette_id": "V09",
            "vignette_title": v09_title,
            "vignette_text": v09_text,
            "los": "Identify and explain biases in financial screening and comparable company selection.",
            "question": "If Chloe backtests a peer valuation screen using a historical database that excludes companies that went bankrupt, merged, or were delisted during the backtest period, her analysis will most likely suffer from:",
            "options": {
                "A": "Look-ahead bias, leading to delayed entry signals.",
                "B": "Survivorship bias, resulting in an upwardly skewed estimate of historical peer performance and apparent returns.",
                "C": "Data-snooping bias, caused by testing excessive fundamental variables without theoretical foundation."
            },
            "answer": "B",
            "explanation": "Survivorship bias occurs when failed, bankrupt, or delisted firms are excluded from historical sample data, leaving only successful 'survivors'. This systematically biases historical returns upward and paints an overly optimistic picture of peer performance and multiple valuation characteristics.",
            "distractor_analysis": {
                "A": "Look-ahead bias involves using information that was not publicly available at the time of the simulated decision.",
                "C": "Data snooping occurs when an analyst continuously tests statistical relationships until finding a spurious correlation."
            }
        }
    ]
    vignettes.append((v09_title, v09_text, v09_questions))

    # =========================================================================
    # Vignette 10: V10
    # =========================================================================
    v10_text = (
        "Cobalt Engineering Corp (CEC) is a heavy civil engineering contractor specializing in marine port infrastructure. "
        "Financial analyst Tariq Mansoor is valuing CEC using the Residual Income (RI) framework, Economic Value Added (EVA), "
        "and Market Value Added (MVA).\n\n"
        "Per-share financial data for CEC:\n"
        "- Current book value per share ($B_0$): 45.00 USD\n"
        "- Forecasted Year 1 Earnings per Share ($E_1$): 6.30 USD\n"
        "- Dividend payout ratio: 30.0% (expected Year 1 dividend $D_1 = 1.89\\text{ USD}$)\n"
        "- Cost of equity ($r$): 9.00%\n"
        "- Clean surplus accounting holds: $B_1 = B_0 + E_1 - D_1$\n\n"
        "Corporate financial metrics for CEC:\n"
        "- Total capital employed: 1,200.0 USD million (40% debt, 60% equity)\n"
        "- Net Operating Profit After Tax (NOPAT): 132.0 USD million\n"
        "- Weighted Average Cost of Capital (WACC): 8.00%\n"
        "- Total market value of the firm (debt + equity): 1,750.0 USD million\n\n"
        "Tariq also examines violations of clean surplus accounting caused by Other Comprehensive Income (OCI) items."
    )
    v10_title = "Cobalt Engineering: Residual Income, Clean Surplus Accounting, EVA, & MVA"

    v10_questions = [
        {
            "id": "L2-EQ-V10-Q1",
            "level": 2,
            "topic": "Equity Valuation",
            "subtopic": "Residual Income Calculation",
            "vignette_id": "V10",
            "vignette_title": v10_title,
            "vignette_text": v10_text,
            "los": "Calculate residual income (RI) and explain the equity charge.",
            "question": "Forecasted per-share Residual Income (RI) for Cobalt Engineering for Year 1 is closest to:",
            "options": {
                "A": "2.25 USD.",
                "B": "4.05 USD.",
                "C": "4.41 USD."
            },
            "answer": "A",
            "explanation": "Residual income is net income minus the equity charge: $$\\text{RI}_t = E_t - (r \\times B_{t-1})$$ Calculate equity charge: $$\\text{Equity Charge} = r \\times B_0 = 0.090 \\times 45.00\\text{ USD} = 4.05\\text{ USD}$$ Subtract from forecasted EPS: $$\\text{RI}_1 = 6.30 - 4.05 = 2.25\\text{ USD}$$.",
            "distractor_analysis": {
                "B": "Represents the equity charge alone ($0.09 \\times 45.00 = 4.05\\text{ USD}$).",
                "C": "Subtracts the dividend instead of the equity charge: $6.30 - 1.89 = 4.41\\text{ USD}$."
            }
        },
        {
            "id": "L2-EQ-V10-Q2",
            "level": 2,
            "topic": "Equity Valuation",
            "subtopic": "Clean Surplus Relation & OCI Violations",
            "vignette_id": "V10",
            "vignette_title": v10_title,
            "vignette_text": v10_text,
            "los": "Demonstrate the clean surplus relationship and evaluate the impact of clean surplus violations.",
            "question": "Under clean surplus accounting, Cobalt's forecasted book value per share at the end of Year 1 ($B_1$), and an item that violates clean surplus, are closest to:",
            "options": {
                "A": "B1 of 49.41 USD; foreign currency translation gains/losses under OCI.",
                "B": "B1 of 51.30 USD; routine depreciation expense.",
                "C": "B1 of 47.25 USD; share repurchases executed exactly at book value."
            },
            "answer": "A",
            "explanation": "Under the clean surplus relation: $$B_1 = B_0 + E_1 - D_1 = 45.00 + 6.30 - 1.89 = 49.41\\text{ USD}$$ Clean surplus requires that all balance sheet equity changes (other than capital contributions and dividend distributions) pass through the income statement. Items that bypass net income directly to Other Comprehensive Income (OCI)—such as cumulative foreign currency translation adjustments, unrealized gains/losses on available-for-sale debt securities, and defined benefit pension actuarial adjustments—violate the clean surplus relation.",
            "distractor_analysis": {
                "B": "Omits dividend deduction ($45.00 + 6.30 = 51.30\\text{ USD}$) and depreciation does not violate clean surplus.",
                "C": "Incorrect arithmetic and share buybacks at book value do not violate clean surplus."
            }
        },
        {
            "id": "L2-EQ-V10-Q3",
            "level": 2,
            "topic": "Equity Valuation",
            "subtopic": "Economic Value Added (EVA)",
            "vignette_id": "V10",
            "vignette_title": v10_title,
            "vignette_text": v10_text,
            "los": "Calculate Economic Value Added (EVA).",
            "question": "Cobalt Engineering's Economic Value Added (EVA) for the year is closest to:",
            "options": {
                "A": "36.0 USD million.",
                "B": "60.0 USD million.",
                "C": "96.0 USD million."
            },
            "answer": "A",
            "explanation": "EVA measures economic profit generated over and above the total cost of capital: $$\\text{EVA} = \\text{NOPAT} - (\\text{WACC} \\times \\text{Total Capital})$$ Calculate capital charge: $$\\text{Capital Charge} = 0.080 \\times 1,200.0\\text{ USD million} = 96.0\\text{ USD million}$$ Calculate EVA: $$\\text{EVA} = 132.0 - 96.0 = 36.0\\text{ USD million}$$.",
            "distractor_analysis": {
                "B": "Uses cost of equity ($9.00\\% \\times 1,200 = 108$, $132 - 108 = 24$) or arithmetic error.",
                "C": "Represents the total capital charge alone ($96.0\\text{ USD million}$)."
            }
        },
        {
            "id": "L2-EQ-V10-Q4",
            "level": 2,
            "topic": "Equity Valuation",
            "subtopic": "Market Value Added (MVA)",
            "vignette_id": "V10",
            "vignette_title": v10_title,
            "vignette_text": v10_text,
            "los": "Calculate and interpret Market Value Added (MVA).",
            "question": "Cobalt Engineering's Market Value Added (MVA) is closest to:",
            "options": {
                "A": "360.0 USD million.",
                "B": "550.0 USD million.",
                "C": "750.0 USD million."
            },
            "answer": "B",
            "explanation": "Market Value Added measures cumulative value created by management above the capital supplied by investors: $$\\text{MVA} = \\text{Total Market Value of Capital} - \\text{Total Capital Employed}$$ Given market value of $1,750.0\\text{ USD million}$ and capital employed of $1,200.0\\text{ USD million}$: $$\\text{MVA} = 1,750.0 - 1,200.0 = 550.0\\text{ USD million}$$ MVA represents the market's expectation of the present value of all future EVA.",
            "distractor_analysis": {
                "A": "Multiplies annual EVA by 10 or arithmetic error.",
                "C": "Subtracts equity capital only ($1,750 - 720 = 1,030$) or arithmetic error."
            }
        },
        {
            "id": "L2-EQ-V10-Q5",
            "level": 2,
            "topic": "Equity Valuation",
            "subtopic": "Residual Income Model vs. DCF",
            "vignette_id": "V10",
            "vignette_title": v10_title,
            "vignette_text": v10_text,
            "los": "Compare the residual income model to discounted cash flow models.",
            "question": "A key structural advantage of the Residual Income model relative to multistage Dividend Discount and Free Cash Flow models is that:",
            "options": {
                "A": "A large portion of intrinsic value is recognized immediately through beginning book value, making terminal value less dominant.",
                "B": "The Residual Income model does not require estimating a cost of equity or terminal value.",
                "C": "The model is completely unaffected by conservative or aggressive accounting choices."
            },
            "answer": "A",
            "explanation": "In standard DCF/DDM models, the terminal value typically accounts for 60% to 85% of total estimated intrinsic value, making the valuation hypersensitive to terminal growth and WACC assumptions. In the Residual Income model, current book value of equity ($B_0$) is already recognized on the balance sheet, so the discounted stream of residual income (and especially terminal residual income) represents a much smaller proportion of total estimated value.",
            "distractor_analysis": {
                "B": "The Residual Income model strictly requires estimating a cost of equity and terminal residual income.",
                "C": "Accounting choices alter book value and future residual income; while clean surplus guarantees theoretical convergence, near-term estimates are affected."
            }
        }
    ]
    vignettes.append((v10_title, v10_text, v10_questions))

    # =========================================================================
    # Vignette 11: V11
    # =========================================================================
    v11_text = (
        "Apex Dynamics (AD) develops industrial robotics and automated guided vehicles. "
        "Senior equity analyst Simon Vance is constructing a multistage Residual Income model for AD. "
        "AD's current book value per share ($B_0$) is $36.00\\text{ USD}$, and its cost of equity ($r$) is estimated at $10.00\\%$.\n\n"
        "Simon forecasts Year 1 Residual Income ($\\text{RI}_1$) at $4.40\\text{ USD}$ per share. "
        "Because competitive pressures erode economic rents over time, Simon models the terminal period beyond Year 1 "
        "using alternative persistence parameters ($\\omega$):\n\n"
        "- Scenario 1: Residual income persists with a decay persistence factor of $\\omega = 0.60$ indefinitely.\n"
        "- Scenario 2: Residual income continues indefinitely at the Year 1 level of $4.40\\text{ USD}$ (constant persistence, $\\omega = 1.0$).\n"
        "- Scenario 3: Residual income drops immediately to zero after Year 1 (zero persistence, $\\omega = 0.0$).\n\n"
        "Simon also evaluates how accounting conservatism (such as expensing R&D) affects book value, ROE, and long-term residual income."
    )
    v11_title = "Apex Dynamics: Multistage Residual Income & Persistence Factor Modeling"

    v11_questions = [
        {
            "id": "L2-EQ-V11-Q1",
            "level": 2,
            "topic": "Equity Valuation",
            "subtopic": "Present Value of Continuing Residual Income",
            "vignette_id": "V11",
            "vignette_title": v11_title,
            "vignette_text": v11_text,
            "los": "Calculate the present value of continuing residual income given a persistence parameter.",
            "question": "Under Scenario 1 (persistence parameter $\\omega = 0.60$), the present value at $t = 0$ of continuing residual income beyond Year 0 is closest to:",
            "options": {
                "A": "7.33 USD.",
                "B": "8.80 USD.",
                "C": "11.00 USD."
            },
            "answer": "B",
            "explanation": "When residual income begins at $\\text{RI}_1$ and declines at a persistence factor $\\omega$ where $0 \\le \\omega < 1$, the present value of continuing residual income at $t = 0$ is: $$\\text{PV of Continuing RI} = \\frac{\\text{RI}_1}{1 + r - \\omega}$$ Substituting $\\text{RI}_1 = 4.40\\text{ USD}$, $r = 0.10$, and $\\omega = 0.60$: $$\\text{PV of Continuing RI} = \\frac{4.40}{1 + 0.10 - 0.60} = \\frac{4.40}{0.50} = 8.80\\text{ USD}$$.",
            "distractor_analysis": {
                "A": "Uses $(1 + r + \\omega) = 1.70$ in denominator ($4.40 / 1.70 = 2.59$) or misapplies discount factor.",
                "C": "Uses $\\omega = 0.70$: $4.40 / 0.40 = 11.00\\text{ USD}$."
            }
        },
        {
            "id": "L2-EQ-V11-Q2",
            "level": 2,
            "topic": "Equity Valuation",
            "subtopic": "Intrinsic Value with Persistence Factor",
            "vignette_id": "V11",
            "vignette_title": v11_title,
            "vignette_text": v11_text,
            "los": "Calculate the intrinsic value of a common stock using a multistage residual income model with a persistence factor.",
            "question": "Under Scenario 1 (persistence parameter $\\omega = 0.60$), the estimated intrinsic value of Apex Dynamics per share is closest to:",
            "options": {
                "A": "40.40 USD.",
                "B": "44.80 USD.",
                "C": "48.20 USD."
            },
            "answer": "B",
            "explanation": "The intrinsic value under the residual income model is beginning book value plus the present value of continuing residual income: $$V_0 = B_0 + \\frac{\\text{RI}_1}{1 + r - \\omega}$$ Given $B_0 = 36.00\\text{ USD}$ and $\\text{PV of Continuing RI} = 8.80\\text{ USD}$: $$V_0 = 36.00 + 8.80 = 44.80\\text{ USD}$$.",
            "distractor_analysis": {
                "A": "Uses $\\omega = 0$ ($36.00 + 4.00 = 40.00\\text{ USD}$) or arithmetic error.",
                "C": "Adds un-discounted residual income or calculation error."
            }
        },
        {
            "id": "L2-EQ-V11-Q3",
            "level": 2,
            "topic": "Equity Valuation",
            "subtopic": "Zero Persistence vs. Constant Persistence",
            "vignette_id": "V11",
            "vignette_title": v11_title,
            "vignette_text": v11_text,
            "los": "Calculate intrinsic value under zero persistence and constant persistence scenarios.",
            "question": "The estimated intrinsic value of Apex Dynamics per share under Scenario 3 (zero persistence, $\\omega = 0.0$) and Scenario 2 (constant persistence, $\\omega = 1.0$) are closest to:",
            "options": {
                "A": "Scenario 3: 40.00 USD; Scenario 2: 80.00 USD.",
                "B": "Scenario 3: 36.00 USD; Scenario 2: 76.00 USD.",
                "C": "Scenario 3: 40.40 USD; Scenario 2: 72.00 USD."
            },
            "answer": "A",
            "explanation": "Under Scenario 3 (zero persistence, $\\omega = 0$): Residual income drops to zero after Year 1. $$V_0 = B_0 + \\frac{\\text{RI}_1}{1 + r} = 36.00 + \\frac{4.40}{1.10} = 36.00 + 4.00 = 40.00\\text{ USD}$$ Under Scenario 2 (constant persistence, $\\omega = 1.0$): Residual income continues in perpetuity at $4.40\\text{ USD}$. $$V_0 = B_0 + \\frac{\\text{RI}_1}{r} = 36.00 + \\frac{4.40}{0.10} = 36.00 + 44.00 = 80.00\\text{ USD}$$.",
            "distractor_analysis": {
                "B": "For Scenario 3, assumes $\\text{RI}_1 = 0$, giving $V_0 = B_0 = 36.00\\text{ USD}$.",
                "C": "Miscalculates the discount factor for Year 1."
            }
        },
        {
            "id": "L2-EQ-V11-Q4",
            "level": 2,
            "topic": "Equity Valuation",
            "subtopic": "Justified Price-to-Book and Residual Income Relation",
            "vignette_id": "V11",
            "vignette_title": v11_title,
            "vignette_text": v11_text,
            "los": "Explain the relationship between the justified price-to-book ratio and residual income.",
            "question": "In the residual income valuation framework, a company will trade at a justified Price-to-Book ratio strictly greater than 1.0 ($P_0/B_0 > 1.0$) if and only if:",
            "options": {
                "A": "The company pays out 100% of its earnings as dividends.",
                "B": "The company's expected Return on Equity (ROE) strictly exceeds its cost of equity ($r$).",
                "C": "The company's asset beta is greater than the market average of 1.0."
            },
            "answer": "B",
            "explanation": "The justified P/B ratio can be rewritten as: $$\\frac{P_0}{B_0} = 1 + \\frac{\\text{ROE} - r}{r - g}$$ When expected $\\text{ROE} > r$, the firm generates positive residual income, which creates economic value beyond the book value of invested capital ($P_0/B_0 > 1.0$). If $\\text{ROE} = r$, residual income is zero and $P_0/B_0 = 1.0$. If $\\text{ROE} < r$, the firm destroys value and $P_0/B_0 < 1.0$.",
            "distractor_analysis": {
                "A": "Dividend payout policy does not determine whether P/B exceeds 1.0; economic profitability (ROE vs r) does.",
                "C": "A higher beta increases $r$, which actually makes it harder for ROE to exceed $r$."
            }
        },
        {
            "id": "L2-EQ-V11-Q5",
            "level": 2,
            "topic": "Equity Valuation",
            "subtopic": "Accounting Conservatism & Residual Income Dynamics",
            "vignette_id": "V11",
            "vignette_title": v11_title,
            "vignette_text": v11_text,
            "los": "Evaluate the impact of accounting conservatism on book value, ROE, and residual income.",
            "question": "Which of the following describes the long-term impact of accounting conservatism (e.g., immediate expensing of all R&D) on reported book value and subsequent Return on Equity (ROE)?",
            "options": {
                "A": "Book value of equity is permanently understated, and subsequent ROE is artificially inflated.",
                "B": "Book value of equity is permanently overstated, and subsequent ROE is depressed.",
                "C": "Both book value and ROE are understated in all future periods."
            },
            "answer": "A",
            "explanation": "Conservative accounting immediately expenses outlays that have future economic value (e.g., R&D, brand building). This depresses near-term net income and permanently suppresses book value of equity by keeping productive intangible assets off the balance sheet. In subsequent periods, because the denominator (book value) is artificially low while future revenues benefit from past investments, reported ROE is artificially inflated.",
            "distractor_analysis": {
                "B": "Book value is understated, not overstated, by conservative expensing.",
                "C": "Subsequent ROE is inflated because the capital base (denominator) is depressed."
            }
        }
    ]
    vignettes.append((v11_title, v11_text, v11_questions))

    # =========================================================================
    # Vignette 12: V12
    # =========================================================================
    v12_text = (
        "Vanguard Precision Tools (VPT) is a privately held industrial manufacturing company founded and managed by CEO Robert Harris. "
        "An institutional private equity buyout fund is conducting a formal valuation of VPT for a proposed 100% control acquisition.\n\n"
        "VPT reported the following financial performance for the most recent fiscal year:\n"
        "- Reported EBITDA: 15.5 USD million\n\n"
        "The buyout fund's transaction diligence team identifies several non-arm's-length and non-operating transactions:\n"
        "1. Executive Compensation: CEO Robert Harris received $3.2\\text{ USD million}$ in total compensation. Diligence benchmarks "
        "indicate that an independent replacement executive would command market compensation of $1.4\\text{ USD million}$.\n"
        "2. Related-Party Facility Lease: VPT leases its main factory from a partnership owned by Harris at an annual rent of $2.2\\text{ USD million}$. "
        "Current market rent for equivalent manufacturing space is $1.5\\text{ USD million}$.\n"
        "3. Non-recurring Legal Settlement: VPT incurred an isolated litigation settlement fee of $0.8\\text{ USD million}$ defending a patent dispute.\n"
        "4. Non-Operating Income: VPT recorded $0.6\\text{ USD million}$ in rental income from an unrelated vacant parcel of land.\n\n"
        "The diligence team discusses normalized earnings from a controlling versus minority perspective, "
        "as well as private company valuation motives and life-cycle approach selection."
    )
    v12_title = "Vanguard Precision Tools: Private Company Valuation & Earnings Normalization"

    v12_questions = [
        {
            "id": "L2-EQ-V12-Q1",
            "level": 2,
            "topic": "Equity Valuation",
            "subtopic": "EBITDA Normalization Adjustments",
            "vignette_id": "V12",
            "vignette_title": v12_title,
            "vignette_text": v12_text,
            "los": "Calculate normalized earnings for a private company from a controlling shareholder perspective.",
            "question": "From the perspective of a controlling acquirer, Vanguard Precision Tools' normalized EBITDA is closest to:",
            "options": {
                "A": "17.0 USD million.",
                "B": "18.2 USD million.",
                "C": "19.4 USD million."
            },
            "answer": "B",
            "explanation": "Starting from reported EBITDA of $15.5\\text{ USD million}$, adjust from a controlling perspective: 1. Add back excess CEO compensation: $+ (3.2 - 1.4) = +1.8\\text{ USD million}$. 2. Add back above-market related-party rent: $+ (2.2 - 1.5) = +0.7\\text{ USD million}$. 3. Add back non-recurring legal settlement: $+0.8\\text{ USD million}$. 4. Deduct non-operating rental income: $-0.6\\text{ USD million}$. $$\\text{Normalized EBITDA} = 15.5 + 1.8 + 0.7 + 0.8 - 0.6 = 18.2\\text{ USD million}$$.",
            "distractor_analysis": {
                "A": "Omits the related-party lease adjustment or adds non-operating income: $15.5 + 1.8 + 0.8 - 0.6 = 17.5\\text{ USD million}$.",
                "C": "Adds back non-operating income instead of deducting it: $15.5 + 1.8 + 0.7 + 0.8 + 0.6 = 19.4\\text{ USD million}$."
            }
        },
        {
            "id": "L2-EQ-V12-Q2",
            "level": 2,
            "topic": "Equity Valuation",
            "subtopic": "Control vs. Minority Normalization Perspective",
            "vignette_id": "V12",
            "vignette_title": v12_title,
            "vignette_text": v12_text,
            "los": "Contrast earnings normalization adjustments from a controlling versus minority perspective.",
            "question": "If an analyst was valuing a 5% non-voting minority interest in VPT rather than a 100% controlling interest, the adjustments for excess executive compensation and related-party rent should most appropriately be:",
            "options": {
                "A": "Excluded from normalized earnings because a minority shareholder lacks the power to replace management or renegotiate related-party contracts.",
                "B": "Included in full because accounting principles require fair market value adjustments regardless of ownership percentage.",
                "C": "Doubled to compensate the minority shareholder for governance risk."
            },
            "answer": "A",
            "explanation": "A minority shareholder lacks the voting power to remove the owner-manager, lower executive compensation, or renegotiate related-party leases. Because the owner-manager can continue extracting private benefits of control, these discretionary cash flows will not accrue to a minority investor. Therefore, normalizing adjustments for excess compensation and above-market leases are inappropriate when valuing a minority interest.",
            "distractor_analysis": {
                "B": "Fair market value for a minority interest must reflect the actual economic cash flows accessible to that minority interest.",
                "C": "Adjustments are not doubled; governance risk is addressed through the Discount for Lack of Control (DLOC)."
            }
        },
        {
            "id": "L2-EQ-V12-Q3",
            "level": 2,
            "topic": "Equity Valuation",
            "subtopic": "Private Company Valuation Motivations",
            "vignette_id": "V12",
            "vignette_title": v12_title,
            "vignette_text": v12_text,
            "los": "Identify and explain the three primary categories of private company valuation motivations.",
            "question": "Which of the following scenarios represents a compliance-related motivation for valuing a private company?",
            "options": {
                "A": "Valuation of common stock for estate and gift tax filing or financial reporting goodwill impairment testing.",
                "B": "Valuation performed by an investment bank to negotiate an initial public offering (IPO) subscription price.",
                "C": "Valuation performed to settle shareholder oppression claims in corporate dissolution litigation."
            },
            "answer": "A",
            "explanation": "Private company valuations fall into three main categories: (1) Transaction-related (M&A, IPOs, venture capital financing, buyouts); (2) Compliance-related (tax reporting such as gift/estate tax, and financial reporting such as purchase price allocation and goodwill impairment testing under ASC 350 / IFRS 3); and (3) Litigation-related (divorce proceedings, shareholder disputes, bankruptcy).",
            "distractor_analysis": {
                "B": "An IPO pricing valuation is transaction-related.",
                "C": "Settling shareholder oppression disputes is litigation-related."
            }
        },
        {
            "id": "L2-EQ-V12-Q4",
            "level": 2,
            "topic": "Equity Valuation",
            "subtopic": "Private vs. Public Valuation Risk Factors",
            "vignette_id": "V12",
            "vignette_title": v12_title,
            "vignette_text": v12_text,
            "los": "Explain risk factors that distinguish private companies from public companies.",
            "question": "Which of the following characteristics is most characteristic of private companies relative to publicly traded peers, warranting a higher cost of capital?",
            "options": {
                "A": "Greater access to public debt capital markets and lower operational leverage.",
                "B": "Higher customer concentration, key-person dependency, and restricted access to equity capital.",
                "C": "Greater regulatory disclosure requirements and higher analyst following."
            },
            "answer": "B",
            "explanation": "Private companies typically face distinct risk factors compared to public companies: smaller size, higher customer concentration, dependency on key founding executives (key-person risk), illiquid stock, lower quality/depth of financial disclosures, and limited access to institutional capital markets. These factors typically lead to a size premium and company-specific risk premium in the discount rate.",
            "distractor_analysis": {
                "A": "Private companies have restricted access to public debt markets, not greater access.",
                "C": "Public companies face rigorous disclosure requirements and analyst coverage, whereas private companies do not."
            }
        },
        {
            "id": "L2-EQ-V12-Q5",
            "level": 2,
            "topic": "Equity Valuation",
            "subtopic": "Valuation Approach Selection by Life-Cycle Stage",
            "vignette_id": "V12",
            "vignette_title": v12_title,
            "vignette_text": v12_text,
            "los": "Evaluate the selection of valuation approaches across private company life-cycle stages.",
            "question": "For a private company that is an ongoing operating business with established positive cash flows and unique intellectual property, the asset-based approach is generally:",
            "options": {
                "A": "The preferred valuation approach because tangible asset values can be verified objectively without forecasting.",
                "B": "The least appropriate valuation approach because it ignores the going-concern value and future cash flow generation of unrecorded intangible assets.",
                "C": "Identical in output to the capitalized cash flow approach under all circumstances."
            },
            "answer": "B",
            "explanation": "The asset-based approach values a company by summing the fair market values of individual assets and subtracting liabilities. For an ongoing, profitable operating business with customer relationships, goodwill, and intangibles, the asset-based approach is least appropriate because it fails to capture going-concern economic earnings power and typically provides only a floor liquidation value.",
            "distractor_analysis": {
                "A": "Asset-based models are primarily suited for holding companies, resource extraction firms, early-stage asset assemblers, or distressed/liquidation entities.",
                "C": "Asset-based approaches rarely match income approaches for profitable operating companies with substantial intangibles."
            }
        }
    ]
    vignettes.append((v12_title, v12_text, v12_questions))

    # =========================================================================
    # Vignette 13: V13
    # =========================================================================
    v13_text = (
        "Crestview Medical Diagnostics (CMD) is an established private diagnostic imaging and laboratory testing practice. "
        "Certified business appraiser Rachel Goldberg is conducting an appraisal of CMD's common equity for partnership restructuring.\n\n"
        "Financial data for CMD for the year just concluded:\n"
        "- Normalized after-tax cash flow to equity ($CF_0$): 4.80 USD million\n"
        "- Expected long-term constant sustainable growth rate ($g$): 3.00%\n"
        "- Required rate of return on equity ($k_e$): 15.00%\n\n"
        "In addition to the Capitalized Cash Flow (CCF) method, Rachel applies the Excess Earnings Method (EEM) to value CMD's intangible assets:\n"
        "- Normalized Working Capital: 6.0 USD million, with a required return of 6.00%\n"
        "- Normalized Tangible Fixed Assets (fair market value): 18.0 USD million, with a required return of 10.00%\n"
        "- Normalized total firm earnings after tax ($E_0$): 4.80 USD million\n"
        "- Required rate of return on intangible assets ($k_{\\text{intangible}}$): 18.00%\n"
        "- Expected long-term growth rate of intangible cash flows: 3.00%\n\n"
        "Rachel reviews capitalization rates, discount rates, and the limitations of multi-asset return partitioning under the EEM."
    )
    v13_title = "Crestview Medical: Capitalization of Earnings & Excess Earnings Method (EEM)"

    v13_questions = [
        {
            "id": "L2-EQ-V13-Q1",
            "level": 2,
            "topic": "Equity Valuation",
            "subtopic": "Capitalized Cash Flow (CCF) Valuation",
            "vignette_id": "V13",
            "vignette_title": v13_title,
            "vignette_text": v13_text,
            "los": "Calculate the value of a private company using the capitalized cash flow (CCF) method.",
            "question": "Using the Capitalized Cash Flow (CCF) method, the estimated intrinsic value of Crestview Medical's equity is closest to:",
            "options": {
                "A": "32.00 USD million.",
                "B": "40.00 USD million.",
                "C": "41.20 USD million."
            },
            "answer": "C",
            "explanation": "Step 1: Compute expected cash flow for Year 1: $$CF_1 = CF_0 \\times (1 + g) = 4.80 \\times (1 + 0.03) = 4.944\\text{ USD million}$$ Step 2: Compute capitalization rate: $$\\text{Cap Rate} = k_e - g = 0.150 - 0.030 = 0.120 = 12.00\\%$$ Step 3: Compute equity value: $$\\text{Equity Value} = \\frac{CF_1}{k_e - g} = \\frac{4.944}{0.120} = 41.20\\text{ USD million}$$.",
            "distractor_analysis": {
                "A": "Divides by $k_e$ without subtracting growth: $4.80 / 0.15 = 32.00\\text{ USD million}$.",
                "B": "Uses $CF_0$ without growing to $CF_1$: $4.80 / 0.12 = 40.00\\text{ USD million}$."
            }
        },
        {
            "id": "L2-EQ-V13-Q2",
            "level": 2,
            "topic": "Equity Valuation",
            "subtopic": "Capitalization Rate vs. Discount Rate",
            "vignette_id": "V13",
            "vignette_title": v13_title,
            "vignette_text": v13_text,
            "los": "Explain the relationship between the discount rate and the capitalization rate in private valuation.",
            "question": "In the capitalized cash flow method, the capitalization rate is related to the discount rate by the formula:",
            "options": {
                "A": "Capitalization Rate = Discount Rate + Long-Term Growth Rate.",
                "B": "Capitalization Rate = Discount Rate - Long-Term Growth Rate.",
                "C": "Capitalization Rate = Discount Rate / (1 + Long-Term Growth Rate)."
            },
            "answer": "B",
            "explanation": "The capitalization rate is defined as the required rate of return (discount rate) minus the constant expected long-term growth rate: $\\text{Cap Rate} = r - g$. Applying the capitalization rate to Year 1 cash flow ($CF_1$) is mathematically identical to applying the Gordon Growth Model.",
            "distractor_analysis": {
                "A": "Incorrectly adds growth rate, which would deflate valuation.",
                "C": "Incorrectly divides by $(1 + g)$."
            }
        },
        {
            "id": "L2-EQ-V13-Q3",
            "level": 2,
            "topic": "Equity Valuation",
            "subtopic": "Excess Earnings Attribution to Intangibles",
            "vignette_id": "V13",
            "vignette_title": v13_title,
            "vignette_text": v13_text,
            "los": "Calculate excess earnings attributable to intangible assets under the Excess Earnings Method (EEM).",
            "question": "Under the Excess Earnings Method (EEM), the excess earnings attributable to Crestview's intangible assets in Year 0 are closest to:",
            "options": {
                "A": "2.16 USD million.",
                "B": "2.64 USD million.",
                "C": "3.24 USD million."
            },
            "answer": "B",
            "explanation": "Step 1: Compute required return on working capital: $$6.0\\text{ USD million} \\times 6.00\\% = 0.360\\text{ USD million}$$ Step 2: Compute required return on tangible fixed assets: $$18.0\\text{ USD million} \\times 10.00\\% = 1.800\\text{ USD million}$$ Step 3: Compute total earnings required for tangible capital: $$0.360 + 1.800 = 2.160\\text{ USD million}$$ Step 4: Compute excess earnings attributable to intangibles: $$\\text{Excess Earnings} = \\text{Total Normalized Earnings} - \\text{Tangible Earnings Required}$$ $$\\text{Excess Earnings} = 4.80 - 2.16 = 2.64\\text{ USD million}$$.",
            "distractor_analysis": {
                "A": "Represents the total earnings required by tangible assets ($2.16\\text{ USD million}$).",
                "C": "Subtracts only the fixed asset charge: $4.80 - 1.80 = 3.00\\text{ USD million}$ or arithmetic error."
            }
        },
        {
            "id": "L2-EQ-V13-Q4",
            "level": 2,
            "topic": "Equity Valuation",
            "subtopic": "Intangible Asset & Total Firm Value under EEM",
            "vignette_id": "V13",
            "vignette_title": v13_title,
            "vignette_text": v13_text,
            "los": "Calculate total firm value using the Excess Earnings Method.",
            "question": "Using the Excess Earnings Method (EEM), the estimated value of Crestview's intangible assets and total firm equity value are closest to:",
            "options": {
                "A": "Intangible value of 14.67 USD million; Total firm equity of 38.67 USD million.",
                "B": "Intangible value of 18.13 USD million; Total firm equity of 42.13 USD million.",
                "C": "Intangible value of 21.60 USD million; Total firm equity of 45.60 USD million."
            },
            "answer": "B",
            "explanation": "Step 1: Forecast Year 1 intangible earnings: $$\\text{Excess Earnings}_1 = 2.64 \\times (1 + 0.03) = 2.7192\\text{ USD million}$$ Step 2: Compute capitalization rate for intangibles: $$\\text{Intangible Cap Rate} = k_{\\text{intangible}} - g = 0.180 - 0.030 = 0.150 = 15.00\\%$$ Step 3: Compute intangible asset value: $$\\text{Value of Intangibles} = \\frac{2.7192}{0.150} = 18.128\\text{ USD million} \\approx 18.13\\text{ USD million}$$ Step 4: Sum tangible and intangible asset values: $$\\text{Total Equity Value} = \\text{Working Capital} + \\text{Tangible Fixed Assets} + \\text{Intangibles}$$ $$\\text{Total Equity Value} = 6.00 + 18.00 + 18.13 = 42.13\\text{ USD million}$$.",
            "distractor_analysis": {
                "A": "Does not grow excess earnings into Year 1: $2.64 / 0.18 = 14.67\\text{ USD million}$; Total $= 38.67\\text{ USD million}$.",
                "C": "Uses tangible discount rate ($10.0\\%$) instead of intangible discount rate ($18.0\\%$) to capitalize intangibles."
            }
        },
        {
            "id": "L2-EQ-V13-Q5",
            "level": 2,
            "topic": "Equity Valuation",
            "subtopic": "Limitations of Excess Earnings Method",
            "vignette_id": "V13",
            "vignette_title": v13_title,
            "vignette_text": v13_text,
            "los": "Explain the limitations and risks of the Excess Earnings Method.",
            "question": "Which of the following is considered a primary theoretical and practical limitation of the Excess Earnings Method (EEM)?",
            "options": {
                "A": "The method cannot be applied to companies with positive earnings.",
                "B": "The model is highly sensitive to small, subjective changes in the assigned required rates of return across individual asset classes, creating compound estimation error.",
                "C": "The method violates US GAAP and IFRS rules for all purchase price allocations."
            },
            "answer": "B",
            "explanation": "The EEM is known as a 'formula method' and has significant limitations: assigning separate required rates of return to working capital, tangible fixed assets, and intangibles is subjective and difficult to ground empirically. Because intangible value is calculated as a residual capitalized stream, small estimation errors in the required returns on tangible assets compound dramatically into the residual value assigned to intangibles.",
            "distractor_analysis": {
                "A": "The EEM requires positive normalized earnings; it cannot be applied if normalized earnings are negative.",
                "C": "A variation of EEM (the Multi-Period Excess Earnings Method, MPEEM) is actively used in financial reporting for valuing specific primary intangible assets."
            }
        }
    ]
    vignettes.append((v13_title, v13_text, v13_questions))

    # =========================================================================
    # Vignette 14: V14
    # =========================================================================
    v14_text = (
        "Beacon Retail Logistics (BRL) is a privately held third-party logistics (3PL) and fulfillment provider. "
        "Appraisal director Marcus Vance is valuing BRL using market-based and asset-based approaches. "
        "Financial data for BRL includes:\n\n"
        "- Normalized EBITDA: 25.0 USD million\n"
        "- Interest-bearing debt: 65.0 USD million\n"
        "- Cash and cash equivalents: 15.0 USD million\n\n"
        "Marcus gathers data from two market benchmarks:\n"
        "1. Guideline Public Company Method (GPCM): Publicly traded 3PL peers trade at a median EV/EBITDA multiple of $8.50\\times$. "
        "Public peers enjoy broad liquidity, access to equity markets, and diversified customer portfolios.\n"
        "2. Guideline Transactions Method (GTM): Recent controlling M&A acquisitions of private and public logistics peers occurred "
        "at a median EV/EBITDA transaction multiple of $11.00\\times$. Diligence notes that these deals reflected strategic buyer synergies.\n\n"
        "Marcus also performs an Asset-Based Approach (Adjusted Net Asset Method):\n"
        "- Book value of assets: 110.0 USD million; Revalued fair market value of tangible assets: 145.0 USD million.\n"
        "- Book value of liabilities: 70.0 USD million; Revalued fair market value of liabilities: 70.0 USD million.\n\n"
        "Marcus reviews the Prior Transactions Method (PTM) and reconciles the resulting valuation indications."
    )
    v14_title = "Beacon Retail Logistics: GPCM, GTM, Prior Transactions, & Asset-Based Models"

    v14_questions = [
        {
            "id": "L2-EQ-V14-Q1",
            "level": 2,
            "topic": "Equity Valuation",
            "subtopic": "Guideline Public Company Method (GPCM)",
            "vignette_id": "V14",
            "vignette_title": v14_title,
            "vignette_text": v14_text,
            "los": "Calculate firm and equity value using the Guideline Public Company Method (GPCM) and explain control implications.",
            "question": "Using the Guideline Public Company Method (median multiple of $8.50\\times$), Beacon's estimated Enterprise Value and common equity value on a marketable minority basis are closest to:",
            "options": {
                "A": "Enterprise Value of 212.5 USD million; Equity Value of 162.5 USD million.",
                "B": "Enterprise Value of 212.5 USD million; Equity Value of 147.5 USD million.",
                "C": "Enterprise Value of 275.0 USD million; Equity Value of 225.0 USD million."
            },
            "answer": "A",
            "explanation": "Step 1: Compute Enterprise Value: $$\\text{EV} = 8.50 \\times 25.0\\text{ USD million} = 212.5\\text{ USD million}$$ Step 2: Compute common equity value: $$\\text{Equity Value} = \\text{EV} - \\text{Debt} + \\text{Cash} = 212.5 - 65.0 + 15.0 = 162.5\\text{ USD million}$$ Because guideline public company stock trades reflect non-controlling minority transactions, this valuation represents a marketable, minority basis.",
            "distractor_analysis": {
                "B": "Forgets to add cash: $212.5 - 65.0 = 147.5\\text{ USD million}$.",
                "C": "Uses the GTM multiple ($11.0\\times$) rather than the GPCM multiple ($8.5\\times$)."
            }
        },
        {
            "id": "L2-EQ-V14-Q2",
            "level": 2,
            "topic": "Equity Valuation",
            "subtopic": "Guideline Transactions Method (GTM)",
            "vignette_id": "V14",
            "vignette_title": v14_title,
            "vignette_text": v14_text,
            "los": "Calculate firm and equity value using the Guideline Transactions Method (GTM) and contrast with GPCM.",
            "question": "Using the Guideline Transactions Method (median multiple of $11.00\\times$), Beacon's estimated Enterprise Value and common equity value on a controlling basis are closest to:",
            "options": {
                "A": "Enterprise Value of 212.5 USD million; Equity Value of 162.5 USD million.",
                "B": "Enterprise Value of 275.0 USD million; Equity Value of 210.0 USD million.",
                "C": "Enterprise Value of 275.0 USD million; Equity Value of 225.0 USD million."
            },
            "answer": "C",
            "explanation": "Step 1: Compute Enterprise Value: $$\\text{EV} = 11.00 \\times 25.0\\text{ USD million} = 275.0\\text{ USD million}$$ Step 2: Compute common equity value: $$\\text{Equity Value} = \\text{EV} - \\text{Debt} + \\text{Cash} = 275.0 - 65.0 + 15.0 = 225.0\\text{ USD million}$$ Guideline transactions involve controlling acquisitions, so GTM multiples inherently reflect a control premium and buyer synergy expectations.",
            "distractor_analysis": {
                "A": "Uses GPCM multiple ($8.5\\times$) instead of GTM multiple ($11.0\\times$).",
                "B": "Forgets to add cash: $275.0 - 65.0 = 210.0\\text{ USD million}$."
            }
        },
        {
            "id": "L2-EQ-V14-Q3",
            "level": 2,
            "topic": "Equity Valuation",
            "subtopic": "Control Premium Embedded in GTM vs. GPCM",
            "vignette_id": "V14",
            "vignette_title": v14_title,
            "vignette_text": v14_text,
            "los": "Explain why transaction multiples generally exceed public company multiples.",
            "question": "The median GTM multiple ($11.00\\times$) is significantly higher than the median GPCM multiple ($8.50\\times$). Which of the following best explains this divergence?",
            "options": {
                "A": "Public markets systematically undervalue logistics companies due to liquidity penalties.",
                "B": "Acquisitions in the GTM represent control transactions where buyers pay a control premium and capitalize anticipated strategic operational synergies.",
                "C": "GTM multiples are calculated on pre-tax earnings whereas GPCM multiples use after-tax earnings."
            },
            "answer": "B",
            "explanation": "M&A buyout transactions reflect the purchase of 100% controlling interests. Strategic acquirers are willing to pay higher multiples because control grants the ability to eliminate duplicate overhead, capture commercial synergies, and direct all cash flows. In contrast, GPCM multiples reflect trades of minority shares on public stock exchanges where investors have no power to alter corporate operations.",
            "distractor_analysis": {
                "A": "Public markets typically provide a liquidity premium, not a liquidity penalty, compared to private companies.",
                "C": "Both GTM and GPCM EV/EBITDA multiples use pre-interest, pre-tax EBITDA."
            }
        },
        {
            "id": "L2-EQ-V14-Q4",
            "level": 2,
            "topic": "Equity Valuation",
            "subtopic": "Asset-Based Valuation (Adjusted Net Asset Method)",
            "vignette_id": "V14",
            "vignette_title": v14_title,
            "vignette_text": v14_text,
            "los": "Calculate equity value using the asset-based approach and evaluate its limitations.",
            "question": "Using the Adjusted Net Asset Method, Beacon's estimated equity value is closest to:",
            "options": {
                "A": "40.0 USD million.",
                "B": "75.0 USD million.",
                "C": "145.0 USD million."
            },
            "answer": "B",
            "explanation": "Under the Adjusted Net Asset Method: $$\\text{Adjusted Equity Value} = \\text{Fair Market Value of Assets} - \\text{Fair Market Value of Liabilities}$$ $$\\text{Adjusted Equity Value} = 145.0 - 70.0 = 75.0\\text{ USD million}$$ Note that book value of equity is $110.0 - 70.0 = 40.0\\text{ USD million}$. The $75.0\\text{ USD million}$ asset-based value is significantly lower than the income/market indications ($162.5\\text{ USD}$ to $225.0\\text{ USD million}$) because it excludes the value of customer relationships, brand reputation, and future cash generation.",
            "distractor_analysis": {
                "A": "Represents unadjusted historical book value of equity: $110.0 - 70.0 = 40.0\\text{ USD million}$.",
                "C": "Represents total revalued assets without deducting liabilities ($145.0\\text{ USD million}$)."
            }
        },
        {
            "id": "L2-EQ-V14-Q5",
            "level": 2,
            "topic": "Equity Valuation",
            "subtopic": "Prior Transactions Method (PTM)",
            "vignette_id": "V14",
            "vignette_title": v14_title,
            "vignette_text": v14_text,
            "los": "Evaluate the Prior Transactions Method (PTM) for private company valuation.",
            "question": "In evaluating historical share transactions in Beacon's own stock under the Prior Transactions Method (PTM), Marcus should consider a historical transaction most reliable if it:",
            "options": {
                "A": "Occurred within the past 6 months between unrelated arm's-length third parties under consistent industry economic conditions.",
                "B": "Involved an internal transfer of shares between founding family members for estate planning purposes.",
                "C": "Took place four years ago during a private venture financing round at a higher valuation."
            },
            "answer": "A",
            "explanation": "Under the Prior Transactions Method (PTM), historical trades in the subject company's own shares provide highly relevant evidence of fair value only if they are recent, arm's-length transactions between informed, unrelated parties, and if operating and macroeconomic conditions have remained substantially similar since the transaction date.",
            "distractor_analysis": {
                "B": "Transactions between family members are related-party transactions and are not arm's length.",
                "C": "A four-year-old transaction is stale and fails to reflect current economic reality."
            }
        }
    ]
    vignettes.append((v14_title, v14_text, v14_questions))

    # =========================================================================
    # Vignette 15: V15
    # =========================================================================
    v15_text = (
        "Keystone Fabricators is a privately held heavy structural steel fabricator. "
        "Valuation consultant Elena Gomez is appraising a 15% non-voting minority equity interest in Keystone "
        "for gift and estate tax compliance.\n\n"
        "Elena establishes the baseline enterprise valuation: on a controlling, fully marketable basis, "
        "Keystone's total common equity value is estimated at $120.0\\text{ USD million}$.\n\n"
        "Elena examines empirical market evidence regarding valuation adjustments:\n"
        "1. Control Premium: A study of recent acquisitions in comparable industrial manufacturing firms reveals a median takeover control premium of $25.00\\%$.\n"
        "2. Lack of Marketability: Empirical benchmarks from restricted stock studies (Rule 144) and pre-IPO transaction studies indicate an appropriate "
        "Discount for Lack of Marketability (DLOM) of $22.00\\%$.\n\n"
        "Elena reviews the sequence of discounts, the quantitative formula for the Discount for Lack of Control (DLOC), "
        "the total combined discount, and common errors when applying valuation adjustments."
    )
    v15_title = "Keystone Fabricators: DLOC, DLOM, & Combined Valuation Adjustments"

    v15_questions = [
        {
            "id": "L2-EQ-V15-Q1",
            "level": 2,
            "topic": "Equity Valuation",
            "subtopic": "Discount for Lack of Control (DLOC)",
            "vignette_id": "V15",
            "vignette_title": v15_title,
            "vignette_text": v15_text,
            "los": "Calculate the Discount for Lack of Control (DLOC) from a control premium.",
            "question": "Given a median control premium of $25.00\\%$, the implied Discount for Lack of Control (DLOC) is closest to:",
            "options": {
                "A": "20.00%.",
                "B": "25.00%.",
                "C": "31.25%."
            },
            "answer": "A",
            "explanation": "The mathematical relationship linking the control premium and the Discount for Lack of Control (DLOC) is: $$\\text{DLOC} = 1 - \\frac{1}{1 + \\text{Control Premium}}$$ Given a control premium of $0.250$: $$\\text{DLOC} = 1 - \\frac{1}{1 + 0.250} = 1 - \\frac{1}{1.250} = 1 - 0.800 = 0.200 = 20.00\\%$$.",
            "distractor_analysis": {
                "B": "Equates DLOC directly to the control premium ($25.00\\%$), ignoring the non-linear reciprocal relationship.",
                "C": "Multiplies $1.25 \\times 0.25 = 31.25\\%$."
            }
        },
        {
            "id": "L2-EQ-V15-Q2",
            "level": 2,
            "topic": "Equity Valuation",
            "subtopic": "Total Combined Discount Calculation",
            "vignette_id": "V15",
            "vignette_title": v15_title,
            "vignette_text": v15_text,
            "los": "Calculate the total combined discount from DLOC and DLOM.",
            "question": "Combining the Discount for Lack of Control (DLOC $= 20.00\\%$) and the Discount for Lack of Marketability (DLOM $= 22.00\\%$), the total combined discount is closest to:",
            "options": {
                "A": "37.60%.",
                "B": "42.00%.",
                "C": "44.00%."
            },
            "answer": "A",
            "explanation": "Discounts are applied multiplicatively, not additively: $$\\text{Total Combined Discount} = 1 - [(1 - \\text{DLOC}) \\times (1 - \\text{DLOM})]$$ Substituting $\\text{DLOC} = 0.200$ and $\\text{DLOM} = 0.220$: $$\\text{Total Discount} = 1 - [(1 - 0.200) \\times (1 - 0.220)] = 1 - [0.800 \\times 0.780] = 1 - 0.624 = 0.376 = 37.60\\%$$.",
            "distractor_analysis": {
                "B": "Simply adds the two discounts together ($20.00\\% + 22.00\\% = 42.00\\%$), which incorrectly double-counts the overlapping base.",
                "C": "Adds control premium and DLOM ($25\\% + 22\\% - 3\\% = 44\\%$) or calculation error."
            }
        },
        {
            "id": "L2-EQ-V15-Q3",
            "level": 2,
            "topic": "Equity Valuation",
            "subtopic": "Valuation of Non-Marketable Minority Interest",
            "vignette_id": "V15",
            "vignette_title": v15_title,
            "vignette_text": v15_text,
            "los": "Calculate the value of a non-marketable minority equity interest using DLOC and DLOM.",
            "question": "Starting from the controlling, marketable equity value of $120.0\\text{ USD million}$, the estimated value of the 15% non-voting minority interest is closest to:",
            "options": {
                "A": "10.44 USD million.",
                "B": "11.23 USD million.",
                "C": "14.40 USD million."
            },
            "answer": "B",
            "explanation": "Step 1: Compute marketable minority equity value by applying DLOC ($20.00\\%$): $$\\text{Marketable Minority Value} = 120.0 \\times (1 - 0.200) = 96.0\\text{ USD million}$$ Step 2: Compute non-marketable minority equity value by applying DLOM ($22.00\\%$): $$\\text{Non-Marketable Minority Value} = 96.0 \\times (1 - 0.220) = 74.88\\text{ USD million}$$ (Alternatively: $120.0 \\times [1 - 0.376] = 74.88\\text{ USD million}$.) Step 3: Compute the pro-rata 15% interest value: $$\\text{Value of 15\\% Interest} = 74.88\\text{ USD million} \\times 0.15 = 11.232\\text{ USD million} \\approx 11.23\\text{ USD million}$$.",
            "distractor_analysis": {
                "A": "Uses additive discounts of 42%: $120.0 \\times (1 - 0.42) \\times 0.15 = 120.0 \\times 0.58 \\times 0.15 = 10.44\\text{ USD million}$.",
                "C": "Applies DLOC only, omitting DLOM: $96.0 \\times 0.15 = 14.40\\text{ USD million}$."
            }
        },
        {
            "id": "L2-EQ-V15-Q4",
            "level": 2,
            "topic": "Equity Valuation",
            "subtopic": "Option Pricing Models for Estimating DLOM",
            "vignette_id": "V15",
            "vignette_title": v15_title,
            "vignette_text": v15_text,
            "los": "Explain quantitative option pricing models for estimating the Discount for Lack of Marketability (DLOM).",
            "question": "Quantitative option-based models (such as the Chaffe model or Finnerty model) estimate the Discount for Lack of Marketability (DLOM) primarily by framing the lack of marketability as:",
            "options": {
                "A": "The price of a European or average-strike put option required to insure the illiquid shareholder against downside price fluctuations during the restriction period.",
                "B": "The value of a call option granting the holder the right to buy additional shares at a predetermined discount.",
                "C": "The yield spread on an illiquid corporate bond converted to equity volatility."
            },
            "answer": "A",
            "explanation": "Option models for DLOM view the restriction on marketability as depriving the holder of the right to sell the security at will. A marketable share combined with a put option struck at the initial market price guarantees the ability to exit without loss. Therefore, the value of a put option (e.g., Chaffe European put or Finnerty average-strike put) relative to share price serves as a quantitative proxy for DLOM.",
            "distractor_analysis": {
                "B": "Call options capture upside participation, whereas illiquidity risk is downside price locking.",
                "C": "Bond yield spreads reflect credit default risk rather than equity marketability restrictions."
            }
        },
        {
            "id": "L2-EQ-V15-Q5",
            "level": 2,
            "topic": "Equity Valuation",
            "subtopic": "Common Errors in Applying Discounts and Premiums",
            "vignette_id": "V15",
            "vignette_title": v15_title,
            "vignette_text": v15_text,
            "los": "Identify common errors and misapplications of valuation discounts and premiums.",
            "question": "Which of the following represents a serious methodological error when applying valuation discounts and premiums?",
            "options": {
                "A": "Applying a DLOM after applying a DLOC to controlling equity value.",
                "B": "Applying a Discount for Lack of Control (DLOC) to a valuation derived from the Guideline Public Company Method (GPCM).",
                "C": "Deducting debt and adding cash to Enterprise Value before calculating equity discounts."
            },
            "answer": "B",
            "explanation": "Guideline Public Company Method (GPCM) multiples are derived from trading prices of minority shares on public stock exchanges. Therefore, the GPCM already produces a non-controlling (minority) valuation indication. Applying a Discount for Lack of Control (DLOC) to a GPCM valuation represents severe double-counting of the minority discount.",
            "distractor_analysis": {
                "A": "Applying DLOM after DLOC is the standard, correct chronological sequence.",
                "C": "Discounts and premiums apply to equity value, so bridging from Enterprise Value to Equity Value first is correct."
            }
        }
    ]
    vignettes.append((v15_title, v15_text, v15_questions))

    # =========================================================================
    # Vignette 16: V16
    # =========================================================================
    v16_text = (
        "Andean Mining Corp (AMC) operates high-grade copper and precious metals concessions in an emerging market economy in South America. "
        "Corporate finance analyst Carlos Mendoza is estimating the required return on equity ($r_e$) for AMC's capital allocation models.\n\n"
        "Carlos gathers the following macroeconomic and financial market data (all denominated in USD):\n"
        "- US 10-year Treasury bond yield (Risk-free rate, $R_f$): 3.80%\n"
        "- Local emerging market 10-year sovereign USD-denominated bond yield: 6.80%\n"
        "- Sovereign yield spread ($6.80\\% - 3.80\\%$): 3.00%\n"
        "- Annualized standard deviation of the local emerging equity market index ($\\sigma_{\\text{equity}}$): 26.00%\n"
        "- Annualized standard deviation of the local emerging sovereign bond index ($\\sigma_{\\text{bond}}$): 18.00%\n"
        "- Developed market Equity Risk Premium (ERP): 5.00%\n"
        "- Andean Mining's equity beta ($\\beta$): 1.20\n\n"
        "Carlos also values an unlisted domestic processing subsidiary using the Build-up method with domestic inputs:\n"
        "- Risk-free rate ($R_f$): 3.80%\n"
        "- Equity risk premium (ERP): 5.00%\n"
        "- Size premium: 2.50%\n"
        "- Industry risk premium: 1.20%\n"
        "- Company-specific risk premium: 1.50%\n\n"
        "Carlos evaluates the Pastor-Stambaugh model liquidity factor and forward-looking ERP estimation methodologies."
    )
    v16_title = "Andean Mining Corp: Emerging Market Cost of Equity, Build-up, & Country Risk Premium"

    v16_questions = [
        {
            "id": "L2-EQ-V16-Q1",
            "level": 2,
            "topic": "Equity Valuation",
            "subtopic": "Country Risk Premium (CRP) Calculation",
            "vignette_id": "V16",
            "vignette_title": v16_title,
            "vignette_text": v16_text,
            "los": "Calculate the Country Risk Premium (CRP) for an emerging market.",
            "question": "The Country Risk Premium (CRP) for the emerging market where Andean Mining operates is closest to:",
            "options": {
                "A": "3.00%.",
                "B": "4.33%.",
                "C": "5.78%."
            },
            "answer": "B",
            "explanation": "The Country Risk Premium is calculated by scaling the sovereign bond yield spread by the relative annualized volatility of the equity market to the sovereign bond market: $$\\text{CRP} = \\text{Sovereign Yield Spread} \\times \\left( \\frac{\\sigma_{\\text{equity}}}{\\sigma_{\\text{bond}}} \\right)$$ Given sovereign spread $= 6.80\\% - 3.80\\% = 3.00\\%$, $\\sigma_{\\text{equity}} = 26.00\\%$, and $\\sigma_{\\text{bond}} = 18.00\\%$: $$\\text{CRP} = 3.00\\% \\times \\left( \\frac{26.0\\%}{18.0\\%} \\right) = 3.00\\% \\times 1.4444 = 4.333\\% \\approx 4.33\\%$$.",
            "distractor_analysis": {
                "A": "Uses the unadjusted sovereign bond spread ($3.00\\%$), ignoring the higher volatility of equity.",
                "C": "Inverts the volatility ratio or uses an erroneous scaling factor."
            }
        },
        {
            "id": "L2-EQ-V16-Q2",
            "level": 2,
            "topic": "Equity Valuation",
            "subtopic": "Expanded CAPM with Country Risk Premium",
            "vignette_id": "V16",
            "vignette_title": v16_title,
            "vignette_text": v16_text,
            "los": "Calculate the required return on equity using the expanded CAPM incorporating the Country Risk Premium.",
            "question": "Using the expanded CAPM formula ($r_e = R_f + \\beta \\times \\text{ERP} + \\text{CRP}$), Andean Mining's required return on equity is closest to:",
            "options": {
                "A": "12.80%.",
                "B": "14.13%.",
                "C": "14.93%."
            },
            "answer": "B",
            "explanation": "Applying the expanded CAPM formula: $$r_e = R_f + (\\beta \\times \\text{ERP}) + \\text{CRP}$$ Substituting given values: $$R_f = 3.80\\%$$ $$\\beta \\times \\text{ERP} = 1.20 \\times 5.00\\% = 6.00\\%$$ $$\\text{CRP} = 4.33\\%$$ $$r_e = 3.80\\% + 6.00\\% + 4.33\\% = 14.133\\% \\approx 14.13\\%$$.",
            "distractor_analysis": {
                "A": "Omits the Country Risk Premium entirely: $3.80\\% + 6.00\\% = 9.80\\%$ or uses unadjusted sovereign spread $3.00\\% \\implies 12.80\\%$.",
                "C": "Multiplies beta by both ERP and CRP: $3.80\\% + 1.20 \\times (5.00\\% + 4.33\\%) = 3.80\\% + 11.20\\% = 15.00\\%$ (standard variant adds CRP separately as country risk is systematic to the location)."
            }
        },
        {
            "id": "L2-EQ-V16-Q3",
            "level": 2,
            "topic": "Equity Valuation",
            "subtopic": "Build-up Method for Cost of Equity",
            "vignette_id": "V16",
            "vignette_title": v16_title,
            "vignette_text": v16_text,
            "los": "Calculate the cost of equity using the build-up method.",
            "question": "Using the Build-up method, the estimated required return on equity for Andean Mining's domestic processing subsidiary is closest to:",
            "options": {
                "A": "12.50%.",
                "B": "14.00%.",
                "C": "15.20%."
            },
            "answer": "B",
            "explanation": "The Build-up method sums the risk-free rate and individual risk premia without using beta: $$r_e = R_f + \\text{ERP} + \\text{Size Premium} + \\text{Industry Premium} + \\text{Company-Specific Premium}$$ Substituting: $$r_e = 3.80\\% + 5.00\\% + 2.50\\% + 1.20\\% + 1.50\\% = 14.00\\%$$.",
            "distractor_analysis": {
                "A": "Omits the company-specific risk premium: $3.80\\% + 5.00\\% + 2.50\\% + 1.20\\% = 12.50\\%$.",
                "C": "Multiplies ERP by beta ($1.20$) within the build-up method, which is a conceptual error."
            }
        },
        {
            "id": "L2-EQ-V16-Q4",
            "level": 2,
            "topic": "Equity Valuation",
            "subtopic": "Pastor-Stambaugh Model & Liquidity Factor",
            "vignette_id": "V16",
            "vignette_title": v16_title,
            "vignette_text": v16_text,
            "los": "Explain the Pastor-Stambaugh model and the role of the liquidity premium.",
            "question": "The Pastor-Stambaugh model augments the Fama-French three-factor model by adding which of the following systematic factors?",
            "options": {
                "A": "A momentum factor measuring 12-month prior relative strength.",
                "B": "A liquidity factor measuring the sensitivity of stock returns to market-wide equity liquidity.",
                "C": "A currency exchange rate factor measuring exposure to foreign exchange fluctuations."
            },
            "answer": "B",
            "explanation": "The Pastor-Stambaugh model adds a fourth factor to the Fama-French model representing systematic liquidity risk. Stocks that have higher sensitivity to market-wide liquidity contractions are viewed as riskier by investors and require a higher expected return (liquidity premium).",
            "distractor_analysis": {
                "A": "A momentum factor is added in the Carhart four-factor model, not the Pastor-Stambaugh model.",
                "C": "Currency exchange risk is not the defining factor added in the Pastor-Stambaugh model."
            }
        },
        {
            "id": "L2-EQ-V16-Q5",
            "level": 2,
            "topic": "Equity Valuation",
            "subtopic": "Forward-Looking vs. Historical ERP Estimates",
            "vignette_id": "V16",
            "vignette_title": v16_title,
            "vignette_text": v16_text,
            "los": "Contrast forward-looking and historical estimates of the equity risk premium.",
            "question": "Which of the following approaches is classified as a forward-looking macroeconomic supply-side model for estimating the Equity Risk Premium (ERP)?",
            "options": {
                "A": "The Ibbotson-Chen model, which adjusts expected inflation, real GDP/earnings growth, and changes in P/E valuation multiples.",
                "B": "Calculating the historical arithmetic mean return of equity indices relative to government bonds over the past 80 years.",
                "C": "Using historical roll-yield on emerging market sovereign credit default swaps."
            },
            "answer": "A",
            "explanation": "The Ibbotson-Chen model is a supply-side macroeconomic model that estimates the forward-looking equity risk premium based on underlying economic drivers: expected inflation, real earnings per share growth (linked to real GDP growth), expected dividend yield, and expected changes in the P/E multiple. Supply-side models avoid the survivorship bias and non-stationarity of purely backward-looking historical series.",
            "distractor_analysis": {
                "B": "Historical mean estimation is a backward-looking historical approach, not a supply-side macroeconomic model.",
                "C": "CDS roll-yield measures credit risk premia, not an equity supply-side model."
            }
        }
    ]
    vignettes.append((v16_title, v16_text, v16_questions))

    # =========================================================================
    # Vignette 17: V17
    # =========================================================================
    v17_text = (
        "Solis Semiconductors (SS) is a fabless designer of high-performance artificial intelligence accelerators. "
        "Senior technology analyst Frank Richter is developing an integrated financial model to evaluate Solis's economic moat, "
        "Competitive Advantage Period (CAP), and the impact of inflation on cash flow forecasting.\n\n"
        "Baseline financial metrics for Solis Semiconductors (monetary values in millions of USD):\n"
        "- Net Operating Profit After Tax (NOPAT): 420.0 USD\n"
        "- Total Invested Capital (Total Assets minus Non-interest-bearing current liabilities): 2,800.0 USD\n"
        "- Weighted Average Cost of Capital (WACC): 9.00%\n"
        "- Forecasted revenue growth rate: 8.00%\n\n"
        "Frank evaluates Solis's Competitive Advantage Period (CAP): Solis currently generates an economic spread "
        "($\\text{ROIC} - \\text{WACC}$). However, as semiconductor patent exclusivity ages and global competitors invest in competing "
        "chip architectures, Solis's ROIC is modeled to fade linearly toward WACC over a 7-year Competitive Advantage Period.\n\n"
        "Additionally, Frank evaluates how unexpected inflation ($3.50\\%$) affects depreciation tax shields, FIFO versus LIFO inventory, "
        "and the consistency principle between nominal and real discount rates."
    )
    v17_title = "Solis Semiconductors: ROIC vs. WACC, Competitive Advantage Period, & Inflation Effects"

    v17_questions = [
        {
            "id": "L2-EQ-V17-Q1",
            "level": 2,
            "topic": "Equity Valuation",
            "subtopic": "ROIC and Economic Spread Calculation",
            "vignette_id": "V17",
            "vignette_title": v17_title,
            "vignette_text": v17_text,
            "los": "Calculate Return on Invested Capital (ROIC) and the economic spread.",
            "question": "Solis Semiconductors' Return on Invested Capital (ROIC) and its economic spread over WACC are closest to:",
            "options": {
                "A": "ROIC of 12.00%; Economic Spread of 3.00%.",
                "B": "ROIC of 15.00%; Economic Spread of 6.00%.",
                "C": "ROIC of 17.50%; Economic Spread of 8.50%."
            },
            "answer": "B",
            "explanation": "Step 1: Compute Return on Invested Capital (ROIC): $$\\text{ROIC} = \\frac{\\text{NOPAT}}{\\text{Total Invested Capital}} = \\frac{420.0\\text{ USD million}}{2,800.0\\text{ USD million}} = 0.1500 = 15.00\\%$$ Step 2: Compute Economic Spread: $$\\text{Economic Spread} = \\text{ROIC} - \\text{WACC} = 15.00\\% - 9.00\\% = 6.00\\%$$.",
            "distractor_analysis": {
                "A": "Divides by an assumed capital base of $3,500\\text{ USD million}$ ($420 / 3,500 = 12.00\\%$).",
                "C": "Uses $2,400\\text{ USD million}$ as capital base ($420 / 2,400 = 17.50\\%$)."
            }
        },
        {
            "id": "L2-EQ-V17-Q2",
            "level": 2,
            "topic": "Equity Valuation",
            "subtopic": "Value Creation and Growth Dynamics",
            "vignette_id": "V17",
            "vignette_title": v17_title,
            "vignette_text": v17_text,
            "los": "Explain how growth impacts shareholder value when ROIC exceeds, equals, or is less than WACC.",
            "question": "Which of the following best describes the relationship between company growth and shareholder value creation?",
            "options": {
                "A": "Growth always creates shareholder value regardless of ROIC because higher revenues increase future cash flow potential.",
                "B": "Growth creates shareholder value only when $\\text{ROIC} > \\text{WACC}$; if $\\text{ROIC} < \\text{WACC}$, growth destroys shareholder value by consuming capital at returns below the opportunity cost.",
                "C": "Growth is value-neutral when $\\text{ROIC} > \\text{WACC}$ and value-accretive when $\\text{ROIC} < \\text{WACC}$."
            },
            "answer": "B",
            "explanation": "Growth is not inherently value-creating. Growth creates shareholder value if and only if the return on newly invested capital exceeds the firm's cost of capital ($\\text{ROIC} > \\text{WACC}$). When a company invests at $\\text{ROIC} = \\text{WACC}$, growth is value-neutral. When $\\text{ROIC} < \\text{WACC}$, each incremental dollar invested destroys shareholder wealth, and faster growth accelerates wealth destruction.",
            "distractor_analysis": {
                "A": "Ignores the capital investment required to generate growth; unprofitable growth destroys value.",
                "C": "Directly inverts the economic principles of corporate finance."
            }
        },
        {
            "id": "L2-EQ-V17-Q3",
            "level": 2,
            "topic": "Equity Valuation",
            "subtopic": "Competitive Advantage Period (CAP) & Fade Rate",
            "vignette_id": "V17",
            "vignette_title": v17_title,
            "vignette_text": v17_text,
            "los": "Explain the Competitive Advantage Period (CAP) and the fade rate of excess returns.",
            "question": "In financial modeling, the Competitive Advantage Period (CAP) represents the time horizon during which:",
            "options": {
                "A": "A firm can generate returns on incremental invested capital in excess of its cost of capital (ROIC > WACC) before competitive forces eliminate economic rents.",
                "B": "A firm's stock price grows faster than the benchmark equity index.",
                "C": "A firm is legally protected from all patent infringement by regulatory authorities."
            },
            "answer": "A",
            "explanation": "The Competitive Advantage Period (CAP) is the expected period over which a company's economic moat allows it to maintain an economic spread ($\\text{ROIC} > \\text{WACC}$). In competitive microeconomic equilibrium, supernormal economic profits attract competitors and capital investment, driving industry prices and margins down until ROIC fades to WACC at the conclusion of the CAP.",
            "distractor_analysis": {
                "B": "CAP refers to corporate economic profitability (ROIC vs WACC), not market price outperformance.",
                "C": "Patents represent one possible barrier to entry, but CAP encompasses all competitive advantages and moat longevity."
            }
        },
        {
            "id": "L2-EQ-V17-Q4",
            "level": 2,
            "topic": "Equity Valuation",
            "subtopic": "Inflation Distortions on Financial Performance",
            "vignette_id": "V17",
            "vignette_title": v17_title,
            "vignette_text": v17_text,
            "los": "Evaluate the effects of inflation on financial statement line items and cash flow forecasting.",
            "question": "In an inflationary environment, which of the following accounting effects most severely depresses a company's real cash flow generation?",
            "options": {
                "A": "Depreciation expense based on historical cost erodes the real purchasing power of the depreciation tax shield.",
                "B": "LIFO inventory accounting understates ending inventory on the balance sheet.",
                "C": "Interest expense on fixed-rate debt increases in real terms."
            },
            "answer": "A",
            "explanation": "Depreciation tax shields are fixed based on historical nominal asset costs. As inflation accelerates, the replacement cost of capital assets escalates, but nominal tax-deductible depreciation remains locked at historical levels. This diminishes the real purchasing power of the depreciation tax shield and increases the firm's real effective tax burden, depressing real cash flows.",
            "distractor_analysis": {
                "B": "LIFO inventory accounting matches current higher costs against current revenue, which minimizes phantom inventory profits and preserves real cash flow by lowering income taxes.",
                "C": "Inflation benefits fixed-rate debt issuers because debt is serviced with depreciated currency, reducing the real burden of debt."
            }
        },
        {
            "id": "L2-EQ-V17-Q5",
            "level": 2,
            "topic": "Equity Valuation",
            "subtopic": "Consistency Principle: Nominal vs. Real Cash Flows",
            "vignette_id": "V17",
            "vignette_title": v17_title,
            "vignette_text": v17_text,
            "los": "Explain the consistency principle in applying nominal versus real discount rates and cash flows.",
            "question": "When valuing a company using discounted cash flow models under inflation, the consistency principle requires that:",
            "options": {
                "A": "Nominal cash flows must be discounted at a nominal discount rate, and real cash flows must be discounted at a real discount rate.",
                "B": "Nominal cash flows should be discounted at a real discount rate to remove inflation distortions.",
                "C": "The real discount rate must equal the nominal discount rate plus the expected inflation rate."
            },
            "answer": "A",
            "explanation": "The consistency principle is fundamental to valuation: cash flows and discount rates must match in terms of inflation treatment. Nominal cash flows (which reflect expected inflation) must be discounted at a nominal discount rate $(1 + r_{\\text{nominal}})$, whereas real cash flows (which exclude inflation) must be discounted at a real discount rate $(1 + r_{\\text{real}})$, related by the Fisher equation: $(1 + r_{\\text{nominal}}) = (1 + r_{\\text{real}})(1 + \\pi)$. Mixing nominal cash flows with a real discount rate drastically overstates intrinsic value.",
            "distractor_analysis": {
                "B": "Discounting nominal cash flows at a real discount rate double counts inflation and artificially inflates valuation.",
                "C": "The real rate equals the nominal rate divided by $(1 + \\pi)$, not plus inflation."
            }
        }
    ]
    vignettes.append((v17_title, v17_text, v17_questions))

    return vignettes

def build_all_questions():
    vignettes_data = get_vignettes()
    all_questions = []

    for v_title, v_text, q_list in vignettes_data:
        for q in q_list:
            all_questions.append(q)

    return all_questions

def validate_questions(questions):
    assert len(questions) == 85, f"Expected 85 questions, got {len(questions)}"
    vignette_ids = set()
    for q in questions:
        vignette_ids.add(q["vignette_id"])
    assert len(vignette_ids) == 17, f"Expected 17 vignettes, got {len(vignette_ids)}"

    # Check question counts per vignette
    from collections import Counter
    counts = Counter(q["vignette_id"] for q in questions)
    for v_id, cnt in counts.items():
        assert cnt == 5, f"Vignette {v_id} has {cnt} questions, expected exactly 5"

    # Currency and Math delimiter validation
    def check_text(text, ctx):
        # 1. Check balanced display math $$ ... $$
        t_no_display = re.sub(r'\$\$.*?\$\$', ' [DISPLAY_MATH] ', text, flags=re.DOTALL)
        
        # 2. Extract inline math blocks
        inline_blocks = re.findall(r'(?<!\\)\$([^\$]+?)(?<!\\)\$', t_no_display)
        for block in inline_blocks:
            if '$' in block:
                raise ValueError(f"Nested/stray '$' in math block in {ctx}: '{block}'")
        
        # 3. Remove inline math
        t_no_math = re.sub(r'(?<!\\)\$[^\$]+?(?<!\\)\$', ' [INLINE_MATH] ', t_no_display)
        
        # 4. In remaining text (prose), there must be NO unescaped '$'
        stray_dollars = re.findall(r'(?<!\\)\$', t_no_math)
        if stray_dollars:
            raise ValueError(f"Stray unescaped '$' found in {ctx}: '{t_no_math}'")

    for q in questions:
        for field in ["question", "explanation", "vignette_text"]:
            check_text(q[field], f"{q['id']} field '{field}'")
        
        for opt_key, opt_text in q["options"].items():
            check_text(opt_text, f"{q['id']} option {opt_key}")
        
        for dist_key, dist_text in q["distractor_analysis"].items():
            check_text(dist_text, f"{q['id']} distractor {dist_key}")

    print(f"Validation successful: Exactly {len(questions)} questions across {len(vignette_ids)} vignettes.")
    print("Currency check passed: Zero unescaped '$' currency symbols detected.")

def main():
    questions = build_all_questions()
    validate_questions(questions)

    output_path = Path("data/fi_eq/l2_equity.json")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(questions, f, indent=2, ensure_ascii=False)

    print(f"Successfully generated and wrote {len(questions)} questions to {output_path.resolve()}")

if __name__ == "__main__":
    main()
