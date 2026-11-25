"""
Generate 140 CFA-style Derivatives questions (85 Level 1 + 55 Level 2 across 11 vignettes)
and validate every question through scripts/qbank_helper.py.
"""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from qbank_helper import add_l1, add_l2, bsm_values, norm_cdf, norm_pdf, save_validated_json

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_PATH = os.path.join(ROOT, "data", "courses", "deriv_qbank.json")
SUBJECT = "Derivatives"

NUM_Q_IDS = set()


def _fmt_usd(val: float, dec: int = 2) -> str:
    sign = "-" if val < 0 else ""
    return f"{sign}USD {abs(val):,.{dec}f}"


def _fmt_eur(val: float, dec: int = 2) -> str:
    sign = "-" if val < 0 else ""
    return f"{sign}EUR {abs(val):,.{dec}f}"


def _fmt_pct(val: float, dec: int = 2) -> str:
    return f"{val * 100:.{dec}f}%"


def _fmt_num(val: float, dec: int = 2) -> str:
    return f"{val:,.{dec}f}"


def build_num_opts(
    correct_val: float,
    d1_val: float,
    d1_why: str,
    d2_val: float,
    d2_why: str,
    fmt_fn,
    descending: bool = False,
):
    """Sort three numeric choices cleanly and map exact distractor explanations."""
    items = [
        ("C", correct_val, fmt_fn(correct_val), None),
        ("D1", d1_val, fmt_fn(d1_val), d1_why),
        ("D2", d2_val, fmt_fn(d2_val), d2_why),
    ]
    strs = [x[2] for x in items]
    assert len(set(strs)) == 3, f"Duplicate formatted options: {strs}"
    items.sort(key=lambda x: x[1], reverse=descending)
    letters = ("A", "B", "C")
    options = {}
    distractors = {}
    answer = None
    for ltr, (tag, _, label, why) in zip(letters, items):
        options[ltr] = label
        if tag == "C":
            answer = ltr
        else:
            distractors[ltr] = why
    return options, answer, distractors


def build_text_opts(
    correct_txt: str,
    d1_txt: str,
    d1_why: str,
    d2_txt: str,
    d2_why: str,
    ans_letter: str,
):
    """Place three text choices at a chosen answer letter."""
    assert ans_letter in ("A", "B", "C")
    assert len({correct_txt, d1_txt, d2_txt}) == 3
    other = [k for k in ("A", "B", "C") if k != ans_letter]
    options = {ans_letter: correct_txt, other[0]: d1_txt, other[1]: d2_txt}
    distractors = {other[0]: d1_why, other[1]: d2_why}
    return options, ans_letter, distractors


def add_num_l1(out, qid, subject, module, topic, subtopic, los, question, options, answer, explanation, distractors):
    NUM_Q_IDS.add(qid)
    add_l1(out, qid, subject, module, topic, subtopic, los, question, options, answer, explanation, distractors)


def add_num_l2(
    out,
    qid,
    module,
    topic,
    subtopic,
    vignette_id,
    vignette_title,
    vignette_text,
    los,
    question,
    options,
    answer,
    explanation,
    distractors,
):
    NUM_Q_IDS.add(qid)
    add_l2(
        out,
        qid,
        SUBJECT,
        module,
        topic,
        subtopic,
        vignette_id,
        vignette_id,
        vignette_title,
        vignette_text,
        los,
        question,
        options,
        answer,
        explanation,
        distractors,
    )


def bsm_theta(S: float, K: float, r: float, T: float, sigma: float, q: float = 0.0):
    """Return annualized call and put theta under continuous compounding."""
    res = bsm_values(S, K, r, T, sigma, q)
    d1, Nd1, Nd2 = res["d1"], res["Nd1"], res["Nd2"]
    term1 = -(S * math.exp(-q * T) * norm_pdf(d1) * sigma) / (2.0 * math.sqrt(T))
    theta_c = term1 - r * K * math.exp(-r * T) * Nd2 + q * S * math.exp(-q * T) * Nd1
    theta_p = term1 + r * K * math.exp(-r * T) * (1.0 - Nd2) - q * S * math.exp(-q * T) * (1.0 - Nd1)
    return theta_c, theta_p


# =============================================================================
# LEVEL 1 QUESTIONS (85 Questions: L1-DRV-001 .. L1-DRV-085)
# =============================================================================

def build_l1_lm1_to_lm3(qs: list):
    """LM1 (001-008), LM2 (009-016), LM3 (017-022): Markets, Instruments, Uses."""
    # 001 (Conceptual)
    m, t, st = "DRV-LM1", "Derivative Markets and Instruments", "Exchange vs. OTC Markets"
    opts, ans, dist = build_text_opts(
        "Standardized contract terms, central clearinghouse novation, and high transparency",
        "Fully customized maturities, bilateral counterparty credit exposure, and private terms",
        "Customization, bilateral credit exposure, and privacy characterize over-the-counter (OTC) markets rather than exchanges.",
        "Zero margin requirements and settlement strictly upon contract maturity",
        "Exchange-traded derivatives require daily mark-to-market variation margin and initial margin rather than zero margin.",
        "B",
    )
    add_l1(
        qs, "L1-DRV-001", SUBJECT, m, t, st,
        "Contrast exchange-traded and over-the-counter derivative markets.",
        "Compared with over-the-counter (OTC) derivative markets, exchange-traded derivative markets are primarily characterized by:",
        opts, ans,
        "Exchange-traded derivatives feature standardized contract specifications, public price/volume transparency, daily mark-to-market margining, and a central clearinghouse (CCP) that interposes itself via novation to mitigate bilateral default risk.",
        dist,
    )

    # 002 (Conceptual)
    opts, ans, dist = build_text_opts(
        "Becoming the legal counterparty to both the original buyer and the original seller via novation",
        "Eliminating all market price risk on the underlying asset for both clearing members",
        "A CCP eliminates bilateral counterparty default risk via novation and margining, not the underlying asset's market price risk.",
        "Setting fixed forward contract prices by decree rather than supply and demand",
        "Prices are determined by market supply and demand on the exchange or OTC market, not set by the CCP.",
        "A",
    )
    add_l1(
        qs, "L1-DRV-002", SUBJECT, m, t, "Central Counterparty Clearing",
        "Describe the role of central clearinghouses in derivative markets.",
        "In centrally cleared derivative markets, how does a central counterparty (CCP) reduce bilateral credit risk?",
        opts, ans,
        "Through novation, the CCP replaces the original bilateral trade with two separate contracts—becoming the buyer to the seller and the seller to the buyer—while enforcing initial and variation margin.",
        dist,
    )

    # 003 (Numerical)
    pos_mtm, neg_mtm, notional = 1_850_000.0, -720_000.0, 60_000_000.0
    net_exp = pos_mtm + neg_mtm
    opts, ans, dist = build_num_opts(
        net_exp,
        pos_mtm, "USD 1,850,000 ignores the negative MTM offset allowed under the bilateral master netting agreement.",
        pos_mtm - neg_mtm, "USD 2,570,000 sums the absolute MTM values instead of netting positive and negative exposures.",
        lambda v: _fmt_usd(v, 0),
    )
    add_num_l1(
        qs, "L1-DRV-003", SUBJECT, m, t, "Notional vs. Credit Exposure",
        "Distinguish notional amount from market value and credit exposure.",
        "A dealer holds two OTC interest rate swaps with the same counterparty under an enforceable bilateral master netting agreement. Swap 1 has a notional of USD 35,000,000 and a mark-to-market (MTM) value of +USD 1,850,000; Swap 2 has a notional of USD 25,000,000 and an MTM value of -USD 720,000. What is the dealer's current net credit exposure to this counterparty?",
        opts, ans,
        f"Current credit exposure equals the netted positive replacement value across contracts under the master netting agreement: $\\max(0, \\text{{USD }} 1,850,000 - \\text{{USD }} 720,000) = \\text{{USD }} {net_exp:,.0f}$. Notional principals (USD 60,000,000) are not exchanged and do not measure replacement cost.",
        dist,
    )

    # 004 (Numerical)
    idx, mult, init_m, move = 4800.0, 50.0, 12_000.0, 0.025
    cval = idx * mult
    roe = (cval * move) / init_m
    opts, ans, dist = build_num_opts(
        roe,
        move, "2.50% is the unlevered return on the underlying index rather than the return on posted initial margin.",
        (cval * move) / (init_m * 2.0), "25.00% halves the return by misstating the leverage ratio as 10x instead of 20x.",
        lambda v: _fmt_pct(v, 2),
    )
    add_num_l1(
        qs, "L1-DRV-004", SUBJECT, m, t, "Futures Leverage",
        "Calculate leverage and margin return on exchange-traded futures.",
        f"An equity index futures contract trades at {idx:,.0f} with a multiplier of USD {mult:,.0f} and requires an initial margin of USD {init_m:,.0f} per contract. If a trader posts exactly the initial margin for 1 long contract and the futures price rises by {move*100:.1f}%, the trader's percentage return on initial margin is closest to:",
        opts, ans,
        f"Contract notional value is $4,800 \\times 50 = \\text{{USD }} {cval:,.0f}$, giving leverage of $\\text{{USD }} 240,000 / \\text{{USD }} 12,000 = 20.0\\times$. A $2.5\\%$ price rise generates a dollar gain of $\\text{{USD }} 240,000 \\times 0.025 = \\text{{USD }} 6,000$, which is $\\text{{USD }} 6,000 / \\text{{USD }} 12,000 = 50.00\\%$ on margin.",
        dist,
    )

    # 005 (Conceptual)
    opts, ans, dist = build_text_opts(
        "Forward commitments obligate both parties to transact; contingent claims grant a right without an obligation to the holder",
        "Forward commitments require an upfront cash premium; contingent claims always have zero value at initiation",
        "It is contingent claims (options) that require an upfront premium, whereas standard forward commitments have zero market value at initiation.",
        "Forward commitments have asymmetric payoffs; contingent claims always exhibit linear symmetric payoffs",
        "Forward commitments have linear, symmetric payoffs, while contingent claims have asymmetric (nonlinear) payoffs.",
        "C",
    )
    add_l1(
        qs, "L1-DRV-005", SUBJECT, m, t, "Commitments vs. Claims",
        "Distinguish forward commitments from contingent claims.",
        "Which statement accurately distinguishes forward commitments from contingent claims?",
        opts, ans,
        "Forward commitments (forwards, futures, swaps) legally obligate both parties to transact at agreed terms with symmetric linear payoffs. Contingent claims (such as options) give the buyer a right, not an obligation, creating asymmetric payoffs.",
        dist,
    )

    # 006 (Numerical)
    mtm, thresh, posted, mta = 3_150_000.0, 1_000_000.0, 1_400_000.0, 250_000.0
    req_col = mtm - thresh
    call_amt = req_col - posted
    opts, ans, dist = build_num_opts(
        call_amt,
        mtm - posted, "USD 1,750,000 omits subtracting the USD 1,000,000 uncollateralized threshold from MTM exposure.",
        req_col, "USD 2,150,000 ignores the USD 1,400,000 collateral already posted by the counterparty.",
        lambda v: _fmt_usd(v, 0),
    )
    add_num_l1(
        qs, "L1-DRV-006", SUBJECT, m, t, "Bilateral Collateralization",
        "Compute variation margin under an OTC Credit Support Annex (CSA).",
        "Under an OTC CSA, a dealer's MTM exposure to a counterparty is USD 3,150,000. The agreement specifies an unsecured threshold of USD 1,000,000 and a minimum transfer amount (MTA) of USD 250,000. The counterparty currently holds USD 1,400,000 in posted collateral with the dealer. What additional collateral must the counterparty post?",
        opts, ans,
        f"Required collateral is $\\max(0, \\text{{MTM}} - \\text{{Threshold}}) = \\text{{USD }} 3,150,000 - \\text{{USD }} 1,000,000 = \\text{{USD }} 2,150,000$. Subtracting existing collateral of USD 1,400,000 yields a shortfall of $\\text{{USD }} {call_amt:,.0f}$, which exceeds the USD 250,000 MTA and triggers a full transfer.",
        dist,
    )

    # 007 (Conceptual)
    opts, ans, dist = build_text_opts(
        "Cash settlement eliminates physical delivery logistics by transferring the net dollar difference between spot and contract prices",
        "Cash settlement converts a forward commitment into a contingent claim at maturity",
        "Settlement method does not change a forward commitment into an option; both parties remain obligated.",
        "Cash-settled contracts carry lower leverage because the full notional value must be deposited upfront",
        "Cash-settled futures still use margin leverage rather than full notional prefunding.",
        "A",
    )
    add_l1(
        qs, "L1-DRV-007", SUBJECT, m, t, "Settlement Mechanics",
        "Compare physical delivery and cash settlement in derivative contracts.",
        "Which statement best explains the primary operational advantage of cash-settled derivatives over physically settled contracts?",
        opts, ans,
        "Cash settlement settles contracts via a single net cash payment reflecting the difference between the final settlement price and the contract price, avoiding transportation, storage, and transfer costs of physical delivery.",
        dist,
    )

    # 008 (Numerical)
    n_ct, oz, p0, p1, pct_m = 5, 100, 2350.0, 2279.50, 0.08
    notional_g = n_ct * oz * p0
    init_mg = notional_g * pct_m
    pnl = n_ct * oz * (p0 - p1)
    roe_s = pnl / init_mg
    opts, ans, dist = build_num_opts(
        roe_s,
        (p0 - p1) / p0, "3.00% reflects only the unlevered percentage price decline in gold rather than return on posted margin.",
        -roe_s, "-37.50% reverses the sign; a short futures position profits when the futures price falls.",
        lambda v: _fmt_pct(v, 2),
    )
    add_num_l1(
        qs, "L1-DRV-008", SUBJECT, m, t, "Short Margin Return",
        "Calculate return on margin for a short commodity futures trade.",
        f"A trader shorts {n_ct} gold futures contracts ({oz} oz per contract) at USD {p0:,.2f}/oz, posting {pct_m*100:.0f}% initial margin. If gold futures fall to USD {p1:,.2f}/oz and the trader closes the position, the return on initial margin is closest to:",
        opts, ans,
        f"Initial notional is $5 \\times 100 \\times 2,350 = \\text{{USD }} {notional_g:,.0f}$, requiring initial margin of $0.08 \\times \\text{{USD }} 1,175,000 = \\text{{USD }} {init_mg:,.0f}$. Short gain is $500 \\times (2,350.00 - 2,279.50) = \\text{{USD }} {pnl:,.0f}$, yielding $\\text{{USD }} 35,250 / \\text{{USD }} 94,000 = {roe_s*100:.2f}\\%$.",
        dist,
    )

    # LM2 (009-016): Forward Commitments & Contingent Claims Payoffs
    m2, t2 = "DRV-LM2", "Forward Commitments and Contingent Claims"

    # 009 (Numerical)
    qty, f0_w, st_w = 10_000.0, 6.45, 6.18
    pay_short = qty * (f0_w - st_w)
    opts, ans, dist = build_num_opts(
        pay_short,
        -pay_short, "-USD 2,700 represents the long forward holder's payoff rather than the short forward seller's payoff.",
        qty * st_w, "USD 61,800 is the gross spot value of the wheat rather than the net forward settlement payoff.",
        lambda v: _fmt_usd(v, 0),
    )
    add_num_l1(
        qs, "L1-DRV-009", SUBJECT, m2, t2, "Forward Payoffs",
        "Calculate forward contract payoffs for long and short positions.",
        f"A grain producer enters a short forward contract to sell {qty:,.0f} bushels of wheat at USD {f0_w:.2f}/bushel. If the spot price at expiration is USD {st_w:.2f}/bushel, what is the producer's payoff at expiration?",
        opts, ans,
        f"The short forward payoff at expiration is $N \\times (F_0(T) - S_T) = 10,000 \\times (6.45 - 6.18) = \\text{{USD }} {pay_short:,.0f}$.",
        dist,
    )

    # 010 (Numerical)
    shares, x_c, prem_c, st_c = 1000.0, 85.0, 4.20, 92.50
    prof_c = shares * (max(0.0, st_c - x_c) - prem_c)
    payoff_c = shares * max(0.0, st_c - x_c)
    opts, ans, dist = build_num_opts(
        prof_c,
        payoff_c, "USD 7,500 is the option's gross expiration payoff without deducting the USD 4,200 premium paid.",
        shares * (st_c - x_c + prem_c), "USD 11,700 adds the call premium instead of subtracting it from expiration payoff.",
        lambda v: _fmt_usd(v, 0),
    )
    add_num_l1(
        qs, "L1-DRV-010", SUBJECT, m2, t2, "Call Option Profit",
        "Calculate payoff and profit for a long call option.",
        f"An investor buys 10 call option contracts (100 shares per contract) with an exercise price of USD {x_c:.2f} for a premium of USD {prem_c:.2f} per share. If the underlying stock trades at USD {st_c:.2f} at expiration, the investor's net profit is:",
        opts, ans,
        f"Total shares equal $10 \\times 100 = 1,000$. Gross payoff is $1,000 \\times \\max(0, 92.50 - 85.00) = \\text{{USD }} 7,500$. Subtracting the upfront premium ($1,000 \\times 4.20 = \\text{{USD }} 4,200$) gives a net profit of $\\text{{USD }} {prof_c:,.0f}$.",
        dist,
    )

    # 011 (Numerical)
    x_sc, prem_sc, st_sc = 120.0, 6.50, 129.0
    prof_sc = prem_sc - max(0.0, st_sc - x_sc)
    be_sc = x_sc + prem_sc
    opts, ans, dist = build_num_opts(
        prof_sc,
        -prof_sc, "+USD 2.50 is the net profit of the long call buyer, not the short call writer.",
        -(st_sc - x_sc), "-USD 9.00 omits the USD 6.50 option premium received by the call seller.",
        lambda v: _fmt_usd(v, 2),
    )
    add_num_l1(
        qs, "L1-DRV-011", SUBJECT, m2, t2, "Short Call Profit",
        "Determine profit and breakeven for a short call position.",
        f"A trader writes one European call option per share with strike USD {x_sc:.2f} and collects a premium of USD {prem_sc:.2f}. At expiration, the stock price is USD {st_sc:.2f}. What is the writer's profit per share?",
        opts, ans,
        f"The short call writer's profit is $\\Pi = c_0 - \\max(0, S_T - X) = 6.50 - \\max(0, 129.00 - 120.00) = 6.50 - 9.00 = -\\text{{USD }} 2.50$ (breakeven is $X + c_0 = \\text{{USD }} {be_sc:.2f}$).",
        dist,
    )

    # 012 (Numerical)
    x_p, prem_p, st_p = 60.0, 3.80, 51.50
    prof_p = max(0.0, x_p - st_p) - prem_p
    opts, ans, dist = build_num_opts(
        prof_p,
        max(0.0, x_p - st_p), "USD 8.50 is the gross put payoff, ignoring the USD 3.80 premium paid.",
        x_p - prem_p, "USD 56.20 is the breakeven stock price of the long put rather than its net profit.",
        lambda v: _fmt_usd(v, 2),
    )
    add_num_l1(
        qs, "L1-DRV-012", SUBJECT, m2, t2, "Long Put Profit",
        "Calculate payoff and profit for a long put option.",
        f"An investor purchases a put option with a strike price of USD {x_p:.2f} for USD {prem_p:.2f}. If the underlying asset closes at USD {st_p:.2f} at expiration, the investor's net profit per share is:",
        opts, ans,
        f"Long put profit is $\\Pi = \\max(0, X - S_T) - p_0 = \\max(0, 60.00 - 51.50) - 3.80 = 8.50 - 3.80 = \\text{{USD }} {prof_p:.2f}$.",
        dist,
    )

    # 013 (Numerical)
    x_sp, prem_sp = 45.0, 2.60
    max_loss_sp = x_sp - prem_sp
    opts, ans, dist = build_num_opts(
        max_loss_sp,
        x_sp, "USD 45.00 ignores the USD 2.60 premium collected upfront by the put writer.",
        x_sp + prem_sp, "USD 47.60 erroneously adds the premium to the strike instead of subtracting it.",
        lambda v: _fmt_usd(v, 2),
    )
    add_num_l1(
        qs, "L1-DRV-013", SUBJECT, m2, t2, "Short Put Risk",
        "Identify maximum gain and maximum loss for a short put.",
        f"An investor sells a naked put option with a strike price of USD {x_sp:.2f} for a premium of USD {prem_sp:.2f}. What is the investor's maximum possible loss per share at expiration?",
        opts, ans,
        f"A short put incurs its worst loss if the stock drops to zero ($S_T = 0$), forcing the writer to pay $X$ for a worthless asset, offset by the premium collected: $\\text{{Max Loss}} = X - p_0 = 45.00 - 2.60 = \\text{{USD }} {max_loss_sp:.2f}$.",
        dist,
    )

    # 014 (Conceptual)
    opts, ans, dist = build_text_opts(
        "Buying a call option and selling a put option with identical strike prices and expiration dates",
        "Buying a call option and buying a put option with identical strike prices and expiration dates",
        "A long call plus a long put forms a straddle, which yields a V-shaped symmetric-volatility payoff rather than a linear forward payoff.",
        "Selling a call option and selling a put option with identical strike prices and expiration dates",
        "Shorting both a call and a put creates a short straddle with capped upside and unbounded downside, not a long forward.",
        "B",
    )
    add_l1(
        qs, "L1-DRV-014", SUBJECT, m2, t2, "Option Combination Payoff",
        "Explain how combining options replicates a linear forward payoff.",
        "Which option combination at expiration produces a payoff identical to a long forward contract with delivery price $X$?",
        opts, ans,
        "At expiration, a long call pays $\\max(0, S_T - X)$ and a short put pays $-\\max(0, X - S_T)$. Combining them produces $S_T - X$ across all values of $S_T$, replicating a long forward payoff.",
        dist,
    )

    # 015 (Numerical)
    cds_np, rec = 12_000_000.0, 0.35
    cds_pay = cds_np * (1.0 - rec)
    opts, ans, dist = build_num_opts(
        cds_pay,
        cds_np * rec, "USD 4,200,000 equals the recovery value rather than the loss-given-default payout.",
        cds_np, "USD 12,000,000 assumes zero recovery on the defaulted reference obligation.",
        lambda v: _fmt_usd(v, 0),
    )
    add_num_l1(
        qs, "L1-DRV-015", SUBJECT, m2, t2, "Credit Default Swaps",
        "Calculate the contingent payoff of a credit default swap (CDS).",
        "A portfolio manager buys USD 12,000,000 notional protection on a corporate issuer via a single-name CDS. A credit event occurs and the CDS settlement auction determines a recovery rate of 35% of par. What cash settlement amount must the protection seller pay the buyer?",
        opts, ans,
        f"Upon a credit event, the CDS protection seller pays the loss given default: $\\text{{Notional}} \\times (1 - \\text{{Recovery Rate}}) = \\text{{USD }} 12,000,000 \\times (1 - 0.35) = \\text{{USD }} {cds_pay:,.0f}$.",
        dist,
    )

    # 016 (Numerical)
    fx_k, c_p16, st_16 = 100.0, 7.40, 114.0
    prof_fwd16 = st_16 - fx_k
    prof_call16 = (st_16 - fx_k) - c_p16
    diff_16 = prof_fwd16 - prof_call16
    opts, ans, dist = build_num_opts(
        prof_call16,
        prof_fwd16, "USD 14.00 is the profit on the long forward contract, ignoring the USD 7.40 call premium.",
        diff_16, "USD 7.40 is the difference between the forward profit and call profit, not the call's net profit.",
        lambda v: _fmt_usd(v, 2),
    )
    add_num_l1(
        qs, "L1-DRV-016", SUBJECT, m2, t2, "Forward vs. Option Profit",
        "Compare net profit profiles of forwards and call options.",
        f"A forward contract has a forward price of USD {fx_k:.2f}, and a European call on the same asset has a strike price of USD {fx_k:.2f} and costs USD {c_p16:.2f}. If the underlying asset finishes at USD {st_16:.2f} at expiration, the net profit of the long call is:",
        opts, ans,
        f"The long forward profits $S_T - F_0 = 114.00 - 100.00 = \\text{{USD }} 14.00$. The long call pays the same gross USD 14.00 but incurred an upfront cost of USD {c_p16:.2f}, netting $\\text{{USD }} {prof_call16:.2f}$.",
        dist,
    )

    # LM3 (017-022): Benefits, Risks, Hedging Uses
    m3, t3 = "DRV-LM3", "Derivative Benefits, Risks, and Uses"

    # 017 (Conceptual)
    opts, ans, dist = build_text_opts(
        "Lower transaction costs, easier short exposure without borrowing the underlying, and operational price discovery",
        "Elimination of all systemic financial leverage and counterparty risks across capital markets",
        "Derivatives introduce leverage and (especially in OTC markets) counterparty risk rather than eliminating them.",
        "Guaranteed positive expected returns above the risk-free rate for corporate hedgers",
        "Derivatives redistribute risk and aid price discovery; they do not guarantee riskless excess returns.",
        "C",
    )
    add_l1(
        qs, "L1-DRV-017", SUBJECT, m3, t3, "Market Efficiency Benefits",
        "Describe benefits of derivative markets for investors and issuers.",
        "Which of the following is a primary economic benefit that derivative markets provide relative to trading solely in spot cash markets?",
        opts, ans,
        "Derivative markets lower transaction costs, enable efficient short positioning without securities lending, facilitate risk allocation, and improve market liquidity and price discovery.",
        dist,
    )

    # 018 (Conceptual)
    opts, ans, dist = build_text_opts(
        "Basis risk arising from an imperfect match between the hedged exposure and the derivative's underlying asset or maturity",
        "Model risk caused by an exchange clearinghouse changing contract multipliers daily",
        "Exchange clearinghouses do not alter multipliers daily; daily settlement adjusts variation margin, not contract specifications.",
        "Settlement risk arising solely because cash-settled futures have zero correlation with spot prices",
        "Cash-settled futures track spot prices tightly and converge to spot at expiration.",
        "A",
    )
    add_l1(
        qs, "L1-DRV-018", SUBJECT, m3, t3, "Basis Risk",
        "Identify risks associated with cross-hedging using derivatives.",
        "An airline hedges jet fuel expenses using heating oil futures because liquid jet fuel futures are unavailable. Which risk remains most prominent in this hedging strategy?",
        opts, ans,
        "Cross-hedging introduces basis risk—the risk that price changes in the hedging instrument (heating oil futures) do not move identically with the hedged item (jet fuel).",
        dist,
    )

    # 019 (Numerical)
    s0_cc, x_cc, prem_cc, st_cc = 74.0, 80.0, 3.40, 83.0
    prof_cc = (x_cc - s0_cc) + prem_cc
    opts, ans, dist = build_num_opts(
        prof_cc,
        (st_cc - s0_cc) + prem_cc, "USD 12.40 fails to cap the stock's upside appreciation at the USD 80.00 short call strike.",
        (x_cc - s0_cc) - prem_cc, "USD 2.60 subtracts the call premium received instead of adding it to the position profit.",
        lambda v: _fmt_usd(v, 2),
    )
    add_num_l1(
        qs, "L1-DRV-019", SUBJECT, m3, t3, "Covered Call Strategy",
        "Calculate payoff, profit, and breakeven for a covered call.",
        f"An equity investor owns shares currently trading at USD {s0_cc:.2f} and writes a covered call with strike USD {x_cc:.2f} for a premium of USD {prem_cc:.2f}. If the stock ends at USD {st_cc:.2f} at expiration, the net profit per share (relative to current price) is:",
        opts, ans,
        f"Because $S_T = 83.00 > X = 80.00$, the shares are called away at USD 80.00. Covered call profit is $\\min(S_T, X) - S_0 + c_0 = (80.00 - 74.00) + 3.40 = \\text{{USD }} {prof_cc:.2f}$.",
        dist,
    )

    # 020 (Numerical)
    s0_pp, x_pp, prem_pp, st_pp = 95.0, 90.0, 2.90, 82.0
    prof_pp = x_pp - s0_pp - prem_pp
    opts, ans, dist = build_num_opts(
        prof_pp,
        st_pp - s0_pp - prem_pp, "-USD 15.90 treats the put as expired worthless rather than exercising it at USD 90.00.",
        x_pp - s0_pp, "-USD 5.00 ignores the USD 2.90 put premium paid to establish the floor.",
        lambda v: _fmt_usd(v, 2),
    )
    add_num_l1(
        qs, "L1-DRV-020", SUBJECT, m3, t3, "Protective Put Strategy",
        "Calculate payoff, minimum value, and profit for a protective put.",
        f"A portfolio manager holds stock trading at USD {s0_pp:.2f} and buys a protective put with strike USD {x_pp:.2f} for USD {prem_pp:.2f}. If the stock falls to USD {st_pp:.2f} at expiration, what is the strategy's net profit per share (from current value)?",
        opts, ans,
        f"Because $S_T = 82.00 < X = 90.00$, the put is exercised so total ending value is floored at USD 90.00. Net profit is $X - S_0 - p_0 = 90.00 - 95.00 - 2.90 = -\\text{{USD }} {abs(prof_pp):.2f}$.",
        dist,
    )

    # 021 (Numerical)
    vp, bp, bt, fp21, m21 = 27_000_000.0, 1.20, 0.80, 4500.0, 50.0
    vf21 = fp21 * m21
    n_f21 = (bt - bp) * (vp / vf21)
    opts, ans, dist = build_num_opts(
        abs(n_f21),
        round(bp * (vp / vf21)), "144 contracts reduces the portfolio beta all the way to zero rather than to the 0.80 target.",
        round(bt * (vp / vf21)), "96 contracts uses the target beta directly instead of the beta reduction (1.20 - 0.80).",
        lambda v: f"Short {v:,.0f} contracts",
    )
    add_num_l1(
        qs, "L1-DRV-021", SUBJECT, m3, t3, "Portfolio Beta Hedging",
        "Calculate the number of index futures contracts needed to adjust portfolio beta.",
        f"An equity fund valued at USD {vp:,.0f} has a beta of {bp:.2f}. The manager wants to reduce portfolio beta to {bt:.2f} using index futures trading at {fp21:,.0f} with a USD {m21:,.0f} multiplier (futures beta = 1.00). What futures trade should the manager execute?",
        opts, ans,
        f"Number of contracts: $N_f = \\left(\\frac{{\\beta_T - \\beta_P}}{{\\beta_F}}\\right) \\left(\\frac{{V_P}}{{F_0 \\times m}}\\right) = \\left(\\frac{{0.80 - 1.20}}{{1.00}}\\right) \\left(\\frac{{27,000,000}}{{225,000}}\\right) = -0.40 \\times 120 = -48$ (short {abs(n_f21):.0f} contracts).",
        dist,
    )

    # 022 (Numerical)
    gal, s0_f, f0_f, s1_f, f1_f = 500_000.0, 2.72, 2.68, 3.05, 2.99
    eff_cost = s1_f - (f1_f - f0_f)
    opts, ans, dist = build_num_opts(
        eff_cost,
        s1_f, "USD 3.05/gal reflects the unhedged spot price without offsetting the futures gain.",
        s1_f + (f1_f - f0_f), "USD 3.36/gal adds the futures gain instead of subtracting it from the fuel purchase cost.",
        lambda v: f"USD {v:.2f}/gal",
    )
    add_num_l1(
        qs, "L1-DRV-022", SUBJECT, m3, t3, "Cash-Flow Cross-Hedge",
        "Calculate effective hedged purchase cost with futures basis.",
        f"A transport firm plans to buy {gal:,.0f} gallons of diesel in 3 months and goes long futures on {gal:,.0f} gallons at USD {f0_f:.2f}/gal (current spot is USD {s0_f:.2f}/gal). At purchase, spot diesel is USD {s1_f:.2f}/gal and the futures contract closes at USD {f1_f:.2f}/gal. The firm's effective hedged cost per gallon is:",
        opts, ans,
        f"Futures gain per gallon is $2.99 - 2.68 = \\text{{USD }} 0.31$. Subtracting this hedge gain from the spot purchase price gives an effective cost of $3.05 - 0.31 = \\text{{USD }} {eff_cost:.2f}\\text{{/gal}}$ (equivalently $F_0 + \\text{{ending basis}} = 2.68 + 0.06$).",
        dist,
    )


