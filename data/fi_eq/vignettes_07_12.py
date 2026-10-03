"""
Vignettes 07 to 12 for CFA Level 2 Fixed Income Question Bank.
Each vignette contains exactly 5 exam-grade clinical questions.
"""

VIGNETTES_07_12 = [
    # -------------------------------------------------------------------------
    # VIGNETTE 07
    # -------------------------------------------------------------------------
    {
        "id": "L2-FI-V07-Q1",
        "level": 2,
        "topic": "Fixed Income",
        "subtopic": "Option-Adjusted Spread (OAS) Analysis",
        "vignette_id": "V07",
        "vignette_title": "Option-Adjusted Spread (OAS), Zero-Volatility Spread, and Option Cost",
        "vignette_text": "Vanguard Credit Research analyst Diana Prince is evaluating whether corporate bonds issued by utilities and telecommunications companies are rich or cheap. Diana analyzes a 5-year callable corporate bond issued by Nexus Telecom trading at a market price of USD 98.25. The bond has a zero-volatility spread (Z-spread) of 165 bps over the benchmark spot curve. Using a binomial interest rate tree calibrated with 18% annual interest rate volatility, Diana solves for the constant spread added to all short rates that equates the tree model value to the market price: the Option-Adjusted Spread (OAS), which equals 115 bps. Diana is comparing OAS, Z-spread, and option cost across callable and putable peer issues.",
        "los": "Calculate and interpret the option cost in basis points, and describe how option-adjusted spread (OAS) is related to zero-volatility spread (Z-spread).",
        "question": "Based on Diana's analysis of Nexus Telecom's callable bond, the option cost of the embedded call option in basis points is closest to:",
        "options": {
            "A": "-50 bps",
            "B": "+50 bps",
            "C": "+280 bps"
        },
        "answer": "B",
        "explanation": "For a callable bond, the zero-volatility spread (Z-spread) compensates the investor for credit risk, liquidity risk, and the risk of the issuer calling the bond. The Option-Adjusted Spread (OAS) is the spread remaining after stripping out the cost of the embedded option (pure credit and liquidity spread). Therefore:\n$$\\text{Option Cost (bps)} = \\text{Z-spread} - \\text{OAS}$$\nGiven $\\text{Z-spread} = 165 \\text{ bps}$ and $\\text{OAS} = 115 \\text{ bps}$:\n$$\\text{Option Cost} = 165 \\text{ bps} - 115 \\text{ bps} = +50 \\text{ bps}$$\nBecause the call option is granted to the issuer, the investor requires a higher total spread (Z-spread) than the pure credit/liquidity spread (OAS); hence option cost is positive (+50 bps).",
        "distractor_analysis": {
            "A": "Incorrect. -50 bps is the option cost for a putable bond where the investor owns the option ($\\text{Option Cost} = \\text{Z-spread} - \\text{OAS} < 0$).",
            "C": "Incorrect. +280 bps is the sum of Z-spread and OAS ($165 + 115$), which has no economic meaning."
        }
    },
    {
        "id": "L2-FI-V07-Q2",
        "level": 2,
        "topic": "Fixed Income",
        "subtopic": "Option-Adjusted Spread (OAS) Analysis",
        "vignette_id": "V07",
        "vignette_title": "Option-Adjusted Spread (OAS), Zero-Volatility Spread, and Option Cost",
        "vignette_text": "Vanguard Credit Research analyst Diana Prince is evaluating whether corporate bonds issued by utilities and telecommunications companies are rich or cheap. Diana analyzes a 5-year callable corporate bond issued by Nexus Telecom trading at a market price of USD 98.25. The bond has a zero-volatility spread (Z-spread) of 165 bps over the benchmark spot curve. Using a binomial interest rate tree calibrated with 18% annual interest rate volatility, Diana solves for the constant spread added to all short rates that equates the tree model value to the market price: the Option-Adjusted Spread (OAS), which equals 115 bps. Diana is comparing OAS, Z-spread, and option cost across callable and putable peer issues.",
        "los": "Determine whether a bond with embedded options is underpriced or overpriced using option-adjusted spread.",
        "question": "Diana determines that the fair compensation for credit and liquidity risk for Nexus Telecom is 135 bps. Comparing this required spread to the bond's model OAS of 115 bps, Diana should conclude that the bond is:",
        "options": {
            "A": "Underpriced (cheap), because the market OAS is below the required credit spread.",
            "B": "Fairly priced, because the Z-spread of 165 bps exceeds the required spread.",
            "C": "Overpriced (rich), because the market OAS provides insufficient compensation for the bond's credit and liquidity risk."
        },
        "answer": "C",
        "explanation": "To determine relative value using OAS:\n- If $\\text{Market OAS} > \\text{Required Spread}$, the bond offers more spread compensation than required for its credit/liquidity risk, meaning the bond is underpriced (cheap / attractive buy).\n- If $\\text{Market OAS} < \\text{Required Spread}$, the bond offers less spread than required, indicating that investors are overpaying for the bond relative to its risk; therefore, the bond is overpriced (rich / avoid or sell).\nHere, the market OAS is 115 bps, which is below the analyst's required spread of 135 bps. Thus, the bond is overpriced (rich).",
        "distractor_analysis": {
            "A": "Incorrect. An OAS lower than the required spread indicates inadequate yield compensation, meaning the bond price is too high (rich), not cheap.",
            "B": "Incorrect. Comparing Z-spread to the required credit spread is erroneous because Z-spread includes compensation for the embedded call option."
        }
    },
    {
        "id": "L2-FI-V07-Q3",
        "level": 2,
        "topic": "Fixed Income",
        "subtopic": "Option-Adjusted Spread (OAS) Analysis",
        "vignette_id": "V07",
        "vignette_title": "Option-Adjusted Spread (OAS), Zero-Volatility Spread, and Option Cost",
        "vignette_text": "Vanguard Credit Research analyst Diana Prince is evaluating whether corporate bonds issued by utilities and telecommunications companies are rich or cheap. Diana analyzes a 5-year callable corporate bond issued by Nexus Telecom trading at a market price of USD 98.25. The bond has a zero-volatility spread (Z-spread) of 165 bps over the benchmark spot curve. Using a binomial interest rate tree calibrated with 18% annual interest rate volatility, Diana solves for the constant spread added to all short rates that equates the tree model value to the market price: the Option-Adjusted Spread (OAS), which equals 115 bps. Diana is comparing OAS, Z-spread, and option cost across callable and putable peer issues.",
        "los": "Describe the effect of changes in assumed interest rate volatility on the option-adjusted spread.",
        "question": "If Diana increases the assumed interest rate volatility input in her binomial pricing model from 18% to 22%, the calculated OAS for Nexus Telecom's callable bond will:",
        "options": {
            "A": "Decrease.",
            "B": "Increase.",
            "C": "Remain unchanged."
        },
        "answer": "A",
        "explanation": "When the assumed interest rate volatility increases:\n1. The model value of the embedded call option ($V_{\\text{call}}$) increases.\n2. In a callable bond, $V_{\\text{callable}} = V_{\\text{straight}} - V_{\\text{call}}$. Thus, higher assumed volatility reduces the theoretical model price of the callable bond for any given spread.\n3. To reconcile this lower theoretical model price back up to the fixed observed market price (USD 98.25), the discount spread added to the tree nodes must be reduced.\n4. Therefore, as assumed volatility increases, the calculated OAS of a callable bond decreases.\n(Conversely, for a putable bond, higher volatility increases the model put value, requiring a higher spread to match market price, so OAS increases).",
        "distractor_analysis": {
            "B": "Incorrect. OAS decreases for callable bonds when volatility increases; it increases for putable bonds.",
            "C": "Incorrect. OAS is directly sensitive to the volatility parameter because volatility determines option valuation."
        }
    },
    {
        "id": "L2-FI-V07-Q4",
        "level": 2,
        "topic": "Fixed Income",
        "subtopic": "Option-Adjusted Spread (OAS) Analysis",
        "vignette_id": "V07",
        "vignette_title": "Option-Adjusted Spread (OAS), Zero-Volatility Spread, and Option Cost",
        "vignette_text": "Vanguard Credit Research analyst Diana Prince is evaluating whether corporate bonds issued by utilities and telecommunications companies are rich or cheap. Diana analyzes a 5-year callable corporate bond issued by Nexus Telecom trading at a market price of USD 98.25. The bond has a zero-volatility spread (Z-spread) of 165 bps over the benchmark spot curve. Using a binomial interest rate tree calibrated with 18% annual interest rate volatility, Diana solves for the constant spread added to all short rates that equates the tree model value to the market price: the Option-Adjusted Spread (OAS), which equals 115 bps. Diana is comparing OAS, Z-spread, and option cost across callable and putable peer issues.",
        "los": "Compare the relationship between Z-spread and OAS for callable and putable bonds.",
        "question": "For an otherwise identical putable corporate bond, the relationship between its Option-Adjusted Spread (OAS) and its Zero-Volatility Spread (Z-spread) is best described as:",
        "options": {
            "A": "$$\\text{OAS}_{\\text{putable}} < \\text{Z-spread}_{\\text{putable}}$$",
            "B": "$$\\text{OAS}_{\\text{putable}} = \\text{Z-spread}_{\\text{putable}}$$",
            "C": "$$\\text{OAS}_{\\text{putable}} > \\text{Z-spread}_{\\text{putable}}$$"
        },
        "answer": "C",
        "explanation": "For a putable bond, the embedded option belongs to the bondholder. Because the investor benefits from the put feature, the market accepts a lower yield / spread on the putable bond:\n$$V_{\\text{putable}} = V_{\\text{straight}} + V_{\\text{put}}$$\nThe investor 'pays' for the put option by accepting a lower total spread (Z-spread) than the bond's pure credit and liquidity spread (OAS). Hence:\n$$\\text{Z-spread}_{\\text{putable}} = \\text{OAS} - \\text{Option Cost (bps)} \\implies \\text{OAS}_{\\text{putable}} > \\text{Z-spread}_{\\text{putable}}$$\nFor putable bonds, OAS strictly exceeds the Z-spread.",
        "distractor_analysis": {
            "A": "Incorrect. $\\text{OAS} < \\text{Z-spread}$ holds for callable bonds, where the investor must be compensated for granting the call option.",
            "B": "Incorrect. OAS equals Z-spread only for option-free straight bonds where the option cost is zero."
        }
    },
    {
        "id": "L2-FI-V07-Q5",
        "level": 2,
        "topic": "Fixed Income",
        "subtopic": "Option-Adjusted Spread (OAS) Analysis",
        "vignette_id": "V07",
        "vignette_title": "Option-Adjusted Spread (OAS), Zero-Volatility Spread, and Option Cost",
        "vignette_text": "Vanguard Credit Research analyst Diana Prince is evaluating whether corporate bonds issued by utilities and telecommunications companies are rich or cheap. Diana analyzes a 5-year callable corporate bond issued by Nexus Telecom trading at a market price of USD 98.25. The bond has a zero-volatility spread (Z-spread) of 165 bps over the benchmark spot curve. Using a binomial interest rate tree calibrated with 18% annual interest rate volatility, Diana solves for the constant spread added to all short rates that equates the tree model value to the market price: the Option-Adjusted Spread (OAS), which equals 115 bps. Diana is comparing OAS, Z-spread, and option cost across callable and putable peer issues.",
        "los": "Explain why option-adjusted spread is used to evaluate bonds with embedded options.",
        "question": "Why is the Option-Adjusted Spread (OAS) considered the superior metric compared to the nominal spread or Z-spread when comparing corporate bonds with different embedded call features?",
        "options": {
            "A": "OAS eliminates default risk from the corporate bond yield.",
            "B": "OAS removes the distortion caused by differing embedded option structures, isolating the pure compensation for credit and liquidity risk.",
            "C": "OAS guarantees that the bond's price will not change when benchmark interest rates shift."
        },
        "answer": "B",
        "explanation": "Bonds with embedded call options trade at different nominal yields and Z-spreads simply because of differences in call schedules, strike prices, and notice periods. The Z-spread bundles credit risk, liquidity risk, and option risk together. The OAS explicitly models and strips out the interest rate option component using an arbitrage-free lattice, leaving only the spread attributable to credit risk and liquidity risk. This allows portfolio managers to make direct apples-to-apples credit comparisons across bonds with varying option features.",
        "distractor_analysis": {
            "A": "Incorrect. OAS does not eliminate default risk; in fact, OAS is designed specifically to isolate and measure default and liquidity risk.",
            "C": "Incorrect. OAS is a spread metric, not a duration hedge, and does not guarantee price invariance to interest rate shifts."
        }
    },

    # -------------------------------------------------------------------------
    # VIGNETTE 08
    # -------------------------------------------------------------------------
    {
        "id": "L2-FI-V08-Q1",
        "level": 2,
        "topic": "Fixed Income",
        "subtopic": "Effective Duration and Convexity",
        "vignette_id": "V08",
        "vignette_title": "Empirical and Effective Risk Sensitivity for Asymmetric Cash Flows",
        "vignette_text": "Portfolio manager Kevin Zhang manages an institutional bond mandate with strict duration matching criteria. He is analyzing a 10-year callable corporate bond trading at USD 101.50 and an otherwise similar 10-year putable bond trading at USD 99.20. Traditional modified duration is inadequate due to interest-rate contingent cash flows. Kevin shifts the benchmark interest rate tree by $\\Delta y = \\pm 30 \\text{ bps}$ ($0.0030$) while holding the OAS constant. For the callable bond, the model price increases to USD 102.40 if yields drop 30 bps ($PV_-$) and falls to USD 99.80 if yields rise 30 bps ($PV_+$).",
        "los": "Calculate the effective duration of a bond with embedded options.",
        "question": "Based on Kevin's OAS-adjusted valuation model, the effective duration of the callable bond is closest to:",
        "options": {
            "A": "4.27",
            "B": "7.14",
            "C": "8.52"
        },
        "answer": "A",
        "explanation": "Effective duration measures the percentage price change of a bond for a given shift in benchmark interest rates, taking into account changes in interest-rate contingent cash flows:\n$$\\text{Effective Duration (ED)} = \\frac{PV_- - PV_+}{2 \\times \\Delta y \\times PV_0}$$\nGiven:\n- $PV_0 = \\text{USD } 101.50$\n- $PV_- = \\text{USD } 102.40$ (when yields decline by 30 bps)\n- $PV_+ = \\text{USD } 99.80$ (when yields rise by 30 bps)\n- $\\Delta y = 0.0030$\nCalculate:\n$$\\text{ED} = \\frac{102.40 - 99.80}{2 \\times 0.0030 \\times 101.50} = \\frac{2.60}{0.0060 \\times 101.50} = \\frac{2.60}{0.6090} = 4.2693 \\approx 4.27$$",
        "distractor_analysis": {
            "B": "Incorrect. 7.14 would be the typical modified duration of a straight 10-year bond, which overstates the callable bond's duration due to call compression.",
            "C": "Incorrect. 8.52 results from dividing by a single $\\Delta y$ instead of $2 \\times \\Delta y$ in the denominator."
        }
    },
    {
        "id": "L2-FI-V08-Q2",
        "level": 2,
        "topic": "Fixed Income",
        "subtopic": "Effective Duration and Convexity",
        "vignette_id": "V08",
        "vignette_title": "Empirical and Effective Risk Sensitivity for Asymmetric Cash Flows",
        "vignette_text": "Portfolio manager Kevin Zhang manages an institutional bond mandate with strict duration matching criteria. He is analyzing a 10-year callable corporate bond trading at USD 101.50 and an otherwise similar 10-year putable bond trading at USD 99.20. Traditional modified duration is inadequate due to interest-rate contingent cash flows. Kevin shifts the benchmark interest rate tree by $\\Delta y = \\pm 30 \\text{ bps}$ ($0.0030$) while holding the OAS constant. For the callable bond, the model price increases to USD 102.40 if yields drop 30 bps ($PV_-$) and falls to USD 99.80 if yields rise 30 bps ($PV_+$).",
        "los": "Calculate the effective convexity of a bond with embedded options, and interpret the sign of effective convexity.",
        "question": "Using the same model inputs, the effective convexity of the callable bond is closest to:",
        "options": {
            "A": "-145.8",
            "B": "-875.2",
            "C": "+124.5"
        },
        "answer": "B",
        "explanation": "Effective convexity measures the curvature of the price-yield relationship taking cash flow adjustments into account:\n$$\\text{Effective Convexity (EC)} = \\frac{PV_- + PV_+ - 2 \\times PV_0}{(\\Delta y)^2 \\times PV_0}$$\nSubstitute the values:\n- $PV_- = 102.40$\n- $PV_+ = 99.80$\n- $PV_0 = 101.50$\n- $\\Delta y = 0.0030$\nCalculate numerator:\n$$PV_- + PV_+ - 2 \\times PV_0 = 102.40 + 99.80 - 2 \\times (101.50) = 202.20 - 203.00 = -0.80$$\nCalculate denominator:\n$$(\\Delta y)^2 \\times PV_0 = (0.0030)^2 \\times 101.50 = 0.000009 \\times 101.50 = 0.0009135$$\nCalculate EC:\n$$\\text{EC} = \\frac{-0.80}{0.0009135} = -875.75 \\approx -875.2$$\nThe negative sign confirms that the callable bond exhibits negative convexity around this price/yield level.",
        "distractor_analysis": {
            "A": "Incorrect. -145.8 results from using $\\Delta y = 0.01$ instead of $0.0030$ in the denominator squaring.",
            "C": "Incorrect. +124.5 assumes positive convexity, which contradicts the behavior of a callable bond trading near or above par."
        }
    },
    {
        "id": "L2-FI-V08-Q3",
        "level": 2,
        "topic": "Fixed Income",
        "subtopic": "Effective Duration and Convexity",
        "vignette_id": "V08",
        "vignette_title": "Empirical and Effective Risk Sensitivity for Asymmetric Cash Flows",
        "vignette_text": "Portfolio manager Kevin Zhang manages an institutional bond mandate with strict duration matching criteria. He is analyzing a 10-year callable corporate bond trading at USD 101.50 and an otherwise similar 10-year putable bond trading at USD 99.20. Traditional modified duration is inadequate due to interest-rate contingent cash flows. Kevin shifts the benchmark interest rate tree by $\\Delta y = \\pm 30 \\text{ bps}$ ($0.0030$) while holding the OAS constant. For the callable bond, the model price increases to USD 102.40 if yields drop 30 bps ($PV_-$) and falls to USD 99.80 if yields rise 30 bps ($PV_+$).",
        "los": "Describe key rate duration and evaluate its use in analyzing the sensitivity of a bond portfolio to non-parallel yield curve shifts.",
        "question": "Kevin examines the Key Rate Durations (KRDs) of the callable bond. If the bond is trading with a high probability of being called at Year 3, which of the following distributions of key rate durations will most likely be observed?",
        "options": {
            "A": "The 10-year key rate duration will dominate, with near-zero duration at maturities 1 through 5 years.",
            "B": "The key rate durations will be highest around the 2-year and 3-year maturities, while the 10-year key rate duration will drop significantly toward zero.",
            "C": "Key rate durations will be distributed equally across all maturities from 1 to 10 years."
        },
        "answer": "B",
        "explanation": "Key rate duration measures price sensitivity to a shift in a single benchmark spot rate while keeping all other rates constant. When a callable bond is highly likely to be called (in-the-money call option at Year 3), its effective maturity compresses from 10 years to approximately 3 years. The bond's cash flows beyond Year 3 are unlikely to be received. Consequently, the bond becomes sensitive primarily to shifts in the 2-year and 3-year key rates, and its sensitivity to the 10-year key rate drops toward zero.",
        "distractor_analysis": {
            "A": "Incorrect. A dominant 10-year key rate duration characterizes an option-free straight bond or a callable bond where the call is deeply out-of-the-money.",
            "C": "Incorrect. Key rate durations reflect cash flow timing; they are not uniformly equal across all maturities."
        }
    },
    {
        "id": "L2-FI-V08-Q4",
        "level": 2,
        "topic": "Fixed Income",
        "subtopic": "Effective Duration and Convexity",
        "vignette_id": "V08",
        "vignette_title": "Empirical and Effective Risk Sensitivity for Asymmetric Cash Flows",
        "vignette_text": "Portfolio manager Kevin Zhang manages an institutional bond mandate with strict duration matching criteria. He is analyzing a 10-year callable corporate bond trading at USD 101.50 and an otherwise similar 10-year putable bond trading at USD 99.20. Traditional modified duration is inadequate due to interest-rate contingent cash flows. Kevin shifts the benchmark interest rate tree by $\\Delta y = \\pm 30 \\text{ bps}$ ($0.0030$) while holding the OAS constant. For the callable bond, the model price increases to USD 102.40 if yields drop 30 bps ($PV_-$) and falls to USD 99.80 if yields rise 30 bps ($PV_+$).",
        "los": "Describe one-sided durations and their importance for bonds with embedded options.",
        "question": "For a callable bond trading near its call price, how does its one-sided 'down-duration' ($ED_-$) compare to its one-sided 'up-duration' ($ED_+$)?",
        "options": {
            "A": "$$ED_- > ED_+$$",
            "B": "$$ED_- = ED_+$$",
            "C": "$$ED_- < ED_+$$"
        },
        "answer": "C",
        "explanation": "One-sided durations measure price sensitivity to an isolated downward or upward shift in interest rates:\n- $ED_-$ measures sensitivity when rates fall ($\\% \\Delta P$ when rates decrease).\n- $ED_+$ measures sensitivity when rates rise ($\\% \\Delta P$ when rates increase).\nWhen a callable bond trades near its call price, a further decline in yields increases the likelihood of the call being exercised, capping price appreciation ($PV_-$ changes little; small price response). Conversely, if yields rise, the call moves out-of-the-money and the bond's maturity extends toward its full 10-year life, suffering substantial price depreciation ($PV_+$ drops sharply; large price response). Therefore, $ED_- < ED_+$.",
        "distractor_analysis": {
            "A": "Incorrect. $ED_- > ED_+$ applies to putable bonds, where downside rate moves yield full straight-bond appreciation while upside rate moves are floored by the put.",
            "B": "Incorrect. One-sided durations are equal only for option-free straight bonds with symmetric price changes."
        }
    },
    {
        "id": "L2-FI-V08-Q5",
        "level": 2,
        "topic": "Fixed Income",
        "subtopic": "Effective Duration and Convexity",
        "vignette_id": "V08",
        "vignette_title": "Empirical and Effective Risk Sensitivity for Asymmetric Cash Flows",
        "vignette_text": "Portfolio manager Kevin Zhang manages an institutional bond mandate with strict duration matching criteria. He is analyzing a 10-year callable corporate bond trading at USD 101.50 and an otherwise similar 10-year putable bond trading at USD 99.20. Traditional modified duration is inadequate due to interest-rate contingent cash flows. Kevin shifts the benchmark interest rate tree by $\\Delta y = \\pm 30 \\text{ bps}$ ($0.0030$) while holding the OAS constant. For the callable bond, the model price increases to USD 102.40 if yields drop 30 bps ($PV_-$) and falls to USD 99.80 if yields rise 30 bps ($PV_+$).",
        "los": "Explain why modified duration is an inappropriate measure of interest rate sensitivity for bonds with embedded options.",
        "question": "Modified duration is an inappropriate risk measure for bonds with embedded options primarily because it:",
        "options": {
            "A": "Assumes that future cash flows are fixed and do not alter when interest rates change.",
            "B": "Fails to discount cash flows using the spot rate curve.",
            "C": "Cannot be calculated for bonds with maturities exceeding 5 years."
        },
        "answer": "A",
        "explanation": "Modified duration and Macaulay duration are derived under the strict mathematical assumption that the bond's cash flows (coupons and principal repayment dates) are completely fixed and invariant to interest rate movements. For bonds with embedded options (callable, putable, prepayable MBS), future cash flows are contingent on the path of interest rates. Effective duration must be used instead because it re-estimates cash flows at each node of a calibrated lattice or Monte Carlo simulation when yields shift.",
        "distractor_analysis": {
            "B": "Incorrect. Modified duration is based on yield to maturity, but the failure to adjust cash flows is the core fatal flaw for option-embedded bonds.",
            "C": "Incorrect. Modified duration can be calculated for any maturity; its limitation is cash-flow fixity, not tenor length."
        }
    },

    # -------------------------------------------------------------------------
    # VIGNETTE 09
    # -------------------------------------------------------------------------
    {
        "id": "L2-FI-V09-Q1",
        "level": 2,
        "topic": "Fixed Income",
        "subtopic": "Structural Credit Models",
        "vignette_id": "V09",
        "vignette_title": "Merton Structural Model and Firm Capital Structure as Contingent Claims",
        "vignette_text": "Quantitative credit analyst Samuel O'Connor uses the Merton (1974) structural credit risk model to evaluate the default probability and credit spread of Sterling Logistics. The firm's capital structure consists of equity and a single zero-coupon debt issue with face value $K = \\text{USD } 180 \\text{ million}$ maturing in 1 year ($T = 1$). The current market value of the firm's total assets is $V_0 = \\text{USD } 250 \\text{ million}$, asset return volatility is $\\sigma_V = 22\\%$, and the annualized risk-free interest rate is $r = 4.00\\%$. Samuel models equity as a European call option on firm assets: $E = C(V, K, T)$.",
        "los": "Describe the structural approach to credit risk modeling (Merton model), including modeling equity as a call option and debt as a put option.",
        "question": "In the Merton structural model, the market value of the firm's debt ($D$) at time $t = 0$ can be represented as:",
        "options": {
            "A": "$$D = K e^{-rT} + P(V, K, T)$$",
            "B": "$$D = V_0 - C(V, K, T) = K e^{-rT} - P(V, K, T)$$",
            "C": "$$D = C(V, K, T) - K e^{-rT}$$"
        },
        "answer": "B",
        "explanation": "In the Merton framework, the total asset value is $V = E + D$. Equityholders have limited liability and hold a residual claim on the firm's assets after repaying debt $K$ at maturity $T$. Thus:\n$$E = C(V, K, T) = \\max(V_T - K, 0)$$\nUsing the accounting identity $D = V - E$ and put-call parity ($C - P = V - K e^{-rT} \\implies V - C = K e^{-rT} - P$):\n$$D = V_0 - C(V, K, T) = K e^{-rT} - P(V, K, T)$$\nEconomically, debtholders own a risk-free bond with face value $K$ and have written a European put option on the firm's assets to the equityholders with strike price $K$. If $V_T < K$, the equityholders exercise their put (defaulting and walking away), transferring the assets $V_T$ to debtholders.",
        "distractor_analysis": {
            "A": "Incorrect. Debtholders are short the put option, so the put value is subtracted from the risk-free bond ($K e^{-rT} - P$), not added.",
            "C": "Incorrect. Violates put-call parity and basic contingent claims pricing."
        }
    },
    {
        "id": "L2-FI-V09-Q2",
        "level": 2,
        "topic": "Fixed Income",
        "subtopic": "Structural Credit Models",
        "vignette_id": "V09",
        "vignette_title": "Merton Structural Model and Firm Capital Structure as Contingent Claims",
        "vignette_text": "Quantitative credit analyst Samuel O'Connor uses the Merton (1974) structural credit risk model to evaluate the default probability and credit spread of Sterling Logistics. The firm's capital structure consists of equity and a single zero-coupon debt issue with face value $K = \\text{USD } 180 \\text{ million}$ maturing in 1 year ($T = 1$). The current market value of the firm's total assets is $V_0 = \\text{USD } 250 \\text{ million}$, asset return volatility is $\\sigma_V = 22\\%$, and the annualized risk-free interest rate is $r = 4.00\\%$. Samuel models equity as a European call option on firm assets: $E = C(V, K, T)$.",
        "los": "Calculate and interpret the distance to default and risk-neutral probability of default in the Merton model.",
        "question": "Using the inputs for Sterling Logistics, the parameter $d_2$ from the Black-Scholes-Merton formula is closest to:",
        "options": {
            "A": "1.35",
            "B": "1.57",
            "C": "1.79"
        },
        "answer": "B",
        "explanation": "In the Black-Scholes-Merton formula:\n$$d_1 = \\frac{\\ln(V_0 / K) + (r + 0.5 \\sigma_V^2)T}{\\sigma_V \\sqrt{T}}$$\n$$d_2 = d_1 - \\sigma_V \\sqrt{T}$$\nSubstitute the values ($V_0 = 250$, $K = 180$, $r = 0.04$, $\\sigma_V = 0.22$, $T = 1$):\n$$\\ln(250 / 180) = \\ln(1.388889) = 0.328504$$\n$$r + 0.5 \\sigma_V^2 = 0.04 + 0.5 \\times (0.22)^2 = 0.04 + 0.0242 = 0.0642$$\n$$\\sigma_V \\sqrt{T} = 0.22 \\times 1 = 0.22$$\nCalculate $d_1$:\n$$d_1 = \\frac{0.328504 + 0.0642}{0.22} = \\frac{0.392704}{0.22} = 1.7850$$\nCalculate $d_2$:\n$$d_2 = 1.7850 - 0.22 = 1.5650 \\approx 1.57$$\nNote that $d_2$ represents the distance to default in standard deviation units under the risk-neutral measure, and $N(-d_2)$ gives the risk-neutral probability of default.",
        "distractor_analysis": {
            "A": "Incorrect. 1.35 results from omitting the drift term $(r + 0.5\\sigma_V^2)T$ in the numerator: $\\frac{0.3285}{0.22} - 0.22 = 1.49 - 0.22 = 1.27$, or misapplying volatility.",
            "C": "Incorrect. 1.79 is $d_1$, not $d_2$ ($d_2 = d_1 - \\sigma_V \\sqrt{T} = 1.785 - 0.22 = 1.565$)."
        }
    },
    {
        "id": "L2-FI-V09-Q3",
        "level": 2,
        "topic": "Fixed Income",
        "subtopic": "Structural Credit Models",
        "vignette_id": "V09",
        "vignette_title": "Merton Structural Model and Firm Capital Structure as Contingent Claims",
        "vignette_text": "Quantitative credit analyst Samuel O'Connor uses the Merton (1974) structural credit risk model to evaluate the default probability and credit spread of Sterling Logistics. The firm's capital structure consists of equity and a single zero-coupon debt issue with face value $K = \\text{USD } 180 \\text{ million}$ maturing in 1 year ($T = 1$). The current market value of the firm's total assets is $V_0 = \\text{USD } 250 \\text{ million}$, asset return volatility is $\\sigma_V = 22\\%$, and the annualized risk-free interest rate is $r = 4.00\\%$. Samuel models equity as a European call option on firm assets: $E = C(V, K, T)$.",
        "los": "Calculate the credit spread of a zero-coupon bond in the Merton structural model.",
        "question": "Under the Merton model, if the market value of Sterling Logistics' debt is USD 167.50 million, the continuously compounded credit spread on the debt is closest to:",
        "options": {
            "A": "3.19%",
            "B": "4.00%",
            "C": "7.19%"
        },
        "answer": "A",
        "explanation": "The yield to maturity on the zero-coupon debt ($y_D$) under continuous compounding is given by:\n$$D = K e^{-y_D T} \\implies y_D = -\\frac{1}{T}\\ln\\left(\\frac{D}{K}\\right)$$\nSubstitute $D = 167.50$, $K = 180$, and $T = 1$:\n$$y_D = -\\ln\\left(\\frac{167.50}{180}\\right) = -\\ln(0.930556) = -(-0.071973) = 7.197\\%$$\nThe credit spread ($s$) is the yield on the risky debt minus the risk-free rate ($r = 4.00\\%$):\n$$s = y_D - r = 7.197\\% - 4.00\\% = 3.197\\% \\approx 3.19\\% = 319 \\text{ bps}$$",
        "distractor_analysis": {
            "B": "Incorrect. 4.00% is the risk-free rate itself ($r$).",
            "C": "Incorrect. 7.19% is the total yield to maturity ($y_D$) of the risky debt, not the credit spread over the risk-free rate."
        }
    },
    {
        "id": "L2-FI-V09-Q4",
        "level": 2,
        "topic": "Fixed Income",
        "subtopic": "Structural Credit Models",
        "vignette_id": "V09",
        "vignette_title": "Merton Structural Model and Firm Capital Structure as Contingent Claims",
        "vignette_text": "Quantitative credit analyst Samuel O'Connor uses the Merton (1974) structural credit risk model to evaluate the default probability and credit spread of Sterling Logistics. The firm's capital structure consists of equity and a single zero-coupon debt issue with face value $K = \\text{USD } 180 \\text{ million}$ maturing in 1 year ($T = 1$). The current market value of the firm's total assets is $V_0 = \\text{USD } 250 \\text{ million}$, asset return volatility is $\\sigma_V = 22\\%$, and the annualized risk-free interest rate is $r = 4.00\\%$. Samuel models equity as a European call option on firm assets: $E = C(V, K, T)$.",
        "los": "Describe the assumptions and limitations of the Merton structural model.",
        "question": "Which of the following is a primary practical limitation of implementing the Merton structural model in live credit analysis?",
        "options": {
            "A": "It assumes that default can occur at any time prior to debt maturity.",
            "B": "Firm asset value $V$ and asset return volatility $\\sigma_V$ are not directly observable in financial markets.",
            "C": "It cannot incorporate debt instruments with fixed principal amounts."
        },
        "answer": "B",
        "explanation": "A major practical hurdle of structural models is that the total market value of the firm's assets ($V$) and the volatility of firm assets ($\\sigma_V$) cannot be directly observed from market prices because only publicly traded equity (and sometimes debt) is quoted. Analysts must iteratively infer $V$ and $\\sigma_V$ from equity market capitalization and equity volatility using simultaneous nonlinear equations.\nAdditional limitations include the assumption of a single zero-coupon debt maturing at $T$ (default can only occur at maturity, not before), and constant risk-free rates.",
        "distractor_analysis": {
            "A": "Incorrect. In the Merton model, default can ONLY occur at maturity $T$; this is a recognized unrealistic assumption of the model.",
            "C": "Incorrect. The Merton model explicitly models debt with a fixed face value $K$."
        }
    },
    {
        "id": "L2-FI-V09-Q5",
        "level": 2,
        "topic": "Fixed Income",
        "subtopic": "Structural Credit Models",
        "vignette_id": "V09",
        "vignette_title": "Merton Structural Model and Firm Capital Structure as Contingent Claims",
        "vignette_text": "Quantitative credit analyst Samuel O'Connor uses the Merton (1974) structural credit risk model to evaluate the default probability and credit spread of Sterling Logistics. The firm's capital structure consists of equity and a single zero-coupon debt issue with face value $K = \\text{USD } 180 \\text{ million}$ maturing in 1 year ($T = 1$). The current market value of the firm's total assets is $V_0 = \\text{USD } 250 \\text{ million}$, asset return volatility is $\\sigma_V = 22\\%$, and the annualized risk-free interest rate is $r = 4.00\\%$. Samuel models equity as a European call option on firm assets: $E = C(V, K, T)$.",
        "los": "Describe how changes in asset volatility and leverage affect equity value and debt value in structural models.",
        "question": "If Sterling Logistics increases its asset risk such that asset volatility $\\sigma_V$ increases from 22% to 35% without changing total asset value $V_0$, what is the impact on equity value and debt value?",
        "options": {
            "A": "Equity value increases; debt value decreases.",
            "B": "Equity value decreases; debt value increases.",
            "C": "Both equity value and debt value increase due to expanded firm optionality."
        },
        "answer": "A",
        "explanation": "In contingent claims analysis:\n- Equity is a call option on firm assets ($E = C(V, K, T)$).\n- Debt is $D = V_0 - E = K e^{-rT} - P(V, K, T)$.\nOption values (both calls and puts) are monotonically increasing in volatility ($\\text{Vega} > 0$). When $\\sigma_V$ rises:\n1. The call option value increases, so equity value ($E$) increases.\n2. The put option written by debtholders ($P$) increases in value, meaning the short put position loses value, so debt value ($D = V_0 - E$) decreases.\nThis represents the classic 'asset substitution' (risk-shifting) problem: equityholders gain from higher volatility at the expense of debtholders.",
        "distractor_analysis": {
            "B": "Incorrect. Reverses the relationship; equity gains from upside volatility while limited liability protects downside.",
            "C": "Incorrect. Firm value $V_0$ is fixed ($V_0 = E + D$). A gain in equity must come directly at the expense of debt."
        }
    },

    # -------------------------------------------------------------------------
    # VIGNETTE 10
    # -------------------------------------------------------------------------
    {
        "id": "L2-FI-V10-Q1",
        "level": 2,
        "topic": "Fixed Income",
        "subtopic": "Reduced-Form Credit Models",
        "vignette_id": "V10",
        "vignette_title": "Intensity-Based Reduced-Form Credit Models and Hazard Rate Estimation",
        "vignette_text": "Credit derivatives desk strategist Liam Gallagher develops intensity-based (reduced-form) credit risk models for corporate bond portfolios. Unlike structural models, reduced-form models treat default as an unpredictable exogenous event governed by a Poisson jump process with hazard rate (default intensity) $\\lambda(t)$. Liam estimates a constant hazard rate $\\lambda = 2.50\\%$ per annum for an issuer, with an assumed recovery rate of $R = 40\\%$ upon default.",
        "los": "Calculate the cumulative probability of default and survival probability using a hazard rate.",
        "question": "Based on Liam's estimated constant hazard rate of 2.50% per annum, the cumulative probability of default over a 3-year horizon, $PD(3)$, is closest to:",
        "options": {
            "A": "7.23%",
            "B": "7.50%",
            "C": "92.77%"
        },
        "answer": "A",
        "explanation": "Under a constant hazard rate $\\lambda$, survival probability through time $t$ is governed by an exponential decay distribution:\n$$S(t) = e^{-\\lambda t}$$\nFor $t = 3$ years and $\\lambda = 0.025$:\n$$S(3) = e^{-0.025 \\times 3} = e^{-0.075} = 0.927744$$\nThe cumulative probability of default over 3 years is the complement of the survival probability:\n$$PD(3) = 1 - S(3) = 1 - 0.927744 = 0.072256 \\approx 7.23\\%$$",
        "distractor_analysis": {
            "B": "Incorrect. 7.50% is the simple linear sum ($3 \\times 2.50\\% = 7.50\\%$), which ignores the compounding conditional survival probability.",
            "C": "Incorrect. 92.77% is the survival probability $S(3)$, not the probability of default $PD(3)$."
        }
    },
    {
        "id": "L2-FI-V10-Q2",
        "level": 2,
        "topic": "Fixed Income",
        "subtopic": "Reduced-Form Credit Models",
        "vignette_id": "V10",
        "vignette_title": "Intensity-Based Reduced-Form Credit Models and Hazard Rate Estimation",
        "vignette_text": "Credit derivatives desk strategist Liam Gallagher develops intensity-based (reduced-form) credit risk models for corporate bond portfolios. Unlike structural models, reduced-form models treat default as an unpredictable exogenous event governed by a Poisson jump process with hazard rate (default intensity) $\\lambda(t)$. Liam estimates a constant hazard rate $\\lambda = 2.50\\%$ per annum for an issuer, with an assumed recovery rate of $R = 40\\%$ upon default.",
        "los": "Calculate the credit spread under the reduced-form model.",
        "question": "Using the approximation formula in reduced-form credit modeling, the model-implied credit spread ($s$) is closest to:",
        "options": {
            "A": "1.00%",
            "B": "1.50%",
            "C": "2.50%"
        },
        "answer": "B",
        "explanation": "In reduced-form models, the credit spread is approximately equal to the product of the hazard rate (default intensity $\\lambda$) and the loss given default ($LGD = 1 - R$):\n$$s \\approx \\lambda \\times (1 - R)$$\nGiven $\\lambda = 2.50\\%$ and recovery rate $R = 40\\%$:\n$$LGD = 1 - 0.40 = 0.60$$\n$$s \\approx 0.025 \\times 0.60 = 0.0150 = 1.50\\% = 150 \\text{ bps}$$",
        "distractor_analysis": {
            "A": "Incorrect. 1.00% is computed using the recovery rate rather than LGD: $\\lambda \\times R = 2.50\\% \\times 0.40 = 1.00\\%$.",
            "C": "Incorrect. 2.50% is the hazard rate $\\lambda$, assuming a zero recovery rate ($R = 0$)."
        }
    },
    {
        "id": "L2-FI-V10-Q3",
        "level": 2,
        "topic": "Fixed Income",
        "subtopic": "Reduced-Form Credit Models",
        "vignette_id": "V10",
        "vignette_title": "Intensity-Based Reduced-Form Credit Models and Hazard Rate Estimation",
        "vignette_text": "Credit derivatives desk strategist Liam Gallagher develops intensity-based (reduced-form) credit risk models for corporate bond portfolios. Unlike structural models, reduced-form models treat default as an unpredictable exogenous event governed by a Poisson jump process with hazard rate (default intensity) $\\lambda(t)$. Liam estimates a constant hazard rate $\\lambda = 2.50\\%$ per annum for an issuer, with an assumed recovery rate of $R = 40\\%$ upon default.",
        "los": "Compare structural and reduced-form models of credit risk.",
        "question": "Which of the following characteristics is a defining advantage of reduced-form models over structural models?",
        "options": {
            "A": "Reduced-form models allow default to occur unexpectedly at any time and can be calibrated directly to observable market prices of debt and CDS.",
            "B": "Reduced-form models provide an economic explanation for why default occurs based on asset value and balance sheet leverage.",
            "C": "Reduced-form models do not require specification of a recovery rate."
        },
        "answer": "A",
        "explanation": "Reduced-form models have two key advantages over structural models:\n1. Default is modeled as an exogenous Poisson arrival, meaning default can happen unexpectedly at any point in time (matching empirical credit spread behavior at short maturities).\n2. Model parameters (hazard rates $\\lambda$) can be calibrated directly to observable market prices of corporate bonds, credit default swaps (CDS), and macroeconomic variables, rather than relying on unobservable balance sheet asset values ($V$) and asset volatilities ($\\sigma_V$).",
        "distractor_analysis": {
            "B": "Incorrect. Explaining the economic cause of default based on balance sheet leverage is the primary feature of structural models, not reduced-form models.",
            "C": "Incorrect. Reduced-form models explicitly require an assumed recovery rate or loss given default input."
        }
    },
    {
        "id": "L2-FI-V10-Q4",
        "level": 2,
        "topic": "Fixed Income",
        "subtopic": "Reduced-Form Credit Models",
        "vignette_id": "V10",
        "vignette_title": "Intensity-Based Reduced-Form Credit Models and Hazard Rate Estimation",
        "vignette_text": "Credit derivatives desk strategist Liam Gallagher develops intensity-based (reduced-form) credit risk models for corporate bond portfolios. Unlike structural models, reduced-form models treat default as an unpredictable exogenous event governed by a Poisson jump process with hazard rate (default intensity) $\\lambda(t)$. Liam estimates a constant hazard rate $\\lambda = 2.50\\%$ per annum for an issuer, with an assumed recovery rate of $R = 40\\%$ upon default.",
        "los": "Calculate expected loss on a bond using conditional default probability and loss given default.",
        "question": "For a 1-year horizon on a bond with par value USD 100, if the hazard rate for Year 1 is 2.50% and recovery rate is 40%, the expected loss ($EL$) in currency units is closest to:",
        "options": {
            "A": "USD 0.98",
            "B": "USD 1.48",
            "C": "USD 2.47"
        },
        "answer": "B",
        "explanation": "Expected Loss ($EL$) is defined as:\n$$EL = \\text{Exposure at Default (EAD)} \\times \\text{Probability of Default (PD)} \\times \\text{Loss Given Default (LGD)}$$\n1. $\\text{EAD} = \\text{USD } 100$.\n2. $PD(1) = 1 - e^{-\\lambda \\times 1} = 1 - e^{-0.025} = 1 - 0.97531 = 0.02469 = 2.469\\%$.\n3. $LGD = 1 - R = 1 - 0.40 = 60\\%$.\n$$EL = 100 \\times 0.02469 \\times 0.60 = \\text{USD } 1.4814 \\approx \\text{USD } 1.48$$",
        "distractor_analysis": {
            "A": "Incorrect. USD 0.98 is calculated using $R = 40\\%$ instead of $LGD = 60\\%$ ($100 \\times 0.02469 \\times 0.40 = 0.988$).",
            "C": "Incorrect. USD 2.47 is the total default probability exposure without taking into account the recovery value ($100 \\times 0.02469 = 2.47$)."
        }
    },
    {
        "id": "L2-FI-V10-Q5",
        "level": 2,
        "topic": "Fixed Income",
        "subtopic": "Reduced-Form Credit Models",
        "vignette_id": "V10",
        "vignette_title": "Intensity-Based Reduced-Form Credit Models and Hazard Rate Estimation",
        "vignette_text": "Credit derivatives desk strategist Liam Gallagher develops intensity-based (reduced-form) credit risk models for corporate bond portfolios. Unlike structural models, reduced-form models treat default as an unpredictable exogenous event governed by a Poisson jump process with hazard rate (default intensity) $\\lambda(t)$. Liam estimates a constant hazard rate $\\lambda = 2.50\\%$ per annum for an issuer, with an assumed recovery rate of $R = 40\\%$ upon default.",
        "los": "Describe how macroeconomic variables are incorporated into reduced-form credit models.",
        "question": "In advanced reduced-form models, how is the default intensity $\\lambda_t$ typically specified to reflect the macroeconomic credit cycle?",
        "options": {
            "A": "As a stochastic process or logistic function dependent on macroeconomic covariates such as GDP growth, unemployment, and interest rates.",
            "B": "As a strictly deterministic decreasing function of time to maturity.",
            "C": "As an invariant constant across all issuers in the same rating tier."
        },
        "answer": "A",
        "explanation": "Advanced reduced-form models (such as Cox processes / doubly stochastic Poisson processes) specify the default intensity $\\lambda_t$ as a function of observable time-varying state variables and macroeconomic covariates. When macroeconomic indicators worsen (e.g., GDP contracting, high unemployment, credit spreads widening), default intensity $\\lambda_t$ increases dynamically across firms, capturing systemic credit cycles and default clustering.",
        "distractor_analysis": {
            "B": "Incorrect. Specifying $\\lambda_t$ as a deterministic decreasing function ignores empirical macroeconomic volatility and business cycles.",
            "C": "Incorrect. Assuming invariant constant intensity across issuers eliminates the key flexibility of reduced-form models to reflect firm-specific and macro changes."
        }
    },

    # -------------------------------------------------------------------------
    # VIGNETTE 11
    # -------------------------------------------------------------------------
    {
        "id": "L2-FI-V11-Q1",
        "level": 2,
        "topic": "Fixed Income",
        "subtopic": "Term Structure of Credit Spreads",
        "vignette_id": "V11",
        "vignette_title": "Credit Spread Curves, Business Cycle Dynamics, and Migration Risk",
        "vignette_text": "Senior portfolio manager Beatrice Morales is managing a USD 1.2 billion investment-grade credit mandate. She analyzes the term structure of credit spreads for high-yield vs investment-grade issuers across economic cycles. Beatrice notices that AA-rated corporate curves display an upward-sloping credit spread curve, while CCC-rated distressed curves are steeply inverted. Furthermore, she reviews credit migration transition matrices to evaluate downgrade risk and spread widening for a BBB-rated bond with a spread duration of 6.5 years and convexity of 55.",
        "los": "Describe the term structure of credit spreads and explain why credit spread curves can be upward sloping, flat, or inverted.",
        "question": "Which of the following factors best explains why high-quality investment-grade issuers exhibit upward-sloping credit spread curves while distressed issuers exhibit inverted credit spread curves?",
        "options": {
            "A": "High-quality issuers have negligible short-term default risk that can only increase over time, whereas distressed issuers face severe immediate default risk that diminishes if they survive the near term.",
            "B": "Distressed issuers have higher long-term recovery rates than high-quality issuers.",
            "C": "High-quality issuers face greater liquidity risk at short maturities than distressed issuers."
        },
        "answer": "A",
        "explanation": "For high-quality investment-grade issuers (e.g., AA), near-term default probability is virtually zero, but uncertainty regarding business viability and credit quality increases over longer horizons (ratings migration is predominantly downward). Hence, their credit spread curve is upward sloping.\nFor distressed high-yield issuers (e.g., CCC), the firm faces immediate refinancing or liquidity crises, causing high short-term default intensity and elevated short-dated credit spreads. If the firm survives the near-term crisis, its financial health usually improves or its debt is restructured, meaning conditional default hazard rates decline at longer horizons, resulting in an inverted credit spread curve.",
        "distractor_analysis": {
            "B": "Incorrect. Distressed issuers do not have higher recovery rates than investment-grade issuers; recovery rates depend on collateral and seniority.",
            "C": "Incorrect. Distressed issuers face far greater liquidity risk across all maturities, especially in the short term."
        }
    },
    {
        "id": "L2-FI-V11-Q2",
        "level": 2,
        "topic": "Fixed Income",
        "subtopic": "Term Structure of Credit Spreads",
        "vignette_id": "V11",
        "vignette_title": "Credit Spread Curves, Business Cycle Dynamics, and Migration Risk",
        "vignette_text": "Senior portfolio manager Beatrice Morales is managing a USD 1.2 billion investment-grade credit mandate. She analyzes the term structure of credit spreads for high-yield vs investment-grade issuers across economic cycles. Beatrice notices that AA-rated corporate curves display an upward-sloping credit spread curve, while CCC-rated distressed curves are steeply inverted. Furthermore, she reviews credit migration transition matrices to evaluate downgrade risk and spread widening for a BBB-rated bond with a spread duration of 6.5 years and convexity of 55.",
        "los": "Calculate the price impact of a change in credit spread using spread duration and convexity.",
        "question": "If the credit spread on Beatrice's BBB-rated bond widens by 75 bps (+0.0075), the estimated percentage price change of the bond is closest to:",
        "options": {
            "A": "-4.72%",
            "B": "-4.86%",
            "C": "-5.18%"
        },
        "answer": "A",
        "explanation": "The percentage price change resulting from a change in credit spread ($\\Delta s$) is calculated using spread duration ($SD$) and spread convexity ($C$):\n$$\\% \\Delta P \\approx -(SD \\times \\Delta s) + \\frac{1}{2} C \\times (\\Delta s)^2$$\nGiven:\n- $SD = 6.5$\n- $C = 55$\n- $\\Delta s = +0.0075$ (+75 bps)\nCalculate duration effect:\n$$-(6.5 \\times 0.0075) = -0.04875 = -4.875\\%$$\nCalculate convexity adjustment:\n$$\\frac{1}{2} \\times 55 \\times (0.0075)^2 = 27.5 \\times 0.00005625 = +0.001547 = +0.155\\%$$\nNet percentage price change:\n$$\\% \\Delta P \\approx -4.875\\% + 0.155\\% = -4.720\\% \\approx -4.72\\%$$",
        "distractor_analysis": {
            "B": "Incorrect. -4.88% accounts only for the duration effect ($-6.5 \\times 0.0075 = -4.875\\%$), omitting the positive convexity adjustment.",
            "C": "Incorrect. -5.18% erroneously subtracts the convexity term rather than adding it."
        }
    },
    {
        "id": "L2-FI-V11-Q3",
        "level": 2,
        "topic": "Fixed Income",
        "subtopic": "Term Structure of Credit Spreads",
        "vignette_id": "V11",
        "vignette_title": "Credit Spread Curves, Business Cycle Dynamics, and Migration Risk",
        "vignette_text": "Senior portfolio manager Beatrice Morales is managing a USD 1.2 billion investment-grade credit mandate. She analyzes the term structure of credit spreads for high-yield vs investment-grade issuers across economic cycles. Beatrice notices that AA-rated corporate curves display an upward-sloping credit spread curve, while CCC-rated distressed curves are steeply inverted. Furthermore, she reviews credit migration transition matrices to evaluate downgrade risk and spread widening for a BBB-rated bond with a spread duration of 6.5 years and convexity of 55.",
        "los": "Describe how credit rating migration affects bond valuation and expected return.",
        "question": "In a credit rating transition matrix, BBB-rated bonds have an 82% probability of remaining BBB, a 5% probability of upgrade to A, a 10% probability of downgrade to BB (high yield), and a 3% probability of deeper distress/default over a 1-year horizon. This asymmetry illustrates that:",
        "options": {
            "A": "Credit rating migration risk is negatively skewed, because the price loss from a downgrade is substantially larger than the price gain from an upgrade.",
            "B": "Credit rating upgrades occur more frequently than downgrades across investment-grade bonds.",
            "C": "Spread duration decreases immediately before a rating downgrade occurs."
        },
        "answer": "A",
        "explanation": "Credit rating migration exhibits pronounced negative skewness for BBB-rated bonds (the lowest investment-grade tier). First, the probability of downgrade (10% + 3% = 13%) exceeds the probability of upgrade (5%). Second, the spread widening associated with losing investment-grade status (the 'fallen angel' penalty crossing into high yield) is much larger in magnitude than the spread narrowing from an upgrade to A. Hence, downgrade risk exerts an asymmetric downward drag on expected bond returns.",
        "distractor_analysis": {
            "B": "Incorrect. Transition matrices empirically show that downgrades are more common than upgrades for BBB bonds, especially during late-cycle phases.",
            "C": "Incorrect. Spread duration depends on bond cash flows and maturity; it does not mechanically shrink prior to a downgrade."
        }
    },
    {
        "id": "L2-FI-V11-Q4",
        "level": 2,
        "topic": "Fixed Income",
        "subtopic": "Term Structure of Credit Spreads",
        "vignette_id": "V11",
        "vignette_title": "Credit Spread Curves, Business Cycle Dynamics, and Migration Risk",
        "vignette_text": "Senior portfolio manager Beatrice Morales is managing a USD 1.2 billion investment-grade credit mandate. She analyzes the term structure of credit spreads for high-yield vs investment-grade issuers across economic cycles. Beatrice notices that AA-rated corporate curves display an upward-sloping credit spread curve, while CCC-rated distressed curves are steeply inverted. Furthermore, she reviews credit migration transition matrices to evaluate downgrade risk and spread widening for a BBB-rated bond with a spread duration of 6.5 years and convexity of 55.",
        "los": "Describe the behavior of credit spreads across the business cycle.",
        "question": "As an economy transitions from an economic expansion into an unexpected recession, credit spreads typically:",
        "options": {
            "A": "Narrow across all sectors, with high-yield spreads narrowing more than investment-grade spreads.",
            "B": "Widen across all sectors, with high-yield credit spreads widening by a greater magnitude than investment-grade spreads.",
            "C": "Remain constant, because sovereign yields fall to fully absorb corporate default risk."
        },
        "answer": "B",
        "explanation": "During recessions, corporate revenues fall, default probabilities rise, and risk aversion intensifies. Consequently, credit spreads widen across all rating categories. High-yield bonds, having higher operating leverage and lower credit buffers, experience far greater spread widening in absolute basis point terms than investment-grade bonds.",
        "distractor_analysis": {
            "A": "Incorrect. Credit spreads widen during recessions; they narrow during economic expansions.",
            "C": "Incorrect. Corporate spreads widen independently of benchmark yield declines; sovereign yields dropping while corporate yields remain sticky or rise leads to widening spreads."
        }
    },
    {
        "id": "L2-FI-V11-Q5",
        "level": 2,
        "topic": "Fixed Income",
        "subtopic": "Term Structure of Credit Spreads",
        "vignette_id": "V11",
        "vignette_title": "Credit Spread Curves, Business Cycle Dynamics, and Migration Risk",
        "vignette_text": "Senior portfolio manager Beatrice Morales is managing a USD 1.2 billion investment-grade credit mandate. She analyzes the term structure of credit spreads for high-yield vs investment-grade issuers across economic cycles. Beatrice notices that AA-rated corporate curves display an upward-sloping credit spread curve, while CCC-rated distressed curves are steeply inverted. Furthermore, she reviews credit migration transition matrices to evaluate downgrade risk and spread widening for a BBB-rated bond with a spread duration of 6.5 years and convexity of 55.",
        "los": "Decompose credit spreads into expected loss and risk premium components.",
        "question": "Empirical studies decomposing corporate bond credit spreads show that the total spread exceeds the expected loss from default ($PD \\times LGD$). The residual component of the credit spread is primarily attributed to:",
        "options": {
            "A": "A liquidity premium and compensation for bearing systematic default correlation risk.",
            "B": "Tax differentials between sovereign bonds and corporate issues only.",
            "C": "Errors in historical recovery rate estimations."
        },
        "answer": "A",
        "explanation": "Total credit spread can be decomposed into:\n$$\\text{Credit Spread} = \\text{Expected Loss} + \\text{Credit Risk Premium} + \\text{Liquidity Premium}$$\nThe credit risk premium compensates risk-averse investors for bearing systematic credit risk (the risk that defaults cluster during economic downturns when marginal utility of wealth is highest). The liquidity premium compensates investors for lower secondary market trading liquidity and higher bid-ask transaction costs in corporate bonds relative to benchmark sovereign bonds.",
        "distractor_analysis": {
            "B": "Incorrect. While tax differences can play a small role in municipal or specific local markets, the credit risk premium and liquidity premium are the primary components universally documented in financial literature.",
            "C": "Incorrect. Recovery estimation errors do not explain the persistent, large premium observed systematically across decades."
        }
    },

    # -------------------------------------------------------------------------
    # VIGNETTE 12
    # -------------------------------------------------------------------------
    {
        "id": "L2-FI-V12-Q1",
        "level": 2,
        "topic": "Fixed Income",
        "subtopic": "Credit Default Swaps Mechanics and Pricing",
        "vignette_id": "V12",
        "vignette_title": "CDS Contract Specifications, Upfront Premium, and Mark-to-Market Valuation",
        "vignette_text": "Hedge fund manager Arthur Pendelton is trading single-name Credit Default Swaps (CDS) referencing automotive manufacturer Apex Motors. The standard CDS contract has a 5-year tenor, standardized coupon of 100 bps (standard investment grade), and an assumed recovery rate of 40%. Apex Motors' credit quality has deteriorated, and its 5-year CDS par spread has widened to 280 bps. The CDS duration (present value of a basis point on the premium leg, $PV01$) is 4.35 years. Arthur is evaluating buying USD 10 million notional of 5-year CDS protection.",
        "los": "Calculate the upfront premium on a credit default swap.",
        "question": "The approximate upfront premium (as a percentage of notional and currency amount) payable by Arthur to purchase USD 10 million of CDS protection on Apex Motors is closest to:",
        "options": {
            "A": "7.83% (USD 783,000)",
            "B": "12.18% (USD 1,218,000)",
            "C": "18.00% (USD 1,800,000)"
        },
        "answer": "A",
        "explanation": "Standardized CDS contracts trade with fixed coupons (100 bps for investment-grade, 500 bps for high-yield) and an upfront premium to reconcile the fixed coupon with the market par credit spread:\n$$\\text{Upfront Premium (\\%)} \\approx (\\text{CDS Spread} - \\text{Fixed Coupon}) \\times \\text{CDS Duration}$$\nGiven:\n- $\\text{CDS Spread} = 280 \\text{ bps} = 2.80\\%$\n- $\\text{Fixed Coupon} = 100 \\text{ bps} = 1.00\\%$\n- $\\text{CDS Duration} = 4.35$\n$$\\text{Upfront Premium (\\%)} \\approx (2.80\\% - 1.00\\%) \\times 4.35 = 1.80\\% \\times 4.35 = 7.83\\%$$\nFor a notional of USD 10,000,000:\n$$\\text{Upfront Amount} = 7.83\\% \\times \\text{USD } 10,000,000 = \\text{USD } 783,000$$\nBecause the market CDS spread (280 bps) exceeds the fixed coupon (100 bps), the protection buyer must pay this upfront premium to the protection seller.",
        "distractor_analysis": {
            "B": "Incorrect. 12.18% is computed using the total spread without subtracting the fixed coupon ($2.80\\% \\times 4.35 = 12.18\\%$).",
            "C": "Incorrect. 18.00% is simply $(280 - 100) = 1.80\\%$ multiplied by 10 without multiplying by CDS duration 4.35."
        }
    },
    {
        "id": "L2-FI-V12-Q2",
        "level": 2,
        "topic": "Fixed Income",
        "subtopic": "Credit Default Swaps Mechanics and Pricing",
        "vignette_id": "V12",
        "vignette_title": "CDS Contract Specifications, Upfront Premium, and Mark-to-Market Valuation",
        "vignette_text": "Hedge fund manager Arthur Pendelton is trading single-name Credit Default Swaps (CDS) referencing automotive manufacturer Apex Motors. The standard CDS contract has a 5-year tenor, standardized coupon of 100 bps (standard investment grade), and an assumed recovery rate of 40%. Apex Motors' credit quality has deteriorated, and its 5-year CDS par spread has widened to 280 bps. The CDS duration (present value of a basis point on the premium leg, $PV01$) is 4.35 years. Arthur is evaluating buying USD 10 million notional of 5-year CDS protection.",
        "los": "Describe the settlement process following a credit event in a credit default swap.",
        "question": "If Apex Motors triggers a credit event and an ISDA credit auction establishes a final bond recovery price of 35%, what cash settlement payment does the protection buyer receive on a USD 10 million notional CDS contract?",
        "options": {
            "A": "USD 3,500,000",
            "B": "USD 6,000,000",
            "C": "USD 6,500,000"
        },
        "answer": "C",
        "explanation": "Under standard cash settlement following an ISDA auction:\n$$\\text{Payoff to Protection Buyer} = \\text{Notional} \\times (1 - \\text{Auction Recovery Rate})$$\nGiven notional = USD 10,000,000 and auction recovery rate = 35%:\n$$\\text{Payoff} = \\text{USD } 10,000,000 \\times (1 - 0.35) = \\text{USD } 10,000,000 \\times 0.65 = \\text{USD } 6,500,000$$\nThe protection seller pays USD 6,500,000 to the protection buyer.",
        "distractor_analysis": {
            "A": "Incorrect. USD 3,500,000 is the recovery value received by bondholders ($35\\% \\times 10,000,000$), not the CDS payoff ($1 - R$).",
            "B": "Incorrect. USD 6,000,000 assumes the standard theoretical recovery rate of 40% ($1 - 0.40 = 60\\%$), ignoring the auction-determined recovery of 35%."
        }
    },
    {
        "id": "L2-FI-V12-Q3",
        "level": 2,
        "topic": "Fixed Income",
        "subtopic": "Credit Default Swaps Mechanics and Pricing",
        "vignette_id": "V12",
        "vignette_title": "CDS Contract Specifications, Upfront Premium, and Mark-to-Market Valuation",
        "vignette_text": "Hedge fund manager Arthur Pendelton is trading single-name Credit Default Swaps (CDS) referencing automotive manufacturer Apex Motors. The standard CDS contract has a 5-year tenor, standardized coupon of 100 bps (standard investment grade), and an assumed recovery rate of 40%. Apex Motors' credit quality has deteriorated, and its 5-year CDS par spread has widened to 280 bps. The CDS duration (present value of a basis point on the premium leg, $PV01$) is 4.35 years. Arthur is evaluating buying USD 10 million notional of 5-year CDS protection.",
        "los": "Calculate the change in value of a credit default swap position after a change in credit spread.",
        "question": "After Arthur purchases the CDS protection at a spread of 280 bps, Apex Motors experiences severe operational difficulties and its 5-year CDS spread widens further to 360 bps. Assuming the CDS duration is now 4.10 years, the mark-to-market gain on Arthur's USD 10 million protection position is closest to:",
        "options": {
            "A": "USD 328,000",
            "B": "USD 800,000",
            "C": "USD 1,476,000"
        },
        "answer": "A",
        "explanation": "The change in the mark-to-market value of a CDS position for the protection buyer is given by:\n$$\\Delta \\text{CDS Value to Buyer} \\approx \\Delta \\text{Spread} \\times \\text{CDS Duration} \\times \\text{Notional}$$\nGiven:\n- $\\Delta \\text{Spread} = 360 \\text{ bps} - 280 \\text{ bps} = 80 \\text{ bps} = 0.0080$\n- $\\text{CDS Duration} = 4.10$\n- $\\text{Notional} = \\text{USD } 10,000,000$\nCalculate:\n$$\\Delta \\text{CDS Value} \\approx 0.0080 \\times 4.10 \\times \\text{USD } 10,000,000 = 0.0328 \\times \\text{USD } 10,000,000 = \\text{USD } 328,000$$\nBecause Arthur is long protection (buying protection), credit deterioration and spread widening produce a mark-to-market profit.",
        "distractor_analysis": {
            "B": "Incorrect. USD 800,000 ignores CDS duration and calculates $80 \\text{ bps} \\times 10,000,000 = 80,000 \\times 10 = 800,000$.",
            "C": "Incorrect. USD 1,476,000 uses the total spread of 360 bps ($3.60\\% \\times 4.10 \\times 10M = 1,476,000$) rather than the change in spread $\\Delta \\text{Spread}$."
        }
    },
    {
        "id": "L2-FI-V12-Q4",
        "level": 2,
        "topic": "Fixed Income",
        "subtopic": "Credit Default Swaps Mechanics and Pricing",
        "vignette_id": "V12",
        "vignette_title": "CDS Contract Specifications, Upfront Premium, and Mark-to-Market Valuation",
        "vignette_text": "Hedge fund manager Arthur Pendelton is trading single-name Credit Default Swaps (CDS) referencing automotive manufacturer Apex Motors. The standard CDS contract has a 5-year tenor, standardized coupon of 100 bps (standard investment grade), and an assumed recovery rate of 40%. Apex Motors' credit quality has deteriorated, and its 5-year CDS par spread has widened to 280 bps. The CDS duration (present value of a basis point on the premium leg, $PV01$) is 4.35 years. Arthur is evaluating buying USD 10 million notional of 5-year CDS protection.",
        "los": "Describe the standardized features of credit default swap contracts post-Big Bang protocol.",
        "question": "Under the standardized post-'Big Bang' CDS market conventions, which of the following fixed coupon rates are universally standardized for North American and European corporate CDS?",
        "options": {
            "A": "0% for all sovereigns and floating MRR for corporates.",
            "B": "100 bps for investment-grade entities and 500 bps for high-yield entities.",
            "C": "250 bps for all corporate issuers regardless of credit rating."
        },
        "answer": "B",
        "explanation": "To promote liquidity, fungibility, and centralized clearing, the 2009 ISDA CDS 'Big Bang' and 'Small Bang' protocols standardized fixed coupons:\n- 100 bps (1.00%) for Investment Grade (IG) reference entities.\n- 500 bps (5.00%) for High Yield (HY) reference entities.\nAny difference between the market par CDS spread and this fixed coupon is settled via an upfront cash premium paid at inception.",
        "distractor_analysis": {
            "A": "Incorrect. CDS fixed coupons are not floating MRR; they are standardized fixed coupons (100 bps or 500 bps).",
            "C": "Incorrect. 250 bps is not a standard CDS coupon tier."
        }
    },
    {
        "id": "L2-FI-V12-Q5",
        "level": 2,
        "topic": "Fixed Income",
        "subtopic": "Credit Default Swaps Mechanics and Pricing",
        "vignette_id": "V12",
        "vignette_title": "CDS Contract Specifications, Upfront Premium, and Mark-to-Market Valuation",
        "vignette_text": "Hedge fund manager Arthur Pendelton is trading single-name Credit Default Swaps (CDS) referencing automotive manufacturer Apex Motors. The standard CDS contract has a 5-year tenor, standardized coupon of 100 bps (standard investment grade), and an assumed recovery rate of 40%. Apex Motors' credit quality has deteriorated, and its 5-year CDS par spread has widened to 280 bps. The CDS duration (present value of a basis point on the premium leg, $PV01$) is 4.35 years. Arthur is evaluating buying USD 10 million notional of 5-year CDS protection.",
        "los": "Identify credit events defined under standard ISDA master agreements.",
        "question": "Which of the following events is recognized as a standard credit event under ISDA documentation for North American corporate CDS contracts?",
        "options": {
            "A": "Credit rating downgrade from BBB- to BB+.",
            "B": "Failure to pay a scheduled debt obligation after expiration of any grace period.",
            "C": "A decline in the issuer's common stock price exceeding 50% in a single trading session."
        },
        "answer": "B",
        "explanation": "Standard credit events defined under ISDA agreements include:\n1. Bankruptcy: The reference entity becomes insolvent or initiates bankruptcy proceedings.\n2. Failure to Pay: The entity fails to make scheduled interest or principal payments above a specified minimum threshold (e.g., USD 1 million) after the expiration of contractual grace periods.\n3. Restructuring: In European/corporate contracts (modified restructuring), a forced debt alteration (reduction of principal or coupon, maturity extension) that harms creditors.\nRating downgrades and stock price declines do NOT constitute credit events.",
        "distractor_analysis": {
            "A": "Incorrect. A rating downgrade is not a credit event under ISDA definitions.",
            "C": "Incorrect. Equity price crashes are not credit events."
        }
    }
]
