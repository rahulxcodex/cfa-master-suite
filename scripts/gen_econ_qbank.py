"""
Generator for CFA Economics Question Bank (Level 1: 80 MCQs, Level 2: 50 Vignette MCQs).
All numerical calculations are executed directly in Python with strict KaTeX and schema validation.
"""
import math
import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(SCRIPT_DIR)
if SCRIPT_DIR not in sys.path:
    sys.path.insert(0, SCRIPT_DIR)

from qbank_helper import add_l1, add_l2, save_validated_json

SUBJECT = "Economics"
CONTROL_CHARS = ("\x07", "\x08", "\x0c", "\r", "\t")


def make_mcq(
    correct_text: str,
    wrong1_text: str,
    wrong1_reason: str,
    wrong2_text: str,
    wrong2_reason: str,
    answer_letter: str,
):
    """Assemble A/B/C options and exact 2-key distractor analysis."""
    assert answer_letter in ("A", "B", "C")
    assert len({correct_text, wrong1_text, wrong2_text}) == 3, (
        f"Duplicate option text detected: {correct_text} | {wrong1_text} | {wrong2_text}"
    )
    if answer_letter == "A":
        opts = {"A": correct_text, "B": wrong1_text, "C": wrong2_text}
        dist = {"B": wrong1_reason, "C": wrong2_reason}
    elif answer_letter == "B":
        opts = {"A": wrong1_text, "B": correct_text, "C": wrong2_text}
        dist = {"A": wrong1_reason, "C": wrong2_reason}
    else:
        opts = {"A": wrong1_text, "B": wrong2_text, "C": correct_text}
        dist = {"A": wrong1_reason, "B": wrong2_reason}
    return opts, answer_letter, dist


def ans_cycle(idx: int) -> str:
    """Balanced deterministic rotation across A, B, C."""
    return ("A", "B", "C")[idx % 3]


def build_l1_m1_demand_supply(out: list, calc_ids: set):
    """Module 1: Demand & Supply Analysis, Consumer Choice & Elasticities (10 Qs)."""
    mod = "Module 1"
    sub = "Demand and Supply Analysis"

    # L1-ECN-001 (calc): Point price elasticity from linear demand
    a, b, p = 120.0, 2.5, 30.0
    q = a - b * p
    ep = -b * (p / q)
    ep_wrong1 = -b
    ep_wrong2 = -(q / (b * p))
    opts, ans, dist = make_mcq(
        f"${ep:.2f}$",
        f"${ep_wrong1:.2f}$",
        "Mistakes the demand slope $\\partial Q / \\partial P = -2.5$ for point price elasticity without multiplying by $P/Q$.",
        f"${ep_wrong2:.2f}$",
        "Inverts the price-to-quantity ratio $Q / (b P)$ instead of applying $E_d = (\\partial Q / \\partial P)(P / Q)$.",
        ans_cycle(0),
    )
    add_l1(
        out, "L1-ECN-001", SUBJECT, mod, "Economics", sub,
        "Calculate and interpret price, income, and cross-price elasticities of demand",
        f"A product has linear demand $Q_d = {a:.0f} - {b:.1f}P$. At price $P = \\text{{USD }} {p:.0f}$, the own-price elasticity of demand is closest to:",
        opts, ans,
        f"At $P = {p:.0f}$, quantity demanded is $Q = {a:.0f} - {b:.1f}({p:.0f}) = {q:.0f}$. Point elasticity is $E_d = \\frac{{\\partial Q}}{{\\partial P}} \\cdot \\frac{{P}}{{Q}} = -{b:.1f} \\times \\frac{{{p:.0f}}}{{{q:.0f}}} = {ep:.2f}$.",
        dist,
    )
    calc_ids.add("L1-ECN-001")

    # L1-ECN-002 (calc): Arc price elasticity of demand
    p1, q1, p2, q2 = 40.0, 500.0, 48.0, 420.0
    pct_q = (q2 - q1) / ((q1 + q2) / 2.0)
    pct_p = (p2 - p1) / ((p1 + p2) / 2.0)
    arc_ep = pct_q / pct_p
    w1 = ((q2 - q1) / q1) / ((p2 - p1) / p1)
    w2 = pct_p / pct_q
    opts, ans, dist = make_mcq(
        f"${arc_ep:.2f}$",
        f"${w1:.2f}$",
        "Uses initial point values $Q_1$ and $P_1$ as denominators rather than the midpoint averages.",
        f"${w2:.2f}$",
        "Inverts the arc elasticity ratio by placing percentage price change in the numerator.",
        ans_cycle(1),
    )
    add_l1(
        out, "L1-ECN-002", SUBJECT, mod, "Economics", sub,
        "Calculate and interpret price, income, and cross-price elasticities of demand",
        f"When a streaming service raises its monthly fee from USD {p1:.0f} to USD {p2:.0f}, active subscribers decline from {q1:.0f} thousand to {q2:.0f} thousand. Using the midpoint (arc) formula, the own-price elasticity of demand is closest to:",
        opts, ans,
        f"Midpoint quantity is $({q1:.0f}+{q2:.0f})/2 = {(q1+q2)/2:.0f}$ and midpoint price is $({p1:.0f}+{p2:.0f})/2 = {(p1+p2)/2:.0f}$. Thus $E_d = \\frac{{({q2:.0f}-{q1:.0f})/{(q1+q2)/2:.0f}}}{{({p2:.0f}-{p1:.0f})/{(p1+p2)/2:.0f}}} = \\frac{{{pct_q:.4f}}}{{{pct_p:.4f}}} = {arc_ep:.2f}$.",
        dist,
    )
    calc_ids.add("L1-ECN-002")

    # L1-ECN-003 (calc): Revenue maximization price from linear demand
    a3, b3 = 300.0, 3.0
    p_rev_max = a3 / (2.0 * b3)
    q_rev_max = a3 - b3 * p_rev_max
    rev_max = p_rev_max * q_rev_max
    w1_p = a3 / b3
    w2_p = a3 / (4.0 * b3)
    opts, ans, dist = make_mcq(
        f"USD {p_rev_max:.2f}",
        f"USD {w1_p:.2f}",
        "Sets $Q = 0$ (the choke price) rather than setting marginal revenue equal to zero.",
        f"USD {w2_p:.2f}",
        "Divides the intercept by $4b$ instead of $2b$ when solving $MR = 0$.",
        ans_cycle(2),
    )
    add_l1(
        out, "L1-ECN-003", SUBJECT, mod, "Economics", sub,
        "Determine the price and output that maximize total revenue",
        f"Inverse demand for a digital license is $P = {a3/b3:.0f} - \\frac{{1}}{{{b3:.0f}}}Q$ (equivalently $Q = {a3:.0f} - {b3:.0f}P$), where $P$ is in USD. Which price maximizes total revenue?",
        opts, ans,
        f"Total revenue $TR = P \\cdot Q = {a3:.0f}P - {b3:.0f}P^2$ is maximized where $\\frac{{d(TR)}}{{dP}} = {a3:.0f} - {2*b3:.0f}P = 0$ (unit elasticity $E_d = -1$), giving $P = \\text{{USD }} {p_rev_max:.2f}$ (and $Q = {q_rev_max:.0f}$, $TR = \\text{{USD }} {rev_max:,.0f}$).",
        dist,
    )
    calc_ids.add("L1-ECN-003")

    # L1-ECN-004 (calc): Income elasticity and cross-price elasticity combined demand forecast
    ed, ei, exy = -1.4, 0.8, 0.5
    dp, di, dpy = -0.05, 0.04, 0.06
    dq = ed * dp + ei * di + exy * dpy
    dq_pct = dq * 100.0
    w1 = (ed * (-dp) + ei * di + exy * dpy) * 100.0
    w2 = (ed * dp + ei * di - exy * dpy) * 100.0
    opts, ans, dist = make_mcq(
        f"{dq_pct:+.1f}%",
        f"{w1:+.1f}%",
        "Uses the wrong sign on the own-price change, assuming a 5% price cut reduces demand.",
        f"{w2:+.1f}%",
        "Treats the two goods as complements ($E_{{xy}} < 0$) rather than substitutes ($E_{{xy}} = +0.5$).",
        ans_cycle(3),
    )
    add_l1(
        out, "L1-ECN-004", SUBJECT, mod, "Economics", sub,
        "Calculate and interpret price, income, and cross-price elasticities of demand",
        f"A beverage has own-price elasticity $E_d = {ed:.1f}$, income elasticity $E_I = {ei:.1f}$, and cross-price elasticity with respect to a competing drink $E_{{xy}} = {exy:.1f}$. If its price falls by 5%, consumer income rises by 4%, and the rival price rises by 6%, the expected change in quantity demanded is closest to:",
        opts, ans,
        f"Total percentage change in quantity demanded is $\\%\\Delta Q = E_d(\\%\\Delta P) + E_I(\\%\\Delta I) + E_{{xy}}(\\%\\Delta P_y) = ({ed:.1f})(-5\\%) + ({ei:.1f})(+4\\%) + ({exy:.1f})(+6\\%) = {ed*dp*100:+.1f}\\% {ei*di*100:+.1f}\\% {exy*dpy*100:+.1f}\\% = {dq_pct:+.1f}\\%$.",
        dist,
    )
    calc_ids.add("L1-ECN-004")

    # L1-ECN-005 (calc): Consumer and producer surplus at market equilibrium
    # Demand: P = 100 - 0.5Q; Supply: P = 20 + 0.3Q -> 0.8Q = 80 -> Q* = 100, P* = 50
    a_d, b_d = 100.0, 0.5
    a_s, b_s = 20.0, 0.3
    q_eq = (a_d - a_s) / (b_d + b_s)
    p_eq = a_d - b_d * q_eq
    cs = 0.5 * (a_d - p_eq) * q_eq
    ps = 0.5 * (p_eq - a_s) * q_eq
    ts = cs + ps
    opts, ans, dist = make_mcq(
        f"USD {ts:,.0f}",
        f"USD {cs:,.0f}",
        "Computes only consumer surplus while omitting producer surplus.",
        f"USD {2*ts:,.0f}",
        "Forgets the $1/2$ triangle factor when integrating linear surplus areas.",
        ans_cycle(4),
    )
    add_l1(
        out, "L1-ECN-005", SUBJECT, mod, "Economics", sub,
        "Calculate consumer surplus, producer surplus, and total surplus",
        f"Market inverse demand is $P = {a_d:.0f} - {b_d:.1f}Q$ and inverse supply is $P = {a_s:.0f} + {b_s:.1f}Q$ (prices in USD). Total economic surplus at competitive equilibrium is closest to:",
        opts, ans,
        f"Equilibrium satisfies ${a_d:.0f} - {b_d:.1f}Q = {a_s:.0f} + {b_s:.1f}Q \\implies Q^* = {q_eq:.0f}$ and $P^* = \\text{{USD }} {p_eq:.0f}$. Consumer surplus is $\\frac{{1}}{{2}}({a_d:.0f} - {p_eq:.0f})({q_eq:.0f}) = \\text{{USD }} {cs:,.0f}$ and producer surplus is $\\frac{{1}}{{2}}({p_eq:.0f} - {a_s:.0f})({q_eq:.0f}) = \\text{{USD }} {ps:,.0f}$, yielding total surplus of USD {ts:,.0f}.",
        dist,
    )
    calc_ids.add("L1-ECN-005")

    # L1-ECN-006 (calc): Deadweight loss and tax incidence under per-unit excise tax
    # Using same curves: P_d = 100 - 0.5Q, P_s = 20 + 0.3Q, tax t = 16
    tax = 16.0
    q_tax = (a_d - a_s - tax) / (b_d + b_s)
    dwl = 0.5 * tax * (q_eq - q_tax)
    tax_rev = tax * q_tax
    opts, ans, dist = make_mcq(
        f"USD {dwl:,.0f}",
        f"USD {2*dwl:,.0f}",
        "Calculates the full rectangle $t \\times \\Delta Q$ instead of the deadweight loss triangle $\\frac{{1}}{{2}} t \\times \\Delta Q$.",
        f"USD {tax_rev:,.0f}",
        "Reports government tax revenue ($t \\times Q_{{\\text{{tax}}}}$) rather than deadweight loss.",
        ans_cycle(5),
    )
    add_l1(
        out, "L1-ECN-006", SUBJECT, mod, "Economics", sub,
        "Evaluate the welfare effects of taxes, price ceilings, and price floors",
        f"Given inverse demand $P = {a_d:.0f} - {b_d:.1f}Q$ and inverse supply $P = {a_s:.0f} + {b_s:.1f}Q$, suppose the government imposes a per-unit excise tax of USD {tax:.0f}. The resulting deadweight loss is closest to:",
        opts, ans,
        f"Pre-tax equilibrium is $Q^* = {q_eq:.0f}$. With tax $t = {tax:.0f}$, $P_d - P_s = {tax:.0f} \\implies ({a_d:.0f} - {b_d:.1f}Q) - ({a_s:.0f} + {b_s:.1f}Q) = {tax:.0f} \\implies Q_{{\\text{{tax}}}} = {q_tax:.0f}$. Deadweight loss is $\\frac{{1}}{{2}} \\times t \\times (Q^* - Q_{{\\text{{tax}}}}) = \\frac{{1}}{{2}}({tax:.0f})({q_eq - q_tax:.0f}) = \\text{{USD }} {dwl:,.0f}$.",
        dist,
    )
    calc_ids.add("L1-ECN-006")

    # L1-ECN-007 (calc): Tax burden share borne by buyers via elasticities
    ed7, es7 = -0.6, 1.4
    buyer_share = es7 / (es7 + abs(ed7))
    seller_share = abs(ed7) / (es7 + abs(ed7))
    w2_share = abs(ed7) / es7
    opts, ans, dist = make_mcq(
        f"{buyer_share*100:.1f}%",
        f"{seller_share*100:.1f}%",
        "Computes the seller's share of the tax burden rather than the buyer's share.",
        f"{w2_share*100:.1f}%",
        "Takes the raw ratio $|E_d|/E_s$ instead of normalizing by $E_s + |E_d|$.",
        ans_cycle(6),
    )
    add_l1(
        out, "L1-ECN-007", SUBJECT, mod, "Economics", sub,
        "Evaluate the welfare effects of taxes, price ceilings, and price floors",
        f"In a market where demand elasticity is $E_d = {ed7:.1f}$ and supply elasticity is $E_s = {es7:.1f}$, the proportion of a per-unit excise tax effectively borne by buyers is closest to:",
        opts, ans,
        f"Tax incidence falls more heavily on the less elastic side. Buyers' share is $\\frac{{E_s}}{{E_s + |E_d|}} = \\frac{{{es7:.1f}}}{{{es7:.1f} + {abs(ed7):.1f}}} = {buyer_share*100:.1f}\\%$.",
        dist,
    )
    calc_ids.add("L1-ECN-007")

    # L1-ECN-008 (calc): Binding price ceiling shortage and lost surplus
    p_ceil = 38.0
    q_supp_ceil = (p_ceil - a_s) / b_s
    q_dem_ceil = (a_d - p_ceil) / b_d
    shortage = q_dem_ceil - q_supp_ceil
    opts, ans, dist = make_mcq(
        f"{shortage:.0f} units",
        f"{q_dem_ceil - q_eq:.0f} units",
        "Measures only the expansion in quantity demanded above $Q^*$ without subtracting the contraction in quantity supplied.",
        f"{q_eq - q_supp_ceil:.0f} units",
        "Reports only the drop in quantity supplied below $Q^*$ rather than the full excess demand.",
        ans_cycle(7),
    )
    add_l1(
        out, "L1-ECN-008", SUBJECT, mod, "Economics", sub,
        "Evaluate the welfare effects of taxes, price ceilings, and price floors",
        f"If inverse demand is $P = {a_d:.0f} - {b_d:.1f}Q$ and inverse supply is $P = {a_s:.0f} + {b_s:.1f}Q$, imposing a binding price ceiling at USD {p_ceil:.0f} creates a market shortage of:",
        opts, ans,
        f"At $P = {p_ceil:.0f}$, quantity supplied is $({p_ceil:.0f} - {a_s:.0f})/{b_s:.1f} = {q_supp_ceil:.0f}$ and quantity demanded is $({a_d:.0f} - {p_ceil:.0f})/{b_d:.1f} = {q_dem_ceil:.0f}$. Excess demand (shortage) is ${q_dem_ceil:.0f} - {q_supp_ceil:.0f} = {shortage:.0f}$ units.",
        dist,
    )
    calc_ids.add("L1-ECN-008")

    # L1-ECN-009 (conceptual): Giffen vs Veblen goods
    opts, ans, dist = make_mcq(
        "A Giffen good is an inferior good whose negative income effect exceeds its substitution effect.",
        "A Giffen good has a positive income elasticity of demand greater than one.",
        "Describes a luxury normal good (or Veblen status motivation), whereas Giffen goods must be strongly inferior.",
        "A Veblen good violates the law of demand solely because its income effect outweighs its substitution effect.",
        "Confuses Veblen goods (conspicuous consumption signaling status) with Giffen goods (income effect mechanism).",
        ans_cycle(8),
    )
    add_l1(
        out, "L1-ECN-009", SUBJECT, mod, "Economics", sub,
        "Contrast substitution and income effects for normal, inferior, Giffen, and Veblen goods",
        "Which statement accurately explains an upward-sloping demand relationship?",
        opts, ans,
        "For a Giffen good, when price rises, the negative income effect on an inferior staple good is large enough to dominate the negative substitution effect, causing total quantity demanded to increase. Veblen goods also exhibit upward-sloping demand over some range due to status signaling rather than income-effect dominance.",
        dist,
    )

    # L1-ECN-010 (conceptual): Short-run vs long-run supply and breakeven/shutdown
    opts, ans, dist = make_mcq(
        "Continue operating in the short run if price exceeds average variable cost, even though economic profit is negative.",
        "Shut down immediately in the short run whenever price falls below average total cost.",
        "Confuses the long-run exit condition ($P < ATC$) with the short-run shutdown condition ($P < AVC$).",
        "Continue operating indefinitely in the long run as long as variable costs are covered.",
        "Ignores that fixed costs become variable in the long run, forcing exit unless $P \\ge ATC$.",
        ans_cycle(9),
    )
    add_l1(
        out, "L1-ECN-010", SUBJECT, mod, "Economics", sub,
        "Distinguish between shutdown and breakeven conditions in the short run and long run",
        "A competitive manufacturing plant faces a market price below average total cost ($ATC$) but above average variable cost ($AVC$). To minimize losses, management should:",
        opts, ans,
        "Because fixed costs are sunk in the short run, any price $P > AVC$ generates positive contribution margin toward fixed costs, so staying open minimizes short-run losses. In the long run, the firm exits if $P < ATC$.",
        dist,
    )


def build_l1_m2_market_structures(out: list, calc_ids: set):
    """Module 2: Firms & Market Structures (10 Qs)."""
    mod = "Module 2"
    sub = "Firms and Market Structures"

    # L1-ECN-011 (calc): Perfect competition profit-maximizing output and economic profit
    # TC = 120 + 10Q + 0.5Q^2 -> MC = 10 + Q. P = 34 -> Q = 24
    fc, c1, c2 = 120.0, 10.0, 0.5
    p11 = 34.0
    q11 = (p11 - c1) / (2.0 * c2)
    tc11 = fc + c1 * q11 + c2 * (q11 ** 2)
    tr11 = p11 * q11
    prof11 = tr11 - tc11
    w1 = tr11 - (c1 * q11 + c2 * (q11 ** 2))
    w2 = fc
    opts, ans, dist = make_mcq(
        f"USD {prof11:,.0f}",
        f"USD {w1:,.0f}",
        "Computes contribution margin ($TR - TVC$) by forgetting to subtract fixed cost of USD 120.",
        f"USD {w2:,.0f}",
        "Reports fixed cost rather than net economic profit ($TR - TC$).",
        ans_cycle(10),
    )
    add_l1(
        out, "L1-ECN-011", SUBJECT, mod, "Economics", sub,
        "Determine profit-maximizing price and output under perfect competition",
        f"A price-taking firm faces market price $P = \\text{{USD }} {p11:.0f}$ and has total cost $TC = {fc:.0f} + {c1:.0f}Q + {c2:.1f}Q^2$ (marginal cost $MC = {c1:.0f} + Q$). Its maximum short-run economic profit is closest to:",
        opts, ans,
        f"Profit maximization sets $P = MC \\implies {p11:.0f} = {c1:.0f} + Q \\implies Q^* = {q11:.0f}$. Then $TR = {p11:.0f}({q11:.0f}) = {tr11:.0f}$ and $TC = {fc:.0f} + {c1:.0f}({q11:.0f}) + {c2:.1f}({q11:.0f})^2 = {tc11:.0f}$, yielding profit of USD {prof11:,.0f}.",
        dist,
    )
    calc_ids.add("L1-ECN-011")

    # L1-ECN-012 (calc): Monopoly profit-maximizing price, output, and deadweight loss
    # P = 140 - 2Q -> MR = 140 - 4Q; MC = 20
    a12, b12, mc12 = 140.0, 2.0, 20.0
    q_m = (a12 - mc12) / (2.0 * b12)
    p_m = a12 - b12 * q_m
    q_c = (a12 - mc12) / b12
    dwl12 = 0.5 * (p_m - mc12) * (q_c - q_m)
    prof_m = (p_m - mc12) * q_m
    ts_comp = 0.5 * (a12 - mc12) * q_c
    opts, ans, dist = make_mcq(
        f"USD {dwl12:,.0f}",
        f"USD {ts_comp:,.0f}",
        "Reports total competitive economic surplus rather than the deadweight loss triangle.",
        f"USD {prof_m:,.0f}",
        "Confuses monopoly economic profit ($Q_m(P_m - MC)$) with the deadweight welfare loss triangle.",
        ans_cycle(11),
    )
    add_l1(
        out, "L1-ECN-012", SUBJECT, mod, "Economics", sub,
        "Analyze pricing, output, and welfare loss under monopoly",
        f"A natural monopolist faces market demand $P = {a12:.0f} - {b12:.0f}Q$ and has constant marginal and average total cost $MC = ATC = \\text{{USD }} {mc12:.0f}$. Compared with competitive pricing ($P = MC$), the monopoly deadweight loss is closest to:",
        opts, ans,
        f"Setting $MR = {a12:.0f} - {2*b12:.0f}Q = MC = {mc12:.0f}$ gives $Q_m = {q_m:.0f}$ and $P_m = {a12:.0f} - {b12:.0f}({q_m:.0f}) = \\text{{USD }} {p_m:.0f}$. Competitive output is $Q_c = ({a12:.0f} - {mc12:.0f})/{b12:.0f} = {q_c:.0f}$. Deadweight loss is $\\frac{{1}}{{2}}({p_m:.0f} - {mc12:.0f})({q_c:.0f} - {q_m:.0f}) = \\text{{USD }} {dwl12:,.0f}$.",
        dist,
    )
    calc_ids.add("L1-ECN-012")

    # L1-ECN-013 (calc): Lerner Index / Monopoly Markup from demand elasticity
    ed13, mc13 = -2.5, 45.0
    p13 = mc13 / (1.0 + 1.0 / ed13)
    w1_p = mc13 * (1.0 - 1.0 / ed13)
    w2_p = mc13 / abs(ed13)
    opts, ans, dist = make_mcq(
        f"USD {p13:.2f}",
        f"USD {w1_p:.2f}",
        "Applies markup directly onto $MC$ via $MC(1 + 1/|E_d|)$ instead of solving $\\frac{{P-MC}}{{P}} = \\frac{{1}}{{|E_d|}}$.",
        f"USD {w2_p:.2f}",
        "Divides $MC$ by $|E_d|$ rather than by $(1 - 1/|E_d|)$.",
        ans_cycle(12),
    )
    add_l1(
        out, "L1-ECN-013", SUBJECT, mod, "Economics", sub,
        "Analyze pricing, output, and welfare loss under monopoly",
        f"A firm with market power faces constant price elasticity of demand $E_d = {ed13:.1f}$ and constant marginal cost $MC = \\text{{USD }} {mc13:.0f}$. Its profit-maximizing price is closest to:",
        opts, ans,
        f"From the Lerner markup identity $\\frac{{P - MC}}{{P}} = -\\frac{{1}}{{E_d}} = \\frac{{1}}{{{abs(ed13):.1f}}} = {1/abs(ed13):.2f}$, solving for price gives $P = \\frac{{MC}}{{1 + 1/E_d}} = \\frac{{{mc13:.0f}}}{{1 - {1/abs(ed13):.2f}}} = \\text{{USD }} {p13:.2f}$.",
        dist,
    )
    calc_ids.add("L1-ECN-013")

    # L1-ECN-014 (calc): Cournot duopoly symmetric equilibrium
    # P = 180 - 2.5(q1 + q2), MC = 30
    a14, b14, mc14 = 180.0, 2.5, 30.0
    q_each = (a14 - mc14) / (3.0 * b14)
    Q_tot = 2.0 * q_each
    P_cournot = a14 - b14 * Q_tot
    Q_cartel = (a14 - mc14) / (2.0 * b14)
    P_cartel = a14 - b14 * Q_cartel
    P_comp = mc14
    opts, ans, dist = make_mcq(
        f"USD {P_cournot:.0f}",
        f"USD {P_cartel:.0f}",
        "Solves for the collusive monopoly/cartel price rather than the non-cooperative Cournot-Nash equilibrium.",
        f"USD {P_comp:.0f}",
        "Assumes Bertrand price competition ($P = MC$) rather than Cournot quantity competition.",
        ans_cycle(13),
    )
    add_l1(
        out, "L1-ECN-014", SUBJECT, mod, "Economics", sub,
        "Explain oligopoly models including Cournot, kinked demand, and Nash equilibrium",
        f"Two symmetric Cournot duopolists face market demand $P = {a14:.0f} - {b14:.1f}(q_1 + q_2)$ and each have constant marginal cost $MC = \\text{{USD }} {mc14:.0f}$. In Cournot-Nash equilibrium, the market price is:",
        opts, ans,
        f"Each firm's best response is $q_i = \\frac{{{a14:.0f} - {mc14:.0f} - {b14:.1f}q_j}}{{2({b14:.1f})}}$. By symmetry $q_1 = q_2 = \\frac{{{a14:.0f} - {mc14:.0f}}}{{3({b14:.1f})}} = {q_each:.0f}$, giving total $Q = {Q_tot:.0f}$ and $P = {a14:.0f} - {b14:.1f}({Q_tot:.0f}) = \\text{{USD }} {P_cournot:.0f}$.",
        dist,
    )
    calc_ids.add("L1-ECN-014")

    # L1-ECN-015 (calc): Kinked demand curve MR discontinuity bounds
    p0_k, e_up, e_low = 60.0, -3.0, -1.25
    mr_up = p0_k * (1.0 + 1.0 / e_up)
    mr_low = p0_k * (1.0 + 1.0 / e_low)
    opts, ans, dist = make_mcq(
        f"USD {mr_low:.0f} to USD {mr_up:.0f}",
        f"USD {mr_up:.0f} to USD {p0_k:.0f}",
        "Uses the upper marginal revenue up to the kink price instead of the lower segment marginal revenue as the floor.",
        f"USD 0 to USD {mr_low:.0f}",
        "Sets the upper bound of the MR gap at the lower-segment marginal revenue.",
        ans_cycle(14),
    )
    add_l1(
        out, "L1-ECN-015", SUBJECT, mod, "Economics", sub,
        "Explain oligopoly models including Cournot, kinked demand, and Nash equilibrium",
        f"An oligopolist faces a kinked demand curve at current price $P_0 = \\text{{USD }} {p0_k:.0f}$. Above $P_0$ (rivals ignore price hikes), demand elasticity is $E_{{\\text{{upper}}}} = {e_up:.1f}$; below $P_0$ (rivals match price cuts), demand elasticity is $E_{{\\text{{lower}}}} = {e_low:.2f}$. Over what range can marginal cost fluctuate without changing the firm's profit-maximizing price?",
        opts, ans,
        f"Using $MR = P(1 + 1/E_d)$: upper-segment $MR = {p0_k:.0f}(1 - 1/{abs(e_up):.1f}) = \\text{{USD }} {mr_up:.0f}$ and lower-segment $MR = {p0_k:.0f}(1 - 1/{abs(e_low):.2f}) = \\text{{USD }} {mr_low:.0f}$. Within this vertical MR gap (USD {mr_low:.0f} to USD {mr_up:.0f}), price remains rigid at USD {p0_k:.0f}.",
        dist,
    )
    calc_ids.add("L1-ECN-015")

    # L1-ECN-016 (calc): HHI pre-merger and post-merger change
    shares = [28, 22, 18, 12, 10, 10]
    hhi_pre = sum(s * s for s in shares)
    delta_hhi = 2 * shares[1] * shares[2]  # merge #2 (22%) and #3 (18%)
    hhi_post = hhi_pre + delta_hhi
    w1_hhi = hhi_pre + shares[1] * shares[2]
    opts, ans, dist = make_mcq(
        f"Post-merger HHI = {hhi_post:,}; $\\Delta\\text{{HHI}} = {delta_hhi:,}$",
        f"Post-merger HHI = {w1_hhi:,}; $\\Delta\\text{{HHI}} = {shares[1]*shares[2]:,}$",
        "Computes $\\Delta\\text{{HHI}} = s_A s_B$ instead of $2 s_A s_B$ when expanding $(s_A + s_B)^2 - (s_A^2 + s_B^2)$.",
        f"Post-merger HHI = {hhi_pre:,}; $\\Delta\\text{{HHI}} = 0$",
        "Assumes combining two market shares leaves the sum of squared shares unchanged.",
        ans_cycle(15),
    )
    add_l1(
        out, "L1-ECN-016", SUBJECT, mod, "Economics", sub,
        "Calculate and interpret concentration ratios and the Herfindahl-Hirschman Index",
        "An industry has six firms with market shares of 28%, 22%, 18%, 12%, 10%, and 10%. If the firms holding 22% and 18% propose a merger, the post-merger Herfindahl-Hirschman Index (HHI) and change in HHI are:",
        opts, ans,
        f"Pre-merger $\\text{{HHI}} = 28^2 + 22^2 + 18^2 + 12^2 + 10^2 + 10^2 = {hhi_pre:,}$. Merging shares 22% and 18% creates a 40% firm, raising HHI by $\\Delta\\text{{HHI}} = 2(22)(18) = {delta_hhi:,}$ to {hhi_post:,}.",
        dist,
    )
    calc_ids.add("L1-ECN-016")

    # L1-ECN-017 (calc): N-firm Concentration Ratio vs HHI limitation
    cr4 = sum(shares[:4])
    cr3 = sum(shares[:3])
    opts, ans, dist = make_mcq(
        f"{cr4}%",
        f"{cr3}%",
        "Calculates the 3-firm concentration ratio ($CR_3$) rather than $CR_4$.",
        f"{cr4 + shares[4]}%",
        "Calculates the 5-firm concentration ratio ($CR_5$).",
        ans_cycle(16),
    )
    add_l1(
        out, "L1-ECN-017", SUBJECT, mod, "Economics", sub,
        "Calculate and interpret concentration ratios and the Herfindahl-Hirschman Index",
        "Using market shares of 28%, 22%, 18%, 12%, 10%, and 10%, the pre-merger four-firm concentration ratio ($CR_4$) is:",
        opts, ans,
        f"$CR_4$ sums the market shares of the four largest firms: $28\\% + 22\\% + 18\\% + 12\\% = {cr4}\\%$. Unlike HHI, $CR_4$ does not reflect share dispersion among the top four firms or mergers among smaller firms.",
        dist,
    )
    calc_ids.add("L1-ECN-017")

    # L1-ECN-018 (conceptual): Monopolistic competition long-run equilibrium & excess capacity
    opts, ans, dist = make_mcq(
        "Produces below minimum average total cost with zero economic profit ($P = ATC > MC$).",
        "Produces at minimum average total cost with zero economic profit ($P = MC = ATC$).",
        "Describes perfect competition in long-run equilibrium rather than monopolistic competition.",
        "Earns persistent positive economic profit because product differentiation prevents entry.",
        "Ignores that low entry barriers allow competitors to introduce close substitutes until $P = ATC$.",
        ans_cycle(17),
    )
    add_l1(
        out, "L1-ECN-018", SUBJECT, mod, "Economics", sub,
        "Describe long-run equilibrium and efficiency under monopolistic competition",
        "In long-run equilibrium, a firm operating in a monopolistically competitive market:",
        opts, ans,
        "Free entry drives economic profit to zero ($P = ATC$), so the downward-sloping demand curve is tangent to the $ATC$ curve to the left of minimum $ATC$. Thus $P = ATC > MC$, creating excess capacity and markup over marginal cost.",
        dist,
    )

    # L1-ECN-019 (conceptual): Nash equilibrium in Prisoner's Dilemma payoff matrix
    opts, ans, dist = make_mcq(
        "Both firms cheat (cut prices) because cheating is a strictly dominant strategy for each firm.",
        "Both firms honor the cartel price because joint industry profits are maximized at that outcome.",
        "Joint profit maximization is Pareto superior for the firms, not a Nash equilibrium in a one-shot game.",
        "One firm honors the cartel price while the other cheats, yielding a symmetric stable split.",
        "The cheated firm would improve its payoff by switching to cheating as well.",
        ans_cycle(18),
    )
    add_l1(
        out, "L1-ECN-019", SUBJECT, mod, "Economics", sub,
        "Explain oligopoly models including Cournot, kinked demand, and Nash equilibrium",
        "Two airlines simultaneously choose between maintaining a high collusive fare or discounting. Regardless of the rival's choice, discounting yields a higher individual profit (USD 80M vs USD 70M if rival holds high; USD 40M vs USD 25M if rival discounts). In a one-shot Nash equilibrium:",
        opts, ans,
        "Discounting strictly dominates holding high ($80 > 70$ and $40 > 25$). Therefore, the unique Nash equilibrium is (Discount, Discount), earning USD 40M each despite (High, High) yielding USD 70M each.",
        dist,
    )

    # L1-ECN-020 (conceptual): Identifying market structure via pricing power and elasticity
    opts, ans, dist = make_mcq(
        "Oligopoly with homogeneous products or high interdependence.",
        "Perfect competition with standardized products and zero barriers.",
        "In perfect competition, firms have zero pricing power and take the market price as given.",
        "Monopolistic competition with negligible switching costs and many small rivals.",
        "Monopolistic competition features many firms with limited strategic interdependence.",
        ans_cycle(19),
    )
    add_l1(
        out, "L1-ECN-020", SUBJECT, mod, "Economics", sub,
        "Identify market structures using number of firms, barriers to entry, and pricing power",
        "Four aircraft engine manufacturers dominate global supply. R&D capital barriers are immense, and each firm explicitly anticipates rival reactions before altering list prices or capacity. This industry is best classified as:",
        opts, ans,
        "Small number of dominant firms, very high barriers to entry, and strategic interdependence are the defining characteristics of an oligopoly.",
        dist,
    )


