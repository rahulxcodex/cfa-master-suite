"""
Generate 130 validated CFA Corporate Issuers questions (80 Level 1 + 50 Level 2 across 10 vignettes).
Output: data/courses/corp_qbank.json
"""
import os
import sys

SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(SCRIPTS_DIR)
if SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, SCRIPTS_DIR)

from qbank_helper import add_l1, add_l2, save_validated_json  # noqa: E402


def calc_irr(cfs: list[float]) -> float:
    """Compute Internal Rate of Return (IRR) via bracket scan + Newton/bisection."""
    def npv(r: float) -> float:
        return sum(cf / ((1.0 + r) ** t) for t, cf in enumerate(cfs))

    def dnpv(r: float) -> float:
        return sum(-t * cf / ((1.0 + r) ** (t + 1)) for t, cf in enumerate(cfs) if t > 0)

    # Scan for sign change across (-0.95, 5.0)
    grid = [-0.90 + i * 0.01 for i in range(590)]
    lo, hi = None, None
    prev_r = grid[0]
    prev_val = npv(prev_r)
    for r in grid[1:]:
        val = npv(r)
        if prev_val == 0.0:
            return prev_r
        if prev_val * val < 0.0:
            lo, hi = prev_r, r
            break
        prev_r, prev_val = r, val

    if lo is None or hi is None:
        # Fallback Newton from 0.10
        r = 0.10
        for _ in range(200):
            f = npv(r)
            df = dnpv(r)
            if abs(f) < 1e-10:
                return r
            if abs(df) < 1e-12:
                break
            r = max(-0.95, r - f / df)
        raise ValueError(f"IRR failed to converge for cashflows {cfs}")

    # Bisection + Newton refinement
    f_lo = npv(lo)
    for _ in range(120):
        mid = 0.5 * (lo + hi)
        f_mid = npv(mid)
        if abs(f_mid) < 1e-11 or (hi - lo) < 1e-12:
            return mid
        if f_lo * f_mid <= 0.0:
            hi = mid
        else:
            lo = mid
            f_lo = f_mid
    return 0.5 * (lo + hi)


KEY_CYCLE = ["B", "C", "A", "C", "A", "B", "A", "C", "B", "A", "B", "C"]


def make_opts(correct: str, w1: str, why1: str, w2: str, why2: str, idx: int):
    """Arrange 3 unique options deterministically across A/B/C with exact distractor map."""
    assert len({correct, w1, w2}) == 3, f"Duplicate option text detected at idx={idx}: {(correct, w1, w2)}"
    ans = KEY_CYCLE[idx % len(KEY_CYCLE)]
    rem = [k for k in ("A", "B", "C") if k != ans]
    options = {ans: correct, rem[0]: w1, rem[1]: w2}
    distractors = {rem[0]: why1, rem[1]: why2}
    return options, distractors, ans


def assert_no_control_escapes(items: list[dict]):
    """Guard against accidental unescaped backslash sequences like \\t, \\f, \\b, \\r in LaTeX."""
    bad = ("\t", "\f", "\b", "\r", "\a", "\v")
    for q in items:
        fields = [
            ("question", q["question"]),
            ("explanation", q["explanation"]),
            ("optA", q["options"]["A"]),
            ("optB", q["options"]["B"]),
            ("optC", q["options"]["C"]),
        ]
        if "vignette_text" in q:
            fields.append(("vignette_text", q["vignette_text"]))
        for dk, dv in q["distractor_analysis"].items():
            fields.append((f"dist_{dk}", dv))
        for fname, val in fields:
            for ch in bad:
                assert ch not in val, f"{q['id']}.{fname} contains control char {repr(ch)} (likely unescaped LaTeX backslash)"


SUBJ = "Corporate Issuers"
questions: list[dict] = []
calc_flags: list[bool] = []


def add_q1(
    qid: str,
    mod: str,
    topic: str,
    subtopic: str,
    los: str,
    qtext: str,
    correct: str,
    w1: str,
    why1: str,
    w2: str,
    why2: str,
    expl: str,
    is_calc: bool,
):
    idx = len(questions)
    opts, dists, ans = make_opts(correct, w1, why1, w2, why2, idx)
    add_l1(questions, qid, SUBJ, mod, topic, subtopic, los, qtext, opts, ans, expl, dists)
    calc_flags.append(is_calc)


def add_q2(
    qid: str,
    mod: str,
    topic: str,
    subtopic: str,
    vid: str,
    vtitle: str,
    vtext: str,
    los: str,
    qtext: str,
    correct: str,
    w1: str,
    why1: str,
    w2: str,
    why2: str,
    expl: str,
    is_calc: bool,
):
    idx = len(questions)
    opts, dists, ans = make_opts(correct, w1, why1, w2, why2, idx)
    add_l2(questions, qid, SUBJ, mod, topic, subtopic, vid, vid, vtitle, vtext, los, qtext, opts, ans, expl, dists)
    calc_flags.append(is_calc)


# =============================================================================
# LEVEL 1: MODULE 1 — CORPORATE STRUCTURES & OWNERSHIP (L1-CRP-001 .. 010)
# =============================================================================
M1 = "CI-L1-M1"
T1 = "Corporate Structures & Ownership"

add_q1(
    "L1-CRP-001", M1, T1, "Legal Forms of Business",
    "Compare the legal liability, taxation, and operational features of sole proprietorships, partnerships, and corporations.",
    "In a limited partnership (LP) structure used by a private investment fund, which statement best characterizes the legal liability and tax treatment of the partners?",
    "The general partner bears unlimited personal liability for partnership obligations, whereas limited partners enjoy liability capped at their invested capital and pass-through tax treatment.",
    "Both general and limited partners enjoy limited liability capped at capital contributed, while the partnership itself pays corporate income tax before distributions.",
    "Confuses a limited partnership with a C-corporation or LLP; in a standard LP, the general partner retains unlimited liability and income passes through to partners without entity-level corporate tax.",
    "Limited partners actively manage daily operations alongside the general partner and face joint and several unlimited liability if the fund defaults.",
    "Reverses the statutory role of limited partners; participating in active management forfeits limited partner protection, and passive LPs do not incur unlimited liability.",
    "In a limited partnership (LP), at least one general partner (GP) manages the enterprise and assumes unlimited personal liability for partnership debts. Limited partners (LPs) act as passive investors whose liability is capped at their committed capital. For tax purposes, LPs are pass-through entities where profits and losses flow directly to partners' personal tax returns rather than being taxed at the entity level.",
    False,
)

# L1-CRP-002 (Calc): Double taxation effective tax rate
tc_02, td_02, inc_02 = 0.24, 0.20, 500_000.0
net_02 = inc_02 * (1.0 - tc_02) * (1.0 - td_02)
teff_02 = 1.0 - (1.0 - tc_02) * (1.0 - td_02)
naive_sum_02 = tc_02 + td_02
wrong_mult_02 = tc_02 * td_02
add_q1(
    "L1-CRP-002", M1, T1, "Corporate Double Taxation",
    "Compare the tax treatment of corporate profits versus pass-through business structures.",
    f"A C-corporation generates USD {inc_02:,.0f} in pre-tax income and distributes 100% of its after-tax earnings as cash dividends to its sole individual shareholder. If the corporate tax rate is {tc_02*100:.0f}% and the shareholder's dividend tax rate is {td_02*100:.0f}%, the effective combined tax rate on the pre-tax corporate income is closest to:",
    f"{teff_02*100:.2f}%",
    f"{naive_sum_02*100:.2f}%",
    f"Adds the corporate and dividend tax rates directly ($24\\% + 20\\% = {naive_sum_02*100:.2f}\\%$) instead of applying the dividend tax only to post-corporate-tax income.",
    f"{tc_02*100:.2f}%",
    "Considers only the entity-level corporate tax rate and ignores the second layer of taxation levied on the shareholder's dividend distribution.",
    rf"Under a classical double-taxation system, corporate income is taxed first at the corporate level and remaining after-tax profits are taxed again when distributed as dividends: "
    rf"$$t_{{\text{{eff}}}} = t_c + (1 - t_c)t_d = 1 - (1 - {tc_02:.2f})(1 - {td_02:.2f}) = 1 - ({1-tc_02:.2f})({1-td_02:.2f}) = {teff_02*100:.2f}\%$$ "
    rf"Equivalently, USD {inc_02*(1-tc_02):,.0f} remains after corporate tax, and USD {net_02:,.0f} remains after dividend tax, representing total taxes of USD {inc_02 - net_02:,.0f} ({teff_02*100:.2f}%).",
    True,
)

# L1-CRP-003 (Calc): Dual-class voting shares
sh_b_03, vote_b_03 = 3_000_000, 10
sh_a_03, vote_a_03 = 17_000_000, 1
tot_sh_03 = sh_b_03 + sh_a_03
tot_votes_03 = sh_b_03 * vote_b_03 + sh_a_03 * vote_a_03
econ_pct_03 = sh_b_03 / tot_sh_03 * 100.0
vote_pct_03 = (sh_b_03 * vote_b_03) / tot_votes_03 * 100.0
wrong_ratio_03 = (sh_b_03 * vote_b_03) / (sh_b_03 * vote_b_03 + tot_sh_03 * vote_a_03) * 100.0
add_q1(
    "L1-CRP-003", M1, T1, "Dual-Class Voting Structures",
    "Analyze how dual-class share structures separate voting control from economic ownership.",
    f"Founders of Northstar Tech hold all {sh_b_03:,} Class B shares carrying {vote_b_03} votes per share, while public investors hold {sh_a_03:,} Class A shares carrying {vote_a_03} vote per share. Both classes have identical dividend and liquidation rights. What percentage of total voting power do the founders control?",
    f"{vote_pct_03:.2f}%",
    f"{econ_pct_03:.2f}%",
    f"Computes the founders' economic (cash flow) ownership ($3\\text{{M}} / 20\\text{{M}} = {econ_pct_03:.2f}\\%$) rather than their weighted voting power.",
    f"{wrong_ratio_03:.2f}%",
    "Includes the founders' 3 million shares in the public Class A share count when computing the denominator of total votes ($30\\text{M} / 50\\text{M}$).",
    rf"Total votes equal Class B votes plus Class A votes: "
    rf"$$\text{{Total Votes}} = ({sh_b_03:,} \times {vote_b_03}) + ({sh_a_03:,} \times {vote_a_03}) = {tot_votes_03:,}$$ "
    rf"Founders' voting power is: "
    rf"$$\text{{Voting Share}} = \frac{{{sh_b_03 * vote_b_03:,}}}{{{tot_votes_03:,}}} = {vote_pct_03:.2f}\%$$ "
    rf"Despite holding only {econ_pct_03:.2f}% of economic cash flow rights, dual-class shares grant the founders majority voting control.",
    True,
)

# L1-CRP-004 (Calc): Cumulative voting
N_04, D_04, d_04 = 2_400_000, 7, 2
min_sh_04 = (d_04 * N_04) // (D_04 + 1) + 1
wrong_div_D_04 = (d_04 * N_04) // D_04 + 1
wrong_one_seat_04 = N_04 // (D_04 + 1) + 1
add_q1(
    "L1-CRP-004", M1, T1, "Board Voting Mechanisms",
    "Calculate voting thresholds under statutory versus cumulative voting.",
    f"A corporation with {N_04:,} voting shares outstanding uses cumulative voting to elect {D_04} board directors at its annual meeting. What is the minimum number of shares an activist investor must control to guarantee the election of {d_04} directors?",
    f"{min_sh_04:,} shares",
    f"{wrong_div_D_04:,} shares",
    f"Divides by $D = {D_04}$ seats instead of $D + 1 = {D_04 + 1}$ in the cumulative voting threshold formula.",
    f"{wrong_one_seat_04:,} shares",
    "Calculates the minimum shares needed to elect only 1 director rather than 2 directors.",
    rf"Under cumulative voting, each share carries $D$ votes that can be concentrated on fewer candidates. The minimum shares required to guarantee electing $d$ out of $D$ open seats with $N$ total shares is: "
    rf"$$S_{{\min}} = \left\lfloor \frac{{d \cdot N}}{{D + 1}} \right\rfloor + 1 = \left\lfloor \frac{{{d_04} \times {N_04:,}}}{{{D_04} + 1}} \right\rfloor + 1 = {min_sh_04:,}\text{{ shares}}$$",
    True,
)

add_q1(
    "L1-CRP-005", M1, T1, "Public Listing Mechanisms",
    "Compare traditional IPOs, direct listings, and special purpose acquisition companies (SPACs).",
    "Which feature most clearly distinguishes a direct listing from a traditional underwritten initial public offering (IPO)?",
    "A direct listing avoids primary share issuance and investment bank underwriting syndicates, relying on existing shareholders to sell shares directly onto the exchange.",
    "A direct listing provides a guaranteed minimum offering price set by bookbuilding underwriters prior to market open.",
    "Describes a firm-commitment underwritten IPO, whereas direct listings employ a reference price without firm-commitment underwriter price stabilization or bookbuilding.",
    "A direct listing places cash proceeds into an interest-bearing trust account for up to 24 months while management searches for a private operating target.",
    "Describes a Special Purpose Acquisition Company (SPAC), not a direct listing of an operating company.",
    "In a direct listing, a private company lists existing shares directly on a public exchange without hiring an underwriting syndicate to sell new primary shares or guarantee pricing. This eliminates underwriting fees and lock-up restrictions, though it does not raise new primary capital for the issuer.",
    False,
)

# L1-CRP-006 (Calc): SPAC founder promote dilution
pub_cash_06, pub_sh_06, fees_06, promo_sh_06, promo_cash_06 = 250_000_000.0, 25_000_000, 12_500_000.0, 6_250_000, 25_000.0
tot_sh_06 = pub_sh_06 + promo_sh_06
net_cash_06 = pub_cash_06 + promo_cash_06 - fees_06
cash_per_sh_06 = net_cash_06 / tot_sh_06
no_promo_06 = (pub_cash_06 - fees_06) / pub_sh_06
no_fees_06 = (pub_cash_06 + promo_cash_06) / tot_sh_06
add_q1(
    "L1-CRP-006", M1, T1, "SPAC Dilution Economics",
    "Evaluate dilution effects in Special Purpose Acquisition Company (SPAC) structures.",
    f"A SPAC raises USD {pub_cash_06/1e6:.0f} million in its IPO by issuing {pub_sh_06:,} public shares at USD 10.00 each. The SPAC sponsor receives {promo_sh_06:,} founder promote shares for USD {promo_cash_06:,.0f} (20% of post-IPO shares). Assuming no redemptions and USD {fees_06/1e6:.1f} million in underwriting and transaction fees paid from the trust, net cash per post-IPO share is closest to:",
    f"USD {cash_per_sh_06:.2f}",
    f"USD {no_promo_06:.2f}",
    "Excludes the 6,250,000 sponsor promote shares from the post-IPO share count denominator.",
    f"USD {no_fees_06:.2f}",
    "Accounts for the sponsor promote shares but omits the USD 12.5 million underwriting and transaction fee deduction.",
    rf"Total net cash available after underwriting and deal fees is: "
    rf"$$\text{{Net Cash}} = {pub_cash_06/1e6:.0f}\text{{M}} + {promo_cash_06/1e6:.3f}\text{{M}} - {fees_06/1e6:.1f}\text{{M}} = \text{{USD }}{net_cash_06/1e6:.3f}\text{{ million}}$$ "
    rf"Dividing across all {tot_sh_06:,} combined public and founder promote shares gives: "
    rf"$$\text{{Net Cash per Share}} = \frac{{\text{{USD }}{net_cash_06:,.0f}}}{{{tot_sh_06:,}}} = \text{{USD }}{cash_per_sh_06:.2f}$$",
    True,
)

# L1-CRP-007 (Calc): LP/GP waterfall
lp_cap_07, ret_07, hurdle_07, carry_07 = 120_000_000.0, 165_000_000.0, 0.08, 0.20
profit_07 = ret_07 - lp_cap_07
pref_07 = lp_cap_07 * hurdle_07
excess_07 = profit_07 - pref_07
gp_carry_07 = excess_07 * carry_07
wrong_no_hurdle_07 = profit_07 * carry_07
wrong_hurdle_only_07 = pref_07 * carry_07
add_q1(
    "L1-CRP-007", M1, T1, "Private Investment Partnership Waterfalls",
    "Calculate partner distributions in limited partnership investment vehicles.",
    f"Limited partners contribute USD {lp_cap_07/1e6:.0f} million (and the general partner contributes USD 0) to a one-year private fund. The partnership agreement grants LPs an {hurdle_07*100:.0f}% preferred return on contributed capital, after which remaining profits are split {100-carry_07*100:.0f}% to LPs and {carry_07*100:.0f}% carried interest to the GP with no catch-up provision. If the fund liquidates at year-end for USD {ret_07/1e6:.0f} million, the GP's carried interest payout is closest to:",
    f"USD {gp_carry_07/1e6:.2f} million",
    f"USD {wrong_no_hurdle_07/1e6:.2f} million",
    f"Applies the 20% carried interest rate to total gross profit (USD {profit_07/1e6:.0f} million) without first deducting the 8% LP preferred return.",
    f"USD {wrong_hurdle_only_07/1e6:.2f} million",
    f"Applies the 20% carry percentage to the USD {pref_07/1e6:.2f} million preferred return hurdle instead of the excess profit above the hurdle.",
    rf"Total fund profit equals $\text{{USD }}{ret_07/1e6:.0f}\text{{M}} - \text{{USD }}{lp_cap_07/1e6:.0f}\text{{M}} = \text{{USD }}{profit_07/1e6:.0f}\text{{M}}$. "
    rf"After returning USD {lp_cap_07/1e6:.0f}M principal and paying the 8% LP hurdle of $\text{{USD }}{lp_cap_07/1e6:.0f}\text{{M}} \times 8\% = \text{{USD }}{pref_07/1e6:.2f}\text{{M}}$, excess profit is: "
    rf"$$\text{{Excess Profit}} = {profit_07/1e6:.0f} - {pref_07/1e6:.2f} = \text{{USD }}{excess_07/1e6:.2f}\text{{ million}}$$ "
    rf"With no catch-up, GP carried interest is $20\% \times \text{{USD }}{excess_07/1e6:.2f}\text{{M}} = \text{{USD }}{gp_carry_07/1e6:.2f}\text{{ million}}$.",
    True,
)

add_q1(
    "L1-CRP-008", M1, T1, "Organizational Mandates",
    "Contrast for-profit corporations, state-owned enterprises, and non-profit entities.",
    "Which statement accurately describes a primary governance difference between a publicly listed for-profit corporation and a state-owned enterprise (SOE)?",
    "An SOE often pursues dual public policy and social objectives alongside commercial goals, whereas a listed for-profit corporation focuses primarily on maximizing shareholder value.",
    "An SOE issues voting common stock exclusively to private institutional investors and cannot borrow in public bond markets.",
    "Incorrectly characterizes SOE financing; SOEs are wholly or majority government-owned and frequently issue debt in domestic or international bond markets.",
    "A listed for-profit corporation faces no fiduciary obligation to shareholders once debt covenants are satisfied.",
    "Directors of a listed for-profit corporation retain ongoing fiduciary duties to shareholders regardless of debt covenant compliance.",
    "While publicly traded corporations prioritize long-term shareholder value creation, state-owned enterprises (SOEs) are government-controlled entities established to fulfill public policy mandates (such as utility access, employment, or strategic infrastructure) alongside or ahead of profit maximization.",
    False,
)

# L1-CRP-009 (Calc): Pyramidal ownership cash flow rights
p1_09, p2_09 = 0.58, 0.55
cf_rights_09 = p1_09 * p2_09 * 100.0
avg_09 = 0.5 * (p1_09 + p2_09) * 100.0
add_q1(
    "L1-CRP-009", M1, T1, "Pyramidal Ownership & Control Wedges",
    "Determine indirect cash flow rights versus voting control in pyramidal ownership structures.",
    f"Apex Family Holding owns {p1_09*100:.0f}% of the single-class voting shares of MidTier Corp, and MidTier Corp owns {p2_09*100:.0f}% of the single-class voting shares of Operating Sub. What is Apex Family Holding's indirect economic (cash flow) claim on Operating Sub's dividends?",
    f"{cf_rights_09:.1f}%",
    f"{p2_09*100:.1f}%",
    "Reports MidTier Corp's direct ownership stake in Operating Sub without multiplying through Apex Family Holding's stake in MidTier Corp.",
    f"{avg_09:.1f}%",
    "Takes the arithmetic mean of the two ownership tiers instead of multiplying the sequential equity claims.",
    rf"Through a two-tier pyramid, voting control is maintained at every majority-owned link (58% then 55%), but indirect economic cash flow rights multiply across tiers: "
    rf"$$\text{{Cash Flow Rights}} = {p1_09:.2f} \times {p2_09:.2f} = {cf_rights_09:.1f}\%$$",
    True,
)

add_q1(
    "L1-CRP-010", M1, T1, "Private vs Public Corporations",
    "Distinguish private corporations from publicly listed corporations in capital access and governance.",
    "Compared with a publicly traded corporation, a private corporation typically exhibits:",
    "Greater long-term strategic flexibility and lower regulatory compliance costs, balanced against less liquid equity and higher costs of raising external capital.",
    "Mandatory quarterly SEC-style financial filings and lower share-price volatility due to continuous exchange trading.",
    "Private firms generally avoid public exchange listing requirements and quarterly public reporting, and their shares lack continuous market liquidity.",
    "Greater separation between ownership and daily management, creating more severe dispersed-shareholder monitoring problems.",
    "Public firms with dispersed retail/institutional ownership exhibit wider separation of ownership and control than private firms with concentrated founders/PE owners.",
    "Private corporations operate with concentrated ownership, avoiding costly public disclosure mandates and short-term quarterly earnings pressure, while sacrificing public equity liquidity and broad capital market access.",
    False,
)

# =============================================================================
# LEVEL 1: MODULE 2 — GOVERNANCE & ESG RISK FACTORS (L1-CRP-011 .. 022)
# =============================================================================
M2 = "CI-L1-M2"
T2 = "Corporate Governance & ESG"

add_q1(
    "L1-CRP-011", M2, T2, "Stakeholder vs Shareholder Theory",
    "Contrast shareholder theory and stakeholder theory in corporate governance.",
    "Under stakeholder theory of corporate governance, the board of directors is primarily expected to:",
    "Balance the competing interests of shareholders, employees, customers, suppliers, creditors, and communities to sustain long-term enterprise value.",
    "Maximize short-term quarterly earnings per share regardless of supplier, environmental, or workforce externalities.",
    "Describes an extreme short-termism distortion rather than stakeholder theory (or even long-term shareholder theory).",
    "Grant employees and creditors equal board voting rights with common shareholders in all jurisdictions.",
    "While some two-tier systems (e.g., Germany's co-determination) reserve supervisory seats for labor, stakeholder theory as a governance principle does not require equal statutory voting rights for all groups.",
    "Stakeholder theory recognizes that long-term corporate sustainability depends on managing material relationships across all stakeholders—including customers, employees, suppliers, debtholders, regulators, and communities—rather than focusing solely on equity holders.",
    False,
)

add_q1(
    "L1-CRP-012", M2, T2, "Principal-Agent Conflicts",
    "Identify principal-agent conflicts among shareholders, managers, controlling owners, and creditors.",
    "When a distressed corporation near bankruptcy uses its remaining cash to fund a highly speculative project with negative expected NPV but huge upside variance, which agency conflict is occurring?",
    "Shareholder-debtholder conflict (asset substitution / risk shifting), where equity holders capture upside gains while creditors bear downside losses.",
    "Manager-shareholder conflict (empire building), where management seeks to grow revenues regardless of profitability.",
    "Empire building involves growing firm scale or perks at shareholder expense; shifting into high-variance negative-NPV bets near insolvency benefits equity holders at creditors' expense.",
    "Controlling-minority shareholder conflict (tunneling), where insiders transfer firm assets to a private affiliate.",
    "Tunneling transfers value from minority shareholders to a controlling blockholder, rather than transferring risk from equity to creditors.",
    "Because common equity resembles a call option on firm assets, shareholders of a levered firm near distress capture unlimited upside if a risky gamble succeeds while limited liability caps their downside, shifting losses onto bondholders (asset substitution).",
    False,
)

add_q1(
    "L1-CRP-013", M2, T2, "Board Structure & Independence",
    "Compare one-tier and two-tier board structures and evaluate board independence.",
    "Which structural feature is characteristic of a two-tier corporate board system?",
    "A formal separation between an executive management board running daily operations and an independent supervisory board overseeing strategy and appointing managers.",
    "Combining the roles of Chief Executive Officer and Board Chair into a single executive position.",
    "CEO duality occurs in one-tier boards; two-tier systems strictly prohibit management board members from serving simultaneously on the supervisory board.",
    "Holding all board elections simultaneously every year via cumulative voting.",
    "Describes annual voting mechanics rather than the structural division between management and supervisory boards.",
    "Two-tier boards (common in Germany and the Netherlands) separate daily operations (Management Board) from oversight and executive appointment/compensation (Supervisory Board), preventing insider dominance of oversight.",
    False,
)

add_q1(
    "L1-CRP-014", M2, T2, "Board Elections & Committees",
    "Evaluate staggered boards, CEO duality, and key board committee independence.",
    "Why do institutional investors generally view a staggered (classified) board structure as a governance risk factor?",
    "It forces an activist or acquirer to win multiple consecutive annual proxy contests to gain a board majority, entrenching underperforming directors.",
    "It requires every director to stand for re-election annually, creating excessive board turnover and short-termism.",
    "Describes an annually elected (declassified) board rather than a staggered board.",
    "It automatically eliminates the independence of the audit and remuneration committees.",
    "Staggered terms do not legally preclude committee independence, though they reduce overall board accountability to shareholders.",
    "In a staggered board (typically divided into three classes serving three-year terms), only one-third of seats stand for election each year, delaying proxy replacement and acting as a potent anti-takeover defense.",
    False,
)

# L1-CRP-015 (Calc): Carbon pricing impact on project NPV
rev_15, opex_15, depr_15, tax_15, tons_15, price_ton_15, capex_15, wacc_15, n_15 = (
    80.0, 48.0, 10.0, 0.25, 150_000.0, 40.0, 65.0, 0.10, 4
)
carbon_cost_m_15 = (tons_15 * price_ton_15) / 1e6  # 6.0M/yr
ebit_base_15 = rev_15 - opex_15 - depr_15  # 22.0M
ocf_base_15 = ebit_base_15 * (1.0 - tax_15) + depr_15  # 26.5M
ebit_carb_15 = ebit_base_15 - carbon_cost_m_15  # 16.0M
ocf_carb_15 = ebit_carb_15 * (1.0 - tax_15) + depr_15  # 22.0M
pv_factor_15 = sum(1.0 / ((1.0 + wacc_15) ** t) for t in range(1, n_15 + 1))
npv_carb_15 = -capex_15 + ocf_carb_15 * pv_factor_15
npv_no_tax_shield_15 = -capex_15 + (ocf_base_15 - carbon_cost_m_15) * pv_factor_15
npv_base_15 = -capex_15 + ocf_base_15 * pv_factor_15
add_q1(
    "L1-CRP-015", M2, T2, "ESG Transition Risk Valuation",
    "Integrate environmental transition risks such as carbon pricing into corporate cash flow and valuation analysis.",
    f"An industrial plant requires an upfront outlay of USD {capex_15:.0f} million and generates annual revenues of USD {rev_15:.0f} million, cash operating expenses of USD {opex_15:.0f} million, and straight-line depreciation of USD {depr_15:.0f} million over {n_15} years (zero salvage). Regulators introduce a carbon tax of USD {price_ton_15:.0f} per metric ton on the plant's {tons_15:,.0f} metric tons of annual Scope 1 emissions. With a {tax_15*100:.0f}% corporate tax rate and {wacc_15*100:.0f}% WACC, the plant's carbon-adjusted NPV is closest to:",
    f"USD {npv_carb_15:.2f} million",
    f"USD {npv_no_tax_shield_15:.2f} million",
    "Subtracts the USD 6.0 million pre-tax carbon cost directly from after-tax operating cash flow instead of recognizing its tax deductibility.",
    f"USD {npv_base_15:.2f} million",
    "Computes baseline NPV while omitting the carbon tax expense completely.",
    rf"Annual carbon tax expense is $150,000 \times \text{{USD }}40 = \text{{USD }}{carbon_cost_m_15:.1f}\text{{ million}}$. "
    rf"Adjusted annual EBIT is ${rev_15:.0f} - {opex_15:.0f} - {depr_15:.0f} - {carbon_cost_m_15:.1f} = \text{{USD }}{ebit_carb_15:.1f}\text{{ million}}$, yielding annual after-tax OCF: "
    rf"$$\text{{OCF}} = {ebit_carb_15:.1f}(1 - {tax_15:.2f}) + {depr_15:.0f} = \text{{USD }}{ocf_carb_15:.2f}\text{{ million}}$$ "
    rf"Discounting this 4-year annuity at {wacc_15*100:.0f}% ($\text{{PVIFA}}_{{10\%,4}} = {pv_factor_15:.4f}$): "
    rf"$$\text{{NPV}} = -{capex_15:.0f} + {ocf_carb_15:.2f}({pv_factor_15:.4f}) = \text{{USD }}{npv_carb_15:.2f}\text{{ million}}$$",
    True,
)

# L1-CRP-016 (Calc): Stranded asset useful life truncation
ocf_16, r_16, n_old_16, n_new_16 = 18.0, 0.08, 10, 4
pv_old_16 = ocf_16 * sum(1.0 / ((1.0 + r_16) ** t) for t in range(1, n_old_16 + 1))
pv_new_16 = ocf_16 * sum(1.0 / ((1.0 + r_16) ** t) for t in range(1, n_new_16 + 1))
loss_pv_16 = pv_old_16 - pv_new_16
undisc_loss_16 = ocf_16 * (n_old_16 - n_new_16)
add_q1(
    "L1-CRP-016", M2, T2, "Stranded Asset Financial Impact",
    "Quantify the valuation impact of stranded assets caused by environmental regulation.",
    f"A thermal power facility was originally modeled to generate constant after-tax operating cash flows of USD {ocf_16:.0f} million annually for {n_old_16} years at an {r_16*100:.0f}% discount rate. New decarbonization mandates force early retirement after Year {n_new_16} with zero salvage value. The reduction in the facility's present value due to stranded-asset truncation is closest to:",
    f"USD {loss_pv_16:.2f} million",
    f"USD {undisc_loss_16:.2f} million",
    "Sums the 6 lost years of cash flows without discounting them back to Year 0.",
    f"USD {pv_new_16:.2f} million",
    "Reports the remaining 4-year present value rather than the present value lost from Years 5 to 10.",
    rf"Original 10-year PV is $\text{{USD }}{ocf_16:.0f}\text{{M}} \times \text{{PVIFA}}_{{8\%,10}} = \text{{USD }}{pv_old_16:.2f}\text{{M}}$. "
    rf"Truncated 4-year PV is $\text{{USD }}{ocf_16:.0f}\text{{M}} \times \text{{PVIFA}}_{{8\%,4}} = \text{{USD }}{pv_new_16:.2f}\text{{M}}$. "
    rf"The stranded-asset value loss equals the PV of Years 5 through 10: "
    rf"$$\Delta \text{{PV}} = {pv_old_16:.2f} - {pv_new_16:.2f} = \text{{USD }}{loss_pv_16:.2f}\text{{ million}}$$",
    True,
)

# L1-CRP-017 (Calc): ESG governance risk premium impact on WACC
wd_17, we_17, t_17, d_kd_17, d_ke_17 = 0.40, 0.60, 0.25, 0.0080, 0.0120  # 80 bps debt, 120 bps equity
dwacc_17 = (wd_17 * d_kd_17 * (1.0 - t_17) + we_17 * d_ke_17) * 10_000  # bps
wrong_no_tax_17 = (wd_17 * d_kd_17 + we_17 * d_ke_17) * 10_000
wrong_avg_17 = 0.5 * (d_kd_17 + d_ke_17) * 10_000
add_q1(
    "L1-CRP-017", M2, T2, "ESG Adjustments to Cost of Capital",
    "Incorporate governance and environmental risk adjustments into cost of debt, cost of equity, and WACC.",
    f"Due to material governance deficiencies, credit and equity analysts apply an ESG risk premium of {d_kd_17*10000:.0f} bps to a firm's pre-tax cost of debt and {d_ke_17*10000:.0f} bps to its cost of equity. The firm maintains a target capital structure of {wd_17*100:.0f}% debt and {we_17*100:.0f}% equity and faces a {tax_15*100:.0f}% tax rate. The resulting increase in the firm's WACC is closest to:",
    f"{dwacc_17:.0f} bps",
    f"{wrong_no_tax_17:.0f} bps",
    "Fails to multiply the debt spread increase by $(1 - t)$ to reflect the corporate tax shield.",
    f"{wrong_avg_17:.0f} bps",
    "Takes an unweighted simple average of the debt and equity risk premia.",
    rf"Weighting the after-tax debt spread increase and equity risk premium increase by target capital weights: "
    rf"$$\Delta \text{{WACC}} = w_d (\Delta k_d)(1 - t) + w_e (\Delta k_e) = 0.40(80)(1 - 0.25) + 0.60(120) = 24 + 72 = {dwacc_17:.0f}\text{{ bps}}$$",
    True,
)

# L1-CRP-018 (Calc): Green bond greenium annual after-tax savings
face_18, greenium_18, tax_18 = 500_000_000.0, 0.0025, 0.25
gross_sav_18 = face_18 * greenium_18
after_tax_sav_18 = gross_sav_18 * (1.0 - tax_18)
wrong_18 = face_18 * greenium_18 * tax_18
add_q1(
    "L1-CRP-018", M2, T2, "Sustainable Debt & Green Bonds",
    "Evaluate sustainable finance instruments such as green bonds and sustainability-linked loans.",
    f"An issuer prices a USD {face_18/1e6:.0f} million 5-year fixed-rate green bond at a {greenium_18*10000:.0f} bps lower annual coupon yield ('greenium') than an otherwise identical conventional bond. At a {tax_18*100:.0f}% marginal corporate tax rate, the issuer's annual after-tax interest savings equals:",
    f"USD {after_tax_sav_18/1e3:,.1f} thousand",
    f"USD {gross_sav_18/1e3:,.1f} thousand",
    "Reports pre-tax coupon savings without adjusting for the smaller interest tax deduction.",
    f"USD {wrong_18/1e3:,.1f} thousand",
    "Multiplies the pre-tax savings by the tax rate $t$ rather than $(1 - t)$.",
    rf"Annual pre-tax coupon savings equal $\text{{USD }}{face_18/1e6:.0f}\text{{M}} \times 0.25\% = \text{{USD }}{gross_sav_18/1e3:,.1f}\text{{ thousand}}$. "
    rf"Because interest is tax-deductible, the net after-tax annual cash flow benefit is: "
    rf"$$\text{{After-Tax Savings}} = \text{{USD }}{gross_sav_18/1e3:,.1f}\text{{k}} \times (1 - {tax_18:.2f}) = \text{{USD }}{after_tax_sav_18/1e3:,.1f}\text{{ thousand}}$$",
    True,
)

