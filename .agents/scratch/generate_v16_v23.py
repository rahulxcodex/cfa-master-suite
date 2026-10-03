# -*- coding: utf-8 -*-
"""
generate_v16_v23.py
Generates Vignettes 16 through 23 (48 questions) for Topic 15: Multinational Operations.
Strict currency compliance: USD, EUR, GBP, CHF, NOK, SGD, ZAR, ARS, LC.
Math equations use KaTeX delimiters. No bare dollar signs before digits.
"""

def get_vignettes_16_to_23():
    vignettes = []

    # =========================================================================
    # VIGNETTE 16: Functional Currency Determination & IAS 21 / ASC 830
    # =========================================================================
    v16_text = (
        "Elena Vance, CFA, is a senior multinational equity analyst at Kensington Capital. "
        "She is currently evaluating the international subsidiaries of Northgate Industries, "
        "a multinational industrial conglomerate based in the United States that presents its "
        "consolidated financial statements in US dollars (USD).\n\n"
        "Vance gathers operational and financial data for three wholly owned foreign subsidiaries:\n\n"
        "1. Batavia BV (Netherlands): Batavia manufactures and distributes industrial valves "
        "throughout the Eurozone. Pricing of its products is dictated by aggressive local competition "
        "in Germany and France and is invoiced exclusively in euros (EUR). Raw materials and local "
        "labor are procured within the European Union and paid in EUR. Batavia secured a long-term "
        "credit facility with an Amsterdam-based bank denominated in EUR, which is serviced solely "
        "from Batavia's operating cash flows without any parent guarantee or parent cash infusions. "
        "Surplus cash flows are routinely retained in the Netherlands to fund regional expansion.\n\n"
        "2. Montrose Ltd (United Kingdom): Montrose operates as an assembly and packaging facility "
        "for specialized aircraft sensors. Over 92% of the sub-components assembled by Montrose are "
        "engineered and shipped directly from Northgate's main manufacturing facility in Ohio. "
        "Montrose sells 95% of its assembled output back to the US parent company, and all transactions "
        "are invoiced and settled in USD. Montrose's day-to-day working capital requirements are "
        "continuously funded by an intercompany revolving credit line denominated in USD provided by "
        "Northgate, and Montrose remits all operating cash surpluses back to the US parent weekly.\n\n"
        "3. Solaria SpA (Italy): Solaria manufactures specialty solar inverters. It sells inverters "
        "to commercial distributors globally. While sales contracts are denominated in EUR, the contract "
        "prices are mechanically indexed to global benchmark prices established in USD. Local labor "
        "and overhead are incurred in EUR, but high-tech electronic components (comprising 65% of total "
        "costs) are sourced internationally and invoiced in USD. Solaria's management has full pricing "
        "discretion within southern Europe, but its capital budget and long-term financing are controlled "
        "and guaranteed by Northgate in the United States.\n\n"
        "Northgate prepares its consolidated financial statements in accordance with IFRS (IAS 21: "
        "The Effects of Changes in Foreign Exchange Rates), but Vance also needs to evaluate the "
        "implications if the company reported under US GAAP (ASC 830)."
    )

    v16_questions = [
        {
            "id": "L2-V16-Q1",
            "level": 2,
            "module": "m15-multinational",
            "topic": "Multinational Operations",
            "vignette_id": "V16",
            "vignette_title": "Global Manufacturing Corp: Functional Currency Determination & IAS 21 / ASC 830 Criteria",
            "vignette_text": v16_text,
            "los": "LOS 15.a: Distinguish between the local currency, functional currency, and presentation currency, and determine an entity's functional currency under IFRS and US GAAP.",
            "question": "Under IAS 21, which currency is most appropriately designated as Batavia BV's functional currency?",
            "options": {
                "A": "The US dollar (USD), because it is the reporting currency of the ultimate parent entity.",
                "B": "The euro (EUR), because Batavia's sales prices, operating expenses, and financing are predominantly determined in the Eurozone.",
                "C": "The British pound (GBP), because European industrial valve markets benchmark regional contracts to London exchange prices."
            },
            "answer": "B",
            "explanation": (
                "Under IAS 21, the functional currency is the currency of the primary economic environment "
                "in which the entity operates. Primary indicators include the currency that mainly influences sales "
                "prices for goods and services, and the currency of the country whose competitive forces and regulations "
                "mainly determine sales prices, as well as the currency that mainly influences labor, material, and other costs. "
                "Batavia's sales prices are determined by local competition in Germany and France and invoiced in EUR, "
                "its labor and materials are paid in EUR, and its financing is locally sourced in EUR without parent recourse. "
                "Therefore, the euro (EUR) is clearly its functional currency.\n\n"
                "Distractor A is incorrect because the parent's presentation currency does not dictate the subsidiary's "
                "functional currency when the subsidiary is an autonomous, self-sustaining foreign operation.\n\n"
                "Distractor C is incorrect because Batavia operates in the Netherlands and Eurozone with no operational "
                "or sales connection to the British pound."
            )
        },
        {
            "id": "L2-V16-Q2",
            "level": 2,
            "module": "m15-multinational",
            "topic": "Multinational Operations",
            "vignette_id": "V16",
            "vignette_title": "Global Manufacturing Corp: Functional Currency Determination & IAS 21 / ASC 830 Criteria",
            "vignette_text": v16_text,
            "los": "LOS 15.a: Distinguish between the local currency, functional currency, and presentation currency, and determine an entity's functional currency under IFRS and US GAAP.",
            "question": "Regarding Montrose Ltd, which functional currency and translation method must Northgate apply in consolidation?",
            "options": {
                "A": "Functional currency is GBP; translation method is the Current Rate Method.",
                "B": "Functional currency is USD; translation method is the Temporal Method (remeasurement).",
                "C": "Functional currency is USD; translation method is the Current Rate Method."
            },
            "answer": "B",
            "explanation": (
                "Montrose acts as a direct extension of the US parent company: 92% of components come from the US parent, "
                "95% of sales are made directly to the parent in USD, working capital is financed by the parent in USD, "
                "and cash surpluses are remitted weekly to the parent. Under both IAS 21 and ASC 830, when a foreign subsidiary "
                "operates as a conduit or integrated operational arm of the parent, its functional currency is the parent's "
                "currency (USD). When the local books are kept in local currency (GBP) but the functional currency is USD, "
                "the financial statements must be remeasured into the functional currency (USD) using the Temporal Method.\n\n"
                "Distractor A is incorrect because Montrose does not operate autonomously, so GBP cannot be the functional currency.\n\n"
                "Distractor C is incorrect because when the functional currency is the parent's presentation currency, the required "
                "method is remeasurement via the Temporal Method, not the Current Rate Method."
            )
        },
        {
            "id": "L2-V16-Q3",
            "level": 2,
            "module": "m15-multinational",
            "topic": "Multinational Operations",
            "vignette_id": "V16",
            "vignette_title": "Global Manufacturing Corp: Functional Currency Determination & IAS 21 / ASC 830 Criteria",
            "vignette_text": v16_text,
            "los": "LOS 15.b: Compare the current rate method and the temporal method, evaluate how each method affects the parent company's balance sheet and income statement.",
            "question": "Where are translation adjustments arising from Batavia BV and Montrose Ltd reported in Northgate's consolidated financial statements?",
            "options": {
                "A": "Batavia's adjustments appear in OCI (Cumulative Translation Adjustment); Montrose's adjustments appear in the consolidated Income Statement.",
                "B": "Both Batavia's and Montrose's translation adjustments appear in Other Comprehensive Income (OCI).",
                "C": "Batavia's adjustments appear in the Income Statement; Montrose's adjustments appear in OCI."
            },
            "answer": "A",
            "explanation": (
                "Under the Current Rate Method (applied to Batavia BV because its functional currency is EUR, differing from the parent's "
                "presentation currency USD), the translation gains and losses are accumulated in equity as a Cumulative Translation "
                "Adjustment (CTA) under Other Comprehensive Income (OCI). Under the Temporal Method (applied to Montrose Ltd because "
                "its functional currency is the parent's presentation currency USD), remeasurement gains and losses are recognized "
                "immediately in the consolidated Income Statement.\n\n"
                "Distractor B is incorrect because remeasurement gains and losses under the temporal method flow through net income.\n\n"
                "Distractor C is the exact inverse of the correct accounting standards."
            )
        },
        {
            "id": "L2-V16-Q4",
            "level": 2,
            "module": "m15-multinational",
            "topic": "Multinational Operations",
            "vignette_id": "V16",
            "vignette_title": "Global Manufacturing Corp: Functional Currency Determination & IAS 21 / ASC 830 Criteria",
            "vignette_text": v16_text,
            "los": "LOS 15.a: Distinguish between the local currency, functional currency, and presentation currency, and determine an entity's functional currency under IFRS and US GAAP.",
            "question": "When evaluating Solaria SpA under IAS 21 where primary economic indicators provide mixed signals, which secondary factor most strongly points toward the US dollar as its functional currency?",
            "options": {
                "A": "The geographic location of its manufacturing plants within Italy.",
                "B": "The degree of operational independence and the fact that financing is provided and guaranteed by the US parent.",
                "C": "The language utilized in regional distributor sales contracts."
            },
            "answer": "B",
            "explanation": (
                "Under IAS 21.10-11, when primary indicators are mixed or inconclusive, management examines secondary indicators: "
                "(1) the currency in which funds from financing activities (debt and equity) are generated, (2) the currency in which receipts "
                "from operating activities are usually retained, and (3) whether foreign activities are carried out as an extension of the reporting "
                "entity rather than with significant autonomy. Solaria's capital budget and financing are strictly controlled and guaranteed "
                "by Northgate in the US, and its operational independence is constrained, pointing toward the USD as the functional currency.\n\n"
                "Distractor A is an environmental characteristic, not an IAS 21 functional currency indicator.\n\n"
                "Distractor C is irrelevant to the economic reality of the transactions."
            )
        },
        {
            "id": "L2-V16-Q5",
            "level": 2,
            "module": "m15-multinational",
            "topic": "Multinational Operations",
            "vignette_id": "V16",
            "vignette_title": "Global Manufacturing Corp: Functional Currency Determination & IAS 21 / ASC 830 Criteria",
            "vignette_text": v16_text,
            "los": "LOS 15.a: Distinguish between the local currency, functional currency, and presentation currency, and determine an entity's functional currency under IFRS and US GAAP.",
            "question": "Which statement correctly describes the relationship between local currency, functional currency, and presentation currency?",
            "options": {
                "A": "The functional currency can never match the presentation currency.",
                "B": "The presentation currency is always selected by local statutory regulators in each subsidiary's country.",
                "C": "The functional currency is determined by the underlying economic reality, while the presentation currency is chosen by management for financial reporting."
            },
            "answer": "C",
            "explanation": (
                "An entity's functional currency is determined by the primary economic environment in which it operates (economic substance). "
                "In contrast, the presentation currency (or reporting currency) is the currency in which the financial statements are presented, "
                "which is selected at the discretion of the reporting entity's management.\n\n"
                "Distractor A is incorrect because a foreign subsidiary's functional currency can indeed be the parent's presentation currency "
                "(as with Montrose Ltd).\n\n"
                "Distractor B is incorrect because local statutory authorities require statutory filings in local currency, but consolidated "
                "presentation currency is chosen by corporate management."
            )
        },
        {
            "id": "L2-V16-Q6",
            "level": 2,
            "module": "m15-multinational",
            "topic": "Multinational Operations",
            "vignette_id": "V16",
            "vignette_title": "Global Manufacturing Corp: Functional Currency Determination & IAS 21 / ASC 830 Criteria",
            "vignette_text": v16_text,
            "los": "LOS 15.a: Distinguish between the local currency, functional currency, and presentation currency, and determine an entity's functional currency under IFRS and US GAAP.",
            "question": "How does IAS 21 differ from US GAAP (ASC 830) regarding the determination of an entity's functional currency?",
            "options": {
                "A": "IAS 21 mandates an explicit hierarchy where primary indicators take precedence over secondary indicators, whereas ASC 830 lists indicators without a hierarchical order.",
                "B": "ASC 830 requires primary indicators to be satisfied before looking at secondary indicators, whereas IAS 21 allows equal weighting.",
                "C": "IAS 21 mandates that the functional currency must always equal the currency of the parent entity."
            },
            "answer": "A",
            "explanation": (
                "Under IAS 21, there is an explicit hierarchy: primary indicators (sales price influences, labor/material costs) must be evaluated first. "
                "Secondary indicators (financing currency, cash flow retention, degree of autonomy) are considered only if primary indicators are mixed "
                "or inconclusive. Under US GAAP (ASC 830), six economic factors (cash flows, sales prices, sales market, expenses, financing, intercompany "
                "transactions) are listed as factors to consider without an explicit hierarchical priority.\n\n"
                "Distractor B is inverted.\n\n"
                "Distractor C is false; IAS 21 emphasizes the local operational environment."
            )
        }
    ]
    vignettes.append((v16_text, v16_questions))

    # =========================================================================
    # VIGNETTE 17: Current Rate Method Translation & Cumulative Translation Adjustment
    # =========================================================================
    v17_text = (
        "NordVest Retail ASA is a wholly owned Norwegian subsidiary of Apex Global Brands Inc., "
        "a US-based retailer that reports in US dollars (USD). NordVest's functional currency is the "
        "Norwegian Krone (NOK). Accordingly, Apex translates NordVest's financial statements into USD "
        "using the Current Rate Method.\n\n"
        "Elena Vance examines NordVest's financial statements for the fiscal year ended 31 December Year 2.\n\n"
        "Exhibit 1: NordVest Financial Statements (in millions of NOK)\n"
        "Balance Sheet at 31 Dec Year 2:\n"
        "Cash and cash equivalents: 40 NOK\n"
        "Accounts receivable: 80 NOK\n"
        "Inventory: 120 NOK\n"
        "Net property, plant & equipment (PPE): 360 NOK\n"
        "Total Assets: 600 NOK\n\n"
        "Accounts payable: 60 NOK\n"
        "Long-term bank debt: 240 NOK\n"
        "Common stock (issued Year 0): 100 NOK\n"
        "Retained earnings at 31 Dec Year 1: 120 NOK\n"
        "Year 2 Net income: 100 NOK\n"
        "Less: Dividends declared and paid in Year 2: (20 NOK)\n"
        "Ending Retained earnings at 31 Dec Year 2: 200 NOK\n"
        "Total Liabilities and Shareholders' Equity: 600 NOK\n\n"
        "Income Statement for Year 2 ended 31 Dec:\n"
        "Revenue: 500 NOK\n"
        "Cost of goods sold (COGS): 300 NOK\n"
        "Gross profit: 200 NOK\n"
        "Depreciation expense: 40 NOK\n"
        "SG&A expenses: 60 NOK\n"
        "Operating income: 100 NOK\n"
        "Taxes (0% simplified): 0 NOK\n"
        "Net income: 100 NOK\n\n"
        "Exhibit 2: Relevant Foreign Exchange Rates (USD per 1 NOK)\n"
        "- Historical rate at common stock issuance (Year 0): 0.1000 USD/NOK\n"
        "- Historical rate when existing PPE was acquired: 0.1100 USD/NOK\n"
        "- Ending exchange rate at 31 Dec Year 1: 0.1200 USD/NOK\n"
        "- Cumulative translated retained earnings at 31 Dec Year 1: 13.20 million USD\n"
        "- Weighted average exchange rate for Year 2: 0.1250 USD/NOK\n"
        "- Exchange rate when Year 2 dividends were declared and paid: 0.1280 USD/NOK\n"
        "- Current ending exchange rate at 31 Dec Year 2: 0.1300 USD/NOK\n\n"
        "Apex translates revenues and expenses at the weighted average rate for the year. "
        "Dividends are translated at the rate on the date of declaration."
    )

    v17_questions = [
        {
            "id": "L2-V17-Q1",
            "level": 2,
            "module": "m15-multinational",
            "topic": "Multinational Operations",
            "vignette_id": "V17",
            "vignette_title": "Nordic Retailers AS: Current Rate Method Translation & Cumulative Translation Adjustment (CTA)",
            "vignette_text": v17_text,
            "los": "LOS 15.c: Calculate the translation effects, and evaluate the translation of a subsidiary's balance sheet and income statement using the current rate method.",
            "question": "Under the Current Rate Method, NordVest's translated Year 2 Gross Profit in Apex's consolidated income statement is closest to:",
            "options": {
                "A": "25.00 million USD.",
                "B": "26.00 million USD.",
                "C": "22.00 million USD."
            },
            "answer": "A",
            "explanation": (
                "Under the Current Rate Method, all income statement items (including Revenue and Cost of Goods Sold) "
                "are translated at the weighted average exchange rate prevailing during the reporting period.\n\n"
                "Year 2 Gross Profit = 200 million NOK.\n"
                "Weighted average exchange rate = 0.1250 USD/NOK.\n"
                "Translated Gross Profit = $200 \\times 0.1250 = 25.00$ million USD.\n\n"
                "Distractor B is based on translating gross profit at the ending rate: $200 \\times 0.1300 = 26.00$ million USD.\n"
                "Distractor C is based on the historical PPE acquisition rate: $200 \\times 0.1100 = 22.00$ million USD."
            )
        },
        {
            "id": "L2-V17-Q2",
            "level": 2,
            "module": "m15-multinational",
            "topic": "Multinational Operations",
            "vignette_id": "V17",
            "vignette_title": "Nordic Retailers AS: Current Rate Method Translation & Cumulative Translation Adjustment (CTA)",
            "vignette_text": v17_text,
            "los": "LOS 15.c: Calculate the translation effects, and evaluate the translation of a subsidiary's balance sheet and income statement using the current rate method.",
            "question": "Under the Current Rate Method, NordVest's total assets translated into Apex's consolidated balance sheet at 31 December Year 2 are closest to:",
            "options": {
                "A": "75.00 million USD.",
                "B": "78.00 million USD.",
                "C": "69.60 million USD."
            },
            "answer": "B",
            "explanation": (
                "Under the Current Rate Method, all assets (both monetary and non-monetary, including cash, receivables, "
                "inventory, and net PPE) are translated at the current exchange rate at the balance sheet date.\n\n"
                "Total Assets = 600 million NOK.\n"
                "Current exchange rate at 31 Dec Year 2 = 0.1300 USD/NOK.\n"
                "Translated Total Assets = $600 \\times 0.1300 = 78.00$ million USD.\n\n"
                "Distractor A incorrectly uses the weighted average rate: $600 \\times 0.1250 = 75.00$ million USD.\n"
                "Distractor C incorrectly translates PPE at historical rate and current assets at ending rate: "
                "$(240 \\times 0.1300) + (360 \\times 0.1100) = 31.20 + 39.60 = 70.80$ million USD."
            )
        },
        {
            "id": "L2-V17-Q3",
            "level": 2,
            "module": "m15-multinational",
            "topic": "Multinational Operations",
            "vignette_id": "V17",
            "vignette_title": "Nordic Retailers AS: Current Rate Method Translation & Cumulative Translation Adjustment (CTA)",
            "vignette_text": v17_text,
            "los": "LOS 15.c: Calculate the translation effects, and evaluate the translation of a subsidiary's balance sheet and income statement using the current rate method.",
            "question": "NordVest's translated ending Retained Earnings at 31 December Year 2 is closest to:",
            "options": {
                "A": "23.14 million USD.",
                "B": "25.00 million USD.",
                "C": "26.00 million USD."
            },
            "answer": "A",
            "explanation": (
                "Under the Current Rate Method, ending Retained Earnings is calculated cumulatively as:\n"
                "$\\text{Ending Retained Earnings} = \\text{Beginning Retained Earnings} + \\text{Translated Net Income} - \\text{Translated Dividends}$\n\n"
                "- Beginning Retained Earnings (at 31 Dec Year 1) = 13.20 million USD (given).\n"
                "- Translated Year 2 Net Income = $100 \\text{ million NOK} \\times 0.1250 = 12.50$ million USD.\n"
                "- Translated Dividends = $20 \\text{ million NOK} \\times 0.1280 = 2.56$ million USD.\n"
                "- Ending Retained Earnings = $13.20 + 12.50 - 2.56 = 23.14$ million USD.\n\n"
                "Distractor B is $200 \\text{ million NOK} \\times 0.1250 = 25.00$ million USD (multiplying ending RE by average rate).\n"
                "Distractor C is $200 \\text{ million NOK} \\times 0.1300 = 26.00$ million USD (multiplying ending RE by ending rate)."
            )
        },
        {
            "id": "L2-V17-Q4",
            "level": 2,
            "module": "m15-multinational",
            "topic": "Multinational Operations",
            "vignette_id": "V17",
            "vignette_title": "Nordic Retailers AS: Current Rate Method Translation & Cumulative Translation Adjustment (CTA)",
            "vignette_text": v17_text,
            "los": "LOS 15.c: Calculate the translation effects, and evaluate the translation of a subsidiary's balance sheet and income statement using the current rate method.",
            "question": "The Cumulative Translation Adjustment (CTA) reported in shareholders' equity on Apex's consolidated balance sheet at 31 December Year 2 is closest to:",
            "options": {
                "A": "3.86 million USD.",
                "B": "5.86 million USD.",
                "C": "7.86 million USD."
            },
            "answer": "B",
            "explanation": (
                "The Cumulative Translation Adjustment (CTA) is the balancing plug in equity required to make total assets equal "
                "total liabilities plus shareholders' equity.\n\n"
                "1. Translated Total Assets = $600 \\text{ NOK} \\times 0.1300 = 78.00$ million USD.\n"
                "2. Translated Total Liabilities = $300 \\text{ NOK} \\times 0.1300 = 39.00$ million USD.\n"
                "3. Translated Common Stock = $100 \\text{ NOK} \\times 0.1000 \\text{ (historical rate)} = 10.00$ million USD.\n"
                "4. Translated Retained Earnings = 23.14 million USD (from previous question).\n"
                "5. Liabilities plus Equity before CTA = $39.00 + 10.00 + 23.14 = 72.14$ million USD.\n"
                "6. CTA = $\\text{Total Assets} - (\\text{Liabilities} + \\text{Common Stock} + \\text{Retained Earnings})$\n"
                "CTA = $78.00 - 72.14 = 5.86$ million USD.\n\n"
                "Distractor A and C result from miscalculating retained earnings or using ending exchange rates on common stock."
            )
        },
        {
            "id": "L2-V17-Q5",
            "level": 2,
            "module": "m15-multinational",
            "topic": "Multinational Operations",
            "vignette_id": "V17",
            "vignette_title": "Nordic Retailers AS: Current Rate Method Translation & Cumulative Translation Adjustment (CTA)",
            "vignette_text": v17_text,
            "los": "LOS 15.b: Compare the current rate method and the temporal method, evaluate how each method affects the parent company's balance sheet and income statement.",
            "question": "Under the Current Rate Method, what is Apex's net balance sheet foreign exchange exposure to NordVest?",
            "options": {
                "A": "A net asset exposure of 300 million NOK.",
                "B": "A net monetary liability exposure of 140 million NOK.",
                "C": "A net monetary asset exposure of 60 million NOK."
            },
            "answer": "A",
            "explanation": (
                "Under the Current Rate Method, all assets and all liabilities are translated at the current exchange rate. "
                "Consequently, the net balance sheet foreign exchange exposure equals the subsidiary's Net Assets (Total Assets - Total Liabilities "
                "= Shareholders' Equity). Here, Net Assets = $600 - 300 = 300$ million NOK.\n\n"
                "Because foreign currency assets exceed foreign currency liabilities, Apex has a net asset exposure. "
                "When the foreign currency (NOK) appreciates against the reporting currency (USD), the net asset exposure generates "
                "a positive translation adjustment in OCI.\n\n"
                "Distractor B and C reflect monetary balance sheet positions, which determine foreign exchange exposure under the "
                "Temporal Method, not the Current Rate Method."
            )
        },
        {
            "id": "L2-V17-Q6",
            "level": 2,
            "module": "m15-multinational",
            "topic": "Multinational Operations",
            "vignette_id": "V17",
            "vignette_title": "Nordic Retailers AS: Current Rate Method Translation & Cumulative Translation Adjustment (CTA)",
            "vignette_text": v17_text,
            "los": "LOS 15.d: Analyze the effect of alternative translation methods and exchange rate changes on financial ratios.",
            "question": "Because the Norwegian Krone appreciated during Year 2, what is the effect on Apex's consolidated financial statements under the Current Rate Method?",
            "options": {
                "A": "Consolidated Net Income increases due to an unrealized foreign currency translation gain.",
                "B": "Consolidated OCI increases via a positive Cumulative Translation Adjustment, while pure balance sheet ratios in NOK are preserved in USD.",
                "C": "Total Assets decrease in USD terms because of currency translation losses."
            },
            "answer": "B",
            "explanation": (
                "When a foreign subsidiary's functional currency appreciates against the presentation currency under the Current Rate Method, "
                "the net asset exposure yields a positive translation adjustment recognized in Other Comprehensive Income (OCI) and accumulated "
                "in equity as CTA. Crucially, pure balance sheet ratios (e.g., Current Ratio, Debt-to-Assets) calculated from the translated "
                "statements in USD are identical to those calculated from the local currency (NOK) statements because all assets and liabilities "
                "are multiplied by the exact same ending exchange rate ($0.1300$).\n\n"
                "Distractor A is incorrect because translation gains under the Current Rate Method bypass Net Income and flow into OCI.\n\n"
                "Distractor C is incorrect because an appreciating foreign currency increases translated asset values in USD."
            )
        }
    ]
    vignettes.append((v17_text, v17_questions))

    # =========================================================================
    # VIGNETTE 18: Temporal Method / Remeasurement Mechanics
    # =========================================================================
    v18_text = (
        "Zenith Precision AG is a Swiss manufacturing subsidiary of US-based Meridian Instruments Inc. "
        "Meridian's presentation currency is the US dollar (USD). Zenith maintains its local accounting records "
        "in Swiss francs (CHF). However, Zenith functions as a centralized precision engineering hub whose "
        "strategic decisions, principal product pricing, and corporate financing are directed by Meridian in USD. "
        "Consequently, Zenith's functional currency is determined to be the US dollar (USD).\n\n"
        "Because Zenith's functional currency (USD) differs from its local record-keeping currency (CHF), "
        "Meridian remeasures Zenith's financial statements into USD using the Temporal Method.\n\n"
        "Exhibit 1: Zenith Balance Sheet at 31 December Year 2 (in millions of CHF)\n"
        "Cash: 30 CHF\n"
        "Accounts receivable: 50 CHF\n"
        "Inventory (FIFO): 70 CHF\n"
        "Net property, plant & equipment: 150 CHF\n"
        "Total Assets: 300 CHF\n\n"
        "Accounts payable: 40 CHF\n"
        "Long-term bank debt: 120 CHF\n"
        "Common stock: 80 CHF\n"
        "Retained earnings at 31 Dec Year 2: 60 CHF\n"
        "Total Liabilities and Shareholders' Equity: 300 CHF\n\n"
        "Exhibit 2: Inventory & Operating Data for Year 2 (in millions of CHF)\n"
        "- Beginning inventory (acquired evenly in Q4 Year 1): 50 CHF\n"
        "- Purchases throughout Year 2: 180 CHF\n"
        "- Ending inventory at 31 Dec Year 2 (acquired in Q4 Year 2): 70 CHF\n"
        "- Cost of goods sold (COGS) under FIFO: $50 + 180 - 70 = 160$ CHF\n"
        "- Depreciation expense on PPE for Year 2: 15 CHF\n\n"
        "Exhibit 3: Relevant Exchange Rates (USD per 1 CHF)\n"
        "- Historical rate at common stock issuance: 1.00 USD/CHF\n"
        "- Historical rate when existing PPE was acquired: 1.02 USD/CHF\n"
        "- Historical rate for beginning inventory (Q4 Year 1): 1.05 USD/CHF\n"
        "- Weighted average exchange rate for Year 2 purchases: 1.10 USD/CHF\n"
        "- Historical rate for ending inventory (Q4 Year 2): 1.12 USD/CHF\n"
        "- Weighted average exchange rate for Year 2: 1.08 USD/CHF\n"
        "- Current ending exchange rate at 31 Dec Year 2: 1.15 USD/CHF"
    )

    v18_questions = [
        {
            "id": "L2-V18-Q1",
            "level": 2,
            "module": "m15-multinational",
            "topic": "Multinational Operations",
            "vignette_id": "V18",
            "vignette_title": "Zenith Precision Ltd: Remeasurement Under the Temporal Method",
            "vignette_text": v18_text,
            "los": "LOS 15.c: Calculate the translation effects, and evaluate the translation of a subsidiary's balance sheet and income statement using the temporal method.",
            "question": "Under the Temporal Method, Zenith's remeasured Ending Inventory and Cost of Goods Sold (COGS) in USD for Year 2 are closest to:",
            "options": {
                "A": "Ending Inventory: 78.40 million USD; COGS: 172.10 million USD.",
                "B": "Ending Inventory: 80.50 million USD; COGS: 172.80 million USD.",
                "C": "Ending Inventory: 75.60 million USD; COGS: 176.00 million USD."
            },
            "answer": "A",
            "explanation": (
                "Under the Temporal Method, non-monetary assets carried at historical cost (such as inventory under FIFO) "
                "are remeasured using the historical exchange rates prevailing when the assets were acquired.\n\n"
                "1. Ending Inventory remeasured:\n"
                "Ending inventory (70 million CHF) was acquired in Q4 Year 2 when the exchange rate was 1.12 USD/CHF.\n"
                "$\\text{Remeasured Ending Inventory} = 70 \\times 1.12 = 78.40$ million USD.\n\n"
                "2. Cost of Goods Sold (COGS) under FIFO:\n"
                "$\\text{COGS} = \\text{Beginning Inventory} + \\text{Purchases} - \\text{Ending Inventory}$\n"
                "- Beginning inventory remeasured: $50 \\text{ CHF} \\times 1.05 = 52.50$ million USD.\n"
                "- Purchases remeasured: $180 \\text{ CHF} \\times 1.10 = 198.00$ million USD.\n"
                "- Remeasured COGS: $52.50 + 198.00 - 78.40 = 172.10$ million USD.\n\n"
                "Distractor B mistakenly uses the ending rate (1.15) for ending inventory: $70 \\times 1.15 = 80.50$ million USD, "
                "which is the Current Rate Method treatment."
            )
        },
        {
            "id": "L2-V18-Q2",
            "level": 2,
            "module": "m15-multinational",
            "topic": "Multinational Operations",
            "vignette_id": "V18",
            "vignette_title": "Zenith Precision Ltd: Remeasurement Under the Temporal Method",
            "vignette_text": v18_text,
            "los": "LOS 15.c: Calculate the translation effects, and evaluate the translation of a subsidiary's balance sheet and income statement using the temporal method.",
            "question": "Under the Temporal Method, Zenith's remeasured Net PPE at 31 Dec Year 2 and Year 2 Depreciation expense in USD are closest to:",
            "options": {
                "A": "Net PPE: 172.50 million USD; Depreciation: 16.20 million USD.",
                "B": "Net PPE: 153.00 million USD; Depreciation: 15.30 million USD.",
                "C": "Net PPE: 162.00 million USD; Depreciation: 17.25 million USD."
            },
            "answer": "B",
            "explanation": (
                "Under the Temporal Method, non-monetary fixed assets and related depreciation are remeasured at the "
                "historical exchange rates prevailing at the time the assets were acquired.\n\n"
                "- Historical rate for PPE = 1.02 USD/CHF.\n"
                "- Remeasured Net PPE = $150 \\text{ million CHF} \\times 1.02 = 153.00$ million USD.\n"
                "- Remeasured Depreciation expense = $15 \\text{ million CHF} \\times 1.02 = 15.30$ million USD.\n\n"
                "Distractor A uses the current ending rate (1.15) for PPE and average rate (1.08) for depreciation, "
                "which is the Current Rate Method treatment."
            )
        },
        {
            "id": "L2-V18-Q3",
            "level": 2,
            "module": "m15-multinational",
            "topic": "Multinational Operations",
            "vignette_id": "V18",
            "vignette_title": "Zenith Precision Ltd: Remeasurement Under the Temporal Method",
            "vignette_text": v18_text,
            "los": "LOS 15.c: Calculate the translation effects, and evaluate the translation of a subsidiary's balance sheet and income statement using the temporal method.",
            "question": "Which exchange rate should Meridian use to remeasure Zenith's Accounts Payable and Deferred Revenue liabilities under the Temporal Method?",
            "options": {
                "A": "Accounts Payable at the current exchange rate; Deferred Revenue at historical exchange rates.",
                "B": "Both Accounts Payable and Deferred Revenue at the current exchange rate.",
                "C": "Both Accounts Payable and Deferred Revenue at the weighted average exchange rate."
            },
            "answer": "A",
            "explanation": (
                "Under the Temporal Method, the balance sheet items are partitioned into monetary and non-monetary items:\n"
                "- Monetary assets and liabilities represent cash or claims/obligations to pay a fixed amount of currency in the future. "
                "Accounts payable is a monetary liability and is therefore remeasured at the current exchange rate at the balance sheet date.\n"
                "- Deferred revenue is a non-monetary liability (representing an obligation to deliver goods or services in the future, "
                "not to refund a fixed amount of cash). Therefore, deferred revenue is remeasured at the historical exchange rate on the date "
                "the cash advance was received.\n\n"
                "Distractor B incorrectly treats deferred revenue as monetary.\n"
                "Distractor C incorrectly applies average rates to balance sheet liabilities."
            )
        },
        {
            "id": "L2-V18-Q4",
            "level": 2,
            "module": "m15-multinational",
            "topic": "Multinational Operations",
            "vignette_id": "V18",
            "vignette_title": "Zenith Precision Ltd: Remeasurement Under the Temporal Method",
            "vignette_text": v18_text,
            "los": "LOS 15.b: Compare the current rate method and the temporal method, evaluate how each method affects the parent company's balance sheet and income statement.",
            "question": "What is Zenith's net balance sheet foreign exchange exposure under the Temporal Method?",
            "options": {
                "A": "A net asset exposure of 140 million CHF.",
                "B": "A net monetary liability exposure of 80 million CHF.",
                "C": "A net monetary asset exposure of 30 million CHF."
            },
            "answer": "B",
            "explanation": (
                "Under the Temporal Method, only monetary assets and monetary liabilities are exposed to foreign exchange rate risk "
                "because non-monetary items are remeasured at historical rates.\n\n"
                "- Monetary Assets = Cash (30 CHF) + Accounts Receivable (50 CHF) = 80 million CHF.\n"
                "- Monetary Liabilities = Accounts Payable (40 CHF) + Long-term Debt (120 CHF) = 160 million CHF.\n"
                "- Net Monetary Position = $\\text{Monetary Assets} - \\text{Monetary Liabilities} = 80 - 160 = -80$ million CHF.\n\n"
                "Because monetary liabilities exceed monetary assets, Zenith has a Net Monetary Liability exposure of 80 million CHF.\n\n"
                "Distractor A represents total net assets (equity), which is the exposure under the Current Rate Method, not the Temporal Method."
            )
        },
        {
            "id": "L2-V18-Q5",
            "level": 2,
            "module": "m15-multinational",
            "topic": "Multinational Operations",
            "vignette_id": "V18",
            "vignette_title": "Zenith Precision Ltd: Remeasurement Under the Temporal Method",
            "vignette_text": v18_text,
            "los": "LOS 15.b: Compare the current rate method and the temporal method, evaluate how each method affects the parent company's balance sheet and income statement.",
            "question": "Because the Swiss franc (CHF) appreciated during Year 2, what is the effect of Zenith's net monetary position on Meridian's consolidated income statement under the Temporal Method?",
            "options": {
                "A": "A remeasurement gain recognized in net income.",
                "B": "A remeasurement loss recognized in net income.",
                "C": "A positive cumulative translation adjustment recognized in OCI."
            },
            "answer": "B",
            "explanation": (
                "Under the Temporal Method, Zenith has a net monetary liability position ($-80$ million CHF). "
                "When a foreign currency strengthens/appreciates, liabilities denominated in that currency become more expensive "
                "to settle in terms of the reporting currency (USD). Holding net monetary liabilities in an appreciating foreign "
                "currency generates an unrealized foreign exchange remeasurement LOSS.\n\n"
                "Crucially, under the Temporal Method, this remeasurement loss is recognized directly in the consolidated "
                "Income Statement, reducing consolidated Net Income.\n\n"
                "Distractor A is incorrect because holding net liabilities in an appreciating currency yields a loss, not a gain.\n"
                "Distractor C describes the Current Rate Method (where translation gains go to OCI)."
            )
        },
        {
            "id": "L2-V18-Q6",
            "level": 2,
            "module": "m15-multinational",
            "topic": "Multinational Operations",
            "vignette_id": "V18",
            "vignette_title": "Zenith Precision Ltd: Remeasurement Under the Temporal Method",
            "vignette_text": v18_text,
            "los": "LOS 15.b: Compare the current rate method and the temporal method, evaluate how each method affects the parent company's balance sheet and income statement.",
            "question": "Which of the following correctly summarizes the accounting location of translation gains and losses under the Temporal Method versus the Current Rate Method?",
            "options": {
                "A": "Temporal: Consolidated Net Income; Current Rate: Balance Sheet Equity (OCI / CTA).",
                "B": "Temporal: Balance Sheet Equity (OCI / CTA); Current Rate: Consolidated Net Income.",
                "C": "Both methods report translation gains and losses directly in Operating Income."
            },
            "answer": "A",
            "explanation": (
                "Under the Temporal Method (remeasurement), foreign exchange gains and losses are recognized directly "
                "in the consolidated Income Statement, typically below operating income, affecting Net Income and EPS.\n\n"
                "Under the Current Rate Method (translation), translation gains and losses bypass the income statement completely "
                "and are accumulated in shareholders' equity under Other Comprehensive Income (OCI) as a Cumulative Translation Adjustment (CTA).\n\n"
                "Distractor B inverts the two standards. Distractor C is incorrect because Current Rate never flows through operating income."
            )
        }
    ]
    vignettes.append((v18_text, v18_questions))

    # =========================================================================
    # VIGNETTE 19: Direct Comparison of Current Rate and Temporal Methods
    # =========================================================================
    v19_text = (
        "Orion Technologies Inc. is a major US semiconductor equipment manufacturer reporting in USD. "
        "Orion owns 100% of SingTech Pte Ltd, a semiconductor manufacturing subsidiary located in Singapore. "
        "Orion's CFO is preparing a comparative analysis showing how SingTech's Year 2 financial statements "
        "would be presented under both the Current Rate Method (assuming SGD is the functional currency) "
        "and the Temporal Method (assuming USD is the functional currency).\n\n"
        "Exhibit 1: SingTech Summary Financial Statements (in millions of Singapore dollars, SGD)\n"
        "Balance Sheet at 31 Dec Year 2:\n"
        "Monetary assets (Cash + Receivables): 80 SGD\n"
        "Inventory (FIFO): 40 SGD\n"
        "Net Property, Plant & Equipment: 80 SGD\n"
        "Total Assets: 200 SGD\n\n"
        "Monetary liabilities (A/P + Debt): 120 SGD\n"
        "Common stock: 50 SGD\n"
        "Retained earnings: 30 SGD\n"
        "Total Liabilities and Equity: 200 SGD\n\n"
        "Income Statement for Year 2:\n"
        "Revenues: 100 SGD\n"
        "Cost of goods sold (COGS): 60 SGD\n"
        "Depreciation expense: 10 SGD\n"
        "SG&A expenses: 15 SGD\n"
        "Operating income: 15 SGD\n\n"
        "Exhibit 2: Foreign Exchange Rates (USD per 1 SGD)\n"
        "- Historical rate at stock issuance: 0.65 USD/SGD\n"
        "- Historical rate when existing PPE was acquired: 0.60 USD/SGD\n"
        "- Historical rate for ending inventory: 0.68 USD/SGD\n"
        "- Historical rate for COGS under FIFO: 0.66 USD/SGD\n"
        "- Weighted average exchange rate for Year 2: 0.70 USD/SGD\n"
        "- Ending exchange rate at 31 Dec Year 2: 0.75 USD/SGD\n\n"
        "Note: The Singapore dollar has appreciated steadily against the USD over the past several years."
    )

    v19_questions = [
        {
            "id": "L2-V19-Q1",
            "level": 2,
            "module": "m15-multinational",
            "topic": "Multinational Operations",
            "vignette_id": "V19",
            "vignette_title": "Orion Technologies Corp: Direct Comparison of Current Rate and Temporal Methods",
            "vignette_text": v19_text,
            "los": "LOS 15.b: Compare the current rate method and the temporal method, evaluate how each method affects the parent company's balance sheet and income statement.",
            "question": "Comparing the translated Gross Profit Margin (Gross Profit / Revenues) under both methods:",
            "options": {
                "A": "Gross profit margin is higher under the Temporal Method (34.0%) than under the Current Rate Method (40.0%).",
                "B": "Gross profit margin is higher under the Temporal Method (43.4%) than under the Current Rate Method (40.0%).",
                "C": "Gross profit margin is identical under both methods at 40.0%."
            },
            "answer": "B",
            "explanation": (
                "1. Under the Current Rate Method:\n"
                "- Revenues = $100 \\times 0.70 = 70.0$ million USD.\n"
                "- COGS = $60 \\times 0.70 = 42.0$ million USD.\n"
                "- Gross Profit = $70.0 - 42.0 = 28.0$ million USD.\n"
                "- Gross Profit Margin = $28.0 / 70.0 = 40.0\\%$.\n"
                "(Note: Under the Current Rate Method, gross profit margin is always identical to the local currency margin: $40 / 100 = 40.0\\%$).\n\n"
                "2. Under the Temporal Method:\n"
                "- Revenues = $100 \\times 0.70 = 70.0$ million USD (average rate).\n"
                "- COGS = $60 \\times 0.66 = 39.6$ million USD (historical rate).\n"
                "- Gross Profit = $70.0 - 39.6 = 30.4$ million USD.\n"
                "- Gross Profit Margin = $30.4 / 70.0 = 43.43\\%$.\n\n"
                "Because the foreign currency was appreciating, historical inventory costs were lower ($0.66$ vs $0.70$), "
                "leading to a lower translated COGS and a higher Gross Profit Margin under the Temporal Method."
            )
        },
        {
            "id": "L2-V19-Q2",
            "level": 2,
            "module": "m15-multinational",
            "topic": "Multinational Operations",
            "vignette_id": "V19",
            "vignette_title": "Orion Technologies Corp: Direct Comparison of Current Rate and Temporal Methods",
            "vignette_text": v19_text,
            "los": "LOS 15.b: Compare the current rate method and the temporal method, evaluate how each method affects the parent company's balance sheet and income statement.",
            "question": "SingTech's translated Depreciation expense in USD under the Temporal Method and Current Rate Method is:",
            "options": {
                "A": "Temporal: 6.0 million USD; Current Rate: 7.0 million USD.",
                "B": "Temporal: 7.5 million USD; Current Rate: 7.0 million USD.",
                "C": "Temporal: 7.0 million USD; Current Rate: 6.0 million USD."
            },
            "answer": "A",
            "explanation": (
                "- Under the Temporal Method, depreciation expense is remeasured at the historical exchange rate when the fixed assets "
                "were acquired ($0.60$ USD/SGD):\n"
                "$\\text{Depreciation} = 10 \\text{ SGD} \\times 0.60 = 6.0$ million USD.\n\n"
                "- Under the Current Rate Method, depreciation expense is translated at the weighted average exchange rate ($0.70$ USD/SGD):\n"
                "$\\text{Depreciation} = 10 \\text{ SGD} \\times 0.70 = 7.0$ million USD.\n\n"
                "Distractor B and C mix up the rates or use the ending rate ($0.75$)."
            )
        },
        {
            "id": "L2-V19-Q3",
            "level": 2,
            "module": "m15-multinational",
            "topic": "Multinational Operations",
            "vignette_id": "V19",
            "vignette_title": "Orion Technologies Corp: Direct Comparison of Current Rate and Temporal Methods",
            "vignette_text": v19_text,
            "los": "LOS 15.b: Compare the current rate method and the temporal method, evaluate how each method affects the parent company's balance sheet and income statement.",
            "question": "What are SingTech's net balance sheet foreign exchange exposures under the Current Rate Method and Temporal Method, respectively?",
            "options": {
                "A": "Current Rate: +80 million SGD; Temporal: -40 million SGD.",
                "B": "Current Rate: +200 million SGD; Temporal: +80 million SGD.",
                "C": "Current Rate: -40 million SGD; Temporal: +80 million SGD."
            },
            "answer": "A",
            "explanation": (
                "1. Under the Current Rate Method, exposure equals Net Assets:\n"
                "$\\text{Net Assets} = \\text{Total Assets} - \\text{Total Liabilities} = 200 - 120 = +80$ million SGD (Net Asset exposure).\n\n"
                "2. Under the Temporal Method, exposure equals Net Monetary Assets:\n"
                "$\\text{Net Monetary Assets} = \\text{Monetary Assets} - \\text{Monetary Liabilities} = 80 - 120 = -40$ million SGD (Net Monetary Liability exposure).\n\n"
                "Notice that the exposure has OPPOSITE signs under the two methods! SingTech has a positive exposure under the Current Rate "
                "Method, but a negative exposure under the Temporal Method."
            )
        },
        {
            "id": "L2-V19-Q4",
            "level": 2,
            "module": "m15-multinational",
            "topic": "Multinational Operations",
            "vignette_id": "V19",
            "vignette_title": "Orion Technologies Corp: Direct Comparison of Current Rate and Temporal Methods",
            "vignette_text": v19_text,
            "los": "LOS 15.b: Compare the current rate method and the temporal method, evaluate how each method affects the parent company's balance sheet and income statement.",
            "question": "SingTech's translated Total Assets at 31 Dec Year 2 under the Current Rate Method and Temporal Method are closest to:",
            "options": {
                "A": "Current Rate: 150.0 million USD; Temporal: 135.2 million USD.",
                "B": "Current Rate: 140.0 million USD; Temporal: 150.0 million USD.",
                "C": "Current Rate: 135.2 million USD; Temporal: 150.0 million USD."
            },
            "answer": "A",
            "explanation": (
                "1. Current Rate Method:\n"
                "All assets translated at current ending rate ($0.75$):\n"
                "$\\text{Total Assets} = 200 \\text{ SGD} \\times 0.75 = 150.0$ million USD.\n\n"
                "2. Temporal Method:\n"
                "- Monetary assets at ending rate ($0.75$): $80 \\times 0.75 = 60.0$ million USD.\n"
                "- Inventory at historical rate ($0.68$): $40 \\times 0.68 = 27.2$ million USD.\n"
                "- Net PPE at historical rate ($0.60$): $80 \\times 0.60 = 48.0$ million USD.\n"
                "- Total Assets = $60.0 + 27.2 + 48.0 = 135.2$ million USD.\n\n"
                "Because SGD has appreciated, translating non-monetary assets at historical rates results in lower total assets under the Temporal Method."
            )
        },
        {
            "id": "L2-V19-Q5",
            "level": 2,
            "module": "m15-multinational",
            "topic": "Multinational Operations",
            "vignette_id": "V19",
            "vignette_title": "Orion Technologies Corp: Direct Comparison of Current Rate and Temporal Methods",
            "vignette_text": v19_text,
            "los": "LOS 15.d: Analyze the effect of alternative translation methods and exchange rate changes on financial ratios.",
            "question": "If the Singapore dollar had depreciated during Year 2 instead of appreciating, what would be the direction of translation adjustments under both methods?",
            "options": {
                "A": "Current Rate: Positive CTA in OCI; Temporal: Remeasurement loss in Net Income.",
                "B": "Current Rate: Negative CTA in OCI; Temporal: Remeasurement gain in Net Income.",
                "C": "Current Rate: Negative CTA in OCI; Temporal: Remeasurement loss in Net Income."
            },
            "answer": "B",
            "explanation": (
                "1. Under the Current Rate Method: SingTech has a net asset exposure ($+80$ million SGD). When the foreign currency depreciates, "
                "holding net assets produces a negative translation adjustment (loss) accumulated in OCI (reducing equity CTA).\n\n"
                "2. Under the Temporal Method: SingTech has a net monetary liability position ($-40$ million SGD). When the foreign currency "
                "depreciates, obligations denominated in that currency become cheaper to satisfy in USD terms, resulting in an unrealized "
                "remeasurement GAIN recognized in consolidated Net Income.\n\n"
                "Distractor A and C fail to recognize the opposite effects generated by net asset vs net monetary liability positions."
            )
        },
        {
            "id": "L2-V19-Q6",
            "level": 2,
            "module": "m15-multinational",
            "topic": "Multinational Operations",
            "vignette_id": "V19",
            "vignette_title": "Orion Technologies Corp: Direct Comparison of Current Rate and Temporal Methods",
            "vignette_text": v19_text,
            "los": "LOS 15.d: Analyze the effect of alternative translation methods and exchange rate changes on financial ratios.",
            "question": "At 31 Dec Year 2, which method results in a higher Debt-to-Assets ratio (Total Monetary Liabilities / Total Assets) for SingTech?",
            "options": {
                "A": "The Current Rate Method.",
                "B": "The Temporal Method.",
                "C": "Both methods yield an identical Debt-to-Assets ratio."
            },
            "answer": "B",
            "explanation": (
                "Let's compute the Debt-to-Assets ratio under both methods:\n"
                "Under both methods, monetary liabilities are translated at the current ending rate ($0.75$):\n"
                "$\\text{Total Liabilities} = 120 \\times 0.75 = 90.0$ million USD.\n\n"
                "- Under the Current Rate Method:\n"
                "$\\text{Total Assets} = 150.0$ million USD.\n"
                "$\\text{Debt-to-Assets} = 90.0 / 150.0 = 60.0\\%$ (identical to local currency: $120 / 200 = 60.0\\%$).\n\n"
                "- Under the Temporal Method:\n"
                "$\\text{Total Assets} = 135.2$ million USD.\n"
                "$\\text{Debt-to-Assets} = 90.0 / 135.2 = 66.57\\%$.\n\n"
                "Because non-monetary assets are carried at lower historical rates under the Temporal Method during a period of foreign currency "
                "appreciation, the denominator (Total Assets) is smaller, resulting in a higher reported Debt-to-Assets ratio."
            )
        }
    ]
    vignettes.append((v19_text, v19_questions))

    # =========================================================================
    # VIGNETTE 20: Financial Ratio Effects under Appreciating Foreign Currency
    # =========================================================================
    v20_text = (
        "Helios Energy AG is a Munich-based renewable energy subsidiary of Apollo Global Power Inc., "
        "a US corporation reporting in USD. Helios's local and functional currency is the euro (EUR). "
        "Over the past fiscal year, the euro appreciated significantly against the US dollar.\n\n"
        "Exhibit 1: Exchange Rates (USD per 1 EUR)\n"
        "- Beginning exchange rate (1 Jan): 1.10 USD/EUR\n"
        "- Ending exchange rate (31 Dec): 1.30 USD/EUR\n"
        "- Weighted average exchange rate for the year: 1.20 USD/EUR\n\n"
        "Exhibit 2: Helios Summary Financial Data (in millions of EUR)\n"
        "Revenues: 600 EUR\n"
        "Cost of goods sold (COGS): 360 EUR\n"
        "Operating expenses: 120 EUR\n"
        "Operating income (EBIT): 120 EUR\n"
        "Net income: 90 EUR\n\n"
        "Current assets (Cash + A/R + Inventory): 200 EUR\n"
        "Fixed assets (Net PPE): 400 EUR\n"
        "Total Assets: 600 EUR\n"
        "Current liabilities: 100 EUR\n"
        "Long-term debt: 200 EUR\n"
        "Shareholders' equity (Beginning): 250 EUR\n"
        "Shareholders' equity (Ending, before translation adjustment): 300 EUR\n\n"
        "Apollo's senior analyst, Marcus Vance, is evaluating how the translation method impacts "
        "financial ratios and whether ratios calculated from the translated USD statements reflect "
        "the underlying operational performance in Germany."
    )

    v20_questions = [
        {
            "id": "L2-V20-Q1",
            "level": 2,
            "module": "m15-multinational",
            "topic": "Multinational Operations",
            "vignette_id": "V20",
            "vignette_title": "Helios Energy AG: Ratio Distortions Under a Strengthening Foreign Currency",
            "vignette_text": v20_text,
            "los": "LOS 15.d: Analyze the effect of alternative translation methods and exchange rate changes on financial ratios.",
            "question": "Under the Current Rate Method, how does the translated Current Ratio in USD compare to the original Current Ratio in EUR?",
            "options": {
                "A": "The translated Current Ratio is identical to the local currency Current Ratio.",
                "B": "The translated Current Ratio is higher because the ending exchange rate exceeds the average exchange rate.",
                "C": "The translated Current Ratio is lower because current assets include inventory translated at historical rates."
            },
            "answer": "A",
            "explanation": (
                "Under the Current Rate Method, pure balance sheet ratios (such as the Current Ratio, Quick Ratio, Debt-to-Equity, "
                "and Debt-to-Assets) are perfectly preserved. All current assets and current liabilities are translated at the exact same "
                "current exchange rate at the balance sheet date ($1.30$ USD/EUR).\n\n"
                "$\\text{Current Ratio (EUR)} = 200 / 100 = 2.00$.\n"
                "$\\text{Current Ratio (USD)} = (200 \\times 1.30) / (100 \\times 1.30) = 260 / 130 = 2.00$.\n\n"
                "Because the exchange rate cancels out in numerator and denominator, pure balance sheet ratios remain unchanged."
            )
        },
        {
            "id": "L2-V20-Q2",
            "level": 2,
            "module": "m15-multinational",
            "topic": "Multinational Operations",
            "vignette_id": "V20",
            "vignette_title": "Helios Energy AG: Ratio Distortions Under a Strengthening Foreign Currency",
            "vignette_text": v20_text,
            "los": "LOS 15.d: Analyze the effect of alternative translation methods and exchange rate changes on financial ratios.",
            "question": "Under the Current Rate Method, how does the translated Operating Profit Margin (EBIT / Revenues) in USD compare to the local currency margin?",
            "options": {
                "A": "It is higher because revenues are translated at the ending rate.",
                "B": "It is perfectly preserved because both EBIT and Revenues are translated at the weighted average exchange rate.",
                "C": "It is lower because operating expenses are translated at a higher exchange rate than revenues."
            },
            "answer": "B",
            "explanation": (
                "Pure income statement ratios (such as Gross Margin, Operating Margin, and Net Profit Margin) are perfectly preserved "
                "under the Current Rate Method because all revenue and expense line items are translated at the same weighted average "
                "exchange rate ($1.20$ USD/EUR).\n\n"
                "$\\text{Operating Margin (EUR)} = 120 / 600 = 20.0\\%$.\n"
                "$\\text{Operating Margin (USD)} = (120 \\times 1.20) / (600 \\times 1.20) = 144 / 720 = 20.0\\%$.\n\n"
                "Distractor A and C are incorrect because all income statement items share the same average exchange rate."
            )
        },
        {
            "id": "L2-V20-Q3",
            "level": 2,
            "module": "m15-multinational",
            "topic": "Multinational Operations",
            "vignette_id": "V20",
            "vignette_title": "Helios Energy AG: Ratio Distortions Under a Strengthening Foreign Currency",
            "vignette_text": v20_text,
            "los": "LOS 15.d: Analyze the effect of alternative translation methods and exchange rate changes on financial ratios.",
            "question": "Under the Current Rate Method, how does the translated Total Asset Turnover ratio (Revenues / Ending Total Assets) compare to the local currency ratio?",
            "options": {
                "A": "The translated Total Asset Turnover is lower than the local currency ratio.",
                "B": "The translated Total Asset Turnover is higher than the local currency ratio.",
                "C": "The translated Total Asset Turnover is identical to the local currency ratio."
            },
            "answer": "A",
            "explanation": (
                "Total Asset Turnover is a 'mixed ratio' because its numerator comes from the income statement (translated at average rate, "
                "$1.20$) while its denominator comes from the ending balance sheet (translated at ending rate, $1.30$).\n\n"
                "- In EUR: $\\text{Asset Turnover} = 600 / 600 = 1.00$.\n"
                "- In USD: $\\text{Revenues} = 600 \\times 1.20 = 720$ million USD.\n"
                "- In USD: $\\text{Ending Assets} = 600 \\times 1.30 = 780$ million USD.\n"
                "- In USD: $\\text{Asset Turnover} = 720 / 780 = 0.923$.\n\n"
                "Because the foreign currency appreciated over the year, the ending rate ($1.30$) is greater than the average rate ($1.20$). "
                "Thus, the denominator is expanded by a larger factor than the numerator, resulting in a translated ratio that is LOWER "
                "than the original local currency ratio."
            )
        },
        {
            "id": "L2-V20-Q4",
            "level": 2,
            "module": "m15-multinational",
            "topic": "Multinational Operations",
            "vignette_id": "V20",
            "vignette_title": "Helios Energy AG: Ratio Distortions Under a Strengthening Foreign Currency",
            "vignette_text": v20_text,
            "los": "LOS 15.d: Analyze the effect of alternative translation methods and exchange rate changes on financial ratios.",
            "question": "If Helios had been remeasured using the Temporal Method instead, how would the Current Ratio compare to the local currency ratio?",
            "options": {
                "A": "It would be preserved identically at 2.00.",
                "B": "It would be altered and generally lower because inventory is remeasured at historical rates while current liabilities are at the higher ending rate.",
                "C": "It would be higher because all monetary assets are translated at the average exchange rate."
            },
            "answer": "B",
            "explanation": (
                "Under the Temporal Method, the Current Ratio is NOT preserved. Current liabilities and monetary current assets (cash, receivables) "
                "are remeasured at the current ending exchange rate ($1.30$), but inventory is a non-monetary asset carried at historical cost, "
                "remeasured at lower historical exchange rates ($1.10$ - $1.20$). Consequently, during a period of foreign currency appreciation, "
                "inventory in the numerator is remeasured at an older, lower rate while current liabilities in the denominator are remeasured "
                "at the higher ending rate, depressing the Current Ratio relative to the local currency ratio."
            )
        },
        {
            "id": "L2-V20-Q5",
            "level": 2,
            "module": "m15-multinational",
            "topic": "Multinational Operations",
            "vignette_id": "V20",
            "vignette_title": "Helios Energy AG: Ratio Distortions Under a Strengthening Foreign Currency",
            "vignette_text": v20_text,
            "los": "LOS 15.d: Analyze the effect of alternative translation methods and exchange rate changes on financial ratios.",
            "question": "Under the Current Rate Method, which of the following general rules governs ratio preservation?",
            "options": {
                "A": "All financial ratios are perfectly preserved without exception.",
                "B": "Pure balance sheet and pure income statement ratios are preserved; mixed ratios combining income statement and balance sheet items are distorted.",
                "C": "Mixed ratios are preserved, but pure balance sheet ratios are distorted."
            },
            "answer": "B",
            "explanation": (
                "Under the Current Rate Method:\n"
                "1. Pure balance sheet ratios (e.g. Current Ratio, Quick Ratio, Debt-to-Equity) are preserved because both numerator and denominator "
                "are translated at the current ending rate ($S_t$).\n"
                "2. Pure income statement ratios (e.g. Gross Margin, Operating Margin, Net Margin) are preserved because both numerator and "
                "denominator are translated at the weighted average rate ($S_{avg}$).\n"
                "3. Mixed ratios (e.g. ROA, ROE, Asset Turnover, Receivables Turnover) combine an income statement item ($S_{avg}$) and a balance "
                "sheet item ($S_t$ or historical equity), so the exchange rates do NOT cancel out, distorting the translated ratio."
            )
        },
        {
            "id": "L2-V20-Q6",
            "level": 2,
            "module": "m15-multinational",
            "topic": "Multinational Operations",
            "vignette_id": "V20",
            "vignette_title": "Helios Energy AG: Ratio Distortions Under a Strengthening Foreign Currency",
            "vignette_text": v20_text,
            "los": "LOS 15.d: Analyze the effect of alternative translation methods and exchange rate changes on financial ratios.",
            "question": "Under the Temporal Method, how is Fixed Asset Turnover (Revenues / Net PPE) distorted when the foreign currency is appreciating?",
            "options": {
                "A": "Translated Fixed Asset Turnover is higher than the local currency ratio because revenues (average rate) exceed PPE (historical rate).",
                "B": "Translated Fixed Asset Turnover is lower than the local currency ratio because PPE is at the ending rate.",
                "C": "Translated Fixed Asset Turnover is preserved identically."
            },
            "answer": "A",
            "explanation": (
                "Under the Temporal Method, Net PPE is remeasured at the historical exchange rate prevailing when the fixed assets were acquired "
                "(which is lower than both the average and ending rate during a period of foreign currency appreciation). Meanwhile, Revenues are "
                "remeasured at the higher weighted average exchange rate.\n\n"
                "Because the numerator (Revenues at $S_{avg}$) is scaled up by a larger exchange rate than the denominator (PPE at $S_{hist}$), "
                "the translated Fixed Asset Turnover is HIGHER than the original local currency ratio."
            )
        }
    ]
    vignettes.append((v20_text, v20_questions))

    # =========================================================================
    # VIGNETTE 21: Financial Ratio Effects under Depreciating Foreign Currency
    # =========================================================================
    v21_text = (
        "Astra Minerals SA is a manganese mining operation based in South Africa, wholly owned by "
        "Highland Resources PLC, a UK mining group reporting in British pounds (GBP). "
        "Astra's local and functional currency is the South African Rand (ZAR). Over the past fiscal year, "
        "the South African Rand depreciated steadily against the British pound.\n\n"
        "Exhibit 1: Exchange Rates (GBP per 1 ZAR)\n"
        "- Beginning exchange rate (1 Jan): 0.055 GBP/ZAR\n"
        "- Weighted average exchange rate for Year 1: 0.048 GBP/ZAR\n"
        "- Ending exchange rate (31 Dec): 0.040 GBP/ZAR\n\n"
        "Exhibit 2: Astra Minerals Year 1 Financial Statements (in millions of ZAR)\n"
        "Revenue: 1,000 ZAR\n"
        "Cost of goods sold (FIFO): 600 ZAR\n"
        "Operating expenses: 200 ZAR\n"
        "Operating income (EBIT): 200 ZAR\n"
        "Interest expense: 50 ZAR\n"
        "Net income: 150 ZAR\n\n"
        "Current assets: 400 ZAR\n"
        "Net fixed assets: 800 ZAR\n"
        "Total Assets: 1,200 ZAR\n"
        "Current liabilities: 200 ZAR\n"
        "Long-term debt: 400 ZAR\n"
        "Common stock: 300 ZAR\n"
        "Ending retained earnings: 300 ZAR\n"
        "Total Liabilities and Equity: 1,200 ZAR\n\n"
        "Highland's treasury analyst, Tariq Modise, is evaluating the effects of ZAR depreciation on Astra's "
        "translated profitability, leverage, and turnover ratios."
    )

    v21_questions = [
        {
            "id": "L2-V21-Q1",
            "level": 2,
            "module": "m15-multinational",
            "topic": "Multinational Operations",
            "vignette_id": "V21",
            "vignette_title": "Astra Minerals SA: Ratio Distortions Under a Weakening Foreign Currency",
            "vignette_text": v21_text,
            "los": "LOS 15.d: Analyze the effect of alternative translation methods and exchange rate changes on financial ratios.",
            "question": "Under the Current Rate Method, how does the translated Interest Coverage ratio (EBIT / Interest Expense) in GBP compare to the ratio in ZAR?",
            "options": {
                "A": "It is identical to the local currency ratio at 4.00.",
                "B": "It is higher than 4.00 because of the declining exchange rate.",
                "C": "It is lower than 4.00 because interest expense is translated at the ending rate."
            },
            "answer": "A",
            "explanation": (
                "Interest Coverage is a pure income statement ratio: $\\text{EBIT} / \\text{Interest Expense} = 200 / 50 = 4.00$.\n"
                "Under the Current Rate Method, both EBIT and Interest Expense are translated at the weighted average exchange rate "
                "($0.048$ GBP/ZAR):\n"
                "$\\text{EBIT in GBP} = 200 \\times 0.048 = 9.60$ million GBP.\n"
                "$\\text{Interest Expense in GBP} = 50 \\times 0.048 = 2.40$ million GBP.\n"
                "$\\text{Interest Coverage} = 9.60 / 2.40 = 4.00$.\n\n"
                "Because both items are translated at the identical exchange rate, pure income statement ratios are perfectly preserved."
            )
        },
        {
            "id": "L2-V21-Q2",
            "level": 2,
            "module": "m15-multinational",
            "topic": "Multinational Operations",
            "vignette_id": "V21",
            "vignette_title": "Astra Minerals SA: Ratio Distortions Under a Weakening Foreign Currency",
            "vignette_text": v21_text,
            "los": "LOS 15.d: Analyze the effect of alternative translation methods and exchange rate changes on financial ratios.",
            "question": "Under the Current Rate Method, how does the translated Total Asset Turnover ratio (Revenue / Ending Total Assets) compare to the local currency ratio?",
            "options": {
                "A": "The translated Total Asset Turnover is lower than the local currency ratio.",
                "B": "The translated Total Asset Turnover is higher than the local currency ratio.",
                "C": "The translated Total Asset Turnover is identical to the local currency ratio."
            },
            "answer": "B",
            "explanation": (
                "Total Asset Turnover is a mixed ratio:\n"
                "- In local currency (ZAR): $\\text{Asset Turnover} = 1,000 / 1,200 = 0.833$.\n"
                "- In translated GBP:\n"
                "  Revenue = $1,000 \\times 0.048 \\text{ (average rate)} = 48.0$ million GBP.\n"
                "  Ending Total Assets = $1,200 \\times 0.040 \\text{ (ending rate)} = 48.0$ million GBP.\n"
                "  Translated Asset Turnover = $48.0 / 48.0 = 1.000$.\n\n"
                "Because the foreign currency depreciated, the average rate ($0.048$) is higher than the ending rate ($0.040$). "
                "Consequently, the numerator (Revenue) is multiplied by a larger exchange rate than the denominator (Assets), "
                "making the translated Asset Turnover HIGHER than the original local currency ratio."
            )
        },
        {
            "id": "L2-V21-Q3",
            "level": 2,
            "module": "m15-multinational",
            "topic": "Multinational Operations",
            "vignette_id": "V21",
            "vignette_title": "Astra Minerals SA: Ratio Distortions Under a Weakening Foreign Currency",
            "vignette_text": v21_text,
            "los": "LOS 15.d: Analyze the effect of alternative translation methods and exchange rate changes on financial ratios.",
            "question": "Under the Current Rate Method, what is the impact of ZAR depreciation on Highland's consolidated equity and Cumulative Translation Adjustment (CTA)?",
            "options": {
                "A": "CTA increases, expanding consolidated equity.",
                "B": "CTA becomes more negative, reducing consolidated shareholders' equity.",
                "C": "There is no impact on CTA because translation gains/losses flow through net income."
            },
            "answer": "B",
            "explanation": (
                "Under the Current Rate Method, Astra has a net asset foreign exchange exposure (Total Assets 1,200 ZAR - Total Liabilities 600 ZAR "
                "= +600 million ZAR). When a foreign currency depreciates, translating positive net assets at declining exchange rates produces "
                "an unrealized translation loss. This loss accumulates as a negative Cumulative Translation Adjustment (CTA) in Other Comprehensive "
                "Income (OCI), directly reducing consolidated shareholders' equity."
            )
        },
        {
            "id": "L2-V21-Q4",
            "level": 2,
            "module": "m15-multinational",
            "topic": "Multinational Operations",
            "vignette_id": "V21",
            "vignette_title": "Astra Minerals SA: Ratio Distortions Under a Weakening Foreign Currency",
            "vignette_text": v21_text,
            "los": "LOS 15.b: Compare the current rate method and the temporal method, evaluate how each method affects the parent company's balance sheet and income statement.",
            "question": "If Astra were translated using the Temporal Method during a period of steady ZAR depreciation, how would its reported Gross Profit Margin compare to the Current Rate Method?",
            "options": {
                "A": "Gross profit margin would be higher under the Temporal Method.",
                "B": "Gross profit margin would be lower under the Temporal Method.",
                "C": "Gross profit margin would be identical under both methods."
            },
            "answer": "B",
            "explanation": (
                "Under FIFO inventory accounting, goods sold were acquired earlier in the period when the foreign currency was stronger "
                "(higher exchange rate, e.g. $0.055$). Under the Temporal Method, COGS is remeasured using these older, higher historical exchange "
                "rates, whereas revenues are remeasured at the lower average exchange rate ($0.048$). This inflates remeasured COGS relative to revenues, "
                "depressing the reported Gross Profit Margin under the Temporal Method.\n\n"
                "Under the Current Rate Method, both revenues and COGS are translated at the same average rate ($0.048$), preserving the local margin."
            )
        },
        {
            "id": "L2-V21-Q5",
            "level": 2,
            "module": "m15-multinational",
            "topic": "Multinational Operations",
            "vignette_id": "V21",
            "vignette_title": "Astra Minerals SA: Ratio Distortions Under a Weakening Foreign Currency",
            "vignette_text": v21_text,
            "los": "LOS 15.b: Compare the current rate method and the temporal method, evaluate how each method affects the parent company's balance sheet and income statement.",
            "question": "Under the Temporal Method, how can a multinational eliminate balance sheet foreign exchange exposure without using derivatives?",
            "options": {
                "A": "By setting total assets equal to total liabilities.",
                "B": "By executing a natural balance sheet hedge that maintains Monetary Assets equal to Monetary Liabilities.",
                "C": "By converting all local debt into parent equity."
            },
            "answer": "B",
            "explanation": (
                "Under the Temporal Method, balance sheet exposure is strictly limited to Net Monetary Assets (Monetary Assets - Monetary Liabilities). "
                "A multinational can execute a 'natural balance sheet hedge' by matching monetary assets with monetary liabilities (net monetary position = 0). "
                "When $\\text{Monetary Assets} = \\text{Monetary Liabilities}$, any change in the exchange rate produces an equal and offsetting gain "
                "and loss, completely immunizing the consolidated income statement from remeasurement gains and losses."
            )
        },
        {
            "id": "L2-V21-Q6",
            "level": 2,
            "module": "m15-multinational",
            "topic": "Multinational Operations",
            "vignette_id": "V21",
            "vignette_title": "Astra Minerals SA: Ratio Distortions Under a Weakening Foreign Currency",
            "vignette_text": v21_text,
            "los": "LOS 15.d: Analyze the effect of alternative translation methods and exchange rate changes on financial ratios.",
            "question": "Under the Current Rate Method, how does the translated Return on Assets (Net Income / Ending Assets) compare to the local currency ratio as ZAR depreciates?",
            "options": {
                "A": "The translated Return on Assets is higher than the local currency ratio.",
                "B": "The translated Return on Assets is lower than the local currency ratio.",
                "C": "The translated Return on Assets is identical to the local currency ratio."
            },
            "answer": "A",
            "explanation": (
                "ROA is a mixed ratio:\n"
                "- In ZAR: $\\text{ROA} = 150 / 1,200 = 12.50\\%$.\n"
                "- In translated GBP:\n"
                "  Net Income = $150 \\times 0.048 \\text{ (average rate)} = 7.20$ million GBP.\n"
                "  Ending Assets = $1,200 \\times 0.040 \\text{ (ending rate)} = 48.00$ million GBP.\n"
                "  Translated ROA = $7.20 / 48.00 = 15.00\\%$.\n\n"
                "Because the exchange rate declined over the year, the average rate ($0.048$) in the numerator exceeds the ending rate ($0.040$) "
                "in the denominator, causing the translated ROA in GBP to be HIGHER than the original local currency ROA."
            )
        }
    ]
    vignettes.append((v21_text, v21_questions))

    # =========================================================================
    # VIGNETTE 22: Hyperinflationary Economies under IFRS (IAS 29)
    # =========================================================================
    v22_text = (
        "Pampa Agroindustrial SA is an agricultural processing subsidiary operating in Argentina, "
        "wholly owned by EuroFood Group SE, a European multinational reporting in euros (EUR). "
        "Over the past three years, Argentina experienced cumulative general price inflation of 115%. "
        "EuroFood prepares its consolidated financial statements under IFRS. Management determines that "
        "Argentina is a hyperinflationary economy in accordance with IAS 29 (Financial Reporting in "
        "Hyperinflationary Economies).\n\n"
        "Exhibit 1: General Price Index (CPI) and Exchange Rates\n"
        "- CPI at acquisition of Net PPE: 100\n"
        "- CPI at common stock issuance: 100\n"
        "- CPI at acquisition of ending inventory: 280\n"
        "- CPI at beginning of current year (1 Jan): 200\n"
        "- CPI at end of current year (31 Dec): 320\n"
        "- Current ending exchange rate at 31 Dec: 0.0020 EUR/ARS\n\n"
        "Exhibit 2: Pampa Agroindustrial Balance Sheet at 31 Dec (in millions of Argentine pesos, ARS)\n"
        "Monetary assets (Cash and Receivables): 120 ARS\n"
        "Inventory (acquired when CPI was 280): 140 ARS\n"
        "Net Property, plant & equipment (acquired when CPI was 100): 300 ARS\n"
        "Total Assets: 560 ARS\n\n"
        "Monetary liabilities (Accounts payable and bank loans): 200 ARS\n"
        "Common stock (issued when CPI was 100): 100 ARS\n"
        "Retained earnings (unadjusted historical cost): 260 ARS\n"
        "Total Liabilities and Equity: 560 ARS\n\n"
        "Under IAS 29, financial statement items must be restated for changes in the general price level "
        "using the price index at the balance sheet date, and then translated into the presentation currency "
        "(EUR) at the current exchange rate at the balance sheet date."
    )

    v22_questions = [
        {
            "id": "L2-V22-Q1",
            "level": 2,
            "module": "m15-multinational",
            "topic": "Multinational Operations",
            "vignette_id": "V22",
            "vignette_title": "Pampa Agroindustrial SA: Restatement and Translation under IAS 29",
            "vignette_text": v22_text,
            "los": "LOS 15.e: Explain how foreign operations in hyperinflationary economies are accounted for under IFRS and US GAAP.",
            "question": "Which of the following is an explicit quantitative indicator that an economy is hyperinflationary under IAS 29?",
            "options": {
                "A": "Annual inflation exceeding 20% in the current reporting year.",
                "B": "Cumulative inflation over a three-year period approaching or exceeding 100%.",
                "C": "Currency depreciation against the US dollar of more than 50% in a single quarter."
            },
            "answer": "B",
            "explanation": (
                "Under IAS 29.3, the primary quantitative benchmark indicating hyperinflation is when the cumulative inflation rate "
                "over three years approaches or exceeds 100% (equivalent to compounding roughly 26% per year over 3 consecutive years). "
                "Qualitative indicators include the general population preferring to keep wealth in non-monetary assets or a stable foreign currency, "
                "prices quoted in foreign currencies, and interest rates, wages, and prices linked to a price index.\n\n"
                "Distractor A and C are incorrect because single-year or quarterly spikes do not define hyperinflation under IAS 29."
            )
        },
        {
            "id": "L2-V22-Q2",
            "level": 2,
            "module": "m15-multinational",
            "topic": "Multinational Operations",
            "vignette_id": "V22",
            "vignette_title": "Pampa Agroindustrial SA: Restatement and Translation under IAS 29",
            "vignette_text": v22_text,
            "los": "LOS 15.e: Explain how foreign operations in hyperinflationary economies are accounted for under IFRS and US GAAP.",
            "question": "Under IAS 29, what are the restated values of Pampa's Net PPE and Ending Inventory in Argentine pesos (ARS) at 31 December?",
            "options": {
                "A": "Net PPE: 960 million ARS; Inventory: 160 million ARS.",
                "B": "Net PPE: 600 million ARS; Inventory: 140 million ARS.",
                "C": "Net PPE: 960 million ARS; Inventory: 224 million ARS."
            },
            "answer": "A",
            "explanation": (
                "Under IAS 29, non-monetary assets are restated by applying the change in the general price index from the date of acquisition "
                "to the balance sheet date:\n"
                "$\\text{Restated Value} = \\text{Historical Cost} \\times \\left(\\frac{\\text{Ending CPI}}{\\text{Acquisition CPI}}\\right)$\n\n"
                "1. Net PPE (acquired when CPI was 100, ending CPI is 320):\n"
                "$\\text{Restated Net PPE} = 300 \\times \\left(\\frac{320}{100}\\right) = 300 \\times 3.20 = 960$ million ARS.\n\n"
                "2. Inventory (acquired when CPI was 280, ending CPI is 320):\n"
                "$\\text{Restated Inventory} = 140 \\times \\left(\\frac{320}{280}\\right) = 140 \\times 1.14286 = 160$ million ARS.\n\n"
                "Distractor C incorrectly restates inventory from CPI 200 ($140 \\times 320/200 = 224$)."
            )
        },
        {
            "id": "L2-V22-Q3",
            "level": 2,
            "module": "m15-multinational",
            "topic": "Multinational Operations",
            "vignette_id": "V22",
            "vignette_title": "Pampa Agroindustrial SA: Restatement and Translation under IAS 29",
            "vignette_text": v22_text,
            "los": "LOS 15.e: Explain how foreign operations in hyperinflationary economies are accounted for under IFRS and US GAAP.",
            "question": "How are monetary assets and monetary liabilities treated during IAS 29 price-level restatement?",
            "options": {
                "A": "They are restated using the change in the CPI from the beginning of the year.",
                "B": "They are not restated because they are already expressed in terms of the monetary unit current at the balance sheet date.",
                "C": "They are restated using the current exchange rate against the euro."
            },
            "answer": "B",
            "explanation": (
                "Under IAS 29, monetary assets and monetary liabilities (such as cash, receivables, payables, and loans) are NOT restated "
                "because they are already expressed in terms of the monetary unit current at the balance sheet date. "
                "However, holding net monetary assets or liabilities during inflation results in a purchasing power gain or loss that must "
                "be recognized in Net Income."
            )
        },
        {
            "id": "L2-V22-Q4",
            "level": 2,
            "module": "m15-multinational",
            "topic": "Multinational Operations",
            "vignette_id": "V22",
            "vignette_title": "Pampa Agroindustrial SA: Restatement and Translation under IAS 29",
            "vignette_text": v22_text,
            "los": "LOS 15.e: Explain how foreign operations in hyperinflationary economies are accounted for under IFRS and US GAAP.",
            "question": "Because Pampa held a Net Monetary Liability position throughout the year, what purchasing power effect is recognized in its restated income statement under IAS 29?",
            "options": {
                "A": "A net purchasing power loss recognized in Net Income.",
                "B": "A net purchasing power gain recognized in Net Income.",
                "C": "A purchasing power gain recognized in OCI."
            },
            "answer": "B",
            "explanation": (
                "Pampa's Net Monetary Position = Monetary Assets (120 ARS) - Monetary Liabilities (200 ARS) = -80 million ARS (Net Monetary Liability).\n"
                "During a period of severe inflation, debtors pay back fixed nominal monetary liabilities with currency that has substantially "
                "diminished purchasing power. Therefore, holding net monetary liabilities during inflation produces a PURCHASING POWER GAIN.\n\n"
                "Under IAS 29, this gain on the net monetary position is recognized directly in the Income Statement (in Net Income), "
                "not in equity/OCI."
            )
        },
        {
            "id": "L2-V22-Q5",
            "level": 2,
            "module": "m15-multinational",
            "topic": "Multinational Operations",
            "vignette_id": "V22",
            "vignette_title": "Pampa Agroindustrial SA: Restatement and Translation under IAS 29",
            "vignette_text": v22_text,
            "los": "LOS 15.e: Explain how foreign operations in hyperinflationary economies are accounted for under IFRS and US GAAP.",
            "question": "After restating Pampa's balance sheet under IAS 29, what exchange rate does EuroFood apply to translate the restated figures into EUR?",
            "options": {
                "A": "The current exchange rate at the balance sheet date (0.0020 EUR/ARS) for all balance sheet and income statement items.",
                "B": "The weighted average exchange rate for the income statement and current rate for assets.",
                "C": "Historical exchange rates for non-monetary assets and current rates for monetary items."
            },
            "answer": "A",
            "explanation": (
                "Under IFRS (IAS 29 combined with IAS 21), once the financial statements of a hyperinflationary subsidiary have been fully "
                "restated for price-level changes into current units of purchasing power at the balance sheet date, ALL items (both balance sheet "
                "and income statement) are translated into the presentation currency at the CURRENT exchange rate prevailing at the balance sheet date "
                "($0.0020$ EUR/ARS).\n\n"
                "Distractor B and C reflect normal non-hyperinflationary translation or US GAAP rules."
            )
        },
        {
            "id": "L2-V22-Q6",
            "level": 2,
            "module": "m15-multinational",
            "topic": "Multinational Operations",
            "vignette_id": "V22",
            "vignette_title": "Pampa Agroindustrial SA: Restatement and Translation under IAS 29",
            "vignette_text": v22_text,
            "los": "LOS 15.e: Explain how foreign operations in hyperinflationary economies are accounted for under IFRS and US GAAP.",
            "question": "Pampa's translated Total Assets in EuroFood's consolidated balance sheet in EUR is closest to:",
            "options": {
                "A": "1.12 million EUR.",
                "B": "2.48 million EUR.",
                "C": "1.76 million EUR."
            },
            "answer": "B",
            "explanation": (
                "1. Calculate Restated Total Assets in ARS:\n"
                "- Monetary assets (unadjusted): 120 million ARS\n"
                "- Restated Inventory: 160 million ARS (from Question 2)\n"
                "- Restated Net PPE: 960 million ARS (from Question 2)\n"
                "- Restated Total Assets = $120 + 160 + 960 = 1,240$ million ARS.\n\n"
                "2. Translate into EUR at the current exchange rate ($0.0020$ EUR/ARS):\n"
                "$\\text{Translated Total Assets} = 1,240 \\times 0.0020 = 2.48$ million EUR.\n\n"
                "Distractor A incorrectly translates unadjusted historical cost assets ($560 \\times 0.0020 = 1.12$ million EUR).\n"
                "Distractor C incorrectly omits the PPE restatement."
            )
        }
    ]
    vignettes.append((v22_text, v22_questions))

    # =========================================================================
    # VIGNETTE 23: Hyperinflationary Economies under US GAAP vs IFRS
    # =========================================================================
    v23_text = (
        "Mercosur Logistics Corp is a multinational logistics enterprise. It owns two identical distribution "
        "subsidiaries operating in a country experiencing severe hyperinflation (cumulative 3-year inflation of 120%):\n"
        "- Sub A is consolidated under US GAAP (ASC 830).\n"
        "- Sub B is consolidated under IFRS (IAS 21 and IAS 29).\n\n"
        "Both subsidiaries hold the following identical balance sheet items in local currency (LC) at year-end:\n"
        "- Monetary assets (Cash and A/R): 100 million LC\n"
        "- Inventory (acquired when CPI was 250): 100 million LC\n"
        "- Net Fixed Assets (acquired when CPI was 100): 400 million LC\n"
        "- Monetary liabilities (Debt): 300 million LC\n\n"
        "Price Index and Exchange Rate Data:\n"
        "- CPI at fixed asset acquisition date: 100\n"
        "- CPI at ending inventory acquisition: 250\n"
        "- CPI at current balance sheet date: 300\n"
        "- Exchange rate when fixed assets acquired: 0.10 USD/LC\n"
        "- Exchange rate when ending inventory acquired: 0.04 USD/LC\n"
        "- Average exchange rate for the year: 0.05 USD/LC\n"
        "- Current ending exchange rate at balance sheet date: 0.02 USD/LC\n\n"
        "Financial analyst Sophia Lin is preparing a briefing for the board comparing the balance sheet "
        "and earnings differences caused strictly by US GAAP versus IFRS rules for hyperinflation."
    )

    v23_questions = [
        {
            "id": "L2-V23-Q1",
            "level": 2,
            "module": "m15-multinational",
            "topic": "Multinational Operations",
            "vignette_id": "V23",
            "vignette_title": "Mercosur Logistics Corp: US GAAP (ASC 830) vs IFRS (IAS 29) in Hyperinflation",
            "vignette_text": v23_text,
            "los": "LOS 15.e: Explain how foreign operations in hyperinflationary economies are accounted for under IFRS and US GAAP.",
            "question": "Under US GAAP (ASC 830), how must a foreign subsidiary operating in a hyperinflationary economy be accounted for?",
            "options": {
                "A": "Restate local currency financial statements using the local price index, then translate using the current exchange rate.",
                "B": "The subsidiary's functional currency is mandated to be the parent's reporting currency (USD), and financial statements must be remeasured using the Temporal Method.",
                "C": "The subsidiary must use the Current Rate Method, with all translation gains/losses recognized directly in net income."
            },
            "answer": "B",
            "explanation": (
                "Under US GAAP (ASC 830), the financial statements of a foreign entity in a hyperinflationary economy (cumulative 3-year "
                "inflation $\\ge 100\\%$) must be remeasured as if the functional currency were the reporting currency (typically USD). "
                "Therefore, the entity MUST apply the Temporal Method. Price-level restatement of local currency statements is NOT permitted under US GAAP.\n\n"
                "Distractor A describes the IFRS approach under IAS 29.\n"
                "Distractor C is incorrect because the Current Rate Method is prohibited for hyperinflationary operations under US GAAP."
            )
        },
        {
            "id": "L2-V23-Q2",
            "level": 2,
            "module": "m15-multinational",
            "topic": "Multinational Operations",
            "vignette_id": "V23",
            "vignette_title": "Mercosur Logistics Corp: US GAAP (ASC 830) vs IFRS (IAS 29) in Hyperinflation",
            "vignette_text": v23_text,
            "los": "LOS 15.e: Explain how foreign operations in hyperinflationary economies are accounted for under IFRS and US GAAP.",
            "question": "What is the reported value of Net Fixed Assets in USD for Sub A (US GAAP) versus Sub B (IFRS)?",
            "options": {
                "A": "Sub A (US GAAP): 40.0 million USD; Sub B (IFRS): 24.0 million USD.",
                "B": "Sub A (US GAAP): 8.0 million USD; Sub B (IFRS): 24.0 million USD.",
                "C": "Sub A (US GAAP): 40.0 million USD; Sub B (IFRS): 8.0 million USD."
            },
            "answer": "A",
            "explanation": (
                "1. Sub A under US GAAP (Temporal Method):\n"
                "Net Fixed Assets are remeasured at the historical exchange rate when acquired ($0.10$ USD/LC):\n"
                "$\\text{Fixed Assets (US GAAP)} = 400 \\text{ million LC} \\times 0.10 = 40.0$ million USD.\n\n"
                "2. Sub B under IFRS (IAS 29 Restate-then-Translate):\n"
                "- First, restate for local price inflation: $400 \\times (300 / 100) = 1,200$ million LC.\n"
                "- Second, translate at current ending exchange rate ($0.02$ USD/LC):\n"
                "$\\text{Fixed Assets (IFRS)} = 1,200 \\times 0.02 = 24.0$ million USD.\n\n"
                "Therefore, Sub A reports 40.0 million USD while Sub B reports 24.0 million USD.\n\n"
                "Distractor B and C miscalculate the restatement or use the wrong exchange rates."
            )
        },
        {
            "id": "L2-V23-Q3",
            "level": 2,
            "module": "m15-multinational",
            "topic": "Multinational Operations",
            "vignette_id": "V23",
            "vignette_title": "Mercosur Logistics Corp: US GAAP (ASC 830) vs IFRS (IAS 29) in Hyperinflation",
            "vignette_text": v23_text,
            "los": "LOS 15.e: Explain how foreign operations in hyperinflationary economies are accounted for under IFRS and US GAAP.",
            "question": "Where are inflation-related gains and losses reported under US GAAP versus IFRS?",
            "options": {
                "A": "Both US GAAP (remeasurement gains/losses) and IFRS (net purchasing power gains/losses) recognize the impact in Net Income.",
                "B": "US GAAP recognizes them in Net Income, whereas IFRS recognizes purchasing power gains/losses in OCI.",
                "C": "US GAAP recognizes them in OCI, whereas IFRS recognizes them in Net Income."
            },
            "answer": "A",
            "explanation": (
                "Both frameworks report the gain/loss in Net Income, but from fundamentally different concepts:\n"
                "- Under US GAAP, the entity recognizes a foreign exchange remeasurement gain/loss on its net monetary position in Net Income.\n"
                "- Under IFRS (IAS 29), the entity recognizes a purchasing power gain/loss on its net monetary position in Net Income.\n\n"
                "Distractor B and C incorrectly state that one of the standards places these gains/losses in OCI."
            )
        },
        {
            "id": "L2-V23-Q4",
            "level": 2,
            "module": "m15-multinational",
            "topic": "Multinational Operations",
            "vignette_id": "V23",
            "vignette_title": "Mercosur Logistics Corp: US GAAP (ASC 830) vs IFRS (IAS 29) in Hyperinflation",
            "vignette_text": v23_text,
            "los": "LOS 15.e: Explain how foreign operations in hyperinflationary economies are accounted for under IFRS and US GAAP.",
            "question": "Under IFRS (IAS 29), what is the restated value of ending inventory in local currency (LC)?",
            "options": {
                "A": "100 million LC.",
                "B": "120 million LC.",
                "C": "300 million LC."
            },
            "answer": "B",
            "explanation": (
                "Inventory was acquired when the CPI was 250, and the ending CPI at the balance sheet date is 300.\n"
                "$\\text{Restated Inventory} = 100 \\times \\left(\\frac{300}{250}\\right) = 100 \\times 1.20 = 120$ million LC.\n\n"
                "Distractor A represents unadjusted historical cost.\n"
                "Distractor C restates from CPI 100."
            )
        },
        {
            "id": "L2-V23-Q5",
            "level": 2,
            "module": "m15-multinational",
            "topic": "Multinational Operations",
            "vignette_id": "V23",
            "vignette_title": "Mercosur Logistics Corp: US GAAP (ASC 830) vs IFRS (IAS 29) in Hyperinflation",
            "vignette_text": v23_text,
            "los": "LOS 15.e: Explain how foreign operations in hyperinflationary economies are accounted for under IFRS and US GAAP.",
            "question": "Why do reported fixed asset values differ between US GAAP and IFRS in hyperinflationary conditions?",
            "options": {
                "A": "Because purchasing power parity (PPP) rarely holds in the short run, so currency depreciation often outpaces or lags general price inflation.",
                "B": "Because US GAAP mandates fair value mark-to-market for fixed assets.",
                "C": "Because IFRS prohibits translation of fixed assets into foreign currencies."
            },
            "answer": "A",
            "explanation": (
                "Under relative purchasing power parity (PPP), the rate of currency depreciation would exactly equal the difference in inflation rates. "
                "If PPP held perfectly, restating for inflation and multiplying by the ending exchange rate (IFRS) would yield the exact same figure "
                "as remeasuring at historical exchange rates (US GAAP). However, in real-world hyperinflationary environments, currency depreciation "
                "often deviates significantly from domestic inflation due to capital controls, sovereign risk, or speculative runs, creating substantial "
                "divergence between IFRS and US GAAP asset valuations.\n\n"
                "Distractor B and C are factually untrue."
            )
        },
        {
            "id": "L2-V23-Q6",
            "level": 2,
            "module": "m15-multinational",
            "topic": "Multinational Operations",
            "vignette_id": "V23",
            "vignette_title": "Mercosur Logistics Corp: US GAAP (ASC 830) vs IFRS (IAS 29) in Hyperinflation",
            "vignette_text": v23_text,
            "los": "LOS 15.e: Explain how foreign operations in hyperinflationary economies are accounted for under IFRS and US GAAP.",
            "question": "When comparing two peer companies operating in the same hyperinflationary market—one reporting under US GAAP and the other under IFRS—an analyst should recognize that:",
            "options": {
                "A": "US GAAP operating margins are typically more comparable to local economic realities than IFRS margins.",
                "B": "IFRS price-level adjusted statements provide a more economically realistic depiction of real operating capacity and replacement cost.",
                "C": "Both accounting systems produce identical asset turnover and leverage ratios."
            },
            "answer": "B",
            "explanation": (
                "Under IFRS (IAS 29), restating non-monetary assets to current general purchasing power units adjusts historical costs "
                "for cumulative erosion in money value. Consequently, depreciation and asset values reflect current purchasing power, "
                "providing analysts with a much more realistic picture of the company's real capital maintenance and productive capacity. "
                "Under US GAAP, temporal method remeasurement ignores local inflation and relies on historical nominal exchange rates, "
                "which can severely distort profitability and asset values."
            )
        }
    ]
    vignettes.append((v23_text, v23_questions))

    return vignettes

if __name__ == "__main__":
    vigs = get_vignettes_16_to_23()
    total_q = sum(len(q_list) for _, q_list in vigs)
    print(f"Generated {len(vigs)} vignettes with {total_q} questions for Topic 15.")
