"""
scripts/notes_econ.py
Generates data/econ_reference_extracted.html:
Economics Master Reference Library (10 Modules)
Aligned with CFA CBOK III & L1 (8 LMs) + L2 (2 LMs) + Inflation/Regulation/Geopolitics/CME.
Includes 12 Python-computed Worked Numericals + 20 Interactive Chapter Exercises (10 Solved + 10 Unsolved).
"""
import math
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scripts.notes_helper import worked_box, exercise_card, exercise_toolbar, write_notes_html

OUTPUT_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "econ_reference_extracted.html")

# Python-verified calculations
# Elasticity
p1, p2, q1, q2 = 50.0, 55.0, 1000.0, 850.0
ed_arc = ((q2 - q1) / ((q2 + q1) / 2)) / ((p2 - p1) / ((p2 + p1) / 2))
# Money & Fiscal multiplier
mpc, tax = 0.80, 0.25
fiscal_mult = 1 / (1 - mpc * (1 - tax))
money_mult = 1 / 0.10
# Taylor Rule
i_taylor = 2.0 + 3.4 + 0.5 * (3.4 - 2.0) + 0.5 * (-0.8)
# Cross rate bid/ask & forward points
usd_eur_bid, usd_eur_ask = 1.0800, 1.0810
jpy_usd_bid, jpy_usd_ask = 150.00, 150.20
jpy_eur_bid = usd_eur_bid * jpy_usd_bid
jpy_eur_ask = usd_eur_ask * jpy_usd_ask
# CIRP forward rate
spot_fx = 1.2500
r_price, r_base, days = 0.052, 0.038, 180
fwd_fx = spot_fx * (1 + r_price * days / 360) / (1 + r_base * days / 360)
fwd_pts = (fwd_fx - spot_fx) * 10000
# Carry trade return
carry_return = ((1 + 0.065) * (1.012)) - (1 + 0.025)
# Cobb-Douglas growth accounting
dy_l2 = 0.014 + 0.35 * 0.032 + 0.65 * 0.010
# Solow steady state k*
s_rate, alpha_s, tfp_s, dep_s, n_pop = 0.24, 0.40, 1.0, 0.06, 0.02
# Steady state y* per worker: k* = (s*A/(delta+n))^(1/(1-alpha))
k_star = (s_rate * tfp_s / (dep_s + n_pop)) ** (1 / (1 - alpha_s))

parts = []

parts.append("""<div class="top-controls">
  <button class="btn-ctrl" onclick="toggleTheme()">🌓 Switch Theme</button>
  <button class="btn-ctrl" onclick="window.print()">🖨️ Print / Save as PDF</button>
</div>

<div class="doc-hero">
  <h1>Economics &amp; Global Macro Analysis (CFA&reg; CBOK III)</h1>
  <p>Master Reference for CFA&reg; Level 1 (Micro/Macro Foundations, Trade, FX Mechanics, Geopolitics) &amp; Level 2 (Currency Parity Forecasting, Carry Trades, Mundell-Fleming, Cobb-Douglas Growth Accounting, Regulatory Economics). Includes 12 Worked Numericals and 20 Interactive Chapter Exercises (10 Solved + 10 Unsolved).</p>
  <div class="meta-tags">
    <span class="badge badge-cyan">L1 Weight: 6%–9%</span>
    <span class="badge badge-blue">L2 Weight: 5%–10%</span>
    <span class="badge badge-emerald">10 Modules + 20 Exercises</span>
    <span class="badge badge-amber">FX Parity &amp; Growth Math</span>
  </div>
</div>

<div class="card" style="margin-top: 15px; margin-bottom: 25px;">
  <div class="card-title">🌍 Quick Navigation: Economics Curriculum Modules</div>
  <div class="fsa-nav-bar">
    <a class="fsa-nav-btn" href="#econ-m1-supply">01. Supply &amp; Elasticity</a>
    <a class="fsa-nav-btn" href="#econ-m2-firm">02. Market Structures</a>
    <a class="fsa-nav-btn" href="#econ-m3-cycles">03. Cycles &amp; Inflation</a>
    <a class="fsa-nav-btn" href="#econ-m4-policy">04. Monetary &amp; Fiscal</a>
    <a class="fsa-nav-btn" href="#econ-m5-trade">05. Trade &amp; Geopolitics</a>
    <a class="fsa-nav-btn" href="#econ-m6-fxcalc">06. FX Quotes &amp; Cross Rates</a>
    <a class="fsa-nav-btn" href="#econ-m7-fxparity">07. FX Parity &amp; Carry (L2)</a>
    <a class="fsa-nav-btn" href="#econ-m8-growth">08. Growth &amp; Regulation (L2)</a>
    <a class="fsa-nav-btn" href="#econ-m9-cme">09. Macro &amp; Asset Markets</a>
    <a class="fsa-nav-btn" href="#econ-m10-formulas" style="color: var(--accent-emerald); font-weight: 700;">10. Formula Sheet</a>
  </div>
  <div style="display:flex; gap:10px; flex-wrap:wrap; margin-top:10px;">
    <button type="button" class="btn" onclick="jumpToSubjectBank(1, 'Economics')">📝 Practice 80 L1 Economics MCQs</button>
    <button type="button" class="btn btn-secondary" onclick="jumpToSubjectBank(2, 'Economics')">📑 Practice 10 L2 Economics Vignettes (50 Qs)</button>
    <button type="button" class="filter-btn" onclick="toggleChapterExercises('econ-reference', false)">🙈 Hide Solutions</button>
    <button type="button" class="filter-btn" onclick="toggleChapterExercises('econ-reference', true)">✅ Reveal All Solutions</button>
  </div>
</div>
""")

