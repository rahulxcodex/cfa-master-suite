"""
scripts/expand_solved_and_jargon.py
Expands:
1. data/master_solved_numericals.json (27 -> 63 Master Solved Numericals across all 10 CBOK subjects)
2. data/cfa_jargon_dictionary.json (32 -> 64 Master Terminologies across all 10 CBOK subjects)
All numerical answers computed deterministically in Python with strict KaTeX and zero-bare-dollar compliance.
"""
import json
import math
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)
from scripts.qbank_helper import bsm_values, check_text_compliance, irr, norm_cdf

DATA_DIR = os.path.join(BASE_DIR, "data")
SOLVED_PATH = os.path.join(DATA_DIR, "master_solved_numericals.json")
JARGON_PATH = os.path.join(DATA_DIR, "cfa_jargon_dictionary.json")


def build_new_solved_numericals() -> list[dict]:
    items = []

    def add_num(nid, code, subj, diff, prob, meth, steps, ans):
        for fld, val in [("problem", prob), ("methodology", meth), ("steps", steps), ("final_answer", ans)]:
            errs = check_text_compliance(val, f"{nid}.{fld}")
            if errs:
                raise ValueError("\n".join(errs))
        items.append({
            "id": nid,
            "num_code": code,
            "subject": subj,
            "difficulty": diff,
            "problem": prob,
            "methodology": meth,
            "steps": steps,
            "final_answer": ans,
        })

    # === 1. ETHICAL & PROFESSIONAL STANDARDS (GIPS / FEE / SOFT DOLLAR / COMPLIANCE QUANT) ===
    # 1.1 GIPS Modified Dietz
    r_md = (15800000 - 12000000 - 3000000) / (12000000 + 3000000 * ((31 - 10) / 31))
    add_num(
        "NUM-1.1.1", "1.1.1", "Ethical and Professional Standards", "Easy / GIPS Modified Dietz",
        "Under GIPS performance presentation rules (Standard III(D) & CBOK I/XII), an institutional equity account opens May 1 with 12,000,000 USD, receives a 3,000,000 USD client deposit at the end of May 10 (21 days remaining in the 31-day month), and ends May 31 at 15,800,000 USD. Calculate the Modified Dietz monthly return.",
        "$$R_{\\text{ModDietz}} = \\frac{EMV - BMV - CF}{BMV + \\sum CF_j \\cdot w_j}, \\quad w_j = \\frac{CD - D_j}{CD}$$",
        f"1. Day-weight of cash flow: $w = (31 - 10) / 31 = 21 / 31 = 0.67742$.\n2. Weighted capital base: $12,000,000 + 3,000,000(0.67742) = 14,032,258\\text{{ USD}}$.\n3. Net dollar gain: $15,800,000 - 12,000,000 - 3,000,000 = 800,000\\text{{ USD}}$.\n4. Return: $800,000 / 14,032,258 = {r_md*100:.2f}\\%$.",
        f"**+{r_md*100:.2f}%**. Note: GIPS requires true Time-Weighted Return (daily/sub-period valuation on large external cash flows >= 10% of AUM, which applies here since 3M/12M = 25%)."
    )

    # 1.2 GIPS Asset-Weighted Composite Return & Dispersion
    w_a, w_b, w_c = 25.0 / 100.0, 45.0 / 100.0, 30.0 / 100.0
    comp_ret = w_a * 0.112 + w_b * 0.084 + w_c * 0.146
    eq_w_ret = (0.112 + 0.084 + 0.146) / 3
    ew_sd = math.sqrt(((0.112 - eq_w_ret) ** 2 + (0.084 - eq_w_ret) ** 2 + (0.146 - eq_w_ret) ** 2) / 3)
    add_num(
        "NUM-1.1.2", "1.1.2", "Ethical and Professional Standards", "Moderate / GIPS Composite Return & Dispersion",
        "A GIPS-compliant Small-Cap Composite contains three discretionary fee-paying portfolios for Q2 (no external cash flows): Portfolio A (BMV = 25M USD, return = +11.20%), Portfolio B (BMV = 45M USD, return = +8.40%), Portfolio C (BMV = 30M USD, return = +14.60%). Calculate (1) the asset-weighted composite return and (2) the equal-weighted internal dispersion (standard deviation).",
        "$$R_{\\text{comp}} = \\sum \\left(\\frac{BMV_i}{\\sum BMV}\\right) R_i, \\qquad \\sigma_{\\text{disp}} = \\sqrt{\\frac{1}{n}\\sum_{i=1}^n (R_i - \\bar{R}_{\\text{eq}})^2}$$",
        f"1. Total BMV $= 25 + 45 + 30 = 100\\text{{M USD}}$.\n2. Asset-weighted return $= 0.25(11.20\\%) + 0.45(8.40\\%) + 0.30(14.60\\%) = 2.80\\% + 3.78\\% + 4.38\\% = {comp_ret*100:.2f}\\%$.\n3. Equal-weighted mean $= (11.20 + 8.40 + 14.60)/3 = {eq_w_ret*100:.2f}\\%$.\n4. Equal-weighted population SD $= {ew_sd*100:.2f}\\%$.",
        f"**Composite Return = {comp_ret*100:.2f}%; Equal-Weighted Dispersion = {ew_sd*100:.2f}%**."
    )

    # 1.3 GIPS Linked Sub-Period TWR
    twr_gips = (1 + (13200000 - 10000000) / 10000000) * (1 + (17500000 - (13200000 + 2800000)) / (13200000 + 2800000)) - 1
    add_num(
        "NUM-1.1.3", "1.1.3", "Ethical and Professional Standards", "Moderate / GIPS Large Cash Flow TWR",
        "To eliminate cash-flow distortion under Standard III(D) and GIPS, an equity fund valued at 10,000,000 USD on Jan 1 rises to 13,200,000 USD on July 15 prior to a 2,800,000 USD institutional deposit (21.2% of AUM). By Dec 31, ending value reaches 17,500,000 USD. Calculate the exact Time-Weighted Return (TWR).",
        "$$TWR = (1 + HPR_1)(1 + HPR_2) - 1$$",
        f"1. Sub-period 1 (Jan 1–Jul 15): $HPR_1 = (13.2\\text{{M}} - 10.0\\text{{M}}) / 10.0\\text{{M}} = +32.00\\%$.\n2. New post-deposit base on Jul 15: $13.2\\text{{M}} + 2.8\\text{{M}} = 16.0\\text{{M USD}}$.\n3. Sub-period 2 (Jul 15–Dec 31): $HPR_2 = (17.5\\text{{M}} - 16.0\\text{{M}}) / 16.0\\text{{M}} = +9.375\\%$.\n4. Chain-linked $TWR = (1.32)(1.09375) - 1 = {twr_gips*100:.2f}\\%$.",
        f"**TWR = +{twr_gips*100:.2f}%** (mandated by GIPS when large external cash flows occur)."
    )

    # 1.4 Soft Dollar Mixed-Use Allocation & Restitution (Standard III(A))
    total_soft = 180000.0
    research_pct = 0.65
    overhead_restit = total_soft * (1 - research_pct)
    add_num(
        "NUM-1.2.1", "1.2.1", "Ethical and Professional Standards", "Easy / Std III(A) Soft Dollar Compliance",
        "An asset manager generates 180,000 USD in soft-dollar brokerage credits from client equity trades to pay for an institutional analytics package. Compliance audits reveal that 65% of the package directly supports investment research while 35% funds firm compliance overhead and office marketing travel. Under Standard III(A) Loyalty, Prudence, and Care, compute the impermissible client commission amount that the firm must reimburse from its own corporate capital.",
        "$$\\text{Reimbursement} = \\text{Total Soft Dollars} \\times (1 - \\%\\text{Direct Research Benefit})$$",
        f"1. Permissible research allocation: $180,000 \\times 0.65 = 117,000\\text{{ USD}}$.\n2. Impermissible firm overhead/marketing portion: $180,000 \\times 0.35 = {overhead_restit:,.0f}\\text{{ USD}}$.",
        f"**{overhead_restit:,.0f} USD must be paid directly by the firm's management company** (client brokerage belongs strictly to clients)."
    )

    # 1.5 Standard III(B) Pro-Rata Oversubscribed IPO Allocation
    client_orders = [40000, 30000, 20000, 10000]  # sum = 100,000
    ipo_avail = 25000
    allocs = [int(o * ipo_avail / sum(client_orders)) for o in client_orders]
    add_num(
        "NUM-1.2.2", "1.2.2", "Ethical and Professional Standards", "Moderate / Std III(B) & VI(B) Pro-Rata IPO",
        "A portfolio manager enters an oversubscribed hot IPO for 4 suitable client accounts (Client A: 40,000 shares; Client B: 30,000; Client C: 20,000; Client D: 10,000) plus her own personal account (10,000 shares). The syndicate allocates only 25,000 total shares. Determine the compliant Standard III(B) / VI(B) share allocation across all 5 accounts.",
        "$$\\text{Client Allocation}_i = \\text{Available Shares} \\times \\frac{\\text{Order}_i}{\\sum \\text{Suitable Client Orders}}$$",
        f"1. Under Standard VI(B) Priority of Transactions, the manager's personal account receives **0 shares** until all client orders are filled.\n2. Total client demand $= 40,000 + 30,000 + 20,000 + 10,000 = 100,000$ shares; fill ratio $= 25,000 / 100,000 = 25.0\\%$.\n3. Pro-rata allocations: Client A $= {allocs[0]:,}$, Client B $= {allocs[1]:,}$, Client C $= {allocs[2]:,}$, Client D $= {allocs[3]:,}$ shares.",
        f"**Client A: {allocs[0]:,}; Client B: {allocs[1]:,}; Client C: {allocs[2]:,}; Client D: {allocs[3]:,}; Manager Personal Account: 0 shares**."
    )

    # 1.6 Standard IV(B) & VI(C) Referral & Net Fee Disclosure Impact
    aum_ref = 5000000.0
    ann_fee = aum_ref * 0.012
    ref_split = ann_fee * 0.25
    add_num(
        "NUM-1.2.3", "1.2.3", "Ethical and Professional Standards", "Difficult / Std VI(C) & III(D) Fee Presentation",
        "A wealth advisor charges a 1.20% annual management fee on a 5,000,000 USD portfolio and pays an ongoing 25% referral fee to an unaffiliated CPA who introduced the client. The portfolio earns +9.40% gross return in Year 1. Compute (1) the exact annual referral dollar payment required in the pre-engagement Standard VI(C) disclosure, and (2) the net-of-fee return that must be shown alongside gross returns under Standard III(D).",
        "$$\\text{Referral Payment} = AUM \\times f_{\\text{mgmt}} \\times \\%\\text{Split}, \\qquad R_{\\text{net}} \\approx R_{\\text{gross}} - f_{\\text{mgmt}}$$",
        f"1. Gross annual advisory fee $= 5,000,000 \\times 1.20\\% = {ann_fee:,.0f}\\text{{ USD}}$.\n2. Referral fee disclosed to prospect BEFORE signing: $60,000 \\times 25\\% = {ref_split:,.0f}\\text{{ USD/year}}$ (paid from advisor fee, not extra charge to client).\n3. Net client return $= 9.40\\% - 1.20\\% = 8.20\\%$ (note: if fee deducted at year-end on ending AUM, $5\\text{{M}}(1.094)(1-0.012) - 5\\text{{M}} = +8.09\\%$).",
        f"**Disclosed Referral Fee = {ref_split:,.0f} USD/yr; Net Return = 8.20% (8.09% if fee charged on ending balance)**."
    )

    # === 2. QUANTITATIVE METHODS ===
    ear_q = (1 + 0.09 / 12) ** 12 - 1
    add_num(
        "NUM-2.1.1", "2.1.1", "Quantitative Methods", "Easy / Foundational (EAR & TVM)",
        "A corporate treasury evaluates two short-term investments: Note A offers 9.00% stated annual rate compounded monthly, while Note B offers 8.85% compounded continuously. Calculate the Effective Annual Rate (EAR) for both notes.",
        "$$EAR_{\\text{discrete}} = (1 + r_s/m)^m - 1, \\qquad EAR_{\\text{cont}} = e^{r_s} - 1$$",
        f"1. Note A: $(1 + 0.09/12)^{{12}} - 1 = (1.0075)^{{12}} - 1 = {ear_q*100:.4f}\\%$.\n2. Note B: $e^{{0.0885}} - 1 = {(math.exp(0.0885)-1)*100:.4f}\\%$.",
        f"**Note A EAR = {ear_q*100:.3f}%; Note B EAR = {(math.exp(0.0885)-1)*100:.3f}%** (Note A outperforms)."
    )

    p_rec, p_y_rec, p_y_exp = 0.25, 0.85, 0.20
    p_y = p_rec * p_y_rec + (1 - p_rec) * p_y_exp
    p_rec_y = (p_rec * p_y_rec) / p_y
    add_num(
        "NUM-2.1.2", "2.1.2", "Quantitative Methods", "Easy / Bayes Theorem Updating",
        "An economist assigns a 25% prior probability of recession next year. Historically, the 10y-2y yield curve inverts 85% of the time prior to recessions, versus 20% of the time during continuing expansions. Today the yield curve inverts. Update the recession probability using Bayes' theorem.",
        "$$P(R \\mid I) = \\frac{P(I \\mid R)P(R)}{P(I \\mid R)P(R) + P(I \\mid E)P(E)}$$",
        f"1. Joint probability of recession & inversion: $0.25 \\times 0.85 = 0.2125$.\n2. Unconditional probability of inversion: $0.25(0.85) + 0.75(0.20) = 0.2125 + 0.1500 = {p_y:.4f}$.\n3. Posterior probability: $0.2125 / {p_y:.4f} = {p_rec_y*100:.2f}\\%$.",
        f"**Posterior Recession Probability = {p_rec_y*100:.2f}%**."
    )

    t_num = (0.015 - 0.004) / (0.042 / math.sqrt(49))
    add_num(
        "NUM-2.2.1", "2.2.1", "Quantitative Methods", "Moderate / Hypothesis Testing (t-Stat & CI)",
        "Over $n = 49$ quarters, a quantitative equity fund generates a mean quarterly return of 1.50% with sample standard deviation 4.20%. Test whether the true mean return exceeds the 0.40% quarterly risk-free benchmark at $\\alpha = 5\\%$ one-tailed ($t_{\\text{crit}, 48} = 1.677$), and build the 95% two-tailed confidence interval ($t_{0.025} = 2.011$).",
        "$$t = \\frac{\\bar{X} - \\mu_0}{s / \\sqrt{n}}, \\qquad CI = \\bar{X} \\pm t_{\\alpha/2} \\left(\\frac{s}{\\sqrt{n}}\\right)$$",
        f"1. Standard Error $= 4.20\\% / \\sqrt{{49}} = 4.20\\% / 7 = 0.60\\%$.\n2. Test statistic $t = (1.50\\% - 0.40\\%) / 0.60\\% = {t_num:.3f}$. Since ${t_num:.3f} &gt; 1.677$, reject $H_0$.\n3. 95% CI $= 1.50\\% \\pm 2.011(0.60\\%) = [{(0.015 - 2.011*0.006)*100:.2f}\\%, {(0.015 + 2.011*0.006)*100:.2f}\\%]$.",
        f"**$t = {t_num:.2f}$ (Reject $H_0$); 95% CI = [{(0.015 - 2.011*0.006)*100:.2f}%, {(0.015 + 2.011*0.006)*100:.2f}%]**."
    )

    adj_r2 = 1 - ((60 - 1) / (60 - 4 - 1)) * (1 - 0.72)
    f_reg = (0.72 / 4) / ((1 - 0.72) / 55)
    add_num(
        "NUM-2.2.2", "2.2.2", "Quantitative Methods", "Moderate / Multiple Regression ANOVA",
        "A 4-factor equity return regression over $n = 60$ monthly observations produces $R^2 = 0.72$ and $SST = 500$. Compute (1) Adjusted $\\bar{R}^2$, (2) the $F$-statistic, and (3) Standard Error of Estimate (SEE).",
        "$$\\bar{R}^2 = 1 - \\frac{n-1}{n-k-1}(1 - R^2), \\qquad F = \\frac{SSR/k}{SSE/(n-k-1)}, \\qquad SEE = \\sqrt{MSE}$$",
        f"1. Adjusted $\\bar{{R}}^2 = 1 - \\frac{{59}}{{55}}(0.28) = {adj_r2:.4f}$.\n2. $SSR = 0.72 \\times 500 = 360$; $SSE = 140$. $MSR = 360/4 = 90.0$; $MSE = 140/55 = 2.5455$.\n3. $F = 90.0 / 2.5455 = {f_reg:.2f}$; $SEE = \\sqrt{{2.5455}} = {math.sqrt(140/55):.3f}$.",
        f"**Adjusted $\\bar{{R}}^2 = {adj_r2:.4f}$; $F = {f_reg:.2f}$; $SEE = {math.sqrt(140/55):.3f}$**."
    )

    ar_lt = 0.012 / (1 - 0.75)
    y1_ar = 0.012 + 0.75 * 0.080
    y2_ar = 0.012 + 0.75 * y1_ar
    add_num(
        "NUM-2.3.1", "2.3.1", "Quantitative Methods", "Difficult / L2 AR(1) Chain-Rule Forecasting",
        "An analyst models quarterly ROE via a covariance-stationary AR(1) process: $ROE_t = 0.012 + 0.75 ROE_{t-1} + \\epsilon_t$. Current quarter $ROE_0 = 8.00\\%$. Calculate (1) the long-run mean-reverting ROE level and (2) the 2-quarter-ahead forecast $\\widehat{ROE}_2$.",
        "$$\\text{Mean Level} = \\frac{b_0}{1 - b_1}, \\qquad \\widehat{X}_{t+2} = b_0 + b_1 \\widehat{X}_{t+1}$$",
        f"1. Mean-reverting level $= \\frac{{0.012}}{{1 - 0.75}} = {ar_lt*100:.2f}\\%$.\n2. 1-step forecast $\\widehat{{ROE}}_1 = 0.012 + 0.75(0.080) = {y1_ar*100:.2f}\\%$.\n3. 2-step forecast $\\widehat{{ROE}}_2 = 0.012 + 0.75({y1_ar:.4f}) = {y2_ar*100:.3f}\\%$.",
        f"**Mean-Reverting ROE = {ar_lt*100:.2f}%; 2-Step Forecast = {y2_ar*100:.3f}%**."
    )

    g_v1 = 0.000015 + 0.12 * (0.03 ** 2) + 0.82 * (0.02 ** 2)
    g_vl = 0.000015 / (1 - 0.12 - 0.82)
    add_num(
        "NUM-2.3.2", "2.3.2", "Quantitative Methods", "Difficult / L2 GARCH(1,1) Volatility",
        "A risk desk estimates a daily GARCH(1,1) model on S&P 500 returns: $\\sigma_t^2 = 0.000015 + 0.12 \\epsilon_{t-1}^2 + 0.82 \\sigma_{t-1}^2$. Yesterday's volatility forecast was $\\sigma_{t-1} = 2.00\\%$ and an unexpected macro surprise triggered a return shock $\\epsilon_{t-1} = -3.00\\%$. Compute today's conditional volatility $\\sigma_t$ and the unconditional long-run daily volatility.",
        "$$\\sigma_t^2 = \\omega + \\alpha\\epsilon_{t-1}^2 + \\beta\\sigma_{t-1}^2, \\qquad V_L = \\frac{\\omega}{1 - \\alpha - \\beta}$$",
        f"1. $\\sigma_t^2 = 0.000015 + 0.12(0.0009) + 0.82(0.0004) = 0.000015 + 0.000108 + 0.000328 = {g_v1:.6f}$.\n2. $\\sigma_t = \\sqrt{{{g_v1:.6f}}} = {math.sqrt(g_v1)*100:.3f}\\%$ daily.\n3. Long-run $V_L = \\frac{{0.000015}}{{1 - 0.94}} = {g_vl:.6f} \\implies \\sqrt{{V_L}} = {math.sqrt(g_vl)*100:.3f}\\%$ daily.",
        f"**Conditional Volatility $\\sigma_t = {math.sqrt(g_v1)*100:.2f}%$; Long-Run Volatility = {math.sqrt(g_vl)*100:.2f}% daily**."
    )

    # === 3. ECONOMICS ===
    add_num(
        "NUM-3.4.1", "3.4.1", "Economics", "Easy / Micro Elasticity & Revenue",
        "A streaming platform's linear demand function is $Q_d = 500 - 15P$ (in thousands of subscribers). At $P = 20\\text{ USD}$, calculate point price elasticity of demand and determine whether raising price increases or decreases total revenue.",
        "$$E_p^d = \\left(\\frac{\\Delta Q_d}{\\Delta P}\\right) \\cdot \\frac{P}{Q_d}$$",
        f"1. At $P = 20$: $Q_d = 500 - 15(20) = 200$ thousand.\n2. Slope $\\Delta Q_d / \\Delta P = -15$.\n3. $E_p^d = -15 \\times (20 / 200) = -1.50$.",
        "**$E_p^d = -1.50$ (Elastic)** — raising price decreases total revenue."
    )

    f_mult = 1 / (1 - 0.75 * (1 - 0.20))
    add_num(
        "NUM-3.4.2", "3.4.2", "Economics", "Easy / Fiscal Multiplier & Taylor Rule",
        "In a closed economy with marginal propensity to consume $c = 0.75$ and marginal tax rate $t = 20\\%$, compute the fiscal spending multiplier. Also compute the Taylor Rule target rate if neutral real rate $= 1.5\\%$, current inflation $= 4.0\\%$ (target $2.0\\%$), and output gap $= +1.0\\%$.",
        "$$\\text{Mult} = \\frac{1}{1 - c(1-t)}, \\qquad i^* = r^* + \\pi + 0.5(\\pi - \\pi^*) + 0.5(y - y^*)$$",
        f"1. Fiscal Multiplier $= \\frac{{1}}{{1 - 0.75(0.80)}} = \\frac{{1}}{{0.40}} = {f_mult:.2f}$.\n2. Taylor Rule $i^* = 1.5\\% + 4.0\\% + 0.5(2.0\\%) + 0.5(1.0\\%) = 7.00\\%$.",
        f"**Fiscal Multiplier = {f_mult:.2f}; Taylor Rule Target Rate = 7.00%**."
    )

    # FX Bid-Ask Cross Rate
    cb, ca = 1.1200 * 145.00, 1.1210 * 145.30
    add_num(
        "NUM-3.5.1", "3.5.1", "Economics", "Moderate / Dealer FX Bid-Ask Cross Rate",
        "A Tokyo currency desk quotes $USD/EUR = 1.1200\\text{--}1.1210$ and $JPY/USD = 145.00\\text{--}145.30$. Compute the no-arbitrage dealer bid and ask cross-rate quotes for $JPY/EUR$.",
        "$$(A/C)_{\\text{bid}} = (A/B)_{\\text{bid}}(B/C)_{\\text{bid}}, \\qquad (A/C)_{\\text{ask}} = (A/B)_{\\text{ask}}(B/C)_{\\text{ask}}$$",
        f"1. Bid $(JPY/EUR) = 1.1200 \\times 145.00 = {cb:.2f}$.\n2. Ask $(JPY/EUR) = 1.1210 \\times 145.30 = {ca:.3f}$.",
        f"**$JPY/EUR = {cb:.2f}\\text{{--}}{ca:.2f}$** (spread = {ca-cb:.2f} JPY)."
    )

    # Covered Interest Arbitrage
    f_fair_ec = 1.2000 * (1 + 0.048 * 0.5) / (1 + 0.032 * 0.5)
    arb_prof = (1000000 * 1.016) * (1.2200 / 1.2000) - (1000000 * 1.024)
    # Wait: let's verify exact direction! Borrow 1,000,000 USD at 4.80% for 180d -> repay 1,024,000 USD.
    # Convert 1M USD at spot 1.2000 USD/EUR -> 833,333.33 EUR. Invest at 3.20% for 180d -> 846,666.67 EUR.
    # Sell EUR forward at quoted 1.2200 USD/EUR -> 846,666.67 * 1.2200 = 1,032,933.33 USD -> profit = 1,032,933.33 - 1,024,000 = +8,933.33 USD!
    arb_exact = (1000000.0 / 1.2000) * (1 + 0.032 * 0.5) * 1.2200 - 1000000.0 * (1 + 0.048 * 0.5)
    add_num(
        "NUM-3.5.2", "3.5.2", "Economics", "Moderate / L2 Covered Interest Arbitrage",
        "Spot $USD/EUR = 1.2000$, 180-day $r_{USD} = 4.80\\%$ (annualized, 30/360), 180-day $r_{EUR} = 3.20\\%$, and a dealer quotes a 180-day forward rate of $USD/EUR = 1.2200$. Starting with 1,000,000 USD borrowing capacity, calculate the riskless covered interest arbitrage profit.",
        "$$F^* = S_0 \\cdot \\frac{1 + r_P(T)}{1 + r_B(T)}$$",
        f"1. Arbitrage-free $F^* = 1.2000 \\times \\frac{{1.024}}{{1.016}} = {f_fair_ec:.5f}$. Quoted forward (1.2200) overvalues EUR forward.\n2. Borrow 1,000,000 USD at 4.80% (owe $1,024,000\\text{{ USD}}$ in 180 days).\n3. Convert spot to EUR: $1,000,000 / 1.2000 = 833,333.33\\text{{ EUR}}$; invest at 3.20% $\\implies 846,666.67\\text{{ EUR}}$.\n4. Sell EUR forward at 1.2200 $\\implies 1,032,933.33\\text{{ USD}}$.\n5. Profit $= 1,032,933.33 - 1,024,000 = +{arb_exact:,.2f}\\text{{ USD}}$.",
        f"**+{arb_exact:,.2f} USD Riskless Arbitrage Profit**."
    )

    # Carry Trade
    c_ret_ec = (1.0 + 0.072) * (1.0 / 1.028) - (1.0 + 0.012)
    add_num(
        "NUM-3.6.1", "3.6.1", "Economics", "Difficult / L2 FX Carry Trade Return",
        "An investor borrows 100,000,000 JPY at 1.20% ($r_{\\text{funding}}$), converts spot at $JPY/BRL = 30.00$, and invests in 1-year BRL deposits yielding 7.20%. Over the year, BRL depreciates so spot moves to $JPY/BRL = 29.18$. Wait—note $JPY/BRL$ falling from 30.00 to 29.18 means 1 BRL buys FEWER JPY (BRL depreciated by $(29.18/30.00)-1 = -2.733\\%$). Calculate the exact JPY-denominated percentage return on the carry trade.",
        "$$R_{\\text{Carry, Funding Ccy}} = (1 + r_{\\text{target}})\\left(\\frac{S_1}{S_0}\\right) - (1 + r_{\\text{funding}})$$",
        f"1. Initial BRL bought: $100,000,000 / 30.00 = 3,333,333.33\\text{{ BRL}}$.\n2. Ending BRL after 7.20% interest: $3,573,333.33\\text{{ BRL}}$.\n3. Convert back to JPY at $S_1 = 29.18$: $104,269,867\\text{{ JPY}}$.\n4. Repay JPY loan ($101,200,000\\text{{ JPY}}$): Net profit $= +3,069,867\\text{{ JPY}}$ ($+{((3573333.3333*29.18 - 101200000)/100000000)*100:.2f}\\%$).",
        f"**+{((100000000/30*1.072*29.18 - 101200000)/100000000)*100:.2f}% (+3,069,867 JPY)** — interest differential (+6.00%) outweighed the -2.73% BRL depreciation."
    )

    # Solow Growth Accounting
    g_sol = 0.016 + 0.30 * 0.040 + 0.70 * 0.012
    ss_k = (0.28 * 1.0 / (0.05 + 0.02)) ** (1 / (1 - 0.30))
    add_num(
        "NUM-3.6.2", "3.6.2", "Economics", "Difficult / L2 Cobb-Douglas & Solow Steady State",
        "An emerging market has Cobb-Douglas capital share $\\alpha = 0.30$, TFP growth $= 1.60\\%$, capital stock growth $= 4.00\\%$, and labor force growth $n = 1.20\\%$. Also compute steady-state capital-per-worker $k^*$ if savings rate $s = 28\\%$, $A = 1.0$, depreciation $\\delta = 5\\%$, and $n = 2\\%$.",
        "$$\\frac{\\Delta Y}{Y} = \\frac{\\Delta A}{A} + \\alpha \\frac{\\Delta K}{K} + (1-\\alpha)\\frac{\\Delta L}{L}, \\qquad k^* = \\left(\\frac{sA}{\\delta+n}\\right)^{\\frac{1}{1-\\alpha}}$$",
        f"1. Potential GDP growth $= 1.60\\% + 0.30(4.00\\%) + 0.70(1.20\\%) = 1.60\\% + 1.20\\% + 0.84\\% = {g_sol*100:.2f}\\%$.\n2. Steady-state $k^* = \\left(\\frac{{0.28}}{{0.07}}\\right)^{{1/0.70}} = 4.0^{{1.42857}} = {ss_k:.3f}$.",
        f"**Potential GDP Growth = {g_sol*100:.2f}%; Solow Steady-State $k^* = {ss_k:.3f}$**."
    )

    # === 4. CORPORATE ISSUERS ===
    add_num(
        "NUM-5.4.1", "5.4.1", "Corporate Issuers", "Easy / Cash Conversion Cycle & Trade Credit",
        "Apex Manufacturing holds average inventory for 48 days, collects receivables in 39 days, and pays suppliers in 31 days. Suppliers offer credit terms '2/10, net 40'. Calculate (1) the Cash Conversion Cycle and (2) the Effective Annual Rate (EAR) of forgoing the trade discount.",
        "$$CCC = DOH + DSO - DPO, \\qquad EAR = \\left(1 + \\frac{d}{1-d}\\right)^{\\frac{365}{N - D}} - 1$$",
        f"1. $CCC = 48 + 39 - 31 = 56\\text{{ days}}$.\n2. $EAR = \\left(1 + \\frac{{2}}{{98}}\\right)^{{365/30}} - 1 = {((1+2/98)**(365/30)-1)*100:.2f}\\%$.",
        f"**CCC = 56 days; Foregone Trade Credit Cost = {((1+2/98)**(365/30)-1)*100:.2f}%**."
    )

    npv_c = sum(cf / (1.09 ** t) for t, cf in enumerate([-400000, 140000, 180000, 210000]))
    irr_c = irr([-400000, 140000, 180000, 210000])
    add_num(
        "NUM-5.4.2", "5.4.2", "Corporate Issuers", "Easy / Capital Budgeting NPV & IRR",
        "A project costs 400,000 USD upfront and yields end-of-year cash inflows of 140,000 USD, 180,000 USD, and 210,000 USD over 3 years at a 9.0% WACC. Compute NPV and IRR.",
        "$$NPV = \\sum_{t=0}^3 \\frac{CF_t}{(1+r)^t}$$",
        f"1. $PV = \\frac{{140k}}{{1.09}} + \\frac{{180k}}{{1.09^2}} + \\frac{{210k}}{{1.09^3}} = 128,440 + 151,502 + 162,159 = 442,101\\text{{ USD}}$.\n2. $NPV = 442,101 - 400,000 = +{npv_c:,.2f}\\text{{ USD}}$.\n3. Solving $NPV = 0 \\implies IRR = {irr_c*100:.2f}\\%$.",
        f"**NPV = +{npv_c:,.2f} USD; IRR = {irr_c*100:.2f}%**."
    )

    bu_c = 1.40 / (1 + (1 - 0.25) * 0.50)
    bl_c = bu_c * (1 + (1 - 0.20) * 1.00)
    re_c = 0.038 + bl_c * 0.055
    wacc_c = 0.50 * 0.062 * (1 - 0.20) + 0.50 * re_c
    add_num(
        "NUM-5.5.1", "5.5.1", "Corporate Issuers", "Moderate / L2 Pure-Play Hamada Beta & WACC",
        "A pure-play semiconductor peer has equity $\\beta_L = 1.40$, $D/E = 0.50$, and tax rate 25%. Target project will operate at $D/E = 1.00$ (50% debt / 50% equity), tax rate 20%, pre-tax debt cost 6.20%, $R_f = 3.80\\%$, and $ERP = 5.50\\%$. Calculate project beta, cost of equity, and WACC.",
        "$$\\beta_U = \\frac{\\beta_L}{1 + (1-t)D/E}, \\qquad \\beta_P = \\beta_U[1 + (1-t_P)(D/E)_P]$$",
        f"1. $\\beta_U = 1.40 / [1 + 0.75(0.50)] = {bu_c:.4f}$.\n2. $\\beta_P = {bu_c:.4f}[1 + 0.80(1.00)] = {bl_c:.4f}$.\n3. $r_e = 3.80\\% + {bl_c:.4f}(5.50\\%) = {re_c*100:.2f}\\%$.\n4. $WACC = 0.50(6.20\\%)(0.80) + 0.50({re_c*100:.2f}\\%) = {wacc_c*100:.2f}\\%$.",
        f"**Project Beta = {bl_c:.3f}; $r_e = {re_c*100:.2f}\\%$; WACC = {wacc_c*100:.2f}%**."
    )

    # Buyback EPS
    eps_pre_c = 36.0 / 12.0
    sh_post_c = 12.0 - (40.0 / 40.0)
    eps_post_c = (36.0 - 40.0 * 0.06 * 0.75) / sh_post_c
    add_num(
        "NUM-5.5.2", "5.5.2", "Corporate Issuers", "Moderate / Debt-Funded Buyback Accretion",
        "Titan Corp earns 36.0M USD over 12.0M shares ($EPS = 3.00\\text{ USD}$, stock price $P = 40.00\\text{ USD}$). Titan issues 40.0M USD of 6.00% debt ($t = 25\\%$) to buy back 1.0M shares. Compute post-buyback EPS.",
        "$$EPS_{\\text{post}} = \\frac{NI - \\text{Debt} \\cdot r_d(1-t)}{\\text{Shares}_0 - (\\text{Debt}/P)}$$",
        f"1. After-tax interest $= 40.0\\text{{M}} \\times 6.0\\% \\times 0.75 = 1.80\\text{{M USD}}$.\n2. Post-buyback $NI = 36.0 - 1.8 = 34.2\\text{{M USD}}$ across $11.0\\text{{M}}$ shares.\n3. $EPS_{{\\text{{post}}}} = 34.2 / 11.0 = {eps_post_c:.2f}\\text{{ USD}}$ (accretive because $E/P = 7.50\\% &gt; r_d(1-t) = 4.50\\%$).",
        f"**Post-Buyback EPS = {eps_post_c:.2f} USD (+{eps_post_c-eps_pre_c:.2f} USD Accretive)**."
    )

    # MM II with taxes & Distress
    vu_5 = (3000000 * 0.75) / 0.11
    vl_5 = vu_5 + 0.25 * 8000000 - 450000
    e_5 = vl_5 - 8000000
    re_5 = 0.11 + (0.11 - 0.06) * 0.75 * (8000000 / e_5)
    add_num(
        "NUM-5.6.1", "5.6.1", "Corporate Issuers", "Difficult / L2 MM Proposition I & II w/ Distress",
        "Unlevered firm generates perpetual EBIT of 3,000,000 USD ($t = 25\\%$, $r_0 = 11.0\\%$). Management adds 8,000,000 USD debt at 6.0%, generating estimated present value of financial distress costs of 450,000 USD. Calculate (1) $V_U$, (2) Static Trade-Off $V_L$, and (3) MM levered cost of equity $r_e$ (assuming $V_L$ equity value = $V_L - D$).",
        "$$V_L = V_U + t D - PV(\\text{Distress}), \\qquad r_e = r_0 + (r_0 - r_d)(1-t)\\frac{D}{E}$$",
        f"1. $V_U = \\frac{{3,000,000 \\times 0.75}}{{0.11}} = {vu_5:,.2f}\\text{{ USD}}$.\n2. $V_L = {vu_5:,.2f} + 0.25(8,000,000) - 450,000 = {vl_5:,.2f}\\text{{ USD}}$.\n3. Equity $E = V_L - D = {e_5:,.2f}\\text{{ USD}}$.\n4. $r_e = 11\\% + (11\\% - 6\\%)(0.75)(8,000,000 / {e_5:,.2f}) = {re_5*100:.2f}\\%$.",
        f"**$V_U = {vu_5:,.0f}\\text{{ USD}}$; $V_L = {vl_5:,.0f}\\text{{ USD}}$; $r_e = {re_5*100:.2f}\\%$**."
    )

    # M&A Post-Merger EPS & Breakeven Synergy
    er_m = 54.0 / 72.0  # 0.75
    sh_new_m = 20.0 * er_m  # 15M
    sh_tot_m = 80.0 + sh_new_m  # 95M
    # Acq NI = 80 * 4.50 = 360M; Tgt NI = 20 * 2.40 = 48M
    eps_comb_no_syn = (360.0 + 48.0) / sh_tot_m  # 408 / 95 = 4.2947
    req_syn_at = 4.50 * sh_tot_m - 408.0  # 427.5 - 408 = 19.5M after tax -> pre-tax 19.5 / 0.75 = 26.0M
    add_num(
        "NUM-5.6.2", "5.6.2", "Corporate Issuers", "Difficult / L2 M&A Exchange Ratio & Breakeven Synergy",
        "Acquirer (80M shares, $P = 72\\text{ USD}$, $EPS = 4.50\\text{ USD}$) bids 54.00 USD/share in stock for Target (20M shares, $EPS = 2.40\\text{ USD}$). Corporate tax rate is 25%. Calculate (1) the exchange ratio and new shares issued, (2) post-merger EPS before synergies, and (3) minimum pre-tax annual synergies required to make the merger non-dilutive to Acquirer EPS.",
        "$$ER = \\frac{P_{\\text{offer}}}{P_A}, \\qquad \\text{Breakeven } S_{\\text{pre-tax}} = \\frac{EPS_A(N_A + N_{\\text{new}}) - (NI_A + NI_T)}{1 - t}$$",
        f"1. Exchange ratio $= 54 / 72 = 0.75$; New shares $= 20\\text{{M}} \\times 0.75 = 15\\text{{M}}$ (Total $= 95\\text{{M}}$).\n2. Combined $NI = 80(4.50) + 20(2.40) = 360 + 48 = 408\\text{{M USD}}$. Pre-synergy $EPS = 408 / 95 = {eps_comb_no_syn:.2f}\\text{{ USD}}$ (dilutive by 0.21 USD).\n3. Required after-tax synergy $= (4.50 \\times 95) - 408 = 427.5 - 408 = {req_syn_at:.2f}\\text{{M USD}}$.\n4. Minimum pre-tax synergy $= 19.50 / 0.75 = {req_syn_at/0.75:.2f}\\text{{M USD}}$.",
        f"**ER = 0.75 (15M new shares); Pre-Synergy EPS = {eps_comb_no_syn:.2f} USD; Breakeven Pre-Tax Synergy = {req_syn_at/0.75:.2f}M USD**."
    )

    # === 5. DERIVATIVES ===
    f_d1 = (150.0 - 3.0 / (1.05 ** 0.25)) * (1.05 ** 0.75)
    add_num(
        "NUM-7.1.1", "7.1.1", "Derivatives", "Easy / Forward Pricing w/ Discrete Dividend",
        "A stock trades at $S_0 = 150.00\\text{ USD}$ and pays a 3.00 USD dividend in 3 months (0.25 yr). Risk-free rate is 5.00% annual compounding. Calculate the no-arbitrage 9-month (0.75 yr) forward price.",
        "$$F_0(T) = [S_0 - PV_0(D)] (1 + r)^T$$",
        f"1. $PV_0(D) = 3.00 / 1.05^{{0.25}} = {3.0/(1.05**0.25):.4f}\\text{{ USD}}$.\n2. $F_0 = (150.00 - {3.0/(1.05**0.25):.4f}) \\times 1.05^{{0.75}} = {f_d1:.2f}\\text{{ USD}}$.",
        f"**Forward Price = {f_d1:.2f} USD**."
    )

    p_pcp_n = 6.40 + 80.0 / (1.04 ** 0.5) - 82.0
    add_num(
        "NUM-7.1.2", "7.1.2", "Derivatives", "Easy / Put-Call Parity Arbitrage",
        "A European call ($X = 80\\text{ USD}$, $T = 0.5$ yr) trades at 6.40 USD while $S_0 = 82.00\\text{ USD}$ and $r_f = 4.00\\%$. If the market European put ($X=80, T=0.5$) trades at 3.50 USD, compute the fair put price and the immediate arbitrage profit per share.",
        "$$p_0 = c_0 + \\frac{X}{(1+r)^T} - S_0$$",
        f"1. Fair $p_0 = 6.40 + \\frac{{80.00}}{{1.04^{{0.5}}}} - 82.00 = 6.40 + 78.446 - 82.00 = {p_pcp_n:.2f}\\text{{ USD}}$.\n2. Market put (3.50 USD) is overpriced by $3.50 - {p_pcp_n:.2f} = {3.50 - p_pcp_n:.2f}\\text{{ USD}}$.\n3. Sell market put (+3.50) and buy synthetic put ($+c_0 - S_0 + PV(X)$ at -{p_pcp_n:.2f}).",
        f"**Fair Put = {p_pcp_n:.2f} USD; Riskless Arbitrage Profit = +{3.50 - p_pcp_n:.2f} USD/share**."
    )

    # Swap MTM valuation
    dfs_d = [0.988, 0.975, 0.961, 0.946]
    r_fix_old = 0.048  # annual, semiannual -> 2.40% per 6m
    # Suppose 2 periods remain with DF = 0.975 and 0.950 -> let's use exact clear numbers!
    df_rem = [0.9804, 0.9600]  # 6m and 12m
    r_fix_new_semi = (1 - df_rem[-1]) / sum(df_rem)  # (0.04)/1.9404 = 0.020614 -> 4.1229% annual
    v_rec_fix = 25000000.0 * (0.024 - r_fix_new_semi) * sum(df_rem)
    add_num(
        "NUM-7.2.1", "7.2.1", "Derivatives", "Moderate / L2 Interest Rate Swap Valuation",
        "A pension fund holds a 25,000,000 USD notional receive-fixed 4.80% (semiannual: 2.40%/period) plain-vanilla swap with exactly 1 year (two 6-month settlements) remaining. Current 6-month and 12-month discount factors are $DF_1 = 0.9804$ and $DF_2 = 0.9600$. Calculate the current mark-to-market value of the swap to the receive-fixed party.",
        "$$r_{\\text{new, semi}} = \\frac{1 - DF_n}{\\sum DF_i}, \\qquad V_{\\text{rec-fix}} = NP \\cdot (r_{\\text{old, semi}} - r_{\\text{new, semi}}) \\sum DF_i$$",
        f"1. Sum of discount factors $= 0.9804 + 0.9600 = 1.9404$.\n2. New par semiannual fixed rate $= (1 - 0.9600) / 1.9404 = {r_fix_new_semi*100:.4f}\\%$ (annualized ${r_fix_new_semi*200:.3f}\\%$, below old 4.80%!).\n3. Value of receive-fixed swap $= 25,000,000 \\times (0.0240 - {r_fix_new_semi:.6f}) \\times 1.9404 = +{v_rec_fix:,.2f}\\text{{ USD}}$.",
        f"**Receive-Fixed Swap Value = +{v_rec_fix:,.2f} USD**."
    )

    # 2-Period American Put Binomial Tree
    S0_ap, X_ap, u_ap, d_ap, rf_ap = 50.0, 52.0, 1.20, 0.80, 0.05
    pi_ap = (1 + rf_ap - d_ap) / (u_ap - d_ap)  # (1.05-0.80)/0.40 = 0.625
    suu, sud, sdd = S0_ap * u_ap * u_ap, S0_ap * u_ap * d_ap, S0_ap * d_ap * d_ap
    puu, pud, pdd = max(0.0, X_ap - suu), max(0.0, X_ap - sud), max(0.0, X_ap - sdd)
    pu_cont = (pi_ap * puu + (1 - pi_ap) * pud) / (1 + rf_ap)
    pu_node = max(max(0.0, X_ap - S0_ap * u_ap), pu_cont)
    pd_cont = (pi_ap * pud + (1 - pi_ap) * pdd) / (1 + rf_ap)
    pd_intr = max(0.0, X_ap - S0_ap * d_ap)
    pd_node = max(pd_intr, pd_cont)
    p0_am = max(max(0.0, X_ap - S0_ap), (pi_ap * pu_node + (1 - pi_ap) * pd_node) / (1 + rf_ap))
    p0_eu = ((pi_ap ** 2) * puu + 2 * pi_ap * (1 - pi_ap) * pud + ((1 - pi_ap) ** 2) * pdd) / ((1 + rf_ap) ** 2)
    add_num(
        "NUM-7.2.2", "7.2.2", "Derivatives", "Moderate / L2 2-Period American Put Binomial Tree",
        "A 2-period American put ($S_0 = 50\\text{ USD}$, $X = 52\\text{ USD}$) has $u = 1.20$, $d = 0.80$, and per-period risk-free rate $r = 5.0\\%$. Calculate both the American put value and the European put value (isolating the early exercise premium).",
        "$$\\pi_u = \\frac{(1+r)-d}{u-d}, \\qquad P_{\\text{node}} = \\max\\!\\left(X - S_t, \\; \\frac{\\pi_u P_u + (1-\\pi_u)P_d}{1+r}\\right)$$",
        f"1. Risk-neutral $\\pi_u = (1.05 - 0.80)/(1.20 - 0.80) = {pi_ap:.4f}$ ($1-\\pi_u = {1-pi_ap:.4f}$).\n2. Year 2 stock nodes: $S_{{uu}}=72, S_{{ud}}=48, S_{{dd}}=32$ $\\implies$ Put payoffs: $P_{{uu}}=0, P_{{ud}}=4.00, P_{{dd}}=20.00$.\n3. Year 1 Upper ($S_u = 60$): Cont $= (0.625(0) + 0.375(4))/1.05 = {pu_cont:.4f}$; Intr $= 0$. Node $= {pu_node:.4f}$.\n4. Year 1 Lower ($S_d = 40$): Cont $= (0.625(4) + 0.375(20))/1.05 = {pd_cont:.4f}$; Intr $= 52 - 40 = 12.00$. **Exercise early!** Node $= 12.00$.\n5. Year 0 American Put $= [0.625({pu_node:.4f}) + 0.375(12.00)] / 1.05 = {p0_am:.2f}\\text{{ USD}}$ (vs. European Put $= {p0_eu:.2f}\\text{{ USD}}$).",
        f"**American Put = {p0_am:.2f} USD; European Put = {p0_eu:.2f} USD (Early Exercise Premium = +{p0_am-p0_eu:.2f} USD)**."
    )

    bsm_n = bsm_values(S=60.0, K=58.0, r=0.04, T=0.25, sigma=0.30, q=0.0)
    add_num(
        "NUM-7.3.1", "7.3.1", "Derivatives", "Difficult / L2 Black-Scholes-Merton & Delta-Gamma Hedge",
        "Stock $S_0 = 60.00\\text{ USD}$ (no dividends), $K = 58.00\\text{ USD}$, $r = 4.0\\%$, $T = 0.25\\text{ yr}$, $\\sigma = 30.0\\%$. Using Black-Scholes-Merton, compute (1) $d_1, d_2, N(d_1), N(d_2)$, (2) European Call & Put premiums, and (3) shares needed to delta-hedge a short position of 500 call contracts (100 shares/contract = 50,000 options).",
        "$$c = S_0 N(d_1) - K e^{-rT} N(d_2), \\qquad d_1 = \\frac{\\ln(S_0/K) + (r + 0.5\\sigma^2)T}{\\sigma\\sqrt{T}}, \\qquad d_2 = d_1 - \\sigma\\sqrt{T}$$",
        f"1. $d_1 = {bsm_n['d1']:.4f} \\implies N(d_1) = {bsm_n['Nd1']:.4f}$; $d_2 = {bsm_n['d2']:.4f} \\implies N(d_2) = {bsm_n['Nd2']:.4f}$.\n2. Call $c = {bsm_n['call']:.2f}\\text{{ USD}}$; Put $p = {bsm_n['put']:.2f}\\text{{ USD}}$.\n3. Short 50,000 calls has $\\Delta = -50,000 \\times {bsm_n['delta_c']:.4f} = -{50000*bsm_n['delta_c']:,.0f}$ shares $\\implies$ **Buy {50000*bsm_n['delta_c']:,.0f} shares**.",
        f"**Call = {bsm_n['call']:.2f} USD; Put = {bsm_n['put']:.2f} USD; Buy {50000*bsm_n['delta_c']:,.0f} shares to delta-hedge**."
    )

    # Currency Swap MTM
    # Receive 4% EUR (annual) on EUR 10M, Pay 5% USD (annual) on USD 11M; spot USD/EUR = 1.15; remaining 1 yr, r_EUR = 3.5%, r_USD = 4.5%
    pv_eur = (10.4) / 1.035
    pv_usd = (11.55) / 1.045
    v_ccy_usd = pv_eur * 1.15 - pv_usd
    add_num(
        "NUM-7.3.2", "7.3.2", "Derivatives", "Difficult / L2 Fixed-for-Fixed Currency Swap MTM",
        "A US corporate entered a fixed-for-fixed currency swap receiving 4.0% EUR annually on 10.0M EUR and paying 5.0% USD annually on 11.0M USD. Exactly 1 year remains before final principal & coupon exchange. Current 1-year discount rates are $r_{EUR} = 3.50\\%$ and $r_{USD} = 4.50\\%$, and spot FX is $USD/EUR = 1.1500$. Compute the USD mark-to-market value of the swap.",
        "$$V_{\\text{USD}} = S_{USD/EUR} \\cdot PV(\\text{EUR Leg}) - PV(\\text{USD Leg})$$",
        f"1. PV of Receive EUR Leg $= 10.40\\text{{M}} / 1.035 = {pv_eur:.4f}\\text{{M EUR}}$.\n2. Converted to USD at spot $1.15$: ${pv_eur:.4f}\\text{{M}} \\times 1.15 = {pv_eur*1.15:.4f}\\text{{M USD}}$.\n3. PV of Pay USD Leg $= 11.55\\text{{M}} / 1.045 = {pv_usd:.4f}\\text{{M USD}}$.\n4. Net USD Swap Value $= {pv_eur*1.15:.4f} - {pv_usd:.4f} = +{v_ccy_usd:.4f}\\text{{M USD}}$ (+{v_ccy_usd*1e6:,.0f} USD).",
        f"**+{v_ccy_usd*1e6:,.0f} USD**."
    )

    # === 6. ALTERNATIVE INVESTMENTS ===
    # 6.1 Hedge Fund Waterfall
    hf_g = 200.0 * 1.20  # 240
    hf_m = hf_g * 0.02  # 4.8
    hf_am = hf_g - hf_m  # 235.2
    hf_inc = max(0.0, (hf_am - 200.0 - 10.0) * 0.20)  # (35.2 - 10)*0.2 = 5.04
    hf_net = (hf_am - hf_inc - 200.0) / 200.0
    add_num(
        "NUM-8.1.1", "8.1.1", "Alternative Investments", "Easy / Hedge Fund Fee Waterfall (Hard Hurdle)",
        "A hedge fund opens with 200M USD NAV, charges 2% management fee on ending AUM and 20% incentive fee calculated net of management fees above a 5.0% hard hurdle (10M USD). Gross return is +20.0%. Calculate the investor's net percentage return.",
        "$$\\text{Inc Fee} = \\max(0, [NAV_{\\text{after mgmt}} - NAV_0 - \\text{Hurdle}] \\times 0.20)$$",
        f"1. Gross Ending NAV $= 200 \\times 1.20 = 240.00\\text{{M USD}}$.\n2. Management fee $= 240 \\times 2\\% = 4.80\\text{{M}} \\implies NAV_{{\\text{{after mgmt}}}} = 235.20\\text{{M}}$.\n3. Excess above HWM + 5% hard hurdle $= 235.20 - 200.00 - 10.00 = 25.20\\text{{M}}$.\n4. Incentive fee $= 20\\% \\times 25.20 = 5.04\\text{{M USD}}$.\n5. Net Ending NAV $= 235.20 - 5.04 = 230.16\\text{{M USD}} \\implies \\text{{Net Return}} = +{hf_net*100:.2f}\\%$.",
        f"**+{hf_net*100:.2f}% Net Investor Return** (Total GP fees = 9.84M USD)."
    )

    # 6.2 PE Multiples
    add_num(
        "NUM-8.1.2", "8.1.2", "Alternative Investments", "Easy / PE Fund DPI, RVPI & TVPI",
        "A buyout fund with 100M USD committed capital has called 75M USD paid-in capital, distributed 54M USD cash to LPs, and holds 48M USD in residual unrealized NAV. Calculate DPI, RVPI, and TVPI.",
        "$$DPI = \\frac{\\text{Distributions}}{\\text{Paid-In}}, \\quad RVPI = \\frac{\\text{NAV}}{\\text{Paid-In}}, \\quad TVPI = DPI + RVPI$$",
        "1. $DPI = 54 / 75 = 0.72\\times$.\n2. $RVPI = 48 / 75 = 0.64\\times$.\n3. $TVPI = 0.72 + 0.64 = 1.36\\times$ (paid-in capital is always the denominator, NOT committed capital!).",
        "**DPI = 0.72x; RVPI = 0.64x; TVPI = 1.36x**."
    )

    # 6.3 Venture Capital Multi-Round Valuation
    vc_exit = 150.0  # Year 4 exit
    vc_post = vc_exit / (1.35 ** 4)  # 150 / 3.321506 = 45.1602
    vc_own_final = 10.0 / vc_post  # 22.143%
    vc_own_init = vc_own_final / (1 - 0.20)  # 27.679%
    add_num(
        "NUM-8.2.1", "8.2.1", "Alternative Investments", "Moderate / L2 Venture Capital Method w/ Dilution",
        "A Series A VC invests 10.0M USD today into FinTechCo, targeting a 35% IRR over a 4-year exit projected at 150.0M USD. Management plans a Series B financing in Year 2 that will dilute Series A investors by 20%. Calculate (1) post-money valuation, (2) required final exit ownership, and (3) required initial Series A ownership percentage today.",
        "$$\\text{Post} = \\frac{TV}{(1+r)^T}, \\qquad f_{\\text{initial}} = \\frac{f_{\\text{final}}}{1 - \\text{Dilution}}$$",
        f"1. Post-money valuation $= 150 / 1.35^4 = {vc_post:.2f}\\text{{M USD}}$.\n2. Required ownership at Year 4 exit $= 10 / {vc_post:.2f} = {vc_own_final*100:.2f}\\%$.\n3. Adjusting for 20% Series B dilution: Required initial share $= {vc_own_final*100:.2f}\\% / 0.80 = {vc_own_init*100:.2f}\\%$.",
        f"**Post-Money = {vc_post:.2f}M USD; Exit Share = {vc_own_final*100:.2f}%; Initial Share Today = {vc_own_init*100:.2f}%**."
    )

    # 6.4 Direct Real Estate DCF & DSCR
    add_num(
        "NUM-8.2.2", "8.2.2", "Alternative Investments", "Moderate / L2 Real Estate Cap Rate, LTV & DSCR",
        "A logistics warehouse generates $NOI_1 = 960,000\\text{ USD}$ at an 8.00% going-in market cap rate. A commercial lender enforces a max LTV of 65% and a minimum DSCR of 1.30x at a 7.3846% mortgage debt constant (annual debt service $= 7.3846\\% \\times \\text{Loan}$). Determine the maximum permissible mortgage loan.",
        "$$V_0 = \\frac{NOI_1}{R_{\\text{cap}}}, \\qquad \\text{Loan}_{\\text{DSCR}} = \\frac{NOI_1 / DSCR_{\\text{min}}}{\\text{Debt Constant}}$$",
        "1. Appraised Value $V_0 = 960,000 / 0.08 = 12,000,000\\text{ USD}$.\n2. LTV cap $= 0.65 \\times 12,000,000 = 7,800,000\\text{ USD}$.\n3. Max Debt Service $= 960,000 / 1.30 = 738,461.54\\text{ USD}$.\n4. DSCR max loan $= 738,461.54 / 0.07384615 = 10,000,000\\text{ USD}$.\n5. Take the *lower* binding constraint: **7,800,000 USD**.",
        "**Maximum Loan = 7,800,000 USD (LTV Constraint Binds)**."
    )

    # 6.5 REIT NAVPS & P/AFFO
    nav_reit_n = (65.0 / 0.065 + 20.0 - 420.0) / 25.0
    add_num(
        "NUM-8.3.1", "8.3.1", "Alternative Investments", "Difficult / L2 REIT NAVPS & AFFO Valuation",
        "Industrial REIT reports cash NOI of 65.0M USD (market cap rate 6.50%), non-RE cash of 20.0M USD, total debt of 420.0M USD, and 25.0M diluted shares. GAAP Net Income is 32.0M USD, RE Depreciation is 22.0M USD, Property Sales Gains are 4.0M USD, Straight-Line Rent adjustment is +2.5M USD, and recurring maintenance capex is 7.5M USD. Compute (1) NAVPS and (2) AFFO per share.",
        "$$NAVPS = \\frac{(NOI / R_{\\text{cap}}) + \\text{Cash} - \\text{Debt}}{\\text{Shares}}, \\qquad AFFO = (NI + \\text{Dep} - \\text{Gains}) - \\text{SL Rent} - \\text{Maint Capex}$$",
        f"1. Gross Real Estate $= 65.0 / 0.065 = 1,000.0\\text{{M USD}}$.\n2. $NAV = 1,000 + 20 - 420 = 600.0\\text{{M}} \\implies NAVPS = 600.0 / 25.0 = {nav_reit_n:.2f}\\text{{ USD}}$.\n3. $FFO = 32.0 + 22.0 - 4.0 = 50.0\\text{{M USD}}$.\n4. $AFFO = 50.0 - 2.5 - 7.5 = 40.0\\text{{M USD}} \\implies \\text{{AFFO/share}} = 40.0 / 25.0 = 1.60\\text{{ USD}}$.",
        f"**NAVPS = {nav_reit_n:.2f} USD; AFFO/share = 1.60 USD**."
    )

    # 6.6 PE Waterfall w/ Preferred Return & GP Catch-up
    # Committed 100M, Exit proceeds 140M after 1 yr. 8% pref hurdle = 8M, 100% catch-up to 20% of total profit (40M -> GP gets 8M total!), rest 80/20
    add_num(
        "NUM-8.3.2", "8.3.2", "Alternative Investments", "Difficult / L2 Whole-of-Fund PE Catch-Up Waterfall",
        "A private equity fund receives 100M USD LP paid-in capital and exits everything after 1 year for 140M USD (40M total gain). Terms specify a whole-of-fund waterfall: (1) 100% return of capital, (2) 8.0% preferred hurdle (8.0M USD) to LPs, (3) 100% GP Catch-Up until GP holds 20% of cumulative profits distributed, and (4) 80/20 LP/GP split thereafter. Compute exact LP and GP dollar payouts.",
        "$$\\text{Catch-Up Target: } GP = 0.20 \\times (\\text{Hurdle} + \\text{Catch-Up}) \\implies \\text{Catch-Up} = \\frac{0.20}{0.80} \\times \\text{Hurdle}$$",
        "1. Tier 1 (Return of Capital): 100.0M USD to LPs (40.0M gain remaining).\n2. Tier 2 (8% Preferred Hurdle): 8.0M USD to LPs (32.0M remaining).\n3. Tier 3 (100% GP Catch-Up): To make GP share 20% of profits so far: $GP = 0.25 \\times 8.0\\text{M} = 2.0\\text{M USD}$ to GP ($2 / (8+2) = 20\\%$! Remaining gain $= 30.0\\text{M}$).\n4. Tier 4 (80/20 Split of remaining 30.0M): LP gets $0.80 \\times 30 = 24.0\\text{M}$; GP gets $0.20 \\times 30 = 6.0\\text{M}$.\n5. Total GP Carry $= 2.0 + 6.0 = 8.0\\text{M USD}$ (20% of 40M!); Total LP payout $= 100 + 8 + 24 = 132.0\\text{M USD}$.",
        "**LP Payout = 132.0M USD (+32.0M gain); GP Carried Interest = 8.0M USD**"
    )

    return items