def build_l1_lm4_to_lm6(qs: list):
    """LM4 (023-036), LM5 (037-046), LM6 (047-054): Cost of Carry, Forwards, Futures."""
    m4, t4 = "DRV-LM4", "Arbitrage, Replication, and Cost of Carry"

    # 023 (Conceptual)
    opts, ans, dist = build_text_opts(
        "The asset's spot price, risk-free rate, and net cost of carry—independent of investor expectations of future spot prices",
        "Investors' consensus expected spot price at maturity discounted at the asset's required return on equity",
        "Unlike spot asset valuation, forward pricing relies on riskless no-arbitrage replication rather than expected future spot prices or risk premiums.",
        "Historical 12-month realized return volatility and the correlation with the market portfolio",
        "Volatility and beta affect option prices and spot risk premiums, not linear no-arbitrage forward prices.",
        "A",
    )
    add_l1(
        qs, "L1-DRV-023", SUBJECT, m4, t4, "No-Arbitrage Principle",
        "Explain why forward prices do not depend on expected future spot prices.",
        "Under the no-arbitrage pricing framework, the fair forward price of an underlying asset is determined directly by:",
        opts, ans,
        "By cash-and-carry replication (buying the asset spot and financing it at the risk-free rate while accounting for carry costs and benefits), no-arbitrage fixes $F_0(T)$ solely from $S_0$, $r$, and net carry—independent of subjective expectations of $S_T$.",
        dist,
    )

    # 024 (Numerical)
    s0_24, r_24, t_24, fm_24 = 150.0, 0.045, 0.5, 155.20
    fair_24 = s0_24 * ((1.0 + r_24) ** t_24)
    pv_arb24 = (fm_24 - fair_24) / ((1.0 + r_24) ** t_24)
    opts, ans, dist = build_num_opts(
        pv_arb24,
        fm_24 - fair_24, f"USD {fm_24 - fair_24:.2f} is the future value profit at T = 0.5 years rather than its present value at t = 0.",
        fm_24 - s0_24, f"USD {fm_24 - s0_24:.2f} ignores the risk-free financing cost of holding the underlying stock.",
        lambda v: _fmt_usd(v, 2),
    )
    add_num_l1(
        qs, "L1-DRV-024", SUBJECT, m4, t4, "Cash-and-Carry Arbitrage",
        "Calculate arbitrage profit when a forward contract is overpriced.",
        f"A non-dividend-paying stock trades at USD {s0_24:.2f}. The annual risk-free rate is {r_24*100:.1f}% (discrete compounding), and a 6-month ($T = 0.5$) forward contract trades at USD {fm_24:.2f}. What is the present value at $t = 0$ of the riskless arbitrage profit per share?",
        opts, ans,
        f"No-arbitrage forward price is $F_0 = 150(1.045)^{{0.5}} = \\text{{USD }} {fair_24:.4f}$. Selling the overpriced forward at USD {fm_24:.2f} and buying the stock with borrowed funds locks in a $T=0.5$ profit of $155.20 - {fair_24:.4f} = \\text{{USD }} {fm_24 - fair_24:.4f}$, with present value $\\text{{USD }} {fm_24 - fair_24:.4f} / (1.045)^{{0.5}} = \\text{{USD }} {pv_arb24:.2f}$.",
        dist,
    )

    # 025 (Numerical)
    s0_25, r_25, t_25, fm_25 = 80.0, 0.05, 1.0, 82.40
    fair_25 = s0_25 * (1.0 + r_25)
    pv_arb25 = (fair_25 - fm_25) / (1.0 + r_25)
    opts, ans, dist = build_num_opts(
        pv_arb25,
        fair_25 - fm_25, f"USD {fair_25 - fm_25:.2f} is the future-value profit at T = 1 year rather than the present value at t = 0.",
        s0_25 - fm_25 / (1.0 + r_25) - 0.50, "Incorrectly adjusts the forward discount factor.",
        lambda v: _fmt_usd(v, 2),
    )
    # Better d2 for 025: ignoring discounting and subtracting fm from s0
    d2_25 = s0_25 - fm_25
    opts, ans, dist = build_num_opts(
        pv_arb25,
        fair_25 - fm_25, f"USD {fair_25 - fm_25:.2f} reports the arbitrage profit at maturity T = 1 instead of its present value at t = 0.",
        fm_25 - s0_25, f"USD {fm_25 - s0_25:.2f} simply takes the basis spread without incorporating the 5% risk-free lending rate.",
        lambda v: _fmt_usd(v, 2),
    )
    add_num_l1(
        qs, "L1-DRV-025", SUBJECT, m4, t4, "Reverse Cash-and-Carry",
        "Calculate arbitrage profit when a forward contract is underpriced.",
        f"A non-dividend-paying stock trades at USD {s0_25:.2f} and the 1-year risk-free rate is {r_25*100:.1f}% (annual compounding). If a 1-year forward contract is quoted at USD {fm_25:.2f}, the present value of the reverse cash-and-carry arbitrage profit per share is closest to:",
        opts, ans,
        f"Fair forward price is $80(1.05) = \\text{{USD }} {fair_25:.2f}$. Because the market forward ({fm_25:.2f}) is underpriced, shorting the stock at USD 80, lending proceeds at 5%, and going long the forward yields $84.00 - 82.40 = \\text{{USD }} 1.60$ at $T=1$, whose present value is $1.60 / 1.05 = \\text{{USD }} {pv_arb25:.2f}$.",
        dist,
    )

    # 026 (Numerical)
    s0_26, r_26, c_26, tc_26, t_26 = 2100.0, 0.04, 18.0, 0.5, 1.0
    pvc_26 = c_26 / ((1.0 + r_26) ** tc_26)
    f0_26 = (s0_26 + pvc_26) * (1.0 + r_26)
    opts, ans, dist = build_num_opts(
        f0_26,
        (s0_26 - pvc_26) * (1.0 + r_26), "Subtracts storage costs from spot instead of adding them as a carrying cost.",
        s0_26 * (1.0 + r_26) + c_26, "Fails to compound the mid-year storage cost from t = 0.5 to maturity T = 1.0.",
        lambda v: _fmt_usd(v, 2),
    )
    add_num_l1(
        qs, "L1-DRV-026", SUBJECT, m4, t4, "Storage Costs",
        "Price a commodity forward with discrete storage costs.",
        f"Gold trades at a spot price of USD {s0_26:,.2f}/oz. Storage costs of USD {c_26:.2f}/oz must be paid in 6 months ($t = 0.5$). If the annual discrete risk-free rate is {r_26*100:.1f}%, the 1-year equilibrium forward price per ounce is closest to:",
        opts, ans,
        f"PV of storage cost is $PV_0(C) = 18.00 / (1.04)^{{0.5}} = \\text{{USD }} {pvc_26:.4f}$. Adding carrying costs to spot and compounding gives $F_0(1) = (2,100 + {pvc_26:.4f})(1.04) = \\text{{USD }} {f0_26:,.2f}$.",
        dist,
    )

    # 027 (Numerical)
    s0_27, div_27, r_27, td_27, t_27 = 120.0, 2.50, 0.052, 90.0 / 365.0, 180.0 / 365.0
    pvd_27 = div_27 / ((1.0 + r_27) ** td_27)
    f0_27 = (s0_27 - pvd_27) * ((1.0 + r_27) ** t_27)
    opts, ans, dist = build_num_opts(
        f0_27,
        (s0_27 + pvd_27) * ((1.0 + r_27) ** t_27), "Adds the PV of the dividend instead of subtracting it as a carry benefit.",
        s0_27 * ((1.0 + r_27) ** t_27), "Ignores the USD 2.50 dividend paid prior to forward expiration.",
        lambda v: _fmt_usd(v, 2),
    )
    add_num_l1(
        qs, "L1-DRV-027", SUBJECT, m4, t4, "Discrete Dividends",
        "Price an equity forward when the underlying pays discrete dividends.",
        f"A stock trades at USD {s0_27:.2f} and is expected to pay a USD {div_27:.2f} dividend in 90 days. Using an annual discrete risk-free rate of {r_27*100:.1f}% and a 365-day year, the fair 180-day forward price is closest to:",
        opts, ans,
        f"$PV_0(D) = 2.50 / (1.052)^{{90/365}} = \\text{{USD }} {pvd_27:.4f}$. Subtracting this benefit from spot and compounding for 180 days gives $F_0 = (120.00 - {pvd_27:.4f})(1.052)^{{180/365}} = \\text{{USD }} {f0_27:.2f}$.",
        dist,
    )

    # 028 (Numerical)
    s0_28, q_28, r_28, t_28 = 4900.0, 0.018, 0.046, 0.75
    f0_28 = s0_28 * math.exp((r_28 - q_28) * t_28)
    opts, ans, dist = build_num_opts(
        f0_28,
        s0_28 * math.exp((r_28 + q_28) * t_28), "Adds the continuous dividend yield q instead of subtracting it from r.",
        s0_28 * math.exp(r_28 * t_28), "Omits the continuous dividend yield from the cost-of-carry exponent.",
        lambda v: _fmt_num(v, 2),
    )
    add_num_l1(
        qs, "L1-DRV-028", SUBJECT, m4, t4, "Continuous Dividend Yield",
        "Price an equity index forward using continuous compounding.",
        f"An equity index stands at {s0_28:,.0f} and carries a continuous dividend yield of {q_28*100:.1f}%. If the continuously compounded risk-free rate is {r_28*100:.1f}%, what is the 9-month ($T = 0.75$) fair forward price?",
        opts, ans,
        f"With continuous compounding, $F_0(T) = S_0 e^{{(r - q)T}} = 4,900 e^{{(0.046 - 0.018)(0.75)}} = 4,900 e^{{0.021}} = {f0_28:,.2f}$.",
        dist,
    )

    # 029 (Numerical)
    s0_29, r_29, c_29, gam_29, t_29 = 78.0, 0.042, 0.035, 0.061, 0.50
    f0_29 = s0_29 * math.exp((r_29 + c_29 - gam_29) * t_29)
    opts, ans, dist = build_num_opts(
        f0_29,
        s0_29 * math.exp((r_29 + c_29 + gam_29) * t_29), "Adds convenience yield instead of subtracting it as a non-monetary carry benefit.",
        s0_29 * math.exp((r_29 - c_29 - gam_29) * t_29), "Subtracts storage cost instead of adding it to the cost of carry.",
        lambda v: _fmt_usd(v, 2),
    )
    add_num_l1(
        qs, "L1-DRV-029", SUBJECT, m4, t4, "Convenience Yield",
        "Price a commodity forward incorporating storage costs and convenience yield.",
        f"Copper trades at USD {s0_29:.2f}. Continuous annualized rates are: risk-free rate {r_29*100:.1f}%, storage cost {c_29*100:.1f}%, and convenience yield {gam_29*100:.1f}%. The 6-month ($T = 0.50$) forward price is closest to:",
        opts, ans,
        f"Net carry rate is $r + c - \\gamma = 4.2\\% + 3.5\\% - 6.1\\% = +1.6\\%$. Thus $F_0(0.5) = 78 e^{{0.016 \\times 0.5}} = \\text{{USD }} {f0_29:.2f}$.",
        dist,
    )

    # 030 (Numerical)
    s0_30, f0_30, r_30, c_30, t_30 = 92.0, 90.50, 0.048, 0.024, 1.0
    gam_30 = r_30 + c_30 - math.log(f0_30 / s0_30) / t_30
    opts, ans, dist = build_num_opts(
        gam_30,
        math.log(f0_30 / s0_30) / t_30, "-1.64% reports the net cost of carry rather than solving for the convenience yield.",
        r_30 - c_30 - math.log(f0_30 / s0_30), "4.04% subtracts storage cost from r rather than adding it before deducting ln(F0/S0).",
        lambda v: _fmt_pct(v, 2),
    )
    add_num_l1(
        qs, "L1-DRV-030", SUBJECT, m4, t4, "Implied Convenience Yield",
        "Solve for the implied convenience yield from an observed forward price.",
        f"Crude oil spot trades at USD {s0_30:.2f}/bbl while the 1-year forward trades in backwardation at USD {f0_30:.2f}/bbl. If the continuous risk-free rate is {r_30*100:.1f}% and continuous storage cost is {c_30*100:.1f}% annually, what is the implied annual convenience yield?",
        opts, ans,
        f"From $F_0 = S_0 e^{{(r + c - \\gamma)T}}$, we get $\\gamma = r + c - \\frac{{\\ln(F_0/S_0)}}{{T}} = 0.048 + 0.024 - \\ln(90.50/92.00) = 0.072 - (-0.01644) = {gam_30*100:.2f}\\%$.",
        dist,
    )

    # 031 (Numerical)
    s0_31, r_usd31, r_gbp31, days31 = 1.2650, 0.050, 0.042, 90.0
    f0_31 = s0_31 * (1.0 + r_usd31 * days31 / 360.0) / (1.0 + r_gbp31 * days31 / 360.0)
    opts, ans, dist = build_num_opts(
        f0_31,
        s0_31 * (1.0 + r_gbp31 * days31 / 360.0) / (1.0 + r_usd31 * days31 / 360.0), "Inverts the domestic and foreign interest rates in covered interest rate parity.",
        s0_31 * (1.0 + r_usd31) / (1.0 + r_gbp31), "Applies full-year rates instead of 90/360 simple periodic rates.",
        lambda v: f"{v:.4f} USD/GBP",
    )
    add_num_l1(
        qs, "L1-DRV-031", SUBJECT, m4, t4, "Currency Forward Pricing",
        "Calculate an equilibrium FX forward rate using covered interest rate parity.",
        f"The spot exchange rate is {s0_31:.4f} USD per GBP. Annualized 90-day money market rates (Act/360) are {r_usd31*100:.2f}% in USD and {r_gbp31*100:.2f}% in GBP. The no-arbitrage 90-day forward rate (in USD per GBP) is closest to:",
        opts, ans,
        f"By covered interest rate parity, $F_0 = S_0 \\frac{{1 + r_{{\\text{{USD}}}} (90/360)}}{{1 + r_{{\\text{{GBP}}}} (90/360)}} = 1.2650 \\times \\frac{{1.0125}}{{1.0105}} = {f0_31:.4f}$ USD/GBP.",
        dist,
    )

    # 032 (Numerical)
    s0_32, r_usd32, r_eur32, fm_32, np_eur = 1.0850, 0.048, 0.032, 1.1140, 1_000_000.0
    fair_32 = s0_32 * (1.0 + r_usd32) / (1.0 + r_eur32)
    # Borrow USD to convert EUR 1M/(1+r_eur) at spot, invest EUR to get EUR 1M at T=1, sell EUR 1M forward at fm_32
    prof_usd32 = np_eur * (fm_32 - fair_32)
    opts, ans, dist = build_num_opts(
        prof_usd32,
        np_eur * (fm_32 - s0_32), "USD 29,000 ignores the USD-EUR interest rate differential in computing the fair forward rate.",
        prof_usd32 / (1.0 + r_usd32), f"USD {prof_usd32/(1+r_usd32):,.0f} reports the present value at t = 0 rather than the realized USD profit at T = 1 year.",
        lambda v: _fmt_usd(v, 0),
    )
    add_num_l1(
        qs, "L1-DRV-032", SUBJECT, m4, t4, "Covered Interest Arbitrage",
        "Calculate covered interest arbitrage profit on a mispriced FX forward.",
        f"The spot exchange rate is {s0_32:.4f} USD per EUR, 1-year USD rate is {r_usd32*100:.1f}%, and 1-year EUR rate is {r_eur32*100:.1f}% (annual compounding). If the 1-year FX forward trades at {fm_32:.4f} USD per EUR, borrowing USD to invest in EUR so as to deliver EUR 1,000,000 forward at maturity yields an arbitrage profit at $T = 1$ year closest to:",
        opts, ans,
        f"Equilibrium forward rate is $1.0850 \\times \\frac{{1.048}}{{1.032}} = {fair_32:.6f}$ USD/EUR. Selling EUR 1,000,000 forward at {fm_32:.4f} against borrowing $\\frac{{1,000,000}}{{1.032}} \\times 1.0850$ USD locks in $1,000,000 \\times ({fm_32:.4f} - {fair_32:.6f}) = \\text{{USD }} {prof_usd32:,.0f}$ at $T=1$.",
        dist,
    )

    # 033 (Conceptual)
    opts, ans, dist = build_text_opts(
        "Futures prices exceed current spot prices (contango) while futures prices remain below expected future spot prices (normal backwardation)",
        "Spot prices exceed futures prices (contango) while expected future spot prices are below futures prices",
        "Contango means F0 > S0 (not S0 > F0), and normal backwardation means F0 < E(ST).",
        "Futures prices must always equal expected future spot prices regardless of hedging pressure",
        "Hedging pressure and risk premiums cause F0 to diverge from E(ST) under Keynes's normal backwardation theory.",
        "B",
    )
    add_l1(
        qs, "L1-DRV-033", SUBJECT, m4, t4, "Contango vs. Normal Backwardation",
        "Distinguish contango from backwardation and normal backwardation.",
        "A commodity market exhibits high storage costs, zero convenience yield, and heavy producer short-hedging pressure demanding a risk premium for speculators. Simultaneously, this market can display:",
        opts, ans,
        "Contango ($F_0 > S_0$) reflects positive net carry ($r + c - \\gamma > 0$), whereas normal backwardation ($F_0 < E(S_T)$) occurs when short hedgers induce a downward bias below expected future spot prices to compensate long speculators.",
        dist,
    )

    # 034 (Numerical)
    s0_34, f0_34 = 100.0, 102.40
    imp_r34 = (f0_34 / s0_34) ** 2 - 1.0
    opts, ans, dist = build_num_opts(
        imp_r34,
        (f0_34 / s0_34 - 1.0) * 2.0, "4.80% uses simple annualization instead of discrete annual compounding.",
        (f0_34 / s0_34 - 1.0), "2.40% is the unannualized 6-month return rather than the annualized implied risk-free rate.",
        lambda v: _fmt_pct(v, 2),
    )
    add_num_l1(
        qs, "L1-DRV-034", SUBJECT, m4, t4, "Synthetic Risk-Free Asset",
        "Compute the implied risk-free rate from spot and forward replication.",
        f"A non-dividend-paying stock trades at USD {s0_34:.2f}, and its 6-month ($T = 0.5$) forward contract trades at USD {f0_34:.2f}. Buying the stock and shorting the forward creates a synthetic 6-month risk-free bond with an annualized (discrete compound) implied risk-free rate closest to:",
        opts, ans,
        f"The synthetic bond earns $102.40 / 100.00 - 1 = 2.40\\%$ over 6 months. Compounding annually: $(1.024)^2 - 1 = {imp_r34*100:.2f}\\%$.",
        dist,
    )

    # 035 (Numerical)
    b0_35, cpn_35, r_35 = 1020.0, 25.0, 0.044
    pvc_35 = cpn_35 / ((1.0 + r_35) ** 0.25)
    f0_35 = (b0_35 - pvc_35) * ((1.0 + r_35) ** 0.50)
    opts, ans, dist = build_num_opts(
        f0_35,
        (b0_35 + pvc_35) * ((1.0 + r_35) ** 0.50), "Adds the coupon PV instead of subtracting it as a carry benefit.",
        b0_35 * ((1.0 + r_35) ** 0.50), "Ignores the USD 25 coupon received at t = 0.25 years.",
        lambda v: _fmt_usd(v, 2),
    )
    add_num_l1(
        qs, "L1-DRV-035", SUBJECT, m4, t4, "Fixed-Income Carry",
        "Compute the forward price on a coupon-bearing bond.",
        f"A corporate bond has a full spot price of USD {b0_35:,.2f} and pays a coupon of USD {cpn_35:.2f} in 3 months ($t = 0.25$). Assuming an annual discrete risk-free rate of {r_35*100:.1f}%, the 6-month ($T = 0.50$) full forward price of the bond is closest to:",
        opts, ans,
        f"$PV_0(C) = 25.00 / (1.044)^{{0.25}} = \\text{{USD }} {pvc_35:.4f}$. Thus $F_0(0.5) = (1,020.00 - {pvc_35:.4f})(1.044)^{{0.5}} = \\text{{USD }} {f0_35:,.2f}$.",
        dist,
    )

    # 036 (Numerical)
    s0_36, r_36, q1_36, q2_36 = 5000.0, 0.045, 0.015, 0.025
    f1_36 = s0_36 * math.exp(r_36 - q1_36)
    f2_36 = s0_36 * math.exp(r_36 - q2_36)
    chg_36 = f2_36 - f1_36
    opts, ans, dist = build_num_opts(
        chg_36,
        -chg_36, "+51.27 reverses the direction; higher dividend yield reduces the forward price.",
        s0_36 * (q2_36 - q1_36) * -1.0 - 10.0, "Approximates without exponential carry adjustment.",
        lambda v: f"{v:+.2f} pts",
    )
    # Better d2 for 036: -0.01 * f1_36 or +100
    d2_36 = s0_36 * (math.exp(r_36 + q2_36) - math.exp(r_36 + q1_36))
    opts, ans, dist = build_num_opts(
        chg_36,
        -chg_36, "+51.27 incorrectly predicts an increase when dividend yield rises.",
        -s0_36 * 0.01, "-50.00 estimates the drop using simple multiplication without exponential compounding.",
        lambda v: f"{v:+.2f} pts",
    )
    add_num_l1(
        qs, "L1-DRV-036", SUBJECT, m4, t4, "Forward Carry Sensitivity",
        "Assess how a change in dividend yield alters an index forward price.",
        f"A 1-year equity index forward is priced with spot index level {s0_36:,.0f} and continuous risk-free rate {r_36*100:.1f}%. If the continuous dividend yield rises from {q1_36*100:.1f}% to {q2_36*100:.1f}% while spot and rates remain constant, the fair forward index level changes by:",
        opts, ans,
        f"Initially $F_0 = 5,000 e^{{0.045 - 0.015}} = {f1_36:,.2f}$. After the yield increases, $F_0' = 5,000 e^{{0.045 - 0.025}} = {f2_36:,.2f}$, a change of ${chg_36:+.2f}$ index points.",
        dist,
    )

    # LM5 (037-046): Forward Valuation & FRAs
    m5, t5 = "DRV-LM5", "Pricing and Valuation of Forward Contracts"

    # 037 (Numerical)
    s0_37, r_37, st_37 = 64.0, 0.05, 70.0
    f0_37 = s0_37 * (1.0 + r_37)
    vt_37 = st_37 - f0_37 / ((1.0 + r_37) ** 0.75)
    opts, ans, dist = build_num_opts(
        vt_37,
        st_37 - f0_37, "USD 2.80 fails to discount the original forward price over the remaining 0.75-year maturity.",
        st_37 - s0_37, "USD 6.00 ignores the risk-free financing cost embedded in the forward price.",
        lambda v: _fmt_usd(v, 2),
    )
    add_num_l1(
        qs, "L1-DRV-037", SUBJECT, m5, t5, "Mid-Life Forward Value",
        "Calculate the mark-to-market value of a forward contract during its life.",
        f"Three months ago ($t = 0$), an investor entered a long 1-year forward contract on a non-dividend-paying stock at the no-arbitrage price when spot was USD {s0_37:.2f}. The annual discrete risk-free rate remains constant at {r_37*100:.1f}%. If the stock now trades at USD {st_37:.2f} (with 9 months remaining), the value of the long forward per share is closest to:",
        opts, ans,
        f"Original forward price was $F_0 = 64.00(1.05) = \\text{{USD }} {f0_37:.2f}$. Mid-life value at $t = 0.25$ ($T - t = 0.75$) is $V_t = S_t - \\frac{{F_0}}{{(1+r)^{{0.75}}}} = 70.00 - \\frac{{67.20}}{{(1.05)^{{0.75}}}} = \\text{{USD }} {vt_37:.2f}$.",
        dist,
    )

    # 038 (Numerical)
    s0_38, d_38, r_38, st_38 = 110.0, 3.00, 0.04, 115.0
    pvd_38 = d_38 / (1.0 + r_38) ** 0.25
    f0_38 = (s0_38 - pvd_38) * (1.0 + r_38) ** 0.75
    vt_long38 = st_38 - f0_38 / (1.0 + r_38) ** 0.25
    vt_short38 = -vt_long38
    opts, ans, dist = build_num_opts(
        vt_short38,
        vt_long38, f"+USD {vt_long38:.2f} represents the long forward value rather than the short forward value.",
        -(st_38 - pvd_38 - f0_38 / (1.0 + r_38) ** 0.25), "Incorrectly deducts the past t = 0.25 dividend again at t = 0.50.",
        lambda v: _fmt_usd(v, 2),
    )
    add_num_l1(
        qs, "L1-DRV-038", SUBJECT, m5, t5, "Short Forward Mid-Life",
        "Value a short equity forward after a discrete dividend has been paid.",
        f"Six months ago ($t = 0$), a trader shorted a 9-month equity forward when spot was USD {s0_38:.2f}. A discrete dividend of USD {d_38:.2f} was expected (and paid) at $t = 0.25$ years. The annual discrete risk-free rate remains {r_38*100:.1f}%. Today at $t = 0.50$ years (3 months remaining), the stock trades at USD {st_38:.2f}. The value of the short forward per share is closest to:",
        opts, ans,
        f"Initial forward price was $F_0 = (110.00 - 3.00/1.04^{{0.25}})(1.04)^{{0.75}} = \\text{{USD }} {f0_38:.4f}$. Because the dividend is already paid, remaining benefits = 0 at $t=0.50$. Thus $V_t(\\text{{short}}) = \\frac{{F_0}}{{(1.04)^{{0.25}}}} - S_t = {f0_38/(1.04**0.25):.4f} - 115.00 = -\\text{{USD }} {abs(vt_short38):.2f}$.",
        dist,
    )

    # 039 (Numerical)
    f0_39, st_39 = 85.40, 79.10
    v_exp39 = f0_39 - st_39
    opts, ans, dist = build_num_opts(
        v_exp39,
        -v_exp39, "-USD 6.30 is the value of the long forward at expiration, not the short position.",
        st_39, "USD 79.10 is the terminal spot price rather than the short forward's settlement value.",
        lambda v: _fmt_usd(v, 2),
    )
    add_num_l1(
        qs, "L1-DRV-039", SUBJECT, m5, t5, "Expiration Value",
        "Determine forward contract value at maturity.",
        f"A trader holds a short forward contract with a contract delivery price of USD {f0_39:.2f}. At expiration, the underlying asset trades at USD {st_39:.2f}. What is the value of the short forward contract per unit at expiration?",
        opts, ans,
        f"At expiration ($t = T$), no discounting remains: $V_T(\\text{{short}}) = F_0(T) - S_T = 85.40 - 79.10 = \\text{{USD }} {v_exp39:.2f}$.",
        dist,
    )

    # 040 (Numerical)
    s0_40, q_40, r_40, st_40 = 3200.0, 0.02, 0.045, 3350.0
    f0_40 = s0_40 * math.exp((r_40 - q_40) * 1.0)
    vt_40 = st_40 * math.exp(-q_40 * 0.5) - f0_40 * math.exp(-r_40 * 0.5)
    opts, ans, dist = build_num_opts(
        vt_40,
        st_40 - f0_40 * math.exp(-r_40 * 0.5), "Omits discounting spot by the remaining continuous dividend yield exp(-q(T-t)).",
        st_40 - f0_40, "Takes the undiscounted difference between current spot and original forward price.",
        lambda v: _fmt_num(v, 2),
    )
    add_num_l1(
        qs, "L1-DRV-040", SUBJECT, m5, t5, "Continuous Index Forward",
        "Value an equity index forward mid-life under continuous compounding.",
        f"Six months ago, an institution entered a long 1-year forward contract on an index trading at {s0_40:,.0f}, with continuous dividend yield {q_40*100:.1f}% and continuous risk-free rate {r_40*100:.1f}%. Today, with 6 months remaining, the index is at {st_40:,.0f} (rates unchanged). The value per index unit is closest to:",
        opts, ans,
        f"At $t=0$, $F_0 = 3,200 e^{{0.045 - 0.02}} = {f0_40:,.4f}$. At $t = 0.5$ ($T - t = 0.5$), $V_t(\\text{{long}}) = S_t e^{{-q(T-t)}} - F_0 e^{{-r(T-t)}} = 3,350 e^{{-0.01}} - {f0_40:,.4f} e^{{-0.0225}} = {vt_40:,.2f}$.",
        dist,
    )

    # 041 (Numerical)
    fc_41, f0_41, r_41 = 100.0, 104.50, 0.045
    v0_41 = (f0_41 - fc_41) / (1.0 + r_41)
    opts, ans, dist = build_num_opts(
        v0_41,
        f0_41 - fc_41, "USD 4.50 fails to discount the price advantage from maturity back to t = 0.",
        -v0_41, "-USD 4.31 reverses the sign; contracting below the fair forward price creates positive value for the long.",
        lambda v: _fmt_usd(v, 2),
    )
    add_num_l1(
        qs, "L1-DRV-041", SUBJECT, m5, t5, "Off-Market Forward",
        "Calculate the initial value of an off-market forward contract.",
        f"The fair 1-year forward price on a stock is USD {f0_41:.2f}, and the 1-year discrete risk-free rate is {r_41*100:.1f}%. If two parties execute an off-market 1-year forward contract at a delivery price of USD {fc_41:.2f}, the value of this contract to the long party at initiation is:",
        opts, ans,
        f"The long party secures a guaranteed USD 4.50 saving at $T = 1$, so initial value is $V_0 = \\frac{{F_0 - F_{{\\text{{contract}}}}}}{{1 + r}} = \\frac{{104.50 - 100.00}}{{1.045}} = \\text{{USD }} {v0_41:.2f}$.",
        dist,
    )

    # 042 (Numerical)
    l90, l180 = 0.044, 0.048
    fra_42 = (((1.0 + l180 * 0.5) / (1.0 + l90 * 0.25)) - 1.0) / 0.25
    opts, ans, dist = build_num_opts(
        fra_42,
        ((1.0 + l180 * 0.5) / (1.0 + l90 * 0.25)) - 1.0, "1.29% is the unannualized 90-day forward rate rather than the annualized FRA rate.",
        (l180 + l90) / 2.0, "4.60% averages the two spot rates instead of solving via forward compounding.",
        lambda v: _fmt_pct(v, 2),
    )
    add_num_l1(
        qs, "L1-DRV-042", SUBJECT, m5, t5, "FRA Pricing",
        "Compute a 3x6 FRA fixed rate from spot MRR rates.",
        f"Using a 30/360 convention, annualized 90-day MRR is {l90*100:.2f}% and annualized 180-day MRR is {l180*100:.2f}%. What is the equilibrium annualized fixed rate on a $3 \\times 6$ FRA?",
        opts, ans,
        f"Equilibrium $3 \\times 6$ FRA rate satisfies $(1 + L_{{90}} \\cdot 0.25)(1 + FRA \\cdot 0.25) = 1 + L_{{180}} \\cdot 0.50$. Thus $FRA = \\left(\\frac{{1 + 0.048(0.5)}}{{1 + 0.044(0.25)}} - 1\\right) \\times 4 = {fra_42*100:.2f}\\%$.",
        dist,
    )

    # 043 (Numerical)
    np_43, fra0_43, mr_43 = 10_000_000.0, 0.046, 0.051
    pay_43 = np_43 * ((mr_43 - fra0_43) * 0.5) / (1.0 + mr_43 * 0.5)
    opts, ans, dist = build_num_opts(
        pay_43,
        np_43 * (mr_43 - fra0_43) * 0.5, "USD 25,000 omits discounting the advance settlement over the 180-day borrowing period.",
        np_43 * (mr_43 - fra0_43) / (1.0 + mr_43 * 0.5), "USD 48,757 forgets to scale the annualized rate spread by 180/360 = 0.5.",
        lambda v: _fmt_usd(v, 0),
    )
    add_num_l1(
        qs, "L1-DRV-043", SUBJECT, m5, t5, "FRA Settlement Payoff",
        "Calculate the settlement payoff on a long FRA at expiration.",
        f"A corporation is long a $3 \\times 9$ FRA on USD 10,000,000 notional at a contract rate of {fra0_43*100:.2f}% (30/360). At FRA expiration ($t = 90$ days), 180-day MRR resets at {mr_43*100:.2f}%. What cash settlement does the long party receive at $t = 90$ days?",
        opts, ans,
        f"Because an FRA settles in advance at expiration ($t=90$), the interest differential is discounted over 180 days ($0.5$ yr): $\\text{{Payoff}} = 10,000,000 \\times \\frac{{(0.051 - 0.046)(0.5)}}{{1 + 0.051(0.5)}} = \\text{{USD }} {pay_43:,.0f}$.",
        dist,
    )

    # 044 (Numerical)
    # Replicating a 6x12 FRA on USD 1M: borrow 6M at 4.0%, lend 12M at 4.6%
    # At T=6M, repay USD 1M*(1+0.04*0.5)=1.02M; synthetic borrowing rate for next 6M:
    r6_44, r12_44 = 0.040, 0.046
    syn_44 = (((1.0 + r12_44) / (1.0 + r6_44 * 0.5)) - 1.0) * 2.0
    opts, ans, dist = build_num_opts(
        syn_44,
        (r12_44 - r6_44) * 2.0, "1.20% takes the simple spread difference rather than compounding the ratio of spot factors.",
        ((1.0 + r12_44) / (1.0 + r6_44 * 0.5)) - 1.0, "2.55% is the unannualized 6-month forward rate rather than the annualized 6x12 rate.",
        lambda v: _fmt_pct(v, 2),
    )
    add_num_l1(
        qs, "L1-DRV-044", SUBJECT, m5, t5, "Synthetic FRA Replication",
        "Derive a 6x12 forward rate via spot borrowing and lending.",
        f"If the 6-month spot MRR is {r6_44*100:.2f}% and the 12-month spot MRR is {r12_44*100:.2f}% (30/360), what annualized synthetic $6 \\times 12$ borrowing rate is locked in by lending for 12 months and borrowing for 6 months?",
        opts, ans,
        f"Lending for 12 months and borrowing for 6 months locks in an annualized $6 \\times 12$ rate of $\\left(\\frac{{1 + 0.046(1.0)}}{{1 + 0.040(0.5)}} - 1\\right) \\times 2 = \\left(\\frac{{1.046}}{{1.020}} - 1\\right) \\times 2 = {syn_44*100:.2f}\\%$.",
        dist,
    )

    # 045 (Numerical)
    np_e45, f0_45, st_45, rusd_45, reur_45 = 1_000_000.0, 1.0900, 1.1180, 0.048, 0.030
    # Remaining 0.5 yr Act/360 simple
    ft_45 = st_45 * (1.0 + rusd_45 * 0.5) / (1.0 + reur_45 * 0.5)
    vt_45 = np_e45 * (ft_45 - f0_45) / (1.0 + rusd_45 * 0.5)
    opts, ans, dist = build_num_opts(
        vt_45,
        np_e45 * (st_45 - f0_45), "USD 28,000 fails to discount the EUR leg by the EUR rate and the forward price by the USD rate.",
        np_e45 * (ft_45 - f0_45), f"USD {np_e45*(ft_45-f0_45):,.0f} forgets to discount the future FX difference back from maturity to t = 0.5.",
        lambda v: _fmt_usd(v, 0),
    )
    add_num_l1(
        qs, "L1-DRV-045", SUBJECT, m5, t5, "FX Forward Valuation",
        "Value an existing currency forward contract mid-life.",
        f"A US investor holds a long 1-year forward to buy EUR 1,000,000 at {f0_45:.4f} USD per EUR. Six months later (with 180 days remaining, Act/360), the spot rate is {st_45:.4f} USD per EUR, the 180-day USD rate is {rusd_45*100:.1f}%, and the 180-day EUR rate is {reur_45*100:.1f}%. The mark-to-market value of the contract is closest to:",
        opts, ans,
        f"PV of EUR leg in USD is $\\frac{{1,000,000}}{{1 + 0.03(0.5)}} \\times 1.1180 = \\text{{USD }} {np_e45*st_45/(1+reur_45*0.5):,.2f}$, minus PV of USD payable $\\frac{{1,090,000}}{{1 + 0.048(0.5)}} = \\text{{USD }} {np_e45*f0_45/(1+rusd_45*0.5):,.2f}$, yielding $\\text{{USD }} {vt_45:,.0f}$.",
        dist,
    )

    # 046 (Conceptual)
    opts, ans, dist = build_text_opts(
        "The contract price is set so PV of expected delivery equals spot value; value begins at zero and becomes positive for the party favored by subsequent spot or rate moves",
        "The forward price equals zero at initiation and rises linearly until reaching the spot price at expiration",
        "The forward price is non-zero (equal to spot compounded by net carry); it is the forward contract value that starts at zero.",
        "Forward contract value always equals the forward price minus the spot price throughout its entire life",
        "Mid-life value equals discounted new forward minus old forward, not Ft minus St.",
        "B",
    )
    add_l1(
        qs, "L1-DRV-046", SUBJECT, m5, t5, "Price vs. Value Dynamics",
        "Distinguish forward price from forward value over the contract lifecycle.",
        "Which statement accurately explains the relationship between a forward contract's price and its mark-to-market value from initiation to expiration?",
        opts, ans,
        "At initiation, the delivery price $F_0(T)$ is chosen so that no cash changes hands and contract value $V_0 = 0$. Over the contract's life, $F_0(T)$ stays fixed while $V_t$ fluctuates with $S_t$ and interest rates—creating asymmetric credit exposure for the winning side.",
        dist,
    )

    # LM6 (047-054): Futures Pricing & Margin
    m6, t6 = "DRV-LM6", "Pricing and Valuation of Futures Contracts"

    # 047 (Numerical)
    n_47, mult_47, im_47, mm_47 = 4, 50.0, 13_200.0, 12_000.0
    p0_47, p1_47, p2_47 = 5200.0, 5185.0, 5168.0
    bal0 = n_47 * im_47
    bal2 = bal0 + n_47 * mult_47 * (p2_47 - p0_47)
    mcall_47 = bal0 - bal2
    # Check maintenance trigger: bal0 = 52800, maint = 48000, drop = 32 * 200 = 6400 -> bal2 = 46400 < 48000! Call restores to initial = 6400!
    opts, ans, dist = build_num_opts(
        mcall_47,
        n_47 * mm_47 - bal2, "USD 1,600 restores the margin account only to maintenance margin instead of initial margin.",
        n_47 * mult_47 * (p1_47 - p2_47), "USD 3,400 includes only Day 2's MTM loss rather than the cumulative variation call back to initial margin.",
        lambda v: _fmt_usd(v, 0),
    )
    add_num_l1(
        qs, "L1-DRV-047", SUBJECT, m6, t6, "Margin Call Mechanics",
        "Calculate variation margin calls under daily mark-to-market.",
        f"A trader goes long {n_47} equity index futures (multiplier USD {mult_47:.0f}) at {p0_47:,.0f}, posting initial margin of USD {im_47:,.0f}/contract and maintenance margin of USD {mm_47:,.0f}/contract. Futures settle at {p1_47:,.0f} on Day 1 and {p2_47:,.0f} on Day 2. What variation margin must the trader deposit after Day 2?",
        opts, ans,
        f"Initial equity is $4 \\times 13,200 = \\text{{USD }} {bal0:,.0f}$ (total maintenance = USD 48,000). Cumulative loss by Day 2 is $4 \\times 50 \\times (5,168 - 5,200) = -\\text{{USD }} 6,400$, leaving USD {bal2:,.0f} (< USD 48,000). A margin call restores the balance to initial margin: $\\text{{USD }} 52,800 - \\text{{USD }} 46,400 = \\text{{USD }} {mcall_47:,.0f}$.",
        dist,
    )

    # 048 (Numerical)
    n_48, pf0, pf1 = 12, 95.32, 95.48
    bps_48 = round((pf1 - pf0) * 100)
    gain_48 = n_48 * bps_48 * 25.0
    opts, ans, dist = build_num_opts(
        gain_48,
        -gain_48, "-USD 4,800 reverses the sign; a rise in interest rate futures prices generates a gain for a long position.",
        gain_48 * 4.0, "USD 19,200 fails to apply the 90/360 (0.25 year) day-count multiplier to the USD 1,000,000 notional.",
        lambda v: _fmt_usd(v, 0),
    )
    add_num_l1(
        qs, "L1-DRV-048", SUBJECT, m6, t6, "Interest Rate Futures",
        "Calculate dollar P&L on 3-month SOFR interest rate futures.",
        f"A portfolio manager goes long {n_48} 3-month SOFR futures contracts (USD 1,000,000 notional, USD 25 per basis point) at a quoted price of {pf0:.2f}. If implied 3-month rates fall by {bps_48} bps and the futures settle at {pf1:.2f}, the manager's total dollar gain or loss is:",
        opts, ans,
        f"When rates drop by {bps_48} bps, the futures price rises by {bps_48} bps ($95.48 - 95.32 = +0.16$). Total gain for the long position is $12 \\times 16 \\times \\text{{USD }} 25 = \\text{{USD }} {gain_48:,.0f}$.",
        dist,
    )

    # 049 (Numerical)
    b0_49, ai0_49, r_49, ait_49, cf_49 = 104.20, 1.15, 0.048, 2.35, 1.0520
    qfp_49 = ((b0_49 + ai0_49) * ((1.0 + r_49) ** 0.25) - ait_49) / cf_49
    opts, ans, dist = build_num_opts(
        qfp_49,
        ((b0_49 + ai0_49) * ((1.0 + r_49) ** 0.25) - ait_49), "Omits dividing the clean forward price by the bond's conversion factor.",
        ((b0_49 * ((1.0 + r_49) ** 0.25)) - ait_49) / cf_49, "Omits initial accrued interest AI0 when forming the full spot price.",
        lambda v: _fmt_num(v, 2),
    )
    add_num_l1(
        qs, "L1-DRV-049", SUBJECT, m6, t6, "Treasury Futures Pricing",
        "Calculate the quoted Treasury bond futures price using conversion factors.",
        f"A Treasury bond has a clean spot price of {b0_49:.2f}, accrued interest of {ai0_49:.2f}, and a conversion factor of {cf_49:.4f}. A futures contract expires in 3 months ($T = 0.25$) with no intervening coupon, at which point accrued interest will be {ait_49:.2f}. If the annual discrete risk-free rate is {r_49*100:.1f}%, the equilibrium quoted futures price is closest to:",
        opts, ans,
        f"Full spot price $= 104.20 + 1.15 = 105.35$. Full forward price $= 105.35(1.048)^{{0.25}} = {105.35*(1.048**0.25):.4f}$. Subtracting $AI_T = 2.35$ and dividing by $CF = 1.0520$ yields $QFP = {qfp_49:.2f}$.",
        dist,
    )

    # 050 (Conceptual)
    opts, ans, dist = build_text_opts(
        "The futures price will exceed the forward price because mark-to-market gains occur when reinvestment interest rates are higher",
        "The forward price will exceed the futures price because daily margining imposes higher financing costs on long positions",
        "Positive correlation favors daily mark-to-market futures over forwards, raising the futures price above the forward price.",
        "Both prices remain identical because no-arbitrage requires convergence at expiration",
        "They converge at expiration, but prior to expiration stochastic rates correlated with the asset create a convexity/MTM timing difference.",
        "C",
    )
    add_l1(
        qs, "L1-DRV-050", SUBJECT, m6, t6, "Futures vs. Forward Pricing",
        "Explain when futures and forward prices diverge due to interest rate correlation.",
        "When underlying asset prices are strongly positively correlated with short-term interest rates, how does a futures price compare with an otherwise identical forward price prior to maturity?",
        opts, ans,
        "If asset prices and interest rates move together positively, long futures holders receive MTM cash inflows when rates are high (reinvesting at higher rates) and fund MTM outflows when rates are low, making futures more desirable and pushing $f_0(T) > F_0(T)$.",
        dist,
    )

    # 051 (Numerical)
    # Multi-day MTM with reinvestment on a 2-day contract
    # Day 1 futures +5 -> earns 10% overnight? Let's do clean numbers:
    # 10 contracts, mult 100. Long at 500. Day 1 settles at 510 (+10,000 cash inflow), reinvested for 1 period at 5% -> +500 interest; Day 2 settles at 506 (-4,000 cash outflow). Total futures wealth = 10,000*1.05 - 4,000 = +6,500 vs forward +6,000.
    mtm1, mtm2, r_re = 10_000.0, -4_000.0, 0.05
    fut_tot = mtm1 * (1.0 + r_re) + mtm2
    opts, ans, dist = build_num_opts(
        fut_tot,
        mtm1 + mtm2, "USD 6,000 represents the terminal payoff of a static forward contract without interest earned on Day 1's MTM inflow.",
        mtm1 * (1.0 + r_re) + mtm2 * (1.0 + r_re), "USD 6,300 erroneously compounds the Day 2 final settlement flow as if it were earned a period earlier.",
        lambda v: _fmt_usd(v, 0),
    )
    add_num_l1(
        qs, "L1-DRV-051", SUBJECT, m6, t6, "MTM Reinvestment Impact",
        "Quantify how daily futures MTM reinvestment alters cumulative payoff.",
        "A trader holds a long position in 10 futures contracts (multiplier USD 100) entered at 500.00. On Day 1, futures settle at 510.00 and the trader reinvests the MTM cash inflow for one period at 5.0%. On Day 2 (expiration), futures settle at 506.00. Total cumulative dollar profit on the futures position including reinvestment interest is:",
        opts, ans,
        f"Day 1 MTM gain is $10 \\times 100 \\times (510 - 500) = \\text{{USD }} 10,000$, growing at 5% to USD 10,500. Day 2 MTM loss is $10 \\times 100 \\times (506 - 510) = -\\text{{USD }} 4,000$. Total cumulative profit is $\\text{{USD }} 10,500 - \\text{{USD }} 4,000 = \\text{{USD }} {fut_tot:,.0f}$ (vs. USD 6,000 for a forward).",
        dist,
    )

    # 052 (Numerical)
    n_52, bbl_52, p0_52, im_52, mm_52 = 2, 1000.0, 76.50, 6500.0, 5800.0
    loss_buf = (im_52 - mm_52) / bbl_52
    trig_p = p0_52 + loss_buf
    opts, ans, dist = build_num_opts(
        trig_p,
        p0_52 - loss_buf, "USD 75.80 applies to a long futures position rather than a short futures position.",
        p0_52 + (im_52 - mm_52) / (n_52 * bbl_52), "USD 76.85 divides the single-contract margin buffer by both contracts combined.",
        lambda v: _fmt_usd(v, 2),
    )
    add_num_l1(
        qs, "L1-DRV-052", SUBJECT, m6, t6, "Short Margin Trigger",
        "Compute the price level triggering a margin call on short commodity futures.",
        f"A speculator shorts {n_52} WTI crude oil futures contracts (1,000 barrels each) at USD {p0_52:.2f}/bbl. Initial margin is USD {im_52:,.0f}/contract and maintenance margin is USD {mm_52:,.0f}/contract. Above what settlement price will the speculator receive a variation margin call?",
        opts, ans,
        f"Per contract, equity drops to maintenance margin after a loss of $\\text{{USD }} 6,500 - \\text{{USD }} 5,800 = \\text{{USD }} 700$, or $\\text{{USD }} 700 / 1,000 = \\text{{USD }} 0.70\\text{{/bbl}}$. Since the position is short, the price rise trigger is $76.50 + 0.70 = \\text{{USD }} {trig_p:.2f}\\text{{/bbl}}$.",
        dist,
    )

    # 053 (Numerical)
    s0_53, pv_div53, r_53 = 5120.0, 22.0, 0.05
    f0_53 = (s0_53 - pv_div53) * ((1.0 + r_53) ** (90.0 / 365.0))
    opts, ans, dist = build_num_opts(
        f0_53,
        (s0_53 + pv_div53) * ((1.0 + r_53) ** (90.0 / 365.0)), "Adds the PV of index dividends rather than subtracting them.",
        s0_53 * ((1.0 + r_53) ** (90.0 / 365.0)), "Omits the 22.00 index-point dividend deduction.",
        lambda v: _fmt_num(v, 2),
    )
    add_num_l1(
        qs, "L1-DRV-053", SUBJECT, m6, t6, "Index Futures Fair Value",
        "Compute fair equity index futures price with dividend index points.",
        f"An equity index is at {s0_53:,.0f} and the present value of dividends expected over the next 90 days equals {pv_div53:.0f} index points. With a discrete annual risk-free rate of {r_53*100:.1f}% (365-day year), the fair 90-day equity index futures level is closest to:",
        opts, ans,
        f"Subtracting dividend PV from spot and compounding for 90 days yields $F_0 = (5,120 - 22)(1.05)^{{90/365}} = {f0_53:,.2f}$.",
        dist,
    )

    # 054 (Conceptual)
    opts, ans, dist = build_text_opts(
        "Daily mark-to-market settlement realizes gains/losses each day and resets the futures contract value to zero",
        "Futures contracts carry a zero delivery price at the end of each trading day",
        "The futures price changes daily to match market equilibrium; it is the futures contract value (MTM) that resets to zero.",
        "Futures counterparties must settle the entire notional principal in cash at the close of every trading day",
        "Only daily price changes (variation margin) are settled in cash, never the full notional principal.",
        "A",
    )
    add_l1(
        qs, "L1-DRV-054", SUBJECT, m6, t6, "Daily Resetting Mechanics",
        "Explain why futures contract value resets to zero daily.",
        "Why does the mark-to-market value of an exchange-traded futures contract reset to zero at the end of every trading day while a forward contract accumulates unrealized value?",
        opts, ans,
        "Daily variation margin settles all gains and losses in cash at each daily settlement price, effectively re-contracting the futures position at the new settlement price so its remaining MTM value equals zero.",
        dist,
    )


