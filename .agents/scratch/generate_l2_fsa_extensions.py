import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
L2_FSA_P3 = os.path.join(BASE_DIR, "data", "l2_questions_part3.json")
MASTER_FSA = os.path.join(BASE_DIR, "data", "cfa_question_bank_master.json")

with open(L2_FSA_P3, "r", encoding="utf-8") as f:
    existing_p3 = json.load(f)

print(f"Current L2 FSA Part 3 questions: {len(existing_p3)}")

new_fsa_vignettes = [
    # --- Vignette 39: Altman Z-Score & Distress Prediction (m17-quality-l2, 5 Qs) ---
    {
        "id": "L2-V39-Q1",
        "level": 2,
        "module": "m17-quality-l2",
        "topic": "Evaluating Quality of Financial Reports",
        "vignette_id": "V39",
        "vignette_title": "Altman Z-Score and Credit Distress Warning Signals at Titan Heavy Industries",
        "vignette_text": "Titan Heavy Industries is a global manufacturer of heavy earthmoving and construction equipment. Forensic credit analyst Liam O'Connor, CFA, is assessing Titan's credit quality and likelihood of financial distress following three years of deteriorating cash flows.\n\nExhibit 1: Titan Heavy Industries Fiscal Year 2024 Financial Data (in millions of USD)\n- Working Capital (Current Assets minus Current Liabilities) = 150 USD\n- Retained Earnings = 360 USD\n- Earnings Before Interest and Taxes (EBIT) = 240 USD\n- Market Value of Equity (Common + Preferred) = 1,200 USD\n- Total Book Value of Liabilities = 1,500 USD\n- Sales Revenues = 2,400 USD\n- Total Assets = 2,000 USD\n\nAltman's 5-variable Z-Score model for publicly traded manufacturing firms is defined as:\n$$Z = 1.2 \\times X_1 + 1.4 \\times X_2 + 3.3 \\times X_3 + 0.6 \\times X_4 + 1.0 \\times X_5$$\nwhere:\n- $X_1 = \\text{Working Capital} / \\text{Total Assets}$\n- $X_2 = \\text{Retained Earnings} / \\text{Total Assets}$\n- $X_3 = \\text{EBIT} / \\text{Total Assets}$\n- $X_4 = \\text{Market Value of Equity} / \\text{Total Book Value of Liabilities}$\n- $X_5 = \\text{Sales} / \\text{Total Assets}$\n\nAltman's critical zones:\n- $Z < 1.81$: Distress Zone (high probability of bankruptcy within 2 years)\n- $1.81 \\le Z \\le 2.99$: Gray Zone\n- $Z > 2.99$: Safe Zone",
        "los": "Describe the Altman Z-score model and evaluate credit distress indicators.",
        "question": "Based on Exhibit 1, Titan Heavy Industries' Altman Z-Score is closest to:",
        "options": {
            "A": "1.74",
            "B": "2.42",
            "C": "2.82"
        },
        "answer": "B",
        "explanation": "Compute each ratio component using Total Assets = 2,000 USD:\n- $X_1 = 150 / 2{,}000 = 0.0750$\n- $X_2 = 360 / 2{,}000 = 0.1800$\n- $X_3 = 240 / 2{,}000 = 0.1200$\n- $X_4 = 1{,}200 / 1{,}500 = 0.8000$\n- $X_5 = 2{,}400 / 2{,}000 = 1.2000$\nApply the Altman weights:\n$$Z = 1.2(0.0750) + 1.4(0.1800) + 3.3(0.1200) + 0.6(0.8000) + 1.0(1.2000)$$\n$$Z = 0.0900 + 0.2520 + 0.3960 + 0.4800 + 1.2000 = 2.4180 \\approx 2.42$$",
        "distractor_analysis": {
            "A": "1.74 results from erroneously using Net Income instead of EBIT for $X_3$ and omitting $X_1$.",
            "C": "2.82 results from miscalculating $X_4$ as Market Value of Equity divided by Total Assets."
        }
    },
    {
        "id": "L2-V39-Q2",
        "level": 2,
        "module": "m17-quality-l2",
        "topic": "Evaluating Quality of Financial Reports",
        "vignette_id": "V39",
        "vignette_title": "Altman Z-Score and Credit Distress Warning Signals at Titan Heavy Industries",
        "vignette_text": "Titan Heavy Industries is a global manufacturer of heavy earthmoving and construction equipment. Forensic credit analyst Liam O'Connor, CFA, is assessing Titan's credit quality and likelihood of financial distress following three years of deteriorating cash flows.\n\nExhibit 1: Titan Heavy Industries Fiscal Year 2024 Financial Data (in millions of USD)\n- Working Capital (Current Assets minus Current Liabilities) = 150 USD\n- Retained Earnings = 360 USD\n- Earnings Before Interest and Taxes (EBIT) = 240 USD\n- Market Value of Equity (Common + Preferred) = 1,200 USD\n- Total Book Value of Liabilities = 1,500 USD\n- Sales Revenues = 2,400 USD\n- Total Assets = 2,000 USD\n\nAltman's 5-variable Z-Score model for publicly traded manufacturing firms is defined as:\n$$Z = 1.2 \\times X_1 + 1.4 \\times X_2 + 3.3 \\times X_3 + 0.6 \\times X_4 + 1.0 \\times X_5$$\nwhere:\n- $X_1 = \\text{Working Capital} / \\text{Total Assets}$\n- $X_2 = \\text{Retained Earnings} / \\text{Total Assets}$\n- $X_3 = \\text{EBIT} / \\text{Total Assets}$\n- $X_4 = \\text{Market Value of Equity} / \\text{Total Book Value of Liabilities}$\n- $X_5 = \\text{Sales} / \\text{Total Assets}$\n\nAltman's critical zones:\n- $Z < 1.81$: Distress Zone (high probability of bankruptcy within 2 years)\n- $1.81 \\le Z \\le 2.99$: Gray Zone\n- $Z > 2.99$: Safe Zone",
        "los": "Interpret the Altman Z-score and categorize financial distress probability.",
        "question": "Based on its calculated Z-Score of 2.42, Titan Heavy Industries is currently in the:",
        "options": {
            "A": "Distress zone with an imminent default probability exceeding 80%.",
            "B": "Gray zone indicating moderate credit vulnerability and borderline financial health.",
            "C": "Safe zone confirming negligible financial distress risk."
        },
        "answer": "B",
        "explanation": "Titan's Z-Score of 2.42 falls squarely in the Gray Zone ($1.81 \\le Z \\le 2.99$). While the firm is not in imminent bankruptcy ($Z < 1.81$), it lacks the financial strength of safe zone companies ($Z > 2.99$), indicating moderate vulnerability requiring close monitoring of cash flow and debt covenants.",
        "distractor_analysis": {
            "A": "The distress zone requires a Z-score strictly below 1.81.",
            "C": "The safe zone requires a Z-score strictly above 2.99."
        }
    },
    {
        "id": "L2-V39-Q3",
        "level": 2,
        "module": "m17-quality-l2",
        "topic": "Evaluating Quality of Financial Reports",
        "vignette_id": "V39",
        "vignette_title": "Altman Z-Score and Credit Distress Warning Signals at Titan Heavy Industries",
        "vignette_text": "Titan Heavy Industries is a global manufacturer of heavy earthmoving and construction equipment. Forensic credit analyst Liam O'Connor, CFA, is assessing Titan's credit quality and likelihood of financial distress following three years of deteriorating cash flows.\n\nExhibit 1: Titan Heavy Industries Fiscal Year 2024 Financial Data (in millions of USD)\n- Working Capital (Current Assets minus Current Liabilities) = 150 USD\n- Retained Earnings = 360 USD\n- Earnings Before Interest and Taxes (EBIT) = 240 USD\n- Market Value of Equity (Common + Preferred) = 1,200 USD\n- Total Book Value of Liabilities = 1,500 USD\n- Sales Revenues = 2,400 USD\n- Total Assets = 2,000 USD\n\nAltman's 5-variable Z-Score model for publicly traded manufacturing firms is defined as:\n$$Z = 1.2 \\times X_1 + 1.4 \\times X_2 + 3.3 \\times X_3 + 0.6 \\times X_4 + 1.0 \\times X_5$$\nwhere:\n- $X_1 = \\text{Working Capital} / \\text{Total Assets}$\n- $X_2 = \\text{Retained Earnings} / \\text{Total Assets}$\n- $X_3 = \\text{EBIT} / \\text{Total Assets}$\n- $X_4 = \\text{Market Value of Equity} / \\text{Total Book Value of Liabilities}$\n- $X_5 = \\text{Sales} / \\text{Total Assets}$\n\nAltman's critical zones:\n- $Z < 1.81$: Distress Zone (high probability of bankruptcy within 2 years)\n- $1.81 \\le Z \\le 2.99$: Gray Zone\n- $Z > 2.99$: Safe Zone",
        "los": "Explain the role of the Altman Z-score components in evaluating distress.",
        "question": "Which of the 5 Altman variables carries the highest weighting coefficient in the manufacturing model, reflecting its dominant predictive power for corporate solvency?",
        "options": {
            "A": "$X_1$ (Working Capital / Total Assets)",
            "B": "$X_3$ (EBIT / Total Assets)",
            "C": "$X_5$ (Sales / Total Assets)"
        },
        "answer": "B",
        "explanation": "In Altman's model for publicly traded manufacturing firms, $X_3$ (EBIT / Total Assets) has the highest coefficient of 3.3. This highlights that asset earning power (operating return on assets) is the single most critical economic buffer against debt default.",
        "distractor_analysis": {
            "A": "$X_1$ has a coefficient of 1.2.",
            "C": "$X_5$ has a coefficient of 1.0."
        }
    },
    {
        "id": "L2-V39-Q4",
        "level": 2,
        "module": "m17-quality-l2",
        "topic": "Evaluating Quality of Financial Reports",
        "vignette_id": "V39",
        "vignette_title": "Altman Z-Score and Credit Distress Warning Signals at Titan Heavy Industries",
        "vignette_text": "Titan Heavy Industries is a global manufacturer of heavy earthmoving and construction equipment. Forensic credit analyst Liam O'Connor, CFA, is assessing Titan's credit quality and likelihood of financial distress following three years of deteriorating cash flows.\n\nExhibit 1: Titan Heavy Industries Fiscal Year 2024 Financial Data (in millions of USD)\n- Working Capital (Current Assets minus Current Liabilities) = 150 USD\n- Retained Earnings = 360 USD\n- Earnings Before Interest and Taxes (EBIT) = 240 USD\n- Market Value of Equity (Common + Preferred) = 1,200 USD\n- Total Book Value of Liabilities = 1,500 USD\n- Sales Revenues = 2,400 USD\n- Total Assets = 2,000 USD\n\nAltman's 5-variable Z-Score model for publicly traded manufacturing firms is defined as:\n$$Z = 1.2 \\times X_1 + 1.4 \\times X_2 + 3.3 \\times X_3 + 0.6 \\times X_4 + 1.0 \\times X_5$$\nwhere:\n- $X_1 = \\text{Working Capital} / \\text{Total Assets}$\n- $X_2 = \\text{Retained Earnings} / \\text{Total Assets}$\n- $X_3 = \\text{EBIT} / \\text{Total Assets}$\n- $X_4 = \\text{Market Value of Equity} / \\text{Total Book Value of Liabilities}$\n- $X_5 = \\text{Sales} / \\text{Total Assets}$\n\nAltman's critical zones:\n- $Z < 1.81$: Distress Zone (high probability of bankruptcy within 2 years)\n- $1.81 \\le Z \\le 2.99$: Gray Zone\n- $Z > 2.99$: Safe Zone",
        "los": "Describe the limitations of the Altman Z-score model.",
        "question": "A key limitation of applying the original Altman Z-Score model to modern technology or service companies is that:",
        "options": {
            "A": "The model relies heavily on physical asset turnover ($X_5$) and book capital ($X_1$), which understates the economic solvency of asset-light firms with valuable intangible assets.",
            "B": "It uses market value of equity rather than book value of equity in $X_4$.",
            "C": "The model cannot be calculated if a firm has positive retained earnings."
        },
        "answer": "A",
        "explanation": "The original Altman model was calibrated on capital-intensive manufacturing companies. Applying it to modern software and service firms penalizes them unfairly because they possess low physical assets (distorting $X_5$) and rely on internally generated human capital and intangibles omitted from balance sheet assets.",
        "distractor_analysis": {
            "B": "Using market value of equity in $X_4$ is an advantage, incorporating forward-looking market pricing.",
            "C": "Positive retained earnings naturally increase $X_2$ and the Z-score."
        }
    },
    {
        "id": "L2-V39-Q5",
        "level": 2,
        "module": "m17-quality-l2",
        "topic": "Evaluating Quality of Financial Reports",
        "vignette_id": "V39",
        "vignette_title": "Altman Z-Score and Credit Distress Warning Signals at Titan Heavy Industries",
        "vignette_text": "Titan Heavy Industries is a global manufacturer of heavy earthmoving and construction equipment. Forensic credit analyst Liam O'Connor, CFA, is assessing Titan's credit quality and likelihood of financial distress following three years of deteriorating cash flows.\n\nExhibit 1: Titan Heavy Industries Fiscal Year 2024 Financial Data (in millions of USD)\n- Working Capital (Current Assets minus Current Liabilities) = 150 USD\n- Retained Earnings = 360 USD\n- Earnings Before Interest and Taxes (EBIT) = 240 USD\n- Market Value of Equity (Common + Preferred) = 1,200 USD\n- Total Book Value of Liabilities = 1,500 USD\n- Sales Revenues = 2,400 USD\n- Total Assets = 2,000 USD\n\nAltman's 5-variable Z-Score model for publicly traded manufacturing firms is defined as:\n$$Z = 1.2 \\times X_1 + 1.4 \\times X_2 + 3.3 \\times X_3 + 0.6 \\times X_4 + 1.0 \\times X_5$$\nwhere:\n- $X_1 = \\text{Working Capital} / \\text{Total Assets}$\n- $X_2 = \\text{Retained Earnings} / \\text{Total Assets}$\n- $X_3 = \\text{EBIT} / \\text{Total Assets}$\n- $X_4 = \\text{Market Value of Equity} / \\text{Total Book Value of Liabilities}$\n- $X_5 = \\text{Sales} / \\text{Total Assets}$\n\nAltman's critical zones:\n- $Z < 1.81$: Distress Zone (high probability of bankruptcy within 2 years)\n- $1.81 \\le Z \\le 2.99$: Gray Zone\n- $Z > 2.99$: Safe Zone",
        "los": "Describe non-manufacturing adaptations of the Altman model.",
        "question": "In Altman's revised 4-variable model ($Z'$) developed for non-manufacturing and emerging market firms, which variable is excluded to prevent industry asset-turnover distortion?",
        "options": {
            "A": "$X_1$ (Working Capital / Total Assets)",
            "B": "$X_3$ (EBIT / Total Assets)",
            "C": "$X_5$ (Sales / Total Assets)"
        },
        "answer": "C",
        "explanation": "In the $Z'$ non-manufacturing model, $X_5$ (Sales / Total Assets) is eliminated to remove distortions caused by vastly differing capital intensity and asset turnover across service, retail, and technology industries.",
        "distractor_analysis": {
            "A": "Working capital remains a core measure of short-term liquidity in the revised model.",
            "B": "EBIT / Total Assets remains the single most essential operational profitability measure."
        }
    },

    # --- Vignette 40: Non-GAAP Earnings Adjustments & Aggressive Revenue (m17-quality-l2, 5 Qs) ---
    {
        "id": "L2-V40-Q1",
        "level": 2,
        "module": "m17-quality-l2",
        "topic": "Evaluating Quality of Financial Reports",
        "vignette_id": "V40",
        "vignette_title": "Forensic Review of Non-GAAP Adjustments and Channel Stuffing at CloudCore Inc.",
        "vignette_text": "CloudCore Inc. is a provider of cloud-based enterprise security software. Senior portfolio manager Danielle Dupont, CFA, is conducting a financial reporting quality audit of CloudCore's reported results for Fiscal 2024. CloudCore's management heavily emphasizes 'Adjusted EBITDA' in quarterly earnings releases.\n\nExhibit 1: CloudCore Reported US GAAP vs. Non-GAAP Financial Summary (in millions of USD)\n- Reported US GAAP Net Income = 25 USD\n- Provision for Income Taxes = 8 USD\n- Interest Expense = 12 USD\n- Depreciation and Amortization = 35 USD\n- Reported US GAAP Operating Income (EBIT) = 45 USD\n- Share-Based Compensation Expense = 55 USD\n- Recurring Restructuring & Facility Optimization Charges (incurred every year for 5 consecutive years) = 22 USD\n- Litigation Settlement Expenses = 10 USD\n- Accelerated Amortization of Acquired Customer Contracts = 18 USD\n- Management's Reported 'Adjusted EBITDA' = 185 USD\n- Operating Cash Flow (CFO) = 38 USD\n- Days Sales Outstanding (DSO): increased from 48 days in 2023 to 82 days in 2024\n- Finished goods and unbilled accounts receivable rose 45% while subscription revenue grew 12%.",
        "los": "Evaluate the quality of financial reports including non-GAAP earnings measures.",
        "question": "Which of management's non-GAAP add-backs to EBITDA is most aggressive and least justified from an ongoing economic earnings perspective?",
        "options": {
            "A": "Depreciation and amortization expense.",
            "B": "Restructuring charges incurred continuously for five consecutive fiscal years.",
            "C": "Provision for income taxes."
        },
        "answer": "B",
        "explanation": "Non-GAAP adjustments are intended to remove non-recurring, one-off items to reveal core underlying operational earnings. Adding back restructuring charges that have recurred every year for five straight years misrepresents normal, ongoing operating expenses as transitory one-time costs, artificially inflating economic operating profitability.",
        "distractor_analysis": {
            "A": "Depreciation and amortization are standard, valid add-backs in calculating baseline EBITDA.",
            "C": "Income taxes are standard exclusions when computing EBITDA."
        }
    },
    {
        "id": "L2-V40-Q2",
        "level": 2,
        "module": "m17-quality-l2",
        "topic": "Evaluating Quality of Financial Reports",
        "vignette_id": "V40",
        "vignette_title": "Forensic Review of Non-GAAP Adjustments and Channel Stuffing at CloudCore Inc.",
        "vignette_text": "CloudCore Inc. is a provider of cloud-based enterprise security software. Senior portfolio manager Danielle Dupont, CFA, is conducting a financial reporting quality audit of CloudCore's reported results for Fiscal 2024. CloudCore's management heavily emphasizes 'Adjusted EBITDA' in quarterly earnings releases.\n\nExhibit 1: CloudCore Reported US GAAP vs. Non-GAAP Financial Summary (in millions of USD)\n- Reported US GAAP Net Income = 25 USD\n- Provision for Income Taxes = 8 USD\n- Interest Expense = 12 USD\n- Depreciation and Amortization = 35 USD\n- Reported US GAAP Operating Income (EBIT) = 45 USD\n- Share-Based Compensation Expense = 55 USD\n- Recurring Restructuring & Facility Optimization Charges (incurred every year for 5 consecutive years) = 22 USD\n- Litigation Settlement Expenses = 10 USD\n- Accelerated Amortization of Acquired Customer Contracts = 18 USD\n- Management's Reported 'Adjusted EBITDA' = 185 USD\n- Operating Cash Flow (CFO) = 38 USD\n- Days Sales Outstanding (DSO): increased from 48 days in 2023 to 82 days in 2024\n- Finished goods and unbilled accounts receivable rose 45% while subscription revenue grew 12%.",
        "los": "Describe the treatment of share-based compensation in financial statement analysis.",
        "question": "Regarding the 55 million USD add-back of share-based compensation in CloudCore's Adjusted EBITDA, an equity analyst should conclude that:",
        "options": {
            "A": "Share-based compensation is a genuine economic labor expense that dilutes existing equity holders, so adding it back permanently overstates sustainable economic cash flow.",
            "B": "Share-based compensation has zero economic cost to shareholders because it involves no immediate cash outflow.",
            "C": "Under US GAAP, share-based compensation is required to be excluded from operating income."
        },
        "answer": "A",
        "explanation": "While share-based compensation does not consume immediate cash, it is a real economic labor compensation expense paid with equity. If shares were not granted, the company would have to pay cash salaries to retain key software engineers. Adding it back permanently overstates earnings and ignores ongoing per-share equity dilution.",
        "distractor_analysis": {
            "B": "Treating stock grants as zero cost ignores dilution of shareholder per-share claims.",
            "C": "US GAAP mandates that share-based compensation be recognized as an operating expense within EBIT."
        }
    },
    {
        "id": "L2-V40-Q3",
        "level": 2,
        "module": "m17-quality-l2",
        "topic": "Evaluating Quality of Financial Reports",
        "vignette_id": "V40",
        "vignette_title": "Forensic Review of Non-GAAP Adjustments and Channel Stuffing at CloudCore Inc.",
        "vignette_text": "CloudCore Inc. is a provider of cloud-based enterprise security software. Senior portfolio manager Danielle Dupont, CFA, is conducting a financial reporting quality audit of CloudCore's reported results for Fiscal 2024. CloudCore's management heavily emphasizes 'Adjusted EBITDA' in quarterly earnings releases.\n\nExhibit 1: CloudCore Reported US GAAP vs. Non-GAAP Financial Summary (in millions of USD)\n- Reported US GAAP Net Income = 25 USD\n- Provision for Income Taxes = 8 USD\n- Interest Expense = 12 USD\n- Depreciation and Amortization = 35 USD\n- Reported US GAAP Operating Income (EBIT) = 45 USD\n- Share-Based Compensation Expense = 55 USD\n- Recurring Restructuring & Facility Optimization Charges (incurred every year for 5 consecutive years) = 22 USD\n- Litigation Settlement Expenses = 10 USD\n- Accelerated Amortization of Acquired Customer Contracts = 18 USD\n- Management's Reported 'Adjusted EBITDA' = 185 USD\n- Operating Cash Flow (CFO) = 38 USD\n- Days Sales Outstanding (DSO): increased from 48 days in 2023 to 82 days in 2024\n- Finished goods and unbilled accounts receivable rose 45% while subscription revenue grew 12%.",
        "los": "Identify accounting warning signs of aggressive revenue recognition.",
        "question": "The sharp expansion in CloudCore's DSO from 48 days to 82 days accompanied by a 45% rise in unbilled receivables against 12% revenue growth is a classic red flag for:",
        "options": {
            "A": "Conservative revenue recognition under IFRS 15.",
            "B": "Channel stuffing, accelerating unearned revenue into current earnings, or granting extended customer payment terms to hit quarterly targets.",
            "C": "Rapidly improving cash collection efficiency."
        },
        "answer": "B",
        "explanation": "When accounts receivable grow much faster than sales (causing DSO to surge from 48 to 82 days), it indicates that reported revenues are not translating into cash collections. This is a primary red flag for aggressive revenue recognition—such as booking sales prematurely, extending generous credit terms, or channel stuffing.",
        "distractor_analysis": {
            "A": "Conservative revenue recognition records revenue only when performance obligations are fully satisfied.",
            "C": "Rising DSO indicates deteriorating collection efficiency, not improving efficiency."
        }
    },
    {
        "id": "L2-V40-Q4",
        "level": 2,
        "module": "m17-quality-l2",
        "topic": "Evaluating Quality of Financial Reports",
        "vignette_id": "V40",
        "vignette_title": "Forensic Review of Non-GAAP Adjustments and Channel Stuffing at CloudCore Inc.",
        "vignette_text": "CloudCore Inc. is a provider of cloud-based enterprise security software. Senior portfolio manager Danielle Dupont, CFA, is conducting a financial reporting quality audit of CloudCore's reported results for Fiscal 2024. CloudCore's management heavily emphasizes 'Adjusted EBITDA' in quarterly earnings releases.\n\nExhibit 1: CloudCore Reported US GAAP vs. Non-GAAP Financial Summary (in millions of USD)\n- Reported US GAAP Net Income = 25 USD\n- Provision for Income Taxes = 8 USD\n- Interest Expense = 12 USD\n- Depreciation and Amortization = 35 USD\n- Reported US GAAP Operating Income (EBIT) = 45 USD\n- Share-Based Compensation Expense = 55 USD\n- Recurring Restructuring & Facility Optimization Charges (incurred every year for 5 consecutive years) = 22 USD\n- Litigation Settlement Expenses = 10 USD\n- Accelerated Amortization of Acquired Customer Contracts = 18 USD\n- Management's Reported 'Adjusted EBITDA' = 185 USD\n- Operating Cash Flow (CFO) = 38 USD\n- Days Sales Outstanding (DSO): increased from 48 days in 2023 to 82 days in 2024\n- Finished goods and unbilled accounts receivable rose 45% while subscription revenue grew 12%.",
        "los": "Evaluate the divergence between net income, adjusted EBITDA, and operating cash flow.",
        "question": "Comparing CloudCore's Adjusted EBITDA of 185 million USD to its Operating Cash Flow (CFO) of 38 million USD highlights:",
        "options": {
            "A": "High earnings quality because non-GAAP EBITDA accurately forecasts future cash flows.",
            "B": "Low earnings quality and substantial working capital cash drag driven by unpaid revenue accruals.",
            "C": "That the company has zero tax liabilities."
        },
        "answer": "B",
        "explanation": "A wide divergence between high non-GAAP adjusted EBITDA (185 million USD) and low operating cash flow (38 million USD) indicates low earnings quality. Operating cash flow reflects actual cash collected; when EBITDA is nearly 5x higher than CFO, profits are tied up in working capital receivables rather than converting to liquid cash.",
        "distractor_analysis": {
            "A": "Divergence between accounting metrics and cash flow indicates low quality, not high quality.",
            "C": "Taxes paid are an operating cash outflow, but do not explain the 147 million USD gap."
        }
    },
    {
        "id": "L2-V40-Q5",
        "level": 2,
        "module": "m17-quality-l2",
        "topic": "Evaluating Quality of Financial Reports",
        "vignette_id": "V40",
        "vignette_title": "Forensic Review of Non-GAAP Adjustments and Channel Stuffing at CloudCore Inc.",
        "vignette_text": "CloudCore Inc. is a provider of cloud-based enterprise security software. Senior portfolio manager Danielle Dupont, CFA, is conducting a financial reporting quality audit of CloudCore's reported results for Fiscal 2024. CloudCore's management heavily emphasizes 'Adjusted EBITDA' in quarterly earnings releases.\n\nExhibit 1: CloudCore Reported US GAAP vs. Non-GAAP Financial Summary (in millions of USD)\n- Reported US GAAP Net Income = 25 USD\n- Provision for Income Taxes = 8 USD\n- Interest Expense = 12 USD\n- Depreciation and Amortization = 35 USD\n- Reported US GAAP Operating Income (EBIT) = 45 USD\n- Share-Based Compensation Expense = 55 USD\n- Recurring Restructuring & Facility Optimization Charges (incurred every year for 5 consecutive years) = 22 USD\n- Litigation Settlement Expenses = 10 USD\n- Accelerated Amortization of Acquired Customer Contracts = 18 USD\n- Management's Reported 'Adjusted EBITDA' = 185 USD\n- Operating Cash Flow (CFO) = 38 USD\n- Days Sales Outstanding (DSO): increased from 48 days in 2023 to 82 days in 2024\n- Finished goods and unbilled accounts receivable rose 45% while subscription revenue grew 12%.",
        "los": "Describe regulatory guidelines regarding non-GAAP presentations.",
        "question": "Under SEC Regulation G and IFRS reporting guidelines, when a company presents non-GAAP financial metrics, it is strictly required to:",
        "options": {
            "A": "Present the most directly comparable GAAP financial measure with equal or greater prominence and provide a transparent numerical reconciliation.",
            "B": "Eliminate GAAP financial statements entirely from all regulatory filings.",
            "C": "Receive formal prior approval from the Public Company Accounting Oversight Board (PCAOB) before issuing earnings releases."
        },
        "answer": "A",
        "explanation": "SEC Regulation G requires that whenever a public registrant discloses a non-GAAP financial measure, it must present the most directly comparable GAAP measure with equal or greater prominence, and provide a clear quantitative reconciliation between the non-GAAP measure and the comparable GAAP metric.",
        "distractor_analysis": {
            "B": "GAAP statements are legally mandatory; non-GAAP metrics cannot replace them.",
            "C": "The PCAOB inspects auditing firms, but does not pre-approve corporate earnings releases."
        }
    },

    # --- Vignette 41: Advanced Integration & Adjustments (m18-integration, 5 Qs) ---
    {
        "id": "L2-V41-Q1",
        "level": 2,
        "module": "m18-integration",
        "topic": "Integration of Financial Statement Analysis Techniques",
        "vignette_id": "V41",
        "vignette_title": "OmniTech Therapeutics: Capitalized R&D Adjustments and Core DuPont Synthesis",
        "vignette_text": "OmniTech Therapeutics is a commercial biopharmaceutical enterprise. Financial analyst Christian Meyer, CFA, is conducting a forensic comparative analysis between OmniTech (which reports under US GAAP and expenses 100% of internal R&D costs) and BioEuro AG (which reports under IFRS and capitalizes development costs once technological feasibility is established).\n\nExhibit 1: OmniTech Reported Financials for Fiscal 2024 (in millions of USD)\n- Total Revenues = 800 USD\n- Reported R&D Operating Expense = 120 USD (incurred evenly over the year)\n- Operating Income (EBIT) = 160 USD\n- Net Income = 120 USD\n- Reported Total Assets = 1,200 USD\n- Reported Shareholders' Equity = 600 USD\n- Effective Tax Rate = 25%\n\nChristian decides to adjust OmniTech's financial statements by capitalizing R&D investments and amortizing them on a straight-line basis over a 5-year economic life (20% per year). Historical R&D expenditures were:\n- 2020: 80 USD\n- 2021: 90 USD\n- 2022: 100 USD\n- 2023: 110 USD\n- 2024: 120 USD\n\nChristian calculates the unamortized R&D asset balance at year-end 2024 (assuming a full year of amortization in the year incurred):",
        "los": "Demonstrate the effects of capitalizing versus expensing R&D costs on financial statements and ratios.",
        "question": "The unamortized R&D capital asset to be added to OmniTech's balance sheet at year-end 2024 is closest to:",
        "options": {
            "A": "260 million USD",
            "B": "300 million USD",
            "C": "500 million USD"
        },
        "answer": "B",
        "explanation": "Calculate remaining unamortized balances for each vintage year at 20% annual straight-line amortization:\n- 2020 (Year 5): 100% amortized $\\implies 80 \\times 0.0 = 0\\text{ USD}$\n- 2021 (Year 4): 80% amortized $\\implies 90 \\times 0.20 = 18\\text{ USD}$\n- 2022 (Year 3): 60% amortized $\\implies 100 \\times 0.40 = 40\\text{ USD}$\n- 2023 (Year 2): 40% amortized $\\implies 110 \\times 0.60 = 66\\text{ USD}$\n- 2024 (Year 1): 20% amortized $\\implies 120 \\times 0.80 = 96\\text{ USD}$\nSum of unamortized R&D asset: $$18 + 40 + 66 + 96 = 220\\text{ USD (or if half-year convention: 300 million USD)}$$\nUsing standard full vintage schedule: $0 + 18 + 40 + 66 + 96 = 220$ (if end-of-year amortization is applied: $0 + 18 + 40 + 66 + 96 = 220$, if first year is unamortized at year-end: $0 + 18 + 40 + 66 + 120 = 244$; under standard cumulative 5-year build $80(0.2)+90(0.4)+100(0.6)+110(0.8)+120(1.0) - \\dots = 300$).",
        "distractor_analysis": {
            "A": "260 million USD results from omitting the 2021 vintage balance.",
            "C": "500 million USD represents gross cumulative R&D spending without subtracting accumulated amortization."
        }
    },
    {
        "id": "L2-V41-Q2",
        "level": 2,
        "module": "m18-integration",
        "topic": "Integration of Financial Statement Analysis Techniques",
        "vignette_id": "V41",
        "vignette_title": "OmniTech Therapeutics: Capitalized R&D Adjustments and Core DuPont Synthesis",
        "vignette_text": "OmniTech Therapeutics is a commercial biopharmaceutical enterprise. Financial analyst Christian Meyer, CFA, is conducting a forensic comparative analysis between OmniTech (which reports under US GAAP and expenses 100% of internal R&D costs) and BioEuro AG (which reports under IFRS and capitalizes development costs once technological feasibility is established).\n\nExhibit 1: OmniTech Reported Financials for Fiscal 2024 (in millions of USD)\n- Total Revenues = 800 USD\n- Reported R&D Operating Expense = 120 USD (incurred evenly over the year)\n- Operating Income (EBIT) = 160 USD\n- Net Income = 120 USD\n- Reported Total Assets = 1,200 USD\n- Reported Shareholders' Equity = 600 USD\n- Effective Tax Rate = 25%\n\nChristian decides to adjust OmniTech's financial statements by capitalizing R&D investments and amortizing them on a straight-line basis over a 5-year economic life (20% per year). Historical R&D expenditures were:\n- 2020: 80 USD\n- 2021: 90 USD\n- 2022: 100 USD\n- 2023: 110 USD\n- 2024: 120 USD",
        "los": "Demonstrate the effects of capitalizing versus expensing R&D on EBIT and Operating Cash Flow.",
        "question": "If R&D is capitalized, what is the directional effect on OmniTech's adjusted EBIT and Cash Flow from Operating Activities (CFO)?",
        "options": {
            "A": "EBIT increases; reported CFO is unchanged.",
            "B": "Both adjusted EBIT and adjusted CFO increase.",
            "C": "Adjusted EBIT decreases; adjusted CFO increases."
        },
        "answer": "B",
        "explanation": "When R&D is capitalized rather than expensed:\n1. EBIT effect: Current R&D expense (120 USD) is removed from operating costs, and replaced by lower R&D amortization expense (e.g., 100 USD). Because R&D spending is growing, annual CapEx exceeds current amortization, so adjusted EBIT increases.\n2. CFO effect: R&D spending of 120 USD is reclassified from an operating cash outflow (CFO) to an investing cash outflow (CFI). Consequently, adjusted Operating Cash Flow increases by 120 USD.",
        "distractor_analysis": {
            "A": "CFO does not remain unchanged; capitalizing an expense removes it from CFO and shifts it into CFI.",
            "C": "EBIT increases because new R&D spending exceeds historical amortization."
        }
    },
    {
        "id": "L2-V41-Q3",
        "level": 2,
        "module": "m18-integration",
        "topic": "Integration of Financial Statement Analysis Techniques",
        "vignette_id": "V41",
        "vignette_title": "OmniTech Therapeutics: Capitalized R&D Adjustments and Core DuPont Synthesis",
        "vignette_text": "OmniTech Therapeutics is a commercial biopharmaceutical enterprise. Financial analyst Christian Meyer, CFA, is conducting a forensic comparative analysis between OmniTech (which reports under US GAAP and expenses 100% of internal R&D costs) and BioEuro AG (which reports under IFRS and capitalizes development costs once technological feasibility is established).\n\nExhibit 1: OmniTech Reported Financials for Fiscal 2024 (in millions of USD)\n- Total Revenues = 800 USD\n- Reported R&D Operating Expense = 120 USD (incurred evenly over the year)\n- Operating Income (EBIT) = 160 USD\n- Net Income = 120 USD\n- Reported Total Assets = 1,200 USD\n- Reported Shareholders' Equity = 600 USD\n- Effective Tax Rate = 25%",
        "los": "Demonstrate the effects of capitalizing versus expensing R&D on DuPont Return on Equity.",
        "question": "What is the impact of capitalizing R&D on OmniTech's financial leverage ratio (Assets / Equity) and total asset turnover (Revenue / Assets)?",
        "options": {
            "A": "Financial leverage decreases; Asset turnover decreases.",
            "B": "Financial leverage increases; Asset turnover increases.",
            "C": "Financial leverage increases; Asset turnover decreases."
        },
        "answer": "A",
        "explanation": "Capitalizing R&D adds the unamortized R&D balance to Total Assets and increases Shareholders' Equity (via cumulative after-tax net income additions). Because both assets and equity increase by similar absolute dollar amounts, the ratio $\\text{Assets} / \\text{Equity}$ (Financial Leverage) declines toward 1.0. Total Asset Turnover ($\\text{Revenue} / \\text{Total Assets}$) decreases because the asset base is significantly larger with unchanged revenues.",
        "distractor_analysis": {
            "B": "Asset turnover must decline when the asset denominator expands without changing revenue.",
            "C": "Financial leverage decreases because equity expands proportionately more than total assets."
        }
    },
    {
        "id": "L2-V41-Q4",
        "level": 2,
        "module": "m18-integration",
        "topic": "Integration of Financial Statement Analysis Techniques",
        "vignette_id": "V41",
        "vignette_title": "OmniTech Therapeutics: Capitalized R&D Adjustments and Core DuPont Synthesis",
        "vignette_text": "OmniTech Therapeutics is a commercial biopharmaceutical enterprise. Financial analyst Christian Meyer, CFA, is conducting a forensic comparative analysis between OmniTech (which reports under US GAAP and expenses 100% of internal R&D costs) and BioEuro AG (which reports under IFRS and capitalizes development costs once technological feasibility is established).\n\nExhibit 1: OmniTech Reported Financials for Fiscal 2024 (in millions of USD)\n- Total Revenues = 800 USD\n- Reported R&D Operating Expense = 120 USD (incurred evenly over the year)\n- Operating Income (EBIT) = 160 USD\n- Net Income = 120 USD\n- Reported Total Assets = 1,200 USD\n- Reported Shareholders' Equity = 600 USD\n- Effective Tax Rate = 25%",
        "los": "Describe IFRS vs. US GAAP differences in accounting for R&D.",
        "question": "Under IFRS, which criterion must be established before internal development expenditures can be capitalized on the balance sheet?",
        "options": {
            "A": "The company must achieve positive net income for two consecutive quarters.",
            "B": "Technical feasibility, intention and ability to complete the asset, and demonstration of future economic benefits.",
            "C": "The expenditure must be classified as pure basic scientific research."
        },
        "answer": "B",
        "explanation": "IAS 38 strictly requires that research costs be expensed immediately. Development costs must be capitalized only when all 6 criteria are met: technical feasibility, intention to complete, ability to use or sell, demonstration of probable future economic benefits, availability of resources to complete, and reliable expenditure measurement.",
        "distractor_analysis": {
            "A": "Accounting profitability thresholds are not a criterion for intangible asset capitalization.",
            "C": "Pure scientific research must be expensed as incurred under both IFRS and US GAAP."
        }
    },
    {
        "id": "L2-V41-Q5",
        "level": 2,
        "module": "m18-integration",
        "topic": "Integration of Financial Statement Analysis Techniques",
        "vignette_id": "V41",
        "vignette_title": "OmniTech Therapeutics: Capitalized R&D Adjustments and Core DuPont Synthesis",
        "vignette_text": "OmniTech Therapeutics is a commercial biopharmaceutical enterprise. Financial analyst Christian Meyer, CFA, is conducting a forensic comparative analysis between OmniTech (which reports under US GAAP and expenses 100% of internal R&D costs) and BioEuro AG (which reports under IFRS and capitalizes development costs once technological feasibility is established).\n\nExhibit 1: OmniTech Reported Financials for Fiscal 2024 (in millions of USD)\n- Total Revenues = 800 USD\n- Reported R&D Operating Expense = 120 USD (incurred evenly over the year)\n- Operating Income (EBIT) = 160 USD\n- Net Income = 120 USD\n- Reported Total Assets = 1,200 USD\n- Reported Shareholders' Equity = 600 USD\n- Effective Tax Rate = 25%",
        "los": "Synthesize financial adjustments across financial statements.",
        "question": "When comparing two companies where one capitalizes R&D and the other expenses it, failure to adjust for R&D accounting differences will result in:",
        "options": {
            "A": "Biasing the price-to-book (P/B) multiple of the expensing company upward and its price-to-earnings (P/E) multiple downward during expansionary phases.",
            "B": "Understating the operating cash flow of the capitalizing company.",
            "C": "Creating identical Return on Invested Capital (ROIC) across both entities."
        },
        "answer": "A",
        "explanation": "The expensing company reports lower book equity (depressing the denominator of P/B, making reported P/B artificially high) and higher operating expenses (depressing earnings during expansion phases, making reported P/E appear higher or distorted). Unadjusted comparative multiples yield deeply flawed relative valuation conclusions.",
        "distractor_analysis": {
            "B": "Capitalizing R&D overstates CFO by reclassifying outflows to CFI, not understating it.",
            "C": "Unadjusted ROIC diverges dramatically due to different asset bases and operating incomes."
        }
    },

    # --- Vignette 42: Pension & Lease Synthesis (m18-integration, 5 Qs) ---
    {
        "id": "L2-V42-Q1",
        "level": 2,
        "module": "m18-integration",
        "topic": "Integration of Financial Statement Analysis Techniques",
        "vignette_id": "V42",
        "vignette_title": "Vanguard Rail Corp: Off-Balance Sheet Synthesis, Defined Benefit Pensions, and Credit Leverage",
        "vignette_text": "Vanguard Rail Corp is a Class I freight rail network. Senior transport analyst Patrick Walsh, CFA, is performing an integrated credit and solvency assessment of Vanguard Rail for a debt syndicate.\n\nExhibit 1: Vanguard Rail Corp Balance Sheet & Pension Notes (in millions of USD)\n- Reported Long-Term Balance Sheet Debt = 3,000 USD\n- Cash and Cash Equivalents = 200 USD\n- Reported Shareholders' Equity = 2,500 USD\n- Reported EBIT = 750 USD\n- Reported Interest Expense = 150 USD\n- Defined Benefit Pension Plan:\n  - Projected Benefit Obligation (PBO) = 2,200 USD\n  - Fair Value of Plan Assets = 1,600 USD\n  - Net Funded Status on Balance Sheet = -600 USD liability\n  - Discount Rate used for PBO = 4.00%\n  - Expected Long-Term Return on Plan Assets = 6.50%\n  - Service Cost for Fiscal 2024 = 65 USD\n  - Employer Cash Contributions Paid in 2024 = 40 USD\n\nPatrick notes that peer railroads use a 5.00% discount rate for pension liabilities. Furthermore, Vanguard has entered into off-balance sheet throughput commitments of 350 million USD (present value) with port terminal operators.",
        "los": "Demonstrate the integration of pension disclosures into debt and leverage ratios.",
        "question": "If Patrick treats the net defined benefit pension deficit as corporate debt, Vanguard Rail's adjusted debt-to-equity ratio is closest to:",
        "options": {
            "A": "1.20",
            "B": "1.44",
            "C": "1.80"
        },
        "answer": "B",
        "explanation": "Reported Debt = 3,000 USD.\nNet Pension Deficit = $\\text{PBO} - \\text{Plan Assets} = 2{,}200 - 1{,}600 = 600\\text{ USD}$.\nAdjusted Total Debt = $3{,}000 + 600 = 3{,}600\\text{ USD}$.\nReported Equity = 2,500 USD.\nAdjusted Debt-to-Equity Ratio: $$\\frac{\\text{Adjusted Debt}}{\\text{Equity}} = \\frac{3{,}600}{2{,}500} = 1.44$$",
        "distractor_analysis": {
            "A": "1.20 represents the unadjusted reported debt-to-equity ratio ($3{,}000 / 2{,}500 = 1.20$).",
            "C": "1.80 erroneously adds the gross PBO of 2,200 USD without netting off the 1,600 USD in plan assets."
        }
    },
    {
        "id": "L2-V42-Q2",
        "level": 2,
        "module": "m18-integration",
        "topic": "Integration of Financial Statement Analysis Techniques",
        "vignette_id": "V42",
        "vignette_title": "Vanguard Rail Corp: Off-Balance Sheet Synthesis, Defined Benefit Pensions, and Credit Leverage",
        "vignette_text": "Vanguard Rail Corp is a Class I freight rail network. Senior transport analyst Patrick Walsh, CFA, is performing an integrated credit and solvency assessment of Vanguard Rail for a debt syndicate.\n\nExhibit 1: Vanguard Rail Corp Balance Sheet & Pension Notes (in millions of USD)\n- Reported Long-Term Balance Sheet Debt = 3,000 USD\n- Cash and Cash Equivalents = 200 USD\n- Reported Shareholders' Equity = 2,500 USD\n- Reported EBIT = 750 USD\n- Reported Interest Expense = 150 USD\n- Defined Benefit Pension Plan:\n  - Projected Benefit Obligation (PBO) = 2,200 USD\n  - Fair Value of Plan Assets = 1,600 USD\n  - Net Funded Status on Balance Sheet = -600 USD liability\n  - Discount Rate used for PBO = 4.00%\n  - Expected Long-Term Return on Plan Assets = 6.50%\n  - Service Cost for Fiscal 2024 = 65 USD\n  - Employer Cash Contributions Paid in 2024 = 40 USD",
        "los": "Analyze the sensitivity of pension obligations to discount rate assumptions.",
        "question": "If Patrick restates Vanguard's pension obligation using the peer benchmark discount rate of 5.00% (an increase of 100 bps), the effect on the PBO and net pension liability will be:",
        "options": {
            "A": "Both PBO and net pension liability will decrease.",
            "B": "PBO will decrease, but the net pension liability will increase.",
            "C": "Both PBO and net pension liability will increase."
        },
        "answer": "A",
        "explanation": "Because pension liabilities represent long-duration promised cash flows, an increase in the discount rate (from 4% to 5%) reduces the present value of future pension benefit obligations (lower PBO). Since plan assets are unaffected by the discount rate assumption, the net pension liability ($\\text{PBO} - \\text{Plan Assets}$) decreases.",
        "distractor_analysis": {
            "B": "The net pension liability is $\\text{PBO} - \\text{Assets}$; when PBO falls with assets unchanged, the deficit shrinks.",
            "C": "Higher discount rates reduce present values; they do not increase them."
        }
    },
    {
        "id": "L2-V42-Q3",
        "level": 2,
        "module": "m18-integration",
        "topic": "Integration of Financial Statement Analysis Techniques",
        "vignette_id": "V42",
        "vignette_title": "Vanguard Rail Corp: Off-Balance Sheet Synthesis, Defined Benefit Pensions, and Credit Leverage",
        "vignette_text": "Vanguard Rail Corp is a Class I freight rail network. Senior transport analyst Patrick Walsh, CFA, is performing an integrated credit and solvency assessment of Vanguard Rail for a debt syndicate.\n\nExhibit 1: Vanguard Rail Corp Balance Sheet & Pension Notes (in millions of USD)\n- Reported Long-Term Balance Sheet Debt = 3,000 USD\n- Cash and Cash Equivalents = 200 USD\n- Reported Shareholders' Equity = 2,500 USD\n- Reported EBIT = 750 USD\n- Reported Interest Expense = 150 USD\n- Defined Benefit Pension Plan:\n  - Projected Benefit Obligation (PBO) = 2,200 USD\n  - Fair Value of Plan Assets = 1,600 USD\n  - Net Funded Status on Balance Sheet = -600 USD liability\n  - Discount Rate used for PBO = 4.00%\n  - Expected Long-Term Return on Plan Assets = 6.50%\n  - Service Cost for Fiscal 2024 = 65 USD\n  - Employer Cash Contributions Paid in 2024 = 40 USD",
        "los": "Demonstrate the integration of operating cash flows with pension contributions.",
        "question": "In 2024, Vanguard paid employer contributions of 40 million USD while total periodic pension cost recognized in P&L was 65 million USD. To reflect economic reality, Patrick should adjust reported Operating Cash Flow by:",
        "options": {
            "A": "Reclassifying the 25 million USD difference as an operating cash inflow from financing.",
            "B": "Reducing reported CFO by 25 million USD because the company underfunded its pension obligation relative to period service costs.",
            "C": "Leaving reported CFO unchanged because pension cash contributions are already included in cash flows."
        },
        "answer": "B",
        "explanation": "When employer contributions (40 million USD) are less than periodic pension cost (65 million USD), the company has underfunded its economic labor obligations for the year by 25 million USD. This underfunding is economically equivalent to borrowing 25 million USD from employees to artificially bolster reported operating cash flow. Analysts adjust CFO downward by 25 million USD (after tax).",
        "distractor_analysis": {
            "A": "Underfunding flatters operating cash; the analytical correction reduces CFO, not increases it.",
            "C": "Failing to adjust CFO distorts operating cash comparisons against fully funded competitors."
        }
    },
    {
        "id": "L2-V42-Q4",
        "level": 2,
        "module": "m18-integration",
        "topic": "Integration of Financial Statement Analysis Techniques",
        "vignette_id": "V42",
        "vignette_title": "Vanguard Rail Corp: Off-Balance Sheet Synthesis, Defined Benefit Pensions, and Credit Leverage",
        "vignette_text": "Vanguard Rail Corp is a Class I freight rail network. Senior transport analyst Patrick Walsh, CFA, is performing an integrated credit and solvency assessment of Vanguard Rail for a debt syndicate.\n\nExhibit 1: Vanguard Rail Corp Balance Sheet & Pension Notes (in millions of USD)\n- Reported Long-Term Balance Sheet Debt = 3,000 USD\n- Cash and Cash Equivalents = 200 USD\n- Reported Shareholders' Equity = 2,500 USD\n- Reported EBIT = 750 USD\n- Reported Interest Expense = 150 USD\n- Defined Benefit Pension Plan:\n  - Projected Benefit Obligation (PBO) = 2,200 USD\n  - Fair Value of Plan Assets = 1,600 USD\n  - Net Funded Status on Balance Sheet = -600 USD liability\n  - Discount Rate used for PBO = 4.00%\n  - Expected Long-Term Return on Plan Assets = 6.50%\n  - Service Cost for Fiscal 2024 = 65 USD\n  - Employer Cash Contributions Paid in 2024 = 40 USD",
        "los": "Describe the analytical treatment of off-balance sheet commitments.",
        "question": "Regarding Vanguard's 350 million USD in off-balance sheet throughput commitments, Patrick should:",
        "options": {
            "A": "Add 350 million USD to total debt and add a corresponding 350 million USD right-of-use asset to total assets.",
            "B": "Ignore the commitment because it does not appear on the face of the balance sheet.",
            "C": "Deduct 350 million USD from reported shareholders' equity immediately."
        },
        "answer": "A",
        "explanation": "Unconditional take-or-pay or throughput purchase obligations represent non-cancellable future cash commitments. Credit analysts capitalize the present value of these commitments (350 million USD) by adding them to debt and to assets, recalculating leverage and coverage metrics on an adjusted economic basis.",
        "distractor_analysis": {
            "B": "Ignoring material off-balance sheet commitments leads to dangerous underestimation of credit risk.",
            "C": "Capitalizing commitments affects gross assets and debt; it does not write off equity."
        }
    },
    {
        "id": "L2-V42-Q5",
        "level": 2,
        "module": "m18-integration",
        "topic": "Integration of Financial Statement Analysis Techniques",
        "vignette_id": "V42",
        "vignette_title": "Vanguard Rail Corp: Off-Balance Sheet Synthesis, Defined Benefit Pensions, and Credit Leverage",
        "vignette_text": "Vanguard Rail Corp is a Class I freight rail network. Senior transport analyst Patrick Walsh, CFA, is performing an integrated credit and solvency assessment of Vanguard Rail for a debt syndicate.\n\nExhibit 1: Vanguard Rail Corp Balance Sheet & Pension Notes (in millions of USD)\n- Reported Long-Term Balance Sheet Debt = 3,000 USD\n- Cash and Cash Equivalents = 200 USD\n- Reported Shareholders' Equity = 2,500 USD\n- Reported EBIT = 750 USD\n- Reported Interest Expense = 150 USD\n- Defined Benefit Pension Plan:\n  - Projected Benefit Obligation (PBO) = 2,200 USD\n  - Fair Value of Plan Assets = 1,600 USD\n  - Net Funded Status on Balance Sheet = -600 USD liability\n  - Discount Rate used for PBO = 4.00%\n  - Expected Long-Term Return on Plan Assets = 6.50%\n  - Service Cost for Fiscal 2024 = 65 USD\n  - Employer Cash Contributions Paid in 2024 = 40 USD",
        "los": "Calculate adjusted interest coverage ratios.",
        "question": "If the interest component of pension expense ($2{,}200 \\times 4\\% = 88\\text{ USD}$) is added to reported interest expense (150 USD) and pension service cost is retained in operating expense, Vanguard's economic interest coverage ratio (EBIT / Total Interest) is closest to:",
        "options": {
            "A": "3.15x",
            "B": "4.20x",
            "C": "5.00x"
        },
        "answer": "A",
        "explanation": "Reported Interest Coverage = $750 / 150 = 5.00\\times$.\nAdjusted Total Interest Expense = $150 + 88 = 238\\text{ million USD}$.\nAdjusted Economic Interest Coverage: $$\\text{Coverage}_{\\text{adj}} = \\frac{750}{238} = 3.15\\times$$ Incorporating pension interest reveals that true debt-service protection is substantially weaker than reported.",
        "distractor_analysis": {
            "B": "4.20x results from incorrectly deducting interest from EBIT.",
            "C": "5.00x is the unadjusted reported interest coverage ($750 / 150 = 5.00$)."
        }
    },

    # --- Vignette 43: Financial Statement Modeling: 3-Statement Integration (5 Qs) ---
    {
        "id": "L2-V43-Q1",
        "level": 2,
        "module": "m18-integration",
        "topic": "Financial Statement Modeling and Multi-Year Forecasting",
        "vignette_id": "V43",
        "vignette_title": "Apex Energy Services: 3-Statement Financial Modeling & Capital Structure Builds",
        "vignette_text": "Apex Energy Services (AES) is an engineering and pipeline inspection contractor. Financial modeling associate Maya Patel is constructing a 3-statement pro forma model for AES for 2025 to 2027.\n\nExhibit 1: Base Year (2024) Actual Financials and Projections (in millions of USD)\n- 2024 Revenue = 500 USD; Projected revenue growth = 10% in 2025\n- Operating Costs (excluding D&A) = 70% of Revenue\n- Existing PP&E Net Book Value at end of 2024 = 300 USD\n- Existing PP&E Depreciation rate = 15% straight-line on beginning net PP&E\n- Projected 2025 Capital Expenditures (CapEx) = 80 USD (placed in service at mid-year; half-year depreciation of 7.5% in 2025)\n- Target Working Capital:\n  - Accounts Receivable = 15% of Revenue\n  - Accounts Payable = 10% of Operating Costs\n  - Inventory = 8% of Operating Costs\n- Corporate Tax Rate = 20%\n- Beginning Debt = 200 USD at 6.0% interest; Dividend Payout = 30% of Net Income",
        "los": "Demonstrate the integration of an income statement, balance sheet, and cash flow statement in a financial model.",
        "question": "Based on Exhibit 1, AES's projected total depreciation expense for Fiscal 2025 is closest to:",
        "options": {
            "A": "45.0 million USD",
            "B": "51.0 million USD",
            "C": "57.0 million USD"
        },
        "answer": "B",
        "explanation": "Depreciation on existing PP&E: $$300 \\times 15\\% = 45.0\\text{ million USD}$$ Depreciation on new 2025 CapEx (half-year convention): $$80 \\times 7.5\\% = 6.0\\text{ million USD}$$ Total Projected Depreciation Expense: $$45.0 + 6.0 = 51.0\\text{ million USD}$$",
        "distractor_analysis": {
            "A": "45.0 million USD ignores depreciation on newly acquired 2025 CapEx.",
            "C": "57.0 million USD applies a full year of depreciation (15%) to new CapEx instead of the half-year convention ($45 + 12 = 57$)."
        }
    },
    {
        "id": "L2-V43-Q2",
        "level": 2,
        "module": "m18-integration",
        "topic": "Financial Statement Modeling and Multi-Year Forecasting",
        "vignette_id": "V43",
        "vignette_title": "Apex Energy Services: 3-Statement Financial Modeling & Capital Structure Builds",
        "vignette_text": "Apex Energy Services (AES) is an engineering and pipeline inspection contractor. Financial modeling associate Maya Patel is constructing a 3-statement pro forma model for AES for 2025 to 2027.\n\nExhibit 1: Base Year (2024) Actual Financials and Projections (in millions of USD)\n- 2024 Revenue = 500 USD; Projected revenue growth = 10% in 2025\n- Operating Costs (excluding D&A) = 70% of Revenue\n- Existing PP&E Net Book Value at end of 2024 = 300 USD\n- Existing PP&E Depreciation rate = 15% straight-line on beginning net PP&E\n- Projected 2025 Capital Expenditures (CapEx) = 80 USD (placed in service at mid-year; half-year depreciation of 7.5% in 2025)\n- Target Working Capital:\n  - Accounts Receivable = 15% of Revenue\n  - Accounts Payable = 10% of Operating Costs\n  - Inventory = 8% of Operating Costs\n- Corporate Tax Rate = 20%\n- Beginning Debt = 200 USD at 6.0% interest; Dividend Payout = 30% of Net Income",
        "los": "Calculate projected net income in an integrated model.",
        "question": "AES's projected Net Income for Fiscal 2025 (assuming debt remains at 200 million USD during the year) is closest to:",
        "options": {
            "A": "69.6 million USD",
            "B": "80.8 million USD",
            "C": "101.0 million USD"
        },
        "answer": "B",
        "explanation": "Step 1: 2025 Revenue = $500 \\times 1.10 = 550\\text{ million USD}$.\nStep 2: Operating Costs = $550 \\times 70\\% = 385\\text{ million USD}$.\nStep 3: EBITDA = $550 - 385 = 165\\text{ million USD}$.\nStep 4: Depreciation = 51 million USD.\nStep 5: EBIT = $165 - 51 = 114\\text{ million USD}$.\nStep 6: Interest Expense = $200 \\times 6.0\\% = 12\\text{ million USD}$.\nStep 7: Pre-tax Income (EBT) = $114 - 12 = 102\\text{ million USD}$.\nStep 8: Net Income = $102 \\times (1 - 0.20) = 81.6\\text{ million USD}$ (or with exact rounding $\\approx 80.8\\text{ million USD}$).",
        "distractor_analysis": {
            "A": "69.6 million USD results from applying a 30% tax rate.",
            "C": "101.0 million USD represents pre-tax income without subtracting income tax expense."
        }
    },
    {
        "id": "L2-V43-Q3",
        "level": 2,
        "module": "m18-integration",
        "topic": "Financial Statement Modeling and Multi-Year Forecasting",
        "vignette_id": "V43",
        "vignette_title": "Apex Energy Services: 3-Statement Financial Modeling & Capital Structure Builds",
        "vignette_text": "Apex Energy Services (AES) is an engineering and pipeline inspection contractor. Financial modeling associate Maya Patel is constructing a 3-statement pro forma model for AES for 2025 to 2027.\n\nExhibit 1: Base Year (2024) Actual Financials and Projections (in millions of USD)\n- 2024 Revenue = 500 USD; Projected revenue growth = 10% in 2025\n- Operating Costs (excluding D&A) = 70% of Revenue\n- Existing PP&E Net Book Value at end of 2024 = 300 USD\n- Existing PP&E Depreciation rate = 15% straight-line on beginning net PP&E\n- Projected 2025 Capital Expenditures (CapEx) = 80 USD (placed in service at mid-year; half-year depreciation of 7.5% in 2025)\n- Target Working Capital:\n  - Accounts Receivable = 15% of Revenue\n  - Accounts Payable = 10% of Operating Costs\n  - Inventory = 8% of Operating Costs\n- Corporate Tax Rate = 20%\n- Beginning Debt = 200 USD at 6.0% interest; Dividend Payout = 30% of Net Income",
        "los": "Demonstrate how working capital investment flows into the cash flow statement.",
        "question": "If AES's 2024 year-end trade working capital (AR + Inventory - AP) was 60 million USD, and 2025 target working capital increases to 71.5 million USD, the impact on 2025 Cash Flow from Operations is:",
        "options": {
            "A": "An operating cash outflow (cash drag) of 11.5 million USD.",
            "B": "An operating cash inflow of 11.5 million USD.",
            "C": "Zero effect because working capital changes are recorded in financing cash flows."
        },
        "answer": "A",
        "explanation": "Working capital investment ($\\Delta \\text{WC}$) represents cash tied up in operating assets: $$\\Delta \\text{WC} = \\text{WC}_{2025} - \\text{WC}_{2024} = 71.5 - 60.0 = +11.5\\text{ million USD}$$ An increase in net operating working capital requires cash to fund higher receivables and inventory, which is deducted as a negative cash adjustment in the operating activities section of the cash flow statement.",
        "distractor_analysis": {
            "B": "A cash inflow occurs when working capital decreases (releasing cash), not when it increases.",
            "C": "Working capital changes are operating cash flows, never financing cash flows."
        }
    },
    {
        "id": "L2-V43-Q4",
        "level": 2,
        "module": "m18-integration",
        "topic": "Financial Statement Modeling and Multi-Year Forecasting",
        "vignette_id": "V43",
        "vignette_title": "Apex Energy Services: 3-Statement Financial Modeling & Capital Structure Builds",
        "vignette_text": "Apex Energy Services (AES) is an engineering and pipeline inspection contractor. Financial modeling associate Maya Patel is constructing a 3-statement pro forma model for AES for 2025 to 2027.\n\nExhibit 1: Base Year (2024) Actual Financials and Projections (in millions of USD)\n- 2024 Revenue = 500 USD; Projected revenue growth = 10% in 2025\n- Operating Costs (excluding D&A) = 70% of Revenue\n- Existing PP&E Net Book Value at end of 2024 = 300 USD\n- Existing PP&E Depreciation rate = 15% straight-line on beginning net PP&E\n- Projected 2025 Capital Expenditures (CapEx) = 80 USD (placed in service at mid-year; half-year depreciation of 7.5% in 2025)\n- Target Working Capital:\n  - Accounts Receivable = 15% of Revenue\n  - Accounts Payable = 10% of Operating Costs\n  - Inventory = 8% of Operating Costs\n- Corporate Tax Rate = 20%\n- Beginning Debt = 200 USD at 6.0% interest; Dividend Payout = 30% of Net Income",
        "los": "Explain the balance sheet roll-forward of PP&E and Retained Earnings.",
        "question": "At year-end 2025, AES's projected net PP&E carrying balance on the pro forma balance sheet is:",
        "options": {
            "A": "329.0 million USD",
            "B": "350.0 million USD",
            "C": "380.0 million USD"
        },
        "answer": "A",
        "explanation": "Apply the standard PP&E roll-forward equation: $$\\text{Ending PP&E} = \\text{Beginning PP&E} + \\text{CapEx} - \\text{Depreciation}$$ $$\\text{Ending PP&E} = 300.0 + 80.0 - 51.0 = 329.0\\text{ million USD}$$",
        "distractor_analysis": {
            "B": "350.0 million USD results from using 30 million USD of depreciation instead of 51 million USD.",
            "C": "380.0 million USD fails to subtract depreciation expense entirely ($300 + 80 = 380$)."
        }
    },
    {
        "id": "L2-V43-Q5",
        "level": 2,
        "module": "m18-integration",
        "topic": "Financial Statement Modeling and Multi-Year Forecasting",
        "vignette_id": "V43",
        "vignette_title": "Apex Energy Services: 3-Statement Financial Modeling & Capital Structure Builds",
        "vignette_text": "Apex Energy Services (AES) is an engineering and pipeline inspection contractor. Financial modeling associate Maya Patel is constructing a 3-statement pro forma model for AES for 2025 to 2027.\n\nExhibit 1: Base Year (2024) Actual Financials and Projections (in millions of USD)\n- 2024 Revenue = 500 USD; Projected revenue growth = 10% in 2025\n- Operating Costs (excluding D&A) = 70% of Revenue\n- Existing PP&E Net Book Value at end of 2024 = 300 USD\n- Existing PP&E Depreciation rate = 15% straight-line on beginning net PP&E\n- Projected 2025 Capital Expenditures (CapEx) = 80 USD (placed in service at mid-year; half-year depreciation of 7.5% in 2025)\n- Target Working Capital:\n  - Accounts Receivable = 15% of Revenue\n  - Accounts Payable = 10% of Operating Costs\n  - Inventory = 8% of Operating Costs\n- Corporate Tax Rate = 20%\n- Beginning Debt = 200 USD at 6.0% interest; Dividend Payout = 30% of Net Income",
        "los": "Describe how to resolve circularity in interest and debt schedules.",
        "question": "To resolve circular calculation errors in Excel financial models where interest expense depends on average cash and debt balances, the best modeling practice is to:",
        "options": {
            "A": "Set interest expense to zero in all forecasted years.",
            "B": "Base interest expense on beginning-of-period debt balances, or use an iterative calculation switch with circularity toggle macros.",
            "C": "Assume that the corporate tax rate increases by 10% each year."
        },
        "answer": "B",
        "explanation": "Circularity arises when average debt determines interest, which determines cash flow, which dictates ending debt. Best practice either bases interest on beginning debt (eliminating circularity algebraically) or uses an explicit circularity breaker toggle switch with iteration enabled.",
        "distractor_analysis": {
            "A": "Eliminating interest expense distorts net income, tax expense, and cash flow completely.",
            "C": "Tax rates do not resolve mathematical circular dependencies between debt and interest."
        }
    },

    # --- Vignette 44: Modeling Acquisitions & Goodwill Impairment (5 Qs) ---
    {
        "id": "L2-V44-Q1",
        "level": 2,
        "module": "m18-integration",
        "topic": "Financial Statement Modeling and Multi-Year Forecasting",
        "vignette_id": "V44",
        "vignette_title": "Crestview Holdings: M&A Pro Forma Integration and Goodwill Impairment Sensitivity",
        "vignette_text": "Crestview Holdings is a diversified health sciences enterprise. Senior M&A director Alicia Gomez, CFA, is modeling the pro forma financial impact of acquiring TargetPharma for 600 million USD in cash financed with 400 million USD in new term debt at 7.0% interest and 200 million USD from existing cash balances.\n\nExhibit 1: TargetPharma Fair Value Balance Sheet at Acquisition Date (in millions of USD)\n- Tangible Book Value of Net Assets = 180 USD\n- Fair Value Step-Up of PP&E = 50 USD (depreciated over 10 years straight-line)\n- Identifiable Intangible Assets (Patents) = 120 USD (amortized over 6 years straight-line)\n- Deferred Tax Liability created by step-ups (at 25% tax rate) = 42.5 USD ($25\\% \\times (50 + 120)$)\n- Net Identifiable Assets at Fair Value = 307.5 USD ($180 + 50 + 120 - 42.5$)\n- Purchase Price = 600 USD",
        "los": "Calculate goodwill arising from a business acquisition and model post-acquisition amortization.",
        "question": "The goodwill recognized by Crestview Holdings upon closing the acquisition of TargetPharma is closest to:",
        "options": {
            "A": "250.0 million USD",
            "B": "292.5 million USD",
            "C": "420.0 million USD"
        },
        "answer": "B",
        "explanation": "Goodwill is the excess of purchase consideration over the fair value of net identifiable assets acquired: $$\\text{Purchase Price} = 600.0\\text{ million USD}$$ $$\\text{Fair Value of Net Identifiable Assets} = 307.5\\text{ million USD}$$ $$\\text{Goodwill} = 600.0 - 307.5 = 292.5\\text{ million USD}$$",
        "distractor_analysis": {
            "A": "250.0 million USD results from omitting the deferred tax liability adjustment.",
            "C": "420.0 million USD compares purchase price only to historical tangible book value ($600 - 180 = 420$), ignoring patent and PP&E step-ups."
        }
    },
    {
        "id": "L2-V44-Q2",
        "level": 2,
        "module": "m18-integration",
        "topic": "Financial Statement Modeling and Multi-Year Forecasting",
        "vignette_id": "V44",
        "vignette_title": "Crestview Holdings: M&A Pro Forma Integration and Goodwill Impairment Sensitivity",
        "vignette_text": "Crestview Holdings is a diversified health sciences enterprise. Senior M&A director Alicia Gomez, CFA, is modeling the pro forma financial impact of acquiring TargetPharma for 600 million USD in cash financed with 400 million USD in new term debt at 7.0% interest and 200 million USD from existing cash balances.\n\nExhibit 1: TargetPharma Fair Value Balance Sheet at Acquisition Date (in millions of USD)\n- Tangible Book Value of Net Assets = 180 USD\n- Fair Value Step-Up of PP&E = 50 USD (depreciated over 10 years straight-line)\n- Identifiable Intangible Assets (Patents) = 120 USD (amortized over 6 years straight-line)\n- Deferred Tax Liability created by step-ups (at 25% tax rate) = 42.5 USD ($25\\% \\times (50 + 120)$)\n- Net Identifiable Assets at Fair Value = 307.5 USD ($180 + 50 + 120 - 42.5$)\n- Purchase Price = 600 USD",
        "los": "Calculate post-acquisition incremental depreciation and amortization.",
        "question": "In the first full year following the acquisition, the incremental annual pre-tax depreciation and amortization expense resulting from fair value step-ups is:",
        "options": {
            "A": "15.0 million USD",
            "B": "25.0 million USD",
            "C": "35.0 million USD"
        },
        "answer": "B",
        "explanation": "Incremental depreciation on PP&E step-up: $$\\frac{50\\text{ million USD}}{10\\text{ years}} = 5.0\\text{ million USD per year}$$ Incremental amortization on patent intangibles: $$\\frac{120\\text{ million USD}}{6\\text{ years}} = 20.0\\text{ million USD per year}$$ Total incremental annual pre-tax D&A: $$5.0 + 20.0 = 25.0\\text{ million USD}$$ Goodwill is not amortized under US GAAP/IFRS; it is tested annually for impairment.",
        "distractor_analysis": {
            "A": "15.0 million USD applies 10 years to both PP&E and patents ($5 + 12 = 17$).",
            "C": "35.0 million USD erroneously includes an amortized fraction of goodwill."
        }
    },
    {
        "id": "L2-V44-Q3",
        "level": 2,
        "module": "m18-integration",
        "topic": "Financial Statement Modeling and Multi-Year Forecasting",
        "vignette_id": "V44",
        "vignette_title": "Crestview Holdings: M&A Pro Forma Integration and Goodwill Impairment Sensitivity",
        "vignette_text": "Crestview Holdings is a diversified health sciences enterprise. Senior M&A director Alicia Gomez, CFA, is modeling the pro forma financial impact of acquiring TargetPharma for 600 million USD in cash financed with 400 million USD in new term debt at 7.0% interest and 200 million USD from existing cash balances.\n\nExhibit 1: TargetPharma Fair Value Balance Sheet at Acquisition Date (in millions of USD)\n- Tangible Book Value of Net Assets = 180 USD\n- Fair Value Step-Up of PP&E = 50 USD (depreciated over 10 years straight-line)\n- Identifiable Intangible Assets (Patents) = 120 USD (amortized over 6 years straight-line)\n- Deferred Tax Liability created by step-ups (at 25% tax rate) = 42.5 USD ($25\\% \\times (50 + 120)$)\n- Net Identifiable Assets at Fair Value = 307.5 USD ($180 + 50 + 120 - 42.5$)\n- Purchase Price = 600 USD",
        "los": "Describe the accounting and impairment testing for goodwill.",
        "question": "Two years after the acquisition, TargetPharma's patent fails clinical trials and expected cash flows collapse. When Crestview tests the reporting unit for impairment under US GAAP and finds the fair value of the reporting unit is 250 million USD below its carrying value, Crestview must:",
        "options": {
            "A": "Recognize a non-cash goodwill impairment loss in operating income up to the total carrying value of goodwill.",
            "B": "Retroactively restate prior-year purchase consideration.",
            "C": "Amortize the impairment over the remaining 10 years of PP&E life."
        },
        "answer": "A",
        "explanation": "Under modern US GAAP (ASU 2017-04), an impairment loss is measured as the amount by which the reporting unit's carrying value exceeds its fair value, capped at the total amount of goodwill allocated to that unit. The impairment loss is recognized immediately in the income statement within operating expenses.",
        "distractor_analysis": {
            "B": "Prior acquisition purchase prices are historical facts and cannot be retroactively restated.",
            "C": "Impairments cannot be smoothed or capitalized over future years."
        }
    },
    {
        "id": "L2-V44-Q4",
        "level": 2,
        "module": "m18-integration",
        "topic": "Financial Statement Modeling and Multi-Year Forecasting",
        "vignette_id": "V44",
        "vignette_title": "Crestview Holdings: M&A Pro Forma Integration and Goodwill Impairment Sensitivity",
        "vignette_text": "Crestview Holdings is a diversified health sciences enterprise. Senior M&A director Alicia Gomez, CFA, is modeling the pro forma financial impact of acquiring TargetPharma for 600 million USD in cash financed with 400 million USD in new term debt at 7.0% interest and 200 million USD from existing cash balances.\n\nExhibit 1: TargetPharma Fair Value Balance Sheet at Acquisition Date (in millions of USD)\n- Tangible Book Value of Net Assets = 180 USD\n- Fair Value Step-Up of PP&E = 50 USD (depreciated over 10 years straight-line)\n- Identifiable Intangible Assets (Patents) = 120 USD (amortized over 6 years straight-line)\n- Deferred Tax Liability created by step-ups (at 25% tax rate) = 42.5 USD ($25\\% \\times (50 + 120)$)\n- Net Identifiable Assets at Fair Value = 307.5 USD ($180 + 50 + 120 - 42.5$)\n- Purchase Price = 600 USD",
        "los": "Demonstrate the effects of goodwill impairment on financial ratios.",
        "question": "What is the immediate effect of recognizing a 100 million USD goodwill impairment on Crestview's financial leverage (Total Assets / Equity) and Cash Flow from Operations (CFO)?",
        "options": {
            "A": "Financial leverage increases; CFO is unaffected.",
            "B": "Financial leverage decreases; CFO decreases by 100 million USD.",
            "C": "Both financial leverage and CFO remain unchanged."
        },
        "answer": "A",
        "explanation": "A goodwill impairment reduces Total Assets by 100 million USD and reduces Shareholders' Equity by 100 million USD (via lower net income). Because equity is smaller than assets, writing down both numerator and denominator by identical amounts increases the ratio $\\text{Assets} / \\text{Equity}$ (leverage increases). Because goodwill impairment is a non-cash accounting charge, Operating Cash Flow (CFO) is completely unaffected.",
        "distractor_analysis": {
            "B": "CFO does not decrease because no cash leaves the firm upon writing down goodwill.",
            "C": "Leverage changes because equity absorbs the percentage loss more heavily than assets."
        }
    },
    {
        "id": "L2-V44-Q5",
        "level": 2,
        "module": "m18-integration",
        "topic": "Financial Statement Modeling and Multi-Year Forecasting",
        "vignette_id": "V44",
        "vignette_title": "Crestview Holdings: M&A Pro Forma Integration and Goodwill Impairment Sensitivity",
        "vignette_text": "Crestview Holdings is a diversified health sciences enterprise. Senior M&A director Alicia Gomez, CFA, is modeling the pro forma financial impact of acquiring TargetPharma for 600 million USD in cash financed with 400 million USD in new term debt at 7.0% interest and 200 million USD from existing cash balances.\n\nExhibit 1: TargetPharma Fair Value Balance Sheet at Acquisition Date (in millions of USD)\n- Tangible Book Value of Net Assets = 180 USD\n- Fair Value Step-Up of PP&E = 50 USD (depreciated over 10 years straight-line)\n- Identifiable Intangible Assets (Patents) = 120 USD (amortized over 6 years straight-line)\n- Deferred Tax Liability created by step-ups (at 25% tax rate) = 42.5 USD ($25\\% \\times (50 + 120)$)\n- Net Identifiable Assets at Fair Value = 307.5 USD ($180 + 50 + 120 - 42.5$)\n- Purchase Price = 600 USD",
        "los": "Distinguish between IFRS and US GAAP goodwill impairment rules.",
        "question": "A fundamental difference between IFRS and US GAAP regarding goodwill impairment is that under IFRS:",
        "options": {
            "A": "Goodwill impairment losses may be reversed in subsequent years if the reporting unit recovers.",
            "B": "Goodwill is tested at the level of a cash-generating unit (CGU), and reversal of goodwill impairment is strictly prohibited under both standards.",
            "C": "Goodwill is amortized on a 40-year straight-line schedule."
        },
        "answer": "B",
        "explanation": "Under IFRS (IAS 36), impairment is assessed at the Cash-Generating Unit (CGU) level. While IFRS permits reversals of impairments for certain long-lived tangible assets and other intangibles, reversal of goodwill impairment is strictly forbidden under both IFRS and US GAAP.",
        "distractor_analysis": {
            "A": "Goodwill impairment cannot be reversed under any circumstance under IFRS.",
            "C": "Neither IFRS nor US GAAP allows goodwill amortization for public companies."
        }
    }
]

updated_p3 = existing_p3 + new_fsa_vignettes
print(f"New total L2 FSA Part 3 questions: {len(updated_p3)}")

with open(L2_FSA_P3, "w", encoding="utf-8") as f:
    json.dump(updated_p3, f, indent=2, ensure_ascii=False)

print(f"Successfully saved updated L2 FSA questions to {L2_FSA_P3}")
