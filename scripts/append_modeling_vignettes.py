import json
import os
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
PART3_PATH = os.path.join(DATA_DIR, "l2_questions_part3.json")

def get_new_modeling_questions():
    questions = []

    # =========================================================================
    # VIGNETTE 45: Solaria Dynamics
    # Topic: Financial Statement Modeling and Multi-Year Forecasting
    # =========================================================================
    v45_id = "V45"
    v45_title = "Solaria Dynamics: Top-Down vs. Bottom-Up Revenue Modeling and Operating Leverage"
    v45_text = (
        "Solaria Dynamics is a global manufacturer of advanced photovoltaic solar inverters and energy storage "
        "power conversion systems. Equity research analyst Daniel Vance, CFA, is constructing a multi-year pro forma "
        "earnings model for Solaria for Fiscal 2025 through Fiscal 2027.\n\n"
        "Exhibit 1: Solaria Historical Data (2024) and Industry Projections (in millions of USD)\n"
        "- 2024 Actual Revenue = 800 USD\n"
        "- 2024 Actual Global Industry Market Size = 8,000 USD (Solaria market share = 10.0%)\n"
        "- Projected 2025 Global Industry Growth Rate = 15.0%\n"
        "- Projected 2025 Solaria Market Share Expansion = +1.0% (to 11.0% of global market)\n"
        "- 2024 Cost of Goods Sold (COGS) = 520 USD (comprising 360 USD variable costs and 160 USD fixed manufacturing overhead)\n"
        "- 2024 Selling, General, and Administrative (SG&A) = 140 USD (comprising 40 USD variable sales commissions and 100 USD fixed overhead)\n"
        "- 2024 Operating Income (EBIT) = 140 USD\n\n"
        "Vance evaluates both top-down and bottom-up forecasting frameworks to determine projected revenue growth, cost scaling, and degree of operating leverage (DOL)."
    )

    questions.append({
        "id": "L2-V45-Q1",
        "level": 2,
        "module": "m18-integration",
        "topic": "Financial Statement Modeling and Multi-Year Forecasting",
        "vignette_id": v45_id,
        "vignette_title": v45_title,
        "vignette_text": v45_text,
        "los": "Compare top-down and bottom-up approaches to revenue forecasting.",
        "question": "Using the top-down market share approach based on Exhibit 1, Solaria's projected revenue for Fiscal 2025 is closest to:",
        "options": {
            "A": "880.0 million USD",
            "B": "920.0 million USD",
            "C": "1,012.0 million USD"
        },
        "answer": "C",
        "explanation": (
            "Step 1: Compute projected 2025 global industry market size:\n"
            "$$\\text{Projected Industry Market} = 8,000 \\times (1 + 0.15) = 9,200\\text{ million USD}$$\n\n"
            "Step 2: Apply projected market share of 11.0%:\n"
            "$$\\text{Projected Revenue} = 9,200 \\times 0.110 = 1,012.0\\text{ million USD}$$\n\n"
            "Under a top-down market share approach, the analyst first forecasts macroeconomic and industry growth, then applies expected market share shifts to derive firm revenue. "
            "Option A (880 million USD) assumes only an arbitrary 10% company growth rate. "
            "Option B (920 million USD) applies 15% growth directly to 2024 revenue ($800 \\times 1.15 = 920$) without accounting for market share expansion from 10% to 11%."
        )
    })

    questions.append({
        "id": "L2-V45-Q2",
        "level": 2,
        "module": "m18-integration",
        "topic": "Financial Statement Modeling and Multi-Year Forecasting",
        "vignette_id": v45_id,
        "vignette_title": v45_title,
        "vignette_text": v45_text,
        "los": "Demonstrate the effects of fixed and variable cost structures on gross margin and operating leverage.",
        "question": "Assuming Solaria's variable costs scale strictly in proportion to revenue while fixed overhead costs remain unchanged at 260 million USD (160 fixed COGS + 100 fixed SG&A), Solaria's projected 2025 operating income (EBIT) on projected revenue of 1,012.0 million USD is closest to:",
        "options": {
            "A": "177.1 million USD",
            "B": "246.0 million USD",
            "C": "294.0 million USD"
        },
        "answer": "B",
        "explanation": (
            "Step 1: Calculate 2024 variable cost ratio relative to revenue:\n"
            "$$\\text{Variable COGS Ratio} = \\frac{360}{800} = 45.0\\%$$\n"
            "$$\\text{Variable SG&A Ratio} = \\frac{40}{800} = 5.0\\%$$\n"
            "$$\\text{Total Variable Cost Ratio} = 45.0\\% + 5.0\\% = 50.0\\%$$\n\n"
            "Step 2: Calculate projected 2025 variable costs on 1,012.0 million USD revenue:\n"
            "$$\\text{Projected Variable Costs} = 1,012.0 \\times 50.0\\% = 506.0\\text{ million USD}$$\n\n"
            "Step 3: Calculate projected 2025 EBIT:\n"
            "$$\\text{EBIT} = \\text{Revenue} - \\text{Variable Costs} - \\text{Fixed Costs}$$\n"
            "$$\\text{EBIT} = 1,012.0 - 506.0 - (160 + 100) = 1,012.0 - 506.0 - 260.0 = 246.0\\text{ million USD}$$\n\n"
            "Notice that EBIT expands from 140 million USD to 246 million USD (+75.7%) on a 26.5% revenue increase, illustrating substantial operating leverage due to fixed cost dilution."
        )
    })

    questions.append({
        "id": "L2-V45-Q3",
        "level": 2,
        "module": "m18-integration",
        "topic": "Financial Statement Modeling and Multi-Year Forecasting",
        "vignette_id": v45_id,
        "vignette_title": v45_title,
        "vignette_text": v45_text,
        "los": "Demonstrate the calculation and interpretation of the degree of operating leverage (DOL).",
        "question": "Solaria's Degree of Operating Leverage (DOL) at its 2024 revenue base of 800 million USD is closest to:",
        "options": {
            "A": "1.86",
            "B": "2.86",
            "C": "3.86"
        },
        "answer": "B",
        "explanation": (
            "Step 1: Calculate contribution margin in 2024:\n"
            "$$\\text{Contribution Margin} = \\text{Revenue} - \\text{Variable Costs} = 800 - (360 + 40) = 400\\text{ million USD}$$\n\n"
            "Step 2: Calculate Degree of Operating Leverage (DOL):\n"
            "$$\\text{DOL} = \\frac{\\text{Contribution Margin}}{\\text{EBIT}} = \\frac{400}{140} \\approx 2.857$$\n\n"
            "A DOL of 2.86 indicates that for every 1.0% change in revenue, operating income changes by 2.86%, assuming fixed costs remain constant."
        )
    })

    questions.append({
        "id": "L2-V45-Q4",
        "level": 2,
        "module": "m18-integration",
        "topic": "Financial Statement Modeling and Multi-Year Forecasting",
        "vignette_id": v45_id,
        "vignette_title": v45_title,
        "vignette_text": v45_text,
        "los": "Explain how competitive dynamics and industry life cycles influence margin forecasts.",
        "question": "In Year 2027, Vance models aggressive pricing pressure from new competitor entrants. If competitors force a 10% decline in average selling prices (ASP) across Solaria's product lines while unit production volumes remain constant, the most likely impact on Solaria's gross profit margin is:",
        "options": {
            "A": "Gross profit margin contracts by more than 10 percentage points due to unabsorbed fixed manufacturing costs.",
            "B": "Gross profit margin expands because lower prices stimulate industry demand elasticity.",
            "C": "Gross profit margin contracts by exactly 10 percentage points because price cuts flow linearly to revenues."
        },
        "answer": "A",
        "explanation": (
            "Because manufacturing costs include substantial fixed overhead that does not decline when market selling prices drop, a 10% reduction in average selling prices compresses gross profit margin disproportionately.\n\n"
            "For example, if price falls from 100 to 90 USD per unit while variable costs (45 USD) and allocated fixed costs (20 USD) remain at 65 USD total:\n"
            "- Initial Gross Margin: $\\frac{100 - 65}{100} = 35.0\\%$\n"
            "- New Gross Margin: $\\frac{90 - 65}{90} = \\frac{25}{90} = 27.78\\%$\n"
            "The gross margin contracts by 7.22 percentage points (a 20.6% relative collapse). When price deflation hits high-fixed-cost producers, gross margin contraction is magnified beyond the nominal price reduction."
        )
    })

    questions.append({
        "id": "L2-V45-Q5",
        "level": 2,
        "module": "m18-integration",
        "topic": "Financial Statement Modeling and Multi-Year Forecasting",
        "vignette_id": v45_id,
        "vignette_title": v45_title,
        "vignette_text": v45_text,
        "los": "Identify behavioral biases in financial statement modeling and revenue forecasting.",
        "question": "During a research committee meeting, Vance's managing director points out that Vance has projected 15% to 25% annual revenue growth for Solaria for the next 7 consecutive years, identical to the company's prior 2-year early growth phase. Vance exhibits which behavioral bias?",
        "options": {
            "A": "Conservatism bias, by failing to revise beliefs sufficiently in response to new data.",
            "B": "Base-rate neglect and anchoring bias, by overweighting recent firm-specific growth while ignoring historical industry growth moderation curves.",
            "C": "Loss aversion bias, by disproportionately seeking to avoid forecast downgrades."
        },
        "answer": "B",
        "explanation": (
            "Projecting early-stage hypergrowth indefinitely without factoring in the base rate of industry maturity, product cycle deceleration, or competitive entry is a textbook manifestation of base-rate neglect combined with anchoring on recent historical growth rates. "
            "Empirical corporate life cycle studies show that corporate growth rates mean-revert rapidly toward nominal GDP growth."
        )
    })

    # =========================================================================
    # VIGNETTE 46: Vanguard Industrial Robotics
    # Topic: Financial Statement Modeling and Multi-Year Forecasting
    # =========================================================================
    v46_id = "V46"
    v46_title = "Vanguard Industrial Robotics: Working Capital Schedules & PP&E Roll-Forward Modeling"
    v46_text = (
        "Vanguard Industrial Robotics manufactures precision automated assembly machines. Financial modeling "
        "specialist Elena Rostova, CFA, is building an integrated working capital and capital expenditure projection schedule "
        "for Fiscal 2025.\n\n"
        "Exhibit 1: Vanguard Financial Statement Excerpts and Operating Parameters (in millions of USD)\n"
        "- 2024 Actual Revenue = 1,200 USD; 2025 Projected Revenue = 1,460 USD\n"
        "- 2024 Actual Cost of Goods Sold (COGS) = 730 USD; 2025 Projected COGS = 876 USD\n"
        "- 2024 Year-End Balance Sheet Balances: Accounts Receivable = 150 USD; Inventory = 120 USD; Accounts Payable = 100 USD\n"
        "- Target Activity Ratios for 2025 (using 365 days):\n"
        "  * Days Sales Outstanding (DSO) = 45.0 days\n"
        "  * Days of Inventory on Hand (DOH) = 55.0 days\n"
        "  * Days Payable Outstanding (DPO) = 50.0 days\n"
        "- Beginning Gross PP&E (2024 Year-End) = 1,000 USD; Accumulated Depreciation = 400 USD (Net PP&E = 600 USD)\n"
        "- Existing PP&E Depreciation Rate = 10% of Beginning Gross PP&E\n"
        "- 2025 Planned Capital Expenditures: Maintenance CapEx = 50 USD; Growth CapEx = 70 USD (Total CapEx = 120 USD)\n"
        "- First-year depreciation on new CapEx is modeled at 5% (reflecting half-year convention)."
    )

    questions.append({
        "id": "L2-V46-Q1",
        "level": 2,
        "module": "m18-integration",
        "topic": "Financial Statement Modeling and Multi-Year Forecasting",
        "vignette_id": v46_id,
        "vignette_title": v46_title,
        "vignette_text": v46_text,
        "los": "Demonstrate the projection of working capital items using activity ratios.",
        "question": "Based on Exhibit 1, Vanguard's projected Accounts Receivable and Inventory balances at year-end 2025 are closest to:",
        "options": {
            "A": "Accounts Receivable = 180.0 million USD; Inventory = 132.0 million USD",
            "B": "Accounts Receivable = 180.0 million USD; Inventory = 120.0 million USD",
            "C": "Accounts Receivable = 160.0 million USD; Inventory = 145.0 million USD"
        },
        "answer": "A",
        "explanation": (
            "Step 1: Calculate projected Accounts Receivable using DSO:\n"
            "$$\\text{Accounts Receivable}_{2025} = \\frac{\\text{DSO} \\times \\text{Revenue}_{2025}}{365} = \\frac{45.0 \\times 1,460}{365} = 180.0\\text{ million USD}$$\n\n"
            "Step 2: Calculate projected Inventory using DOH and projected COGS:\n"
            "$$\\text{Inventory}_{2025} = \\frac{\\text{DOH} \\times \\text{COGS}_{2025}}{365} = \\frac{55.0 \\times 876}{365} = 132.0\\text{ million USD}$$\n\n"
            "Thus, Accounts Receivable is 180.0 million USD and Inventory is 132.0 million USD."
        )
    })

    questions.append({
        "id": "L2-V46-Q2",
        "level": 2,
        "module": "m18-integration",
        "topic": "Financial Statement Modeling and Multi-Year Forecasting",
        "vignette_id": v46_id,
        "vignette_title": v46_title,
        "vignette_text": v46_text,
        "los": "Demonstrate the impact of working capital changes on cash flow from operations.",
        "question": "Based on Exhibit 1, if projected Accounts Payable for 2025 is 120.0 million USD (calculated as $\\frac{50.0 \\times 876}{365}$), the projected net cash outflow (inflow) from changes in operating working capital (AR + Inventory - AP) in 2025 is closest to:",
        "options": {
            "A": "Cash inflow of 22.0 million USD",
            "B": "Cash outflow of 22.0 million USD",
            "C": "Cash outflow of 42.0 million USD"
        },
        "answer": "B",
        "explanation": (
            "Step 1: Calculate 2024 Operating Working Capital:\n"
            "$$\\text{OWC}_{2024} = \\text{AR} + \\text{Inventory} - \\text{AP} = 150 + 120 - 100 = 170.0\\text{ million USD}$$\n\n"
            "Step 2: Calculate 2025 Operating Working Capital:\n"
            "$$\\text{OWC}_{2025} = 180.0 + 132.0 - 120.0 = 192.0\\text{ million USD}$$\n\n"
            "Step 3: Calculate Change in Operating Working Capital:\n"
            "$$\\Delta \\text{OWC} = 192.0 - 170.0 = +22.0\\text{ million USD}$$\n\n"
            "Because operating working capital increased by 22.0 million USD, cash was absorbed by operational assets, creating a net cash OUTFLOW of 22.0 million USD on the statement of cash flows."
        )
    })

    questions.append({
        "id": "L2-V46-Q3",
        "level": 2,
        "module": "m18-integration",
        "topic": "Financial Statement Modeling and Multi-Year Forecasting",
        "vignette_id": v46_id,
        "vignette_title": v46_title,
        "vignette_text": v46_text,
        "los": "Demonstrate the construction of a property, plant, and equipment (PP&E) schedule in a financial model.",
        "question": "Based on Exhibit 1, Vanguard's projected total depreciation expense for 2025 and ending Net PP&E carrying balance at year-end 2025 are closest to:",
        "options": {
            "A": "Total Depreciation = 106.0 million USD; Ending Net PP&E = 614.0 million USD",
            "B": "Total Depreciation = 100.0 million USD; Ending Net PP&E = 620.0 million USD",
            "C": "Total Depreciation = 120.0 million USD; Ending Net PP&E = 600.0 million USD"
        },
        "answer": "A",
        "explanation": (
            "Step 1: Calculate 2025 depreciation expense:\n"
            "- Depreciation on existing PP&E: $10\\% \\times 1,000\\text{ Gross PP&E} = 100.0\\text{ million USD}$\n"
            "- First-year depreciation on new CapEx (half-year convention): $5\\% \\times 120 = 6.0\\text{ million USD}$\n"
            "$$\\text{Total Depreciation}_{2025} = 100.0 + 6.0 = 106.0\\text{ million USD}$$\n\n"
            "Step 2: Roll forward Net PP&E balance:\n"
            "$$\\text{Ending Net PP&E} = \\text{Beginning Net PP&E} + \\text{Total CapEx} - \\text{Depreciation}$$\n"
            "$$\\text{Ending Net PP&E} = 600.0 + 120.0 - 106.0 = 614.0\\text{ million USD}$$\n\n"
            "Total Depreciation is 106.0 million USD and ending Net PP&E is 614.0 million USD."
        )
    })

    questions.append({
        "id": "L2-V46-Q4",
        "level": 2,
        "module": "m18-integration",
        "topic": "Financial Statement Modeling and Multi-Year Forecasting",
        "vignette_id": v46_id,
        "vignette_title": v46_title,
        "vignette_text": v46_text,
        "los": "Distinguish between maintenance and growth capital expenditures in financial forecasting.",
        "question": "In evaluating Vanguard's capital investment profile, Rostova segregates maintenance CapEx (50 million USD) from growth CapEx (70 million USD). Which of the following analytical statements regarding this segregation is most accurate?",
        "options": {
            "A": "Maintenance CapEx is required to maintain the current operational capacity and replace worn assets, whereas growth CapEx expands future productive capacity and supports projected revenue growth.",
            "B": "Maintenance CapEx is capitalized on the balance sheet while growth CapEx must be expensed immediately through the income statement under IFRS.",
            "C": "Maintenance CapEx reduces Cash Flow from Operations (CFO), while growth CapEx is classified in Cash Flow from Financing (CFF)."
        },
        "answer": "A",
        "explanation": (
            "Maintenance CapEx represents the capital required to sustain current business operations, replace obsolete machinery, and preserve competitive standing (often benchmarked against economic depreciation). "
            "Growth CapEx represents discretionary investments to expand operational capacity, build new facilities, or acquire technology to generate future incremental revenue. "
            "Both forms are capitalized on the balance sheet within PP&E and reported under Cash Flow from Investing (CFI)."
        )
    })

    questions.append({
        "id": "L2-V46-Q5",
        "level": 2,
        "module": "m18-integration",
        "topic": "Financial Statement Modeling and Multi-Year Forecasting",
        "vignette_id": v46_id,
        "vignette_title": v46_title,
        "vignette_text": v46_text,
        "los": "Demonstrate how fixed asset turnover and capacity constraints limit multi-year revenue projections.",
        "question": "Vanguard's manufacturing plants operate at maximum design capacity when annual revenue reaches 2.5x Gross PP&E. If Gross PP&E increases to 1,120 million USD in 2025, Vanguard's maximum achievable revenue before requiring additional facility expansion is:",
        "options": {
            "A": "2,240 million USD",
            "B": "2,800 million USD",
            "C": "3,360 million USD"
        },
        "answer": "B",
        "explanation": (
            "$$\\text{Maximum Capacity Revenue} = 2.5 \\times \\text{Gross PP&E} = 2.5 \\times 1,120 = 2,800\\text{ million USD}$$\n\n"
            "In multi-year financial modeling, analysts must cross-verify revenue growth trajectories against physical capacity limits. When projected revenues approach maximum asset utilization thresholds, the model must incorporate incremental growth CapEx step-functions (facility construction) to avoid projecting mathematically impossible production volumes."
        )
    })

    # =========================================================================
    # VIGNETTE 47: Aegis Telecommunications
    # Topic: Financial Statement Modeling and Multi-Year Forecasting
    # =========================================================================
    v47_id = "V47"
    v47_title = "Aegis Telecommunications: Pro Forma 3-Statement Integration, Debt Schedules & Circularity Resolution"
    v47_text = (
        "Aegis Telecommunications is a national fiber broadband network operator. Senior financial analyst "
        "Liam Thorne, CFA, is constructing a multi-year pro forma integrated three-statement financial model for Aegis "
        "to assess credit metrics and debt repayment capacity.\n\n"
        "Exhibit 1: Aegis Baseline Financial Data (in millions of USD)\n"
        "- 2025 Projected Operating Income (EBIT) = 300 USD\n"
        "- Marginal Corporate Tax Rate = 25%\n"
        "- Beginning Debt Balance (Jan 1, 2025) = 1,000 USD; Contractual mandatory principal repayment on Dec 31, 2025 = 100 USD\n"
        "- Stated interest rate on debt = 6.0% per annum\n"
        "- Beginning Cash Balance (Jan 1, 2025) = 80 USD; Minimum target operational cash balance = 50 USD\n"
        "- Interest earned on cash balances = 2.0% per annum\n"
        "- Free Cash Flow before Debt Financing and Discretionary Sweep = 180 USD\n\n"
        "Thorne must decide whether to model interest expense using beginning debt balances or average debt balances, "
        "and evaluate how circular references arise in automated financial models."
    )

    questions.append({
        "id": "L2-V47-Q1",
        "level": 2,
        "module": "m18-integration",
        "topic": "Financial Statement Modeling and Multi-Year Forecasting",
        "vignette_id": v47_id,
        "vignette_title": v47_title,
        "vignette_text": v47_text,
        "los": "Demonstrate the construction of a debt schedule and interest expense modeling.",
        "question": "Under standard financial modeling practice using the average debt balance during the period, Aegis's projected gross interest expense for 2025 is closest to:",
        "options": {
            "A": "54.0 million USD",
            "B": "57.0 million USD",
            "C": "60.0 million USD"
        },
        "answer": "B",
        "explanation": (
            "Step 1: Determine beginning and ending debt balances:\n"
            "- Beginning Debt = 1,000 million USD\n"
            "- Ending Debt = $1,000 - 100\\text{ mandatory repayment} = 900\\text{ million USD}$\n\n"
            "Step 2: Calculate average debt balance:\n"
            "$$\\text{Average Debt} = \\frac{1,000 + 900}{2} = 950.0\\text{ million USD}$$\n\n"
            "Step 3: Calculate gross interest expense at 6.0%:\n"
            "$$\\text{Interest Expense} = 950.0 \\times 6.0\\% = 57.0\\text{ million USD}$$\n\n"
            "Option A (54.0 million USD) applies 6.0% to ending debt ($900 \\times 0.06$). Option C (60.0 million USD) applies 6.0% strictly to beginning debt ($1,000 \\times 0.06$)."
        )
    })

    questions.append({
        "id": "L2-V47-Q2",
        "level": 2,
        "module": "m18-integration",
        "topic": "Financial Statement Modeling and Multi-Year Forecasting",
        "vignette_id": v47_id,
        "vignette_title": v47_title,
        "vignette_text": v47_text,
        "los": "Explain circular references in financial modeling and methods to resolve them.",
        "question": "Why does calculating interest expense and interest income based on average balances create a circular reference in an integrated three-statement model?",
        "options": {
            "A": "Because taxes depend on EBITDA, which depends on non-operating working capital.",
            "B": "Because interest expense determines net income and cash flow, which dictates ending cash/debt, which in turn determines the average debt/cash balance that defines interest expense.",
            "C": "Because the cash sweep requires equity repurchases that violate the clean surplus relationship."
        },
        "answer": "B",
        "explanation": (
            "A circular reference occurs because:\n"
            "1. Average debt/cash balance determines interest expense and interest income on the income statement.\n"
            "2. Interest expense directly feeds Net Income, which determines Cash Flow from Operations.\n"
            "3. Cash Flow determines the ending cash balance and how much debt is paid down via the cash sweep.\n"
            "4. Ending debt/cash changes the average debt/cash balance, looping back to step 1.\n\n"
            "To resolve or prevent model instability, analysts frequently base interest calculations on beginning-of-period balances or introduce an iterative calculation circuit-breaker toggle."
        )
    })

    questions.append({
        "id": "L2-V47-Q3",
        "level": 2,
        "module": "m18-integration",
        "topic": "Financial Statement Modeling and Multi-Year Forecasting",
        "vignette_id": v47_id,
        "vignette_title": v47_title,
        "vignette_text": v47_text,
        "los": "Demonstrate the mechanics of a cash sweep in financial statement modeling.",
        "question": "Aegis's credit agreement mandates a 100% excess cash sweep to prepay prepayable debt, subject to retaining a minimum operational cash balance of 50 million USD. If beginning cash is 80 million USD and net cash generated before optional debt paydown is 120 million USD, the amount of debt prepaid via the discretionary cash sweep is closest to:",
        "options": {
            "A": "120.0 million USD",
            "B": "150.0 million USD",
            "C": "180.0 million USD"
        },
        "answer": "B",
        "explanation": (
            "Step 1: Determine total cash available before discretionary sweep:\n"
            "$$\\text{Total Cash Available} = \\text{Beginning Cash} + \\text{Net Cash Generated} = 80 + 120 = 200.0\\text{ million USD}$$\n\n"
            "Step 2: Determine excess cash over minimum operational cash buffer:\n"
            "$$\\text{Minimum Cash Required} = 50.0\\text{ million USD}$$\n"
            "$$\\text{Excess Cash for Sweep} = 200.0 - 50.0 = 150.0\\text{ million USD}$$\n\n"
            "Under a 100% sweep, the entire 150.0 million USD of excess liquidity is directed toward prepaying debt, leaving exactly the minimum operational buffer of 50 million USD in cash on the balance sheet."
        )
    })

    questions.append({
        "id": "L2-V47-Q4",
        "level": 2,
        "module": "m18-integration",
        "topic": "Financial Statement Modeling and Multi-Year Forecasting",
        "vignette_id": v47_id,
        "vignette_title": v47_title,
        "vignette_text": v47_text,
        "los": "Explain the role of plug variables in balancing pro forma balance sheets.",
        "question": "When balancing a pro forma balance sheet in an integrated financial model without circular debt logic, the analyst should most appropriately use which plug variable when projected assets exceed projected liabilities and equity?",
        "options": {
            "A": "Cash buffer (as an asset plug) to accumulate surplus liquidity.",
            "B": "Revolving credit facility (or short-term debt) as a liability plug to fund the capital shortfall.",
            "C": "Additional paid-in capital (APIC) as an equity plug to absorb operational deficits."
        },
        "answer": "B",
        "explanation": (
            "When projected assets exceed projected liabilities and equity (Assets > Liabilities + Equity), the company has an unfinanced funding deficit. "
            "To make the balance sheet balance (Assets = Liabilities + Equity), a financing liability plug—typically a revolving credit facility or short-term borrowing—must increase to provide the required debt capital. "
            "Conversely, if Liabilities + Equity > Assets, the company has surplus liquidity, and cash serves as the asset plug."
        )
    })

    questions.append({
        "id": "L2-V47-Q5",
        "level": 2,
        "module": "m18-integration",
        "topic": "Financial Statement Modeling and Multi-Year Forecasting",
        "vignette_id": v47_id,
        "vignette_title": v47_title,
        "vignette_text": v47_text,
        "los": "Synthesize the effect of financial leverage reductions on Return on Equity (ROE).",
        "question": "If Aegis aggressively deploys all excess cash flows over the next 3 years to prepay 500 million USD of debt, which of the following impacts on Aegis's financial ratios is most likely, assuming operating earnings (EBIT) remain constant and the cost of debt is below ROA?",
        "options": {
            "A": "Interest coverage ratio improves; Return on Equity (ROE) declines.",
            "B": "Interest coverage ratio deteriorates; Return on Equity (ROE) increases.",
            "C": "Both interest coverage ratio and Return on Equity (ROE) increase simultaneously."
        },
        "answer": "A",
        "explanation": (
            "1. Interest coverage (EBIT / Interest Expense): Paying down 500 million USD of debt reduces annual interest expense, causing interest coverage to improve substantially (credit solvency improves).\n"
            "2. Return on Equity (ROE): Because ROA exceeds the borrowing cost of debt, positive financial leverage previously magnified ROE. Deleveraging the capital structure shrinks the financial leverage multiplier (Assets / Equity), causing ROE to decrease toward ROA, even though financial risk is lowered."
        )
    })

    # =========================================================================
    # VIGNETTE 48: BioHealth Diagnostics
    # Topic: Financial Statement Modeling and Multi-Year Forecasting
    # =========================================================================
    v48_id = "V48"
    v48_title = "BioHealth Diagnostics: Scenario Analysis, Monte Carlo Simulation & Long-Run Growth Bounds"
    v48_text = (
        "BioHealth Diagnostics is a commercial-stage molecular diagnostic tools developer. Senior healthcare "
        "analyst Dr. Marcus Vance, CFA, is constructing a multi-year valuation model for BioHealth's flagship gene-sequencing "
        "diagnostic platform.\n\n"
        "Exhibit 1: Key Pro Forma Modeling Assumptions and Economic Bounds\n"
        "- Explicit Forecast Period: 5 years (2025 to 2029)\n"
        "- Year 5 (2029) Projected Free Cash Flow to Firm (FCFF) = 240 USD\n"
        "- Weighted Average Cost of Capital (WACC) = 9.0%\n"
        "- Long-term sustainable nominal GDP growth rate of the global economy = 3.5%\n"
        "- Three Discrete Operational Scenarios Modeled for Year 1 to 5:\n"
        "  * Bull Case (Probability = 25%): 22% Revenue CAGR, 32% Operating Margin\n"
        "  * Base Case (Probability = 50%): 14% Revenue CAGR, 25% Operating Margin\n"
        "  * Bear Case (Probability = 25%): 4% Revenue CAGR, 15% Operating Margin\n"
        "- BioHealth has a bank credit agreement with a strict maximum debt covenant of $\\text{Total Debt} / \\text{EBITDA} \\le 3.5\\times$.\n\n"
        "Vance incorporates scenario analysis and a 10,000-trial Monte Carlo simulation to quantify covenant breach probabilities "
        "and tests the economic validity of terminal growth rate assumptions."
    )

    questions.append({
        "id": "L2-V48-Q1",
        "level": 2,
        "module": "m18-integration",
        "topic": "Financial Statement Modeling and Multi-Year Forecasting",
        "vignette_id": v48_id,
        "vignette_title": v48_title,
        "vignette_text": v48_text,
        "los": "Compare scenario analysis, sensitivity analysis, and simulation in financial modeling.",
        "question": "What is the primary methodological distinction between scenario analysis and sensitivity analysis in financial statement modeling?",
        "options": {
            "A": "Sensitivity analysis changes one input variable at a time holding all others constant, whereas scenario analysis defines mutually consistent simultaneous changes across multiple correlated variables.",
            "B": "Scenario analysis assigns continuous probability distributions to all variables, whereas sensitivity analysis only uses historical standard deviations.",
            "C": "Sensitivity analysis can only be applied to balance sheet items, whereas scenario analysis is exclusive to the income statement."
        },
        "answer": "A",
        "explanation": (
            "Sensitivity analysis evaluates the marginal effect of changing a single key variable (e.g., selling price or discount rate) while holding all other inputs ceteris paribus. "
            "Scenario analysis recognizes that economic shifts rarely occur in isolation; it models discrete economic states (Bull, Base, Bear) where multiple correlated variables "
            "(e.g., sales volume, price realization, raw material inflation, and interest rates) change simultaneously in a mutually consistent manner."
        )
    })

    questions.append({
        "id": "L2-V48-Q2",
        "level": 2,
        "module": "m18-integration",
        "topic": "Financial Statement Modeling and Multi-Year Forecasting",
        "vignette_id": v48_id,
        "vignette_title": v48_title,
        "vignette_text": v48_text,
        "los": "Explain the economic constraints on terminal growth rates in multi-stage DCF models.",
        "question": "An associate analyst recommends using a perpetual terminal growth rate ($g$) of 5.5% for BioHealth in the Gordon Growth terminal value formula, arguing that the diagnostic tools sector has grown at 8% historically. Dr. Vance should reject this recommendation because:",
        "options": {
            "A": "A perpetual growth rate exceeding long-term nominal GDP growth (3.5%) mathematically implies the company will eventually become larger than the entire macroeconomy.",
            "B": "Perpetual terminal growth rates can never exceed the risk-free rate plus the equity risk premium.",
            "C": "IFRS explicitly caps terminal growth rates at zero percent for diagnostic technology companies."
        },
        "answer": "A",
        "explanation": (
            "In multi-stage discounted cash flow and financial modeling, the perpetual growth rate ($g$) applied into perpetuity cannot logically exceed the long-term sustainable nominal growth rate of the economy in which the firm operates (typically 2% to 4% nominal GDP growth). "
            "If a firm were modeled to grow perpetually faster than the global economy, its mathematical share of world output would eventually exceed 100%, which is economically impossible."
        )
    })

    questions.append({
        "id": "L2-V48-Q3",
        "level": 2,
        "module": "m18-integration",
        "topic": "Financial Statement Modeling and Multi-Year Forecasting",
        "vignette_id": v48_id,
        "vignette_title": v48_title,
        "vignette_text": v48_text,
        "los": "Explain the economic rationale for Return on Invested Capital (ROIC) convergence toward WACC.",
        "question": "In formulating continuing residual income and terminal year cash flows, modern financial modeling theory assumes that a firm's Return on Invested Capital (ROIC) will eventually converge toward its WACC over the long run because:",
        "options": {
            "A": "Accounting standards mandate straight-line depreciation of goodwill.",
            "B": "Excess economic rents (ROIC > WACC) inevitably attract new competitive entrants, capital investment, and technological imitation that erode abnormal margins.",
            "C": "Central bank monetary policy forces corporate debt interest rates to equal ROIC."
        },
        "answer": "B",
        "explanation": (
            "Under Porter's competitive forces and economic equilibrium theory, high abnormal returns on capital (ROIC in excess of the cost of capital, WACC) generate economic rents that incentivize competitors to enter the industry, expand supply, duplicate technologies, and bid down prices. "
            "Unless protected by an insurmountable economic moat, competitive market dynamics cause industry returns on capital to fade toward the cost of capital over the terminal horizon."
        )
    })

    questions.append({
        "id": "L2-V48-Q4",
        "level": 2,
        "module": "m18-integration",
        "topic": "Financial Statement Modeling and Multi-Year Forecasting",
        "vignette_id": v48_id,
        "vignette_title": v48_title,
        "vignette_text": v48_text,
        "los": "Interpret the outputs of a Monte Carlo simulation in financial risk modeling.",
        "question": "Vance runs a 10,000-trial Monte Carlo simulation on BioHealth's integrated model, varying pricing, volume, and unit manufacturing costs across normal distributions. The simulation reveals that 650 trials result in a $\\text{Total Debt} / \\text{EBITDA}$ ratio exceeding $3.5\\times$. The implied probability of covenant breach is closest to:",
        "options": {
            "A": "0.65%",
            "B": "6.50%",
            "C": "13.00%"
        },
        "answer": "B",
        "explanation": (
            "$$\\text{Empirical Breach Probability} = \\frac{\\text{Breach Trials}}{\\text{Total Trials}} = \\frac{650}{10,000} = 6.50\\%$$\n\n"
            "Monte Carlo simulation allows analysts to transform deterministic static point estimates into full continuous probability distributions. A 6.50% probability provides the investment committee with quantitative insight into tail-risk covenant insolvency under stochastic operating volatility."
        )
    })

    questions.append({
        "id": "L2-V48-Q5",
        "level": 2,
        "module": "m18-integration",
        "topic": "Financial Statement Modeling and Multi-Year Forecasting",
        "vignette_id": v48_id,
        "vignette_title": v48_title,
        "vignette_text": v48_text,
        "los": "Identify analyst cognitive biases and heuristics in financial forecasts.",
        "question": "After BioHealth's management provides ambitious five-year margin guidance during an investor day, Vance actively gathers industry articles praising BioHealth's leadership while disregarding FDA inspection warning letters and clinical trial delay reports. Vance is primarily demonstrating:",
        "options": {
            "A": "Confirmation bias",
            "B": "Availability heuristic",
            "C": "Endowment effect"
        },
        "answer": "A",
        "explanation": (
            "Confirmation bias is the cognitive heuristic wherein an analyst selectively seeks out, emphasizes, and validates information that conforms to their preconceived belief or management's narrative, while actively filtering out, discounting, or ignoring contradictory evidence (such as regulatory warnings or trial delays). "
            "In financial statement modeling, confirmation bias leads to systematically overstated forecasts and underappreciated downside risk."
        )
    })

    return questions