def build_l1_lm7_to_lm10(qs: list):
    """LM7 (055-062) Swaps, LM8 (063-073) Options, LM9 (074-079) PCP, LM10 (080-085) 1-Per Binomial."""
    m7, t7 = "DRV-LM7", "Pricing and Valuation of Swaps"

    # 055 (Numerical)
    np_55, fix_55, flt_55 = 20_000_000.0, 0.048, 0.0525
    net_55 = np_55 * (flt_55 - fix_55) * 0.5
    opts, ans, dist = build_num_opts(
        net_55,
        np_55 * (flt_55 - fix_55), "USD 90,000 omits multiplying the annualized rate differential by the 180/360 = 0.50 accrual period.",
        -net_55, "-USD 45,000 represents the net cash flow for the receive-fixed counterparty rather than the pay-fixed party.",
        lambda v: f"Receives USD {v:,.0f}" if v >= 0 else f"Pays USD {abs(v):,.0f}",
    )
    # Build distinct text options for 055 since negative flips label cleanly
    opts, ans, dist = build_text_opts(
        f"Receives USD {net_55:,.0f}",
        f"Pays USD {net_55:,.0f}",
        "Paying fixed 4.80% while receiving floating 5.25% produces a net cash inflow, not an outflow.",
        f"Receives USD {net_55 * 2:,.0f}",
        "USD 90,000 omits applying the 180/360 = 0.50 semi-annual day-count fraction.",
        "B",
    )
    NUM_Q_IDS.add("L1-DRV-055")
    add_l1(
        qs, "L1-DRV-055", SUBJECT, m7, t7, "Swap Net Cash Flow",
        "Calculate the periodic net settlement on an interest rate swap.",
        f"A firm enters a USD 20,000,000 notional semi-annual interest rate swap (30/360) as the pay-fixed party at an annualized fixed rate of {fix_55*100:.2f}%. If 6-month MRR for the first period resets at {flt_55*100:.2f}%, what is the firm's net cash flow on the first settlement date?",
        opts, ans,
        f"Fixed outflow is $20\\text{{M}} \\times 0.048 \\times 0.5 = \\text{{USD }} 480,000$; floating inflow is $20\\text{{M}} \\times 0.0525 \\times 0.5 = \\text{{USD }} 525,000$. Net receipt = $\\text{{USD }} {net_55:,.0f}$.",
        dist,
    )

    # 056 (Conceptual)
    opts, ans, dist = build_text_opts(
        "A series of off-market FRAs priced at a single common fixed rate such that the sum of their initial values equals zero",
        "A series of at-market FRAs each individually having an initial value of zero and identical forward rates",
        "An upward- or downward-sloping yield curve means forward rates vary by maturity, so a single swap rate sets individual FRAs off-market (non-zero initial value) while their sum equals zero.",
        "A portfolio of European interest rate call options expiring on each reset date",
        "Swaps are symmetric forward commitments; interest rate options form caps/floors, not swaps.",
        "A",
    )
    add_l1(
        qs, "L1-DRV-056", SUBJECT, m7, t7, "Swap-FRA Equivalence",
        "Explain the equivalence between an interest rate swap and a series of FRAs.",
        "Economically, a plain-vanilla interest rate swap at initiation is equivalent to:",
        opts, ans,
        "A swap exchanges multiple fixed-rate cash flows at a single constant swap rate against floating rates, replicating a strip of off-market FRAs whose individual initial values (positive and negative) sum exactly to zero at inception.",
        dist,
    )

    # 057 (Numerical)
    s05_57, s10_57 = 0.042, 0.046
    df1_57 = 1.0 / (1.0 + s05_57 * 0.5)
    df2_57 = 1.0 / (1.0 + s10_57 * 1.0)
    fix_per57 = (1.0 - df2_57) / (df1_57 + df2_57)
    fix_ann57 = fix_per57 * 2.0
    opts, ans, dist = build_num_opts(
        fix_ann57,
        fix_per57, f"{fix_per57*100:.2f}% is the semi-annual periodic coupon rate rather than the annualized swap fixed rate.",
        (s05_57 + s10_57) / 2.0, "4.40% takes the simple arithmetic mean of spot rates instead of using discount factors.",
        lambda v: _fmt_pct(v, 2),
    )
    add_num_l1(
        qs, "L1-DRV-057", SUBJECT, m7, t7, "Swap Fixed Rate",
        "Compute the fixed rate on a 1-year semi-annual interest rate swap.",
        f"Annualized spot MRR rates (30/360) are {s05_57*100:.2f}% for 180 days and {s10_57*100:.2f}% for 360 days. What is the annualized fixed swap rate on a 1-year semi-annual plain-vanilla interest rate swap?",
        opts, ans,
        f"$DF_1 = 1/(1 + 0.042(0.5)) = {df1_57:.6f}$ and $DF_2 = 1/(1 + 0.046(1.0)) = {df2_57:.6f}$. Periodic rate $= \\frac{{1 - DF_2}}{{DF_1 + DF_2}} = {fix_per57*100:.4f}\\%$, so annualized swap rate $= 2 \\times {fix_per57*100:.4f}\\% = {fix_ann57*100:.2f}\\%$.",
        dist,
    )

    # 058 (Numerical)
    pv_fix58, pv_flt58 = 10_240_000.0, 10_080_000.0
    val_pay58 = pv_flt58 - pv_fix58
    opts, ans, dist = build_num_opts(
        val_pay58,
        pv_fix58 - pv_flt58, "+USD 160,000 is the MTM value to the receive-fixed party rather than the pay-fixed party.",
        -(pv_fix58 - 10_000_000.0), "-USD 240,000 assumes the floating leg equals par mid-period.",
        lambda v: _fmt_usd(v, 0),
    )
    add_num_l1(
        qs, "L1-DRV-058", SUBJECT, m7, t7, "Bond Replication Value",
        "Value an interest rate swap using fixed and floating bond values.",
        "A corporation is the pay-fixed, receive-floating counterparty on a USD 10,000,000 notional swap. Between reset dates, the present value of the fixed-rate bond leg is USD 10,240,000 and the present value of the floating-rate bond leg is USD 10,080,000. What is the swap's MTM value to the corporation?",
        opts, ans,
        f"Pay-fixed equals long floating bond minus short fixed bond: $V(\\text{{pay-fixed}}) = V_{{\\text{{float}}}} - V_{{\\text{{fixed}}}} = 10,080,000 - 10,240,000 = -\\text{{USD }} {abs(val_pay58):,.0f}$.",
        dist,
    )

    # 059 (Numerical)
    usd_np59, s0_59, r_usd59, r_eur59 = 11_000_000.0, 1.10, 0.048, 0.032
    eur_np59 = usd_np59 / s0_59
    eur_cpn59 = eur_np59 * r_eur59
    usd_cpn59 = usd_np59 * r_usd59
    opts, ans, dist = build_text_opts(
        f"Pay EUR {eur_cpn59:,.0f}; receive USD {usd_cpn59:,.0f} (gross, no netting)",
        f"Pay USD {usd_cpn59:,.0f}; receive EUR {eur_cpn59:,.0f} (gross, no netting)",
        "Reverses the cash flow direction; the firm receives USD fixed and pays EUR fixed.",
        f"Pay EUR {eur_np59 * r_usd59:,.0f}; receive USD {usd_np59 * r_eur59:,.0f}",
        "Applies the USD coupon rate to EUR principal and the EUR coupon rate to USD principal.",
        "C",
    )
    NUM_Q_IDS.add("L1-DRV-059")
    add_l1(
        qs, "L1-DRV-059", SUBJECT, m7, t7, "Currency Swap Cash Flows",
        "Determine periodic coupon exchanges in a fixed-for-fixed currency swap.",
        f"At spot {s0_59:.2f} USD per EUR, a firm enters a currency swap to pay EUR fixed at {r_eur59*100:.1f}% and receive USD fixed at {r_usd59*100:.1f}% annually on USD {usd_np59:,.0f} notional. What are the Year 1 coupon cash flows for the firm?",
        opts, ans,
        f"EUR notional $= \\text{{USD }} 11,000,000 / 1.10 = \\text{{EUR }} {eur_np59:,.0f}$. Because currency swap coupons are denominated in different currencies, they are exchanged gross: pay $0.032 \\times 10,000,000 = \\text{{EUR }} {eur_cpn59:,.0f}$ and receive $0.048 \\times 11,000,000 = \\text{{USD }} {usd_cpn59:,.0f}$.",
        dist,
    )

    # 060 (Conceptual)
    opts, ans, dist = build_text_opts(
        "A currency swap exchanges notional principals at maturity, concentrating credit exposure at the end, whereas an IRS does not exchange notional",
        "An interest rate swap exchanges notional principals at maturity whereas a currency swap never exchanges notional",
        "This reverses the two instruments; IRS notionals are never exchanged, whereas currency swap notionals are typically exchanged at both initiation and maturity.",
        "Currency swaps require daily exchange-traded variation margin that eliminates credit exposure entirely",
        "Standard cross-currency swaps are OTC instruments whose principal exchanges create peak credit exposure late in the swap's life.",
        "A",
    )
    add_l1(
        qs, "L1-DRV-060", SUBJECT, m7, t7, "Swap Credit Risk Profile",
        "Compare counterparty credit risk across interest rate swaps and currency swaps.",
        "Why does a fixed-for-fixed currency swap carry substantially higher counterparty credit exposure near maturity than a plain-vanilla interest rate swap?",
        opts, ans,
        "In a plain-vanilla IRS, only interest differentials are netted and credit risk peaks mid-life before amortizing toward zero. In a currency swap, full notional principals in two currencies are re-exchanged at maturity, creating large terminal FX credit exposure.",
        dist,
    )

    # 061 (Numerical)
    np_61, c0_61, c1_61, sum_df61 = 50_000_000.0, 0.040, 0.046, 3.912
    val_pay61 = np_61 * ((c1_61 - c0_61) / 4.0) * sum_df61
    opts, ans, dist = build_num_opts(
        val_pay61,
        -val_pay61, f"-USD {val_pay61:,.0f} represents the value to the receive-fixed party rather than the pay-fixed party.",
        val_pay61 * 4.0, f"USD {val_pay61*4:,.0f} forgets to divide the annualized coupon spread by 4 for quarterly settlement.",
        lambda v: _fmt_usd(v, 0),
    )
    add_num_l1(
        qs, "L1-DRV-061", SUBJECT, m7, t7, "Mid-Life Swap Value",
        "Value an interest rate swap mid-life using updated par swap rates.",
        f"A pay-fixed quarterly swap on USD 50,000,000 notional has a contract fixed rate of {c0_61*100:.2f}% and exactly 1 year (4 quarters) remaining on a reset date. The current 1-year par swap rate is {c1_61*100:.2f}%, and the sum of the four quarterly discount factors is {sum_df61:.3f}. The swap's MTM value to the pay-fixed party is closest to:",
        opts, ans,
        f"The pay-fixed party saves $(4.60\\% - 4.00\\%)/4 = 0.15\\%$ per quarter compared with a new swap. PV of savings $= 50,000,000 \\times 0.0015 \\times 3.912 = \\text{{USD }} {val_pay61:,.0f}$.",
        dist,
    )

    # 062 (Numerical)
    np_62, par_sp62, cpn_62, dur_62 = 10_000_000.0, 0.0180, 0.0100, 4.20
    upf_62 = np_62 * (par_sp62 - cpn_62) * dur_62
    opts, ans, dist = build_num_opts(
        upf_62,
        np_62 * (par_sp62 - cpn_62), "USD 80,000 multiplies the spread by notional without scaling by the 4.20-year credit duration.",
        np_62 * par_sp62 * dur_62, "USD 756,000 ignores the 100 bps standardized fixed coupon paid by the buyer.",
        lambda v: _fmt_usd(v, 0),
    )
    add_num_l1(
        qs, "L1-DRV-062", SUBJECT, m7, t7, "CDS Upfront Pricing",
        "Approximate the upfront premium on a standard CDS contract.",
        "A 5-year CDS on USD 10,000,000 notional carries a standardized coupon of 100 bps while the issuer's par credit spread is 180 bps. Given a CDS credit duration of 4.20 years, the approximate upfront payment from the protection buyer to the seller is:",
        opts, ans,
        f"Upfront payment $\\approx \\text{{Notional}} \\times (\\text{{Par Spread}} - \\text{{Coupon}}) \\times \\text{{EffDur}}_{{\\text{{CDS}}}} = 10,000,000 \\times (0.0180 - 0.0100) \\times 4.20 = \\text{{USD }} {upf_62:,.0f}$.",
        dist,
    )

    # LM8 (063-073): Option Moneyness, Bounds, Determinants
    m8, t8 = "DRV-LM8", "Pricing and Valuation of Options"

    # 063 (Numerical)
    s0_63, xc_63, c_63, xp_63, p_63 = 68.0, 65.0, 5.80, 72.0, 6.40
    tvc_63 = c_63 - max(0.0, s0_63 - xc_63)
    tvp_63 = p_63 - max(0.0, xp_63 - s0_63)
    opts, ans, dist = build_text_opts(
        f"Call time value = USD {tvc_63:.2f}; Put time value = USD {tvp_63:.2f}",
        f"Call time value = USD {s0_63 - xc_63:.2f}; Put time value = USD {xp_63 - s0_63:.2f}",
        "USD 3.00 and USD 4.00 are the options' intrinsic values rather than their time values.",
        f"Call time value = USD {c_63:.2f}; Put time value = USD {p_63:.2f}",
        "USD 5.80 and USD 6.40 are total option premiums rather than time values.",
        "B",
    )
    NUM_Q_IDS.add("L1-DRV-063")
    add_l1(
        qs, "L1-DRV-063", SUBJECT, m8, t8, "Intrinsic and Time Value",
        "Decompose option premiums into intrinsic value and time value.",
        f"A stock trades at USD {s0_63:.2f}. A call with strike USD {xc_63:.2f} trades at USD {c_63:.2f}, and a put with strike USD {xp_63:.2f} trades at USD {p_63:.2f}. What are the time values of the call and put?",
        opts, ans,
        f"Call intrinsic value $= \\max(0, 68 - 65) = 3.00 \\implies \\text{{Call time value}} = 5.80 - 3.00 = \\text{{USD }} {tvc_63:.2f}$. Put intrinsic value $= \\max(0, 72 - 68) = 4.00 \\implies \\text{{Put time value}} = 6.40 - 4.00 = \\text{{USD }} {tvp_63:.2f}$.",
        dist,
    )

    # 064 (Numerical)
    s0_64, x_64, r_64, t_64, cm_64 = 96.0, 90.0, 0.05, 0.50, 7.10
    lb_64 = s0_64 - x_64 / ((1.0 + r_64) ** t_64)
    arb_64 = lb_64 - cm_64
    opts, ans, dist = build_num_opts(
        arb_64,
        (s0_64 - x_64) - cm_64, "Omits discounting the strike price X over 6 months when forming the European lower bound.",
        lb_64, f"USD {lb_64:.2f} is the theoretical lower bound itself, not the arbitrage profit above the USD 7.10 market price.",
        lambda v: _fmt_usd(v, 2),
    )
    add_num_l1(
        qs, "L1-DRV-064", SUBJECT, m8, t8, "Call Lower Bound",
        "Calculate the European call lower bound and arbitrage opportunity.",
        f"A non-dividend-paying stock trades at USD {s0_64:.2f}. A 6-month ($T = 0.50$) European call with strike USD {x_64:.2f} trades at USD {cm_64:.2f} when the annual discrete risk-free rate is {r_64*100:.1f}%. What is the minimum immediate arbitrage profit per share?",
        opts, ans,
        f"European call lower bound is $\\max(0, S_0 - X(1+r)^{{-T}}) = 96.00 - 90.00 / 1.05^{{0.5}} = \\text{{USD }} {lb_64:.4f}$. Buying the underpriced call at USD {cm_64:.2f}, shorting the stock at USD 96, and lending $90/1.05^{{0.5}}$ nets $\\text{{USD }} {lb_64:.4f} - 7.10 = \\text{{USD }} {arb_64:.2f}$ immediately.",
        dist,
    )

    # 065 (Numerical)
    s0_65, x_65, r_65, t_65, pm_65 = 42.0, 48.0, 0.045, 1.0, 3.30
    lb_65 = x_65 / (1.0 + r_65) - s0_65
    arb_65 = lb_65 - pm_65
    opts, ans, dist = build_num_opts(
        arb_65,
        (x_65 - s0_65) - pm_65, "Uses the undiscounted American put intrinsic value instead of discounting X by (1 + r).",
        lb_65, f"USD {lb_65:.2f} equals the European put lower bound rather than the arbitrage profit above USD {pm_65:.2f}.",
        lambda v: _fmt_usd(v, 2),
    )
    add_num_l1(
        qs, "L1-DRV-065", SUBJECT, m8, t8, "Put Lower Bound",
        "Calculate the European put lower bound and arbitrage profit.",
        f"A non-dividend-paying stock trades at USD {s0_65:.2f}. A 1-year European put with strike USD {x_65:.2f} is quoted at USD {pm_65:.2f}, and the 1-year discrete risk-free rate is {r_65*100:.1f}%. What is the immediate arbitrage profit per share from buying the put and stock with borrowed funds?",
        opts, ans,
        f"European put lower bound is $\\max(0, X(1+r)^{{-1}} - S_0) = 48.00 / 1.045 - 42.00 = \\text{{USD }} {lb_65:.4f}$. Buying the put and stock and borrowing $48/1.045$ generates $\\text{{USD }} {lb_65:.4f} - 3.30 = \\text{{USD }} {arb_65:.2f}$ immediately.",
        dist,
    )

    # 066 (Numerical)
    s0_66, x_66, r_66 = 50.0, 60.0, 0.06
    lb_am66 = x_66 - s0_66
    lb_eu66 = x_66 / (1.0 + r_66) - s0_66
    diff_66 = lb_am66 - lb_eu66
    opts, ans, dist = build_num_opts(
        diff_66,
        lb_am66, "USD 10.00 is the American put lower bound itself, not the difference over the European bound.",
        lb_eu66, f"USD {lb_eu66:.2f} is the European put lower bound rather than the excess American bound.",
        lambda v: _fmt_usd(v, 2),
    )
    add_num_l1(
        qs, "L1-DRV-066", SUBJECT, m8, t8, "American vs. European Bound",
        "Compare lower bounds of American and European put options.",
        f"A non-dividend-paying stock trades at USD {s0_66:.2f} with a 1-year discrete risk-free rate of {r_66*100:.1f}%. By how much does the lower bound of a 1-year American put with strike USD {x_66:.2f} exceed that of an otherwise identical European put?",
        opts, ans,
        f"American lower bound $= X - S_0 = \\text{{USD }} 10.00$. European lower bound $= X/(1+r) - S_0 = 60/1.06 - 50 = \\text{{USD }} {lb_eu66:.4f}$. Difference $= 60 - 60/1.06 = \\text{{USD }} {diff_66:.2f}$.",
        dist,
    )

    # 067 (Conceptual)
    opts, ans, dist = build_text_opts(
        "Exercising early forfeits remaining time value and loses the interest earned by deferring payment of the strike price",
        "The American call lower bound falls below zero whenever risk-free rates are positive",
        "Option lower bounds are always non-negative due to limited liability.",
        "Selling the option in the market always yields less than intrinsic value when no dividends are paid",
        "Because time value is non-negative, selling a call on a non-dividend stock in the market yields at least intrinsic value plus interest on X.",
        "A",
    )
    add_l1(
        qs, "L1-DRV-067", SUBJECT, m8, t8, "Early Exercise: American Calls",
        "Explain why American calls on non-dividend stocks are never exercised early.",
        "Why is it never optimal to exercise an American call option early on a stock that pays no dividends?",
        opts, ans,
        "Since $C_t \\ge c_t \\ge S_t - X(1+r)^{-(T-t)} > S_t - X$, selling the call in the open market recovers both intrinsic value and time value—whereas exercising early sacrifices time value and requires paying $X$ sooner.",
        dist,
    )

    # 068 (Conceptual)
    opts, ans, dist = build_text_opts(
        "Deep in-the-money American puts and American calls just prior to a sufficiently large cash dividend",
        "Deep out-of-the-money American calls and at-the-money American puts",
        "Out-of-the-money options have zero intrinsic value and would never be exercised early.",
        "American puts on high-dividend stocks just before an ex-dividend date",
        "A dividend drop pushes the stock price down, increasing put value—so put holders wait until after the ex-dividend drop rather than exercising before it.",
        "C",
    )
    add_l1(
        qs, "L1-DRV-068", SUBJECT, m8, t8, "Early Exercise Conditions",
        "Identify situations where early exercise of American options may be optimal.",
        "Early exercise can be economically optimal for which pair of American options?",
        opts, ans,
        "Deep in-the-money American puts may be exercised early to capture the strike $X$ immediately and earn risk-free interest when upside time value is tiny. American calls may be exercised right before an ex-dividend date if the dividend exceeds forfeited interest and time value.",
        dist,
    )

    # 069 (Numerical)
    x_69, r_69, t_69 = 80.0, 0.05, 0.25
    min_div69 = x_69 * (1.0 - 1.0 / ((1.0 + r_69) ** t_69))
    opts, ans, dist = build_num_opts(
        min_div69,
        x_69 * r_69, "USD 4.00 uses the full-year interest cost instead of the remaining 3-month interest savings.",
        x_69 * ((1.0 + r_69) ** t_69 - 1.0) + 1.00, "USD 1.98 overstates the interest hurdle by adding an arbitrary dollar margin.",
        lambda v: _fmt_usd(v, 2),
    )
    add_num_l1(
        qs, "L1-DRV-069", SUBJECT, m8, t8, "Dividend Early Exercise",
        "Compute the minimum dividend threshold for early American call exercise.",
        f"A deep-in-the-money American call option has strike USD {x_69:.2f} and 3 months ($T = 0.25$) left to expiration immediately after tomorrow's ex-dividend date. Given an annual discrete risk-free rate of {r_69*100:.1f}%, what is the minimum dividend threshold $X - X(1+r)^{{-T}}$ that must be exceeded to justify exercising just before ex-dividend?",
        opts, ans,
        f"Early exercise forfeits the interest saved on delaying $X$, equal to $80 - 80 / (1.05)^{{0.25}} = \\text{{USD }} {min_div69:.2f}$. A dividend smaller than this cannot justify early exercise even if remaining optionality value is zero.",
        dist,
    )

    # 070 (Conceptual)
    opts, ans, dist = build_text_opts(
        "Increases European call values and decreases European put values",
        "Decreases both European call and European put values symmetrically",
        "Higher rates raise the present value advantage of deferring strike payment on calls, increasing call value rather than lowering it.",
        "Increases European put values while leaving European call values unchanged",
        "Via put-call parity c - p = S0 - PV(X), higher risk-free rates raise PV-adjusted forward prices, lifting calls and lowering puts.",
        "B",
    )
    add_l1(
        qs, "L1-DRV-070", SUBJECT, m8, t8, "Option Price Determinants",
        "Explain the effect of interest rate changes on European option prices.",
        "Holding all other factors constant, an increase in the risk-free interest rate generally:",
        opts, ans,
        "Higher risk-free rates lower the present value of the strike price $X(1+r)^{-T}$, raising the value of the right to pay $X$ later (European calls increase) and lowering the value of the right to receive $X$ later (European puts decrease).",
        dist,
    )

    # 071 (Numerical)
    s0_71, x_71, c_71, st_71 = 50.0, 52.0, 2.40, 58.0
    ret_c71 = (st_71 - x_71 - c_71) / c_71
    ret_s71 = (st_71 - s0_71) / s0_71
    opts, ans, dist = build_num_opts(
        ret_c71,
        (st_71 - x_71) / c_71, "250.00% computes gross payoff divided by premium without deducting the USD 2.40 cost.",
        ret_s71, "16.00% is the percentage return on buying the underlying stock directly.",
        lambda v: _fmt_pct(v, 2),
    )
    add_num_l1(
        qs, "L1-DRV-071", SUBJECT, m8, t8, "Option Leverage Return",
        "Compare percentage return of an OTM call option versus direct stock purchase.",
        f"A stock trades at USD {s0_71:.2f} and an out-of-the-money call with strike USD {x_71:.2f} costs USD {c_71:.2f}. If the stock finishes at USD {st_71:.2f} at expiration, what is the percentage return on the call option?",
        opts, ans,
        f"Gross payoff is $58.00 - 52.00 = \\text{{USD }} 6.00$, giving net profit of $6.00 - 2.40 = \\text{{USD }} 3.60$. Percentage return $= 3.60 / 2.40 = {ret_c71*100:.2f}\\%$ (compared with $16.00\\%$ on the stock).",
        dist,
    )

    # 072 (Numerical)
    s0_72, x_72, r_72 = 75.0, 80.0, 0.05
    ub_eu72 = x_72 / (1.0 + r_72)
    opts, ans, dist = build_num_opts(
        ub_eu72,
        x_72, "USD 80.00 is the upper bound of an American put, not a 1-year European put.",
        s0_72, "USD 75.00 is the upper bound of a call option (the stock price) rather than a put option.",
        lambda v: _fmt_usd(v, 2),
    )
    add_num_l1(
        qs, "L1-DRV-072", SUBJECT, m8, t8, "Put Upper Bounds",
        "Identify upper bounds for European and American put options.",
        f"A stock trades at USD {s0_72:.2f} and the 1-year discrete risk-free rate is {r_72*100:.1f}%. What is the theoretical upper bound on the price of a 1-year European put option with strike USD {x_72:.2f}?",
        opts, ans,
        f"Because a European put pays at most $X = \\text{{USD }} 80.00$ at $T = 1$, its price today cannot exceed the discounted strike: $p_0 \\le X/(1+r) = 80.00 / 1.05 = \\text{{USD }} {ub_eu72:.2f}$.",
        dist,
    )

    # 073 (Numerical)
    s0_73, x_73, r1_73, r2_73 = 100.0, 100.0, 0.04, 0.05
    diff1_73 = s0_73 - x_73 / (1.0 + r1_73)
    diff2_73 = s0_73 - x_73 / (1.0 + r2_73)
    chg_73 = diff2_73 - diff1_73
    opts, ans, dist = build_num_opts(
        chg_73,
        -chg_73, "-USD 0.92 reverses the sign; a higher rate lowers PV(X) and widens (c - p).",
        1.00, "USD 1.00 ignores discounting and simply multiplies USD 100 by the 1% rate change.",
        lambda v: f"{v:+.2f} USD",
    )
    add_num_l1(
        qs, "L1-DRV-073", SUBJECT, m8, t8, "Put-Call Spread Rate Sensitivity",
        "Measure how interest rate shifts affect the c - p price difference.",
        "Consider a 1-year European call and put on a non-dividend stock ($S_0 = X = 100$). If the 1-year discrete risk-free rate rises instantly from 4.0% to 5.0% with no change in $S_0$ or implied volatility, by how much does $(c - p)$ change?",
        opts, ans,
        f"By put-call parity, $c - p = S_0 - X/(1+r)$. At 4%, $c - p = 100 - 100/1.04 = {diff1_73:.4f}$. At 5%, $c - p = 100 - 100/1.05 = {diff2_73:.4f}$. Change $= {chg_73:+.2f}$ USD.",
        dist,
    )

    # LM9 (074-079): Put-Call Parity & Option Replication
    m9, t9 = "DRV-LM9", "Option Replication Using Put-Call Parity"

    # 074 (Numerical)
    s0_74, x_74, c_74, r_74 = 105.0, 100.0, 10.80, 0.048
    p_74 = c_74 + x_74 / ((1.0 + r_74) ** 0.5) - s0_74
    opts, ans, dist = build_num_opts(
        p_74,
        c_74 + x_74 - s0_74, "USD 5.80 omits discounting the strike price over the 6-month maturity.",
        c_74 + x_74 / (1.0 + r_74) - s0_74, "Uses full 1-year discounting instead of T = 0.50 years.",
        lambda v: _fmt_usd(v, 2),
    )
    add_num_l1(
        qs, "L1-DRV-074", SUBJECT, m9, t9, "Put-Call Parity",
        "Solve for a European put price using put-call parity.",
        f"A non-dividend stock trades at USD {s0_74:.2f}. A 6-month ($T = 0.50$) European call with strike USD {x_74:.2f} costs USD {c_74:.2f}. If the annual discrete risk-free rate is {r_74*100:.1f}%, what is the no-arbitrage price of the corresponding 6-month European put?",
        opts, ans,
        f"From $p_0 = c_0 + X(1+r)^{{-T}} - S_0$: $p_0 = 10.80 + 100.00 / (1.048)^{{0.5}} - 105.00 = 10.80 + {x_74/(1.048**0.5):.4f} - 105.00 = \\text{{USD }} {p_74:.2f}$.",
        dist,
    )

    # 075 (Numerical)
    s0_75, d_75, r_75, x_75, p_75 = 84.0, 2.00, 0.05, 80.0, 2.65
    pvd_75 = d_75 / ((1.0 + r_75) ** 0.25)
    c_75 = p_75 + (s0_75 - pvd_75) - x_75 / ((1.0 + r_75) ** 0.5)
    opts, ans, dist = build_num_opts(
        c_75,
        p_75 + s0_75 - x_75 / ((1.0 + r_75) ** 0.5), "Omits subtracting the PV of the USD 2.00 dividend from S0.",
        p_75 + (s0_75 + pvd_75) - x_75 / ((1.0 + r_75) ** 0.5), "Adds the dividend PV to S0 instead of subtracting it.",
        lambda v: _fmt_usd(v, 2),
    )
    add_num_l1(
        qs, "L1-DRV-075", SUBJECT, m9, t9, "Put-Call Parity with Dividends",
        "Apply put-call parity adjusted for discrete dividends.",
        f"A stock trades at USD {s0_75:.2f} and will pay a USD {d_75:.2f} dividend in 3 months ($t = 0.25$). A 6-month ($T = 0.50$) European put with strike USD {x_75:.2f} trades at USD {p_75:.2f}, and the discrete annual risk-free rate is {r_75*100:.1f}%. What is the fair price of the 6-month European call with strike USD {x_75:.2f}?",
        opts, ans,
        f"Adjusted parity: $c_0 = p_0 + (S_0 - PV_0(D)) - X(1+r)^{{-T}}$. With $PV_0(D) = 2.00/1.05^{{0.25}} = {pvd_75:.4f}$ and $PV(X) = 80/1.05^{{0.5}} = {x_75/(1.05**0.5):.4f}$, $c_0 = 2.65 + (84 - {pvd_75:.4f}) - {x_75/(1.05**0.5):.4f} = \\text{{USD }} {c_75:.2f}$.",
        dist,
    )

    # 076 (Numerical)
    s0_76, x_76, r_76, cm_76, pm_76 = 55.0, 55.0, 0.04, 5.90, 3.10
    fid_76 = cm_76 + x_76 / (1.0 + r_76)
    prot_76 = pm_76 + s0_76
    arb_76 = fid_76 - prot_76
    opts, ans, dist = build_num_opts(
        arb_76,
        (cm_76 - pm_76) - (s0_76 - x_76), "USD 2.80 ignores discounting the strike price X in the fiduciary call.",
        arb_76 * (1.0 + r_76), f"USD {arb_76*(1+r_76):.2f} computes the future value of the parity discrepancy at T = 1 instead of its PV at t = 0.",
        lambda v: _fmt_usd(v, 2),
    )
    add_num_l1(
        qs, "L1-DRV-076", SUBJECT, m9, t9, "Fiduciary Call vs. Protective Put",
        "Identify arbitrage between a fiduciary call and a protective put.",
        f"A non-dividend stock trades at USD {s0_76:.2f} and the 1-year discrete risk-free rate is {r_76*100:.1f}%. One-year European options with strike USD {x_76:.2f} trade at $c_0 = \\text{{USD }} {cm_76:.2f}$ and $p_0 = \\text{{USD }} {pm_76:.2f}$. What is the immediate arbitrage profit per share at $t = 0$?",
        opts, ans,
        f"Fiduciary call cost $= c_0 + X/(1+r) = 5.90 + 55/1.04 = \\text{{USD }} {fid_76:.4f}$. Protective put cost $= p_0 + S_0 = 3.10 + 55.00 = \\text{{USD }} {prot_76:.2f}$. Selling the overpriced fiduciary call and buying the protective put captures $\\text{{USD }} {arb_76:.2f}$ immediately.",
        dist,
    )

    # 077 (Numerical)
    f0_77, x_77, r_77, p_77 = 148.0, 145.0, 0.045, 4.80
    c_77 = p_77 + (f0_77 - x_77) / (1.0 + r_77)
    opts, ans, dist = build_num_opts(
        c_77,
        p_77 + (f0_77 - x_77), "USD 7.80 omits discounting (F0 - X) at the risk-free rate.",
        p_77 - (f0_77 - x_77) / (1.0 + r_77), "USD 1.93 reverses the sign of (F0 - X); when F0 > X, the call must cost more than the put.",
        lambda v: _fmt_usd(v, 2),
    )
    add_num_l1(
        qs, "L1-DRV-077", SUBJECT, m9, t9, "Put-Call-Forward Parity",
        "Value an option using put-call-forward parity.",
        f"A 1-year forward contract on an asset has a forward price of USD {f0_77:.2f} when the 1-year discrete risk-free rate is {r_77*100:.1f}%. If a 1-year European put with strike USD {x_77:.2f} trades at USD {p_77:.2f}, what is the fair price of the 1-year European call at the same strike?",
        opts, ans,
        f"Put-call-forward parity: $c_0 + X(1+r)^{{-T}} = p_0 + F_0(1+r)^{{-T}} \\implies c_0 = 4.80 + \\frac{{148.00 - 145.00}}{{1.045}} = \\text{{USD }} {c_77:.2f}$.",
        dist,
    )

    # 078 (Conceptual)
    opts, ans, dist = build_text_opts(
        "Long a call option, short a put option at strike X, and long a risk-free bond paying X at maturity",
        "Short a call option, long a put option at strike X, and long a risk-free bond paying X at maturity",
        "Short call plus long put replicates a short forward (-ST + X), which when combined with +X creates cash +2X - ST rather than long stock.",
        "Long a call option, long a put option at strike X, and short a risk-free bond paying X at maturity",
        "Long call plus long put is a straddle, which does not replicate linear stock ownership.",
        "C",
    )
    add_l1(
        qs, "L1-DRV-078", SUBJECT, m9, t9, "Synthetic Asset Replication",
        "Replicate a long underlying stock position using options and a bond.",
        "Using European options with strike $X$ and expiration $T$, which portfolio replicates a long position in one share of a non-dividend-paying stock?",
        opts, ans,
        "Rearranging put-call parity ($c_0 + X(1+r)^{-T} = p_0 + S_0$) gives $S_0 = c_0 - p_0 + X(1+r)^{-T}$: long a call, short a put, and long a zero-coupon risk-free bond with face value $X$.",
        dist,
    )

    # 079 (Numerical)
    s0_79, x_79, c_79, p_79 = 100.0, 100.0, 8.40, 3.85
    pv_x79 = s0_79 + p_79 - c_79
    r_imp79 = x_79 / pv_x79 - 1.0
    opts, ans, dist = build_num_opts(
        r_imp79,
        (c_79 - p_79) / s0_79, "4.55% divides (c - p) by S0 rather than computing X / PV(X) - 1.",
        x_79 / (s0_79 + c_79 - p_79) - 1.0, "Reverses the signs of c and p when solving for PV(X).",
        lambda v: _fmt_pct(v, 2),
    )
    add_num_l1(
        qs, "L1-DRV-079", SUBJECT, m9, t9, "Synthetic Risk-Free Yield",
        "Compute the implied risk-free rate from put-call parity.",
        f"A non-dividend stock trades at USD {s0_79:.2f}. One-year European options with strike USD {x_79:.2f} trade at $c_0 = \\text{{USD }} {c_79:.2f}$ and $p_0 = \\text{{USD }} {p_79:.2f}$. What is the implied 1-year discrete risk-free interest rate?",
        opts, ans,
        f"Solving parity for $PV(X)$: $X/(1+r) = S_0 + p_0 - c_0 = 100 + 3.85 - 8.40 = \\text{{USD }} {pv_x79:.2f}$. Thus $1+r = 100.00 / 95.45 \\implies r = {r_imp79*100:.2f}\\%$.",
        dist,
    )

    # LM10 (080-085): 1-Period Binomial Model
    m10, t10 = "DRV-LM10", "One-Period Binomial Model"

    # 080 (Numerical)
    s0_80, u_80, d_80, x_80 = 50.0, 1.25, 0.80, 52.0
    su_80, sd_80 = s0_80 * u_80, s0_80 * d_80
    cu_80, cd_80 = max(0.0, su_80 - x_80), max(0.0, sd_80 - x_80)
    h_80 = (cu_80 - cd_80) / (su_80 - sd_80)
    opts, ans, dist = build_num_opts(
        h_80,
        (su_80 - x_80) / su_80, "0.168 divides call payoff by Su instead of by the spread (Su - Sd).",
        h_80 - 1.0, "-0.533 is the hedge ratio for the corresponding put option rather than the call option.",
        lambda v: _fmt_num(v, 3),
    )
    add_num_l1(
        qs, "L1-DRV-080", SUBJECT, m10, t10, "Binomial Hedge Ratio",
        "Calculate the optimal hedge ratio in a one-period binomial model.",
        f"A stock currently trades at USD {s0_80:.2f} and can move over one period to either $uS_0 = \\text{{USD }} {su_80:.2f}$ or $dS_0 = \\text{{USD }} {sd_80:.2f}$. What is the optimal hedge ratio $h$ for a one-period European call option with strike USD {x_80:.2f}?",
        opts, ans,
        f"$c^+ = \\max(0, 62.50 - 52.00) = 10.50$; $c^- = \\max(0, 40.00 - 52.00) = 0$. Optimal hedge ratio $h = \\frac{{c^+ - c^-}}{{S^+ - S^-}} = \\frac{{10.50 - 0}}{{62.50 - 40.00}} = {h_80:.3f}$.",
        dist,
    )

    # 081 (Numerical)
    u_81, d_81, r_81 = 1.20, 0.85, 0.05
    pi_81 = (1.0 + r_81 - d_81) / (u_81 - d_81)
    opts, ans, dist = build_num_opts(
        pi_81,
        1.0 - pi_81, "0.4286 is the risk-neutral down probability (1 - pi) rather than the up probability pi.",
        (1.0 - r_81 - d_81) / (u_81 - d_81), "0.2857 subtracts the risk-free rate r instead of adding it.",
        lambda v: _fmt_num(v, 4),
    )
    add_num_l1(
        qs, "L1-DRV-081", SUBJECT, m10, t10, "Risk-Neutral Probability",
        "Calculate risk-neutral probabilities in a binomial model.",
        f"In a one-period binomial model, the gross up factor is $u = {u_81:.2f}$, the gross down factor is $d = {d_81:.2f}$, and the one-period risk-free rate is {r_81*100:.1f}%. What is the risk-neutral probability $\\pi$ of an up move?",
        opts, ans,
        f"Risk-neutral up probability: $\\pi = \\frac{{1 + r - d}}{{u - d}} = \\frac{{1.05 - 0.85}}{{1.20 - 0.85}} = \\frac{{0.20}}{{0.35}} = {pi_81:.4f}$.",
        dist,
    )

    # 082 (Numerical)
    s0_82, u_82, d_82, x_82, r_82 = 80.0, 1.15, 0.88, 82.0, 0.04
    pi_82 = (1.0 + r_82 - d_82) / (u_82 - d_82)
    cu_82 = max(0.0, s0_82 * u_82 - x_82)
    cd_82 = max(0.0, s0_82 * d_82 - x_82)
    c0_82 = (pi_82 * cu_82 + (1.0 - pi_82) * cd_82) / (1.0 + r_82)
    opts, ans, dist = build_num_opts(
        c0_82,
        (0.5 * cu_82 + 0.5 * cd_82) / (1.0 + r_82), "Uses an arbitrary 50/50 probability instead of the risk-neutral probability pi.",
        pi_82 * cu_82 + (1.0 - pi_82) * cd_82, "Fails to discount the risk-neutral expected payoff at (1 + r).",
        lambda v: _fmt_usd(v, 2),
    )
    add_num_l1(
        qs, "L1-DRV-082", SUBJECT, m10, t10, "Binomial Call Pricing",
        "Value a European call using the one-period binomial model.",
        f"A stock priced at USD {s0_82:.2f} moves in one period by $u = {u_82:.2f}$ or $d = {d_82:.2f}$. The one-period risk-free rate is {r_82*100:.1f}%. Using risk-neutral valuation, the value of a one-period European call option with strike USD {x_82:.2f} is closest to:",
        opts, ans,
        f"$S^+ = 92.00 \\implies c^+ = 10.00$; $S^- = 70.40 \\implies c^- = 0$. $\\pi = \\frac{{1.04 - 0.88}}{{1.15 - 0.88}} = {pi_82:.4f}$. Then $c_0 = \\frac{{{pi_82:.4f}(10.00) + {1-pi_82:.4f}(0)}}{{1.04}} = \\text{{USD }} {c0_82:.2f}$.",
        dist,
    )

    # 083 (Numerical)
    s0_83, u_83, d_83, x_83, r_83 = 60.0, 1.20, 0.82, 62.0, 0.035
    pi_83 = (1.0 + r_83 - d_83) / (u_83 - d_83)
    pu_83 = max(0.0, x_83 - s0_83 * u_83)
    pd_83 = max(0.0, x_83 - s0_83 * d_83)
    p0_83 = (pi_83 * pu_83 + (1.0 - pi_83) * pd_83) / (1.0 + r_83)
    opts, ans, dist = build_num_opts(
        p0_83,
        (pi_83 * pd_83 + (1.0 - pi_83) * pu_83) / (1.0 + r_83), "Applies pi to the down-node put payoff instead of (1 - pi).",
        pi_83 * pu_83 + (1.0 - pi_83) * pd_83, "Omits discounting the expected put payoff by 1 + r.",
        lambda v: _fmt_usd(v, 2),
    )
    add_num_l1(
        qs, "L1-DRV-083", SUBJECT, m10, t10, "Binomial Put Pricing",
        "Value a European put using the one-period binomial model.",
        f"A stock trades at USD {s0_83:.2f} with one-period factors $u = {u_83:.2f}$ and $d = {d_83:.2f}$, and a one-period risk-free rate of {r_83*100:.1f}%. What is the no-arbitrage price of a one-period European put option with strike USD {x_83:.2f}?",
        opts, ans,
        f"$S^+ = 72.00 \\implies p^+ = 0$; $S^- = 49.20 \\implies p^- = 12.80$. $\\pi = \\frac{{1.035 - 0.82}}{{1.20 - 0.82}} = {pi_83:.4f}$, so $1 - \\pi = {1-pi_83:.4f}$. Thus $p_0 = \\frac{{{1-pi_83:.4f}(12.80)}}{{1.035}} = \\text{{USD }} {p0_83:.2f}$.",
        dist,
    )

    # 084 (Numerical)
    # Using 082 parameters, market call trades at USD 6.20 vs fair c0_82
    cm_84 = 6.20
    arb_84 = cm_84 - c0_82
    opts, ans, dist = build_num_opts(
        arb_84,
        arb_84 * (1.0 + r_82), f"USD {arb_84*(1+r_82):.2f} computes the future value of the mispricing at T = 1 instead of its PV at t = 0.",
        c0_82, f"USD {c0_82:.2f} is the theoretical binomial option price rather than the arbitrage profit.",
        lambda v: _fmt_usd(v, 2),
    )
    add_num_l1(
        qs, "L1-DRV-084", SUBJECT, m10, t10, "Binomial Arbitrage",
        "Exploit a mispriced option in a one-period binomial framework.",
        f"Continuing with a stock at USD {s0_82:.2f} ($u = {u_82:.2f}, d = {d_82:.2f}, r = {r_82*100:.1f}\\%$), suppose the one-period European call with strike USD {x_82:.2f} (fair value USD {c0_82:.2f}) trades in the market at USD {cm_84:.2f}. What is the immediate riskless arbitrage profit per share by selling the market call and buying the replicating portfolio?",
        opts, ans,
        f"Selling the overpriced call for USD {cm_84:.2f} and buying the synthetic replicating portfolio ($h S_0 - PV(hS^-)$) costing exactly USD {c0_82:.2f} generates an immediate risk-free profit of $6.20 - {c0_82:.2f} = \\text{{USD }} {arb_84:.2f}$ per share.",
        dist,
    )

    # 085 (Conceptual)
    opts, ans, dist = build_text_opts(
        "No-arbitrage replication locks in exact terminal payoffs regardless of which path occurs, making subjective real-world probabilities irrelevant",
        "Risk-neutral probabilities are always strictly equal to historical real-world probabilities when assets are fairly priced",
        "Real-world probabilities include risk premiums and typically exceed risk-neutral up probabilities for risky equities.",
        "Real-world probabilities only matter for European puts and are ignored solely for calls",
        "No-arbitrage replication eliminates subjective probabilities for both calls and puts.",
        "A",
    )
    add_l1(
        qs, "L1-DRV-085", SUBJECT, m10, t10, "Real-World vs. Risk-Neutral Probabilities",
        "Explain why actual probabilities of up/down moves are excluded from binomial option pricing.",
        "Why do investors' subjective estimates of the true probability of an up move have no direct effect on the no-arbitrage option price in a binomial model (given $S_0, u, d, r$)?",
        opts, ans,
        "Because a portfolio of $h$ shares and riskless borrowing replicates the option's exact cash flows in both states, no-arbitrage forces the option price to equal the replication cost, leaving no role for subjective probabilities.",
        dist,
    )


