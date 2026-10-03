# -*- coding: utf-8 -*-
"""
Module 1: Defining Elements of Fixed Income Securities (Q01-Q14)
CFA Level 1 Fixed Income Question Bank
"""

M1_QUESTIONS = [
    {
        "id": "L1-FI-001",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Defining Elements of Fixed Income Securities",
        "los": "Describe basic features of a fixed-income security",
        "question": "A fixed-income analyst examines a corporate bond with a par value of USD 1,000, an original maturity of 10 years, and a fixed annual coupon rate of 5.50%. If 3 years have elapsed since issuance, which statement correctly identifies the bond's tenor and current coupon payment?",
        "options": {
            "A": "The tenor is 7 years and the annual coupon payment is USD 55.00.",
            "B": "The tenor is 10 years and the annual coupon payment is USD 55.00.",
            "C": "The tenor is 7 years and the annual coupon payment is USD 550.00."
        },
        "answer": "A",
        "explanation": "Tenor refers to the remaining time until the bond's maturity date. Since 3 years have elapsed on an original 10-year maturity bond, the tenor is: $$\\text{Tenor} = 10 - 3 = 7 \\text{ years}$$ The annual coupon payment is calculated as the coupon rate multiplied by par value: $$\\text{Coupon} = 5.50\\% \\times \\text{USD } 1{,}000 = \\text{USD } 55.00$$",
        "distractor_analysis": {
            "B": "Incorrect because 10 years represents the original maturity at issuance, not the remaining tenor.",
            "C": "Incorrect because USD 550.00 represents 55% of par rather than 5.50% ($0.055 \\times 1{,}000 = 55$)."
        }
    },
    {
        "id": "L1-FI-002",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Defining Elements of Fixed Income Securities",
        "los": "Describe affirmative and negative covenants and explain their purpose",
        "question": "Which of the following provisions in a bond indenture is most likely classified as an affirmative covenant?",
        "options": {
            "A": "A restriction prohibiting the issuer from exceeding a debt-to-equity ratio of 1.50.",
            "B": "A requirement to insure and maintain pledged collateral assets in good working order.",
            "C": "A limitation on dividend distributions to common shareholders during the bond's life."
        },
        "answer": "B",
        "explanation": "Affirmative covenants specify administrative actions that the borrower promises to perform during the life of the bond. Common examples include maintaining insurance on pledged assets, paying taxes on time, complying with environmental laws, and providing audited financial statements periodically. Negative covenants, by contrast, prohibit or restrict the borrower from engaging in specific actions that could impair creditworthiness, such as taking on additional debt (Option A) or paying excessive dividends (Option C).",
        "distractor_analysis": {
            "A": "Incorrect because debt incurrence restrictions and maximum leverage ceilings are classic negative covenants.",
            "C": "Incorrect because restrictions on distributions or shareholder payouts represent negative covenants designed to preserve cash."
        }
    },
    {
        "id": "L1-FI-003",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Defining Elements of Fixed Income Securities",
        "los": "Describe legal, regulatory, and tax considerations in fixed-income issuance",
        "question": "A multinational corporation incorporated in Germany issues a USD-denominated bond in London that is distributed to investors across multiple jurisdictions outside both the United States and Germany. This security is best classified as a:",
        "options": {
            "A": "Foreign bond.",
            "B": "Eurobond.",
            "C": "Domestic bond."
        },
        "answer": "B",
        "explanation": "A Eurobond is issued outside the jurisdiction of any single country and denominated in a currency other than the local currency of the country where it is issued. Here, a German issuer sells USD-denominated bonds in London to international investors, which is the definition of a Eurobond (specifically an offshore USD Eurodollar bond). Foreign bonds are issued by foreign entities in a local market in the local currency (e.g., a German firm issuing USD bonds in the US, known as a Yankee bond). Domestic bonds are issued by domestic entities in their home market and currency.",
        "distractor_analysis": {
            "A": "Incorrect because a foreign bond would be issued in the domestic market of the currency (e.g., German issuer issuing USD in the US domestic market).",
            "C": "Incorrect because domestic bonds are issued by domestic borrowers in their local currency and local exchange."
        }
    },
    {
        "id": "L1-FI-004",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Defining Elements of Fixed Income Securities",
        "los": "Describe how legal, regulatory, and tax constraints affect fixed-income securities",
        "question": "An investor purchases a 5-year, fully amortizing loan of USD 100,000 with an annual fixed interest rate of 6.00% and equal annual year-end payments. The equal annual payment is USD 23,739.64. At the end of Year 1, the remaining principal balance is closest to:",
        "options": {
            "A": "USD 76,260.36.",
            "B": "USD 82,260.36.",
            "C": "USD 94,000.00."
        },
        "answer": "B",
        "explanation": "In a fully amortizing bond or loan, each periodic payment consists of both interest and principal repayment. For Year 1: $$\\text{Interest}_1 = 6.00\\% \\times \\text{USD } 100{,}000 = \\text{USD } 6{,}000.00$$ The principal paid in Year 1 is: $$\\text{Principal}_1 = \\text{Payment} - \\text{Interest}_1 = \\text{USD } 23{,}739.64 - \\text{USD } 6{,}000.00 = \\text{USD } 17{,}739.64$$ The ending principal balance after Year 1 is: $$\\text{Balance}_1 = \\text{USD } 100{,}000 - \\text{USD } 17{,}739.64 = \\text{USD } 82{,}260.36$$",
        "distractor_analysis": {
            "A": "Incorrect because USD 76,260.36 subtracts the entire annual payment from the principal without accounting for the USD 6,000 interest component ($100{,}000 - 23{,}739.64$).",
            "C": "Incorrect because USD 94,000.00 only accounts for subtracting the interest payment ($100{,}000 - 6{,}000$)."
        }
    },
    {
        "id": "L1-FI-005",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Defining Elements of Fixed Income Securities",
        "los": "Describe basic features of a fixed-income security",
        "question": "A corporate bond indenture includes a sinking fund provision requiring the issuer to retire 5% of the original principal each year starting in Year 5. If the bonds trade at a market price of 96% of par value, the issuer is most likely to fulfill its sinking fund obligation by:",
        "options": {
            "A": "Exercising its random lottery call to redeem bonds at par value.",
            "B": "Purchasing bonds in the open market at the prevailing market price.",
            "C": "Increasing the coupon rate to incentivize voluntary bond tenders."
        },
        "answer": "B",
        "explanation": "Sinking fund arrangements often give the issuer the option to deliver either cash to the trustee (who retires bonds at par via random drawing) or bonds purchased directly in the secondary market at prevailing market prices (the delivery option). When market price is below par (trading at 96% of par), the issuer minimizes its cost by purchasing bonds in the open market at 96% of par rather than calling them at 100% of par.",
        "distractor_analysis": {
            "A": "Incorrect because redeeming bonds at par would cost 100% of par, which is more expensive than buying them in the market at 96%.",
            "C": "Incorrect because sinking funds are structured mandatory obligations; the issuer does not increase the coupon to solicit voluntary tenders."
        }
    },
    {
        "id": "L1-FI-006",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Defining Elements of Fixed Income Securities",
        "los": "Describe coupon payment structures",
        "question": "A floating-rate note (FRN) pays a quarterly coupon based on 90-day Euribor plus a quoted margin of 80 bps. The FRN has a cap of 4.50% and a floor of 2.00%. If 90-day Euribor resets at 4.00% on a coupon reset date, the annualized coupon rate for the subsequent quarter is closest to:",
        "options": {
            "A": "4.00%.",
            "B": "4.50%.",
            "C": "4.80%."
        },
        "answer": "B",
        "explanation": "The formula for the coupon rate of an FRN is: $$\\text{Coupon Rate} = \\text{Reference Rate} + \\text{Quoted Margin}$$ Without constraints: $$\\text{Uncapped Rate} = 4.00\\% + 0.80\\% = 4.80\\%$$ However, the bond features an interest rate cap of 4.50%. Because the calculated rate of 4.80% exceeds the cap, the cap is triggered, and the coupon rate for the upcoming quarter is limited to: $$\\text{Coupon Rate} = \\min(4.80\\%, 4.50\\%) = 4.50\\%$$",
        "distractor_analysis": {
            "A": "Incorrect because 4.00% ignores the quoted margin of 80 bps.",
            "C": "Incorrect because 4.80% ignores the coupon rate cap of 4.50%."
        }
    },
    {
        "id": "L1-FI-007",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Defining Elements of Fixed Income Securities",
        "los": "Describe coupon payment structures",
        "question": "A credit-linked coupon bond is structured such that its coupon rate increases by 75 bps for every notch downgrade below investment grade (BBB-/Baa3). Which of the following statements best describes this bond structure?",
        "options": {
            "A": "It provides credit protection to the issuer by reducing debt service costs during financial distress.",
            "B": "It exposes the issuer to increased debt service costs at the exact time its creditworthiness deteriorates.",
            "C": "It is identical to an inverse floating-rate note tied to benchmark interbank offer rates."
        },
        "answer": "B",
        "explanation": "A credit-linked coupon bond features a coupon that is inversely related to the issuer's credit rating. While this protects the investor against rating downgrades by offering higher yield compensation, it creates a potential liquidity strain for the issuer because debt service cash outflows increase precisely when the issuer faces financial stress and downgrades.",
        "distractor_analysis": {
            "A": "Incorrect because the coupon increases upon downgrade, which raises (not reduces) the issuer's debt service costs.",
            "C": "Incorrect because an inverse floater coupon depends on a market benchmark interest rate (e.g., $K - L \\times \\text{Reference Rate}$), not credit rating migration."
        }
    },
    {
        "id": "L1-FI-008",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Defining Elements of Fixed Income Securities",
        "los": "Describe coupon payment structures",
        "question": "An investor purchases a 3-year capital-indexed bond (such as TIPS) with an initial par value of USD 1,000 and an annual real coupon rate of 2.50%. In Year 1, the annual inflation rate is 4.00%. The inflation-adjusted coupon payment received at the end of Year 1 is closest to:",
        "options": {
            "A": "USD 25.00.",
            "B": "USD 26.00.",
            "C": "USD 65.00."
        },
        "answer": "B",
        "explanation": "In a capital-indexed bond (such as US TIPS), the coupon rate remains constant while the principal value is adjusted periodically for inflation: $$\\text{Adjusted Principal}_1 = \\text{USD } 1{,}000 \\times (1 + 0.04) = \\text{USD } 1{,}040$$ The coupon payment is calculated by multiplying the fixed real coupon rate by the adjusted principal: $$\\text{Coupon}_1 = 2.50\\% \\times \\text{USD } 1{,}040 = \\text{USD } 26.00$$",
        "distractor_analysis": {
            "A": "Incorrect because USD 25.00 is calculated on the unadjusted initial par value ($2.50\\% \\times 1{,}000$).",
            "C": "Incorrect because USD 65.00 incorrectly adds the inflation rate to the coupon rate and applies it to par ($6.50\\% \\times 1{,}000$), which is the structure of an interest-indexed bond, not a capital-indexed bond."
        }
    },
    {
        "id": "L1-FI-009",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Defining Elements of Fixed Income Securities",
        "los": "Describe bonds with embedded options",
        "question": "A corporate bond indenture includes an embedded call option allowing the issuer to redeem the bond at par after 5 years. From the perspective of the bondholder, this embedded call option:",
        "options": {
            "A": "Caps the bond's potential price appreciation when market interest rates decline.",
            "B": "Provides a floor on the bond's market price when interest rates rise.",
            "C": "Lowers the bond's required yield to maturity relative to an identical straight bond."
        },
        "answer": "A",
        "explanation": "An embedded call option gives the issuer the right, but not the obligation, to repurchase the bond at a specified call price. When interest rates fall significantly, the market price of a straight bond rises. However, the price of a callable bond is bounded near the call price because the issuer will likely call the bond and refinance at lower rates. This creates 'price compression' or capped price appreciation, exposing investors to reinvestment risk. Consequently, investors demand a higher yield (lower price) compared to an option-free bond.",
        "distractor_analysis": {
            "B": "Incorrect because a put option, not a call option, establishes a price floor when interest rates rise.",
            "C": "Incorrect because callable bonds carry higher yields (not lower yields) to compensate investors for call risk."
        }
    },
    {
        "id": "L1-FI-010",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Defining Elements of Fixed Income Securities",
        "los": "Describe bonds with embedded options",
        "question": "Which of the following bonds will most likely exhibit the lowest yield to maturity at issuance, assuming identical coupon rates, maturities, and issuer credit risk?",
        "options": {
            "A": "A putable bond.",
            "B": "A straight (option-free) bond.",
            "C": "A callable bond."
        },
        "answer": "A",
        "explanation": "A putable bond gives the investor the right to sell the bond back to the issuer at par on specified dates. Because this embedded option benefits the bondholder by providing downside price protection when interest rates rise, investors are willing to pay a higher price, resulting in a lower required yield to maturity: $$\\text{Price}_{\\text{putable}} = \\text{Price}_{\\text{straight}} + \\text{Price}_{\\text{put}}$$ $$\\text{Yield}_{\\text{putable}} < \\text{Yield}_{\\text{straight}} < \\text{Yield}_{\\text{callable}}$$ Callable bonds have the highest yield because the option benefits the issuer.",
        "distractor_analysis": {
            "B": "Incorrect because straight bonds offer higher yields than putable bonds due to the absence of the investor-friendly put option.",
            "C": "Incorrect because callable bonds have the highest yield to maturity to compensate investors for the embedded call risk."
        }
    },
    {
        "id": "L1-FI-011",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Defining Elements of Fixed Income Securities",
        "los": "Describe bonds with embedded options",
        "question": "A convertible bond has a par value of USD 1,000, a conversion price of USD 40.00 per share, and trades at a market price of USD 1,080. If the issuer's common stock currently trades at USD 42.00 per share, the conversion value and conversion premium are closest to:",
        "options": {
            "A": "Conversion value = USD 1,050; Conversion premium = USD 30.",
            "B": "Conversion value = USD 1,000; Conversion premium = USD 80.",
            "C": "Conversion value = USD 1,050; Conversion premium = USD 80."
        },
        "answer": "A",
        "explanation": "First, calculate the conversion ratio: $$\\text{Conversion Ratio} = \\frac{\\text{Par Value}}{\\text{Conversion Price}} = \\frac{\\text{USD } 1{,}000}{\\text{USD } 40.00} = 25 \\text{ shares}$$ Next, compute the conversion value: $$\\text{Conversion Value} = \\text{Conversion Ratio} \\times \\text{Stock Price} = 25 \\times \\text{USD } 42.00 = \\text{USD } 1{,}050$$ Finally, compute the market conversion premium: $$\\text{Conversion Premium} = \\text{Bond Price} - \\text{Conversion Value} = \\text{USD } 1{,}080 - \\text{USD } 1{,}050 = \\text{USD } 30$$",
        "distractor_analysis": {
            "B": "Incorrect because it compares market price to par value ($1{,}080 - 1{,}000 = 80$) instead of conversion value.",
            "C": "Incorrect because it correctly calculates conversion value but calculates premium as bond price minus par ($1{,}080 - 1{,}000 = 80$)."
        }
    },
    {
        "id": "L1-FI-012",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Defining Elements of Fixed Income Securities",
        "los": "Describe bonds with embedded options",
        "question": "Contingent convertible bonds (CoCos) differ from traditional convertible bonds primarily because CoCos:",
        "options": {
            "A": "Allow the bondholder to convert the bond to common stock at any time prior to maturity.",
            "B": "Convert into equity automatically or write down principal upon the occurrence of a pre-specified trigger event.",
            "C": "Pay a variable coupon rate tied directly to the issuer's common stock dividend payout."
        },
        "answer": "B",
        "explanation": "Contingent convertible bonds (CoCos) are hybrid capital instruments commonly issued by banks to meet regulatory Tier 1 capital requirements. Unlike traditional convertibles where the investor chooses whether and when to convert, CoCos convert into common equity automatically (or undergo an automatic principal write-down) if a pre-specified contractual event occurs, such as the bank's Common Equity Tier 1 (CET1) ratio falling below a regulatory threshold.",
        "distractor_analysis": {
            "A": "Incorrect because CoCo conversion is involuntary and triggered by capital distress, not initiated at the bondholder's discretion.",
            "C": "Incorrect because CoCos pay contractual fixed or floating coupons; they do not pay coupons tied to equity dividends."
        }
    },
    {
        "id": "L1-FI-013",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Defining Elements of Fixed Income Securities",
        "los": "Describe basic features of a fixed-income security",
        "question": "A corporate bond is issued with detachable warrants that allow the holder to buy common stock at a stated strike price. The primary financial effect of attaching warrants to the bond is to:",
        "options": {
            "A": "Lower the coupon rate the issuer must offer to sell the bond.",
            "B": "Require the bondholder to surrender the bond upon exercising the warrant.",
            "C": "Increase the effective duration of the corporate debt."
        },
        "answer": "A",
        "explanation": "Warrants are equity call options attached to a debt security as a 'sweetener'. Because the warrants provide upside equity participation and can typically be detached and traded separately, investors accept a lower coupon rate (and lower yield) on the host bond than they would require on an identical plain-vanilla straight bond. Unlike convertible bonds, exercising a warrant does not retire the bond; the bond remains outstanding.",
        "distractor_analysis": {
            "B": "Incorrect because warrants are separate instruments; exercising them requires paying cash for shares, leaving the debt outstanding.",
            "C": "Incorrect because the warrant lowers the bond's coupon yield and does not inherently increase duration."
        }
    },
    {
        "id": "L1-FI-014",
        "level": 1,
        "topic": "Fixed Income",
        "subtopic": "Defining Elements of Fixed Income Securities",
        "los": "Describe basic features of a fixed-income security",
        "question": "A bond pays annual coupon payments in Japanese yen (JPY) but will repay its principal balance at maturity in US dollars (USD). This security is best classified as a:",
        "options": {
            "A": "Currency option bond.",
            "B": "Dual-currency bond.",
            "C": "Supranational bond."
        },
        "answer": "B",
        "explanation": "A dual-currency bond makes coupon payments in one currency and principal repayment at maturity in a different currency. For example, a bond paying interest in JPY and returning principal in USD is a dual-currency bond. In contrast, a currency option bond gives the bondholder the choice to select which currency to receive payments in from two pre-agreed currencies.",
        "distractor_analysis": {
            "A": "Incorrect because currency option bonds give the investor the right to choose between two currencies for each payment, rather than fixing different currencies for coupon and principal.",
            "C": "Incorrect because supranational bonds refer to bonds issued by multilateral institutions (e.g., World Bank), which is an issuer classification rather than a currency cash flow structure."
        }
    }
]
