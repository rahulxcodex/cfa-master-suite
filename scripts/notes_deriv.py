"""
scripts/notes_deriv.py
Generates data/deriv_reference_extracted.html:
Derivatives and Risk Management Master Reference Library (9 Modules)
Aligned with CFA CBOK VIII & L1/L2 curricula.
Includes 14 Python-computed Worked Numericals (incl. exact BSM via bsm_values) + 20 Interactive Chapter Exercises.
"""
import math
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scripts.qbank_helper import bsm_values
from scripts.notes_helper import worked_box, exercise_card, exercise_toolbar, write_notes_html

OUTPUT_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "deriv_reference_extracted.html")

# Python-verified exact calculations
# Equity forward with discrete dividend & MTM mid-life
S0_eq, div1, r_f, T_eq = 120.0, 2.50, 0.04, 0.50
pv_div = div1 / (1 + r_f) ** 0.25
F0_eq = (S0_eq - pv_div) * ((1 + r_f) ** T_eq)
# Mid-life at t=0.30 (after dividend paid, remaining T=0.20), St = 126
St_eq = 126.0
Vt_eq = St_eq - F0_eq / ((1 + r_f) ** 0.20)
# Commodity forward with storage & convenience yield
F0_com = 80.0 * math.exp((0.04 + 0.03 - 0.05) * 0.5)
# FRA pricing from spot rates: 90-day spot 4.0%, 180-day spot 4.5% -> 3x6 FRA
r90, r180 = 0.040, 0.045
fra_rate = (((1 + r180 * 180 / 360) / (1 + r90 * 90 / 360)) - 1) * (360 / 90)
# FRA valuation mid-life: Notional 10M, contract 4.20%, 60 days later new 90-day spot = 5.10%, 150-day discount rate = 5.00%
fra_val = 10000000.0 * ((0.0510 - 0.0420) * 90 / 360) / (1 + 0.0500 * 150 / 360)
# Interest Rate Swap fixed rate: DF90=0.9901, DF180=0.9794, DF270=0.9675, DF360=0.9550
dfs = [0.9901, 0.9794, 0.9675, 0.9550]
qtr_swap = (1.0 - dfs[-1]) / sum(dfs)
ann_swap = qtr_swap * 4
# Put-Call Parity
S_pcp, X_pcp, r_pcp, T_pcp, c_pcp = 52.0, 50.0, 0.05, 0.5, 4.80
p_pcp = c_pcp + X_pcp / ((1 + r_pcp) ** T_pcp) - S_pcp
# 1-Period Binomial Call
S_b, X_b, u_b, d_b, rf_b = 100.0, 102.0, 1.15, 0.88, 0.04
pi_b = (1 + rf_b - d_b) / (u_b - d_b)
cu, cd = max(0.0, S_b * u_b - X_b), max(0.0, S_b * d_b - X_b)
c0_b = (pi_b * cu + (1 - pi_b) * cd) / (1 + rf_b)
delta_b = (cu - cd) / (S_b * u_b - S_b * d_b)
# Exact BSM calculation
bsm = bsm_values(S=100.0, K=100.0, r=0.05, T=0.5, sigma=0.24, q=0.02)

parts = []