add_q1(
    "L1-CRP-019", M2, T2, "ESG Materiality & Risk Categories",
    "Classify environmental, social, and governance risk factors across industries.",
    "Which ESG risk factor is classified as a physical climate risk rather than a transition climate risk?",
    "Coastal warehouse flooding and supply-chain disruptions caused by intensifying severe weather events.",
    "Mandatory carbon border adjustment taxes imposed on steel imports into the European Union.",
    "Carbon pricing and border adjustment tariffs are policy-driven transition risks, not physical risks.",
    "Consumer preference shifts away from internal-combustion vehicles toward battery-electric alternatives.",
    "Market and technological shifts toward low-carbon substitutes are transition risks.",
    "Climate risks divide into physical risks (acute extreme weather events and chronic sea-level or temperature shifts damaging physical assets) and transition risks (policy, legal, technology, and market changes associated with decarbonization).",
    False,
)

# L1-CRP-020 (Calc): Executive performance share unit (PSU) compensation payout
base_psu_20, target_tsr_20, act_tsr_20, mult_per_pct_20, price_20 = 50_000, 10.0, 14.0, 0.05, 80.0
# Base 100% at 10% TSR, +5% shares per +1% excess TSR (capped at 200%)
mult_20 = 1.0 + (act_tsr_20 - target_tsr_20) * mult_per_pct_20  # 1.20x
vested_sh_20 = int(base_psu_20 * mult_20)
payout_20 = vested_sh_20 * price_20
wrong_base_20 = base_psu_20 * price_20
wrong_linear_20 = int(base_psu_20 * (act_tsr_20 / target_tsr_20)) * price_20
add_q1(
    "L1-CRP-020", M2, T2, "Executive Compensation Alignment",
    "Analyze executive remuneration structures and performance vesting metrics.",
    f"A CEO receives {base_psu_20:,} target performance share units (PSUs). Vesting equals 100% at a {target_tsr_20:.0f}% annualized total shareholder return (TSR), increasing by {mult_per_pct_20*100:.0f} percentage points for each 1 percentage point that TSR exceeds {target_tsr_20:.0f}%. If actual TSR is {act_tsr_20:.0f}% and the ending share price is USD {price_20:.2f}, the vested PSU value is closest to:",
    f"USD {payout_20/1e6:.2f} million",
    f"USD {wrong_linear_20/1e6:.2f} million",
    "Scales the payout proportionally by the ratio $14\\% / 10\\% = 1.40\\times$ instead of using the contractual 5 percentage point slope per 1% excess TSR.",
    f"USD {wrong_base_20/1e6:.2f} million",
    "Uses the target grant of 50,000 shares without adjusting for outperformance vesting.",
    rf"Excess TSR equals ${act_tsr_20:.0f}\% - {target_tsr_20:.0f}\% = 4$ percentage points. The vesting multiplier is $100\% + 4(5\%) = {mult_20*100:.0f}\%$. "
    rf"Vested shares equal ${base_psu_20:,} \times {mult_20:.2f} = {vested_sh_20:,}$ shares, worth ${vested_sh_20:,} \times \text{{USD }}{price_20:.2f} = \text{{USD }}{payout_20/1e6:.2f}\text{{ million}}$.",
    True,
)

add_q1(
    "L1-CRP-021", M2, T2, "Shareholder Activism & Market Discipline",
    "Explain how external governance mechanisms influence corporate management.",
    "Which mechanism represents an internal corporate governance control rather than an external market discipline mechanism?",
    "An independent audit committee reviewing related-party transactions and internal financial controls.",
    "A hostile tender offer launched by a competing firm at a 30% premium to market price.",
    "The market for corporate control (hostile takeovers) is an external governance mechanism disciplining inefficient managers.",
    "Activist hedge funds accumulating a 6% stake and launching a public proxy campaign.",
    "Outside investor activism and public proxy battles are external shareholder-driven interventions.",
    "Internal governance controls operate from within the corporation's governance architecture (independent boards, audit/compensation committees, internal whistleblowing and bylaws), whereas hostile takeovers, credit rating downgrades, and external activist campaigns represent external disciplines.",
    False,
)

add_q1(
    "L1-CRP-022", M2, T2, "Debt Covenants & Creditor Protection",
    "Describe how affirmative and negative debt covenants mitigate agency costs.",
    "A bond indenture clause prohibiting the borrower from paying cash dividends exceeding 50% of cumulative net income is best categorized as a:",
    "Negative covenant designed to limit cash extraction and protect creditor collateral.",
    "Affirmative covenant requiring management to maintain hazard insurance and timely audited statements.",
    "Affirmative covenants specify actions the borrower must perform; restricting dividends is a prohibitive (negative) restriction.",
    "Cross-default provision triggered solely by a change in corporate board chair.",
    "Cross-default clauses trigger default upon missing payments on other debt obligations, not upon board leadership transitions or dividend caps.",
    "Negative covenants prohibit borrower actions that could impair creditor recovery—such as excessive dividends, issuing senior secured debt (negative pledge), or selling core assets—directly mitigating debtholder-shareholder agency conflicts.",
    False,
)

# =============================================================================
# LEVEL 1: MODULE 3 — BUSINESS MODELS (L1-CRP-023 .. 032)
# =============================================================================
M3 = "CI-L1-M3"
T3 = "Business Models & Unit Economics"

add_q1(
    "L1-CRP-023", M3, T3, "Business Model Archetypes",
    "Describe key business model components including value proposition, channels, and pricing.",
    "A software marketplace charges a percentage transaction fee to connect freelance designers with enterprise buyers without holding inventory or employing the designers. This business model is best characterized as:",
    "A two-sided asset-light platform business model generating revenue via a transaction take rate.",
    "A vertically integrated manufacturer owning upstream supply and downstream retail stores.",
    "Vertically integrated manufacturers own physical production assets and inventories rather than intermediating independent third parties.",
    "A razor-and-blades model subsidizing initial hardware sales with high-margin proprietary consumables.",
    "Razor-and-blades relies on selling complementary physical hardware and proprietary recurring consumables rather than matching buyers and sellers on a digital marketplace.",
    "Two-sided digital marketplaces match supply and demand across independent participants while keeping physical asset intensity near zero, earning a percentage take rate on Gross Merchandise Value (GMV).",
    False,
)

# L1-CRP-024 (Calc): SaaS LTV and LTV/CAC ratio
arpu_24, gm_24, churn_24, cac_24 = 120.0, 0.80, 0.025, 960.0
ltv_24 = (arpu_24 * gm_24) / churn_24
ltv_cac_24 = ltv_24 / cac_24
wrong_no_gm_24 = (arpu_24 / churn_24) / cac_24
wrong_ann_24 = (arpu_24 * gm_24) / (churn_24 * 12) / cac_24
add_q1(
    "L1-CRP-024", M3, T3, "SaaS Customer Lifetime Value",
    "Evaluate subscription business unit economics using LTV and CAC ratios.",
    f"A cloud software vendor reports monthly average revenue per user (ARPU) of USD {arpu_24:.0f}, a gross margin of {gm_24*100:.0f}%, a monthly customer churn rate of {churn_24*100:.1f}%, and a customer acquisition cost (CAC) of USD {cac_24:.0f}. Ignoring discounting, the vendor's LTV-to-CAC ratio is closest to:",
    f"{ltv_cac_24:.1f}x",
    f"{wrong_no_gm_24:.1f}x",
    "Computes LTV using gross ARPU rather than gross profit contribution ($\\text{ARPU} \\times \\text{Gross Margin}$).",
    f"{wrong_ann_24:.2f}x",
    "Multiplies monthly churn by 12 in the denominator without converting monthly ARPU to annual revenue.",
    rf"Monthly gross profit per customer is $\text{{USD }}{arpu_24:.0f} \times {gm_24:.2f} = \text{{USD }}{arpu_24*gm_24:.0f}$. "
    rf"Undiscounted Customer Lifetime Value (LTV) equals: "
    rf"$$\text{{LTV}} = \frac{{\text{{ARPU}} \times \text{{Gross Margin}}}}{{\text{{Monthly Churn}}}} = \frac{{\text{{USD }}{arpu_24*gm_24:.0f}}}{{{churn_24:.3f}}} = \text{{USD }}{ltv_24:,.0f}$$ "
    rf"Thus, $\text{{LTV}} / \text{{CAC}} = \text{{USD }}{ltv_24:,.0f} / \text{{USD }}{cac_24:,.0f} = {ltv_cac_24:.1f}\text{{x}}$.",
    True,
)

# L1-CRP-025 (Calc): CAC Payback Period
arpu_25, gm_25, cac_25 = 85.0, 0.75, 1_147.50
payback_25 = cac_25 / (arpu_25 * gm_25)
wrong_rev_25 = cac_25 / arpu_25
wrong_one_minus_gm_25 = cac_25 / (arpu_25 * (1.0 - gm_25))
add_q1(
    "L1-CRP-025", M3, T3, "CAC Payback Analysis",
    "Compute customer acquisition cost payback periods for recurring revenue models.",
    f"A subscription streaming service spends USD {cac_25:,.2f} in marketing and onboarding costs to acquire a subscriber paying USD {arpu_25:.2f} per month. If the gross margin on subscription revenue is {gm_25*100:.0f}%, the CAC payback period is closest to:",
    f"{payback_25:.1f} months",
    f"{wrong_rev_25:.1f} months",
    "Divides CAC by total monthly ARPU rather than monthly gross profit per subscriber.",
    f"{wrong_one_minus_gm_25:.1f} months",
    "Uses the cost-of-goods ratio $(1 - \\text{Gross Margin})$ instead of the gross margin percentage.",
    rf"Monthly gross profit per subscriber equals $\text{{USD }}{arpu_25:.2f} \times {gm_25:.2f} = \text{{USD }}{arpu_25*gm_25:.3f}$. "
    rf"The CAC payback period is: "
    rf"$$\text{{CAC Payback}} = \frac{{\text{{CAC}}}}{{\text{{ARPU}} \times \text{{GM}}\%}} = \frac{{\text{{USD }}{cac_25:,.2f}}}{{\text{{USD }}{arpu_25*gm_25:.3f}}} = {payback_25:.1f}\text{{ months}}$$",
    True,
)

# L1-CRP-026 (Calc): Razor-and-blades customer NPV
p_hw_26, c_hw_26, p_cart_26, c_cart_26, qty_yr_26, r_26, yrs_26 = 90.0, 140.0, 45.0, 12.0, 3, 0.10, 3
cf0_26 = p_hw_26 - c_hw_26  # -50
cf_yr_26 = (p_cart_26 - c_cart_26) * qty_yr_26  # 99/yr
npv_26 = cf0_26 + cf_yr_26 * sum(1.0 / ((1.0 + r_26) ** t) for t in range(1, yrs_26 + 1))
undisc_26 = cf0_26 + cf_yr_26 * yrs_26
wrong_rev_only_26 = cf0_26 + (p_cart_26 * qty_yr_26) * sum(1.0 / ((1.0 + r_26) ** t) for t in range(1, yrs_26 + 1))
add_q1(
    "L1-CRP-026", M3, T3, "Razor-and-Blades Pricing Economics",
    "Analyze customer-level profitability under bundled or razor-and-blades pricing models.",
    f"An electronics firm sells a smart coffee brewer at Year 0 for USD {p_hw_26:.0f} (unit manufacturing cost USD {c_hw_26:.0f}) and expects each buyer to purchase {qty_yr_26} proprietary pod packs at the end of Years 1, 2, and 3 priced at USD {p_cart_26:.0f} per pack (unit cost USD {c_cart_26:.0f}). At a {r_26*100:.0f}% discount rate, the net present value per acquired customer is closest to:",
    f"USD {npv_26:.2f}",
    f"USD {undisc_26:.2f}",
    "Sums the three years of cartridge gross profit without discounting at 10%.",
    f"USD {wrong_rev_only_26:.2f}",
    "Uses gross pod revenue (USD 135/yr) instead of pod gross margin (USD 99/yr).",
    rf"At Year 0, the brewer generates a net subsidy of $\text{{USD }}{p_hw_26:.0f} - \text{{USD }}{c_hw_26:.0f} = -\text{{USD }}{abs(cf0_26):.0f}$. "
    rf"Each year for 3 years, pod gross profit equals $3 \times (\text{{USD }}{p_cart_26:.0f} - \text{{USD }}{c_cart_26:.0f}) = \text{{USD }}{cf_yr_26:.0f}$. "
    rf"Discounting at 10% ($\text{{PVIFA}}_{{10\%,3}} = {sum(1/(1+r_26)**t for t in range(1,4)):.4f}$): "
    rf"$$\text{{NPV}} = {cf0_26:.0f} + \frac{{{cf_yr_26:.0f}}}{{1.10}} + \frac{{{cf_yr_26:.0f}}}{{1.10^2}} + \frac{{{cf_yr_26:.0f}}}{{1.10^3}} = \text{{USD }}{npv_26:.2f}$$",
    True,
)

# L1-CRP-027 (Calc): Sales-mix multi-product break-even
p1_27, v1_27, w1_27 = 100.0, 60.0, 0.60
p2_27, v2_27, w2_27 = 200.0, 110.0, 0.40
fixed_27 = 1_200_000.0
cm1_27, cm2_27 = p1_27 - v1_27, p2_27 - v2_27
wacm_27 = w1_27 * cm1_27 + w2_27 * cm2_27  # 24 + 36 = 60
be_units_27 = fixed_27 / wacm_27  # 20,000
wrong_simple_avg_27 = fixed_27 / (0.5 * (cm1_27 + cm2_27))
wrong_rev_27 = fixed_27 / (w1_27 * p1_27 + w2_27 * p2_27)
add_q1(
    "L1-CRP-027", M3, T3, "Sales-Mix Break-Even Analysis",
    "Calculate multi-product unit break-even volumes given unit economics and sales mix.",
    f"A hardware business sells Standard units (price USD {p1_27:.0f}, variable cost USD {v1_27:.0f}) and Pro units (price USD {p2_27:.0f}, variable cost USD {v2_27:.0f}) in a constant unit mix of {w1_27*100:.0f}% Standard and {w2_27*100:.0f}% Pro. Annual fixed costs total USD {fixed_27/1e6:.1f} million. Total combined units needed to break even annually equals:",
    f"{be_units_27:,.0f} units",
    f"{wrong_simple_avg_27:,.0f} units",
    "Uses a simple unweighted average contribution margin (USD 65/unit) instead of weighting by the 60%/40% unit sales mix.",
    f"{wrong_rev_27:,.0f} units",
    "Divides fixed costs by weighted-average selling price rather than weighted-average contribution margin.",
    rf"Unit contribution margins are $\text{{CM}}_{{\text{{Std}}}} = 100 - 60 = \text{{USD }}40$ and $\text{{CM}}_{{\text{{Pro}}}} = 200 - 110 = \text{{USD }}90$. "
    rf"Weighted-average contribution margin is $0.60(40) + 0.40(90) = \text{{USD }}{wacm_27:.0f}$ per blended unit. "
    rf"Total break-even volume equals: "
    rf"$$Q_{{\text{{BE}}}} = \frac{{\text{{USD }}{fixed_27:,.0f}}}{{\text{{USD }}{wacm_27:.0f}}} = {be_units_27:,.0f}\text{{ units}}$$",
    True,
)

# L1-CRP-028 (Calc): Operating cost structure comparison
rev_28, drop_28 = 100.0, 0.15
vc_a_28, fc_a_28 = 0.25, 55.0  # capital intensive: EBIT = 75 - 55 = 20 -> drop rev 15 -> CM=63.75 -> EBIT=8.75 (-56.25%)
vc_b_28, fc_b_28 = 0.65, 15.0  # asset light: EBIT = 35 - 15 = 20 -> drop rev 15 -> CM=29.75 -> EBIT=14.75 (-26.25%)
ebit_a0_28 = rev_28 * (1 - vc_a_28) - fc_a_28
ebit_a1_28 = rev_28 * (1 - drop_28) * (1 - vc_a_28) - fc_a_28
pct_a_28 = (ebit_a1_28 - ebit_a0_28) / ebit_a0_28 * 100.0
ebit_b0_28 = rev_28 * (1 - vc_b_28) - fc_b_28
ebit_b1_28 = rev_28 * (1 - drop_28) * (1 - vc_b_28) - fc_b_28
pct_b_28 = (ebit_b1_28 - ebit_b0_28) / ebit_b0_28 * 100.0
diff_28 = abs(pct_a_28) - abs(pct_b_28)
add_q1(
    "L1-CRP-028", M3, T3, "Asset-Light vs Capital-Intensive Economics",
    "Compare earnings sensitivity between fixed-cost and variable-cost business models.",
    f"Both Firm A (capital-intensive) and Firm B (asset-light) generate USD {rev_28:.0f} million in revenue and USD {ebit_a0_28:.0f} million in EBIT. Firm A has variable costs equal to {vc_a_28*100:.0f}% of revenue and USD {fc_a_28:.0f} million in fixed costs, whereas Firm B has variable costs equal to {vc_b_28*100:.0f}% of revenue and USD {fc_b_28:.0f} million in fixed costs. If revenue falls by {drop_28*100:.0f}% at both firms, Firm A's EBIT declines by:",
    f"{abs(pct_a_28):.2f}%, compared with {abs(pct_b_28):.2f}% for Firm B",
    f"{abs(pct_b_28):.2f}%, compared with {abs(pct_a_28):.2f}% for Firm B",
    "Reverses the sensitivity of the two models, attributing higher operating leverage to the variable-cost asset-light firm.",
    f"{drop_28*100:.2f}%, compared with {drop_28*100:.2f}% for Firm B",
    "Assumes EBIT declines strictly proportionally with the 15% revenue drop, ignoring fixed operating cost leverage.",
    rf"When revenue drops 15% to USD {rev_28*(1-drop_28):.0f}M, contribution margin drops 15% while fixed costs stay constant: "
    rf"Firm A: $\text{{EBIT}}_1 = 85(0.75) - 55 = \text{{USD }}{ebit_a1_28:.2f}\text{{M}}$, a ${pct_a_28:.2f}\%$ change ($\text{{DOL}}_A = 75/20 = 3.75$). "
    rf"Firm B: $\text{{EBIT}}_1 = 85(0.35) - 15 = \text{{USD }}{ebit_b1_28:.2f}\text{{M}}$, a ${pct_b_28:.2f}\%$ change ($\text{{DOL}}_B = 35/20 = 1.75$).",
    True,
)

# L1-CRP-029 (Calc): Tiered pricing contribution margin gain
u_flat_29, p_flat_29, vc_29 = 10_000, 50.0, 10.0
u_pro_29, p_pro_29, u_bas_29, p_bas_29 = 6_000, 70.0, 8_000, 35.0
cm_flat_29 = u_flat_29 * (p_flat_29 - vc_29)
cm_tier_29 = u_pro_29 * (p_pro_29 - vc_29) + u_bas_29 * (p_bas_29 - vc_29)
gain_29 = cm_tier_29 - cm_flat_29
rev_gain_29 = (u_pro_29 * p_pro_29 + u_bas_29 * p_bas_29) - (u_flat_29 * p_flat_29)
add_q1(
    "L1-CRP-029", M3, T3, "Pricing Power & Tiered Monetization",
    "Evaluate how tiered pricing strategies affect contribution margin.",
    f"Under flat pricing at USD {p_flat_29:.0f}/user, a software vendor attracts {u_flat_29:,} subscribers, incurring variable support costs of USD {vc_29:.0f}/user. Switching to two tiers attracts {u_pro_29:,} Pro users at USD {p_pro_29:.0f}/user and {u_bas_29:,} Basic users at USD {p_bas_29:.0f}/user (same USD {vc_29:.0f}/user variable cost). The net change in total contribution margin from tiered pricing is:",
    f"+USD {gain_29:,.0f}",
    f"+USD {rev_gain_29:,.0f}",
    "Measures the increase in total revenue (USD 200,000) without subtracting the incremental USD 40,000 in variable support costs for 4,000 additional subscribers.",
    f"+USD {cm_tier_29:,.0f}",
    "Reports the total tiered contribution margin rather than the incremental gain over flat pricing.",
    rf"Flat pricing contribution margin: ${u_flat_29:,} \times (50 - 10) = \text{{USD }}{cm_flat_29:,.0f}$. "
    rf"Tiered pricing contribution margin: ${u_pro_29:,}(70 - 10) + {u_bas_29:,}(35 - 10) = 360,000 + 200,000 = \text{{USD }}{cm_tier_29:,.0f}$. "
    rf"Incremental contribution margin gain is $\text{{USD }}{cm_tier_29:,.0f} - \text{{USD }}{cm_flat_29:,.0f} = +\text{{USD }}{gain_29:,.0f}$.",
    True,
)

add_q1(
    "L1-CRP-030", M3, T3, "Distribution Channel Economics",
    "Assess direct-to-consumer versus wholesale distribution business models.",
    "Transitioning sales from third-party wholesale distributors to a direct-to-consumer (DTC) e-commerce channel most likely results in:",
    "Higher gross margins and direct customer data ownership, paired with higher customer acquisition costs and fulfillment expenses.",
    "Lower gross margins and elimination of all working capital inventory requirements.",
    "Eliminating wholesaler markups raises gross margin (not lowers it), and holding DTC inventory typically increases rather than eliminates inventory requirements.",
    "Complete elimination of marketing spend alongside guaranteed pricing power.",
    "DTC businesses typically incur substantially higher marketing and CAC expenses to drive direct traffic without retail shelf distribution.",
    "Selling direct-to-consumer captures the wholesale/retail markup (increasing gross margin) and gives the brand first-party customer analytics, while requiring higher investments in marketing (CAC), logistics, and inventory management.",
    False,
)

# L1-CRP-031 (Calc): Marketplace GMV take rate and net contribution
gmv_31, take_31, proc_fee_31, fix_plat_31 = 400.0, 0.12, 0.025, 22.0
net_rev_31 = gmv_31 * take_31
var_cost_31 = gmv_31 * proc_fee_31
ebit_31 = net_rev_31 - var_cost_31 - fix_plat_31
wrong_fee_on_rev_31 = net_rev_31 * (1 - proc_fee_31) - fix_plat_31
wrong_gmv_ebit_31 = gmv_31 - var_cost_31 - fix_plat_31
add_q1(
    "L1-CRP-031", M3, T3, "Platform Take-Rate Economics",
    "Analyze revenue recognition and profitability metrics for marketplace platforms.",
    f"An e-commerce marketplace processes USD {gmv_31:.0f} million in Gross Merchandise Value (GMV) while charging a {take_31*100:.0f}% seller take rate. Payment processing costs equal {proc_fee_31*100:.1f}% of GMV, and fixed platform operating costs are USD {fix_plat_31:.0f} million. Operating profit (EBIT) is closest to:",
    f"USD {ebit_31:.2f} million",
    f"USD {wrong_fee_on_rev_31:.2f} million",
    "Applies the 2.5% payment processing cost only to platform net revenue (USD 48M) instead of total processed GMV (USD 400M).",
    f"USD {wrong_gmv_ebit_31:.2f} million",
    "Treats total GMV (USD 400M) as the marketplace's own GAAP revenue rather than the 12% take rate.",
    rf"Platform net revenue equals $\text{{GMV}} \times \text{{Take Rate}} = 400 \times 0.12 = \text{{USD }}{net_rev_31:.1f}\text{{M}}$. "
    rf"Payment processing costs apply to full GMV: $400 \times 0.025 = \text{{USD }}{var_cost_31:.1f}\text{{M}}$. "
    rf"Operating profit is: "
    rf"$$\text{{EBIT}} = {net_rev_31:.1f} - {var_cost_31:.1f} - {fix_plat_31:.1f} = \text{{USD }}{ebit_31:.2f}\text{{ million}}$$",
    True,
)

add_q1(
    "L1-CRP-032", M3, T3, "Business Model Risk Profiling",
    "Identify macroeconomic, industry, and execution risks in corporate business models.",
    "Which business model characteristic provides the strongest structural protection against cyclical macroeconomic downturns?",
    "High recurring subscription revenue locked under multi-year mission-critical enterprise contracts with high switching costs.",
    "Discretionary luxury hardware sales funded primarily by one-time consumer financing promotions.",
    "Big-ticket discretionary purchases exhibit high income elasticity and sharp cyclical revenue contractions during recessions.",
    "Spot-priced commodity mining coupled with high fixed labor and debt service commitments.",
    "Commodity price cyclicality combined with high operating and financial leverage magnifies earnings volatility during downturns.",
    "Multi-year contracted recurring revenues for mission-critical services with high switching costs insulate cash flows from macro contractions far better than discretionary or spot-commodity sales.",
    False,
)

# =============================================================================
# LEVEL 1: MODULE 4 — CAPITAL ALLOCATION (L1-CRP-033 .. 046)
# =============================================================================
M4 = "CI-L1-M4"
T4 = "Capital Allocation"

add_q1(
    "L1-CRP-033", M4, T4, "Capital Budgeting Principles",
    "Apply core capital allocation principles regarding sunk costs, incremental cash flows, and financing costs.",
    "When estimating incremental after-tax cash flows for a proposed manufacturing expansion project, an analyst should include:",
    "The after-tax lost gross profit from existing product sales expected to be cannibalized by the new product.",
    "USD 1.5 million already spent and expensed last year on market feasibility consulting.",
    "Prior consulting outlays are sunk costs that cannot be recovered regardless of the accept/reject decision and must be excluded.",
    "Interest expense on the specific 5-year bank loan raised to finance the new factory equipment.",
    "Financing costs are already reflected in the WACC discount rate; subtracting interest from project cash flows double-counts financing costs.",
    "Capital budgeting relies strictly on incremental after-tax cash flows: externalities such as cannibalization and opportunity costs must be included, whereas sunk costs and financing charges (captured in WACC) are excluded.",
    False,
)

# L1-CRP-034 (Calc): Full Expansion Project NPV (Capex, NWC, OCF, Salvage, Tax)
capex_34, nwc_34, ebitda_34, n_34, salv_34, tax_34, r_34 = 120.0, 15.0, 48.0, 4, 24.0, 0.25, 0.10
depr_34 = capex_34 / n_34  # 30M/yr -> BV at t=4 is 0
ebit_34 = ebitda_34 - depr_34  # 18M/yr
ocf_34 = ebit_34 * (1 - tax_34) + depr_34  # 13.5 + 30 = 43.5M/yr
after_tax_salv_34 = salv_34 - tax_34 * (salv_34 - 0.0)  # 18.0M
cf0_34 = -(capex_34 + nwc_34)  # -135
term_34 = after_tax_salv_34 + nwc_34  # 33.0
cfs_34 = [cf0_34, ocf_34, ocf_34, ocf_34, ocf_34 + term_34]
npv_34 = sum(cf / ((1 + r_34) ** t) for t, cf in enumerate(cfs_34))
wrong_no_nwc_rec_34 = sum(cf / ((1 + r_34) ** t) for t, cf in enumerate([cf0_34, ocf_34, ocf_34, ocf_34, ocf_34 + after_tax_salv_34]))
wrong_pretax_salv_34 = sum(cf / ((1 + r_34) ** t) for t, cf in enumerate([cf0_34, ocf_34, ocf_34, ocf_34, ocf_34 + salv_34 + nwc_34]))
add_q1(
    "L1-CRP-034", M4, T4, "Expansion Project NPV",
    "Compute project NPV incorporating initial capital outlay, working capital, depreciation tax shields, and terminal salvage.",
    f"A firm evaluates a {n_34}-year expansion requiring USD {capex_34:.0f} million in equipment (depreciated straight-line to zero over {n_34} years) plus an upfront USD {nwc_34:.0f} million net working capital investment (fully recovered at Year {n_34}). Annual EBITDA is USD {ebitda_34:.0f} million, the equipment is sold at Year {n_34} for USD {salv_34:.0f} million, the corporate tax rate is {tax_34*100:.0f}%, and WACC is {r_34*100:.0f}%. The project's NPV is closest to:",
    f"USD {npv_34:.2f} million",
    f"USD {wrong_no_nwc_rec_34:.2f} million",
    "Includes the USD 15 million working capital outlay at Year 0 but forgets to recover it in Year 4.",
    f"USD {wrong_pretax_salv_34:.2f} million",
    "Uses the pre-tax salvage value (USD 24M) without deducting the 25% tax on the capital gain above zero book value.",
    rf"Initial outlay is $\text{{CF}}_0 = -(120 + 15) = -\text{{USD }}{abs(cf0_34):.0f}\text{{M}}$. "
    rf"Annual straight-line depreciation is $120 / 4 = \text{{USD }}{depr_34:.0f}\text{{M}}$, so $\text{{EBIT}} = 48 - 30 = \text{{USD }}{ebit_34:.0f}\text{{M}}$ and "
    rf"$\text{{OCF}} = 18(1 - 0.25) + 30 = \text{{USD }}{ocf_34:.1f}\text{{M}}$. "
    rf"At Year 4, book value is zero, so after-tax salvage is $24(1 - 0.25) = \text{{USD }}{after_tax_salv_34:.1f}\text{{M}}$ plus USD {nwc_34:.0f}M NWC recovery ($\text{{CF}}_4 = {ocf_34 + term_34:.1f}\text{{M}}$). "
    rf"$$\text{{NPV}} = -135 + \sum_{{t=1}}^{{3}} \frac{{43.5}}{{1.10^t}} + \frac{{76.5}}{{1.10^4}} = \text{{USD }}{npv_34:.2f}\text{{ million}}$$",
    True,
)

# L1-CRP-035 (Calc): IRR calculation
cfs_35 = [-100.0, 35.0, 45.0, 50.0]
irr_35 = calc_irr(cfs_35) * 100.0
wrong_avg_ret_35 = ((sum(cfs_35[1:]) / 100.0) ** (1 / 3) - 1) * 100.0
wrong_simple_roi_35 = (sum(cfs_35) / 100.0) / 3.0 * 100.0
add_q1(
    "L1-CRP-035", M4, T4, "Internal Rate of Return (IRR)",
    "Calculate and interpret the internal rate of return for multi-period cash flows.",
    "A capital project requires an initial investment of USD 100 million and produces end-of-year after-tax cash flows of USD 35 million in Year 1, USD 45 million in Year 2, and USD 50 million in Year 3. The project's internal rate of return (IRR) is closest to:",
    f"{irr_35:.2f}%",
    f"{wrong_avg_ret_35:.2f}%",
    "Computes the geometric average return on summed cash flows $(130/100)^{1/3} - 1$ rather than solving for the discount rate setting NPV to zero.",
    f"{wrong_simple_roi_35:.2f}%",
    "Computes the simple average annual return $(30/100)/3$ ignoring time value of money.",
    rf"The IRR is the discount rate $r$ that sets project NPV to zero: "
    rf"$$0 = -100 + \frac{{35}}{{1+r}} + \frac{{45}}{{(1+r)^2}} + \frac{{50}}{{(1+r)^3}}$$ "
    rf"Solving numerically yields $\text{{IRR}} = {irr_35:.2f}\%$ (checking at {irr_35:.2f}%: $\text{{NPV}} \approx 0$).",
    True,
)

# L1-CRP-036 (Calc): Crossover rate
cfs_a_36 = [-200.0, 120.0, 100.0, 40.0]
cfs_b_36 = [-200.0, 30.0, 80.0, 175.0]
diff_cfs_36 = [b - a for a, b in zip(cfs_a_36, cfs_b_36)]  # [0, -90, -20, 135]
# For t=1,2,3: -90 - 20/(1+r) + 135/(1+r)^2 = 0 -> let x = 1+r: -90x^2 - 20x + 135 = 0
irr_a_36 = calc_irr(cfs_a_36) * 100.0
irr_b_36 = calc_irr(cfs_b_36) * 100.0
xover_36 = calc_irr(diff_cfs_36[1:]) * 100.0
wrong_avg_irr_36 = 0.5 * (irr_a_36 + irr_b_36)
wrong_min_irr_36 = min(irr_a_36, irr_b_36)
add_q1(
    "L1-CRP-036", M4, T4, "Crossover Rate & Mutually Exclusive Ranking",
    "Determine the crossover rate at which two mutually exclusive projects have identical NPVs.",
    "Two mutually exclusive projects each cost USD 200 million today. Project A returns USD 120M, USD 100M, and USD 40M in Years 1–3; Project B returns USD 30M, USD 80M, and USD 175M in Years 1–3. The crossover discount rate at which both projects yield the same NPV is closest to:",
    f"{xover_36:.2f}%",
    f"{wrong_avg_irr_36:.2f}%",
    "Averages the standalone IRRs of Project A and Project B instead of computing the IRR of incremental cash flows.",
    f"{wrong_min_irr_36:.2f}%",
    "Mistakes the standalone IRR of Project B for the crossover rate between the two cash flow profiles.",
    rf"The crossover rate equals the IRR of incremental cash flows ($\text{{CF}}_B - \text{{CF}}_A = [0, -90, -20, +135]$): "
    rf"$$-90 - \frac{{20}}{{1+r^*}} + \frac{{135}}{{(1+r^*)^2}} = 0 \implies r^* = {xover_36:.2f}\%$$ "
    rf"At $r = {xover_36:.2f}\%$, both projects share an identical NPV.",
    True,
)

# L1-CRP-037 (Calc): Discounted Payback Period
c0_37, cfs_37, r_37 = 150.0, [50.0, 70.0, 80.0, 60.0], 0.10
pvs_37 = [cf / ((1 + r_37) ** t) for t, cf in enumerate(cfs_37, start=1)]
cum_pv_37 = []
s_37 = 0.0
for pv in pvs_37:
    s_37 += pv
    cum_pv_37.append(s_37)
