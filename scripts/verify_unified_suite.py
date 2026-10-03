#!/usr/bin/env python3
"""
verify_unified_suite.py
Rigorous audit and assertion verification for the unified CFA Master Platform:
- 855 total questions
- 425 Level 1 questions (190 FSA, 120 FI, 115 Equity)
- 430 Level 2 questions across 80 distinct vignettes (250 FSA across 44 V, 85 FI across 17 V, 95 EQ across 19 V)
- 9 Financial simulation engines
- KaTeX syntax balance and currency rule compliance
"""

import json
import os
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
MASTER_JSON = os.path.join(DATA_DIR, "cfa_master_855.json")
INDEX_HTML = os.path.join(BASE_DIR, "index.html")
FI_EQ_HTML = os.path.join(BASE_DIR, "fi_eq_dashboard.html")

assert os.path.exists(MASTER_JSON), "Missing cfa_master_855.json"
assert os.path.exists(INDEX_HTML), "Missing index.html"
assert os.path.exists(FI_EQ_HTML), "Missing fi_eq_dashboard.html"

with open(MASTER_JSON, "r", encoding="utf-8") as f:
    questions = json.load(f)

total_count = len(questions)
print(f"Total questions loaded from {MASTER_JSON}: {total_count}")
assert total_count == 855, f"Expected 855 questions, got {total_count}"

# Subject and level counters
by_subj = {}
by_level = {1: 0, 2: 0}
l1_by_subj = {}
l2_by_subj = {}
vignettes_by_subj = {"Financial Statement Analysis": set(), "Fixed Income": set(), "Equity Investments": set()}
all_ids = set()

# KaTeX delimiter and bare currency patterns
re_display = re.compile(r'\$\$.*?\$\$', re.DOTALL)
re_inline = re.compile(r'(?<!\\)\$.*?(?<!\\)\$')

schema_errors = []
currency_errors = []
katex_errors = []

for q in questions:
    qid = q["id"]
    assert qid not in all_ids, f"Duplicate Question ID: {qid}"
    all_ids.add(qid)

    subj = q["subject"]
    lvl = q["level"]
    ans = q["answer"]
    opts = q["options"]
    expl = q.get("explanation", "")

    # Schema checks
    if ans not in ["A", "B", "C"]:
        schema_errors.append(f"{qid}: Invalid answer '{ans}'")
    if set(opts.keys()) != {"A", "B", "C"}:
        schema_errors.append(f"{qid}: Invalid option keys {list(opts.keys())}")

    by_subj[subj] = by_subj.get(subj, 0) + 1
    by_level[lvl] = by_level.get(lvl, 0) + 1

    if lvl == 1:
        l1_by_subj[subj] = l1_by_subj.get(subj, 0) + 1
    elif lvl == 2:
        l2_by_subj[subj] = l2_by_subj.get(subj, 0) + 1
        vid = q.get("global_vignette_id")
        assert vid, f"Missing global_vignette_id in {qid}"
        assert q.get("vignette_title"), f"Missing vignette_title in {qid}"
        assert q.get("vignette_text"), f"Missing vignette_text in {qid}"
        vignettes_by_subj[subj].add(vid)

    # Rigorous check across all textual fields for KaTeX parity and bare dollars
    for field_name in ["question", "explanation", "vignette_text"]:
        field_val = q.get(field_name, "")
        if not field_val:
            continue

        # 1. Delimiter parity check
        if field_val.count("$$") % 2 != 0:
            katex_errors.append(f"{qid} ({field_name}): Unbalanced $$ delimiters")
        cleaned_dollars = field_val.replace("$$", "").replace(r"\$", "")
        if cleaned_dollars.count("$") % 2 != 0:
            katex_errors.append(f"{qid} ({field_name}): Unbalanced inline $ delimiters")

        # 2. Currency/stray dollar check: No unescaped bare $ allowed outside math blocks
        no_display = re_display.sub("", field_val)
        no_inline = re_inline.sub("", no_display)
        no_escaped = no_inline.replace(r"\$", "")
        if "$" in no_escaped:
            currency_errors.append(f"{qid} ({field_name}): Bare unescaped $ found in prose outside math block")

print("--- Subject Breakdown ---")
for s, c in sorted(by_subj.items()):
    print(f"  {s}: {c} Questions")

print("--- Level Breakdown ---")
print(f"  Level 1: {by_level[1]} MCQs (FSA: {l1_by_subj.get('Financial Statement Analysis', 0)}, FI: {l1_by_subj.get('Fixed Income', 0)}, Equity: {l1_by_subj.get('Equity Investments', 0)})")
print(f"  Level 2: {by_level[2]} Questions (FSA: {l2_by_subj.get('Financial Statement Analysis', 0)}, FI: {l2_by_subj.get('Fixed Income', 0)}, Equity: {l2_by_subj.get('Equity Investments', 0)})")

total_vignettes = sum(len(v) for v in vignettes_by_subj.values())
print(f"  Level 2 Item Sets: {total_vignettes} distinct vignettes (FSA: {len(vignettes_by_subj['Financial Statement Analysis'])}, FI: {len(vignettes_by_subj['Fixed Income'])}, Equity: {len(vignettes_by_subj['Equity Investments'])})")

# Assertions
assert by_level[1] == 425, f"Expected 425 L1, got {by_level[1]}"
assert by_level[2] == 430, f"Expected 430 L2, got {by_level[2]}"
assert total_vignettes == 80, f"Expected 80 vignettes, got {total_vignettes}"

# Check HTML size and content
with open(INDEX_HTML, "r", encoding="utf-8") as f:
    html_content = f.read()

print(f"\nUnified index.html size: {len(html_content)} bytes ({len(html_content)/1024/1024:.2f} MB)")
assert len(html_content) > 1_500_000, "index.html appears truncated"

# Check that all 9 simulations exist in index.html
sim_ids = [
    "sim-yield", "sim-tree", "sim-equity", "sim-duration",
    "sim-frn", "sim-ri-decay", "sim-waterfall", "sim-translation", "sim-prepayment"
]
for sid in sim_ids:
    assert f'id="{sid}"' in html_content, f"Simulation {sid} missing from index.html"

# Check FSA Reference section
assert 'id="fsa-reference"' in html_content, "FSA reference section missing from index.html"
assert 'GAAP vs IFRS Matrix' in html_content, "GAAP vs IFRS matrix missing from index.html"

# Check redirect file
with open(FI_EQ_HTML, "r", encoding="utf-8") as f:
    redirect_content = f.read()
assert 'http-equiv="refresh"' in redirect_content, "fi_eq_dashboard.html missing refresh redirect"
assert 'url=index.html' in redirect_content, "fi_eq_dashboard.html redirect destination incorrect"

print("\n--- Compliance & Auditing ---")
print(f"  Schema Errors:   {len(schema_errors)}")
print(f"  Currency Errors: {len(currency_errors)}")
print(f"  KaTeX Errors:    {len(katex_errors)}")

assert len(schema_errors) == 0, f"Found schema errors: {schema_errors[:5]}"
assert len(currency_errors) == 0, f"Found currency errors: {currency_errors[:5]}"
assert len(katex_errors) == 0, f"Found KaTeX errors: {katex_errors[:5]}"

print("\n[SUCCESS] ALL AUDIT ASSERTIONS PASSED WITH 100% COMPLIANCE!")