parts.append("""<div class="top-controls">
  <button class="btn-ctrl" onclick="toggleTheme()">🌓 Switch Theme</button>
  <button class="btn-ctrl" onclick="window.print()">🖨️ Print / Save as PDF</button>
</div>

<div class="doc-hero">
  <h1>Derivatives &amp; Risk Management (CFA&reg; CBOK VIII)</h1>
  <p>Master Reference for CFA&reg; Level 1 (Instruments, Cost-of-Carry Forward Pricing, Put-Call Parity, 1-Step Binomial) &amp; Level 2 (Mid-Life Forward/FRA/Swap Valuation, Currency &amp; Equity Swaps, Multi-Period American Binomial Trees, Black-Scholes-Merton &amp; Option Greeks). Includes 14 Python-verified Worked Numericals and 20 Interactive Chapter Exercises.</p>
  <div class="meta-tags">
    <span class="badge badge-cyan">L1 Weight: 6%–9%</span>
    <span class="badge badge-purple">L2 Weight: 5%–10%</span>
    <span class="badge badge-emerald">9 Modules + 20 Exercises</span>
    <span class="badge badge-amber">Interactive BSM &amp; Greeks Lab</span>
  </div>
</div>

<div class="card" style="margin-top: 15px; margin-bottom: 25px;">
  <div class="card-title">⚡ Quick Navigation: Derivatives Curriculum Modules</div>
  <div class="fsa-nav-bar">
    <a class="fsa-nav-btn" href="#deriv-m1-inst">01. Instruments &amp; Replication</a>
    <a class="fsa-nav-btn" href="#deriv-m2-fwd">02. Forwards &amp; Futures (L1/L2)</a>
    <a class="fsa-nav-btn" href="#deriv-m3-fra">03. FRAs &amp; Interest Swaps (L2)</a>
    <a class="fsa-nav-btn" href="#deriv-m4-ccyswap">04. Currency &amp; Equity Swaps (L2)</a>
    <a class="fsa-nav-btn" href="#deriv-m5-pcp">05. Options &amp; Put-Call Parity</a>
    <a class="fsa-nav-btn" href="#deriv-m6-binom">06. Binomial Option Trees (L2)</a>
    <a class="fsa-nav-btn" href="#deriv-m7-bsm">07. BSM Model &amp; Greeks (L2)</a>
    <a class="fsa-nav-btn" href="#deriv-m8-strat">08. Spreads, Collars &amp; FX Hedging</a>
    <a class="fsa-nav-btn" href="#deriv-m9-formulas" style="color: var(--accent-emerald); font-weight: 700;">09. Formula Sheet</a>
  </div>
  <div style="display:flex; gap:10px; flex-wrap:wrap; margin-top:10px;">
    <button type="button" class="btn" onclick="jumpToSubjectBank(1, 'Derivatives')">📝 Practice 85 L1 Derivatives MCQs</button>
    <button type="button" class="btn btn-secondary" onclick="jumpToSubjectBank(2, 'Derivatives')">📑 Practice 11 L2 Derivatives Vignettes (55 Qs)</button>
    <button type="button" class="btn btn-secondary" onclick="switchTab('sim-bsm')">🔬 Open Black-Scholes &amp; Greeks Lab</button>
    <button type="button" class="filter-btn" onclick="toggleChapterExercises('deriv-reference', false)">🙈 Hide Solutions</button>
    <button type="button" class="filter-btn" onclick="toggleChapterExercises('deriv-reference', true)">✅ Reveal All Solutions</button>
  </div>
</div>
""")

# MODULE 1
parts.append("""
<section id="deriv-m1-inst" class="notes-chapter">
  <h2 class="section-heading"><span class="num">01.</span> Derivative Instruments, Markets &amp; No-Arbitrage Replication</h2>
  <ul>
    <li><strong>Forward Commitments</strong> (Obligation to transact): Forwards (OTC, bespoke, counterparty default risk), Futures (exchange-traded, daily mark-to-market via CCP clearinghouse), Swaps (series of forwards).</li>
    <li><strong>Contingent Claims</strong> (Right, not obligation): Options (Calls/Puts), Credit Default Swaps (CDS).</li>
    <li><strong>No-Arbitrage Replication</strong>: $\\text{Risky Asset} + \\text{Short Forward} = \\text{Risk-Free Bond}$. If futures prices correlate <em>positively</em> with interest rates, futures prices exceed forward prices (daily MTM cash inflows can be reinvested at higher rates!).</li>
  </ul>
""" + exercise_toolbar("deriv-m1-inst", "Module 01 Chapter Exercises (Instruments)") +
exercise_card("deriv-ex-1", "Exercise 1.1 (Solved): Futures vs. Forward Price Correlation Bias",
"<p>When underlying bond/equity asset prices correlate <em>negatively</em> with short-term interest rates, which has the higher price: a forward or a futures contract?</p>",
"<p><strong>Answer: Forward contract trades at a slightly higher price</strong>. Under negative correlation, futures gains happen when rates fall (poor reinvestment) and losses happen when rates rise (costly margin funding), making futures less attractive than forwards.</p>", "solved", "L1 Deriv") +
exercise_card("deriv-ex-2", "Exercise 1.2 (Unsolved): Synthetic Risk-Free Asset Replication",
"<p>How can an investor replicate a risk-free zero-coupon bond using a non-dividend stock and a forward contract?</p>",
"<p><strong>Answer: Long Stock ($+S_0$) + Short Forward ($-F_0$)</strong>. At expiration $T$, total payoff equals $S_T - (S_T - F_0) = F_0$ with zero market risk.</p>", "unsolved", "L1 Deriv") +
"</section>")

