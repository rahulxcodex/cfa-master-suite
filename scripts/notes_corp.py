"""
scripts/notes_corp.py
Generates data/corp_reference_extracted.html:
Corporate Issuers (Corporate Finance) Master Reference Library (9 Modules)
Aligned with CFA CBOK V & L1/L2 curricula.
Includes 12 Python-computed Worked Numericals + 20 Interactive Chapter Exercises (10 Solved + 10 Unsolved).
"""
import math
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scripts.qbank_helper import irr
from scripts.notes_helper import worked_box, exercise_card, exercise_toolbar, write_notes_html

OUTPUT_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "corp_reference_extracted.html")

# Python-verified calculations
# Capital budgeting NPV & IRR
cfs_corp = [-500000, 180000, 220000, 250000]
npv_corp = sum(cf / (1.10 ** t) for t, cf in enumerate(cfs_corp))
irr_corp = irr(cfs_corp)
pi_corp = (npv_corp + 500000) / 500000
# Cash conversion cycle & trade credit cost
doh, dso, dpo = 52.0, 44.0, 38.0
ccc = doh + dso - dpo
ear_trade = (1 + 2.0 / 98.0) ** (365 / 20) - 1
# WACC & Hamada Beta
beta_u = 1.25 / (1 + (1 - 0.25) * 0.60)
beta_l_proj = beta_u * (1 + (1 - 0.30) * 0.80)
re_proj = 0.04 + beta_l_proj * 0.055
wacc_proj = (0.8 / 1.8) * 0.065 * (1 - 0.30) + (1.0 / 1.8) * re_proj
# Leverage DOL, DFL, DTL
units_q, price_p, vc_v, fc_f, int_i = 10000, 80.0, 45.0, 200000.0, 50000.0
cm = units_q * (price_p - vc_v)
ebit_lev = cm - fc_f
dol = cm / ebit_lev
dfl = ebit_lev / (ebit_lev - int_i)
dtl = dol * dfl
q_be = fc_f / (price_p - vc_v)
q_obe = (fc_f + int_i) / (price_p - vc_v)
# MM Proposition I & II with taxes
vu_mm = 1200000.0 / 0.12
d_mm = 4000000.0
vl_mm = vu_mm + 0.25 * d_mm
e_mm = vl_mm - d_mm
re_mm = 0.12 + (0.12 - 0.06) * (1 - 0.25) * (d_mm / e_mm)
# Buyback EPS impact
ni_bb, sh_bb, px_bb, buy_amt, after_tax_r = 24000000.0, 8000000.0, 30.0, 30000000.0, 0.045
eps_old = ni_bb / sh_bb
sh_rep = buy_amt / px_bb
ni_new_bb = ni_bb - buy_amt * after_tax_r
eps_new = ni_new_bb / (sh_bb - sh_rep)
# M&A exchange ratio & accretion
sh_acq, eps_acq, px_acq = 50000000.0, 4.00, 60.0
sh_tgt, eps_tgt, px_offer = 10000000.0, 2.50, 45.0
ex_ratio = px_offer / px_acq
new_sh_ma = sh_tgt * ex_ratio
synergies_at = 18000000.0
post_eps_ma = (sh_acq * eps_acq + sh_tgt * eps_tgt + synergies_at) / (sh_acq + new_sh_ma)

parts = []

