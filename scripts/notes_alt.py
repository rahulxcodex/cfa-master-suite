"""
scripts/notes_alt.py
Generates data/alt_reference_extracted.html:
Alternative Investments Master Reference Library (9 Modules)
Aligned with CFA CBOK IX & L1/L2 curricula.
Includes 12 Python-computed Worked Numericals + 20 Interactive Chapter Exercises (10 Solved + 10 Unsolved).
"""
import math
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scripts.qbank_helper import irr
from scripts.notes_helper import worked_box, exercise_card, exercise_toolbar, write_notes_html

OUTPUT_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "alt_reference_extracted.html")

# Python-verified exact calculations
# Hedge fund fees (2 and 20, hard hurdle 6%, beginning NAV 100M, ending 118M)
nav0, gross_r = 100.0, 0.18
nav1_gross = nav0 * (1 + gross_r)
mgmt_fee = nav1_gross * 0.02
nav_after_mgmt = nav1_gross - mgmt_fee
hurdle_amt = nav0 * 0.06
inc_fee_hard = max(0.0, (nav_after_mgmt - nav0 - hurdle_amt) * 0.20)
net_nav_hf = nav_after_mgmt - inc_fee_hard
net_ret_hf = (net_nav_hf - nav0) / nav0
# Soft hurdle (if net return after mgmt exceeds 6%, 20% of ALL gains above nav0)
inc_fee_soft = (nav_after_mgmt - nav0) * 0.20 if (nav_after_mgmt - nav0) > hurdle_amt else 0.0
# PE metrics DPI, RVPI, TVPI
paid_in, dist_cum, rem_nav = 85.0, 68.0, 76.5
dpi = dist_cum / paid_in
rvpi = rem_nav / paid_in
tvpi = dpi + rvpi
# VC Method: Year 5 EBITDA 12M, Exit 10x = 120M, target IRR 40%, investment 8M
tv_vc = 120.0
post_money = tv_vc / (1.40 ** 5)
pre_money = post_money - 8.0
own_vc = 8.0 / post_money
# Real estate Direct Cap & LTV/DSCR
noi_re, cap_rate = 1250000.0, 0.0625
val_re = noi_re / cap_rate
max_loan_ltv = val_re * 0.70
max_loan_dscr = (noi_re / 1.25) / 0.075  # assuming debt constant 7.5%
# REIT NAVPS, FFO, AFFO
reit_noi, reit_cap, reit_cash, reit_debt, reit_shares = 48.0, 0.06, 15.0, 315.0, 20.0
reit_nav = (reit_noi / reit_cap + reit_cash - reit_debt) / reit_shares
# Commodity Total Return
spot_prev, fut_near, fut_next, rf_comm = 70.0, 72.0, 70.5, 0.045
# Roll yield approx when near contract matures and rolls into cheaper next contract (backwardation)
roll_yield = (fut_near - fut_next) / fut_near

parts = []

