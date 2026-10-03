"""
Script: gen_l1_eq.py
Purpose: Generate 85 CFA Level 1 Equity Investments exam questions across 6 core modules.
Output: data/fi_eq/l1_equity.json
Compliance: KaTeX delimiters strictly reserved for math ($...$ or $$...$$), currency formatted as 'USD'.
"""

import json
import os
import re

questions = [
    # =========================================================================
    # MODULE 1: MARKET ORGANIZATION AND STRUCTURE (Q01 - Q14)
    # =========================================================================
    {
        "id": "L1-EQ-001",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Functions of the Financial System",
        "los": "Explain the main functions of the financial system.",
        "question": "Which of the following is most accurately described as a core economic function of a well-functioning financial system?",
        "options": {
            "A": "Facilitating price discovery and determining the equilibrium rate of return that balances aggregate savings and investment.",
            "B": "Guaranteeing that market participants achieve positive real risk-adjusted rates of return across all investment horizons.",
            "C": "Completely eliminating asymmetric information and agency conflicts between corporate managers and capital providers."
        },
        "answer": "A",
        "explanation": "A well-functioning financial system fulfills three primary economic functions: (1) enabling entities to save, borrow, raise equity capital, manage financial risks, and exchange assets; (2) determining the equilibrium interest rates and asset prices that balance aggregate saving with capital investment (price discovery); and (3) allocating capital to its highest-value productive uses across the economy.",
        "distractor_analysis": {
            "B": "The financial system allocates capital and facilitates risk transfer, but it cannot eliminate market risk or guarantee positive investment returns.",
            "C": "Intermediaries and disclosure regulations mitigate informational frictions, but financial markets cannot completely eliminate asymmetric information or agency conflicts."
        }
    },
    {
        "id": "L1-EQ-002",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Financial Intermediaries",
        "los": "Describe the roles of financial intermediaries.",
        "question": "An intermediary that commits its own capital, maintains an inventory of securities, and provides liquidity by standing ready to buy at the bid and sell at the ask operates as a:",
        "options": {
            "A": "Broker.",
            "B": "Dealer.",
            "C": "Securitizer."
        },
        "answer": "B",
        "explanation": "A dealer (or market maker) acts as a principal by trading for its own account and inventory, bearing inventory risk, and earning the bid-ask spread: $\\text{Spread} = P_{\\text{ask}} - P_{\\text{bid}}$. Brokers act strictly as agents executing trades on behalf of clients without maintaining inventory. Securitizers package debt obligations into tradable pools.",
        "distractor_analysis": {
            "A": "Brokers act as agents facilitating transactions between buyers and sellers, earning commissions without taking principal inventory risk.",
            "C": "Securitizers pool individual loans (such as mortgages or auto loans) to issue asset-backed securities; they do not quote continuous two-sided dealer markets."
        }
    },
    {
        "id": "L1-EQ-003",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Positions and Leverage",
        "los": "Calculate and interpret the leverage ratio and the return on a margin transaction.",
        "question": "An investor purchases 200 shares of stock at 50 USD per share on an initial margin of 40%. The broker charges a call loan interest rate of 5% per annum on borrowed funds. One year later, the company pays a dividend of 2.00 USD per share and the investor sells the shares for 59 USD per share. The investor's return on initial equity is closest to:",
        "options": {
            "A": "38.0%.",
            "B": "42.5%.",
            "C": "47.5%."
        },
        "answer": "C",
        "explanation": "Total purchase value: $V_0 = 200 \\times 50\\text{ USD} = 10{,}000\\text{ USD}$.\nInitial equity invested: $\\text{Equity}_0 = 10{,}000\\text{ USD} \\times 0.40 = 4{,}000\\text{ USD}$.\nBorrowed margin loan: $\\text{Loan}_0 = 10{,}000\\text{ USD} \\times 0.60 = 6{,}000\\text{ USD}$.\nCapital gain: $\\text{Gain} = 200 \\times (59 - 50) = 1{,}800\\text{ USD}$.\nTotal dividends received: $\\text{Dividends} = 200 \\times 2.00\\text{ USD} = 400\\text{ USD}$.\nMargin loan interest expense: $\\text{Interest} = 6{,}000\\text{ USD} \\times 0.05 = 300\\text{ USD}$.\nNet profit: $\\text{Net Profit} = 1{,}800 + 400 - 300 = 1{,}900\\text{ USD}$.\nReturn on equity (ROE): $$\\text{ROE} = \\frac{1{,}900\\text{ USD}}{4{,}000\\text{ USD}} = 47.5\\%$$",
        "distractor_analysis": {
            "A": "38.0% erroneously omits the dividend income or computes $(1{,}800 - 300) / 4{,}000 = 37.5\\% \\approx 38.0\\%$.",
            "B": "42.5% computes $(1{,}800 + 400 - 500) / 4{,}000$ or miscalculates loan interest as 500 USD instead of 300 USD."
        }
    },
    {
        "id": "L1-EQ-004",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Margin Call Calculations",
        "los": "Calculate and interpret the margin call price.",
        "question": "An investor buys 500 shares of stock at 60 USD per share on an initial margin requirement of 50%. The broker requires a maintenance margin of 30%. The share price below which the investor will receive a margin call is closest to:",
        "options": {
            "A": "37.50 USD.",
            "B": "42.86 USD.",
            "C": "48.00 USD."
        },
        "answer": "B",
        "explanation": "The margin call price $P$ for a long position is calculated using: $$P = P_0 \\times \\frac{1 - \\text{Initial Margin}}{1 - \\text{Maintenance Margin}}$$ Substituting the parameters: $$P = 60\\text{ USD} \\times \\frac{1 - 0.50}{1 - 0.30} = 60 \\times \\frac{0.50}{0.70} \\approx 42.86\\text{ USD}$$ At 42.86 USD, equity per share is $\\text{Equity} = 42.86 - 30.00 = 12.86\\text{ USD}$, which equals exactly 30% of 42.86 USD.",
        "distractor_analysis": {
            "A": "37.50 USD is calculated using an incorrect maintenance margin of 20% in the denominator: $P = 60\\text{ USD} \\times \\frac{0.50}{0.80} = 37.50\\text{ USD}$.",
            "C": "48.00 USD subtracts the 20% margin spread directly from the purchase price: $P = 60\\text{ USD} \\times (1 - 0.20) = 48.00\\text{ USD}$."
        }
    },
    {
        "id": "L1-EQ-005",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Short Positions",
        "los": "Describe the characteristics of short positions and calculate short sale returns.",
        "question": "An investor sells short 100 shares of a stock at 80 USD per share with an initial margin requirement of 50%. Over the holding period, the company distributes a cash dividend of 2.00 USD per share. The investor covers the short position at 70 USD per share. Ignoring interest and commissions, the investor's return on initial equity is closest to:",
        "options": {
            "A": "10.0%.",
            "B": "20.0%.",
            "C": "25.0%."
        },
        "answer": "B",
        "explanation": "Initial equity requirement: $\\text{Equity}_0 = 100 \\times 80\\text{ USD} \\times 0.50 = 4{,}000\\text{ USD}$.\nCapital gain on short position: $\\text{Gain} = (80 - 70) \\times 100 = 1{,}000\\text{ USD}$.\nDividend obligation paid to lender: $\\text{Dividend} = 100 \\times 2.00\\text{ USD} = 200\\text{ USD}$.\nNet profit: $\\text{Net Profit} = 1{,}000 - 200 = 800\\text{ USD}$.\nReturn on equity: $$\\text{Return} = \\frac{800\\text{ USD}}{4{,}000\\text{ USD}} = 20.0\\%$$",
        "distractor_analysis": {
            "A": "10.0% is the unleveraged return on total short transaction value: $\\frac{800\\text{ USD}}{8{,}000\\text{ USD}} = 10.0\\%$.",
            "C": "25.0% ignores the required dividend payment to the securities lender: $\\frac{1{,}000\\text{ USD}}{4{,}000\\text{ USD}} = 25.0\\%$."
        }
    },
    {
        "id": "L1-EQ-006",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Order Types and Execution Instructions",
        "los": "Compare market orders with limit orders.",
        "question": "A portfolio manager who prioritizes speed and certainty of trade execution over price certainty should most appropriately place a:",
        "options": {
            "A": "Market order.",
            "B": "Limit order.",
            "C": "Stop-loss order."
        },
        "answer": "A",
        "explanation": "A market order instructs the executing broker to execute immediately at the best available prevailing prices in the market. It guarantees immediate execution but exposes the buyer/seller to price uncertainty and potential market impact/slippage. Limit orders specify price limits but carry execution risk.",
        "distractor_analysis": {
            "B": "A limit order guarantees price certainty (at or better than the limit price) but sacrifices execution certainty because it may not execute if the market moves away.",
            "C": "A stop-loss order remains inactive until a specified stop price is triggered, converting into an order to trade; it does not guarantee immediate execution upon submission."
        }
    },
    {
        "id": "L1-EQ-007",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Order Validity Instructions",
        "los": "Explain execution, validity, and clearing instructions.",
        "question": "An order instruction directing that an order must be executed immediately in its entirety or cancelled completely without partial execution is a(n):",
        "options": {
            "A": "Immediate-or-Cancel (IOC) order.",
            "B": "Fill-or-Kill (FOK) order.",
            "C": "Good-till-Cancelled (GTC) order."
        },
        "answer": "B",
        "explanation": "A Fill-or-Kill (FOK) order combines an immediate execution requirement with an all-or-none quantity constraint: the order must be filled in its entirety immediately, or it is cancelled in full. An Immediate-or-Cancel (IOC) order allows partial fills immediately and cancels only the unfilled balance.",
        "distractor_analysis": {
            "A": "An IOC order permits partial execution immediately; any remaining unexecuted shares are cancelled, unlike FOK which forbids partial fills.",
            "C": "A GTC order specifies time validity (the order remains active indefinitely until executed or manually revoked) and has no immediate fill constraint."
        }
    },
    {
        "id": "L1-EQ-008",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Stop Orders",
        "los": "Contrast market orders, limit orders, and stop orders.",
        "question": "An investor holding a long equity position currently priced at 75 USD wishes to protect against severe downside losses. The investor should most appropriately place a:",
        "options": {
            "A": "Stop-sell order with a stop price below 75 USD.",
            "B": "Limit-sell order with a limit price below 75 USD.",
            "C": "Stop-buy order with a stop price above 75 USD."
        },
        "answer": "A",
        "explanation": "A stop-sell (or stop-loss sell) order is placed below the current market price (e.g., at 70 USD). If market prices drop to or below the stop price, the order becomes an active market order to sell, protecting the investor against deeper losses.",
        "distractor_analysis": {
            "B": "A limit-sell order placed below 75 USD would execute immediately at the current market price (75 USD), since 75 USD is higher than the minimum acceptable selling price.",
            "C": "A stop-buy order is placed above the current market price to protect short positions or buy on an upside technical breakout."
        }
    },
    {
        "id": "L1-EQ-009",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Primary vs. Secondary Markets",
        "los": "Describe primary and secondary markets and how securities are offered in each.",
        "question": "In an initial public offering (IPO), an investment bank acting under a best-efforts offering commitment:",
        "options": {
            "A": "Purchases the entire offering from the issuer as a principal, bearing inventory and price risk.",
            "B": "Acts strictly as an agent, agreeing to sell as many shares as possible without guaranteeing capital proceeds.",
            "C": "Guarantees the corporate issuer a minimum fixed total dollar amount of proceeds."
        },
        "answer": "B",
        "explanation": "In a best-efforts offering, the investment bank acts strictly as an agent and does not buy the issue or guarantee proceeds. The bank commits to using its best efforts to place the securities, but any unsold shares remain with the issuing company. In an underwritten (firm commitment) offering, the bank acts as principal and absorbs inventory risk.",
        "distractor_analysis": {
            "A": "Purchasing the full issue and bearing inventory risk describes an underwritten (firm commitment) offering.",
            "C": "Guaranteeing fixed minimum proceeds to the issuing firm is characteristic of firm-commitment underwriting, not best-efforts placement."
        }
    },
    {
        "id": "L1-EQ-010",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Market Structures",
        "los": "Explain the characteristics of quote-driven, order-driven, and brokered markets.",
        "question": "A trading venue where submitted orders are batched together over a specific time window and executed simultaneously at a single market-clearing price is classified as a:",
        "options": {
            "A": "Continuous order-driven market.",
            "B": "Call market.",
            "C": "Brokered market."
        },
        "answer": "B",
        "explanation": "In a call market, orders accumulate over a designated interval and clear at discrete points in time at a single equilibrium price that maximizes executable volume. This structure is frequently used for market open/close auctions. Continuous markets execute trades dynamically as orders arrive.",
        "distractor_analysis": {
            "A": "A continuous order-driven market matches buyers and sellers continuously throughout the trading session at varying bid and ask prices.",
            "C": "A brokered market relies on human brokers who locate counterparties for custom, illiquid, or block assets (e.g., real estate or large private placements)."
        }
    },
    {
        "id": "L1-EQ-011",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Market Quality",
        "los": "Explain the characteristics of a well-functioning financial system.",
        "question": "A financial market characterized by low transaction costs, tight bid-ask spreads, and minimal market impact for large trades exhibits high:",
        "options": {
            "A": "Operational efficiency.",
            "B": "Informational efficiency.",
            "C": "Allocational efficiency."
        },
        "answer": "A",
        "explanation": "Operational efficiency (internal efficiency) means that transaction costs—such as commissions, bid-ask spreads, clearing fees, and market impact costs—are low. Informational efficiency (external efficiency) means market prices rapidly reflect all available fundamental information. Allocational efficiency occurs when capital flows to its most productive uses.",
        "distractor_analysis": {
            "B": "Informational efficiency describes how rapidly and completely prices incorporate economic information, not the magnitude of trading commissions or bid-ask spreads.",
            "C": "Allocational efficiency measures the societal distribution of capital to highest-return productive enterprises."
        }
    },
    {
        "id": "L1-EQ-012",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Margin Call Calculations",
        "los": "Calculate and interpret the margin call price.",
        "question": "An investor purchases 1,000 shares of stock at 80 USD per share on an initial margin of 50%. The maintenance margin requirement is 30%. At what share price will the broker issue a margin call?",
        "options": {
            "A": "48.00 USD.",
            "B": "53.33 USD.",
            "C": "57.14 USD."
        },
        "answer": "C",
        "explanation": "Applying the margin call price formula: $$P = P_0 \\times \\frac{1 - \\text{Initial Margin}}{1 - \\text{Maintenance Margin}} = 80\\text{ USD} \\times \\frac{1 - 0.50}{1 - 0.30} = 80 \\times \\frac{0.50}{0.70} \\approx 57.14\\text{ USD}$$ Verification: At 57.14 USD, equity per share is $\\text{Equity} = 57.14 - 40.00 = 17.14\\text{ USD}$. The margin percentage is $\\frac{17.14}{57.14} = 30.0\\%$, reaching the maintenance threshold.",
        "distractor_analysis": {
            "A": "48.00 USD results from multiplying the purchase price by $(1 - 0.40) = 48.00\\text{ USD}$.",
            "B": "53.33 USD results from applying a 25% maintenance margin requirement: $P = 80\\text{ USD} \\times \\frac{0.50}{0.75} = 53.33\\text{ USD}$."
        }
    },
    {
        "id": "L1-EQ-013",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Short Sale Margin Call Price",
        "los": "Calculate and interpret the margin call price for a short position.",
        "question": "An investor sells short 400 shares of stock at 50 USD per share. The initial margin requirement is 50%, and the maintenance margin requirement is 30%. The share price at or above which the investor will receive a margin call is closest to:",
        "options": {
            "A": "57.69 USD.",
            "B": "62.50 USD.",
            "C": "65.00 USD."
        },
        "answer": "A",
        "explanation": "For a short position, margin calls occur when the stock price rises. The margin call price $P$ is: $$P = P_0 \\times \\frac{1 + \\text{Initial Margin}}{1 + \\text{Maintenance Margin}} = 50\\text{ USD} \\times \\frac{1 + 0.50}{1 + 0.30} = 50 \\times \\frac{1.50}{1.30} \\approx 57.69\\text{ USD}$$ Verification: Total assets per share = $\\text{Assets} = 50 \\times 1.50 = 75.00\\text{ USD}$. At $P = 57.69\\text{ USD}$, equity per share is $\\text{Equity} = 75.00 - 57.69 = 17.31\\text{ USD}$. The margin ratio is $\\frac{17.31}{57.69} = 30.0\\%$.",
        "distractor_analysis": {
            "B": "62.50 USD is calculated using $P = 50\\text{ USD} \\times \\frac{1.50}{1.20} = 62.50\\text{ USD}$ (assuming a 20% maintenance margin).",
            "C": "65.00 USD simply adds $P = 50 \\times 1.30 = 65.00\\text{ USD}$ or uses an incorrect margin adjustment."
        }
    },
    {
        "id": "L1-EQ-014",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Market Microstructure and Transparency",
        "los": "Describe the characteristics of dark pools and iceberg orders.",
        "question": "An institutional trader wishing to execute a large block of shares without displaying the entire order quantity to public market feeds to avoid front-running should place a(n):",
        "options": {
            "A": "Iceberg order.",
            "B": "Day order.",
            "C": "Stop-limit order."
        },
        "answer": "A",
        "explanation": "An iceberg (or hidden) order displays only a small fraction of the total order size in the public order book at any given time. As displayed tranches are executed, additional tranches from the hidden reserve are released, allowing institutional traders to minimize market impact.",
        "distractor_analysis": {
            "B": "A day order is a validity instruction stating that the order will expire at the close of trading, but it does not conceal order quantity.",
            "C": "A stop-limit order specifies trigger and execution boundary prices, but is fully visible to the market once activated."
        }
    },

    # =========================================================================
    # MODULE 2: SECURITY MARKET INDICES (Q15 - Q28)
    # =========================================================================
    {
        "id": "L1-EQ-015",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Index Construction and Weighting",
        "los": "Calculate and interpret the value, price return, and total return of an index.",
        "question": "A price-weighted index consists of three stocks: Stock X priced at 20 USD, Stock Y priced at 50 USD, and Stock Z priced at 110 USD. If the initial index divisor is 3.0, the index value is closest to:",
        "options": {
            "A": "60.0.",
            "B": "90.0.",
            "C": "180.0."
        },
        "answer": "A",
        "explanation": "The value of a price-weighted index is calculated by summing constituent prices and dividing by the divisor: $$\\text{Index Value} = \\frac{\\sum P_i}{D} = \\frac{20\\text{ USD} + 50\\text{ USD} + 110\\text{ USD}}{3.0} = \\frac{180\\text{ USD}}{3.0} = 60.0$$",
        "distractor_analysis": {
            "B": "90.0 divides by 2.0 instead of the given divisor of 3.0.",
            "C": "180.0 is the unadjusted sum of the three constituent share prices without dividing by the divisor."
        }
    },
    {
        "id": "L1-EQ-016",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Divisor Adjustments",
        "los": "Explain the effect of stock splits on price-weighted indices.",
        "question": "A price-weighted index includes Stock A at 30 USD, Stock B at 60 USD, and Stock C at 90 USD with a divisor of 3.0 (index value = 60.0). If Stock C executes a 2-for-1 stock split, causing its price to adjust to 45 USD while stocks A and B remain unchanged, the new divisor needed to prevent index distortion is closest to:",
        "options": {
            "A": "2.25.",
            "B": "2.50.",
            "C": "2.75."
        },
        "answer": "A",
        "explanation": "Prior to the split, the sum of prices was $\\sum P = 30 + 60 + 90 = 180\\text{ USD}$, and index value was $\\text{Index Value} = 180 / 3.0 = 60.0$. Following the 2-for-1 split of Stock C, the new sum of prices is $\\sum P_{\\text{new}} = 30 + 60 + 45 = 135\\text{ USD}$. To maintain index continuity at 60.0: $$D_{\\text{new}} = \\frac{\\sum P_{\\text{new}}}{\\text{Index Value}} = \\frac{135\\text{ USD}}{60.0} = 2.25$$",
        "distractor_analysis": {
            "B": "2.50 erroneously averages the divisor adjustment or uses an incorrect split factor.",
            "C": "2.75 computes $D = 3.0 - (45 / 180) = 2.75$, which is an algebraically incorrect divisor adjustment."
        }
    },
    {
        "id": "L1-EQ-017",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Index Weighting Methods",
        "los": "Compare the different weighting methods used in index construction.",
        "question": "An index weighting methodology where each constituent's weight is determined by multiplying its market share price by only the shares available for public trading (excluding controlling family blocks, government stakes, and insider lock-ups) is classified as:",
        "options": {
            "A": "Price-weighted.",
            "B": "Free-float adjusted market-capitalization weighted.",
            "C": "Fundamentally weighted."
        },
        "answer": "B",
        "explanation": "A free-float adjusted market-capitalization weighted index weights each company according to its available market value—reflecting only shares genuinely accessible to public investors rather than total legal shares outstanding. Major indices like the S&P 500 and MSCI World employ this method.",
        "distractor_analysis": {
            "A": "A price-weighted index weights components based exclusively on per-share price, regardless of shares outstanding or market float.",
            "C": "A fundamentally weighted index weights constituents based on accounting fundamentals such as earnings, book value, or cash flow."
        }
    },
    {
        "id": "L1-EQ-018",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Equal-Weighted Indices",
        "los": "Describe the advantages and disadvantages of equal weighting.",
        "question": "Which of the following is an inherent feature and operational drawback of maintaining an equal-weighted equity index?",
        "options": {
            "A": "It places disproportionately large weights on mega-cap stocks relative to small-cap stocks.",
            "B": "It requires frequent portfolio rebalancing, which incurs transaction costs and imposes a contrarian trading bias.",
            "C": "It automatically self-adjusts for stock splits and dividends without requiring any periodic trades."
        },
        "answer": "B",
        "explanation": "In an equal-weighted index, price divergence immediately shifts constituent weights away from parity. Restoring equal weights requires periodic rebalancing (selling outperforming stocks and buying underperforming stocks—a contrarian strategy). This frequent rebalancing incurs substantial transaction costs and introduces a small-cap bias.",
        "distractor_analysis": {
            "A": "Equal weighting overweights small-cap companies relative to their market capitalization, rather than mega-cap stocks.",
            "C": "Market-cap weighted indices are self-rebalancing with respect to stock splits; equal-weighted indices require active rebalancing."
        }
    },
    {
        "id": "L1-EQ-019",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Fundamental Weighting",
        "los": "Describe the characteristics and biases of fundamentally weighted indices.",
        "question": "A fundamentally weighted equity index constructed using fundamental accounting metrics such as earnings, book value, and dividends will most likely exhibit a systematic:",
        "options": {
            "A": "Momentum tilt.",
            "B": "Value tilt.",
            "C": "Growth tilt."
        },
        "answer": "B",
        "explanation": "Fundamentally weighted indices weight companies based on economic size metrics rather than market prices. When a stock's price rises relative to its fundamentals, its market-cap weight increases, but its fundamental weight remains tied to fundamentals. Thus, fundamental weighting systematically overweights stocks with low price-to-fundamental ratios, imparting a value tilt.",
        "distractor_analysis": {
            "A": "Market-cap weighted indices inherently carry a momentum tilt (holding larger weights in winning stocks as their prices climb).",
            "C": "Growth tilts characterize indices with high valuation multiples and high expected earnings expansion; fundamental weighting has a value tilt."
        }
    },
    {
        "id": "L1-EQ-020",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Price Return vs. Total Return",
        "los": "Calculate and interpret the price return and total return of an index.",
        "question": "The percentage return on a price return equity index differs from that of a total return equity index over the same measurement period because the total return index incorporates:",
        "options": {
            "A": "Capital gains only.",
            "B": "Reinvestment of all cash dividends and distributions paid by constituent firms.",
            "C": "Adjustments for stock splits and stock dividends only."
        },
        "answer": "B",
        "explanation": "A price return index measures solely the percentage price changes (capital appreciation/depreciation) of constituent securities. A total return index measures both capital appreciation and income, assuming that all cash dividends and distributions are fully reinvested in the index constituents.",
        "distractor_analysis": {
            "A": "Both price return and total return indices measure capital gains; only total return includes dividend income.",
            "C": "Both price return and total return indices account for stock splits and bonus issues through divisor adjustments."
        }
    },
    {
        "id": "L1-EQ-021",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Index Management",
        "los": "Explain the concepts of rebalancing and reconstitution.",
        "question": "The formal periodic review process in which an index committee determines which securities are eligible to be added to the index and which failing securities must be removed is defined as:",
        "options": {
            "A": "Reconstitution.",
            "B": "Divisor recalibration.",
            "C": "Rebalancing."
        },
        "answer": "A",
        "explanation": "Reconstitution is the process of updating index membership—adding eligible companies that meet criteria and removing constituents that no longer qualify (due to delisting, mergers, or failing size/liquidity rules). Rebalancing refers to adjusting the portfolio weights of existing constituents.",
        "distractor_analysis": {
            "B": "Divisor recalibration is a mathematical calculation used to preserve index continuity across corporate actions.",
            "C": "Rebalancing is the adjustment of portfolio weights back to their specified target allocations without necessarily changing the constituent roster."
        }
    },
    {
        "id": "L1-EQ-022",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Multi-Market Equity Indices",
        "los": "Describe types of equity indices.",
        "question": "An investor who holds an unhedged multi-market global equity index denominated in domestic currency is exposed to:",
        "options": {
            "A": "Domestic interest rate risk only.",
            "B": "Both foreign asset price fluctuations and currency exchange rate movements.",
            "C": "Asset price risk only, because geographical diversification eliminates currency risk."
        },
        "answer": "B",
        "explanation": "The domestic-currency return of an unhedged foreign equity position equals the foreign equity asset return combined with the exchange rate return of the foreign currency relative to the investor's home currency: $$(1 + R_{\\text{domestic}}) = (1 + R_{\\text{local}}) \\times (1 + R_{\\text{FX}})$$",
        "distractor_analysis": {
            "A": "Multi-market equity indices are primarily exposed to equity market risk and foreign currency exchange rate risk.",
            "C": "Geographic diversification reduces idiosyncratic company risk, but foreign currency risk remains active unless explicitly hedged."
        }
    },
    {
        "id": "L1-EQ-023",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Sector and Style Indices",
        "los": "Describe types of equity indices.",
        "question": "An index designed specifically to represent companies characterized by low price-to-earnings (P/E) ratios, low price-to-book (P/B) ratios, and high dividend yields is a:",
        "options": {
            "A": "Growth style index.",
            "B": "Value style index.",
            "C": "Sector index."
        },
        "answer": "B",
        "explanation": "A value style index selects securities trading at low valuation multiples relative to accounting fundamentals (low P/E, low P/B, low P/CF) and offering higher dividend yields. Growth indices focus on high earnings growth rates and trade at higher valuation multiples.",
        "distractor_analysis": {
            "A": "Growth indices group companies with rapid earnings growth expectations, high P/E multiples, and low dividend yields.",
            "C": "A sector index tracks a specific industry classification (such as Financials or Healthcare), irrespective of value or growth style."
        }
    },
    {
        "id": "L1-EQ-024",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Fixed Income Indices",
        "los": "Compare fixed-income indices with equity indices.",
        "question": "Constructing and replicating fixed-income market indices is generally more challenging than equity indices primarily because:",
        "options": {
            "A": "The universe of publicly traded bond issues is much smaller than the universe of public equity shares.",
            "B": "Bonds trade predominantly in decentralized, dealer-based, illiquid markets and individual issues mature periodically.",
            "C": "Bonds possess continuous, high-volume centralized exchange trading with real-time price discovery."
        },
        "answer": "B",
        "explanation": "Fixed income index replication faces major hurdles: (1) bonds trade over-the-counter (OTC) in dealer markets where pricing is illiquid and often matrix-estimated; (2) individual corporations issue dozens of distinct bond tranches; and (3) bonds mature, requiring continuous index turnover and replacement.",
        "distractor_analysis": {
            "A": "The universe of bond issues is vastly larger (hundreds of thousands of individual CUSIPs) than listed corporate equities.",
            "C": "Bonds trade in opaque OTC dealer markets, not continuous high-volume centralized public exchanges."
        }
    },
    {
        "id": "L1-EQ-025",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Alternative Asset Indices",
        "los": "Describe indices representing alternative assets.",
        "question": "The total return on a fully collateralized commodity futures index comprises which three components?",
        "options": {
            "A": "Spot price return, roll yield, and collateral yield.",
            "B": "Dividend yield, spot price return, and foreign exchange yield.",
            "C": "Coupon yield, capital gains yield, and reinvestment yield."
        },
        "answer": "A",
        "explanation": "A fully collateralized commodity futures index generates returns from: (1) spot price return (changes in underlying commodity prices); (2) roll yield (the return from rolling expiring front-month futures contracts to longer-dated contracts, positive in backwardation and negative in contango); and (3) collateral yield (interest earned on Treasury bills posted as margin).",
        "distractor_analysis": {
            "B": "Physical commodities do not pay dividends; dividend yields apply to equity investments.",
            "C": "Coupon yield and reinvestment yield represent bond index returns, not commodity futures returns."
        }
    },
    {
        "id": "L1-EQ-026",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Market-Cap Index Calculations",
        "los": "Calculate the performance of a market-capitalization weighted index.",
        "question": "An index consists of two stocks, Alpha and Beta. At $t=0$, Alpha trades at 40 USD with 10 million shares, and Beta trades at 20 USD with 30 million shares. At $t=1$, Alpha trades at 50 USD and Beta trades at 22 USD. The 1-year price return of the market-cap weighted index is closest to:",
        "options": {
            "A": "13.5%.",
            "B": "16.0%.",
            "C": "17.5%."
        },
        "answer": "B",
        "explanation": "Market caps at $t=0$:\nAlpha: $\\text{Cap}_{\\text{Alpha}, 0} = 40\\text{ USD} \\times 10\\text{M} = 400\\text{M USD}$.\nBeta: $\\text{Cap}_{\\text{Beta}, 0} = 20\\text{ USD} \\times 30\\text{M} = 600\\text{M USD}$.\nTotal base market cap: $\\text{Cap}_0 = 400\\text{M} + 600\\text{M} = 1{,}000\\text{M USD}$.\nMarket caps at $t=1$:\nAlpha: $\\text{Cap}_{\\text{Alpha}, 1} = 50\\text{ USD} \\times 10\\text{M} = 500\\text{M USD}$.\nBeta: $\\text{Cap}_{\\text{Beta}, 1} = 22\\text{ USD} \\times 30\\text{M} = 660\\text{M USD}$.\nTotal ending market cap: $\\text{Cap}_1 = 500\\text{M} + 660\\text{M} = 1{,}160\\text{M USD}$.\n$$\\text{Return} = \\frac{1{,}160\\text{M} - 1{,}000\\text{M}}{1{,}000\\text{M}} = 16.0\\%$$",
        "distractor_analysis": {
            "A": "13.5% results from an arithmetic weighting error or using price weighting.",
            "C": "17.5% is the equal-weighted return: $\\frac{25.0\\% + 10.0\\%}{2} = 17.5\\%$."
        }
    },
    {
        "id": "L1-EQ-027",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Index Weighting Comparison",
        "los": "Compare the performance of price-weighted and equal-weighted indices.",
        "question": "A portfolio manager tracks three stocks: Stock P at 10 USD (rises to 15 USD), Stock Q at 20 USD (rises to 22 USD), and Stock R at 70 USD (falls to 63 USD). The price return of an equal-weighted index of these three stocks is closest to:",
        "options": {
            "A": "0.0%.",
            "B": "8.3%.",
            "C": "16.7%."
        },
        "answer": "C",
        "explanation": "Calculate individual stock percentage returns:\nStock P: $\\frac{15 - 10}{10} = +50.0\\%$.\nStock Q: $\\frac{22 - 20}{20} = +10.0\\%$.\nStock R: $\\frac{63 - 70}{70} = -10.0\\%$.\nThe equal-weighted index return is the simple arithmetic mean of the returns: $$R_{\\text{EW}} = \\frac{+50.0\\% + 10.0\\% + (-10.0\\%)}{3} = \\frac{50.0\\%}{3} \\approx 16.7\\%$$ Note that the price-weighted index return is 0.0% because the sum of prices remains 100 USD.",
        "distractor_analysis": {
            "A": "0.0% is the price-weighted index return: $\\frac{(15 + 22 + 63) - (10 + 20 + 70)}{10 + 20 + 70} = \\frac{100 - 100}{100} = 0.0\\%$.",
            "B": "8.3% calculates the return incorrectly by dividing the return sum by 6 instead of 3."
        }
    },
    {
        "id": "L1-EQ-028",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Float-Adjusted Market Capitalization",
        "los": "Calculate the float-adjusted market capitalization of a company.",
        "question": "A corporation has 50 million total shares outstanding. The founding family owns 15 million shares in a controlling trust, the government holds 5 million restricted shares, and an employee stock ownership plan holds 2 million shares subject to multi-year lock-up. If the current share price is 40 USD, the company's free-float market capitalization is closest to:",
        "options": {
            "A": "1,120 million USD.",
            "B": "1,200 million USD.",
            "C": "2,000 million USD."
        },
        "answer": "A",
        "explanation": "Free-float shares exclude non-public, controlling, government, and restricted holdings: $$\\text{Free-Float Shares} = 50\\text{M} - (15\\text{M} + 5\\text{M} + 2\\text{M}) = 50\\text{M} - 22\\text{M} = 28\\text{ million shares}$$ $$\\text{Free-Float Market Cap} = 28\\text{M shares} \\times 40\\text{ USD} = 1{,}120\\text{ million USD}$$",
        "distractor_analysis": {
            "B": "1,200 million USD omits the 2 million locked-up employee shares: $(50\\text{M} - 20\\text{M}) \\times 40 = 1{,}200\\text{M USD}$.",
            "C": "2,000 million USD is the total unadjusted market capitalization: $\\text{Cap} = 50\\text{M shares} \\times 40\\text{ USD} = 2{,}000\\text{M USD}$."
        }
    },

    # =========================================================================
    # MODULE 3: MARKET EFFICIENCY (Q29 - Q42)
    # =========================================================================
    {
        "id": "L1-EQ-029",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Market Efficiency Concepts",
        "los": "Describe market efficiency and explain the difference between market value and intrinsic value.",
        "question": "In an informationally efficient capital market, the prevailing market price of a security represents:",
        "options": {
            "A": "An unbiased estimate of the security's fundamental intrinsic value.",
            "B": "A definitive valuation floor that guarantees investors will not suffer capital losses.",
            "C": "The historical accounting book value of corporate net assets."
        },
        "answer": "A",
        "explanation": "In an informationally efficient market, asset prices rapidly and accurately adjust to all available information. Consequently, market price is an unbiased estimate of intrinsic value, with pricing errors being random and unsystematic.",
        "distractor_analysis": {
            "B": "Market efficiency does not guarantee against losses; prices fluctuate randomly as unpredictable new economic information arrives.",
            "C": "Market prices reflect the discounted present value of expected future cash flows, not historical balance sheet book values."
        }
    },
    {
        "id": "L1-EQ-030",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Determinants of Market Efficiency",
        "los": "Explain factors that affect market efficiency.",
        "question": "Informational market efficiency is most likely to be enhanced by an increase in:",
        "options": {
            "A": "Borrowing fees and regulatory restrictions on short selling.",
            "B": "The number of active market participants and independent research analysts covering the securities.",
            "C": "Brokerage transaction commissions and bid-ask spreads."
        },
        "answer": "B",
        "explanation": "Market efficiency increases when many independent market participants and analysts compete to gather, process, and trade on information. Conversely, impediments to trading—such as short-selling bans, high borrow fees, or wide bid-ask spreads—inhibit arbitrage and degrade market efficiency.",
        "distractor_analysis": {
            "A": "Short-selling restrictions impede arbitrage and prevent overvalued assets from correcting, reducing market efficiency.",
            "C": "Higher transaction costs widen arbitrage bounds, permitting larger pricing distortions to persist."
        }
    },
    {
        "id": "L1-EQ-031",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Weak-Form Market Efficiency",
        "los": "Contrast weak-form, semi-strong-form, and strong-form market efficiency.",
        "question": "If a market is weak-form efficient, an investor who trades systematically based on moving average crossovers and historical volume patterns will most likely:",
        "options": {
            "A": "Earn consistent abnormal risk-adjusted returns over time.",
            "B": "Be unable to earn abnormal risk-adjusted returns net of trading costs.",
            "C": "Outperform passive buy-and-hold index benchmarks consistently."
        },
        "answer": "B",
        "explanation": "Under weak-form market efficiency, current prices fully incorporate all historical market trading data (past prices, returns, and trading volume). Consequently, technical analysis cannot systematically produce abnormal risk-adjusted returns.",
        "distractor_analysis": {
            "A": "Weak-form efficiency explicitly invalidates technical analysis as a source of consistent abnormal risk-adjusted returns.",
            "C": "Trading on historical price charts will incur transaction costs and underperform a passive buy-and-hold index strategy."
        }
    },
    {
        "id": "L1-EQ-032",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Semi-Strong Form Market Efficiency",
        "los": "Explain the implications of semi-strong-form market efficiency for fundamental analysis.",
        "question": "If an equity market is semi-strong-form efficient, which of the following strategies can consistently generate abnormal risk-adjusted returns?",
        "options": {
            "A": "Conducting in-depth fundamental analysis of published 10-K financial statements and earnings reports.",
            "B": "Executing trading rules based on moving average support and resistance levels.",
            "C": "Neither fundamental analysis of public records nor technical analysis."
        },
        "answer": "C",
        "explanation": "In a semi-strong-form efficient market, security prices rapidly reflect all publicly available information (including historical market data, company financial reports, news releases, and economic forecasts). Thus, neither fundamental analysis based on public data nor technical analysis can earn abnormal risk-adjusted returns.",
        "distractor_analysis": {
            "A": "Fundamental analysis of public records cannot beat the market in semi-strong efficiency because public data is already priced in.",
            "B": "Technical analysis is ineffective in weak-form efficient markets, and semi-strong efficiency subsumes weak-form efficiency."
        }
    },
    {
        "id": "L1-EQ-033",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Strong-Form Market Efficiency",
        "los": "Describe strong-form market efficiency and its empirical validity.",
        "question": "Strong-form market efficiency asserts that security prices fully and instantaneously reflect:",
        "options": {
            "A": "Historical price and volume trading data only.",
            "B": "All publicly available financial and economic information only.",
            "C": "All information from both public and private (insider) sources."
        },
        "answer": "C",
        "explanation": "Strong-form efficiency states that stock prices incorporate all information—public and private. Under strong-form efficiency, even corporate insiders cannot generate abnormal returns. Empirical evidence rejects strong-form efficiency, as insiders consistently profit from private data (which is why insider trading is legally banned).",
        "distractor_analysis": {
            "A": "Historical price and volume data describes weak-form efficiency.",
            "B": "All publicly available information describes semi-strong-form efficiency."
        }
    },
    {
        "id": "L1-EQ-034",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Implications of Market Efficiency",
        "los": "Explain the role of a portfolio manager in an efficient market.",
        "question": "Even in an informationally efficient market where active stock-picking cannot beat index benchmarks, professional portfolio managers add vital value by:",
        "options": {
            "A": "Consistently identifying undervalued individual stocks to achieve superior alpha.",
            "B": "Establishing optimal asset allocation, achieving broad diversification, and minimizing client taxes and transaction costs.",
            "C": "Timing macroeconomic market tops and bottoms using technical cycles."
        },
        "answer": "B",
        "explanation": "In an efficient market, managers provide crucial services: (1) establishing appropriate asset allocation tailored to the client's risk-return objectives; (2) constructing a diversified portfolio eliminating idiosyncratic risk; (3) managing tax liability through tax-loss harvesting; and (4) rebalancing efficiently to maintain target risk exposures.",
        "distractor_analysis": {
            "A": "In an efficient market, security selection cannot generate consistent abnormal alpha.",
            "C": "Market timing through technical cycles is ineffective in an efficient market."
        }
    },
    {
        "id": "L1-EQ-035",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Market Anomalies",
        "los": "Explain calendar, cross-sectional, and event-related market anomalies.",
        "question": "The January effect is a calendar anomaly where equities—especially small-cap stocks—tend to exhibit abnormally high returns in January. The primary behavioral and economic explanation for this effect is:",
        "options": {
            "A": "Year-end tax-loss selling in December followed by aggressive reinvestment in January.",
            "B": "Predictable quarterly dividend announcements scheduled exclusively for January.",
            "C": "Corporate managers buying shares ahead of mandatory annual shareholder meetings."
        },
        "answer": "A",
        "explanation": "The January effect is primarily driven by tax-loss selling: investors sell underperforming small-cap stocks in December to realize capital losses for tax purposes, depressing prices. In January, the selling pressure ceases and investors reinvest their liquidity, causing a predictable rebound.",
        "distractor_analysis": {
            "B": "Corporate dividend announcements are distributed throughout all four quarters and do not concentrate solely in January.",
            "C": "Manager insider buying is strictly regulated and does not systematically cause the January effect."
        }
    },
    {
        "id": "L1-EQ-036",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Cross-Sectional Anomalies",
        "los": "Describe cross-sectional anomalies.",
        "question": "The empirical finding that stocks with low price-to-earnings (P/E) ratios and low price-to-book (P/B) ratios systematically earn higher long-run risk-adjusted returns than stocks with high valuation multiples is known as the:",
        "options": {
            "A": "Momentum effect.",
            "B": "Value effect.",
            "C": "Size effect."
        },
        "answer": "B",
        "explanation": "The value effect is a well-documented cross-sectional anomaly where value stocks (low P/E, low P/B, high dividend yield) systematically outperform growth stocks on a risk-adjusted basis over multi-year horizons.",
        "distractor_analysis": {
            "A": "The momentum effect describes the tendency for stocks with high recent returns to continue outperforming in the short-to-medium term.",
            "C": "The size effect refers to the empirical outperformance of small-capitalization stocks relative to large-capitalization stocks."
        }
    },
    {
        "id": "L1-EQ-037",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Event-Related Anomalies",
        "los": "Describe event-related market anomalies.",
        "question": "The empirical anomaly where stock prices exhibit a prolonged, gradual drift in the direction of an earnings surprise for weeks following the earnings announcement is known as:",
        "options": {
            "A": "Post-earnings announcement drift (PEAD).",
            "B": "The closed-end fund discount.",
            "C": "The turn-of-the-month effect."
        },
        "answer": "A",
        "explanation": "Post-earnings announcement drift (PEAD) occurs when market prices underreact to quarterly earnings surprises. Prices of firms with positive earnings surprises continue to drift upward for 60 to 90 days following the announcement, directly challenging semi-strong market efficiency.",
        "distractor_analysis": {
            "B": "The closed-end fund discount refers to closed-end funds trading at market prices below their net asset value (NAV).",
            "C": "The turn-of-the-month effect is a calendar anomaly showing higher returns on the final day and first few days of each month."
        }
    },
    {
        "id": "L1-EQ-038",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Behavioral Finance",
        "los": "Contrast behavioral finance with the traditional efficient market hypothesis.",
        "question": "Under Kahneman and Tversky's prospect theory, the behavioral finding that investors experience the psychological pain of a monetary loss roughly twice as intensely as the pleasure from an equivalent gain is termed:",
        "options": {
            "A": "Mental accounting.",
            "B": "Loss aversion.",
            "C": "Overconfidence."
        },
        "answer": "B",
        "explanation": "Loss aversion demonstrates that utility functions are asymmetric: the disutility of a loss is approximately 2 to 2.5 times larger than the utility of an equivalent monetary gain. This induces investors to hold losing stocks too long (disposition effect) in the hope of breaking even.",
        "distractor_analysis": {
            "A": "Mental accounting involves treating money differently based on subjective compartments or source of funds rather than total wealth.",
            "C": "Overconfidence refers to individuals overestimating their forecasting accuracy and knowledge precision."
        }
    },
    {
        "id": "L1-EQ-039",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Behavioral Biases",
        "los": "Describe behavioral biases that cause market anomalies.",
        "question": "An investor who attributes profitable stock selections to superior personal intelligence while blaming losing investments on unexpected external economic shocks is exhibiting:",
        "options": {
            "A": "Self-attribution bias.",
            "B": "Anchoring and adjustment bias.",
            "C": "Conservatism bias."
        },
        "answer": "A",
        "explanation": "Self-attribution bias is the cognitive tendency to attribute positive outcomes to one's own skill and analytical talent while blaming negative outcomes on bad luck or external forces, reinforcing unwarranted overconfidence.",
        "distractor_analysis": {
            "B": "Anchoring bias occurs when an investor fixates on an initial figure (such as historical purchase price) when estimating value.",
            "C": "Conservatism bias occurs when an investor underreacts to new evidence, clinging excessively to prior forecasts."
        }
    },
    {
        "id": "L1-EQ-040",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Behavioral Biases",
        "los": "Explain mental accounting and its impact on portfolio construction.",
        "question": "An individual maintains an ultra-conservative portfolio of treasury bills for a child's college fund while simultaneously day-trading high-risk options in a separate 'speculative' account, refusing to analyze aggregate portfolio risk. This behavior best illustrates:",
        "options": {
            "A": "Mental accounting.",
            "B": "Gambler's fallacy.",
            "C": "Framing bias."
        },
        "answer": "A",
        "explanation": "Mental accounting is the behavioral bias where investors separate capital into isolated mental buckets (e.g., retirement, education, speculative play), ignoring portfolio covariance and failing to construct an integrated, mean-variance efficient portfolio.",
        "distractor_analysis": {
            "B": "Gambler's fallacy is the erroneous belief that independent random events are self-reversing (e.g., expecting a stock to rise because it fell three days in a row).",
            "C": "Framing bias occurs when decision-makers reach different conclusions depending on whether a scenario is presented as a gain or a loss."
        }
    },
    {
        "id": "L1-EQ-041",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Behavioral Biases",
        "los": "Contrast conservatism bias with representativeness bias.",
        "question": "When an analyst fails to revise an earnings forecast sufficiently after a company releases an extraordinary earnings report that completely transforms its fundamental outlook, the analyst is displaying:",
        "options": {
            "A": "Representativeness bias.",
            "B": "Conservatism bias.",
            "C": "Availability bias."
        },
        "answer": "B",
        "explanation": "Conservatism bias is a cognitive error where investors underreact to new information, maintaining excessive adherence to their prior beliefs. This psychological inertia is considered a core driver of post-earnings announcement drift.",
        "distractor_analysis": {
            "A": "Representativeness bias involves overreacting to recent patterns and categorizing events based on superficial similarities without considering base rates.",
            "C": "Availability bias occurs when people over-weight events that are easily recalled from memory (e.g., vivid recent market crashes)."
        }
    },
    {
        "id": "L1-EQ-042",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Limits to Arbitrage",
        "los": "Explain why limits to arbitrage may prevent markets from being fully efficient.",
        "question": "Even when sophisticated arbitrageurs detect blatant pricing discrepancies, market mispricings can persist for prolonged periods primarily because:",
        "options": {
            "A": "Arbitrageurs face short-selling borrow fees, recall risk, and the risk that noise traders push prices further away from fundamental value.",
            "B": "Modern electronic exchanges charge zero transaction fees and provide unlimited liquidity.",
            "C": "Regulatory bodies force asset prices to converge to fundamental value within 24 hours."
        },
        "answer": "A",
        "explanation": "Limits to arbitrage explain why mispricings endure: real-world arbitrage requires capital and entails risk. Arbitrageurs face short-borrow fees, margin calls, liquidity constraints, and noise trader risk (the risk that irrational market participants push prices even further from fair value before correcting).",
        "distractor_analysis": {
            "B": "Electronic exchanges impose transaction costs, and liquidity is finite, creating barriers to costless arbitrage.",
            "C": "Regulatory agencies monitor fraud and disclosure; they do not dictate or enforce market prices."
        }
    },

    # =========================================================================
    # MODULE 4: OVERVIEW OF EQUITY SECURITIES (Q43 - Q54)
    # =========================================================================
    {
        "id": "L1-EQ-043",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Common Shares",
        "los": "Describe characteristics of common shares.",
        "question": "Which of the following characteristics is uniquely true of common equity shareholders compared to debt holders and preferred shareholders?",
        "options": {
            "A": "Contractual guarantee of fixed periodic income distributions.",
            "B": "Subordinated residual claim on corporate assets and earnings in bankruptcy liquidation.",
            "C": "Senior priority claim on operating cash flow prior to corporate tax assessment."
        },
        "answer": "B",
        "explanation": "Common equity holders possess a residual claim on company earnings and assets. In liquidation, they receive proceeds only after all contractual obligations—including senior debt, subordinated debt, accounts payable, and preferred stock—are satisfied in full. In return, they participate in unlimited upside.",
        "distractor_analysis": {
            "A": "Fixed income distributions are contractual features of bonds and preferred stock; common stock dividends are fully discretionary.",
            "C": "Debt interest payments have senior priority over common equity and are paid before corporate tax liabilities."
        }
    },
    {
        "id": "L1-EQ-044",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Voting Rights",
        "los": "Compare statutory voting with cumulative voting.",
        "question": "A shareholder owns 500 shares in a corporation holding an election for four open board of directors seats. Under cumulative voting, the maximum number of votes the shareholder can cast for a single candidate is:",
        "options": {
            "A": "500 votes.",
            "B": "1,500 votes.",
            "C": "2,000 votes."
        },
        "answer": "C",
        "explanation": "Under statutory voting, a shareholder can cast at most 500 votes per seat. Under cumulative voting, total votes equal shares owned multiplied by open director seats: $$\\text{Total Votes} = 500 \\times 4 = 2{,}000\\text{ votes}$$ The shareholder can allocate all 2,000 votes to one preferred candidate, empowering minority shareholders to gain board representation.",
        "distractor_analysis": {
            "A": "500 votes is the limit per seat under statutory voting.",
            "B": "1,500 votes corresponds to 3 director seats under cumulative voting: $\\text{Votes} = 500 \\times 3 = 1{,}500$."
        }
    },
    {
        "id": "L1-EQ-045",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Preference Shares",
        "los": "Compare cumulative and non-cumulative preferred shares.",
        "question": "If a corporation encounters financial distress and suspends all preferred dividend declarations for two years, holders of cumulative preferred shares:",
        "options": {
            "A": "Forfeit all omitted dividend payments permanently.",
            "B": "Must receive all accumulated dividends in arrears before any dividends can be paid to common shareholders.",
            "C": "Have the immediate legal power to force the issuing corporation into involuntary bankruptcy."
        },
        "answer": "B",
        "explanation": "Cumulative preferred stock stipulates that any skipped dividend payments accumulate as 'dividends in arrears.' The company cannot distribute any dividends to common stockholders until all dividends in arrears and current preferred dividends are paid in full.",
        "distractor_analysis": {
            "A": "Permanent forfeiture of omitted dividends describes non-cumulative preferred stock, not cumulative preferred stock.",
            "C": "Preferred stock is equity capital; failure to declare dividends does not constitute an event of default or trigger bankruptcy."
        }
    },
    {
        "id": "L1-EQ-046",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Preference Shares",
        "los": "Compare participating and non-participating preference shares.",
        "question": "In addition to a stated fixed dividend rate, participating preferred shares provide investors with the right to:",
        "options": {
            "A": "Receive an additional distribution if common dividends or corporate earnings exceed a specified hurdle.",
            "B": "Force the company to redeem the shares at par value at the investor's sole option.",
            "C": "Exercise permanent board of directors veto power over operational budgets."
        },
        "answer": "A",
        "explanation": "Participating preferred shares entitle the holder to receive the standard stated preferred dividend plus an extra distribution if common dividends or company net profits exceed a specified threshold. They may also participate in extra liquidation proceeds.",
        "distractor_analysis": {
            "B": "Forcing the company to redeem shares at par is a put option embedded in putable shares, not participating shares.",
            "C": "Participating shares do not convey board veto power over operational budgets."
        }
    },
    {
        "id": "L1-EQ-047",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Convertible Preference Shares",
        "los": "Explain the features and investment characteristics of convertible preference shares.",
        "question": "An investor owns convertible preferred shares with a par value of 100 USD and a conversion ratio of 4 shares of common stock. If the market price of the common stock rises to 32 USD per share, the conversion value of each preferred share is:",
        "options": {
            "A": "100 USD.",
            "B": "125 USD.",
            "C": "128 USD."
        },
        "answer": "C",
        "explanation": "The conversion value of a convertible preferred share is: $$\\text{Conversion Value} = \\text{Conversion Ratio} \\times \\text{Market Price of Common Stock} = 4 \\times 32\\text{ USD} = 128\\text{ USD}$$ Because the conversion value (128 USD) exceeds the par value (100 USD), the preferred share will trade at least at 128 USD.",
        "distractor_analysis": {
            "A": "100 USD is the fixed par value of the preferred share.",
            "B": "125 USD is calculated using $V = 100 / 0.80 = 125\\text{ USD}$ or an erroneous conversion multiple."
        }
    },
    {
        "id": "L1-EQ-048",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Callable and Putable Shares",
        "los": "Describe callable and putable equity shares.",
        "question": "A company issues callable preferred shares. Compared to an otherwise identical non-callable preferred share, the callable preferred share will most likely:",
        "options": {
            "A": "Trade at a higher market price and offer a lower dividend yield.",
            "B": "Trade at a lower market price and offer a higher dividend yield.",
            "C": "Provide the investor with an option to force redemption at par."
        },
        "answer": "B",
        "explanation": "A callable preferred share includes an embedded call option benefiting the issuer, allowing the company to retire the shares if interest rates fall. Because this caps upside and imposes reinvestment risk on the investor, investors demand a higher dividend yield, which depresses the market price.",
        "distractor_analysis": {
            "A": "A higher price and lower yield characterize putable shares, where the embedded option benefits the investor.",
            "C": "The right to force redemption at par is the defining feature of putable shares, not callable shares."
        }
    },
    {
        "id": "L1-EQ-049",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Private Equity Securities",
        "los": "Compare private equity securities with public equity securities.",
        "question": "Compared to publicly traded equity investments, private equity investments are generally characterized by:",
        "options": {
            "A": "Continuous exchange liquidity and strict quarterly financial disclosure filings.",
            "B": "Lower liquidity, longer investment holding horizons, and less stringent regulatory reporting obligations.",
            "C": "Shorter holding periods and lower target rates of return."
        },
        "answer": "B",
        "explanation": "Private equity investments (venture capital, buyout) are characterized by illiquidity (capital commitments locked for 7 to 10 years), private contractual reporting without public SEC mandates, and higher hurdle rates to compensate for the illiquidity premium.",
        "distractor_analysis": {
            "A": "Continuous exchange liquidity and public regulatory filings (such as 10-K/10-Q) characterize public equities.",
            "C": "Private equity requires long investment horizons and targets higher returns than public equities."
        }
    },
    {
        "id": "L1-EQ-050",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Depository Receipts",
        "los": "Describe types of depository receipts.",
        "question": "In a sponsored American Depository Receipt (ADR) program:",
        "options": {
            "A": "The foreign issuing company actively participates, and ADR holders retain voting rights.",
            "B": "A US bank creates the receipts without the formal cooperation or authorization of the foreign company.",
            "C": "The receipts are prohibited from trading on major registered US stock exchanges."
        },
        "answer": "A",
        "explanation": "In a sponsored ADR, the foreign issuing corporation signs a formal deposit agreement with the US depositary bank. The foreign firm provides financial disclosures, and voting rights are passed directly through to ADR holders. In unsponsored ADRs, the bank creates the program without issuer involvement.",
        "distractor_analysis": {
            "B": "Creation without the foreign company's formal involvement defines an unsponsored ADR.",
            "C": "Sponsored ADRs (Levels II and III) are specifically designed to trade on major US exchanges like NYSE and Nasdaq."
        }
    },
    {
        "id": "L1-EQ-051",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "ADR Levels",
        "los": "Compare the characteristics of ADR levels.",
        "question": "A foreign corporation wishing to raise new equity capital directly from public investors in the United States by listing on the New York Stock Exchange must issue:",
        "options": {
            "A": "Level I ADRs.",
            "B": "Level II ADRs.",
            "C": "Level III ADRs."
        },
        "answer": "C",
        "explanation": "Level III ADR programs allow foreign issuers to raise new equity capital on major US exchanges (NYSE, Nasdaq). They require the most comprehensive SEC registration (Form F-1) and full compliance with US GAAP or IFRS. Level II ADRs list on US exchanges but only trade existing shares without raising new capital. Level I ADRs trade OTC.",
        "distractor_analysis": {
            "A": "Level I ADRs trade over-the-counter (OTC) and cannot be used to raise new capital or list on major exchanges.",
            "B": "Level II ADRs list on major exchanges to trade existing shares, but cannot be used for primary capital raising."
        }
    },
    {
        "id": "L1-EQ-052",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Book Value vs. Market Value",
        "los": "Explain the difference between the book value and the market value of equity.",
        "question": "The market value of a successful corporation's common equity is frequently substantially higher than its balance sheet book value of equity primarily because:",
        "options": {
            "A": "Book value ignores accumulated retained earnings and par share capital.",
            "B": "Market value incorporates investor expectations of future earnings growth and unrecorded intangible assets.",
            "C": "Accounting standards record all corporate debt liabilities at inflated market values."
        },
        "answer": "B",
        "explanation": "Book value reflects historical accounting costs of recorded assets less liabilities. Market value reflects the forward-looking market consensus regarding future earnings power, growth opportunities, brand equity, patents, and intellectual capital that are not capitalized on the balance sheet.",
        "distractor_analysis": {
            "A": "Book value explicitly consists of common stock, additional paid-in capital, and cumulative retained earnings.",
            "C": "Liabilities are generally carried at historical amortized cost under accounting standards, not inflated values."
        }
    },
    {
        "id": "L1-EQ-053",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Return on Equity and DuPont Analysis",
        "los": "Calculate and interpret Return on Equity (ROE) using DuPont decomposition.",
        "question": "A firm reports Net Income of 45 million USD, Total Revenue of 300 million USD, Total Assets of 500 million USD, and Average Shareholders' Equity of 250 million USD. Using the 3-step DuPont decomposition, the company's Return on Equity (ROE) is:",
        "options": {
            "A": "15.0%.",
            "B": "18.0%.",
            "C": "22.5%."
        },
        "answer": "B",
        "explanation": "Using the 3-step DuPont model: $$\\text{ROE} = \\text{Net Profit Margin} \\times \\text{Asset Turnover} \\times \\text{Financial Leverage}$$ $$\\text{Net Profit Margin} = \\frac{45\\text{M USD}}{300\\text{M USD}} = 15.0\\%$$ $$\\text{Asset Turnover} = \\frac{300\\text{M USD}}{500\\text{M USD}} = 0.60$$ $$\\text{Financial Leverage} = \\frac{500\\text{M USD}}{250\\text{M USD}} = 2.0$$ $$\\text{ROE} = 15.0\\% \\times 0.60 \\times 2.0 = 18.0\\%$$ Alternatively, $\\text{ROE} = \\frac{45\\text{M USD}}{250\\text{M USD}} = 18.0\\%$.",
        "distractor_analysis": {
            "A": "15.0% is the Net Profit Margin ($\\frac{45\\text{M}}{300\\text{M}}$).",
            "C": "22.5% uses an incorrect leverage multiplier of 2.5 ($\\text{Leverage} = 500 / 200 = 2.5$)."
        }
    },
    {
        "id": "L1-EQ-054",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Cost of Equity vs. Cost of Debt",
        "los": "Explain why the cost of equity exceeds the cost of debt.",
        "question": "From an investor's perspective, an investment in a corporation's common equity requires a higher expected rate of return than an investment in its debt primarily because:",
        "options": {
            "A": "Common equity cash flows are residual and dividends are discretionary, whereas debt service is legally binding and senior in liquidation.",
            "B": "Corporate interest payments are taxed at the firm level, whereas common dividends are tax-deductible to the corporation.",
            "C": "Common equity prices exhibit lower standard deviations of returns than corporate bonds."
        },
        "answer": "A",
        "explanation": "Equity investors bear higher risk than debt holders because equity is a residual claim: dividends are discretionary, debt service is a mandatory legal contract, and equity is wiped out first in bankruptcy liquidation. Additionally, corporate interest is tax-deductible to the firm, lowering the after-tax cost of debt.",
        "distractor_analysis": {
            "B": "Debt interest payments are tax-deductible for the issuing firm; dividend payments are made from after-tax income.",
            "C": "Common equity exhibits substantially higher standard deviation (volatility) of returns than corporate debt."
        }
    },

    # =========================================================================
    # MODULE 5: INTRODUCTION TO INDUSTRY AND COMPANY ANALYSIS (Q55 - Q66)
    # =========================================================================
    {
        "id": "L1-EQ-055",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Industry Classification Systems",
        "los": "Compare commercial and government industry classification systems.",
        "question": "When performing equity investment research, commercial industry classification systems (such as GICS and ICB) are preferred over government systems (such as SIC and NAICS) primarily because commercial systems:",
        "options": {
            "A": "Group firms solely based on physical raw material inputs rather than market demand.",
            "B": "Are updated more frequently, cover global public firms, and categorize companies based on principal revenue source.",
            "C": "Provide confidential non-public tax filings of private enterprises."
        },
        "answer": "B",
        "explanation": "Commercial systems (MSCI/S&P GICS, FTSE/Dow Jones ICB) are dynamically updated to capture new industries, classify global corporations based on primary commercial revenue sources, and are designed specifically for asset management. Government systems (SIC, NAICS) are updated only every 5 years and emphasize production facilities.",
        "distractor_analysis": {
            "A": "Commercial systems classify by business activity and revenue source, whereas historical government systems emphasized production processes.",
            "C": "Commercial classification systems do not disclose confidential private tax documents."
        }
    },
    {
        "id": "L1-EQ-056",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Cyclical vs. Non-Cyclical Industries",
        "los": "Distinguish between cyclical and non-cyclical industries.",
        "question": "Which of the following industries is most accurately classified as non-cyclical and defensive?",
        "options": {
            "A": "Automobile manufacturing.",
            "B": "Luxury hospitality and resorts.",
            "C": "Pharmaceutical healthcare."
        },
        "answer": "C",
        "explanation": "Non-cyclical defensive industries produce essential goods and services with inelastic demand that remain stable regardless of the economic cycle (e.g., pharmaceuticals, healthcare, consumer staples, regulated utilities). Cyclical industries (automotive, luxury resorts, steel) experience revenues that fluctuate with GDP.",
        "distractor_analysis": {
            "A": "Automobile manufacturing is highly cyclical, as consumers defer big-ticket vehicle purchases during recessions.",
            "B": "Luxury hospitality is discretionary and highly sensitive to corporate travel budgets and consumer disposable income."
        }
    },
    {
        "id": "L1-EQ-057",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Growth vs. Defensive Industries",
        "los": "Contrast growth and defensive industries.",
        "question": "A growth industry is primarily distinguished by which of the following characteristics?",
        "options": {
            "A": "Demand is driven by strong secular trends such that industry revenues expand even during general macroeconomic recessions.",
            "B": "Consistently high dividend payout ratios and low price-to-earnings valuation multiples.",
            "C": "Complete insulation from technological disruption and obsolescence."
        },
        "answer": "A",
        "explanation": "Growth industries benefit from strong structural secular demand trends (e.g., cloud computing, renewable energy) that allow revenue to grow independent of the business cycle. Defensive industries have stable demand during recessions but lack explosive secular growth.",
        "distractor_analysis": {
            "B": "High dividend payouts and low P/E multiples characterize mature or defensive industries, not high-growth sectors.",
            "C": "Growth industries are frequently at the forefront of technological disruption and are highly vulnerable to obsolescence."
        }
    },
    {
        "id": "L1-EQ-058",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Peer Group Analysis",
        "los": "Describe the process of constructing a peer group.",
        "question": "When constructing an appropriate peer group of comparable companies for relative valuation, an equity analyst should prioritize companies that:",
        "options": {
            "A": "Share identical 12-month trailing stock price return correlations.",
            "B": "Exhibit similar principal business activities, demand drivers, cost structures, and capital expenditure profiles.",
            "C": "Have identical executive compensation structures."
        },
        "answer": "B",
        "explanation": "A peer group consists of companies whose economic activities are comparable: similar primary business segments, customer demand drivers, cost structures, operating leverage, and capital expenditure needs. Analysts verify comparability by reviewing competitor disclosures in annual 10-K filings.",
        "distractor_analysis": {
            "A": "Peer groups are selected on fundamental business comparability, not past statistical share price correlations.",
            "C": "Executive compensation is a corporate governance item and does not dictate economic business comparability."
        }
    },
    {
        "id": "L1-EQ-059",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Industry Life Cycle",
        "los": "Describe the stages of the industry life cycle.",
        "question": "An industry characterized by slow initial market adoption, high product prices due to lack of scale, substantial R&D requirements, and a high participant failure rate is in the:",
        "options": {
            "A": "Embryonic stage.",
            "B": "Growth stage.",
            "C": "Shakeout stage."
        },
        "answer": "A",
        "explanation": "The embryonic stage is the initial phase of the industry life cycle featuring: slow growth due to customer unfamiliarity, high product prices because scale economies are absent, heavy capital/R&D requirements, and significant risk of startup failure.",
        "distractor_analysis": {
            "B": "The growth stage is characterized by rapidly expanding demand, falling unit costs, increasing scale economies, and entering competitors.",
            "C": "The shakeout stage is marked by decelerating demand growth, industry overcapacity, and intense price wars."
        }
    },
    {
        "id": "L1-EQ-060",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Industry Life Cycle",
        "los": "Describe the shakeout stage of the industry life cycle.",
        "question": "Which of the following conditions is most typical of an industry entering the shakeout stage of its life cycle?",
        "options": {
            "A": "Customer demand growth decelerates, industry capacity built during the expansion exceeds demand, and price wars emerge.",
            "B": "Substantial barriers to entry prevent any competitors from failing or exiting the market.",
            "C": "Rapidly accelerating customer demand allows all competitors to raise prices and operating margins simultaneously."
        },
        "answer": "A",
        "explanation": "During the shakeout stage, revenue growth slows as market penetration approaches saturation. Productive capacity built during the growth phase exceeds actual demand, triggering intense price competition and margin compression that forces high-cost producers out of business.",
        "distractor_analysis": {
            "B": "The shakeout stage is characterized by high corporate failure rates and industry consolidation, not the prevention of exits.",
            "C": "Accelerating demand and expanding profit margins characterize the rapid growth stage."
        }
    },
    {
        "id": "L1-EQ-061",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Industry Life Cycle",
        "los": "Describe the mature stage of the industry life cycle.",
        "question": "In the mature stage of an industry life cycle, surviving companies typically:",
        "options": {
            "A": "Reinvest 100% of cash flows into speculative basic research projects.",
            "B": "Consolidate into an oligopoly, maintain pricing discipline, face high entry barriers, and generate strong free cash flows returned as dividends.",
            "C": "Engage in continuous cutthroat price wars that permanently destroy all industry operating profits."
        },
        "answer": "B",
        "explanation": "Mature industries are characterized by replacement demand, consolidation into an oligopoly of established brand leaders, high barriers to entry, rational pricing discipline, and low capital expenditure needs. Consequently, mature firms generate strong free cash flow and distribute generous dividends.",
        "distractor_analysis": {
            "A": "Mature companies focus on efficiency and cash returns, minimizing speculative R&D compared to embryonic firms.",
            "C": "While competition exists, mature oligopolies avoid self-destructive price wars, adhering instead to price leadership."
        }
    },
    {
        "id": "L1-EQ-062",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Porter's Five Forces",
        "los": "Explain the factors affecting the threat of new entrants in an industry.",
        "question": "Under Michael Porter's Five Forces framework, the threat of new entrants is lowest when an industry exhibits:",
        "options": {
            "A": "High customer switching costs, substantial economies of scale, and proprietary patent protection.",
            "B": "Low capital requirements, standardized generic commodities, and open access to distribution channels.",
            "C": "Rapid technological turnover that renders incumbent manufacturing equipment obsolete."
        },
        "answer": "A",
        "explanation": "High barriers to entry protect incumbent pricing power and profitability. High barriers exist when: (1) substantial economies of scale make small-scale entry unprofitable; (2) high switching costs bind customers; (3) large capital requirements exist; and (4) incumbents hold proprietary patents and distribution networks.",
        "distractor_analysis": {
            "B": "Low capital needs, generic products, and open distribution allow easy entry, resulting in a high threat of new entrants.",
            "C": "Rapid technological turnover lowers entry barriers by enabling nimble startups to leapfrog incumbents."
        }
    },
    {
        "id": "L1-EQ-063",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Porter's Five Forces",
        "los": "Analyze supplier and buyer bargaining power.",
        "question": "An industry's overall pricing power and profitability are most likely to be depressed when:",
        "options": {
            "A": "Suppliers are fragmented and deliver commodity raw materials with multiple substitute options.",
            "B": "Buyers are concentrated, purchase large proportions of industry output, and face negligible switching costs.",
            "C": "Buyers are atomized retail consumers with strong emotional brand attachment."
        },
        "answer": "B",
        "explanation": "Bargaining power of buyers is high when buyers are concentrated, buy in large volumes, have low switching costs, and can credibly threaten backward integration. High buyer power squeezes industry margins through demanded price concessions.",
        "distractor_analysis": {
            "A": "Fragmented suppliers of commodity goods have weak bargaining power, enhancing industry profitability.",
            "C": "Atomized consumers with strong emotional brand loyalty have weak bargaining power, supporting high margins."
        }
    },
    {
        "id": "L1-EQ-064",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Industry Concentration",
        "los": "Describe the effects of industry concentration on pricing power and price competition.",
        "question": "Even in a highly concentrated industry with few competitors, severe price wars are most likely to erupt if:",
        "options": {
            "A": "Products are highly differentiated and customer switching costs are high.",
            "B": "Fixed costs are high, products are undifferentiated commodities, and substantial excess capacity exists.",
            "C": "Industry exit barriers are completely absent."
        },
        "answer": "B",
        "explanation": "Concentrated industries can experience destructive price wars if: (1) fixed costs are high (high operating leverage); (2) products are undifferentiated commodities; (3) substantial industry excess capacity exists; and (4) high exit barriers prevent uncompetitive plants from closing. Firms slash prices toward marginal cost to cover fixed overhead.",
        "distractor_analysis": {
            "A": "Differentiated products and high switching costs shield firms from direct price competition.",
            "C": "Low exit barriers allow uncompetitive firms to exit smoothly, preventing destructive price wars."
        }
    },
    {
        "id": "L1-EQ-065",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Competitive Strategies",
        "los": "Compare cost leadership and product differentiation competitive strategies.",
        "question": "A firm pursuing a low-cost leadership strategy must focus primarily on:",
        "options": {
            "A": "Charging premium prices justified by perceived luxury brand uniqueness.",
            "B": "Achieving scale economies, process efficiency, tight overhead control, and low-cost input sourcing.",
            "C": "Investing heavily in bespoke custom packaging and personalized white-glove customer service."
        },
        "answer": "B",
        "explanation": "Porter's cost leadership strategy involves becoming the lowest-cost producer in the industry through economies of scale, proprietary process technology, low-cost raw materials access, and relentless operating efficiency. The firm can then price at or below market to generate superior margins.",
        "distractor_analysis": {
            "A": "Charging premium prices for perceived uniqueness defines a product differentiation strategy.",
            "C": "Bespoke packaging and personalized service increase operating costs, undermining cost leadership."
        }
    },
    {
        "id": "L1-EQ-066",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Macroeconomic and External Factors",
        "los": "Explain external factors affecting industry growth and profitability.",
        "question": "A persistent secular shift in national demographics toward an aging population is most likely to provide strong structural tailwinds for:",
        "options": {
            "A": "Kindergarten and elementary educational textbook publishing.",
            "B": "Outpatient specialized medical services, assisted living facilities, and wealth preservation advisory.",
            "C": "Youth entertainment and electronic dance music festivals."
        },
        "answer": "B",
        "explanation": "Demographic trends are powerful macroeconomic drivers. An aging demographic profile structurally increases aggregate societal expenditure on specialized healthcare, pharmaceuticals, senior assisted living communities, and post-retirement wealth preservation.",
        "distractor_analysis": {
            "A": "An aging population accompanied by declining birth rates reduces demand for elementary educational materials.",
            "C": "Youth entertainment venues face demographic headwinds as the youth cohort shrinks relative to older age brackets."
        }
    },

    # =========================================================================
    # MODULE 6: EQUITY VALUATION CONCEPTS AND BASIC TOOLS (Q67 - Q85)
    # =========================================================================
    {
        "id": "L1-EQ-067",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Valuation Concepts",
        "los": "Distinguish among intrinsic value, market value, and fair value.",
        "question": "An equity analyst calculates an intrinsic value of 85 USD per share for a stock currently trading in the market at 70 USD per share. The analyst should conclude that the stock is:",
        "options": {
            "A": "Overvalued by the market.",
            "B": "Fairly valued by the market.",
            "C": "Undervalued by the market."
        },
        "answer": "C",
        "explanation": "When an analyst's estimated intrinsic value exceeds the prevailing market price ($V_0 = 85\\text{ USD} > P_0 = 70\\text{ USD}$), the security is undervalued by the market. If market prices converge toward fundamental value over time, the investor will earn an abnormal capital gain.",
        "distractor_analysis": {
            "A": "A security is overvalued when market price exceeds intrinsic value ($P > V_0$).",
            "B": "A stock is fairly valued only when market price equals estimated intrinsic value ($P = V_0$)."
        }
    },
    {
        "id": "L1-EQ-068",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Valuation Model Overview",
        "los": "Explain the rationale for and categories of equity valuation models.",
        "question": "A valuation model that establishes the intrinsic value of common equity by estimating the present value of future cash distributions to shareholders is classified as a(n):",
        "options": {
            "A": "Present value (discounted cash flow) model.",
            "B": "Multiplier (market-multiple) model.",
            "C": "Asset-based valuation model."
        },
        "answer": "A",
        "explanation": "Present value (discounted cash flow, DCF) models value equity by discounting future expected cash flows (such as dividends in the Dividend Discount Model, or free cash flows in FCFE/FCFF models) to the present using a risk-adjusted required rate of return.",
        "distractor_analysis": {
            "B": "Multiplier models evaluate value relative to a financial metric (P/E, P/B, EV/EBITDA) compared to peers.",
            "C": "Asset-based models value equity as the difference between the fair market value of assets and liabilities."
        }
    },
    {
        "id": "L1-EQ-069",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Gordon Growth Model",
        "los": "Calculate the intrinsic value of a non-callable, non-convertible preferred stock and common stock using the Gordon growth model.",
        "question": "A company just paid an annual dividend of 2.50 USD per share ($D_0$). Dividends are expected to grow at a constant annual rate of 4% indefinitely. If the required rate of return on the stock is 9%, the intrinsic value of the share using the Gordon Growth Model is closest to:",
        "options": {
            "A": "50.00 USD.",
            "B": "52.00 USD.",
            "C": "54.17 USD."
        },
        "answer": "B",
        "explanation": "Using the Gordon Growth Model: $$V_0 = \\frac{D_1}{r - g} = \\frac{D_0(1 + g)}{r - g}$$ First calculate expected dividend $D_1$: $$D_1 = 2.50\\text{ USD} \\times (1 + 0.04) = 2.60\\text{ USD}$$ Then calculate intrinsic value: $$V_0 = \\frac{2.60\\text{ USD}}{0.09 - 0.04} = \\frac{2.60\\text{ USD}}{0.05} = 52.00\\text{ USD}$$",
        "distractor_analysis": {
            "A": "50.00 USD erroneously uses $D_0$ instead of $D_1$ in the numerator: $\\frac{2.50}{0.05} = 50.00\\text{ USD}$.",
            "C": "54.17 USD uses an incorrect discount rate or calculates $\\frac{2.60}{0.048} = 54.17\\text{ USD}$."
        }
    },
    {
        "id": "L1-EQ-070",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Gordon Growth Model",
        "los": "Calculate the implied required rate of return using the Gordon growth model.",
        "question": "A stock trades at 40 USD per share. The company is projected to pay a dividend of 1.60 USD per share next year ($D_1$), and dividends are expected to grow at a constant annual rate of 5% indefinitely. The implied required rate of return on the stock is closest to:",
        "options": {
            "A": "7.5%.",
            "B": "9.0%.",
            "C": "10.5%."
        },
        "answer": "B",
        "explanation": "Rearranging the Gordon Growth Model for the required rate of return: $$r = \\frac{D_1}{P_0} + g$$ $$r = \\frac{1.60\\text{ USD}}{40\\text{ USD}} + 0.05 = 0.04 + 0.05 = 0.09 = 9.0\\%$$ The required return equals the dividend yield (4.0%) plus the capital gains growth rate (5.0%).",
        "distractor_analysis": {
            "A": "7.5% uses an incorrect price base or miscalculates dividend yield as 2.5%.",
            "C": "10.5% double-counts growth or adds growth twice: $r = 4.0\\% + 5.0\\% + 1.5\\% = 10.5\\%$."
        }
    },
    {
        "id": "L1-EQ-071",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Sustainable Growth Rate",
        "los": "Calculate and interpret the sustainable growth rate.",
        "question": "A corporation has a Return on Equity (ROE) of 15% and maintains a dividend payout ratio of 40%. The company's sustainable growth rate ($g$) is closest to:",
        "options": {
            "A": "6.0%.",
            "B": "9.0%.",
            "C": "10.0%."
        },
        "answer": "B",
        "explanation": "The sustainable growth rate $g$ is the product of the earnings retention rate ($b$) and Return on Equity ($\\text{ROE}$): $$b = 1 - \\text{Dividend Payout Ratio} = 1 - 0.40 = 0.60$$ $$g = b \\times \\text{ROE} = 0.60 \\times 15\\% = 9.0\\%$$",
        "distractor_analysis": {
            "A": "6.0% uses the dividend payout ratio instead of the retention rate: $g = 0.40 \\times 15\\% = 6.0\\%$.",
            "C": "10.0% is calculated using an incorrect retention rate of 0.67: $g = 0.67 \\times 15\\% = 10.0\\%$."
        }
    },
    {
        "id": "L1-EQ-072",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Multistage Dividend Discount Model",
        "los": "Explain the rationale for and structure of a two-stage dividend discount model.",
        "question": "A two-stage dividend discount model is most appropriately applied to value a company that:",
        "options": {
            "A": "Is in a mature, low-growth stage with permanent 3% constant growth.",
            "B": "Currently enjoys temporary high competitive advantage and supernormal growth, transitioning later to mature sustainable growth.",
            "C": "Has erratic negative cash flows and has never declared a dividend."
        },
        "answer": "B",
        "explanation": "The two-stage DDM is tailored for companies experiencing an initial finite stage of high supernormal growth (due to patents, high market share, or rapid product adoption), followed by a terminal stage where competitive forces erode excess returns and growth stabilizes at a long-term sustainable rate.",
        "distractor_analysis": {
            "A": "A mature company with constant 3% growth is best valued using the single-stage Gordon Growth Model.",
            "C": "A company with negative cash flows and no dividends is better valued using Free Cash Flow or Price-to-Sales multiples."
        }
    },
    {
        "id": "L1-EQ-073",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Multistage Dividend Discount Model",
        "los": "Calculate the intrinsic value of a stock using the two-stage dividend discount model.",
        "question": "A stock just paid an annual dividend of 2.00 USD ($D_0$). Dividends are projected to grow at 10% per year for the next 2 years ($t=1, 2$), after which growth will stabilize at a constant 4% per year indefinitely. If the required rate of return is 8%, the intrinsic value of the stock today is closest to:",
        "options": {
            "A": "53.94 USD.",
            "B": "58.06 USD.",
            "C": "65.34 USD."
        },
        "answer": "B",
        "explanation": "Step 1: Forecast dividends for years 1 and 2:\n$$D_1 = 2.00 \\times 1.10 = 2.20\\text{ USD}$$\n$$D_2 = 2.20 \\times 1.10 = 2.42\\text{ USD}$$\nStep 2: Forecast year 3 dividend (start of constant growth stage):\n$$D_3 = 2.42 \\times 1.04 = 2.5168\\text{ USD}$$\nStep 3: Calculate terminal price at $t=2$:\n$$P_2 = \\frac{D_3}{r - g} = \\frac{2.5168\\text{ USD}}{0.08 - 0.04} = 62.92\\text{ USD}$$\nStep 4: Discount cash flows to present ($t=0$):\n$$\\text{PV}(D_1) = \\frac{2.20}{1.08^1} = 2.0370\\text{ USD}$$\n$$\\text{PV}(D_2) = \\frac{2.42}{1.08^2} = 2.0748\\text{ USD}$$\n$$\\text{PV}(P_2) = \\frac{62.92}{1.08^2} = 53.9438\\text{ USD}$$\n$$V_0 = 2.0370 + 2.0748 + 53.9438 = 58.06\\text{ USD}$$",
        "distractor_analysis": {
            "A": "53.94 USD is only the discounted terminal value $\\text{PV}(P_2)$, omitting the dividends received in years 1 and 2.",
            "C": "65.34 USD is the undiscounted nominal sum of $D_2$ and $P_2$: $V = 2.42 + 62.92 = 65.34\\text{ USD}$."
        }
    },
    {
        "id": "L1-EQ-074",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Preferred Stock Valuation",
        "los": "Calculate the intrinsic value of non-callable, non-convertible perpetual preferred stock.",
        "question": "A perpetual, non-callable, non-convertible preferred stock with a stated par value of 100 USD pays a fixed annual dividend rate of 6.5%. If the required rate of return for this security is 5.0%, the intrinsic value of the preferred share is closest to:",
        "options": {
            "A": "65.00 USD.",
            "B": "100.00 USD.",
            "C": "130.00 USD."
        },
        "answer": "C",
        "explanation": "Because dividend growth is zero ($g = 0$), perpetual preferred stock is valued as a perpetuity: $$D_p = 100\\text{ USD} \\times 6.5\\% = 6.50\\text{ USD}$$ $$V_0 = \\frac{D_p}{r_p} = \\frac{6.50\\text{ USD}}{0.05} = 130.00\\text{ USD}$$ Because the required rate of return (5.0%) is lower than the dividend coupon yield (6.5%), the preferred stock trades at a substantial premium to par.",
        "distractor_analysis": {
            "A": "65.00 USD is computed as $\\frac{6.50}{0.10} = 65.00\\text{ USD}$.",
            "B": "100.00 USD is the par value, which would only equal intrinsic value if the required return equaled 6.5%."
        }
    },
    {
        "id": "L1-EQ-075",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Justified Leading P/E Ratio",
        "los": "Calculate and interpret the justified leading and trailing P/E ratios.",
        "question": "The justified leading price-to-earnings (P/E) ratio based on the Gordon growth model is given by $\\frac{P_0}{E_1} = \\frac{1 - b}{r - g}$. All else being equal, the justified leading P/E ratio will increase if there is an increase in the:",
        "options": {
            "A": "Equity required rate of return ($r$).",
            "B": "Expected long-term dividend growth rate ($g$).",
            "C": "Earnings retention rate ($b$).",
        },
        "answer": "B",
        "explanation": "In the formula $\\frac{P_0}{E_1} = \\frac{1 - b}{r - g}$, an increase in dividend growth rate $g$ narrows the denominator $(r - g)$, causing the justified leading P/E multiple to increase. An increase in $r$ widens the denominator, reducing P/E. An increase in retention $b$ lowers the numerator $(1 - b)$, reducing P/E.",
        "distractor_analysis": {
            "A": "An increase in required return $r$ widens the denominator $(r - g)$, decreasing the justified P/E ratio.",
            "C": "An increase in retention rate $b$ reduces the dividend payout ratio $(1 - b)$ in the numerator, lowering justified P/E."
        }
    },
    {
        "id": "L1-EQ-076",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Justified Trailing P/E Ratio",
        "los": "Calculate the justified trailing P/E ratio.",
        "question": "A company has a dividend payout ratio of 45%, an expected dividend growth rate of 5%, and an equity required rate of return of 10%. The company's justified trailing P/E ratio is closest to:",
        "options": {
            "A": "9.00.",
            "B": "9.45.",
            "C": "10.50."
        },
        "answer": "B",
        "explanation": "The justified trailing P/E ratio incorporates the growth factor $(1 + g)$ in the numerator: $$\\frac{P_0}{E_0} = \\frac{(1 - b)(1 + g)}{r - g} = \\frac{0.45 \\times (1 + 0.05)}{0.10 - 0.05} = \\frac{0.45 \\times 1.05}{0.05} = \\frac{0.4725}{0.05} = 9.45$$",
        "distractor_analysis": {
            "A": "9.00 is the justified leading P/E ratio: $\\frac{0.45}{0.10 - 0.05} = 9.00$.",
            "C": "10.50 results from dividing by $r - g = 0.10 - 0.055$ or misapplying growth."
        }
    },
    {
        "id": "L1-EQ-077",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Price-to-Book Ratio",
        "los": "Explain the rationale for and limitations of the Price-to-Book ratio.",
        "question": "A primary advantage of using the price-to-book (P/B) ratio rather than the price-to-earnings (P/E) ratio in equity valuation is that:",
        "options": {
            "A": "Book value accurately captures all unrecorded intellectual property and human capital.",
            "B": "Book value of equity is generally positive, allowing P/B to be evaluated even when a firm reports negative net income.",
            "C": "Book value is immune to distortions caused by historical accounting conventions and depreciation methods."
        },
        "answer": "B",
        "explanation": "P/E ratios are undefined and meaningless when a company experiences negative net income. In contrast, book value of equity is typically positive (except for severely distressed firms), enabling P/B to be applied across cyclical firms during downturns. Book value is also more stable than annual net income.",
        "distractor_analysis": {
            "A": "Book value excludes internally generated intangible assets (e.g., brand value, patents, human capital).",
            "C": "Book value is heavily influenced by accounting conventions (IFRS vs US GAAP) and historical cost asset carry values."
        }
    },
    {
        "id": "L1-EQ-078",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Price-to-Sales Ratio",
        "los": "Describe the rationale for and limitations of the Price-to-Sales ratio.",
        "question": "Which of the following points represents a significant limitation of relying exclusively on the price-to-sales (P/S) ratio for equity valuation?",
        "options": {
            "A": "Sales figures cannot be observed for early-stage startup companies.",
            "B": "A company can show rapid sales revenue growth while operating with deeply unprofitable cost structures and unsustainable cash burn.",
            "C": "Sales revenue is far more vulnerable to management accounting manipulation than net income."
        },
        "answer": "B",
        "explanation": "A major weakness of P/S is that it ignores operating expenses, debt service, and cost structure. A company can generate expanding revenue while simultaneously incurring catastrophic net losses and negative cash flows, making high sales deceptive without profitability.",
        "distractor_analysis": {
            "A": "P/S is useful precisely because revenue exists for young startups where net income and operating cash flow are negative.",
            "C": "Revenue is generally less vulnerable to subjective distortion than net income, which contains non-cash accruals and reserves."
        }
    },
    {
        "id": "L1-EQ-079",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Price-to-Cash Flow Ratio",
        "los": "Describe the advantages of cash flow multiples.",
        "question": "Analysts frequently prefer price-to-cash flow (P/CF) multiples over price-to-earnings (P/E) multiples primarily because cash flow:",
        "options": {
            "A": "Is less susceptible to management accounting discretion and accrual manipulation than net income.",
            "B": "Is guaranteed to be positive for all listed corporations across every operating year.",
            "C": "Excludes all debt obligations, interest payments, and capital expenditures automatically."
        },
        "answer": "A",
        "explanation": "Accounting net income relies on accrual estimates, subjective revenue recognition, and depreciation schedules, making it vulnerable to earnings manipulation. Cash flow (such as CFO or FCFE) reflects actual liquidity generated and is less distorted by accounting choices.",
        "distractor_analysis": {
            "B": "Operating cash flow can frequently be negative for rapidly expanding, capital-intensive, or distressed companies.",
            "C": "Operating cash flow does not automatically deduct capital expenditures (FCFE deducts CapEx, and CFO includes interest paid)."
        }
    },
    {
        "id": "L1-EQ-080",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Enterprise Value Calculations",
        "los": "Calculate and interpret enterprise value (EV) and EV multiples.",
        "question": "A corporation has 20 million shares of common stock trading at 35 USD per share, preferred stock with a market value of 50 million USD, total debt with a market value of 250 million USD, and cash and cash equivalents of 80 million USD. The company's Enterprise Value (EV) is closest to:",
        "options": {
            "A": "870 million USD.",
            "B": "920 million USD.",
            "C": "1,080 million USD."
        },
        "answer": "B",
        "explanation": "Enterprise Value (EV) represents the total market value of the operating business: $$\\text{Market Value of Equity} = 20\\text{M} \\times 35\\text{ USD} = 700\\text{M USD}$$ $$\\text{EV} = \\text{Market Equity} + \\text{Preferred Stock} + \\text{Total Debt} - \\text{Cash}$$ $$\\text{EV} = 700\\text{M} + 50\\text{M} + 250\\text{M} - 80\\text{M} = 920\\text{ million USD}$$",
        "distractor_analysis": {
            "A": "870 million USD forgets to include the 50 million USD of preferred stock: $\\text{EV} = 700 + 250 - 80 = 870\\text{M USD}$.",
            "C": "1,080 million USD erroneously adds cash instead of subtracting it: $\\text{EV} = 700 + 50 + 250 + 80 = 1{,}080\\text{M USD}$."
        }
    },
    {
        "id": "L1-EQ-081",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "EV/EBITDA Multiple Advantages",
        "los": "Explain the rationale for using EV/EBITDA.",
        "question": "An analyst comparing two companies within the same capital-intensive industry prefers the EV/EBITDA multiple over the P/E multiple primarily because EV/EBITDA:",
        "options": {
            "A": "Allows comparison across firms with differing capital structures and depreciation policies, and can be used when net income is negative.",
            "B": "Directly measures the residual equity cash flow distributed to common shareholders after debt service.",
            "C": "Is always strictly higher than the P/E ratio for any profitable operating business."
        },
        "answer": "A",
        "explanation": "EV/EBITDA compares total firm enterprise value to operating earnings before interest, taxes, depreciation, and amortization. It is neutral to capital structure differences (debt vs. equity financing), unaffected by differing depreciation choices, and applicable when net income is depressed or negative.",
        "distractor_analysis": {
            "B": "EV/EBITDA measures firm-wide operating cash flow available to all capital providers, not residual cash flow to equity.",
            "C": "EV/EBITDA is not universally higher than P/E; EV and EBITDA scale differently depending on debt and tax rates."
        }
    },
    {
        "id": "L1-EQ-082",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Asset-Based Valuation",
        "los": "Describe asset-based valuation models and explain their appropriate application.",
        "question": "An asset-based valuation model is most appropriately applied to value which of the following entities?",
        "options": {
            "A": "A cloud software enterprise whose primary assets consist of proprietary machine learning code and human engineers.",
            "B": "A natural resource exploration company or closed-end real estate trust whose assets have readily determinable market values.",
            "C": "A multinational consumer branding company whose value is driven by unrecorded advertising goodwill."
        },
        "answer": "B",
        "explanation": "Asset-based valuation values equity by subtracting the fair market value of liabilities from the fair market value of assets. It is most reliable for financial holding companies, closed-end investment funds, natural resource firms, and real estate companies whose tangible assets are traded in active markets.",
        "distractor_analysis": {
            "A": "Software companies derive value from proprietary intellectual property and talent, which cannot be reliably marked to market.",
            "C": "Consumer branding companies rely on unrecorded goodwill and customer loyalty that cannot be evaluated in isolation."
        }
    },
    {
        "id": "L1-EQ-083",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Limitations of Asset-Based Valuation",
        "los": "Explain the limitations of asset-based valuation models.",
        "question": "A fundamental difficulty in applying asset-based valuation models to going-concern operating businesses is that:",
        "options": {
            "A": "Cash balances and short-term debt obligations cannot be verified.",
            "B": "The fair market value of intangible assets and going-concern synergies is difficult to determine independently.",
            "C": "Contractual bank liabilities are omitted from corporate financial footnotes."
        },
        "answer": "B",
        "explanation": "A going-concern operating business is worth more than the static liquidation value of its individual separable assets. Estimating the fair market value of intangible assets (brand, customer lists, human capital) and synergistic interactions among business units is subjective and challenging.",
        "distractor_analysis": {
            "A": "Cash and short-term debt are among the most straightforward balance sheet items to value.",
            "C": "Bank liabilities are contractual and explicitly disclosed in audited financial statement footnotes."
        }
    },
    {
        "id": "L1-EQ-084",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Multiples Valuation Methods",
        "los": "Compare the method of comparables with valuation based on fundamental multiples.",
        "question": "An analyst observes that Company T trades at a trailing P/E of 14.0x while its direct industry peer group median is 18.0x. Concluding that Company T is undervalued based solely on this comparison is an application of the:",
        "options": {
            "A": "Gordon growth model.",
            "B": "Method of comparables.",
            "C": "Asset-based valuation model."
        },
        "answer": "B",
        "explanation": "The method of comparables evaluates whether an asset is fairly priced relative to a benchmark peer group multiple. It assumes that comparable firms should trade at similar multiples. However, if Company T has lower expected growth or higher leverage, the discount may be justified.",
        "distractor_analysis": {
            "A": "The Gordon growth model calculates an intrinsic justified multiple from fundamental variables ($r, g, b$).",
            "C": "Asset-based valuation calculates net asset fair values, not relative peer trading multiples."
        }
    },
    {
        "id": "L1-EQ-085",
        "level": 1,
        "topic": "Equity Investments",
        "subtopic": "Valuation Synthesis",
        "los": "Compare valuation models and evaluate whether an asset is fairly valued, overvalued, or undervalued.",
        "question": "An equity analyst estimates that a stock has an intrinsic value of 45 USD per share using a two-stage DDM and a justified P/E valuation of 48 USD per share. The stock currently trades in the market at 55 USD per share. The analyst should conclude that the stock is:",
        "options": {
            "A": "Undervalued by the market.",
            "B": "Overvalued by the market.",
            "C": "Fairly valued by the market."
        },
        "answer": "B",
        "explanation": "Both independent intrinsic valuation models yield value estimates (45 USD and 48 USD) that are significantly below the current market price of 55 USD per share. Because market price exceeds intrinsic value ($P > V_0$), the stock is overvalued by the market, warranting a sell or underweight recommendation.",
        "distractor_analysis": {
            "A": "The stock would be undervalued if the market price were below the intrinsic value estimates (e.g., trading at 40 USD).",
            "C": "A slight divergence between models is expected; when both models indicate that intrinsic value is below market price, the stock is overvalued."
        }
    }
]


