"""
Generate 125 CFA Alternative Investments questions (75 Level 1 + 50 Level 2 across 10 vignettes).
All numerical answers and distractors are computed directly in Python and validated via qbank_helper.
"""
import math
import os
import re
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(SCRIPT_DIR)
if SCRIPT_DIR not in sys.path:
    sys.path.insert(0, SCRIPT_DIR)

from qbank_helper import add_l1, add_l2, save_validated_json  # noqa: E402

SUBJECT = "Alternative Investments"
OUT_PATH = os.path.join(ROOT_DIR, "data", "courses", "alt_qbank.json")


def calc_irr(cfs: list[float]) -> float:
    """Solve exact IRR via bisection on NPV(r) = 0 over (-0.95, 5.0)."""
    def npv(r: float) -> float:
        return sum(cf / ((1.0 + r) ** t) for t, cf in enumerate(cfs))

    lo, hi = -0.95, 5.0
    f_lo, f_hi = npv(lo), npv(hi)
    if f_lo * f_hi > 0:
        raise ValueError(f"IRR not bracketed for cash flows: {cfs}")
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


def opt_pack(
    correct_text: str,
    wrong1_text: str,
    wrong1_why: str,
    wrong2_text: str,
    wrong2_why: str,
    pos: str,
) -> tuple[dict, str, dict]:
    """Place correct option at pos ('A'|'B'|'C') and build exact options + distractors dict."""
    assert pos in ("A", "B", "C"), f"Invalid option position {pos}"
    assert len({correct_text, wrong1_text, wrong2_text}) == 3, (
        f"Duplicate option strings: {correct_text} | {wrong1_text} | {wrong2_text}"
    )
    keys = ["A", "B", "C"]
    rem = [k for k in keys if k != pos]
    raw = {pos: correct_text, rem[0]: wrong1_text, rem[1]: wrong2_text}
    options = {k: raw[k] for k in keys}
    distractors = {rem[0]: wrong1_why, rem[1]: wrong2_why}
    return options, pos, distractors


def pos_cycle(idx: int) -> str:
    """Balanced deterministic option key permutation."""
    pattern = ("A", "B", "C", "B", "C", "A", "C", "A", "B")
    return pattern[(idx - 1) % len(pattern)]