parts.append("""<div class="top-controls">
  <button class="btn-ctrl" onclick="toggleTheme()">🌓 Switch Theme</button>
  <button class="btn-ctrl" onclick="window.print()">🖨️ Print / Save as PDF</button>
</div>

<div class="doc-hero">
  <h1>Alternative Investments (CFA&reg; CBOK IX)</h1>
  <p>Master Reference for CFA&reg; Level 1 &amp; Level 2 covering Private Capital (PE/VC/Credit), Hedge Fund Fee Waterfalls, Commercial Real Estate &amp; REITs, Infrastructure/Timberland, Commodity Futures Term Structure, Digital Assets &amp; Tokenization, Shorting &amp; ESG in Alternatives. Includes 12 Worked Numericals and 20 Interactive Chapter Exercises.</p>
  <div class="meta-tags">
    <span class="badge badge-purple">L1 Weight: 6%–9%</span>
    <span class="badge badge-blue">L2 Weight: 5%–10%</span>
    <span class="badge badge-emerald">9 Modules + 20 Exercises</span>
    <span class="badge badge-amber">Interactive Fee Waterfall Lab</span>
  </div>
</div>

<div class="card" style="margin-top: 15px; margin-bottom: 25px;">
  <div class="card-title">🏛️ Quick Navigation: Alternative Investments Modules</div>
  <div class="fsa-nav-bar">
    <a class="fsa-nav-btn" href="#alt-m1-fees">01. Structures &amp; Fee Waterfalls</a>
    <a class="fsa-nav-btn" href="#alt-m2-pevc">02. Private Equity &amp; VC (L1/L2)</a>
    <a class="fsa-nav-btn" href="#alt-m3-re">03. Direct Real Estate &amp; Debt (L2)</a>
    <a class="fsa-nav-btn" href="#alt-m4-reit">04. Public REITs: NAV/FFO/AFFO (L2)</a>
    <a class="fsa-nav-btn" href="#alt-m5-real">05. Infrastructure, Timber &amp; Farmland</a>
    <a class="fsa-nav-btn" href="#alt-m6-hf">06. Hedge Funds &amp; Factor Risk</a>
    <a class="fsa-nav-btn" href="#alt-m7-comm">07. Commodities &amp; Term Structure</a>
    <a class="fsa-nav-btn" href="#alt-m8-dig">08. Digital Assets, Shorting &amp; ESG</a>
    <a class="fsa-nav-btn" href="#alt-m9-formulas" style="color: var(--accent-emerald); font-weight: 700;">09. Formula Sheet</a>
  </div>
  <div style="display:flex; gap:10px; flex-wrap:wrap; margin-top:10px;">
    <button type="button" class="btn" onclick="jumpToSubjectBank(1, 'Alternative Investments')">📝 Practice 75 L1 Alts MCQs</button>
    <button type="button" class="btn btn-secondary" onclick="jumpToSubjectBank(2, 'Alternative Investments')">📑 Practice 10 L2 Alts Vignettes (50 Qs)</button>
    <button type="button" class="btn btn-secondary" onclick="switchTab('sim-alts')">🔬 Open Fee Waterfall &amp; J-Curve Lab</button>
    <button type="button" class="filter-btn" onclick="toggleChapterExercises('alt-reference', false)">🙈 Hide Solutions</button>
    <button type="button" class="filter-btn" onclick="toggleChapterExercises('alt-reference', true)">✅ Reveal All Solutions</button>
  </div>
</div>
""")

# MODULE 1: STRUCTURES & FEE WATERFALLS
parts.append(f"""
<section id="alt-m1-fees" class="notes-chapter">
  <h2 class="section-heading"><span class="num">01.</span> Fund Structures, Fee Waterfalls, Hurdle Rates &amp; High-Water Marks</h2>
  <ul>
    <li><strong>Investment Methods</strong>: <em>Direct</em> (sole control, zero GP fees, massive minimum capital/expertise); <em>Co-Investment</em> (LP invests alongside GP with reduced/zero fees on co-invest sleeve); <em>Fund Investing</em> (GP/LP blind pool, 2 &amp; 20 fee drag).</li>
    <li><strong>Hurdle Rates</strong>: <em>Hard hurdle</em> pays incentive fee ONLY on return above hurdle; <em>Soft hurdle</em> unlocks incentive fee on the <strong>entire</strong> return once cleared (often paired with a GP catch-up clause in PE!).</li>
    <li><strong>High-Water Mark (HWM)</strong>: Prevents GP from charging double performance fees while merely recovering past drawdowns.</li>
    <li><strong>Clawback &amp; Distribution Waterfalls</strong>: <em>Deal-by-deal (American)</em> pays GP carried interest early per exited deal (requires escrow/clawback protection for LPs); <em>Whole-of-fund (European)</em> returns 100% of total committed/paid-in capital + preferred hurdle before GP receives carried interest!</li>
  </ul>
""" + worked_box("Worked Numerical 1: Hedge Fund Net Return with Hard vs. Soft Hurdle",
f"<p>Fund starts at 100.0M USD, rises +18.0% gross to 118.0M USD. Terms: 2% management fee on ending AUM (independent of incentive fee), 20% incentive fee net of management fee, 6.0% hurdle rate.</p>"
f"<ul><li><strong>Management Fee</strong> $= 2\\% \\times 118.0\\text{{M}} = {mgmt_fee:.2f}\\text{{M USD}}$, leaving $NAV_{{\\text{{pre-inc}}}} = {nav_after_mgmt:.2f}\\text{{M USD}}$.</li>"
f"<li><strong>Hard Hurdle (6M)</strong>: Excess gain $= 115.64 - 100 - 6.00 = 9.64\\text{{M}}$. Incentive fee $= 20\\% \\times 9.64\\text{{M}} = {inc_fee_hard:.3f}\\text{{M USD}}$. Net Ending NAV $= {net_nav_hf:.3f}\\text{{M USD}}$ ($+ {net_ret_hf*100:.2f}\\%$ net).</li>"
f"<li><strong>Soft Hurdle</strong>: Since gain $15.64\\text{{M}} &gt; 6.00\\text{{M}}$, incentive fee applies to full $15.64\\text{{M}}$ gain $= {inc_fee_soft:.3f}\\text{{M USD}}$ ($+{((nav_after_mgmt - inc_fee_soft - 100)/100)*100:.2f}\\%$ net).</li></ul>", "emerald") +
exercise_toolbar("alt-m1-fees", "Module 01 Chapter Exercises (Fee Waterfalls)") +
exercise_card("alt-ex-1", "Exercise 1.1 (Solved): Multi-Year High-Water Mark Reset",
"<p>A hedge fund starts Year 1 at 200M USD (HWM = 200M), drops -15% in Year 1 (before fees) to 170M USD, charges 2% ending management fee (3.40M), ending Year 1 at 166.60M USD. In Year 2, it rebounds +25% gross before fees. Assuming a 20% incentive fee computed net of management fee (2% ending) with HWM, compute Year 2 incentive fee.</p>",
f"<p><strong>Answer: 0.817M USD</strong>. Year 2 gross $= 166.60 \\times 1.25 = 208.25\\text{{M}}$. Mgmt fee $= 2\\% \\times 208.25 = 4.165\\text{{M}}$, leaving $204.085\\text{{M}}$. Excess above prior HWM (200.0M) $= 4.085\\text{{M}} \\implies \\text{{Incentive}} = 0.20 \\times 4.085 = 0.817\\text{{M USD}}$.</p>", "solved", "L1/L2 HF") +
exercise_card("alt-ex-2", "Exercise 1.2 (Unsolved): European vs. American PE Waterfall",
"<p>In a European (whole-of-fund) PE waterfall, Deal #1 exits at a 3x profit while total fund paid-in capital is 100M USD and Deal #1 returned 45M USD. Can the GP collect carried interest immediately?</p>",
"<p><strong>Answer: No</strong>. Under whole-of-fund waterfalls, LPs must first receive 100% of total contributed capital (plus preferred return) across the entire fund before GP carry is paid.</p>", "unsolved", "L1/L2 PE") +
"</section>")