# =============================================================================
# LEVEL 2 VIGNETTES (11 Vignettes x 5 Questions = 55 Questions: L2-DRV-V01..V11)
# =============================================================================

def build_v01(qs: list):
    """V01: Equity & Fixed-Income Forward Contract Valuation Mid-Life (AI / Conversion Factor)."""
    vid = "DRV-V01"
    vtitle = "Meridian Multi-Asset Equity and Treasury Forward Valuation"
    # Parameters
    s0_nv, div_nv, r_nv, t_nv = 140.00, 2.40, 0.048, 0.75
    pvd_nv = div_nv / ((1.0 + r_nv) ** 0.25)
    f0_nv = (s0_nv - pvd_nv) * ((1.0 + r_nv) ** t_nv)
    st_nv = 148.50
    vt_long_nv_per = st_nv - f0_nv / ((1.0 + r_nv) ** 0.25)
    vt_long_nv_tot = 5000.0 * vt_long_nv_per

    i0_idx, q_idx, r_idx0, t_idx = 4800.0, 0.019, 0.044, 1.0
    f0_idx = i0_idx * math.exp((r_idx0 - q_idx) * t_idx)
    it_idx, r_idxt, rem_idx = 4960.0, 0.046, 0.60
    vt_long_idx = it_idx * math.exp(-q_idx * rem_idx) - f0_idx * math.exp(-r_idxt * rem_idx)
    vt_short_idx_tot = -250.0 * vt_long_idx

    # Bond C: 30/360 annual discrete r_b = 4.50%
    bc_clean, ai0_c, cpn_c, r_b, ait_c, cf_c = 98.40, 0.70, 2.10, 0.045, 0.70, 0.9240
    bc_full = bc_clean + ai0_c
    pvc_c = cpn_c / ((1.0 + r_b) ** (120.0 / 360.0))
    f0_full_c = (bc_full - pvc_c) * ((1.0 + r_b) ** 0.50)
    f0_clean_c = f0_full_c - ait_c
    qfp_c = f0_clean_c / cf_c

    # CTD comparison at delivery / current futures quote QFP_mkt = 105.00
    qfp_mkt = 105.00
    # Bond C clean vs Bond D clean at same date:
    c_clean_ctd, cf_c_ctd = 97.90, 0.9240
    d_clean_ctd, cf_d_ctd = 107.60, 1.0120
    # Basis / cost to deliver (Clean - QFP*CF)
    net_c = c_clean_ctd - qfp_mkt * cf_c_ctd
    net_d = d_clean_ctd - qfp_mkt * cf_d_ctd

    vtext = (
        "Elena Vance, CFA, manages equity and sovereign fixed-income forward overlays at Meridian Multi-Asset Partners. "
        "She is reviewing three forward and futures exposures across client portfolios:\n\n"
        "1. **NovaTech Equity Forward**: Six months ago ($t = 0$), Meridian entered a **long** 9-month ($T = 0.75$ yr) "
        f"forward contract on 5,000 shares of NovaTech when spot was USD {s0_nv:.2f}. A discrete dividend of USD {div_nv:.2f}/share "
        f"was expected and paid at $t = 0.25$ years. Today ($t = 0.50$ yr, 3 months remaining), NovaTech trades at USD {st_nv:.2f}. "
        f"The annual discrete risk-free rate has remained constant at {r_nv*100:.2f}%.\n\n"
        "2. **Global Equity Index Forward**: Four and a half months ago ($t = 0$), Meridian entered a **short** 1-year forward "
        f"on 250 units of a broad equity index at {i0_idx:,.0f}, when the continuous dividend yield was {q_idx*100:.2f}% and the continuous "
        f"risk-free rate was {r_idx0*100:.2f}%. Today ($t = 0.40$ yr, 0.60 yr remaining), the index is {it_idx:,.0f} and the continuous "
        f"risk-free rate has shifted to {r_idxt*100:.2f}% (dividend yield unchanged).\n\n"
        "3. **US Treasury Bond Forward & Futures**: Meridian is pricing a 6-month ($T = 0.50$ yr, 180/360) forward contract on "
        f"Treasury Note C (4.20% semi-annual coupon, USD 2.10 per 100 par). Note C trades at a clean spot price of {bc_clean:.2f} "
        f"with accrued interest $AI_0 = {ai0_c:.2f}$. A coupon of 2.10 will be paid in 120 days, and accrued interest at $T = 0.50$ yr "
        f"will be $AI_T = {ait_c:.2f}$. The annual discrete risk-free rate is {r_b*100:.2f}% (30/360). For Treasury futures, "
        f"Note C has conversion factor $CF = {cf_c_ctd:.4f}$, while eligible Note D has $CF = {cf_d_ctd:.4f}$. Currently, "
        f"if spot clean prices are {c_clean_ctd:.2f} (Note C) and {d_clean_ctd:.2f} (Note D) against a quoted futures price of {qfp_mkt:.2f}, "
        "Vance checks which bond is cheapest to deliver (CTD)."
    )

    m, t = "DRV-LM11", "Pricing and Valuation of Forward Commitments"
    # Q1: Fair F0 of NovaTech
    opts, ans, dist = build_num_opts(
        f0_nv,
        (s0_nv + pvd_nv) * ((1.0 + r_nv) ** t_nv), "Adds the dividend PV instead of subtracting it from spot.",
        s0_nv * ((1.0 + r_nv) ** t_nv), "Ignores the USD 2.40 discrete dividend paid at t = 0.25 years.",
        lambda v: _fmt_usd(v, 2),
    )
    add_num_l2(
        qs, "L2-DRV-V01-Q1", m, t, "Equity Forward Pricing", vid, vtitle, vtext,
        "Calculate the no-arbitrage forward price of a stock paying discrete dividends.",
        "At $t = 0$, the fair forward price per share on NovaTech was closest to:",
        opts, ans,
        f"$PV_0(D) = 2.40 / (1.048)^{{0.25}} = \\text{{USD }} {pvd_nv:.4f}$. Thus $F_0 = (140.00 - {pvd_nv:.4f})(1.048)^{{0.75}} = \\text{{USD }} {f0_nv:.2f}$.",
        dist,
    )

    # Q2: Mid-life MTM of 5,000 long NovaTech forwards
    opts, ans, dist = build_num_opts(
        vt_long_nv_tot,
        5000.0 * (st_nv - pvd_nv - f0_nv / ((1.0 + r_nv) ** 0.25)), "Erroneously deducts the already-paid dividend at t = 0.50 years.",
        5000.0 * (st_nv - f0_nv), "Omits discounting the original forward price F0 over the remaining 0.25 years.",
        lambda v: _fmt_usd(v, 0),
    )
    add_num_l2(
        qs, "L2-DRV-V01-Q2", m, t, "Equity Forward Valuation", vid, vtitle, vtext,
        "Calculate the mid-life mark-to-market value of an equity forward.",
        "At $t = 0.50$ years, the mark-to-market value of Meridian's 5,000-share **long** NovaTech forward position is closest to:",
        opts, ans,
        f"Because the $t=0.25$ dividend has already been paid, remaining benefits equal zero. Per share value $= S_t - F_0/(1+r)^{{0.25}} = 148.50 - {f0_nv:.4f}/(1.048)^{{0.25}} = \\text{{USD }} {vt_long_nv_per:.4f}$. Across 5,000 shares, total value $= \\text{{USD }} {vt_long_nv_tot:,.0f}$.",
        dist,
    )

    # Q3: Short index forward MTM
    opts, ans, dist = build_num_opts(
        vt_short_idx_tot,
        -vt_short_idx_tot, f"+USD {abs(vt_short_idx_tot):,.0f} is the value of the long counterparty rather than Meridian's short position.",
        -250.0 * (it_idx - f0_idx * math.exp(-r_idxt * rem_idx)), "Omits discounting the current index level by exp(-q(T-t)).",
        lambda v: _fmt_usd(v, 0),
    )
    add_num_l2(
        qs, "L2-DRV-V01-Q3", m, t, "Index Forward Valuation", vid, vtitle, vtext,
        "Value a continuous-yield equity index forward after interest rates change.",
        "At $t = 0.40$ years, the mark-to-market value of Meridian's 250-unit **short** Global Equity Index forward is closest to:",
        opts, ans,
        f"Initial forward price $F_0 = 4,800 e^{{(0.044 - 0.019)(1.0)}} = {f0_idx:,.4f}$. Long value per unit at $t=0.40$ ($T-t=0.60$) is $4,960 e^{{-0.019(0.60)}} - {f0_idx:,.4f} e^{{-0.046(0.60)}} = {vt_long_idx:.4f}$. For 250 short units, value $= -250 \\times {vt_long_idx:.4f} = \\text{{USD }} {vt_short_idx_tot:,.0f}$.",
        dist,
    )

    # Q4: Clean forward price on Note C
    opts, ans, dist = build_num_opts(
        f0_clean_c,
        f0_full_c, f"{f0_full_c:.2f} is the full (dirty) forward price rather than the quoted (clean) forward price.",
        ((bc_clean - pvc_c) * ((1.0 + r_b) ** 0.50)) - ait_c, "Omits initial accrued interest AI0 when calculating the spot full price.",
        lambda v: _fmt_num(v, 2),
    )
    add_num_l2(
        qs, "L2-DRV-V01-Q4", m, t, "Bond Forward Pricing", vid, vtitle, vtext,
        "Determine the quoted (clean) forward price of a coupon-bearing Treasury bond.",
        "The equilibrium **quoted (clean)** 6-month forward price per 100 par for Treasury Note C is closest to:",
        opts, ans,
        f"Full spot price $= 98.40 + 0.70 = 99.10$. $PV_0(C) = 2.10/(1.045)^{{120/360}} = {pvc_c:.4f}$. Full forward price $= (99.10 - {pvc_c:.4f})(1.045)^{{0.5}} = {f0_full_c:.4f}$. Subtracting $AI_T = 0.70$ gives clean forward price $= {f0_clean_c:.2f}$.",
        dist,
    )

    # Q5: CTD & Quoted Futures Price
    # Ask for equilibrium QFP of Note C AND identify CTD between C and D? Let's compute net_c and net_d clearly:
    # net_c = 97.90 - 105.00*0.9240 = 97.90 - 97.02 = 0.88
    # net_d = 107.60 - 105.00*1.0120 = 107.60 - 106.26 = 1.34
    # CTD is Note C with net delivery cost (Clean - QFP*CF) = 0.88 < 1.34!
    opts, ans, dist = build_text_opts(
        f"Note C, because its clean price minus converted futures price is {net_c:.2f} vs. {net_d:.2f} for Note D",
        f"Note D, because its clean price minus converted futures price is {net_d:.2f} vs. {net_c:.2f} for Note C",
        "The short seller pays the spot clean price to buy the bond and receives QFP x CF, so the seller minimizes (Clean - QFP x CF), not maximizes it.",
        f"Note C, because its conversion factor ({cf_c_ctd:.4f}) is lower than Note D's ({cf_d_ctd:.4f})",
        "Conversion factor alone does not determine CTD; CTD depends on the relative spot clean price minus QFP x CF.",
        "A",
    )
    NUM_Q_IDS.add("L2-DRV-V01-Q5")
    add_num_l2(
        qs, "L2-DRV-V01-Q5", m, t, "Cheapest-to-Deliver Bond", vid, vtitle, vtext,
        "Identify the cheapest-to-deliver bond using conversion factors.",
        "Using the spot clean prices and conversion factors at the quoted futures price of 105.00, which Treasury note is cheapest to deliver (CTD)?",
        opts, ans,
        f"The short delivers the bond minimizing $(B_{{\\text{{clean}}}} - QFP \\times CF)$: Note C gives $97.90 - 105.00(0.9240) = {net_c:.2f}$, while Note D gives $107.60 - 105.00(1.0120) = {net_d:.2f}$. Thus Note C is CTD.",
        dist,
    )


