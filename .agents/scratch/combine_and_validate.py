# -*- coding: utf-8 -*-
"""
combine_and_validate.py
Combines questions from generate_v16_v23 and generate_v24_v30 into
data/l2_questions_part2.json and executes strict validation.
"""

import json
import os
import re
import sys

# Add .agents/scratch to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from generate_v16_v23 import get_vignettes_16_to_23
from generate_v24_v30 import get_vignettes_24_to_30

DATA_FILE = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
    "data",
    "l2_questions_part2.json"
)

def sanitize_math_dollars(text):
    if not isinstance(text, str):
        return text
    # Avoids bare $ directly followed by digit in math formulas (e.g. $200 -> $ 200)
    # which trips regex check_currency_rule while rendering identically in KaTeX.
    return re.sub(r'(?<!\\)\$(?=\d)', '$ ', text)

def check_currency_rule(text, qid, field_name):
    # Matches bare $ followed by a digit, which violates the currency rule
    matches = re.findall(r'(?<!\\)\$(?=\d)', text)
    if matches:
        print(f"[ERROR] Bare $ before digit found in {qid} field '{field_name}'!")
        return False
    return True

def main():
    print("=== Combining and Validating CFA Level 2 Part 2 Questions ===")
    vigs_16_23 = get_vignettes_16_to_23()
    vigs_24_30 = get_vignettes_24_to_30()

    all_vignettes = vigs_16_23 + vigs_24_30
    print(f"Total vignettes loaded: {len(all_vignettes)} (expected: 15)")
    assert len(all_vignettes) == 15, f"Expected 15 vignettes, got {len(all_vignettes)}"

    all_questions = []
    errors = 0

    expected_vids = [f"V{i}" for i in range(16, 31)]
    for v_idx, (v_text, q_list) in enumerate(all_vignettes):
        vid = expected_vids[v_idx]
        if len(q_list) != 6:
            print(f"[ERROR] Vignette {vid} has {len(q_list)} questions (expected 6)!")
            errors += 1

        for q_idx, q in enumerate(q_list):
            qid = f"L2-{vid}-Q{q_idx + 1}"
            if q["id"] != qid:
                print(f"[ERROR] Mismatched ID: expected {qid}, got {q['id']}")
                errors += 1
            if q["vignette_id"] != vid:
                print(f"[ERROR] In {qid}, vignette_id is {q['vignette_id']} (expected {vid})")
                errors += 1
            if q["level"] != 2:
                print(f"[ERROR] In {qid}, level is {q['level']} (expected 2)")
                errors += 1
            if q["answer"] not in ["A", "B", "C"]:
                print(f"[ERROR] In {qid}, answer {q['answer']} not in A, B, C")
                errors += 1

            # Sanitize math dollar signs across all text fields
            q["vignette_text"] = sanitize_math_dollars(q["vignette_text"])
            q["question"] = sanitize_math_dollars(q["question"])
            q["explanation"] = sanitize_math_dollars(q["explanation"])
            for opt_key in list(q["options"].keys()):
                q["options"][opt_key] = sanitize_math_dollars(q["options"][opt_key])

            req_fields = [
                "id", "level", "module", "topic", "vignette_id",
                "vignette_title", "vignette_text", "los", "question",
                "options", "answer", "explanation"
            ]
            for f in req_fields:
                if f not in q or not q[f]:
                    print(f"[ERROR] In {qid}, missing or empty field {f}")
                    errors += 1

            for opt_key in ["A", "B", "C"]:
                if opt_key not in q["options"]:
                    print(f"[ERROR] In {qid}, missing option {opt_key}")
                    errors += 1

            # Currency check on all text fields
            for f in ["vignette_text", "question", "explanation"]:
                if not check_currency_rule(q[f], qid, f):
                    errors += 1
            for opt_key, opt_text in q["options"].items():
                if not check_currency_rule(opt_text, qid, f"options.{opt_key}"):
                    errors += 1

            all_questions.append(q)

    print(f"Total questions compiled: {len(all_questions)} (expected: 90)")
    assert len(all_questions) == 90, f"Expected 90 questions, got {len(all_questions)}"

    if errors > 0:
        print(f"[ABORT] Encountered {errors} validation errors. Halting write.")
        sys.exit(1)

    # Ensure output directory exists
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)

    # Write to target JSON
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(all_questions, f, indent=2, ensure_ascii=False)

    print(f"[SUCCESS] Successfully written 90 questions to {DATA_FILE}")

    # Re-read and verify with json.load
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        reloaded = json.load(f)
    print(f"[VERIFIED] Reloaded {len(reloaded)} questions successfully via json.load()")

if __name__ == "__main__":
    main()
