# CFA Program Curriculum Audit, Completeness Analysis & Master Solved Numericals

**Target Platform**: [CFA Master Study Platform (rahulxcodex.github.io/cfa-master-suite)](https://rahulxcodex.github.io/cfa-master-suite)  
**Authoritative Benchmark**: CFA Institute Official Curriculum (2024–2026 Exam Cycles) cross-referenced against Kaplan SchweserNotes, Wiley/UWorld, and Fitch Learning.  
**Audited Levels**: CFA Level 1 & CFA Level 2  
**Active Subjects Audited**:
1. Financial Statement Analysis (FSA)
2. Fixed Income (FI)
3. Equity Investments (EQ)
4. Portfolio Management and Wealth Planning (PM)

---

## 1. Executive Platform Inventory & Current Coverage Audit

### 1.1 Architecture & Asset Inventory
The live platform deployed at `https://rahulxcodex.github.io/cfa-master-suite` constitutes a single-page exam preparation engine containing:
- **Total Certified Questions**: **1,085 Questions** (545 Level 1 MCQs and 540 Level 2 Vignette Item Sets across 102 multi-part vignettes).
- **Core Subject Breakdown**:
  - **Financial Statement Analysis**: 460 Total Questions (190 L1 MCQs + 270 L2 Questions across 48 vignettes).
  - **Fixed Income**: 205 Total Questions (120 L1 MCQs + 85 L2 Questions across 17 vignettes).
  - **Equity Investments**: 210 Total Questions (115 L1 MCQs + 95 L2 Questions across 19 vignettes).
  - **Portfolio Management**: 210 Total Questions (120 L1 MCQs + 90 L2 Questions across 18 vignettes).
- **Embedded Curriculum Reference Libraries**: 4 extracted technical sheets (`fsa_reference_extracted.html`, `fi_reference_extracted.html`, `eq_reference_extracted.html`, `pm_reference_extracted.html`).
- **Interactive Financial Simulations (12 Engines)**:
  1. Yield Curve Shift, Twist & Butterfly Simulator.
  2. Binomial Interest Rate Tree & Embedded Option Backward Induction Engine.
  3. Equity Valuation: Two-Stage DDM & DuPont Explorer.
  4. Key Rate Duration & Sensitivity Visualizer.
  5. Floating-Rate Note (FRN) Pricing & Discount Margin Engine.
  6. Residual Income Persistence Decay Explorer.
  7. FCFF to FCFE Cash Flow Waterfall Bridge.
  8. Multinational Currency Translation Engine (Current Rate vs. Temporal Method).
  9. MBS Prepayment Simulator & Contraction/Extension Risk Engine.
  10. Markowitz Mean-Variance Frontier & CAL/Indifference Curve Optimizer.
  11. Grinold's Fundamental Law of Active Management & Sharpe Expansion Engine.
  12. Dynamic Rebalancing Corridors & Tolerance Band Simulation Engine.

---

## 2. Curriculum Completeness Analysis (CFA Institute vs. Schweser vs. Live Suite)

### 2.1 Macro Curriculum Scope: 4 Subjects vs. Full 10-Topic CFA Program
The current master suite is explicitly focused on the **quantitative core four** subjects. While these 4 subjects constitute approximately 45%–55% of the total exam weight on both Level 1 and Level 2, the **full CFA Program curriculum consists of 10 distinct topic areas**:

| Topic Area | Level 1 Exam Weight | Level 2 Exam Weight | Present in Master Suite? | Status & Completeness |
| :--- | :---: | :---: | :---: | :--- |
| **Financial Statement Analysis** | 11%–14% | 10%–15% | **YES** | **High Completeness (88%)** |
| **Fixed Income** | 11%–14% | 10%–15% | **YES** | **High Completeness (85%)** |
| **Equity Investments** | 11%–14% | 10%–15% | **YES** | **High Completeness (86%)** |
| **Portfolio Management** | 8%–12% | 10%–15% | **YES** | **High Completeness (82%)** |
| **Ethical & Professional Standards** | 15%–20% | 10%–15% | **NO** | Missing (Standard I–VII, GIPS) |
| **Quantitative Methods** | 6%–9% | 5%–10% | **NO** | Missing (TVM, Regression, Time Series, Machine Learning) |
| **Economics** | 6%–9% | 5%–10% | **NO** | Missing (FX Parity, Growth, Regulatory, Cycles) |
| **Corporate Issuers (Corp Finance)** | 6%–9% | 5%–10% | **NO** | Missing (Capital Structure, Mergers, ESG, Governance) |
| **Derivatives** | 5%–8% | 5%–10% | **NO** | Missing (Futures/Forwards, Options BSM, Swaps) |
| **Alternative Investments** | 7%–10% | 5%–10% | **NO** | Missing (Real Estate, Private Equity NAV, Commodities, Hedge Funds) |

---

### 2.2 In-Depth Topic Audit: Financial Statement Analysis (FSA)

#### Level 1 FSA Mapping:
- **Official Learning Modules (LMs)**:
  1. *LM1: Introduction to Financial Statement Analysis* -> Covered (`m1-intro`)
  2. *LM2: Financial Reporting Standards* -> Covered (`m2-standards`)
  3. *LM3: Understanding Income Statements* -> Covered (`m3-income-statement`)
  4. *LM4: Understanding Balance Sheets* -> Covered (`m4-balance-sheet`)
  5. *LM5: Understanding Statements of Cash Flows* -> Covered (`m5-cash-flow`)
  6. *LM6: Financial Analysis Techniques* -> Covered (`m6-ratios`)
  7. *LM7: Inventories* -> Covered (`m7-inventories`)
  8. *LM8: Long-Lived Assets* -> Covered (`m8-long-lived-assets`)
  9. *LM9: Income Taxes* -> Covered (`m9-taxes`)
  10. *LM10: Non-Current (Long-Term) Liabilities* -> Covered (`m10-debt`)
  11. *LM11: Leases* -> Covered (`m11-leases`)
  12. *LM12: Financial Reporting Quality* -> Covered (`m12-quality-l1`)
- **Missing / Underserved Subtopics**:
  - **Financial Statement Modeling (LM12 in 2025/2026 update)**: Behavioral forecast drivers, sales-driven operating asset/liability projections, and circular interest expense modeling.
  - **Revaluation Surplus Recycling under IFRS vs. US GAAP**: Detailed treatment of revaluation reserve when long-lived asset is derecognized.

#### Level 2 FSA Mapping:
- **Official Learning Modules (LMs)**:
  1. *Intercorporate Investments* -> Covered (`m13-intercorporate`)
  2. *Employee Compensation (Pensions & Stock-Based)* -> Covered (`m14-pensions`)
  3. *Multinational Operations* -> Covered (`m15-multinational`)
  4. *Analysis of Financial Institutions* -> Covered (`m16-financial-institutions`)
  5. *Evaluating Quality of Financial Reports* -> Covered (`m17-quality-l2`)
  6. *Integration of FSA Techniques* -> Covered (`m18-integration`)
- **Missing / Underserved Subtopics**:
  - **Share-Based Compensation Details**: Stock options vs. restricted stock units (RSUs) vs. stock appreciation rights (SARs), grant-date fair value amortized over service period, service-period forfeitures, and tax-windfall deductions in operating cash flows.
  - **Hyperinflationary Accounting (IAS 29 vs. US GAAP temporal)**: Purchasing power gain/loss on net monetary items and index restatement mechanics.

---

### 2.3 In-Depth Topic Audit: Fixed Income (FI)

#### Level 1 Fixed Income Mapping:
- **Official Learning Modules (LMs)**:
  1. *Fixed-Income Instrument Features* -> Covered
  2. *Fixed-Income Cash Flows and Types* -> Covered
  3. *Fixed-Income Issuance and Trading* -> Covered
  4. *Fixed-Income Bond Valuation: Prices and Yields* -> Covered
  5. *Yield and Yield Spread Measures for Fixed-Rate Bonds* -> Covered
  6. *Introduction to Fixed-Income Risk and Return* -> Covered
  7. *Yield Curve and Term Structure* -> Covered
  8. *Fundamentals of Credit Analysis* -> Covered
  9. *Overview of Securitization* -> Covered
- **Missing / Underserved Subtopics**:
  - **Detailed Matrix Pricing**: Exact linear interpolation across both coupon rate differences and maturity spreads.
  - **Covered Bonds vs. ABS**: The dual recourse mechanism and dynamic cover pool mechanics.

#### Level 2 Fixed Income Mapping:
- **Official Learning Modules (LMs)**:
  1. *The Term Structure and Interest Rate Dynamics* -> Covered
  2. *The Arbitrage-Free Valuation Framework* -> Covered
  3. *Valuation and Analysis of Bonds with Embedded Options* -> Covered
  4. *Credit Analysis Models (Structural & Reduced-Form)* -> Covered
  5. *Credit Default Swaps (CDS)* -> Covered
- **Missing / Underserved Subtopics**:
  - **Convertible Bond Valuation & Greeks**: Minimum value of convertible bond, conversion parity price, market conversion premium ratio, premium over straight value, and downside equity risk.
  - **Equilibrium vs. Arbitrage-Free Term Structure Models**: Vasicek model (mean-reverting constant volatility), Cox-Ingersoll-Ross (CIR, volatility proportional to interest rate level), Ho-Lee (time-dependent drift), and Kalotay-Williams-Fabozzi (lognormal rates).
  - **CDS Basis Trading Mechanics**: Negative basis trades (CDS spread < bond credit spread) vs. positive basis trades, and curve steepener / flattener trades.

---

### 2.4 In-Depth Topic Audit: Equity Investments (EQ)

#### Level 1 Equity Investments Mapping:
- **Official Learning Modules (LMs)**:
  1. *Market Organization and Structure* -> Covered
  2. *Security Market Indices* -> Covered
  3. *Market Efficiency* -> Covered
  4. *Overview of Equity Securities* -> Covered
  5. *Company Analysis: Past and Present* -> Covered
  6. *Industry and Competitive Analysis* -> Covered
  7. *Equity Valuation: Concepts and Basic Tools* -> Covered
- **Missing / Underserved Subtopics**:
  - **Margin Call Exact Threshold Equations**: Maintenance margin triggers under tiered commissions and borrowing rates.
  - **Fundamental Indexing vs. Market-Cap Bias**: Rebalancing drag and contrarian rebalancing alpha.

#### Level 2 Equity Valuation Mapping:
- **Official Learning Modules (LMs)**:
  1. *Equity Valuation: Applications and Processes* -> Covered
  2. *Discounted Dividend Valuation* -> Covered
  3. *Free Cash Flow Valuation (FCFF & FCFE)* -> Covered
  4. *Market-Based Valuation: Price & EV Multiples* -> Covered
  5. *Residual Income Valuation* -> Covered
  6. *Private Company Valuation* -> Covered
- **Missing / Underserved Subtopics**:
  - **Excess Earnings Method (EEM) for Private Firms**: Normalized earnings allocated to working capital, fixed tangible assets, and the residual capitalized to value intangible assets.
  - **Clean Surplus Accounting Violations**: Direct adjustments to book value for OCI items (available-for-sale securities, cumulative translation adjustments, post-retirement actuarial adjustments).
  - **H-Model Advanced Algebraic Solving**: Solving for the market-implied required rate of return `r` or the half-life `H` given current trading price.

---

### 2.5 In-Depth Topic Audit: Portfolio Management (PM)

#### Level 1 Portfolio Management Mapping:
- **Official Learning Modules (LMs)**:
  1. *Portfolio Management: An Overview* -> Covered
  2. *Portfolio Risk and Return: Part I* -> Covered
  3. *Portfolio Risk and Return: Part II* -> Covered
  4. *Basics of Portfolio Planning and Construction* -> Covered
  5. *The Behavioral Biases of Individuals* -> Covered
  6. *Introduction to Risk Management* -> Covered
  7. *Technical Analysis* -> Covered
  8. *Fintech in Investment Management* -> Covered
- **Missing / Underserved Subtopics**:
  - **Three-Asset Portfolio Variance Expansion**: Matrix variance-covariance derivation.
  - **Utility Maximization with Risk Aversion A**: Exact portfolio allocation between risk-free asset and optimal risky portfolio.

#### Level 2 Portfolio Management Mapping:
- **Official Learning Modules (LMs)**:
  1. *The Theory of Active Portfolio Management (Fundamental Law)* -> Covered
  2. *Multifactor Models (Macroeconomic, Fundamental, Statistical)* -> Covered
  3. *Analysis of Active Portfolio Management / Factor Investing* -> Covered
  4. *Economics and Asset Allocation* -> Covered
  5. *Portfolio Construction & Rebalancing* -> Covered
  6. *Institutional Investor Portfolios & ALM* -> Covered
  7. *Trade Strategy and Execution* -> Covered
  8. *Portfolio Performance Evaluation & Attribution* -> Covered
- **Missing / Underserved Subtopics**:
  - **Implementation Shortfall (Perold 1988) 4-Way Breakdown**: Execution cost, opportunity cost (unexecuted shares), delay cost (slippage), and explicit fees.
  - **Singer-Terhaar International Asset Pricing Model**: Capital market expectations under partial market integration with the global market portfolio.
  - **Multi-Period Brinson-Fachler Attribution**: Allocation effect, Selection effect, and Interaction effect.
  - **Corridor Width Tolerance Band Dynamics**: Quantitative formulation of optimal rebalancing bandwidth based on transaction costs, volatility, and correlation.
  - **Endowment Spending Rules**: Constant growth rule, rolling 3-year average rule, and hybrid geometric (Tobin) spending formula.

---

---

## 3. Master Solved Numericals: Financial Statement Analysis (FSA)

### Subtopic 3.1: Earnings Per Share (Basic & Diluted EPS)

#### Numerical 3.1.1 (Level: Easy / Foundational)
**Problem Statement**:
Apex Corp reported net income of 1,200,000 USD for the fiscal year ended December 31, 2025. On January 1, 2025, Apex had 500,000 common shares outstanding. On May 1, 2025, Apex issued 120,000 additional common shares. Apex paid 100,000 USD in preferred dividends on its non-convertible cumulative preferred stock. Calculate Apex Corp's Basic EPS.

**Methodology & Formulas**:
`Weighted Average Shares Outstanding (WASO) = sum(Shares_i * (Months_i / 12))`  
`Basic EPS = (Net Income - Preferred Dividends) / WASO`

**Step-by-Step Calculation**:
1. Calculate WASO:
   - Initial shares: `500,000 * (12 / 12) = 500,000`
   - New shares issued May 1 (outstanding for 8 months): `120,000 * (8 / 12) = 80,000`
   - `WASO = 500,000 + 80,000 = 580,000 shares`
2. Earnings Available to Common Shareholders:
   - `Net Income - Preferred Dividends = 1,200,000 USD - 100,000 USD = 1,100,000 USD`
3. Basic EPS:
   - `Basic EPS = 1,100,000 USD / 580,000 = 1.8966 USD` (rounded to 1.90 USD per share).

**Final Answer**: **1.90 USD per share**.  
*Exam Trap Warning*: Cumulative preferred dividends must be subtracted from Net Income whether declared/paid or not!

---

#### Numerical 3.1.2 (Level: Moderate / Intermediate)
**Problem Statement**:
Sigma Holdings reported net income of 4,500,000 USD for 2025 with 1,000,000 common shares outstanding throughout the year. The company had two potentially dilutive securities outstanding:
1. 50,000 shares of 6% cumulative convertible preferred stock, par value 100 USD (each preferred share is convertible into 4 common shares).
2. 200,000 stock options with an exercise price of 30 USD per share. The average market price of common shares during the year was 50 USD.
The corporate tax rate is 25%. Calculate Sigma's Diluted EPS.

**Methodology & Formulas**:
Treasury Stock Method for Options:
`Incremental Shares = Options * (1 - (Exercise Price / Average Market Price))`  
If-Converted Method for Convertible Preferred:
`Incremental Earnings = Preferred Dividend saved = Shares_pref * Par * Dividend Rate`  
`Incremental Shares = Shares_pref * Conversion Ratio`  
Check for antidilution: Incremental EPS must be lower than Basic EPS.

**Step-by-Step Calculation**:
1. Basic EPS:
   - Preferred Dividend: `50,000 * 100 USD * 0.06 = 300,000 USD`
   - Numerator: `4,500,000 USD - 300,000 USD = 4,200,000 USD`
   - Denominator: `1,000,000 shares`
   - `Basic EPS = 4,200,000 USD / 1,000,000 = 4.20 USD`
2. Options Test (Treasury Stock Method):
   - `Incremental Shares = 200,000 * (1 - (30 / 50)) = 200,000 * 0.40 = 80,000 shares`
   - Incremental EPS for options = `0 USD / 80,000 = 0.00 USD` (strongly dilutive).
3. Convertible Preferred Test (If-Converted Method):
   - Preferred Dividend added back: `+300,000 USD` (no tax effect on dividends).
   - Incremental Shares: `50,000 * 4 = 200,000 shares`.
   - Incremental EPS: `300,000 USD / 200,000 = 1.50 USD`.
   - Since `1.50 USD < 4.20 USD`, the convertible preferred is dilutive.
4. Total Diluted EPS Calculation:
   - Diluted Numerator = `4,200,000 USD + 300,000 USD = 4,500,000 USD`
   - Diluted Denominator = `1,000,000 + 80,000 + 200,000 = 1,280,000 shares`
   - `Diluted EPS = 4,500,000 USD / 1,280,000 = 3.5156 USD`

**Final Answer**: **3.52 USD per share**.  
*Exam Trap Warning*: Preferred dividends are NOT tax-deductible; do NOT multiply preferred dividends by `(1 - t)` when adding back to the numerator!

---

#### Numerical 3.1.3 (Level: Difficult / Vignette Multi-Step)
**Problem Statement**:
Vanguard Industrial has Net Income of 8,000,000 USD. Throughout 2025, 2,000,000 common shares were outstanding. The marginal tax rate is 21%. During 2025, the following securities were outstanding:
- 10,000,000 USD face value of 7% convertible bonds issued at par. Each 1,000 USD bond is convertible into 25 common shares.
- 100,000 shares of 8% cumulative convertible preferred stock, 100 USD par. Each preferred share converts into 2 common shares.
- 150,000 executive stock warrants with an exercise price of 40 USD. The average common share price was 60 USD.
Determine which securities are dilutive by ranking incremental EPS from most to least dilutive, and calculate the final Diluted EPS reported in SEC Form 10-K.

**Methodology & Formulas**:
1. Basic EPS benchmark: `(Net Income - Preferred Div) / WASO`
2. Individual Incremental EPS ranking:
   - Warrants: `0 USD / Incremental Shares`
   - Convertible Bonds: `Interest * (1 - t) / Incremental Shares`
   - Convertible Preferred: `Preferred Dividend / Incremental Shares`
3. Sequentially incorporate the most dilutive security into the running EPS until incremental EPS exceeds running EPS.

**Step-by-Step Calculation**:
1. Basic EPS:
   - Preferred Dividend: `100,000 * 100 USD * 0.08 = 800,000 USD`
   - Net Income to Common: `8,000,000 USD - 800,000 USD = 7,200,000 USD`
   - `Basic EPS = 7,200,000 USD / 2,000,000 = 3.60 USD`
2. Incremental EPS for each security:
   - **Warrants**:
     - Shares = `150,000 * (1 - (40 / 60)) = 150,000 * (1/3) = 50,000 shares`
     - Incremental EPS = `0 / 50,000 = 0.00 USD` (Rank 1 - Most dilutive).
   - **Convertible Bonds**:
     - After-tax interest saved = `10,000,000 USD * 0.07 * (1 - 0.21) = 700,000 USD * 0.79 = 553,000 USD`
     - Incremental Shares = `(10,000,000 / 1,000) * 25 = 10,000 * 25 = 250,000 shares`
     - Incremental EPS = `553,000 USD / 250,000 = 2.212 USD` (Rank 2).
   - **Convertible Preferred**:
     - Dividend saved = `800,000 USD`
     - Incremental Shares = `100,000 * 2 = 200,000 shares`
     - Incremental EPS = `800,000 USD / 200,000 = 4.00 USD` (Rank 3).
3. Sequential Dilution Inclusion:
   - **Step 1 (Include Warrants)**:
     - Numerator: `7,200,000 USD`
     - Denominator: `2,000,000 + 50,000 = 2,050,000 shares`
     - Running EPS: `7,200,000 / 2,050,000 = 3.5122 USD`
   - **Step 2 (Include Convertible Bonds)**:
     - Incremental EPS (`2.212 USD`) < Running EPS (`3.5122 USD`) -> Dilutive!
     - Numerator: `7,200,000 USD + 553,000 USD = 7,753,000 USD`
     - Denominator: `2,050,000 + 250,000 = 2,300,000 shares`
     - Running EPS: `7,753,000 / 2,300,000 = 3.3709 USD`
   - **Step 3 (Test Convertible Preferred)**:
     - Incremental EPS is `4.00 USD`.
     - Since `4.00 USD > Running EPS (3.3709 USD)`, including the convertible preferred would **increase** EPS back to `(7,753,000 + 800,000) / (2,300,000 + 200,000) = 8,553,000 / 2,500,000 = 3.4212 USD`.
     - Therefore, the convertible preferred stock is **ANTIDILUTIVE** and must be excluded from Diluted EPS!

**Final Answer**: **Diluted EPS = 3.37 USD per share** (Convertible Preferred excluded as antidilutive).

---

### Subtopic 3.2: Inventories (FIFO, LIFO & LIFO Reserve Adjustments)

#### Numerical 3.2.1 (Level: Easy / Foundational)
**Problem Statement**:
At the beginning of 2025, Global Logistics had a LIFO reserve of 140,000 USD. At the end of 2025, the LIFO reserve was 210,000 USD. For 2025, the company reported Cost of Goods Sold (COGS) under LIFO of 2,800,000 USD. Calculate COGS under FIFO for 2025.

**Methodology & Formulas**:
`LIFO Reserve = Inventory_FIFO - Inventory_LIFO`  
`Change in LIFO Reserve (Delta LIFO Reserve) = Ending LIFO Reserve - Beginning LIFO Reserve`  
`COGS_FIFO = COGS_LIFO - Delta LIFO Reserve`

**Step-by-Step Calculation**:
1. `Delta LIFO Reserve = 210,000 USD - 140,000 USD = +70,000 USD`
2. `COGS_FIFO = 2,800,000 USD - 70,000 USD = 2,730,000 USD`

**Final Answer**: **2,730,000 USD**.  
*Exam Takeaway*: When prices are rising, FIFO COGS is lower than LIFO COGS by the exact increase in the LIFO Reserve.

---

#### Numerical 3.2.2 (Level: Moderate / Intermediate)
**Problem Statement**:
Pacifica Inc. reports under US GAAP and uses LIFO for inventory valuation. For 2025, Pacifica reported:
- LIFO Ending Inventory: 850,000 USD
- Beginning LIFO Reserve: 120,000 USD; Ending LIFO Reserve: 195,000 USD
- LIFO Net Income: 420,000 USD
- Effective Tax Rate: 25%
- Total Debt: 1,500,000 USD; Total Equity: 2,000,000 USD
Convert Pacifica's financial statements to FIFO and compute the adjusted Debt-to-Equity ratio.

**Methodology & Formulas**:
`Inventory_FIFO = Inventory_LIFO + Ending LIFO Reserve`  
`Retained Earnings_FIFO = Retained Earnings_LIFO + [Ending LIFO Reserve * (1 - t)]`  
`Cash adjustment (Cumulative taxes paid under FIFO) = -[Ending LIFO Reserve * t]`  
`Equity_FIFO = Equity_LIFO + [Ending LIFO Reserve * (1 - t)]`  
`Debt-to-Equity_FIFO = Total Debt / Equity_FIFO`

**Step-by-Step Calculation**:
1. Adjust Inventory to FIFO:
   - `Inventory_FIFO = 850,000 USD + 195,000 USD = 1,045,000 USD`
2. Adjust Equity to FIFO:
   - Cumulative after-tax addition to Retained Earnings: `195,000 USD * (1 - 0.25) = 195,000 USD * 0.75 = 146,250 USD`
   - `Equity_FIFO = 2,000,000 USD + 146,250 USD = 2,146,250 USD`
3. Debt remains unchanged at `1,500,000 USD`.
4. Calculate Debt-to-Equity:
   - Original LIFO D/E: `1,500,000 / 2,000,000 = 0.750`
   - Adjusted FIFO D/E: `1,500,000 / 2,146,250 = 0.6989` (or `69.89%`).

**Final Answer**: **FIFO D/E Ratio = 0.70 (or 69.89%)** (leverage decreases under FIFO during rising prices).

---

#### Numerical 3.2.3 (Level: Difficult / LIFO Liquidation)
**Problem Statement**:
Continental Steel experienced a LIFO liquidation in 2025 due to supply chain disruptions. In 2025, Continental sold 100,000 units of steel at 80 USD per unit. During the year, Continental produced only 70,000 units at an average cost of 55 USD per unit. The remaining 30,000 units were liquidated from beginning LIFO inventory base layers, which had an average historical cost of 25 USD per unit. The corporate tax rate is 30%.
Calculate:
1. The reported LIFO COGS and Gross Profit.
2. The pre-tax and after-tax Gross Profit windfall directly attributable to the LIFO liquidation.
3. The adjusted Gross Profit if Continental had not experienced a LIFO liquidation (i.e., if all 100,000 units sold had been produced at the current cost of 55 USD).

**Methodology & Formulas**:
`LIFO COGS = (Current Units Produced * Current Cost) + (Liquidated Units * Historical Cost)`  
`LIFO Liquidation Pre-Tax Windfall = Liquidated Units * (Current Replacement Cost - Historical Layer Cost)`  
`After-Tax Windfall = Pre-Tax Windfall * (1 - t)`  
`Normal (Sustainable) COGS = Total Units Sold * Current Replacement Cost`

**Step-by-Step Calculation**:
1. Reported LIFO COGS & Gross Profit:
   - Cost from current production: `70,000 units * 55 USD = 3,850,000 USD`
   - Cost from liquidated inventory layers: `30,000 units * 25 USD = 750,000 USD`
   - `Total Reported LIFO COGS = 3,850,000 USD + 750,000 USD = 4,600,000 USD`
   - Revenue: `100,000 units * 80 USD = 8,000,000 USD`
   - `Reported Gross Profit = 8,000,000 USD - 4,600,000 USD = 3,400,000 USD`
2. LIFO Liquidation Windfall:
   - Per unit cost distortion: `55 USD (current) - 25 USD (historical) = 30 USD per unit`
   - `Pre-Tax Windfall = 30,000 units * 30 USD = 900,000 USD`
   - `After-Tax Windfall = 900,000 USD * (1 - 0.30) = 630,000 USD`
3. Normalized (Sustainable) Figures:
   - `Normalized COGS = 100,000 * 55 USD = 5,500,000 USD`
   - `Normalized Gross Profit = 8,000,000 USD - 5,500,000 USD = 2,500,000 USD`
   - Notice: `Reported Gross Profit (3,400,000 USD) - Pre-tax Windfall (900,000 USD) = 2,500,000 USD`.

**Final Answer**: **Reported Gross Profit = 3,400,000 USD; Pre-tax Liquidation Windfall = 900,000 USD (After-tax = 630,000 USD); Normalized Gross Profit = 2,500,000 USD**.

---

### Subtopic 3.3: Post-Employment Benefits & Defined Benefit Pensions (L2)

#### Numerical 3.3.1 (Level: Easy / Foundational)
**Problem Statement**:
At the start of 2025, Horizon Corp's Defined Benefit Pension Plan had a Projected Benefit Obligation (PBO) of 12,000,000 USD and Plan Assets of 10,500,000 USD. During 2025:
- Employer contributions paid to the trust: 800,000 USD
- Actual return on plan assets: 950,000 USD
- Benefit payments made to retirees: 600,000 USD
Calculate the fair value of Plan Assets at the end of 2025.

**Methodology & Formulas**:
`Ending Plan Assets = Beginning Plan Assets + Actual Return + Employer Contributions - Benefits Paid`

**Step-by-Step Calculation**:
`Ending Plan Assets = 10,500,000 USD + 950,000 USD + 800,000 USD - 600,000 USD = 11,650,000 USD`

**Final Answer**: **11,650,000 USD**.

---

#### Numerical 3.3.2 (Level: Moderate / Intermediate)
**Problem Statement**:
Omega Energy reports pension accounting under IFRS (IAS 19). At the beginning of 2025:
- Defined Benefit Obligation (DBO) = 25,000,000 EUR
- Fair Value of Plan Assets = 22,000,000 EUR
- Net Pension Liability = 3,000,000 EUR
- Discount rate = 4.0%
During 2025:
- Current service cost = 1,400,000 EUR
- Past service cost (plan amendment) = 300,000 EUR
- Actual return on plan assets = 1,200,000 EUR
- Actuarial loss from changes in demographic assumptions = 500,000 EUR
Calculate:
1. The Net Interest Expense / Income recognized in Profit & Loss (P&L).
2. The Total Periodic Pension Cost recognized in P&L under IFRS.
3. The Remeasurement recognized in Other Comprehensive Income (OCI).

**Methodology & Formulas**:
Under IFRS (IAS 19):
`Net Interest Expense = Net Pension Liability (or Asset) * Discount Rate`  
`P&L Components = Current Service Cost + Past Service Cost + Net Interest Expense`  
`OCI Remeasurement = Actuarial Gains/Losses - (Actual Return - Expected Return based on discount rate)`  
where `Expected Return = Plan Assets * Discount Rate`.

**Step-by-Step Calculation**:
1. Net Interest Expense:
   - `Net Pension Liability = 25,000,000 EUR - 22,000,000 EUR = 3,000,000 EUR`
   - `Net Interest Expense = 3,000,000 EUR * 4.0% = 120,000 EUR`
2. Total Pension Expense in P&L:
   - Current Service Cost: `1,400,000 EUR`
   - Past Service Cost (immediately expensed in P&L under IFRS): `300,000 EUR`
   - Net Interest Expense: `120,000 EUR`
   - `Total P&L Pension Cost = 1,400,000 EUR + 300,000 EUR + 120,000 EUR = 1,820,000 EUR`
3. OCI Remeasurements:
   - Interest income on assets = `22,000,000 EUR * 4.0% = 880,000 EUR`
   - Asset return remeasurement = `Actual Return (1,200,000 EUR) - Expected Return (880,000 EUR) = +320,000 EUR (gain)`
   - Actuarial loss on DBO = `-500,000 EUR (loss)`
   - `Net OCI Remeasurement = -500,000 EUR + 320,000 EUR = -180,000 EUR (net loss in OCI)`

**Final Answer**: **P&L Cost = 1,820,000 EUR; Net OCI Loss = 180,000 EUR** (under IFRS, OCI remeasurements are never recycled to P&L).

---

#### Numerical 3.3.3 (Level: Difficult / US GAAP vs. IFRS Reconciliation)
**Problem Statement**:
Using the exact parameters of Omega Energy above, now assume the company reports under US GAAP (ASC 715) with an Expected Long-Term Rate of Return on Plan Assets (ERR) of 6.5%. Unrecognized prior service costs are amortized over a 10-year expected service life at 30,000 EUR per year. The corridor approach applies for actuarial gains/losses (corridor = 10% of the greater of beginning PBO or Plan Assets).
Calculate:
1. The Periodic Pension Cost recognized in the Income Statement under US GAAP.
2. The exact numerical difference between IFRS P&L pension expense and US GAAP Income Statement pension cost, highlighting why analyst adjustments are necessary.

**Methodology & Formulas**:
US GAAP Income Statement Periodic Pension Cost:
`P&L Cost = Service Cost + Interest Cost on PBO - Expected Return on Plan Assets + Amortization of Prior Service Cost + Amortization of Actuarial Loss (if exceeding corridor)`  
`Interest Cost on PBO = Beginning PBO * Discount Rate`  
`Expected Return on Assets = Beginning Plan Assets * ERR`

**Step-by-Step Calculation**:
1. US GAAP Pension Expense Components:
   - Current Service Cost: `1,400,000 EUR`
   - Interest Cost on PBO: `25,000,000 EUR * 4.0% = 1,000,000 EUR`
   - Expected Return on Plan Assets: `22,000,000 EUR * 6.5% = -1,430,000 EUR`
   - Amortization of Prior Service Cost: `+30,000 EUR`
   - Corridor check: `10% of max(25M, 22M) = 2.5M EUR`. Unamortized net actuarial losses (`500,000 - 320,000 = 180,000 EUR`) are well within the 2,500,000 EUR corridor, so amortization is `0 EUR`.
   - `Total US GAAP P&L Pension Cost = 1,400,000 + 1,000,000 - 1,430,000 + 30,000 = 1,000,000 EUR`
2. Comparative Analysis:
   - IFRS P&L Expense: `1,820,000 EUR`
   - US GAAP P&L Expense: `1,000,000 EUR`
   - **Variance**: US GAAP reports **820,000 EUR lower operating expense** (higher operating profit).
   - Drivers:
     a) Under US GAAP, the full 300,000 EUR prior service cost was capitalized into OCI and amortized at only 30,000 EUR (270,000 EUR difference).
     b) Under US GAAP, an aggressive expected return on assets (6.5% vs. 4.0% discount rate) suppressed expense by `22,000,000 * (6.5% - 4.0%) = 550,000 EUR`.
     c) Total variance: `270,000 EUR + 550,000 EUR = 820,000 EUR`.

