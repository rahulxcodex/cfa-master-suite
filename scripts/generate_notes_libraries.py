"""
generate_notes_libraries.py
Generates comprehensive curriculum reference libraries for:
  1. data/fi_reference_extracted.html (Fixed Income Master Reference Library)
  2. data/eq_reference_extracted.html (Equity Investments Master Reference Library)
  3. data/pm_reference_extracted.html (Portfolio Management Master Reference Library)
Strictly complies with KaTeX delimiter rules and currency formatting.
"""

import os

FI_HTML_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "fi_reference_extracted.html")
EQ_HTML_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "eq_reference_extracted.html")
PM_HTML_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "pm_reference_extracted.html")

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
  <p>When a target bond is illiquid or newly issued without market quotes, analysts utilize <strong>Matrix Pricing</strong> (linear interpolation of yields on comparable liquid benchmark bonds matching maturity and credit quality) to establish the appropriate discounting yield:</p>
  <div class="formula-card">
    <div class="formula-title">Matrix Pricing Linear Interpolation</div>
    $$y_{\\text{target}} = y_{\\text{short}} + \\left( \\frac{T_{\\text{target}} - T_{\\text{short}}}{T_{\\text{long}} - T_{\\text{short}}} \\right) \\times (y_{\\text{long}} - y_{\\text{short}})$$
  </div>

  <div class="card" style="background: rgba(16, 185, 129, 0.05); border-left: 4px solid var(--accent-emerald); margin: 15px 0;">
    <h4 style="margin: 0 0 10px 0; color: var(--accent-emerald);">Worked Numerical Example 1: Clean vs. Dirty Price &amp; Matrix Pricing</h4>
    <p><strong>Part A (Accrued Interest &amp; Full Price)</strong>: A 6.0% semiannual-pay Treasury bond (Par = 1,000 USD) settles 62 days into a 182-day coupon period (Actual/Actual convention) at a quoted flat (clean) price of 1,018.50 USD.</p>
    <ul>
      <li>Semiannual coupon payment: $PMT = \\frac{6.0\\% \\times 1,000}{2} = 30.00\\text{ USD}$</li>
      <li>Accrued Interest: $AI = 30.00 \\times \\frac{62}{182} = 10.22\\text{ USD}$</li>
      <li>Full (Dirty) Price paid by buyer: $PV^{\\text{Full}} = 1,018.50 + 10.22 = 1,028.72\\text{ USD}$</li>
    </ul>
    <p><strong>Part B (Matrix Pricing)</strong>: A newly issued 4.2-year BBB-rated corporate bond lacks market quotes. Comparable liquid BBB bonds yield 5.20% (3.0-year maturity) and 5.80% (5.0-year maturity):</p>
    $$y_{\\text{4.2Y}} = 5.20\\% + \\left(\\frac{4.2 - 3.0}{5.0 - 3.0}\\right) \\times (5.80\\% - 5.20\\%) = 5.20\\% + 0.60 \\times 0.60\\% = 5.56\\%$$
  </div>

  <h3 class="subheading">Floating-Rate Notes (FRNs), Repo &amp; Shorting Fixed Income (CBOK VII)</h3>
  <p><strong>Floating-Rate Notes (FRNs)</strong> reset coupons periodically relative to a market reference rate (MRR / SOFR) plus a fixed <strong>Quoted Margin ($QM$)</strong>. When credit quality changes after issuance, the market discounts cash flows using MRR plus the required <strong>Discount Margin ($DM$)</strong> ($PV < \\text{Par}$ if $DM > QM$).</p>
  <p><strong>Repurchase Agreements (Repo) &amp; Shorting Bonds</strong>: A repo is a collateralized short-term loan where a dealer sells a bond today and agrees to repurchase it at a higher price on a future date. Conversely, investors <strong>short fixed-income securities</strong> by entering a <em>reverse repo</em> (lending cash to borrow the bond collateral), selling the bond in the market, and obligating themselves to reimburse the lender for any interim coupon payments. High demand to short a specific Treasury issue drives its collateral rate down—trading <strong>"on special"</strong> (below the general collateral repo rate).</p>
  <div class="formula-card">
    <div class="formula-title">Repurchase Agreement (Repo) Pricing &amp; Haircut</div>
    $$\\text{Initial Loan (Purchase Price)} = \\text{Collateral Market Value} \\times (1 - \\text{Repo Margin / Haircut})$$
    $$\\text{Repurchase Price} = \\text{Purchase Price} \\times \\left(1 + \\text{Repo Rate} \\times \\frac{\\text{Days}}{360}\\right)$$
  </div>

  <div class="card" style="background: rgba(59, 130, 246, 0.05); border-left: 4px solid var(--accent-blue); margin: 15px 0;">
    <h4 style="margin: 0 0 10px 0; color: var(--accent-blue);">Worked Numerical Example 2: Repo Haircut, Dollar Interest &amp; Short Financing</h4>
    <p><strong>Scenario</strong>: A dealer finances 10,000,000 USD market value of corporate bonds via a 30-day repo agreement with a 4.0% haircut and a 4.80% annualized repo rate (Actual/360 convention).</p>
    <ol>
      <li><strong>Purchase Price (Cash Borrowed)</strong>: $10,000,000 \\times (1 - 0.04) = 9,600,000\\text{ USD}$</li>
      <li><strong>Repo Dollar Interest</strong>: $9,600,000 \\times 0.0480 \\times \\frac{30}{360} = 38,400\\text{ USD}$</li>
      <li><strong>Repurchase Price at Maturity</strong>: $9,600,000 + 38,400 = 9,638,400\\text{ USD}$</li>
    </ol>
    <p><em>Short-Selling Link</em>: A hedge fund acting as the reverse-repo counterparty lends 9,600,000 USD, receives the bonds as collateral, shorts them for cash, and earns 4.80% on its posted cash margin (rebate) while paying the bond's accrued coupon to the collateral owner.</p>
  </div>
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

  <div class="card" style="background: rgba(147, 51, 234, 0.05); border-left: 4px solid var(--accent-purple); margin: 15px 0;">
    <h4 style="margin: 0 0 10px 0; color: var(--accent-purple);">Worked Numerical Example 3: Bootstrapping Spot Rates &amp; Forward Rate Parity</h4>
    <p><strong>Scenario</strong>: Given annual-pay benchmark government par yields of $y_1 = 4.00\\%$, $y_2 = 4.50\\%$, and $y_3 = 5.00\\%$, bootstrap the spot curve ($S_1, S_2, S_3$) and derive the 2-year forward rate starting in 1 year, $f(1,2)$.</p>
    <ol>
      <li><strong>1-Year Spot Rate ($S_1$)</strong>: $S_1 = y_1 = 4.0000\\%$</li>
      <li><strong>2-Year Spot Rate ($S_2$)</strong>: Using a 2-year par bond ($c = 4.50\\%$):
        $$1.00 = \\frac{0.045}{1.04} + \\frac{1.045}{(1+S_2)^2} \\implies (1+S_2)^2 = \\frac{1.045}{1 - 0.043269} = 1.09226 \\implies S_2 = 4.5113\\%$$
      </li>
      <li><strong>3-Year Spot Rate ($S_3$)</strong>: Using a 3-year par bond ($c = 5.00\\%$):
        $$1.00 = \\frac{0.05}{1.04} + \\frac{0.05}{(1.045113)^2} + \\frac{1.05}{(1+S_3)^3} \\implies S_3 = \\left(\\frac{1.05}{1 - 0.048077 - 0.045777}\\right)^{1/3} - 1 = 5.0341\\%$$
      </li>
      <li><strong>Implied 2-Year Forward Rate 1 Year Forward ($f(1,2)$)</strong>:
        $$[1 + f(1,2)]^2 = \\frac{(1+S_3)^3}{(1+S_1)^1} = \\frac{(1.050341)^3}{1.0400} = 1.11408 \\implies f(1,2) = \\sqrt{1.11408} - 1 = 5.5550\\%$$
      </li>
    </ol>
    <p><em>Check</em>: Because the spot curve is upward sloping, $f(1,2) = 5.56\\% > S_3 = 5.03\\% > y_3 = 5.00\\%$.</p>
  </div>

  <h3 class="subheading">Equilibrium vs. Arbitrage-Free Term Structure Models (L2) &amp; Yield Curve Strategies</h3>
  <div class="table-container">
    <table>
      <thead>
        <tr>
          <th>Model / Class</th>
          <th>Drift &amp; Volatility Specification</th>
          <th>Key Properties &amp; Exam Distinction</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Vasicek Model</strong> (Equilibrium)</td>
          <td>$dr = a(b - r)dt + \\sigma dW$</td>
          <td>Mean-reverting ($b$ = long-run mean); <strong>constant volatility</strong> $\\sigma$; permits <em>negative</em> interest rates.</td>
        </tr>
        <tr>
          <td><strong>Cox-Ingersoll-Ross (CIR)</strong> (Equilibrium)</td>
          <td>$dr = a(b - r)dt + \\sigma\\sqrt{r}\\,dW$</td>
          <td>Mean-reverting; volatility proportional to $\\sqrt{r}$ (rises with rate level); prevents negative rates if $2ab \\ge \\sigma^2$.</td>
        </tr>
        <tr>
          <td><strong>Ho-Lee Model</strong> (Arbitrage-Free)</td>
          <td>$dr = \\theta_t\\,dt + \\sigma dW$</td>
          <td>Calibrated exactly to today's observed spot curve via time-dependent drift $\\theta_t$; normal distribution (allows negative rates).</td>
        </tr>
        <tr>
          <td><strong>Kalotay-Williams-Fabozzi (KWF)</strong> (Arbitrage-Free)</td>
          <td>$d\\ln(r) = \\theta_t\\,dt + \\sigma dW$</td>
          <td>Lognormal short-rate distribution; calibrated to market term structure; guarantees <strong>strictly positive rates</strong> with constant proportional vol.</td>
        </tr>
      </tbody>
    </table>
  </div>
  <p><strong>Active Curve Strategies</strong>: Under an upward-sloping, stable yield curve, <strong>Riding the Yield Curve</strong> purchases bonds with maturities longer than the holding horizon so the bond "rolls down" the curve to lower yields and appreciates in price. The <strong>MRR–OIS Spread</strong> (difference between interbank funding rates and overnight index swap rates) serves as a primary gauge of banking-sector funding stress.</p>
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
    <li><strong>Current Yield, Yield-to-Call (YTC) &amp; Yield-to-Worst (YTW)</strong>: Current yield $= \\frac{\\text{Annual Coupon}}{\\text{Flat Price}}$. For callable bonds, compute YTM and YTC to every call schedule date; <strong>Yield-to-Worst (YTW)</strong> is the minimum of YTM and all YTCs.</li>
  </ul>

  <div class="card" style="background: rgba(245, 158, 11, 0.05); border-left: 4px solid var(--accent-amber); margin: 15px 0;">
    <h4 style="margin: 0 0 10px 0; color: var(--accent-amber);">Worked Numerical Example 4: Yield-to-Worst (YTW), Z-Spread &amp; OAS Decomposition</h4>
    <p><strong>Scenario</strong>: A 10-year, 6.0% semiannual coupon corporate bond (Par = 1,000 USD) trades at 1,060.00 USD and is callable in 4 years at 1,030.00 USD. A comparable government benchmark yields 4.00%, the bond's $Z$-spread is 148 bps, and the embedded call option cost is estimated at 36 bps.</p>
    <ol>
      <li><strong>Yield-to-Maturity (YTM)</strong>: Solving $1,060 = \\sum_{t=1}^{20} \\frac{30}{(1+r)^{t}} + \\frac{1,000}{(1+r)^{20}}$ yields semiannual $r = 2.61\\% \\implies \\text{YTM} = 5.22\\%$.</li>
      <li><strong>Yield-to-Call (YTC at 4Y)</strong>: Solving $1,060 = \\sum_{t=1}^{8} \\frac{30}{(1+r_c)^{t}} + \\frac{1,030}{(1+r_c)^{8}}$ yields semiannual $r_c = 2.505\\% \\implies \\text{YTC} = 5.01\\%$.</li>
      <li><strong>Yield-to-Worst (YTW)</strong>: $\\min(5.22\\%, 5.01\\%) = 5.01\\%$ (YTC governs because bond trades above call price).</li>
      <li><strong>G-Spread &amp; OAS</strong>: $\\text{G-Spread} = 5.22\\% - 4.00\\% = 122\\text{ bps}$. Removing the call option cost gives pure credit/liquidity compensation: $OAS = Z\\text{-spread} - \\text{Option Cost} = 148 - 36 = 112\\text{ bps}$.</li>
    </ol>
  </div>

  <h3 class="subheading">Sustainability Considerations in Fixed Income (CBOK VII)</h3>
  <ul>
    <li><strong>Green, Social &amp; Sustainability Bonds</strong>: Use-of-proceeds debt ring-fenced to environmental or social projects; credit risk remains backed by the issuer's general balance sheet. When investor demand outpaces supply, green bonds may price at a slight yield discount (<strong>Greenium</strong>).</li>
    <li><strong>Sustainability-Linked Bonds (SLBs)</strong>: General corporate purpose debt whose financial terms (typically a coupon step-up of +25 bps to +50 bps) adjust if the issuer fails to achieve predefined Sustainability Performance Targets (SPTs) by a target observation date.</li>
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

  <h3 class="subheading">Key Rate Duration (KRD), Money Duration &amp; Empirical Duration</h3>
  <p>Key rate duration measures bond price sensitivity to a 100 bps shift at a single maturity point on the spot curve while holding all other points constant. The sum of all key rate durations equals the effective duration for a parallel shift:</p>
  $$EffDur = \\sum_{i=1}^M KRD_i, \\qquad \\text{MoneyDur} = ModDur \\times PV^{\\text{Full}}, \\qquad \\text{PVBP} = \\frac{PV_- - PV_+}{2} \\text{ (for } \\Delta y = 1\\text{ bp)}$$
  <p><strong>Portfolio Duration</strong> equals the <em>market-value weighted average</em> of constituent bond durations ($Dur_P = \\sum w_i Dur_i$), NOT an equally weighted average. <strong>Analytical vs. Empirical Duration</strong>: Analytical formulas assume benchmark yields and credit spreads move independently. In "flight-to-safety" recessions, government benchmark yields fall while high-yield credit spreads widen simultaneously—making <strong>Empirical Duration</strong> (estimated via historical regression of bond prices on benchmark yields) substantially lower than analytical duration for high-yield corporates.</p>

  <div class="card" style="background: rgba(16, 185, 129, 0.05); border-left: 4px solid var(--accent-emerald); margin: 15px 0;">
    <h4 style="margin: 0 0 10px 0; color: var(--accent-emerald);">Worked Numerical Example 5: Effective Duration, Convexity &amp; Key Rate Duration Twist</h4>
    <p><strong>Scenario</strong>: A bond trades at $PV_0 = 100.00\\text{ USD}$. Shifting the benchmark par curve by $\\Delta y = \\pm 25\\text{ bps}$ ($0.0025$) produces $PV_- = 101.84\\text{ USD}$ and $PV_+ = 98.24\\text{ USD}$. Its key rate profile is $KRD_2 = 1.20$, $KRD_5 = 2.80$, $KRD_{10} = 3.20$.</p>
    <ol>
      <li><strong>Effective Duration</strong>: $EffDur = \\frac{101.84 - 98.24}{2 \\times 0.0025 \\times 100.00} = \\frac{3.60}{0.50} = 7.20$ (Notice $1.20 + 2.80 + 3.20 = 7.20$).</li>
      <li><strong>Effective Convexity</strong>: $EffConv = \\frac{101.84 + 98.24 - 2(100.00)}{(0.0025)^2 \\times 100.00} = \\frac{0.08}{0.000625} = 128.00$.</li>
      <li><strong>+100 bps Parallel Yield Increase ($\\Delta y = +0.01$)</strong>:
        $$\\%\\Delta PV \\approx -7.20(0.01) + \\frac{1}{2}(128.00)(0.01)^2 = -7.20\\% + 0.64\\% = -6.56\\%$$
      </li>
      <li><strong>Non-Parallel Curve Flattening Twist</strong> ($\\Delta y_2 = +40\\text{ bps}$, $\\Delta y_5 = +10\\text{ bps}$, $\\Delta y_{10} = -25\\text{ bps}$):
        $$\\%\\Delta PV \\approx -(1.20 \\times 0.40\\% + 2.80 \\times 0.10\\% + 3.20 \\times (-0.25\\%)) = -(0.48\\% + 0.28\\% - 0.80\\%) = +0.04\\%$$
      </li>
    </ol>
  </div>
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

  <div class="card" style="background: rgba(59, 130, 246, 0.05); border-left: 4px solid var(--accent-blue); margin: 15px 0;">
    <h4 style="margin: 0 0 10px 0; color: var(--accent-blue);">Worked Numerical Example 6: 2-Period Binomial Tree Backward Induction (Callable Bond)</h4>
    <p><strong>Scenario</strong>: Value a 2-year, 6.0% annual-pay bond (Par = 100.00) callable at 101.00 at $t=1$. The calibrated 1-year forward rates are $r_0 = 4.00\\%$ at $t=0$, and $r_{1,u} = 5.50\\%$, $r_{1,d} = 4.20\\%$ at $t=1$.</p>
    <ol>
      <li><strong>Straight Bond at $t=1$</strong> ($CF_2 = 106.00$):
        $$V_{1,u}^{\\text{straight}} = \\frac{106.00}{1.055} = 100.4739, \\qquad V_{1,d}^{\\text{straight}} = \\frac{106.00}{1.042} = 101.7274$$
        $$V_0^{\\text{straight}} = \\frac{1}{2}\\left[\\frac{100.4739 + 6}{1.04} + \\frac{101.7274 + 6}{1.04}\\right] = 102.9814$$
      </li>
      <li><strong>Callable Bond Decision at $t=1$</strong> ($V_{\\text{call}} = \\min(V_{\\text{calc}}, 101.00)$):
        <ul>
          <li>Upper node: $\\min(100.4739, 101.00) = 100.4739$ (not called).</li>
          <li>Lower node: $\\min(101.7274, 101.00) = 101.0000$ (<strong>called</strong> at 101.00!).</li>
        </ul>
      </li>
      <li><strong>Callable Value &amp; Embedded Call Option Value at $t=0$</strong>:
        $$V_0^{\\text{callable}} = \\frac{1}{2}\\left[\\frac{100.4739 + 6}{1.04} + \\frac{101.0000 + 6}{1.04}\\right] = 102.6317$$
        $$V_{\\text{Call Option}} = V_0^{\\text{straight}} - V_0^{\\text{callable}} = 102.9814 - 102.6317 = 0.3497$$
      </li>
    </ol>
  </div>

  <h3 class="subheading">Convertible Bonds Valuation &amp; Parity Metrics (L2)</h3>
  <p>A <strong>Convertible Bond</strong> grants the holder the right to convert the bond into a specified number of common shares (<strong>Conversion Ratio</strong>). Its value cannot fall below the greater of its straight debt value or conversion value:</p>
  <div class="formula-card">
    <div class="formula-title">Convertible Bond Identities</div>
    $$\\text{Conversion Value} = \\text{Conversion Ratio} \\times \\text{Stock Price}, \\qquad \\text{Minimum Value} = \\max(\\text{Straight Value}, \\text{Conversion Value})$$
    $$\\text{Market Conversion Price} = \\frac{\\text{Convertible Bond Price}}{\\text{Conversion Ratio}}, \\qquad \\text{Conv. Premium Ratio} = \\frac{\\text{Market Conv. Price} - \\text{Stock Price}}{\\text{Stock Price}}$$
  </div>

  <div class="card" style="background: rgba(147, 51, 234, 0.05); border-left: 4px solid var(--accent-purple); margin: 15px 0;">
    <h4 style="margin: 0 0 10px 0; color: var(--accent-purple);">Worked Numerical Example 7: Convertible Bond Parity &amp; Premiums</h4>
    <p><strong>Scenario</strong>: A convertible bond (Par = 1,000 USD) has a Conversion Ratio of 25 shares, Straight Value of 940 USD, and trades at 1,144 USD when the underlying common stock trades at 44.00 USD.</p>
    <ul>
      <li><strong>Conversion Value</strong>: $25 \\times 44.00 = 1,100.00\\text{ USD}$</li>
      <li><strong>Minimum Value</strong>: $\\max(940.00, 1,100.00) = 1,100.00\\text{ USD}$</li>
      <li><strong>Market Conversion Price</strong>: $\\frac{1,144}{25} = 45.76\\text{ USD}$ (effective entry price per share via the bond).</li>
      <li><strong>Market Conversion Premium Ratio</strong>: $\\frac{45.76 - 44.00}{44.00} = 4.00\\%$ (or $\\frac{1,144 - 1,100}{1,100} = 4.00\\%$).</li>
      <li><strong>Premium Over Straight Value</strong> (Downside Risk): $\\frac{1,144 - 940}{940} = 21.70\\%$.</li>
    </ul>
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

  <h3 class="subheading">4 Cs of Credit, Sovereign/Municipal/HY Debt &amp; CDS Mechanics (L1 &amp; L2)</h3>
  <ul>
    <li><strong>The 4 Cs of Corporate Credit</strong>: <strong>Capacity</strong> (EBITDA coverage, FCF/Debt), <strong>Collateral</strong> (asset quality, seniority waterfall), <strong>Covenants</strong> (affirmative &amp; negative restrictions), and <strong>Character</strong> (management integrity &amp; capital allocation history).</li>
    <li><strong>Sovereign, Municipal &amp; High-Yield Debt</strong>: Sovereigns lack collateral and rely on fiscal/monetary institutional strength and FX reserves. US Municipal bonds divide into <strong>General Obligation (GO)</strong> (tax-backed) vs. <strong>Revenue Bonds</strong> (project-backed; higher risk); evaluate via <em>Tax-Equivalent Yield</em> $= \\frac{y_{\\text{muni}}}{1 - t}$. High-yield issuers emphasize structural subordination, liquidity runways, and recovery waterfalls.</li>
    <li><strong>Credit Default Swaps (CDS) &amp; Upfront Payments</strong>: Protection buyer pays standardized fixed coupon (100 bps IG / 500 bps HY) to protection seller. Upfront payment reconciles coupon to market spread:
      $$\\text{Upfront Payment (\\%)} \\approx (\\text{CDS Spread} - \\text{Fixed Coupon}) \\times \\text{EffDur}_{\\text{CDS}}$$
      $$\\Delta\\text{Value}_{\\text{Buyer}} \\approx \\Delta\\text{Spread} \\times \\text{EffDur}_{\\text{CDS}} \\times \\text{Notional}, \\qquad POD(t) = 1 - e^{-\\lambda t}$$
      <strong>Basis &amp; Curve Trades</strong>: Negative basis trade (buy bond + buy CDS when CDS spread $<$ bond credit spread). Credit curve steepener (sell short-dated CDS protection + buy long-dated CDS protection).
    </li>
  </ul>

  <div class="card" style="background: rgba(245, 158, 11, 0.05); border-left: 4px solid var(--accent-amber); margin: 15px 0;">
    <h4 style="margin: 0 0 10px 0; color: var(--accent-amber);">Worked Numerical Example 8: Multi-Period Credit Valuation Adjustment (CVA)</h4>
    <p><strong>Scenario</strong>: Value a 2-year, 5.0% annual-pay corporate bond (Par = 1,000 USD) given a flat 3.00% risk-free rate, conditional annual hazard rate $PD = 2.00\\%$, and Recovery Rate $RR = 40\\%$ ($LGD = 60\\%$).</p>
    <ol>
      <li><strong>Default-Free Bond Value</strong>: $V_{\\text{ND}} = \\frac{50}{1.03} + \\frac{1,050}{1.03^2} = 48.54 + 989.73 = 1,038.27\\text{ USD}$.</li>
      <li><strong>Year 1 Expected Loss</strong>: Exposure $= 50 + \\frac{1,050}{1.03} = 1,069.42\\text{ USD}$. $EL_1 = 0.02 \\times 0.60 \\times 1,069.42 = 12.83\\text{ USD}$. $PV(EL_1) = \\frac{12.83}{1.03} = 12.46\\text{ USD}$.</li>
      <li><strong>Year 2 Expected Loss</strong>: Unconditional $PD_2 = (1 - 0.02) \\times 0.02 = 1.96\\%$. Exposure $= 1,050\\text{ USD}$. $EL_2 = 0.0196 \\times 0.60 \\times 1,050 = 12.35\\text{ USD}$. $PV(EL_2) = \\frac{12.35}{1.03^2} = 11.64\\text{ USD}$.</li>
      <li><strong>CVA &amp; Fair Risky Value</strong>: $CVA = 12.46 + 11.64 = 24.10\\text{ USD} \\implies V_{\\text{Risky}} = 1,038.27 - 24.10 = 1,014.17\\text{ USD}$.</li>
    </ol>
  </div>

  <div class="card" style="background: rgba(16, 185, 129, 0.05); border-left: 4px solid var(--accent-emerald); margin: 15px 0;">
    <h4 style="margin: 0 0 10px 0; color: var(--accent-emerald);">Worked Numerical Example 9: CDS Upfront Payment &amp; Mark-to-Market Valuation</h4>
    <p><strong>Scenario</strong>: An investor buys 10,000,000 USD notional of 5-year high-yield CDS protection (standardized fixed coupon = 500 bps) when the market CDS spread is 620 bps and $EffDur_{\\text{CDS}} = 4.2$.</p>
    <ol>
      <li><strong>Initial Upfront Payment</strong>: $(6.20\\% - 5.00\\%) \\times 4.2 = 1.20\\% \\times 4.2 = 5.04\\%$ of notional ($504,000\\text{ USD}$ paid by buyer to seller at initiation).</li>
      <li><strong>Mark-to-Market After Spread Widening</strong>: Suppose credit fundamentals deteriorate and the CDS spread widens by $+80\\text{ bps}$ to 700 bps (new duration $= 4.0$):
        $$\\text{Buyer MTM Gain} \\approx +0.0080 \\times 4.0 \\times 10,000,000\\text{ USD} = +320,000\\text{ USD}$$
      </li>
    </ol>
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

  <h3 class="subheading">Collateralized Mortgage Obligations (CMO), CMBS, CDO &amp; Covered Bonds (CBOK VII)</h3>
  <ul>
    <li><strong>Sequential-Pay Tranches</strong>: Principal payments retire tranches in sequential order (Tranche A first, then B, then C). Early tranches absorb contraction risk; later tranches absorb extension risk.</li>
    <li><strong>PAC &amp; Support Tranches</strong>: Planned Amortization Class (PAC) tranches provide stable cash flows within a specified prepayment collar. The support tranche absorbs prepayments above or below the band, exhibiting high volatility.</li>
    <li><strong>Commercial MBS (CMBS) &amp; Credit Enhancement</strong>: Non-recourse loans analyzed via <em>DSCR</em> ($\\text{NOI} / \\text{Debt Service}$) and <em>LTV</em>. Call protection is embedded via lockout, defeasance, and yield maintenance. ABS/CDO waterfalls combine internal credit enhancement (overcollateralization, subordination, excess spread) to shield senior tranches.</li>
    <li><strong>Covered Bonds</strong>: On-balance-sheet senior debt backed by <strong>dual recourse</strong>—both to the issuing financial institution and to a ring-fenced, dynamic cover pool (non-performing loans must be replaced). Redemption structures include <em>hard-bullet</em>, <em>soft-bullet</em>, and <em>conditional pass-through</em>.</li>
  </ul>

  <div class="card" style="background: rgba(59, 130, 246, 0.05); border-left: 4px solid var(--accent-blue); margin: 15px 0;">
    <h4 style="margin: 0 0 10px 0; color: var(--accent-blue);">Worked Numerical Example 10: MBS Prepayment Speed (PSA, CPR &amp; SMM)</h4>
    <p><strong>Scenario</strong>: A residential mortgage pass-through pool has a beginning balance of 50,000,000 USD in Month 20, scheduled principal payment of 180,000 USD, and prepays at 150% PSA.</p>
    <ol>
      <li><strong>100% PSA Benchmark CPR (Month 20)</strong>: Ramps linearly at 0.20% per month up to Month 30 ($6.0\\%$): $\\text{CPR}_{100\\%}(20) = 6.0\\% \\times \\frac{20}{30} = 4.00\\%$.</li>
      <li><strong>150% PSA CPR</strong>: $\\text{CPR}_{150\\%} = 1.50 \\times 4.00\\% = 6.00\\%$.</li>
      <li><strong>Single Monthly Mortality (SMM)</strong>: $SMM = 1 - (1 - 0.060)^{1/12} = 0.005143 \\; (0.5143\\%)$.</li>
      <li><strong>Monthly Principal Prepayment</strong>: $0.005143 \\times (50,000,000 - 180,000) = 256,225\\text{ USD}$.</li>
    </ol>
  </div>

  <div class="card" style="background: rgba(147, 51, 234, 0.05); border-left: 4px solid var(--accent-purple); margin: 15px 0;">
    <h4 style="margin: 0 0 10px 0; color: var(--accent-purple);">Worked Numerical Example 11: ABS / CDO Subordination Waterfall</h4>
    <p><strong>Scenario</strong>: A 100,000,000 USD collateralized debt structure issues Senior Tranche (75,000,000 USD), Mezzanine Tranche (15,000,000 USD), and Equity/First-Loss Tranche (10,000,000 USD). Cumulative net default losses reach 18,000,000 USD.</p>
    <ul>
      <li><strong>Equity Tranche</strong>: Absorbs the first 10,000,000 USD of losses $\\implies$ completely wiped out (0 USD remaining).</li>
      <li><strong>Mezzanine Tranche</strong>: Absorbs remaining $18,000,000 - 10,000,000 = 8,000,000\\text{ USD}$ $\\implies$ impaired to 7,000,000 USD principal.</li>
      <li><strong>Senior Tranche</strong>: Fully protected by 25% subordination buffer $\\implies$ 75,000,000 USD principal remains 100% intact.</li>
    </ul>
  </div>
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
        <tr>
          <td><strong>Repo</strong></td>
          <td>Repurchase Price</td>
          <td>$$P_{\\text{rep}} = MV(1 - h)\\left(1 + r_{\\text{repo}} \\frac{\\text{Days}}{360}\\right)$$</td>
          <td>Short-term collateralized financing &amp; bond shorting.</td>
        </tr>
        <tr>
          <td><strong>Convertibles</strong></td>
          <td>Min. Convertible Value</td>
          <td>$$V_{\\min} = \\max(\\text{Straight Value}, \\text{CR} \\times P_{\\text{stock}})$$</td>
          <td>Floor valuation combining debt &amp; equity parity.</td>
        </tr>
        <tr>
          <td><strong>CDS</strong></td>
          <td>CDS Upfront (%)</td>
          <td>$$\\text{Upfront} \\approx (S_{\\text{CDS}} - C_{\\text{fixed}}) \\times EffDur_{\\text{CDS}}$$</td>
          <td>Upfront compensation between market spread &amp; fixed coupon.</td>
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

  <h3 class="subheading">Shorting Equity Securities, Voting Jurisdictions &amp; Market Efficiency (CBOK VI &amp; 2027 L1)</h3>
  <ul>
    <li><strong>Shorting Equities &amp; Short Margin Call</strong>: A short seller borrows shares through a broker, sells them at $P_0$, deposits initial margin ($IM$), and remains liable for dividends paid during the short period plus any stock loan fee. The broker pays interest on cash proceeds minus the loan fee (the <strong>short rebate rate</strong>; hard-to-borrow stocks carry negative rebate rates and risk a <em>short squeeze</em>). Trigger price for a short margin call:
      $$P_{\\text{Short Call}} = P_0 \\times \\left(\\frac{1 + IM}{1 + MM}\\right)$$
    </li>
    <li><strong>Equity Features, Jurisdictions &amp; Depositary Receipts (2027 L1 LM1–LM2)</strong>: <em>Statutory voting</em> assigns one vote per share per board seat; <em>cumulative voting</em> lets minority shareholders concentrate votes ($\\text{shares} \\times \\text{seats}$) onto a single director. Dual-class shares grant superior voting rights to founders. <strong>ADRs</strong> (Level I OTC, Level II listed, Level III capital-raising, Rule 144A private) vs. <strong>GDRs</strong> trade foreign equities across borders. Preference shares may be cumulative, participating, callable, or convertible.</li>
    <li><strong>Market Efficiency &amp; Anomalies (EMH)</strong>: <em>Weak-form</em> rejects technical analysis; <em>Semi-strong-form</em> rejects both technical and fundamental analysis of public data; <em>Strong-form</em> prices reflect even private insider information. Apparent calendar, size, value, or momentum anomalies often stem from unmodeled risk factors, behavioral biases, or data mining.</li>
  </ul>

  <div class="card" style="background: rgba(16, 185, 129, 0.05); border-left: 4px solid var(--accent-emerald); margin: 15px 0;">
    <h4 style="margin: 0 0 10px 0; color: var(--accent-emerald);">Worked Numerical Example 1: Long &amp; Short Margin Call Triggers &amp; Leveraged Return</h4>
    <p><strong>Scenario</strong>: Initial margin $IM = 50\\%$, maintenance margin $MM = 30\\%$, initial stock price $P_0 = 80.00\\text{ USD}$ on 1,000 shares.</p>
    <ol>
      <li><strong>Long Position Margin Call Price</strong>: $P_{\\text{Long Call}} = 80.00 \\times \\frac{1 - 0.50}{1 - 0.30} = 80.00 \\times \\frac{0.50}{0.70} = 57.14\\text{ USD}$.</li>
      <li><strong>Long Leveraged Return</strong>: If stock rises to 96.00 USD, pays 2.00 USD/share dividend, and margin loan interest on 40,000 USD is 6.0% ($2,400\\text{ USD}$):
        $$R_{\\text{Leveraged}} = \\frac{1,000(96 - 80) + 1,000(2) - 2,400}{40,000} = \\frac{15,600}{40,000} = 39.00\\%$$
      </li>
      <li><strong>Short Sale Margin Call Price</strong>: $P_{\\text{Short Call}} = 80.00 \\times \\frac{1 + 0.50}{1 + 0.30} = 80.00 \\times \\frac{1.50}{1.30} = 92.31\\text{ USD}$.</li>
    </ol>
  </div>

  <div class="card" style="background: rgba(59, 130, 246, 0.05); border-left: 4px solid var(--accent-blue); margin: 15px 0;">
    <h4 style="margin: 0 0 10px 0; color: var(--accent-blue);">Worked Numerical Example 2: Price-Weighted, Market-Cap-Weighted &amp; Equal-Weighted Index Returns</h4>
    <p><strong>Scenario</strong>: A 3-stock index consists of Stock A ($P_0=100, Q=1\\text{M} \\to P_1=110$), Stock B ($P_0=50, Q=4\\text{M} \\to P_1=55$), and Stock C ($P_0=30, Q=10\\text{M} \\to P_1=27$).</p>
    <ul>
      <li><strong>Price-Weighted Return</strong>: $\\text{Index}_0 = \\frac{100+50+30}{3} = 60.00$, $\\text{Index}_1 = \\frac{110+55+27}{3} = 64.00 \\implies R_{PW} = \\frac{64}{60} - 1 = +6.67\\%$. If Stock A executes a 2-for-1 split at $t=0$ ($P_A \\to 50$), the new divisor is $d_{\\text{new}} = \\frac{50+50+30}{60.00} = 2.1667$.</li>
      <li><strong>Market-Cap Weighted Return</strong>: $MC_0 = 100 + 200 + 300 = 600\\text{M}$, $MC_1 = 110 + 220 + 270 = 600\\text{M} \\implies R_{MCW} = 0.00\\%$.</li>
      <li><strong>Equal-Weighted Return</strong>: $\\frac{1}{3}(+10.0\\% + 10.0\\% - 10.0\\%) = +3.33\\%$.</li>
    </ul>
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

  <h3 class="subheading">Financial Statement Forecasting, Research Reports &amp; ESG Integration (2027 L1 &amp; CBOK VI)</h3>
  <ul>
    <li><strong>Disaggregated Financial Forecasting</strong>: Combine <em>Top-Down</em> drivers (GDP growth, market share) with <em>Bottom-Up</em> unit drivers (stores $\\times$ sales/store, volume $\\times$ ASP). Model COGS and SG&amp;A separately via fixed vs. variable operating leverage, working capital via DSO/DIO/DPO days, and CapEx into maintenance vs. growth buckets.</li>
    <li><strong>Equity Analyst Research Reports</strong>: <em>Initiation of Coverage</em> reports cover company overview, industry Porter analysis, financial forecasts, valuation, investment risks, and ESG factors; <em>Update Reports</em> analyze quarterly earnings surprises and catalyst revisions. Sell-side reports serve external institutional/retail clients; buy-side research serves internal portfolio managers.</li>
    <li><strong>Sustainability / ESG in Equity Valuation</strong>: Material ESG risks translate into DCF inputs—adjusting revenue growth (green demand / carbon regulation), operating margins (transition costs), cost of capital (beta/credit spread), or terminal value (stranded assets).</li>
  </ul>

  <div class="card" style="background: rgba(147, 51, 234, 0.05); border-left: 4px solid var(--accent-purple); margin: 15px 0;">
    <h4 style="margin: 0 0 10px 0; color: var(--accent-purple);">Worked Numerical Example 3: Probability-Weighted Scenario Valuation</h4>
    <p><strong>Scenario</strong>: Following disaggregated financial modeling across three macro/regulatory scenarios, an equity analyst estimates intrinsic equity values of 58.00 USD (Bull, 25% probability), 46.00 USD (Base, 50% probability), and 32.00 USD (Bear, 25% probability). Current market price is 40.00 USD.</p>
    $$E(V_0) = (0.25 \\times 58.00) + (0.50 \\times 46.00) + (0.25 \\times 32.00) = 14.50 + 23.00 + 8.00 = 45.50\\text{ USD}$$
    <p><strong>Implied Upside</strong>: $\\frac{45.50 - 40.00}{40.00} = +13.75\\% \\implies$ <em>Buy / Outperform</em> recommendation.</p>
  </div>
