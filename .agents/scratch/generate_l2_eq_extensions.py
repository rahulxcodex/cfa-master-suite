import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
L2_EQ_PATH = os.path.join(BASE_DIR, "data", "fi_eq", "l2_equity.json")

with open(L2_EQ_PATH, "r", encoding="utf-8") as f:
    existing_qs = json.load(f)

print(f"Current L2 EQ questions: {len(existing_qs)}")

v18_v19_questions = [
    # --- Vignette 18: Equity Valuation Applications & Model Selection (5 Questions) ---
    {
        "id": "L2-EQ-V18-Q1",
        "level": 2,
        "topic": "Equity Valuation",
        "subtopic": "Valuation Model Selection: DDM vs. FCF vs. Residual Income",
        "vignette_id": "V18",
        "vignette_title": "Apex Global Capital: Valuation Model Selection & Corporate Governance Alignment",
        "vignette_text": "Apex Global Capital is a multi-strategy asset management firm. Senior valuation director Marcus Vance and equity associate Linnea Holm are reviewing valuation models for three target investment opportunities:\n\nCompany Alpha: A rapidly growing software-as-a-service (SaaS) provider that has never paid a dividend and reinvests 100% of cash flow into software development and customer acquisition. Alpha expects to turn free cash flow positive in Year 3. Its capital structure contains zero debt, and management is not controlled by the target investor group.\n\nCompany Beta: A mature, highly leveraged telecom company undergoing a comprehensive 5-year debt deleveraging program that will dramatically reduce its debt-to-equity ratio from 2.50 to 0.80 over the next 4 years. Beta's dividend payments have historically fluctuated with capital expenditure cycles.\n\nCompany Gamma: A profitable, capital-intensive manufacturing conglomerate with unpredictable, cyclical dividend payments, significant non-operating real estate holdings, and negative expected free cash flows during an impending 4-year factory retooling phase. Gamma's accounting follows standard clean surplus accounting principles.\n\nMarcus asks Linnea to determine the most theoretically sound and practically robust valuation methodology for each firm.",
        "los": "Explain the rationale for selecting appropriate valuation models given company characteristics.",
        "question": "For Company Alpha, which valuation methodology is most theoretically sound and practically implementable?",
        "options": {
            "A": "Dividend Discount Model (DDM).",
            "B": "Free Cash Flow to Equity (FCFE) model.",
            "C": "Asset-based liquidation model."
        },
        "answer": "B",
        "explanation": "Because Company Alpha pays zero dividends and reinvests all earnings into rapid growth, the Dividend Discount Model (DDM) is ineffective (forecasting the start date and payout ratio of future dividends introduces excessive estimation error). Alpha is an all-equity firm with zero debt and a non-controlling equity analyst perspective; therefore, FCFE reflects the underlying cash generation capacity of the equity claims directly once free cash flows turn positive.",
        "distractor_analysis": {
            "A": "DDM is unsuited for zero-dividend growth companies because dividend forecasting requires arbitrary timing assumptions.",
            "C": "Asset-based liquidation ignores intangible SaaS IP, recurring revenue subscriptions, and enterprise going-concern value."
        }
    },
    {
        "id": "L2-EQ-V18-Q2",
        "level": 2,
        "topic": "Equity Valuation",
        "subtopic": "Valuation Model Selection: DDM vs. FCF vs. Residual Income",
        "vignette_id": "V18",
        "vignette_title": "Apex Global Capital: Valuation Model Selection & Corporate Governance Alignment",
        "vignette_text": "Apex Global Capital is a multi-strategy asset management firm. Senior valuation director Marcus Vance and equity associate Linnea Holm are reviewing valuation models for three target investment opportunities:\n\nCompany Alpha: A rapidly growing software-as-a-service (SaaS) provider that has never paid a dividend and reinvests 100% of cash flow into software development and customer acquisition. Alpha expects to turn free cash flow positive in Year 3. Its capital structure contains zero debt, and management is not controlled by the target investor group.\n\nCompany Beta: A mature, highly leveraged telecom company undergoing a comprehensive 5-year debt deleveraging program that will dramatically reduce its debt-to-equity ratio from 2.50 to 0.80 over the next 4 years. Beta's dividend payments have historically fluctuated with capital expenditure cycles.\n\nCompany Gamma: A profitable, capital-intensive manufacturing conglomerate with unpredictable, cyclical dividend payments, significant non-operating real estate holdings, and negative expected free cash flows during an impending 4-year factory retooling phase. Gamma's accounting follows standard clean surplus accounting principles.\n\nMarcus asks Linnea to determine the most theoretically sound and practically robust valuation methodology for each firm.",
        "los": "Compare the FCFF and FCFE approaches to valuing equity when leverage is volatile.",
        "question": "For Company Beta, which valuation approach is most appropriate given its planned 5-year capital structure transformation?",
        "options": {
            "A": "FCFE discounted at the Cost of Equity ($r_e$).",
            "B": "FCFF discounted at WACC, followed by subtracting the current market value of debt.",
            "C": "A constant growth Gordon Dividend Discount Model."
        },
        "answer": "B",
        "explanation": "When a firm's capital structure is changing significantly (e.g., rapid deleveraging where debt-to-equity shifts from 2.50 to 0.80), forecasting net borrowing and future FCFE per period is complicated and volatile, and the Cost of Equity ($r_e$) changes every period. The FCFF approach is preferred because operating cash flows and WACC can be modeled more cleanly, and total enterprise value is calculated directly before deducting current debt.",
        "distractor_analysis": {
            "A": "FCFE requires period-by-period adjustments to levered beta and Cost of Equity as the debt ratio changes.",
            "C": "The Gordon DDM requires constant leverage and steady-state dividend growth, neither of which applies to Beta."
        }
    },
    {
        "id": "L2-EQ-V18-Q3",
        "level": 2,
        "topic": "Equity Valuation",
        "subtopic": "Valuation Model Selection: DDM vs. FCF vs. Residual Income",
        "vignette_id": "V18",
        "vignette_title": "Apex Global Capital: Valuation Model Selection & Corporate Governance Alignment",
        "vignette_text": "Apex Global Capital is a multi-strategy asset management firm. Senior valuation director Marcus Vance and equity associate Linnea Holm are reviewing valuation models for three target investment opportunities:\n\nCompany Alpha: A rapidly growing software-as-a-service (SaaS) provider that has never paid a dividend and reinvests 100% of cash flow into software development and customer acquisition. Alpha expects to turn free cash flow positive in Year 3. Its capital structure contains zero debt, and management is not controlled by the target investor group.\n\nCompany Beta: A mature, highly leveraged telecom company undergoing a comprehensive 5-year debt deleveraging program that will dramatically reduce its debt-to-equity ratio from 2.50 to 0.80 over the next 4 years. Beta's dividend payments have historically fluctuated with capital expenditure cycles.\n\nCompany Gamma: A profitable, capital-intensive manufacturing conglomerate with unpredictable, cyclical dividend payments, significant non-operating real estate holdings, and negative expected free cash flows during an impending 4-year factory retooling phase. Gamma's accounting follows standard clean surplus accounting principles.\n\nMarcus asks Linnea to determine the most theoretically sound and practically robust valuation methodology for each firm.",
        "los": "Explain the conditions under which the residual income model is most appropriate.",
        "question": "For Company Gamma, why is the Residual Income (RI) model particularly well-suited relative to a discounted free cash flow model?",
        "options": {
            "A": "Residual income models fail whenever accounting numbers adhere to clean surplus relations.",
            "B": "A large portion of intrinsic value is recognized immediately in the starting book value of equity, and RI remains positive and well-behaved even when free cash flows are temporarily negative due to heavy CapEx.",
            "C": "Residual income models eliminate the need to estimate a terminal value or cost of equity."
        },
        "answer": "B",
        "explanation": "Residual income models are ideal for companies with negative or volatile free cash flows resulting from heavy capital expenditure cycles. A major fraction of total intrinsic value is grounded in current balance sheet book value ($B_0$), and residual income ($NI - r_e \\times B_{t-1}$) remains positive as long as return on equity exceeds the cost of equity, avoiding DCF terminal value distortions.",
        "distractor_analysis": {
            "A": "Clean surplus accounting is a strict requirement for residual income models to be mathematically valid.",
            "C": "Residual income models still require an estimated Cost of Equity and terminal persistence assumption."
        }
    },
    {
        "id": "L2-EQ-V18-Q4",
        "level": 2,
        "topic": "Equity Valuation",
        "subtopic": "Valuation Model Selection: DDM vs. FCF vs. Residual Income",
        "vignette_id": "V18",
        "vignette_title": "Apex Global Capital: Valuation Model Selection & Corporate Governance Alignment",
        "vignette_text": "Apex Global Capital is a multi-strategy asset management firm. Senior valuation director Marcus Vance and equity associate Linnea Holm are reviewing valuation models for three target investment opportunities:\n\nCompany Alpha: A rapidly growing software-as-a-service (SaaS) provider that has never paid a dividend and reinvests 100% of cash flow into software development and customer acquisition. Alpha expects to turn free cash flow positive in Year 3. Its capital structure contains zero debt, and management is not controlled by the target investor group.\n\nCompany Beta: A mature, highly leveraged telecom company undergoing a comprehensive 5-year debt deleveraging program that will dramatically reduce its debt-to-equity ratio from 2.50 to 0.80 over the next 4 years. Beta's dividend payments have historically fluctuated with capital expenditure cycles.\n\nCompany Gamma: A profitable, capital-intensive manufacturing conglomerate with unpredictable, cyclical dividend payments, significant non-operating real estate holdings, and negative expected free cash flows during an impending 4-year factory retooling phase. Gamma's accounting follows standard clean surplus accounting principles.\n\nMarcus asks Linnea to determine the most theoretically sound and practically robust valuation methodology for each firm.",
        "los": "Explain the role of investor control and perspective in valuation model selection.",
        "question": "If an activist private equity acquirer seeks to purchase a controlling 100% stake in Company Beta to redirect free cash flows, optimize working capital, and alter capital structure, the acquirer should value the firm using:",
        "options": {
            "A": "A dividend discount model based on historical dividend payouts.",
            "B": "A free cash flow model (FCFF or FCFE) reflecting discretionary cash generation capacity under new control.",
            "C": "The historical trailing P/E multiple of passive minority shareholders."
        },
        "answer": "B",
        "explanation": "A controlling shareholder has the legal power to determine corporate dividend policy, optimize capital structure, and redeploy free cash flows. For controlling acquisitions, free cash flow models measure the true economic cash capacity of the firm, whereas DDM reflects only discretionary payments made to passive minority investors.",
        "distractor_analysis": {
            "A": "Historical dividends reflect prior minority distributions, not the cash flows accessible to a controlling owner.",
            "C": "Trailing minority trading multiples reflect lack of control and exclude control synergies."
        }
    },
    {
        "id": "L2-EQ-V18-Q5",
        "level": 2,
        "topic": "Equity Valuation",
        "subtopic": "Valuation Model Selection: DDM vs. FCF vs. Residual Income",
        "vignette_id": "V18",
        "vignette_title": "Apex Global Capital: Valuation Model Selection & Corporate Governance Alignment",
        "vignette_text": "Apex Global Capital is a multi-strategy asset management firm. Senior valuation director Marcus Vance and equity associate Linnea Holm are reviewing valuation models for three target investment opportunities:\n\nCompany Alpha: A rapidly growing software-as-a-service (SaaS) provider that has never paid a dividend and reinvests 100% of cash flow into software development and customer acquisition. Alpha expects to turn free cash flow positive in Year 3. Its capital structure contains zero debt, and management is not controlled by the target investor group.\n\nCompany Beta: A mature, highly leveraged telecom company undergoing a comprehensive 5-year debt deleveraging program that will dramatically reduce its debt-to-equity ratio from 2.50 to 0.80 over the next 4 years. Beta's dividend payments have historically fluctuated with capital expenditure cycles.\n\nCompany Gamma: A profitable, capital-intensive manufacturing conglomerate with unpredictable, cyclical dividend payments, significant non-operating real estate holdings, and negative expected free cash flows during an impending 4-year factory retooling phase. Gamma's accounting follows standard clean surplus accounting principles.\n\nMarcus asks Linnea to determine the most theoretically sound and practically robust valuation methodology for each firm.",
        "los": "Distinguish between going-concern value and liquidation value.",
        "question": "When valuing a company facing imminent bankruptcy and court-supervised asset dissolution, the analyst should base valuation on:",
        "options": {
            "A": "Going-concern value using a multistage DCF with perpetual growth.",
            "B": "Orderly or forced liquidation value of net identifiable tangible assets after deducting liquidation costs and debt claims.",
            "C": "A justified price-to-book multiple based on historical sustainable ROE."
        },
        "answer": "B",
        "explanation": "Going-concern value assumes the entity will continue operating indefinitely to generate future cash flows. When liquidation or bankruptcy is imminent, going-concern assumptions fail, and the equity must be valued on net liquidation value—the estimated net cash proceeds from selling assets separately minus debt claims and liquidation expenses.",
        "distractor_analysis": {
            "A": "Perpetual DCF growth assumes ongoing business continuity, which is invalid in bankruptcy liquidation.",
            "C": "Historical ROE and P/B multiples assume future operating profits that will not materialize."
        }
    },

    # --- Vignette 19: Sum-of-the-Parts (SOTP) Valuation & Conglomerates (5 Questions) ---
    {
        "id": "L2-EQ-V19-Q1",
        "level": 2,
        "topic": "Equity Valuation",
        "subtopic": "Sum-of-the-Parts (SOTP) Valuation",
        "vignette_id": "V19",
        "vignette_title": "Nordic Industries: Sum-of-the-Parts Valuation and Conglomerate Discount Decomposition",
        "vignette_text": "Nordic Industries (NI) is a diversified holding conglomerate operating across three distinct, autonomous divisions: Industrial Machinery, Specialty Chemicals, and Renewable Energy. Investment analyst Henrik Lind is conducting a sum-of-the-parts (SOTP) valuation to determine whether Nordic Industries is trading at a conglomerate discount.\n\nExhibit 1: Nordic Industries Segment Financial Data (in millions of EUR)\n- Industrial Machinery: Projected 2025 EBITDA = 180 EUR; Benchmark Peer Median EV/EBITDA = 8.5x\n- Specialty Chemicals: Projected 2025 EBITDA = 120 EUR; Benchmark Peer Median EV/EBITDA = 11.0x\n- Renewable Energy: Projected 2025 EBITDA = 90 EUR; Benchmark Peer Median EV/EBITDA = 14.0x\n\nExhibit 2: Corporate-Level Balance Sheet & Overhead Items (in millions of EUR)\n- Unallocated Corporate Headquarters Annual Overhead Expense = 15 EUR (capitalized at an overhead multiple of 10.0x)\n- Market Value of Total Long-Term Debt = 750 EUR\n- Cash and Cash Equivalents = 120 EUR\n- Market Value of Non-Controlling Interest (Minority Interest) = 60 EUR\n- Common Shares Outstanding = 100 million shares\n- Current Nordic Industries Market Price per Share = 26.50 EUR",
        "los": "Calculate the sum-of-the-parts (SOTP) value of a diversified company.",
        "question": "Based on Exhibits 1 and 2, the estimated total Enterprise Value (EV) of Nordic Industries' operating business segments before corporate overhead adjustments is closest to:",
        "options": {
            "A": "3,110 million EUR",
            "B": "3,900 million EUR",
            "C": "4,110 million EUR"
        },
        "answer": "C",
        "explanation": "Compute the sum of enterprise values across the three autonomous operating divisions: $$\\text{EV}_{\\text{Machinery}} = 180 \\times 8.5 = 1{,}530\\text{ million EUR}$$ $$\\text{EV}_{\\text{Chemicals}} = 120 \\times 11.0 = 1{,}320\\text{ million EUR}$$ $$\\text{EV}_{\\text{Renewable}} = 90 \\times 14.0 = 1{,}260\\text{ million EUR}$$ $$\\text{Total Operating Segment EV} = 1{,}530 + 1{,}320 + 1{,}260 = 4{,}110\\text{ million EUR}$$",
        "distractor_analysis": {
            "A": "3,110 million EUR results from omitting the Renewable Energy division ($4{,}110 - 1{,}260 = 2{,}850$) or incorrect arithmetic.",
            "B": "3,900 million EUR erroneously subtracts the Machinery EV."
        }
    },
    {
        "id": "L2-EQ-V19-Q2",
        "level": 2,
        "topic": "Equity Valuation",
        "subtopic": "Sum-of-the-Parts (SOTP) Valuation",
        "vignette_id": "V19",
        "vignette_title": "Nordic Industries: Sum-of-the-Parts Valuation and Conglomerate Discount Decomposition",
        "vignette_text": "Nordic Industries (NI) is a diversified holding conglomerate operating across three distinct, autonomous divisions: Industrial Machinery, Specialty Chemicals, and Renewable Energy. Investment analyst Henrik Lind is conducting a sum-of-the-parts (SOTP) valuation to determine whether Nordic Industries is trading at a conglomerate discount.\n\nExhibit 1: Nordic Industries Segment Financial Data (in millions of EUR)\n- Industrial Machinery: Projected 2025 EBITDA = 180 EUR; Benchmark Peer Median EV/EBITDA = 8.5x\n- Specialty Chemicals: Projected 2025 EBITDA = 120 EUR; Benchmark Peer Median EV/EBITDA = 11.0x\n- Renewable Energy: Projected 2025 EBITDA = 90 EUR; Benchmark Peer Median EV/EBITDA = 14.0x\n\nExhibit 2: Corporate-Level Balance Sheet & Overhead Items (in millions of EUR)\n- Unallocated Corporate Headquarters Annual Overhead Expense = 15 EUR (capitalized at an overhead multiple of 10.0x)\n- Market Value of Total Long-Term Debt = 750 EUR\n- Cash and Cash Equivalents = 120 EUR\n- Market Value of Non-Controlling Interest (Minority Interest) = 60 EUR\n- Common Shares Outstanding = 100 million shares\n- Current Nordic Industries Market Price per Share = 26.50 EUR",
        "los": "Calculate the per-share equity value of a company using the sum-of-the-parts method.",
        "question": "Accounting for unallocated corporate overhead and balance sheet adjustments, the SOTP intrinsic value per common share of Nordic Industries is closest to:",
        "options": {
            "A": "26.50 EUR",
            "B": "32.70 EUR",
            "C": "34.20 EUR"
        },
        "answer": "B",
        "explanation": "Step 1: Total Operating EV = 4,110 million EUR.\nStep 2: Capitalized corporate overhead = $15 \\times 10.0 = 150\\text{ million EUR}$.\nStep 3: Adjusted Enterprise Value: $$\\text{EV}_{\\text{adj}} = 4{,}110 - 150 = 3{,}960\\text{ million EUR}$$\nStep 4: Bridge to Equity Value: $$\\text{Equity Value} = \\text{EV}_{\\text{adj}} - \\text{Debt} + \\text{Cash} - \\text{Minority Interest}$$\n$$\\text{Equity Value} = 3{,}960 - 750 + 120 - 60 = 3{,}270\\text{ million EUR}$$\nStep 5: Per share value: $$\\text{Value per share} = \\frac{3{,}270\\text{ million EUR}}{100\\text{ million shares}} = 32.70\\text{ EUR}$$",
        "distractor_analysis": {
            "A": "26.50 EUR is the current trading price in the market, not the SOTP intrinsic value.",
            "C": "34.20 EUR erroneously omits the 150 million EUR corporate overhead capitalization ($3{,}420 / 100 = 34.20$)."
        }
    },
    {
        "id": "L2-EQ-V19-Q3",
        "level": 2,
        "topic": "Equity Valuation",
        "subtopic": "Sum-of-the-Parts (SOTP) Valuation",
        "vignette_id": "V19",
        "vignette_title": "Nordic Industries: Sum-of-the-Parts Valuation and Conglomerate Discount Decomposition",
        "vignette_text": "Nordic Industries (NI) is a diversified holding conglomerate operating across three distinct, autonomous divisions: Industrial Machinery, Specialty Chemicals, and Renewable Energy. Investment analyst Henrik Lind is conducting a sum-of-the-parts (SOTP) valuation to determine whether Nordic Industries is trading at a conglomerate discount.\n\nExhibit 1: Nordic Industries Segment Financial Data (in millions of EUR)\n- Industrial Machinery: Projected 2025 EBITDA = 180 EUR; Benchmark Peer Median EV/EBITDA = 8.5x\n- Specialty Chemicals: Projected 2025 EBITDA = 120 EUR; Benchmark Peer Median EV/EBITDA = 11.0x\n- Renewable Energy: Projected 2025 EBITDA = 90 EUR; Benchmark Peer Median EV/EBITDA = 14.0x\n\nExhibit 2: Corporate-Level Balance Sheet & Overhead Items (in millions of EUR)\n- Unallocated Corporate Headquarters Annual Overhead Expense = 15 EUR (capitalized at an overhead multiple of 10.0x)\n- Market Value of Total Long-Term Debt = 750 EUR\n- Cash and Cash Equivalents = 120 EUR\n- Market Value of Non-Controlling Interest (Minority Interest) = 60 EUR\n- Common Shares Outstanding = 100 million shares\n- Current Nordic Industries Market Price per Share = 26.50 EUR",
        "los": "Explain the reasons for conglomerate discounts in market valuations.",
        "question": "Comparing the market price of 26.50 EUR to the SOTP intrinsic value of 32.70 EUR reveals a conglomerate discount of approximately 19.0%. Which of the following is the most plausible economic explanation for this conglomerate discount?",
        "options": {
            "A": "Superior operational transparency and extensive standalone segment disclosures.",
            "B": "Capital allocation inefficiencies (cross-subsidization of underperforming divisions) and corporate agency costs.",
            "C": "A complete absence of corporate governance overhead."
        },
        "answer": "B",
        "explanation": "Conglomerates frequently trade at a discount (typically 10%–20%) relative to the sum of their standalone parts due to: (1) internal capital market inefficiencies where cash generated by profitable divisions is wasted subsidizing weaker segments; (2) organizational complexity and managerial agency costs; and (3) lack of pure-play focus for institutional investors.",
        "distractor_analysis": {
            "A": "Conglomerates generally suffer from reduced disclosure transparency, which widens discounts.",
            "C": "Conglomerates incur heavy central corporate headquarters overhead, adding cost."
        }
    },
    {
        "id": "L2-EQ-V19-Q4",
        "level": 2,
        "topic": "Equity Valuation",
        "subtopic": "Sum-of-the-Parts (SOTP) Valuation",
        "vignette_id": "V19",
        "vignette_title": "Nordic Industries: Sum-of-the-Parts Valuation and Conglomerate Discount Decomposition",
        "vignette_text": "Nordic Industries (NI) is a diversified holding conglomerate operating across three distinct, autonomous divisions: Industrial Machinery, Specialty Chemicals, and Renewable Energy. Investment analyst Henrik Lind is conducting a sum-of-the-parts (SOTP) valuation to determine whether Nordic Industries is trading at a conglomerate discount.\n\nExhibit 1: Nordic Industries Segment Financial Data (in millions of EUR)\n- Industrial Machinery: Projected 2025 EBITDA = 180 EUR; Benchmark Peer Median EV/EBITDA = 8.5x\n- Specialty Chemicals: Projected 2025 EBITDA = 120 EUR; Benchmark Peer Median EV/EBITDA = 11.0x\n- Renewable Energy: Projected 2025 EBITDA = 90 EUR; Benchmark Peer Median EV/EBITDA = 14.0x\n\nExhibit 2: Corporate-Level Balance Sheet & Overhead Items (in millions of EUR)\n- Unallocated Corporate Headquarters Annual Overhead Expense = 15 EUR (capitalized at an overhead multiple of 10.0x)\n- Market Value of Total Long-Term Debt = 750 EUR\n- Cash and Cash Equivalents = 120 EUR\n- Market Value of Non-Controlling Interest (Minority Interest) = 60 EUR\n- Common Shares Outstanding = 100 million shares\n- Current Nordic Industries Market Price per Share = 26.50 EUR",
        "los": "Describe corporate restructuring actions to eliminate conglomerate discounts.",
        "question": "If Nordic Industries spins off its Renewable Energy division into a separate publicly traded company, the transaction will most likely:",
        "options": {
            "A": "Permanently eliminate all tax deductions for Nordic Industries.",
            "B": "Unlock shareholder value by allowing the high-multiple Renewable division to trade at pure-play peer multiples (14.0x) without conglomerate drag.",
            "C": "Force the Machinery and Chemicals divisions into involuntary insolvency."
        },
        "answer": "B",
        "explanation": "Corporate spin-offs eliminate the conglomerate discount by creating an independent 'pure-play' vehicle. The market can value the high-growth renewable energy assets directly at prevailing pure-play industry multiples (14.0x) and eliminate internal cross-subsidization frictions.",
        "distractor_analysis": {
            "A": "Spin-offs are typically structured as tax-free reorganizations under corporate tax codes.",
            "C": "The remaining divisions continue operating as independent viable cash-generating units."
        }
    },
    {
        "id": "L2-EQ-V19-Q5",
        "level": 2,
        "topic": "Equity Valuation",
        "subtopic": "Sum-of-the-Parts (SOTP) Valuation",
        "vignette_id": "V19",
        "vignette_title": "Nordic Industries: Sum-of-the-Parts Valuation and Conglomerate Discount Decomposition",
        "vignette_text": "Nordic Industries (NI) is a diversified holding conglomerate operating across three distinct, autonomous divisions: Industrial Machinery, Specialty Chemicals, and Renewable Energy. Investment analyst Henrik Lind is conducting a sum-of-the-parts (SOTP) valuation to determine whether Nordic Industries is trading at a conglomerate discount.\n\nExhibit 1: Nordic Industries Segment Financial Data (in millions of EUR)\n- Industrial Machinery: Projected 2025 EBITDA = 180 EUR; Benchmark Peer Median EV/EBITDA = 8.5x\n- Specialty Chemicals: Projected 2025 EBITDA = 120 EUR; Benchmark Peer Median EV/EBITDA = 11.0x\n- Renewable Energy: Projected 2025 EBITDA = 90 EUR; Benchmark Peer Median EV/EBITDA = 14.0x\n\nExhibit 2: Corporate-Level Balance Sheet & Overhead Items (in millions of EUR)\n- Unallocated Corporate Headquarters Annual Overhead Expense = 15 EUR (capitalized at an overhead multiple of 10.0x)\n- Market Value of Total Long-Term Debt = 750 EUR\n- Cash and Cash Equivalents = 120 EUR\n- Market Value of Non-Controlling Interest (Minority Interest) = 60 EUR\n- Common Shares Outstanding = 100 million shares\n- Current Nordic Industries Market Price per Share = 26.50 EUR",
        "los": "Describe how intercompany transactions affect SOTP valuation.",
        "question": "When applying SOTP valuation to a conglomerate where Division A sells intermediate chemical components to Division B at non-market transfer prices, Henrik must adjust segment financials by:",
        "options": {
            "A": "Restating internal transactions at arm's-length market prices to ensure division EBITDAs reflect true standalone profitability.",
            "B": "Double-counting the internal revenue in both divisions' reported figures.",
            "C": "Ignoring intercompany transfer prices because consolidated net income is unaffected."
        },
        "answer": "A",
        "explanation": "If internal transfer pricing deviates from fair market terms, one division's EBITDA is artificially subsidized while the other is depressed. Applying peer multiples to distorted division EBITDA generates inaccurate SOTP values; the analyst must restate intercompany transfers to fair arm's-length prices before applying peer multiples.",
        "distractor_analysis": {
            "B": "Double-counting internal sales creates fictitious enterprise value across the company.",
            "C": "While consolidated net income cancels transfers out, individual segment multiples will be severely misapplied if unadjusted."
        }
    }
]

updated_qs = existing_qs + v18_v19_questions
print(f"New total L2 EQ questions: {len(updated_qs)}")

with open(L2_EQ_PATH, "w", encoding="utf-8") as f:
    json.dump(updated_qs, f, indent=2, ensure_ascii=False)

print(f"Successfully saved updated L2 EQ questions to {L2_EQ_PATH}")