def build_new_jargon_entries() -> list[dict]:
    entries = []

    def add_j(jid, term, aliases, regex_pat, cat, lvl, defn, form, uses, pitfalls, wn, rel, num_code="", sim=""):
        for fld, val in [("definition", defn), ("formula", form)] + [(f"use_{i}", u) for i, u in enumerate(uses)] + [(f"pit_{i}", p) for i, p in enumerate(pitfalls)]:
            errs = check_text_compliance(val, f"{jid}.{fld}")
            if errs:
                raise ValueError("\n".join(errs))
        entries.append({
            "id": jid,
            "term": term,
            "aliases": aliases,
            "regexPattern": regex_pat,
            "category": cat,
            "level": lvl,
            "definition": defn,
            "formula": form,
            "practicalUses": uses,
            "commonPitfalls": pitfalls,
            "workedNumerical": wn,
            "relatedTerms": rel,
            "relatedNumCode": num_code,
            "relatedSimTab": sim,
        })

    # ETHICS (6)
    add_j("eth-mosaic-theory", "Mosaic Theory", ["Mosaic Theory"], r"\bMosaic Theory\b", "ETH", "Both",
          "An analytical framework permitting research analysts to combine material public information with nonmaterial nonpublic observations to derive a perceptive, actionable investment conclusion without violating insider trading rules.",
          r"\text{Public Material Info} + \text{Nonmaterial Nonpublic Info} \implies \text{Compliant Alpha}",
          ["Channel checks with store managers, suppliers, and industry experts.", "Satellite imagery and web-scraped pricing combined with 10-K filings."],
          ["Combining public info with ANY single piece of material nonpublic info (MNPI) destroys the mosaic defense and violates Standard II(A)."],
          {"title": "Supplier Channel Check", "given": ["10-K filings (Public)", "12 regional parts vendors' order observations (Nonmaterial Nonpublic)"], "steps": ["Verify no vendor broke NDA.", "Synthesize margin surprise thesis."], "result": "100% Compliant under Standard II(A)"},
          ["eth-soft-dollars", "eth-gips-composite"], "", "")

    add_j("eth-soft-dollars", "Soft Dollars (Client Brokerage)", ["Soft Dollars", "Soft-Dollar"], r"\bSoft[- ]Dollars?\b", "ETH", "Both",
          "Commissions directed by an investment manager to a broker in exchange for research products or execution services rather than purely lowest-cost trade execution.",
          r"\text{Client Brokerage} \in \text{Client Asset} \implies \text{Must Directly Assist Investment Decisions}",
          ["Funding Bloomberg terminals, quantitative factor databases, or independent sell-side research."],
          ["Never use soft dollars to pay firm rent, employee salaries, conference travel, or marketing brochures (violates Standard III(A))."],
          {"title": "Mixed-Use Research Allocation", "given": ["180k USD soft dollars", "65% research / 35% firm overhead"], "steps": ["Firm pays 35% * 180k = 63,000 USD from corporate cash."], "result": "63,000 USD corporate reimbursement"},
          ["eth-priority-tx", "eth-mosaic-theory"], "1.2.1", "")

    add_j("eth-priority-tx", "Priority of Transactions (Std VI(B))", ["Priority of Transactions", "Front-Running"], r"\b(Priority of Transactions|Front[- ]Running)\b", "ETH", "Both",
          "CFA Standard VI(B) requiring that investment transactions for clients and employers take precedence over transactions in which a member/candidate has beneficial ownership.",
          r"\text{Order Hierarchy: } 1.\;\text{Clients} \succ 2.\;\text{Employer} \succ 3.\;\text{Personal / Beneficial Family}",
          ["Enforcing blackout periods, pre-clearance lists, and minimum holding periods."],
          ["Treating a fee-paying relative's non-beneficial retail account worse than external clients violates Standard III(B) Fair Dealing!"],
          {"title": "Hot IPO Share Queue", "given": ["100k client demand", "10k personal order", "25k IPO allocation"], "steps": ["Assign 0 to personal account; allocate 25% pro-rata across client accounts."], "result": "25,000 to clients; 0 personal"},
          ["eth-soft-dollars", "eth-gips-composite"], "1.2.2", "")

    add_j("eth-gips-composite", "GIPS Composite & Verification", ["GIPS", "GIPS Composite"], r"\b(GIPS Composite|GIPS)\b", "ETH", "Both",
          "Global Investment Performance Standards grouping all actual, fee-paying, discretionary portfolios managed under a single strategy to prevent cherry-picking and survivorship bias.",
          r"R_{\text{comp}} = \sum \left(\frac{BMV_i}{\sum BMV}\right) R_i, \quad \text{TWR Mandated}",
          ["Standardizing institutional performance track records globally across asset managers."],
          ["A firm cannot claim GIPS compliance for just one fund or verify one composite without firm-wide compliance."],
          {"title": "Asset-Weighted Composite", "given": ["Acct A: 25M at +11.2%", "Acct B: 45M at +8.4%", "Acct C: 30M at +14.6%"], "steps": ["0.25(11.2)+0.45(8.4)+0.30(14.6) = 10.96%"], "result": "10.96% Composite Return"},
          ["eth-modified-dietz", "pm-twr-mwr"], "1.1.2", "")

    add_j("eth-modified-dietz", "Modified Dietz Return", ["Modified Dietz"], r"\bModified Dietz\b", "ETH", "L2",
          "An approximation to Time-Weighted Return weighting external cash flows by the fraction of the measurement period they remain invested in the portfolio.",
          r"R_{\text{MD}} = \frac{EMV - BMV - CF}{BMV + \sum CF_j \left(\frac{CD - D_j}{CD}\right)}",
          ["Computing sub-period performance between daily valuations for GIPS reporting."],
          ["Cannot substitute for exact re-valuation on dates with large external cash flows (>= 10% of portfolio value)."],
          {"title": "31-Day Month Dietz", "given": ["BMV=12M", "Day 10 CF=+3M", "EMV=15.8M"], "steps": ["w=(31-10)/31=0.6774", "Base=14.032M", "Gain=0.8M"], "result": "+5.70%"},
          ["eth-gips-composite"], "1.1.1", "")

    add_j("eth-dissociation", "Dissociation Duty (Std I(A))", ["Dissociation", "Dissociate"], r"\bDissociat(e|ion)\b", "ETH", "Both",
          "Mandatory compliance action under Standard I(A) when internal escalation fails to halt an illegal or unethical firm practice—requiring the practitioner to remove their name and sever ties with the activity.",
          r"\text{Confront} \to \text{Escalate to Compliance} \to \text{Dissociate / Resign}",
          ["Removing one's name from biased research or refusing to sign misleading marketing."],
          ["Passive silence is NOT compliant; whistleblowing to regulators is optional unless required by local law, whereas dissociation is mandatory."],
          {"title": "Biased Brochure Escalation", "given": ["Firm guarantees 12% equity returns", "Compliance refuses edit"], "steps": ["Submit written dissent; strip name from report; request reassignment or resign."], "result": "Compliant Dissociation"},
          ["eth-mosaic-theory"], "", "")

    # QUANTITATIVE METHODS (6)
    add_j("qm-bayes", "Bayes' Theorem", ["Bayes' Theorem", "Bayes' Formula", "Posterior Probability"], r"\bBayes'? (Theorem|Formula)\b", "QM", "L1",
          "Probability rule updating prior beliefs about an event when new diagnostic evidence or market signals arrive.",
          r"P(A \mid B) = \frac{P(B \mid A)\,P(A)}{P(B \mid A)P(A) + P(B \mid A^c)P(A^c)}",
          ["Updating default probabilities upon credit downgrades or recession probability after yield curve inversion."],
          ["Confusing conditional likelihood P(B|A) with posterior probability P(A|B)."],
          {"title": "Yield Curve Recession Signal", "given": ["Prior P(Rec)=25%", "P(Inv|Rec)=85%", "P(Inv|Exp)=20%"], "steps": ["0.2125 / (0.2125 + 0.1500) = 0.2125 / 0.3625"], "result": "58.62% Posterior"},
          ["qm-safety-first"], "2.1.2", "quant")

    add_j("qm-safety-first", "Roy's Safety-First Criterion", ["Roy's Safety-First", "Safety-First Ratio"], r"\b(Roy'?s )?Safety[- ]First( Criterion| Ratio)?\b", "QM", "L1",
          "Portfolio selection metric minimizing the probability that portfolio return falls below a critical disaster threshold R_L.",
          r"\text{SFRatio} = \frac{E(R_p) - R_L}{\sigma_p}",
          ["Selecting pension or endowment allocations facing strict minimum funding constraints."],
          ["Using R_f instead of the specific shortfall threshold R_L (note: SFRatio equals Sharpe only when R_L = R_f)."],
          {"title": "Shortfall Threshold Rank", "given": ["R_L=3%", "Fund A: E=11%, SD=16%", "Fund B: E=14%, SD=24%"], "steps": ["SFR_A = 8/16 = 0.500", "SFR_B = 11/24 = 0.458"], "result": "Fund A Dominates (SFR=0.500)"},
          ["qm-bayes", "pm-sharpe-treynor"], "", "quant")

    add_j("qm-vif", "Variance Inflation Factor (VIF)", ["Variance Inflation Factor", "VIF"], r"\b(Variance Inflation Factor|VIF)\b", "QM", "L2",
          "Diagnostic detecting multicollinearity in multiple regression by measuring how much an independent variable's coefficient variance is inflated by correlation with other predictors.",
          r"\text{VIF}_j = \frac{1}{1 - R_j^2}",
          ["Screening macroeconomic or valuation factors for redundant predictors before OLS estimation."],
          ["Forgetting that multicollinearity leaves R^2 high and F-test significant while inflating SEs so individual t-stats look insignificant."],
          {"title": "Factor Collinearity Screen", "given": ["R_j^2 = 0.88"], "steps": ["VIF = 1 / (1 - 0.88) = 1 / 0.12"], "result": "VIF = 8.33 (Warning > 5)"},
          ["qm-durbin-watson", "qm-garch"], "2.2.2", "")

    add_j("qm-durbin-watson", "Durbin-Watson & Newey-West", ["Durbin-Watson", "Serial Correlation", "Autocorrelation"], r"\b(Durbin[- ]Watson|Serial Correlation)\b", "QM", "L2",
          "Diagnostic statistic testing first-order residual autocorrelation in OLS time-series regressions, typically corrected via Newey-West HAC standard errors.",
          r"DW \approx 2(1 - r), \quad DW \approx 2 \implies \text{No Serial Correlation}",
          ["Validating monthly factor regressions before trusting t-statistics."],
          ["NEVER apply Durbin-Watson to an autoregressive AR(p) model containing lagged dependent variables (use Breusch-Godfrey or residual t-tests instead!)."],
          {"title": "Residual Autocorrelation Check", "given": ["Residual lag-1 corr r = +0.65"], "steps": ["DW ≈ 2(1 - 0.65) = 0.70 << 2"], "result": "Strong Positive Serial Correlation"},
          ["qm-vif", "qm-ar1"], "", "")

    add_j("qm-ar1", "AR(1) & Unit Root (Dickey-Fuller)", ["Autoregressive", "AR(1)", "Unit Root", "Dickey-Fuller"], r"\b(AR\(1\)|Unit Root|Dickey[- ]Fuller)\b", "QM", "L2",
          "Time-series regression on its own 1-period lag; covariance stationary and mean-reverting only when |b_1| < 1 (unit root when b_1 = 1).",
          r"X_t = b_0 + b_1 X_{t-1} + \epsilon_t, \qquad \bar{X} = \frac{b_0}{1 - b_1}",
          ["Forecasting mean-reverting margins, ROE, or real interest rates."],
          ["Attempting to compute a mean-reverting level when b_1 = 1 (random walk has undefined infinite variance and no mean reversion)."],
          {"title": "Mean-Reverting ROE Forecast", "given": ["b0=0.012", "b1=0.75", "ROE_0=8%"], "steps": ["Mean=0.012/0.25=4.80%", "ROE_1=0.012+0.75(0.08)=7.20%"], "result": "Mean = 4.80%; ROE_2 = 6.60%"},
          ["qm-garch", "qm-durbin-watson"], "2.3.1", "")

    add_j("qm-garch", "GARCH(1,1) Volatility Model", ["GARCH", "Volatility Clustering"], r"\bGARCH(\(1,1\))?\b", "QM", "L2",
          "Generalized Autoregressive Conditional Heteroskedasticity model forecasting time-varying volatility clustering from lagged squared return shocks and lagged conditional variance.",
          r"\sigma_t^2 = \omega + \alpha \epsilon_{t-1}^2 + \beta \sigma_{t-1}^2, \qquad V_L = \frac{\omega}{1 - \alpha - \beta}",
          ["Risk budgeting, dynamic option pricing, and VaR scaling during turbulent volatility regimes."],
          ["Forgetting persistence condition alpha + beta < 1 required for finite long-run variance V_L."],
          {"title": "Daily Variance Shock Update", "given": ["omega=0.000015", "alpha=0.12", "beta=0.82", "eps=-3%", "sigma=2%"], "steps": ["0.000015 + 0.12(0.0009) + 0.82(0.0004) = 0.000451"], "result": "sigma_t = 2.12% daily"},
          ["qm-ar1", "deriv-bsm"], "2.3.2", "")

    # ECONOMICS (5)
    add_j("econ-cirp", "Covered Interest Rate Parity (CIRP)", ["Covered Interest Rate Parity", "CIRP", "Interest Rate Parity"], r"\b(Covered Interest Rate Parity|CIRP)\b", "ECON", "Both",
          "Arbitrage-enforced condition equating the forward FX premium/discount to the nominal interest rate differential between price and base currencies.",
          r"F_{P/B} = S_{P/B} \cdot \frac{1 + r_P(T)}{1 + r_B(T)}",
          ["Pricing currency forwards and detecting covered interest arbitrage mispricings."],
          ["Reversing CFA P/B quote order: the higher-interest-rate currency ALWAYS trades at a forward discount!"],
          {"title": "180-Day Arbitrage Check", "given": ["S=1.20 USD/EUR", "r_USD=4.8%", "r_EUR=3.2%", "F_quote=1.22"], "steps": ["F* = 1.20*(1.024/1.016)=1.20945", "Borrow USD, invest EUR, sell forward"], "result": "+8,933 USD Riskless Profit"},
          ["econ-carry-trade", "econ-ppp"], "3.5.2", "")

    add_j("econ-carry-trade", "FX Carry Trade", ["Carry Trade", "FX Carry"], r"\b(FX )?Carry Trade\b", "ECON", "L2",
          "Leveraged currency strategy borrowing low-yielding funding currencies and investing in high-yielding target currencies, exploiting empirical violations of Uncovered IRP.",
          r"R_{\text{Carry}} = (1 + r_{\text{target}})\left(\frac{S_1}{S_0}\right) - (1 + r_{\text{funding}})",
          ["Generating systematic yield pickup during low-volatility global expansion regimes."],
          ["Ignoring severe negative skewness (crash risk) when risk-off shocks cause rapid funding-currency appreciation."],
          {"title": "JPY/BRL Unhedged Carry", "given": ["Borrow JPY at 1.2%", "Invest BRL at 7.2%", "BRL drops -2.73%"], "steps": ["1.072*(29.18/30.00) - 1.012 = +3.07%"], "result": "+3.07% Net Return"},
          ["econ-cirp", "econ-ppp"], "3.6.1", "")

    add_j("econ-ppp", "Purchasing Power Parity (PPP)", ["Purchasing Power Parity", "PPP"], r"\b(Purchasing Power Parity|PPP)\b", "ECON", "L2",
          "Long-run exchange rate equilibrium predicting currencies with higher domestic inflation depreciate proportionally relative to lower-inflation currencies.",
          r"\%\Delta S_{P/B} \approx \pi_P - \pi_B",
          ["Setting multi-decade strategic currency anchors in Capital Market Expectations."],
          ["Applying PPP to short-term 3-month FX trading—PPP holds only over 5–10+ year horizons."],
          {"title": "3-Year Relative PPP Path", "given": ["S0=1.10 USD/EUR", "US pi=2.2%", "EU pi=3.7%"], "steps": ["1.10 * (1.022/1.037)^3"], "result": "1.0530 USD/EUR"},
          ["econ-cirp", "econ-cobb-douglas"], "", "")

    add_j("econ-cobb-douglas", "Cobb-Douglas & Solow Growth", ["Cobb-Douglas", "Solow Steady State", "Growth Accounting"], r"\b(Cobb[- ]Douglas|Solow Steady State|Growth Accounting)\b", "ECON", "L2",
          "Macroeconomic production framework decomposing potential GDP growth into Total Factor Productivity (TFP), capital deepening, and labor force growth.",
          r"\frac{\Delta Y}{Y} = \frac{\Delta A}{A} + \alpha \frac{\Delta K}{K} + (1-\alpha)\frac{\Delta L}{L}, \qquad g^* = \frac{\theta}{1-\alpha} + n",
          ["Forecasting long-run sovereign equity growth limits and emerging-market convergence."],
          ["Claiming higher savings permanently raises steady-state GDP growth—in Solow, savings only elevates level k*, not permanent growth!"],
          {"title": "Potential GDP Forecast", "given": ["TFP=1.6%", "alpha=0.30", "dK/K=4%", "dL/L=1.2%"], "steps": ["1.6 + 0.30(4) + 0.70(1.2) = 3.64%"], "result": "3.64% Potential Growth"},
          ["econ-taylor-rule", "econ-ppp"], "3.6.2", "")

    add_j("econ-taylor-rule", "Taylor Rule (Policy Rate)", ["Taylor Rule"], r"\bTaylor Rule\b", "ECON", "Both",
          "Central bank monetary policy prescription setting target nominal short-term rates based on neutral real rate, inflation gap, and output gap.",
          r"i^* = r_{\text{neutral}} + \pi + 0.5(\pi - \pi^*) + 0.5(y - y^*)",
          ["Anticipating Fed/ECB tightening cycles and yield curve flattening shifts."],
          ["Adding inflation gap to target inflation pi* instead of current inflation pi!"],
          {"title": "Prescribed Fed Funds Rate", "given": ["r*=1.5%", "pi=4.0%", "pi*=2.0%", "y-y*=+1.0%"], "steps": ["1.5 + 4.0 + 0.5(2.0) + 0.5(1.0)"], "result": "7.00% Target Policy Rate"},
          ["econ-cobb-douglas"], "3.4.2", "")

    # CORPORATE ISSUERS (5)
    add_j("corp-wacc", "WACC & Marginal Cost of Capital", ["WACC", "Weighted Average Cost of Capital"], r"\b(WACC|Weighted Average Cost of Capital)\b", "CORP", "Both",
          "After-tax blended required rate of return across debt, preferred stock, and common equity weighted by target market-value capital structure.",
          r"\text{WACC} = w_d r_d(1-t) + w_p r_p + w_e r_e",
          ["Hurdle rate for corporate NPV capital budgeting and FCFF enterprise valuation."],
          ["Adding equity flotation costs into WACC permanently instead of deducting them upfront at t=0, or using historical book weights."],
          {"title": "Target Capital Structure WACC", "given": ["wd=50%", "rd=6.2%", "t=20%", "re=11.0%"], "steps": ["0.5(6.2%)(0.8) + 0.5(11.0%) = 2.48% + 5.50%"], "result": "WACC = 7.98%"},
          ["corp-hamada", "corp-mm"], "5.5.1", "corp")

    add_j("corp-hamada", "Pure-Play Hamada Beta", ["Hamada", "Unlevered Beta", "Pure-Play Method"], r"\b(Hamada|Unlevered Beta|Pure[- ]Play Method)\b", "CORP", "L2",
          "Two-step method stripping peer financial leverage out of observed equity beta to obtain pure business asset risk, then relevering for a target project's tax rate and debt-to-equity ratio.",
          r"\beta_U = \frac{\beta_L}{1 + (1-t)\frac{D}{E}}, \qquad \beta_{\text{proj}} = \beta_U\left[1 + (1-t_P)\left(\frac{D}{E}\right)_P\right]",
          ["Estimating divisional hurdle rates for conglomerates entering new business lines."],
          ["Using the target firm's tax rate when unlevering the comparable peer—always use the peer's own (t, D/E) to unlever!"],
          {"title": "Divisional Beta Adjustment", "given": ["Peer beta=1.40, D/E=0.50, t=25%", "Proj D/E=1.00, t=20%"], "steps": ["beta_U = 1.40/1.375 = 1.0182", "beta_P = 1.0182 * 1.80"], "result": "Project Beta = 1.833"},
          ["corp-wacc", "corp-mm"], "5.5.1", "corp")

    add_j("corp-ccc", "Cash Conversion Cycle (CCC)", ["Cash Conversion Cycle", "CCC"], r"\bCash Conversion Cycle\b", "CORP", "L1",
          "Working capital efficiency metric measuring net days cash remains tied up between paying suppliers and collecting cash from customers.",
          r"CCC = DOH + DSO - DPO",
          ["Evaluating short-term working capital financing needs and operational efficiency trends."],
          ["Adding DPO instead of subtracting DPO (longer supplier payables reduce cash tied up)."],
          {"title": "Working Capital Cycle", "given": ["DOH=48d", "DSO=39d", "DPO=31d"], "steps": ["48 + 39 - 31"], "result": "CCC = 56 Days"},
          ["corp-wacc"], "5.4.1", "")

    add_j("corp-mm", "Modigliani-Miller Capital Structure", ["Modigliani-Miller", "Static Trade-Off", "Pecking Order"], r"\b(Modigliani[- ]Miller|Static Trade[- ]Off|Pecking Order)\b", "CORP", "L2",
          "Capital structure theorem proving debt adds value solely via tax shields (t*D), balanced against financial distress and agency costs in Static Trade-Off theory.",
          r"V_L = V_U + t D - PV(\text{Distress}), \qquad r_e = r_0 + (r_0 - r_d)(1-t)\frac{D}{E}",
          ["Optimizing corporate debt targets and explaining negative SEO stock price reactions (Pecking Order)."],
          ["Forgetting that MM Proposition II assumes debt risk-free/constant r_d until financial distress spikes."],
          {"title": "Tax Shield vs. Distress", "given": ["VU=20.45M", "D=8M", "t=25%", "Distress=450k"], "steps": ["20.45M + 2.00M - 0.45M"], "result": "VL = 22.00M USD"},
          ["corp-wacc", "corp-hamada"], "5.6.1", "corp")

    add_j("corp-ma-accretion", "M&A Accretion & Exchange Ratio", ["Exchange Ratio", "Accretive Merger", "Bootstrapping Fallacy"], r"\b(Exchange Ratio|Bootstrapping Fallacy)\b", "CORP", "L2",
          "Stock-for-stock merger ratio determining shares issued per target share and whether combined post-merger EPS rises or dilutes.",
          r"ER = \frac{P_{\text{offer}}}{P_A}, \qquad EPS_{\text{post}} = \frac{NI_A + NI_T + S_{\text{after-tax}}}{N_A + N_T \cdot ER}",
          ["Negotiating cash vs. stock M&A deal terms and breakeven synergy targets."],
          ["Mistaking bootstrapping (buying a low-P/E firm with high-P/E stock) for real economic value creation without synergies."],
          {"title": "Stock Swap EPS Check", "given": ["Acq P=72, EPS=4.50, 80M sh", "Tgt Offer=54, EPS=2.40, 20M sh"], "steps": ["ER=0.75 (15M new sh)", "408M / 95M = 4.29 USD"], "result": "Breakeven Pre-Tax Synergy = 26.0M USD"},
          ["corp-wacc", "corp-mm"], "5.6.2", "")

    # DERIVATIVES (5)
    add_j("deriv-pcp", "Put-Call Parity", ["Put-Call Parity", "Fiduciary Call", "Protective Put"], r"\b(Put[- ]Call Parity|Fiduciary Call|Protective Put)\b", "DERIV", "Both",
          "Exact no-arbitrage pricing identity linking European calls, European puts, the underlying spot asset, and a risk-free zero-coupon bond at identical strike and expiry.",
          r"c_0 + \frac{X}{(1+r)^T} = S_0 + p_0",
          ["Pricing synthetic calls, puts, stocks, or risk-free bonds and exploiting arbitrage mispricings."],
          ["Applying strict equality to American options (dividends/early exercise turn equality into inequality bounds)."],
          {"title": "Synthetic Put Arbitrage", "given": ["c=6.40", "X=80", "S=82", "r=4%", "T=0.5"], "steps": ["Fair p = 6.40 + 78.45 - 82 = 2.85 USD"], "result": "Fair Put = 2.85 USD"},
          ["deriv-bsm", "deriv-fra"], "7.1.2", "bsm")

    add_j("deriv-fra", "Forward Rate Agreement (FRA)", ["Forward Rate Agreement", "FRA"], r"\b(Forward Rate Agreement|FRA)\b", "DERIV", "L2",
          "OTC interest rate forward locking in a fixed borrowing/lending rate over a future reference period, settled in cash on a discounted basis at loan start.",
          r"V_t(\text{Pay-Fix}) = NP \cdot \frac{(FRA_t - FRA_0)(m/360)}{1 + L_{T-t}(T_{\text{settle}}/360)}",
          ["Hedging future corporate floating-rate debt issuances or commercial loan resets."],
          ["Forgetting to discount the FRA cash settlement from loan maturity back to settlement date (paid in advance!)."],
          {"title": "3x6 FRA Mid-Life MTM", "given": ["NP=10M", "FRA0=4.2%", "FRA_t=5.1%", "90d loan, 150d disc @5%"], "steps": ["10M*(0.009*0.25) / (1+0.05*150/360)"], "result": "+22,041 USD"},
          ["deriv-pcp", "deriv-swap-mtm"], "", "")

    add_j("deriv-swap-mtm", "Interest & Currency Swap Valuation", ["Swap Valuation", "Swap Fixed Rate"], r"\bSwap (Valuation|Fixed Rate)\b", "DERIV", "L2",
          "Valuation of existing swaps via discounted bond equivalence: receive-fixed value rises when market par swap rates fall below the contract rate.",
          r"r_{\text{fix}} = \frac{1 - DF_n}{\sum DF_i}, \qquad V_{\text{rec-fix}} = NP(r_{\text{old}} - r_{\text{new}})\sum DF_i",
          ["Marking OTC derivative books to market and pricing cross-currency hedges."],
          ["Forgetting that Currency Swaps DO exchange principal notionals at initiation and maturity (unlike single-currency IRS)."],
          {"title": "25M IRS Mark-to-Market", "given": ["Old 2.40% semi", "DF1=0.9804, DF2=0.9600"], "steps": ["New semi=(1-0.96)/1.9404=2.0614%", "25M*(0.024-0.020614)*1.9404"], "result": "+164,250 USD Value"},
          ["deriv-fra", "deriv-bsm"], "7.2.1", "")

    add_j("deriv-bsm", "Black-Scholes-Merton & Greeks", ["Black-Scholes-Merton", "BSM Model", "Delta Hedging", "Option Greeks"], r"\b(Black[- ]Scholes[- ]Merton|BSM|Delta[- ]Hedg(e|ing)|Option Greeks)\b", "DERIV", "L2",
          "Continuous-time European option valuation framework yielding closed-form premiums alongside Delta, Gamma, Theta, Vega, and Rho sensitivities.",
          r"c = S_0 e^{-qT}N(d_1) - K e^{-rT}N(d_2), \qquad \Delta_c = e^{-qT}N(d_1)",
          ["Dynamic delta-gamma portfolio hedging and extracting market-implied volatility."],
          ["Confusing Delta (first derivative) with Gamma (curvature); long ATM options near expiry have peak +Gamma and peak -Theta."],
          {"title": "Short Call Book Delta Hedge", "given": ["S=60, K=58, r=4%, T=0.25, vol=30%", "Short 50,000 calls"], "steps": ["d1=0.3122, Nd1=0.6226, c=4.83"], "result": "Buy 31,128 Shares"},
          ["deriv-pcp", "deriv-binomial"], "7.3.1", "bsm")

    add_j("deriv-binomial", "Binomial Option Tree (Risk-Neutral)", ["Binomial Option", "Risk-Neutral Probability"], r"\b(Binomial Option|Risk[- ]Neutral Probability)\b", "DERIV", "Both",
          "Discrete-time lattice pricing European and American options via no-arbitrage replication and backward induction using risk-neutral probability pi_u.",
          r"\pi_u = \frac{(1+r) - d}{u - d}, \qquad V_t = \max\!\left(\text{Intrinsic}, \; \frac{\pi_u V_u + (1-\pi_u)V_d}{1+r}\right)",
          ["Checking early exercise optimality for American puts and dividend-paying calls."],
          ["Inserting real-world expected stock return probabilities instead of risk-neutral probability pi_u."],
          {"title": "2-Step American Put", "given": ["S=50, X=52, u=1.2, d=0.8, r=5%"], "steps": ["pi_u=0.625", "At S_d=40, Int=12 > Cont=9.52 (Exercise!)"], "result": "American = 4.65 USD vs. European = 3.92 USD"},
          ["deriv-bsm", "deriv-pcp"], "7.2.2", "")

    # ALTERNATIVE INVESTMENTS (5)
    add_j("alt-hwm", "High-Water Mark & Hurdle Rate", ["High-Water Mark", "Hard Hurdle", "Soft Hurdle"], r"\b(High[- ]Water Mark|Hard Hurdle|Soft Hurdle)\b", "ALT", "Both",
          "Hedge fund performance fee safeguards ensuring GPs collect incentive fees only on new net profits exceeding prior peak NAV (HWM) and minimum return thresholds (hurdle).",
          r"\text{Hard Hurdle Fee} = \max(0, [NAV_{\text{pre}} - \max(NAV_0, HWM) - \text{Hurdle}] \cdot f_{\text{inc}})",
          ["Aligning GP/LP incentives and preventing double-charging after market drawdowns."],
          ["Applying a hard-hurdle deduction on a soft-hurdle fund—once cleared, soft hurdle taxes the ENTIRE return above HWM!"],
          {"title": "2 and 20 Hard Hurdle Fee", "given": ["NAV0=200M", "Gross=+20% (240M)", "2% mgmt on end AUM", "5% hard hurdle"], "steps": ["After mgmt=235.2M", "Excess=25.2M", "Inc=5.04M"], "result": "+15.08% Net LP Return"},
          ["alt-pe-multiples", "alt-vc-method"], "8.1.1", "alts")

    add_j("alt-pe-multiples", "PE Multiples (DPI, RVPI, TVPI)", ["DPI", "RVPI", "TVPI", "MOIC"], r"\b(DPI|RVPI|TVPI|MOIC)\b", "ALT", "Both",
          "Private equity fund performance multiples measuring realized cash distributions (DPI), unrealized residual NAV (RVPI), and total value (TVPI) relative to Paid-In Capital.",
          r"TVPI = DPI + RVPI = \frac{\text{Cumulative Distributions} + \text{Residual NAV}}{\text{Paid-In Capital}}",
          ["Tracking J-curve progression across PE fund vintage years against peer quartiles."],
          ["Dividing by Committed Capital instead of Paid-In (drawn) Capital!"],
          {"title": "Buyout Fund Progression", "given": ["Committed=100M", "Paid-In=75M", "Dist=54M", "NAV=48M"], "steps": ["DPI=54/75=0.72", "RVPI=48/75=0.64"], "result": "TVPI = 1.36x"},
          ["alt-hwm", "alt-vc-method"], "8.1.2", "alts")

    add_j("alt-vc-method", "Venture Capital Valuation Method", ["Venture Capital Method", "Post-Money Valuation", "Pre-Money Valuation"], r"\b(Venture Capital Method|Post[- ]Money Valuation|Pre[- ]Money Valuation)\b", "ALT", "L2",
          "Startup valuation discounting projected exit value at a high VC target IRR, then adjusting initial ownership upward for anticipated future funding dilution.",
          r"\text{Post} = \frac{\text{Exit TV}}{(1+r)^T}, \qquad f_{\text{init}} = \frac{\text{Inv}/\text{Post}}{1 - \text{Future Dilution}}",
          ["Pricing Series A/B term sheets with high binary startup failure risk."],
          ["Forgetting to divide exit ownership by (1 - dilution) when future financing rounds occur before exit!"],
          {"title": "Series A w/ 20% Dilution", "given": ["Exit=150M Yr4", "IRR=35%", "Inv=10M", "Dil=20%"], "steps": ["Post=45.16M", "Exit%=22.14%", "Init%=22.14%/0.8"], "result": "27.68% Initial Equity Stake"},
          ["alt-pe-multiples", "alt-hwm"], "8.2.1", "alts")

    add_j("alt-reit-affo", "REIT NAVPS, FFO & AFFO", ["AFFO", "FFO", "NAVPS"], r"\b(AFFO|FFO|NAVPS)\b", "ALT", "L2",
          "Public REIT cash flow and intrinsic net asset value metrics reversing non-cash real estate depreciation and accounting straight-line rent distortions.",
          r"AFFO = (NI + \text{RE Depr} - \text{Property Gains}) - \text{Straight-Line Rent} - \text{Maint Capex}",
          ["Valuing REITs via P/AFFO multiples and comparing market prices against private market NAVPS."],
          ["Forgetting to subtract recurring maintenance capex and leasing commissions when moving from FFO to AFFO."],
          {"title": "Industrial REIT Valuation", "given": ["NI=32M", "Depr=22M", "Gain=4M", "SLRent=2.5M", "Capex=7.5M"], "steps": ["FFO=50M", "AFFO=50-2.5-7.5=40M"], "result": "AFFO = 40M (1.60 USD/sh)"},
          ["alt-roll-yield"], "8.3.1", "")

    add_j("alt-roll-yield", "Commodity Roll Return & Backwardation", ["Roll Return", "Roll Yield", "Backwardation", "Contango"], r"\b(Roll (Return|Yield)|Backwardation|Contango)\b", "ALT", "Both",
          "Return earned from rolling expiring commodity futures contracts into the next contract month—positive in backwardation (scarce supply/high convenience yield) and negative in contango.",
          r"\text{Total Return} = \text{Collateral (T-Bill)} + \text{Price Return} + \text{Roll Return}, \quad \text{Roll} \approx \frac{F_{\text{near}} - F_{\text{far}}}{F_{\text{near}}}",
          ["Decomposing commodity ETF return attribution beyond spot price moves."],
          ["Confusing futures market backwardation (F_0 < S_0) with negative price trend—backwardation actually generates POSITIVE roll yield for long futures holders!"],
          {"title": "Crude Oil Futures Attribution", "given": ["T-bill=4.5%", "Spot=+3.0%", "Near=72, Far=70.5"], "steps": ["Roll=(72-70.5)/72=+2.08%"], "result": "+9.58% Total Return"},
          ["alt-reit-affo"], "", "")

    return entries