# Year 2 cum PV = 45.4545 + 57.8512 = 103.3058; Year 3 PV = 60.1052
rem_37 = c0_37 - cum_pv_37[1]
dpb_37 = 2.0 + rem_37 / pvs_37[2]
pb_undisc_37 = 2.0 + (c0_37 - (cfs_37[0] + cfs_37[1])) / cfs_37[2]
wrong_yr3_frac_37 = 2.0 + rem_37 / cfs_37[2]
add_q1(
    "L1-CRP-037", M4, T4, "Discounted Payback Period",
    "Compute payback and discounted payback periods for capital investments.",
    f"A project requires USD {c0_37:.0f} million upfront and yields cash flows of USD 50M, USD 70M, USD 80M, and USD 60M at the end of Years 1–4. At a {r_37*100:.0f}% cost of capital, the discounted payback period is closest to:",
    f"{dpb_37:.2f} years",
    f"{pb_undisc_37:.2f} years",
    "Computes the undiscounted regular payback period rather than discounting each year's cash flow at 10%.",
    f"{wrong_yr3_frac_37:.2f} years",
    "Discounts Years 1 and 2 cash flows properly but divides the remaining balance by undiscounted Year 3 cash flow (USD 80M) instead of discounted Year 3 PV.",
    rf"Discounted cash flows at 10% are: Year 1 $= {pvs_37[0]:.2f}\text{{M}}$, Year 2 $= {pvs_37[1]:.2f}\text{{M}}$ (cumulative $= {cum_pv_37[1]:.2f}\text{{M}}$), and Year 3 $= {pvs_37[2]:.2f}\text{{M}}$. "
    rf"Remaining principal entering Year 3 is $150 - {cum_pv_37[1]:.2f} = {rem_37:.2f}\text{{M}}$: "
    rf"$$\text{{Discounted Payback}} = 2 + \frac{{{rem_37:.2f}}}{{{pvs_37[2]:.2f}}} = {dpb_37:.2f}\text{{ years}}$$",
    True,
)

# L1-CRP-038 (Calc): Profitability Index & Capital Rationing
# Budget = 100M. Indivisible projects:
# P1: Outlay 60M, NPV 21M (PI = 1.35)
# P2: Outlay 50M, NPV 20M (PI = 1.40)
# P3: Outlay 45M, NPV 18M (PI = 1.40)
# P4: Outlay 35M, NPV 11.9M (PI = 1.34)
# Wait: P2 + P3 = 95M, NPV = 38M. P1 + P4 = 95M, NPV = 32.9M. P2 + P4 = 85M, NPV = 31.9M.
# Let's make highest PI NOT equal highest NPV? No, let's test PI + budget constraint cleanly where P1 has highest standalone NPV (26M, outlay 80M -> PI=1.325) while P2 (50M, NPV 19M -> PI=1.38) + P3 (50M, NPV 17M -> PI=1.34) = 100M, total NPV = 36M!
b_38 = 100.0
projs_38 = [("Alpha", 80.0, 26.0), ("Beta", 50.0, 19.0), ("Gamma", 50.0, 17.0), ("Delta", 20.0, 5.0)]
# Combos <= 100: Alpha+Delta = 100 -> NPV = 31; Beta+Gamma = 100 -> NPV = 36; Beta+Delta = 70 -> 24
pi_alpha_38 = (80.0 + 26.0) / 80.0
pi_beta_38 = (50.0 + 19.0) / 50.0
max_npv_38 = 19.0 + 17.0
alpha_delta_38 = 26.0 + 5.0
add_q1(
    "L1-CRP-038", M4, T4, "Profitability Index & Capital Rationing",
    "Apply the Profitability Index to allocate capital under hard budget rationing.",
    "Under a strict USD 100 million capital budget, management evaluates four independent, indivisible projects: Alpha (Outlay USD 80M, NPV USD 26M), Beta (Outlay USD 50M, NPV USD 19M), Gamma (Outlay USD 50M, NPV USD 17M), and Delta (Outlay USD 20M, NPV USD 5M). Which selection maximizes shareholder value, and what is its total NPV?",
    f"Beta and Gamma; total NPV = USD {max_npv_38:.0f} million",
    f"Alpha and Delta; total NPV = USD {alpha_delta_38:.0f} million",
    "Selects Alpha for having the largest standalone dollar NPV (USD 26M), leaving only USD 20M for Delta (PI = 1.25) and achieving lower aggregate value.",
    "Alpha only; total NPV = USD 26 million",
    "Selects the single largest-NPV project without using remaining budget or ranking by Profitability Index.",
    rf"Rank projects by Profitability Index $\text{{PI}} = 1 + \frac{{\text{{NPV}}}}{{\text{{Outlay}}}}$: "
    rf"Beta ($\text{{PI}} = {pi_beta_38:.2f}$), Gamma ($\text{{PI}} = 1.34$), Alpha ($\text{{PI}} = {pi_alpha_38:.3f}$), Delta ($\text{{PI}} = 1.25$). "
    rf"Selecting Beta + Gamma consumes the full USD 100M budget and produces maximum total NPV of $19 + 17 = \text{{USD }}{max_npv_38:.0f}\text{{ million}}$.",
    True,
)

# L1-CRP-039 (Calc): ROIC vs WACC and EVA
ebit_39, tax_39, ic_39, wacc_39 = 45.0, 0.20, 250.0, 0.11
nopat_39 = ebit_39 * (1.0 - tax_39)  # 36.0M
roic_39 = nopat_39 / ic_39  # 14.4%
eva_39 = nopat_39 - wacc_39 * ic_39  # 36 - 27.5 = 8.5M
wrong_pretax_eva_39 = ebit_39 - wacc_39 * ic_39  # 17.5M
wrong_roic_only_39 = roic_39 * 100.0
add_q1(
    "L1-CRP-039", M4, T4, "ROIC, WACC, and Economic Profit",
    "Evaluate corporate capital efficiency using ROIC relative to WACC and Economic Value Added.",
    f"A division generates EBIT of USD {ebit_39:.0f} million on USD {ic_39:.0f} million of invested capital. If the corporate tax rate is {tax_39*100:.0f}% and WACC is {wacc_39*100:.0f}%, the division's Return on Invested Capital (ROIC) and Economic Value Added (EVA) are closest to:",
    f"ROIC = {roic_39*100:.1f}%; EVA = USD {eva_39:.1f} million",
    f"ROIC = {ebit_39/ic_39*100:.1f}%; EVA = USD {wrong_pretax_eva_39:.1f} million",
    "Computes ROIC and EVA using pre-tax EBIT instead of after-tax NOPAT.",
    f"ROIC = {roic_39*100:.1f}%; EVA = USD {nopat_39:.1f} million",
    "Computes ROIC correctly from NOPAT but omits the capital charge ($\\text{WACC} \\times \\text{Invested Capital}$) when stating EVA.",
    rf"Net Operating Profit After Tax is $\text{{NOPAT}} = \text{{EBIT}}(1 - t) = 45(0.80) = \text{{USD }}{nopat_39:.1f}\text{{M}}$. "
    rf"Thus, $\text{{ROIC}} = {nopat_39:.1f} / {ic_39:.0f} = {roic_39*100:.1f}\%$, exceeding the 11.0% WACC by 3.4%. "
    rf"$$\text{{EVA}} = \text{{NOPAT}} - (\text{{WACC}} \times \text{{Invested Capital}}) = {nopat_39:.1f} - 0.11({ic_39:.0f}) = \text{{USD }}{eva_39:.1f}\text{{ million}}$$",
    True,
)

add_q1(
    "L1-CRP-040", M4, T4, "NPV vs IRR Ranking Conflicts",
    "Explain why NPV dominates IRR when evaluating mutually exclusive or non-conventional projects.",
    "When comparing two mutually exclusive projects of different sizes and cash flow timing, NPV and IRR occasionally yield conflicting rankings. Which statement accurately explains why NPV is the superior decision criterion?",
    "NPV directly measures absolute dollar value added assuming interim cash flows are reinvested at the firm's opportunity cost of capital (WACC), whereas IRR assumes reinvestment at the project's own IRR.",
    "IRR properly scales mutually exclusive investments to reflect total dollar wealth created regardless of capital outlay.",
    "IRR is a percentage rate of return insensitive to project scale, so a tiny high-IRR project can appear superior to a large positive-NPV project.",
    "NPV always produces multiple solutions whenever project cash flows change signs more than once.",
    "Multiple solutions (up to $n$ real roots by Descartes' rule of signs) are a flaw of IRR for non-conventional cash flows; NPV always gives a single unique dollar value.",
    "NPV directly measures expected shareholder wealth creation in currency terms, correctly accounts for project scale, avoids multiple-root ambiguities on non-conventional cash flows, and assumes realistic reinvestment at WACC rather than the project's IRR.",
    False,
)

# L1-CRP-041 (Calc): Cannibalization & Opportunity Cost
rev_new_41, gm_new_41, cann_rev_41, gm_old_41, rent_lost_41, depr_41, tax_41, capex_41, n_41, r_41 = (
    50.0, 0.50, 12.0, 0.40, 4.0, 8.0, 0.25, 40.0, 5, 0.10
)
# Incremental EBIT = (50*0.50) - (12*0.40) - 4.0 - 8.0 = 25 - 4.8 - 4 - 8 = 8.2M
inc_ebit_41 = rev_new_41 * gm_new_41 - cann_rev_41 * gm_old_41 - rent_lost_41 - depr_41
inc_ocf_41 = inc_ebit_41 * (1.0 - tax_41) + depr_41  # 6.15 + 8 = 14.15M
npv_41 = -capex_41 + inc_ocf_41 * sum(1.0 / ((1.0 + r_41) ** t) for t in range(1, n_41 + 1))
wrong_no_cann_41 = ((rev_new_41 * gm_new_41 - rent_lost_41 - depr_41) * (1.0 - tax_41) + depr_41)
wrong_no_opp_41 = ((rev_new_41 * gm_new_41 - cann_rev_41 * gm_old_41 - depr_41) * (1.0 - tax_41) + depr_41)
add_q1(
    "L1-CRP-041", M4, T4, "Externalities & Opportunity Costs",
    "Incorporate cannibalization and opportunity costs into incremental cash flow estimation.",
    f"A beverage firm launches a new product requiring USD {capex_41:.0f} million equipment depreciated straight-line over {n_41} years (USD {depr_41:.0f}M/yr). The product generates USD {rev_new_41:.0f}M annual sales at a {gm_new_41*100:.0f}% gross margin, but cannibalizes USD {cann_rev_41:.0f}M of annual sales of an existing line carrying a {gm_old_41*100:.0f}% gross margin. Production also occupies a company-owned warehouse that could otherwise be leased out for USD {rent_lost_41:.0f}M/yr pre-tax. At a {tax_41*100:.0f}% tax rate, annual incremental after-tax operating cash flow (OCF) is closest to:",
    f"USD {inc_ocf_41:.2f} million",
    f"USD {wrong_no_cann_41:.2f} million",
    "Includes the foregone warehouse rent opportunity cost but ignores the USD 4.8M/yr gross profit lost from cannibalized existing sales.",
    f"USD {wrong_no_opp_41:.2f} million",
    "Deducts cannibalization but treats the owned warehouse as 'free', ignoring its USD 4.0M/yr pre-tax lease opportunity cost.",
    rf"Incremental gross profit is $50(0.50) - 12(0.40) = 25.0 - 4.8 = \text{{USD }}20.2\text{{M}}$. "
    rf"Subtracting the foregone lease opportunity cost (USD 4.0M) and depreciation (USD 8.0M) yields $\text{{EBIT}} = 20.2 - 4.0 - 8.0 = \text{{USD }}{inc_ebit_41:.1f}\text{{M}}$: "
    rf"$$\text{{Incremental OCF}} = {inc_ebit_41:.1f}(1 - {tax_41:.2f}) + {depr_41:.0f} = \text{{USD }}{inc_ocf_41:.2f}\text{{ million}}$$",
    True,
)

# L1-CRP-042 (Calc): Real Option to Abandon
i0_42, p_hi_42, cf_hi_42, cf_lo_42, aband_42, r_42 = 100.0, 0.50, 80.0, 20.0, 45.0, 0.10
# Two periods t=1, t=2: at t=1 high state gives 80 at t=1 + 80 at t=2; low state gives 20 at t=1 + 20 at t=2 OR abandon at t=1 for 45 (so receive 20 + 45 = 65 at t=1).
pv_hi_42 = cf_hi_42 / (1 + r_42) + cf_hi_42 / ((1 + r_42) ** 2)
pv_lo_no_opt_42 = cf_lo_42 / (1 + r_42) + cf_lo_42 / ((1 + r_42) ** 2)
static_npv_42 = -i0_42 + p_hi_42 * pv_hi_42 + (1 - p_hi_42) * pv_lo_no_opt_42
pv_lo_opt_42 = (cf_lo_42 + aband_42) / (1 + r_42)  # abandon after t=1 CF
opt_npv_42 = -i0_42 + p_hi_42 * pv_hi_42 + (1 - p_hi_42) * pv_lo_opt_42
opt_val_42 = opt_npv_42 - static_npv_42
wrong_full_pv_42 = (aband_42 - cf_lo_42 / (1 + r_42)) / (1 + r_42)
add_q1(
    "L1-CRP-042", M4, T4, "Real Options: Abandonment Option",
    "Value embedded real options to abandon, expand, or delay capital projects.",
    f"A 2-year project costs USD {i0_42:.0f} million today (WACC = {r_42*100:.0f}%). Demand is equally likely (50%/50%) to be High (USD {cf_hi_42:.0f}M/yr in Years 1 and 2) or Low (USD {cf_lo_42:.0f}M/yr in Years 1 and 2). After observing Year 1 cash flow, management can abandon the project at Year 1 for a certain salvage value of USD {aband_42:.0f} million (forgoing Year 2 cash flow). The value of the abandonment real option is closest to:",
    f"USD {opt_val_42:.2f} million",
    f"USD {wrong_full_pv_42:.2f} million",
    "Fails to multiply the incremental abandonment payoff in the Low state by its 50% probability of occurrence.",
    f"USD {opt_npv_42:.2f} million",
    "Reports the total project NPV including the option rather than the standalone value of the abandonment option.",
    rf"Without abandonment, Low-state Year 2 PV at Year 1 is $20 / 1.10 = \text{{USD }}{cf_lo_42/(1+r_42):.2f}\text{{M}}$, whereas abandoning at Year 1 captures $\text{{USD }}{aband_42:.0f}\text{{M}}$. "
    rf"The Year 1 gain in the Low state is $45.00 - {cf_lo_42/(1+r_42):.2f} = \text{{USD }}{aband_42 - cf_lo_42/(1+r_42):.2f}\text{{M}}$. "
    rf"Weighting by the 50% probability and discounting from Year 1 to Year 0: "
    rf"$$\text{{Option Value}} = 0.50 \times \frac{{{aband_42 - cf_lo_42/(1+r_42):.2f}}}{{1.10}} = \text{{USD }}{opt_val_42:.2f}\text{{ million}}$$ "
    rf"(Static NPV = USD {static_npv_42:.2f}M; NPV with option = USD {opt_npv_42:.2f}M).",
    True,
)

# L1-CRP-043 (Calc): Timing / Delay real option
# Invest today: cost 100, PV = 104 -> NPV_now = +4.
# Wait 1 year: 50% prob PV at t=1 is 150 (cost 100 -> NPV_1 = +50); 50% prob PV at t=1 is 70 (cost 100 -> don't invest -> 0).
# Expected NPV_wait = (0.50 * 50 + 0.50 * 0) / 1.10 = 22.73M!
npv_now_43, p_up_43, npv_up_t1_43, r_43 = 4.0, 0.50, 50.0, 0.10
npv_wait_43 = (p_up_43 * npv_up_t1_43) / (1.0 + r_43)
opt_delay_val_43 = npv_wait_43 - npv_now_43
wrong_undisc_43 = p_up_43 * npv_up_t1_43
add_q1(
    "L1-CRP-043", M4, T4, "Real Options: Timing / Delay Option",
    "Determine whether delaying a capital investment creates value via a timing real option.",
    f"Investing USD 100 million immediately yields an expected NPV of USD {npv_now_43:.0f} million. Alternatively, management holds a 1-year exclusive license allowing it to wait 1 year before deciding to invest USD 100 million. In 1 year, there is a 50% chance market demand surges (project Year 1 NPV = +USD {npv_up_t1_43:.0f} million) and a 50% chance demand slumps (Year 1 NPV = -USD 30 million, so management declines). At a {r_43*100:.0f}% discount rate, the project's expected NPV today if management waits 1 year is closest to:",
    f"USD {npv_wait_43:.2f} million",
    f"USD {wrong_undisc_43:.2f} million",
    "Computes the probability-weighted Year 1 payoff ($0.50 \\times 50 = 25.00$) without discounting it back from Year 1 to Year 0.",
    f"USD {(p_up_43*npv_up_t1_43 + 0.5*(-30.0))/(1+r_43):.2f} million",
    "Assumes management still invests in the unfavorable slump state rather than exercising its option to walk away.",
    rf"Waiting creates asymmetric option value because management invests only in the favorable state (NPV = +USD 50M) and avoids investing in the slump state (payoff = USD 0): "
    rf"$$\text{{NPV}}_{{\text{{wait}}}} = \frac{{0.50(\text{{USD }}50\text{{M}}) + 0.50(0)}}{{1.10}} = \text{{USD }}{npv_wait_43:.2f}\text{{ million}}$$ "
    rf"Because $\text{{NPV}}_{{\text{{wait}}}} > \text{{NPV}}_{{\text{{now}}}}$ (USD {npv_wait_43:.2f}M vs. USD {npv_now_43:.0f}M), waiting creates USD {opt_delay_val_43:.2f}M of incremental timing option value.",
    True,
)

# L1-CRP-044 (Calc): Expansion real option
npv_phase1_44, p_exp_44, npv_exp_t2_44, r_44 = -6.0, 0.40, 40.0, 0.10
pv_exp_44 = (p_exp_44 * npv_exp_t2_44) / ((1.0 + r_44) ** 2)
tot_npv_44 = npv_phase1_44 + pv_exp_44
wrong_t1_44 = npv_phase1_44 + (p_exp_44 * npv_exp_t2_44) / (1.0 + r_44)
add_q1(
    "L1-CRP-044", M4, T4, "Real Options: Growth & Expansion Option",
    "Incorporate expansion real option values into negative static-NPV pilot investments.",
    f"A pilot factory generates a standalone static NPV of -USD {abs(npv_phase1_44):.0f} million. However, building the pilot grants a strategic option at Year 2 to launch a full commercial scale-up if clinical validation succeeds (probability {p_exp_44*100:.0f}%), yielding a Year 2 NPV of +USD {npv_exp_t2_44:.0f} million (and USD 0 if validation fails). At a {r_44*100:.0f}% discount rate, the project's strategic NPV including the expansion option is closest to:",
    f"USD {tot_npv_44:.2f} million",
    f"USD {wrong_t1_44:.2f} million",
    "Discounts the Year 2 expansion option payoff for only 1 year instead of 2 years.",
    f"-USD {abs(npv_phase1_44):.2f} million",
    "Evaluates only the standalone static NPV and ignores the embedded expansion option.",
    rf"The present value of the Year 2 expansion option is: "
    rf"$$\text{{PV}}(\text{{Expansion Option}}) = \frac{{0.40 \times \text{{USD }}40\text{{M}}}}{{1.10^2}} = \text{{USD }}{pv_exp_44:.2f}\text{{ million}}$$ "
    rf"Adding the static pilot NPV yields strategic NPV: "
    rf"$$\text{{Strategic NPV}} = -{abs(npv_phase1_44):.0f} + {pv_exp_44:.2f} = \text{{USD }}{tot_npv_44:.2f}\text{{ million}}$$",
    True,
)

add_q1(
    "L1-CRP-045", M4, T4, "Capital Allocation Pitfalls",
    "Identify common analytical and behavioral biases in corporate capital allocation.",
    "Which practice represents a classic behavioral or analytical error during corporate capital allocation?",
    "Using nominal cash flows discounted at a real (inflation-adjusted) WACC, causing upward NPV bias.",
    "Evaluating projects strictly on incremental after-tax cash flows discounted at project-specific risk-adjusted WACC.",
    "Matching project risk to discount rate and using incremental after-tax cash flows is best-practice capital budgeting.",
    "Applying post-audit reviews to compare realized project cash flows against initial budget forecasts.",
    "Post-audits enhance accountability and forecasting discipline, helping mitigate managerial over-optimism.",
    "Cash flows and discount rates must maintain strict inflation consistency: nominal cash flows require a nominal discount rate, while real cash flows require a real discount rate. Discounting nominal flows at a lower real rate systematically overstates NPV.",
    False,
)

# L1-CRP-046 (Calc): Equivalent Annual Annuity (EAA)
npv_x_46, n_x_46, npv_y_46, n_y_46, r_46 = 18.0, 3, 25.0, 5, 0.10
pvifa_x_46 = sum(1.0 / ((1 + r_46) ** t) for t in range(1, n_x_46 + 1))
pvifa_y_46 = sum(1.0 / ((1 + r_46) ** t) for t in range(1, n_y_46 + 1))
eaa_x_46 = npv_x_46 / pvifa_x_46
eaa_y_46 = npv_y_46 / pvifa_y_46
wrong_avg_x_46 = npv_x_46 / n_x_46
wrong_avg_y_46 = npv_y_46 / n_y_46
add_q1(
    "L1-CRP-046", M4, T4, "Unequal-Lived Projects (EAA)",
    "Apply the Equivalent Annual Annuity method to compare mutually exclusive projects with different useful lives.",
    f"A firm must choose between two mutually exclusive machines that can be continuously replaced upon expiration, given a {r_46*100:.0f}% WACC. Machine X has a {n_x_46}-year life and NPV of USD {npv_x_46:.0f} million; Machine Y has a {n_y_46}-year life and NPV of USD {npv_y_46:.0f} million. Based on the Equivalent Annual Annuity (EAA) method, management should select:",
    f"Machine X (EAA = USD {eaa_x_46:.2f}M vs. USD {eaa_y_46:.2f}M for Machine Y)",
    f"Machine Y (EAA = USD {eaa_y_46:.2f}M vs. USD {eaa_x_46:.2f}M for Machine X)",
    "Selects Machine Y based on higher single-cycle NPV (USD 25M vs USD 18M) despite its lower annualized EAA.",
    f"Machine X (EAA = USD {wrong_avg_x_46:.2f}M vs. USD {wrong_avg_y_46:.2f}M for Machine Y)",
    "Divides each project's NPV by simple project life in years instead of its annuity present value factor ($\\text{PVIFA}_{r,n}$).",
    rf"For repeatable projects with unequal lives, divide each project's NPV by its annuity factor at 10%: "
    rf"$$\text{{EAA}}_X = \frac{{18.0}}{{{pvifa_x_46:.4f}}} = \text{{USD }}{eaa_x_46:.2f}\text{{M/yr}}, \quad \text{{EAA}}_Y = \frac{{25.0}}{{{pvifa_y_46:.4f}}} = \text{{USD }}{eaa_y_46:.2f}\text{{M/yr}}$$ "
    rf"Machine X delivers higher annualized economic value and should be chosen.",
    True,
)

# =============================================================================
# LEVEL 1: MODULE 5 — WORKING CAPITAL & LIQUIDITY (L1-CRP-047 .. 058)
# =============================================================================
M5 = "CI-L1-M5"
T5 = "Working Capital & Liquidity"

add_q1(
    "L1-CRP-047", M5, T5, "Primary vs Secondary Liquidity Sources",
    "Distinguish primary sources of liquidity from secondary sources of liquidity.",
    "Which action represents a secondary source of liquidity rather than a primary source of liquidity?",
    "Liquidating non-core factory equipment and renegotiating bank debt covenants during a cash crunch.",
    "Drawing down an existing committed revolving bank credit facility.",
    "Committed bank lines of credit, alongside ready cash and short-term marketable securities, are primary sources of liquidity used in normal operations.",
    "Collecting maturing customer accounts receivable and sweeping daily cash balances.",
    "Routine cash management and receivables collection are primary liquidity sources that do not disrupt ongoing business operations.",
    "Primary sources of liquidity (ready cash, short-term investments, trade credit, and bank credit lines) preserve normal operations. Secondary sources (asset sales, debt restructuring, equity issuance in distress, or bankruptcy protection) alter business operations or financial structure and often signal financial distress.",
    False,
)

add_q1(
    "L1-CRP-048", M5, T5, "Drags and Pulls on Liquidity",
    "Identify drags and pulls on corporate liquidity management.",
    "A major raw-materials supplier reduces a manufacturer's payment window from net 60 days to cash-on-delivery while an economic slowdown delays customer invoice payments. These two developments represent, respectively:",
    "A pull on liquidity and a drag on liquidity.",
    "A drag on liquidity and a pull on liquidity.",
    "Reverses the definitions: accelerating vendor cash outflows is a pull, whereas slowing customer cash inflows is a drag.",
    "Two primary sources of liquidity.",
    "Both changes tighten cash availability and weaken the firm's short-term liquidity position.",
    "Pulls on liquidity accelerate cash outflows (such as reduced supplier credit limits, early payment demands, or credit line reductions). Drags on liquidity delay cash inflows (such as uncollected receivables, obsolete inventory, or tight credit markets).",
    False,
)

# L1-CRP-049 (Calc): Operating Cycle & Cash Conversion Cycle
rev_49, cogs_49, inv_49, ar_49, ap_49 = 730.0, 547.5, 90.0, 110.0, 60.0
doh_49 = inv_49 / (cogs_49 / 365.0)  # 60.0 days
dso_49 = ar_49 / (rev_49 / 365.0)    # 55.0 days
dpo_49 = ap_49 / (cogs_49 / 365.0)   # 40.0 days
oc_49 = doh_49 + dso_49              # 115.0 days
ccc_49 = doh_49 + dso_49 - dpo_49    # 75.0 days
wrong_rev_ap_49 = doh_49 + dso_49 - (ap_49 / (rev_49 / 365.0))
add_q1(
    "L1-CRP-049", M5, T5, "Operating Cycle & Cash Conversion Cycle",
    "Calculate days of inventory on hand, days sales outstanding, days payable outstanding, and the cash conversion cycle.",
    f"Using a 365-day year, a distributor reports annual revenue of USD {rev_49:.0f} million, COGS of USD {cogs_49:.1f} million, average inventory of USD {inv_49:.0f} million, average accounts receivable of USD {ar_49:.0f} million, and average accounts payable of USD {ap_49:.0f} million. Its Operating Cycle and Cash Conversion Cycle (CCC) are closest to:",
    f"Operating Cycle = {oc_49:.1f} days; CCC = {ccc_49:.1f} days",
    f"Operating Cycle = {oc_49:.1f} days; CCC = {wrong_rev_ap_49:.1f} days",
    "Computes DPO using daily revenue (USD 2.0M/day) instead of daily COGS (USD 1.5M/day).",
    f"Operating Cycle = {ccc_49:.1f} days; CCC = {oc_49:.1f} days",
    "Swaps the definitions of Operating Cycle ($\\text{DOH} + \\text{DSO}$) and Cash Conversion Cycle ($\\text{DOH} + \\text{DSO} - \\text{DPO}$).",
    rf"Daily revenue is $730 / 365 = \text{{USD }}2.0\text{{M/day}}$ and daily COGS is $547.5 / 365 = \text{{USD }}1.5\text{{M/day}}$: "
    rf"$$\text{{DOH}} = \frac{{90}}{{1.5}} = {doh_49:.1f}\text{{ d}}, \quad \text{{DSO}} = \frac{{110}}{{2.0}} = {dso_49:.1f}\text{{ d}}, \quad \text{{DPO}} = \frac{{60}}{{1.5}} = {dpo_49:.1f}\text{{ d}}$$ "
    rf"Thus, $\text{{Operating Cycle}} = {doh_49:.1f} + {dso_49:.1f} = {oc_49:.1f}\text{{ days}}$ and $\text{{CCC}} = {oc_49:.1f} - {dpo_49:.1f} = {ccc_49:.1f}\text{{ days}}$.",
    True,
)

# L1-CRP-050 (Calc): Cash released from CCC reduction
rev_50, cogs_50, d_dso_50, d_dpo_50 = 1_095.0, 730.0, 6.0, 5.0
# Daily rev = 3.0M, Daily COGS = 2.0M
cash_ar_50 = d_dso_50 * (rev_50 / 365.0)   # 18.0M
cash_ap_50 = d_dpo_50 * (cogs_50 / 365.0)  # 10.0M
tot_cash_50 = cash_ar_50 + cash_ap_50       # 28.0M
wrong_sub_50 = cash_ar_50 - cash_ap_50
wrong_rev_both_50 = (d_dso_50 + d_dpo_50) * (rev_50 / 365.0)
add_q1(
    "L1-CRP-050", M5, T5, "Working Capital Cash Release",
    "Estimate working capital cash flow generated by shortening the cash conversion cycle.",
    f"A firm with annual revenue of USD {rev_50:,.0f} million and COGS of USD {cogs_50:.0f} million implements working capital reforms that trim DSO by {d_dso_50:.0f} days and extend DPO by {d_dpo_50:.0f} days (365-day year). Assuming revenue and COGS remain unchanged, total cash released from net working capital is closest to:",
    f"USD {tot_cash_50:.1f} million",
    f"USD {wrong_sub_50:.1f} million",
    "Subtracts the DPO extension benefit from the AR reduction rather than adding both cash inflows.",
    f"USD {wrong_rev_both_50:.1f} million",
    "Applies daily revenue (USD 3.0M/day) to the DPO extension instead of daily COGS (USD 2.0M/day).",
    rf"Daily sales equal $1,095 / 365 = \text{{USD }}3.0\text{{M/day}}$ and daily COGS equal $730 / 365 = \text{{USD }}2.0\text{{M/day}}$. "
    rf"Reducing receivables releases $6 \times 3.0 = \text{{USD }}{cash_ar_50:.1f}\text{{M}}$, while stretching payables retains $5 \times 2.0 = \text{{USD }}{cash_ap_50:.1f}\text{{M}}$: "
    rf"$$\text{{Total Cash Released}} = {cash_ar_50:.1f} + {cash_ap_50:.1f} = \text{{USD }}{tot_cash_50:.1f}\text{{ million}}$$",
    True,
)

# L1-CRP-051 (Calc): Cost of Trade Credit EAR
disc_51, disc_days_51, net_days_51 = 0.02, 10, 45
period_rate_51 = disc_51 / (1.0 - disc_51)
periods_51 = 365.0 / (net_days_51 - disc_days_51)
ear_51 = ((1.0 + period_rate_51) ** periods_51 - 1.0) * 100.0
wrong_apr_51 = period_rate_51 * periods_51 * 100.0
wrong_full_net_51 = ((1.0 + period_rate_51) ** (365.0 / net_days_51) - 1.0) * 100.0
add_q1(
    "L1-CRP-051", M5, T5, "Cost of Trade Credit",
    "Calculate the effective annual rate (EAR) of forgoing a supplier's trade credit discount.",
    f"A vendor offers trade credit terms of '2/{disc_days_51}, net {net_days_51}'. Using a 365-day year, the effective annual rate (EAR) of declining the early-payment discount and paying on Day {net_days_51} is closest to:",
    f"{ear_51:.2f}%",
    f"{wrong_apr_51:.2f}%",
    "Computes the uncompounded simple APR ($2.0408\\% \\times 365/35$) instead of compounding over the year.",
    f"{wrong_full_net_51:.2f}%",
    "Uses the full 45-day net period in the exponent instead of the 35-day credit window ($45 - 10$).",
    rf"Forgoing the 2% discount borrows 98% of the invoice for $45 - 10 = 35$ extra days at a periodic cost of $0.02 / 0.98 = {period_rate_51*100:.4f}\%$: "
    rf"$$\text{{EAR}} = \left(1 + \frac{{0.02}}{{0.98}}\right)^{{365/35}} - 1 = {ear_51:.2f}\%$$",
    True,
)

# L1-CRP-052 (Calc): Trade credit vs Bank loan spread comparison
disc_52, d_days_52, n_days_52, bank_ear_52 = 0.015, 10, 40, 11.50
tc_ear_52 = ((1.0 + disc_52 / (1.0 - disc_52)) ** (365.0 / (n_days_52 - d_days_52)) - 1.0) * 100.0
diff_bps_52 = (tc_ear_52 - bank_ear_52) * 100.0
wrong_apr_diff_52 = ((disc_52 / (1.0 - disc_52)) * (365.0 / (n_days_52 - d_days_52)) * 100.0 - bank_ear_52) * 100.0
add_q1(
    "L1-CRP-052", M5, T5, "Trade Credit vs Short-Term Bank Debt",
    "Compare trade credit financing costs against bank revolving lines of credit.",
    f"A supplier quotes terms of '1.5/{d_days_52}, net {n_days_52}' (365-day year), while a company's revolving credit line carries an effective annual rate of {bank_ear_52:.2f}%. How much cheaper (in annual percentage rate terms, rounded to the nearest basis point) is borrowing on the bank line to take the supplier discount compared with skipping the discount?",
    f"{diff_bps_52:,.0f} bps",
    f"{wrong_apr_diff_52:,.0f} bps",
    "Uses the simple annualized trade credit APR rather than the compounded trade credit EAR.",
    "0 bps (the supplier credit is cheaper than the bank line)",
    "Underestimates the annualized cost of 1.5% for 30 days, which compounds to over 20% annually.",
    rf"Trade credit EAR for '1.5/10, net 40' over $40 - 10 = 30$ financing days is: "
    rf"$$\text{{EAR}}_{{\text{{TC}}}} = \left(1 + \frac{{0.015}}{{0.985}}\right)^{{365/30}} - 1 = {tc_ear_52:.2f}\%$$ "
    rf"Borrowing on the {bank_ear_52:.2f}% bank line saves ${tc_ear_52:.2f}\% - {bank_ear_52:.2f}\% = {tc_ear_52 - bank_ear_52:.2f}\%$, or {diff_bps_52:,.0f} bps.",
    True,
)

# L1-CRP-053 (Calc): Line of credit with commitment fee + compensating balance
fac_53, draw_53, r_53, comm_53, cb_53 = 20.0, 12.0, 0.08, 0.005, 0.10
int_cost_53 = draw_53 * r_53                 # 0.96M
comm_cost_53 = (fac_53 - draw_53) * comm_53  # 0.04M
tot_cost_53 = int_cost_53 + comm_cost_53     # 1.00M
usable_53 = draw_53 * (1.0 - cb_53)          # 10.80M
eff_rate_53 = (tot_cost_53 / usable_53) * 100.0
wrong_no_cb_53 = (tot_cost_53 / draw_53) * 100.0
wrong_no_comm_53 = (int_cost_53 / usable_53) * 100.0
add_q1(
    "L1-CRP-053", M5, T5, "Bank Credit Facility Effective Cost",
    "Compute the effective borrowing cost of a bank line of credit with commitment fees and compensating balances.",
    f"A firm secures a USD {fac_53:.0f} million revolving credit facility at an {r_53*100:.1f}% annual interest rate, a {comm_53*100:.2f}% annual commitment fee on the unused portion, and a {cb_53*100:.0f}% non-interest-bearing compensating balance on drawn amounts (the firm otherwise holds zero cash). If the firm draws USD {draw_53:.0f} million continuously for a full year, its effective annual financing cost is closest to:",
    f"{eff_rate_53:.2f}%",
    f"{wrong_no_cb_53:.2f}%",
    "Includes the commitment fee but divides by the full USD 12M drawn instead of the USD 10.8M usable proceeds after the 10% compensating balance.",
    f"{wrong_no_comm_53:.2f}%",
    "Adjusts usable proceeds for the compensating balance but omits the USD 40,000 commitment fee on the unused USD 8M credit line.",
    rf"Total annual facility cost equals interest plus commitment fee: "
    rf"$$\text{{Total Cost}} = 12(0.08) + (20 - 12)(0.005) = 0.96 + 0.04 = \text{{USD }}{tot_cost_53:.2f}\text{{M}}$$ "
    rf"Because 10% of the draw must stay idle as a compensating balance, usable cash is $12(1 - 0.10) = \text{{USD }}{usable_53:.1f}\text{{M}}$: "
    rf"$$\text{{Effective Rate}} = \frac{{1.00}}{{10.80}} = {eff_rate_53:.2f}\%$$",
    True,
)