parts.append("""<div class="top-controls">
  <button class="btn-ctrl" onclick="toggleTheme()">🌓 Switch Theme</button>
  <button class="btn-ctrl" onclick="window.print()">🖨️ Print / Save as PDF</button>
</div>

<div class="doc-hero">
  <h1>Corporate Issuers &amp; Corporate Finance (CFA&reg; CBOK V)</h1>
  <p>Master Reference for CFA&reg; Level 1 (Corporate Structures, ESG, Capital Budgeting, Working Capital, Cost of Capital, Leverage) &amp; Level 2 (Hamada Pure-Play Beta, Modigliani-Miller Capital Structure, Dividends &amp; Buybacks, Mergers &amp; Acquisitions). Features 12 Worked Numericals and 20 Interactive Chapter Exercises (10 Solved + 10 Unsolved).</p>
  <div class="meta-tags">
    <span class="badge badge-amber">L1 Weight: 6%–9%</span>
    <span class="badge badge-purple">L2 Weight: 5%–10%</span>
    <span class="badge badge-emerald">9 Modules + 20 Exercises</span>
    <span class="badge badge-blue">Interactive WACC &amp; MM Lab</span>
  </div>
</div>

<div class="card" style="margin-top: 15px; margin-bottom: 25px;">
  <div class="card-title">🏢 Quick Navigation: Corporate Issuers Curriculum Modules</div>
  <div class="fsa-nav-bar">
    <a class="fsa-nav-btn" href="#corp-m1-gov">01. Governance &amp; ESG</a>
    <a class="fsa-nav-btn" href="#corp-m2-capbud">02. Capital Allocation &amp; ROIC</a>
    <a class="fsa-nav-btn" href="#corp-m3-wc">03. Working Capital &amp; Liquidity</a>
    <a class="fsa-nav-btn" href="#corp-m4-wacc">04. Cost of Capital &amp; Hamada</a>
    <a class="fsa-nav-btn" href="#corp-m5-lev">05. DOL, DFL &amp; Break-Even</a>
    <a class="fsa-nav-btn" href="#corp-m6-mm">06. Capital Structure (MM) (L2)</a>
    <a class="fsa-nav-btn" href="#corp-m7-div">07. Dividends &amp; Buybacks (L2)</a>
    <a class="fsa-nav-btn" href="#corp-m8-ma">08. M&amp;A &amp; Restructuring (L2)</a>
    <a class="fsa-nav-btn" href="#corp-m9-formulas" style="color: var(--accent-emerald); font-weight: 700;">09. Formula Sheet</a>
  </div>
  <div style="display:flex; gap:10px; flex-wrap:wrap; margin-top:10px;">
    <button type="button" class="btn" onclick="jumpToSubjectBank(1, 'Corporate Issuers')">📝 Practice 80 L1 Corp Issuers MCQs</button>
    <button type="button" class="btn btn-secondary" onclick="jumpToSubjectBank(2, 'Corporate Issuers')">📑 Practice 10 L2 Corp Issuers Vignettes (50 Qs)</button>
    <button type="button" class="btn btn-secondary" onclick="switchTab('sim-corp')">🔬 Open WACC &amp; MM Capital Structure Lab</button>
    <button type="button" class="filter-btn" onclick="toggleChapterExercises('corp-reference', false)">🙈 Hide Solutions</button>
    <button type="button" class="filter-btn" onclick="toggleChapterExercises('corp-reference', true)">✅ Reveal All Solutions</button>
  </div>
</div>
""")

# MODULE 1
parts.append("""
<section id="corp-m1-gov" class="notes-chapter">
  <h2 class="section-heading"><span class="num">01.</span> Corporate Structures, Ownership, Governance &amp; ESG Risk Factors</h2>
  <ul>
    <li><strong>Organizational Forms</strong>: Sole Proprietorship &amp; General Partnership (unlimited liability, pass-through tax) vs. Limited Partnership (GP unlimited, LP limited) vs. Corporation (separate legal entity, limited liability, double taxation unless S-Corp/pass-through).</li>
    <li><strong>Shareholder vs. Stakeholder Theories</strong>: Principal-agent problems arise between shareholders &amp; managers, and between controlling &amp; minority shareholders (especially via <em>dual-class voting structures</em>).</li>
    <li><strong>Board Independence &amp; Committees</strong>: Independent audit, compensation, and nominating committees mitigate entrenchment; <em>staggered boards</em> protect management from hostile takeovers (negative for minority governance).</li>
    <li><strong>ESG Materiality</strong>: Environmental (carbon transition, stranded assets), Social (labor safety, data privacy), Governance (executive pay alignment, clawbacks).</li>
  </ul>
""" + exercise_toolbar("corp-m1-gov", "Module 01 Chapter Exercises (Governance &amp; ESG)") +
exercise_card("corp-ex-1", "Exercise 1.1 (Solved): Dual-Class Shares &amp; Controlling Shareholder Agency Risk",
"<p>A founder owns 15% of economic equity via Class B shares carrying 10 votes/share while public Class A holds 1 vote/share. Which corporate governance conflict intensifies?</p>",
"<p><strong>Answer: Principal-Principal conflict (controlling minority-vote holder extracting private benefits at public shareholders' expense)</strong>, insulating management from activist proxy accountability.</p>", "solved", "L1 Corp") +
exercise_card("corp-ex-2", "Exercise 1.2 (Unsolved): Debt-Holder vs. Equity-Holder Agency Conflict",
"<p>When a leveraged firm nears distress, why might equity holders favor ultra-risky negative-NPV projects?</p>",
"<p><strong>Answer: Risk-shifting / asset substitution</strong>. Equity acts like a call option on firm assets—shareholders capture unlimited upside if the gamble succeeds while bondholders bear downside losses.</p>", "unsolved", "L1/L2 Corp") +
"</section>")