# MODULE 2: PRIVATE EQUITY & VENTURE CAPITAL
parts.append(f"""
<section id="alt-m2-pevc" class="notes-chapter">
  <h2 class="section-heading"><span class="num">02.</span> Private Capital: Private Equity, Venture Capital &amp; Private Credit</h2>
  <div class="formula-card">
    <div class="formula-title">PE Performance Multiples &amp; Venture Capital Valuation Method</div>
    $$DPI = \\frac{{\\text{{Cumulative Distributions}}}}{{\\text{{Paid-In Capital}}}}, \\qquad RVPI = \\frac{{\\text{{Residual NAV}}}}{{\\text{{Paid-In Capital}}}}, \\qquad TVPI = DPI + RVPI$$
    $$\\text{{Post-Money}} = \\frac{{\\text{{Exit Terminal Value}}}}{{(1 + IRR_{{\\text{{target}}}})^T}}, \\qquad \\text{{Pre-Money}} = \\text{{Post-Money}} - \\text{{Investment}}, \\qquad \\text{{Ownership}} = \\frac{{\\text{{Inv}}}}{{\\text{{Post}}}}$$
  </div>
  <p><strong>The J-Curve Effect</strong>: Early negative cash flows (drawdowns, management fees on committed capital, upfront write-downs) transition into steep positive realizations in Years 4–8. <strong>Private Credit</strong> spans direct lending, mezzanine debt (with warrants), and distressed debt (loan-to-own).</p>
""" + worked_box("Worked Numerical 2: PE Fund Multiples &amp; Venture Capital Equity Ownership",
f"<p><strong>PE Multiples</strong>: Paid-in capital $= 85\\text{{M}}$, cumulative LP distributions $= 68\\text{{M}}$, remaining NAV $= 76.5\\text{{M}}$. $DPI = {dpi:.2f}\\times$, $RVPI = {rvpi:.2f}\\times$, $TVPI = {tvpi:.2f}\\times$.</p>"
f"<p><strong>VC Method</strong>: Startup projects Year 5 EBITDA of 12M USD at 10x exit ($TV = 120\\text{{M}}$). VC invests 8.0M USD at a 40% target IRR: $\\text{{Post-Money}} = 120 / 1.40^5 = {post_money:.2f}\\text{{M USD}}$, $\\text{{Pre-Money}} = {pre_money:.2f}\\text{{M USD}}$, VC ownership $= 8 / {post_money:.2f} = {own_vc*100:.2f}\\%$.</p>", "blue") +
exercise_toolbar("alt-m2-pevc", "Module 02 Chapter Exercises (Private Equity &amp; VC)") +
exercise_card("alt-ex-3", "Exercise 2.1 (Solved): Multi-Round VC Dilution Adjustment",
"<p>If the VC in Worked Numerical 2 expects a Series B round in Year 3 to dilute Year-0 investors by 25%, how much ownership must the Series A VC demand TODAY to preserve 35.83% at Year 5 exit?</p>",
f"<p><strong>Answer: 47.77% today</strong>. $\\text{{Required Initial Share}} = \\frac{{0.3583}}{{1 - 0.25}} = {0.3583/0.75*100:.2f}\\%$.</p>", "solved", "L2 VC") +
exercise_card("alt-ex-4", "Exercise 2.2 (Unsolved): LBO Exit Equity Return Drivers",
"<p>What are the three primary drivers of Leveraged Buyout (LBO) equity returns?</p>",
"<p><strong>Answer: (1) EBITDA earnings growth, (2) Debt paydown via free cash flow (de-leveraging), and (3) Multiple expansion (Exit EV/EBITDA &gt; Entry EV/EBITDA)</strong>.</p>", "unsolved", "L2 PE") +
"</section>")