</section>

<!-- ========================================================================================= -->
<!-- MODULE 3: DIVIDEND DISCOUNT MODELS (DDM) -->
<!-- ========================================================================================= -->
<section id="eq-m3-ddm" class="notes-chapter">
  <h2 class="section-heading"><span class="num">03.</span> Dividend Discount Models & Multi-Stage Valuation</h2>
  <p>The Dividend Discount Model (DDM) values common stock as the present value of all expected future cash dividend payments discounted at the required return on equity ($r$).</p>

  <h3 class="subheading">Cost of Equity Estimation Models (2027 L1 LM12 &amp; L2 Return Concepts)</h3>
  <div class="formula-card">
    <div class="formula-title">CAPM, Blume Adjusted Beta, Expanded CAPM &amp; Country Risk Premium</div>
    $$r_{\\text{CAPM}} = R_f + \\beta_{\\text{adj}} \\times ERP, \\qquad \\beta_{\\text{adj}} = \\frac{2}{3}\\beta_{\\text{raw}} + \\frac{1}{3}(1.0)$$
    $$r_{\\text{Expanded CAPM}} = R_f + \\beta_{\\text{peer}}(ERP) + SP + IP + SCRP$$
    $$CRP = \\text{Sovereign Yield Spread} \\times \\left(\\frac{\\sigma_{\\text{Equity}}}{\\sigma_{\\text{Bond}}}\\right), \\qquad r_{\\text{BYPRP}} = \\text{Bond Yield} + \\text{Risk Premium}$$
    $$\\text{Fama-French 3-Factor + Liquidity: } r = R_f + \\beta_{mkt}ERP + \\beta_{size}SMB + \\beta_{val}HML + \\beta_{liq}LIQ$$
  </div>

  <div class="card" style="background: rgba(245, 158, 11, 0.05); border-left: 4px solid var(--accent-amber); margin: 15px 0;">
    <h4 style="margin: 0 0 10px 0; color: var(--accent-amber);">Worked Numerical Example 4: Adjusted Beta, Country Risk Premium &amp; Expanded CAPM</h4>
    <p><strong>Scenario</strong>: An emerging-market mid-cap stock has raw historical $\\beta_{\\text{raw}} = 1.30$, risk-free rate $R_f = 4.00\\%$, developed ERP $= 5.00\\%$, small-stock premium $SP = 1.50\\%$, company-specific risk premium $SCRP = 1.00\\%$, sovereign yield spread $= 1.80\\%$, and equity-to-sovereign-bond volatility ratio $= 1.25$.</p>
    <ol>
      <li><strong>Blume's Adjusted Beta</strong>: $\\beta_{\\text{adj}} = \\frac{2}{3}(1.30) + \\frac{1}{3}(1.00) = 1.20$.</li>
      <li><strong>Country Risk Premium (CRP)</strong>: $CRP = 1.80\\% \\times 1.25 = 2.25\\%$.</li>
      <li><strong>Required Return on Equity</strong>: $r = 4.00\\% + 1.20(5.00\\%) + 1.50\\% + 1.00\\% + 2.25\\% = 14.75\\%$.</li>
    </ol>
  </div>

  <h3 class="subheading">Gordon Growth Model &amp; Sustainable Growth Rate (PRAT)</h3>
  <div class="formula-card">
    <div class="formula-title">Constant Growth DDM (Gordon Growth)</div>
    $$V_0 = \\frac{D_1}{r - g} = \\frac{D_0 (1 + g)}{r - g} \\quad (\\text{Condition: } r > g)$$
    $$g = b \\times ROE = \\left(\\frac{NI - Div}{NI}\\right) \\times \\left(\\frac{NI}{Sales}\\right) \\times \\left(\\frac{Sales}{Assets}\\right) \\times \\left(\\frac{Assets}{Equity}\\right) \\quad (\\text{PRAT Model})$$
  </div>

  <h3 class="subheading">Present Value of Growth Opportunities (PVGO)</h3>
  <p>A firm's stock value can be decomposed into the value of its current no-growth earnings stream plus the net present value of profitable growth investments:</p>
  <div class="formula-card">
    <div class="formula-title">PVGO Decomposition</div>
    $$V_0 = \\frac{E_1}{r} + PVGO \\implies PVGO = V_0 - \\frac{E_1}{r}$$
  </div>

  <div class="card" style="background: rgba(16, 185, 129, 0.05); border-left: 4px solid var(--accent-emerald); margin: 15px 0;">
    <h4 style="margin: 0 0 10px 0; color: var(--accent-emerald);">Worked Numerical Example 5: Gordon Growth, PRAT &amp; PVGO Decomposition</h4>
    <p><strong>Scenario</strong>: Expected next-year EPS $E_1 = 5.00\\text{ USD}$, Dividend Payout Ratio $= 50\\%$ ($b = 0.50$, $D_1 = 2.50\\text{ USD}$), $ROE = 16.0\\%$, and required equity return $r = 12.0\\%$.</p>
    <ul>
      <li><strong>Sustainable Growth Rate</strong>: $g = 0.50 \\times 16.0\\% = 8.00\\%$.</li>
      <li><strong>Gordon Growth Intrinsic Value</strong>: $V_0 = \\frac{2.50}{0.12 - 0.08} = 62.50\\text{ USD}$.</li>
      <li><strong>No-Growth Value &amp; PVGO</strong>: $\\frac{E_1}{r} = \\frac{5.00}{0.12} = 41.67\\text{ USD} \\implies PVGO = 62.50 - 41.67 = 20.83\\text{ USD}$ (33.3% of total stock value comes from future growth opportunities!).</li>
    </ul>
  </div>

  <h3 class="subheading">The H-Model for Linearly Transitioning Growth</h3>
  <p>The H-Model values a firm experiencing high initial growth ($g_S$) that transitions linearly over half-life $H$ (years $= 2H$) to a sustainable long-term rate ($g_L$):</p>
  <div class="formula-card">
    <div class="formula-title">H-Model Valuation Equation</div>
    $$V_0 = \\frac{D_0 (1 + g_L)}{r - g_L} + \\frac{D_0 \\times H \\times (g_S - g_L)}{r - g_L}, \\qquad r_{\\text{implied}} = \\left(\\frac{D_0}{P_0}\\right)[(1 + g_L) + H(g_S - g_L)] + g_L$$
  </div>

  <div class="card" style="background: rgba(59, 130, 246, 0.05); border-left: 4px solid var(--accent-blue); margin: 15px 0;">
    <h4 style="margin: 0 0 10px 0; color: var(--accent-blue);">Worked Numerical Example 6: H-Model Valuation &amp; Implied Expected Return</h4>
    <p><strong>Scenario</strong>: A firm just paid $D_0 = 2.00\\text{ USD}$. Dividend growth starts at $g_S = 14.0\\%$ and declines linearly over 8 years ($H = 4$) to $g_L = 4.0\\%$. Required return $r = 10.0\\%$.</p>
    <ol>
      <li><strong>Intrinsic Value ($V_0$)</strong>:
        $$V_0 = \\frac{2.00(1.04) + 2.00(4)(0.14 - 0.04)}{0.10 - 0.04} = \\frac{2.08 + 0.80}{0.06} = \\frac{2.88}{0.06} = 48.00\\text{ USD}$$
      </li>
      <li><strong>Implied Expected Return if Market Price $P_0 = 52.00\\text{ USD}$</strong>:
        $$r_{\\text{implied}} = \\frac{2.00}{52.00}(1.04 + 0.40) + 0.04 = \\frac{2.88}{52.00} + 0.04 = 5.54\\% + 4.00\\% = 9.54\\%$$
      </li>
    </ol>
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

  <div class="card" style="background: rgba(16, 185, 129, 0.05); border-left: 4px solid var(--accent-emerald); margin: 15px 0;">
    <h4 style="margin: 0 0 10px 0; color: var(--accent-emerald);">Worked Numerical Example 7: FCFF &amp; FCFE Derivation and Firm Valuation</h4>
    <p><strong>Scenario</strong>: A firm reports Net Income $= 120\\text{M USD}$, Depreciation (NCC) $= 35\\text{M USD}$, Interest Expense $= 20\\text{M USD}$, Tax Rate $T = 25\\%$, Capital Expenditures ($FCInv$) $= 50\\text{M USD}$, Working Capital Investment ($WCInv$) $= 15\\text{M USD}$, and Net Debt Borrowing $= +10\\text{M USD}$. $WACC = 9.0\\%$, perpetual growth $g = 4.0\\%$, and market value of debt $= 400\\text{M USD}$.</p>
    <ol>
      <li><strong>Free Cash Flow to Firm ($FCFF_0$)</strong>:
        $$FCFF_0 = 120 + 35 + 20(1 - 0.25) - 50 - 15 = 120 + 35 + 15 - 50 - 15 = 105.00\\text{M USD}$$
      </li>
      <li><strong>Free Cash Flow to Equity ($FCFE_0$)</strong>:
        $$FCFE_0 = 105.00 - 20(1 - 0.25) + 10 = 105.00 - 15.00 + 10.00 = 100.00\\text{M USD}$$
      </li>
      <li><strong>Intrinsic Firm &amp; Equity Value</strong>:
        $$V_{\\text{Firm}} = \\frac{105.00(1.04)}{0.09 - 0.04} = \\frac{109.20}{0.05} = 2,184.00\\text{M USD} \\implies V_{\\text{Equity}} = 2,184.00 - 400.00 = 1,784.00\\text{M USD}$$
      </li>
    </ol>
    <p><em>Exam Trap</em>: Ignore non-cash share-based compensation add-backs if analysts treat SBC as a real economic dilution cost; always add back after-tax interest to Net Income/CFO when computing FCFF, NEVER pre-tax interest.</p>
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

  <h3 class="subheading">Enterprise Value Multipliers, Harmonic Mean &amp; Sum-of-the-Parts (SOTP)</h3>
  <p><strong>Enterprise Value ($EV$)</strong> measures total market value of core operations independent of capital structure financing:</p>
  <div class="formula-card">
    <div class="formula-title">Enterprise Value, PEG &amp; Harmonic Mean Identities</div>
    $$EV = \\text{Market Value of Common Equity} + \\text{Total Debt} + \\text{Preferred Stock} + \\text{Minority Interest} - \\text{Cash &amp; Equivalents}$$
    $$\\text{PEG Ratio} = \\frac{P/E}{g \\text{ (in whole \\%)}}, \\qquad \\bar{X}_{H} = \\frac{n}{\\sum_{i=1}^n (1 / X_i)}$$
  </div>
  <p><strong>CFA Exam Rule on Peer Multiples</strong>: When averaging peer P/E multiples containing high positive outliers (e.g., depressed earnings), the <strong>Harmonic Mean</strong> mitigates extreme upward skew compared to the arithmetic mean. For diversified conglomerates, use <strong>Sum-of-the-Parts (SOTP)</strong> valuation—applying distinct EV/EBITDA or P/E multiples to each operating segment before subtracting net debt.</p>

  <div class="card" style="background: rgba(147, 51, 234, 0.05); border-left: 4px solid var(--accent-purple); margin: 15px 0;">
    <h4 style="margin: 0 0 10px 0; color: var(--accent-purple);">Worked Numerical Example 8: Justified Multiples &amp; Harmonic Mean Benchmark</h4>
    <p><strong>Part A (Justified Fundamentals)</strong>: A company earns $ROE = 15.0\\%$, retains $b = 40\\%$ ($g = 0.40 \\times 15.0\\% = 6.0\\%$), and has required return $r = 10.0\\%$.</p>
    <ul>
      <li><strong>Justified Leading P/E</strong>: $\\frac{1 - 0.40}{0.10 - 0.06} = \\frac{0.60}{0.04} = 15.00\\times$. <strong>Justified Trailing P/E</strong>: $15.00 \\times 1.06 = 15.90\\times$.</li>
      <li><strong>Justified P/B</strong>: $\\frac{ROE - g}{r - g} = \\frac{0.15 - 0.06}{0.10 - 0.06} = 2.25\\times$.</li>
    </ul>
    <p><strong>Part B (Harmonic vs. Arithmetic Mean)</strong>: Three industry peers trade at P/E ratios of $12.0\\times$, $15.0\\times$, and $60.0\\times$.</p>
    $$\\text{Arithmetic Mean} = \\frac{12 + 15 + 60}{3} = 29.00\\times, \\qquad \\text{Harmonic Mean } \\bar{X}_H = \\frac{3}{\\frac{1}{12} + \\frac{1}{15} + \\frac{1}{60}} = \\frac{3}{0.1667} = 18.00\\times$$
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

  <h3 class="subheading">Continuing Residual Income, Persistence ($\\omega$) &amp; EVA / MVA</h3>
  <p>Under competitive market dynamics, supernormal returns decay over time to normal returns ($ROE \\to r$). Related economic metrics include <strong>Economic Value Added (EVA)</strong> $= NOPAT - (WACC \\times \\text{Invested Capital})$ and <strong>Market Value Added (MVA)</strong> $= \\text{Market Value} - \\text{Invested Capital}$:</p>
  <div class="formula-card">
    <div class="formula-title">Terminal Value with Persistence Decay ($\\omega$)</div>
    $$PV(\\text{Continuing RI at } T-1) = \\frac{RI_T}{1 + r - \\omega}$$
    $$\\text{Where } \\omega \\in [0, 1]: \\quad \\omega = 1.0 \\implies \\text{Perpetual RI}, \\quad \\omega = 0.0 \\implies \\text{Instant Return to Cost of Equity}$$
  </div>

  <div class="card" style="background: rgba(245, 158, 11, 0.05); border-left: 4px solid var(--accent-amber); margin: 15px 0;">
    <h4 style="margin: 0 0 10px 0; color: var(--accent-amber);">Worked Numerical Example 9: Multi-Stage Residual Income with Persistence Decay</h4>
    <p><strong>Scenario</strong>: Beginning book value $B_0 = 20.00\\text{ USD}$, cost of equity $r = 10.0\\%$. Forecasts: Year 1 ($EPS_1 = 4.00, D_1 = 1.00$), Year 2 ($EPS_2 = 4.50, D_2 = 1.20$), Year 3 ($EPS_3 = 4.80, D_3 = 1.30$). After Year 3, residual income decays with persistence factor $\\omega = 0.60$.</p>
    <ol>
      <li><strong>Year 1</strong>: $RI_1 = 4.00 - 0.10(20.00) = 2.00\\text{ USD}$; $B_1 = 20.00 + 4.00 - 1.00 = 23.00\\text{ USD}$.</li>
      <li><strong>Year 2</strong>: $RI_2 = 4.50 - 0.10(23.00) = 2.20\\text{ USD}$; $B_2 = 23.00 + 4.50 - 1.20 = 26.30\\text{ USD}$.</li>
      <li><strong>Year 3</strong>: $RI_3 = 4.80 - 0.10(26.30) = 2.17\\text{ USD}$.</li>
      <li><strong>PV of Continuing RI at $t=2$</strong>: $\\frac{RI_3}{1 + r - \\omega} = \\frac{2.17}{1 + 0.10 - 0.60} = \\frac{2.17}{0.50} = 4.34\\text{ USD}$.</li>
      <li><strong>Intrinsic Equity Value ($V_0$)</strong>:
        $$V_0 = 20.00 + \\frac{2.00}{1.10} + \\frac{2.20 + 4.34}{(1.10)^2} = 20.00 + 1.818 + 5.405 = 27.22\\text{ USD}$$
      </li>
    </ol>
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

  <h3 class="subheading">Private Company Methods: Excess Earnings Method (EEM), GPCM, GTM &amp; Discounts</h3>
  <p>Private equity appraisals apply three main approaches: <strong>Income Approach</strong> (FCF and the <em>Excess Earnings Method [EEM]</em> for intangible-heavy firms), <strong>Market Approach</strong> (<em>Guideline Public Company Method [GPCM]</em>, <em>Guideline Transactions Method [GTM]</em>, and <em>Prior Transaction Method [PTM]</em>), and <strong>Asset-Based Approach</strong> (adjusted book value).</p>
  <div class="formula-card">
    <div class="formula-title">Control and Marketability Discount Interaction</div>
    $$\\text{Total Combined Discount} = 1 - (1 - DLOC) \\times (1 - DLOM)$$
    $$DLOC = 1 - \\left( \\frac{1}{1 + \\text{Control Premium}} \\right)$$
    $$\\text{Where: } DLOC = \\text{Discount for Lack of Control}, \\quad DLOM = \\text{Discount for Lack of Marketability}$$
  </div>

  <div class="card" style="background: rgba(16, 185, 129, 0.05); border-left: 4px solid var(--accent-emerald); margin: 15px 0;">
    <h4 style="margin: 0 0 10px 0; color: var(--accent-emerald);">Worked Numerical Example 10: Excess Earnings Method (EEM) Private Firm Valuation</h4>
    <p><strong>Scenario</strong>: A private firm generates normalized EBIT $= 360,000\\text{ USD}$ (25% tax rate). Working capital $= 500,000\\text{ USD}$ (6.0% required return), Fixed Assets $= 1,200,000\\text{ USD}$ (10.0% required return), intangible asset capitalization rate $= 18.0\\%$, and perpetual intangible growth $= 3.0\\%$.</p>
    <ol>
      <li><strong>Normalized NOPAT</strong>: $360,000 \\times (1 - 0.25) = 270,000\\text{ USD}$.</li>
      <li><strong>Required Returns on Tangible Assets</strong>: $WC = 500,000 \\times 0.06 = 30,000\\text{ USD}$; $FA = 1,200,000 \\times 0.10 = 120,000\\text{ USD}$.</li>
      <li><strong>Residual Intangible Income</strong>: $270,000 - (30,000 + 120,000) = 120,000\\text{ USD}$.</li>
      <li><strong>Intangible Value &amp; Total Firm Value</strong>:
        $$V_{\\text{Intangible}} = \\frac{120,000(1.03)}{0.18 - 0.03} = 824,000\\text{ USD} \\implies V_{\\text{Firm}} = 500,000 + 1,200,000 + 824,000 = 2,524,000\\text{ USD}$$
      </li>
    </ol>
  </div>

  <div class="card" style="background: rgba(59, 130, 246, 0.05); border-left: 4px solid var(--accent-blue); margin: 15px 0;">
    <h4 style="margin: 0 0 10px 0; color: var(--accent-blue);">Worked Numerical Example 11: DLOC &amp; DLOM Multiplicative Discounting</h4>
    <p><strong>Scenario</strong>: A controlling equity stake in a private company is valued at 10,000,000 USD. Guideline transaction control premiums average 25.0%, and the estimated DLOM is 15.0%. Value a non-controlling, non-marketable minority stake.</p>
    <ol>
      <li><strong>Discount for Lack of Control ($DLOC$)</strong>: $1 - \\frac{1}{1 + 0.25} = 1 - 0.80 = 20.0\\%$.</li>
      <li><strong>Total Multiplicative Discount</strong>: $1 - (1 - 0.20)(1 - 0.15) = 1 - (0.80 \\times 0.85) = 1 - 0.68 = 32.0\\%$ (NOT $20\\% + 15\\% = 35\\%$!).</li>
      <li><strong>Implied Minority Non-Marketable Value</strong>: $10,000,000 \\times (1 - 0.32) = 6,800,000\\text{ USD}$.</li>
    </ol>
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
        <tr>
          <td><strong>Trading</strong></td>
          <td>Short Margin Call</td>
          <td>$$P_{\\text{call}} = P_0 \\left(\\frac{1 + IM}{1 + MM}\\right)$$</td>
          <td>Short sale collateral trigger price when shares rally.</td>
        </tr>
        <tr>
          <td><strong>Cost of Equity</strong></td>
          <td>Blume Adj. Beta &amp; CRP</td>
          <td>$$\\beta_{\\text{adj}} = \\frac{2}{3}\\beta_{\\text{raw}} + \\frac{1}{3}, \\quad CRP = \\Delta y_{\\text{sov}}\\frac{\\sigma_{\\text{eq}}}{\\sigma_{\\text{bond}}}$$</td>
          <td>Forward-looking beta mean reversion &amp; emerging market risk.</td>
        </tr>
        <tr>
          <td><strong>Multipliers</strong></td>
          <td>Harmonic Mean P/E</td>
          <td>$$\\bar{X}_H = \\frac{n}{\\sum_{i=1}^n (1/X_i)}$$</td>
          <td>Eliminates upward outlier distortion in peer multiples.</td>
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