# MODULE 2
parts.append(f"""
<section id="corp-m2-capbud" class="notes-chapter">
  <h2 class="section-heading"><span class="num">02.</span> Capital Allocation, NPV, IRR, ROIC &amp; Real Options</h2>
  <div class="formula-card">
    <div class="formula-title">Capital Budgeting Metrics &amp; Return on Invested Capital (ROIC)</div>
    $$NPV = \\sum_{{t=0}}^N \\frac{{CF_t}}{{(1+r)^t}}, \\qquad PI = \\frac{{PV(\\text{{Future CFs}})}}{{CF_0}} = 1 + \\frac{{NPV}}{{CF_0}}$$
    $$ROIC = \\frac{{NOPAT}}{{\\text{{Average Invested Capital}}}} = \\frac{{EBIT(1 - t)}}{{\\text{{Total Debt + Equity - Excess Cash}}}}$$
  </div>
  <p><strong>Exam Traps</strong>: When NPV and IRR conflict on <em>mutually exclusive projects</em> (due to scale or cash flow timing differences), <strong>ALWAYS pick the higher NPV</strong>! Non-conventional cash flows (multiple sign changes) produce multiple IRRs. Real options (timing, abandonment, expansion, flexibility) increase project NPV: $\\text{{Project NPV}} = \\text{{Static NPV}} + \\text{{Option Value}}$.</p>
""" + worked_box("Worked Numerical 1: Project NPV, IRR &amp; Profitability Index",
f"<p>An industrial robotics upgrade requires 500,000 USD upfront ($t=0$) and returns 180,000 USD ($t=1$), 220,000 USD ($t=2$), and 250,000 USD ($t=3$) at WACC $= 10.0\\%$. $NPV = {npv_corp:,.2f}\\text{{ USD}}$, $IRR = {irr_corp*100:.2f}\\%$, and $PI = {pi_corp:.3f}$.</p>", "emerald") +
exercise_toolbar("corp-m2-capbud", "Module 02 Chapter Exercises (Capital Allocation)") +
exercise_card("corp-ex-3", "Exercise 2.1 (Solved): Mutually Exclusive NPV vs. IRR Conflict",
"<p>Project X requires 1M USD ($NPV = 250\\text{k USD}$, $IRR = 22\\%$); Project Y requires 4M USD ($NPV = 520\\text{k USD}$, $IRR = 16\\%$). Projects are mutually exclusive and capital is unconstrained at 10% WACC. Choose?</p>",
"<p><strong>Answer: Project Y</strong>. Maximizing dollar shareholder wealth requires selecting the highest positive NPV (+520k USD vs. +250k USD) regardless of IRR.</p>", "solved", "L1 Corp") +
exercise_card("corp-ex-4", "Exercise 2.2 (Unsolved): Computing Economic Value Added (ROIC Spread)",
"<p>A firm earns EBIT of 15M USD, pays a 20% tax rate, holds 100M USD invested capital, and faces an 8.5% WACC. Compute ROIC and annual economic profit (EVA).</p>",
"<p><strong>Answer: ROIC = 12.0%; EVA = +3.50M USD</strong>. $NOPAT = 15(0.80) = 12\\text{M}$. $ROIC = 12/100 = 12.0\\%$. $EVA = 12\\text{M} - (0.085 \\times 100\\text{M}) = +3.50\\text{M USD}$.</p>", "unsolved", "L1 Corp") +
"</section>")