# L1-CRP-054 (Calc): Commercial Paper effective annual cost
face_54, disc_r_54, days_54, dealer_54, backup_54 = 10_000_000.0, 0.048, 90, 12_000.0, 8_000.0
disc_amt_54 = face_54 * disc_r_54 * (days_54 / 360.0)  # 120,000
tot_cost_54 = disc_amt_54 + dealer_54 + backup_54      # 140,000
net_proc_54 = face_54 - tot_cost_54                    # 9,860,000
per_cost_54 = tot_cost_54 / net_proc_54
ear_cp_54 = ((1.0 + per_cost_54) ** (365.0 / days_54) - 1.0) * 100.0
wrong_apr_54 = per_cost_54 * (365.0 / days_54) * 100.0
wrong_no_fees_54 = ((1.0 + disc_amt_54 / (face_54 - disc_amt_54)) ** (365.0 / days_54) - 1.0) * 100.0
add_q1(
    "L1-CRP-054", M5, T5, "Commercial Paper Issuance Cost",
    "Calculate the effective annual yield on discount-basis commercial paper including dealer and backup fees.",
    f"An investment-grade corporation issues {days_54}-day commercial paper with a USD {face_54/1e6:.0f} million face value at a {disc_r_54*100:.2f}% annual discount rate (360-day discount basis), incurring USD {dealer_54:,.0f} in dealer fees and USD {backup_54:,.0f} in backup liquidity line fees deducted from proceeds at issuance. On a 365-day effective annual yield basis, the effective annual cost of the commercial paper is closest to:",
    f"{ear_cp_54:.2f}%",
    f"{wrong_apr_54:.2f}%",
    "Multiplies the 90-day holding-period cost by $365/90$ without compounding.",
    f"{wrong_no_fees_54:.2f}%",
    "Excludes the USD 20,000 combined dealer and backup line fees from financing cost and net proceeds.",
    rf"Discount interest is $\text{{USD }}10\text{{M}} \times 4.80\% \times (90/360) = \text{{USD }}{disc_amt_54:,.0f}$. "
    rf"Adding USD {dealer_54 + backup_54:,.0f} in fees yields total 90-day cost of USD {tot_cost_54:,.0f} and net proceeds of USD {net_proc_54:,.0f}. "
    rf"$$\text{{EAR}} = \left(1 + \frac{{{tot_cost_54:,.0f}}}{{{net_proc_54:,.0f}}}\right)^{{365/90}} - 1 = {ear_cp_54:.2f}\%$$",
    True,
)

# L1-CRP-055 (Calc): Factoring receivables effective annual cost
ar_55, days_55, fact_fee_55, int_rate_55 = 1_000_000.0, 30, 0.012, 0.09
fee_55 = ar_55 * fact_fee_55                           # 12,000
int_55 = ar_55 * int_rate_55 * (days_55 / 365.0)       # 7,397.26
tot_55 = fee_55 + int_55
net_55 = ar_55 - tot_55
ear_55 = ((1.0 + tot_55 / net_55) ** (365.0 / days_55) - 1.0) * 100.0
wrong_apr_55 = (tot_55 / net_55) * (365.0 / days_55) * 100.0
wrong_no_fee_55 = ((1.0 + int_55 / (ar_55 - int_55)) ** (365.0 / days_55) - 1.0) * 100.0
add_q1(
    "L1-CRP-055", M5, T5, "Accounts Receivable Factoring",
    "Evaluate the annualized cost of factoring accounts receivable.",
    f"A manufacturer factors USD {ar_55/1e6:.0f} million of {days_55}-day accounts receivable non-recourse with no reserve holdback. The factor charges a {fact_fee_55*100:.1f}% flat factoring fee and deducts {int_rate_55*100:.1f}% annual simple interest (365-day year) upfront on the full USD 1.0 million face value. The effective annual rate (EAR) on the net proceeds received is closest to:",
    f"{ear_55:.2f}%",
    f"{wrong_apr_55:.2f}%",
    "Computes an uncompounded simple APR instead of compounding the 30-day periodic cost over $365/30$ periods.",
    f"{wrong_no_fee_55:.2f}%",
    "Includes only the 9% interest charge and ignores the 1.2% upfront factoring fee.",
    rf"Upfront charges equal the factoring fee ($\text{{USD }}{fee_55:,.0f}$) plus 30-day interest ($1,000,000 \times 9\% \times 30/365 = \text{{USD }}{int_55:,.2f}$), totaling USD {tot_55:,.2f}. "
    rf"Net cash received is USD {net_55:,.2f}: "
    rf"$$\text{{EAR}} = \left(1 + \frac{{{tot_55:,.2f}}}{{{net_55:,.2f}}}\right)^{{365/30}} - 1 = {ear_55:.2f}\%$$",
    True,
)

# L1-CRP-056 (Calc): Quick Ratio impact of cash AP paydown
cash_56, mkt_56, ar_56, inv_56, cl_56, pay_56 = 8.0, 4.0, 15.0, 18.0, 30.0, 6.0
qr0_56 = (cash_56 + mkt_56 + ar_56) / cl_56               # 27/30 = 0.90
qr1_56 = (cash_56 - pay_56 + mkt_56 + ar_56) / (cl_56 - pay_56)  # 21/24 = 0.875
cr1_56 = (cash_56 - pay_56 + mkt_56 + ar_56 + inv_56) / (cl_56 - pay_56) # 39/24 = 1.625
add_q1(
    "L1-CRP-056", M5, T5, "Liquidity Ratio Dynamics",
    "Determine how working capital cash transactions affect current and quick ratios.",
    f"A retailer holds USD {cash_56:.0f}M in cash, USD {mkt_56:.0f}M in marketable securities, USD {ar_56:.0f}M in accounts receivable, and USD {inv_56:.0f}M in inventory against USD {cl_56:.0f}M in current liabilities. If the retailer uses USD {pay_56:.0f}M of cash to pay down USD {pay_56:.0f}M of accounts payable, its post-transaction Quick Ratio is closest to:",
    f"{qr1_56:.3f}x (declining from {qr0_56:.2f}x)",
    f"{cr1_56:.3f}x (increasing from {(cash_56+mkt_56+ar_56+inv_56)/cl_56:.2f}x)",
    "Computes the Current Ratio (including USD 18M of inventory) instead of the Quick Ratio.",
    f"{qr0_56:.3f}x (unchanged at {qr0_56:.2f}x)",
    "Assumes equal reductions in numerator and denominator leave a ratio below 1.0x unchanged.",
    rf"Initial Quick Ratio is $(8 + 4 + 15) / 30 = {qr0_56:.2f}\text{{x}}$. "
    rf"Because the initial Quick Ratio is below 1.0x, reducing both quick assets and current liabilities by USD {pay_56:.0f}M lowers the Quick Ratio further: "
    rf"$$\text{{New Quick Ratio}} = \frac{{27 - 6}}{{30 - 6}} = \frac{{21}}{{24}} = {qr1_56:.3f}\text{{x}}$$",
    True,
)

add_q1(
    "L1-CRP-057", M5, T5, "Working Capital Financing Policies",
    "Compare conservative, moderate (maturity-matching), and aggressive working capital policies.",
    "Under an aggressive working capital financing strategy, a firm finances:",
    "All temporary current assets plus a portion of permanent current assets (or fixed assets) using short-term debt, increasing rollover and interest-rate risk.",
    "Both permanent current assets and most seasonal working capital fluctuations with long-term debt and common equity.",
    "Describes a conservative working capital financing policy, which lowers rollover risk at the expense of higher long-term funding costs.",
    "Temporary seasonal inventory spikes exclusively with matching 90-day commercial paper while funding permanent assets with long-term capital.",
    "Describes a moderate (maturity-matching) working capital approach.",
    "An aggressive financing policy relies heavily on short-term liabilities to fund not only seasonal peaks but also part of permanent working capital. While typically lowering interest expense when yield curves are upward-sloping, it exposes the firm to refinancing/rollover risk.",
    False,
)

# L1-CRP-058 (Calc): Extending customer credit terms (net 30 -> net 60)
s0_58, s1_58, cm_58, bd0_58, bd1_58, dso0_58, dso1_58, k_58 = 50.0, 56.0, 0.30, 0.01, 0.02, 30.0, 60.0, 0.10
inc_cm_58 = (s1_58 - s0_58) * cm_58 * 1e6  # 1,800,000
inc_bd_58 = (s1_58 * bd1_58 - s0_58 * bd0_58) * 1e6  # (1.12 - 0.50)M = 620,000
ar0_58 = s0_58 * 1e6 * (dso0_58 / 365.0)
ar1_58 = s1_58 * 1e6 * (dso1_58 / 365.0)
inc_fin_58 = (ar1_58 - ar0_58) * k_58
net_ben_58 = inc_cm_58 - inc_bd_58 - inc_fin_58
wrong_no_fin_58 = inc_cm_58 - inc_bd_58
wrong_bd_new_only_58 = inc_cm_58 - ((s1_58 - s0_58) * bd1_58 * 1e6) - inc_fin_58
add_q1(
    "L1-CRP-058", M5, T5, "Credit Policy Evaluation",
    "Evaluate incremental profitability from relaxing trade credit terms.",
    f"A wholesaler considers relaxing customer credit from net {dso0_58:.0f} to net {dso1_58:.0f} (365-day year). Annual sales are projected to grow from USD {s0_58:.0f}M to USD {s1_58:.0f}M at a {cm_58*100:.0f}% contribution margin, but bad-debt losses across all sales will rise from {bd0_58*100:.0f}% to {bd1_58*100:.0f}% and DSO will shift from {dso0_58:.0f} to {dso1_58:.0f} days. At a {k_58*100:.0f}% pre-tax financing cost on incremental receivables, the incremental annual pre-tax net benefit is closest to:",
    f"USD {net_ben_58:,.0f}",
    f"USD {wrong_no_fin_58:,.0f}",
    "Captures higher contribution margin and bad debts but omits the 10% financing cost of carrying larger receivables.",
    f"USD {wrong_bd_new_only_58:,.0f}",
    "Applies the higher 2% bad-debt rate only to the USD 6M incremental sales rather than to all USD 56M of sales.",
    rf"Incremental contribution margin is $(56 - 50) \times 0.30 = \text{{USD }}1,800,000$. "
    rf"Incremental bad-debt expense is $(56 \times 0.02 - 50 \times 0.01)\text{{M}} = 1.12\text{{M}} - 0.50\text{{M}} = \text{{USD }}620,000$. "
    rf"Receivables rise from $50\text{{M}}(30/365) = \text{{USD }}{ar0_58:,.0f}$ to $56\text{{M}}(60/365) = \text{{USD }}{ar1_58:,.0f}$, adding $10\% \times \text{{USD }}{ar1_58 - ar0_58:,.0f} = \text{{USD }}{inc_fin_58:,.0f}$ in financing cost: "
    rf"$$\text{{Net Benefit}} = 1,800,000 - 620,000 - {inc_fin_58:,.0f} = \text{{USD }}{net_ben_58:,.0f}$$",
    True,
)

# =============================================================================
# LEVEL 1: MODULE 6 — COST OF CAPITAL (L1-CRP-059 .. 070)
# =============================================================================
M6 = "CI-L1-M6"
T6 = "Cost of Capital"

# L1-CRP-059 (Calc): Standard WACC using target market weights
mv_d_59, mv_p_59, mv_e_59 = 300.0, 100.0, 600.0
tot_mv_59 = mv_d_59 + mv_p_59 + mv_e_59  # 1000
kd_59, t_59, dp_59, pp_59, rf_59, beta_59, erp_59 = 0.06, 0.25, 4.20, 60.0, 0.04, 1.20, 0.055
kp_59 = dp_59 / pp_59                   # 7.0%
ke_59 = rf_59 + beta_59 * erp_59        # 10.6%
wacc_59 = (mv_d_59 / tot_mv_59) * kd_59 * (1 - t_59) + (mv_p_59 / tot_mv_59) * kp_59 + (mv_e_59 / tot_mv_59) * ke_59
wrong_no_tax_d_59 = (mv_d_59 / tot_mv_59) * kd_59 + (mv_p_59 / tot_mv_59) * kp_59 + (mv_e_59 / tot_mv_59) * ke_59
wrong_tax_p_59 = (mv_d_59 / tot_mv_59) * kd_59 * (1 - t_59) + (mv_p_59 / tot_mv_59) * kp_59 * (1 - t_59) + (mv_e_59 / tot_mv_59) * ke_59
add_q1(
    "L1-CRP-059", M6, T6, "Weighted Average Cost of Capital (WACC)",
    "Calculate and interpret a company's weighted average cost of capital.",
    f"An issuer's target capital structure matches its current market values: USD {mv_d_59:.0f}M debt (pre-tax YTM {kd_59*100:.1f}%), USD {mv_p_59:.0f}M perpetual preferred stock (USD {dp_59:.2f} annual dividend trading at USD {pp_59:.2f}), and USD {mv_e_59:.0f}M common equity (beta {beta_59:.2f}). Given a risk-free rate of {rf_59*100:.1f}%, equity risk premium of {erp_59*100:.1f}%, and {t_59*100:.0f}% tax rate, the firm's WACC is closest to:",
    f"{wacc_59*100:.2f}%",
    f"{wrong_no_tax_d_59*100:.2f}%",
    "Uses the pre-tax debt yield (6.0%) instead of the after-tax cost of debt ($6.0\\%(1 - 0.25) = 4.5\\%$).",
    f"{wrong_tax_p_59*100:.2f}%",
    "Erroneously applies the corporate tax shield $(1 - t)$ to preferred stock dividends, which are not tax-deductible.",
    rf"Target weights are $w_d = 0.30$, $w_p = 0.10$, $w_e = 0.60$. Component costs are: "
    rf"$k_d(1-t) = 6.0\%(0.75) = 4.50\%$, $k_p = 4.20 / 60.00 = {kp_59*100:.2f}\%$, and $k_e = 4.0\% + 1.20(5.5\%) = {ke_59*100:.2f}\%$. "
    rf"$$\text{{WACC}} = 0.30(4.50\%) + 0.10(7.00\%) + 0.60(10.60\%) = {wacc_59*100:.2f}\%$$",
    True,
)

# L1-CRP-060 (Calc): Cost of Debt via semi-annual bond YTM
p_bond_60, c_semi_60, par_60, n_semi_60, t_60 = 945.0, 28.0, 1000.0, 10, 0.25
cfs_60 = [-p_bond_60] + [c_semi_60] * (n_semi_60 - 1) + [c_semi_60 + par_60]
ytm_semi_60 = calc_irr(cfs_60)
bey_60 = 2.0 * ytm_semi_60
kd_at_60 = bey_60 * (1.0 - t_60)
wrong_pretax_60 = bey_60
wrong_semi_only_60 = ytm_semi_60 * (1.0 - t_60)
add_q1(
    "L1-CRP-060", M6, T6, "Cost of Debt (YTM Approach)",
    "Compute pre-tax and after-tax cost of debt using bond yield to maturity.",
    f"A firm's 5-year, 5.6% semi-annual coupon non-callable bond (par USD {par_60:,.0f}, paying USD {c_semi_60:.0f} every 6 months) currently trades at USD {p_bond_60:.2f}. With a {t_60*100:.0f}% marginal corporate tax rate, the firm's after-tax cost of debt (on a bond-equivalent yield basis) is closest to:",
    f"{kd_at_60*100:.2f}%",
    f"{wrong_pretax_60*100:.2f}%",
    "Reports the annualized pre-tax YTM without multiplying by $(1 - t)$.",
    f"{wrong_semi_only_60*100:.2f}%",
    "Applies the tax adjustment to the 6-month periodic yield without annualizing by multiplying by 2.",
    rf"Solving the 10-period semi-annual bond equation $-945.00 + \sum_{{t=1}}^{{10}} \frac{{28}}{{(1+y_s)^t}} + \frac{{1,000}}{{(1+y_s)^{{10}}}} = 0$ gives $y_s = {ytm_semi_60*100:.3f}\%$. "
    rf"Annualized pre-tax YTM is $2 \times {ytm_semi_60*100:.3f}\% = {bey_60*100:.2f}\%$, so after-tax cost of debt is: "
    rf"$$k_d(1 - t) = {bey_60*100:.2f}\% \times (1 - {t_60:.2f}) = {kd_at_60*100:.2f}\%$$",
    True,
)

# L1-CRP-061 (Calc): Matrix pricing (debt-rating approach)
m1_61, y1_61, m2_61, y2_61, m_t_61, t_61 = 4.0, 5.40, 10.0, 6.30, 7.0, 0.25
y_interp_61 = y1_61 + ((m_t_61 - m1_61) / (m2_61 - m1_61)) * (y2_61 - y1_61)  # 5.85%
kd_at_61 = y_interp_61 * (1.0 - t_61)
wrong_simple_avg_61 = 0.5 * (y1_61 + y2_61) * (1.0 - t_61) if False else (y1_61 * (1 - t_61))
add_q1(
    "L1-CRP-061", M6, T6, "Debt-Rating Matrix Pricing",
    "Estimate the cost of debt for illiquid bonds using matrix pricing.",
    f"A private firm plans to issue a {m_t_61:.0f}-year A-rated fixed-rate bond. Two actively traded A-rated benchmark bonds yield {y1_61:.2f}% ({m1_61:.0f}-year maturity) and {y2_61:.2f}% ({m2_61:.0f}-year maturity). Using linear matrix pricing interpolation and a {t_61*100:.0f}% tax rate, the estimated after-tax cost of the new bond is closest to:",
    f"{kd_at_61:.2f}%",
    f"{y_interp_61:.2f}%",
    "Interpolates the 7-year pre-tax yield accurately (5.85%) but omits the $(1 - t)$ tax shield adjustment.",
    f"{y2_61*(1-t_61):.2f}%",
    "Uses the 10-year benchmark yield directly instead of interpolating between 4 and 10 years.",
    rf"Linearly interpolating between 4-year ({y1_61:.2f}%) and 10-year ({y2_61:.2f}%) maturities for a 7-year bond (midpoint): "
    rf"$$k_{{d,\text{{pre}}}} = 5.40\% + \frac{{7 - 4}}{{10 - 4}}(6.30\% - 5.40\%) = {y_interp_61:.2f}\%$$ "
    rf"After a {t_61*100:.0f}% tax rate, $k_d(1 - t) = {y_interp_61:.2f}\%(0.75) = {kd_at_61:.2f}\%$.",
    True,
)

# L1-CRP-062 (Calc): Preferred stock cost with flotation
par_p_62, div_rate_62, price_p_62, flot_p_62 = 50.0, 0.065, 45.0, 0.04
dp_62 = par_p_62 * div_rate_62            # 3.25
p_net_62 = price_p_62 * (1.0 - flot_p_62) # 43.20
kp_62 = (dp_62 / p_net_62) * 100.0
wrong_no_flot_62 = (dp_62 / price_p_62) * 100.0
wrong_par_62 = (dp_62 / (par_p_62 * (1.0 - flot_p_62))) * 100.0
add_q1(
    "L1-CRP-062", M6, T6, "Cost of Preferred Stock",
    "Calculate the cost of preferred stock adjusting for issuance flotation costs.",
    f"A utility issues perpetual non-callable {div_rate_62*100:.1f}% preferred shares (USD {par_p_62:.0f} par value) at a market price of USD {price_p_62:.2f}, incurring underwriting flotation costs of {flot_p_62*100:.0f}% of the market offering price. The firm's net cost of preferred equity is closest to:",
    f"{kp_62:.2f}%",
    f"{wrong_no_flot_62:.2f}%",
    "Uses gross market offering price (USD 45.00) rather than net proceeds after 4% flotation costs (USD 43.20).",
    f"{wrong_par_62:.2f}%",
    "Applies the 4% flotation cost to the USD 50.00 par value instead of the USD 45.00 market price.",
    rf"Annual preferred dividend is $\text{{USD }}{par_p_62:.0f} \times {div_rate_62:.3f} = \text{{USD }}{dp_62:.2f}$. "
    rf"Net proceeds per share after flotation costs equal $\text{{USD }}{price_p_62:.2f}(1 - 0.04) = \text{{USD }}{p_net_62:.2f}$: "
    rf"$$k_p = \frac{{D_p}}{{P_{{\text{{net}}}}}} = \frac{{3.25}}{{43.20}} = {kp_62:.2f}\%$$",
    True,
)

# L1-CRP-063 (Calc): CAPM with Country Risk Premium (CRP)
rf_63, beta_63, erp_63, sov_spr_63, sig_eq_63, sig_bd_63 = 0.04, 1.20, 0.055, 0.025, 0.24, 0.15
crp_63 = sov_spr_63 * (sig_eq_63 / sig_bd_63)  # 0.025 * 1.6 = 0.04 (4.0%)
ke_63 = (rf_63 + beta_63 * (erp_63 + crp_63)) * 100.0  # 4 + 1.2*(5.5+4.0) = 15.40%
wrong_unscaled_63 = (rf_63 + beta_63 * (erp_63 + sov_spr_63)) * 100.0
wrong_outside_beta_63 = (rf_63 + beta_63 * erp_63 + crp_63) * 100.0
add_q1(
    "L1-CRP-063", M6, T6, "Country Risk Premium (CRP)",
    "Estimate the cost of equity in emerging markets using the country risk premium adjustment.",
    f"An analyst estimates the cost of equity for a Brazilian manufacturer using a developed-market risk-free rate of {rf_63*100:.1f}%, developed equity risk premium of {erp_63*100:.1f}%, and company beta of {beta_63:.2f}. Brazil's USD-denominated sovereign yield spread is {sov_spr_63*100:.1f}%, its local equity market annualized volatility is {sig_eq_63*100:.0f}%, and its sovereign bond volatility is {sig_bd_63*100:.0f}%. Using the standard CFA beta-adjusted country risk premium model, $k_e$ is closest to:",
    f"{ke_63:.2f}%",
    f"{wrong_unscaled_63:.2f}%",
    "Uses the raw 2.50% sovereign bond spread as CRP without scaling by the relative equity-to-bond volatility ratio ($24\\% / 15\\%$).",
    f"{wrong_outside_beta_63:.2f}%",
    "Adds the scaled 4.00% CRP outside beta rather than multiplying $(\\text{ERP} + \\text{CRP})$ by beta.",
    rf"First compute the Country Risk Premium: "
    rf"$$\text{{CRP}} = 2.50\% \times \frac{{24\%}}{{15\%}} = {crp_63*100:.2f}\%$$ "
    rf"Applying the CFA beta-scaled CAPM with CRP: "
    rf"$$k_e = r_f + \beta(\text{{ERP}} + \text{{CRP}}) = 4.00\% + 1.20(5.50\% + 4.00\%) = {ke_63:.2f}\%$$",
    True,
)

# L1-CRP-064 (Calc): DDM Gordon Growth cost of equity
d0_64, g_64, p0_64 = 2.40, 0.05, 42.00
d1_64 = d0_64 * (1.0 + g_64)  # 2.52
ke_64 = (d1_64 / p0_64 + g_64) * 100.0  # 6% + 5% = 11.00%
wrong_d0_64 = (d0_64 / p0_64 + g_64) * 100.0
wrong_no_g_64 = (d1_64 / p0_64) * 100.0
add_q1(
    "L1-CRP-064", M6, T6, "Dividend Discount Model Cost of Equity",
    "Estimate cost of common equity using the constant-growth dividend discount model.",
    f"A mature utility just paid an annual common dividend ($D_0$) of USD {d0_64:.2f} per share. Dividends are expected to grow indefinitely at {g_64*100:.1f}% per year, and shares trade at USD {p0_64:.2f}. Using the Gordon growth model, the firm's cost of common equity is closest to:",
    f"{ke_64:.2f}%",
    f"{wrong_d0_64:.2f}%",
    "Uses trailing dividend $D_0$ (USD 2.40) instead of next year's expected dividend $D_1 = D_0(1+g)$ (USD 2.52).",
    f"{wrong_no_g_64:.2f}%",
    "Computes only the forward dividend yield ($D_1 / P_0 = 6.00\\%$) and omits the expected 5.0% capital-gains growth term $g$.",
    rf"Next year's expected dividend is $D_1 = 2.40(1.05) = \text{{USD }}{d1_64:.2f}$. Using the Gordon growth identity: "
    rf"$$k_e = \frac{{D_1}}{{P_0}} + g = \frac{{2.52}}{{42.00}} + 0.05 = 6.00\% + 5.00\% = {ke_64:.2f}\%$$",
    True,
)

# L1-CRP-065 (Calc): Bond-Yield-Plus-Risk-Premium + WACC
kd_pre_65, rp_65, wd_65, we_65, t_65 = 0.068, 0.042, 0.35, 0.65, 0.20
ke_65 = kd_pre_65 + rp_65  # 11.0%
wacc_65 = (wd_65 * kd_pre_65 * (1 - t_65) + we_65 * ke_65) * 100.0
wrong_ke_at_65 = (wd_65 * kd_pre_65 * (1 - t_65) + we_65 * (kd_pre_65 * (1 - t_65) + rp_65)) * 100.0
wrong_no_tax_65 = (wd_65 * kd_pre_65 + we_65 * ke_65) * 100.0
add_q1(
    "L1-CRP-065", M6, T6, "Bond-Yield-Plus-Risk-Premium Approach",
    "Estimate cost of equity via the bond-yield-plus-risk-premium method and integrate it into WACC.",
    f"An issuer's long-term debt yields {kd_pre_65*100:.1f}% pre-tax, and analysts estimate its equity risk premium over own debt at {rp_65*100:.1f}%. If target weights are {wd_65*100:.0f}% debt and {we_65*100:.0f}% common equity and the tax rate is {t_65*100:.0f}%, the firm's WACC using the bond-yield-plus-risk-premium approach for $k_e$ is closest to:",
    f"{wacc_65:.2f}%",
    f"{wrong_ke_at_65:.2f}%",
    "Adds the 4.2% risk premium to the after-tax cost of debt rather than the pre-tax bond yield when estimating $k_e$.",
    f"{wrong_no_tax_65:.2f}%",
    "Omits the corporate tax shield $(1 - t)$ on the debt component in WACC.",
    rf"Under the bond-yield-plus-risk-premium method, $k_e = k_{{d,\text{{pre}}}} + \text{{RP}} = 6.80\% + 4.20\% = {ke_65*100:.1f}\%$. "
    rf"After-tax cost of debt is $6.80\%(1 - 0.20) = {kd_pre_65*(1-t_65)*100:.2f}\%$: "
    rf"$$\text{{WACC}} = 0.35({kd_pre_65*(1-t_65)*100:.2f}\%) + 0.65(11.00\%) = {wacc_65:.2f}\%$$",
    True,
)

# L1-CRP-066 (Calc): Flotation costs (CFA dollar outlay adjustment)
i0_66, pv_cf_66, we_66, wd_66, fe_66, fd_66 = 60.0, 64.0, 0.70, 0.30, 0.05, 0.015
flot_cost_66 = i0_66 * (we_66 * fe_66 + wd_66 * fd_66)  # 60 * (0.035 + 0.0045) = 60 * 0.0395 = 2.37M
npv_adj_66 = pv_cf_66 - i0_66 - flot_cost_66            # 64 - 60 - 2.37 = 1.63M
npv_unadj_66 = pv_cf_66 - i0_66
wrong_eq_only_66 = pv_cf_66 - i0_66 - (i0_66 * fe_66)
add_q1(
    "L1-CRP-066", M6, T6, "Flotation Cost Treatment",
    "Apply the recommended CFA adjustment for flotation costs in capital budgeting.",
    f"A firm evaluates an expansion costing USD {i0_66:.0f} million upfront (before issuance fees) whose discounted future operating cash flows have a present value of USD {pv_cf_66:.0f} million at WACC. The project is funded at the firm's target weights of {we_66*100:.0f}% new common equity (flotation fee {fe_66*100:.1f}%) and {wd_66*100:.0f}% new debt (flotation fee {fd_66*100:.1f}%). Applying CFA Institute's recommended treatment of flotation costs, the project's adjusted NPV is closest to:",
    f"USD {npv_adj_66:.2f} million",
    f"USD {npv_unadj_66:.2f} million",
    "Ignores issuance flotation costs entirely, reporting the unadjusted NPV.",
    f"USD {wrong_eq_only_66:.2f} million",
    "Applies the 5.0% equity flotation fee to the entire USD 60M project outlay instead of weighting equity (70%) and debt (30%) fees.",
    rf"Flotation costs represent an upfront Year 0 cash outlay rather than an ongoing WACC increase: "
    rf"$$\text{{Flotation Outlay}} = 60 \times [0.70(0.050) + 0.30(0.015)] = 60(0.0395) = \text{{USD }}{flot_cost_66:.2f}\text{{M}}$$ "
    rf"Adjusted NPV equals $\text{{USD }}64.00\text{{M}} - \text{{USD }}60.00\text{{M}} - \text{{USD }}{flot_cost_66:.2f}\text{{M}} = \text{{USD }}{npv_adj_66:.2f}\text{{ million}}$.",
    True,
)

# L1-CRP-067 (Calc): Marginal Cost of Capital (MCC) Break-Point
re_67, we_67, wd_67, kd_pre1_67, kd_pre2_67, ke_re_67, ke_new_67, t_67 = 45.0, 0.60, 0.40, 0.05, 0.06, 0.10, 0.115, 0.25
bp_eq_67 = re_67 / we_67  # 75.0M
# Suppose debt rises only above 100M total capital, or let's ask for the equity break-point AND WACC above it (with debt unchanged at 5% pre-tax, or specify debt rises above 60M total capital). Let's ask cleanly for equity break-point and WACC just above it when new equity replaces retained earnings.
wacc_below_67 = (wd_67 * kd_pre1_67 * (1 - t_67) + we_67 * ke_re_67) * 100.0
wacc_above_67 = (wd_67 * kd_pre1_67 * (1 - t_67) + we_67 * ke_new_67) * 100.0
wrong_bp_mult_67 = re_67 * we_67
add_q1(
    "L1-CRP-067", M6, T6, "Marginal Cost of Capital Break-Points",
    "Calculate break-points in the marginal cost of capital schedule.",
    f"A company targets {we_67*100:.0f}% common equity and {wd_67*100:.0f}% debt. It expects USD {re_67:.0f} million in retained earnings (cost {ke_re_67*100:.1f}%), after which new common equity costs {ke_new_67*100:.1f}%. Debt costs {kd_pre1_67*100:.1f}% pre-tax across the relevant range (tax rate {t_67*100:.0f}%). The equity capital break-point and the WACC immediately above that break-point are:",
    f"USD {bp_eq_67:.1f} million; WACC = {wacc_above_67:.2f}%",
    f"USD {re_67:.1f} million; WACC = {wacc_above_67:.2f}%",
    "Uses available retained earnings (USD 45M) directly as the total capital break-point without dividing by the 60% equity weight.",
    f"USD {bp_eq_67:.1f} million; WACC = {wacc_below_67:.2f}%",
    "Computes the USD 75.0M break-point accurately but keeps using the 10.0% retained earnings cost instead of the 11.5% new equity cost.",
    rf"The retained-earnings break-point occurs when total new capital exhausts USD 45M at the 60% target equity weight: "
    rf"$$\text{{Break-Point}} = \frac{{\text{{USD }}45\text{{M}}}}{{0.60}} = \text{{USD }}{bp_eq_67:.1f}\text{{ million}}$$ "
    rf"Above USD 75.0M, new equity costs 11.5% while after-tax debt remains $5.0\%(1 - 0.25) = 3.75\%$: "
    rf"$$\text{{WACC}}_{{>75\text{{M}}}} = 0.40(3.75\%) + 0.60(11.50\%) = {wacc_above_67:.2f}\%$$",
    True,
)

# L1-CRP-068 (Calc): Single-peer Hamada unlevering and relevering
beta_peer_68, de_peer_68, t_peer_68 = 1.45, 0.60, 0.25
de_tgt_68, t_tgt_68, rf_68, erp_68 = 0.25, 0.20, 0.035, 0.06
beta_u_68 = beta_peer_68 / (1.0 + (1.0 - t_peer_68) * de_peer_68)  # 1.45 / 1.45 = 1.00
beta_l_68 = beta_u_68 * (1.0 + (1.0 - t_tgt_68) * de_tgt_68)      # 1.00 * 1.20 = 1.20
ke_68 = (rf_68 + beta_l_68 * erp_68) * 100.0
wrong_no_tax_68 = (rf_68 + (beta_peer_68 / (1 + de_peer_68) * (1 + de_tgt_68)) * erp_68) * 100.0
wrong_unrel_68 = (rf_68 + beta_peer_68 * erp_68) * 100.0
add_q1(
    "L1-CRP-068", M6, T6, "Pure-Play Beta Adjustment",
    "Unlever and relever beta using the Hamada equation to estimate a project's cost of equity.",
    f"A pure-play competitor has an equity beta of {beta_peer_68:.2f}, a debt-to-equity ratio of {de_peer_68:.2f}, and a {t_peer_68*100:.0f}% tax rate. An analyst seeks the cost of equity for a private division with a target debt-to-equity ratio of {de_tgt_68:.2f} and a {t_tgt_68*100:.0f}% tax rate. Assuming debt beta is zero, $r_f = {rf_68*100:.1f}\\%$, and $\\text{{ERP}} = {erp_68*100:.1f}\\%$, the division's CAPM cost of equity is closest to:",
    f"{ke_68:.2f}%",
    f"{wrong_no_tax_68:.2f}%",
    "Omits the $(1 - t)$ tax shields when unlevering and relevering beta.",
    f"{wrong_unrel_68:.2f}%",
    "Applies the competitor's levered equity beta (1.45) directly without adjusting for the lower target leverage.",
    rf"Unlever the peer beta: "
    rf"$$\beta_U = \frac{{1.45}}{{1 + (1 - 0.25)(0.60)}} = \frac{{1.45}}{{1.45}} = {beta_u_68:.2f}$$ "
    rf"Relever at the target D/E and tax rate: "
    rf"$$\beta_L = {beta_u_68:.2f}[1 + (1 - 0.20)(0.25)] = {beta_l_68:.2f}$$ "
    rf"CAPM cost of equity is $k_e = 3.50\% + 1.20(6.00\%) = {ke_68:.2f}\%$.",
    True,
)