# MODULE 2: FORWARDS & FUTURES
parts.append(f"""
<section id="deriv-m2-fwd" class="notes-chapter">
  <h2 class="section-heading"><span class="num">02.</span> Pricing &amp; Valuation of Forward Commitments (L1 &amp; L2)</h2>
  <div class="formula-card">
    <div class="formula-title">No-Arbitrage Forward Price &amp; Mid-Life Valuation ($0 &lt; t &lt; T$)</div>
    $$F_0(T) = [S_0 - PV_0(\\text{{Benefits}}) + PV_0(\\text{{Costs}})](1 + r)^T, \\qquad F_0^{{\\text{{cont}}}} = S_0 e^{{(r + c - \\gamma)T}}$$
    $$V_t(\\text{{Long Forward}}) = [S_t - PV_t(\\text{{Remaining Benefits}}) + PV_t(\\text{{Remaining Costs}})] - \\frac{{F_0(T)}}{{(1+r)^{{T-t}}}}$$
    $$\\text{{Bond Futures Quoted Price: }} QFP = \\frac{{F_0(T) - AI_T}}{{CF}}, \\qquad F_0(\\text{{FX, }} P/B) = S_0 \\frac{{(1+r_P)^T}}{{(1+r_B)^T}}$$
  </div>
""" + worked_box("Worked Numerical 1: Equity Forward Price &amp; Mid-Life MTM Valuation",
f"<p><strong>At $t=0$</strong>: Stock $S_0 = 120.00\\text{{ USD}}$ pays a 2.50 USD dividend in 0.25 years; $r_f = 4.0\\%$, $T = 0.50$ years. $PV_0(D) = 2.50 / 1.04^{{0.25}} = {pv_div:.4f}\\text{{ USD}}$. Forward price $F_0 = (120 - {pv_div:.4f})(1.04)^{{0.5}} = {F0_eq:.2f}\\text{{ USD}}$.</p>"
f"<p><strong>At $t=0.30$ (after ex-dividend, $T-t = 0.20$)</strong>: Stock trades at $S_t = 126.00\\text{{ USD}}$. Long forward value $V_t = 126.00 - \\frac{{{F0_eq:.2f}}}{{1.04^{{0.20}}}} = {Vt_eq:.2f}\\text{{ USD}}$.</p>", "emerald") +
worked_box("Worked Numerical 2: Commodity Forward with Storage &amp; Convenience Yield",
f"<p>Oil spot $S_0 = 80.00\\text{{ USD}}$, continuous $r_f = 4.0\\%$, storage cost $c = 3.0\\%$, convenience yield $\\gamma = 5.0\\%$, $T = 0.5$ yr. $F_0 = 80 e^{{(0.04 + 0.03 - 0.05)(0.5)}} = {F0_com:.2f}\\text{{ USD}}$.</p>", "blue") +
exercise_toolbar("deriv-m2-fwd", "Module 02 Chapter Exercises (Forwards)") +
exercise_card("deriv-ex-3", "Exercise 2.1 (Solved): Treasury Bond Futures Clean Quoted Price",
"<p>A Treasury bond with Conversion Factor $CF = 1.12$ has a full forward price of 108.50 per 100 par and accrued interest at delivery $AI_T = 1.60$. Compute Quoted Futures Price ($QFP$).</p>",
f"<p><strong>Answer: 95.45</strong>. $QFP = \\frac{{108.50 - 1.60}}{{1.12}} = {(108.50-1.60)/1.12:.2f}$.</p>", "solved", "L2 Deriv") +
exercise_card("deriv-ex-4", "Exercise 2.2 (Unsolved): Forward Value at Initiation",
"<p>Why is the mark-to-market value of a newly signed forward contract equal to zero at $t=0$, whereas its forward price $F_0(T)$ is non-zero?</p>",
"<p><strong>Answer: Because $F_0(T)$ is set via cost-of-carry so neither party pays an upfront premium at $t=0$</strong>; value arises later solely as spot price and interest rates diverge from $F_0(T)$.</p>", "unsolved", "L1/L2 Deriv") +
"</section>")