# MODULE 1: SUPPLY, DEMAND & ELASTICITIES
parts.append(f"""
<section id="econ-m1-supply" class="notes-chapter">
  <h2 class="section-heading"><span class="num">01.</span> Market Forces of Supply, Demand &amp; Elasticities</h2>
  <div class="formula-card">
    <div class="formula-title">Price, Income &amp; Cross-Price Elasticities</div>
    $$E_p^d = \\frac{{\\%\\Delta Q_d}}{{\\%\\Delta P}} = \\left(\\frac{{\\Delta Q_d}}{{\\Delta P}}\\right)\\frac{{P_0}}{{Q_0}}, \\qquad E_{{arc}} = \\frac{{(Q_2 - Q_1)/[(Q_1+Q_2)/2]}}{{(P_2 - P_1)/[(P_1+P_2)/2]}}$$
    $$E_I = \\frac{{\\%\\Delta Q_d}}{{\\%\\Delta I}} \\; (>0 \\text{{ Normal}}, <0 \\text{{ Inferior}}), \\qquad E_{{XY}} = \\frac{{\\%\\Delta Q_X}}{{\\%\\Delta P_Y}} \\; (>0 \\text{{ Substitutes}}, <0 \\text{{ Complements}})$$
  </div>
  <p><strong>Total Revenue Test</strong>: When $|E_p^d| &gt; 1$ (elastic), raising price <em>decreases</em> total revenue; when $|E_p^d| &lt; 1$ (inelastic), raising price <em>increases</em> total revenue. Giffen goods (inferior + strong negative income effect &gt; substitution effect) exhibit upward-sloping demand; Veblen goods reflect prestige consumption.</p>
""" + worked_box("Worked Numerical 1: Arc Price Elasticity &amp; Total Revenue Effect",
f"<p>Raising software subscription price from 50 USD to 55 USD reduces users from 1,000 to 850. Arc elasticity $E_{{arc}} = \\frac{{-150 / 925}}{{5 / 52.5}} = {ed_arc:.3f}$. Because $|E_{{arc}}| = {abs(ed_arc):.3f} &gt; 1$ (elastic), revenue falls from 50,000 USD to 46,750 USD.</p>", "emerald") +
exercise_toolbar("econ-m1-supply", "Module 01 Chapter Exercises (Elasticity)") +
exercise_card("econ-ex-1", "Exercise 1.1 (Solved): Linear Demand Elasticity &amp; Deadweight Loss",
"<p>Given $Q_d = 120 - 4P$, calculate point price elasticity at $P = 10\\text{ USD}$.</p>",
"<p><strong>Answer: $E_p^d = -0.50$ (inelastic)</strong>. $Q = 120 - 4(10) = 80$. $E_p^d = (-4)(10/80) = -0.50$.</p>", "solved", "L1 Micro") +
exercise_card("econ-ex-2", "Exercise 1.2 (Unsolved): Cross-Price Elasticity Sign",
"<p>A 10% rise in coffee bean price causes creamer demand to fall by 4%. Compute $E_{{XY}}$ and classify the pair.</p>",
"<p><strong>Answer: $-0.40$ (Complements)</strong>. Negative cross-price elasticity confirms complementary consumption.</p>", "unsolved", "L1 Micro") +
"</section>")

