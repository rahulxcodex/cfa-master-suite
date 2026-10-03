# Module 5: Understanding Cash Flow Statements
# Questions L1-Q061 to L1-Q075 (15 questions)

questions = [
    {
        "id": "L1-Q061",
        "level": 1,
        "module": "m5-cash-flow",
        "topic": "Understanding Cash Flow Statements",
        "los": "LOS 24.a: Compare cash flows from operating, investing, and financing activities under IFRS and US GAAP.",
        "question": "Which of the following correctly describes the difference between US GAAP and IFRS regarding the classification of interest paid and dividends paid on the statement of cash flows?",
        "options": {
            "A": "Under US GAAP, interest paid is CFO and dividends paid is CFF; under IFRS, interest paid can be CFO or CFF, and dividends paid can be CFO or CFF.",
            "B": "Under US GAAP, interest paid is CFF and dividends paid is CFO; under IFRS, both must be classified strictly as CFO.",
            "C": "Under both US GAAP and IFRS, interest paid and dividends paid must be classified exclusively as financing activities (CFF)."
        },
        "answer": "A",
        "explanation": "Cash flow classifications differ significantly between standard-setters:\n- Under US GAAP:\n  - Interest paid: CFO\n  - Interest received: CFO\n  - Dividends received: CFO\n  - Dividends paid: CFF\n- Under IFRS:\n  - Interest paid: CFO or CFF (financing cost)\n  - Interest received: CFO or CFI (return on investment)\n  - Dividends paid: CFF or CFO (operating cash flow component)\n  - Dividends received: CFO or CFI\n\nDistractor Analysis:\n- B incorrectly states US GAAP classifications and claims IFRS restricts both to CFO.\n- C ignores the flexibility permitted under IFRS and misstates US GAAP interest paid."
    },
    {
        "id": "L1-Q062",
        "level": 1,
        "module": "m5-cash-flow",
        "topic": "Understanding Cash Flow Statements",
        "los": "LOS 24.b: Demonstrate the indirect method of calculating cash flow from operating activities.",
        "question": "A company reports net income of 1,200,000 USD for the year. The income statement includes depreciation expense of 250,000 USD and a gain on sale of equipment of 40,000 USD. Balance sheet working capital changes are:\n- Accounts receivable increased by 60,000 USD\n- Inventory decreased by 30,000 USD\n- Accounts payable decreased by 50,000 USD\nUsing the indirect method, what is the cash flow from operating activities (CFO)?",
        "options": {
            "A": "1,330,000 USD",
            "B": "1,410,000 USD",
            "C": "1,450,000 USD"
        },
        "answer": "A",
        "explanation": "Under the indirect method, CFO is calculated starting from Net Income:\n$$\\text{Net Income} = 1,200,000\\text{ USD}$$\nAdjustments for non-cash and non-operating items:\n- Add back Depreciation: $+250,000\\text{ USD}$\n- Subtract Gain on sale of equipment (investing activity): $-40,000\\text{ USD}$\nWorking capital adjustments:\n- Increase in Accounts Receivable (cash tied up): $-60,000\\text{ USD}$\n- Decrease in Inventory (cash released): $+30,000\\text{ USD}$\n- Decrease in Accounts Payable (cash paid to vendors): $-50,000\\text{ USD}$\n\nCalculation:\n$$\\text{CFO} = 1,200,000 + 250,000 - 40,000 - 60,000 + 30,000 - 50,000 = 1,330,000\\text{ USD}$$\n\nDistractor Analysis:\n- B mistakenly adds the gain on sale (+40,000 USD instead of -40,000 USD) and adds the decrease in accounts payable.\n- C adds back gain on sale and mismanages working capital directions."
    },
    {
        "id": "L1-Q063",
        "level": 1,
        "module": "m5-cash-flow",
        "topic": "Understanding Cash Flow Statements",
        "los": "LOS 24.c: Demonstrate the direct method of calculating cash flow from operating activities.",
        "question": "For the year ended 31 December, a retail corporation reported total sales revenue of 8,500,000 USD on its income statement. During the year, accounts receivable increased by 350,000 USD, and unearned revenue increased by 120,000 USD. How much cash did the company collect from customers during the year?",
        "options": {
            "A": "8,030,000 USD",
            "B": "8,270,000 USD",
            "C": "8,730,000 USD"
        },
        "answer": "B",
        "explanation": "To determine cash collections from customers under the direct method:\n$$\\text{Cash Collected from Customers} = \\text{Sales Revenue} - \\Delta\\text{Accounts Receivable} + \\Delta\\text{Unearned Revenue}$$\n$$\\text{Cash Collected} = 8,500,000\\text{ USD} - 350,000\\text{ USD} + 120,000\\text{ USD} = 8,270,000\\text{ USD}$$\nAn increase in accounts receivable means sales exceeded cash collected. An increase in unearned revenue means cash was collected before goods were delivered.\n\nDistractor Analysis:\n- A subtracts both changes: $8,500,000 - 350,000 - 120,000 = 8,030,000\\text{ USD}$.\n- C adds both changes: $8,500,000 + 350,000 - 120,000 = 8,730,000\\text{ USD}$."
    },
    {
        "id": "L1-Q064",
        "level": 1,
        "module": "m5-cash-flow",
        "topic": "Understanding Cash Flow Statements",
        "los": "LOS 24.c: Demonstrate the direct method of calculating cash flow from operating activities.",
        "question": "A company reports Cost of Goods Sold (COGS) of 4,200,000 USD. During the fiscal year:\n- Inventory increased by 280,000 USD\n- Accounts payable to suppliers increased by 190,000 USD\nWhat was the total cash paid to suppliers during the year?",
        "options": {
            "A": "3,730,000 USD",
            "B": "4,110,000 USD",
            "C": "4,290,000 USD"
        },
        "answer": "C",
        "explanation": "Step 1: Compute total inventory purchases:\n$$\\text{Purchases} = \\text{COGS} + \\Delta\\text{Inventory} = 4,200,000\\text{ USD} + 280,000\\text{ USD} = 4,480,000\\text{ USD}$$\nStep 2: Compute cash paid to suppliers:\n$$\\text{Cash Paid to Suppliers} = \\text{Purchases} - \\Delta\\text{Accounts Payable}$$\n$$\\text{Cash Paid to Suppliers} = 4,480,000\\text{ USD} - 190,000\\text{ USD} = 4,290,000\\text{ USD}$$\n\nDistractor Analysis:\n- B incorrectly subtracts the inventory change and adds the AP change: $4,200,000 - 280,000 + 190,000 = 4,110,000\\text{ USD}$.\n- A reverses both signs: $4,200,000 - 280,000 - 190,000 = 3,730,000\\text{ USD}$."
    },
    {
        "id": "L1-Q065",
        "level": 1,
        "module": "m5-cash-flow",
        "topic": "Understanding Cash Flow Statements",
        "los": "LOS 24.b: Demonstrate the indirect method of calculating cash flow from operating activities.",
        "question": "During Year 2, a firm sold manufacturing equipment that originally cost 200,000 USD with accumulated depreciation of 130,000 USD for a cash gain on sale of 25,000 USD. What was the net cash flow from investing activities (CFI) generated from this transaction?",
        "options": {
            "A": "25,000 USD cash inflow",
            "B": "70,000 USD cash inflow",
            "C": "95,000 USD cash inflow"
        },
        "answer": "C",
        "explanation": "1. Book value (carrying value) of the equipment sold:\n$$\\text{Book Value} = \\text{Historical Cost} - \\text{Accumulated Depreciation} = 200,000\\text{ USD} - 130,000\\text{ USD} = 70,000\\text{ USD}$$\n2. Cash proceeds from the sale:\n$$\\text{Cash Proceeds} = \\text{Book Value} + \\text{Gain on Sale} = 70,000\\text{ USD} + 25,000\\text{ USD} = 95,000\\text{ USD}$$\nCash flow from investing activities reflects the full cash proceeds received of 95,000 USD.\n(Note: The 25,000 USD gain is included in net income and must be subtracted in CFO to avoid double-counting).\n\nDistractor Analysis:\n- A reflects only the accounting gain, not the total cash proceeds.\n- B reflects only the book value, ignoring the cash premium received."
    },
    {
        "id": "L1-Q066",
        "level": 1,
        "module": "m5-cash-flow",
        "topic": "Understanding Cash Flow Statements",
        "los": "LOS 24.a: Compare cash flows from operating, investing, and financing activities under IFRS and US GAAP.",
        "question": "During the year, a company engaged in the following cash transactions:\n- Issued 5,000,000 USD of new common stock\n- Repurchased 1,200,000 USD of common shares in the open market\n- Paid 600,000 USD in cash dividends to shareholders\n- Repaid 2,000,000 USD principal on maturing long-term bank debt\n- Paid 400,000 USD in interest on long-term debt\nUnder US GAAP, what is the net cash flow from financing activities (CFF)?",
        "options": {
            "A": "800,000 USD",
            "B": "1,200,000 USD",
            "C": "1,600,000 USD"
        },
        "answer": "B",
        "explanation": "Under US GAAP, CFF includes transactions involving equity owners and long-term debt principal:\n- Stock issuance: $+5,000,000\\text{ USD}$\n- Share repurchase: $-1,200,000\\text{ USD}$\n- Dividends paid: $-600,000\\text{ USD}$\n- Debt principal repayment: $-2,000,000\\text{ USD}$\nNote: Under US GAAP, interest paid (400,000 USD) must be classified as CFO, NOT CFF.\n\nCalculation:\n$$\\text{CFF} = +5,000,000 - 1,200,000 - 600,000 - 2,000,000 = 1,200,000\\text{ USD}$$\n\nDistractor Analysis:\n- A incorrectly deducts interest paid of 400,000 USD from CFF ($1,200,000 - 400,000 = 800,000\\text{ USD}$).\n- C fails to deduct dividends paid of 600,000 USD."
    },
    {
        "id": "L1-Q067",
        "level": 1,
        "module": "m5-cash-flow",
        "topic": "Understanding Cash Flow Statements",
        "los": "LOS 24.d: Describe non-cash investing and financing activities.",
        "question": "A corporation converts 10,000,000 USD of convertible bonds into 500,000 shares of common stock. How should this transaction be reported on the statement of cash flows?",
        "options": {
            "A": "As a 10,000,000 USD financing cash inflow and a 10,000,000 USD financing cash outflow on the face of the cash flow statement.",
            "B": "Excluded from the face of the statement of cash flows and disclosed in a footnote or supplementary schedule as a non-cash investing and financing activity.",
            "C": "As an operating cash flow item because it modifies interest expense obligations."
        },
        "answer": "B",
        "explanation": "Non-cash investing and financing activities (such as debt-for-equity conversions, acquiring assets via direct finance leases, or exchanging real estate) do not involve direct cash disbursements or receipts. Standard setters require that these material non-cash transactions be omitted from the face of the cash flow statement and disclosed in the footnotes or a supplementary schedule.\n\nDistractor Analysis:\n- A violates cash flow reporting rules by grossing up non-cash transactions on the statement face.\n- C is incorrect because capital structure restructurings are financing in nature, not operating."
    },
    {
        "id": "L1-Q068",
        "level": 1,
        "module": "m5-cash-flow",
        "topic": "Understanding Cash Flow Statements",
        "los": "LOS 24.e: Calculate and interpret free cash flow to the firm (FCFF) and free cash flow to equity (FCFE).",
        "question": "A company reports the following financial data for the fiscal year:\n- Cash flow from operations (CFO) under US GAAP: 3,500,000 USD\n- Interest expense: 600,000 USD\n- Corporate income tax rate: 25%\n- Capital expenditures (FCInv): 1,800,000 USD\nWhat is the company's Free Cash Flow to the Firm (FCFF)?",
        "options": {
            "A": "1,700,000 USD",
            "B": "2,150,000 USD",
            "C": "2,300,000 USD"
        },
        "answer": "B",
        "explanation": "Under US GAAP (where interest paid is deducted in CFO):\n$$\\text{FCFF} = \\text{CFO} + \\text{Interest Expense} \\times (1 - \\text{Tax Rate}) - \\text{FCInv}$$\nCalculation:\n- After-tax interest = $600,000\\text{ USD} \\times (1 - 0.25) = 450,000\\text{ USD}$\n$$\\text{FCFF} = 3,500,000\\text{ USD} + 450,000\\text{ USD} - 1,800,000\\text{ USD} = 2,150,000\\text{ USD}$$\n\nDistractor Analysis:\n- A fails to add back after-tax interest: $3,500,000 - 1,800,000 = 1,700,000\\text{ USD}$.\n- C adds back pre-tax interest without tax adjustment: $3,500,000 + 600,000 - 1,800,000 = 2,300,000\\text{ USD}$."
    },
    {
        "id": "L1-Q069",
        "level": 1,
        "module": "m5-cash-flow",
        "topic": "Understanding Cash Flow Statements",
        "los": "LOS 24.e: Calculate and interpret free cash flow to the firm (FCFF) and free cash flow to equity (FCFE).",
        "question": "A firm reports CFO of 2,800,000 USD, capital expenditures on PP&E of 1,200,000 USD, debt principal repayments of 500,000 USD, and new debt issuances of 900,000 USD during the period. Assuming interest paid is included in CFO, what is the Free Cash Flow to Equity (FCFE)?",
        "options": {
            "A": "1,200,000 USD",
            "B": "1,600,000 USD",
            "C": "2,000,000 USD"
        },
        "answer": "C",
        "explanation": "Free Cash Flow to Equity (FCFE) is calculated as:\n$$\\text{FCFE} = \\text{CFO} - \\text{FCInv} + \\text{Net Borrowing}$$\n1. Net Borrowing = $\\text{New Debt Issued} - \\text{Debt Repaid} = 900,000\\text{ USD} - 500,000\\text{ USD} = +400,000\\text{ USD}$.\n2. FCFE Calculation:\n$$\\text{FCFE} = 2,800,000\\text{ USD} - 1,200,000\\text{ USD} + 400,000\\text{ USD} = 2,000,000\\text{ USD}$$\n\nDistractor Analysis:\n- A subtracts net borrowing instead of adding it: $2,800,000 - 1,200,000 - 400,000 = 1,200,000\\text{ USD}$.\n- B ignores net borrowing altogether: $2,800,000 - 1,200,000 = 1,600,000\\text{ USD}$."
    },
    {
        "id": "L1-Q070",
        "level": 1,
        "module": "m5-cash-flow",
        "topic": "Understanding Cash Flow Statements",
        "los": "LOS 24.b: Demonstrate the indirect method of calculating cash flow from operating activities.",
        "question": "A company's gross PP&E was 6,000,000 USD at the beginning of the year and 7,400,000 USD at the end of the year. During the year, the company sold machinery with an original cost of 500,000 USD. If all asset acquisitions were paid in cash, how much cash was paid for new PP&E (capital expenditures) during the year?",
        "options": {
            "A": "1,400,000 USD",
            "B": "1,900,000 USD",
            "C": "2,400,000 USD"
        },
        "answer": "B",
        "explanation": "Analyzing the Gross PP&E account balance:\n$$\\text{Ending Gross PP\\&E} = \\text{Beginning Gross PP\\&E} + \\text{Purchases of PP\\&E} - \\text{Gross Cost of PP\\&E Sold}$$\n$$7,400,000\\text{ USD} = 6,000,000\\text{ USD} + \\text{Purchases} - 500,000\\text{ USD}$$\n$$7,400,000\\text{ USD} = 5,500,000\\text{ USD} + \\text{Purchases} \\implies \\text{Purchases} = 1,900,000\\text{ USD}$$\nTherefore, cash capital expenditures were 1,900,000 USD.\n\nDistractor Analysis:\n- A looks only at the net change in gross PP&E ($7,400,000 - 6,000,000 = 1,400,000\\text{ USD}$), failing to account for the retired equipment.\n- C adds the 500,000 USD to the ending balance incorrectly."
    },
    {
        "id": "L1-Q071",
        "level": 1,
        "module": "m5-cash-flow",
        "topic": "Understanding Cash Flow Statements",
        "los": "LOS 24.f: Calculate and interpret cash flow performance and coverage ratios.",
        "question": "A corporation reports the following data:\n- CFO: 800,000 USD\n- Total Revenue: 4,000,000 USD\n- Average Total Assets: 5,000,000 USD\n- Average Shareholders' Equity: 2,500,000 USD\nWhat are the company's cash flow-to-revenue ratio and cash return on assets (ROA) ratio?",
        "options": {
            "A": "Cash flow-to-revenue: 20%; Cash return on assets: 16%.",
            "B": "Cash flow-to-revenue: 20%; Cash return on assets: 32%.",
            "C": "Cash flow-to-revenue: 16%; Cash return on assets: 20%."
        },
        "answer": "A",
        "explanation": "1. Cash flow-to-revenue ratio:\n$$\\frac{\\text{CFO}}{\\text{Total Revenue}} = \\frac{800,000\\text{ USD}}{4,000,000\\text{ USD}} = 20\\%$$\n2. Cash return on assets ratio:\n$$\\frac{\\text{CFO}}{\\text{Average Total Assets}} = \\frac{800,000\\text{ USD}}{5,000,000\\text{ USD}} = 16\\%$$\n(Note: Cash return on equity would be $800,000 / 2,500,000 = 32\\%$).\n\nDistractor Analysis:\n- B combines cash flow-to-revenue with cash return on equity (32%).\n- C reverses the two calculated values."
    },
    {
        "id": "L1-Q072",
        "level": 1,
        "module": "m5-cash-flow",
        "topic": "Understanding Cash Flow Statements",
        "los": "LOS 24.f: Calculate and interpret cash flow performance and coverage ratios.",
        "question": "A firm has CFO of 1,500,000 USD, interest paid of 250,000 USD, taxes paid of 350,000 USD, and total debt of 4,500,000 USD. What is the firm's debt coverage ratio and cash interest coverage ratio?",
        "options": {
            "A": "Debt coverage: 0.33; Cash interest coverage: 6.00.",
            "B": "Debt coverage: 0.33; Cash interest coverage: 8.40.",
            "C": "Debt coverage: 0.40; Cash interest coverage: 6.00."
        },
        "answer": "B",
        "explanation": "1. Debt Coverage Ratio:\n$$\\text{Debt Coverage} = \\frac{\\text{CFO}}{\\text{Total Debt}} = \\frac{1,500,000\\text{ USD}}{4,500,000\\text{ USD}} = 0.333 \\approx 0.33$$\n2. Cash Interest Coverage Ratio:\n$$\\text{Cash Interest Coverage} = \\frac{\\text{CFO} + \\text{Interest Paid} + \\text{Taxes Paid}}{\\text{Interest Paid}}$$\n$$\\text{Cash Interest Coverage} = \\frac{1,500,000\\text{ USD} + 250,000\\text{ USD} + 350,000\\text{ USD}}{250,000\\text{ USD}} = \\frac{2,100,000\\text{ USD}}{250,000\\text{ USD}} = 8.40$$\n\nDistractor Analysis:\n- A calculates cash interest coverage as $1,500,000 / 250,000 = 6.00$, failing to add back interest and taxes paid to measure total pre-tax/pre-interest cash generated.\n- C makes errors in both calculations."
    },
    {
        "id": "L1-Q073",
        "level": 1,
        "module": "m5-cash-flow",
        "topic": "Understanding Cash Flow Statements",
        "los": "LOS 24.f: Calculate and interpret cash flow performance and coverage ratios.",
        "question": "The cash reinvestment ratio measures a company's ability to finance capital replacement and expansion internally from operations. It is computed as CFO divided by:",
        "options": {
            "A": "Cash paid for long-term productive assets.",
            "B": "Total shareholders' equity plus long-term debt.",
            "C": "Net income minus dividends declared."
        },
        "answer": "A",
        "explanation": "The cash reinvestment ratio is calculated as:\n$$\\text{Cash Reinvestment Ratio} = \\frac{\\text{CFO}}{\\text{Cash Paid for Long-Term Assets (Capital Expenditures)}}$$\nIt evaluates the extent to which operating cash flows cover ongoing investments in productive long-term physical assets.\n\nDistractor Analysis:\n- B describes invested capital, not the reinvestment denominator.\n- C describes additions to retained earnings."
    },
    {
        "id": "L1-Q074",
        "level": 1,
        "module": "m5-cash-flow",
        "topic": "Understanding Cash Flow Statements",
        "los": "LOS 24.a: Compare cash flows from operating, investing, and financing activities under IFRS and US GAAP.",
        "question": "Regarding the presentation of the cash flow statement, which of the following statements is most accurate under US GAAP and IFRS?",
        "options": {
            "A": "Both IASB and FASB encourage the direct method for CFO; however, under US GAAP, companies using the direct method must also provide a reconciliation of net income to CFO using the indirect method.",
            "B": "US GAAP mandates the direct method, whereas IFRS mandates the indirect method.",
            "C": "Under IFRS, if a firm chooses the direct method, it must provide a full reconciliation of net income to operating cash flow in the notes."
        },
        "answer": "A",
        "explanation": "Both standard setters express a preference for the direct method because it provides more granular information regarding gross operating receipts and payments. However, under US GAAP, if an entity presents CFO using the direct method, it is required to disclose an indirect method reconciliation of net income to CFO in a supplementary schedule. Under IFRS, this reconciliation is encouraged but not strictly required.\n\nDistractor Analysis:\n- B is incorrect because both frameworks allow either the direct or indirect method.\n- C is incorrect because IFRS does not mandate an indirect reconciliation when the direct method is used."
    },
    {
        "id": "L1-Q075",
        "level": 1,
        "module": "m5-cash-flow",
        "topic": "Understanding Cash Flow Statements",
        "los": "LOS 24.b: Demonstrate the indirect method of calculating cash flow from operating activities.",
        "question": "During the year, a company reported net income of 950,000 USD. Selected balance sheet and income statement items include:\n- Depreciation expense: 180,000 USD\n- Amortization of patents: 30,000 USD\n- Impairment of goodwill: 50,000 USD\n- Increase in accounts receivable: 70,000 USD\n- Increase in inventories: 45,000 USD\n- Increase in accounts payable: 60,000 USD\n- Increase in unearned revenue: 25,000 USD\nAssuming no other items, what is CFO under the indirect method?",
        "options": {
            "A": "1,110,000 USD",
            "B": "1,180,000 USD",
            "C": "1,240,000 USD"
        },
        "answer": "B",
        "explanation": "Indirect CFO calculation:\n$$\\text{Net Income} = 950,000\\text{ USD}$$\nAdd non-cash expenses:\n- Depreciation: $+180,000\\text{ USD}$\n- Amortization: $+30,000\\text{ USD}$\n- Goodwill impairment: $+50,000\\text{ USD}$\nSubtotal non-cash items = $+260,000\\text{ USD}$\n\nWorking capital adjustments:\n- Increase in Accounts Receivable: $-70,000\\text{ USD}$\n- Increase in Inventories: $-45,000\\text{ USD}$\n- Increase in Accounts Payable: $+60,000\\text{ USD}$\n- Increase in Unearned Revenue: $+25,000\\text{ USD}$\nNet working capital change = $-70,000 - 45,000 + 60,000 + 25,000 = -30,000\\text{ USD}$\n\nTotal CFO:\n$$\\text{CFO} = 950,000 + 260,000 - 30,000 = 1,180,000\\text{ USD}$$\n\nDistractor Analysis:\n- A fails to include the non-cash goodwill impairment add-back: $1,180,000 - 50,000 = 1,130,000$ or miscalculates working capital.\n- C treats the increase in accounts receivable as an addition instead of a deduction."
    }
]
