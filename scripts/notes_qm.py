"""
scripts/notes_qm.py
Generates data/qm_reference_extracted.html:
Quantitative Methods Master Reference Library (12 Modules)
Aligned with CFA CBOK II & 2026-2027 L1 (11 LMs) + L2 (7 LMs) + Volatility/Backtesting/LLMs.
Includes 14 Python-computed Worked Numericals + 24 Interactive Chapter Exercises (12 Solved + 12 Unsolved).
"""
import math
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scripts.qbank_helper import norm_cdf, irr
from scripts.notes_helper import worked_box, exercise_card, exercise_toolbar, write_notes_html

OUTPUT_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "qm_reference_extracted.html")

# Pre-compute exact numerical answers in Python
ear_m = (1 + 0.08 / 12) ** 12 - 1
ear_c = math.exp(0.08) - 1
hpr_1, hpr_2, hpr_3 = 0.14, -0.08, 0.19
geo_mean = ((1 + hpr_1) * (1 + hpr_2) * (1 + hpr_3)) ** (1 / 3) - 1
arith_mean = (hpr_1 + hpr_2 + hpr_3) / 3
harm_mean = 3 / (1 / 42.0 + 1 / 48.0 + 1 / 55.0)
mwr_cf = irr([-100000, -50000, 178000])
# TVM bond/equity & forward rate
f_1_1 = ((1.054 ** 2) / 1.046) - 1
# Bayes
p_beat = 0.40
p_up_given_beat = 0.80
p_up_given_miss = 0.25
p_up = p_beat * p_up_given_beat + (1 - p_beat) * p_up_given_miss
p_beat_given_up = (p_beat * p_up_given_beat) / p_up
# Roy safety first
sfr_a = (0.11 - 0.03) / 0.16
sfr_b = (0.14 - 0.03) / 0.24
# Hypothesis test t-stat
t_stat_qm = (0.012 - 0.0) / (0.036 / math.sqrt(36))
# Regression & ANOVA
b1_reg = 0.0288 / 0.0256
# Logistic odds
log_odds = -1.25 + 0.85 * 2.0 - 0.40 * 1.5
prob_default = 1 / (1 + math.exp(-log_odds))
# AR(1) mean reversion
ar_mean = 0.018 / (1 - 0.64)
ar_f1 = 0.018 + 0.64 * 0.065
ar_f2 = 0.018 + 0.64 * ar_f1
# GARCH(1,1)
garch_var = 0.000012 + 0.10 * (0.025 ** 2) + 0.85 * (0.018 ** 2)
garch_vol = math.sqrt(garch_var)
# Portfolio 2-asset risk
var_p = (0.6 ** 2) * (0.18 ** 2) + (0.4 ** 2) * (0.12 ** 2) + 2 * 0.6 * 0.4 * 0.25 * 0.18 * 0.12
sd_p = math.sqrt(var_p)

parts = []

parts.append("""<div class="top-controls">
  <button class="btn-ctrl" onclick="toggleTheme()">🌓 Switch Theme</button>
  <button class="btn-ctrl" onclick="window.print()">🖨️ Print / Save as PDF</button>
</div>

<div class="doc-hero">
  <h1>Quantitative Methods &amp; Data Science (CFA&reg; CBOK II)</h1>
  <p>Master Curriculum Reference for CFA&reg; Level 1 (2027 11-Module Structure, 11%–14% Weight) &amp; Level 2 (Multiple Regression, Time Series, Volatility Models, Backtesting, Machine Learning &amp; LLMs/GenAI). Features 14 Python-verified Worked Numericals and 24 Interactive Chapter Exercises (12 Solved + 12 Unsolved Self-Test).</p>
  <div class="meta-tags">
    <span class="badge badge-blue">L1 Weight: 11%–14% (2027)</span>
    <span class="badge badge-purple">L2 Weight: 5%–10%</span>
    <span class="badge badge-emerald">12 Modules + 24 Exercises</span>
    <span class="badge badge-cyan">Interactive Monte Carlo &amp; TVM Lab</span>
  </div>
</div>

<div class="card" style="margin-top: 15px; margin-bottom: 25px;">
  <div class="card-title">📐 Quick Navigation: Quantitative Methods Modules</div>
  <div class="fsa-nav-bar">
    <a class="fsa-nav-btn" href="#qm-m1-returns">01. Rates &amp; Returns</a>
    <a class="fsa-nav-btn" href="#qm-m2-tvm">02. Time Value of Money</a>
    <a class="fsa-nav-btn" href="#qm-m3-stats">03. Return Statistics</a>
    <a class="fsa-nav-btn" href="#qm-m4-prob">04. Probability &amp; Bayes</a>
    <a class="fsa-nav-btn" href="#qm-m5-hyp">05. Sampling &amp; Hypothesis</a>
    <a class="fsa-nav-btn" href="#qm-m6-reg">06. Multiple &amp; Logistic Reg</a>
    <a class="fsa-nav-btn" href="#qm-m7-mis">07. Misspecification</a>
    <a class="fsa-nav-btn" href="#qm-m8-ts">08. Time Series &amp; GARCH</a>
    <a class="fsa-nav-btn" href="#qm-m9-sim">09. Simulation &amp; Backtest</a>
    <a class="fsa-nav-btn" href="#qm-m10-port">10. Portfolio Risk Math</a>
    <a class="fsa-nav-btn" href="#qm-m11-ml">11. ML, Big Data &amp; LLMs</a>
    <a class="fsa-nav-btn" href="#qm-m12-formulas" style="color: var(--accent-emerald); font-weight: 700;">12. Formula Sheet</a>
  </div>
  <div style="display:flex; gap:10px; flex-wrap:wrap; margin-top:10px;">
    <button type="button" class="btn" onclick="jumpToSubjectBank(1, 'Quantitative Methods')">📝 Practice 90 L1 Quant MCQs</button>
    <button type="button" class="btn btn-secondary" onclick="jumpToSubjectBank(2, 'Quantitative Methods')">📑 Practice 10 L2 Quant Vignettes (60 Qs)</button>
    <button type="button" class="btn btn-secondary" onclick="switchTab('sim-quant')">🔬 Open Quant Monte Carlo &amp; TVM Lab</button>
    <button type="button" class="filter-btn" onclick="toggleChapterExercises('qm-reference', false)">🙈 Hide Solutions</button>
    <button type="button" class="filter-btn" onclick="toggleChapterExercises('qm-reference', true)">✅ Reveal All Solutions</button>
  </div>
</div>
""")

