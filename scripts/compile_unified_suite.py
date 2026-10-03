import json
import os
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
FI_EQ_DIR = os.path.join(DATA_DIR, "fi_eq")
OUTPUT_MASTER = os.path.join(DATA_DIR, "cfa_master_855.json")

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
]

def compile_all():
    all_questions = []
    seen_ids = set()

    # 1. Process FSA
    fsa_count = 0
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
            fsa_count += 1
    print(f"Loaded {fsa_count} FSA questions.")

    # 2. Process FI & Equity
    fi_eq_count = 0
    for subj, fpath in FI_EQ_FILES:
        with open(fpath, "r", encoding="utf-8") as f:
            qs = json.load(f)
        for q in qs:
            qid = q["id"]
            assert qid not in seen_ids, f"Duplicate ID in FI/EQ: {qid}"
            seen_ids.add(qid)
            q["subject"] = subj
            q["module_title"] = q.get("subtopic") or q.get("topic") or subj
            if q.get("level") == 2:
                vid = q.get("vignette_id", "V00")
                prefix = "FI" if subj == "Fixed Income" else "EQ"
                q["global_vignette_id"] = f"{prefix}-{vid}"
            all_questions.append(q)
            fi_eq_count += 1
    print(f"Loaded {fi_eq_count} Fixed Income & Equity questions.")

    total = len(all_questions)
    print(f"Total consolidated questions: {total}")
    assert total == 875, f"Expected 875 questions, found {total}"

    # Validation of fields
    for q in all_questions:
        assert "id" in q and "level" in q and "question" in q and "options" in q and "answer" in q
        assert q["answer"] in ["A", "B", "C"]
        assert set(q["options"].keys()) == {"A", "B", "C"}
        if q["level"] == 2:
            assert "global_vignette_id" in q
            assert "vignette_title" in q and len(q["vignette_title"]) > 0
            assert "vignette_text" in q and len(q["vignette_text"]) > 0

    l1_qs = [q for q in all_questions if q["level"] == 1]
    l2_qs = [q for q in all_questions if q["level"] == 2]
    print(f"  Level 1 Questions: {len(l1_qs)}")
    print(f"  Level 2 Questions: {len(l2_qs)}")
    
    distinct_vignettes = set(q.get("global_vignette_id") for q in l2_qs)
    print(f"  Level 2 Distinct Vignettes: {len(distinct_vignettes)}")

    with open(OUTPUT_MASTER, "w", encoding="utf-8") as f:
        json.dump(all_questions, f, indent=2, ensure_ascii=False)

    print(f"Saved master JSON to {OUTPUT_MASTER} ({os.path.getsize(OUTPUT_MASTER)} bytes)")
    return all_questions

if __name__ == "__main__":
    compile_all()
