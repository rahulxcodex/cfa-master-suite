# Module 6: Financial Analysis Techniques & DuPont Analysis
# Questions L1-Q076 to L1-Q090 (15 questions)

questions = [
    {
        "id": "L1-Q076",
        "level": 1,
        "module": "m6-ratios",
        "topic": "Financial Analysis Techniques",
        "los": "LOS 25.b: Calculate and interpret activity, liquidity, solvency, and profitability ratios.",
        "question": "A wholesale distributor reports Cost of Goods Sold of 6,570,000 USD for the year. Beginning inventory was 710,000 USD and ending inventory was 750,000 USD. Assuming a 365-day year, what are the company's inventory turnover and days of inventory on hand (DOH)?",
        "options": {
            "A": "Inventory turnover: 8.76 times; DOH: 41.7 days.",
            "B": "Inventory turnover: 9.00 times; DOH: 40.6 days.",
            "C": "Inventory turnover: 9.25 times; DOH: 39.5 days."
        },
        "answer": "B",
        "explanation": "1. Average Inventory:\n$$\\text{Average Inventory} = \\frac{710,000\\text{ USD} + 750,000\\text{ USD}}{2} = 730,000\\text{ USD}$$\n2. Inventory Turnover:\n$$\\text{Inventory Turnover} = \\frac{\\text{COGS}}{\\text{Average Inventory}} = \\frac{6,570,000\\text{ USD}}{730,000\\text{ USD}} = 9.00\\text{ times}$$\n3. Days of Inventory on Hand (DOH):\n$$\\text{DOH} = \\frac{365}{\\text{Inventory Turnover}} = \\frac{365}{9.00} \\approx 40.56 \\approx 40.6\\text{ days}$$\n\nDistractor Analysis:\n- A uses ending inventory ($6,570,000 / 750,000 = 8.76$ times; $365 / 8.76 = 41.7$ days) instead of average inventory.\n- C uses beginning inventory ($6,570,000 / 710,000 = 9.25$ times; $365 / 9.25 = 39.5$ days)."
    },
    {
        "id": "L1-Q077",
        "level": 1,
        "module": "m6-ratios",
        "topic": "Financial Analysis Techniques",
        "los": "LOS 25.b: Calculate and interpret activity, liquidity, solvency, and profitability ratios.",
        "question": "A company reports annual credit sales revenue of 10,950,000 USD. Beginning accounts receivable was 850,000 USD and ending accounts receivable was 950,000 USD. Assuming a 365-day year, what is the receivables turnover and days sales outstanding (DSO)?",
        "options": {
            "A": "Receivables turnover: 11.53 times; DSO: 31.7 days.",
            "B": "Receivables turnover: 12.17 times; DSO: 30.0 days.",
            "C": "Receivables turnover: 12.88 times; DSO: 28.3 days."
        },
        "answer": "B",
        "explanation": "1. Average Accounts Receivable:\n$$\\text{Average AR} = \\frac{850,000\\text{ USD} + 950,000\\text{ USD}}{2} = 900,000\\text{ USD}$$\n2. Receivables Turnover:\n$$\\text{Receivables Turnover} = \\frac{\\text{Revenue}}{\\text{Average AR}} = \\frac{10,950,000\\text{ USD}}{900,000\\text{ USD}} = 12.167 \\approx 12.17\\text{ times}$$\n3. Days Sales Outstanding (DSO):\n$$\\text{DSO} = \\frac{365}{\\text{Receivables Turnover}} = \\frac{365}{12.167} \\approx 30.0\\text{ days}$$\n\nDistractor Analysis:\n- A uses ending receivables ($10,950,000 / 950,000 = 11.53$ times; $365 / 11.53 = 31.7$ days).\n- C uses beginning receivables ($10,950,000 / 850,000 = 12.88$ times; $365 / 12.88 = 28.3$ days)."
    },
    {
        "id": "L1-Q078",
        "level": 1,
        "module": "m6-ratios",
        "topic": "Financial Analysis Techniques",
        "los": "LOS 25.b: Calculate and interpret activity, liquidity, solvency, and profitability ratios.",
        "question": "A manufacturing firm had total inventory purchases of 5,840,000 USD during the fiscal year. Beginning accounts payable was 700,000 USD and ending accounts payable was 760,000 USD. Using a 365-day year, what is the number of days of payables outstanding?",
        "options": {
            "A": "43.8 days",
            "B": "45.6 days",
            "C": "47.5 days"
        },
        "answer": "B",
        "explanation": "1. Average Accounts Payable:\n$$\\text{Average AP} = \\frac{700,000\\text{ USD} + 760,000\\text{ USD}}{2} = 730,000\\text{ USD}$$\n2. Payables Turnover:\n$$\\text{Payables Turnover} = \\frac{\\text{Purchases}}{\\text{Average AP}} = \\frac{5,840,000\\text{ USD}}{730,000\\text{ USD}} = 8.00\\text{ times}$$\n3. Number of Days of Payables:\n$$\\text{Number of Days of Payables} = \\frac{365}{\\text{Payables Turnover}} = \\frac{365}{8.00} = 45.625 \\approx 45.6\\text{ days}$$\n\nDistractor Analysis:\n- A uses beginning AP ($5,840,000 / 700,000 = 8.34$ times; $365 / 8.34 = 43.8$ days).\n- C uses ending AP ($5,840,000 / 760,000 = 7.68$ times; $365 / 7.68 = 47.5$ days)."
    },
    {
        "id": "L1-Q079",
        "level": 1,
        "module": "m6-ratios",
        "topic": "Financial Analysis Techniques",
        "los": "LOS 25.b: Calculate and interpret activity, liquidity, solvency, and profitability ratios.",
        "question": "An analyst compiles the following operating metrics for a major retailer: Days of inventory on hand (DOH) is 38 days, Days sales outstanding (DSO) is 12 days, and Number of days of payables is 65 days. What is the firm's Cash Conversion Cycle (CCC), and what does this metric signify?",
        "options": {
            "A": "CCC is -15 days, indicating that the company collects cash from sales well before it must pay its suppliers, effectively financing its working capital through supplier credit.",
            "B": "CCC is +15 days, indicating that the company requires external short-term credit lines to cover 15 days of operating working capital.",
            "C": "CCC is +89 days, indicating substantial operational inefficiency in managing inventory and customer receivables."
        },
        "answer": "A",
        "explanation": "The Cash Conversion Cycle (net operating cycle) is:\n$$\\text{CCC} = \\text{DOH} + \\text{DSO} - \\text{Number of Days of Payables}$$\n$$\\text{CCC} = 38\\text{ days} + 12\\text{ days} - 65\\text{ days} = -15\\text{ days}$$\nA negative cash conversion cycle indicates that the company collects receivables and sells inventory faster than it pays suppliers. The suppliers effectively finance the retailer's inventory and operating liquidity, which is characteristic of dominant retail models like supermarkets or hypermarkets.\n\nDistractor Analysis:\n- B incorrectly calculates a positive number ($65 - 38 - 12 = +15$ days).\n- C adds all three components without subtracting payables: $38 + 12 + 65 = 115$ or $89$ days."
    },
    {
        "id": "L1-Q080",
        "level": 1,
        "module": "m6-ratios",
        "topic": "Financial Analysis Techniques",
        "los": "LOS 25.b: Calculate and interpret activity, liquidity, solvency, and profitability ratios.",
        "question": "A firm reports total revenue of 12,000,000 USD. Current assets are 3,000,000 USD, current liabilities are 1,800,000 USD, and average net fixed assets are 4,000,000 USD. Assuming current assets and liabilities remained constant across the year, what are the firm's working capital turnover and fixed asset turnover ratios?",
        "options": {
            "A": "Working capital turnover: 10.0 times; Fixed asset turnover: 3.0 times.",
            "B": "Working capital turnover: 4.0 times; Fixed asset turnover: 3.0 times.",
            "C": "Working capital turnover: 6.67 times; Fixed asset turnover: 2.5 times."
        },
        "answer": "A",
        "explanation": "1. Working Capital:\n$$\\text{Working Capital} = \\text{Current Assets} - \\text{Current Liabilities} = 3,000,000\\text{ USD} - 1,800,000\\text{ USD} = 1,200,000\\text{ USD}$$\n2. Working Capital Turnover:\n$$\\text{Working Capital Turnover} = \\frac{\\text{Revenue}}{\\text{Average Working Capital}} = \\frac{12,000,000\\text{ USD}}{1,200,000\\text{ USD}} = 10.0\\text{ times}$$\n3. Fixed Asset Turnover:\n$$\\text{Fixed Asset Turnover} = \\frac{\\text{Revenue}}{\\text{Average Net Fixed Assets}} = \\frac{12,000,000\\text{ USD}}{4,000,000\\text{ USD}} = 3.0\\text{ times}$$\n\nDistractor Analysis:\n- B calculates working capital turnover using total current assets: $12,000,000 / 3,000,000 = 4.0$ times.\n- C makes errors in denominator selection."
    },
    {
        "id": "L1-Q081",
        "level": 1,
        "module": "m6-ratios",
        "topic": "Financial Analysis Techniques",
        "los": "LOS 25.b: Calculate and interpret activity, liquidity, solvency, and profitability ratios.",
        "question": "A company presents the following balance sheet information:\n- Cash and cash equivalents: 150,000 USD\n- Marketable securities: 250,000 USD\n- Accounts receivable: 400,000 USD\n- Inventories: 500,000 USD\n- Prepaid expenses: 50,000 USD\n- Current liabilities: 675,000 USD\nWhat are the company's quick ratio and cash ratio?",
        "options": {
            "A": "Quick ratio: 1.19; Cash ratio: 0.59.",
            "B": "Quick ratio: 1.93; Cash ratio: 0.22.",
            "C": "Quick ratio: 0.89; Cash ratio: 0.59."
        },
        "answer": "A",
        "explanation": "1. Quick Ratio (Acid-Test Ratio):\n$$\\text{Quick Assets} = \\text{Cash} + \\text{Marketable Securities} + \\text{Receivables}$$\n$$\\text{Quick Assets} = 150,000\\text{ USD} + 250,000\\text{ USD} + 400,000\\text{ USD} = 800,000\\text{ USD}$$\n$$\\text{Quick Ratio} = \\frac{800,000\\text{ USD}}{675,000\\text{ USD}} = 1.185 \\approx 1.19$$\n2. Cash Ratio:\n$$\\text{Cash Assets} = \\text{Cash} + \\text{Marketable Securities} = 150,000\\text{ USD} + 250,000\\text{ USD} = 400,000\\text{ USD}$$\n$$\\text{Cash Ratio} = \\frac{400,000\\text{ USD}}{675,000\\text{ USD}} = 0.5925 \\approx 0.59$$\n(Note: Total current assets = 1,350,000 USD; Current ratio = $1,350,000 / 675,000 = 2.00$).\n\nDistractor Analysis:\n- B uses current ratio (or includes inventory in quick assets) and divides only cash ($150,000 / 675,000 = 0.22$).\n- C excludes receivables from quick assets ($400,000 / 675,000$ or similar error)."
    },
    {
        "id": "L1-Q082",
        "level": 1,
        "module": "m6-ratios",
        "topic": "Financial Analysis Techniques",
        "los": "LOS 25.b: Calculate and interpret activity, liquidity, solvency, and profitability ratios.",
        "question": "A firm has cash of 300,000 USD, marketable securities of 200,000 USD, and accounts receivable of 500,000 USD. Annual cash expenditures (projected operating costs excluding non-cash depreciation) are 7,300,000 USD. Assuming 365 days in a year, what is the firm's Defensive Interval Ratio (DIR)?",
        "options": {
            "A": "25 days",
            "B": "50 days",
            "C": "75 days"
        },
        "answer": "B",
        "explanation": "1. Daily Cash Expenditures:\n$$\\text{Daily Expenditures} = \\frac{\\text{Annual Cash Expenditures}}{365} = \\frac{7,300,000\\text{ USD}}{365} = 20,000\\text{ USD per day}$$\n2. Defensive Assets:\n$$\\text{Defensive Assets} = \\text{Cash} + \\text{Marketable Securities} + \\text{Receivables}$$\n$$\\text{Defensive Assets} = 300,000\\text{ USD} + 200,000\\text{ USD} + 500,000\\text{ USD} = 1,000,000\\text{ USD}$$\n3. Defensive Interval Ratio (DIR):\n$$\\text{DIR} = \\frac{\\text{Defensive Assets}}{\\text{Daily Cash Expenditures}} = \\frac{1,000,000\\text{ USD}}{20,000\\text{ USD/day}} = 50\\text{ days}$$\nThis indicates the company can cover its daily cash expenses for 50 days without any additional cash inflow.\n\nDistractor Analysis:\n- A considers only cash and marketable securities ($500,000 / 20,000 = 25$ days).\n- C uses incorrect expense assumptions or miscalculated daily burn rates."
    },
    {
        "id": "L1-Q083",
        "level": 1,
        "module": "m6-ratios",
        "topic": "Financial Analysis Techniques",
        "los": "LOS 25.b: Calculate and interpret activity, liquidity, solvency, and profitability ratios.",
        "question": "A company has short-term interest-bearing notes of 400,000 USD, long-term debt of 1,600,000 USD, total liabilities of 3,000,000 USD, and total shareholders' equity of 2,000,000 USD. Total assets are 5,000,000 USD. What are the company's debt-to-equity ratio (using total debt) and financial leverage ratio?",
        "options": {
            "A": "Debt-to-equity: 1.00; Financial leverage: 2.50.",
            "B": "Debt-to-equity: 1.50; Financial leverage: 2.50.",
            "C": "Debt-to-equity: 1.00; Financial leverage: 1.50."
        },
        "answer": "A",
        "explanation": "1. Total Debt (interest-bearing debt):\n$$\\text{Total Debt} = \\text{Short-Term Debt} + \\text{Long-Term Debt} = 400,000\\text{ USD} + 1,600,000\\text{ USD} = 2,000,000\\text{ USD}$$\n2. Debt-to-Equity Ratio:\n$$\\text{Debt-to-Equity} = \\frac{\\text{Total Debt}}{\\text{Total Equity}} = \\frac{2,000,000\\text{ USD}}{2,000,000\\text{ USD}} = 1.00$$\n3. Financial Leverage Ratio (Equity Multiplier):\n$$\\text{Financial Leverage} = \\frac{\\text{Total Assets}}{\\text{Total Equity}} = \\frac{5,000,000\\text{ USD}}{2,000,000\\text{ USD}} = 2.50$$\n\nDistractor Analysis:\n- B uses total liabilities (3,000,000 USD) instead of interest-bearing debt for the debt-to-equity ratio: $3,000,000 / 2,000,000 = 1.50$.\n- C uses total liabilities divided by total equity for leverage."
    },
    {
        "id": "L1-Q084",
        "level": 1,
        "module": "m6-ratios",
        "topic": "Financial Analysis Techniques",
        "los": "LOS 25.b: Calculate and interpret activity, liquidity, solvency, and profitability ratios.",
        "question": "For the year ended 31 December, an industrial firm reports EBIT of 4,800,000 USD, interest expense of 800,000 USD, and operating lease payments of 400,000 USD. What are the company's interest coverage ratio (times interest earned) and fixed charge coverage ratio?",
        "options": {
            "A": "Interest coverage: 6.00 times; Fixed charge coverage: 4.33 times.",
            "B": "Interest coverage: 6.00 times; Fixed charge coverage: 4.00 times.",
            "C": "Interest coverage: 5.00 times; Fixed charge coverage: 3.75 times."
        },
        "answer": "A",
        "explanation": "1. Interest Coverage Ratio (Times Interest Earned):\n$$\\text{Interest Coverage} = \\frac{\\text{EBIT}}{\\text{Interest Payments}} = \\frac{4,800,000\\text{ USD}}{800,000\\text{ USD}} = 6.00\\text{ times}$$\n2. Fixed Charge Coverage Ratio:\n$$\\text{Fixed Charge Coverage} = \\frac{\\text{EBIT} + \\text{Lease Payments}}{\\text{Interest Payments} + \\text{Lease Payments}}$$\n$$\\text{Fixed Charge Coverage} = \\frac{4,800,000\\text{ USD} + 400,000\\text{ USD}}{800,000\\text{ USD} + 400,000\\text{ USD}} = \\frac{5,200,000\\text{ USD}}{1,200,000\\text{ USD}} = 4.333 \\approx 4.33\\text{ times}$$\n\nDistractor Analysis:\n- B fails to add back lease payments to the numerator: $4,800,000 / 1,200,000 = 4.00$ times.\n- C makes calculation errors in EBIT."
    },
    {
        "id": "L1-Q085",
        "level": 1,
        "module": "m6-ratios",
        "topic": "Financial Analysis Techniques",
        "los": "LOS 25.b: Calculate and interpret activity, liquidity, solvency, and profitability ratios.",
        "question": "A company reports revenue of 10,000,000 USD, gross profit of 4,500,000 USD, operating profit (EBIT) of 1,800,000 USD, and net income of 1,200,000 USD. Average total assets are 8,000,000 USD. What are the company's operating profit margin and return on assets (ROA)?",
        "options": {
            "A": "Operating profit margin: 45%; ROA: 15%.",
            "B": "Operating profit margin: 18%; ROA: 15%.",
            "C": "Operating profit margin: 18%; ROA: 22.5%."
        },
        "answer": "B",
        "explanation": "1. Operating Profit Margin:\n$$\\text{Operating Margin} = \\frac{\\text{Operating Profit (EBIT)}}{\\text{Revenue}} = \\frac{1,800,000\\text{ USD}}{10,000,000\\text{ USD}} = 18.0\\%$$\n2. Return on Assets (ROA):\n$$\\text{ROA} = \\frac{\\text{Net Income}}{\\text{Average Total Assets}} = \\frac{1,200,000\\text{ USD}}{8,000,000\\text{ USD}} = 15.0\\%$$\n(Note: Operating ROA would be $\\text{EBIT} / \\text{Assets} = 1,800,000 / 8,000,000 = 22.5\\%$).\n\nDistractor Analysis:\n- A quotes gross margin ($4,500,000 / 10,000,000 = 45\\%$).\n- C quotes operating ROA (22.5%) instead of standard net ROA (15%)."
    },
    {
        "id": "L1-Q086",
        "level": 1,
        "module": "m6-ratios",
        "topic": "Financial Analysis Techniques",
        "los": "LOS 25.c: Describe the DuPont system of analysis and calculate return on equity using three-stage and five-stage models.",
        "question": "Under the traditional three-stage DuPont model, return on equity (ROE) is decomposed into which three multiplicative components?",
        "options": {
            "A": "Gross profit margin, fixed asset turnover, and debt-to-capital ratio.",
            "B": "Net profit margin, total asset turnover, and financial leverage (equity multiplier).",
            "C": "Operating margin, working capital turnover, and times interest earned."
        },
        "answer": "B",
        "explanation": "The 3-stage DuPont model decomposes Return on Equity as:\n$$\\text{ROE} = \\frac{\\text{Net Income}}{\\text{Equity}} = \\left(\\frac{\\text{Net Income}}{\\text{Revenue}}\\right) \\times \\left(\\frac{\\text{Revenue}}{\\text{Assets}}\\right) \\times \\left(\\frac{\\text{Assets}}{\\text{Equity}}\\right)$$\n$$\\text{ROE} = \\text{Net Profit Margin} \\times \\text{Total Asset Turnover} \\times \\text{Financial Leverage}$$\n\nDistractor Analysis:\n- A and C list ratios from disparate categories that do not mathematically equate to ROE when multiplied."
    },
    {
        "id": "L1-Q087",
        "level": 1,
        "module": "m6-ratios",
        "topic": "Financial Analysis Techniques",
        "los": "LOS 25.c: Describe the DuPont system of analysis and calculate return on equity using three-stage and five-stage models.",
        "question": "In the five-stage DuPont system, how is the 'Tax Burden' component calculated, and what does an increase in this ratio signify?",
        "options": {
            "A": "$\\frac{\\text{Tax Expense}}{\\text{EBT}}$; an increase signifies that the company faces higher marginal tax rates.",
            "B": "$\\frac{\\text{Net Income}}{\\text{EBT}}$; an increase signifies that the company retains a larger proportion of pretax earnings due to a lower effective tax rate.",
            "C": "$\\frac{\\text{EBT}}{\\text{EBIT}}$; an increase signifies lower interest costs relative to operating profits."
        },
        "answer": "B",
        "explanation": "In the 5-stage DuPont system:\n$$\\text{Tax Burden} = \\frac{\\text{Net Income}}{\\text{EBT}} = 1 - \\text{Effective Tax Rate}$$\nBecause $\\text{Net Income} = \\text{EBT} - \\text{Taxes}$, an increase in the Tax Burden ratio means the firm retains more profit per dollar of pretax income (i.e., its effective tax rate has decreased), which increases ROE.\n\nDistractor Analysis:\n- A represents the effective tax rate itself; in DuPont analysis, the tax burden is defined as $NI / EBT$.\n- C defines the 'Interest Burden' ratio ($EBT / EBIT$)."
    },
    {
        "id": "L1-Q088",
        "level": 1,
        "module": "m6-ratios",
        "topic": "Financial Analysis Techniques",
        "los": "LOS 25.c: Describe the DuPont system of analysis and calculate return on equity using three-stage and five-stage models.",
        "question": "An analyst compiles the following financial data for a firm:\n- Net income: 630,000 USD\n- Pretax income (EBT): 900,000 USD\n- Operating profit (EBIT): 1,200,000 USD\n- Revenue: 8,000,000 USD\n- Average total assets: 5,000,000 USD\n- Average shareholders' equity: 2,000,000 USD\nUsing the five-stage DuPont model, what are the interest burden and the return on equity (ROE)?",
        "options": {
            "A": "Interest burden: 0.75; ROE: 31.5%.",
            "B": "Interest burden: 0.70; ROE: 31.5%.",
            "C": "Interest burden: 0.75; ROE: 25.2%."
        },
        "answer": "A",
        "explanation": "Calculating the 5 components of the five-stage DuPont system:\n1. Tax Burden = $\\frac{\\text{Net Income}}{\\text{EBT}} = \\frac{630,000\\text{ USD}}{900,000\\text{ USD}} = 0.70$\n2. Interest Burden = $\\frac{\\text{EBT}}{\\text{EBIT}} = \\frac{900,000\\text{ USD}}{1,200,000\\text{ USD}} = 0.75$\n3. EBIT Margin = $\\frac{\\text{EBIT}}{\\text{Revenue}} = \\frac{1,200,000\\text{ USD}}{8,000,000\\text{ USD}} = 0.15$ (15%)\n4. Asset Turnover = $\\frac{\\text{Revenue}}{\\text{Assets}} = \\frac{8,000,000\\text{ USD}}{5,000,000\\text{ USD}} = 1.60$\n5. Financial Leverage = $\\frac{\\text{Assets}}{\\text{Equity}} = \\frac{5,000,000\\text{ USD}}{2,000,000\\text{ USD}} = 2.50$\n\nMultiplying all 5 components:\n$$\\text{ROE} = 0.70 \\times 0.75 \\times 0.15 \\times 1.60 \\times 2.50 = 0.315 = 31.5\\%$$\nDirect check: $\\text{ROE} = \\frac{\\text{Net Income}}{\\text{Equity}} = \\frac{630,000\\text{ USD}}{2,000,000\\text{ USD}} = 31.5\\%$.\n\nDistractor Analysis:\n- B confuses the Tax Burden (0.70) with the Interest Burden (0.75).\n- C uses incorrect leverage or turnover multiplications."
    },
    {
        "id": "L1-Q089",
        "level": 1,
        "module": "m6-ratios",
        "topic": "Financial Analysis Techniques",
        "los": "LOS 25.d: Describe the limitations of financial ratio analysis.",
        "question": "Which of the following scenarios presents the most significant limitation to cross-sectional financial ratio analysis between two competing public corporations?",
        "options": {
            "A": "Both companies operate in the same industry and report under IFRS using straight-line depreciation.",
            "B": "One company operates as a multi-industry conglomerate and uses LIFO inventory accounting under US GAAP, while the competitor is a pure-play firm using FIFO under IFRS.",
            "C": "Both companies utilize the direct method to prepare their statement of cash flows with standard fiscal year ends."
        },
        "answer": "B",
        "explanation": "Key limitations of ratio analysis include differences in accounting methods (e.g., LIFO vs FIFO creates large differences in inventory turnover and profitability), differing regulatory frameworks (US GAAP vs IFRS), and conglomerate structures where consolidated ratios aggregate wildly different industry segments. Comparing a LIFO US GAAP conglomerate against a FIFO IFRS pure-play firm introduces major distortions that require extensive analytical restatements.\n\nDistractor Analysis:\n- A represents high comparability (same industry, same standard, same depreciation method).\n- C represents highly comparable cash flow reporting."
    },
    {
        "id": "L1-Q090",
        "level": 1,
        "module": "m6-ratios",
        "topic": "Financial Analysis Techniques",
        "los": "LOS 25.b: Calculate and interpret activity, liquidity, solvency, and profitability ratios.",
        "question": "In financial statement analysis, business risk is distinct from financial risk. Which of the following statements correctly differentiates between the two?",
        "options": {
            "A": "Business risk arises from the uncertainty regarding operating earnings driven by sales variability and fixed operating costs (operating leverage), whereas financial risk arises from the use of debt financing.",
            "B": "Business risk relates exclusively to fluctuations in market interest rates and foreign exchange rates, whereas financial risk relates to inventory obsolescence.",
            "C": "Business risk is measured by the debt-to-equity ratio, whereas financial risk is measured by the degree of operating leverage."
        },
        "answer": "A",
        "explanation": "Business risk is the risk inherent in the company's operations, comprising sales risk (uncertainty of demand and output prices) and operating risk (uncertainty driven by the presence of fixed operating costs, known as operating leverage). It is reflected in the variability of operating income (EBIT). Financial risk is the additional risk placed on common shareholders as a result of using debt financing and fixed financial obligations (financial leverage).\n\nDistractor Analysis:\n- B misclassifies interest rate/FX risk and inventory risks.\n- C reverses the definitions and metrics of business risk and financial risk."
    }
]