**Final Answer**: **US GAAP Pension Cost = 1,000,000 EUR (820,000 EUR lower than IFRS)**.

---

---

## 4. Master Solved Numericals: Fixed Income (FI)

### Subtopic 4.1: Bond Pricing, Accrued Interest & Matrix Pricing

#### Numerical 4.1.1 (Level: Easy / Foundational)
**Problem Statement**:
A 1,000 USD par value, 6.0% annual coupon corporate bond matures exactly 4 years from today. The current market yield-to-maturity (YTM) for comparable risk bonds is 5.2% per annum. Calculate the fair price of the bond.

**Methodology & Formulas**:
`PV = sum_{t=1}^N [ Coupon / (1 + YTM)^t ] + [ Par / (1 + YTM)^N ]`  
Using financial calculator keystrokes:
`N = 4`, `I/Y = 5.2`, `PMT = 60`, `FV = 1000` -> Solve for `PV`.

**Step-by-Step Calculation**:
1. Annual Coupon = `1,000 USD * 0.06 = 60 USD`.
2. Present Value of Annuity of Coupons:
   - Year 1: `60 / (1.052)^1 = 57.034 USD`
   - Year 2: `60 / (1.052)^2 = 54.215 USD`
   - Year 3: `60 / (1.052)^3 = 51.535 USD`
   - Year 4: `60 / (1.052)^4 = 48.988 USD`
   - Sum of Coupons = `211.772 USD`