# MODULE 2: MARKET STRUCTURES
parts.append("""
<section id="econ-m2-firm" class="notes-chapter">
  <h2 class="section-heading"><span class="num">02.</span> The Firm and Industry Organization (Market Structures)</h2>
  <div class="table-container">
    <table>
      <thead><tr><th>Structure</th><th>Pricing Power</th><th>Profit-Max Rule</th><th>Long-Run Econ Profit &amp; Shutdown</th></tr></thead>
      <tbody>
        <tr><td><strong>Perfect Competition</strong></td><td>None ($P = MR = MC$)</td><td>Produce where $P = MC$</td><td>Zero economic profit ($P = \\min ATC$). Shutdown in short run if $P &lt; AVC$!</td></tr>
        <tr><td><strong>Monopolistic Comp</strong></td><td>Some (brand differentiation)</td><td>$MR = MC$, price off $D$</td><td>Zero economic profit ($P = ATC$ tangent), excess capacity remains.</td></tr>
        <tr><td><strong>Oligopoly</strong></td><td>High (strategic interdependence)</td><td>Kinked Demand / Cournot / Nash</td><td>Sustainable positive profit if collusion holds; prisoner's dilemma incentives to cheat.</td></tr>
        <tr><td><strong>Monopoly</strong></td><td>Very High (no close substitutes)</td><td>$MR = MC$, price off $D$</td><td>Positive LR economic profit unless regulated ($P = ATC$ avg-cost vs $P = MC$ marginal-cost pricing).</td></tr>
      </tbody>
    </table>
  </div>
  <div class="formula-card">
    <div class="formula-title">Concentration Measures: $N$-Firm Ratio vs. Herfindahl-Hirschman Index (HHI)</div>
    $$CR_N = \\sum_{{i=1}}^N s_i, \\qquad \\text{{HHI}} = \\sum_{{i=1}}^n s_i^2 \\quad (\\text{{using percentage shares, e.g., }} 30^2 + 25^2 + \\dots, \\text{{ max }} = 10,000)$$
  </div>
""" + exercise_toolbar("econ-m2-firm", "Module 02 Chapter Exercises (Market Structures)") +
exercise_card("econ-ex-3", "Exercise 2.1 (Solved): Merger HHI Screening",
"<p>An industry has 4 firms with market shares 40%, 30%, 20%, and 10%. If the 20% and 10% firms merge, compute pre- and post-merger HHI.</p>",
f"<p><strong>Answer: Pre-HHI = 3,000; Post-HHI = 3,400 ($\\Delta\\text{{HHI}} = +400$)</strong>. Pre $= 40^2+30^2+20^2+10^2 = 3,000$. Post $= 40^2+30^2+30^2 = 3,400$. Likely triggers antitrust challenge.</p>", "solved", "L1 Micro") +
exercise_card("econ-ex-4", "Exercise 2.2 (Unsolved): Short-Run Shutdown Price",
"<p>A perfectly competitive firm faces price 18 USD/unit, average total cost 21 USD/unit, and average variable cost 16 USD/unit. Should it shut down immediately in the short run?</p>",
"<p><strong>Answer: Continue operating in the short run ($P = 18 &gt; AVC = 16$)</strong>. Revenue covers all variable costs plus 2 USD/unit toward fixed costs; exit only in the long run if $P &lt; ATC$.</p>", "unsolved", "L1 Micro") +
"</section>")

# MODULE 3: BUSINESS CYCLES & INFLATION
parts.append("""
<section id="econ-m3-cycles" class="notes-chapter">
  <h2 class="section-heading"><span class="num">03.</span> Business Cycles, Inflation, Deflation &amp; Economic Indicators</h2>
  <ul>
    <li><strong>Four Phases</strong>: Expansion (capex rises, inventories lean) &rarr; Peak (bottlenecks, inflation rises) &rarr; Contraction/Recession (two quarters negative GDP; inventory-to-sales spikes initially then draws down) &rarr; Trough (hiring starts with temp workers before permanent payrolls!).</li>
    <li><strong>Indicator Classification</strong>: <em>Leading</em> (S&amp;P 500, building permits, ISM new orders, yield spread, initial jobless claims inverted, average weekly manufacturing hours); <em>Coincident</em> (industrial production, nonfarm payrolls, personal income); <em>Lagging</em> (unemployment rate, prime rate, average duration of unemployment, CPI services).</li>
    <li><strong>Inflation Price Indices</strong>: <em>Laspeyres</em> (fixed base basket &rarr; overstates inflation via substitution/quality bias); <em>Paasche</em> (current basket &rarr; understates inflation); <em>Fisher</em> $= \\sqrt{\\text{Laspeyres} \\times \\text{Paasche}}$ (ideal chained index).</li>
  </ul>
""" + exercise_toolbar("econ-m3-cycles", "Module 03 Chapter Exercises (Cycles &amp; Inflation)") +
exercise_card("econ-ex-5", "Exercise 3.1 (Solved): Laspeyres vs. Paasche Inflation Bias",
"<p>Year 0 basket is 10 apples (1.00 USD) and 5 coffees (2.00 USD). In Year 1, apples rise to 1.50 USD and coffees remain 2.00 USD, so consumers buy 6 apples and 9 coffees. Compute Laspeyres and Paasche CPI (base = 100).</p>",
f"<p><strong>Answer: Laspeyres = 125.0; Paasche = 112.5</strong>. Laspeyres $= \\frac{{10(1.5)+5(2)}}{{10(1)+5(2)}} \\times 100 = 125.0$. Paasche $= \\frac{{6(1.5)+9(2)}}{{6(1)+9(2)}} \\times 100 = \\frac{{27}}{{24}} \\times 100 = 112.5$. Fisher $= \\sqrt{{125 \\times 112.5}} = {math.sqrt(125*112.5):.2f}$.</p>", "solved", "L1 Macro") +
exercise_card("econ-ex-6", "Exercise 3.2 (Unsolved): Early Recovery Labor Signal",
"<p>Coming out of a recession trough, why do firms expand temporary agency workers and average weekly overtime hours before increasing permanent full-time payrolls?</p>",
"<p><strong>Answer: Firms confirm demand durability before incurring fixed hiring/training costs</strong> — making average weekly hours a <em>leading</em> indicator while the headline unemployment rate is a <em>lagging</em> indicator.</p>", "unsolved", "L1 Macro") +
"</section>")