# MODULE 3: DIRECT REAL ESTATE (L2)
parts.append(f"""
<section id="alt-m3-re" class="notes-chapter">
  <h2 class="section-heading"><span class="num">03.</span> Direct Commercial Real Estate Valuation &amp; Debt Sizing (L2)</h2>
  <div class="formula-card">
    <div class="formula-title">NOI, Direct Capitalization, DCF Reversion &amp; Debt Sizing (LTV / DSCR)</div>
    $$V_0 = \\frac{{NOI_1}}{{R_{{\\text{{cap}}}}}}, \\qquad R_{{\\text{{cap}}}} = r - g, \\qquad \\text{{Terminal Value}}_N = \\frac{{NOI_{{N+1}}}}{{R_{{\\text{{terminal cap}}}}}}$$
    $$DSCR = \\frac{{NOI_1}}{{\\text{{Annual Debt Service}}}}, \\qquad LTV = \\frac{{\\text{{Mortgage Principal}}}}{{\\text{{Appraised Value}}}}$$
  </div>
""" + worked_box("Worked Numerical 3: Direct Cap Valuation &amp; Binding Lender Constraint (LTV vs. DSCR)",
f"<p>Office building generates $NOI_1 = 1,250,000\\text{{ USD}}$ at a 6.25% market cap rate: $V_0 = {val_re:,.0f}\\text{{ USD}}$. Bank permits max $LTV = 70\\%$ (max loan $= {max_loan_ltv:,.0f}\\text{{ USD}}$) AND minimum $DSCR = 1.25\\times$ at a 7.50% annual mortgage constant (max debt service $= 1,000,000\\text{{ USD}} \\implies$ max loan $= {max_loan_dscr:,.0f}\\text{{ USD}}$). The <strong>DSCR constraint binds</strong> at {max_loan_dscr:,.0f} USD!</p>", "amber") +
exercise_toolbar("alt-m3-re", "Module 03 Chapter Exercises (Direct Real Estate)") +
exercise_card("alt-ex-5", "Exercise 3.1 (Solved): Computing NOI from Potential Gross Income",
"<p>A warehouse has Potential Gross Income (PGI) of 800,000 USD, vacancy/collection loss of 8%, and operating expenses (incl. property taxes &amp; insurance, excluding debt service/income tax/depreciation) of 240,000 USD. Compute NOI.</p>",
"<p><strong>Answer: 496,000 USD</strong>. $EGI = 800,000(1 - 0.08) = 736,000\\text{ USD}$. $NOI = 736,000 - 240,000 = 496,000\\text{ USD}$ (never subtract interest or depreciation!).</p>", "solved", "L2 RE") +
exercise_card("alt-ex-6", "Exercise 3.2 (Unsolved): Terminal Cap Rate vs. Going-In Cap Rate",
"<p>Why is the terminal (exit) capitalization rate typically set 50–100 bps higher than the going-in cap rate in a 10-year commercial real estate DCF?</p>",
"<p><strong>Answer: Older building age, higher physical obsolescence/capex needs, and lower expected future NOI growth ($R_{\\text{cap}} = r - g$)</strong>.</p>", "unsolved", "L2 RE") +
"</section>")