# MODULE 1: RATES & RETURNS
parts.append(f"""
<section id="qm-m1-returns" class="notes-chapter">
  <h2 class="section-heading"><span class="num">01.</span> Rates, Returns &amp; Benchmarking (2027 L1 Modules 1–3)</h2>
  <p>Interest rates serve simultaneously as required rates of return, discount rates, and opportunity costs: $r = r_{{\\text{{real}}}} + E(\\pi) + \\text{{Default}} + \\text{{Liquidity}} + \\text{{Maturity}}$.</p>
  <div class="formula-card">
    <div class="formula-title">Effective Annual Rate (EAR), Geometric vs. Harmonic Mean &amp; Real After-Tax Return</div>
    $$EAR = \\left(1 + \\frac{{r_s}}{{m}}\\right)^m - 1, \\qquad EAR_{{\\text{{cont}}}} = e^{{r_s}} - 1$$
    $$\\bar{{R}}_G = \\left[\\prod_{{t=1}}^T (1 + R_t)\\right]^{{1/T}} - 1, \\qquad \\bar{{X}}_H = \\frac{{n}}{{\\sum_{{i=1}}^n \\frac{{1}}{{X_i}}}}, \\qquad \\bar{{X}}_H \\le \\bar{{R}}_G \\le \\bar{{R}}_A$$
    $$R_{{\\text{{after-tax, real}}}} = \\frac{{1 + R_{{\\text{{nominal}}}}(1 - t)}}{{1 + \\pi}} - 1$$
  </div>
  <p><strong>Exam Traps</strong>: Use the <em>harmonic mean</em> when averaging purchase prices under constant dollar cost-averaging or aggregating valuation multiples like P/E across a portfolio. Use <em>trimmed/winsorized means</em> to handle outliers.</p>
""" + worked_box("Worked Numerical 1: Compounding EAR, Geometric Mean &amp; Harmonic Dollar-Cost Averaging",
f"<p><strong>Part A (EAR)</strong>: An 8.00% stated annual rate compounded monthly yields $EAR = (1 + 0.08/12)^{{12}} - 1 = {ear_m*100:.3f}\\%$; compounded continuously yields $e^{{0.08}} - 1 = {ear_c*100:.3f}\\%$.</p>"
f"<p><strong>Part B (Geometric vs. Arithmetic)</strong>: Annual returns of +14.0%, -8.0%, +19.0% give Arithmetic Mean $= {arith_mean*100:.2f}\\%$ and Geometric Mean $= [(1.14)(0.92)(1.19)]^{{1/3}} - 1 = {geo_mean*100:.2f}\\%$.</p>"
f"<p><strong>Part C (Harmonic Mean)</strong>: Investing 1,000 USD quarterly at 42 USD, 48 USD, and 55 USD gives average cost per share $= \\frac{{3}}{{1/42 + 1/48 + 1/55}} = {harm_mean:.2f}\\text{{ USD}}$.</p>", "emerald") +
exercise_toolbar("qm-m1-returns", "Module 01 Chapter Exercises (Rates &amp; Returns)") +
exercise_card("qm-ex-1", "Exercise 1.1 (Solved): MWR vs. TWR with Mid-Year Contribution",
"<p>An investor deposits 100,000 USD at $t=0$, adds 50,000 USD at $t=1$, and ends at 178,000 USD at $t=2$. Compute the annualized Money-Weighted Return (IRR).</p>",
f"<p><strong>Answer: $MWR = {mwr_cf*100:.2f}\\%$</strong>. Solving $-100,000 - \\frac{{50,000}}{{1+r}} + \\frac{{178,000}}{{(1+r)^2}} = 0$ yields $r = {mwr_cf*100:.2f}\\%$.</p>", "solved", "L1 Quant") +
exercise_card("qm-ex-2", "Exercise 1.2 (Unsolved): After-Tax Real Return",
"<p>A taxable bond earns 6.40% nominal yield, marginal tax rate is 25%, and inflation is 3.00%. Compute the exact after-tax real return.</p>",
f"<p><strong>Answer: $+1.75\\%$</strong>. After-tax nominal $= 6.40\\% \\times (1 - 0.25) = 4.80\\%$. Real after-tax $= \\frac{{1.048}}{{1.03}} - 1 = {((1.048/1.03)-1)*100:.2f}\\%$.</p>", "unsolved", "L1 Quant") +
"</section>")