def build_l1_part1(questions: list, calc_ids: set):
    """Build L1-ALT-001 through L1-ALT-037 (Structures/Fees, Private Capital, Real Estate/REITs)."""
    mod1 = "Alternative Investment Features, Methods, and Structures"

    # L1-ALT-001 (Calc): Management fee on committed vs invested + independent incentive fee
    comm, inv, gross_nav, mgmt_rate, inc_rate = 250.0, 180.0, 225.0, 0.015, 0.20
    mgmt_fee = comm * mgmt_rate
    profit = gross_nav - inv
    inc_fee = profit * inc_rate
    total_fee = mgmt_fee + inc_fee
    w1_001 = inv * mgmt_rate + inc_fee
    w2_001 = mgmt_fee + (profit - mgmt_fee) * inc_rate
    opts, ans, dist = opt_pack(
        rf"USD {total_fee:.2f} million",
        rf"USD {w1_001:.2f} million",
        r"Incorrectly applies the management fee to invested capital rather than committed capital.",
        rf"USD {w2_001:.2f} million",
        r"Incorrectly deducts the management fee before computing the incentive fee, violating the independent fee specification.",
        pos_cycle(1),
    )
    calc_ids.add("L1-ALT-001")
    add_l1(
        questions, "L1-ALT-001", SUBJECT, mod1, "Fee Structures", "Committed vs. Invested Capital Fees",
        "Calculate and interpret alternative investment returns both before and after fees.",
        rf"A private equity fund has USD {comm:.0f} million in committed capital and USD {inv:.0f} million in invested capital at the start of the year. The fund charges a 1.50% management fee based on committed capital and a 20% incentive fee on gross gains above invested capital, calculated independently of the management fee. If year-end gross asset value reaches USD {gross_nav:.0f} million (with no interim distributions), what is the total fee earned by the GP?",
        opts, ans,
        rf"Management fee is based on committed capital: $\text{{USD }} {comm:.0f}\text{{M}} \times 1.50\% = \text{{USD }} {mgmt_fee:.2f}\text{{M}}$. Gross gain is $\text{{USD }} {gross_nav:.0f}\text{{M}} - \text{{USD }} {inv:.0f}\text{{M}} = \text{{USD }} {profit:.2f}\text{{M}}$. Because the incentive fee is independent of the management fee, incentive fee $= {profit:.2f} \times 20\% = \text{{USD }} {inc_fee:.2f}\text{{M}}$. Total GP fees $= {mgmt_fee:.2f} + {inc_fee:.2f} = \text{{USD }} {total_fee:.2f}\text{{M}}$.",
        dist,
    )

    # L1-ALT-002 (Calc): Hard vs Soft hurdle net investor return
    aum0, r_gross, mgmt_r, inc_r, hurdle = 100.0, 0.18, 0.02, 0.20, 0.06
    aum_end_gross = aum0 * (1 + r_gross)
    mgmt_f = aum_end_gross * mgmt_r
    aum_net_mgmt = aum_end_gross - mgmt_f
    hard_base = aum0 * (1 + hurdle)
    inc_hard = max(0.0, (aum_net_mgmt - hard_base) * inc_r)
    net_ret_hard = (aum_net_mgmt - inc_hard - aum0) / aum0 * 100
    inc_soft = max(0.0, (aum_net_mgmt - aum0) * inc_r)
    w1_002 = (aum_net_mgmt - inc_soft - aum0) / aum0 * 100
    inc_indep = max(0.0, (aum_end_gross - hard_base) * inc_r)
    w2_002 = (aum_end_gross - mgmt_f - inc_indep - aum0) / aum0 * 100
    opts, ans, dist = opt_pack(
        rf"{net_ret_hard:.2f}%",
        rf"{w1_002:.2f}%",
        r"Reflects a soft hurdle structure where the 20% incentive fee is charged on the entire net profit once the hurdle is cleared.",
        rf"{w2_002:.2f}%",
        r"Fails to subtract the management fee from gross ending AUM before applying the hard hurdle and incentive fee.",
        pos_cycle(2),
    )
    calc_ids.add("L1-ALT-002")
    add_l1(
        questions, "L1-ALT-002", SUBJECT, mod1, "Fee Structures", "Hard Hurdle Rate",
        "Calculate and interpret alternative investment returns both before and after fees.",
        rf"A hedge fund starts the year with USD {aum0:.0f} million and earns a 18.00% gross return. The fee structure specifies a 2.00% management fee based on year-end gross AUM and a 20% incentive fee calculated net of the management fee, subject to a 6.00% hard hurdle rate. What is the investor's net return for the year?",
        opts, ans,
        rf"Year-end gross AUM is ${aum0:.0f} \times 1.18 = \text{{USD }} {aum_end_gross:.2f}\text{{M}}$. Management fee $= {aum_end_gross:.2f} \times 2\% = \text{{USD }} {mgmt_f:.2f}\text{{M}}$, leaving $\text{{USD }} {aum_net_mgmt:.2f}\text{{M}}$ net of management fee. Under a 6.00% hard hurdle, the threshold is $\text{{USD }} {hard_base:.2f}\text{{M}}$, so the incentive fee is $({aum_net_mgmt:.2f} - {hard_base:.2f}) \times 20\% = \text{{USD }} {inc_hard:.2f}\text{{M}}$. Ending net AUM is ${aum_net_mgmt - inc_hard:.2f}\text{{M}}$, giving a net return of ${net_ret_hard:.2f}\%$.",
        dist,
    )

    # L1-ALT-003 (Calc): High-water mark across 2 years
    hwm0, r1, r2 = 120.0, -0.15, 0.25
    mgmt_r3, inc_r3 = 0.015, 0.20
    # Year 1: mgmt fee on beginning AUM
    y1_gross = hwm0 * (1 + r1)
    y1_mgmt = hwm0 * mgmt_r3
    y1_end = y1_gross - y1_mgmt  # below HWM = 120, so inc = 0
    # Year 2: mgmt fee on beginning AUM
    y2_gross = y1_end * (1 + r2)
    y2_mgmt = y1_end * mgmt_r3
    y2_net_mgmt = y2_gross - y2_mgmt
    y2_inc = (y2_net_mgmt - hwm0) * inc_r3
    y2_end = y2_net_mgmt - y2_inc
    w1_003 = y2_net_mgmt - (y2_net_mgmt - y1_end) * inc_r3
    w2_003 = y2_net_mgmt - (y2_gross - hwm0) * inc_r3
    opts, ans, dist = opt_pack(
        rf"USD {y2_end:.2f} million",
        rf"USD {w1_003:.2f} million",
        r"Omits the high-water mark protection and charges incentive fees on all Year 2 gains above Year 1 ending value.",
        rf"USD {w2_003:.2f} million",
        r"Computes the Year 2 incentive fee above the high-water mark before deducting the Year 2 management fee.",
        pos_cycle(3),
    )
    calc_ids.add("L1-ALT-003")
    add_l1(
        questions, "L1-ALT-003", SUBJECT, mod1, "Fee Structures", "High-Water Mark",
        "Calculate and interpret alternative investment returns both before and after fees.",
        rf"An investor enters a hedge fund at an initial NAV and high-water mark (HWM) of USD {hwm0:.0f} million. The fund charges a 1.50% annual management fee on beginning-of-year AUM and a 20% incentive fee calculated net of the management fee, subject to the HWM (no hurdle). Gross returns are -15.0% in Year 1 and +25.0% in Year 2. What is the investor's net ending value at the end of Year 2?",
        opts, ans,
        rf"Year 1 gross AUM $= {hwm0:.0f} \times 0.85 = {y1_gross:.2f}\text{{M}}$; less management fee $({hwm0:.0f} \times 1.5\% = {y1_mgmt:.2f}\text{{M}})$ yields ${y1_end:.2f}\text{{M}}$ (below the USD {hwm0:.0f}M HWM, so Year 1 incentive fee is zero). Year 2 gross AUM $= {y1_end:.2f} \times 1.25 = {y2_gross:.2f}\text{{M}}$; less management fee $({y1_end:.2f} \times 1.5\% = {y2_mgmt:.2f}\text{{M}})$ yields ${y2_net_mgmt:.2f}\text{{M}}$. Incentive fee applies only above the USD {hwm0:.0f}M HWM: $({y2_net_mgmt:.2f} - {hwm0:.0f}) \times 20\% = {y2_inc:.2f}\text{{M}}$. Ending net NAV $= {y2_net_mgmt:.2f} - {y2_inc:.2f} = \text{{USD }} {y2_end:.2f}\text{{M}}$.",
        dist,
    )

    # L1-ALT-004 (Calc): Soft hurdle with 100% catch-up
    c0, gross_r, hurdle_r, inc_r4 = 100.0, 0.14, 0.08, 0.20
    profit4 = c0 * gross_r
    pref4 = c0 * hurdle_r
    # 100% catch-up until GP = 20% of total profits = 0.20 * 14 = 2.8? Wait: 0.25 * 8 = 2.0, then 20% of remaining 6 = 1.2 -> 3.2?
    # Wait: 0.20 * 14 = 2.8! Because at 10 + 8 + 2 = 110, GP has 2 of 10 (20%), then remaining 4 is split 80/20 -> 0.8 to GP -> 2.8 total!
    catchup_cap = (inc_r4 / (1.0 - inc_r4)) * pref4  # 2.0
    gp_catchup = min(profit4 - pref4, catchup_cap)  # 2.0
    rem_profit = max(0.0, profit4 - pref4 - gp_catchup)  # 4.0
    gp_total = gp_catchup + inc_r4 * rem_profit  # 2.8
    w1_004 = (profit4 - pref4) * inc_r4  # hard hurdle = 1.2
    w2_004 = pref4 * inc_r4 + (profit4 - pref4) * 0.5  # misapplied catch-up
    opts, ans, dist = opt_pack(
        rf"USD {gp_total:.2f} million",
        rf"USD {w1_004:.2f} million",
        r"Applies a hard hurdle without a catch-up provision, giving the GP 20% only of profits above the 8% hurdle.",
        rf"USD {w2_004:.2f} million",
        r"Miscomputes the catch-up band by splitting excess profits 50/50 instead of applying 100% catch-up up to a 20% cumulative split.",
        pos_cycle(4),
    )
    calc_ids.add("L1-ALT-004")
    add_l1(
        questions, "L1-ALT-004", SUBJECT, mod1, "Fee Structures", "Soft Hurdle and Catch-Up",
        "Describe alternative investment fee structures and waterfall mechanics.",
        rf"A private credit fund with USD {c0:.0f} million of contributed capital earns a net-of-management-fee profit of USD {profit4:.0f} million in a single realization (no prior losses). The waterfall provides an 8.0% preferred return to LPs, followed by a 100% GP catch-up until the GP receives 20% of total profits, and an 80%/20% LP/GP split thereafter. How much total carried interest does the GP earn?",
        opts, ans,
        rf"First, LPs receive the 8.0% preferred return of USD {pref4:.2f}M. Under a 100% catch-up, the GP takes all next profits up to $\frac{{0.20}}{{0.80}} \times {pref4:.2f} = \text{{USD }} {catchup_cap:.2f}\text{{M}}$ (at USD {pref4 + catchup_cap:.2f}M total profit, GP has {catchup_cap:.2f}M $= 20\%$). Remaining profit is ${profit4:.2f} - {pref4:.2f} - {catchup_cap:.2f} = \text{{USD }} {rem_profit:.2f}\text{{M}}$, split 80/20 (${inc_r4 * rem_profit:.2f}\text{{M}}$ to GP). Total GP carry $= {gp_catchup:.2f} + {inc_r4 * rem_profit:.2f} = \text{{USD }} {gp_total:.2f}\text{{M}}$ (20% of USD {profit4:.0f}M).",
        dist,
    )

    # L1-ALT-005 (Calc): Fund-of-Funds asymmetric incentive fees across underlying managers
    alloc = 50.0  # each of 2 underlying funds
    r_a, r_b = 0.24, -0.10
    # Underlying: 2% mgmt on beg, 20% inc net of mgmt
    net_a = alloc * (1 + r_a) - alloc * 0.02
    inc_a = (net_a - alloc) * 0.20
    end_a = net_a - inc_a
    net_b = alloc * (1 + r_b) - alloc * 0.02
    inc_b = 0.0
    end_b = net_b
    fof_gross = end_a + end_b  # out of 100
    fof_mgmt = 100.0 * 0.01  # 1% on beg 100
    fof_net_mgmt = fof_gross - fof_mgmt
    fof_inc = max(0.0, (fof_net_mgmt - 100.0) * 0.10)
    fof_end = fof_net_mgmt - fof_inc
    net_ret_5 = (fof_end - 100.0)
    # Wrong 1: netting A and B before underlying incentive fee
    agg_net = (alloc * (1 + r_a) + alloc * (1 + r_b)) - 100.0 * 0.02
    agg_inc = max(0.0, (agg_net - 100.0) * 0.20)
    w1_005 = (agg_net - agg_inc - 100.0 * 0.01) - max(0.0, ((agg_net - agg_inc - 1.0) - 100.0) * 0.10) - 100.0
    # Wrong 2: omitting FoF 1% management fee
    w2_005 = (fof_gross - max(0.0, (fof_gross - 100.0) * 0.10)) - 100.0
    opts, ans, dist = opt_pack(
        rf"{net_ret_5:.2f}%",
        rf"{w1_005:.2f}%",
        r"Improperly nets Fund A's gain against Fund B's loss before calculating the underlying managers' 20% incentive fees.",
        rf"{w2_005:.2f}%",
        r"Omits the fund-of-funds layer 1.0% management fee before determining the FoF investor's net return.",
        pos_cycle(5),
    )
    calc_ids.add("L1-ALT-005")
    add_l1(
        questions, "L1-ALT-005", SUBJECT, mod1, "Fund Structures", "Fund-of-Funds Fee Drag",
        "Describe advantages and disadvantages of direct, co-investment, and fund investing.",
        rf"A fund-of-funds (FoF) allocates USD 50 million to Hedge Fund A and USD 50 million to Hedge Fund B (USD 100 million total). Both underlying funds charge a 2% management fee on beginning capital plus a 20% incentive fee net of management fees. The FoF charges a 1% management fee on beginning capital plus a 10% incentive fee net of its management fee. If Fund A earns +24.0% gross and Fund B loses -10.0% gross, what is the FoF investor's net return?",
        opts, ans,
        rf"Fund A: gross ending $= 50 \times 1.24 = 62.00\text{{M}}$; management fee $= 50 \times 2\% = 1.00\text{{M}}$; net before incentive $= 61.00\text{{M}}$; incentive fee $= (61.00 - 50) \times 20\% = 2.20\text{{M}}$; Fund A net $= \text{{USD }} {end_a:.2f}\text{{M}}$. Fund B: gross ending $= 50 \times 0.90 = 45.00\text{{M}}$; management fee $= 1.00\text{{M}}$; no incentive fee on loss; Fund B net $= \text{{USD }} {end_b:.2f}\text{{M}}$. FoF gross $= {end_a:.2f} + {end_b:.2f} = {fof_gross:.2f}\text{{M}}$. Less FoF management fee ($1.00\text{{M}}$) leaves ${fof_net_mgmt:.2f}\text{{M}}$; FoF incentive fee $= ({fof_net_mgmt:.2f} - 100) \times 10\% = {fof_inc:.2f}\text{{M}}$. Net ending value $= \text{{USD }} {fof_end:.2f}\text{{M}}$, or ${net_ret_5:.2f}\%$.",
        dist,
    )

    # L1-ALT-006 (Calc): GP Clawback under deal-by-deal vs whole-of-fund
    # Deal 1 profit +40 -> GP carry 8; Deal 2 loss -15 -> total net profit 25 -> entitled carry 5 -> clawback = 3
    d1_prof, d2_loss, carry_r = 40.0, -15.0, 0.20
    paid_carry = d1_prof * carry_r
    net_prof = d1_prof + d2_loss
    entitled_carry = max(0.0, net_prof * carry_r)
    clawback = paid_carry - entitled_carry
    w1_006 = paid_carry
    w2_006 = abs(d2_loss) * carry_r * 0.5
    opts, ans, dist = opt_pack(
        rf"USD {clawback:.2f} million",
        rf"USD {w1_006:.2f} million",
        r"Mistakenly assumes the entire carried interest earned on Deal 1 must be refunded rather than only the excess over aggregate fund profits.",
        rf"USD {w2_006:.2f} million",
        r"Applies an arbitrary 50% haircut to the clawback instead of computing exact excess carried interest paid.",
        pos_cycle(6),
    )
    calc_ids.add("L1-ALT-006")
    add_l1(
        questions, "L1-ALT-006", SUBJECT, mod1, "Fee Structures", "Clawback Provision",
        "Describe alternative investment fee structures and waterfall mechanics.",
        rf"A private equity fund operates under a deal-by-deal (American) waterfall with a 20% carried interest and an active clawback provision (ignoring preferred returns for simplicity). Deal 1 generates a realized net gain of USD {d1_prof:.0f} million, and the GP collects USD {paid_carry:.0f} million in carry. Deal 2 later realizes a net loss of USD {abs(d2_loss):.0f} million, and the fund liquidates with no other investments. Assuming no tax-reduction offset, what amount must the GP return to LPs under the clawback?",
        opts, ans,
        rf"Aggregate fund profit across both deals is $\text{{USD }} {d1_prof:.0f}\text{{M}} - \text{{USD }} {abs(d2_loss):.0f}\text{{M}} = \text{{USD }} {net_prof:.0f}\text{{M}}$. Under a whole-of-fund reconciliation, total entitled carry is $20\% \times {net_prof:.0f}\text{{M}} = \text{{USD }} {entitled_carry:.2f}\text{{M}}$. Because the GP already received USD {paid_carry:.2f}M, the GP owes a clawback of ${paid_carry:.2f} - {entitled_carry:.2f} = \text{{USD }} {clawback:.2f}\text{{M}}$.",
        dist,
    )

    # L1-ALT-007 (Calc): Redemption Gate + Side Pocket Liquidity
    nav_total, side_pct, lp_share_val, gate_pct = 500.0, 0.20, 40.0, 0.15
    liquid_nav = nav_total * (1 - side_pct)  # 400
    lp_liquid = lp_share_val * (1 - side_pct)  # 32
    max_fund_gate = liquid_nav * gate_pct  # 60
    # Suppose total redemption requests = 160M of liquid NAV; LP requests full 32M liquid share -> pro-rata factor = 60/160 = 0.375
    tot_req = 160.0
    prorata = max_fund_gate / tot_req
    lp_paid = lp_liquid * prorata
    w1_007 = lp_share_val * gate_pct  # applies gate directly to LP balance
    w2_007 = lp_share_val * prorata  # applies pro-rata to total including side pocket
    opts, ans, dist = opt_pack(
        rf"USD {lp_paid:.2f} million",
        rf"USD {w1_007:.2f} million",
        r"Applies the 15% fund-level gate percentage directly to the LP's total account rather than using the pro-rata fund gate allocation on liquid assets.",
        rf"USD {w2_007:.2f} million",
        r"Applies the pro-rata payout factor to the LP's entire USD 40 million balance, ignoring that the 20% side pocket is illiquid and excluded from redemptions.",
        pos_cycle(7),
    )
    calc_ids.add("L1-ALT-007")
    add_l1(
        questions, "L1-ALT-007", SUBJECT, mod1, "Liquidity & Governance", "Gates and Side Pockets",
        "Describe features and terms of alternative investment funds.",
        rf"A USD {nav_total:.0f} million hedge fund places 20% of its portfolio in an illiquid side pocket and imposes a quarterly fund-level redemption gate of 15% of liquid NAV. An LP holding USD {lp_share_val:.0f} million of total NAV submits a full redemption request, while total quarterly redemption requests across all LPs reach USD {tot_req:.0f} million of liquid NAV (applied pro rata). How much cash will the LP receive this quarter?",
        opts, ans,
        rf"Liquid fund NAV is ${nav_total:.0f} \times (1 - 0.20) = \text{{USD }} {liquid_nav:.0f}\text{{M}}$, so the 15% quarterly fund gate caps total payouts at $0.15 \times {liquid_nav:.0f} = \text{{USD }} {max_fund_gate:.0f}\text{{M}}$. Because USD {tot_req:.0f}M was requested, the pro-rata fill rate is $\frac{{{max_fund_gate:.0f}}}{{{tot_req:.0f}}} = {prorata:.3f}$ ($37.5\%$). The LP's liquid holdings are ${lp_share_val:.0f} \times 0.80 = \text{{USD }} {lp_liquid:.0f}\text{{M}}$, yielding ${lp_liquid:.0f} \times {prorata:.3f} = \text{{USD }} {lp_paid:.2f}\text{{M}}$ in cash.",
        dist,
    )

    # L1-ALT-008 (Calc): Management fee offset (monitoring/transaction fee sharing)
    comm8, rate8, tx_fee, offset_pct = 400.0, 0.0175, 2.5, 0.80
    gross_mgmt8 = comm8 * rate8  # 7.0
    offset_amt = tx_fee * offset_pct  # 2.0
    net_mgmt8 = gross_mgmt8 - offset_amt  # 5.0
    w1_008 = gross_mgmt8 - tx_fee
    w2_008 = gross_mgmt8 + (tx_fee * (1 - offset_pct))
    opts, ans, dist = opt_pack(
        rf"USD {net_mgmt8:.2f} million",
        rf"USD {w1_008:.2f} million",
        r"Deducts 100% of the transaction fee instead of applying the 80% fee-offset agreement.",
        rf"USD {w2_008:.2f} million",
        r"Adds the GP's retained 20% fee share to the management fee rather than crediting the 80% offset against it.",
        pos_cycle(8),
    )
    calc_ids.add("L1-ALT-008")
    add_l1(
        questions, "L1-ALT-008", SUBJECT, mod1, "Fee Structures", "Management Fee Offset",
        "Describe alternative investment fee structures and waterfall mechanics.",
        rf"A buyout fund with USD {comm8:.0f} million in committed capital charges a 1.75% annual management fee. During the year, the GP collects USD {tx_fee:.1f} million in portfolio-company monitoring and transaction fees, subject to an 80% management fee offset. What net management fee do LPs pay for the year?",
        opts, ans,
        rf"Base management fee is $\text{{USD }} {comm8:.0f}\text{{M}} \times 1.75\% = \text{{USD }} {gross_mgmt8:.2f}\text{{M}}$. The 80% offset credits $0.80 \times \text{{USD }} {tx_fee:.1f}\text{{M}} = \text{{USD }} {offset_amt:.2f}\text{{M}}$ against the management fee, reducing the net LP management fee to ${gross_mgmt8:.2f} - {offset_amt:.2f} = \text{{USD }} {net_mgmt8:.2f}\text{{M}}$.",
        dist,
    )

    # L1-ALT-009 (Concept): Direct vs Co-investment vs Fund investing
    opts, ans, dist = opt_pack(
        r"Co-investing provides direct exposure to specific deals with reduced or zero management and performance fees, while relying on the lead GP's sourcing and due diligence.",
        r"Co-investing completely eliminates concentration risk because LPs automatically gain exposure across every portfolio company in the GP's flagship fund.",
        r"Co-investments increase deal-level concentration by sizing up into specific portfolio companies rather than diversifying across the entire fund.",
        r"Direct investing requires the lowest internal staffing and operational expertise because third-party GPs retain full asset-management responsibility.",
        r"Direct investing requires the highest internal origination, due diligence, and governance resources because no external GP manages the asset.",
        pos_cycle(9),
    )
    add_l1(
        questions, "L1-ALT-009", SUBJECT, mod1, "Investment Methods", "Direct, Co-Investment, and Fund Investing",
        "Describe advantages and disadvantages of direct, co-investment, and fund investing.",
        r"Which statement most accurately distinguishes co-investing from fund investing and direct investing in private markets?",
        opts, ans,
        r"Co-investing lets LPs invest alongside a GP in specific transactions—often on a no-fee, no-carry basis—lowering overall fee drag while leveraging the GP's origination and operational expertise, though it increases single-deal concentration and requires quick LP execution.",
        dist,
    )

    # L1-ALT-010 (Concept): Partnership clauses (Key-person, MFN, No-fault divorce)
    opts, ans, dist = opt_pack(
        r"A key-person provision suspends the investment period if designated senior professionals depart or cease devoting required time to the fund.",
        r"A most-favored-nation (MFN) clause guarantees that the GP will match the highest historical IRR achieved by any peer fund in the same vintage year.",
        r"MFN clauses allow an LP to receive fee or governance terms granted via side letters to equal or smaller LPs, not performance guarantees.",
        r"A key-person provision requires the GP to immediately liquidate all portfolio companies at market value if a senior partner leaves.",
        r"A key-person trigger halts new capital calls for investments during a cure period, rather than forcing fire-sale liquidation of existing holdings.",
        pos_cycle(10),
    )
    add_l1(
        questions, "L1-ALT-010", SUBJECT, mod1, "Fund Governance", "Partnership Clauses",
        "Describe features and terms of alternative investment funds.",
        r"Which statement accurately describes a standard limited partnership governance provision in private alternative funds?",
        opts, ans,
        r"A key-person clause protects LPs from team departures during the commitment period by automatically suspending new investment activity until replacement principals are approved or LPs vote to lift the suspension.",
        dist,
    )

    # L1-ALT-011 (Concept): Soft hurdle catch-up mechanics
    opts, ans, dist = opt_pack(
        r"Once total return exceeds the soft hurdle rate, the GP earns incentive fees on the entire gain from the first dollar, typically via a catch-up band.",
        r"Under a soft hurdle, incentive fees apply only to returns generated above the hurdle rate, leaving the GP permanently below 20% of total profits.",
        r"Charging incentive fees solely on excess returns above the hurdle describes a hard hurdle, not a soft hurdle.",
        r"A soft hurdle eliminates the GP's preferred return obligation to LPs and pays 20% incentive fees even when returns are negative.",
        r"A soft hurdle still requires total returns to clear the hurdle before any incentive fee is triggered; negative returns earn zero carry.",
        pos_cycle(11),
    )
    add_l1(
        questions, "L1-ALT-011", SUBJECT, mod1, "Fee Structures", "Hard vs. Soft Hurdle",
        "Describe alternative investment fee structures and waterfall mechanics.",
        r"How does a soft hurdle rate differ from a hard hurdle rate in an alternative fund's incentive compensation structure?",
        opts, ans,
        r"With a soft hurdle, once cumulative returns exceed the hurdle, the GP's incentive fee (often via a catch-up tranche) applies to total profits rather than solely the margin above the hurdle.",
        dist,
    )

    # L1-ALT-012 (Concept): Appraisal smoothing and return biases
    opts, ans, dist = opt_pack(
        r"Appraisal-based valuation smooths interim returns, artificially depressing measured volatility and correlation with public equities.",
        r"Survivorship bias in alternative investment databases overstates historical risk and understates average realized returns.",
        r"Survivorship bias drops failed funds from databases, which understates risk and overstates average historical returns.",
        r"Backfill bias occurs when underperforming funds retroactively submit pre-inception returns to boost database averages.",
        r"Backfill (instant-history) bias occurs when successful funds selectively report strong early track records upon entering a database, inflating returns.",
        pos_cycle(12),
    )
    add_l1(
        questions, "L1-ALT-012", SUBJECT, mod1, "Performance Appraisal", "Smoothing and Database Biases",
        "Explain issues in measuring and evaluating returns of alternative investments.",
        r"Which statement accurately describes a measurement issue when evaluating illiquid alternative investments?",
        opts, ans,
        r"Infrequent appraisals create stale prices and positive serial autocorrelation, which artificially dampens measured standard deviation and understated beta/correlation relative to mark-to-market public markets.",
        dist,
    )

    # Topic 2: Private Capital (L1-ALT-013 to L1-ALT-025)
    mod2 = "Investments in Private Capital: Equity and Debt"

    # L1-ALT-013 (Calc): DPI, RVPI, TVPI
    comm13, pic13, dist13, nav13 = 200.0, 160.0, 128.0, 144.0
    dpi13 = dist13 / pic13
    rvpi13 = nav13 / pic13
    tvpi13 = dpi13 + rvpi13
    w1_013 = (dist13 + nav13) / comm13  # uses committed capital
    w2_013 = dist13 / pic13  # confuses DPI with TVPI
    opts, ans, dist = opt_pack(
        rf"DPI = {dpi13:.2f}x; TVPI = {tvpi13:.2f}x",
        rf"DPI = {dist13 / comm13:.2f}x; TVPI = {w1_013:.2f}x",
        r"Uses committed capital (USD 200M) rather than paid-in capital (USD 160M) in the denominator.",
        rf"DPI = {rvpi13:.2f}x; TVPI = {w2_013:.2f}x",
        r"Confuses RVPI with DPI and omits residual NAV when computing TVPI.",
        pos_cycle(13),
    )
    calc_ids.add("L1-ALT-013")
    add_l1(
        questions, "L1-ALT-013", SUBJECT, mod2, "Private Equity Performance", "DPI, RVPI, and TVPI",
        "Calculate and interpret private capital performance metrics.",
        rf"At the end of Year 6, a private equity fund with USD {comm13:.0f} million in committed capital has called USD {pic13:.0f} million (paid-in capital), distributed USD {dist13:.0f} million to LPs, and holds a remaining net asset value (NAV) of USD {nav13:.0f} million. What are the fund's DPI and TVPI?",
        opts, ans,
        rf"$\text{{DPI}} = \frac{{\text{{Distributions}}}}{{\text{{Paid-In Capital}}}} = \frac{{{dist13:.0f}}}{{{pic13:.0f}}} = {dpi13:.2f}\text{{x}}$. $\text{{RVPI}} = \frac{{\text{{NAV}}}}{{\text{{PIC}}}} = \frac{{{nav13:.0f}}}{{{pic13:.0f}}} = {rvpi13:.2f}\text{{x}}$. $\text{{TVPI}} = \text{{DPI}} + \text{{RVPI}} = {dpi13:.2f} + {rvpi13:.2f} = {tvpi13:.2f}\text{{x}}$.",
        dist,
    )

    # L1-ALT-014 (Calc): Multi-period PE IRR
    cfs14 = [-50.0, -40.0, 15.0, 45.0, 95.0]
    irr14 = calc_irr(cfs14) * 100
    # Wrong 1: simple annualized MOIC
    tot_in = 90.0
    tot_out = sum(c for c in cfs14 if c > 0)
    w1_014 = ((tot_out / tot_in) ** (1 / 4) - 1) * 100
    # Wrong 2: ignore t=1 negative cash flow timing (treat all -90 at t=0)
    w2_014 = calc_irr([-90.0, 0.0, 15.0, 45.0, 95.0]) * 100
    opts, ans, dist = opt_pack(
        rf"{irr14:.2f}%",
        rf"{w1_014:.2f}%",
        r"Uses a 4-year geometric growth rate on total MOIC, ignoring intermediate cash-flow timing.",
        rf"{w2_014:.2f}%",
        r"Assumes the entire USD 90 million was called at Year 0 instead of Year 0 and Year 1.",
        pos_cycle(14),
    )
    calc_ids.add("L1-ALT-014")
    add_l1(
        questions, "L1-ALT-014", SUBJECT, mod2, "Private Equity Performance", "Money-Weighted IRR",
        "Calculate and interpret private capital performance metrics.",
        r"A private equity fund reports the following annual net cash flows to LPs (in USD millions): Year 0: -50; Year 1: -40; Year 2: +15; Year 3: +45; Year 4 (liquidation): +95. What is the fund's since-inception annualized IRR?",
        opts, ans,
        rf"Solving $0 = -50 + \frac{{-40}}{{1+r}} + \frac{{15}}{{(1+r)^2}} + \frac{{45}}{{(1+r)^3}} + \frac{{95}}{{(1+r)^4}}$ numerically yields an exact IRR of ${irr14:.2f}\%$.",
        dist,
    )

    # L1-ALT-015 (Calc): LBO equity MOIC & IRR
    ebitda0, mult0, debt0 = 40.0, 8.0, 220.0
    ev0 = ebitda0 * mult0  # 320
    eq0 = ev0 - debt0  # 100
    ebitda5, mult5, debt_repaid = 58.0, 9.0, 120.0
    ev5 = ebitda5 * mult5  # 522
    debt5 = debt0 - debt_repaid  # 100
    eq5 = ev5 - debt5  # 422
    moic15 = eq5 / eq0
    irr15 = (moic15 ** (1 / 5) - 1) * 100
    w1_015 = ((ev5 / ev0) ** (1 / 5) - 1) * 100
    w2_015 = (((ev5 - debt0) / eq0) ** (1 / 5) - 1) * 100
    opts, ans, dist = opt_pack(
        rf"{irr15:.2f}%",
        rf"{w1_015:.2f}%",
        r"Calculates unlevered enterprise value CAGR rather than levered sponsor equity IRR.",
        rf"{w2_015:.2f}%",
        r"Subtracts initial debt instead of remaining Year 5 debt after paydown when computing exit equity value.",
        pos_cycle(15),
    )
    calc_ids.add("L1-ALT-015")
    add_l1(
        questions, "L1-ALT-015", SUBJECT, mod2, "Leveraged Buyouts", "LBO Equity Return",
        "Explain buyout strategies and value creation drivers.",
        rf"A buyout firm acquires a company with USD {ebitda0:.0f} million EBITDA at an 8.0x EV/EBITDA multiple, funded with USD {debt0:.0f} million of debt and sponsor equity. Over a 5-year holding period, EBITDA grows to USD {ebitda5:.0f} million, USD {debt_repaid:.0f} million of debt is repaid from free cash flow, and the firm exits at 9.0x EV/EBITDA. Assuming no interim dividends, what is the sponsor's annualized equity IRR?",
        opts, ans,
        rf"Entry EV $= {ebitda0:.0f} \times 8.0 = \text{{USD }} {ev0:.0f}\text{{M}}$; Entry Equity $= {ev0:.0f} - {debt0:.0f} = \text{{USD }} {eq0:.0f}\text{{M}}$. Exit EV $= {ebitda5:.0f} \times 9.0 = \text{{USD }} {ev5:.0f}\text{{M}}$; Exit Debt $= {debt0:.0f} - {debt_repaid:.0f} = \text{{USD }} {debt5:.0f}\text{{M}}$; Exit Equity $= {ev5:.0f} - {debt5:.0f} = \text{{USD }} {eq5:.0f}\text{{M}}$. Equity MOIC $= \frac{{{eq5:.0f}}}{{{eq0:.0f}}} = {moic15:.2f}\text{{x}}$, giving a 5-year IRR of $({moic15:.2f})^{{1/5}} - 1 = {irr15:.2f}\%$.",
        dist,
    )

    # L1-ALT-016 (Calc): VC Method single round pre/post-money & share price
    inv16, exit_e16, mult16, t16, r16, n_old16 = 5.0, 8.0, 15.0, 4, 0.35, 2.0  # n_old in millions
    exit_v16 = exit_e16 * mult16  # 120M
    post16 = exit_v16 / ((1 + r16) ** t16)
    pre16 = post16 - inv16
    p_share16 = pre16 / n_old16
    w1_016 = post16 / n_old16
    w2_016 = (exit_v16 / ((1 + r16) ** (t16 + 1)) - inv16) / n_old16
    opts, ans, dist = opt_pack(
        rf"USD {p_share16:.2f}",
        rf"USD {w1_016:.2f}",
        r"Divides post-money valuation rather than pre-money valuation by existing founder shares.",
        rf"USD {w2_016:.2f}",
        r"Discounts the exit equity value for 5 years instead of the 4-year horizon.",
        pos_cycle(16),
    )
    calc_ids.add("L1-ALT-016")
    add_l1(
        questions, "L1-ALT-016", SUBJECT, mod2, "Venture Capital", "VC Method Valuation",
        "Explain venture capital strategies and valuation methods.",
        rf"A venture investor plans to invest USD {inv16:.0f} million in a startup with {n_old16:.1f} million existing shares. The startup is projected to generate USD {exit_e16:.0f} million in earnings in Year 4 and exit at a 15.0x P/E multiple. Using a 35.0% target annual return and assuming no subsequent dilution rounds, what price per share should the VC pay?",
        opts, ans,
        rf"Terminal value at Year 4 is ${exit_e16:.0f} \times 15.0 = \text{{USD }} {exit_v16:.0f}\text{{M}}$. Post-money valuation is $\frac{{{exit_v16:.0f}}}{{1.35^4}} = \text{{USD }} {post16:.2f}\text{{M}}$. Pre-money valuation is ${post16:.2f} - {inv16:.0f} = \text{{USD }} {pre16:.2f}\text{{M}}$. Dividing by {n_old16:.1f} million existing shares gives $\text{{USD }} {p_share16:.2f}$ per share.",
        dist,
    )

    # L1-ALT-017 (Calc): VC Method with future round dilution
    inv_a, exit_v17, t17, r17, dil_b = 4.0, 150.0, 5, 0.40, 0.25
    pv17 = exit_v17 / ((1 + r17) ** t17)
    req_exit_pct = inv_a / pv17
    req_curr_pct = req_exit_pct / (1 - dil_b)
    w1_017 = req_exit_pct * (1 - dil_b) * 100
    w2_017 = req_exit_pct * 100
    opts, ans, dist = opt_pack(
        rf"{req_curr_pct * 100:.2f}%",
        rf"{w1_017:.2f}%",
        r"Multiplies by the retention factor (1 - 25%) instead of dividing by it, understating required current ownership.",
        rf"{w2_017:.2f}%",
        r"Ignores the expected 25% dilution from the future Series B financing round.",
        pos_cycle(17),
    )
    calc_ids.add("L1-ALT-017")
    add_l1(
        questions, "L1-ALT-017", SUBJECT, mod2, "Venture Capital", "Multi-Round Dilution",
        "Explain venture capital strategies and valuation methods.",
        rf"A Series A investor contributes USD {inv_a:.0f} million into a tech venture targeting an exit value of USD {exit_v17:.0f} million in Year 5 and requires a 40.0% annualized return. If a subsequent Series B round is expected to dilute Series A holders by 25.0%, what current ownership percentage must the Series A investor negotiate today?",
        opts, ans,
        rf"Discounted post-money value today is $\frac{{{exit_v17:.0f}}}{{1.40^5}} = \text{{USD }} {pv17:.2f}\text{{M}}$, requiring an exit ownership stake of $\frac{{{inv_a:.0f}}}{{{pv17:.2f}}} = {req_exit_pct * 100:.2f}\%$. Accounting for 25% Series B dilution (75% retention), current Series A ownership must be $\frac{{{req_exit_pct * 100:.2f}\%}}{{1 - 0.25}} = {req_curr_pct * 100:.2f}\%$.",
        dist,
    )

    # L1-ALT-018 (Calc): Participating preferred vs non-participating convertible preferred
    inv18, own18, exit18 = 10.0, 0.25, 28.0
    # 1x participating preferred with no cap: gets 10M pref + 25% of remaining (28 - 10) = 10 + 4.5 = 14.5M
    part_payoff = inv18 + own18 * (exit18 - inv18)
    w1_018 = max(inv18, own18 * exit18)  # non-participating
    w2_018 = inv18 + own18 * exit18  # double-counts pref in remaining pool
    opts, ans, dist = opt_pack(
        rf"USD {part_payoff:.2f} million",
        rf"USD {w1_018:.2f} million",
        r"Computes the payoff for non-participating convertible preferred (greater of 1x preference or 25% common conversion).",
        rf"USD {w2_018:.2f} million",
        r"Double-counts the USD 10M liquidation preference by applying the 25% participation share to the entire USD 28M exit value.",
        pos_cycle(18),
    )
    calc_ids.add("L1-ALT-018")
    add_l1(
        questions, "L1-ALT-018", SUBJECT, mod2, "Venture Capital", "Preferred Stock Payoffs",
        "Explain venture capital strategies and valuation methods.",
        rf"A VC firm invests USD {inv18:.0f} million for a 25% equity stake structured as 1x participating preferred stock (uncapped). The company is acquired for USD {exit18:.0f} million. How much does the VC firm receive at exit?",
        opts, ans,
        rf"Under 1x uncapped participating preferred, the VC first receives its USD {inv18:.0f}M liquidation preference, then participates pro rata (25%) in the remaining proceeds of ${exit18:.0f} - {inv18:.0f} = \text{{USD }} {exit18 - inv18:.0f}\text{{M}}$. Total VC payoff $= {inv18:.0f} + 0.25 \times {exit18 - inv18:.0f} = \text{{USD }} {part_payoff:.2f}\text{{M}}$.",
        dist,
    )

    # L1-ALT-019 (Calc): Private credit unitranche / mezzanine yield with PIK & OID
    par19, oid19, cash_c, pik_c, mat19 = 100.0, 97.0, 0.08, 0.03, 5
    # Year-by-year cash flows per 100 par: t=0: -97; t=1..4: +8 cash, principal compounds at 3% PIK
    # Ending principal = 100 * (1.03)^5; annual cash coupon = 8% of growing principal?
    # Let's specify simple coupon on initial par OR compounding PIK on principal:
    # Standard clean CFA setup: annual cash coupon 8% on initial par (USD 8/yr), plus 3% annual compounding PIK added to principal paid at Year 5, issued at 97 (3% OID).
    end_prin = par19 * ((1 + pik_c) ** mat19)
    cfs19 = [-oid19] + [par19 * cash_c] * (mat19 - 1) + [par19 * cash_c + end_prin]
    ytm19 = calc_irr(cfs19) * 100
    w1_019 = (cash_c + pik_c) * 100  # ignores OID
    w2_019 = (cash_c + (par19 - oid19) / (mat19 * par19)) * 100  # omits PIK
    opts, ans, dist = opt_pack(
        rf"{ytm19:.2f}%",
        rf"{w1_019:.2f}%",
        r"Sums cash and PIK coupons while ignoring the 3% original issue discount (OID) price accretion.",
        rf"{w2_019:.2f}%",
        r"Includes cash coupon and OID amortization while omitting the 3% compounding PIK interest paid at maturity.",
        pos_cycle(19),
    )
    calc_ids.add("L1-ALT-019")
    add_l1(
        questions, "L1-ALT-019", SUBJECT, mod2, "Private Debt", "Mezzanine Yield with PIK and OID",
        "Explain private credit strategies and return characteristics.",
        rf"A 5-year mezzanine loan with USD {par19:.0f} million face value is issued at an original issue discount price of USD {oid19:.0f} million. It pays an 8.0% annual cash coupon on initial face value plus 3.0% annual payment-in-kind (PIK) interest that compounds on principal and is paid in full at Year 5 maturity. What is the annualized yield-to-maturity (IRR) to the lender?",
        opts, ans,
        rf"Principal compounds via PIK to $100 \times 1.03^5 = \text{{USD }} {end_prin:.2f}\text{{M}}$ at Year 5. Cash flows are: $t=0$: $-97.00$; $t=1\text{{-}}4$: $+8.00$; $t=5$: $+8.00 + {end_prin:.2f} = +{8 + end_prin:.2f}$. Solving for IRR yields ${ytm19:.2f}\%$.",
        dist,
    )

    # L1-ALT-020 (Calc): Distressed debt recovery waterfall (absolute priority)
    ev20, sen_claim, sub_claim, sub_buy_pct, t20 = 150.0, 110.0, 80.0, 0.35, 2
    sub_recovery = max(0.0, min(sub_claim, ev20 - sen_claim))  # 40M out of 80M = 50% of par
    sub_cost = sub_claim * sub_buy_pct  # 28M
    ann_ret20 = ((sub_recovery / sub_cost) ** (1 / t20) - 1) * 100
    w1_020 = ((sub_recovery / sub_cost) - 1) * 100  # unannualized total return
    # Pro-rata recovery ignoring absolute priority
    prorata_sub = ev20 * (sub_claim / (sen_claim + sub_claim))
    w2_020 = ((prorata_sub / sub_cost) ** (1 / t20) - 1) * 100
    opts, ans, dist = opt_pack(
        rf"{ann_ret20:.2f}%",
        rf"{w1_020:.2f}%",
        r"Reports the cumulative 2-year total return instead of the annualized return.",
        rf"{w2_020:.2f}%",
        r"Assumes pro-rata recovery across senior and subordinated debt, violating absolute priority.",
        pos_cycle(20),
    )
    calc_ids.add("L1-ALT-020")
    add_l1(
        questions, "L1-ALT-020", SUBJECT, mod2, "Private Debt", "Distressed Debt Waterfall",
        "Explain private credit strategies and return characteristics.",
        rf"A distressed firm enters restructuring with USD {sen_claim:.0f} million of senior secured debt and USD {sub_claim:.0f} million of subordinated notes. A distressed debt fund buys the entire subordinated note tranche at 35% of par. After 2 years, the reorganized enterprise value is USD {ev20:.0f} million and distributed strictly by absolute priority (no interim coupons). What is the fund's annualized return?",
        opts, ans,
        rf"Purchase cost $= {sub_claim:.0f} \times 0.35 = \text{{USD }} {sub_cost:.2f}\text{{M}}$. Under absolute priority, senior debt receives its full USD {sen_claim:.0f}M, leaving ${ev20:.0f} - {sen_claim:.0f} = \text{{USD }} {sub_recovery:.2f}\text{{M}}$ for subordinated noteholders. Over 2 years, annualized return is $\left(\frac{{{sub_recovery:.2f}}}{{{sub_cost:.2f}}}\right)^{{1/2}} - 1 = {ann_ret20:.2f}\%$.",
        dist,
    )

    # L1-ALT-021 (Calc): Subscription credit line effect on IRR vs MOIC
    cap21, exit21, dur_no_line, dur_with_line = 100.0, 200.0, 4.0, 3.0
    irr_no = (exit21 / cap21) ** (1 / dur_no_line) - 1
    irr_with = (exit21 / cap21) ** (1 / dur_with_line) - 1
    diff_bps = (irr_with - irr_no) * 100
    opts, ans, dist = opt_pack(
        rf"IRR rises from {irr_no * 100:.2f}% to {irr_with * 100:.2f}% while MOIC stays at 2.00x",
        rf"IRR stays at {irr_no * 100:.2f}% while MOIC increases from 2.00x to 2.67x",
        r"Confuses the time-weighting sensitivity of IRR with cash-multiple MOIC, which ignores timing.",
        rf"IRR rises to {irr_with * 100:.2f}% and MOIC falls to 1.50x",
        r"Incorrectly assumes borrowing on a credit line reduces gross exit proceeds by 25% of principal.",
        pos_cycle(21),
    )
    calc_ids.add("L1-ALT-021")
    add_l1(
        questions, "L1-ALT-021", SUBJECT, mod2, "Private Equity Performance", "Subscription Credit Lines",
        "Calculate and interpret private capital performance metrics.",
        rf"A private equity fund invests USD {cap21:.0f} million and exits at USD {exit21:.0f} million 4.0 years after acquisition (ignoring line interest expense). If the GP uses a subscription credit facility to delay calling LP capital until 1.0 year after acquisition (making LP capital invested for 3.0 years), how do reported LP IRR and MOIC change?",
        opts, ans,
        rf"Without the line, 4-year IRR is $(2.00)^{{1/4}} - 1 = {irr_no * 100:.2f}\%$. Delaying the LP capital call by 1 year compresses LP capital duration to 3.0 years, boosting IRR to $(2.00)^{{1/3}} - 1 = {irr_with * 100:.2f}\%$ (+{diff_bps:.2f} pp), while total cash multiple (MOIC) remains unchanged at $200/100 = 2.00\text{{x}}$.",
        dist,
    )

    # L1-ALT-022 (Concept): J-Curve effect
    opts, ans, dist = opt_pack(
        r"Negative net IRRs in the early years caused by management fees charged on committed capital and initial investments held at cost or written down before value realization.",
        r"Positive early IRRs caused by immediate dividend recapitalizations followed by declining returns as portfolio companies mature.",
        r"Dividend recapitalizations typically occur mid-to-late in the holding period after deleveraging, not at initial deployment.",
        r"A regulatory capital curve requiring pension funds to post collateral equal to 100% of unfunded commitments.",
        r"The J-curve describes fund cash flows and IRR evolution over time, not a collateral posting requirement.",
        pos_cycle(22),
    )
    add_l1(
        questions, "L1-ALT-022", SUBJECT, mod2, "Private Equity Performance", "J-Curve Effect",
        "Calculate and interpret private capital performance metrics.",
        r"What primarily drives the J-curve pattern observed in private equity fund net returns during the first 2 to 4 years of a fund's life?",
        opts, ans,
        r"Early capital outflows reflect organization costs and management fees computed on committed capital while portfolio companies are carried at cost or early write-downs, producing negative initial IRRs before later profitable exits steepen returns upward.",
        dist,
    )

    # L1-ALT-023 (Concept): VC stages
    opts, ans, dist = opt_pack(
        r"Early-stage (Series A) financing funds initial commercial production and sales, carrying high business/technology failure risk and negative operating cash flow.",
        r"Mezzanine or pre-IPO financing carries the highest risk of total capital loss because the company has not yet built a commercial prototype.",
        r"Prototype development belongs to seed/angel funding; pre-IPO financing carries much lower technology risk and focuses on scaling toward liquidity.",
        r"Angel financing typically provides the largest single equity check sizes to fund cross-border acquisitions.",
        r"Angel rounds are small initial investments from high-net-worth individuals to validate a concept, whereas growth equity funds large expansion.",
        pos_cycle(23),
    )
    add_l1(
        questions, "L1-ALT-023", SUBJECT, mod2, "Venture Capital", "Venture Capital Stages",
        "Explain venture capital strategies and valuation methods.",
        r"Which statement accurately characterizes venture capital financing stages?",
        opts, ans,
        r"Early-stage venture capital supports companies moving beyond proof-of-concept into initial commercialization and customer acquisition, characterized by high failure rates, negative free cash flow, and high return dispersion.",
        dist,
    )

    # L1-ALT-024 (Concept): Private credit covenants and seniority
    opts, ans, dist = opt_pack(
        r"Direct lending typically provides senior secured loans with maintenance covenants, floating rates, and bespoke terms to middle-market borrowers.",
        r"Mezzanine debt ranks senior to first-lien bank loans and relies strictly on fixed-rate collateral liquidation for return.",
        r"Mezzanine debt is subordinated to senior debt and derives return from higher coupons, PIK interest, and equity kickers such as warrants.",
        r"Private credit funds generally have daily public pricing transparency and lower illiquidity premia than investment-grade corporate bonds.",
        r"Private credit loans are illiquid, bilaterally negotiated instruments lacking daily market prices, which underpins their illiquidity spread premium.",
        pos_cycle(24),
    )
    add_l1(
        questions, "L1-ALT-024", SUBJECT, mod2, "Private Debt", "Direct Lending vs. Mezzanine",
        "Explain private credit strategies and return characteristics.",
        r"Which description most accurately captures a core feature of private credit investing?",
        opts, ans,
        r"Direct lending funds typically originate senior secured, floating-rate loans with protective financial maintenance covenants directly to middle-market firms, offering illiquidity premia and lower interest-rate duration than fixed-rate bonds.",
        dist,
    )

    # L1-ALT-025 (Concept): PE Exit routes
    opts, ans, dist = opt_pack(
        r"A strategic trade sale to a corporate acquirer often commands a synergy premium and provides immediate full cash liquidity, though it may face antitrust scrutiny.",
        r"An initial public offering (IPO) allows the PE sponsor to immediately sell 100% of its shares on listing day without lock-up restrictions.",
        r"Sponsors exiting via IPO are typically subject to a 180-day lock-up and must sell remaining stakes gradually in public markets.",
        r"A secondary buyout (sponsor-to-sponsor) is viewed purely as a distressed liquidation option when a company is insolvent.",
        r"Secondary buyouts are common exits for healthy cash-generative businesses moving from a smaller PE firm to a larger buyout platform.",
        pos_cycle(25),
    )
    add_l1(
        questions, "L1-ALT-025", SUBJECT, mod2, "Private Equity Exits", "Exit Strategies",
        "Explain buyout strategies and value creation drivers.",
        r"Which statement accurately compares private equity exit mechanisms?",
        opts, ans,
        r"Selling to a strategic buyer can capture revenue or cost synergies unavailable to financial sponsors and delivers immediate full exit proceeds, whereas an IPO leaves the sponsor exposed to post-listing lock-up market risk.",
        dist,
    )

    # Topic 3: Real Estate & REITs (L1-ALT-026 to L1-ALT-037)
    mod3 = "Investments in Real Estate"

    # L1-ALT-026 (Calc): NOI calculation
    pgi, vac_r, other_inc, opex, debt_svc, capex = 2400.0, 0.08, 120.0, 780.0, 620.0, 150.0
    egi = pgi * (1 - vac_r) + other_inc
    noi26 = egi - opex
    w1_026 = noi26 - capex
    w2_026 = noi26 - debt_svc
    opts, ans, dist = opt_pack(
        rf"USD {noi26:,.0f} thousand",
        rf"USD {w1_026:,.0f} thousand",
        r"Improperly deducts capital expenditures (replacement reserves) above the NOI line.",
        rf"USD {w2_026:,.0f} thousand",
        r"Improperly subtracts mortgage debt service, which is a financing outflow rather than a property operating expense.",
        pos_cycle(26),
    )
    calc_ids.add("L1-ALT-026")
    add_l1(
        questions, "L1-ALT-026", SUBJECT, mod3, "Real Estate Valuation", "Net Operating Income (NOI)",
        "Calculate and interpret net operating income and capitalization rates.",
        rf"A commercial retail center reports (in USD thousands): Potential Gross Income = {pgi:,.0f}; Vacancy & Collection Loss = 8.0% of PGI; Ancillary Parking Income = {other_inc:,.0f}; Operating Expenses = {opex:,.0f}; Annual Mortgage Debt Service = {debt_svc:,.0f}; Capital Improvements = {capex:,.0f}. What is the property's Net Operating Income (NOI)?",
        opts, ans,
        rf"Effective Gross Income (EGI) $= {pgi:,.0f} \times (1 - 0.08) + {other_inc:,.0f} = {pgi * (1 - vac_r):,.0f} + {other_inc:,.0f} = \text{{USD }} {egi:,.0f}\text{{k}}$. Subtracting operating expenses gives $\text{{NOI}} = {egi:,.0f} - {opex:,.0f} = \text{{USD }} {noi26:,.0f}\text{{k}}$. Debt service and capital improvements are excluded from NOI.",
        dist,
    )

    # L1-ALT-027 (Calc): Direct Cap Valuation & Cap Rate
    noi27, cap_rate27 = 3.60, 0.0625
    val27 = noi27 / cap_rate27
    w1_027 = noi27 / (cap_rate27 + 0.01)
    w2_027 = noi27 * (1 + cap_rate27) / cap_rate27
    opts, ans, dist = opt_pack(
        rf"USD {val27:.2f} million",
        rf"USD {w1_027:.2f} million",
        r"Uses an incorrect 7.25% cap rate instead of the 6.25% market going-in cap rate.",
        rf"USD {w2_027:.2f} million",
        r"Multiplies forward Year 1 NOI by (1 + cap rate), double-counting first-year growth.",
        pos_cycle(27),
    )
    calc_ids.add("L1-ALT-027")
    add_l1(
        questions, "L1-ALT-027", SUBJECT, mod3, "Real Estate Valuation", "Direct Capitalization Method",
        "Calculate and interpret net operating income and capitalization rates.",
        rf"A stabilized multifamily property is projected to produce Year 1 NOI of USD {noi27:.2f} million. Comparable Class A apartment transactions indicate a going-in capitalization rate of 6.25%. Using the direct capitalization method, what is the indicated property value?",
        opts, ans,
        rf"Under direct capitalization, $V_0 = \frac{{\text{{NOI}}_1}}{{R_0}} = \frac{{{noi27:.2f}}}{{0.0625}} = \text{{USD }} {val27:.2f}\text{{M}}$.",
        dist,
    )

    # L1-ALT-028 (Calc): 3-year DCF + Terminal Reversion
    noi_y = [2.0, 2.1, 2.2]
    noi_y4 = 2.31
    exit_cap, sell_cost, disc_r = 0.065, 0.02, 0.085
    gross_rev = noi_y4 / exit_cap
    net_rev = gross_rev * (1 - sell_cost)
    pv_noi = sum(noi_y[t] / ((1 + disc_r) ** (t + 1)) for t in range(3))
    pv_rev = net_rev / ((1 + disc_r) ** 3)
    val28 = pv_noi + pv_rev
    w1_028 = pv_noi + (gross_rev / ((1 + disc_r) ** 3))
    w2_028 = pv_noi + ((noi_y[2] / exit_cap * (1 - sell_cost)) / ((1 + disc_r) ** 3))
    opts, ans, dist = opt_pack(
        rf"USD {val28:.2f} million",
        rf"USD {w1_028:.2f} million",
        r"Omits the 2.0% selling costs from the Year 3 reversion value.",
        rf"USD {w2_028:.2f} million",
        r"Capitalizes Year 3 NOI rather than forward Year 4 NOI to compute the Year 3 exit price.",
        pos_cycle(28),
    )
    calc_ids.add("L1-ALT-028")
    add_l1(
        questions, "L1-ALT-028", SUBJECT, mod3, "Real Estate Valuation", "Property DCF and Reversion",
        "Value commercial real estate using direct capitalization and discounted cash flow methods.",
        rf"An office property is expected to generate NOI (in USD millions) of {noi_y[0]:.2f} (Year 1), {noi_y[1]:.2f} (Year 2), {noi_y[2]:.2f} (Year 3), and {noi_y4:.2f} (Year 4). The investor applies an 8.50% discount rate, assumes an exit capitalization rate of 6.50% at the end of Year 3, and deducts 2.0% selling costs on reversion. What is the property's DCF valuation today?",
        opts, ans,
        rf"Net Year 3 reversion $= \frac{{\text{{NOI}}_4}}{{R_T}}(1 - 0.02) = \frac{{{noi_y4:.2f}}}{{0.065}} \times 0.98 = \text{{USD }} {net_rev:.2f}\text{{M}}$. Discounting at 8.50%: $\text{{PV}}(\text{{NOI}}_{{1\text{{-}}3}}) = \frac{{2.00}}{{1.085}} + \frac{{2.10}}{{1.085^2}} + \frac{{2.20}}{{1.085^3}} = {pv_noi:.2f}\text{{M}}$; $\text{{PV}}(\text{{Reversion}}) = \frac{{{net_rev:.2f}}}{{1.085^3}} = {pv_rev:.2f}\text{{M}}$. Total value $= {pv_noi:.2f} + {pv_rev:.2f} = \text{{USD }} {val28:.2f}\text{{M}}$.",
        dist,
    )

    # L1-ALT-029 (Calc): Debt Sizing LTV vs DSCR
    prop_v, noi29, max_ltv, min_dscr, debt_const = 40.0, 2.6, 0.70, 1.30, 0.08
    loan_ltv = prop_v * max_ltv  # 28.0M
    max_ds = noi29 / min_dscr  # 2.0M
    loan_dscr = max_ds / debt_const  # 25.0M
    bind_loan = min(loan_ltv, loan_dscr)
    w1_029 = loan_ltv
    w2_029 = (noi29 / debt_const) / min_dscr * 1.1  # wrong formula or unbinding
    w2_029 = noi29 / debt_const  # omits DSCR entirely
    opts, ans, dist = opt_pack(
        rf"USD {bind_loan:.2f} million",
        rf"USD {w1_029:.2f} million",
        r"Uses the 70% LTV loan ceiling without verifying that the minimum 1.30x DSCR constraint is more restrictive.",
        rf"USD {w2_029:.2f} million",
        r"Divides NOI directly by the mortgage constant without enforcing the 1.30x minimum DSCR coverage cushion.",
        pos_cycle(29),
    )
    calc_ids.add("L1-ALT-029")
    add_l1(
        questions, "L1-ALT-029", SUBJECT, mod3, "Real Estate Financing", "LTV and DSCR Loan Sizing",
        "Evaluate real estate debt financing constraints using LTV and DSCR.",
        rf"A commercial lender evaluates a mortgage on a USD {prop_v:.0f} million industrial warehouse generating USD {noi29:.2f} million in Year 1 NOI. Lender guidelines stipulate a maximum LTV of 70%, a minimum DSCR of 1.30x, and an annual mortgage debt constant of 8.00%. What is the maximum loan amount the lender will approve?",
        opts, ans,
        rf"LTV limit: $0.70 \times \text{{USD }} {prop_v:.0f}\text{{M}} = \text{{USD }} {loan_ltv:.2f}\text{{M}}$. DSCR limit: maximum annual debt service $= \frac{{{noi29:.2f}}}{{1.30}} = \text{{USD }} {max_ds:.2f}\text{{M}}$, supporting a loan of $\frac{{{max_ds:.2f}}}{{0.08}} = \text{{USD }} {loan_dscr:.2f}\text{{M}}$. The lender enforces the lower bound: $\min({loan_ltv:.2f}, {loan_dscr:.2f}) = \text{{USD }} {bind_loan:.2f}\text{{M}}$.",
        dist,
    )

    # L1-ALT-030 (Calc): Leveraged real estate ROE (1-year total return)
    price30, ltv30, rate30, noi30, app30 = 20.0, 0.60, 0.055, 1.40, 0.04
    debt30 = price30 * ltv30  # 12M IO loan
    eq30 = price30 - debt30  # 8M
    interest30 = debt30 * rate30  # 0.66M
    btcf30 = noi30 - interest30  # 0.74M
    cap_gain30 = price30 * app30  # 0.80M
    roe30 = (btcf30 + cap_gain30) / eq30 * 100
    w1_030 = btcf30 / eq30 * 100  # ignores appreciation
    w2_030 = (noi30 + cap_gain30) / price30 * 100  # unlevered return
    opts, ans, dist = opt_pack(
        rf"{roe30:.2f}%",
        rf"{w1_030:.2f}%",
        r"Measures only the cash-on-cash yield and omits the 4.0% property appreciation accruing to equity.",
        rf"{w2_030:.2f}%",
        r"Computes the unlevered total property return rather than the levered return on the USD 8 million equity.",
        pos_cycle(30),
    )
    calc_ids.add("L1-ALT-030")
    add_l1(
        questions, "L1-ALT-030", SUBJECT, mod3, "Real Estate Returns", "Leveraged Equity Return",
        "Evaluate real estate debt financing constraints using LTV and DSCR.",
        rf"An investor buys an apartment building for USD {price30:.0f} million using a 60% LTV interest-only loan at a 5.50% annual rate. In Year 1, the property produces USD {noi30:.2f} million in NOI and appreciates in value by 4.00%. What is the investor's total pre-tax leveraged return on equity in Year 1?",
        opts, ans,
        rf"Initial equity $= {price30:.0f} \times (1 - 0.60) = \text{{USD }} {eq30:.0f}\text{{M}}$; debt $= \text{{USD }} {debt30:.0f}\text{{M}}$. Annual interest $= {debt30:.0f} \times 5.50\% = \text{{USD }} {interest30:.2f}\text{{M}}$, leaving cash flow $= {noi30:.2f} - {interest30:.2f} = \text{{USD }} {btcf30:.2f}\text{{M}}$. Price appreciation $= {price30:.0f} \times 4\% = \text{{USD }} {cap_gain30:.2f}\text{{M}}$. Total equity return $= \frac{{{btcf30:.2f} + {cap_gain30:.2f}}}{{{eq30:.0f}}} = {roe30:.2f}\%$.",
        dist,
    )

    # L1-ALT-031 (Calc): REIT FFO
    ni31, da31, gain31, loss31, shares31 = 84.0, 46.0, 12.0, 3.0, 40.0
    ffo31 = ni31 + da31 - gain31 + loss31
    ffops31 = ffo31 / shares31
    w1_031 = (ni31 + da31 + gain31 - loss31) / shares31  # reverses signs on gains/losses
    w2_031 = (ni31 + da31) / shares31  # omits gains/losses
    opts, ans, dist = opt_pack(
        rf"USD {ffops31:.2f}",
        rf"USD {w1_031:.2f}",
        r"Adds gains and subtracts losses on property sales instead of reversing non-recurring capital gains/losses.",
        rf"USD {w2_031:.2f}",
        r"Adds back depreciation but fails to exclude non-operating gains and losses from property dispositions.",
        pos_cycle(31),
    )
    calc_ids.add("L1-ALT-031")
    add_l1(
        questions, "L1-ALT-031", SUBJECT, mod3, "REIT Valuation", "Funds From Operations (FFO)",
        "Calculate and interpret FFO, AFFO, and NAV per share for REITs.",
        rf"A residential REIT reports (in USD millions): GAAP Net Income = {ni31:.0f}; Real Estate Depreciation & Amortization = {da31:.0f}; Gains on Property Sales = {gain31:.0f}; Losses on Property Sales = {loss31:.0f}; Diluted Shares = {shares31:.0f} million. What is the REIT's FFO per share?",
        opts, ans,
        rf"$\text{{FFO}} = \text{{Net Income}} + \text{{Real Estate D\&A}} - \text{{Gains on Sales}} + \text{{Losses on Sales}} = {ni31:.0f} + {da31:.0f} - {gain31:.0f} + {loss31:.0f} = \text{{USD }} {ffo31:.0f}\text{{M}}$. Dividing by {shares31:.0f} million shares gives $\text{{FFO/share}} = \text{{USD }} {ffops31:.2f}$.",
        dist,
    )

    # L1-ALT-032 (Calc): REIT AFFO
    ffo32, sl_rent32, maint_capex32, leasing32, shares32 = 165.0, 9.0, 18.0, 6.0, 50.0
    affo32 = ffo32 - sl_rent32 - maint_capex32 - leasing32
    affops32 = affo32 / shares32
    w1_032 = (ffo32 + sl_rent32 - maint_capex32 - leasing32) / shares32  # adds sl_rent
    w2_032 = (ffo32 - sl_rent32) / shares32  # ignores capex & leasing
    opts, ans, dist = opt_pack(
        rf"USD {affops32:.2f}",
        rf"USD {w1_032:.2f}",
        r"Adds back straight-line rent adjustment instead of deducting non-cash accrued rental income.",
        rf"USD {w2_032:.2f}",
        r"Deducts non-cash straight-line rent but omits recurring maintenance CapEx and leasing commissions.",
        pos_cycle(32),
    )
    calc_ids.add("L1-ALT-032")
    add_l1(
        questions, "L1-ALT-032", SUBJECT, mod3, "REIT Valuation", "Adjusted FFO (AFFO)",
        "Calculate and interpret FFO, AFFO, and NAV per share for REITs.",
        rf"An office REIT reports FFO of USD {ffo32:.0f} million, non-cash straight-line rent revenue of USD {sl_rent32:.0f} million (accounting rent exceeding cash rent), recurring maintenance CapEx of USD {maint_capex32:.0f} million, and capitalized leasing commissions of USD {leasing32:.0f} million across {shares32:.0f} million shares. What is AFFO per share?",
        opts, ans,
        rf"$\text{{AFFO}} = \text{{FFO}} - \text{{Non-cash straight-line rent}} - \text{{Maintenance CapEx}} - \text{{Leasing Costs}} = {ffo32:.0f} - {sl_rent32:.0f} - {maint_capex32:.0f} - {leasing32:.0f} = \text{{USD }} {affo32:.0f}\text{{M}}$. Per share: $\frac{{{affo32:.0f}}}{{{shares32:.0f}}} = \text{{USD }} {affops32:.2f}$.",
        dist,
    )

    # L1-ALT-033 (Calc): REIT NAVPS & discount/premium
    cash_noi33, cap33, cash_assets33, debt33, shares33, price33 = 140.0, 0.056, 85.0, 985.0, 40.0, 36.0
    prop_v33 = cash_noi33 / cap33  # 2500
    nav33 = prop_v33 + cash_assets33 - debt33  # 1600
    navps33 = nav33 / shares33  # 40.00
    disc33 = (price33 - navps33) / navps33 * 100  # -10.0%
    w1_033 = (prop_v33 - debt33) / shares33
    w2_033 = (prop_v33 + cash_assets33) / shares33
    opts, ans, dist = opt_pack(
        rf"NAVPS = USD {navps33:.2f}; trading at a {abs(disc33):.1f}% discount",
        rf"NAVPS = USD {w1_033:.2f}; trading at a {abs((price33 - w1_033) / w1_033 * 100):.1f}% discount",
        r"Omits cash and other tangible non-real-estate assets when calculating total NAV.",
        rf"NAVPS = USD {w2_033:.2f}; trading at a {abs((price33 - w2_033) / w2_033 * 100):.1f}% discount",
        r"Reports gross asset value per share without deducting total debt and liabilities.",
        pos_cycle(33),
    )
    calc_ids.add("L1-ALT-033")
    add_l1(
        questions, "L1-ALT-033", SUBJECT, mod3, "REIT Valuation", "Net Asset Value Per Share (NAVPS)",
        "Calculate and interpret FFO, AFFO, and NAV per share for REITs.",
        rf"A retail REIT generates forward annualized cash NOI of USD {cash_noi33:.0f} million and faces a 5.60% market capitalization rate. It holds USD {cash_assets33:.0f} million in cash and receivables, carries USD {debt33:.0f} million in debt and other liabilities, has {shares33:.0f} million shares outstanding, and trades at USD {price33:.2f} per share. What is its NAVPS and valuation relative to NAV?",
        opts, ans,
        rf"Estimated real estate value $= \frac{{{cash_noi33:.0f}}}{{0.056}} = \text{{USD }} {prop_v33:,.0f}\text{{M}}$. $\text{{NAV}} = {prop_v33:,.0f} + {cash_assets33:.0f} - {debt33:.0f} = \text{{USD }} {nav33:,.0f}\text{{M}}$, so $\text{{NAVPS}} = \frac{{{nav33:,.0f}}}{{{shares33:.0f}}} = \text{{USD }} {navps33:.2f}$. At USD {price33:.2f}, the shares trade at $\frac{{{price33:.2f} - {navps33:.2f}}}{{{navps33:.2f}}} = {disc33:.1f}\%$ (a 10.0% discount to NAV).",
        dist,
    )

    # L1-ALT-034 (Calc): Cap rate buildup r - g
    rf34, rp34, g34 = 0.042, 0.043, 0.025
    cap34 = (rf34 + rp34 - g34) * 100
    w1_034 = (rf34 + rp34 + g34) * 100
    w2_034 = (rf34 + rp34) * 100
    opts, ans, dist = opt_pack(
        rf"{cap34:.2f}%",
        rf"{w1_034:.2f}%",
        r"Adds the NOI growth rate instead of subtracting it from the required return.",
        rf"{w2_034:.2f}%",
        r"Reports the discount rate (required return) rather than the capitalization rate.",
        pos_cycle(34),
    )
    calc_ids.add("L1-ALT-034")
    add_l1(
        questions, "L1-ALT-034", SUBJECT, mod3, "Real Estate Valuation", "Cap Rate Buildup Model",
        "Calculate and interpret net operating income and capitalization rates.",
        rf"For a prime logistics facility, the 10-year risk-free rate is 4.20%, the property-specific risk and illiquidity premium is 4.30%, and long-term expected NOI growth is 2.50% per year. What is the implied market capitalization rate?",
        opts, ans,
        rf"The required discount rate is $r = 4.20\% + 4.30\% = 8.50\%$. Subtracting constant NOI growth gives $R = r - g = 8.50\% - 2.50\% = {cap34:.2f}\%$.",
        dist,
    )

    # L1-ALT-035 (Concept): Real estate style spectrum
    opts, ans, dist = opt_pack(
        r"Core real estate targets fully leased, institutional-quality properties with low leverage and most return coming from current income.",
        r"Opportunistic real estate relies solely on stable existing leases with minimal leverage and zero development exposure.",
        r"Opportunistic strategies involve ground-up development, distressed repositioning, and high leverage, generating returns primarily from capital appreciation.",
        r"Value-add properties forbid physical renovations or lease-up initiatives and prohibit debt financing above 20% LTV.",
        r"Value-add strategies deliberately employ moderate leverage and active repositioning or re-tenanting to lift NOI.",
        pos_cycle(35),
    )
    add_l1(
        questions, "L1-ALT-035", SUBJECT, mod3, "Real Estate Strategies", "Core, Value-Add, and Opportunistic",
        "Describe real estate investment categories and risk-return profiles.",
        r"Which statement accurately describes the real estate risk-return style spectrum?",
        opts, ans,
        r"Core strategies invest in stabilized, high-occupancy prime assets with modest leverage (typically <=40%-50% LTV), deriving the majority of total return from predictable rental income.",
        dist,
    )

    # L1-ALT-036 (Concept): REIT structural requirements & sector sensitivity
    opts, ans, dist = opt_pack(
        r"REITs generally avoid corporate-level income tax by distributing at least 90% of taxable income, while hotel REITs exhibit shorter lease durations and higher cyclical sensitivity than industrial REITs.",
        r"REITs retain 100% of earnings internally to minimize external equity issuance and pay double corporate taxation.",
        r"To maintain pass-through tax status, REITs must distribute almost all (e.g., >=90%) taxable income as dividends, forcing frequent external capital raising.",
        r"Healthcare and industrial REITs reprice lease rates daily like hotels, giving them higher cash-flow volatility than hospitality assets.",
        r"Hotels effectively reprice room rates daily, making hospitality the shortest-duration and most economically cyclical REIT subsector.",
        pos_cycle(36),
    )
    add_l1(
        questions, "L1-ALT-036", SUBJECT, mod3, "REIT Characteristics", "Tax Status and Subsector Cycles",
        "Describe features and investment characteristics of REITs.",
        r"Which statement accurately characterizes REIT structures and subsector cash-flow profiles?",
        opts, ans,
        r"REITs enjoy pass-through tax status by meeting asset, income, and mandatory high dividend-payout tests (commonly >=90% of taxable income); operational lease lengths drive subsector cyclicality, with short-stay hotels far more cyclical than multi-year triple-net industrial leases.",
        dist,
    )

    # L1-ALT-037 (Concept): Appraisal vs Transaction vs REIT indices
    opts, ans, dist = opt_pack(
        r"Appraisal-based property indices exhibit lag and understated volatility relative to transaction-based and listed REIT indices.",
        r"Publicly traded REITs show zero short-term correlation with broader equity markets because underlying leases are illiquid.",
        r"Because REITs trade on stock exchanges, their short-term prices reflect broad equity market sentiment and exhibit higher short-term correlation with stocks than private real estate.",
        r"Repeat-sales transaction indices eliminate all sample-selection bias regardless of how infrequently properties trade.",
        r"Repeat-sales indices face thin-trading volatility and selection bias because only properties sold twice enter the sample.",
        pos_cycle(37),
    )
    add_l1(
        questions, "L1-ALT-037", SUBJECT, mod3, "Real Estate Indices", "Appraisal Lag and Index Comparison",
        "Compare public and private real estate indices and valuation methods.",
        r"When benchmarking private real estate against listed REITs, what distinguishes an appraisal-based index (such as the NCREIF Property Index)?",
        opts, ans,
        r"Periodic property appraisals incorporate past comparable sales and subjective smoothing, producing lagged turning points, lower reported volatility, and artificially low measured correlation with equities compared to transaction-based or REIT indices.",
        dist,
    )