add_q1(
    "L1-CRP-069", M6, T6, "Capital Structure Weighting",
    "Explain why target market-value weights are preferred over historical book-value weights in WACC.",
    "Why should analysts use target market-value capital weights rather than balance-sheet book-value weights when computing WACC for capital budgeting?",
    "Market-value weights reflect the current opportunity cost and actual proportions in which new capital must be raised today.",
    "Book-value weights fluctuate continuously with daily stock returns, making WACC overly volatile.",
    "Market values—not historical accounting book values—fluctuate daily; historical book values ignore current market valuations of equity.",
    "Book-value weights eliminate the need to adjust debt yields for corporate income taxes.",
    "Regardless of whether book or market weights are used, the tax deductibility of interest requires $(1 - t)$ on debt cost.",
    "WACC measures the marginal cost of raising capital today to fund new investments. Target market-value weights match current economic capital proportions, whereas accounting book values reflect historical issuance and accumulated retained earnings.",
    False,
)

add_q1(
    "L1-CRP-070", M6, T6, "Firm WACC vs Project Risk",
    "Explain the consequences of applying a single corporate-wide WACC to projects with differing systematic risk.",
    "If a diversified conglomerate uses its single company-wide WACC to evaluate every capital project across all divisions without risk adjustment, the firm will systematically:",
    "Overinvest in high-risk divisions (accepting negative-NPV projects) and underinvest in low-risk divisions (rejecting positive-NPV projects).",
    "Overinvest in low-risk divisions and underinvest in high-risk divisions.",
    "Reverses the bias: low-risk divisions face an artificially high hurdle rate and get starved of capital, while high-risk divisions face an artificially low hurdle rate.",
    "Accept only projects whose IRR exceeds the company's unlevered cost of equity.",
    "Using firm WACC compares project IRRs against corporate WACC, not unlevered cost of equity, causing systematic risk-mispricing.",
    "Applying a blended corporate WACC penalizes safer low-beta divisions (rejecting value-adding projects whose returns exceed their true risk-adjusted hurdle rate but fall below corporate WACC) and subsidizes high-beta divisions (accepting value-destroying projects).",
    False,
)

# =============================================================================
# LEVEL 1: MODULE 7 — MEASURES OF LEVERAGE & BREAK-EVEN (L1-CRP-071 .. 080)
# =============================================================================
M7 = "CI-L1-M7"
T7 = "Measures of Leverage & Break-Even"

add_q1(
    "L1-CRP-071", M7, T7, "Business Risk vs Financial Risk",
    "Define and distinguish sales risk, operating risk, business risk, and financial risk.",
    "Business risk consists of two core components, which are best described as:",
    "Sales risk (uncertainty regarding unit volume and selling price) and operating risk (earnings sensitivity from fixed operating costs).",
    "Interest-rate risk and financial leverage risk from issuing senior fixed-coupon bonds.",
    "Risk stemming from fixed debt financing obligations constitutes financial risk, not business risk.",
    "Default risk and equity dilution risk arising from convertible preferred stock.",
    "Both relate to capital structure and financing instruments (financial risk) rather than underlying operating business risk.",
    "Business risk captures uncertainty in operating income (EBIT) before financing decisions: it combines sales risk (volatility of revenues) and operating risk (amplification of EBIT volatility due to fixed operating expenses).",
    False,
)

# L1-CRP-072 (Calc): Degree of Operating Leverage (DOL)
q_72, p_72, v_72, f_72 = 100_000, 65.0, 40.0, 1_500_000.0
cm_tot_72 = q_72 * (p_72 - v_72)        # 2,500,000
ebit_72 = cm_tot_72 - f_72              # 1,000,000
dol_72 = cm_tot_72 / ebit_72            # 2.50x
wrong_rev_ebit_72 = (q_72 * p_72) / ebit_72
wrong_inv_72 = ebit_72 / cm_tot_72
add_q1(
    "L1-CRP-072", M7, T7, "Degree of Operating Leverage (DOL)",
    "Calculate and interpret the degree of operating leverage.",
    f"A manufacturer sells {q_72:,} units at USD {p_72:.0f}/unit with variable operating costs of USD {v_72:.0f}/unit and fixed operating costs of USD {f_72/1e6:.1f} million. At this production level, the firm's Degree of Operating Leverage (DOL) is closest to:",
    f"{dol_72:.2f}x",
    f"{wrong_rev_ebit_72:.2f}x",
    "Uses total revenue (USD 6.5M) in the numerator instead of total contribution margin (USD 2.5M).",
    f"{wrong_inv_72:.2f}x",
    "Inverts the DOL formula ($\\text{EBIT} / \\text{Contribution Margin}$).",
    rf"Total contribution margin is $100,000 \times (65 - 40) = \text{{USD }}2.5\text{{M}}$, and $\text{{EBIT}} = 2.5\text{{M}} - 1.5\text{{M}} = \text{{USD }}1.0\text{{M}}$: "
    rf"$$\text{{DOL}} = \frac{{Q(P - V)}}{{Q(P - V) - F}} = \frac{{2.5\text{{M}}}}{{1.0\text{{M}}}} = {dol_72:.2f}\text{{x}}$$",
    True,
)

# L1-CRP-073 (Calc): DFL with interest and preferred dividends
ebit_73, int_73, dp_73, t_73 = 50.0, 10.0, 6.0, 0.25
# CFA formula when preferred dividends exist: DFL = EBIT / [EBIT - I - D_p/(1-t)] or if no preferred: EBIT/(EBIT - I).
# Wait: using D_p=6 and t=0.25: D_p/(1-t) = 8.0 -> denom = 50 - 10 - 8 = 32 -> DFL = 50/32 = 1.5625
# Let's double check: in standard corporate finance, preferred dividends are paid after tax, so EBT equivalent needed is D_p/(1-t)!
# Let's state cleanly: "assuming the firm pays USD 6.0 million in preferred dividends (pre-tax equivalent = Dp/(1-t))..." OR keep DFL crisp with only Interest OR state preferred formula! Actually let's check: does CFA L1 include preferred dividends in DFL? Yes, or interest-only. Even simpler and 100% standard: interest-only in L1-CRP-073 or explicitly note preferred dividends! Let's include interest AND preferred dividends with clean explanation, OR check: if D_p = 0, no ambiguity at all? Wait: testing D_p/(1-t) or interest-only — let's make D_p = 0 here so there's zero ambiguity across textbooks, and test DFL = EBIT / (EBIT - I) cleanly! Wait: what if we test D_p = 0 and make EBIT=40M, I=8M -> DFL = 40/32 = 1.25x, OR test preferred dividends? Let's check: CFA Level I curriculum explicitly defines DFL = EBIT / (EBIT - I) (ignoring preferred) in recent readings, whereas older readings included D_p/(1-t). Using D_p = 0 guarantees 100% consistency across every CFA edition!
ebit_73, int_73, t_73 = 48.0, 12.0, 0.25
dfl_73 = ebit_73 / (ebit_73 - int_73)  # 48 / 36 = 1.3333
wrong_at_int_73 = ebit_73 / (ebit_73 - int_73 * (1 - t_73))
wrong_rev_73 = (ebit_73 - int_73) / ebit_73
add_q1(
    "L1-CRP-073", M7, T7, "Degree of Financial Leverage (DFL)",
    "Calculate and interpret the degree of financial leverage.",
    f"A firm with no preferred stock reports EBIT of USD {ebit_73:.0f} million, annual interest expense of USD {int_73:.0f} million, and a {t_73*100:.0f}% corporate tax rate. Its Degree of Financial Leverage (DFL) is closest to:",
    f"{dfl_73:.2f}x",
    f"{wrong_at_int_73:.2f}x",
    "Subtracts after-tax interest ($I(1-t) = 9\\text{M}$) from EBIT rather than pre-tax interest ($I = 12\\text{M}$), understating financial leverage.",
    f"{wrong_rev_73:.2f}x",
    "Inverts the DFL ratio ($\\text{EBT} / \\text{EBIT}$).",
    rf"With zero preferred dividends, the Degree of Financial Leverage measures the elasticity of net income (and EPS) to changes in EBIT: "
    rf"$$\text{{DFL}} = \frac{{\text{{EBIT}}}}{{\text{{EBIT}} - I}} = \frac{{48}}{{48 - 12}} = {dfl_73:.2f}\text{{x}}$$ "
    r"(Because the tax factor $(1 - t)$ cancels out in numerator and denominator of $\%\Delta \text{NI} / \%\Delta \text{EBIT}$, pre-tax interest is subtracted from EBIT.)",
    True,
)

# L1-CRP-074 (Calc): DTL and EPS forecast
dol_74, dfl_74, eps0_74, dq_pct_74 = 2.20, 1.50, 3.00, 0.10
dtl_74 = dol_74 * dfl_74  # 3.30
eps1_74 = eps0_74 * (1.0 + dtl_74 * dq_pct_74)  # 3.00 * 1.33 = 3.99
wrong_add_74 = eps0_74 * (1.0 + (dol_74 + dfl_74) * dq_pct_74)
wrong_dol_only_74 = eps0_74 * (1.0 + dol_74 * dq_pct_74)
add_q1(
    "L1-CRP-074", M7, T7, "Degree of Total Leverage (DTL)",
    "Combine DOL and DFL to compute DTL and project EPS changes from sales growth.",
    f"A retailer currently generates EPS of USD {eps0_74:.2f} with a Degree of Operating Leverage (DOL) of {dol_74:.2f}x and a Degree of Financial Leverage (DFL) of {dfl_74:.2f}x. If unit sales volume increases by {dq_pct_74*100:.0f}% (with fixed price and unit cost structure), projected EPS is closest to:",
    f"USD {eps1_74:.2f}",
    f"USD {wrong_add_74:.2f}",
    "Adds DOL and DFL ($2.20 + 1.50 = 3.70$) instead of multiplying them to obtain DTL.",
    f"USD {wrong_dol_only_74:.2f}",
    "Applies only operating leverage (DOL) to forecast EPS, omitting financial leverage amplification.",
    rf"Degree of Total Leverage equals the product of operating and financial leverage: "
    rf"$$\text{{DTL}} = \text{{DOL}} \times \text{{DFL}} = 2.20 \times 1.50 = {dtl_74:.2f}\text{{x}}$$ "
    rf"A 10% unit sales increase raises EPS by $3.30 \times 10\% = 33.0\%$: "
    rf"$$\text{{EPS}}_1 = \text{{USD }}{eps0_74:.2f} \times (1 + 0.33) = \text{{USD }}{eps1_74:.2f}$$",
    True,
)

# L1-CRP-075 (Calc): Operating Break-Even Quantity (Q_OBE)
p_75, v_75, f_75, int_75 = 120.0, 75.0, 1_800_000.0, 450_000.0
q_obe_75 = f_75 / (p_75 - v_75)             # 40,000 units
q_tbe_75 = (f_75 + int_75) / (p_75 - v_75)  # 50,000 units
wrong_price_75 = f_75 / p_75
add_q1(
    "L1-CRP-075", M7, T7, "Operating Break-Even Volume",
    "Calculate operating break-even quantity and revenue.",
    f"A product sells for USD {p_75:.0f}/unit with variable cost of USD {v_75:.0f}/unit, fixed operating costs of USD {f_75/1e6:.1f} million, and annual interest expense of USD {int_75/1e3:.0f} thousand. The firm's operating break-even quantity ($Q_{{\\text{{OBE}}}}$) is:",
    f"{q_obe_75:,.0f} units",
    f"{q_tbe_75:,.0f} units",
    "Includes fixed financing interest (USD 450,000), which yields total net-income break-even ($Q_{\\text{BE}}$) rather than operating break-even ($Q_{\\text{OBE}}$).",
    f"{wrong_price_75:,.0f} units",
    "Divides fixed operating costs by selling price (USD 120) instead of unit contribution margin (USD 45).",
    rf"Operating break-even ($Q_{{\text{{OBE}}}}$) is the sales volume at which $\text{{EBIT}} = 0$ (covering fixed operating costs excluding interest): "
    rf"$$Q_{{\text{{OBE}}}} = \frac{{F}}{{P - V}} = \frac{{1,800,000}}{{120 - 75}} = {q_obe_75:,.0f}\text{{ units}}$$",
    True,
)

# L1-CRP-076 (Calc): Total Break-Even Quantity (Q_BE)
p_76, v_76, f_76, int_76 = 80.0, 50.0, 1_200_000.0, 300_000.0
q_be_76 = (f_76 + int_76) / (p_76 - v_76)  # 50,000 units
q_obe_76 = f_76 / (p_76 - v_76)             # 40,000 units
wrong_var_76 = (f_76 + int_76) / v_76
add_q1(
    "L1-CRP-076", M7, T7, "Total Break-Even Quantity",
    "Calculate total break-even quantity incorporating both operating and financing fixed costs.",
    f"A specialty equipment producer sells units at USD {p_76:.0f} with variable cost of USD {v_76:.0f}/unit, fixed operating costs of USD {f_76/1e6:.1f} million, and annual interest expense of USD {int_76/1e3:.0f} thousand. The total break-even quantity ($Q_{{\\text{{BE}}}}$) at which net income equals zero is:",
    f"{q_be_76:,.0f} units",
    f"{q_obe_76:,.0f} units",
    "Omits the USD 300,000 fixed interest expense, calculating operating break-even ($Q_{\\text{OBE}}$) instead of total break-even ($Q_{\\text{BE}}$).",
    f"{wrong_var_76:,.0f} units",
    "Divides total fixed costs by variable unit cost (USD 50) instead of contribution margin (USD 30).",
    rf"Total break-even quantity covers both fixed operating costs ($F$) and fixed financial costs ($I$): "
    rf"$$Q_{{\text{{BE}}}} = \frac{{F + I}}{{P - V}} = \frac{{1,200,000 + 300,000}}{{80 - 50}} = {q_be_76:,.0f}\text{{ units}}$$",
    True,
)

# L1-CRP-077 (Calc): Cash Operating Break-Even Quantity
p_77, v_77, f_tot_77, depr_77 = 150.0, 90.0, 2_400_000.0, 600_000.0
q_cash_77 = (f_tot_77 - depr_77) / (p_77 - v_77)  # 1.8M / 60 = 30,000
q_acc_77 = f_tot_77 / (p_77 - v_77)               # 2.4M / 60 = 40,000
wrong_add_77 = (f_tot_77 + depr_77) / (p_77 - v_77)
add_q1(
    "L1-CRP-077", M7, T7, "Cash Break-Even Analysis",
    "Determine cash operating break-even volume excluding non-cash depreciation.",
    rf"A factory sells output for USD {p_77:.0f}/unit with variable cost of USD {v_77:.0f}/unit and total fixed operating costs of USD {f_tot_77/1e6:.1f} million, which includes USD {depr_77/1e3:.0f} thousand of non-cash depreciation. Ignoring interest and taxes, the unit sales volume required to achieve cash operating break-even ($\text{{EBITDA}} = 0$) is:",
    f"{q_cash_77:,.0f} units",
    f"{q_acc_77:,.0f} units",
    "Includes non-cash depreciation in the numerator, yielding accounting EBIT break-even rather than cash EBITDA break-even.",
    f"{wrong_add_77:,.0f} units",
    "Adds non-cash depreciation to total fixed costs instead of subtracting it.",
    rf"Cash fixed operating costs equal total fixed costs minus non-cash depreciation: $2,400,000 - 600,000 = \text{{USD }}1,800,000$. "
    rf"$$Q_{{\text{{cash}}}} = \frac{{F - \text{{Depreciation}}}}{{P - V}} = \frac{{1,800,000}}{{150 - 90}} = {q_cash_77:,.0f}\text{{ units}}$$",
    True,
)

# L1-CRP-078 (Calc): Technology crossover volume (EBIT indifference)
p_78 = 100.0
f_auto_78, v_auto_78 = 3_000_000.0, 40.0   # CM = 60
f_man_78, v_man_78 = 1_200_000.0, 70.0     # CM = 30
# Q*(60) - 3.0M = Q*(30) - 1.2M -> 30*Q = 1.8M -> Q = 60,000
q_indiff_78 = (f_auto_78 - f_man_78) / ((p_78 - v_auto_78) - (p_78 - v_man_78))
wrong_sum_78 = (f_auto_78 + f_man_78) / ((p_78 - v_auto_78) + (p_78 - v_man_78))
wrong_be_auto_78 = f_auto_78 / (p_78 - v_auto_78)
add_q1(
    "L1-CRP-078", M7, T7, "Operating Cost Structure Trade-Offs",
    "Compute the indifference unit volume between high-fixed-cost and low-fixed-cost production technologies.",
    f"Both options sell widgets at USD {p_78:.0f}/unit. Automated Line A requires USD {f_auto_78/1e6:.1f}M in annual fixed costs and USD {v_auto_78:.0f}/unit variable cost; Manual Line B requires USD {f_man_78/1e6:.1f}M in annual fixed costs and USD {v_man_78:.0f}/unit variable cost. At what annual unit volume do both production lines earn identical EBIT?",
    f"{q_indiff_78:,.0f} units",
    f"{wrong_be_auto_78:,.0f} units",
    r"Computes Automated Line A's standalone operating break-even volume ($\text{EBIT} = 0$) instead of the cross-over volume between Line A and Line B.",
    f"{wrong_sum_78:,.0f} units",
    "Adds fixed costs and adds contribution margins instead of equating the two EBIT functions.",
    rf"Equating $\text{{EBIT}}_A = \text{{EBIT}}_B$: "
    rf"$$Q(100 - 40) - 3,000,000 = Q(100 - 70) - 1,200,000 \implies 30Q = 1,800,000 \implies Q = {q_indiff_78:,.0f}\text{{ units}}$$ "
    rf"At {q_indiff_78:,.0f} units, both lines generate $\text{{EBIT}} = \text{{USD }}600,000$; above 60,000 units, Automated Line A earns higher EBIT.",
    True,
)

# L1-CRP-079 (Calc): Solving backward from DTL and DOL for interest expense
cm_tot_79, f_79, dtl_79 = 60.0, 20.0, 2.0
ebit_79 = cm_tot_79 - f_79                 # 40M
dol_79 = cm_tot_79 / ebit_79               # 1.50x
# DTL = CM / (EBIT - I) -> 2.0 = 60 / (40 - I) -> 40 - I = 30 -> I = 10M
int_79 = ebit_79 - (cm_tot_79 / dtl_79)    # 10.0M
wrong_ebit_79 = ebit_79 / dtl_79           # 20.0M
wrong_cm_div_79 = cm_tot_79 / dtl_79       # 30.0M
add_q1(
    "L1-CRP-079", M7, T7, "Decomposing Total Leverage",
    "Infer underlying fixed financing charges from contribution margin, fixed operating costs, and DTL.",
    f"A firm with zero preferred stock generates USD {cm_tot_79:.0f} million in total contribution margin, incurs USD {f_79:.0f} million in fixed operating costs, and operates with a Degree of Total Leverage (DTL) of {dtl_79:.1f}x. Its annual interest expense is closest to:",
    f"USD {int_79:.1f} million",
    f"USD {wrong_ebit_79:.1f} million",
    "Solves $\\text{DFL} = \\text{DTL}$ directly ($\\text{EBIT} / (\\text{EBIT} - I) = 2.0$), overlooking that DOL already accounts for $1.50\\times$ leverage.",
    f"USD {wrong_cm_div_79:.1f} million",
    "Solves for EBT ($\\text{EBIT} - I = 30\\text{M}$) rather than subtracting EBT from EBIT to isolate interest expense $I$.",
    rf"First compute $\text{{EBIT}} = 60 - 20 = \text{{USD }}{ebit_79:.0f}\text{{M}}$, so $\text{{DOL}} = 60 / 40 = {dol_79:.2f}\text{{x}}$. "
    rf"Since $\text{{DTL}} = \frac{{Q(P - V)}}{{\text{{EBIT}} - I}}$: "
    rf"$$2.0 = \frac{{60}}{{40 - I}} \implies 40 - I = 30 \implies I = \text{{USD }}{int_79:.1f}\text{{ million}}$$",
    True,
)

# L1-CRP-080 (Calc): EPS sensitivity to 20% revenue decline (All-Equity vs 50% Debt)
# Invested capital = 100M, price/share = 10 -> All-equity: 10M shares, EBIT = 20M, F=10M, CM=30M (DOL=1.5). Tax=25%.
# 50% Debt: 50M debt at 8% (I=4M), 5M shares.
# Revenue drops 20% -> CM drops 20% (from 30M to 24M) -> EBIT drops from 20M to 14M (-30%).
# All-Equity EPS0 = 20*(0.75)/10 = 1.50 -> EPS1 = 14*(0.75)/10 = 1.05 (-30.0%)
# Levered EPS0 = (20-4)*(0.75)/5 = 2.40 -> EPS1 = (14-4)*(0.75)/5 = 1.50 (-37.5%)
cm0_80, f_80, d_lev_80, kd_80, sh_u_80, sh_l_80, t_80, drop_80 = 30.0, 10.0, 50.0, 0.08, 10.0, 5.0, 0.25, 0.20
ebit0_80 = cm0_80 - f_80                  # 20.0M
ebit1_80 = cm0_80 * (1 - drop_80) - f_80  # 14.0M
int_80 = d_lev_80 * kd_80                 # 4.0M
eps_u0_80 = ebit0_80 * (1 - t_80) / sh_u_80
eps_u1_80 = ebit1_80 * (1 - t_80) / sh_u_80
pct_u_80 = (eps_u1_80 - eps_u0_80) / eps_u0_80 * 100.0  # -30.0%
eps_l0_80 = (ebit0_80 - int_80) * (1 - t_80) / sh_l_80
eps_l1_80 = (ebit1_80 - int_80) * (1 - t_80) / sh_l_80
pct_l_80 = (eps_l1_80 - eps_l0_80) / eps_l0_80 * 100.0  # -37.5%
add_q1(
    "L1-CRP-080", M7, T7, "Financial Leverage & Downside EPS Risk",
    "Quantify how replacing equity with debt amplifies downside EPS volatility.",
    f"A firm with USD 100 million in assets generates USD {cm0_80:.0f}M contribution margin and USD {f_80:.0f}M fixed operating costs (EBIT = USD {ebit0_80:.0f}M, tax rate {t_80*100:.0f}%). Under Plan U (all-equity: 10M shares), debt is zero. Under Plan L (levered: USD {d_lev_80:.0f}M debt at {kd_80*100:.0f}%, 5M shares), interest is USD {int_80:.0f}M. If revenue drops {drop_80*100:.0f}% (reducing contribution margin {drop_80*100:.0f}%), the percentage decline in EPS under Plan L versus Plan U is:",
    f"Plan L: {abs(pct_l_80):.1f}% decline; Plan U: {abs(pct_u_80):.1f}% decline",
    f"Plan L: {abs(pct_u_80):.1f}% decline; Plan U: {abs(pct_l_80):.1f}% decline",
    "Reverses the two plans, failing to recognize that interest expense magnifies EPS declines under Plan L.",
    f"Plan L: {drop_80*100:.1f}% decline; Plan U: {drop_80*100:.1f}% decline",
    "Assumes EPS falls in exact 1-to-1 proportion with the 20% revenue decline under both structures.",
    rf"A 20% revenue drop lowers contribution margin from USD 30M to USD 24M, reducing EBIT from USD 20M to USD 14M ($-30.0\%$, $\text{{DOL}} = 1.50$). "
    rf"Under Plan U ($\text{{DFL}} = 1.0$), EPS falls by {abs(pct_u_80):.1f}% (from USD {eps_u0_80:.2f} to USD {eps_u1_80:.2f}). "
    rf"Under Plan L ($\text{{DFL}} = 20 / (20 - 4) = 1.25$), EBT drops from USD 16M to USD 10M, driving a {abs(pct_l_80):.1f}% EPS drop (from USD {eps_l0_80:.2f} to USD {eps_l1_80:.2f}).",
    True,
)

# =============================================================================
# LEVEL 2: VIGNETTE 1 — PURE-PLAY HAMADA BETA & DIVISIONAL WACC (CRP-V01)
# =============================================================================
V1_ID = "CRP-V01"
V1_MOD = "CI-L2-M1"
V1_TOP = "Cost of Capital & Divisional Hurdle Rates"
V1_SUB = "Pure-Play Hamada Method & Divisional WACC"
V1_TITLE = "Vanguard Conglomerate Inc. — Divisional WACC Evaluation"

p1_bl, p1_de, p1_t = 1.54, 0.50, 0.20  # beta_u = 1.10
p2_bl, p2_de, p2_t = 1.92, 0.80, 0.25  # beta_u = 1.20
p3_bl, p3_de, p3_t = 1.56, 0.25, 0.20  # beta_u = 1.30
bu1 = p1_bl / (1.0 + (1.0 - p1_t) * p1_de)
bu2 = p2_bl / (1.0 + (1.0 - p2_t) * p2_de)
bu3 = p3_bl / (1.0 + (1.0 - p3_t) * p3_de)
bu_avg = (bu1 + bu2 + bu3) / 3.0       # 1.20

v1_de, v1_t, v1_rf, v1_erp, v1_kd_pre = 0.40, 0.25, 0.04, 0.055, 0.06
v1_corp_wacc = 0.08
v1_bl = bu_avg * (1.0 + (1.0 - v1_t) * v1_de)  # 1.20 * 1.30 = 1.56
v1_ke = v1_rf + v1_bl * v1_erp                  # 12.58%
v1_wd = v1_de / (1.0 + v1_de)
v1_we = 1.0 / (1.0 + v1_de)
v1_wacc = v1_wd * v1_kd_pre * (1.0 - v1_t) + v1_we * v1_ke  # ~10.2714%

v1_capex, v1_ocf, v1_yrs = 100.0, 31.0, 4
v1_npv_div = -v1_capex + v1_ocf * sum(1.0 / ((1.0 + v1_wacc) ** t) for t in range(1, v1_yrs + 1))
v1_npv_corp = -v1_capex + v1_ocf * sum(1.0 / ((1.0 + v1_corp_wacc) ** t) for t in range(1, v1_yrs + 1))

V1_TEXT = (
    "Vanguard Conglomerate Inc. is evaluating capital allocation for its newly formed Robotics Automation division. "
    "Vanguard's existing corporate-wide WACC is 8.00%, driven largely by its mature, low-beta consumer utilities segment. "
    "To estimate the Robotics division's standalone cost of capital, CFO Maya Lin gathers market data on three pure-play "
    "public robotics firms (assuming debt beta equals zero for all firms):\n\n"
    "| Pure-Play Peer | Levered Equity Beta ($\\beta_L$) | Debt-to-Equity ($D/E$) | Marginal Tax Rate |\n"
    "| :--- | :---: | :---: | :---: |\n"
    "| RoboCore Systems | 1.54 | 0.50 | 20% |\n"
    "| Kinetic Automation | 1.92 | 0.80 | 25% |\n"
    "| Precision Mechatronics | 1.56 | 0.25 | 20% |\n\n"
    "Vanguard's Robotics division will maintain a target debt-to-equity ratio ($D/E$) of 0.40, face a 25% corporate tax rate, "
    "and borrow at a 6.00% pre-tax cost of debt. Capital market assumptions include a 4.00% risk-free rate and a 5.50% equity risk premium (ERP). "
    "The division's flagship capital proposal requires a USD 100.0 million upfront outlay and generates USD 31.0 million in annual "
    "after-tax operating cash flows for 4 years (zero terminal salvage)."
)

# Q1: Average unlevered asset beta
wrong_avg_bl_v1 = (p1_bl + p2_bl + p3_bl) / 3.0
wrong_no_tax_bu_v1 = (p1_bl / (1 + p1_de) + p2_bl / (1 + p2_de) + p3_bl / (1 + p3_de)) / 3.0
add_q2(
    "L2-CRP-V01-Q1", V1_MOD, V1_TOP, V1_SUB, V1_ID, V1_TITLE, V1_TEXT,
    "Unlever peer equity betas using the Hamada model to estimate industry asset beta.",
    "Based on the pure-play peer group, the equal-weighted average unlevered asset beta ($\\beta_U$) for the robotics industry is closest to:",
    f"{bu_avg:.2f}",
    f"{wrong_avg_bl_v1:.2f}",
    "Averages the peers' levered equity betas directly without unlevering for financial leverage.",
    f"{wrong_no_tax_bu_v1:.2f}",
    "Omits the $(1 - t)$ corporate tax shields when unlevering the three peer betas.",
    rf"Applying the Hamada unlevering formula $\beta_U = \frac{{\beta_L}}{{1 + (1 - t)(D/E)}}$ to each peer: "
    rf"RoboCore $= 1.54 / [1 + 0.80(0.50)] = {bu1:.2f}$; Kinetic $= 1.92 / [1 + 0.75(0.80)] = {bu2:.2f}$; Precision $= 1.56 / [1 + 0.80(0.25)] = {bu3:.2f}$. "
    rf"The equal-weighted average asset beta is $(1.10 + 1.20 + 1.30)/3 = {bu_avg:.2f}$.",
    True,
)

# Q2: Relevered beta & divisional cost of equity
wrong_no_tax_ke_v1 = (v1_rf + (bu_avg * (1 + v1_de)) * v1_erp) * 100.0
wrong_unrel_ke_v1 = (v1_rf + bu_avg * v1_erp) * 100.0
add_q2(
    "L2-CRP-V01-Q2", V1_MOD, V1_TOP, V1_SUB, V1_ID, V1_TITLE, V1_TEXT,
    "Relever asset beta to target capital structure and estimate divisional cost of equity.",
    "Using the industry average asset beta of 1.20, the Robotics division's relevered equity beta and CAPM cost of equity ($k_e$) are closest to:",
    f"Relevered beta = {v1_bl:.2f}; Cost of equity = {v1_ke*100:.2f}%",
    f"Relevered beta = {bu_avg*(1+v1_de):.2f}; Cost of equity = {wrong_no_tax_ke_v1:.2f}%",
    "Omits the 25% corporate tax shield when relevering beta ($1.20 \\times 1.40 = 1.68$).",
    f"Relevered beta = {bu_avg:.2f}; Cost of equity = {wrong_unrel_ke_v1:.2f}%",
    "Uses the unlevered asset beta (1.20) in CAPM without relevering for the division's 0.40 target D/E ratio.",
    rf"Relevering the asset beta at target $D/E = 0.40$ and $t = 25\%$: "
    rf"$$\beta_L = 1.20[1 + (1 - 0.25)(0.40)] = 1.20(1.30) = {v1_bl:.2f}$$ "
    rf"Applying CAPM: $k_e = 4.00\% + 1.56(5.50\%) = {v1_ke*100:.2f}\%$.",
    True,
)

# Q3: Divisional WACC
wrong_de_wt_wacc_v1 = (v1_de * v1_kd_pre * (1 - v1_t) + (1 - v1_de) * v1_ke) * 100.0
wrong_pretax_wacc_v1 = (v1_wd * v1_kd_pre + v1_we * v1_ke) * 100.0
add_q2(
    "L2-CRP-V01-Q3", V1_MOD, V1_TOP, V1_SUB, V1_ID, V1_TITLE, V1_TEXT,
    "Compute project-specific divisional WACC from target debt-to-equity weights.",
    "The Robotics division's standalone after-tax WACC is closest to:",
    f"{v1_wacc*100:.2f}%",
    f"{wrong_de_wt_wacc_v1:.2f}%",
    "Treats the 0.40 $D/E$ ratio directly as a 40% debt weight ($D/V$) instead of converting $D/E$ into $w_d = 0.40/1.40 = 28.57\\%$.",
    f"{wrong_pretax_wacc_v1:.2f}%",
    "Uses target weights properly but omits the $(1 - t)$ tax adjustment on the 6.00% debt yield.",
    rf"Convert $D/E = 0.40$ to capital weights: $w_d = \frac{{0.40}}{{1.40}} = {v1_wd*100:.2f}\%$ and $w_e = \frac{{1.00}}{{1.40}} = {v1_we*100:.2f}\%$. "
    rf"After-tax cost of debt is $6.00\%(1 - 0.25) = 4.50\%$: "
    rf"$$\text{{WACC}}_{{\text{{div}}}} = \frac{{0.40}}{{1.40}}(4.50\%) + \frac{{1.00}}{{1.40}}(12.58\%) = {v1_wacc*100:.2f}\%$$",
    True,
)

# Q4: Project NPV at divisional WACC vs corporate WACC
add_q2(
    "L2-CRP-V01-Q4", V1_MOD, V1_TOP, V1_SUB, V1_ID, V1_TITLE, V1_TEXT,
    "Evaluate capital projects using divisional WACC rather than corporate WACC.",
    "Evaluating the flagship Robotics proposal at its standalone divisional WACC versus Vanguard's 8.00% corporate WACC yields a divisional NPV closest to:",
    f"USD {v1_npv_div:.2f} million (Reject, whereas corporate WACC gives +USD {v1_npv_corp:.2f} million)",
    f"USD {v1_npv_corp:.2f} million (Accept, matching corporate WACC evaluation)",
    "Erroneously evaluates the high-beta Robotics cash flows at the 8.00% corporate WACC.",
    f"USD {(v1_ocf*4 - v1_capex):.2f} million (Accept based on undiscounted cash flows)",
    "Sums the 4 years of USD 31.0M inflows without discounting at the divisional WACC.",
    rf"At the true divisional WACC of ${v1_wacc*100:.2f}\%$: "
    rf"$$\text{{NPV}}_{{\text{{div}}}} = -100 + \sum_{{t=1}}^{{4}} \frac{{31.0}}{{1.102714^t}} = \text{{USD }}{v1_npv_div:.2f}\text{{ million}}$$ "
    rf"Because $\text{{NPV}}_{{\text{{div}}}} < 0$, the project destroys value and must be rejected—even though applying Vanguard's 8.00% corporate WACC produces a misleading $+\text{{USD }}{v1_npv_corp:.2f}\text{{ million}}$ NPV.",
    True,
)

# Q5: Conceptual
add_q2(
    "L2-CRP-V01-Q5", V1_MOD, V1_TOP, V1_SUB, V1_ID, V1_TITLE, V1_TEXT,
    "Explain capital allocation distortions arising from ignoring divisional risk differences.",
    "If CFO Maya Lin ignores the pure-play analysis and mandates Vanguard's 8.00% corporate WACC across all operating segments, over time Vanguard's firm-wide asset beta will most likely:",
    "Drift upward as high-risk divisions win excessive capital allocations while low-risk utility projects are starved.",
    "Drift downward because low-risk utility projects earn higher accounting returns on book assets.",
    "Low-risk projects have true required returns below 8.00% and will be systematically rejected, shrinking the low-beta asset base.",
    "Remain unchanged because positive and negative NPV estimation errors cancel out symmetrically across divisions.",
    "Errors do not cancel: high-risk negative-NPV projects pass the artificially low 8% hurdle while safe positive-NPV projects fail it, steadily tilting the firm toward riskier assets.",
    "Using a single corporate hurdle rate subsidizes higher-beta divisions (causing overinvestment in riskier projects) and penalizes lower-beta divisions (causing underinvestment in safe projects), shifting Vanguard's business mix toward higher systematic risk.",
    False,
)