def build_l1_m3_business_cycles(out: list, calc_ids: set):
    """Module 3: Business Cycles, Labor Market & Economic Indicators (10 Qs)."""
    mod = "Module 3"
    sub = "Understanding Business Cycles"

    # L1-ECN-021 (calc): Unemployment rate and labor force participation rate
    pop = 260.0
    emp = 156.0
    unemp = 9.0
    discouraged = 3.0
    lf = emp + unemp
    ur = (unemp / lf) * 100.0
    lfpr = (lf / pop) * 100.0
    ur_broad = ((unemp + discouraged) / (lf + discouraged)) * 100.0
    ur_wrong_pop = (unemp / pop) * 100.0
    opts, ans, dist = make_mcq(
        f"Unemployment rate = {ur:.2f}%; LFPR = {lfpr:.2f}%",
        f"Unemployment rate = {ur_broad:.2f}%; LFPR = {((lf+discouraged)/pop)*100:.2f}%",
        "Incorrectly includes discouraged workers in the official labor force and U-3 unemployed count.",
        f"Unemployment rate = {ur_wrong_pop:.2f}%; LFPR = {lfpr:.2f}%",
        "Divides unemployed persons by the entire working-age population instead of the labor force.",
        ans_cycle(20),
    )
    add_l1(
        out, "L1-ECN-021", SUBJECT, mod, "Economics", sub,
        "Calculate unemployment rates and labor force participation rates",
        f"A country has a working-age population of {pop:.0f} million, with {emp:.0f} million employed, {unemp:.0f} million actively seeking work, and {discouraged:.0f} million discouraged workers who stopped looking. Official unemployment rate and labor force participation rate (LFPR) are closest to:",
        opts, ans,
        f"Official labor force excludes discouraged workers: $LF = {emp:.0f} + {unemp:.0f} = {lf:.0f}$ million. Unemployment rate $= {unemp:.0f}/{lf:.0f} = {ur:.2f}\\%$, and LFPR $= {lf:.0f}/{pop:.0f} = {lfpr:.2f}\\%$.",
        dist,
    )
    calc_ids.add("L1-ECN-021")

    # L1-ECN-022 (calc): Inventory-to-sales ratio dynamics
    inv_q1, sales_q1 = 420.0, 300.0
    inv_q2, sales_q2 = 468.0, 280.0
    isr1 = inv_q1 / sales_q1
    isr2 = inv_q2 / sales_q2
    w1_isr = sales_q2 / inv_q2
    opts, ans, dist = make_mcq(
        f"Rose from {isr1:.2f} to {isr2:.2f}, signaling an approaching contraction (early slowdown).",
        f"Fell from {1/isr1:.2f} to {w1_isr:.2f}, signaling an early recovery.",
        "Inverts the ratio to sales-to-inventory instead of inventory-to-sales.",
        f"Rose from {isr1:.2f} to {isr2:.2f}, signaling businesses are aggressively ramping up production.",
        "Misinterprets involuntary inventory accumulation during falling sales as bullish expansion.",
        ans_cycle(21),
    )
    add_l1(
        out, "L1-ECN-022", SUBJECT, mod, "Economics", sub,
        "Describe business cycle phases and firm inventory/resource adjustments",
        f"Aggregate business inventories rose from USD {inv_q1:.0f}B to USD {inv_q2:.0f}B while quarterly sales fell from USD {sales_q1:.0f}B to USD {sales_q2:.0f}B. How did the inventory-to-sales ratio change, and what cycle phase does this typically indicate?",
        opts, ans,
        f"Inventory-to-sales rose from ${inv_q1:.0f}/{sales_q1:.0f} = {isr1:.2f}$ to ${inv_q2:.0f}/{sales_q2:.0f} = {isr2:.2f}$. Unplanned inventory buildup as sales drop typically precedes production cuts and layoffs at the peak/onset of contraction.",
        dist,
    )
    calc_ids.add("L1-ECN-022")

    # L1-ECN-023 (calc): Okun's Law / Output Gap & Unemployment Relationship
    u_curr, u_nat, okun_coeff = 6.4, 4.4, 2.0
    gap = -okun_coeff * (u_curr - u_nat)
    y_pot = 25000.0
    y_act = y_pot * (1.0 + gap / 100.0)
    opts, ans, dist = make_mcq(
        f"USD {y_act:,.0f} billion (output gap of {gap:.1f}%)",
        f"USD {y_pot * (1.0 - gap/100.0):,.0f} billion (output gap of {-gap:+.1f}%)",
        "Reverses the sign of Okun's law, implying higher unemployment boosts actual GDP above potential.",
        f"USD {y_pot * (1.0 - (u_curr - u_nat)/100.0):,.0f} billion (output gap of {-(u_curr - u_nat):.1f}%)",
        "Assumes a 1-for-1 relationship rather than applying the Okun coefficient of 2.0.",
        ans_cycle(22),
    )
    add_l1(
        out, "L1-ECN-023", SUBJECT, mod, "Economics", sub,
        "Describe unemployment, output gaps, and business cycle dynamics",
        f"Potential GDP is USD {y_pot:,.0f} billion, the natural rate of unemployment is {u_nat:.1f}%, and current unemployment is {u_curr:.1f}%. Using Okun's Law with a coefficient of {okun_coeff:.1f} ($\\text{{Output gap}} = -2.0(u - u^*)$), actual GDP is closest to:",
        opts, ans,
        f"Cyclical unemployment is ${u_curr:.1f}\\% - {u_nat:.1f}\\% = {u_curr-u_nat:.1f}\\%$. Okun's Law implies an output gap of $-2.0({u_curr-u_nat:.1f}\\%) = {gap:.1f}\\%$, so actual GDP $\\approx {y_pot:,.0f} \\times (1 {gap/100.0:+.3f}) = \\text{{USD }} {y_act:,.0f}$ billion.",
        dist,
    )
    calc_ids.add("L1-ECN-023")

    # L1-ECN-024 (calc): Diffusion index calculation
    up_ind, flat_ind, down_ind = 6, 1, 3
    tot_ind = up_ind + flat_ind + down_ind
    diff_idx = ((up_ind + 0.5 * flat_ind) / tot_ind) * 100.0
    w1_diff = (up_ind / tot_ind) * 100.0
    w2_diff = ((up_ind - down_ind) / tot_ind) * 100.0
    opts, ans, dist = make_mcq(
        f"{diff_idx:.1f}%",
        f"{w1_diff:.1f}%",
        "Omits the standard 0.5 weight assigned to unchanged components in a diffusion index.",
        f"{w2_diff:.1f}%",
        "Computes net percentage rising minus falling rather than the 0-100 diffusion scale.",
        ans_cycle(23),
    )
    add_l1(
        out, "L1-ECN-024", SUBJECT, mod, "Economics", sub,
        "Distinguish leading, coincident, and lagging economic indicators",
        f"Of {tot_ind} components in a composite leading indicator index, {up_ind} rose, {flat_ind} was unchanged, and {down_ind} declined during the month. Using standard half-weight for unchanged series, the diffusion index is:",
        opts, ans,
        f"Diffusion index $= \\frac{{\\text{{Rising}} + 0.5 \\times \\text{{Unchanged}}}}{{\\text{{Total}}}} \\times 100 = \\frac{{{up_ind} + 0.5({flat_ind})}}{{{tot_ind}}} \\times 100 = {diff_idx:.1f}\\%$. Values above 50% signal broad-based expansion.",
        dist,
    )
    calc_ids.add("L1-ECN-024")

    # L1-ECN-025 (calc): Labor productivity growth vs unit labor costs
    # ULC growth = Wage growth - Productivity growth
    w_g, prod_g = 4.8, 1.9
    ulc_g = w_g - prod_g
    w1_ulc = w_g + prod_g
    w2_ulc = prod_g - w_g
    opts, ans, dist = make_mcq(
        f"{ulc_g:+.1f}%",
        f"{w1_ulc:+.1f}%",
        "Adds productivity growth to nominal wage growth instead of subtracting productivity gains.",
        f"{w2_ulc:+.1f}%",
        "Subtracts wage growth from productivity growth, reversing the sign of unit labor cost pressure.",
        ans_cycle(24),
    )
    add_l1(
        out, "L1-ECN-025", SUBJECT, mod, "Economics", sub,
        "Analyze resource utilization, productivity, and labor costs over the cycle",
        f"Late in an economic expansion, hourly compensation grows at {w_g:.1f}% annually while output per hour grows at {prod_g:.1f}%. Annual growth in unit labor costs (ULC) is closest to:",
        opts, ans,
        f"Since $\\text{{ULC}} = \\text{{Compensation per hour}} / \\text{{Output per hour}}$, percentage change in ULC is $\\%\\Delta W - \\%\\Delta (Y/L) = {w_g:.1f}\\% - {prod_g:.1f}\\% = {ulc_g:+.1f}\\%$, creating margin compression or cost-push inflation pressure.",
        dist,
    )
    calc_ids.add("L1-ECN-025")

    # L1-ECN-026 (conceptual): Theories of the business cycle (Austrian vs Keynesian vs RBC)
    opts, ans, dist = make_mcq(
        "Real Business Cycle (RBC) theory attributes fluctuations to exogenous technological and supply shocks under flexible prices.",
        "Keynesian theory advocates allowing wages and prices to clear naturally with zero fiscal intervention.",
        "Describes classical/neoclassical laissez-faire policy, whereas Keynesians urge countercyclical fiscal stimulus due to sticky wages.",
        "Austrian school theory attributes recessions primarily to insufficient consumer aggregate demand.",
        "Confuses Keynesian demand-deficiency explanations with the Austrian focus on credit-fueled malinvestment.",
        ans_cycle(25),
    )
    add_l1(
        out, "L1-ECN-026", SUBJECT, mod, "Economics", sub,
        "Compare theories of the business cycle",
        "Which statement accurately characterizes a major business cycle school of thought?",
        opts, ans,
        "Neoclassical / Real Business Cycle (RBC) models view cycles as efficient responses by rational agents to real productivity or technology shocks in markets with flexible prices. Monetarists emphasize money-supply volatility, Austrians emphasize central bank credit distortions, and Keynesians emphasize sticky wages and animal spirits.",
        dist,
    )

    # L1-ECN-027 (conceptual): Classification of leading, coincident, lagging indicators
    opts, ans, dist = make_mcq(
        "Average weekly initial unemployment claims and S&P 500 stock prices.",
        "Industrial production and commercial/industrial loans outstanding.",
        "Industrial production is a coincident indicator, while C&I loans outstanding are a lagging indicator.",
        "Average duration of unemployment and manufacturing & trade sales.",
        "Average duration of unemployment is lagging, while manufacturing & trade sales are coincident.",
        ans_cycle(26),
    )
    add_l1(
        out, "L1-ECN-027", SUBJECT, mod, "Economics", sub,
        "Distinguish leading, coincident, and lagging economic indicators",
        "Which pair consists strictly of LEADING economic indicators?",
        opts, ans,
        "Initial jobless claims (inverted), equity prices, building permits, yield spread, and average weekly manufacturing hours turn ahead of aggregate economic activity. Duration of unemployment and bank C&I loans lag turning points.",
        dist,
    )

    # L1-ECN-028 (conceptual): Early recovery hiring behavior (temporary workers & overtime)
    opts, ans, dist = make_mcq(
        "Firms first increase overtime hours and hire temporary workers before committing to permanent full-time payrolls.",
        "Firms immediately hire permanent staff, causing the unemployment rate to drop sharply before GDP bottoms.",
        "Permanent hiring lags output recovery; unemployment is a lagging indicator that peaks after the trough.",
        "Discouraged workers permanently exit the workforce, keeping the unemployment rate artificially elevated forever.",
        "During recovery, previously discouraged workers re-enter the labor force, which can temporarily hold up the unemployment rate rather than permanently depressing participation.",
        ans_cycle(27),
    )
    add_l1(
        out, "L1-ECN-028", SUBJECT, mod, "Economics", sub,
        "Describe business cycle phases and firm inventory/resource adjustments",
        "Why does the official unemployment rate often continue rising or stay elevated during the initial months of an economic recovery?",
        opts, ans,
        "Uncertain about recovery durability, firms initially stretch existing employees via overtime and use temporary workers; simultaneously, discouraged workers re-enter the labor force, delaying drops in the measured unemployment rate.",
        dist,
    )

    # L1-ECN-029 (conceptual): Credit cycle characteristics vs business cycle
    opts, ans, dist = make_mcq(
        "Credit cycles typically exhibit longer durations and larger amplitudes than traditional business cycles.",
        "Credit cycles are synchronized strictly with 3-year inventory cycles and vanish during low inflation.",
        "Empirical BIS/CFA research shows credit cycles span 10 to 20 years and can build systemic leverage even under low CPI inflation.",
        "Credit cycles only reflect corporate bond issuance and exclude residential real estate collateral.",
        "Residential and commercial property values and private debt are core drivers of credit cycles.",
        ans_cycle(28),
    )
    add_l1(
        out, "L1-ECN-029", SUBJECT, mod, "Economics", sub,
        "Describe credit cycles and their interaction with business cycles",
        "How do credit cycles typically differ from standard business cycles?",
        opts, ans,
        "Credit cycles—driven by private-sector leverage, lending standards, and property valuations—tend to last longer (often 10–20 years) and feature deeper contractions when balance-sheet deleveraging coincides with a recession.",
        dist,
    )

    # L1-ECN-030 (conceptual): Types of unemployment
    opts, ans, dist = make_mcq(
        "Structural unemployment.",
        "Frictional unemployment.",
        "Frictional unemployment reflects normal short-term job search between matches when skills already align.",
        "Cyclical unemployment.",
        "Cyclical unemployment arises from temporary economy-wide recessions rather than permanent technological obsolescence.",
        ans_cycle(29),
    )
    add_l1(
        out, "L1-ECN-030", SUBJECT, mod, "Economics", sub,
        "Distinguish frictional, structural, and cyclical unemployment",
        "Automation and generative software permanently eliminate routine data-entry roles while creating shortages in AI systems engineering. Workers displaced by this long-run skill mismatch experience:",
        opts, ans,
        "Structural unemployment stems from long-run shifts in industry structure or technology that create a mismatch between workers' skills/locations and available jobs.",
        dist,
    )


def build_l1_m4_inflation_indicators(out: list, calc_ids: set):
    """Module 4: Inflation, Deflation & Economic Indicators (10 Qs)."""
    mod = "Module 4"
    sub = "Inflation and Economic Indicators"

    # L1-ECN-031 (calc): Laspeyres, Paasche, and Fisher CPI indices
    # Basket: Food (Q0=10, P0=4 -> P1=5, Q1=8); Tech (Q0=2, P0=50 -> P1=45, Q1=4)
    p0_f, q0_f, p1_f, q1_f = 4.0, 10.0, 5.0, 8.0
    p0_t, q0_t, p1_t, q1_t = 50.0, 2.0, 45.0, 4.0
    lasp = ((p1_f * q0_f + p1_t * q0_t) / (p0_f * q0_f + p0_t * q0_t)) * 100.0
    paas = ((p1_f * q1_f + p1_t * q1_t) / (p0_f * q1_f + p0_t * q1_t)) * 100.0
    fish = math.sqrt(lasp * paas)
    opts, ans, dist = make_mcq(
        f"Laspeyres = {lasp:.2f}; Paasche = {paas:.2f}; Fisher = {fish:.2f}",
        f"Laspeyres = {paas:.2f}; Paasche = {lasp:.2f}; Fisher = {fish:.2f}",
        "Swaps the Laspeyres (base-period quantity weights) and Paasche (current-period quantity weights) indices.",
        f"Laspeyres = {lasp:.2f}; Paasche = {paas:.2f}; Fisher = {(lasp+paas)/2:.2f}",
        "Computes the Fisher index as the arithmetic mean instead of the geometric mean $\\sqrt{{I_L \\times I_P}}$.",
        ans_cycle(30),
    )
    add_l1(
        out, "L1-ECN-031", SUBJECT, mod, "Economics", sub,
        "Calculate and interpret Laspeyres, Paasche, and Fisher price indices",
        "A household basket consists of Food (Year 0: $P=4, Q=10$; Year 1: $P=5, Q=8$) and Electronics (Year 0: $P=50, Q=2$; Year 1: $P=45, Q=4$). With Year 0 as base (= 100), the Year 1 Laspeyres, Paasche, and Fisher indices are closest to:",
        opts, ans,
        f"Laspeyres uses base quantities: $\\frac{{5(10)+45(2)}}{{4(10)+50(2)}} \\times 100 = \\frac{{140}}{{140}} \\times 100 = {lasp:.2f}$. Paasche uses Year 1 quantities: $\\frac{{5(8)+45(4)}}{{4(8)+50(4)}} \\times 100 = \\frac{{220}}{{232}} \\times 100 = {paas:.2f}$. Fisher $= \\sqrt{{{lasp:.2f} \\times {paas:.4f}}} = {fish:.2f}$.",
        dist,
    )
    calc_ids.add("L1-ECN-031")

    # L1-ECN-032 (calc): Nominal vs Real GDP & GDP Deflator inflation rate
    nom0, real0 = 20000.0, 18000.0
    nom1, real1 = 21630.0, 18540.0
    def0 = (nom0 / real0) * 100.0
    def1 = (nom1 / real1) * 100.0
    inf_def = ((def1 / def0) - 1.0) * 100.0
    nom_g = ((nom1 / nom0) - 1.0) * 100.0
    real_g = ((real1 / real0) - 1.0) * 100.0
    opts, ans, dist = make_mcq(
        f"{inf_def:.2f}%",
        f"{nom_g:.2f}%",
        "Reports nominal GDP growth without adjusting for real output growth.",
        f"{real_g:.2f}%",
        "Reports real GDP growth rather than the percentage change in the GDP deflator.",
        ans_cycle(31),
    )
    add_l1(
        out, "L1-ECN-032", SUBJECT, mod, "Economics", sub,
        "Calculate nominal GDP, real GDP, and GDP deflator inflation",
        f"An economy reports Year 0 Nominal GDP of USD {nom0:,.0f}B and Real GDP of USD {real0:,.0f}B. In Year 1, Nominal GDP is USD {nom1:,.0f}B and Real GDP is USD {real1:,.0f}B. Economy-wide inflation measured by the GDP deflator is closest to:",
        opts, ans,
        f"GDP Deflator in Year 0 $= ({nom0:,.0f}/{real0:,.0f}) \\times 100 = {def0:.2f}$. Year 1 Deflator $= ({nom1:,.0f}/{real1:,.0f}) \\times 100 = {def1:.2f}$. Inflation $= ({def1:.4f}/{def0:.4f}) - 1 = {inf_def:.2f}\\%$.",
        dist,
    )
    calc_ids.add("L1-ECN-032")

    # L1-ECN-033 (calc): Expenditure approach GDP calculation
    c_e, i_e, g_e, x_e, m_e, fin_inv = 14200.0, 3800.0, 4100.0, 2900.0, 3500.0, 950.0
    gdp_exp = c_e + i_e + g_e + (x_e - m_e)
    w1_gdp = gdp_exp + fin_inv
    w2_gdp = c_e + i_e + g_e + (x_e + m_e)
    opts, ans, dist = make_mcq(
        f"USD {gdp_exp:,.0f} billion",
        f"USD {w1_gdp:,.0f} billion",
        "Double-counts financial intermediate asset transactions (stock/bond turnover), which are excluded from GDP.",
        f"USD {w2_gdp:,.0f} billion",
        "Adds imports instead of subtracting imports when calculating net exports ($X - M$).",
        ans_cycle(32),
    )
    add_l1(
        out, "L1-ECN-033", SUBJECT, mod, "Economics", sub,
        "Calculate GDP using expenditure and income approaches",
        f"National accounts report household consumption = USD {c_e:,.0f}B, gross private domestic investment = USD {i_e:,.0f}B, government purchases = USD {g_e:,.0f}B, exports = USD {x_e:,.0f}B, imports = USD {m_e:,.0f}B, and secondary-market equity turnover = USD {fin_inv:,.0f}B. Nominal GDP is:",
        opts, ans,
        f"Using the expenditure approach $GDP = C + I + G + (X - M) = {c_e:,.0f} + {i_e:,.0f} + {g_e:,.0f} + ({x_e:,.0f} - {m_e:,.0f}) = \\text{{USD }} {gdp_exp:,.0f}$ billion. Financial asset trading is excluded.",
        dist,
    )
    calc_ids.add("L1-ECN-033")

    # L1-ECN-034 (calc): Compounding inflation / disinflation purchasing power erosion
    inf_y1, inf_y2, inf_y3 = 0.06, 0.04, -0.015
    cpi_factor = (1.0 + inf_y1) * (1.0 + inf_y2) * (1.0 + inf_y3)
    cum_inf = (cpi_factor - 1.0) * 100.0
    pp_loss = (1.0 - 1.0 / cpi_factor) * 100.0
    w1_sum = (inf_y1 + inf_y2 + inf_y3) * 100.0
    opts, ans, dist = make_mcq(
        f"Cumulative price level change = {cum_inf:+.2f}%; purchasing power change = -{pp_loss:.2f}%",
        f"Cumulative price level change = {w1_sum:+.2f}%; purchasing power change = -{w1_sum:.2f}%",
        "Adds annual rates arithmetically instead of compounding and ignores $1/(1+\\pi) - 1$ for purchasing power.",
        f"Cumulative price level change = {cum_inf:+.2f}%; purchasing power change = -{cum_inf:.2f}%",
        "Sets purchasing power erosion equal to cumulative inflation rather than $1 - 1/\\text{{CPI factor}}$.",
        ans_cycle(33),
    )
    add_l1(
        out, "L1-ECN-034", SUBJECT, mod, "Economics", sub,
        "Distinguish inflation, disinflation, hyperinflation, and deflation",
        "An economy experiences inflation of 6.0% in Year 1, disinflation to 4.0% in Year 2, and mild deflation of -1.5% in Year 3. The cumulative three-year change in the price level and purchasing power of currency are closest to:",
        opts, ans,
        f"Price level factor is $(1.06)(1.04)(0.985) = {cpi_factor:.6f}$, giving cumulative inflation of {cum_inf:+.2f}%. Purchasing power falls to $1/{cpi_factor:.6f} = {1/cpi_factor:.6f}$, a decline of {pp_loss:.2f}%.",
        dist,
    )
    calc_ids.add("L1-ECN-034")

    # L1-ECN-035 (calc): Short-run Phillips curve inflation calculation
    pi_exp, beta_pc, u_curr35, u_nairu = 2.5, 0.6, 3.5, 4.5
    pi_act = pi_exp - beta_pc * (u_curr35 - u_nairu)
    w1_pc = pi_exp + beta_pc * (u_curr35 - u_nairu)
    w2_pc = pi_exp - beta_pc * u_curr35
    opts, ans, dist = make_mcq(
        f"{pi_act:.1f}%",
        f"{w1_pc:.1f}%",
        "Uses a positive slope on $(u - u^*)$, implying tight labor markets lower inflation.",
        f"{w2_pc:.1f}%",
        "Uses total unemployment instead of the cyclical gap $(u - u_{{\\text{{NAIRU}}}})$.",
        ans_cycle(34),
    )
    add_l1(
        out, "L1-ECN-035", SUBJECT, mod, "Economics", sub,
        "Explain the NAIRU and short-run vs long-run Phillips curve",
        f"In an expectations-augmented Phillips curve $\\pi = \\pi^e - {beta_pc:.1f}(u - u^*)$, expected inflation is {pi_exp:.1f}%, NAIRU ($u^*$) is {u_nairu:.1f}%, and actual unemployment is {u_curr35:.1f}%. Actual inflation is closest to:",
        opts, ans,
        f"Because unemployment is 1.0 percentage point below NAIRU, tight labor markets lift inflation: $\\pi = {pi_exp:.1f}\\% - {beta_pc:.1f}({u_curr35:.1f}\\% - {u_nairu:.1f}\\%) = {pi_act:.1f}\\%$.",
        dist,
    )
    calc_ids.add("L1-ECN-035")

    # L1-ECN-036 (calc): Real GDP per capita growth approximation
    gdp_nom_g, def_g, pop_g = 7.4, 2.8, 1.1
    real_g36 = ((1.0 + gdp_nom_g/100) / (1.0 + def_g/100) - 1.0) * 100.0
    per_cap_g = ((1.0 + real_g36/100) / (1.0 + pop_g/100) - 1.0) * 100.0
    w1_pc = gdp_nom_g - pop_g
    w2_pc = gdp_nom_g + def_g - pop_g
    opts, ans, dist = make_mcq(
        f"{per_cap_g:.2f}%",
        f"{w1_pc:.2f}%",
        "Subtracts population growth from nominal GDP growth without removing inflation.",
        f"{w2_pc:.2f}%",
        "Adds inflation to nominal growth rather than deflating nominal output.",
        ans_cycle(35),
    )
    add_l1(
        out, "L1-ECN-036", SUBJECT, mod, "Economics", sub,
        "Calculate nominal GDP, real GDP, and GDP deflator inflation",
        f"Nominal GDP grew by {gdp_nom_g:.1f}%, the GDP deflator rose by {def_g:.1f}%, and population expanded by {pop_g:.1f}%. Exact growth in real GDP per capita is closest to:",
        opts, ans,
        f"Real GDP growth $= \\frac{{1.074}}{{1.028}} - 1 = {real_g36:.3f}\\%$. Dividing by population growth gives real GDP per capita growth $= \\frac{{{1+real_g36/100:.6f}}}{{1.011}} - 1 = {per_cap_g:.2f}\\%$.",
        dist,
    )
    calc_ids.add("L1-ECN-036")

    # L1-ECN-037 (conceptual): CPI upward biases
    opts, ans, dist = make_mcq(
        "Substitution bias, quality bias, and new-goods bias.",
        "Exclusion of imported goods and double-counting of intermediate inputs.",
        "CPI includes imported consumer goods and excludes intermediate business inputs.",
        "Overweighting of volatile energy prices compared with core inflation indices.",
        "Core CPI strips food and energy for policy signal, not because headline CPI creates fixed-weight upward bias.",
        ans_cycle(36),
    )
    add_l1(
        out, "L1-ECN-037", SUBJECT, mod, "Economics", sub,
        "Explain biases in fixed-basket consumer price indices",
        "Why does a fixed-basket Laspeyres CPI typically overstate true increases in the cost of living?",
        opts, ans,
        "Fixed weights ignore consumer substitution toward relatively cheaper items (substitution bias), understate quality improvements (quality bias), and delay adding newly invented products until basket updates (new-goods bias).",
        dist,
    )

    # L1-ECN-038 (conceptual): Cost-push vs demand-pull inflation
    opts, ans, dist = make_mcq(
        "Rising prices accompanied by contracting real output (stagflation) caused by an inward shift of short-run aggregate supply.",
        "Rising prices accompanied by expanding real output above potential GDP driven by excess monetary stimulus.",
        "Describes demand-pull inflation, where aggregate demand shifts rightward.",
        "Falling prices alongside falling real output caused by collapsing household credit.",
        "Describes a deflationary demand contraction rather than cost-push inflation.",
        ans_cycle(37),
    )
    add_l1(
        out, "L1-ECN-038", SUBJECT, mod, "Economics", sub,
        "Contrast cost-push and demand-pull inflation",
        "Cost-push inflation is most distinctively characterized by:",
        opts, ans,
        "A supply shock (such as surging energy prices or unit labor costs above productivity) shifts SRAS leftward, simultaneously pushing the price level up and real GDP down.",
        dist,
    )

    # L1-ECN-039 (conceptual): Deflation risks (debt-deflation & deferred consumption)
    opts, ans, dist = make_mcq(
        "Increases the real burden of nominal debt and encourages consumers to delay discretionary purchases.",
        "Lowers real interest rates automatically below zero as nominal rates hit the zero lower bound.",
        "When nominal rates are bounded near zero, falling prices raise real interest rates ($r = i - \\pi > 0$ when $\\pi < 0$).",
        "Transfers real wealth from creditors to leveraged corporate borrowers.",
        "Unexpected deflation transfers wealth from debtors to creditors by raising the real value of fixed nominal obligations.",
        ans_cycle(38),
    )
    add_l1(
        out, "L1-ECN-039", SUBJECT, mod, "Economics", sub,
        "Distinguish inflation, disinflation, hyperinflation, and deflation",
        "Why do central banks regard entrenched economy-wide deflation as a severe macroeconomic hazard?",
        opts, ans,
        "Deflation raises the real value of fixed nominal debts (triggering defaults and fire sales) and incentivizes households and firms to postpone spending in anticipation of lower future prices.",
        dist,
    )

    # L1-ECN-040 (conceptual): Core vs Headline CPI & GDP Deflator vs CPI differences
    opts, ans, dist = make_mcq(
        "The GDP deflator uses current-period production weights and excludes imported consumer goods.",
        "The CPI covers all domestically produced capital goods and government defense equipment.",
        "CPI covers only the urban household consumption basket; capital goods and government spending belong in the GDP deflator.",
        "Core CPI permanently omits housing shelter costs to reduce monthly volatility.",
        "Core CPI excludes food and energy, whereas shelter represents a major share of core CPI.",
        ans_cycle(39),
    )
    add_l1(
        out, "L1-ECN-040", SUBJECT, mod, "Economics", sub,
        "Compare consumer price indices, core inflation, and the GDP deflator",
        "How does the GDP deflator fundamentally differ from the Consumer Price Index (CPI)?",
        opts, ans,
        "The GDP deflator is a Paasche-style index covering all domestic final goods and services (including capital goods and exports, excluding imports), whereas CPI uses a fixed consumer basket that includes imported consumer goods.",
        dist,
    )