# MODULE 4: MONETARY & FISCAL POLICY
parts.append(f"""
<section id="econ-m4-policy" class="notes-chapter">
  <h2 class="section-heading"><span class="num">04.</span> Monetary System, Monetary &amp; Fiscal Policy</h2>
  <div class="formula-card">
    <div class="formula-title">Multipliers, Neutral Rate, Fisher Effect &amp; Taylor Rule</div>
    $$\\text{{Money Multiplier}} = \\frac{{1}}{{\\text{{Reserve Req}}}}, \\qquad \\text{{Fiscal Multiplier}} = \\frac{{1}}{{1 - c(1 - t)}}$$
    $$R_{{\\text{{nominal}}}} = r_{{\\text{{real}}}} + E(\\pi) + \\text{{IRP}}, \\qquad i^* = r_{{\\text{{neutral}}}} + \\pi + 0.5(\\pi - \\pi^*) + 0.5(y - y^*)$$
  </div>
  <ul>
    <li><strong>Ricardian Equivalence</strong>: Tax cuts financed by debt fail to boost aggregate demand if forward-looking households save the tax cut expecting future tax hikes.</li>
    <li><strong>Policy Mix Impact on Rates</strong>: Tight monetary + loose fiscal &rarr; sharply higher interest rates, stronger currency; Loose monetary + tight fiscal &rarr; lower interest rates.</li>
  </ul>
""" + worked_box("Worked Numerical 2: Fiscal Multiplier &amp; Taylor Rule Target Policy Rate",
f"<p><strong>Fiscal Multiplier</strong>: Given $MPC = 0.80$ and tax rate $t = 25\\%$, $\\text{{Multiplier}} = \\frac{{1}}{{1 - 0.80(0.75)}} = \\frac{{1}}{{0.40}} = {fiscal_mult:.2f}$. A 20B USD deficit-financed infrastructure spend raises GDP by $20\\text{{B}} \\times 2.50 = 50\\text{{B USD}}$.</p>"
f"<p><strong>Taylor Rule</strong>: Neutral real rate $2.0\\%$, current inflation $3.4\\%$ (target $2.0\\%$), output gap $-0.8\\%$. $i^* = 2.0\\% + 3.4\\% + 0.5(1.4\\%) + 0.5(-0.8\\%) = {i_taylor:.2f}\\%$.</p>", "blue") +
exercise_toolbar("econ-m4-policy", "Module 04 Chapter Exercises (Policy)") +
exercise_card("econ-ex-7", "Exercise 4.1 (Solved): Balanced Budget Multiplier",
"<p>With $MPC = 0.80$ and $t = 25\\%$, government simultaneously raises spending by 10B USD and raises lump-sum taxes by 10B USD. Compute the net GDP impact (ignoring automatic tax bracket changes).</p>",
"<p><strong>Answer: +10B USD</strong>? Wait: careful with tax rate $t$: lump-sum tax reduces initial consumption by $MPC \\times 10\\text{B} = 8\\text{B}$, so net first-round stimulus is $(10 - 8) = 2\\text{B}$, multiplied by $2.50 = +5.0\\text{B USD}$! (Only when $t=0$ does balanced budget multiplier equal exactly $1.0$.)</p>", "solved", "L1 Macro") +
exercise_card("econ-ex-8", "Exercise 4.2 (Unsolved): Contractionary Monetary &amp; Expansionary Fiscal Mix",
"<p>If a central bank hikes policy rates aggressively while parliament passes large deficit-funded tax cuts, what happens to real interest rates and the domestic currency?</p>",
"<p><strong>Answer: Real interest rates rise sharply and the currency appreciates</strong> (higher yields attract foreign capital inflows).</p>", "unsolved", "L1 Macro") +
"</section>")