def run_append():
    with open(PART3_PATH, "r", encoding="utf-8") as f:
        existing_qs = json.load(f)

    existing_ids = set(q["id"] for q in existing_qs)
    print(f"Existing questions in part3: {len(existing_qs)}")

    new_qs = get_new_modeling_questions()
    print(f"Generated {len(new_qs)} new modeling questions (V45 to V48).")

    # Delimiter and bare dollar checks
    re_display = re.compile(r'\$\$.*?\$\$', re.DOTALL)
    re_inline = re.compile(r'(?<!\\)\$.*?(?<!\\)\$')
    
    for q in new_qs:
        qid = q["id"]
        assert qid not in existing_ids, f"Duplicate ID: {qid}"
        assert q["answer"] in ["A", "B", "C"]
        assert set(q["options"].keys()) == {"A", "B", "C"}
        
        for field in ["question", "explanation", "vignette_text"]:
            val = q[field]
            if val.count("$$") % 2 != 0:
                raise ValueError(f"Unbalanced $$ in {qid} {field}")
            cleaned = val.replace("$$", "").replace(r"\$", "")
            if cleaned.count("$") % 2 != 0:
                raise ValueError(f"Unbalanced inline $ in {qid} {field}")
            
            no_disp = re_display.sub("", val)
            no_inl = re_inline.sub("", no_disp)
            no_esc = no_inl.replace(r"\$", "")
            if "$" in no_esc:
                raise ValueError(f"Bare unescaped $ found in {qid} {field}")

    print("All 20 new questions passed schema, KaTeX, and currency validation!")

    combined = existing_qs + new_qs
    print(f"Total part3 questions after appending: {len(combined)}")

    with open(PART3_PATH, "w", encoding="utf-8") as f:
        json.dump(combined, f, indent=2, ensure_ascii=False)

    print(f"Successfully saved updated part3 to {PART3_PATH}")

if __name__ == "__main__":
    run_append()