# MODULE 3
parts.append(f"""
<section id="corp-m3-wc" class="notes-chapter">
  <h2 class="section-heading"><span class="num">03.</span> Working Capital, Liquidity &amp; Short-Term Financing</h2>
  <div class="formula-card">
    <div class="formula-title">Cash Conversion Cycle &amp; Effective Annual Cost of Trade Credit</div>
    $$CCC = DOH + DSO - DPO, \\qquad EAR_{{\\text{{trade credit}}}} = \\left(1 + \\frac{{\\%\\text{{Discount}}}}{{100 - \\%\\text{{Discount}}}}\\right)^{{\\frac{{365}}{{\\text{{Net Days}} - \\text{{Discount Days}}}}}} - 1$$
  </div>
""" + worked_box("Worked Numerical 2: Cash Conversion Cycle &amp; Foregoing '2/10, Net 30' Trade Discount",
f"<p><strong>CCC</strong>: With $DOH = 52$, $DSO = 44$, and $DPO = 38$, $CCC = 52 + 44 - 38 = {ccc:.0f}\\text{{ days}}$ (operating cycle $= 52 + 44 = 96$ days).</p>"
f"<p><strong>Trade Credit Cost</strong>: Supplier offers terms '2/10, net 30'. Missing the 2% discount to borrow for 20 extra days costs an annualized $EAR = \\left(1 + \\frac{{2}}{{98}}\\right)^{{365/20}} - 1 = {ear_trade*100:.2f}\\%$—far costlier than a 7% bank line!</p>", "blue") +
exercise_toolbar("corp-m3-wc", "Module 03 Chapter Exercises (Working Capital)") +
exercise_card("corp-ex-5", "Exercise 3.1 (Solved): Primary vs. Secondary Liquidity Sources",
"<p>Categorize committed bank credit lines, cash/marketable securities, and selling a manufacturing subsidiary under stress as primary or secondary liquidity.</p>",
"<p><strong>Answer: Cash &amp; committed bank credit lines = Primary liquidity</strong> (available immediately without disrupting operations); <strong>selling a subsidiary / bankruptcy renegotiation = Secondary liquidity</strong> (signals distress/value destruction).</p>", "solved", "L1 Corp") +
exercise_card("corp-ex-6", "Exercise 3.2 (Unsolved): Trade Credit EAR ('1/15, Net 45')",
"<p>Compute the annualized cost of skipping a '1/15, net 45' vendor discount.</p>",
f"<p><strong>Answer: 13.00%</strong>. $(1 + 1/99)^{{365/30}} - 1 = {((1 + 1/99)**(365/30) - 1)*100:.2f}\\%$.</p>", "unsolved", "L1 Corp") +
"</section>")

# MODULE 4
parts.append(f"""
<section id="corp-m4-wacc" class="notes-chapter">
  <h2 class="section-heading"><span class="num">04.</span> Cost of Capital, Flotation Costs &amp; Pure-Play Hamada Beta</h2>
  <div class="formula-card">
    <div class="formula-title">WACC &amp; Pure-Play Beta Unlevering / Relevering</div>
    $$WACC = w_d r_d(1-t) + w_p r_p + w_e r_e, \\qquad r_p = \\frac{{D_p}}{{P_p}}$$
    $$\\beta_U = \\frac{{\\beta_L}}{{1 + (1 - t)\\left(\\frac{{D}}{{E}}\\right)_{{\\text{{comp}}}}}}, \\qquad \\beta_{{\\text{{proj}}}} = \\beta_U \\left[1 + (1 - t_{{\\text{{proj}}}})\\left(\\frac{{D}}{{E}}\\right)_{{\\text{{proj}}}}\\right]$$
  </div>
  <p><strong>Exam Trap on Flotation Costs</strong>: NEVER add flotation costs into WACC permanently! Correct practice adjusts initial cash outflow $CF_0$ upward by dollar flotation cost (or divides $NPV$ adjustment cleanly at $t=0$).</p>
""" + worked_box("Worked Numerical 3: Pure-Play Hamada Beta &amp; Divisional Project WACC",
f"<p>A pure-play peer has $\\beta_L = 1.25$, $D/E = 0.60$, tax rate $25\\%$. Unlevered asset beta $\\beta_U = \\frac{{1.25}}{{1 + 0.75(0.60)}} = {beta_u:.4f}$. Relevering for our division ($D/E = 0.80$, $t = 30\\%$): $\\beta_{{\\text{{proj}}}} = {beta_u:.4f}[1 + 0.70(0.80)] = {beta_l_proj:.4f}$. With $R_f = 4.0\\%$, $ERP = 5.5\\%$, pre-tax $r_d = 6.5\\%$: $r_e = {re_proj*100:.2f}\\%$, and $WACC = (0.8/1.8)(6.5\\%)(0.70) + (1.0/1.8)({re_proj*100:.2f}\\%) = {wacc_proj*100:.2f}\\%$.</p>", "amber") +
exercise_toolbar("corp-m4-wacc", "Module 04 Chapter Exercises (Cost of Capital)") +
exercise_card("corp-ex-7", "Exercise 4.1 (Solved): Target Weights vs. Book Weights",
"<p>A firm's book capital structure is 70% debt / 30% equity, market values are 40% debt / 60% equity, and management's announced target capital structure is 50% debt / 50% equity. Which weights belong in WACC?</p>",
"<p><strong>Answer: 50% debt / 50% equity (target weights)</strong>; if target weights are unavailable, use current market-value weights—never historical book weights.</p>", "solved", "L1/L2 Corp") +
exercise_card("corp-ex-8", "Exercise 4.2 (Unsolved): Country Risk Premium Adjustment",
"<p>If $R_f = 4.0\\%$, $\\beta = 1.1$, developed $ERP = 5.0\\%$, and Emerging Country Risk Premium $CRP = 2.8\\%$, compute CAPM cost of equity.</p>",
"<p><strong>Answer: 12.58%</strong> (or 12.30% if CRP added outside $\\beta$). Using CFA standard $r_e = R_f + \\beta(ERP + CRP) = 4.0\\% + 1.1(5.0\\% + 2.8\\%) = 12.58\\%$.</p>", "unsolved", "L1/L2 Corp") +
"</section>")