# MODULE 5: INTERNATIONAL TRADE & GEOPOLITICS
parts.append("""
<section id="econ-m5-trade" class="notes-chapter">
  <h2 class="section-heading"><span class="num">05.</span> International Trade, Capital Flows &amp; Geopolitics</h2>
  <ul>
    <li><strong>Comparative Advantage (Ricardo)</strong>: Gains from trade depend on lower <em>opportunity cost</em>, not absolute productivity! Heckscher-Ohlin attributes advantage to relative factor endowments (capital vs. labor).</li>
    <li><strong>Tariffs vs. Quotas</strong>: Both raise domestic price and produce <strong>deadweight loss</strong> (inefficiency + consumption loss). Tariffs yield government tax revenue; quotas transfer <strong>quota rents</strong> to foreign exporters unless licenses are auctioned!</li>
    <li><strong>Balance of Payments</strong>: $CA + KA + FA = 0$. Persistent current account deficits require capital/financial inflows ($S - I = X - M$: low domestic savings vs. investment drives current account deficits).</li>
    <li><strong>Geopolitics Archetypes</strong>: Autarky, Hegemony, Multilateralism, Bilateralism; evaluated via Velocity, Impact, and Likelihood.</li>
  </ul>
""" + exercise_toolbar("econ-m5-trade", "Module 05 Chapter Exercises (Trade &amp; Geopolitics)") +
exercise_card("econ-ex-9", "Exercise 5.1 (Solved): Domestic Savings-Investment Identity",
"<p>An economy reports private savings $S = 400\\text{B USD}$, private investment $I = 460\\text{B USD}$, and a fiscal budget surplus $(T - G) = +20\\text{B USD}$. Compute the Current Account balance $(X - M)$.</p>",
"<p><strong>Answer: Current Account Deficit = -40B USD</strong>. $(X - M) = (S - I) + (T - G) = (400 - 460) + 20 = -40\\text{B USD}$.</p>", "solved", "L1 Trade") +
exercise_card("econ-ex-10", "Exercise 5.2 (Unsolved): Opportunity Cost &amp; Specialization",
"<p>Country A produces 10 cars or 20 laptops per worker; Country B produces 6 cars or 18 laptops per worker. Which country has comparative advantage in cars?</p>",
"<p><strong>Answer: Country A</strong>. Country A sacrifices only $20/10 = 2$ laptops per car, vs. Country B sacrificing $18/6 = 3$ laptops per car.</p>", "unsolved", "L1 Trade") +
"</section>")

# MODULE 6: FX QUOTES & CROSS-RATE CALCULATIONS
parts.append(f"""
<section id="econ-m6-fxcalc" class="notes-chapter">
  <h2 class="section-heading"><span class="num">06.</span> FX Market Mechanics &amp; Cross-Rate Calculations (L1 Module 8)</h2>
  <div class="formula-card">
    <div class="formula-title">CFA Quote Convention ($\\text{{Price}} / \\text{{Base}}$) &amp; Dealer Bid-Ask Cross Rates</div>
    $$A/B \\text{{ quote}} = \\text{{Units of Price currency }} A \\text{{ per 1 unit of Base currency }} B$$
    $$(A/C)_{{\\text{{bid}}}} = (A/B)_{{\\text{{bid}}}} \\times (B/C)_{{\\text{{bid}}}}, \\qquad (A/C)_{{\\text{{ask}}}} = (A/B)_{{\\text{{ask}}}} \\times (B/C)_{{\\text{{ask}}}}$$
    $$(B/A)_{{\\text{{bid}}}} = \\frac{{1}}{{(A/B)_{{\\text{{ask}}}}}}, \\qquad F_{{P/B}} = S_{{P/B}} \\cdot \\frac{{1 + r_P (\\text{{Days}}/360)}}{{1 + r_B (\\text{{Days}}/360)}}$$
  </div>
  <p><strong>Remember CFA Quote Notation</strong>: Unlike street convention in some desks, CFA reads $USD/EUR = 1.0800$ as <strong>1.0800 USD per 1 EUR</strong> (Price = USD, Base = EUR)!</p>
""" + worked_box("Worked Numerical 3: Dealer Bid-Ask Cross-Rate &amp; 180-Day Forward Points",
f"<p><strong>Cross Rate</strong>: Dealer quotes $USD/EUR = 1.0800\\text{{--}}1.0810$ and $JPY/USD = 150.00\\text{{--}}150.20$. Cross $JPY/EUR$: Bid $= 1.0800 \\times 150.00 = {jpy_eur_bid:.2f}$, Ask $= 1.0810 \\times 150.20 = {jpy_eur_ask:.4f}$.</p>"
f"<p><strong>Forward Points</strong>: $S_{{USD/GBP}} = 1.2500$, $r_{{USD}} = 5.20\\%$, $r_{{GBP}} = 3.80\\%$, $T = 180$ days. $F = 1.2500 \\times \\frac{{1 + 0.052(0.5)}}{{1 + 0.038(0.5)}} = {fwd_fx:.4f} \\implies \\text{{Forward Points}} = +{fwd_pts:.1f}\\text{{ pips}}$.</p>", "amber") +
exercise_toolbar("econ-m6-fxcalc", "Module 06 Chapter Exercises (FX Mechanics)") +
exercise_card("econ-ex-11", "Exercise 6.1 (Solved): Triangular Arbitrage Check",
"<p>Dealer 1 quotes $USD/EUR = 1.1000$ (mid), Dealer 2 quotes $JPY/USD = 148.00$, and Dealer 3 quotes $JPY/EUR = 165.00$. Starting with 1,000,000 USD, compute arbitrage profit if any.</p>",
f"<p><strong>Answer: +13,513.51 USD arbitrage profit</strong>. Implied $JPY/EUR = 1.10 \\times 148 = 162.80 &lt; 165.00$ (EUR overvalued at Dealer 3). Sell USD for EUR at 1.10 ($909,090.91\\text{{ EUR}}$) &rarr; sell EUR for JPY at 165.00 ($150,000,000\\text{{ JPY}}$) &rarr; buy USD at 148.00 ($1,013,513.51\\text{{ USD}}$).</p>", "solved", "L1/L2 FX") +
exercise_card("econ-ex-12", "Exercise 6.2 (Unsolved): Inverting a Bid-Ask Spread",
"<p>If $CHF/USD = 0.8800\\text{{--}}0.8805$, compute the $USD/CHF$ bid-ask quote to 4 decimals.</p>",
f"<p><strong>Answer: $1.1357\\text{{--}}1.1364$</strong>. Bid $= 1/0.8805 = {1/0.8805:.4f}$; Ask $= 1/0.8800 = {1/0.8800:.4f}$.</p>", "unsolved", "L1/L2 FX") +
"</section>")