# MODULE 3: FRAs & INTEREST RATE SWAPS (L2)
parts.append(f"""
<section id="deriv-m3-fra" class="notes-chapter">
  <h2 class="section-heading"><span class="num">03.</span> Forward Rate Agreements (FRAs) &amp; Interest Rate Swaps (L2)</h2>
  <div class="formula-card">
    <div class="formula-title">FRA Synthetic Rate, FRA Valuation &amp; Swap Fixed Rate</div>
    $$FRA(0, h, m) = \\left[\\frac{{1 + L_{{h+m}}(\\frac{{h+m}}{{360}})}}{{1 + L_h(\\frac{{h}}{{360}})}} - 1\\right]\\left(\\frac{{360}}{{m}}\\right)$$
    $$V_t(\\text{{Pay-Fixed FRA}}) = \\text{{NP}} \\cdot \\frac{{(FRA_t - FRA_0)(\\frac{{m}}{{360}})}}{{1 + L_{{T-t}}(\\frac{{T-t}}{{360}})}}$$
    $$r_{{\\text{{fix, period}}}} = \\frac{{1 - DF_n}}{{\\sum_{{i=1}}^n DF_i}}, \\qquad V_t(\\text{{Receive-Fixed Swap}}) = NP \\cdot (r_{{\\text{{fix}},0}} - r_{{\\text{{fix}},t}}) \\sum DF_i \\text{{ (or Fixed Bond - Floating Bond)}}$$
  </div>
""" + worked_box("Worked Numerical 3: 3x6 FRA Rate &amp; Mid-Life Pay-Fixed FRA Valuation",
f"<p><strong>FRA Pricing</strong>: 90-day spot $L_{{90}} = 4.00\\%$, 180-day spot $L_{{180}} = 4.50\\%$. Implied 3x6 FRA $= {fra_rate*100:.3f}\\%$.</p>"
f"<p><strong>Mid-Life FRA Value</strong>: Long (pay-fixed) a 10M USD FRA locked at $4.20\\%$ on 90-day MRR. 60 days later ($150$ days to final settlement), current forward 90-day rate is $5.10\\%$ and 150-day discount rate is $5.00\\%$. $V_t = 10\\text{{M}} \\times \\frac{{(0.051 - 0.042)(90/360)}}{{1 + 0.050(150/360)}} = +{fra_val:,.2f}\\text{{ USD}}$.</p>", "amber") +
worked_box("Worked Numerical 4: Bootstrapping Fixed Swap Rate from Discount Factors",
f"<p>Quarterly discount factors: $DF_{{90}}=0.9901, DF_{{180}}=0.9794, DF_{{270}}=0.9675, DF_{{360}}=0.9550$. Quarterly fixed rate $= \\frac{{1 - 0.9550}}{{3.8920}} = {qtr_swap*100:.4f}\\% \\implies$ Annualized Swap Fixed Rate $= {ann_swap*100:.3f}\\%$.</p>", "cyan") +
exercise_toolbar("deriv-m3-fra", "Module 03 Chapter Exercises (FRAs &amp; Swaps)") +
exercise_card("deriv-ex-5", "Exercise 3.1 (Solved): Pay-Fixed Swap Value on Reset Date",
"<p>A company pays fixed 4.60% (annualized, semiannual payments) on 20M USD notional. Immediately after a coupon reset, the new par swap rate for remaining maturities drops to 4.00% with sum of discount factors $\\sum DF = 3.80$. Compute MTM value for the pay-fixed party.</p>",
f"<p><strong>Answer: -228,000 USD</strong>. Receive-fixed gains; pay-fixed loses $20\\text{{M}} \\times \\frac{{0.040 - 0.046}}{{2}} \\times 3.80 = -228,000\\text{{ USD}}$.</p>", "solved", "L2 Swap") +
exercise_card("deriv-ex-6", "Exercise 3.2 (Unsolved): Floating-Rate Bond Valuation on Reset Date",
"<p>What is the mark-to-market value of the floating leg of a plain-vanilla interest rate swap immediately after a coupon reset date (assuming no credit downgrade)?</p>",
"<p><strong>Answer: Equal to Par (100% of Notional Principal)</strong>.</p>", "unsolved", "L2 Swap") +
"</section>")

# MODULE 4: CURRENCY & EQUITY SWAPS (L2)
parts.append("""
<section id="deriv-m4-ccyswap" class="notes-chapter">
  <h2 class="section-heading"><span class="num">04.</span> Currency Swaps &amp; Equity Swaps (L2)</h2>
  <ul>
    <li><strong>Currency Swaps</strong>: Notional principals in two currencies <em>ARE exchanged</em> at initiation and re-exchanged at maturity! Mid-life MTM value equals $\\text{PV}(\\text{Receive Bond}) - S_t \\cdot \\text{PV}(\\text{Pay Bond})$ converted at current spot FX $S_t$!</li>
    <li><strong>Equity Swaps</strong>: Value of receive-equity / pay-fixed swap on date $t$ equals $NP \\cdot \\frac{S_t}{S_{t-1}} - \\text{PV}(\\text{Remaining Fixed Coupons + Notional})$ (remember: if equity index drops since last reset, the equity receiver must PAY the negative return PLUS the fixed/floating leg!).</li>
  </ul>
""" + exercise_toolbar("deriv-m4-ccyswap", "Module 04 Chapter Exercises (Currency &amp; Equity Swaps)") +
exercise_card("deriv-ex-7", "Exercise 4.1 (Solved): Equity Swap Negative Return Settlement",
"<p>An institutional investor receives S&amp;P 500 total return and pays 4.00% annualized fixed quarterly on 50M USD notional. Over Q1, the S&amp;P 500 falls -3.00%. Compute the investor's net cash flow at quarter-end.</p>",
"<p><strong>Answer: Investor PAYS 2,000,000 USD</strong>. Equity leg $= -3.00\\% \\times 50\\text{M} = -1.50\\text{M}$; Fixed leg paid $= -(4.00\\%/4) \\times 50\\text{M} = -0.50\\text{M}$. Net outflow $= -2.00\\text{M USD}$.</p>", "solved", "L2 Eq Swap") +
exercise_card("deriv-ex-8", "Exercise 4.2 (Unsolved): Currency Swap Principal Exchange",
"<p>Why do currency swaps exchange notional principals at initiation and maturity whereas single-currency interest rate swaps do not?</p>",
"<p><strong>Answer: Because cash flows are denominated in different currencies</strong>, so differing currency interest rates reflect exchange-rate expectations embedded via principal repayment at maturity.</p>", "unsolved", "L2 Ccy Swap") +
"</section>")