def build_l1_part2(questions: list, calc_ids: set):
    """Build L1-ALT-038 through L1-ALT-075 (Infra/Timber, Hedge Funds, Commodities, Digital Assets/ESG)."""
    mod4 = "Infrastructure, Timberland, and Farmland"

    # L1-ALT-038 (Calc): Brownfield toll-road finite concession DCF
    traf, toll, opex38, r38 = 5.0, 4.0, 6.0, 0.08  # 20M rev - 6M opex = 14M/yr for 4 yrs
    cf38 = traf * toll - opex38
    pv38 = sum(cf38 / ((1 + r38) ** t) for t in range(1, 5))
    w1_038 = pv38 + (cf38 / r38) / ((1 + r38) ** 4)  # adds perpetual terminal value on concession
    w2_038 = sum((traf * toll) / ((1 + r38) ** t) for t in range(1, 5))  # forgets opex
    opts, ans, dist = opt_pack(
        rf"USD {pv38:.2f} million",
        rf"USD {w1_038:.2f} million",
        r"Incorrectly adds a perpetual terminal value even though ownership reverts to the grantor at Year 4.",
        rf"USD {w2_038:.2f} million",
        r"Discounts gross toll revenue rather than net operating cash flow after O&M expenses.",
        pos_cycle(38),
    )
    calc_ids.add("L1-ALT-038")
    add_l1(
        questions, "L1-ALT-038", SUBJECT, mod4, "Infrastructure Valuation", "Concession DCF",
        "Describe infrastructure investment characteristics and valuation.",
        rf"A brownfield toll-road concession has 4 years remaining before reverting to the government at zero terminal value. Annual traffic is {traf:.1f} million vehicles paying USD {toll:.2f} per trip, with annual O&M costs of USD {opex38:.1f} million (constant nominal cash flows). At an 8.00% discount rate, what is the concession's present value?",
        opts, ans,
        rf"Annual net cash flow $= {traf:.1f} \times {toll:.2f} - {opex38:.1f} = \text{{USD }} {cf38:.2f}\text{{M}}$. Discounting a 4-year annuity at 8.00% with zero terminal value gives $\text{{PV}} = {cf38:.2f} \times \frac{{1 - 1.08^{{-4}}}}{{0.08}} = \text{{USD }} {pv38:.2f}\text{{M}}$.",
        dist,
    )

    # L1-ALT-039 (Calc): Inflation-linked regulated asset real vs nominal valuation
    cf_real39, infl39, r_real39 = 12.0, 0.03, 0.05  # perpetual real cash flow growing at CPI
    # Exact Fisher nominal rate = (1+0.05)(1+0.03)-1 = 8.15%; growing perpetuity at infl = cf_real39*(1+infl) / (r_nom - infl) = 12*1.03 / (0.0815-0.03) = 12*1.03 / 0.0515 = 240.0!
    val39 = cf_real39 / r_real39  # 240.0M using real CF / real discount rate (Wait: real perpetuity paid end of yr 1 in yr-0 dollars = 12 / 0.05 = 240!)
    r_nom39 = (1 + r_real39) * (1 + infl39) - 1
    w1_039 = cf_real39 / r_nom39  # mixes real CF with nominal rate
    w2_039 = cf_real39 * (1 + infl39) / r_real39  # mixes nominal CF with real rate
    opts, ans, dist = opt_pack(
        rf"USD {val39:.2f} million",
        rf"USD {w1_039:.2f} million",
        r"Discounts real cash flows using the nominal discount rate, double-penalizing inflation.",
        rf"USD {w2_039:.2f} million",
        r"Applies the nominal growth-adjusted cash flow while still dividing by the real discount rate.",
        pos_cycle(39),
    )
    calc_ids.add("L1-ALT-039")
    add_l1(
        questions, "L1-ALT-039", SUBJECT, mod4, "Infrastructure Valuation", "Real vs. Nominal Discounting",
        "Describe infrastructure investment characteristics and valuation.",
        rf"A perpetual regulated water utility earns USD {cf_real39:.0f} million in Year 1 real cash flows (expressed in today's purchasing power, growing annually at the 3.00% inflation rate). If investors require a 5.00% real discount rate (consistent with an 8.15% nominal rate), what is the utility's present value?",
        opts, ans,
        rf"Consistent valuation matches real cash flows with the real discount rate: $V_0 = \frac{{{cf_real39:.0f}}}{{0.05}} = \text{{USD }} {val39:.2f}\text{{M}}$ (equivalently, nominal Year 1 cash flow ${cf_real39 * (1 + infl39):.2f}\text{{M}}$ divided by $r_{{\text{{nom}}}} - \pi = 8.15\% - 3.00\% = 5.15\%$ also gives USD 240.00M).",
        dist,
    )

    # L1-ALT-040 (Calc): Timberland return attribution
    bio_g, price_g, land_g, cost_drag = 0.06, 0.025, 0.02, 0.012
    # Compounded multiplicative total net return: (1+0.06)*(1+0.025)*(1+0.02) - 1 - 0.012? Wait: specify additive vs multiplicative clearly!
    # Cleanest CFA setup: gross biological volume +6.0%, timber price +2.5% (multiplicative biological*price on standing timber = 80% of asset, land 20% grows 2.0%), or simple additive components on total timberland asset!
    # Let's make standing timber 75% of asset value (growing at (1.06)*(1.025)-1) and bare land 25% of asset value (growing at 2.0%), minus 1.2% management cost, OR simple multiplicative (1+bio)*(1+price)+(land/net) stated explicitly!
    w_timb, w_land = 0.75, 0.25
    timb_ret = (1 + bio_g) * (1 + price_g) - 1
    tot_ret40 = (w_timb * timb_ret + w_land * land_g - cost_drag) * 100
    w1_040 = (timb_ret + land_g - cost_drag) * 100  # forgets portfolio weights
    w2_040 = (w_timb * bio_g + w_land * land_g - cost_drag) * 100  # omits timber price gain
    opts, ans, dist = opt_pack(
        rf"{tot_ret40:.2f}%",
        rf"{w1_040:.2f}%",
        r"Adds 100% of timber appreciation and 100% of land appreciation without weighting by their 75%/25% asset shares.",
        rf"{w2_040:.2f}%",
        r"Omits the 2.50% timber stumpage price appreciation on the standing timber component.",
        pos_cycle(40),
    )
    calc_ids.add("L1-ALT-040")
    add_l1(
        questions, "L1-ALT-040", SUBJECT, mod4, "Natural Resources", "Timberland Return Drivers",
        "Describe timberland and farmland investment characteristics and return drivers.",
        r"A timberland parcel's value comprises 75% standing timber and 25% underlying land. Over one year, biological tree volume grows 6.00%, stumpage prices rise 2.50%, land values appreciate 2.00%, and net management expenses equal 1.20% of total beginning asset value (zero harvest). What is the net annual return?",
        opts, ans,
        rf"Standing timber appreciates by $(1.06 \times 1.025) - 1 = {timb_ret * 100:.2f}\%$. Weighted gross return is $0.75({timb_ret * 100:.2f}\%) + 0.25(2.00\%) = {(w_timb * timb_ret + w_land * land_g) * 100:.2f}\%$. Subtracting 1.20% management costs yields ${tot_ret40:.2f}\%$.",
        dist,
    )

    # L1-ALT-041 (Calc): Farmland total return & real return
    lease_y41, land_app41, infl41 = 0.045, 0.055, 0.028
    nom_ret41 = lease_y41 + land_app41  # 10.0%
    real_ret41 = ((1 + nom_ret41) / (1 + infl41) - 1) * 100
    w1_041 = (nom_ret41 - infl41) * 100  # approximate Fisher
    w2_041 = ((1 + land_app41) / (1 + infl41) - 1) * 100  # ignores lease income
    # Ensure approximate Fisher differs enough: 7.20% vs 7.00% -> 20 bps difference!
    opts, ans, dist = opt_pack(
        rf"{real_ret41:.2f}%",
        rf"{w1_041:.2f}%",
        r"Uses the additive Fisher approximation rather than exact geometric deflation.",
        rf"{w2_041:.2f}%",
        r"Excludes the 4.50% annual cash farm lease income from the total return.",
        pos_cycle(41),
    )
    calc_ids.add("L1-ALT-041")
    add_l1(
        questions, "L1-ALT-041", SUBJECT, mod4, "Natural Resources", "Farmland Real Return",
        "Describe timberland and farmland investment characteristics and return drivers.",
        r"A Midwest row-crop farm leased to an operator yields a net annual cash rent of 4.50% of beginning value plus 5.50% land appreciation over the year (10.00% total nominal return). If CPI inflation is 2.80%, what is the exact real total return?",
        opts, ans,
        rf"Using the exact Fisher equation, $r_{{\text{{real}}}} = \frac{{1 + 0.1000}}{{1 + 0.0280}} - 1 = {real_ret41:.2f}\%$.",
        dist,
    )

    # L1-ALT-042 (Calc): PPP Availability payment project DSCR and Equity cash yield
    avail_pay, om_cost, debt_svc42, eq_inv42 = 42.0, 12.0, 22.5, 60.0
    cfads42 = avail_pay - om_cost  # 30.0
    dscr42 = cfads42 / debt_svc42
    eq_cf42 = cfads42 - debt_svc42
    eq_y42 = eq_cf42 / eq_inv42 * 100
    w1_042 = avail_pay / debt_svc42
    w2_042 = (cfads42 - debt_svc42 * 0.8) / debt_svc42
    opts, ans, dist = opt_pack(
        rf"DSCR = {dscr42:.2f}x; Equity cash yield = {eq_y42:.2f}%",
        rf"DSCR = {w1_042:.2f}x; Equity cash yield = {eq_y42:.2f}%",
        r"Computes DSCR using gross availability revenue rather than cash flow available for debt service (CFADS) after O&M costs.",
        rf"DSCR = {dscr42:.2f}x; Equity cash yield = {cfads42 / eq_inv42 * 100:.2f}%",
        r"Reports unlevered project cash yield on equity without deducting senior debt service.",
        pos_cycle(42),
    )
    calc_ids.add("L1-ALT-042")
    add_l1(
        questions, "L1-ALT-042", SUBJECT, mod4, "Infrastructure Financing", "PPP Availability Payments",
        "Describe infrastructure investment characteristics and valuation.",
        rf"A hospital PPP project receives an annual government availability payment of USD {avail_pay:.0f} million (assuming 100% uptime), incurs USD {om_cost:.0f} million in O&M costs, and pays USD {debt_svc42:.1f} million in senior debt service. If sponsor equity invested is USD {eq_inv42:.0f} million, what are the DSCR and annual equity cash yield?",
        opts, ans,
        rf"Cash Flow Available for Debt Service ($\text{{CFADS}}$) $= {avail_pay:.0f} - {om_cost:.0f} = \text{{USD }} {cfads42:.0f}\text{{M}}$. $\text{{DSCR}} = \frac{{{cfads42:.0f}}}{{{debt_svc42:.1f}}} = {dscr42:.2f}\text{{x}}$. Residual cash flow to equity $= {cfads42:.0f} - {debt_svc42:.1f} = \text{{USD }} {eq_cf42:.1f}\text{{M}}$, giving an equity yield of $\frac{{{eq_cf42:.1f}}}{{{eq_inv42:.0f}}} = {eq_y42:.2f}\%$.",
        dist,
    )

    # L1-ALT-043 (Concept): Greenfield vs Brownfield infrastructure
    opts, ans, dist = opt_pack(
        r"Brownfield infrastructure involves existing operating assets with established cash-flow histories, yielding immediate income and lower construction risk than greenfield projects.",
        r"Greenfield infrastructure generates stable cash yields from Day 1 with negligible permitting or cost-overrun risk.",
        r"Greenfield projects require multi-year construction and development phases with negative early cash flows and high execution risk.",
        r"Brownfield infrastructure assets are restricted solely to social facilities such as schools and cannot include toll roads or airports.",
        r"Brownfield refers to operational status regardless of whether the asset is economic (ports, toll roads) or social (hospitals, prisons).",
        pos_cycle(43),
    )
    add_l1(
        questions, "L1-ALT-043", SUBJECT, mod4, "Infrastructure Categories", "Greenfield vs. Brownfield",
        "Describe infrastructure investment characteristics and valuation.",
        r"How do brownfield infrastructure investments compare with greenfield infrastructure investments?",
        opts, ans,
        r"Brownfield assets are already operational and cash-generative, providing predictable inflation-linked distributions and lower development risk, whereas greenfield projects involve construction, permitting, and demand ramp-up risks.",
        dist,
    )

    # L1-ALT-044 (Concept): Economic vs Social infrastructure & revenue models
    opts, ans, dist = opt_pack(
        r"Economic infrastructure (e.g., toll roads, ports) typically carries demand or patronage risk unless structured as an availability-based concession.",
        r"Social infrastructure (e.g., public hospitals and courthouses) generates revenue primarily from commodity price volatility.",
        r"Social infrastructure generally relies on fixed long-term government availability payments tied to facility performance rather than commodity exposure.",
        r"Regulated utilities face uncapped market pricing and zero regulatory oversight over allowed return on equity.",
        r"Regulated utilities operate as natural monopolies whose allowed returns on their regulated asset base (RAB) are explicitly capped by regulators.",
        pos_cycle(44),
    )
    add_l1(
        questions, "L1-ALT-044", SUBJECT, mod4, "Infrastructure Categories", "Economic vs. Social Assets",
        "Describe infrastructure investment characteristics and valuation.",
        r"Which statement accurately differentiates infrastructure revenue models?",
        opts, ans,
        r"Economic infrastructure assets supporting trade and transport often depend on user traffic/volume demand, whereas social infrastructure typically operates under long-term availability-payment contracts backed by government counterparties.",
        dist,
    )

    # L1-ALT-045 (Concept): Timberland biological optionality
    opts, ans, dist = opt_pack(
        r"Unlike perishable agricultural crops, standing timber can be left unharvested during depressed lumber markets while trees continue gaining biological volume and higher-value sawtimber grade.",
        r"Timberland requires mandatory annual clear-cutting because standing trees lose all value if not harvested every 12 months.",
        r"Trees can remain " + "\"stored on the stump\"" + " for years, compounding biological volume until timber prices recover.",
        r"Timberland exhibits high positive beta to equity recessions because biological photosynthesis slows whenever the S&P 500 declines.",
        r"Biological tree growth depends on sunlight, rainfall, and silviculture—completely uncorrelated with financial market cycles.",
        pos_cycle(45),
    )
    add_l1(
        questions, "L1-ALT-045", SUBJECT, mod4, "Natural Resources", "Biological Storage Optionality",
        "Describe timberland and farmland investment characteristics and return drivers.",
        r"What makes timberland's harvest flexibility a unique real-option advantage relative to row-crop farmland?",
        opts, ans,
        r"Harvest timing can be deferred for years during weak pricing cycles; while deferred, trees continue growing physically (" + "\"storing on the stump\"" + ") and upgrading from lower-value pulpwood to higher-value sawtimber.",
        dist,
    )

    # Topic 5: Hedge Funds & Multi-Asset Strategies (L1-ALT-046 to L1-ALT-056)
    mod5 = "Hedge Fund Strategies"

    # L1-ALT-046 (Calc): Beta-neutral equity market neutral sizing
    long_not, beta_l, beta_s = 120.0, 1.15, 0.92
    short_not = (long_not * beta_l) / beta_s  # 150.0M
    gross_exp = long_not + short_not
    w1_046 = long_not  # dollar-neutral = 120 -> net beta != 0
    w2_046 = (long_not * beta_s) / beta_l  # inverted beta ratio
    opts, ans, dist = opt_pack(
        rf"USD {short_not:.2f} million short (Gross exposure: USD {gross_exp:.2f} million)",
        rf"USD {w1_046:.2f} million short (Gross exposure: USD {long_not + w1_046:.2f} million)",
        r"Constructs a dollar-neutral portfolio rather than beta-neutral, leaving positive residual market beta.",
        rf"USD {w2_046:.2f} million short (Gross exposure: USD {long_not + w2_046:.2f} million)",
        r"Inverts the beta ratio, further increasing positive net beta exposure instead of neutralizing it.",
        pos_cycle(46),
    )
    calc_ids.add("L1-ALT-046")
    add_l1(
        questions, "L1-ALT-046", SUBJECT, mod5, "Equity Strategies", "Beta-Neutral Positioning",
        "Analyze equity-related hedge fund strategies.",
        rf"An equity market-neutral manager buys USD {long_not:.0f} million of stocks with a portfolio beta of {beta_l:.2f} and wants to short a basket of stocks with a beta of {beta_s:.2f} so that net portfolio beta equals zero. What short notional amount and total gross exposure result?",
        opts, ans,
        rf"For zero net beta: $N_L \beta_L - N_S \beta_S = 0 \implies N_S = \frac{{{long_not:.0f} \times {beta_l:.2f}}}{{{beta_s:.2f}}} = \text{{USD }} {short_not:.2f}\text{{M}}$. Total gross exposure $= {long_not:.0f} + {short_not:.2f} = \text{{USD }} {gross_exp:.2f}\text{{M}}$.",
        dist,
    )

    # L1-ALT-047 (Calc): Merger arbitrage annualized return (cash deal)
    p_tgt, p_offer, days_close = 47.50, 50.00, 90
    spread47 = p_offer - p_tgt
    ret_period = spread47 / p_tgt
    ann_simple = ret_period * (365 / days_close) * 100
    w1_047 = ret_period * 100  # unannualized
    w2_047 = (spread47 / p_offer) * (365 / days_close) * 100  # divides by offer price
    opts, ans, dist = opt_pack(
        rf"{ann_simple:.2f}%",
        rf"{w1_047:.2f}%",
        r"Reports the 90-day holding-period spread return without annualizing.",
        rf"{w2_047:.2f}%",
        r"Divides the spread by the USD 50.00 offer price instead of the USD 47.50 invested capital.",
        pos_cycle(47),
    )
    calc_ids.add("L1-ALT-047")
    add_l1(
        questions, "L1-ALT-047", SUBJECT, mod5, "Event-Driven Strategies", "Merger Arbitrage Spread",
        "Analyze event-driven and relative value hedge fund strategies.",
        rf"An acquirer announces an all-cash takeover of a target at USD {p_offer:.2f} per share, expected to close in {days_close} days (365-day year). The target currently trades at USD {p_tgt:.2f}. Assuming no dividends and ignoring financing costs, what is the annualized simple return if the deal closes as scheduled?",
        opts, ans,
        rf"Per-share spread $= {p_offer:.2f} - {p_tgt:.2f} = \text{{USD }} {spread47:.2f}$, giving a 90-day return of $\frac{{{spread47:.2f}}}{{{p_tgt:.2f}}} = {ret_period * 100:.2f}\%$. Annualized simple return $= {ret_period * 100:.2f}\% \times \frac{{365}}{{90}} = {ann_simple:.2f}\%$.",
        dist,
    )

    # L1-ALT-048 (Calc): Convertible bond arbitrage conversion parity & delta hedge shares
    cb_par, cb_price, conv_ratio, stk_p, delta48, n_bonds = 1000.0, 1080.0, 25.0, 40.0, 0.65, 500
    conv_val = conv_ratio * stk_p  # 1000
    conv_prem_pct = (cb_price - conv_val) / conv_val * 100  # 8.0%
    short_shares = n_bonds * conv_ratio * delta48  # 500 * 25 * 0.65 = 8125
    w1_048 = n_bonds * conv_ratio  # 12500 (delta=1)
    w2_048 = n_bonds * delta48  # omits conversion ratio
    opts, ans, dist = opt_pack(
        rf"Conversion premium = {conv_prem_pct:.1f}%; Short {short_shares:,.0f} shares",
        rf"Conversion premium = {conv_prem_pct:.1f}%; Short {w1_048:,.0f} shares",
        r"Shorts 100% of the underlying conversion shares (delta = 1.0) rather than delta-hedging at 0.65.",
        rf"Conversion premium = {(cb_price - cb_par) / cb_par * 100:.1f}%; Short {w2_048:,.0f} shares",
        r"Omits the conversion ratio when sizing the short equity hedge.",
        pos_cycle(48),
    )
    calc_ids.add("L1-ALT-048")
    add_l1(
        questions, "L1-ALT-048", SUBJECT, mod5, "Relative Value Strategies", "Convertible Bond Arbitrage",
        "Analyze event-driven and relative value hedge fund strategies.",
        rf"A convertible arbitrage fund buys {n_bonds} convertible bonds (USD 1,000 par each) trading at USD {cb_price:,.0f} per bond, with a conversion ratio of {conv_ratio:.0f} shares and a bond delta of {delta48:.2f}. The underlying stock trades at USD {stk_p:.2f}. What are the conversion premium and the required number of short shares for a delta-neutral hedge?",
        opts, ans,
        rf"Conversion value per bond $= {conv_ratio:.0f} \times {stk_p:.2f} = \text{{USD }} {conv_val:,.0f}$. Conversion premium $= \frac{{{cb_price:,.0f} - {conv_val:,.0f}}}{{{conv_val:,.0f}}} = {conv_prem_pct:.1f}\%$. Delta-neutral short shares $= {n_bonds} \times {conv_ratio:.0f} \times {delta48:.2f} = {short_shares:,.0f}$ shares.",
        dist,
    )

    # L1-ALT-049 (Calc): Fixed-income duration-neutral 2s10s steepener
    l_2y_not, d_2y, d_10y, dy_2, dy_10 = 100.0, 1.9, 8.5, -0.0025, 0.0015  # 2y yield -25bp, 10y +15bp
    # DV01 neutral: Short 10y notional = 100 * (1.9 / 8.5)
    s_10y_not = l_2y_not * (d_2y / d_10y)
    # P&L: Long 2y gain = -100 * 1.9 * (-0.0025) = +0.475M; Short 10y gain = +s_10y * 8.5 * (+0.0015) = +0.285M
    pnl_2y = -l_2y_not * d_2y * dy_2
    pnl_10y = s_10y_not * d_10y * dy_10
    tot_pnl49 = pnl_2y + pnl_10y
    w1_049 = pnl_2y - pnl_10y
    w2_049 = -l_2y_not * d_2y * dy_2 + l_2y_not * d_10y * dy_10  # dollar-matched instead of DV01-matched
    opts, ans, dist = opt_pack(
        rf"USD {tot_pnl49:.3f} million",
        rf"USD {w1_049:.3f} million",
        r"Treats the short 10-year bond leg as generating a loss rather than a gain when 10-year yields rise.",
        rf"USD {w2_049:.3f} million",
        r"Uses equal USD 100M notionals on both legs instead of duration-weighting the 10-year short leg.",
        pos_cycle(49),
    )
    calc_ids.add("L1-ALT-049")
    add_l1(
        questions, "L1-ALT-049", SUBJECT, mod5, "Relative Value Strategies", "Duration-Neutral Yield Curve Steepener",
        "Analyze event-driven and relative value hedge fund strategies.",
        rf"A fixed-income relative value fund puts on a duration-neutral 2s10s curve steepener: long USD {l_2y_not:.0f} million of 2-year Treasuries (modified duration {d_2y:.1f}) and short enough 10-year Treasuries (modified duration {d_10y:.1f}) to match dollar duration. If 2-year yields fall 25 bps and 10-year yields rise 15 bps (ignoring carry/convexity), what is the total P&L?",
        opts, ans,
        rf"Duration-matched 10-year short notional $= {l_2y_not:.0f} \times \frac{{{d_2y:.1f}}}{{{d_10y:.1f}}} = \text{{USD }} {s_10y_not:.2f}\text{{M}}$ (dollar duration $= 190\text{{M}}$ on each leg). P&L from 2-year long $= 190 \times 0.0025 = +\text{{USD }} {pnl_2y:.3f}\text{{M}}$. P&L from 10-year short $= 190 \times 0.0015 = +\text{{USD }} {pnl_10y:.3f}\text{{M}}$. Total P&L $= +\text{{USD }} {tot_pnl49:.3f}\text{{M}}$.",
        dist,
    )

    # L1-ALT-050 (Calc): Leverage amplification & borrowing cost ROE
    eq50, lev50, gross_r50, borrow_r50 = 100.0, 3.0, 0.07, 0.04
    assets50 = eq50 * lev50  # 300
    debt50 = assets50 - eq50  # 200
    roe50 = (assets50 * gross_r50 - debt50 * borrow_r50) / eq50 * 100
    w1_050 = (lev50 * gross_r50) * 100  # ignores borrow cost
    w2_050 = ((assets50 * gross_r50 - assets50 * borrow_r50) / eq50) * 100  # charges borrow on entire 300 assets
    opts, ans, dist = opt_pack(
        rf"{roe50:.2f}%",
        rf"{w1_050:.2f}%",
        r"Multiplies unlevered return by 3.0x leverage without deducting financing costs on borrowed funds.",
        rf"{w2_050:.2f}%",
        r"Charges the 4.0% borrowing cost on total assets (USD 300M) rather than borrowed debt (USD 200M).",
        pos_cycle(50),
    )
    calc_ids.add("L1-ALT-050")
    add_l1(
        questions, "L1-ALT-050", SUBJECT, mod5, "Hedge Fund Leverage", "Leveraged Return on Equity",
        "Analyze hedge fund risk, leverage, and portfolio impact.",
        rf"A relative-value fund with USD {eq50:.0f} million of equity capital applies 3.0x asset-to-equity leverage (total long positions = USD {assets50:.0f} million) by borrowing USD {debt50:.0f} million at 4.00%. If the portfolio earns a 7.00% gross asset return, what is the levered return on equity before management fees?",
        opts, ans,
        rf"Gross portfolio gain $= {assets50:.0f} \times 7.00\% = \text{{USD }} {assets50 * gross_r50:.2f}\text{{M}}$. Borrowing cost $= {debt50:.0f} \times 4.00\% = \text{{USD }} {debt50 * borrow_r50:.2f}\text{{M}}$. Net return on USD {eq50:.0f}M equity $= \frac{{{assets50 * gross_r50:.2f} - {debt50 * borrow_r50:.2f}}}{{{eq50:.0f}}} = {roe50:.2f}\%$.",
        dist,
    )

    # L1-ALT-051 (Calc): Margin call / collateral trigger
    init_pos, init_debt, maint_m = 200.0, 140.0, 0.25
    # Price drops such that (Pos' - 140) / Pos' = 0.25 -> 0.75 * Pos' = 140 -> Pos' = 140 / 0.75 = 186.667 -> drop = (200 - 186.667)/200 = 6.67%
    trig_pos = init_debt / (1 - maint_m)
    drop_pct = (init_pos - trig_pos) / init_pos * 100
    w1_051 = (1 - maint_m) * (init_pos - init_debt) / init_pos * 100
    w2_051 = maint_m * 100
    opts, ans, dist = opt_pack(
        rf"{drop_pct:.2f}%",
        rf"{w1_051:.2f}%",
        r"Applies 75% to initial equity rather than solving for the maintenance margin boundary relative to the fixed USD 140M loan.",
        rf"{w2_051:.2f}%",
        r"Equates the required percentage drop directly to the 25% maintenance margin percentage.",
        pos_cycle(51),
    )
    calc_ids.add("L1-ALT-051")
    add_l1(
        questions, "L1-ALT-051", SUBJECT, mod5, "Hedge Fund Risk", "Margin Call Trigger",
        "Analyze hedge fund risk, leverage, and portfolio impact.",
        rf"A hedge fund buys USD {init_pos:.0f} million of securities funded with USD 60 million of equity and USD {init_debt:.0f} million of prime-broker margin debt, subject to a 25% maintenance margin requirement. What percentage decline in portfolio market value triggers a margin call?",
        opts, ans,
        rf"At the margin call boundary, $\frac{{V - {init_debt:.0f}}}{{V}} = 0.25 \implies V = \frac{{{init_debt:.0f}}}{{0.75}} = \text{{USD }} {trig_pos:.2f}\text{{M}}$. This represents a market decline of $\frac{{{init_pos:.0f} - {trig_pos:.2f}}}{{{init_pos:.0f}}} = {drop_pct:.2f}\%$.",
        dist,
    )

    # L1-ALT-052 (Calc): Portfolio Sharpe impact when adding uncorrelated CTA
    # Core portfolio: E[R]=8%, rf=3%, sig=12% -> Sharpe = 5/12 = 0.4167
    # Blend 85% Core + 15% CTA (E[R]=8%, sig=12%, rho=-0.10)
    w_c, w_cta, er_c, er_cta, rf52, sig_c, sig_cta, rho52 = 0.85, 0.15, 0.08, 0.08, 0.03, 0.12, 0.12, -0.10
    er_p = w_c * er_c + w_cta * er_cta
    var_p = (w_c * sig_c) ** 2 + (w_cta * sig_cta) ** 2 + 2 * w_c * w_cta * sig_c * sig_cta * rho52
    sig_p = math.sqrt(var_p)
    sr_before = (er_c - rf52) / sig_c
    sr_after = (er_p - rf52) / sig_p
    w1_052 = (er_p - rf52) / (w_c * sig_c + w_cta * sig_cta)
    w2_052 = sr_before
    opts, ans, dist = opt_pack(
        rf"Portfolio volatility falls to {sig_p * 100:.2f}% and Sharpe ratio rises from {sr_before:.2f} to {sr_after:.2f}",
        rf"Portfolio volatility stays at {sig_c * 100:.2f}% and Sharpe ratio remains unchanged at {w2_052:.2f}",
        r"Ignores the diversification benefit from the negative -0.10 correlation between the core portfolio and the CTA sleeve.",
        rf"Portfolio volatility equals {sig_c * 100:.2f}% and Sharpe ratio equals {w1_052:.2f}",
        r"Computes weighted average volatility assuming +1.0 correlation instead of accounting for -0.10 correlation.",
        pos_cycle(52),
    )
    calc_ids.add("L1-ALT-052")
    add_l1(
        questions, "L1-ALT-052", SUBJECT, mod5, "Portfolio Allocation", "CTA Diversification Effect",
        "Analyze hedge fund risk, leverage, and portfolio impact.",
        r"An institutional portfolio has an expected return of 8.0%, volatility of 12.0%, and faces a 3.0% risk-free rate. Adding a 15% allocation to a managed futures (CTA) fund (expected return 8.0%, volatility 12.0%, correlation -0.10 with the existing portfolio) shifts weights to 85% core / 15% CTA. What happens to portfolio volatility and Sharpe ratio?",
        opts, ans,
        rf"Portfolio expected return remains $8.0\%$. Portfolio variance $= (0.85 \times 0.12)^2 + (0.15 \times 0.12)^2 + 2(0.85)(0.15)(0.12)(0.12)(-0.10) = {var_p:.6f}$, so $\sigma_p = {sig_p * 100:.2f}\%$. Thus, Sharpe ratio rises from $\frac{{8.0 - 3.0}}{{12.0}} = {sr_before:.2f}$ to $\frac{{8.0 - 3.0}}{{{sig_p * 100:.2f}}} = {sr_after:.2f}$.",
        dist,
    )

    # L1-ALT-053 (Concept): Event-driven left-tail risk
    opts, ans, dist = opt_pack(
        r"Merger arbitrage exhibits a payoff resembling a short put option: small, steady gains when deals close paired with sharp left-tail losses when deals break during market stress.",
        r"Merger arbitrage produces strongly positive skewness because broken deals automatically pay higher breakup premiums to target shareholders.",
        r"When a takeover fails, the target share price typically plunges back toward its pre-announcement level, causing large asymmetric losses.",
        r"Distressed debt investing avoids equity-like downside because bankrupt companies immediately repay unsecured claims in cash.",
        r"Distressed investors often receive restructured equity and bear reorganization, liquidity, and valuation uncertainty.",
        pos_cycle(53),
    )
    add_l1(
        questions, "L1-ALT-053", SUBJECT, mod5, "Event-Driven Strategies", "Payoff Skewness",
        "Analyze event-driven and relative value hedge fund strategies.",
        r"Why do event-driven strategies such as merger arbitrage display negative return skewness?",
        opts, ans,
        r"Successful deals yield a capped arbitrage spread, whereas failed deals—often clustered during systemic credit or regulatory shocks—cause steep price drops back toward standalone target value, mimicking a short out-of-the-money put payoff.",
        dist,
    )

    # L1-ALT-054 (Concept): Global macro vs Managed futures (CTA)
    opts, ans, dist = opt_pack(
        r"Systematic CTAs use rule-based trend-following models across futures markets and historically deliver positive skewness (" + "\"crisis alpha\"" + ") during sustained equity drawdowns.",
        r"Global macro funds are strictly prohibited from trading sovereign fixed income or G10 currencies.",
        r"Rates, currencies, and sovereign debt are core liquid instruments for global macro managers.",
        r"Trend-following CTAs perform best during choppy, range-bound, mean-reverting markets with rapid reversals.",
        r"Trend-following strategies suffer whipsaw losses in directionless, mean-reverting markets and thrive in sustained directional trends.",
        pos_cycle(54),
    )
    add_l1(
        questions, "L1-ALT-054", SUBJECT, mod5, "Macro & CTA Strategies", "Global Macro vs. Managed Futures",
        "Compare opportunistic hedge fund strategies including global macro and managed futures.",
        r"Which statement accurately describes systematic managed futures (CTA) strategies relative to global macro?",
        opts, ans,
        r"Systematic CTAs deploy algorithmic trend-following and momentum rules across liquid commodity, equity, currency, and bond futures, frequently generating convex positive returns during prolonged market crises.",
        dist,
    )

    # L1-ALT-055 (Concept): Conditional correlation & tail behavior
    opts, ans, dist = opt_pack(
        r"During liquidity crises, strategies such as convertible arbitrage and fixed-income relative value often experience correlation spikes toward +1.0 as leveraged funds unwind simultaneously.",
        r"Hedge fund diversification benefits remain completely invariant across normal and stressed market regimes.",
        r"Correlations across credit and arbitrage strategies rise sharply in systemic liquidity shocks (conditional correlation instability).",
        r"Positive excess kurtosis indicates thinner tails and fewer extreme outlier returns than a normal distribution.",
        r"Excess kurtosis reflects fat tails (leptokurtic distributions), indicating higher probability of extreme return events than predicted by normality.",
        pos_cycle(55),
    )
    add_l1(
        questions, "L1-ALT-055", SUBJECT, mod5, "Hedge Fund Risk", "Conditional Correlation and Kurtosis",
        "Analyze hedge fund risk, leverage, and portfolio impact.",
        r"What risk phenomenon limits reliance on unconditional historical variance-covariance matrices for relative-value hedge funds?",
        opts, ans,
        r"Leverage and crowded positioning cause conditional correlations to surge during market selloffs, while negative skewness and high excess kurtosis create far larger tail losses than normal-distribution Sharpe or VaR models imply.",
        dist,
    )

    # L1-ALT-056 (Concept): Hedge fund index biases
    opts, ans, dist = opt_pack(
        r"Liquidation bias occurs when failing funds stop reporting their final severe drawdown months prior to closure, causing index returns to appear artificially high.",
        r"Self-reporting (selection) bias reduces reported index returns because only the worst-performing funds volunteer data.",
        r"Selection bias inflates index returns because top performers choose to report to attract institutional assets while weak funds abstain.",
        r"Backfill bias eliminates all pre-inclusion returns from a fund's database record.",
        r"Backfill (instant-history) bias includes favorable prior track-record returns retroactively upon database entry, biasing historical returns upward.",
        pos_cycle(56),
    )
    add_l1(
        questions, "L1-ALT-056", SUBJECT, mod5, "Hedge Fund Benchmarks", "Database Biases",
        "Explain issues in measuring and evaluating returns of alternative investments.",
        r"Which hedge fund index bias arises specifically from failing funds ceasing data submissions before final losses are realized?",
        opts, ans,
        r"Liquidation (or delisting) bias occurs when distressed managers stop reporting ahead of fund wind-down, omitting terminal losses and biasing aggregate index performance upward.",
        dist,
    )

    # Topic 6: Commodities (L1-ALT-057 to L1-ALT-066)
    mod6 = "Investments in Commodities"

    # L1-ALT-057 (Calc): Commodity futures total return (multiplicative)
    r_spot57, r_roll57, r_coll57 = 0.06, -0.025, 0.045
    tot57_mult = ((1 + r_spot57 + r_roll57) * (1 + r_coll57) - 1) * 100
    # Wait: check both standard conventions: (1+spot)*(1+roll)*(1+coll)-1 vs (1+spot+roll)*(1+coll)-1!
    # Wait: (1+0.06)*(1-0.025)*(1+0.045)-1 = 7.999%, while (1+0.035)*(1.045)-1 = 8.1575%, while additive = 8.00%!
    # Let's make the question explicitly use additive sum OR geometric product clearly, with distractors off by wrong sign on roll yield (+2.5%) and omitted collateral!
    tot57_add = (r_spot57 + r_roll57 + r_coll57) * 100  # 8.00%
    w1_057 = (r_spot57 - r_roll57 + r_coll57) * 100  # reverses roll sign = 13.00%
    w2_057 = (r_spot57 + r_roll57) * 100  # omits collateral = 3.50%
    opts, ans, dist = opt_pack(
        rf"{tot57_add:.2f}%",
        rf"{w1_057:.2f}%",
        r"Treats the contango roll return as positive (+2.50%) rather than negative (-2.50%).",
        rf"{w2_057:.2f}%",
        r"Calculates only the excess futures return (spot plus roll) and omits the T-bill collateral yield.",
        pos_cycle(57),
    )
    calc_ids.add("L1-ALT-057")
    add_l1(
        questions, "L1-ALT-057", SUBJECT, mod6, "Commodity Returns", "Total Return Decomposition",
        "Calculate and interpret components of commodity futures total return.",
        r"A fully collateralized commodity futures portfolio generates a spot (price) return of +6.00%, a roll return of -2.50%, and a Treasury-bill collateral return of +4.50% over one year. Using the additive return decomposition, what is the portfolio's total return?",
        opts, ans,
        r"Under the additive decomposition, $\text{Total Return} = \text{Price Return} + \text{Roll Return} + \text{Collateral Return} = 6.00\% - 2.50\% + 4.50\% = 8.00\%$.",
        dist,
    )

    # L1-ALT-058 (Calc): Roll yield calculation
    f_near58, f_far58 = 84.00, 79.80
    roll58 = (f_near58 - f_far58) / f_near58 * 100  # +5.00%
    w1_058 = -roll58  # -5.00%
    w2_058 = ((f_near58 - f_far58) / 100.0) * 100  # raw dollar spread as %
    opts, ans, dist = opt_pack(
        rf"+{roll58:.2f}% (backwardation)",
        rf"{w1_058:.2f}% (contango)",
        r"Reverses the contract ordering and misidentifies a downward-sloping curve as contango.",
        rf"+{w2_058:.2f}% (backwardation)",
        r"Reports the raw USD 4.20 price differential as a percentage without dividing by the near-term contract price.",
        pos_cycle(58),
    )
    calc_ids.add("L1-ALT-058")
    add_l1(
        questions, "L1-ALT-058", SUBJECT, mod6, "Commodity Futures", "Roll Yield and Curve Shape",
        "Calculate and interpret components of commodity futures total return.",
        rf"A long commodity investor rolls out of an expiring front-month futures contract priced at USD {f_near58:.2f} into a second-month futures contract priced at USD {f_far58:.2f}. What is the roll return for this roll period and the shape of the futures curve?",
        opts, ans,
        rf"Because the near-month futures price (USD {f_near58:.2f}) exceeds the farther-month price (USD {f_far58:.2f}), the curve is in backwardation. Using the CFA roll return formula: $\frac{{F_{{\text{{near}}}} - F_{{\text{{far}}}}}}{{F_{{\text{{near}}}}}} = \frac{{{f_near58:.2f} - {f_far58:.2f}}}{{{f_near58:.2f}}} = +{roll58:.2f}\%$.",
        dist,
    )

    # L1-ALT-059 (Calc): Cost-of-carry continuous futures pricing
    s59, r59, u59, y59, t59 = 95.0, 0.045, 0.035, 0.060, 0.5
    f59 = s59 * math.exp((r59 + u59 - y59) * t59)
    w1_059 = s59 * math.exp((r59 - u59 + y59) * t59)  # swaps signs of u and y
    w2_059 = s59 * math.exp((r59 + u59) * t59)  # omits convenience yield
    opts, ans, dist = opt_pack(
        rf"USD {f59:.2f}",
        rf"USD {w1_059:.2f}",
        r"Reverses the signs of storage cost and convenience yield, subtracting storage and adding convenience yield.",
        rf"USD {w2_059:.2f}",
        r"Omits the 6.00% annualized convenience yield from the cost-of-carry exponent.",
        pos_cycle(59),
    )
    calc_ids.add("L1-ALT-059")
    add_l1(
        questions, "L1-ALT-059", SUBJECT, mod6, "Commodity Pricing", "No-Arbitrage Futures Pricing",
        "Calculate commodity futures prices using storage costs and convenience yield.",
        rf"A commodity has a spot price of USD {s59:.2f}, a continuously compounded risk-free rate of 4.50%, annualized storage cost of 3.50%, and an annualized convenience yield of 6.00%. What is the theoretical 6-month ($T = 0.5$) futures price?",
        opts, ans,
        rf"Under continuous compounding, $F_0 = S_0 e^{{(r + u - y)T}} = {s59:.2f} \times e^{{(0.045 + 0.035 - 0.060) \times 0.5}} = {s59:.2f} \times e^{{0.010}} = \text{{USD }} {f59:.2f}$.",
        dist,
    )

    # L1-ALT-060 (Calc): Implied convenience yield
    s60, f60, r60, u60, t60 = 200.0, 196.0, 0.04, 0.02, 0.5
    # F = S * exp((r + u - y)*T) -> ln(F/S)/T = r + u - y -> y = r + u - ln(F/S)/T
    y60 = (r60 + u60 - math.log(f60 / s60) / t60) * 100
    w1_060 = (r60 + u60 + math.log(f60 / s60) / t60) * 100  # wrong sign on ln(F/S)
    w2_060 = (r60 - u60 - math.log(f60 / s60) / t60) * 100  # wrong sign on storage
    opts, ans, dist = opt_pack(
        rf"{y60:.2f}%",
        rf"{w1_060:.2f}%",
        r"Adds $\ln(F_0/S_0)/T$ instead of subtracting it when isolating convenience yield.",
        rf"{w2_060:.2f}%",
        r"Subtracts storage cost instead of adding it to the risk-free carrying rate.",
        pos_cycle(60),
    )
    calc_ids.add("L1-ALT-060")
    add_l1(
        questions, "L1-ALT-060", SUBJECT, mod6, "Commodity Pricing", "Implied Convenience Yield",
        "Calculate commodity futures prices using storage costs and convenience yield.",
        rf"A metal trades at a spot price of USD {s60:.2f} and a 6-month ($T = 0.5$) futures price of USD {f60:.2f}. With a continuously compounded risk-free rate of 4.00% and annualized storage costs of 2.00%, what is the implied annualized convenience yield?",
        opts, ans,
        rf"From $F_0 = S_0 e^{{(r + u - y)T}}$, solving for $y$ yields $y = r + u - \frac{{\ln(F_0 / S_0)}}{{T}} = 0.04 + 0.02 - \frac{{\ln(196/200)}}{{0.5}} = 0.06 - (-0.0404) = {y60:.2f}\%$.",
        dist,
    )

    # L1-ALT-061 (Calc): Collateral yield with initial margin + excess T-bill reserve
    # Actually: 100M portfolio buys 100M notional futures; 10% posted as initial margin (also T-bills earning 4.8%) and 90% in T-bill portfolio (4.8%) + margin fee 0% or simple T-bill return
    # Let's test effective collateral yield when margin earns 4.2% (after prime haircut) on 15% margin and 85% earns 4.8% T-bill yield
    m_w, m_r, tb_w, tb_r = 0.15, 0.042, 0.85, 0.048
    coll_y61 = (m_w * m_r + tb_w * tb_r) * 100
    w1_061 = (tb_w * tb_r) * 100  # forgets initial margin also earns T-bill interest
    w2_061 = ((m_r + tb_r) / 2) * 100  # unweighted 50/50 average
    opts, ans, dist = opt_pack(
        rf"{coll_y61:.2f}%",
        rf"{w1_061:.2f}%",
        r"Assumes initial margin T-bills earn 0% rather than the 4.20% T-bill custody rate.",
        rf"{w2_061:.2f}%",
        r"Computes an unweighted average of the two rates instead of weighting 15%/85% by capital allocation.",
        pos_cycle(61),
    )
    calc_ids.add("L1-ALT-061")
    add_l1(
        questions, "L1-ALT-061", SUBJECT, mod6, "Commodity Returns", "Collateral Yield Calculation",
        "Calculate and interpret components of commodity futures total return.",
        r"A fully collateralized commodity futures fund posts 15% of capital as initial margin in Treasury bills yielding 4.20% (net of broker custody spread) and holds the remaining 85% in unencumbered Treasury bills yielding 4.80%. What is the fund's annual collateral yield?",
        opts, ans,
        rf"Weighted collateral yield $= (0.15 \times 4.20\%) + (0.85 \times 4.80\%) = {m_w * m_r * 100:.2f}\% + {tb_w * tb_r * 100:.2f}\% = {coll_y61:.2f}\%$.",
        dist,
    )

    # L1-ALT-062 (Calc): Calendar spread P&L
    # Long 3M at 75.00, Short 6M at 77.50 (initial spread = 2.50 contango). Later 3M = 78.20, 6M = 79.10 (spread narrows to 0.90).
    # Long leg P&L = +3.20; Short leg P&L = -1.60; Net P&L per unit = +1.60 * 1000 bbl/contract * 50 contracts = +80,000 USD
    l0, s0, l1, s1, bbl, n_c = 75.00, 77.50, 78.20, 79.10, 1000, 50
    pnl62 = ((l1 - l0) + (s0 - s1)) * bbl * n_c
    w1_062 = ((l1 - l0) + (s1 - s0)) * bbl * n_c  # treats short leg as long
    w2_062 = ((s0 - s1)) * bbl * n_c  # only counts short leg
    opts, ans, dist = opt_pack(
        rf"+USD {pnl62:,.0f}",
        rf"+USD {w1_062:,.0f}",
        r"Treats both contracts as long positions instead of subtracting the loss on the short 6-month leg.",
        rf"-USD {abs(w2_062):,.0f}",
        r"Captures only the loss on the short 6-month leg and omits the gain on the long 3-month leg.",
        pos_cycle(62),
    )
    calc_ids.add("L1-ALT-062")
    add_l1(
        questions, "L1-ALT-062", SUBJECT, mod6, "Commodity Strategies", "Calendar Spread P&L",
        "Explain commodity market participants, curve dynamics, and trading strategies.",
        rf"A trader enters 50 contracts of a bull calendar spread (1,000 barrels per contract): long 3-month crude futures at USD {l0:.2f} and short 6-month crude futures at USD {s0:.2f}. Two weeks later, the 3-month contract trades at USD {l1:.2f} and the 6-month contract trades at USD {s1:.2f}. What is the trader's net profit or loss?",
        opts, ans,
        rf"Long 3-month leg gain $= {l1:.2f} - {l0:.2f} = +\text{{USD }} {l1 - l0:.2f}$/bbl. Short 6-month leg P&L $= {s0:.2f} - {s1:.2f} = -\text{{USD }} {s1 - s0:.2f}$/bbl. Net spread profit $= +{l1 - l0 - (s1 - s0):.2f}$/bbl. Across $50 \times 1,000 = 50,000$ bbls, total profit $= +\text{{USD }} {pnl62:,.0f}$.",
        dist,
    )

    # L1-ALT-063 (Calc): Diversification / Rebalancing return in equal-weight commodity index
    # Erb & Harvey variance-drain/rebalancing yield: R_div = 0.5 * (avg_var - port_var)
    # 4 commodities each sigma = 28%, pairwise correlation = 0.10
    n63, sig63, rho63 = 4, 0.28, 0.10
    avg_var = sig63 ** 2  # 0.0784
    port_var = avg_var / n63 + (1 - 1 / n63) * rho63 * avg_var  # 0.0784/4 + 0.75*0.1*0.0784 = 0.0196 + 0.00588 = 0.02548
    rebal_y = 0.5 * (avg_var - port_var) * 100
    w1_063 = (avg_var - port_var) * 100  # omits 0.5 factor
    w2_063 = (0.5 * avg_var) * 100  # forgets portfolio variance subtraction
    opts, ans, dist = opt_pack(
        rf"{rebal_y:.2f}%",
        rf"{w1_063:.2f}%",
        r"Omits the 1/2 factor in the geometric diversification return approximation.",
        rf"{w2_063:.2f}%",
        r"Computes half of individual asset variance without subtracting total portfolio variance.",
        pos_cycle(63),
    )
    calc_ids.add("L1-ALT-063")
    add_l1(
        questions, "L1-ALT-063", SUBJECT, mod6, "Commodity Indices", "Rebalancing Diversification Return",
        "Calculate and interpret components of commodity futures total return.",
        r"An equally weighted index holds 4 commodity futures sleeves, each with 28.0% annual return volatility and pairwise correlation of 0.10. Using the standard variance-reduction approximation $\frac{1}{2}(\bar{\sigma}^2 - \sigma_p^2)$, what is the estimated annualized rebalancing (diversification) return?",
        opts, ans,
        rf"Individual asset variance $\bar{{\sigma}}^2 = 0.28^2 = {avg_var:.4f}$. Portfolio variance $\sigma_p^2 = \frac{{\bar{{\sigma}}^2}}{{4}} + \frac{{3}}{{4}}(0.10)\bar{{\sigma}}^2 = {port_var:.5f}$. Rebalancing return $\approx 0.5 \times ({avg_var:.4f} - {port_var:.5f}) = {rebal_y:.2f}\%$.",
        dist,
    )

    # L1-ALT-064 (Concept): Contango vs Backwardation & Hedging Pressure
    opts, ans, dist = opt_pack(
        r"When commercial producers heavily short futures to lock in selling prices while speculative long demand is scarce, futures prices tend to trade below expected future spot prices (normal backwardation).",
        r"High physical storage costs and abundant inventories drive the futures curve into steep backwardation.",
        r"Abundant inventory lowers convenience yield toward zero while storage costs push futures prices above spot (contango).",
        r"Contango always yields positive roll returns for passive long-only commodity futures investors.",
        r"In contango, rolling from cheaper expiring contracts into costlier deferred contracts creates negative roll yield.",
        pos_cycle(64),
    )
    add_l1(
        questions, "L1-ALT-064", SUBJECT, mod6, "Commodity Curves", "Hedging Pressure and Theory of Storage",
        "Explain commodity market participants, curve dynamics, and trading strategies.",
        r"Which explanation best aligns with Keynes' hedging pressure hypothesis and commodity term-structure dynamics?",
        opts, ans,
        r"Under hedging pressure, net short hedging by commodity producers creates a risk premium that depresses futures prices below expected future spot prices, allowing long speculators to earn positive roll returns in backwardation.",
        dist,
    )

    # L1-ALT-065 (Concept): Commodity sector supply/demand fundamentals
    opts, ans, dist = opt_pack(
        r"Agricultural grain curves exhibit seasonal price patterns tied to harvest schedules and weather shocks, whereas industrial metals respond strongly to global manufacturing cycles and mine capex lags.",
        r"Electricity can be cheaply warehoused across seasons in large tanks like crude oil, keeping power prices flat.",
        r"Electricity cannot be stored economically at grid scale, causing extreme seasonal and intraday price spikes.",
        r"Crude oil supply can expand instantaneously within days regardless of multi-year offshore drilling lead times.",
        r"Upstream oil exploration and production carry multi-year investment lags, making short-run supply highly price-inelastic.",
        pos_cycle(65),
    )
    add_l1(
        questions, "L1-ALT-065", SUBJECT, mod6, "Commodity Fundamentals", "Sector Supply and Demand",
        "Explain commodity market participants, curve dynamics, and trading strategies.",
        r"Which statement accurately contrasts supply-demand fundamentals across major commodity sectors?",
        opts, ans,
        r"Grains display weather-driven and planting/harvest seasonality, industrial metals track industrial capex cycles, and non-storable electricity experiences acute spot spikes compared to storable energy commodities.",
        dist,
    )

    # L1-ALT-066 (Concept): Futures vs Commodity Producer Equities vs Physical
    opts, ans, dist = opt_pack(
        r"Commodity producer equities often hedge output prices and carry general equity-market beta and operational leverage, diluting pure spot commodity inflation sensitivity compared to futures.",
        r"Buying physical crude oil directly eliminates all storage, insurance, and transportation expenses.",
        r"Physical ownership incurs direct storage, insurance, transport, and spoilage costs that futures avoid.",
        r"Commodity futures pay contractual quarterly cash dividends based on corporate earnings.",
        r"Futures contracts do not pay corporate dividends; collateral yield arises solely from underlying cash/T-bill collateral.",
        pos_cycle(66),
    )
    add_l1(
        questions, "L1-ALT-066", SUBJECT, mod6, "Commodity Access", "Futures vs. Natural Resource Equities",
        "Explain commodity market participants, curve dynamics, and trading strategies.",
        r"Why do institutional investors seeking direct inflation protection generally prefer commodity futures over commodity-producer stocks?",
        opts, ans,
        r"Commodity producers frequently hedge forward production and exhibit broad stock-market beta, management risk, and capital-structure effects, whereas futures deliver direct commodity price and roll exposure without physical storage logistics.",
        dist,
    )

    # Topic 7: Digital Assets, Shorting & Sustainability (L1-ALT-067 to L1-ALT-075)
    mod7 = "Digital Assets, Shorting, and Sustainability in Alternatives"

    # L1-ALT-067 (Calc): Staking nominal vs real dilution-adjusted yield
    nom_y67, infl67 = 0.084, 0.052
    real_y67 = ((1 + nom_y67) / (1 + infl67) - 1) * 100
    w1_067 = (nom_y67 + infl67) * 100
    w2_067 = nom_y67 * 100
    opts, ans, dist = opt_pack(
        rf"{real_y67:.2f}%",
        rf"{w1_067:.2f}%",
        r"Adds token supply inflation to the nominal staking APR instead of deflating for supply dilution.",
        rf"{w2_067:.2f}%",
        r"Reports the gross nominal staking yield without adjusting for the 5.20% annual circulating supply expansion.",
        pos_cycle(67),
    )
    calc_ids.add("L1-ALT-067")
    add_l1(
        questions, "L1-ALT-067", SUBJECT, mod7, "Digital Assets", "Proof-of-Stake Real Yield",
        "Describe digital asset consensus mechanisms and valuation principles.",
        r"A Proof-of-Stake Layer-1 token offers a nominal staking reward of 8.40% APR while expanding total circulating token supply by 5.20% per year (zero fee burn). What is a staker's exact real (dilution-adjusted) staking yield?",
        opts, ans,
        rf"Adjusting nominal staking rewards for token supply inflation gives $\text{{Real Yield}} = \frac{{1 + 0.0840}}{{1 + 0.0520}} - 1 = {real_y67:.2f}\%$.",
        dist,
    )

    # L1-ALT-068 (Calc): DeFi AMM Impermanent Loss
    # 50/50 constant product pool; token A rises 4x (r=4) -> IL = 2*sqrt(4)/(1+4) - 1 = -20.00%
    r68 = 4.0
    il68 = (2 * math.sqrt(r68) / (1 + r68) - 1) * 100
    w1_068 = (1 / (1 + r68) - 0.5) * 100  # wrong linear formula = -30.00%
    w2_068 = ((2 * math.sqrt(2.0) / 3.0) - 1) * 100  # uses 2x instead of 4x = -5.72%
    opts, ans, dist = opt_pack(
        rf"{il68:.2f}%",
        rf"{w1_068:.2f}%",
        r"Uses an incorrect linear fraction rather than the constant-product geometric mean formula.",
        rf"{w2_068:.2f}%",
        r"Computes the impermanent loss for a 2x price move instead of a 4x relative price move.",
        pos_cycle(68),
    )
    calc_ids.add("L1-ALT-068")
    add_l1(
        questions, "L1-ALT-068", SUBJECT, mod7, "Digital Assets", "AMM Impermanent Loss",
        "Describe digital asset consensus mechanisms and valuation principles.",
        r"A liquidity provider deposits equal USD values into a 50/50 constant-product ($x \cdot y = k$) decentralized exchange pool. If one token quadruples in price relative to the other ($r = 4.0$), ignoring trading fees, what is the liquidity provider's percentage impermanent loss versus simply holding the initial assets?",
        opts, ans,
        rf"For a 50/50 constant-product AMM, impermanent loss equals $\frac{{2\sqrt{{r}}}}{{1 + r}} - 1 = \frac{{2\sqrt{{4}}}}{{1 + 4}} - 1 = \frac{{4}}{{5}} - 1 = {il68:.2f}\%$.",
        dist,
    )

    # L1-ALT-069 (Calc): Tokenized RWA net yield
    gross_y69, plat_fee69, gas_cost69, nav69 = 0.072, 0.0045, 0.0015, 25.0
    net_y69 = (gross_y69 - plat_fee69 - gas_cost69) * 100
    net_usd69 = nav69 * (gross_y69 - plat_fee69 - gas_cost69)
    w1_069 = (gross_y69 - plat_fee69) * 100
    w2_069 = (gross_y69 + plat_fee69 - gas_cost69) * 100
    opts, ans, dist = opt_pack(
        rf"{net_y69:.2f}% (USD {net_usd69:.2f} million)",
        rf"{w1_069:.2f}% (USD {nav69 * (gross_y69 - plat_fee69):.2f} million)",
        r"Deducts the platform smart-contract management fee but omits the 15 bps oracle and custody expense.",
        rf"{w2_069:.2f}% (USD {nav69 * (gross_y69 + plat_fee69 - gas_cost69):.2f} million)",
        r"Adds the platform fee to gross yield instead of deducting it.",
        pos_cycle(69),
    )
    calc_ids.add("L1-ALT-069")
    add_l1(
        questions, "L1-ALT-069", SUBJECT, mod7, "Tokenization", "Tokenized RWA Net Yield",
        "Evaluate real-world asset tokenization and institutional digital asset risks.",
        rf"An institution allocates USD {nav69:.0f} million to a tokenized private credit vault earning 7.20% gross annualized yield. The tokenization platform charges a 45 bps annual protocol fee, and regulated custody plus oracle verification costs 15 bps annually. What is the net annual yield and income?",
        opts, ans,
        rf"Net yield $= 7.20\% - 0.45\% - 0.15\% = {net_y69:.2f}\%$. Annual net income $= \text{{USD }} {nav69:.0f}\text{{M}} \times {net_y69:.2f}\% = \text{{USD }} {net_usd69:.2f}\text{{M}}$.",
        dist,
    )

    # L1-ALT-070 (Calc): Short selling total return with borrow fee & dividend
    p0_70, p1_70, div70, borrow70, rebate70 = 80.0, 68.0, 2.40, 0.03, 0.04
    # Classic short sale: borrow 1 share at 80, sell for 80, post cash collateral = 80 (assuming 100% cash proceeds earn rebate 4% minus 3% borrow fee = +1% net short rebate, OR state explicit 3% borrow cost & 0 rebate, or +4% cash rebate - 3% borrow!)
    # Let's state explicitly: cash proceeds earn 4.0% short rebate while stock loan borrow fee is 3.0%, and trader must reimburse USD 2.40 dividend over 1 year!
    price_gain = p0_70 - p1_70  # +12.00
    net_fin = p0_70 * (rebate70 - borrow70)  # +0.80
    tot_usd = price_gain - div70 + net_fin  # 12 - 2.40 + 0.80 = 10.40
    ret70 = tot_usd / p0_70 * 100  # 13.00%
    w1_070 = (price_gain + div70 + net_fin) / p0_70 * 100  # adds dividend instead of paying it
    w2_070 = (price_gain - div70) / p0_70 * 100  # omits net financing/rebate
    opts, ans, dist = opt_pack(
        rf"+{ret70:.2f}%",
        rf"+{w1_070:.2f}%",
        r"Adds the USD 2.40 dividend as income rather than deducting it as a dividend reimbursement owed to the stock lender.",
        rf"+{w2_070:.2f}%",
        r"Ignores the net +1.0% financing spread between the 4.0% cash rebate and 3.0% borrow fee.",
        pos_cycle(70),
    )
    calc_ids.add("L1-ALT-070")
    add_l1(
        questions, "L1-ALT-070", SUBJECT, mod7, "Shorting Mechanics", "Short Position Return",
        "Analyze short-selling mechanics, financing costs, and short-squeeze risks.",
        rf"A manager shorts a stock at USD {p0_70:.2f} for one year, posting initial collateral equal to 100% of short sale proceeds (USD {p0_70:.2f} denominator). During the year, the stock falls to USD {p1_70:.2f} and pays a USD {div70:.2f} dividend. The short cash proceeds earn a 4.00% rebate while the prime broker charges a 3.00% stock-borrow fee on initial value. What is the short position's total return?",
        opts, ans,
        rf"Price gain $= {p0_70:.2f} - {p1_70:.2f} = +\text{{USD }} {price_gain:.2f}$. The short seller must reimburse the USD {div70:.2f} dividend ($-\text{{USD }} {div70:.2f}$) and earns net interest rebate $(4.00\% - 3.00\%) \times {p0_70:.2f} = +\text{{USD }} {net_fin:.2f}$. Net dollar profit $= {price_gain:.2f} - {div70:.2f} + {net_fin:.2f} = \text{{USD }} {tot_usd:.2f}$, or $\frac{{{tot_usd:.2f}}}{{{p0_70:.2f}}} = +{ret70:.2f}\%$.",
        dist,
    )

    # L1-ALT-071 (Calc): Short interest ratio (Days to Cover) and margin equity
    short_sh, adv_sh = 18.0, 2.25
    dtc71 = short_sh / adv_sh  # 8.0 days
    sh_num, p_start71, p_spike71, cash_collat = 100000, 30.0, 42.0, 4500000.0
    # Equity = cash_collat - short_liab; Margin equity ratio = Equity / short_liab
    short_liab = sh_num * p_spike71  # 4.2M
    eq71 = cash_collat - short_liab  # 0.3M
    m_ratio71 = eq71 / short_liab * 100  # 7.14%
    w1_071 = eq71 / cash_collat * 100  # divides by initial collateral
    w2_071 = (cash_collat - sh_num * p_start71) / short_liab * 100  # fails to mark short liability to market
    opts, ans, dist = opt_pack(
        rf"Days to cover = {dtc71:.1f} days; Short margin equity ratio = {m_ratio71:.2f}%",
        rf"Days to cover = {dtc71:.1f} days; Short margin equity ratio = {w1_071:.2f}%",
        r"Divides remaining equity by initial collateral rather than current market value of the short liability.",
        rf"Days to cover = {adv_sh / short_sh:.2f} days; Short margin equity ratio = {w2_071:.2f}%",
        r"Inverts the days-to-cover ratio and values the short liability at entry price instead of current market price.",
        pos_cycle(71),
    )
    calc_ids.add("L1-ALT-071")
    add_l1(
        questions, "L1-ALT-071", SUBJECT, mod7, "Shorting Mechanics", "Days to Cover and Margin Ratio",
        "Analyze short-selling mechanics, financing costs, and short-squeeze risks.",
        rf"A stock has {short_sh:.1f} million shares sold short and an average daily trading volume of {adv_sh:.2f} million shares. Separately, a fund holds USD 4.50 million in total margin cash/collateral against a 100,000-share short position originally opened at USD 30.00 that spikes to USD 42.00 during a squeeze. What are the stock's days-to-cover ratio and the fund's current short margin equity ratio?",
        opts, ans,
        rf"Days to cover $= \frac{{{short_sh:.1f}\text{{M}}}}{{{adv_sh:.2f}\text{{M}}}} = {dtc71:.1f}$ days. Current short liability $= 100,000 \times 42.00 = \text{{USD }} 4.20\text{{M}}$, leaving equity $= 4.50 - 4.20 = \text{{USD }} 0.30\text{{M}}$. Short margin equity ratio $= \frac{{0.30}}{{4.20}} = {m_ratio71:.2f}\%$.",
        dist,
    )

    # L1-ALT-072 (Calc): Sustainability carbon-credit NPV uplift in timberland
    hectares, tons_ha, price_t, mrv_cost, yrs72, r72 = 5000, 8.0, 22.0, 80000.0, 5, 0.07
    ann_rev72 = hectares * tons_ha * price_t  # 880,000
    ann_net72 = (ann_rev72 - mrv_cost) / 1e6  # 0.80M/yr
    npv72 = sum(ann_net72 / ((1 + r72) ** t) for t in range(1, yrs72 + 1))
    w1_072 = sum((ann_rev72 / 1e6) / ((1 + r72) ** t) for t in range(1, yrs72 + 1))
    w2_072 = ann_net72 * yrs72
    opts, ans, dist = opt_pack(
        rf"USD {npv72:.2f} million",
        rf"USD {w1_072:.2f} million",
        r"Omits the annual USD 80,000 MRV certification cost when computing net carbon cash flows.",
        rf"USD {w2_072:.2f} million",
        r"Sums undiscounted net carbon revenues across 5 years instead of discounting at 7.0%.",
        pos_cycle(72),
    )
    calc_ids.add("L1-ALT-072")
    add_l1(
        questions, "L1-ALT-072", SUBJECT, mod7, "Sustainability in Alternatives", "Carbon Offset NPV",
        "Evaluate ESG and sustainability integration across alternative investments.",
        rf"A {hectares:,}-hectare improved-forest-management project generates {tons_ha:.1f} metric tons of verified carbon credits per hectare annually over Years 1-5, sold at USD {price_t:.0f} per ton, with annual verification (MRV) costs of USD 80,000. Using a 7.00% discount rate, what is the incremental present value of the carbon credit stream?",
        opts, ans,
        rf"Annual gross carbon revenue $= {hectares:,} \times {tons_ha:.1f} \times {price_t:.0f} = \text{{USD }} {ann_rev72:,.0f}$; net of USD 80,000 MRV cost gives USD {ann_net72:.2f}M/year. Discounting this 5-year annuity at 7.00% produces $\text{{PV}} = {ann_net72:.2f} \times \frac{{1 - 1.07^{{-5}}}}{{0.07}} = \text{{USD }} {npv72:.2f}\text{{M}}$.",
        dist,
    )

    # L1-ALT-073 (Concept): PoW vs PoS consensus
    opts, ans, dist = opt_pack(
        r"Proof-of-Stake secures blocks via staked economic collateral subject to validator slashing, consuming orders of magnitude less energy than hash-rate competition under Proof-of-Work.",
        r"Proof-of-Work rewards block validators solely according to their locked token holdings with near-zero electricity consumption.",
        r"Proof-of-Work requires specialized hardware racing to solve cryptographic hashes, creating substantial electricity usage.",
        r"Proof-of-Stake eliminates all smart-contract and governance concentration risks because anyone can print unlimited validator stake for free.",
        r"Staking requires locking real economic value, and heavy token concentration can create validator centralization risks.",
        pos_cycle(73),
    )
    add_l1(
        questions, "L1-ALT-073", SUBJECT, mod7, "Digital Assets", "Consensus Mechanisms",
        "Describe digital asset consensus mechanisms and valuation principles.",
        r"Which statement accurately contrasts Proof-of-Work (PoW) and Proof-of-Stake (PoS) blockchain consensus mechanisms?",
        opts, ans,
        r"PoW relies on computational hash-power expenditure to deter attacks, whereas PoS substitutes bonded token capital with slashing penalties for malicious validation, dramatically reducing energy intensity.",
        dist,
    )

    # L1-ALT-074 (Concept): Custody, smart-contract & oracle risks
    opts, ans, dist = opt_pack(
        r"Institutional cold storage keeps private keys offline to mitigate cybertheft, whereas DeFi tokenization relies on external price oracles and immutable smart-contract code that introduce exploit vulnerabilities.",
        r"Hot wallets keep private keys permanently air-gapped offline, making them immune to internet phishing or API breaches.",
        r"Hot wallets remain internet-connected for fast execution and are more vulnerable to online compromise than air-gapped cold storage.",
        r"Tokenizing real estate automatically eliminates underlying property illiquidity and guarantees daily par redemption regardless of secondary buyers.",
        r"Tokenization fractionalizes ownership records, but liquidity still depends on secondary market depth and legal redemption rights.",
        pos_cycle(74),
    )
    add_l1(
        questions, "L1-ALT-074", SUBJECT, mod7, "Digital Assets", "Custody and Tokenization Risks",
        "Evaluate real-world asset tokenization and institutional digital asset risks.",
        r"Which statement most accurately describes operational and structural risks in institutional digital assets?",
        opts, ans,
        r"Air-gapped cold custody protects private keys from online intrusion, while on-chain DeFi and tokenized protocols introduce smart-contract bugs, oracle manipulation, and legal enforceability gaps between off-chain assets and on-chain tokens.",
        dist,
    )

    # L1-ALT-075 (Concept): Sustainability in Alternatives
    opts, ans, dist = opt_pack(
        r"In private equity and real estate, integrating energy-efficiency upgrades and green building certifications can enhance exit multiples (" + "\"brown-to-green\"" + " premium) and lower long-term obsolescence risk.",
        r"Green leases eliminate all tenant credit risk and force landlords to pay 100% of energy-retrofit CapEx without rent recovery.",
        r"Green leases establish cost-sharing and data-transparency terms between landlords and tenants rather than eliminating tenant default risk.",
        r"ESG data reporting across private markets is already governed by a single globally audited standard identical to IFRS.",
        r"Private alternative assets suffer from fragmented, self-reported ESG metrics and inconsistent verification standards.",
        pos_cycle(75),
    )
    add_l1(
        questions, "L1-ALT-075", SUBJECT, mod7, "Sustainability in Alternatives", "ESG Integration Across Private Assets",
        "Evaluate ESG and sustainability integration across alternative investments.",
        r"Which statement accurately characterizes ESG integration in alternative investments?",
        opts, ans,
        r"Active ownership in private equity and real estate allows sponsors to implement operational decarbonization and green certifications that improve tenant demand, financing terms, and exit valuations despite fragmented private-market disclosure.",
        dist,
    )


