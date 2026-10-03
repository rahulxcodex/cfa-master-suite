import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
EQ_PATH = os.path.join(BASE_DIR, "data", "fi_eq", "l1_equity.json")

with open(EQ_PATH, "r", encoding="utf-8") as f:
    existing_qs = json.load(f)

print(f"Current L1 EQ questions: {len(existing_qs)}")

new_questions = [
    # --- Module 7: Company Analysis: Forecasting (10 Qs: 086 to 095) ---
    {
        "id": "L1-EQ-086",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Company Analysis: Forecasting",
        "los": "Compare top-down, bottom-up, and hybrid approaches to forecasting revenue.",
        "question": "An equity research analyst projects an automobile manufacturer's revenue by first forecasting nominal global GDP growth, estimating total vehicle sales per unit of GDP, calculating the firm's projected market share, and multiplying by expected average selling price. This forecasting methodology is best characterized as a:",
        "options": {
            "A": "Pure bottom-up approach.",
            "B": "Top-down approach.",
            "C": "Hybrid consensus approach."
        },
        "answer": "B",
        "explanation": "A top-down approach begins at the macroeconomic aggregate level (GDP growth, interest rates), cascades down to total industry demand, and then projects the company's market share and average realized selling prices. In contrast, a bottom-up approach begins with individual product lines, store locations, or manufacturing plant capacities and aggregates upward.",
        "distractor_analysis": {
            "A": "Bottom-up forecasting starts with customer-level contracts or individual store unit metrics without starting from macroeconomic GDP aggregates.",
            "C": "A hybrid approach combines both top-down macro constraints with detailed bottom-up segment builds."
        }
    },
    {
        "id": "L1-EQ-087",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Company Analysis: Forecasting",
        "los": "Describe methods for forecasting costs and operating margins.",
        "question": "When forecasting a manufacturing firm's Cost of Goods Sold (COGS), the most appropriate modeling technique when economies of scale exist is to:",
        "options": {
            "A": "Model COGS as a strictly constant percentage of revenue.",
            "B": "Separate COGS into fixed overhead costs and variable per-unit direct costs.",
            "C": "Grow COGS at the long-term statutory corporate tax rate."
        },
        "answer": "B",
        "explanation": "When economies of scale exist, fixed manufacturing overhead (factory depreciation, plant maintenance) does not increase proportionally with production volume. Decomposing COGS into fixed and variable components accurately captures operating leverage, showing that gross margin expands as revenue rises.",
        "distractor_analysis": {
            "A": "Assuming a constant percentage of revenue fails to capture gross margin expansion resulting from scale economies.",
            "C": "Tax rates govern corporate income tax liabilities, not manufacturing production costs."
        }
    },
    {
        "id": "L1-EQ-088",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Company Analysis: Forecasting",
        "los": "Explain the concept and modeling of operating leverage.",
        "question": "A firm has high degree of operating leverage (DOL). If industry sales decline during an economic recession, the firm will experience:",
        "options": {
            "A": "A smaller percentage decline in operating income (EBIT) than in revenues.",
            "B": "A larger percentage decline in operating income (EBIT) than in revenues.",
            "C": "An increase in operating profit margin because variable costs drop to zero."
        },
        "answer": "B",
        "explanation": "Degree of Operating Leverage (DOL) measures the sensitivity of EBIT to revenue changes: $$\\text{DOL} = \\frac{\\% \\Delta \\text{EBIT}}{\\% \\Delta \\text{Revenue}} = \\frac{Q(P - V)}{Q(P - V) - F}$$ High fixed costs ($F$) amplify both upside and downside EBIT swings. When revenues fall, fixed costs must still be paid, causing EBIT to decline at a significantly greater percentage rate than revenues.",
        "distractor_analysis": {
            "A": "A smaller decline in EBIT occurs only when operating leverage is near zero or costs are 100% variable.",
            "C": "Operating profit margins contract severely during downcycles when fixed costs absorb a larger share of revenue."
        }
    },
    {
        "id": "L1-EQ-089",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Company Analysis: Forecasting",
        "los": "Describe working capital and capital expenditure forecasting.",
        "question": "In a pro forma financial model, working capital accounts such as Accounts Receivable and Inventory are most commonly forecasted by linking them to:",
        "options": {
            "A": "Days Sales Outstanding (DSO) and Days Sales of Inventory (DSI) relative to projected sales and COGS.",
            "B": "The firm's historical dividend payout ratio.",
            "C": "Long-term yield on benchmark sovereign bonds."
        },
        "answer": "A",
        "explanation": "Operating working capital scales with operational activity. Analysts forecast Accounts Receivable by assuming a target or historical Days Sales Outstanding ($\\text{DSO} = \\frac{\\text{AR}}{\\text{Sales}} \\times 365$) applied to projected sales, and Inventory by applying Days Sales of Inventory ($\\text{DSI} = \\frac{\\text{Inventory}}{\\text{COGS}} \\times 365$) to projected COGS.",
        "distractor_analysis": {
            "B": "The dividend payout ratio governs cash dividends to equity holders, not working capital operations.",
            "C": "Benchmark bond yields affect discount rates, not operational trade working capital turnover."
        }
    },
    {
        "id": "L1-EQ-090",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Company Analysis: Forecasting",
        "los": "Describe the factors influencing the choice of forecast horizon.",
        "question": "Which of the following firm characteristics justifies using a LONGER explicit forecast horizon (e.g., 10 to 15 years rather than 3 to 5 years)?",
        "options": {
            "A": "A mature consumer packaged goods company operating in a steady-state competitive market.",
            "B": "A cyclical mining enterprise or an early-stage infrastructure project with long-gestation multi-year asset builds.",
            "C": "A company facing imminent patent expiration with zero replacement pipeline products."
        },
        "answer": "B",
        "explanation": "The explicit forecast horizon should extend until the company reaches normalized steady-state growth and sustainable return on invested capital. Highly cyclical capital-intensive firms, concession infrastructure developers, or emerging growth biotech companies require longer forecast periods to capture full capital deployment and project maturation cycles.",
        "distractor_analysis": {
            "A": "Mature, steady-state firms can be accurately valued with standard short 3–5 year horizons.",
            "C": "Imminent loss of competitive moat truncates explicit growth modeling rather than extending it."
        }
    },
    {
        "id": "L1-EQ-091",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Company Analysis: Forecasting",
        "los": "Describe pro forma balance sheet balancing (the plug account).",
        "question": "When building an integrated 3-statement financial model, if projected assets exceed projected liabilities and shareholders' equity before financing decisions, the balancing 'plug' item is typically:",
        "options": {
            "A": "Additional external debt or equity financing (or a reduction in cash).",
            "B": "An automatic retroactive reduction in cost of goods sold.",
            "C": "A mandatory write-off of property, plant, and equipment."
        },
        "answer": "A",
        "explanation": "By the fundamental accounting equation, $\\text{Assets} = \\text{Liabilities} + \\text{Equity}$. If projected asset needs exceed internally generated equity and operating liabilities, the firm faces a financing deficit that must be plugged with external borrowing (revolver/debt) or equity issuance, or by depleting existing cash reserves.",
        "distractor_analysis": {
            "B": "Income statement operating costs cannot be arbitrarily adjusted to balance the balance sheet.",
            "C": "PP&E write-offs occur due to economic impairment, not mechanical balance sheet modeling balancing."
        }
    },
    {
        "id": "L1-EQ-092",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Company Analysis: Forecasting",
        "los": "Explain sensitivity analysis and scenario analysis in financial modeling.",
        "question": "In financial modeling, an analyst who changes one input variable (e.g., sales growth) across a range while keeping all other variables constant is conducting:",
        "options": {
            "A": "Scenario analysis.",
            "B": "Sensitivity analysis.",
            "C": "Monte Carlo simulation."
        },
        "answer": "B",
        "explanation": "Sensitivity analysis evaluates how the valuation or earnings outcome changes when a single underlying assumption is varied while all other variables remain ceteris paribus. In contrast, scenario analysis alters multiple correlated variables simultaneously to model discrete states of the world (e.g., bull, base, bear cases).",
        "distractor_analysis": {
            "A": "Scenario analysis modifies multiple variables together to reflect coherent alternative economic states.",
            "C": "Monte Carlo simulation draws thousands of random combinations based on assigned probability distributions."
        }
    },
    {
        "id": "L1-EQ-093",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Company Analysis: Forecasting",
        "los": "Explain the modeling of maintenance vs. growth capital expenditures.",
        "question": "Maintenance capital expenditure is best described as the investment required to:",
        "options": {
            "A": "Expand into adjacent geographic markets and launch new product lines.",
            "B": "Replace worn-out productive capacity and sustain current operational revenue levels.",
            "C": "Acquire controlling equity stakes in industry competitors."
        },
        "answer": "B",
        "explanation": "Maintenance CapEx represents the ongoing capital investments needed to sustain current productive assets, replace depreciated machinery, and preserve the company's existing competitive position. Growth CapEx is discretionary spending dedicated to expanding future production volume or entering new business segments.",
        "distractor_analysis": {
            "A": "Market expansion and new product lines represent discretionary growth CapEx.",
            "C": "Corporate acquisitions are classified as business combinations, not maintenance capital expenditures."
        }
    },
    {
        "id": "L1-EQ-094",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Company Analysis: Forecasting",
        "los": "Describe inflation passthrough in revenue and cost forecasting.",
        "question": "A company with strong brand loyalty, high pricing power, and inelastic demand will most likely respond to rising input cost inflation by:",
        "options": {
            "A": "Fully passing cost increases through to consumers via price increases, preserving gross margins.",
            "B": "Absorbing input cost increases, leading to severe gross margin compression.",
            "C": "Reducing product prices to capture market share."
        },
        "answer": "A",
        "explanation": "Firms possessing pricing power (an economic moat) can pass inflationary increases in raw materials and labor directly to end customers without suffering substantial volume declines. This insulates operating profit margins from cost inflation.",
        "distractor_analysis": {
            "B": "Absorbing cost increases occurs when companies produce undifferentiated commodities with elastic demand.",
            "C": "Lowering prices during input inflation would cause rapid profitability destruction."
        }
    },
    {
        "id": "L1-EQ-095",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Company Analysis: Forecasting",
        "los": "Explain financial modeling circularity.",
        "question": "Circularity in a 3-statement financial model typically arises because:",
        "options": {
            "A": "Revenue depends on historical depreciation expense.",
            "B": "Interest expense depends on the average debt balance, which depends on net cash flow, which itself depends on interest expense.",
            "C": "Shareholders' equity is independent of retained earnings."
        },
        "answer": "B",
        "explanation": "Circularity occurs when two accounts mutually determine each other: interest expense on the income statement lowers net income and operating cash flow, which dictates ending cash and required revolver debt borrowing, which in turn determines interest expense.",
        "distractor_analysis": {
            "A": "Revenue is modeled from demand and price, not from historical depreciation schedules.",
            "C": "Shareholders' equity directly links to net income via retained earnings."
        }
    },

    # --- Module 5: Company Analysis: Past & Present (7 Qs: 096 to 102) ---
    {
        "id": "L1-EQ-096",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Company Analysis: Past and Present",
        "los": "Describe return on invested capital (ROIC) and its role in competitive advantage.",
        "question": "A firm that consistently generates a Return on Invested Capital (ROIC) substantially in excess of its Weighted Average Cost of Capital (WACC) over multiple business cycles is best described as:",
        "options": {
            "A": "Operating in a perfectly competitive commodity industry.",
            "B": "Possessing a sustainable competitive advantage (economic moat).",
            "C": "Overleveraged with unsustainable financial risk."
        },
        "answer": "B",
        "explanation": "Economic value is created when $\\text{ROIC} > \\text{WACC}$. In competitive markets, excess profits attract new entrants who bid down returns toward the cost of capital. A firm that sustains an economic spread ($\\text{ROIC} - \\text{WACC} > 0$) across full cycles must possess structural barriers to entry, such as patents, brand equity, or switching costs.",
        "distractor_analysis": {
            "A": "In perfect competition, economic profit is driven to zero as $\\text{ROIC} \\to \\text{WACC}$.",
            "C": "ROIC is an operational metric independent of financing leverage; excess ROIC indicates operational superiority."
        }
    },
    {
        "id": "L1-EQ-097",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Company Analysis: Past and Present",
        "los": "Distinguish between organic and inorganic revenue growth.",
        "question": "When evaluating a company's historical revenue trajectory, an equity analyst should consider organic revenue growth superior to acquisition-driven growth because organic growth:",
        "options": {
            "A": "Avoids integration risks, acquisition balance sheet premiums, and goodwill impairment vulnerabilities.",
            "B": "Is entirely tax-exempt under both IFRS and US GAAP.",
            "C": "Guarantees a permanent monopoly in the product sector."
        },
        "answer": "A",
        "explanation": "Organic growth reflects core customer demand, market share expansion, and internal operational execution. M&A-driven growth often incurs high deal premiums, dilutive equity issuance or excessive debt, complex cultural integration challenges, and future goodwill write-downs.",
        "distractor_analysis": {
            "B": "Organic revenues are fully subject to standard statutory corporate income taxation.",
            "C": "Organic growth does not confer monopoly status; competitive pressures persist."
        }
    },
    {
        "id": "L1-EQ-098",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Company Analysis: Past and Present",
        "los": "Evaluate corporate capital allocation effectiveness.",
        "question": "Management that repurchases substantial volumes of corporate stock when share prices trade at all-time peak valuation multiples and pauses buybacks when shares are severely depressed is demonstrating:",
        "options": {
            "A": "Exemplary countercyclical capital stewardship.",
            "B": "Procyclical and value-destructive capital allocation.",
            "C": "Statutory compliance with stock exchange listing rules."
        },
        "answer": "B",
        "explanation": "Disciplined capital allocation requires repurchasing shares when intrinsic value exceeds market price ($V_0 > P$). Repurchasing shares at peak valuation multiples destroys shareholder value by overpaying, while hoarding cash and halting buybacks during downturns misses value-accretive opportunities.",
        "distractor_analysis": {
            "A": "Countercyclical buybacks occur when management repurchases shares aggressively at market lows.",
            "C": "Share buyback timing is entirely discretionary, not mandated by stock exchange rules."
        }
    },
    {
        "id": "L1-EQ-099",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Company Analysis: Past and Present",
        "los": "Describe cyclical vs. defensive company characteristics.",
        "question": "Which of the following companies is best characterized as a defensive non-cyclical enterprise?",
        "options": {
            "A": "A luxury cruise ship operator.",
            "B": "A regulated water and electricity utility provider.",
            "C": "A commercial aircraft manufacturer."
        },
        "answer": "B",
        "explanation": "Defensive companies produce essential goods and services with highly inelastic consumer demand (e.g., electricity, water, basic foodstuffs). Their earnings and cash flows remain stable throughout economic expansions and recessions alike.",
        "distractor_analysis": {
            "A": "Luxury travel is a discretionary consumer expenditure that collapses during economic contractions.",
            "C": "Commercial aircraft manufacturing is highly capital-intensive and intensely cyclical."
        }
    },
    {
        "id": "L1-EQ-100",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Company Analysis: Past and Present",
        "los": "Analyze historical operating profit margin stability.",
        "question": "An analyst examines three firms in the same industry. Firm X exhibits a standard deviation of operating margin of 1.2%, while Firms Y and Z exhibit standard deviations of 6.8% and 8.4%. Firm X's lower margin volatility most likely indicates:",
        "options": {
            "A": "Higher operating leverage and high fixed cost exposure.",
            "B": "Superior cost control, pricing power, or a higher proportion of variable operating costs.",
            "C": "Erratic revenue recognition practices."
        },
        "answer": "B",
        "explanation": "Stable operating margins throughout economic cycles signal competitive strength: either strong pricing power that passes input costs through, disciplined cost management, or flexible variable cost structures that cushion bottom-line profitability.",
        "distractor_analysis": {
            "A": "High operating leverage produces high margin volatility, not low volatility.",
            "C": "Erratic accounting choices typically produce high reported earnings volatility."
        }
    },
    {
        "id": "L1-EQ-101",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Company Analysis: Past and Present",
        "los": "Explain cash conversion cycle (CCC) trends.",
        "question": "A shortening Cash Conversion Cycle (CCC = DSO + DSI - DPO) over a 5-year period indicates that the company is:",
        "options": {
            "A": "Tying up more working capital per dollar of revenue.",
            "B": "Improving working capital efficiency and converting investments in inventory into cash more rapidly.",
            "C": "Approaching technical insolvency."
        },
        "answer": "B",
        "explanation": "The Cash Conversion Cycle measures the days required to turn cash outflows for inventory purchases into cash inflows from sales. A declining CCC means the firm collects receivables faster, sells inventory more quickly, or extends supplier payables, liberating operational cash.",
        "distractor_analysis": {
            "A": "A shortening CCC ties up less cash in working capital, not more.",
            "C": "Faster cash conversion strengthens corporate liquidity and solvency."
        }
    },
    {
        "id": "L1-EQ-102",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Company Analysis: Past and Present",
        "los": "Describe peer group selection criteria.",
        "question": "When constructing an industry peer group for comparative valuation, an analyst should prioritize companies with similar:",
        "options": {
            "A": "Stock ticker symbols and alphabetical names.",
            "B": "Business models, demand drivers, capital structures, and geographic exposure.",
            "C": "Date of initial public offering (IPO)."
        },
        "answer": "B",
        "explanation": "Peer group comparability requires fundamental economic alignment: similar end-market demand, cost structures, operating risks, competitive dynamics, and capital intensity. Simply sharing a broad sector classification is insufficient if revenue models diverge.",
        "distractor_analysis": {
            "A": "Ticker symbols and names are irrelevant to economic and operational performance.",
            "C": "IPO timing has no bearing on business comparability or operating multiples."
        }
    },

    # --- Module 6: Industry & Competitive Analysis (7 Qs: 103 to 109) ---
    {
        "id": "L1-EQ-103",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Industry and Competitive Analysis",
        "los": "Describe Porter's Five Forces framework and its application to industry profitability.",
        "question": "According to Porter's Five Forces framework, which of the following industry conditions is most likely to limit long-term industry profitability?",
        "options": {
            "A": "High barriers to entry and strong patent protections.",
            "B": "Low buyer switching costs and high availability of close substitute products.",
            "C": "A fragmented supplier base with zero collective bargaining power."
        },
        "answer": "B",
        "explanation": "When buyers face low switching costs, they can easily migrate to alternative providers or substitute products whenever prices rise. This elastic demand caps industry pricing power and depresses long-term return on invested capital.",
        "distractor_analysis": {
            "A": "High entry barriers shield incumbents from new competition, preserving high profitability.",
            "C": "Weak, fragmented suppliers have little pricing leverage, allowing incumbents to capture higher margins."
        }
    },
    {
        "id": "L1-EQ-104",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Industry and Competitive Analysis",
        "los": "Calculate and interpret industry concentration measures (HHI and CR4).",
        "question": "An industry consists of four equal-sized firms, each holding a 25% market share. The Herfindahl-Hirschman Index (HHI) for this industry is:",
        "options": {
            "A": "1,000",
            "B": "2,500",
            "C": "10,000"
        },
        "answer": "B",
        "explanation": "The Herfindahl-Hirschman Index (HHI) is calculated as the sum of squared percentage market shares of all firms in the industry: $$\\text{HHI} = \\sum_{i=1}^n s_i^2 = 25^2 + 25^2 + 25^2 + 25^2 = 625 + 625 + 625 + 625 = 2{,}500$$ Under US Department of Justice guidelines, an HHI above 1,800 indicates a highly concentrated industry.",
        "distractor_analysis": {
            "A": "1,000 corresponds to 10 equal firms of 10% each ($10 \\times 10^2 = 1{,}000$).",
            "C": "10,000 represents a pure monopoly with a single firm holding 100% market share ($100^2 = 10{,}000$)."
        }
    },
    {
        "id": "L1-EQ-105",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Industry and Competitive Analysis",
        "los": "Describe the stages of the industry life cycle.",
        "question": "An industry characterized by slowing sales growth, intense price competition, industry consolidation, and excess productive capacity is most likely in which life cycle stage?",
        "options": {
            "A": "Embryonic stage.",
            "B": "Growth stage.",
            "C": "Shakeout stage."
        },
        "answer": "C",
        "explanation": "During the shakeout stage, revenue growth decelerates toward GDP rates as the market becomes saturated. Incumbents fiercely defend market share through price cuts, creating profit margin erosion that forces weaker, higher-cost producers into bankruptcy or acquisition.",
        "distractor_analysis": {
            "A": "The embryonic stage has rapid technical change, high prices, and few early adopters.",
            "B": "The growth stage features accelerating demand, high profitability, and minimal price competition."
        }
    },
    {
        "id": "L1-EQ-106",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Industry and Competitive Analysis",
        "los": "Distinguish between cost leadership and product differentiation strategies.",
        "question": "Under Porter's generic business strategies, a company pursuing a differentiation strategy focuses primarily on:",
        "options": {
            "A": "Minimizing operating expenses to offer the lowest market prices across the entire sector.",
            "B": "Creating unique product features, premium brand perception, and superior customer service that command price premiums.",
            "C": "Maintaining an identical cost structure to the lowest-cost competitor."
        },
        "answer": "B",
        "explanation": "A differentiation strategy seeks to create perceived customer value through distinctive styling, superior technology, brand prestige, or after-sales support. This uniqueness allows the company to charge premium prices that exceed the extra cost of differentiating.",
        "distractor_analysis": {
            "A": "Low price through lowest operating expenses defines a cost leadership strategy.",
            "C": "Matching cost structures without differentiation leads to being 'stuck in the middle'."
        }
    },
    {
        "id": "L1-EQ-107",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Industry and Competitive Analysis",
        "los": "Describe switching costs as a barrier to entry.",
        "question": "Enterprise enterprise-resource-planning (ERP) software providers typically enjoy wide economic moats primarily due to:",
        "options": {
            "A": "Low switching costs that allow corporate clients to migrate platforms overnight.",
            "B": "High switching costs involving mission-critical operational disruptions, employee retraining, and data migration expenses.",
            "C": "Complete absence of copyright and trade secret protections."
        },
        "answer": "B",
        "explanation": "Switching costs arise when replacing an incumbent provider requires substantial monetary outlays, operational disruption, risk of data loss, and staff retraining. For ERP systems deeply embedded in day-to-day business operations, switching costs create substantial customer lock-in and pricing power.",
        "distractor_analysis": {
            "A": "Low switching costs undermine competitive moats by encouraging customer churn.",
            "C": "Software firms rely heavily on copyright and intellectual property protections."
        }
    },
    {
        "id": "L1-EQ-108",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Industry and Competitive Analysis",
        "los": "Describe macroeconomic and demographic influences on industry performance.",
        "question": "Which of the following macroeconomic factors is most critical to analyze when forecasting revenue for the residential housing and construction sector?",
        "options": {
            "A": "Long-term mortgage interest rates, household formation rates, and real personal disposable income.",
            "B": "Semiconductor fabrication cleanroom utilization metrics.",
            "C": "International container shipping freight tariffs on bulk dry agricultural grains."
        },
        "answer": "A",
        "explanation": "Residential construction demand is highly interest-rate sensitive. Key drivers are mortgage interest rates (which dictate monthly affordability), household formation demographics (underlying physical demand), and real disposable wage growth.",
        "distractor_analysis": {
            "B": "Semiconductor utilization impacts microelectronics hardware, not residential real estate framing.",
            "C": "Agricultural bulk freight rates govern grain exports, not domestic residential housing."
        }
    },
    {
        "id": "L1-EQ-109",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Industry and Competitive Analysis",
        "los": "Explain network effects as an entry barrier.",
        "question": "A two-sided payment card network becomes increasingly valuable to existing cardholders as more merchants accept the card, and more valuable to merchants as more consumers carry the card. This dynamic is an example of:",
        "options": {
            "A": "Two-sided network effects.",
            "B": "Diminishing marginal utility of capital.",
            "C": "Pure regulatory licensing protection."
        },
        "answer": "A",
        "explanation": "Network effects occur when the value of a service increases with the number of users. In two-sided networks (like credit card payment systems), adoption on one side (consumers) drives adoption on the opposite side (merchants), creating an insurmountable competitive moat for sub-scale new entrants.",
        "distractor_analysis": {
            "B": "Diminishing marginal returns describe declining incremental output, opposite to self-reinforcing network scaling.",
            "C": "Network effects stem from platform utility and adoption, not statutory regulatory fiat."
        }
    },

    # --- Module 8: Valuation Tools: DDM, Multiples, EV/EBITDA (6 Qs: 110 to 115) ---
    {
        "id": "L1-EQ-110",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Equity Valuation: Concepts and Basic Tools",
        "los": "Calculate and interpret the Gordon Growth Model intrinsic value.",
        "question": "Company V recently paid an annual dividend of 3.00 USD per share ($D_0 = 3.00$). The dividend is expected to grow indefinitely at a constant rate of 4.5% per year. If the required return on equity is 9.0%, the intrinsic value of the stock using the Gordon growth model is closest to:",
        "options": {
            "A": "66.67 USD",
            "B": "69.67 USD",
            "C": "73.33 USD"
        },
        "answer": "B",
        "explanation": "Step 1: Calculate next year's dividend $D_1$: $$D_1 = D_0 \\times (1 + g) = 3.00 \\times (1 + 0.045) = 3.135\\text{ USD}$$ Step 2: Apply the Gordon Growth Model: $$V_0 = \\frac{D_1}{r - g} = \\frac{3.135}{0.090 - 0.045} = \\frac{3.135}{0.045} = 69.67\\text{ USD}$$",
        "distractor_analysis": {
            "A": "66.67 USD erroneously uses $D_0$ in the numerator without growing the dividend: $3.00 / 0.045 = 66.67$.",
            "C": "73.33 USD results from using an incorrect spread in the denominator ($0.090 - 0.049$).",
        }
    },
    {
        "id": "L1-EQ-111",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Equity Valuation: Concepts and Basic Tools",
        "los": "Calculate and interpret justified forward P/E.",
        "question": "A firm has a dividend payout ratio of 40%, an expected sustainable dividend growth rate of 5.0%, and a required rate of return of 10.0%. The firm's justified forward price-to-earnings (P/E) multiple is:",
        "options": {
            "A": "6.0x",
            "B": "8.0x",
            "C": "10.0x"
        },
        "answer": "B",
        "explanation": "The justified forward P/E (based on next year's expected earnings $E_1$) is derived from the Gordon Growth Model: $$\\frac{P_0}{E_1} = \\frac{D_1 / E_1}{r - g} = \\frac{1 - b}{r - g} = \\frac{0.40}{0.100 - 0.050} = \\frac{0.40}{0.050} = 8.0\\times$$",
        "distractor_analysis": {
            "A": "6.0x results from incorrectly dividing 0.30 by 0.05.",
            "C": "10.0x is simply $1 / r = 1 / 0.10$, ignoring dividend retention and growth."
        }
    },
    {
        "id": "L1-EQ-112",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Equity Valuation: Concepts and Basic Tools",
        "los": "Calculate enterprise value (EV) and explain EV/EBITDA.",
        "question": "A corporation has 50 million common shares outstanding trading at 40 USD per share. It has 400 million USD in market value of long-term debt, 50 million USD in preferred stock, and 150 million USD in cash and short-term marketable securities. The firm's Enterprise Value (EV) is:",
        "options": {
            "A": "2,000 million USD",
            "B": "2,300 million USD",
            "C": "2,600 million USD"
        },
        "answer": "B",
        "explanation": "Enterprise Value (EV) represents the total economic market value of the operating business: $$\\text{Market Value of Common Equity} = 50\\text{ million} \\times 40\\text{ USD} = 2{,}000\\text{ million USD}$$ $$\\text{EV} = \\text{Equity Value} + \\text{Total Debt} + \\text{Preferred Stock} - \\text{Cash}$$ $$\\text{EV} = 2{,}000 + 400 + 50 - 150 = 2{,}300\\text{ million USD}$$",
        "distractor_analysis": {
            "A": "2,000 million USD is only the equity market capitalization, omitting net debt and preferred stock.",
            "C": "2,600 million USD erroneously adds cash instead of subtracting it ($2{,}000 + 400 + 50 + 150 = 2{,}600$)."
        }
    },
    {
        "id": "L1-EQ-113",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Equity Valuation: Concepts and Basic Tools",
        "los": "Explain why EV/EBITDA is preferred over P/E when comparing companies with different capital structures.",
        "question": "An equity analyst prefers using the EV/EBITDA multiple rather than the P/E multiple when comparing two direct competitors because EV/EBITDA is:",
        "options": {
            "A": "Neutral to differences in financial leverage (debt vs. equity financing) and independent of depreciation accounting policies.",
            "B": "Always numerically lower than the price-to-book multiple.",
            "C": "Unaffected by differences in sales revenue."
        },
        "answer": "A",
        "explanation": "Enterprise Value reflects the total enterprise claims (debt + equity), while EBITDA reflects operating profitability before financing costs (interest) and capital asset depreciation schedules. Consequently, EV/EBITDA permits cleaner comparisons across firms with differing financial leverage and capital intensity.",
        "distractor_analysis": {
            "B": "EV/EBITDA is not mechanically lower than P/B; the two multiples measure fundamentally different bases.",
            "C": "EBITDA is directly derived from sales revenues and operating costs."
        }
    },
    {
        "id": "L1-EQ-114",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Equity Valuation: Concepts and Basic Tools",
        "los": "Calculate and interpret the PEG ratio.",
        "question": "Stock A has a P/E multiple of 24.0x and an expected long-term earnings growth rate of 16.0%. Stock B has a P/E multiple of 18.0x and an expected earnings growth rate of 9.0%. Based strictly on the Price/Earnings-to-Growth (PEG) ratio, which stock appears more attractively valued?",
        "options": {
            "A": "Stock A, because its PEG ratio of 1.50 is lower than Stock B's PEG ratio of 2.00.",
            "B": "Stock B, because its P/E multiple is 6.0 turns lower than Stock A.",
            "C": "Both stocks are equally attractive because both PEG ratios exceed 1.0."
        },
        "answer": "A",
        "explanation": "The PEG ratio adjusts the P/E multiple for the expected growth rate ($g$ expressed as a percentage): $$\\text{PEG}_A = \\frac{24.0}{16.0} = 1.50$$ $$\\text{PEG}_B = \\frac{18.0}{9.0} = 2.00$$ A lower PEG ratio indicates a lower price per unit of expected growth. Stock A is more attractively valued despite its higher headline P/E multiple.",
        "distractor_analysis": {
            "B": "Evaluating headline P/E without adjusting for growth ignores the fact that Stock A is growing nearly twice as fast.",
            "C": "A PEG of 1.50 is superior to 2.00; they are not equally attractive."
        }
    },
    {
        "id": "L1-EQ-115",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Equity Valuation: Concepts and Basic Tools",
        "los": "Explain the relationship between ROE, retention rate, and sustainable growth.",
        "question": "A firm reports Return on Equity (ROE) of 18.0% and maintains a dividend payout ratio of 30.0%. The firm's sustainable growth rate ($g$) is closest to:",
        "options": {
            "A": "5.4%",
            "B": "12.6%",
            "C": "18.0%"
        },
        "answer": "B",
        "explanation": "Sustainable growth rate ($g$) is the rate at which equity earnings and dividends can grow without changing financial leverage: $$b = \\text{Retention Rate} = 1 - \\text{Payout Ratio} = 1 - 0.30 = 0.70$$ $$g = b \\times \\text{ROE} = 0.70 \\times 18.0\\% = 12.6\\%$$",
        "distractor_analysis": {
            "A": "5.4% is calculated by erroneously multiplying ROE by the payout ratio ($0.30 \\times 18\\% = 5.4\\%$).",
            "C": "18.0% represents ROE with 100% earnings retention ($b = 1.0$)."
        }
    }
]

updated_qs = existing_qs + new_questions
print(f"New total L1 EQ questions: {len(updated_qs)}")

with open(EQ_PATH, "w", encoding="utf-8") as f:
    json.dump(updated_qs, f, indent=2, ensure_ascii=False)

print(f"Successfully saved updated L1 EQ questions to {EQ_PATH}")