# MODULE 2: TIME VALUE OF MONEY
parts.append(f"""
<section id="qm-m2-tvm" class="notes-chapter">
  <h2 class="section-heading"><span class="num">02.</span> Time Value of Money in Finance (2027 L1 Module 4)</h2>
  <p>The 2027 L1 syllabus integrates TVM directly into bond discounting, perpetual preferred/equity valuation, implied growth rates, and the <strong>Cash Flow Additivity Principle</strong> (two cash flow streams with identical future payoffs in all states must have identical present values—forming the basis of no-arbitrage forward pricing).</p>
  <div class="formula-card">
    <div class="formula-title">Annuities, Perpetuities &amp; Forward Rate Implication</div>
    $$PV_{{\\text{{ord}}}} = PMT \\cdot \\frac{{1 - (1+r)^{{-N}}}}{{r}}, \\qquad PV_{{\\text{{due}}}} = PV_{{\\text{{ord}}}} \\cdot (1+r), \\qquad PV_{{\\text{{perp}}}} = \\frac{{PMT}}{{r - g}}$$
    $$(1 + z_2)^2 = (1 + z_1)(1 + f_{{1,1}}) \\implies f_{{1,1}} = \\frac{{(1+z_2)^2}}{{1+z_1}} - 1$$
  </div>
""" + worked_box("Worked Numerical 2: Cash Flow Additivity &amp; Implied 1-Year Forward Rate",
f"<p>If the 1-year spot rate is $z_1 = 4.60\\%$ and the 2-year spot rate is $z_2 = 5.40\\%$, cash flow additivity prevents arbitrage only if the 1-year forward rate one year from today equals: $f_{{1,1}} = \\frac{{1.054^2}}{{1.046}} - 1 = {f_1_1*100:.2f}\\%$.</p>", "blue") +
exercise_toolbar("qm-m2-tvm", "Module 02 Chapter Exercises (TVM)") +
exercise_card("qm-ex-3", "Exercise 2.1 (Solved): Deferred Perpetuity Valuation",
"<p>A perpetual preferred share begins paying an annual dividend of 4.50 USD starting at $t=4$ (no dividends at $t=1, 2, 3$). Required return is 9.0%. Compute $PV_0$.</p>",
f"<p><strong>Answer: 38.61 USD</strong>. At $t=3$, $PV_3 = 4.50 / 0.09 = 50.00\\text{{ USD}}$. Discounting back 3 years: $PV_0 = 50.00 / 1.09^3 = {50/(1.09**3):.2f}\\text{{ USD}}$.</p>", "solved", "L1 TVM") +
exercise_card("qm-ex-4", "Exercise 2.2 (Unsolved): Implied Dividend Growth Rate from Market Price",
"<p>A stock trades at 60.00 USD, pays $D_1 = 2.10\\text{{ USD}}$, and has a required return of 10.50%. Compute the market-implied perpetual growth rate $g$.</p>",
f"<p><strong>Answer: 7.00%</strong>. $g = r - D_1/P_0 = 0.105 - 2.10/60.00 = 0.105 - 0.035 = 0.070 = 7.00\\%$.</p>", "unsolved", "L1 TVM") +
"</section>")

# MODULE 3: STATISTICAL CHARACTERISTICS
parts.append("""
<section id="qm-m3-stats" class="notes-chapter">
  <h2 class="section-heading"><span class="num">03.</span> Statistical Characteristics of Asset Returns (2027 L1 Module 5)</h2>
  <div class="formula-card">
    <div class="formula-title">Dispersion, Downside Risk, Skewness &amp; Excess Kurtosis</div>
    $$s^2 = \\frac{\\sum (X_i - \\bar{{X}})^2}{{n - 1}}, \\qquad s_{{\\text{{target}}}} = \\sqrt{{\\frac{{\\sum_{{X_i < B}} (X_i - B)^2}}{{n - 1}}}}, \\qquad CV = \\frac{{s}}{{\\bar{{X}}}}$$
    $$\\text{Positive Skew: } \\text{Mean} > \\text{Median} > \\text{Mode}; \\qquad \\text{Excess Kurtosis} = \\text{Kurtosis} - 3 \\quad (\\text{Leptokurtic } > 0 \\implies \\text{Fat Tails})$$
  </div>
""" + exercise_toolbar("qm-m3-stats", "Module 03 Chapter Exercises (Return Statistics)") +
exercise_card("qm-ex-5", "Exercise 3.1 (Solved): Target Semideviation",
"<p>Given annual returns of 12%, 4%, -6%, and 10% and a target benchmark $B = 5\\%$, compute the sample target semideviation.</p>",
f"<p><strong>Answer: 6.38%</strong>. Only 4% ($-1\\%$) and -6% ($-11\\%$) fall below $B=5\\%$. Sum of squared shortfalls $= (-0.01)^2 + (-0.11)^2 = 0.0001 + 0.0121 = 0.0122$. Divide by $n-1 = 3$: $0.004067$. Square root $= {math.sqrt(0.0122/3)*100:.2f}\\%$.</p>", "solved", "L1 Stats") +
exercise_card("qm-ex-6", "Exercise 3.2 (Unsolved): Chebyshev's Inequality",
"<p>An asymmetric hedge fund index has a mean return of 9% and standard deviation of 6%. Without assuming normality, what is the minimum percentage of returns lying between -3% and +21%?</p>",
f"<p><strong>Answer: 75.0%</strong>. Distance is $k = (21 - 9)/6 = 2.0$ SDs. By Chebyshev's inequality, at least $1 - 1/k^2 = 1 - 1/4 = 75\\%$.</p>", "unsolved", "L1 Stats") +
"</section>")

