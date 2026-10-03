# Module 3: Understanding Income Statements
# Questions L1-Q031 to L1-Q045 (15 questions)

questions = [
    {
        "id": "L1-Q031",
        "level": 1,
        "module": "m3-income-statement",
        "topic": "Understanding Income Statements",
        "los": "LOS 22.a: Describe the five-step model for recognizing revenue under IFRS 15 and ASC Topic 606.",
        "question": "Which of the following correctly identifies the third step in the core five-step revenue recognition model established under IFRS 15 and ASC Topic 606?",
        "options": {
            "A": "Identify the performance obligations in the contract.",
            "B": "Determine the transaction price.",
            "C": "Allocate the transaction price to the performance obligations."
        },
        "answer": "B",
        "explanation": "The converged five-step revenue recognition model consists of:\n1. Identify the contract with a customer.\n2. Identify the performance obligations in the contract.\n3. Determine the transaction price.\n4. Allocate the transaction price to the performance obligations in the contract.\n5. Recognize revenue when (or as) the entity satisfies a performance obligation.\n\nDistractor Analysis:\n- A is Step 2.\n- C is Step 4."
    },
    {
        "id": "L1-Q032",
        "level": 1,
        "module": "m3-income-statement",
        "topic": "Understanding Income Statements",
        "los": "LOS 22.b: Calculate revenue and gross profit under the percentage-of-completion (over time) method.",
        "question": "A construction company enters into a fixed-price contract to build a commercial bridge for 12,000,000 USD. Total estimated construction costs are 9,000,000 USD. In Year 1, the company incurs 2,700,000 USD in construction costs and bills the client 3,500,000 USD, receiving 3,000,000 USD in cash. Using the percentage-of-completion input method (cost-to-cost), how much revenue and gross profit should the company recognize in Year 1?",
        "options": {
            "A": "Revenue: 3,600,000 USD; Gross Profit: 900,000 USD.",
            "B": "Revenue: 3,500,000 USD; Gross Profit: 800,000 USD.",
            "C": "Revenue: 3,000,000 USD; Gross Profit: 300,000 USD."
        },
        "answer": "A",
        "explanation": "Under the cost-to-cost input method, progress toward completion is measured as:\n$$\\text{Percentage of Completion} = \\frac{\\text{Cumulative Costs Incurred}}{\\text{Total Estimated Costs}} = \\frac{2,700,000\\text{ USD}}{9,000,000\\text{ USD}} = 30\\%$$\n1. Revenue Recognized Year 1:\n$$\\text{Revenue} = 30\\% \\times 12,000,000\\text{ USD} = 3,600,000\\text{ USD}$$\n2. Cost of Construction Recognized Year 1:\n$$\\text{Costs} = 2,700,000\\text{ USD}$$\n3. Gross Profit Recognized Year 1:\n$$\\text{Gross Profit} = 3,600,000\\text{ USD} - 2,700,000\\text{ USD} = 900,000\\text{ USD}$$\nEquivalently, total expected profit is $12,000,000 - 9,000,000 = 3,000,000\\text{ USD}$, and $30\\% \\times 3,000,000 = 900,000\\text{ USD}$.\nNote: Amounts billed (3,500,000 USD) and cash collected (3,000,000 USD) affect balance sheet accounts (accounts receivable and contract asset/liability) but do not dictate revenue recognition.\n\nDistractor Analysis:\n- B incorrectly uses the billed amount as revenue ($3,500,000 - 2,700,000 = 800,000\\text{ USD}$).\n- C incorrectly uses the cash collected as revenue ($3,000,000 - 2,700,000 = 300,000\\text{ USD}$)."
    },
    {
        "id": "L1-Q033",
        "level": 1,
        "module": "m3-income-statement",
        "topic": "Understanding Income Statements",
        "los": "LOS 22.a: Describe the five-step model for recognizing revenue under IFRS 15 and ASC Topic 606.",
        "question": "Under IFRS 15 and ASC 606, when contract consideration includes a variable amount (e.g., performance bonuses or volume discounts), an entity may include variable consideration in the transaction price only to the extent that:",
        "options": {
            "A": "Cash has been received in full in an escrow account.",
            "B": "It is highly probable that a significant reversal in the amount of cumulative revenue recognized will not occur.",
            "C": "The customer signs an unconditional waiver forfeiting all legal claims to performance verification."
        },
        "answer": "B",
        "explanation": "Standard setters impose a constraint on variable consideration: an entity may include an estimate of variable consideration in the transaction price only to the extent that it is highly probable (under US GAAP: 'probable') that a significant reversal in the cumulative revenue recognized will not occur once the uncertainty is resolved.\n\nDistractor Analysis:\n- A is incorrect because accrual accounting does not require cash in escrow.\n- C is incorrect because standard commercial contracts do not require liability waivers to recognize variable revenue."
    },
    {
        "id": "L1-Q034",
        "level": 1,
        "module": "m3-income-statement",
        "topic": "Understanding Income Statements",
        "los": "LOS 22.c: Compare the accounting treatment and presentation for principal versus agent transactions.",
        "question": "An online travel portal arranges hotel bookings for travelers. The portal does not control the hotel rooms before transfer, has no inventory risk, and receives a 12% commission on each 500 USD booking. How should the portal report revenue for each booking?",
        "options": {
            "A": "Gross reporting: 500 USD revenue and 440 USD cost of sales.",
            "B": "Net reporting: 60 USD revenue and 0 USD cost of sales.",
            "C": "Gross reporting: 500 USD revenue and 60 USD commission expense."
        },
        "answer": "B",
        "explanation": "Because the portal does not control the service before it is provided to the customer, does not bear inventory risk, and acts solely as an intermediary matching customers with hotels, it acts as an agent rather than a principal. An agent recognizes revenue on a net basis equal to the commission or fee earned:\n$$\\text{Revenue} = 12\\% \\times 500\\text{ USD} = 60\\text{ USD}$$\n\nDistractor Analysis:\n- A and C apply gross reporting, which is permitted only when the entity is the principal (controls the goods/services, bears inventory risk, and sets prices)."
    },
    {
        "id": "L1-Q035",
        "level": 1,
        "module": "m3-income-statement",
        "topic": "Understanding Income Statements",
        "los": "LOS 22.d: Describe general principles of expense recognition and specific expense items.",
        "question": "Which of the following expenditures is best classified as a period cost rather than a product cost, and must therefore be expensed in the period incurred?",
        "options": {
            "A": "Direct labor costs incurred in assembling finished goods.",
            "B": "Depreciation of factory machinery used in manufacturing.",
            "C": "Chief executive officer and corporate headquarters administrative salaries."
        },
        "answer": "C",
        "explanation": "Period costs are expensed in the period incurred because they cannot be directly matched to specific revenues or capitalized into inventory. Corporate administrative expenses, executive salaries, and marketing expenses are period costs. Product costs (direct materials, direct labor, and manufacturing overhead including factory depreciation) are capitalized as inventory and expensed as Cost of Goods Sold (COGS) only when the inventory is sold under the matching principle.\n\nDistractor Analysis:\n- A is direct labor (product cost, capitalized into inventory until sold).\n- B is manufacturing overhead (product cost, capitalized into inventory until sold)."
    },
    {
        "id": "L1-Q036",
        "level": 1,
        "module": "m3-income-statement",
        "topic": "Understanding Income Statements",
        "los": "LOS 22.e: Describe the financial reporting treatment and analysis of non-recurring items.",
        "question": "In Year 2, a diversified conglomerate votes to dispose of its retail textile division, which represents a separate major line of business. The division incurred an operating loss of 4,000,000 USD during Year 2 and was sold at a pre-tax loss of 2,000,000 USD. If the applicable corporate income tax rate is 25%, how should these events be presented on the Year 2 income statement?",
        "options": {
            "A": "Included in operating expenses within continuing operations as a 6,000,000 USD pre-tax charge.",
            "B": "Reported separately below income from continuing operations as discontinued operations, net of tax at 4,500,000 USD.",
            "C": "Reported directly as a 4,500,000 USD deduction in other comprehensive income (OCI)."
        },
        "answer": "B",
        "explanation": "A component of an entity that is disposed of and represents a separate major line of business or geographical area of operations qualifies for discontinued operations treatment. Discontinued operations are reported separately below income from continuing operations on a net-of-tax basis.\n- Total pre-tax loss = $4,000,000\\text{ USD (operating loss)} + 2,000,000\\text{ USD (loss on sale)} = 6,000,000\\text{ USD}$.\n- Tax benefit = $25\\% \\times 6,000,000\\text{ USD} = 1,500,000\\text{ USD}$.\n- Loss from discontinued operations (net of tax) = $6,000,000\\text{ USD} \\times (1 - 0.25) = 4,500,000\\text{ USD}$.\n\nDistractor Analysis:\n- A is incorrect because discontinued operations must be segregated below income from continuing operations.\n- C is incorrect because discontinued operations flow through net income, not OCI."
    },
    {
        "id": "L1-Q037",
        "level": 1,
        "module": "m3-income-statement",
        "topic": "Understanding Income Statements",
        "los": "LOS 22.e: Describe the financial reporting treatment and analysis of non-recurring items.",
        "question": "How should a material, unusual or infrequent item—such as an impairment charge from restructuring a production plant—be presented on the income statement under IFRS and US GAAP?",
        "options": {
            "A": "As a separate line item within income from continuing operations, disclosed on a pre-tax basis.",
            "B": "Below net income from continuing operations, net of tax, labeled as an extraordinary item.",
            "C": "Directly in the statement of changes in equity, bypassing the income statement entirely."
        },
        "answer": "A",
        "explanation": "Items that are unusual in nature or infrequent in occurrence (such as restructuring charges or asset write-downs) must be presented as a separate component of income from continuing operations (pre-tax) and disclosed in the footnotes. Both IFRS and US GAAP prohibit the classification of any item as 'extraordinary'.\n\nDistractor Analysis:\n- B is incorrect because 'extraordinary items' have been eliminated from both IFRS and US GAAP.\n- C is incorrect because operating impairments and restructuring costs must be recognized on the income statement."
    },
    {
        "id": "L1-Q038",
        "level": 1,
        "module": "m3-income-statement",
        "topic": "Understanding Income Statements",
        "los": "LOS 22.f: Calculate and interpret basic and diluted earnings per share.",
        "question": "A corporation reports net income of 7,500,000 USD for the year ended 31 December Year 1. During the year, it had 100,000 shares of 8% cumulative preferred stock (100 USD par value) outstanding, on which no dividends were declared this year. Common shares outstanding were:\n- 1 January: 2,000,000 shares\n- 1 May: Issued 600,000 new shares\n- 1 September: Repurchased 300,000 shares as treasury stock\nWhat is the company's Basic EPS for Year 1?",
        "options": {
            "A": "2.91 USD",
            "B": "3.26 USD",
            "C": "2.83 USD"
        },
        "answer": "A",
        "explanation": "1. Preferred Dividends:\nBecause the preferred stock is cumulative, the preferred dividend must be subtracted from net income regardless of whether it was declared:\n$$\\text{Preferred Dividends} = 100,000\\text{ shares} \\times 100\\text{ USD} \\times 8\\% = 800,000\\text{ USD}$$\n$$\\text{Income Available to Common} = 7,500,000\\text{ USD} - 800,000\\text{ USD} = 6,700,000\\text{ USD}$$\n\n2. Weighted Average Number of Common Shares (WANCS):\n- Jan 1 to May 1 (4 months): $2,000,000 \\times (4/12) = 666,667$\n- May 1 to Sept 1 (4 months): $(2,000,000 + 600,000) \\times (4/12) = 2,600,000 \\times (4/12) = 866,667$\n- Sept 1 to Dec 31 (4 months): $(2,600,000 - 300,000) \\times (4/12) = 2,300,000 \\times (4/12) = 766,667$\n$$\\text{WANCS} = 2,000,000 + 600,000 \\times \\left(\\frac{8}{12}\\right) - 300,000 \\times \\left(\\frac{4}{12}\\right) = 2,000,000 + 400,000 - 100,000 = 2,300,000\\text{ shares}$$\n\n3. Basic EPS:\n$$\\text{Basic EPS} = \\frac{6,700,000\\text{ USD}}{2,300,000\\text{ shares}} = 2.913\\text{ USD} \\approx 2.91\\text{ USD}$$\n\nDistractor Analysis:\n- B fails to deduct cumulative preferred dividends: $7,500,000 / 2,300,000 = 3.26\\text{ USD}$.\n- C uses end-of-year shares ($2,300,000$) or unweighted averages incorrectly."
    },
    {
        "id": "L1-Q039",
        "level": 1,
        "module": "m3-income-statement",
        "topic": "Understanding Income Statements",
        "los": "LOS 22.f: Calculate and interpret basic and diluted earnings per share.",
        "question": "A firm had 1,000,000 common shares outstanding on 1 January. On 1 April, it issued 200,000 additional shares. On 1 July, the firm declared and distributed a 20% stock dividend. On 1 October, it issued another 100,000 shares. What is the weighted average number of common shares for computing EPS for the year?",
        "options": {
            "A": "1,350,000 shares",
            "B": "1,405,000 shares",
            "C": "1,480,000 shares"
        },
        "answer": "B",
        "explanation": "Stock dividends and stock splits are treated as having occurred at the beginning of the earliest period presented. Therefore, all shares outstanding prior to the stock dividend must be multiplied by the factor $(1 + 0.20) = 1.20$:\n1. 1 Jan shares: $1,000,000 \\times 1.20 \\times (12/12) = 1,200,000$\n2. 1 Apr issuance: $200,000 \\times 1.20 \\times (9/12) = 180,000$\n3. 1 Oct issuance (after the stock dividend, so NOT adjusted): $100,000 \\times (3/12) = 25,000$\n\nSum of weighted shares:\n$$\\text{WANCS} = 1,200,000 + 180,000 + 25,000 = 1,405,000\\text{ shares}$$\n\nDistractor Analysis:\n- A fails to adjust the 1 April share issuance for the 20% stock dividend: $1,000,000 \\times 1.20 + 200,000 \\times (9/12) + 100,000 \\times (3/12) = 1,200,000 + 150,000 + 25,000 = 1,375,000$ or applies 1.20 without weighting.\n- C incorrectly applies the 1.20 stock dividend factor to the 1 October issuance as well: $1,405,000 + 5,000 = 1,410,000$ or other calculation errors."
    },
    {
        "id": "L1-Q040",
        "level": 1,
        "module": "m3-income-statement",
        "topic": "Understanding Income Statements",
        "los": "LOS 22.f: Calculate and interpret basic and diluted earnings per share.",
        "question": "A firm has net income of 2,400,000 USD and 800,000 weighted average common shares outstanding. It has 100,000 stock options outstanding throughout the year with an exercise price of 30 USD. The average market price of the common shares during the year was 50 USD. Under the treasury stock method, what is the firm's diluted EPS?",
        "options": {
            "A": "2.67 USD",
            "B": "2.86 USD",
            "C": "3.00 USD"
        },
        "answer": "B",
        "explanation": "Under the treasury stock method:\n1. Proceeds from option exercise:\n$$\\text{Proceeds} = 100,000 \\times 30\\text{ USD} = 3,000,000\\text{ USD}$$\n2. Shares repurchased at average market price:\n$$\\text{Shares repurchased} = \\frac{3,000,000\\text{ USD}}{50\\text{ USD}} = 60,000\\text{ shares}$$\n3. Net incremental shares issued:\n$$\\Delta\\text{Shares} = 100,000 - 60,000 = 40,000\\text{ shares}$$\nAlternatively:\n$$\\Delta\\text{Shares} = 100,000 \\times \\left(1 - \\frac{30}{50}\\right) = 40,000\\text{ shares}$$\n4. Diluted EPS:\n$$\\text{Diluted WANCS} = 800,000 + 40,000 = 840,000\\text{ shares}$$\n$$\\text{Diluted EPS} = \\frac{2,400,000\\text{ USD}}{840,000\\text{ shares}} = 2.857\\text{ USD} \\approx 2.86\\text{ USD}$$\n(Basic EPS was $2,400,000 / 800,000 = 3.00\\text{ USD}$; since $2.86 < 3.00$, the options are dilutive).\n\nDistractor Analysis:\n- A adds the entire 100,000 shares without assuming treasury stock buyback: $2,400,000 / 900,000 = 2.67\\text{ USD}$.\n- C equals Basic EPS, ignoring the dilutive effect of in-the-money options."
    },
    {
        "id": "L1-Q041",
        "level": 1,
        "module": "m3-income-statement",
        "topic": "Understanding Income Statements",
        "los": "LOS 22.f: Calculate and interpret basic and diluted earnings per share.",
        "question": "For Year 1, Zenith Corp. had net income of 4,000,000 USD and 1,000,000 common shares outstanding. Zenith also had 50,000 shares of 6% convertible cumulative preferred stock (100 USD par value) outstanding. Each preferred share is convertible into 4 shares of common stock. What is Zenith's diluted EPS?",
        "options": {
            "A": "3.33 USD",
            "B": "3.70 USD",
            "C": "4.00 USD"
        },
        "answer": "A",
        "explanation": "1. Preferred Dividend:\n$$\\text{Preferred Dividends} = 50,000 \\times 100\\text{ USD} \\times 6\\% = 300,000\\text{ USD}$$\n2. Basic EPS:\n$$\\text{Basic EPS} = \\frac{4,000,000\\text{ USD} - 300,000\\text{ USD}}{1,000,000\\text{ shares}} = \\frac{3,700,000\\text{ USD}}{1,000,000} = 3.70\\text{ USD}$$\n3. If-Converted Method for Diluted EPS:\n- Assume conversion at the beginning of the year.\n- Preferred dividends are avoided: add back 300,000 USD to numerator.\n- New common shares issued = $50,000 \\times 4 = 200,000\\text{ shares}$.\n$$\\text{Diluted EPS} = \\frac{3,700,000\\text{ USD} + 300,000\\text{ USD}}{1,000,000 + 200,000\\text{ shares}} = \\frac{4,000,000\\text{ USD}}{1,200,000\\text{ shares}} = 3.333\\text{ USD} \\approx 3.33\\text{ USD}$$\nSince $3.33\\text{ USD} < 3.70\\text{ USD}$, the preferred shares are dilutive.\n\nDistractor Analysis:\n- B equals Basic EPS (3.70 USD).\n- C incorrectly keeps 4,000,000 USD numerator but divides by 1,000,000 shares."
    },
    {
        "id": "L1-Q042",
        "level": 1,
        "module": "m3-income-statement",
        "topic": "Understanding Income Statements",
        "los": "LOS 22.f: Calculate and interpret basic and diluted earnings per share.",
        "question": "A company has net income of 5,000,000 USD and 2,000,000 weighted average common shares outstanding. It has 10,000,000 USD of 7% convertible bonds outstanding. Each 1,000 USD par bond is convertible into 40 shares of common stock. The corporate tax rate is 30%. What is the diluted EPS?",
        "options": {
            "A": "2.29 USD",
            "B": "2.37 USD",
            "C": "2.50 USD"
        },
        "answer": "A",
        "explanation": "1. Basic EPS:\n$$\\text{Basic EPS} = \\frac{5,000,000\\text{ USD}}{2,000,000\\text{ shares}} = 2.50\\text{ USD}$$\n2. If-Converted Method for Convertible Bonds:\n- Annual interest on bonds = $10,000,000\\text{ USD} \\times 7\\% = 700,000\\text{ USD}$.\n- After-tax interest saved = $700,000\\text{ USD} \\times (1 - 0.30) = 490,000\\text{ USD}$.\n- Number of bonds = $10,000,000 / 1,000 = 10,000\\text{ bonds}$.\n- Incremental common shares = $10,000 \\times 40 = 400,000\\text{ shares}$.\n3. Diluted EPS Calculation:\n$$\\text{Diluted EPS} = \\frac{5,000,000\\text{ USD} + 490,000\\text{ USD}}{2,000,000 + 400,000\\text{ shares}} = \\frac{5,490,000\\text{ USD}}{2,400,000\\text{ shares}} = 2.2875\\text{ USD} \\approx 2.29\\text{ USD}$$\nSince $2.29\\text{ USD} < 2.50\\text{ USD}$, the convertible bonds are dilutive.\n\nDistractor Analysis:\n- B fails to adjust interest for tax savings: $(5,000,000 + 700,000) / 2,400,000 = 5,700,000 / 2,400,000 = 2.375\\text{ USD}$.\n- C is Basic EPS (2.50 USD)."
    },
    {
        "id": "L1-Q043",
        "level": 1,
        "module": "m3-income-statement",
        "topic": "Understanding Income Statements",
        "los": "LOS 22.f: Calculate and interpret basic and diluted earnings per share.",
        "question": "A firm has basic EPS of 1.50 USD based on 1,000,000 common shares and net income of 1,500,000 USD. It has 2,000,000 USD of 10% convertible debt (convertible into 100,000 common shares). The tax rate is 20%. If converted, the per-share effect of the convertible debt is 1.60 USD. What is the diluted EPS reported by the company?",
        "options": {
            "A": "1.50 USD",
            "B": "1.51 USD",
            "C": "1.60 USD"
        },
        "answer": "A",
        "explanation": "To determine whether a security is included in diluted EPS, we evaluate its per-share effect:\n- Interest saved net of tax = $2,000,000 \\times 10\\% \\times (1 - 0.20) = 160,000\\text{ USD}$.\n- Incremental shares = 100,000.\n- Per-share effect = $160,000\\text{ USD} / 100,000\\text{ shares} = 1.60\\text{ USD}$.\nBecause the per-share effect ($1.60\\text{ USD}$) exceeds Basic EPS ($1.50\\text{ USD}$), the convertible debt is antidilutive. Including it would increase EPS to $(1,500,000 + 160,000) / (1,000,000 + 100,000) = 1,660,000 / 1,100,000 = 1.509\\text{ USD} \\approx 1.51\\text{ USD}$. Accounting standards require antidilutive securities to be excluded from diluted EPS calculations. Therefore, Diluted EPS equals Basic EPS = 1.50 USD.\n\nDistractor Analysis:\n- B includes the antidilutive security, violating GAAP/IFRS rules.\n- C is the incremental per-share effect of the convertible debt."
    },
    {
        "id": "L1-Q044",
        "level": 1,
        "module": "m3-income-statement",
        "topic": "Understanding Income Statements",
        "los": "LOS 22.g: Describe other comprehensive income and its components.",
        "question": "Which of the following items is recognized in Other Comprehensive Income (OCI) rather than Net Income under both IFRS and US GAAP?",
        "options": {
            "A": "Unrealized holding gains and losses on trading (FVPL) equity securities.",
            "B": "Unrealized gains and losses from translating the financial statements of a foreign subsidiary into the parent's reporting currency.",
            "C": "Losses incurred from the early retirement of long-term debt obligations."
        },
        "answer": "B",
        "explanation": "Other Comprehensive Income includes revenues, expenses, gains, and losses that bypass the income statement and are accumulated directly in equity. The standard components (often remembered by the acronym PUFI) are:\n1. Pension and post-retirement plan adjustments (remeasurements);\n2. Unrealized gains/losses on available-for-sale (FVOCI) debt securities;\n3. Foreign currency translation adjustments from foreign subsidiaries;\n4. Effective portion of cash flow hedges.\n\nDistractor Analysis:\n- A (FVPL securities) must have unrealized gains and losses recognized directly in Net Income.\n- C (Gain/loss on early debt extinguishment) is recognized in Net Income as part of continuing operations."
    },
    {
        "id": "L1-Q045",
        "level": 1,
        "module": "m3-income-statement",
        "topic": "Understanding Income Statements",
        "los": "LOS 22.h: Describe common-size analysis of the income statement.",
        "question": "In vertical common-size analysis of the income statement, every line item is expressed as a percentage of:",
        "options": {
            "A": "Total assets.",
            "B": "Net revenue (sales).",
            "C": "Gross profit."
        },
        "answer": "B",
        "explanation": "A vertical common-size income statement divides each income statement item by net revenue (or total sales), expressing each line item as a percentage of revenue. This allows analysts to compare performance across time and across peer firms of differing sizes.\n\nDistractor Analysis:\n- A (Total assets) is the standard base for vertical common-size balance sheet analysis.\n- C is an intermediate income statement subtotal, not the standard common-size denominator."
    }
]