def build_v02(qs: list):
    """V02: FRA Pricing from Spot Rates & Mid-Life Valuation."""
    vid = "DRV-V02"
    vtitle = "Cascade Industrial Forward Rate Agreement (FRA) Valuation"
    # t=0 spot rates (30/360)
    r30, r90, r180, r270, r360 = 0.0410, 0.0435, 0.0465, 0.0490, 0.0510
    # 3x9 FRA (h=0.25, m=0.50, total=0.75)
    fra_3x9 = (((1.0 + r270 * 0.75) / (1.0 + r90 * 0.25)) - 1.0) / 0.50
    # 6x12 FRA (h=0.50, m=0.50, total=1.00)
    fra_6x12 = (((1.0 + r360 * 1.00) / (1.0 + r180 * 0.50)) - 1.0) / 0.50

    # At t=60 days: spot rates
    rt30, rt120, rt210, rt300 = 0.0450, 0.0485, 0.0515, 0.0535
    # 3x9 FRA now has h'=30/360, h'+m=210/360 (1x7 FRA)
    fra_t_3x9 = (((1.0 + rt210 * (210.0 / 360.0)) / (1.0 + rt30 * (30.0 / 360.0))) - 1.0) / 0.50
    np_long = 25_000_000.0
    vt_long_3x9 = np_long * ((fra_t_3x9 - fra_3x9) * 0.50) / (1.0 + rt210 * (210.0 / 360.0))

    # Existing short 6x12 FRA at fixed 4.75% on USD 15M; at t=60, remaining is 120x300 (4x10)
    np_short, fra_c_short = 15_000_000.0, 0.0475
    fra_t_6x12 = (((1.0 + rt300 * (300.0 / 360.0)) / (1.0 + rt120 * (120.0 / 360.0))) - 1.0) / 0.50
    vt_short_6x12 = np_short * ((fra_c_short - fra_t_6x12) * 0.50) / (1.0 + rt300 * (300.0 / 360.0))

    vtext = (
        "Marcus Chen, treasury director at Cascade Industrial, uses Forward Rate Agreements (FRAs) under a 30/360 day-count "
        "convention to hedge upcoming floating-rate debt issuances. Spot annualized MRR rates at initiation ($t = 0$) and "
        "60 days later ($t = 60$ days) are reported below:\n\n"
        "| Maturity at $t=0$ | Rate at $t=0$ | Remaining Maturity at $t=60$ | Rate at $t=60$ |\n"
        "|---|---|---|---|\n"
        f"| 30-day | {r30*100:.2f}% | 30-day | {rt30*100:.2f}% |\n"
        f"| 90-day | {r90*100:.2f}% | 120-day | {rt120*100:.2f}% |\n"
        f"| 180-day | {r180*100:.2f}% | 210-day | {rt210*100:.2f}% |\n"
        f"| 270-day | {r270*100:.2f}% | 300-day | {rt300*100:.2f}% |\n"
        f"| 360-day | {r360*100:.2f}% | — | — |\n\n"
        f"At $t = 0$, Cascade enters a **long** $3 \\times 9$ FRA on USD {np_long:,.0f} notional at the equilibrium market rate. "
        f"Cascade also holds an off-market **short** $6 \\times 12$ FRA (initiated on the same day $t = 0$) with a contract rate "
        f"of {fra_c_short*100:.2f}% on USD {np_short:,.0f} notional."
    )

    m, t = "DRV-LM11", "Pricing and Valuation of Forward Commitments"
    # Q1: 3x9 FRA rate
    opts, ans, dist = build_num_opts(
        fra_3x9,
        ((1.0 + r270 * 0.75) / (1.0 + r90 * 0.25)) - 1.0, "2.56% is the unannualized 180-day forward rate rather than the annualized FRA rate.",
        (r270 - r90) / 0.50, "1.10% confuses rate differences with forward compounding factors.",
        lambda v: _fmt_pct(v, 2),
    )
    add_num_l2(
        qs, "L2-DRV-V02-Q1", m, t, "FRA Pricing", vid, vtitle, vtext,
        "Determine the equilibrium FRA rate from the MRR spot curve.",
        "At $t = 0$, the equilibrium annualized fixed rate on the $3 \\times 9$ FRA is closest to:",
        opts, ans,
        f"$FRA(0, 90, 180) = \\left[\\frac{{1 + 0.0490(270/360)}}{{1 + 0.0435(90/360)}} - 1\\right] \\times \\frac{{360}}{{180}} = {fra_3x9*100:.2f}\\%$.",
        dist,
    )

    # Q2: 6x12 FRA rate
    opts, ans, dist = build_num_opts(
        fra_6x12,
        ((1.0 + r360) / (1.0 + r180 * 0.50)) - 1.0, "2.71% is the unannualized 6-month forward rate rather than the annualized 6x12 rate.",
        (r360 + r180) / 2.0, "4.88% takes an arithmetic average instead of stripping the implied forward factor.",
        lambda v: _fmt_pct(v, 2),
    )
    add_num_l2(
        qs, "L2-DRV-V02-Q2", m, t, "6x12 FRA Pricing", vid, vtitle, vtext,
        "Calculate forward rates along an upward-sloping MRR spot curve.",
        "At $t = 0$, the equilibrium annualized fixed rate on a $6 \\times 12$ FRA is closest to:",
        opts, ans,
        f"$FRA(0, 180, 180) = \\left[\\frac{{1 + 0.0510(1.0)}}{{1 + 0.0465(0.5)}} - 1\\right] \\times 2 = {fra_6x12*100:.2f}\\%$.",
        dist,
    )

    # Q3: Updated market FRA rate at t=60 for 3x9 FRA (remaining 1x7)
    opts, ans, dist = build_num_opts(
        fra_t_3x9,
        (((1.0 + rt210 * (210.0 / 360.0)) / (1.0 + rt30 * (30.0 / 360.0))) - 1.0), "2.62% is the unannualized 180-day forward rate at t = 60.",
        (((1.0 + rt300 * (300.0 / 360.0)) / (1.0 + rt120 * (120.0 / 360.0))) - 1.0) / 0.50, f"{fra_t_6x12*100:.2f}% corresponds to the 4x10 period of the 6x12 FRA rather than the 1x7 period.",
        lambda v: _fmt_pct(v, 2),
    )
    add_num_l2(
        qs, "L2-DRV-V02-Q3", m, t, "Mid-Life Repricing", vid, vtitle, vtext,
        "Determine the updated implied forward rate needed for mid-life FRA valuation.",
        "At $t = 60$ days, the new market annualized FRA rate applicable to the remaining underlying period of the $3 \\times 9$ FRA is closest to:",
        opts, ans,
        f"After 60 days, the $3 \\times 9$ FRA has 30 days to expiration and 210 days to final settlement ($1 \\times 7$ FRA). Using 30-day ({rt30*100:.2f}%) and 210-day ({rt210*100:.2f}%) rates: $FRA_{{60}}(30, 180) = \\left[\\frac{{1 + 0.0515(210/360)}}{{1 + 0.0450(30/360)}} - 1\\right] \\times 2 = {fra_t_3x9*100:.2f}\\%$.",
        dist,
    )

    # Q4: Mid-life MTM of long 3x9 FRA
    opts, ans, dist = build_num_opts(
        vt_long_3x9,
        np_long * (fra_t_3x9 - fra_3x9) * 0.50, "Omits discounting the settlement cash flow over the 210-day period to maturity.",
        np_long * (fra_t_3x9 - fra_3x9) * 0.50 / (1.0 + rt30 * (30.0 / 360.0)), "Discounts using the 30-day rate (expiration) instead of the 210-day rate (settlement end).",
        lambda v: _fmt_usd(v, 0),
    )
    add_num_l2(
        qs, "L2-DRV-V02-Q4", m, t, "Mid-Life Long FRA Value", vid, vtitle, vtext,
        "Calculate the mark-to-market value of a long FRA mid-life.",
        "At $t = 60$ days, the mark-to-market value of Cascade's **long** USD 25,000,000 $3 \\times 9$ FRA is closest to:",
        opts, ans,
        f"$V_{{60}}(\\text{{long}}) = 25,000,000 \\times \\frac{{({fra_t_3x9:.6f} - {fra_3x9:.6f})(0.50)}}{{1 + 0.0515(210/360)}} = \\text{{USD }} {vt_long_3x9:,.0f}$.",
        dist,
    )

    # Q5: Mid-life MTM of short 6x12 FRA
    opts, ans, dist = build_num_opts(
        vt_short_6x12,
        -vt_short_6x12, f"+USD {abs(vt_short_6x12):,.0f} is the value to the long counterparty rather than Cascade's short FRA.",
        np_short * ((fra_c_short - fra_t_6x12) * 0.50), "Omits discounting over the 300-day horizon at 5.35%.",
        lambda v: _fmt_usd(v, 0),
    )
    add_num_l2(
        qs, "L2-DRV-V02-Q5", m, t, "Mid-Life Short FRA Value", vid, vtitle, vtext,
        "Calculate the mark-to-market value of a short off-market FRA mid-life.",
        "At $t = 60$ days, the mark-to-market value of Cascade's **short** USD 15,000,000 $6 \\times 12$ FRA (contract rate 4.75%) is closest to:",
        opts, ans,
        f"Remaining window is 120 to 300 days. New market FRA rate $= \\left[\\frac{{1 + 0.0535(300/360)}}{{1 + 0.0485(120/360)}} - 1\\right] \\times 2 = {fra_t_6x12*100:.4f}\\%$. For the short side, $V_{{60}}(\\text{{short}}) = 15,000,000 \\times \\frac{{(0.0475 - {fra_t_6x12:.6f})(0.5)}}{{1 + 0.0535(300/360)}} = \\text{{USD }} {vt_short_6x12:,.0f}$.",
        dist,
    )


def build_v03(qs: list):
    """V03: Interest Rate Swap Fixed Rate & Mid-Life MTM Valuation."""
    vid = "DRV-V03"
    vtitle = "Veridian Insurance Interest Rate Swap Valuation"
    s90, s180, s270, s360 = 0.0420, 0.0445, 0.0470, 0.0495
    df90 = 1.0 / (1.0 + s90 * 0.25)
    df180 = 1.0 / (1.0 + s180 * 0.50)
    df270 = 1.0 / (1.0 + s270 * 0.75)
    df360 = 1.0 / (1.0 + s360 * 1.00)
    c_per0 = (1.0 - df360) / (df90 + df180 + df270 + df360)
    c_ann0 = c_per0 * 4.0
    np_swap = 40_000_000.0

    # Q2: Day 90 net cash flow for pay-fixed (90d MRR at t=0 was 4.20%)
    cf90_pay = np_swap * (s90 * 0.25 - c_per0)

    # Scenario A at Day 180 (post-settlement): remaining 90d=4.80%, 180d=5.10%
    sa90, sa180 = 0.0480, 0.0510
    dfa90 = 1.0 / (1.0 + sa90 * 0.25)
    dfa180 = 1.0 / (1.0 + sa180 * 0.50)
    v_fix_a = np_swap * (c_per0 * (dfa90 + dfa180) + dfa180)
    v_rec_a = v_fix_a - np_swap
    v_pay_a = np_swap - v_fix_a

    # Scenario B at Day 210 (between resets: 60d and 150d remaining; Day 180 floating reset = 4.80%)
    sb60, sb150 = 0.0490, 0.0520
    dfb60 = 1.0 / (1.0 + sb60 * (60.0 / 360.0))
    dfb150 = 1.0 / (1.0 + sb150 * (150.0 / 360.0))
    v_fix_b = np_swap * (c_per0 * (dfb60 + dfb150) + dfb150)
    v_flt_b = np_swap * (1.0 + sa90 * 0.25) * dfb60
    v_rec_b = v_fix_b - v_flt_b

    vtext = (
        "Sarah Patel, ALM strategist at Veridian Insurance, enters a 1-year quarterly-pay plain-vanilla interest rate swap "
        f"(30/360) on USD {np_swap:,.0f} notional at $t = 0$ as the **pay-fixed, receive-floating** party. At initiation, "
        "spot MRR rates are:\n\n"
        f"- 90-day: {s90*100:.2f}% | 180-day: {s180*100:.2f}% | 270-day: {s270*100:.2f}% | 360-day: {s360*100:.2f}%\n\n"
        "**Scenario A (Day 180, immediately after settlement)**: Two quarterly settlements remain (Days 270 and 360). "
        f"Current spot rates are {sa90*100:.2f}% (90-day) and {sa180*100:.2f}% (180-day). The Day 180 floating reset for Day 270 is {sa90*100:.2f}%.\n\n"
        "**Scenario B (Day 210, between reset dates)**: Thirty days later (60 days until Day 270 and 150 days until Day 360), "
        f"spot MRR rates stand at {sb60*100:.2f}% (60-day) and {sb150*100:.2f}% (150-day)."
    )

    m, t = "DRV-LM11", "Pricing and Valuation of Swaps"
    # Q1: Annualized fixed swap rate at t=0
    opts, ans, dist = build_num_opts(
        c_ann0,
        c_per0, f"{c_per0*100:.2f}% is the quarterly periodic coupon rate rather than the annualized fixed swap rate.",
        (s90 + s180 + s270 + s360) / 4.0, "4.58% takes the simple arithmetic average of the four spot rates.",
        lambda v: _fmt_pct(v, 2),
    )
    add_num_l2(
        qs, "L2-DRV-V03-Q1", m, t, "Swap Fixed Rate", vid, vtitle, vtext,
        "Compute the par fixed swap rate from spot discount factors.",
        "At $t = 0$, the equilibrium **annualized** fixed rate on Veridian's 1-year quarterly swap is closest to:",
        opts, ans,
        f"Discount factors: $DF_{{90}}={df90:.6f}$, $DF_{{180}}={df180:.6f}$, $DF_{{270}}={df270:.6f}$, $DF_{{360}}={df360:.6f}$ ($\\sum DF = {df90+df180+df270+df360:.6f}$). Quarterly rate $= \\frac{{1 - {df360:.6f}}}{{{df90+df180+df270+df360:.6f}}} = {c_per0*100:.4f}\\%$, or $4 \\times {c_per0*100:.4f}\\% = {c_ann0*100:.2f}\\%$ annualized.",
        dist,
    )

    # Q2: Day 90 net cash flow
    opts, ans, dist = build_num_opts(
        cf90_pay,
        -cf90_pay, f"+USD {abs(cf90_pay):,.0f} represents the net inflow to the receive-fixed counterparty rather than Veridian.",
        np_swap * (s90 - c_ann0), f"-USD {abs(np_swap * (s90 - c_ann0)):,.0f} fails to scale the annualized rate spread by 90/360 = 0.25.",
        lambda v: _fmt_usd(v, 0),
    )
    add_num_l2(
        qs, "L2-DRV-V03-Q2", m, t, "First Settlement Cash Flow", vid, vtitle, vtext,
        "Calculate the first quarterly net cash flow of an interest rate swap.",
        "Using the Day 0 floating reset of 4.20%, Veridian's net cash flow on the Day 90 settlement date is closest to:",
        opts, ans,
        f"Veridian receives floating $40\\text{{M}} \\times 0.0420(0.25) = \\text{{USD }} 420,000$ and pays fixed $40\\text{{M}} \\times {c_per0:.6f} = \\text{{USD }} {np_swap*c_per0:,.0f}$, yielding a net cash flow of $\\text{{USD }} {cf90_pay:,.0f}$.",
        dist,
    )

    # Q3: Scenario A MTM value to pay-fixed at Day 180
    opts, ans, dist = build_num_opts(
        v_pay_a,
        v_rec_a, f"-USD {abs(v_rec_a):,.0f} is the value to the receive-fixed counterparty rather than Veridian.",
        np_swap * (sa180 - c_ann0) * 0.5, "Approximates without using exact quarterly discount factors.",
        lambda v: _fmt_usd(v, 0),
    )
    add_num_l2(
        qs, "L2-DRV-V03-Q3", m, t, "Swap Valuation on Reset Date", vid, vtitle, vtext,
        "Value an interest rate swap on a settlement date using updated discount factors.",
        "Under Scenario A (Day 180, immediately after settlement), the MTM value of the swap to Veridian (**pay-fixed**) is closest to:",
        opts, ans,
        f"$DF_{{90}}^{{\\text{{new}}}} = 1/(1+0.048(0.25)) = {dfa90:.6f}$ and $DF_{{180}}^{{\\text{{new}}}} = 1/(1+0.051(0.50)) = {dfa180:.6f}$. Fixed leg PV $= 40\\text{{M}}[{c_per0:.6f}({dfa90+dfa180:.6f}) + {dfa180:.6f}] = \\text{{USD }} {v_fix_a:,.0f}$. Since floating leg resets to par (USD 40M), $V_{{180}}(\\text{{pay-fixed}}) = \\text{{USD }} 40,000,000 - \\text{{USD }} {v_fix_a:,.0f} = \\text{{USD }} {v_pay_a:,.0f}$.",
        dist,
    )

    # Q4: Scenario B between resets (value to receive-fixed!)
    opts, ans, dist = build_num_opts(
        v_rec_b,
        v_fix_b - np_swap, "Erroneously treats the floating-rate bond leg as equal to par (USD 40,000,000) between reset dates.",
        -v_rec_b, f"+USD {abs(v_rec_b):,.0f} is the MTM value to the pay-fixed party rather than the receive-fixed party.",
        lambda v: _fmt_usd(v, 0),
    )
    add_num_l2(
        qs, "L2-DRV-V03-Q4", m, t, "Mid-Period Swap Valuation", vid, vtitle, vtext,
        "Value an interest rate swap between reset dates including the locked-in next floating payment.",
        "Under Scenario B (Day 210, between resets), the MTM value of the swap to the **receive-fixed** dealer is closest to:",
        opts, ans,
        f"$DF_{{60}} = {dfb60:.6f}$ and $DF_{{150}} = {dfb150:.6f}$. Fixed leg PV $= \\text{{USD }} {v_fix_b:,.0f}$. Floating leg PV $= 40\\text{{M}}(1 + 0.0480 \\times 0.25) \\times DF_{{60}} = \\text{{USD }} {v_flt_b:,.0f}$. Receive-fixed value $= V_{{\\text{{fix}}}} - V_{{\\text{{flt}}}} = \\text{{USD }} {v_rec_b:,.0f}$.",
        dist,
    )

    # Q5: Conceptual
    opts, ans, dist = build_text_opts(
        "The floating bond's future coupons reset to market rates at each date, keeping its present value equal to par immediately after settlement",
        "The swap fixed rate automatically resets every quarter to match the 90-day spot rate",
        "The fixed swap rate remains locked for the entire contract life; only the floating leg resets.",
        "Both fixed and floating legs equal par on every settlement date regardless of rate changes",
        "Only the floating leg equals par on reset dates; the fixed bond moves inversely with yields.",
        "B",
    )
    add_l2(
        qs, "L2-DRV-V03-Q5", SUBJECT, m, t, "Floating Leg Par Property", vid, vid, vtitle, vtext,
        "Explain why a floating-rate leg resets to par on settlement dates.",
        "In Scenario A, why can Patel set the value of the floating-rate leg exactly equal to USD 40,000,000 immediately after the Day 180 settlement?",
        opts, ans,
        "Immediately after paying a coupon on a reset date, a par floating-rate note pays market-clearing MRR over every subsequent period, so discounting those expected coupons plus principal at the market MRR curve recovers exact par value.",
        dist,
    )


