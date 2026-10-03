# -*- coding: utf-8 -*-
"""
Master Generator Script: CFA Level 1 Fixed Income Question Bank (85 Questions)
Output: data/fi_eq/l1_fixed_income.json
"""

import os
import sys
import json
import re

# Add current directory to path for imports
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

from modules.m1_defining_elements import M1_QUESTIONS
from modules.m2_markets import M2_QUESTIONS
from modules.m3_valuation import M3_QUESTIONS
from modules.m4_abs import M4_QUESTIONS
from modules.m5_risk_return import M5_QUESTIONS
from modules.m6_credit import M6_QUESTIONS


def validate_and_assemble():
    all_questions = []
    modules = [
        ("Module 1: Defining Elements", M1_QUESTIONS, 14),
        ("Module 2: Fixed-Income Markets", M2_QUESTIONS, 12),
        ("Module 3: Fixed-Income Valuation", M3_QUESTIONS, 18),
        ("Module 4: Asset-Backed Securities", M4_QUESTIONS, 12),
        ("Module 5: Fixed-Income Risk & Return", M5_QUESTIONS, 16),
        ("Module 6: Fundamentals of Credit Analysis", M6_QUESTIONS, 13),
    ]

    print("=" * 60)
    print("CFA Level 1 Fixed Income Question Bank Compilation")
    print("=" * 60)

    total_count = 0
    for name, q_list, expected_len in modules:
        actual_len = len(q_list)
        print(f"[*] {name}: {actual_len} questions (Expected: {expected_len})")
        assert actual_len == expected_len, f"Length mismatch in {name}: got {actual_len}, expected {expected_len}"
        all_questions.extend(q_list)
        total_count += actual_len

    print(f"\n[+] Total Questions: {total_count} (Expected: 85)")
    assert total_count == 85, f"Total count must be exactly 85, got {total_count}"

    # Schema & Content Validation
    required_keys = {
        "id", "level", "topic", "subtopic", "los",
        "question", "options", "answer", "explanation", "distractor_analysis"
    }

    seen_ids = set()
    raw_currency_pattern = re.compile(r'(?<!\\)\$\d+')

    for idx, q in enumerate(all_questions, 1):
        qid = q.get("id")
        assert qid, f"Question at index {idx} missing 'id'"
        assert qid not in seen_ids, f"Duplicate ID: {qid}"
        seen_ids.add(qid)

        # Verify key set
        missing = required_keys - set(q.keys())
        assert not missing, f"Question {qid} missing keys: {missing}"

        # Level & Topic
        assert q["level"] == 1, f"Question {qid} level must be 1"
        assert q["topic"] == "Fixed Income", f"Question {qid} topic must be 'Fixed Income'"

        # Options
        options = q["options"]
        assert set(options.keys()) == {"A", "B", "C"}, f"Question {qid} options must have keys A, B, C"
        for opt_key, opt_val in options.items():
            assert opt_val.strip(), f"Question {qid} option {opt_key} is empty"

        # Answer
        ans = q["answer"]
        assert ans in {"A", "B", "C"}, f"Question {qid} answer must be A, B, or C"

        # Distractor analysis
        distractors = q["distractor_analysis"]
        expected_distractors = {"A", "B", "C"} - {ans}
        for d_key in expected_distractors:
            assert d_key in distractors, f"Question {qid} missing distractor analysis for option {d_key}"
            assert distractors[d_key].strip(), f"Question {qid} distractor {d_key} empty"

        # Currency & Math Rule Validation:
        # STRICTLY RESERVE the '$' symbol for math mode delimiters ONLY ($...$ or $$...$$).
        # DO NOT use the '$' symbol for currency amounts (e.g. '$500').
        for field in ["question", "explanation"]:
            text = q[field]
            cleaned = text.replace(r"\$", "")  # remove valid escaped \$
            # Remove display math $$...$$
            no_display = re.sub(r"\$\$.*?\$\$", "", cleaned, flags=re.DOTALL)
            # Count remaining unescaped single $ - must be even (balanced pairs)
            single_dollars = no_display.count("$")
            if single_dollars % 2 != 0:
                raise ValueError(f"Question {qid} field {field} has unbalanced math '$': count={single_dollars}")

            # Outside math blocks, there should be NO unescaped '$'
            plain_text = re.sub(r"\$.*?\$", "", no_display, flags=re.DOTALL)
            if "$" in plain_text:
                raise ValueError(f"Question {qid} field {field} has unescaped '$' outside math mode: {plain_text}")

            # Inside inline math, verify nobody put a naked currency number like $500$
            for m in re.finditer(r"\$([^\$]+)\$", no_display):
                math_inner = m.group(1).strip()
                if re.match(r"^\d+([,\.]\d+)?$", math_inner):
                    raise ValueError(f"Question {qid} field {field} has naked number in math delimiters (${math_inner}$), suspect currency.")

        for d_key, d_text in q["distractor_analysis"].items():
            cleaned = d_text.replace(r"\$", "")
            no_display = re.sub(r"\$\$.*?\$\$", "", cleaned, flags=re.DOTALL)
            single_dollars = no_display.count("$")
            if single_dollars % 2 != 0:
                raise ValueError(f"Question {qid} distractor {d_key} has unbalanced math '$': count={single_dollars}")
            plain_text = re.sub(r"\$.*?\$", "", no_display, flags=re.DOTALL)
            if "$" in plain_text:
                raise ValueError(f"Question {qid} distractor {d_key} has unescaped '$' outside math mode")

    print("[+] All 85 questions passed schema and rule validation.")

    # Write to target JSON
    output_path = os.path.join(current_dir, "l1_fixed_income.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(all_questions, f, indent=2, ensure_ascii=False)

    print(f"[+] Output written to: {output_path}")

    # Re-read and verify valid JSON
    with open(output_path, "r", encoding="utf-8") as f:
        reloaded = json.load(f)
    print(f"[+] Re-read verification successful: {len(reloaded)} items in valid JSON.")
    print("=" * 60)


if __name__ == "__main__":
    validate_and_assemble()