def build_l2_v01_v05(questions: list, calc_ids: set):
    """Build Vignettes ALT-V01 through ALT-V05 (25 L2 questions)."""

    # =========================================================================
    # V01: Multi-Year Hedge Fund Fee Waterfall with GP Catch-Up & HWM
    # =========================================================================
    v1_id = "ALT-V01"
    v1_title = "Apex Macro Opportunities: Multi-Year Hedge Fund Fee Waterfall"
    v1_text = (
        "Elena Vance, Chief Investment Officer of the Meridian University Endowment, is auditing a 3-year investment "
        "in Apex Macro Opportunities LP initiated on 1 January Year 1 with USD 100.00 million.\n\n"
        "Fee Terms of Apex Macro Opportunities LP:\n"
        "- Management Fee: 1.50% annually, calculated on end-of-year gross AUM (before incentive fees).\n"
        "- Incentive Fee: 20.00% annually, calculated strictly net of the management fee.\n"
        "- Hurdle Rate: 5.00% annual hard hurdle (non-cumulative, reset each year against the greater of beginning net AUM or the HWM).\n"
        "- High-Water Mark (HWM): Initial HWM is USD 100.00 million; HWM resets upward only at year-end to the highest historical net ending AUM after all fees.\n\n"
        "Gross Annual Returns: Year 1: +20.00%; Year 2: -10.00%; Year 3: +25.00%.\n"
        "Alternative Structure Evaluated: A competing share class replaces the 5.00% hard hurdle with a 5.00% soft hurdle incorporating a 100% GP catch-up above the hurdle."
    )
    mod_v1 = "Hedge Fund Fee Waterfalls"

    # Compute exact 3-year schedule
    a0 = 100.00
    mgmt_r, inc_r, hurd_r = 0.015, 0.20, 0.05
    # Year 1
    y1_gross = a0 * 1.20  # 120.00
    y1_mgmt = y1_gross * mgmt_r  # 1.80
    y1_net_m = y1_gross - y1_mgmt  # 118.20
    y1_thresh = a0 * (1 + hurd_r)  # 105.00
    y1_inc = max(0.0, (y1_net_m - y1_thresh) * inc_r)  # (118.20 - 105)*0.2 = 2.64
    y1_end = y1_net_m - y1_inc  # 115.56
    y1_tot_fee = y1_mgmt + y1_inc  # 4.44
    y1_ret = (y1_end / a0 - 1) * 100  # 15.56%
    hwm1 = max(a0, y1_end)  # 115.56

    # Year 2
    y2_gross = y1_end * 0.90  # 104.004
    y2_mgmt = y2_gross * mgmt_r  # 1.56006
    y2_net_m = y2_gross - y2_mgmt  # 102.44394
    y2_inc = 0.0  # below HWM 115.56
    y2_end = y2_net_m  # 102.44394
    hwm2 = max(hwm1, y2_end)  # 115.56

    # Year 3: base for hurdle = max(y2_end, hwm2) = 115.56; hurdle threshold = 115.56 * 1.05 = 121.338!
    # Wait: let's check both standard CFA conventions for HWM + hurdle:
    # Usually either (a) incentive applies above HWM*(1+hurdle) OR (b) incentive applies above max(HWM, beg*(1+hurdle))!
    # Let's make the text crystal clear: "against the greater of beginning net AUM or the HWM" -> hurdle base = HWM = 115.56, so 5% hurdle threshold = 115.56 * 1.05 = 121.338!
    y3_gross = y2_end * 1.25  # 128.054925
    y3_mgmt = y3_gross * mgmt_r  # 1.920823875
    y3_net_m = y3_gross - y3_mgmt  # 126.134101125
    y3_thresh = max(y2_end, hwm2) * (1 + hurd_r)  # 115.56 * 1.05 = 121.338
    y3_inc = max(0.0, (y3_net_m - y3_thresh) * inc_r)  # (126.134101 - 121.338)*0.20 = 0.959220
    y3_end = y3_net_m - y3_inc  # 125.174881
    cagr3 = ((y3_end / a0) ** (1 / 3) - 1) * 100

    # Q1: Year 1 total fees & LP net return
    w1_v1q1 = y1_mgmt + (y1_gross - y1_thresh) * inc_r  # independent inc fee
    w2_v1q1 = (a0 * mgmt_r) + max(0.0, ((y1_gross - a0 * mgmt_r) - y1_thresh) * inc_r)  # beg AUM mgmt
    opts, ans, dist = opt_pack(
        rf"USD {y1_tot_fee:.2f} million (Net return: {y1_ret:.2f}%)",
        rf"USD {w1_v1q1:.2f} million (Net return: {(y1_gross - w1_v1q1 - a0) / a0 * 100:.2f}%)",
        r"Calculates the incentive fee independently of the management fee instead of net of the management fee.",
        rf"USD {w2_v1q1:.2f} million (Net return: {(y1_gross - w2_v1q1 - a0) / a0 * 100:.2f}%)",
        r"Computes the 1.50% management fee on beginning AUM (USD 100M) rather than ending gross AUM (USD 120M).",
        pos_cycle(1),
    )
    calc_ids.add("L2-ALT-V01-Q1")
    add_l2(
        questions, "L2-ALT-V01-Q1", SUBJECT, mod_v1, "Fee Waterfalls", "Year 1 Hard Hurdle Calculation",
        v1_id, v1_id, v1_title, v1_text,
        "Evaluate multi-year hedge fund fee structures including management fees, incentive fees, hurdles, and high-water marks.",
        r"In Year 1, what are the total fees earned by Apex Macro Opportunities LP and the endowment's net return?",
        opts, ans,
        rf"Year 1 gross ending AUM $= 100 \times 1.20 = \text{{USD }} {y1_gross:.2f}\text{{M}}$. Management fee $= {y1_gross:.2f} \times 1.50\% = \text{{USD }} {y1_mgmt:.2f}\text{{M}}$, leaving ${y1_net_m:.2f}\text{{M}}$ net of management fee. Hard hurdle threshold $= 100 \times 1.05 = \text{{USD }} {y1_thresh:.2f}\text{{M}}$. Incentive fee $= ({y1_net_m:.2f} - {y1_thresh:.2f}) \times 20\% = \text{{USD }} {y1_inc:.2f}\text{{M}}$. Total fees $= {y1_mgmt:.2f} + {y1_inc:.2f} = \text{{USD }} {y1_tot_fee:.2f}\text{{M}}$, giving ending net AUM of USD {y1_end:.2f}M and net return of ${y1_ret:.2f}\%$.",
        dist,
    )

    # Q2: Year 2 ending NAV & carried-forward HWM
    w1_v1q2 = y2_end  # wait need different numbers!
    w1_v1q2_nav = y1_end * 0.90 - y1_end * mgmt_r  # mgmt fee on beg AUM instead of ending gross
    w2_v1q2_hwm = y2_end  # resets HWM downward!
    opts, ans, dist = opt_pack(
        rf"Ending net AUM = USD {y2_end:.2f} million; Carried-forward HWM = USD {hwm2:.2f} million",
        rf"Ending net AUM = USD {w1_v1q2_nav:.2f} million; Carried-forward HWM = USD {hwm2:.2f} million",
        r"Applies the Year 2 management fee to beginning AUM rather than end-of-year gross AUM.",
        rf"Ending net AUM = USD {y2_end:.2f} million; Carried-forward HWM = USD {w2_v1q2_hwm:.2f} million",
        r"Improperly resets the HWM downward after a losing year instead of preserving the Year 1 peak HWM.",
        pos_cycle(2),
    )
    calc_ids.add("L2-ALT-V01-Q2")
    add_l2(
        questions, "L2-ALT-V01-Q2", SUBJECT, mod_v1, "Fee Waterfalls", "Drawdown and High-Water Mark",
        v1_id, v1_id, v1_title, v1_text,
        "Evaluate multi-year hedge fund fee structures including management fees, incentive fees, hurdles, and high-water marks.",
        r"At the end of Year 2, what are the endowment's net ending AUM and the high-water mark carried forward into Year 3?",
        opts, ans,
        rf"Year 2 gross ending AUM $= {y1_end:.2f} \times 0.90 = \text{{USD }} {y2_gross:.2f}\text{{M}}$. Management fee $= {y2_gross:.2f} \times 1.50\% = \text{{USD }} {y2_mgmt:.2f}\text{{M}}$, yielding net ending AUM of ${y2_net_m:.2f}\text{{M}}$ (no incentive fee during a drawdown). The HWM remains at the Year 1 peak of USD {hwm2:.2f} million.",
        dist,
    )

    # Q3: Year 3 recovery incentive fee & 3-year net CAGR
    # Wrong 1: incentive above Year 2 ending * 1.05 (ignores HWM)
    y3_inc_nohwm = (y3_net_m - y2_end * 1.05) * inc_r
    # Wrong 2: incentive above HWM without 5% hurdle
    y3_inc_nohurd = (y3_net_m - hwm2) * inc_r
    opts, ans, dist = opt_pack(
        rf"Year 3 incentive fee = USD {y3_inc:.2f} million; 3-year net CAGR = {cagr3:.2f}%",
        rf"Year 3 incentive fee = USD {y3_inc_nohwm:.2f} million; 3-year net CAGR = {((y3_net_m - y3_inc_nohwm) / a0) ** (1 / 3) * 100 - 100:.2f}%",
        r"Computes the Year 3 hurdle base off Year 2's depressed ending AUM rather than the higher USD 115.56M HWM.",
        rf"Year 3 incentive fee = USD {y3_inc_nohurd:.2f} million; 3-year net CAGR = {((y3_net_m - y3_inc_nohurd) / a0) ** (1 / 3) * 100 - 100:.2f}%",
        r"Applies the incentive fee directly above the HWM without adding the 5.00% annual hurdle.",
        pos_cycle(3),
    )
    calc_ids.add("L2-ALT-V01-Q3")
    add_l2(
        questions, "L2-ALT-V01-Q3", SUBJECT, mod_v1, "Fee Waterfalls", "Recovery Above HWM and Multi-Year CAGR",
        v1_id, v1_id, v1_title, v1_text,
        "Evaluate multi-year hedge fund fee structures including management fees, incentive fees, hurdles, and high-water marks.",
        r"What are Apex Macro's Year 3 incentive fee and the endowment's 3-year annualized net return (CAGR)?",
        opts, ans,
        rf"Year 3 gross AUM $= {y2_end:.2f} \times 1.25 = \text{{USD }} {y3_gross:.2f}\text{{M}}$; management fee $= {y3_gross:.2f} \times 1.50\% = \text{{USD }} {y3_mgmt:.2f}\text{{M}}$; net before incentive $= \text{{USD }} {y3_net_m:.2f}\text{{M}}$. Hurdle threshold $= \max({y2_end:.2f}, {hwm2:.2f}) \times 1.05 = \text{{USD }} {y3_thresh:.2f}\text{{M}}$. Year 3 incentive fee $= ({y3_net_m:.2f} - {y3_thresh:.2f}) \times 20\% = \text{{USD }} {y3_inc:.2f}\text{{M}}$, leaving Year 3 net AUM $= \text{{USD }} {y3_end:.2f}\text{{M}}$. 3-year CAGR $= \left(\frac{{{y3_end:.2f}}}{{100}}\right)^{{1/3}} - 1 = {cagr3:.2f}\%$.",
        dist,
    )

    # Q4: Year 1 soft hurdle with 100% catch-up vs hard hurdle
    # Net gain after mgmt in Y1 = 18.20M (>5M hurdle). Under soft hurdle with 100% catch-up:
    # LP gets 5.00M; catch-up cap = (0.20/0.80)*5.00 = 1.25M; remaining = 18.20 - 6.25 = 11.95M -> 20% = 2.39 -> total = 3.64M (exactly 20% of 18.20M!)
    y1_inc_soft = (y1_net_m - a0) * inc_r  # 3.64
    inc_diff_q4 = y1_inc_soft - y1_inc  # 1.00
    w1_v1q4 = y1_inc  # computes hard hurdle again
    w2_v1q4 = y1_inc_soft + y1_mgmt  # includes mgmt fee in difference
    opts, ans, dist = opt_pack(
        rf"USD {y1_inc_soft:.2f} million (USD {inc_diff_q4:.2f} million higher than the hard hurdle)",
        rf"USD {w1_v1q4:.2f} million (unchanged from the hard hurdle)",
        r"Fails to recognize that a 100% GP catch-up lifts total GP carry to 20% of the entire USD 18.20M net-of-management gain.",
        rf"USD {y1_inc_soft + 1.25:.2f} million (USD {inc_diff_q4 + 1.25:.2f} million higher than the hard hurdle)",
        r"Double-counts the USD 1.25M catch-up tranche on top of 20% of the total profit.",
        pos_cycle(4),
    )
    calc_ids.add("L2-ALT-V01-Q4")
    add_l2(
        questions, "L2-ALT-V01-Q4", SUBJECT, mod_v1, "Fee Waterfalls", "Soft Hurdle Catch-Up Comparison",
        v1_id, v1_id, v1_title, v1_text,
        "Evaluate multi-year hedge fund fee structures including management fees, incentive fees, hurdles, and high-water marks.",
        r"Under the alternative share class (5.00% soft hurdle with a 100% GP catch-up), what would Apex Macro's Year 1 incentive fee be, and how much does it exceed the hard-hurdle incentive fee?",
        opts, ans,
        rf"Net-of-management profit in Year 1 is ${y1_net_m:.2f} - 100 = \text{{USD }} {y1_net_m - a0:.2f}\text{{M}}$, which easily exceeds the 5.00% hurdle (USD 5.00M). Following the 5.00M preferred return, the 100% catch-up pays the GP $\frac{{0.20}}{{0.80}} \times 5.00 = \text{{USD }} 1.25\text{{M}}$ (putting GP at 20% of USD 6.25M), plus 20% of the remaining ${y1_net_m - a0 - 6.25:.2f}\text{{M}}$ (${(y1_net_m - a0 - 6.25) * 0.20:.2f}\text{{M}}$), totaling $\text{{USD }} {y1_inc_soft:.2f}\text{{M}}$ ($= 20\% \times {y1_net_m - a0:.2f}\text{{M}}$)—exceeding the hard-hurdle fee by ${y1_inc_soft:.2f} - {y1_inc:.2f} = \text{{USD }} {inc_diff_q4:.2f}\text{{M}}$.",
        dist,
    )

    # Q5 (Concept): Incentive asymmetry & risk-shifting
    opts, ans, dist = opt_pack(
        r"Because incentive fees crystallize annually without a clawback, deep below-HWM drawdowns create a convex incentive for the GP to increase portfolio risk or close and restart the fund.",
        r"Paying management fees on ending gross AUM rather than beginning AUM lowers total GP fees whenever gross returns are positive.",
        r"When gross returns are positive, ending AUM exceeds beginning AUM, increasing the dollar management fee.",
        r"HWM resets eliminate all asymmetric risk-taking incentives even if the fund drops 40% below its peak.",
        r"A deep drawdown makes the GP's call option deeply out-of-the-money, exacerbating risk-shifting or shutdown risk.",
        pos_cycle(5),
    )
    add_l2(
        questions, "L2-ALT-V01-Q5", SUBJECT, mod_v1, "Fee Governance", "Incentive Alignment and Risk-Shifting",
        v1_id, v1_id, v1_title, v1_text,
        "Evaluate multi-year hedge fund fee structures including management fees, incentive fees, hurdles, and high-water marks.",
        r"Which governance conclusion is Vance most justified in drawing from Apex Macro's fee structure?",
        opts, ans,
        r"Annualized incentive crystallization acts like a free call option for the GP: gains trigger immediate 20% fees while losses are borne by LPs, creating risk-shifting or abandonment risk following deep drawdowns below the HWM.",
        dist,
    )

    # =========================================================================
    # V02: PE Fund IRR/DPI/RVPI/TVPI & Deal-by-Deal vs Whole-of-Fund Clawback
    # =========================================================================
    v2_id = "ALT-V02"
    v2_title = "Northbridge Buyout Fund IV: Waterfall, Performance, and Clawback"
    v2_text = (
        "Marcus Chen, Senior Private Markets Analyst at Pacific Pension Fund, reviews Northbridge Buyout Fund IV "
        "(USD 200.00 million total LP commitments, 8.0% annualized preferred return ignored only for the simplified deal-by-deal vs. whole-of-fund carry comparison below unless explicitly specified).\n\n"
        "Annual Fund-Level LP Net Cash Flows and Valuation (USD millions):\n"
        "- Year 0: Capital Call -60.00 | Distribution 0.00 | Year-End NAV 58.00\n"
        "- Year 1: Capital Call -70.00 | Distribution 0.00 | Year-End NAV 124.00\n"
        "- Year 2: Capital Call -40.00 | Distribution +25.00 | Year-End NAV 148.00\n"
        "- Year 3: Capital Call -10.00 | Distribution +85.00 | Year-End NAV 122.00\n"
        "- Year 4: Capital Call 0.00   | Distribution +92.00 | Year-End NAV 70.00\n"
        "- Year 5 (Liquidation): Capital Call 0.00 | Distribution +88.00 | Year-End NAV 0.00\n\n"
        "Underlying 4-Deal Attribution (20.0% Carry, Zero Hurdle for Deal-Level Clawback Audit):\n"
        "- Deal 1 (Exited Y2): Invested 40.0M -> Realized 90.0M (+50.0M profit)\n"
        "- Deal 2 (Exited Y3): Invested 50.0M -> Realized 105.0M (+55.0M profit)\n"
        "- Deal 3 (Exited Y4): Invested 50.0M -> Realized 25.0M (-25.0M loss)\n"
        "- Deal 4 (Exited Y5): Invested 40.0M -> Realized 70.0M (+30.0M profit)\n"
        "Total Invested Capital across Deals 1-4 = USD 180.0M; Aggregate Deal Gross Proceeds = USD 290.0M."
    )
    mod_v2 = "Private Equity Performance & Waterfalls"

    # Q1: Year 4 DPI, RVPI, TVPI
    pic_y4 = 60 + 70 + 40 + 10  # 180.0
    dist_y4 = 25 + 85 + 92  # 202.0
    nav_y4 = 70.0
    dpi_y4 = dist_y4 / pic_y4
    rvpi_y4 = nav_y4 / pic_y4
    tvpi_y4 = dpi_y4 + rvpi_y4
    w1_v2q1 = (dist_y4 / 200.0)
    w1_v2q1_tvpi = (dist_y4 + nav_y4) / 200.0
    w2_v2q1_dpi = (dist_y4 + nav_y4) / pic_y4  # confuses TVPI with DPI
    opts, ans, dist = opt_pack(
        rf"DPI = {dpi_y4:.2f}x; RVPI = {rvpi_y4:.2f}x; TVPI = {tvpi_y4:.2f}x",
        rf"DPI = {w1_v2q1:.2f}x; RVPI = {nav_y4 / 200.0:.2f}x; TVPI = {w1_v2q1_tvpi:.2f}x",
        r"Uses total committed capital (USD 200M) instead of paid-in capital (USD 180M) in the denominator.",
        rf"DPI = {w2_v2q1_dpi:.2f}x; RVPI = {rvpi_y4:.2f}x; TVPI = {dpi_y4:.2f}x",
        r"Swaps TVPI and DPI definitions by including residual NAV in DPI and omitting it from TVPI.",
        pos_cycle(6),
    )
    calc_ids.add("L2-ALT-V02-Q1")
    add_l2(
        questions, "L2-ALT-V02-Q1", SUBJECT, mod_v2, "Private Equity Metrics", "Year 4 Multiples",
        v2_id, v2_id, v2_title, v2_text,
        "Calculate and interpret DPI, RVPI, TVPI, IRR, and clawback provisions in private equity waterfalls.",
        r"At the end of Year 4, what are Northbridge Buyout Fund IV's DPI, RVPI, and TVPI?",
        opts, ans,
        rf"Cumulative paid-in capital through Year 4 $= 60 + 70 + 40 + 10 = \text{{USD }} {pic_y4:.0f}\text{{M}}$. Cumulative distributions $= 25 + 85 + 92 = \text{{USD }} {dist_y4:.0f}\text{{M}}$; Year 4 residual NAV $= \text{{USD }} {nav_y4:.0f}\text{{M}}$. Thus: $\text{{DPI}} = \frac{{{dist_y4:.0f}}}{{{pic_y4:.0f}}} = {dpi_y4:.2f}\text{{x}}$, $\text{{RVPI}} = \frac{{{nav_y4:.0f}}}{{{pic_y4:.0f}}} = {rvpi_y4:.2f}\text{{x}}$, and $\text{{TVPI}} = {dpi_y4:.2f} + {rvpi_y4:.2f} = {tvpi_y4:.2f}\text{{x}}$.",
        dist,
    )

    # Q2: Net LP IRR over Years 0-5
    cfs_v2 = [-60.0, -70.0, -15.0, 75.0, 92.0, 88.0]  # net each year: Y2 = -40+25=-15, Y3 = -10+85=+75
    irr_v2 = calc_irr(cfs_v2) * 100
    tot_moic_v2 = (25 + 85 + 92 + 88) / 180.0
    w1_v2q2 = (tot_moic_v2 ** (1 / 5) - 1) * 100  # simple 5-yr MOIC CAGR
    w2_v2q2 = calc_irr([-180.0, 0.0, 25.0, 85.0, 92.0, 88.0]) * 100  # all capital called at t=0
    opts, ans, dist = opt_pack(
        rf"{irr_v2:.2f}%",
        rf"{w1_v2q2:.2f}%",
        r"Takes the 5th root of total MOIC (1.61x), ignoring the staggered timing of calls and distributions.",
        rf"{w2_v2q2:.2f}%",
        r"Assumes all USD 180M was called upfront at Year 0 instead of staggered across Years 0 to 3.",
        pos_cycle(7),
    )
    calc_ids.add("L2-ALT-V02-Q2")
    add_l2(
        questions, "L2-ALT-V02-Q2", SUBJECT, mod_v2, "Private Equity Metrics", "Since-Inception Net IRR",
        v2_id, v2_id, v2_title, v2_text,
        "Calculate and interpret DPI, RVPI, TVPI, IRR, and clawback provisions in private equity waterfalls.",
        r"Based on the annual net LP cash flows through full liquidation at Year 5, what is the fund's annualized since-inception net IRR?",
        opts, ans,
        rf"Net annual LP cash flows (calls plus distributions) are: $t=0$: $-60$; $t=1$: $-70$; $t=2$: $-40 + 25 = -15$; $t=3$: $-10 + 85 = +75$; $t=4$: $+92$; $t=5$: $+88$. Solving $\sum_{{t=0}}^5 \frac{{CF_t}}{{(1 + \text{{IRR}})^t}} = 0$ yields $\text{{IRR}} = {irr_v2:.2f}\%$.",
        dist,
    )

    # Q3: Deal-by-Deal carry at Year 4 vs Whole-of-Fund carry -> Clawback at Year 4 (after Deal 3 loss, before Deal 4 exit!) OR at Year 5!
    # Wait: Look at Deal 1 (+50 -> carry 10), Deal 2 (+55 -> carry 11) -> cumulative carry paid through Y3 = 21.0M!
    # At Year 4, Deal 3 realizes -25M -> cumulative realized profit across Deals 1-3 = 50 + 55 - 25 = 80M -> entitled carry = 16.0M -> overpayment = 5.0M.
    # At Year 5, Deal 4 realizes +30M -> total aggregate fund profit across Deals 1-4 = 50 + 55 - 25 + 30 = 110M -> total entitled carry = 22.0M!
    # Let's ask specifically at Year 4 (after Deal 3 loss, assuming Deal 4 has not yet exited) vs Year 5! Actually if Deal 1, 2, 3 realized by Year 4: cumulative profit = 80M -> carry 16M vs 21M paid = 5.0M interim clawback / over-distribution! OR make Deal 4 lose -10M instead of +30M? Wait: if Deal 4 = +30M (already in text!), at Year 4 (if evaluated on Deals 1-3 realized to date) clawback deficit is 5.0M, OR let's ask: "Under a deal-by-deal waterfall without escrow, how much carried interest had the GP collected through Year 3, and what would the GP's Year 4 clawback liability be if Deal 4 were written off to zero?" Or simply evaluate Deals 1-3 vs Whole-of-Fund through Year 4!
    # Let's check exact wording: "Through Year 4 (covering exited Deals 1, 2, and 3, assuming Deal 4 is still held at cost), how much excess carried interest has the GP collected under a deal-by-deal waterfall relative to a whole-of-fund waterfall?"
    carry_d12 = (50.0 + 55.0) * 0.20  # 21.0
    net_d123 = 50.0 + 55.0 - 25.0  # 80.0
    entitled_y4 = net_d123 * 0.20  # 16.0
    excess_y4 = carry_d12 - entitled_y4  # 5.0
    w1_v2q3 = 25.0 * 0.20 + 2.0  # wait avoid coincidence! Use 25.0 (whole loss) or 0.0 (no clawback) or 21.0 (full carry)
    opts, ans, dist = opt_pack(
        rf"Collected USD {carry_d12:.1f}M; Excess carry (clawback deficit) = USD {excess_y4:.1f}M",
        rf"Collected USD {carry_d12:.1f}M; Excess carry (clawback deficit) = USD {carry_d12:.1f}M",
        r"Assumes the entire USD 21.0M carry is clawed back instead of only the USD 5.0M attributable to Deal 3's loss.",
        rf"Collected USD {entitled_y4:.1f}M; Excess carry (clawback deficit) = USD 0.0M",
        r"Assumes a deal-by-deal waterfall automatically offsets future deal losses before paying carry on Deals 1 and 2.",
        pos_cycle(8),
    )
    calc_ids.add("L2-ALT-V02-Q3")
    add_l2(
        questions, "L2-ALT-V02-Q3", SUBJECT, mod_v2, "Private Equity Waterfalls", "Deal-by-Deal Clawback Deficit",
        v2_id, v2_id, v2_title, v2_text,
        "Calculate and interpret DPI, RVPI, TVPI, IRR, and clawback provisions in private equity waterfalls.",
        r"Under a deal-by-deal waterfall (with zero hurdle and no escrow holdback), how much carry did the GP collect across Deals 1 and 2, and what excess carry deficit exists at Year 4 after Deal 3's realized loss (holding Deal 4 unrealized at cost)?",
        opts, ans,
        rf"Under deal-by-deal distribution, the GP collects $20\% \times (50.0 + 55.0) = \text{{USD }} {carry_d12:.1f}\text{{M}}$ on profitable Deals 1 and 2. After Deal 3 loses USD 25.0M in Year 4, aggregate realized profit across Deals 1-3 drops to $50.0 + 55.0 - 25.0 = \text{{USD }} {net_d123:.1f}\text{{M}}$, entitling the GP to $20\% \times {net_d123:.1f} = \text{{USD }} {entitled_y4:.1f}\text{{M}}$. The excess carry collected (clawback deficit) is ${carry_d12:.1f} - {entitled_y4:.1f} = \text{{USD }} {excess_y4:.1f}\text{{M}}$.",
        dist,
    )

    # Q4: Whole-of-Fund with 8% preferred return + 100% catch-up on 180M invested and 290M total proceeds
    # Suppose total fund duration pref = 18.0M cumulative hurdle (explicitly stated in question: "cumulative 8.0% preferred return dollar obligation of USD 24.0M")
    #Wait: let's state explicit cumulative preferred return USD 24.0M so there is zero ambiguity on IRR compounding of pref!
    pic_q4, proc_q4, pref_q4 = 180.0, 290.0, 24.0
    tot_prof_q4 = proc_q4 - pic_q4  # 110.0
    catchup_q4 = (0.20 / 0.80) * pref_q4  # 6.0 (at 24+6=30, GP has 6=20%)
    rem_q4 = tot_prof_q4 - pref_q4 - catchup_q4  # 110 - 30 = 80.0
    gp_carry_q4 = catchup_q4 + 0.20 * rem_q4  # 6 + 16 = 22.0 (20% of 110!)
    lp_net_q4 = proc_q4 - gp_carry_q4  # 268.0
    w1_v2q4 = (tot_prof_q4 - pref_q4) * 0.20  # 17.2 (hard hurdle, no catch-up)
    w2_v2q4 = pref_q4 * 0.20 + rem_q4 * 0.20  # miscomputes catch-up
    opts, ans, dist = opt_pack(
        rf"GP Total Carry = USD {gp_carry_q4:.2f}M; LP Total Distributions = USD {lp_net_q4:.2f}M",
        rf"GP Total Carry = USD {w1_v2q4:.2f}M; LP Total Distributions = USD {proc_q4 - w1_v2q4:.2f}M",
        r"Applies a hard hurdle without the 100% GP catch-up band, leaving GP carry below 20% of total fund profits.",
        rf"GP Total Carry = USD {gp_carry_q4 + catchup_q4:.2f}M; LP Total Distributions = USD {proc_q4 - gp_carry_q4 - catchup_q4:.2f}M",
        r"Double-counts the USD 6.00M catch-up tranche in addition to 20% of total profits.",
        pos_cycle(9),
    )
    calc_ids.add("L2-ALT-V02-Q4")
    add_l2(
        questions, "L2-ALT-V02-Q4", SUBJECT, mod_v2, "Private Equity Waterfalls", "Preferred Return and Catch-Up",
        v2_id, v2_id, v2_title, v2_text,
        "Calculate and interpret DPI, RVPI, TVPI, IRR, and clawback provisions in private equity waterfalls.",
        rf"Suppose Fund IV's whole-of-fund waterfall distributes USD {proc_q4:.0f}M of gross proceeds on USD {pic_q4:.0f}M paid-in capital, with a cumulative preferred return obligation of USD {pref_q4:.0f}M, a 100% GP catch-up up to 20% of total profits, and an 80%/20% split thereafter. What are the final GP carry and net LP distributions?",
        opts, ans,
        rf"Total profit $= {proc_q4:.0f} - {pic_q4:.0f} = \text{{USD }} {tot_prof_q4:.0f}\text{{M}}$. Tier 1 returns USD {pic_q4:.0f}M capital to LPs; Tier 2 pays USD {pref_q4:.0f}M preferred return to LPs; Tier 3 pays 100% catch-up to GP of $\frac{{0.20}}{{0.80}} \times {pref_q4:.0f} = \text{{USD }} {catchup_q4:.2f}\text{{M}}$ (GP now holds 20% of USD 30M profit); Tier 4 splits remaining ${rem_q4:.0f}\text{{M}}$ 80/20, adding $0.20 \times {rem_q4:.0f} = \text{{USD }} 16.00\text{{M}}$ to GP. Total GP carry $= {catchup_q4:.2f} + 16.00 = \text{{USD }} {gp_carry_q4:.2f}\text{{M}}$, leaving $\text{{USD }} {lp_net_q4:.2f}\text{{M}}$ to LPs.",
        dist,
    )

    # Q5 (Concept): Escrow holdback & clawback credit risk
    opts, ans, dist = opt_pack(
        r"Escrow holdback accounts (retaining 20%-30% of interim deal-by-deal carry) mitigate LP counterparty risk when clawback obligations are otherwise limited to after-tax GP distributions.",
        r"Deal-by-deal waterfalls shift early timing risk onto the GP and permanently eliminate any need for clawback provisions.",
        r"Deal-by-deal waterfalls favor the GP by paying carry earlier and create clawback credit risk for LPs if later deals lose money.",
        r"Switching from a whole-of-fund waterfall to a deal-by-deal waterfall increases the LPs' net IRR whenever early exits win and late exits lose.",
        r"Paying carry early reduces LP net cash flows and lowers LP net IRR compared with deferring carry until all capital is returned.",
        pos_cycle(10),
    )
    add_l2(
        questions, "L2-ALT-V02-Q5", SUBJECT, mod_v2, "Private Equity Governance", "Clawback Protection Mechanisms",
        v2_id, v2_id, v2_title, v2_text,
        "Calculate and interpret DPI, RVPI, TVPI, IRR, and clawback provisions in private equity waterfalls.",
        r"To protect Pacific Pension Fund if Northbridge switches future funds to a deal-by-deal waterfall, which contractual protection is Chen most justified in requesting?",
        opts, ans,
        r"Because GPs often pay income tax on distributed carry and clawbacks are commonly capped at net-of-tax proceeds, requiring a 20%-30% escrow holdback plus personal partner guarantees directly protects LPs against clawback default.",
        dist,
    )

    # =========================================================================
    # V03: VC Method Multi-Round Pre/Post-Money & Dilution
    # =========================================================================
    v3_id = "ALT-V03"
    v3_title = "BioPulse Diagnostics: Multi-Round Venture Capital Valuation"
    v3_text = (
        "Priya Nair, Managing Director at Helix Ventures, is structuring a Series A investment in BioPulse Diagnostics, "
        "which currently has 4,000,000 common shares owned by its founders and an unallocated employee option pool already included inside those 4,000,000 shares.\n\n"
        "Series A Financing & Exit Projections:\n"
        "- Series A Investment Needed Today (Year 0): USD 8.00 million.\n"
        "- Projected Year 5 Exit Metrics: Net Earnings of USD 15.00 million; Comparable Exit P/E Multiple of 20.0x.\n"
        "- Helix Ventures Target Hurdle Rate (IRR): 40.0% per annum.\n"
        "- Anticipated Future Series B Financing (Year 2): Expected to issue new shares representing a 20.0% ownership stake in the company post-Series B (diluting Series A and founders by 20.0%, i.e., 80.0% retention).\n"
        "- Alternative Term Sheet Under Consideration: 1x non-participating convertible preferred vs. 1x participating preferred with a 3.0x total return cap (evaluated at an illustrative downside Year 5 exit of USD 40.00 million assuming no Series B occurred and Helix holds 25.0% post-Series-A ownership)."
    )
    mod_v3 = "Venture Capital Valuation"

    # Q1: Terminal Exit Value and required exit ownership share
    earn_y5, pe_exit, r_vc, t_vc, inv_a3 = 15.0, 20.0, 0.40, 5, 8.0
    term_v = earn_y5 * pe_exit  # 300.0M
    req_fv_a = inv_a3 * ((1 + r_vc) ** t_vc)  # 8 * 1.4^5 = 43.02592M
    req_exit_share = req_fv_a / term_v  # 14.342%
    w1_v3q1 = (inv_a3 / term_v) * 100
    w2_v3q1 = (req_fv_a / (term_v / (1 + r_vc))) * 100
    opts, ans, dist = opt_pack(
        rf"Exit Value = USD {term_v:.0f}M; Required Year 5 exit ownership = {req_exit_share * 100:.2f}%",
        rf"Exit Value = USD {term_v:.0f}M; Required Year 5 exit ownership = {w1_v3q1:.2f}%",
        r"Divides the USD 8.00M initial investment by the USD 300M terminal value without compounding at the 40% target IRR.",
        rf"Exit Value = USD {term_v:.0f}M; Required Year 5 exit ownership = {req_exit_share * 100 * 1.25:.2f}%",
        r"Applies a 25% markup instead of compounding strictly at $(1.40)^5$ over the 5-year holding horizon.",
        pos_cycle(11),
    )
    calc_ids.add("L2-ALT-V03-Q1")
    add_l2(
        questions, "L2-ALT-V03-Q1", SUBJECT, mod_v3, "VC Method", "Exit Value and Required Final Ownership",
        v3_id, v3_id, v3_title, v3_text,
        "Apply the venture capital method across multiple financing rounds with dilution and preferred payoffs.",
        r"What are BioPulse Diagnostics' projected Year 5 exit equity value and the minimum Year 5 exit ownership percentage Helix Ventures requires to achieve its 40.0% target IRR?",
        opts, ans,
        rf"Projected Year 5 exit value $= 15.00 \times 20.0 = \text{{USD }} {term_v:.0f}\text{{M}}$. Future value required by Helix at Year 5 is $8.00 \times 1.40^5 = \text{{USD }} {req_fv_a:.2f}\text{{M}}$. Required Year 5 ownership share $= \frac{{{req_fv_a:.2f}}}{{{term_v:.0f}}} = {req_exit_share * 100:.2f}\%$.",
        dist,
    )

    # Q2: Series A ownership required today accounting for 20% Series B dilution
    dil_b3 = 0.20
    req_init_share = req_exit_share / (1 - dil_b3)  # 17.9275%
    w1_v3q2 = req_exit_share * (1 - dil_b3) * 100
    w2_v3q2 = req_exit_share * 100
    opts, ans, dist = opt_pack(
        rf"{req_init_share * 100:.2f}%",
        rf"{w1_v3q2:.2f}%",
        r"Multiplies the required exit ownership by 0.80 instead of dividing by the 0.80 retention factor.",
        rf"{w2_v3q2:.2f}%",
        r"Fails to adjust Series A ownership for the 20% dilution caused by the anticipated Series B round.",
        pos_cycle(12),
    )
    calc_ids.add("L2-ALT-V03-Q2")
    add_l2(
        questions, "L2-ALT-V03-Q2", SUBJECT, mod_v3, "VC Method", "Dilution Adjustment",
        v3_id, v3_id, v3_title, v3_text,
        "Apply the venture capital method across multiple financing rounds with dilution and preferred payoffs.",
        r"Incorporating the expected 20.0% dilution from the future Series B financing, what Series A ownership percentage must Helix Ventures negotiate today?",
        opts, ans,
        rf"Because Series B retains $(1 - 0.20) = 80.0\%$ of Series A's stake, initial Series A ownership must be $\frac{{{req_exit_share * 100:.2f}\%}}{{0.80}} = {req_init_share * 100:.2f}\%$.",
        dist,
    )

    # Q3: Series A Post-Money, Pre-Money, and Share Price
    post_a = inv_a3 / req_init_share
    pre_a = post_a - inv_a3
    n_found = 4.0  # million shares
    p_sh_a = pre_a / n_found
    w1_v3q3 = post_a / n_found
    post_nodil = inv_a3 / req_exit_share
    w2_v3q3 = (post_nodil - inv_a3) / n_found
    opts, ans, dist = opt_pack(
        rf"Pre-Money = USD {pre_a:.2f}M; Series A Share Price = USD {p_sh_a:.2f}",
        rf"Pre-Money = USD {pre_a:.2f}M; Series A Share Price = USD {w1_v3q3:.2f}",
        r"Divides post-money valuation rather than pre-money valuation by the 4.0 million existing shares.",
        rf"Pre-Money = USD {post_nodil - inv_a3:.2f}M; Series A Share Price = USD {w2_v3q3:.2f}",
        r"Computes pre-money valuation using unadjusted exit ownership without Series B dilution.",
        pos_cycle(13),
    )
    calc_ids.add("L2-ALT-V03-Q3")
    add_l2(
        questions, "L2-ALT-V03-Q3", SUBJECT, mod_v3, "VC Method", "Pre-Money Valuation and Share Price",
        v3_id, v3_id, v3_title, v3_text,
        "Apply the venture capital method across multiple financing rounds with dilution and preferred payoffs.",
        r"Using the dilution-adjusted Series A ownership requirement, what are BioPulse's Series A pre-money valuation and price per share?",
        opts, ans,
        rf"Series A post-money valuation $= \frac{{\text{{USD }} 8.00\text{{M}}}}{{{req_init_share:.6f}}} = \text{{USD }} {post_a:.2f}\text{{M}}$. Pre-money valuation $= {post_a:.2f} - 8.00 = \text{{USD }} {pre_a:.2f}\text{{M}}$. Dividing by {n_found:.1f} million existing shares gives $\frac{{{pre_a:.2f}}}{{{n_found:.1f}}} = \text{{USD }} {p_sh_a:.2f}$ per share.",
        dist,
    )

    # Q4: Downside exit (USD 40M, 25% stake, USD 8M invested) -> Participating preferred with 3x cap vs non-participating
    exit_ds, stake_ds, inv_ds = 40.0, 0.25, 8.0
    # Participating with 3x cap: uncapped = 8 + 0.25*(40-8) = 16.0M; cap = 3*8 = 24.0M -> 16.0M!
    # Wait: make downside exit USD 80M? No, let's check: at 40M, 1x non-part gets max(8, 0.25*40) = 10.0M; 1x part gets 8 + 0.25*32 = 16.0M (under 24M cap)!
    pay_part = min(3 * inv_ds, inv_ds + stake_ds * (exit_ds - inv_ds))  # 16.0
    pay_nonpart = max(inv_ds, stake_ds * exit_ds)  # 10.0
    diff_pref = pay_part - pay_nonpart  # 6.0M
    w1_v3q4 = pay_nonpart
    w2_v3q4 = 3 * inv_ds  # hits 3x cap prematurely
    opts, ans, dist = opt_pack(
        rf"USD {pay_part:.2f} million (USD {diff_pref:.2f} million more than non-participating convertible preferred)",
        rf"USD {w1_v3q4:.2f} million (equal to non-participating convertible preferred)",
        r"Assumes Helix converts to common stock (25% of USD 40M) instead of receiving its liquidation preference plus participation.",
        rf"USD {w2_v3q4:.2f} million (capped at the 3.0x return ceiling)",
        r"Applies the 3.0x maximum return cap even though the USD 16.00M payoff lies below the USD 24.00M cap.",
        pos_cycle(14),
    )
    calc_ids.add("L2-ALT-V03-Q4")
    add_l2(
        questions, "L2-ALT-V03-Q4", SUBJECT, mod_v3, "VC Deal Terms", "Participating Preferred Payoff",
        v3_id, v3_id, v3_title, v3_text,
        "Apply the venture capital method across multiple financing rounds with dilution and preferred payoffs.",
        r"Under the illustrative USD 40.00 million downside exit (25.0% stake, USD 8.00M invested, no Series B), what payoff does Helix receive with 1x participating preferred (3.0x cap), and how does it compare with 1x non-participating convertible preferred?",
        opts, ans,
        rf"Under 1x participating preferred, Helix receives USD 8.00M preference plus $25\% \times (40.00 - 8.00) = \text{{USD }} 8.00\text{{M}}$ participation $= \text{{USD }} {pay_part:.2f}\text{{M}}$ (below the $3 \times 8.00 = \text{{USD }} 24.00\text{{M}}$ cap). Under 1x non-participating convertible preferred, Helix takes $\max(8.00, 0.25 \times 40.00) = \text{{USD }} {pay_nonpart:.2f}\text{{M}}$, a difference of USD {diff_pref:.2f}M.",
        dist,
    )

    # Q5 (Concept): Why VC hurdle rates are 30-50% vs CAPM
    opts, ans, dist = opt_pack(
        r"VC target hurdle rates embed survival/failure probability adjustments on single startups, severe illiquidity, and compensation for active operational mentoring—making them expected conditional success rates rather than realized fund returns.",
        r"VC target hurdle rates strictly reflect CAPM market beta multiplied by the historical equity risk premium.",
        r"Startups have low market liquidity and extreme idiosyncratic failure risk not captured by standard public-equity CAPM beta.",
        r"A 40% deal-level hurdle rate implies that diversified VC funds reliably compound aggregate LP capital at 40% net IRR.",
        r"Portfolio-wide realized VC returns are far lower than single-deal hurdle rates because write-offs drag down winners.",
        pos_cycle(15),
    )
    add_l2(
        questions, "L2-ALT-V03-Q5", SUBJECT, mod_v3, "VC Hurdle Rates", "Discount Rate Justification",
        v3_id, v3_id, v3_title, v3_text,
        "Apply the venture capital method across multiple financing rounds with dilution and preferred payoffs.",
        r"Why does Helix Ventures discount BioPulse's projected exit value at a 40.0% target hurdle rate rather than a standard public-equity CAPM cost of equity?",
        opts, ans,
        r"High VC discount rates adjust optimistic success-case terminal projections for the high probability of binary startup failure, long holding-period illiquidity, and the GP's active governance and mentoring contribution.",
        dist,
    )

    # =========================================================================
    # V04: LBO Value Attribution & Exit Multiple
    # =========================================================================
    v4_id = "ALT-V04"
    v4_title = "Sterling Industrial Partners: Titan Logistics LBO Valuation"
    v4_text = (
        "Daniel Brooks, Principal at Sterling Industrial Partners, prepares the Year 5 exit attribution memo for Titan Logistics.\n\n"
        "Entry Deal Structure (Year 0):\n"
        "- Entry LTM EBITDA: USD 50.00 million; Entry Enterprise Value Multiple: 8.0x EBITDA.\n"
        "- Debt Financing: Senior Term Loan at 4.0x Entry EBITDA + Subordinated Notes at 2.0x Entry EBITDA (Total Entry Debt = 6.0x EBITDA).\n"
        "- Sponsor Equity Contribution: Remainder of purchase price (ignoring transaction fees).\n\n"
        "Operating Performance & Exit (Year 5):\n"
        "- Year 5 Exit LTM EBITDA: USD 72.00 million.\n"
        "- Cumulative Free Cash Flow Debt Paydown (Years 1-5): USD 130.00 million (no interim equity dividends).\n"
        "- Exit Enterprise Value Multiple: 9.5x EBITDA.\n"
        "- Management Incentive Plan: Management receives 10.0% of total equity dollar gains above Sponsor's 1.0x initial equity cost."
    )
    mod_v4 = "Leveraged Buyout Value Attribution"

    eb0, m0, d_mult0 = 50.0, 8.0, 6.0
    ev0_4 = eb0 * m0  # 400
    debt0_4 = eb0 * d_mult0  # 300
    eq0_4 = ev0_4 - debt0_4  # 100
    eb5, m5, paydown4 = 72.0, 9.5, 130.0
    ev5_4 = eb5 * m5  # 684
    debt5_4 = debt0_4 - paydown4  # 170
    eq5_gross4 = ev5_4 - debt5_4  # 514
    gain_tot4 = eq5_gross4 - eq0_4  # 414

    # Attribution bridge (standard PE bridge):
    # 1. EBITDA Growth = (EBITDA5 - EBITDA0) * Entry Multiple = (72 - 50) * 8.0 = 176.0
    # 2. Multiple Expansion = (Exit Mult - Entry Mult) * Exit EBITDA = (9.5 - 8.0) * 72 = 108.0
    # (Wait: note check! 176 + 108 = 284 = 684 - 400 = delta EV! And Deleveraging = 130 -> 284 + 130 = 414 total equity gain!)
    attr_eb = (eb5 - eb0) * m0  # 176
    attr_mult = (m5 - m0) * eb5  # 108
    attr_del = paydown4  # 130
    assert abs((attr_eb + attr_mult + attr_del) - gain_tot4) < 1e-9

    # Q1: Entry Sponsor Equity & Gross Year 5 Exit Equity
    w1_v4q1 = ev5_4 - debt0_4
    w2_v4q1 = ev5_4 - paydown4
    opts, ans, dist = opt_pack(
        rf"Entry Equity = USD {eq0_4:.0f}M; Year 5 Gross Exit Equity = USD {eq5_gross4:.0f}M",
        rf"Entry Equity = USD {eq0_4:.0f}M; Year 5 Gross Exit Equity = USD {w1_v4q1:.0f}M",
        r"Subtracts initial entry debt (USD 300M) rather than reduced Year 5 debt (USD 170M) at exit.",
        rf"Entry Equity = USD {eq0_4:.0f}M; Year 5 Gross Exit Equity = USD {w2_v4q1:.0f}M",
        r"Subtracts debt repaid (USD 130M) instead of remaining exit debt (USD 170M) from Exit EV.",
        pos_cycle(16),
    )
    calc_ids.add("L2-ALT-V04-Q1")
    add_l2(
        questions, "L2-ALT-V04-Q1", SUBJECT, mod_v4, "LBO Mechanics", "Entry and Exit Equity Valuation",
        v4_id, v4_id, v4_title, v4_text,
        "Analyze leveraged buyout return drivers and attribute equity value creation.",
        r"What are Sterling Industrial Partners' initial equity investment and Year 5 gross exit equity value (before management equity dilution)?",
        opts, ans,
        rf"Entry EV $= 50 \times 8.0 = \text{{USD }} 400\text{{M}}$; Entry Debt $= 50 \times 6.0 = \text{{USD }} 300\text{{M}}$; Sponsor Equity $= 400 - 300 = \text{{USD }} {eq0_4:.0f}\text{{M}}$. At Year 5, Exit EV $= 72 \times 9.5 = \text{{USD }} {ev5_4:.0f}\text{{M}}$; Remaining Debt $= 300 - 130 = \text{{USD }} {debt5_4:.0f}\text{{M}}$; Gross Exit Equity $= {ev5_4:.0f} - {debt5_4:.0f} = \text{{USD }} {eq5_gross4:.0f}\text{{M}}$.",
        dist,
    )

    # Q2: Gross MOIC and Equity IRR
    moic4_gross = eq5_gross4 / eq0_4  # 5.14x
    irr4_gross = (moic4_gross ** (1 / 5) - 1) * 100
    w1_v4q2 = ((ev5_4 / ev0_4) ** (1 / 5) - 1) * 100
    w2_v4q2 = ((eq5_gross4 / eq0_4 - 1) / 5) * 100  # simple average annual return
    opts, ans, dist = opt_pack(
        rf"Gross MOIC = {moic4_gross:.2f}x; Gross Equity IRR = {irr4_gross:.2f}%",
        rf"Gross MOIC = {ev5_4 / ev0_4:.2f}x; Gross Equity IRR = {w1_v4q2:.2f}%",
        r"Reports the unlevered enterprise value multiple and CAGR rather than levered sponsor equity return.",
        rf"Gross MOIC = {moic4_gross:.2f}x; Gross Equity IRR = {w2_v4q2:.2f}%",
        r"Divides cumulative percentage gain linearly by 5 years instead of compounding geometrically.",
        pos_cycle(17),
    )
    calc_ids.add("L2-ALT-V04-Q2")
    add_l2(
        questions, "L2-ALT-V04-Q2", SUBJECT, mod_v4, "LBO Returns", "Gross MOIC and IRR",
        v4_id, v4_id, v4_title, v4_text,
        "Analyze leveraged buyout return drivers and attribute equity value creation.",
        r"Prior to the management incentive payout, what are the gross sponsor equity MOIC and annualized equity IRR over the 5-year holding period?",
        opts, ans,
        rf"Gross MOIC $= \frac{{{eq5_gross4:.0f}}}{{{eq0_4:.0f}}} = {moic4_gross:.2f}\text{{x}}$. Over 5 years with zero interim dividends, $\text{{IRR}} = ({moic4_gross:.2f})^{{1/5}} - 1 = {irr4_gross:.2f}\%$.",
        dist,
    )

    # Q3: LBO Value Attribution Bridge (% share of USD 414M gain)
    pct_eb = attr_eb / gain_tot4 * 100
    pct_mult = attr_mult / gain_tot4 * 100
    pct_del = attr_del / gain_tot4 * 100
    # Alternative split using Entry EBITDA for multiple expansion and Exit Mult for EBITDA growth -> explain convention cleanly!
    # Wait: if someone computes Multiple Expansion = (9.5 - 8.0)*50 = 75 and EBITDA growth = (72-50)*9.5 = 209, that swaps the interaction term! Let's specify "attributing the cross-product interaction to multiple expansion (applying exit multiple change to exit EBITDA)" or test the exact USD breakdown!
    w1_v4q3_eb = (eb5 - eb0) * m5
    w1_v4q3_mult = (m5 - m0) * eb0
    opts, ans, dist = opt_pack(
        rf"EBITDA Growth: USD {attr_eb:.0f}M ({pct_eb:.1f}%); Multiple Expansion: USD {attr_mult:.0f}M ({pct_mult:.1f}%); Deleveraging: USD {attr_del:.0f}M ({pct_del:.1f}%)",
        rf"EBITDA Growth: USD {w1_v4q3_eb:.0f}M ({w1_v4q3_eb / gain_tot4 * 100:.1f}%); Multiple Expansion: USD {w1_v4q3_mult:.0f}M ({w1_v4q3_mult / gain_tot4 * 100:.1f}%); Deleveraging: USD {attr_del:.0f}M ({pct_del:.1f}%)",
        r"Assigns the cross-product interaction term to EBITDA growth instead of multiple expansion.",
        rf"EBITDA Growth: USD {attr_eb:.0f}M ({attr_eb / (attr_eb + attr_mult) * 100:.1f}%); Multiple Expansion: USD {attr_mult:.0f}M ({attr_mult / (attr_eb + attr_mult) * 100:.1f}%); Deleveraging: USD 0M (0.0%)",
        r"Attributes only the USD 284M EV gain and omits the USD 130M equity contribution from debt paydown.",
        pos_cycle(18),
    )
    calc_ids.add("L2-ALT-V04-Q3")
    add_l2(
        questions, "L2-ALT-V04-Q3", SUBJECT, mod_v4, "LBO Value Creation", "Value Attribution Bridge",
        v4_id, v4_id, v4_title, v4_text,
        "Analyze leveraged buyout return drivers and attribute equity value creation.",
        r"Attributing EBITDA growth at the entry multiple and multiple expansion across exit EBITDA, how does the USD 414 million total gross equity gain break down across EBITDA growth, multiple expansion, and deleveraging?",
        opts, ans,
        rf"EBITDA growth $= (72 - 50) \times 8.0 = \text{{USD }} {attr_eb:.0f}\text{{M}}$ (${pct_eb:.1f}\%$). Multiple expansion $= (9.5 - 8.0) \times 72 = \text{{USD }} {attr_mult:.0f}\text{{M}}$ (${pct_mult:.1f}\%$). Deleveraging (debt paydown) $= \text{{USD }} {attr_del:.0f}\text{{M}}$ (${pct_del:.1f}\%$). Sum $= 176 + 108 + 130 = \text{{USD }} {gain_tot4:.0f}\text{{M}}$.",
        dist,
    )

    # Q4: Net Sponsor MOIC after 10% management profit-share
    mgmt_pool4 = 0.10 * gain_tot4  # 41.4M
    net_eq5_4 = eq5_gross4 - mgmt_pool4  # 472.6M
    net_moic4 = net_eq5_4 / eq0_4  # 4.726x -> 4.73x
    net_irr4 = (net_moic4 ** (1 / 5) - 1) * 100
    w1_v4q4 = (eq5_gross4 * 0.90) / eq0_4  # takes 10% of total exit equity instead of equity profit
    w2_v4q4 = (eq5_gross4 - 0.10 * (ev5_4 - ev0_4)) / eq0_4  # applies 10% to EV gain instead of equity gain
    opts, ans, dist = opt_pack(
        rf"Net Sponsor Equity = USD {net_eq5_4:.1f}M; Net MOIC = {net_moic4:.2f}x",
        rf"Net Sponsor Equity = USD {eq5_gross4 * 0.90:.1f}M; Net MOIC = {w1_v4q4:.2f}x",
        r"Awards management 10% of gross exit equity value rather than 10% of equity profits above Sterling's 1.0x cost.",
        rf"Net Sponsor Equity = USD {eq5_gross4 - 0.10 * (ev5_4 - ev0_4):.1f}M; Net MOIC = {w2_v4q4:.2f}x",
        r"Applies management's 10% profit share only to the enterprise value increase rather than total equity profit including debt paydown.",
        pos_cycle(19),
    )
    calc_ids.add("L2-ALT-V04-Q4")
    add_l2(
        questions, "L2-ALT-V04-Q4", SUBJECT, mod_v4, "LBO Returns", "Management Equity Dilution",
        v4_id, v4_id, v4_title, v4_text,
        "Analyze leveraged buyout return drivers and attribute equity value creation.",
        r"After deducting the management incentive pool (10.0% of equity dollar gains above Sterling's 1.0x initial equity), what are Sterling's net exit equity proceeds and net MOIC?",
        opts, ans,
        rf"Total equity gain $= {eq5_gross4:.0f} - {eq0_4:.0f} = \text{{USD }} {gain_tot4:.0f}\text{{M}}$. Management receives $10\% \times {gain_tot4:.0f} = \text{{USD }} {mgmt_pool4:.1f}\text{{M}}$. Sterling's net exit equity $= {eq5_gross4:.0f} - {mgmt_pool4:.1f} = \text{{USD }} {net_eq5_4:.1f}\text{{M}}$, yielding a net MOIC of $\frac{{{net_eq5_4:.1f}}}{{{eq0_4:.0f}}} = {net_moic4:.2f}\text{{x}}$.",
        dist,
    )

    # Q5 (Concept): Ideal LBO candidate characteristics & controllable drivers
    opts, ans, dist = opt_pack(
        r"Steady, predictable free cash flows and low capital intensity support high initial leverage and deleveraging, whereas exit multiple expansion depends heavily on external capital-market sentiment.",
        r"High cyclical earnings volatility and heavy R&D requirements make companies ideal LBO targets because interest tax shields stabilize cash burn.",
        r"High earnings volatility and heavy R&D capex impair debt service coverage and increase LBO distress risk.",
        r"Buyout sponsors rely primarily on unpredictable macro interest-rate cuts for multiple expansion rather than EBITDA growth.",
        r"Operational EBITDA expansion and debt paydown are controllable drivers; macro-driven multiple expansion is exogenous and unreliable.",
        pos_cycle(20),
    )
    add_l2(
        questions, "L2-ALT-V04-Q5", SUBJECT, mod_v4, "LBO Strategy", "Target Characteristics and Return Reliability",
        v4_id, v4_id, v4_title, v4_text,
        "Analyze leveraged buyout return drivers and attribute equity value creation.",
        r"When evaluating future deals for Sterling Industrial Partners, which statement best guides Brooks' underwriting of LBO value drivers?",
        opts, ans,
        r"Ideal LBO targets possess defensive market positions, stable margins, and strong cash conversion to service 5x-6x debt; operational EBITDA growth and deleveraging are controllable, whereas exit multiple expansion is subject to macro market risk.",
        dist,
    )

    # =========================================================================
    # V05: Direct Commercial Real Estate DCF & Reversion + DSCR/LTV Debt Sizing
    # =========================================================================
    v5_id = "ALT-V05"
    v5_title = "Harborview Tower: Commercial Real Estate DCF and Debt Sizing"
    v5_text = (
        "Sophia Martinez, Director of Real Estate Acquisitions at Harborstone Capital, is underwriting the acquisition "
        "of Harborview Tower, a stabilized Class A mixed-use property.\n\n"
        "Operating Cash Flow Schedule (USD millions):\n"
        "- Year 1 Potential Gross Income (PGI): USD 12.00M; Vacancy & Collection Loss: 10.0%; Operating Expenses: USD 4.20M.\n"
        "- Projected Annual NOI: Year 1 as calculated above; Year 2: USD 7.00M; Year 3: USD 7.35M; Year 4: USD 7.70M.\n\n"
        "Valuation & Transaction Assumptions:\n"
        "- Comparable Market Going-In Cap Rate: 6.25%.\n"
        "- DCF Underwriting Horizon: 3 years; Discount Rate (Unlevered Required Return): 8.50%.\n"
        "- Exit Cap Rate at End of Year 3: 6.50% applied to Year 4 NOI, less 2.50% selling costs on gross exit price.\n\n"
        "Senior Debt Terms (Evaluated against Direct Cap Property Value):\n"
        "- Maximum LTV: 65.0%; Minimum Year 1 DSCR: 1.35x; Interest-Only Loan Rate: 5.80% vs. 25-year Amortizing Loan Constant: 7.40% (for Q3, use the 25-year amortizing constant of 7.40%)."
    )
    mod_v5 = "Commercial Real Estate Valuation & Financing"

    pgi5, vac5, opex5 = 12.0, 0.10, 4.20
    noi1_5 = pgi5 * (1 - vac5) - opex5  # 10.80 - 4.20 = 6.60M
    noi2_5, noi3_5, noi4_5 = 7.00, 7.35, 7.70
    cap_in5, cap_out5, sell_c5, disc5 = 0.0625, 0.065, 0.025, 0.085
    dir_cap_v5 = noi1_5 / cap_in5  # 6.60 / 0.0625 = 105.60M

    # Q1: Year 1 NOI and Direct Cap Value
    w1_v5q1 = (pgi5 - opex5) / cap_in5
    w2_v5q1 = noi1_5 / cap_out5
    opts, ans, dist = opt_pack(
        rf"Year 1 NOI = USD {noi1_5:.2f}M; Direct Cap Value = USD {dir_cap_v5:.2f}M",
        rf"Year 1 NOI = USD {pgi5 - opex5:.2f}M; Direct Cap Value = USD {w1_v5q1:.2f}M",
        r"Fails to deduct the 10.0% vacancy and collection loss from PGI when computing Year 1 NOI.",
        rf"Year 1 NOI = USD {noi1_5:.2f}M; Direct Cap Value = USD {w2_v5q1:.2f}M",
        r"Applies the Year 3 exit cap rate (6.50%) rather than the market going-in cap rate (6.25%).",
        pos_cycle(21),
    )
    calc_ids.add("L2-ALT-V05-Q1")
    add_l2(
        questions, "L2-ALT-V05-Q1", SUBJECT, mod_v5, "Real Estate Valuation", "NOI and Direct Capitalization",
        v5_id, v5_id, v5_title, v5_text,
        "Value commercial real estate via direct capitalization and DCF and determine binding debt capacity.",
        r"What are Harborview Tower's Year 1 NOI and implied Direct Capitalization valuation?",
        opts, ans,
        rf"Year 1 Effective Gross Income $= 12.00 \times (1 - 0.10) = \text{{USD }} 10.80\text{{M}}$; $\text{{NOI}}_1 = 10.80 - 4.20 = \text{{USD }} {noi1_5:.2f}\text{{M}}$. Direct Cap Value $= \frac{{{noi1_5:.2f}}}{{0.0625}} = \text{{USD }} {dir_cap_v5:.2f}\text{{M}}$.",
        dist,
    )

    # Q2: 3-year DCF valuation
    gross_rev5 = noi4_5 / cap_out5
    net_rev5 = gross_rev5 * (1 - sell_c5)
    pv_noiy = noi1_5 / (1 + disc5) + noi2_5 / ((1 + disc5) ** 2) + noi3_5 / ((1 + disc5) ** 3)
    pv_rev5 = net_rev5 / ((1 + disc5) ** 3)
    dcf_v5 = pv_noiy + pv_rev5
    w1_v5q2 = pv_noiy + gross_rev5 / ((1 + disc5) ** 3)  # omits 2.5% selling costs
    w2_v5q2 = pv_noiy + ((noi3_5 / cap_out5) * (1 - sell_c5)) / ((1 + disc5) ** 3)  # capitalizes Y3 NOI
    opts, ans, dist = opt_pack(
        rf"USD {dcf_v5:.2f} million",
        rf"USD {w1_v5q2:.2f} million",
        r"Omits the 2.50% selling costs from the Year 3 gross reversion price.",
        rf"USD {w2_v5q2:.2f} million",
        r"Capitalizes Year 3 NOI instead of forward Year 4 NOI when computing Year 3 terminal value.",
        pos_cycle(22),
    )
    calc_ids.add("L2-ALT-V05-Q2")
    add_l2(
        questions, "L2-ALT-V05-Q2", SUBJECT, mod_v5, "Real Estate Valuation", "3-Year Property DCF",
        v5_id, v5_id, v5_title, v5_text,
        "Value commercial real estate via direct capitalization and DCF and determine binding debt capacity.",
        r"Using the 3-year DCF model at an 8.50% discount rate, what is Harborview Tower's estimated value today?",
        opts, ans,
        rf"Year 3 gross reversion $= \frac{{7.70}}{{0.065}} = \text{{USD }} {gross_rev5:.2f}\text{{M}}$; net of 2.50% selling costs $= \text{{USD }} {net_rev5:.2f}\text{{M}}$. Discounting at 8.50%: $\text{{PV}}(\text{{NOI}}_{{1\text{{-}}3}}) = \frac{{6.60}}{{1.085}} + \frac{{7.00}}{{1.085^2}} + \frac{{7.35}}{{1.085^3}} = {pv_noiy:.2f}\text{{M}}$; $\text{{PV}}(\text{{Reversion}}) = \frac{{{net_rev5:.2f}}}{{1.085^3}} = {pv_rev5:.2f}\text{{M}}$. Total DCF value $= \text{{USD }} {dcf_v5:.2f}\text{{M}}$.",
        dist,
    )

    # Q3: Debt sizing LTV vs DSCR (against Direct Cap value 105.60M)
    loan_ltv5 = dir_cap_v5 * 0.65  # 68.64M
    max_ds5 = noi1_5 / 1.35  # 4.8889M
    loan_dscr5 = max_ds5 / 0.074  # 66.066M
    bind_loan5 = min(loan_ltv5, loan_dscr5)
    w1_v5q3 = loan_ltv5
    w2_v5q3 = max_ds5 / 0.058  # uses IO rate 5.80% instead of 7.40% amortizing constant (Wait: min(68.64, 84.29) -> if someone ignored LTV and used IO!)
    opts, ans, dist = opt_pack(
        rf"USD {bind_loan5:.2f} million (constrained by DSCR)",
        rf"USD {w1_v5q3:.2f} million (constrained by LTV)",
        r"Applies the 65% LTV ceiling without checking that the 1.35x DSCR constraint is tighter.",
        rf"USD {w2_v5q3:.2f} million (constrained by DSCR)",
        r"Divides maximum debt service by the 5.80% interest-only rate rather than the 7.40% amortizing loan constant and breaches LTV.",
        pos_cycle(23),
    )
    calc_ids.add("L2-ALT-V05-Q3")
    add_l2(
        questions, "L2-ALT-V05-Q3", SUBJECT, mod_v5, "Real Estate Debt Sizing", "Binding Loan Constraint",
        v5_id, v5_id, v5_title, v5_text,
        "Value commercial real estate via direct capitalization and DCF and determine binding debt capacity.",
        r"Evaluating the 25-year amortizing loan (7.40% debt constant) against Harborview Tower's Direct Capitalization value (USD 105.60M), what is the maximum loan the lender will extend and which constraint binds?",
        opts, ans,
        rf"LTV cap $= 0.65 \times 105.60 = \text{{USD }} {loan_ltv5:.2f}\text{{M}}$. DSCR cap: maximum annual debt service $= \frac{{6.60}}{{1.35}} = \text{{USD }} {max_ds5:.2f}\text{{M}}$, supporting a loan of $\frac{{{max_ds5:.2f}}}{{0.074}} = \text{{USD }} {loan_dscr5:.2f}\text{{M}}$. Because ${loan_dscr5:.2f} < {loan_ltv5:.2f}$, the 1.35x DSCR binds at USD {bind_loan5:.2f}M.",
        dist,
    )

    # Q4: Levered Year 1 cash-on-cash return (equity dividend rate) at purchase price = Direct Cap Value 105.60M with binding loan 66.07M
    eq_init5 = dir_cap_v5 - bind_loan5  # 105.60 - 66.066 = 39.534M
    ds_actual5 = bind_loan5 * 0.074  # 4.8889M (= max_ds5)
    btcf5 = noi1_5 - ds_actual5  # 1.7111M
    coc5 = btcf5 / eq_init5 * 100  # 4.33%
    # Wait: what if loan was LTV-bound (68.64)? Or omitted equity deduction?
    w1_v5q4 = noi1_5 / eq_init5 * 100  # forgets to subtract debt service
    w2_v5q4 = (noi1_5 - loan_ltv5 * 0.074) / (dir_cap_v5 - loan_ltv5) * 100
    opts, ans, dist = opt_pack(
        rf"{coc5:.2f}%",
        rf"{w1_v5q4:.2f}%",
        r"Divides unlevered Year 1 NOI by initial equity without subtracting annual debt service.",
        rf"{w2_v5q4:.2f}%",
        r"Computes cash-on-cash yield using the unapproved 65% LTV loan amount rather than the binding DSCR-capped loan.",
        pos_cycle(24),
    )
    calc_ids.add("L2-ALT-V05-Q4")
    add_l2(
        questions, "L2-ALT-V05-Q4", SUBJECT, mod_v5, "Real Estate Returns", "Equity Dividend Rate (Cash-on-Cash)",
        v5_id, v5_id, v5_title, v5_text,
        "Value commercial real estate via direct capitalization and DCF and determine binding debt capacity.",
        r"Assuming Harborstone acquires Harborview Tower at its Direct Capitalization value (USD 105.60M) financed by the binding DSCR-constrained amortizing loan, what is Year 1 before-tax cash-on-cash equity return (equity dividend rate)?",
        opts, ans,
        rf"Initial equity $= 105.60 - {bind_loan5:.2f} = \text{{USD }} {eq_init5:.2f}\text{{M}}$. Annual debt service $= {bind_loan5:.2f} \times 7.40\% = \text{{USD }} {ds_actual5:.2f}\text{{M}}$, leaving Year 1 before-tax cash flow $= 6.60 - {ds_actual5:.2f} = \text{{USD }} {btcf5:.2f}\text{{M}}$. Cash-on-cash return $= \frac{{{btcf5:.2f}}}{{{eq_init5:.2f}}} = {coc5:.2f}\%$.",
        dist,
    )

    # Q5 (Concept): Term & Reversion vs Direct Cap when in-place rent < market rent
    opts, ans, dist = opt_pack(
        r"When existing leases are materially below current market rent, a multi-year DCF or term-and-reversion approach accurately separates below-market contract cash flows from the higher post-lease market reversion.",
        r"Direct capitalization on depressed Year 1 NOI automatically reflects future lease mark-to-market rent step-ups at Year 4.",
        r"Simple direct capitalization assumes Year 1 NOI grows forever at a constant rate and undervalues properties with imminent above-trend lease rollovers.",
        r"Raising the exit capitalization rate increases the Year 3 reversion value by compressing the capitalization denominator.",
        r"Higher exit cap rates reduce terminal reversion value because exit value equals forward NOI divided by the exit cap rate.",
        pos_cycle(25),
    )
    add_l2(
        questions, "L2-ALT-V05-Q5", SUBJECT, mod_v5, "Real Estate Methodologies", "DCF vs. Direct Capitalization",
        v5_id, v5_id, v5_title, v5_text,
        "Value commercial real estate via direct capitalization and DCF and determine binding debt capacity.",
        r"Which valuation judgment should Martinez emphasize if Harborview Tower currently has legacy leases priced 20% below market expiring in Year 3?",
        opts, ans,
        r"Because direct capitalization applies a single stabilized rate to Year 1 NOI, explicit DCF or term-and-reversion modeling is superior whenever irregular lease-up, rent resets, or scheduled capital expenditures alter cash-flow timing.",
        dist,
    )