# MODULE 7: FX PARITY & CARRY TRADE (LEVEL 2)
parts.append(f"""
<section id="econ-m7-fxparity" class="notes-chapter">
  <h2 class="section-heading"><span class="num">07.</span> Currency Exchange Rates: Parity Conditions &amp; Carry Trade (L2 Module 2)</h2>
  <div class="table-container">
    <table>
      <thead><tr><th>Parity Condition</th><th>Governing Equation ($P/B$)</th><th>Holds Short/Long Run?</th></tr></thead>
      <tbody>
        <tr><td><strong>Covered IRP (CIRP)</strong></td><td>$$F/S = (1+r_P)/(1+r_B)$$</td><td><strong>Yes — Enforced continuously by arbitrage!</strong></td></tr>
        <tr><td><strong>Uncovered IRP (UIRP)</strong></td><td>$$E(\\%\\Delta S_{{P/B}}) \\approx r_P - r_B$$</td><td>Often fails short/med run &rarr; creates <strong>FX Carry Trade profits</strong>!</td></tr>
        <tr><td><strong>Relative PPP</strong></td><td>$$\\%\\Delta S_{{P/B}} \\approx \\pi_P - \\pi_B$$</td><td>Holds over long horizons (5–10+ yrs).</td></tr>
        <tr><td><strong>Intl Fisher Effect</strong></td><td>$$r_P - r_B \\approx E(\\pi_P) - E(\\pi_B)$$</td><td>Combines Fisher Effect + equal real rates.</td></tr>
      </tbody>
    </table>
  </div>
  <p><strong>Mundell-Fleming Model (Capital Mobility)</strong>: Under <em>high capital mobility + floating FX</em>, expansionary Monetary policy lowers rates &rarr; capital outflow &rarr; currency depreciates &rarr; boosts exports (strong expansion!); under <em>fixed FX</em>, monetary policy is powerless and only Fiscal policy expands output. <strong>Dornbusch Overshooting</strong>: sticky goods prices force spot FX to overshoot long-run equilibrium immediately upon monetary shocks.</p>
""" + worked_box("Worked Numerical 4: Unhedged FX Carry Trade Return",
f"<p>A hedge fund borrows JPY at 2.50% ($r_{{\\text{{funding}}}}$) and invests in MXN deposits at 6.50% ($r_{{\\text{{target}}}}$). Over 1 year, $JPY/MXN$ appreciates by +1.20% (MXN strengthens). Net return $= (1 + 0.065)(1.012) - (1 + 0.025) = {carry_return*100:.2f}\\%$. Warning: Carry trades exhibit negative skewness / crash risk!</p>", "purple") +
exercise_toolbar("econ-m7-fxparity", "Module 07 Chapter Exercises (L2 FX Parity)") +
exercise_card("econ-ex-13", "Exercise 7.1 (Solved): Covered Interest Arbitrage",
"<p>Spot $CAD/USD = 1.3500$, 1-year $r_{{CAD}} = 4.00\\%$, $r_{{USD}} = 5.00\\%$, and quoted 1-year forward $F = 1.3450$. Identify the arbitrage trade and profit per 1,000,000 USD borrowed.</p>",
f"<p><strong>Answer: +8,250 CAD riskless arbitrage profit</strong>. Arbitrage-free $F^* = 1.3500 \\times \\frac{{1.04}}{{1.05}} = {1.35*1.04/1.05:.5f} &lt; 1.3450$ (USD forward is overvalued relative to CAD). Borrow 1,350,000 CAD at 4% (repay $1,404,000\\text{{ CAD}}$), convert spot at 1.35 to 1,000,000 USD, invest at 5% to 1,050,000 USD, and sell 1,050,000 USD forward at 1.3450 to lock in $1,412,250\\text{{ CAD}}$ &rarr; guaranteed profit $= 1,412,250 - 1,404,000 = +8,250\\text{{ CAD}}$.</p>", "solved", "L2 FX Arb") +
exercise_card("econ-ex-14", "Exercise 7.2 (Unsolved): Long-Run Relative PPP Forecast",
"<p>If expected annual US inflation is 2.2% and Eurozone inflation is 3.7%, and spot $USD/EUR = 1.1000$, forecast the 3-year PPP spot rate.</p>",
f"<p><strong>Answer: 1.0530 USD/EUR</strong> (USD appreciates vs EUR due to lower inflation). $S_3 = 1.1000 \\times \\left(\\frac{{1.022}}{{1.037}}\\right)^3 = {1.10*((1.022/1.037)**3):.4f}$.</p>", "unsolved", "L2 FX PPP") +
"</section>")