def build_l1_m5_fiscal_monetary(out: list, calc_ids: set):
    """Module 5: Fiscal Policy & Monetary Policy (12 Qs)."""
    mod = "Module 5"
    sub = "Fiscal and Monetary Policy"

    # L1-ECN-041 (calc): Fiscal spending multiplier with income tax
    mpc, tax_r, dg = 0.80, 0.25, 40.0
    mult = 1.0 / (1.0 - mpc * (1.0 - tax_r))
    dy = mult * dg
    w1_mult = 1.0 / (1.0 - mpc)
    w2_mult = 1.0 / (mpc * (1.0 - tax_r))
    opts, ans, dist = make_mcq(
        f"USD {dy:.1f} billion (multiplier = {mult:.2f})",
        f"USD {w1_mult*dg:.1f} billion (multiplier = {w1_mult:.2f})",
        "Uses the tax-free multiplier $\\frac{{1}}{{1 - c}}$ instead of $\\frac{{1}}{{1 - c(1 - t)}}$.",
        f"USD {w2_mult*dg:.1f} billion (multiplier = {w2_mult:.2f})",
        "Places $c(1-t)$ directly in the denominator instead of $1 - c(1-t)$.",
        ans_cycle(40),
    )
    add_l1(
        out, "L1-ECN-041", SUBJECT, mod, "Economics", sub,
        "Calculate fiscal multipliers and assess fiscal stimulus impact",
        f"In a closed economy, the marginal propensity to consume out of disposable income is $c = {mpc:.2f}$ and the proportional income tax rate is $t = {tax_r:.2f}$. If government purchases increase by USD {dg:.0f} billion, the total cumulative expansion in aggregate demand (holding prices and interest rates fixed) is:",
        opts, ans,
        f"The government spending multiplier is $\\frac{{1}}{{1 - c(1 - t)}} = \\frac{{1}}{{1 - {mpc:.2f}(1 - {tax_r:.2f})}} = \\frac{{1}}{{1 - {mpc*(1-tax_r):.2f}}} = {mult:.2f}$. Total demand rises by ${mult:.2f} \\times {dg:.0f} = \\text{{USD }} {dy:.1f}$ billion.",
        dist,
    )
    calc_ids.add("L1-ECN-041")

    # L1-ECN-042 (calc): Balanced budget multiplier vs Tax cut impact
    # Lump-sum tax cut of 40B -> initial spending c*40 = 32B -> total impact = c * mult * 40
    dt = 40.0
    tax_mult = (mpc / (1.0 - mpc * (1.0 - tax_r)))
    dy_tax = tax_mult * dt
    opts, ans, dist = make_mcq(
        f"USD {dy_tax:.1f} billion",
        f"USD {dy:.1f} billion",
        "Applies the government purchase multiplier directly to a tax cut, ignoring first-round saving $(1-c)$.",
        f"USD {mpc*dt:.1f} billion",
        "Computes only the first-round consumption boost $c \\Delta T$ without subsequent multiplier rounds.",
        ans_cycle(41),
    )
    add_l1(
        out, "L1-ECN-042", SUBJECT, mod, "Economics", sub,
        "Calculate fiscal multipliers and assess fiscal stimulus impact",
        f"Using $c = {mpc:.2f}$ and $t = {tax_r:.2f}$, if the government instead implements a lump-sum household tax rebate of USD {dt:.0f} billion (with households spending fraction $c$ initially), the cumulative boost to aggregate demand is closest to:",
        opts, ans,
        f"Households initially spend $c \\Delta T = {mpc:.2f}({dt:.0f}) = {mpc*dt:.0f}$ billion (saving the remaining $1-c$). Applying the spending multiplier ${mult:.2f}$ yields ${mult:.2f} \\times {mpc*dt:.0f} = \\text{{USD }} {dy_tax:.1f}$ billion.",
        dist,
    )
    calc_ids.add("L1-ECN-042")

    # L1-ECN-043 (calc): Balanced-budget multiplier in no-tax simple Keynesian model
    # Equal increase in G and lump-sum T by 50B when t=0, c=0.75 -> net multiplier = 1 -> 50B
    dg_bb = 50.0
    c_bb = 0.75
    net_bb = (1.0 / (1.0 - c_bb) - c_bb / (1.0 - c_bb)) * dg_bb
    opts, ans, dist = make_mcq(
        f"USD {net_bb:.0f} billion",
        f"USD 0 billion",
        "Assumes equal spending and tax increases offset each other one-for-one, ignoring household saving out of taxes.",
        f"USD {dg_bb / (1.0 - c_bb):.0f} billion",
        "Applies the spending multiplier without subtracting the contractionary tax multiplier.",
        ans_cycle(42),
    )
    add_l1(
        out, "L1-ECN-043", SUBJECT, mod, "Economics", sub,
        "Calculate fiscal multipliers and assess fiscal stimulus impact",
        f"In a simple closed economy ($c = {c_bb:.2f}$, lump-sum taxes, zero proportional income tax), the government raises both purchases and lump-sum taxes by USD {dg_bb:.0f} billion simultaneously. What is the net increase in equilibrium aggregate demand?",
        opts, ans,
        f"The spending multiplier is $1/(1 - {c_bb:.2f}) = {1/(1-c_bb):.1f}$ and the lump-sum tax multiplier is $-{c_bb:.2f}/(1 - {c_bb:.2f}) = {-c_bb/(1-c_bb):.1f}$. Their sum is the balanced-budget multiplier of $1.0$, yielding ${net_bb:.0f}$ billion.",
        dist,
    )
    calc_ids.add("L1-ECN-043")

    # L1-ECN-044 (calc): Money multiplier & maximum money supply expansion
    rr = 0.125
    inj = 250.0
    mm = 1.0 / rr
    ms_exp = mm * inj
    w1_ms = (mm - 1.0) * inj
    w2_ms = inj / (1.0 - rr)
    opts, ans, dist = make_mcq(
        f"USD {ms_exp:,.0f} million (multiplier = {mm:.1f})",
        f"USD {w1_ms:,.0f} million (multiplier = {mm-1:.1f})",
        "Subtracts 1 from the money multiplier, measuring only additional loans beyond the initial deposit rather than total new broad money.",
        f"USD {w2_ms:,.0f} million (multiplier = {1/(1-rr):.2f})",
        "Computes $1/(1 - rr)$ instead of $1/rr$.",
        ans_cycle(43),
    )
    add_l1(
        out, "L1-ECN-044", SUBJECT, mod, "Economics", sub,
        "Explain money creation, the money multiplier, and quantity theory of money",
        f"Suppose the central bank purchases USD {inj:.0f} million of government bonds from commercial banks, the required reserve ratio is {rr*100:.1f}%, and banks hold zero excess reserves with zero currency leakage. The maximum total increase in the money supply is:",
        opts, ans,
        f"The money multiplier is $m = \\frac{{1}}{{rr}} = \\frac{{1}}{{{rr:.3f}}} = {mm:.1f}$. Total broad money expands by ${mm:.1f} \\times {inj:.0f} = \\text{{USD }} {ms_exp:,.0f}$ million.",
        dist,
    )
    calc_ids.add("L1-ECN-044")

    # L1-ECN-045 (calc): Exact Fisher effect & inflation risk premium
    r_real, pi_e, rp = 0.018, 0.032, 0.004
    i_nom_exact = ((1.0 + r_real) * (1.0 + pi_e) * (1.0 + rp) - 1.0) * 100.0
    i_nom_no_rp = ((1.0 + r_real) * (1.0 + pi_e) - 1.0) * 100.0
    i_nom_approx = (r_real + pi_e + rp) * 100.0
    opts, ans, dist = make_mcq(
        f"{i_nom_exact:.2f}%",
        f"{i_nom_no_rp:.2f}%",
        "Omits the inflation uncertainty risk premium when pricing nominal Treasury yields.",
        f"{(r_real + pi_e)*100:.2f}%",
        "Uses the simple additive Fisher equation without the risk premium.",
        ans_cycle(44),
    )
    add_l1(
        out, "L1-ECN-045", SUBJECT, mod, "Economics", sub,
        "Apply the Fisher effect to decompose nominal interest rates",
        f"If the required real interest rate is {r_real*100:.1f}%, expected annual inflation is {pi_e*100:.1f}%, and the inflation uncertainty risk premium is {rp*100:.1f}%, the exact compounded nominal interest rate is closest to:",
        opts, ans,
        f"Compounding all three components gives $1 + i = (1 + {r_real:.3f})(1 + {pi_e:.3f})(1 + {rp:.3f}) = {(1+r_real)*(1+pi_e)*(1+rp):.6f}$, or $i = {i_nom_exact:.2f}\\%$ (additive approximation is {i_nom_approx:.2f}%).",
        dist,
    )
    calc_ids.add("L1-ECN-045")

    # L1-ECN-046 (calc): Neutral policy rate and Monetary Policy Stance
    r_trend, pi_tgt, curr_pol, pi_curr = 1.75, 2.0, 4.5, 2.2
    neutral_nom = r_trend + pi_tgt
    w1_neutral = r_trend
    w2_neutral = curr_pol - pi_curr
    opts, ans, dist = make_mcq(
        f"Neutral rate = {neutral_nom:.2f}%; current policy is contractionary.",
        f"Neutral rate = {w1_neutral:.2f}%; current policy is expansionary.",
        "Reports only the real trend growth rate as the nominal neutral policy rate and reverses stance assessment.",
        f"Neutral rate = {neutral_nom:.2f}%; current policy is expansionary.",
        "Incorrectly classifies a policy rate above the nominal neutral rate (4.50% > 3.75%) as expansionary.",
        ans_cycle(45),
    )
    add_l1(
        out, "L1-ECN-046", SUBJECT, mod, "Economics", sub,
        "Determine the neutral interest rate and evaluate monetary policy stance",
        f"An economy has real trend growth of {r_trend:.2f}%, an inflation target of {pi_tgt:.1f}%, current inflation of {pi_curr:.1f}%, and a central bank policy rate of {curr_pol:.1f}%. What is the nominal neutral policy rate, and how is current monetary policy oriented?",
        opts, ans,
        f"Nominal neutral rate $= r_{{\\text{{trend}}}} + \\pi_{{\\text{{target}}}} = {r_trend:.2f}\\% + {pi_tgt:.1f}\\% = {neutral_nom:.2f}\\%$. Because the current policy rate ({curr_pol:.1f}%) exceeds {neutral_nom:.2f}%, policy is contractionary.",
        dist,
    )
    calc_ids.add("L1-ECN-046")

    # L1-ECN-047 (calc): Taylor Rule target policy rate
    r_n, pi_47, pi_t47, y_gap = 2.0, 3.6, 2.0, 1.4
    taylor_i = r_n + pi_47 + 0.5 * (pi_47 - pi_t47) + 0.5 * y_gap
    w1_tay = r_n + pi_t47 + 0.5 * (pi_47 - pi_t47) + 0.5 * y_gap
    w2_tay = r_n + pi_47 + 0.5 * (pi_47 - pi_t47) - 0.5 * y_gap
    opts, ans, dist = make_mcq(
        f"{taylor_i:.2f}%",
        f"{w1_tay:.2f}%",
        "Substitutes target inflation instead of actual inflation for the base $\\pi$ term in the Taylor rule.",
        f"{w2_tay:.2f}%",
        "Subtracts the positive output gap rather than adding $0.5(y - y^*)$.",
        ans_cycle(46),
    )
    add_l1(
        out, "L1-ECN-047", SUBJECT, mod, "Economics", sub,
        "Calculate the Taylor Rule target policy rate",
        f"Using the Taylor rule $i^* = r_{{\\text{{neutral}}}} + \\pi + 0.5(\\pi - \\pi^*) + 0.5(y - y^*)$, suppose the real neutral rate $r_{{\\text{{neutral}}}} = {r_n:.1f}\\%$, current inflation $\\pi = {pi_47:.1f}\\%$, target inflation $\\pi^* = {pi_t47:.1f}\\%$, and output is {y_gap:.1f}% above potential. The prescribed policy rate $i^*$ is:",
        opts, ans,
        f"$i^* = {r_n:.1f}\\% + {pi_47:.1f}\\% + 0.5({pi_47:.1f}\\% - {pi_t47:.1f}\\%) + 0.5({y_gap:.1f}\\%) = {r_n + pi_47:.1f}\\% + {0.5*(pi_47-pi_t47):.2f}\\% + {0.5*y_gap:.2f}\\% = {taylor_i:.2f}\\%$.",
        dist,
    )
    calc_ids.add("L1-ECN-047")

    # L1-ECN-048 (calc): Quantity theory of money (MV = PY)
    m_g, v_g, y_g48 = 6.5, -1.0, 2.3
    pi_qtm = (((1 + m_g/100)*(1 + v_g/100)) / (1 + y_g48/100) - 1) * 100.0
    pi_qtm_approx = m_g + v_g - y_g48
    w1_qtm = m_g - v_g - y_g48
    w2_qtm = m_g + v_g + y_g48
    opts, ans, dist = make_mcq(
        f"{pi_qtm_approx:.1f}% (exact: {pi_qtm:.2f}%)",
        f"{w1_qtm:.1f}%",
        "Subtracts velocity decline as a negative, inadvertently adding to inflation rather than reducing MV growth.",
        f"{w2_qtm:.1f}%",
        "Adds real output growth instead of subtracting it when solving $P = MV/Y$.",
        ans_cycle(47),
    )
    add_l1(
        out, "L1-ECN-048", SUBJECT, mod, "Economics", sub,
        "Explain money creation, the money multiplier, and quantity theory of money",
        f"Under the equation of exchange $MV = PY$, suppose broad money supply grows at {m_g:.1f}%, velocity changes by {v_g:.1f}%, and real GDP grows at {y_g48:.1f}%. The implied inflation rate is closest to:",
        opts, ans,
        f"In percentage change form, $\\pi \\approx \\%\\Delta M + \\%\\Delta V - \\%\\Delta Y = {m_g:.1f}\\% + ({v_g:.1f}\\%) - {y_g48:.1f}\\% = {pi_qtm_approx:.1f}\\%$ (exact: $\\frac{{1.065 \\times 0.99}}{{1.023}} - 1 = {pi_qtm:.2f}\\%$).",
        dist,
    )
    calc_ids.add("L1-ECN-048")

    # L1-ECN-049 (conceptual): Ricardian equivalence
    opts, ans, dist = make_mcq(
        "Households save the entire deficit-financed tax cut in anticipation of higher future taxes, leaving aggregate demand unchanged.",
        "Deficit spending permanently raises real interest rates and crowds out private investment dollar-for-dollar.",
        "Describes standard Keynesian/neoclassical crowding out, whereas Ricardian equivalence predicts higher private saving keeps total national saving and interest rates unchanged.",
        "Government bond issuance is treated by households as net private wealth, boosting lifetime consumption.",
        "Ricardian equivalence explicitly assumes government bonds are NOT net wealth because discounted future tax liabilities equal bond value.",
        ans_cycle(48),
    )
    add_l1(
        out, "L1-ECN-049", SUBJECT, mod, "Economics", sub,
        "Evaluate Ricardian equivalence, crowding out, and fiscal policy lags",
        "According to Ricardian equivalence, if a government cuts current taxes and issues sovereign bonds to finance the deficit without changing government spending:",
        opts, ans,
        "Forward-looking taxpayers recognize that bond-financed tax cuts merely defer taxation. They increase private saving by the full tax cut to pay future taxes, leaving consumption, national saving, interest rates, and aggregate demand unchanged.",
        dist,
    )

    # L1-ECN-050 (conceptual): Fiscal policy lags & structural vs cyclical deficit
    opts, ans, dist = make_mcq(
        "Recognition lag, action (legislation) lag, and impact lag.",
        "Only monetary transmission lag, as fiscal changes always take effect immediately upon announcement.",
        "Fiscal policy faces major legislative action lags; impact lags are shorter once spending begins, whereas monetary policy has quick action lags but long impact lags.",
        "A structural budget deficit increases automatically during recessions solely due to automatic stabilizers.",
        "Automatic stabilizers drive the cyclical deficit; the structural deficit reflects the balance at full-employment potential GDP.",
        ans_cycle(49),
    )
    add_l1(
        out, "L1-ECN-050", SUBJECT, mod, "Economics", sub,
        "Evaluate Ricardian equivalence, crowding out, and fiscal policy lags",
        "Which set of implementation lags explains why discretionary fiscal policy can inadvertently destabilize the economy?",
        opts, ans,
        "Fiscal stimulus must overcome recognition lag (identifying the downturn via lagging data), legislative action lag (political passage), and impact lag (disbursing capital into GDP), often arriving after recovery has already started.",
        dist,
    )

    # L1-ECN-051 (conceptual): Central bank roles, independence & liquidity trap
    opts, ans, dist = make_mcq(
        "Demand for money becomes infinitely elastic so further increases in bank reserves fail to lower nominal short-term interest rates.",
        "Commercial banks voluntarily invest all excess reserves into risky corporate equities.",
        "In a liquidity trap, banks and households hoard safe liquid reserves/cash rather than lending or spending.",
        "Operational independence prevents a central bank from controlling inflation targets.",
        "Operational independence enhances inflation-targeting credibility by insulating rate decisions from short-term political interference.",
        ans_cycle(50),
    )
    add_l1(
        out, "L1-ECN-051", SUBJECT, mod, "Economics", sub,
        "Describe monetary policy tools, transmission, central bank independence, and limitations",
        "During a severe deflationary slump near the zero lower bound, a liquidity trap impairs conventional monetary policy because:",
        opts, ans,
        "In a liquidity trap, short-term nominal rates approach zero and money demand turns flat (infinitely elastic), causing standard open-market reserve injections to be hoarded rather than stimulating borrowing, often requiring QE or fiscal expansion.",
        dist,
    )

    # L1-ECN-052 (conceptual): Monetary & fiscal policy interaction mix
    opts, ans, dist = make_mcq(
        "Tight fiscal policy combined with easy monetary policy.",
        "Easy fiscal policy combined with tight monetary policy.",
        "Easy fiscal + tight monetary produces higher interest rates, crowding out private investment and shrinking the private capital share.",
        "Easy fiscal policy combined with easy monetary policy.",
        "Double expansion maximizes aggregate demand and inflation pressure rather than shrinking public borrowing while boosting private investment.",
        ans_cycle(51),
    )
    add_l1(
        out, "L1-ECN-052", SUBJECT, mod, "Economics", sub,
        "Assess the combined effects of monetary and fiscal policy mixes",
        "If policymakers aim to reduce the government budget deficit over the medium term while encouraging private capital investment and keeping aggregate output steady, the optimal policy mix is:",
        opts, ans,
        "Contractionary fiscal policy narrows the deficit and lowers real interest rates, while expansionary monetary policy reinforces lower borrowing costs, stimulating private investment to offset lower public spending.",
        dist,
    )


def build_l1_m6_geopolitics_reg(out: list, calc_ids: set):
    """Module 6: Geopolitics & Economic Regulations (8 Qs)."""
    mod = "Module 6"
    sub = "Geopolitics and Regulations"

    # L1-ECN-053 (calc): Regulatory compliance cost vs risk-reduction benefit (NPV)
    rev, cost_pct, loss_base, p_old, p_new, disc_r = 500.0, 0.012, 300.0, 0.06, 0.015, 0.08
    ann_cost = rev * cost_pct
    ann_benefit = loss_base * (p_old - p_new)
    net_ann = ann_benefit - ann_cost
    pv_perp = net_ann / disc_r
    w1_pv = ann_benefit / disc_r
    w2_pv = (ann_cost - ann_benefit) / disc_r
    opts, ans, dist = make_mcq(
        f"USD {pv_perp:+.2f} million (net positive societal value)",
        f"USD {w1_pv:+.2f} million",
        "Reports gross expected loss avoidance without subtracting ongoing compliance costs.",
        f"USD {w2_pv:+.2f} million",
        "Reverses benefit minus cost, implying the rule destroys economic value.",
        ans_cycle(52),
    )
    add_l1(
        out, "L1-ECN-053", SUBJECT, mod, "Economics", sub,
        "Evaluate economic costs and benefits of financial and industry regulations",
        f"A new clearinghouse rule imposes annual compliance costs equal to {cost_pct*100:.1f}% of USD {rev:.0f} million in annual industry revenue, while lowering the annual probability of a USD {loss_base:.0f} million systemic failure from {p_old*100:.1f}% to {p_new*100:.1f}%. Using a {disc_r*100:.0f}% real discount rate in perpetuity, the net present economic benefit of the regulation is closest to:",
        opts, ans,
        f"Annual compliance cost $= {cost_pct:.3f} \\times {rev:.0f} = \\text{{USD }} {ann_cost:.1f}$M. Annual expected loss reduction $= {loss_base:.0f} \\times ({p_old:.3f} - {p_new:.3f}) = \\text{{USD }} {ann_benefit:.1f}$M. Net annual benefit $= {net_ann:.1f}$M; perpetual NPV $= {net_ann:.1f}/{disc_r:.2f} = \\text{{USD }} {pv_perp:+.2f}$M.",
        dist,
    )
    calc_ids.add("L1-ECN-053")

    # L1-ECN-054 (calc): Geopolitical shock portfolio weighted scenario return
    p_base, p_esc, p_de = 0.55, 0.25, 0.20
    r_base, r_esc, r_de = 8.0, -18.0, 14.0
    exp_ret = p_base * r_base + p_esc * r_esc + p_de * r_de
    var_r = p_base * (r_base - exp_ret)**2 + p_esc * (r_esc - exp_ret)**2 + p_de * (r_de - exp_ret)**2
    sd_r = math.sqrt(var_r)
    w1_ret = (r_base + r_esc + r_de) / 3.0
    w2_ret = p_base * r_base + p_esc * abs(r_esc) + p_de * r_de
    opts, ans, dist = make_mcq(
        f"Expected return = {exp_ret:.2f}%; standard deviation = {sd_r:.2f}%",
        f"Expected return = {w1_ret:.2f}%; standard deviation = {sd_r:.2f}%",
        "Takes an equal-weighted average of scenario returns rather than weighting by assigned geopolitical probabilities.",
        f"Expected return = {w2_ret:.2f}%; standard deviation = {sd_r:.2f}%",
        "Uses $+18\\%$ instead of $-18\\%$ for the tariff escalation tail scenario.",
        ans_cycle(53),
    )
    add_l1(
        out, "L1-ECN-054", SUBJECT, mod, "Economics", sub,
        "Assess geopolitical risk scenarios and their impact on asset valuation",
        "An analyst models semiconductor equity returns across three geopolitical regimes: Status Quo (55% probability, +8% return), Export Embargo Escalation (25%, -18%), and Trade Accord (20%, +14%). Expected return and return standard deviation are closest to:",
        opts, ans,
        f"$E(R) = 0.55(8) + 0.25(-18) + 0.20(14) = 4.4 - 4.5 + 2.8 = {exp_ret:.2f}\\%$. Variance $= 0.55(8 - {exp_ret:.2f})^2 + 0.25(-18 - {exp_ret:.2f})^2 + 0.20(14 - {exp_ret:.2f})^2 = {var_r:.2f}$, so $\\sigma = {sd_r:.2f}\\%$.",
        dist,
    )
    calc_ids.add("L1-ECN-054")

    # L1-ECN-055 (conceptual): Geopolitical archetypes (Autarky, Hegemony, Bilateralism, Multilateralism)
    opts, ans, dist = make_mcq(
        "Hegemony.",
        "Autarky.",
        "Autarky seeks complete national self-sufficiency and minimization of external trade rather than global rule-setting.",
        "Bilateralism.",
        "Bilateralism involves reciprocal agreements between two nations rather than one dominant state underwriting global institutions.",
        ans_cycle(54),
    )
    add_l1(
        out, "L1-ECN-055", SUBJECT, mod, "Economics", sub,
        "Compare geopolitical cooperation and competition archetypes",
        "Which geopolitical model features one dominant nation acting as global rules-setter, reserve currency supplier, and security guarantor with high global trade integration?",
        opts, ans,
        "Hegemony relies on a leading power providing global public goods (reserve liquidity, maritime security, multilateral rules) while maintaining open trade networks.",
        dist,
    )

    # L1-ECN-056 (conceptual): Geopolitical risk categorization (Event, Exogenous, Thematic)
    opts, ans, dist = make_mcq(
        "Thematic risk.",
        "Event risk.",
        "Event risk refers to known scheduled dates (elections, treaty expirations, referendum votes) rather than gradual structural shifts.",
        "Exogenous risk.",
        "Exogenous risk refers to sudden, unanticipated shocks such as pandemics or surprise conflicts.",
        ans_cycle(55),
    )
    add_l1(
        out, "L1-ECN-056", SUBJECT, mod, "Economics", sub,
        "Classify geopolitical risks by velocity, likelihood, and impact",
        "Decades-long supply-chain decoupling, climate migration pressures, and demographic aging reshaping sovereign alliances are best classified as which type of geopolitical risk?",
        opts, ans,
        "Thematic risks are slow-moving, structural forces evolving over years or decades, unlike discrete scheduled event risks or sudden exogenous shocks.",
        dist,
    )

    # L1-ECN-057 (conceptual): National security vs economic tools (Sanctions, Capital Controls)
    opts, ans, dist = make_mcq(
        "Financial sanctions blocking cross-border SWIFT clearing and freezing central bank reserve assets.",
        "Lowering import tariffs on strategic rare-earth minerals.",
        "Reducing import tariffs expands cross-border trade integration rather than restricting economic access.",
        "Unilateral domestic monetary easing to depreciate the domestic exchange rate.",
        "Monetary easing is a macroeconomic stabilization lever rather than a targeted coercive geopolitical tool.",
        ans_cycle(56),
    )
    add_l1(
        out, "L1-ECN-057", SUBJECT, mod, "Economics", sub,
        "Evaluate geopolitical tools including sanctions, tariffs, and standardization",
        "Which measure represents a financial geopolitical tool aimed at constraining a target nation's external liquidity and cross-border payments?",
        opts, ans,
        "Restrictions on payment rails, sovereign reserve freezes, and capital-market exclusions directly weaponize financial infrastructure, whereas tariffs and embargoes operate through goods-trade channels.",
        dist,
    )

    # L1-ECN-058 (conceptual): Regulatory capture vs Regulatory arbitrage
    opts, ans, dist = make_mcq(
        "Regulatory arbitrage.",
        "Regulatory capture.",
        "Regulatory capture occurs when an agency prioritizes the interests of the regulated industry over the public interest.",
        "Regulatory forbearance.",
        "Forbearance occurs when regulators temporarily delay enforcement of capital or solvency rules on distressed institutions.",
        ans_cycle(57),
    )
    add_l1(
        out, "L1-ECN-058", SUBJECT, mod, "Economics", sub,
        "Distinguish regulatory capture, arbitrage, and unintended consequences",
        "After strict leverage caps are imposed on regulated commercial banks, credit origination migrates rapidly to lightly regulated private credit funds offering identical loan structures. This market response exemplifies:",
        opts, ans,
        "Regulatory arbitrage arises when financial activity shifts across jurisdictions or legal entity wrappers to exploit differing regulatory rules.",
        dist,
    )

    # L1-ECN-059 (conceptual): State capitalism vs Market capitalism
    opts, ans, dist = make_mcq(
        "Higher strategic alignment with national industrial policy alongside potential capital misallocation and weaker minority investor protections.",
        "Guaranteed superior long-run total factor productivity growth compared with market capitalism.",
        "State-directed lending often funds politically favored enterprises at below-market costs, risking lower capital efficiency and overcapacity.",
        "Complete elimination of fiscal deficits through sovereign wealth fund transfers.",
        "State-owned enterprise subsidies and implicit guarantees frequently create contingent sovereign fiscal liabilities.",
        ans_cycle(58),
    )
    add_l1(
        out, "L1-ECN-059", SUBJECT, mod, "Economics", sub,
        "Contrast state capitalism and market-oriented governance structures",
        "From an institutional investor's perspective, a defining trade-off of state capitalism (state-owned enterprises and directed credit) is:",
        opts, ans,
        "State capitalism accelerates infrastructure and strategic sector scale-up but introduces political governance interference, soft budget constraints, and subordination of minority shareholder returns.",
        dist,
    )

    # L1-ECN-060 (conceptual): Self-regulating organizations (SROs) vs Government agencies
    opts, ans, dist = make_mcq(
        "Independent SROs recognized and backed by statutory government oversight.",
        "Purely informal trade associations with zero statutory enforcement authority.",
        "Without statutory backing or legal recognition, informal groups struggle to compel compliance across unwilling firms.",
        "Non-SRO legislative committees enacting static statutes without technical market rules.",
        "Legislative bodies lack day-to-day technical flexibility and enforcement specialization compared with SROs and independent regulators.",
        ans_cycle(59),
    )
    add_l1(
        out, "L1-ECN-060", SUBJECT, mod, "Economics", sub,
        "Classify regulatory bodies and self-regulating organizations (SROs)",
        "Which regulatory structure best combines deep industry technical expertise with credible enforcement power?",
        opts, ans,
        "Independent SROs (such as FINRA or recognized securities exchanges) operating under statutory government supervision leverage market expertise while retaining enforceable disciplinary authority.",
        dist,
    )


