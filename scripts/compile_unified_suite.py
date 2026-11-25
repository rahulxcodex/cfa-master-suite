import json
import os
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
FI_EQ_DIR = os.path.join(DATA_DIR, "fi_eq")
COURSES_DIR = os.path.join(DATA_DIR, "courses")
OUTPUT_MASTER = os.path.join(DATA_DIR, "cfa_master_855.json")
OUTPUT_MANIFEST = os.path.join(DATA_DIR, "suite_manifest.json")

FSA_FILES = [
    os.path.join(DATA_DIR, "l1_questions_part1.json"),
    os.path.join(DATA_DIR, "l1_questions_part2.json"),
    os.path.join(DATA_DIR, "l2_questions_part1.json"),
    os.path.join(DATA_DIR, "l2_questions_part2.json"),
    os.path.join(DATA_DIR, "l2_questions_part3.json"),
]

FI_EQ_FILES = [
    ("Fixed Income", os.path.join(FI_EQ_DIR, "l1_fixed_income.json")),
    ("Equity Investments", os.path.join(FI_EQ_DIR, "l1_equity.json")),
    ("Fixed Income", os.path.join(FI_EQ_DIR, "l2_fixed_income.json")),
    ("Equity Investments", os.path.join(FI_EQ_DIR, "l2_equity.json")),
    ("Portfolio Management", os.path.join(FI_EQ_DIR, "l1_portfolio_mgmt.json")),
    ("Portfolio Management", os.path.join(FI_EQ_DIR, "l2_portfolio_mgmt.json")),
]

COURSE_FILES = [
    ("Ethical and Professional Standards", "ETH", os.path.join(COURSES_DIR, "l1_ethics_part1.json")),
    ("Ethical and Professional Standards", "ETH", os.path.join(COURSES_DIR, "l1_ethics_part2.json")),
    ("Ethical and Professional Standards", "ETH", os.path.join(COURSES_DIR, "l2_ethics.json")),
    ("Quantitative Methods", "QM", os.path.join(COURSES_DIR, "qm_qbank.json")),
    ("Economics", "ECN", os.path.join(COURSES_DIR, "econ_qbank.json")),
    ("Corporate Issuers", "CRP", os.path.join(COURSES_DIR, "corp_qbank.json")),
    ("Derivatives", "DRV", os.path.join(COURSES_DIR, "deriv_qbank.json")),
    ("Alternative Investments", "ALT", os.path.join(COURSES_DIR, "alt_qbank.json")),
]

SUBJECT_ORDER = [
    "Ethical and Professional Standards",
    "Quantitative Methods",
    "Economics",
    "Financial Statement Analysis",
    "Corporate Issuers",
    "Equity Investments",
    "Fixed Income",
    "Derivatives",
    "Alternative Investments",
    "Portfolio Management",
]


def compile_all():
    all_questions = []
    seen_ids = set()

    # 1. Process FSA (460 Qs)
    for fpath in FSA_FILES:
        with open(fpath, "r", encoding="utf-8") as f:
            qs = json.load(f)
        for q in qs:
            qid = q["id"]
            assert qid not in seen_ids, f"Duplicate ID in FSA: {qid}"
            seen_ids.add(qid)
            q["subject"] = "Financial Statement Analysis"
            q["module_title"] = q.get("topic") or q.get("module") or "FSA Core Module"
            if q.get("level") == 2:
                vid = q.get("vignette_id", "V00")
                q["global_vignette_id"] = f"FSA-{vid}"
            all_questions.append(q)

    # 2. Process FI, Equity & PM (625 Qs)
    for subj, fpath in FI_EQ_FILES:
        with open(fpath, "r", encoding="utf-8") as f:
            qs = json.load(f)
        for q in qs:
            qid = q["id"]
            assert qid not in seen_ids, f"Duplicate ID in FI/EQ/PM: {qid}"
            seen_ids.add(qid)
            q["subject"] = subj
            q["module_title"] = q.get("subtopic") or q.get("topic") or subj
            if q.get("level") == 2:
                vid = q.get("vignette_id", "V00")
                prefix = "FI" if subj == "Fixed Income" else ("EQ" if subj == "Equity Investments" else "PM")
                q["global_vignette_id"] = f"{prefix}-{vid}"
            all_questions.append(q)

    # 3. Process Remaining 6 CBOK Courses (1,125 Qs)
    for subj, prefix, fpath in COURSE_FILES:
        assert os.path.exists(fpath), f"Missing course file: {fpath}"
        with open(fpath, "r", encoding="utf-8") as f:
            qs = json.load(f)
        for q in qs:
            qid = q["id"]
            assert qid not in seen_ids, f"Duplicate ID in {subj}: {qid}"
            seen_ids.add(qid)
            q["subject"] = subj
            q["module_title"] = q.get("module_title") or q.get("subtopic") or q.get("topic") or subj
            if q.get("level") == 2:
                if not q.get("global_vignette_id"):
                    vid = q.get("vignette_id", "V00")
                    q["global_vignette_id"] = f"{prefix}-{vid}"
            all_questions.append(q)

    # Validate every question
    by_subj = {}
    vignettes_by_subj = {s: set() for s in SUBJECT_ORDER}
    for q in all_questions:
        assert "id" in q and "level" in q and "question" in q and "options" in q and "answer" in q
        assert q["answer"] in ["A", "B", "C"], f"{q['id']}: invalid answer {q['answer']}"
        assert set(q["options"].keys()) == {"A", "B", "C"}, f"{q['id']}: invalid options"
        s = q["subject"]
        assert s in vignettes_by_subj, f"Unexpected subject: {s}"
        if s not in by_subj:
            by_subj[s] = {"total": 0, "l1": 0, "l2": 0}
        by_subj[s]["total"] += 1
        if q["level"] == 1:
            by_subj[s]["l1"] += 1
        elif q["level"] == 2:
            by_subj[s]["l2"] += 1
            assert q.get("global_vignette_id") and q.get("vignette_title") and q.get("vignette_text"), f"{q['id']}: incomplete L2 vignette"
            vignettes_by_subj[s].add(q["global_vignette_id"])

    for s in SUBJECT_ORDER:
        by_subj[s]["vignettes"] = len(vignettes_by_subj[s])

    l1_total = sum(v["l1"] for v in by_subj.values())
    l2_total = sum(v["l2"] for v in by_subj.values())
    v_total = sum(v["vignettes"] for v in by_subj.values())

    manifest = {
        "total_questions": len(all_questions),
        "l1_total": l1_total,
        "l2_total": l2_total,
        "vignettes_total": v_total,
        "subjects": by_subj,
        "subject_order": SUBJECT_ORDER,
    }

    with open(OUTPUT_MASTER, "w", encoding="utf-8") as f:
        json.dump(all_questions, f, indent=2, ensure_ascii=False)
    with open(OUTPUT_MANIFEST, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)

    print(f"Compiled {len(all_questions)} total questions ({l1_total} L1 + {l2_total} L2 across {v_total} vignettes)")
    for s in SUBJECT_ORDER:
        st = by_subj[s]
        print(f"  {s:36s}: {st['total']:4d} Qs ({st['l1']:3d} L1 + {st['l2']:3d} L2 across {st['vignettes']:2d} V)")
    return all_questions, manifest


if __name__ == "__main__":
    compile_all()