# =============================================================================
# LEVEL 2: VIGNETTE 2 — MM PROPOSITIONS I & II (NO TAXES) (CRP-V02)
# =============================================================================
V2_ID = "CRP-V02"
V2_MOD = "CI-L2-M2"
V2_TOP = "Capital Structure Theory"
V2_SUB = "Modigliani-Miller Propositions I & II (No Taxes)"
V2_TITLE = "Helios Solar Systems — Tax-Free Capital Structure Arbitrage"

v2_ebit, v2_r0, v2_rd, v2_d = 45.0, 0.09, 0.05, 200.0
v2_vu = v2_ebit / v2_r0              # 500.0M
v2_e_eq = v2_vu - v2_d               # 300.0M
v2_sh_l = 6.0                        # 6M shares -> eq price = 50.00
v2_p_mkt = 53.0                      # market price 53 -> E_mkt = 318M
v2_e_mkt = v2_sh_l * v2_p_mkt        # 318M
v2_arb_1pct = 0.01 * (v2_e_mkt - v2_e_eq)  # 0.18M = 180,000 USD
v2_re_eq = v2_r0 + (v2_r0 - v2_rd) * (v2_d / v2_e_eq)  # 9 + 4*(2/3) = 11.67%
v2_d2 = 300.0
v2_e2 = v2_vu - v2_d2                # 200.0M -> D/E = 1.50
v2_re2 = v2_r0 + (v2_r0 - v2_rd) * (v2_d2 / v2_e2)  # 9 + 4*(1.5) = 15.00%
v2_stake_hl = 0.05
v2_hl_loan = v2_stake_hl * v2_d      # 10.0M
v2_hl_gross_u = v2_stake_hl * v2_vu  # 25.0M

V2_TEXT = (
    "Helios Solar Systems (Unlevered, Firm U) and Borealis Solar Corp. (Levered, Firm L) operate in a tax-free jurisdiction "
    "(0% corporate and personal taxes) with frictionless capital markets. Both firms own identical generating assets producing "
    "perpetual annual EBIT of USD 45.0 million. Firm U is 100% equity-financed (10.0 million shares trading at USD 50.00/share, "
    "yielding an unlevered cost of capital $r_0 = 9.00\\%$). Firm L carries USD 200.0 million in perpetual risk-free debt "
    "yielding $r_d = 5.00\\%$ (annual interest USD 10.0 million) and has 6.0 million common shares outstanding, which momentarily "
    "trade at USD 53.00/share prior to arbitrage."
)

# Q1: MM Prop I & Arbitrage Profit
add_q2(
    "L2-CRP-V02-Q1", V2_MOD, V2_TOP, V2_SUB, V2_ID, V2_TITLE, V2_TEXT,
    "Apply Modigliani-Miller Proposition I (no taxes) and homemade leverage to identify arbitrage profits.",
    "Under MM Proposition I (no taxes), what is the equilibrium market value of Firm L's equity, and what immediate Year 0 riskless arbitrage profit is earned by shorting 1% of Firm L's overvalued shares while replicating their payoff via Firm U and personal debt?",
    f"Equilibrium equity = USD {v2_e_eq:.0f}M; Year 0 arbitrage profit = USD {v2_arb_1pct*1e3:,.0f}",
    f"Equilibrium equity = USD {v2_vu:.0f}M; Year 0 arbitrage profit = USD 0",
    "Mistakes Firm L's total enterprise value (USD 500M) for its equilibrium equity value after debt.",
    f"Equilibrium equity = USD {v2_e_eq:.0f}M; Year 0 arbitrage profit = USD {0.01*v2_e_mkt*1e3:,.0f}",
    "Reports the gross short-sale proceeds (USD 3.18M) rather than the net Year 0 arbitrage profit after funding the USD 3.00M replicating portfolio.",
    rf"Since $\text{{EBIT}} = \text{{USD }}45\text{{M}}$ and $r_0 = 9\%$, $V_U = 45 / 0.09 = \text{{USD }}500\text{{M}}$. By MM Proposition I without taxes, $V_L = V_U = \text{{USD }}500\text{{M}}$, so equilibrium equity $E_L = 500 - 200 = \text{{USD }}{v2_e_eq:.0f}\text{{M}}$. "
    rf"At USD 53/share, $E_{{L,\text{{mkt}}}} = 6 \times 53 = \text{{USD }}318\text{{M}}$ (USD 18M overvalued). Shorting 1% of Firm L equity yields +USD 3.18M (owing USD 0.35M/yr). Buying 1% of Firm U (USD 5.00M) financed with a USD 2.00M personal loan at 5% costs USD 3.00M net and pays $0.45 - 0.10 = \text{{USD }}0.35\text{{M/yr}}$, locking in a riskless Year 0 arbitrage profit of $3.18\text{{M}} - 3.00\text{{M}} = \text{{USD }}{v2_arb_1pct*1e3:,.0f}$.",
    True,
)

# Q2: MM Prop II at equilibrium (D=200, E=300)
wrong_no_spread_v2 = (v2_r0 + v2_r0 * (v2_d / v2_e_eq)) * 100.0
wrong_w_wt_v2 = (v2_r0 + (v2_r0 - v2_rd) * (v2_d / v2_vu)) * 100.0
add_q2(
    "L2-CRP-V02-Q2", V2_MOD, V2_TOP, V2_SUB, V2_ID, V2_TITLE, V2_TEXT,
    "Calculate cost of equity under Modigliani-Miller Proposition II without taxes.",
    "At Firm L's equilibrium capital structure ($D = \\text{USD }200\\text{M}$, $E = \\text{USD }300\\text{M}$), Firm L's cost of equity ($r_e$) under MM Proposition II (no taxes) is closest to:",
    f"{v2_re_eq*100:.2f}%",
    f"{wrong_w_wt_v2:.2f}%",
    "Uses the debt-to-value weight $D/V = 0.40$ instead of the debt-to-equity ratio $D/E = 2/3$ in MM Proposition II.",
    f"{wrong_no_spread_v2:.2f}%",
    "Multiplies $r_0$ directly by $D/E$ instead of multiplying $(r_0 - r_d)$ by $D/E$.",
    rf"Under MM Proposition II (no taxes): "
    rf"$$r_e = r_0 + (r_0 - r_d)\frac{{D}}{{E}} = 9.00\% + (9.00\% - 5.00\%)\left(\frac{{200}}{{300}}\right) = {v2_re_eq*100:.2f}\%$$",
    True,
)

# Q3: Increasing debt to 300M (D/E = 1.50) -> r_e = 15.0%, WACC stays 9.00%
wrong_wacc_up_v2 = (0.60 * v2_rd + 0.40 * v2_re_eq) * 100.0
add_q2(
    "L2-CRP-V02-Q3", V2_MOD, V2_TOP, V2_SUB, V2_ID, V2_TITLE, V2_TEXT,
    "Evaluate how changes in leverage affect cost of equity and WACC under MM Proposition II (no taxes).",
    "Suppose Firm L issues an additional USD 100.0 million of risk-free 5.00% debt to repurchase USD 100.0 million of equity (bringing total debt to USD 300.0 million and equity to USD 200.0 million). Under MM Proposition II (no taxes), Firm L's new cost of equity and WACC become:",
    f"$r_e = {v2_re2*100:.2f}\\%$; WACC = {v2_r0*100:.2f}%",
    f"$r_e = {v2_re_eq*100:.2f}\\%$; WACC = {wrong_wacc_up_v2:.2f}%",
    "Fails to update $r_e$ for the higher $D/E = 1.50$ ratio, causing WACC to drop erroneously when substituting cheap debt for equity.",
    f"$r_e = {(v2_r0 + (v2_r0 - v2_rd)*(v2_d2/v2_vu))*100:.2f}\\%$; WACC = {v2_r0*100:.2f}%",
    "Uses $D/V = 0.60$ instead of $D/E = 1.50$ when recalculating $r_e$.",
    rf"With $D = 300\text{{M}}$ and $E = 200\text{{M}}$ ($D/E = 1.50$), equity cost rises linearly to offset cheaper debt: "
    rf"$$r_e = 9.00\% + (9.00\% - 5.00\%)(1.50) = {v2_re2*100:.2f}\%$$ "
    rf"Checking WACC: $\text{{WACC}} = 0.60(5.00\%) + 0.40(15.00\%) = 3.00\% + 6.00\% = {v2_r0*100:.2f}\% = r_0$.",
    True,
)

# Q4: Homemade leverage replication of 5% of Firm L equity
add_q2(
    "L2-CRP-V02-Q4", V2_MOD, V2_TOP, V2_SUB, V2_ID, V2_TITLE, V2_TEXT,
    "Construct homemade leverage strategies to replicate levered equity cash flows.",
    "An investor wants to replicate the exact equilibrium cash flow of owning 5.0% of Firm L's equity (at $D = \\text{USD }200\\text{M}$, $E = \\text{USD }300\\text{M}$) by investing in Firm U's unlevered shares combined with personal borrowing at 5.00%. How much must the investor borrow personally, and what total dollar value of Firm U shares must she purchase?",
    f"Borrow USD {v2_hl_loan:.1f}M; purchase USD {v2_hl_gross_u:.1f}M of Firm U shares",
    f"Borrow USD {v2_stake_hl*v2_e_eq:.1f}M; purchase USD {v2_hl_gross_u:.1f}M of Firm U shares",
    "Borrows an amount equal to 5% of Firm L's equity (USD 15.0M) instead of 5% of Firm L's debt (USD 10.0M).",
    f"Borrow USD {v2_hl_loan:.1f}M; purchase USD {v2_stake_hl*v2_e_eq:.1f}M of Firm U shares",
    "Purchases only USD 15.0M of Firm U shares (net personal equity) instead of investing both her USD 15.0M capital and the USD 10.0M loan into USD 25.0M of Firm U shares.",
    rf"To replicate 5% of Firm L's levered equity payoff ($0.05 \times (45 - 10) = \text{{USD }}1.75\text{{M/yr}}$), the investor combines her USD 15.0M personal funds with a personal loan equal to 5% of Firm L's debt ($0.05 \times 200 = \text{{USD }}{v2_hl_loan:.1f}\text{{M}}$ at 5.0% interest = USD 0.50M/yr) and buys 5% of Firm U ($0.05 \times 500 = \text{{USD }}{v2_hl_gross_u:.1f}\text{{M}}$ paying $0.05 \times 45 = \text{{USD }}2.25\text{{M/yr}}$), netting $2.25 - 0.50 = \text{{USD }}1.75\text{{M/yr}}$.",
    True,
)

# Q5: Conceptual on risky debt
add_q2(
    "L2-CRP-V02-Q5", V2_MOD, V2_TOP, V2_SUB, V2_ID, V2_TITLE, V2_TEXT,
    "Explain how risky debt affects the slope of cost of equity under MM Proposition II.",
    "In practice, at very high debt-to-equity ratios, corporate debt becomes risky ($\\beta_D > 0$) and its yield $r_d$ rises with leverage. Under MM Proposition II without taxes, what happens to the cost of equity ($r_e$) curve as $D/E$ becomes very large?",
    "The rate of increase in $r_e$ flattens (concave slope) because debtholders absorb an increasing share of the firm's operating business risk.",
    "The slope of $r_e$ turns negative so WACC falls steadily below $r_0$ at extreme leverage.",
    "In a tax-free MM world, WACC always remains fixed at $r_0$ regardless of debt riskiness; $r_e$ rises more slowly rather than declining.",
    "The slope of $r_e$ steepens exponentially while WACC increases well above $r_0$.",
    r"Without distress costs or taxes, WACC stays constant at $r_0$; because $r_d$ absorbs part of the asset risk ($\beta_D > 0$), $\beta_E$ and $r_e$ rise more slowly at extreme $D/E$.",
    r"Since $\beta_U = \frac{D}{V}\beta_D + \frac{E}{V}\beta_E$ and $\text{WACC} = r_0$, when high leverage shifts business risk onto risky creditors ($\beta_D$ and $r_d$ rise), the incremental risk borne by equity slows down, causing the $r_e$ line to flatten.",
    False,
)

# =============================================================================
# LEVEL 2: VIGNETTE 3 — MM WITH TAXES & FINANCIAL DISTRESS (CRP-V03)
# =============================================================================
V3_ID = "CRP-V03"
V3_MOD = "CI-L2-M3"
V3_TOP = "Capital Structure Theory"
V3_SUB = "MM With Corporate Taxes & Static Trade-Off"
V3_TITLE = "Meridian Manufacturing — Tax Shields vs. Financial Distress"

v3_vu, v3_r0, v3_t, v3_rd = 800.0, 0.10, 0.25, 0.06
v3_d_t2 = 400.0
v3_ts_t2 = v3_t * v3_d_t2                    # 100.0M
v3_vl_t2 = v3_vu + v3_ts_t2                  # 900.0M
v3_e_t2 = v3_vl_t2 - v3_d_t2                 # 500.0M
v3_re_t2 = v3_r0 + (v3_r0 - v3_rd) * (1.0 - v3_t) * (v3_d_t2 / v3_e_t2)  # 10 + 4*0.75*0.8 = 12.40%
v3_wacc_t2 = v3_r0 * (1.0 - v3_t * (v3_d_t2 / v3_vl_t2))                 # 8.8889%

# Static trade-off across 3 tiers:
v3_t1_d, v3_t1_dist = 200.0, 5.0
v3_t2_d, v3_t2_dist = 400.0, 28.0
v3_t3_d, v3_t3_dist = 600.0, 95.0
v3_net_t1 = v3_vu + v3_t * v3_t1_d - v3_t1_dist  # 845M
v3_net_t2 = v3_vu + v3_t * v3_t2_d - v3_t2_dist  # 872M
v3_net_t3 = v3_vu + v3_t * v3_t3_d - v3_t3_dist  # 855M

V3_TEXT = (
    "Meridian Manufacturing is an unlevered industrial producer with a current unlevered enterprise value ($V_U$) of "
    "USD 800.0 million, an unlevered cost of equity ($r_0$) of 10.00%, and a 25% marginal corporate tax rate. Management "
    "can issue perpetual fixed-rate debt at a constant pre-tax cost of debt ($r_d$) of 6.00%. Corporate finance advisors "
    "present three recapitalization tiers along with estimated present values of expected financial distress costs:\n\n"
    "| Debt Tier | Perpetual Debt Issued ($D$) | PV of Expected Financial Distress Costs |\n"
    "| :--- | :---: | :---: |\n"
    "| Tier 1 (Conservative) | USD 200.0 million | USD 5.0 million |\n"
    "| Tier 2 (Moderate) | USD 400.0 million | USD 28.0 million |\n"
    "| Tier 3 (Aggressive) | USD 600.0 million | USD 95.0 million |"
)

# Q1: MM Prop I with taxes (ignoring distress) at Tier 2
add_q2(
    "L2-CRP-V03-Q1", V3_MOD, V3_TOP, V3_SUB, V3_ID, V3_TITLE, V3_TEXT,
    "Apply Modigliani-Miller Proposition I with corporate taxes to value levered firms.",
    "Ignoring financial distress costs, under MM Proposition I with corporate taxes, issuing Tier 2 debt (USD 400.0 million) produces a levered firm value ($V_L$) and PV of tax shield equal to:",
    f"$V_L = \\text{{USD }}{v3_vl_t2:.0f}\\text{{M}}$; Tax shield PV = USD {v3_ts_t2:.0f}M",
    f"$V_L = \\text{{USD }}{v3_vu + v3_d_t2:.0f}\\text{{M}}$; Tax shield PV = USD {v3_d_t2:.0f}M",
    "Adds the full USD 400M debt face value to $V_U$ instead of only the corporate tax shield $t \\cdot D$.",
    f"$V_L = \\text{{USD }}{v3_vu + v3_t*v3_d_t2*v3_rd:.1f}\\text{{M}}$; Tax shield PV = USD {v3_t*v3_d_t2*v3_rd:.1f}M",
    "Adds only one year's interest tax shield ($t \\cdot r_d \\cdot D = 6.0\\text{M}$) rather than the present value of the perpetual tax shield.",
    rf"Under MM Proposition I with corporate taxes, the perpetual interest tax shield worth $t \cdot r_d \cdot D$ per year discounted at $r_d$ equals $t \cdot D$: "
    rf"$$\text{{PV}}(\text{{Tax Shield}}) = 0.25 \times \text{{USD }}400\text{{M}} = \text{{USD }}{v3_ts_t2:.0f}\text{{M}}, \quad V_L = 800 + 100 = \text{{USD }}{v3_vl_t2:.0f}\text{{M}}$$",
    True,
)

# Q2: MM Prop II with taxes cost of equity at Tier 2
wrong_no_tax_re_v3 = v3_r0 + (v3_r0 - v3_rd) * (v3_d_t2 / v3_e_t2)
wrong_vu_den_v3 = v3_r0 + (v3_r0 - v3_rd) * (1 - v3_t) * (v3_d_t2 / (v3_vu - v3_d_t2))
add_q2(
    "L2-CRP-V03-Q2", V3_MOD, V3_TOP, V3_SUB, V3_ID, V3_TITLE, V3_TEXT,
    "Calculate cost of equity under Modigliani-Miller Proposition II with corporate taxes.",
    "Ignoring financial distress costs, under MM Proposition II with corporate taxes, Meridian's cost of equity ($r_e$) after issuing Tier 2 debt (USD 400.0 million) is closest to:",
    f"{v3_re_t2*100:.2f}%",
    f"{wrong_no_tax_re_v3*100:.2f}%",
    "Omits the $(1 - t)$ tax shield dampening factor in MM Proposition II with corporate taxes.",
    f"{wrong_vu_den_v3*100:.2f}%",
    "Computes $D/E$ using $E = V_U - D = 400\\text{M}$ ($D/E = 1.0$) instead of levered equity $E = V_L - D = 500\\text{M}$ ($D/E = 0.80$).",
    rf"With $V_L = \text{{USD }}900\text{{M}}$ and $D = \text{{USD }}400\text{{M}}$, levered equity value is $E = 900 - 400 = \text{{USD }}500\text{{M}}$ ($D/E = 0.80$): "
    rf"$$r_e = r_0 + (r_0 - r_d)(1 - t)\frac{{D}}{{E}} = 10.00\% + (10.00\% - 6.00\%)(0.75)(0.80) = 10.00\% + 2.40\% = {v3_re_t2*100:.2f}\%$$",
    True,
)

# Q3: WACC under MM with taxes at Tier 2
wrong_no_t_wacc_v3 = ((v3_d_t2 / v3_vl_t2) * v3_rd + (v3_e_t2 / v3_vl_t2) * v3_re_t2) * 100.0
wrong_r0_v3 = v3_r0 * 100.0
add_q2(
    "L2-CRP-V03-Q3", V3_MOD, V3_TOP, V3_SUB, V3_ID, V3_TITLE, V3_TEXT,
    "Compute WACC under Modigliani-Miller Proposition II with corporate taxes.",
    "Ignoring financial distress costs, Meridian's WACC at Tier 2 leverage ($D = \\text{USD }400\\text{M}$, $V_L = \\text{USD }900\\text{M}$) is closest to:",
    f"{v3_wacc_t2*100:.2f}%",
    f"{wrong_no_t_wacc_v3:.2f}%",
    "Uses the pre-tax debt yield (6.00%) in WACC instead of the after-tax cost of debt ($6.00\\% \\times 0.75 = 4.50\\%$).",
    f"{wrong_r0_v3:.2f}%",
    "Assumes WACC remains invariant at $r_0 = 10.00\\%$ even when corporate interest is tax-deductible.",
    rf"Using either weighted components or the MM tax-adjusted WACC shortcut: "
    rf"$$\text{{WACC}} = r_0\left(1 - t\frac{{D}}{{V_L}}\right) = 10.00\%\left(1 - 0.25 \times \frac{{400}}{{900}}\right) = {v3_wacc_t2*100:.2f}\%$$ "
    rf"(Verification: $\frac{{400}}{{900}}(4.50\%) + \frac{{500}}{{900}}(12.40\%) = 2.00\% + 6.89\% = {v3_wacc_t2*100:.2f}\%$.)",
    True,
)

# Q4: Static Trade-Off net firm value across 3 tiers
add_q2(
    "L2-CRP-V03-Q4", V3_MOD, V3_TOP, V3_SUB, V3_ID, V3_TITLE, V3_TEXT,
    "Determine optimal leverage under Static Trade-Off theory balancing tax shields and distress costs.",
    "Incorporating the advisors' PV of expected financial distress costs under Static Trade-Off theory, which debt tier maximizes Meridian's net firm value, and what is that maximum firm value?",
    f"Tier 2 (USD {v3_t2_d:.0f}M debt); maximum firm value = USD {v3_net_t2:.0f} million",
    f"Tier 3 (USD {v3_t3_d:.0f}M debt); maximum firm value = USD {v3_vu + v3_t*v3_t3_d:.0f} million",
    "Selects Tier 3 by maximizing the gross tax shield (USD 150M) while omitting the USD 95M PV of financial distress costs.",
    f"Tier 1 (USD {v3_t1_d:.0f}M debt); maximum firm value = USD {v3_net_t1:.0f} million",
    "Minimizes distress costs at Tier 1 (USD 5M) but stops below the optimal leverage point where marginal tax benefits still exceed marginal distress costs.",
    rf"Compute $V_L = V_U + t \cdot D - \text{{PV}}(\text{{Distress}})$ across all three tiers: "
    rf"Tier 1 $= 800 + 50 - 5 = \text{{USD }}{v3_net_t1:.0f}\text{{M}}$; "
    rf"Tier 2 $= 800 + 100 - 28 = \text{{USD }}{v3_net_t2:.0f}\text{{M}}$; "
    rf"Tier 3 $= 800 + 150 - 95 = \text{{USD }}{v3_net_t3:.0f}\text{{M}}$. "
    rf"Tier 2 maximizes enterprise value at USD {v3_net_t2:.0f} million.",
    True,
)

# Q5: Conceptual distress drivers
add_q2(
    "L2-CRP-V03-Q5", V3_MOD, V3_TOP, V3_SUB, V3_ID, V3_TITLE, V3_TEXT,
    "Analyze business characteristics that increase expected costs of financial distress.",
    "Compared with Meridian Manufacturing's tangible plant-and-equipment asset base, a software biotech firm whose value derives primarily from early-stage R&D intangibles and specialized human capital will most likely exhibit:",
    "Higher expected financial distress costs and therefore a lower optimal debt-to-equity ratio under Static Trade-Off theory.",
    "Lower expected financial distress costs and therefore a higher optimal debt-to-equity ratio.",
    "Intangible R&D assets and specialized talent lose value rapidly in bankruptcy (high indirect and direct distress costs), requiring lower leverage.",
    "Identical optimal leverage because corporate tax rates determine optimal debt independently of asset tangibility.",
    "Optimal leverage under Static Trade-Off depends critically on both tax rates and marginal distress costs, which vary sharply with asset tangibility and earnings volatility.",
    "Firms reliant on intangible growth options, customer trust, and specialized talent suffer severe indirect distress costs (key staff departures, halted R&D, customer defections) and poor liquidation recovery, forcing them toward conservative leverage.",
    False,
)

# =============================================================================
# LEVEL 2: VIGNETTE 4 — STATIC TRADE-OFF, PECKING ORDER & AGENCY (CRP-V04)
# =============================================================================
V4_ID = "CRP-V04"
V4_MOD = "CI-L2-M4"
V4_TOP = "Capital Structure Theory"
V4_SUB = "Pecking Order & Debt Agency Conflicts"
V4_TITLE = "Aegis Biotech — Asymmetric Information & Leverage Conflicts"

# Q1: Myers-Majluf asymmetric info wealth transfer
v4_true_assets = 120.0
v4_mkt_val = 90.0
v4_sh0 = 10.0
v4_p_mkt = v4_mkt_val / v4_sh0        # 9.00
v4_p_true = v4_true_assets / v4_sh0   # 12.00
v4_capex = 30.0
v4_proj_npv = 15.0
v4_proj_pv = v4_capex + v4_proj_npv   # 45.0M
v4_new_sh = v4_capex / v4_p_mkt       # 3.3333M shares
v4_tot_sh = v4_sh0 + v4_new_sh        # 13.3333M shares
v4_tot_true_val = v4_true_assets + v4_proj_pv  # 165.0M
v4_iv_eq_issue = v4_tot_true_val / v4_tot_sh   # 165 / 13.3333 = 12.375/share
v4_iv_internal = (v4_true_assets + v4_proj_npv) / v4_sh0  # 135 / 10 = 13.50/share
v4_dilution_loss = (v4_iv_internal - v4_iv_eq_issue) * v4_sh0  # 11.25M transferred to new shareholders!

# Q2: Debt overhang (underinvestment)
v4_debt_face = 50.0
v4_exist_cf = 40.0
v4_overhang_cost = 15.0
v4_overhang_cf = 20.0
v4_eq_payoff_with = max(v4_exist_cf + v4_overhang_cf - v4_debt_face, 0.0)  # 10.0M
v4_eq_net_gain = v4_eq_payoff_with - v4_overhang_cost  # -5.0M!

# Q3: Asset substitution (risk shifting)
v4_cash = 20.0
v4_safe_cf = 35.0
v4_risky_hi, v4_risky_p = 70.0, 0.20
v4_risky_npv = v4_risky_p * v4_risky_hi - v4_cash  # 14 - 20 = -6.0M
v4_eq_safe = max(v4_safe_cf - v4_debt_face, 0.0)   # 0.0M
v4_eq_risky = v4_risky_p * max(v4_risky_hi - v4_debt_face, 0.0)  # 0.20 * 20 = +4.0M

V4_TEXT = (
    "Aegis Biotech has 10.0 million shares outstanding trading at USD 9.00/share (market capitalization USD 90.0 million) due to "
    "market skepticism, even though management privately knows existing drug patents have a true intrinsic value of USD 120.0 million "
    "(USD 12.00/share). Aegis can invest USD 30.0 million today in a new Phase III drug trial with a present value of USD 45.0 million "
    "(NPV = +USD 15.0 million).\n\n"
    "Separately, Aegis operates a highly levered manufacturing subsidiary facing USD 50.0 million in senior debt maturing in 1 year "
    "(discount rate 0% for simplicity). Two mutually independent subsidiary scenarios are reviewed:\n"
    "- **Scenario A (Debt Overhang):** The subsidiary's existing assets will pay USD 40.0 million with certainty in 1 year. Equityholders "
    "are asked to inject USD 15.0 million of fresh equity to fund a safe project returning USD 20.0 million with certainty in 1 year (NPV = +USD 5.0 million).\n"
    "- **Scenario B (Asset Substitution):** The subsidiary holds USD 20.0 million cash (and zero other assets) and can choose either Project Safe "
    "(certain 1-year payoff USD 35.0 million, NPV = +USD 15.0 million) or Project Risky (20% chance of USD 70.0 million, 80% chance of USD 0)."
)

# Q1: Myers-Majluf wealth transfer
add_q2(
    "L2-CRP-V04-Q1", V4_MOD, V4_TOP, V4_SUB, V4_ID, V4_TITLE, V4_TEXT,
    "Quantify equity dilution and wealth transfer under Myers-Majluf asymmetric information.",
    "If Aegis funds the Phase III trial by issuing USD 30.0 million of new common stock at the depressed USD 9.00/share market price, what will the true post-financing intrinsic value per share be, and how much total wealth is transferred from existing shareholders compared with funding via internal cash?",
    f"Intrinsic value = USD {v4_iv_eq_issue:.3f}/share; wealth transfer = USD {v4_dilution_loss:.2f} million",
    f"Intrinsic value = USD {v4_iv_internal:.3f}/share; wealth transfer = USD 0.00 million",
    "Assumes existing shareholders retain the full USD 13.50/share intrinsic value regardless of issuing undervalued shares at USD 9.00.",
    f"Intrinsic value = USD {(v4_mkt_val + v4_proj_pv)/v4_tot_sh:.3f}/share; wealth transfer = USD {v4_proj_npv:.2f} million",
    "Uses the depressed USD 90.0M market valuation instead of the true USD 120.0M asset value when computing intrinsic value per share.",
    rf"Issuing USD 30.0M at USD 9.00/share creates $30 / 9 = 3.3333\text{{ million}}$ new shares (total $13.3333\text{{M}}$ shares). "
    rf"Total post-financing true enterprise value is $120 + 45 = \text{{USD }}165.0\text{{M}}$, giving an intrinsic price of $165 / 13.3333 = \text{{USD }}{v4_iv_eq_issue:.3f}\text{{ /share}}$. "
    rf"With internal cash, intrinsic value would be $(120 + 15)/10 = \text{{USD }}{v4_iv_internal:.2f}\text{{ /share}}$. Existing shareholders lose $10\text{{M}} \times (13.50 - 12.375) = \text{{USD }}{v4_dilution_loss:.2f}\text{{ million}}$ to new investors.",
    True,
)

# Q2: Debt overhang
add_q2(
    "L2-CRP-V04-Q2", V4_MOD, V4_TOP, V4_SUB, V4_ID, V4_TITLE, V4_TEXT,
    "Evaluate debt overhang (underinvestment) incentives in highly levered firms.",
    "In Scenario A (Debt Overhang), what is the net dollar payoff to existing equityholders if they inject USD 15.0 million to undertake the +USD 5.0 million NPV project?",
    f"-USD {abs(v4_eq_net_gain):.1f} million (equityholders reject the positive-NPV project)",
    f"+USD {v4_eq_payoff_with:.1f} million (equityholders accept the positive-NPV project)",
    "Computes equityholders' gross residual Year 1 claim (USD 10.0M) without subtracting their USD 15.0M upfront equity contribution.",
    "+USD 5.0 million (equityholders capture the full project NPV)",
    "Assumes equityholders receive the project's +USD 5.0M NPV; in reality, USD 10.0M of the project's payoff rescues senior bondholders from a USD 40M-to-50M shortfall.",
    rf"Without the project, firm value is USD 40M against USD 50M debt, leaving equityholders with USD 0. "
    rf"With the project, total firm value rises to $40 + 20 = \text{{USD }}60\text{{M}}$; senior bondholders take USD 50M and equityholders receive USD 10M. "
    rf"After paying the USD 15M cost, equityholders' net payoff is $10 - 15 = -\text{{USD }}{abs(v4_eq_net_gain):.1f}\text{{M}}$, causing underinvestment.",
    True,
)

# Q3: Asset substitution
add_q2(
    "L2-CRP-V04-Q3", V4_MOD, V4_TOP, V4_SUB, V4_ID, V4_TITLE, V4_TEXT,
    "Quantify asset substitution (risk shifting) agency costs under high leverage.",
    "In Scenario B (Asset Substitution), what are the expected Year 1 equityholder payoff and project NPV if management chooses Project Risky rather than Project Safe?",
    f"Expected equity payoff = +USD {v4_eq_risky:.1f}M; Project Risky NPV = -USD {abs(v4_risky_npv):.1f}M",
    f"Expected equity payoff = +USD {v4_risky_p*v4_risky_hi:.1f}M; Project Risky NPV = +USD {v4_safe_cf - v4_cash:.1f}M",
    "Mistakes expected total firm payoff ($0.20 \\times 70 = 14\\text{M}$) for equity payoff and assigns Project Safe's +USD 15M NPV to Project Risky.",
    f"Expected equity payoff = USD {v4_eq_safe:.1f}M; Project Risky NPV = -USD {abs(v4_risky_npv):.1f}M",
    "Reports Project Safe's equity payoff (USD 0) rather than Project Risky's expected equity payoff (+USD 4.0M).",
    rf"Project Risky's expected payoff is $0.20(70) + 0.80(0) = \text{{USD }}14.0\text{{M}}$, giving negative NPV $= 14 - 20 = -\text{{USD }}{abs(v4_risky_npv):.1f}\text{{M}}$. "
    rf"However, equityholders earn $0.20 \times (70 - 50) + 0.80(0) = +\text{{USD }}{v4_eq_risky:.1f}\text{{M}}$ (versus USD 0 under Project Safe, since 35M < 50M debt), creating an incentive to shift risk onto creditors.",
    True,
)

# Q4: Pecking Order Conceptual
add_q2(
    "L2-CRP-V04-Q4", V4_MOD, V4_TOP, V4_SUB, V4_ID, V4_TITLE, V4_TEXT,
    "Compare Pecking Order theory predictions against Static Trade-Off theory.",
    "Consistent with the Myers-Majluf framework demonstrated in Aegis Biotech's Phase III financing analysis, Pecking Order theory predicts which financing hierarchy and empirical relationship between profitability and leverage?",
    "Internal cash flows first, then debt, then external equity as last resort; more profitable firms exhibit lower debt ratios.",
    "External equity first, then convertible debt, then internal retained earnings; more profitable firms exhibit higher debt ratios.",
    "Inverts the Pecking Order hierarchy and confuses it with Static Trade-Off theory's prediction that profitable firms borrow more for tax shields.",
    "Debt first, then external equity, then internal cash; leverage stays strictly fixed at a target debt-to-equity ratio.",
    "Pecking Order explicitly rejects a fixed target leverage ratio and places internal funds at the top to avoid asymmetric-information adverse selection.",
    "Because external equity suffers the sharpest asymmetric-information discount, managers prefer internal cash first, low-risk debt second, and equity last. Highly profitable firms fund investments internally without borrowing, producing lower observed leverage.",
    False,
)

# Q5: Mitigating debt agency conflicts
add_q2(
    "L2-CRP-V04-Q5", V4_MOD, V4_TOP, V4_SUB, V4_ID, V4_TITLE, V4_TEXT,
    "Evaluate contractual instruments and covenants that reduce debt-equity agency costs.",
    "Which financing design feature most directly mitigates BOTH asset substitution (Scenario B) and debt overhang (Scenario A) when raising new corporate debt?",
    "Including a conversion feature (convertible bonds) paired with restrictive investment/dividend covenants and shorter debt maturities.",
    "Issuing long-term non-callable zero-coupon junior subordinated debt with zero covenants.",
    "Long-maturity, covenant-free junior debt maximizes equityholders' option-like incentives to shift risk and underinvest.",
    "Eliminating all interest payments via preferred equity while allowing unlimited asset sales.",
    "Preferred equity is not a debt covenant solution and unrestricted asset sales exacerbate creditor expropriation.",
    "Convertible debt gives creditors an equity upside kicker that offsets risk-shifting gains, while short maturities and negative covenants restrict speculative investments and force early renegotiation before debt overhang worsens.",
    False,
)