def build_l1_m7_trade_bop(out: list, calc_ids: set):
    """Module 7: International Trade & Balance of Payments (10 Qs)."""
    mod = "Module 7"
    sub = "International Trade and Capital Flows"

    # L1-ECN-061 (calc): Ricardian comparative advantage opportunity cost & terms of trade
    # Country A: 1 worker produces 12 cars or 36 tons wheat -> OC of 1 car = 3 wheat
    # Country B: 1 worker produces 6 cars or 30 tons wheat -> OC of 1 car = 5 wheat
    a_car, a_wht = 12.0, 36.0
    b_car, b_wht = 6.0, 30.0
    oc_a_car = a_wht / a_car  # 3 wheat
    oc_b_car = b_wht / b_car  # 5 wheat
    opts, ans, dist = make_mcq(
        f"Country A exports cars at a terms of trade between {oc_a_car:.0f} and {oc_b_car:.0f} tons of wheat per car.",
        f"Country B exports cars because its absolute productivity disadvantage is smaller in wheat.",
        "Reverses comparative advantage: Country B has the higher opportunity cost of cars (5 vs 3 wheat) and therefore should export wheat.",
        f"Country A exports wheat at a terms of trade between {1/oc_b_car:.2f} and {1/oc_a_car:.2f} cars per ton of wheat.",
        "Assigns wheat export to Country A, even though Country A's opportunity cost of wheat (0.33 cars) exceeds Country B's (0.20 cars).",
        ans_cycle(60),
    )
    add_l1(
        out, "L1-ECN-061", SUBJECT, mod, "Economics", sub,
        "Compare absolute and comparative advantage and determine mutually beneficial terms of trade",
        f"Per unit of labor, Country A produces {a_car:.0f} cars or {a_wht:.0f} tons of wheat; Country B produces {b_car:.0f} cars or {b_wht:.0f} tons of wheat. Under Ricardian free trade, what pattern of specialization and terms of trade benefit both nations?",
        opts, ans,
        f"Opportunity cost of 1 car is ${a_wht:.0f}/{a_car:.0f} = {oc_a_car:.0f}$ tons of wheat in A and ${b_wht:.0f}/{b_car:.0f} = {oc_b_car:.0f}$ tons in B. Thus A has comparative advantage in cars (B in wheat), and mutually beneficial terms of trade lie between {oc_a_car:.0f} and {oc_b_car:.0f} tons of wheat per car.",
        dist,
    )
    calc_ids.add("L1-ECN-061")

    # L1-ECN-062 (calc): Tariff welfare decomposition (CS loss, PS gain, Gov rev, DWL)
    # Domestic Demand: Q_d = 200 - 2P; Domestic Supply: Q_s = -20 + 2P; World price Pw = 30; Tariff t = 10 -> Pt = 40
    pw, t_tar = 30.0, 10.0
    pt = pw + t_tar
    qd_w, qs_w = 200.0 - 2.0 * pw, -20.0 + 2.0 * pw  # 140, 40 -> imports 100
    qd_t, qs_t = 200.0 - 2.0 * pt, -20.0 + 2.0 * pt  # 120, 60 -> imports 60
    cs_loss = 0.5 * (qd_w + qd_t) * t_tar
    ps_gain = 0.5 * (qs_w + qs_t) * t_tar
    gov_rev = (qd_t - qs_t) * t_tar
    dwl_prod = 0.5 * (qs_t - qs_w) * t_tar
    dwl_cons = 0.5 * (qd_w - qd_t) * t_tar
    dwl_tot = dwl_prod + dwl_cons
    opts, ans, dist = make_mcq(
        f"Government revenue = USD {gov_rev:,.0f}; Deadweight loss = USD {dwl_tot:,.0f}",
        f"Government revenue = USD {(qd_w-qs_w)*t_tar:,.0f}; Deadweight loss = USD {dwl_tot:,.0f}",
        "Computes tariff revenue using pre-tariff imports (100 units) instead of post-tariff imports (60 units).",
        f"Government revenue = USD {gov_rev:,.0f}; Deadweight loss = USD {dwl_prod:,.0f}",
        "Includes only the production distortion triangle while omitting the consumption deadweight loss triangle.",
        ans_cycle(61),
    )
    add_l1(
        out, "L1-ECN-062", SUBJECT, mod, "Economics", sub,
        "Analyze welfare impacts of tariffs, quotas, and export subsidies",
        f"A small country faces world price $P_w = \\text{{USD }} {pw:.0f}$, domestic demand $Q_d = 200 - 2P$, and domestic supply $Q_s = -20 + 2P$. Imposing a specific import tariff of USD {t_tar:.0f} raises domestic price to USD {pt:.0f}. Tariff revenue and total deadweight loss are:",
        opts, ans,
        f"At $P_w={pw:.0f}$: $Q_d={qd_w:.0f}, Q_s={qs_w:.0f}$. At $P_t={pt:.0f}$: $Q_d={qd_t:.0f}, Q_s={qs_t:.0f}$, so imports fall to {qd_t-qs_t:.0f}. Tariff revenue $= {qd_t-qs_t:.0f} \\times {t_tar:.0f} = \\text{{USD }} {gov_rev:,.0f}$. DWL $= \\frac{{1}}{{2}}({qs_t-qs_w:.0f})({t_tar:.0f}) + \\frac{{1}}{{2}}({qd_w-qd_t:.0f})({t_tar:.0f}) = {dwl_prod:.0f} + {dwl_cons:.0f} = \\text{{USD }} {dwl_tot:,.0f}$.",
        dist,
    )
    calc_ids.add("L1-ECN-062")

    # L1-ECN-063 (calc): Macroeconomic Savings-Investment Twin Deficits Identity
    # (S_p - I) + (T - G) = X - M
    sp_minus_i = 180.0
    t_minus_g = -420.0
    ca = sp_minus_i + t_minus_g
    w1_ca = -sp_minus_i + t_minus_g
    w2_ca = sp_minus_i - t_minus_g
    opts, ans, dist = make_mcq(
        f"Current account deficit of USD {abs(ca):.0f} billion ($X - M = {ca:.0f}$ billion)",
        f"Current account surplus of USD {w2_ca:.0f} billion ($X - M = +{w2_ca:.0f}$ billion)",
        "Subtracts the fiscal deficit $(T-G)$ instead of adding it in $(S_p - I) + (T - G) = CA$.",
        f"Current account deficit of USD {abs(w1_ca):.0f} billion ($X - M = {w1_ca:.0f}$ billion)",
        "Treats private net saving $(S_p - I > 0)$ as negative.",
        ans_cycle(62),
    )
    add_l1(
        out, "L1-ECN-063", SUBJECT, mod, "Economics", sub,
        "Apply national saving-investment and balance of payments identities",
        f"An economy runs a fiscal budget deficit ($G - T$) of USD {abs(t_minus_g):.0f} billion while private saving exceeds private domestic investment ($S_p - I$) by USD {sp_minus_i:.0f} billion. Ignoring net foreign income transfers, the current account balance is a:",
        opts, ans,
        f"Using $(S_p - I) + (T - G) = CA$: $({sp_minus_i:+.0f}) + ({t_minus_g:+.0f}) = {ca:+.0f}$ billion USD, i.e., a current account deficit of USD {abs(ca):.0f} billion financed by net foreign capital inflows.",
        dist,
    )
    calc_ids.add("L1-ECN-063")

    # L1-ECN-064 (calc): Balance of Payments accounts reconciliation
    goods_bal, serv_bal, prim_inc, sec_inc, cap_acc = -520.0, 140.0, 65.0, -35.0, 5.0
    ca_tot = goods_bal + serv_bal + prim_inc + sec_inc
    fin_acc = -(ca_tot + cap_acc)
    w1_fin = -(goods_bal + serv_bal)
    opts, ans, dist = make_mcq(
        f"Current Account = USD {ca_tot:.0f}B; Financial Account = USD {fin_acc:+.0f}B",
        f"Current Account = USD {goods_bal + serv_bal:.0f}B; Financial Account = USD {w1_fin:+.0f}B",
        "Omits primary and secondary income from the Current Account and ignores the Capital Account.",
        f"Current Account = USD {ca_tot:.0f}B; Financial Account = USD {-fin_acc:.0f}B",
        "Assigns a financial account outflow instead of the net capital inflow required to balance a current account deficit.",
        ans_cycle(63),
    )
    add_l1(
        out, "L1-ECN-064", SUBJECT, mod, "Economics", sub,
        "Classify transactions across current, capital, and financial accounts",
        f"A country reports Merchandise Trade Balance = USD {goods_bal:.0f}B, Services Balance = USD {serv_bal:+.0f}B, Net Primary Income = USD {prim_inc:+.0f}B, Net Secondary Income = USD {sec_inc:.0f}B, and Capital Account = USD {cap_acc:+.0f}B. Assuming zero statistical discrepancy, the Current Account and Financial Account balances are:",
        opts, ans,
        f"Current Account $= {goods_bal:.0f} + {serv_bal:.0f} + {prim_inc:.0f} + ({sec_inc:.0f}) = \\text{{USD }} {ca_tot:.0f}$B. By $CA + KA + FA = 0$, Financial Account $= -({ca_tot:.0f} + {cap_acc:.0f}) = \\text{{USD }} {fin_acc:+.0f}$B (net capital inflow).",
        dist,
    )
    calc_ids.add("L1-ECN-064")

    # L1-ECN-065 (calc): Marshall-Lerner condition for trade balance improvement
    wx, wm = 0.45, 0.55
    ex, em = 0.80, 1.30
    ml_val = wx * ex + wm * em
    w1_ml = ex + em
    w2_ml = wx * em + wm * ex
    opts, ans, dist = make_mcq(
        f"Weighted elasticity = {ml_val:.3f} (> 1), so currency depreciation will narrow the trade deficit over the long run.",
        f"Weighted elasticity = {ml_val:.3f} (< 1), so depreciation worsens the trade deficit permanently.",
        "Compares the weighted elasticity against 1.5 instead of the true Marshall-Lerner threshold of 1.0.",
        f"Weighted elasticity = {w2_ml:.3f} (< 1), because import share gets multiplied by export elasticity.",
        "Cross-multiplies weights by the wrong elasticities ($w_X \\varepsilon_M + w_M \\varepsilon_X$).",
        ans_cycle(64),
    )
    add_l1(
        out, "L1-ECN-065", SUBJECT, mod, "Economics", sub,
        "Evaluate the Marshall-Lerner condition and J-curve effect",
        f"A nation's trade volume is {wx*100:.0f}% exports ($\\omega_X = {wx:.2f}$) and {wm*100:.0f}% imports ($\\omega_M = {wm:.2f}$). Given long-run price elasticities $\\varepsilon_X = {ex:.2f}$ and $\\varepsilon_M = {em:.2f}$, does the Marshall-Lerner condition hold?",
        opts, ans,
        f"The general Marshall-Lerner threshold is $\\omega_X \\varepsilon_X + \\omega_M \\varepsilon_M > 1$. Here ${wx:.2f}({ex:.2f}) + {wm:.2f}({em:.2f}) = {wx*ex:.3f} + {wm*em:.3f} = {ml_val:.3f} > 1$ (note unweighted sum is {w1_ml:.2f}), so depreciation improves the trade balance after short-run J-curve lags.",
        dist,
    )
    calc_ids.add("L1-ECN-065")

    # L1-ECN-066 (conceptual): Heckscher-Ohlin model
    opts, ans, dist = make_mcq(
        "Exports goods intensive in its relatively abundant factors and imports goods intensive in its scarce factors.",
        "Exports all goods in which it holds an absolute labor productivity advantage regardless of capital stock.",
        "Describes an incorrect absolute-advantage rule rather than Heckscher-Ohlin factor endowment proportions.",
        "Equalizes factor prices exclusively through unrestricted cross-border labor migration.",
        "Heckscher-Ohlin assumes factors cannot move across borders; goods trade alone drives factor-price equalization.",
        ans_cycle(65),
    )
    add_l1(
        out, "L1-ECN-066", SUBJECT, mod, "Economics", sub,
        "Compare Ricardian and Heckscher-Ohlin models of international trade",
        "Under the Heckscher-Ohlin model of international trade, a capital-abundant country:",
        opts, ans,
        "Heckscher-Ohlin explains comparative advantage through relative factor endowments (capital vs labor), predicting that countries export goods utilizing their abundant, cheaper factors intensively.",
        dist,
    )

    # L1-ECN-067 (conceptual): Quotas vs Tariffs vs VERs
    opts, ans, dist = make_mcq(
        "Under a voluntary export restraint (VER), foreign exporters capture the quota rents, creating an even larger domestic welfare loss than a tariff.",
        "Under an import tariff, foreign governments automatically collect the quota license fees.",
        "Domestic governments collect tariff revenue, whereas foreign exporters capture rents under a VER.",
        "Import quotas never generate domestic deadweight loss as long as import licenses are auctioned.",
        "Restricting trade below free-trade volume creates production and consumption deadweight loss triangles regardless of how licenses are allocated.",
        ans_cycle(66),
    )
    add_l1(
        out, "L1-ECN-067", SUBJECT, mod, "Economics", sub,
        "Analyze welfare impacts of tariffs, quotas, and export subsidies",
        "How do the national welfare effects of a Voluntary Export Restraint (VER) compare with an equivalent import tariff?",
        opts, ans,
        "Both tariffs and VERs reduce consumer surplus and create deadweight loss triangles, but under a VER the rectangle of quota rents accrues to foreign exporting firms rather than the importing nation's treasury.",
        dist,
    )

    # L1-ECN-068 (conceptual): Regional economic integration hierarchy
    opts, ans, dist = make_mcq(
        "Common market.",
        "Customs union.",
        "A customs union adopts common external tariffs but does not eliminate restrictions on cross-border labor and capital mobility.",
        "Free trade area.",
        "A free trade area removes internal tariffs only, retaining separate external trade policies and factor barriers.",
        ans_cycle(67),
    )
    add_l1(
        out, "L1-ECN-068", SUBJECT, mod, "Economics", sub,
        "Classify stages of regional economic integration",
        "A regional bloc eliminates internal tariffs, establishes a unified external tariff schedule against non-members, and allows free movement of labor and capital across member borders while retaining distinct national currencies and fiscal budgets. This describes a:",
        opts, ans,
        "Hierarchy of integration: Free Trade Area -> Customs Union (+ common external tariff) -> Common Market (+ free factor mobility) -> Economic Union (+ policy harmonization) -> Monetary Union (+ single currency).",
        dist,
    )

    # L1-ECN-069 (conceptual): J-Curve short-run effect
    opts, ans, dist = make_mcq(
        "Existing trade contracts are fixed in quantity in the short run, so higher import prices immediately inflate the import bill before export volumes respond.",
        "Export elasticities exceed import elasticities immediately on day one, then decay over two years.",
        "Short-run trade elasticities are low (inelastic), causing an initial deterioration before volumes adjust.",
        "Central banks automatically raise tariffs during the first quarter following currency depreciation.",
        "The J-curve results from contract lags and inelastic short-run volume adjustment, not automatic tariff hikes.",
        ans_cycle(68),
    )
    add_l1(
        out, "L1-ECN-069", SUBJECT, mod, "Economics", sub,
        "Evaluate the Marshall-Lerner condition and J-curve effect",
        "Why does a currency depreciation often cause the trade deficit to widen initially before improving (the J-curve effect)?",
        opts, ans,
        "In the short run, import and export volumes are contractually sticky; domestic-currency costs of existing imports jump immediately (price effect) while quantity adjustments (volume effect) occur later.",
        dist,
    )

    # L1-ECN-070 (conceptual): Capital controls & impossible trinity teaser
    opts, ans, dist = make_mcq(
        "Restricting international capital flows allows a country to maintain both a fixed exchange rate and independent domestic monetary policy.",
        "Unrestricted capital mobility allows a central bank to run both a rigid currency peg and an independent interest rate target.",
        "The Mundell-Fleming trilemma states a country can maintain at most two of: free capital mobility, fixed FX rate, and independent monetary policy.",
        "Floating exchange rates force countries to abandon domestic monetary policy autonomy.",
        "Floating exchange rates preserve monetary policy autonomy even with full capital mobility.",
        ans_cycle(69),
    )
    add_l1(
        out, "L1-ECN-070", SUBJECT, mod, "Economics", sub,
        "Explain the macroeconomic policy trilemma and capital flow controls",
        "According to the macroeconomic impossible trinity (trilemma), how do effective capital controls alter a central bank's policy options?",
        opts, ans,
        "A country cannot simultaneously achieve (1) free capital mobility, (2) a fixed exchange rate, and (3) sovereign monetary policy. Imposing capital controls decouples domestic rates from foreign rates, enabling a fixed peg alongside monetary independence.",
        dist,
    )


def build_l1_m8_fx_rates(out: list, calc_ids: set):
    """Module 8: FX Quotes, Cross-Rates, Forward Points & Regimes (10 Qs)."""
    mod = "Module 8"
    sub = "Currency Exchange Rates"

    # L1-ECN-071 (calc): Percentage appreciation/depreciation of base vs price currency
    s0, s1 = 1.0800, 1.1340  # USD/EUR (price/base: USD per 1 EUR)
    eur_chg = (s1 / s0 - 1.0) * 100.0
    usd_chg = ((1.0 / s1) / (1.0 / s0) - 1.0) * 100.0
    opts, ans, dist = make_mcq(
        f"EUR appreciated by {eur_chg:+.2f}%; USD depreciated by {usd_chg:.2f}%",
        f"EUR appreciated by {eur_chg:+.2f}%; USD depreciated by {-eur_chg:.2f}%",
        "Negates the EUR appreciation instead of inverting the quote ($S_0 / S_1 - 1$) to compute USD depreciation.",
        f"USD appreciated by {eur_chg:+.2f}%; EUR depreciated by {usd_chg:.2f}%",
        "Confuses price and base currencies in CFA P/B notation (`USD/EUR` = USD per 1 EUR).",
        ans_cycle(70),
    )
    add_l1(
        out, "L1-ECN-071", SUBJECT, mod, "Economics", sub,
        "Calculate exchange rate appreciation and depreciation using P/B notation",
        f"Using CFA price/base notation, the `USD/EUR` spot rate (USD per 1 EUR) moves from {s0:.4f} to {s1:.4f}. The exact percentage changes in the EUR and USD are:",
        opts, ans,
        f"EUR is the base currency: $\\%\\Delta \\text{{EUR}} = {s1:.4f}/{s0:.4f} - 1 = {eur_chg:+.2f}\\%$. Inverting gives `EUR/USD` falling from {1/s0:.6f} to {1/s1:.6f}: $\\%\\Delta \\text{{USD}} = {s0:.4f}/{s1:.4f} - 1 = {usd_chg:.2f}\\%$.",
        dist,
    )
    calc_ids.add("L1-ECN-071")

    # L1-ECN-072 (calc): FX Cross-Rate calculation
    # Given JPY/USD = 152.00 (JPY per 1 USD) and USD/GBP = 1.2500 (USD per 1 GBP)
    # Find JPY/GBP = (JPY/USD) * (USD/GBP)
    jpy_usd = 152.00
    usd_gbp = 1.2500
    jpy_gbp = jpy_usd * usd_gbp
    w1_cross = jpy_usd / usd_gbp
    w2_cross = 1.0 / jpy_gbp
    opts, ans, dist = make_mcq(
        f"{jpy_gbp:.2f} JPY/GBP",
        f"{w1_cross:.2f} JPY/GBP",
        "Divides JPY/USD by USD/GBP instead of multiplying to cancel the USD currency unit.",
        f"{w2_cross:.5f} JPY/GBP",
        "Computes the inverse quote (`GBP/JPY`) rather than `JPY/GBP`.",
        ans_cycle(71),
    )
    add_l1(
        out, "L1-ECN-072", SUBJECT, mod, "Economics", sub,
        "Calculate FX cross-rates from spot quotes",
        f"Given spot quotes `JPY/USD` = {jpy_usd:.2f} (JPY per 1 USD) and `USD/GBP` = {usd_gbp:.4f} (USD per 1 GBP), the `JPY/GBP` cross-rate (JPY per 1 GBP) is:",
        opts, ans,
        f"Canceling USD: $\\text{{JPY/GBP}} = \\text{{JPY/USD}} \\times \\text{{USD/GBP}} = {jpy_usd:.2f} \\times {usd_gbp:.4f} = {jpy_gbp:.2f}$.",
        dist,
    )
    calc_ids.add("L1-ECN-072")

    # L1-ECN-073 (calc): Cross-rate with common base currency
    # Given CHF/USD = 0.8800 and CAD/USD = 1.3640 -> find CAD/CHF = (CAD/USD) / (CHF/USD)
    chf_usd, cad_usd = 0.8800, 1.3640
    cad_chf = cad_usd / chf_usd
    w1_cad = chf_usd / cad_usd
    w2_cad = chf_usd * cad_usd
    opts, ans, dist = make_mcq(
        f"{cad_chf:.4f} CAD/CHF",
        f"{w1_cad:.4f} CAD/CHF",
        "Computes `CHF/CAD` instead of `CAD/CHF`.",
        f"{w2_cad:.4f} CAD/CHF",
        "Multiplies both USD-based quotes without inverting `CHF/USD` first.",
        ans_cycle(72),
    )
    add_l1(
        out, "L1-ECN-073", SUBJECT, mod, "Economics", sub,
        "Calculate FX cross-rates from spot quotes",
        f"Spot rates in CFA price/base notation are `CHF/USD` = {chf_usd:.4f} (CHF per 1 USD) and `CAD/USD` = {cad_usd:.4f} (CAD per 1 USD). The `CAD/CHF` cross-rate (CAD per 1 CHF) is:",
        opts, ans,
        f"$\\text{{CAD/CHF}} = \\text{{CAD/USD}} \\times \\text{{USD/CHF}} = \\frac{{{cad_usd:.4f}}}{{{chf_usd:.4f}}} = {cad_chf:.4f}$.",
        dist,
    )
    calc_ids.add("L1-ECN-073")

    # L1-ECN-074 (calc): Real exchange rate level and percentage change
    # RER_{USD/EUR} = S_{USD/EUR} * (P_EUR / P_USD)
    s0_74, s1_74 = 1.1000, 1.1440
    p_eur_0, p_eur_1 = 100.0, 102.0
    p_usd_0, p_usd_1 = 100.0, 105.0
    rer0 = s0_74 * (p_eur_0 / p_usd_0)
    rer1 = s1_74 * (p_eur_1 / p_usd_1)
    rer_chg = (rer1 / rer0 - 1.0) * 100.0
    w1_rer = ((s1_74 * (p_usd_1 / p_eur_1)) / rer0 - 1.0) * 100.0
    nom_chg = (s1_74 / s0_74 - 1.0) * 100.0
    opts, ans, dist = make_mcq(
        f"Real `USD/EUR` = {rer1:.4f}; EUR appreciated by {rer_chg:+.2f}% in real terms.",
        f"Real `USD/EUR` = {s1_74*(p_usd_1/p_eur_1):.4f}; EUR appreciated by {w1_rer:+.2f}% in real terms.",
        "Multiplies by domestic-over-foreign price ratio ($P_{{\\text{{USD}}}}/P_{{\\text{{EUR}}}}$) instead of foreign-over-domestic ($P_{{\\text{{EUR}}}}/P_{{\\text{{USD}}}}$).",
        f"Real `USD/EUR` = {s1_74:.4f}; EUR appreciated by {nom_chg:+.2f}% in real terms.",
        "Reports the nominal exchange rate change without adjusting for inflation differential.",
        ans_cycle(73),
    )
    add_l1(
        out, "L1-ECN-074", SUBJECT, mod, "Economics", sub,
        "Calculate real exchange rates and explain competitiveness implications",
        f"The nominal `USD/EUR` rate rises from {s0_74:.4f} to {s1_74:.4f}. Over the same year, the Eurozone price index rises from 100 to {p_eur_1:.0f} while the US price index rises from 100 to {p_usd_1:.0f}. The ending real `USD/EUR` exchange rate and real change in EUR are closest to:",
        opts, ans,
        f"Real exchange rate $RER_{{\\text{{USD/EUR}}}} = S_{{\\text{{USD/EUR}}}} \\times \\frac{{P_{{\\text{{EUR}}}}}}{{P_{{\\text{{USD}}}}}} = {s1_74:.4f} \\times \\frac{{{p_eur_1:.0f}}}{{{p_usd_1:.0f}}} = {rer1:.4f}$. Compared with base {rer0:.4f}, EUR appreciated in real terms by $({rer1:.4f}/{rer0:.4f}) - 1 = {rer_chg:+.2f}\\%$, reducing Eurozone price competitiveness.",
        dist,
    )
    calc_ids.add("L1-ECN-074")

    # L1-ECN-075 (calc): Forward points to outright forward rate and forward discount/premium
    spot_75, pts_75 = 1.2650, -45.0  # USD/GBP, -45 pips = -0.0045
    fwd_75 = spot_75 + pts_75 / 10000.0
    prem_pct = (fwd_75 / spot_75 - 1.0) * 100.0
    w1_fwd = spot_75 + pts_75 / 100.0
    w2_fwd = spot_75 - pts_75 / 10000.0
    opts, ans, dist = make_mcq(
        f"{fwd_75:.4f} (GBP forward discount of {abs(prem_pct):.3f}%)",
        f"{w1_fwd:.4f} (GBP forward discount of {abs(w1_fwd/spot_75-1)*100:.2f}%)",
        "Scales 4-decimal FX points by 100 (JPY convention) instead of 10,000.",
        f"{w2_fwd:.4f} (GBP forward premium of {abs(w2_fwd/spot_75-1)*100:.3f}%)",
        "Adds positive points instead of subtracting negative forward points.",
        ans_cycle(74),
    )
    add_l1(
        out, "L1-ECN-075", SUBJECT, mod, "Economics", sub,
        "Convert forward points to outright forward exchange rates",
        f"A dealer quotes spot `USD/GBP` at {spot_75:.4f} (USD per 1 GBP) and 90-day forward points of {pts_75:.0f}. The outright 90-day forward `USD/GBP` rate and forward discount/premium on GBP are:",
        opts, ans,
        f"Because `USD/GBP` is quoted to 4 decimal places, 1 point $= 0.0001$. Thus $F = {spot_75:.4f} + ({pts_75:.0f}/10{{,}}000) = {fwd_75:.4f}$, a {prem_pct:.3f}% forward discount on GBP.",
        dist,
    )
    calc_ids.add("L1-ECN-075")

    # L1-ECN-076 (calc): Covered interest rate parity forward rate (CFA Act/360)
    s_76, i_usd, i_eur, days_76 = 1.1000, 0.048, 0.028, 180
    f_76 = s_76 * (1.0 + i_usd * days_76 / 360.0) / (1.0 + i_eur * days_76 / 360.0)
    pts_76 = (f_76 - s_76) * 10000.0
    w1_f76 = s_76 * (1.0 + i_eur * days_76 / 360.0) / (1.0 + i_usd * days_76 / 360.0)
    w2_f76 = s_76 * (1.0 + i_usd) / (1.0 + i_eur)
    opts, ans, dist = make_mcq(
        f"{f_76:.4f} (+{pts_76:.1f} forward points)",
        f"{w1_f76:.4f} ({(w1_f76-s_76)*10000:+.1f} forward points)",
        "Inverts the interest rate ratio by placing the base currency (EUR) rate in the numerator.",
        f"{w2_f76:.4f} ({(w2_f76-s_76)*10000:+.1f} forward points)",
        "Uses full 1-year interest rates without de-annualizing for the 180-day horizon.",
        ans_cycle(75),
    )
    add_l1(
        out, "L1-ECN-076", SUBJECT, mod, "Economics", sub,
        "Compute arbitrage-free forward exchange rates using covered interest rate parity",
        f"Spot `USD/EUR` is {s_76:.4f}. Annualized 180-day money market rates (Act/360) are {i_usd*100:.1f}% for USD and {i_eur*100:.1f}% for EUR. The arbitrage-free 180-day forward `USD/EUR` rate is closest to:",
        opts, ans,
        f"By no-arbitrage CIP: $F_{{\\text{{USD/EUR}}}} = {s_76:.4f} \\times \\frac{{1 + {i_usd:.3f}(180/360)}}{{1 + {i_eur:.3f}(180/360)}} = {s_76:.4f} \\times \\frac{{1.0240}}{{1.0140}} = {f_76:.4f}$ (+{pts_76:.1f} pips).",
        dist,
    )
    calc_ids.add("L1-ECN-076")

    # L1-ECN-077 (calc): JPY forward points (scaled by 100)
    s_jpy, pts_jpy = 150.40, -185.0  # JPY/USD, -185 pips = -1.85 JPY
    f_jpy = s_jpy + pts_jpy / 100.0
    w1_jpy = s_jpy + pts_jpy / 10000.0
    w2_jpy = s_jpy - pts_jpy / 100.0
    opts, ans, dist = make_mcq(
        f"{f_jpy:.2f} JPY/USD",
        f"{w1_jpy:.4f} JPY/USD",
        "Divides JPY forward points by 10,000 instead of 100 (JPY quotes carry two decimal places).",
        f"{w2_jpy:.2f} JPY/USD",
        "Adds the absolute points instead of subtracting negative forward points.",
        ans_cycle(76),
    )
    add_l1(
        out, "L1-ECN-077", SUBJECT, mod, "Economics", sub,
        "Convert forward points to outright forward exchange rates",
        f"Spot `JPY/USD` is {s_jpy:.2f} (JPY per 1 USD) and 1-year forward points are {pts_jpy:.0f}. What is the outright 1-year forward `JPY/USD` rate?",
        opts, ans,
        f"For JPY pairs quoted to two decimal places, 1 point $= 0.01$. Thus $F = {s_jpy:.2f} + ({pts_jpy:.0f}/100) = {f_jpy:.2f}$ JPY/USD.",
        dist,
    )
    calc_ids.add("L1-ECN-077")

    # L1-ECN-078 (conceptual): Exchange rate regimes (Currency board vs Dollarization vs Peg)
    opts, ans, dist = make_mcq(
        "A currency board retains a domestic currency backed 100% by foreign reserves and earns seigniorage on reserves, whereas dollarization sacrifices seigniorage.",
        "Dollarization allows the domestic central bank to act freely as an unlimited lender of last resort.",
        "Neither a strict currency board nor dollarization allows discretionary money printing for lender-of-last-resort bailouts.",
        "A crawling peg prohibits central bank FX market intervention while holding the nominal exchange rate permanently fixed.",
        "A crawling peg adjusts the parity band gradually (often for inflation differentials) through active FX intervention.",
        ans_cycle(77),
    )
    add_l1(
        out, "L1-ECN-078", SUBJECT, mod, "Economics", sub,
        "Compare currency exchange rate regimes",
        "What is a key institutional difference between a currency board and formal dollarization?",
        opts, ans,
        "Under a currency board (e.g., Hong Kong), the monetary authority issues local notes backed at least 100% by interest-earning foreign reserve assets (retaining seigniorage), whereas dollarization replaces domestic currency entirely with a foreign currency.",
        dist,
    )

    # L1-ECN-079 (conceptual): Capital flows & FX demand elasticity (Asset market vs trade flow)
    opts, ans, dist = make_mcq(
        "Cross-border portfolio and direct capital flows vastly exceed merchandise trade flows in daily FX turnover.",
        "Import and export invoices clear instantaneously without forward hedging, neutralizing capital accounts.",
        "Trade flows adjust slowly and represent a small fraction of daily FX volume compared with capital flows.",
        "Exchange rates are strictly determined by bilateral consumer price index levels every trading day.",
        "PPP holds only over multi-year horizons; short-term FX rates are driven by interest differentials, risk sentiment, and capital flows.",
        ans_cycle(78),
    )
    add_l1(
        out, "L1-ECN-079", SUBJECT, mod, "Economics", sub,
        "Evaluate exchange rate effects on international trade and capital flows",
        "Why do short-term movements in major floating currencies correlate more closely with yield spreads and equity flows than with bilateral trade deficits?",
        opts, ans,
        "Financial and capital account transactions dwarf current account goods flows in short-term FX volume, so real interest differentials, asset return expectations, and capital flows dominate short-run exchange rate determination.",
        dist,
    )

    # L1-ECN-080 (conceptual): Carry trade & forward discount parity failure
    opts, ans, dist = make_mcq(
        "Borrowing in a lower-yielding currency and investing unhedged in a higher-yielding currency when uncovered IRP fails to hold.",
        "Borrowing in a high-interest currency, converting spot, and locking in a forward rate at covered parity.",
        "Locking in a forward rate locks in Covered Interest Parity—yielding zero arbitrage profit rather than carry-trade alpha.",
        "Purchasing an inflation-indexed bond in the same currency funded by overnight repo.",
        "Intra-currency duration/credit spread trades do not constitute an FX carry trade.",
        ans_cycle(79),
    )
    add_l1(
        out, "L1-ECN-080", SUBJECT, mod, "Economics", sub,
        "Contrast covered interest parity, uncovered interest parity, and FX carry trades",
        "An FX carry trade generates positive excess returns primarily by:",
        opts, ans,
        "In an FX carry trade, investors borrow low-yield funding currencies and go long high-yield currencies unhedged, earning the interest rate differential whenever the high-yield currency does not depreciate by the full amount predicted by UIRP.",
        dist,
    )