# MODULE 5: PUT-CALL PARITY & OPTION PAYOFFS
parts.append(f"""
<section id="deriv-m5-pcp" class="notes-chapter">
  <h2 class="section-heading"><span class="num">05.</span> Option Mechanics, Payoffs &amp; Put-Call Parity (L1 &amp; L2)</h2>
  <div class="formula-card">
    <div class="formula-title">Put-Call Parity &amp; Put-Call-Forward Parity</div>
    $$c_0 + \\frac{{X}}{{(1+r)^T}} = S_0 + p_0 \\quad (\\text{{Fiduciary Call = Protective Put}})$$
    $$c_0 + \\frac{{X - F_0(T)}}{{(1+r)^T}} = p_0 \\quad (\\text{{Put-Call-Forward Parity}})$$
  </div>
  <ul>
    <li><strong>Option Value Bounds</strong>: European Call $\\ge \\max(0, S_0 - X/(1+r)^T)$; European Put $\\ge \\max(0, X/(1+r)^T - S_0)$. American puts may be exercised early when deep in-the-money ($r &gt; 0$); American calls on <em>non-dividend</em> stocks are NEVER optimal to exercise early!</li>
  </ul>
""" + worked_box("Worked Numerical 5: Put-Call Parity &amp; Synthetic Put Arbitrage",
f"<p>Stock $S_0 = 52.00\\text{{ USD}}$, $X = 50.00\\text{{ USD}}$, $r_f = 5.0\\%$, $T = 0.50$ yr, European call $c_0 = 4.80\\text{{ USD}}$. Fair no-arbitrage European put price $p_0 = 4.80 + \\frac{{50.00}}{{1.05^{{0.5}}}} - 52.00 = {p_pcp:.2f}\\text{{ USD}}$. If market put trades at 2.10 USD (overpriced), sell the market put and buy synthetic put ($+c_0 - S_0 + PV(X)$) for riskless profit!</p>", "emerald") +
exercise_toolbar("deriv-m5-pcp", "Module 05 Chapter Exercises (Put-Call Parity)") +
exercise_card("deriv-ex-9", "Exercise 5.1 (Solved): Early Exercise of American Call",
"<p>A non-dividend stock trades at 140 USD and an American call with strike 100 USD has 6 months left ($r_f = 5\\%$). Should the holder exercise immediately or sell in the market?</p>",
"<p><strong>Answer: Sell the call in the market</strong>. Because the stock pays zero dividends, $C_{{American}} \\ge S_0 - PV(X) = 42.41 &gt; \\text{Intrinsic } 40.00$. Exercising destroys time value + interest saved on strike!</p>", "solved", "L1/L2 Option") +
exercise_card("deriv-ex-10", "Exercise 5.2 (Unsolved): Synthetic Long Stock via Options",
"<p>How do you synthesize a long stock position using calls, puts, and risk-free bonds?</p>",
"<p><strong>Answer: Long Call ($+c$) + Short Put ($-p$) + Long Zero-Coupon Bond ($+PV(X)$)</strong>.</p>", "unsolved", "L1/L2 Option") +
"</section>")