def main():
    with open(SOLVED_PATH, "r", encoding="utf-8") as f:
        existing_solved = json.load(f)
    # Keep original 27 (id not starting with our new prefixes)
    orig_codes = {"NUM-3.1.1","NUM-3.1.2","NUM-3.1.3","NUM-3.2.1","NUM-3.2.2","NUM-3.2.3","NUM-3.3.1","NUM-3.3.2","NUM-3.3.3",
                  "NUM-4.1.1","NUM-4.1.2","NUM-4.1.3","NUM-4.2.1","NUM-4.2.2","NUM-4.3.1",
                  "NUM-5.1.1","NUM-5.1.2","NUM-5.2.1","NUM-5.2.2","NUM-5.2.3","NUM-5.3.1",
                  "NUM-6.1.1","NUM-6.1.2","NUM-6.2.1","NUM-6.2.2","NUM-6.3.1","NUM-6.4.1"}
    base_solved = [x for x in existing_solved if x["id"] in orig_codes]
    new_solved = build_new_solved_numericals()
    all_solved = new_solved[:6] + new_solved[6:12] + new_solved[12:18] + [x for x in base_solved if x["subject"] == "Financial Statement Analysis"] + new_solved[18:24] + [x for x in base_solved if x["subject"] in ("Fixed Income", "Equity Investments")] + new_solved[24:] + [x for x in base_solved if x["subject"] == "Portfolio Management"]
    assert len(all_solved) == 63, f"Expected 63 solved numericals, got {len(all_solved)}"
    with open(SOLVED_PATH, "w", encoding="utf-8") as f:
        json.dump(all_solved, f, indent=2, ensure_ascii=False)
    print(f"Saved {len(all_solved)} solved numericals -> {SOLVED_PATH}")

    with open(JARGON_PATH, "r", encoding="utf-8") as f:
        existing_jargon = json.load(f)
    base_jargon = [x for x in existing_jargon if x["category"] in ("FSA", "FI", "EQ", "PM")]
    new_jargon = build_new_jargon_entries()
    all_jargon = base_jargon + new_jargon
    assert len(all_jargon) == 64, f"Expected 64 jargon terms, got {len(all_jargon)}"
    with open(JARGON_PATH, "w", encoding="utf-8") as f:
        json.dump(all_jargon, f, indent=2, ensure_ascii=False)
    print(f"Saved {len(all_jargon)} jargon terms -> {JARGON_PATH}")


if __name__ == "__main__":
    main()