def build_l2_v01_to_v05(out: list, calc_ids: set):
    """Level 2 Vignettes V01 to V05 (25 Questions)."""
    # =========================================================================
    # V01: Bid-Ask FX Cross-Rates & Triangular Arbitrage
    # =========================================================================
    vid1 = "ECN-V01"
    vtitle1 = "Apex FX Desk: Bid-Ask Cross-Rates and Triangular Arbitrage"
    # Clean exact quotes (CFA P/B notation):
    # USD/EUR: 1.0980 / 1.0984 (USD per 1 EUR)
    # JPY/USD: 151.20 / 151.26 (JPY per 1 USD)
    # Dealer C direct quote JPY/EUR: 166.15 / 166.22 (JPY per 1 EUR) -> intentionally mispriced high to create arbitrage!
    usd_eur_b, usd_eur_a = 1.0980, 1.0984
    jpy_usd_b, jpy_usd_a = 151.20, 151.26
    jpy_eur_c_b, jpy_eur_c_a = 166.15, 166.22
    vtext1 = (
        "Maya Lin is a senior FX execution trader at Apex Capital Management in New York. "
        "Apex uses standard CFA price/base (`P/B`) currency convention for all quotes. "
        "At 10:00 EST, three Tier-1 liquidity providers stream the following executable spot quotes:\n"
        "- Dealer A (`USD/EUR`, USD per 1 EUR): 1.0980 / 1.0984\n"
        "- Dealer B (`JPY/USD`, JPY per 1 USD): 151.20 / 151.26\n"
        "- Dealer C (`JPY/EUR`, JPY per 1 EUR): 166.15 / 166.22\n"
        "Apex holds a USD 10,000,000 proprietary arbitrage line with zero execution fees across these three dealers."
    )
    mod1, sub1 = "Module 1", "Currency Exchange Rates: Cross-Rates and Arbitrage"

    # Q1: Synthetic JPY/EUR bid and ask from Dealers A & B
    syn_b = usd_eur_b * jpy_usd_b
    syn_a = usd_eur_a * jpy_usd_a
    w1_b = usd_eur_b * jpy_usd_a
    w1_a = usd_eur_a * jpy_usd_b
    opts, ans, dist = make_mcq(
        f"{syn_b:.4f} / {syn_a:.4f}",
        f"{w1_b:.4f} / {w1_a:.4f}",
        "Cross-multiplies bid by ask instead of pairing bids with bids and asks with asks.",
        f"{1/syn_a:.6f} / {1/syn_b:.6f}",
        "Inverts the synthetic cross-rate into `EUR/JPY` instead of `JPY/EUR`.",
        ans_cycle(80),
    )
    add_l2(
        out, "L2-ECN-V01-Q1", SUBJECT, mod1, "Economics", sub1, vid1, vid1, vtitle1, vtext1,
        "Calculate bid-ask FX cross-rates from two dealer quotes",
        "Based on Dealer A and Dealer B quotes, the synthetic `JPY/EUR` interbank bid–ask quote is closest to:",
        opts, ans,
        f"To synthesize `JPY/EUR` = `JPY/USD` $\\times$ `USD/EUR`, multiply bids and multiply asks: Bid $= {jpy_usd_b:.2f} \\times {usd_eur_b:.4f} = {syn_b:.4f}$; Ask $= {jpy_usd_a:.2f} \\times {usd_eur_a:.4f} = {syn_a:.4f}$.",
        dist,
    )
    calc_ids.add("L2-ECN-V01-Q1")

    # Q2: Triangular arbitrage existence and direction
    # Synthetic Ask JPY/EUR = 166.143968 < Dealer C Bid JPY/EUR = 166.15 -> Buy EUR with USD (Dealer A Ask), sell EUR for JPY (Dealer C Bid), sell JPY for USD (Dealer B Ask)!
    # Wait: check USD -> EUR -> JPY -> USD:
    # Start USD 10M -> buy EUR at Dealer A Ask (1.0984) -> EUR = 10M / 1.0984
    # Sell EUR for JPY at Dealer C Bid (166.15) -> JPY = (10M / 1.0984) * 166.15
    # Sell JPY for USD (buy USD with JPY) at Dealer B Ask (151.26 JPY per 1 USD)!
    # Wait: let's check both directions carefully!
    # Direction 1 (USD -> EUR -> JPY -> USD):
    notional = 10_000_000.0
    eur_bought = notional / usd_eur_a
    jpy_bought = eur_bought * jpy_eur_c_b
    usd_end_1 = jpy_bought / jpy_usd_a
    prof_1 = usd_end_1 - notional
    # Wait! Let's check: 166.15 / (1.0984 * 151.26) = 166.15 / 166.143984 = 1.0000362 -> positive profit USD 362.10!
    # Let's make the arbitrage clearer (e.g., Dealer C quote 166.35 / 166.42) so spread isn't razor-thin! Wait: let's keep 166.15 / 166.22 or widen? Wait—let's check! With 166.15 / 166.22, profit is USD 362.10 on 10M, which is genuinely valid (0.36 bps)! Even better, let's check Direction 2 (USD -> JPY -> EUR -> USD):
    # Sell USD for JPY at Dealer B Bid (151.20), buy EUR with JPY at Dealer C Ask (166.22), sell EUR for USD at Dealer A Bid (1.0980):
    usd_end_2 = notional * jpy_usd_b / jpy_eur_c_a * usd_eur_b
    prof_2 = usd_end_2 - notional  # negative!
    opts, ans, dist = make_mcq(
        f"Buy EUR with USD from Dealer A, sell EUR for JPY to Dealer C, and convert JPY back to USD with Dealer B for a profit of USD {prof_1:,.2f}.",
        f"Sell USD for JPY with Dealer B, buy EUR with JPY from Dealer C, and sell EUR for USD to Dealer A for a profit of USD {abs(prof_2):,.2f}.",
        "Takes the loss-making loop: Dealer C's `JPY/EUR` ask (166.22) is higher than the synthetic `JPY/EUR` bid (166.0176), producing a loss.",
        "No triangular arbitrage exists because Dealer C's bid–ask spread overlaps the synthetic bid–ask spread.",
        "Overlap alone only compares inside spreads lazily; exact arbitrage exists because Dealer C's bid (166.15) exceeds the synthetic ask (166.1440).",
        ans_cycle(81),
    )
    add_l2(
        out, "L2-ECN-V01-Q2", SUBJECT, mod1, "Economics", sub1, vid1, vid1, vtitle1, vtext1,
        "Identify triangular arbitrage opportunities and compute arbitrage profits",
        "Using the USD 10,000,000 credit line across Dealers A, B, and C, what is the optimal triangular arbitrage trade and resulting net profit?",
        opts, ans,
        f"Dealer C's `JPY/EUR` bid ({jpy_eur_c_b:.2f}) strictly exceeds the synthetic `JPY/EUR` ask ({syn_a:.4f}). Therefore, sell EUR to Dealer C: (1) Buy EUR with USD 10M at Dealer A's ask ({usd_eur_a:.4f}) $\\to$ EUR {eur_bought:,.2f}; (2) Sell EUR for JPY at Dealer C's bid ({jpy_eur_c_b:.2f}) $\\to$ JPY {jpy_bought:,.0f}; (3) Buy USD with JPY at Dealer B's ask ({jpy_usd_a:.2f}) $\\to$ USD {usd_end_1:,.2f}. Net profit $= \\text{{USD }} {prof_1:,.2f}$.",
        dist,
    )
    calc_ids.add("L2-ECN-V01-Q2")

    # Q3: Inverted quote USD/JPY from Dealer B
    inv_b = 1.0 / jpy_usd_a
    inv_a = 1.0 / jpy_usd_b
    opts, ans, dist = make_mcq(
        f"{inv_b:.6f} / {inv_a:.6f}",
        f"{inv_a:.6f} / {inv_b:.6f}",
        "Places the higher number as the bid rather than inverting the original ask to get the new bid.",
        f"{1/151.23:.6f} / {1/151.23:.6f}",
        "Inverts the midpoint rate and collapses the dealer bid–ask spread to zero.",
        ans_cycle(82),
    )
    add_l2(
        out, "L2-ECN-V01-Q3", SUBJECT, mod1, "Economics", sub1, vid1, vid1, vtitle1, vtext1,
        "Invert bid-ask currency quotes using price/base conventions",
        "If Lin asks Dealer B to quote `USD/JPY` (USD per 1 JPY) consistent with its `JPY/USD` quote of 151.20 / 151.26, the inverted bid–ask quote is closest to:",
        opts, ans,
        f"Inverting `JPY/USD` flips bid and ask: $\\text{{Bid}}_{{\\text{{USD/JPY}}}} = 1/{jpy_usd_a:.2f} = {inv_b:.6f}$ and $\\text{{Ask}}_{{\\text{{USD/JPY}}}} = 1/{jpy_usd_b:.2f} = {inv_a:.6f}$.",
        dist,
    )
    calc_ids.add("L2-ECN-V01-Q3")

    # Q4: Synthetic spread vs Dealer C spread in bps and minimum breakeven Dealer C bid
    spread_c_bps = ((jpy_eur_c_a - jpy_eur_c_b) / ((jpy_eur_c_a + jpy_eur_c_b) / 2.0)) * 10000.0
    spread_syn_bps = ((syn_a - syn_b) / ((syn_a + syn_b) / 2.0)) * 10000.0
    opts, ans, dist = make_mcq(
        f"Synthetic spread is {spread_syn_bps:.2f} bps; Dealer C spread is {spread_c_bps:.2f} bps.",
        f"Synthetic spread is {spread_c_bps:.2f} bps; Dealer C spread is {spread_syn_bps:.2f} bps.",
        "Reverses the two spreads—synthesizing via two legs stacks two bid–ask spreads, making the synthetic spread wider than Dealer C's direct quote.",
        f"Synthetic spread is {spread_syn_bps/2:.2f} bps; Dealer C spread is {spread_c_bps:.2f} bps.",
        "Divides the synthetic bid–ask spread in half rather than comparing full bid–ask width to midpoint.",
        ans_cycle(83),
    )
    add_l2(
        out, "L2-ECN-V01-Q4", SUBJECT, mod1, "Economics", sub1, vid1, vid1, vtitle1, vtext1,
        "Evaluate dealer bid-ask spreads vs synthetic cross-rate spreads",
        "Comparing percentage bid–ask spreads (relative to midpoint), how does the synthetic `JPY/EUR` spread from Dealers A and B compare with Dealer C's direct `JPY/EUR` spread?",
        opts, ans,
        f"Synthetic spread $= ({syn_a:.4f} - {syn_b:.4f})/{(syn_a+syn_b)/2:.4f} = {spread_syn_bps:.2f}$ bps (cumulative cost of two USD legs), whereas Dealer C's direct cross spread $= ({jpy_eur_c_a:.2f} - {jpy_eur_c_b:.2f})/{(jpy_eur_c_a+jpy_eur_c_b)/2:.4f} = {spread_c_bps:.2f}$ bps.",
        dist,
    )
    calc_ids.add("L2-ECN-V01-Q4")

    # Q5: Conceptual - why triangular arbitrage disappears and dealer spread constraint
    opts, ans, dist = make_mcq(
        "Dealer C must quote a bid less than or equal to the synthetic ask and an ask greater than or equal to the synthetic bid.",
        "Dealer C must set both its bid and ask strictly narrower than Dealer A's `USD/EUR` midpoint.",
        "Spreads cannot be compared across different currency pairs (`JPY/EUR` vs `USD/EUR`).",
        "Dealer C must quote a bid strictly above the synthetic ask so liquidity takers always trade directly.",
        "Quoting a bid above the synthetic ask is precisely what creates riskless triangular arbitrage losses for the quoting dealer.",
        ans_cycle(84),
    )
    add_l2(
        out, "L2-ECN-V01-Q5", SUBJECT, mod1, "Economics", sub1, vid1, vid1, vtitle1, vtext1,
        "Explain no-arbitrage bounds on cross-rate dealer quotes",
        "To prevent triangular arbitrage by high-frequency desks, what condition must hold between Dealer C's direct `JPY/EUR` quote and the synthetic cross-rate from Dealers A and B?",
        opts, ans,
        "No-arbitrage requires that a trader cannot buy EUR cheaper synthetically than Dealer C's bid ($\\text{{Bid}}_{{\\text{{direct}}}} \\le \\text{{Ask}}_{{\\text{{synthetic}}}}$) and cannot buy EUR cheaper from Dealer C than selling synthetically ($\\text{{Ask}}_{{\\text{{direct}}}} \\ge \\text{{Bid}}_{{\\text{{synthetic}}}}$).",
        dist,
    )

    # =========================================================================
    # V02: Covered Interest Rate Parity & Arbitrage Profit
    # =========================================================================
    vid2 = "ECN-V02"
    vtitle2 = "Meridian Treasury: Covered Interest Arbitrage"
    # USD/GBP: Spot = 1.2500 / 1.2504 (USD per 1 GBP)
    # 90-day Fwd Points: -60 / -55 -> Fwd bid = 1.2440, Fwd ask = 1.2449
    # Wait: let's make an explicit arbitrage opportunity!
    # Suppose 90-day USD rate (Act/360) = 5.10% borrow / 5.00% lend (so dealer quote 5.00% / 5.10%)
    # 90-day GBP rate (Act/365) = 4.00% lend / 4.10% borrow (Wait: Act/365!)
    # Let's test no-arbitrage CIP forward USD/GBP at mid:
    # 1.2502 * (1 + 0.0505*90/360) / (1 + 0.0405*90/365) = 1.2502 * 1.012625 / 1.0099863 = 1.25347 -> Fwd points ~ +33!
    # Aha! Because i_USD > i_GBP, GBP should trade at a FORWARD PREMIUM in USD/GBP!
    # If dealer quotes forward points as -20 / -15 (USD/GBP fwd = 1.2480 / 1.2489), GBP is massively underpriced forward!
    # Let's check arbitrage: Borrow USD at 5.10% (Act/360), buy GBP spot at Ask 1.2504, invest GBP at 4.00% (Act/365), sell GBP forward at Bid 1.2480?
    # Wait: if GBP forward is UNDERPRICED (1.2480 vs 1.2535 fair value), you want to BUY GBP forward (sell USD forward) -> No! Borrow GBP at 4.10% (Act/365), sell GBP spot for USD at Bid 1.2500, invest USD at 5.00% (Act/360), BUY GBP forward at Ask 1.2489!
    # Let's verify exact profit on borrowing GBP 10,000,000!
    s_b2, s_a2 = 1.2500, 1.2504
    pts_b2, pts_a2 = -20.0, -15.0
    f_b2 = s_b2 + pts_b2 / 10000.0  # 1.2480
    f_a2 = s_a2 + pts_a2 / 10000.0  # 1.2489
    r_usd_lend, r_usd_bor = 0.0500, 0.0510  # Act/360
    r_gbp_lend, r_gbp_bor = 0.0400, 0.0410  # Act/365
    days2 = 90
    gbp_bor = 10_000_000.0
    # Loop A (Borrow GBP -> USD -> Buy GBP forward):
    usd_spot = gbp_bor * s_b2
    usd_mat = usd_spot * (1.0 + r_usd_lend * days2 / 360.0)
    gbp_fwd_rec = usd_mat / f_a2
    gbp_owe = gbp_bor * (1.0 + r_gbp_bor * days2 / 365.0)
    gbp_prof = gbp_fwd_rec - gbp_owe  # Let's check in Python!
    # Loop B (Borrow USD 12,500,000 -> GBP -> Sell GBP forward):
    usd_bor = 12_500_000.0
    gbp_spot_b = usd_bor / s_a2
    gbp_mat_b = gbp_spot_b * (1.0 + r_gbp_lend * days2 / 365.0)
    usd_fwd_rec = gbp_mat_b * f_b2
    usd_owe = usd_bor * (1.0 + r_usd_bor * days2 / 360.0)
    usd_loss_b = usd_fwd_rec - usd_owe  # negative!

    vtext2 = (
        "David Park, corporate treasurer at Meridian Global, observes the following 90-day money market and FX quotes "
        "(using CFA `P/B` notation where `USD/GBP` denotes USD per 1 GBP):\n"
        "- Spot `USD/GBP`: 1.2500 / 1.2504\n"
        "- 90-day forward points (`USD/GBP`): -20 / -15\n"
        "- 90-day USD deposit/borrowing rates (Act/360): 5.00% / 5.10%\n"
        "- 90-day GBP deposit/borrowing rates (Act/365): 4.00% / 4.10%\n"
        "Meridian has access to wholesale credit lines of GBP 10,000,000 or USD 12,500,000 at quoted interbank borrowing rates."
    )
    mod2, sub2 = "Module 1", "Covered Interest Rate Parity"

    # Q1: Outright 90-day forward bid-ask quote
    opts, ans, dist = make_mcq(
        f"{f_b2:.4f} / {f_a2:.4f}",
        f"{s_b2 - 0.0015:.4f} / {s_a2 - 0.0020:.4f}",
        "Applies the ask points (-15) to the spot bid and bid points (-20) to the spot ask, producing an inverted spread.",
        f"{s_b2 + 0.0020:.4f} / {s_a2 + 0.0015:.4f}",
        "Treats negative forward points as positive forward premiums.",
        ans_cycle(85),
    )
    add_l2(
        out, "L2-ECN-V02-Q1", SUBJECT, mod2, "Economics", sub2, vid2, vid2, vtitle2, vtext2,
        "Calculate outright bid-ask forward FX rates from forward points",
        "The outright 90-day forward `USD/GBP` bid–ask quote is:",
        opts, ans,
        f"Add bid points to spot bid and ask points to spot ask: Forward Bid $= {s_b2:.4f} - 0.0020 = {f_b2:.4f}$; Forward Ask $= {s_a2:.4f} - 0.0015 = {f_a2:.4f}$.",
        dist,
    )
    calc_ids.add("L2-ECN-V02-Q1")

    # Q2: Arbitrage-free CIP mid-rate vs market forward quote
    s_mid2 = 0.5 * (s_b2 + s_a2)
    r_usd_mid = 0.5 * (r_usd_lend + r_usd_bor)
    r_gbp_mid = 0.5 * (r_gbp_lend + r_gbp_bor)
    f_cip_mid = s_mid2 * (1.0 + r_usd_mid * days2 / 360.0) / (1.0 + r_gbp_mid * days2 / 365.0)
    pts_cip_mid = (f_cip_mid - s_mid2) * 10000.0
    w1_fcip = s_mid2 * (1.0 + r_gbp_mid * days2 / 365.0) / (1.0 + r_usd_mid * days2 / 360.0)
    opts, ans, dist = make_mcq(
        f"{f_cip_mid:.4f} (+{pts_cip_mid:.1f} points); GBP should trade at a forward premium.",
        f"{w1_fcip:.4f} ({(w1_fcip-s_mid2)*10000:+.1f} points); GBP should trade at a forward discount.",
        "Inverts the interest factor ratio by putting the GBP rate in the numerator instead of USD.",
        f"{s_mid2 * (1 + r_usd_mid)/(1 + r_gbp_mid):.4f}; uses unscaled annual interest rates.",
        "Fails to de-annualize 90-day interest rates using the Act/360 and Act/365 day counts.",
        ans_cycle(86),
    )
    add_l2(
        out, "L2-ECN-V02-Q2", SUBJECT, mod2, "Economics", sub2, vid2, vid2, vtitle2, vtext2,
        "Calculate the arbitrage-free forward rate under Covered Interest Rate Parity",
        "Using midpoint spot and interest rates, what is the theoretical CIP-implied 90-day forward `USD/GBP` rate?",
        opts, ans,
        f"Midpoint spot is {s_mid2:.4f}, USD rate is {r_usd_mid*100:.2f}% (Act/360), GBP rate is {r_gbp_mid*100:.2f}% (Act/365). $F_{{\\text{{CIP}}}} = {s_mid2:.4f} \\times \\frac{{1 + {r_usd_mid:.4f}(90/360)}}{{1 + {r_gbp_mid:.4f}(90/365)}} = {f_cip_mid:.4f}$ (+{pts_cip_mid:.1f} points). Because USD rates exceed GBP rates, GBP must trade at a forward premium.",
        dist,
    )
    calc_ids.add("L2-ECN-V02-Q2")

    # Q3: Exact Covered Interest Arbitrage Profit (GBP)
    w1_gbp_prof = gbp_bor * ((s_b2 * (1 + r_usd_lend * days2 / 360) / f_b2) - (1 + r_gbp_bor * days2 / 365))
    opts, ans, dist = make_mcq(
        f"Borrow GBP 10,000,000, invest in USD, and buy GBP forward for a net profit of GBP {gbp_prof:,.0f}.",
        f"Borrow USD 12,500,000, invest in GBP, and sell GBP forward for a net profit of USD {abs(usd_loss_b):,.0f}.",
        "Executes the reverse loop, locking in a guaranteed loss of USD 66k because GBP yields less than USD AND trades at a forward discount.",
        f"Borrow GBP 10,000,000, invest in USD, and buy GBP forward for a net profit of GBP {w1_gbp_prof:,.0f}.",
        "Applies the forward bid (1.2480) instead of the forward ask (1.2489) when buying GBP forward.",
        ans_cycle(87),
    )
    add_l2(
        out, "L2-ECN-V02-Q3", SUBJECT, mod2, "Economics", sub2, vid2, vid2, vtitle2, vtext2,
        "Calculate net covered interest arbitrage profit using bid-ask rates and day counts",
        "Which covered interest arbitrage strategy generates a riskless profit, and what is the exact net profit at maturity?",
        opts, ans,
        f"Borrow GBP 10,000,000 at {r_gbp_bor*100:.2f}% (Act/365) $\\to$ owe GBP {gbp_owe:,.0f}. Sell GBP spot at {s_b2:.4f} $\\to$ USD {usd_spot:,.0f}; invest at {r_usd_lend*100:.2f}% (Act/360) $\\to$ USD {usd_mat:,.0f}. Buy GBP forward at ask {f_a2:.4f} $\\to$ GBP {gbp_fwd_rec:,.0f}. Riskless profit $= \\text{{GBP }} {gbp_prof:,.0f}$.",
        dist,
    )
    calc_ids.add("L2-ECN-V02-Q3")

    # Q4: Upper arbitrage-free bound on forward ask rate before arbitrage closes
    # Profit vanishes when usd_mat / f_a_breakeven = gbp_owe -> f_a_breakeven = (s_b2 * (1 + r_usd_lend*90/360)) / (1 + r_gbp_bor*90/365)
    f_be_ask = s_b2 * (1.0 + r_usd_lend * days2 / 360.0) / (1.0 + r_gbp_bor * days2 / 365.0)
    w1_be = s_a2 * (1.0 + r_usd_bor * days2 / 360.0) / (1.0 + r_gbp_lend * days2 / 365.0)
    opts, ans, dist = make_mcq(
        f"{f_be_ask:.4f}",
        f"{w1_be:.4f}",
        "Computes the upper arbitrage bound (for borrowing USD) rather than the lower no-arbitrage floor on the forward ask for borrowing GBP.",
        f"{s_b2 * (1 + r_gbp_bor * days2 / 365) / (1 + r_usd_lend * days2 / 360):.4f}",
        "Inverts the interest compounding ratio.",
        ans_cycle(88),
    )
    add_l2(
        out, "L2-ECN-V02-Q4", SUBJECT, mod2, "Economics", sub2, vid2, vid2, vtitle2, vtext2,
        "Determine no-arbitrage forward bid-ask boundaries under transaction costs",
        "Holding spot and money-market rates constant, the arbitrage profit in the GBP-borrowing loop disappears if the 90-day forward `USD/GBP` ask rate rises to at least:",
        opts, ans,
        f"Breakeven forward ask satisfies $F_{{\\text{{ask}}}} \\ge {s_b2:.4f} \\times \\frac{{1 + {r_usd_lend:.4f}(90/360)}}{{1 + {r_gbp_bor:.4f}(90/365)}} = {f_be_ask:.4f}$.",
        dist,
    )
    calc_ids.add("L2-ECN-V02-Q4")

    # Q5: Conceptual - why deviations from CIP occur post-2008 (cross-currency basis)
    opts, ans, dist = make_mcq(
        "Bank balance-sheet regulatory constraints, USD funding liquidity premiums, and counterparty credit risk.",
        "Failure of long-run purchasing power parity due to non-tradable goods inflation.",
        "PPP governs long-run real exchange rates; CIP relies strictly on hedged money-market and forward contracts.",
        "Risk aversion causing investors to demand an equity-like risk premium on unhedged FX exposure.",
        "Unhedged FX risk premiums explain deviations from UIRP, not covered (hedged) interest parity.",
        ans_cycle(89),
    )
    add_l2(
        out, "L2-ECN-V02-Q5", SUBJECT, mod2, "Economics", sub2, vid2, vid2, vtitle2, vtext2,
        "Explain real-world deviations from Covered Interest Rate Parity",
        "In modern global currency markets, persistent minor deviations from textbook Covered Interest Parity (known as the cross-currency basis) primarily arise from:",
        opts, ans,
        "Post-2008 leverage ratio rules (Basel III), dealer balance-sheet scarcity, collateral funding costs, and counterparty credit differences restrict unlimited arbitrage capacity, creating non-zero cross-currency basis spreads.",
        dist,
    )

    # =========================================================================
    # V03: Uncovered Interest Rate Parity (UIRP) & Forward Rate Bias
    # =========================================================================
    vid3 = "ECN-V03"
    vtitle3 = "Nordic Sovereign Fund: Uncovered IRP and Forward Rate Bias"
    # Spot SEK/EUR = 11.4000 (SEK per 1 EUR). 1-yr rates: i_SEK = 3.25%, i_EUR = 4.25% -> SEK expected to appreciate!
    # Wait: make i_SEK = 4.50%, i_EUR = 3.00% -> high-yield SEK expected to depreciate under UIRP!
    s_sek_eur = 11.4000
    i_sek, i_eur3 = 0.0450, 0.0300
    vtext3 = (
        "Astrid Lindqvist manages currency overlays for the Nordic Sovereign Fund (base currency: EUR). "
        "The current spot rate is `SEK/EUR` = 11.4000 (SEK per 1 EUR). "
        "One-year risk-free money market rates are 4.50% in Sweden (SEK) and 3.00% in the Eurozone (EUR). "
        "Quantitative research at the fund also estimated a historical 1-year Fama regression on G10 currencies:\n"
        "$$\\%\\Delta S_{t+1} = a + b(F_t - S_t)/S_t + \\varepsilon_{t+1}$$\n"
        "yielding point estimates $a = 0.002$ and $b = -0.85$."
    )
    mod3, sub3 = "Module 1", "Uncovered Interest Rate Parity"

    # Q1: UIRP expected spot rate in 1 year
    e_s1 = s_sek_eur * (1.0 + i_sek) / (1.0 + i_eur3)
    pct_dep_sek = (s_sek_eur / e_s1 - 1.0) * 100.0  # SEK depreciates vs EUR
    pct_app_eur = (e_s1 / s_sek_eur - 1.0) * 100.0
    w1_s1 = s_sek_eur * (1.0 + i_eur3) / (1.0 + i_sek)
    w2_s1 = s_sek_eur * (1.0 + i_sek - i_eur3)
    opts, ans, dist = make_mcq(
        f"{e_s1:.4f} SEK/EUR (SEK depreciates by {abs(pct_dep_sek):.2f}% vs EUR)",
        f"{w1_s1:.4f} SEK/EUR (SEK appreciates vs EUR)",
        "Inverts the interest factor ratio, predicting the higher-yielding currency appreciates instead of depreciates.",
        f"{w2_s1:.4f} SEK/EUR (SEK depreciates by {(1 - 1/(1+i_sek-i_eur3))*100:.2f}%)",
        "Uses linear approximation $1 + (i_{\\text{SEK}} - i_{\\text{EUR}})$ instead of exact ratio $(1+i_{\\text{SEK}})/(1+i_{\\text{EUR}})$.",
        ans_cycle(90),
    )
    add_l2(
        out, "L2-ECN-V03-Q1", SUBJECT, mod3, "Economics", sub3, vid3, vid3, vtitle3, vtext3,
        "Calculate expected future spot exchange rates under Uncovered Interest Rate Parity",
        "Under exact Uncovered Interest Rate Parity (UIRP), what is the expected 1-year `SEK/EUR` spot exchange rate?",
        opts, ans,
        f"Under UIRP, the higher-yielding currency (SEK) is expected to depreciate to equalize expected returns: $E(S_{{1, \\text{{SEK/EUR}}}}) = {s_sek_eur:.4f} \\times \\frac{{1.0450}}{{1.0300}} = {e_s1:.4f}$ SEK/EUR (EUR appreciates by {pct_app_eur:+.2f}%, meaning SEK depreciates by {pct_dep_sek:.2f}%).",
        dist,
    )
    calc_ids.add("L2-ECN-V03-Q1")

    # Q2: Realized unhedged EUR return if spot moves to 11.4800 instead of UIRP
    s_realized = 11.4800
    r_eur_unhedged = ((1.0 + i_sek) * (s_sek_eur / s_realized) - 1.0) * 100.0
    r_eur_wrong_dir = ((1.0 + i_sek) * (s_realized / s_sek_eur) - 1.0) * 100.0
    opts, ans, dist = make_mcq(
        f"{r_eur_unhedged:.2f}%",
        f"{r_eur_wrong_dir:.2f}%",
        "Multiplies by $S_1 / S_0$ instead of $S_0 / S_1$ when converting a SEK investment back into EUR under `SEK/EUR` quotes.",
        f"{(i_sek - (s_realized/s_sek_eur - 1))*100:.2f}%",
        "Uses an additive approximation rather than exact compounding $(1+i_{\\text{SEK}})(S_0/S_1) - 1$.",
        ans_cycle(91),
    )
    add_l2(
        out, "L2-ECN-V03-Q2", SUBJECT, mod3, "Economics", sub3, vid3, vid3, vtitle3, vtext3,
        "Calculate unhedged foreign investment returns in domestic currency",
        f"Suppose the fund invests EUR unhedged into 1-year SEK deposits at {i_sek*100:.2f}% and the realized `SEK/EUR` spot rate in one year is {s_realized:.4f}. The fund's realized 1-year return in EUR terms is closest to:",
        opts, ans,
        f"Because `SEK/EUR` rose from {s_sek_eur:.4f} to {s_realized:.4f}, SEK depreciated by $({s_sek_eur:.4f}/{s_realized:.4f}) - 1 = {(s_sek_eur/s_realized - 1)*100:.2f}\\%$ vs EUR. Total EUR return $= (1.0450) \\times ({s_sek_eur:.4f}/{s_realized:.4f}) - 1 = {r_eur_unhedged:.2f}\\%$, outperforming the {i_eur3*100:.2f}% domestic EUR rate.",
        dist,
    )
    calc_ids.add("L2-ECN-V03-Q2")

    # Q3: Fama forward-rate unbiasedness prediction vs UIRP
    fwd_prem = (1.0 + i_sek) / (1.0 + i_eur3) - 1.0
    fama_pred_chg = (0.002 + (-0.85) * fwd_prem) * 100.0
    s_fama = s_sek_eur * (1.0 + fama_pred_chg / 100.0)
    opts, ans, dist = make_mcq(
        f"{s_fama:.4f} SEK/EUR (SEK appreciates, contradicting UIRP)",
        f"{e_s1:.4f} SEK/EUR (SEK depreciates one-for-one with the forward premium)",
        "Assumes $a = 0$ and $b = 1$, which represents the theoretical UIRP null hypothesis rejected by $b = -0.85$.",
        f"{s_sek_eur * (1 + 0.002 + 0.85*fwd_prem):.4f} SEK/EUR",
        "Uses $+0.85$ instead of $-0.85$ as the slope on the forward premium.",
        ans_cycle(92),
    )
    add_l2(
        out, "L2-ECN-V03-Q3", SUBJECT, mod3, "Economics", sub3, vid3, vid3, vtitle3, vtext3,
        "Interpret empirical tests of the forward rate as an unbiased predictor of future spot rates",
        "Using Lindqvist's Fama regression estimates ($a = 0.002, b = -0.85$) and the CIP-implied forward premium on EUR, what 1-year `SEK/EUR` spot rate is forecasted?",
        opts, ans,
        f"CIP forward premium on EUR is $(F_t - S_t)/S_t = 1.045/1.030 - 1 = {fwd_prem*100:.4f}\\%$. Plugging into the Fama equation gives $\\%\\Delta S_{{t+1}} = 0.002 - 0.85({fwd_prem:.6f}) = {fama_pred_chg:.2f}\\%$, predicting `SEK/EUR` $= {s_sek_eur:.4f}(1 {fama_pred_chg/100:+.6f}) = {s_fama:.4f}$ (high-yield SEK strengthens rather than weakens).",
        dist,
    )
    calc_ids.add("L2-ECN-V03-Q3")

    # Q4: Currency-hedged SEK investment return (comparing CIP vs UIRP)
    r_hedged = ((1.0 + i_sek) * (s_sek_eur / e_s1) - 1.0) * 100.0
    opts, ans, dist = make_mcq(
        f"{r_hedged:.2f}% (exactly equal to the domestic EUR risk-free rate)",
        f"{i_sek*100:.2f}% (preserving the higher Swedish yield risk-free)",
        "Ignores the forward hedge cost $(S_0/F_0)$ required to lock in SEK proceeds back into EUR.",
        f"{r_eur_unhedged:.2f}% (equal to the unhedged realized return)",
        "A forward hedge locks in $F_0$ at inception, making the return invariant to the realized future spot rate.",
        ans_cycle(93),
    )
    add_l2(
        out, "L2-ECN-V03-Q4", SUBJECT, mod3, "Economics", sub3, vid3, vid3, vtitle3, vtext3,
        "Contrast covered interest rate parity with uncovered interest rate parity",
        "If Lindqvist invests in 1-year risk-free SEK deposits while fully hedging the currency exposure using a 1-year forward contract at CIP parity, the guaranteed EUR-denominated return is:",
        opts, ans,
        f"By Covered Interest Parity, $F_{{\\text{{SEK/EUR}}}} = {e_s1:.4f}$, so selling the SEK principal plus interest forward converts back into $(1.0450) \\times ({s_sek_eur:.4f}/{e_s1:.4f}) - 1 = {r_hedged:.2f}\\%$, identical to the EUR rate.",
        dist,
    )
    calc_ids.add("L2-ECN-V03-Q4")

    # Q5: Conceptual - why UIRP fails empirically over short horizons
    opts, ans, dist = make_mcq(
        "UIRP relies on risk neutrality and zero FX risk premium, whereas in reality investors demand a time-varying risk premium and capital chases higher yields.",
        "UIRP is mathematically enforceable via riskless spot-forward arbitrage just like CIP.",
        "CIP is enforced by riskless arbitrage; UIRP involves uncertain future spot rates and cannot be risklessly arbitraged.",
        "Central banks automatically fix exchange rates whenever interest differentials exceed 100 bps.",
        "Floating G10 currencies such as SEK/EUR are not pegged at 100 bps differentials.",
        ans_cycle(94),
    )
    add_l2(
        out, "L2-ECN-V03-Q5", SUBJECT, mod3, "Economics", sub3, vid3, vid3, vtitle3, vtext3,
        "Explain why uncovered interest parity tends to fail over short and medium horizons",
        "Which explanation best accounts for the empirical finding $b < 1$ (and often $b < 0$) in short-horizon tests of UIRP?",
        opts, ans,
        "Unlike CIP, UIRP is not an arbitrage identity. Because investors are risk-averse and central banks respond gradually to inflation, capital inflows often strengthen high-yielding currencies over short-to-medium horizons before eventual reversion.",
        dist,
    )

    # =========================================================================
    # V04: Relative PPP & International Fisher Effect
    # =========================================================================
    vid4 = "ECN-V04"
    vtitle4 = "Solstice Macro: Relative PPP and the International Fisher Effect"
    # CHF/USD spot = 0.8950 (CHF per 1 USD).
    # Basket cost: CHF 85 in Zurich, USD 100 in Chicago -> Absolute PPP = 0.8500 CHF/USD!
    # Expected 3-year annualized inflation: Switzerland 1.20%, US 3.20%
    # Nominal 3-yr annual yield: US 4.60%, Switzerland? If real interest rate parity holds (exact): (1+i_CHF)/(1+pi_CHF) = (1+i_USD)/(1+pi_USD)
    s_chf_usd = 0.8950
    ppp_abs = 85.0 / 100.0
    pi_chf, pi_usd = 0.012, 0.032
    i_usd4 = 0.046
    vtext4 = (
        "Solstice Global Macro is evaluating long-term currency valuation between the Swiss franc (CHF) and US dollar (USD). "
        "Current spot `CHF/USD` (CHF per 1 USD) is 0.8950. A standardized tradable consumption basket costs CHF 85.00 in Zurich "
        "and USD 100.00 in Chicago. Consensus forecasts annual inflation over the next three years at 1.20% in Switzerland "
        "and 3.20% in the United States. Currently, 3-year annualized US Treasury yields are 4.60%."
    )
    mod4, sub4 = "Module 1", "Purchasing Power Parity and International Fisher Effect"

    # Q1: Absolute PPP & over/undervaluation of USD vs CHF
    usd_overval = (s_chf_usd / ppp_abs - 1.0) * 100.0
    w1_over = (ppp_abs / s_chf_usd - 1.0) * 100.0
    opts, ans, dist = make_mcq(
        f"PPP implied rate = {ppp_abs:.4f} CHF/USD; USD is {usd_overval:.2f}% overvalued vs CHF.",
        f"PPP implied rate = {ppp_abs:.4f} CHF/USD; USD is {abs(w1_over):.2f}% undervalued vs CHF.",
        "Compares $(S_{{\\text{PPP}}}/S_0 - 1)$ instead of $(S_0/S_{{\\text{PPP}}} - 1)$ and misidentifies the overvalued base currency.",
        f"PPP implied rate = {1/ppp_abs:.4f} CHF/USD; USD is 24.0% undervalued vs CHF.",
        "Inverts the basket cost ratio into `USD/CHF` while labeling it `CHF/USD`.",
        ans_cycle(95),
    )
    add_l2(
        out, "L2-ECN-V04-Q1", SUBJECT, mod4, "Economics", sub4, vid4, vid4, vtitle4, vtext4,
        "Calculate absolute PPP exchange rates and currency over/undervaluation",
        "Based on the consumption basket, what is the absolute PPP implied `CHF/USD` rate and the current valuation of USD relative to CHF?",
        opts, ans,
        f"Absolute PPP implies $S_{{\\text{{PPP}}}} = P_{{\\text{{CHF}}}} / P_{{\\text{{USD}}}} = 85.00 / 100.00 = {ppp_abs:.4f}$ CHF/USD. Since spot ({s_chf_usd:.4f}) exceeds {ppp_abs:.4f}, the USD buys more CHF than parity predicts and is overvalued by $({s_chf_usd:.4f}/{ppp_abs:.4f}) - 1 = {usd_overval:.2f}\\%$.",
        dist,
    )
    calc_ids.add("L2-ECN-V04-Q1")

    # Q2: Relative PPP 3-year expected spot rate
    s_3yr_rppp = s_chf_usd * ((1.0 + pi_chf) / (1.0 + pi_usd)) ** 3
    s_1yr_rppp = s_chf_usd * ((1.0 + pi_chf) / (1.0 + pi_usd))
    w2_rppp = s_chf_usd * ((1.0 + pi_usd) / (1.0 + pi_chf)) ** 3
    opts, ans, dist = make_mcq(
        f"{s_3yr_rppp:.4f} CHF/USD",
        f"{s_1yr_rppp:.4f} CHF/USD",
        "Projects only 1 year of inflation differentials rather than compounding over the 3-year horizon.",
        f"{w2_rppp:.4f} CHF/USD",
        "Reverses the inflation ratio, causing the higher-inflation currency (USD) to appreciate under PPP.",
        ans_cycle(96),
    )
    add_l2(
        out, "L2-ECN-V04-Q2", SUBJECT, mod4, "Economics", sub4, vid4, vid4, vtitle4, vtext4,
        "Forecast exchange rates using compounded relative Purchasing Power Parity",
        "Starting from current spot (`CHF/USD` = 0.8950), what `CHF/USD` spot rate does exact compounded relative PPP predict at the end of Year 3?",
        opts, ans,
        f"Relative PPP compounds inflation differentials: $E(S_3) = {s_chf_usd:.4f} \\times \\left(\\frac{{1 + {pi_chf:.3f}}}{{1 + {pi_usd:.3f}}}\\right)^3 = {s_chf_usd:.4f} \\times ({(1+pi_chf)/(1+pi_usd):.6f})^3 = {s_3yr_rppp:.4f}$ CHF/USD.",
        dist,
    )
    calc_ids.add("L2-ECN-V04-Q2")

    # Q3: Real interest rate parity & International Fisher Effect implied Swiss 3-yr nominal yield
    real_usd4 = (1.0 + i_usd4) / (1.0 + pi_usd) - 1.0
    i_chf_ife = (1.0 + real_usd4) * (1.0 + pi_chf) - 1.0
    w1_ichf = i_usd4 + (pi_usd - pi_chf)
    w2_ichf = real_usd4
    opts, ans, dist = make_mcq(
        f"{i_chf_ife*100:.2f}%",
        f"{w1_ichf*100:.2f}%",
        "Adds the inflation differential to the US nominal yield instead of subtracting it.",
        f"{w2_ichf*100:.2f}%",
        "Reports the real interest rate rather than adding back Swiss expected inflation.",
        ans_cycle(97),
    )
    add_l2(
        out, "L2-ECN-V04-Q3", SUBJECT, mod4, "Economics", sub4, vid4, vid4, vtitle4, vtext4,
        "Apply Real Interest Rate Parity and the International Fisher Effect",
        "Assuming exact Real Interest Rate Parity holds between Switzerland and the United States, what is the implied 3-year annualized Swiss nominal government bond yield?",
        opts, ans,
        f"Exact US real yield is $(1.046/1.032) - 1 = {real_usd4*100:.3f}\\%$. Under real interest rate parity, Swiss real yield equals US real yield, so $i_{{\\text{{CHF}}}} = (1 + {real_usd4:.6f})(1.012) - 1 = {i_chf_ife*100:.2f}\\%$ (IFE nominal difference equals expected inflation difference).",
        dist,
    )
    calc_ids.add("L2-ECN-V04-Q3")

    # Q4: Real exchange rate appreciation if nominal rate hits 0.8700 instead
    s_3yr_alt = 0.8700
    rer_ratio = (s_3yr_alt / s_chf_usd) * ((1.0 + pi_usd) / (1.0 + pi_chf)) ** 3
    rer_chg_4 = (rer_ratio - 1.0) * 100.0
    opts, ans, dist = make_mcq(
        f"USD appreciates in real terms by {rer_chg_4:+.2f}% vs CHF.",
        f"USD depreciates in real terms by {(s_3yr_alt/s_chf_usd - 1)*100:.2f}% vs CHF.",
        "Reports only the nominal spot decline of USD without adjusting for higher US cumulative inflation.",
        f"USD real exchange rate remains unchanged (0.00%) because relative PPP held exactly.",
        "Relative PPP predicted 0.8440, not 0.8700; since USD declined less nominally than the inflation gap, USD appreciated in real terms.",
        ans_cycle(98),
    )
    add_l2(
        out, "L2-ECN-V04-Q4", SUBJECT, mod4, "Economics", sub4, vid4, vid4, vtitle4, vtext4,
        "Calculate changes in the real exchange rate over multi-year horizons",
        f"If nominal `CHF/USD` instead finishes Year 3 at {s_3yr_alt:.4f} while inflation occurs at forecast rates, how does the real `CHF/USD` exchange rate change over the three years?",
        opts, ans,
        f"Real `CHF/USD` ratio $= \\frac{{{s_3yr_alt:.4f}}}{{{s_chf_usd:.4f}}} \\times \\left(\\frac{{1.032}}{{1.012}}\\right)^3 = {rer_ratio:.4f}$, meaning the USD experienced a cumulative real appreciation of {rer_chg_4:+.2f}% (CHF became cheaper in real terms).",
        dist,
    )
    calc_ids.add("L2-ECN-V04-Q4")

    # Q5: Conceptual - why absolute PPP fails in practice
    opts, ans, dist = make_mcq(
        "Trade barriers, transportation costs, non-tradable local services, and differing consumption basket weights across countries.",
        "Identical monetary policy targets across all G10 central banks.",
        "Even identical inflation targets do not eliminate shipping costs, tariffs, or non-tradable service price gaps.",
        "Perfect frictionless arbitrage of haircuts and residential real estate across oceans.",
        "Services like haircuts and real estate are prime examples of non-tradables that cannot be arbitraged across borders.",
        ans_cycle(99),
    )
    add_l2(
        out, "L2-ECN-V04-Q5", SUBJECT, mod4, "Economics", sub4, vid4, vid4, vtitle4, vtext4,
        "Explain structural reasons why absolute and relative PPP fail in the short run",
        "Which factor primarily explains why real exchange rates routinely deviate from absolute PPP over short and medium horizons?",
        opts, ans,
        "Non-tradable goods/services (Balassa-Samuelson effect), tariffs, transport expenses, and heterogeneous CPI weights prevent instantaneous cross-border price equalization.",
        dist,
    )

    # =========================================================================
    # V05: FX Carry Trade Return & Crashes
    # =========================================================================
    vid5 = "ECN-V05"
    vtitle5 = "Pacific Alpha Partners: FX Carry Trade Return and Crash Risk"
    # Funding: JPY at 0.50% (1-yr) -> borrow JPY 1,500,000,000 (USD 10M equiv at JPY/USD 150)
    # Target: MXN at 9.50% (1-yr).
    # Spot MXN/JPY? Or let's use JPY/MXN = 8.4000 (JPY per 1 MXN).
    # If Yen funded carry trade: borrow JPY 840,000,000 at 0.50%, convert to MXN 100,000,000 at JPY/MXN = 8.4000, invest at 9.50%.
    jpy_bor = 840_000_000.0
    s0_jm = 8.4000  # JPY per 1 MXN
    i_jpy, i_mxn = 0.0050, 0.0950
    # Scenario A (Normal year): Spot JPY/MXN falls slightly to 8.2000
    s1_norm = 8.2000
    # Scenario B (Risk-off crash): Spot JPY/MXN drops 16% to 7.0560
    s1_crash = 8.4000 * 0.84  # 7.0560
    vtext5 = (
        "Pacific Alpha Partners executes a leveraged 1-year FX carry trade funded in Japanese yen (JPY) and deployed into "
        "Mexican peso (MXN) sovereign bills. At trade inception, spot `JPY/MXN` is 8.4000 (JPY per 1 MXN). "
        "One-year borrowing/investment interest rates are 0.50% in JPY and 9.50% in MXN. "
        "The desk borrows JPY 840,000,000 unhedged for one year and converts the proceeds into MXN 100,000,000. "
        "Historical backtests of the fund's G10/EM carry index indicate an annualized mean excess return of 5.2%, "
        "annualized volatility of 8.0%, and return skewness of -1.85."
    )
    mod5, sub5 = "Module 1", "FX Carry Trade Strategies"

    # Q1: Normal-year return in JPY terms and profit
    mxn_end = 100_000_000.0 * (1.0 + i_mxn)
    jpy_end_norm = mxn_end * s1_norm
    jpy_repay = jpy_bor * (1.0 + i_jpy)
    jpy_prof_norm = jpy_end_norm - jpy_repay
    ret_jpy_norm = (jpy_prof_norm / jpy_bor) * 100.0
    w1_ret_norm = ((1 + i_mxn) * (s0_jm / s1_norm) - (1 + i_jpy)) * 100.0
    opts, ans, dist = make_mcq(
        f"{ret_jpy_norm:+.2f}% (net profit of JPY {jpy_prof_norm:,.0f})",
        f"{w1_ret_norm:+.2f}% (net profit of JPY {jpy_bor*(w1_ret_norm/100):,.0f})",
        "Multiplies by $S_0 / S_1$ instead of $S_1 / S_0$ when converting MXN proceeds back into JPY under `JPY/MXN` quotes.",
        f"{(i_mxn - i_jpy)*100:+.2f}% (net profit of JPY {jpy_bor*(i_mxn-i_jpy):,.0f})",
        "Computes only the interest differential while ignoring the 2.38% depreciation of MXN against JPY.",
        ans_cycle(100),
    )
    add_l2(
        out, "L2-ECN-V05-Q1", SUBJECT, mod5, "Economics", sub5, vid5, vid5, vtitle5, vtext5,
        "Calculate FX carry trade returns and profits in funding currency",
        f"If spot `JPY/MXN` finishes the year at {s1_norm:.4f}, the carry trade's exact 1-year return (as a percentage of borrowed JPY notional) and net JPY profit are closest to:",
        opts, ans,
        f"MXN investment grows to MXN {mxn_end:,.0f}. Converted at {s1_norm:.4f} JPY/MXN, this yields JPY {jpy_end_norm:,.0f}. Subtracting JPY loan repayment of ${jpy_bor:,.0f}(1.005) = \\text{{JPY }} {jpy_repay:,.0f}$ leaves JPY {jpy_prof_norm:,.0f}, or ${jpy_prof_norm:,.0f}/{jpy_bor:,.0f} = {ret_jpy_norm:+.2f}\\%$.",
        dist,
    )
    calc_ids.add("L2-ECN-V05-Q1")

    # Q2: Breakeven ending JPY/MXN exchange rate
    s_be = s0_jm * (1.0 + i_jpy) / (1.0 + i_mxn)
    dep_be = (s_be / s0_jm - 1.0) * 100.0
    w1_sbe = s0_jm * (1.0 + i_mxn) / (1.0 + i_jpy)
    opts, ans, dist = make_mcq(
        f"{s_be:.4f} JPY/MXN (a {abs(dep_be):.2f}% depreciation of MXN)",
        f"{w1_sbe:.4f} JPY/MXN (a {(w1_sbe/s0_jm - 1)*100:.2f}% appreciation of MXN)",
        "Inverts the rate ratio, implying MXN must appreciate for the carry trade to break even.",
        f"{s0_jm * (1 - (i_mxn - i_jpy)):.4f} JPY/MXN (an exact 9.00% drop)",
        "Uses the linear interest spread rather than the exact ratio $(1+i_{\\text{JPY}})/(1+i_{\\text{MXN}})$.",
        ans_cycle(101),
    )
    add_l2(
        out, "L2-ECN-V05-Q2", SUBJECT, mod5, "Economics", sub5, vid5, vid5, vtitle5, vtext5,
        "Calculate the break-even exchange rate for an FX carry trade",
        "At what ending `JPY/MXN` spot rate does the carry trade break even (zero net JPY profit)?",
        opts, ans,
        f"Setting proceeds equal to repayment: $\\text{{MXN }}100\\text{{M}}(1.095) \\times S_1 = \\text{{JPY }}840\\text{{M}}(1.005) \\implies S_{{\\text{{BE}}}} = {s0_jm:.4f} \\times \\frac{{1.005}}{{1.095}} = {s_be:.4f}$ JPY/MXN, an MXN depreciation of {abs(dep_be):.2f}%.",
        dist,
    )
    calc_ids.add("L2-ECN-V05-Q2")

    # Q3: Risk-off crash loss calculation
    jpy_end_crash = mxn_end * s1_crash
    jpy_prof_crash = jpy_end_crash - jpy_repay
    ret_crash = (jpy_prof_crash / jpy_bor) * 100.0
    opts, ans, dist = make_mcq(
        f"{ret_crash:.2f}% (a loss of JPY {abs(jpy_prof_crash):,.0f})",
        f"{-16.00:.2f}% (a loss of JPY {0.16*jpy_bor:,.0f})",
        "Reports only the 16% spot drop without accounting for the +9.50% MXN interest cushion and -0.50% funding cost.",
        f"{(i_mxn - i_jpy - 16.0/100)*100:.2f}%",
        "Uses simple addition of carry spread and spot drop instead of exact multiplicative FX conversion $(1+i_{\\text{MXN}})(0.84) - (1+i_{\\text{JPY}})$.",
        ans_cycle(102),
    )
    add_l2(
        out, "L2-ECN-V05-Q3", SUBJECT, mod5, "Economics", sub5, vid5, vid5, vtitle5, vtext5,
        "Evaluate carry trade crash losses during risk-off unwinds",
        f"During a sudden global liquidity shock, MXN plunges 16.0% against JPY so that `JPY/MXN` ends the year at {s1_crash:.4f}. The carry trade's exact 1-year return and JPY loss are closest to:",
        opts, ans,
        f"Proceeds convert to ${mxn_end:,.0f} \\times {s1_crash:.4f} = \\text{{JPY }} {jpy_end_crash:,.0f}$. Subtracting repayment of JPY {jpy_repay:,.0f} produces a net loss of JPY {abs(jpy_prof_crash):,.0f}, or {ret_crash:.2f}% of notional.",
        dist,
    )
    calc_ids.add("L2-ECN-V05-Q3")

    # Q4: Sharpe ratio and fat-tail interpretation
    sharpe5 = 5.2 / 8.0
    opts, ans, dist = make_mcq(
        f"Sharpe ratio = {sharpe5:.2f}; negative skewness ({-1.85:.2f}) indicates frequent small gains punctuated by occasional severe crash losses.",
        f"Sharpe ratio = {sharpe5:.2f}; negative skewness ({-1.85:.2f}) indicates occasional windfall gains and capped downside.",
        "Reverses the meaning of negative skewness; positive skewness represents windfall right-tail gains.",
        f"Sharpe ratio = {8.0/5.2:.2f}; negative skewness confirms returns are normally distributed.",
        "Inverts the Sharpe ratio ($\\sigma / E(R)$) and claims skewed returns are normal.",
        ans_cycle(103),
    )
    add_l2(
        out, "L2-ECN-V05-Q4", SUBJECT, mod5, "Economics", sub5, vid5, vid5, vtitle5, vtext5,
        "Assess risk-adjusted performance and return skewness of FX carry trades",
        "Based on the backtest statistics, what is the carry index's Sharpe ratio, and what does the reported skewness imply for risk management?",
        opts, ans,
        f"Sharpe ratio $= 5.2\\% / 8.0\\% = {sharpe5:.2f}$. Negative skewness (-1.85) reflects asymmetric crash risk: steady carry accrual is vulnerable to violent crowding unwinds when volatility spikes.",
        dist,
    )
    calc_ids.add("L2-ECN-V05-Q4")

    # Q5: Conceptual - Volatility filter & risk mitigation
    opts, ans, dist = make_mcq(
        "Dynamic volatility-filtering (scaling down leverage when implied FX volatility surges) and combining carry with momentum/value signals.",
        "Increasing leverage systematically whenever implied volatility spikes to capture wider yields.",
        "Adding leverage during volatility spikes amplifies crash drawdowns as leveraged participants rush to unwind funding shorts.",
        "Selling deep out-of-the-money MXN puts to earn additional premium during crises.",
        "Shorting high-yield currency puts adds extra negative convexity precisely when carry crashes occur.",
        ans_cycle(104),
    )
    add_l2(
        out, "L2-ECN-V05-Q5", SUBJECT, mod5, "Economics", sub5, vid5, vid5, vtitle5, vtext5,
        "Evaluate risk-management overlays for FX carry strategies",
        "Which portfolio construction overlay most effectively mitigates the negative tail risk of Pacific Alpha's carry strategy?",
        opts, ans,
        "Carry trades perform best in low-volatility environments; trimming exposure when FX volatility spikes and diversifying across trend/value signals mitigates sudden funding-squeeze crashes.",
        dist,
    )