pm_html = r"""<div class="top-controls">
  <button class="btn-ctrl" onclick="toggleTheme()">🌓 Switch Theme</button>
  <button class="btn-ctrl" onclick="window.print()">🖨️ Print / Save as PDF</button>
</div>

<div class="doc-hero">
  <h1>Portfolio Management &amp; Wealth Planning Master Reference Library</h1>
  <p>The curriculum-complete master study guide synthesized for CFA&reg; Level 1 and Level 2 candidates. Covering institutional governance, investment policy statements (IPS), return/risk mechanics, Modern Portfolio Theory (MPT), Capital Market Expectations (Grinold-Kroner &amp; Singer-Terhaar), Grinold's Fundamental Law of Active Management, multifactor risk attribution, and algorithmic trade execution &amp; Implementation Shortfall.</p>
  <div class="meta-tags">
    <span class="badge badge-cyan">CFA Exam Syllabus (L1 &amp; L2)</span>
    <span class="badge badge-blue">Portfolio Management Core</span>
    <span class="badge badge-purple">Active Management &amp; Attributions</span>
    <span class="badge badge-amber">Execution &amp; Microstructure</span>
  </div>
</div>

<div class="card" style="margin-top: 15px; margin-bottom: 25px;">
  <div class="card-title">📈 Quick Navigation: Portfolio Management Curriculum Modules</div>
  <div class="fsa-nav-bar">
    <a class="fsa-nav-btn" href="#pm-m1-matrix">01. Institutional Matrix &amp; Overview</a>
    <a class="fsa-nav-btn" href="#pm-m2-returns">02. Return &amp; Risk Mechanics</a>
    <a class="fsa-nav-btn" href="#pm-m3-mpt">03. MPT &amp; Asset Pricing</a>
    <a class="fsa-nav-btn" href="#pm-m4-planning">04. IPS &amp; Asset Allocation</a>
    <a class="fsa-nav-btn" href="#pm-m5-cme">05. CME &amp; Macro Risk Premia</a>
    <a class="fsa-nav-btn" href="#pm-m6-active">06. Active Management &amp; Fundamental Law</a>
    <a class="fsa-nav-btn" href="#pm-m7-multifactor">07. Multifactor Risk Models</a>
    <a class="fsa-nav-btn" href="#pm-m8-execution">08. ETFs, Algos &amp; Implementation Shortfall</a>
    <a class="fsa-nav-btn" href="#pm-m10-cbok1112">09. Asset Allocation &amp; Perf (CBOK XI-XII)</a>
    <a class="fsa-nav-btn" href="#pm-formulas" style="color: var(--accent-emerald); font-weight: 700;">Master Formula Sheet</a>
  </div>
</div>

<!-- ========================================================================================= -->
<!-- MODULE 1: INSTITUTIONAL MATRIX & PORTFOLIO MANAGEMENT OVERVIEW -->
<!-- ========================================================================================= -->
<section id="pm-m1-matrix" class="notes-chapter">
  <h2 class="section-heading"><span class="num">01.</span> Portfolio Management Overview, Client Types &amp; Institutional Matrix</h2>
  <p>The portfolio management process is an ongoing dynamic framework consisting of three continuous operational phases: <strong>Planning</strong> (identifying client objectives and constraints, drafting the IPS, forming CME, establishing SAA), <strong>Execution</strong> (portfolio construction, tactical tilts, and security implementation), and <strong>Feedback</strong> (performance measurement, attribution, monitoring, and rebalancing).</p>

  <h3 class="subheading">Defined Benefit (DB) vs Defined Contribution (DC) Pension Plans</h3>
  <p>Retirement plans represent the largest institutional pools of capital globally. The economic distinction between DB and DC structures dictates liability modeling, investment horizon, and risk tolerance:</p>
  <ul>
    <li><strong>Defined Benefit (DB) Plans</strong>: The plan sponsor (employer) guarantees a defined periodic retirement payout based on a formula (years of service, final average salary). The <em>sponsor bears all investment risk and longevity risk</em>. If portfolio returns underperform or longevity exceeds actuarial projections, the plan incurs an underfunded deficit that the sponsor must remediate via cash contributions. Liabilities are long-term, fixed/inflation-linked cash flows discounted at high-grade corporate bond yields.</li>
    <li><strong>Defined Contribution (DC) Plans</strong>: The plan sponsor makes defined contributions into individual participant accounts. The <em>plan participant (employee) bears all investment risk and longevity risk</em>. The plan sponsor's obligation terminates once contributions are deposited. Asset allocation is directed by the employee based on lifecycle considerations and risk tolerance.</li>
  </ul>

  <h3 class="subheading">Comprehensive Institutional Investor Comparison Matrix</h3>
  <div class="table-wrap">
    <table>
      <thead>
        <tr>
          <th>Institution</th>
          <th>Time Horizon</th>
          <th>Risk Tolerance</th>
          <th>Liquidity Needs</th>
          <th>Tax Status</th>
          <th>Regulations &amp; Governance</th>
          <th>Return Objective &amp; Liabilities</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Defined Benefit (DB) Pension</strong></td>
          <td>Long (active workforce to retirement; shorter for frozen/mature plans)</td>
          <td>Moderate-to-High (rises with funded status, sponsor financial strength, and younger active workforce)</td>
          <td>Low-to-Moderate (retiree benefit payouts; net cash outflows for mature/closed plans)</td>
          <td>Tax-exempt in most jurisdictions</td>
          <td>ERISA (US), PBGC, prudent expert rule, minimum funding requirements</td>
          <td>Achieve discount rate / actuarial return hurdle (e.g., 6.0%–7.0%) while immunizing explicit pension obligations (PBO).</td>
        </tr>
        <tr>
          <td><strong>Defined Contribution (DC) Pension</strong></td>
          <td>Individual-specific (long for youth, short approaching retirement)</td>
          <td>Borne by participant; varies widely across demographic cohorts</td>
          <td>Low during accumulation; high at retirement or upon rollover/withdrawal</td>
          <td>Tax-deferred accumulation until retirement distribution</td>
          <td>ERISA, qualified default investment alternatives (QDIA), participant education rules</td>
          <td>Maximize wealth accumulation subject to individual lifecycle horizons; no contractual sponsor liability.</td>
        </tr>
        <tr>
          <td><strong>University Endowment</strong></td>
          <td>Perpetual / Multi-generational (intergenerational equity)</td>
          <td>High (long horizon and absence of contractual liabilities permit high alternative asset illiquidity)</td>
          <td>Low (typically 4.0%–5.0% annual spending policy rate plus capital calls)</td>
          <td>Tax-exempt (subject to minor US net investment excise tax for elite endowments)</td>
          <td>UPMIFA (Uniform Prudent Management of Institutional Funds Act)</td>
          <td>Maintain real purchasing power after spending and inflation: $r_{\text{req}} = \text{Spending Rate} + \text{HEPI} + \text{Investment Expenses}$.</td>
        </tr>
        <tr>
          <td><strong>Private Foundation</strong></td>
          <td>Perpetual (unless structured with a finite spend-down terminal date)</td>
          <td>Moderate-to-High (high capacity, but constrained by legal payout mandates)</td>
          <td>Moderate (US law mandates minimum 5.0% annual distribution of trailing net assets plus expenses)</td>
          <td>Tax-exempt (subject to 1.39% flat US federal excise tax on net investment income)</td>
          <td>Internal Revenue Code (IRC &sect;4942 mandatory 5% payout rule), UPMIFA</td>
          <td>Preserve real endowment corpus: $r_{\text{req}} = 5.0\% + \text{CPI} + \text{Management Fees}$.</td>
        </tr>
        <tr>
          <td><strong>Life Insurance Company</strong></td>
          <td>Long-term (multi-decade liabilities for whole life and guaranteed annuities)</td>
          <td>Low-to-Moderate (fiduciary solvency, conservative surplus protection, ALM duration matching)</td>
          <td>Low-to-Moderate (surrender values, policy loans, predictable mortality payouts)</td>
          <td>Fully taxable corporate income tax rate</td>
          <td>State insurance commissioners, NAIC Risk-Based Capital (RBC) formulas, Solvency II</td>
          <td>Earn a spread over contractually guaranteed crediting rates on policy reserves; duration-matched fixed income.</td>
        </tr>
        <tr>
          <td><strong>Non-Life (P&amp;C) Insurer</strong></td>
          <td>Short-to-Intermediate (claims settle rapidly over 1 to 3 years)</td>
          <td>Very Low (volatile underwriting cycles and unpredictable catastrophe shocks)</td>
          <td>Very High (unexpected catastrophe claims from hurricanes, earthquakes, and floods)</td>
          <td>Fully taxable corporate income tax rate</td>
          <td>State insurance commissioners, NAIC RBC standards, statutory accounting principles (SAP)</td>
          <td>Preserve policyholder surplus and capital adequacy; conservative liquid debt matching erratic claim schedules.</td>
        </tr>
        <tr>
          <td><strong>Commercial Bank</strong></td>
          <td>Short-term (asset/liability maturity mismatch; assets longer than deposits)</td>
          <td>Very Low (protect depositor principal and retain Tier 1 capital buffers)</td>
          <td>Very High (continuous demand deposit withdrawals, reserve requirements)</td>
          <td>Fully taxable corporate income tax rate</td>
          <td>Basel III (CET1 capital ratios, Liquidity Coverage Ratio LCR, Net Stable Funding Ratio NSFR)</td>
          <td>Maximize Net Interest Margin (NIM) spread over funding costs while strictly managing asset-liability duration gaps.</td>
        </tr>
        <tr>
          <td><strong>Sovereign Wealth Fund (SWF)</strong></td>
          <td>Varies by SWF mandate: Stabilization (Short), Savings/Intergenerational (Perpetual)</td>
          <td>Stabilization: Low; Savings/Heritage: High; Reserve: Moderate</td>
          <td>Stabilization: Very High (fiscal shock absorber); Savings: Very Low</td>
          <td>Tax-exempt in home jurisdiction; often sovereign immunity abroad</td>
          <td>Santiago Principles (Generally Accepted Principles and Practices - GAPP), domestic statutory laws</td>
          <td>Stabilization: Protect state budget from commodity price shocks; Savings: Diversify sovereign wealth for future generations.</td>
        </tr>
      </tbody>
    </table>
  </div>

  <h3 class="subheading">Endowment Spending Rules &amp; Intergenerational Equity (L2 Institutional PM)</h3>
  <ul>
    <li><strong>Simple / Constant Growth Rule</strong>: $\text{Spending}_t = \text{Spending}_{t-1} \times (1 + \pi)$. Protects purchasing power stability but ignores AUM drawdowns.</li>
    <li><strong>Rolling Average (Market-Value) Rule</strong>: $\text{Spending}_t = r \times \frac{1}{3}(AUM_{t-1} + AUM_{t-2} + AUM_{t-3})$. Smoothes market volatility over 3 years.</li>
    <li><strong>Geometric / Hybrid (Tobin) Rule</strong>: Balances budget stability ($w$) with market reality ($1 - w$):
      $$\text{Spending}_t = w \cdot [\text{Spending}_{t-1} \times (1 + \pi)] + (1 - w) \cdot [r \times AUM_{t-1}]$$
    </li>
  </ul>

  <div class="card" style="background: rgba(16, 185, 129, 0.05); border-left: 4px solid var(--accent-emerald); margin: 15px 0;">
    <h4 style="margin: 0 0 10px 0; color: var(--accent-emerald);">Worked Numerical Example: Hybrid (Tobin) Endowment Spending Calculation</h4>
    <p><strong>Scenario</strong>: A university endowment has prior-year spending of 4.20M USD, annual inflation $\pi = 2.50\%$, trailing market value $AUM_{t-1} = 100.00\text{M USD}$, target spending rate $r = 4.50\%$, and smoothing weight $w = 0.70$.</p>
    $$\text{Spending}_t = 0.70 \times [4.20\text{M} \times 1.025] + 0.30 \times [0.045 \times 100.00\text{M}] = 0.70(4.305\text{M}) + 0.30(4.500\text{M}) = 3.0135\text{M} + 1.3500\text{M} = 4.3635\text{M USD}$$
  </div>
</section>

<!-- ========================================================================================= -->
<!-- MODULE 2: RETURN & RISK MECHANICS -->
<!-- ========================================================================================= -->
<section id="pm-m2-returns" class="notes-chapter">
  <h2 class="section-heading"><span class="num">02.</span> Return &amp; Risk Mechanics</h2>
  <p>Accurate performance measurement requires distinguishing between single-period holding gains, compound multi-period growth, and cash-flow-weighted returns.</p>

  <h3 class="subheading">Holding Period Return (HPR), Arithmetic &amp; Geometric Returns</h3>
  <div class="formula-card">
    <div class="formula-title">Fundamental Return Formulations</div>
    $$HPR = \frac{P_t - P_{t-1} + D_t}{P_{t-1}} = \frac{P_t + D_t}{P_{t-1}} - 1$$
    $$R_A = \frac{1}{T} \sum_{t=1}^T R_t, \qquad R_G = \left[ \prod_{t=1}^T (1 + R_t) \right]^{1/T} - 1$$
    $$R_G \approx R_A - \frac{1}{2} \sigma^2$$
    $$\text{Where: } R_A = \text{Arithmetic mean return}, \quad R_G = \text{Geometric compound return}, \quad \sigma^2 = \text{Variance of returns}$$
  </div>
  <p>The geometric mean represents the true compound growth rate of capital per period. It is always less than or equal to the arithmetic mean ($R_G \le R_A$), with the gap widening as return volatility ($\sigma^2$) increases.</p>

  <h3 class="subheading">Money-Weighted Return (MWR) vs Time-Weighted Return (TWR)</h3>
  <ul>
    <li><strong>Time-Weighted Return (TWR)</strong>: Measures the compound growth rate of an initial investment over multiple subperiods. By calculating returns across each subperiod separated by external cash flows, TWR isolates investment performance from the timing and magnitude of external deposits and withdrawals. <em>Mandated by GIPS for evaluating investment managers who do not control cash flows</em>.</li>
    <li><strong>Money-Weighted Return (MWR)</strong>: The internal rate of return (IRR) that equates the present value of all cash inflows to the present value of all cash outflows. MWR is heavily influenced by the timing and size of external cash injections and withdrawals. If capital is added prior to strong performance, MWR exceeds TWR; if capital is added prior to poor performance, MWR lags TWR.</li>
  </ul>

  <div class="card" style="background: rgba(16, 185, 129, 0.05); border-left: 4px solid var(--accent-emerald); margin: 15px 0;">
    <h4 style="margin: 0 0 10px 0; color: var(--accent-emerald);">Worked Numerical Example: MWR vs TWR with Cash Flow Timing</h4>
    <p><strong>Scenario</strong>: An investor opens a portfolio account with an initial outlay of 100,000 USD at $t=0$.</p>
    <ul>
      <li>At $t=1$, the portfolio value prior to any new cash flows rises to 120,000 USD. The client immediately deposits an additional 50,000 USD into the account, bringing the total portfolio value to 170,000 USD.</li>
      <li>At $t=2$, the portfolio value falls by 20.0% to 136,000 USD.</li>
    </ul>
    <p><strong>Step 1: Compute Subperiod Returns for TWR</strong></p>
    $$R_1 = \frac{120,000 - 100,000}{100,000} = +20.00\%$$
    $$R_2 = \frac{136,000 - 170,000}{170,000} = -20.00\%$$
    $$\text{Annualized TWR} = \sqrt{(1 + R_1)(1 + R_2)} - 1 = \sqrt{(1 + 0.20)(1 - 0.20)} - 1 = \sqrt{0.96} - 1 = 0.9798 - 1 = -2.02\%$$

    <p><strong>Step 2: Compute MWR (IRR)</strong></p>
    <p>Set the present value of cash inflows equal to cash outflows:</p>
    $$\text{Cash Outflows: } t=0: -100,000\text{ USD}; \quad t=1: -50,000\text{ USD}$$
    $$\text{Terminal Value: } t=2: +136,000\text{ USD}$$
    $$-100,000 - \frac{50,000}{1 + r} + \frac{136,000}{(1 + r)^2} = 0$$
    $$100(1+r)^2 + 50(1+r) - 136 = 0$$
    $$\text{Let } x = 1+r: \quad 100x^2 + 50x - 136 = 0$$
    $$x = \frac{-50 + \sqrt{50^2 - 4(100)(-136)}}{200} = \frac{-50 + \sqrt{2,500 + 54,400}}{200} = \frac{-50 + \sqrt{56,900}}{200} = \frac{-50 + 238.537}{200} = 0.9427$$
    $$r = 0.9427 - 1 = -5.73\%$$

    <p><strong>Conclusion &amp; Performance Audit</strong>: $\text{MWR } (-5.73\%) < \text{TWR } (-2.02\%)$. The investor experienced a worse money-weighted outcome because substantial capital (50,000 USD) was injected immediately before the portfolio suffered a 20.0% downturn, destroying wealth on an enlarged capital base. Evaluating the manager using MWR would unfairly penalize them for client cash-flow timing.</p>
  </div>

  <h3 class="subheading">Two-Asset Portfolio Variance and Covariance Mechanics</h3>
  <div class="formula-card">
    <div class="formula-title">Portfolio Expected Return and Risk Formulation</div>
    $$E(R_p) = w_1 E(R_1) + w_2 E(R_2)$$
    $$\sigma_p^2 = w_1^2 \sigma_1^2 + w_2^2 \sigma_2^2 + 2 w_1 w_2 \text{Cov}(R_1, R_2) = w_1^2 \sigma_1^2 + w_2^2 \sigma_2^2 + 2 w_1 w_2 \rho_{1,2} \sigma_1 \sigma_2$$
    $$\sigma_p = \sqrt{w_1^2 \sigma_1^2 + w_2^2 \sigma_2^2 + 2 w_1 w_2 \rho_{1,2} \sigma_1 \sigma_2}$$
    $$w_1^{\text{min}} = \frac{\sigma_2^2 - \text{Cov}(R_1, R_2)}{\sigma_1^2 + \sigma_2^2 - 2\text{Cov}(R_1, R_2)} \quad (\text{Global Minimum Variance Portfolio Weight})$$
  </div>

  <div class="card" style="background: rgba(59, 130, 246, 0.05); border-left: 4px solid var(--accent-blue); margin: 15px 0;">
    <h4 style="margin: 0 0 10px 0; color: var(--accent-blue);">Worked Numerical Example: Two-Asset Risk Diversification Benefit</h4>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li>Asset 1 (Equities): $w_1 = 0.60$, $E(R_1) = 10.0\%$, $\sigma_1 = 18.0\%$</li>
      <li>Asset 2 (Fixed Income): $w_2 = 0.40$, $E(R_2) = 4.5\%$, $\sigma_2 = 7.0\%$</li>
      <li>Correlation: $\rho_{1,2} = 0.15$</li>
    </ul>
    <p><strong>Step 1: Expected Return Calculation</strong></p>
    $$E(R_p) = (0.60)(10.0\%) + (0.40)(4.5\%) = 6.00\% + 1.80\% = 7.80\%$$

    <p><strong>Step 2: Covariance Calculation</strong></p>
    $$\text{Cov}(R_1, R_2) = \rho_{1,2} \sigma_1 \sigma_2 = 0.15 \times 0.18 \times 0.07 = 0.001890$$

    <p><strong>Step 3: Variance Component Summation</strong></p>
    $$w_1^2 \sigma_1^2 = (0.60)^2 \times (0.18)^2 = 0.36 \times 0.0324 = 0.011664$$
    $$w_2^2 \sigma_2^2 = (0.40)^2 \times (0.07)^2 = 0.16 \times 0.0049 = 0.000784$$
    $$2 w_1 w_2 \text{Cov}(R_1, R_2) = 2 \times (0.60) \times (0.40) \times 0.001890 = 0.0009072$$
    $$\sigma_p^2 = 0.011664 + 0.000784 + 0.0009072 = 0.0133552$$
    $$\sigma_p = \sqrt{0.0133552} = 11.56\%$$

    <p><strong>Diversification Analysis</strong>: The weighted-average standard deviation is $0.60(18.0\%) + 0.40(7.0\%) = 10.80\% + 2.80\% = 13.60\%$. Because $\rho_{1,2} = 0.15 < 1.0$, the actual portfolio risk is $\sigma_p = 11.56\%$. Diversification eliminates $13.60\% - 11.56\% = 2.04\%$ percentage points of annual volatility with zero reduction in expected return.</p>
  </div>

  <h3 class="subheading">Three-Asset Portfolio Variance Expansion</h3>
  <div class="formula-card">
    <div class="formula-title">N-Asset Variance Covariance Matrix Form</div>
    $$\sigma_p^2 = w_1^2\sigma_1^2 + w_2^2\sigma_2^2 + w_3^2\sigma_3^2 + 2w_1w_2\rho_{1,2}\sigma_1\sigma_2 + 2w_1w_3\rho_{1,3}\sigma_1\sigma_3 + 2w_2w_3\rho_{2,3}\sigma_2\sigma_3$$
  </div>

  <div class="card" style="background: rgba(147, 51, 234, 0.05); border-left: 4px solid var(--accent-purple); margin: 15px 0;">
    <h4 style="margin: 0 0 10px 0; color: var(--accent-purple);">Worked Numerical Example: Three-Asset Portfolio Risk</h4>
    <p><strong>Scenario</strong>: Weights $w_1 = 50\%$ ($\sigma_1 = 18\%$), $w_2 = 30\%$ ($\sigma_2 = 10\%$), $w_3 = 20\%$ ($\sigma_3 = 6\%$). Correlations: $\rho_{1,2} = 0.25$, $\rho_{1,3} = -0.10$, $\rho_{2,3} = 0.40$.</p>
    $$\sigma_p^2 = (0.5^2)(0.18^2) + (0.3^2)(0.10^2) + (0.2^2)(0.06^2) + 2(0.5)(0.3)(0.25)(0.18)(0.10) + 2(0.5)(0.2)(-0.10)(0.18)(0.06) + 2(0.3)(0.2)(0.40)(0.10)(0.06)$$
    $$\sigma_p^2 = 0.008100 + 0.000900 + 0.000144 + 0.001350 - 0.000216 + 0.000288 = 0.010566 \implies \sigma_p = \sqrt{0.010566} = 10.28\%$$
  </div>
</section>

<!-- ========================================================================================= -->
<!-- MODULE 3: MODERN PORTFOLIO THEORY & ASSET PRICING -->
<!-- ========================================================================================= -->
<section id="pm-m3-mpt" class="notes-chapter">
  <h2 class="section-heading"><span class="num">03.</span> Modern Portfolio Theory &amp; Asset Pricing</h2>
  <p>Markowitz Modern Portfolio Theory formalizes the mathematical trade-off between risk and expected return, establishing the foundational transition from individual asset characteristics to portfolio equilibrium pricing.</p>

  <h3 class="subheading">Investor Utility &amp; Indifference Curves</h3>
  <div class="formula-card">
    <div class="formula-title">Mean-Variance Utility Function</div>
    $$U = E(R) - \frac{1}{2} A \sigma^2$$
    $$\text{Where: } U = \text{Expected utility score}, \quad A = \text{Risk-aversion coefficient}, \quad \sigma^2 = \text{Variance of portfolio returns}$$
  </div>
  <ul>
    <li>$A > 0$: <strong>Risk-Averse</strong> (requires higher expected return to accept incremental variance; indifference curves slope upward).</li>
    <li>$A = 0$: <strong>Risk-Neutral</strong> (evaluates portfolios purely on expected return, ignoring variance).</li>
    <li>$A < 0$: <strong>Risk-Seeking</strong> (willing to sacrifice expected return for higher variance; indifference curves slope downward).</li>
  </ul>

  <div class="card" style="background: rgba(147, 51, 234, 0.05); border-left: 4px solid var(--accent-purple); margin: 15px 0;">
    <h4 style="margin: 0 0 10px 0; color: var(--accent-purple);">Worked Numerical Example: Utility Ranks Across Differing Risk-Aversion Coefficients</h4>
    <p>Consider two investment portfolios:</p>
    <ul>
      <li><strong>Portfolio 1 (Aggressive Equity)</strong>: $E(R_1) = 11.0\% = 0.11$, $\sigma_1 = 16.0\% = 0.16$ (Variance $\sigma_1^2 = 0.0256$)</li>
      <li><strong>Portfolio 2 (Conservative Balanced)</strong>: $E(R_2) = 8.0\% = 0.08$, $\sigma_2 = 8.0\% = 0.08$ (Variance $\sigma_2^2 = 0.0064$)</li>
    </ul>
    <p><strong>Evaluation for Investor X (High Risk Aversion, $A = 4$)</strong>:</p>
    $$U_1(A=4) = 0.11 - 0.5(4)(0.0256) = 0.11 - 0.0512 = 0.0588 \quad (5.88\%)$$
    $$U_2(A=4) = 0.08 - 0.5(4)(0.0064) = 0.08 - 0.0128 = 0.0672 \quad (6.72\%)$$
    <p><em>Decision</em>: Investor X strictly prefers <strong>Portfolio 2</strong> ($U_2 > U_1$).</p>
    <p><strong>Evaluation for Investor Y (Moderate Risk Aversion, $A = 2$)</strong>:</p>
    $$U_1(A=2) = 0.11 - 0.5(2)(0.0256) = 0.11 - 0.0256 = 0.0844 \quad (8.44\%)$$
    $$U_2(A=2) = 0.08 - 0.5(2)(0.0064) = 0.08 - 0.0064 = 0.0736 \quad (7.36\%)$$
    <p><em>Decision</em>: Investor Y strictly prefers <strong>Portfolio 1</strong> ($U_1 > U_2$).</p>
  </div>

  <h3 class="subheading">CAL, CML, CAPM &amp; The Security Market Line (SML)</h3>
  <div class="table-wrap">
    <table>
      <thead>
        <tr>
          <th>Concept</th>
          <th>Mathematical Formulation</th>
          <th>Risk Metric (X-Axis)</th>
          <th>Applicable Assets</th>
          <th>Slope Interpretation</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Capital Allocation Line (CAL)</strong></td>
          <td>$$E(R_c) = R_f + \left( \frac{E(R_i) - R_f}{\sigma_i} \right) \sigma_c$$</td>
          <td>Total Risk ($\sigma$)</td>
          <td>Combinations of $R_f$ and any specific risky portfolio $i$</td>
          <td>Sharpe Ratio of risky portfolio $i$</td>
        </tr>
        <tr>
          <td><strong>Capital Market Line (CML)</strong></td>
          <td>$$E(R_p) = R_f + \left( \frac{E(R_m) - R_f}{\sigma_m} \right) \sigma_p$$</td>
          <td>Total Risk ($\sigma$)</td>
          <td>Only completely efficient portfolios lying on the tangent line</td>
          <td>Sharpe Ratio of the Market Portfolio (Market Price of Risk)</td>
        </tr>
        <tr>
          <td><strong>Security Market Line (SML / CAPM)</strong></td>
          <td>$$E(R_i) = R_f + \beta_i \left[ E(R_m) - R_f \right]$$</td>
          <td>Systematic Risk ($\beta$)</td>
          <td>ALL individual assets, inefficient portfolios, and efficient portfolios</td>
          <td>Market Equity Risk Premium ($E(R_m) - R_f$)</td>
        </tr>
      </tbody>
    </table>
  </div>

  <h3 class="subheading">Beta Formulation &amp; Systematic vs Unsystematic Decomposition</h3>
  <div class="formula-card">
    <div class="formula-title">Systematic Risk &amp; Variance Decomposition</div>
    $$\beta_i = \frac{\text{Cov}(R_i, R_m)}{\sigma_m^2} = \frac{\rho_{i,m} \sigma_i \sigma_m}{\sigma_m^2} = \rho_{i,m} \frac{\sigma_i}{\sigma_m}$$
    $$\sigma_i^2 = \underbrace{\beta_i^2 \sigma_m^2}_{\text{Systematic (Market) Risk}} + \underbrace{\sigma_{\epsilon,i}^2}_{\text{Unsystematic (Idiosyncratic) Risk}}$$
  </div>

  <h3 class="subheading">Performance Metrics &amp; Roy's Safety-First Criterion</h3>
  <div class="formula-card">
    <div class="formula-title">Master Performance Ratio Compendium</div>
    $$\text{Sharpe Ratio: } SR_p = \frac{R_p - R_f}{\sigma_p}, \qquad \text{Treynor Ratio: } TR_p = \frac{R_p - R_f}{\beta_p}$$
    $$\text{Jensen's Alpha: } \alpha_p = R_p - \left[ R_f + \beta_p (R_m - R_f) \right]$$
    $$M^2 (\text{Modigliani-Modigliani}): M^2 = (SR_p - SR_m) \sigma_m = R_f + SR_p \sigma_m - R_m$$
    $$\text{Roy's Safety-First Ratio: } \text{SFRatio} = \frac{E(R_p) - R_L}{\sigma_p}, \quad P(R_p < R_L) \le N(-\text{SFRatio})$$
  </div>

  <div class="card" style="background: rgba(245, 158, 11, 0.05); border-left: 4px solid var(--accent-amber); margin: 15px 0;">
    <h4 style="margin: 0 0 10px 0; color: var(--accent-amber);">Worked Numerical Example: Comprehensive Multi-Metric Portfolio Evaluation</h4>
    <p><strong>Baseline Environment</strong>: Risk-free rate $R_f = 3.00\%$, Market expected return $E(R_m) = 9.00\%$, Market risk $\sigma_m = 15.00\%$, Shortfall disaster threshold $R_L = 2.00\%$. Market Sharpe Ratio $SR_m = \frac{9.0 - 3.0}{15.0} = 0.4000$.</p>
    <div class="table-wrap">
      <table>
        <thead>
          <tr>
            <th>Portfolio</th>
            <th>$E(R_p)$</th>
            <th>$\sigma_p$</th>
            <th>$\beta_p$</th>
            <th>Sharpe ($SR$)</th>
            <th>Treynor ($TR$)</th>
            <th>Jensen $\alpha$</th>
            <th>$M^2$</th>
            <th>SFRatio ($R_L=2\%$)</th>
            <th>Shortfall $P(R < 2\%)$</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Portfolio A</strong></td>
            <td>11.50%</td>
            <td>18.00%</td>
            <td>1.25</td>
            <td>0.4722</td>
            <td>6.80%</td>
            <td>+1.00%</td>
            <td>+1.08%</td>
            <td>0.5278</td>
            <td>29.88%</td>
          </tr>
          <tr>
            <td><strong>Portfolio B</strong></td>
            <td>9.50%</td>
            <td>12.00%</td>
            <td>0.90</td>
            <td>0.5417</td>
            <td>7.22%</td>
            <td>+1.10%</td>
            <td>+2.13%</td>
            <td>0.6250</td>
            <td>26.60%</td>
          </tr>
          <tr>
            <td><strong>Portfolio C</strong></td>
            <td>8.00%</td>
            <td>9.00%</td>
            <td>0.70</td>
            <td>0.5556</td>
            <td>7.14%</td>
            <td>+0.80%</td>
            <td>+2.33%</td>
            <td>0.6667</td>
            <td>25.25%</td>
          </tr>
        </tbody>
      </table>
    </div>
    <p><strong>Analytical Observations</strong>:</p>
    <ul>
      <li><strong>Total Risk View (Sharpe &amp; $M^2$)</strong>: <em>Portfolio C ranks #1</em> ($SR = 0.5556, M^2 = +2.33\%$), providing superior excess return per unit of total risk.</li>
      <li><strong>Systematic Risk View (Treynor &amp; Jensen's Alpha)</strong>: <em>Portfolio B ranks #1</em> ($TR = 7.22\%, \alpha = +1.10\%$), delivering highest abnormal return per unit of undiversifiable market risk.</li>
      <li><strong>Capital Preservation (Roy's Safety-First)</strong>: <em>Portfolio C ranks #1</em> with $\text{SFRatio} = 0.6667$, minimizing probability of falling below the 2.0% threshold to $N(-0.6667) \approx 25.25\%$.</li>
    </ul>
  </div>
</section>

<!-- ========================================================================================= -->
<!-- MODULE 4: PORTFOLIO PLANNING, IPS & STRATEGIC ASSET ALLOCATION -->
<!-- ========================================================================================= -->
<section id="pm-m4-planning" class="notes-chapter">
  <h2 class="section-heading"><span class="num">04.</span> Portfolio Planning, IPS &amp; Strategic Asset Allocation</h2>
  <p>The Investment Policy Statement (IPS) acts as the operational constitution governing the client-advisor fiduciary relationship, converting qualitative needs into an executable Strategic Asset Allocation (SAA).</p>

  <h3 class="subheading">The RRTTLLU Framework</h3>
  <div class="table-wrap">
    <table>
      <thead>
        <tr>
          <th>IPS Dimension</th>
          <th>Key Tenets &amp; Execution Principles</th>
          <th>Analytical Pitfalls &amp; Rules</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Risk Objective (R)</strong></td>
          <td>Separated into <em>Willingness</em> (psychological/behavioral tolerance) and <em>Ability</em> (financial capacity based on wealth relative to liabilities, horizon, income stability).</td>
          <td>When willingness and ability conflict, <strong>Ability to take risk ALWAYS dominates</strong>. An advisor must never expose a portfolio to risk exceeding financial capacity.</td>
        </tr>
        <tr>
          <td><strong>Return Objective (R)</strong></td>
          <td>Distinguishes <em>Desired Return</em> (aspirational) from <em>Required Return</em> (mathematically derived to fund mandatory liabilities, spending rates, inflation, and fees).</td>
          <td>For institutions: $r_{\text{req}} = \text{Spending Rate} + \text{Inflation} + \text{Investment Expenses}$. Must be evaluated on real vs nominal terms.</td>
        </tr>
        <tr>
          <td><strong>Time Horizon (T)</strong></td>
          <td>Identifies whether horizon is single-stage or multi-stage (divided by major liquidity events, e.g., retirement, business sale, college tuition funding).</td>
          <td>A longer time horizon directly expands risk capacity, enabling greater allocations to illiquid asset classes and equities.</td>
        </tr>
        <tr>
          <td><strong>Tax Considerations (T)</strong></td>
          <td>Analyzes taxable, tax-deferred, and tax-exempt accounts. Dictates <em>Asset Location</em>: high ordinary income debt in sheltered accounts; equities in taxable accounts.</td>
          <td>Capital gains realization timing, tax-loss harvesting, and dividend vs capital gain preferential rate differentials.</td>
        </tr>
        <tr>
          <td><strong>Liquidity Needs (L)</strong></td>
          <td>Immediate cash distributions, regular net cash outflows, cash reserves for unforeseen emergencies, and capital call commitments.</td>
          <td>Liquid assets must be maintained in cash equivalents to prevent forced selling of depressed assets during market drawdowns.</td>
        </tr>
        <tr>
          <td><strong>Legal &amp; Regulatory (L)</strong></td>
          <td>Fiduciary constraints, ERISA qualified plan standards, UPMIFA, prudent investor rule, statutory concentration limits, and trust declarations.</td>
          <td>Prohibitions on specific asset classes (e.g., short sales, naked derivatives, unrated private placements).</td>
        </tr>
        <tr>
          <td><strong>Unique Circumstances (U)</strong></td>
          <td>Socially Responsible Investing (SRI/ESG) screens, concentrated single-stock equity holdings, non-financial assets (art, real estate), family legacy goals.</td>
          <td>Concentrated single-stock positions demand hedging (equity collars, prepaid variable forwards) or staged tax-efficient diversification.</td>
        </tr>
      </tbody>
    </table>
  </div>

  <h3 class="subheading">Strategic Asset Allocation (SAA) vs Tactical Asset Allocation (TAA)</h3>
  <ul>
    <li><strong>Strategic Asset Allocation (SAA)</strong>: Establishes the long-term target asset mix designed to satisfy the client's risk-return profile across market cycles. Empirical research shows SAA accounts for over 85%–90% of long-term return variability.</li>
    <li><strong>Tactical Asset Allocation (TAA)</strong>: Deliberate short-term adjustments to asset class weights away from SAA targets to exploit short-term valuation anomalies or cyclical macroeconomic dynamics. TAA introduces active risk and tracking error against the policy benchmark.</li>
  </ul>

  <h3 class="subheading">Portfolio Rebalancing Principles &amp; Corridor Width Determinants</h3>
  <p>Portfolio drift alters intended risk exposures. Investors utilize <strong>Calendar Rebalancing</strong> (fixed periodic intervals) or <strong>Corridor / Percentage-of-Portfolio Rebalancing</strong> (rebalance when weight deviates outside target corridor $w_i \pm \Delta w_i$). Optimal corridor width is governed by six core variables:</p>
  <div class="table-wrap">
    <table>
      <thead>
        <tr>
          <th>Factor</th>
          <th>Impact on Corridor Width</th>
          <th>Economic Rationale</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Transaction Costs</strong></td>
          <td>Wider Corridor</td>
          <td>High trading commissions, bid-ask spreads, and market impact discourage frequent rebalancing.</td>
        </tr>
        <tr>
          <td><strong>Risk Tolerance</strong></td>
          <td>Wider Corridor</td>
          <td>Clients with higher risk tolerance are comfortable with greater allocation drift from target policy weights.</td>
        </tr>
        <tr>
          <td><strong>Asset Class Volatility</strong></td>
          <td>Narrower Corridor</td>
          <td>High-volatility assets drift rapidly into excessive risk exposures; tight corridors control downside variance.</td>
        </tr>
        <tr>
          <td><strong>Correlation with Portfolio</strong></td>
          <td>Wider Corridor</td>
          <td>Assets highly correlated with the broader portfolio do not alter overall portfolio risk substantially when they drift.</td>
        </tr>
        <tr>
          <td><strong>Asset Illiquidity</strong></td>
          <td>Wider Corridor</td>
          <td>Illiquid private assets cannot be traded frequently without incurring prohibitive liquidation penalties.</td>
        </tr>
        <tr>
          <td><strong>Tax Impact (Taxable Accounts)</strong></td>
          <td>Wider Corridor</td>
          <td>Rebalancing in taxable accounts triggers taxable capital gains; wider corridors defer tax liabilities.</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="card" style="background: rgba(59, 130, 246, 0.05); border-left: 4px solid var(--accent-blue); margin: 15px 0;">
    <h4 style="margin: 0 0 10px 0; color: var(--accent-blue);">Worked Numerical Example: Utility-Optimal Risky Asset Weight ($w^*$)</h4>
    <p><strong>Scenario</strong>: An investor with risk-aversion coefficient $A = 4.0$ allocates between a risk-free T-bill ($R_f = 3.50\%$) and an optimal risky portfolio ($E(R_p) = 9.50\%$, $\sigma_p = 16.0\%$). Determine the utility-maximizing allocation $w^*$ to the risky portfolio.</p>
    $$w^* = \frac{E(R_p) - R_f}{A \sigma_p^2} = \frac{0.095 - 0.035}{4.0 \times (0.16)^2} = \frac{0.060}{0.1024} = 58.59\% \quad (\text{and } 41.41\% \text{ in } R_f)$$
  </div>

  <h3 class="subheading">Behavioral Biases of Individuals (L1 &amp; CBOK X)</h3>
  <p>Behavioral finance contrasts rational decision-making with psychological biases. The pivotal exam rule: <strong>Cognitive errors</strong> stem from faulty reasoning or statistical mistakes and can usually be <em>corrected/mitigated</em> through advisor education; <strong>Emotional biases</strong> stem from deep-seated feelings or impulses and generally must be <em>adapted to</em>.</p>
  <div class="table-container">
    <table>
      <thead>
        <tr>
          <th>Category</th>
          <th>Key Biases</th>
          <th>Portfolio Consequence</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Cognitive: Belief Perseverance</strong></td>
          <td>Conservatism, Confirmation, Representativeness (base-rate/sample-size neglect), Illusion of Control, Hindsight</td>
          <td>Underreacting to new earnings surprises; extrapolating small sample trends; holding concentrated employer stock.</td>
        </tr>
        <tr>
          <td><strong>Cognitive: Information Processing</strong></td>
          <td>Anchoring &amp; Adjustment, Mental Accounting, Framing, Availability</td>
          <td>Fixating on purchase price; treating dividends separately from capital gains; home-country bias.</td>
        </tr>
        <tr>
          <td><strong>Emotional Biases</strong></td>
          <td>Loss Aversion (Disposition Effect), Overconfidence, Self-Control, Status Quo, Endowment, Regret Aversion</td>
          <td>Selling winners too early while riding losers; excessive turnover; holding inherited legacy positions indefinitely.</td>
        </tr>
      </tbody>
    </table>
  </div>

  <h3 class="subheading">Sustainability / ESG Integration &amp; Shorting in Portfolios (CBOK X)</h3>
  <ul>
    <li><strong>ESG Investment Spectrum</strong>: Ranges from <em>Negative / Exclusionary Screening</em> (avoiding sin/fossil stocks) and <em>Best-in-Class / Positive Screening</em> to full <em>ESG Integration</em> into valuation models, <em>Thematic Investing</em> (clean energy), and <em>Impact Investing</em> (targeting measurable social/environmental outcomes alongside return).</li>
    <li><strong>Shorting Securities in Portfolio Construction</strong>: Active extension strategies (e.g., <strong>130/30 funds</strong>: 130% long / 30% short, maintaining 100% net equity beta) relax the long-only constraint, raising Grinold's Transfer Coefficient ($TC \to 1.0$) and allowing alpha capture on overvalued stocks. Risks include unlimited upside loss, short-rebate compression, and stock-borrow recall risk.</li>
  </ul>
</section>

<!-- ========================================================================================= -->
<!-- MODULE 5: CAPITAL MARKET EXPECTATIONS & MACRO RISK PREMIA -->
<!-- ========================================================================================= -->
<section id="pm-m5-cme" class="notes-chapter">
  <h2 class="section-heading"><span class="num">05.</span> Capital Market Expectations &amp; Macro Risk Premia</h2>
  <p>Setting long-term expectations for asset class returns, volatilities, and correlations is essential for forming the efficient frontier and designing sound SAA policies.</p>

  <h3 class="subheading">The Grinold-Kroner Model</h3>
  <div class="formula-card">
    <div class="formula-title">Grinold-Kroner Equity Expected Return Model</div>
    $$E(R_e) \approx \underbrace{\frac{D_1}{P_0}}_{\text{Dividend Yield}} - \underbrace{\% \Delta S}_{\text{Net Share Repurchases}} + \underbrace{i}_{\text{Expected Inflation}} + \underbrace{g}_{\text{Real Earnings Growth}} + \underbrace{\% \Delta (P/E)}_{\text{Valuation Repricing}}$$
    $$\text{Income Return} = \frac{D_1}{P_0} - \% \Delta S, \qquad \text{Nominal Earnings Growth} = i + g, \qquad \text{Repricing} = \% \Delta (P/E)$$
  </div>

  <div class="card" style="background: rgba(16, 185, 129, 0.05); border-left: 4px solid var(--accent-emerald); margin: 15px 0;">
    <h4 style="margin: 0 0 10px 0; color: var(--accent-emerald);">Worked Numerical Example: Step-by-Step Grinold-Kroner Expected Return</h4>
    <p><strong>Input Estimates for Large-Cap Equity Index</strong>:</p>
    <ul>
      <li>Forward Dividend Yield: $\frac{D_1}{P_0} = 2.40\%$</li>
      <li>Net Share Issuance / Repurchase: $\% \Delta S = -1.10\%$ (representing an annual net repurchase of 1.10%)</li>
      <li>Long-term Expected Inflation: $i = 2.25\%$</li>
      <li>Expected Real GDP / Earnings Growth: $g = 2.75\%$</li>
      <li>Current Trailing P/E = 22.0, Expected P/E in 10 Years = 20.0</li>
    </ul>
    <p><strong>Step 1: Calculate Annualized P/E Repricing Rate</strong></p>
    $$\% \Delta (P/E) = \left( \frac{20.0}{22.0} \right)^{1/10} - 1 = (0.90909)^{0.10} - 1 = 0.9905 - 1 = -0.95\%$$
    <p><strong>Step 2: Component Aggregation</strong></p>
    $$\text{Expected Income Return} = 2.40\% - (-1.10\%) = 2.40\% + 1.10\% = 3.50\%$$
    $$\text{Expected Nominal Earnings Growth} = 2.25\% + 2.75\% = 5.00\%$$
    $$\text{Expected Repricing Return} = -0.95\%$$
    $$E(R_e) = 3.50\% + 5.00\% - 0.95\% = 7.55\%$$
  </div>

  <h3 class="subheading">The Singer-Terhaar Model</h3>
  <div class="formula-card">
    <div class="formula-title">Singer-Terhaar International Asset Pricing with Partial Integration</div>
    $$ERP_i = \phi \cdot ERP_{i,\text{integrated}} + (1 - \phi) \cdot ERP_{i,\text{segmented}} + \text{Illiquidity Premium}$$
    $$ERP_{i,\text{integrated}} = \beta_{i,G} \cdot ERP_G = \rho_{i,G} \cdot \sigma_i \cdot \left( \frac{ERP_G}{\sigma_G} \right) = \rho_{i,G} \cdot \sigma_i \cdot SR_G$$
    $$ERP_{i,\text{segmented}} = \sigma_i \cdot \left( \frac{ERP_i}{\sigma_i} \right) = \sigma_i \cdot SR_i \quad (\text{where } SR_i \approx SR_G)$$
    $$E(R_i) = R_f + ERP_i$$
  </div>

  <div class="card" style="background: rgba(59, 130, 246, 0.05); border-left: 4px solid var(--accent-blue); margin: 15px 0;">
    <h4 style="margin: 0 0 10px 0; color: var(--accent-blue);">Worked Numerical Example: Singer-Terhaar Emerging Market Equity Premium</h4>
    <p><strong>Market Inputs</strong>:</p>
    <ul>
      <li>Risk-free rate: $R_f = 3.50\%$</li>
      <li>Global Investable Market: Volatility $\sigma_G = 16.0\%$, Global Risk Premium $ERP_G = 4.80\%$ $\implies SR_G = \frac{4.80\%}{16.0\%} = 0.30$</li>
      <li>Target Emerging Market X: Volatility $\sigma_X = 24.0\%$, Correlation with Global $\rho_{X,G} = 0.55$</li>
      <li>Degree of Global Integration: $\phi = 0.70$ (70% integrated, 30% segmented)</li>
      <li>Illiquidity Premium for Market X: $0.75\%$</li>
    </ul>
    <p><strong>Step 1: Compute Fully Integrated Risk Premium</strong></p>
    $$ERP_{X,\text{integrated}} = \rho_{X,G} \times \sigma_X \times SR_G = 0.55 \times 24.0\% \times 0.30 = 3.96\%$$
    <p><strong>Step 2: Compute Fully Segmented Risk Premium</strong></p>
    $$ERP_{X,\text{segmented}} = \sigma_X \times SR_G = 24.0\% \times 0.30 = 7.20\%$$
    <p><strong>Step 3: Calculate Blended Risk Premium and Total Expected Return</strong></p>
    $$ERP_X = (0.70 \times 3.96\%) + (0.30 \times 7.20\%) + 0.75\% = 2.772\% + 2.160\% + 0.75\% = 5.682\%$$
    $$E(R_X) = R_f + ERP_X = 3.50\% + 5.682\% = 9.182\% \approx 9.18\%$$
  </div>

  <h3 class="subheading">The Taylor Rule for Central Bank Policy Rate Determination</h3>
  <div class="formula-card">
    <div class="formula-title">Taylor Rule Policy Rate Formulation</div>
    $$i^* = r_{\text{neutral}} + \pi + 0.5(\pi - \pi^*) + 0.5(y - y^*)$$
    $$\text{Where: } i^* = \text{Target central bank policy rate}, \quad r_{\text{neutral}} = \text{Neutral real policy rate}, \quad \pi = \text{Current inflation rate}$$
    $$\pi^* = \text{Central bank inflation target}, \quad y - y^* = \text{Output gap (actual vs potential real GDP in percent)}$$
  </div>
  <p><strong>Policy Implication</strong>: When actual inflation exceeds the target ($\pi > \pi^*$) or output exceeds potential ($y > y^*$), the Taylor Rule prescribes an elevated policy rate to cool aggregate demand. If current rates are below $i^*$, monetary authorities will likely hike rates, inducing yield curve flattening and compressed equity valuation multiples.</p>

  <h3 class="subheading">Economics and Investment Markets (L2): Discount Rates &amp; Bad-Times Covariance</h3>
  <p>Asset values equal expected future cash flows discounted by the stochastic <strong>Intertemporal Rate of Substitution ($m_t$)</strong>, which reflects the marginal utility of consuming 1 unit tomorrow versus today ($m_t = \beta u'(c_t)/u'(c_0)$):</p>
  <div class="formula-card">
    <div class="formula-title">Macro Asset Pricing Decomposition</div>
    $$\text{Risk-Free Real Rate: } r_{\text{real}} \approx -\ln(\beta) + \text{Expected Real GDP Growth}$$
    $$\text{Nominal Default-Free Yield} = r_{\text{real}} + \text{Expected Inflation } (\pi) + \text{Inflation Risk Premium } (\theta)$$
    $$\text{Risky Asset Discount Rate} = r_{\text{real}} + \pi + \theta + \text{Credit / Equity Risk Premium } (\lambda)$$
  </div>
  <ul>
    <li><strong>Covariance with Bad Times</strong>: Assets whose payoffs drop during recessions ("bad times," when marginal utility of consumption $m_t$ is highest) have $\text{Cov}(P_t, m_t) < 0$ and therefore demand a positive risk premium (equities, corporate credit, commercial real estate). Default-free inflation-linked bonds exhibit near-zero or positive covariance and command lower yields.</li>
    <li><strong>Business Cycle Behavior</strong>: Corporate credit spreads widen sharply in contractions (flight to quality) and compress during expansions; break-even inflation ($BEI = \text{Nominal Yield} - \text{TIPS Yield} = \pi + \theta$) falls when recessionary deflation risks dominate.</li>
  </ul>
</section>

<!-- ========================================================================================= -->
<!-- MODULE 6: ACTIVE PORTFOLIO MANAGEMENT & THE FUNDAMENTAL LAW -->
<!-- ========================================================================================= -->
<section id="pm-m6-active" class="notes-chapter">
  <h2 class="section-heading"><span class="num">06.</span> Analysis of Active Portfolio Management &amp; The Fundamental Law</h2>
  <p>Active portfolio management seeks to generate positive risk-adjusted excess returns over a benchmark through superior forecasting skill, breadth of independent decisions, and unconstrained implementation.</p>

  <h3 class="subheading">Active Return, Tracking Error &amp; Information Ratio</h3>
  <div class="formula-card">
    <div class="formula-title">Core Active Risk &amp; Return Metrics</div>
    $$R_A = R_P - R_B \quad (\text{Active Return})$$
    $$\sigma_A = \sqrt{\frac{1}{T-1} \sum_{t=1}^T (R_{A,t} - \bar{R}_A)^2} \quad (\text{Tracking Error / Active Risk})$$
    $$IR = \frac{\bar{R}_A}{\sigma_A} = \frac{R_P - R_B}{\sigma_A} \quad (\text{Information Ratio})$$
  </div>

  <h3 class="subheading">Grinold's Fundamental Law of Active Management</h3>
  <div class="formula-card">
    <div class="formula-title">The Fundamental Law (Unconstrained vs Constrained)</div>
    $$\text{Unconstrained: } IR = IC \times \sqrt{BR}, \qquad E(R_A) = IC \times \sqrt{BR} \times \sigma_A$$
    $$\text{Full (Constrained): } IR = TC \times IC \times \sqrt{BR}, \qquad E(R_A) = TC \times IC \times \sqrt{BR} \times \sigma_A$$
    $$\sigma_A^* = \frac{IR}{SR_B} \cdot \sigma_B = TC \cdot \frac{IC \cdot \sqrt{BR}}{SR_B} \cdot \sigma_B \quad (\text{Optimal Active Risk})$$
    $$SR_P^2 = SR_B^2 + IR^2 = SR_B^2 + (TC \times IC \times \sqrt{BR})^2 \quad (\text{Total Sharpe Expansion})$$
  </div>
  <ul>
    <li><strong>Information Coefficient ($IC$)</strong>: Ex-ante forecast skill. Correlation between forecasted and realized active returns ($IC = \text{Corr}(\hat{R}_A, R_A)$). From hit rate $p$: $IC = 2p - 1$.</li>
    <li><strong>Transfer Coefficient ($TC$)</strong>: Ability to translate unconstrained active bets into actual portfolio holdings ($TC = \text{Corr}(\Delta w_i, \Delta w_i^*)$). $TC = 1.0$ for unconstrained portfolios; $TC < 1.0$ for long-only or benchmark-constrained portfolios.</li>
    <li><strong>Breadth ($BR$)</strong>: Number of independent return forecasts executed per year.</li>
  </ul>

  <div class="card" style="background: rgba(147, 51, 234, 0.05); border-left: 4px solid var(--accent-purple); margin: 15px 0;">
    <h4 style="margin: 0 0 10px 0; color: var(--accent-purple);">Worked Numerical Example: The Fundamental Law, Optimal Active Risk &amp; Sharpe Ratio</h4>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li>Benchmark: Sharpe Ratio $SR_B = 0.50$, Standard Deviation $\sigma_B = 14.0\%$</li>
      <li>Active Manager: Universe of 100 stocks evaluated quarterly ($BR = 100 \times 4 = 400$ independent decisions per year)</li>
      <li>Skill: Information Coefficient $IC = 0.05$</li>
      <li>Implementation Constraints: Long-only mandate reduces Transfer Coefficient to $TC = 0.70$</li>
    </ul>
    <p><strong>Step 1: Calculate Achievable Information Ratio ($IR$)</strong></p>
    $$IR = TC \times IC \times \sqrt{BR} = 0.70 \times 0.05 \times \sqrt{400} = 0.70 \times 0.05 \times 20 = 0.70$$

    <p><strong>Step 2: Compute Optimal Active Risk ($\sigma_A^*$)</strong></p>
    $$\sigma_A^* = \frac{IR}{SR_B} \times \sigma_B = \frac{0.70}{0.50} \times 14.0\% = 1.40 \times 14.0\% = 19.60\%$$

    <p><strong>Step 3: Calculate Expected Active Return ($E(R_A)$)</strong></p>
    $$E(R_A) = IR \times \sigma_A^* = 0.70 \times 19.60\% = 13.72\%$$

    <p><strong>Step 4: Compute Total Maximized Portfolio Sharpe Ratio ($SR_P$)</strong></p>
    $$SR_P = \sqrt{SR_B^2 + IR^2} = \sqrt{(0.50)^2 + (0.70)^2} = \sqrt{0.25 + 0.49} = \sqrt{0.74} = 0.8602$$
  </div>

  <h3 class="subheading">Active Share vs Active Risk (Tracking Error) Matrix</h3>
  <div class="formula-card">
    <div class="formula-title">Active Share Formulation</div>
    $$AS = \frac{1}{2} \sum_{i=1}^{N} |w_{P,i} - w_{B,i}|$$
  </div>
  <div class="table-wrap">
    <table>
      <thead>
        <tr>
          <th>Category</th>
          <th>Active Share ($AS$)</th>
          <th>Active Risk ($\sigma_A$)</th>
          <th>Investment Strategy &amp; Characteristics</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Pure Indexing / Closet Indexer</strong></td>
          <td>Low ($< 60\%$)</td>
          <td>Low ($< 2.0\%$)</td>
          <td>Closely replicates benchmark weights; closet indexers charge active management fees for passive market exposure.</td>
        </tr>
        <tr>
          <td><strong>Factor Bets / Sector Rotator</strong></td>
          <td>Low ($< 60\%$)</td>
          <td>High ($> 6.0\%$)</td>
          <td>Holds majority of benchmark names but takes aggressive systematic factor bets (e.g., heavy sector overweights, duration tilts).</td>
        </tr>
        <tr>
          <td><strong>Diversified Stock Picker</strong></td>
          <td>High ($> 70\%$)</td>
          <td>Low ($< 3.5\%$)</td>
          <td>Holds large portfolio of non-benchmark stocks, but individual idiosyncratic risks diversify away at the aggregate portfolio level.</td>
        </tr>
        <tr>
          <td><strong>Concentrated Stock Picker</strong></td>
          <td>High ($> 80\%$)</td>
          <td>High ($> 7.0\%$)</td>
          <td>High-conviction, bottom-up portfolio (20–30 holdings); substantial security-specific risk and tracking error.</td>
        </tr>
      </tbody>
    </table>
  </div>

  <h3 class="subheading">Brinson-Fachler Return Attribution (Allocation, Selection &amp; Interaction)</h3>
  <p>Performance attribution decomposes active portfolio return ($R_P - R_B$) across asset classes or equity sectors relative to benchmark weights ($w_{B,i}$) and benchmark total return ($R_B$):</p>
  <div class="formula-card">
    <div class="formula-title">Brinson-Fachler Single-Period Attribution Equations</div>
    $$A_i = (w_{P,i} - w_{B,i}) \times (R_{B,i} - R_B) \quad (\text{Allocation Effect})$$
    $$S_i = w_{B,i} \times (R_{P,i} - R_{B,i}) \quad (\text{Security Selection Effect})$$
    $$I_i = (w_{P,i} - w_{B,i}) \times (R_{P,i} - R_{B,i}) \quad (\text{Interaction Effect})$$
  </div>

  <div class="card" style="background: rgba(245, 158, 11, 0.05); border-left: 4px solid var(--accent-amber); margin: 15px 0;">
    <h4 style="margin: 0 0 10px 0; color: var(--accent-amber);">Worked Numerical Example: Brinson-Fachler Sector Attribution</h4>
    <p><strong>Scenario</strong>: Technology ($w_B = 50\%, R_B = 10.0\%$ vs. $w_P = 60\%, R_P = 12.0\%$) and Healthcare ($w_B = 50\%, R_B = 6.0\%$ vs. $w_P = 40\%, R_P = 5.0\%$). Total $R_B = 0.5(10\%) + 0.5(6\%) = 8.00\%$, Total $R_P = 0.6(12\%) + 0.4(5\%) = 9.20\%$, Active Return $= +1.20\%$ (+120 bps).</p>
    <ol>
      <li><strong>Allocation Effect</strong>:
        $$A_{\text{Tech}} = (0.60 - 0.50)(10.0\% - 8.0\%) = +0.20\%, \quad A_{\text{HC}} = (0.40 - 0.50)(6.0\% - 8.0\%) = +0.20\% \implies \sum A_i = +0.40\%$$
      </li>
      <li><strong>Selection Effect</strong>:
        $$S_{\text{Tech}} = 0.50(12.0\% - 10.0\%) = +1.00\%, \quad S_{\text{HC}} = 0.50(5.0\% - 6.0\%) = -0.50\% \implies \sum S_i = +0.50\%$$
      </li>
      <li><strong>Interaction Effect</strong>:
        $$I_{\text{Tech}} = (0.60 - 0.50)(12.0\% - 10.0\%) = +0.20\%, \quad I_{\text{HC}} = (0.40 - 0.50)(5.0\% - 6.0\%) = +0.10\% \implies \sum I_i = +0.30\%$$
      </li>
      <li><strong>Total Attribution Check</strong>: $+0.40\% + 0.50\% + 0.30\% = +1.20\%$ (120 bps exact match).</li>
    </ol>
  </div>
</section>

<!-- ========================================================================================= -->
<!-- MODULE 7: MULTIFACTOR RISK MODELS & FACTOR ATTRIBUTION -->
<!-- ========================================================================================= -->
<section id="pm-m7-multifactor" class="notes-chapter">
  <h2 class="section-heading"><span class="num">07.</span> Multifactor Risk Models &amp; Factor Attribution</h2>
  <p>Multifactor models decompose asset returns and risks into common systematic factor exposures and asset-specific idiosyncratic noise.</p>

  <h3 class="subheading">Three Types of Multifactor Models</h3>
  <ul>
    <li><strong>Macroeconomic Factor Models</strong>: Factor sensitivities are estimated via time-series regression against unexpected macroeconomic surprises:
      $$R_i = E(R_i) + b_{i,1} F_1^{\text{surprise}} + b_{i,2} F_2^{\text{surprise}} + \dots + \epsilon_i$$
      Examples: Inflation surprise, GDP growth surprise, credit default spread shifts.</li>
    <li><strong>Fundamental Factor Models</strong>: Factor sensitivities are standardized firm attributes (e.g., P/E, Market Cap, Momentum), and factor returns are estimated via cross-sectional regression:
      $$R_i = a_i + b_{i,1} F_1 + b_{i,2} F_2 + \dots + \epsilon_i, \qquad b_{i,k} = \frac{X_{i,k} - \bar{X}_k}{\sigma_{X_k}}$$</li>
    <li><strong>Statistical Factor Models</strong>: Factor portfolios are extracted mathematically using Principal Component Analysis (PCA) or maximum likelihood factor analysis. Maximize explained return variance but lack direct economic interpretability.</li>
  </ul>

  <h3 class="subheading">Carhart 4-Factor &amp; Fama-French 5-Factor Models</h3>
  <div class="formula-card">
    <div class="formula-title">Empirical Factor Pricing Models</div>
    $$\text{Carhart 4-Factor: } E(R_i) - R_f = \beta_{i,MKT} (R_m - R_f) + \beta_{i,SMB} SMB + \beta_{i,HML} HML + \beta_{i,WML} WML$$
    $$\text{Fama-French 5-Factor: } E(R_i) - R_f = \beta_{i,MKT} (R_m - R_f) + \beta_{i,SMB} SMB + \beta_{i,HML} HML + \beta_{i,RMW} RMW + \beta_{i,CMA} CMA$$
    $$\text{Where: } SMB = \text{Small Minus Big}, \quad HML = \text{High Minus Low (Book-to-Market)}, \quad WML = \text{Winners Minus Losers (Momentum)}$$
    $$RMW = \text{Robust Minus Weak Profitability}, \quad CMA = \text{Conservative Minus Aggressive Investment}$$
  </div>

  <h3 class="subheading">Active Risk Decomposition: Factor Risk vs Specific Risk</h3>
  <div class="formula-card">
    <div class="formula-title">Active Variance Decomposition</div>
    $$\sigma_A^2 = \underbrace{\sum_{j=1}^K \sum_{k=1}^K \Delta \beta_j \Delta \beta_k \text{Cov}(F_j, F_k)}_{\text{Active Factor Risk (Systematic)}} + \underbrace{\sum_{i=1}^N \Delta w_i^2 \sigma_{\epsilon,i}^2}_{\text{Active Specific Risk (Idiosyncratic)}}$$
    $$\text{Where: } \Delta \beta_k = \beta_{P,k} - \beta_{B,k} \quad (\text{Active Factor Sensitivity}), \quad \Delta w_i = w_{P,i} - w_{B,i} \quad (\text{Active Asset Weight})$$
  </div>

  <div class="card" style="background: rgba(16, 185, 129, 0.05); border-left: 4px solid var(--accent-emerald); margin: 15px 0;">
    <h4 style="margin: 0 0 10px 0; color: var(--accent-emerald);">Worked Numerical Example: Factor vs Specific Active Risk Decomposition</h4>
    <p>A portfolio manager holds active exposures to two factors: Market ($\Delta \beta_1 = +0.15$) and Size ($\Delta \beta_2 = +0.25$).</p>
    <ul>
      <li>Factor Volatilities: $\sigma_{F1} = 15.0\%$, $\sigma_{F2} = 8.0\%$; Factor Correlation: $\rho_{1,2} = 0.20$</li>
      <li>Active Specific Risk (from security selection): $\sigma_{\epsilon,A} = 2.80\%$ (Specific Variance $= 2.80^2 = 7.84$)</li>
    </ul>
    <p><strong>Step 1: Compute Factor Covariance</strong></p>
    $$\text{Cov}(F_1, F_2) = \rho_{1,2} \sigma_{F1} \sigma_{F2} = 0.20 \times 15.0 \times 8.0 = 24.0$$
    <p><strong>Step 2: Compute Active Factor Variance</strong></p>
    $$\text{Var}(F_1 \text{ component}) = (\Delta \beta_1)^2 \sigma_{F1}^2 = (0.15)^2 \times (15.0)^2 = 0.0225 \times 225 = 5.0625$$
    $$\text{Var}(F_2 \text{ component}) = (\Delta \beta_2)^2 \sigma_{F2}^2 = (0.25)^2 \times (8.0)^2 = 0.0625 \times 64 = 4.0000$$
    $$\text{Covariance component} = 2 \Delta \beta_1 \Delta \beta_2 \text{Cov}(F_1, F_2) = 2 \times 0.15 \times 0.25 \times 24.0 = 1.8000$$
    $$\text{Active Factor Variance} = 5.0625 + 4.0000 + 1.8000 = 10.8625$$

    <p><strong>Step 3: Total Active Variance and Tracking Error</strong></p>
    $$\sigma_A^2 = \text{Active Factor Variance} + \text{Active Specific Variance} = 10.8625 + 7.8400 = 18.7025$$
    $$\sigma_A = \sqrt{18.7025} = 4.32\%$$
    <p><em>Attribution Breakdown</em>: Active factor risk accounts for $\frac{10.8625}{18.7025} = 58.08\%$ of total active variance, while active specific risk accounts for $\frac{7.8400}{18.7025} = 41.92\%$.</p>
  </div>

  <h3 class="subheading">Measuring &amp; Managing Market Risk: VaR, CVaR &amp; Risk Budgeting (L2)</h3>
  <ul>
    <li><strong>Value at Risk (VaR)</strong>: Minimum expected loss over a given time horizon at a specified confidence level (or probability $p$ of exceeding loss). Three estimation methods:
      <ol>
        <li><em>Parametric (Variance-Covariance)</em>: $\text{VaR}_{p} = |\mu_p - z_{p}\sigma_p| \times V_P$ (assumes normal returns; fast but underestimates fat tails &amp; non-linear option gamma).</li>
        <li><em>Historical Simulation</em>: Ranks actual past returns empirically without distributional assumptions (captures fat tails, assumes history repeats).</li>
        <li><em>Monte Carlo Simulation</em>: Generates thousands of random paths allowing non-normal distributions, fat tails, and path-dependent options.</li>
      </ol>
    </li>
    <li><strong>Extensions &amp; Risk Governance</strong>: <strong>Conditional VaR (CVaR / Expected Shortfall)</strong> measures the <em>average</em> loss given that the VaR threshold has been breached (coherent risk measure). <strong>Incremental VaR (IVaR)</strong> measures exact change in VaR from adding/removing a position; <strong>Marginal VaR (MVaR)</strong> gives the first derivative ($\partial \text{VaR}/\partial w_i$). Combine VaR with <em>Stress Testing</em>, <em>Scenario Analysis</em>, and <em>Risk Budgeting</em> (allocating capital by marginal contribution to risk).</li>
  </ul>

  <div class="card" style="background: rgba(16, 185, 129, 0.05); border-left: 4px solid var(--accent-emerald); margin: 15px 0;">
    <h4 style="margin: 0 0 10px 0; color: var(--accent-emerald);">Worked Numerical Example: Parametric 95% &amp; 99% Portfolio VaR</h4>
    <p><strong>Scenario</strong>: A 50,000,000 USD multi-asset portfolio has daily expected return $\mu_d = 0.04\%$ and daily volatility $\sigma_d = 1.25\%$. Compute 1-day 95% ($z = 1.645$) and 99% ($z = 2.326$) parametric VaR.</p>
    <ul>
      <li><strong>1-Day 95% VaR</strong>: $|0.04\% - 1.645(1.25\%)| = 2.01625\% \implies 0.0201625 \times 50,000,000 = 1,008,125\text{ USD}$ (meaning there is a 5% probability of losing <em>at least</em> 1,008,125 USD in a single day).</li>
      <li><strong>1-Day 99% VaR</strong>: $|0.04\% - 2.326(1.25\%)| = 2.8675\% \implies 0.028675 \times 50,000,000 = 1,433,750\text{ USD}$.</li>
    </ul>
  </div>
</section>

<!-- ========================================================================================= -->
<!-- MODULE 8: ETFS, ALGORITHMIC EXECUTION & IMPLEMENTATION SHORTFALL -->
<!-- ========================================================================================= -->
<section id="pm-m8-execution" class="notes-chapter">
  <h2 class="section-heading"><span class="num">08.</span> ETFs, Algorithmic Execution &amp; Implementation Shortfall</h2>
  <p>Trade execution represents the critical bridge between investment decision-making and realized portfolio returns, demanding precise cost decomposition and execution algorithm selection.</p>

  <h3 class="subheading">ETF Creation / Redemption &amp; Arbitrage Bands</h3>
  <ul>
    <li><strong>Authorized Participants (APs) &amp; In-Kind Mechanism</strong>: APs create and redeem ETF shares in large blocks (Creation Units) directly with the ETF fund sponsor using in-kind transfers of underlying security baskets. Because securities are transferred in-kind rather than sold for cash, capital gains are not realized within the fund, preserving structural tax efficiency.</li>
    <li><strong>Arbitrage Bands</strong>: When ETF market prices deviate from Net Asset Value (NAV), APs arbitrage the spread:
      <ul>
        <li>If ETF trades at a <em>premium</em>: AP buys underlying basket, delivers to sponsor for new ETF shares, sells ETF shares in open market.</li>
        <li>If ETF trades at a <em>discount</em>: AP buys undervalued ETF shares, redeems with sponsor for underlying basket, sells underlying securities in open market.</li>
      </ul>
      Arbitrage bands are bounded by AP transaction costs (bid-ask spread of underlying securities + creation/redemption fees + hedging costs).</li>
    <li><strong>Tracking Difference vs Tracking Error</strong>:
      <ul>
        <li><em>Tracking Difference ($TD$)</em>: Holding period return differential: $TD = R_{\text{ETF}} - R_{\text{Benchmark}}$. Primary drivers: expense ratio, cash drag, securities lending revenue.</li>
        <li><em>Tracking Error ($TE$)</em>: Standard deviation of excess returns over time: $TE = \text{Std}(R_{\text{ETF}} - R_{\text{Benchmark}})$.</li>
      </ul>
    </li>
  </ul>

  <h3 class="subheading">Algorithmic Trade Execution Strategies</h3>
  <div class="table-wrap">
    <table>
      <thead>
        <tr>
          <th>Algorithm Type</th>
          <th>Execution Mechanism</th>
          <th>Optimal Market Environment</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Volume-Weighted Average Price (VWAP)</strong></td>
          <td>Slices parent order over the trading day in proportion to historical intraday volume distributions.</td>
          <td>Liquid equities, trade size is small proportion of Average Daily Volume (ADV &lt; 10%), no extreme urgency.</td>
        </tr>
        <tr>
          <td><strong>Time-Weighted Average Price (TWAP)</strong></td>
          <td>Slices parent order evenly across equal time intervals throughout the trading session.</td>
          <td>Markets with erratic or non-standard volume distributions where historical volume curves are unreliable.</td>
        </tr>
        <tr>
          <td><strong>Percentage of Volume (POV)</strong></td>
          <td>Participates dynamically as a specified target percentage of continuous market volume (e.g., 15% of volume).</td>
          <td>Orders where manager wants execution rate to automatically accelerate during volume spikes and pause during lulls.</td>
        </tr>
        <tr>
          <td><strong>Implementation Shortfall (IS) Algos</strong></td>
          <td>Dynamically balances market impact costs (accelerated trading) against price slippage and timing risk (slower trading).</td>
          <td>High-urgency trades, orders with high alpha decay, or orders where market momentum threatens to move price away.</td>
        </tr>
      </tbody>
    </table>
  </div>

  <h3 class="subheading">Implementation Shortfall 4-Component Cost Decomposition</h3>
  <div class="formula-card">
    <div class="formula-title">Implementation Shortfall Mathematical Framework</div>
    $$\text{Paper Portfolio Return: } \Pi_{\text{Paper}} = S \times P_n - S \times P_d$$
    $$\text{Real Portfolio Return: } \Pi_{\text{Real}} = \sum s_j P_n - \sum s_j p_j - \text{Fees}$$
    $$\text{Total IS} = \Pi_{\text{Paper}} - \Pi_{\text{Real}} = \text{Delay Cost} + \text{Trading Cost} + \text{Opportunity Cost} + \text{Explicit Fees}$$
  </div>
  <p>For a <strong>BUY order</strong> of $S$ shares with decision price $P_d$, arrival price $P_0$, executed prices $p_j$ for $S_E = \sum s_j$ shares, cancelled unexecuted shares $S_U = S - S_E$, and cancellation price $P_{\text{cancel}}$:</p>
  <div class="table-wrap">
    <table>
      <thead>
        <tr>
          <th>Component</th>
          <th>Formula (BUY Order)</th>
          <th>Economic Representation</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>1. Delay Cost (Slippage)</strong></td>
          <td>$$(P_0 - P_d) \times S_E$$</td>
          <td>Price drift between the PM's investment decision and order arrival at the market for executed shares.</td>
        </tr>
        <tr>
          <td><strong>2. Trading Cost (Market Impact)</strong></td>
          <td>$$\sum_{j} (p_j - P_0) \times s_j$$</td>
          <td>Price movement caused by executing the trade relative to the market arrival price.</td>
        </tr>
        <tr>
          <td><strong>3. Opportunity Cost (Unexecuted)</strong></td>
          <td>$$(P_{\text{cancel}} - P_d) \times S_U$$</td>
          <td>Return foregone on unfilled shares due to adverse price movements prior to order cancellation.</td>
        </tr>
        <tr>
          <td><strong>4. Explicit Costs</strong></td>
          <td>$$\text{Broker commissions, exchange fees, taxes}$$</td>
          <td>Direct cash fees incurred during execution.</td>
        </tr>
      </tbody>
    </table>
  </div>
  <p><em>Note on Combined Execution Cost</em>: $\text{Delay Cost} + \text{Trading Cost} = \sum_{j} (p_j - P_d) \times s_j$.</p>

  <div class="card" style="background: rgba(245, 158, 11, 0.05); border-left: 4px solid var(--accent-amber); margin: 15px 0;">
    <h4 style="margin: 0 0 10px 0; color: var(--accent-amber);">Worked Numerical Example: Complete Step-by-Step Implementation Shortfall Audit</h4>
    <p><strong>Order Scenario</strong>:</p>
    <ul>
      <li>On Monday, a portfolio manager decides to purchase $S = 10,000$ shares of Stock XYZ. The decision price is $P_d = 50.00\text{ USD}$.</li>
      <li>The theoretical paper portfolio investment is $10,000 \times 50.00\text{ USD} = 500,000\text{ USD}$.</li>
      <li>The order is released to the trading desk on Tuesday morning when the market opens at an arrival price of $P_0 = 50.50\text{ USD}$.</li>
      <li><strong>Execution Day 1</strong>: 6,000 shares are executed at an average price of $p_1 = 51.20\text{ USD}$.</li>
      <li><strong>Execution Day 2</strong>: 2,000 shares are executed at an average price of $p_2 = 52.00\text{ USD}$.</li>
      <li>Total executed shares: $S_E = 6,000 + 2,000 = 8,000$ shares.</li>
      <li>At the close of Day 2, the remaining $S_U = 2,000$ shares are cancelled when the market price is $P_{\text{cancel}} = 53.00\text{ USD}$.</li>
      <li>Total explicit commissions and fees: 1,200 USD.</li>
    </ul>

    <p><strong>Step-by-Step Component Calculations</strong>:</p>
    <ol>
      <li><strong>Delay Cost (Arrival Slippage on Executed Shares)</strong>:
        $$(P_0 - P_d) \times S_E = (50.50\text{ USD} - 50.00\text{ USD}) \times 8,000 = 0.50\text{ USD} \times 8,000 = 4,000\text{ USD}$$
        $$\text{In basis points: } \frac{4,000\text{ USD}}{500,000\text{ USD}} \times 10,000 = 80.0\text{ bps}$$
      </li>
      <li><strong>Trading Cost (Market Impact on Executed Shares)</strong>:
        $$\sum (p_j - P_0) s_j = (51.20 - 50.50) \times 6,000 + (52.00 - 50.50) \times 2,000 = (0.70 \times 6,000) + (1.50 \times 2,000) = 4,200\text{ USD} + 3,000\text{ USD} = 7,200\text{ USD}$$
        $$\text{In basis points: } \frac{7,200\text{ USD}}{500,000\text{ USD}} \times 10,000 = 144.0\text{ bps}$$
        <em>(Check total execution cost: $4,000 + 7,200 = 11,200\text{ USD}$, which matches $\sum (p_j - P_d) s_j = (51.20-50)\times 6,000 + (52.00-50)\times 2,000 = 7,200 + 4,000 = 11,200\text{ USD}$ or $224.0\text{ bps}$.)</em>
      </li>
      <li><strong>Opportunity Cost (Unexecuted Shares)</strong>:
        $$(P_{\text{cancel}} - P_d) \times S_U = (53.00\text{ USD} - 50.00\text{ USD}) \times 2,000 = 3.00\text{ USD} \times 2,000 = 6,000\text{ USD}$$
        $$\text{In basis points: } \frac{6,000\text{ USD}}{500,000\text{ USD}} \times 10,000 = 120.0\text{ bps}$$
      </li>
      <li><strong>Explicit Costs</strong>:
        $$\text{Fees} = 1,200\text{ USD}$$
        $$\text{In basis points: } \frac{1,200\text{ USD}}{500,000\text{ USD}} \times 10,000 = 24.0\text{ bps}$$
      </li>
      <li><strong>Total Implementation Shortfall</strong>:
        $$\text{Total IS} = 4,000\text{ USD} + 7,200\text{ USD} + 6,000\text{ USD} + 1,200\text{ USD} = 18,400\text{ USD}$$
        $$\text{IS (bps)} = \frac{18,400\text{ USD}}{500,000\text{ USD}} \times 10,000 = 368.0\text{ bps} \quad (3.68\%)$$
      </li>
    </ol>
  </div>

  <h3 class="subheading">Backtesting &amp; Simulation Pitfalls (L2)</h3>
  <ul>
    <li><strong>Core Backtesting Biases</strong>: <em>Survivorship Bias</em> (excluding delisted/bankrupt firms inflates backtested alpha); <em>Look-Ahead Bias</em> (using financial statements before their actual public filing date); <em>Data Snooping / Overfitting</em> (p-hacking multiple rules on one dataset without out-of-sample cross-validation).</li>
    <li><strong>Simulation Methods</strong>: <em>Rolling Window</em> drops oldest observations (captures regime shifts); <em>Expanding Window</em> keeps all history (reduces estimation error). <em>Bootstrapping</em> resamples actual historical returns with replacement (preserving empirical skewness/kurtosis), whereas <em>Monte Carlo</em> samples from a parameterized theoretical distribution.</li>
  </ul>

  <h3 class="subheading">Technical Analysis, Market Microstructure &amp; Fintech (L1 &amp; CBOK X)</h3>
  <ul>
    <li><strong>Technical Analysis &amp; Market Sentiment</strong>: Assumes market prices discount all known fundamentals and trends persist. Analysts track <strong>Support/Resistance</strong> levels, reversal patterns (<em>Head &amp; Shoulders</em>, <em>Double Top/Bottom</em>), continuation patterns (<em>Triangles</em>, <em>Flags</em>), trend indicators (50/200-day <em>Moving Averages</em>, <em>MACD</em>), momentum oscillators (<em>RSI &gt; 70 overbought, &lt; 30 oversold</em>), and contrarian sentiment gauges (Put/Call ratio, VIX).</li>
    <li><strong>Fintech, Big Data, AI &amp; DLT</strong>: Structured vs. unstructured data (satellite imagery, earnings-call transcripts) analyzed via <strong>Natural Language Processing (NLP)</strong> and <strong>Machine Learning</strong> (Supervised: LASSO/Ridge/Random Forests for return prediction; Unsupervised: clustering/PCA for risk regimes). <em>Robo-advisors</em> automate IPS profiling and tax-loss harvesting; <em>Distributed Ledger Technology (DLT)</em> and smart contracts streamline trade clearing and tokenized settlement.</li>
  </ul>
</section>

<!-- ========================================================================================= -->
<!-- MODULE 10: ASSET ALLOCATION (CBOK XI) & PERFORMANCE MEASUREMENT / MANAGER SELECTION (CBOK XII) -->
<!-- ========================================================================================= -->
<section id="pm-m10-cbok1112" class="notes-chapter">
  <h2 class="section-heading"><span class="num">09B.</span> Asset Allocation (CBOK XI) &amp; Performance Appraisal / Manager Selection (CBOK XII)</h2>
  <p>Completing the official 12-section CFA CBOK framework, Asset Allocation and Performance Measurement integrate Capital Market Expectations into multi-horizon portfolio construction, Liability-Driven Investing (LDI), Manager Selection, and Attribution Appraisal.</p>

  <h3 class="subheading">Strategic Asset Allocation (SAA), Tactical Tilts (TAA) &amp; Liability-Driven Investing (LDI)</h3>
  <ul>
    <li><strong>Mean-Variance Optimization (MVO) &amp; Resampled / Reverse Optimization</strong>: Unconstrained MVO suffers from input sensitivity (small return perturbations cause extreme concentrated weights). <em>Black-Litterman</em> blends market-implied equilibrium returns with investor views; <em>Risk Parity</em> equalizes marginal contribution to total risk ($MCTR_i \times w_i$) across asset classes.</li>
    <li><strong>Strategic vs. Tactical Asset Allocation (SAA vs. TAA)</strong>: SAA establishes policy weights matching long-term IPS goals; TAA introduces disciplined short-term factor/valuation tilts inside IPS corridor bands, evaluated via Information Ratio of active risk budget.</li>
    <li><strong>Liability-Driven Investing (LDI / ALM) &amp; Goals-Based Investing (GBI)</strong>: Institutional pensions align asset duration ($D_A \cdot A = D_L \cdot L$) to immunize funded status against rate shocks (Type I cash-flow matching vs. Type II duration/convexity matching). Individual wealth divides capital into sub-portfolios ("buckets") mapped to distinct probabilities of achieving safety, lifestyle, and aspirational goals.</li>
  </ul>

  <h3 class="subheading">Performance Appraisal, Manager Selection &amp; Fee Structuring (CBOK XII)</h3>
  <div class="formula-card">
    <div class="formula-title">Appraisal Ratio, Sortino Ratio &amp; Manager Selection Decision Errors</div>
    $$\text{Appraisal Ratio} = \frac{\alpha_p}{\sigma_{\epsilon_p}}, \qquad \text{Sortino Ratio} = \frac{E(R_p) - MAR}{\text{Downside Deviation}_{MAR}}, \qquad \text{Capture Ratio} = \frac{R_{\text{mgr}}}{R_{\text{bench}}}$$
  </div>
  <ul>
    <li><strong>Type I vs. Type II Errors in Manager Selection</strong>: <em>Type I Error (False Positive)</em> = hiring/retaining an unskilled manager who loses alpha; <em>Type II Error (False Negative)</em> = firing/passing over a skilled manager during a temporary style drawdown. Style-box consistency, holdings-based attribution, and operational due diligence mitigate selection errors.</li>
    <li><strong>Symmetric vs. Asymmetric Performance Fees</strong>: <em>Fulcrum fees</em> reward outperformance and penalize underperformance symmetrically; <em>Option-like bonus fees</em> ($Base + k \cdot \max(0, R_p - R_b)$) incentivize managers to raise portfolio volatility unless paired with high-water marks and clawbacks.</li>
  </ul>

  <div class="card" style="background: rgba(16, 185, 129, 0.05); border-left: 4px solid var(--accent-emerald); margin: 15px 0;">
    <h4 style="margin: 0 0 10px 0; color: var(--accent-emerald);">Worked Numerical Example: Risk-Budgeted Active SAA/TAA &amp; Pension Dollar-Duration Immunizing</h4>
    <p><strong>Part A (Pension Surplus Duration Match)</strong>: A defined-benefit pension holds 400M USD in assets ($D_A = 8.0$) against 500M USD in projected benefit liabilities ($D_L = 11.2$). Asset BPV $= 400\text{M} \times 8.0 \times 0.0001 = 320,000\text{ USD}$; Liability BPV $= 500\text{M} \times 11.2 \times 0.0001 = 560,000\text{ USD}$. To close the $-240,000\text{ USD}$ duration gap using 30-year Treasury futures ($\text{BPV}_{\text{ct}} = 2,400\text{ USD}$ per contract), the CIO buys $N_f = 240,000 / 2,400 = +100\text{ contracts}$.</p>
    <p><strong>Part B (Upside/Downside Capture)</strong>: An active equity manager captures +12.0% when the index gains +10.0% (Upside Capture $= 120\%$) and loses -6.4% when the index falls -8.0% (Downside Capture $= 80\%$), achieving an asymmetric Capture Ratio $= 120\% / 80\% = 1.50\times$.</p>
  </div>

  <div class="exercise-toolbar" style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:10px; margin: 18px 0 10px 0; padding:10px 14px; background:var(--bg-secondary); border:1px solid var(--border-color); border-radius:6px;">
    <span style="font-weight:700; font-size:13.5px; color:var(--accent-amber);">Module 09B Chapter Exercises (Asset Allocation &amp; Perf Measurement)</span>
    <div style="display:flex; gap:8px;">
      <button type="button" class="filter-btn" onclick="toggleChapterExercises('pm-m10-cbok1112', false)">Hide All (Unsolved Mode)</button>
      <button type="button" class="filter-btn" onclick="toggleChapterExercises('pm-m10-cbok1112', true)">Reveal All (Solved Mode)</button>
    </div>
  </div>
  <div class="chapter-exercise-card card" id="pm-ex-1" style="margin: 14px 0; border-left: 3px solid var(--accent-cyan); background: var(--bg-tertiary);">
    <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:8px; margin-bottom:8px;">
      <strong style="color:var(--text-primary); font-size:14px;">Exercise 9B.1 (Solved): Appraisal Ratio &amp; Sortino Comparison</strong>
      <span class="badge-diff-easy" style="font-size:10px;">SOLVED WALKTHROUGH</span>
    </div>
    <div style="font-size:13.5px; line-height:1.65; margin-bottom:10px;">Fund Alpha delivers $\alpha = +2.40\%$ with unsystematic residual risk $\sigma_\epsilon = 3.00\%$; Fund Beta delivers $\alpha = +3.00\%$ with $\sigma_\epsilon = 5.00\%$. Which manager exhibits superior risk-adjusted stock-selection skill per unit of idiosyncratic noise?</div>
    <details class="exercise-solution-details" open style="border:1px solid var(--border-color); border-radius:6px; padding:8px 12px; background:var(--bg-secondary);">
      <summary style="cursor:pointer; font-weight:600; color:var(--accent-cyan); font-size:12.5px;">Solution &amp; Derivation</summary>
      <div style="margin-top:10px; font-size:13px; line-height:1.65;"><strong>Fund Alpha</strong>: $AR_A = 2.40\% / 3.00\% = 0.80$ vs. $AR_B = 3.00\% / 5.00\% = 0.60$. Fund Alpha generates higher alpha per unit of active idiosyncratic risk.</div>
    </details>
  </div>
  <div class="chapter-exercise-card card" id="pm-ex-2" style="margin: 14px 0; border-left: 3px solid var(--accent-cyan); background: var(--bg-tertiary);">
    <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:8px; margin-bottom:8px;">
      <strong style="color:var(--text-primary); font-size:14px;">Exercise 9B.2 (Unsolved): Type I vs. Type II Manager Selection Errors</strong>
      <span class="badge-diff-moderate" style="font-size:10px;">UNSOLVED SELF-TEST</span>
    </div>
    <div style="font-size:13.5px; line-height:1.65; margin-bottom:10px;">An institutional committee fires a deep-value equity manager solely because the manager trailed the S&amp;P 500 growth rally over 2 consecutive years, only for the manager's value style to rebound +18% above benchmark the very next year. Which selection error occurred?</div>
    <details class="exercise-solution-details" style="border:1px solid var(--border-color); border-radius:6px; padding:8px 12px; background:var(--bg-secondary);">
      <summary style="cursor:pointer; font-weight:600; color:var(--accent-cyan); font-size:12.5px;">Click to Reveal Answer &amp; Derivation</summary>
      <div style="margin-top:10px; font-size:13px; line-height:1.65;"><strong>Type II Error (False Negative — prematurely terminating a skilled manager during a cyclical style headwind)</strong>.</div>
    </details>
  </div>
</section>

<!-- ========================================================================================= -->
<!-- MASTER FORMULA SHEET: PORTFOLIO MANAGEMENT -->
<!-- ========================================================================================= -->
<section id="pm-formulas" class="notes-chapter">
  <h2 class="section-heading"><span class="num">09.</span> Portfolio Management Master Formula Sheet (L1 &amp; L2)</h2>
  <p>Consolidated, rigorous formula sheet mapping all key mathematical equations across Level 1 and Level 2 Portfolio Management syllabus.</p>

  <div class="table-wrap">
    <table>
      <thead>
        <tr>
          <th>Topic / Area</th>
          <th>Concept</th>
          <th>Exact Mathematical Formula</th>
          <th>Key Variable Definitions &amp; Exam Notes</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Return Mechanics</strong></td>
          <td>Geometric Return Approx</td>
          <td>$$R_G \approx R_A - \frac{1}{2} \sigma^2$$</td>
          <td>$R_A$: Arithmetic mean, $\sigma^2$: Variance. Volatility creates return drag.</td>
        </tr>
        <tr>
          <td><strong>Two-Asset Risk</strong></td>
          <td>Portfolio Variance</td>
          <td>$$\sigma_p^2 = w_1^2 \sigma_1^2 + w_2^2 \sigma_2^2 + 2 w_1 w_2 \rho_{1,2} \sigma_1 \sigma_2$$</td>
          <td>Diversification benefit maximizes as correlation $\rho_{1,2} \to -1$.</td>
        </tr>
        <tr>
          <td><strong>Utility Theory</strong></td>
          <td>Mean-Variance Utility</td>
          <td>$$U = E(R) - \frac{1}{2} A \sigma^2$$</td>
          <td>$A$: Risk aversion coefficient. If $A > 0$, investor is risk-averse.</td>
        </tr>
        <tr>
          <td><strong>Asset Pricing</strong></td>
          <td>Capital Market Line</td>
          <td>$$E(R_p) = R_f + \left( \frac{E(R_m) - R_f}{\sigma_m} \right) \sigma_p$$</td>
          <td>Applies strictly to efficient portfolios; slope is Market Sharpe Ratio.</td>
        </tr>
        <tr>
          <td><strong>Systematic Risk</strong></td>
          <td>Asset Beta ($\beta_i$)</td>
          <td>$$\beta_i = \frac{\text{Cov}(R_i, R_m)}{\sigma_m^2} = \rho_{i,m} \frac{\sigma_i}{\sigma_m}$$</td>
          <td>Measures sensitivity of asset returns to market returns.</td>
        </tr>
        <tr>
          <td><strong>CAPM</strong></td>
          <td>Security Market Line</td>
          <td>$$E(R_i) = R_f + \beta_i \left[ E(R_m) - R_f \right]$$</td>
          <td>Applies to all individual assets; assets above SML have $\alpha > 0$.</td>
        </tr>
        <tr>
          <td><strong>Performance</strong></td>
          <td>Sharpe Ratio</td>
          <td>$$SR_p = \frac{R_p - R_f}{\sigma_p}$$</td>
          <td>Measures excess return per unit of total risk $\sigma_p$.</td>
        </tr>
        <tr>
          <td><strong>Performance</strong></td>
          <td>Treynor Ratio</td>
          <td>$$TR_p = \frac{R_p - R_f}{\beta_p}$$</td>
          <td>Measures excess return per unit of systematic risk $\beta_p$.</td>
        </tr>
        <tr>
          <td><strong>Performance</strong></td>
          <td>Jensen's Alpha</td>
          <td>$$\alpha_p = R_p - \left[ R_f + \beta_p (R_m - R_f) \right]$$</td>
          <td>Abnormal return relative to CAPM benchmark hurdle.</td>
        </tr>
        <tr>
          <td><strong>Performance</strong></td>
          <td>Modigliani-Modigliani ($M^2$)</td>
          <td>$$M^2 = (SR_p - SR_m) \sigma_m$$</td>
          <td>Leverages portfolio to match market volatility $\sigma_m$; in percent.</td>
        </tr>
        <tr>
          <td><strong>Downside Risk</strong></td>
          <td>Roy's Safety-First</td>
          <td>$$\text{SFRatio} = \frac{E(R_p) - R_L}{\sigma_p}$$</td>
          <td>$R_L$: Shortfall disaster threshold. Highest ratio minimizes $P(R < R_L)$.</td>
        </tr>
        <tr>
          <td><strong>CME</strong></td>
          <td>Grinold-Kroner Model</td>
          <td>$$E(R_e) \approx \frac{D_1}{P_0} - \% \Delta S + i + g + \% \Delta(P/E)$$</td>
          <td>$\frac{D_1}{P_0} - \% \Delta S$: Income, $i + g$: Earnings growth, $\% \Delta(P/E)$: Repricing.</td>
        </tr>
        <tr>
          <td><strong>CME</strong></td>
          <td>Singer-Terhaar Model</td>
          <td>$$ERP_i = \phi (\rho_{i,G} \sigma_i SR_G) + (1-\phi)(\sigma_i SR_G) + \text{Prem}_{\text{illiquid}}$$</td>
          <td>$\phi$: Integration degree. Blends integrated and segmented risk premia.</td>
        </tr>
        <tr>
          <td><strong>Macro Policy</strong></td>
          <td>Taylor Rule</td>
          <td>$$i^* = r_{\text{neutral}} + \pi + 0.5(\pi - \pi^*) + 0.5(y - y^*)$$</td>
          <td>Prescribes central bank target rate based on inflation and output gap.</td>
        </tr>
        <tr>
          <td><strong>Active Management</strong></td>
          <td>Fundamental Law</td>
          <td>$$IR = TC \times IC \times \sqrt{BR}$$</td>
          <td>$TC$: Transfer coeff, $IC$: Information coeff, $BR$: Breadth.</td>
        </tr>
        <tr>
          <td><strong>Active Risk</strong></td>
          <td>Optimal Active Risk</td>
          <td>$$\sigma_A^* = \frac{IR}{SR_B} \cdot \sigma_B = TC \cdot \frac{IC \sqrt{BR}}{SR_B} \cdot \sigma_B$$</td>
          <td>Maximizes combined portfolio Sharpe ratio.</td>
        </tr>
        <tr>
          <td><strong>Active Management</strong></td>
          <td>Sharpe Ratio Expansion</td>
          <td>$$SR_P^2 = SR_B^2 + IR^2$$</td>
          <td>Pythagorean expansion of Sharpe ratio through uncorrelated active alpha.</td>
        </tr>
        <tr>
          <td><strong>Active Management</strong></td>
          <td>Active Share</td>
          <td>$$AS = \frac{1}{2} \sum_{i=1}^N |w_{P,i} - w_{B,i}|$$</td>
          <td>Measures non-overlap of weights; independent of tracking error.</td>
        </tr>
        <tr>
          <td><strong>Multifactor Risk</strong></td>
          <td>Active Variance Split</td>
          <td>$$\sigma_A^2 = \Delta \beta^T \Sigma_F \Delta \beta + \sum \Delta w_i^2 \sigma_{\epsilon,i}^2$$</td>
          <td>Decomposes active risk into active factor risk and active specific risk.</td>
        </tr>
        <tr>
          <td><strong>Trade Execution</strong></td>
          <td>Implementation Shortfall</td>
          <td>$$\text{IS} = (P_0 - P_d)S_E + \sum (p_j - P_0)s_j + (P_{\text{cancel}} - P_d)S_U + \text{Fees}$$</td>
          <td>Delay cost + Trading cost + Opportunity cost + Explicit fees.</td>
        </tr>
        <tr>
          <td><strong>Allocation</strong></td>
          <td>Optimal Risky Weight</td>
          <td>$$w^* = \frac{E(R_p) - R_f}{A\sigma_p^2}$$</td>
          <td>Utility-maximizing allocation to optimal risky portfolio.</td>
        </tr>
        <tr>
          <td><strong>Attribution</strong></td>
          <td>Brinson-Fachler</td>
          <td>$$A_i = (w_{P,i}-w_{B,i})(R_{B,i}-R_B), \quad S_i = w_{B,i}(R_{P,i}-R_{B,i})$$</td>
          <td>Decomposes active return into allocation, selection, and interaction.</td>
        </tr>
        <tr>
          <td><strong>Market Risk</strong></td>
          <td>Parametric VaR</td>
          <td>$$\text{VaR}_p = |\mu_p - z_p\sigma_p| \times V_P$$</td>
          <td>Minimum expected portfolio loss at confidence threshold.</td>
        </tr>
        <tr>
          <td><strong>Institutional</strong></td>
          <td>Tobin Spending Rule</td>
          <td>$$S_t = w \cdot S_{t-1}(1+\pi) + (1-w) \cdot r \cdot AUM_{t-1}$$</td>
          <td>Balances budget predictability with market endowment value.</td>
        </tr>
      </tbody>
    </table>
  </div>
</section>
"""

with open(PM_HTML_PATH, "w", encoding="utf-8") as f:
    f.write(pm_html)
print(f"Generated {PM_HTML_PATH} ({len(pm_html)} bytes)")
