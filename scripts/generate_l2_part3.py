import json
import os
import re

def create_part3_questions():
    questions = []

    # =========================================================================
    # VIGNETTE 31: Beneish M-Score and Earnings Manipulation Detection (5 Questions)
    # Module: m17-quality-l2
    # Topic: Evaluating Quality of Financial Reports
    # =========================================================================
    v31_id = "V31"
    v31_title = "Beneish M-Score and Earnings Manipulation Detection at Nexa Systems"
    v31_text = (
        "Nexa Systems, Inc. is a publicly traded designer and manufacturer of enterprise communication "
        "hardware and cloud networking infrastructure. Sarah Chen, CFA, an equity research analyst at "
        "Highland Asset Management, is conducting a forensic accounting review of Nexa Systems following "
        "a period of rapid revenue growth and rising non-current assets. Chen suspects that management may "
        "be utilizing aggressive accounting choices or earnings manipulation to meet consensus earnings targets.\n\n"
        "Chen compiles the financial statement data for Nexa Systems for Fiscal Year 2023 (Year t-1) and "
        "Fiscal Year 2024 (Year t) presented in Exhibit 1.\n\n"
        "Exhibit 1: Nexa Systems Financial Statement Excerpts (in millions of USD)\n"
        "- Revenues: Year t-1 = 1,200; Year t = 1,500\n"
        "- Cost of Goods Sold: Year t-1 = 720; Year t = 975\n"
        "- Gross Profit: Year t-1 = 480; Year t = 525\n"
        "- Accounts Receivable: Year t-1 = 150; Year t = 250\n"
        "- Selling, General, and Administrative (SG&A) Expenses: Year t-1 = 180; Year t = 240\n"
        "- Depreciation Expense: Year t-1 = 100; Year t = 95\n"
        "- Gross Property, Plant, and Equipment (PP&E): Year t-1 = 1,500; Year t = 1,900\n"
        "- Net PP&E: Year t-1 = 1,000; Year t = 1,150\n"
        "- Current Assets: Year t-1 = 700; Year t = 850\n"
        "- Non-Current Assets (excluding Net PP&E): Year t-1 = 300; Year t = 600\n"
        "- Total Assets: Year t-1 = 2,000; Year t = 2,600\n"
        "- Long-Term Debt and Current Portion of Debt: Year t-1 = 600; Year t = 910\n"
        "- Net Income: Year t = 160\n"
        "- Cash Flow from Operating Activities (CFO): Year t = 56\n\n"
        "Chen uses the 8-variable Beneish M-Score model to evaluate the probability of earnings manipulation:\n"
        "$$\\text{M-Score} = -4.84 + 0.920 \\times \\text{DSRI} + 0.528 \\times \\text{GMI} + 0.404 \\times \\text{AQI} + 0.892 \\times \\text{SGI} + 0.115 \\times \\text{DEPI} - 0.172 \\times \\text{SGAI} + 4.037 \\times \\text{TATA} + 0.0327 \\times \\text{LVGI}$$\n"
        "The standard benchmark cutoff is -1.78. An M-score greater than -1.78 (i.e., less negative) indicates a higher probability of earnings manipulation."
    )

    questions.append({
        "id": "L2-V31-Q1",
        "level": 2,
        "module": "m17-quality-l2",
        "topic": "Evaluating Quality of Financial Reports",
        "vignette_id": v31_id,
        "vignette_title": v31_title,
        "vignette_text": v31_text,
        "los": "Describe the Beneish model, calculate its component ratios, and evaluate financial reporting quality.",
        "question": "Based on Exhibit 1, Nexa Systems' Days Sales in Receivables Index (DSRI) is closest to:",
        "options": {
            "A": "0.833",
            "B": "1.125",
            "C": "1.333"
        },
        "answer": "C",
        "explanation": (
            "Step 1: Compute Days Sales in Receivables for Year t and Year t-1 relative to sales:\n"
            "$$\\text{DSRI} = \\frac{\\text{Receivables}_t / \\text{Sales}_t}{\\text{Receivables}_{t-1} / \\text{Sales}_{t-1}}$$\n"
            "For Year t: $\\frac{250}{1500} = 0.1667$.\n"
            "For Year t-1: $\\frac{150}{1200} = 0.1250$.\n"
            "Step 2: Calculate DSRI:\n"
            "$$\\text{DSRI} = \\frac{0.1667}{0.1250} = 1.333$$\n"
            "A DSRI of 1.333 is substantially greater than 1.0, indicating that receivables grew 33.3% faster than sales. "
            "This suggests aggressive revenue recognition policies (e.g., channel stuffing or unearned revenue acceleration) "
            "or deteriorating customer credit quality."
        )
    })

    questions.append({
        "id": "L2-V31-Q2",
        "level": 2,
        "module": "m17-quality-l2",
        "topic": "Evaluating Quality of Financial Reports",
        "vignette_id": v31_id,
        "vignette_title": v31_title,
        "vignette_text": v31_text,
        "los": "Describe the Beneish model, calculate its component ratios, and evaluate financial reporting quality.",
        "question": "Which of the following best describes the Asset Quality Index (AQI) calculation for Nexa Systems and its implication for financial reporting quality?",
        "options": {
            "A": "AQI is 0.650, indicating conservative accounting and a shrinking intangible asset base.",
            "B": "AQI is 1.538, indicating an increasing proportion of capitalized expenses or intangible assets, which lowers earnings quality.",
            "C": "AQI is 1.250, indicating that non-current assets are growing in line with revenues."
        },
        "answer": "B",
        "explanation": (
            "Step 1: Define Asset Quality (AQ) as the ratio of non-current assets other than PP&E to total assets:\n"
            "$$\\text{AQ} = 1 - \\frac{\\text{Current Assets} + \\text{Net PP&E}}{\\text{Total Assets}} = \\frac{\\text{Non-Current Assets excluding PP&E}}{\\text{Total Assets}}$$\n"
            "For Year t-1: $\\text{AQ}_{t-1} = \\frac{300}{2000} = 0.1500$.\n"
            "For Year t: $\\text{AQ}_t = \\frac{600}{2600} = 0.2308$.\n"
            "Step 2: Calculate AQI:\n"
            "$$\\text{AQI} = \\frac{\\text{AQ}_t}{\\text{AQ}_{t-1}} = \\frac{0.2308}{0.1500} = 1.538$$\n"
            "An AQI of 1.538 is significantly greater than 1.0, indicating that Nexa's proportion of non-traditional assets "
            "(such as deferred charges, capitalized development costs, or intangibles) jumped by 53.8%. This is a classic indicator "
            "that the company may be capitalizing operating costs to defer expense recognition and artificially inflate reported net income."
        )
    })

    questions.append({
        "id": "L2-V31-Q3",
        "level": 2,
        "module": "m17-quality-l2",
        "topic": "Evaluating Quality of Financial Reports",
        "vignette_id": v31_id,
        "vignette_title": v31_title,
        "vignette_text": v31_text,
        "los": "Describe the Beneish model, calculate its component ratios, and evaluate financial reporting quality.",
        "question": "Using Exhibit 1 and Chen's 8-variable Beneish model, Nexa Systems' M-Score and the appropriate conclusion regarding manipulation are closest to:",
        "options": {
            "A": "M-Score = -2.145, indicating a low probability of earnings manipulation.",
            "B": "M-Score = -1.106, indicating a high probability of earnings manipulation.",
            "C": "M-Score = +0.892, indicating a low probability of earnings manipulation."
        },
        "answer": "B",
        "explanation": (
            "Step 1: Calculate the 8 Beneish component variables:\n"
            "- $\\text{DSRI} = \\frac{250/1500}{150/1200} = 1.333$\n"
            "- $\\text{GMI} = \\frac{\\text{Gross Margin}_{t-1}}{\\text{Gross Margin}_t} = \\frac{480/1200}{525/1500} = \\frac{0.400}{0.350} = 1.143$\n"
            "- $\\text{AQI} = \\frac{600/2600}{300/2000} = \\frac{0.2308}{0.1500} = 1.538$\n"
            "- $\\text{SGI} = \\frac{1500}{1200} = 1.250$\n"
            "- $\\text{DEPI} = \\frac{100/1500}{95/1900} = \\frac{0.0667}{0.0500} = 1.333$\n"
            "- $\\text{SGAI} = \\frac{240/1500}{180/1200} = \\frac{0.1600}{0.1500} = 1.067$\n"
            "- $\\text{LVGI} = \\frac{910/2600}{600/2000} = \\frac{0.3500}{0.3000} = 1.167$\n"
            "- $\\text{TATA} = \\frac{\\text{Net Income} - \\text{CFO}}{\\text{Total Assets}_t} = \\frac{160 - 56}{2600} = \\frac{104}{2600} = 0.0400$\n\n"
            "Step 2: Plug into the Beneish equation:\n"
            "$$\\text{M-Score} = -4.84 + 0.920(1.333) + 0.528(1.143) + 0.404(1.538) + 0.892(1.250) + 0.115(1.333) - 0.172(1.067) + 4.037(0.040) + 0.0327(1.167)$$\n"
            "$$\\text{M-Score} = -4.84 + 1.226 + 0.604 + 0.621 + 1.115 + 0.153 - 0.184 + 0.161 + 0.038 = -1.106$$\n"
            "Conclusion: Because -1.106 is greater than the standard cutoff of -1.78 (i.e., less negative), the Beneish model indicates a high probability of earnings manipulation."
        )
    })

    questions.append({
        "id": "L2-V31-Q4",
        "level": 2,
        "module": "m17-quality-l2",
        "topic": "Evaluating Quality of Financial Reports",
        "vignette_id": v31_id,
        "vignette_title": v31_title,
        "vignette_text": v31_text,
        "los": "Describe the Beneish model and interpret its individual component ratios.",
        "question": "When interpreting the Depreciation Index (DEPI = 1.333) and Gross Margin Index (GMI = 1.143), Chen should conclude that:",
        "options": {
            "A": "GMI > 1 indicates expanding profitability, reducing pressure to manipulate, while DEPI > 1 reflects accelerated depreciation.",
            "B": "DEPI > 1 indicates a faster depreciation schedule that understates current net income.",
            "C": "GMI > 1 signals deteriorating profit margins, creating incentives to manipulate, while DEPI > 1 indicates a slowing depreciation rate that boosts reported profits."
        },
        "answer": "C",
        "explanation": (
            "Under the Beneish model framework:\n"
            "1. $\\text{GMI} = \\frac{\\text{Gross Margin}_{t-1}}{\\text{Gross Margin}_t}$. When GMI > 1, gross margins have contracted (from 40.0% to 35.0%). "
            "Deteriorating gross margins put pressure on management to engage in aggressive accounting practices to sustain headline earnings growth.\n"
            "2. $\\text{DEPI} = \\frac{\\text{Depreciation Rate}_{t-1}}{\\text{Depreciation Rate}_t}$. When DEPI > 1, the current depreciation rate has declined "
            "(from 6.67% to 5.00%). Slower depreciation implies that management may have extended the estimated useful lives of existing PP&E or "
            "adopted more aggressive depreciation methods to lower current depreciation expense, thereby artificially inflating operating profit."
        )
    })

    questions.append({
        "id": "L2-V31-Q5",
        "level": 2,
        "module": "m17-quality-l2",
        "topic": "Evaluating Quality of Financial Reports",
        "vignette_id": v31_id,
        "vignette_title": v31_title,
        "vignette_text": v31_text,
        "los": "Explain the limitations of models used to evaluate financial reporting quality.",
        "question": "Regarding the inherent limitations of the Beneish M-Score model in forensic analysis, Chen would be most accurate in stating that:",
        "options": {
            "A": "The model is a definitive deterministic proof of financial statement fraud.",
            "B": "The model is a probabilistic empirical screen that may yield false positives, and management can deliberately game individual metrics once the screen is known.",
            "C": "The model cannot be used on firms that generate positive operating cash flows."
        },
        "answer": "B",
        "explanation": (
            "The Beneish M-Score is an empirical probit model estimated from historical samples of known manipulators versus non-manipulators. "
            "Key limitations include:\n"
            "1. It is a probabilistic screening tool, not a legal or deterministic proof of fraud. An M-score above -1.78 flags high risk, but does not prove intentional manipulation.\n"
            "2. It is subject to Type I errors (false positives: classifying rapidly growing, legitimate companies as manipulators) and Type II errors (false negatives: missing sophisticated manipulators).\n"
            "3. If corporate executives know they are being evaluated against the 8 Beneish ratios, they may strategically manipulate other accounting lines that are not captured or weighted heavily by the model."
        )
    })

    # =========================================================================
    # VIGNETTE 32: Accrual Models: Balance Sheet vs. Cash Flow Accruals Ratios (5 Questions)
    # Module: m17-quality-l2
    # Topic: Evaluating Quality of Financial Reports
    # =========================================================================
    v32_id = "V32"
    v32_title = "Accrual Models and Earnings Quality: MedEquip Global vs. BioPharm Instruments"
    v32_text = (
        "David Rossi, CFA, is a senior healthcare equity analyst at Alpine Capital. Rossi is conducting a comparative "
        "earnings quality analysis of two medical equipment manufacturers: MedEquip Global and BioPharm Instruments. Both "
        "companies operate in the same sub-industry and reported an identical net income of 120 million EUR for the fiscal "
        "year ended 2024 (Year t). However, Rossi notes substantial differences in the working capital dynamics, asset growth, "
        "and cash flow profiles of the two firms.\n\n"
        "Rossi compiles the financial data for both companies presented in Exhibit 1 and Exhibit 2.\n\n"
        "Exhibit 1: MedEquip Global Financial Summary (in millions of EUR)\n"
        "- Year t-1:\n"
        "  - Total Assets = 1,000\n"
        "  - Cash, Cash Equivalents, and Short-Term Marketable Securities = 120\n"
        "  - Total Liabilities = 450\n"
        "  - Total Financial Debt (Short-Term and Long-Term Borrowings) = 200\n"
        "- Year t:\n"
        "  - Total Assets = 1,220\n"
        "  - Cash, Cash Equivalents, and Short-Term Marketable Securities = 80\n"
        "  - Total Liabilities = 480\n"
        "  - Total Financial Debt (Short-Term and Long-Term Borrowings) = 200\n"
        "  - Net Income = 120\n"
        "  - Cash Flow from Operating Activities (CFO) = 30\n"
        "  - Cash Flow from Investing Activities (CFI) = -120\n\n"
        "Exhibit 2: BioPharm Instruments Financial Summary (in millions of EUR)\n"
        "- Year t-1: Net Operating Assets (NOA) = 700\n"
        "- Year t: Net Operating Assets (NOA) = 735\n"
        "- Year t Net Income = 120\n"
        "- Year t Cash Flow from Operating Activities (CFO) = 135\n"
        "- Year t Cash Flow from Investing Activities (CFI) = -25\n\n"
        "Rossi applies accrual accounting models to evaluate the persistence and quality of reported net income for both firms."
    )

    questions.append({
        "id": "L2-V32-Q1",
        "level": 2,
        "module": "m17-quality-l2",
        "topic": "Evaluating Quality of Financial Reports",
        "vignette_id": v32_id,
        "vignette_title": v32_title,
        "vignette_text": v32_text,
        "los": "Describe and calculate balance sheet-based and cash flow-based accruals ratios, and evaluate earnings quality.",
        "question": "Based on Exhibit 1, MedEquip Global's Net Operating Assets (NOA) for Year t and Balance Sheet Accruals for Year t are closest to:",
        "options": {
            "A": "NOA = 860 million EUR; Balance Sheet Accruals = 230 million EUR",
            "B": "NOA = 740 million EUR; Balance Sheet Accruals = 110 million EUR",
            "C": "NOA = 1,140 million EUR; Balance Sheet Accruals = 140 million EUR"
        },
        "answer": "A",
        "explanation": (
            "Step 1: Calculate Net Operating Assets (NOA) as Operating Assets minus Operating Liabilities:\n"
            "$$\\text{Operating Assets} = \\text{Total Assets} - \\text{Cash and Short-Term Marketable Securities}$$\n"
            "$$\\text{Operating Liabilities} = \\text{Total Liabilities} - \\text{Total Debt}$$\n"
            "$$\\text{NOA} = \\text{Operating Assets} - \\text{Operating Liabilities}$$\n\n"
            "For Year t-1:\n"
            "$\\text{Operating Assets}_{t-1} = 1000 - 120 = 880\\text{ million EUR}$\n"
            "$\\text{Operating Liabilities}_{t-1} = 450 - 200 = 250\\text{ million EUR}$\n"
            "$\\text{NOA}_{t-1} = 880 - 250 = 630\\text{ million EUR}$\n\n"
            "For Year t:\n"
            "$\\text{Operating Assets}_t = 1220 - 80 = 1140\\text{ million EUR}$\n"
            "$\\text{Operating Liabilities}_t = 480 - 200 = 280\\text{ million EUR}$\n"
            "$\\text{NOA}_t = 1140 - 280 = 860\\text{ million EUR}$\n\n"
            "Step 2: Calculate Balance Sheet Accruals:\n"
            "$$\\text{Accruals}_{BS} = \\text{NOA}_t - \\text{NOA}_{t-1} = 860 - 630 = 230\\text{ million EUR}$$"
        )
    })

    questions.append({
        "id": "L2-V32-Q2",
        "level": 2,
        "module": "m17-quality-l2",
        "topic": "Evaluating Quality of Financial Reports",
        "vignette_id": v32_id,
        "vignette_title": v32_title,
        "vignette_text": v32_text,
        "los": "Describe and calculate balance sheet-based and cash flow-based accruals ratios, and evaluate earnings quality.",
        "question": "MedEquip Global's Balance Sheet Accruals Ratio for Year t and the resulting assessment of its earnings quality relative to BioPharm Instruments are:",
        "options": {
            "A": "Accruals Ratio = +18.9%; MedEquip has higher earnings quality than BioPharm.",
            "B": "Accruals Ratio = +30.9%; MedEquip has lower earnings quality than BioPharm.",
            "C": "Accruals Ratio = +26.7%; MedEquip and BioPharm have equivalent earnings quality."
        },
        "answer": "B",
        "explanation": (
            "Step 1: Compute Average Net Operating Assets for MedEquip Global:\n"
            "$$\\text{Average NOA}_{\\text{MedEquip}} = \\frac{\\text{NOA}_t + \\text{NOA}_{t-1}}{2} = \\frac{860 + 630}{2} = 745\\text{ million EUR}$$\n"
            "Step 2: Calculate MedEquip's Balance Sheet Accruals Ratio:\n"
            "$$\\text{BS Accruals Ratio}_{\\text{MedEquip}} = \\frac{\\Delta \\text{NOA}}{\\text{Average NOA}} = \\frac{230}{745} = +30.87\\% \\approx +30.9\\%$$\n\n"
            "Step 3: Calculate BioPharm Instruments' Balance Sheet Accruals Ratio:\n"
            "$$\\text{Average NOA}_{\\text{BioPharm}} = \\frac{735 + 700}{2} = 717.5\\text{ million EUR}$$\n"
            "$$\\Delta \\text{NOA}_{\\text{BioPharm}} = 735 - 700 = 35\\text{ million EUR}$$\n"
            "$$\\text{BS Accruals Ratio}_{\\text{BioPharm}} = \\frac{35}{717.5} = +4.88\\% \\approx +4.9\\%$$\n\n"
            "Conclusion: A lower accruals ratio indicates that earnings are backed by cash flows rather than growth in net operating accruals. "
            "MedEquip's accruals ratio (+30.9%) is dramatically higher than BioPharm's (+4.9%), indicating MedEquip has substantially lower earnings quality."
        )
    })

    questions.append({
        "id": "L2-V32-Q3",
        "level": 2,
        "module": "m17-quality-l2",
        "topic": "Evaluating Quality of Financial Reports",
        "vignette_id": v32_id,
        "vignette_title": v32_title,
        "vignette_text": v32_text,
        "los": "Describe and calculate balance sheet-based and cash flow-based accruals ratios, and evaluate earnings quality.",
        "question": "Based on Exhibit 2, BioPharm Instruments' Cash Flow Accruals and Cash Flow Accruals Ratio for Year t are closest to:",
        "options": {
            "A": "Cash Flow Accruals = 10 million EUR; Accruals Ratio = +1.39%",
            "B": "Cash Flow Accruals = -15 million EUR; Accruals Ratio = -2.09%",
            "C": "Cash Flow Accruals = 40 million EUR; Accruals Ratio = +5.57%"
        },
        "answer": "A",
        "explanation": (
            "Step 1: Calculate Cash Flow Accruals using the cash flow statement definition:\n"
            "$$\\text{Accruals}_{CF} = \\text{Net Income} - (\\text{CFO} + \\text{CFI})$$\n"
            "For BioPharm Instruments in Year t:\n"
            "$\\text{Net Income} = 120\\text{ million EUR}$\n"
            "$\\text{CFO} = 135\\text{ million EUR}$\n"
            "$\\text{CFI} = -25\\text{ million EUR}$\n"
            "$$\\text{Accruals}_{CF} = 120 - (135 + (-25)) = 120 - 110 = 10\\text{ million EUR}$$\n\n"
            "Step 2: Calculate Cash Flow Accruals Ratio using Average NOA (717.5 million EUR):\n"
            "$$\\text{CF Accruals Ratio} = \\frac{\\text{Accruals}_{CF}}{\\text{Average NOA}} = \\frac{10}{717.5} = +1.39\\%$$\n"
            "A ratio of +1.39% demonstrates that almost all of BioPharm's net income is confirmed by cash flow generation, reflecting excellent earnings quality."
        )
    })

    questions.append({
        "id": "L2-V32-Q4",
        "level": 2,
        "module": "m17-quality-l2",
        "topic": "Evaluating Quality of Financial Reports",
        "vignette_id": v32_id,
        "vignette_title": v32_title,
        "vignette_text": v32_text,
        "los": "Explain the causes of differences between balance sheet-based and cash flow-based accruals measures.",
        "question": "Rossi notes that for MedEquip Global, Balance Sheet Accruals are 230 million EUR, whereas Cash Flow Accruals are 210 million EUR. Which of the following factors is most likely to cause a divergence between balance sheet and cash flow accruals?",
        "options": {
            "A": "Straight-line depreciation versus accelerated depreciation on domestic equipment.",
            "B": "Business acquisitions and foreign currency translation adjustments.",
            "C": "Payment of cash dividends to common equity holders."
        },
        "answer": "B",
        "explanation": (
            "The balance sheet accruals measure ($\\Delta\\text{NOA}$) and cash flow accruals measure ($\\text{Net Income} - (\\text{CFO} + \\text{CFI})$) "
            "will diverge due to non-operating and non-transactional accounting changes. The two primary drivers are:\n"
            "1. Mergers, acquisitions, and divestitures: Acquired operating assets and liabilities are recorded on the balance sheet at fair value without "
            "flowing through individual operating working capital accounts in CFO or CFI.\n"
            "2. Foreign currency translation gains/losses: Exchange rate movements directly revalue foreign subsidiary balance sheet assets and liabilities "
            "through other comprehensive income (OCI), changing NOA without flowing through CFO/CFI.\n"
            "Depreciation affects both measures symmetrically, and cash dividends affect financing cash flow and equity, not NOA or CFO/CFI."
        )
    })

    questions.append({
        "id": "L2-V32-Q5",
        "level": 2,
        "module": "m17-quality-l2",
        "topic": "Evaluating Quality of Financial Reports",
        "vignette_id": v32_id,
        "vignette_title": v32_title,
        "vignette_text": v32_text,
        "los": "Evaluate the implications of accruals for future earnings persistence and equity returns.",
        "question": "Empirical research on the accrual anomaly indicates that over the next 1-3 years, MedEquip Global's return on equity (ROE) is most likely to:",
        "options": {
            "A": "Outperform industry peers because aggressive accruals reflect high reinvestment in productive operating assets.",
            "B": "Mean-revert downward more quickly than BioPharm's ROE due to the low persistence of the accrual component of earnings.",
            "C": "Persist at current levels because accounting accruals provide identical forward predictive power as cash flows."
        },
        "answer": "B",
        "explanation": (
            "Empirical accounting research (e.g., Sloan 1996) demonstrates that net income driven primarily by accruals has significantly lower "
            "persistence than earnings driven by cash flows. Companies with large positive accruals (such as MedEquip, whose accruals ratio is +30.9%) "
            "frequently experience downward mean reversion in subsequent periods. As temporary accounting accruals reverse or prove uncollectible, "
            "future earnings, margins, and ROE deteriorate, often leading to negative earnings surprises and lower equity returns compared to high-cash-quality peers like BioPharm."
        )
    })

    # =========================================================================
    # VIGNETTE 33: Revenue Recognition Quality, Channel Stuffing, Reserve Manipulation (5 Questions)
    # Module: m17-quality-l2
    # Topic: Evaluating Quality of Financial Reports
    # =========================================================================
    v33_id = "V33"
    v33_title = "Revenue Recognition Quality, Channel Stuffing, and Reserve Manipulation at CloudStream Corporation"
    v33_text = (
        "Maya Lin, CFA, is a technology equity analyst investigating CloudStream Corporation, a rapid-growth provider of "
        "cloud data storage platforms and optical networking hardware. CloudStream's management has met or beaten Wall Street "
        "revenue forecasts for eight consecutive quarters. However, Lin has observed several accounting anomalies across "
        "CloudStream's quarterly filings for the fiscal year 2024.\n\n"
        "Lin compiles the quarterly data shown in Exhibit 1.\n\n"
        "Exhibit 1: CloudStream Corporation Quarterly Operational Data (in millions of USD)\n"
        "- Revenues: Q1 = 300; Q2 = 330; Q3 = 380; Q4 = 490\n"
        "- Days Sales Outstanding (DSO): Q1 = 45 days; Q2 = 52 days; Q3 = 68 days; Q4 = 92 days\n"
        "- Deferred (Unearned) Revenue Balance: Q1 = 180; Q2 = 165; Q3 = 135; Q4 = 95\n"
        "- Gross Accounts Receivable: Q1 = 150; Q2 = 191; Q3 = 287; Q4 = 501\n"
        "- Allowance for Credit Losses (Doubtful Accounts): Q1 = 6.3; Q2 = 7.5; Q3 = 8.9; Q4 = 10.0\n"
        "- Allowance as % of Gross Accounts Receivable: Q1 = 4.2%; Q2 = 3.9%; Q3 = 3.1%; Q4 = 2.0%\n\n"
        "Footnote disclosures in the Q4 report reveal:\n"
        "1. In the final two weeks of Q4, CloudStream booked 45 million USD of revenue under 'bill-and-hold' arrangements with "
        "three distributors. The equipment was moved to a leased warehouse controlled by CloudStream, with scheduled customer delivery "
        "in Q2 of the subsequent year. CloudStream initiated the arrangement to meet internal shipping quotas.\n"
        "2. CloudStream granted its largest distributor 180-day extended payment terms (versus normal 30-day terms) along with an "
        "explicit right of full return if the hardware remains unsold after six months.\n"
        "3. During Q4, CloudStream entered into an agreement with a hardware vendor, Titan Systems, purchasing 25 million USD of data "
        "center management software while simultaneously selling 25 million USD of consulting and integration services to Titan Systems."
    )

    questions.append({
        "id": "L2-V33-Q1",
        "level": 2,
        "module": "m17-quality-l2",
        "topic": "Evaluating Quality of Financial Reports",
        "vignette_id": v33_id,
        "vignette_title": v33_title,
        "vignette_text": v33_text,
        "los": "Explain earnings quality red flags, evaluate revenue recognition practices, and assess accounting warning signs.",
        "question": "Under IFRS 15 / ASC 606, CloudStream's recognition of 45 million USD in revenue for the Q4 'bill-and-hold' transactions is most likely:",
        "options": {
            "A": "Compliant, provided the hardware has been specifically identified and segregated in CloudStream's leased warehouse.",
            "B": "Inappropriate, because the buyer did not request the arrangement for a substantive business purpose and control has not transferred.",
            "C": "Compliant, because CloudStream holds physical possession and retains risk of loss during storage."
        },
        "answer": "B",
        "explanation": (
            "Under IFRS 15 and ASC 606, revenue cannot be recognized in a bill-and-hold arrangement unless all of the following criteria are met:\n"
            "1. The reason for the bill-and-hold arrangement must be substantive (i.e., requested explicitly by the customer for its own business needs, such as lack of warehouse space).\n"
            "2. The product must be identified separately as belonging to the customer.\n"
            "3. The product must currently be ready for physical transfer to the customer.\n"
            "4. The seller cannot have the ability to use the product or direct it to another customer.\n"
            "Because CloudStream initiated the bill-and-hold transaction to meet its own internal shipping quotas rather than fulfilling a customer request, "
            "control of the asset did not pass to the customer. Recognizing 45 million USD in Q4 violates revenue recognition criteria and represents premature revenue inflation."
        )
    })

    questions.append({
        "id": "L2-V33-Q2",
        "level": 2,
        "module": "m17-quality-l2",
        "topic": "Evaluating Quality of Financial Reports",
        "vignette_id": v33_id,
        "vignette_title": v33_title,
        "vignette_text": v33_text,
        "los": "Explain earnings quality red flags, evaluate revenue recognition practices, and assess accounting warning signs.",
        "question": "Lin analyzes the relationship between CloudStream's accelerating revenues and declining deferred revenue balances. The most appropriate interpretation of this trend is that CloudStream:",
        "options": {
            "A": "Is experiencing growing customer billings and expanding unearned deposits.",
            "B": "Is depleting its deferred revenue backlog to bolster current period recognized revenue, creating an unsustainable driver of top-line growth.",
            "C": "Has transitioned to cash-on-delivery payment terms with its recurring software customers."
        },
        "answer": "B",
        "explanation": (
            "Deferred (unearned) revenue represents upfront cash collections for services to be delivered over future periods. "
            "When reported revenue accelerates rapidly (from 300 million USD in Q1 to 490 million USD in Q4) while deferred revenue collapses "
            "(from 180 million USD in Q1 down to 95 million USD in Q4), it indicates that current revenue growth is being driven by exhausting the "
            "existing deferred revenue reserve rather than originating new customer contracts. Because unearned revenue cannot be drawn down indefinitely, "
            "this practice borrows revenue from the future and creates a severe revenue growth headwind once the backlog is depleted."
        )
    })

    questions.append({
        "id": "L2-V33-Q3",
        "level": 2,
        "module": "m17-quality-l2",
        "topic": "Evaluating Quality of Financial Reports",
        "vignette_id": v33_id,
        "vignette_title": v33_title,
        "vignette_text": v33_text,
        "los": "Evaluate the financial reporting quality of a company by analyzing accounting choices and estimates.",
        "question": "CloudStream's allowance for credit losses dropped from 4.2% of gross accounts receivable in Q1 to 2.0% in Q4. If CloudStream had maintained the 4.2% allowance ratio in Q4, Q4 operating income would have been:",
        "options": {
            "A": "11.0 million USD lower.",
            "B": "21.0 million USD lower.",
            "C": "10.0 million USD higher."
        },
        "answer": "A",
        "explanation": (
            "Step 1: Compute required allowance at 4.2% on Q4 Gross Accounts Receivable of 501 million USD:\n"
            "$$\\text{Required Allowance} = 4.2\\% \\times 501\\text{ million USD} = 21.042\\text{ million USD}$$\n"
            "Step 2: Compare to the reported Q4 allowance:\n"
            "$$\\text{Reported Allowance} = 10.0\\text{ million USD}$$\n"
            "$$\\text{Shortfall in Bad Debt Provision} = 21.042 - 10.0 = 11.042\\text{ million USD} \\approx 11.0\\text{ million USD}$$\n"
            "Step 3: Evaluate operating income effect:\n"
            "By allowing the allowance percentage to decline from 4.2% to 2.0% even while receivables surged and DSO deteriorated from 45 to 92 days, "
            "CloudStream under-accrued bad debt expense by 11.0 million USD, artificially inflating Q4 operating income by 11.0 million USD."
        )
    })

    questions.append({
        "id": "L2-V33-Q4",
        "level": 2,
        "module": "m17-quality-l2",
        "topic": "Evaluating Quality of Financial Reports",
        "vignette_id": v33_id,
        "vignette_title": v33_title,
        "vignette_text": v33_text,
        "los": "Explain earnings quality red flags, evaluate revenue recognition practices, and assess accounting warning signs.",
        "question": "The combination of DSO surging to 92 days and granting 180-day extended payment terms with right-of-return in Q4 most likely indicates:",
        "options": {
            "A": "Adoption of a highly conservative revenue recognition policy under ASC 606.",
            "B": "Channel stuffing, where revenue should be deferred until the return right expires or returns can be reliably estimated.",
            "C": "A permanent structural increase in distributor cash collection efficiency."
        },
        "answer": "B",
        "explanation": (
            "Channel stuffing occurs when a manufacturer ships excess product to distributors near quarter-end to inflate headline sales, "
            "often accompanied by extended credit terms (180 days vs normal 30 days) and explicit return privileges. Under IFRS 15 / ASC 606, "
            "variable consideration rules require that when significant return uncertainty exists, revenue recognition must be constrained "
            "to the amount that is highly probable of not experiencing a significant reversal. Surging DSO (jumping from 45 to 92 days) is a classic "
            "warning sign that channel partners cannot absorb the shipped inventory, signaling that reported revenue is prematurely recognized."
        )
    })

    questions.append({
        "id": "L2-V33-Q5",
        "level": 2,
        "module": "m17-quality-l2",
        "topic": "Evaluating Quality of Financial Reports",
        "vignette_id": v33_id,
        "vignette_title": v33_title,
        "vignette_text": v33_text,
        "los": "Explain earnings quality red flags, evaluate revenue recognition practices, and assess accounting warning signs.",
        "question": "Regarding the concurrent 25 million USD software purchase and 25 million USD consulting sale with Titan Systems, Lin should conclude that:",
        "options": {
            "A": "This is a round-trip (barter) transaction lacking commercial substance that inflates gross revenue and should be removed from core operating results.",
            "B": "Both transactions should be reported gross because software and consulting services represent distinct operating contracts.",
            "C": "Under IFRS 15, round-trip transactions are standard practice and indicate joint research synergies."
        },
        "answer": "A",
        "explanation": (
            "Concurrent, equal-value reciprocal transactions between commercial parties (buying 25 million USD of software while selling 25 million USD "
            "of consulting services to the same counterparty) are known as 'round-trip' or barter transactions. Because cash merely circulates between "
            "the two entities without net economic substance, accounting standards mandate that such transactions be netted or omitted from reported revenue. "
            "Recognizing 25 million USD in gross revenues artificially pumped CloudStream's top line without contributing true operational economic value."
        )
    })

    # =========================================================================
    # VIGNETTE 34: Balance Sheet Quality, Off-Balance Sheet Liabilities, Cash Flow (5 Questions)
    # Module: m17-quality-l2
    # Topic: Evaluating Quality of Financial Reports
    # =========================================================================
    v34_id = "V34"
    v34_title = "Orion Logistics Holdings: Off-Balance Sheet Financing, Receivables Factoring, and Cash Flow Quality"
    v34_text = (
        "Marcus Vance, CFA, is a senior credit analyst at Apex Rating Agency assessing Orion Logistics Holdings, an "
        "international multimodal freight and supply chain solutions provider. Orion reported a 57% increase in Cash Flow "
        "from Operating Activities (CFO) for Fiscal Year 2024, which management highlighted as proof of exceptional cash "
        "generation and working capital discipline.\n\n"
        "Vance conducts an in-depth audit of Orion's cash flow mechanics, supply chain financing arrangements, off-balance "
        "sheet commitments, and accounting policy choices. Relevant information is summarized in Exhibit 1 and Exhibit 2.\n\n"
        "Exhibit 1: Orion Logistics Financial Data (in millions of USD)\n"
        "- Fiscal 2023:\n"
        "  - Reported CFO = 140\n"
        "  - Reported CFI = -80\n"
        "  - Net Income = 110\n"
        "  - Accounts Receivable (AR) at year-end = 320\n"
        "  - Revenues = 2,000\n"
        "- Fiscal 2024:\n"
        "  - Reported CFO = 220\n"
        "  - Reported CFI = -135\n"
        "  - Net Income = 130\n"
        "  - Accounts Receivable (AR) at year-end = 270\n"
        "  - Revenues = 2,300\n\n"
        "Exhibit 2: Footnote Disclosures for Fiscal 2024\n"
        "1. Receivables Factoring: On 28 December 2024, Orion factored 70 million USD of trade accounts receivable with a commercial "
        "bank without recourse. The bank charged a factoring fee of 2 million USD and remitted 68 million USD in cash, which Orion classified "
        "entirely within Operating Cash Flow.\n"
        "2. Supply Chain Financing (Reverse Factoring): Orion enrolled key suppliers in a bank-administered reverse factoring program totaling "
        "50 million USD. Suppliers receive immediate payment from the bank, while Orion repays the bank in 120 days (extended from standard "
        "45-day terms). Orion presents these obligations within Trade Payables on the balance sheet and cash settlements within CFO.\n"
        "3. Capitalized Software Development: In 2024, Orion capitalized 45 million USD of internal software development expenditures within "
        "Investing Cash Flow (CFI), compared to 15 million USD capitalized in 2023. Under Orion's prior accounting policy, these costs were expensed "
        "as incurred in operating expenses.\n"
        "4. Joint Venture Commitments: Orion holds a 40% equity-method investment in Pacific Terminal JV. The joint venture borrowed 100 million USD "
        "to construct a marine cargo terminal. Orion has entered into a binding take-or-pay throughput agreement guaranteeing minimum annual capacity "
        "payments covering 100% of the joint venture's debt service."
    )

    questions.append({
        "id": "L2-V34-Q1",
        "level": 2,
        "module": "m17-quality-l2",
        "topic": "Evaluating Quality of Financial Reports",
        "vignette_id": v34_id,
        "vignette_title": v34_title,
        "vignette_text": v34_text,
        "los": "Describe indicators of cash flow quality and adjust reported cash flows for non-recurring or aggressive financing items.",
        "question": "Based on Exhibit 1 and Exhibit 2, if Vance adjusts Orion's Fiscal 2024 operating cash flow by removing the effect of the non-recourse receivables factoring, the normalized 2024 CFO is closest to:",
        "options": {
            "A": "152 million USD, indicating normalized CFO growth of 8.6% over 2023.",
            "B": "175 million USD, indicating normalized CFO growth of 25.0% over 2023.",
            "C": "218 million USD, indicating normalized CFO growth of 55.7% over 2023."
        },
        "answer": "A",
        "explanation": (
            "Step 1: Identify cash inflow accelerated through non-recourse receivables factoring:\n"
            "Orion received 68 million USD in cash on 28 December 2024 by transferring 70 million USD of receivables to the bank.\n"
            "Step 2: Calculate normalized CFO by subtracting the non-sustainable cash acceleration:\n"
            "$$\\text{Normalized CFO}_{2024} = \\text{Reported CFO} - \\text{Factoring Inflow} = 220 - 68 = 152\\text{ million USD}$$\n"
            "Step 3: Calculate normalized CFO growth relative to 2023 (140 million USD):\n"
            "$$\\text{Normalized Growth} = \\frac{152 - 140}{140} = \\frac{12}{140} = 8.57\\% \\approx 8.6\\%$$\n"
            "Rather than the reported 57.1% surge, normalized CFO grew by only 8.6%. Factoring is a one-time financing acceleration of receivables "
            "that cannot be repeated on an ongoing operational basis."
        )
    })

    questions.append({
        "id": "L2-V34-Q2",
        "level": 2,
        "module": "m17-quality-l2",
        "topic": "Evaluating Quality of Financial Reports",
        "vignette_id": v34_id,
        "vignette_title": v34_title,
        "vignette_text": v34_text,
        "los": "Describe indicators of balance sheet and cash flow quality, and evaluate off-balance sheet liabilities.",
        "question": "Regarding Orion's reverse factoring (supply chain financing) program of 50 million USD, credit rating agencies would most appropriately adjust the financial statements by:",
        "options": {
            "A": "Leaving trade payables unchanged because the liabilities originated from supplier trade purchases.",
            "B": "Reclassifying the 50 million USD from trade payables to financial debt, and reclassifying subsequent settlements from CFO to financing cash outflows (CFF).",
            "C": "Deducting 50 million USD from investing cash flows (CFI) and adding 50 million USD to equity."
        },
        "answer": "B",
        "explanation": (
            "Under credit rating agency frameworks (e.g., S&P and Moody's):\n"
            "When an entity arranges reverse factoring / supplier finance programs extending payment terms substantially beyond customary commercial terms "
            "(e.g., from 45 days to 120 days), the obligation economically transforms into bank borrowing.\n"
            "Appropriate analytical adjustments include:\n"
            "1. Reclassifying the 50 million USD liability from Trade Payables to Short-Term Financial Debt on the balance sheet.\n"
            "2. Reclassifying payments to the financing intermediary from Cash Flow from Operating Activities (CFO) to Cash Flow from Financing Activities (CFF).\n"
            "Treating these payments as operating outflows disguises bank borrowing as operating working capital management."
        )
    })

    questions.append({
        "id": "L2-V34-Q3",
        "level": 2,
        "module": "m17-quality-l2",
        "topic": "Evaluating Quality of Financial Reports",
        "vignette_id": v34_id,
        "vignette_title": v34_title,
        "vignette_text": v34_text,
        "los": "Evaluate the financial reporting quality of a company by analyzing accounting choices and estimates.",
        "question": "By capitalizing 45 million USD of software development costs in 2024 within CFI instead of expensing them in operating expenses, Orion's reported EBITDA and CFO were affected in which of the following ways?",
        "options": {
            "A": "EBITDA was overstated by 45 million USD, and CFO was overstated by 45 million USD.",
            "B": "EBITDA was unaffected, but CFO was overstated by 45 million USD.",
            "C": "EBITDA was overstated by 45 million USD, but CFO was unaffected."
        },
        "answer": "A",
        "explanation": (
            "Accounting treatment of software development expenditures:\n"
            "- If expensed: The 45 million USD reduces operating income, EBITDA, and operating cash flow (CFO).\n"
            "- If capitalized: The 45 million USD bypasses the income statement and is capitalized on the balance sheet, appearing as a cash outflow in Investing Cash Flow (CFI).\n"
            "Therefore, capitalizing rather than expensing:\n"
            "1. Overstates EBITDA by 45 million USD, since SG&A operating expenses are 45 million USD lower.\n"
            "2. Overstates CFO by 45 million USD, because the cash outflow is shifted from operating activities (CFO) to investing activities (CFI)."
        )
    })

    questions.append({
        "id": "L2-V34-Q4",
        "level": 2,
        "module": "m17-quality-l2",
        "topic": "Evaluating Quality of Financial Reports",
        "vignette_id": v34_id,
        "vignette_title": v34_title,
        "vignette_text": v34_text,
        "los": "Describe indicators of balance sheet and cash flow quality, and evaluate off-balance sheet liabilities.",
        "question": "Regarding the 40% equity-method joint venture and take-or-pay throughput agreement, Vance's most appropriate analytical adjustment is to:",
        "options": {
            "A": "Make no adjustment because the joint venture's borrowings are legally non-recourse to Orion under corporate law.",
            "B": "Add the present value of the take-or-pay capacity payments (or Orion's share of joint venture debt) to Orion's total debt obligations when calculating leverage ratios.",
            "C": "Consolidate 100% of the joint venture's revenues and subtract the 100 million USD debt directly from retained earnings."
        },
        "answer": "B",
        "explanation": (
            "Under financial statement analysis principles for off-balance sheet liabilities:\n"
            "Even though equity-method accounting does not consolidate the debt of an investee onto the investor's balance sheet, a binding take-or-pay "
            "throughput contract that guarantees capacity payments sufficient to cover 100% of debt service creates an unconditional purchase obligation. "
            "Economically, this is equivalent to an off-balance sheet debt guarantee. Analysts must add the present value of these unconditional commitments "
            "(or the underlying debt) to Orion's total financial debt when evaluating creditworthiness, leverage, and fixed-charge coverage ratios."
        )
    })

    questions.append({
        "id": "L2-V34-Q5",
        "level": 2,
        "module": "m17-quality-l2",
        "topic": "Evaluating Quality of Financial Reports",
        "vignette_id": v34_id,
        "vignette_title": v34_title,
        "vignette_text": v34_text,
        "los": "Describe indicators of cash flow quality and compare cash flow reporting under IFRS and US GAAP.",
        "question": "Under IFRS, an entity has flexibility in classifying interest paid, interest received, and dividends received. Which classification policy choice maximizes reported Cash Flow from Operating Activities (CFO)?",
        "options": {
            "A": "Classifying interest paid in CFO and dividends received in CFO.",
            "B": "Classifying interest paid in CFF and dividends received in CFO.",
            "C": "Classifying interest paid in CFO and dividends received in CFI."
        },
        "answer": "B",
        "explanation": (
            "Under IFRS (IAS 7):\n"
            "- Interest paid can be classified either in CFO or Financing Cash Flow (CFF). Moving interest paid to CFF eliminates an operating cash outflow, thereby maximizing reported CFO.\n"
            "- Dividends received can be classified either in CFO or Investing Cash Flow (CFI). Placing dividends received in CFO introduces an operating cash inflow, thereby maximizing reported CFO.\n"
            "Consequently, electing to classify interest paid as CFF and dividends received as CFO results in the highest possible reported CFO."
        )
    })

    # =========================================================================
    # VIGNETTE 35: Operating Lease Capitalization and Valuation Multiples (5 Questions)
    # Module: m18-integration
    # Topic: Integration of Financial Statement Analysis Techniques
    # =========================================================================
    v35_id = "V35"
    v35_title = "GlobalMart Retail Group: Operating Lease Capitalization and Valuation Multiples Adjustment"
    v35_text = (
        "Elena Rostova, CFA, is a consumer retail analyst at ValuTech Capital. Rostova is preparing an equity valuation and "
        "credit analysis for GlobalMart Retail Group for Fiscal Year 2024. GlobalMart operates a chain of 450 general merchandise stores. "
        "To compare GlobalMart on an equivalent basis with peer retailers that own their store properties or operate under different leasing "
        "accounting regimes, Rostova must capitalize GlobalMart's historical operating leases and evaluate the impact on financial ratios, "
        "EBITDA, and valuation multiples.\n\n"
        "Rostova compiles the financial information for GlobalMart shown in Exhibit 1 and Exhibit 2.\n\n"
        "Exhibit 1: GlobalMart Retail Group Reported Financial Excerpts (in millions of USD)\n"
        "- Fiscal Year 2024:\n"
        "  - Revenues = 5,000\n"
        "  - Operating Income (Reported EBIT) = 400\n"
        "  - Depreciation and Amortization = 150\n"
        "  - Reported EBITDA = 550\n"
        "  - Reported Interest Expense = 60\n"
        "  - Income Tax Expense (at 25% tax rate) = 85\n"
        "  - Net Income = 255\n"
        "  - Cash and Cash Equivalents = 100\n"
        "  - Reported Long-Term Financial Debt = 800\n"
        "  - Shareholders' Equity = 1,600\n"
        "  - Shares Outstanding = 100 million\n"
        "  - Current Share Price = 30.00 USD (Market Capitalization of Equity = 3,000 million USD)\n\n"
        "Exhibit 2: Operating Lease Disclosures and Obligations\n"
        "- Minimum future operating lease commitments as of fiscal year-end 2024 (in millions of USD):\n"
        "  - Year 1 (2025): 120\n"
        "  - Year 2 (2026): 110\n"
        "  - Year 3 (2027): 100\n"
        "  - Year 4 (2028): 90\n"
        "  - Year 5 (2029): 80\n"
        "  - Thereafter: 240 (payable in equal annual installments of 80 in Years 6, 7, and 8)\n"
        "- GlobalMart's incremental borrowing rate (discount rate) = 6.0%\n"
        "- Annual operating lease rent expense included in 2024 SG&A expenses = 125 million USD."
    )

    questions.append({
        "id": "L2-V35-Q1",
        "level": 2,
        "module": "m18-integration",
        "topic": "Integration of Financial Statement Analysis Techniques",
        "vignette_id": v35_id,
        "vignette_title": v35_title,
        "vignette_text": v35_text,
        "los": "Adjust financial statements for operating leases and demonstrate the impact on financial statements and ratios.",
        "question": "Based on Exhibit 2 and using GlobalMart's 6.0% incremental borrowing rate, the present value of the operating lease commitments (capitalized lease liability) is closest to:",
        "options": {
            "A": "586 million USD",
            "B": "660 million USD",
            "C": "740 million USD"
        },
        "answer": "A",
        "explanation": (
            "Discount each future operating lease commitment at the 6.0% incremental borrowing rate:\n"
            "$$\\text{PV} = \\sum_{t=1}^8 \\frac{\\text{Payment}_t}{(1 + 0.06)^t}$$\n"
            "- Year 1: $\\frac{120}{1.06^1} = 113.21\\text{ million USD}$\n"
            "- Year 2: $\\frac{110}{1.06^2} = 97.90\\text{ million USD}$\n"
            "- Year 3: $\\frac{100}{1.06^3} = 83.96\\text{ million USD}$\n"
            "- Year 4: $\\frac{90}{1.06^4} = 71.29\\text{ million USD}$\n"
            "- Year 5: $\\frac{80}{1.06^5} = 59.78\\text{ million USD}$\n"
            "- Year 6: $\\frac{80}{1.06^6} = 56.40\\text{ million USD}$\n"
            "- Year 7: $\\frac{80}{1.06^7} = 53.20\\text{ million USD}$\n"
            "- Year 8: $\\frac{80}{1.06^8} = 50.19\\text{ million USD}$\n\n"
            "Summing all discounted cash flows:\n"
            "$$\\text{PV} = 113.21 + 97.90 + 83.96 + 71.29 + 59.78 + 56.40 + 53.20 + 50.19 = 585.93\\text{ million USD} \\approx 586\\text{ million USD}$$"
        )
    })

    questions.append({
        "id": "L2-V35-Q2",
        "level": 2,
        "module": "m18-integration",
        "topic": "Integration of Financial Statement Analysis Techniques",
        "vignette_id": v35_id,
        "vignette_title": v35_title,
        "vignette_text": v35_text,
        "los": "Adjust financial statements for operating leases and evaluate the impact on debt and enterprise value.",
        "question": "Following the capitalization of operating leases, GlobalMart's Adjusted Total Debt and Adjusted Enterprise Value (EV) are closest to:",
        "options": {
            "A": "Adjusted Total Debt = 1,386 million USD; Adjusted EV = 4,286 million USD",
            "B": "Adjusted Total Debt = 1,040 million USD; Adjusted EV = 3,940 million USD",
            "C": "Adjusted Total Debt = 1,540 million USD; Adjusted EV = 4,440 million USD"
        },
        "answer": "A",
        "explanation": (
            "Step 1: Calculate Adjusted Total Debt by adding the capitalized lease liability (586 million USD) to reported financial debt:\n"
            "$$\\text{Adjusted Total Debt} = \\text{Reported Debt} + \\text{PV of Leases} = 800 + 586 = 1,386\\text{ million USD}$$\n"
            "Step 2: Calculate Adjusted Net Debt:\n"
            "$$\\text{Adjusted Net Debt} = \\text{Adjusted Total Debt} - \\text{Cash} = 1,386 - 100 = 1,286\\text{ million USD}$$\n"
            "Step 3: Calculate Adjusted Enterprise Value (EV):\n"
            "$$\\text{Adjusted EV} = \\text{Market Value of Equity} + \\text{Adjusted Net Debt} = 3,000 + 1,286 = 4,286\\text{ million USD}$$\n"
            "(Note: Prior to adjustment, unadjusted $\\text{EV} = 3,000 + (800 - 100) = 3,700\\text{ million USD}$)."
        )
    })

    questions.append({
        "id": "L2-V35-Q3",
        "level": 2,
        "module": "m18-integration",
        "topic": "Integration of Financial Statement Analysis Techniques",
        "vignette_id": v35_id,
        "vignette_title": v35_title,
        "vignette_text": v35_text,
        "los": "Adjust financial statements for operating leases and demonstrate the impact on operating profitability and EBITDA.",
        "question": "When adjusting GlobalMart's 2024 reported earnings to reflect lease capitalization, GlobalMart's Adjusted EBITDA is closest to:",
        "options": {
            "A": "550 million USD",
            "B": "675 million USD",
            "C": "700 million USD"
        },
        "answer": "B",
        "explanation": (
            "Under operating lease accounting, the entire rental payment (125 million USD) is included within operating expenses (SG&A), reducing EBITDA.\n"
            "Upon capitalizing operating leases, the rental expense is eliminated and replaced by:\n"
            "1. Depreciation of the right-of-use asset.\n"
            "2. Interest expense on the lease liability.\n"
            "Because EBITDA is measured before both depreciation and interest, the entire 125 million USD operating lease payment is added back to EBITDA:\n"
            "$$\\text{Adjusted EBITDA} = \\text{Reported EBITDA} + \\text{Lease Rent Expense} = 550 + 125 = 675\\text{ million USD}$$"
        )
    })

    questions.append({
        "id": "L2-V35-Q4",
        "level": 2,
        "module": "m18-integration",
        "topic": "Integration of Financial Statement Analysis Techniques",
        "vignette_id": v35_id,
        "vignette_title": v35_title,
        "vignette_text": v35_text,
        "los": "Demonstrate the use of financial statement analysis in evaluating the impact of accounting choices on valuation multiples.",
        "question": "Comparing the unadjusted and adjusted valuation multiples, capitalizing operating leases causes GlobalMart's EV/EBITDA multiple to:",
        "options": {
            "A": "Decrease from 6.73x to 6.35x.",
            "B": "Increase from 5.45x to 7.20x.",
            "C": "Remain completely unchanged at 6.73x."
        },
        "answer": "A",
        "explanation": (
            "Step 1: Calculate Unadjusted EV/EBITDA multiple:\n"
            "$$\\text{Unadjusted EV} = 3,700\\text{ million USD}$$\n"
            "$$\\text{Unadjusted EBITDA} = 550\\text{ million USD}$$\n"
            "$$\\text{Unadjusted EV/EBITDA} = \\frac{3,700}{550} = 6.727\\times \\approx 6.73\\times$$\n\n"
            "Step 2: Calculate Adjusted EV/EBITDA multiple:\n"
            "$$\\text{Adjusted EV} = 4,286\\text{ million USD}$$\n"
            "$$\\text{Adjusted EBITDA} = 675\\text{ million USD}$$\n"
            "$$\\text{Adjusted EV/EBITDA} = \\frac{4,286}{675} = 6.3496\\times \\approx 6.35\\times$$\n\n"
            "Conclusion: Capitalizing leases increases EBITDA by +22.7% (from 550 to 675), while EV increases by +15.8% (from 3,700 to 4,286). "
            "Because the denominator expands by a greater percentage than the numerator, the EV/EBITDA multiple contracts from 6.73x to 6.35x."
        )
    })

    questions.append({
        "id": "L2-V35-Q5",
        "level": 2,
        "module": "m18-integration",
        "topic": "Integration of Financial Statement Analysis Techniques",
        "vignette_id": v35_id,
        "vignette_title": v35_title,
        "vignette_text": v35_text,
        "los": "Adjust financial statements for operating leases and explain the impact on cash flow statement classification.",
        "question": "Capitalizing operating leases alters GlobalMart's cash flow statement presentation by:",
        "options": {
            "A": "Decreasing Cash Flow from Operating Activities (CFO) and increasing Cash Flow from Financing Activities (CFF).",
            "B": "Increasing Cash Flow from Operating Activities (CFO) and increasing Cash Flow from Financing Activities (CFF) cash outflows.",
            "C": "Leaving CFO, CFI, and CFF completely unchanged."
        },
        "answer": "B",
        "explanation": (
            "Under operating lease accounting, the entire lease rental payment of 125 million USD is classified as an operating cash outflow within CFO.\n"
            "When operating leases are capitalized:\n"
            "1. The interest portion of the lease payment is classified within CFO (or CFF under IFRS).\n"
            "2. The principal portion of the lease payment is classified as a debt principal repayment within CFF.\n"
            "Consequently, CFO increases (because the operating cash outflow is reduced to only the interest portion), while financing cash outflows in CFF increase "
            "by the principal reduction component."
        )
    })

    # =========================================================================
    # VIGNETTE 36: Defined Benefit Pension Plan Adjustments (5 Questions)
    # Module: m18-integration
    # Topic: Integration of Financial Statement Analysis Techniques
    # =========================================================================
    v36_id = "V36"
    v36_title = "Vulcan Heavy Industries: Adjusting Defined Benefit Pension Assumptions and Financial Statements"
    v36_text = (
        "Priya Patel, CFA, is an industrial sector credit and equity analyst at Meridian Capital. Patel is evaluating Vulcan "
        "Heavy Industries, a manufacturer of heavy mining and construction machinery. Vulcan sponsors an extensive defined "
        "benefit (DB) pension plan covering current and retired manufacturing personnel. Patel is concerned about the "
        "aggressiveness of Vulcan's pension assumptions under US GAAP, their impact on reported operating profit, and the "
        "implications of the plan deficit for enterprise valuation and debt covenants.\n\n"
        "Patel gathers the pension plan information for Vulcan Heavy Industries for Fiscal Year 2024 shown in Exhibit 1.\n\n"
        "Exhibit 1: Vulcan Heavy Industries Defined Benefit Plan Data (in millions of USD)\n"
        "- Present Value of Benefit Obligation (PBO) as of 31 Dec 2024 = 1,800\n"
        "- Effective Duration of the PBO = 14.0 years\n"
        "- Fair Value of Plan Assets as of 31 Dec 2024 = 1,500\n"
        "- Funded Status (Net Pension Liability on Balance Sheet) = -300\n"
        "- Plan Assumptions:\n"
        "  - Discount Rate used by Vulcan = 5.50%\n"
        "  - Benchmark High-Quality Corporate Bond Yield (Market Rate) = 4.50%\n"
        "  - Expected Long-Term Rate of Return on Plan Assets = 7.50%\n"
        "  - Actual Return on Plan Assets during 2024 = 4.00%\n"
        "- Fiscal Year 2024 Pension Cost and Cash Flow Data:\n"
        "  - Service Cost (Current Service Cost) = 45\n"
        "  - Interest Cost on PBO = 93.5\n"
        "  - Expected Return on Plan Assets = 105\n"
        "  - Amortization of Prior Actuarial Loss = 6.5\n"
        "  - Net Periodic Pension Cost reported on Income Statement = 40 (45 + 93.5 - 105 + 6.5)\n"
        "  - Employer Cash Contribution to Plan Assets in 2024 = 65\n"
        "  - Reported Operating Income (EBIT) = 320\n"
        "  - Total Financial Debt (excluding Pension Deficit) = 1,100"
    )

    questions.append({
        "id": "L2-V36-Q1",
        "level": 2,
        "module": "m18-integration",
        "topic": "Integration of Financial Statement Analysis Techniques",
        "vignette_id": v36_id,
        "vignette_title": v36_title,
        "vignette_text": v36_text,
        "los": "Adjust financial statements for post-employment benefit plan assumptions and evaluate the impact on financial statements.",
        "question": "If Patel adjusts Vulcan's pension assumptions to match the benchmark corporate bond discount rate of 4.50% (a 100 basis point decrease), the adjusted PBO and adjusted funded status are closest to:",
        "options": {
            "A": "Adjusted PBO = 2,052 million USD; Adjusted Funded Status = -552 million USD",
            "B": "Adjusted PBO = 1,926 million USD; Adjusted Funded Status = -426 million USD",
            "C": "Adjusted PBO = 2,210 million USD; Adjusted Funded Status = -710 million USD"
        },
        "answer": "A",
        "explanation": (
            "Step 1: Estimate percentage change in PBO using effective duration:\n"
            "$$\\% \\Delta \\text{PBO} \\approx -\\text{Duration} \\times \\Delta y$$\n"
            "With a 100 bps decrease in discount rate ($\\Delta y = -0.010$):\n"
            "$$\\% \\Delta \\text{PBO} \\approx -14.0 \\times (-0.010) = +14.0\\%$$\n"
            "Step 2: Calculate dollar change and adjusted PBO:\n"
            "$$\\Delta \\text{PBO} = +14.0\\% \\times 1,800\\text{ million USD} = +252\\text{ million USD}$$\n"
            "$$\\text{Adjusted PBO} = 1,800 + 252 = 2,052\\text{ million USD}$$\n"
            "Step 3: Calculate adjusted funded status:\n"
            "$$\\text{Adjusted Funded Status} = \\text{Plan Assets} - \\text{Adjusted PBO} = 1,500 - 2,052 = -552\\text{ million USD}$$\n"
            "The net pension liability expands from -300 million USD to -552 million USD."
        )
    })

    questions.append({
        "id": "L2-V36-Q2",
        "level": 2,
        "module": "m18-integration",
        "topic": "Integration of Financial Statement Analysis Techniques",
        "vignette_id": v36_id,
        "vignette_title": v36_title,
        "vignette_text": v36_text,
        "los": "Adjust financial statements for post-employment benefit plan assumptions and evaluate economic pension expense.",
        "question": "To reflect economic operating performance, Patel adjusts Vulcan's reported Operating Income (EBIT = 320 million USD) by replacing reported net periodic pension cost with service cost. Vulcan's Adjusted Operating Income is:",
        "options": {
            "A": "315 million USD",
            "B": "325 million USD",
            "C": "360 million USD"
        },
        "answer": "A",
        "explanation": (
            "In financial statement analysis of defined benefit pension plans:\n"
            "Only service cost (45 million USD) represents operating labor compensation for the current period. Interest cost (93.5 million USD) "
            "is a financing expense, and the expected return on assets (105 million USD) is an investment return.\n"
            "To adjust operating profit:\n"
            "$$\\text{Adjusted EBIT} = \\text{Reported EBIT} + \\text{Reported Net Pension Cost} - \\text{Service Cost}$$\n"
            "$$\\text{Adjusted EBIT} = 320 + 40 - 45 = 315\\text{ million USD}$$\n"
            "Reported operating income was overstated by 5 million USD because the net non-operating pension credit (-65 net of return and interest) "
            "artificially subsidized reported operating expenses."
        )
    })

    questions.append({
        "id": "L2-V36-Q3",
        "level": 2,
        "module": "m18-integration",
        "topic": "Integration of Financial Statement Analysis Techniques",
        "vignette_id": v36_id,
        "vignette_title": v36_title,
        "vignette_text": v36_text,
        "los": "Compare the accounting for post-employment benefit plans under IFRS and US GAAP.",
        "question": "Under US GAAP, Vulcan assumed an expected rate of return on plan assets of 7.50% (generating 105 million USD in expected return), while actual asset return was 4.00% (generating 56 million USD). Under IFRS (IAS 19), how would this discrepancy be accounted for?",
        "options": {
            "A": "IFRS does not permit an expected rate of return assumption; net interest expense is calculated using the discount rate, and asset return variances flow to OCI and are never recycled to P&L.",
            "B": "IFRS requires the actual return on assets of 56 million USD to be recognized directly in operating income.",
            "C": "IFRS allows management to set the expected return up to 10% regardless of actual portfolio performance."
        },
        "answer": "A",
        "explanation": (
            "Under IFRS (IAS 19):\n"
            "1. The expected rate of return assumption is not permitted. Instead, net interest expense/income is computed by multiplying the net funded deficit/surplus "
            "by the discount rate.\n"
            "2. Any difference between actual return on assets and the discount-rate-based interest income is treated as an actuarial remeasurement recognized directly in "
            "Other Comprehensive Income (OCI).\n"
            "3. Remeasurements in OCI are never recycled to profit and loss. This eliminates the managerial discretion available under US GAAP to boost reported net income "
            "by assuming an aggressive expected rate of return on assets."
        )
    })

    questions.append({
        "id": "L2-V36-Q4",
        "level": 2,
        "module": "m18-integration",
        "topic": "Integration of Financial Statement Analysis Techniques",
        "vignette_id": v36_id,
        "vignette_title": v36_title,
        "vignette_text": v36_text,
        "los": "Adjust financial statements for post-employment benefit plan contributions and explain cash flow effects.",
        "question": "Vulcan made an employer cash contribution of 65 million USD to plan assets during 2024, while reported net periodic pension cost was 40 million USD. What adjustment should Patel make to reported Cash Flow from Operating Activities (CFO)?",
        "options": {
            "A": "No adjustment is required because employer pension contributions are properly classified in CFO.",
            "B": "Add 25 million USD to CFO and deduct 25 million USD from Cash Flow from Financing Activities (CFF).",
            "C": "Deduct 25 million USD from CFO and add 25 million USD to Cash Flow from Investing Activities (CFI)."
        },
        "answer": "B",
        "explanation": (
            "When employer cash contributions exceed reported net periodic pension cost:\n"
            "$$\\text{Excess Contribution} = \\text{Employer Contribution} - \\text{Net Periodic Pension Cost} = 65 - 40 = 25\\text{ million USD}$$\n"
            "Economically, the excess contribution of 25 million USD represents a paydown of the principal of a long-term debt-like liability (the pension deficit). "
            "Principal repayments are financing activities, not operating activities.\n"
            "Therefore, to reflect economic reality:\n"
            "1. Add 25 million USD back to CFO (correcting for the operating cash flow understatement).\n"
            "2. Deduct 25 million USD from CFF (classifying it as a debt repayment financing outflow)."
        )
    })

    questions.append({
        "id": "L2-V36-Q5",
        "level": 2,
        "module": "m18-integration",
        "topic": "Integration of Financial Statement Analysis Techniques",
        "vignette_id": v36_id,
        "vignette_title": v36_title,
        "vignette_text": v36_text,
        "los": "Demonstrate the use of financial statement analysis in evaluating the credit and equity valuation effects of pension plans.",
        "question": "When integrating Vulcan's defined benefit pension plan into Enterprise Value (EV) calculation and credit rating evaluation, Patel should treat the net pension deficit by:",
        "options": {
            "A": "Adding the net pension liability (-300 million USD reported, or -552 million USD adjusted) to financial debt in calculating EV.",
            "B": "Ignoring the funded status because pension liabilities are contingent on employee retirement dates.",
            "C": "Adding the full PBO of 1,800 million USD to enterprise value while ignoring plan assets."
        },
        "answer": "A",
        "explanation": (
            "In enterprise valuation and credit rating analysis:\n"
            "A defined benefit pension deficit represents a contractual claim on corporate assets by employees that has economic priority similar to senior financial debt. "
            "Therefore, the net pension liability (Funded Status) is treated as a debt-equivalent:\n"
            "$$\\text{Adjusted Total Debt} = \\text{Financial Debt} + \\text{Net Pension Liability}$$\n"
            "Using the reported deficit: $ 1,100 + 300 = 1,400\\text{ million USD} $.\n"
            "Using the benchmark-adjusted deficit: $ 1,100 + 552 = 1,652\\text{ million USD} $.\n"
            "Adding the net pension deficit to Net Debt ensures that Enterprise Value and debt multiples (e.g., Debt/EBITDA) accurately reflect all financial obligations."
        )
    })

    # =========================================================================
    # VIGNETTE 37: Normalizing Earnings, Tax Adjustments, Non-Recurring Items (5 Questions)
    # Module: m18-integration
    # Topic: Integration of Financial Statement Analysis Techniques
    # =========================================================================
    v37_id = "V37"
    v37_title = "HealthTech Global: Normalizing Earnings, Tax Adjustments, and Non-Recurring Items"
    v37_text = (
        "James Thornton, CFA, is a private equity associate at Crestview Capital. Thornton is conducting due diligence "
        "and building an LBO financial model for HealthTech Global, a multinational provider of outpatient clinical services "
        "and specialized medical diagnostics. HealthTech's reported operating results have been volatile over the past three fiscal "
        "years, marked by numerous non-operating gains, restructuring programs, litigation settlements, and inventory adjustments.\n\n"
        "To evaluate HealthTech's sustainable earnings power and support valuation multiples, Thornton compiles the income statement "
        "data for Fiscal Year 2024 presented in Exhibit 1 and Exhibit 2.\n\n"
        "Exhibit 1: HealthTech Global Reported Income Statement Excerpts (in millions of USD)\n"
        "- Fiscal Year 2024:\n"
        "  - Revenues = 2,400\n"
        "  - Cost of Goods Sold (including 10 million USD inventory write-down) = 1,450\n"
        "  - Gross Profit = 950\n"
        "  - Selling, General, and Administrative (SG&A) Expenses = 580\n"
        "  - Restructuring Charges = 45\n"
        "  - Litigation Settlement Expense = 15\n"
        "  - Acquisition Integration and Advisory Costs = 20\n"
        "  - Gain on Sale of Corporate Real Estate = 35 (recorded in operating income)\n"
        "  - Reported Operating Income (EBIT) = 325 (950 - 580 - 45 - 15 - 20 + 35)\n"
        "  - Interest Expense = 65\n"
        "  - Pre-Tax Income = 260\n"
        "  - Income Tax Expense = 52\n"
        "  - Reported Net Income = 208\n"
        "  - Depreciation and Amortization = 95\n\n"
        "Exhibit 2: Additional Operating and Tax Information\n"
        "1. Restructuring History: HealthTech recorded restructuring charges in each of the past three fiscal years: 38 million USD in 2022, "
        "42 million USD in 2023, and 45 million USD in 2024, primarily related to continuous clinic reconfigurations.\n"
        "2. Litigation Settlement: The 15 million USD expense settled a one-time patent dispute with an equipment supplier.\n"
        "3. Real Estate Gain: The 35 million USD pre-tax gain arose from selling HealthTech's historical corporate headquarters building.\n"
        "4. Acquisition Integration Costs: The 20 million USD represents one-off advisory and IT migration costs from acquiring a regional lab operator.\n"
        "5. Tax Rates: HealthTech's reported effective tax rate is 20.0% (52 / 260), while its statutory marginal corporate tax rate is 25.0%."
    )

    questions.append({
        "id": "L2-V37-Q1",
        "level": 2,
        "module": "m18-integration",
        "topic": "Integration of Financial Statement Analysis Techniques",
        "vignette_id": v37_id,
        "vignette_title": v37_title,
        "vignette_text": v37_text,
        "los": "Demonstrate the use of financial statement analysis in screening, normalizing historical earnings, and removing non-recurring items.",
        "question": "When normalizing HealthTech Global's Operating Income (EBIT) for 2024, Thornton should conclude regarding the restructuring charges that:",
        "options": {
            "A": "Restructuring charges should be added back because they are labeled non-recurring by management.",
            "B": "Restructuring charges should not be added back because recurring in each of the last three years demonstrates they are routine operating expenses.",
            "C": "Exactly 50% of the restructuring charges should be capitalized into goodwill."
        },
        "answer": "B",
        "explanation": (
            "In financial statement analysis, an analyst must distinguish between genuinely non-recurring events and routine costs of business. "
            "Although management presents restructuring charges as 'unusual' or 'non-recurring', HealthTech has incurred restructuring charges in every "
            "single year (38 million USD in 2022, 42 million USD in 2023, and 45 million USD in 2024) to reconfigure clinics. "
            "Because clinic restructuring is an ongoing operational requirement in HealthTech's business model, adding these costs back would artificially "
            "overstate normalized operating profit and sustainable earnings power."
        )
    })

    questions.append({
        "id": "L2-V37-Q2",
        "level": 2,
        "module": "m18-integration",
        "topic": "Integration of Financial Statement Analysis Techniques",
        "vignette_id": v37_id,
        "vignette_title": v37_title,
        "vignette_text": v37_text,
        "los": "Demonstrate the use of financial statement analysis in normalizing historical earnings and adjusting operating profit.",
        "question": "Treating the real estate gain (+35 million USD), the litigation settlement (-15 million USD), and acquisition integration costs (-20 million USD) as genuinely non-recurring, HealthTech's Normalized Operating Income (EBIT) for 2024 is closest to:",
        "options": {
            "A": "325 million USD",
            "B": "360 million USD",
            "C": "370 million USD"
        },
        "answer": "A",
        "explanation": (
            "Step 1: Identify genuinely non-recurring items included in Reported Operating Income (EBIT):\n"
            "- Pre-tax gain on sale of real estate: +35 million USD (deduct, as it is a one-time non-operating gain).\n"
            "- One-off litigation settlement: -15 million USD (add back).\n"
            "- Acquisition integration advisory costs: -20 million USD (add back).\n"
            "- Note: Restructuring charges (-45 million USD) are recurring operational costs and are NOT adjusted.\n\n"
            "Step 2: Calculate Normalized Operating Income:\n"
            "$$\\text{Normalized EBIT} = \\text{Reported EBIT} - \\text{Gain on Real Estate} + \\text{Litigation} + \\text{Integration Costs}$$\n"
            "$$\\text{Normalized EBIT} = 325 - 35 + 15 + 20 = 325\\text{ million USD}$$\n"
            "Because the non-recurring expenses (+35 million USD add-backs) exactly equal the non-recurring gain (-35 million USD deduction), Normalized EBIT equals 325 million USD."
        )
    })

    questions.append({
        "id": "L2-V37-Q3",
        "level": 2,
        "module": "m18-integration",
        "topic": "Integration of Financial Statement Analysis Techniques",
        "vignette_id": v37_id,
        "vignette_title": v37_title,
        "vignette_text": v37_text,
        "los": "Demonstrate the use of financial statement analysis in tax-effecting adjustments to normalize earnings.",
        "question": "When calculating Normalized Net Income, which tax rate should Thornton apply to incremental pre-tax normalizing adjustments, and what is the underlying rationale?",
        "options": {
            "A": "The effective tax rate of 20.0%, because it reflects the actual average cash taxes paid on reported pre-tax income.",
            "B": "The marginal tax rate of 25.0%, because incremental additions or deductions to taxable income affect taxes at the statutory marginal rate.",
            "C": "A blended tax rate of 0%, because non-recurring adjustments are permanently exempt from corporate income taxes."
        },
        "answer": "B",
        "explanation": (
            "When normalizing earnings for non-recurring or unusual items:\n"
            "The statutory marginal tax rate (25.0%) must be applied to incremental pre-tax adjustments, not the effective tax rate (20.0%). "
            "The effective tax rate is an average historical rate impacted by discrete tax credits, foreign subsidiary rate differences, and one-time settlements. "
            "Any incremental dollar added to or subtracted from pre-tax operating income will be taxed or generate a tax shield at the company's marginal statutory rate."
        )
    })

    questions.append({
        "id": "L2-V37-Q4",
        "level": 2,
        "module": "m18-integration",
        "topic": "Integration of Financial Statement Analysis Techniques",
        "vignette_id": v37_id,
        "vignette_title": v37_title,
        "vignette_text": v37_text,
        "los": "Adjust financial statements to normalize earnings by removing non-recurring items and tax-effecting adjustments.",
        "question": "Suppose Thornton evaluates an alternative scenario where the 10 million USD inventory write-down is also determined to be a one-time non-recurring event. HealthTech's Normalized Net Income under this scenario (using the 25.0% marginal tax rate) is closest to:",
        "options": {
            "A": "208.0 million USD",
            "B": "215.5 million USD",
            "C": "218.0 million USD"
        },
        "answer": "B",
        "explanation": (
            "Step 1: Compute total net pre-tax normalizing adjustments:\n"
            "- Remove real estate gain: -35 million USD\n"
            "- Add back litigation settlement: +15 million USD\n"
            "- Add back acquisition integration costs: +20 million USD\n"
            "- Add back inventory write-down: +10 million USD\n"
            "$$\\text{Net Pre-Tax Adjustment} = -35 + 15 + 20 + 10 = +10\\text{ million USD}$$\n\n"
            "Step 2: Calculate after-tax adjustment using the 25.0% marginal tax rate:\n"
            "$$\\text{After-Tax Adjustment} = 10 \\times (1 - 0.25) = +7.5\\text{ million USD}$$\n\n"
            "Step 3: Calculate Normalized Net Income:\n"
            "$$\\text{Normalized Net Income} = \\text{Reported Net Income} + \\text{After-Tax Adjustment} = 208.0 + 7.5 = 215.5\\text{ million USD}$$"
        )
    })

    questions.append({
        "id": "L2-V37-Q5",
        "level": 2,
        "module": "m18-integration",
        "topic": "Integration of Financial Statement Analysis Techniques",
        "vignette_id": v37_id,
        "vignette_title": v37_title,
        "vignette_text": v37_text,
        "los": "Demonstrate the use of financial statement analysis in evaluating the impact of accounting choices on valuation multiples.",
        "question": "Thornton calculates Normalized EBITDA for HealthTech. Adding back depreciation and amortization of 95 million USD to Normalized EBIT (325 million USD) yields Normalized EBITDA of 420 million USD (equal to Reported EBITDA of 420 million USD). If the acquisition Enterprise Value is 3,360 million USD, which of the following best describes the effect of earnings normalization on the EV/EBITDA multiple?",
        "options": {
            "A": "The EV/EBITDA multiple remains 8.0x because the non-recurring add-backs offset the non-recurring gain.",
            "B": "The EV/EBITDA multiple contracts to 6.5x due to higher sustainable cash flow.",
            "C": "The EV/EBITDA multiple expands to 10.5x because restructuring charges are eliminated."
        },
        "answer": "A",
        "explanation": (
            "Step 1: Compute Reported EBITDA and Normalized EBITDA:\n"
            "$$\\text{Reported EBITDA} = \\text{Reported EBIT} (325) + \\text{D&A} (95) = 420\\text{ million USD}$$\n"
            "$$\\text{Normalized EBITDA} = \\text{Normalized EBIT} (325) + \\text{D&A} (95) = 420\\text{ million USD}$$\n"
            "Step 2: Calculate EV/EBITDA multiple:\n"
            "$$\\text{EV/EBITDA} = \\frac{3,360}{420} = 8.0\\times$$\n"
            "Because the non-recurring operating gain of 35 million USD was exactly matched by non-recurring add-backs (15 million USD litigation and 20 million USD integration), "
            "and because routine restructuring was properly preserved in operating expenses, Normalized EBITDA and the transaction EV/EBITDA multiple remain unchanged at 8.0x."
        )
    })

    # =========================================================================
    # VIGNETTE 38: Multi-Period DuPont Synthesis, Capitalized Borrowing Costs, FCFF (5 Questions)
    # Module: m18-integration
    # Topic: Integration of Financial Statement Analysis Techniques
    # =========================================================================
    v38_id = "V38"
    v38_title = "Apex Infrastructure Ltd: Multi-Period DuPont Synthesis, Capitalized Borrowing Costs, and Free Cash Flow Integration"
    v38_text = (
        "Karen Brooks, CFA, is a senior infrastructure analyst at Vanguard Global Securities. Brooks is conducting a "
        "comprehensive multi-period financial analysis of Apex Infrastructure Ltd, a major civil engineering and utility "
        "infrastructure contractor. Apex executes long-term construction contracts and builds energy assets. Over the period "
        "2022 to 2024, Apex's return on equity (ROE) declined from 15.0% to 12.6%.\n\n"
        "Brooks analyzes Apex's financial statements to uncover the operational and accounting drivers of this return decline, "
        "focusing on capitalized interest, DuPont decomposition, and Free Cash Flow to the Firm (FCFF).\n\n"
        "Exhibit 1: Apex Infrastructure Financial Summary (in millions of GBP)\n"
        "- Fiscal Year 2024:\n"
        "  - Revenues = 1,800\n"
        "  - Operating Income (Reported EBIT) = 270\n"
        "  - Total Interest Incurred = 60\n"
        "    - Interest Expensed on Income Statement = 40\n"
        "    - Interest Capitalized into Construction in Progress (PP&E) = 20\n"
        "  - Pre-Tax Income = 230 (270 - 40)\n"
        "  - Income Tax Expense (at 20% tax rate) = 46\n"
        "  - Net Income = 184\n"
        "  - Depreciation and Amortization (including 5 of depreciation of previously capitalized interest) = 80\n"
        "  - Reported Cash Flow from Operating Activities (CFO) under US GAAP = 210\n"
        "  - Capital Expenditures (including 20 of capitalized interest paid) = 150\n"
        "  - Total Assets: 2022 = 2,000; 2023 = 2,250; 2024 = 2,500\n"
        "  - Shareholders' Equity: 2022 = 800; 2023 = 900; 2024 = 1,000\n\n"
        "Exhibit 2: Multi-Period DuPont Metrics (5-Step Decomposition)\n"
        "- Fiscal 2022:\n"
        "  - Tax Burden (Net Income / EBT) = 0.800\n"
        "  - Interest Burden (EBT / EBIT) = 0.889\n"
        "  - Operating Margin (EBIT / Revenue) = 18.75%\n"
        "  - Asset Turnover (Revenue / Total Assets) = 0.750\n"
        "  - Financial Leverage (Total Assets / Equity) = 2.500\n"
        "  - ROE = 15.00%\n"
        "- Fiscal 2024:\n"
        "  - Tax Burden = 0.800\n"
        "  - Interest Burden = 0.852 (230 / 270)\n"
        "  - Operating Margin = 15.00% (270 / 1,800)\n"
        "  - Asset Turnover = 0.720 (1,800 / 2,500)\n"
        "  - Financial Leverage = 2.500 (2,500 / 1,000)\n"
        "  - ROE = 12.60%"
    )

    questions.append({
        "id": "L2-V38-Q1",
        "level": 2,
        "module": "m18-integration",
        "topic": "Integration of Financial Statement Analysis Techniques",
        "vignette_id": v38_id,
        "vignette_title": v38_title,
        "vignette_text": v38_text,
        "los": "Adjust financial statements for capitalized interest and evaluate the impact on cash flow and free cash flow.",
        "question": "Under US GAAP, Apex reports 210 million GBP in CFO and 150 million GBP in CapEx (including 20 million GBP of capitalized interest paid). When adjusting CFO for capitalized interest, and calculating Free Cash Flow to the Firm (FCFF), what is the Adjusted CFO and does the adjustment change FCFF?",
        "options": {
            "A": "Adjusted CFO = 190 million GBP; FCFF is unchanged.",
            "B": "Adjusted CFO = 230 million GBP; FCFF increases by 20 million GBP.",
            "C": "Adjusted CFO = 190 million GBP; FCFF decreases by 20 million GBP."
        },
        "answer": "A",
        "explanation": (
            "Step 1: Adjust CFO for capitalized interest under US GAAP:\n"
            "Under US GAAP, capitalized interest paid is reported as an investing cash outflow in CFI. Because interest paid is economically an operating cash outflow, "
            "analysts reclassify the 20 million GBP capitalized interest from CFI to CFO:\n"
            "$$\\text{Adjusted CFO} = \\text{Reported CFO} - \\text{Capitalized Interest} = 210 - 20 = 190\\text{ million GBP}$$\n"
            "$$\\text{Adjusted CapEx} = \\text{Reported CapEx} - \\text{Capitalized Interest} = 150 - 20 = 130\\text{ million GBP}$$\n\n"
            "Step 2: Calculate Free Cash Flow to the Firm (FCFF):\n"
            "$$\\text{FCFF} = \\text{Adjusted CFO} + \\text{Total Interest Expensed} \\times (1 - t) - \\text{Adjusted CapEx}$$\n"
            "$$\\text{FCFF} = 190 + 40 \\times (1 - 0.20) - 130 = 190 + 32 - 130 = 92\\text{ million GBP}$$\n"
            "Using unadjusted reported figures: $\\text{FCFF} = 210 + 32 - 150 = 92\\text{ million GBP}$.\n"
            "FCFF is completely unchanged because the 20 million GBP reduction in Adjusted CFO is exactly offset by an identical 20 million GBP reduction in Adjusted CapEx."
        )
    })

    questions.append({
        "id": "L2-V38-Q2",
        "level": 2,
        "module": "m18-integration",
        "topic": "Integration of Financial Statement Analysis Techniques",
        "vignette_id": v38_id,
        "vignette_title": v38_title,
        "vignette_text": v38_text,
        "los": "Adjust financial statements for capitalized interest and evaluate interest coverage and credit quality.",
        "question": "Based on Exhibit 1, Apex's reported interest coverage ratio (using expensed interest) and true interest coverage ratio (using total interest incurred) are closest to:",
        "options": {
            "A": "Reported Coverage = 6.75x; True Coverage = 4.50x",
            "B": "Reported Coverage = 5.25x; True Coverage = 3.80x",
            "C": "Reported Coverage = 6.75x; True Coverage = 6.75x"
        },
        "answer": "A",
        "explanation": (
            "Step 1: Calculate reported interest coverage ratio:\n"
            "$$\\text{Reported Interest Coverage} = \\frac{\\text{Reported EBIT}}{\\text{Expensed Interest}} = \\frac{270}{40} = 6.75\\times$$\n\n"
            "Step 2: Calculate true economic interest coverage ratio using total interest incurred:\n"
            "$$\\text{Total Interest Incurred} = \\text{Expensed Interest} + \\text{Capitalized Interest} = 40 + 20 = 60\\text{ million GBP}$$\n"
            "$$\\text{True Economic Interest Coverage} = \\frac{\\text{Reported EBIT}}{\\text{Total Interest Incurred}} = \\frac{270}{60} = 4.50\\times$$\n\n"
            "Conclusion: Capitalizing interest significantly distorts solvency analysis. The reported interest coverage of 6.75x makes the company appear "
            "substantially safer than its true economic coverage of 4.50x, understating debt service risk."
        )
    })

    questions.append({
        "id": "L2-V38-Q3",
        "level": 2,
        "module": "m18-integration",
        "topic": "Integration of Financial Statement Analysis Techniques",
        "vignette_id": v38_id,
        "vignette_title": v38_title,
        "vignette_text": v38_text,
        "los": "Demonstrate the use of DuPont analysis in evaluating multi-period financial performance.",
        "question": "Using the 5-step DuPont decomposition in Exhibit 2, the primary drivers of Apex's ROE contraction from 15.00% in 2022 to 12.60% in 2024 were:",
        "options": {
            "A": "Increases in the corporate tax burden and debt deleveraging.",
            "B": "Declines in operating margin (from 18.75% to 15.00%) and asset turnover (from 0.750 to 0.720), alongside a higher interest burden.",
            "C": "An expansion in financial leverage offset by falling tax burden."
        },
        "answer": "B",
        "explanation": (
            "Under the 5-step DuPont framework:\n"
            "$$\\text{ROE} = \\text{Tax Burden} \\times \\text{Interest Burden} \\times \\text{Operating Margin} \\times \\text{Asset Turnover} \\times \\text{Financial Leverage}$$\n"
            "Comparing 2022 to 2024:\n"
            "1. Tax Burden: Constant at 0.800 (no impact).\n"
            "2. Financial Leverage: Constant at 2.500 (no impact).\n"
            "3. Operating Margin: Declined from 18.75% to 15.00% (reflecting falling operational profitability or project cost overruns).\n"
            "4. Asset Turnover: Declined from 0.750 to 0.720 (reflecting less efficient utilization of total assets to generate revenue).\n"
            "5. Interest Burden: Fell from 0.889 to 0.852 (meaning higher interest expense absorbed a larger fraction of operating earnings).\n"
            "Thus, deterioration in operating efficiency and asset turnover, compounded by a higher interest burden, drove the ROE decline."
        )
    })

    questions.append({
        "id": "L2-V38-Q4",
        "level": 2,
        "module": "m18-integration",
        "topic": "Integration of Financial Statement Analysis Techniques",
        "vignette_id": v38_id,
        "vignette_title": v38_title,
        "vignette_text": v38_text,
        "los": "Analyze the sensitivity of financial statements and ratios to the choice between capital expenditures and operating expenses.",
        "question": "If Apex had expensed the 20 million GBP of borrowing costs rather than capitalizing them in 2024, the effect on reported EBITDA and the carrying value of PP&E would be:",
        "options": {
            "A": "EBITDA would be unaffected; PP&E carrying value would be 20 million GBP lower.",
            "B": "EBITDA would decrease by 20 million GBP; PP&E carrying value would be unchanged.",
            "C": "EBITDA would increase by 20 million GBP; PP&E carrying value would be 20 million GBP higher."
        },
        "answer": "A",
        "explanation": (
            "Analysis of interest expensing versus capitalization:\n"
            "1. Effect on EBITDA: EBITDA is defined as earnings before interest, taxes, depreciation, and amortization. Expensed interest is classified "
            "below operating profit as a financing item; whether interest is expensed or capitalized, it does not enter EBITDA. Thus, EBITDA is unaffected.\n"
            "2. Effect on PP&E: Capitalized interest is added directly to construction-in-progress on the balance sheet within PP&E. Expensing the 20 million GBP "
            "would mean it is not added to PP&E, resulting in a 20 million GBP lower PP&E carrying value."
        )
    })

    questions.append({
        "id": "L2-V38-Q5",
        "level": 2,
        "module": "m18-integration",
        "topic": "Integration of Financial Statement Analysis Techniques",
        "vignette_id": v38_id,
        "vignette_title": v38_title,
        "vignette_text": v38_text,
        "los": "Synthesize financial statement analysis techniques to evaluate credit risk and accounting distortions.",
        "question": "In synthesizing Apex's overall credit profile, Brooks integrates the capitalized interest adjustment, off-balance sheet commitments, and cash flow trends. Which of the following conclusions is most accurate?",
        "options": {
            "A": "Apex's credit risk is lower than reported because capitalized interest can be deducted from total debt.",
            "B": "Apex's reported financial statements understate credit risk because true economic interest coverage is 4.50x (vs 6.75x reported) and operating cash flow is overstated by 20 million GBP.",
            "C": "Apex's credit profile is entirely unaffected by accounting choices because cash flows are identical across all reporting frameworks."
        },
        "answer": "B",
        "explanation": (
            "A holistic synthesis of Apex's accounting choices reveals significant understatement of credit risk:\n"
            "1. True economic interest coverage is 4.50x rather than the reported 6.75x, because 20 million GBP of interest payments were capitalized into PP&E rather than expensed.\n"
            "2. Operating cash generation is overstated: under US GAAP, capitalized interest is classified in CFI, artificially boosting reported CFO by 20 million GBP (reported CFO = 210 million GBP vs normalized CFO = 190 million GBP).\n"
            "3. Future depreciation will be higher as capitalized interest is amortized over the asset's useful life.\n"
            "Consequently, headline financial statements provide an overly optimistic picture of debt service capacity and cash flow quality."
        )
    })

    return questions

if __name__ == "__main__":
    qs = create_part3_questions()
    print(f"Generated {len(qs)} questions.")
    
    # Currency and KaTeX validation
    bare_dollar_regex = re.compile(r'(?<!\\)\$(?=\d)')
    warnings = 0
    for q in qs:
        text = f"{q['question']} {str(q['options'])} {q['explanation']} {q['vignette_text']}"
        matches = bare_dollar_regex.findall(text)
        if matches:
            print(f"Warning bare dollar in {q['id']}: {matches}")
            warnings += 1
    
    print(f"Bare dollar warnings: {warnings}")
    
    output_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "l2_questions_part3.json")
    
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(qs, f, indent=2, ensure_ascii=False)
        
    print(f"Successfully saved to {output_path} ({os.path.getsize(output_path)} bytes)")