def build_l2_v06_to_v10(out: list, calc_ids: set):
    """Level 2 Vignettes V06 to V10 (25 Questions)."""
    # =========================================================================
    # V06: Mundell-Fleming Fiscal/Monetary Mix under Fixed vs Floating FX
    # =========================================================================
    vid6 = "ECN-V06"
    vtitle6 = "Aethelgard Central Bank: Mundell-Fleming Policy Mix and Exchange Regimes"
    # IS-LM-BP small open economy example for exact numerical rigor alongside conceptual checks!
    # Suppose Country A (floating FX, high capital mobility) has open-economy multiplier under fixed interest rate?
    # Wait: let's provide clean macro parameters:
    # Domestic IS: Y = 400 + 0.6(Y - 0.2Y) - 1000 r + NX(e), where at world r* = 4% (0.04):
    # Let's check: Y - 0.48Y = 400 - 40 + NX -> 0.52Y = 360 + NX. Wait: let's make numbers super clean!
    # Suppose small open economy with perfect capital mobility (r = r* = 4%):
    # C = 150 + 0.75(Y - T), T = 0.20Y, I = 200 - 1500r, G = 250, NX = 120 - 0.10Y + 50 E (E = domestic/foreign FX).
    # Wait: under perfect capital mobility, Y* satisfies LM: M/P = 0.5Y - 2500r! Let's check!
    # If M/P = 400 and r = r* = 0.04 -> 0.5Y - 100 = 400 -> 0.5Y = 500 -> Y = 1000!
    # Look how transparent and awesome that is! Let's verify:
    # LM: M/P = 0.5Y - 2500r. With M/P = 400 and world rate r* = 0.04:
    # 400 = 0.5Y - 2500(0.04) = 0.5Y - 100 -> 0.5Y = 500 -> Y = 1000!
    # Now suppose fiscal expansion raises G from 250 to 310 (+60) under FLOATING FX and perfect capital mobility:
    # Because M/P is fixed at 400 and r must equal r* = 0.04, LM forces Y = 1000! So fiscal expansion causes currency appreciation that crowds out NX by EXACTLY 60!
    # Whereas if monetary expansion raises M/P from 400 to 450 (+50): 450 = 0.5Y - 100 -> 0.5Y = 550 -> Y = 1100 (+100)!
    # And under FIXED FX, if G rises by +60 and central bank defends peg, central bank must expand M/P to keep r = r*! Let's compute new IS output at E_fixed!
    # Check IS with G = 250, E = 1.0:
    # Y = 150 + 0.75(0.8Y) + 200 - 1500(0.04) + 250 + 120 - 0.10Y + 50(1.0)
    #   = 150 + 0.60Y + 200 - 60 + 250 + 120 - 0.10Y + 50 = 710 + 0.50Y -> 0.50Y = 710 -> Wait: 0.50Y = 710 -> Y = 1420! Adjust constant C0 = 150 -> let's make total autonomous = 500 so 0.5Y = 500 -> Y = 1000!
    # Let's check: C = 100 + 0.75(0.8Y), I = 150 - 1500r, G = 200, NX = 60 - 0.10Y + 50E -> at r=0.04, E=1.0:
    # Autonomous = 100 + (150 - 60) + 200 + 60 + 50 = 500!
    # Slope in Y = 0.60Y - 0.10Y = 0.50Y!
    # So Y = 500 + 0.50Y -> 0.50Y = 500 -> Y = 1000! Exact match!
    # Now if G rises from 200 to 260 (+60) under FIXED FX (E=1.0):
    # Autonomous rises to 560 -> Y = 560 / 0.50 = 1120! And to keep r=0.04 at Y=1120, central bank accommodates M/P to 0.5(1120) - 100 = 460!
    # And under FLOATING FX (M/P fixed at 400): Y stays 1000, so E appreciates by Delta E: 50 * Delta E = -60 -> Delta E = -1.20? Wait: E = 1.0 -> -0.20 if coefficient is 300! Let's make NX = 60 - 0.10Y + 200(E - 1.0) or + 200E - 150 (at E=1, 200-150 = +50 -> Wait: 60 - 150 + 200E -> let's set NX = 60 - 0.10Y + 300(E - 1) + 50 = 110 - 0.10Y + 300(E - 1)). Then at E=1.0, NX = 110 - 100 = +10. Wait: 100 + 90 + 200 + 10 (wait: 100 + 90 + 200 + 110 = 500!). So:
    # C = 100 + 0.75(Y - 0.2Y)
    # I = 150 - 1500 r
    # G = 200
    # NX = 110 - 0.10 Y + 300 (E - 1.0), where E is domestic per foreign FX (higher E = domestic depreciation).
    # Let's verify in Python!
    y0_mf = (100 + (150 - 1500 * 0.04) + 200 + 110) / (1 - 0.75 * 0.8 + 0.10)  # 500 / 0.50 = 1000!
    mp0_mf = 0.5 * y0_mf - 2500 * 0.04  # 400!
    # With G = 260 under floating FX, Y = 1000 so 300(E - 1) = -60 -> E = 0.80 (domestic appreciates by 20%!)
    # Wait: let's check G = 230 (+30): 300(E - 1) = -30 -> E = 0.90 (10% appreciation!). Even more realistic!
    # Under fixed FX (E = 1.0), G = 230 -> Y_fixed = 530 / 0.50 = 1060, and M/P accommodates to 0.5(1060) - 100 = 430!
    dg_mf = 30.0
    y_fixed_new = (500 + dg_mf) / 0.50  # 1060
    mp_fixed_new = 0.5 * y_fixed_new - 2500 * 0.04  # 430
    e_float_new = 1.0 - dg_mf / 300.0  # 0.90
    # Under floating FX, if M/P expands from 400 to 440 (+40): Y_float_m = (440 + 100)/0.5 = 1080!
    # Then from IS: 1080 = (500 + 300(E - 1)) / 0.50 -> 540 = 500 + 300(E - 1) -> 300(E - 1) = 40 -> E = 1.1333!
    dmp_mf = 40.0
    y_float_m = (mp0_mf + dmp_mf + 2500 * 0.04) / 0.50  # 1080
    e_float_m = 1.0 + (0.50 * y_float_m - 500.0) / 300.0  # 1.1333

    vtext6 = (
        "Dr. Elena Rostova advises the Aethelgard Central Bank using a Mundell-Fleming small open-economy model with "
        "perfect capital mobility ($r = r^* = 4.0\\%$ initially) and sticky short-run prices. "
        "Goods-market (IS) and money-market (LM) relationships are:\n"
        "- Consumption: $C = 100 + 0.75(Y - T)$, with proportional tax $T = 0.20Y$\n"
        "- Investment: $I = 150 - 1{,}500r$; Baseline Government Purchases: $G = 200$\n"
        "- Net Exports: $NX = 110 - 0.10Y + 300(E - 1.00)$, where $E$ is the exchange rate in domestic currency per 1 unit of foreign currency (initially $E_0 = 1.00$)\n"
        "- Real Money Demand/Supply (LM): $M/P = 0.50Y - 2{,}500r$, initially $M/P = 400$ and $Y_0 = 1{,}000$."
    )
    mod6, sub6 = "Module 2", "Mundell-Fleming Model and Policy Mix"

    # Q1: Fiscal expansion (+30 G) under Fixed FX
    opts, ans, dist = make_mcq(
        f"$Y = {y_fixed_new:,.0f}$, requiring the central bank to expand $M/P$ to {mp_fixed_new:.0f}.",
        f"$Y = {y0_mf:,.0f}$, because higher interest rates completely crowd out net exports.",
        "Applies the floating-FX full crowding-out outcome to a fixed-exchange-rate regime.",
        f"$Y = {y0_mf + dg_mf / (1 - 0.75*0.8):.0f}$, ignoring import leakage ($0.10Y$) in the open-economy multiplier.",
        "Uses the closed-economy multiplier $1/[1 - 0.75(0.8)] = 2.5$ instead of the open-economy multiplier $1/[1 - 0.75(0.8) + 0.10] = 2.0$.",
        ans_cycle(105),
    )
    add_l2(
        out, "L2-ECN-V06-Q1", SUBJECT, mod6, "Economics", sub6, vid6, vid6, vtitle6, vtext6,
        "Calculate open-economy fiscal policy output effects under fixed exchange rates",
        "Suppose Aethelgard maintains a FIXED exchange rate at $E = 1.00$ and raises government spending from $G = 200$ to $G = 230$. In the new short-run Mundell-Fleming equilibrium, real output $Y$ and central bank money supply $M/P$ become:",
        opts, ans,
        f"With $E=1.00$ and $r=0.04$, open-economy multiplier is $1/[1 - 0.75(0.8) + 0.10] = 1/0.50 = 2.0$. Output increases by $2.0 \\times 30 = 60$ to $Y = {y_fixed_new:,.0f}$. To prevent currency appreciation above the peg, the central bank buys foreign FX, expanding $M/P$ to $0.50({y_fixed_new:,.0f}) - 2{{,}}500(0.04) = {mp_fixed_new:.0f}$.",
        dist,
    )
    calc_ids.add("L2-ECN-V06-Q1")

    # Q2: Fiscal expansion (+30 G) under Floating FX
    app_pct = (1.0 - e_float_new) * 100.0
    opts, ans, dist = make_mcq(
        f"$Y = {y0_mf:,.0f}$ (unchanged) and $E = {e_float_new:.2f}$ (domestic currency appreciates by {app_pct:.0f}%).",
        f"$Y = {y_fixed_new:,.0f}$ and $E = 1.10$ (domestic currency depreciates by 10%).",
        "Reverses both output and FX direction—under floating FX with perfect capital mobility, fiscal stimulus appreciates the currency and crowds out net exports completely.",
        f"$Y = {y0_mf + dg_mf:,.0f}$ and $E = 1.00$ (balanced-budget expansion).",
        "Assumes output rises dollar-for-dollar with $G$ while keeping the exchange rate unchanged.",
        ans_cycle(106),
    )
    add_l2(
        out, "L2-ECN-V06-Q2", SUBJECT, mod6, "Economics", sub6, vid6, vid6, vtitle6, vtext6,
        "Calculate exchange rate and crowding-out effects of fiscal policy under floating FX",
        "If Aethelgard instead operates a FLOATING exchange rate with unchanged money supply ($M/P = 400$) and raises $G$ from 200 to 230, what happens to equilibrium $Y$ and $E$?",
        opts, ans,
        f"With $M/P = 400$ and $r = r^* = 0.04$, the LM curve pins output at $Y = {y0_mf:,.0f}$. Upward interest pressure draws foreign capital inflows, appreciating domestic currency ($E$ falls) until $\\Delta NX = 300(E - 1) = -30 \\implies E = {e_float_new:.2f}$ (a {app_pct:.0f}% domestic currency appreciation).",
        dist,
    )
    calc_ids.add("L2-ECN-V06-Q2")

    # Q3: Monetary expansion (+40 M/P) under Floating FX
    dep_pct_m = (e_float_m - 1.0) * 100.0
    opts, ans, dist = make_mcq(
        f"$Y = {y_float_m:,.0f}$ and $E = {e_float_m:.4f}$ (domestic currency depreciates by {dep_pct_m:.2f}%).",
        f"$Y = {y0_mf:,.0f}$ and $E = {1 - (e_float_m - 1):.4f}$ (domestic currency appreciates).",
        "Conflates monetary expansion under floating FX with fixed-FX reserve loss; here monetary easing expands output via currency depreciation.",
        f"$Y = {y_float_m:,.0f}$ and $E = 1.00$ (exchange rate invariant to money supply).",
        "Ignores that higher output requires stronger net exports via currency depreciation when $r$ remains tied to $r^*$.",
        ans_cycle(107),
    )
    add_l2(
        out, "L2-ECN-V06-Q3", SUBJECT, mod6, "Economics", sub6, vid6, vid6, vtitle6, vtext6,
        "Calculate output and exchange rate effects of monetary policy under floating FX",
        "Returning to baseline ($G = 200$) under a FLOATING exchange rate, the central bank increases real money supply from $M/P = 400$ to $M/P = 440$. New equilibrium $Y$ and $E$ are closest to:",
        opts, ans,
        f"From LM at $r = 0.04$: $440 = 0.50Y - 100 \\implies Y = {y_float_m:,.0f}$. Substituting into IS: $0.50({y_float_m:,.0f}) = 500 + 300(E - 1) \\implies 300(E - 1) = 40 \\implies E = {e_float_m:.4f}$ ({dep_pct_m:.2f}% domestic depreciation boosting net exports).",
        dist,
    )
    calc_ids.add("L2-ECN-V06-Q3")

    # Q4: Conceptual - Monetary policy impotence under fixed FX + high capital mobility
    opts, ans, dist = make_mcq(
        "Capital outflows force the central bank to sell foreign reserves and contract the domestic money supply back to its starting level.",
        "Domestic interest rates permanently remain below world rates without affecting FX reserves.",
        "With perfect capital mobility, arbitrage eliminates rate differentials instantly, triggering massive reserve outflows under a peg.",
        "Fiscal deficits immediately shrink to zero as foreign reserves decline.",
        "Monetary reserve losses do not automatically eliminate discretionary fiscal deficits.",
        ans_cycle(108),
    )
    add_l2(
        out, "L2-ECN-V06-Q4", SUBJECT, mod6, "Economics", sub6, vid6, vid6, vtitle6, vtext6,
        "Explain why monetary policy loses potency under fixed exchange rates and high capital mobility",
        "Why does an attempted open-market monetary expansion fail to boost real output if Aethelgard maintains a rigid fixed exchange rate with free capital flows?",
        opts, ans,
        "Any downward pressure on domestic interest rates causes rapid capital outflows. To defend the fixed peg, the central bank must sell foreign currency and buy back domestic currency, reversing the initial monetary expansion.",
        dist,
    )

    # Q5: Conceptual - Low capital mobility + fiscal expansion under floating FX
    opts, ans, dist = make_mcq(
        "The domestic currency is likely to DEPRECIATE because trade-deficit deterioration from higher income outweighs modest capital inflows.",
        "The domestic currency appreciates even more strongly than under high capital mobility.",
        "Strong appreciation requires large interest-sensitive capital inflows exceeding import demand; under low capital mobility, import expansion dominates.",
        "Monetary policy becomes completely ineffective even under floating rates.",
        "Under floating FX, monetary expansion lowers domestic rates, boosts investment, and depreciates the currency—remaining effective even with low capital mobility.",
        ans_cycle(109),
    )
    add_l2(
        out, "L2-ECN-V06-Q5", SUBJECT, mod6, "Economics", sub6, vid6, vid6, vtitle6, vtext6,
        "Contrast Mundell-Fleming FX responses under low vs high capital mobility",
        "If Aethelgard imposes strict capital controls (very LOW capital mobility) under a floating exchange rate and then enacts fiscal stimulus, what happens to the domestic currency?",
        opts, ans,
        "When capital mobility is low, higher domestic output raises imports (worsening the current account) while higher domestic interest rates attract minimal foreign capital inflows, shifting net balance-of-payments demand toward domestic currency depreciation.",
        dist,
    )

    # =========================================================================
    # V07: Cobb-Douglas Growth Accounting
    # =========================================================================
    vid7 = "ECN-V07"
    vtitle7 = "Veridian Research: Cobb-Douglas Growth Accounting and Potential GDP"
    # dY/Y = dA/A + alpha*(dK/K) + (1 - alpha)*(dL/L)
    # Country X: alpha = 0.35, dA/A = 1.40%, dK/K = 4.00%, dL/L = 0.80%
    # Country Y (aging): alpha = 0.30, observed dY/Y = 2.60%, dK/K = 3.00%, dL/L = -0.50% -> solve dA/A!
    alpha_x, da_x, dk_x, dl_x = 0.35, 1.40, 4.00, 0.80
    alpha_y, dy_y, dk_y, dl_y = 0.30, 2.60, 3.00, -0.50
    vtext7 = (
        "Veridian Macro Research forecasts 10-year potential GDP growth across two economies using a Cobb-Douglas "
        "production framework, $Y = A K^\\alpha L^{1-\\alpha}$, where growth accounting follows:\n"
        "$$\\frac{\\Delta Y}{Y} = \\frac{\\Delta A}{A} + \\alpha \\frac{\\Delta K}{K} + (1 - \\alpha)\\frac{\\Delta L}{L}$$\n"
        "Inputs for the upcoming decade are:\n"
        "- **Economy X (Emerging Industrial):** Capital share $\\alpha = 0.35$; expected TFP growth $\\Delta A/A = 1.40\\%$; "
        "capital stock growth $\\Delta K/K = 4.00\\%$; labor force growth $\\Delta L/L = 0.80\\%$.\n"
        "- **Economy Y (Mature Aging):** Capital share $\\alpha = 0.30$; observed/projected potential GDP growth $\\Delta Y/Y = 2.60\\%$; "
        "capital stock growth $\\Delta K/K = 3.00\\%$; labor force growth $\\Delta L/L = -0.50\\%$."
    )
    mod7, sub7 = "Module 3", "Economic Growth Accounting"

    # Q1: Economy X potential GDP growth
    dy_x = da_x + alpha_x * dk_x + (1.0 - alpha_x) * dl_x
    w1_dyx = da_x + (1 - alpha_x) * dk_x + alpha_x * dl_x
    w2_dyx = da_x + dk_x + dl_x
    opts, ans, dist = make_mcq(
        f"{dy_x:.2f}%",
        f"{w1_dyx:.2f}%",
        "Swaps the factor income shares by weighting capital with $(1-\\alpha)$ and labor with $\\alpha$.",
        f"{w2_dyx:.2f}%",
        "Sums unweighted growth rates of TFP, capital, and labor.",
        ans_cycle(110),
    )
    add_l2(
        out, "L2-ECN-V07-Q1", SUBJECT, mod7, "Economics", sub7, vid7, vid7, vtitle7, vtext7,
        "Calculate potential GDP growth using the Cobb-Douglas growth accounting equation",
        "Economy X's projected annual potential GDP growth rate is closest to:",
        opts, ans,
        f"$\\Delta Y/Y = {da_x:.2f}\\% + {alpha_x:.2f}({dk_x:.2f}\\%) + (1 - {alpha_x:.2f})({dl_x:.2f}\\%) = {da_x:.2f}\\% + {alpha_x*dk_x:.2f}\\% + {(1-alpha_x)*dl_x:.2f}\\% = {dy_x:.2f}\\%$.",
        dist,
    )
    calc_ids.add("L2-ECN-V07-Q1")

    # Q2: Economy X labor productivity growth and capital deepening contribution
    # d(Y/L)/(Y/L) = dY/Y - dL/L = dA/A + alpha*(dK/K - dL/L)
    cap_deep_x = alpha_x * (dk_x - dl_x)
    lp_x = da_x + cap_deep_x
    w1_lpx = da_x + alpha_x * dk_x
    opts, ans, dist = make_mcq(
        f"Labor productivity growth = {lp_x:.2f}%; capital deepening contribution = {cap_deep_x:.2f}%",
        f"Labor productivity growth = {w1_lpx:.2f}%; capital deepening contribution = {alpha_x*dk_x:.2f}%",
        "Uses gross capital growth $\\alpha(\\Delta K/K)$ rather than capital-per-worker growth $\\alpha(\\Delta K/K - \\Delta L/L)$.",
        f"Labor productivity growth = {dy_x:.2f}%; capital deepening contribution = {dk_x - dl_x:.2f}%",
        "Reports aggregate GDP growth instead of output-per-worker growth and omits the $\\alpha$ weight on capital deepening.",
        ans_cycle(111),
    )
    add_l2(
        out, "L2-ECN-V07-Q2", SUBJECT, mod7, "Economics", sub7, vid7, vid7, vtitle7, vtext7,
        "Decompose labor productivity growth into TFP growth and capital deepening",
        "In Economy X, expected annual labor productivity growth ($\\Delta(Y/L)/(Y/L)$) and the contribution of capital deepening are:",
        opts, ans,
        f"Capital-per-worker grows at $\\Delta K/K - \\Delta L/L = {dk_x:.2f}\\% - {dl_x:.2f}\\% = {dk_x-dl_x:.2f}\\%$, so capital deepening contributes $\\alpha({dk_x-dl_x:.2f}\\%) = {cap_deep_x:.2f}\\%$. Adding TFP growth ({da_x:.2f}%) yields labor productivity growth of {lp_x:.2f}% (matching $\\Delta Y/Y - \\Delta L/L = {dy_x:.2f}\\% - {dl_x:.2f}\\%$).",
        dist,
    )
    calc_ids.add("L2-ECN-V07-Q2")

    # Q3: Solve for implied TFP growth (Solow residual) in Economy Y
    da_y = dy_y - alpha_y * dk_y - (1.0 - alpha_y) * dl_y
    w1_day = dy_y - alpha_y * dk_y + (1.0 - alpha_y) * dl_y
    w2_day = dy_y - (1.0 - alpha_y) * dk_y - alpha_y * dl_y
    opts, ans, dist = make_mcq(
        f"{da_y:.2f}%",
        f"{w1_day:.2f}%",
        "Adds the negative labor growth contribution instead of subtracting it, understating required TFP.",
        f"{w2_day:.2f}%",
        "Applies labor's weight $(1-\\alpha)$ to capital and $\\alpha$ to labor.",
        ans_cycle(112),
    )
    add_l2(
        out, "L2-ECN-V07-Q3", SUBJECT, mod7, "Economics", sub7, vid7, vid7, vtitle7, vtext7,
        "Solve for Total Factor Productivity (TFP) growth as the Solow residual",
        "What annual TFP growth rate ($\\Delta A/A$) is implied for Economy Y to achieve its 2.60% potential GDP growth projection?",
        opts, ans,
        f"Solving for the Solow residual: $\\frac{{\\Delta A}}{{A}} = {dy_y:.2f}\\% - {alpha_y:.2f}({dk_y:.2f}\\%) - (1 - {alpha_y:.2f})({dl_y:.2f}\\%) = {dy_y:.2f}\\% - {alpha_y*dk_y:.2f}\\% - ({(1-alpha_y)*dl_y:.2f}\\%) = {da_y:.2f}\\%$.",
        dist,
    )
    calc_ids.add("L2-ECN-V07-Q3")

    # Q4: Impact of immigration / participation reform raising dL/L in Economy Y from -0.50% to +0.50%
    dl_y_new = 0.50
    dy_y_new = da_y + alpha_y * dk_y + (1.0 - alpha_y) * dl_y_new
    gain_y = dy_y_new - dy_y
    opts, ans, dist = make_mcq(
        f"{dy_y_new:.2f}% (a +{gain_y:.2f} percentage point boost)",
        f"{dy_y + 1.00:.2f}% (a +1.00 percentage point boost)",
        "Assumes a 1.00% increase in labor growth lifts GDP growth by 1.00% instead of weighting by labor's share $(1 - \\alpha) = 0.70$.",
        f"{dy_y + alpha_y * 1.00:.2f}% (a +{alpha_y:.2f} percentage point boost)",
        "Weights the labor force gain by capital's share $\\alpha = 0.30$ instead of labor's share $1 - \\alpha = 0.70$.",
        ans_cycle(113),
    )
    add_l2(
        out, "L2-ECN-V07-Q4", SUBJECT, mod7, "Economics", sub7, vid7, vid7, vtitle7, vtext7,
        "Quantify demographic and labor force policy impacts on potential GDP growth",
        "Suppose Economy Y enacts skilled-immigration and pension reforms that raise $\\Delta L/L$ from -0.50% to +0.50% while leaving TFP and capital growth unchanged. Economy Y's revised potential GDP growth becomes:",
        opts, ans,
        f"A +1.00 percentage point increase in $\\Delta L/L$ adds $(1 - \\alpha)(1.00\\%) = 0.70\\%$ to potential GDP growth, lifting Economy Y from {dy_y:.2f}% to {dy_y_new:.2f}%.",
        dist,
    )
    calc_ids.add("L2-ECN-V07-Q4")

    # Q5: Conceptual - Diminishing marginal productivity of capital vs TFP for sustainable growth
    opts, ans, dist = make_mcq(
        "Capital deepening faces diminishing marginal returns, so only sustained TFP growth ($\\Delta A/A$) can permanently elevate long-run per-capita growth.",
        "Raising the investment-to-GDP ratio perpetually raises steady-state per-capita GDP growth without limit.",
        "In neoclassical growth, higher savings/investment raises the steady-state LEVEL of output per worker but cannot permanently raise the steady-state growth RATE.",
        "Labor's share $(1-\\alpha)$ falls to zero once capital deepening begins.",
        "In Cobb-Douglas production, factor income shares $\\alpha$ and $1-\\alpha$ are constant.",
        ans_cycle(114),
    )
    add_l2(
        out, "L2-ECN-V07-Q5", SUBJECT, mod7, "Economics", sub7, vid7, vid7, vtitle7, vtext7,
        "Explain why sustainable per-capita growth depends on Total Factor Productivity",
        "Why does Veridian Research emphasize Economy Y's TFP trajectory over pure capital accumulation when forecasting long-run living standards?",
        opts, ans,
        "Because $\\alpha < 1$, capital exhibits diminishing marginal returns; as $K/L$ rises, each incremental unit of physical capital yields smaller output gains, leaving technological progress (TFP) as the sole driver of permanent per-capita growth.",
        dist,
    )

    # =========================================================================
    # V08: Solow Steady-State Capital-to-Labor & Convergence
    # =========================================================================
    vid8 = "ECN-V08"
    vtitle8 = "Solow Sovereign Analytics: Steady-State Capital and Convergence"
    # Standard CFA Level 2 Solow steady-state setup:
    # Production per worker: y = A * k^alpha (let alpha = 0.50 for ultra-clean exact powers, or alpha = 1/3 -> 1/(1-alpha) = 1.5!)
    # Wait: alpha = 1/3 -> 1 - alpha = 2/3 -> 1/(1-alpha) = 1.5, alpha/(1-alpha) = 0.5!
    # Or alpha = 0.50 -> 1/(1-alpha) = 2.0, alpha/(1-alpha) = 1.0!
    # Let's check alpha = 0.50 vs alpha = 1/3: alpha = 0.40 -> 1/(1-alpha) = 5/3!
    # Wait: alpha = 0.50 makes mental verification crystal clear while still fully rigorous:
    # Let's test alpha = 0.50 OR alpha = 0.3333? Actually, in Python any alpha (e.g. alpha = 0.35 or 0.40) is computed identically! Let's use alpha = 0.40 (realistic capital share!) so students can't guess trivial squares, and compute everything exactly in Python!
    # Wait: let's check numbers with alpha = 0.40:
    # Economy S: A = 2.0, alpha = 0.40, s = 0.24 (24% savings rate), delta = 0.05 (5% depreciation), n = 0.01 (1% labor growth), theta = 0.018 (1.8% TFP growth).
    # Steady-state labor productivity growth g* = theta / (1 - alpha) = 0.018 / 0.60 = 0.030 (3.0%!)
    # Effective depreciation term = delta + n + theta/(1 - alpha) = 0.05 + 0.01 + 0.03 = 0.09 (9.0%!)
    # Steady-state capital-to-output ratio (K/Y)* = s / (delta + n + theta/(1 - alpha)) = 0.24 / 0.09 = 2.6667!
    # Steady-state capital-to-effective-labor k* = (s * A / (delta + n + theta/(1 - alpha)))^(1/(1-alpha)) = (0.24 * 2.0 / 0.09)^(1/0.60) = (5.3333)^1.6667!
    # Wait: what if theta = 0 for Question 1 (exact steady-state k* and y* in basic Solow with stationary A=2.0), OR we keep theta=0.018 for steady-state growth rate & K/Y, and theta=0 in baseline? Let's be super consistent inside ONE vignette!
    # Let's make Economy S have theta = 0.012 (1.2% TFP growth), alpha = 0.40 -> steady-state per-worker growth = theta/(1-alpha) = 0.012/0.60 = 2.0%!
    # Wait: delta = 0.05, n = 0.01, theta/(1-alpha) = 0.02 -> denominator = 0.08 (8.0%!)
    # s = 0.24 -> K/Y* = 0.24 / 0.08 = 3.00!! WHOA, exact 3.00!
    # And if A_0 = 2.0 (at current period, normalized effective technology A=2.0):
    # k* = ( (s * A) / (delta + n + g) )^(1/(1-alpha)) = ( (0.24 * 2.0) / 0.08 )^(1/0.60) = 6.0^(5/3) = 19.8116!
    # And y* = A * (k*)^alpha = 2.0 * (19.8116)^0.40 = 6.6039! Check K/Y = k*/y* = 19.8116 / 6.6039 = 3.0000! Exact!!
    # Check Golden Rule savings rate: s_GR = alpha = 0.40 (40%)!
    # Check transitional GDP growth when s rises from 0.24 to 0.32 (keeping theta=0.012, n=0.01 -> long-run total GDP growth = n + theta/(1-alpha) = 1.0% + 2.0% = 3.0%! Wait: what is transitional impact? Higher s raises K/Y from 3.0 to 4.0 and boosts transitional growth above 3.0%, converging back to 3.0%!).
    alpha8 = 0.40
    A8 = 2.0
    s8 = 0.24
    delta8 = 0.05
    n8 = 0.01
    theta8 = 0.012
    g_per_worker8 = theta8 / (1.0 - alpha8)  # 0.020 (2.0%)
    g_total_ss8 = n8 + g_per_worker8         # 0.030 (3.0%)
    denom8 = delta8 + n8 + g_per_worker8     # 0.080 (8.0%)
    ky_ss8 = s8 / denom8                     # 3.00
    k_ss8 = ((s8 * A8) / denom8) ** (1.0 / (1.0 - alpha8))
    y_ss8 = A8 * (k_ss8 ** alpha8)

    vtext8 = (
        "Solow Sovereign Analytics models long-run economic convergence for Developing Economy S using the neoclassical "
        "Solow growth framework with aggregate production $Y = A K^\\alpha L^{1-\\alpha}$ (so per-worker output $y = A k^\\alpha$, "
        "where $k = K/L$ and current technology scale $A = 2.00$). Baseline structural parameters for Economy S are:\n"
        "- Capital income share: $\\alpha = 0.40$\n"
        "- National savings rate: $s = 24.0\\%$\n"
        "- Capital depreciation rate: $\\delta = 5.0\\%$\n"
        "- Labor force growth rate: $n = 1.0\\%$\n"
        "- Exogenous TFP growth rate: $\\theta = 1.2\\%$\n"
        "In the neoclassical steady state, the capital-to-output ratio stays constant at $(K/Y)^* = \\frac{s}{\\delta + n + \\theta/(1-\\alpha)}$, "
        "and steady-state capital per worker (at $A = 2.00$) satisfies $k^* = \\left(\\frac{sA}{\\delta + n + \\theta/(1-\\alpha)}\\right)^{1/(1-\\alpha)}$."
    )
    mod8, sub8 = "Module 3", "Neoclassical Solow Growth and Convergence"

    # Q1: Steady-state growth rate of output per worker and aggregate GDP
    opts, ans, dist = make_mcq(
        f"Output per worker growth = {g_per_worker8*100:.1f}%; aggregate GDP growth = {g_total_ss8*100:.1f}%",
        f"Output per worker growth = {theta8*100:.1f}%; aggregate GDP growth = {(n8+theta8)*100:.1f}%",
        "Uses raw TFP growth $\\theta$ instead of the steady-state induced capital-deepening multiplier $\\theta / (1 - \\alpha)$.",
        f"Output per worker growth = {(theta8/alpha8)*100:.1f}%; aggregate GDP growth = {(n8+theta8/alpha8)*100:.1f}%",
        "Divides $\\theta$ by $\\alpha$ instead of $(1 - \\alpha)$.",
        ans_cycle(115),
    )
    add_l2(
        out, "L2-ECN-V08-Q1", SUBJECT, mod8, "Economics", sub8, vid8, vid8, vtitle8, vtext8,
        "Calculate steady-state growth rates of per-worker output and total GDP",
        "In steady-state balanced growth, Economy S's sustainable annual growth rates of output per worker ($Y/L$) and total GDP ($Y$) are:",
        opts, ans,
        f"Because TFP growth induces proportional capital deepening in steady state, per-worker output grows at $g^* = \\frac{{\\theta}}{{1 - \\alpha}} = \\frac{{1.2\\%}}{{1 - 0.40}} = {g_per_worker8*100:.1f}\\%$. Aggregate GDP grows at $g^* + n = {g_per_worker8*100:.1f}\\% + {n8*100:.1f}\\% = {g_total_ss8*100:.1f}\\%$.",
        dist,
    )
    calc_ids.add("L2-ECN-V08-Q1")

    # Q2: Steady-state capital-to-output ratio (K/Y)* and steady-state k*
    w1_kss = ((s8 * A8) / (delta8 + n8)) ** (1.0 / (1.0 - alpha8))
    w2_ky = s8 / (delta8 + n8)
    opts, ans, dist = make_mcq(
        f"$(K/Y)^* = {ky_ss8:.2f}$; $k^* = {k_ss8:.2f}$",
        f"$(K/Y)^* = {w2_ky:.2f}$; $k^* = {w1_kss:.2f}$",
        "Omits the steady-state per-worker growth term $\\theta/(1-\\alpha) = 2.0\\%$ from the capital-widening denominator.",
        f"$(K/Y)^* = {ky_ss8:.2f}$; $k^* = {((s8*A8)/denom8)**(1/alpha8):.2f}$",
        "Raises the inner term to $1/\\alpha$ instead of $1/(1 - \\alpha)$.",
        ans_cycle(116),
    )
    add_l2(
        out, "L2-ECN-V08-Q2", SUBJECT, mod8, "Economics", sub8, vid8, vid8, vtitle8, vtext8,
        "Calculate steady-state capital-to-output ratio and capital per worker",
        "At $A = 2.00$, what are Economy S's steady-state capital-to-output ratio $(K/Y)^*$ and steady-state capital per worker $k^*$?",
        opts, ans,
        f"Capital-widening requirement is $\\delta + n + \\theta/(1-\\alpha) = 5.0\\% + 1.0\\% + 2.0\\% = 8.0\\%$. Thus $(K/Y)^* = 0.24 / 0.08 = {ky_ss8:.2f}$, and $k^* = \\left(\\frac{{0.24 \\times 2.00}}{{0.08}}\\right)^{{1/0.60}} = (6.0)^{{1.6667}} = {k_ss8:.2f}$ (with $y^* = 2.00 \\times {k_ss8:.2f}^{{0.40}} = {y_ss8:.2f}$).",
        dist,
    )
    calc_ids.add("L2-ECN-V08-Q2")

    # Q3: Savings rate hike from 24% to 32% (transitional vs long-run effect)
    s8_new = 0.32
    ky_ss8_new = s8_new / denom8
    k_ss8_new = ((s8_new * A8) / denom8) ** (1.0 / (1.0 - alpha8))
    k_pct_jump = (k_ss8_new / k_ss8 - 1.0) * 100.0
    opts, ans, dist = make_mcq(
        f"$(K/Y)^*$ rises to {ky_ss8_new:.2f}, raising $k^*$ by {k_pct_jump:.1f}% during the transition, while long-run steady-state GDP growth returns to {g_total_ss8*100:.1f}%.",
        f"$(K/Y)^*$ rises to {ky_ss8_new:.2f}, permanently elevating steady-state aggregate GDP growth from {g_total_ss8*100:.1f}% to 4.0%.",
        "Violates the Solow invariance result: saving rates alter the steady-state LEVEL of capital and output, not the permanent steady-state growth rate.",
        f"$(K/Y)^*$ remains unchanged at {ky_ss8:.2f} because depreciation absorbs all extra saving.",
        "Ignores that higher saving increases equilibrium $K/Y$ until higher depreciation matches the higher saving flow.",
        ans_cycle(117),
    )
    add_l2(
        out, "L2-ECN-V08-Q3", SUBJECT, mod8, "Economics", sub8, vid8, vid8, vtitle8, vtext8,
        "Evaluate transitional and long-run effects of a higher savings rate in the Solow model",
        "If structural reforms raise Economy S's national savings rate permanently from 24.0% to 32.0%, the neoclassical Solow model predicts that:",
        opts, ans,
        f"The new steady-state ratio $(K/Y)^* = 0.32 / 0.08 = {ky_ss8_new:.2f}$, lifting $k^*$ by $(32/24)^{{1/0.60}} - 1 = {k_pct_jump:.1f}\\%$. Growth accelerates temporarily during the transition to the higher capital path, then settles back to {g_total_ss8*100:.1f}%.",
        dist,
    )
    calc_ids.add("L2-ECN-V08-Q3")

    # Q4: Golden Rule savings rate & dynamic efficiency
    opts, ans, dist = make_mcq(
        f"40.0% ($s_{{\\text{{GR}}}} = \\alpha$); Economy S currently saves less than the Golden Rule level, so raising savings increases steady-state consumption per worker.",
        f"40.0% ($s_{{\\text{{GR}}}} = \\alpha$); Economy S is dynamically inefficient because its savings rate is below 40.0%.",
        "Dynamic inefficiency (over-saving) only occurs when $s > \\alpha$ (saving ABOVE the Golden Rule rate, depressing consumption).",
        f"60.0% ($s_{{\\text{{GR}}}} = 1 - \\alpha$); Economy S should cut its savings rate to boost consumption.",
        "Confuses labor's share $(1-\\alpha)$ with capital's share $\\alpha$ in the Phelps Golden Rule condition.",
        ans_cycle(118),
    )
    add_l2(
        out, "L2-ECN-V08-Q4", SUBJECT, mod8, "Economics", sub8, vid8, vid8, vtitle8, vtext8,
        "Determine the Golden Rule savings rate that maximizes steady-state consumption",
        "In the Solow model, what savings rate maximizes steady-state consumption per worker (the Golden Rule), and what does it imply for Economy S?",
        opts, ans,
        "Golden Rule steady-state consumption is maximized when the marginal product of capital equals $\\delta + n + g$, which in a Cobb-Douglas economy equals setting $s_{\\text{GR}} = \\alpha = 40.0\\%$. Since $24.0\\% < 40.0\\%$, higher saving boosts long-run steady-state consumption.",
        dist,
    )
    calc_ids.add("L2-ECN-V08-Q4")

    # Q5: Conceptual - Conditional vs Club Convergence & Endogenous Growth (AK)
    opts, ans, dist = make_mcq(
        "Conditional convergence predicts poor economies grow faster only after controlling for savings rates, demographics, and institutional quality; endogenous growth models eliminate diminishing returns to broad capital.",
        "Absolute convergence guarantees all poor nations catch up to rich nations unconditionally regardless of savings or institutions.",
        "Empirical data reject unconditional absolute convergence globally; convergence is conditional on structural fundamentals or restricted to institutional 'clubs'.",
        "Endogenous growth theory ($Y = AK$) predicts rapid convergence of all countries to a zero per-capita growth steady state.",
        "In $Y = AK$, constant returns to broad capital (including R&D/human capital) yield perpetual positive per-capita growth without forced convergence.",
        ans_cycle(119),
    )
    add_l2(
        out, "L2-ECN-V08-Q5", SUBJECT, mod8, "Economics", sub8, vid8, vid8, vtitle8, vtext8,
        "Distinguish absolute, conditional, and club convergence and endogenous growth theory",
        "Which statement accurately contrasts convergence hypotheses with endogenous growth theory?",
        opts, ans,
        "Neoclassical growth predicts conditional convergence (countries converge toward their own steady states defined by $s, n, \\theta$, and institutions), whereas endogenous growth ($Y = AK$) treats knowledge/human capital as non-diminishing, sustaining growth via R&D externalities.",
        dist,
    )

    # =========================================================================
    # V09: Economic Effects of Regulation
    # =========================================================================
    vid9 = "ECN-V09"
    vtitle9 = "Kestrel Financial Oversight: Economics of Regulation"
    # Numerical regulatory scenarios:
    # 1) Optimal abatement / regulatory stringency: MB(x) = 180 - 3x, MC(x) = 20 + 5x -> 8x = 160 -> x* = 20 units! Net benefit = 0.5*(180-20)*20 = 1600!
    # 2) Bank Tier-1 Capital buffer hike from 8% to 12%: ROE drops from 15.0% to what if ROA fixed at 1.20%? Wait: ROE = ROA / (E/A) -> 1.20%/0.08 = 15%, 1.20%/0.12 = 10%! And to preserve 12% target ROE, lending spread must increase by how many bps (assuming tax rate 25% and pre-tax ROA boost)?
    #    Target pre-tax ROA = Target ROE * (E/A) / (1 - tax)!
    #    Old pre-tax ROA = 0.15 * 0.08 / 0.75 = 1.60%. New ROE at 12% capital if pre-tax ROA unchanged = 1.60% * 0.75 / 0.12 = 10.0%.
    #    To hit 12% ROE at 12% equity ratio (25% tax), required pre-tax ROA = 0.12 * 0.12 / 0.75 = 1.92% -> +32 bps lending rate pass-through (ignoring Modigliani-Miller risk offset)!
    # 3) Regulatory Sunset & Deadweight compliance burden NPV: Initial setup cost USD 45M + ongoing USD 12M/yr vs benefit USD 22M/yr over 6 yrs at 6% discount rate (annuity factor)!
    vtext9 = (
        "Kestrel Advisory evaluates the macroeconomic and banking-sector consequences of two proposed regulations:\n"
        "- **Proposal 1 (Emissions & Operational Risk Rule):** Marginal societal benefit of compliance intensity $x$ (in index units) "
        "is $MB(x) = 180 - 3x$ (in USD millions per unit), while marginal regulatory compliance cost is $MC(x) = 20 + 5x$ (USD millions per unit).\n"
        "- **Proposal 2 (Bank Capital Surcharge):** Banking regulators propose raising minimum equity-to-assets from 8.0% to 12.0%. "
        "Currently, banks earn a 1.60% pre-tax return on assets (ROA), face a 25.0% corporate tax rate, and deliver a 15.0% after-tax ROE.\n"
        "- **Proposal 3 (Clearing Mandate):** Requires USD 45 million upfront IT overhaul plus USD 12 million annual audit costs, "
        "yielding USD 22 million in annual fraud-prevention benefits over a fixed 6-year horizon (discount rate = 6.0%) before a sunset review."
    )
    mod9, sub9 = "Module 4", "Economics of Regulation"

    # Q1: Optimal regulatory stringency x* and net social surplus
    x_opt = (180.0 - 20.0) / (3.0 + 5.0)  # 20
    net_surplus9 = 0.5 * (180.0 - 20.0) * x_opt  # 1600
    over_reg_x = (180.0 - 20.0) / 5.0  # 32 (where MB=MC wrong? No, where MC = 180 -> 20+5x = 180)
    opts, ans, dist = make_mcq(
        f"$x^* = {x_opt:.0f}$ units; net social benefit = USD {net_surplus9:,.0f} million",
        f"$x^* = {over_reg_x:.0f}$ units; net social benefit = USD {net_surplus9:,.0f} million",
        "Sets $MC(x)$ equal to maximum $MB(0) = 180$ instead of equating marginal benefit and marginal cost at $x^*$.",
        f"$x^* = {x_opt:.0f}$ units; net social benefit = USD {2*net_surplus9:,.0f} million",
        "Omits the $1/2$ triangle area factor when integrating $(MB - MC)$ from $0$ to $x^*$.",
        ans_cycle(120),
    )
    add_l2(
        out, "L2-ECN-V09-Q1", SUBJECT, mod9, "Economics", sub9, vid9, vid9, vtitle9, vtext9,
        "Determine the socially optimal level of regulation using marginal benefit and marginal cost",
        "Under Proposal 1, what regulatory intensity $x^*$ maximizes net economic welfare, and what is the resulting total net social benefit?",
        opts, ans,
        f"Optimal regulation equates $MB(x) = MC(x) \\implies 180 - 3x = 20 + 5x \\implies 8x = 160 \\implies x^* = {x_opt:.0f}$ units. Total net social benefit is the area between $MB$ and $MC$: $\\frac{{1}}{{2}}(180 - 20)({x_opt:.0f}) = \\text{{USD }} {net_surplus9:,.0f}$ million.",
        dist,
    )
    calc_ids.add("L2-ECN-V09-Q1")

    # Q2: Bank capital surcharge ROE dilution & lending spread pass-through (Modigliani-Miller off vs partial)
    pretax_roa_old = 0.0160
    tax9 = 0.25
    e_old, e_new = 0.08, 0.12
    roe_new_unchanged = pretax_roa_old * (1.0 - tax9) / e_new  # 10.0%
    # Target ROE = 12.0% -> required pretax ROA = 0.12 * 0.12 / 0.75 = 1.92% -> +32 bps!
    req_pretax_roa = 0.12 * e_new / (1.0 - tax9)
    bps_hike = (req_pretax_roa - pretax_roa_old) * 10000.0
    opts, ans, dist = make_mcq(
        f"ROE falls to {roe_new_unchanged*100:.1f}%; requires +{bps_hike:.0f} bps higher asset yield to hit a 12.0% ROE.",
        f"ROE falls to {roe_new_unchanged*100:.1f}%; requires +{((0.12*e_new - pretax_roa_old*(1-tax9))*10000):.0f} bps higher asset yield to hit a 12.0% ROE.",
        "Forgets to gross up the after-tax ROA shortfall by $(1 - t) = 0.75$ to obtain the required pre-tax lending spread increase.",
        f"ROE falls to {15.0 * (e_new/e_old):.1f}%; requires +{bps_hike:.0f} bps higher asset yield.",
        "Multiplies ROE by $0.12/0.08$ instead of dividing by the higher equity ratio (lower leverage lowers ROE).",
        ans_cycle(121),
    )
    add_l2(
        out, "L2-ECN-V09-Q2", SUBJECT, mod9, "Economics", sub9, vid9, vid9, vtitle9, vtext9,
        "Quantify financial institution ROE and lending-spread impacts of regulatory capital mandates",
        "Under Proposal 2 (ignoring Modigliani-Miller funding-cost offsets), if pre-tax ROA stays at 1.60%, what happens to after-tax ROE, and by how many basis points must pre-tax ROA rise to achieve a 12.0% target ROE?",
        opts, ans,
        f"After-tax ROA is $1.60\\%(1 - 0.25) = 1.20\\%$. At 12.0% equity/assets, ROE falls to $1.20\\% / 0.12 = {roe_new_unchanged*100:.1f}\\%$. Achieving 12.0% ROE requires after-tax ROA $= 0.12 \\times 0.12 = 1.44\\%$, or pre-tax ROA $= 1.44\\% / 0.75 = {req_pretax_roa*100:.2f}\\%$, a +{bps_hike:.0f} bps increase.",
        dist,
    )
    calc_ids.add("L2-ECN-V09-Q2")

    # Q3: Clearing mandate 6-year NPV calculation
    upfront9, net_cf9, r9, n9 = 45.0, 22.0 - 12.0, 0.06, 6
    pv_ann9 = net_cf9 * (1.0 - (1.0 + r9) ** (-n9)) / r9
    npv9 = pv_ann9 - upfront9
    undisc9 = net_cf9 * n9 - upfront9
    opts, ans, dist = make_mcq(
        f"USD {npv9:+.2f} million (passes benefit–cost test)",
        f"USD {undisc9:+.2f} million (passes benefit–cost test)",
        "Uses undiscounted cumulative net cash flows instead of discounting at 6.0%.",
        f"USD {(22.0 * ((1-(1+r9)**(-n9))/r9) - upfront9):+.2f} million",
        "Discounts gross benefits while omitting the USD 12 million annual compliance audit costs.",
        ans_cycle(122),
    )
    add_l2(
        out, "L2-ECN-V09-Q3", SUBJECT, mod9, "Economics", sub9, vid9, vid9, vtitle9, vtext9,
        "Perform cost-benefit net present value analysis on proposed regulations",
        "Evaluating Proposal 3 over its 6-year statutory window at a 6.0% discount rate, the regulatory Net Present Value (NPV) is closest to:",
        opts, ans,
        f"Annual net benefit is $22 - 12 = \\text{{USD }} {net_cf9:.0f}$M. Six-year annuity factor at 6.0% is $\\frac{{1 - 1.06^{{-6}}}}{{0.06}} = {pv_ann9/net_cf9:.4f}$, giving PV $= \\text{{USD }} {pv_ann9:.2f}$M and $\\text{{NPV}} = {pv_ann9:.2f} - 45.00 = \\text{{USD }} {npv9:+.2f}$M.",
        dist,
    )
    calc_ids.add("L2-ECN-V09-Q3")

    # Q4: Conceptual - Sunset clauses & regulatory review
    opts, ans, dist = make_mcq(
        "Forces periodic empirical re-evaluation so obsolete rules expire unless legislators or regulators prove ongoing net benefits.",
        "Automatically doubles industry compliance budgets every five years to track inflation.",
        "Sunset provisions force expiration and re-justification rather than automatic budget expansion.",
        "Eliminates judicial review and public comment periods before rule enactment.",
        "Administrative procedure comment periods apply to new rules; sunset clauses govern scheduled post-enactment re-assessment.",
        ans_cycle(123),
    )
    add_l2(
        out, "L2-ECN-V09-Q4", SUBJECT, mod9, "Economics", sub9, vid9, vid9, vtitle9, vtext9,
        "Explain regulatory classification, sunset clauses, and judicial/administrative review",
        "Why do economists frequently recommend attaching a 6-year sunset provision to Proposal 3?",
        opts, ans,
        "Sunset provisions counteract regulatory inertia and technological obsolescence by requiring regulators to demonstrate continued net social benefit before extending compliance mandates.",
        dist,
    )

    # Q5: Conceptual - Regulatory capture & unintended consequences
    opts, ans, dist = make_mcq(
        "High fixed compliance costs create economies of scale that favor incumbent mega-banks and raise barriers against smaller fintech entrants.",
        "Mandatory compliance audits always increase competition by lowering fixed overhead for startups.",
        "Fixed regulatory compliance overhead disproportionately burdens small firms, reducing competition.",
        "Higher bank capital requirements cause unregulated shadow credit markets to shrink to zero.",
        "Stricter regulated-bank requirements typically push credit intermediation toward less-regulated non-bank lenders (regulatory arbitrage).",
        ans_cycle(124),
    )
    add_l2(
        out, "L2-ECN-V09-Q5", SUBJECT, mod9, "Economics", sub9, vid9, vid9, vtitle9, vtext9,
        "Identify unintended consequences and competitive distortions of financial regulation",
        "Which unintended market structure consequence is most likely to emerge following Proposal 3 and Proposal 2?",
        opts, ans,
        "Fixed regulatory compliance infrastructure acts as a barrier to entry favoring large incumbents (sometimes reinforced via regulatory capture), while tighter bank capital rules spur credit migration into shadow banking.",
        dist,
    )

    # =========================================================================
    # V10: Economics for Capital Market Expectations
    # =========================================================================
    vid10 = "ECN-V10"
    vtitle10 = "Horizon Endowment: Macro Inputs for Capital Market Expectations"
    # 1) Grinold-Kroner equity expected return:
    #    E(Re) = D/P + (%dE - %dS) + %d(P/E)
    #    Wait: real earnings growth = trend real GDP growth + delta(profit share) = 2.4% + 0.0% = 2.4%; inflation = 2.2% -> nominal earnings growth %dE = (1.024*1.022 - 1) = 4.6528% (or approx 4.6%). Net share repurchase (-%dS) = +1.1% (share count shrinks 1.1%/yr). Valuation contraction %d(P/E) = -0.7%/yr. Dividend yield D/P = 1.9%.
    # 2) Singer-Terhaar global CAPM for Emerging Market Equities:
    #    rf = 3.8%, Sharpe_GIM = 0.30, rho(EM, GIM) = 0.65, sigma_EM = 20%, phi (degree of integration) = 0.75, illiquidity premium = 0.80%
    #    Fully integrated ERP = phi * rho * sigma * Sharpe_GIM? No!
    #    Full integration RP_int = rho * sigma * Sharpe_GIM = 0.65 * 0.20 * 0.30 = 3.90%
    #    Full segmentation RP_seg = 1.0 * sigma * Sharpe_seg (assume Sharpe_seg = 0.30 or 0.35! Let's specify Sharpe_seg = 0.35 -> RP_seg = 0.20 * 0.35 = 7.00%!)
    #    Weighted ERP = phi * RP_int + (1 - phi) * RP_seg = 0.75 * 3.90% + 0.25 * 7.00% = 2.925% + 1.750% = 4.675%
    #    Total E(R) = rf + ERP + illiquidity = 3.80% + 4.675% + 0.80% = 9.275% (9.28%!)
    # 3) Taylor Rule rate path forecast:
    #    r_neutral = 1.5%, pi_curr = 3.1%, pi_target = 2.0%, output gap = -1.2% -> i* = 1.5 + 3.1 + 0.5(1.1) + 0.5(-1.2) = 4.60 + 0.55 - 0.60 = 4.55%
    # 4) Long-term nominal GDP / corporate earnings anchor & bond return duration impact
    dp_10, real_g10, pi_10, net_buyback_10, dpe_10 = 1.90, 2.40, 2.20, 1.10, -0.70
    # Nominal earnings growth (compounded vs additive): let's state additive Grinold-Kroner or compute exact!
    # In CFA L3/L2 CME: Grinold-Kroner uses %dE = real GDP growth + expected inflation (approx 4.60%, exact 4.65%)
    nom_e_approx = real_g10 + pi_10  # 4.60%
    gk_ret_approx = dp_10 + nom_e_approx + net_buyback_10 + dpe_10  # 1.9 + 4.6 + 1.1 - 0.7 = 6.90%
    nom_e_exact = ((1 + real_g10/100)*(1 + pi_10/100) - 1)*100
    gk_ret_exact = dp_10 + nom_e_exact + net_buyback_10 + dpe_10

    rf_10, sharpe_gim, sharpe_seg, rho_em, sig_em, phi_10, illiq_10 = 3.80, 0.30, 0.35, 0.65, 20.0, 0.75, 0.80
    rp_int = rho_em * sig_em * sharpe_gim  # 3.90%
    rp_seg = sig_em * sharpe_seg           # 7.00%
    erp_st = phi_10 * rp_int + (1.0 - phi_10) * rp_seg  # 4.675%
    er_em = rf_10 + erp_st + illiq_10      # 9.275%

    r_n10, pi_c10, pi_t10, ygap_10 = 1.50, 3.10, 2.00, -1.20
    tay_10 = r_n10 + pi_c10 + 0.5 * (pi_c10 - pi_t10) + 0.5 * ygap_10  # 4.55%

    vtext10 = (
        "Marcus Vance, CIO of Horizon University Endowment, is updating 10-year Capital Market Expectations (CMEs):\n"
        "- **Developed Equities (Grinold-Kroner inputs):** Expected dividend yield $D/P = 1.90\\%$; trend real GDP/earnings growth $= 2.40\\%$; "
        "expected inflation $= 2.20\\%$; net share count change $\\%\\Delta S = -1.10\\%$ (net buybacks); expected annualized P/E multiple change $\\%\\Delta(P/E) = -0.70\\%$.\n"
        "- **Emerging Market Equities (Singer-Terhaar inputs):** Global risk-free rate $r_f = 3.80\\%$; global market Sharpe ratio $= 0.30$; "
        "segmented local Sharpe ratio $= 0.35$; EM return volatility $\\sigma_{\\text{EM}} = 20.0\\%$; correlation with global market $\\rho = 0.65$; "
        "degree of global market integration $\\phi = 0.75$; illiquidity premium $= 0.80\\%$.\n"
        "- **Sovereign Policy Benchmark (Taylor Rule):** Real neutral rate $r_{\\text{neutral}} = 1.50\\%$, current inflation $\\pi = 3.10\\%$, "
        "target inflation $\\pi^* = 2.00\\%$, and current output gap $(y - y^*) = -1.20\\%$."
    )
    mod10, sub10 = "Module 4", "Economics and Capital Market Expectations"

    # Q1: Grinold-Kroner expected equity return
    w1_gk = dp_10 + nom_e_approx - net_buyback_10 + dpe_10
    w2_gk = dp_10 + nom_e_approx + net_buyback_10
    opts, ans, dist = make_mcq(
        f"{gk_ret_approx:.2f}% (additive; {gk_ret_exact:.2f}% using compounded nominal growth)",
        f"{w1_gk:.2f}%",
        "Subtracts net buybacks instead of adding them—remember $-\\Delta S = -(-1.10\\%) = +1.10\\%$ boosts EPS per share.",
        f"{w2_gk:.2f}%",
        "Omits the -0.70% annual P/E valuation multiple contraction.",
        ans_cycle(125),
    )
    add_l2(
        out, "L2-ECN-V10-Q1", SUBJECT, mod10, "Economics", sub10, vid10, vid10, vtitle10, vtext10,
        "Calculate long-term equity expected returns using the Grinold-Kroner model",
        "Using the Grinold-Kroner decomposition $E(R_e) = D/P + (\\%\\Delta E - \\%\\Delta S) + \\%\\Delta(P/E)$, Horizon's 10-year expected nominal return on developed equities is closest to:",
        opts, ans,
        f"Expected nominal earnings growth $\\%\\Delta E \\approx 2.40\\% + 2.20\\% = 4.60\\%$ (compounded: {nom_e_exact:.2f}%). Because shares shrink by 1.10% ($-\\%\\Delta S = +1.10\\%$), $E(R_e) = 1.90\\% + 4.60\\% + 1.10\\% - 0.70\\% = {gk_ret_approx:.2f}\\%$ ({gk_ret_exact:.2f}% compounded).",
        dist,
    )
    calc_ids.add("L2-ECN-V10-Q1")

    # Q2: Singer-Terhaar expected return for EM equities
    w1_er = rf_10 + rp_int + illiq_10
    w2_er = rf_10 + erp_st
    opts, ans, dist = make_mcq(
        f"{er_em:.2f}%",
        f"{w1_er:.2f}%",
        "Assumes 100% global market integration ($\\phi = 1.00$), ignoring the 25% segmented market risk weight.",
        f"{w2_er:.2f}%",
        "Omits the 0.80% EM illiquidity premium when summing total expected return.",
        ans_cycle(126),
    )
    add_l2(
        out, "L2-ECN-V10-Q2", SUBJECT, mod10, "Economics", sub10, vid10, vid10, vtitle10, vtext10,
        "Calculate emerging market equity expected returns via the Singer-Terhaar model",
        "Under the Singer-Terhaar framework, Horizon's expected nominal return for Emerging Market equities is closest to:",
        opts, ans,
        f"Integrated risk premium $= \\rho \\sigma \\text{{Sharpe}}_{{\\text{{GIM}}}} = 0.65(20.0\\%)(0.30) = {rp_int:.2f}\\%$. Segmented risk premium $= \\sigma \\text{{Sharpe}}_{{\\text{{seg}}}} = 20.0\\%(0.35) = {rp_seg:.2f}\\%$. Weighted ERP $= 0.75({rp_int:.2f}\\%) + 0.25({rp_seg:.2f}\\%) = {erp_st:.3f}\\%$. Adding $r_f = 3.80\\%$ and illiquidity premium $0.80\\%$ gives {er_em:.2f}%.",
        dist,
    )
    calc_ids.add("L2-ECN-V10-Q2")

    # Q3: Taylor Rule target policy rate & yield curve implication
    w1_tay10 = r_n10 + pi_c10 + 0.5 * (pi_c10 - pi_t10) - 0.5 * ygap_10
    w2_tay10 = r_n10 + pi_t10 + 0.5 * (pi_c10 - pi_t10) + 0.5 * ygap_10
    opts, ans, dist = make_mcq(
        f"{tay_10:.2f}%",
        f"{w1_tay10:.2f}%",
        "Adds $+0.5(1.20\\%)$ instead of subtracting $0.5(-1.20\\%)$ for the negative output gap.",
        f"{w2_tay10:.2f}%",
        "Substitutes target inflation (2.00%) instead of current inflation (3.10%) in the baseline term.",
        ans_cycle(127),
    )
    add_l2(
        out, "L2-ECN-V10-Q3", SUBJECT, mod10, "Economics", sub10, vid10, vid10, vtitle10, vtext10,
        "Forecast short-term central bank policy rates using the Taylor Rule",
        "Using the standard Taylor rule $i^* = r_{\\text{neutral}} + \\pi + 0.5(\\pi - \\pi^*) + 0.5(y - y^*)$, the prescribed policy rate is:",
        opts, ans,
        f"$i^* = {r_n10:.2f}\\% + {pi_c10:.2f}\\% + 0.5({pi_c10:.2f}\\% - {pi_t10:.2f}\\%) + 0.5({ygap_10:.2f}\\%) = 4.60\\% + 0.55\\% - 0.60\\% = {tay_10:.2f}\\%$.",
        dist,
    )
    calc_ids.add("L2-ECN-V10-Q3")

    # Q4: Yield curve / Duration return impact from policy rate surprise
    # Suppose 10-year Treasuries (modified duration = 7.8, convexity = 68) currently yield 4.10%, and market expects Taylor rate to fall to 3.75% next year,
    # Wait: let's ask a clean numerical question based ONLY on vignette data + single given duration parameter!
    # If the current policy rate is 5.25% and the central bank cuts immediately toward the Taylor Rule rate of 4.55% (-70 bps), and 2-year sovereign notes have modified duration 1.90 and convexity 4.5:
    dy_bp = (tay_10 - 5.25) / 100.0  # -0.0070 (-70 bps)
    dur_2yr, conv_2yr = 1.90, 4.50
    px_chg = (-dur_2yr * dy_bp + 0.5 * conv_2yr * (dy_bp ** 2)) * 100.0
    w1_px = (-dur_2yr * abs(dy_bp) + 0.5 * conv_2yr * (dy_bp ** 2)) * 100.0
    opts, ans, dist = make_mcq(
        f"{px_chg:+.2f}%",
        f"{w1_px:.2f}%",
        "Uses a positive yield change sign instead of a -70 bps rate cut from 5.25% down to 4.55%.",
        f"{(dur_2yr * 1.00)*100:.2f}%",
        "Uses wrong rate shock magnitude instead of 5.25% moving to 4.55% (-70 bps).",
        ans_cycle(128),
    )
    add_l2(
        out, "L2-ECN-V10-Q4", SUBJECT, mod10, "Economics", sub10, vid10, vid10, vtitle10, vtext10,
        "Translate Taylor Rule policy rate shifts into fixed-income price changes",
        "If the current policy rate is 5.25% and 2-year sovereign yields immediately fall by the full shift down to the Taylor Rule target rate (modified duration = 1.90, convexity = 4.50), the estimated price change on the 2-year note is closest to:",
        opts, ans,
        f"Rate shift $\\Delta y = {tay_10:.2f}\\% - 5.25\\% = -0.70\\% = -0.0070$. Price change $\\approx -D(\\Delta y) + \\frac{{1}}{{2}}C(\\Delta y)^2 = -1.90(-0.0070) + 0.5(4.50)(-0.0070)^2 = +1.330\\% + 0.011\\% = {px_chg:+.2f}\\%$.",
        dist,
    )
    calc_ids.add("L2-ECN-V10-Q4")

    # Q5: Conceptual - CME forecasting pitfalls (time-period bias, regime change, status quo, survivorship)
    opts, ans, dist = make_mcq(
        "Time-period bias and failure to adjust for structural regime change (non-stationarity).",
        "Exclusively survivorship bias from delisted technology stocks.",
        "Survivorship bias affects fund/equity index averages, whereas extrapolating falling rates from 1982–2021 primarily reflects non-stationarity and time-period bias.",
        "Anchoring strictly on forward-looking Grinold-Kroner valuation adjustments.",
        "Adjusting forward P/E multiples downward prevents naive extrapolation of historical windfall multiple expansion.",
        ans_cycle(129),
    )
    add_l2(
        out, "L2-ECN-V10-Q5", SUBJECT, mod10, "Economics", sub10, vid10, vid10, vtitle10, vtext10,
        "Identify macroeconomic and statistical pitfalls in forming capital market expectations",
        "An analyst on Vance's team forecasts future 10-year bond and equity returns simply by taking sample means from 1982–2021 (a four-decade secular disinflation and falling-yield regime). Which CME forecasting pitfall is most directly exhibited?",
        opts, ans,
        "Sampling a specific favorable historical era (1982–2021 rate compression) and projecting those windfall capital gains forward exemplifies time-period bias and ignoring macroeconomic regime non-stationarity.",
        dist,
    )