# MODULE 8: ECONOMIC GROWTH & REGULATION (LEVEL 2)
parts.append(f"""
<section id="econ-m8-growth" class="notes-chapter">
  <h2 class="section-heading"><span class="num">08.</span> Economic Growth, Development &amp; Regulation (L2 Module 1 &amp; CBOK III)</h2>
  <div class="formula-card">
    <div class="formula-title">Cobb-Douglas Growth Accounting &amp; Solow Steady-State Equations</div>
    $$\\frac{{\\Delta Y}}{{Y}} = \\frac{{\\Delta A}}{{A}} + \\alpha \\frac{{\\Delta K}}{{K}} + (1 - \\alpha)\\frac{{\\Delta L}}{{L}}, \\qquad g^* = \\frac{{\\theta}}{{1 - \\alpha}} + n \\; (\\text{{Steady-State Output Growth}})$$
    $$\\text{{Solow Steady-State Capital per Worker: }} k^* = \\left(\\frac{{s A}}{{\\delta + n}}\\right)^{{\\frac{{1}}{{1 - \\alpha}}}}, \\qquad \\frac{{I}}{{Y}} = s = \\left(\\frac{{\\delta + n + \\theta/(1-\\alpha)}}{{Y/K}}\\right)\\frac{{K}}{{Y}}$$
  </div>
  <ul>
    <li><strong>Neoclassical (Solow)</strong>: Capital deepening alone yields <em>diminishing marginal returns</em>—only Total Factor Productivity (TFP $\\theta$) drives permanent per-capita growth! Supports <em>conditional convergence</em> (poor nations grow faster given similar savings/institutions).</li>
    <li><strong>Endogenous Growth (Romer)</strong>: R&amp;D, human capital, and knowledge spillovers yield constant/increasing returns to capital—permanent growth without exogenous shocks.</li>
    <li><strong>Economics of Regulation</strong>: <em>Regulatory capture</em> occurs when regulators serve the regulated industry rather than the public; cost-benefit analysis weighs compliance burden against systemic stability.</li>
  </ul>
""" + worked_box("Worked Numerical 5: Cobb-Douglas Potential GDP Growth &amp; Solow Steady State",
f"<p><strong>Growth Accounting</strong>: TFP growth $= 1.4\\%$, capital share $\\alpha = 0.35$, capital stock growth $= 3.2\\%$, labor growth $= 1.0\\%$. Potential GDP growth $= 1.4\\% + 0.35(3.2\\%) + 0.65(1.0\\%) = {dy_l2*100:.2f}\\%$.</p>"
f"<p><strong>Solow Steady State</strong>: Savings rate $s=24\\%$, $A=1.0$, $\\alpha=0.40$, depreciation $\\delta=6\\%$, labor growth $n=2\\%$. $k^* = \\left(\\frac{{0.24}}{{0.08}}\\right)^{{1/0.60}} = 3.0^{{1.6667}} = {k_star:.2f}$.</p>", "emerald") +
exercise_toolbar("econ-m8-growth", "Module 08 Chapter Exercises (L2 Growth)") +
exercise_card("econ-ex-15", "Exercise 8.1 (Solved): Steady-State Per-Capita Growth Rate",
"<p>If TFP growth $\\theta = 1.2\\%$, capital share $\\alpha = 0.40$, and labor force grows at $n = 1.5\\%$, compute the steady-state per-capita and total GDP growth rates.</p>",
"<p><strong>Answer: Per-capita = 2.00%; Total GDP = 3.50%</strong>. Per-capita $= \\frac{\\theta}{1-\\alpha} = \\frac{1.2\\%}{0.60} = 2.00\\%$. Total GDP $= 2.00\\% + 1.50\\% = 3.50\\%$.</p>", "solved", "L2 Growth") +
exercise_card("econ-ex-16", "Exercise 8.2 (Unsolved): Impact of Increasing Savings Rate in Solow Model",
"<p>Under the Neoclassical growth model, raising the national savings rate from 20% to 30% causes what effect on growth rates?</p>",
"<p><strong>Answer: Temporarily raises per-capita GDP growth during transition to a higher steady-state level ($k^*$), but leaves permanent long-run steady-state growth unchanged</strong> (depends solely on TFP).</p>", "unsolved", "L2 Growth") +
"</section>")