def build_v04(qs: list):
    """V04: Currency Swap Pricing & Valuation."""
    vid = "DRV-V04"
    vtitle = "Global Capital USD-EUR Currency Swap Valuation"
    s0 = 1.1200  # USD per EUR
    np_eur = 20_000_000.0
    np_usd = np_eur * s0  # 22,400,000

    # t=0 annual spot rates (30/360)
    u1, u2 = 0.0460, 0.0490
    e1, e2 = 0.0310, 0.0340
    dfu1, dfu2 = 1.0 / (1.0 + u1 * 1.0), 1.0 / (1.0 + u2 * 2.0)
    dfe1, dfe2 = 1.0 / (1.0 + e1 * 1.0), 1.0 / (1.0 + e2 * 2.0)
    r_usd_fix = (1.0 - dfu2) / (dfu1 + dfu2)
    r_eur_fix = (1.0 - dfe2) / (dfe1 + dfe2)

    # At t=0.50 yr: spot FX = 1.1600 USD/EUR
    st = 1.1600
    ut05, ut15 = 0.0500, 0.0525
    et05, et15 = 0.0280, 0.0305
    dfut05, dfut15 = 1.0 / (1.0 + ut05 * 0.5), 1.0 / (1.0 + ut15 * 1.5)
    dfet05, dfet15 = 1.0 / (1.0 + et05 * 0.5), 1.0 / (1.0 + et15 * 1.5)

    v_usd_leg = np_usd * (r_usd_fix * (dfut05 + dfut15) + dfut15)
    v_eur_leg_eur = np_eur * (r_eur_fix * (dfet05 + dfet15) + dfet15)
    v_swap_rec_usd_pay_eur_fix = v_usd_leg - st * v_eur_leg_eur

    # Q5: Pay EUR floating (Year 1 EUR coupon locked at e1=3.10%), receive USD fixed
    v_eur_flt_eur = np_eur * (1.0 + e1 * 1.0) * dfet05
    v_swap_rec_usd_pay_eur_flt = v_usd_leg - st * v_eur_flt_eur

    vtext = (
        "Henrik Lindqvist, head of corporate treasury at Global Capital Group, enters a 2-year annual-pay fixed-for-fixed "
        f"currency swap at $t = 0$ to **pay EUR fixed and receive USD fixed**, with initial and final exchange of notional principals "
        f"(30/360 convention, discount factor $DF_t = 1/(1 + S_t \\cdot t)$). At $t = 0$, the spot rate is {s0:.4f} USD per EUR "
        f"and the EUR notional is EUR {np_eur:,.0f} (USD {np_usd:,.0f}).\n\n"
        f"- **$t = 0$ Spot Curves**: USD 1-yr = {u1*100:.2f}%, USD 2-yr = {u2*100:.2f}%; EUR 1-yr = {e1*100:.2f}%, EUR 2-yr = {e2*100:.2f}%.\n\n"
        f"Six months later ($t = 0.50$ yr, remaining payments at $0.50$ yr and $1.50$ yr), the spot rate moves to {st:.4f} USD per EUR. "
        "Updated spot rates are:\n"
        f"- **USD**: 0.5-yr = {ut05*100:.2f}%, 1.5-yr = {ut15*100:.2f}%\n"
        f"- **EUR**: 0.5-yr = {et05*100:.2f}%, 1.5-yr = {et15*100:.2f}%"
    )

    m, t = "DRV-LM11", "Pricing and Valuation of Swaps"
    # Q1: Equilibrium USD & EUR fixed swap rates
    opts, ans, dist = build_text_opts(
        f"USD fixed = {r_usd_fix*100:.2f}%; EUR fixed = {r_eur_fix*100:.2f}%",
        f"USD fixed = {u2*100:.2f}%; EUR fixed = {e2*100:.2f}%",
        "Uses the 2-year spot rates directly instead of solving (1 - DF2) / (DF1 + DF2).",
        f"USD fixed = {r_eur_fix*100:.2f}%; EUR fixed = {r_usd_fix*100:.2f}%",
        "Swaps the USD and EUR equilibrium swap rates.",
        "B",
    )
    NUM_Q_IDS.add("L2-DRV-V04-Q1")
    add_num_l2(
        qs, "L2-DRV-V04-Q1", m, t, "Currency Swap Pricing", vid, vtitle, vtext,
        "Calculate fixed swap rates for each leg of a currency swap.",
        "At $t = 0$, the equilibrium annualized fixed swap rates on the USD and EUR legs are closest to:",
        opts, ans,
        f"USD: $DF_1={dfu1:.6f}, DF_2={dfu2:.6f} \\implies c_{{\\text{{USD}}}} = \\frac{{1-{dfu2:.6f}}}{{{dfu1+dfu2:.6f}}} = {r_usd_fix*100:.2f}\\%$. EUR: $DF_1={dfe1:.6f}, DF_2={dfe2:.6f} \\implies c_{{\\text{{EUR}}}} = \\frac{{1-{dfe2:.6f}}}{{{dfe1+dfe2:.6f}}} = {r_eur_fix*100:.2f}\\%$.",
        dist,
    )

    # Q2: Year 1 coupon payments
    usd_cpn = np_usd * r_usd_fix
    eur_cpn = np_eur * r_eur_fix
    opts, ans, dist = build_text_opts(
        f"Receive USD {usd_cpn:,.0f} and pay EUR {eur_cpn:,.0f}",
        f"Pay USD {usd_cpn:,.0f} and receive EUR {eur_cpn:,.0f}",
        "Reverses the cash flow direction; Global Capital pays EUR fixed and receives USD fixed.",
        f"Net USD {usd_cpn - s0 * eur_cpn:,.0f} only",
        "Currency swaps exchange gross coupons in their respective currencies rather than netting.",
        "C",
    )
    NUM_Q_IDS.add("L2-DRV-V04-Q2")
    add_num_l2(
        qs, "L2-DRV-V04-Q2", m, t, "Currency Swap Cash Flows", vid, vtitle, vtext,
        "Determine periodic coupon cash flows in a currency swap.",
        "At Year 1, what coupon cash flows occur for Global Capital (using exact unrounded equilibrium swap rates)?",
        opts, ans,
        f"USD receipt $= 22,400,000 \\times {r_usd_fix:.6f} = \\text{{USD }} {usd_cpn:,.0f}$; EUR payment $= 20,000,000 \\times {r_eur_fix:.6f} = \\text{{EUR }} {eur_cpn:,.0f}$, exchanged gross.",
        dist,
    )

    # Q3: USD value of USD fixed bond leg at t=0.50
    opts, ans, dist = build_num_opts(
        v_usd_leg,
        np_usd, "USD 22,400,000 assumes the fixed USD leg stays at par despite interest rates rising.",
        np_usd * (r_usd_fix * dfut05 + dfut15), "Omits the Year 2 fixed coupon payment from the USD bond valuation.",
        lambda v: _fmt_usd(v, 0),
    )
    add_num_l2(
        qs, "L2-DRV-V04-Q3", m, t, "USD Bond Leg Valuation", vid, vtitle, vtext,
        "Compute the mark-to-market value of the USD fixed leg mid-life.",
        "At $t = 0.50$ years, the present value of the USD fixed-rate bond leg is closest to:",
        opts, ans,
        f"$DF_{{0.5}} = 1/(1+0.05(0.5)) = {dfut05:.6f}$ and $DF_{{1.5}} = 1/(1+0.0525(1.5)) = {dfut15:.6f}$. Thus $V_{{\\text{{USD}}}} = 22.4\\text{{M}}[{r_usd_fix:.6f}({dfut05+dfut15:.6f}) + {dfut15:.6f}] = \\text{{USD }} {v_usd_leg:,.0f}$.",
        dist,
    )

    # Q4: Mid-life MTM value in USD (receive USD fixed, pay EUR fixed)
    opts, ans, dist = build_num_opts(
        v_swap_rec_usd_pay_eur_fix,
        v_usd_leg - s0 * v_eur_leg_eur, "Translates the EUR bond leg using the stale t = 0 exchange rate (1.1200) instead of current spot (1.1600).",
        -v_swap_rec_usd_pay_eur_fix, f"+USD {abs(v_swap_rec_usd_pay_eur_fix):,.0f} is the value to the pay-USD / receive-EUR counterparty rather than Global Capital.",
        lambda v: _fmt_usd(v, 0),
    )
    add_num_l2(
        qs, "L2-DRV-V04-Q4", m, t, "Currency Swap MTM Valuation", vid, vtitle, vtext,
        "Calculate the mid-life mark-to-market value of a fixed-for-fixed currency swap.",
        "At $t = 0.50$ years, the MTM value in USD to Global Capital (**receive USD fixed, pay EUR fixed**) is closest to:",
        opts, ans,
        f"$V_{{\\text{{EUR}}}} = \\text{{EUR }} {v_eur_leg_eur:,.0f}$. Converting at $S_{{0.5}} = 1.1600$ gives $1.1600 \\times {v_eur_leg_eur:,.0f} = \\text{{USD }} {st*v_eur_leg_eur:,.0f}$. Value $= V_{{\\text{{USD}}}} - S_{{0.5}} V_{{\\text{{EUR}}}} = \\text{{USD }} {v_usd_leg:,.0f} - \\text{{USD }} {st*v_eur_leg_eur:,.0f} = \\text{{USD }} {v_swap_rec_usd_pay_eur_fix:,.0f}$.",
        dist,
    )

    # Q5: Pay EUR floating (Year 1 EUR floating reset at t=0 1-yr EUR rate 3.10%), receive USD fixed
    opts, ans, dist = build_num_opts(
        v_swap_rec_usd_pay_eur_flt,
        v_usd_leg - st * np_eur, "Assumes the EUR floating leg equals EUR 20,000,000 par mid-period instead of discounting the locked-in Year 1 floating coupon.",
        v_usd_leg - s0 * v_eur_flt_eur, "Uses the initial FX rate 1.1200 rather than current spot 1.1600 to convert the EUR floating bond.",
        lambda v: _fmt_usd(v, 0),
    )
    add_num_l2(
        qs, "L2-DRV-V04-Q5", m, t, "Fixed-for-Floating Currency Swap", vid, vtitle, vtext,
        "Value a fixed-for-floating currency swap between reset dates.",
        "If Global Capital had instead entered a **pay EUR floating, receive USD fixed** swap (with Year 1 EUR floating coupon locked at 3.10%), the USD MTM value at $t = 0.50$ years would be closest to:",
        opts, ans,
        f"Between resets, $V_{{\\text{{EUR,flt}}}} = 20\\text{{M}}(1 + 0.0310) \\times DF_{{0.5}}^{{\\text{{EUR}}}} = \\text{{EUR }} {v_eur_flt_eur:,.0f}$. In USD, $1.1600 \\times {v_eur_flt_eur:,.0f} = \\text{{USD }} {st*v_eur_flt_eur:,.0f}$. Swap value $= \\text{{USD }} {v_usd_leg:,.0f} - \\text{{USD }} {st*v_eur_flt_eur:,.0f} = \\text{{USD }} {v_swap_rec_usd_pay_eur_flt:,.0f}$.",
        dist,
    )


def build_v05(qs: list):
    """V05: Equity Swap Cash Flow & Valuation."""
    vid = "DRV-V05"
    vtitle = "Sovereign Equity Total Return Swap Valuation"
    np_eq = 30_000_000.0
    fix_ann = 0.0440
    fix_q = fix_ann / 4.0  # 1.10%
    i0, i90, i180, i210 = 2500.0, 2610.0, 2492.55, 2580.0
    ret_q1 = (i90 - i0) / i0  # +4.40%
    cf_q1 = np_eq * (ret_q1 - fix_q)
    ret_q2 = (i180 - i90) / i90  # -4.50%
    cf_q2 = np_eq * (ret_q2 - fix_q)

    # At Day 210: 60d=4.60%, 150d=4.85% (remaining Q3=60d, Q4=150d)
    r60, r150 = 0.0460, 0.0485
    df60 = 1.0 / (1.0 + r60 * (60.0 / 360.0))
    df150 = 1.0 / (1.0 + r150 * (150.0 / 360.0))
    eq_leg_210 = np_eq * (i210 / i180)
    fix_leg_210 = np_eq * (fix_q * (df60 + df150) + df150)
    val_rec_eq_fix = eq_leg_210 - fix_leg_210

    # Floating alternative: Day 180 90-day MRR reset at 4.50%
    mrr180 = 0.0450
    flt_leg_210 = np_eq * (1.0 + mrr180 * 0.25) * df60
    val_rec_eq_flt = eq_leg_210 - flt_leg_210

    vtext = (
        "Nadia Al-Mansoor, portfolio manager at a sovereign fund, executes a 1-year quarterly-reset Total Return Equity Swap "
        f"(30/360) on notional USD {np_eq:,.0f}. The fund **receives the total return on Equity Index EQX** and **pays a fixed "
        f"annualized rate of {fix_ann*100:.2f}%** ({fix_q*100:.2f}% per quarter). EQX total return index levels and market rates are:\n\n"
        f"- $t = 0$ (Initiation): $EQX_0 = {i0:,.2f}$\n"
        f"- Day 90 (Q1 settlement): $EQX_{{90}} = {i90:,.2f}$\n"
        f"- Day 180 (Q2 settlement): $EQX_{{180}} = {i180:,.2f}$ (90-day MRR resets at {mrr180*100:.2f}%)\n"
        f"- Day 210 (mid-Q3, 60 days to Day 270 and 150 days to Day 360): $EQX_{{210}} = {i210:,.2f}$; 60-day spot MRR = {r60*100:.2f}%, "
        f"150-day spot MRR = {r150*100:.2f}%."
    )

    m, t = "DRV-LM11", "Pricing and Valuation of Swaps"
    # Q1: Day 90 net cash flow
    opts, ans, dist = build_num_opts(
        cf_q1,
        np_eq * ret_q1, "USD 1,320,000 is the gross equity leg gain without deducting the 1.10% quarterly fixed payment.",
        np_eq * (ret_q1 - fix_ann), "USD 0 erroneously deducts the full 4.40% annual fixed rate in a single quarter.",
        lambda v: _fmt_usd(v, 0),
    )
    add_num_l2(
        qs, "L2-DRV-V05-Q1", m, t, "Equity Swap Cash Flow", vid, vtitle, vtext,
        "Calculate periodic net cash flows on an equity total return swap.",
        "On Day 90, the net cash flow received by the sovereign fund is closest to:",
        opts, ans,
        f"Q1 equity return $= (2,610.00 - 2,500.00)/2,500.00 = +4.40\\%$. Net receipt $= 30\\text{{M}} \\times (0.0440 - 0.0110) = \\text{{USD }} {cf_q1:,.0f}$.",
        dist,
    )

    # Q2: Day 180 negative return cash flow
    opts, ans, dist = build_num_opts(
        cf_q2,
        np_eq * (ret_q2 + fix_q), "Offsets the fixed coupon against the equity loss instead of adding the two outflows.",
        np_eq * ((i180 - i0) / i0 - fix_q), "Measures Q2 equity return from t = 0 rather than from the Q1 reset level (2,610.00).",
        lambda v: _fmt_usd(v, 0),
    )
    add_num_l2(
        qs, "L2-DRV-V05-Q2", m, t, "Negative Equity Return Flow", vid, vtitle, vtext,
        "Determine equity swap settlement when the equity index declines.",
        "On Day 180, after EQX declines to 2,492.55, the net cash flow to the sovereign fund (receive-equity, pay-fixed) is closest to:",
        opts, ans,
        f"Q2 return $= (2,492.55 - 2,610.00)/2,610.00 = -4.50\\%$. When equity returns are negative, the equity receiver pays BOTH the equity loss and the fixed coupon: $30\\text{{M}} \\times (-0.0450 - 0.0110) = -\\text{{USD }} {abs(cf_q2):,.0f}$.",
        dist,
    )

    # Q3: Mid-Q3 Day 210 MTM value (pay-fixed)
    opts, ans, dist = build_num_opts(
        val_rec_eq_fix,
        np_eq * (i210 / i0) - fix_leg_210, "Scales the equity leg from EQX0 (2,500) instead of the latest reset EQX180 (2,492.55).",
        eq_leg_210 - np_eq, "Assumes the fixed bond leg equals par (USD 30,000,000) rather than discounting fixed coupons and principal.",
        lambda v: _fmt_usd(v, 0),
    )
    add_num_l2(
        qs, "L2-DRV-V05-Q3", m, t, "Mid-Quarter Equity Swap Value", vid, vtitle, vtext,
        "Value a pay-fixed equity swap between reset dates.",
        "At Day 210, the MTM value of the **receive-equity, pay-fixed** swap to the sovereign fund is closest to:",
        opts, ans,
        f"Equity leg value $= 30\\text{{M}} \\times (2,580.00 / 2,492.55) = \\text{{USD }} {eq_leg_210:,.0f}$. With $DF_{{60}}={df60:.6f}$ and $DF_{{150}}={df150:.6f}$, fixed bond PV $= \\text{{USD }} {fix_leg_210:,.0f}$. Swap value $= \\text{{USD }} {eq_leg_210:,.0f} - \\text{{USD }} {fix_leg_210:,.0f} = \\text{{USD }} {val_rec_eq_fix:,.0f}$.",
        dist,
    )

    # Q4: Mid-Q3 Day 210 MTM value if pay-floating (mrr180 = 4.50%)
    opts, ans, dist = build_num_opts(
        val_rec_eq_flt,
        eq_leg_210 - np_eq, "Ignores the locked-in Day 180 floating coupon and 60-day discounting by setting floating leg to par.",
        np_eq * (i210 / i0) - flt_leg_210, "Computes the equity leg from initial index 2,500 instead of the Q2 reset 2,492.55.",
        lambda v: _fmt_usd(v, 0),
    )
    add_num_l2(
        qs, "L2-DRV-V05-Q4", m, t, "Pay-Floating Equity Swap", vid, vtitle, vtext,
        "Value a pay-floating equity swap between reset dates.",
        "If the fund had instead entered a **receive-equity, pay-floating** swap (with Day 180 90-day MRR reset at 4.50%), the MTM value at Day 210 would be closest to:",
        opts, ans,
        f"Floating leg PV $= 30\\text{{M}}(1 + 0.045 \\times 0.25) \\times DF_{{60}} = \\text{{USD }} {flt_leg_210:,.0f}$. Swap value $= \\text{{USD }} {eq_leg_210:,.0f} - \\text{{USD }} {flt_leg_210:,.0f} = \\text{{USD }} {val_rec_eq_flt:,.0f}$.",
        dist,
    )

    # Q5: Conceptual
    opts, ans, dist = build_text_opts(
        "Total return equity swaps automatically include cash dividends and reset notional on each reset date, whereas equity index futures reflect only price appreciation and require rolling across expirations",
        "Equity swaps eliminate all counterparty credit exposure via daily exchange variation margin, whereas equity futures carry bilateral OTC credit risk",
        "The reverse is true: exchange-traded futures eliminate bilateral credit risk via CCP margining, whereas OTC equity swaps carry counterparty risk unless collateralized.",
        "Equity swap fixed rates must equal the underlying stock's dividend yield at initiation",
        "The swap fixed/floating financing leg reflects money market interest rates plus/minus a dealer spread, not the stock's dividend yield.",
        "A",
    )
    add_l2(
        qs, "L2-DRV-V05-Q5", SUBJECT, m, t, "Equity Swap vs. Futures", vid, vid, vtitle, vtext,
        "Compare total return equity swaps with equity index futures.",
        "Compared with gaining EQX exposure via listed equity index futures, which feature best distinguishes Al-Mansoor's total return equity swap?",
        opts, ans,
        "A total return equity swap delivers exact dividend reinvestment (avoiding dividend forecast risk) and automatically resets notional each period, whereas equity index futures track only price returns and require periodic contract rolls.",
        dist,
    )


def build_v06(qs: list):
    """V06: 2-Period Binomial European & American Put Tree."""
    vid = "DRV-V06"
    vtitle = "BioVax Two-Period Binomial Option Valuation"
    s0, x, u, d, r = 100.0, 105.0, 1.20, 0.80, 0.025
    pi = (1.0 + r - d) / (u - d)  # (1.025 - 0.8)/0.4 = 0.5625
    su, sd = s0 * u, s0 * d  # 120, 80
    suu, sud, sdd = su * u, su * d, sd * d  # 144, 96, 64

    puu = max(0.0, x - suu)  # 0
    pud = max(0.0, x - sud)  # 9
    pdd = max(0.0, x - sdd)  # 41

    # European put
    pu_eu = (pi * puu + (1.0 - pi) * pud) / (1.0 + r)
    pd_eu = (pi * pud + (1.0 - pi) * pdd) / (1.0 + r)
    p0_eu = (pi * pu_eu + (1.0 - pi) * pd_eu) / (1.0 + r)

    # American put: intrinsic at u is max(0, 105-120)=0; at d is max(0, 105-80)=25
    pu_am = max(max(0.0, x - su), pu_eu)
    pd_cont = (pi * pud + (1.0 - pi) * pdd) / (1.0 + r)
    pd_intr = max(0.0, x - sd)  # 25.00 vs cont ~ 22.439
    pd_am = max(pd_intr, pd_cont)
    p0_am = max(max(0.0, x - s0), (pi * pu_am + (1.0 - pi) * pd_am) / (1.0 + r))
    eep = p0_am - p0_eu

    # Hedge ratios for European put
    h0_eu = (pu_eu - pd_eu) / (su - sd)
    hd_eu = (pud - pdd) / (sud - sdd)

    # Arbitrage if American put trades at USD 11.40 vs p0_am
    pmkt = 11.40
    arb_am = pmkt - p0_am

    vtext = (
        "David Kovács, equity derivatives trader, values 1-year European and American put options on non-dividend-paying "
        f"biotech stock BioVax ($S_0 = \\text{{USD }} {s0:.2f}$) with strike price $X = \\text{{USD }} {x:.2f}$ using a two-period "
        "binomial lattice (two 6-month steps). Each step uses multiplicative factors $u = 1.20$ and $d = 0.80$, with a discrete "
        f"6-month risk-free rate of $r = {r*100:.2f}\\%$ per period ($1 + r = 1.025$)."
    )

    m, t = "DRV-LM12", "Valuation of Contingent Claims"
    # Q1: European put value p0
    opts, ans, dist = build_num_opts(
        p0_eu,
        (0.5 * ((0.5 * puu + 0.5 * pud) / (1 + r)) + 0.5 * ((0.5 * pud + 0.5 * pdd) / (1 + r))) / (1 + r),
        "Uses a 0.50 equal probability instead of the risk-neutral probability pi = 0.5625.",
        p0_am, f"USD {p0_am:.2f} values the American put with early exercise at node d rather than the European put.",
        lambda v: _fmt_usd(v, 2),
    )
    add_num_l2(
        qs, "L2-DRV-V06-Q1", m, t, "Two-Period European Put", vid, vtitle, vtext,
        "Price a European put option using a two-period binomial model.",
        "Using the two-period binomial tree, the fair value of the **European** put option at $t = 0$ is closest to:",
        opts, ans,
        f"$\\pi = (1.025 - 0.80)/(1.20 - 0.80) = {pi:.4f}$. Terminal payoffs: $p_{{uu}}=0, p_{{ud}}=9, p_{{dd}}=41$. At $t=1$: $p_u = {pu_eu:.4f}$ and $p_d = {pd_eu:.4f}$. Discounting back: $p_0 = \\frac{{{pi:.4f}({pu_eu:.4f}) + {1-pi:.4f}({pd_eu:.4f})}}{{1.025}} = \\text{{USD }} {p0_eu:.2f}$.",
        dist,
    )

    # Q2: American put value & early exercise check at d
    opts, ans, dist = build_num_opts(
        p0_am,
        p0_eu, f"USD {p0_eu:.2f} ignores optimal early exercise at node Sd = 80 (where intrinsic USD 25.00 exceeds continuation USD {pd_cont:.2f}).",
        max(max(0.0, x - s0), (pi * pu_am + (1.0 - pi) * (pd_intr + 2.0)) / (1 + r)),
        "Overstates the down-node payoff above its USD 25.00 intrinsic exercise value.",
        lambda v: _fmt_usd(v, 2),
    )
    add_num_l2(
        qs, "L2-DRV-V06-Q2", m, t, "American Put Early Exercise", vid, vtitle, vtext,
        "Price an American put option checking for early exercise at intermediate nodes.",
        "Allowing for optimal early exercise, the fair value of the **American** put option at $t = 0$ is closest to:",
        opts, ans,
        f"At node $S_d = 80$, continuation value is ${pd_cont:.4f}$ whereas intrinsic value is $105 - 80 = \\text{{USD }} 25.00$, so early exercise is optimal ($P_d = 25.00$). At $S_u = 120$, $P_u = {pu_am:.4f}$. Thus $P_0 = \\max\\left(5, \\frac{{{pi:.4f}({pu_am:.4f}) + {1-pi:.4f}(25.00)}}{{1.025}}\\right) = \\text{{USD }} {p0_am:.2f}$.",
        dist,
    )

    # Q3: Early exercise premium
    opts, ans, dist = build_num_opts(
        eep,
        pd_intr - pd_cont, f"USD {pd_intr - pd_cont:.2f} reports the raw early exercise benefit at node Sd = 80 without weighting by (1 - pi) and discounting to t = 0.",
        x - s0, "USD 5.00 is the t = 0 intrinsic value rather than the American early exercise premium.",
        lambda v: _fmt_usd(v, 2),
    )
    add_num_l2(
        qs, "L2-DRV-V06-Q3", m, t, "Early Exercise Premium", vid, vtitle, vtext,
        "Calculate the early exercise premium of an American put.",
        "The value of the early exercise privilege (early exercise premium) embedded in the American put at $t = 0$ is closest to:",
        opts, ans,
        f"Early exercise premium $= P_0^{{\\text{{Am}}}} - p_0^{{\\text{{Eu}}}} = {p0_am:.4f} - {p0_eu:.4f} = \\text{{USD }} {eep:.2f}$ (equivalently $\\frac{{(1-\\pi)(25.00 - {pd_cont:.4f})}}{{1.025}}$).",
        dist,
    )

    # Q4: Hedge ratios h0 and hd for European put
    opts, ans, dist = build_text_opts(
        f"h0 = {h0_eu:.3f} at t = 0; hd = {hd_eu:.3f} at node Sd = 80",
        f"h0 = {abs(h0_eu):.3f} at t = 0; hd = {abs(hd_eu):.3f} at node Sd = 80",
        "Positive deltas apply to call options; put hedge ratios are negative because put values move inversely with stock prices.",
        f"h0 = {h0_eu:.3f} at t = 0; hd = -0.781 at node Sd = 80",
        "At node Sd = 80, the European put is guaranteed to finish in the money (pud=9, pdd=41), giving a delta of -1.000 rather than -0.781.",
        "C",
    )
    NUM_Q_IDS.add("L2-DRV-V06-Q4")
    add_num_l2(
        qs, "L2-DRV-V06-Q4", m, t, "Dynamic Binomial Hedge Ratio", vid, vtitle, vtext,
        "Compute dynamic binomial hedge ratios across tree nodes.",
        "For the **European** put option, the optimal hedge ratios (option delta) at $t = 0$ ($h_0$) and at the down node $S_d = 80$ ($h_d$) are:",
        opts, ans,
        f"At $t=0$: $h_0 = \\frac{{{pu_eu:.4f} - {pd_eu:.4f}}}{{120 - 80}} = {h0_eu:.3f}$. At $S_d = 80$: $h_d = \\frac{{9 - 41}}{{96 - 64}} = \\frac{{-32}}{{32}} = -1.000$.",
        dist,
    )

    # Q5: Arbitrage if American put trades at 11.40
    opts, ans, dist = build_num_opts(
        arb_am,
        pmkt - p0_eu, f"USD {pmkt - p0_eu:.2f} compares the American market price against the European model value instead of the American model value.",
        arb_am * (1.0 + r) ** 2, "Compounds the mispricing to T = 1 year instead of measuring t = 0 arbitrage profit.",
        lambda v: _fmt_usd(v, 2),
    )
    add_num_l2(
        qs, "L2-DRV-V06-Q5", m, t, "Binomial Option Arbitrage", vid, vtitle, vtext,
        "Quantify arbitrage from a mispriced American option.",
        f"If the BioVax **American** put trades in the market at USD {pmkt:.2f}, the riskless arbitrage profit per option captured at $t = 0$ by selling the market option and dynamically replicating it is closest to:",
        opts, ans,
        f"Fair American put value is USD {p0_am:.4f}. Selling the overpriced put at USD {pmkt:.2f} and constructing the replicating portfolio at USD {p0_am:.4f} locks in $\\text{{USD }} {pmkt:.2f} - \\text{{USD }} {p0_am:.4f} = \\text{{USD }} {arb_am:.2f}$ at $t = 0$.",
        dist,
    )