def build_l2_v06_v10(questions: list, calc_ids: set):
    """Build Vignettes ALT-V06 through ALT-V10 (25 L2 questions)."""

    # =========================================================================
    # V06: Public REIT NAVPS & P/FFO/P/AFFO Valuation
    # =========================================================================
    v6_id = "ALT-V06"
    v6_title = "MetroCore Industrial REIT: FFO, AFFO, and NAVPS Valuation"
    v6_text = (
        "Liam O'Connor, Equity REIT Analyst at Crestline Asset Management, is valuing MetroCore Industrial REIT (MCIR).\n\n"
        "MCIR Selected Financial Data (USD millions, except share price and share count):\n"
        "- GAAP Net Income: USD 210.00M\n"
        "- Real Estate Depreciation & Amortization: USD 145.00M\n"
        "- Gains on Property Dispositions: USD 25.00M\n"
        "- Non-Cash Straight-Line Rent Revenue Adjustment: USD 14.00M (GAAP rent exceeds cash rent)\n"
        "- Recurring Maintenance CapEx & Leasing Commissions: USD 36.00M\n"
        "- Annualized Forward Cash NOI (excluding straight-line rent): USD 420.00M\n"
        "- Cash and Other Tangible Non-Property Assets: USD 160.00M\n"
        "- Total Debt & Other Liabilities: USD 2,860.00M\n"
        "- Common Shares Outstanding: 120.00 million; Current Share Price: USD 39.00\n\n"
        "Market & Peer Valuation Benchmarks:\n"
        "- Market Capitalization Rate for Prime Logistics Properties: 5.25%\n"
        "- Industrial REIT Peer Group Average Multiples: P/FFO = 16.0x; P/AFFO = 18.5x."
    )
    mod_v6 = "Public REIT Valuation"

    ni6, da6, gain6, sl6, mcap6, sh6, px6 = 210.0, 145.0, 25.0, 14.0, 36.0, 120.0, 39.0
    ffo6 = ni6 + da6 - gain6  # 330.0
    ffops6 = ffo6 / sh6  # 2.75
    affo6 = ffo6 - sl6 - mcap6  # 280.0
    affops6 = affo6 / sh6  # 2.3333
    # Property value = 420 / 0.0525 = 8000.0; NAV = 8000 + 160 - 2860 = 5300.0; NAVPS = 5300 / 120 = 44.1667
    noi6, cap6, cash6, debt6 = 420.0, 0.0525, 160.0, 2860.0
    pv_re6 = noi6 / cap6  # 8000.0
    nav6 = pv_re6 + cash6 - debt6  # 5300.0
    navps6 = nav6 / sh6  # 44.17
    prem_disc6 = (px6 - navps6) / navps6 * 100  # -11.70%

    # Q1: FFO and FFO per share
    w1_v6q1 = (ni6 + da6 + gain6) / sh6  # adds gains
    w2_v6q1 = (ni6 + da6) / sh6  # ignores gains
    opts, ans, dist = opt_pack(
        rf"FFO = USD {ffo6:.2f}M; FFO/share = USD {ffops6:.2f}",
        rf"FFO = USD {ni6 + da6 + gain6:.2f}M; FFO/share = USD {w1_v6q1:.2f}",
        r"Adds gains on property sales to GAAP net income instead of subtracting non-operating disposition gains.",
        rf"FFO = USD {ni6 + da6:.2f}M; FFO/share = USD {w2_v6q1:.2f}",
        r"Adds back depreciation and amortization without excluding gains on property dispositions.",
        pos_cycle(26),
    )
    calc_ids.add("L2-ALT-V06-Q1")
    add_l2(
        questions, "L2-ALT-V06-Q1", SUBJECT, mod_v6, "REIT Cash Flows", "FFO Calculation",
        v6_id, v6_id, v6_title, v6_text,
        "Calculate and interpret REIT FFO, AFFO, NAVPS, and implied capitalization rate.",
        r"What are MetroCore Industrial REIT's Funds From Operations (FFO) and FFO per share?",
        opts, ans,
        rf"$\text{{FFO}} = \text{{Net Income}} + \text{{Real Estate D\&A}} - \text{{Gains on Property Sales}} = 210 + 145 - 25 = \text{{USD }} {ffo6:.2f}\text{{M}}$. $\text{{FFO/share}} = \frac{{{ffo6:.2f}}}{{{sh6:.0f}}} = \text{{USD }} {ffops6:.2f}$.",
        dist,
    )

    # Q2: AFFO and AFFO per share
    w1_v6q2 = (ffo6 - mcap6) / sh6  # forgets straight-line rent
    w2_v6q2 = (ffo6 + sl6 - mcap6) / sh6  # adds straight-line rent
    opts, ans, dist = opt_pack(
        rf"AFFO = USD {affo6:.2f}M; AFFO/share = USD {affops6:.2f}",
        rf"AFFO = USD {ffo6 - mcap6:.2f}M; AFFO/share = USD {w1_v6q2:.2f}",
        r"Deducts recurring CapEx and leasing commissions but omits the non-cash straight-line rent subtraction.",
        rf"AFFO = USD {ffo6 + sl6 - mcap6:.2f}M; AFFO/share = USD {w2_v6q2:.2f}",
        r"Adds the straight-line rent excess rather than subtracting it from FFO.",
        pos_cycle(27),
    )
    calc_ids.add("L2-ALT-V06-Q2")
    add_l2(
        questions, "L2-ALT-V06-Q2", SUBJECT, mod_v6, "REIT Cash Flows", "AFFO Calculation",
        v6_id, v6_id, v6_title, v6_text,
        "Calculate and interpret REIT FFO, AFFO, NAVPS, and implied capitalization rate.",
        r"What are MetroCore Industrial REIT's Adjusted Funds From Operations (AFFO) and AFFO per share?",
        opts, ans,
        rf"$\text{{AFFO}} = \text{{FFO}} - \text{{Straight-line rent}} - \text{{Maintenance CapEx \& Leasing}} = {ffo6:.0f} - {sl6:.0f} - {mcap6:.0f} = \text{{USD }} {affo6:.2f}\text{{M}}$. $\text{{AFFO/share}} = \frac{{{affo6:.2f}}}{{{sh6:.0f}}} = \text{{USD }} {affops6:.2f}$.",
        dist,
    )

    # Q3: NAVPS and premium/discount
    w1_v6q3 = (pv_re6 - debt6) / sh6  # forgets cash
    w2_v6q3 = (pv_re6 + cash6 + debt6) / sh6  # adds debt instead of subtracting
    opts, ans, dist = opt_pack(
        rf"NAVPS = USD {navps6:.2f}; trading at an {abs(prem_disc6):.1f}% discount to NAVPS",
        rf"NAVPS = USD {w1_v6q3:.2f}; trading at a {abs((px6 - w1_v6q3) / w1_v6q3 * 100):.1f}% discount to NAVPS",
        r"Excludes the USD 160M of cash and tangible non-property assets when calculating total NAV.",
        rf"NAVPS = USD {w2_v6q3:.2f}; trading at a {abs((px6 - w2_v6q3) / w2_v6q3 * 100):.1f}% discount to NAVPS",
        r"Adds total debt and liabilities to gross real estate value instead of subtracting liabilities.",
        pos_cycle(28),
    )
    calc_ids.add("L2-ALT-V06-Q3")
    add_l2(
        questions, "L2-ALT-V06-Q3", SUBJECT, mod_v6, "REIT Valuation", "NAVPS and Market Discount",
        v6_id, v6_id, v6_title, v6_text,
        "Calculate and interpret REIT FFO, AFFO, NAVPS, and implied capitalization rate.",
        r"Based on the 5.25% market capitalization rate, what is MCIR's Net Asset Value Per Share (NAVPS) and how does its current USD 39.00 share price trade relative to NAVPS?",
        opts, ans,
        rf"Estimated property portfolio value $= \frac{{420.00}}{{0.0525}} = \text{{USD }} {pv_re6:,.0f}\text{{M}}$. $\text{{NAV}} = {pv_re6:,.0f} + {cash6:.0f} - {debt6:,.0f} = \text{{USD }} {nav6:,.0f}\text{{M}}$; $\text{{NAVPS}} = \frac{{{nav6:,.0f}}}{{{sh6:.0f}}} = \text{{USD }} {navps6:.2f}$. At USD {px6:.2f}, MCIR trades at $\frac{{{px6:.2f} - {navps6:.2f}}}{{{navps6:.2f}}} = {prem_disc6:.1f}\%$ (an {abs(prem_disc6):.1f}% discount).",
        dist,
    )

    # Q4: Peer P/AFFO Valuation & Implied Cap Rate at current price
    fair_p_affo = affops6 * 18.5  # 43.17
    mkt_cap6 = px6 * sh6  # 4680
    imp_ev6 = mkt_cap6 + debt6 - cash6  # 4680 + 2860 - 160 = 7380
    imp_cap6 = (noi6 / imp_ev6) * 100  # 420 / 7380 = 5.69%
    w1_v6q4 = (noi6 / (mkt_cap6 + debt6)) * 100  # omits cash deduction from EV
    w2_v6q4 = affops6 * 16.0  # applies P/FFO multiple to AFFO/share
    opts, ans, dist = opt_pack(
        rf"Peer P/AFFO value = USD {fair_p_affo:.2f}/share; Implied Cap Rate = {imp_cap6:.2f}%",
        rf"Peer P/AFFO value = USD {fair_p_affo:.2f}/share; Implied Cap Rate = {w1_v6q4:.2f}%",
        r"Omits subtracting the USD 160M cash balance from enterprise value when calculating the implied cap rate.",
        rf"Peer P/AFFO value = USD {w2_v6q4:.2f}/share; Implied Cap Rate = {imp_cap6:.2f}%",
        r"Applies the peer P/FFO multiple (16.0x) to AFFO per share instead of the peer P/AFFO multiple (18.5x).",
        pos_cycle(29),
    )
    calc_ids.add("L2-ALT-V06-Q4")
    add_l2(
        questions, "L2-ALT-V06-Q4", SUBJECT, mod_v6, "REIT Valuation", "Relative Multiple and Implied Cap Rate",
        v6_id, v6_id, v6_title, v6_text,
        "Calculate and interpret REIT FFO, AFFO, NAVPS, and implied capitalization rate.",
        r"What are MCIR's peer P/AFFO-implied fair share value and the implied capitalization rate at its current USD 39.00 share price?",
        opts, ans,
        rf"Peer P/AFFO implied share price $= \text{{USD }} {affops6:.4f} \times 18.5 = \text{{USD }} {fair_p_affo:.2f}$. At USD {px6:.2f}/share, Equity Market Cap $= 39 \times 120 = \text{{USD }} {mkt_cap6:,.0f}\text{{M}}$; Implied Real Estate Value (EV) $= {mkt_cap6:,.0f} + {debt6:,.0f} - {cash6:.0f} = \text{{USD }} {imp_ev6:,.0f}\text{{M}}$; Implied Cap Rate $= \frac{{420}}{{{imp_ev6:,.0f}}} = {imp_cap6:.2f}\%$.",
        dist,
    )

    # Q5 (Concept): AFFO superiority & NAV discount persistence
    opts, ans, dist = opt_pack(
        r"AFFO better approximates recurring distributable cash flow by deducting maintenance CapEx and non-cash straight-line rent, while persistent NAV discounts often reflect high G&A costs, governance flaws, or elevated balance-sheet leverage.",
        r"GAAP P/E is superior to P/AFFO for REIT valuation because historical depreciation accurately measures property appreciation.",
        r"Historical-cost accounting depreciation typically overstates economic value loss on well-maintained real estate, distorting GAAP net income downward.",
        r"A REIT trading at a discount to NAVPS is always guaranteed to converge upward to NAVPS within 12 months regardless of management quality.",
        r"Value traps persist when poor capital allocation, conflicts of interest, or prohibitive debt prevent NAV realization.",
        pos_cycle(30),
    )
    add_l2(
        questions, "L2-ALT-V06-Q5", SUBJECT, mod_v6, "REIT Analysis", "AFFO vs. NAVPS Interpretation",
        v6_id, v6_id, v6_title, v6_text,
        "Calculate and interpret REIT FFO, AFFO, NAVPS, and implied capitalization rate.",
        r"Which conclusion best supports O'Connor's investment memo comparing P/AFFO and NAVPS for MCIR?",
        opts, ans,
        r"AFFO captures true economic cash available for dividends and growth after recurring CapEx and straight-line accruals; persistent public-market discounts to NAVPS can reflect excessive overhead, leverage concerns, or capital-allocation skepticism.",
        dist,
    )

    # =========================================================================
    # V07: Hedge Fund Conditional Factor Risk & Merger/Convertible Arbitrage
    # =========================================================================
    v7_id = "ALT-V07"
    v7_title = "Vanguard Ridge Multi-Strategy: Arbitrage Trades and Conditional Risk"
    v7_text = (
        "Hannah Park, Risk Manager at Vanguard Ridge Multi-Strategy Fund, is reviewing three quantitative sleeves:\n\n"
        "Sleeve 1 — Merger Arbitrage Trade (Cash + Stock Offer):\n"
        "- Target (AlphaCorp) current price: USD 56.00; Acquirer (BetaTech) current price: USD 80.00.\n"
        "- Announced Deal Terms: BetaTech will pay USD 24.00 cash plus 0.45 BetaTech shares for each AlphaCorp share, expected to close in 120 days (365-day year).\n"
        "- If regulatory blockage breaks the deal, AlphaCorp is projected to fall to USD 44.00 (and BetaTech stays near USD 80.00).\n\n"
        "Sleeve 2 — Convertible Arbitrage Position:\n"
        "- Fund purchases 1,000 convertible bonds (USD 1,000 par each; total par USD 1.00M) at 105% of par (USD 1,050,000), paying a 4.00% annual coupon.\n"
        "- Conversion Ratio: 20 shares per bond; Stock Price: USD 48.00; Bond Delta: 0.60; Stock pays zero dividends.\n"
        "- Short stock proceeds earn 4.50% rebate minus a 1.00% stock-borrow fee (net +3.50% short rebate on short market value), while bond purchase is funded at 5.00% prime borrowing cost on the USD 1,050,000 purchase price.\n\n"
        "Sleeve 3 — Conditional Factor Regression (Monthly Excess Returns):\n"
        "- Multi-Strategy Fund Model: $R_p - R_f = 0.35\\% + 0.15(R_m - R_f) + 0.55 D_{\\text{crisis}}(R_m - R_f) + \\varepsilon$, where $D_{\\text{crisis}} = 1$ when monthly equity excess return $(R_m - R_f) < -4.0\\%$, and $0$ otherwise."
    )
    mod_v7 = "Hedge Fund Arbitrage & Factor Risk"

    # Q1: Merger Arb spread, annualized return, and break-even deal completion probability
    p_tgt7, p_acq7, cash_o7, ratio7, days7, p_break7 = 56.0, 80.0, 24.0, 0.45, 120, 44.0
    offer_v7 = cash_o7 + ratio7 * p_acq7  # 24 + 36 = 60.0
    spread7 = offer_v7 - p_tgt7  # +4.00 gain if closes
    loss_break7 = p_tgt7 - p_break7  # -12.00 loss if breaks
    # Break-even p: p * 4.00 - (1 - p) * 12.00 = 0 -> 16p = 12 -> p = 75.0%!
    be_prob7 = loss_break7 / (spread7 + loss_break7) * 100  # 75.0%
    ann_ret7 = (spread7 / p_tgt7) * (365 / days7) * 100  # (4/56)*(365/120) = 21.73%
    w1_v7q1 = (spread7 / offer_v7) * (365 / days7) * 100
    w2_v7q1 = (spread7 / loss_break7) * 100  # wrong break-even probability = 33.3%
    opts, ans, dist = opt_pack(
        rf"Annualized return = {ann_ret7:.2f}%; Implied break-even probability = {be_prob7:.1f}%",
        rf"Annualized return = {w1_v7q1:.2f}%; Implied break-even probability = {be_prob7:.1f}%",
        r"Divides the USD 4.00 deal spread by the USD 60.00 offer value instead of the USD 56.00 target cost.",
        rf"Annualized return = {ann_ret7:.2f}%; Implied break-even probability = {100 - be_prob7:.1f}%",
        r"Computes the implied break-even failure probability (25.0%) rather than the completion probability (75.0%).",
        pos_cycle(31),
    )
    calc_ids.add("L2-ALT-V07-Q1")
    add_l2(
        questions, "L2-ALT-V07-Q1", SUBJECT, mod_v7, "Event-Driven Arbitrage", "Merger Arbitrage Spread and Implied Probability",
        v7_id, v7_id, v7_title, v7_text,
        "Evaluate merger arbitrage, convertible arbitrage, and conditional factor exposures in hedge funds.",
        r"For Sleeve 1 (ignoring financing costs), what are the annualized simple spread return if the deal closes on time and the break-even probability of deal completion?",
        opts, ans,
        rf"Deal offer value $= 24.00 + 0.45(80.00) = \text{{USD }} {offer_v7:.2f}$. Spread $= 60.00 - 56.00 = \text{{USD }} {spread7:.2f}$. Annualized return $= \frac{{4.00}}{{56.00}} \times \frac{{365}}{{120}} = {ann_ret7:.2f}\%$. Downside on break $= 56.00 - 44.00 = \text{{USD }} {loss_break7:.2f}$. Setting $p({spread7:.2f}) - (1-p)({loss_break7:.2f}) = 0$ gives $p = \frac{{12}}{{12 + 4}} = {be_prob7:.1f}\%$.",
        dist,
    )

    # Q2: Convertible Arb delta hedge short shares & net annual dollar carry
    n_cb7, cb_val7, cpn_r7, cr7, stk7, del7, short_reb7, fin_r7 = 1000, 1050000.0, 0.04, 20, 48.0, 0.60, 0.035, 0.05
    sh_short7 = n_cb7 * cr7 * del7  # 12,000 shares
    short_val7 = sh_short7 * stk7  # 576,000
    cpn_inc7 = n_cb7 * 1000 * cpn_r7  # 40,000
    reb_inc7 = short_val7 * short_reb7  # 20,160
    fin_cost7 = cb_val7 * fin_r7  # 52,500
    net_carry7 = cpn_inc7 + reb_inc7 - fin_cost7  # +7,660
    w1_v7q2 = cpn_inc7 - fin_cost7  # omits short stock rebate income
    w2_v7q2 = cpn_inc7 + (n_cb7 * cr7 * stk7 * short_reb7) - fin_cost7  # uses delta=1 for short value
    opts, ans, dist = opt_pack(
        rf"Short {sh_short7:,.0f} shares; Net annual carry = +USD {net_carry7:,.0f}",
        rf"Short {sh_short7:,.0f} shares; Net annual carry = -USD {abs(w1_v7q2):,.0f}",
        r"Omits the +3.50% net short rebate earned on the USD 576,000 short stock proceeds.",
        rf"Short {n_cb7 * cr7:,.0f} shares; Net annual carry = +USD {w2_v7q2:,.0f}",
        r"Hedges using a 1.00 conversion delta (20,000 shares) instead of the 0.60 bond delta (12,000 shares).",
        pos_cycle(32),
    )
    calc_ids.add("L2-ALT-V07-Q2")
    add_l2(
        questions, "L2-ALT-V07-Q2", SUBJECT, mod_v7, "Relative Value Arbitrage", "Convertible Arbitrage Delta Hedge and Carry",
        v7_id, v7_id, v7_title, v7_text,
        "Evaluate merger arbitrage, convertible arbitrage, and conditional factor exposures in hedge funds.",
        r"In Sleeve 2, how many shares must the fund short for a delta-neutral hedge, and what is the position's annual net dollar carry?",
        opts, ans,
        rf"Short shares $= 1,000 \times 20 \times 0.60 = {sh_short7:,.0f}$ shares, generating short proceeds of ${sh_short7:,.0f} \times 48 = \text{{USD }} {short_val7:,.0f}$. Annual cash carry: Coupon $= 1,000,000 \times 4.00\% = +\text{{USD }} {cpn_inc7:,.0f}$; Net short rebate $= {short_val7:,.0f} \times 3.50\% = +\text{{USD }} {reb_inc7:,.0f}$; Prime funding cost $= {cb_val7:,.0f} \times 5.00\% = -\text{{USD }} {fin_cost7:,.0f}$. Net carry $= +\text{{USD }} {net_carry7:,.0f}$.",
        dist,
    )

    # Q3: Conditional Factor Regression during crisis month (Rm - Rf = -10%)
    alpha7, b_calm7, b_dum7, rm_ex7 = 0.0035, 0.15, 0.55, -0.10
    eff_beta7 = b_calm7 + b_dum7  # 0.70
    exp_ex7 = (alpha7 + eff_beta7 * rm_ex7) * 100  # 0.35% - 7.00% = -6.65%
    w1_v7q3 = (alpha7 + b_calm7 * rm_ex7) * 100  # ignores crisis dummy = -1.15%
    w2_v7q3 = (alpha7 + b_dum7 * rm_ex7) * 100  # forgets calm beta = -5.15%
    opts, ans, dist = opt_pack(
        rf"Crisis beta = {eff_beta7:.2f}; Expected monthly excess return = {exp_ex7:.2f}%",
        rf"Crisis beta = {b_calm7:.2f}; Expected monthly excess return = {w1_v7q3:.2f}%",
        r"Uses only the normal-regime beta of 0.15 and omits the +0.55 conditional crisis beta shift.",
        rf"Crisis beta = {b_dum7:.2f}; Expected monthly excess return = {w2_v7q3:.2f}%",
        r"Replaces the base beta (0.15) with the incremental dummy coefficient (0.55) instead of summing them.",
        pos_cycle(33),
    )
    calc_ids.add("L2-ALT-V07-Q3")
    add_l2(
        questions, "L2-ALT-V07-Q3", SUBJECT, mod_v7, "Conditional Risk", "Regime-Dependent Factor Beta",
        v7_id, v7_id, v7_title, v7_text,
        "Evaluate merger arbitrage, convertible arbitrage, and conditional factor exposures in hedge funds.",
        r"In Sleeve 3, during a stressed month where $(R_m - R_f) = -10.00\\%$, what are the fund's effective equity market beta and predicted monthly excess return (assuming $\\varepsilon = 0$)?",
        opts, ans,
        rf"Because $(R_m - R_f) = -10.0\% < -4.0\%$, $D_{{\text{{crisis}}}} = 1$, so effective crisis beta $= 0.15 + 0.55 = {eff_beta7:.2f}$. Expected excess return $= 0.35\% + 0.70(-10.00\%) = {exp_ex7:.2f}\%$.",
        dist,
    )

    # Q4: Volatility-targeted position sizing / leverage under stressed vol spike
    # Target annualized vol = 8.0%, normal vol = 10% -> gross lev = 0.8x; crisis vol jumps to 20% -> target lev = 0.4x (or with 120M capital)
    cap7, targ_vol7, norm_vol7, stress_vol7 = 150.0, 0.09, 0.12, 0.225
    not_norm7 = cap7 * (targ_vol7 / norm_vol7)  # 112.5M
    not_stress7 = cap7 * (targ_vol7 / stress_vol7)  # 60.0M
    cut7 = not_norm7 - not_stress7  # 52.5M
    w1_v7q4 = cap7 * (norm_vol7 / stress_vol7)  # ignores 9% vol target -> 80M (cut 70M)
    w2_v7q4 = not_norm7 * (norm_vol7 / stress_vol7)  # right! Wait: 112.5 * (12/22.5) = 60.0! Need distinct wrong calculation!
    w2_v7q4 = cap7 - not_stress7  # 90.0M cut instead of cut from initial notional
    opts, ans, dist = opt_pack(
        rf"Reduce gross notional from USD {not_norm7:.1f}M to USD {not_stress7:.1f}M (a USD {cut7:.1f}M cut)",
        rf"Reduce gross notional from USD {cap7:.1f}M to USD {cap7 * (norm_vol7 / stress_vol7):.1f}M (a USD {cap7 - cap7 * (norm_vol7 / stress_vol7):.1f}M cut)",
        r"Starts from 1.0x unadjusted capital instead of targeting 9.0% portfolio volatility in both regimes.",
        rf"Increase gross notional from USD {not_norm7:.1f}M to USD {cap7 * (stress_vol7 / targ_vol7):.1f}M",
        r"Inverts the volatility-targeting ratio, adding leverage rather than de-risking when volatility spikes.",
        pos_cycle(34),
    )
    calc_ids.add("L2-ALT-V07-Q4")
    add_l2(
        questions, "L2-ALT-V07-Q4", SUBJECT, mod_v7, "Hedge Fund Risk", "Volatility-Targeted Deleveraging",
        v7_id, v7_id, v7_title, v7_text,
        "Evaluate merger arbitrage, convertible arbitrage, and conditional factor exposures in hedge funds.",
        rf"Suppose Park enforces a strict 9.0% annualized volatility target on USD {cap7:.0f} million of risk capital in Sleeve 2. If strategy volatility doubles from 12.0% in calm markets to 22.5% during stress, how must gross notional exposure be adjusted?",
        opts, ans,
        rf"Calm notional $= {cap7:.0f} \times \frac{{9.0\%}}{{12.0\%}} = \text{{USD }} {not_norm7:.1f}\text{{M}}$. Stressed notional $= {cap7:.0f} \times \frac{{9.0\%}}{{22.5\%}} = \text{{USD }} {not_stress7:.1f}\text{{M}}$, requiring a USD {cut7:.1f}M reduction.",
        dist,
    )

    # Q5 (Concept): Why conditional beta spikes in merger/convertible arb vs CTA
    opts, ans, dist = opt_pack(
        r"Both merger arbitrage and convertible arbitrage carry latent equity and credit liquidity exposure that expands sharply during systemic stress as spreads widen and prime brokers tighten margin, unlike trend-following CTAs that often profit from sustained downward momentum.",
        r"Convertible arbitrage earns pure risk-free yield in crises because credit spreads automatically tighten to zero when equities crash.",
        r"Credit spreads widen in crises, causing convertible bond prices to drop faster than equity delta hedges recover unless credit/volatility hedges are held.",
        r"Merger arbitrage has zero correlation with equity markets during severe crashes because antitrust timelines ignore economic shocks.",
        r"Deal-break probability and financing withdrawal risk escalate during crashes, creating strong conditional downside equity beta.",
        pos_cycle(35),
    )
    add_l2(
        questions, "L2-ALT-V07-Q5", SUBJECT, mod_v7, "Hedge Fund Risk", "Tail Risk and Strategy Comovement",
        v7_id, v7_id, v7_title, v7_text,
        "Evaluate merger arbitrage, convertible arbitrage, and conditional factor exposures in hedge funds.",
        r"How should Park explain Sleeve 3's +0.55 conditional crisis beta shift to the investment committee?",
        opts, ans,
        r"Arbitrage strategies appear market-neutral in calm regimes ($\\beta = 0.15$), yet deal-break risk, credit-spread widening, and forced deleveraging drive crisis beta to $0.70$, underscoring why trend-following CTAs offer superior crash diversification.",
        dist,
    )

    # =========================================================================
    # V08: Commodity Futures Pricing (Convenience Yield & Storage) & Roll Yield
    # =========================================================================
    v8_id = "ALT-V08"
    v8_title = "Meridian Commodities Desk: Storage, Convenience Yield, and Roll Attribution"
    v8_text = (
        "Devon Patel, Commodities Strategist at Meridian Asset Management, analyzes Brent Crude Oil and Copper futures curves.\n\n"
        "Current Market Quotes (Continuous Compounding):\n"
        "- Continuously Compounded Risk-Free Rate ($r$): 4.50% per annum.\n"
        "- Brent Crude Spot Price ($S_0$): USD 82.00/bbl.\n"
        "- Brent Crude Annualized Storage Cost ($u$): 3.00%; Estimated Convenience Yield ($y$): 9.50%.\n"
        "- Copper Spot Price ($S_0$): USD 9,200/ton; Observed 6-Month ($T = 0.5$) Futures Price: USD 9,315/ton; Annualized Storage Cost ($u$): 2.50%.\n\n"
        "1-Year Commodity Roll & Portfolio Attribution Case:\n"
        "- An active energy futures index rolls quarterly across backwardated Brent contracts where the expiring front-quarter contract averages USD 80.00/bbl and the next-quarter contract averages USD 77.60/bbl (4 equal quarterly rolls).\n"
        "- Over the full year, the spot price rises +5.00% and the portfolio's T-bill collateral earns +4.60%."
    )
    mod_v8 = "Commodity Futures & Term Structure"

    # Q1: Theoretical 6-month Brent futures price
    s_brent, r8, u_brent, y_brent, t8 = 82.00, 0.045, 0.030, 0.095, 0.5
    f_brent6m = s_brent * math.exp((r8 + u_brent - y_brent) * t8)
    w1_v8q1 = s_brent * math.exp((r8 + u_brent + y_brent) * t8)  # adds convenience yield
    w2_v8q1 = s_brent * math.exp((r8 - u_brent - y_brent) * t8)  # subtracts storage cost
    opts, ans, dist = opt_pack(
        rf"USD {f_brent6m:.2f}/bbl (Backwardation)",
        rf"USD {w1_v8q1:.2f}/bbl (Contango)",
        r"Adds convenience yield instead of subtracting it in the cost-of-carry exponent.",
        rf"USD {w2_v8q1:.2f}/bbl (Backwardation)",
        r"Subtracts storage cost instead of adding it to the cost of carry.",
        pos_cycle(36),
    )
    calc_ids.add("L2-ALT-V08-Q1")
    add_l2(
        questions, "L2-ALT-V08-Q1", SUBJECT, mod_v8, "Commodity Pricing", "Brent Futures Cost-of-Carry Price",
        v8_id, v8_id, v8_title, v8_text,
        "Determine commodity futures prices, implied convenience yields, roll yields, and total portfolio returns.",
        r"What is the theoretical 6-month ($T = 0.5$) no-arbitrage futures price for Brent Crude, and what curve shape does it imply?",
        opts, ans,
        rf"$F_0 = S_0 e^{{(r + u - y)T}} = 82.00 \times e^{{(0.045 + 0.030 - 0.095) \times 0.5}} = 82.00 \times e^{{-0.010}} = \text{{USD }} {f_brent6m:.2f}$/bbl. Because $F_0 < S_0$ (as $y > r + u$), the curve is in backwardation.",
        dist,
    )

    # Q2: Implied convenience yield for Copper
    s_cu, f_cu, u_cu = 9200.0, 9315.0, 0.025
    y_cu = (r8 + u_cu - math.log(f_cu / s_cu) / t8) * 100
    w1_v8q2 = (r8 + u_cu + math.log(f_cu / s_cu) / t8) * 100
    w2_v8q2 = (r8 - u_cu - math.log(f_cu / s_cu) / t8) * 100
    opts, ans, dist = opt_pack(
        rf"{y_cu:.2f}%",
        rf"{w1_v8q2:.2f}%",
        r"Adds the futures log-basis $\ln(F/S)/T$ instead of subtracting it from total carry costs.",
        rf"{w2_v8q2:.2f}%",
        r"Subtracts storage cost instead of adding it to the risk-free rate.",
        pos_cycle(37),
    )
    calc_ids.add("L2-ALT-V08-Q2")
    add_l2(
        questions, "L2-ALT-V08-Q2", SUBJECT, mod_v8, "Commodity Pricing", "Copper Implied Convenience Yield",
        v8_id, v8_id, v8_title, v8_text,
        "Determine commodity futures prices, implied convenience yields, roll yields, and total portfolio returns.",
        r"Based on the observed 6-month Copper futures price of USD 9,315/ton, what is Copper's implied annualized convenience yield?",
        opts, ans,
        rf"$y = r + u - \frac{{\ln(F_0/S_0)}}{{T}} = 0.045 + 0.025 - \frac{{\ln(9,315/9,200)}}{{0.5}} = 0.070 - {math.log(f_cu / s_cu) / t8:.4f} = {y_cu:.2f}\%$.",
        dist,
    )

    # Q3: Quarterly and Annualized Roll Yield on Brent index
    f_near8, f_far8 = 80.00, 77.60
    q_roll8 = (f_near8 - f_far8) / f_near8  # 0.030 = +3.00% per quarter
    ann_roll_comp = ((1 + q_roll8) ** 4 - 1) * 100  # 12.55% compounded, vs 12.00% simple!
    # Let's specify "compounded across the 4 quarterly rolls" explicitly!
    w1_v8q3 = (-q_roll8) * 4 * 100  # negative sign
    w2_v8q3 = q_roll8 * 100  # unannualized single-roll return
    opts, ans, dist = opt_pack(
        rf"+{ann_roll_comp:.2f}% (+{q_roll8 * 100:.2f}% per quarterly roll)",
        rf"{w1_v8q3:.2f}% (-{q_roll8 * 100:.2f}% per quarterly roll)",
        r"Reverses the backwardation roll sign by assuming rolling into cheaper contracts creates a loss.",
        rf"+{w2_v8q3:.2f}% (single-quarter roll yield unannualized)",
        r"Reports only a single quarterly roll return rather than compounding across all 4 annual rolls.",
        pos_cycle(38),
    )
    calc_ids.add("L2-ALT-V08-Q3")
    add_l2(
        questions, "L2-ALT-V08-Q3", SUBJECT, mod_v8, "Commodity Returns", "Compounded Roll Yield",
        v8_id, v8_id, v8_title, v8_text,
        "Determine commodity futures prices, implied convenience yields, roll yields, and total portfolio returns.",
        r"For the active energy futures index rolling 4 times per year (expiring USD 80.00/bbl into next-quarter USD 77.60/bbl), what is the annualized compounded roll yield?",
        opts, ans,
        rf"Each quarterly roll yields $\frac{{80.00 - 77.60}}{{80.00}} = +{q_roll8 * 100:.2f}\%$. Compounding across 4 quarterly rolls gives $(1 + {q_roll8:.4f})^4 - 1 = +{ann_roll_comp:.2f}\%$.",
        dist,
    )

    # Q4: Total fully collateralized portfolio return (multiplicative)
    spot8, coll8 = 0.05, 0.046
    roll8_dec = (1 + q_roll8) ** 4 - 1
    tot8_mult = ((1 + spot8) * (1 + roll8_dec) * (1 + coll8) - 1) * 100
    tot8_add = (spot8 + roll8_dec + coll8) * 100  # additive
    w1_v8q4 = ((1 + spot8) * (1 + roll8_dec) - 1) * 100  # omits collateral
    w2_v8q4 = ((1 + spot8) * (1 - roll8_dec) * (1 + coll8) - 1) * 100  # negates roll
    opts, ans, dist = opt_pack(
        rf"+{tot8_mult:.2f}%",
        rf"+{w1_v8q4:.2f}%",
        r"Reports only the excess futures return (spot plus roll) and omits the +4.60% T-bill collateral yield.",
        rf"{w2_v8q4:.2f}%",
        r"Subtracts the roll return instead of compounding positive backwardation roll gains.",
        pos_cycle(39),
    )
    calc_ids.add("L2-ALT-V08-Q4")
    add_l2(
        questions, "L2-ALT-V08-Q4", SUBJECT, mod_v8, "Commodity Returns", "Multiplicative Total Return",
        v8_id, v8_id, v8_title, v8_text,
        "Determine commodity futures prices, implied convenience yields, roll yields, and total portfolio returns.",
        r"Using exact geometric multiplicative compounding across spot return (+5.00%), annualized compounded roll return, and collateral yield (+4.60%), what is the total annual return on the fully collateralized energy futures portfolio?",
        opts, ans,
        rf"Multiplicative total return $= (1 + 0.0500)(1 + {roll8_dec:.6f})(1 + 0.0460) - 1 = +{tot8_mult:.2f}\%$.",
        dist,
    )

    # Q5 (Concept): Theory of storage & convenience yield drivers
    opts, ans, dist = opt_pack(
        r"When physical inventories fall critically low, the non-monetary benefit of holding spot supply (convenience yield) spikes above storage plus interest costs, flipping the curve into backwardation.",
        r"Higher physical warehouse storage costs always push commodity futures curves into steeper backwardation.",
        r"Higher storage costs increase $r + u$, pushing futures prices higher above spot (contango), not backwardation.",
        r"If consumers hold excess surplus inventory, convenience yield surges toward infinity.",
        r"Abundant inventory depresses convenience yield toward zero because supply shortages are unlikely.",
        pos_cycle(40),
    )
    add_l2(
        questions, "L2-ALT-V08-Q5", SUBJECT, mod_v8, "Commodity Theory", "Theory of Storage",
        v8_id, v8_id, v8_title, v8_text,
        "Determine commodity futures prices, implied convenience yields, roll yields, and total portfolio returns.",
        r"According to the theory of storage, why does Brent Crude trade in backwardation while Copper trades in contango in Patel's data?",
        opts, ans,
        r"Scarce Brent inventories generate a 9.50% convenience yield exceeding $r + u = 7.50\%$, pulling futures below spot (backwardation), whereas Copper's ample supply keeps convenience yield below carrying costs (contango).",
        dist,
    )

    # =========================================================================
    # V09: Infrastructure Concession & Natural Resources (Timberland) Valuation
    # =========================================================================
    v9_id = "ALT-V09"
    v9_title = "Meridien Real Assets: Toll Bridge Concession and Timberland Valuation"
    v9_text = (
        "Clara Lindholm, Senior Real Assets Analyst at Meridien Infrastructure Partners, evaluates two acquisitions:\n\n"
        "Asset A — Harbor Crossing Brownfield Toll Bridge Concession:\n"
        "- Remaining Concession Term: 5 years (Years 1-5), after which ownership reverts to the state at zero terminal value.\n"
        "- Year 1 Projected Toll Revenue: USD 40.00M; Expected Annual Revenue Growth (traffic + CPI toll escalation): 4.00%/yr.\n"
        "- Annual Routine O&M Expense: USD 12.00M in Year 1, growing 3.00%/yr.\n"
        "- Major Mid-Life Structural Deck Overhaul (CapEx): USD 15.00M outflow occurring at Year 3.\n"
        "- Unlevered Asset Discount Rate: 8.00% (ignore corporate taxes for this asset-level cash flow valuation).\n\n"
        "Asset B — Southern Pine Timberland Estate (10,000 Hectares, USD 50.00M Entry Valuation):\n"
        "- Asset Value Composition: 80% Standing Timber, 20% Underlying Land.\n"
        "- Expected Annual Drivers: Biological timber volume growth +5.50%; Stumpage timber price growth +2.00%; Bare land appreciation +2.50%; Verified net carbon-credit cash yield +0.80% of total beginning asset value; Management & silviculture expenses -1.10% of total beginning asset value."
    )
    mod_v9 = "Infrastructure & Natural Resources"

    # Compute exact 5-year concession free cash flows
    cfs_bridge = []
    for t in range(1, 6):
        rev_t = 40.0 * (1.04 ** (t - 1))
        om_t = 12.0 * (1.03 ** (t - 1))
        cap_t = 15.0 if t == 3 else 0.0
        cfs_bridge.append(rev_t - om_t - cap_t)
    pv_bridge = sum(cfs_bridge[t - 1] / (1.08 ** t) for t in range(1, 6))

    # Q1: Year 1 and Year 3 Net Free Cash Flow of Toll Bridge
    cf_y1_b, cf_y3_b = cfs_bridge[0], cfs_bridge[2]
    w1_v9q1 = cf_y3_b + 15.0  # forgets Year 3 overhaul CapEx
    w2_v9q1 = (40.0 * (1.04 ** 3) - 12.0 * (1.03 ** 3) - 15.0)  # grows from Y1 by 3 yrs instead of 2 yrs
    opts, ans, dist = opt_pack(
        rf"Year 1 FCF = USD {cf_y1_b:.2f}M; Year 3 FCF = USD {cf_y3_b:.2f}M",
        rf"Year 1 FCF = USD {cf_y1_b:.2f}M; Year 3 FCF = USD {w1_v9q1:.2f}M",
        r"Omits the scheduled USD 15.00M mid-life structural overhaul CapEx in Year 3.",
        rf"Year 1 FCF = USD {cf_y1_b:.2f}M; Year 3 FCF = USD {w2_v9q1:.2f}M",
        r"Compounds Year 1 revenue and O&M over 3 periods instead of 2 periods to reach Year 3.",
        pos_cycle(41),
    )
    calc_ids.add("L2-ALT-V09-Q1")
    add_l2(
        questions, "L2-ALT-V09-Q1", SUBJECT, mod_v9, "Infrastructure Cash Flows", "Concession FCF Schedule",
        v9_id, v9_id, v9_title, v9_text,
        "Value finite-life infrastructure concessions and attribute timberland returns.",
        r"What are the Harbor Crossing Toll Bridge's net unlevered free cash flows in Year 1 and Year 3?",
        opts, ans,
        rf"Year 1 FCF $= 40.00 - 12.00 = \text{{USD }} {cf_y1_b:.2f}\text{{M}}$. Year 3 revenue $= 40.00 \times 1.04^2 = 43.26\text{{M}}$; Year 3 O&M $= 12.00 \times 1.03^2 = 12.73\text{{M}}$; less USD 15.00M overhaul CapEx gives Year 3 FCF $= 43.26 - 12.73 - 15.00 = \text{{USD }} {cf_y3_b:.2f}\text{{M}}$.",
        dist,
    )

    # Q2: Total EV (NPV of 5-year concession)
    pv_no_cap = sum((40.0 * (1.04 ** (t - 1)) - 12.0 * (1.03 ** (t - 1))) / (1.08 ** t) for t in range(1, 6))
    term_mistake = (cfs_bridge[4] / (0.08 - 0.04)) / (1.08 ** 5)
    opts, ans, dist = opt_pack(
        rf"USD {pv_bridge:.2f} million",
        rf"USD {pv_no_cap:.2f} million",
        r"Omits the present value of the USD 15.00M Year 3 overhaul CapEx.",
        rf"USD {pv_bridge + term_mistake:.2f} million",
        r"Incorrectly adds a perpetual growing terminal value after Year 5 when the concession reverts for zero value.",
        pos_cycle(42),
    )
    calc_ids.add("L2-ALT-V09-Q2")
    add_l2(
        questions, "L2-ALT-V09-Q2", SUBJECT, mod_v9, "Infrastructure Valuation", "Finite-Horizon Concession DCF",
        v9_id, v9_id, v9_title, v9_text,
        "Value finite-life infrastructure concessions and attribute timberland returns.",
        r"Discounting all 5 years of unlevered free cash flows at 8.00% with zero handback terminal value, what is the maximum enterprise value Meridien should pay for Asset A?",
        opts, ans,
        rf"Annual FCFs (Years 1-5) are ${cfs_bridge[0]:.2f}, {cfs_bridge[1]:.2f}, {cfs_bridge[2]:.2f}, {cfs_bridge[3]:.2f}, {cfs_bridge[4]:.2f}\text{{M}}$. Discounting at 8.00% yields $\text{{PV}} = \sum_{{t=1}}^5 \frac{{\text{{FCF}}_t}}{{1.08^t}} = \text{{USD }} {pv_bridge:.2f}\text{{M}}$.",
        dist,
    )

    # Q3: Timberland expected annual total net return
    timb_app9 = (1.055 * 1.020) - 1  # 7.61%
    tot_ret9 = (0.80 * timb_app9 + 0.20 * 0.025 + 0.008 - 0.011) * 100
    w1_v9q3 = (timb_app9 + 0.025 + 0.008 - 0.011) * 100  # ignores 80/20 weights
    w2_v9q3 = (0.80 * timb_app9 + 0.20 * 0.025 - 0.011) * 100  # omits carbon yield
    opts, ans, dist = opt_pack(
        rf"{tot_ret9:.2f}%",
        rf"{w1_v9q3:.2f}%",
        r"Adds standing timber and land appreciation directly without weighting by their 80%/20% value shares.",
        rf"{w2_v9q3:.2f}%",
        r"Excludes the +0.80% net carbon-credit cash yield from total timberland return.",
        pos_cycle(43),
    )
    calc_ids.add("L2-ALT-V09-Q3")
    add_l2(
        questions, "L2-ALT-V09-Q3", SUBJECT, mod_v9, "Natural Resources", "Timberland Total Return",
        v9_id, v9_id, v9_title, v9_text,
        "Value finite-life infrastructure concessions and attribute timberland returns.",
        r"For Asset B (Southern Pine Timberland), what is the expected net annual total return?",
        opts, ans,
        rf"Standing timber appreciates by $(1.055 \times 1.020) - 1 = {timb_app9 * 100:.2f}\%$. Weighted asset appreciation $= 0.80({timb_app9 * 100:.2f}\%) + 0.20(2.50\%) = {(0.80 * timb_app9 + 0.20 * 0.025) * 100:.2f}\%$. Adding +0.80% carbon yield and deducting -1.10% expenses yields ${tot_ret9:.2f}\%$.",
        dist,
    )

    # Q4: Bridge Year 1 DSCR sensitivity under 15% traffic drop (with fixed debt service of 18.0M)
    # Base Y1 CFADS = 28.0M -> if toll revenue falls 15% (40 -> 34), O&M stays 12 -> stressed CFADS = 22.0M; with debt service 18.0M -> DSCR falls from 1.56x to 1.22x!
    ds9 = 18.0
    dscr_base9 = cf_y1_b / ds9  # 28/18 = 1.56x
    rev_stress9 = 40.0 * 0.85  # 34.0
    cf_stress9 = rev_stress9 - 12.0  # 22.0
    dscr_stress9 = cf_stress9 / ds9  # 1.22x
    w1_v9q4 = (cf_y1_b * 0.85) / ds9  # scales CFADS by 0.85 instead of revenue
    w2_v9q4 = rev_stress9 / ds9  # ignores O&M in stressed DSCR
    opts, ans, dist = opt_pack(
        rf"DSCR drops from {dscr_base9:.2f}x to {dscr_stress9:.2f}x",
        rf"DSCR drops from {dscr_base9:.2f}x to {w1_v9q4:.2f}x",
        r"Applies the 15% drop directly to net CFADS rather than reducing revenue while keeping fixed O&M at USD 12.00M.",
        rf"DSCR drops from {dscr_base9:.2f}x to {w2_v9q4:.2f}x",
        r"Computes stressed DSCR using gross toll revenue without subtracting USD 12.00M O&M expense.",
        pos_cycle(44),
    )
    calc_ids.add("L2-ALT-V09-Q4")
    add_l2(
        questions, "L2-ALT-V09-Q4", SUBJECT, mod_v9, "Infrastructure Risk", "Patronage Traffic Shock and DSCR",
        v9_id, v9_id, v9_title, v9_text,
        "Value finite-life infrastructure concessions and attribute timberland returns.",
        rf"If Asset A carries USD {ds9:.1f}M in annual senior debt service in Year 1 and an unexpected 15.0% traffic decline cuts Year 1 toll revenue while O&M expenses remain fixed at USD 12.00M, how does Year 1 DSCR change?",
        opts, ans,
        rf"Base Year 1 $\text{{DSCR}} = \frac{{28.00}}{{18.00}} = {dscr_base9:.2f}\text{{x}}$. With 15% lower revenue ($40 \times 0.85 = \text{{USD }} 34.00\text{{M}}$) and fixed USD 12.00M O&M, stressed $\text{{CFADS}} = 34.00 - 12.00 = \text{{USD }} {cf_stress9:.2f}\text{{M}}$, reducing DSCR to $\frac{{{cf_stress9:.2f}}}{{{ds9:.1f}}} = {dscr_stress9:.2f}\text{{x}}$.",
        dist,
    )

    # Q5 (Concept): Finite concession vs perpetual timberland optionality
    opts, ans, dist = opt_pack(
        r"Toll-road concessions are wasting finite-term assets requiring capital recovery within the concession horizon, whereas perpetual timberland creates real harvest-timing optionality through continuous biological growth.",
        r"Concession agreements allow private operators to defer toll-road handback indefinitely whenever traffic underperforms.",
        r"Concession expiration dates are strictly contractual; traffic shortfalls do not automatically confer perpetual ownership.",
        r"Timberland returns are derived solely from annual contractual availability payments issued by municipal authorities.",
        r"Timberland relies on market stumpage prices, biological growth, and land appreciation rather than government availability payments.",
        pos_cycle(45),
    )
    add_l2(
        questions, "L2-ALT-V09-Q5", SUBJECT, mod_v9, "Real Assets Comparison", "Concession Decay vs. Biological Growth",
        v9_id, v9_id, v9_title, v9_text,
        "Value finite-life infrastructure concessions and attribute timberland returns.",
        r"What fundamental valuation and risk distinction must Lindholm highlight when comparing Asset A and Asset B?",
        opts, ans,
        r"Finite concessions depreciate to zero value upon handback—making cash-flow recovery and mid-life CapEx timing critical—whereas perpetual timberland provides inflation hedging and harvest deferral flexibility while trees compound biologically.",
        dist,
    )

    # =========================================================================
    # V10: Digital Assets & Tokenization Valuation + Portfolio Allocation
    # =========================================================================
    v10_id = "ALT-V10"
    v10_title = "Digital Capital Partners: Tokenomics, RWA Tokenization, and Allocation"
    v10_text = (
        "Kenji Takahashi, Head of Digital Assets Research at Digital Capital Partners, evaluates three institutional initiatives:\n\n"
        "Initiative 1 — NovaChain Layer-1 PoS Protocol Valuation:\n"
        "- Circulating Supply: 100.00 million NOVA tokens; Fully Diluted Supply (FDV base): 150.00 million NOVA tokens (remaining 50.00M vest over 3 years).\n"
        "- Current Market Price: USD 12.00 per NOVA.\n"
        "- Staking Mechanics: Nominal staking APR = 9.00%; Gross annual token supply inflation = 6.50%.\n"
        "- Protocol Cash Flow Proxy (Fee Burn): Protocol generates USD 48.00M in Year 1 transaction fees burned (permanently removed from supply, accruing to token holders), projected to grow at 12.00% annually in perpetuity, discounted at an 18.00% crypto cost of equity.\n\n"
        "Initiative 2 — Tokenized U.S. Treasury / Private Credit RWA Vault:\n"
        "- Gross Underlying Asset Yield: 6.40% per annum on USD 80.00M AUM.\n"
        "- Legacy Securitized Structure Costs: 85 bps admin/custody/settlement drag.\n"
        "- On-Chain Tokenized Structure Costs: 25 bps smart-contract protocol fee + 15 bps regulated custodian & Chainlink-style oracle fee.\n\n"
        "Initiative 3 — Institutional Portfolio Allocation (Core 60/40 vs. 96% Core / 4% Digital Asset Sleeve):\n"
        "- Existing 60/40 Core Portfolio: Expected Return = 7.50%; Volatility = 10.00%; Risk-Free Rate = 3.50%.\n"
        "- Digital Asset Sleeve: Expected Return = 18.00%; Volatility = 60.00%; Correlation with Core 60/40 = +0.20."
    )
    mod_v10 = "Digital Assets & Tokenization"

    # Q1: Net Real Staking Yield & Circulating vs FDV Market Cap
    nom_s10, inf_s10 = 0.09, 0.065
    real_s10 = ((1 + nom_s10) / (1 + inf_s10) - 1) * 100  # 2.35%
    circ_mc = 100.0 * 12.0  # 1,200M
    fdv_mc = 150.0 * 12.0  # 1,800M
    w1_v10q1 = (nom_s10 + inf_s10) * 100
    w2_v10q1 = nom_s10 * 100
    opts, ans, dist = opt_pack(
        rf"Real staking yield = {real_s10:.2f}%; Circulating Market Cap = USD {circ_mc:,.0f}M; FDV = USD {fdv_mc:,.0f}M",
        rf"Real staking yield = {w1_v10q1:.2f}%; Circulating Market Cap = USD {circ_mc:,.0f}M; FDV = USD {fdv_mc:,.0f}M",
        r"Adds supply inflation to nominal APR instead of adjusting downward for token dilution.",
        rf"Real staking yield = {w2_v10q1:.2f}%; Circulating Market Cap = USD {fdv_mc:,.0f}M; FDV = USD {circ_mc:,.0f}M",
        r"Reports unadjusted nominal APR as real yield and reverses circulating market cap and fully diluted valuation.",
        pos_cycle(46),
    )
    calc_ids.add("L2-ALT-V10-Q1")
    add_l2(
        questions, "L2-ALT-V10-Q1", SUBJECT, mod_v10, "Tokenomics", "Real Staking Yield and FDV",
        v10_id, v10_id, v10_title, v10_text,
        "Value digital asset protocols, tokenized real-world assets, and digital asset portfolio allocations.",
        r"For Initiative 1 (NovaChain), what are the exact dilution-adjusted real staking yield, circulating market capitalization, and fully diluted valuation (FDV)?",
        opts, ans,
        rf"Exact real staking yield $= \frac{{1 + 0.090}}{{1 + 0.065}} - 1 = {real_s10:.2f}\%$. Circulating market cap $= 100\text{{M}} \times 12 = \text{{USD }} {circ_mc:,.0f}\text{{M}}$; FDV $= 150\text{{M}} \times 12 = \text{{USD }} {fdv_mc:,.0f}\text{{M}}$.",
        dist,
    )

    # Q2: NovaChain DCF fundamental value vs current FDV
    fee10, g10, ke10 = 48.0, 0.12, 0.18
    fund_ev10 = fee10 / (ke10 - g10)  # 48 / 0.06 = 800M
    prem_to_circ = (circ_mc - fund_ev10) / fund_ev10 * 100  # 50% overvalued vs circulating
    prem_to_fdv = (fdv_mc - fund_ev10) / fund_ev10 * 100  # 125% overvalued vs FDV -> Wait: ask price per FDV token!
    fair_p_fdv = fund_ev10 / 150.0  # USD 5.33
    fair_p_circ = fund_ev10 / 100.0  # USD 8.00
    w1_v10q2 = fee10 / ke10  # ignores perpetual growth = 266.67M -> 1.78/token
    w2_v10q2 = (fee10 * (1 + g10) / (ke10 - g10))  # applies extra (1+g) to Year 1 fee = 896M
    opts, ans, dist = opt_pack(
        rf"Fundamental Network Value = USD {fund_ev10:.0f}M (USD {fair_p_fdv:.2f} per fully diluted token)",
        rf"Fundamental Network Value = USD {w1_v10q2:.2f}M (USD {w1_v10q2 / 150.0:.2f} per fully diluted token)",
        r"Treats Year 1 burned fees as a zero-growth perpetuity instead of incorporating 12.00% perpetual growth.",
        rf"Fundamental Network Value = USD {w2_v10q2:.0f}M (USD {w2_v10q2 / 150.0:.2f} per fully diluted token)",
        r"Multiplies forward Year 1 fee cash flow by (1 + 12.00%), double-counting Year 1 growth.",
        pos_cycle(47),
    )
    calc_ids.add("L2-ALT-V10-Q2")
    add_l2(
        questions, "L2-ALT-V10-Q2", SUBJECT, mod_v10, "Protocol Valuation", "Fee-Burn Gordon Growth Valuation",
        v10_id, v10_id, v10_title, v10_text,
        "Value digital asset protocols, tokenized real-world assets, and digital asset portfolio allocations.",
        r"Treating Year 1 burned transaction fees (USD 48.00M) as an equity-like cash flow growing at 12.00% annually in perpetuity, what are NovaChain's fundamental network valuation and implied fair value per fully diluted token?",
        opts, ans,
        rf"Using the constant-growth model on Year 1 cash flow: $V_0 = \frac{{48.00}}{{0.18 - 0.12}} = \text{{USD }} {fund_ev10:.0f}\text{{M}}$. Dividing by 150.00 million fully diluted tokens gives $\frac{{{fund_ev10:.0f}}}{{150}} = \text{{USD }} {fair_p_fdv:.2f}$/token.",
        dist,
    )

    # Q3: Tokenized RWA net yield & bps cost savings vs legacy structure
    gross_rwa, leg_cost, tok_cost, aum_rwa = 0.064, 0.0085, 0.0040, 80.0
    net_tok_y = (gross_rwa - tok_cost) * 100  # 6.00%
    bps_saved = (leg_cost - tok_cost) * 10000  # 45 bps
    usd_saved = aum_rwa * (leg_cost - tok_cost) * 1000  # 360k
    w1_v10q3 = (gross_rwa - 0.0025) * 100  # omits 15bps oracle/custody
    w2_v10q3 = (gross_rwa - leg_cost) * 100
    opts, ans, dist = opt_pack(
        rf"Net tokenized yield = {net_tok_y:.2f}%; Annual fee savings = {bps_saved:.0f} bps (USD {usd_saved:,.0f}k)",
        rf"Net tokenized yield = {w1_v10q3:.2f}%; Annual fee savings = {(leg_cost - 0.0025) * 10000:.0f} bps (USD {aum_rwa * (leg_cost - 0.0025) * 1000:,.0f}k)",
        r"Omits the 15 bps regulated custodian and oracle fee when computing net tokenized costs.",
        rf"Net tokenized yield = {w2_v10q3:.2f}%; Annual fee savings = 0 bps (USD 0k)",
        r"Reports the legacy securitized net yield rather than the on-chain tokenized structure.",
        pos_cycle(48),
    )
    calc_ids.add("L2-ALT-V10-Q3")
    add_l2(
        questions, "L2-ALT-V10-Q3", SUBJECT, mod_v10, "RWA Tokenization", "Tokenized Yield and Cost Efficiency",
        v10_id, v10_id, v10_title, v10_text,
        "Value digital asset protocols, tokenized real-world assets, and digital asset portfolio allocations.",
        r"In Initiative 2, what are the RWA vault's net investor yield and annual cost savings relative to the legacy securitized structure?",
        opts, ans,
        rf"Total tokenized cost $= 25 + 15 = 40\text{{ bps}} = 0.40\%$, yielding $6.40\% - 0.40\% = {net_tok_y:.2f}\%$ net. Compared with 85 bps legacy expenses, tokenization saves $85 - 40 = {bps_saved:.0f}\text{{ bps}}$, or $\text{{USD }} 80\text{{M}} \times 0.45\% = \text{{USD }} {usd_saved:,.0f}\text{{ thousand}}$ annually.",
        dist,
    )

    # Q4: Portfolio Allocation Sharpe Ratio impact (96% Core / 4% Crypto)
    wc10, wd10, erc10, erd10, rf10, sc10, sd10, rho10 = 0.96, 0.04, 0.075, 0.18, 0.035, 0.10, 0.60, 0.20
    er_mix10 = wc10 * erc10 + wd10 * erd10  # 7.20 + 0.72 = 7.92%
    var_mix10 = (wc10 * sc10) ** 2 + (wd10 * sd10) ** 2 + 2 * wc10 * wd10 * sc10 * sd10 * rho10
    sig_mix10 = math.sqrt(var_mix10)
    sr_core10 = (erc10 - rf10) / sc10  # 0.400
    sr_mix10 = (er_mix10 - rf10) / sig_mix10
    w1_v10q4_sig = wc10 * sc10 + wd10 * sd10  # 12.00% linear vol
    w1_v10q4_sr = (er_mix10 - rf10) / w1_v10q4_sig
    w2_v10q4_var = (wc10 * sc10) ** 2 + (wd10 * sd10) ** 2  # assumes rho = 0
    w2_v10q4_sig = math.sqrt(w2_v10q4_var)
    w2_v10q4_sr = (er_mix10 - rf10) / w2_v10q4_sig
    opts, ans, dist = opt_pack(
        rf"E[R] = {er_mix10 * 100:.2f}%; Volatility = {sig_mix10 * 100:.2f}%; Sharpe rises from {sr_core10:.3f} to {sr_mix10:.3f}",
        rf"E[R] = {er_mix10 * 100:.2f}%; Volatility = {w1_v10q4_sig * 100:.2f}%; Sharpe falls from {sr_core10:.3f} to {w1_v10q4_sr:.3f}",
        r"Computes weighted-average portfolio volatility assuming +1.00 correlation instead of +0.20.",
        rf"E[R] = {er_mix10 * 100:.2f}%; Volatility = {w2_v10q4_sig * 100:.2f}%; Sharpe rises from {sr_core10:.3f} to {w2_v10q4_sr:.3f}",
        r"Omits the covariance term ($2 w_1 w_2 \sigma_1 \sigma_2 \rho$) by assuming zero correlation.",
        pos_cycle(49),
    )
    calc_ids.add("L2-ALT-V10-Q4")
    add_l2(
        questions, "L2-ALT-V10-Q4", SUBJECT, mod_v10, "Portfolio Allocation", "Digital Asset Mean-Variance Impact",
        v10_id, v10_id, v10_title, v10_text,
        "Value digital asset protocols, tokenized real-world assets, and digital asset portfolio allocations.",
        r"Under Initiative 3, how do portfolio expected return, annualized volatility, and Sharpe ratio change when moving from 100% Core 60/40 to a 96% Core / 4% Digital Asset allocation?",
        opts, ans,
        rf"Expected return $= 0.96(7.50\%) + 0.04(18.00\%) = {er_mix10 * 100:.2f}\%$. Variance $= (0.96 \times 0.10)^2 + (0.04 \times 0.60)^2 + 2(0.96)(0.04)(0.10)(0.60)(0.20) = {var_mix10:.6f} \implies \sigma_p = {sig_mix10 * 100:.2f}\%$. Sharpe ratio improves from $\frac{{7.50 - 3.50}}{{10.00}} = {sr_core10:.3f}$ to $\frac{{{er_mix10 * 100:.2f} - 3.50}}{{{sig_mix10 * 100:.2f}}} = {sr_mix10:.3f}$.",
        dist,
    )

    # Q5 (Concept): Institutional risks in token valuation & RWA tokenization
    opts, ans, dist = opt_pack(
        r"Large unvested token unlock schedules create persistent FDV supply overhang against circulating valuation, while RWA tokenization still faces oracle dependency, smart-contract bugs, and off-chain legal enforceability risk.",
        r"Tokenizing illiquid private credit loans eliminates underlying borrower credit default risk via blockchain immutability.",
        r"On-chain tokenization alters ledger settlement mechanics but does not alter underlying borrower solvency or collateral recovery risk.",
        r"High positive return skewness in cryptocurrency portfolios guarantees that mean-variance Sharpe ratios overstate true tail risk.",
        r"Crypto assets exhibit extreme fat tails and deep multi-year drawdowns (e.g., 70%-80%) that standard variance understates.",
        pos_cycle(50),
    )
    add_l2(
        questions, "L2-ALT-V10-Q5", SUBJECT, mod_v10, "Digital Asset Governance", "Unlock Overhang and Legal Finality",
        v10_id, v10_id, v10_title, v10_text,
        "Value digital asset protocols, tokenized real-world assets, and digital asset portfolio allocations.",
        r"Which key risk assessment should Takahashi emphasize in his institutional investment committee brief across Initiatives 1-3?",
        opts, ans,
        r"Ignoring the 50M locked NovaChain tokens understates future dilution pressure (FDV overhang), while tokenized RWAs require legal parity between on-chain tokens and off-chain bankruptcy-remote SPV ownership alongside audited smart contracts and redundant price oracles.",
        dist,
    )


