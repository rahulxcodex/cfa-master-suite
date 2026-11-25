"""
Generate 150 CFA Quantitative Methods questions (90 L1 + 60 L2 across 10 vignettes)
aligned with the 2027 CFA curriculum and save to data/courses/qm_qbank.json.
"""
import math
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from qbank_helper import add_l1, add_l2, norm_cdf, save_validated_json  # noqa: E402


# ---------------------------------------------------------------------------
# Exact Quantitative Helpers (Pure Standard Library)
# ---------------------------------------------------------------------------
def calc_irr(cfs: list[float], lo: float = -0.99, hi: float = 10.0) -> float:
    """Exact IRR via bisection on NPV(r) = 0."""
    def npv(r: float) -> float:
        return sum(cf / ((1.0 + r) ** t) for t, cf in enumerate(cfs))

    f_lo, f_hi = npv(lo), npv(hi)
    if f_lo * f_hi > 0:
        raise ValueError(f"IRR not bracketed for {cfs}")
    for _ in range(120):
        mid = 0.5 * (lo + hi)
        f_mid = npv(mid)
        if abs(f_mid) < 1e-12:
            return mid
        if f_lo * f_mid <= 0:
            hi, f_hi = mid, f_mid
        else:
            lo, f_lo = mid, f_mid
    return 0.5 * (lo + hi)


def pv_annuity(pmt: float, r: float, n: int, due: bool = False) -> float:
    pv = pmt * (1.0 - (1.0 + r) ** (-n)) / r
    return pv * (1.0 + r) if due else pv


def fv_annuity(pmt: float, r: float, n: int, due: bool = False) -> float:
    fv = pmt * (((1.0 + r) ** n) - 1.0) / r
    return fv * (1.0 + r) if due else fv


def geo_mean(rets: list[float]) -> float:
    prod = 1.0
    for r in rets:
        prod *= 1.0 + r
    return prod ** (1.0 / len(rets)) - 1.0


def harm_mean(vals: list[float]) -> float:
    return len(vals) / sum(1.0 / v for v in vals)


def sample_mean(xs: list[float]) -> float:
    return sum(xs) / len(xs)


def sample_var(xs: list[float]) -> float:
    m = sample_mean(xs)
    return sum((x - m) ** 2 for x in xs) / (len(xs) - 1)


def sample_sd(xs: list[float]) -> float:
    return math.sqrt(sample_var(xs))


def sample_cov(xs: list[float], ys: list[float]) -> float:
    mx, my = sample_mean(xs), sample_mean(ys)
    return sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / (len(xs) - 1)


def sample_corr(xs: list[float], ys: list[float]) -> float:
    return sample_cov(xs, ys) / (sample_sd(xs) * sample_sd(ys))


def target_semidev(xs: list[float], target: float) -> float:
    sq = sum((x - target) ** 2 for x in xs if x <= target)
    return math.sqrt(sq / (len(xs) - 1))


def sample_skewness(xs: list[float]) -> float:
    n = len(xs)
    m = sample_mean(xs)
    s = sample_sd(xs)
    return (n / ((n - 1) * (n - 2))) * sum(((x - m) / s) ** 3 for x in xs)


def sample_excess_kurtosis(xs: list[float]) -> float:
    n = len(xs)
    m = sample_mean(xs)
    s = sample_sd(xs)
    term1 = (n * (n + 1)) / ((n - 1) * (n - 2) * (n - 3))
    term1 *= sum(((x - m) / s) ** 4 for x in xs)
    term2 = (3.0 * ((n - 1) ** 2)) / ((n - 2) * (n - 3))
    return term1 - term2


def ols_simple(xs: list[float], ys: list[float]) -> dict:
    n = len(xs)
    mx, my = sample_mean(xs), sample_mean(ys)
    sxx = sum((x - mx) ** 2 for x in xs)
    syy = sum((y - my) ** 2 for y in ys)
    sxy = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    b1 = sxy / sxx
    b0 = my - b1 * mx
    ssr = b1 * sxy
    sse = syy - ssr
    r2 = ssr / syy
    see = math.sqrt(sse / (n - 2))
    msr = ssr
    mse = sse / (n - 2)
    f_stat = msr / mse
    se_b1 = see / math.sqrt(sxx)
    t_b1 = b1 / se_b1
    return {
        "n": n,
        "mx": mx,
        "my": my,
        "b0": b0,
        "b1": b1,
        "sxx": sxx,
        "syy": syy,
        "sxy": sxy,
        "ssr": ssr,
        "sse": sse,
        "r2": r2,
        "see": see,
        "msr": msr,
        "mse": mse,
        "f_stat": f_stat,
        "se_b1": se_b1,
        "t_b1": t_b1,
    }


def _simpson(f, a: float, b: float, steps: int = 2000) -> float:
    if steps % 2 == 1:
        steps += 1
    h = (b - a) / steps
    total = f(a) + f(b)
    for i in range(1, steps):
        total += (4.0 if i % 2 == 1 else 2.0) * f(a + i * h)
    return total * h / 3.0


def t_cdf(t_val: float, df: int) -> float:
    c = math.gamma((df + 1) / 2.0) / (math.sqrt(df * math.pi) * math.gamma(df / 2.0))
    pdf = lambda u: c * ((1.0 + (u * u) / df) ** (-(df + 1) / 2.0))
    if t_val >= 0:
        return 0.5 + _simpson(pdf, 0.0, t_val, 1000)
    return 0.5 - _simpson(pdf, 0.0, -t_val, 1000)


def t_crit_two_tailed(alpha: float, df: int) -> float:
    target = 1.0 - alpha / 2.0
    lo, hi = 0.0, 20.0
    for _ in range(60):
        mid = 0.5 * (lo + hi)
        if t_cdf(mid, df) < target:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def chi2_cdf(x: float, df: int) -> float:
    if x <= 0:
        return 0.0
    k = df / 2.0
    c = 1.0 / ((2.0 ** k) * math.gamma(k))
    pdf = lambda u: 0.0 if u <= 0 else c * (u ** (k - 1.0)) * math.exp(-u / 2.0)
    return _simpson(pdf, 1e-12, x, 2000)


def chi2_crit_upper(alpha: float, df: int) -> float:
    target = 1.0 - alpha
    lo, hi = 0.0, 100.0
    for _ in range(60):
        mid = 0.5 * (lo + hi)
        if chi2_cdf(mid, df) < target:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def f_cdf(x: float, df1: int, df2: int) -> float:
    if x <= 0:
        return 0.0
    a, b = df1 / 2.0, df2 / 2.0
    beta_val = math.gamma(a) * math.gamma(b) / math.gamma(a + b)
    c = ((df1 / df2) ** a) / beta_val
    pdf = lambda u: 0.0 if u <= 0 else c * (u ** (a - 1.0)) * ((1.0 + (df1 / df2) * u) ** (-(a + b)))
    return _simpson(pdf, 1e-12, x, 2000)


def f_crit_upper(alpha: float, df1: int, df2: int) -> float:
    target = 1.0 - alpha
    lo, hi = 0.01, 50.0
    for _ in range(60):
        mid = 0.5 * (lo + hi)
        if f_cdf(mid, df1, df2) < target:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


# ---------------------------------------------------------------------------
# Tracking & Integrity Validators
# ---------------------------------------------------------------------------
QUESTIONS: list[dict] = []
CALC_FLAGS: list[bool] = []
RE_CTRL = re.compile(r"[\x07\x08\x0b\x0c\r]")


def _check_strings(fields: list[str], qid: str):
    for s in fields:
        assert not RE_CTRL.search(s), f"{qid}: Stray control character in {s!r}"
        assert "{{" not in s, f"{qid}: Double curly brace in {s!r}"
        # Check brace balance inside $...$ blocks
        in_math = re.findall(r"\$\$(.*?)\$\$|\$(.*?)\$", s, flags=re.DOTALL)
        for m1, m2 in in_math:
            expr = m1 or m2
            assert expr.count("{") == expr.count("}"), f"{qid}: Unbalanced braces in math {expr!r}"


def q_l1(
    qid: str,
    module: str,
    topic: str,
    subtopic: str,
    los: str,
    is_calc: bool,
    question: str,
    options: dict,
    answer: str,
    explanation: str,
    distractors: dict,
):
    assert len({options["A"], options["B"], options["C"]}) == 3, f"{qid}: Duplicate options {options}"
    _check_strings(
        [question, explanation, options["A"], options["B"], options["C"]]
        + list(distractors.values()),
        qid,
    )
    add_l1(
        QUESTIONS,
        qid=qid,
        subject="Quantitative Methods",
        module=module,
        topic=topic,
        subtopic=subtopic,
        los=los,
        question=question,
        options=options,
        answer=answer,
        explanation=explanation,
        distractors=distractors,
    )
    CALC_FLAGS.append(is_calc)


def q_l2(
    qid: str,
    module: str,
    topic: str,
    subtopic: str,
    vignette_id: str,
    vignette_title: str,
    vignette_text: str,
    los: str,
    is_calc: bool,
    question: str,
    options: dict,
    answer: str,
    explanation: str,
    distractors: dict,
):
    assert len({options["A"], options["B"], options["C"]}) == 3, f"{qid}: Duplicate options {options}"
    _check_strings(
        [vignette_text, question, explanation, options["A"], options["B"], options["C"]]
        + list(distractors.values()),
        qid,
    )
    add_l2(
        QUESTIONS,
        qid=qid,
        subject="Quantitative Methods",
        module=module,
        topic=topic,
        subtopic=subtopic,
        vignette_id=vignette_id,
        global_vignette_id=vignette_id,
        vignette_title=vignette_title,
        vignette_text=vignette_text,
        los=los,
        question=question,
        options=options,
        answer=answer,
        explanation=explanation,
        distractors=distractors,
    )
    CALC_FLAGS.append(is_calc)


