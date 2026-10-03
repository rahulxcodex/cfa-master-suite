import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
L1_P2 = os.path.join(BASE_DIR, "data", "l1_questions_part2.json")

with open(L1_P2, "r", encoding="utf-8") as f:
    existing_l1_p2 = json.load(f)

print(f"Current L1 Part 2 questions: {len(existing_l1_p2)}")

new_m12_questions = [
    {
        "id": "L1-M12-016",
        "level": 1,
        "module": "m12-quality-l1",
        "topic": "Financial Reporting Quality",
        "los": "Calculate and interpret the balance-sheet-based and cash-flow-based accruals ratios.",
        "question": "A firm reports average net operating assets of 1,000 million USD and net income of 150 million USD, with cash flow from operations (CFO) of 60 million USD and cash flow from investing (CFI) of -80 million USD. Using the cash-flow-based approach, the firm's accruals ratio is:",
        "options": {
            "A": "0.090",
            "B": "0.170",
            "C": "0.210"
        },
        "answer": "B",
        "explanation": "Under the cash-flow-based approach, aggregate accruals are defined as: $$\\text{Accruals}_{\\text{CF}} = \\text{Net Income} - (\\text{CFO} + \\text{CFI})$$ $$\\text{Accruals}_{\\text{CF}} = 150 - (60 + (-80)) = 150 - (-20) = 170\\text{ million USD}$$ The cash-flow-based accruals ratio is: $$\\text{Accruals Ratio} = \\frac{\\text{Accruals}_{\\text{CF}}}{\\text{Average NOA}} = \\frac{170}{1{,}000} = 0.170$$ A higher accruals ratio indicates lower earnings quality.",
        "distractor_analysis": {
            "A": "0.090 subtracts only CFO ($150 - 60 = 90 / 1000 = 0.090$), ignoring CFI.",
            "C": "0.210 results from an arithmetic error in sign handling ($150 + 60$)."
        }
    },
    {
        "id": "L1-M12-017",
        "level": 1,
        "module": "m12-quality-l1",
        "topic": "Financial Reporting Quality",
        "los": "Describe the spectrum of financial reporting quality.",
        "question": "Which of the following levels on the financial reporting quality spectrum reflects the HIGHEST level of quality?",
        "options": {
            "A": "Reporting is compliant with GAAP/IFRS, decision-useful, and reflects sustainable earnings and high return on capital.",
            "B": "Reporting is compliant with GAAP/IFRS but management uses biased accounting choices that obscure underlying economic reality.",
            "C": "Reporting is non-compliant and contains outright fraudulent transactions."
        },
        "answer": "A",
        "explanation": "At the top of the quality spectrum is reporting that is not only fully compliant with GAAP/IFRS and decision-useful, but also reflects high-quality economic earnings—meaning earnings are sustainable and provide adequate returns on capital.",
        "distractor_analysis": {
            "B": "Biased choices (aggressive or conservative) represent a lower quality tier on the spectrum.",
            "C": "Fraudulent non-compliance is at the very bottom of the quality hierarchy."
        }
    },
    {
        "id": "L1-M12-018",
        "level": 1,
        "module": "m12-quality-l1",
        "topic": "Financial Reporting Quality",
        "los": "Describe warnings signs of earnings manipulation.",
        "question": "Which of the following accounting relationships is considered a significant red flag for aggressive revenue recognition?",
        "options": {
            "A": "Days sales outstanding (DSO) that increases significantly while sales growth accelerates.",
            "B": "Cash flow from operations that consistently exceeds net income over multiple consecutive years.",
            "C": "Inventory turnover that increases while gross margins remain stable."
        },
        "answer": "A",
        "explanation": "A surging DSO alongside rapid revenue growth indicates that receivables are expanding faster than sales. This suggests that the firm may be booking uncollectible sales, offering extended customer credit terms, or shipping unordered goods (channel stuffing) to inflate top-line results.",
        "distractor_analysis": {
            "B": "CFO consistently exceeding net income is a sign of high earnings quality and conservative accounting.",
            "C": "Faster inventory turnover reflects strong operational efficiency, not manipulation."
        }
    },
    {
        "id": "L1-M12-019",
        "level": 1,
        "module": "m12-quality-l1",
        "topic": "Financial Reporting Quality",
        "los": "Describe differences between conservative and aggressive accounting choices.",
        "question": "A firm that uses accelerated depreciation and LIFO inventory accounting during periods of rising prices is employing:",
        "options": {
            "A": "Aggressive accounting choices that overstate current earnings and equity.",
            "B": "Conservative accounting choices that reduce reported current earnings and provide higher future earnings potential.",
            "C": "Fraudulent non-GAAP accounting."
        },
        "answer": "B",
        "explanation": "Conservative accounting choices defer income recognition and accelerate expense recognition. LIFO in inflationary periods charges higher current replacement costs to COGS, and accelerated depreciation front-loads asset wear, reducing current net income and book equity while boosting real cash flow through lower taxes.",
        "distractor_analysis": {
            "A": "Aggressive choices would use straight-line depreciation and FIFO to inflate current net income.",
            "C": "Accelerated depreciation and LIFO are fully compliant standard GAAP methods."
        }
    },
    {
        "id": "L1-M12-020",
        "level": 1,
        "module": "m12-quality-l1",
        "topic": "Financial Reporting Quality",
        "los": "Describe types of auditor opinions.",
        "question": "An auditor issues a disclaimer of opinion when:",
        "options": {
            "A": "The financial statements are presented fairly in all material respects.",
            "B": "There is a severe limitation on the scope of the audit, or the auditor is unable to obtain sufficient appropriate audit evidence.",
            "C": "There is a specific, isolated material departure from accounting standards that does not pervasively affect the entire report."
        },
        "answer": "B",
        "explanation": "A disclaimer of opinion is issued when the auditor is unable to obtain sufficient appropriate audit evidence to form an opinion (scope limitation) or when significant uncertainties undermine the entire audit. An unqualified opinion confirms fair presentation, while a qualified opinion addresses isolated non-pervasive departures.",
        "distractor_analysis": {
            "A": "Fair presentation in all material respects earns an unqualified (clean) opinion.",
            "C": "An isolated material departure results in a qualified ('except for') opinion."
        }
    },
    {
        "id": "L1-M12-021",
        "level": 1,
        "module": "m12-quality-l1",
        "topic": "Financial Reporting Quality",
        "los": "Describe motivations for management to manage earnings.",
        "question": "Corporate managers are most strongly incentivized to adopt aggressive earnings choices when:",
        "options": {
            "A": "Company performance is substantially above the upper ceiling of management's annual incentive bonus plan.",
            "B": "Reported earnings are slightly below consensus Wall Street analyst forecasts or debt covenant threshold ratios.",
            "C": "The company plans to repurchase shares from existing shareholders in an open-market buyback."
        },
        "answer": "B",
        "explanation": "Failing to meet quarterly consensus earnings by even one cent can trigger severe stock price declines and threaten managerial tenure. Similarly, breaching debt covenant ratios triggers technical default and lender penalties. These situations create intense pressure for aggressive accounting accruals.",
        "distractor_analysis": {
            "A": "When above the bonus ceiling, managers tend to manage earnings downward ('cookie-jar reserves') for future periods.",
            "C": "When buying back shares, management has an incentive to depress share prices, not inflate them."
        }
    },
    {
        "id": "L1-M12-022",
        "level": 1,
        "module": "m12-quality-l1",
        "topic": "Financial Reporting Quality",
        "los": "Describe the balance-sheet-based accruals ratio.",
        "question": "Using the balance sheet approach, Net Operating Assets (NOA) is defined as:",
        "options": {
            "A": "(Total Assets - Cash and Marketable Securities) - (Total Liabilities - Total Debt).",
            "B": "Total Current Assets minus Total Current Liabilities.",
            "C": "Gross Property, Plant, and Equipment minus Accumulated Depreciation."
        },
        "answer": "A",
        "explanation": "Net Operating Assets (NOA) isolates operating capital from financial assets and financing debt: Operating Assets equal Total Assets minus Cash and Cash Equivalents; Operating Liabilities equal Total Liabilities minus Total Debt (short- and long-term interest-bearing debt). NOA is Operating Assets minus Operating Liabilities.",
        "distractor_analysis": {
            "B": "Current assets minus current liabilities is working capital, not NOA.",
            "C": "PP&E is only one component of non-current operating assets."
        }
    },
    {
        "id": "L1-M12-023",
        "level": 1,
        "module": "m12-quality-l1",
        "topic": "Financial Reporting Quality",
        "los": "Explain mean reversion in earnings and accruals.",
        "question": "Empirical accounting research demonstrates that firms with high positive accruals tend to experience:",
        "options": {
            "A": "Permanent and indefinite acceleration of return on equity.",
            "B": "Mean reversion and subsequent declines in future earnings as prior-period accruals reverse.",
            "C": "Statutory immunity from SEC regulatory enforcement audits."
        },
        "answer": "B",
        "explanation": "Accruals are temporary accounting entries that must eventually reverse in future periods (e.g., accrued receivables must either be collected in cash or written off). Firms with high positive accrual components exhibit low earnings persistence and experience mean reversion in future profitability.",
        "distractor_analysis": {
            "A": "Accrual-driven earnings cannot sustain perpetual ROE acceleration.",
            "C": "Firms with high accruals are frequent targets of regulatory investigation."
        }
    },
    {
        "id": "L1-M12-024",
        "level": 1,
        "module": "m12-quality-l1",
        "topic": "Financial Reporting Quality",
        "los": "Describe warning signs related to cash flow manipulation.",
        "question": "Which of the following management actions artificially inflates Cash Flow from Operating Activities (CFO)?",
        "options": {
            "A": "Selling accounts receivable with recourse or securitizing receivables just before fiscal year-end.",
            "B": "Accelerating payments to trade suppliers prior to the balance sheet date.",
            "C": "Purchasing manufacturing equipment with available cash."
        },
        "answer": "A",
        "explanation": "Selling or factoring accounts receivable accelerates cash collections from future periods into the current period, boosting headline CFO before year-end. If sold with recourse, the credit risk remains with the firm, disguising short-term financing as operational cash flow.",
        "distractor_analysis": {
            "B": "Accelerating vendor payments reduces CFO in the current period.",
            "C": "Equipment purchases are classified as investing cash outflows (CFI), not operating cash flows."
        }
    },
    {
        "id": "L1-M12-025",
        "level": 1,
        "module": "m12-quality-l1",
        "topic": "Financial Reporting Quality",
        "los": "Explain the role of internal controls and the Sarbanes-Oxley Act.",
        "question": "Under Section 404 of the Sarbanes-Oxley Act (SOX), management and independent auditors must:",
        "options": {
            "A": "Guarantee that the stock price will not drop below the original issuance price.",
            "B": "Assess and report on the effectiveness of the company's internal control over financial reporting (ICFR).",
            "C": "Eliminate all operating leases from financial footnote disclosures."
        },
        "answer": "B",
        "explanation": "Section 404 of SOX mandates that public company management accept responsibility for establishing and maintaining an adequate internal control structure and assess its effectiveness annually. Independent auditors must attest to and issue an audit report on management's internal control assessment.",
        "distractor_analysis": {
            "A": "SOX governs reporting integrity and controls; it cannot guarantee stock market returns.",
            "C": "Leases are governed by ASC 842 / IFRS 16 accounting standards, not SOX section 404."
        }
    }
]

updated_l1_p2 = existing_l1_p2 + new_m12_questions
print(f"New total L1 Part 2 questions: {len(updated_l1_p2)}")

with open(L1_P2, "w", encoding="utf-8") as f:
    json.dump(updated_l1_p2, f, indent=2, ensure_ascii=False)

print(f"Successfully saved updated L1 Part 2 questions to {L1_P2}")