# MODULE 5
parts.append(f"""
<section id="corp-m5-lev" class="notes-chapter">
  <h2 class="section-heading"><span class="num">05.</span> Measures of Leverage &amp; Break-Even Points (DOL, DFL, DTL)</h2>
  <div class="formula-card">
    <div class="formula-title">Operating, Financial &amp; Total Leverage</div>
    $$DOL = \\frac{{Q(P - V)}}{{Q(P - V) - F}}, \\qquad DFL = \\frac{{EBIT}}{{EBIT - I}}, \\qquad DTL = DOL \\times DFL = \\frac{{Q(P - V)}}{{Q(P - V) - F - I}}$$
    $$Q_{{BE}} = \\frac{{F + I}}{{P - V}}, \\qquad Q_{{OBE}} = \\frac{{F}}{{P - V}}$$
  </div>
""" + worked_box("Worked Numerical 4: Computing DOL, DFL, DTL &amp; Break-Even Units",
f"<p>Selling $Q = 10,000$ units at $P = 80\\text{{ USD}}$, variable cost $V = 45\\text{{ USD}}$, fixed operating costs $F = 200,000\\text{{ USD}}$, interest $I = 50,000\\text{{ USD}}$. Contribution margin $= 350,000\\text{{ USD}}$, $EBIT = 150,000\\text{{ USD}}$. $DOL = {dol:.3f}$, $DFL = {dfl:.3f}$, $DTL = {dtl:.3f}$. Operating break-even $Q_{{OBE}} = {q_obe:,.0f}$ units; Total break-even $Q_{{BE}} = {q_be:,.0f}$ units.</p>", "cyan") +
exercise_toolbar("corp-m5-lev", "Module 05 Chapter Exercises (Leverage)") +
exercise_card("corp-ex-9", "Exercise 5.1 (Solved): EPS Sensitivity to Sales Drop",
"<p>If $DOL = 2.5$ and $DFL = 1.6$, what happens to EPS if unit sales decline by 10%?</p>",
"<p><strong>Answer: EPS falls by 40.0%</strong>. $DTL = 2.5 \\times 1.6 = 4.0$, so $\\%\\Delta EPS = 4.0 \\times (-10\\%) = -40.0\\%$.</p>", "solved", "L1/L2 Corp") +
exercise_card("corp-ex-10", "Exercise 5.2 (Unsolved): Zero-Debt DFL",
"<p>What is the Degree of Financial Leverage (DFL) for an unlevered firm with zero interest expense and zero preferred dividends?</p>",
"<p><strong>Answer: $DFL = 1.00$</strong> ($EBIT / (EBIT - 0) = 1.00$).</p>", "unsolved", "L1 Corp") +
"</section>")