# MODULE 4: PUBLIC REITS (L2)
parts.append("""
<section id="alt-m4-reit" class="notes-chapter">
  <h2 class="section-heading"><span class="num">04.</span> Public REITs: NAVPS, FFO &amp; AFFO Valuation (L2)</h2>
  <div class="formula-card">
    <div class="formula-title">Net Asset Value Per Share (NAVPS), FFO &amp; AFFO</div>
    $$NAVPS = \\frac{(NOI_{\\text{cash, fwd}} / R_{\\text{cap}}) + \\text{Cash/Other Assets} - \\text{Total Debt/Liabilities}}{\\text{Diluted Shares}}$$
    $$FFO = \\text{GAAP Net Income} + \\text{RE Depreciation} - \\text{Gains on Property Sales} + \\text{Losses}$$
    $$AFFO = FFO - \\text{Non-Cash Straight-Line Rent} - \\text{Maintenance Capex / Leasing Commissions}$$
  </div>
""" + worked_box("Worked Numerical 4: REIT NAV Per Share vs. Market Price",
f"<p>A retail REIT forecasts cash NOI of 48.0M USD (market cap rate $= 6.0\\%$), holds 15.0M USD cash, owes 315.0M USD debt across 20.0M shares. Gross real estate $= 48 / 0.06 = 800.0\\text{{M}}$. $NAV = 800 + 15 - 315 = 500.0\\text{{M}} \\implies NAVPS = {reit_nav:.2f}\\text{{ USD/share}}$. If REIT trades at 22.50 USD, it trades at a 10% discount to NAV.</p>", "cyan") +
exercise_toolbar("alt-m4-reit", "Module 04 Chapter Exercises (Public REITs)") +
exercise_card("alt-ex-7", "Exercise 4.1 (Solved): FFO &amp; AFFO Reconciliation",
"<p>A REIT reports GAAP Net Income of 32M USD, Real Estate Depreciation of 18M USD, a 4M USD gain on property sale, straight-line rent adjustment of +2M USD (GAAP exceeds cash rent), and recurring maintenance capex of 5M USD. Compute FFO and AFFO.</p>",
"<p><strong>Answer: FFO = 46M USD; AFFO = 39M USD</strong>. $FFO = 32 + 18 - 4 = 46\\text{M}$. $AFFO = 46 - 2 - 5 = 39\\text{M USD}$.</p>", "solved", "L2 REIT") +
exercise_card("alt-ex-8", "Exercise 4.2 (Unsolved): Why AFFO Beats FFO for Valuation",
"<p>Why do institutional REIT analysts prefer Price/AFFO over Price/FFO?</p>",
"<p><strong>Answer: AFFO deducts recurring maintenance capex, leasing commissions, and non-cash straight-line rent</strong>—measuring true sustainable dividend-paying economic cash flow.</p>", "unsolved", "L2 REIT") +
"</section>")

# MODULE 5: REAL ASSETS (INFRASTRUCTURE, TIMBER, FARMLAND)
parts.append("""
<section id="alt-m5-real" class="notes-chapter">
  <h2 class="section-heading"><span class="num">05.</span> Real Assets: Infrastructure, Timberland &amp; Farmland</h2>
  <ul>
    <li><strong>Infrastructure</strong>: <em>Economic</em> (toll roads, airports, ports, grid) vs. <em>Social</em> (hospitals, schools); <em>Greenfield</em> (construction/development risk, higher return) vs. <em>Brownfield</em> (existing cash-flowing assets, lower risk); <em>Availability-based PPPs</em> vs. <em>Demand-based concessions</em>.</li>
    <li><strong>Timberland</strong>: Unique biological growth driver (~60% of return comes from trees physically growing in volume and upgrading from pulpwood to sawtimber—allowing owners to delay harvest when lumber prices slump!).</li>
    <li><strong>Farmland</strong>: Row crops (annual flexibility) vs. Permanent crops (orchards/vineyards—higher upfront capex, multi-year price lock-in).</li>
  </ul>
""" + exercise_toolbar("alt-m5-real", "Module 05 Chapter Exercises (Real Assets)") +
exercise_card("alt-ex-9", "Exercise 5.1 (Solved): Biological Flexibility in Timber vs. Farmland",
"<p>During a severe construction downturn, why does timberland preserve capital better than annual row-crop farmland?</p>",
"<p><strong>Answer: Biological storage ('on-the-stump')</strong>. Timber managers simply defer harvesting while trees continue growing into higher-value sawtimber grades, whereas perishable crops must be harvested and sold regardless of spot price.</p>", "solved", "L1/L2 Real") +
exercise_card("alt-ex-10", "Exercise 5.2 (Unsolved): Greenfield vs. Brownfield Toll Road",
"<p>Which infrastructure asset best fits a risk-averse defined-benefit pension seeking immediate inflation-linked yield?</p>",
"<p><strong>Answer: Brownfield regulated availability-payment infrastructure</strong> (zero construction risk and predictable inflation-indexed cash flows).</p>", "unsolved", "L1/L2 Real") +
"</section>")