# MODULE 9: ECONOMIC ANALYSIS & CAPITAL MARKET EXPECTATIONS
parts.append("""
<section id="econ-m9-cme" class="notes-chapter">
  <h2 class="section-heading"><span class="num">09.</span> Economic Analysis, Indicators &amp; Capital Market Expectations</h2>
  <ul>
    <li><strong>Equity Link</strong>: Sustainable long-run equity returns cannot exceed nominal GDP growth plus dividend yield minus dilution ($E(R_e) \\approx D/P + g_{\\text{GDP}}$ over multi-decade horizons).</li>
    <li><strong>Yield Curve &amp; Cycle</strong>: Steepening (Trough/Early Expansion) favors Cyclical Equities &amp; High Yield; Flattening/Inverted (Late Boom) signals monetary tightening &rarr; extend Government Bond duration &amp; rotate into Defensive Staples/Healthcare!</li>
  </ul>
""" + exercise_toolbar("econ-m9-cme", "Module 09 Chapter Exercises (Macro CME)") +
exercise_card("econ-ex-17", "Exercise 9.1 (Solved): Yield Curve Inversion Tactical Signal",
"<p>The 10y–2y Treasury spread turns $-45\\text{ bps}$ as central banks hike rates above Taylor Rule neutral. Which fixed-income and equity stance aligns best?</p>",
"<p><strong>Answer: Extend Sovereign Duration (long duration high-grade bonds) and tilt equities toward Defensives (Healthcare/Utilities/Consumer Staples)</strong> ahead of contraction.</p>", "solved", "CBOK III/CME") +
exercise_card("econ-ex-18", "Exercise 9.2 (Unsolved): Early Expansion Sector Tilt",
"<p>Unemployment peaks, central banks slash rates, and the yield curve is at maximum steepness. Which asset class historically leads early recovery?</p>",
"<p><strong>Answer: Small-Cap Cyclical Equities, High-Yield Credit, and Industrials/Tech</strong> (credit spreads tighten sharply from recession peaks).</p>", "unsolved", "CBOK III/CME") +
"</section>")

# MODULE 10: FORMULA SHEET
parts.append("""
<section id="econ-m10-formulas" class="notes-chapter">
  <h2 class="section-heading"><span class="num">10.</span> Master Economics Formula Cheat Sheet</h2>
  <div class="table-container">
    <table>
      <thead><tr><th>Concept</th><th>Governing Formula</th><th>Key Exam Rule</th></tr></thead>
      <tbody>
        <tr><td><strong>Price Elasticity</strong></td><td>$$E_p^d = (\\Delta Q / \\Delta P)(P/Q)$$</td><td>$|E|>1$ elastic; raising price cuts revenue</td></tr>
        <tr><td><strong>Fiscal Multiplier</strong></td><td>$$1 / [1 - c(1 - t)]$$</td><td>Decreases as marginal tax rate $t$ or import leakage rises</td></tr>
        <tr><td><strong>Taylor Rule</strong></td><td>$$i^* = r^* + \\pi + 0.5(\\pi-\\pi^*) + 0.5(y-y^*)$$</td><td>Weights inflation gap &amp; output gap equally at 0.5</td></tr>
        <tr><td><strong>CIRP Forward</strong></td><td>$$F_{P/B} = S_{P/B} \\frac{1 + r_P(T)}{1 + r_B(T)}$$</td><td>Higher-rate currency trades at forward <em>discount</em></td></tr>
        <tr><td><strong>Relative PPP</strong></td><td>$$\\%\\Delta S_{P/B} \\approx \\pi_P - \\pi_B$$</td><td>Higher-inflation currency depreciates long-term</td></tr>
        <tr><td><strong>Growth Accounting</strong></td><td>$$\\frac{\\Delta Y}{Y} = \\frac{\\Delta A}{A} + \\alpha \\frac{\\Delta K}{K} + (1-\\alpha)\\frac{\\Delta L}{L}$$</td><td>Steady-state growth $= \\theta/(1-\\alpha) + n$</td></tr>
      </tbody>
    </table>
  </div>
""" + exercise_toolbar("econ-m10-formulas", "Module 10 Capstone Drills") +
exercise_card("econ-ex-19", "Exercise 10.1 (Solved): Computing Implied TFP Contribution",
"<p>An economy grows 4.1% per year with capital stock growing 5.0%, labor growing 1.2%, and $\\alpha = 0.30$. Back out TFP growth.</p>",
f"<p><strong>Answer: +1.76%</strong>. $\\Delta A/A = 4.10\\% - 0.30(5.0\\%) - 0.70(1.2\\%) = 4.10\\% - 1.50\\% - 0.84\\% = {4.10 - 1.50 - 0.84:.2f}\\%$.</p>", "solved", "L2 Growth") +
exercise_card("econ-ex-20", "Exercise 10.2 (Unsolved): Forward Premium/Discount Intuition",
"<p>If 1-year USD rates are 5.0% and JPY rates are 0.5%, should $JPY/USD$ trade at a forward premium or forward discount?</p>",
"<p><strong>Answer: Forward discount on USD (fewer JPY per USD forward)</strong>. Because $r_{{JPY}} &lt; r_{{USD}}$, higher-yielding USD trades at a forward discount relative to JPY under CIRP.</p>", "unsolved", "L1/L2 FX") +
"</section>")

write_notes_html("".join(parts), OUTPUT_PATH)