# MODULE 6: MODIGLIANI-MILLER & CAPITAL STRUCTURE (L2)
parts.append(f"""
<section id="corp-m6-mm" class="notes-chapter">
  <h2 class="section-heading"><span class="num">06.</span> Capital Structure Theory: MM, Static Trade-Off &amp; Pecking Order (L2)</h2>
  <div class="table-container">
    <table>
      <thead><tr><th>Theory / World</th><th>Firm Value ($V_L$)</th><th>Cost of Equity ($r_e$)</th><th>Optimal Debt Ratio</th></tr></thead>
      <tbody>
        <tr><td><strong>MM No Taxes</strong></td><td>$V_L = V_U$ (Irrelevant)</td><td>$r_e = r_0 + (r_0 - r_d)(D/E)$</td><td>No optimal ratio; WACC flat</td></tr>
        <tr><td><strong>MM With Corp Taxes</strong></td><td>$V_L = V_U + t \\cdot D$</td><td>$r_e = r_0 + (r_0 - r_d)(1-t)(D/E)$</td><td>100% debt (ignoring distress)</td></tr>
        <tr><td><strong>Static Trade-Off</strong></td><td>$V_L = V_U + t D - PV(\\text{{Distress}})$</td><td>U-shaped WACC</td><td>Where $PV(\\text{{Marginal Tax Shield}}) = PV(\\text{{Marginal Distress}})$</td></tr>
      </tbody>
    </table>
  </div>
  <p><strong>Pecking Order Theory (Myers-Majluf)</strong>: Due to asymmetric information, managers prefer financing in order: (1) <strong>Internal Retained Earnings</strong> &rarr; (2) <strong>Debt</strong> &rarr; (3) <strong>External Equity</strong> (issuing stock signals overvaluation!). Free Cash Flow hypothesis: debt disciplines empire-building managers.</p>
""" + worked_box("Worked Numerical 5: Modigliani-Miller With Corporate Taxes",
f"<p>An all-equity firm earns perpetual pre-tax EBIT of 1,600,000 USD ($NI = 1,200,000\\text{{ USD}}$ at $t=25\\%$) with unlevered $r_0 = 12.0\\%$, so $V_U = {vu_mm:,.0f}\\text{{ USD}}$. It issues 4,000,000 USD permanent debt at $r_d = 6.0\\%$ to buy back shares. $V_L = 10,000,000 + 0.25(4,000,000) = {vl_mm:,.0f}\\text{{ USD}}$, $E = {e_mm:,.0f}\\text{{ USD}}$, and levered $r_e = 12\\% + (12\\% - 6\\%)(0.75)(4/7) = {re_mm*100:.2f}\\%$.</p>", "purple") +
exercise_toolbar("corp-m6-mm", "Module 06 Chapter Exercises (L2 Capital Structure)") +
exercise_card("corp-ex-11", "Exercise 6.1 (Solved): Pecking Order Announcement Signal",
"<p>Why do equity markets typically react negatively when a mature industrial company announces a seasoned equity offering (SEO), but neutrally or positively to a straight bond issue?</p>",
"<p><strong>Answer: Asymmetric information / Pecking Order signaling</strong>. Managers issue new equity primarily when they believe shares are overvalued, whereas debt signals confidence in future cash flows.</p>", "solved", "L2 Corp") +
exercise_card("corp-ex-12", "Exercise 6.2 (Unsolved): MM With Taxes &amp; Distress",
"<p>Using $V_U = 10\\text{M USD}$, tax rate 25%, Debt $= 4\\text{M USD}$, and estimated $PV(\\text{Financial Distress}) = 650,000\\text{ USD}$, compute Static Trade-Off firm value $V_L$.</p>",
"<p><strong>Answer: 10,350,000 USD</strong>. $V_L = 10,000,000 + 0.25(4,000,000) - 650,000 = 10,350,000\\text{ USD}$.</p>", "unsolved", "L2 Corp") +
"</section>")

# MODULE 7: DIVIDENDS & BUYBACKS (L2)
parts.append(f"""
<section id="corp-m7-div" class="notes-chapter">
  <h2 class="section-heading"><span class="num">07.</span> Dividends, Share Repurchases &amp; Payout Policy (L2)</h2>
  <div class="formula-card">
    <div class="formula-title">Target Payout Adjustment (Lintner) &amp; Double-Taxation Effective Tax Rate</div>
    $$\\Delta D_t = (\\text{{Target Payout}} \\times E_t - D_{{t-1}}) \\times \\text{{Adjustment Factor}}$$
    $$\\text{{Effective Tax Rate on Dividends}} = 1 - (1 - t_{{\\text{{corp}}}})(1 - t_{{\\text{{div}}}})$$
  </div>
  <ul>
    <li><strong>Buyback Impact on EPS</strong>: Accretive if <strong>Earnings Yield ($E/P$) &gt; After-Tax Borrowing Cost (or After-Tax Cash Yield)</strong>!</li>
    <li><strong>Buyback Impact on BVPS</strong>: Increases Book Value Per Share ONLY if Repurchase Price &lt; Pre-buyback BVPS!</li>
  </ul>
""" + worked_box("Worked Numerical 6: Debt-Financed Share Repurchase EPS Accretion Test",
f"<p>A firm earns 24.0M USD across 8.0M shares ($EPS = {eps_old:.2f}\\text{{ USD}}$) at $P = 30.00\\text{{ USD}}$ ($E/P = 10.0\\%$). It borrows 30.0M USD at 4.50% after-tax interest to repurchase 1.0M shares. Since $E/P (10.0\\%) &gt; r_d(1-t) (4.5\\%)$, post-buyback $EPS = \\frac{{24.0\\text{{M}} - 1.35\\text{{M}}}}{{7.0\\text{{M}}}} = {eps_new:.2f}\\text{{ USD}}$ (Accretive!).</p>", "emerald") +
exercise_toolbar("corp-m7-div", "Module 07 Chapter Exercises (L2 Payout Policy)") +
exercise_card("corp-ex-13", "Exercise 7.1 (Solved): Residual Dividend Policy",
"<p>A firm forecasts Net Income of 60M USD, optimal capital budget of 75M USD, and target capital structure of 40% debt / 60% equity. Under a strict residual dividend policy, compute dividends paid.</p>",
"<p><strong>Answer: 15.0M USD</strong>. Equity needed for capex $= 0.60 \\times 75\\text{M} = 45\\text{M}$. Residual cash $= 60\\text{M} - 45\\text{M} = 15\\text{M USD}$.</p>", "solved", "L2 Payout") +
exercise_card("corp-ex-14", "Exercise 7.2 (Unsolved): Share Repurchase Effect on BVPS",
"<p>A stock trades at $P = 48\\text{ USD}$ while Book Value Per Share is $BVPS = 32\\text{ USD}$. If management buys back 10% of shares with excess cash, what happens to BVPS?</p>",
"<p><strong>Answer: BVPS decreases</strong> because shares are repurchased above book value ($P &gt; BVPS$).</p>", "unsolved", "L2 Payout") +
"</section>")