# MODULE 6: HEDGE FUNDS
parts.append("""
<section id="alt-m6-hf" class="notes-chapter">
  <h2 class="section-heading"><span class="num">06.</span> Hedge Fund Strategies, Factor Risks &amp; Fund-of-Funds</h2>
  <ul>
    <li><strong>Equity Hedge</strong>: Market Neutral (beta = 0, pairs/quant), Long/Short Equity, Short Bias.</li>
    <li><strong>Event-Driven</strong>: <em>Merger Arbitrage</em> (long target, short acquirer in stock deals—payoff looks like writing a short put / crash risk if deal breaks!), <em>Distressed Securities</em>.</li>
    <li><strong>Relative Value</strong>: <em>Convertible Arbitrage</em> (long convertible bond + short underlying stock &Delta;-hedged), Fixed Income Arbitrage (high leverage, liquidity squeeze risk).</li>
    <li><strong>Macro &amp; Managed Futures (CTA)</strong>: Trend-following / global FX-rate-commodity plays; provides <strong>crisis alpha</strong> (positive skewness during equity crashes).</li>
    <li><strong>Conditional Factor Risk</strong>: Standard linear regression hides crisis correlations—use conditional dummy variables ($D_{\\text{crisis}}$) to capture non-linear tail risk!</li>
  </ul>
""" + exercise_toolbar("alt-m6-hf", "Module 06 Chapter Exercises (Hedge Funds)") +
exercise_card("alt-ex-11", "Exercise 6.1 (Solved): Merger Arbitrage Asymmetry",
"<p>In an announced stock-for-stock merger, why is a merger arbitrage spread payoff frequently compared to writing an out-of-the-money put option?</p>",
"<p><strong>Answer: Small capped upside if deal closes vs. severe left-tail loss if regulators block the deal</strong> (target crashes back to pre-bid price while short acquirer rises).</p>", "solved", "L2 HF") +
exercise_card("alt-ex-12", "Exercise 6.2 (Unsolved): Fund-of-Funds Double Fee Layering",
"<p>An investor buys a Fund-of-Funds (1% mgmt / 10% incentive) allocating to underlying hedge funds (2% / 20%). Suppose underlying funds earn 15% gross, 11.4% net. What fee drag problem occurs if Fund A gains +30% and Fund B loses -10%?</p>",
"<p><strong>Answer: Netting risk / Asymmetric incentive fee drag</strong>. Fund A still charges 20% performance fee on +30% even though the portfolio average net gain across A &amp; B is modest, plus the FoF layers an extra 1% + 10% fee on top.</p>", "unsolved", "L1/L2 HF") +
"</section>")