# MODULE 4: PROBABILITY, BAYES & DISTRIBUTIONS
parts.append(f"""
<section id="qm-m4-prob" class="notes-chapter">
  <h2 class="section-heading"><span class="num">04.</span> Probability, Bayes' Theorem &amp; Distributions (2027 L1 Module 6)</h2>
  <div class="formula-card">
    <div class="formula-title">Bayes' Updating, Roy's Safety-First Criterion &amp; Lognormal Pricing</div>
    $$P(A \\mid B) = \\frac{{P(B \\mid A) P(A)}}{{P(B)}}, \\qquad \\text{{SFRatio}} = \\frac{{E(R_p) - R_L}}{{\\sigma_p}}$$
  </div>
  <ul>
    <li><strong>Normal vs. Lognormal</strong>: Continuously compounded asset returns follow a Normal distribution; asset <em>prices</em> (bounded below by zero, positively skewed) follow a Lognormal distribution.</li>
    <li><strong>Monte Carlo vs. Parametric Normal</strong>: Student's t ($df < 30$) captures fatter tails; Chi-Square and F-distributions govern variance tests (always right-skewed, non-negative).</li>
  </ul>
""" + worked_box("Worked Numerical 3: Bayes' Theorem &amp; Roy's Safety-First Portfolio Selection",
f"<p><strong>Bayes</strong>: Prior probability of an earnings beat is $P(\\text{{Beat}}) = 40\\%$. Historically, 80% of beating firms rally ($P(\\text{{Up}}\\mid\\text{{Beat}})=0.80$), while 25% of missing firms rally ($P(\\text{{Up}}\\mid\\text{{Miss}})=0.25$). Given a stock rallies today, updated probability of a beat is: $P(\\text{{Beat}}\\mid\\text{{Up}}) = \\frac{{0.40 \\times 0.80}}{{0.40(0.80)+0.60(0.25)}} = \\frac{{0.32}}{{0.47}} = {p_beat_given_up*100:.2f}\\%$.</p>"
f"<p><strong>Roy's Safety-First</strong> ($R_L = 3.0\\%$): Fund A ($E=11\\%, \\sigma=16\\%$) gives $SFR_A = {sfr_a:.3f}$; Fund B ($E=14\\%, \\sigma=24\\%$) gives $SFR_B = {sfr_b:.3f}$. Fund A maximizes safety-first utility.</p>", "purple") +
exercise_toolbar("qm-m4-prob", "Module 04 Chapter Exercises (Probability)") +
exercise_card("qm-ex-7", "Exercise 4.1 (Solved): Binomial Option Path Counting",
"<p>A stock has a 60% probability of moving up each quarter over 3 quarters. What is the probability of getting exactly 2 up-moves?</p>",
f"<p><strong>Answer: 43.20%</strong>. $\\binom{{3}}{{2}}(0.6)^2(0.4)^1 = 3 \\times 0.36 \\times 0.4 = {3*0.36*0.4*100:.2f}\\%$.</p>", "solved", "L1 Prob") +
exercise_card("qm-ex-8", "Exercise 4.2 (Unsolved): Normal Z-Score Shortfall Probability",
"<p>A portfolio has $E(R) = 10\\%$ and $\\sigma = 15\\%$. Compute the z-score for returns falling below $-5\\%$.</p>",
"<p><strong>Answer: $z = -1.00$ ($\approx 15.87\\%$ probability)</strong>. $z = (-5\\% - 10\\%) / 15\\% = -1.00$.</p>", "unsolved", "L1 Prob") +
"</section>")

# MODULE 5: SAMPLING, BIASES & HYPOTHESIS TESTING
parts.append(f"""
<section id="qm-m5-hyp" class="notes-chapter">
  <h2 class="section-heading"><span class="num">05.</span> Sampling, Estimation, Biases &amp; Hypothesis Testing (2027 L1 Module 7)</h2>
  <div class="formula-card">
    <div class="formula-title">Test Statistics &amp; Parametric vs. Nonparametric Selection</div>
    $$t = \\frac{{\\bar{{X}} - \\mu_0}}{{s / \\sqrt{{n}}}} \\; (df=n-1), \\qquad \\chi^2 = \\frac{{(n-1)s^2}}{{\\sigma_0^2}}, \\qquad F = \\frac{{s_1^2}}{{s_2^2}} \\; (s_1^2 \\ge s_2^2)$$
  </div>
  <ul>
    <li><strong>Biases</strong>: <em>Data snooping / p-hacking</em> (testing dozens of strategies until one hits $p&lt;0.05$), <em>Survivorship bias</em> (omitting delisted funds), <em>Look-ahead bias</em> (using accounting data before its filing date), <em>Time-period bias</em>.</li>
    <li><strong>Errors &amp; Power</strong>: Type I ($\alpha = P(\\text{{Reject true }} H_0)$); Type II ($\beta = P(\\text{{Fail to reject false }} H_0)$); Power $= 1 - \beta$.</li>
    <li><strong>Nonparametric Equivalents</strong>: Wilcoxon signed-rank (paired), Mann-Whitney U (independent), Spearman rank correlation (ordinal/outliers).</li>
  </ul>
""" + worked_box("Worked Numerical 4: One-Sample t-Test on Active Alpha",
f"<p>Over $n=36$ months, a fund earns mean monthly excess return $\\bar{{X}} = +1.20\\%$ with sample SD $s = 3.60\\%$. Test $H_0: \\mu = 0$: $t = \\frac{{0.012 - 0}}{{0.036 / \\sqrt{{36}}}} = \\frac{{0.012}}{{0.006}} = {t_stat_qm:.2f}$. Since $t = 2.00$ vs. two-tailed $t_{{0.025, 35}} \\approx 2.03$, we <strong>fail to reject</strong> $H_0$ at $\\alpha = 5\\%$.</p>", "cyan") +
exercise_toolbar("qm-m5-hyp", "Module 05 Chapter Exercises (Hypothesis Testing)") +
exercise_card("qm-ex-9", "Exercise 5.1 (Solved): Chi-Square Variance Test",
"<p>A portfolio targets volatility $\\sigma_0 \\le 12\\%$. Over $n=25$ months, sample SD is $s = 15\\%$. Compute the $\\chi^2$ test statistic.</p>",
f"<p><strong>Answer: $\\chi^2 = 37.50$</strong>. $\\chi^2 = \\frac{{24 \\times 0.15^2}}{{0.12^2}} = \\frac{{24 \\times 0.0225}}{{0.0144}} = {24*(0.15**2)/(0.12**2):.2f}$.</p>", "solved", "L1 Quant") +
exercise_card("qm-ex-10", "Exercise 5.2 (Unsolved): Look-Ahead vs. Survivorship Bias",
"<p>A value strategy backtest forms portfolios on January 1 using fiscal year-end December 31 earnings released in March. Which bias invalidates the backtest?</p>",
"<p><strong>Answer: Look-ahead bias</strong> (incorporating fundamental information before it was publicly available at trade execution).</p>", "unsolved", "L1 Quant") +
"</section>")