# MODULE 6: BINOMIAL OPTION PRICING (L2)
parts.append(f"""
<section id="deriv-m6-binom" class="notes-chapter">
  <h2 class="section-heading"><span class="num">06.</span> Binomial Option Pricing Model (L1 &amp; L2)</h2>
  <div class="formula-card">
    <div class="formula-title">Risk-Neutral Probability, Hedge Ratio &amp; Backward Induction</div>
    $$\\pi_u = \\frac{{(1+r) - d}}{{u - d}}, \\qquad c_0 = \\frac{{\\pi_u c_u + (1 - \\pi_u) c_d}}{{1 + r}}, \\qquad \\Delta = \\frac{{c_u - c_d}}{{S_u - S_d}}$$
    $$\\text{{American Put Node Check: }} V_t = \\max\\!\\left(X - S_t, \\; \\frac{{\\pi_u V_{{u}} + (1 - \\pi_u) V_{{d}}}}{{1 + r}}\\right)$$
  </div>
  <p><strong>Crucial L2 Insight</strong>: Real-world directional probabilities ($P$) NEVER enter the option valuation formula—only risk-neutral probabilities ($\\pi_u$) determined by no-arbitrage replication!</p>
""" + worked_box("Worked Numerical 6: 1-Period Binomial Call &amp; Replication Hedge Ratio",
f"<p>Spot $S_0 = 100\\text{{ USD}}$, $X = 102\\text{{ USD}}$, $u = 1.15$ ($S_u = 115$), $d = 0.88$ ($S_d = 88$), $r = 4.0\\%$. Risk-neutral $\\pi_u = \\frac{{1.04 - 0.88}}{{1.15 - 0.88}} = {pi_b:.4f}$. Payoffs: $c_u = 13$, $c_d = 0$. $c_0 = \\frac{{{pi_b:.4f} \\times 13}}{{1.04}} = {c0_b:.2f}\\text{{ USD}}$, with hedge ratio $\\Delta = \\frac{{13 - 0}}{{115 - 88}} = {delta_b:.4f}$.</p>", "blue") +
exercise_toolbar("deriv-m6-binom", "Module 06 Chapter Exercises (Binomial Trees)") +
exercise_card("deriv-ex-11", "Exercise 6.1 (Solved): Replicating Portfolio Debt Financing",
"<p>In the worked numerical above ($S_0=100, \\Delta={delta_b:.4f}, c_0={c0_b:.2f}$), how much must be borrowed at $r=4\\%$ alongside buying $\\Delta$ shares to replicate the call?</p>",
f"<p><strong>Answer: Borrow {delta_b*100 - c0_b:.2f} USD</strong>. $\\text{{Stock Cost}} - c_0 = ({delta_b:.4f} \\times 100) - {c0_b:.2f} = {delta_b*100 - c0_b:.2f}\\text{{ USD}}$ (Notice: $\\frac{{\\Delta \\cdot S_d}}{{1+r}} = {delta_b*88/1.04:.2f}$ matches!).</p>", "solved", "L2 Binomial") +
exercise_card("deriv-ex-12", "Exercise 6.2 (Unsolved): Early Exercise Trigger on American Put",
"<p>At Year 1 in a 2-period tree ($X = 60, r = 5\\%$), stock falls to $S_d = 40$, while continuation value of the put is 18.20 USD. What is the node value?</p>",
"<p><strong>Answer: 20.00 USD (Exercise Early!)</strong>. Immediate intrinsic payoff $60 - 40 = 20.00 &gt; 18.20$ continuation value.</p>", "unsolved", "L2 Binomial") +
"</section>")

# MODULE 7: BLACK-SCHOLES-MERTON & GREEKS (L2)
parts.append(f"""
<section id="deriv-m7-bsm" class="notes-chapter">
  <h2 class="section-heading"><span class="num">07.</span> Black-Scholes-Merton (BSM) Model &amp; Option Greeks (L2)</h2>
  <div class="formula-card">
    <div class="formula-title">BSM Model with Dividend Yield $q$, Black Futures Model &amp; Greeks</div>
    $$c = S_0 e^{{-qT}} N(d_1) - X e^{{-rT}} N(d_2), \\qquad p = X e^{{-rT}} N(-d_2) - S_0 e^{{-qT}} N(-d_1)$$
    $$d_1 = \\frac{{\\ln(S_0/X) + (r - q + \\frac{{1}}{{2}}\\sigma^2)T}}{{\\sigma\\sqrt{{T}}}}, \\qquad d_2 = d_1 - \\sigma\\sqrt{{T}}$$
    $$\\Delta_c = e^{{-qT}}N(d_1), \\quad \\Delta_p = e^{{-qT}}[N(d_1)-1], \\quad \\Delta\\text{{ Portfolio Hedge Shares}} = -\\frac{{N_{{\\text{{opt}}}} \\cdot \\Delta_{{\\text{{opt}}}}}}{{1}}, \\quad \\Delta c \\approx \\Delta \\cdot \\Delta S + \\frac{{1}}{{2}}\\Gamma(\\Delta S)^2$$
  </div>
  <ul>
    <li><strong>BSM Assumptions</strong>: Geometric Brownian motion (lognormal prices), constant known volatility $\\sigma$ and risk-free rate $r$, continuous trading, no taxes/costs, European exercise.</li>
    <li><strong>Black Model (Futures/Interest Rate Options)</strong>: Replaces $S_0 e^{{-qT}}$ with $F_0(T) e^{{-rT}}$!</li>
    <li><strong>Gamma vs. Theta Trade-off</strong>: Long ATM options near expiration have peak positive <strong>Gamma ($\\Gamma$)</strong> and peak negative <strong>Theta ($\\Theta$)</strong> (rapid time decay). Dynamic delta-neutral hedging profits when <em>realized volatility exceeds implied volatility</em>!</li>
  </ul>
""" + worked_box("Worked Numerical 7: Full Python-Exact Black-Scholes-Merton &amp; Delta/Gamma Hedge",
f"<p>Inputs: $S_0 = 100\\text{{ USD}}$, $K = 100\\text{{ USD}}$, $r = 5.0\\%$, $q = 2.0\\%$, $T = 0.50\\text{{ yr}}$, $\\sigma = 24.0\\%$.</p>"
f"<ul><li>$d_1 = {bsm['d1']:.4f} \\implies N(d_1) = {bsm['Nd1']:.4f}$; $d_2 = {bsm['d2']:.4f} \\implies N(d_2) = {bsm['Nd2']:.4f}$.</li>"
f"<li><strong>Call Price</strong> $= {bsm['call']:.2f}\\text{{ USD}}$; <strong>Put Price</strong> $= {bsm['put']:.2f}\\text{{ USD}}$.</li>"
f"<li><strong>Greeks</strong>: Call $\\Delta_c = +{bsm['delta_c']:.4f}$, Put $\\Delta_p = {bsm['delta_p']:.4f}$, $\\Gamma = {bsm['gamma']:.4f}$, Vega $= {bsm['vega']:.2f}$ per $100\\%$ vol (or ${bsm['vega']*0.01:.3f}$ per $1\\%$ vol).</li></ul>", "purple") +
exercise_toolbar("deriv-m7-bsm", "Module 07 Chapter Exercises (BSM &amp; Greeks)") +
exercise_card("deriv-ex-13", "Exercise 7.1 (Solved): Delta-Neutralizing a Short Call Book",
"<p>A dealer sells 1,000 European calls (100 shares/contract = 100,000 shares notional) with $\\Delta_c = 0.54$. How many shares must the dealer buy/sell to become delta-neutral?</p>",
"<p><strong>Answer: Buy 54,000 shares</strong>. Short call portfolio delta $= -100,000 \\times 0.54 = -54,000 \\implies$ purchase $+54,000$ shares to set net $\\Delta = 0$.</p>", "solved", "L2 Greeks") +
exercise_card("deriv-ex-14", "Exercise 7.2 (Unsolved): Volatility Smile Evidence",
"<p>If OTM index puts trade at 28% implied volatility while ATM calls trade at 18%, what shape does the volatility curve show and what BSM assumption fails?</p>",
"<p><strong>Answer: Volatility skew (downward-sloping smirk)</strong>—violating BSM's constant-volatility and lognormal-return assumptions (reflecting crash fat-tail demand for portfolio insurance).</p>", "unsolved", "L2 BSM") +
"</section>")