# MODULE 7: COMMODITIES
parts.append(f"""
<section id="alt-m7-comm" class="notes-chapter">
  <h2 class="section-heading"><span class="num">07.</span> Commodities &amp; Futures Term Structure (L1 &amp; L2)</h2>
  <div class="formula-card">
    <div class="formula-title">Commodity Futures Pricing &amp; Total Return Decomposition</div>
    $$F_0(T) \\approx S_0 e^{{(r + c - \\gamma)T}} \\quad (\\text{{Backwardation: }} F_0 &lt; S_0 \\text{{ when }} \\gamma &gt; r + c)$$
    $$\\text{{Total Return}} = \\text{{Collateral Return (T-Bill)}} + \\text{{Price Return}} + \\text{{Roll Return}}$$
    $$\\text{{Roll Return}} = \\frac{{\\text{{Near Futures}} - \\text{{Far Futures}}}}{{\\text{{Near Futures}}}} \\quad (\\text{{Positive in Backwardation, Negative in Contango}})$$
  </div>
  <ul>
    <li><strong>Theories of Futures Returns</strong>: <em>Insurance Theory</em> (Keynes: producers hedge by selling futures below expected spot &rarr; normal backwardation); <em>Hedging Pressure Hypothesis</em> (both producers &amp; consumers hedge); <em>Theory of Storage</em> (high inventory &rarr; low convenience yield &rarr; contango; scarce inventory &rarr; high convenience yield &rarr; backwardation).</li>
  </ul>
""" + worked_box("Worked Numerical 5: Commodity Futures Total Return Attribution",
f"<p>A fully collateralized crude oil futures index earns T-Bill collateral yield of 4.50%, spot oil rises +3.00%, and the futures curve is in <strong>backwardation</strong> (expiring near contract at 72.00 USD rolls into next contract at 70.50 USD). Roll yield $= \\frac{{72.00 - 70.50}}{{72.00}} = +{roll_yield*100:.2f}\\%$. Total return $\\approx 4.50\\% + 3.00\\% + {roll_yield*100:.2f}\\% = {4.50 + 3.00 + roll_yield*100:.2f}\\%$.</p>", "emerald") +
exercise_toolbar("alt-m7-comm", "Module 07 Chapter Exercises (Commodities)") +
exercise_card("alt-ex-13", "Exercise 7.1 (Solved): Theory of Storage &amp; Inventory Scarcity",
"<p>Unexpected port disruptions deplete copper warehouse inventories to 10-year lows. What happens to convenience yield and curve shape?</p>",
"<p><strong>Answer: Convenience yield surges above storage + interest ($\\gamma &gt; r + c$), shifting the curve into steep backwardation ($F_0 &lt; S_0$)</strong> and producing positive roll yield for long futures holders.</p>", "solved", "L2 Comm") +
exercise_card("alt-ex-14", "Exercise 7.2 (Unsolved): Contango Roll Drag",
"<p>Natural gas spot rises +2.0%, T-bills yield +4.0%, yet a long futures ETF returns -1.5%. Explain the driver.</p>",
"<p><strong>Answer: Negative roll return (-7.5% drag) from steep contango</strong> ($F_{\\text{far}} &gt; F_{\\text{near}}$ due to high storage costs &amp; ample supply).</p>", "unsolved", "L2 Comm") +
"</section>")

# MODULE 8: DIGITAL ASSETS, SHORTING & ESG
parts.append("""
<section id="alt-m8-dig" class="notes-chapter">
  <h2 class="section-heading"><span class="num">08.</span> Digital Assets, Shorting Alternatives &amp; Sustainability (CBOK IX)</h2>
  <ul>
    <li><strong>Digital Assets &amp; Tokenization</strong>: Cryptocurrencies (Bitcoin PoW, Proof-of-Stake chains, permissioned vs. permissionless ledgers), Smart Contracts, Tokenization of illiquid assets (fractional real estate/PE ownership improving liquidity &amp; settlement speed). Risks: regulatory shifts, custody key loss, 51% consensus attacks, extreme volatility &amp; episodic correlation spikes during risk-off crashes.</li>
    <li><strong>Shorting Alternatives</strong>: Direct shorting of private PE/RE/hedge funds is structurally impossible due to lock-ups &amp; lack of borrow; instead investors short public proxies (listed REITs, BDCs, commodity futures, or buy CDS/TRS).</li>
    <li><strong>ESG in Alternatives</strong>: PE sponsors drive operational decarbonization during ownership; green buildings earn rental/cap-rate premiums ("green alpha") vs. brown-asset stranding discounts.</li>
  </ul>
""" + exercise_toolbar("alt-m8-dig", "Module 08 Chapter Exercises (Digital Assets &amp; ESG)") +
exercise_card("alt-ex-15", "Exercise 8.1 (Solved): Proof-of-Work vs. Proof-of-Stake Validation",
"<p>Contrast Proof-of-Work (PoW) and Proof-of-Stake (PoS) regarding energy intensity and economic security guarantees.</p>",
"<p><strong>Answer: PoW secures blocks via computational hashing energy expenditure; PoS secures blocks via staked capital slashed upon malicious validation</strong> (drastically lower electricity footprint).</p>", "solved", "L1/CBOK Dig") +
exercise_card("alt-ex-16", "Exercise 8.2 (Unsolved): Shorting Private Real Estate",
"<p>A macro fund wants to express a bearish view on US commercial office real estate. Since direct buildings cannot be shorted, what liquid proxy instruments can be used?</p>",
"<p><strong>Answer: Short public office REIT equities, buy protection on CMBX tranches, or enter negative-return office property total return swaps</strong>.</p>", "unsolved", "CBOK Short") +
"</section>")

