"""
generate_notes_libraries.py
Generates comprehensive curriculum reference libraries for:
  1. data/fi_reference_extracted.html (Fixed Income Master Reference Library)
  2. data/eq_reference_extracted.html (Equity Investments Master Reference Library)
Strictly complies with KaTeX delimiter rules and currency formatting.
"""

import os

FI_HTML_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "fi_reference_extracted.html")
EQ_HTML_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "eq_reference_extracted.html")

fi_html = """<div class="top-controls">
  <button class="btn-ctrl" onclick="toggleTheme()">🌓 Switch Theme</button>
  <button class="btn-ctrl" onclick="window.print()">🖨️ Print / Save as PDF</button>
</div>

<div class="doc-hero">
  <h1>Fixed Income Analysis & Valuation</h1>
  <p>The curriculum-complete master study guide synthesized for CFA&reg; Level 1 and Level 2 candidates. Covering bond pricing mechanics, spot curve bootstrapping, forward rate parity, duration/convexity risk management, credit spreads (Z-spread vs OAS), binomial tree backward induction, and asset-backed securitization structures.</p>
  <div class="meta-tags">
    <span class="badge badge-cyan">CFA Exam Syllabus (L1 & L2)</span>
    <span class="badge badge-blue">Comprehensive Core Scope</span>
    <span class="badge badge-purple">Embedded Options & Trees</span>
    <span class="badge badge-amber">Yield & Spread Analytics</span>
  </div>
</div>

<div class="card" style="margin-top: 15px; margin-bottom: 25px;">
  <div class="card-title">📈 Quick Navigation: Fixed Income Curriculum Modules</div>
  <div class="fsa-nav-bar">
    <a class="fsa-nav-btn" href="#fi-m1-pricing">01. Pricing & Mechanics</a>
    <a class="fsa-nav-btn" href="#fi-m2-curves">02. Spot & Forward Curves</a>
    <a class="fsa-nav-btn" href="#fi-m3-spreads">03. Yield Measures & Spreads</a>
    <a class="fsa-nav-btn" href="#fi-m4-duration">04. Duration & Convexity</a>
    <a class="fsa-nav-btn" href="#fi-m5-options">05. Embedded Options & Trees</a>
    <a class="fsa-nav-btn" href="#fi-m6-credit">06. Credit Analysis & Default</a>
    <a class="fsa-nav-btn" href="#fi-m7-abs">07. ABS & Mortgage Structures</a>
    <a class="fsa-nav-btn" href="#fi-formulas" style="color: var(--accent-emerald); font-weight: 700;">Master Formula Sheet</a>
  </div>
</div>

<!-- ========================================================================================= -->
<!-- MODULE 1: BOND MECHANICS & PRICING -->
<!-- ========================================================================================= -->
<section id="fi-m1-pricing" class="notes-chapter">
  <h2 class="section-heading"><span class="num">01.</span> Fixed Income Essentials & Bond Pricing Mechanics</h2>
  <p>A bond represents a contractual debt obligation between the issuer (borrower) and the investor (creditor). The fundamental value of any default-free fixed-income instrument equals the present value of its future cash flows discounted at the market discount rate (YTM).</p>

  <h3 class="subheading">The Universal Bond Valuation Equation</h3>
  <div class="formula-card">
    <div class="formula-title">Fundamental Bond Pricing Formula</div>
    $$PV = \\sum_{t=1}^N \\frac{PMT}{(1 + r)^t} + \\frac{FV}{(1 + r)^N}$$
    $$\\text{Where: } PMT = \\text{Coupon payment per period}, \\quad FV = \\text{Face (Par) value}, \\quad r = \\text{Market discount rate per period}$$
  </div>

  <h3 class="subheading">Full Price (Dirty Price) vs Flat Price (Clean Price)</h3>
  <p>In secondary bond markets, transactions rarely settle precisely on a coupon payment date. The buyer must compensate the seller for accrued interest earned from the last coupon date to settlement date:</p>
  <div class="formula-card">
    <div class="formula-title">Clean vs Dirty Bond Pricing & Accrued Interest</div>
    $$PV^{\\text{Full}} = PV^{\\text{Flat}} + AI$$
    $$AI = PMT \\times \\left( \\frac{t}{T} \\right)$$
    $$\\text{Where: } t = \\text{Days accrued since prior coupon}, \\quad T = \\text{Total days in coupon period}$$
  </div>
  <ul>
    <li><strong>Actual/Actual Convention</strong>: Standard for government bonds. Exact calendar days elapsed divided by actual days in coupon period.</li>
    <li><strong>30/360 Convention</strong>: Standard for corporate and municipal bonds. Assumes 30 days per month and 360 days per year.</li>
  </ul>

  <h3 class="subheading">Matrix Pricing for Illiquid & Unrated Bonds</h3>
  <p>When a target bond is illiquid or newly issued without market quotes, analysts utilize <strong>Matrix Pricing</strong> (linear interpolation of yields on comparable liquid benchmark bonds matching maturity and credit quality) to establish the appropriate discounting yield.</p>
</section>

<!-- ========================================================================================= -->
<!-- MODULE 2: TERM STRUCTURE, SPOT & FORWARD RATES -->
<!-- ========================================================================================= -->
<section id="fi-m2-curves" class="notes-chapter">
  <h2 class="section-heading"><span class="num">02.</span> Term Structure of Interest Rates & Yield Curves</h2>
  <p>The term structure of interest rates describes the relationship between maturity tenors and yields for benchmark bonds of identical creditworthiness. A single discount rate (YTM) for all cash flows is a simplification; rigorous valuation requires discounting each cash flow at its specific spot rate.</p>

  <h3 class="subheading">Spot Rates & Curve Bootstrapping</h3>
  <p>The <strong>Spot Rate ($S_t$)</strong> is the yield to maturity on a zero-coupon bond maturing at period $t$. Bootstrapping systematically extracts zero-coupon spot rates from par yield curves:</p>
  <div class="formula-card">
    <div class="formula-title">Spot Rate Valuation & Bootstrapping Equation</div>
    $$PV = \\frac{PMT}{1 + S_1} + \\frac{PMT}{(1 + S_2)^2} + \\cdots + \\frac{PMT + FV}{(1 + S_N)^N}$$
    $$1 = \\frac{c}{1 + S_1} + \\frac{c}{(1 + S_2)^2} + \\frac{1 + c}{(1 + S_3)^3} \\implies S_3 = \\left( \\frac{1 + c}{1 - \\frac{c}{1+S_1} - \\frac{c}{(1+S_2)^2}} \\right)^{1/3} - 1$$
  </div>

  <h3 class="subheading">Forward Rates & Forward Rate Parity</h3>
  <p>A forward rate $f(A, B-A)$ is an interest rate agreed upon today for a loan beginning at future period $A$ and maturing at period $B$. Under no-arbitrage conditions:</p>
  <div class="formula-card">
    <div class="formula-title">Forward Rate Parity Identity</div>
    $$(1 + S_B)^B = (1 + S_A)^A \\times [1 + f(A, B-A)]^{B-A}$$
    $$[1 + f(1, 1)] = \\frac{(1 + S_2)^2}{(1 + S_1)^1}$$
  </div>

  <div class="chart-box">
    <div class="chart-header">
      <div class="chart-title">Visual 1: Benchmark Spot Curve vs Implied Forward Curve</div>
      <div class="chart-desc">When the spot yield curve is upward sloping, the forward curve always lies above the spot curve ($f(t-1, 1) > S_t > y_{par}$).</div>
    </div>
    <div class="chart-canvas-wrap" style="height: 280px;">
      <canvas id="fiNotesCurveChart"></canvas>
    </div>
  </div>

  <h3 class="subheading">Term Structure Theories</h3>
  <div class="table-container">
    <table>
      <thead>
        <tr>
          <th>Hypothesis</th>
          <th>Core Principle</th>
          <th>Yield Curve Interpretation</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Pure Expectations Theory</strong></td>
          <td>Forward rates are unbiased predictors of future spot rates. No risk premium required for longer maturities.</td>
          <td>Upward slope indicates market expects future short-term interest rates to rise.</td>
        </tr>
        <tr>
          <td><strong>Liquidity Preference Theory</strong></td>
          <td>Investors demand a liquidity premium ($L_t$) for tying up funds in longer-term, less liquid bonds.</td>
          <td>Curves slope upward naturally even if expected future spot rates are flat or slightly declining.</td>
        </tr>
        <tr>
          <td><strong>Segmented Markets Theory</strong></td>
          <td>Yields at each maturity are determined independently by supply and demand of institutional habitat participants.</td>
          <td>Shape is determined by supply-demand imbalances across market segments (e.g. pension funds in 30Y).</td>
        </tr>
        <tr>
          <td><strong>Preferred Habitat Theory</strong></td>
          <td>Market participants have preferred maturities but will cross segments if yield premium is sufficiently attractive.</td>
          <td>Humps and twists reflect market-clearing risk premiums required to induce cross-segment capital migration.</td>
        </tr>
      </tbody>
    </table>
  </div>
</section>

<!-- ========================================================================================= -->
<!-- MODULE 3: YIELD MEASURES & CREDIT SPREADS -->
<!-- ========================================================================================= -->
<section id="fi-m3-spreads" class="notes-chapter">
  <h2 class="section-heading"><span class="num">03.</span> Yield Measures, Benchmark Spreads & Option-Adjusted Spreads</h2>
  <p>Credit risk, liquidity risk, and taxation cause corporate bonds to trade at a spread above default-free benchmark government bonds.</p>

  <h3 class="subheading">Key Spread Definitions</h3>
  <ul>
    <li><strong>G-Spread (Government Spread)</strong>: Yield spread between a corporate bond and an interpolated government benchmark bond of identical maturity.</li>
    <li><strong>I-Spread (Interpolated Spread)</strong>: Yield spread over standard interbank swap benchmark rates (MRR / SOFR swap rates).</li>
    <li><strong>Zero-Volatility Spread (Z-Spread)</strong>: Constant basis point spread added to each spot rate on the benchmark zero curve to equate the present value of bond cash flows to its market price:
      $$PV = \\sum_{t=1}^N \\frac{CF_t}{(1 + S_t + Z)^t}$$
    </li>
    <li><strong>Option-Adjusted Spread (OAS)</strong>: The spread isolated after stripping out the cost of embedded options (calls, puts). Measures pure credit and liquidity risk:
      $$\\text{Option Cost (bps)} = Z\\text{-spread} - OAS$$
      $$\\text{For a Callable Bond: } Z\\text{-spread} > OAS \\implies \\text{Option Cost} > 0$$
      $$\\text{For a Putable Bond: } Z\\text{-spread} < OAS \\implies \\text{Option Cost} < 0$$
    </li>
  </ul>
</section>

<!-- ========================================================================================= -->
<!-- MODULE 4: DURATION & CONVEXITY RISK -->
<!-- ========================================================================================= -->
<section id="fi-m4-duration" class="notes-chapter">
  <h2 class="section-heading"><span class="num">04.</span> Interest Rate Risk: Duration, Convexity & Sensitivity</h2>
  <p>Duration measures a bond's price sensitivity to changes in benchmark interest rates. Convexity measures the rate of change of duration, providing a second-order curvature adjustment for large interest rate shocks.</p>

  <h3 class="subheading">Macaulay, Modified & Effective Duration</h3>
  <div class="formula-card">
    <div class="formula-title">Duration Formulas & Relationships</div>
    $$MacDur = \\sum_{t=1}^N \\left[ t \\times \\frac{CF_t / (1 + y)^t}{PV} \\right]$$
    $$ModDur = \\frac{MacDur}{1 + y / k} \\quad (k = \\text{compounding frequency per year})$$
    $$EffDur = \\frac{PV_- - PV_+}{2 \\times \\Delta y \\times PV_0} \\quad (\\text{Mandatory for bonds with embedded options})$$
  </div>

  <h3 class="subheading">Convexity & The Combined Price Approximation</h3>
  <p>Because the price-yield relationship of a straight bond is convex (curves upward), a linear duration estimate underestimates price increases when yields fall and overestimates price declines when yields rise:</p>
  <div class="formula-card">
    <div class="formula-title">Full Taylor-Series Price Change Approximation</div>
    $$\\% \\Delta PV \\approx -ModDur \\times \\Delta y + \\frac{1}{2} \\times Convexity \\times (\\Delta y)^2$$
    $$ApproxConvexity = \\frac{PV_- + PV_+ - 2PV_0}{(\\Delta y)^2 \\times PV_0}$$
  </div>

  <div class="chart-box">
    <div class="chart-header">
      <div class="chart-title">Visual 2: Price-Yield Convexity vs Linear Duration Approximation</div>
      <div class="chart-desc">The tangible benefit of positive convexity: the bond price rises more when yields drop than it falls when yields increase by the same magnitude.</div>
    </div>
    <div class="chart-canvas-wrap" style="height: 280px;">
      <canvas id="fiNotesDurationChart"></canvas>
    </div>
  </div>

  <h3 class="subheading">Key Rate Duration (KRD)</h3>
  <p>Key rate duration measures bond price sensitivity to a 100 bps shift at a single maturity point on the spot curve while holding all other points constant. The sum of all key rate durations equals the effective duration for a parallel shift:</p>
  $$EffDur = \\sum_{i=1}^M KRD_i$$
</section>

<!-- ========================================================================================= -->
<!-- MODULE 5: EMBEDDED OPTIONS & VALUATION TREES -->
<!-- ========================================================================================= -->
<section id="fi-m5-options" class="notes-chapter">
  <h2 class="section-heading"><span class="num">05.</span> Bonds with Embedded Options & Binomial Trees</h2>
  <p>Bonds containing call, put, or conversion features cannot be valued with standard yield-to-maturity discounting due to cash flow uncertainty contingent on path-dependent interest rate outcomes.</p>

  <h3 class="subheading">Callable vs Putable Bond Valuation</h3>
  <div class="formula-card">
    <div class="formula-title">Embedded Option Decomposition</div>
    $$V_{\\text{Callable Bond}} = V_{\\text{Straight Bond}} - V_{\\text{Call Option}}$$
    $$V_{\\text{Putable Bond}} = V_{\\text{Straight Bond}} + V_{\\text{Put Option}}$$
  </div>

  <div class="callout callout-warning">
    <strong>Negative Convexity Trap</strong>: As benchmark yields decline, the probability of the issuer calling the bond increases dramatically. The price of a callable bond compression ceiling is reached at the call price. At low yields, callable bonds exhibit <em>negative convexity</em> (falling yields yield diminishing price gains).
  </div>

  <h3 class="subheading">Binomial Interest Rate Tree Backward Induction</h3>
  <p>A binomial tree models interest rate evolution under lognormal volatility: $r_{1, u} = r_{1, d} e^{2\\sigma}$. Valuation proceeds backwards from maturity ($T$) to node 0:</p>
  <div class="formula-card">
    <div class="formula-title">Backward Induction Valuation Node Equation</div>
    $$V_{\\text{node}} = \\frac{1}{2} \\left[ \\frac{V_{u} + PMT}{1 + r_{\\text{node}}} + \\frac{V_{d} + PMT}{1 + r_{\\text{node}}} \\right]$$
    $$\\text{Callable Node Decision: } V = \\min(\\text{Calculated Node Value}, \\text{Call Price})$$
    $$\\text{Putable Node Decision: } V = \\max(\\text{Calculated Node Value}, \\text{Put Price})$$
  </div>
</section>

<!-- ========================================================================================= -->
<!-- MODULE 6: CREDIT ANALYSIS & DEFAULT MODELS -->
<!-- ========================================================================================= -->
<section id="fi-m6-credit" class="notes-chapter">
  <h2 class="section-heading"><span class="num">06.</span> Credit Analysis, Expected Loss & Structural Models</h2>
  <p>Credit analysis evaluates an issuer's default risk and creditworthiness. Credit risk comprises two core components: default probability and recovery rate upon default.</p>

  <h3 class="subheading">Expected Loss Mathematics</h3>
  <div class="formula-card">
    <div class="formula-title">Expected Loss & Recovery Rate</div>
    $$\\text{Expected Loss} = \\text{Probability of Default (PD)} \\times \\text{Loss Given Default (LGD)}$$
    $$\\text{LGD} = 1 - \\text{Recovery Rate (RR)}$$
    $$\\text{Present Value of Expected Loss (CVA)} = PV_{\\text{Default-Free}} - PV_{\\text{Risky}}$$
  </div>

  <h3 class="subheading">Structural vs Reduced Form Credit Models</h3>
  <div class="table-container">
    <table>
      <thead>
        <tr>
          <th>Attribute</th>
          <th>Structural Models (Merton 1974)</th>
          <th>Reduced Form Models</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Core Foundation</strong></td>
          <td>Company's balance sheet structure: equity is a European call option on firm assets ($V_A$) with strike equal to debt face value ($K$).</td>
          <td>Statistical intensity process where default occurs as an exogenous Poisson jump process.</td>
        </tr>
        <tr>
          <td><strong>Default Condition</strong></td>
          <td>Default occurs at maturity $T$ if total asset value falls below debt obligations: $V_A(T) < K$.</td>
          <td>Default can occur randomly at any instant prior to maturity based on macro hazard rates.</td>
        </tr>
        <tr>
          <td><strong>Inputs Required</strong></td>
          <td>Market value of firm assets, asset return volatility ($\\sigma_A$), balance sheet debt levels.</td>
          <td>Market credit spreads, macroeconomic covariates, historical rating transition matrices.</td>
        </tr>
      </tbody>
    </table>
  </div>
</section>

<!-- ========================================================================================= -->
<!-- MODULE 7: ABS & MORTGAGE STRUCTURES -->
<!-- ========================================================================================= -->
<section id="fi-m7-abs" class="notes-chapter">
  <h2 class="section-heading"><span class="num">07.</span> Asset-Backed (ABS) & Mortgage-Backed Securities (MBS)</h2>
  <p>Securitization pools illiquid financial assets (residential mortgages, auto loans, credit card debt) and converts them into tradable marketable securities through a bankruptcy-remote Special Purpose Vehicle (SPV).</p>

  <h3 class="subheading">Prepayment Risk: Contraction vs Extension Risk</h3>
  <ul>
    <li><strong>Contraction Risk</strong>: Occurs when interest rates decline significantly. Homeowners refinance mortgages at lower rates, accelerating principal prepayments. MBS investors receive early principal and are forced to reinvest at lower prevailing rates, shortening maturity.</li>
    <li><strong>Extension Risk</strong>: Occurs when interest rates rise. Homeowners delay moving or refinancing, slowing prepayments. Investors remain locked into below-market coupon payments, extending average life.</li>
  </ul>

  <h3 class="subheading">Prepayment Metrics: SMM & CPR</h3>
  <div class="formula-card">
    <div class="formula-title">Prepayment Rate Identities</div>
    $$SMM = \\frac{\\text{Prepayment in Month } t}{\\text{Beginning Mortgage Balance} - \\text{Scheduled Principal}}$$
    $$CPR = 1 - (1 - SMM)^{12} \\iff SMM = 1 - (1 - CPR)^{1/12}$$
  </div>

  <h3 class="subheading">Collateralized Mortgage Obligations (CMO) Tranching</h3>
  <ul>
    <li><strong>Sequential-Pay Tranches</strong>: Principal payments retire tranches in sequential order (Tranche A first, then B, then C). Early tranches absorb contraction risk; later tranches absorb extension risk.</li>
    <li><strong>PAC & Support Tranches</strong>: Planned Amortization Class (PAC) tranches provide stable cash flows within a specified prepayment collar. The support tranche absorbs prepayments above or below the band, exhibiting high volatility.</li>
  </ul>
</section>

<!-- ========================================================================================= -->
<!-- MODULE 8: MASTER FORMULA CHEAT SHEET -->
<!-- ========================================================================================= -->
<section id="fi-formulas" class="notes-chapter">
  <h2 class="section-heading"><span class="num">08.</span> Master Fixed Income Formula Cheat Sheet</h2>
  <p>Direct lookup formula card for rapid calculation during CFA Level 1 and Level 2 exam problem solving:</p>
  
  <div class="table-container">
    <table>
      <thead>
        <tr>
          <th>Topic</th>
          <th>Metric / Formula</th>
          <th>KaTeX Mathematical Formulation</th>
          <th>Notes & Key Usage</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Pricing</strong></td>
          <td>Full Bond Price</td>
          <td>$$PV^{\\text{Full}} = PV^{\\text{Flat}} + AI$$</td>
          <td>Clean price plus accrued interest based on day-count convention.</td>
        </tr>
        <tr>
          <td><strong>Curves</strong></td>
          <td>Forward Rate Parity</td>
          <td>$$(1 + S_B)^B = (1 + S_A)^A \\times [1 + f(A, B-A)]^{B-A}$$</td>
          <td>No-arbitrage relationship linking spot and forward rates.</td>
        </tr>
        <tr>
          <td><strong>Risk</strong></td>
          <td>Modified Duration</td>
          <td>$$ModDur = \\frac{MacDur}{1 + y / k}$$</td>
          <td>Measures percentage price change per 100 bps shift in yield.</td>
        </tr>
        <tr>
          <td><strong>Risk</strong></td>
          <td>Convexity Adjustment</td>
          <td>$$\\% \\Delta PV \\approx -ModDur(\\Delta y) + \\frac{1}{2} Convexity(\\Delta y)^2$$</td>
          <td>Second-order Taylor expansion correcting for curvature.</td>
        </tr>
        <tr>
          <td><strong>Spreads</strong></td>
          <td>Option Cost (bps)</td>
          <td>$$\\text{Option Cost} = Z\\text{-spread} - OAS$$</td>
          <td>Positive for callable bonds; negative for putable bonds.</td>
        </tr>
        <tr>
          <td><strong>Trees</strong></td>
          <td>Binomial Node Value</td>
          <td>$$V = \\frac{1}{2} \\left[ \\frac{V_u + C}{1 + r_u} + \\frac{V_d + C}{1 + r_d} \\right]$$</td>
          <td>Backward induction node pricing using 50/50 risk-neutral branch probabilities.</td>
        </tr>
        <tr>
          <td><strong>Credit</strong></td>
          <td>Expected Loss</td>
          <td>$$\\text{ExpLoss} = PD \\times (1 - RR)$$</td>
          <td>Default probability times loss given default.</td>
        </tr>
        <tr>
          <td><strong>Prepayment</strong></td>
          <td>SMM from CPR</td>
          <td>$$SMM = 1 - (1 - CPR)^{1/12}$$</td>
          <td>Monthly equivalent prepayment rate.</td>
        </tr>
      </tbody>
    </table>
  </div>
</section>
"""

