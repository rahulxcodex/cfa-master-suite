import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
FI_PATH = os.path.join(BASE_DIR, "data", "fi_eq", "l1_fixed_income.json")

with open(FI_PATH, "r", encoding="utf-8") as f:
    existing_qs = json.load(f)

print(f"Current L1 FI questions: {len(existing_qs)}")

new_questions = [
    # --- M8: Floating-Rate Instruments (12 Questions: 086 to 097) ---
    {
        "id": "L1-FI-086",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Floating-Rate Note Pricing and Yield Measures",
        "los": "Calculate and interpret the discount margin for a floating-rate note.",
        "question": "A 3-year floating-rate note (FRN) pays annual coupons of 1-year SOFR + 80 bps. If 1-year SOFR is currently 4.00% and the note is priced at 99.20 per 100 of par value, the discount margin (required margin) relative to the quoted margin is:",
        "options": {
            "A": "Greater than the quoted margin.",
            "B": "Equal to the quoted margin.",
            "C": "Less than the quoted margin."
        },
        "answer": "A",
        "explanation": "When an FRN is priced at a discount to par ($P < 100$), the note's yield to maturity exceeds the coupon rate. Consequently, the discount margin (the margin required by investors over the reference rate to price the bond at market) must exceed the quoted margin ($DM > QM$). If $P = 100$, $DM = QM$; if $P > 100$, $DM < QM$.",
        "distractor_analysis": {
            "B": "The discount margin equals the quoted margin only when the FRN trades exactly at par value (100).",
            "C": "The discount margin is less than the quoted margin when the FRN trades at a premium ($P > 100$)."
        }
    },
    {
        "id": "L1-FI-087",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Floating-Rate Note Pricing and Yield Measures",
        "los": "Calculate and interpret the discount margin for a floating-rate note.",
        "question": "A 1-year quarterly floating-rate note has a quoted margin of 100 bps over 90-day Euribor. The current 90-day Euribor is 3.00%. If an investor requires a discount margin of 140 bps, the estimated price of the FRN per 100 par value on a reset date is closest to:",
        "options": {
            "A": "98.85",
            "B": "99.61",
            "C": "100.39"
        },
        "answer": "B",
        "explanation": "On a coupon reset date, each quarterly coupon payment is determined by the quoted margin: $$\\text{Coupon} = \\frac{3.00\\% + 1.00\\%}{4} \\times 100 = 1.00\\text{ EUR}$$ The required quarterly discount rate is based on Euribor plus discount margin: $$\\text{Discount rate per period} = \\frac{3.00\\% + 1.40\\%}{4} = \\frac{4.40\\%}{4} = 1.10\\%$$ Discounting the 4 quarterly cash flows: $$P = \\frac{1.00}{(1.0110)^1} + \\frac{1.00}{(1.0110)^2} + \\frac{1.00}{(1.0110)^3} + \\frac{101.00}{(1.0110)^4} = 0.9891 + 0.9784 + 0.9677 + 96.6749 = 99.61$$",
        "distractor_analysis": {
            "A": "98.85 results from erroneously applying an annual spread difference of 40 bps without quarterly compounding adjustments.",
            "C": "100.39 occurs if the discount rate is incorrectly set below the coupon rate (treating required margin as less than quoted margin)."
        }
    },
    {
        "id": "L1-FI-088",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Floating-Rate Note Pricing and Yield Measures",
        "los": "Describe the characteristics and risks of floating-rate notes.",
        "question": "Between coupon reset dates, the primary driver of price fluctuations in a high-grade floating-rate note is changes in:",
        "options": {
            "A": "The benchmark reference rate.",
            "B": "The issuer's credit risk and required margin.",
            "C": "The quoted margin specified in the indenture."
        },
        "answer": "B",
        "explanation": "The quoted margin is contractually fixed in the bond indenture. The coupon rate resets periodically to reflect changes in the benchmark reference rate, which insulates the FRN from benchmark interest rate duration risk. Therefore, between reset dates, price volatility is primarily driven by changes in the issuer's credit risk (or liquidity premium), which changes the discount margin required by the market.",
        "distractor_analysis": {
            "A": "Changes in the benchmark rate are passed through to the next coupon at reset, giving FRNs near-zero benchmark duration.",
            "C": "The quoted margin is constant throughout the life of the instrument and does not fluctuate."
        }
    },
    {
        "id": "L1-FI-089",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Floating-Rate Note Pricing and Yield Measures",
        "los": "Explain how caps and floors affect the price and interest rate risk of floating-rate notes.",
        "question": "A floating-rate note with an embedded coupon cap will exhibit effective duration that:",
        "options": {
            "A": "Approaches zero as market interest rates rise significantly above the cap level.",
            "B": "Increases significantly toward the duration of a fixed-rate bond as market interest rates rise above the cap rate.",
            "C": "Remains constant across all interest rate environments."
        },
        "answer": "B",
        "explanation": "When benchmark rates rise well above the cap rate, the coupon becomes fixed at the maximum capped rate. At that point, the FRN no longer resets higher with market rates, transforming it effectively into a fixed-rate bond with full interest rate duration until maturity.",
        "distractor_analysis": {
            "A": "Duration approaches zero when the cap is unconstrained, but rises substantially once the cap binds.",
            "C": "The embedded option creates path-dependent duration that changes dynamically with rate levels."
        }
    },
    {
        "id": "L1-FI-090",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Floating-Rate Note Pricing and Yield Measures",
        "los": "Calculate and interpret the discount margin for a floating-rate note.",
        "question": "If an issuer experiences a credit rating upgrade after issuing an FRN, what is the expected impact on the required margin and the market price of the FRN on the reset date?",
        "options": {
            "A": "Required margin decreases, and the market price rises above par.",
            "B": "Required margin increases, and the market price falls below par.",
            "C": "Required margin decreases, and the market price remains exactly at par."
        },
        "answer": "A",
        "explanation": "A credit upgrade reduces the credit spread demanded by investors, causing the required discount margin ($DM$) to decrease below the contractually fixed quoted margin ($QM$). Because $QM > DM$, the cash flow coupon rate exceeds the required discount rate, causing the market price to trade at a premium ($P > 100$).",
        "distractor_analysis": {
            "B": "Required margin increases during a credit downgrade, not an upgrade.",
            "C": "The price only remains at par if $DM = QM$. Since $DM < QM$, the bond trades above par."
        }
    },
    {
        "id": "L1-FI-091",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Floating-Rate Note Pricing and Yield Measures",
        "los": "Describe the mechanics of reference rates including SOFR and Euribor.",
        "question": "Which of the following best describes the difference between term Euribor and compounded Secured Overnight Financing Rate (SOFR)?",
        "options": {
            "A": "Euribor is an unsecured, forward-looking rate based on bank quotes; SOFR is a secured, backward-looking overnight rate based on actual repo transactions.",
            "B": "Euribor is backed by sovereign collateral; SOFR contains bank credit risk.",
            "C": "SOFR includes an embedded term bank credit risk spread; Euribor is completely risk-free."
        },
        "answer": "A",
        "explanation": "Euribor is an unsecured interbank lending rate determined forward-looking for specified tenors (e.g., 1-month, 3-month) and includes bank credit risk. In contrast, SOFR is a nearly risk-free secured rate reflecting actual overnight Treasury repurchase transactions, aggregated backward-looking over the interest period (in arrears).",
        "distractor_analysis": {
            "B": "Euribor is unsecured; SOFR is secured by US Treasury collateral.",
            "C": "SOFR is nearly free of bank credit risk; Euribor contains term bank credit risk."
        }
    },
    {
        "id": "L1-FI-092",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Floating-Rate Note Pricing and Yield Measures",
        "los": "Calculate and interpret the discount margin for a floating-rate note.",
        "question": "An FRN has a face value of USD 1,000, 2 years to maturity, semi-annual coupons at 180-day SOFR + 60 bps. If the current 180-day SOFR is 3.50% and the note is purchased at 100.50 per 100 par, the required discount margin must be:",
        "options": {
            "A": "Greater than 60 bps.",
            "B": "Equal to 60 bps.",
            "C": "Less than 60 bps."
        },
        "answer": "C",
        "explanation": "Because the FRN trades at a premium ($100.50 > 100$), the investor is willing to accept a discount margin lower than the contractual quoted margin of 60 bps ($DM < 60\\text{ bps}$).",
        "distractor_analysis": {
            "A": "If $DM > 60\\text{ bps}$, the note would trade at a discount ($P < 100$).",
            "B": "If $DM = 60\\text{ bps}$, the note would trade exactly at par ($P = 100$)."
        }
    },
    {
        "id": "L1-FI-093",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Floating-Rate Note Pricing and Yield Measures",
        "los": "Explain inverse floating-rate notes and their leverage characteristics.",
        "question": "An inverse floating-rate note has a coupon formula of $12\\% - 1.5 \\times \\text{SOFR}$. If SOFR increases by 100 bps, the coupon rate will:",
        "options": {
            "A": "Decrease by 100 bps.",
            "B": "Decrease by 150 bps.",
            "C": "Increase by 150 bps."
        },
        "answer": "B",
        "explanation": "The coupon has a leverage factor of $-1.5$. A 100 bps increase in the reference rate results in: $$\\Delta \\text{Coupon} = -1.5 \\times (+100\\text{ bps}) = -150\\text{ bps}$$ An inverse floater has higher duration than a standard fixed-rate bond because rising rates both decrease cash flows and increase discount rates.",
        "distractor_analysis": {
            "A": "100 bps ignores the multiplier coefficient of 1.5.",
            "C": "The negative sign ensures that the coupon declines when the reference rate rises."
        }
    },
    {
        "id": "L1-FI-094",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Floating-Rate Note Pricing and Yield Measures",
        "los": "Explain the concept of reset frequency and effective duration of floating-rate notes.",
        "question": "A 5-year FRN with semi-annual coupon resets has an effective duration closest to:",
        "options": {
            "A": "0.25 years.",
            "B": "2.50 years.",
            "C": "4.50 years."
        },
        "answer": "A",
        "explanation": "The effective duration of an unconstrained FRN with respect to benchmark interest rates is approximately half of the time remaining until the next coupon reset date. For a semi-annual reset bond, the maximum duration just after a reset is 0.50 years, and the average duration across the reset cycle is approximately $0.50 / 2 = 0.25$ years.",
        "distractor_analysis": {
            "B": "2.50 years corresponds to half the bond maturity, which applies to a 5-year zero coupon bond, not an FRN.",
            "C": "4.50 years would be typical for a 5-year fixed-rate coupon bond."
        }
    },
    {
        "id": "L1-FI-095",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Floating-Rate Note Pricing and Yield Measures",
        "los": "Describe payment conventions and coupon accrual for floating-rate debt.",
        "question": "In an 'in-arrears' floating-rate note structure, the coupon rate for a payment period is determined at the:",
        "options": {
            "A": "Beginning of the coupon period and paid at the end of the period.",
            "B": "End of the coupon period and paid at the end of the period.",
            "C": "Beginning of the period and paid at the beginning of the period."
        },
        "answer": "A",
        "explanation": "Under standard advanced-set in-arrears convention, the benchmark rate is observed and fixed at the start of the accrual period (reset date), and the resulting interest is paid at the end of the period (payment date).",
        "distractor_analysis": {
            "B": "Setting the rate at the end of the period is known as 'in-advance' or arrears-resetting, which is less common in traditional corporate FRNs.",
            "C": "Coupons are paid at the end of accrual periods, not at the beginning."
        }
    },
    {
        "id": "L1-FI-096",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Floating-Rate Note Pricing and Yield Measures",
        "los": "Calculate and interpret the discount margin for a floating-rate note.",
        "question": "When computing the discount margin for an FRN using the simplified model, which assumption is typically made regarding future reference rates?",
        "options": {
            "A": "Reference rates will equal forward rates derived from the spot curve.",
            "B": "Reference rates will remain constant at the current index rate over the life of the note.",
            "C": "Reference rates will follow a lognormal interest rate tree."
        },
        "answer": "B",
        "explanation": "The standard simplified discount margin calculation assumes that the reference rate remains constant at the current level for all future reset periods. Both future cash flows and the discount rate are projected using this constant rate, isolating the quoted margin versus discount margin relationship.",
        "distractor_analysis": {
            "A": "Forward rate modeling is used in complex OAS or swap-margin models, not the standard quoted discount margin calculation.",
            "C": "Lognormal trees are used for pricing embedded options (caps and floors), not standard FRN discount margin."
        }
    },
    {
        "id": "L1-FI-097",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Floating-Rate Note Pricing and Yield Measures",
        "los": "Explain how credit rating migration affects FRN pricing.",
        "question": "If an investor purchases an FRN at par value (100) and the issuer subsequently experiences widened credit spreads across the market, the price of the FRN at the next reset date will:",
        "options": {
            "A": "Remain at 100 because the coupon resets to the new market reference rate.",
            "B": "Drop below 100 because the quoted margin is now lower than the required discount margin.",
            "C": "Rise above 100 to compensate the investor for higher credit risk."
        },
        "answer": "B",
        "explanation": "While the reference rate resets, the quoted margin ($QM$) does not change. When the issuer's credit spread widens, investors demand a higher discount margin ($DM > QM$). With the coupon stream lower than required market returns, the price falls below par ($P < 100$).",
        "distractor_analysis": {
            "A": "The coupon resets to the benchmark index, but does not adjust for issuer-specific credit spread widening.",
            "C": "Higher required return reduces bond market value, it does not increase it."
        }
    },

    # --- M15: Government Credit Analysis (8 Questions: 098 to 105) ---
    {
        "id": "L1-FI-098",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Sovereign and Government Credit Analysis",
        "los": "Describe factors evaluated in sovereign credit analysis.",
        "question": "Which of the following institutional and political factors is considered most favorable in sovereign credit rating assessments?",
        "options": {
            "A": "High concentration of political power in the executive branch with minimal checks and balances.",
            "B": "Strong rule of law, transparent public finances, and independent central banking institutions.",
            "C": "A fixed currency peg backed by limited foreign exchange reserves."
        },
        "answer": "B",
        "explanation": "Sovereign rating agencies (such as S&P, Moody's, and Fitch) place high weight on institutional effectiveness: strong rule of law, checks and balances, independent monetary authorities, and transparent fiscal governance enhance policy predictability and debt servicing commitment.",
        "distractor_analysis": {
            "A": "Concentration of power without institutional checks creates policy volatility and credit vulnerability.",
            "C": "Fixed pegs with low reserves expose the sovereign to currency and balance of payments crises."
        }
    },
    {
        "id": "L1-FI-099",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Sovereign and Government Credit Analysis",
        "los": "Distinguish between local currency and foreign currency sovereign debt ratings.",
        "question": "Why is a sovereign government's foreign currency credit rating typically equal to or lower than its local currency credit rating?",
        "options": {
            "A": "Foreign currency debt cannot be serviced by printing domestic currency and requires foreign exchange reserves or export surpluses.",
            "B": "Domestic currency debt carries higher legal priority in international court jurisdictions.",
            "C": "Sovereigns have unlimited statutory ability to levy taxes on foreign creditors."
        },
        "answer": "A",
        "explanation": "A sovereign possesses the sovereign prerogative to issue local currency, making outright default on local currency debt less common (though it can cause inflation). Foreign currency debt, however, requires earning or borrowing foreign exchange. If export receipts fall or reserves deplete, the sovereign cannot print foreign currency to repay debt, creating higher default risk.",
        "distractor_analysis": {
            "B": "Foreign currency debt often includes collective action clauses and foreign governing law that protects creditors more vigorously.",
            "C": "Sovereigns cannot tax foreign citizens outside their territorial jurisdiction."
        }
    },
    {
        "id": "L1-FI-100",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Sovereign and Government Credit Analysis",
        "los": "Calculate and interpret debt sustainability metrics for sovereign issuers.",
        "question": "A sovereign country has an initial government debt-to-GDP ratio of 60%. If the real interest rate on government debt is 4.0% and the country's real GDP growth rate is 1.5%, which condition is necessary to prevent the debt-to-GDP ratio from rising?",
        "options": {
            "A": "The government must run a primary fiscal surplus.",
            "B": "The government can run an unlimited primary fiscal deficit.",
            "C": "The nominal GDP growth rate must equal zero."
        },
        "answer": "A",
        "explanation": "The change in debt-to-GDP ratio is governed by: $$\\Delta d = (r - g) \\times d - pb$$ where $r$ is real interest rate, $g$ is real growth rate, and $pb$ is the primary balance as a % of GDP. Because $r > g$ ($4.0\\% > 1.5\\%$), the existing debt compounds faster than economic growth. To keep $\\Delta d \\le 0$, the government must generate a primary surplus ($pb > 0$) of at least: $$pb \\ge (0.04 - 0.015) \\times 0.60 = 0.015 = 1.50\\% \\text{ of GDP}$$",
        "distractor_analysis": {
            "B": "A primary deficit would accelerate debt accumulation when interest rate exceeds growth.",
            "C": "Nominal GDP growth of zero would worsen debt sustainability."
        }
    },
    {
        "id": "L1-FI-101",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Sovereign and Government Credit Analysis",
        "los": "Describe external accounts and reserve adequacy in sovereign credit assessment.",
        "question": "In evaluating a sovereign's external vulnerability, which indicator provides the strongest signal of resilience against sudden capital flight?",
        "options": {
            "A": "High ratio of short-term external debt to central bank foreign exchange reserves.",
            "B": "Foreign exchange reserves covering more than 100% of short-term external debt obligations (Greenspan-Guidotti rule).",
            "C": "A persistent current account deficit exceeding 8% of GDP financed by portfolio flows."
        },
        "answer": "B",
        "explanation": "The Greenspan-Guidotti benchmark requires usable foreign exchange reserves to cover at least 100% of external debt maturing within one year. This provides a critical liquidity cushion allowing the sovereign to service foreign liabilities during a balance-of-payments crisis without resorting to default.",
        "distractor_analysis": {
            "A": "High short-term debt relative to reserves indicates extreme rollover risk and vulnerability.",
            "C": "Large current account deficits funded by volatile hot-money portfolio flows heighten default risk."
        }
    },
    {
        "id": "L1-FI-102",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Sovereign and Government Credit Analysis",
        "los": "Describe the factors affecting municipal and non-sovereign government credit.",
        "question": "Which of the following factors is most critical when evaluating the creditworthiness of a regional non-sovereign government (e.g., a province or state)?",
        "options": {
            "A": "Monetary printing authority and sovereign seigniorage revenues.",
            "B": "Revenue generation autonomy, expenditure mandates, and intergovernmental transfer formulas.",
            "C": "Ability to issue currency in the international Eurobond market."
        },
        "answer": "B",
        "explanation": "Regional governments lack central banks and cannot print currency. Their credit strength depends on fiscal autonomy: the ability to raise local tax revenues independently, the flexibility of their public expenditure programs, and the stability of statutory transfer subsidies from the national central government.",
        "distractor_analysis": {
            "A": "Non-sovereign regional governments do not possess monetary authorities or currency printing rights.",
            "C": "Non-sovereigns rarely issue in sovereign debt formats and do not have sovereign monetary status."
        }
    },
    {
        "id": "L1-FI-103",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Sovereign and Government Credit Analysis",
        "los": "Explain sovereign default mechanisms and restructuring terms.",
        "question": "Collective Action Clauses (CACs) in sovereign bond indentures are designed to:",
        "options": {
            "A": "Prevent a supermajority of bondholders from agreeing to debt restructuring.",
            "B": "Enable a supermajority of bondholders to approve a restructuring that binds all bondholders, preventing holdout creditor litigation.",
            "C": "Provide an automatic sovereign guarantee from the International Monetary Fund."
        },
        "answer": "B",
        "explanation": "Collective Action Clauses (CACs) allow a specified supermajority of bondholders (e.g., 75%) to vote in favor of modifying repayment terms (haircuts, maturity extensions) and legally bind 100% of holders in the issue. This neutralizes minority 'holdout' creditors seeking full par recovery through court litigation.",
        "distractor_analysis": {
            "A": "CACs facilitate restructuring by enabling supermajority decisions, not preventing them.",
            "C": "The IMF provides conditional adjustment lending, not automated guarantees."
        }
    },
    {
        "id": "L1-FI-104",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Sovereign and Government Credit Analysis",
        "los": "Describe the economic structure and growth prospects in sovereign analysis.",
        "question": "A sovereign economy whose fiscal revenues and export base are 80% dependent on crude oil exports is most vulnerable to which credit risk?",
        "options": {
            "A": "Terms-of-trade shocks and procyclical fiscal revenue volatility.",
            "B": "Hyper-diversification drag on capital productivity.",
            "C": "Inability to implement countercyclical capital controls."
        },
        "answer": "A",
        "explanation": "Commodity-dependent sovereigns suffer from severe terms-of-trade volatility. A collapse in commodity prices sharply compresses export earnings, fiscal royalties, and tax receipts simultaneously, often forcing painful fiscal austerity or external debt restructuring.",
        "distractor_analysis": {
            "B": "The vulnerability is lack of diversification (monoline risk), not over-diversification.",
            "C": "Capital controls are an administrative policy choice, not the primary economic vulnerability."
        }
    },
    {
        "id": "L1-FI-105",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Sovereign and Government Credit Analysis",
        "los": "Describe non-economic factors in sovereign credit analysis.",
        "question": "Which demographic trend poses the greatest long-term structural threat to sovereign fiscal sustainability and sovereign credit ratings?",
        "options": {
            "A": "A growing working-age population with low dependency ratios.",
            "B": "An aging population with an increasing old-age dependency ratio that inflates public healthcare and pension obligations.",
            "C": "High net immigration of skilled technical labor."
        },
        "answer": "B",
        "explanation": "Rapid demographic aging increases entitlement spending (statutory pensions and healthcare) while simultaneously shrinking the active income-tax-paying labor base, leading to structural primary deficits unless offset by entitlement reform or productivity gains.",
        "distractor_analysis": {
            "A": "A growing workforce creates a demographic dividend that strengthens public finances.",
            "C": "Skilled immigration expands the tax base and mitigates dependency pressures."
        }
    },

    # --- M13: Empirical vs. Analytical Duration (7 Questions: 106 to 112) ---
    {
        "id": "L1-FI-106",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Empirical Duration and Yield Curve Sensitivity",
        "los": "Distinguish between analytical duration and empirical duration.",
        "question": "Analytical duration is derived from a mathematical pricing formula assuming benchmark yield shifts occur with credit spreads held constant. In contrast, empirical duration is determined by:",
        "options": {
            "A": "Linear regression analysis of historical bond price returns against historical benchmark yield changes.",
            "B": "Taking the second derivative of the price-yield curve with respect to convexity.",
            "C": "Calculating the Macaulay duration divided by the annualized coupon frequency."
        },
        "answer": "A",
        "explanation": "Empirical duration is an econometric measure estimated from statistical regressions of actual historical bond returns against changes in benchmark yields: $$\\Delta P/P = -D_{\\text{emp}} \\Delta y + \\epsilon$$ It captures real-world interactions where credit spreads often move inversely to benchmark government yields.",
        "distractor_analysis": {
            "B": "The second derivative measures convexity, not empirical duration.",
            "C": "Macaulay duration divided by $(1+y/m)$ is analytical modified duration."
        }
    },
    {
        "id": "L1-FI-107",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Empirical Duration and Yield Curve Sensitivity",
        "los": "Explain why empirical duration is lower than analytical duration for high-yield corporate bonds.",
        "question": "For high-yield corporate bonds, empirical duration is generally lower than analytical duration because:",
        "options": {
            "A": "High-yield bond prices are immune to changes in credit spreads.",
            "B": "Credit spreads typically compress during periods of economic expansion when benchmark yields are rising.",
            "C": "High-yield coupon payments reset continuously with the interbank lending rate."
        },
        "answer": "B",
        "explanation": "During economic expansions, central banks raise benchmark interest rates ($\Delta y_{\\text{benchmark}} > 0$), but robust corporate earnings reduce default risk, causing credit spreads to narrow ($\Delta \\text{Spread} < 0$). The tightening spread offsets part of the rise in benchmark yields, dampening bond price declines and resulting in empirical duration being noticeably lower than analytical duration.",
        "distractor_analysis": {
            "A": "High-yield bonds are heavily exposed to credit spreads; that correlation is precisely why duration differs.",
            "C": "High-yield bonds are predominantly fixed-rate coupon instruments, not daily floaters."
        }
    },
    {
        "id": "L1-FI-108",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Empirical Duration and Yield Curve Sensitivity",
        "los": "Compare interest rate sensitivity across rating categories.",
        "question": "In which bond market sector is the divergence between analytical modified duration and empirical duration smallest?",
        "options": {
            "A": "Distressed high-yield corporate debt.",
            "B": "High-grade AAA sovereign debt.",
            "C": "Subordinated contingent convertible bank debt."
        },
        "answer": "B",
        "explanation": "AAA sovereign debt carries zero or negligible credit spread risk. Because its price movements are driven almost entirely by changes in the benchmark yield curve itself, empirical regression estimates match mathematical analytical duration very closely.",
        "distractor_analysis": {
            "A": "Distressed debt is driven primarily by recovery expectations and equity-like credit risk, creating huge differences.",
            "C": "Contingent convertibles have strong equity and conversion dynamics that distort analytical bond duration."
        }
    },
    {
        "id": "L1-FI-109",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Empirical Duration and Yield Curve Sensitivity",
        "los": "Explain limitations of empirical duration.",
        "question": "A major limitation of using empirical duration for portfolio hedging is that:",
        "options": {
            "A": "It assumes that bond prices have zero relationship to coupon payments.",
            "B": "Historical statistical relationships between benchmark yields and credit spreads may break down during severe market crises.",
            "C": "It cannot be calculated using computer regression packages."
        },
        "answer": "B",
        "explanation": "Empirical duration depends on the historical covariance between benchmark yield shifts and credit spread adjustments. In periods of structural regime changes, liquidity freezes, or 'flight-to-safety' episodes (where benchmark yields collapse while credit spreads explode), the historical empirical correlation breaks down.",
        "distractor_analysis": {
            "A": "Empirical duration reflects actual total return price dynamics, which incorporate coupon effects.",
            "C": "It is straightforward to calculate via standard ordinary least squares (OLS) regression."
        }
    },
    {
        "id": "L1-FI-110",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Empirical Duration and Yield Curve Sensitivity",
        "los": "Calculate portfolio empirical price change under spread and benchmark shifts.",
        "question": "A high-yield bond has an analytical modified duration of 5.0 years and an empirical duration of 3.2 years. If benchmark Treasury yields increase by 100 bps, the expected percentage price change based on empirical duration is:",
        "options": {
            "A": "-5.0%",
            "B": "-3.2%",
            "C": "+1.8%"
        },
        "answer": "B",
        "explanation": "Using empirical duration: $$\\frac{\\Delta P}{P} \\approx -D_{\\text{emp}} \\times \\Delta y = -3.2 \\times (+1.00\\%) = -3.2\\%$$ This reflects the historical empirical fact that high-yield bonds suffer less price loss than pure analytical duration (-5.0%) predicts when interest rates rise.",
        "distractor_analysis": {
            "A": "-5.0% is based on analytical duration, which overstates price loss by ignoring spread tightening.",
            "C": "+1.8% represents the difference between the two durations ($5.0 - 3.2$), not the bond's percentage price return."
        }
    },
    {
        "id": "L1-FI-111",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Empirical Duration and Yield Curve Sensitivity",
        "los": "Describe key rate duration versus empirical duration.",
        "question": "Key rate duration measures a bond's price sensitivity to:",
        "options": {
            "A": "A change in benchmark yield at a specific maturity point along the yield curve with other rates held constant.",
            "B": "Changes in empirical credit spreads while holding the benchmark curve fixed.",
            "C": "Parallel shifts in the discount margin of floating-rate notes."
        },
        "answer": "A",
        "explanation": "Key rate duration (or partial duration) measures price sensitivity to a 100 bps change in the benchmark spot rate at a specific single key maturity point on the curve (e.g., 2-year, 5-year, 10-year, 30-year), holding yields at all other maturities constant. It allows portfolio managers to measure non-parallel yield curve risk.",
        "distractor_analysis": {
            "B": "Spread duration measures sensitivity to credit spread changes, not key rate curve shifts.",
            "C": "FRN discount margin sensitivity is measured by DM duration."
        }
    },
    {
        "id": "L1-FI-112",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Empirical Duration and Yield Curve Sensitivity",
        "los": "Describe effective duration for bonds with negative convexity.",
        "question": "When mortgage-backed securities (MBS) trade at prices near par, falling interest rates often cause effective duration to:",
        "options": {
            "A": "Increase due to positive convexity.",
            "B": "Decrease due to homeowners refinancing and prepaying mortgages (negative convexity).",
            "C": "Remain constant because mortgage pool rates are fixed."
        },
        "answer": "B",
        "explanation": "When mortgage rates drop, borrowers exercise prepayment options to refinance their loans. This accelerates cash flows returned to investors precisely when reinvestment rates are low. The expected maturity shortens, which compresses effective duration—the defining hallmark of negative convexity.",
        "distractor_analysis": {
            "A": "Positive convexity causes duration to increase as rates fall; MBS exhibit negative convexity.",
            "C": "Prepayment variability makes MBS cash flows and duration highly dynamic."
        }
    },

    # --- M3/M4/M5: Market Mechanics & Issuance (8 Questions: 113 to 120) ---
    {
        "id": "L1-FI-113",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Fixed-Income Markets: Issuance and Trading",
        "los": "Describe primary market issuance mechanisms for fixed-income securities.",
        "question": "In an underwritten corporate bond offering, which party bears the price risk if the bonds cannot be sold at the offering price?",
        "options": {
            "A": "The investment bank (underwriting syndicate).",
            "B": "The issuing corporation.",
            "C": "The central securities depository."
        },
        "answer": "A",
        "explanation": "In a firm-commitment underwritten offering, the investment bank or syndicate guarantees the purchase of the entire bond issue from the company at a negotiated price, subsequently reselling to investors. If market demand softens, the underwriters must absorb the price decline and inventory losses.",
        "distractor_analysis": {
            "B": "In a 'best-efforts' offering the issuer retains risk, but under firm underwriting the syndicate assumes it.",
            "C": "The depository provides clearing and settlement infrastructure, never taking principal underwriting risk."
        }
    },
    {
        "id": "L1-FI-114",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Fixed-Income Markets: Issuance and Trading",
        "los": "Describe sovereign bond auction mechanisms.",
        "question": "In a single-price (Dutch) sovereign bond auction, all successful competitive bidders and non-competitive bidders pay:",
        "options": {
            "A": "The highest price submitted by any competitive bidder.",
            "B": "The clearing price (stop-out yield) associated with the lowest winning bid.",
            "C": "Each individual bidder's own submitted price."
        },
        "answer": "B",
        "explanation": "In a single-price Dutch auction (such as US Treasury auctions), all accepted competitive bids and all non-competitive bids are awarded at a uniform single price—the stop-out price (highest yield) required to clear the total offering amount.",
        "distractor_analysis": {
            "A": "The highest price would fail to clear the total quantity offered.",
            "C": "Paying each individual bid price describes a multiple-price (discriminatory) auction."
        }
    },
    {
        "id": "L1-FI-115",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Fixed-Income Markets: Issuance and Trading",
        "los": "Describe shelf registration and private placements in corporate debt markets.",
        "question": "A major advantage of a shelf registration (e.g., SEC Rule 415) for a corporate bond issuer is:",
        "options": {
            "A": "Exemption from all financial disclosure requirements in annual regulatory filings.",
            "B": "The flexibility to issue debt securities in multiple tranches over time without filing a new prospectus for each issuance.",
            "C": "An absolute statutory guarantee that secondary trading will occur without bid-ask spreads."
        },
        "answer": "B",
        "explanation": "Shelf registration permits a qualified issuer to file a single master registration document covering a predetermined total volume of debt securities. The issuer can then 'take securities off the shelf' and sell tranches quickly when market conditions and interest rates are favorable.",
        "distractor_analysis": {
            "A": "Shelf issuers must maintain up-to-date regular disclosure filings (10-K, 10-Q).",
            "C": "Secondary market liquidity and spreads are market-driven and cannot be statutorily eliminated."
        }
    },
    {
        "id": "L1-FI-116",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Fixed-Income Markets: Issuance and Trading",
        "los": "Describe repurchase agreements (repos) and their funding mechanics.",
        "question": "In a repurchase agreement (repo), the difference between the sale price and the repurchase price of the underlying collateral represents the:",
        "options": {
            "A": "Haircut margin.",
            "B": "Repo interest cost.",
            "C": "Underwriting commission."
        },
        "answer": "B",
        "explanation": "A repo is economically a secured collateralized short-term loan. The cash borrower sells securities to the lender today and agrees to repurchase them at a higher price in the future. The dollar difference between the repurchase price and the initial sale price is the repo interest accrued at the repo rate.",
        "distractor_analysis": {
            "A": "The haircut is the percentage discount applied to the collateral's market value to determine loan principal.",
            "C": "Underwriting commissions apply to primary security issuance, not money market repo financing."
        }
    },
    {
        "id": "L1-FI-117",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Fixed-Income Markets: Issuance and Trading",
        "los": "Calculate repo interest and evaluate repo haircut factors.",
        "question": "Which of the following collateral characteristics will result in a lender requiring a LARGER repo haircut?",
        "options": {
            "A": "High credit quality, low price volatility, and high trading liquidity.",
            "B": "Low credit rating, high price volatility, and limited market liquidity.",
            "C": "Shorter time to maturity on sovereign Treasury bills."
        },
        "answer": "B",
        "explanation": "The repo haircut protects the cash lender against a decline in collateral value in the event that the borrower defaults. Lower credit quality, higher price volatility, and wider illiquidity increase the potential loss on collateral liquidation, necessitating a larger haircut buffer.",
        "distractor_analysis": {
            "A": "High credit and liquid collateral (like short Treasuries) command tiny haircuts (e.g., 0.5%–1%).",
            "C": "Short-maturity sovereign bills carry minimal price volatility, warranting low haircuts."
        }
    },
    {
        "id": "L1-FI-118",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Fixed-Income Markets: Issuance and Trading",
        "los": "Describe secondary market structures for fixed-income instruments.",
        "question": "The vast majority of global fixed-income secondary market trading occurs in:",
        "options": {
            "A": "Continuous, centralized order-driven public stock exchanges.",
            "B": "Over-the-counter (OTC) quote-driven dealer markets.",
            "C": "Pure call auctions held once weekly."
        },
        "answer": "B",
        "explanation": "Unlike equity markets, where trading is heavily concentrated on centralized order-driven electronic exchanges, fixed income is primarily traded in over-the-counter (OTC) dealer networks. Dealers hold inventory and post bid and ask quotes for institutional counterparties.",
        "distractor_analysis": {
            "A": "Exchange trading is rare for corporate and sovereign bonds due to the vast proliferation of individual CUSIPs.",
            "C": "Call auctions are used for sovereign primary auctions, not general day-to-day secondary liquidity."
        }
    },
    {
        "id": "L1-FI-119",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Fixed-Income Markets: Issuance and Trading",
        "los": "Describe settlement conventions and settlement cycles for bonds.",
        "question": "For major sovereign government bonds (such as US Treasuries), standard secondary market settlement convention is typically:",
        "options": {
            "A": "T + 0 (same day).",
            "B": "T + 1 (next business day).",
            "C": "T + 5 (five business days).",
        },
        "answer": "B",
        "explanation": "US government Treasuries settle on $T+1$ (the next business day following trade date). Corporate bonds and municipal bonds have also transitioned to a $T+1$ standard settlement cycle in modern US markets.",
        "distractor_analysis": {
            "A": "$T+0$ settlement is reserved for special cash trades or Fedwire money market operations.",
            "C": "$T+5$ was an obsolete historical settlement cycle from prior decades."
        }
    },
    {
        "id": "L1-FI-120",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Fixed-Income Markets: Issuance and Trading",
        "los": "Describe green bonds and sustainability-linked debt structures.",
        "question": "A fundamental difference between a 'Green Bond' and a 'Sustainability-Linked Bond' (SLB) is that a Green Bond:",
        "options": {
            "A": "Requires proceeds to be ring-fenced exclusively for eligible environmentally beneficial projects (use-of-proceeds).",
            "B": "Adjusts its coupon rate upward if the issuer fails to achieve targeted greenhouse gas reductions.",
            "C": "Is entirely unsecured while SLBs must be 100% asset-backed."
        },
        "answer": "A",
        "explanation": "A traditional Green Bond is a 'use-of-proceeds' instrument where the issuer contractually covenants to deploy 100% of proceeds into designated eligible green projects (e.g., renewable energy). In contrast, a Sustainability-Linked Bond (SLB) allows proceeds for general corporate purposes, but its coupon rate steps up or down based on whether the firm meets predefined key performance indicator (KPI) sustainability targets.",
        "distractor_analysis": {
            "B": "Coupon step-ups based on company-wide ESG target attainment are the signature mechanism of Sustainability-Linked Bonds (SLBs), not traditional Green Bonds.",
            "C": "Both Green Bonds and SLBs can be issued as senior unsecured corporate debentures."
        }
    }
]

updated_qs = existing_qs + new_questions
print(f"New total L1 FI questions: {len(updated_qs)}")

with open(FI_PATH, "w", encoding="utf-8") as f:
    json.dump(updated_qs, f, indent=2, ensure_ascii=False)

print(f"Successfully saved updated L1 FI questions to {FI_PATH}")