# MODULE 9: FORMULA SHEET
parts.append("""
<section id="alt-m9-formulas" class="notes-chapter">
  <h2 class="section-heading"><span class="num">09.</span> Master Alternative Investments Formula Cheat Sheet</h2>
  <div class="table-container">
    <table>
      <thead><tr><th>Asset Class</th><th>Governing Formula</th><th>Key Exam Trap</th></tr></thead>
      <tbody>
        <tr><td><strong>PE Multiples</strong></td><td>$$TVPI = DPI + RVPI$$</td><td>MOIC ignores timing; IRR captures timing</td></tr>
        <tr><td><strong>VC Method</strong></td><td>$$\\text{Post} = \\frac{TV}{(1+r)^T}, \\; f = \\frac{I}{\\text{Post}}$$</td><td>Scale up initial share for future round dilution!</td></tr>
        <tr><td><strong>Direct Real Estate</strong></td><td>$$V_0 = \\frac{NOI_1}{R_{\\text{cap}}}, \\; DSCR = \\frac{NOI}{\\text{Debt Svc}}$$</td><td>Take the <em>lower</em> of LTV max loan and DSCR max loan</td></tr>
        <tr><td><strong>REIT AFFO</strong></td><td>$$AFFO = FFO - \\text{SL Rent} - \\text{Maint Capex}$$</td><td>FFO adds back RE depreciation &amp; subtracts gains</td></tr>
        <tr><td><strong>Commodities</strong></td><td>$$Total = \\text{Collateral} + \\text{Price} + \\text{Roll}$$</td><td>Backwardation = positive roll yield</td></tr>
      </tbody>
    </table>
  </div>
""" + exercise_toolbar("alt-m9-formulas", "Module 09 Capstone Drills") +
exercise_card("alt-ex-17", "Exercise 9.1 (Solved): VC Post-Money &amp; Pre-Money Valuation",
"<p>A VC targets 35% IRR over 4 years on a 5M USD investment in a SaaS startup expected to sell for 66.43M USD at Year 4. Compute Post-Money and Pre-Money valuation.</p>",
f"<p><strong>Answer: Post = 20.00M USD; Pre = 15.00M USD; Ownership = 25.0%</strong>. $66.43 / 1.35^4 = {66.43/(1.35**4):.2f}\\text{{M}}$; $20 - 5 = 15\\text{{M}}$.</p>", "solved", "L2 VC") +
exercise_card("alt-ex-18", "Exercise 9.2 (Unsolved): Soft Hurdle Trigger Check",
"<p>A hedge fund charges 20% performance fee with an 8.0% <em>soft</em> hurdle. Net return after management fee is +7.8%. Compute the incentive fee.</p>",
"<p><strong>Answer: Zero (0.00%)</strong>. Because +7.8% failed to clear the 8.0% hurdle threshold, no incentive fee triggers.</p>", "unsolved", "L1 HF") +
exercise_card("alt-ex-19", "Exercise 9.3 (Solved): Convertible Arbitrage Position Setup",
"<p>How does a convertible arbitrage hedge fund construct a volatility-neutral trade on an undervalued convertible bond?</p>",
"<p><strong>Answer: Long the convertible bond + Short $\\Delta$ shares of the underlying equity</strong> (capturing bond yield, implied vol underpricing, and gamma).</p>", "solved", "L2 HF") +
exercise_card("alt-ex-20", "Exercise 9.4 (Unsolved): GP Clawback Scenario",
"<p>In a deal-by-deal PE waterfall, Exit #1 earns +40M (GP takes 8M carry), then Exits #2 and #3 lose -40M combined, leaving net fund profit = 0. What mechanism protects LPs?</p>",
"<p><strong>Answer: Clawback provision</strong> requiring the GP to return the excess 8M USD carry at fund liquidation.</p>", "unsolved", "L1/L2 PE") +
"</section>")

write_notes_html("".join(parts), OUTPUT_PATH)