3. Present Value of Principal:
   - `1,000 / (1.052)^4 = 816.467 USD`
4. Total Bond Price:
   - `Price = 211.772 USD + 816.467 USD = 1,028.239 USD`

**Final Answer**: **1,028.24 USD** (Trading at a premium because Coupon Rate 6.0% > YTM 5.2%).

---

#### Numerical 4.1.2 (Level: Moderate / Full Price vs. Flat Price)
**Problem Statement**:
An 8% semi-annual coupon bond with 1,000 USD par value pays coupons on March 15 and September 15. The bond is settled on June 27, 2025. The stated annual YTM on a semi-annual bond basis is 6.5%. The market convention is 30/360.
The number of days from the last coupon (March 15) to settlement (June 27) is 102 days. The total number of days in the coupon period is 180 days.
There are 8 full semi-annual periods remaining after September 15, 2025 (i.e., total remaining maturity after next coupon is 4 years).
Calculate:
1. The Full (Dirty) Price of the bond per 1,000 USD par.
2. The Accrued Interest (AI).
3. The Flat (Clean) Price of the bond quoted on dealer screens.

**Methodology & Formulas**:
`Fraction of coupon period elapsed (t / T) = 102 / 180 = 0.56667`  
`Semi-annual coupon (PMT) = (8% * 1,000) / 2 = 40 USD`  
`Semi-annual yield (r) = 6.5% / 2 = 3.25% (0.0325)`  
`PV_0 (Value at March 15) = PV of 9 remaining coupons of 40 USD plus 1,000 USD par at 3.25%`  
`Full Price = PV_0 * (1 + r)^(t / T)`  
`Accrued Interest (AI) = PMT * (t / T)`  
`Flat Price = Full Price - Accrued Interest`