def build_v07(qs: list):
    """V07: 2-Period Binomial Interest Rate Tree & Interest Rate Options / Bond Options."""
    vid = "DRV-V07"
    vtitle = "Binomial Interest Rate Tree: Caplets, Floorlets, Bond Options & Swaptions"
    r0 = 0.0400
    r1h, r1l = 0.0540, 0.0340
    r2hh, r2hl, r2ll = 0.0680, 0.0460, 0.0280
    np_ir = 10_000_000.0
    k_cap = 0.0420

    # Q1: 2-yr caplet (period [1,2], reset at t=1, paid in arrears at t=2)
    pay1h_cap = np_ir * max(0.0, r1h - k_cap)
    pay1l_cap = np_ir * max(0.0, r1l - k_cap)
    pv1h_cap = pay1h_cap / (1.0 + r1h)
    pv1l_cap = pay1l_cap / (1.0 + r1l)
    caplet_0 = (0.5 * pv1h_cap + 0.5 * pv1l_cap) / (1.0 + r0)

    # Q2: Year-2 floorlet (period [2,3], reset at t=2, paid in arrears at t=3, strike 4.20%)
    pv2hh_flr = np_ir * max(0.0, k_cap - r2hh) / (1.0 + r2hh)
    pv2hl_flr = np_ir * max(0.0, k_cap - r2hl) / (1.0 + r2hl)
    pv2ll_flr = np_ir * max(0.0, k_cap - r2ll) / (1.0 + r2ll)
    pv1h_flr = (0.5 * pv2hh_flr + 0.5 * pv2hl_flr) / (1.0 + r1h)
    pv1l_flr = (0.5 * pv2hl_flr + 0.5 * pv2ll_flr) / (1.0 + r1l)
    floorlet_0 = (0.5 * pv1h_flr + 0.5 * pv1l_flr) / (1.0 + r0)

    # Q3 & Q4: 3-year 4.50% annual coupon bond (par 100) + 1-year European call at X=99.00 on USD 1M par
    cpn = 4.50
    v2hh = (100.0 + cpn) / (1.0 + r2hh)
    v2hl = (100.0 + cpn) / (1.0 + r2hl)
    v2ll = (100.0 + cpn) / (1.0 + r2ll)
    v1h = (0.5 * (v2hh + cpn) + 0.5 * (v2hl + cpn)) / (1.0 + r1h)
    v1l = (0.5 * (v2hl + cpn) + 0.5 * (v2ll + cpn)) / (1.0 + r1l)
    k_bond = 99.00
    c1h = max(0.0, v1h - k_bond)
    c1l = max(0.0, v1l - k_bond)
    call_bond_pct = (0.5 * c1h + 0.5 * c1l) / (1.0 + r0)
    call_bond_usd = 1_000_000.0 * (call_bond_pct / 100.0)

    # Q5: 1-year European payer swaption (strike 4.40% on 2-yr swap covering t=2,3, NP=USD 10M)
    cpn_sw = 4.40
    s2hh = (100.0 + cpn_sw) / (1.0 + r2hh)
    s2hl = (100.0 + cpn_sw) / (1.0 + r2hl)
    s2ll = (100.0 + cpn_sw) / (1.0 + r2ll)
    s1h = (0.5 * (s2hh + cpn_sw) + 0.5 * (s2hl + cpn_sw)) / (1.0 + r1h)
    s1l = (0.5 * (s2hl + cpn_sw) + 0.5 * (s2ll + cpn_sw)) / (1.0 + r1l)
    # Payer swaption payoff at t=1 = max(0, 100 - V_fixed_bond) per 100 par
    sw1h = max(0.0, 100.0 - s1h)
    sw1l = max(0.0, 100.0 - s1l)
    swaption_0 = np_ir * ((0.5 * sw1h + 0.5 * sw1l) / (1.0 + r0)) / 100.0

    vtext = (
        "Priya Nair, fixed-income derivatives analyst, is valuing interest rate derivatives using a calibrated binomial "
        "1-year forward interest rate tree with risk-neutral probability $\\pi = 0.50$ at every node:\n\n"
        f"- **$t = 0$**: $r_0 = {r0*100:.2f}\\%$\n"
        f"- **$t = 1$**: $r_{{1,H}} = {r1h*100:.2f}\\%$, $r_{{1,L}} = {r1l*100:.2f}\\%$\n"
        f"- **$t = 2$**: $r_{{2,HH}} = {r2hh*100:.2f}\\%$, $r_{{2,HL}} = {r2hl*100:.2f}\\%$, $r_{{2,LL}} = {r2ll*100:.2f}\\%$\n\n"
        "Nair evaluates four instruments off this tree:\n"
        f"1. A **caplet** on USD {np_ir:,.0f} notional resetting at $t = 1$ (based on $r_1$) and settling in arrears at $t = 2$ with strike rate $K = {k_cap*100:.2f}\\%$.\n"
        f"2. A **floorlet** on USD {np_ir:,.0f} notional resetting at $t = 2$ (based on $r_2$) and settling in arrears at $t = 3$ with strike rate $K = {k_cap*100:.2f}\\%$.\n"
        "3. A **1-year European call option** (strike 99.00% of par) on USD 1,000,000 par value of an option-free 3-year, 4.50% annual-pay bond.\n"
        "4. A **1-year European payer swaption** on USD 10,000,000 notional granting the right at $t = 1$ to pay 4.40% fixed annually in a 2-year swap (cash flows at $t = 2$ and $t = 3$)."
    )

    m, t = "DRV-LM12", "Valuation of Contingent Claims"
    # Q1: Caplet value
    opts, ans, dist = build_num_opts(
        caplet_0,
        (0.5 * pay1h_cap + 0.5 * pay1l_cap) / (1.0 + r0), "Fails to discount the t = 2 arrears settlement back to t = 1 by (1 + r1,H).",
        caplet_0 * (1.0 + r0), "Omits discounting from t = 1 back to t = 0 at (1 + r0).",
        lambda v: _fmt_usd(v, 0),
    )
    add_num_l2(
        qs, "L2-DRV-V07-Q1", m, t, "Interest Rate Caplet", vid, vtitle, vtext,
        "Value an interest rate caplet on a binomial interest rate tree.",
        "The value at $t = 0$ of the USD 10,000,000 interest rate caplet resetting at $t = 1$ is closest to:",
        opts, ans,
        f"At $t=1$, node H pays $10\\text{{M}}(0.054 - 0.042) = \\text{{USD }} 120,000$ at $t=2$, whose $t=1$ PV is $120,000 / 1.054 = \\text{{USD }} {pv1h_cap:,.2f}$. Node L pays 0. At $t=0$, value $= \\frac{{0.5({pv1h_cap:,.2f}) + 0}}{{1.040}} = \\text{{USD }} {caplet_0:,.0f}$.",
        dist,
    )

    # Q2: Year-2 floorlet
    opts, ans, dist = build_num_opts(
        floorlet_0,
        (0.5 * ((0.5 * (np_ir * max(0.0, k_cap - r2ll)) / (1.0 + r1l))) / (1.0 + r0)),
        "Omits discounting the t = 3 arrears floorlet payout back from t = 3 to t = 2 by (1 + r2,LL).",
        0.5 * pv1l_flr, "Omit discounting at r0 = 4.00% when folding node L back to t = 0.",
        lambda v: _fmt_usd(v, 0),
    )
    add_num_l2(
        qs, "L2-DRV-V07-Q2", m, t, "Interest Rate Floorlet", vid, vtitle, vtext,
        "Value a multi-period interest rate floorlet using backward induction.",
        "The value at $t = 0$ of the USD 10,000,000 interest rate floorlet resetting at $t = 2$ is closest to:",
        opts, ans,
        f"Only node $(2,LL)$ is in the money: $10\\text{{M}}(0.042 - 0.028)/1.028 = \\text{{USD }} {pv2ll_flr:,.2f}$ at $t=2$. Folding back to node $(1,L)$ gives $0.5({pv2ll_flr:,.2f})/1.034 = \\text{{USD }} {pv1l_flr:,.2f}$, and to $t=0$ gives $0.5({pv1l_flr:,.2f})/1.040 = \\text{{USD }} {floorlet_0:,.0f}$.",
        dist,
    )

    # Q3: Bond values at t=1 (ex-coupon)
    opts, ans, dist = build_text_opts(
        f"V(1,H) = {v1h:.2f}; V(1,L) = {v1l:.2f}",
        f"V(1,H) = {v1h + cpn:.2f}; V(1,L) = {v1l + cpn:.2f}",
        "Includes the t = 1 coupon of 4.50 instead of reporting the ex-coupon bond price at t = 1.",
        f"V(1,H) = {v2hh:.2f}; V(1,L) = {v2ll:.2f}",
        "Reports the t = 2 terminal-branch bond prices V(2,HH) and V(2,LL) rather than t = 1.",
        "B",
    )
    NUM_Q_IDS.add("L2-DRV-V07-Q3")
    add_num_l2(
        qs, "L2-DRV-V07-Q3", m, t, "Bond Valuation on Rate Tree", vid, vtitle, vtext,
        "Compute ex-coupon bond prices at intermediate nodes of a binomial rate tree.",
        "At $t = 1$, the ex-coupon prices per 100 par of the 3-year, 4.50% coupon bond at the high-rate ($r_{{1,H}}$) and low-rate ($r_{{1,L}}$) nodes are closest to:",
        opts, ans,
        f"At $t=2$: $V_{{HH}} = 104.50/1.068 = {v2hh:.4f}$, $V_{{HL}} = 104.50/1.046 = {v2hl:.4f}$, $V_{{LL}} = 104.50/1.028 = {v2ll:.4f}$. At $t=1$: $V_{{1,H}} = \\frac{{0.5({v2hh:.4f}+4.50)+0.5({v2hl:.4f}+4.50)}}{{1.054}} = {v1h:.2f}$; $V_{{1,L}} = \\frac{{0.5({v2hl:.4f}+4.50)+0.5({v2ll:.4f}+4.50)}}{{1.034}} = {v1l:.2f}$.",
        dist,
    )

    # Q4: European Call on Bond
    opts, ans, dist = build_num_opts(
        call_bond_usd,
        1_000_000.0 * (0.5 * c1h + 0.5 * c1l) / 100.0, "Fails to discount the t = 1 option payoff back to t = 0 at r0 = 4.00%.",
        1_000_000.0 * ((0.5 * max(0.0, (v1h + cpn) - k_bond) + 0.5 * max(0.0, (v1l + cpn) - k_bond)) / (1.0 + r0)) / 100.0,
        "Erroneously exercises on the cum-coupon bond price instead of the ex-coupon price.",
        lambda v: _fmt_usd(v, 0),
    )
    add_num_l2(
        qs, "L2-DRV-V07-Q4", m, t, "Bond Call Option", vid, vtitle, vtext,
        "Price a European call option on a coupon bond using an interest rate tree.",
        "At $t = 0$, the value of the 1-year European call option (strike 99.00% of par) on USD 1,000,000 par value of the 3-year 4.50% bond is closest to:",
        opts, ans,
        f"At $t=1$, $V_{{1,H}}={v1h:.4f} < 99.00$ (payoff 0), while $V_{{1,L}}={v1l:.4f} > 99.00$ (payoff ${c1l:.4f}$ per 100). Discounting to $t=0$: $\\frac{{0.5({c1l:.4f})}}{{1.040}} = {call_bond_pct:.4f}\\%$ of par, or $\\text{{USD }} {call_bond_usd:,.0f}$.",
        dist,
    )

    # Q5: 1-year European payer swaption (strike 4.40% on 2-yr swap covering t=2,3)
    opts, ans, dist = build_num_opts(
        swaption_0,
        np_ir * ((0.5 * max(0.0, s1l - 100.0)) / (1.0 + r0)) / 100.0, "Values a receiver swaption (in the money when rates fall) instead of a payer swaption.",
        np_ir * (0.5 * sw1h) / 100.0, "Fails to discount the t = 1 payer swaption payoff back to t = 0 by (1 + r0).",
        lambda v: _fmt_usd(v, 0),
    )
    add_num_l2(
        qs, "L2-DRV-V07-Q5", m, t, "Interest Rate Swaption", vid, vtitle, vtext,
        "Price a European payer swaption on a binomial interest rate tree.",
        "At $t = 0$, the value of the USD 10,000,000 1-year European **payer swaption** (strike 4.40% on the 2-year swap covering $t = 2$ and $t = 3$) is closest to:",
        opts, ans,
        f"A 4.40% coupon bond valued on the same tree from $t=1$ to $t=3$ yields $V_{{1,H}} = {s1h:.4f}$ and $V_{{1,L}} = {s1l:.4f}$. Pay-fixed swap value $= 100 - V_{{\\text{{fix}}}}$, which is positive only at node $(1,H)$: $100 - {s1h:.4f} = {sw1h:.4f}\\%$. At $t=0$, value $= 10\\text{{M}} \\times \\frac{{0.5({sw1h:.4f}\\%)}}{{1.040}} = \\text{{USD }} {swaption_0:,.0f}$.",
        dist,
    )


def build_v08(qs: list):
    """V08: BSM Model & Black Futures Option Model (using bsm_values!)."""
    vid = "DRV-V08"
    vtitle = "Black-Scholes-Merton (BSM) and Black Futures Option Pricing"

    # Equity BSM: Apex S0=120, K=125, r=4.5%, q=2.0%, T=0.5, sigma=28%
    s_eq, k_eq, r_eq, t_eq, sig_eq, q_eq = 120.0, 125.0, 0.045, 0.50, 0.28, 0.02
    res_eq = bsm_values(s_eq, k_eq, r_eq, t_eq, sig_eq, q_eq)

    # Check 4-dp table matches exact to 2 decimals!
    nd1_eq_4, nd2_eq_4 = round(res_eq["Nd1"], 4), round(res_eq["Nd2"], 4)
    c_eq_tab = s_eq * math.exp(-q_eq * t_eq) * nd1_eq_4 - k_eq * math.exp(-r_eq * t_eq) * nd2_eq_4
    assert round(c_eq_tab, 2) == round(res_eq["call"], 2)

    # Black Futures Option: F0=84, K=80, r=4.2%, T=0.75, sigma=32%
    f0_blk, k_blk, r_blk, t_blk, sig_blk = 84.0, 80.0, 0.042, 0.75, 0.32
    res_blk = bsm_values(f0_blk, k_blk, r_blk, t_blk, sig_blk, q=r_blk)
    nd1_blk_4, nd2_blk_4 = round(res_blk["Nd1"], 4), round(res_blk["Nd2"], 4)
    c_blk_tab = math.exp(-r_blk * t_blk) * (f0_blk * nd1_blk_4 - k_blk * nd2_blk_4)
    assert round(c_blk_tab, 2) == round(res_blk["call"], 2)

    # Garman-Kohlhagen FX Option: S=1.25 USD/GBP, K=1.24, r_usd=4.8%, r_gbp=4.0%, T=0.25, sigma=12%
    s_fx, k_fx, r_usd, r_gbp, t_fx, sig_fx = 1.25, 1.24, 0.048, 0.040, 0.25, 0.12
    res_fx = bsm_values(s_fx, k_fx, r_usd, t_fx, sig_fx, q=r_gbp)
    nd1_fx_4, nd2_fx_4 = round(res_fx["Nd1"], 4), round(res_fx["Nd2"], 4)
    c_fx_tab = s_fx * math.exp(-r_gbp * t_fx) * nd1_fx_4 - k_fx * math.exp(-r_usd * t_fx) * nd2_fx_4
    assert round(c_fx_tab, 4) == round(res_fx["call"], 4)

    vtext = (
        "Claire Laurent, quantitative options strategist at NorthStar Capital, applies the continuous-time Black-Scholes-Merton (BSM), "
        "Black (1976) futures option, and Garman-Kohlhagen currency option models across three trades:\n\n"
        f"1. **Apex Equity Option (BSM with Dividend Yield)**: Spot $S_0 = \\text{{USD }} {s_eq:.2f}$, strike $K = \\text{{USD }} {k_eq:.2f}$, "
        f"maturity $T = {t_eq:.2f}$ yr, continuous risk-free rate $r = {r_eq*100:.2f}\\%$, continuous dividend yield $q = {q_eq*100:.2f}\\%$, "
        f"volatility $\\sigma = {sig_eq*100:.1f}\\%$. Normal CDF values: $N(d_1) = {nd1_eq_4:.4f}$, $N(d_2) = {nd2_eq_4:.4f}$.\n\n"
        f"2. **Commodity Futures Option (Black Model)**: 9-month futures price $F_0 = \\text{{USD }} {f0_blk:.2f}$, strike $K_F = \\text{{USD }} {k_blk:.2f}$, "
        f"option maturity $T = {t_blk:.2f}$ yr, continuous risk-free rate $r = {r_blk*100:.2f}\\%$, futures volatility $\\sigma_F = {sig_blk*100:.1f}\\%$. "
        f"Normal CDF values: $N(d_1) = {nd1_blk_4:.4f}$, $N(d_2) = {nd2_blk_4:.4f}$.\n\n"
        f"3. **GBP/USD Currency Call Option (Garman-Kohlhagen)**: Spot $S_{{\\text{{FX}}}} = {s_fx:.4f}$ USD per GBP, strike $K_{{\\text{{FX}}}} = {k_fx:.4f}$, "
        f"maturity $T = {t_fx:.2f}$ yr, $r_{{\\text{{USD}}}} = {r_usd*100:.2f}\\%$, $r_{{\\text{{GBP}}}} = {r_gbp*100:.2f}\\%$, "
        f"volatility $\\sigma_{{\\text{{FX}}}} = {sig_fx*100:.1f}\\%$. Normal CDF values: $N(d_1) = {nd1_fx_4:.4f}$, $N(d_2) = {nd2_fx_4:.4f}$."
    )

    m, t = "DRV-LM12", "Valuation of Contingent Claims"
    # Q1: BSM call on Apex
    c_no_q = bsm_values(s_eq, k_eq, r_eq, t_eq, sig_eq, 0.0)["call"]
    opts, ans, dist = build_num_opts(
        res_eq["call"],
        c_no_q, "Omits the continuous dividend yield q = 2.0% from the BSM calculation.",
        s_eq * res_eq["Nd1"] - k_eq * math.exp(-r_eq * t_eq) * res_eq["Nd2"], "Omits exp(-qT) when discounting S0 * N(d1).",
        lambda v: _fmt_usd(v, 2),
    )
    add_num_l2(
        qs, "L2-DRV-V08-Q1", m, t, "BSM Equity Call", vid, vtitle, vtext,
        "Compute the Black-Scholes-Merton price of a European call with continuous dividend yield.",
        "Using the BSM model with continuous dividend yield, the fair value of the 6-month Apex call option is closest to:",
        opts, ans,
        f"$c_0 = S_0 e^{{-qT}} N(d_1) - K e^{{-rT}} N(d_2) = 120 e^{{-0.01}}({nd1_eq_4:.4f}) - 125 e^{{-0.0225}}({nd2_eq_4:.4f}) = \\text{{USD }} {res_eq['call']:.2f}$.",
        dist,
    )

    # Q2: BSM put on Apex
    opts, ans, dist = build_num_opts(
        res_eq["put"],
        res_eq["call"] + k_eq * math.exp(-r_eq * t_eq) - s_eq, "Omits the exp(-qT) carry adjustment on S0 in put-call parity.",
        res_eq["call"] + k_eq - s_eq * math.exp(-q_eq * t_eq), "Omits discounting the strike price K by exp(-rT).",
        lambda v: _fmt_usd(v, 2),
    )
    add_num_l2(
        qs, "L2-DRV-V08-Q2", m, t, "BSM Equity Put", vid, vtitle, vtext,
        "Compute the Black-Scholes-Merton price of a European put with continuous dividend yield.",
        "Using the BSM model (or carry-adjusted put-call parity), the fair value of the 6-month Apex put option with strike USD 125.00 is closest to:",
        opts, ans,
        f"$p_0 = K e^{{-rT}} N(-d_2) - S_0 e^{{-qT}} N(-d_1) = 125 e^{{-0.0225}}({1-nd2_eq_4:.4f}) - 120 e^{{-0.01}}({1-nd1_eq_4:.4f}) = \\text{{USD }} {res_eq['put']:.2f}$.",
        dist,
    )

    # Q3: Black futures call option
    opts, ans, dist = build_num_opts(
        res_blk["call"],
        f0_blk * res_blk["Nd1"] - k_blk * res_blk["Nd2"], "Fails to discount the futures call payoff by exp(-rT) in Black's model.",
        f0_blk * res_blk["Nd1"] - k_blk * math.exp(-r_blk * t_blk) * res_blk["Nd2"], "Fails to apply exp(-rT) to F0 * N(d1), treating the futures price like a non-dividend spot asset.",
        lambda v: _fmt_usd(v, 2),
    )
    add_num_l2(
        qs, "L2-DRV-V08-Q3", m, t, "Black Futures Call", vid, vtitle, vtext,
        "Calculate the price of a European call option on a futures contract using the Black model.",
        "Under the Black (1976) model, the fair value of the 9-month commodity futures call option is closest to:",
        opts, ans,
        f"Black futures call: $c_0 = e^{{-rT}}[F_0 N(d_1) - K_F N(d_2)] = e^{{-0.042(0.75)}}[84({nd1_blk_4:.4f}) - 80({nd2_blk_4:.4f})] = \\text{{USD }} {res_blk['call']:.2f}$.",
        dist,
    )

    # Q4: Black futures put option & BSM equivalence
    opts, ans, dist = build_num_opts(
        res_blk["put"],
        res_blk["call"] + k_blk - f0_blk, "Omits the exp(-rT) discount factor on (K_F - F0) in put-call-futures parity.",
        k_blk * math.exp(-r_blk * t_blk) * (1.0 - res_blk["Nd2"]) - f0_blk * (1.0 - res_blk["Nd1"]),
        "Omits discounting F0 * N(-d1) by exp(-rT).",
        lambda v: _fmt_usd(v, 2),
    )
    add_num_l2(
        qs, "L2-DRV-V08-Q4", m, t, "Black Futures Put", vid, vtitle, vtext,
        "Calculate the price of a European put option on a futures contract.",
        "The fair value of the 9-month commodity futures **put** option with strike USD 80.00 is closest to:",
        opts, ans,
        f"Black futures put: $p_0 = e^{{-rT}}[K_F N(-d_2) - F_0 N(-d_1)] = e^{{-0.0315}}[80({1-nd2_blk_4:.4f}) - 84({1-nd1_blk_4:.4f})] = \\text{{USD }} {res_blk['put']:.2f}$.",
        dist,
    )

    # Q5: Garman-Kohlhagen FX call on GBP 1,000,000 notional
    tot_fx_prem = 1_000_000.0 * res_fx["call"]
    # Distractor: swapped r_usd and r_gbp
    res_fx_swap = bsm_values(s_fx, k_fx, r_gbp, t_fx, sig_fx, q=r_usd)
    opts, ans, dist = build_num_opts(
        tot_fx_prem,
        1_000_000.0 * res_fx_swap["call"], "Reverses the domestic (USD) and foreign (GBP) risk-free interest rates in the Garman-Kohlhagen formula.",
        1_000_000.0 * bsm_values(s_fx, k_fx, r_usd, t_fx, sig_fx, q=0.0)["call"], "Omits the foreign GBP carry yield (r_GBP = 4.0%) from the spot exchange rate term.",
        lambda v: _fmt_usd(v, 0),
    )
    add_num_l2(
        qs, "L2-DRV-V08-Q5", m, t, "Currency Option Valuation", vid, vtitle, vtext,
        "Value a foreign currency option using the Garman-Kohlhagen (BSM) model.",
        "For a notional size of GBP 1,000,000, the total USD premium of the 3-month GBP call option (strike 1.2400 USD/GBP) is closest to:",
        opts, ans,
        f"Per GBP unit, $c_0 = 1.25 e^{{-0.04(0.25)}}({nd1_fx_4:.4f}) - 1.24 e^{{-0.048(0.25)}}({nd2_fx_4:.4f}) = \\text{{USD }} {res_fx['call']:.4f}$/GBP. Across GBP 1,000,000, total premium $= \\text{{USD }} {tot_fx_prem:,.0f}$.",
        dist,
    )


