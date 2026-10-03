# -*- coding: utf-8 -*-
"""
Module 5: Understanding Fixed-Income Risk and Return (Q57-Q72)
CFA Level 1 Fixed Income Question Bank
"""

M5_QUESTIONS = [
    {
        "id": "L1-FI-057",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Understanding Fixed-Income Risk and Return",
        "los": "Calculate and interpret the sources of return from investing in a fixed-rate bond",
        "question": "An investor purchases a 10-year, 6.00% annual coupon bond at par value (USD 1,000) and holds it until maturity. If market interest rates immediately drop to 4.00% and stay there for the entire 10 years, the investor's realized annualized rate of return will be:",
        "options": {
            "A": "Strictly greater than 6.00%.",
            "B": "Exactly equal to 6.00%.",
            "C": "Strictly less than 6.00%."
        },
        "answer": "C",
        "explanation": "The three sources of return for a fixed-rate bond held to maturity are: (1) coupon payments, (2) the return of principal at maturity, and (3) reinvestment income from coupons. To achieve a realized compound yield equal to the initial YTM ($6.00\\%$), all coupons must be reinvested at that initial YTM. Because market rates fell to $4.00\\%$, all coupon payments are reinvested at the lower rate, resulting in lower total coupon reinvestment income. Since the bond was held to maturity, there is no capital gain to offset this reinvestment loss, so the realized return is strictly less than 6.00%.",
        "distractor_analysis": {
            "A": "Incorrect because a drop in reinvestment rates reduces total compound return, not increases it.",
            "B": "Incorrect because earning exactly 6.00% requires all coupons to be reinvested at 6.00%."
        }
    },
    {
        "id": "L1-FI-058",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Understanding Fixed-Income Risk and Return",
        "los": "Calculate and interpret Macaulay, modified, and effective duration",
        "question": "A fixed-income portfolio manager holds a bond portfolio with a Macaulay duration of 7.5 years. If the manager's target investment horizon is 5.0 years, the duration gap is:",
        "options": {
            "A": "+2.5 years, and the portfolio is dominated by market price risk.",
            "B": "-2.5 years, and the portfolio is dominated by coupon reinvestment risk.",
            "C": "+2.5 years, and the portfolio is immunized against interest rate risk."
        },
        "answer": "A",
        "explanation": "The duration gap is defined as the Macaulay duration minus the investment horizon: $$\\text{Duration Gap} = \\text{Macaulay Duration} - \\text{Investment Horizon}$$ $$\\text{Duration Gap} = 7.5 - 5.0 = +2.5 \\text{ years}$$ When the duration gap is positive (Macaulay duration exceeds horizon), the investor must sell the bonds before maturity, meaning market price risk dominates coupon reinvestment risk. If rates rise, the capital loss upon sale exceeds the higher reinvestment income.",
        "distractor_analysis": {
            "B": "Incorrect because the duration gap is positive ($+2.5$, not $-2.5$). A negative duration gap occurs when the investment horizon exceeds duration.",
            "C": "Incorrect because immunization occurs only when the duration gap is zero (Macaulay duration equals investment horizon)."
        }
    },
    {
        "id": "L1-FI-059",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Understanding Fixed-Income Risk and Return",
        "los": "Calculate and interpret Macaulay, modified, and effective duration",
        "question": "A 2-year, 5.00% annual coupon bond has a par value of USD 1,000 and trades at par (YTM = 5.00%). The Macaulay duration of the bond is closest to:",
        "options": {
            "A": "1.86 years.",
            "B": "1.95 years.",
            "C": "2.00 years."
        },
        "answer": "B",
        "explanation": "Macaulay duration is the weighted average time to receipt of cash flows, where weights are the present value of each cash flow divided by bond price: $$\\text{MacDur} = \\sum_{t=1}^n \\frac{t \\times CF_t / (1 + y)^t}{P}$$ Cash flows: Year 1 = USD 50, Year 2 = USD 1,050. At $y = 5.00\\%$, $P = \\text{USD } 1{,}000$: $$PV(CF_1) = \\frac{50}{1.05^1} = \\text{USD } 47.6190$$ $$PV(CF_2) = \\frac{1{,}050}{1.05^2} = \\text{USD } 952.3810$$ Weights: $w_1 = \\frac{47.6190}{1{,}000} = 0.047619$, $w_2 = \\frac{952.3810}{1{,}000} = 0.952381$. $$\\text{MacDur} = (1 \\times 0.047619) + (2 \\times 0.952381) = 0.047619 + 1.904762 = 1.9524 \\text{ years} \\approx 1.95 \\text{ years}$$",
        "distractor_analysis": {
            "A": "Incorrect because 1.86 years represents the modified duration: $\\text{ModDur} = 1.9524 / 1.05 = 1.8594 \\approx 1.86$ years.",
            "C": "Incorrect because 2.00 years is the maturity of the bond; Macaulay duration for a coupon-paying bond is strictly less than its maturity."
        }
    },
    {
        "id": "L1-FI-060",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Understanding Fixed-Income Risk and Return",
        "los": "Calculate and interpret Macaulay, modified, and effective duration",
        "question": "A corporate bond with a Macaulay duration of 6.30 years has an annual yield-to-maturity of 5.00%. If the market yield increases by 75 bps, the estimated percentage change in the bond's price based on modified duration is closest to:",
        "options": {
            "A": "-4.50%.",
            "B": "-4.73%.",
            "C": "+4.50%."
        },
        "answer": "A",
        "explanation": "First, calculate Modified Duration: $$\\text{ModDur} = \\frac{\\text{MacDur}}{1 + y} = \\frac{6.30}{1 + 0.05} = \\frac{6.30}{1.05} = 6.00 \\text{ years}$$ Next, estimate the percentage price change: $$\\frac{\\Delta P}{P} \\approx -\\text{ModDur} \\times \\Delta y$$ $$\\frac{\\Delta P}{P} \\approx -6.00 \\times (+0.0075) = -0.0450 = -4.50\\%$$ Because yields increased, bond prices decline.",
        "distractor_analysis": {
            "B": "Incorrect because -4.73% incorrectly uses Macaulay duration directly without dividing by $1 + y$ ($-6.30 \\times 0.0075 = -4.725\\%$).",
            "C": "Incorrect because bond price and yield are inversely related; a yield increase causes a price decline (-4.50%), not a price increase (+4.50%)."
        }
    },
    {
        "id": "L1-FI-061",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Understanding Fixed-Income Risk and Return",
        "los": "Calculate and interpret Macaulay, modified, and effective duration",
        "question": "A bond trades at a baseline price of USD 102.50. When its yield decreases by 25 bps, its price increases to USD 104.25. When its yield increases by 25 bps, its price decreases to USD 100.80. The bond's approximate modified duration is closest to:",
        "options": {
            "A": "3.37.",
            "B": "6.73.",
            "C": "13.46."
        },
        "answer": "B",
        "explanation": "The formula for approximate modified duration is: $$\\text{ApproxModDur} = \\frac{P_- - P_+}{2 \\times P_0 \\times \\Delta y}$$ Given $P_0 = 102.50$, $P_- = 104.25$, $P_+ = 100.80$, and $\\Delta y = 0.0025$: $$\\text{ApproxModDur} = \\frac{104.25 - 100.80}{2 \\times 102.50 \\times 0.0025} = \\frac{3.45}{0.5125} = 6.7317 \\approx 6.73$$",
        "distractor_analysis": {
            "A": "Incorrect because 3.37 forgets to divide by 2 in the denominator or uses $2 \\times \\Delta y$ improperly ($3.45 / 1.025 = 3.37$).",
            "C": "Incorrect because 13.46 uses $\\Delta y = 0.00125$ or multiplies by 2 rather than dividing by 2."
        }
    },
    {
        "id": "L1-FI-062",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Understanding Fixed-Income Risk and Return",
        "los": "Calculate and interpret Macaulay, modified, and effective duration",
        "question": "Why is effective duration, rather than modified duration, the appropriate measure of interest rate risk for bonds with embedded options?",
        "options": {
            "A": "Modified duration assumes that expected future cash flows do not change when interest rates change.",
            "B": "Effective duration assumes that the benchmark yield curve undergoes non-parallel twists.",
            "C": "Modified duration cannot be calculated for bonds paying semi-annual coupons."
        },
        "answer": "A",
        "explanation": "Modified duration is a yield duration measure that assumes a bond's contractual cash flows are fixed and independent of interest rate movements. For bonds with embedded options (such as callable or putable bonds), interest rate changes alter the probability of option exercise, thereby changing the timing and amount of expected cash flows. Effective duration is a curve duration measure that dynamically re-estimates cash flows across interest rate shifts, making it essential for options-bearing bonds.",
        "distractor_analysis": {
            "B": "Incorrect because effective duration assumes a parallel shift in the benchmark yield curve, not non-parallel twists.",
            "C": "Incorrect because modified duration is routinely computed for semi-annual bonds by dividing by $(1 + y/2)$."
        }
    },
    {
        "id": "L1-FI-063",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Understanding Fixed-Income Risk and Return",
        "los": "Describe key rate duration and its use",
        "question": "An institutional fixed-income portfolio manager wishing to evaluate the portfolio's sensitivity to a steepening of the yield curve should primarily examine the portfolio's:",
        "options": {
            "A": "Effective duration.",
            "B": "Key rate durations.",
            "C": "Macaulay duration."
        },
        "answer": "B",
        "explanation": "Key rate duration (or partial duration) measures a portfolio's price sensitivity to a change in the benchmark yield at a specific maturity point along the yield curve, holding all other key rates constant. While aggregate effective duration and Macaulay duration assume parallel shifts across the entire curve, key rate durations isolate 'shaping risk' (such as steepening, flattening, or twists in the yield curve).",
        "distractor_analysis": {
            "A": "Incorrect because effective duration measures price sensitivity to a parallel shift across all maturities.",
            "C": "Incorrect because Macaulay duration is a cash-flow weighted maturity measure that does not capture non-parallel yield curve reshaping."
        }
    },
    {
        "id": "L1-FI-064",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Understanding Fixed-Income Risk and Return",
        "los": "Calculate the duration of a bond portfolio and describe its limitations",
        "question": "A portfolio consists of two bonds:\n- Bond X: Market value USD 6,000,000; Modified duration = 4.0\n- Bond Y: Market value USD 4,000,000; Modified duration = 9.0\nThe weighted-average modified duration of the portfolio is closest to:",
        "options": {
            "A": "6.0.",
            "B": "6.5.",
            "C": "7.0."
        },
        "answer": "A",
        "explanation": "Total portfolio market value is: $$\\text{Total Value} = \\text{USD } 6{,}000{,}000 + \\text{USD } 4{,}000{,}000 = \\text{USD } 10{,}000{,}000$$ The portfolio weights are $w_X = 60\\%$ and $w_Y = 40\\%$. The portfolio modified duration is: $$\\text{Portfolio Duration} = w_X \\text{ModDur}_X + w_Y \\text{ModDur}_Y$$ $$\\text{Portfolio Duration} = (0.60 \\times 4.0) + (0.40 \\times 9.0) = 2.40 + 3.60 = 6.00$$ A primary limitation of this measure is that it assumes a parallel shift in yields across all portfolio holdings.",
        "distractor_analysis": {
            "B": "Incorrect because 6.5 is the simple unweighted average of the two durations ($(4 + 9)/2 = 6.5$), ignoring portfolio weights.",
            "C": "Incorrect because 7.0 reverses the portfolio weights ($0.40 \\times 4.0 + 0.60 \\times 9.0 = 1.6 + 5.4 = 7.0$)."
        }
    },
    {
        "id": "L1-FI-065",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Understanding Fixed-Income Risk and Return",
        "los": "Calculate and interpret money duration and price value of a basis point",
        "question": "A fixed-income portfolio has a market value of USD 50,000,000 and a modified duration of 5.60. The portfolio's Money Duration is closest to:",
        "options": {
            "A": "USD 28,000.",
            "B": "USD 280,000.",
            "C": "USD 280,000,000."
        },
        "answer": "C",
        "explanation": "Money duration (also known as dollar duration in the US) measures the dollar price change per unit change in yield: $$\\text{Money Duration} = \\text{Modified Duration} \\times \\text{Portfolio Market Value}$$ $$\\text{Money Duration} = 5.60 \\times \\text{USD } 50{,}000{,}000 = \\text{USD } 280{,}000{,}000$$ For a 100 bps (1%) parallel shift in yield, the portfolio value changes by approximately: $$\\Delta PV \\approx -\\text{Money Duration} \\times \\Delta y = -\\text{USD } 280{,}000{,}000 \\times 0.01 = -\\text{USD } 2{,}800{,}000$$",
        "distractor_analysis": {
            "A": "Incorrect because USD 28,000 represents the price value of a basis point (PVBP), not the money duration ($280{,}000{,}000 \\times 0.0001 = 28{,}000$).",
            "B": "Incorrect due to a factor of 1,000 magnitude calculation error."
        }
    },
    {
        "id": "L1-FI-066",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Understanding Fixed-Income Risk and Return",
        "los": "Calculate and interpret money duration and price value of a basis point",
        "question": "A bond trading at USD 100 has a modified duration of 7.20. Its Price Value of a Basis Point (PVBP, or DV01) per USD 1,000,000 of par value is closest to:",
        "options": {
            "A": "USD 72.00.",
            "B": "USD 720.00.",
            "C": "USD 7,200.00."
        },
        "answer": "B",
        "explanation": "PVBP measures the absolute change in the price of a bond for a 1 basis point (0.01% = 0.0001) change in yield: $$\\text{PVBP} = \\text{Modified Duration} \\times \\text{Portfolio Value} \\times 0.0001$$ For a position value of USD 1,000,000: $$\\text{PVBP} = 7.20 \\times \\text{USD } 1{,}000{,}000 \\times 0.0001 = \\text{USD } 720.00$$",
        "distractor_analysis": {
            "A": "Incorrect because USD 72.00 corresponds to a position value of USD 100,000 rather than USD 1,000,000.",
            "C": "Incorrect because USD 7,200.00 corresponds to a 10 basis point change rather than a 1 basis point change."
        }
    },
    {
        "id": "L1-FI-067",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Understanding Fixed-Income Risk and Return",
        "los": "Calculate and interpret convexity",
        "question": "A bond has a modified duration of 8.00 and an annual convexity of 80.0. If the bond's yield-to-maturity increases by 150 bps (+0.0150), the estimated percentage change in the bond's price incorporating both duration and convexity is closest to:",
        "options": {
            "A": "-12.00%.",
            "B": "-11.10%.",
            "C": "-10.20%."
        },
        "answer": "B",
        "explanation": "The full Taylor series approximation for percentage price change including convexity is: $$\\frac{\\Delta P}{P} \\approx -\\text{ModDur} \\times \\Delta y + \\frac{1}{2} \\times \\text{Convexity} \\times (\\Delta y)^2$$ 1. Duration effect: $$-8.00 \\times (+0.0150) = -0.1200 = -12.00\\%$$ 2. Convexity adjustment: $$\\frac{1}{2} \\times 80.0 \\times (0.0150)^2 = 40.0 \\times 0.000225 = +0.0090 = +0.90\\%$$ 3. Combined price change: $$\\frac{\\Delta P}{P} \\approx -12.00\\% + 0.90\\% = -11.10\\%$$ Convexity always exerts a positive adjustment to price estimates for straight bonds.",
        "distractor_analysis": {
            "A": "Incorrect because -12.00% reflects the duration effect alone, omitting the positive convexity correction.",
            "C": "Incorrect because -10.20% mistakenly omits the 1/2 factor in the convexity term, adding $1.80\\%$ instead of $0.90\\%$ ($-12.00\\% + 1.80\\% = -10.20\\%$)."
        }
    },
    {
        "id": "L1-FI-068",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Understanding Fixed-Income Risk and Return",
        "los": "Calculate and interpret convexity",
        "question": "A bond's price is USD 100.00 at baseline. If yields decrease by 20 bps ($\\Delta y = 0.0020$), its price rises to USD 101.55. If yields increase by 20 bps, its price falls to USD 98.51. The bond's approximate convexity is closest to:",
        "options": {
            "A": "76.0.",
            "B": "150.0.",
            "C": "300.0."
        },
        "answer": "B",
        "explanation": "Approximate convexity is calculated using the formula: $$\\text{ApproxConvexity} = \\frac{P_- + P_+ - 2P_0}{P_0 \\times (\\Delta y)^2}$$ Given $P_0 = 100.00$, $P_- = 101.55$, $P_+ = 98.51$, and $\\Delta y = 0.0020$: $$\\text{Numerator} = 101.55 + 98.51 - 2(100.00) = 200.06 - 200.00 = 0.06$$ $$\\text{Denominator} = 100.00 \\times (0.0020)^2 = 100.00 \\times 0.000004 = 0.0004$$ $$\\text{ApproxConvexity} = \\frac{0.06}{0.0004} = 150.0$$",
        "distractor_analysis": {
            "A": "Incorrect because 76.0 divides by 2 in the formula incorrectly ($150 / 2 = 75$).",
            "C": "Incorrect because 300.0 multiplies the convexity by 2 or uses $\\Delta y = 0.0040$ erroneously."
        }
    },
    {
        "id": "L1-FI-069",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Understanding Fixed-Income Risk and Return",
        "los": "Calculate and interpret convexity",
        "question": "When market yields fall to levels below the coupon rate of a callable bond, the bond is most likely to exhibit:",
        "options": {
            "A": "Negative convexity.",
            "B": "Increased effective duration.",
            "C": "Zero convexity."
        },
        "answer": "A",
        "explanation": "For a callable bond at low yield levels, the price is compressed by the call price ceiling because the issuer is highly likely to exercise the call option. As yields fall, the price increases at a decreasing rate, and price appreciation is capped. On a price-yield graph, the curve bends concave downward, which is the definition of negative convexity. In this region, effective duration also drops sharply because the expected life contracts to the call date.",
        "distractor_analysis": {
            "B": "Incorrect because effective duration drops substantially (contracts toward the call date) as yields decline, rather than increasing.",
            "C": "Incorrect because convexity becomes distinctly negative, not zero."
        }
    },
    {
        "id": "L1-FI-070",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Understanding Fixed-Income Risk and Return",
        "los": "Calculate and interpret convexity",
        "question": "The positive convexity property of an option-free bond implies that for an equal-sized upward and downward parallel shift in yield:",
        "options": {
            "A": "The price decrease when yields rise is greater in magnitude than the price increase when yields fall.",
            "B": "The price increase when yields fall is greater in magnitude than the price decrease when yields rise.",
            "C": "The price changes are symmetric and equal in magnitude."
        },
        "answer": "B",
        "explanation": "The price-yield relationship for an option-free bond is convex to the origin. This positive curvature ensures that as yields fall, bond prices accelerate upward (at an increasing rate), whereas when yields rise, bond prices decline at a decreasing rate. Therefore, for equal changes in yield ($+\\Delta y$ and $-\\Delta y$), the percentage price increase from a yield drop exceeds the percentage price decrease from a yield rise.",
        "distractor_analysis": {
            "A": "Incorrect because this describes negative convexity, where downside price declines exceed upside appreciation.",
            "C": "Incorrect because a linear symmetric relationship holds only under pure first-order duration approximations, ignoring convexity."
        }
    },
    {
        "id": "L1-FI-071",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Understanding Fixed-Income Risk and Return",
        "los": "Calculate and interpret convexity",
        "question": "As market yields rise toward and beyond the put strike yield for a putable bond, the bond's price sensitivity (effective duration):",
        "options": {
            "A": "Increases significantly toward that of a zero-coupon bond.",
            "B": "Decreases as the put option establishes a floor on the bond's price.",
            "C": "Becomes negative, causing bond prices to rise as yields rise."
        },
        "answer": "B",
        "explanation": "A put option gives the investor the right to sell the bond back at par. As market interest rates rise, the value of this put option increases, creating an effective price floor near the put strike price. Because the bond's price cannot fall substantially below the put price, its price sensitivity to further yield increases diminishes sharply. Consequently, effective duration decreases and convexity remains strongly positive.",
        "distractor_analysis": {
            "A": "Incorrect because duration shortens toward the put date, rather than lengthening toward a zero-coupon bond.",
            "C": "Incorrect because duration remains positive; fixed-income bonds do not exhibit negative duration merely from put features."
        }
    },
    {
        "id": "L1-FI-072",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Understanding Fixed-Income Risk and Return",
        "los": "Describe how credit spread and liquidity affect duration and convexity",
        "question": "An analyst observes that high-yield corporate bonds often exhibit an 'empirical duration' that is materially lower than their analytical (modified) duration. The most likely explanation is that:",
        "options": {
            "A": "High-yield bonds have zero exposure to benchmark government interest rate shifts.",
            "B": "Credit spreads typically widen during economic expansions when benchmark interest rates are rising.",
            "C": "Credit spreads often narrow during economic expansions when benchmark interest rates are rising, muting total yield increases."
        },
        "answer": "C",
        "explanation": "Empirical duration measures interest rate sensitivity using historical regressions of actual bond price changes against benchmark yield changes. In economic expansions, benchmark interest rates typically rise as monetary policy tightens, but corporate default risk declines, causing credit spreads to narrow. Because the narrowing credit spread partially offsets the rising benchmark rate, the total yield on high-yield bonds increases by less than the benchmark rate, resulting in observed price declines that are smaller than analytical duration predicts (i.e., lower empirical duration).",
        "distractor_analysis": {
            "A": "Incorrect because high-yield bonds are still fixed-income instruments exposed to interest rate risk.",
            "B": "Incorrect because credit spreads contract (narrow) during economic expansions due to improving corporate earnings and lower default rates."
        }
    }
]