def validate_and_dump():
    # 1. Check count
    assert len(questions) == 85, f"Expected 85 questions, got {len(questions)}"

    # 2. Schema check & currency dollar symbol check
    currency_regex = re.compile(r'(?<!\\)\$\s*\d')  # unescaped $ followed by digit
    
    for idx, q in enumerate(questions, 1):
        expected_id = f"L1-EQ-{idx:03d}"
        assert q["id"] == expected_id, f"Question index {idx} has id {q['id']}, expected {expected_id}"
        assert q["level"] == 1, f"{q['id']} level must be 1"
        assert q["topic"] == "Equity Investments", f"{q['id']} topic mismatch"
        assert len(q["options"]) == 3, f"{q['id']} must have exactly 3 options"
        assert set(q["options"].keys()) == {"A", "B", "C"}, f"{q['id']} options keys must be A, B, C"
        assert q["answer"] in {"A", "B", "C"}, f"{q['id']} answer must be A, B, or C"
        
        # Distractor analysis keys must be the two incorrect options
        expected_distractors = {"A", "B", "C"} - {q["answer"]}
        assert set(q["distractor_analysis"].keys()) == expected_distractors, (
            f"{q['id']} distractor keys {set(q['distractor_analysis'].keys())} != {expected_distractors}"
        )

        # Check for unescaped currency dollar signs across all text fields
        text_fields = [
            q["question"],
            q["explanation"],
            q["options"]["A"],
            q["options"]["B"],
            q["options"]["C"],
            q["distractor_analysis"][list(expected_distractors)[0]],
            q["distractor_analysis"][list(expected_distractors)[1]],
        ]
        for tf in text_fields:
            m = currency_regex.search(tf)
            assert not m, f"Found unescaped currency dollar in {q['id']}: {m.group(0)} in '{tf[:50]}...'"

    # 3. Output directory and file
    out_dir = os.path.join("data", "fi_eq")
    os.makedirs(out_dir, exist_ok=True)
    out_file = os.path.join(out_dir, "l1_equity.json")

    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(questions, f, indent=2, ensure_ascii=False)

    print(f"SUCCESS: Generated exactly {len(questions)} CFA Level 1 Equity questions.")
    print(f"Output saved to: {out_file}")
    print("JSON validation and strict currency symbol audit: PASSED.")


if __name__ == "__main__":
    validate_and_dump()
