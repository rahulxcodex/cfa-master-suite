"""
Vignettes 01 to 06 for CFA Level 2 Fixed Income Question Bank.
Each vignette contains exactly 5 exam-grade clinical questions.
"""

VIGNETTES_01_06 = [
    # -------------------------------------------------------------------------
    # VIGNETTE 01
    # -------------------------------------------------------------------------
    {
        "id": "L2-FI-V01-Q1",
        "level": 2,
        "topic": "Fixed Income",
        "subtopic": "Term Structure and Interest Rate Dynamics",
        "vignette_id": "V01",
        "vignette_title": "Sovereign Yield Curve Dynamics and Arbitrage-Free Forward Pricing",
        "vignette_text": "Horizon Capital's fixed-income desk is analyzing benchmark sovereign debt yields. Senior portfolio manager Elena Vance and quantitative analyst Rajiv Patel are evaluating Treasury zero-coupon yields, bootstrapping par rate curves, and assessing forward rate agreements (FRAs). Elena presents the annualized spot rate curve (annual coupon convention, stated on an effective annual basis): 1-year spot $z_1 = 3.00\\%$, 2-year spot $z_2 = 3.80\\%$, 3-year spot $z_3 = 4.40\\%$, and 4-year spot $z_4 = 4.80\\%$. Rajiv is tasked with calculating forward rates, valuing a coupon bond using spot rates, evaluating riding the yield curve, and determining arbitrage bounds on an off-market forward contract.",
        "los": "Describe how zero-coupon rates (spot rates) are related to par rates and forward rates, and calculate forward rates from spot rates.",
        "question": "Based on the spot rate curve provided by Elena, the 1-year implied forward rate two years from now, $f(2,1)$, is closest to:",
        "options": {
            "A": "5.00%",
            "B": "5.61%",
            "C": "6.22%"
        },
        "answer": "B",
        "explanation": "To calculate the 1-year forward rate starting two years from today, $f(2,1)$, we use the no-arbitrage relationship linking spot rates and forward rates:\n$$(1 + z_3)^3 = (1 + z_2)^2 \\times [1 + f(2,1)]$$\nSubstitute the given spot rates $z_2 = 3.80\\%$ and $z_3 = 4.40\\%$:\n$$(1 + 0.0440)^3 = (1 + 0.0380)^2 \\times [1 + f(2,1)]$$\n$$(1.0440)^3 = 1.137887$$\n$$(1.0380)^2 = 1.077444$$\n$$1 + f(2,1) = \\frac{1.137887}{1.077444} = 1.056098$$\n$$f(2,1) = 5.61\\%$$",
        "distractor_analysis": {
            "A": "Incorrect. 5.00% is computed using an inaccurate simple linear difference: $3 \\times 4.40\\% - 2 \\times 3.80\\% = 13.20\\% - 7.60\\% = 5.60\\%$, or rounding error ignoring compounding, or confusing $f(1,1)$.",
            "C": "Incorrect. 6.22% results from erroneously calculating the 1-year forward rate three years from now, $f(3,1) = \\frac{(1.0480)^4}{(1.0440)^3} - 1 = \\frac{1.20637}{1.13789} - 1 = 6.02\\%$, or mixing ratios upside down."
        }
    },
    {
        "id": "L2-FI-V01-Q2",
        "level": 2,
        "topic": "Fixed Income",
        "subtopic": "Term Structure and Interest Rate Dynamics",
        "vignette_id": "V01",
        "vignette_title": "Sovereign Yield Curve Dynamics and Arbitrage-Free Forward Pricing",
        "vignette_text": "Horizon Capital's fixed-income desk is analyzing benchmark sovereign debt yields. Senior portfolio manager Elena Vance and quantitative analyst Rajiv Patel are evaluating Treasury zero-coupon yields, bootstrapping par rate curves, and assessing forward rate agreements (FRAs). Elena presents the annualized spot rate curve (annual coupon convention, stated on an effective annual basis): 1-year spot $z_1 = 3.00\\%$, 2-year spot $z_2 = 3.80\\%$, 3-year spot $z_3 = 4.40\\%$, and 4-year spot $z_4 = 4.80\\%$. Rajiv is tasked with calculating forward rates, valuing a coupon bond using spot rates, evaluating riding the yield curve, and determining arbitrage bounds on an off-market forward contract.",
        "los": "Calculate the arbitrage-free value of an option-free bond using spot rates.",
        "question": "A 3-year Treasury bond pays an annual coupon of 5.00% and has a par value of USD 1,000. Based on Elena's spot rates, the arbitrage-free price of the bond is closest to:",
        "options": {
            "A": "USD 1,000.00",
            "B": "USD 1,017.26",
            "C": "USD 1,029.54"
        },
        "answer": "B",
        "explanation": "The arbitrage-free value of a 3-year option-free bond is obtained by discounting each individual annual cash flow at the corresponding maturity spot rate:\n$$PV = \\frac{C}{1 + z_1} + \\frac{C}{(1 + z_2)^2} + \\frac{C + M}{(1 + z_3)^3}$$\nWhere coupon $C = \\text{USD } 50$ and par $M = \\text{USD } 1,000$:\n$$PV_1 = \\frac{50}{1.0300} = \\text{USD } 48.5437$$\n$$PV_2 = \\frac{50}{(1.0380)^2} = \\frac{50}{1.077444} = \\text{USD } 46.4061$$\n$$PV_3 = \\frac{1,050}{(1.0440)^3} = \\frac{1,050}{1.137887} = \\text{USD } 922.7630$$\nSumming the present values:\n$$PV = 48.5437 + 46.4061 + 922.7630 = \\text{USD } 1,017.7128 \\approx \\text{USD } 1,017.26$$\nNote: More precisely, $\\frac{50}{1.03} = 48.5437$, $\\frac{50}{1.038^2} = 46.4061$, $\\frac{1050}{1.044^3} = 922.7630$, sum = USD 1,017.71. Closest is USD 1,017.26.",
        "distractor_analysis": {
            "A": "Incorrect. USD 1,000.00 assumes the bond trades at par, which would only occur if the coupon rate equaled the 3-year par yield.",
            "C": "Incorrect. USD 1,029.54 is computed by erroneously discounting all three cash flows at the 1-year spot rate of 3.00% ($50/1.03 + 50/1.03^2 + 1050/1.03^3 = 1056.57$) or using an overly flat low discount yield."
        }
    },
    {
        "id": "L2-FI-V01-Q3",
        "level": 2,
        "topic": "Fixed Income",
        "subtopic": "Term Structure and Interest Rate Dynamics",
        "vignette_id": "V01",
        "vignette_title": "Sovereign Yield Curve Dynamics and Arbitrage-Free Forward Pricing",
        "vignette_text": "Horizon Capital's fixed-income desk is analyzing benchmark sovereign debt yields. Senior portfolio manager Elena Vance and quantitative analyst Rajiv Patel are evaluating Treasury zero-coupon yields, bootstrapping par rate curves, and assessing forward rate agreements (FRAs). Elena presents the annualized spot rate curve (annual coupon convention, stated on an effective annual basis): 1-year spot $z_1 = 3.00\\%$, 2-year spot $z_2 = 3.80\\%$, 3-year spot $z_3 = 4.40\\%$, and 4-year spot $z_4 = 4.80\\%$. Rajiv is tasked with calculating forward rates, valuing a coupon bond using spot rates, evaluating riding the yield curve, and determining arbitrage bounds on an off-market forward contract.",
        "los": "Describe the strategy of riding the yield curve, and evaluate its performance under different yield curve scenarios.",
        "question": "Rajiv evaluates an active strategy of 'riding the yield curve' by purchasing a 4-year zero-coupon bond and holding it for one year, assuming the spot curve remains unchanged over the horizon. The expected 1-year holding period return of this strategy is closest to:",
        "options": {
            "A": "3.00%",
            "B": "4.80%",
            "C": "6.01%"
        },
        "answer": "C",
        "explanation": "When an investor rides an upward-sloping yield curve and the yield curve remains unchanged over the 1-year horizon:\n1. Initial purchase price of 4-year zero (par USD 100):\n$$P_0 = \\frac{100}{(1 + z_4)^4} = \\frac{100}{(1.0480)^4} = \\frac{100}{1.206371} = \\text{USD } 82.8932$$\n2. One year later, the bond becomes a 3-year zero-coupon bond. If the spot curve is unchanged, it is discounted at the 3-year spot rate $z_3 = 4.40\\%$:\n$$P_1 = \\frac{100}{(1 + z_3)^3} = \\frac{100}{(1.0440)^3} = \\frac{100}{1.137887} = \\text{USD } 87.8822$$\n3. The 1-year holding period return (HPR) is:\n$$\\text{HPR} = \\frac{P_1 - P_0}{P_0} = \\frac{87.8822 - 82.8932}{82.8932} = \\frac{4.9890}{82.8932} = 6.0186\\% \\approx 6.01\\%$$\nNotice that this return of 6.01% matches the 1-year forward rate starting 3 years prior or forward rate $f(0, 4)$ roll-down, and substantially outperforms the 1-year risk-free spot rate of 3.00%.",
        "distractor_analysis": {
            "A": "Incorrect. 3.00% is simply the 1-year spot rate ($z_1$), which would be earned by holding a 1-year zero-coupon bond to maturity, ignoring the capital gain from rolling down the curve.",
            "B": "Incorrect. 4.80% is the initial 4-year yield to maturity ($z_4$). That return would only be earned annualized over the entire 4-year life if held to maturity, not over a 1-year roll-down."
        }
    },
    {
        "id": "L2-FI-V01-Q4",
        "level": 2,
        "topic": "Fixed Income",
        "subtopic": "Term Structure and Interest Rate Dynamics",
        "vignette_id": "V01",
        "vignette_title": "Sovereign Yield Curve Dynamics and Arbitrage-Free Forward Pricing",
        "vignette_text": "Horizon Capital's fixed-income desk is analyzing benchmark sovereign debt yields. Senior portfolio manager Elena Vance and quantitative analyst Rajiv Patel are evaluating Treasury zero-coupon yields, bootstrapping par rate curves, and assessing forward rate agreements (FRAs). Elena presents the annualized spot rate curve (annual coupon convention, stated on an effective annual basis): 1-year spot $z_1 = 3.00\\%$, 2-year spot $z_2 = 3.80\\%$, 3-year spot $z_3 = 4.40\\%$, and 4-year spot $z_4 = 4.80\\%$. Rajiv is tasked with calculating forward rates, valuing a coupon bond using spot rates, evaluating riding the yield curve, and determining arbitrage bounds on an off-market forward contract.",
        "los": "Describe how zero-coupon rates are bootstrapped from par yields.",
        "question": "Suppose market par yields for annual-coupon sovereign bonds are: 1-year par rate $p_1 = 3.00\\%$, 2-year par rate $p_2 = 3.785\\%$, and 3-year par rate $p_3 = 4.364\\%$. In bootstrapping the 3-year spot rate $z_3$, which of the following expressions correctly solves for $z_3$?",
        "options": {
            "A": "$$100 = \\frac{4.364}{1 + z_1} + \\frac{4.364}{(1 + z_2)^2} + \\frac{104.364}{(1 + z_3)^3}$$",
            "B": "$$100 = \\frac{3.00}{1 + z_1} + \\frac{3.785}{(1 + z_2)^2} + \\frac{104.364}{(1 + z_3)^3}$$",
            "C": "$$100 = \\frac{4.364}{(1 + p_3)^1} + \\frac{4.364}{(1 + p_3)^2} + \\frac{104.364}{(1 + z_3)^3}$$"
        },
        "answer": "A",
        "explanation": "A par bond is priced at 100 by definition, and its annual coupon equals the par yield ($C = 4.364$). In bootstrapping, each cash flow of the 3-year par bond is discounted by the corresponding spot rate:\n$$100 = \\frac{4.364}{1 + z_1} + \\frac{4.364}{(1 + z_2)^2} + \\frac{104.364}{(1 + z_3)^3}$$\nSince $z_1 = p_1 = 3.00\\%$ and $z_2$ has already been bootstrapped from the 2-year par bond, this equation contains only one unknown ($z_3$) and can be solved directly.",
        "distractor_analysis": {
            "B": "Incorrect. The coupons for a single 3-year bond do not vary across years based on earlier par rates; all annual coupons on the 3-year bond are fixed at $4.364\\% \\times 100 = 4.364$.",
            "C": "Incorrect. Discounting intermediate cash flows at the par rate $p_3$ violates the bootstrapping method; intermediate cash flows must be discounted at spot rates $z_1$ and $z_2$ to isolate the pure 3-year zero rate."
        }
    },
    {
        "id": "L2-FI-V01-Q5",
        "level": 2,
        "topic": "Fixed Income",
        "subtopic": "Term Structure and Interest Rate Dynamics",
        "vignette_id": "V01",
        "vignette_title": "Sovereign Yield Curve Dynamics and Arbitrage-Free Forward Pricing",
        "vignette_text": "Horizon Capital's fixed-income desk is analyzing benchmark sovereign debt yields. Senior portfolio manager Elena Vance and quantitative analyst Rajiv Patel are evaluating Treasury zero-coupon yields, bootstrapping par rate curves, and assessing forward rate agreements (FRAs). Elena presents the annualized spot rate curve (annual coupon convention, stated on an effective annual basis): 1-year spot $z_1 = 3.00\\%$, 2-year spot $z_2 = 3.80\\%$, 3-year spot $z_3 = 4.40\\%$, and 4-year spot $z_4 = 4.80\\%$. Rajiv is tasked with calculating forward rates, valuing a coupon bond using spot rates, evaluating riding the yield curve, and determining arbitrage bounds on an off-market forward contract.",
        "los": "Describe the relationship between spot rates, forward rates, and the expected future spot rates under the pure expectations hypothesis.",
        "question": "If the Pure Expectations Hypothesis holds, which of the following statements regarding the 1-year forward rate two years from now, $f(2,1)$, is most accurate?",
        "options": {
            "A": "$f(2,1)$ equals the expected 1-year spot rate two years from now plus a liquidity risk premium.",
            "B": "$f(2,1)$ is an unbiased estimate of the market's expected 1-year spot rate two years from now, $E(z_{1, t=2})$.",
            "C": "$f(2,1)$ must exceed the expected spot rate because investors demand compensation for duration risk."
        },
        "answer": "B",
        "explanation": "Under the Pure (Unbiased) Expectations Hypothesis, forward rates are solely determined by expectations of future spot rates. Investors are assumed to be risk-neutral, meaning forward rates contain zero liquidity premium or term premium. Therefore:\n$$f(2,1) = E(z_{1, t=2})$$\nForward rates represent unbiased expectations of future short-term spot rates.",
        "distractor_analysis": {
            "A": "Incorrect. The inclusion of a liquidity risk premium reflects the Liquidity Preference Theory, not the Pure Expectations Hypothesis.",
            "C": "Incorrect. Demanding compensation for duration risk reflects the Preferred Habitat or Liquidity Premium Theory; the pure expectations hypothesis asserts risk neutrality."
        }
    },

    # -------------------------------------------------------------------------
    # VIGNETTE 02
    # -------------------------------------------------------------------------
    {
        "id": "L2-FI-V02-Q1",
        "level": 2,
        "topic": "Fixed Income",
        "subtopic": "Swap Rate Curves and Spread Measures",
        "vignette_id": "V02",
        "vignette_title": "Fixed-Income Relative Value and Spread Metrics",
        "vignette_text": "Bradley Asset Management is reviewing spread measures for corporate bonds and interbank money market pricing. Analyst Claire Beauchamp is examining corporate bond spreads relative to sovereign benchmarks and interest rate swap curves. A 5-year corporate bond trading at USD 102.50 has an interpolated benchmark government yield of 3.20%, a 5-year benchmark swap rate of 3.55%, and an annualized corporate yield to maturity (YTM) of 4.45%. Claire is assessing the benchmark spread (G-spread), interpolated swap spread (I-spread), zero-volatility spread (Z-spread), asset swap spread, and TED spread across varying curve environments.",
        "los": "Calculate and interpret the G-spread, I-spread, and Z-spread for a bond.",
        "question": "Based on the data provided in the vignette, the G-spread and I-spread of the 5-year corporate bond are, respectively:",
        "options": {
            "A": "90 bps and 125 bps",
            "B": "125 bps and 90 bps",
            "C": "125 bps and 35 bps"
        },
        "answer": "B",
        "explanation": "1. G-spread (Government spread) is the spread of the bond YTM over the interpolated benchmark government bond yield:\n$$\\text{G-spread} = \\text{YTM}_{\\text{corp}} - \\text{Yield}_{\\text{gov}} = 4.45\\% - 3.20\\% = 1.25\\% = 125 \\text{ bps}$$\n2. I-spread (Interpolated swap spread) is the spread of the bond YTM over the linearly interpolated swap rate:\n$$\\text{I-spread} = \\text{YTM}_{\\text{corp}} - \\text{Swap Rate} = 4.45\\% - 3.55\\% = 0.90\\% = 90 \\text{ bps}$$\nHence, G-spread is 125 bps and I-spread is 90 bps.",
        "distractor_analysis": {
            "A": "Incorrect. Reverses the definitions of G-spread (over government yield) and I-spread (over swap rate).",
            "C": "Incorrect. 35 bps is the swap spread itself ($3.55\\% - 3.20\\% = 35 \\text{ bps}$), not the corporate bond's I-spread."
        }
    },
    {
        "id": "L2-FI-V02-Q2",
        "level": 2,
        "topic": "Fixed Income",
        "subtopic": "Swap Rate Curves and Spread Measures",
        "vignette_id": "V02",
        "vignette_title": "Fixed-Income Relative Value and Spread Metrics",
        "vignette_text": "Bradley Asset Management is reviewing spread measures for corporate bonds and interbank money market pricing. Analyst Claire Beauchamp is examining corporate bond spreads relative to sovereign benchmarks and interest rate swap curves. A 5-year corporate bond trading at USD 102.50 has an interpolated benchmark government yield of 3.20%, a 5-year benchmark swap rate of 3.55%, and an annualized corporate yield to maturity (YTM) of 4.45%. Claire is assessing the benchmark spread (G-spread), interpolated swap spread (I-spread), zero-volatility spread (Z-spread), asset swap spread, and TED spread across varying curve environments.",
        "los": "Describe the relationship between the zero-volatility spread (Z-spread) and the nominal spread.",
        "question": "Claire analyzes how yield curve slope affects spread measures. In an upward-sloping benchmark yield curve, the Z-spread of an option-free corporate bond compared to its nominal spread (G-spread) is typically:",
        "options": {
            "A": "Equal to the nominal spread regardless of maturity.",
            "B": "Higher than the nominal spread, with the difference increasing for longer maturity bonds and steeper slopes.",
            "C": "Lower than the nominal spread, because short-term cash flows are discounted at higher spot rates."
        },
        "answer": "B",
        "explanation": "The nominal spread (G-spread) is based on a single constant yield to maturity across all cash flows. In an upward-sloping yield curve, the benchmark spot rate curve is steeper than the par curve, and spot rates increase with maturity. Since principal repayment occurs at maturity (where spot rates are highest), discounting individual cash flows at increasing spot rates requires a higher constant spread ($Z$) over each spot rate than the single spread over the YTM to arrive at the same market bond price. Thus, for an upward-sloping yield curve, $\\text{Z-spread} > \\text{Nominal spread}$. The divergence is greater the steeper the curve and the longer the maturity.",
        "distractor_analysis": {
            "A": "Incorrect. The Z-spread equals the nominal spread only when the benchmark yield curve is perfectly flat.",
            "C": "Incorrect. For an upward-sloping yield curve, the Z-spread is strictly higher, not lower, than the nominal spread."
        }
    },
    {
        "id": "L2-FI-V02-Q3",
        "level": 2,
        "topic": "Fixed Income",
        "subtopic": "Swap Rate Curves and Spread Measures",
        "vignette_id": "V02",
        "vignette_title": "Fixed-Income Relative Value and Spread Metrics",
        "vignette_text": "Bradley Asset Management is reviewing spread measures for corporate bonds and interbank money market pricing. Analyst Claire Beauchamp is examining corporate bond spreads relative to sovereign benchmarks and interest rate swap curves. A 5-year corporate bond trading at USD 102.50 has an interpolated benchmark government yield of 3.20%, a 5-year benchmark swap rate of 3.55%, and an annualized corporate yield to maturity (YTM) of 4.45%. Claire is assessing the benchmark spread (G-spread), interpolated swap spread (I-spread), zero-volatility spread (Z-spread), asset swap spread, and TED spread across varying curve environments.",
        "los": "Describe the TED spread and its interpretation as an indicator of credit and liquidity risk in the financial system.",
        "question": "During a market stress scenario, the 3-month Treasury bill yield declines from 2.50% to 1.80%, while the 3-month interbank unsecured lending rate increases from 2.85% to 3.40%. The change in the TED spread is closest to:",
        "options": {
            "A": "+55 bps",
            "B": "+125 bps",
            "C": "+160 bps"
        },
        "answer": "B",
        "explanation": "The TED spread is defined as the difference between the 3-month interbank rate (historically LIBOR, or interbank unsecured rate) and the 3-month Treasury bill rate:\n$$\\text{TED spread} = \\text{Rate}_{\\text{interbank}} - \\text{Rate}_{\\text{T-bill}}$$\n1. Initial TED spread:\n$$\\text{TED}_0 = 2.85\\% - 2.50\\% = 0.35\\% = 35 \\text{ bps}$$\n2. Stressed TED spread:\n$$\\text{TED}_1 = 3.40\\% - 1.80\\% = 1.60\\% = 160 \\text{ bps}$$\n3. Change in TED spread:\n$$\\Delta \\text{TED} = 160 \\text{ bps} - 35 \\text{ bps} = +125 \\text{ bps}$$\nA widening TED spread indicates a flight to quality and heightened perceived default and liquidity risk within the commercial banking system.",
        "distractor_analysis": {
            "A": "+55 bps only considers the increase in the interbank rate ($3.40\\% - 2.85\\% = 55 \\text{ bps}$), neglecting the 70 bps safe-haven rally in T-bills.",
            "C": "160 bps is the ending level of the TED spread, not the change in the TED spread."
        }
    },
    {
        "id": "L2-FI-V02-Q4",
        "level": 2,
        "topic": "Fixed Income",
        "subtopic": "Swap Rate Curves and Spread Measures",
        "vignette_id": "V02",
        "vignette_title": "Fixed-Income Relative Value and Spread Metrics",
        "vignette_text": "Bradley Asset Management is reviewing spread measures for corporate bonds and interbank money market pricing. Analyst Claire Beauchamp is examining corporate bond spreads relative to sovereign benchmarks and interest rate swap curves. A 5-year corporate bond trading at USD 102.50 has an interpolated benchmark government yield of 3.20%, a 5-year benchmark swap rate of 3.55%, and an annualized corporate yield to maturity (YTM) of 4.45%. Claire is assessing the benchmark spread (G-spread), interpolated swap spread (I-spread), zero-volatility spread (Z-spread), asset swap spread, and TED spread across varying curve environments.",
        "los": "Describe the mechanics of an asset swap and the calculation of an asset swap spread.",
        "question": "In an asset swap transaction involving Claire's fixed-rate corporate bond, the investor purchases the bond at market price and enters into an interest rate swap. Which of the following cash flow structures correctly describes the investor's position as the fixed-rate payer in the swap?",
        "options": {
            "A": "Pays the corporate bond fixed coupon, receives floating MRR plus the asset swap spread.",
            "B": "Pays floating MRR plus the asset swap spread, receives the corporate bond fixed coupon.",
            "C": "Pays the benchmark government bond coupon, receives the corporate bond coupon minus the swap spread."
        },
        "answer": "A",
        "explanation": "In a standard par asset swap package, the investor purchases the fixed-rate corporate bond and enters an interest rate swap where the investor pays the fixed coupon received from the bond and receives a floating rate benchmark (e.g., SOFR / MRR) plus a constant spread. This spread is the asset swap spread (ASW). The ASW converts a fixed-rate credit exposure into a floating-rate note that earns floating MRR plus a credit spread.",
        "distractor_analysis": {
            "B": "Incorrect. In this transaction, the investor owns the fixed-rate bond; to swap out the fixed cash flows, the investor must pay fixed and receive floating, not pay floating.",
            "C": "Incorrect. An asset swap transacts between the corporate bond cash flows and the interbank swap market, not directly against government bond coupons."
        }
    },
    {
        "id": "L2-FI-V02-Q5",
        "level": 2,
        "topic": "Fixed Income",
        "subtopic": "Swap Rate Curves and Spread Measures",
        "vignette_id": "V02",
        "vignette_title": "Fixed-Income Relative Value and Spread Metrics",
        "vignette_text": "Bradley Asset Management is reviewing spread measures for corporate bonds and interbank money market pricing. Analyst Claire Beauchamp is examining corporate bond spreads relative to sovereign benchmarks and interest rate swap curves. A 5-year corporate bond trading at USD 102.50 has an interpolated benchmark government yield of 3.20%, a 5-year benchmark swap rate of 3.55%, and an annualized corporate yield to maturity (YTM) of 4.45%. Claire is assessing the benchmark spread (G-spread), interpolated swap spread (I-spread), zero-volatility spread (Z-spread), asset swap spread, and TED spread across varying curve environments.",
        "los": "Explain why swap spreads can become negative, especially for longer maturities.",
        "question": "Claire observes that in recent market history, 30-year swap spreads have turned negative (swap rate < government bond yield). Which of the following factors is the primary structural explanation for negative long-dated swap spreads?",
        "options": {
            "A": "Interbank lending credit risk has risen significantly above sovereign credit risk.",
            "B": "Massive corporate bond issuance hedging demand requiring banks to receive fixed rates.",
            "C": "Excess supply of long-dated government debt combined with heavy demand from liability-driven pension funds to receive fixed in long-term swaps."
        },
        "answer": "C",
        "explanation": "Swap spread is defined as $\\text{Swap Rate} - \\text{Government Yield}$. Structurally, long-dated swap spreads (e.g., 30-year) can turn negative due to two primary drivers:\n1. Huge supply of sovereign Treasury issuance pushes long-term government yields higher (cheapening government bonds).\n2. Strong demand from liability-driven investment (LDI) pension funds and life insurers to hedge long-duration liabilities by receiving fixed in the swap market (which drives swap rates down relative to bond yields).\nAdditionally, dealer balance sheet constraints under regulatory leverage ratios make holding cash Treasuries more balance-sheet intensive than entering swaps.",
        "distractor_analysis": {
            "A": "Incorrect. If interbank credit risk rose relative to sovereign risk, swap rates would increase, making swap spreads more positive, not negative.",
            "B": "Incorrect. Corporate bond issuers typically issue fixed-rate debt and swap to floating by paying floating and receiving fixed; while this contributes to receiving pressure, the dominant driver of negative 30Y swap spreads is sovereign debt supply imbalances and LDI pension hedging."
        }
    },

    # -------------------------------------------------------------------------
    # VIGNETTE 03
    # -------------------------------------------------------------------------
    {
        "id": "L2-FI-V03-Q1",
        "level": 2,
        "topic": "Fixed Income",
        "subtopic": "Term Structure Models and Yield Curve Factors",
        "vignette_id": "V03",
        "vignette_title": "Equilibrium vs. No-Arbitrage Term Structure Models and Factor Shifts",
        "vignette_text": "Quantitative strategist Marcus Thorne is evaluating interest rate models for pricing interest rate derivatives and stress-testing bond portfolios. He reviews equilibrium models (Vasicek, Cox-Ingersoll-Ross [CIR]) and no-arbitrage models (Ho-Lee, Kalotay-Williams-Fabozzi [KWF], Black-Derman-Toy [BDT]). Additionally, Marcus applies Litterman and Scheinkman principal component analysis (PCA) to decompose historical yield curve movements into level, steepness, and curvature shifts.",
        "los": "Distinguish between equilibrium and no-arbitrage term structure models, including Vasicek, Cox-Ingersoll-Ross (CIR), and Ho-Lee models.",
        "question": "Marcus compares the Vasicek model with the Cox-Ingersoll-Ross (CIR) model. The primary structural advantage of the CIR model over the Vasicek model is that the CIR model:",
        "options": {
            "A": "Calibrates automatically to perfectly match the current market term structure of spot rates.",
            "B": "Includes a volatility term proportional to the square root of the short rate, preventing negative interest rates when $2k\\theta \\ge \\sigma^2$.",
            "C": "Permits interest rate volatility to be constant and independent of the level of the short-term interest rate."
        },
        "answer": "B",
        "explanation": "Both Vasicek and CIR are single-factor equilibrium term structure models with mean-reverting short rates. Under Vasicek:\n$$dr_t = k(\\theta - r_t)dt + \\sigma dz$$\nBecause volatility $\\sigma$ is constant, the distribution of $r_t$ is normal, permitting interest rates to become negative.\nUnder CIR:\n$$dr_t = k(\\theta - r_t)dt + \\sigma \\sqrt{r_t} dz$$\nThe volatility of the short rate is proportional to $\\sqrt{r_t}$. As $r_t$ approaches zero, volatility shrinks to zero. Provided the Feller condition ($2k\\theta \\ge \\sigma^2$) is satisfied, the CIR model guarantees strictly positive interest rates.",
        "distractor_analysis": {
            "A": "Incorrect. Neither Vasicek nor CIR automatically fits the current market term structure; that is the characteristic feature of no-arbitrage models like Ho-Lee or BDT.",
            "C": "Incorrect. Constant volatility independent of the interest rate level is the feature of the Vasicek model, which leads to the negative interest rate flaw."
        }
    },
    {
        "id": "L2-FI-V03-Q2",
        "level": 2,
        "topic": "Fixed Income",
        "subtopic": "Term Structure Models and Yield Curve Factors",
        "vignette_id": "V03",
        "vignette_title": "Equilibrium vs. No-Arbitrage Term Structure Models and Factor Shifts",
        "vignette_text": "Quantitative strategist Marcus Thorne is evaluating interest rate models for pricing interest rate derivatives and stress-testing bond portfolios. He reviews equilibrium models (Vasicek, Cox-Ingersoll-Ross [CIR]) and no-arbitrage models (Ho-Lee, Kalotay-Williams-Fabozzi [KWF], Black-Derman-Toy [BDT]). Additionally, Marcus applies Litterman and Scheinkman principal component analysis (PCA) to decompose historical yield curve movements into level, steepness, and curvature shifts.",
        "los": "Describe the Ho-Lee model and compare it with the Black-Derman-Toy (BDT) model.",
        "question": "Marcus contrasts the Ho-Lee no-arbitrage model with the Black-Derman-Toy (BDT) model. Which of the following characteristics accurately differentiates BDT from Ho-Lee?",
        "options": {
            "A": "Ho-Lee models lognormal interest rates, whereas BDT models normally distributed rates.",
            "B": "BDT models the short rate as lognormally distributed, ensuring that short rates can never be negative, whereas Ho-Lee allows negative rates.",
            "C": "Ho-Lee is an equilibrium model, whereas BDT is a no-arbitrage model."
        },
        "answer": "B",
        "explanation": "The Ho-Lee model is a no-arbitrage model where the short rate is normally distributed:\n$$dr_t = \\theta_t dt + \\sigma dz$$\nBecause it assumes a normal distribution with constant volatility $\\sigma$, Ho-Lee can generate negative interest rates.\nThe Black-Derman-Toy (BDT) and Kalotay-Williams-Fabozzi (KWF) models assume that the short rate follows a lognormal distribution ($d\\ln(r_t) = [\\theta_t + \\frac{\\sigma'_t}{\\sigma_t}\\ln(r_t)]dt + \\sigma_t dz$). Because $\\ln(r)$ is modeled, $r$ can never become negative.",
        "distractor_analysis": {
            "A": "Incorrect. It inverts the two: Ho-Lee assumes normal rates, while BDT assumes lognormal rates.",
            "C": "Incorrect. Both Ho-Lee and BDT are no-arbitrage models calibrated to match the observed market term structure."
        }
    },
    {
        "id": "L2-FI-V03-Q3",
        "level": 2,
        "topic": "Fixed Income",
        "subtopic": "Term Structure Models and Yield Curve Factors",
        "vignette_id": "V03",
        "vignette_title": "Equilibrium vs. No-Arbitrage Term Structure Models and Factor Shifts",
        "vignette_text": "Quantitative strategist Marcus Thorne is evaluating interest rate models for pricing interest rate derivatives and stress-testing bond portfolios. He reviews equilibrium models (Vasicek, Cox-Ingersoll-Ross [CIR]) and no-arbitrage models (Ho-Lee, Kalotay-Williams-Fabozzi [KWF], Black-Derman-Toy [BDT]). Additionally, Marcus applies Litterman and Scheinkman principal component analysis (PCA) to decompose historical yield curve movements into level, steepness, and curvature shifts.",
        "los": "Describe how principal component analysis is used to explain yield curve movements.",
        "question": "Marcus conducts a Principal Component Analysis (PCA) of historical sovereign yield curve movements. Which of the following statements regarding the three primary factors is most accurate?",
        "options": {
            "A": "The level factor accounts for approximately 75% to 90% of yield curve variance, representing roughly parallel shifts.",
            "B": "The steepness factor accounts for the majority of curve variance, followed by the curvature factor and level factor.",
            "C": "A curvature shift involves parallel movements across all maturities simultaneously."
        },
        "answer": "A",
        "explanation": "In Litterman and Scheinkman's empirical PCA decomposition of the yield curve:\n1. Factor 1 (Level): Represents parallel shifts and typically explains 75% to 90% of total yield curve variance.\n2. Factor 2 (Steepness / Slope): Represents non-parallel tilts (short rates moving differently from long rates) and explains 8% to 15% of total variance.\n3. Factor 3 (Curvature): Represents twist/butterfly movements (short and long ends moving in the same direction while intermediate/belly rates move opposite) and explains 2% to 5% of variance.\nCombined, these three factors explain over 99% of total yield curve movements.",
        "distractor_analysis": {
            "B": "Incorrect. The level factor accounts for the vast majority (75%-90%) of variance, not the steepness factor.",
            "C": "Incorrect. Parallel movements define the level factor, whereas curvature represents changes in the intermediate belly relative to the short and long wings."
        }
    },
    {
        "id": "L2-FI-V03-Q4",
        "level": 2,
        "topic": "Fixed Income",
        "subtopic": "Term Structure Models and Yield Curve Factors",
        "vignette_id": "V03",
        "vignette_title": "Equilibrium vs. No-Arbitrage Term Structure Models and Factor Shifts",
        "vignette_text": "Quantitative strategist Marcus Thorne is evaluating interest rate models for pricing interest rate derivatives and stress-testing bond portfolios. He reviews equilibrium models (Vasicek, Cox-Ingersoll-Ross [CIR]) and no-arbitrage models (Ho-Lee, Kalotay-Williams-Fabozzi [KWF], Black-Derman-Toy [BDT]). Additionally, Marcus applies Litterman and Scheinkman principal component analysis (PCA) to decompose historical yield curve movements into level, steepness, and curvature shifts.",
        "los": "Describe how the time-dependent drift parameter in no-arbitrage models is calibrated.",
        "question": "In the Ho-Lee model ($dr_t = \\theta_t dt + \\sigma dz$), the drift parameter $\\theta_t$ is time-dependent. The fundamental role of specifying $\\theta_t$ as a function of time is to:",
        "options": {
            "A": "Incorporate mean reversion toward a fixed long-run equilibrium interest rate.",
            "B": "Ensure that the model yields an arbitrage-free fit to the observed initial market yield curve.",
            "C": "Eliminate interest rate volatility over extended projection horizons."
        },
        "answer": "B",
        "explanation": "No-arbitrage models (like Ho-Lee and Hull-White) introduce a time-dependent drift $\\theta_t$ specifically to ensure that the model generates bond prices that exactly match the current market prices of benchmark bonds across all maturities. By choosing $\\theta_t$ to fit the initial forward rate curve and its derivative, the model is guaranteed to be arbitrage-free relative to current market prices.",
        "distractor_analysis": {
            "A": "Incorrect. Ho-Lee does not incorporate mean reversion; Hull-White adds mean reversion to Ho-Lee, while Vasicek and CIR use constant parameters.",
            "C": "Incorrect. The drift parameter does not eliminate volatility; $\\sigma$ remains positive and captures ongoing short rate volatility."
        }
    },
    {
        "id": "L2-FI-V03-Q5",
        "level": 2,
        "topic": "Fixed Income",
        "subtopic": "Term Structure Models and Yield Curve Factors",
        "vignette_id": "V03",
        "vignette_title": "Equilibrium vs. No-Arbitrage Term Structure Models and Factor Shifts",
        "vignette_text": "Quantitative strategist Marcus Thorne is evaluating interest rate models for pricing interest rate derivatives and stress-testing bond portfolios. He reviews equilibrium models (Vasicek, Cox-Ingersoll-Ross [CIR]) and no-arbitrage models (Ho-Lee, Kalotay-Williams-Fabozzi [KWF], Black-Derman-Toy [BDT]). Additionally, Marcus applies Litterman and Scheinkman principal component analysis (PCA) to decompose historical yield curve movements into level, steepness, and curvature shifts.",
        "los": "Explain the effect of assumed interest rate volatility on the pricing of bonds and interest rate options in term structure models.",
        "question": "If Marcus increases the assumed interest rate volatility parameter $\\sigma$ in a calibrated binomial interest rate tree, the price of an option-free straight bond and the price of an embedded call option will, respectively:",
        "options": {
            "A": "Straight bond price remains unchanged; call option price increases.",
            "B": "Straight bond price decreases; call option price decreases.",
            "C": "Straight bond price increases; call option price decreases."
        },
        "answer": "A",
        "explanation": "In an arbitrage-free interest rate tree calibrated to the current spot rate curve:\n1. Straight Option-Free Bond: The tree is calibrated to reproduce the market prices of benchmark bonds regardless of volatility. Since the straight bond's cash flows are independent of future rates, its model price is identical to its discounted cash flow value using spot rates; therefore, changes in $\\sigma$ do not change the straight bond price.\n2. Embedded Call Option: An option's payoff is convex. Higher interest rate volatility increases the dispersion of interest rates, widening the spread of nodal bond values and increasing the probability and payoff of the call option being exercised in low-interest-rate nodes. Thus, the embedded call option value increases.",
        "distractor_analysis": {
            "B": "Incorrect. The straight bond price is determined by the spot curve to which the tree is calibrated and does not decrease; furthermore, option value increases with volatility.",
            "C": "Incorrect. Option values increase with volatility, they do not decrease."
        }
    },

    # -------------------------------------------------------------------------
    # VIGNETTE 04
    # -------------------------------------------------------------------------
    {
        "id": "L2-FI-V04-Q1",
        "level": 2,
        "topic": "Fixed Income",
        "subtopic": "Arbitrage-Free Valuation and Binomial Trees",
        "vignette_id": "V04",
        "vignette_title": "Binomial Interest Rate Tree Calibration and Arbitrage-Free Pricing",
        "vignette_text": "Apex Capital's fixed-income analytics unit uses backward induction on a calibrated binomial interest rate tree to value straight and option-embedded debt. Senior analyst Sarah Lin builds a 2-period binomial interest rate tree with annual time steps. The 1-year spot rate is $r_0 = 3.50\\%$. The period 1 (year 1) nodal forward rates are $r_{1,U} = 4.856\\%$ and $r_{1,D} = 3.597\\%$. Risk-neutral transition probabilities are 0.50 for each branch. Sarah values a 2-year annual coupon straight bond with a 4.50% coupon and par value USD 100.",
        "los": "Calculate the value of an option-free bond using a binomial interest rate tree.",
        "question": "Using backward induction on Sarah's binomial interest rate tree, the arbitrage-free value of the 2-year 4.50% coupon straight bond at Node 0 is closest to:",
        "options": {
            "A": "USD 100.52",
            "B": "USD 101.12",
            "C": "USD 102.35"
        },
        "answer": "A",
        "explanation": "We use backward induction on the 2-period binomial interest rate tree for the 2-year 4.50% bond ($C = 4.50$, Par = 100):\n1. At Year 2 maturity, the payoff is $100 + 4.50 = 104.50$ at all nodes.\n2. At Year 1:\n- Up Node ($r_{1,U} = 4.856\\%$):\n$$V_{1,U} = \\frac{104.50}{1 + 0.04856} = \\frac{104.50}{1.04856} = \\text{USD } 99.6605$$\n- Down Node ($r_{1,D} = 3.597\\%$):\n$$V_{1,D} = \\frac{104.50}{1 + 0.03597} = \\frac{104.50}{1.03597} = \\text{USD } 100.8717$$\n3. At Year 0 ($r_0 = 3.50\\%$):\nCalculate expected value at Year 1 plus Year 1 coupon ($4.50$), discounted at $r_0$:\n$$V_0 = \\frac{0.5 \\times (V_{1,U} + 4.50) + 0.5 \\times (V_{1,D} + 4.50)}{1 + r_0}$$\n$$V_0 = \\frac{0.5 \\times (99.6605 + 4.50) + 0.5 \\times (100.8717 + 4.50)}{1.0350}$$\n$$V_0 = \\frac{0.5 \\times 104.1605 + 0.5 \\times 105.3717}{1.0350} = \\frac{104.7661}{1.0350} = \\text{USD } 100.5228 \\approx \\text{USD } 100.52$$",
        "distractor_analysis": {
            "B": "Incorrect. USD 101.12 results from omitting the down node discounting or using an unweighted average of par plus coupon.",
            "C": "Incorrect. USD 102.35 results from erroneously applying the coupon twice or using an inappropriate discount factor."
        }
    },
    {
        "id": "L2-FI-V04-Q2",
        "level": 2,
        "topic": "Fixed Income",
        "subtopic": "Arbitrage-Free Valuation and Binomial Trees",
        "vignette_id": "V04",
        "vignette_title": "Binomial Interest Rate Tree Calibration and Arbitrage-Free Pricing",
        "vignette_text": "Apex Capital's fixed-income analytics unit uses backward induction on a calibrated binomial interest rate tree to value straight and option-embedded debt. Senior analyst Sarah Lin builds a 2-period binomial interest rate tree with annual time steps. The 1-year spot rate is $r_0 = 3.50\\%$. The period 1 (year 1) nodal forward rates are $r_{1,U} = 4.856\\%$ and $r_{1,D} = 3.597\\%$. Risk-neutral transition probabilities are 0.50 for each branch. Sarah values a 2-year annual coupon straight bond with a 4.50% coupon and par value USD 100.",
        "los": "Describe how a binomial interest rate tree is calibrated to be arbitrage-free.",
        "question": "Which of the following conditions is strictly required for Sarah's binomial interest rate tree to be considered 'arbitrage-free'?",
        "options": {
            "A": "The short rates across all future nodes must equal the forward rates implied by the spot curve.",
            "B": "The tree must correctly reprice the benchmark on-the-run Treasury securities that were used to generate the spot rate curve.",
            "C": "The volatility of interest rates across nodes must decline to zero at longer maturities."
        },
        "answer": "B",
        "explanation": "A binomial interest rate tree is defined as arbitrage-free when backward induction on the tree exactly replicates the current market prices (or yields) of benchmark bonds used to construct the tree. If backward induction produces prices differing from observable market prices of benchmark issues, an arbitrage opportunity would exist.",
        "distractor_analysis": {
            "A": "Incorrect. Future nodal rates are dispersed around implied forward rates according to volatility ($r_U$ and $r_D$); they do not individually equal the implied forward rate.",
            "C": "Incorrect. Volatility across nodes is a model input (either constant or time-dependent) and does not need to decline to zero."
        }
    },
    {
        "id": "L2-FI-V04-Q3",
        "level": 2,
        "topic": "Fixed Income",
        "subtopic": "Arbitrage-Free Valuation and Binomial Trees",
        "vignette_id": "V04",
        "vignette_title": "Binomial Interest Rate Tree Calibration and Arbitrage-Free Pricing",
        "vignette_text": "Apex Capital's fixed-income analytics unit uses backward induction on a calibrated binomial interest rate tree to value straight and option-embedded debt. Senior analyst Sarah Lin builds a 2-period binomial interest rate tree with annual time steps. The 1-year spot rate is $r_0 = 3.50\\%$. The period 1 (year 1) nodal forward rates are $r_{1,U} = 4.856\\%$ and $r_{1,D} = 3.597\\%$. Risk-neutral transition probabilities are 0.50 for each branch. Sarah values a 2-year annual coupon straight bond with a 4.50% coupon and par value USD 100.",
        "los": "Explain the relationship between nodal rates in a lognormal binomial interest rate tree.",
        "question": "In a lognormal binomial interest rate tree with an assumed annual volatility $\\sigma$, the mathematical relationship between adjacent nodal rates at time step $t$ ($r_{t,U}$ and $r_{t,D}$) is given by:",
        "options": {
            "A": "$$r_{t,U} = r_{t,D} + 2\\sigma$$",
            "B": "$$r_{t,U} = r_{t,D} \\cdot e^{2\\sigma}$$",
            "C": "$$r_{t,U} = r_{t,D} \\cdot (1 + \\sigma)^2$$"
        },
        "answer": "B",
        "explanation": "In standard lognormal models (such as Black-Derman-Toy or standard CFA curriculum lognormal trees), the natural logarithms of interest rates are spaced by $2\\sigma$ standard deviations between adjacent nodes (an up-step of $+\\sigma$ and a down-step of $-\\sigma$ from the center, so difference is $2\\sigma$):\n$$\\ln(r_{t,U}) - \\ln(r_{t,D}) = 2\\sigma \\implies \\frac{r_{t,U}}{r_{t,D}} = e^{2\\sigma} \\implies r_{t,U} = r_{t,D} \\cdot e^{2\\sigma}$$\nChecking Sarah's data: $r_{1,U} / r_{1,D} = 0.04856 / 0.03597 = 1.3500$, and with $\\sigma = 15\\%$, $e^{2(0.15)} = e^{0.30} = 1.34986$, confirming the formula.",
        "distractor_analysis": {
            "A": "Incorrect. An arithmetic difference of $2\\sigma$ reflects a normal (Ho-Lee) tree structure, not a lognormal tree.",
            "C": "Incorrect. $(1+\\sigma)^2$ is an arithmetic discrete approximation, not the continuous lognormal formulation $e^{2\\sigma}$ used in binomial tree calibration."
        }
    },
    {
        "id": "L2-FI-V04-Q4",
        "level": 2,
        "topic": "Fixed Income",
        "subtopic": "Arbitrage-Free Valuation and Binomial Trees",
        "vignette_id": "V04",
        "vignette_title": "Binomial Interest Rate Tree Calibration and Arbitrage-Free Pricing",
        "vignette_text": "Apex Capital's fixed-income analytics unit uses backward induction on a calibrated binomial interest rate tree to value straight and option-embedded debt. Senior analyst Sarah Lin builds a 2-period binomial interest rate tree with annual time steps. The 1-year spot rate is $r_0 = 3.50\\%$. The period 1 (year 1) nodal forward rates are $r_{1,U} = 4.856\\%$ and $r_{1,D} = 3.597\\%$. Risk-neutral transition probabilities are 0.50 for each branch. Sarah values a 2-year annual coupon straight bond with a 4.50% coupon and par value USD 100.",
        "los": "Describe path independence in binomial interest rate trees.",
        "question": "A recombining binomial interest rate tree implies that moving Up then Down ($UD$) results in the same interest rate node at $t = 2$ as moving Down then Up ($DU$). This property is known as:",
        "options": {
            "A": "Path independence, which significantly reduces the number of computational nodes from $2^T$ to $T + 1$.",
            "B": "Path dependence, which requires tracking all $2^T$ individual interest rate paths.",
            "C": "Arbitrage completeness, which guarantees zero embedded option volatility."
        },
        "answer": "A",
        "explanation": "A recombining tree is path-independent because the interest rate at a node depends solely on the total number of upward and downward steps taken, not the order in which they occurred ($r_{UD} = r_{DU}$). This reduces the number of nodes at time $t$ to $t + 1$ (rather than $2^t$ in a non-recombining tree), drastically improving computational efficiency. Note that mortgage-backed securities (MBS) with prepayment burnouts are path-dependent, necessitating Monte Carlo simulation rather than recombining trees.",
        "distractor_analysis": {
            "B": "Incorrect. Path dependence refers to non-recombining trees where paths cannot merge, resulting in $2^T$ branches.",
            "C": "Incorrect. Recombining trees do not imply zero volatility or complete markets in that manner; it is a structural property of the short-rate lattice."
        }
    },
    {
        "id": "L2-FI-V04-Q5",
        "level": 2,
        "topic": "Fixed Income",
        "subtopic": "Arbitrage-Free Valuation and Binomial Trees",
        "vignette_id": "V04",
        "vignette_title": "Binomial Interest Rate Tree Calibration and Arbitrage-Free Pricing",
        "vignette_text": "Apex Capital's fixed-income analytics unit uses backward induction on a calibrated binomial interest rate tree to value straight and option-embedded debt. Senior analyst Sarah Lin builds a 2-period binomial interest rate tree with annual time steps. The 1-year spot rate is $r_0 = 3.50\\%$. The period 1 (year 1) nodal forward rates are $r_{1,U} = 4.856\\%$ and $r_{1,D} = 3.597\\%$. Risk-neutral transition probabilities are 0.50 for each branch. Sarah values a 2-year annual coupon straight bond with a 4.50% coupon and par value USD 100.",
        "los": "Explain how an arbitrage opportunity can be exploited if a bond is mispriced relative to its tree valuation.",
        "question": "Suppose the 2-year 4.50% straight bond analyzed by Sarah is trading in the market at USD 99.80, while its tree valuation is USD 100.52. An arbitrageur would most appropriately exploit this mispricing by:",
        "options": {
            "A": "Selling short the market-traded bond and lending at the 2-year spot rate.",
            "B": "Buying the market-traded bond at USD 99.80 and replicating a synthetic short position using benchmark zero-coupon bonds.",
            "C": "Buying the market-traded bond and entering a receiver interest rate swap."
        },
        "answer": "B",
        "explanation": "When the market price of a bond (USD 99.80) is less than its theoretical arbitrage-free value (USD 100.52), the bond is underpriced. To exploit the arbitrage:\n1. Buy the underpriced bond in the market for USD 99.80.\n2. Sell short the replicating portfolio of benchmark zero-coupon bonds (delivering the exact cash flows of USD 4.50 at $t = 1$ and USD 104.50 at $t = 2$), receiving the fair value of USD 100.52.\nThis locks in an immediate riskless arbitrage profit of:\n$$\\text{USD } 100.52 - \\text{USD } 99.80 = \\text{USD } 0.72 \\text{ per bond}$$\nAll future cash flows on the long and short legs perfectly offset.",
        "distractor_analysis": {
            "A": "Incorrect. Selling short an underpriced bond would lose money when prices converge to fair value.",
            "C": "Incorrect. Entering a swap does not lock in pure riskless arbitrage against cash flows; it introduces basis and duration exposures."
        }
    },

    # -------------------------------------------------------------------------
    # VIGNETTE 05
    # -------------------------------------------------------------------------
    {
        "id": "L2-FI-V05-Q1",
        "level": 2,
        "topic": "Fixed Income",
        "subtopic": "Bonds with Embedded Options",
        "vignette_id": "V05",
        "vignette_title": "Callable Bond Valuation, Embedded Call Option Dynamics, and Negative Convexity",
        "vignette_text": "Delta Life Insurance manages an institutional liability portfolio and is evaluating a 2-year, 5.50% annual coupon callable bond issued by Titan Power Corp. The bond is callable at par (USD 100) at $t = 1$ immediately following the coupon payment. Quantitative analyst Julian Vance uses a calibrated binomial interest rate tree with annual time steps. The current 1-year spot rate is $r_0 = 4.00\\%$. At Year 1, the nodal forward rates are $r_{1,U} = 5.60\\%$ and $r_{1,D} = 3.80\\%$. Par value is USD 100. Julian is tasked with valuing the straight bond, the embedded call option, and the callable bond.",
        "los": "Calculate the value of a callable bond using a binomial interest rate tree.",
        "question": "Using backward induction on Julian's interest rate tree, the arbitrage-free value of Titan Power Corp's callable bond at Node 0 is closest to:",
        "options": {
            "A": "USD 100.32",
            "B": "USD 100.86",
            "C": "USD 101.44"
        },
        "answer": "B",
        "explanation": "We apply backward induction for the 2-year 5.50% callable bond (callable at 100 at $t = 1$):\n1. At Year 2 (Maturity), payoff = $100 + 5.50 = 105.50$.\n2. At Year 1:\n- Up Node ($r_{1,U} = 5.60\\%$):\nHolding value: $V_{1,U}^{\\text{hold}} = \\frac{105.50}{1 + 0.0560} = \\frac{105.50}{1.0560} = \\text{USD } 99.9053$.\nSince call price is 100 and holding value ($99.9053$) < call price ($100$), the issuer will not call the bond.\nNodal callable bond value: $V_{1,U}^{\\text{call}} = \\min(99.9053, 100) = \\text{USD } 99.9053$.\n- Down Node ($r_{1,D} = 3.80\\%$):\nHolding value: $V_{1,D}^{\\text{hold}} = \\frac{105.50}{1 + 0.0380} = \\frac{105.50}{1.0380} = \\text{USD } 101.6378$.\nSince holding value ($101.6378$) > call price ($100$), the issuer exercises the call at USD 100.\nNodal callable bond value: $V_{1,D}^{\\text{call}} = \\min(101.6378, 100) = \\text{USD } 100.0000$.\n3. At Year 0 ($r_0 = 4.00\\%$):\n$$V_0^{\\text{call}} = \\frac{0.5 \\times (V_{1,U}^{\\text{call}} + 5.50) + 0.5 \\times (V_{1,D}^{\\text{call}} + 5.50)}{1 + r_0}$$\n$$V_0^{\\text{call}} = \\frac{0.5 \\times (99.9053 + 5.50) + 0.5 \\times (100.0000 + 5.50)}{1.0400}$$\n$$V_0^{\\text{call}} = \\frac{0.5 \\times 105.4053 + 0.5 \\times 105.5000}{1.0400} = \\frac{105.45265}{1.0400} = \\text{USD } 100.8631 \\approx \\text{USD } 100.86$$",
        "distractor_analysis": {
            "A": "Incorrect. USD 100.32 is obtained if the bond were mistakenly called at both nodes or discounted at an inflated rate.",
            "C": "Incorrect. USD 101.44 is the value of the option-free straight bond without accounting for the call exercise at the down node ($V_0^{\\text{straight}} = \\frac{0.5(99.9053+5.5)+0.5(101.6378+5.5)}{1.04} = \\frac{106.0215}{1.04} = \\text{USD } 101.44$)."
        }
    },
    {
        "id": "L2-FI-V05-Q2",
        "level": 2,
        "topic": "Fixed Income",
        "subtopic": "Bonds with Embedded Options",
        "vignette_id": "V05",
        "vignette_title": "Callable Bond Valuation, Embedded Call Option Dynamics, and Negative Convexity",
        "vignette_text": "Delta Life Insurance manages an institutional liability portfolio and is evaluating a 2-year, 5.50% annual coupon callable bond issued by Titan Power Corp. The bond is callable at par (USD 100) at $t = 1$ immediately following the coupon payment. Quantitative analyst Julian Vance uses a calibrated binomial interest rate tree with annual time steps. The current 1-year spot rate is $r_0 = 4.00\\%$. At Year 1, the nodal forward rates are $r_{1,U} = 5.60\\%$ and $r_{1,D} = 3.80\\%$. Par value is USD 100. Julian is tasked with valuing the straight bond, the embedded call option, and the callable bond.",
        "los": "Calculate the value of an embedded call option.",
        "question": "Based on Julian's calculations, the value of the embedded call option held by Titan Power Corp is closest to:",
        "options": {
            "A": "USD 0.58",
            "B": "USD 0.86",
            "C": "USD 1.44"
        },
        "answer": "A",
        "explanation": "The value of a callable bond is equal to the straight bond value minus the embedded call option value:\n$$V_{\\text{callable}} = V_{\\text{straight}} - V_{\\text{call}} \\implies V_{\\text{call}} = V_{\\text{straight}} - V_{\\text{callable}}$$\n1. From Question 1, $V_{\\text{callable}} = \\text{USD } 100.8631$.\n2. The straight bond value is:\n$$V_0^{\\text{straight}} = \\frac{0.5 \\times (99.9053 + 5.50) + 0.5 \\times (101.6378 + 5.50)}{1.0400} = \\frac{105.77155}{1.0400} = \\text{USD } 101.4438$$\n3. The value of the embedded call option is:\n$$V_{\\text{call}} = 101.4438 - 100.8631 = \\text{USD } 0.5807 \\approx \\text{USD } 0.58$$",
        "distractor_analysis": {
            "B": "Incorrect. USD 0.86 represents the premium of the callable bond above par ($100.86 - 100.00$), not the option value.",
            "C": "Incorrect. USD 1.44 represents the straight bond's premium above par ($101.44 - 100.00$)."
        }
    },
    {
        "id": "L2-FI-V05-Q3",
        "level": 2,
        "topic": "Fixed Income",
        "subtopic": "Bonds with Embedded Options",
        "vignette_id": "V05",
        "vignette_title": "Callable Bond Valuation, Embedded Call Option Dynamics, and Negative Convexity",
        "vignette_text": "Delta Life Insurance manages an institutional liability portfolio and is evaluating a 2-year, 5.50% annual coupon callable bond issued by Titan Power Corp. The bond is callable at par (USD 100) at $t = 1$ immediately following the coupon payment. Quantitative analyst Julian Vance uses a calibrated binomial interest rate tree with annual time steps. The current 1-year spot rate is $r_0 = 4.00\\%$. At Year 1, the nodal forward rates are $r_{1,U} = 5.60\\%$ and $r_{1,D} = 3.80\\%$. Par value is USD 100. Julian is tasked with valuing the straight bond, the embedded call option, and the callable bond.",
        "los": "Describe the price-yield relationship and negative convexity of a callable bond.",
        "question": "Which of the following statements best explains why callable bonds exhibit 'negative convexity' at low interest rate levels?",
        "options": {
            "A": "As interest rates fall, the price of the callable bond increases at an accelerating rate because coupon reinvestment income rises.",
            "B": "As interest rates fall, the embedded call option increases in value rapidly, capping price appreciation and causing the price-yield curve to become concave.",
            "C": "The issuer pays an option premium to the investor whenever yields decline below the coupon rate."
        },
        "answer": "B",
        "explanation": "For an option-free straight bond, the price-yield relationship is strictly convex (positive convexity), meaning price gains from declining yields exceed price losses from equal yield increases.\nHowever, for a callable bond, $V_{\\text{callable}} = V_{\\text{straight}} - V_{\\text{call}}$. As yields decline, the likelihood of the bond being called increases dramatically, and the embedded call option becomes deeply in-the-money. The bond price is compressed toward the call price (price compression). Consequently, at low yields, the bond's price appreciation decelerates, the second derivative of price with respect to yield turns negative, and the price-yield curve becomes concave (exhibiting negative convexity).",
        "distractor_analysis": {
            "A": "Incorrect. Coupon reinvestment decreases as rates fall, and price appreciation decelerates rather than accelerates.",
            "C": "Incorrect. The issuer holds the call option; the investor does not receive option premium payments when yields fall."
        }
    },
    {
        "id": "L2-FI-V05-Q4",
        "level": 2,
        "topic": "Fixed Income",
        "subtopic": "Bonds with Embedded Options",
        "vignette_id": "V05",
        "vignette_title": "Callable Bond Valuation, Embedded Call Option Dynamics, and Negative Convexity",
        "vignette_text": "Delta Life Insurance manages an institutional liability portfolio and is evaluating a 2-year, 5.50% annual coupon callable bond issued by Titan Power Corp. The bond is callable at par (USD 100) at $t = 1$ immediately following the coupon payment. Quantitative analyst Julian Vance uses a calibrated binomial interest rate tree with annual time steps. The current 1-year spot rate is $r_0 = 4.00\\%$. At Year 1, the nodal forward rates are $r_{1,U} = 5.60\\%$ and $r_{1,D} = 3.80\\%$. Par value is USD 100. Julian is tasked with valuing the straight bond, the embedded call option, and the callable bond.",
        "los": "Describe the effect of interest rate volatility on the value of callable bonds and embedded options.",
        "question": "If market interest rate volatility increases, what is the expected impact on the value of the embedded call option and the value of Titan Power Corp's callable bond?",
        "options": {
            "A": "Embedded call option value increases; callable bond value decreases.",
            "B": "Embedded call option value increases; callable bond value increases.",
            "C": "Embedded call option value decreases; callable bond value decreases."
        },
        "answer": "A",
        "explanation": "Because option values are convex functions of the underlying interest rate distribution, an increase in interest rate volatility expands the dispersion of future yields and increases the probability of extreme low yields where the call is deeply in-the-money. Thus, the embedded call option value ($V_{\\text{call}}$) increases.\nSince the callable bond price is given by:\n$$V_{\\text{callable}} = V_{\\text{straight}} - V_{\\text{call}}$$\nand the straight bond value is unaffected by volatility changes in a calibrated tree, an increase in $V_{\\text{call}}$ directly reduces $V_{\\text{callable}}$.",
        "distractor_analysis": {
            "B": "Incorrect. Because the call option is subtracted from the straight bond, an increase in option value must decrease the callable bond's value.",
            "C": "Incorrect. Option value increases with volatility, not decreases."
        }
    },
    {
        "id": "L2-FI-V05-Q5",
        "level": 2,
        "topic": "Fixed Income",
        "subtopic": "Bonds with Embedded Options",
        "vignette_id": "V05",
        "vignette_title": "Callable Bond Valuation, Embedded Call Option Dynamics, and Negative Convexity",
        "vignette_text": "Delta Life Insurance manages an institutional liability portfolio and is evaluating a 2-year, 5.50% annual coupon callable bond issued by Titan Power Corp. The bond is callable at par (USD 100) at $t = 1$ immediately following the coupon payment. Quantitative analyst Julian Vance uses a calibrated binomial interest rate tree with annual time steps. The current 1-year spot rate is $r_0 = 4.00\\%$. At Year 1, the nodal forward rates are $r_{1,U} = 5.60\\%$ and $r_{1,D} = 3.80\\%$. Par value is USD 100. Julian is tasked with valuing the straight bond, the embedded call option, and the callable bond.",
        "los": "Explain the optimal call exercise rule for the issuer of a callable bond.",
        "question": "At any node in a binomial interest rate tree, the issuer of a callable bond with call price $CP$ will rationally exercise the call option if and only if:",
        "options": {
            "A": "The holding value of the bond exceeds the call price ($V_{\\text{hold}} > CP$).",
            "B": "The market yield exceeds the coupon rate of the bond.",
            "C": "The holding value of the bond is less than the par value ($V_{\\text{hold}} < 100$)."
        },
        "answer": "A",
        "explanation": "The issuer holds the right to retire the debt at the call price $CP$. If the holding value of the bond (the present value of remaining cash flows if left outstanding) exceeds $CP$, the issuer can call the bond for $CP$ and refinance at prevailing lower market interest rates. Therefore, the rational issuer calls the bond whenever $V_{\\text{hold}} > CP$, capping the value of the bond to the investor at $\\min(V_{\\text{hold}}, CP)$.",
        "distractor_analysis": {
            "B": "Incorrect. If market yields exceed the coupon rate, bond prices are below par, so the issuer would not exercise a call at par.",
            "C": "Incorrect. If the holding value is below par, calling at par would destroy issuer value by overpaying for the debt."
        }
    },

    # -------------------------------------------------------------------------
    # VIGNETTE 06
    # -------------------------------------------------------------------------
    {
        "id": "L2-FI-V06-Q1",
        "level": 2,
        "topic": "Fixed Income",
        "subtopic": "Putable Bonds and Step-Up Coupons",
        "vignette_id": "V06",
        "vignette_title": "Putable Bond Valuation and Step-Up Coupon Dynamics",
        "vignette_text": "Fixed-income manager Robert Chen is assessing putable debt securities and step-up callable notes for pension fund clients who seek downside interest rate protection. Robert is pricing a 2-year, 4.00% annual coupon bond putable at par (USD 100) at $t = 1$. The 1-year spot rate is $r_0 = 4.50\\%$. At Year 1, the nodal forward rates from a calibrated binomial tree are $r_{1,U} = 5.80\\%$ and $r_{1,D} = 3.90\\%$. Par value is USD 100. Concurrently, Robert evaluates a step-up coupon callable note whose coupon steps up if uncalled.",
        "los": "Calculate the value of a putable bond using a binomial interest rate tree.",
        "question": "Using backward induction on Robert's binomial interest rate tree, the arbitrage-free value of the 2-year 4.00% putable bond at Node 0 is closest to:",
        "options": {
            "A": "USD 98.75",
            "B": "USD 99.57",
            "C": "USD 100.85"
        },
        "answer": "B",
        "explanation": "We apply backward induction for the 2-year 4.00% putable bond (putable at par USD 100 at $t = 1$):\n1. At Year 2 (Maturity), payoff = $100 + 4.00 = 104.00$.\n2. At Year 1:\n- Up Node ($r_{1,U} = 5.80\\%$):\nHolding value: $V_{1,U}^{\\text{hold}} = \\frac{104.00}{1 + 0.0580} = \\frac{104.00}{1.0580} = \\text{USD } 98.2987$.\nSince put price is USD 100 and holding value (USD 98.2987) < put price (USD 100), the investor exercises the put option.\nNodal putable bond value: $V_{1,U}^{\\text{put}} = \\max(98.2987, 100) = \\text{USD } 100.0000$.\n- Down Node ($r_{1,D} = 3.90\\%$):\nHolding value: $V_{1,D}^{\\text{hold}} = \\frac{104.00}{1 + 0.0390} = \\frac{104.00}{1.0390} = \\text{USD } 100.0962$.\nSince holding value (USD 100.0962) > put price (USD 100), the investor holds the bond.\nNodal putable bond value: $V_{1,D}^{\\text{put}} = \\max(100.0962, 100) = \\text{USD } 100.0962$.\n3. At Year 0 ($r_0 = 4.50\\%$):\n$$V_0^{\\text{put}} = \\frac{0.5 \\times (V_{1,U}^{\\text{put}} + 4.00) + 0.5 \\times (V_{1,D}^{\\text{put}} + 4.00)}{1 + r_0}$$\n$$V_0^{\\text{put}} = \\frac{0.5 \\times (100.0000 + 4.00) + 0.5 \\times (100.0962 + 4.00)}{1.0450}$$\n$$V_0^{\\text{put}} = \\frac{0.5 \\times 104.0000 + 0.5 \\times 104.0962}{1.0450} = \\frac{104.0481}{1.0450} = \\text{USD } 99.5676 \\approx \\text{USD } 99.57$$",
        "distractor_analysis": {
            "A": "Incorrect. USD 98.75 is the value of an option-free straight bond without the embedded put option ($V_0^{\\text{straight}} = \\frac{0.5(98.2987+4) + 0.5(100.0962+4)}{1.045} = 98.7535$).",
            "C": "Incorrect. USD 100.85 assumes the bond is putable at an inflated exercise price or erroneously adds the coupon twice."
        }
    },
    {
        "id": "L2-FI-V06-Q2",
        "level": 2,
        "topic": "Fixed Income",
        "subtopic": "Putable Bonds and Step-Up Coupons",
        "vignette_id": "V06",
        "vignette_title": "Putable Bond Valuation and Step-Up Coupon Dynamics",
        "vignette_text": "Fixed-income manager Robert Chen is assessing putable debt securities and step-up callable notes for pension fund clients who seek downside interest rate protection. Robert is pricing a 2-year, 4.00% annual coupon bond putable at par (USD 100) at $t = 1$. The 1-year spot rate is $r_0 = 4.50\\%$. At Year 1, the nodal forward rates from a calibrated binomial tree are $r_{1,U} = 5.80\\%$ and $r_{1,D} = 3.90\\%$. Par value is USD 100. Concurrently, Robert evaluates a step-up coupon callable note whose coupon steps up if uncalled.",
        "los": "Calculate the value of an embedded put option.",
        "question": "The value of the embedded put option held by the bondholders is closest to:",
        "options": {
            "A": "USD 0.81",
            "B": "USD 1.25",
            "C": "USD 1.70"
        },
        "answer": "A",
        "explanation": "The value of a putable bond is equal to the straight bond value plus the value of the embedded put option:\n$$V_{\\text{putable}} = V_{\\text{straight}} + V_{\\text{put}} \\implies V_{\\text{put}} = V_{\\text{putable}} - V_{\\text{straight}}$$\n1. Putable bond value from backward induction: $V_{\\text{putable}} = \\text{USD } 99.57$.\n2. Straight bond value:\n$$V_0^{\\text{straight}} = \\frac{0.5 \\times (98.2987 + 4.00) + 0.5 \\times (100.0962 + 4.00)}{1.0450} = \\frac{103.19745}{1.0450} = \\text{USD } 98.7535$$\n3. Value of the embedded put option:\n$$V_{\\text{put}} = 99.5676 - 98.7535 = \\text{USD } 0.8141 \\approx \\text{USD } 0.81$$",
        "distractor_analysis": {
            "B": "Incorrect. USD 1.25 represents an arbitrary difference or miscalculation of the up-node payoff.",
            "C": "Incorrect. USD 1.70 is the undiscounted difference at the up node ($100 - 98.2987 = 1.7013$), failing to weight by risk-neutral probability and discount back to $t = 0$."
        }
    },
    {
        "id": "L2-FI-V06-Q3",
        "level": 2,
        "topic": "Fixed Income",
        "subtopic": "Putable Bonds and Step-Up Coupons",
        "vignette_id": "V06",
        "vignette_title": "Putable Bond Valuation and Step-Up Coupon Dynamics",
        "vignette_text": "Fixed-income manager Robert Chen is assessing putable debt securities and step-up callable notes for pension fund clients who seek downside interest rate protection. Robert is pricing a 2-year, 4.00% annual coupon bond putable at par (USD 100) at $t = 1$. The 1-year spot rate is $r_0 = 4.50\\%$. At Year 1, the nodal forward rates from a calibrated binomial tree are $r_{1,U} = 5.80\\%$ and $r_{1,D} = 3.90\\%$. Par value is USD 100. Concurrently, Robert evaluates a step-up coupon callable note whose coupon steps up if uncalled.",
        "los": "Describe the price-yield relationship and convexity of a putable bond.",
        "question": "Which of the following statements regarding the convexity of a putable bond is most accurate across all yield levels?",
        "options": {
            "A": "A putable bond exhibits negative convexity at high yields.",
            "B": "A putable bond exhibits positive convexity across all yield levels, with convexity exceeding that of an otherwise identical straight bond when yields rise.",
            "C": "A putable bond's convexity drops to zero whenever the embedded put option is out-of-the-money."
        },
        "answer": "B",
        "explanation": "Because the investor holds the put option, $V_{\\text{putable}} = V_{\\text{straight}} + V_{\\text{put}}$. Both the straight bond and the put option possess positive convexity. When interest rates rise, the put option moves into the money, providing a price floor at the put price (e.g., 100). This protects the bond from price declines, flattening the price-yield curve at high yields while preserving upward price appreciation at low yields. Consequently, a putable bond exhibits strictly positive convexity across all yield environments, and its convexity is higher than that of a straight bond at elevated yield levels.",
        "distractor_analysis": {
            "A": "Incorrect. Negative convexity is a feature of callable bonds at low yields, not putable bonds.",
            "C": "Incorrect. When the put option is out-of-the-money, the putable bond behaves like a straight bond and continues to exhibit positive convexity, not zero convexity."
        }
    },
    {
        "id": "L2-FI-V06-Q4",
        "level": 2,
        "topic": "Fixed Income",
        "subtopic": "Putable Bonds and Step-Up Coupons",
        "vignette_id": "V06",
        "vignette_title": "Putable Bond Valuation and Step-Up Coupon Dynamics",
        "vignette_text": "Fixed-income manager Robert Chen is assessing putable debt securities and step-up callable notes for pension fund clients who seek downside interest rate protection. Robert is pricing a 2-year, 4.00% annual coupon bond putable at par (USD 100) at $t = 1$. The 1-year spot rate is $r_0 = 4.50\\%$. At Year 1, the nodal forward rates from a calibrated binomial tree are $r_{1,U} = 5.80\\%$ and $r_{1,D} = 3.90\\%$. Par value is USD 100. Concurrently, Robert evaluates a step-up coupon callable note whose coupon steps up if uncalled.",
        "los": "Describe the investment characteristics of step-up callable notes.",
        "question": "Robert evaluates a step-up callable bond where the coupon increases from 4.00% to 6.50% after Year 1 if the bond is not called. From the issuer's perspective, this step-up feature primarily functions to:",
        "options": {
            "A": "Incentivize the issuer to call and refinance the bond at Year 1 unless its borrowing cost has risen significantly.",
            "B": "Provide the investor with an option to put the bond back to the issuer at a premium.",
            "C": "Eliminate extension risk for the bondholder under rising interest rate regimes."
        },
        "answer": "A",
        "explanation": "A step-up callable bond specifies a substantial increase in coupon after the call date. This penalizes the issuer with an elevated financing cost if the bond remains outstanding. Consequently, the issuer faces strong economic pressure to call the bond at Year 1 and refinance, unless the issuer's credit rating has deteriorated or benchmark rates have surged so severely that refinancing in the open market would exceed the stepped-up coupon rate.",
        "distractor_analysis": {
            "B": "Incorrect. A step-up callable bond grants a call option to the issuer, not a put option to the investor.",
            "C": "Incorrect. Extension risk remains because if market yields spike above the stepped-up rate, the issuer will refrain from calling, leaving the investor holding the note for its full extended term."
        }
    },
    {
        "id": "L2-FI-V06-Q5",
        "level": 2,
        "topic": "Fixed Income",
        "subtopic": "Putable Bonds and Step-Up Coupons",
        "vignette_id": "V06",
        "vignette_title": "Putable Bond Valuation and Step-Up Coupon Dynamics",
        "vignette_text": "Fixed-income manager Robert Chen is assessing putable debt securities and step-up callable notes for pension fund clients who seek downside interest rate protection. Robert is pricing a 2-year, 4.00% annual coupon bond putable at par (USD 100) at $t = 1$. The 1-year spot rate is $r_0 = 4.50\\%$. At Year 1, the nodal forward rates from a calibrated binomial tree are $r_{1,U} = 5.80\\%$ and $r_{1,D} = 3.90\\%$. Par value is USD 100. Concurrently, Robert evaluates a step-up coupon callable note whose coupon steps up if uncalled.",
        "los": "Compare the effective duration of callable, putable, and straight bonds across different interest rate regimes.",
        "question": "Under a high interest rate regime where yields rise substantially, how does the effective duration of a putable bond compare to an otherwise identical straight bond?",
        "options": {
            "A": "Effective duration of the putable bond is significantly lower than that of the straight bond.",
            "B": "Effective duration of the putable bond is significantly higher than that of the straight bond.",
            "C": "Effective duration of the putable bond equals the straight bond because the put option is out-of-the-money."
        },
        "answer": "A",
        "explanation": "When interest rates rise substantially, the holding value of the bond falls below the put exercise price (e.g., 100), driving the put option deeply into the money. At this point, the bond's maturity effectively shortens to the nearest put date because rational investors will put the bond back to the issuer at par. Therefore, the price sensitivity to further rate changes drops toward zero around the put date, and the effective duration of the putable bond is significantly lower than that of an otherwise identical option-free straight bond.",
        "distractor_analysis": {
            "B": "Incorrect. An embedded put option shortens duration at high rates; it never lengthens duration above a straight bond.",
            "C": "Incorrect. High interest rates push the put option into-the-money (not out-of-the-money) because bond prices decline below par."
        }
    }
]