**Step-by-Step Calculation**:
1. Calculate `PV_0` on previous coupon date (March 15, 9 periods total):
   - `PV_0 = 40 * [ (1 - (1 + 0.0325)^(-9)) / 0.0325 ] + 1000 * (1 + 0.0325)^(-9)`
   - Annuity Factor = `(1 - 0.74955) / 0.0325 = 7.70615`
   - `PV of Coupons = 40 * 7.70615 = 308.246 USD`
   - `PV of Par = 1000 * 0.74955 = 749.550 USD`
   - `PV_0 = 308.246 + 749.550 = 1,057.796 USD`
2. Full (Dirty) Price on settlement date (June 27):
   - `Full Price = 1,057.796 USD * (1 + 0.0325)^(102 / 180)`
   - `(1.0325)^0.56667 = 1.01832`
   - `Full Price = 1,057.796 * 1.01832 = 1,077.174 USD`
3. Accrued Interest:
   - `AI = 40 USD * (102 / 180) = 22.667 USD`
4. Flat (Clean) Price:
   - `Flat Price = 1,077.174 USD - 22.667 USD = 1,054.507 USD`

**Final Answer**: **Full Price = 1,077.17 USD; Accrued Interest = 22.67 USD; Flat Price = 1,054.51 USD**.

---

#### Numerical 4.1.3 (Level: Difficult / Matrix Pricing Interpolation)
**Problem Statement**:
An illiquid, newly issued 7-year, 5.0% annual coupon corporate bond (Bond X) needs to be priced via matrix pricing. The following liquid benchmark corporate bonds with similar credit ratings are trading in the secondary market:
- Bond A: 5-year maturity, 4.5% coupon, priced at 101.50 (YTM = 4.161%).
- Bond B: 5-year maturity, 6.0% coupon, priced at 107.80 (YTM = 4.238%).
- Bond C: 9-year maturity, 5.2% coupon, priced at 98.20 (YTM = 5.460%).
- Bond D: 9-year maturity, 4.0% coupon, priced at 89.60 (YTM = 5.520%).
Calculate:
1. The estimated 5-year and 9-year benchmark required yields.
2. The interpolated 7-year required yield for Bond X using linear interpolation.
3. The estimated matrix price per 100 par for Bond X.

**Methodology & Formulas**:
`Benchmark YTM_5 = (YTM_A + YTM_B) / 2`  
`Benchmark YTM_9 = (YTM_C + YTM_D) / 2`  
`Linear Interpolation: YTM_7 = YTM_5 + [ (7 - 5) / (9 - 5) ] * (YTM_9 - YTM_5)`  
`Price = sum_{t=1}^7 [ 5 / (1 + YTM_7)^t ] + [ 100 / (1 + YTM_7)^7 ]`

**Step-by-Step Calculation**:
1. Benchmark Average Yields:
   - `5-Year Average YTM = (4.161% + 4.238%) / 2 = 4.1995%`
   - `9-Year Average YTM = (5.460% + 5.520%) / 2 = 5.4900%`
2. Linear Interpolation for 7-Year Maturity:
   - `Spread = 5.4900% - 4.1995% = 1.2905%`
   - `Maturity Fraction = (7 - 5) / (9 - 5) = 2 / 4 = 0.50`
   - `YTM_7 = 4.1995% + (0.50 * 1.2905%) = 4.1995% + 0.64525% = 4.84475% (4.845%)`
3. Price of Bond X (N = 7, PMT = 5, FV = 100, YTM = 4.84475%):
   - Annuity factor for 7 years at 4.84475%:
     `AF = [ 1 - (1.0484475)^(-7) ] / 0.0484475 = (1 - 0.71872) / 0.0484475 = 5.8058`
   - `PV of Coupons = 5 * 5.8058 = 29.029`
   - `PV of Par = 100 * 0.71872 = 71.872`
   - `Price = 29.029 + 71.872 = 100.901`

**Final Answer**: **Interpolated YTM = 4.845%; Estimated Matrix Price = 100.90 per 100 par**.

---

### Subtopic 4.2: Duration, Convexity & PVBP Mechanics

#### Numerical 4.2.1 (Level: Easy / Foundational)
**Problem Statement**:
A portfolio manager holds a 10,000,000 USD par position in a bond trading at 98.50 per 100 par. The bond has a Modified Duration of 6.40 years and an Annualized Convexity of 55.2. Market yields suddenly increase by 75 basis points (0.75%).
Estimate the percentage and dollar price change of the bond using both duration and convexity.

**Methodology & Formulas**:
`Percentage Price Change (% Delta P) = [ -ModDur * Delta Y ] + [ 0.5 * Convexity * (Delta Y)^2 ]`  
`Dollar Price Change (Delta P_dollar) = % Delta P * Current Portfolio Market Value`

**Step-by-Step Calculation**:
1. Duration Effect:
   - `-ModDur * Delta Y = -6.40 * (+0.0075) = -0.0480 (or -4.80%)`
2. Convexity Adjustment:
   - `+0.5 * Convexity * (Delta Y)^2 = 0.5 * 55.2 * (0.0075)^2`
   - `(0.0075)^2 = 0.00005625`
   - `0.5 * 55.2 * 0.00005625 = 27.6 * 0.00005625 = +0.0015525 (or +0.15525%)`
3. Net Percentage Price Change:
   - `% Delta P = -4.80% + 0.15525% = -4.64475%`
4. Dollar Price Change:
   - Current Market Value = `10,000,000 USD * (98.50 / 100) = 9,850,000 USD`
   - `Dollar Loss = 9,850,000 USD * (-0.0464475) = -457,508 USD`

**Final Answer**: **Percentage Price Change = -4.64%; Dollar Value Loss = -457,508 USD**.

---

#### Numerical 4.2.2 (Level: Moderate / Key Rate Duration & Yield Curve Twists)
**Problem Statement**:
An institutional fixed-income portfolio has a market value of 50,000,000 USD with Key Rate Durations (KRD) distributed across four benchmark maturities:
- 2-year KRD = 0.85
- 5-year KRD = 2.10
- 10-year KRD = 4.25
- 30-year KRD = 1.60
Total Effective Duration = `0.85 + 2.10 + 4.25 + 1.60 = 8.80 years`.
The yield curve experiences an asymmetrical steepening twist:
- 2-year yield decreases by 40 bps (-0.40%)
- 5-year yield decreases by 10 bps (-0.10%)
- 10-year yield increases by 25 bps (+0.25%)
- 30-year yield increases by 60 bps (+0.60%)
Calculate:
1. The contribution of each key rate bucket to portfolio return.
2. The total expected percentage change in portfolio market value.
3. The difference between the actual KRD-based return and the naive return obtained using single effective duration with the average curve shift (+8.75 bps).

**Methodology & Formulas**:
`Portfolio % Delta P = -sum(KRD_k * Delta Y_k)`

**Step-by-Step Calculation**:
1. Individual Bucket Contributions:
   - 2-Year Bucket: `-0.85 * (-0.0040) = +0.00340 (or +0.340%)`
   - 5-Year Bucket: `-2.10 * (-0.0010) = +0.00210 (or +0.210%)`
   - 10-Year Bucket: `-4.25 * (+0.0025) = -0.010625 (or -1.0625%)`
   - 30-Year Bucket: `-1.60 * (+0.0060) = -0.00960 (or -0.960%)`
2. Total Portfolio % Change:
   - `% Delta P = +0.340% + 0.210% - 1.0625% - 0.960% = -1.4725%`
   - Total Dollar Impact = `50,000,000 USD * (-0.014725) = -736,250 USD`.
3. Naive Effective Duration Benchmark:
   - Average yield change: `(-40 - 10 + 25 + 60) / 4 = +35 / 4 = +8.75 bps (+0.000875)`
   - Naive estimate: `-8.80 * (+0.000875) = -0.00770 (or -0.770%)`
   - **Variance**: The naive model underestimates the loss by `0.7025%` (a 351,250 USD forecasting error) because the heaviest portfolio exposure (10-year KRD = 4.25) coincided with substantial yield increases.

**Final Answer**: **KRD Portfolio Return = -1.47% (Dollar loss = -736,250 USD); Naive Duration Error = 0.70% (351,250 USD)**.

---

### Subtopic 4.3: Binomial Interest Rate Trees & Embedded Options (L2)

#### Numerical 4.3.1 (Level: Difficult / Backward Induction for Callable Bond)
**Problem Statement**:
A 2-year, 5.0% annual coupon corporate bond with 100 par value is callable at par (100) at the end of Year 1 (immediately after the Year 1 coupon is paid).
The 1-year spot rate today is `r_0 = 3.5%`.
The calibrated 1-year forward rates on the binomial tree at Year 1 are:
- Upper state (higher interest rate): `r_{1,U} = 5.80%`
- Lower state (lower interest rate): `r_{1,D} = 3.90%`
The probability of each state is 0.50.
Calculate:
1. The value of an option-free (straight) bond.
2. The value of the callable bond using backward induction.
3. The embedded call option value held by the issuer.

**Methodology & Formulas**:
`Value at Year 2 = Par + Coupon = 100 + 5 = 105`  
`Straight Value at Year 1 node = (Par + Coupon) / (1 + r_1)`  
`Callable Bond Value at Year 1 node = min(Call Price, (Par + Coupon) / (1 + r_1))`  
`Value at Node 0 = [ 0.5 * (Value_{1,U} + Coupon) + 0.5 * (Value_{1,D} + Coupon) ] / (1 + r_0)`  
`Call Option Value = Value_{straight} - Value_{callable}`

**Step-by-Step Calculation**:
1. Option-Free (Straight) Bond Value:
   - At Node `1,U`: `V_{1,U} = 105 / (1 + 0.0580) = 99.2439`
   - At Node `1,D`: `V_{1,D} = 105 / (1 + 0.0390) = 101.0587`
   - At Node 0:
     `V_0 = [ 0.5 * (99.2439 + 5) + 0.5 * (101.0587 + 5) ] / (1 + 0.035)`
     `V_0 = [ 0.5 * 104.2439 + 0.5 * 106.0587 ] / 1.035 = 105.1513 / 1.035 = 101.5955`
   - `Straight Bond Value = 101.60 per 100 par`.
2. Callable Bond Value (Call Price = 100):
   - At Node `1,U`: Unconstrained value is `99.2439`. Since `99.2439 <= 100`, the issuer will **not call**. Node value = `99.2439`.
   - At Node `1,D`: Unconstrained value is `101.0587`. Since `101.0587 > 100`, the issuer **will exercise the call** at 100! Node value = `100.0000`.
   - At Node 0:
     `V_{callable,0} = [ 0.5 * (99.2439 + 5) + 0.5 * (100.0000 + 5) ] / (1 + 0.035)`
     `V_{callable,0} = [ 0.5 * 104.2439 + 0.5 * 105.0000 ] / 1.035 = 104.62195 / 1.035 = 101.0840`
   - `Callable Bond Value = 101.08 per 100 par`.
3. Embedded Option Value:
   - `Option Value = Value_{straight} - Value_{callable} = 101.5955 - 101.0840 = 0.5115 per 100 par`.

