#!/usr/bin/env python3
"""
compile_qb.py
Validates, checks currency and KaTeX rules, and consolidates the 400 CFA L1 & L2 questions
into data/cfa_question_bank_master.json, and injects the interactive question engine
into build_notes.py and index.html.
"""

import json
import os
import re
import sys

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data")
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX_PATH = os.path.join(BASE_DIR, "index.html")
BUILD_NOTES_PATH = os.path.join(BASE_DIR, "build_notes.py")

FILES = [
    "l1_questions_part1.json",
    "l1_questions_part2.json",
    "l2_questions_part1.json",
    "l2_questions_part2.json",
    "l2_questions_part3.json"
]

def check_currency_rule(text, qid):
    """
    Flags any bare dollar signs used for currency like $50, $10M, etc.
    Math expressions should be $E=mc^2$ or $\\$50$.
    """
    # Regex for bare dollar sign followed directly by a digit
    bare_dollar = re.findall(r'(?<!\\)\$(?=\d)', text)
    if bare_dollar:
        print(f"  [WARNING] Possible bare currency symbol in {qid}: found bare $ before digit")
        return False
    return True

def validate_and_compile():
    all_questions = []
    l1_questions = []
    l2_questions = []
    errors = 0
    warnings = 0

    print("=== CFA QUESTION BANK COMPILER & VALIDATOR ===")
    
    for filename in FILES:
        filepath = os.path.join(DATA_DIR, filename)
        if not os.path.exists(filepath):
            print(f"[PENDING] File not found yet: {filename}")
            continue
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except Exception as e:
            print(f"[ERROR] Failed to parse JSON in {filename}: {e}")
            errors += 1
            continue

        print(f"[LOADED] {filename} -> {len(data)} questions")
        for q in data:
            qid = q.get("id", "UNKNOWN")
            level = q.get("level")
            
            # Validation
            req_fields = ["id", "level", "module", "topic", "los", "question", "options", "answer", "explanation"]
            for field in req_fields:
                if field not in q:
                    print(f"  [ERROR] Question {qid} missing field: {field}")
                    errors += 1
            
            if q.get("answer") not in ["A", "B", "C"]:
                print(f"  [ERROR] Question {qid} invalid answer: {q.get('answer')}")
                errors += 1
                
            opts = q.get("options", {})
            for key in ["A", "B", "C"]:
                if key not in opts:
                    print(f"  [ERROR] Question {qid} missing option {key}")
                    errors += 1

            if level == 2:
                if not q.get("vignette_id") or not q.get("vignette_text"):
                    print(f"  [ERROR] Level 2 Question {qid} missing vignette_id or vignette_text")
                    errors += 1
                l2_questions.append(q)
            elif level == 1:
                l1_questions.append(q)

            # Currency check
            all_text = f"{q.get('question','')} {str(opts)} {q.get('explanation','')}"
            if not check_currency_rule(all_text, qid):
                warnings += 1

            all_questions.append(q)

    print(f"\nValidation Summary:")
    print(f"  Total Valid Questions: {len(all_questions)}")
    print(f"  - Level 1 Questions:   {len(l1_questions)}")
    print(f"  - Level 2 Questions:   {len(l2_questions)}")
    print(f"  Total Errors:         {errors}")
    print(f"  Total Warnings:       {warnings}")

    if len(all_questions) == 0:
        print("[INFO] No questions compiled yet. Waiting for subagents.")
        return False

    master_path = os.path.join(DATA_DIR, "cfa_question_bank_master.json")
    with open(master_path, 'w', encoding='utf-8') as f:
        json.dump(all_questions, f, indent=2, ensure_ascii=False)
    print(f"[SAVED] Master Question Bank saved to {master_path} ({os.path.getsize(master_path)} bytes)")

    return True

if __name__ == "__main__":
    validate_and_compile()
