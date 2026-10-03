# Module 1: Introduction to Financial Statement Analysis & Accounting Mechanics
# Questions L1-Q001 to L1-Q015 (15 questions)

questions = [
    {
        "id": "L1-Q001",
        "level": 1,
        "module": "m1-intro",
        "topic": "Introduction to Financial Statement Analysis",
        "los": "LOS 19.a: Describe the roles of financial reporting and financial statement analysis.",
        "question": "Which of the following statements best describes the primary distinction between financial reporting and financial statement analysis?",
        "options": {
            "A": "Financial reporting focuses on assessing a company's past performance to forecast future cash flows, whereas financial statement analysis focuses on providing information about financial position.",
            "B": "Financial reporting provides information about a company's financial position, performance, and changes in financial position, whereas financial statement analysis uses this information to evaluate past performance and make economic decisions.",
            "C": "Financial reporting is designed exclusively for external regulatory compliance, whereas financial statement analysis is prepared exclusively for internal corporate management."
        },
        "answer": "B",
        "explanation": "Financial reporting seeks to provide information about a company's financial performance, financial position, and changes in financial position that is useful to a wide range of users (equity investors, creditors, suppliers, etc.). In contrast, financial statement analysis evaluates financial reports and other disclosures to assess past performance, evaluate creditworthiness, and forecast future performance to make economic decisions (e.g., investing in equity or lending capital).\n\nDistractor Analysis:\n- A is incorrect because it reverses the roles: financial reporting provides the data, whereas analysis evaluates performance to forecast future outcomes.\n- C is incorrect because financial reporting serves diverse external users (not just regulators), and financial statement analysis is widely conducted by external analysts, investors, and rating agencies (not exclusively internal management)."
    },
    {
        "id": "L1-Q002",
        "level": 1,
        "module": "m1-intro",
        "topic": "Introduction to Financial Statement Analysis",
        "los": "LOS 20.b: Describe the accounting equation and the process of recording business transactions.",
        "question": "A corporation issues 100,000 USD of long-term bonds at face value. It immediately uses 60,000 USD of the proceeds to purchase manufacturing machinery and retains the remaining 40,000 USD in cash. What is the net impact of these transactions on the fundamental accounting equation?",
        "options": {
            "A": "Total assets increase by 100,000 USD, liabilities increase by 100,000 USD, and equity remains unchanged.",
            "B": "Total assets increase by 40,000 USD, liabilities increase by 100,000 USD, and equity decreases by 60,000 USD.",
            "C": "Total assets increase by 160,000 USD, liabilities increase by 100,000 USD, and equity increases by 60,000 USD."
        },
        "answer": "A",
        "explanation": "The fundamental accounting equation is:\n$$\\text{Assets} = \\text{Liabilities} + \\text{Equity}$$\n1. Issuance of bonds: Cash (Asset) increases by 100,000 USD, and Bonds Payable (Liability) increases by 100,000 USD.\n2. Purchase of machinery: Machinery (Asset) increases by 60,000 USD, and Cash (Asset) decreases by 60,000 USD (net asset change for step 2 is 0 USD).\n\nNet combined result:\n- Total Assets change = $+40,000\\text{ USD (Cash)} + 60,000\\text{ USD (Machinery)} = +100,000\\text{ USD}$.\n- Liabilities change = $+100,000\\text{ USD (Bonds Payable)}$.\n- Equity change = $0\\text{ USD}$.\n\nDistractor Analysis:\n- B is incorrect because purchasing an asset with cash does not reduce equity; it is an asset exchange.\n- C is incorrect because the cash outflow of 60,000 USD is ignored, incorrectly double counting the total asset inflow."
    },
    {
        "id": "L1-Q003",
        "level": 1,
        "module": "m1-intro",
        "topic": "Introduction to Financial Statement Analysis",
        "los": "LOS 20.c: Describe accrual accounting and the need for accruals and other adjustments.",
        "question": "On 1 November Year 1, a software firm receives an upfront cash payment of 36,000 USD for an annual cloud subscription service covering 1 November Year 1 through 31 October Year 2. Under accrual accounting, how should this transaction be reflected on the financial statements for the fiscal year ended 31 December Year 1?",
        "options": {
            "A": "Recognize 36,000 USD of subscription revenue on the income statement and zero liabilities on the balance sheet.",
            "B": "Recognize 6,000 USD of subscription revenue on the income statement and 30,000 USD of unearned revenue as a liability on the balance sheet.",
            "C": "Recognize 0 USD of revenue on the income statement until the contract is fully fulfilled on 31 October Year 2."
        },
        "answer": "B",
        "explanation": "Under accrual accounting, revenue is recognized when performance obligations are satisfied over time. \n- The total contract duration is 12 months for 36,000 USD, or $36,000 / 12 = 3,000\\text{ USD}$ per month.\n- For Year 1 (November and December = 2 months), revenue recognized is:\n$$2 \\times 3,000\\text{ USD} = 6,000\\text{ USD}$$\n- The remaining 10 months represents an obligation to perform services in Year 2 and is recorded as unearned (deferred) revenue liability:\n$$10 \\times 3,000\\text{ USD} = 30,000\\text{ USD}$$\n\nDistractor Analysis:\n- A represents cash-basis accounting, which violates the accrual principle by recognizing revenue before performance.\n- C is incorrect because performance occurs ratably over the subscription period; deferring all revenue until contract completion is only appropriate under completed-contract treatment where progress cannot be measured."
    },
    {
        "id": "L1-Q004",
        "level": 1,
        "module": "m1-intro",
        "topic": "Introduction to Financial Statement Analysis",
        "los": "LOS 20.c: Describe accrual accounting and the need for accruals and other adjustments.",
        "question": "At the fiscal year-end of 31 December, an industrial firm failed to record an adjusting journal entry for 15,000 USD of accrued interest expense incurred on short-term bank borrowings payable on 15 January. What is the impact of this omission on the firm's Year 1 financial statements?",
        "options": {
            "A": "Liabilities are understated, and net income is overstated.",
            "B": "Liabilities are overstated, and net income is understated.",
            "C": "Assets are overstated, and liabilities are understated."
        },
        "answer": "A",
        "explanation": "The proper year-end adjusting entry requires:\n- Debit: Interest Expense (15,000 USD)\n- Credit: Interest Payable (Liability) (15,000 USD)\n\nOmitting this entry results in:\n- Expenses being understated by 15,000 USD, which overstates Net Income by 15,000 USD (and consequently overstates ending Retained Earnings / Equity).\n- Interest Payable (Liabilities) being understated by 15,000 USD.\n- Assets are unaffected because cash has not yet been disbursed.\n\nDistractor Analysis:\n- B is incorrect because liabilities are understated (the obligation was omitted) and net income is overstated.\n- C is incorrect because assets are not affected by an unrecorded accrued expense."
    },
    {
        "id": "L1-Q005",
        "level": 1,
        "module": "m1-intro",
        "topic": "Introduction to Financial Statement Analysis",
        "los": "LOS 20.b: Describe the accounting equation and the process of recording business transactions.",
        "question": "On 1 October Year 1, Apex Corp. paid 24,000 USD cash for a two-year commercial property insurance policy effective immediately. What amounts should Apex report as insurance expense on its income statement for the year ended 31 December Year 1 and as prepaid insurance on its balance sheet as of 31 December Year 1?",
        "options": {
            "A": "Insurance Expense: 3,000 USD; Prepaid Insurance: 21,000 USD.",
            "B": "Insurance Expense: 6,000 USD; Prepaid Insurance: 18,000 USD.",
            "C": "Insurance Expense: 12,000 USD; Prepaid Insurance: 12,000 USD."
        },
        "answer": "A",
        "explanation": "The policy duration is 24 months for 24,000 USD, which equals $1,000\\text{ USD}$ per month.\n- From 1 October to 31 December Year 1, 3 months have expired:\n$$\\text{Insurance Expense} = 3 \\times 1,000\\text{ USD} = 3,000\\text{ USD}$$\n- The unexpired coverage as of 31 December Year 1 is 21 months:\n$$\\text{Prepaid Insurance (Asset)} = 21 \\times 1,000\\text{ USD} = 21,000\\text{ USD}$$\n\nDistractor Analysis:\n- B incorrectly assumes a 1-year policy expiring after 6 months or 3 months of a 1-year policy.\n- C incorrectly amortizes 1 full year of expense (12 months) instead of the 3 months that actually elapsed."
    },
    {
        "id": "L1-Q006",
        "level": 1,
        "module": "m1-intro",
        "topic": "Introduction to Financial Statement Analysis",
        "los": "LOS 19.b: Describe the roles of the key financial statements and how they are interrelated.",
        "question": "During Year 2, a company reported beginning retained earnings of 450,000 USD, ending retained earnings of 580,000 USD, and declared total dividends of 70,000 USD. What was the company's net income for Year 2?",
        "options": {
            "A": "60,000 USD",
            "B": "130,000 USD",
            "C": "200,000 USD"
        },
        "answer": "C",
        "explanation": "The statement of changes in retained earnings links the income statement to the balance sheet via the formula:\n$$\\text{Ending Retained Earnings} = \\text{Beginning Retained Earnings} + \\text{Net Income} - \\text{Dividends Declared}$$\nRearranging to solve for Net Income:\n$$\\text{Net Income} = \\text{Ending Retained Earnings} - \\text{Beginning Retained Earnings} + \\text{Dividends Declared}$$\n$$\\text{Net Income} = 580,000\\text{ USD} - 450,000\\text{ USD} + 70,000\\text{ USD} = 130,000\\text{ USD} + 70,000\\text{ USD} = 200,000\\text{ USD}$$\n\nDistractor Analysis:\n- A subtracts dividends from the change in retained earnings ($130,000 - 70,000 = 60,000\\text{ USD}$), which incorrectly treats dividends as adding to retained earnings.\n- B equals the net change in retained earnings ($580,000 - 450,000 = 130,000\\text{ USD}$), neglecting dividends declared."
    },
    {
        "id": "L1-Q007",
        "level": 1,
        "module": "m1-intro",
        "topic": "Introduction to Financial Statement Analysis",
        "los": "LOS 19.c: Describe the importance of financial statement notes and supplementary schedules.",
        "question": "Which of the following items is an analyst most likely to find exclusively within the footnotes to the financial statements rather than on the face of the primary financial statements?",
        "options": {
            "A": "Total operating expenses and operating income for the fiscal period.",
            "B": "Detailed accounting policies, significant management estimates, and commitments and contingencies.",
            "C": "Cash flows generated from operating, investing, and financing activities."
        },
        "answer": "B",
        "explanation": "Footnotes provide critical context to the primary financial statements, including summary of significant accounting policies, revenue recognition methods, inventory valuation methods, depreciation schedules, pension assumptions, financial instrument risks, and legal contingencies.\n\nDistractor Analysis:\n- A appears directly on the face of the income statement.\n- C appears directly on the face of the statement of cash flows."
    },
    {
        "id": "L1-Q008",
        "level": 1,
        "module": "m1-intro",
        "topic": "Introduction to Financial Statement Analysis",
        "los": "LOS 19.d: Describe the objective of audits of financial statements, the types of audit reports, and the importance of effective internal controls.",
        "question": "An independent auditor evaluates a corporation's financial statements and concludes that they contain a material departure from applicable accounting standards that is pervasive to the financial statements as a whole. Which type of audit opinion should the auditor issue?",
        "options": {
            "A": "Qualified audit opinion.",
            "B": "Adverse audit opinion.",
            "C": "Disclaimer of opinion."
        },
        "answer": "B",
        "explanation": "An adverse opinion is issued when financial statements are materially misstated and the misstatements are pervasive, meaning they are not confined to specific elements or represent a substantial proportion of the financial statements.\n\nDistractor Analysis:\n- A (Qualified opinion) is issued when there is a material misstatement or scope limitation, but the effect is NOT pervasive (the financial statements are fairly presented 'except for' the matter).\n- C (Disclaimer of opinion) is issued when the auditor is unable to obtain sufficient appropriate audit evidence due to a pervasive scope limitation and cannot express an opinion."
    },
    {
        "id": "L1-Q009",
        "level": 1,
        "module": "m1-intro",
        "topic": "Introduction to Financial Statement Analysis",
        "los": "LOS 19.d: Describe the objective of audits of financial statements, the types of audit reports, and the importance of effective internal controls.",
        "question": "What level of assurance does an auditor's unqualified opinion provide regarding the absolute absence of fraud or error in a company's financial statements?",
        "options": {
            "A": "Absolute assurance that the financial statements are completely free from error or fraud.",
            "B": "Reasonable assurance that the financial statements as a whole are free from material misstatement, whether caused by fraud or error.",
            "C": "Limited assurance based solely on analytical procedures and management inquiries."
        },
        "answer": "B",
        "explanation": "An audit provides reasonable assurance—not absolute assurance—that the financial statements are free from material misstatement. Absolute assurance is unattainable due to the inherent limitations of an audit, including the use of testing/sampling, inherent limitations of internal controls, and the persuasive rather than conclusive nature of audit evidence.\n\nDistractor Analysis:\n- A is incorrect because auditors do not provide absolute guarantees or ensure complete accuracy.\n- C describes a review engagement (negative/limited assurance), not an audit which requires substantive testing."
    },
    {
        "id": "L1-Q010",
        "level": 1,
        "module": "m1-intro",
        "topic": "Introduction to Financial Statement Analysis",
        "los": "LOS 19.e: Identify and describe information sources that analysts use in financial statement analysis besides annual financial statements and supplementary information.",
        "question": "An equity analyst seeking information on executive compensation, board committee structures, and transactions with affiliated parties would most likely consult which of the following regulatory filings?",
        "options": {
            "A": "Form 8-K.",
            "B": "Form 10-Q.",
            "C": "Proxy statement (DEF 14A)."
        },
        "answer": "C",
        "explanation": "Proxy statements (filed as Form DEF 14A in the United States) are distributed to shareholders prior to the annual general meeting and disclose executive remuneration, equity awards, board member biographies, governance practices, and potential conflicts of interest / related-party transactions.\n\nDistractor Analysis:\n- A (Form 8-K) is used to report major unscheduled corporate events (material acquisitions, changes in management, bankruptcy, auditor resignation).\n- B (Form 10-Q) is the quarterly report containing unaudited interim financial statements and management commentary."
    },
    {
        "id": "L1-Q011",
        "level": 1,
        "module": "m1-intro",
        "topic": "Introduction to Financial Statement Analysis",
        "los": "LOS 19.f: Describe the steps in the financial statement analysis framework.",
        "question": "In the standard six-step financial statement analysis framework, which of the following tasks is performed during the 'Process data' phase?",
        "options": {
            "A": "Stating the purpose and context of the analysis.",
            "B": "Computing financial ratios, common-size financial statements, and preparing graphical charts.",
            "C": "Formulating investment recommendations and preparing the final synthesis report."
        },
        "answer": "B",
        "explanation": "The six steps in the financial statement analysis framework are:\n1. State the objective and context.\n2. Gather data.\n3. Process data (computing ratios, developing common-size statements, adjusting statements).\n4. Analyze/interpret the processed data.\n5. Develop and communicate conclusions and recommendations.\n6. Follow up.\n\nDistractor Analysis:\n- A is Step 1 (State the objective and context).\n- C is Step 5 (Develop and communicate conclusions/recommendations)."
    },
    {
        "id": "L1-Q012",
        "level": 1,
        "module": "m1-intro",
        "topic": "Introduction to Financial Statement Analysis",
        "los": "LOS 20.b: Describe the accounting equation and the process of recording business transactions.",
        "question": "A merchant sells merchandise inventory that originally cost 50,000 USD to a customer on credit for 85,000 USD. What is the immediate net impact on the merchant's total assets and shareholders' equity?",
        "options": {
            "A": "Total assets increase by 35,000 USD; Shareholders' equity increases by 35,000 USD.",
            "B": "Total assets increase by 85,000 USD; Shareholders' equity increases by 85,000 USD.",
            "C": "Total assets increase by 35,000 USD; Shareholders' equity remains unchanged."
        },
        "answer": "A",
        "explanation": "This transaction involves two simultaneous entries:\n1. Revenue recognition: Accounts Receivable increases by 85,000 USD; Revenue increases by 85,000 USD (increasing Equity via Net Income).\n2. Expense recognition: Inventory decreases by 50,000 USD; Cost of Goods Sold increases by 50,000 USD (reducing Equity via Net Income).\n\nNet effects:\n- Assets: $+85,000\\text{ USD (AR)} - 50,000\\text{ USD (Inventory)} = +35,000\\text{ USD}$.\n- Equity: $+85,000\\text{ USD (Revenue)} - 50,000\\text{ USD (COGS)} = +35,000\\text{ USD}$.\n\nDistractor Analysis:\n- B records the revenue side while ignoring the cost of inventory derecognition.\n- C recognizes the asset change but fails to reflect the gross profit of 35,000 USD flowing to retained earnings."
    },
    {
        "id": "L1-Q013",
        "level": 1,
        "module": "m1-intro",
        "topic": "Introduction to Financial Statement Analysis",
        "los": "LOS 19.b: Describe the roles of the key financial statements and how they are interrelated.",
        "question": "A manufacturing company's financial records show that total assets increased by 120,000 USD and total liabilities decreased by 40,000 USD during the fiscal year. If the company issued 50,000 USD of new common equity and paid 30,000 USD in cash dividends, what was its net income for the year?",
        "options": {
            "A": "80,000 USD",
            "B": "140,000 USD",
            "C": "160,000 USD"
        },
        "answer": "B",
        "explanation": "Using the expanded accounting equation:\n$$\\Delta\\text{Assets} = \\Delta\\text{Liabilities} + \\Delta\\text{Equity}$$\nGiven $\\Delta\\text{Assets} = +120,000\\text{ USD}$ and $\\Delta\\text{Liabilities} = -40,000\\text{ USD}$:\n$$+120,000\\text{ USD} = -40,000\\text{ USD} + \\Delta\\text{Equity} \\implies \\Delta\\text{Equity} = 160,000\\text{ USD}$$\nEquity changes via capital contributions, dividends, and net income:\n$$\\Delta\\text{Equity} = \\text{Stock Issued} - \\text{Dividends Paid} + \\text{Net Income}$$\n$$160,000\\text{ USD} = 50,000\\text{ USD} - 30,000\\text{ USD} + \\text{Net Income}$$\n$$160,000\\text{ USD} = 20,000\\text{ USD} + \\text{Net Income} \\implies \\text{Net Income} = 140,000\\text{ USD}$$\n\nDistractor Analysis:\n- A incorrectly calculates $\\Delta\\text{Equity} = 120,000 - 40,000 = 80,000\\text{ USD}$, leading to $80,000 - 20,000 = 60,000\\text{ USD}$ or similar missteps.\n- C represents the total change in equity ($160,000\\text{ USD}$) without subtracting net capital contributions ($50,000 - 30,000 = 20,000\\text{ USD}$)."
    },
    {
        "id": "L1-Q014",
        "level": 1,
        "module": "m1-intro",
        "topic": "Introduction to Financial Statement Analysis",
        "los": "LOS 20.c: Describe accrual accounting and the need for accruals and other adjustments.",
        "question": "A consulting company provides 75,000 USD of services to a client in December Year 1. The client will not be billed until January Year 2, and payment is expected in February Year 2. If the consulting company correctly applies accrual accounting, what adjusting entry is required on 31 December Year 1?",
        "options": {
            "A": "Debit Cash 75,000 USD, Credit Service Revenue 75,000 USD.",
            "B": "Debit Unbilled Receivables (Accrued Asset) 75,000 USD, Credit Service Revenue 75,000 USD.",
            "C": "No entry is required until an official invoice is generated in January Year 2."
        },
        "answer": "B",
        "explanation": "Because the service obligation was performed in December Year 1, revenue must be recognized in Year 1 to satisfy accrual accounting principles, even though no invoice has been sent.\n- Debit: Accrued (Unbilled) Receivables (an asset account) for 75,000 USD.\n- Credit: Service Revenue (an income statement account) for 75,000 USD.\n\nDistractor Analysis:\n- A is incorrect because no cash was received in December.\n- C is incorrect because waiting for billing violates accrual accounting and understates revenue and assets for Year 1."
    },
    {
        "id": "L1-Q015",
        "level": 1,
        "module": "m1-intro",
        "topic": "Introduction to Financial Statement Analysis",
        "los": "LOS 19.c: Describe the role of the Management Discussion and Analysis (MD&A) section in financial reporting.",
        "question": "Regarding the Management Discussion and Analysis (MD&A) section of a publicly traded company's annual report, which of the following statements is most accurate?",
        "options": {
            "A": "Under SEC rules, MD&A must discuss trends, significant events, capital resources, liquidity, and results of operations, and auditors express a formal audit opinion on its fairness.",
            "B": "MD&A typically contains forward-looking statements and management insights, and although auditors read it for material inconsistencies with the financial statements, it is not audited.",
            "C": "IFRS and US GAAP require identical quantitative disclosures within the MD&A section, prohibiting qualitative assessments."
        },
        "answer": "B",
        "explanation": "MD&A provides management's perspective on financial conditions, operating results, liquidity, capital commitments, and future uncertainties. While independent auditors review the MD&A to verify that its contents are not materially inconsistent with the audited financial statements, the MD&A itself is unaudited and does not receive an audit opinion.\n\nDistractor Analysis:\n- A is incorrect because auditors do not audit or issue an opinion on the MD&A section.\n- C is incorrect because MD&A is largely qualitative and narrative in nature, and regulatory requirements differ across jurisdictions."
    }
]