**Final Answer**: **Straight Bond Value = 101.60; Callable Bond Value = 101.08; Embedded Call Option = 0.51 per 100 par**.

---

---

## 5. Master Solved Numericals: Equity Investments (EQ)

### Subtopic 5.1: Margin Transactions & Margin Call Triggers

#### Numerical 5.1.1 (Level: Easy / Foundational)
**Problem Statement**:
An investor buys 1,000 shares of TechCorp on margin at 50 USD per share. The initial margin requirement is 40%, and the maintenance margin requirement is 25%.
Calculate:
1. The initial equity contributed by the investor and the borrowed margin loan.
2. The price at which the investor will receive a margin call.

**Methodology & Formulas**:
`Total Investment = Shares * Initial Price`  
`Initial Equity = Total Investment * Initial Margin %`  
`Margin Loan = Total Investment - Initial Equity`  
`Margin Call Trigger Price (P_call) = P_0 * [ (1 - Initial Margin %) / (1 - Maintenance Margin %) ]`

**Step-by-Step Calculation**:
1. Initial Position:
   - `Total Investment = 1,000 * 50 USD = 50,000 USD`
   - `Initial Equity = 50,000 USD * 0.40 = 20,000 USD`
   - `Margin Loan = 50,000 USD - 20,000 USD = 30,000 USD`
2. Margin Call Trigger Price:
   - `P_call = 50 USD * [ (1 - 0.40) / (1 - 0.25) ]`
   - `P_call = 50 USD * (0.60 / 0.75) = 50 USD * 0.80 = 40.00 USD`
3. Verification:
   - At 40 USD, Total Value = `1,000 * 40 USD = 40,000 USD`.
   - Equity = `40,000 USD - 30,000 USD loan = 10,000 USD`.
   - Equity % = `10,000 USD / 40,000 USD = 25.0%` (exact maintenance threshold).

**Final Answer**: **Initial Equity = 20,000 USD; Margin Call Price = 40.00 USD per share**.

---

#### Numerical 5.1.2 (Level: Moderate / Return on Leveraged Margin Long)
**Problem Statement**:
An investor purchases 500 shares of BioPharm at 80 USD per share using 50% initial margin. The broker charges a call money interest rate of 6.0% per annum on the margin loan. During the 1-year holding period, BioPharm pays a dividend of 2.00 USD per share. At the end of the year, the investor sells the shares at 96 USD per share. The commission paid on purchase is 0.20 USD per share and on sale is 0.20 USD per share.
Calculate the investor's leveraged return on equity investment.

**Methodology & Formulas**:
`Initial Equity = (500 * 80 * 0.50) + (500 * 0.20 commission)`  
`Margin Loan = 500 * 80 * 0.50`  
`Interest Paid = Margin Loan * 6.0%`  
`Total Dividends Received = 500 * 2.00`  
`Net Sales Proceeds = (500 * 96) - (500 * 0.20 commission) - Margin Loan - Interest Paid`  
`Leveraged Return = (Net Sales Proceeds + Dividends - Initial Equity) / Initial Equity`

**Step-by-Step Calculation**:
1. Initial Outflow:
   - Share purchase: `500 * 80 USD = 40,000 USD`
   - Margin Loan: `40,000 USD * 0.50 = 20,000 USD`
   - Initial Equity invested: `20,000 USD + (500 * 0.20 USD) = 20,100 USD`
2. Carrying Costs & Dividends:
   - Margin loan interest: `20,000 USD * 0.06 = 1,200 USD`
   - Dividends received: `500 * 2.00 USD = +1,000 USD`
3. Terminal Liquidation Outflow:
   - Gross sale value: `500 * 96 USD = 48,000 USD`
   - Selling commission: `500 * 0.20 USD = -100 USD`
   - Repay margin loan principal: `-20,000 USD`
   - Repay margin interest: `-1,200 USD`
   - Cash received at sale: `48,000 - 100 - 20,000 - 1,200 = 26,700 USD`
4. Net Total Return:
   - Total Cash Inflow = `26,700 USD + 1,000 USD dividends = 27,700 USD`
   - Profit = `27,700 USD - 20,100 USD initial equity = 7,600 USD`
   - `Return on Equity = 7,600 USD / 20,100 USD = 0.3781 (or 37.81%)`
   - Compare with unleveraged return: `(96 - 80 + 2 - 0.40) / 80.20 = 17.60 / 80.20 = 21.94%`. Leverage increased return by 15.87%!

**Final Answer**: **Leveraged Return on Equity = 37.81%**.

---

### Subtopic 5.2: Dividend Discount Models & Multi-Stage Valuation (L1 & L2)

#### Numerical 5.2.1 (Level: Easy / Gordon Growth & PVGO)
**Problem Statement**:
Crestline Energy currently earns 6.00 USD per share (EPS_1) and pays out 40% of its earnings as dividends. The required rate of return on equity is 10.0%.
1. If the sustainable return on equity (ROE) is 15.0%, calculate the intrinsic value per share using the Gordon Growth Model.
2. Decompose the intrinsic value into the value of assets in place (no-growth value) and the Present Value of Growth Opportunities (PVGO).

**Methodology & Formulas**:
`Retention rate (b) = 1 - Dividend Payout Ratio`  
`Sustainable growth rate (g) = b * ROE`  
`Expected Dividend (D_1) = EPS_1 * Payout Ratio`  
`Intrinsic Value (P_0) = D_1 / (r - g)`  
`No-Growth Value per share = EPS_1 / r`  
`PVGO = P_0 - (EPS_1 / r)`

**Step-by-Step Calculation**:
1. Growth & Dividend:
   - `Retention rate b = 1 - 0.40 = 0.60`
   - `g = 0.60 * 15.0% = 9.0% (0.09)`
   - `D_1 = 6.00 USD * 0.40 = 2.40 USD`
2. Gordon Growth Model Value:
   - `P_0 = 2.40 USD / (0.10 - 0.09) = 2.40 USD / 0.01 = 240.00 USD`
3. PVGO Decomposition:
   - `No-Growth Value = 6.00 USD / 0.10 = 60.00 USD`
   - `PVGO = 240.00 USD - 60.00 USD = 180.00 USD`
   - `PVGO % of Stock Price = 180.00 USD / 240.00 USD = 75.0%`.

**Final Answer**: **Intrinsic Value = 240.00 USD; No-Growth Value = 60.00 USD; PVGO = 180.00 USD (75% of firm value)**.

---

#### Numerical 5.2.2 (Level: Moderate / The H-Model Valuation)
**Problem Statement**:
Apex Semiconductor just paid an annual dividend of `D_0 = 2.50 USD` per share. Due to competitive patent expiration, the current high growth rate of 18.0% (`g_S`) is projected to decline linearly over a transition period of 8 years to a long-term mature sustainable growth rate of 4.0% (`g_L`). The required rate of return for Apex is 9.0%.
Calculate the intrinsic value per share using the Fuller-Hsia H-Model.

**Methodology & Formulas**:
`H = Transition Period (years) / 2`  
`P_0 = [ D_0 * (1 + g_L) / (r - g_L) ] + [ D_0 * H * (g_S - g_L) / (r - g_L) ]`  
or equivalently:  
`P_0 = [ D_0 / (r - g_L) ] * [ (1 + g_L) + H * (g_S - g_L) ]`

**Step-by-Step Calculation**:
1. Parameters:
   - `D_0 = 2.50 USD`
   - `r = 0.09`
   - `g_S = 0.18`
   - `g_L = 0.04`
   - `Transition period = 8 years -> Half-life H = 8 / 2 = 4 years`
   - `Denominator = r - g_L = 0.09 - 0.04 = 0.05`
2. Base Terminal Value Component:
   - `Base Value = [ 2.50 USD * (1 + 0.04) ] / 0.05 = [ 2.50 * 1.04 ] / 0.05 = 2.60 / 0.05 = 52.00 USD`
3. High-Growth Linear Transition Premium Component:
   - `Growth Premium = [ 2.50 USD * 4 * (0.18 - 0.04) ] / 0.05`
   - `2.50 * 4 = 10.00`
   - `10.00 * 0.14 = 1.40 USD`
   - `Growth Premium = 1.40 USD / 0.05 = 28.00 USD`
4. Total H-Model Value:
   - `P_0 = 52.00 USD + 28.00 USD = 80.00 USD per share`.

**Final Answer**: **Intrinsic Value = 80.00 USD per share** (Base value = 52.00 USD, Linear transition excess value = 28.00 USD).

---

#### Numerical 5.2.3 (Level: Difficult / Reverse-Solving H-Model for Implied Return)
**Problem Statement**:
NovaTech stock currently trades in the market at `P_0 = 65.00 USD`. The company just paid a dividend of `D_0 = 1.80 USD`. Equity research consensus projects an initial extraordinary growth rate of `g_S = 16.0%`, declining linearly over a 6-year transition period to a perpetual growth rate of `g_L = 4.5%`.
An analyst wants to determine the market-implied required rate of return (`r`) embedded in NovaTech's current market price. Calculate `r`.

**Methodology & Formulas**:
Rearranging the H-Model equation for `r`:
`P_0 * (r - g_L) = D_0 * [ (1 + g_L) + H * (g_S - g_L) ]`  
`r = g_L + [ (D_0 / P_0) * [ (1 + g_L) + H * (g_S - g_L) ] ]`

**Step-by-Step Calculation**:
1. Parameters:
   - `P_0 = 65.00 USD`
   - `D_0 = 1.80 USD`
   - `g_S = 0.16`
   - `g_L = 0.045`
   - `Transition period = 6 years -> H = 6 / 2 = 3`
2. Calculate the dividend adjustment factor:
   - `Base factor = 1 + g_L = 1 + 0.045 = 1.045`
   - `Excess growth factor = H * (g_S - g_L) = 3 * (0.16 - 0.045) = 3 * 0.115 = 0.345`
   - `Total multiplier = 1.045 + 0.345 = 1.390`
3. Solve for `r`:
   - `Effective Adjusted Dividend = 1.80 USD * 1.390 = 2.502 USD`
   - `Spread over g_L = 2.502 USD / 65.00 USD = 0.038492 (or 3.849%)`
   - `r = g_L + 3.849% = 4.50% + 3.849% = 8.349% (8.35%)`

**Final Answer**: **Market-Implied Required Rate of Return r = 8.35%**.

---

### Subtopic 5.3: Free Cash Flow Valuation (FCFF & FCFE Bridges)

#### Numerical 5.3.1 (Level: Difficult / Comprehensive FCFF to FCFE Reconciliation)
**Problem Statement**:
Zeta Corp reported the following financial statement figures for fiscal year 2025:
- Net Income = 450,000 USD
- Non-Cash Charges (Depreciation & Amortization) = 180,000 USD
- Capital Expenditures (FCInv) = 220,000 USD
- Increase in Working Capital (WCInv) = 45,000 USD
- Interest Expense = 80,000 USD
- Corporate Tax Rate = 25%
- Long-term debt issued during year = 120,000 USD
- Long-term debt retired during year = 50,000 USD
- Target Debt-to-Capital Ratio = 35%
Calculate:
1. Free Cash Flow to the Firm (FCFF) starting from Net Income.
2. Free Cash Flow to Equity (FCFE) starting from FCFF.
3. Verify FCFE starting directly from Net Income.

**Methodology & Formulas**:
`FCFF = Net Income + Non-Cash Charges + [ Interest * (1 - t) ] - FCInv - WCInv`  
`Net Borrowing = Debt Issued - Debt Repaid`  
`FCFE = FCFF - [ Interest * (1 - t) ] + Net Borrowing`  
`Direct FCFE = Net Income + Non-Cash Charges - FCInv - WCInv + Net Borrowing`

**Step-by-Step Calculation**:
1. Calculate FCFF:
   - `Net Income = 450,000 USD`
   - `+ Non-Cash Charges = +180,000 USD`
   - `+ After-tax Interest = 80,000 USD * (1 - 0.25) = +60,000 USD`
   - `- Fixed Capital Investment (FCInv) = -220,000 USD`
   - `- Working Capital Investment (WCInv) = -45,000 USD`
   - `FCFF = 450,000 + 180,000 + 60,000 - 220,000 - 45,000 = 425,000 USD`