eq_html = """<div class="top-controls">
  <button class="btn-ctrl" onclick="toggleTheme()">🌓 Switch Theme</button>
  <button class="btn-ctrl" onclick="window.print()">🖨️ Print / Save as PDF</button>
</div>

<div class="doc-hero">
  <h1>Equity Valuation & Analysis</h1>
  <p>The curriculum-complete master study guide synthesized for CFA&reg; Level 1 and Level 2 candidates. Covering industry competitive strategy (Porter's Five Forces), multi-stage Dividend Discount Models (DDM & H-Model), Free Cash Flow valuation (FCFF & FCFE derivations), enterprise value multiples, residual income accounting, and private company normalization discounts.</p>
  <div class="meta-tags">
    <span class="badge badge-green">CFA Exam Syllabus (L1 & L2)</span>
    <span class="badge badge-blue">Comprehensive Core Scope</span>
    <span class="badge badge-purple">DCF & Multiplier Valuation</span>
    <span class="badge badge-amber">Clean Surplus Accounting</span>
  </div>
</div>

<div class="card" style="margin-top: 15px; margin-bottom: 25px;">
  <div class="card-title">📊 Quick Navigation: Equity Investments Curriculum Modules</div>
  <div class="fsa-nav-bar">
    <a class="fsa-nav-btn" href="#eq-m1-markets">01. Market Structure & Indexes</a>
    <a class="fsa-nav-btn" href="#eq-m2-industry">02. Industry & Strategy</a>
    <a class="fsa-nav-btn" href="#eq-m3-ddm">03. Dividend Discount Models</a>
    <a class="fsa-nav-btn" href="#eq-m4-fcf">04. Free Cash Flow (FCFF/FCFE)</a>
    <a class="fsa-nav-btn" href="#eq-m5-multiples">05. Multipliers & Multiples</a>
    <a class="fsa-nav-btn" href="#eq-m6-ri">06. Residual Income (RI)</a>
    <a class="fsa-nav-btn" href="#eq-m7-private">07. Private Company Valuation</a>
    <a class="fsa-nav-btn" href="#eq-formulas" style="color: var(--accent-emerald); font-weight: 700;">Master Formula Sheet</a>
  </div>
</div>

<!-- ========================================================================================= -->
<!-- MODULE 1: MARKET STRUCTURE & INDEXES -->
<!-- ========================================================================================= -->
<section id="eq-m1-markets" class="notes-chapter">
  <h2 class="section-heading"><span class="num">01.</span> Market Organization, Security Trading & Indexes</h2>
  <p>Financial markets channel capital from savers to productive investment. Analysts must evaluate market order execution mechanisms, leverage trading limits, and benchmark index construction.</p>

  <h3 class="subheading">Margin Transactions & Margin Call Pricing</h3>
  <p>When buying securities on margin, the investor borrows part of the purchase price from the broker. The <strong>Margin Call Price ($P$)</strong> is the stock price below which the broker requires additional equity collateral:</p>
  <div class="formula-card">
    <div class="formula-title">Margin Call Trigger Price Formula</div>
    $$P = P_0 \\times \\left( \\frac{1 - \\text{Initial Margin}}{1 - \\text{Maintenance Margin}} \\right)$$
    $$\\text{Where: } P_0 = \\text{Initial purchase price}, \\quad IM = \\text{Initial equity margin %}, \\quad MM = \\text{Maintenance margin %}$$
  </div>

  <h3 class="subheading">Equity Index Construction Methodologies</h3>
  <div class="table-container">
    <table>
      <thead>
        <tr>
          <th>Weighting Method</th>
          <th>Weighting Basis</th>
          <th>Stock Split Impact</th>
          <th>Prominent Example</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Price-Weighted</strong></td>
          <td>Price per share divided by index divisor: $w_i = P_i / \\sum P_k$.</td>
          <td>Requires divisor adjustment; high-priced stocks have disproportionate influence.</td>
          <td>Dow Jones Industrial Average (DJIA), Nikkei 225.</td>
        </tr>
        <tr>
          <td><strong>Value-Weighted (Market-Cap)</strong></td>
          <td>Total market capitalization: $w_i = (P_i Q_i) / \\sum (P_k Q_k)$. Often float-adjusted.</td>
          <td>No divisor adjustment required for stock splits; mirrors true aggregate wealth.</td>
          <td>S&P 500, MSCI World, FTSE 100.</td>
        </tr>
        <tr>
          <td><strong>Equal-Weighted</strong></td>
          <td>Each constituent stock receives identical weight: $w_i = 1 / N$.</td>
          <td>Requires frequent rebalancing as stock prices diverge; small-cap tilt.</td>
          <td>S&P 500 Equal Weight Index.</td>
        </tr>
      </tbody>
    </table>
  </div>
</section>

<!-- ========================================================================================= -->
<!-- MODULE 2: INDUSTRY & COMPETITIVE ANALYSIS -->
<!-- ========================================================================================= -->
<section id="eq-m2-industry" class="notes-chapter">
  <h2 class="section-heading"><span class="num">02.</span> Industry & Competitive Strategy Analysis</h2>
  <p>Industry structure drives fundamental return on invested capital (ROIC). Michael Porter's Five Forces framework analyzes the competitive intensity and sustainable pricing power of an industry.</p>

  <h3 class="subheading">Porter's Five Forces Framework</h3>
  <ul>
    <li><strong>Threat of New Entrants</strong>: High barriers to entry (economies of scale, patents, high switching costs) protect economic profits.</li>
    <li><strong>Bargaining Power of Buyers</strong>: Concentrated buyers or standardized commodity products reduce pricing power.</li>
    <li><strong>Bargaining Power of Suppliers</strong>: Fragmented buyers dealing with few specialized suppliers face high input costs.</li>
    <li><strong>Threat of Substitute Products</strong>: Close substitutes cap pricing power and elastic demand.</li>
    <li><strong>Rivalry Among Existing Competitors</strong>: Intense price competition occurs in fragmented industries with high exit barriers and slow growth.</li>
  </ul>

  <h3 class="subheading">Industry Life Cycle Stages</h3>
  <ol>
    <li><strong>Embryonic</strong>: Slow growth, high startup costs, unproven customer demand.</li>
    <li><strong>Growth</strong>: Rapidly rising demand, improving profitability, falling production costs.</li>
    <li><strong>Shakeout</strong>: Growth slows, overcapacity develops, price wars force weaker firms out.</li>
    <li><strong>Mature</strong>: Slower growth matching GDP, consolidated oligopoly, focus on efficiency.</li>
    <li><strong>Decline</strong>: Negative demand growth due to technological substitution.</li>
  </ol>
</section>

<!-- ========================================================================================= -->
<!-- MODULE 3: DIVIDEND DISCOUNT MODELS (DDM) -->
<!-- ========================================================================================= -->
<section id="eq-m3-ddm" class="notes-chapter">
  <h2 class="section-heading"><span class="num">03.</span> Dividend Discount Models & Multi-Stage Valuation</h2>
  <p>The Dividend Discount Model (DDM) values common stock as the present value of all expected future cash dividend payments discounted at the required return on equity ($r$).</p>

  <h3 class="subheading">Gordon Growth Model & Sustainable Growth Rate</h3>
  <div class="formula-card">
    <div class="formula-title">Constant Growth DDM (Gordon Growth)</div>
    $$V_0 = \\frac{D_1}{r - g} = \\frac{D_0 (1 + g)}{r - g} \\quad (\\text{Condition: } r > g)$$
    $$g = b \\times ROE = (1 - \\text{Dividend Payout Ratio}) \\times ROE$$
  </div>

  <h3 class="subheading">Present Value of Growth Opportunities (PVGO)</h3>
  <p>A firm's stock value can be decomposed into the value of its current no-growth earnings stream plus the net present value of profitable growth investments:</p>
  <div class="formula-card">
    <div class="formula-title">PVGO Decomposition</div>
    $$V_0 = \\frac{E_1}{r} + PVGO \\implies PVGO = V_0 - \\frac{E_1}{r}$$
  </div>

  <h3 class="subheading">The H-Model for Linearly Transitioning Growth</h3>
  <p>The H-Model values a firm experiencing high initial growth ($g_S$) that transitions linearly over half-life $H$ (years $= 2H$) to a sustainable long-term rate ($g_L$):</p>
  <div class="formula-card">
    <div class="formula-title">H-Model Valuation Equation</div>
    $$V_0 = \\frac{D_0 (1 + g_L)}{r - g_L} + \\frac{D_0 \\times H \\times (g_S - g_L)}{r - g_L}$$
  </div>

  <div class="chart-box">
    <div class="chart-header">
      <div class="chart-title">Visual 1: DDM Valuation Sensitivity to Cost of Equity & Long-Term Growth</div>
      <div class="chart-desc">Demonstrates asymptotic intrinsic value expansion as the required return $r$ approaches the perpetual growth rate $g$.</div>
    </div>
    <div class="chart-canvas-wrap" style="height: 280px;">
      <canvas id="eqNotesDdmChart"></canvas>
    </div>
  </div>
</section>

<!-- ========================================================================================= -->
<!-- MODULE 4: FREE CASH FLOW VALUATION (FCFF & FCFE) -->
<!-- ========================================================================================= -->
<section id="eq-m4-fcf" class="notes-chapter">
  <h2 class="section-heading"><span class="num">04.</span> Free Cash Flow Valuation (FCFF & FCFE)</h2>
  <p>Free cash flow models are superior when firms do not pay dividends, dividend policy does not reflect underlying profitability, or an acquiring firm seeks control of total operational cash flow.</p>

  <h3 class="subheading">Free Cash Flow to Firm (FCFF) Derivations</h3>
  <div class="formula-card">
    <div class="formula-title">FCFF Multi-Source Accounting Identities</div>
    $$\\text{From Net Income: } FCFF = NI + NCC + \\text{Interest}(1 - T) - FCInv - WCInv$$
    $$\\text{From CFO: } FCFF = CFO + \\text{Interest}(1 - T) - FCInv$$
    $$\\text{From EBIT: } FCFF = EBIT(1 - T) + Dep - FCInv - WCInv$$
    $$\\text{From EBITDA: } FCFF = EBITDA(1 - T) + (Dep \\times T) - FCInv - WCInv$$
  </div>

  <h3 class="subheading">Free Cash Flow to Equity (FCFE) Derivations</h3>
  <div class="formula-card">
    <div class="formula-title">FCFE Formulas & Net Borrowing Integration</div>
    $$FCFE = FCFF - \\text{Interest}(1 - T) + \\text{Net Borrowing}$$
    $$FCFE = NI + NCC - FCInv - WCInv + \\text{Net Borrowing}$$
    $$FCFE = CFO - FCInv + \\text{Net Borrowing}$$
    $$\\text{Where: } \\text{Net Borrowing} = \\text{New Debt Issued} - \\text{Principal Repayments}$$
  </div>

  <div class="chart-box">
    <div class="chart-header">
      <div class="chart-title">Visual 2: Cash Flow Waterfall Bridge from Operational Profit to Free Cash Flow</div>
      <div class="chart-desc">Step-by-step conversion of EBITDA down to Free Cash Flow to Firm (FCFF) and Free Cash Flow to Equity (FCFE).</div>
    </div>
    <div class="chart-canvas-wrap" style="height: 280px;">
      <canvas id="eqNotesFcfChart"></canvas>
    </div>
  </div>
</section>

<!-- ========================================================================================= -->
<!-- MODULE 5: MARKET MULTIPLIERS (P/E, P/B, EV/EBITDA) -->
<!-- ========================================================================================= -->
<section id="eq-m5-multiples" class="notes-chapter">
  <h2 class="section-heading"><span class="num">05.</span> Market Multiples & Valuation Ratios</h2>
  <p>Relative valuation compares a company's market price multiplier against comparable peer benchmarks or historic averages. Justified multiples are derived directly from fundamental discounted cash flow economics.</p>

  <h3 class="subheading">Justified Multipliers Derived from Fundamentals</h3>
  <div class="formula-card">
    <div class="formula-title">Core Fundamental Justified Multiplier Identities</div>
    $$\\text{Justified Leading P/E: } \\frac{P_0}{E_1} = \\frac{1 - b}{r - g}$$
    $$\\text{Justified Trailing P/E: } \\frac{P_0}{E_0} = \\frac{(1 - b)(1 + g)}{r - g}$$
    $$\\text{Justified Price-to-Book (P/B): } \\frac{P_0}{B_0} = \\frac{ROE - g}{r - g}$$
    $$\\text{Justified Price-to-Sales (P/S): } \\frac{P_0}{S_0} = \\frac{\\text{Net Margin} \\times (1 - b)(1 + g)}{r - g}$$
  </div>

  <h3 class="subheading">Enterprise Value Multipliers</h3>
  <p><strong>Enterprise Value ($EV$)</strong> measures total market value of core operations independent of capital structure financing:</p>
  <div class="formula-card">
    <div class="formula-title">Enterprise Value Accounting Identity</div>
    $$EV = \\text{Market Value of Common Equity} + \\text{Total Debt} + \\text{Preferred Stock} + \\text{Minority Interest} - \\text{Cash & Equivalents}$$
  </div>
</section>

<!-- ========================================================================================= -->
<!-- MODULE 6: RESIDUAL INCOME (RI) & CLEAN SURPLUS -->
<!-- ========================================================================================= -->
<section id="eq-m6-ri" class="notes-chapter">
  <h2 class="section-heading"><span class="num">06.</span> Residual Income Valuation & Clean Surplus Accounting</h2>
  <p>Residual Income (Economic Profit) equals net income in excess of the accounting equity charge for the cost of equity capital ($r \\times B_{t-1}$).</p>

  <h3 class="subheading">Residual Income Valuation Equation</h3>
  <div class="formula-card">
    <div class="formula-title">Universal Residual Income Model</div>
    $$V_0 = B_0 + \\sum_{t=1}^\\infty \\frac{RI_t}{(1 + r)^t}$$
    $$RI_t = NI_t - (r \\times B_{t-1}) = (ROE_t - r) \\times B_{t-1}$$
  </div>

  <div class="callout callout-info">
    <strong>Clean Surplus Relation</strong>: The balance sheet book value must reconcile perfectly through earnings and dividends:
    $$B_t = B_{t-1} + NI_t - Div_t$$
    Items bypassing the income statement through Other Comprehensive Income (AOCI)—such as foreign currency translation adjustments or unrealized gains on OCI securities—violate clean surplus and require analyst normalization.
  </div>

  <h3 class="subheading">Continuing Residual Income & Persistence Factor ($\\omega$)</h3>
  <p>Under competitive market dynamics, supernormal returns decay over time to normal returns ($ROE \\to r$):</p>
  <div class="formula-card">
    <div class="formula-title">Terminal Value with Persistence Decay ($\\omega$)</div>
    $$PV(\\text{Continuing RI at } T-1) = \\frac{RI_T}{1 + r - \\omega}$$
    $$\\text{Where } \\omega \\in [0, 1]: \\quad \\omega = 1.0 \\implies \\text{Perpetual RI}, \\quad \\omega = 0.0 \\implies \\text{Instant Return to Cost of Equity}$$
  </div>
</section>

<!-- ========================================================================================= -->
<!-- MODULE 7: PRIVATE COMPANY VALUATION -->
<!-- ========================================================================================= -->
<section id="eq-m7-private" class="notes-chapter">
  <h2 class="section-heading"><span class="num">07.</span> Private Company Valuation & Normalization Adjustments</h2>
  <p>Private company valuation requires adjusting financial statements for non-market transactions and quantifying illiquidity and control differentials.</p>

  <h3 class="subheading">Financial Statement Normalization</h3>
  <ul>
    <li><strong>Officer/Owner Compensation</strong>: Replace non-market excessive or below-market salaries with fair market executive compensation.</li>
    <li><strong>Non-Operating Assets & Expenses</strong>: Segregate excess cash, corporate personal aircraft, or real estate assets held for speculation.</li>
    <li><strong>Related-Party Transactions</strong>: Re-align intercompany lease agreements to market rents.</li>
  </ul>

  <h3 class="subheading">Valuation Discounts & Premiums</h3>
  <div class="formula-card">
    <div class="formula-title">Control and Marketability Discount Interaction</div>
    $$\\text{Total Combined Discount} = 1 - (1 - DLOC) \\times (1 - DLOM)$$
    $$DLOC = 1 - \\left( \\frac{1}{1 + \\text{Control Premium}} \\right)$$
    $$\\text{Where: } DLOC = \\text{Discount for Lack of Control}, \\quad DLOM = \\text{Discount for Lack of Marketability}$$
  </div>
</section>

<!-- ========================================================================================= -->
<!-- MODULE 8: MASTER EQUITY FORMULA CHEAT SHEET -->
<!-- ========================================================================================= -->
<section id="eq-formulas" class="notes-chapter">
  <h2 class="section-heading"><span class="num">08.</span> Master Equity Valuation Formula Cheat Sheet</h2>
  <p>Direct reference formula cheat sheet for rapid multi-model valuation problem solving:</p>

  <div class="table-container">
    <table>
      <thead>
        <tr>
          <th>Model</th>
          <th>Metric Name</th>
          <th>KaTeX Mathematical Formulation</th>
          <th>Primary Exam Usage</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>DDM</strong></td>
          <td>Gordon Growth Value</td>
          <td>$$V_0 = \\frac{D_1}{r - g} = \\frac{D_0 (1 + g)}{r - g}$$</td>
          <td>Mature, steady dividend-paying corporations.</td>
        </tr>
        <tr>
          <td><strong>DDM</strong></td>
          <td>Sustainable Growth</td>
          <td>$$g = b \\times ROE = (1 - PR) \\times ROE$$</td>
          <td>Internal equity reinvestment rate.</td>
        </tr>
        <tr>
          <td><strong>DDM</strong></td>
          <td>H-Model Value</td>
          <td>$$V_0 = \\frac{D_0 (1 + g_L)}{r - g_L} + \\frac{D_0 H (g_S - g_L)}{r - g_L}$$</td>
          <td>High growth transitioning linearly to long-term rate.</td>
        </tr>
        <tr>
          <td><strong>DCF</strong></td>
          <td>FCFF from CFO</td>
          <td>$$FCFF = CFO + \\text{Interest}(1 - T) - FCInv$$</td>
          <td>Fastest calculation when Cash Flow Statement is provided.</td>
        </tr>
        <tr>
          <td><strong>DCF</strong></td>
          <td>FCFE from FCFF</td>
          <td>$$FCFE = FCFF - \\text{Interest}(1 - T) + \\text{Net Borrowing}$$</td>
          <td>Direct equity cash flow valuation.</td>
        </tr>
        <tr>
          <td><strong>Multipliers</strong></td>
          <td>Justified P/B</td>
          <td>$$\\frac{P_0}{B_0} = \\frac{ROE - g}{r - g}$$</td>
          <td>Values capital-intensive financial and asset-heavy firms.</td>
        </tr>
        <tr>
          <td><strong>Residual Income</strong></td>
          <td>Residual Income Value</td>
          <td>$$V_0 = B_0 + \\sum_{t=1}^\\infty \\frac{(ROE_t - r) B_{t-1}}{(1 + r)^t}$$</td>
          <td>Values firms with negative cash flows or non-dividend payers.</td>
        </tr>
        <tr>
          <td><strong>Private</strong></td>
          <td>Total Discount</td>
          <td>$$\\text{Total Disc} = 1 - (1 - DLOC)(1 - DLOM)$$</td>
          <td>Multiplicative interaction of lack of control and marketability.</td>
        </tr>
      </tbody>
    </table>
  </div>
</section>
"""

with open(FI_HTML_PATH, "w", encoding="utf-8") as f:
    f.write(fi_html)
print(f"Generated {FI_HTML_PATH} ({len(fi_html)} bytes)")

with open(EQ_HTML_PATH, "w", encoding="utf-8") as f:
    f.write(eq_html)
print(f"Generated {EQ_HTML_PATH} ({len(eq_html)} bytes)")