# =============================================================================
# LEVEL 2: VIGNETTE 5 — AGENCY COSTS, GOVERNANCE & VALUATION (CRP-V05)
# =============================================================================
V5_ID = "CRP-V05"
V5_MOD = "CI-L2-M5"
V5_TOP = "Corporate Governance & Valuation"
V5_SUB = "Agency Costs, Voting Wedges & Governance Discount"
V5_TITLE = "Chronos Holdings — Governance Overhaul Valuation"

v5_sh_b, v5_vt_b = 5.0, 10.0    # 5M sh, 50M votes
v5_sh_a, v5_vt_a = 45.0, 1.0    # 45M sh, 45M votes
v5_tot_sh = v5_sh_b + v5_sh_a   # 50M
v5_tot_vt = v5_sh_b * v5_vt_b + v5_sh_a * v5_vt_a  # 95M
v5_econ_pct = (v5_sh_b / v5_tot_sh) * 100.0        # 10.00%
v5_vote_pct = (v5_sh_b * v5_vt_b / v5_tot_vt) * 100.0  # 52.6316%
v5_wedge = v5_vote_pct - v5_econ_pct               # 42.63 pct pts

v5_fcf_excess = 80.0
v5_acq_cf = 5.6
v5_wacc = 0.10
v5_acq_pv = v5_acq_cf / v5_wacc                    # 56.0M
v5_npv_loss = v5_acq_pv - v5_fcf_excess            # -24.0M

v5_d1, v5_g, v5_ke_base, v5_gov_prem = 2.20, 0.04, 0.098, 0.012
v5_ke_pen = v5_ke_base + v5_gov_prem               # 11.0%
v5_p_pen = v5_d1 / (v5_ke_pen - v5_g)              # 2.20 / 0.07 = 31.4286
v5_p_clean = v5_d1 / (v5_ke_base - v5_g)           # 2.20 / 0.058 = 37.9310
v5_uplift = v5_p_clean - v5_p_pen                  # +6.5025
v5_uplift_pct = (v5_p_clean / v5_p_pen - 1.0) * 100.0

V5_TEXT = (
    "Chronos Holdings is a mature media-software conglomerate controlled by its founder-CEO, who also serves as Board Chair. "
    "Chronos's equity consists of 5.0 million Class B shares (10 votes per share, 100% owned by the founder) and 45.0 million "
    "Class A shares (1 vote per share, widely held by institutions); both classes share equal economic cash flow rights per share. "
    "Chronos operates with a staggered 3-year board.\n\n"
    "Chronos currently holds USD 80.0 million in excess free cash flow. Management proposes spending the entire USD 80.0 million "
    "to acquire a prestige boutique film studio expected to generate perpetual after-tax cash flows of USD 5.6 million annually "
    "(a 7.00% return), well below Chronos's 10.00% WACC. Governance analysts estimate that Chronos's entrenched governance imposes "
    "a 120 bps governance risk premium on its cost of equity, lifting $k_e$ from 9.80% to 11.00%. Chronos's forward dividend ($D_1$) "
    "is USD 2.20/share with a 4.00% perpetual growth rate."
)

# Q1: Control-ownership wedge
add_q2(
    "L2-CRP-V05-Q1", V5_MOD, V5_TOP, V5_SUB, V5_ID, V5_TITLE, V5_TEXT,
    "Quantify voting control versus economic ownership wedges in dual-class structures.",
    "What is the founder-CEO's control-ownership wedge (percentage voting power minus percentage economic cash flow rights)?",
    f"{v5_wedge:.2f} percentage points ({v5_vote_pct:.2f}% voting vs. {v5_econ_pct:.2f}% economic)",
    f"{v5_vote_pct:.2f} percentage points ({v5_vote_pct:.2f}% voting vs. 0.00% economic)",
    "Reports total voting share without subtracting the founder's 10.00% economic ownership.",
    f"{(50.0/55.0 - 0.10)*100:.2f} percentage points ({(50.0/55.0)*100:.2f}% voting vs. 10.00% economic)",
    "Uses total shares (50M) instead of total votes (95M) when computing Class B voting share.",
    rf"Founder economic ownership is $5 / (5 + 45) = {v5_econ_pct:.2f}\%$. "
    rf"Total votes equal $5(10) + 45(1) = 95\text{{M}}$, so founder voting power is $50 / 95 = {v5_vote_pct:.2f}\%$. "
    rf"The control-ownership wedge equals ${v5_vote_pct:.2f}\% - {v5_econ_pct:.2f}\% = {v5_wedge:.2f}$ percentage points.",
    True,
)

# Q2: Jensen FCF empire building NPV destruction
add_q2(
    "L2-CRP-V05-Q2", V5_MOD, V5_TOP, V5_SUB, V5_ID, V5_TITLE, V5_TEXT,
    "Quantify equity agency costs of free cash flow from value-destroying acquisitions.",
    "How much shareholder value (NPV) would be preserved if Chronos returned the USD 80.0 million excess free cash flow to shareholders rather than executing management's proposed film studio acquisition?",
    f"USD {abs(v5_npv_loss):.1f} million",
    f"USD {v5_acq_pv:.1f} million",
    "Reports the gross present value of the film studio's cash flows (USD 56.0M) rather than the negative NPV avoided.",
    f"USD {v5_fcf_excess:.1f} million",
    "Assumes the entire USD 80.0M purchase price is wasted rather than recognizing the USD 56.0M PV of cash inflows generated.",
    rf"The studio's present value at Chronos's 10.0% WACC is $\text{{PV}} = 5.6 / 0.10 = \text{{USD }}{v5_acq_pv:.1f}\text{{M}}$. "
    rf"Paying USD 80.0M yields an acquisition NPV of $56.0 - 80.0 = -\text{{USD }}{abs(v5_npv_loss):.1f}\text{{M}}$. "
    rf"Returning the cash instead preserves USD {abs(v5_npv_loss):.1f} million of shareholder wealth.",
    True,
)

# Q3: Governance discount removal share price uplift
add_q2(
    "L2-CRP-V05-Q3", V5_MOD, V5_TOP, V5_SUB, V5_ID, V5_TITLE, V5_TEXT,
    "Measure the valuation impact of incorporating governance risk premia into equity discount rates.",
    "Assuming $D_1 = \\text{USD }2.20$ and $g = 4.00\\%$ remain unchanged, if governance reforms eliminate the 120 bps governance risk premium (lowering $k_e$ from 11.00% to 9.80%), Chronos's Gordon Growth intrinsic share price increases by:",
    f"USD {v5_uplift:.2f}/share (+{v5_uplift_pct:.2f}%)",
    f"USD {v5_p_clean:.2f}/share (+100.00%)",
    "Reports the full post-reform share price (USD 37.93) instead of the incremental per-share valuation gain (USD 6.50).",
    f"USD {(v5_d1/0.11 - v5_d1/0.098)*(-1):.2f}/share",
    "Omits the 4.00% perpetual growth rate $g$ in the Gordon Growth denominator ($k_e - g$).",
    rf"Under the 11.00% governance-penalized cost of equity: "
    rf"$$P_{{\text{{penalized}}}} = \frac{{2.20}}{{0.110 - 0.040}} = \text{{USD }}{v5_p_pen:.2f}$$ "
    rf"After reforms remove the 120 bps penalty ($k_e = 9.80\%$): "
    rf"$$P_{{\text{{clean}}}} = \frac{{2.20}}{{0.098 - 0.040}} = \text{{USD }}{v5_p_clean:.2f}$$ "
    rf"Share price increases by $37.93 - 31.43 = \text{{USD }}{v5_uplift:.2f}/\text{{share}}$ (+{v5_uplift_pct:.2f}%).",
    True,
)

# Q4: Governance reform evaluation
add_q2(
    "L2-CRP-V05-Q4", V5_MOD, V5_TOP, V5_SUB, V5_ID, V5_TITLE, V5_TEXT,
    "Evaluate governance reform remedies for entrenched management and dual-class structures.",
    "Which single structural reform would most fundamentally address the root cause of minority Class A shareholder disenfranchisement at Chronos Holdings?",
    "Adopting a time-based sunset provision collapsing Class B super-voting shares into one-share-one-vote Class A shares.",
    "Increasing the annual cash retainer paid to incumbent directors serving on the staggered board.",
    "Higher director pay without structural accountability does not resolve unequal voting rights or board entrenchment.",
    "Retaining CEO/Chair duality while shifting external auditors every 20 years.",
    "Retaining CEO duality preserves governance concentration; external audit rotation does not cure dual-class disenfranchisement.",
    "While separating CEO/Chair and declassifying the staggered board improve oversight, as long as one founder holds 52.63% of total votes via permanent 10-vote Class B stock, minority investors cannot compel board changes without a dual-class sunset.",
    False,
)

# Q5: Jensen FCF hypothesis and debt monitoring
add_q2(
    "L2-CRP-V05-Q5", V5_MOD, V5_TOP, V5_SUB, V5_ID, V5_TITLE, V5_TEXT,
    "Explain Jensen's free cash flow hypothesis on how debt reduces equity agency costs.",
    "According to Jensen's free cash flow hypothesis, how could issuing moderate debt financed with a special cash payout mitigate Chronos's equity agency problem?",
    "Contractual interest and principal obligations legally pre-commit excess operating cash flow to creditors, shrinking discretionary cash available for value-destroying empire building.",
    "Debt interest is paid strictly at management's discretion, allowing managers to skip interest whenever acquisitions look attractive.",
    "Unlike common dividends, debt coupons are binding contractual obligations where default triggers creditor takeover.",
    "Issuing debt automatically converts Class B super-voting shares into single-vote shares.",
    "Debt issuance does not alter common equity share-class voting rights under the corporate charter.",
    "Jensen's free cash flow hypothesis demonstrates that binding debt service forces managers to disgorge excess cash to capital markets rather than investing in negative-NPV pet projects, reducing equity agency costs.",
    False,
)

# =============================================================================
# LEVEL 2: VIGNETTE 6 — DIVIDEND POLICY: LINTNER & RESIDUAL MODEL (CRP-V06)
# =============================================================================
V6_ID = "CRP-V06"
V6_MOD = "CI-L2-M6"
V6_TOP = "Payout Policy"
V6_SUB = "Target Payout Adjustment & Residual Dividend Model"
V6_TITLE = "Apex Industrial — Dividend Smoothing vs. Residual Policy"

v6_sh, v6_d0, v6_tgt_po, v6_adj = 20.0, 1.60, 0.40, 0.30
v6_eps1, v6_eps2 = 5.00, 6.00
v6_ni1, v6_ni2 = v6_eps1 * v6_sh, v6_eps2 * v6_sh  # 100M, 120M
v6_capex1, v6_capex2, v6_we = 120.0, 190.0, 0.60

v6_d1_lint = v6_d0 + ((v6_eps1 * v6_tgt_po) - v6_d0) * v6_adj  # 1.60 + 0.40*0.30 = 1.72
v6_d2_lint = v6_d1_lint + ((v6_eps2 * v6_tgt_po) - v6_d1_lint) * v6_adj  # 1.72 + 0.68*0.30 = 1.924

v6_res_eq1 = v6_we * v6_capex1         # 72.0M
v6_res_div1 = v6_ni1 - v6_res_eq1      # 28.0M
v6_res_dps1 = v6_res_div1 / v6_sh      # 1.40
v6_res_po1 = (v6_res_div1 / v6_ni1) * 100.0  # 28.0%

v6_res_eq2 = v6_we * v6_capex2         # 114.0M
v6_res_div2 = v6_ni2 - v6_res_eq2      # 6.0M
v6_res_dps2 = v6_res_div2 / v6_sh      # 0.30
v6_res_po2 = (v6_res_div2 / v6_ni2) * 100.0  # 5.0%

V6_TEXT = (
    "Apex Industrial has 20.0 million common shares outstanding and maintains a target capital structure of 60% equity and "
    "40% debt. Prior year annual dividend ($D_0$) was USD 1.60/share. Management projects EPS of USD 5.00 in Year 1 "
    "(Net Income = USD 100.0 million) and USD 6.00 in Year 2 (Net Income = USD 120.0 million). Capital budgeting identifies "
    "positive-NPV investment opportunities totaling USD 120.0 million in Year 1 and USD 190.0 million in Year 2.\n\n"
    "The board evaluates two alternative payout frameworks:\n"
    "- **Framework A (Lintner Target Payout Adjustment):** Long-run target payout ratio of 40% with an annual adjustment factor of 0.30.\n"
    "- **Framework B (Pure Residual Dividend Policy):** Fund the equity portion of positive-NPV capex internally first and distribute remaining net income as dividends."
)

# Q1: Lintner Year 1
wrong_no_sub_v6 = v6_d0 + (v6_eps1 * v6_tgt_po) * v6_adj
wrong_1minus_v6 = v6_d0 + ((v6_eps1 * v6_tgt_po) - v6_d0) * (1.0 - v6_adj)
add_q2(
    "L2-CRP-V06-Q1", V6_MOD, V6_TOP, V6_SUB, V6_ID, V6_TITLE, V6_TEXT,
    "Apply Lintner's target payout adjustment model to project future dividends.",
    "Under Framework A (Lintner Target Payout Adjustment), Apex Industrial's expected Year 1 dividend per share ($D_1$) is closest to:",
    f"USD {v6_d1_lint:.3f}",
    f"USD {wrong_1minus_v6:.3f}",
    "Applies $(1 - 0.30) = 0.70$ instead of the 0.30 adjustment factor to the dividend gap.",
    f"USD {wrong_no_sub_v6:.3f}",
    "Adds $0.30 \\times \\text{Target Dividend}$ directly to $D_0$ without subtracting prior dividend $D_0$ inside the brackets.",
    rf"Under the Lintner partial adjustment model: "
    rf"$$D_1 = D_0 + \left[(\text{{EPS}}_1 \times \text{{Target Payout}}) - D_0\right] \times \text{{Adj}} = 1.60 + [(5.00 \times 0.40) - 1.60](0.30) = 1.60 + 0.12 = \text{{USD }}{v6_d1_lint:.2f}$$",
    True,
)

# Q2: Lintner Year 2
wrong_chain_d0_v6 = v6_d0 + ((v6_eps2 * v6_tgt_po) - v6_d0) * v6_adj
wrong_full_tgt_v6 = v6_eps2 * v6_tgt_po
add_q2(
    "L2-CRP-V06-Q2", V6_MOD, V6_TOP, V6_SUB, V6_ID, V6_TITLE, V6_TEXT,
    "Project multi-year dividend paths under the Lintner partial adjustment model.",
    "Continuing under Framework A from Year 1, Apex Industrial's expected Year 2 dividend per share ($D_2$) is closest to:",
    f"USD {v6_d2_lint:.3f}",
    f"USD {wrong_chain_d0_v6:.3f}",
    "Anchors Year 2 adjustment on $D_0 = \\text{USD }1.60$ instead of the updated prior-year dividend $D_1 = \\text{USD }1.72$.",
    f"USD {wrong_full_tgt_v6:.3f}",
    "Assumes instant full convergence to the 40% target payout ratio ($6.00 \\times 0.40 = \\text{USD }2.40$).",
    rf"Year 2 adjusts incrementally from $D_1 = \text{{USD }}{v6_d1_lint:.2f}$ toward the new target of $6.00 \times 0.40 = \text{{USD }}2.40$: "
    rf"$$D_2 = 1.72 + (2.40 - 1.72)(0.30) = 1.72 + 0.204 = \text{{USD }}{v6_d2_lint:.3f}$$",
    True,
)

# Q3: Residual Dividend Year 1
wrong_debt_wt_v6 = (v6_ni1 - 0.40 * v6_capex1) / v6_sh
wrong_full_capex_v6 = max(v6_ni1 - v6_capex1, 0.0) / v6_sh
add_q2(
    "L2-CRP-V06-Q3", V6_MOD, V6_TOP, V6_SUB, V6_ID, V6_TITLE, V6_TEXT,
    "Calculate residual dividends and implied payout ratios under the residual dividend model.",
    "Under Framework B (Pure Residual Dividend Policy), Apex's Year 1 dividend per share and implied payout ratio are:",
    f"USD {v6_res_dps1:.2f}/share ({v6_res_po1:.1f}% payout ratio)",
    f"USD {wrong_debt_wt_v6:.2f}/share ({(v6_ni1 - 0.40*v6_capex1)/v6_ni1*100:.1f}% payout ratio)",
    "Uses the 40% debt weight instead of the 60% target equity weight to compute equity required for the USD 120M capital budget.",
    f"USD {wrong_full_capex_v6:.2f}/share (0.0% payout ratio)",
    "Deducts the entire USD 120M capital budget from Net Income rather than only the 60% equity-financed portion (USD 72M).",
    rf"Year 1 capex requires $0.60 \times \text{{USD }}120\text{{M}} = \text{{USD }}{v6_res_eq1:.1f}\text{{M}}$ of internal equity (with USD 48M funded by new debt). "
    rf"Residual dividend equals $100.0 - 72.0 = \text{{USD }}{v6_res_div1:.1f}\text{{M}}$, or $\text{{USD }}{v6_res_dps1:.2f}/\text{{share}}$ ({v6_res_po1:.1f}% payout ratio).",
    True,
)

# Q4: Residual Dividend Year 2
wrong_res_no_capex_v6 = v6_ni2 / v6_sh
wrong_debt_y2_v6 = (v6_ni2 - 0.40 * v6_capex2) / v6_sh
add_q2(
    "L2-CRP-V06-Q4", V6_MOD, V6_TOP, V6_SUB, V6_ID, V6_TITLE, V6_TEXT,
    "Evaluate how capital expenditure spikes drive dividend volatility under a residual policy.",
    "Under Framework B (Pure Residual Dividend Policy), despite Net Income rising 20% in Year 2, Apex's Year 2 dividend per share falls to:",
    f"USD {v6_res_dps2:.2f}/share ({v6_res_po2:.1f}% payout ratio)",
    f"USD {wrong_debt_y2_v6:.2f}/share ({(v6_ni2 - 0.40*v6_capex2)/v6_ni2*100:.1f}% payout ratio)",
    "Applies the 40% debt weight rather than the 60% equity weight to the USD 190M Year 2 capex.",
    f"USD {wrong_res_no_capex_v6:.2f}/share (100.0% payout ratio)",
    "Distributes all Net Income while financing 100% of Year 2 capex externally.",
    rf"Year 2 equity financing need equals $0.60 \times \text{{USD }}190\text{{M}} = \text{{USD }}{v6_res_eq2:.1f}\text{{M}}$. "
    rf"Residual dividend drops sharply to $120.0 - 114.0 = \text{{USD }}{v6_res_div2:.1f}\text{{M}}$, or $\text{{USD }}{v6_res_dps2:.2f}/\text{{share}}$ ({v6_res_po2:.1f}% payout ratio).",
    True,
)

# Q5: Conceptual signaling/clientele
add_q2(
    "L2-CRP-V06-Q5", V6_MOD, V6_TOP, V6_SUB, V6_ID, V6_TITLE, V6_TEXT,
    "Compare investor signaling and clientele implications of residual versus stable dividend policies.",
    "Why do most publicly listed mature corporations prefer Framework A (smoothed target payout adjustment) over strict Framework B (pure annual residual dividends)?",
    "Pure residual payouts fluctuate violently with lumpy capex, triggering adverse dividend-cut signals and disrupting income-oriented investor clienteles.",
    "Pure residual policies violate Modigliani-Miller dividend irrelevance by lowering corporate WACC whenever dividends fluctuate.",
    "In an ideal MM world dividend policy is irrelevant; real-world preference for Framework A stems from asymmetric-information signaling and clientele transaction costs.",
    "Framework A allows companies to skip dividends without any negative market reaction during earnings downturns.",
    "Under Framework A, dividend cuts are rare and heavily penalized by markets; firms smooth payouts specifically to avoid signaling distress.",
    "Under Framework B, Apex's dividend drops 78.6% (from USD 1.40 to USD 0.30) even though earnings rose 20%. Because investors interpret dividend cuts as pessimistic cash flow signals and face tax/trading friction when adjusting portfolios, firms smooth dividends via Framework A.",
    False,
)

# =============================================================================
# LEVEL 2: VIGNETTE 7 — DIVIDEND TAXATION & CLIENTELE EFFECTS (CRP-V07)
# =============================================================================
V7_ID = "CRP-V07"
V7_MOD = "CI-L2-M7"
V7_TOP = "Payout Policy"
V7_SUB = "Effective Dividend Tax Rates & Ex-Dividend Pricing"
V7_TITLE = "EuroNordic Corp — Cross-Border Dividend Tax Regimes"

v7_inc = 100.0
v7_a_tc, v7_a_td = 0.25, 0.20
v7_a_teff = (1.0 - (1.0 - v7_a_tc) * (1.0 - v7_a_td)) * 100.0  # 40.0%
v7_a_net = v7_inc * (1.0 - v7_a_teff / 100.0)                  # 60.0

v7_b_tret, v7_b_tdist, v7_b_td = 0.30, 0.18, 0.22
v7_b_teff = (1.0 - (1.0 - v7_b_tdist) * (1.0 - v7_b_td)) * 100.0  # 36.04%
v7_b_net = v7_inc * (1.0 - v7_b_teff / 100.0)                     # 63.96

v7_c_tc, v7_c_tsh = 0.25, 0.35
v7_c_div_cash = v7_inc * (1.0 - v7_c_tc)        # 75.0
v7_c_gross_tax = v7_inc * v7_c_tsh              # 35.0
v7_c_credit = v7_inc * v7_c_tc                  # 25.0
v7_c_addl_tax = v7_c_gross_tax - v7_c_credit    # 10.0
v7_c_net = v7_c_div_cash - v7_c_addl_tax        # 65.0 (teff = 35.0%)

v7_p_cum, v7_div_ex, v7_m_td, v7_m_tcg = 60.00, 3.00, 0.25, 0.10
v7_dp = v7_div_ex * (1.0 - v7_m_td) / (1.0 - v7_m_tcg)  # 2.50
v7_p_ex = v7_p_cum - v7_dp                               # 57.50

V7_TEXT = (
    "EuroNordic Corp is evaluating corporate domicile options across three European tax jurisdictions, assuming 100% of "
    "after-tax corporate profits are paid immediately as cash dividends on EUR 100.00 of pre-tax corporate earnings:\n"
    "- **Country A (Classical Double Taxation):** Corporate income tax rate = 25%; personal dividend tax rate = 20%.\n"
    "- **Country B (Split-Rate Corporate Tax):** Corporate tax rate = 30% on retained earnings and 18% on distributed earnings; personal dividend tax rate = 22%.\n"
    "- **Country C (Full Tax Imputation):** Corporate income tax rate = 25% (credited in full to shareholders); shareholder's marginal personal tax rate = 35%.\n\n"
    "In Country A's equity market, EuroNordic shares trade cum-dividend at EUR 60.00 immediately prior to going ex-dividend "
    "for a EUR 3.00/share cash dividend. Marginal investors in EuroNordic face a 25% personal tax rate on dividends and a 10% tax rate on realized capital gains."
)

# Q1: Country A effective tax rate
add_q2(
    "L2-CRP-V07-Q1", V7_MOD, V7_TOP, V7_SUB, V7_ID, V7_TITLE, V7_TEXT,
    "Calculate effective tax rates under a classical double-taxation dividend system.",
    "In Country A (Classical Double Taxation), the effective combined tax rate on distributed corporate profits and net cash received by the shareholder per EUR 100.00 of pre-tax income are:",
    f"{v7_a_teff:.2f}%; net cash = EUR {v7_a_net:.2f}",
    f"{(v7_a_tc + v7_a_td)*100:.2f}%; net cash = EUR {100*(1 - v7_a_tc - v7_a_td):.2f}",
    "Adds the 25% corporate tax and 20% personal dividend tax directly instead of applying 20% only to the EUR 75.00 net corporate payout.",
    f"{v7_a_tc*100:.2f}%; net cash = EUR {100*(1 - v7_a_tc):.2f}",
    "Stops after corporate taxation and overlooks the personal tax levied on the cash dividend.",
    rf"Corporate tax takes EUR 25.00, leaving EUR 75.00 paid as a cash dividend. Personal dividend tax equals $20\% \times 75.00 = \text{{EUR }}15.00$, leaving $\text{{EUR }}{v7_a_net:.2f}$: "
    rf"$$t_{{\text{{eff}},A}} = 1 - (1 - 0.25)(1 - 0.20) = {v7_a_teff:.2f}\%$$",
    True,
)

# Q2: Country B split-rate tax rate
wrong_ret_b_v7 = (1.0 - (1.0 - v7_b_tret) * (1.0 - v7_b_td)) * 100.0
wrong_sum_b_v7 = (v7_b_tdist + v7_b_td) * 100.0
add_q2(
    "L2-CRP-V07-Q2", V7_MOD, V7_TOP, V7_SUB, V7_ID, V7_TITLE, V7_TEXT,
    "Calculate effective dividend tax rates under a split-rate corporate tax system.",
    "In Country B (Split-Rate Corporate Tax), because 100% of earnings are distributed, the effective combined tax rate is closest to:",
    f"{v7_b_teff:.2f}%",
    f"{wrong_ret_b_v7:.2f}%",
    "Applies the 30% retained-earnings corporate tax rate instead of the 18% distributed-earnings corporate rate.",
    f"{wrong_sum_b_v7:.2f}%",
    "Simply sums the 18% corporate tax rate and 22% dividend tax rate ($40.00\\%$).",
    rf"Because 100% of earnings are distributed, corporate tax applies at the 18% distributed rate ($t_{{\text{{dist}}}} = 0.18$): "
    rf"$$t_{{\text{{eff}},B}} = 1 - (1 - 0.18)(1 - 0.22) = 1 - (0.82)(0.78) = {v7_b_teff:.2f}\%$$ "
    rf"Net shareholder cash is EUR {v7_b_net:.2f} per EUR 100.00 of pre-tax income.",
    True,
)

# Q3: Country C Full Imputation
wrong_no_grossup_v7 = v7_c_div_cash - (v7_c_div_cash * v7_c_tsh - v7_c_credit)
wrong_double_c_v7 = v7_inc * (1 - v7_c_tc) * (1 - v7_c_tsh)
add_q2(
    "L2-CRP-V07-Q3", V7_MOD, V7_TOP, V7_SUB, V7_ID, V7_TITLE, V7_TEXT,
    "Calculate shareholder net dividends and tax credits under a full tax imputation system.",
    "In Country C (Full Tax Imputation), what additional personal tax must the shareholder pay (after claiming the corporate tax credit), and what is the shareholder's net after-tax dividend per EUR 100.00 of pre-tax corporate profit?",
    f"Additional tax = EUR {v7_c_addl_tax:.2f}; net cash = EUR {v7_c_net:.2f}",
    f"Additional tax = EUR {v7_c_div_cash * v7_c_tsh - v7_c_credit:.2f}; net cash = EUR {wrong_no_grossup_v7:.2f}",
    "Applies the 35% personal tax rate to the EUR 75.00 cash dividend without grossing it back up to the EUR 100.00 pre-tax corporate profit.",
    f"Additional tax = EUR {v7_c_div_cash * v7_c_tsh:.2f}; net cash = EUR {wrong_double_c_v7:.2f}",
    "Treats Country C as a classical double-taxation system by ignoring the EUR 25.00 corporate tax imputation credit.",
    rf"Under full imputation, EuroNordic pays EUR 25.00 corporate tax and distributes EUR 75.00 cash. The shareholder grosses up the dividend back to EUR 100.00 pre-tax profit, owes $35\% \times 100 = \text{{EUR }}35.00$ gross tax, and offsets the EUR 25.00 corporate tax credit—paying only $35 - 25 = \text{{EUR }}{v7_c_addl_tax:.2f}$ additional personal tax. Net cash received is $75 - 10 = \text{{EUR }}{v7_c_net:.2f}$ (exact overall tax rate = {v7_c_tsh*100:.0f}%).",
    True,
)

# Q4: Ex-dividend price drop
wrong_full_drop_v7 = v7_p_cum - v7_div_ex
wrong_inv_tax_v7 = v7_p_cum - v7_div_ex * (1 - v7_m_tcg) / (1 - v7_m_td)
add_q2(
    "L2-CRP-V07-Q4", V7_MOD, V7_TOP, V7_SUB, V7_ID, V7_TITLE, V7_TEXT,
    "Estimate ex-dividend share price drops as a function of dividend and capital gains tax rates.",
    "Based on marginal investor tax rates in Country A ($t_{{\\text{{div}}}} = 25\\%$, $t_{{\\text{{cg}}}} = 10\\%$), the theoretical ex-dividend opening price for EuroNordic shares is closest to:",
    f"EUR {v7_p_ex:.2f}",
    f"EUR {wrong_full_drop_v7:.2f}",
    "Assumes the share price drops by the full EUR 3.00 dividend, ignoring the relative tax disadvantage of dividends versus capital gains.",
    f"EUR {wrong_inv_tax_v7:.2f}",
    "Inverts the tax ratio $(1 - t_{\\text{cg}}) / (1 - t_{\\text{div}})$, implying a price drop larger than the EUR 3.00 dividend.",
    rf"To prevent short-term dividend-capture arbitrage, the after-tax dividend must equal the after-tax capital loss on the ex-dividend date: "
    rf"$$\Delta P = D \cdot \frac{{1 - t_{{\text{{div}}}}}}{{1 - t_{{\text{{cg}}}}}} = 3.00 \times \frac{{1 - 0.25}}{{1 - 0.10}} = \text{{EUR }}{v7_dp:.2f}$$ "
    rf"Expected ex-dividend price is $\text{{EUR }}60.00 - \text{{EUR }}{v7_dp:.2f} = \text{{EUR }}{v7_p_ex:.2f}$.",
    True,
)

# Q5: Clientele effect
add_q2(
    "L2-CRP-V07-Q5", V7_MOD, V7_TOP, V7_SUB, V7_ID, V7_TITLE, V7_TEXT,
    "Interpret investor tax clienteles across dividend-paying and zero-dividend stocks.",
    "In Country A's classical tax regime ($t_{{\\text{{div}}}} = 25\\%$ vs. $t_{{\\text{{cg}}}} = 10\\%$), which investor group forms the natural clientele for high-dividend-yield utility equities?",
    "Tax-exempt institutional investors such as sovereign wealth funds and defined-benefit pension trusts.",
    "High-net-worth individuals in the top marginal dividend tax bracket seeking capital appreciation.",
    "Taxable high-bracket individuals face a 25% immediate dividend tax drag versus 10% deferred capital gains, driving them toward zero-dividend growth firms or buybacks.",
    "Active short-term equity arbitrageurs subject to 25% ordinary income tax on dividends.",
    "Taxed investors suffer a net tax penalty on dividends unless ex-dividend drops are unusually small.",
    "Because tax-exempt investors pay zero tax on both dividends and capital gains ($t_d = t_{cg} = 0$), they face no tax penalty on cash payouts and naturally gravitate toward high-dividend shares that taxable retail investors avoid.",
    False,
)

# =============================================================================
# LEVEL 2: VIGNETTE 8 — SHARE REPURCHASES: EPS & BVPS IMPACT (CRP-V08)
# =============================================================================
V8_ID = "CRP-V08"
V8_MOD = "CI-L2-M8"
V8_TOP = "Payout Policy"
V8_SUB = "Share Repurchases: EPS Accretion & BVPS Impact"
V8_TITLE = "Titan Logistics — Cash vs. Debt-Funded Share Buybacks"

v8_ni0, v8_sh0, v8_p0, v8_bv0, v8_buy_amt, v8_t = 60.0, 20.0, 36.0, 480.0, 72.0, 0.25
v8_eps0 = v8_ni0 / v8_sh0           # 3.00
v8_bvps0 = v8_bv0 / v8_sh0          # 24.00
v8_ep = v8_eps0 / v8_p0             # 8.3333%
v8_sh_rep = v8_buy_amt / v8_p0      # 2.0M shares
v8_sh1 = v8_sh0 - v8_sh_rep         # 18.0M shares

v8_r_cash_pre = 0.04
v8_r_cash_at = v8_r_cash_pre * (1.0 - v8_t)  # 3.00%
v8_ni_x = v8_ni0 - v8_buy_amt * v8_r_cash_at # 60 - 2.16 = 57.84M
v8_eps_x = v8_ni_x / v8_sh1                  # 3.2133

v8_r_debt_pre = 0.12
v8_r_debt_at = v8_r_debt_pre * (1.0 - v8_t)  # 9.00%
v8_ni_y = v8_ni0 - v8_buy_amt * v8_r_debt_at # 60 - 6.48 = 53.52M
v8_eps_y = v8_ni_y / v8_sh1                  # 2.9733

v8_bv1 = v8_bv0 - v8_buy_amt                 # 408.0M
v8_bvps1 = v8_bv1 / v8_sh1                   # 22.6667

v8_div_ps = v8_buy_amt / v8_sh0              # 3.60
v8_p_ex_div = v8_p0 - v8_div_ps              # 32.40

V8_TEXT = (
    "Titan Logistics reports trailing Net Income of USD 60.0 million, 20.0 million shares outstanding (EPS = USD 3.00), "
    "a share price of USD 36.00 (P/E = 12.0x; earnings yield $E/P = 8.33\\%$), and book value of equity of USD 480.0 million "
    "(BVPS = USD 24.00). The company's marginal corporate tax rate is 25%. Management evaluates returning USD 72.0 million "
    "to shareholders via open-market repurchases at USD 36.00/share (retiring 2.0 million shares) under two financing options, "
    "plus a third equivalent cash dividend alternative:\n"
    "- **Plan X (Cash-Funded Buyback):** Use USD 72.0 million of excess cash currently earning 4.00% pre-tax interest.\n"
    "- **Plan Y (Debt-Funded Buyback):** Issue USD 72.0 million of new bonds at a 12.00% pre-tax borrowing cost.\n"
    "- **Plan Z (Special Cash Dividend):** Pay USD 72.0 million as a one-time cash dividend instead of repurchasing shares."
)

# Q1: Plan X cash buyback EPS
wrong_no_int_x_v8 = v8_ni0 / v8_sh1  # 60/18 = 3.333
wrong_pretax_x_v8 = (v8_ni0 - v8_buy_amt * v8_r_cash_pre) / v8_sh1
add_q2(
    "L2-CRP-V08-Q1", V8_MOD, V8_TOP, V8_SUB, V8_ID, V8_TITLE, V8_TEXT,
    "Evaluate EPS accretion or dilution from a cash-funded share repurchase.",
    "Under Plan X (Cash-Funded Buyback), Titan Logistics's post-repurchase pro forma EPS is closest to:",
    f"USD {v8_eps_x:.2f} (accretive by +USD {v8_eps_x - v8_eps0:.2f}/share)",
    f"USD {wrong_no_int_x_v8:.2f} (accretive by +USD {wrong_no_int_x_v8 - v8_eps0:.2f}/share)",
    "Reduces share count to 18.0M but ignores the USD 2.16M foregone after-tax interest income on the USD 72.0M cash spent.",
    f"USD {wrong_pretax_x_v8:.2f} (accretive by +USD {wrong_pretax_x_v8 - v8_eps0:.2f}/share)",
    "Deducts pre-tax interest (4.00%) rather than after-tax foregone interest ($4.00\\%(1 - 0.25) = 3.00\\%$).",
    rf"Foregone after-tax cash interest is $72.0 \times 4.00\%(1 - 0.25) = \text{{USD }}2.16\text{{M}}$, yielding revised Net Income of $60.0 - 2.16 = \text{{USD }}57.84\text{{M}}$. "
    rf"Because Titan's earnings yield ($8.33\%$) exceeds the after-tax yield on cash ($3.00\%$), the buyback is accretive: "
    rf"$$\text{{EPS}}_X = \frac{{57.84}}{{20.0 - 2.0}} = \text{{USD }}{v8_eps_x:.2f}$$",
    True,
)