2. Calculate FCFE from FCFF:
   - `Net Borrowing = 120,000 USD (issued) - 50,000 USD (retired) = +70,000 USD`
   - `FCFE = 425,000 USD - 60,000 USD (after-tax interest) + 70,000 USD (net borrowing)`
   - `FCFE = 435,000 USD`
3. Direct Verification:
   - `Direct FCFE = 450,000 (NI) + 180,000 (NCC) - 220,000 (FCInv) - 45,000 (WCInv) + 70,000 (Net Borrowing)`
   - `Direct FCFE = 630,000 - 265,000 + 70,000 = 435,000 USD` (Exact reconciliation verified).

**Final Answer**: **FCFF = 425,000 USD; FCFE = 435,000 USD**.

---

---

## 6. Master Solved Numericals: Portfolio Management (PM)

### Subtopic 6.1: Return & Risk Mechanics (MWR, TWR & Multi-Asset Variance)

#### Numerical 6.1.1 (Level: Easy / MWR vs. TWR)
**Problem Statement**:
An investor opens a brokerage account on January 1, 2025:
- Jan 1, 2025: Deposits 100,000 USD and purchases shares.
- June 30, 2025: Portfolio value is 120,000 USD (prior to deposit). Investor deposits an additional 50,000 USD cash (new total value = 170,000 USD).
- Dec 31, 2025: Portfolio value is 153,000 USD.
Calculate:
1. The Time-Weighted Return (TWR) for 2025.
2. The Money-Weighted Return (MWR / IRR) for 2025.
3. Explain which metric accurately evaluates the manager's investment performance.

**Methodology & Formulas**:
`HPR_1 = (End Value_1 - Beginning Value_1) / Beginning Value_1`  
`HPR_2 = (End Value_2 - (Beginning Value_2 + Deposit)) / (Beginning Value_2 + Deposit)`  
`1 + TWR = (1 + HPR_1) * (1 + HPR_2)`  
`MWR (IRR): PV(Outflows) = PV(Inflows)`  
`100,000 USD + [ 50,000 USD / (1 + r)^0.5 ] = 153,000 USD / (1 + r)`

**Step-by-Step Calculation**:
1. Time-Weighted Return (TWR):
   - Period 1 (Jan 1 to June 30):
     `HPR_1 = (120,000 - 100,000) / 100,000 = +20.0% (+0.20)`
   - Period 2 (June 30 to Dec 31):
     Portfolio starting base = `120,000 + 50,000 = 170,000 USD`
     `HPR_2 = (153,000 - 170,000) / 170,000 = -17,000 / 170,000 = -10.0% (-0.10)`
   - Full Year TWR:
     `1 + TWR = (1 + 0.20) * (1 - 0.10) = 1.20 * 0.90 = 1.080`
     `TWR = +8.0% (0.08)`
2. Money-Weighted Return (MWR / IRR):
   - Cash Flow 0 (Jan 1): `-100,000 USD`
   - Cash Flow 0.5 (June 30): `-50,000 USD`
   - Cash Flow 1.0 (Dec 31): `+153,000 USD`
   - Set up semi-annual discount equation:
     `100,000 + [ 50,000 / (1 + r_{semi}) ] = 153,000 / (1 + r_{semi})^2`
     Let `x = 1 / (1 + r_{semi})`:
     `153,000 * x^2 - 50,000 * x - 100,000 = 0`
     Divide by 1,000: `153 * x^2 - 50 * x - 100 = 0`
     Using quadratic formula:
     `x = [ 50 + sqrt((-50)^2 - 4 * 153 * (-100)) ] / (2 * 153)`
     `sqrt(2500 + 61,200) = sqrt(63,700) = 252.388`
     `x = (50 + 252.388) / 306 = 302.388 / 306 = 0.98820`
     `1 + r_{semi} = 1 / 0.98820 = 1.01194 -> r_{semi} = 1.194%`
     Annualized compounded MWR = `(1 + 0.01194)^2 - 1 = 1.0240 - 1 = +2.40%`
3. Performance Evaluation Context:
   - `TWR = +8.0%` vs. `MWR = +2.40%`.
   - The manager generated an 8.0% return on invested assets. The MWR is drastically lower (+2.40%) solely because the **client deposited 50,000 USD right before the market declined 10%**.
   - Because investment managers typically do not control client cash deposit/withdrawal timing, GIPS mandates **TWR** for evaluating portfolio manager skill!

**Final Answer**: **Time-Weighted Return (TWR) = +8.0%; Money-Weighted Return (MWR) = +2.40%**.

---

#### Numerical 6.1.2 (Level: Moderate / Three-Asset Portfolio Variance Expansion)
**Problem Statement**:
An institutional endowment allocates its fund across three asset classes:
- US Large-Cap Equities (Asset 1): Weight `w_1 = 0.50`, Standard Deviation `sigma_1 = 18.0%`
- Global Developed Bonds (Asset 2): Weight `w_2 = 0.35`, Standard Deviation `sigma_2 = 7.0%`
- Private Real Estate (Asset 3): Weight `w_3 = 0.15`, Standard Deviation `sigma_3 = 12.0%`
The correlation matrix `rho_{i,j}` between the asset classes is:
- `rho_{1,2} = -0.15` (Equities vs. Bonds)
- `rho_{1,3} = +0.45` (Equities vs. Real Estate)
- `rho_{2,3} = +0.05` (Bonds vs. Real Estate)
Calculate:
1. The Covariance between each pair of asset classes.
2. The total Portfolio Variance (`sigma_p^2`) and Portfolio Standard Deviation (`sigma_p`).

**Methodology & Formulas**:
`Cov(i, j) = rho_{i, j} * sigma_i * sigma_j`  
`Portfolio Variance (sigma_p^2) = sum_{i=1}^3 (w_i^2 * sigma_i^2) + 2 * sum_{i < j} (w_i * w_j * Cov(i, j))`

**Step-by-Step Calculation**:
1. Pairwise Covariances:
   - `Cov(1, 2) = -0.15 * 0.18 * 0.07 = -0.001890`
   - `Cov(1, 3) = +0.45 * 0.18 * 0.12 = +0.009720`
   - `Cov(2, 3) = +0.05 * 0.07 * 0.12 = +0.000420`
2. Weighted Individual Variances:
   - Asset 1: `(0.50)^2 * (0.18)^2 = 0.25 * 0.0324 = 0.008100`
   - Asset 2: `(0.35)^2 * (0.07)^2 = 0.1225 * 0.0049 = 0.000600`
   - Asset 3: `(0.15)^2 * (0.12)^2 = 0.0225 * 0.0144 = 0.000324`
   - `Sum of individual terms = 0.008100 + 0.000600 + 0.000324 = 0.009024`
3. Weighted Cross-Product Covariances (multiplied by 2):
   - Term 1,2: `2 * 0.50 * 0.35 * (-0.001890) = 0.35 * (-0.001890) = -0.0006615`
   - Term 1,3: `2 * 0.50 * 0.15 * (+0.009720) = 0.15 * (+0.009720) = +0.0014580`
   - Term 2,3: `2 * 0.35 * 0.15 * (+0.000420) = 0.105 * (+0.000420) = +0.0000441`
   - `Sum of covariance terms = -0.0006615 + 0.0014580 + 0.0000441 = +0.0008406`
4. Total Portfolio Variance & Volatility:
   - `sigma_p^2 = 0.009024 + 0.0008406 = 0.0098646`
   - `sigma_p = sqrt(0.0098646) = 0.09932 (or 9.93%)`
   - Notice: Weighted average standard deviation = `0.50 * 18% + 0.35 * 7% + 0.15 * 12% = 9.0% + 2.45% + 1.8% = 13.25%`. Diversification reduced portfolio risk from 13.25% to 9.93%!

**Final Answer**: **Portfolio Variance = 0.009865; Portfolio Standard Deviation = 9.93%**.

---

### Subtopic 6.2: The Fundamental Law of Active Management (Grinold's Rule) (L2)

#### Numerical 6.2.1 (Level: Moderate / Unconstrained Fundamental Law)
**Problem Statement**:
An equity long-only quantitative manager follows an unconstrained stock selection strategy (`Transfer Coefficient TC = 1.0`):
- Number of independent stock return forecasts per year (`Breadth BR`) = 400 stocks
- Information Coefficient per stock forecast (`IC`) = 0.06
- Benchmark Sharpe Ratio (`SR_B`) = 0.40
- Benchmark Standard Deviation (`sigma_B`) = 15.0%
Calculate:
1. The Information Ratio (IR) of the active manager.
2. The expected maximum active return (`E(R_A)`) if active risk (`sigma_A`) is budgeted at 4.0%.
3. The Sharpe Ratio of the actively managed portfolio (`SR_P`).

**Methodology & Formulas**:
Grinold's Fundamental Law of Active Management:
`IR = TC * IC * sqrt(BR)` (where `TC = 1.0` for unconstrained portfolios)  
`Expected Active Return E(R_A) = IR * sigma_A`  
`Sharpe Ratio Expansion: SR_P = sqrt(SR_B^2 + IR^2)`

**Step-by-Step Calculation**:
1. Information Ratio (IR):
   - `sqrt(BR) = sqrt(400) = 20`
   - `IR = 1.0 * 0.06 * 20 = 1.20`
2. Expected Active Return:
   - For `sigma_A = 4.0%`:
   - `E(R_A) = 1.20 * 4.0% = 4.80% (0.048)`
3. Portfolio Total Sharpe Ratio:
   - `SR_B^2 = (0.40)^2 = 0.16`
   - `IR^2 = (1.20)^2 = 1.44`
   - `SR_P^2 = 0.16 + 1.44 = 1.60`
   - `SR_P = sqrt(1.60) = 1.2649 (1.26)`

**Final Answer**: **Information Ratio IR = 1.20; Expected Active Return = 4.80%; Portfolio Sharpe Ratio = 1.26**.

---

#### Numerical 6.2.2 (Level: Difficult / Constrained Fundamental Law & Optimal Active Risk)
**Problem Statement**:
A real-world portfolio manager is subject to long-only constraints, sector neutrality caps, and turnover limits, resulting in a Transfer Coefficient `TC = 0.65`.
The manager covers an investment universe of `BR = 196` independent decisions per year with skill `IC = 0.08`.
The benchmark Sharpe Ratio is `SR_B = 0.45`.
Calculate:
1. The constrained Information Ratio (`IR_constrained`).
2. The optimal active risk (`sigma_A^*`) the manager should target if the benchmark volatility `sigma_B = 16.0%`.
3. The resulting total portfolio Sharpe Ratio (`SR_P`).

**Methodology & Formulas**:
`IR_constrained = TC * IC * sqrt(BR)`  
`Optimal Active Risk sigma_A^* = (IR / SR_B) * sigma_B * TC` (or `sigma_A^* = (IR_constrained / SR_B) * sigma_B`)  
`SR_P = sqrt(SR_B^2 + IR_constrained^2)`

**Step-by-Step Calculation**:
1. Constrained Information Ratio:
   - `sqrt(BR) = sqrt(196) = 14`
   - Unconstrained IR = `0.08 * 14 = 1.12`
   - `IR_constrained = 0.65 * 1.12 = 0.728`
2. Optimal Active Risk:
   - `sigma_A^* = (IR_constrained / SR_B) * sigma_B`
   - `sigma_A^* = (0.728 / 0.45) * 16.0% = 1.6178 * 16.0% = 25.88%`
   - Note: If constrained active risk is capped by the investment mandate (e.g., at `sigma_A = 5.0%`), expected active return would be:
     `E(R_A) = IR_constrained * sigma_A = 0.728 * 5.0% = 3.64%`.
3. Constrained Sharpe Ratio Expansion:
   - `SR_P = sqrt((0.45)^2 + (0.728)^2) = sqrt(0.2025 + 0.52998) = sqrt(0.73248) = 0.8558 (0.86)`

