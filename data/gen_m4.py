# Module 4: Understanding Balance Sheets
# Questions L1-Q046 to L1-Q060 (15 questions)

questions = [
    {
        "id": "L1-Q046",
        "level": 1,
        "module": "m4-balance-sheet",
        "topic": "Understanding Balance Sheets",
        "los": "LOS 23.a: Describe the elements of the balance sheet: current and non-current assets and liabilities.",
        "question": "Under both IFRS and US GAAP, an asset or liability is classified as 'current' if it is expected to be settled, realized, or consumed within:",
        "options": {
            "A": "Exactly 12 calendar months, irrespective of the operating cycle length.",
            "B": "One year or one operating cycle, whichever is longer.",
            "C": "The current fiscal quarter or 90 days."
        },
        "answer": "B",
        "explanation": "Current assets and liabilities are those expected to be converted into cash, consumed, or settled within one year or one normal operating cycle, whichever is longer. The operating cycle is the time required to convert cash into inventory, inventory into accounts receivable, and accounts receivable back into cash.\n\nDistractor Analysis:\n- A is incorrect because for industries with multi-year operating cycles (e.g., aerospace manufacturing, wine aging, shipbuilding), items exceeding 12 months are still classified as current if within the normal operating cycle.\n- C is arbitrary and refers to short-term money market instruments."
    },
    {
        "id": "L1-Q047",
        "level": 1,
        "module": "m4-balance-sheet",
        "topic": "Understanding Balance Sheets",
        "los": "LOS 23.a: Describe the elements of the balance sheet: current and non-current assets and liabilities.",
        "question": "Under International Financial Reporting Standards (IFRS), a company is permitted to present balance sheet items based on liquidity rather than current versus non-current classification when:",
        "options": {
            "A": "The company operates in the technology or retail sector.",
            "B": "A liquidity-based presentation provides information that is reliable and more relevant than a classified presentation.",
            "C": "Shareholders vote by a two-thirds majority at the annual meeting to waive standard presentation."
        },
        "answer": "B",
        "explanation": "IAS 1 allows entities (such as commercial banks and financial institutions) to present assets and liabilities in order of liquidity (either ascending or descending) rather than using a classified current/non-current format, provided that a liquidity presentation provides information that is reliable and more relevant.\n\nDistractor Analysis:\n- A is incorrect because retail and tech companies typically operate with distinct current operating cycles and must use classified presentations.\n- C is incorrect because presentation formats are dictated by accounting standards, not shareholder voting."
    },
    {
        "id": "L1-Q048",
        "level": 1,
        "module": "m4-balance-sheet",
        "topic": "Understanding Balance Sheets",
        "los": "LOS 23.b: Describe measurement bases for assets and liabilities.",
        "question": "At year-end, a company reports gross accounts receivable of 800,000 USD. Based on historical default rates and aging analysis, management estimates that 5% of gross receivables will prove uncollectible. The beginning balance in the Allowance for Doubtful Accounts was 15,000 USD (credit), and 8,000 USD of bad debts were written off during the year. What bad debt expense should be recognized on the income statement, and what is the net realizable value of accounts receivable on the balance sheet?",
        "options": {
            "A": "Bad Debt Expense: 33,000 USD; Net Accounts Receivable: 760,000 USD.",
            "B": "Bad Debt Expense: 40,000 USD; Net Accounts Receivable: 760,000 USD.",
            "C": "Bad Debt Expense: 25,000 USD; Net Accounts Receivable: 775,000 USD."
        },
        "answer": "A",
        "explanation": "1. Required ending balance in Allowance for Doubtful Accounts:\n$$\\text{Ending Allowance} = 5\\% \\times 800,000\\text{ USD} = 40,000\\text{ USD}$$\n2. Net Realizable Value (NRV) on the balance sheet:\n$$\\text{Net AR} = \\text{Gross AR} - \\text{Ending Allowance} = 800,000\\text{ USD} - 40,000\\text{ USD} = 760,000\\text{ USD}$$\n3. Analysis of the Allowance account to find Bad Debt Expense:\n$$\\text{Ending Allowance} = \\text{Beginning Allowance} - \\text{Write-offs} + \\text{Bad Debt Expense}$$\n$$40,000\\text{ USD} = 15,000\\text{ USD} - 8,000\\text{ USD} + \\text{Bad Debt Expense}$$\n$$40,000\\text{ USD} = 7,000\\text{ USD} + \\text{Bad Debt Expense} \\implies \\text{Bad Debt Expense} = 33,000\\text{ USD}$$\n\nDistractor Analysis:\n- B incorrectly sets bad debt expense equal to the desired ending allowance of 40,000 USD, ignoring the unadjusted existing balance in the allowance.\n- C makes errors in calculating the allowance progression."
    },
    {
        "id": "L1-Q049",
        "level": 1,
        "module": "m4-balance-sheet",
        "topic": "Understanding Balance Sheets",
        "los": "LOS 23.b: Describe measurement bases for assets and liabilities.",
        "question": "A manufacturer holds inventory with an original cost of 120,000 USD. At year-end, the estimated selling price is 115,000 USD, with estimated selling costs of 5,000 USD and replacement cost of 105,000 USD. In the subsequent year, market conditions recover and the estimated selling price rises to 135,000 USD (selling costs 5,000 USD). Which statement correctly describes the accounting under IFRS versus US GAAP (assuming FIFO)?",
        "options": {
            "A": "Under both IFRS and US GAAP, the inventory is written down to 110,000 USD in Year 1, and the write-down can be reversed up to original cost in Year 2.",
            "B": "Under both IFRS and US GAAP, the inventory is written down to 110,000 USD in Year 1, but IFRS permits reversing the write-down up to original cost in Year 2, whereas US GAAP strictly prohibits any reversal.",
            "C": "Under IFRS the inventory is written down to 105,000 USD, while under US GAAP it is written down to 110,000 USD, with neither permitting reversals."
        },
        "answer": "B",
        "explanation": "Under IFRS, inventory is measured at the lower of cost and net realizable value (NRV):\n$$\\text{NRV} = \\text{Estimated Selling Price} - \\text{Estimated Selling Costs} = 115,000\\text{ USD} - 5,000\\text{ USD} = 110,000\\text{ USD}$$\nSince NRV (110,000 USD) < Cost (120,000 USD), a 10,000 USD write-down is recorded in Year 1 under IFRS. Under US GAAP (for FIFO/average cost), the lower of cost and NRV is also used, so it is also written down to 110,000 USD in Year 1.\nIn Year 2, new NRV is $135,000 - 5,000 = 130,000\\text{ USD}$:\n- Under IFRS: Write-downs must be reversed if NRV recovers, limited to the original cost basis (a 10,000 USD recovery is recognized).\n- Under US GAAP: Reversals of inventory write-downs are strictly prohibited once recorded; the written-down carrying value becomes the new cost basis.\n\nDistractor Analysis:\n- A is incorrect because US GAAP prohibits inventory write-down reversals.\n- C is incorrect because under FIFO, both standards evaluate NRV (110,000 USD), not replacement cost."
    },
    {
        "id": "L1-Q050",
        "level": 1,
        "module": "m4-balance-sheet",
        "topic": "Understanding Balance Sheets",
        "los": "LOS 23.c: Describe the classification and measurement of financial assets.",
        "question": "A financial institution purchases corporate debt securities with the contractual objective of holding them solely to collect contractual cash flows consisting exclusively of principal and interest payments. Under IFRS 9, how should these financial assets be classified and measured?",
        "options": {
            "A": "Fair value through profit or loss (FVPL).",
            "B": "Amortized cost.",
            "C": "Fair value through other comprehensive income (FVOCI)."
        },
        "answer": "B",
        "explanation": "Under IFRS 9, a financial asset is measured at amortized cost if it meets two criteria:\n1. Business Model Test: The objective of the business model is to hold the financial asset to collect contractual cash flows.\n2. Cash Flow Characteristics (SPPI Test): The contractual cash flows represent solely payments of principal and interest (SPPI) on specified dates.\n\nDistractor Analysis:\n- A (FVPL) applies to debt securities held for trading or those that fail the SPPI test.\n- C (FVOCI) applies when the business model objective is achieved by BOTH collecting contractual cash flows AND selling financial assets."
    },
    {
        "id": "L1-Q051",
        "level": 1,
        "module": "m4-balance-sheet",
        "topic": "Understanding Balance Sheets",
        "los": "LOS 23.b: Describe measurement bases for assets and liabilities.",
        "question": "Which of the following statements correctly compares the accounting measurement models permitted for Property, Plant, and Equipment (PP&E) under IFRS versus US GAAP?",
        "options": {
            "A": "IFRS allows either the cost model or the revaluation model, whereas US GAAP allows only the cost model.",
            "B": "US GAAP allows either the cost model or the revaluation model, whereas IFRS requires the fair value model.",
            "C": "Both IFRS and US GAAP permit companies to freely revalue PP&E to fair value through other comprehensive income."
        },
        "answer": "A",
        "explanation": "Under IAS 16, a company may choose either the cost model (historical cost less accumulated depreciation and impairment) or the revaluation model (fair value at revaluation date less subsequent depreciation) for an entire class of PP&E. Under US GAAP, the revaluation model is strictly prohibited, and only the cost model is permitted.\n\nDistractor Analysis:\n- B and C are incorrect because US GAAP prohibits the revaluation model for PP&E."
    },
    {
        "id": "L1-Q052",
        "level": 1,
        "module": "m4-balance-sheet",
        "topic": "Understanding Balance Sheets",
        "los": "LOS 23.b: Describe measurement bases for assets and liabilities.",
        "question": "Under IFRS (IAS 40), how is an investment property measured if the entity elects the fair value model?",
        "options": {
            "A": "At historical cost less accumulated depreciation, with fair value disclosed in the footnotes.",
            "B": "At fair value at each reporting date, with all changes in fair value recognized directly in profit or loss, and no depreciation is recorded.",
            "C": "At fair value at each reporting date, with unrealized revaluation gains recognized in Other Comprehensive Income (revaluation surplus)."
        },
        "answer": "B",
        "explanation": "Under IAS 40 Investment Property, if a firm elects the fair value model:\n- The property is remeasured to fair value at each balance sheet date.\n- All fair value changes (both gains and losses) are recognized directly in profit or loss (income statement).\n- No depreciation expense is recorded on the investment property.\n(Note: This differs from the PP&E revaluation model under IAS 16, where upward revaluations typically go to OCI / revaluation surplus).\n\nDistractor Analysis:\n- A describes the cost model for investment property.\n- C describes the PP&E revaluation model under IAS 16, not the IAS 40 fair value model."
    },
    {
        "id": "L1-Q053",
        "level": 1,
        "module": "m4-balance-sheet",
        "topic": "Understanding Balance Sheets",
        "los": "LOS 23.b: Describe measurement bases for assets and liabilities.",
        "question": "During Year 1, a pharmaceutical firm spends 5,000,000 USD on basic scientific research to discover new molecular compounds, and 8,000,000 USD on clinical trials developing a specific drug whose technical and commercial feasibility has been proven. How should these expenditures be accounted for under IFRS versus US GAAP?",
        "options": {
            "A": "Under IFRS, 5,000,000 USD is expensed and 8,000,000 USD is capitalized; under US GAAP, the entire 13,000,000 USD is expensed.",
            "B": "Under both IFRS and US GAAP, the entire 13,000,000 USD must be capitalized as an intangible asset.",
            "C": "Under IFRS, the entire 13,000,000 USD is expensed; under US GAAP, 8,000,000 USD is capitalized."
        },
        "answer": "A",
        "explanation": "Under IAS 38 (IFRS):\n- Research costs must always be expensed as incurred (5,000,000 USD).\n- Development costs must be capitalized as an intangible asset once technical feasibility, intent to complete, ability to use or sell, and probable future economic benefits are established (8,000,000 USD capitalized).\nUnder US GAAP:\n- Both research and development costs must generally be expensed as incurred (with narrow exceptions for software development for sale or internal use). Therefore, under US GAAP, the full 13,000,000 USD is expensed.\n\nDistractor Analysis:\n- B is incorrect because research costs cannot be capitalized under either standard.\n- C reverses the standards."
    },
    {
        "id": "L1-Q054",
        "level": 1,
        "module": "m4-balance-sheet",
        "topic": "Understanding Balance Sheets",
        "los": "LOS 23.b: Describe measurement bases for assets and liabilities.",
        "question": "Which of the following statements regarding accounting for goodwill is most accurate under both IFRS and US GAAP?",
        "options": {
            "A": "Internally generated goodwill may be capitalized if its fair value can be verified by independent appraisers.",
            "B": "Goodwill arising from a business combination is amortized on a straight-line basis over an estimated useful life not exceeding 20 years.",
            "C": "Goodwill is not amortized; instead, it is tested for impairment at least annually."
        },
        "answer": "C",
        "explanation": "Under both IFRS (IAS 36) and US GAAP (ASC 350):\n- Goodwill can only arise in a business combination (purchase acquisition); internally generated goodwill is NEVER recognized.\n- Goodwill has an indefinite life and is NOT amortized.\n- Goodwill must be tested for impairment at least annually (or more frequently if triggering events occur).\n\nDistractor Analysis:\n- A is incorrect because internally generated goodwill is strictly prohibited from recognition.\n- B was the legacy accounting standard prior to the adoption of the impairment-only model."
    },
    {
        "id": "L1-Q055",
        "level": 1,
        "module": "m4-balance-sheet",
        "topic": "Understanding Balance Sheets",
        "los": "LOS 23.a: Describe the elements of the balance sheet: current and non-current assets and liabilities.",
        "question": "Which of the following liabilities is classified as an accrued liability rather than a trade account payable?",
        "options": {
            "A": "An unpaid invoice for raw steel shipments received from a primary manufacturing vendor due in 30 days.",
            "B": "Unpaid wages earned by factory workers for the final two weeks of the fiscal year to be disbursed on the next payroll date.",
            "C": "An advance customer deposit received for goods to be manufactured next quarter."
        },
        "answer": "B",
        "explanation": "Accrued liabilities (accrued expenses) are expenses that have been incurred and recognized on the income statement but have not yet been billed or paid in cash (e.g., accrued salaries, accrued warranty costs, accrued interest). Trade accounts payable represent unpaid invoices received from commercial suppliers for goods/services purchased on credit.\n\nDistractor Analysis:\n- A is a standard trade account payable.\n- C is unearned (deferred) revenue."
    },
    {
        "id": "L1-Q056",
        "level": 1,
        "module": "m4-balance-sheet",
        "topic": "Understanding Balance Sheets",
        "los": "LOS 23.b: Describe measurement bases for assets and liabilities.",
        "question": "When a company issues long-term fixed-rate bonds at a discount to par value, how does the carrying amount of the bond liability on the balance sheet change over its life under the effective interest rate method?",
        "options": {
            "A": "The carrying amount increases over time toward the face value.",
            "B": "The carrying amount decreases over time toward zero.",
            "C": "The carrying amount remains constant at the initial net proceeds."
        },
        "answer": "A",
        "explanation": "When bonds are issued at a discount (market rate > coupon rate), the initial carrying amount is less than par value. Under the effective interest rate method, the discount is amortized over the bond's term, with interest expense exceeding coupon interest paid. This amortization increases the carrying amount each period until it converges to the face (par) value at maturity.\n\nDistractor Analysis:\n- B describes a bond issued at a premium (where carrying value decreases toward par).\n- C describes an accounting error failing to amortize bond discount."
    },
    {
        "id": "L1-Q057",
        "level": 1,
        "module": "m4-balance-sheet",
        "topic": "Understanding Balance Sheets",
        "los": "LOS 23.d: Describe the components of shareholders' equity.",
        "question": "Which of the following components of shareholders' equity represents cumulative net income that has not been distributed to shareholders as dividends?",
        "options": {
            "A": "Additional paid-in capital (share premium).",
            "B": "Retained earnings.",
            "C": "Accumulated other comprehensive income (AOCI)."
        },
        "answer": "B",
        "explanation": "Retained earnings represent the cumulative undistributed earnings of the company since inception, calculated as cumulative net income less cumulative dividends declared (both cash and stock dividends).\n\nDistractor Analysis:\n- A (APIC / share premium) is the excess of proceeds received from issuing stock over its par value.\n- C (AOCI) accumulates other comprehensive income items (e.g., foreign currency translation, cash flow hedges, unrealized gains on FVOCI securities) that bypass net income."
    },
    {
        "id": "L1-Q058",
        "level": 1,
        "module": "m4-balance-sheet",
        "topic": "Understanding Balance Sheets",
        "los": "LOS 23.d: Describe the components of shareholders' equity.",
        "question": "A corporation repurchases 50,000 shares of its own 10 USD par common stock in the open market for 45 USD per share and holds them as treasury stock. What is the immediate effect of this transaction on the company's financial statements?",
        "options": {
            "A": "An investment asset increases by 2,250,000 USD, and cash decreases by 2,250,000 USD.",
            "B": "Total shareholders' equity decreases by 2,250,000 USD, and common shares outstanding decrease by 50,000.",
            "C": "Net income decreases by 2,250,000 USD due to an investment expense."
        },
        "answer": "B",
        "explanation": "Treasury stock is a contra-equity account (not an asset). Repurchasing shares reduces cash (Asset) and increases Treasury Stock (a deduction from Equity), resulting in a net decrease in total shareholders' equity of:\n$$50,000 \\times 45\\text{ USD} = 2,250,000\\text{ USD}$$\nTreasury shares carry no voting rights, receive no dividends, and reduce the number of common shares outstanding (though shares issued remains unchanged).\n\nDistractor Analysis:\n- A is incorrect because a firm cannot own an investment asset in its own stock.\n- C is incorrect because repurchasing stock is a financing equity transaction and has zero impact on the income statement."
    },
    {
        "id": "L1-Q059",
        "level": 1,
        "module": "m4-balance-sheet",
        "topic": "Understanding Balance Sheets",
        "los": "LOS 23.d: Describe the components of shareholders' equity.",
        "question": "In a consolidated balance sheet, how is 'non-controlling interest' (minority interest) presented?",
        "options": {
            "A": "As a non-current liability between long-term debt and equity.",
            "B": "As a separate component within total shareholders' equity.",
            "C": "As an offset against consolidated goodwill within non-current assets."
        },
        "answer": "B",
        "explanation": "Under both IFRS and US GAAP, non-controlling interest (NCI) represents the equity interest in a consolidated subsidiary not attributable, directly or indirectly, to the parent company. It must be presented within the total equity section of the consolidated balance sheet, distinctly separated from the parent's shareholders' equity.\n\nDistractor Analysis:\n- A was an obsolete 'mezzanine' presentation prior to modern accounting standards.\n- C is incorrect because NCI is an equity claim, not an asset contra-account."
    },
    {
        "id": "L1-Q060",
        "level": 1,
        "module": "m4-balance-sheet",
        "topic": "Understanding Balance Sheets",
        "los": "LOS 23.e: Convert balance sheets to common-size balance sheets and interpret them.",
        "question": "In a vertical common-size balance sheet, each line item is normalized and presented as a percentage of:",
        "options": {
            "A": "Total equity.",
            "B": "Total assets.",
            "C": "Total current assets."
        },
        "answer": "B",
        "explanation": "In a vertical common-size balance sheet, every asset, liability, and equity line item is divided by total assets (or total liabilities and equity), expressing each balance as a percentage of total assets. This standardizes the balance sheet across companies of different scales and across multiple time periods.\n\nDistractor Analysis:\n- A and C are specific subgroups that do not serve as the universal denominator for vertical common-size balance sheets."
    }
]