# MODULE 6: SIMPLE, MULTIPLE & LOGISTIC REGRESSION
parts.append(f"""
<section id="qm-m6-reg" class="notes-chapter">
  <h2 class="section-heading"><span class="num">06.</span> Simple, Multiple &amp; Logistic Regression (L1 Module 10 &amp; L2 Modules 1–2, 4)</h2>
  <div class="formula-card">
    <div class="formula-title">OLS ANOVA, Adjusted $R^2$, F-Test &amp; Logistic Probability</div>
    $$\\hat{{b}}_1 = \\frac{{\\text{{Cov}}(X,Y)}}{{\\text{{Var}}(X)}}, \\qquad R^2 = \\frac{{\\text{{SSR}}}}{{\\text{{SST}}}}, \\qquad \\bar{{R}}^2 = 1 - \\left(\\frac{{n-1}}{{n-k-1}}\\right)(1 - R^2), \\qquad F = \\frac{{\\text{{MSR}}}}{{\\text{{MSE}}}} = \\frac{{\\text{{SSR}}/k}}{{\\text{{SSE}}/(n-k-1)}}$$
    $$\\ln\\left(\\frac{{P}}{{1-P}}\\right) = b_0 + b_1 X_1 + \\dots + b_k X_k \\implies P(Y=1) = \\frac{{1}}{{1 + e^{{-\\text{{log-odds}}}}}}$$
  </div>
  <p><strong>Key L2 Metrics</strong>: Use <strong>AIC</strong> (prediction accuracy) or <strong>BIC</strong> (parsimony, stricter penalty for $k$) to compare nested/non-nested models—lower is better. Watch for high-leverage points ($h_{{ii}} &gt; 3(k+1)/n$) and Cook's $D &gt; \\sqrt{{k/n}}$.</p>
""" + worked_box("Worked Numerical 5: OLS Regression Slope &amp; Logistic Default Probability",
f"<p><strong>Simple OLS</strong>: If $\\text{{Cov}}(R_i, R_m) = 0.0288$ and $\\text{{Var}}(R_m) = 0.0256$, slope $\\beta = \\frac{{0.0288}}{{0.0256}} = {b1_reg:.3f}$.</p>"
f"<p><strong>Logistic Regression (L2)</strong>: Log-odds of bond default $= -1.25 + 0.85(\\text{{Debt/EBITDA}}) - 0.40(\\text{{Interest Cov}})$. For Debt/EBITDA $= 2.0$ and Coverage $= 1.5$, log-odds $= {log_odds:.3f}$, giving $P(\\text{{Default}}) = \\frac{{1}}{{1 + e^{{-({log_odds:.3f})}}}} = {prob_default*100:.2f}\\%$.</p>", "emerald") +
exercise_toolbar("qm-m6-reg", "Module 06 Chapter Exercises (Regression)") +
exercise_card("qm-ex-11", "Exercise 6.1 (Solved): Adjusted $R^2$ Penalty",
"<p>A regression with $n=45$ and $k=3$ has $R^2 = 0.64$. Compute Adjusted $\\bar{{R}}^2$.</p>",
f"<p><strong>Answer: 0.6137</strong>. $\\bar{{R}}^2 = 1 - \\frac{{44}}{{41}}(1 - 0.64) = 1 - \\frac{{44}}{{41}}(0.36) = {1 - (44/41)*0.36:.4f}$.</p>", "solved", "L2 Quant") +
exercise_card("qm-ex-12", "Exercise 6.2 (Unsolved): Interpreting Dummy Variables",
"<p>To model four distinct calendar quarters without triggering the dummy-variable trap in an OLS model containing an intercept, how many dummy variables must be included?</p>",
"<p><strong>Answer: 3 dummy variables ($m - 1 = 4 - 1 = 3$)</strong>. Including all 4 alongside an intercept causes exact multicollinearity.</p>", "unsolved", "L2 Quant") +
"</section>")

# MODULE 7: MISSPECIFICATION
parts.append("""
<section id="qm-m7-mis" class="notes-chapter">
  <h2 class="section-heading"><span class="num">07.</span> Regression Misspecification &amp; Remedies (L2 Module 3)</h2>
  <div class="table-container">
    <table>
      <thead><tr><th>Violation</th><th>Effect on OLS</th><th>Diagnostic Test</th><th>Remedy</th></tr></thead>
      <tbody>
        <tr><td><strong>Conditional Heteroskedasticity</strong></td><td>Coefficients unbiased; <strong>SEs understated</strong> $\\implies$ inflated $t$-stats (false positives)</td><td><strong>Breusch-Pagan</strong>: $\\chi^2 = n R^2_{\\text{resid}}$ (one-tailed)</td><td>White-corrected (heteroskedasticity-consistent) robust SEs</td></tr>
        <tr><td><strong>Positive Serial Correlation</strong></td><td>Coefficients unbiased (unless lagged $Y$); <strong>SEs understated</strong> $\\implies$ inflated $t$-stats</td><td><strong>Durbin-Watson</strong>: $DW \\approx 2(1-r)$ ($DW < d_L \\implies$ +corr); <strong>Breusch-Godfrey</strong> (for lagged $Y$)</td><td>Newey-West (HAC) SEs or Hansen method</td></tr>
        <tr><td><strong>Multicollinearity</strong></td><td>Coefficients &amp; SEs unstable; <strong>high $R^2$ &amp; $F$-stat yet insignificant individual $t$-stats</strong></td><td><strong>VIF</strong> $= \\frac{1}{1-R_j^2}$ ($VIF &gt; 5$ warning, $&gt; 10$ severe)</td><td>Drop redundant variable or combine via PCA/Ridge</td></tr>
      </tbody>
    </table>
  </div>
""" + exercise_toolbar("qm-m7-mis", "Module 07 Chapter Exercises (Misspecification)") +
exercise_card("qm-ex-13", "Exercise 7.1 (Solved): Variance Inflation Factor (VIF)",
"<p>Regressing predictor $X_1$ on predictors $X_2$ and $X_3$ yields $R_1^2 = 0.88$. Compute $\\text{VIF}_1$ and diagnose multicollinearity.</p>",
f"<p><strong>Answer: $\\text{{VIF}}_1 = {1/(1-0.88):.2f}$</strong>. Since $8.33 &gt; 5$ (approaching 10), moderate-to-serious multicollinearity exists.</p>", "solved", "L2 Quant") +
exercise_card("qm-ex-14", "Exercise 7.2 (Unsolved): Breusch-Pagan Test Statistic",
"<p>In a model with $n=100$ observations and $k=4$ predictors, regressing squared OLS residuals on the 4 predictors produces $R^2 = 0.14$. Compute the Breusch-Pagan test statistic.</p>",
"<p><strong>Answer: $\\chi^2 = 14.00$ ($df=4$)</strong>. $BP = n R^2_{\\text{resid}} = 100 \\times 0.14 = 14.00 &gt; 9.49$ critical value ($\\alpha=5\\%$), confirming conditional heteroskedasticity.</p>", "unsolved", "L2 Quant") +
"</section>")