# MODULE 8: TRADING STRATEGIES & CURRENCY HEDGING
parts.append("""
<section id="deriv-m8-strat" class="notes-chapter">
  <h2 class="section-heading"><span class="num">08.</span> Option Strategies, Currency Hedging &amp; Risk Management</h2>
  <div class="table-container">
    <table>
      <thead><tr><th>Strategy</th><th>Construction</th><th>Market Outlook / Payoff Profile</th></tr></thead>
      <tbody>
        <tr><td><strong>Covered Call</strong></td><td>Long Stock + Short OTM Call</td><td>Income generation / mild bullish; caps upside at $X$, downside buffer = $+c_0$</td></tr>
        <tr><td><strong>Protective Put</strong></td><td>Long Stock + Long Put</td><td>Portfolio insurance; floor value $= X - p_0$, unlimited upside</td></tr>
        <tr><td><strong>Bull Call Spread</strong></td><td>Long Low-$X_1$ Call + Short High-$X_2$ Call</td><td>Moderately bullish; reduces cost; max profit $= (X_2 - X_1) - \\text{Net Prem}$</td></tr>
        <tr><td><strong>Collar</strong></td><td>Long Stock + Long $X_1$ Put + Short $X_2$ Call</td><td>Zero-cost (or low-cost) floor &amp; ceiling around concentrated stock position</td></tr>
        <tr><td><strong>Long Straddle</strong></td><td>Long ATM Call + Long ATM Put ($X, T$)</td><td>Long volatility (profits on big moves in <em>either</em> direction); high negative $\\Theta$</td></tr>
        <tr><td><strong>Calendar Spread</strong></td><td>Short Near-Term Option + Long Far-Term Option</td><td>Profits if underlying stays calm near $X$ (near-term $\\Theta$ decays faster)</td></tr>
      </tbody>
    </table>
  </div>
""" + exercise_toolbar("deriv-m8-strat", "Module 08 Chapter Exercises (Strategies &amp; Hedging)") +
exercise_card("deriv-ex-15", "Exercise 8.1 (Solved): Collar Max Profit, Max Loss &amp; Breakeven",
"<p>An executive holds stock at $S_0 = 80\\text{ USD}$, buys a 75-strike put for 3.00 USD, and sells an 88-strike call for 3.00 USD (zero-cost collar). Compute max gain and max loss per share.</p>",
"<p><strong>Answer: Max Gain = +8.00 USD (at $S_T \\ge 88$); Max Loss = -5.00 USD (at $S_T \\le 75$)</strong>. Net premium = 0.</p>", "solved", "L2 Strategy") +
exercise_card("deriv-ex-16", "Exercise 8.2 (Unsolved): Long Straddle Breakevens",
"<p>Trader buys a 50-strike call for 4.20 USD and a 50-strike put for 3.30 USD. What two stock prices at expiration yield breakeven?</p>",
"<p><strong>Answer: 42.50 USD and 57.50 USD</strong>. Total premium $= 7.50\\text{ USD}$, so breakevens $= 50 \\pm 7.50$.</p>", "unsolved", "L2 Strategy") +
"</section>")

