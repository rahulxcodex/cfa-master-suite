# -*- coding: utf-8 -*-
"""
Module 3: Introduction to Fixed-Income Valuation (Q27-Q44)
CFA Level 1 Fixed Income Question Bank
"""

M3_QUESTIONS = [
    {
        "id": "L1-FI-027",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Introduction to Fixed-Income Valuation",
        "los": "Calculate a bond's price given a market discount rate",
        "question": "A 3-year corporate bond has a par value of USD 1,000 and pays an annual coupon of 6.00%. If the market discount rate (YTM) is 5.00%, the price of the bond is closest to:",
        "options": {
            "A": "USD 973.27.",
            "B": "USD 1,000.00.",
            "C": "USD 1,027.23."
        },
        "answer": "C",
        "explanation": "The price of an annual-pay bond is the present value of its future cash flows discounted at the market discount rate $y = 5.00\\%$: $$P = \\sum_{t=1}^{n} \\frac{C}{(1+y)^t} + \\frac{M}{(1+y)^n}$$ With $C = \\text{USD } 60$, $M = \\text{USD } 1{,}000$, and $n = 3$: $$P = \\frac{60}{1.05^1} + \\frac{60}{1.05^2} + \\frac{1{,}060}{1.05^3}$$ $$P = 57.1429 + 54.4218 + 915.6672 = \\text{USD } 1{,}027.23$$ Because the coupon rate (6.00%) exceeds the market discount rate (5.00%), the bond trades at a premium.",
        "distractor_analysis": {
            "A": "Incorrect because USD 973.27 discounts cash flows at 7.00% instead of 5.00% (discount instead of premium).",
            "B": "Incorrect because USD 1,000.00 is par value, which only occurs when coupon rate equals the market discount rate."
        }
    },
    {
        "id": "L1-FI-028",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Introduction to Fixed-Income Valuation",
        "los": "Calculate a bond's price given a market discount rate",
        "question": "A 5-year, 7.00% semi-annual coupon bond has a par value of USD 1,000 and a yield-to-maturity of 8.00% on a semi-annual bond basis. The price of the bond per USD 100 of par value is closest to:",
        "options": {
            "A": "95.94.",
            "B": "96.01.",
            "C": "104.16."
        },
        "answer": "A",
        "explanation": "For a semi-annual bond, the number of periods is $n = 5 \\times 2 = 10$, the periodic coupon is $PMT = \\frac{7.00}{2} = 3.50$, and the periodic discount rate is $r = \\frac{8.00\\%}{2} = 4.00\\%$: $$PV = \\sum_{t=1}^{10} \\frac{3.50}{(1.04)^t} + \\frac{100}{(1.04)^{10}}$$ Using the annuity formula: $$PV = 3.50 \\times \\left[ \\frac{1 - (1.04)^{-10}}{0.04} \\right] + \\frac{100}{(1.04)^{10}}$$ $$PV = 3.50 \\times 8.11090 + 100 \\times 0.67556 = 28.3881 + 67.5564 = 95.9445 \\approx 95.94$$",
        "distractor_analysis": {
            "B": "Incorrect because 96.01 uses annual compounding ($N=5, I/Y=8\\%, PMT=7, FV=100$) instead of semi-annual compounding.",
            "C": "Incorrect because 104.16 inverts the relationship, pricing the bond as if YTM were 6.00% rather than 8.00%."
        }
    },
    {
        "id": "L1-FI-029",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Introduction to Fixed-Income Valuation",
        "los": "Describe matrix pricing",
        "question": "An analyst uses matrix pricing to estimate the required yield on a newly issued, illiquid 4-year corporate bond rated A. The market yields on actively traded comparable A-rated corporate bonds are:\n- 3-year bond: 4.80%\n- 6-year bond: 5.40%\nUsing linear interpolation, the estimated required yield for the 4-year bond is closest to:",
        "options": {
            "A": "4.95%.",
            "B": "5.00%.",
            "C": "5.10%."
        },
        "answer": "B",
        "explanation": "Matrix pricing estimates the yield of an illiquid bond by interpolating between yields of traded bonds with similar credit ratings and adjacent maturities: $$\\text{Yield}_4 = \\text{Yield}_3 + \\left( \\frac{4 - 3}{6 - 3} \\right) \\times (\\text{Yield}_6 - \\text{Yield}_3)$$ $$\\text{Yield}_4 = 4.80\\% + \\left( \\frac{1}{3} \\right) \\times (5.40\\% - 4.80\\%) = 4.80\\% + 0.20\\% = 5.00\\%$$",
        "distractor_analysis": {
            "A": "Incorrect because 4.95% incorrectly applies a 1/4 weighting instead of 1/3 weighting ($4.80\\% + 0.25 \\times 0.60\\% = 4.95\\%$).",
            "C": "Incorrect because 5.10% is the simple midpoint between 4.80% and 5.40%, corresponding to a 4.5-year bond rather than a 4-year bond."
        }
    },
    {
        "id": "L1-FI-030",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Introduction to Fixed-Income Valuation",
        "los": "Calculate and interpret yield and price measures for money market instruments",
        "question": "A 90-day US Treasury bill with a face value of USD 100,000 is quoted at a bank discount yield of 4.00%. The purchase price of the Treasury bill is closest to:",
        "options": {
            "A": "USD 96,000.",
            "B": "USD 99,000.",
            "C": "USD 99,014."
        },
        "answer": "B",
        "explanation": "The bank discount yield ($r_{\\text{BD}}$) formula is based on face value and a 360-day year: $$r_{\\text{BD}} = \\frac{D}{F} \\times \\frac{360}{t}$$ Solving for the dollar discount $D$: $$D = F \\times r_{\\text{BD}} \\times \\frac{t}{360} = \\text{USD } 100{,}000 \\times 0.0400 \\times \\frac{90}{360} = \\text{USD } 1{,}000$$ The purchase price $P$ is: $$P = F - D = \\text{USD } 100{,}000 - \\text{USD } 1{,}000 = \\text{USD } 99{,}000$$",
        "distractor_analysis": {
            "A": "Incorrect because USD 96,000 calculates the discount without adjusting for the 90-day fraction ($100{,}000 \\times 0.04 = 4{,}000$).",
            "C": "Incorrect because USD 99,014 uses a 365-day year convention ($100{,}000 - 100{,}000 \\times 0.04 \\times 90/365$) instead of the standard 360-day bank discount convention."
        }
    },
    {
        "id": "L1-FI-031",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Introduction to Fixed-Income Valuation",
        "los": "Calculate and interpret yield and price measures for money market instruments",
        "question": "A 180-day commercial paper note with a face value of USD 1,000,000 is purchased for USD 980,000. Assuming a 360-day year, the money market yield (CD-equivalent add-on yield) is closest to:",
        "options": {
            "A": "4.00%.",
            "B": "4.08%.",
            "C": "4.14%."
        },
        "answer": "B",
        "explanation": "The money market yield (also known as CD equivalent yield) is an annualized add-on rate based on purchase price and a 360-day year: $$r_{\\text{MM}} = \\left( \\frac{F - P}{P} \\right) \\times \\frac{360}{t}$$ $$r_{\\text{MM}} = \\left( \\frac{\\text{USD } 1{,}000{,}000 - \\text{USD } 980{,}000}{\\text{USD } 980{,}000} \\right) \\times \\frac{360}{180} = \\left( \\frac{20{,}000}{980{,}000} \\right) \\times 2 = 0.020408 \\times 2 = 4.0816\\% \\approx 4.08\\%$$",
        "distractor_analysis": {
            "A": "Incorrect because 4.00% is the bank discount yield calculated using face value as the denominator: $(20{,}000 / 1{,}000{,}000) \\times (360 / 180) = 4.00\\%$.",
            "C": "Incorrect because 4.14% is the bond equivalent yield (BEY) which annualizes using a 365-day year: $(20{,}000 / 980{,}000) \\times (365 / 180) = 4.138\\% \\approx 4.14\\%$."
        }
    },
    {
        "id": "L1-FI-032",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Introduction to Fixed-Income Valuation",
        "los": "Calculate accrued interest, full price, and clean price",
        "question": "A corporate bond with a par value of USD 1,000 pays a 6.00% semi-annual coupon on 30 June and 31 December. An investor buys the bond for settlement on 30 September at a flat (clean) price of USD 990.00. Assuming the 30/360 day-count convention, the accrued interest and the full (dirty) price are closest to:",
        "options": {
            "A": "Accrued interest = USD 15.00; Full price = USD 1,005.00.",
            "B": "Accrued interest = USD 15.00; Full price = USD 975.00.",
            "C": "Accrued interest = USD 30.00; Full price = USD 1,020.00."
        },
        "answer": "A",
        "explanation": "Under the 30/360 convention, there are 30 days in each month. From 30 June to 30 September is 3 full months: $$\\text{Days elapsed} = 3 \\times 30 = 90 \\text{ days}$$ The semi-annual period contains 180 days. The semi-annual coupon payment is: $$PMT = \\frac{6.00\\% \\times \\text{USD } 1{,}000}{2} = \\text{USD } 30.00$$ The accrued interest is: $$AI = \\frac{t}{T} \\times PMT = \\frac{90}{180} \\times \\text{USD } 30.00 = \\text{USD } 15.00$$ The full (dirty) price paid by the buyer is: $$\\text{Full Price} = \\text{Flat Price} + AI = \\text{USD } 990.00 + \\text{USD } 15.00 = \\text{USD } 1{,}005.00$$",
        "distractor_analysis": {
            "B": "Incorrect because accrued interest is added to the flat price to determine the full price, not subtracted ($990 - 15 = 975$).",
            "C": "Incorrect because USD 30.00 represents the full 6-month semi-annual coupon rather than the 3-month accrued interest portion."
        }
    },
    {
        "id": "L1-FI-033",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Introduction to Fixed-Income Valuation",
        "los": "Describe the relationship among spot rates, forward rates, and yield to maturity",
        "question": "A bond pays annual coupons and has an annual yield-to-maturity of 6.09% (periodicity $m=1$). Its annualized yield-to-maturity on a semi-annual bond basis (periodicity $m=2$) is closest to:",
        "options": {
            "A": "5.91%.",
            "B": "6.00%.",
            "C": "6.18%."
        },
        "answer": "B",
        "explanation": "To convert an annual yield $APR_1 = 6.09\\%$ to an equivalent semi-annual basis $APR_2$, equate their compounding factors: $$\\left(1 + \\frac{APR_2}{2}\\right)^2 = (1 + APR_1)^1$$ $$\\left(1 + \\frac{APR_2}{2}\\right)^2 = 1.0609$$ $$1 + \\frac{APR_2}{2} = \\sqrt{1.0609} = 1.03$$ $$\\frac{APR_2}{2} = 0.03 \\implies APR_2 = 2 \\times 0.03 = 0.0600 = 6.00\\%$$",
        "distractor_analysis": {
            "A": "Incorrect due to misapplying compounding formulas or dividing $6.09\\%$ incorrectly.",
            "C": "Incorrect because converting from an annual rate to a higher frequency rate must result in a lower nominal rate ($6.00\\% < 6.09\\%$), not a higher rate."
        }
    },
    {
        "id": "L1-FI-034",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Introduction to Fixed-Income Valuation",
        "los": "Define and compare yield measures for fixed-rate bonds",
        "question": "A callable bond trading at a premium above par value can be called by the issuer in 3 years at 102 or in 5 years at par (100). The bond matures in 10 years. An investor calculating the bond's Yield-to-Worst (YTW) will select the:",
        "options": {
            "A": "Highest calculated yield among yield-to-maturity and all possible yields-to-call.",
            "B": "Lowest calculated yield among yield-to-maturity and all possible yields-to-call.",
            "C": "Weighted average of yield-to-maturity and the respective yields-to-call."
        },
        "answer": "B",
        "explanation": "Yield-to-Worst (YTW) is the most conservative yield metric for a callable bond. An analyst calculates the yield to maturity (YTM) as well as the yield to call (YTC) for every contractual call date. The minimum (lowest) of all these potential yields represents the Yield-to-Worst, reflecting the worst-case return scenario assuming the issuer behaves rationally.",
        "distractor_analysis": {
            "A": "Incorrect because Yield-to-Worst selects the lowest (most conservative) yield, not the highest.",
            "C": "Incorrect because YTW is a discrete minimum selection, not a probability-weighted average."
        }
    },
    {
        "id": "L1-FI-035",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Introduction to Fixed-Income Valuation",
        "los": "Calculate and interpret the discount margin for a floating-rate note",
        "question": "A floating-rate note (FRN) pays a quarterly coupon of 90-day Euribor plus a quoted margin (QM) of 75 bps. If the market's required margin (discount margin, DM) for the issuer's credit risk rises to 100 bps on a reset date, the FRN will trade at:",
        "options": {
            "A": "A discount to par value.",
            "B": "Par value.",
            "C": "A premium to par value."
        },
        "answer": "A",
        "explanation": "On a coupon reset date, an FRN trades at par value if and only if the quoted margin equals the discount margin ($QM = DM$). When the discount margin required by investors exceeds the quoted margin offered by the note ($DM > QM$), the coupon payments are insufficient relative to market requirements, causing the FRN to trade at a discount to par value. Conversely, if $QM > DM$, it trades at a premium.",
        "distractor_analysis": {
            "B": "Incorrect because an FRN resets to par on reset dates only if $QM = DM$; here $QM = 75$ bps while $DM = 100$ bps.",
            "C": "Incorrect because the note would trade at a premium only if the quoted margin were higher than the required discount margin ($QM > DM$)."
        }
    },
    {
        "id": "L1-FI-036",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Introduction to Fixed-Income Valuation",
        "los": "Calculate the arbitrage-free value of an option-free bond",
        "question": "The annualized spot rates for zero-coupon government bonds are:\n- 1-year: $S_1 = 3.00\\%$\n- 2-year: $S_2 = 4.00\\%$\n- 3-year: $S_3 = 5.00\\%$\nA 3-year, 4.00% annual coupon government bond with par value USD 1,000 has an arbitrage-free price closest to:",
        "options": {
            "A": "USD 974.19.",
            "B": "USD 976.22.",
            "C": "USD 1,000.00."
        },
        "answer": "A",
        "explanation": "Under arbitrage-free valuation, each individual cash flow is discounted at the corresponding spot rate for that specific maturity: $$P = \\frac{C}{1 + S_1} + \\frac{C}{(1 + S_2)^2} + \\frac{C + M}{(1 + S_3)^3}$$ For $C = \\text{USD } 40$ and $M = \\text{USD } 1{,}000$: $$P = \\frac{40}{1.03^1} + \\frac{40}{1.04^2} + \\frac{1{,}040}{1.05^3}$$ $$P = 38.8350 + 36.9822 + 898.3734 = \\text{USD } 974.1906 \\approx \\text{USD } 974.19$$",
        "distractor_analysis": {
            "B": "Incorrect due to rounding errors or discounting cash flows using an average spot rate of 4.00% ($40/1.04 + 40/1.04^2 + 1040/1.04^3 = 1000$).",
            "C": "Incorrect because USD 1,000.00 assumes the yield equals the 4.00% coupon rate across all periods, ignoring the upward sloping spot curve."
        }
    },
    {
        "id": "L1-FI-037",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Introduction to Fixed-Income Valuation",
        "los": "Calculate and interpret forward rates from spot rates",
        "question": "Given 1-year spot rate $S_1 = 3.00\\%$ and 2-year spot rate $S_2 = 4.50\\%$, the 1-year implied forward rate one year from now, $f_{1,1}$ (or 1y1y), is closest to:",
        "options": {
            "A": "5.25%.",
            "B": "6.02%.",
            "C": "6.75%."
        },
        "answer": "B",
        "explanation": "The relationship between spot rates and forward rates is governed by the no-arbitrage condition: $$(1 + S_2)^2 = (1 + S_1)^1 \\times (1 + f_{1,1})^1$$ Substituting the given spot rates: $$(1.045)^2 = (1.03) \\times (1 + f_{1,1})$$ $$1.092025 = 1.03 \\times (1 + f_{1,1})$$ $$1 + f_{1,1} = \\frac{1.092025}{1.03} = 1.060218$$ $$f_{1,1} = 6.0218\\% \\approx 6.02\\%$$",
        "distractor_analysis": {
            "A": "Incorrect because 5.25% incorrectly takes $(2 \\times 4.50\\% - 3.00\\%) / 1.5$ or simple linear subtraction without compounding.",
            "C": "Incorrect because 6.75% incorrectly computes $2 \\times S_2 - S_1 / 2$ or similar linear approximation error."
        }
    },
    {
        "id": "L1-FI-038",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Introduction to Fixed-Income Valuation",
        "los": "Calculate and interpret forward rates from spot rates",
        "question": "A 2-year annual coupon bond pays a 5.00% coupon on a USD 1,000 par value. The current 1-year spot rate is $f_{0,1} = S_1 = 3.00\\%$, and the 1-year forward rate starting in Year 1 is $f_{1,1} = 5.00\\%$. The value of the bond using forward rates is closest to:",
        "options": {
            "A": "USD 990.48.",
            "B": "USD 1,019.42.",
            "C": "USD 1,038.83."
        },
        "answer": "B",
        "explanation": "A bond can be valued by discounting each cash flow by the product of forward rates: $$P = \\frac{C}{1 + f_{0,1}} + \\frac{C + M}{(1 + f_{0,1})(1 + f_{1,1})}$$ Here $C = \\text{USD } 50$ and $M = \\text{USD } 1{,}000$: $$P = \\frac{50}{1.03} + \\frac{1{,}050}{(1.03)(1.05)}$$ $$P = 48.5437 + \\frac{1{,}050}{1.0815} = 48.5437 + 970.8738 = \\text{USD } 1{,}019.42$$ Thus, the value is closest to USD 1,019.42.",
        "distractor_analysis": {
            "A": "Incorrect because USD 990.48 discounts both periods at a higher rate (e.g., 5.50%).",
            "C": "Incorrect because USD 1,038.83 double counts the benefit of lower early forward rates."
        }
    },
    {
        "id": "L1-FI-039",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Introduction to Fixed-Income Valuation",
        "los": "Calculate and interpret yield spread measures",
        "question": "A 5-year corporate bond yields 5.75%. The yield on a 5-year benchmark government bond is 4.15%, and the 5-year swap rate is 4.35%. The corporate bond's G-spread and I-spread are closest to:",
        "options": {
            "A": "G-spread = 140 bps; I-spread = 160 bps.",
            "B": "G-spread = 160 bps; I-spread = 140 bps.",
            "C": "G-spread = 160 bps; I-spread = 20 bps."
        },
        "answer": "B",
        "explanation": "The G-spread is the yield spread over an interpolated government benchmark bond: $$\\text{G-spread} = \\text{Corporate Yield} - \\text{Government Yield} = 5.75\\% - 4.15\\% = 1.60\\% = 160 \\text{ bps}$$ The I-spread (interpolated spread) is the yield spread over the benchmark swap rate (such as the Euribor or SOFR interest rate swap curve): $$\\text{I-spread} = \\text{Corporate Yield} - \\text{Swap Rate} = 5.75\\% - 4.35\\% = 1.40\\% = 140 \\text{ bps}$$",
        "distractor_analysis": {
            "A": "Incorrect because it transposes the definitions of G-spread and I-spread.",
            "C": "Incorrect because 20 bps is the swap spread (Swap Rate - Government Yield = $4.35\\% - 4.15\\% = 0.20\\%$), not the corporate bond's I-spread."
        }
    },
    {
        "id": "L1-FI-040",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Introduction to Fixed-Income Valuation",
        "los": "Calculate and interpret yield spread measures",
        "question": "The zero-volatility spread (Z-spread) of a bond is best defined as the constant basis point spread that must be added to:",
        "options": {
            "A": "The benchmark government bond's yield-to-maturity to match the bond's market price.",
            "B": "Each zero-coupon spot rate along the benchmark yield curve to equate the present value of the bond's cash flows to its market price.",
            "C": "The bond's coupon rate to equate its current yield to its yield-to-maturity."
        },
        "answer": "B",
        "explanation": "The Z-spread (zero-volatility spread) is the single, constant credit/liquidity spread added to each spot rate along the entire default-free zero-coupon yield curve such that the discounted cash flows of the bond equal its current market price: $$P = \\sum_{t=1}^{n} \\frac{C_t}{(1 + S_t + Z)^t} + \\frac{M}{(1 + S_n + Z)^n}$$ It assumes zero interest rate volatility (i.e., that the spot curve is non-stochastic).",
        "distractor_analysis": {
            "A": "Incorrect because adding a spread to a single sovereign YTM defines the nominal G-spread, not the Z-spread.",
            "C": "Incorrect because adding a spread to the coupon rate does not discount future cash flows against the spot curve."
        }
    },
    {
        "id": "L1-FI-041",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Introduction to Fixed-Income Valuation",
        "los": "Calculate and interpret yield spread measures",
        "question": "A callable corporate bond has a Z-spread of 185 bps. An analyst models the embedded call option and determines the option cost is 45 bps. The bond's Option-Adjusted Spread (OAS) is closest to:",
        "options": {
            "A": "140 bps.",
            "B": "185 bps.",
            "C": "230 bps."
        },
        "answer": "A",
        "explanation": "For a callable bond, the embedded call option belongs to the issuer and disadvantages the investor, requiring extra yield compensation. Thus: $$\\text{Z-spread} = \\text{OAS} + \\text{Option Cost}$$ Solving for the Option-Adjusted Spread (OAS): $$\\text{OAS} = \\text{Z-spread} - \\text{Option Cost} = 185 \\text{ bps} - 45 \\text{ bps} = 140 \\text{ bps}$$ The OAS isolates the pure credit and liquidity spread after stripping out the option risk.",
        "distractor_analysis": {
            "B": "Incorrect because 185 bps represents the unadjusted Z-spread, which still includes the 45 bps premium for the embedded call option.",
            "C": "Incorrect because 230 bps mistakenly adds the option cost to the Z-spread ($185 + 45 = 230$), which would be the formula for a putable bond, not a callable bond."
        }
    },
    {
        "id": "L1-FI-042",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Introduction to Fixed-Income Valuation",
        "los": "Calculate and interpret yield spread measures",
        "question": "For a putable corporate bond, which relationship between the zero-volatility spread (Z-spread) and the option-adjusted spread (OAS) is most accurate?",
        "options": {
            "A": "$\\text{OAS} < \\text{Z-spread}$.",
            "B": "$\\text{OAS} = \\text{Z-spread}$.",
            "C": "$\\text{OAS} > \\text{Z-spread}$."
        },
        "answer": "C",
        "explanation": "For a putable bond, the embedded option benefits the investor. Because the investor receives downside protection from the put option, they accept a lower total yield spread (lower Z-spread). Stripping away the value of the put option reveals that the underlying credit/liquidity risk is wider than the observed Z-spread: $$\\text{Z-spread} = \\text{OAS} - \\text{Option Cost} \\implies \\text{OAS} = \\text{Z-spread} + \\text{Option Cost}$$ Since $\\text{Option Cost} > 0$, it follows that $\\text{OAS} > \\text{Z-spread}$.",
        "distractor_analysis": {
            "A": "Incorrect because $\\text{OAS} < \\text{Z-spread}$ applies to callable bonds, where the embedded option benefits the issuer.",
            "B": "Incorrect because $\\text{OAS} = \\text{Z-spread}$ holds only for straight (option-free) bonds where the option cost is zero."
        }
    },
    {
        "id": "L1-FI-043",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Introduction to Fixed-Income Valuation",
        "los": "Describe bonds with embedded options",
        "question": "A 5-year corporate bond is callable at par after 2 years. If an otherwise identical straight bond is valued at USD 104.50 and the embedded call option is valued at USD 2.25, the theoretical market value of the callable bond is closest to:",
        "options": {
            "A": "USD 102.25.",
            "B": "USD 104.50.",
            "C": "USD 106.75."
        },
        "answer": "A",
        "explanation": "Because the issuer holds the option to call back the bond, the value of the callable bond to the investor is reduced by the value of the call option: $$\\text{Price}_{\\text{callable}} = \\text{Price}_{\\text{straight}} - \\text{Value}_{\\text{call}}$$ $$\\text{Price}_{\\text{callable}} = \\text{USD } 104.50 - \\text{USD } 2.25 = \\text{USD } 102.25$$",
        "distractor_analysis": {
            "B": "Incorrect because USD 104.50 is the price of the straight bond, ignoring the value of the embedded call option.",
            "C": "Incorrect because USD 106.75 erroneously adds the call option value ($104.50 + 2.25$), which would be the valuation formula for a putable bond."
        }
    },
    {
        "id": "L1-FI-044",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Introduction to Fixed-Income Valuation",
        "los": "Describe bonds with embedded options",
        "question": "An investor holds a 7-year putable bond with a put option exercisable at par in 3 years. If the value of an otherwise identical option-free straight bond is USD 96.00 and the embedded put option is valued at USD 3.50, the theoretical market value of the putable bond is closest to:",
        "options": {
            "A": "USD 92.50.",
            "B": "USD 96.00.",
            "C": "USD 99.50."
        },
        "answer": "C",
        "explanation": "Because the embedded put option belongs to the investor, it enhances the bond's value relative to a straight bond: $$\\text{Price}_{\\text{putable}} = \\text{Price}_{\\text{straight}} + \\text{Value}_{\\text{put}}$$ $$\\text{Price}_{\\text{putable}} = \\text{USD } 96.00 + \\text{USD } 3.50 = \\text{USD } 99.50$$",
        "distractor_analysis": {
            "A": "Incorrect because USD 92.50 erroneously subtracts the put option value from the straight bond ($96.00 - 3.50 = 92.50$).",
            "B": "Incorrect because USD 96.00 ignores the value of the embedded put option."
        }
    }
]