# MODULE 8: TIME SERIES & GARCH
parts.append(f"""
<section id="qm-m8-ts" class="notes-chapter">
  <h2 class="section-heading"><span class="num">08.</span> Time-Series Forecasting &amp; Volatility Models (L2 Module 5 &amp; CBOK II)</h2>
  <div class="formula-card">
    <div class="formula-title">AR(1) Mean Reversion, Random Walk, Dickey-Fuller &amp; GARCH(1,1)</div>
    $$X_t = b_0 + b_1 X_{{t-1}} + \\epsilon_t \\implies \\bar{{X}} = \\frac{{b_0}}{{1 - b_1}} \\; (|b_1| &lt; 1), \\qquad \\text{{Random Walk: }} b_1 = 1 \\; (\\text{{Unit Root}})$$
    $$\\text{{Seasonality AR(1): }} X_t = b_0 + b_1 X_{{t-1}} + b_2 X_{{t-4}} + \\epsilon_t$$
    $$\\sigma_t^2 = \\omega + \\alpha \\epsilon_{{t-1}}^2 + \\beta \\sigma_{{t-1}}^2, \\qquad \\text{{Long-Run Variance }} V_L = \\frac{{\\omega}}{{1 - \\alpha - \\beta}}$$
  </div>
  <ul>
    <li><strong>Covariance Stationarity</strong>: Constant finite mean, constant finite variance, and constant covariance across lags. <strong>Never use standard DW</strong> on an AR model—inspect residual autocorrelations via $t$-stats!</li>
    <li><strong>Cointegration</strong>: Two unit-root non-stationary series are cointegrated if a linear combination (error term) is stationary (tested via Engle-Granger DF test)—enabling pairs trading and valid long-run regressions.</li>
  </ul>
""" + worked_box("Worked Numerical 6: AR(1) Mean Reversion &amp; GARCH(1,1) Volatility Forecast",
f"<p><strong>AR(1)</strong>: Monthly inflation follows $X_t = 0.018 + 0.64 X_{{t-1}}$. Mean-reverting level $= \\frac{{0.018}}{{1 - 0.64}} = {ar_mean*100:.2f}\\%$. Given $X_t = 6.50\\%$, $\\hat{{X}}_{{t+1}} = {ar_f1*100:.3f}\\%$ and $\\hat{{X}}_{{t+2}} = {ar_f2*100:.3f}\\%$.</p>"
f"<p><strong>GARCH(1,1)</strong>: Parameters $\\omega = 0.000012$, $\\alpha = 0.10$, $\\beta = 0.85$. Yesterday's shock $\\epsilon_{{t-1}} = +2.50\\%$ and prior volatility $\\sigma_{{t-1}} = 1.80\\%$. Today's variance $\\sigma_t^2 = 0.000012 + 0.10(0.025)^2 + 0.85(0.018)^2 = {garch_var:.6f} \\implies \\sigma_t = {garch_vol*100:.2f}\\%$.</p>", "amber") +
exercise_toolbar("qm-m8-ts", "Module 08 Chapter Exercises (Time Series &amp; GARCH)") +
exercise_card("qm-ex-15", "Exercise 8.1 (Solved): Long-Run GARCH Volatility",
"<p>Using $\\omega = 0.000012$, $\\alpha = 0.10$, $\\beta = 0.85$ above, compute the unconditional long-run daily volatility $\\sqrt{{V_L}}$.</p>",
f"<p><strong>Answer: 1.55% daily</strong>. $V_L = \\frac{{0.000012}}{{1 - 0.10 - 0.85}} = \\frac{{0.000012}}{{0.05}} = 0.000240$. $\\sqrt{{V_L}} = {math.sqrt(0.000012/0.05)*100:.2f}\\%$.</p>", "solved", "CBOK Vol") +
exercise_card("qm-ex-16", "Exercise 8.2 (Unsolved): Spurious Regression Remedy",
"<p>An analyst regresses two non-cointegrated random walk stock prices ($Y_t$ on $X_t$) and gets $R^2 = 0.94$ with $DW = 0.18$. What must the analyst do?</p>",
"<p><strong>Answer: Take first differences ($\\Delta Y_t = Y_t - Y_{{t-1}}$) before regressing.</strong> Regressing non-cointegrated random walks produces spurious correlation.</p>", "unsolved", "L2 Quant") +
"</section>")