**Final Answer**: **Constrained IR = 0.73; Optimal Active Risk = 25.88%; Portfolio Sharpe Ratio = 0.86**.

---

### Subtopic 6.3: Trade Execution & Implementation Shortfall (L2)

#### Numerical 6.3.1 (Level: Difficult / Perold 4-Component Implementation Shortfall)
**Problem Statement**:
A portfolio manager decides to buy 50,000 shares of Meridian Tech.
- **Decision Date (Monday 9:30 AM)**: Benchmark Decision Price = `50.00 USD`.
- Order is released to the trading desk at 11:00 AM when the market price is `50.60 USD` (Arrival Price).
- **Execution Day 1 (Monday)**: Desk buys 30,000 shares at an average execution price of `51.20 USD`. Explicit commission is `0.05 USD` per share.
- Monday closing price is `51.50 USD`.
- **Execution Day 2 (Tuesday)**: Desk buys 12,000 shares at an average execution price of `52.10 USD`. Explicit commission is `0.05 USD` per share.
- Tuesday closing price is `52.80 USD`.
- **Cancellation**: The manager cancels the remaining 8,000 shares on Tuesday afternoon as the price has run away.
Calculate the total Implementation Shortfall in dollars and basis points, and decompose it into its 4 distinct components:
1. Explicit Fees (Commissions)
2. Execution Cost (Delay / Market Impact on filled shares relative to Arrival Price)
3. Delay Cost (Slippage from decision time to order release time)
4. Opportunity Cost (Cost of unfilled / cancelled shares)

**Methodology & Formulas**:
`Paper Portfolio Return = Total Target Shares * (Closing Price - Decision Price)`  
`Actual Portfolio Return = sum(Executed Shares_d * Closing Price) - sum(Executed Shares_d * Execution Price_d) - Total Commissions`  
`Total Implementation Shortfall (IS) = Paper Return - Actual Return`  
Component Breakdown:
1. `Explicit Costs = sum(Executed Shares_d * Commission_per_share)`
2. `Delay Cost = Total Executed Shares * (Arrival Price - Decision Price)`
3. `Realized Execution Cost = sum(Executed Shares_d * (Execution Price_d - Arrival Price))`
4. `Opportunity Cost (Unfilled) = Unfilled Shares * (Final Cancellation Price - Decision Price)`

**Step-by-Step Calculation**:
1. Total Target Shares = `50,000`; Decision Price = `50.00 USD`.
   - Total base capital = `50,000 * 50.00 USD = 2,500,000 USD`.
2. Total Executed Shares = `30,000 + 12,000 = 42,000 shares`.
   - Unfilled Shares = `50,000 - 42,000 = 8,000 shares`.
3. Component Calculations:
   - **Component 1: Explicit Costs**:
     - `42,000 shares * 0.05 USD = 2,100 USD` (or `2,100 / 2,500,000 = 8.4 bps`).
   - **Component 2: Delay Cost (Between Decision Price 50.00 and Arrival Price 50.60)**:
     - `Executed Shares * (Arrival Price - Decision Price)`
     - `42,000 * (50.60 USD - 50.00 USD) = 42,000 * 0.60 USD = 25,200 USD` (or `25,200 / 2,500,000 = 100.8 bps`).
   - **Component 3: Realized Execution Cost (Market Impact above Arrival Price 50.60)**:
     - Day 1: `30,000 * (51.20 USD - 50.60 USD) = 30,000 * 0.60 USD = 18,000 USD`
     - Day 2: `12,000 * (52.10 USD - 50.60 USD) = 12,000 * 1.50 USD = 18,000 USD`
     - `Total Execution Cost = 18,000 USD + 18,000 USD = 36,000 USD` (or `36,000 / 2,500,000 = 144.0 bps`).
   - **Component 4: Opportunity Cost (Unfilled Shares 8,000)**:
     - Final Benchmark Price at cancellation (Tuesday close) = `52.80 USD`.
     - `8,000 shares * (52.80 USD - 50.00 USD) = 8,000 * 2.80 USD = 22,400 USD` (or `22,400 / 2,500,000 = 89.6 bps`).
4. Total Implementation Shortfall Reconciliation:
   - `Total IS = 2,100 USD (Explicit) + 25,200 USD (Delay) + 36,000 USD (Execution) + 22,400 USD (Opportunity)`
   - `Total IS = 85,700 USD`
   - In basis points: `85,700 USD / 2,500,000 USD = 0.03428 (or 342.8 bps)`.
   - Verification via Paper Portfolio:
     - Paper Profit = `50,000 * (52.80 - 50.00) = 140,000 USD`.
     - Actual Profit = `(42,000 * 52.80) - (30,000 * 51.20) - (12,000 * 52.10) - 2,100`
     - Actual Profit = `2,217,600 - 1,536,000 - 625,200 - 2,100 = 54,300 USD`.
     - `Shortfall = Paper Profit (140,000 USD) - Actual Profit (54,300 USD) = 85,700 USD` (Reconciliation matches down to the dollar!).

**Final Answer**: **Total Implementation Shortfall = 85,700 USD (342.8 bps)**:
- **Explicit Commissions**: 2,100 USD (8.4 bps)
- **Delay Cost**: 25,200 USD (100.8 bps)
- **Realized Execution Cost**: 36,000 USD (144.0 bps)
- **Opportunity Cost**: 22,400 USD (89.6 bps).

---

### Subtopic 6.4: Performance Attribution (Brinson-Fachler Multi-Period Model) (L2)

#### Numerical 6.4.1 (Level: Difficult / Sector Allocation vs. Stock Selection)
**Problem Statement**:
An active equity portfolio and its benchmark have returns and weights across three sectors over a quarterly evaluation period:

| Sector | Portfolio Weight (`w_i`) | Benchmark Weight (`W_i`) | Portfolio Return (`R_i`) | Benchmark Return (`B_i`) |
| :--- | :---: | :---: | :---: | :---: |
| Technology | 45.0% | 30.0% | 14.0% | 12.0% |
| Financials | 25.0% | 35.0% | 6.0% | 5.0% |
| Healthcare | 30.0% | 35.0% | -2.0% | 1.0% |
| **Total / Benchmark** | **100.0%** | **100.0%** | — | — |

Calculate:
1. The total return of the benchmark (`R_B`) and the portfolio (`R_P`).
2. The Active Return (`R_P - R_B`).
3. Decompose the Active Return using the **Brinson-Fachler model** into:
   - Sector Allocation Effect
   - Within-Sector Selection Effect
   - Interaction Effect.

**Methodology & Formulas**:
`Benchmark Return R_B = sum(W_i * B_i)`  
`Portfolio Return R_P = sum(w_i * R_i)`  
Brinson-Fachler Attribution Formulas:
`Allocation Effect (A_i) = (w_i - W_i) * (B_i - R_B)`  
`Selection Effect (S_i) = W_i * (R_i - B_i)`  
`Interaction Effect (I_i) = (w_i - W_i) * (R_i - B_i)`  
`Active Return = sum(A_i) + sum(S_i) + sum(I_i)`

**Step-by-Step Calculation**:
1. Portfolio and Benchmark Total Returns:
   - Benchmark: `(0.30 * 12%) + (0.35 * 5%) + (0.35 * 1%) = 3.60% + 1.75% + 0.35% = 5.70% (0.057)`
   - Portfolio: `(0.45 * 14%) + (0.25 * 6%) + (0.30 * -2%) = 6.30% + 1.50% - 0.60% = 7.20% (0.072)`
   - `Active Return = 7.20% - 5.70% = +1.50% (+0.0150 or +150 bps)`
2. Allocation Effect (Brinson-Fachler: Evaluates over/underweighting relative to overall benchmark return `R_B = 5.70%`):
   - Tech: `(0.45 - 0.30) * (12.0% - 5.70%) = +0.15 * (+6.30%) = +0.9450% (+94.5 bps)`
   - Financials: `(0.25 - 0.35) * (5.0% - 5.70%) = -0.10 * (-0.70%) = +0.0700% (+7.0 bps)`
   - Healthcare: `(0.30 - 0.35) * (1.0% - 5.70%) = -0.05 * (-4.70%) = +0.2350% (+23.5 bps)`
   - `Total Allocation Effect = +0.9450% + 0.0700% + 0.2350% = +1.2500% (+125 bps)`
3. Selection Effect:
   - Tech: `0.30 * (14.0% - 12.0%) = 0.30 * (+2.0%) = +0.6000% (+60.0 bps)`
   - Financials: `0.35 * (6.0% - 5.0%) = 0.35 * (+1.0%) = +0.3500% (+35.0 bps)`
   - Healthcare: `0.35 * (-2.0% - 1.0%) = 0.35 * (-3.0%) = -1.0500% (-105.0 bps)`
   - `Total Selection Effect = +0.6000% + 0.3500% - 1.0500% = -0.1000% (-10 bps)`
4. Interaction Effect:
   - Tech: `(0.45 - 0.30) * (14.0% - 12.0%) = +0.15 * (+2.0%) = +0.3000% (+30.0 bps)`
   - Financials: `(0.25 - 0.35) * (6.0% - 5.0%) = -0.10 * (+1.0%) = -0.1000% (-10.0 bps)`
   - Healthcare: `(0.30 - 0.35) * (-2.0% - 1.0%) = -0.05 * (-3.0%) = +0.1500% (+15.0 bps)`
   - `Total Interaction Effect = +0.3000% - 0.1000% + 0.1500% = +0.3500% (+35 bps)`
5. Verification:
   - `Sum = +1.25% (Allocation) - 0.10% (Selection) + 0.35% (Interaction) = +1.50%` (Exact match with active return).

**Final Answer**: **Active Return = +150 bps (+1.50%)**:
- **Allocation Effect**: +125 bps (+1.25%) -> Driven primarily by a strong overweight in outperforming Technology.
- **Selection Effect**: -10 bps (-0.10%) -> Good tech and bank selection was offset by severe healthcare stock underperformance.
- **Interaction Effect**: +35 bps (+0.35%).

---

---

## 7. Authoritative Curriculum Mapping Tables (Official CFAI 2024–2026 vs. Schweser & UWorld)