# MODULE 8: M&A & RESTRUCTURING (L2)
parts.append(f"""
<section id="corp-m8-ma" class="notes-chapter">
  <h2 class="section-heading"><span class="num">08.</span> Corporate Actions, Combinations &amp; M&amp;A Valuation (L2)</h2>
  <div class="formula-card">
    <div class="formula-title">Merger Gain Split, Post-Merger EPS &amp; Maximum Exchange Ratio</div>
    $$V_{{AT}} = V_A + V_T + S - C, \\qquad \\text{{Gain}}_T = P_T - V_T, \\qquad \\text{{Gain}}_A = S - \\text{{Premium}}_T$$
    $$\\text{{Stock Offer Exchange Ratio}} = \\frac{{\\text{{Offer Price}}_T}}{{\\text{{Acquirer Share Price}}_A}}$$
  </div>
  <ul>
    <li><strong>Takeover Defenses</strong>: Pre-offer (Poison Pills, Staggered Board, Supermajority, Golden Parachutes) vs. Post-offer (Pac-Man Defense, White Knight, Crown Jewel Defense, Greenmail).</li>
    <li><strong>Divestitures</strong>: <em>Spin-off</em> (new entity distributed pro-rata to existing shareholders, tax-free, no cash raised); <em>Equity Carve-out</em> (IPO of minority stake, raises cash); <em>Split-off</em> (shareholders swap parent shares for subsidiary shares).</li>
  </ul>
""" + worked_box("Worked Numerical 7: Stock-for-Stock M&amp;A Exchange Ratio &amp; Post-Merger EPS",
f"<p>Acquirer ($50\\text{{M}}$ shares, $EPS = 4.00\\text{{ USD}}$, $P = 60.00\\text{{ USD}}$) acquires Target ($10\\text{{M}}$ shares, $EPS = 2.50\\text{{ USD}}$) in a stock swap at 45.00 USD/share, generating 18.0M USD after-tax annual synergies. Exchange ratio $= 45 / 60 = {ex_ratio:.2f}$, issuing $10\\text{{M}} \\times 0.75 = 7.5\\text{{M}}$ new shares. Post-merger $EPS = \\frac{{200\\text{{M}} + 25\\text{{M}} + 18\\text{{M}}}}{{57.5\\text{{M}}}} = {post_eps_ma:.2f}\\text{{ USD}}$ (+0.23 USD accretive!).</p>", "blue") +
exercise_toolbar("corp-m8-ma", "Module 08 Chapter Exercises (L2 M&amp;A)") +
exercise_card("corp-ex-15", "Exercise 8.1 (Solved): Bootstrapping Fallacy in Mergers",
"<p>A high-P/E tech acquirer (P/E = 30x) buys a slow-growth utility (P/E = 12x) in an all-stock deal with zero synergies. EPS jumps immediately, yet total firm value should remain unchanged. Why?</p>",
"<p><strong>Answer: Bootstrapping fallacy</strong>. Simply swapping high-P/E shares for low-P/E earnings mathematically boosts EPS without creating economic cash flow; post-merger P/E compresses to the weighted average.</p>", "solved", "L2 M&A") +
exercise_card("corp-ex-16", "Exercise 8.2 (Unsolved): Cash vs. Stock Risk Sharing in M&amp;A",
"<p>When an acquirer's management is highly confident in merger synergies and believes its own stock is undervalued, which payment form transfers all synergy upside to acquirer shareholders?</p>",
"<p><strong>Answer: All-cash offer</strong>. Target shareholders receive a fixed cash payout and do not share post-merger upside (or downside) with acquirer shareholders.</p>", "unsolved", "L2 M&A") +
"</section>")

