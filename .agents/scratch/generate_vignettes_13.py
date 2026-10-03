# generate_vignettes_13.py
# Topic 13: Intercorporate Investments (Module m13-intercorporate)
# Vignettes V01 to V08 (48 questions)

def get_vignettes_topic13():
    vignettes = []

    # =========================================================================
    # V01: Financial Assets Classification and Measurement (IFRS 9 vs US GAAP)
    # =========================================================================
    v01_text = (
        "Apex Global Investments is an asset management firm based in London that prepares financial statements "
        "in accordance with IFRS 9 Financial Instruments. Senior analyst Marcus Vance is reviewing the accounting "
        "classification, measurement, and reporting for three debt instruments and two equity investments acquired on "
        "1 January 2024:\n\n"
        "1. Bond Alpha: A 5-year, 6.0% annual coupon bond with a face value of 10,000,000 EUR purchased at a discount "
        "for 9,584,170 EUR to yield an effective interest rate of 7.0%. The objective of Apex's business model is solely "
        "to hold the bond to collect contractual cash flows. Contractual cash flows consist solely of payments of principal "
        "and interest (the SPPI test is satisfied).\n"
        "2. Bond Beta: A 4-year, 5.0% annual coupon bond with a face value of 5,000,000 EUR purchased at par (5,000,000 EUR) "
        "with an effective interest rate of 5.0%. Apex's business model objective is achieved by both collecting contractual "
        "cash flows and selling financial assets (SPPI test is satisfied). At 31 December 2024, the market fair value of "
        "Bond Beta is 5,150,000 EUR (ex-coupon).\n"
        "3. Bond Gamma: A 3-year floating-rate note with a face value of 8,000,000 EUR purchased for 8,000,000 EUR. It is held "
        "within a trading portfolio managed to realize short-term gains. At 31 December 2024, its fair value is 7,850,000 EUR.\n"
        "4. Equity Delta: 100,000 ordinary shares of Delta SA purchased for 2,000,000 EUR. The investment is not held for "
        "trading. At initial recognition, Apex made an irrevocable election under IFRS 9 to present subsequent changes in fair "
        "value in other comprehensive income (OCI). During 2024, Apex received 60,000 EUR in cash dividends. At 31 December 2024, "
        "the fair value of Equity Delta is 2,250,000 EUR. On 15 January 2025, Apex sold all 100,000 shares for 2,280,000 EUR.\n"
        "5. Equity Epsilon: 50,000 ordinary shares of Epsilon Corp purchased for 1,500,000 EUR, held actively for short-term "
        "appreciation. During 2024, Epsilon paid 40,000 EUR in dividends, and on 31 December 2024, its fair value is 1,420,000 EUR.\n\n"
        "Vance also reviews Apex's commercial loan portfolio under the IFRS 9 three-stage expected credit loss (ECL) model."
    )

    v01_questions = [
        {
            "id": "L2-V01-Q1",
            "level": 2,
            "module": "m13-intercorporate",
            "topic": "Intercorporate Investments",
            "vignette_id": "V01",
            "vignette_title": "Apex Global Investments: Classification and Measurement of Financial Assets",
            "vignette_text": v01_text,
            "los": "LOS 13.a: describe the classification, measurement, and disclosure of investments in financial assets",
            "question": "Under IFRS 9, how should Bond Alpha and Bond Beta be classified at initial recognition?",
            "options": {
                "A": "Bond Alpha at Amortized Cost; Bond Beta at Fair Value through Other Comprehensive Income (FVOCI)",
                "B": "Bond Alpha at Amortized Cost; Bond Beta at Fair Value through Profit or Loss (FVPL)",
                "C": "Both Bond Alpha and Bond Beta at Amortized Cost"
            },
            "answer": "A",
            "explanation": (
                "Under IFRS 9, debt securities are classified based on two tests:\n"
                "1. **Contractual Cash Flow Characteristics (SPPI Test)**: Contractual cash flows must consist solely of payments of principal and interest.\n"
                "2. **Business Model Test**:\n"
                "- If the objective is solely to collect contractual cash flows, the asset is classified at **Amortized Cost**.\n"
                "- If the objective is achieved by **both** collecting contractual cash flows and selling financial assets, the asset is classified at **Fair Value through Other Comprehensive Income (FVOCI)**.\n\n"
                "Bond Alpha meets the SPPI test and is held solely to collect contractual cash flows $\\rightarrow$ Amortized Cost.\n"
                "Bond Beta meets the SPPI test and is held to both collect cash flows and sell $\\rightarrow$ FVOCI."
            )
        },
        {
            "id": "L2-V01-Q2",
            "level": 2,
            "module": "m13-intercorporate",
            "topic": "Intercorporate Investments",
            "vignette_id": "V01",
            "vignette_title": "Apex Global Investments: Classification and Measurement of Financial Assets",
            "vignette_text": v01_text,
            "los": "LOS 13.a: describe the classification, measurement, and disclosure of investments in financial assets",
            "question": "On Apex's financial statements for the year ended 31 December 2024, the interest revenue recognized in profit or loss and the balance sheet carrying value for Bond Alpha are closest to:",
            "options": {
                "A": "Interest revenue: 600,000 EUR; Carrying value: 9,584,170 EUR",
                "B": "Interest revenue: 670,892 EUR; Carrying value: 9,655,062 EUR",
                "C": "Interest revenue: 670,892 EUR; Carrying value: 10,000,000 EUR"
            },
            "answer": "B",
            "explanation": (
                "Bond Alpha is measured at amortized cost using the effective interest method:\n"
                "$$\\text{Interest Revenue} = \\text{Beginning Carrying Value} \\times \\text{Effective Interest Rate}$$\n"
                "$$\\text{Interest Revenue} = 9,584,170 \\text{ EUR} \\times 7.0\\% = 670,892 \\text{ EUR}$$\n\n"
                "The contractual coupon cash received is:\n"
                "$$\\text{Coupon Payment} = 10,000,000 \\text{ EUR} \\times 6.0\\% = 600,000 \\text{ EUR}$$\n\n"
                "The discount amortization added to the carrying value is:\n"
                "$$\\text{Discount Amortization} = 670,892 - 600,000 = 70,892 \\text{ EUR}$$\n\n"
                "$$\\text{Ending Carrying Value} = 9,584,170 + 70,892 = 9,655,062 \\text{ EUR}$$"
            )
        },
        {
            "id": "L2-V01-Q3",
            "level": 2,
            "module": "m13-intercorporate",
            "topic": "Intercorporate Investments",
            "vignette_id": "V01",
            "vignette_title": "Apex Global Investments: Classification and Measurement of Financial Assets",
            "vignette_text": v01_text,
            "los": "LOS 13.a: describe the classification, measurement, and disclosure of investments in financial assets",
            "question": "For the year ended 31 December 2024, the impacts of Bond Beta on Apex's profit or loss (P&L) and other comprehensive income (OCI) are:",
            "options": {
                "A": "P&L: 250,000 EUR; OCI: 150,000 EUR",
                "B": "P&L: 400,000 EUR; OCI: 0 EUR",
                "C": "P&L: 150,000 EUR; OCI: 250,000 EUR"
            },
            "answer": "A",
            "explanation": (
                "Bond Beta is classified as FVOCI (debt instrument):\n"
                "1. **Profit or Loss (P&L)**: Interest income is recognized using the effective interest method, exactly as if measured at amortized cost:\n"
                "$$\\text{Interest Income} = 5,000,000 \\text{ EUR} \\times 5.0\\% = 250,000 \\text{ EUR}$$\n"
                "2. **Balance Sheet**: Carried at fair value = 5,150,000 EUR.\n"
                "3. **Other Comprehensive Income (OCI)**: Unrealized gain equals the difference between fair value and amortized cost:\n"
                "$$\\text{Amortized Cost at 31 Dec 2024} = 5,000,000 \\text{ EUR}$$\n"
                "$$\\text{Unrealized Gain in OCI} = 5,150,000 - 5,000,000 = 150,000 \\text{ EUR}$$\n\n"
                "Therefore, P&L receives 250,000 EUR and OCI receives 150,000 EUR."
            )
        },
        {
            "id": "L2-V01-Q4",
            "level": 2,
            "module": "m13-intercorporate",
            "topic": "Intercorporate Investments",
            "vignette_id": "V01",
            "vignette_title": "Apex Global Investments: Classification and Measurement of Financial Assets",
            "vignette_text": v01_text,
            "los": "LOS 13.a: describe the classification, measurement, and disclosure of investments in financial assets",
            "question": "Regarding the disposal of Equity Delta on 15 January 2025, which of the following statements correctly describes the accounting under IFRS 9?",
            "options": {
                "A": "A realized gain of 280,000 EUR is reclassified (recycled) from OCI into profit or loss",
                "B": "A realized gain of 30,000 EUR is recognized in profit or loss, while previous OCI gains remain in equity",
                "C": "No gain or loss is recognized in profit or loss; the cumulative gain of 280,000 EUR remains in equity and may be transferred directly to retained earnings"
            },
            "answer": "C",
            "explanation": (
                "Under IFRS 9, for equity instruments designated at initial recognition as FVOCI (irrevocable election):\n"
                "- Dividend income is recognized in profit or loss (unless clearly representing a recovery of cost).\n"
                "- All fair value changes are recognized in OCI.\n"
                "- **Crucial rule**: Cumulative gains and losses accumulated in OCI are **NEVER** reclassified (recycled) to profit or loss upon disposal.\n"
                "- Upon derecognition, the cumulative gain of:\n"
                "$$\\text{Cumulative Gain} = 2,280,000 - 2,000,000 = 280,000 \\text{ EUR}$$\n"
                "may be transferred directly within equity (e.g., from OCI to retained earnings).\n\n"
                "*(Note: Under US GAAP, an FVOCI election for equity securities is not permitted; all equity securities without significant influence must be measured at FVPL).*")
        },
        {
            "id": "L2-V01-Q5",
            "level": 2,
            "module": "m13-intercorporate",
            "topic": "Intercorporate Investments",
            "vignette_id": "V01",
            "vignette_title": "Apex Global Investments: Classification and Measurement of Financial Assets",
            "vignette_text": v01_text,
            "los": "LOS 13.a: describe the classification, measurement, and disclosure of investments in financial assets",
            "question": "Under the IFRS 9 expected credit loss (ECL) impairment model, when a financial asset experiences a significant increase in credit risk (SICR) since initial recognition but is not credit-impaired, it transitions to:",
            "options": {
                "A": "Stage 1, with loss allowance equal to 12-month expected credit losses and interest revenue calculated on the gross carrying amount",
                "B": "Stage 2, with loss allowance equal to lifetime expected credit losses and interest revenue calculated on the gross carrying amount",
                "C": "Stage 3, with loss allowance equal to lifetime expected credit losses and interest revenue calculated on the net carrying amount"
            },
            "answer": "B",
            "explanation": (
                "Under IFRS 9's three-stage ECL model:\n"
                "- **Stage 1 (Performing)**: No significant increase in credit risk since initial recognition. Loss allowance is based on **12-month ECL**. Interest revenue is calculated on **gross carrying amount**.\n"
                "- **Stage 2 (Underperforming)**: Significant increase in credit risk (SICR) has occurred, but the asset is not credit-impaired. Loss allowance is based on **lifetime ECL**. Interest revenue continues to be calculated on the **gross carrying amount**.\n"
                "- **Stage 3 (Credit-impaired)**: Objective evidence of impairment exists (default). Loss allowance is based on **lifetime ECL**. Interest revenue is calculated on the **net carrying amount** (gross carrying amount less loss allowance)."
            )
        },
        {
            "id": "L2-V01-Q6",
            "level": 2,
            "module": "m13-intercorporate",
            "topic": "Intercorporate Investments",
            "vignette_id": "V01",
            "vignette_title": "Apex Global Investments: Classification and Measurement of Financial Assets",
            "vignette_text": v01_text,
            "los": "LOS 13.a: describe the classification, measurement, and disclosure of investments in financial assets",
            "question": "Regarding the reclassification of financial assets under IFRS 9, Vance should conclude that:",
            "options": {
                "A": "Debt instruments must be reclassified if and only if the entity changes its business model for managing them; equity instruments can never be reclassified",
                "B": "Both debt and equity instruments may be freely reclassified whenever management's intent changes",
                "C": "Debt instruments can never be reclassified; equity instruments may be reclassified upon board approval"
            },
            "answer": "A",
            "explanation": (
                "Under IFRS 9:\n"
                "1. **Debt securities**: Reclassification is required **if and only if** the entity changes its business model for managing financial assets. Such changes are expected to be very infrequent, determined by senior management as a result of external or internal changes significant to operations.\n"
                "2. **Equity securities**: Reclassification is **strictly prohibited**. The initial classification (FVPL or irrevocable FVOCI election) cannot be reversed or altered under any circumstances."
            )
        }
    ]
    vignettes.extend(v01_questions)

    # =========================================================================
    # V02: Equity Method and Fair Value Excess Amortization
    # =========================================================================
    v02_text = (
        "On 1 January 2024, Meridian Holdings acquired a 30% voting equity interest in Beacon Technologies for "
        "180 million USD in cash. The acquisition gives Meridian significant influence, and Meridian accounts for the "
        "investment using the equity method. At the acquisition date, Beacon's carrying value of net assets was 400 million USD.\n\n"
        "An independent appraisal on 1 January 2024 revealed the following fair value discrepancies for Beacon's identifiable assets:\n"
        "- Inventory: Book value was 50 million USD; fair value was 60 million USD. All inventory on hand at acquisition was "
        "sold to third parties during 2024.\n"
        "- Equipment: Book value was 120 million USD; fair value was 150 million USD. The equipment has a remaining useful "
        "life of 10 years with zero salvage value (straight-line depreciation).\n"
        "- Patent: Beacon had developed an internal patent with zero book value, but its fair value was appraised at 40 million USD "
        "with a remaining legal and useful life of 5 years (straight-line amortization).\n"
        "- All other identifiable assets and liabilities had book values equal to fair values.\n\n"
        "For the fiscal year ended 31 December 2024, Beacon reported net income of 70 million USD and declared and paid cash "
        "dividends of 20 million USD. Meridian prepares financial statements under US GAAP."
    )

    v02_questions = [
        {
            "id": "L2-V02-Q1",
            "level": 2,
            "module": "m13-intercorporate",
            "topic": "Intercorporate Investments",
            "vignette_id": "V02",
            "vignette_title": "Meridian Holdings: Equity Method and Fair Value Excess Amortization",
            "vignette_text": v02_text,
            "los": "LOS 13.b: distinguish between methods of accounting for intercorporate investments and calculate investment income and carrying values under the equity method",
            "question": "The amount of implied goodwill included in the purchase price of Meridian's investment in Beacon on 1 January 2024 is closest to:",
            "options": {
                "A": "36.0 million USD",
                "B": "48.0 million USD",
                "C": "60.0 million USD"
            },
            "answer": "A",
            "explanation": (
                "Step 1: Compute Beacon's total fair value of net identifiable assets on 1 January 2024:\n"
                "$$\\text{Book Value of Net Assets} = 400.0 \\text{ million USD}$$\n"
                "$$\\text{Inventory Excess} = 60.0 - 50.0 = 10.0 \\text{ million USD}$$\n"
                "$$\\text{Equipment Excess} = 150.0 - 120.0 = 30.0 \\text{ million USD}$$\n"
                "$$\\text{Unrecorded Patent} = 40.0 \\text{ million USD}$$\n"
                "$$\\text{Fair Value of Net Identifiable Assets} = 400.0 + 10.0 + 30.0 + 40.0 = 480.0 \\text{ million USD}$$\n\n"
                "Step 2: Calculate Meridian's proportionate share of fair value of net identifiable assets:\n"
                "$$\\text{Share of Net Identifiable Assets} = 30\\% \\times 480.0 = 144.0 \\text{ million USD}$$\n\n"
                "Step 3: Implied Goodwill embedded in the purchase price:\n"
                "$$\\text{Goodwill} = \\text{Purchase Price} - \\text{Share of Fair Value of Net Identifiable Assets}$$\n"
                "$$\\text{Goodwill} = 180.0 - 144.0 = 36.0 \\text{ million USD}$$"
            )
        },
        {
            "id": "L2-V02-Q2",
            "level": 2,
            "module": "m13-intercorporate",
            "topic": "Intercorporate Investments",
            "vignette_id": "V02",
            "vignette_title": "Meridian Holdings: Equity Method and Fair Value Excess Amortization",
            "vignette_text": v02_text,
            "los": "LOS 13.b: distinguish between methods of accounting for intercorporate investments and calculate investment income and carrying values under the equity method",
            "question": "The total fair value excess amortization/depreciation adjustment reducing Meridian's share of Beacon's net income for 2024 is closest to:",
            "options": {
                "A": "3.3 million USD",
                "B": "6.3 million USD",
                "C": "11.0 million USD"
            },
            "answer": "B",
            "explanation": (
                "The annual fair value excess amortization attributable to Meridian's 30% interest consists of:\n"
                "1. **Inventory**: All inventory sold in 2024 $\\rightarrow$ full excess expensed:\n"
                "$$\\text{Inventory Amortization} = 30\\% \\times 10.0 \\text{ million USD} = 3.00 \\text{ million USD}$$\n"
                "2. **Equipment**: Excess depreciated over 10 years:\n"
                "$$\\text{Equipment Depreciation} = 30\\% \\times \\left(\\frac{30.0 \\text{ million USD}}{10}\\right) = 30\\% \\times 3.00 = 0.90 \\text{ million USD}$$\n"
                "3. **Patent**: Amortized over 5 years:\n"
                "$$\\text{Patent Amortization} = 30\\% \\times \\left(\\frac{40.0 \\text{ million USD}}{5}\\right) = 30\\% \\times 8.00 = 2.40 \\text{ million USD}$$\n\n"
                "$$\\text{Total Amortization Adjustment} = 3.00 + 0.90 + 2.40 = 6.30 \\text{ million USD}$$"
            )
        },
        {
            "id": "L2-V02-Q3",
            "level": 2,
            "module": "m13-intercorporate",
            "topic": "Intercorporate Investments",
            "vignette_id": "V02",
            "vignette_title": "Meridian Holdings: Equity Method and Fair Value Excess Amortization",
            "vignette_text": v02_text,
            "los": "LOS 13.b: distinguish between methods of accounting for intercorporate investments and calculate investment income and carrying values under the equity method",
            "question": "For the year ended 31 December 2024, Meridian should report equity investment income in its income statement closest to:",
            "options": {
                "A": "14.7 million USD",
                "B": "15.0 million USD",
                "C": "21.0 million USD"
            },
            "answer": "A",
            "explanation": (
                "Investment income under the equity method equals the investor's share of reported net income less fair value excess amortization:\n"
                "$$\\text{Share of Reported Net Income} = 30\\% \\times 70.0 \\text{ million USD} = 21.00 \\text{ million USD}$$\n"
                "$$\\text{Fair Value Excess Amortization} = 6.30 \\text{ million USD}$$\n"
                "$$\\text{Equity Income} = 21.00 - 6.30 = 14.70 \\text{ million USD}$$"
            )
        },
        {
            "id": "L2-V02-Q4",
            "level": 2,
            "module": "m13-intercorporate",
            "topic": "Intercorporate Investments",
            "vignette_id": "V02",
            "vignette_title": "Meridian Holdings: Equity Method and Fair Value Excess Amortization",
            "vignette_text": v02_text,
            "los": "LOS 13.b: distinguish between methods of accounting for intercorporate investments and calculate investment income and carrying values under the equity method",
            "question": "On Meridian's balance sheet at 31 December 2024, the carrying value of the investment in Beacon Technologies is closest to:",
            "options": {
                "A": "182.7 million USD",
                "B": "188.7 million USD",
                "C": "195.0 million USD"
            },
            "answer": "B",
            "explanation": (
                "The ending carrying value of an equity method investment is calculated as:\n"
                "$$\\text{Ending Carrying Value} = \\text{Beginning Carrying Value} + \\text{Equity Income} - \\text{Dividends Received}$$\n\n"
                "$$\\text{Beginning Carrying Value} = 180.00 \\text{ million USD}$$\n"
                "$$\\text{Equity Income} = 14.70 \\text{ million USD}$$\n"
                "$$\\text{Dividends Received} = 30\\% \\times 20.0 \\text{ million USD} = 6.00 \\text{ million USD}$$\n\n"
                "$$\\text{Ending Carrying Value} = 180.00 + 14.70 - 6.00 = 188.70 \\text{ million USD}$$\n\n"
                "Note: Dividends received reduce the investment carrying amount on the balance sheet and are recorded as cash inflows; they are not recognized in profit or loss."
            )
        },
        {
            "id": "L2-V02-Q5",
            "level": 2,
            "module": "m13-intercorporate",
            "topic": "Intercorporate Investments",
            "vignette_id": "V02",
            "vignette_title": "Meridian Holdings: Equity Method and Fair Value Excess Amortization",
            "vignette_text": v02_text,
            "los": "LOS 13.b: distinguish between methods of accounting for intercorporate investments and calculate investment income and carrying values under the equity method",
            "question": "In the statement of cash flows of Meridian for 2024, the 6.0 million USD cash dividend received from Beacon is classified as:",
            "options": {
                "A": "Operating cash flow under US GAAP; operating or investing cash flow under IFRS",
                "B": "Investing cash flow under US GAAP; operating cash flow under IFRS",
                "C": "Financing cash flow under both US GAAP and IFRS"
            },
            "answer": "A",
            "explanation": (
                "Under US GAAP, dividends received are classified as **operating cash flows** (CFO).\n"
                "Under IFRS, dividends received can be classified as either **operating cash flows** (CFO) or **investing cash flows** (CFI), provided the classification is applied consistently from period to period."
            )
        },
        {
            "id": "L2-V02-Q6",
            "level": 2,
            "module": "m13-intercorporate",
            "topic": "Intercorporate Investments",
            "vignette_id": "V02",
            "vignette_title": "Meridian Holdings: Equity Method and Fair Value Excess Amortization",
            "vignette_text": v02_text,
            "los": "LOS 13.b: distinguish between methods of accounting for intercorporate investments and calculate investment income and carrying values under the equity method",
            "question": "If Beacon were to incur massive net losses in subsequent years such that Meridian's cumulative share of losses exceeds the investment carrying value, Meridian should:",
            "options": {
                "A": "Discontinue applying the equity method once the carrying amount reaches zero, unless Meridian has legal or constructive obligations to fund Beacon's deficits",
                "B": "Continue recognizing its share of losses, reporting a negative investment liability on the balance sheet regardless of obligations",
                "C": "Immediately write off the investment and recognize an impairment loss directly in other comprehensive income"
            },
            "answer": "A",
            "explanation": (
                "Under both US GAAP (ASC 323) and IFRS (IAS 28):\n"
                "- When the investor's share of losses equals or exceeds its interest in the associate (carrying value plus other long-term interests such as preferred stock or unsecured advances), the investor discontinues recognizing further losses.\n"
                "- The investment balance is reduced to zero.\n"
                "- Additional losses are recognized as a liability **only** to the extent that the investor has incurred legal or constructive obligations or made payments on behalf of the associate.\n"
                "- If the associate subsequently reports net income, the investor resumes recognizing its share of profits only after its share of profits equals the share of unrecognized net losses."
            )
        }
    ]
    vignettes.extend(v02_questions)

    # =========================================================================
    # V03: Equity Method - Intercompany Transactions and Impairment
    # =========================================================================
    v03_text = (
        "Crestview Corporation owns a 25% voting equity interest in Apex Supplies Inc. and accounts for the investment "
        "using the equity method. Crestview prepares financial statements under IFRS. During the fiscal year ended 31 December 2024, "
        "two intercompany inventory transactions occurred between Crestview and Apex:\n\n"
        "1. Downstream Transaction: Crestview sold inventory costing 12.0 million USD to Apex for 16.0 million USD "
        "(realizing a profit of 4.0 million USD). By 31 December 2024, Apex had resold 60% of these goods to unrelated third "
        "parties for 11.5 million USD, retaining 40% in its ending inventory.\n"
        "2. Upstream Transaction: Apex sold inventory costing 6.0 million USD to Crestview for 10.0 million USD "
        "(realizing a profit of 4.0 million USD). By 31 December 2024, Crestview had resold 75% of these goods to unrelated "
        "third parties for 9.0 million USD, retaining 25% in its ending inventory.\n\n"
        "For 2024, Apex reported net income of 32.0 million USD and declared and paid cash dividends of 8.0 million USD. "
        "There were no fair value step-up amortization differences.\n\n"
        "In late 2025, severe industry disruption affects Apex. At 31 December 2025, Crestview's carrying value of the "
        "investment in Apex is 54.0 million USD. Crestview conducts an impairment test under IAS 28 / IAS 36. An independent "
        "valuation indicates Apex's fair value less costs of disposal is 42.0 million USD, and its value in use is 45.0 million USD."
    )

    v03_questions = [
        {
            "id": "L2-V03-Q1",
            "level": 2,
            "module": "m13-intercorporate",
            "topic": "Intercorporate Investments",
            "vignette_id": "V03",
            "vignette_title": "Crestview Corporation: Intercompany Transactions and Impairment of Associates",
            "vignette_text": v03_text,
            "los": "LOS 13.b: distinguish between methods of accounting for intercorporate investments and calculate investment income and carrying values under the equity method",
            "question": "The unrealized profit from the downstream inventory transaction to be eliminated by Crestview in 2024 is closest to:",
            "options": {
                "A": "0.40 million USD",
                "B": "1.00 million USD",
                "C": "1.60 million USD"
            },
            "answer": "A",
            "explanation": (
                "In a downstream transaction, the investor sells to the associate:\n"
                "$$\\text{Total Profit Recorded by Crestview} = 16.0 - 12.0 = 4.0 \\text{ million USD}$$\n"
                "$$\\text{Portion Remaining in Ending Inventory} = 40\\%$$\n"
                "$$\\text{Total Unrealized Intercompany Profit} = 4.0 \\times 40\\% = 1.60 \\text{ million USD}$$\n\n"
                "Under the equity method (both IFRS and US GAAP), the investor eliminates unrealized profit to the extent of its ownership interest:\n"
                "$$\\text{Unrealized Profit Eliminated} = 25\\% \\times 1.60 \\text{ million USD} = 0.40 \\text{ million USD}$$"
            )
        },
        {
            "id": "L2-V03-Q2",
            "level": 2,
            "module": "m13-intercorporate",
            "topic": "Intercorporate Investments",
            "vignette_id": "V03",
            "vignette_title": "Crestview Corporation: Intercompany Transactions and Impairment of Associates",
            "vignette_text": v03_text,
            "los": "LOS 13.b: distinguish between methods of accounting for intercorporate investments and calculate investment income and carrying values under the equity method",
            "question": "The unrealized profit from the upstream inventory transaction to be eliminated from Crestview's equity income in 2024 is closest to:",
            "options": {
                "A": "0.25 million USD",
                "B": "0.50 million USD",
                "C": "1.00 million USD"
            },
            "answer": "A",
            "explanation": (
                "In an upstream transaction, the associate sells to the investor:\n"
                "$$\\text{Total Profit Recorded by Apex} = 10.0 - 6.0 = 4.0 \\text{ million USD}$$\n"
                "$$\\text{Portion Remaining in Crestview's Ending Inventory} = 25\\%$$\n"
                "$$\\text{Total Unrealized Profit} = 4.0 \\times 25\\% = 1.00 \\text{ million USD}$$\n\n"
                "Crestview eliminates its proportionate share of the unrealized upstream profit:\n"
                "$$\\text{Unrealized Profit Eliminated} = 25\\% \\times 1.00 \\text{ million USD} = 0.25 \\text{ million USD}$$"
            )
        },
        {
            "id": "L2-V03-Q3",
            "level": 2,
            "module": "m13-intercorporate",
            "topic": "Intercorporate Investments",
            "vignette_id": "V03",
            "vignette_title": "Crestview Corporation: Intercompany Transactions and Impairment of Associates",
            "vignette_text": v03_text,
            "los": "LOS 13.b: distinguish between methods of accounting for intercorporate investments and calculate investment income and carrying values under the equity method",
            "question": "Crestview's recognized equity income from Apex Supplies for the year ended 31 December 2024 is closest to:",
            "options": {
                "A": "7.35 million USD",
                "B": "7.60 million USD",
                "C": "8.00 million USD"
            },
            "answer": "A",
            "explanation": (
                "Crestview's equity income is calculated as:\n"
                "$$\\text{Proportionate Share of Apex Reported Net Income} = 25\\% \\times 32.0 \\text{ million USD} = 8.00 \\text{ million USD}$$\n"
                "$$\\text{Less: Downstream Unrealized Profit} = -0.40 \\text{ million USD}$$\n"
                "$$\\text{Less: Upstream Unrealized Profit} = -0.25 \\text{ million USD}$$\n\n"
                "$$\\text{Recognized Equity Income} = 8.00 - 0.40 - 0.25 = 7.35 \\text{ million USD}$$"
            )
        },
        {
            "id": "L2-V03-Q4",
            "level": 2,
            "module": "m13-intercorporate",
            "topic": "Intercorporate Investments",
            "vignette_id": "V03",
            "vignette_title": "Crestview Corporation: Intercompany Transactions and Impairment of Associates",
            "vignette_text": v03_text,
            "los": "LOS 13.b: distinguish between methods of accounting for intercorporate investments and calculate investment income and carrying values under the equity method",
            "question": "In 2025, if all remaining inventory from both the downstream and upstream 2024 transactions is sold to third parties, Crestview's 2025 equity income will be adjusted by:",
            "options": {
                "A": "Adding back 0.65 million USD of previously deferred profits",
                "B": "Deducting 0.65 million USD as confirmed realized cost",
                "C": "No adjustment, because prior period intercompany profits are retained in equity reserves"
            },
            "answer": "A",
            "explanation": (
                "When the previously unsold inventory is sold to third parties in a subsequent period, the unrealized intercompany profit is realized.\n"
                "In 2025:\n"
                "$$\\text{Downstream Profit Realized} = +0.40 \\text{ million USD}$$\n"
                "$$\\text{Upstream Profit Realized} = +0.25 \\text{ million USD}$$\n"
                "$$\\text{Total Profit Added to 2025 Equity Income} = 0.40 + 0.25 = 0.65 \\text{ million USD}$$"
            )
        },
        {
            "id": "L2-V03-Q5",
            "level": 2,
            "module": "m13-intercorporate",
            "topic": "Intercorporate Investments",
            "vignette_id": "V03",
            "vignette_title": "Crestview Corporation: Intercompany Transactions and Impairment of Associates",
            "vignette_text": v03_text,
            "los": "LOS 13.c: compare the financial statement effects of the equity method, proportionate consolidation, and acquisition method",
            "question": "Under IFRS (IAS 28 / IAS 36), the impairment loss Crestview should recognize on its investment in Apex at 31 December 2025 is closest to:",
            "options": {
                "A": "9.0 million USD",
                "B": "12.0 million USD",
                "C": "15.0 million USD"
            },
            "answer": "A",
            "explanation": (
                "Under IFRS (IAS 28 and IAS 36):\n"
                "1. The entire carrying amount of the investment (including goodwill) is tested for impairment as a single asset.\n"
                "2. **Recoverable Amount** is the higher of:\n"
                "- Fair value less costs of disposal = 42.0 million USD\n"
                "- Value in use = 45.0 million USD\n"
                "$$\\text{Recoverable Amount} = \\max(42.0, 45.0) = 45.0 \\text{ million USD}$$\n\n"
                "3. Impairment Loss:\n"
                "$$\\text{Impairment Loss} = \\text{Carrying Value} - \\text{Recoverable Amount} = 54.0 - 45.0 = 9.0 \\text{ million USD}$$\n\n"
                "*(Note: Under US GAAP, an impairment is recognized if the decline in fair value is other-than-temporary, written down to fair value of 42.0 million USD, yielding an impairment loss of 12.0 million USD).*"
            )
        },
        {
            "id": "L2-V03-Q6",
            "level": 2,
            "module": "m13-intercorporate",
            "topic": "Intercorporate Investments",
            "vignette_id": "V03",
            "vignette_title": "Crestview Corporation: Intercompany Transactions and Impairment of Associates",
            "vignette_text": v03_text,
            "los": "LOS 13.c: compare the financial statement effects of the equity method, proportionate consolidation, and acquisition method",
            "question": "Regarding the subsequent reversal of impairment losses on equity method investments, which statement is most accurate?",
            "options": {
                "A": "Under IFRS, impairment reversals are permitted up to the recoverable amount if conditions improve; under US GAAP, impairment reversals are prohibited",
                "B": "Under both IFRS and US GAAP, impairment reversals on equity method investments are strictly prohibited",
                "C": "Under US GAAP, impairment reversals are permitted; under IFRS, they are prohibited because goodwill is embedded"
            },
            "answer": "A",
            "explanation": (
                "Under IFRS (IAS 28.42 and IAS 36):\n"
                "- The investment is tested as a single asset, not by allocating impairment separately to embedded goodwill.\n"
                "- Therefore, an impairment loss recognized in prior periods **can be reversed** up to the new recoverable amount if there has been a change in estimates used to determine the recoverable amount.\n\n"
                "Under US GAAP (ASC 323):\n"
                "- An other-than-temporary impairment establishes a new cost basis.\n"
                "- Subsequent reversals of impairment losses are **strictly prohibited**."
            )
        }
    ]
    vignettes.extend(v03_questions)

    # =========================================================================
    # V04: Business Combinations - Acquisition Method & Net Identifiable Assets
    # =========================================================================
    v04_text = (
        "On 1 July 2024, Solaris Energy acquired 100% of Terra Dynamics Inc. in a business combination. Both entities prepare "
        "financial statements under IFRS. The purchase consideration transferred consisted of:\n"
        "- 250 million USD cash paid at closing.\n"
        "- 5.0 million newly issued ordinary shares of Solaris (par value 1 USD). On the acquisition date, Solaris shares "
        "closed at a fair value of 30 USD per share.\n"
        "- Contingent consideration: Solaris agreed to pay an additional cash earn-out of up to 50 million USD in 2026 if Terra "
        "achieves defined cumulative EBITDA hurdles. The acquisition-date fair value of this contingent consideration was "
        "estimated at 35 million USD.\n\n"
        "Solaris incurred 6.0 million USD in legal, investment banking, and accounting advisory fees, and 2.0 million USD in "
        "share issuance registration fees.\n\n"
        "At the acquisition date, Terra's carrying value of net assets was 280 million USD. A comprehensive fair value appraisal revealed:\n"
        "- Property, Plant, and Equipment (PP&E) had a fair value step-up of 40 million USD above book value (useful life of 10 years).\n"
        "- In-process research and development (IPR&D) projects had an appraised fair value of 50 million USD (previously expensed by Terra).\n"
        "- Customer relationships intangible assets were appraised at 30 million USD (useful life of 6 years).\n"
        "- A contingent liability from an environmental lawsuit was appraised at a fair value of 15 million USD (not recognized on Terra's books).\n"
        "- All other assets and liabilities had book values equal to fair values.\n\n"
        "On 31 December 2024, due to exceptional commercial performance by Terra, the fair value of the contingent consideration liability "
        "was remeasured at 42 million USD."
    )

    v04_questions = [
        {
            "id": "L2-V04-Q1",
            "level": 2,
            "module": "m13-intercorporate",
            "topic": "Intercorporate Investments",
            "vignette_id": "V04",
            "vignette_title": "Solaris Energy: Business Combinations and the Acquisition Method",
            "vignette_text": v04_text,
            "los": "LOS 13.d: describe the acquisition method of accounting for a business combination and determine goodwill at the acquisition date",
            "question": "The total purchase consideration transferred by Solaris on the acquisition date is closest to:",
            "options": {
                "A": "400 million USD",
                "B": "435 million USD",
                "C": "443 million USD"
            },
            "answer": "B",
            "explanation": (
                "Under IFRS 3 and ASC 805 (the acquisition method), total consideration transferred includes:\n"
                "1. Cash paid: 250 million USD\n"
                "2. Fair value of equity shares issued: ${5.0}\\text{ million shares} \\times 30\\text{ USD} = 150\\text{ million USD}$\n"
                "3. Fair value of contingent consideration at acquisition date: 35 million USD\n\n"
                "$$\\text{Total Consideration} = 250 + 150 + 35 = 435 \\text{ million USD}$$\n\n"
                "Note on acquisition expenses:\n"
                "- Advisory/legal fees (6.0 million USD) are **expensed** as incurred in P&L.\n"
                "- Share issuance costs (2.0 million USD) reduce equity proceeds (debited to Additional Paid-in Capital)."
            )
        },
        {
            "id": "L2-V04-Q2",
            "level": 2,
            "module": "m13-intercorporate",
            "topic": "Intercorporate Investments",
            "vignette_id": "V04",
            "vignette_title": "Solaris Energy: Business Combinations and the Acquisition Method",
            "vignette_text": v04_text,
            "los": "LOS 13.d: describe the acquisition method of accounting for a business combination and determine goodwill at the acquisition date",
            "question": "The total fair value of net identifiable assets acquired by Solaris on 1 July 2024 is closest to:",
            "options": {
                "A": "370 million USD",
                "B": "385 million USD",
                "C": "400 million USD"
            },
            "answer": "B",
            "explanation": (
                "Fair value of net identifiable assets acquired:\n"
                "$$\\text{Carrying value of net assets} = 280 \\text{ million USD}$$\n"
                "$$\\text{PP\\&E step-up} = +40 \\text{ million USD}$$\n"
                "$$\\text{In-process R\\&D (IPR\\&D)} = +50 \\text{ million USD}$$\n"
                "$$\\text{Customer relationships} = +30 \\text{ million USD}$$\n"
                "$$\\text{Contingent liability (environmental lawsuit)} = -15 \\text{ million USD}$$\n\n"
                "$$\\text{Fair Value of Net Identifiable Assets} = 280 + 40 + 50 + 30 - 15 = 385 \\text{ million USD}$$\n\n"
                "Under IFRS 3, identifiable intangibles (including IPR&D) and present legal/constructive contingent liabilities whose fair value can be reliably measured are recognized at fair value."
            )
        },
        {
            "id": "L2-V04-Q3",
            "level": 2,
            "module": "m13-intercorporate",
            "topic": "Intercorporate Investments",
            "vignette_id": "V04",
            "vignette_title": "Solaris Energy: Business Combinations and the Acquisition Method",
            "vignette_text": v04_text,
            "los": "LOS 13.d: describe the acquisition method of accounting for a business combination and determine goodwill at the acquisition date",
            "question": "The goodwill recognized by Solaris on the acquisition date (1 July 2024) is closest to:",
            "options": {
                "A": "35 million USD",
                "B": "50 million USD",
                "C": "65 million USD"
            },
            "answer": "B",
            "explanation": (
                "Goodwill under the acquisition method:\n"
                "$$\\text{Goodwill} = \\text{Total Consideration Transferred} - \\text{Fair Value of Net Identifiable Assets}$$\n"
                "$$\\text{Goodwill} = 435 - 385 = 50 \\text{ million USD}$$"
            )
        },
        {
            "id": "L2-V04-Q4",
            "level": 2,
            "module": "m13-intercorporate",
            "topic": "Intercorporate Investments",
            "vignette_id": "V04",
            "vignette_title": "Solaris Energy: Business Combinations and the Acquisition Method",
            "vignette_text": v04_text,
            "los": "LOS 13.d: describe the acquisition method of accounting for a business combination and determine goodwill at the acquisition date",
            "question": "How should the 6.0 million USD advisory fees and 2.0 million USD share issuance costs be presented in Solaris's financial statements for the year ended 31 December 2024?",
            "options": {
                "A": "Both the 6.0 million USD and 2.0 million USD are capitalized as part of goodwill",
                "B": "The 6.0 million USD is expensed in profit or loss; the 2.0 million USD is recognized as a reduction of equity (share premium / APIC)",
                "C": "The 6.0 million USD is capitalized into PP&E; the 2.0 million USD is expensed in profit or loss"
            },
            "answer": "B",
            "explanation": (
                "Under both IFRS 3 and ASC 805:\n"
                "1. **Acquisition-related costs** (advisory, legal, accounting, appraisal, consulting): Must be **expensed in profit or loss** in the period incurred.\n"
                "2. **Direct costs of issuing equity securities**: Deducted from the proceeds of the equity issue, thereby **reducing equity (share premium / APIC)**.\n"
                "3. Costs of issuing debt securities: Deducted from the initial carrying amount of the debt liability and amortized through effective interest."
            )
        },
        {
            "id": "L2-V04-Q5",
            "level": 2,
            "module": "m13-intercorporate",
            "topic": "Intercorporate Investments",
            "vignette_id": "V04",
            "vignette_title": "Solaris Energy: Business Combinations and the Acquisition Method",
            "vignette_text": v04_text,
            "los": "LOS 13.d: describe the acquisition method of accounting for a business combination and determine goodwill at the acquisition date",
            "question": "The remeasurement of the contingent consideration liability at 31 December 2024 results in:",
            "options": {
                "A": "A 7.0 million USD increase in goodwill on the balance sheet",
                "B": "A 7.0 million USD loss recognized in profit or loss",
                "C": "A 7.0 million USD unrealized loss recognized in other comprehensive income"
            },
            "answer": "B",
            "explanation": (
                "Subsequent accounting for contingent consideration:\n"
                "- Because the contingent consideration is payable in cash, it is classified as a **liability**.\n"
                "- Liability-classified contingent consideration must be remeasured at fair value at each reporting date, with changes in fair value recognized directly in **profit or loss**:\n"
                "$$\\Delta \\text{Fair Value} = 42.0 - 35.0 = 7.0 \\text{ million USD loss/expense in P&L}$$\n"
                "- It does **not** adjust goodwill, because the change arose from post-acquisition performance (not a measurement period adjustment correcting facts existing at acquisition date)."
            )
        },
        {
            "id": "L2-V04-Q6",
            "level": 2,
            "module": "m13-intercorporate",
            "topic": "Intercorporate Investments",
            "vignette_id": "V04",
            "vignette_title": "Solaris Energy: Business Combinations and the Acquisition Method",
            "vignette_text": v04_text,
            "los": "LOS 13.d: describe the acquisition method of accounting for a business combination and determine goodwill at the acquisition date",
            "question": "If Solaris had instead negotiated a purchase price where total consideration transferred was 350 million USD, the resulting 35 million USD difference would be accounted for as:",
            "options": {
                "A": "Negative goodwill reported as a contra-asset liability amortized over 20 years",
                "B": "A deferred credit recognized in other comprehensive income",
                "C": "A gain on bargain purchase recognized immediately in profit or loss after reassessing identifiable assets and liabilities"
            },
            "answer": "C",
            "explanation": (
                "When consideration transferred is less than the fair value of net identifiable assets acquired:\n"
                "$$\\text{Bargain Purchase Amount} = 385 - 350 = 35 \\text{ million USD}$$\n"
                "Under both IFRS 3 and ASC 805:\n"
                "1. The acquirer must first reassess whether all identifiable assets acquired and liabilities assumed have been correctly identified and measured.\n"
                "2. Any remaining excess is recognized **immediately as an ordinary gain in profit or loss** on the acquisition date (gain on bargain purchase)."
            )
        }
    ]
    vignettes.extend(v04_questions)

    # =========================================================================
    # V05: Goodwill and Non-Controlling Interest (Partial vs Full Goodwill)
    # =========================================================================
    v05_text = (
        "On 1 January 2024, Vanguard Group acquired an 80% controlling interest in Baltic Manufacturing for 480 million EUR cash. "
        "At the acquisition date, the fair value of Baltic's net identifiable assets was 520 million EUR (the book value was 420 million EUR). "
        "An independent business appraiser estimated the fair value of the 20% Non-Controlling Interest (NCI) to be 110 million EUR on "
        "1 January 2024. Baltic is designated as a single cash-generating unit (CGU) under IFRS and a single reporting unit under US GAAP.\n\n"
        "Vanguard is preparing its consolidated financial statements and compares the Full Goodwill method (permitted under IFRS and "
        "mandatory under US GAAP) with the Partial Goodwill method (permitted under IFRS only).\n\n"
        "During 2024, Baltic generated net income of 50 million EUR and paid no dividends. Carrying value of net identifiable assets "
        "(excluding goodwill) at 31 December 2024 was 560 million EUR.\n\n"
        "At 31 December 2024, Vanguard performs an annual goodwill impairment test for the Baltic CGU/reporting unit. The recoverable "
        "amount of the entire Baltic CGU is determined to be 610 million EUR."
    )

    v05_questions = [
        {
            "id": "L2-V05-Q1",
            "level": 2,
            "module": "m13-intercorporate",
            "topic": "Intercorporate Investments",
            "vignette_id": "V05",
            "vignette_title": "Vanguard Group: Goodwill and Non-Controlling Interest (IFRS vs US GAAP)",
            "vignette_text": v05_text,
            "los": "LOS 13.e: calculate and explain goodwill and non-controlling interest and determine impairment under IFRS and US GAAP",
            "question": "The goodwill recognized on 1 January 2024 under the Full Goodwill method and Partial Goodwill method is closest to:",
            "options": {
                "A": "Full Goodwill: 70 million EUR; Partial Goodwill: 64 million EUR",
                "B": "Full Goodwill: 80 million EUR; Partial Goodwill: 64 million EUR",
                "C": "Full Goodwill: 70 million EUR; Partial Goodwill: 56 million EUR"
            },
            "answer": "A",
            "explanation": (
                "**Full Goodwill Method**:\n"
                "$$\\text{Total Fair Value of Target} = \\text{Consideration Paid} + \\text{Fair Value of NCI}$$\n"
                "$$\\text{Total Fair Value} = 480 + 110 = 590 \\text{ million EUR}$$\n"
                "$$\\text{Full Goodwill} = 590 - 520 = 70 \\text{ million EUR}$$\n\n"
                "**Partial Goodwill Method** (Proportionate share method):\n"
                "$$\\text{Acquirer's Share of Net Identifiable Assets} = 80\\% \\times 520 = 416 \\text{ million EUR}$$\n"
                "$$\\text{Partial Goodwill} = 480 - 416 = 64 \\text{ million EUR}$$"
            )
        },
        {
            "id": "L2-V05-Q2",
            "level": 2,
            "module": "m13-intercorporate",
            "topic": "Intercorporate Investments",
            "vignette_id": "V05",
            "vignette_title": "Vanguard Group: Goodwill and Non-Controlling Interest (IFRS vs US GAAP)",
            "vignette_text": v05_text,
            "los": "LOS 13.e: calculate and explain goodwill and non-controlling interest and determine impairment under IFRS and US GAAP",
            "question": "The balance sheet value of Non-Controlling Interest (NCI) on 1 January 2024 under the Full Goodwill and Partial Goodwill methods is:",
            "options": {
                "A": "Full Goodwill: 110 million EUR; Partial Goodwill: 104 million EUR",
                "B": "Full Goodwill: 104 million EUR; Partial Goodwill: 110 million EUR",
                "C": "Full Goodwill: 110 million EUR; Partial Goodwill: 110 million EUR"
            },
            "answer": "A",
            "explanation": (
                "**NCI Measurement**:\n"
                "1. **Full Goodwill Method**: NCI is measured at fair value = 110 million EUR.\n"
                "2. **Partial Goodwill Method**: NCI is measured at its proportionate share of the acquiree's net identifiable assets:\n"
                "$$\\text{NCI} = 20\\% \\times 520 \\text{ million EUR} = 104 \\text{ million EUR}$$\n\n"
                "Notice that the difference in NCI (${110} - 104 = 6\\text{ million EUR}$) exactly equals the difference in recognized goodwill (${70} - 64 = 6\\text{ million EUR}$)."
            )
        },
        {
            "id": "L2-V05-Q3",
            "level": 2,
            "module": "m13-intercorporate",
            "topic": "Intercorporate Investments",
            "vignette_id": "V05",
            "vignette_title": "Vanguard Group: Goodwill and Non-Controlling Interest (IFRS vs US GAAP)",
            "vignette_text": v05_text,
            "los": "LOS 13.e: calculate and explain goodwill and non-controlling interest and determine impairment under IFRS and US GAAP",
            "question": "Comparing the consolidated balance sheet under Full Goodwill versus Partial Goodwill at 1 January 2024, the Full Goodwill method results in:",
            "options": {
                "A": "Higher total assets by 6 million EUR and higher total shareholders' equity by 6 million EUR (all in NCI)",
                "B": "Higher total assets by 6 million EUR and higher parent retained earnings by 6 million EUR",
                "C": "Lower total assets by 6 million EUR and lower liabilities by 6 million EUR"
            },
            "answer": "A",
            "explanation": (
                "Under Full Goodwill:\n"
                "- Goodwill is 70 million EUR vs 64 million EUR (+6 million EUR assets).\n"
                "- NCI in equity is 110 million EUR vs 104 million EUR (+6 million EUR equity).\n"
                "- Equity attributable to Vanguard's shareholders is identical under both methods.\n"
                "- Therefore, total assets are 6 million EUR higher, and total equity is 6 million EUR higher (the increment resides entirely within the NCI equity component)."
            )
        },
        {
            "id": "L2-V05-Q4",
            "level": 2,
            "module": "m13-intercorporate",
            "topic": "Intercorporate Investments",
            "vignette_id": "V05",
            "vignette_title": "Vanguard Group: Goodwill and Non-Controlling Interest (IFRS vs US GAAP)",
            "vignette_text": v05_text,
            "los": "LOS 13.e: calculate and explain goodwill and non-controlling interest and determine impairment under IFRS and US GAAP",
            "question": "Under IFRS using the Partial Goodwill method, the goodwill impairment loss recognized in Vanguard's 2024 consolidated profit or loss is closest to:",
            "options": {
                "A": "24.0 million EUR",
                "B": "30.0 million EUR",
                "C": "34.0 million EUR"
            },
            "answer": "A",
            "explanation": (
                "Under IFRS (IAS 36), when partial goodwill is used:\n"
                "Step 1: Gross up partial goodwill to reflect 100% of the CGU's goodwill:\n"
                "$$\\text{Grossed-up Goodwill} = \\frac{64.0}{0.80} = 80.0 \\text{ million EUR}$$\n\n"
                "Step 2: Compare notional carrying value with recoverable amount:\n"
                "$$\\text{Notional Carrying Amount} = \\text{Net Identifiable Assets} + \\text{Grossed-up Goodwill}$$\n"
                "$$\\text{Notional Carrying Amount} = 560.0 + 80.0 = 640.0 \\text{ million EUR}$$\n"
                "$$\\text{Recoverable Amount} = 610.0 \\text{ million EUR}$$\n"
                "$$\\text{Notional Total Impairment} = 640.0 - 610.0 = 30.0 \\text{ million EUR}$$\n\n"
                "Step 3: Allocate impairment to parent's recognized partial goodwill:\n"
                "Because only Vanguard's 80% share of goodwill was recognized, Vanguard recognizes only its 80% share of the impairment:\n"
                "$$\\text{Recognized Impairment Loss} = 80\\% \\times 30.0 = 24.0 \\text{ million EUR}$$\n"
                "The remaining 6.0 million EUR notional loss belongs to NCI and is unrecorded."
            )
        },
        {
            "id": "L2-V05-Q5",
            "level": 2,
            "module": "m13-intercorporate",
            "topic": "Intercorporate Investments",
            "vignette_id": "V05",
            "vignette_title": "Vanguard Group: Goodwill and Non-Controlling Interest (IFRS vs US GAAP)",
            "vignette_text": v05_text,
            "los": "LOS 13.e: calculate and explain goodwill and non-controlling interest and determine impairment under IFRS and US GAAP",
            "question": "Under US GAAP (ASC 350) and Full Goodwill under IFRS, the goodwill impairment loss recognized in 2024 is closest to:",
            "options": {
                "A": "20.0 million EUR",
                "B": "24.0 million EUR",
                "C": "30.0 million EUR"
            },
            "answer": "A",
            "explanation": (
                "Under the Full Goodwill method (and US GAAP ASC 350 single-step impairment test):\n"
                "$$\\text{Carrying Amount of Reporting Unit/CGU} = \\text{Net Identifiable Assets} + \\text{Full Goodwill}$$\n"
                "$$\\text{Carrying Amount} = 560.0 + 70.0 = 630.0 \\text{ million EUR}$$\n"
                "$$\\text{Recoverable Amount / Fair Value} = 610.0 \\text{ million EUR}$$\n"
                "$$\\text{Impairment Loss} = \\text{Carrying Amount} - \\text{Recoverable Amount} = 630.0 - 610.0 = 20.0 \\text{ million EUR}$$\n\n"
                "Under Full Goodwill, the 20.0 million EUR impairment is allocated between the parent and NCI in proportion to their ownership (16.0 million EUR to parent, 4.0 million EUR to NCI)."
            )
        },
        {
            "id": "L2-V05-Q6",
            "level": 2,
            "module": "m13-intercorporate",
            "topic": "Intercorporate Investments",
            "vignette_id": "V05",
            "vignette_title": "Vanguard Group: Goodwill and Non-Controlling Interest (IFRS vs US GAAP)",
            "vignette_text": v05_text,
            "los": "LOS 13.e: calculate and explain goodwill and non-controlling interest and determine impairment under IFRS and US GAAP",
            "question": "All else equal, in the year of acquisition prior to impairment, how do Return on Assets (ROA) and Return on Equity (ROE) under the Full Goodwill method compare to the Partial Goodwill method?",
            "options": {
                "A": "Full Goodwill results in lower ROA and lower ROE (based on total equity)",
                "B": "Full Goodwill results in higher ROA and higher ROE",
                "C": "Full Goodwill results in identical ROA and identical ROE"
            },
            "answer": "A",
            "explanation": (
                "Under Full Goodwill:\n"
                "- Total assets are higher (due to higher full goodwill).\n"
                "- Total equity is higher (due to higher fair-value NCI).\n"
                "- Net income is identical (before any impairment).\n\n"
                "Therefore:\n"
                "$$\\text{ROA} = \\frac{\\text{Net Income}}{\\text{Total Assets}} \\quad (\\text{higher denominator} \\rightarrow \\text{lower ROA})$$\n"
                "$$\\text{ROE} = \\frac{\\text{Net Income}}{\\text{Total Equity}} \\quad (\\text{higher denominator} \\rightarrow \\text{lower ROE})$$"
            )
        }
    ]
    vignettes.extend(v05_questions)

    # =========================================================================
    # V06: Consolidation vs Equity Method vs Proportionate Consolidation
    # =========================================================================
    v06_text = (
        "Nexus Industrial is evaluating the acquisition of a 50% voting interest in Synergia Corp for 100 million USD. "
        "The carrying values of Synergia's assets and liabilities equal their fair values. The CFO asks the senior analyst "
        "to evaluate the comparative financial statement impacts for 2024 under three alternative accounting treatments:\n"
        "- Method 1: Full Consolidation (assuming Nexus obtains control with 50% NCI).\n"
        "- Method 2: Equity Method (assuming joint control or significant influence).\n"
        "- Method 3: Proportionate Consolidation (for comparison, as applied to joint operations under IFRS 11).\n\n"
        "Stand-alone financial data for the fiscal year ended 31 December 2024 (in million USD):\n"
        "| Financial Metric | Nexus Industrial | Synergia Corp (100%) |\n"
        "| :--- | :--- | :--- |\n"
        "| Revenue | 800.0 | 300.0 |\n"
        "| Operating Expenses | 640.0 | 240.0 |\n"
        "| Operating Profit (EBIT) | 160.0 | 60.0 |\n"
        "| Net Income | 100.0 | 40.0 |\n"
        "| Total Assets | 1,000.0 | 300.0 |\n"
        "| Total Debt | 400.0 | 100.0 |\n"
        "| Common Shareholders' Equity | 600.0 | 200.0 |\n\n"
        "There are no intercompany transactions between Nexus and Synergia."
    )

    v06_questions = [
        {
            "id": "L2-V06-Q1",
            "level": 2,
            "module": "m13-intercorporate",
            "topic": "Intercorporate Investments",
            "vignette_id": "V06",
            "vignette_title": "Nexus Industrial: Consolidation vs Equity Method vs Proportionate Consolidation",
            "vignette_text": v06_text,
            "los": "LOS 13.c: compare the financial statement effects of the equity method, proportionate consolidation, and acquisition method",
            "question": "The reported consolidated revenues under Full Consolidation, Proportionate Consolidation, and the Equity Method, respectively, are:",
            "options": {
                "A": "1,100 million USD, 950 million USD, and 800 million USD",
                "B": "1,100 million USD, 800 million USD, and 800 million USD",
                "C": "950 million USD, 950 million USD, and 800 million USD"
            },
            "answer": "A",
            "explanation": (
                "Revenue under the three methods:\n"
                "1. **Full Consolidation**: Nexus includes 100% of Synergia's revenue:\n"
                "$$\\text{Revenue} = 800.0 + 300.0 = 1,100.0 \\text{ million USD}$$\n"
                "2. **Proportionate Consolidation**: Nexus includes its 50% proportionate share:\n"
                "$$\\text{Revenue} = 800.0 + (50\\% \\times 300.0) = 800.0 + 150.0 = 950.0 \\text{ million USD}$$\n"
                "3. **Equity Method**: Only Nexus's stand-alone revenue is reported on the revenue line (Synergia's net income is reported as a single one-line item below operating profit):\n"
                "$$\\text{Revenue} = 800.0 \\text{ million USD}$$"
            )
        },
        {
            "id": "L2-V06-Q2",
            "level": 2,
            "module": "m13-intercorporate",
            "topic": "Intercorporate Investments",
            "vignette_id": "V06",
            "vignette_title": "Nexus Industrial: Consolidation vs Equity Method vs Proportionate Consolidation",
            "vignette_text": v06_text,
            "los": "LOS 13.c: compare the financial statement effects of the equity method, proportionate consolidation, and acquisition method",
            "question": "Net income attributable to Nexus's shareholders under Full Consolidation, Proportionate Consolidation, and the Equity Method will be:",
            "options": {
                "A": "Identical under all three methods at 120.0 million USD",
                "B": "Highest under Full Consolidation (140.0 million USD) and lowest under Equity Method (120.0 million USD)",
                "C": "Highest under Proportionate Consolidation (120.0 million USD) and lowest under Full Consolidation (100.0 million USD)"
            },
            "answer": "A",
            "explanation": (
                "Net income attributable to the parent company is **identical** under all three methods:\n"
                "1. **Equity Method**:\n"
                "$$\\text{Net Income} = \\text{Nexus Stand-alone Net Income} + 50\\% \\times \\text{Synergia Net Income}$$\n"
                "$$\\text{Net Income} = 100.0 + (50\\% \\times 40.0) = 100.0 + 20.0 = 120.0 \\text{ million USD}$$\n"
                "2. **Full Consolidation**:\n"
                "$$\\text{Consolidated Net Income} = 100.0 + 40.0 = 140.0 \\text{ million USD}$$\n"
                "$$\\text{Less: Non-Controlling Interest (NCI) share} = 50\\% \\times 40.0 = -20.0 \\text{ million USD}$$\n"
                "$$\\text{Net Income Attributable to Nexus} = 140.0 - 20.0 = 120.0 \\text{ million USD}$$\n"
                "3. **Proportionate Consolidation**:\n"
                "$$\\text{Net Income} = 100.0 + (50\\% \\times 40.0) = 120.0 \\text{ million USD}$$\n\n"
                "Parent net income and parent shareholders' equity are identical across all three methods."
            )
        },
        {
            "id": "L2-V06-Q3",
            "level": 2,
            "module": "m13-intercorporate",
            "topic": "Intercorporate Investments",
            "vignette_id": "V06",
            "vignette_title": "Nexus Industrial: Consolidation vs Equity Method vs Proportionate Consolidation",
            "vignette_text": v06_text,
            "los": "LOS 13.c: compare the financial statement effects of the equity method, proportionate consolidation, and acquisition method",
            "question": "The reported Net Profit Margin (Net Income attributable to parent / Revenue) under Full Consolidation, Proportionate Consolidation, and the Equity Method, respectively, is closest to:",
            "options": {
                "A": "10.91%, 12.63%, and 15.00%",
                "B": "15.00%, 12.63%, and 10.91%",
                "C": "12.73%, 12.73%, and 12.73%"
            },
            "answer": "A",
            "explanation": (
                "Computing Net Profit Margin under each method:\n"
                "1. **Full Consolidation**:\n"
                "$$\\text{Net Margin} = \\frac{120.0}{1,100.0} = 10.91\\%$$\n"
                "2. **Proportionate Consolidation**:\n"
                "$$\\text{Net Margin} = \\frac{120.0}{950.0} = 12.63\\%$$\n"
                "3. **Equity Method**:\n"
                "$$\\text{Net Margin} = \\frac{120.0}{800.0} = 15.00\\%$$\n\n"
                "The Equity Method yields the highest net profit margin because the numerator includes 50% of the associate's net income, while the denominator includes zero associate revenue."
            )
        },
        {
            "id": "L2-V06-Q4",
            "level": 2,
            "module": "m13-intercorporate",
            "topic": "Intercorporate Investments",
            "vignette_id": "V06",
            "vignette_title": "Nexus Industrial: Consolidation vs Equity Method vs Proportionate Consolidation",
            "vignette_text": v06_text,
            "los": "LOS 13.c: compare the financial statement effects of the equity method, proportionate consolidation, and acquisition method",
            "question": "The reported Debt-to-Equity ratio (Total Debt / Parent Equity) under the Equity Method and Proportionate Consolidation is closest to:",
            "options": {
                "A": "Equity Method: 0.67; Proportionate Consolidation: 0.75",
                "B": "Equity Method: 0.50; Proportionate Consolidation: 0.60",
                "C": "Equity Method: 0.75; Proportionate Consolidation: 0.67"
            },
            "answer": "A",
            "explanation": (
                "Parent equity is 600.0 million USD under all methods.\n"
                "1. **Equity Method**:\n"
                "- Debt includes only Nexus stand-alone debt = 400.0 million USD.\n"
                "$$\\text{Debt-to-Equity} = \\frac{400.0}{600.0} = 0.667 \\approx 0.67$$\n"
                "2. **Proportionate Consolidation**:\n"
                "- Debt includes Nexus debt + 50% of Synergia debt = ${400.0} + (50\\% \\times 100.0) = 450.0\\text{ million USD}$.\n"
                "$$\\text{Debt-to-Equity} = \\frac{450.0}{600.0} = 0.750 = 0.75$$\n\n"
                "*(Note: Under Full Consolidation, total debt would be ${400} + 100 = 500\\text{ million USD}$, resulting in a Debt / Parent Equity ratio of ${500} / 600 = 0.83$).*"
            )
        },
        {
            "id": "L2-V06-Q5",
            "level": 2,
            "module": "m13-intercorporate",
            "topic": "Intercorporate Investments",
            "vignette_id": "V06",
            "vignette_title": "Nexus Industrial: Consolidation vs Equity Method vs Proportionate Consolidation",
            "vignette_text": v06_text,
            "los": "LOS 13.c: compare the financial statement effects of the equity method, proportionate consolidation, and acquisition method",
            "question": "Regarding Return on Equity (ROE, defined as Net Income attributable to parent / Parent Equity) across the three accounting methods:",
            "options": {
                "A": "ROE is identical across all three methods at 20.0%",
                "B": "ROE is highest under Full Consolidation",
                "C": "ROE is highest under the Equity Method"
            },
            "answer": "A",
            "explanation": (
                "Because both the numerator (Net income attributable to parent = 120.0 million USD) and the denominator (Shareholders' equity attributable to parent = 600.0 million USD) are **identical** under Full Consolidation, Proportionate Consolidation, and the Equity Method:\n"
                "$$\\text{ROE} = \\frac{120.0}{600.0} = 20.0\\%$$\n"
                "ROE is strictly identical across all three methods."
            )
        },
        {
            "id": "L2-V06-Q6",
            "level": 2,
            "module": "m13-intercorporate",
            "topic": "Intercorporate Investments",
            "vignette_id": "V06",
            "vignette_title": "Nexus Industrial: Consolidation vs Equity Method vs Proportionate Consolidation",
            "vignette_text": v06_text,
            "los": "LOS 13.c: compare the financial statement effects of the equity method, proportionate consolidation, and acquisition method",
            "question": "When an analyst evaluates an entity that uses the equity method for a highly leveraged investee, the most appropriate analytical adjustment is to:",
            "options": {
                "A": "Proportionately combine the investee's assets, liabilities, revenues, and expenses with the investor to uncover off-balance-sheet leverage",
                "B": "Reclassify the investee's dividends from cash from operations to cash from financing",
                "C": "Deduct the equity method carrying amount directly from common equity to reduce book value"
            },
            "answer": "A",
            "explanation": (
                "The equity method is often referred to as 'one-line consolidation' because the investee's liabilities and debt do not appear on the investor's balance sheet (hidden leverage).\n"
                "To reflect economic reality and properly evaluate financial risk, analysts perform a proportionate consolidation adjustment: adding the investor's proportionate share of the investee's assets, debt, revenues, and operating expenses to the consolidated statements."
            )
        }
    ]
    vignettes.extend(v06_questions)

    # =========================================================================
    # V07: Variable Interest Entities (VIEs) & De Facto Control
    # =========================================================================
    v07_text = (
        "Titan Capital is a diversified industrial financing and equipment conglomerate. To finance the acquisition and leasing "
        "of a modern fleet of commercial aircraft, Titan structured a special purpose vehicle named Zenith Equipment Trust (ZET). "
        "Titan's accounting team is analyzing ZET's consolidation status under US GAAP (ASC 810) and IFRS 10.\n\n"
        "Capitalization and governance structure of ZET:\n"
        "- Total assets: 200 million USD of commercial aircraft.\n"
        "- Senior secured debt: 120 million USD issued to external commercial banks, collateralized by the aircraft.\n"
        "- Subordinated debt: 60 million USD provided by Titan Capital with an annual coupon of 8.5%.\n"
        "- Equity capital: 20 million USD contributed by independent institutional investors (representing 10% of total assets). "
        "The equity investors have nominal voting rights.\n\n"
        "Contractual and operational agreements:\n"
        "1. Titan acts as the sole asset manager and servicer of ZET under a long-term contract, with sole authority to select "
        "airline lessees, negotiate lease rates, oversee maintenance schedules, and remarket or sell aircraft upon lease termination.\n"
        "2. Titan has provided a partial guarantee covering up to 30 million USD of first losses on the senior debt.\n"
        "3. After paying senior debt service and a fixed 7% preferred dividend to the equity investors, Titan is entitled to receive "
        "75% of ZET's residual profits and cash flows."
    )

    v07_questions = [
        {
            "id": "L2-V07-Q1",
            "level": 2,
            "module": "m13-intercorporate",
            "topic": "Intercorporate Investments",
            "vignette_id": "V07",
            "vignette_title": "Titan Capital: Variable Interest Entities (VIEs) and Control Assessment",
            "vignette_text": v07_text,
            "los": "LOS 13.f: identify a variable interest entity (VIE) and determine whether a VIE should be consolidated",
            "question": "Under US GAAP (ASC 810), which characteristic most clearly indicates that Zenith Equipment Trust (ZET) is a Variable Interest Entity (VIE)?",
            "options": {
                "A": "The equity investment at risk is insufficient to finance the entity's activities without additional subordinated financial support, and the equity holders lack decision-making rights",
                "B": "The entity has issued both senior and subordinated debt tranches",
                "C": "The entity was created to hold long-lived depreciable assets rather than liquid securities"
            },
            "answer": "A",
            "explanation": (
                "Under US GAAP (ASC 810), an entity is a Variable Interest Entity (VIE) if it exhibits any of the following conditions:\n"
                "1. Total equity investment at risk is not sufficient to permit the entity to finance its activities without additional subordinated financial support (generally less than 10% of total assets, or unable to absorb expected losses).\n"
                "2. Equity investors at risk lack any of the following key characteristics of a controlling financial interest:\n"
                "- The power, through voting rights or similar rights, to direct the activities that most significantly impact economic performance.\n"
                "- The obligation to absorb expected losses.\n"
                "- The right to receive expected residual returns.\n\n"
                "ZET exhibits both: equity investors have nominal voting rights (Titan directs the activities) and equity cannot absorb expected losses without Titan's subordinated debt and guarantees."
            )
        },
        {
            "id": "L2-V07-Q2",
            "level": 2,
            "module": "m13-intercorporate",
            "topic": "Intercorporate Investments",
            "vignette_id": "V07",
            "vignette_title": "Titan Capital: Variable Interest Entities (VIEs) and Control Assessment",
            "vignette_text": v07_text,
            "los": "LOS 13.f: identify a variable interest entity (VIE) and determine whether a VIE should be consolidated",
            "question": "Under US GAAP (ASC 810), Titan Capital must consolidate ZET if Titan is determined to be the Primary Beneficiary. Titan is the primary beneficiary because it possesses:",
            "options": {
                "A": "The power to direct the activities that most significantly impact economic performance, AND the obligation to absorb losses or right to receive residual returns",
                "B": "More than 50% of the voting equity shares of the entity",
                "C": "A legal guarantee covering 100% of the entity's senior debt liabilities"
            },
            "answer": "A",
            "explanation": (
                "Under US GAAP (ASC 810), an enterprise is the **Primary Beneficiary** of a VIE and must consolidate it if it has **both**:\n"
                "1. **Power Criterion**: The power to direct the activities of the VIE that most significantly impact the entity's economic performance (Titan directs leasing, maintenance, and remarketing).\n"
                "2. **Economics Criterion**: The obligation to absorb losses of the VIE or the right to receive benefits from the VIE that could potentially be significant to the VIE (Titan holds subordinated debt, provides debt guarantees, and receives 75% of residual returns)."
            )
        },
        {
            "id": "L2-V07-Q3",
            "level": 2,
            "module": "m13-intercorporate",
            "topic": "Intercorporate Investments",
            "vignette_id": "V07",
            "vignette_title": "Titan Capital: Variable Interest Entities (VIEs) and Control Assessment",
            "vignette_text": v07_text,
            "los": "LOS 13.f: identify a variable interest entity (VIE) and determine whether a VIE should be consolidated",
            "question": "Under IFRS 10, control over an investee exists if and only if the investor possesses three specific elements. Which of the following is NOT one of the three required control elements?",
            "options": {
                "A": "Ownership of more than 50% of the legal voting shares of the investee",
                "B": "Power over the investee (existing rights that give current ability to direct relevant activities)",
                "C": "Ability to use its power over the investee to affect the amount of the investor's returns"
            },
            "answer": "A",
            "explanation": (
                "Under IFRS 10, control requires three elements regardless of legal ownership structure:\n"
                "1. **Power**: Rights that give the current ability to direct the relevant activities (the activities that significantly affect returns).\n"
                "2. **Exposure or rights to variable returns**: From its involvement with the investee.\n"
                "3. **Linkage**: The ability to use its power over the investee to affect the amount of its returns (acting as principal, not agent).\n\n"
                "Ownership of more than 50% of voting shares is **not** required; IFRS 10 explicitly recognizes de facto control and control through contractual arrangements."
            )
        },
        {
            "id": "L2-V07-Q4",
            "level": 2,
            "module": "m13-intercorporate",
            "topic": "Intercorporate Investments",
            "vignette_id": "V07",
            "vignette_title": "Titan Capital: Variable Interest Entities (VIEs) and Control Assessment",
            "vignette_text": v07_text,
            "los": "LOS 13.f: identify a variable interest entity (VIE) and determine whether a VIE should be consolidated",
            "question": "If Titan Capital consolidates ZET on its balance sheet, the net addition to Titan's consolidated total assets and third-party liabilities (excluding intercompany eliminations) is closest to:",
            "options": {
                "A": "Total Assets increase by 200 million USD; Third-Party Liabilities increase by 120 million USD",
                "B": "Total Assets increase by 140 million USD; Third-Party Liabilities increase by 180 million USD",
                "C": "Total Assets increase by 200 million USD; Third-Party Liabilities increase by 180 million USD"
            },
            "answer": "A",
            "explanation": (
                "Upon consolidation:\n"
                "1. **Assets**: ZET's aircraft fleet of 200 million USD is added to consolidated assets.\n"
                "2. **Liabilities**: Senior secured debt of 120 million USD owed to external banks is recognized as third-party debt.\n"
                "3. **Intercompany Elimination**: Titan's 60 million USD subordinated debt loan to ZET is an intercompany asset and liability and is fully eliminated in consolidation.\n"
                "4. **Equity**: The 20 million USD third-party equity is recognized as Non-Controlling Interest (NCI) in consolidated equity."
            )
        },
        {
            "id": "L2-V07-Q5",
            "level": 2,
            "module": "m13-intercorporate",
            "topic": "Intercorporate Investments",
            "vignette_id": "V07",
            "vignette_title": "Titan Capital: Variable Interest Entities (VIEs) and Control Assessment",
            "vignette_text": v07_text,
            "los": "LOS 13.f: identify a variable interest entity (VIE) and determine whether a VIE should be consolidated",
            "question": "The impact of consolidating ZET on Titan Capital's leverage ratios is most likely to:",
            "options": {
                "A": "Increase reported financial leverage and worsen the Debt-to-Equity ratio",
                "B": "Decrease reported financial leverage because assets increase by 200 million USD",
                "C": "Have no effect on leverage ratios because intercompany debt is eliminated"
            },
            "answer": "A",
            "explanation": (
                "Consolidating ZET adds 120 million USD of third-party debt to Titan's balance sheet, while parent common equity is unchanged (the 20 million USD equity is attributed to NCI).\n"
                "Consequently:\n"
                "$$\\text{Debt-to-Equity} = \\frac{\\text{Total Debt}}{\\text{Common Equity}} \\quad (\\text{increases significantly})$$\n"
                "Financial leverage ratios worsen, reflecting the enterprise's true legal and economic debt exposure."
            )
        },
        {
            "id": "L2-V07-Q6",
            "level": 2,
            "module": "m13-intercorporate",
            "topic": "Intercorporate Investments",
            "vignette_id": "V07",
            "vignette_title": "Titan Capital: Variable Interest Entities (VIEs) and Control Assessment",
            "vignette_text": v07_text,
            "los": "LOS 13.f: identify a variable interest entity (VIE) and determine whether a VIE should be consolidated",
            "question": "If an entity holds a significant variable interest in a VIE but is NOT the primary beneficiary, US GAAP requires disclosure of:",
            "options": {
                "A": "The nature, purpose, size of the VIE, and the maximum exposure to loss as a result of its involvement",
                "B": "Pro-forma consolidated financial statements including the VIE as if it were a full subsidiary",
                "C": "No disclosures are required if the entity does not consolidate the VIE"
            },
            "answer": "A",
            "explanation": (
                "Under US GAAP (ASC 810) and IFRS 12 (Disclosure of Interests in Other Entities):\n"
                "An enterprise that holds a significant variable interest in an unconsolidated VIE must disclose:\n"
                "1. The nature, purpose, size, and activities of the VIE.\n"
                "2. The carrying amounts and classification of assets and liabilities related to its involvement.\n"
                "3. Its **maximum exposure to loss** as a result of its involvement with the VIE, and how the maximum exposure is determined."
            )
        }
    ]
    vignettes.extend(v07_questions)

    # =========================================================================
    # V08: Advanced Intercorporate Issues: Step Acquisitions & Deconsolidation
    # =========================================================================
    v08_text = (
        "Pacific Retail Corp is a global retail holding corporation that prepares financial statements under IFRS.\n\n"
        "Transaction 1: Step Acquisition of Asian Express\n"
        "On 1 January 2022, Pacific acquired a 25% voting equity interest in Asian Express for 50 million USD, classifying "
        "it as an associate accounted for under the equity method. By 31 December 2023, Pacific's cumulative share of Asian "
        "Express's net income less dividends had increased the carrying value of the investment to 65 million USD.\n\n"
        "On 1 January 2024, Pacific acquired an additional 45% voting interest in Asian Express for 135 million USD in cash, "
        "bringing its total voting interest to 70% and achieving control. On 1 January 2024:\n"
        "- The fair value of Pacific's previously held 25% equity interest was appraised at 75 million USD.\n"
        "- The fair value of the 30% Non-Controlling Interest (NCI) was appraised at 90 million USD.\n"
        "- The fair value of Asian Express's net identifiable assets was 260 million USD.\n\n"
        "Transaction 2: Deconsolidation and Sale of EuroTrade\n"
        "On 30 June 2024, Pacific sold an 80% controlling interest in its wholly owned European subsidiary, EuroTrade SA, for "
        "200 million EUR cash, retaining a 20% passive equity investment. On 30 June 2024:\n"
        "- The carrying value of EuroTrade's net identifiable assets was 180 million EUR.\n"
        "- The fair value of Pacific's retained 20% investment was 50 million EUR.\n"
        "- Cumulative foreign currency translation gains recognized in OCI attributable to EuroTrade amounted to 30 million EUR."
    )

    v08_questions = [
        {
            "id": "L2-V08-Q1",
            "level": 2,
            "module": "m13-intercorporate",
            "topic": "Intercorporate Investments",
            "vignette_id": "V08",
            "vignette_title": "Pacific Retail: Step Acquisitions, Deconsolidation, and Foreign Subsidiaries",
            "vignette_text": v08_text,
            "los": "LOS 13.d: describe the acquisition method of accounting for a business combination and determine goodwill at the acquisition date",
            "question": "In the step acquisition of Asian Express on 1 January 2024, the gain or loss recognized in Pacific's profit or loss on remeasuring its previously held 25% interest is:",
            "options": {
                "A": "A gain of 10 million USD",
                "B": "A gain of 25 million USD",
                "C": "Zero, because changes in fair value of equity method investments are deferred in equity"
            },
            "answer": "A",
            "explanation": (
                "Under both IFRS 3 and ASC 805 (Business Combinations):\n"
                "In a business combination achieved in stages (step acquisition):\n"
                "1. The acquirer remeasures its previously held equity interest at its acquisition-date fair value.\n"
                "2. Any resulting gain or loss is recognized **immediately in profit or loss**:\n"
                "$$\\text{Acquisition-Date Fair Value of 25\\% Interest} = 75 \\text{ million USD}$$\n"
                "$$\\text{Carrying Amount under Equity Method} = 65 \\text{ million USD}$$\n"
                "$$\\text{Remeasurement Gain recognized in P&L} = 75 - 65 = 10 \\text{ million USD}$$"
            )
        },
        {
            "id": "L2-V08-Q2",
            "level": 2,
            "module": "m13-intercorporate",
            "topic": "Intercorporate Investments",
            "vignette_id": "V08",
            "vignette_title": "Pacific Retail: Step Acquisitions, Deconsolidation, and Foreign Subsidiaries",
            "vignette_text": v08_text,
            "los": "LOS 13.d: describe the acquisition method of accounting for a business combination and determine goodwill at the acquisition date",
            "question": "Under the Full Goodwill method, the goodwill recognized in Pacific's consolidated balance sheet for the business combination with Asian Express is closest to:",
            "options": {
                "A": "40 million USD",
                "B": "50 million USD",
                "C": "65 million USD"
            },
            "answer": "A",
            "explanation": (
                "Goodwill under Full Goodwill in a step acquisition:\n"
                "$$\\text{Total Consideration/Enterprise Value} = \\text{New Cash Paid} + \\text{FV of Previously Held Interest} + \\text{FV of NCI}$$\n"
                "$$\\text{Total Enterprise Value} = 135 + 75 + 90 = 300 \\text{ million USD}$$\n"
                "$$\\text{Fair Value of Net Identifiable Assets} = 260 \\text{ million USD}$$\n"
                "$$\\text{Full Goodwill} = 300 - 260 = 40 \\text{ million USD}$$"
            )
        },
        {
            "id": "L2-V08-Q3",
            "level": 2,
            "module": "m13-intercorporate",
            "topic": "Intercorporate Investments",
            "vignette_id": "V08",
            "vignette_title": "Pacific Retail: Step Acquisitions, Deconsolidation, and Foreign Subsidiaries",
            "vignette_text": v08_text,
            "los": "LOS 13.e: calculate and explain goodwill and non-controlling interest and determine impairment under IFRS and US GAAP",
            "question": "If Pacific subsequently purchases an additional 10% of Asian Express's shares from the non-controlling shareholders for 32 million USD, the transaction is accounted for as:",
            "options": {
                "A": "An equity transaction with owners: the difference between consideration paid and NCI carrying value is adjusted directly against parent equity, with zero change in goodwill",
                "B": "A new business combination where incremental goodwill is recognized for the excess consideration",
                "C": "An investment in associate recognized in profit or loss"
            },
            "answer": "A",
            "explanation": (
                "Under both IFRS 10 and US GAAP (ASC 810):\n"
                "- Once control is already obtained, subsequent transactions with non-controlling interest shareholders (acquiring additional NCI shares or selling a portion of shares while retaining control) are **equity transactions** (transactions between owners in their capacity as owners).\n"
                "- No gain or loss is recognized in profit or loss.\n"
                "- **Goodwill is never adjusted**.\n"
                "- The difference between the consideration transferred and the carrying amount of NCI acquired is adjusted directly in the parent company's equity."
            )
        },
        {
            "id": "L2-V08-Q4",
            "level": 2,
            "module": "m13-intercorporate",
            "topic": "Intercorporate Investments",
            "vignette_id": "V08",
            "vignette_title": "Pacific Retail: Step Acquisitions, Deconsolidation, and Foreign Subsidiaries",
            "vignette_text": v08_text,
            "los": "LOS 13.d: describe the acquisition method of accounting for a business combination and determine goodwill at the acquisition date",
            "question": "On the sale and deconsolidation of EuroTrade SA on 30 June 2024, the total gain recognized by Pacific in profit or loss is closest to:",
            "options": {
                "A": "70 million EUR",
                "B": "100 million EUR",
                "C": "40 million EUR"
            },
            "answer": "B",
            "explanation": (
                "Under IFRS 10, when a parent loses control of a subsidiary (deconsolidation):\n"
                "$$\\text{Total Consideration Received} = 200 \\text{ million EUR}$$\n"
                "$$\\text{Fair Value of Retained 20\\% Investment} = 50 \\text{ million EUR}$$\n"
                "$$\\text{Total Value Realized} = 200 + 50 = 250 \\text{ million EUR}$$\n"
                "$$\\text{Less: Carrying Value of Net Assets Derecognized} = -180 \\text{ million EUR}$$\n"
                "$$\\text{Gain before OCI Recycling} = 250 - 180 = 70 \\text{ million EUR}$$\n\n"
                "In addition, cumulative foreign exchange translation gains in OCI attributable to the subsidiary **must be reclassified (recycled) to profit or loss** upon disposal:\n"
                "$$\\text{Recycled Translation Gain} = +30 \\text{ million EUR}$$\n\n"
                "$$\\text{Total Gain Recognized in Profit or Loss} = 70 + 30 = 100 \\text{ million EUR}$$"
            )
        },
        {
            "id": "L2-V08-Q5",
            "level": 2,
            "module": "m13-intercorporate",
            "topic": "Intercorporate Investments",
            "vignette_id": "V08",
            "vignette_title": "Pacific Retail: Step Acquisitions, Deconsolidation, and Foreign Subsidiaries",
            "vignette_text": v08_text,
            "los": "LOS 13.d: describe the acquisition method of accounting for a business combination and determine goodwill at the acquisition date",
            "question": "Following the sale of 80% of EuroTrade, Pacific's retained 20% equity interest must be initially measured on the balance sheet at:",
            "options": {
                "A": "Its fair value of 50 million EUR on the date control was lost",
                "B": "Its historical carrying amount of 36 million EUR (20% of 180 million EUR net assets)",
                "C": "Zero, because the investment was previously part of a consolidated group"
            },
            "answer": "A",
            "explanation": (
                "Under IFRS 10 and US GAAP (ASC 810):\n"
                "Upon loss of control of a subsidiary, any retained non-controlling investment is derecognized from consolidation and remeasured at its **fair value** at the date when control is lost (50 million EUR).\n"
                "This fair value becomes its new cost basis for subsequent accounting (e.g., under the equity method or as a financial asset under IFRS 9 / ASC 321)."
            )
        },
        {
            "id": "L2-V08-Q6",
            "level": 2,
            "module": "m13-intercorporate",
            "topic": "Intercorporate Investments",
            "vignette_id": "V08",
            "vignette_title": "Pacific Retail: Step Acquisitions, Deconsolidation, and Foreign Subsidiaries",
            "vignette_text": v08_text,
            "los": "LOS 13.c: compare the financial statement effects of the equity method, proportionate consolidation, and acquisition method",
            "question": "When an analyst reviews an acquirer's historical financial statements across a period that includes a step acquisition, the analyst should be most cautious about:",
            "options": {
                "A": "A distortion in revenue and EBITDA growth rates, because the acquiree's revenues are included only post-acquisition while the prior periods include only equity method net income",
                "B": "An automatic restatement of all historical prior-period revenue and balance sheet items",
                "C": "Understatement of return on equity due to exclusion of remeasurement gains from net income"
            },
            "answer": "A",
            "explanation": (
                "In a step acquisition, historical financial statements are **not restated retroactively**.\n"
                "Prior to obtaining control, the investor reported 0 USD of the acquiree's revenue and recognized only its share of net income in a single line item.\n"
                "Post-acquisition, 100% of the acquiree's revenue and operating expenses are consolidated.\n"
                "This creates a substantial structural break and artificial jump in revenue and EBITDA growth. Analysts must adjust for pro-forma figures or organic growth to make valid comparisons."
            )
        }
    ]
    vignettes.extend(v08_questions)

    return vignettes

if __name__ == "__main__":
    v = get_vignettes_topic13()
    print("Topic 13 Questions Generated:", len(v))