def verify_and_save(questions: list, calc_ids: set, output_path: str):
    """Run strict integrity assertions before calling save_validated_json."""
    assert len(questions) == 130, f"Expected 130 questions, got {len(questions)}"
    l1_qs = [q for q in questions if q["level"] == 1]
    l2_qs = [q for q in questions if q["level"] == 2]
    assert len(l1_qs) == 80, f"Expected 80 L1 questions, got {len(l1_qs)}"
    assert len(l2_qs) == 50, f"Expected 50 L2 questions, got {len(l2_qs)}"

    expected_l1_ids = [f"L1-ECN-{i:03d}" for i in range(1, 81)]
    assert [q["id"] for q in l1_qs] == expected_l1_ids, "L1 ID sequence mismatch"

    expected_l2_ids = [
        f"L2-ECN-V{v:02d}-Q{q}" for v in range(1, 11) for q in range(1, 6)
    ]
    assert [q["id"] for q in l2_qs] == expected_l2_ids, "L2 ID sequence mismatch"

    # Verify >= 60% numerical calculation questions
    calc_ratio = len(calc_ids) / len(questions)
    assert calc_ratio >= 0.60, f"Calculation ratio {calc_ratio:.2%} < 60%"

    # Verify zero unintended Python escape control characters in any text field
    for q in questions:
        assert q["subject"] == SUBJECT
        fields = [
            q["question"], q["explanation"], q["los"],
            q["options"]["A"], q["options"]["B"], q["options"]["C"],
            *q["distractor_analysis"].values(),
        ]
        if q["level"] == 2:
            fields.extend([q["vignette_title"], q["vignette_text"]])
        for txt in fields:
            for ch in CONTROL_CHARS:
                assert ch not in txt, f"{q['id']}: Found control char {repr(ch)} in {txt[:80]}"

    save_validated_json(questions, output_path)
    ans_dist = {k: sum(1 for q in questions if q["answer"] == k) for k in ("A", "B", "C")}
    print(
        f"Verified 130 questions (80 L1, 50 L2 across 10 vignettes) | "
        f"Numerical: {len(calc_ids)}/130 ({calc_ratio:.1%}) | Answer distribution: {ans_dist}"
    )


def main():
    questions = []
    calc_ids = set()

    build_l1_m1_demand_supply(questions, calc_ids)
    build_l1_m2_market_structures(questions, calc_ids)
    build_l1_m3_business_cycles(questions, calc_ids)
    build_l1_m4_inflation_indicators(questions, calc_ids)
    build_l1_m5_fiscal_monetary(questions, calc_ids)
    build_l1_m6_geopolitics_reg(questions, calc_ids)
    build_l1_m7_trade_bop(questions, calc_ids)
    build_l1_m8_fx_rates(questions, calc_ids)
    build_l2_v01_to_v05(questions, calc_ids)
    build_l2_v06_to_v10(questions, calc_ids)

    output_path = os.path.join(ROOT_DIR, "data", "courses", "econ_qbank.json")
    verify_and_save(questions, calc_ids, output_path)


if __name__ == "__main__":
    main()