def build_v09(qs: list):
    """V09: Dynamic Delta Hedging & Gamma/Vega/Theta Neutrality."""
    vid = "DRV-V09"
    vtitle = "Strata Desk Dynamic Delta-Gamma-Vega-Theta Option Book Management"
    s0, r, q, sig = 100.0, 0.04, 0.0, 0.25
    k1, t1 = 100.0, 0.50
    k2, t2 = 110.0, 0.75
    n_short = 10_000.0

    res1 = bsm_values(s0, k1, r, t1, sig, q)
    res2 = bsm_values(s0, k2, r, t2, sig, q)
    th1_c, _ = bsm_theta(s0, k1, r, t1, sig, q)

    # Q1: Initial shares to delta-hedge short 10,000 Contract A calls
    sh_init = n_short * res1["delta_c"]

    # Q2: Delta+Gamma approximation P&L on delta-hedged short 10,000 Contract A for instant dS = +6.00
    # Hedged position: -10,000 calls + (10,000 * delta1) shares -> Delta_book = 0, Gamma_book = -10,000 * gamma1
    dS = 6.0
    pnl_dg = 0.5 * (-n_short * res1["gamma"]) * (dS ** 2)

    # Q3: Re-hedge shares needed when spot jumps immediately to S1 = 106 (with T unchanged at 0.50)
    res1_new = bsm_values(s0 + dS, k1, r, t1, sig, q)
    sh_new = n_short * res1_new["delta_c"]
    sh_add = sh_new - sh_init

    # Q4: Delta-Gamma Neutrality on initial unhedged short 10,000 Contract A using Contract B + shares
    # Gamma_P = -10,000 * gamma1; need n2 * gamma2 + Gamma_P = 0 -> n2 = +10,000 * (gamma1 / gamma2)
    n2_dg = n_short * (res1["gamma"] / res2["gamma"])
    # Delta_net = -10,000 * delta1 + n2 * delta2 + n_shares = 0 -> n_shares = 10,000*delta1 - n2*delta2
    sh_dg = n_short * res1["delta_c"] - n2_dg * res2["delta_c"]

    # Q5: Daily Theta P&L + +1.5% Vega shock on delta-hedged short 10,000 Contract A (1 day = 1/365, d_sigma = +0.015)
    # Short call collects POSITIVE theta = -n_short * (th1_c / 365), loses NEGATIVE vega = -n_short * vega1 * 0.015
    theta_1d = -n_short * (th1_c / 365.0)
    vega_shock = -n_short * res1["vega"] * 0.015
    net_tv = theta_1d + vega_shock

    vtext = (
        "Victor Reyes manages a market-making book on non-dividend-paying `TechCorp` ($S_0 = \\text{{USD }} 100.00$, continuous "
        f"$r = {r*100:.1f}\\%$, $q = 0\\%$, implied volatility $\\sigma = {sig*100:.1f}\\%$). The desk is currently **short 10,000 call options** "
        f"of Contract A ($K_1 = \\text{{USD }} {k1:.0f}$, $T_1 = {t1:.2f}$ yr). Exact BSM model Greeks per share are:\n\n"
        "| Contract | Strike | Maturity | $\\Delta$ | $\\Gamma$ | Vega ($\\mathcal{V}$, per 1.00 vol) | Annual $\\Theta$ |\n"
        "|---|---|---|---|---|---|---|\n"
        f"| Contract A | USD 100 | 0.50 yr | {res1['delta_c']:.4f} | {res1['gamma']:.5f} | {res1['vega']:.2f} | {th1_c:.2f} |\n"
        f"| Contract B | USD 110 | 0.75 yr | {res2['delta_c']:.4f} | {res2['gamma']:.5f} | {res2['vega']:.2f} | — |\n\n"
        f"*(Note: If `TechCorp` rallies immediately to USD 106.00 with $T_1 = 0.50$ yr, Contract A's call delta increases to {res1_new['delta_c']:.4f}.)*"
    )

    m, t = "DRV-LM12", "Valuation of Contingent Claims"
    # Q1: Initial shares to delta hedge
    opts, ans, dist = build_num_opts(
        sh_init,
        n_short * (1.0 - res1["delta_c"]), "Uses (1 - delta) instead of call delta.",
        -sh_init, "Recommends shorting shares instead of buying shares against a short call position.",
        lambda v: f"{'Buy' if v >= 0 else 'Short'} {abs(v):,.0f} shares",
    )
    add_num_l2(
        qs, "L2-DRV-V09-Q1", m, t, "Delta Hedging", vid, vtitle, vtext,
        "Determine the stock position required to delta-hedge an option portfolio.",
        "To render the short 10,000 Contract A call position **delta-neutral** at $t = 0$, the desk must:",
        opts, ans,
        f"The short call book has $\\Delta = -10,000 \\times {res1['delta_c']:.4f} = -{sh_init:,.1f}$. Neutralizing delta requires buying $+{sh_init:,.0f}$ shares of `TechCorp`.",
        dist,
    )

    # Q2: Delta-Gamma P&L for instant dS = +6.00
    opts, ans, dist = build_num_opts(
        pnl_dg,
        -pnl_dg, f"+USD {abs(pnl_dg):,.0f} reverses the gamma sign; a delta-hedged short option book has negative gamma and loses on large jumps.",
        2.0 * pnl_dg, "Forgets the 1/2 factor in the second-order Taylor gamma term (0.5 * Gamma * dS^2).",
        lambda v: _fmt_usd(v, 0),
    )
    add_num_l2(
        qs, "L2-DRV-V09-Q2", m, t, "Gamma Taylor Approximation", vid, vtitle, vtext,
        "Estimate hedged option portfolio P&L using the Delta-Gamma approximation.",
        "Suppose the desk maintains a delta-neutral book on short 10,000 Contract A calls and `TechCorp` jumps instantly by +USD 6.00 to USD 106.00. Using the Delta-Gamma Taylor approximation, the desk's estimated P&L is closest to:",
        opts, ans,
        f"Because net portfolio delta is zero, $\\Delta V \\approx \\frac{{1}}{{2}} \\Gamma_P (\\Delta S)^2 = \\frac{{1}}{{2}} (-10,000 \\times {res1['gamma']:.5f})(6.00)^2 = \\text{{USD }} {pnl_dg:,.0f}$.",
        dist,
    )

    # Q3: Re-hedging shares needed after jump to 106
    opts, ans, dist = build_num_opts(
        sh_add,
        sh_new, f"Buy {sh_new:,.0f} shares represents the total required share inventory rather than the additional shares to purchase.",
        -sh_add, "Recommends selling shares as the stock rises, whereas short calls require buying more shares when delta increases.",
        lambda v: f"{'Buy' if v >= 0 else 'Sell'} {abs(v):,.0f} additional shares",
    )
    add_num_l2(
        qs, "L2-DRV-V09-Q3", m, t, "Dynamic Re-Hedging", vid, vtitle, vtext,
        "Calculate the dynamic re-hedging trade after an underlying price move.",
        f"Immediately after `TechCorp` jumps to USD 106.00 (delta rises to {res1_new['delta_c']:.4f}), what share trade restores delta neutrality for the previously hedged book?",
        opts, ans,
        f"New required share holding is $10,000 \\times {res1_new['delta_c']:.4f} = {sh_new:,.0f}$ shares. Since {sh_init:,.0f} shares are already held, the desk must buy ${sh_new:,.0f} - {sh_init:,.0f} = {sh_add:,.0f}$ additional shares.",
        dist,
    )

    # Q4: Delta-Gamma Neutrality using Contract B + shares
    opts, ans, dist = build_text_opts(
        f"Buy {n2_dg:,.0f} Contract B calls and buy {sh_dg:,.0f} shares",
        f"Short {n2_dg:,.0f} Contract B calls and buy {n_short*res1['delta_c'] + n2_dg*res2['delta_c']:,.0f} shares",
        "Shorting Contract B adds further negative gamma instead of neutralizing the short Contract A gamma.",
        f"Buy {n2_dg:,.0f} Contract B calls and short {abs(sh_dg):,.0f} shares",
        "Check delta balance: short Contract A delta is negative and exceeds Contract B's positive delta, requiring net share purchases rather than share shorts.",
        "A",
    )
    NUM_Q_IDS.add("L2-DRV-V09-Q4")
    add_num_l2(
        qs, "L2-DRV-V09-Q4", m, t, "Delta-Gamma Neutralization", vid, vtitle, vtext,
        "Construct a simultaneous delta-neutral and gamma-neutral option hedge.",
        "Returning to $t = 0$ ($S_0 = 100$, unhedged short 10,000 Contract A calls), which trades in Contract B calls and `TechCorp` shares establish **both** gamma and delta neutrality?",
        opts, ans,
        f"To neutralize gamma: $n_B = \\frac{{10,000 \\times {res1['gamma']:.5f}}}{{{res2['gamma']:.5f}}} = +{n2_dg:,.0f}$ Contract B calls (bought). Remaining portfolio delta $= -10,000({res1['delta_c']:.4f}) + {n2_dg:,.0f}({res2['delta_c']:.4f}) = -{sh_dg:,.0f}$, requiring buying $+{sh_dg:,.0f}$ shares.",
        dist,
    )

    # Q5: 1-day Theta + 1.5% Vega shock
    opts, ans, dist = build_num_opts(
        net_tv,
        -theta_1d - vega_shock, "Reverses the signs of both theta and vega (treating the position as long options rather than short).",
        theta_1d + (-n_short * res1["vega"] * 1.5), "Multiplies per-1.00-vol vega by 1.5 instead of 0.015.",
        lambda v: _fmt_usd(v, 0),
    )
    add_num_l2(
        qs, "L2-DRV-V09-Q5", m, t, "Theta vs. Vega Trade-off", vid, vtitle, vtext,
        "Quantify net P&L from time decay (theta) and implied volatility shifts (vega).",
        "Over 1 calendar day ($\\Delta t = 1/365$), `TechCorp` stays at USD 100.00 while implied volatility increases by +1.50 percentage points ($\\Delta \\sigma = +0.015$). Using Theta and Vega, the net 1-day P&L of the delta-hedged short 10,000 Contract A position is closest to:",
        opts, ans,
        f"Short options earn positive daily time decay: $-10,000 \\times ({th1_c:.2f} / 365) = +\\text{{USD }} {theta_1d:,.0f}$. Higher volatility hurts short options: $-10,000 \\times {res1['vega']:.2f} \\times 0.015 = -\\text{{USD }} {abs(vega_shock):,.0f}$. Net P&L $= \\text{{USD }} {net_tv:,.0f}$.",
        dist,
    )


def build_v10(qs: list):
    """V10: Option Strategies (Bull/Bear Spreads, Butterfly, Straddle, Collar)."""
    vid = "DRV-V10"
    vtitle = "Horizon Equity Advisors Multi-Strategy Option Overlays"
    # Build arbitrage-free 3-month European option chain using bsm_values!
    s0, r, q, T, sig = 80.0, 0.04, 0.0, 0.25, 0.25
    strikes = [70.0, 75.0, 80.0, 85.0, 90.0]
    chain = {}
    for k in strikes:
        res = bsm_values(s0, k, r, T, sig, q)
        chain[k] = (round(res["call"], 2), round(res["put"], 2))

    # 1. Bull call spread: long K=75 call, short K=85 call
    c75, p75 = chain[75.0]
    c80, p80 = chain[80.0]
    c85, p85 = chain[85.0]

    bull_cost = c75 - c85
    bull_max_prof = (85.0 - 75.0) - bull_cost
    bull_be = 75.0 + bull_cost

    # 2. Bear put spread: long K=85 put, short K=75 put -> P&L at ST = 72.00
    bear_cost = p85 - p75
    st_bear = 72.0
    bear_pnl = (max(0.0, 85.0 - st_bear) - max(0.0, 75.0 - st_bear)) - bear_cost

    # 3. Long call butterfly: long 1 c75, short 2 c80, long 1 c85 -> max profit & breakevens
    fly_cost = c75 - 2.0 * c80 + c85
    fly_max_prof = (80.0 - 75.0) - fly_cost

    # 4. Long straddle at K=80 -> P&L at ST = 91.50
    strad_cost = c80 + p80
    st_strad = 91.50
    strad_pnl = (max(0.0, st_strad - 80.0) + max(0.0, 80.0 - st_strad)) - strad_cost

    # 5. Protective collar on 1,000 shares at S0=80: long K=75 put, short K=85 call -> max profit
    col_net_cost = p75 - c85
    col_max_prof = 1000.0 * ((85.0 - 80.0) - col_net_cost)

    rows = "\n".join(
        f"| USD {k:.0f} | USD {chain[k][0]:.2f} | USD {chain[k][1]:.2f} |" for k in strikes
    )
    vtext = (
        "Devon Morales, derivatives strategist at Horizon Equity Advisors, evaluates five 3-month European option strategies "
        f"on `GlobalRetail` (currently trading at $S_0 = \\text{{USD }} {s0:.2f}$). Available 3-month option premiums per share are:\n\n"
        "| Strike ($K$) | Call Price ($c$) | Put Price ($p$) |\n"
        "|---|---|---|\n"
        f"{rows}\n"
    )

    m, t = "DRV-LM12", "Option Strategies"
    # Q1: Bull Call Spread (75/85) max profit and breakeven
    opts, ans, dist = build_text_opts(
        f"Max profit = USD {bull_max_prof:.2f}; Breakeven = USD {bull_be:.2f}",
        f"Max profit = USD {bull_cost:.2f}; Breakeven = USD {85.0 - bull_cost:.2f}",
        "Confuses the bull call spread's maximum loss (initial debit) with maximum profit and uses the bear put breakeven formula.",
        f"Max profit = USD 10.00; Breakeven = USD 75.00",
        "Ignores the net premium paid when computing maximum profit and breakeven.",
        "B",
    )
    NUM_Q_IDS.add("L2-DRV-V10-Q1")
    add_num_l2(
        qs, "L2-DRV-V10-Q1", m, t, "Bull Call Spread", vid, vtitle, vtext,
        "Calculate maximum profit and breakeven for a bull call spread.",
        "For a **bull call spread** constructed by buying the USD 75 call and selling the USD 85 call, the maximum profit per share and breakeven stock price at expiration are:",
        opts, ans,
        f"Net debit $= c_{{75}} - c_{{85}} = {c75:.2f} - {c85:.2f} = \\text{{USD }} {bull_cost:.2f}$. Max profit $= (85 - 75) - {bull_cost:.2f} = \\text{{USD }} {bull_max_prof:.2f}$ (when $S_T \\ge 85$). Breakeven $= 75 + {bull_cost:.2f} = \\text{{USD }} {bull_be:.2f}$.",
        dist,
    )

    # Q2: Bear Put Spread (85/75) P&L at ST=72
    opts, ans, dist = build_num_opts(
        bear_pnl,
        13.0 - bear_cost, "Uses gross payoff 85 - 72 = USD 13.00 instead of capping the payoff at the USD 75 short put strike.",
        (85.0 - 75.0) + bear_cost, "Adds the net put spread premium instead of subtracting the initial debit.",
        lambda v: _fmt_usd(v, 2),
    )
    add_num_l2(
        qs, "L2-DRV-V10-Q2", m, t, "Bear Put Spread", vid, vtitle, vtext,
        "Calculate expiration profit for a bear put spread.",
        f"For a **bear put spread** (long USD 85 put, short USD 75 put), if `GlobalRetail` closes at USD {st_bear:.2f} at expiration, the net profit per share is:",
        opts, ans,
        f"Net debit $= p_{{85}} - p_{{75}} = {p85:.2f} - {p75:.2f} = \\text{{USD }} {bear_cost:.2f}$. At $S_T = 72$, both puts expire in the money, capping gross payoff at $85 - 75 = \\text{{USD }} 10.00$. Net profit $= 10.00 - {bear_cost:.2f} = \\text{{USD }} {bear_pnl:.2f}$.",
        dist,
    )

    # Q3: Long Call Butterfly (75/80/85) max profit
    opts, ans, dist = build_num_opts(
        fly_max_prof,
        fly_cost, f"USD {fly_cost:.2f} is the initial net debit (maximum loss) of the butterfly spread, not its maximum profit.",
        5.00, "USD 5.00 is the maximum gross payoff at ST = 80 without deducting the net option debit.",
        lambda v: _fmt_usd(v, 2),
    )
    add_num_l2(
        qs, "L2-DRV-V10-Q3", m, t, "Butterfly Spread", vid, vtitle, vtext,
        "Determine the maximum profit and cost of a long call butterfly spread.",
        "For a **long call butterfly spread** (long 1 USD 75 call, short 2 USD 80 calls, long 1 USD 85 call), the maximum profit per spread at expiration is:",
        opts, ans,
        f"Net debit $= c_{{75}} - 2c_{{80}} + c_{{85}} = {c75:.2f} - 2({c80:.2f}) + {c85:.2f} = \\text{{USD }} {fly_cost:.2f}$. Maximum gross payoff at $S_T = 80$ is $80 - 75 = \\text{{USD }} 5.00$, giving max profit $= 5.00 - {fly_cost:.2f} = \\text{{USD }} {fly_max_prof:.2f}$.",
        dist,
    )

    # Q4: Long Straddle at K=80
    opts, ans, dist = build_num_opts(
        strad_pnl,
        (st_strad - 80.0) - c80, "Deducts only the call premium instead of the combined call + put straddle cost.",
        (st_strad - 80.0) + strad_cost, "Adds the straddle premium instead of subtracting it from expiration payoff.",
        lambda v: _fmt_usd(v, 2),
    )
    add_num_l2(
        qs, "L2-DRV-V10-Q4", m, t, "Long Straddle", vid, vtitle, vtext,
        "Evaluate profit and breakevens for a long straddle.",
        f"For a **long straddle** at $K = \\text{{USD }} 80$ (long USD 80 call and long USD 80 put), if `GlobalRetail` settles at USD {st_strad:.2f} at expiration, the net profit per share is:",
        opts, ans,
        f"Straddle cost $= c_{{80}} + p_{{80}} = {c80:.2f} + {p80:.2f} = \\text{{USD }} {strad_cost:.2f}$. Gross payoff at $S_T = 91.50$ is $91.50 - 80.00 = \\text{{USD }} 11.50$, netting $11.50 - {strad_cost:.2f} = \\text{{USD }} {strad_pnl:.2f}$.",
        dist,
    )

    # Q5: Protective Collar on 1,000 shares
    opts, ans, dist = build_num_opts(
        col_max_prof,
        1000.0 * (85.0 - 80.0), "USD 5,000 ignores the net credit/debit between the USD 75 put and USD 85 call.",
        1000.0 * ((85.0 - 80.0) + col_net_cost), "Adds the net option outlay instead of subtracting it (or confuses debit vs credit).",
        lambda v: _fmt_usd(v, 0),
    )
    add_num_l2(
        qs, "L2-DRV-V10-Q5", m, t, "Protective Collar", vid, vtitle, vtext,
        "Calculate maximum profit and floor value for a protective collar.",
        "A client holding 1,000 shares of `GlobalRetail` (worth USD 80.00/share) establishes a **collar** by buying 1,000 USD 75 puts and selling 1,000 USD 85 calls. Relative to today's USD 80,000 equity value, the collar's maximum net profit at expiration is:",
        opts, ans,
        f"Net option cost $= p_{{75}} - c_{{85}} = {p75:.2f} - {c85:.2f} = \\text{{USD }} {col_net_cost:+.2f}$/share (a net credit if negative, or debit if positive). At $S_T \\ge 85$, shares are called at USD 85, giving max profit $= 1,000 \\times [(85 - 80) - ({col_net_cost:.2f})] = \\text{{USD }} {col_max_prof:,.0f}$.",
        dist,
    )


def build_v11(qs: list):
    """V11: Currency Hedging Ratios & Cross-Hedging."""
    vid = "DRV-V11"
    vtitle = "Meridian Global Currency Hedging Ratios and Cross-Hedging"
    # Portfolio 1: EUR 20M, S0=1.1000 USD/EUR, F0=1.1220 USD/EUR
    eur_p1 = 20_000_000.0
    s0_e, f0_e = 1.1000, 1.1220
    r_fc1 = 0.0850
    s1_e = 1.0560  # -4.0% FX return
    r_fx1 = (s1_e - s0_e) / s0_e

    # Cash flow math in USD:
    v0_usd = eur_p1 * s0_e  # USD 22,000,000
    v1_eur = eur_p1 * (1.0 + r_fc1)  # EUR 21,700,000
    v1_usd_unhedged = v1_eur * s1_e
    r_dc_unhedged = v1_usd_unhedged / v0_usd - 1.0
    # 100%-notional forward hedge on initial EUR 20M: gain = EUR 20M * (1.1220 - 1.0560)
    fwd_pnl_100 = eur_p1 * (f0_e - s1_e)
    v1_usd_hedged = v1_usd_unhedged + fwd_pnl_100
    r_dc_hedged = v1_usd_hedged / v0_usd - 1.0

    # MVHR for Portfolio 1: sig_fc=14%, sig_fx=9%, rho=-0.35
    sig_fc, sig_fx, rho_fx = 0.14, 0.09, -0.35
    h_star = 1.0 + rho_fx * (sig_fc / sig_fx)  # 1 + (-0.35)(14/9) = 0.455556
    eur_sell_mvhr = eur_p1 * h_star

    # Portfolio 2: Cross-Hedge CHF 15M using CME EUR futures
    # Spot USD/CHF = 1.1400 -> USD exposure = CHF 15M * 1.1400 = USD 17,100,000
    chf_p2, s0_chf = 15_000_000.0, 1.1400
    usd_exp2 = chf_p2 * s0_chf
    f_eur_cme, mult_eur = 1.1050, 125_000.0
    v_fut_usd = f_eur_cme * mult_eur  # USD 138,125 per contract
    sig_dS, sig_dF, rho_cross = 0.082, 0.095, 0.88
    h_cross = rho_cross * (sig_dS / sig_dF)
    n_fut_cross = h_cross * (usd_exp2 / v_fut_usd)

    # Portfolio 3: JPY bond roll/carry yield (S0=150 JPY/USD, 3M F0=148.50 JPY/USD)
    # In USD per JPY terms: S0_usd_jpy = 1/150, F0_usd_jpy = 1/148.50 -> (F0_usd_jpy - S0_usd_jpy)/S0_usd_jpy = 150/148.50 - 1
    s0_jpy, f0_jpy = 150.0, 148.50
    carry_3m = (s0_jpy / f0_jpy) - 1.0
    carry_ann = carry_3m * 4.0

    # Q5: Portfolio variance reduction check: Var(R_dc) with hedge h:
    # R_dc(h) = R_fc + (1 - h) * R_fx (linear approximation used in MVHR derivation)
    var_unhedged = sig_fc ** 2 + sig_fx ** 2 + 2.0 * rho_fx * sig_fc * sig_fx
    var_mvhr = sig_fc ** 2 + ((1.0 - h_star) ** 2) * (sig_fx ** 2) + 2.0 * (1.0 - h_star) * rho_fx * sig_fc * sig_fx
    vol_unhedged = math.sqrt(var_unhedged)
    vol_mvhr = math.sqrt(var_mvhr)

    vtext = (
        "Kenji Takahashi, currency overlay manager at Meridian Global (USD reporting currency), manages hedging ratios "
        "across three international sleeves:\n\n"
        f"1. **European Equity Sleeve**: Market value EUR {eur_p1:,.0f}; initial spot $S_0 = {s0_e:.4f}$ USD/EUR; "
        f"1-year forward $F_0 = {f0_e:.4f}$ USD/EUR. Over the year, the EUR asset return is $R_{{\\text{{FC}}}} = +{r_fc1*100:.2f}\\%$ "
        f"and spot ends at $S_1 = {s1_e:.4f}$ USD/EUR. Historical risk estimates for this sleeve are $\\sigma(R_{{\\text{{FC}}}}) = {sig_fc*100:.1f}\\%$, "
        f"$\\sigma(R_{{\\text{{FX}}}}) = {sig_fx*100:.1f}\\%$, and correlation $\\rho(R_{{\\text{{FC}}}}, R_{{\\text{{FX}}}}) = {rho_fx:.2f}$.\n\n"
        f"2. **Swiss Industrial Cross-Hedge**: CHF {chf_p2:,.0f} asset exposure (spot {s0_chf:.4f} USD/CHF), hedged using CME EUR futures "
        f"(contract size EUR {mult_eur:,.0f}, futures price {f_eur_cme:.4f} USD/EUR). Regressing $\\Delta S_{{\\text{{USD/CHF}}}}$ on "
        f"$\\Delta F_{{\\text{{USD/EUR}}}}$ yields $\\sigma_{{\\Delta S}} = {sig_dS:.3f}$, $\\sigma_{{\\Delta F}} = {sig_dF:.3f}$, and $\\rho = {rho_cross:.2f}$.\n\n"
        f"3. **Japanese Bond Carry**: JPY 1,500,000,000 bond position hedged via 3-month forwards when spot is {s0_jpy:.2f} JPY/USD "
        f"and the 3-month forward is {f0_jpy:.2f} JPY/USD."
    )

    m, t = "DRV-LM13", "Currency Risk Management"
    # Q1: 100%-notional forward hedged USD return on Sleeve 1
    opts, ans, dist = build_num_opts(
        r_dc_hedged,
        r_dc_unhedged, f"{r_dc_unhedged*100:.2f}% is the unhedged USD return rather than the forward-hedged USD return.",
        (1.0 + r_fc1) * (f0_e / s0_e) - 1.0 + 0.005, "Overstates the forward hedge gain by applying forward points to unrealized gains beyond initial notional.",
        lambda v: _fmt_pct(v, 2),
    )
    # Better distinct d2 for Q1: (1+r_fc1)*(f0_e/s0_e)-1 = 10.67% vs exact 10.33% (difference 0.34%!)
    d2_q1 = (1.0 + r_fc1) * (f0_e / s0_e) - 1.0
    opts, ans, dist = build_num_opts(
        r_dc_hedged,
        r_dc_unhedged, f"{r_dc_unhedged*100:.2f}% is the unhedged USD return without the forward contract payoff.",
        d2_q1, f"{d2_q1*100:.2f}% assumes the forward hedged the unknown ending value EUR 21.70M rather than the initial EUR 20.00M notional.",
        lambda v: _fmt_pct(v, 2),
    )
    add_num_l2(
        qs, "L2-DRV-V11-Q1", m, t, "Hedged Portfolio Return", vid, vtitle, vtext,
        "Calculate the domestic-currency return of a forward-hedged foreign equity portfolio.",
        "If Takahashi sold a 1-year forward for exactly EUR 20,000,000 at $F_0 = 1.1220$, the realized 1-year **hedged USD return** on Sleeve 1 is closest to:",
        opts, ans,
        f"Initial value $= \\text{{USD }} {v0_usd:,.0f}$. Unhedged ending USD value $= 20\\text{{M}}(1.085)(1.0560) = \\text{{USD }} {v1_usd_unhedged:,.0f}$. Forward gain $= 20\\text{{M}}(1.1220 - 1.0560) = \\text{{USD }} {fwd_pnl_100:,.0f}$. Total $= \\text{{USD }} {v1_usd_hedged:,.0f}$, giving $({v1_usd_hedged:,.0f}/{v0_usd:,.0f}) - 1 = {r_dc_hedged*100:.2f}\\%$.",
        dist,
    )

    # Q2: MVHR h* and EUR forward notional to sell
    opts, ans, dist = build_num_opts(
        eur_sell_mvhr,
        eur_p1 * (1.0 - rho_fx * (sig_fc / sig_fx)), "Adds -rho*(sig_FC/sig_FX) instead of adding +rho*(sig_FC/sig_FX), producing an over-hedge (>100%) despite negative correlation.",
        eur_p1 * abs(rho_fx * (sig_fc / sig_fx)), "Uses only |rho*(sig_FC/sig_FX)| instead of 1 + rho*(sig_FC/sig_FX).",
        lambda v: _fmt_eur(v, 0),
    )
    add_num_l2(
        qs, "L2-DRV-V11-Q2", m, t, "Minimum-Variance Hedge Ratio", vid, vtitle, vtext,
        "Compute the minimum-variance currency hedge ratio and optimal forward notional.",
        "Using the minimum-variance hedge ratio (MVHR) for the European equity sleeve ($R_{\\text{DC}} \\approx R_{\\text{FC}} + R_{\\text{FX}}$), the optimal EUR notional to sell forward is closest to:",
        opts, ans,
        f"$h^* = 1 + \\rho \\frac{{\\sigma(R_{{\\text{{FC}}}})}}{{\\sigma(R_{{\\text{{FX}}}})}} = 1 + (-0.35)\\left(\\frac{{14\\%}}{{9\\%}}\\right) = {h_star:.4f}$ (45.56% hedge). Optimal forward sale $= 0.455556 \\times \\text{{EUR }} 20,000,000 = \\text{{EUR }} {eur_sell_mvhr:,.0f}$.",
        dist,
    )

    # Q3: Cross-hedge optimal CME EUR futures contracts
    opts, ans, dist = build_num_opts(
        round(n_fut_cross),
        round(usd_exp2 / v_fut_usd), "124 contracts applies a naive 100% notional hedge without adjusting by the cross-hedge MVHR (0.7596).",
        round(h_cross * (chf_p2 / mult_eur)), "91 contracts fails to translate CHF exposure and EUR contract size into common USD values.",
        lambda v: f"Short {v:,.0f} contracts",
    )
    add_num_l2(
        qs, "L2-DRV-V11-Q3", m, t, "Cross-Currency Futures Hedge", vid, vtitle, vtext,
        "Calculate the optimal number of futures contracts in a currency cross-hedge.",
        "To minimize variance on the CHF 15,000,000 Swiss exposure using CME EUR futures, Takahashi should:",
        opts, ans,
        f"Cross-hedge MVHR $h^* = \\rho \\frac{{\\sigma_{{\\Delta S}}}}{{\\sigma_{{\\Delta F}}}} = 0.88 \\times \\frac{{0.082}}{{0.095}} = {h_cross:.4f}$. USD exposure $= 15\\text{{M}} \\times 1.1400 = \\text{{USD }} {usd_exp2:,.0f}$, and one EUR futures contract $= 125,000 \\times 1.1050 = \\text{{USD }} {v_fut_usd:,.0f}$. Contracts $= {h_cross:.4f} \\times ({usd_exp2:,.0f}/{v_fut_usd:,.0f}) = {n_fut_cross:.1f}$ (short {round(n_fut_cross)} contracts).",
        dist,
    )

    # Q4: Annualized forward carry on JPY bond hedge
    opts, ans, dist = build_num_opts(
        carry_ann,
        -carry_ann, "-4.04% reverses the quote direction; because JPY/USD is quoted in JPY per USD, a lower forward rate (148.50 < 150.00) reflects a forward premium on JPY.",
        carry_3m, f"+{carry_3m*100:.2f}% is the unannualized 3-month forward carry rather than the annualized roll yield.",
        lambda v: _fmt_pct(v, 2),
    )
    add_num_l2(
        qs, "L2-DRV-V11-Q4", m, t, "Forward Carry and Roll Yield", vid, vtitle, vtext,
        "Compute annualized forward carry on a currency hedge.",
        "For the Japanese bond exposure (selling JPY forward against USD for 3 months), the annualized **forward carry (roll yield)** earned by the USD investor is closest to:",
        opts, ans,
        f"In USD per JPY terms, $S_0 = 1/150.00$ and $F_0 = 1/148.50$, so selling JPY forward earns $\\frac{{150.00}}{{148.50}} - 1 = +{carry_3m*100:.4f}\\%$ over 3 months, or $4 \\times {carry_3m*100:.4f}\\% = +{carry_ann*100:.2f}\\%$ annualized.",
        dist,
    )

    # Q5: Portfolio volatility reduction under MVHR vs unhedged
    opts, ans, dist = build_num_opts(
        vol_mvhr,
        vol_unhedged, f"{vol_unhedged*100:.2f}% is the unhedged USD return volatility rather than the MVHR-hedged volatility.",
        sig_fc, "14.00% assumes a 100% static hedge (h = 1.00), which leaves higher portfolio volatility than the optimal MVHR (h* = 0.4556) when rho < 0.",
        lambda v: _fmt_pct(v, 2),
    )
    add_num_l2(
        qs, "L2-DRV-V11-Q5", m, t, "MVHR Volatility Minimization", vid, vtitle, vtext,
        "Evaluate portfolio volatility under an optimal minimum-variance currency hedge.",
        "Under the linear approximation $R_{\\text{DC}}(h) \\approx R_{\\text{FC}} + (1 - h) R_{\\text{FX}}$, applying the optimal MVHR ($h^* = 0.4556$) reduces Sleeve 1's USD return standard deviation to closest to:",
        opts, ans,
        f"Unhedged variance $= 0.14^2 + 0.09^2 + 2(-0.35)(0.14)(0.09) = {var_unhedged:.6f}$ ($\\sigma = {vol_unhedged*100:.2f}\\%$). At $h^* = 0.4556$ ($1 - h^* = 0.5444$), variance $= 0.14^2 + (0.5444)^2(0.09^2) + 2(0.5444)(-0.35)(0.14)(0.09) = {var_mvhr:.6f}$, yielding $\\sigma = {vol_mvhr*100:.2f}\\%$ (below the 14.00% fully hedged volatility).",
        dist,
    )


def main():
    questions = []
    build_l1_lm1_to_lm3(questions)
    build_l1_lm4_to_lm6(questions)
    build_l1_lm7_to_lm10(questions)

    build_v01(questions)
    build_v02(questions)
    build_v03(questions)
    build_v04(questions)
    build_v05(questions)
    build_v06(questions)
    build_v07(questions)
    build_v08(questions)
    build_v09(questions)
    build_v10(questions)
    build_v11(questions)

    l1 = [q for q in questions if q["level"] == 1]
    l2 = [q for q in questions if q["level"] == 2]
    assert len(l1) == 85, f"Expected 85 L1 questions, got {len(l1)}"
    assert len(l2) == 55, f"Expected 55 L2 questions, got {len(l2)}"
    assert len(questions) == 140, f"Expected 140 total questions, got {len(questions)}"

    num_pct = 100.0 * len(NUM_Q_IDS) / len(questions)
    assert num_pct >= 75.0, f"Numerical share {num_pct:.1f}% is below 75%"

    ans_dist = {k: sum(1 for q in questions if q["answer"] == k) for k in ("A", "B", "C")}
    save_validated_json(questions, OUT_PATH)
    print(
        f"Verified: L1={len(l1)}, L2={len(l2)}, Total={len(questions)}, "
        f"Numerical={len(NUM_Q_IDS)}/{len(questions)} ({num_pct:.1f}%), "
        f"Answers={ans_dist}, Errors=0"
    )


if __name__ == "__main__":
    main()