### 7.1 Financial Statement Analysis (FSA) Comprehensive Mapping
| Level | CFAI Official Learning Module (LM) | Kaplan Schweser Reading | UWorld / Wiley Module | Critical Calculation & Concept Focus | Current Platform Status |
| :---: | :--- | :--- | :--- | :--- | :---: |
| **L1** | LM 1: Introduction to FSA | Book 2, Module 13 | Module 1: 6-Step Framework | Audit opinion types, MD&A, 10-K disclosures | **Fully Covered** |
| **L1** | LM 2: Analyzing Income Statements | Book 2, Module 14 | Module 2: Revenue & EPS | ASC 606 5-step model, Basic & Diluted EPS | **Fully Covered** |
| **L1** | LM 3: Analyzing Balance Sheets | Book 2, Module 15 | Module 3: Balance Sheet | Fair value vs. historical cost, Off-balance sheet | **Fully Covered** |
| **L1** | LM 4: Cash Flows Part I | Book 2, Module 16 | Module 4: Cash Flow Direct | CFO indirect vs. direct conversion | **Fully Covered** |
| **L1** | LM 5: Cash Flows Part II | Book 2, Module 17 | Module 5: Free Cash Flow | FCFF, FCFE, CFO coverage ratios | **Fully Covered** |
| **L1** | LM 6: Analysis of Inventories | Book 2, Module 18 | Module 6: FIFO & LIFO | LIFO reserve, LIFO liquidation, NRV | **Fully Covered** |
| **L1** | LM 7: Analysis of Long-Term Assets | Book 2, Module 19 | Module 7: Capitalization | Revaluation surplus, Impairment rules | **Fully Covered** |
| **L1** | LM 8: Income Taxes | Book 2, Module 20 | Module 8: Deferred Taxes | DTA, DTL, Valuation allowances, Rate changes | **Fully Covered** |
| **L1** | LM 9: Non-Current Liabilities | Book 2, Module 21 | Module 9: Long-Term Debt | Effective interest amortization, Debt retirement | **Fully Covered** |
| **L1** | LM 10: Leases | Book 2, Module 22 | Module 10: IFRS 16 / ASC 842 | Operating vs. Finance lease balance sheet impacts | **Fully Covered** |
| **L1** | LM 11: Financial Reporting Quality | Book 2, Module 23 | Module 11: Earnings Quality | Accrual anomalies, Warning signs, Manipulation | **Fully Covered** |
| **L1** | LM 12: Financial Statement Modeling | Book 2, Module 24 | Module 12: Forecasting | 3-Statement modeling, Behavioral forecast | **Gap Addressed** |
| **L2** | LM 1: Intercorporate Investments | Book 2, Topic 1 | Intercorporate Holdings | FVPL, FVOCI, Equity Method, Acquisition Method | **Fully Covered** |
| **L2** | LM 2: Employee Compensation | Book 2, Topic 2 | Post-Employment Benefits | PBO, Plan Assets, US GAAP vs. IFRS pension cost | **Fully Covered** |
| **L2** | LM 3: Multinational Operations | Book 2, Topic 3 | FX Financial Translation | Current Rate vs. Temporal, CTA, Hyperinflation | **Fully Covered** |
| **L2** | LM 4: Analysis of Financial Institutions | Book 2, Topic 4 | Banks & Insurance | CAMELS, Basel III, LCR, NSFR, Loss reserves | **Fully Covered** |
| **L2** | LM 5: Evaluating Reporting Quality | Book 2, Topic 5 | Accounting Quality Models | Beneish M-score, Cash flow quality, Accruals | **Fully Covered** |
| **L2** | LM 6: Integration of FSA Techniques | Book 2, Topic 6 | Financial Statement Synthesis | Multi-statement normalization & adjustments | **Fully Covered** |

---

### 7.2 Fixed Income (FI) Comprehensive Mapping
| Level | CFAI Official Learning Module (LM) | Kaplan Schweser Reading | UWorld / Wiley Module | Critical Calculation & Concept Focus | Current Platform Status |
| :---: | :--- | :--- | :--- | :--- | :---: |
| **L1** | LM 1: Instrument Features | Book 4, Module 31 | Fixed Income Essentials | Indentures, Affirmative/Negative Covenants | **Fully Covered** |
| **L1** | LM 2: Cash Flow Structures | Book 4, Module 32 | Bond Cash Flow Types | Amortizing, Sinking fund, Step-up, FRNs | **Fully Covered** |
| **L1** | LM 3: Issuance & Trading | Book 4, Module 33 | Fixed Income Markets | Sovereign, Non-sovereign, Repos, Commercial paper | **Fully Covered** |
| **L1** | LM 4: Valuation: Prices & Yields | Book 4, Module 34 | Pricing & Spot Rates | Bond pricing formula, Spot curves, Matrix pricing | **Fully Covered** |
| **L1** | LM 5: Yield & Spread Measures | Book 4, Module 35 | Yield Measures & Spreads | YTM, Street convention, G-spread, I-spread, Z-spread | **Fully Covered** |
| **L1** | LM 6: Fixed-Income Risk & Return | Book 4, Module 36 | Duration & Convexity | Macaulay duration, Modified duration, PVBP | **Fully Covered** |
| **L1** | LM 7: Yield Curve & Term Structure | Book 4, Module 37 | Term Structure Analysis | Bootstrapping, Forward pricing, Spot parities | **Fully Covered** |
| **L1** | LM 8: Credit Analysis Fundamentals | Book 4, Module 38 | Credit Risk Fundamentals | 4 Cs, Credit ratings, Expected loss | **Fully Covered** |
| **L1** | LM 9: Overview of Securitization | Book 4, Module 39 | Securitization & MBS | CMO tranches, SMM, CPR, Prepayment risk | **Fully Covered** |
| **L2** | LM 1: Term Structure & Dynamics | Book 4, Topic 1 | Interest Rate Dynamics | Yield curve shifts, Shifts/Twists, Vasicek, CIR | **Gap Addressed** |
| **L2** | LM 2: Arbitrage-Free Valuation | Book 4, Topic 2 | Arbitrage-Free Framework | Binomial tree calibration, Backward induction | **Fully Covered** |
| **L2** | LM 3: Bonds with Embedded Options | Book 4, Topic 3 | Embedded Options | Callable & Puttable bonds, OAS, Effective convexity | **Fully Covered** |
| **L2** | LM 4: Credit Analysis Models | Book 4, Topic 4 | Credit Risk Modeling | Merton structural model, Reduced-form models | **Fully Covered** |
| **L2** | LM 5: Credit Default Swaps (CDS) | Book 4, Topic 5 | CDS Mechanics & Pricing | CDS upfront payment, Basis trading, Curve trades | **Gap Addressed** |

---

### 7.3 Equity Investments (EQ) Comprehensive Mapping
| Level | CFAI Official Learning Module (LM) | Kaplan Schweser Reading | UWorld / Wiley Module | Critical Calculation & Concept Focus | Current Platform Status |
| :---: | :--- | :--- | :--- | :--- | :---: |
| **L1** | LM 1: Market Organization | Book 3, Module 25 | Market Structure | Order types, Leverage ratio, Margin call price | **Fully Covered** |
| **L1** | LM 2: Security Market Indices | Book 3, Module 26 | Index Construction | Price-weighted, Cap-weighted, Equal-weighted | **Fully Covered** |
| **L1** | LM 3: Market Efficiency | Book 3, Module 27 | Efficient Markets | Weak, Semi-strong, Strong forms, Anomalies | **Fully Covered** |
| **L1** | LM 4: Overview of Equity Securities | Book 3, Module 28 | Equity Securities | Common vs. Preferred shares, Depository receipts | **Fully Covered** |
| **L1** | LM 5: Company Analysis: Past & Present | Book 3, Module 29 | Historical Analysis | Financial performance, ROE DuPont decomposition | **Fully Covered** |
| **L1** | LM 6: Industry & Competitive Analysis | Book 3, Module 30 | Industry Frameworks | Porter's 5 Forces, Industry life cycle stages | **Fully Covered** |
| **L1** | LM 7: Equity Valuation: Basic Tools | Book 3, Module 31 | Valuation Fundamentals | Gordon Growth Model, Multipliers, Asset-based | **Fully Covered** |
| **L2** | LM 1: Valuation Applications | Book 3, Topic 1 | Equity Valuation Process | Top-down vs. Bottom-up, Valuation purpose | **Fully Covered** |
| **L2** | LM 2: Discounted Dividend Valuation | Book 3, Topic 2 | DDM & Multi-Stage | Gordon Growth, Multi-stage DDM, H-Model | **Fully Covered** |
| **L2** | LM 3: Free Cash Flow Valuation | Book 3, Topic 3 | FCFF & FCFE Models | FCFF & FCFE bridges from NI, CFO, EBIT, EBITDA | **Fully Covered** |
| **L2** | LM 4: Market-Based Valuation | Book 3, Topic 4 | Price & EV Multiples | Justified P/E, P/B, P/S, EV/EBITDA, EV/Sales | **Fully Covered** |
| **L2** | LM 5: Residual Income Valuation | Book 3, Topic 5 | Residual Income Models | Single-stage RI, Multi-stage RI with persistence | **Fully Covered** |
| **L2** | LM 6: Private Company Valuation | Book 3, Topic 6 | Private Valuation | Excess Earnings Method, DLOC, DLOM | **Gap Addressed** |

---

### 7.4 Portfolio Management (PM) Comprehensive Mapping
| Level | CFAI Official Learning Module (LM) | Kaplan Schweser Reading | UWorld / Wiley Module | Critical Calculation & Concept Focus | Current Platform Status |
| :---: | :--- | :--- | :--- | :--- | :---: |
| **L1** | LM 1: Portfolio Management Overview | Book 5, Module 40 | Portfolio Approach | Diversification benefit, Institutional investor matrix | **Fully Covered** |
| **L1** | LM 2: Risk and Return: Part I | Book 5, Module 41 | Portfolio Math & Frontier | MWR vs. TWR, 2-Asset & 3-Asset variance, MVF | **Fully Covered** |
| **L1** | LM 3: Risk and Return: Part II | Book 5, Module 42 | CAPM, CAL & CML | CAL, CML, CAPM, Beta, Sharpe, Treynor, Jensen | **Fully Covered** |
| **L1** | LM 4: Planning & Construction | Book 5, Module 43 | IPS Framework | Return/Risk objectives, TTLLU constraints, SAA | **Fully Covered** |
| **L1** | LM 5: Behavioral Biases | Book 5, Module 44 | Behavioral Finance | Cognitive errors vs. Emotional biases | **Fully Covered** |
| **L1** | LM 6: Risk Management Basics | Book 5, Module 45 | Risk Governance | Risk tolerance, Risk budgeting, VaR introduction | **Fully Covered** |
| **L2** | LM 1: Theory of Active Portfolio Mgmt | Book 5, Topic 1 | Fundamental Law | Grinold's Law (IR = TC * IC * sqrt(BR)), Sharpe expansion | **Fully Covered** |
| **L2** | LM 2: Multifactor Models | Book 5, Topic 2 | Factor Models & APT | Macroeconomic, Fundamental, Statistical models | **Fully Covered** |
| **L2** | LM 3: Analysis of Active Mgmt | Book 5, Topic 3 | Factor Tilts & Smart Beta | Value, Size, Momentum, Quality style factors | **Fully Covered** |
| **L2** | LM 4: Economics & Asset Allocation | Book 5, Topic 4 | Capital Market Expectations | Singer-Terhaar international asset pricing model | **Gap Addressed** |
| **L2** | LM 5: Portfolio Construction | Book 5, Topic 5 | Rebalancing Corridors | Transaction costs, Volatility, Corridor widths | **Gap Addressed** |
| **L2** | LM 6: Institutional Portfolios & ALM | Book 5, Topic 6 | Pension & Insurance ALM | DB Pension ALM, Surplus optimization, Endowments | **Fully Covered** |
| **L2** | LM 7: Trade Strategy & Execution | Book 5, Topic 7 | Execution Algorithms | Implementation Shortfall 4-component breakdown | **Gap Addressed** |
| **L2** | LM 8: Performance Evaluation | Book 5, Topic 8 | Attribution & Appraisal | Brinson-Fachler attribution (Allocation/Selection) | **Gap Addressed** |

---

## 8. Strategic Roadmap & Implementation Blueprint

### 8.1 Prioritized Recommendations for Platform Expansion
1. **Immediate Platform Enhancements (Within the Active 4 Subjects)**:
   - Ingest the newly formatted solved numericals from Section 3–6 directly into `data/cfa_master_855.json` or as dedicated Practice Problem sets in `index.html`.
   - Add the missing edge cases highlighted in the audit (Implementation Shortfall 4-way breakdown, Excess Earnings Method for private firms, and H-Model reverse-solving) into the interactive simulation suite.
2. **Phase 2 Expansion (Full 10-Topic Curriculum Roadmap)**:
   - To achieve 100% complete CFA L1 & L2 certification, create datasets for the remaining 6 topics:
     * **Derivatives**: Futures, Forwards, European/American Options, Black-Scholes-Merton model, Interest Rate & Currency Swaps.
     * **Quantitative Methods**: Time-Series Modeling, AR(p), Unit Roots, Machine Learning, Decision Trees, Hypothesis Testing.
     * **Corporate Issuers**: Capital Structure Theory, Modigliani-Miller, Mergers & Acquisitions, Corporate Governance.
     * **Economics**: Uncovered Interest Rate Parity, Purchasing Power Parity, Neoclassical Growth, Regulatory Economics.
     * **Alternative Investments**: Real Estate NAV & Cap Rates, Private Equity LBO cascades, Commodities Futures Curves (Contango/Backwardation).
     * **Ethical & Professional Standards**: CFA Institute Code of Ethics, Standards of Professional Conduct I–VII, GIPS compliance rules.