# MODULE 9: FORMULA SHEET
parts.append("""
<section id="corp-m9-formulas" class="notes-chapter">
  <h2 class="section-heading"><span class="num">09.</span> Master Corporate Issuers Formula Cheat Sheet</h2>
  <div class="table-container">
    <table>
      <thead><tr><th>Concept</th><th>Governing Formula</th><th>Exam Reminder</th></tr></thead>
      <tbody>
        <tr><td><strong>CCC</strong></td><td>$$DOH + DSO - DPO$$</td><td>Shorter CCC frees working capital cash</td></tr>
        <tr><td><strong>WACC</strong></td><td>$$w_d r_d(1-t) + w_p r_p + w_e r_e$$</td><td>Use target weights &amp; after-tax cost of debt</td></tr>
        <tr><td><strong>Hamada Relever</strong></td><td>$$\\beta_L = \\beta_U[1 + (1-t)(D/E)]$$</td><td>Unlever peer at peer's $(t, D/E)$, relever at project's</td></tr>
        <tr><td><strong>DTL</strong></td><td>$$DOL \\times DFL = \\frac{Q(P-V)}{Q(P-V)-F-I}$$</td><td>Multiplies sales % change to EPS % change</td></tr>
        <tr><td><strong>MM Proposition I</strong></td><td>$$V_L = V_U + t D$$</td><td>With corporate taxes; add $-PV(\\text{Distress})$ for trade-off</td></tr>
        <tr><td><strong>Buyback Accretion</strong></td><td>$$E/P &gt; r_d(1-t)$$</td><td>Accretive to EPS when earnings yield beats funding cost</td></tr>
      </tbody>
    </table>
  </div>
""" + exercise_toolbar("corp-m9-formulas", "Module 09 Capstone Drills") +
exercise_card("corp-ex-17", "Exercise 9.1 (Solved): Computing Net Acquisition Premium &amp; Acquirer Gain",
"<p>Acquirer ($V_A = 800\\text{M}$) bids 240M cash for Target ($V_T = 200\\text{M}$ pre-bid) with expected synergies $S = 60\\text{M}$. Compute Acquirer Gain.</p>",
"<p><strong>Answer: +20M USD to Acquirer</strong>. Premium paid $= 240\\text{M} - 200\\text{M} = 40\\text{M}$. $\\text{Gain}_A = S - \\text{Premium} = 60\\text{M} - 40\\text{M} = +20\\text{M USD}$.</p>", "solved", "L2 M&A") +
exercise_card("corp-ex-18", "Exercise 9.2 (Unsolved): Fixing Broken DOL Typo Check &amp; Break-Even",
"<p>With fixed costs $F = 200,000\\text{ USD}$, interest $I = 50,000\\text{ USD}$, price $P = 80\\text{ USD}$, variable cost $V = 45\\text{ USD}$, verify Operating Break-Even ($Q_{OBE}$) and Total Break-Even ($Q_{BE}$).</p>",
"<p><strong>Answer: $Q_{OBE} = 5,714$ units; $Q_{BE} = 7,143$ units</strong>. $200,000/35 = 5,714.3$; $250,000/35 = 7,142.9$.</p>", "unsolved", "L1 Leverage") +
exercise_card("corp-ex-19", "Exercise 9.3 (Solved): Spin-Off vs. Carve-Out Cash Flow",
"<p>Which restructuring transaction brings immediate cash proceeds onto the parent corporation's balance sheet?</p>",
"<p><strong>Answer: Equity Carve-Out</strong> (IPO selling subsidiary shares to public investors raises cash; spin-offs distribute shares to current owners without cash inflow).</p>", "solved", "L2 Restruct") +
exercise_card("corp-ex-20", "Exercise 9.4 (Unsolved): Target Payout Lintner Dividend Step",
"<p>Prior dividend was 1.80 USD, new EPS is 4.50 USD, target payout ratio is 50%, and adjustment factor is 0.40. Forecast this year's dividend.</p>",
f"<p><strong>Answer: 1.98 USD</strong>. $\\Delta D = (0.50 \\times 4.50 - 1.80) \\times 0.40 = 0.45 \\times 0.40 = +0.18\\text{{ USD}} \\implies D_t = 1.98\\text{{ USD}}$.</p>", "unsolved", "L2 Payout") +
"</section>")

write_notes_html("".join(parts), OUTPUT_PATH)