def main():
    questions: list[dict] = []
    calc_ids: set[str] = set()

    build_l1_part1(questions, calc_ids)
    build_l1_part2(questions, calc_ids)
    build_l2_v01_v05(questions, calc_ids)
    build_l2_v06_v10(questions, calc_ids)

    # Strict QA integrity checks
    total = len(questions)
    l1 = [q for q in questions if q["level"] == 1]
    l2 = [q for q in questions if q["level"] == 2]
    assert total == 125, f"Expected 125 questions, got {total}"
    assert len(l1) == 75, f"Expected 75 L1 questions, got {len(l1)}"
    assert len(l2) == 50, f"Expected 50 L2 questions, got {len(l2)}"

    # Verify exact IDs
    expected_l1 = [f"L1-ALT-{i:03d}" for i in range(1, 76)]
    assert [q["id"] for q in l1] == expected_l1, "L1 ID sequence mismatch"
    expected_l2 = [f"L2-ALT-V{v:02d}-Q{k}" for v in range(1, 11) for k in range(1, 6)]
    assert [q["id"] for q in l2] == expected_l2, "L2 ID sequence mismatch"

    # Verify >=65% numerical calculation ratio
    calc_ratio = len(calc_ids) / total
    assert calc_ratio >= 0.65, f"Numerical ratio {calc_ratio:.1%} below 65%"

    # Verify zero stray ASCII control characters from unescaped backslashes
    ctrl_re = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f]")
    for q in questions:
        for k, v in q.items():
            if isinstance(v, str) and ctrl_re.search(v):
                raise ValueError(f"{q['id']}.{k} contains control character: {repr(v)}")
            if isinstance(v, dict):
                for sk, sv in v.items():
                    if isinstance(sv, str) and ctrl_re.search(sv):
                        raise ValueError(f"{q['id']}.{k}.{sk} contains control character: {repr(sv)}")

    save_validated_json(questions, OUT_PATH)

    ans_counts = {k: sum(1 for q in questions if q["answer"] == k) for k in ("A", "B", "C")}
    print(
        f"Audit passed: total={total} (L1={len(l1)}, L2={len(l2)}), "
        f"numerical={len(calc_ids)}/{total} ({calc_ratio:.1%}), answers={ans_counts}"
    )


if __name__ == "__main__":
    main()