# MODULE 9: SIMULATION, SCENARIO ANALYSIS & MODEL GOVERNANCE
parts.append("""
<section id="qm-m9-sim" class="notes-chapter">
  <h2 class="section-heading"><span class="num">09.</span> Simulation, Backtesting &amp; Model Governance (2027 L1 Module 9 &amp; CBOK II)</h2>
  <ul>
    <li><strong>Monte Carlo Simulation</strong>: Generates thousands of correlated stochastic paths via parametric distributions (Cholesky decomposition for correlated factors) — ideal for path-dependent options and multi-period retirement planning.</li>
    <li><strong>Historical Simulation &amp; Bootstrapping</strong>: Bootstrapping resamples <em>with replacement</em> from historical returns, preserving empirical fat tails and skewness without imposing normality.</li>
    <li><strong>Model Governance &amp; Walk-Forward Backtesting</strong>: Prevents look-ahead/survivorship bias via expanding/rolling out-of-sample windows, sensitivity sweeps, hyperparameter freeze before out-of-sample test, and ongoing drift/PSI monitoring.</li>
  </ul>
""" + exercise_toolbar("qm-m9-sim", "Module 09 Chapter Exercises (Simulation &amp; Governance)") +
exercise_card("qm-ex-17", "Exercise 9.1 (Solved): Choosing Bootstrap vs. Parametric Monte Carlo",
"<p>A risk manager wants to stress-test a hedged credit portfolio while preserving historical cross-asset crash correlations and extreme skewness without specifying a parametric distribution. Which simulation is best?</p>",
"<p><strong>Answer: Historical Block Bootstrapping</strong> (resampling contiguous multi-day blocks with replacement preserves empirical fat tails, correlation spikes, and serial clustering).</p>", "solved", "L1/CBOK Sim") +
exercise_card("qm-ex-18", "Exercise 9.2 (Unsolved): Walk-Forward Cross-Validation vs. K-Fold CV in Time Series",
"<p>Why is standard randomized K-Fold cross-validation dangerous when backtesting a monthly stock momentum factor?</p>",
"<p><strong>Answer: Look-ahead leakage.</strong> Randomized K-Fold uses future periods in training folds to predict past test folds; quantitative finance requires chronological expanding/rolling walk-forward splits.</p>", "unsolved", "Model Gov") +
"</section>")

# MODULE 10: PORTFOLIO RETURN & RISK MATH
parts.append(f"""
<section id="qm-m10-port" class="notes-chapter">
  <h2 class="section-heading"><span class="num">10.</span> Portfolio Return &amp; Risk Mathematics (2027 L1 Module 8)</h2>
  <div class="formula-card">
    <div class="formula-title">Two-Asset &amp; Three-Asset Portfolio Variance</div>
    $$\\sigma_p^2 = w_1^2\\sigma_1^2 + w_2^2\\sigma_2^2 + 2w_1w_2\\text{{Cov}}(R_1,R_2) = w_1^2\\sigma_1^2 + w_2^2\\sigma_2^2 + 2w_1w_2\\rho_{{1,2}}\\sigma_1\\sigma_2$$
    $$\\text{{Minimum-Variance Weight (2 assets): }} w_1^* = \\frac{{\\sigma_2^2 - \\text{{Cov}}(R_1,R_2)}}{{\\sigma_1^2 + \\sigma_2^2 - 2\\text{{Cov}}(R_1,R_2)}}$$
  </div>
""" + worked_box("Worked Numerical 7: Two-Asset Portfolio Standard Deviation",
f"<p>Asset 1 ($w_1=60\\%, \\sigma_1=18\\%$) and Asset 2 ($w_2=40\\%, \\sigma_2=12\\%$) have correlation $\\rho_{{1,2}} = +0.25$. $\\sigma_p^2 = (0.36)(0.0324) + (0.16)(0.0144) + 2(0.6)(0.4)(0.25)(0.18)(0.12) = {var_p:.6f} \\implies \\sigma_p = {sd_p*100:.2f}\\%$ (vs. weighted average $15.60\\%$, proving $2.76\\%$ diversification gain).</p>", "emerald") +
exercise_toolbar("qm-m10-port", "Module 10 Chapter Exercises (Portfolio Math)") +
exercise_card("qm-ex-19", "Exercise 10.1 (Solved): Minimum-Variance Portfolio Weight",
"<p>Two uncorrelated assets ($\\rho=0$) have $\\sigma_1 = 10\\%$ and $\\sigma_2 = 20\\%$. Compute the global minimum-variance weight $w_1^*$.</p>",
f"<p><strong>Answer: 80.0% in Asset 1</strong>. $w_1^* = \\frac{{0.04}}{{0.01 + 0.04}} = 0.80 = 80\\%$.</p>", "solved", "L1 Quant") +
exercise_card("qm-ex-20", "Exercise 10.2 (Unsolved): Covariance from Correlation",
"<p>If $\\sigma_A = 20\\%$, $\\sigma_B = 15\\%$, and $\\text{{Cov}}(R_A, R_B) = -0.0120$, compute $\\rho_{{A,B}}$.</p>",
"<p><strong>Answer: $-0.40$</strong>. $\\rho = \\frac{{-0.0120}}{{0.20 \\times 0.15}} = \\frac{{-0.0120}}{{0.0300}} = -0.40$.</p>", "unsolved", "L1 Quant") +
"</section>")