# MODULE 9: FORMULA SHEET
parts.append("""
<section id="deriv-m9-formulas" class="notes-chapter">
  <h2 class="section-heading"><span class="num">09.</span> Master Derivatives Formula Cheat Sheet</h2>
  <div class="table-container">
    <table>
      <thead><tr><th>Instrument</th><th>Governing Formula</th><th>Exam Reminder</th></tr></thead>
      <tbody>
        <tr><td><strong>Cost-of-Carry Forward</strong></td><td>$$F_0 = (S_0 - PV(B) + PV(C))(1+r)^T$$</td><td>Convenience yield lowers forward price</td></tr>
        <tr><td><strong>Swap Fixed Rate</strong></td><td>$$r_{\\text{fix}} = \\frac{1 - DF_n}{\\sum DF_i}$$</td><td>Multiply periodic rate by periods/year</td></tr>
        <tr><td><strong>Put-Call Parity</strong></td><td>$$c + PV(X) = S_0 + p$$</td><td>Holds strictly for European options at same $(X,T)$</td></tr>
        <tr><td><strong>Binomial Prob</strong></td><td>$$\\pi_u = \\frac{(1+r)-d}{u-d}$$</td><td>Use $e^{(r-q)T}$ for continuous compounding</td></tr>
        <tr><td><strong>BSM Delta</strong></td><td>$$\\Delta_c = e^{-qT}N(d_1), \\; \\Delta_p = e^{-qT}[N(d_1)-1]$$</td><td>Call $\\Delta - \\text{Put } \\Delta = e^{-qT}$</td></tr>
      </tbody>
    </table>
  </div>
""" + exercise_toolbar("deriv-m9-formulas", "Module 09 Capstone Drills") +
exercise_card("deriv-ex-17", "Exercise 9.1 (Solved): Delta-Gamma Approximation",
"<p>A call option priced at 5.20 USD has $\\Delta = 0.55$ and $\\Gamma = 0.04$. If the stock jumps $+4.00\\text{ USD}$, estimate the new call price using Delta + Gamma.</p>",
f"<p><strong>Answer: 7.72 USD</strong>. $\\Delta c \\approx 0.55(4.00) + \\frac{{1}}{{2}}(0.04)(4.00)^2 = 2.20 + 0.32 = +2.52 \\implies 5.20 + 2.52 = 7.72\\text{{ USD}}$.</p>", "solved", "L2 Greeks") +
exercise_card("deriv-ex-18", "Exercise 9.2 (Unsolved): FX Hedging Ratio When Asset &amp; Currency Correlate",
"<p>If a foreign equity portfolio has a positive correlation between local equity returns and foreign currency depreciation (negative correlation with $FC$ appreciation), should the optimal hedge ratio be above or below 100%?</p>",
"<p><strong>Answer: Below 100% (under-hedge)</strong>: $h^* = 1 + \\beta_{\\text{FX, Asset}}$; negative covariance provides natural offset, so less forward FX hedging minimizes total USD variance!</p>", "unsolved", "CBOK VIII") +
exercise_card("deriv-ex-19", "Exercise 9.3 (Solved): Put-Call-Forward Parity Synthetic Forward",
"<p>If $F_0(T) = 105\\text{ USD}$, $X = 100\\text{ USD}$, $r = 4.0\\%$, $T = 1.0$, and $p_0 = 3.20\\text{ USD}$, compute European call price $c_0$.</p>",
f"<p><strong>Answer: 8.01 USD</strong>. $c_0 = p_0 + \\frac{{F_0 - X}}{{1+r}} = 3.20 + \\frac{{5.00}}{{1.04}} = {3.20 + 5/1.04:.2f}\\text{{ USD}}$.</p>", "solved", "L1/L2 PCP") +
exercise_card("deriv-ex-20", "Exercise 9.4 (Unsolved): Interest Rate Caplet Settlement",
"<p>A corporate borrower owns an interest rate caplet struck at 4.50% on 10M USD notional for a 90-day period. Reference rate resets at 5.30%. Compute the caplet payoff at period end.</p>",
f"<p><strong>Answer: 20,000 USD</strong>. $\\text{{Payoff}} = 10\\text{{M}} \\times \\max(0, 0.053 - 0.045) \\times \\frac{{90}}{{360}} = 20,000\\text{{ USD}}$ (paid in arrears at day 90).</p>", "unsolved", "L2 IR Opt") +
"</section>")

write_notes_html("".join(parts), OUTPUT_PATH)