# ===========================================================================
# LEVEL 1 QUESTIONS (90 Questions: L1-QM-001 to L1-QM-090)
# ===========================================================================
def build_level_1():
    # -----------------------------------------------------------------------
    # LM 1: Rates and Returns (8 Qs: 001 - 008)
    # -----------------------------------------------------------------------
    p0, p1, div = 48.0, 53.40, 1.80
    hpr = (p1 - p0 + div) / p0
    d_nodiv = (p1 - p0) / p0
    d_endbase = (p1 - p0 + div) / p1
    q_l1(
        "L1-QM-001", "LM 1", "Rates and Returns", "Holding Period Return",
        "Calculate and interpret holding period returns.", True,
        rf"An investor buys a share for USD {p0:.2f}, receives a dividend of USD {div:.2f} at the end of the holding period, and sells the share for USD {p1:.2f}. The holding period return is *closest* to:",
        {"A": f"{d_nodiv*100:.2f}%", "B": f"{hpr*100:.2f}%", "C": f"{d_endbase*100:.2f}%"},
        "B",
        rf"The holding period return includes both capital appreciation and cash distributions: $$R = \frac{{P_1 - P_0 + D_1}}{{P_0}} = \frac{{{p1:.2f} - {p0:.2f} + {div:.2f}}}{{{p0:.2f}}} = {hpr*100:.2f}\%$$",
        {
            "A": rf"Omits the USD {div:.2f} dividend from total return, yielding only capital gain return ({d_nodiv*100:.2f}%).",
            "C": rf"Divides by ending price USD {p1:.2f} instead of initial investment USD {p0:.2f} ({d_endbase*100:.2f}%).",
        },
    )

    hpr_18m = 0.21
    ann_18m = (1.0 + hpr_18m) ** (12.0 / 18.0) - 1.0
    d_lin = hpr_18m * (12.0 / 18.0)
    d_inv = (1.0 + hpr_18m) ** (18.0 / 12.0) - 1.0
    q_l1(
        "L1-QM-002", "LM 1", "Rates and Returns", "Annualized Return",
        "Annualize returns over non-annual holding periods.", True,
        "A private credit fund earns a cumulative holding period return of 21.00% over an 18-month horizon. Its annualized rate of return is *closest* to:",
        {"A": f"{ann_18m*100:.2f}%", "B": f"{d_lin*100:.2f}%", "C": f"{d_inv*100:.2f}%"},
        "A",
        rf"To annualize an 18-month ($1.5$-year) cumulative return, compound over $12/18 = 2/3$ of a period: $$R_{{\text{{annual}}}} = (1 + 0.21)^{{12/18}} - 1 = {ann_18m*100:.2f}\%$$",
        {
            "B": rf"Incorrectly scales linearly ($21\% \times 12/18 = {d_lin*100:.2f}\%$) instead of geometric compounding.",
            "C": rf"Inverts the exponent ($18/12 = 1.5$), producing {d_inv*100:.2f}%.",
        },
    )

    cfs_mwr = [-100.0, -106.0, 260.0]
    mwr = calc_irr(cfs_mwr)
    r1_mwr = (110.0 + 4.0 - 100.0) / 100.0
    r2_mwr = (250.0 + 10.0 - 220.0) / 220.0
    twr_mwr = math.sqrt((1.0 + r1_mwr) * (1.0 + r2_mwr)) - 1.0
    arith_mwr = 0.5 * (r1_mwr + r2_mwr)
    q_l1(
        "L1-QM-003", "LM 1", "Rates and Returns", "Money-Weighted Return",
        "Calculate and interpret money-weighted and time-weighted rates of return.", True,
        "An investor purchases 1 share of an equity ETF at USD 100 at $t=0$. At $t=1$, the ETF pays a USD 4 dividend and trades at USD 110, and the investor buys 1 additional share at USD 110. At $t=2$, the ETF pays a USD 5 dividend per share and the investor sells both shares at USD 125 each. The money-weighted rate of return (MWR) is *closest* to:",
        {"A": f"{twr_mwr*100:.2f}%", "B": f"{arith_mwr*100:.2f}%", "C": f"{mwr*100:.2f}%"},
        "C",
        rf"Net cash flows are $CF_0 = -100$, $CF_1 = +4 - 110 = -106$, and $CF_2 = 2(5) + 2(125) = +260$. Solving $$-100 - \frac{{106}}{{1+\text{{IRR}}}} + \frac{{260}}{{(1+\text{{IRR}})^2}} = 0$$ gives $\text{{MWR}} = {mwr*100:.2f}\%$.",
        {
            "A": rf"Computes the geometric time-weighted return ({twr_mwr*100:.2f}%), ignoring the larger capital weight in Year 2.",
            "B": rf"Computes the simple arithmetic average of the two subperiod returns ({arith_mwr*100:.2f}%).",
        },
    )

    s1_r = (1120000.0 - 1000000.0) / 1000000.0
    s2_r = (1444000.0 - 1520000.0) / 1520000.0
    s3_r = (1368400.0 - 1244000.0) / 1244000.0
    twr3 = geo_mean([s1_r, s2_r, s3_r])
    arith3 = sample_mean([s1_r, s2_r, s3_r])
    cum3 = (1.0 + s1_r) * (1.0 + s2_r) * (1.0 + s3_r) - 1.0
    q_l1(
        "L1-QM-004", "LM 1", "Rates and Returns", "Time-Weighted Return",
        "Calculate and interpret money-weighted and time-weighted rates of return.", True,
        "A portfolio begins Year 1 at USD 1,000,000 and ends Year 1 at USD 1,120,000, when the client adds USD 400,000. It ends Year 2 at USD 1,444,000, when the client withdraws USD 200,000. It ends Year 3 at USD 1,368,400. The annualized time-weighted rate of return (TWR) is *closest* to:",
        {"A": f"{arith3*100:.2f}%", "B": f"{twr3*100:.2f}%", "C": f"{cum3*100:.2f}%"},
        "B",
        rf"Subperiod returns are $r_1 = \frac{{1.12 - 1.00}}{{1.00}} = 12.00\%$, $r_2 = \frac{{1.444 - 1.520}}{{1.520}} = -5.00\%$, and $r_3 = \frac{{1.3684 - 1.244}}{{1.244}} = 10.00\%$. Annualized TWR is $$[(1.12)(0.95)(1.10)]^{{1/3}} - 1 = {twr3*100:.2f}\%$$",
        {
            "A": rf"Uses the arithmetic mean of annual subperiod returns ({arith3*100:.2f}%) instead of geometric linking.",
            "C": rf"Reports the 3-year cumulative linked return ({cum3*100:.2f}%) without taking the cube root.",
        },
    )

    r_4y = [0.16, -0.10, 0.22, 0.04]
    gm4 = geo_mean(r_4y)
    am4 = sample_mean(r_4y)
    hm4 = harm_mean([1.0 + r for r in r_4y]) - 1.0
    q_l1(
        "L1-QM-005", "LM 1", "Rates and Returns", "Geometric vs Arithmetic Mean",
        "Calculate and interpret geometric and arithmetic mean returns.", True,
        "A small-cap strategy reports annual returns of 16.0%, -10.0%, 22.0%, and 4.0% over four consecutive years. Its compound annual geometric mean return is *closest* to:",
        {"A": f"{gm4*100:.2f}%", "B": f"{am4*100:.2f}%", "C": f"{hm4*100:.2f}%"},
        "A",
        rf"The geometric mean compounds wealth relatives: $$\bar{{R}}_G = [(1.16)(0.90)(1.22)(1.04)]^{{1/4}} - 1 = {gm4*100:.2f}\%$$",
        {
            "B": rf"Computes the arithmetic mean ({am4*100:.2f}%), which always exceeds the geometric mean when return volatility is positive.",
            "C": rf"Computes the harmonic mean of wealth relatives minus 1 ({hm4*100:.2f}%).",
        },
    )

    px_dca = [20.0, 25.0, 40.0]
    hm_px = harm_mean(px_dca)
    am_px = sample_mean(px_dca)
    gm_px = (20.0 * 25.0 * 40.0) ** (1.0 / 3.0)
    q_l1(
        "L1-QM-006", "LM 1", "Rates and Returns", "Harmonic Mean",
        "Calculate and interpret the harmonic mean in cost-averaging applications.", True,
        "An investor allocates USD 1,000 each month for three months to buy shares at prices of USD 20.00, USD 25.00, and USD 40.00, respectively. The effective average purchase price per share is *closest* to:",
        {"A": f"USD {am_px:.2f}", "B": f"USD {gm_px:.2f}", "C": f"USD {hm_px:.2f}"},
        "C",
        rf"With equal dollar outlays per period, the average cost per share equals the harmonic mean of share prices: $$\bar{{X}}_H = \frac{{3}}{{\frac{{1}}{{20}} + \frac{{1}}{{25}} + \frac{{1}}{{40}}}} = \text{{USD }}{hm_px:.2f}$$",
        {
            "A": rf"Uses the arithmetic mean price (USD {am_px:.2f}), which assumes equal shares purchased rather than equal dollar amounts.",
            "B": rf"Uses the geometric mean price (USD {gm_px:.2f}) instead of the harmonic mean.",
        },
    )

    nom_r, tax_r, inf_r = 0.095, 0.30, 0.025
    real_at = (1.0 + nom_r * (1.0 - tax_r)) / (1.0 + inf_r) - 1.0
    d_pretax_real = (1.0 + nom_r) / (1.0 + inf_r) - 1.0
    d_approx = nom_r - inf_r - nom_r * tax_r
    q_l1(
        "L1-QM-007", "LM 1", "Rates and Returns", "Real After-Tax Return",
        "Compare nominal, real, pre-tax, and after-tax returns.", True,
        "A taxable corporate bond portfolio earns a 9.50% nominal annual return when inflation is 2.50% and the investor's marginal tax rate is 30.0%. Using the exact Fisher relation, the real after-tax return is *closest* to:",
        {"A": f"{d_pretax_real*100:.2f}%", "B": f"{real_at*100:.2f}%", "C": f"{d_approx*100:.2f}%"},
        "B",
        rf"The nominal after-tax return is $9.50\% \times (1 - 0.30) = 6.65\%$. Adjusting exactly for inflation gives: $$r_{{\text{{real, after-tax}}}} = \frac{{1 + 0.0665}}{{1 + 0.025}} - 1 = {real_at*100:.2f}\%$$",
        {
            "A": rf"Omits the 30% tax drag and reports the pre-tax real return ({d_pretax_real*100:.2f}%).",
            "C": rf"Uses the linear approximation $r(1-t) - \pi = {d_approx*100:.2f}\%$ instead of dividing by $(1+\pi)$.",
        },
    )

    eq_inv, debt_inv, r_port, r_debt = 100.0, 50.0, 0.11, 0.05
    lev_ret = ((eq_inv + debt_inv) * r_port - debt_inv * r_debt) / eq_inv
    d_unlev = r_port
    d_gross = ((eq_inv + debt_inv) * r_port) / eq_inv
    q_l1(
        "L1-QM-008", "LM 1", "Rates and Returns", "Leveraged Return",
        "Calculate leveraged portfolio returns.", True,
        "An investor commits USD 100,000 of equity and borrows USD 50,000 at 5.0% annual interest to invest USD 150,000 in an index fund that returns 11.0% over the year. The leveraged return on equity is *closest* to:",
        {"A": f"{lev_ret*100:.2f}%", "B": f"{d_unlev*100:.2f}%", "C": f"{d_gross*100:.2f}%"},
        "A",
        rf"With leverage ratio $V_B/V_E = 0.50$: $$R_L = R_P + \frac{{V_B}}{{V_E}}(R_P - r_D) = 11.0\% + 0.50(11.0\% - 5.0\%) = {lev_ret*100:.2f}\%$$",
        {
            "B": rf"Reports the unleveraged portfolio return ({d_unlev*100:.2f}%).",
            "C": rf"Multiplies portfolio return by $1.5$ ({d_gross*100:.2f}%) without deducting the 5% margin borrowing cost.",
        },
    )

    # -----------------------------------------------------------------------
    # LM 2: Time Value of Money in Finance (9 Qs: 009 - 017)
    # -----------------------------------------------------------------------
    r_nom = 0.08
    ear_m = (1.0 + r_nom / 12.0) ** 12 - 1.0
    ear_c = math.exp(r_nom) - 1.0
    diff_bp = (ear_c - ear_m) * 10000.0
    ear_q = (1.0 + r_nom / 4.0) ** 4 - 1.0
    q_l1(
        "L1-QM-009", "LM 2", "Time Value of Money in Finance", "Compounding Frequencies & EAR",
        "Calculate effective annual rates across compounding frequencies.", True,
        "A bank offers a stated annual interest rate of 8.00%. How much higher is the effective annual rate (EAR) under continuous compounding compared with monthly compounding (in basis points)?",
        {"A": f"{diff_bp:.1f} bps", "B": f"{(ear_c - r_nom)*10000:.1f} bps", "C": f"{(ear_m - ear_q)*10000:.1f} bps"},
        "A",
        rf"Monthly compounding yields $\text{{EAR}}_m = (1 + 0.08/12)^{{12}} - 1 = {ear_m*100:.4f}\%$. Continuous compounding yields $\text{{EAR}}_c = e^{{0.08}} - 1 = {ear_c*100:.4f}\%$. The spread is ${(ear_c - ear_m)*10000:.1f}$ bps.",
        {
            "B": rf"Subtracts the 8.00% stated rate from the continuous EAR ({(ear_c - r_nom)*10000:.1f} bps) instead of the monthly EAR.",
            "C": rf"Computes the difference between monthly and quarterly compounding ({(ear_m - ear_q)*10000:.1f} bps).",
        },
    )

    pmt_ann, r_ann, n_ann = 50000.0, 0.06, 15
    pv_ord = pv_annuity(pmt_ann, r_ann, n_ann, due=False)
    pv_due = pv_annuity(pmt_ann, r_ann, n_ann, due=True)
    d_sum = pmt_ann * n_ann
    q_l1(
        "L1-QM-010", "LM 2", "Time Value of Money in Finance", "Annuity Due vs Ordinary Annuity",
        "Calculate the present value of annuities.", True,
        "An endowment requires USD 50,000 at the beginning of each year for 15 years, starting immediately ($t=0$). At an annual discount rate of 6.0%, the present value required today is *closest* to:",
        {"A": f"USD {pv_ord:,.0f}", "B": f"USD {pv_due:,.0f}", "C": f"USD {d_sum:,.0f}"},
        "B",
        rf"Payments begin immediately, making this an annuity due: $$PV_{{\text{{due}}}} = 50,000 \times \frac{{1 - 1.06^{{-15}}}}{{0.06}} \times 1.06 = \text{{USD }}{pv_due:,.2f}$$",
        {
            "A": rf"Treats the cash flows as an ordinary annuity starting at $t=1$ (USD {pv_ord:,.0f}), understating PV by a factor of $1.06$.",
            "C": rf"Sums nominal undiscounted cash flows (USD {d_sum:,.0f}).",
        },
    )

    pmt_perp, r_perp, start_t = 4.50, 0.09, 5
    pv_t4 = pmt_perp / r_perp
    pv_t0 = pv_t4 / ((1.0 + r_perp) ** (start_t - 1))
    d_t5 = pv_t4 / ((1.0 + r_perp) ** start_t)
    q_l1(
        "L1-QM-011", "LM 2", "Time Value of Money in Finance", "Deferred Perpetuity",
        "Calculate the present value of a deferred perpetuity.", True,
        "A preferred stock issue promises a perpetual annual dividend of USD 4.50 per share, with the first payment occurring exactly 5 years from today ($t=5$). Using a 9.0% required return, the intrinsic value per share at $t=0$ is *closest* to:",
        {"A": f"USD {pv_t0:.2f}", "B": f"USD {d_t5:.2f}", "C": f"USD {pv_t4:.2f}"},
        "A",
        rf"The perpetuity value one period before the first payment ($t=4$) is $PV_4 = 4.50 / 0.09 = \text{{USD }}{pv_t4:.2f}$. Discounting back 4 years gives $$PV_0 = \frac{{{pv_t4:.2f}}}{{1.09^4}} = \text{{USD }}{pv_t0:.2f}$$",
        {
            "B": rf"Discounts $PV_4$ back 5 years instead of 4 years (USD {d_t5:.2f}).",
            "C": rf"Reports $PV_4$ directly without discounting to $t=0$ (USD {pv_t4:.2f}).",
        },
    )

    loan_p, r_m_yr, yrs_l = 300000.0, 0.06, 30
    rm, nm = r_m_yr / 12.0, yrs_l * 12
    pmt_m = loan_p * rm / (1.0 - (1.0 + rm) ** (-nm))
    int1 = loan_p * rm
    prin1 = pmt_m - int1
    d_int = int1
    d_prin_wrong = pmt_m
    q_l1(
        "L1-QM-012", "LM 2", "Time Value of Money in Finance", "Loan Amortization",
        "Calculate amortized loan payments and principal reduction.", True,
        "A borrower takes a USD 300,000, 30-year fixed-rate mortgage with monthly payments at a 6.00% stated annual rate (compounded monthly). The principal repaid in the first monthly payment is *closest* to:",
        {"A": f"USD {d_int:,.2f}", "B": f"USD {d_prin_wrong:,.2f}", "C": f"USD {prin1:,.2f}"},
        "C",
        rf"Monthly rate is $r = 0.06/12 = 0.50\%$ over $N=360$ months, giving monthly payment $$\text{{PMT}} = \frac{{300,000(0.005)}}{{1 - 1.005^{{-360}}}} = \text{{USD }}{pmt_m:,.2f}$$ Month 1 interest is $300,000(0.005) = \text{{USD }}{int1:,.2f}$, so principal reduction is ${pmt_m:,.2f} - {int1:,.2f} = \text{{USD }}{prin1:,.2f}$.",
        {
            "A": rf"Reports the first month's interest expense (USD {d_int:,.2f}) rather than the principal portion.",
            "B": rf"Reports the entire monthly payment (USD {d_prin_wrong:,.2f}) without subtracting interest.",
        },
    )

    face_b, c_semi, y_semi, n_semi = 1000.0, 30.0, 0.035, 10
    p_bond = pv_annuity(c_semi, y_semi, n_semi) + face_b / ((1.0 + y_semi) ** n_semi)
    p_ann_err = pv_annuity(60.0, 0.07, 5) + face_b / (1.07 ** 5)
    p_disc_err = pv_annuity(30.0, 0.07, 10) + face_b / (1.07 ** 10)
    q_l1(
        "L1-QM-013", "LM 2", "Time Value of Money in Finance", "Fixed-Income TVM",
        "Apply time value of money to value fixed-income instruments.", True,
        "A 5-year corporate bond with a USD 1,000 par value pays a 6.0% annual coupon semi-annually. If the bond's yield to maturity is 7.0% compounded semi-annually, its price is *closest* to:",
        {"A": f"USD {p_ann_err:.2f}", "B": f"USD {p_bond:.2f}", "C": f"USD {p_disc_err:.2f}"},
        "B",
        rf"With 10 semi-annual periods, coupon is USD 30 and semi-annual YTM is $3.5\%$: $$PV = 30 \times \frac{{1 - 1.035^{{-10}}}}{{0.035}} + \frac{{1,000}}{{1.035^{{10}}}} = \text{{USD }}{p_bond:.2f}$$",
        {
            "A": rf"Uses annual compounding ($N=5, \text{{PMT}}=60, r=7\%$), yielding USD {p_ann_err:.2f}.",
            "C": rf"Uses semi-annual coupon USD 30 over $N=10$ periods but forgets to halve the 7.0% YTM (USD {p_disc_err:.2f}).",
        },
    )

    d0_ggm, g_ggm, r_ggm = 2.40, 0.04, 0.10
    p0_ggm = d0_ggm * (1.0 + g_ggm) / (r_ggm - g_ggm)
    d_d0_err = d0_ggm / (r_ggm - g_ggm)
    d_sum_err = d0_ggm * (1.0 + g_ggm) / (r_ggm + g_ggm)
    q_l1(
        "L1-QM-014", "LM 2", "Time Value of Money in Finance", "Equity TVM: Constant Growth",
        "Apply time value of money to value equity instruments.", True,
        "A mature utility company just paid an annual dividend of USD 2.40 per share. Dividends are expected to grow indefinitely at 4.0% per year, and the equity required return is 10.0%. The intrinsic share value is *closest* to:",
        {"A": f"USD {d_d0_err:.2f}", "B": f"USD {d_sum_err:.2f}", "C": f"USD {p0_ggm:.2f}"},
        "C",
        rf"Using the constant-growth DDM: $$P_0 = \frac{{D_0(1+g)}}{{r - g}} = \frac{{2.40(1.04)}}{{0.10 - 0.04}} = \text{{USD }}{p0_ggm:.2f}$$",
        {
            "A": rf"Uses trailing dividend $D_0$ instead of forward dividend $D_1$ (USD {d_d0_err:.2f}).",
            "B": rf"Adds $g$ to $r$ in the denominator instead of subtracting $g$ (USD {d_sum_err:.2f}).",
        },
    )

    d0_2s, g1_2s, g2_2s, r_2s = 2.00, 0.15, 0.04, 0.10
    d1_2s = d0_2s * (1.0 + g1_2s)
    d2_2s = d1_2s * (1.0 + g1_2s)
    d3_2s = d2_2s * (1.0 + g1_2s)
    d4_2s = d3_2s * (1.0 + g2_2s)
    p3_2s = d4_2s / (r_2s - g2_2s)
    p0_2s = d1_2s / (1.0 + r_2s) + d2_2s / ((1.0 + r_2s) ** 2) + (d3_2s + p3_2s) / ((1.0 + r_2s) ** 3)
    p0_err_disc4 = d1_2s / (1.0 + r_2s) + d2_2s / ((1.0 + r_2s) ** 2) + d3_2s / ((1.0 + r_2s) ** 3) + p3_2s / ((1.0 + r_2s) ** 4)
    p0_err_d3 = d1_2s / (1.0 + r_2s) + d2_2s / ((1.0 + r_2s) ** 2) + (d3_2s + d3_2s / (r_2s - g2_2s)) / ((1.0 + r_2s) ** 3)
    q_l1(
        "L1-QM-015", "LM 2", "Time Value of Money in Finance", "Multi-Stage Equity TVM",
        "Apply time value of money to multi-stage equity cash flows.", True,
        "A firm just paid a USD 2.00 dividend ($D_0$). Dividends will grow at 15.0% per year for the next three years ($t=1, 2, 3$) and then at 4.0% perpetually thereafter. If the required return is 10.0%, the stock's fair value today is *closest* to:",
        {"A": f"USD {p0_2s:.2f}", "B": f"USD {p0_err_disc4:.2f}", "C": f"USD {p0_err_d3:.2f}"},
        "A",
        rf"Projected dividends are $D_1={d1_2s:.2f}$, $D_2={d2_2s:.3f}$, $D_3={d3_2s:.4f}$, and $D_4={d4_2s:.4f}$. Terminal value at $t=3$ is $P_3 = D_4/(0.10-0.04) = \text{{USD }}{p3_2s:.2f}$. Discounting $D_1, D_2, D_3+P_3$ at 10% yields $$P_0 = \text{{USD }}{p0_2s:.2f}$$",
        {
            "B": rf"Incorrectly discounts terminal value $P_3$ over 4 periods instead of 3 periods (USD {p0_err_disc4:.2f}).",
            "C": rf"Computes $P_3 = D_3/(r - g_2)$ instead of $D_4/(r - g_2)$ (USD {p0_err_d3:.2f}).",
        },
    )

    s1_sp, s2_sp = 0.040, 0.052
    f11 = ((1.0 + s2_sp) ** 2) / (1.0 + s1_sp) - 1.0
    d_diff_f = 2 * s2_sp - s1_sp
    d_avg_f = 0.5 * (s1_sp + s2_sp)
    q_l1(
        "L1-QM-016", "LM 2", "Time Value of Money in Finance", "Cash Flow Additivity & Forward Rates",
        "Calculate implied forward rates using the cash flow additivity principle.", True,
        r"The 1-year zero-coupon spot rate is 4.00% and the 2-year zero-coupon spot rate is 5.20% (annual compounding). By cash flow additivity, the implied 1-year forward rate one year from now, $f_{1,1}$, is *closest* to:",
        {"A": f"{d_avg_f*100:.2f}%", "B": f"{f11*100:.2f}%", "C": f"{d_diff_f*100:.2f}%"},
        "B",
        rf"Equating a 2-year spot investment to a 1-year spot rolled into the 1-year forward rate: $$(1 + s_2)^2 = (1 + s_1)(1 + f_{{1,1}}) \implies f_{{1,1}} = \frac{{1.052^2}}{{1.04}} - 1 = {f11*100:.2f}\%$$",
        {
            "A": rf"Averages the two spot rates ({d_avg_f*100:.2f}%) instead of extracting the marginal Year 2 rate.",
            "C": rf"Uses the simple linear approximation $2 s_2 - s_1 = {d_diff_f*100:.2f}\%$ rather than exact geometric compounding.",
        },
    )

    q_l1(
        "L1-QM-017", "LM 2", "Time Value of Money in Finance", "Cash Flow Additivity Principle",
        "Explain the cash flow additivity principle in no-arbitrage pricing.", False,
        "Under the cash flow additivity principle, if two portfolios generate identical cash flows in every future period and state of the world, which statement is *most likely* correct?",
        {
            "A": "They must have the same present value in an arbitrage-free market even if their intermediate cash flows arrive on different schedules.",
            "B": "They must trade at identical market prices today to prevent riskless arbitrage profits.",
            "C": "Their internal rates of return must be equal regardless of differences in initial capital outlays.",
        },
        "B",
        "Cash flow additivity states that cash flows indexed at the same point in time are additive and that two assets or replicating bundles with identical future cash flows at identical dates must have identical current market prices to rule out arbitrage.",
        {
            "A": "Identical cash flows must match both in magnitude and timing; shifting cash flow timing alters present value.",
            "C": "If prices were different, IRRs would differ; equal IRRs require both cash flows and prices to be identical.",
        },
    )

    # -----------------------------------------------------------------------
    # LM 3: Statistical Measures of Asset Returns (9 Qs: 018 - 026)
    # -----------------------------------------------------------------------
    raw_w = [-2.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 15.0, 48.0]
    wins_w = [4.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 15.0, 15.0]
    w_mean = sample_mean(wins_w)
    t_mean = sample_mean(raw_w[1:-1])
    raw_mean = sample_mean(raw_w)
    q_l1(
        "L1-QM-018", "LM 3", "Statistical Measures of Asset Returns", "Trimmed and Winsorized Means",
        "Calculate measures of central tendency including trimmed and Winsorized means.", True,
        "A sorted sample of 10 monthly returns (%) is: `-2, 4, 5, 6, 7, 8, 9, 10, 15, 48`. The 10% Winsorized mean (replacing the lowest 10% and highest 10% of observations with the adjacent values) is *closest* to:",
        {"A": f"{w_mean:.2f}%", "B": f"{t_mean:.2f}%", "C": f"{raw_mean:.2f}%"},
        "A",
        rf"For $n=10$, a 10% Winsorized mean replaces the bottom 1 observation (-2) with 4 and the top 1 observation (48) with 15: $$\bar{{X}}_W = \frac{{4+4+5+6+7+8+9+10+15+15}}{{10}} = {w_mean:.2f}\%$$",
        {
            "B": rf"Computes the 10% trimmed mean ({t_mean:.2f}%), which discards the extreme observations and divides by 8 instead of 10.",
            "C": rf"Computes the unadjusted arithmetic mean ({raw_mean:.2f}%), allowing the 48% outlier to pull the mean upward.",
        },
    )

    sorted_q = [3.0, 5.0, 8.0, 11.0, 14.0, 18.0, 22.0]
    n_q = len(sorted_q)
    pos_30 = (n_q + 1) * 0.30  # 2.4 -> index 1 (5.0) + 0.4 * (8.0 - 5.0)
    val_30 = sorted_q[1] + 0.4 * (sorted_q[2] - sorted_q[1])
    d_nointerp = sorted_q[1]
    d_n_only = sorted_q[1] + 0.1 * (sorted_q[2] - sorted_q[1])  # 7 * 0.3 = 2.1
    q_l1(
        "L1-QM-019", "LM 3", "Statistical Measures of Asset Returns", "Quantiles & Percentiles",
        "Calculate and interpret quantiles using linear interpolation.", True,
        "Given the 7 sorted returns (%): `3.0, 5.0, 8.0, 11.0, 14.0, 18.0, 22.0`, the 30th percentile using the $(n+1)y/100$ position formula is *closest* to:",
        {"A": f"{d_nointerp:.1f}%", "B": f"{val_30:.1f}%", "C": f"{d_n_only:.1f}%"},
        "B",
        rf"The location is $L_{{30}} = (7 + 1) \times 0.30 = 2.4$. Interpolating 40% of the way from the 2nd value (5.0%) to the 3rd value (8.0%) gives $$P_{{30}} = 5.0 + 0.4(8.0 - 5.0) = {val_30:.1f}\%$$",
        {
            "A": rf"Truncates $L_{{30}} = 2.4$ to position 2 ({d_nointerp:.1f}%) without linear interpolation.",
            "C": rf"Uses $n \times y/100 = 2.1$ instead of $(n+1)y/100 = 2.4$, yielding {d_n_only:.1f}%.",
        },
    )

    xs_sd = [4.0, 8.0, 12.0, 10.0, 16.0]
    s_sd = sample_sd(xs_sd)
    p_sd = math.sqrt(sample_var(xs_sd) * (len(xs_sd) - 1) / len(xs_sd))
    s_var = sample_var(xs_sd)
    q_l1(
        "L1-QM-020", "LM 3", "Statistical Measures of Asset Returns", "Sample Standard Deviation",
        "Calculate sample variance and sample standard deviation.", True,
        "A portfolio posts five annual returns (%): `4.0, 8.0, 12.0, 10.0, 16.0`. Its sample standard deviation is *closest* to:",
        {"A": f"{p_sd:.2f}%", "B": f"{s_var:.2f}%", "C": f"{s_sd:.2f}%"},
        "C",
        rf"Sample mean is $\bar{{X}} = 10.0\%$. Sum of squared deviations is $(-6)^2 + (-2)^2 + 2^2 + 0^2 + 6^2 = 80$. Dividing by $n-1=4$ gives sample variance $s^2 = 20.0$, and $$s = \sqrt{{20.0}} = {s_sd:.2f}\%$$",
        {
            "A": rf"Divides by $n=5$ (population standard deviation = {p_sd:.2f}%) instead of $n-1=4$.",
            "B": rf"Reports sample variance ({s_var:.2f}) without taking the square root.",
        },
    )

    xs_semi = [12.0, 8.0, 2.0, -4.0, 5.0, 1.0]
    tgt_b = 4.0
    t_semi = target_semidev(xs_semi, tgt_b)
    d_n_denom = math.sqrt(sum((x - tgt_b) ** 2 for x in xs_semi if x <= tgt_b) / len(xs_semi))
    below_cnt = sum(1 for x in xs_semi if x <= tgt_b)
    d_sub_denom = math.sqrt(sum((x - tgt_b) ** 2 for x in xs_semi if x <= tgt_b) / (below_cnt - 1))
    q_l1(
        "L1-QM-021", "LM 3", "Statistical Measures of Asset Returns", "Target Semideviation",
        "Calculate and interpret target downside deviation.", True,
        "Monthly fund returns (%) over 6 periods are `12.0, 8.0, 2.0, -4.0, 5.0, 1.0`. Using a target return threshold of 4.0%, the sample target semideviation is *closest* to:",
        {"A": f"{t_semi:.2f}%", "B": f"{d_n_denom:.2f}%", "C": f"{d_sub_denom:.2f}%"},
        "A",
        rf"Observations at or below 4.0% are $2.0, -4.0, 1.0$. Deviations are $(2-4)^2 + (-4-4)^2 + (1-4)^2 = 4 + 64 + 9 = 77$. Dividing by total $n - 1 = 5$ gives $$s_{{\text{{Target}}}} = \sqrt{{\frac{{77}}{{5}}}} = {t_semi:.2f}\%$$",
        {
            "B": rf"Divides by $n=6$ instead of $n-1=5$ ({d_n_denom:.2f}%).",
            "C": rf"Divides by the count of below-target observations minus 1 ($3-1=2$) instead of total $n-1=5$ ({d_sub_denom:.2f}%).",
        },
    )

    m_f1, sd_f1 = 9.0, 12.0
    m_f2, sd_f2 = 14.0, 21.0
    cv1, cv2 = sd_f1 / m_f1, sd_f2 / m_f2
    q_l1(
        "L1-QM-022", "LM 3", "Statistical Measures of Asset Returns", "Coefficient of Variation",
        "Calculate and interpret the coefficient of variation.", True,
        "Fund Alpha has a mean return of 9.0% and standard deviation of 12.0%; Fund Beta has a mean return of 14.0% and standard deviation of 21.0%. Which fund has lower relative dispersion per unit of return, and what is its coefficient of variation (CV)?",
        {"A": f"Fund Alpha, CV = {cv1:.2f}", "B": f"Fund Beta, CV = {cv2:.2f}", "C": f"Fund Alpha, CV = {m_f1/sd_f1:.2f}"},
        "A",
        rf"Coefficient of variation is $\text{{CV}} = s / \bar{{X}}$. $\text{{CV}}_{{\text{{Alpha}}}} = 12.0 / 9.0 = {cv1:.2f}$, whereas $\text{{CV}}_{{\text{{Beta}}}} = 21.0 / 14.0 = {cv2:.2f}$. Lower CV indicates less dispersion per unit of mean return.",
        {
            "B": rf"Fund Beta has CV = {cv2:.2f}, which is higher than Fund Alpha's {cv1:.2f}.",
            "C": rf"Inverts the formula to $\bar{{X}} / s = {m_f1/sd_f1:.2f}$ (the return-to-risk ratio).",
        },
    )

    xs_sk = [-12.0, 2.0, 4.0, 5.0, 6.0]
    sk_val = sample_skewness(xs_sk)
    n_sk = len(xs_sk)
    sk_large = sum(((x - sample_mean(xs_sk)) / sample_sd(xs_sk)) ** 3 for x in xs_sk) / n_sk
    sk_abs = abs(sk_val)
    q_l1(
        "L1-QM-023", "LM 3", "Statistical Measures of Asset Returns", "Sample Skewness",
        "Calculate and interpret sample skewness.", True,
        "Five annual returns (%) for a strategy are `-12.0, 2.0, 4.0, 5.0, 6.0` (sample mean = 1.0%, sample SD = 7.42%). Using the exact small-sample formula, the sample skewness is *closest* to:",
        {"A": f"{sk_large:.2f}", "B": f"{sk_abs:.2f}", "C": f"{sk_val:.2f}"},
        "C",
        rf"Using $s = {sample_sd(xs_sk):.4f}$ and $n=5$: $$\text{{Skewness}} = \frac{{n}}{{(n-1)(n-2)}} \sum \left(\frac{{X_i - \bar{{X}}}}{{s}}\right)^3 = \frac{{5}}{{12}} \times ({sum(((x-1)/sample_sd(xs_sk))**3 for x in xs_sk):.4f}) = {sk_val:.2f}$$",
        {
            "A": rf"Uses the large-sample approximation $(1/n)\sum z_i^3 = {sk_large:.2f}$ rather than the small-sample unbiased adjustment.",
            "B": rf"Reverses the negative sign caused by the $-12.0\%$ left-tail observation ({sk_abs:.2f}).",
        },
    )

    q_l1(
        "L1-QM-024", "LM 3", "Statistical Measures of Asset Returns", "Skewness Distribution Ordering",
        "Contrast skewness characteristics across unimodal distributions.", False,
        "For a unimodal positively (right-) skewed return distribution, which ordering of central tendency measures is *most likely*?",
        {
            "A": "Mean < Median < Mode",
            "B": "Mode < Median < Mean",
            "C": "Median < Mode < Mean",
        },
        "B",
        "In a positively skewed unimodal distribution, a long right tail pulls the mean above the median, while the peak (mode) lies to the left of the median: Mode < Median < Mean.",
        {
            "A": "Describes a negatively (left-) skewed distribution, where extreme left-tail losses pull the mean below the median.",
            "C": "In a unimodal skewed distribution, the median always falls between the mode and the mean.",
        },
    )

    n_k, sum_z4 = 10, 38.0
    ke_val = ((n_k * (n_k + 1)) / ((n_k - 1) * (n_k - 2) * (n_k - 3))) * sum_z4 - (3.0 * (n_k - 1) ** 2) / ((n_k - 2) * (n_k - 3))
    ke_raw = ke_val + 3.0
    ke_large = (sum_z4 / n_k) - 3.0
    q_l1(
        "L1-QM-025", "LM 3", "Statistical Measures of Asset Returns", "Sample Excess Kurtosis",
        "Calculate and interpret sample excess kurtosis.", True,
        "For a sample of $n = 10$ quarterly returns, the sum of fourth powers of standardized deviations is $\\sum_{i=1}^{10} \\left(\\frac{X_i - \\bar{X}}{s}\\right)^4 = 38.0$. The sample excess kurtosis is *closest* to:",
        {"A": f"{ke_val:.2f}", "B": f"{ke_raw:.2f}", "C": f"{ke_large:.2f}"},
        "A",
        rf"Using the exact CFA small-sample excess kurtosis formula with $n=10$: $$K_E = \frac{{10(11)}}{{9(8)(7)}}(38.0) - \frac{{3(9^2)}}{{8(7)}} = {ke_val:.2f}$$ Because $K_E > 0$, the distribution is leptokurtic (fat-tailed).",
        {
            "B": rf"Adds 3 back or reports total kurtosis ({ke_raw:.2f}) instead of excess kurtosis relative to the normal benchmark of 3.",
            "C": rf"Uses the large-sample approximation $(38/10) - 3 = {ke_large:.2f}$, omitting small-sample degrees-of-freedom factors.",
        },
    )

    rx_c = [10.0, 4.0, -2.0, 8.0]
    ry_c = [14.0, 6.0, -6.0, 10.0]
    cov_xy = sample_cov(rx_c, ry_c)
    corr_xy = sample_corr(rx_c, ry_c)
    d_pop_cov = cov_xy * 3.0 / 4.0
    q_l1(
        "L1-QM-026", "LM 3", "Statistical Measures of Asset Returns", "Covariance & Correlation",
        "Calculate and interpret sample covariance and correlation.", True,
        "Over four years, Stock X returns (%) are `10, 4, -2, 8` and Stock Y returns (%) are `14, 6, -6, 10`. The sample correlation coefficient between X and Y is *closest* to:",
        {"A": f"{cov_xy:.2f}", "B": f"{corr_xy:.4f}", "C": f"{d_pop_cov:.2f}"},
        "B",
        rf"Means are $\bar{{X}} = 5\%$ and $\bar{{Y}} = 6\%$. Sample covariance is $\frac{{(5)(8)+(-1)(0)+(-7)(-12)+(3)(4)}}{{3}} = {cov_xy:.2f}$. Sample SDs are $s_X = {sample_sd(rx_c):.4f}$ and $s_Y = {sample_sd(ry_c):.4f}$, yielding $$r = \frac{{{cov_xy:.2f}}}{{{sample_sd(rx_c):.4f} \times {sample_sd(ry_c):.4f}}} = {corr_xy:.4f}$$",
        {
            "A": rf"Reports sample covariance ({cov_xy:.2f}) instead of dividing by $s_X s_Y$ to obtain correlation.",
            "C": rf"Reports population covariance ({d_pop_cov:.2f}) rather than correlation.",
        },
    )

    # -----------------------------------------------------------------------
    # LM 4: Probability Trees & Conditional Expectations (9 Qs: 027 - 035)
    # -----------------------------------------------------------------------
    probs_r = [0.25, 0.55, 0.20]
    eps_r = [4.20, 3.10, 1.50]
    exp_eps = sum(p * e for p, e in zip(probs_r, eps_r))
    d_simple = sample_mean(eps_r)
    d_mode = eps_r[1]
    q_l1(
        "L1-QM-027", "LM 4", "Probability Trees and Conditional Expectations", "Total Probability Rule",
        "Calculate unconditional expected values using the total probability rule.", True,
        "An analyst assigns probabilities of 25%, 55%, and 20% to strong growth, moderate growth, and recession scenarios, with expected EPS of USD 4.20, USD 3.10, and USD 1.50, respectively. Unconditional expected EPS is *closest* to:",
        {"A": f"USD {d_simple:.2f}", "B": f"USD {d_mode:.2f}", "C": f"USD {exp_eps:.2f}"},
        "C",
        rf"By the total probability rule for expected value: $$E(\text{{EPS}}) = 0.25(4.20) + 0.55(3.10) + 0.20(1.50) = \text{{USD }}{exp_eps:.2f}$$",
        {
            "A": rf"Takes an unweighted average of the three scenario EPS estimates (USD {d_simple:.2f}).",
            "B": rf"Selects the most likely (modal) outcome (USD {d_mode:.2f}) instead of probability-weighting all scenarios.",
        },
    )

    # Two-stage probability tree
    p_cut = 0.60
    p_cut_bull, p_cut_flat = 0.70, 0.30
    p_hold_bull, p_hold_flat = 0.25, 0.75
    r_paths = [
        (p_cut * p_cut_bull, 18.0),
        (p_cut * p_cut_flat, 6.0),
        ((1 - p_cut) * p_hold_bull, 10.0),
        ((1 - p_cut) * p_hold_flat, -2.0),
    ]
    exp_tree = sum(p * r for p, r in r_paths)
    var_tree = sum(p * ((r - exp_tree) ** 2) for p, r in r_paths)
    sd_tree = math.sqrt(var_tree)
    d_cond_cut = p_cut_bull * 18.0 + p_cut_flat * 6.0
    q_l1(
        "L1-QM-028", "LM 4", "Probability Trees and Conditional Expectations", "Probability Trees",
        "Use probability trees to compute unconditional expectations and variance.", True,
        "There is a 60% probability of a central bank rate cut and a 40% probability of rates holding steady. Conditional on a rate cut, a REIT returns +18% with 70% probability or +6% with 30% probability. Conditional on steady rates, it returns +10% with 25% probability or -2% with 75% probability. The unconditional expected return of the REIT is *closest* to:",
        {"A": f"{exp_tree:.2f}%", "B": f"{d_cond_cut:.2f}%", "C": f"{sd_tree:.2f}%"},
        "A",
        rf"Joint path probabilities and returns are $(0.42)(18\%) + (0.18)(6\%) + (0.10)(10\%) + (0.30)(-2\%) = {exp_tree:.2f}\%$.",
        {
            "B": rf"Computes only the conditional expected return given a rate cut ({d_cond_cut:.2f}%).",
            "C": rf"Reports the unconditional standard deviation ({sd_tree:.2f}%) instead of the expected return.",
        },
    )

    p_beat = 0.30
    p_pos_g_beat = 0.80
    p_pos_g_miss = 0.25
    p_pos = p_beat * p_pos_g_beat + (1.0 - p_beat) * p_pos_g_miss
    p_beat_g_pos = (p_beat * p_pos_g_beat) / p_pos
    d_joint = p_beat * p_pos_g_beat
    d_uncond = p_pos
    q_l1(
        "L1-QM-029", "LM 4", "Probability Trees and Conditional Expectations", "Bayes' Theorem",
        "Update probabilities using Bayes' formula.", True,
        "Historically, 30% of firms in a sector beat consensus earnings. A positive supply-chain signal occurs in 80% of beating firms and 25% of non-beating firms. Given a positive supply-chain signal, the updated probability that a firm beats consensus earnings is *closest* to:",
        {"A": f"{d_joint*100:.2f}%", "B": f"{p_beat_g_pos*100:.2f}%", "C": f"{d_uncond*100:.2f}%"},
        "B",
        rf"Unconditional probability of a positive signal is $P(S) = 0.30(0.80) + 0.70(0.25) = {p_pos:.3f}$. By Bayes' theorem: $$P(\text{{Beat}} \mid S) = \frac{{0.30 \times 0.80}}{{{p_pos:.3f}}} = {p_beat_g_pos*100:.2f}\%$$",
        {
            "A": rf"Reports the joint probability $P(\text{{Beat}} \cap S) = {d_joint*100:.2f}\%$ without dividing by $P(S)$.",
            "C": rf"Reports the unconditional probability of the signal $P(S) = {d_uncond*100:.2f}\%$.",
        },
    )

    p_mna = 0.375
    odds_for = p_mna / (1.0 - p_mna)  # 3/5 -> 3 to 5
    q_l1(
        "L1-QM-030", "LM 4", "Probability Trees and Conditional Expectations", "Odds and Implied Probability",
        "Convert between probabilities and odds.", True,
        "An event-driven fund implies odds against a merger closing of 5 to 3. The implied probability that the merger closes is *closest* to:",
        {"A": "62.5%", "B": "60.0%", "C": "37.5%"},
        "C",
        rf"Odds against an event of $b$ to $a$ imply probability $P(E) = \frac{{a}}{{a + b}} = \frac{{3}}{{3 + 5}} = 37.5\%$ (equivalently, odds for the merger are 3 to 5, or {odds_for:.2f}).",
        {
            "A": "Reports the complement probability that the merger fails to close (5 / 8 = 62.5%).",
            "B": "Divides 3 by 5 (60.0%) instead of dividing by total outcomes (3 + 5 = 8).",
        },
    )

    n_bin, p_bin, k_bin = 6, 0.20, 2
    p_x2 = math.comb(n_bin, k_bin) * (p_bin ** k_bin) * ((1.0 - p_bin) ** (n_bin - k_bin))
    p_x1 = math.comb(n_bin, 1) * (p_bin ** 1) * ((1.0 - p_bin) ** 5)
    p_no_comb = (p_bin ** k_bin) * ((1.0 - p_bin) ** (n_bin - k_bin))
    q_l1(
        "L1-QM-031", "LM 4", "Probability Trees and Conditional Expectations", "Binomial Distribution",
        "Calculate probabilities using the binomial distribution.", True,
        "Six independent high-yield bonds each have a 20% probability of default over the next three years. The probability that *exactly* two of the six bonds default is *closest* to:",
        {"A": f"{p_x2*100:.2f}%", "B": f"{p_x1*100:.2f}%", "C": f"{p_no_comb*100:.2f}%"},
        "A",
        rf"Using the binomial PMF with $n=6, k=2, p=0.20$: $$P(X=2) = \binom{{6}}{{2}}(0.20)^2(0.80)^4 = 15(0.04)(0.4096) = {p_x2*100:.2f}\%$$",
        {
            "B": rf"Computes $P(X=1) = {p_x1*100:.2f}\%$ instead of $P(X=2)$.",
            "C": rf"Omits the binomial coefficient $\binom{{6}}{{2}} = 15$, yielding {p_no_comb*100:.2f}%.",
        },
    )

    mu_n, sd_n, x_n = 8.0, 12.0, 20.0
    z_n = (x_n - mu_n) / sd_n
    prob_gt = 1.0 - norm_cdf(z_n)
    prob_lt = norm_cdf(z_n)
    prob_2t = 2.0 * prob_gt
    q_l1(
        "L1-QM-032", "LM 4", "Probability Trees and Conditional Expectations", "Normal Distribution Probabilities",
        "Calculate probabilities for a normally distributed return.", True,
        "Portfolio returns are normally distributed with a mean of 8.0% and standard deviation of 12.0%. Given $N(1.00) = 0.8413$, the probability that next year's return exceeds 20.0% is *closest* to:",
        {"A": f"{prob_lt*100:.2f}%", "B": f"{prob_gt*100:.2f}%", "C": f"{prob_2t*100:.2f}%"},
        "B",
        rf"Standardizing $X=20.0\%$: $z = (20 - 8)/12 = +1.00$. Thus $$P(X > 20\%) = 1 - N(1.00) = 1 - 0.8413 = {prob_gt*100:.2f}\%$$",
        {
            "A": rf"Reports $P(X \le 20\%) = N(1.00) = {prob_lt*100:.2f}\%$ rather than the upper tail.",
            "C": rf"Doubles the single tail probability ({prob_2t*100:.2f}%).",
        },
    )

    mu_v, sd_v, z_05 = 9.0, 16.0, -1.645
    r_5pct = mu_v + z_05 * sd_v
    r_1pct = mu_v - 2.326 * sd_v
    r_95pct = mu_v - z_05 * sd_v
    q_l1(
        "L1-QM-033", "LM 4", "Probability Trees and Conditional Expectations", "Normal Tail Quantiles",
        "Calculate return thresholds corresponding to normal distribution quantiles.", True,
        r"A portfolio's annual return is normally distributed with mean 9.0% and standard deviation 16.0%. Using $z_{0.05} = -1.645$, the 5th percentile return threshold is *closest* to:",
        {"A": f"{r_1pct:.2f}%", "B": f"{r_95pct:.2f}%", "C": f"{r_5pct:.2f}%"},
        "C",
        rf"The 5th percentile lies $1.645$ standard deviations below the mean: $$R_{{0.05}} = 9.0\% + (-1.645)(16.0\%) = {r_5pct:.2f}\%$$",
        {
            "A": rf"Uses the 1% critical value ($z = -2.326$), yielding {r_1pct:.2f}%.",
            "B": rf"Adds rather than subtracts $1.645\sigma$ ({r_95pct:.2f}%), giving the 95th percentile.",
        },
    )

    q_l1(
        "L1-QM-034", "LM 4", "Probability Trees and Conditional Expectations", "Lognormal vs Normal Properties",
        "Contrast properties of normal and lognormal distributions.", False,
        "Why is the lognormal distribution commonly used to model future asset *prices*, whereas the normal distribution is used to model continuously compounded *returns*?",
        {
            "A": "A lognormal random variable is symmetric and bounded between -100% and +100%.",
            "B": "A lognormal random variable is positively skewed and bounded below by zero, preventing negative asset prices.",
            "C": "The lognormal distribution has zero excess kurtosis, matching empirical daily equity returns.",
        },
        "B",
        "If continuously compounded return $r = \\ln(S_T/S_0)$ is normally distributed, then $S_T = S_0 e^r$ follows a lognormal distribution, which is positively skewed and strictly positive ($S_T > 0$), reflecting limited liability.",
        {
            "A": "Lognormal distributions are positively skewed and unbounded above, not symmetric or capped at +100%.",
            "C": "Lognormal distributions exhibit positive skewness and excess kurtosis, and empirical daily returns typically display leptokurtosis.",
        },
    )

    # Joint probability expectation & covariance preview
    # States: Boom (0.3): A=15%, B=10%; Base (0.5): A=7%, B=6%; Bust (0.2): A=-5%, B=0%
    p_st = [0.30, 0.50, 0.20]
    ra_st = [15.0, 7.0, -5.0]
    rb_st = [10.0, 6.0, 0.0]
    ea = sum(p * a for p, a in zip(p_st, ra_st))
    eb = sum(p * b for p, b in zip(p_st, rb_st))
    cov_st = sum(p * (a - ea) * (b - eb) for p, a, b in zip(p_st, ra_st, rb_st))
    d_ea = ea
    d_unwt_cov = sum((a - sample_mean(ra_st)) * (b - sample_mean(rb_st)) for a, b in zip(ra_st, rb_st)) / 2.0
    q_l1(
        "L1-QM-035", "LM 4", "Probability Trees and Conditional Expectations", "Probability-Weighted Covariance",
        "Calculate covariance from a joint probability model.", True,
        r"Stocks A and B have returns across Boom ($p=0.30$), Base ($p=0.50$), and Bust ($p=0.20$) states of $(15\%, 10\%)$, $(7\%, 6\%)$, and $(-5\%, 0\%)$, respectively. The covariance between returns (in percent squared) is *closest* to:",
        {"A": f"{cov_st:.2f}", "B": f"{d_unwt_cov:.2f}", "C": f"{d_ea:.2f}"},
        "A",
        rf"Expected returns are $E(R_A) = {ea:.2f}\%$ and $E(R_B) = {eb:.2f}\%$. Probability-weighted covariance is $$\text{{Cov}}(R_A, R_B) = 0.3(15-7)(10-6) + 0.5(7-7)(6-6) + 0.2(-5-7)(0-6) = {cov_st:.2f}$$",
        {
            "B": rf"Computes an equally weighted sample covariance across the three states ({d_unwt_cov:.2f}) instead of probability-weighting.",
            "C": rf"Reports $E(R_A) = {d_ea:.2f}$ instead of the covariance.",
        },
    )

    # -----------------------------------------------------------------------
    # LM 5: Portfolio Mathematics (8 Qs: 036 - 043)
    # -----------------------------------------------------------------------
    w1, w2 = 0.60, 0.40
    sd1, sd2, rho12 = 0.15, 0.25, 0.20
    var_p2 = (w1 ** 2) * (sd1 ** 2) + (w2 ** 2) * (sd2 ** 2) + 2.0 * w1 * w2 * rho12 * sd1 * sd2
    sd_p2 = math.sqrt(var_p2)
    sd_p2_nocov = math.sqrt((w1 ** 2) * (sd1 ** 2) + (w2 ** 2) * (sd2 ** 2))
    sd_p2_wavg = w1 * sd1 + w2 * sd2
    q_l1(
        "L1-QM-036", "LM 5", "Portfolio Mathematics", "Two-Asset Portfolio Risk",
        "Calculate portfolio expected return and standard deviation.", True,
        "A portfolio holds 60% in Equities ($\\sigma = 15.0\\%$) and 40% in Commodities ($\\sigma = 25.0\\%$), with a return correlation of $+0.20$. The portfolio standard deviation is *closest* to:",
        {"A": f"{sd_p2_nocov*100:.2f}%", "B": f"{sd_p2*100:.2f}%", "C": f"{sd_p2_wavg*100:.2f}%"},
        "B",
        rf"Portfolio variance is $\sigma_p^2 = 0.6^2(0.15^2) + 0.4^2(0.25^2) + 2(0.6)(0.4)(0.20)(0.15)(0.25) = {var_p2:.6f}$, so $$\sigma_p = \sqrt{{{var_p2:.6f}}} = {sd_p2*100:.2f}\%$$",
        {
            "A": rf"Omits the covariance term $2 w_1 w_2 \rho \sigma_1 \sigma_2$, giving {sd_p2_nocov*100:.2f}%.",
            "C": rf"Takes a simple weighted average of standard deviations ({sd_p2_wavg*100:.2f}%), which assumes $\rho = +1.0$.",
        },
    )

    # Solving implied correlation
    wa, wb, sda, sdb, sdp_obs = 0.50, 0.50, 0.20, 0.12, 0.14
    cov_imp = (sdp_obs ** 2 - (wa * sda) ** 2 - (wb * sdb) ** 2) / (2.0 * wa * wb)
    rho_imp = cov_imp / (sda * sdb)
    d_cov_only = cov_imp * 100
    d_wrong_denom = (sdp_obs ** 2 - (wa * sda) ** 2 - (wb * sdb) ** 2) / (wa * wb * sda * sdb)
    q_l1(
        "L1-QM-037", "LM 5", "Portfolio Mathematics", "Implied Portfolio Correlation",
        "Infer asset correlation from portfolio variance.", True,
        "An equally weighted two-asset portfolio has standard deviation 14.0%. If Asset A has $\\sigma_A = 20.0\\%$ and Asset B has $\\sigma_B = 12.0\\%$, the correlation between Asset A and Asset B is *closest* to:",
        {"A": f"{rho_imp:.3f}", "B": f"{d_wrong_denom:.3f}", "C": f"{d_cov_only:.3f}"},
        "A",
        rf"Solving $0.14^2 = 0.5^2(0.20^2) + 0.5^2(0.12^2) + 2(0.5)(0.5)\rho(0.20)(0.12)$ gives $0.0196 = 0.0136 + 0.012\rho$, so $\rho = {rho_imp:.3f}$.",
        {
            "B": rf"Forgets the factor of 2 in $2 w_A w_B \text{{Cov}}$, doubling the correlation ({d_wrong_denom:.3f}).",
            "C": rf"Reports covariance scaled by 100 ({d_cov_only:.3f}) instead of dividing by $\sigma_A \sigma_B$.",
        },
    )

    s1_mv, s2_mv, rho_mv = 0.12, 0.20, 0.25
    cov_mv = rho_mv * s1_mv * s2_mv
    w1_mv = (s2_mv ** 2 - cov_mv) / (s1_mv ** 2 + s2_mv ** 2 - 2.0 * cov_mv)
    w1_mv_nocov = (s2_mv ** 2) / (s1_mv ** 2 + s2_mv ** 2)
    w2_mv = 1.0 - w1_mv
    q_l1(
        "L1-QM-038", "LM 5", "Portfolio Mathematics", "Minimum-Variance Weights",
        "Determine minimum-variance portfolio weights.", True,
        "Asset 1 has $\\sigma_1 = 12\\%$, Asset 2 has $\\sigma_2 = 20\\%$, and their correlation is $\\rho = +0.25$. The weight in Asset 1 for the global minimum-variance portfolio is *closest* to:",
        {"A": f"{w1_mv_nocov*100:.1f}%", "B": f"{w2_mv*100:.1f}%", "C": f"{w1_mv*100:.1f}%"},
        "C",
        rf"With $\text{{Cov}}_{{1,2}} = 0.25(0.12)(0.20) = 0.0060$: $$w_1 = \frac{{\sigma_2^2 - \text{{Cov}}_{{1,2}}}}{{\sigma_1^2 + \sigma_2^2 - 2\text{{Cov}}_{{1,2}}}} = \frac{{0.0400 - 0.0060}}{{0.0144 + 0.0400 - 0.0120}} = {w1_mv*100:.1f}\%$$",
        {
            "A": rf"Omits covariance from numerator and denominator ({w1_mv_nocov*100:.1f}%).",
            "B": rf"Reports the complementary weight in Asset 2 ({w2_mv*100:.1f}%).",
        },
    )

    w3 = [0.50, 0.30, 0.20]
    cov3 = [
        [0.0400, 0.0120, 0.0080],
        [0.0120, 0.0225, 0.0045],
        [0.0080, 0.0045, 0.0100],
    ]
    var3 = sum(w3[i] * w3[j] * cov3[i][j] for i in range(3) for j in range(3))
    sd3 = math.sqrt(var3)
    var3_diag = sum((w3[i] ** 2) * cov3[i][i] for i in range(3))
    sd3_diag = math.sqrt(var3_diag)
    q_l1(
        "L1-QM-039", "LM 5", "Portfolio Mathematics", "Three-Asset Portfolio Variance",
        "Calculate portfolio variance using a covariance matrix.", True,
        "A three-asset portfolio has weights $w = (0.50, 0.30, 0.20)$. Variances are $(0.0400, 0.0225, 0.0100)$, and pairwise covariances are $\\text{Cov}_{1,2} = 0.0120$, $\\text{Cov}_{1,3} = 0.0080$, and $\\text{Cov}_{2,3} = 0.0045$. Portfolio standard deviation is *closest* to:",
        {"A": f"{sd3*100:.2f}%", "B": f"{sd3_diag*100:.2f}%", "C": f"{var3*100:.2f}%"},
        "A",
        rf"Summing all 9 matrix terms $\sum_i \sum_j w_i w_j \text{{Cov}}_{{ij}}$ gives $\sigma_p^2 = {var3:.6f}$, so $$\sigma_p = \sqrt{{{var3:.6f}}} = {sd3*100:.2f}\%$$",
        {
            "B": rf"Includes only the three diagonal variance terms and omits all off-diagonal covariances ({sd3_diag*100:.2f}%).",
            "C": rf"Reports portfolio variance scaled by 100 ({var3*100:.2f}%) without taking the square root.",
        },
    )

    p_f, a_f, b_f = [0.40, 0.60], [16.0, 4.0], [10.0, 2.0]
    ea_f = sum(p * a for p, a in zip(p_f, a_f))
    eb_f = sum(p * b for p, b in zip(p_f, b_f))
    cov_f = sum(p * (a - ea_f) * (b - eb_f) for p, a, b in zip(p_f, a_f, b_f))
    d_wrong_cov = (16 - 4) * (10 - 2) * 0.4 * 0.6 * 2
    d_mean_prod = ea_f * eb_f
    q_l1(
        "L1-QM-040", "LM 5", "Portfolio Mathematics", "Two-State Joint Covariance",
        "Calculate covariance from joint probability trees.", True,
        "In an expansion (probability 40%), Fund X returns 16% and Fund Y returns 10%. In a slowdown (probability 60%), Fund X returns 4% and Fund Y returns 2%. Covariance between Fund X and Fund Y (in percent squared) is *closest* to:",
        {"A": f"{d_mean_prod:.2f}", "B": f"{cov_f:.2f}", "C": f"{d_wrong_cov:.2f}"},
        "B",
        rf"Expected returns are $E(R_X) = {ea_f:.1f}\%$ and $E(R_Y) = {eb_f:.1f}\%$. Covariance is $0.40(16-8.8)(10-5.2) + 0.60(4-8.8)(2-5.2) = {cov_f:.2f}$.",
        {
            "A": rf"Multiplies $E(R_X) E(R_Y) = {d_mean_prod:.2f}$ instead of probability-weighted mean deviations.",
            "C": rf"Doubles the cross-product deviation ({d_wrong_cov:.2f}).",
        },
    )

    # Roy's Safety-First
    rl = 3.0
    ports = [("Portfolio X", 9.0, 12.0), ("Portfolio Y", 11.0, 15.0), ("Portfolio Z", 14.0, 22.0)]
    sfs = [(name, (er - rl) / sd) for name, er, sd in ports]
    best_sf = max(sfs, key=lambda t: t[1])
    q_l1(
        "L1-QM-041", "LM 5", "Portfolio Mathematics", "Roy's Safety-First Criterion",
        "Apply Roy's safety-first criterion to select an optimal portfolio.", True,
        r"A foundation requires a minimum threshold return ($R_L$) of 3.0%. Candidate portfolios are X ($E(R)=9.0\%, \sigma=12.0\%$), Y ($E(R)=11.0\%, \sigma=15.0\%$), and Z ($E(R)=14.0\%, \sigma=22.0\%$). According to Roy's safety-first criterion, the optimal portfolio and its SFRatio are:",
        {
            "A": f"Portfolio X (SFRatio = {sfs[0][1]:.3f})",
            "B": f"Portfolio Z (SFRatio = {sfs[2][1]:.3f})",
            "C": f"Portfolio Y (SFRatio = {sfs[1][1]:.3f})",
        },
        "C",
        rf"Roy's safety-first ratio is $\text{{SFRatio}} = [E(R_p) - R_L]/\sigma_p$. Values are X: ${sfs[0][1]:.3f}$, Y: ${sfs[1][1]:.3f}$, and Z: ${sfs[2][1]:.3f}$. {best_sf[0]} maximizes SFRatio.",
        {
            "A": rf"Portfolio X has the lowest volatility, but its SFRatio ({sfs[0][1]:.3f}) is below Portfolio Y's ({sfs[1][1]:.3f}).",
            "B": rf"Portfolio Z has the highest expected return, but its high volatility reduces its SFRatio to {sfs[2][1]:.3f}.",
        },
    )

    sf_opt = best_sf[1]
    p_short = norm_cdf(-sf_opt)
    p_above = norm_cdf(sf_opt)
    p_two_t = 2.0 * p_short
    q_l1(
        "L1-QM-042", "LM 5", "Portfolio Mathematics", "Shortfall Risk Probability",
        "Calculate shortfall probability under normality using Roy's safety-first ratio.", True,
        f"Assuming normal returns, for a portfolio with an expected return of 11.0%, standard deviation of 15.0%, and minimum threshold return $R_L = 3.0\\%$ ($\\text{{SFRatio}} = {sf_opt:.3f}$; $N({sf_opt:.3f}) = {p_above:.4f}$), the probability of falling below 3.0% is *closest* to:",
        {"A": f"{p_above*100:.2f}%", "B": f"{p_short*100:.2f}%", "C": f"{p_two_t*100:.2f}%"},
        "B",
        rf"Shortfall probability is $P(R_p < R_L) = N(-\text{{SFRatio}}) = 1 - N({sf_opt:.3f}) = 1 - {p_above:.4f} = {p_short*100:.2f}\%$.",
        {
            "A": rf"Reports $N(+\text{{SFRatio}}) = {p_above*100:.2f}\%$, which is the probability of *exceeding* the threshold.",
            "C": rf"Doubles the one-tailed shortfall probability ({p_two_t*100:.2f}%).",
        },
    )

    q_l1(
        "L1-QM-043", "LM 5", "Portfolio Mathematics", "Diversification & Covariance Limit",
        "Explain how correlation and portfolio size affect diversification.", False,
        "As the number of assets $N$ in an equally weighted portfolio grows very large ($N \\to \\infty$), the portfolio's variance converges toward:",
        {
            "A": "The average variance of the individual securities.",
            "B": "Zero, provided all pairwise correlations are strictly less than +1.0.",
            "C": "The average pairwise covariance among the securities.",
        },
        "C",
        "For an equally weighted portfolio, $\\sigma_p^2 = \\frac{1}{N}\\bar{\\sigma}^2 + \\frac{N-1}{N}\\overline{\\text{Cov}}$. As $N \\to \\infty$, idiosyncratic variance vanishes ($1/N \\to 0$) and portfolio variance converges to average covariance $\\overline{\\text{Cov}}$.",
        {
            "A": "Individual security variance diversifies away as $1/N \\to 0$.",
            "B": "Non-zero positive systematic covariance cannot be diversified away regardless of how large $N$ becomes.",
        },
    )

    # -----------------------------------------------------------------------
    # LM 6: Simulation Methods (7 Qs: 044 - 050)
    # -----------------------------------------------------------------------
    s0_ln, mu_ln, sig_ln, t_ln = 100.0, 0.08, 0.20, 1.0
    # 95% CI for S_T using mean log return mu*T (or (mu - 0.5*sig^2)*T? Specify continuously compounded annual return r ~ N(8%, 20%^2))
    lo_s = s0_ln * math.exp(mu_ln - 1.96 * sig_ln)
    hi_s = s0_ln * math.exp(mu_ln + 1.96 * sig_ln)
    hi_norm_err = s0_ln * (1.0 + mu_ln + 1.96 * sig_ln)
    q_l1(
        "L1-QM-044", "LM 6", "Simulation Methods", "Lognormal Stock Price Bounds",
        "Apply lognormal return distributions to price boundaries.", True,
        "A stock currently trades at USD 100.00. Its 1-year continuously compounded return follows $r \\sim N(0.08, 0.20^2)$. The upper bound of a 95% confidence interval ($z = \\pm 1.96$) for the stock price in 1 year is *closest* to:",
        {"A": f"USD {hi_s:.2f}", "B": f"USD {hi_norm_err:.2f}", "C": f"USD {lo_s:.2f}"},
        "A",
        rf"The 95% interval for continuously compounded return is $0.08 \pm 1.96(0.20) = [{mu_ln-1.96*sig_ln:.4f}, {mu_ln+1.96*sig_ln:.4f}]$. Exponentiating gives upper price $$S_{{0.975}} = 100 \times e^{{{mu_ln + 1.96*sig_ln:.4f}}} = \text{{USD }}{hi_s:.2f}$$",
        {
            "B": rf"Applies simple linear return $100(1 + 0.472) = \text{{USD }}{hi_norm_err:.2f}$ instead of exponentiating the continuously compounded return.",
            "C": rf"Reports the lower bound of the 95% interval (USD {lo_s:.2f}).",
        },
    )

    payoffs_mc = [0.0, 12.0, 0.0, 18.0, 6.0, 0.0]
    rf_mc, t_mc = 0.04, 1.0
    avg_pay = sample_mean(payoffs_mc)
    pv_mc = avg_pay * math.exp(-rf_mc * t_mc)
    d_nodisc = avg_pay
    d_pos_only = sample_mean([p for p in payoffs_mc if p > 0]) * math.exp(-rf_mc * t_mc)
    q_l1(
        "L1-QM-045", "LM 6", "Simulation Methods", "Monte Carlo Option Valuation",
        "Value contingent payoffs using Monte Carlo simulation paths.", True,
        "Six risk-neutral Monte Carlo paths for a 1-year European call option produce terminal payoffs (USD): `0.00, 12.00, 0.00, 18.00, 6.00, 0.00`. With a continuously compounded risk-free rate of 4.0%, the simulated option price is *closest* to:",
        {"A": f"USD {d_nodisc:.2f}", "B": f"USD {pv_mc:.2f}", "C": f"USD {d_pos_only:.2f}"},
        "B",
        rf"The average terminal payoff across all 6 simulated paths is $\bar{{C}}_T = 36/6 = \text{{USD }}{avg_pay:.2f}$. Discounting at $e^{{-0.04(1)}}$ gives $$\hat{{C}}_0 = {avg_pay:.2f} e^{{-0.04}} = \text{{USD }}{pv_mc:.2f}$$",
        {
            "A": rf"Omits risk-free discounting (USD {d_nodisc:.2f}).",
            "C": rf"Averages only the three positive in-the-money payoffs (USD {d_pos_only:.2f}), ignoring zero payoffs.",
        },
    )

    boot_means = [6.1, 7.3, 6.5, 7.7, 6.9]
    se_boot = sample_sd(boot_means)
    d_var_boot = sample_var(boot_means)
    d_se_div_sqrt5 = se_boot / math.sqrt(5)
    q_l1(
        "L1-QM-046", "LM 6", "Simulation Methods", "Bootstrap Standard Error",
        "Calculate standard error via bootstrap resampling.", True,
        "An analyst generates $B = 5$ bootstrap resamples from a return series and obtains resample means (%): `6.1, 7.3, 6.5, 7.7, 6.9`. The bootstrap estimate of the standard error of the sample mean is *closest* to:",
        {"A": f"{d_se_div_sqrt5:.3f}%", "B": f"{d_var_boot:.3f}%", "C": f"{se_boot:.3f}%"},
        "C",
        rf"The bootstrap standard error of an estimator equals the sample standard deviation of the $B$ bootstrap estimates: $$SE_{{\text{{boot}}}} = \sqrt{{\frac{{(-0.8)^2 + 0.4^2 + (-0.4)^2 + 0.8^2 + 0^2}}{{5 - 1}}}} = {se_boot:.3f}\%$$",
        {
            "A": rf"Incorrectly divides the bootstrap standard deviation by $\sqrt{{B}}$ again ({d_se_div_sqrt5:.3f}%).",
            "B": rf"Reports the variance of the bootstrap means ({d_var_boot:.3f}) rather than the standard deviation.",
        },
    )

    q_l1(
        "L1-QM-047", "LM 6", "Simulation Methods", "Bootstrapping vs Monte Carlo",
        "Contrast bootstrapping and Monte Carlo simulation.", False,
        "How does bootstrap resampling primarily differ from parametric Monte Carlo simulation?",
        {
            "A": "Bootstrapping draws samples with replacement directly from observed empirical data rather than from an assumed theoretical probability distribution.",
            "B": "Bootstrapping draws samples without replacement and requires specifying a closed-form correlation matrix.",
            "C": "Monte Carlo simulation preserves empirical fat tails automatically without any parametric distribution assumption.",
        },
        "A",
        "Bootstrapping resamples directly with replacement from the historical sample, avoiding parametric distributional assumptions, whereas Monte Carlo draws random numbers from user-specified parametric distributions and copulas/correlations.",
        {
            "B": "Bootstrapping resamples *with* replacement (resampling without replacement from size $n$ just returns the exact original sample); Monte Carlo specifies parametric parameters.",
            "C": "Monte Carlo only captures fat tails if the analyst explicitly chooses a fat-tailed distribution (e.g., Student's t).",
        },
    )

    q_l1(
        "L1-QM-048", "LM 6", "Simulation Methods", "Monte Carlo Limitations",
        "Identify limitations of Monte Carlo simulation.", False,
        "Which of the following is *least likely* an advantage of Monte Carlo simulation in financial modeling?",
        {
            "A": "Modeling path-dependent cash flows and complex non-linear derivative payoffs.",
            "B": "Generating direct analytical cause-and-effect formulas linking inputs to optimal policy rules.",
            "C": "Stress-testing correlated multi-asset risk exposures across thousands of trials.",
        },
        "B",
        "Monte Carlo is a numerical sampling technique rather than an analytical tool; it estimates distributions of outcomes given assumptions but does not directly provide closed-form analytical cause-and-effect insights.",
        {
            "A": "Path-dependent payoffs (e.g., Asian or barrier options) are a primary use case for Monte Carlo.",
            "C": "Simulating thousands of correlated joint draws is a core strength of Monte Carlo risk models.",
        },
    )

    hist_rets = [-14.2, -11.5, -9.8, -8.4, -7.1, -6.3, -5.0, -4.1, -3.2, -2.5, -1.8, -1.0, -0.4, 0.2, 0.9, 1.5, 2.1, 3.0, 4.4, 6.5]
    # 20 sorted returns: 10th percentile at (20+1)*0.10 = 2.1 -> -11.5 + 0.1*(-9.8 - (-11.5)) = -11.33
    p10_var = hist_rets[1] + 0.1 * (hist_rets[2] - hist_rets[1])
    d_p10_trunc = hist_rets[1]
    d_p5_var = hist_rets[0] + 0.05 * (hist_rets[1] - hist_rets[0])
    q_l1(
        "L1-QM-049", "LM 6", "Simulation Methods", "Historical Simulation Percentile",
        "Estimate downside tail thresholds from historical simulation.", True,
        "An analyst sorts 20 simulated daily returns (%) from worst to best; the five worst outcomes are `-14.2, -11.5, -9.8, -8.4, -7.1`. Using the $(n+1)p$ interpolation rule, the 10% Value at Risk (left-tail 10th percentile) is *closest* to:",
        {"A": f"{d_p10_trunc:.2f}%", "B": f"{p10_var:.2f}%", "C": f"{d_p5_var:.2f}%"},
        "B",
        rf"Position is $L_{{10}} = (20+1) \times 0.10 = 2.1$. Interpolating between the 2nd (-11.5%) and 3rd (-9.8%) worst values gives $$-11.5 + 0.1(-9.8 - (-11.5)) = {p10_var:.2f}\%$$",
        {
            "A": rf"Takes the 2nd worst observation directly ({d_p10_trunc:.2f}%) without interpolation.",
            "C": rf"Uses position $L_5 = 1.05$ ({d_p5_var:.2f}%), matching the 5th percentile rather than the 10th.",
        },
    )

    q_l1(
        "L1-QM-050", "LM 6", "Simulation Methods", "Simulation vs Scenario Analysis",
        "Distinguish sensitivity analysis, scenario analysis, and simulation.", False,
        "How does sensitivity analysis differ from scenario analysis in capital budgeting and risk modeling?",
        {
            "A": "Sensitivity analysis varies one input assumption at a time holding others fixed, whereas scenario analysis alters multiple correlated variables simultaneously.",
            "B": "Sensitivity analysis estimates full probability distributions of NPV, whereas scenario analysis ignores downside cases.",
            "C": "Scenario analysis modifies only the discount rate, whereas sensitivity analysis modifies only revenue growth.",
        },
        "A",
        "Sensitivity analysis tests the *ceteris paribus* impact of changing a single variable at a time, while scenario analysis evaluates coherent multi-factor joint shocks (e.g., stagflation affecting rates, margins, and volumes together).",
        {
            "B": "Monte Carlo simulation generates full probability distributions; scenario analysis evaluates discrete joint outcomes.",
            "C": "Both methods can evaluate any financial driver, not just discount rates or revenue growth.",
        },
    )

    # -----------------------------------------------------------------------
    # LM 7: Estimation and Inference (8 Qs: 051 - 058)
    # -----------------------------------------------------------------------
    mu_clt, sd_clt, n_clt, xbar_clt = 6.0, 12.0, 36, 9.0
    se_clt = sd_clt / math.sqrt(n_clt)
    z_clt = (xbar_clt - mu_clt) / se_clt
    p_clt = 1.0 - norm_cdf(z_clt)
    p_no_sqrt = 1.0 - norm_cdf((xbar_clt - mu_clt) / sd_clt)
    q_l1(
        "L1-QM-051", "LM 7", "Estimation and Inference", "Central Limit Theorem",
        "Apply the Central Limit Theorem to calculate sampling probabilities.", True,
        "Equity excess returns have population mean 6.0% and standard deviation 12.0%. For a random sample of $n = 36$ years, given $N(1.50) = 0.9332$ and $N(0.25) = 0.5987$, the probability that the *sample mean* exceeds 9.0% is *closest* to:",
        {"A": f"{p_clt*100:.2f}%", "B": f"{p_no_sqrt*100:.2f}%", "C": f"{norm_cdf(z_clt)*100:.2f}%"},
        "A",
        rf"By the CLT, standard error is $\sigma / \sqrt{{n}} = 12.0 / \sqrt{{36}} = 2.0\%$. Thus $z = (9.0 - 6.0)/2.0 = 1.50$, and $$P(\bar{{X}} > 9.0\%) = 1 - N(1.50) = 1 - 0.9332 = {p_clt*100:.2f}\%$$",
        {
            "B": rf"Divides by population SD 12.0% instead of standard error 2.0% ($z=0.25 \implies {p_no_sqrt*100:.2f}\%$).",
            "C": rf"Reports $P(\bar{{X}} \le 9.0\%) = N(1.50) = {norm_cdf(z_clt)*100:.2f}\%$ rather than the upper tail.",
        },
    )

    z95, sig_n, err_n = 1.96, 15.0, 3.0
    n_req = math.ceil((z95 * sig_n / err_n) ** 2)
    n_nosq = math.ceil(z95 * sig_n / err_n)
    n_99 = math.ceil((2.576 * sig_n / err_n) ** 2)
    q_l1(
        "L1-QM-052", "LM 7", "Estimation and Inference", "Sample Size Determination",
        "Calculate the minimum sample size required for a target margin of error.", True,
        "An analyst wants to construct a 95% confidence interval ($z = 1.96$) for a population mean with a margin of error no greater than 3.0% when $\\sigma = 15.0\\%$. The minimum required sample size is:",
        {"A": f"{n_nosq}", "B": f"{n_req}", "C": f"{n_99}"},
        "B",
        rf"Solving $E = z_{{\alpha/2}} \sigma / \sqrt{{n}} \le 3.0$: $$n \ge \left(\frac{{1.96 \times 15.0}}{{3.0}}\right)^2 = (9.8)^2 = 96.04 \implies {n_req}$$",
        {
            "A": rf"Fails to square the ratio ({n_nosq}).",
            "C": rf"Uses the 99% critical value $z = 2.576$ ({n_99}) instead of $1.96$.",
        },
    )

    xbar_ci, s_ci, n_ci = 11.4, 8.0, 25
    t_crit_24 = t_crit_two_tailed(0.05, n_ci - 1)  # ~2.0639
    se_ci = s_ci / math.sqrt(n_ci)
    me_ci = t_crit_24 * se_ci
    ci_lo, ci_hi = xbar_ci - me_ci, xbar_ci + me_ci
    me_z_err = 1.96 * se_ci
    me_no_sqrt = t_crit_24 * s_ci
    q_l1(
        "L1-QM-053", "LM 7", "Estimation and Inference", "Student's t Confidence Interval",
        "Construct and interpret confidence intervals using the t-distribution.", True,
        f"A sample of $n = 25$ hedge funds yields a mean return of 11.40% and sample standard deviation of 8.00%. Using the two-tailed 5% critical value $t_{{0.025, 24}} = {t_crit_24:.3f}$, the upper bound of the 95% confidence interval is *closest* to:",
        {"A": f"{xbar_ci + me_z_err:.2f}%", "B": f"{xbar_ci + me_no_sqrt:.2f}%", "C": f"{ci_hi:.2f}%"},
        "C",
        rf"Standard error is $s / \sqrt{{n}} = 8.00 / 5 = 1.60\%$. The 95% confidence interval is $$11.40\% \pm {t_crit_24:.3f}(1.60\%) = [{ci_lo:.2f}\%,\, {ci_hi:.2f}\%]$$",
        {
            "A": rf"Uses $z_{{0.025}} = 1.96$ instead of the finite-sample Student's t critical value ({xbar_ci + me_z_err:.2f}%).",
            "B": rf"Multiplies $t$-critical by sample SD directly instead of standard error ({xbar_ci + me_no_sqrt:.2f}%).",
        },
    )

    N_pop, n_sub, s_sub = 100, 36, 12.0
    se_unadj = s_sub / math.sqrt(n_sub)
    fpc = math.sqrt((N_pop - n_sub) / (N_pop - 1))
    se_fpc = se_unadj * fpc
    d_noadj = se_unadj
    d_wrong_fpc = se_unadj * math.sqrt(n_sub / N_pop)
    q_l1(
        "L1-QM-054", "LM 7", "Estimation and Inference", "Finite Population Correction",
        "Apply finite population correction when sampling without replacement.", True,
        "From a finite universe of $N = 100$ municipal bonds, an analyst draws a simple random sample of $n = 36$ bonds without replacement and measures a sample standard deviation of 12.0%. Using the finite population correction, the standard error of the sample mean is *closest* to:",
        {"A": f"{se_fpc:.2f}%", "B": f"{d_noadj:.2f}%", "C": f"{d_wrong_fpc:.2f}%"},
        "A",
        rf"Unadjusted $SE = 12 / \sqrt{{36}} = 2.00\%$. With $n/N = 36\% > 5\%$, apply finite population correction: $$SE_{{\text{{FPC}}}} = 2.00\% \times \sqrt{{\frac{{100 - 36}}{{100 - 1}}}} = {se_fpc:.2f}\%$$",
        {
            "B": rf"Omits the finite population correction factor ({d_noadj:.2f}%).",
            "C": rf"Multiplies by $\sqrt{{n/N}}$ instead of $\sqrt{{(N-n)/(N-1)}}$ ({d_wrong_fpc:.2f}%).",
        },
    )

    q_l1(
        "L1-QM-055", "LM 7", "Estimation and Inference", "Sampling Methods",
        "Compare simple random, stratified, cluster, and non-probability sampling.", False,
        "When constructing a bond index tracker across investment-grade sectors, an analyst partitions the bond universe by credit rating and maturity bucket, then draws random samples proportional to each bucket's market weight. This approach is *best* described as:",
        {
            "A": "Two-stage cluster sampling",
            "B": "Stratified random sampling",
            "C": "Judgmental sampling",
        },
        "B",
        "Stratified random sampling divides the population into homogeneous strata (credit/maturity buckets) and draws random samples within every stratum proportionally, reducing sampling error.",
        {
            "A": "Cluster sampling selects entire heterogeneous groups (clusters) at random and leaves other clusters completely unsampled.",
            "C": "Judgmental sampling is non-probability sampling based on analyst discretion rather than random draws within strata.",
        },
    )

    q_l1(
        "L1-QM-056", "LM 7", "Estimation and Inference", "Properties of Estimators",
        "Identify unbiasedness, efficiency, and consistency of estimators.", False,
        "An estimator $\\hat{\\theta}_n$ is said to be *consistent* if, as the sample size $n$ increases without bound:",
        {
            "A": "Its expected value equals $\\theta$ for every finite sample size $n$.",
            "B": "It achieves the smallest variance among all unbiased estimators at fixed $n$.",
            "C": "The probability that $\\hat{\\theta}_n$ differs from $\\theta$ by any positive amount approaches zero.",
        },
        "C",
        "Consistency means $\\hat{\\theta}_n$ converges in probability to the true parameter $\\theta$ as $n \\to \\infty$ (its sampling error and variance shrink toward zero).",
        {
            "A": "Describes *unbiasedness* ($E(\\hat{\\theta}) = \\theta$), not consistency.",
            "B": "Describes *efficiency* (minimum variance among unbiased estimators), not consistency.",
        },
    )

    q_l1(
        "L1-QM-057", "LM 7", "Estimation and Inference", "Data-Snooping & Selection Biases",
        "Identify survivorship, look-ahead, time-period, and data-snooping biases.", False,
        "A backtest of a value-momentum strategy uses year-end balance sheet book value reported in March of the following year to form portfolios on December 31 of the fiscal year-end. This backtest suffers *most directly* from:",
        {
            "A": "Look-ahead bias",
            "B": "Survivorship bias",
            "C": "Time-period bias",
        },
        "A",
        "Look-ahead bias arises when a backtest uses information (such as audited March accounting filings) that was not yet publicly known at the December 31 trading decision date.",
        {
            "B": "Survivorship bias occurs when delisted or failed firms are excluded from the historical database.",
            "C": "Time-period bias occurs when the sample window is too short or coincides with an atypical market regime.",
        },
    )

    q_l1(
        "L1-QM-058", "LM 7", "Estimation and Inference", "Confidence Interval Scaling",
        "Evaluate how sample size changes affect confidence interval width.", True,
        "Holding confidence level and population standard deviation constant, to cut the width of a $z$-based confidence interval by two-thirds (to one-third of its original width), the sample size must be multiplied by a factor of:",
        {"A": "3", "B": "9", "C": "6"},
        "B",
        rf"Margin of error scales inversely with $\sqrt{{n}}$: $E \propto n^{{-1/2}}$. Reducing width to $1/3$ requires $\sqrt{{n_{{\text{{new}}}} / n_{{\text{{old}}}}}} = 3$, so $n$ must increase by $3^2 = 9\times$.",
        {
            "A": "Fails to square the scaling factor (cutting width by 3 requires $3^2 = 9\times$ sample size).",
            "C": "Incorrectly doubles 3 instead of squaring 3.",
        },
    )

    # -----------------------------------------------------------------------
    # LM 8: Hypothesis Testing (9 Qs: 059 - 067)
    # -----------------------------------------------------------------------
    xbar_h, mu_h, s_h, n_h = 10.2, 8.0, 5.5, 25
    t_h = (xbar_h - mu_h) / (s_h / math.sqrt(n_h))
    t_h_crit = t_crit_two_tailed(0.05, n_h - 1)  # 2.064
    t_h_wrong = (xbar_h - mu_h) / s_h
    q_l1(
        "L1-QM-059", "LM 8", "Hypothesis Testing", "One-Sample t-Test",
        "Conduct and interpret a hypothesis test for a single population mean.", True,
        f"A fund averages a 10.20% return over $n = 25$ years with sample standard deviation 5.50%. Testing $H_0: \\mu = 8.00\\%$ vs. $H_a: \\mu \\neq 8.00\\%$ at $\\alpha = 5\\%$ ($t_{{0.025, 24}} = {t_h_crit:.3f}$), the test statistic and decision are:",
        {
            "A": f"t = {t_h:.2f}; reject H0",
            "B": f"t = {t_h:.2f}; fail to reject H0",
            "C": f"t = {t_h_wrong:.2f}; fail to reject H0",
        },
        "B",
        rf"Standard error is $5.50 / \sqrt{{25}} = 1.10\%$. Test statistic is $$t = \frac{{10.20 - 8.00}}{{1.10}} = {t_h:.2f}$$ Since $|{t_h:.2f}| < {t_h_crit:.3f}$, we fail to reject $H_0$.",
        {
            "A": rf"Computes the right test statistic ($t = {t_h:.2f}$), but compares against $1.96$ or a one-tailed cutoff rather than $t_{{0.025,24}} = {t_h_crit:.3f}$.",
            "C": rf"Divides by sample SD instead of standard error ($t = {t_h_wrong:.2f}$).",
        },
    )

    # Two-sample pooled t-test
    x1_2, s1_2, n1_2 = 12.0, 4.0, 12
    x2_2, s2_2, n2_2 = 8.0, 6.0, 10
    sp2 = ((n1_2 - 1) * (s1_2 ** 2) + (n2_2 - 1) * (s2_2 ** 2)) / (n1_2 + n2_2 - 2)
    se_diff = math.sqrt(sp2 * (1.0 / n1_2 + 1.0 / n2_2))
    t_2s = (x1_2 - x2_2) / se_diff
    t_unpooled = (x1_2 - x2_2) / math.sqrt((s1_2 ** 2) / n1_2 + (s2_2 ** 2) / n2_2)
    d_sp = math.sqrt(sp2)
    q_l1(
        "L1-QM-060", "LM 8", "Hypothesis Testing", "Difference Between Means (Pooled)",
        "Test the equality of two population means assuming equal variances.", True,
        "Sample 1 ($n_1 = 12$) has mean 12.0% and SD 4.0%; independent Sample 2 ($n_2 = 10$) has mean 8.0% and SD 6.0%. Assuming equal population variances, the pooled $t$-statistic for testing $H_0: \\mu_1 - \\mu_2 = 0$ is *closest* to:",
        {"A": f"{t_2s:.2f}", "B": f"{t_unpooled:.2f}", "C": f"{d_sp:.2f}"},
        "A",
        rf"Pooled variance is $$s_p^2 = \frac{{11(16) + 9(36)}}{{20}} = {sp2:.2f}$$ Standard error is $\sqrt{{{sp2:.2f}(1/12 + 1/10)}} = {se_diff:.4f}$, giving $t = (12.0 - 8.0)/{se_diff:.4f} = {t_2s:.2f}$.",
        {
            "B": rf"Uses unpooled standard error ({t_unpooled:.2f}), ignoring the equal-variance assumption.",
            "C": rf"Reports the pooled standard deviation ({d_sp:.2f}) instead of the test statistic.",
        },
    )

    diffs_p = [2.4, 1.6, 3.0, 0.8, 2.2]
    dbar = sample_mean(diffs_p)
    sd_d = sample_sd(diffs_p)
    t_pair = dbar / (sd_d / math.sqrt(len(diffs_p)))
    t_pair_nosqrt = dbar / sd_d
    q_l1(
        "L1-QM-061", "LM 8", "Hypothesis Testing", "Paired Comparisons t-Test",
        "Conduct a paired comparisons test on dependent samples.", True,
        "Over 5 quarters, a manager outperforms her benchmark by active returns (%) of `2.4, 1.6, 3.0, 0.8, 2.2`. The paired comparisons $t$-statistic for testing $H_0: \\mu_d \\le 0$ is *closest* to:",
        {"A": f"{dbar:.2f}", "B": f"{t_pair_nosqrt:.2f}", "C": f"{t_pair:.2f}"},
        "C",
        rf"Mean active return is $\bar{{d}} = {dbar:.2f}\%$ and sample SD of differences is $s_d = {sd_d:.4f}\%$. Test statistic is $$t = \frac{{\bar{{d}}}}{{s_d/\sqrt{{n}}}} = \frac{{{dbar:.2f}}}{{{sd_d:.4f}/\sqrt{{5}}}} = {t_pair:.2f}$$",
        {
            "A": rf"Reports mean active return ({dbar:.2f}%) instead of the standardized t-statistic.",
            "B": rf"Divides $\bar{{d}}$ by $s_d$ without dividing by $\sqrt{{5}}$ ({t_pair_nosqrt:.2f}).",
        },
    )

    n_chi, s_chi, sig0_chi = 21, 16.0, 12.0
    chi_stat = (n_chi - 1) * (s_chi ** 2) / (sig0_chi ** 2)
    chi_crit_hi = chi2_crit_upper(0.025, n_chi - 1)  # ~34.17
    d_n_chi = n_chi * (s_chi ** 2) / (sig0_chi ** 2)
    d_sd_ratio = (n_chi - 1) * s_chi / sig0_chi
    q_l1(
        "L1-QM-062", "LM 8", "Hypothesis Testing", "Chi-Square Variance Test",
        "Conduct a chi-square test of a single population variance.", True,
        f"A bond fund targets a maximum annualized return standard deviation of 12.0%. Over $n = 21$ years, sample standard deviation is 16.0%. Testing $H_0: \\sigma^2 = 144$ vs. $H_a: \\sigma^2 \\neq 144$ at $\\alpha = 5\\%$ (upper critical $\\chi^2_{{0.025, 20}} = {chi_crit_hi:.2f}$), the $\\chi^2$ statistic is *closest* to:",
        {"A": f"{chi_stat:.2f}", "B": f"{d_n_chi:.2f}", "C": f"{d_sd_ratio:.2f}"},
        "A",
        rf"The chi-square test statistic is $$\chi^2 = \frac{{(n-1)s^2}}{{\sigma_0^2}} = \frac{{20 \times 16^2}}{{12^2}} = {chi_stat:.2f}$$ Since ${chi_stat:.2f} > {chi_crit_hi:.2f}$, we reject $H_0$.",
        {
            "B": rf"Uses $n=21$ instead of $df = n-1 = 20$ ({d_n_chi:.2f}).",
            "C": rf"Uses the ratio of standard deviations rather than variances ({d_sd_ratio:.2f}).",
        },
    )

    s1_f, n1_f = 18.0, 16
    s2_f, n2_f = 12.0, 21
    f_stat_var = (s1_f ** 2) / (s2_f ** 2)
    f_crit_var = f_crit_upper(0.025, n1_f - 1, n2_f - 1)
    d_f_inv = (s2_f ** 2) / (s1_f ** 2)
    d_sd_f = s1_f / s2_f
    q_l1(
        "L1-QM-063", "LM 8", "Hypothesis Testing", "F-Test of Equality of Variances",
        "Conduct an F-test for equality of two variances.", True,
        f"Strategy A ($n_1 = 16$) exhibits a sample standard deviation of 18.0%, while Strategy B ($n_2 = 21$) exhibits a sample standard deviation of 12.0%. Testing $H_0: \\sigma_A^2 = \\sigma_B^2$ at $\\alpha = 5\\%$ ($F_{{0.025, 15, 20}} = {f_crit_var:.2f}$), the $F$-statistic is *closest* to:",
        {"A": f"{d_sd_f:.2f}", "B": f"{f_stat_var:.2f}", "C": f"{d_f_inv:.2f}"},
        "B",
        rf"Placing the larger variance in the numerator yields $$F = \frac{{s_A^2}}{{s_B^2}} = \frac{{18^2}}{{12^2}} = {f_stat_var:.2f}$$ Because ${f_stat_var:.2f} < {f_crit_var:.2f}$, we fail to reject $H_0$.",
        {
            "A": rf"Reports the ratio of standard deviations ($18/12 = {d_sd_f:.2f}$) instead of variances.",
            "C": rf"Places the smaller variance in the numerator ({d_f_inv:.2f}), violating standard upper-tail F-table convention.",
        },
    )

    z_pv = -2.17
    p_1t = norm_cdf(z_pv)
    p_2t = 2.0 * p_1t
    q_l1(
        "L1-QM-064", "LM 8", "Hypothesis Testing", "p-Value Interpretation",
        "Compute and interpret p-values in hypothesis testing.", True,
        f"For a two-tailed $z$-test, the test statistic is $z = -2.17$. Given $N(-2.17) = {p_1t:.4f}$, what is the two-tailed $p$-value and decision at $\\alpha = 5\\%$ vs. $\\alpha = 1\\%$?",
        {
            "A": f"p = {p_1t:.4f}; reject at 5%, fail to reject at 1%",
            "B": f"p = {p_2t:.4f}; reject at both 5% and 1%",
            "C": f"p = {p_2t:.4f}; reject at 5%, fail to reject at 1%",
        },
        "C",
        rf"For a two-tailed test, $p\text{{-value}} = 2 \times P(Z \le -2.17) = 2({p_1t:.4f}) = {p_2t:.4f}$. Because $0.01 < {p_2t:.4f} < 0.05$, we reject $H_0$ at $\alpha = 5\%$ but fail to reject at $\alpha = 1\%$.",
        {
            "A": rf"Reports the one-tailed p-value ({p_1t:.4f}) instead of doubling for a two-tailed alternative.",
            "B": rf"Incorrectly rejects at 1% even though {p_2t:.4f} > 0.0100.",
        },
    )

    q_l1(
        "L1-QM-065", "LM 8", "Hypothesis Testing", "Type I/II Errors & Power",
        "Explain Type I error, Type II error, and the power of a test.", False,
        "Holding sample size fixed, lowering the significance level $\\alpha$ from 5% to 1% will *most likely*:",
        {
            "A": "Reduce Type I error probability, increase Type II error probability, and reduce test power.",
            "B": "Reduce both Type I error and Type II error probabilities while increasing test power.",
            "C": "Increase Type I error probability while reducing Type II error probability.",
        },
        "A",
        "Type I error probability equals $\\alpha$. Tightening $\\alpha$ from 5% to 1% makes rejecting $H_0$ harder, reducing Type I error at the cost of higher Type II error ($\\beta$) and lower power ($1 - \\beta$).",
        {
            "B": "At fixed $n$, Type I and Type II errors trade off inversely; both can only fall simultaneously by increasing sample size.",
            "C": "Lowering $\\alpha$ reduces, not increases, Type I error probability.",
        },
    )

    q_l1(
        "L1-QM-066", "LM 8", "Hypothesis Testing", "Statistical vs Economic Significance",
        "Distinguish statistical significance from economic significance.", False,
        "A high-frequency arbitrage strategy tested over 500,000 trades generates an average gross profit of 0.4 bps per trade with a $t$-statistic of 4.80 ($p < 0.0001$). After estimated market impact and commissions of 1.2 bps per trade, the strategy is *best* characterized as:",
        {
            "A": "Economically significant but statistically insignificant.",
            "B": "Statistically significant but economically unprofitable.",
            "C": "Suffering from insufficient sample size.",
        },
        "B",
        "Large sample sizes ($n=500,000$) shrink standard errors so even tiny gross alphas appear statistically significant ($t=4.80$), yet net returns ($0.4 - 1.2 = -0.8$ bps) are economically unviable.",
        {
            "A": "The high $t$-stat confirms statistical significance, whereas negative net return rules out economic significance.",
            "C": "The sample size of 500,000 is massive, which is why tiny effects achieve high $t$-stats.",
        },
    )

    q_l1(
        "L1-QM-067", "LM 8", "Hypothesis Testing", "Interpreting the p-Value",
        "Correctly interpret the meaning of a p-value.", False,
        "A regression yields a $p$-value of 0.032 for an alpha coefficient. Which interpretation is *most likely* correct?",
        {
            "A": "There is a 3.2% probability that the null hypothesis ($\\alpha = 0$) is true.",
            "B": "There is a 96.8% probability that the manager possesses genuine investment skill.",
            "C": "Assuming the null hypothesis ($\\alpha = 0$) is true, there is a 3.2% probability of observing a test statistic at least as extreme as the one obtained.",
        },
        "C",
        "By definition, the $p$-value is the conditional probability $P(\\text{data as extreme} \\mid H_0 \\text{ is true})$ — it is the smallest significance level at which $H_0$ can be rejected, not the posterior probability of $H_0$.",
        {
            "A": "Frequentist $p$-values condition on $H_0$ being true; they never give $P(H_0 \\mid \\text{data})$.",
            "B": "Commit the inverse probability fallacy by equating $1 - p$ to the probability that $H_a$ is true.",
        },
    )

    # -----------------------------------------------------------------------
    # LM 9: Parametric and Non-Parametric Tests of Independence (7 Qs: 068 - 074)
    # -----------------------------------------------------------------------
    r_p, n_rp = 0.42, 27
    t_r = r_p * math.sqrt(n_rp - 2) / math.sqrt(1.0 - r_p ** 2)
    t_r_crit = t_crit_two_tailed(0.05, n_rp - 2)
    t_r_n27 = r_p * math.sqrt(n_rp) / math.sqrt(1.0 - r_p ** 2)
    t_r_nodenom = r_p * math.sqrt(n_rp - 2)
    q_l1(
        "L1-QM-068", "LM 9", "Parametric and Non-Parametric Tests of Independence", "Parametric Correlation Test",
        "Conduct a parametric t-test of correlation.", True,
        f"Across $n = 27$ months, the sample Pearson correlation between two factor indices is $r = 0.42$. Testing $H_0: \\rho = 0$ vs. $H_a: \\rho \\neq 0$ at $\\alpha = 5\\%$ ($t_{{0.025, 25}} = {t_r_crit:.3f}$), the test statistic is *closest* to:",
        {"A": f"{t_r:.2f}", "B": f"{t_r_n27:.2f}", "C": f"{t_r_nodenom:.2f}"},
        "A",
        rf"Using $df = n - 2 = 25$: $$t = \frac{{r\sqrt{{n-2}}}}{{\sqrt{{1-r^2}}}} = \frac{{0.42\sqrt{{25}}}}{{\sqrt{{1-0.42^2}}}} = {t_r:.2f}$$ Since ${t_r:.2f} > {t_r_crit:.3f}$, $H_0$ is rejected.",
        {
            "B": rf"Uses $\sqrt{{n}} = \sqrt{{27}}$ instead of $\sqrt{{n-2}} = 5$ ({t_r_n27:.2f}).",
            "C": rf"Omits $\sqrt{{1 - r^2}}$ in the denominator ({t_r_nodenom:.2f}).",
        },
    )

    # Spearman rank correlation: 5 managers ranked on Yr1 vs Yr2
    # Ranks X: [1, 2, 3, 4, 5], Ranks Y: [2, 1, 4, 3, 5] -> d^2 = [1, 1, 1, 1, 0] -> sum=4
    n_sp, sum_d2 = 5, 4
    rs = 1.0 - (6.0 * sum_d2) / (n_sp * (n_sp ** 2 - 1))
    rs_wrong_denom = 1.0 - (6.0 * sum_d2) / (n_sp ** 2 - 1)
    rs_no6 = 1.0 - sum_d2 / (n_sp * (n_sp ** 2 - 1))
    q_l1(
        "L1-QM-069", "LM 9", "Parametric and Non-Parametric Tests of Independence", "Spearman Rank Correlation",
        "Calculate the Spearman rank correlation coefficient.", True,
        "Five mutual funds are ranked on Year 1 and Year 2 performance as pairs $(1,2), (2,1), (3,4), (4,3), (5,5)$, with no ties. The Spearman rank correlation coefficient $r_S$ is *closest* to:",
        {"A": f"{rs_wrong_denom:.2f}", "B": f"{rs:.2f}", "C": f"{rs_no6:.2f}"},
        "B",
        rf"Rank differences $d_i = X_i - Y_i$ are $(-1, +1, -1, +1, 0)$, so $\sum d_i^2 = 4$. With $n=5$: $$r_S = 1 - \frac{{6\sum d_i^2}}{{n(n^2-1)}} = 1 - \frac{{6(4)}}{{5(24)}} = {rs:.2f}$$",
        {
            "A": rf"Omits $n$ in the denominator ({rs_wrong_denom:.2f}).",
            "C": rf"Omits the factor of 6 in the numerator ({rs_no6:.2f}).",
        },
    )

    rs_val, n_rs_t = 0.55, 18
    t_rs = rs_val * math.sqrt(n_rs_t - 2) / math.sqrt(1.0 - rs_val ** 2)
    t_rs_n2 = rs_val * math.sqrt(n_rs_t) / math.sqrt(1.0 - rs_val ** 2)
    t_rs_nod = rs_val * math.sqrt(n_rs_t - 2)
    q_l1(
        "L1-QM-070", "LM 9", "Parametric and Non-Parametric Tests of Independence", "Testing Spearman Rank Correlation",
        "Test the significance of Spearman rank correlation for moderate or large samples.", True,
        "Across $n = 18$ analyst pairs, the Spearman rank correlation between forecast accuracy and experience is $r_S = 0.55$. Using the $t$-approximation with $n - 2 = 16$ degrees of freedom, the test statistic is *closest* to:",
        {"A": f"{t_rs_nod:.2f}", "B": f"{t_rs_n2:.2f}", "C": f"{t_rs:.2f}"},
        "C",
        rf"For $n \ge 10$, the test statistic follows $t = r_S \sqrt{{\frac{{n-2}}{{1-r_S^2}}}} = 0.55 \sqrt{{\frac{{16}}{{1 - 0.55^2}}}} = {t_rs:.2f}$.",
        {
            "A": rf"Omits $\sqrt{{1 - r_S^2}}$ in the denominator ({t_rs_nod:.2f}).",
            "B": rf"Uses $n=18$ instead of $n-2=16$ inside the square root ({t_rs_n2:.2f}).",
        },
    )

    # 2x2 Contingency table Chi-square
    # Observed: [[30, 10], [20, 40]] -> row totals 40, 60; col totals 50, 50; N=100
    obs = [[30, 10], [20, 40]]
    row_tot = [sum(r) for r in obs]
    col_tot = [obs[0][j] + obs[1][j] for j in range(2)]
    tot_n = sum(row_tot)
    exp_tbl = [[row_tot[i] * col_tot[j] / tot_n for j in range(2)] for i in range(2)]
    chi_ind = sum(((obs[i][j] - exp_tbl[i][j]) ** 2) / exp_tbl[i][j] for i in range(2) for j in range(2))
    d_wrong_denom_ind = sum(((obs[i][j] - exp_tbl[i][j]) ** 2) / obs[i][j] for i in range(2) for j in range(2))
    d_no_sq_ind = sum(abs(obs[i][j] - exp_tbl[i][j]) / exp_tbl[i][j] for i in range(2) for j in range(2))
    q_l1(
        "L1-QM-071", "LM 9", "Parametric and Non-Parametric Tests of Independence", "Chi-Square Test of Independence",
        "Conduct a chi-square test of independence using contingency tables.", True,
        "A contingency table classifies 100 funds by style and outperformance: Growth Beat = 30, Growth Miss = 10; Value Beat = 20, Value Miss = 40. The $\\chi^2$ test statistic for independence is *closest* to:",
        {"A": f"{chi_ind:.2f}", "B": f"{d_wrong_denom_ind:.2f}", "C": f"{d_no_sq_ind:.2f}"},
        "A",
        rf"Row totals are 40 and 60; column totals are 50 and 50. Expected counts $E_{{ij}} = (\text{{Row}}_i \times \text{{Col}}_j)/100$ are 20, 20, 30, 30. Thus $$\chi^2 = \frac{{(30-20)^2}}{{20}} + \frac{{(10-20)^2}}{{20}} + \frac{{(20-30)^2}}{{30}} + \frac{{(40-30)^2}}{{30}} = {chi_ind:.2f}$$",
        {
            "B": rf"Divides squared deviations by observed counts $O_{{ij}}$ rather than expected counts $E_{{ij}}$ ({d_wrong_denom_ind:.2f}).",
            "C": rf"Fails to square $(O_{{ij}} - E_{{ij}})$ ({d_no_sq_ind:.2f}).",
        },
    )

    df_3x4 = (3 - 1) * (4 - 1)
    q_l1(
        "L1-QM-072", "LM 9", "Parametric and Non-Parametric Tests of Independence", "Contingency Table Degrees of Freedom",
        "Determine degrees of freedom for a contingency table test.", True,
        "In a chi-square test of independence examining whether credit rating category (3 tiers) is independent of geographic region (4 regions) across 240 corporate issuers, the appropriate degrees of freedom is:",
        {"A": "12", "B": "6", "C": "11"},
        "B",
        "Degrees of freedom for an $r \\times c$ contingency table test of independence equal $(r - 1)(c - 1) = (3 - 1)(4 - 1) = 6$.",
        {
            "A": "Reports total cells $r \\times c = 12$ without subtracting 1 from rows and columns.",
            "C": "Reports $rc - 1 = 11$ instead of $(r-1)(c-1) = 6$.",
        },
    )

    q_l1(
        "L1-QM-073", "LM 9", "Parametric and Non-Parametric Tests of Independence", "Parametric vs Non-Parametric Tests",
        "Identify situations requiring non-parametric tests.", False,
        "An analyst tests the relationship between corporate ESG ratings (ordinal rankings 1 to 10) and future credit spreads across 14 issuers, where two spreads are extreme outliers. Which test is *most appropriate*?",
        {
            "A": "Spearman rank correlation",
            "B": "Pearson product-moment correlation",
            "C": "Paired comparisons z-test",
        },
        "A",
        "Non-parametric tests like Spearman rank correlation do not assume normality, are robust to extreme outliers, and are specifically designed for ordinal/ranked data in small samples.",
        {
            "B": "Pearson correlation measures linear association of interval/ratio variables and is heavily distorted by outliers.",
            "C": "A z-test requires large-sample normality and interval data rather than ordinal ranks.",
        },
    )

    q_l1(
        "L1-QM-074", "LM 9", "Parametric and Non-Parametric Tests of Independence", "Limitations of Correlation",
        "Identify limitations of correlation analysis.", False,
        "If variables $X$ and $Y$ satisfy the exact quadratic relation $Y = X^2$ over a symmetric interval $X \\in [-2, +2]$, their sample Pearson correlation is *closest* to:",
        {
            "A": "+1.00 because $Y$ is a deterministic function of $X$.",
            "B": "0.00 because Pearson correlation only captures linear association.",
            "C": "-1.00 for negative values of $X$ and +1.00 overall.",
        },
        "B",
        "Pearson correlation measures strictly *linear* association. Because $Y = X^2$ is symmetric around $X = 0$, positive and negative cross-products cancel, yielding zero linear correlation despite a strong non-linear dependence.",
        {
            "A": "Deterministic non-linear relationships can have zero Pearson correlation.",
            "C": "A single sample correlation coefficient takes one value over the whole sample, near 0 here.",
        },
    )

    # -----------------------------------------------------------------------
    # LM 10: Simple Linear Regression (9 Qs: 075 - 083)
    # -----------------------------------------------------------------------
    xs_slr = [1.0, 2.0, 3.0, 4.0, 5.0]
    ys_slr = [4.0, 7.0, 8.0, 11.0, 15.0]
    res_slr = ols_simple(xs_slr, ys_slr)
    b1_s, b0_s = res_slr["b1"], res_slr["b0"]
    d_inv_slope = res_slr["sxy"] / res_slr["syy"]
    d_b0_err = res_slr["my"] + b1_s * res_slr["mx"]
    q_l1(
        "L1-QM-075", "LM 10", "Simple Linear Regression", "OLS Slope and Intercept",
        "Estimate slope and intercept coefficients in simple linear regression.", True,
        "Over 5 periods, independent variable $X$ takes values `1, 2, 3, 4, 5` and dependent variable $Y$ takes values `4, 7, 8, 11, 15`. The estimated OLS slope ($\\hat{b}_1$) and intercept ($\\hat{b}_0$) are *closest* to:",
        {
            "A": f"b1 = {d_inv_slope:.2f}, b0 = {res_slr['my'] - d_inv_slope*res_slr['mx']:.2f}",
            "B": f"b1 = {b1_s:.2f}, b0 = {d_b0_err:.2f}",
            "C": f"b1 = {b1_s:.2f}, b0 = {b0_s:.2f}",
        },
        "C",
        rf"Means are $\bar{{X}} = 3$, $\bar{{Y}} = 9$. $\sum(X_i-\bar{{X}})^2 = 10$ and $\sum(X_i-\bar{{X}})(Y_i-\bar{{Y}}) = 26$, so $\hat{{b}}_1 = 26/10 = {b1_s:.2f}$ and $\hat{{b}}_0 = 9 - {b1_s:.2f}(3) = {b0_s:.2f}$.",
        {
            "A": rf"Divides covariance by $\text{{Var}}(Y)$ instead of $\text{{Var}}(X)$ ($\hat{{b}}_1 = {d_inv_slope:.2f}$).",
            "B": rf"Adds $\hat{{b}}_1 \bar{{X}}$ to $\bar{{Y}}$ instead of subtracting ({d_b0_err:.2f}).",
        },
    )

    n_a1, ssr_a1, sse_a1 = 26, 180.0, 60.0
    sst_a1 = ssr_a1 + sse_a1
    r2_a1 = ssr_a1 / sst_a1
    see_a1 = math.sqrt(sse_a1 / (n_a1 - 2))
    see_n_err = math.sqrt(sse_a1 / n_a1)
    q_l1(
        "L1-QM-076", "LM 10", "Simple Linear Regression", "R-Squared & SEE",
        "Calculate and interpret R-squared and the standard error of estimate (SEE).", True,
        "A simple linear regression over $n = 26$ observations yields regression sum of squares $\\text{RSS} = 180.0$ and residual sum of squares $\\text{SSE} = 60.0$. The $R^2$ and standard error of estimate (SEE) are *closest* to:",
        {
            "A": f"R2 = {r2_a1*100:.1f}%, SEE = {see_a1:.3f}",
            "B": f"R2 = {r2_a1*100:.1f}%, SEE = {see_n_err:.3f}",
            "C": f"R2 = {(sse_a1/sst_a1)*100:.1f}%, SEE = {see_a1:.3f}",
        },
        "A",
        rf"Total sum of squares is $\text{{SST}} = 180 + 60 = 240$, so $R^2 = 180/240 = {r2_a1*100:.1f}\%$. With $df = n - 2 = 24$, $$\text{{SEE}} = \sqrt{{\frac{{60.0}}{{24}}}} = \sqrt{{2.50}} = {see_a1:.3f}$$",
        {
            "B": rf"Divides SSE by $n=26$ instead of $n-2=24$ (SEE = {see_n_err:.3f}).",
            "C": rf"Reports $\text{{SSE}}/\text{{SST}} = 1 - R^2 = {(sse_a1/sst_a1)*100:.1f}\%$ instead of $R^2$.",
        },
    )

    f_a1 = (ssr_a1 / 1.0) / (sse_a1 / (n_a1 - 2))
    t_equiv = math.sqrt(f_a1)
    f_err_df = (ssr_a1 / 2.0) / (sse_a1 / (n_a1 - 2))
    q_l1(
        "L1-QM-077", "LM 10", "Simple Linear Regression", "ANOVA F-Test",
        "Calculate and interpret the ANOVA F-statistic in simple linear regression.", True,
        "Using the same simple linear regression ($n = 26$, $\\text{RSS} = 180.0$, $\\text{SSE} = 60.0$), the ANOVA $F$-statistic and corresponding absolute $t$-statistic on the slope are *closest* to:",
        {
            "A": f"F = {f_err_df:.2f}, |t| = {math.sqrt(f_err_df):.2f}",
            "B": f"F = {f_a1:.2f}, |t| = {t_equiv:.2f}",
            "C": f"F = {f_a1:.2f}, |t| = {f_a1:.2f}",
        },
        "B",
        rf"Mean square regression is $\text{{MSR}} = 180/1 = 180$ and mean square error is $\text{{MSE}} = 60/24 = 2.50$. Thus $F = 180/2.50 = {f_a1:.2f}$. In simple linear regression, $F = t^2$, so $|t| = \sqrt{{{f_a1:.2f}}} = {t_equiv:.2f}$.",
        {
            "A": rf"Divides RSS by $2$ instead of $k=1$ (F = {f_err_df:.2f}).",
            "C": rf"Equates $|t| = F$ instead of $|t| = \sqrt{{F}}$.",
        },
    )

    b1_capm, se_capm, b0_hyp = 1.24, 0.10, 1.00
    t_capm = (b1_capm - b0_hyp) / se_capm
    t_zero = b1_capm / se_capm
    q_l1(
        "L1-QM-078", "LM 10", "Simple Linear Regression", "Slope Hypothesis Test",
        "Test hypotheses about the regression slope coefficient.", True,
        "A market-model regression over 60 months estimates a stock's beta as $\\hat{\\beta} = 1.24$ with a standard error of $0.10$. The $t$-statistic to test whether the stock's true beta differs from $1.00$ ($H_0: \\beta = 1.00$) is *closest* to:",
        {"A": f"{t_zero:.2f}", "B": f"{t_capm:.2f}", "C": f"{(b1_capm - b0_hyp):.2f}"},
        "B",
        rf"Testing against hypothesized $\beta_0 = 1.00$ gives $$t = \frac{{\hat{{\beta}} - \beta_0}}{{SE(\hat{{\beta}})}} = \frac{{1.24 - 1.00}}{{0.10}} = {t_capm:.2f}$$",
        {
            "A": rf"Tests against $\beta_0 = 0$ ($t = {t_zero:.2f}$) instead of $\beta_0 = 1.00$.",
            "C": rf"Fails to divide by the standard error $0.10$ ({b1_capm - b0_hyp:.2f}).",
        },
    )

    # Prediction interval
    n_p, see_p, xbar_p, sx_p, xf_p = 32, 2.0, 5.0, 4.0, 11.0
    b0_p, b1_p = 1.5, 0.80
    yhat_p = b0_p + b1_p * xf_p
    sf_p = see_p * math.sqrt(1.0 + 1.0 / n_p + ((xf_p - xbar_p) ** 2) / ((n_p - 1) * (sx_p ** 2)))
    t_p_crit = t_crit_two_tailed(0.05, n_p - 2)
    hi_p = yhat_p + t_p_crit * sf_p
    hi_see_only = yhat_p + t_p_crit * see_p
    lo_p = yhat_p - t_p_crit * sf_p
    q_l1(
        "L1-QM-079", "LM 10", "Simple Linear Regression", "Prediction Interval",
        "Calculate point forecasts and prediction intervals.", True,
        f"In a simple regression ($n = 32$, $\\bar{{X}} = 5.0$, $s_X = 4.0$, $\\text{{SEE}} = 2.0$), $\\hat{{Y}} = 1.5 + 0.8X$. For $X_f = 11.0$, using $t_{{0.025, 30}} = {t_p_crit:.3f}$, the upper bound of the 95% prediction interval for $Y_f$ is *closest* to:",
        {"A": f"{hi_p:.2f}", "B": f"{hi_see_only:.2f}", "C": f"{lo_p:.2f}"},
        "A",
        rf"Point forecast is $\hat{{Y}}_f = 1.5 + 0.8(11) = {yhat_p:.2f}$. Standard error of forecast is $$s_f = 2.0\sqrt{{1 + \frac{{1}}{{32}} + \frac{{(11-5)^2}}{{31(16)}}}} = {sf_p:.4f}$$ Upper bound is ${yhat_p:.2f} + {t_p_crit:.3f}({sf_p:.4f}) = {hi_p:.2f}$.",
        {
            "B": rf"Uses SEE directly instead of $s_f$ ({hi_see_only:.2f}), ignoring parameter estimation uncertainty.",
            "C": rf"Reports the lower bound of the 95% prediction interval ({lo_p:.2f}).",
        },
    )

    # Log-log elasticity
    q_l1(
        "L1-QM-080", "LM 10", "Simple Linear Regression", "Log-Log Functional Form",
        "Interpret slope coefficients in log-transformed simple regressions.", True,
        "A regression of log quarterly revenue on log ad spend yields $\\widehat{\\ln(\\text{Rev})} = 3.20 + 0.65 \\ln(\\text{AdSpend})$. If ad spend increases by 10.0%, expected quarterly revenue increases by *approximately*:",
        {"A": "0.65%", "B": "6.50%", "C": "3.85%"},
        "B",
        "In a log-log specification, the slope coefficient $\\hat{b}_1 = 0.65$ represents elasticity: a $1\\%$ increase in $X$ produces an approximate $0.65\\%$ increase in $Y$, so a $10\\%$ increase produces $10\\% \\times 0.65 = 6.50\\%$.",
        {
            "A": "Reports the change for a 1% increase in ad spend rather than a 10% increase.",
            "C": "Adds the intercept 3.20 to 0.65 rather than scaling by the 10% change.",
        },
    )

    r2_d, mse_d, n_d = 0.60, 12.0, 22
    sse_d = mse_d * (n_d - 2)
    sst_d = sse_d / (1.0 - r2_d)
    rss_d = sst_d - sse_d
    d_sst = sst_d
    d_err_rss = sse_d * r2_d
    q_l1(
        "L1-QM-081", "LM 10", "Simple Linear Regression", "Decomposing Sum of Squares",
        "Derive ANOVA components from R-squared and MSE.", True,
        "A simple linear regression ($n = 22$) reports $R^2 = 0.60$ and mean square error $\\text{MSE} = 12.0$. The regression sum of squares (RSS) is *closest* to:",
        {"A": f"{d_err_rss:.1f}", "B": f"{d_sst:.1f}", "C": f"{rss_d:.1f}"},
        "C",
        rf"Residual sum of squares is $\text{{SSE}} = \text{{MSE}} \times (n-2) = 12.0 \times 20 = {sse_d:.1f}$. Because $\text{{SSE}}/\text{{SST}} = 1 - R^2 = 0.40$, $\text{{SST}} = {sse_d:.1f}/0.40 = {sst_d:.1f}$, giving $\text{{RSS}} = {sst_d:.1f} - {sse_d:.1f} = {rss_d:.1f}$.",
        {
            "A": rf"Multiplies SSE directly by $R^2$ ({d_err_rss:.1f}) instead of deriving SST first.",
            "B": rf"Reports total sum of squares SST ({d_sst:.1f}) instead of RSS.",
        },
    )

    q_l1(
        "L1-QM-082", "LM 10", "Simple Linear Regression", "SLR Assumptions",
        "Describe the assumptions underlying simple linear regression.", False,
        "Which assumption is *not* required for the OLS estimators in simple linear regression to be valid for standard $t$-test hypothesis inference?",
        {
            "A": "The variance of the error term is constant across all observations of $X$ (homoskedasticity).",
            "B": "The independent variable $X$ must follow a normal distribution.",
            "C": "The error terms are uncorrelated across observations.",
        },
        "B",
        "Classical linear regression assumes linearity, homoskedasticity, uncorrelated errors, and normally distributed residuals (for exact small-sample inference) — the independent variable $X$ itself need not be normally distributed.",
        {
            "A": "Homoskedasticity is a core Gauss-Markov assumption required for unadjusted OLS standard errors.",
            "C": "Uncorrelated residuals across observations are required for valid OLS standard errors.",
        },
    )

    q_l1(
        "L1-QM-083", "LM 10", "Simple Linear Regression", "Choosing Functional Forms",
        "Select appropriate log transformations for non-linear relationships.", False,
        "When modeling a firm's revenue that grows at an approximately constant percentage rate each year over time $t$, which functional form is *most appropriate*?",
        {
            "A": "Log-lin model: $\\ln(Y_t) = b_0 + b_1 t + \\varepsilon_t$",
            "B": "Lin-log model: $Y_t = b_0 + b_1 \\ln(t) + \\varepsilon_t$",
            "C": "Linear model: $Y_t = b_0 + b_1 t + \\varepsilon_t$",
        },
        "A",
        "Exponential growth at a constant proportional rate becomes linear after taking the natural logarithm of $Y_t$, making the log-lin model $\\ln(Y_t) = b_0 + b_1 t + \\varepsilon_t$ ideal.",
        {
            "B": "Lin-log models diminishing marginal dollar gains as $\\ln(X)$ rises, not constant exponential growth.",
            "C": "A linear trend implies constant *dollar* increments rather than constant *percentage* growth.",
        },
    )

    # -----------------------------------------------------------------------
    # LM 11: Financial Data Science / Big Data Techniques (7 Qs: 084 - 090)
    # -----------------------------------------------------------------------
    q_l1(
        "L1-QM-084", "LM 11", "Financial Data Science", "Big Data Characteristics",
        "Describe Big Data and alternative data sources in investment analysis.", False,
        "An asset manager incorporates real-time credit card receipts, satellite imagery of retail parking lots, and corporate earnings-call audio into its equity signals. Which Big Data dimension refers specifically to the reliability and cleanliness of these diverse datasets?",
        {"A": "Velocity", "B": "Variety", "C": "Veracity"},
        "C",
        "Big Data is characterized by Volume, Velocity (speed of generation), Variety (structured, semi-structured, and unstructured formats), and Veracity (data accuracy, trustworthiness, and noise level).",
        {
            "A": "Velocity describes the speed at which data streams are generated and processed.",
            "B": "Variety describes mixing structured numerical tables with unstructured text, audio, and satellite imagery.",
        },
    )

    q_l1(
        "L1-QM-085", "LM 11", "Financial Data Science", "Machine Learning Paradigms",
        "Distinguish supervised, unsupervised, and reinforcement learning.", False,
        "A quantitative analyst uses K-means clustering to group 1,200 global equities into peer cohorts based on financial ratios without supplying pre-assigned sector labels. This task is an example of:",
        {"A": "Supervised classification", "B": "Unsupervised learning", "C": "Reinforcement learning"},
        "B",
        "Unsupervised learning discovers hidden structure or groupings (such as clusters or principal components) in unlabeled data without a target $Y$ variable.",
        {
            "A": "Supervised learning requires labeled target outcomes $Y$ during model training.",
            "C": "Reinforcement learning optimizes sequential actions in an environment to maximize cumulative reward.",
        },
    )

    q_l1(
        "L1-QM-086", "LM 11", "Financial Data Science", "Overfitting & Generalization",
        "Explain overfitting, underfitting, and generalization error.", False,
        "A machine learning credit model achieves 99.4% accuracy on the training dataset but only 61.0% accuracy on the out-of-sample test dataset. This pattern *most strongly* indicates:",
        {"A": "Overfitting (high variance)", "B": "Underfitting (high bias)", "C": "Insufficient model complexity"},
        "A",
        "A model that memorizes training noise achieves near-perfect in-sample fit but degrades sharply out of sample — the classic signature of overfitting (excessive variance).",
        {
            "B": "Underfitting produces poor accuracy on *both* the training set and the test set.",
            "C": "Insufficient complexity leads to underfitting, whereas overfitting reflects *excessive* complexity relative to sample size.",
        },
    )

    x_raw, xmin, xmax = 18.0, 10.0, 50.0
    x_mm = (x_raw - xmin) / (xmax - xmin)
    x_mu, x_sd = 22.0, 8.0
    x_zs = (x_raw - x_mu) / x_sd
    q_l1(
        "L1-QM-087", "LM 11", "Financial Data Science", "Feature Scaling (Min-Max vs Z-Score)",
        "Calculate min-max normalized and standardized features.", True,
        "A feature representing P/E ratio has sample minimum 10.0, maximum 50.0, mean 22.0, and standard deviation 8.0. For a stock with P/E = 18.0, its min-max normalized value and standardized $z$-score are *closest* to:",
        {
            "A": f"Min-Max = {x_mm:.2f}, Z-score = {x_zs:.2f}",
            "B": f"Min-Max = {x_raw/xmax:.2f}, Z-score = {x_zs:.2f}",
            "C": f"Min-Max = {x_mm:.2f}, Z-score = {-x_zs:.2f}",
        },
        "A",
        rf"Min-max normalization maps into $[0,1]$: $$X_{{\text{{norm}}}} = \frac{{18 - 10}}{{50 - 10}} = {x_mm:.2f}$$ Standardization yields $$Z = \frac{{18 - 22}}{{8}} = {x_zs:.2f}$$",
        {
            "B": rf"Divides by max 50.0 without subtracting min 10.0 ({x_raw/xmax:.2f}).",
            "C": rf"Reverses the sign of the z-score (+0.50 instead of -0.50).",
        },
    )

    # DTM sparsity
    docs, vocab, nonzero = 500, 2000, 18000
    total_cells = docs * vocab
    sparsity = (total_cells - nonzero) / total_cells
    density = nonzero / total_cells
    d_wrong_s = nonzero / vocab
    q_l1(
        "L1-QM-088", "LM 11", "Financial Data Science", "Document-Term Matrix Sparsity",
        "Calculate sparsity of text document-term matrices.", True,
        "A text analytics pipeline builds a document-term matrix (DTM) across 500 earnings transcripts and a vocabulary of 2,000 unique tokens. If 18,000 entries are non-zero, the sparsity of the DTM is *closest* to:",
        {"A": f"{density*100:.1f}%", "B": f"{sparsity*100:.1f}%", "C": f"{100 - d_wrong_s:.1f}%"},
        "B",
        rf"Total cells equal $500 \times 2,000 = 1,000,000$. Zero entries equal $1,000,000 - 18,000 = 982,000$, so $$\text{{Sparsity}} = \frac{{982,000}}{{1,000,000}} = {sparsity*100:.1f}\%$$",
        {
            "A": rf"Reports matrix *density* (fraction of non-zero entries = {density*100:.1f}%) rather than sparsity.",
            "C": rf"Divides non-zero counts by vocabulary size alone instead of total matrix cells.",
        },
    )

    tp_l1, fp_l1, fn_l1, tn_l1 = 42, 8, 18, 132
    acc_l1 = (tp_l1 + tn_l1) / (tp_l1 + fp_l1 + fn_l1 + tn_l1)
    prec_l1 = tp_l1 / (tp_l1 + fp_l1)
    rec_l1 = tp_l1 / (tp_l1 + fn_l1)
    q_l1(
        "L1-QM-089", "LM 11", "Financial Data Science", "Confusion Matrix Metrics",
        "Calculate accuracy and precision from a classification confusion matrix.", True,
        "A machine learning default classifier evaluated on 200 bonds yields: True Positives = 42, False Positives = 8, False Negatives = 18, and True Negatives = 132. Its overall accuracy and precision are *closest* to:",
        {
            "A": f"Accuracy = {acc_l1*100:.1f}%, Precision = {rec_l1*100:.1f}%",
            "B": f"Accuracy = {prec_l1*100:.1f}%, Precision = {acc_l1*100:.1f}%",
            "C": f"Accuracy = {acc_l1*100:.1f}%, Precision = {prec_l1*100:.1f}%",
        },
        "C",
        rf"Accuracy is $(42 + 132)/200 = {acc_l1*100:.1f}\%$. Precision is $TP / (TP + FP) = 42 / (42 + 8) = {prec_l1*100:.1f}\%$.",
        {
            "A": rf"Confuses Precision with Recall ($TP/(TP+FN) = 42/60 = {rec_l1*100:.1f}\%$).",
            "B": rf"Swaps Accuracy and Precision values.",
        },
    )

    q_l1(
        "L1-QM-090", "LM 11", "Financial Data Science", "LLMs and Generative AI in Finance",
        "Evaluate capabilities and governance risks of LLMs in financial workflows.", False,
        "When integrating large language models (LLMs) into institutional equity research workflows, which operational risk is *most critical* to mitigate through retrieval-augmented generation (RAG) and human review?",
        {
            "A": "Deterministic overfitting of closed-form OLS beta estimates.",
            "B": "Hallucination of plausible-sounding but fabricated financial metrics or citations.",
            "C": "Inability to process unstructured text files without converting them to Excel tables.",
        },
        "B",
        "LLMs predict probable token sequences rather than querying verified accounting databases natively, making hallucinations (confident fabrication of figures or sources) a primary risk requiring RAG grounding and analyst verification.",
        {
            "A": "LLMs are generative transformer models rather than closed-form OLS regressions.",
            "C": "Processing unstructured text directly is a core strength of LLMs.",
        },
    )


