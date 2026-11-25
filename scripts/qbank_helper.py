"""
Shared schema, math, KaTeX, and currency validation helpers for CFA Master Suite.
"""
import json
import math
import os
import re

RE_DISPLAY = re.compile(r"\$\$.*?\$\$", re.DOTALL)
RE_INLINE = re.compile(r"(?<!\\)\$.*?(?<!\\)\$")


def check_text_compliance(text: str, label: str) -> list[str]:
    """Verify KaTeX delimiter parity and zero unescaped stray dollar signs."""
    errors = []
    if not text:
        return errors
    if text.count("$$") % 2 != 0:
        errors.append(f"{label}: Unbalanced $$ display math delimiters")
    cleaned = text.replace("$$", "").replace(r"\$", "")
    if cleaned.count("$") % 2 != 0:
        errors.append(f"{label}: Unbalanced $ inline math delimiters")
    no_disp = RE_DISPLAY.sub("", text)
    no_inl = RE_INLINE.sub("", no_disp)
    no_esc = no_inl.replace(r"\$", "")
    if "$" in no_esc:
        errors.append(f"{label}: Bare unescaped $ outside math block")
    return errors


def add_l1(
    out: list,
    qid: str,
    subject: str,
    module: str,
    topic: str,
    subtopic: str,
    los: str,
    question: str,
    options: dict,
    answer: str,
    explanation: str,
    distractors: dict,
):
    assert answer in ("A", "B", "C"), f"{qid}: Invalid answer {answer}"
    assert set(options.keys()) == {"A", "B", "C"}, f"{qid}: Invalid option keys"
    other_keys = [k for k in ("A", "B", "C") if k != answer]
    assert set(distractors.keys()) == set(other_keys), (
        f"{qid}: distractors must contain exact keys {other_keys}, got {list(distractors.keys())}"
    )
    errs = []
    for fld, val in [
        ("question", question),
        ("explanation", explanation),
        ("optA", options["A"]),
        ("optB", options["B"]),
        ("optC", options["C"]),
    ] + [(f"dist_{k}", distractors[k]) for k in other_keys]:
        errs.extend(check_text_compliance(val, f"{qid}.{fld}"))
    if errs:
        raise ValueError("\n".join(errs))

    out.append(
        {
            "id": qid,
            "level": 1,
            "module": module,
            "topic": topic,
            "subtopic": subtopic,
            "module_title": subtopic or topic,
            "subject": subject,
            "los": los,
            "question": question,
            "options": options,
            "answer": answer,
            "explanation": explanation,
            "distractor_analysis": {k: distractors[k] for k in other_keys},
        }
    )


def add_l2(
    out: list,
    qid: str,
    subject: str,
    module: str,
    topic: str,
    subtopic: str,
    vignette_id: str,
    global_vignette_id: str,
    vignette_title: str,
    vignette_text: str,
    los: str,
    question: str,
    options: dict,
    answer: str,
    explanation: str,
    distractors: dict,
):
    assert answer in ("A", "B", "C"), f"{qid}: Invalid answer {answer}"
    assert set(options.keys()) == {"A", "B", "C"}, f"{qid}: Invalid option keys"
    assert vignette_title and vignette_text, f"{qid}: Missing vignette content"
    other_keys = [k for k in ("A", "B", "C") if k != answer]
    assert set(distractors.keys()) == set(other_keys), (
        f"{qid}: distractors must contain exact keys {other_keys}, got {list(distractors.keys())}"
    )
    errs = []
    for fld, val in [
        ("vignette_text", vignette_text),
        ("question", question),
        ("explanation", explanation),
        ("optA", options["A"]),
        ("optB", options["B"]),
        ("optC", options["C"]),
    ] + [(f"dist_{k}", distractors[k]) for k in other_keys]:
        errs.extend(check_text_compliance(val, f"{qid}.{fld}"))
    if errs:
        raise ValueError("\n".join(errs))

    out.append(
        {
            "id": qid,
            "level": 2,
            "module": module,
            "topic": topic,
            "subtopic": subtopic,
            "module_title": subtopic or topic,
            "subject": subject,
            "vignette_id": vignette_id,
            "global_vignette_id": global_vignette_id,
            "vignette_title": vignette_title,
            "vignette_text": vignette_text,
            "los": los,
            "question": question,
            "options": options,
            "answer": answer,
            "explanation": explanation,
            "distractor_analysis": {k: distractors[k] for k in other_keys},
        }
    )


def save_validated_json(questions: list, output_path: str):
    seen = set()
    for q in questions:
        assert q["id"] not in seen, f"Duplicate ID: {q['id']}"
        seen.add(q["id"])
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(questions, f, indent=2, ensure_ascii=False)
    print(f"Saved {len(questions)} validated questions -> {output_path}")


def save_validated_html(html: str, output_path: str):
    errs = check_text_compliance(html, os.path.basename(output_path))
    if errs:
        raise ValueError("\n".join(errs[:10]))
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Saved {len(html)} bytes validated HTML -> {output_path}")


def norm_cdf(x: float) -> float:
    """Standard normal cumulative distribution function N(x)."""
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def norm_pdf(x: float) -> float:
    """Standard normal probability density function n(x)."""
    return math.exp(-0.5 * x * x) / math.sqrt(2.0 * math.pi)


def bsm_values(S: float, K: float, r: float, T: float, sigma: float, q: float = 0.0) -> dict:
    """Exact Black-Scholes-Merton prices and Greeks with continuous dividend yield q."""
    sqrtT = math.sqrt(T)
    d1 = (math.log(S / K) + (r - q + 0.5 * sigma * sigma) * T) / (sigma * sqrtT)
    d2 = d1 - sigma * sqrtT
    Nd1 = norm_cdf(d1)
    Nd2 = norm_cdf(d2)
    Nmd1 = norm_cdf(-d1)
    Nmd2 = norm_cdf(-d2)
    disc_q = math.exp(-q * T)
    disc_r = math.exp(-r * T)
    call = S * disc_q * Nd1 - K * disc_r * Nd2
    put = K * disc_r * Nmd2 - S * disc_q * Nmd1
    delta_c = disc_q * Nd1
    delta_p = disc_q * (Nd1 - 1.0)
    gamma = (disc_q * norm_pdf(d1)) / (S * sigma * sqrtT)
    vega = S * disc_q * norm_pdf(d1) * sqrtT
    return {
        "d1": d1,
        "d2": d2,
        "Nd1": Nd1,
        "Nd2": Nd2,
        "call": call,
        "put": put,
        "delta_c": delta_c,
        "delta_p": delta_p,
        "gamma": gamma,
        "vega": vega,
    }


def irr(cash_flows: list[float], guess: float = 0.1) -> float:
    """Solve IRR via damped Newton-Raphson + bisection fallback."""
    lo, hi = -0.99, 5.0
    def npv_at(rate: float) -> float:
        return sum(cf / ((1.0 + rate) ** t) for t, cf in enumerate(cash_flows))
    f_lo = npv_at(lo)
    for _ in range(120):
        mid = 0.5 * (lo + hi)
        f_mid = npv_at(mid)
        if abs(f_mid) < 1e-10:
            return mid
        if (f_lo > 0 and f_mid > 0) or (f_lo < 0 and f_mid < 0):
            lo, f_lo = mid, f_mid
        else:
            hi = mid
    return 0.5 * (lo + hi)