# Q2: Plan Y debt buyback EPS
wrong_pretax_y_v8 = (v8_ni0 - v8_buy_amt * v8_r_debt_pre) / v8_sh1
wrong_no_tax_check_v8 = v8_ni0 / v8_sh1
add_q2(
    "L2-CRP-V08-Q2", V8_MOD, V8_TOP, V8_SUB, V8_ID, V8_TITLE, V8_TEXT,
    "Evaluate EPS accretion or dilution from a debt-funded share repurchase.",
    "Under Plan Y (Debt-Funded Buyback at 12.00% pre-tax borrowing cost), Titan's pro forma EPS becomes:",
    f"USD {v8_eps_y:.2f} (dilutive by -USD {v8_eps0 - v8_eps_y:.2f}/share)",
    f"USD {wrong_pretax_y_v8:.2f} (dilutive by -USD {v8_eps0 - wrong_pretax_y_v8:.2f}/share)",
    "Subtracts pre-tax debt interest (USD 8.64M) without recognizing the 25% corporate tax shield (USD 6.48M after-tax interest).",
    f"USD {wrong_no_tax_check_v8:.2f} (accretive by +USD {wrong_no_tax_check_v8 - v8_eps0:.2f}/share)",
    "Divides pre-buyback Net Income by 18.0M shares without subtracting incremental after-tax interest expense.",
    rf"After-tax borrowing cost is $12.00\%(1 - 0.25) = 9.00\%$, which exceeds Titan's earnings yield ($E/P = 8.33\%$), making the buyback dilutive. "
    rf"Incremental after-tax interest equals $72.0 \times 9.00\% = \text{{USD }}6.48\text{{M}}$: "
    rf"$$\text{{EPS}}_Y = \frac{{60.00 - 6.48}}{{18.0}} = \frac{{53.52}}{{18.0}} = \text{{USD }}{v8_eps_y:.2f}$$",
    True,
)

# Q3: BVPS impact
wrong_bv_same_v8 = v8_bvps0
wrong_bv_up_v8 = v8_bv0 / v8_sh1
add_q2(
    "L2-CRP-V08-Q3", V8_MOD, V8_TOP, V8_SUB, V8_ID, V8_TITLE, V8_TEXT,
    "Analyze how share repurchases affect book value per share relative to market price-to-book.",
    "Under Plan X (repurchasing 2.0 million shares at USD 36.00/share), what happens to Titan Logistics's Book Value Per Share (BVPS)?",
    f"BVPS decreases from USD {v8_bvps0:.2f} to USD {v8_bvps1:.2f} because repurchase price exceeds initial BVPS.",
    f"BVPS increases from USD {v8_bvps0:.2f} to USD {wrong_bv_up_v8:.2f} because shares outstanding fall.",
    "Reduces share count in the denominator without subtracting the USD 72.0M treasury stock repurchase from shareholders' equity.",
    f"BVPS remains unchanged at USD {wrong_bv_same_v8:.2f} because book equity and market capitalization drop proportionally.",
    "Market price (USD 36.00) exceeds book value per share (USD 24.00), so retiring shares at $1.5\\times$ book value dilutes remaining BVPS.",
    rf"Share repurchases reduce book equity by the full cash outlay: $\text{{New BV}} = 480.0 - 72.0 = \text{{USD }}408.0\text{{M}}$. "
    rf"$$\text{{BVPS}}_1 = \frac{{408.0}}{{18.0}} = \text{{USD }}{v8_bvps1:.2f}$$ "
    rf"Because $P_{{\text{{buyback}}}} (\text{{USD }}36.00) > \text{{BVPS}}_0 (\text{{USD }}24.00)$, BVPS declines by USD {v8_bvps0 - v8_bvps1:.2f}/share.",
    True,
)

# Q4: Wealth equivalence vs cash dividend (Plan Z)
add_q2(
    "L2-CRP-V08-Q4", V8_MOD, V8_TOP, V8_SUB, V8_ID, V8_TITLE, V8_TEXT,
    "Demonstrate shareholder wealth equivalence between share repurchases and cash dividends in frictionless markets.",
    "In a frictionless market (zero taxes and transaction costs), suppose a shareholder owns 100 shares of Titan Logistics before payout. Comparing Plan X (buyback at USD 36.00) against Plan Z (special cash dividend), under Plan Z the shareholder holds:",
    f"100 shares worth USD {v8_p_ex_div:.2f}/share plus USD {100*v8_div_ps:,.0f} cash (total wealth = USD 3,600, identical to Plan X).",
    f"100 shares worth USD {v8_p0:.2f}/share plus USD {100*v8_div_ps:,.0f} cash (total wealth = USD {100*(v8_p0+v8_div_ps):,.0f}).",
    "Fails to adjust the ex-dividend share price downward by the USD 3.60/share cash distribution.",
    f"90 shares worth USD {v8_p0:.2f}/share plus USD {100*v8_div_ps:,.0f} cash (total wealth = USD 3,600).",
    "Describes tendering 10% of shares into the Plan X buyback rather than receiving the Plan Z cash dividend across all 100 shares.",
    rf"Under Plan Z, the dividend per share is $\text{{USD }}72\text{{M}} / 20\text{{M}} = \text{{USD }}{v8_div_ps:.2f}$, lowering ex-dividend share price to $36.00 - 3.60 = \text{{USD }}{v8_p_ex_div:.2f}$. "
    rf"Total shareholder wealth equals $100(\text{{USD }}32.40) + 100(\text{{USD }}3.60) = \text{{USD }}3,600$, identical to holding 100 shares at USD 36.00 (or tendering 10 shares for USD 360 + 90 shares worth USD 3,240) under Plan X.",
    True,
)

# Q5: Conceptual buyback signaling & EPS illusion
add_q2(
    "L2-CRP-V08-Q5", V8_MOD, V8_TOP, V8_SUB, V8_ID, V8_TITLE, V8_TEXT,
    "Explain why share repurchase EPS accretion alone does not create economic value and compare repurchase execution mechanisms.",
    "Which statement most accurately evaluates Titan Logistics's Plan X cash-funded repurchase from a corporate valuation perspective?",
    "Although Plan X boosts EPS by +7.1%, EPS accretion alone creates zero intrinsic wealth unless the shares are purchased below intrinsic value or tax/signaling benefits exist.",
    "Plan X automatically increases Titan's intrinsic enterprise value because equity shrinks while ROE and EPS rise.",
    "Spending cash earning 3% alters leverage and cuts share count (boosting mechanical EPS), but paying fair market price USD 36.00 yields zero NPV unless shares are undervalued.",
    "Open-market buybacks send a stronger positive valuation signal than fixed-price tender offers at a premium.",
    "Fixed-price tender offers commit to buying a large block at an explicit premium, conveying a far stronger undervaluation signal than flexible open-market authorizations.",
    "Repurchasing shares at fair market value transfers cash for equity at zero NPV: mechanical EPS accretion arises purely because the firm exchanges low-yield cash (3%) for higher-yield equity (8.33%), which simultaneously increases operating risk per remaining share and leaves total shareholder wealth unchanged unless shares were undervalued.",
    False,
)

# =============================================================================
# LEVEL 2: VIGNETTE 9 — M&A VALUATION, EXCHANGE RATIO & DEAL SPLIT (CRP-V09)
# =============================================================================
V9_ID = "CRP-V09"
V9_MOD = "CI-L2-M9"
V9_TOP = "Mergers & Acquisitions"
V9_SUB = "Target Valuation, Exchange Ratio & Merger Gains"
V9_TITLE = "Orion Tech & NovaSoft — All-Cash vs. Stock-Swap Terms"

v9_pa, v9_na = 60.0, 50.0
v9_va = v9_pa * v9_na               # 3,000M
v9_pt, v9_nt = 25.0, 20.0
v9_vt = v9_pt * v9_nt               # 500M
v9_syn = 140.0
v9_v_comb = v9_va + v9_vt + v9_syn  # 3,640M

v9_max_pt = (v9_vt + v9_syn) / v9_nt  # 32.00
v9_max_er = v9_max_pt / v9_pa         # 0.5333

v9_cash_p = 30.0
v9_cash_tot = v9_cash_p * v9_nt     # 600M
v9_cash_prem = v9_cash_tot - v9_vt  # 100M
v9_cash_npv_a = v9_syn - v9_cash_prem  # +40M
v9_cash_pa_post = v9_pa + v9_cash_npv_a / v9_na  # 60.80

v9_er = 0.50
v9_new_sh = v9_er * v9_nt           # 10.0M
v9_tot_sh = v9_na + v9_new_sh       # 60.0M
v9_wt_tgt = v9_new_sh / v9_tot_sh   # 16.6667%
v9_p_post_stk = v9_v_comb / v9_tot_sh  # 60.6667
v9_val_tgt_stk = v9_wt_tgt * v9_v_comb # 606.6667M
v9_tgt_gain_stk = v9_val_tgt_stk - v9_vt # 106.67M
v9_acq_npv_stk = v9_syn - v9_tgt_gain_stk # 33.33M

# Minimum ER acceptable to target shareholders: w_T * V_comb = V_T -> N_new = (V_T * N_A) / (V_comb - V_T)
v9_min_new_sh = (v9_vt * v9_na) / (v9_v_comb - v9_vt)  # 25000 / 3140 = 7.96178M
v9_min_er = v9_min_new_sh / v9_nt                       # 0.3981

V9_TEXT = (
    "Orion Tech (Acquirer) is negotiating to acquire 100% of NovaSoft (Target). Standalone pre-announcement data are:\n\n"
    "| Metric | Orion Tech (Acquirer) | NovaSoft (Target) |\n"
    "| :--- | :---: | :---: |\n"
    "| Pre-Merger Share Price | USD 60.00 | USD 25.00 |\n"
    "| Diluted Shares Outstanding | 50.0 million | 20.0 million |\n"
    "| Standalone Equity Value | USD 3,000.0 million | USD 500.0 million |\n\n"
    "Investment bankers estimate the present value of net cost and revenue synergies at USD 140.0 million. Orion evaluates "
    "two competing bid structures: **Proposal 1 (All-Cash)** at USD 30.00 per NovaSoft share, and **Proposal 2 (All-Stock)** "
    "at a fixed exchange ratio of 0.50 Orion shares per NovaSoft share."
)

# Q1: Max price & max ER
wrong_no_syn_p_v9 = v9_vt / v9_nt
wrong_no_syn_er_v9 = wrong_no_syn_p_v9 / v9_pa
add_q2(
    "L2-CRP-V09-Q1", V9_MOD, V9_TOP, V9_SUB, V9_ID, V9_TITLE, V9_TEXT,
    "Determine maximum target offer prices and exchange ratios in M&A negotiations.",
    "What is the maximum offer price per NovaSoft share—and corresponding maximum stock exchange ratio—Orion can pay without destroying value for Orion's existing shareholders?",
    f"USD {v9_max_pt:.2f}/share (max exchange ratio = {v9_max_er:.4f})",
    f"USD {wrong_no_syn_p_v9:.2f}/share (max exchange ratio = {wrong_no_syn_er_v9:.4f})",
    "Ignores the USD 140.0M PV of synergies, setting maximum offer price equal to NovaSoft's standalone USD 25.00 share price.",
    f"USD {v9_max_pt + 2.50:.2f}/share (max exchange ratio = {(v9_max_pt+2.50)/v9_pa:.4f})",
    "Adds synergies per share using an erroneous share divisor rather than dividing USD 140.0M across 20.0M target shares (USD 7.00/share).",
    rf"Maximum value Orion can pay equals NovaSoft's standalone equity value plus full synergy PV: "
    rf"$$P_{{T,\max}} = \frac{{V_T + \text{{PV}}(\text{{Synergies}})}}{{N_T}} = \frac{{500 + 140}}{{20}} = \text{{USD }}{v9_max_pt:.2f}/\text{{share}}$$ "
    rf"Dividing by Orion's pre-merger share price gives $\text{{ER}}_{{\max}} = 32.00 / 60.00 = {v9_max_er:.4f}$.",
    True,
)

# Q2: All-Cash Offer Acquirer NPV & Post-Merger Share Price
wrong_cash_gross_v9 = v9_pa + v9_syn / v9_na
add_q2(
    "L2-CRP-V09-Q2", V9_MOD, V9_TOP, V9_SUB, V9_ID, V9_TITLE, V9_TEXT,
    "Calculate acquirer NPV and post-merger share price under an all-cash acquisition.",
    "Under Proposal 1 (All-Cash at USD 30.00/share), what are Orion Tech's acquisition NPV and expected post-merger share price?",
    f"Acquirer NPV = +USD {v9_cash_npv_a:.1f}M; post-merger price = USD {v9_cash_pa_post:.2f}",
    f"Acquirer NPV = +USD {v9_syn:.1f}M; post-merger price = USD {wrong_cash_gross_v9:.2f}",
    "Credits Orion with all USD 140.0M of synergies without subtracting the USD 100.0M takeover premium paid to NovaSoft.",
    f"Acquirer NPV = -USD {v9_cash_prem:.1f}M; post-merger price = USD {v9_pa - v9_cash_prem/v9_na:.2f}",
    "Treats the USD 100.0M takeover premium as a pure loss while ignoring the USD 140.0M synergy PV.",
    rf"Total cash paid is $20.0\text{{M}} \times \text{{USD }}30.00 = \text{{USD }}600.0\text{{M}}$, representing a USD 100.0M premium over NovaSoft's USD 500.0M standalone value. "
    rf"Acquirer NPV equals $\text{{Synergies}} - \text{{Premium}} = 140.0 - 100.0 = +\text{{USD }}{v9_cash_npv_a:.1f}\text{{M}}$. "
    rf"Post-merger share price is $60.00 + (40.0 / 50.0) = \text{{USD }}{v9_cash_pa_post:.2f}$.",
    True,
)

# Q3: All-Stock Offer actual value transferred & Acquirer NPV
add_q2(
    "L2-CRP-V09-Q3", V9_MOD, V9_TOP, V9_SUB, V9_ID, V9_TITLE, V9_TEXT,
    "Determine post-merger ownership shares and actual value split in stock-for-stock acquisitions.",
    "Under Proposal 2 (All-Stock at $\\text{ER} = 0.50$), what percentage of the combined company will NovaSoft shareholders own, and what is Orion Tech's actual net acquisition NPV?",
    f"Target ownership = {v9_wt_tgt*100:.2f}%; Acquirer NPV = +USD {v9_acq_npv_stk:.2f}M",
    f"Target ownership = {v9_wt_tgt*100:.2f}%; Acquirer NPV = +USD {v9_cash_npv_a:.2f}M",
    "Assumes stock payment costs exactly $0.50 \\times 60 = \\text{USD }30.00/\\text{share}$ (USD 600M), overlooking that Target shareholders claim 16.67% of the USD 140M post-merger synergies.",
    f"Target ownership = {(v9_new_sh/v9_na)*100:.2f}%; Acquirer NPV = +USD {v9_acq_npv_stk:.2f}M",
    "Divides new shares issued (10M) by Orion's standalone shares (50M) instead of combined post-merger shares (60M).",
    rf"Orion issues $0.50 \times 20.0\text{{M}} = 10.0\text{{M}}$ new shares, yielding 60.0M total shares. Target ownership is $10 / 60 = {v9_wt_tgt*100:.2f}\%$. "
    rf"Combined value equals $3,000 + 500 + 140 = \text{{USD }}3,640\text{{M}}$ (USD {v9_p_post_stk:.2f}/share). "
    rf"NovaSoft receives $\frac{{1}}{{6}} \times 3,640 = \text{{USD }}{v9_val_tgt_stk:.2f}\text{{M}}$ (a USD {v9_tgt_gain_stk:.2f}M gain), leaving Orion with $\text{{NPV}}_A = 140.00 - {v9_tgt_gain_stk:.2f} = +\text{{USD }}{v9_acq_npv_stk:.2f}\text{{ million}}$.",
    True,
)

# Q4: Minimum ER acceptable to target shareholders
wrong_min_pre_v9 = v9_pt / v9_pa  # 25/60 = 0.4167
wrong_min_post_naive_v9 = (v9_vt / (v9_va + v9_vt)) * (v9_na / v9_nt)
add_q2(
    "L2-CRP-V09-Q4", V9_MOD, V9_TOP, V9_SUB, V9_ID, V9_TITLE, V9_TEXT,
    "Calculate the minimum exchange ratio required to preserve target shareholder value in a stock merger.",
    "What is the minimum stock exchange ratio (Orion shares per NovaSoft share) that leaves NovaSoft shareholders just as well off as remaining standalone (Target gain = USD 0, assuming synergies of USD 140.0 million materialize)?",
    f"{v9_min_er:.4f}",
    f"{wrong_min_pre_v9:.4f}",
    "Computes the pre-merger share price ratio ($25 / 60 = 0.4167$), ignoring that NovaSoft shares receive an ownership slice of the USD 140.0M synergy upside.",
    f"{v9_max_er:.4f}",
    "Reports the maximum exchange ratio acceptable to Orion (0.5333) rather than the minimum exchange ratio acceptable to NovaSoft.",
    rf"NovaSoft breaks even when its ownership share $w_T$ of combined firm value (USD 3,640M) equals its USD 500M standalone value: "
    rf"$$\frac{{N_{{\text{{new}}}}}}{{50 + N_{{\text{{new}}}}}}(3,640) = 500 \implies N_{{\text{{new}}}} = \frac{{25,000}}{{3,140}} = {v9_min_new_sh:.4f}\text{{M shares}}$$ "
    rf"Dividing by 20.0M Target shares gives $\text{{ER}}_{{\min}} = {v9_min_er:.4f}$.",
    True,
)

# Q5: Conceptual cash vs stock
add_q2(
    "L2-CRP-V09-Q5", V9_MOD, V9_TOP, V9_SUB, V9_ID, V9_TITLE, V9_TEXT,
    "Evaluate strategic incentives governing cash versus stock consideration in M&A.",
    "Why would Orion Tech's management prefer Proposal 2 (All-Stock) over Proposal 1 (All-Cash) if management privately doubts whether the full USD 140.0 million in synergies will materialize and believes Orion shares are currently overvalued?",
    "Stock payment shares synergy-realization risk proportionally with NovaSoft shareholders and uses overvalued acquirer equity as cheap acquisition currency.",
    "Stock payment guarantees NovaSoft shareholders a fixed USD 30.00/share floor regardless of post-merger integration failures.",
    "A fixed exchange ratio ties Target proceeds to post-merger combined stock performance rather than fixing a cash floor.",
    "All-stock mergers maximize post-merger financial leverage and interest tax shields.",
    "Cash bids funded with debt increase financial leverage and tax shields, whereas all-stock bids preserve debt capacity.",
    "When acquirer shares are richly valued or synergy realization is highly uncertain, paying in stock shifts part of any integration shortfall onto target shareholders (via their 16.67% stake) and avoids depleting cash or issuing debt.",
    False,
)

# =============================================================================
# LEVEL 2: VIGNETTE 10 — POST-MERGER EPS, BREAKEVEN SYNERGIES & SPIN-OFFS (CRP-V10)
# =============================================================================
V10_ID = "CRP-V10"
V10_MOD = "CI-L2-M10"
V10_TOP = "Mergers, Acquisitions & Restructuring"
V10_SUB = "EPS Accretion/Dilution, Breakeven Synergies & Spin-Offs"
V10_TITLE = "Apex Pharma — BioCore Acquisition & Generics Spin-Off"

v10_ea, v10_na, v10_pa = 300.0, 100.0, 75.0    # EPS_A = 3.00, P/E = 25
v10_et, v10_nt, v10_pt = 60.0, 40.0, 22.50     # EPS_T = 1.50, P/E = 15
v10_eps_a = v10_ea / v10_na
v10_offer_stk = 30.0                           # ER = 0.40 -> 16M new shares -> 116M tot
v10_er = v10_offer_stk / v10_pa
v10_new_sh = v10_er * v10_nt
v10_tot_sh = v10_na + v10_new_sh               # 116M

v10_eps_no_syn = (v10_ea + v10_et) / v10_tot_sh  # 360 / 116 = 3.1034
v10_acc_no_syn = (v10_eps_no_syn / v10_eps_a - 1.0) * 100.0

v10_syn_pre, v10_da_pre, v10_t = 24.0, 20.0, 0.25
v10_syn_at = v10_syn_pre * (1.0 - v10_t)       # 18.0M
v10_da_at = v10_da_pre * (1.0 - v10_t)         # 15.0M
v10_ni_comb = v10_ea + v10_et + v10_syn_at - v10_da_at  # 363.0M
v10_eps_syn = v10_ni_comb / v10_tot_sh         # 363 / 116 = 3.1293
v10_acc_syn = (v10_eps_syn / v10_eps_a - 1.0) * 100.0

# Competing All-Cash Offer at USD 36/share = 1,440M debt at 6% pre-tax, 25% tax -> AT interest = 64.8M, plus AT DA = 15.0M
v10_cash_offer = 36.0 * v10_nt                 # 1,440M
v10_kd = 0.06
v10_int_at = v10_cash_offer * v10_kd * (1.0 - v10_t)  # 64.80M
# Need E_A + E_T + Syn_AT - Int_AT - DA_AT = EPS_A * N_A = 300M
v10_req_syn_at = v10_ea - (v10_ea + v10_et - v10_int_at - v10_da_at)  # 19.80M
v10_req_syn_pre = v10_req_syn_at / (1.0 - v10_t)                      # 26.40M

# Spin-off SOTP
v10_ebitda_core, v10_mult_core = 450.0, 14.0   # 6,300M
v10_ebitda_gen, v10_mult_gen = 150.0, 8.0      # 1,200M
v10_net_debt, v10_disc = 900.0, 0.15
v10_sotp_ev = v10_ebitda_core * v10_mult_core + v10_ebitda_gen * v10_mult_gen  # 7,500M
v10_sotp_eq = v10_sotp_ev - v10_net_debt       # 6,600M -> 66.00/sh
v10_sotp_ps = v10_sotp_eq / v10_na             # 66.00
v10_curr_ps = v10_sotp_ps * (1.0 - v10_disc)   # 56.10
v10_uplift_ps = v10_sotp_ps - v10_curr_ps      # 9.90

V10_TEXT = (
    "Apex Pharma (standalone Net Income = USD 300.0M, 100.0M shares, EPS = USD 3.00, share price = USD 75.00, P/E = 25.0x, "
    "tax rate = 25%) evaluates acquiring BioCore Labs (standalone Net Income = USD 60.0M, 40.0M shares, EPS = USD 1.50, "
    "share price = USD 22.50, P/E = 15.0x). Apex considers two deal options:\n"
    "- **Deal Option 1 (All-Stock):** Exchange ratio of 0.40 Apex shares per BioCore share (implied offer USD 30.00/share). "
    "Management models USD 24.0M in annual pre-tax cost synergies and USD 20.0M in annual pre-tax incremental depreciation & "
    "amortization (D&A) from writing up BioCore's intangible assets.\n"
    "- **Deal Option 2 (Debt-Funded All-Cash):** Offer USD 36.00/share in cash (USD 1,440.0M total) financed entirely with new "
    "senior debt yielding 6.00% pre-tax, carrying the same USD 20.0M annual pre-tax incremental D&A.\n\n"
    "Separately, Apex studies spinning off its Legacy Generics segment (EBITDA = USD 150.0M, pure-play peer EV/EBITDA = 8.0x) "
    "from Core Specialty Pharma (EBITDA = USD 450.0M, peer EV/EBITDA = 14.0x). Corporate net debt is USD 900.0M (100.0M Apex shares), "
    "and analysts estimate the consolidated conglomerate currently trades at a 15% sum-of-the-parts (SOTP) equity discount."
)

# Q1: Stock deal EPS without synergies or D&A
wrong_avg_eps_v10 = (v10_ea + v10_et) / (v10_na + v10_nt)
wrong_no_newsh_v10 = (v10_ea + v10_et) / v10_na
add_q2(
    "L2-CRP-V10-Q1", V10_MOD, V10_TOP, V10_SUB, V10_ID, V10_TITLE, V10_TEXT,
    "Calculate pro forma post-merger EPS accretion from P/E bootstrapping.",
    "Under Deal Option 1 (All-Stock at $\\text{ER} = 0.40$), assuming zero synergies and zero incremental D&A, Apex Pharma's pro forma combined EPS and accretion/dilution percentage are closest to:",
    f"USD {v10_eps_no_syn:.2f} (+{v10_acc_no_syn:.2f}% accretive)",
    f"USD {wrong_avg_eps_v10:.2f} ({(wrong_avg_eps_v10/v10_eps_a-1)*100:.2f}% dilutive)",
    "Adds BioCore's full 40.0M standalone shares directly to Apex's 100.0M shares without multiplying by the 0.40 exchange ratio.",
    f"USD {wrong_no_newsh_v10:.2f} (+{(wrong_no_newsh_v10/v10_eps_a-1)*100:.2f}% accretive)",
    "Adds BioCore's USD 60.0M earnings while omitting the 16.0M new Apex shares issued to BioCore shareholders.",
    rf"Apex issues $0.40 \times 40.0\text{{M}} = 16.0\text{{M}}$ new shares, raising total shares to 116.0M. Combined earnings equal $300 + 60 = \text{{USD }}360.0\text{{M}}$: "
    rf"$$\text{{EPS}}_{{\text{{merged}}}} = \frac{{360.0}}{{116.0}} = \text{{USD }}{v10_eps_no_syn:.3f} \quad \left(\frac{{3.1034}}{{3.00}} - 1 = +{v10_acc_no_syn:.2f}\%\right)$$ "
    rf"Because Apex's P/E (25.0x) exceeds the effective offer P/E ($30 / 1.50 = 20.0\text{{x}}$), the deal is mechanically accretive.",
    True,
)

# Q2: Stock deal EPS WITH synergies and incremental D&A
wrong_pretax_adj_v10 = (v10_ea + v10_et + v10_syn_pre - v10_da_pre) / v10_tot_sh
wrong_no_da_v10 = (v10_ea + v10_et + v10_syn_at) / v10_tot_sh
add_q2(
    "L2-CRP-V10-Q2", V10_MOD, V10_TOP, V10_SUB, V10_ID, V10_TITLE, V10_TEXT,
    "Incorporate after-tax synergies and purchase-accounting D&A step-ups into post-merger EPS.",
    "Incorporating Deal Option 1's USD 24.0M annual pre-tax synergies and USD 20.0M annual pre-tax incremental D&A (at a 25% tax rate), Apex's pro forma EPS is closest to:",
    f"USD {v10_eps_syn:.3f} (+{v10_acc_syn:.2f}% accretive)",
    f"USD {wrong_no_da_v10:.3f} (+{(wrong_no_da_v10/v10_eps_a-1)*100:.2f}% accretive)",
    "Includes the USD 18.0M after-tax synergies but omits the USD 15.0M after-tax incremental D&A expense.",
    f"USD {wrong_pretax_adj_v10:.3f} (+{(wrong_pretax_adj_v10/v10_eps_a-1)*100:.2f}% accretive)",
    "Fails to apply the $(1 - 0.25)$ tax rate to the net USD 4.0M pre-tax adjustment ($+24 - 20$).",
    rf"After-tax synergies equal $24.0(1 - 0.25) = +\text{{USD }}18.0\text{{M}}$ and after-tax incremental D&A equals $20.0(1 - 0.25) = -\text{{USD }}15.0\text{{M}}$. "
    rf"Combined Net Income $= 300.0 + 60.0 + 18.0 - 15.0 = \text{{USD }}363.0\text{{M}}$: "
    rf"$$\text{{EPS}}_{{\text{{merged}}}} = \frac{{363.0}}{{116.0}} = \text{{USD }}{v10_eps_syn:.3f} \quad (+{v10_acc_syn:.2f}\%)$$",
    True,
)

# Q3: Breakeven pre-tax synergies under Deal Option 2 (Cash/Debt)
wrong_at_syn_v10 = v10_req_syn_at
wrong_no_da_syn_v10 = (v10_int_at - v10_et) / (1.0 - v10_t)
add_q2(
    "L2-CRP-V10-Q3", V10_MOD, V10_TOP, V10_SUB, V10_ID, V10_TITLE, V10_TEXT,
    "Solve for breakeven annual pre-tax synergies required to avoid EPS dilution in debt-financed deals.",
    "Under Deal Option 2 (Debt-Funded All-Cash at USD 36.00/share with 6.00% pre-tax borrowing cost and USD 20.0M pre-tax incremental D&A), what annual **pre-tax** synergies are required for Apex's post-merger EPS to break even at USD 3.00?",
    f"USD {v10_req_syn_pre:.2f} million",
    f"USD {wrong_at_syn_v10:.2f} million",
    "Reports the required after-tax synergy earnings (USD 19.80M) instead of grossing up by $(1 - 0.25)$ to pre-tax synergies.",
    f"USD {wrong_no_da_syn_v10:.2f} million",
    "Accounts for interest expense and BioCore earnings while omitting the USD 20.0M pre-tax incremental D&A charge.",
    rf"Debt equals $40.0\text{{M}} \times \text{{USD }}36.00 = \text{{USD }}1,440.0\text{{M}}$, incurring after-tax interest of $1,440(0.06)(0.75) = \text{{USD }}64.80\text{{M}}$ and after-tax D&A of $20(0.75) = \text{{USD }}15.00\text{{M}}$. "
    rf"With 100.0M shares unchanged, breakeven Net Income is USD 300.0M. Without synergies, $\text{{NI}} = 300 + 60 - 64.80 - 15.00 = \text{{USD }}280.20\text{{M}}$, leaving an after-tax shortfall of USD {v10_req_syn_at:.2f}M: "
    rf"$$\text{{Breakeven Pre-Tax Synergies}} = \frac{{19.80}}{{1 - 0.25}} = \text{{USD }}{v10_req_syn_pre:.2f}\text{{ million}}$$",
    True,
)

# Q4: Spin-off SOTP valuation uplift
wrong_no_debt_disc_v10 = (v10_sotp_ev / v10_na) * v10_disc
wrong_tot_uplift_v10 = v10_sotp_ps
add_q2(
    "L2-CRP-V10-Q4", V10_MOD, V10_TOP, V10_SUB, V10_ID, V10_TITLE, V10_TEXT,
    "Perform sum-of-the-parts valuation to quantify conglomerate discount removal in corporate spin-offs.",
    "Using the peer EV/EBITDA multiples, if spinning off Legacy Generics completely eliminates Apex's 15% SOTP conglomerate equity discount, the expected per-share equity value uplift is closest to:",
    f"USD {v10_uplift_ps:.2f}/share",
    f"USD {wrong_no_debt_disc_v10:.2f}/share",
    "Applies the 15% conglomerate discount to total enterprise value (USD 7,500M) instead of equity value after deducting USD 900M net debt.",
    f"USD {wrong_tot_uplift_v10:.2f}/share",
    "Reports the full standalone SOTP equity value per share (USD 66.00) rather than the incremental USD 9.90/share uplift.",
    rf"Sum-of-the-parts EV is $(450 \times 14) + (150 \times 8) = 6,300 + 1,200 = \text{{USD }}7,500\text{{M}}$. "
    rf"Subtracting USD 900M net debt yields SOTP equity value of $\text{{USD }}6,600\text{{M}}$, or $\text{{USD }}{v10_sotp_ps:.2f}/\text{{share}}$. "
    rf"With a 15% discount, current price is $66.00(0.85) = \text{{USD }}{v10_curr_ps:.2f}/\text{{share}}$, so eliminating the discount unlocks $66.00 - 56.10 = \text{{USD }}{v10_uplift_ps:.2f}/\text{{share}}$.",
    True,
)

# Q5: Spin-off vs Equity Carve-out vs Split-off
add_q2(
    "L2-CRP-V10-Q5", V10_MOD, V10_TOP, V10_SUB, V10_ID, V10_TITLE, V10_TEXT,
    "Contrast corporate spin-offs, equity carve-outs, and split-offs.",
    "How does a pure pro rata corporate spin-off of Legacy Generics differ structurally from an equity carve-out?",
    "A spin-off distributes subsidiary shares tax-free to existing parent shareholders without raising new cash proceeds, whereas an equity carve-out sells a minority stake via IPO to raise cash.",
    "A spin-off raises immediate cash proceeds for the parent via an IPO while retaining >80% voting control.",
    "Describes an equity carve-out, not a spin-off; spin-offs distribute shares directly to existing shareholders with zero cash inflow.",
    "A spin-off requires existing parent shareholders to surrender parent stock in exchange for subsidiary stock.",
    "Surrendering parent shares to receive subsidiary shares defines a split-off, whereas a spin-off distributes shares pro rata without surrendering parent stock.",
    "In a spin-off, the parent distributes 100% (or >80%) of subsidiary shares pro rata to existing shareholders—typically tax-free—generating no cash proceeds and creating an independent company. An equity carve-out IPOs a subsidiary stake to outside investors to raise cash.",
    False,
)


# =============================================================================
# FINAL VALIDATION & SAVE
# =============================================================================
assert len(questions) == 130, f"Expected 130 questions, got {len(questions)}"
l1_count = sum(1 for q in questions if q["level"] == 1)
l2_count = sum(1 for q in questions if q["level"] == 2)
calc_count = sum(1 for f in calc_flags if f)
calc_pct = calc_count / len(questions) * 100.0
assert l1_count == 80, f"Expected 80 L1 questions, got {l1_count}"
assert l2_count == 50, f"Expected 50 L2 questions, got {l2_count}"
assert calc_pct >= 65.0, f"Calculation ratio {calc_pct:.1f}% < 65%"
assert_no_control_escapes(questions)

ans_dist = {k: sum(1 for q in questions if q["answer"] == k) for k in ("A", "B", "C")}
output_file = os.path.join(ROOT_DIR, "data", "courses", "corp_qbank.json")
save_validated_json(questions, output_file)
print(
    f"Summary: total={len(questions)} (L1={l1_count}, L2={l2_count}), "
    f"numerical={calc_count}/{len(questions)} ({calc_pct:.1f}%), "
    f"answers={ans_dist}, errors=0"
)