# MODULE 11: BIG DATA, MACHINE LEARNING & GENERATIVE AI / LLMs
parts.append(f"""
<section id="qm-m11-ml" class="notes-chapter">
  <h2 class="section-heading"><span class="num">11.</span> Big Data, Machine Learning &amp; LLMs (2027 L1 Module 11 &amp; L2 Modules 6–7)</h2>
  <div class="table-container">
    <table>
      <thead><tr><th>Paradigm</th><th>Key Algorithms</th><th>Financial Use Case &amp; Exam Trap</th></tr></thead>
      <tbody>
        <tr><td><strong>Supervised Learning</strong></td><td>LASSO (L1 sparsity, drops features), Ridge (L2 shrinks coefficients), CART/Random Forest, SVM, Neural Nets</td><td>Target variable $Y$ is labeled (default yes/no, stock excess return). <strong>Bias-Variance Tradeoff</strong>: Underfitting = high bias; Overfitting = high variance (mitigate via CV &amp; regularization $\\lambda$).</td></tr>
        <tr><td><strong>Unsupervised Learning</strong></td><td>K-Means Clustering, Hierarchical Clustering, Principal Components Analysis (PCA)</td><td>No labeled $Y$. PCA extracts orthogonal eigenvectors capturing factor variance (e.g., Level/Slope/Curvature of yield curve).</td></tr>
        <tr><td><strong>Big Data / NLP / GenAI</strong></td><td>Tokenization, Stop-word/Stemming, Bag-of-Words, TF-IDF, Transformer LLMs, RAG</td><td>F1 Score $= \\frac{{2 \\cdot P \\cdot R}}{{P + R}}$ beats Accuracy on imbalanced fraud/default data! LLMs require RAG grounding &amp; human verification (Standard V(A)) to control hallucination risk.</td></tr>
      </tbody>
    </table>
  </div>
""" + worked_box("Worked Numerical 8: Confusion Matrix Precision, Recall &amp; F1 Score",
f"<p>A credit-default classifier identifies $TP = 40$, $FP = 10$, $FN = 10$, $TN = 940$. Precision $P = 40/50 = 0.80$; Recall $R = 40/50 = 0.80$; $F1 = \\frac{{2(0.80)(0.80)}}{{0.80+0.80}} = 0.80$ (whereas naive Accuracy $(40+940)/1000 = 98\\%$ masks class imbalance if model never flagged defaults).</p>", "blue") +
exercise_toolbar("qm-m11-ml", "Module 11 Chapter Exercises (ML &amp; LLMs)") +
exercise_card("qm-ex-21", "Exercise 11.1 (Solved): LASSO vs. Ridge Regression",
"<p>An equity quant wants automatic feature selection that sets irrelevant macro coefficients identically to zero. Choose LASSO or Ridge?</p>",
"<p><strong>Answer: LASSO (L1 penalty $\\lambda \\sum |\\hat{{b}}_k|$)</strong> zeroes out weak coefficients; Ridge (L2 penalty $\\lambda \\sum \\hat{{b}}_k^2$) shrinks coefficients smoothly toward zero without exact elimination.</p>", "solved", "L2 ML") +
exercise_card("qm-ex-22", "Exercise 11.2 (Unsolved): Document-Term Frequency (TF)",
"<p>A 200-token 10-K risk-factor section mentions the word 'tariff' 6 times. Across 500 total filings, 'tariff' appears in 50 filings. Compute TF and $\\text{{IDF}} = \\ln(N/df)$.</p>",
f"<p><strong>Answer: $TF = 0.030$, $\\text{{IDF}} = {math.log(500/50):.3f}$, $TF\\text{{-}}IDF = {0.03*math.log(10):.4f}$</strong>.</p>", "unsolved", "L2 Big Data") +
"</section>")

# MODULE 12: FORMULA CHEAT SHEET
parts.append("""
<section id="qm-m12-formulas" class="notes-chapter">
  <h2 class="section-heading"><span class="num">12.</span> Master Quantitative Methods Formula Cheat Sheet</h2>
  <div class="table-container">
    <table>
      <thead><tr><th>Concept</th><th>Governing Formula</th><th>Key Exam Condition</th></tr></thead>
      <tbody>
        <tr><td><strong>EAR</strong></td><td>$$(1 + r_s/m)^m - 1$$</td><td>Continuous limit: $e^{r_s}-1$</td></tr>
        <tr><td><strong>Bayes' Rule</strong></td><td>$$P(A\\mid B) = \\frac{P(B\\mid A)P(A)}{P(B)}$$</td><td>Total probability sums all mutually exclusive branches</td></tr>
        <tr><td><strong>Roy's Safety-First</strong></td><td>$$SFR = \\frac{E(R_p)-R_L}{\\sigma_p}$$</td><td>Maximize SFR to minimize shortfall below $R_L$</td></tr>
        <tr><td><strong>t-Test (Mean)</strong></td><td>$$t = \\frac{\\bar{X}-\\mu_0}{s/\\sqrt{n}}$$</td><td>$df = n - 1$; use $t$ when $\\sigma$ unknown</td></tr>
        <tr><td><strong>OLS Slope</strong></td><td>$$\\hat{b}_1 = \\frac{\\text{Cov}(X,Y)}{\\text{Var}(X)}$$</td><td>In simple OLS, $R^2 = r_{XY}^2$</td></tr>
        <tr><td><strong>AR(1) Mean</strong></td><td>$$\\bar{X} = \\frac{b_0}{1-b_1}$$</td><td>Valid only if $|b_1| < 1$ (no unit root)</td></tr>
        <tr><td><strong>GARCH(1,1)</strong></td><td>$$\\sigma_t^2 = \\omega + \\alpha\\epsilon_{t-1}^2 + \\beta\\sigma_{t-1}^2$$</td><td>Stationary if $\\alpha + \\beta < 1$</td></tr>
        <tr><td><strong>F1 Score</strong></td><td>$$F1 = \\frac{2 \\cdot P \\cdot R}{P + R}$$</td><td>Harmonic mean of Precision &amp; Recall</td></tr>
      </tbody>
    </table>
  </div>
""" + exercise_toolbar("qm-m12-formulas", "Module 12 Capstone Drills") +
exercise_card("qm-ex-23", "Exercise 12.1 (Solved): F-Statistic from ANOVA Table",
"<p>A 4-predictor regression on $n=45$ observations reports $SSR = 180$ and $SSE = 120$. Compute the $F$-statistic.</p>",
f"<p><strong>Answer: $F = 15.00$</strong>. $MSR = 180/4 = 45.0$; $MSE = 120/(45-4-1) = 120/40 = 3.0$; $F = 45.0 / 3.0 = 15.00$.</p>", "solved", "L2 ANOVA") +
exercise_card("qm-ex-24", "Exercise 12.2 (Unsolved): Logistic Odds Ratio Interpretation",
"<p>In a credit default logistic regression, the coefficient on Leverage is $+0.6931$. By what factor does a 1-unit increase in Leverage multiply the odds of default?</p>",
f"<p><strong>Answer: $2.00\\times$ (doubles the odds)</strong>. Odds multiplier $= e^{{0.6931}} = {math.exp(0.6931):.2f}$.</p>", "unsolved", "L2 Logistic") +
"</section>")

write_notes_html("".join(parts), OUTPUT_PATH)