# ===========================================================================
# LEVEL 2 QUESTIONS (60 Questions across 10 Vignettes: QM-V01 to QM-V10)
# ===========================================================================
def build_level_2():
    # -----------------------------------------------------------------------
    # QM-V01: Multiple Regression, ANOVA & Model Fit
    # -----------------------------------------------------------------------
    v1_title = "Vignette 1: Cross-Sectional Drivers of Corporate Return on Invested Capital"
    v1_text = (
        "Elena Rostova, CFA, is evaluating cross-sectional drivers of return on invested capital "
        "(ROIC, in %) across $n = 65$ industrial corporations. She estimates an unrestricted OLS "
        "multiple regression model (Model 1) with $k = 4$ predictors:\n"
        "$$\\widehat{\\text{ROIC}}_i = b_0 + b_1 \\text{Margin}_i + b_2 \\text{Turnover}_i + b_3 \\text{Capex}_i + b_4 \\text{Size}_i$$\n"
        "where Margin is operating margin (%), Turnover is asset turnover (x), Capex is capital "
        "expenditures/sales (%), and Size is $\\ln(\\text{Total Assets})$. Model 1 output reports:\n"
        "- Estimates (SE): Intercept $b_0 = 2.10\\ (0.90)$, Margin $b_1 = 0.65\\ (0.15)$, "
        "Turnover $b_2 = 4.20\\ (1.05)$, Capex $b_3 = -0.35\\ (0.25)$, Size $b_4 = 0.40\\ (0.16)$.\n"
        "- ANOVA (Model 1): Regression SS ($\\text{RSS}$) = $420.0$, Residual SS ($\\text{SSE}$) = $180.0$, Total SS ($\\text{SST}$) = $600.0$.\n"
        "- Restricted Model 2 (omitting Capex and Size, $k = 2$): $\\text{SSE}_R = 204.0$.\n"
        r"- Critical values at $\alpha = 5\%$: $t_{0.025, 60} = 2.000$, $F_{0.05, 4, 60} = 2.525$, $F_{0.05, 2, 60} = 3.150$."
    )
    b_v1 = [2.10, 0.65, 4.20, -0.35, 0.40]
    roic_hat = b_v1[0] + b_v1[1] * 12.0 + b_v1[2] * 1.5 + b_v1[3] * 4.0 + b_v1[4] * 10.0
    roic_no_int = roic_hat - b_v1[0]
    roic_pos_capex = roic_hat - 2.0 * b_v1[3] * 4.0
    q_l2(
        "L2-QM-V01-Q1", "LM 1", "Evaluating Regression Model Fit", "Multiple Regression Prediction",
        "QM-V01", v1_title, v1_text,
        "Calculate predicted values from a multiple regression equation.", True,
        "For an industrial firm with Margin = 12.0%, Turnover = 1.5x, Capex = 4.0%, and Size = 10.0, Model 1's predicted ROIC is *closest* to:",
        {"A": f"{roic_no_int:.2f}%", "B": f"{roic_hat:.2f}%", "C": f"{roic_pos_capex:.2f}%"},
        "B",
        rf"Substituting into Model 1: $$\widehat{{\text{{ROIC}}}} = 2.10 + 0.65(12.0) + 4.20(1.5) - 0.35(4.0) + 0.40(10.0) = {roic_hat:.2f}\%$$",
        {
            "A": rf"Omits the intercept $b_0 = 2.10$ ({roic_no_int:.2f}%).",
            "C": rf"Adds $+0.35(4.0)$ instead of subtracting $-0.35(4.0)$ ({roic_pos_capex:.2f}%).",
        },
    )

    n_v1, k_v1, rss_v1, sse_v1, sst_v1 = 65, 4, 420.0, 180.0, 600.0
    r2_v1 = rss_v1 / sst_v1
    adj_r2_v1 = 1.0 - ((n_v1 - 1.0) / (n_v1 - k_v1 - 1.0)) * (1.0 - r2_v1)
    adj_r2_err_df = 1.0 - (n_v1 / (n_v1 - k_v1)) * (1.0 - r2_v1)
    q_l2(
        "L2-QM-V01-Q2", "LM 1", "Evaluating Regression Model Fit", "R-Squared & Adjusted R-Squared",
        "QM-V01", v1_title, v1_text,
        "Calculate and interpret R-squared and adjusted R-squared.", True,
        "Based on Model 1's ANOVA summary, $R^2$ and adjusted $R^2$ ($R_a^2$) are *closest* to:",
        {
            "A": f"R2 = {r2_v1:.2f}, Adjusted R2 = {adj_r2_v1:.2f}",
            "B": f"R2 = {r2_v1:.2f}, Adjusted R2 = {adj_r2_err_df:.4f}",
            "C": f"R2 = {1-r2_v1:.2f}, Adjusted R2 = {adj_r2_v1:.2f}",
        },
        "A",
        rf"$R^2 = \text{{RSS}}/\text{{SST}} = 420/600 = {r2_v1:.2f}$. Adjusted $R^2$ penalizes for $k=4$ predictors: $$R_a^2 = 1 - \left(\frac{{65 - 1}}{{65 - 4 - 1}}\right)(1 - 0.70) = 1 - \frac{{64}}{{60}}(0.30) = {adj_r2_v1:.2f}$$",
        {
            "B": rf"Uses $n/(n-k)$ instead of $(n-1)/(n-k-1)$ ({adj_r2_err_df:.4f}).",
            "C": rf"Reports $\text{{SSE}}/\text{{SST}} = 0.30$ instead of $R^2 = 0.70$.",
        },
    )

    msr_v1 = rss_v1 / k_v1
    mse_v1 = sse_v1 / (n_v1 - k_v1 - 1)
    f_v1 = msr_v1 / mse_v1
    f_v1_err = (rss_v1 / (n_v1 - k_v1 - 1)) / (sse_v1 / k_v1)
    q_l2(
        "L2-QM-V01-Q3", "LM 1", "Evaluating Regression Model Fit", "Overall F-Test",
        "QM-V01", v1_title, v1_text,
        "Formulate and interpret the overall F-test in multiple regression.", True,
        "The overall $F$-statistic for testing whether all four slope coefficients in Model 1 equal zero jointly is *closest* to:",
        {"A": f"{msr_v1:.2f}", "B": f"{f_v1_err:.2f}", "C": f"{f_v1:.2f}"},
        "C",
        rf"$\text{{MSR}} = 420.0 / 4 = {msr_v1:.2f}$ and $\text{{MSE}} = 180.0 / 60 = {mse_v1:.2f}$. Thus $F = 105.0 / 3.0 = {f_v1:.2f}$, exceeding $F_{{0.05,4,60}} = 2.525$ and rejecting the joint null.",
        {
            "A": rf"Reports MSR ({msr_v1:.2f}) without dividing by MSE ({mse_v1:.2f}).",
            "B": rf"Swaps numerator and denominator degrees of freedom ({f_v1_err:.2f}).",
        },
    )

    sse_r_v1 = 204.0
    q_res = 2
    f_part = ((sse_r_v1 - sse_v1) / q_res) / mse_v1
    f_part_noq = (sse_r_v1 - sse_v1) / mse_v1
    q_l2(
        "L2-QM-V01-Q4", "LM 1", "Evaluating Regression Model Fit", "Partial F-Test (Nested Models)",
        "QM-V01", v1_title, v1_text,
        "Conduct a partial F-test comparing nested regression models.", True,
        "Comparing restricted Model 2 against unrestricted Model 1, the partial $F$-statistic for testing $H_0: b_3 = b_4 = 0$ and conclusion at $\\alpha = 5\\%$ are *closest* to:",
        {
            "A": f"F = {f_part_noq:.2f}; reject H0",
            "B": f"F = {f_part:.2f}; fail to reject H0",
            "C": f"F = {f_part:.2f}; reject H0",
        },
        "C",
        rf"With $q = 2$ excluded predictors and $\text{{MSE}}_U = 180/60 = 3.0$: $$F = \frac{{(\text{{SSE}}_R - \text{{SSE}}_U)/q}}{{\text{{MSE}}_U}} = \frac{{(204.0 - 180.0)/2}}{{3.0}} = {f_part:.2f}$$ Since ${f_part:.2f} > F_{{0.05, 2, 60}} = 3.150$, we reject $H_0$: Capex and Size are jointly significant.",
        {
            "A": rf"Forgets to divide $(\text{{SSE}}_R - \text{{SSE}}_U)$ by $q = 2$ ({f_part_noq:.2f}).",
            "B": rf"Computes the right statistic ($F = {f_part:.2f}$) but reaches the wrong decision against $3.150$.",
        },
    )

    t_crit_v1 = 2.000
    ci_b1_lo = 0.65 - t_crit_v1 * 0.15
    ci_b1_hi = 0.65 + t_crit_v1 * 0.15
    q_l2(
        "L2-QM-V01-Q5", "LM 1", "Evaluating Regression Model Fit", "Partial Slope Confidence Interval",
        "QM-V01", v1_title, v1_text,
        "Construct confidence intervals for individual partial regression coefficients.", True,
        "Using Model 1's output, the 95% confidence interval for the partial slope coefficient on Margin ($b_1$) is *closest* to:",
        {
            "A": f"[{ci_b1_lo:.2f}, {ci_b1_hi:.2f}]",
            "B": f"[{0.65 - 0.15:.2f}, {0.65 + 0.15:.2f}]",
            "C": f"[{0.65 - 1.67*0.15:.2f}, {0.65 + 1.67*0.15:.2f}]",
        },
        "A",
        rf"With $df = n - k - 1 = 60$ and $t_{{0.025, 60}} = 2.000$: $$0.65 \pm 2.000(0.15) = [{ci_b1_lo:.2f},\, {ci_b1_hi:.2f}]$$",
        {
            "B": r"Constructs a $\pm 1$ standard error band rather than multiplying by $t_{0.025, 60} = 2.000$.",
            "C": "Uses a one-tailed 5% critical value ($1.67$) instead of the two-tailed 95% critical value ($2.000$).",
        },
    )

    q_l2(
        "L2-QM-V01-Q6", "LM 1", "Evaluating Regression Model Fit", "Coefficient Interpretation & BIC",
        "QM-V01", v1_title, v1_text,
        "Interpret partial coefficients and compare AIC vs BIC criteria.", False,
        "If Rostova wishes to select the most parsimonious specification between Model 1 and Model 2 for explaining historical ROIC while penalizing extra parameters more heavily for $n = 65$, which statement is *most likely* correct?",
        {
            "A": "She should prefer BIC over AIC because $\\ln(65) > 2$, imposing a stricter penalty per parameter.",
            "B": "She should prefer AIC over BIC because AIC imposes a $\\ln(n)$ penalty per parameter.",
            "C": "She should choose whichever model yields the higher unadjusted $R^2$ regardless of parameter count.",
        },
        "A",
        "BIC adds $\\ln(n)(k+1)$ to $n \\ln(\\text{SSE}/n)$, whereas AIC adds $2(k+1)$. Because $\\ln(65) \\approx 4.17 > 2$, BIC penalizes additional predictors more severely and favors parsimony.",
        {
            "B": "Reverses the penalty terms: AIC uses $2(k+1)$, while BIC uses $\\ln(n)(k+1)$.",
            "C": "Unadjusted $R^2$ never decreases when variables are added and therefore cannot identify parsimonious models.",
        },
    )

    # -----------------------------------------------------------------------
    # QM-V02: Regression Diagnostics & Model Misspecification
    # -----------------------------------------------------------------------
    v2_title = "Vignette 2: Diagnostic Testing of a Multi-Factor Equity Return Model"
    v2_text = (
        "Marcus Vance, CFA, regresses monthly excess returns of an industrial equity portfolio "
        "($n = 80$ months) on $k = 3$ style factors: Market ($\\text{MKT}$), Value ($\\text{HML}$), "
        "and Momentum ($\\text{UMD}$).\n"
        r"- Initial OLS estimates for Value ($\text{HML}$): $\hat{b}_{\text{HML}} = 0.48$, "
        "unadjusted OLS $SE = 0.15$, White heteroskedasticity-consistent $SE = 0.26$.\n"
        r"- Breusch-Pagan test: Regressing squared OLS residuals $\hat{\varepsilon}_t^2$ on all three factors "
        r"yields $R^2_{\text{resid}} = 0.135$." "\n"
        "- Serial correlation & Collinearity diagnostics: Durbin-Watson $d = 1.12$ ($d_L = 1.56, d_U = 1.72$ at 5%); "
        r"auxiliary regression of Momentum on Market and Value gives $R^2_{\text{UMD}} = 0.84$." "\n"
        r"- Critical values at $\alpha = 5\%$: $t_{0.025, 76} = 1.992$, $\chi^2_{0.05, 3} = 7.815$."
    )
    n_v2, k_v2, r2_bp = 80, 3, 0.135
    bp_stat = n_v2 * r2_bp
    bp_err_df = (n_v2 - k_v2 - 1) * r2_bp
    q_l2(
        "L2-QM-V02-Q1", "LM 2", "Model Misspecification", "Breusch-Pagan Test",
        "QM-V02", v2_title, v2_text,
        "Conduct and interpret the Breusch-Pagan test for conditional heteroskedasticity.", True,
        "The Breusch-Pagan test statistic and conclusion regarding conditional heteroskedasticity at $\\alpha = 5\\%$ are *closest* to:",
        {
            "A": f"BP = {bp_stat:.2f}; fail to reject homoskedasticity",
            "B": f"BP = {bp_stat:.2f}; reject homoskedasticity (conditional heteroskedasticity present)",
            "C": f"BP = {bp_err_df:.2f}; reject homoskedasticity",
        },
        "B",
        rf"The Breusch-Pagan statistic is $BP = n \times R^2_{{\text{{resid}}}} = 80 \times 0.135 = {bp_stat:.2f}$, distributed as $\chi^2_3$. Since ${bp_stat:.2f} > 7.815$, we reject the null of homoskedasticity.",
        {
            "A": rf"Computes the correct statistic ({bp_stat:.2f}) but misinterprets the rejection direction.",
            "C": rf"Multiplies $R^2_{{\text{{resid}}}}$ by $n - k - 1 = 76$ instead of $n = 80$ ({bp_err_df:.2f}).",
        },
    )

    b_hml, se_ols, se_white = 0.48, 0.15, 0.26
    t_ols = b_hml / se_ols
    t_white = b_hml / se_white
    q_l2(
        "L2-QM-V02-Q2", "LM 2", "Model Misspecification", "White Robust Standard Errors",
        "QM-V02", v2_title, v2_text,
        "Adjust t-statistics using White heteroskedasticity-consistent standard errors.", True,
        r"Comparing the unadjusted OLS $t$-statistic against the White robust $t$-statistic for $\hat{b}_{\text{HML}}$ at $\alpha = 5\%$ ($t_{0.025, 76} = 1.992$), which outcome occurs?",
        {
            "A": f"OLS t = {t_ols:.2f} (significant); White t = {t_white:.2f} (insignificant)",
            "B": f"OLS t = {t_ols:.2f} (significant); White t = {t_white:.2f} (significant)",
            "C": f"OLS t = {t_white:.2f} (insignificant); White t = {t_ols:.2f} (significant)",
        },
        "A",
        rf"OLS $t = 0.48 / 0.15 = {t_ols:.2f} > 1.992$ (appears significant), whereas White robust $t = 0.48 / 0.26 = {t_white:.2f} < 1.992$ (not statistically significant at 5%).",
        {
            "B": rf"Misclassifies $|{t_white:.2f}|$ as exceeding $1.992$.",
            "C": "Reverses the OLS and White standard errors.",
        },
    )

    dw_v2 = 1.12
    rho_hat = 1.0 - dw_v2 / 2.0
    q_l2(
        "L2-QM-V02-Q3", "LM 2", "Model Misspecification", "Durbin-Watson Serial Correlation",
        "QM-V02", v2_title, v2_text,
        "Detect serial correlation using the Durbin-Watson statistic.", True,
        "From the Durbin-Watson statistic $d = 1.12$, the implied first-order residual autocorrelation $\\hat{\\rho}$ and test conclusion are *closest* to:",
        {
            "A": f"rho = {rho_hat:.2f}; positive serial correlation present",
            "B": f"rho = {-rho_hat:.2f}; negative serial correlation present",
            "C": f"rho = {rho_hat:.2f}; inconclusive serial correlation test",
        },
        "A",
        rf"Using $d \approx 2(1 - \hat{{\rho}})$ gives $\hat{{\rho}} \approx 1 - 1.12/2 = {rho_hat:.2f}$. Because $d = 1.12 < d_L = 1.56$, there is significant positive serial correlation.",
        {
            "B": "Reverses the sign; $d < 2$ corresponds to positive, not negative, autocorrelation.",
            "C": "The test is only inconclusive when $d_L < d < d_U$; here $1.12 < 1.56$ rejects cleanly.",
        },
    )

    r2_umd = 0.84
    vif_umd = 1.0 / (1.0 - r2_umd)
    tol_umd = 1.0 - r2_umd
    q_l2(
        "L2-QM-V02-Q4", "LM 2", "Model Misspecification", "Variance Inflation Factor (VIF)",
        "QM-V02", v2_title, v2_text,
        "Calculate and interpret Variance Inflation Factors for multicollinearity.", True,
        "The Variance Inflation Factor (VIF) for the Momentum factor and its diagnostic implication are *closest* to:",
        {
            "A": f"VIF = {tol_umd:.2f}; no multicollinearity concern",
            "B": f"VIF = {vif_umd:.2f}; warrants further investigation (> 5)",
            "C": f"VIF = {1.0/r2_umd:.2f}; negligible multicollinearity",
        },
        "B",
        rf"$\text{{VIF}}_{{\text{{UMD}}}} = \frac{{1}}{{1 - R^2_{{\text{{UMD}}}}}} = \frac{{1}}{{1 - 0.84}} = {vif_umd:.2f}$. Because $\text{{VIF}} > 5$, multicollinearity warrants investigation.",
        {
            "A": rf"Reports tolerance $1 - R^2 = {tol_umd:.2f}$ instead of its reciprocal.",
            "C": rf"Computes $1 / R^2 = {1/r2_umd:.2f}$ instead of $1 / (1 - R^2)$.",
        },
    )

    q_l2(
        "L2-QM-V02-Q5", "LM 2", "Model Misspecification", "Conditional vs Unconditional Heteroskedasticity",
        "QM-V02", v2_title, v2_text,
        "Contrast conditional and unconditional heteroskedasticity effects on OLS.", False,
        "In the presence of conditional heteroskedasticity *alone* (without serial correlation or omitted variables), unadjusted OLS regression estimators are *most likely*:",
        {
            "A": "Biased and inconsistent, requiring non-linear maximum likelihood re-estimation.",
            "B": "Unbiased and consistent, but standard errors are typically understated, inflating Type I error rates.",
            "C": "Biased downward, causing adjusted $R^2$ to become negative.",
        },
        "B",
        "Conditional heteroskedasticity leaves OLS slope coefficients unbiased and consistent, but invalidates standard error formulas (typically understating SEs, inflating $t$-statistics, and causing excessive false rejections).",
        {
            "A": "Heteroskedasticity affects coefficient *efficiency and standard errors*, not unbiasedness or consistency.",
            "C": "Coefficient estimates remain unbiased in expectation.",
        },
    )

    q_l2(
        "L2-QM-V02-Q6", "LM 2", "Model Misspecification", "Newey-West HAC & Omitted Variables",
        "QM-V02", v2_title, v2_text,
        "Identify remedies for serial correlation, heteroskedasticity, and omitted variables.", False,
        "Because Vance's regression simultaneously exhibits *both* conditional heteroskedasticity and positive serial correlation, which correction preserves OLS point estimates while producing valid standard errors for $t$-tests?",
        {
            "A": "Newey-West heteroskedasticity and autocorrelation consistent (HAC) standard errors.",
            "B": "Dropping the Momentum factor without replacing it.",
            "C": "Multiplying all returns by 12 to annualize the regression residuals.",
        },
        "A",
        "Newey-West (HAC) standard errors adjust for *both* conditional heteroskedasticity and serial correlation simultaneously while keeping OLS parameter estimates intact.",
        {
            "B": "Dropping a relevant predictor risks omitted variable bias, corrupting remaining slope estimates.",
            "C": "Linearly scaling returns leaves $t$-statistics and serial correlation unchanged.",
        },
    )

    # -----------------------------------------------------------------------
    # QM-V03: Dummy Variables, Interactions & Logistic Regression
    # -----------------------------------------------------------------------
    v3_title = "Vignette 3: Corporate Credit Spreads and Logistic Default Modeling"
    v3_text = (
        "Priya Nair, CFA, builds two quantitative credit models using a sample of $n = 300$ corporate issuers.\n"
        "- **Model A (OLS Spread Model):**\n"
        r"$$\widehat{\text{Spread}}_i = 1.80 + 0.45\,\text{Leverage}_i + 0.60\,D_{\text{HY},i} + 0.25\,(D_{\text{HY},i} \times \text{Leverage}_i)$$" "\n"
        r"where Spread is in %, Leverage is Debt/EBITDA, and $D_{\text{HY}} = 1$ for high-yield issuers ($0$ for investment-grade)." "\n"
        "- **Model B (Logistic Default Model):**\n"
        r"$$\ln\left(\frac{P_i}{1 - P_i}\right) = -3.40 + 0.85\,\text{Leverage}_i - 0.30\,\text{IntCov}_i$$" "\n"
        "where $P_i$ is 1-year default probability and $\\text{IntCov}$ is interest coverage. Log-likelihood of the null intercept-only model is $\\ln L_0 = -180.0$ and of Model B is $\\ln L_1 = -135.0$."
    )
    sp_hy = 1.80 + 0.45 * 4.0 + 0.60 + 0.25 * 4.0
    sp_ig = 1.80 + 0.45 * 4.0
    sp_noint = 1.80 + 0.45 * 4.0 + 0.60
    q_l2(
        "L2-QM-V03-Q1", "LM 3", "Extensions of Multiple Regression", "Interaction Dummy Prediction",
        "QM-V03", v3_title, v3_text,
        "Formulate and interpret dummy variables and interaction terms.", True,
        r"Under Model A, the predicted credit spread for a high-yield issuer ($D_{\text{HY}} = 1$) with Leverage = 4.0x is *closest* to:",
        {"A": f"{sp_ig:.2f}%", "B": f"{sp_noint:.2f}%", "C": f"{sp_hy:.2f}%"},
        "C",
        rf"Setting $D_{{\text{{HY}}}} = 1$ and $\text{{Leverage}} = 4.0$: $$\widehat{{\text{{Spread}}}} = 1.80 + 0.45(4.0) + 0.60(1) + 0.25(1 \times 4.0) = {sp_hy:.2f}\%$$",
        {
            "A": rf"Omits both the high-yield intercept shift ($0.60$) and slope interaction ($0.25 \times 4.0$), giving the IG spread ({sp_ig:.2f}%).",
            "B": rf"Includes the intercept shift ($0.60$) but omits the interaction slope term ({sp_noint:.2f}%).",
        },
    )

    q_l2(
        "L2-QM-V03-Q2", "LM 3", "Extensions of Multiple Regression", "Dummy Variable Trap",
        "QM-V03", v3_title, v3_text,
        "Avoid the dummy variable trap when encoding qualitative categories.", False,
        "Suppose Nair expands Model A to distinguish four credit tiers (AAA/AA, A, BBB, and High Yield) while retaining the regression intercept $b_0$. How many dummy variables should she include, and why?",
        {
            "A": "Three dummy variables, because including four dummies alongside an intercept creates exact multicollinearity (the dummy variable trap).",
            "B": "Four dummy variables, to avoid omitting information about the reference rating tier.",
            "C": "Two dummy variables, because half of the categories serve as the reference benchmark.",
        },
        "A",
        r"To represent $m$ mutually exclusive categories in a regression with an intercept, include $m - 1$ dummy variables ($4 - 1 = 3$); including all $m$ creates perfect linear dependence ($\sum D_j = 1$).",
        {
            "B": "Including all 4 dummies with an intercept creates perfect multicollinearity, making $(X'X)$ non-invertible.",
            "C": "Only 1 category is absorbed into the intercept as the reference group, requiring $4 - 1 = 3$ dummies.",
        },
    )

    z_log = -3.40 + 0.85 * 4.0 - 0.30 * 2.0
    z_wrong_sign = -3.40 + 0.85 * 4.0 + 0.30 * 2.0
    q_l2(
        "L2-QM-V03-Q3", "LM 3", "Extensions of Multiple Regression", "Logistic Regression Log-Odds",
        "QM-V03", v3_title, v3_text,
        "Calculate log-odds from a logistic regression model.", True,
        "For an issuer with Leverage = 4.0x and Interest Coverage = 2.0x, Model B's predicted log-odds of default are *closest* to:",
        {"A": f"{z_log:.2f}", "B": f"{z_wrong_sign:.2f}", "C": f"{math.exp(z_log):.2f}"},
        "A",
        rf"Evaluating the linear log-odds index: $$\ln\left(\frac{{P}}{{1-P}}\right) = -3.40 + 0.85(4.0) - 0.30(2.0) = {z_log:.2f}$$",
        {
            "B": rf"Adds $+0.30(2.0)$ instead of subtracting $-0.30(2.0)$ ({z_wrong_sign:.2f}).",
            "C": rf"Reports the odds ratio $e^{{{z_log:.2f}}} = {math.exp(z_log):.2f}$ rather than the log-odds.",
        },
    )

    p_def = 1.0 / (1.0 + math.exp(-z_log))
    p_comp = 1.0 - p_def
    p_odds = math.exp(z_log)
    q_l2(
        "L2-QM-V03-Q4", "LM 3", "Extensions of Multiple Regression", "Logistic Default Probability",
        "QM-V03", v3_title, v3_text,
        "Convert logistic regression log-odds into event probability.", True,
        f"Using Model B's log-odds of {z_log:.2f} for the issuer above, the predicted 1-year default probability is *closest* to:",
        {"A": f"{p_odds*100:.2f}%", "B": f"{p_def*100:.2f}%", "C": f"{p_comp*100:.2f}%"},
        "B",
        rf"Converting log-odds $z = {z_log:.2f}$ to probability: $$P = \frac{{1}}{{1 + e^{{-z}}}} = \frac{{1}}{{1 + e^{{0.60}}}} = {p_def*100:.2f}\%$$",
        {
            "A": rf"Reports the odds $e^{{-0.60}} = {p_odds:.4f}$ ({p_odds*100:.2f}%) rather than $P = \text{{odds}} / (1 + \text{{odds}})$.",
            "C": rf"Reports the survival probability $1 - P = {p_comp*100:.2f}\%$ instead of default probability $P$.",
        },
    )

    or_lev = math.exp(0.85)
    or_pct = (or_lev - 1.0) * 100.0
    q_l2(
        "L2-QM-V03-Q5", "LM 3", "Extensions of Multiple Regression", "Logistic Odds Ratio",
        "QM-V03", v3_title, v3_text,
        "Interpret slope coefficients as odds ratios in logistic regression.", True,
        "Holding Interest Coverage constant, a 1.0x increase in Leverage changes the *odds* of default by a multiplicative factor (odds ratio) *closest* to:",
        {"A": "0.85x (+85.0%)", "B": f"{or_lev:.2f}x (+{or_pct:.1f}%)", "C": f"{math.exp(-0.85):.2f}x (-{(1-math.exp(-0.85))*100:.1f}%)"},
        "B",
        rf"A 1-unit rise in Leverage adds $0.85$ to log-odds, multiplying odds by $e^{{0.85}} = {or_lev:.2f}$ (a $+{or_pct:.1f}\%$ increase in odds).",
        {
            "A": "Interprets the log-odds slope coefficient directly as the multiplicative odds factor without exponentiating.",
            "C": rf"Applies a negative exponent $e^{{-0.85}} = {math.exp(-0.85):.2f}$.",
        },
    )

    lr_stat = -2.0 * (-180.0 - (-135.0))
    pseudo_r2 = 1.0 - (-135.0 / -180.0)
    q_l2(
        "L2-QM-V03-Q6", "LM 3", "Extensions of Multiple Regression", "Likelihood Ratio & McFadden R2",
        "QM-V03", v3_title, v3_text,
        "Evaluate logistic regression fit using likelihood ratio and pseudo-R2.", True,
        "For Model B, the Likelihood Ratio (LR) test statistic and McFadden's pseudo-$R^2$ are *closest* to:",
        {
            "A": f"LR = {lr_stat/2.0:.1f}, pseudo-R2 = {pseudo_r2:.2f}",
            "B": f"LR = {lr_stat:.1f}, pseudo-R2 = {1-pseudo_r2:.2f}",
            "C": f"LR = {lr_stat:.1f}, pseudo-R2 = {pseudo_r2:.2f}",
        },
        "C",
        rf"$\text{{LR}} = -2(\ln L_0 - \ln L_1) = -2(-180 - (-135)) = {lr_stat:.1f}$. McFadden's pseudo-$R^2$ is $1 - \frac{{\ln L_1}}{{\ln L_0}} = 1 - \frac{{-135}}{{-180}} = {pseudo_r2:.2f}$.",
        {
            "A": rf"Omits the factor of 2 in the LR formula ({lr_stat/2:.1f}).",
            "B": rf"Reports $\ln L_1 / \ln L_0 = {1-pseudo_r2:.2f}$ rather than $1 - \ln L_1 / \ln L_0$.",
        },
    )

    # -----------------------------------------------------------------------
    # QM-V04: Time-Series Trends & AR(1) Mean Reversion
    # -----------------------------------------------------------------------
    v4_title = "Vignette 4: Revenue Trend Modeling and AR(1) Operating Margin Mean Reversion"
    v4_text = (
        "Devon Park, CFA, analyzes quarterly revenue ($\\text{Rev}_t$, in USD millions) and operating "
        "margin ($\\text{Margin}_t$, in %) for a consumer brand across $T = 64$ quarters.\n"
        "- **Revenue Log-Linear Trend (estimated on $t=1,\\dots,40$):**\n"
        "$$\\widehat{\\ln(\\text{Rev}_t)} = 5.20 + 0.045\\,t \\quad (DW = 0.68)$$\n"
        "- **Operating Margin AR(1) Model (estimated on $T = 64$ quarters):**\n"
        r"$$\widehat{\text{Margin}}_t = 3.60 + 0.70\,\text{Margin}_{t-1}, \quad \text{Margin}_{64} = 15.0\%$$" "\n"
        "- Residual autocorrelations from the AR(1) model: lag 1 $r_1 = 0.06$, lag 2 $r_2 = 0.31$ "
        r"($SE = 1/\sqrt{64} = 0.125$; 5% critical $t = 2.00$)." "\n"
        "- Out-of-sample AR(1) forecast errors across 4 holdout quarters (%): `-0.8, 1.2, -1.0, 0.6`."
    )
    g_qtr = math.exp(0.045) - 1.0
    rev_t41 = math.exp(5.20 + 0.045 * 41)
    q_l2(
        "L2-QM-V04-Q1", "LM 4", "Time-Series Analysis", "Log-Linear Trend Forecasting",
        "QM-V04", v4_title, v4_text,
        "Compute implied growth rates and forecasts from a log-linear trend model.", True,
        "From the log-linear revenue trend, the implied quarterly compound growth rate and predicted revenue at $t = 41$ are *closest* to:",
        {
            "A": f"Growth = 4.50%/qtr, Rev41 = USD {rev_t41:.1f}M",
            "B": f"Growth = {g_qtr*100:.2f}%/qtr, Rev41 = USD {rev_t41:.1f}M",
            "C": f"Growth = {g_qtr*100:.2f}%/qtr, Rev41 = USD {5.20 + 0.045*41:.2f}M",
        },
        "B",
        rf"In $\ln(\text{{Rev}}_t) = b_0 + b_1 t$, the exact discrete quarterly growth rate is $e^{{b_1}} - 1 = e^{{0.045}} - 1 = {g_qtr*100:.2f}\%$. Forecast at $t=41$ is $\exp(5.20 + 0.045(41)) = \text{{USD }}{rev_t41:.1f}\text{{M}}$.",
        {
            "A": "Reports the continuously compounded slope $0.045$ (4.50%) rather than the discrete quarterly growth rate $e^{0.045} - 1$.",
            "C": rf"Reports the predicted natural log value ({5.20 + 0.045*41:.2f}) without exponentiating.",
        },
    )

    q_l2(
        "L2-QM-V04-Q2", "LM 4", "Time-Series Analysis", "Trend Model Serial Correlation",
        "QM-V04", v4_title, v4_text,
        "Evaluate limitations of trend models using Durbin-Watson diagnostics.", False,
        "Given the log-linear trend model's Durbin-Watson statistic of $0.68$, Park should *most likely* conclude that:",
        {
            "A": "Strong positive serial correlation remains in the residuals, requiring an autoregressive model instead of a pure deterministic trend.",
            "B": "The revenue series is stationary around a white-noise error process and needs no dynamic lags.",
            "C": "Negative serial correlation is present, causing standard errors to be overly conservative.",
        },
        "A",
        "A Durbin-Watson statistic of 0.68 is well below 2.0, signaling strong positive autocorrelation in the trend residuals ($\\hat{\\rho} \\approx 0.66$). Trend models alone fail to capture serial dependence; an AR specification is needed.",
        {
            "B": "White-noise residuals would yield $DW \\approx 2.0$, not $0.68$.",
            "C": "$DW < 2$ indicates *positive* serial correlation, which understates standard errors rather than inflating them.",
        },
    )

    m65 = 3.60 + 0.70 * 15.0
    m66 = 3.60 + 0.70 * m65
    m_star = 3.60 / (1.0 - 0.70)
    q_l2(
        "L2-QM-V04-Q3", "LM 4", "Time-Series Analysis", "AR(1) One-Step Forecast",
        "QM-V04", v4_title, v4_text,
        "Calculate one-step-ahead forecasts from an AR(1) model.", True,
        r"Using the AR(1) operating margin model with $\text{Margin}_{64} = 15.0\%$, the 1-quarter-ahead forecast $\widehat{\text{Margin}}_{65}$ is *closest* to:",
        {"A": f"{m66:.2f}%", "B": f"{m65:.2f}%", "C": f"{m_star:.2f}%"},
        "B",
        rf"Applying the chain rule of forecasting one period forward: $$\widehat{{\text{{Margin}}}}_{{65}} = 3.60 + 0.70(15.0) = {m65:.2f}\%$$",
        {
            "A": rf"Reports the two-step-ahead forecast $\widehat{{\text{{Margin}}}}_{{66}} = {m66:.2f}\%$.",
            "C": rf"Reports the long-run mean-reverting level ({m_star:.2f}%).",
        },
    )

    m66_no_int = 0.70 * m65
    q_l2(
        "L2-QM-V04-Q4", "LM 4", "Time-Series Analysis", "AR(1) Multi-Step Chain Rule",
        "QM-V04", v4_title, v4_text,
        "Calculate multi-period forecasts using the chain rule of forecasting.", True,
        r"Using the chain rule of forecasting, the 2-quarter-ahead forecast $\widehat{\text{Margin}}_{66}$ is *closest* to:",
        {"A": f"{m66:.2f}%", "B": f"{m66_no_int:.2f}%", "C": f"{m65:.2f}%"},
        "A",
        rf"Feeding $\widehat{{\text{{Margin}}}}_{{65}} = {m65:.2f}\%$ back into the AR(1) equation gives $$\widehat{{\text{{Margin}}}}_{{66}} = 3.60 + 0.70({m65:.2f}) = {m66:.2f}\%$$",
        {
            "B": rf"Omits the intercept $b_0 = 3.60$ in step 2 ({m66_no_int:.2f}%).",
            "C": rf"Reports the 1-step-ahead forecast ({m65:.2f}%).",
        },
    )

    m_star_wrong = 3.60 / 0.70
    q_l2(
        "L2-QM-V04-Q5", "LM 4", "Time-Series Analysis", "AR(1) Mean-Reverting Level",
        "QM-V04", v4_title, v4_text,
        "Determine the mean-reverting level of a covariance-stationary AR(1) series.", True,
        "The long-run mean-reverting operating margin level implied by the AR(1) model is *closest* to:",
        {"A": f"{m_star_wrong:.2f}%", "B": "3.60%", "C": f"{m_star:.2f}%"},
        "C",
        rf"For a covariance-stationary AR(1) model ($|b_1| = 0.70 < 1$), the mean-reverting level is $$x^* = \frac{{b_0}}{{1 - b_1}} = \frac{{3.60}}{{1 - 0.70}} = {m_star:.2f}\%$$",
        {
            "A": rf"Divides $b_0$ by $b_1$ instead of $(1 - b_1)$ ({m_star_wrong:.2f}%).",
            "B": "Reports the intercept $b_0 = 3.60\\%$ directly without scaling by $1/(1-b_1)$.",
        },
    )

    errs_v4 = [-0.8, 1.2, -1.0, 0.6]
    rmse_v4 = math.sqrt(sum(e * e for e in errs_v4) / len(errs_v4))
    t_lag2 = 0.31 / 0.125
    q_l2(
        "L2-QM-V04-Q6", "LM 4", "Time-Series Analysis", "Residual Autocorrelation & RMSE",
        "QM-V04", v4_title, v4_text,
        "Test AR model residuals for autocorrelation and compute out-of-sample RMSE.", True,
        "Based on the AR(1) residual autocorrelations and out-of-sample forecast errors, the lag-2 residual $t$-statistic and holdout RMSE are *closest* to:",
        {
            "A": f"t(lag 2) = {t_lag2:.2f} (misspecified; add lag 2), RMSE = {rmse_v4:.3f}%",
            "B": f"t(lag 2) = {0.06/0.125:.2f} (correctly specified), RMSE = {rmse_v4:.3f}%",
            "C": f"t(lag 2) = {t_lag2:.2f} (misspecified; add lag 2), RMSE = {sum(abs(e) for e in errs_v4)/4:.3f}%",
        },
        "A",
        rf"Lag-2 autocorrelation $t$-statistic is $r_2 / SE = 0.31 / 0.125 = {t_lag2:.2f} > 2.00$, indicating significant lag-2 residual autocorrelation (requiring an AR(2) model). Out-of-sample RMSE is $$\sqrt{{\frac{{(-0.8)^2 + 1.2^2 + (-1.0)^2 + 0.6^2}}{{4}}}} = {rmse_v4:.3f}\%$$",
        {
            "B": rf"Tests lag 1 ($t = {0.06/0.125:.2f}$) and overlooks the significant lag-2 correlation.",
            "C": rf"Reports Mean Absolute Error ({sum(abs(e) for e in errs_v4)/4:.3f}%) instead of Root Mean Squared Error.",
        },
    )

    # -----------------------------------------------------------------------
    # QM-V05: Unit Roots, Random Walks & Cointegration
    # -----------------------------------------------------------------------
    v5_title = "Vignette 5: Non-Stationarity, Unit Roots, and Energy Spread Cointegration"
    v5_text = (
        "Hannah Cho, CFA, studies daily front-month WTI ($W_t$) and Brent ($B_t$) crude oil prices "
        "(in USD/bbl) over $T = 250$ trading days.\n"
        r"- Modeling WTI directly as a random walk with drift: $W_t = 0.25 + W_{t-1} + \varepsilon_t$, "
        r"where $\sigma_\varepsilon = 1.50$ and $W_{250} = 72.00$." "\n"
        r"- Dickey-Fuller unit root regression on WTI: $\Delta W_t = 0.85 - 0.042\,W_{t-1} + \varepsilon_t$, "
        r"with $SE(\hat{g}_1) = 0.020$ ($5\%$ Dickey-Fuller critical value = $-2.89$)." "\n"
        r"- First-differenced AR(1) model on WTI: $\widehat{\Delta W}_{t+1} = 0.12 + 0.35\,\Delta W_t$, "
        r"with $W_{249} = 71.00$ and $W_{250} = 72.00$." "\n"
        "- Cointegration test: Regressing $B_t$ on $W_t$ gives $R^2 = 0.94, DW = 0.18$; applying the "
        r"Dickey-Fuller test to the residuals $\hat{e}_t$ yields $t = -3.85$ (5% Engle-Granger critical value = $-3.37$)."
    )
    q_l2(
        "L2-QM-V05-Q1", "LM 4", "Time-Series Analysis", "Covariance Stationarity Conditions",
        "QM-V05", v5_title, v5_text,
        "State and evaluate the conditions for covariance stationarity.", False,
        "Which condition is *not* required for a time series $y_t$ to be covariance stationary?",
        {
            "A": "The expected value of $y_t$ is constant and finite across all time periods $t$.",
            "B": "The variance of $y_t$ is constant and finite across all time periods $t$.",
            "C": r"The autocovariance $\text{Cov}(y_t, y_{t-s})$ must equal zero for all lags $s \ge 1$.",
        },
        "C",
        "Covariance stationarity requires constant finite mean, constant finite variance, and that autocovariance $\\text{Cov}(y_t, y_{t-s})$ depends only on lag $s$ (not on time $t$) — it need *not* be zero for $s \\ge 1$.",
        {
            "A": "Constant finite mean is one of the three defining requirements of covariance stationarity.",
            "B": "Constant finite variance is a core requirement of covariance stationarity (violated by random walks).",
        },
    )

    w_f3 = 72.00 + 3 * 0.25
    sd_f3 = math.sqrt(3.0) * 1.50
    q_l2(
        "L2-QM-V05-Q2", "LM 4", "Time-Series Analysis", "Random Walk with Drift Forecast",
        "QM-V05", v5_title, v5_text,
        "Forecast a random walk with drift and its multi-step forecast error standard deviation.", True,
        r"Under the random walk with drift model from $W_{250} = 72.00$, the 3-day-ahead point forecast $\hat{W}_{253}$ and 3-day forecast error standard deviation are *closest* to:",
        {
            "A": f"Forecast = USD {w_f3:.2f}, SD = USD {sd_f3:.2f}",
            "B": f"Forecast = USD {w_f3:.2f}, SD = USD {3*1.50:.2f}",
            "C": f"Forecast = USD {72.00+0.25:.2f}, SD = USD {sd_f3:.2f}",
        },
        "A",
        rf"For a random walk with drift $\hat{{W}}_{{t+h}} = W_t + h b_0 = 72.00 + 3(0.25) = \text{{USD }}{w_f3:.2f}$. Because independent shocks accumulate variance linearly over $h$ steps, $\text{{Var}}(e_h) = h\sigma^2$, giving $SD = \sqrt{{3}}(1.50) = \text{{USD }}{sd_f3:.2f}$.",
        {
            "B": rf"Scales standard deviation linearly by $h=3$ ({3*1.50:.2f}) instead of $\sqrt{{h}}$.",
            "C": "Adds only 1 period of drift rather than 3 periods.",
        },
    )

    df_t = -0.042 / 0.020
    q_l2(
        "L2-QM-V05-Q3", "LM 4", "Time-Series Analysis", "Dickey-Fuller Unit Root Test",
        "QM-V05", v5_title, v5_text,
        "Conduct and interpret a Dickey-Fuller unit root test.", True,
        "The Dickey-Fuller test statistic for $W_t$ and the conclusion regarding a unit root at the 5% level are *closest* to:",
        {
            "A": f"t = {df_t:.2f}; reject unit root (series is stationary)",
            "B": f"t = {df_t:.2f}; fail to reject unit root (series is non-stationary)",
            "C": f"t = {-df_t:.2f}; fail to reject unit root",
        },
        "B",
        rf"Testing $H_0: g_1 = 0$ yields $t = -0.042 / 0.020 = {df_t:.2f}$. Because ${df_t:.2f}$ is *not* more negative than the DF critical value $-2.89$, we fail to reject a unit root.",
        {
            "A": rf"Compares $|{df_t:.2f}| = 2.10$ against standard $t_{{0.025}} = 1.97$ instead of the Dickey-Fuller critical value $-2.89$.",
            "C": "Drops the negative sign on $\\hat{g}_1 = -0.042$.",
        },
    )

    dw_last = 72.00 - 71.00
    dw_hat_next = 0.12 + 0.35 * dw_last
    w_hat_next = 72.00 + dw_hat_next
    q_l2(
        "L2-QM-V05-Q4", "LM 4", "Time-Series Analysis", "First-Differenced AR(1) Forecast",
        "QM-V05", v5_title, v5_text,
        "Forecast level values from a first-differenced time-series model.", True,
        r"Using the first-differenced AR(1) model with $W_{249} = 71.00$ and $W_{250} = 72.00$, the predicted price $\hat{W}_{251}$ is *closest* to:",
        {"A": f"USD {dw_hat_next:.2f}", "B": f"USD {w_hat_next:.2f}", "C": f"USD {0.12 + 0.35*72.00:.2f}"},
        "B",
        rf"First difference is $\Delta W_{{250}} = 72.00 - 71.00 = 1.00$. Predicted change is $\widehat{{\Delta W}}_{{251}} = 0.12 + 0.35(1.00) = {dw_hat_next:.2f}$, so $\hat{{W}}_{{251}} = 72.00 + {dw_hat_next:.2f} = \text{{USD }}{w_hat_next:.2f}$.",
        {
            "A": rf"Reports the predicted price change $\widehat{{\Delta W}}_{{251}}$ ({dw_hat_next:.2f}) instead of the price level.",
            "C": rf"Inserts price level $72.00$ into the differenced equation ({0.12 + 0.35*72.00:.2f}).",
        },
    )

    q_l2(
        "L2-QM-V05-Q5", "LM 4", "Time-Series Analysis", "Spurious Regression Indicators",
        "QM-V05", v5_title, v5_text,
        "Diagnose spurious regression when regressing non-stationary time series.", False,
        "In the static levels regression of $B_t$ on $W_t$ ($R^2 = 0.94, DW = 0.18$), what would the high $R^2$ coupled with a near-zero Durbin-Watson statistic signal if the residuals were *not* stationary?",
        {
            "A": "Spurious regression, meaning OLS standard errors are invalid and the relationship may be illusory.",
            "B": "Structural cointegration guaranteeing long-run mean reversion.",
            "C": "Multicollinearity between $B_t$ and the error term.",
        },
        "A",
        "Regressing two independent random walks produces artificially high $R^2$ and extremely low Durbin-Watson ($DW \\ll 2$) because residuals retain unit roots — the classic signature of spurious regression unless cointegration is verified.",
        {
            "B": "Cointegration requires stationary residuals, not merely high $R^2$ and low DW.",
            "C": "Multicollinearity occurs among two or more explanatory variables, not in a univariate regression.",
        },
    )

    q_l2(
        "L2-QM-V05-Q6", "LM 4", "Time-Series Analysis", "Engle-Granger Cointegration",
        "QM-V05", v5_title, v5_text,
        "Interpret the Engle-Granger test for cointegration.", False,
        "Given the residual Dickey-Fuller test statistic of $t = -3.85$ against the 5% Engle-Granger critical value of $-3.37$, Cho should *most likely* conclude that WTI and Brent prices:",
        {
            "A": "Are not cointegrated because the residual $R^2$ is below 0.95.",
            "B": "Are cointegrated, meaning they share a common stochastic trend and an error-correction model can represent their long-run equilibrium.",
            "C": "Must be analyzed strictly via unrelated random walks with zero correlation.",
        },
        "B",
        "Since $t = -3.85 < -3.37$ (more negative than the Engle-Granger critical value), we reject the null of a unit root in the residuals: the series are cointegrated, validating regression analysis and error-correction modeling.",
        {
            "A": "Cointegration depends on residual stationarity via the Engle-Granger DF statistic, not an $R^2 > 0.95$ threshold.",
            "C": "Cointegrated series share a stable long-run equilibrium spread despite individual unit roots.",
        },
    )

    # -----------------------------------------------------------------------
    # QM-V06: Seasonality, ARCH(1) & GARCH(1,1) Volatility Forecasting
    # -----------------------------------------------------------------------
    v6_title = "Vignette 6: Quarterly Retail Seasonality and Conditional Volatility Modeling"
    v6_text = (
        r"Sonia Alvarez, CFA, models quarterly log sales growth ($g_t = \ln S_t - \ln S_{t-1}$) for a "
        "department store chain over $T = 60$ quarters:\n"
        "- **Seasonal AR Model:**\n"
        r"$$\hat{g}_t = 0.012 + 0.30\,g_{t-1} + 0.55\,g_{t-4}, \quad SE(b_2) = 0.11$$" "\n"
        r"Recent quarterly log growth observations: $g_{60} = 0.040$, $g_{57} = 0.080$." "\n"
        "- **ARCH(1) Model on Residuals:**\n"
        r"$$\hat{\varepsilon}_t^2 = 0.00018 + 0.38\,\hat{\varepsilon}_{t-1}^2, \quad SE(a_1) = 0.095$$" "\n"
        r"Most recent squared innovation: $\hat{\varepsilon}_{60} = 0.030$." "\n"
        "- **GARCH(1,1) Alternative on Equity Index Returns:**\n"
        r"$$\sigma_{t+1}^2 = 0.00004 + 0.12\,\varepsilon_t^2 + 0.80\,\sigma_t^2$$" "\n"
        r"with current shock $\varepsilon_t = 0.025$ and current conditional volatility $\sigma_t = 0.015$. "
        r"(5% two-tailed critical $t_{0.025, 55} = 2.004$.)"
    )
    g61 = 0.012 + 0.30 * 0.040 + 0.55 * 0.080
    g61_noseas = 0.012 + 0.30 * 0.040
    g61_wronglag = 0.012 + 0.30 * 0.080 + 0.55 * 0.040
    q_l2(
        "L2-QM-V06-Q1", "LM 4", "Time-Series Analysis", "Seasonal AR Forecasting",
        "QM-V06", v6_title, v6_text,
        "Forecast a time series incorporating a seasonal autoregressive lag.", True,
        r"Using the seasonal AR model, the predicted quarterly log sales growth for Quarter 61 ($\hat{g}_{61}$) is *closest* to:",
        {"A": f"{g61_noseas*100:.2f}%", "B": f"{g61*100:.2f}%", "C": f"{g61_wronglag*100:.2f}%"},
        "B",
        rf"Predicting $t = 61$ uses $g_{{60}} = 0.040$ and seasonal lag $g_{{61-4}} = g_{{57}} = 0.080$: $$\hat{{g}}_{{61}} = 0.012 + 0.30(0.040) + 0.55(0.080) = {g61:.4f} = {g61*100:.2f}\%$$",
        {
            "A": rf"Omits the seasonal lag $g_{{57}}$ ({g61_noseas*100:.2f}%).",
            "C": rf"Swaps $g_{{60}}$ and $g_{{57}}$ in the AR equation ({g61_wronglag*100:.2f}%).",
        },
    )

    t_seas = 0.55 / 0.11
    q_l2(
        "L2-QM-V06-Q2", "LM 4", "Time-Series Analysis", "Testing Seasonal Lag Significance",
        "QM-V06", v6_title, v6_text,
        "Test the statistical significance of a seasonal lag.", True,
        "The $t$-statistic for the seasonal lag coefficient $b_2$ is *closest* to:",
        {"A": "6.05", "B": "2.00", "C": f"{t_seas:.2f}"},
        "C",
        rf"The seasonal lag $t$-statistic is $t = \hat{{b}}_2 / SE(\hat{{b}}_2) = 0.55 / 0.11 = {t_seas:.2f}$, far exceeding $2.004$ and confirming strong fourth-quarter seasonality.",
        {
            "A": "Multiplies $0.55 / 0.11$ incorrectly or multiplies by $0.11$.",
            "B": "Reports the 5% critical value instead of the test statistic.",
        },
    )

    t_arch = 0.38 / 0.095
    q_l2(
        "L2-QM-V06-Q3", "LM 4", "Time-Series Analysis", "Testing for ARCH(1)",
        "QM-V06", v6_title, v6_text,
        "Test for autoregressive conditional heteroskedasticity (ARCH).", True,
        r"Based on the ARCH(1) residual regression, the $t$-statistic on $\hat{a}_1$ and conclusion at $\alpha = 5\%$ are *closest* to:",
        {
            "A": f"t = {t_arch:.2f}; ARCH(1) errors are present",
            "B": f"t = {t_arch:.2f}; errors are homoskedastic",
            "C": f"t = {0.00018/0.095:.2f}; no ARCH(1) errors",
        },
        "A",
        rf"$t = \hat{{a}}_1 / SE(\hat{{a}}_1) = 0.38 / 0.095 = {t_arch:.2f} > 2.004$. Rejecting $H_0: a_1 = 0$ confirms time-varying ARCH(1) volatility clustering.",
        {
            "B": rf"Computes $t = {t_arch:.2f}$ properly but fails to reject $H_0$ despite exceeding $2.004$.",
            "C": "Tests the intercept $a_0$ instead of the ARCH(1) lag coefficient $a_1$.",
        },
    )

    var_arch = 0.00018 + 0.38 * (0.030 ** 2)
    vol_arch = math.sqrt(var_arch)
    vol_arch_lin = 0.00018 + 0.38 * 0.030
    q_l2(
        "L2-QM-V06-Q4", "LM 4", "Time-Series Analysis", "ARCH(1) Variance Forecast",
        "QM-V06", v6_title, v6_text,
        "Forecast next-period conditional variance and volatility with ARCH(1).", True,
        r"Using the ARCH(1) equation and $\hat{\varepsilon}_{60} = 0.030$, the predicted conditional standard deviation (volatility) for Quarter 61 is *closest* to:",
        {"A": f"{var_arch*100:.4f}%", "B": f"{vol_arch*100:.2f}%", "C": f"{vol_arch_lin*100:.2f}%"},
        "B",
        rf"Conditional variance is $\hat{{\sigma}}_{{61}}^2 = 0.00018 + 0.38(0.030)^2 = {var_arch:.6f}$. Taking the square root gives conditional volatility $\hat{{\sigma}}_{{61}} = {vol_arch*100:.2f}\%$.",
        {
            "A": rf"Reports conditional variance scaled by 100 ({var_arch*100:.4f}%) without taking the square root.",
            "C": rf"Fails to square $\hat{{\varepsilon}}_{{60}}$ and omits the square root ({vol_arch_lin*100:.2f}%).",
        },
    )

    var_garch = 0.00004 + 0.12 * (0.025 ** 2) + 0.80 * (0.015 ** 2)
    vol_garch = math.sqrt(var_garch)
    var_lr = 0.00004 / (1.0 - 0.12 - 0.80)
    vol_lr = math.sqrt(var_lr)
    q_l2(
        "L2-QM-V06-Q5", "LM 4", "Time-Series Analysis", "GARCH(1,1) Conditional & Long-Run Volatility",
        "QM-V06", v6_title, v6_text,
        "Compute GARCH(1,1) conditional and unconditional volatility forecasts.", True,
        r"For the equity index GARCH(1,1) model, the next-day conditional volatility $\sigma_{t+1}$ and long-run unconditional volatility are *closest* to:",
        {
            "A": f"Conditional = {vol_garch*100:.2f}%, Unconditional = {vol_lr*100:.2f}%",
            "B": f"Conditional = {vol_lr*100:.2f}%, Unconditional = {vol_garch*100:.2f}%",
            "C": f"Conditional = {vol_garch*100:.2f}%, Unconditional = {math.sqrt(0.00004/0.92)*100:.2f}%",
        },
        "A",
        rf"$\sigma_{{t+1}}^2 = 0.00004 + 0.12(0.025)^2 + 0.80(0.015)^2 = {var_garch:.6f} \implies \sigma_{{t+1}} = {vol_garch*100:.2f}\%$. Long-run unconditional variance is $\frac{{\omega}}{{1 - \alpha - \beta}} = \frac{{0.00004}}{{0.08}} = {var_lr:.6f} \implies \sigma_{{LR}} = {vol_lr*100:.2f}\%$.",
        {
            "B": "Swaps next-day conditional volatility and long-run unconditional volatility.",
            "C": "Divides $\\omega$ by $\\alpha + \\beta = 0.92$ instead of $1 - \\alpha - \\beta = 0.08$.",
        },
    )

    q_l2(
        "L2-QM-V06-Q6", "LM 4", "Time-Series Analysis", "Remedying ARCH in Regression",
        "QM-V06", v6_title, v6_text,
        "Recommend econometric remedies when ARCH errors are detected.", False,
        "If significant ARCH(1) errors are confirmed in Alvarez's time-series regression, which consequence and remedy is *most accurate*?",
        {
            "A": "OLS standard errors are invalid for hypothesis testing; generalized least squares (GLS) or robust standard errors should be applied.",
            "B": "The AR slope estimates are severely biased upward and can only be corrected by first-differencing the dependent variable.",
            "C": "The model suffers from a unit root and must be abandoned in favor of a pure moving-average process.",
        },
        "A",
        "ARCH is a form of conditional heteroskedasticity: OLS coefficient estimates remain consistent, but standard errors are invalid unless adjusted using GLS (modeling the variance explicitly) or heteroskedasticity-robust standard errors.",
        {
            "B": "Conditional heteroskedasticity invalidates standard errors rather than creating systematic slope bias or requiring differencing.",
            "C": "ARCH captures volatility clustering, not a unit root in the level mean.",
        },
    )

    # -----------------------------------------------------------------------
    # QM-V07: Backtesting & Investment Simulation
    # -----------------------------------------------------------------------
    v7_title = "Vignette 7: Quantitative Strategy Backtesting and Correlated Stress Simulation"
    v7_text = (
        "Liam O'Connor, CFA, oversees model validation for a multi-asset systematic strategy.\n"
        "- **Historical Backtest Summary (10-year rolling window):** Gross annualized return = $11.40\\%$, "
        "annualized volatility = $12.00\\%$, risk-free rate = $3.00\\%$, annualized one-way turnover = $180\\%$ "
        "with round-trip trading cost equivalent to $50$ bps per $100\\%$ turnover (i.e., $0.50\\%$ per $100\\%$ annual turnover).\n"
        "- **95% Daily VaR Backtest ($T = 250$ trading days):** Expected exceptions = $12.5$; observed exceptions = $21$.\n"
        "- **Monte Carlo Correlated Draw (2 assets):** Target correlation $\\rho = 0.60$. Two independent standard "
        "normal draws are $Z_1 = +1.50$ and $Z_2 = -0.50$.\n"
        "- **Factor Stress Scenario:** Portfolio weights $60\\%$ Equity ($\\text{beta} = 1.15$) and $40\\%$ IG Credit "
        "($\\text{duration} = 6.5$ years). Scenario applies a $-12.0\\%$ equity market shock and $+150$ bps credit spread widening."
    )
    q_l2(
        "L2-QM-V07-Q1", "LM 7", "Backtesting and Simulation", "Rolling vs Expanding Windows",
        "QM-V07", v7_title, v7_text,
        "Compare rolling-window and expanding-window backtesting.", False,
        "Why might O'Connor prefer a *rolling-window* backtest over an *expanding-window* backtest when structural market regimes shift over time?",
        {
            "A": "A rolling window discards stale early observations so parameter estimates adapt faster to recent regime shifts.",
            "B": "A rolling window maximizes statistical power by retaining all historical observations back to inception.",
            "C": "A rolling window eliminates the need to adjust returns for transaction costs or survivorship bias.",
        },
        "A",
        "Rolling windows drop older observations as the estimation window advances, reducing sensitivity to structural breaks and obsolete regimes at the expense of slightly higher parameter variance.",
        {
            "B": "Retaining all historical observations from inception describes an *expanding* window.",
            "C": "Transaction costs and survivorship bias must be controlled regardless of whether rolling or expanding windows are used.",
        },
    )

    tc_drag = 1.80 * 0.50  # 0.90%
    net_ret = 11.40 - tc_drag
    net_sharpe = (net_ret - 3.00) / 12.00
    gross_sharpe = (11.40 - 3.00) / 12.00
    q_l2(
        "L2-QM-V07-Q2", "LM 7", "Backtesting and Simulation", "Net Backtest Sharpe Ratio",
        "QM-V07", v7_title, v7_text,
        "Calculate backtest net return and Sharpe ratio after transaction costs.", True,
        "Accounting for trading costs, the strategy's net annualized return and net Sharpe ratio are *closest* to:",
        {
            "A": f"Net Return = {net_ret:.2f}%, Sharpe = {gross_sharpe:.3f}",
            "B": f"Net Return = {net_ret:.2f}%, Sharpe = {net_sharpe:.3f}",
            "C": f"Net Return = {11.40 - 0.50:.2f}%, Sharpe = {(11.40 - 0.50 - 3.00)/12.00:.3f}",
        },
        "B",
        rf"Annual transaction cost drag is $1.80 \times 0.50\% = {tc_drag:.2f}\%$, reducing net return to $11.40\% - 0.90\% = {net_ret:.2f}\%$. Net Sharpe ratio is $$\frac{{{net_ret:.2f}\% - 3.00\%}}{{12.00\%}} = {net_sharpe:.3f}$$",
        {
            "A": rf"Reports the gross Sharpe ratio ({gross_sharpe:.3f}) without subtracting trading costs.",
            "C": "Deducts only 50 bps flat instead of scaling by 180% annual turnover.",
        },
    )

    p_var = 0.05
    t_var = 250
    exp_exc = t_var * p_var
    obs_exc = 21
    sd_exc = math.sqrt(t_var * p_var * (1.0 - p_var))
    z_var = (obs_exc - exp_exc) / sd_exc
    z_var_nosd = (obs_exc - exp_exc) / exp_exc
    q_l2(
        "L2-QM-V07-Q3", "LM 7", "Backtesting and Simulation", "VaR Exception Binomial Test",
        "QM-V07", v7_title, v7_text,
        "Evaluate Value at Risk backtesting exception counts.", True,
        "Using the normal approximation to the binomial exception count, the $z$-statistic for testing whether the true VaR violation rate equals 5% is *closest* to (two-tailed 5% critical $z = 1.96$):",
        {
            "A": f"z = {z_var:.2f}; reject model accuracy",
            "B": f"z = {z_var:.2f}; fail to reject model accuracy",
            "C": f"z = {z_var_nosd:.2f}; fail to reject model accuracy",
        },
        "A",
        rf"Expected breaches are $np = 12.5$ with binomial SD $\sqrt{{250(0.05)(0.95)}} = {sd_exc:.3f}$. Thus $z = (21 - 12.5)/{sd_exc:.3f} = {z_var:.2f} > 1.96$, rejecting the 5% VaR calibration.",
        {
            "B": rf"Computes $z = {z_var:.2f}$ accurately but fails to reject at $1.96$.",
            "C": rf"Divides by expected count 12.5 instead of binomial standard deviation ({z_var_nosd:.2f}).",
        },
    )

    z1_c, z2_c, rho_c = 1.50, -0.50, 0.60
    z2_corr = rho_c * z1_c + math.sqrt(1.0 - rho_c ** 2) * z2_c
    z2_nort = rho_c * z1_c + (1.0 - rho_c) * z2_c
    q_l2(
        "L2-QM-V07-Q4", "LM 7", "Backtesting and Simulation", "Cholesky Correlated Normal Draws",
        "QM-V07", v7_title, v7_text,
        "Generate correlated normal random variables in Monte Carlo simulation.", True,
        "Applying the Cholesky transformation to $Z_1 = +1.50$ and $Z_2 = -0.50$ with correlation $\\rho = 0.60$, the correlated shock $Z_2^*$ for Asset 2 is *closest* to:",
        {"A": f"{z2_nort:.2f}", "B": f"{rho_c * z1_c:.2f}", "C": f"{z2_corr:.2f}"},
        "C",
        rf"Using Cholesky decomposition: $$Z_2^* = \rho Z_1 + \sqrt{{1 - \rho^2}}\, Z_2 = 0.60(1.50) + \sqrt{{1 - 0.36}}(-0.50) = 0.90 - 0.40 = {z2_corr:.2f}$$",
        {
            "A": rf"Uses $(1 - \rho)$ instead of $\sqrt{{1 - \rho^2}}$ ({z2_nort:.2f}).",
            "B": rf"Omits the idiosyncratic component $\sqrt{{1 - \rho^2}} Z_2$ ({rho_c * z1_c:.2f}).",
        },
    )

    eq_loss = 0.60 * (1.15 * (-0.12))
    cr_loss = 0.40 * (-6.5 * 0.015)
    tot_loss = eq_loss + cr_loss
    tot_nobeta = 0.60 * (-0.12) + cr_loss
    q_l2(
        "L2-QM-V07-Q5", "LM 7", "Backtesting and Simulation", "Multi-Factor Stress Impact",
        "QM-V07", v7_title, v7_text,
        "Calculate portfolio drawdown under multi-factor stress testing.", True,
        "Under the specified factor stress scenario, the approximate first-order portfolio return is *closest* to:",
        {"A": f"{tot_nobeta*100:.2f}%", "B": f"{tot_loss*100:.2f}%", "C": f"{(eq_loss - cr_loss)*100:.2f}%"},
        "B",
        rf"Equity contribution is $0.60 \times 1.15 \times (-12.0\%) = {eq_loss*100:.2f}\%$. Credit contribution is $0.40 \times (-6.5 \times 1.50\%) = {cr_loss*100:.2f}\%$. Total portfolio shock is ${eq_loss*100:.2f}\% + ({cr_loss*100:.2f}\%) = {tot_loss*100:.2f}\%$.",
        {
            "A": rf"Ignores the equity beta of 1.15 ({tot_nobeta*100:.2f}%).",
            "C": rf"Adds the duration shock as positive rather than negative ({(eq_loss - cr_loss)*100:.2f}%).",
        },
    )

    q_l2(
        "L2-QM-V07-Q6", "LM 7", "Backtesting and Simulation", "Bootstrapped & Heavy-Tail Simulation",
        "QM-V07", v7_title, v7_text,
        "Assess limitations of multivariate normal simulation in backtesting.", False,
        "O'Connor observes that actual strategy drawdowns during crisis episodes far exceed those predicted by his Gaussian Monte Carlo simulator. Which modeling change *best* addresses tail co-movement?",
        {
            "A": "Sampling joint returns via historical bootstrapping or a fat-tailed Student's $t$ copula.",
            "B": "Halving the number of simulation trials from 10,000 to 5,000.",
            "C": "Replacing daily return inputs with 5-year moving averages.",
        },
        "A",
        "Multivariate normal simulations understate tail kurtosis and crisis correlation spikes; historical block bootstrapping or Student's $t$ distributions/copulas capture empirical fat tails and tail dependence.",
        {
            "B": "Reducing Monte Carlo paths increases Monte Carlo sampling error without fixing Gaussian thin tails.",
            "C": "Smoothing inputs with long moving averages artificially suppresses volatility and tail risk.",
        },
    )

    # -----------------------------------------------------------------------
    # QM-V08: Supervised ML: Penalized Regression & Classification
    # -----------------------------------------------------------------------
    v8_title = "Vignette 8: Penalized Factor Selection and Credit Default Classification"
    v8_text = (
        "Mei Lin, CFA, develops supervised machine learning models for corporate credit evaluation.\n"
        "- **Penalized Regression Comparison:** On standardized training data, a model with $K = 3$ predictors "
        "yields $\\text{SSE} = 42.0$, penalty hyperparameter $\\lambda = 2.0$, and slope estimates "
        r"$\hat{b}_1 = 1.50$, $\hat{b}_2 = -0.80$, $\hat{b}_3 = 0.20$." "\n"
        "- **Test-Set Confusion Matrix ($N = 400$ corporate bonds):**\n"
        "  - Actual Default ($+$): Predicted Default ($TP$) = $72$, Predicted Non-Default ($FN$) = $28$.\n"
        "  - Actual Non-Default ($-$): Predicted Default ($FP$) = $18$, Predicted Non-Default ($TN$) = $282$.\n"
        "- **Cost-Benefit Payoffs:** Flagging a true default ($TP$) avoids USD 40,000 loss; a false alarm ($FP$) costs "
        "USD 4,000 in review expense; missing a default ($FN$) incurs USD 50,000 net loss (relative to $TN = \\text{USD } 0$).\n"
        "- **Random Forest Ensemble:** $B = 10$ decision trees, each with prediction variance $\\sigma^2 = 0.25$ and "
        "pairwise tree error correlation $\\rho = 0.20$."
    )
    ridge_obj = 42.0 + 2.0 * (1.50 ** 2 + (-0.80) ** 2 + 0.20 ** 2)
    lasso_obj = 42.0 + 2.0 * (abs(1.50) + abs(-0.80) + abs(0.20))
    ridge_no_lam = 42.0 + (1.50 ** 2 + (-0.80) ** 2 + 0.20 ** 2)
    q_l2(
        "L2-QM-V08-Q1", "LM 5", "Machine Learning", "Ridge vs LASSO Loss Objective",
        "QM-V08", v8_title, v8_text,
        "Calculate the penalized objective function for Ridge and LASSO regression.", True,
        r"Evaluating the penalized objective at the given $\hat{b}_k$ coefficients, the Ridge ($L_2$) and LASSO ($L_1$) total loss values are *closest* to:",
        {
            "A": f"Ridge = {lasso_obj:.2f}, LASSO = {ridge_obj:.2f}",
            "B": f"Ridge = {ridge_obj:.2f}, LASSO = {lasso_obj:.2f}",
            "C": f"Ridge = {ridge_no_lam:.2f}, LASSO = {lasso_obj:.2f}",
        },
        "B",
        rf"Ridge ($L_2$) loss is $\text{{SSE}} + \lambda \sum \hat{{b}}_k^2 = 42.0 + 2.0(2.25 + 0.64 + 0.04) = {ridge_obj:.2f}$. LASSO ($L_1$) loss is $\text{{SSE}} + \lambda \sum |\hat{{b}}_k| = 42.0 + 2.0(1.50 + 0.80 + 0.20) = {lasso_obj:.2f}$.",
        {
            "A": "Swaps the Ridge ($L_2$) and LASSO ($L_1$) penalty values.",
            "C": rf"Omits $\lambda = 2.0$ from the Ridge penalty term ({ridge_no_lam:.2f}).",
        },
    )

    q_l2(
        "L2-QM-V08-Q2", "LM 5", "Machine Learning", "LASSO Sparsity & Cross-Validation",
        "QM-V08", v8_title, v8_text,
        "Contrast feature selection properties of LASSO vs Ridge regression.", False,
        "As Lin increases the regularization hyperparameter $\\lambda$ tuned via $K$-fold cross-validation, how does LASSO differ *most distinctively* from Ridge regression?",
        {
            "A": "LASSO sets smaller slope coefficients exactly to zero, performing automatic feature selection.",
            "B": "Ridge eliminates weak predictors completely while leaving large coefficients unpenalized.",
            "C": "Increasing $\\lambda$ lowers bias and increases variance in both LASSO and Ridge.",
        },
        "A",
        "The $L_1$ absolute-value penalty in LASSO shrinks small coefficients all the way to exactly zero (sparse models), whereas Ridge's quadratic $L_2$ penalty shrinks coefficients asymptotically toward zero without setting them exactly to zero.",
        {
            "B": "Describes LASSO's sparsity, whereas Ridge retains all predictors with non-zero shrunk weights.",
            "C": "Increasing $\\lambda$ shrinks model flexibility, which *increases* bias and *reduces* variance.",
        },
    )

    tp8, fp8, fn8, tn8 = 72, 18, 28, 282
    acc8 = (tp8 + tn8) / 400.0
    prec8 = tp8 / (tp8 + fp8)
    rec8 = tp8 / (tp8 + fn8)
    q_l2(
        "L2-QM-V08-Q3", "LM 5", "Machine Learning", "Confusion Matrix Accuracy & Precision",
        "QM-V08", v8_title, v8_text,
        "Compute accuracy and precision from a test-set confusion matrix.", True,
        "For the bond default classifier, overall test accuracy and precision are *closest* to:",
        {
            "A": f"Accuracy = {acc8*100:.1f}%, Precision = {rec8*100:.1f}%",
            "B": f"Accuracy = {prec8*100:.1f}%, Precision = {acc8*100:.1f}%",
            "C": f"Accuracy = {acc8*100:.1f}%, Precision = {prec8*100:.1f}%",
        },
        "C",
        rf"Accuracy is $(72 + 282)/400 = {acc8*100:.1f}\%$. Precision is $TP/(TP + FP) = 72/(72 + 18) = {prec8*100:.1f}\%$.",
        {
            "A": rf"Confuses Precision with Recall ({rec8*100:.1f}%).",
            "B": "Swaps Accuracy and Precision.",
        },
    )

    fpr8 = fp8 / (fp8 + tn8)
    f1_8 = 2.0 * prec8 * rec8 / (prec8 + rec8)
    q_l2(
        "L2-QM-V08-Q4", "LM 5", "Machine Learning", "Recall, FPR, and F1 Score",
        "QM-V08", v8_title, v8_text,
        "Compute recall, false positive rate, and F1 score.", True,
        "The classifier's Recall (true positive rate), False Positive Rate (FPR), and $F_1$ score are *closest* to:",
        {
            "A": f"Recall = {rec8*100:.1f}%, FPR = {fpr8*100:.1f}%, F1 = {f1_8*100:.1f}%",
            "B": f"Recall = {prec8*100:.1f}%, FPR = {fpr8*100:.1f}%, F1 = {0.5*(prec8+rec8)*100:.1f}%",
            "C": f"Recall = {rec8*100:.1f}%, FPR = {(1-rec8)*100:.1f}%, F1 = {f1_8*100:.1f}%",
        },
        "A",
        rf"Recall $= 72/(72+28) = {rec8*100:.1f}\%$. $\text{{FPR}} = FP/(FP+TN) = 18/300 = {fpr8*100:.1f}\%$. Harmonic mean $F_1 = \frac{{2(0.80)(0.72)}}{{0.80 + 0.72}} = {f1_8*100:.1f}\%$.",
        {
            "B": "Uses Precision for Recall and arithmetic average for F1 instead of harmonic mean.",
            "C": r"Confuses FPR with False Negative Rate ($1 - \text{Recall} = 28.0\%$).",
        },
    )

    net_payoff = tp8 * 40000 - fp8 * 4000 - fn8 * 50000
    no_fp_payoff = tp8 * 40000 - fn8 * 50000
    gross_avoided = tp8 * 40000
    q_l2(
        "L2-QM-V08-Q5", "LM 5", "Machine Learning", "Cost-Weighted Classification Value",
        "QM-V08", v8_title, v8_text,
        "Evaluate expected dollar value of classification decisions.", True,
        "Across the 400 test-set bonds, the net dollar impact of deploying Lin's classifier (vs. USD 0 for true negatives) is *closest* to:",
        {
            "A": f"USD {net_payoff:,.0f}",
            "B": f"USD {no_fp_payoff:,.0f}",
            "C": f"USD {gross_avoided:,.0f}",
        },
        "A",
        rf"Net impact $= 72(40,000) - 18(4,000) - 28(50,000) = 2,880,000 - 72,000 - 1,400,000 = \text{{USD }}{net_payoff:,.0f}$.",
        {
            "B": rf"Omits the review cost of the 18 false positives (USD {no_fp_payoff:,.0f}).",
            "C": rf"Reports gross savings from true positives only without deducting FP or FN losses (USD {gross_avoided:,.0f}).",
        },
    )

    rho_rf, sig2_rf, b_rf = 0.20, 0.25, 10
    var_rf = rho_rf * sig2_rf + ((1.0 - rho_rf) / b_rf) * sig2_rf
    var_rf_uncorr = sig2_rf / b_rf
    q_l2(
        "L2-QM-V08-Q6", "LM 5", "Machine Learning", "Random Forest Variance Reduction",
        "QM-V08", v8_title, v8_text,
        "Calculate ensemble variance reduction in bagging / random forests.", True,
        r"For the $B = 10$ decision trees ($\sigma^2 = 0.25, \rho = 0.20$), the variance of the Random Forest averaged prediction is *closest* to:",
        {"A": f"{var_rf_uncorr:.3f}", "B": f"{var_rf:.3f}", "C": f"{sig2_rf:.3f}"},
        "B",
        rf"Ensemble prediction variance is $$\text{{Var}} = \rho\sigma^2 + \frac{{1-\rho}}{{B}}\sigma^2 = 0.20(0.25) + \frac{{0.80}}{{10}}(0.25) = 0.050 + 0.020 = {var_rf:.3f}$$",
        {
            "A": rf"Assumes trees are completely uncorrelated ($\rho = 0$, giving $\sigma^2/10 = {var_rf_uncorr:.3f}$).",
            "C": rf"Reports single-tree variance ({sig2_rf:.3f}) without ensemble averaging.",
        },
    )

    # -----------------------------------------------------------------------
    # QM-V09: Unsupervised ML, Neural Networks & Governance
    # -----------------------------------------------------------------------
    v9_title = "Vignette 9: Unsupervised Equity Clustering, PCA, and Deep Learning Governance"
    v9_text = (
        "Tariq Al-Mansoor, CFA, applies dimensionality reduction, clustering, and neural networks to "
        "a universe of global industrial equities.\n"
        "- **Principal Components Analysis (PCA) on 5 standardized valuation ratios:** Eigenvalues are "
        "$\\lambda_1 = 2.45$, $\\lambda_2 = 1.35$, $\\lambda_3 = 0.65$, $\\lambda_4 = 0.35$, $\\lambda_5 = 0.20$ (total = $5.00$).\n"
        "- **K-Means Clustering (standardized features: Valuation $X_1$, Quality $X_2$):**\n"
        "  - Centroid A = $(10.0, 15.0)$, Centroid B = $(20.0, 12.0)$.\n"
        "  - New target stock $S$ has coordinates $(X_1 = 14.0, X_2 = 18.0)$.\n"
        "- **Feedforward Neural Network (1 hidden neuron, ReLU activation $f(z) = \\max(0, z)$):**\n"
        "  - Inputs $x_1 = 2.0, x_2 = -1.0$; hidden weights $w_1 = 0.80, w_2 = -0.40$, hidden bias $b_h = 0.20$.\n"
        "  - Linear output weight $v_1 = 1.50$, output bias $b_o = -0.30$.\n"
        "- **Ensemble Classifier:** Combines 3 independent weak binary classifiers, each having $70\\%$ accuracy, via majority vote."
    )
    eigs = [2.45, 1.35, 0.65, 0.35, 0.20]
    cum2 = sum(eigs[:2]) / sum(eigs)
    cum3 = sum(eigs[:3]) / sum(eigs)
    q_l2(
        "L2-QM-V09-Q1", "LM 5", "Machine Learning", "PCA Variance Explained",
        "QM-V09", v9_title, v9_text,
        "Determine the number of principal components needed to capture target variance.", True,
        "What is the cumulative proportion of total variance explained by the first two components, and the minimum number of components needed to exceed 85% variance explained?",
        {
            "A": f"{cum2*100:.1f}%; 3 components ({cum3*100:.1f}%)",
            "B": f"{cum2*100:.1f}%; 2 components",
            "C": f"{eigs[0]/5.0*100:.1f}%; 4 components",
        },
        "A",
        rf"First two components capture $(2.45 + 1.35)/5.00 = {cum2*100:.1f}\%$ ($<85\%$). Adding PC3 brings cumulative variance to $(2.45 + 1.35 + 0.65)/5.00 = {cum3*100:.1f}\% \ge 85\%$, so 3 components are required.",
        {
            "B": rf"2 components explain only {cum2*100:.1f}%, falling short of the 85% threshold.",
            "C": "Uses only PC1 (49.0%) or retains an extra component beyond what is needed.",
        },
    )

    d_a = math.sqrt((14.0 - 10.0) ** 2 + (18.0 - 15.0) ** 2)
    d_b = math.sqrt((14.0 - 20.0) ** 2 + (18.0 - 12.0) ** 2)
    q_l2(
        "L2-QM-V09-Q2", "LM 5", "Machine Learning", "K-Means Centroid Assignment",
        "QM-V09", v9_title, v9_text,
        "Assign observations to K-means clusters using Euclidean distance.", True,
        "Target stock $S(14.0, 18.0)$ is assigned to which cluster, and what is its Euclidean distance to that centroid?",
        {
            "A": f"Cluster B, distance = {d_b:.2f}",
            "B": f"Cluster A, distance = {d_a:.2f}",
            "C": f"Cluster A, distance = {abs(14-10)+abs(18-15):.2f}",
        },
        "B",
        rf"Distance to Centroid A is $\sqrt{{(14-10)^2 + (18-15)^2}} = \sqrt{{16 + 9}} = {d_a:.2f}$. Distance to Centroid B is $\sqrt{{(14-20)^2 + (18-12)^2}} = \sqrt{{72}} = {d_b:.2f}$. Stock $S$ is assigned to nearer Centroid A.",
        {
            "A": rf"Assigns to Cluster B ({d_b:.2f}), which is farther away than Cluster A ({d_a:.2f}).",
            "C": "Computes Manhattan ($L_1$) distance ($4 + 3 = 7.00$) instead of Euclidean ($L_2$) distance.",
        },
    )

    zh = 0.80 * 2.0 + (-0.40) * (-1.0) + 0.20
    ah = max(0.0, zh)
    yhat_nn = 1.50 * ah - 0.30
    yhat_nn_wrongsign = 1.50 * max(0.0, 0.80 * 2.0 - 0.40 * 1.0 + 0.20) - 0.30
    q_l2(
        "L2-QM-V09-Q3", "LM 5", "Machine Learning", "Neural Network Forward Pass",
        "QM-V09", v9_title, v9_text,
        "Compute the output of a feedforward neural network with ReLU activation.", True,
        r"For inputs $(x_1 = 2.0, x_2 = -1.0)$, the neural network's output prediction $\hat{y}$ is *closest* to:",
        {"A": f"{ah:.2f}", "B": f"{yhat_nn_wrongsign:.2f}", "C": f"{yhat_nn:.2f}"},
        "C",
        rf"Hidden summation is $z_h = 0.80(2.0) + (-0.40)(-1.0) + 0.20 = {zh:.2f}$. ReLU activation gives $a_h = \max(0, {zh:.2f}) = {ah:.2f}$. Output is $\hat{{y}} = 1.50({ah:.2f}) - 0.30 = {yhat_nn:.2f}$.",
        {
            "A": rf"Reports the hidden-layer activation ({ah:.2f}) without applying output weights and bias.",
            "B": rf"Drops the double negative in $(-0.40)(-1.0)$ ({yhat_nn_wrongsign:.2f}).",
        },
    )

    p_ens = 0.70
    acc_ens = (p_ens ** 3) + 3.0 * (p_ens ** 2) * (1.0 - p_ens)
    q_l2(
        "L2-QM-V09-Q4", "LM 5", "Machine Learning", "Ensemble Majority Voting Accuracy",
        "QM-V09", v9_title, v9_text,
        "Calculate accuracy improvement from majority voting across independent classifiers.", True,
        "Using majority voting across the 3 independent 70%-accurate weak classifiers, the ensemble classification accuracy is *closest* to:",
        {"A": f"{acc_ens*100:.1f}%", "B": "70.0%", "C": f"{(p_ens**3)*100:.1f}%"},
        "A",
        rf"Majority vote succeeds when 2 or 3 classifiers are right: $$P(\ge 2) = (0.70)^3 + \binom{{3}}{{2}}(0.70)^2(0.30) = 0.343 + 0.441 = {acc_ens*100:.1f}\%$$",
        {
            "B": "Assumes ensemble voting provides zero accuracy gain over an individual weak learner.",
            "C": rf"Computes only the probability that all 3 agree correctly ({(p_ens**3)*100:.1f}%).",
        },
    )

    q_l2(
        "L2-QM-V09-Q5", "LM 5", "Machine Learning", "Clustering Diagnostics",
        "QM-V09", v9_title, v9_text,
        "Compare K-means and hierarchical clustering diagnostics.", False,
        "When evaluating the appropriate number of clusters $K$ in K-means versus hierarchical agglomerative clustering, which statement is *most likely* correct?",
        {
            "A": "K-means requires pre-specifying $K$ (often guided by an elbow or silhouette plot), whereas agglomerative clustering builds a complete dendrogram hierarchy without pre-fixing $K$.",
            "B": "K-means automatically determines optimal $K$ via eigenvalues exceeding 1.0.",
            "C": "Hierarchical clustering can only operate on binary categorical data.",
        },
        "A",
        "K-means requires choosing $K$ upfront (evaluated via within-cluster sum-of-squares elbow curves or silhouette scores), whereas agglomerative hierarchical clustering iteratively merges clusters into a dendrogram that can be cut at any desired level.",
        {
            "B": "Eigenvalues $> 1.0$ (Kaiser criterion) apply to PCA component selection, not K-means.",
            "C": "Hierarchical clustering works on any distance metric over continuous or mixed features.",
        },
    )

    q_l2(
        "L2-QM-V09-Q6", "LM 5", "Machine Learning", "Data Leakage & Model Governance",
        "QM-V09", v9_title, v9_text,
        "Prevent data leakage in machine learning pipelines.", False,
        "Al-Mansoor standardizes his features using the full dataset's mean and standard deviation *before* splitting the data into training, validation, and test folds. What governance flaw does this introduce?",
        {
            "A": "Data leakage, inflating apparent validation and test performance because test-set distributional statistics leaked into training preprocessing.",
            "B": "Severe underfitting due to insufficient training sample size.",
            "C": "Perfect multicollinearity across orthogonal PCA components.",
        },
        "A",
        "Feature scaling parameters (means, standard deviations, or PCA eigenvectors) must be fit *only* on the training fold and then applied to validation/test folds; scaling on the full dataset leaks out-of-sample test information.",
        {
            "B": "Data leakage artificially *inflates* (optimistically biases) out-of-sample accuracy rather than causing underfitting.",
            "C": "Standardizing features before splitting does not create multicollinearity across PCA components.",
        },
    )

    # -----------------------------------------------------------------------
    # QM-V10: Big Data Projects, NLP & Text Analytics
    # -----------------------------------------------------------------------
    v10_title = "Vignette 10: Earnings Call NLP Pipeline and Sentiment Factor Extraction"
    v10_text = (
        "Claire Dubois, CFA, leads a Big Data NLP initiative analyzing 10-K filings and quarterly earnings "
        "call transcripts across $N = 1,000$ corporate issuers.\n"
        "- **Document-Term Matrix (DTM):** Built across $N = 1,000$ filings and $V = 4,000$ unique lemmatized "
        "tokens, containing $140,000$ non-zero entries.\n"
        "- **TF-IDF Scoring:** Defined as $\\text{TF} = \\text{term count} / \\text{doc word count}$ and "
        "$\\text{IDF} = \\ln(N / \\text{df})$. In Filing #42 (300 words total), the token `headwind` appears "
        "$6$ times; across the 1,000-filing corpus, `headwind` appears in $\\text{df} = 50$ filings.\n"
        "- **Cosine Similarity:** Over a 3-token sub-vocabulary (`margin`, `headwind`, `guidance`), Filing A's "
        "TF-IDF vector is $v_A = (3, 4, 0)$ and Filing B's vector is $v_B = (0, 3, 4)$.\n"
        "- **Lexicon Sentiment Scoring:** Filing #42 contains $36$ positive-tone tokens and $12$ negative-tone tokens."
    )
    cells10 = 1000 * 4000
    nz10 = 140000
    spar10 = (cells10 - nz10) / cells10
    dens10 = nz10 / cells10
    q_l2(
        "L2-QM-V10-Q1", "LM 6", "Big Data Projects", "DTM Sparsity Calculation",
        "QM-V10", v10_title, v10_text,
        "Measure sparsity in text document-term matrices.", True,
        "The sparsity of Dubois's document-term matrix is *closest* to:",
        {"A": f"{dens10*100:.1f}%", "B": f"{spar10*100:.1f}%", "C": "99.5%"},
        "B",
        rf"Total cells are $1,000 \times 4,000 = 4,000,000$. Zero entries are $4,000,000 - 140,000 = 3,860,000$, giving sparsity $= 3,860,000 / 4,000,000 = {spar10*100:.1f}\%$.",
        {
            "A": rf"Reports matrix density ({dens10*100:.1f}%) instead of sparsity.",
            "C": "Overstates sparsity by an order of magnitude.",
        },
    )

    tf10 = 6.0 / 300.0
    idf10 = math.log(1000.0 / 50.0)
    tfidf10 = tf10 * idf10
    tfidf_raw = 6.0 * idf10
    tfidf_no_log = tf10 * (1000.0 / 50.0)
    q_l2(
        "L2-QM-V10-Q2", "LM 6", "Big Data Projects", "TF-IDF Computation",
        "QM-V10", v10_title, v10_text,
        "Calculate TF, IDF, and TF-IDF weights in text analytics.", True,
        "The TF-IDF score for the token `headwind` in Filing #42 is *closest* to:",
        {"A": f"{tfidf_no_log:.4f}", "B": f"{tfidf_raw:.4f}", "C": f"{tfidf10:.4f}"},
        "C",
        rf"$\text{{TF}} = 6/300 = {tf10:.3f}$ and $\text{{IDF}} = \ln(1000/50) = \ln(20) = {idf10:.4f}$. Thus $\text{{TF-IDF}} = 0.02 \times {idf10:.4f} = {tfidf10:.4f}$.",
        {
            "A": rf"Omits the natural logarithm in IDF ($0.02 \times 20 = {tfidf_no_log:.4f}$).",
            "B": rf"Uses raw term count 6 instead of relative TF $6/300$ ({tfidf_raw:.4f}).",
        },
    )

    va = [3.0, 4.0, 0.0]
    vb = [0.0, 3.0, 4.0]
    dot_ab = sum(x * y for x, y in zip(va, vb))
    na = math.sqrt(sum(x * x for x in va))
    nb = math.sqrt(sum(y * y for y in vb))
    cos_ab = dot_ab / (na * nb)
    q_l2(
        "L2-QM-V10-Q3", "LM 6", "Big Data Projects", "Cosine Similarity",
        "QM-V10", v10_title, v10_text,
        "Calculate cosine similarity between document vectors.", True,
        "The cosine similarity between Filing A ($v_A = (3, 4, 0)$) and Filing B ($v_B = (0, 3, 4)$) is *closest* to:",
        {"A": f"{cos_ab:.2f}", "B": f"{dot_ab:.2f}", "C": f"{dot_ab/(na*na + nb*nb):.2f}"},
        "A",
        rf"Dot product is $3(0) + 4(3) + 0(4) = 12$. Vector norms are $\|v_A\| = 5$ and $\|v_B\| = 5$, yielding $$\cos(\theta) = \frac{{12}}{{5 \times 5}} = {cos_ab:.2f}$$",
        {
            "B": "Reports the unnormalized dot product (12.00) instead of normalizing by vector magnitudes.",
            "C": "Divides by the sum of squared norms ($25 + 25 = 50$) rather than the product of norms ($5 \\times 5 = 25$).",
        },
    )

    pos10, neg10 = 36, 12
    net_sent = (pos10 - neg10) / (pos10 + neg10)
    sent_tot_ratio = (pos10 - neg10) / 300.0
    pos_share = pos10 / (pos10 + neg10)
    q_l2(
        "L2-QM-V10-Q4", "LM 6", "Big Data Projects", "Net Sentiment Ratio",
        "QM-V10", v10_title, v10_text,
        "Compute lexicon-based sentiment indices from financial text.", True,
        "Using the standard net sentiment score $(\\text{Pos} - \\text{Neg})/(\\text{Pos} + \\text{Neg})$, Filing #42's net sentiment score is *closest* to:",
        {"A": f"{pos_share:.2f}", "B": f"{net_sent:.2f}", "C": f"{sent_tot_ratio:.2f}"},
        "B",
        rf"Net sentiment index is $$\frac{{36 - 12}}{{36 + 12}} = \frac{{24}}{{48}} = {net_sent:.2f}$$",
        {
            "A": rf"Reports positive share $36/48 = {pos_share:.2f}$ without subtracting negative tokens.",
            "C": rf"Divides net count by total document length 300 ({sent_tot_ratio:.2f}) rather than total sentiment tokens.",
        },
    )

    q_l2(
        "L2-QM-V10-Q5", "LM 6", "Big Data Projects", "Text Cleansing & Lemmatization",
        "QM-V10", v10_title, v10_text,
        "Contrast text cleansing steps including stemming and lemmatization.", False,
        "When preprocessing financial transcripts, why does Dubois favor *lemmatization* over aggressive *stemming* despite higher computational cost?",
        {
            "A": "Lemmatization uses vocabulary and morphological context to return valid dictionary root words rather than crudely chopping suffixes.",
            "B": "Lemmatization preserves HTML tags and punctuation marks that carry sentiment.",
            "C": "Stemming automatically translates foreign-language filings into English.",
        },
        "A",
        "Stemming applies rule-based suffix stripping that can produce non-words or conflate distinct financial terms (e.g., 'operating'/'operation'), whereas lemmatization resolves words accurately to valid dictionary lemmas using part-of-speech context.",
        {
            "B": "HTML tags and extraneous punctuation are stripped prior to tokenization/lemmatization.",
            "C": "Neither stemming nor lemmatization performs language translation.",
        },
    )

    q_l2(
        "L2-QM-V10-Q6", "LM 6", "Big Data Projects", "N-Grams, Chi-Square Feature Selection & Governance",
        "QM-V10", v10_title, v10_text,
        "Apply n-grams and feature selection in financial NLP pipelines.", False,
        "Dubois notices that her unigram bag-of-words model misclassifies phrases such as `'not profitable'` and `'no default'` as positive or negative based on the second word alone. Which pipeline enhancement *best* solves this issue?",
        {
            "A": "Adding bigrams (2-grams) so adjacent negation tokens remain paired with their target words, paired with chi-square feature selection.",
            "B": "Expanding the stop-word list to delete every verb and adjective from the corpus.",
            "C": "Converting all numerical figures into random noise tokens.",
        },
        "A",
        "Including bigrams (or $n$-grams) captures local word order such as `'not_profitable'` and `'no_default'` so negation polarity is preserved, while chi-square feature selection filters high-dimensional n-grams down to informative predictors.",
        {
            "B": "Deleting verbs and adjectives strips out the primary carriers of financial sentiment.",
            "C": "Adding noise degrades signal-to-noise ratio without resolving negation context.",
        },
    )


def main():
    build_level_1()
    build_level_2()

    total = len(QUESTIONS)
    l1_cnt = sum(1 for q in QUESTIONS if q["level"] == 1)
    l2_cnt = sum(1 for q in QUESTIONS if q["level"] == 2)
    calc_cnt = sum(1 for f in CALC_FLAGS if f)
    ans_dist = {k: sum(1 for q in QUESTIONS if q["answer"] == k) for k in ("A", "B", "C")}

    assert total == 150, f"Expected 150 questions, got {total}"
    assert l1_cnt == 90, f"Expected 90 L1 questions, got {l1_cnt}"
    assert l2_cnt == 60, f"Expected 60 L2 questions, got {l2_cnt}"
    assert calc_cnt / total >= 0.65, f"Calculation ratio {calc_cnt/total:.2%} < 65%"

    out_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "data",
        "courses",
        "qm_qbank.json",
    )
    save_validated_json(QUESTIONS, out_path)
    print(
        f"Summary: total={total} (L1={l1_cnt}, L2={l2_cnt}), "
        f"calc={calc_cnt}/{total} ({calc_cnt/total:.1%}), answers={ans_dist}"
    )


if __name__ == "__main__":
    main()
