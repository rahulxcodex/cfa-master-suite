#!/usr/bin/env python3
"""
verify_unified_suite.py
Rigorous audit and assertion verification for the complete 10-course CFA Master Platform:
- 2,210 total questions across all 10 CBOK courses
- 1,225 Level 1 MCQs + 985 Level 2 Questions across 183 distinct vignettes
- 16 Financial simulation engines
- 10 Complete Curriculum Reference Note sections (105 chapters)
- 63 Master Solved Numericals & 64 Jargon Terminologies
- 100% KaTeX delimiter balance, currency compliance, and zero unreplaced template tokens
"""

import json
import os
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
MASTER_JSON = os.path.join(DATA_DIR, "cfa_master_855.json")
MANIFEST_JSON = os.path.join(DATA_DIR, "suite_manifest.json")
SOLVED_JSON = os.path.join(DATA_DIR, "master_solved_numericals.json")
JARGON_JSON = os.path.join(DATA_DIR, "cfa_jargon_dictionary.json")
INDEX_HTML = os.path.join(BASE_DIR, "index.html")
FI_EQ_HTML = os.path.join(BASE_DIR, "fi_eq_dashboard.html")

for p in [MASTER_JSON, MANIFEST_JSON, SOLVED_JSON, JARGON_JSON, INDEX_HTML, FI_EQ_HTML]:
    assert os.path.exists(p), f"Missing required file: {p}"

with open(MASTER_JSON, "r", encoding="utf-8") as f:
    questions = json.load(f)
with open(MANIFEST_JSON, "r", encoding="utf-8") as f:
    manifest = json.load(f)
with open(SOLVED_JSON, "r", encoding="utf-8") as f:
    solved_items = json.load(f)
with open(JARGON_JSON, "r", encoding="utf-8") as f:
    jargon_items = json.load(f)

total_count = len(questions)
print(f"Total questions loaded from {MASTER_JSON}: {total_count}")
assert total_count == 2210, f"Expected 2210 questions, got {total_count}"
assert len(solved_items) == 63, f"Expected 63 solved numericals, got {len(solved_items)}"
assert len(jargon_items) == 64, f"Expected 64 jargon terms, got {len(jargon_items)}"

expected_subjects = {
    "Ethical and Professional Standards": (270, 180, 30),
    "Quantitative Methods": (90, 60, 10),
    "Economics": (80, 50, 10),
    "Financial Statement Analysis": (190, 270, 48),
    "Corporate Issuers": (80, 50, 10),
    "Equity Investments": (115, 95, 19),
    "Fixed Income": (120, 85, 17),
    "Derivatives": (85, 55, 11),
    "Alternative Investments": (75, 50, 10),
    "Portfolio Management": (120, 90, 18),
}

by_subj = {}
by_level = {1: 0, 2: 0}
l1_by_subj = {}
l2_by_subj = {}
vignettes_by_subj = {s: set() for s in expected_subjects}
all_ids = set()

re_display = re.compile(r"\$\$.*?\$\$", re.DOTALL)
re_inline = re.compile(r"(?<!\\)\$.*?(?<!\\)\$")

schema_errors = []
currency_errors = []
katex_errors = []

for q in questions:
    qid = q["id"]
    assert qid not in all_ids, f"Duplicate Question ID: {qid}"
    all_ids.add(qid)

    subj = q["subject"]
    assert subj in expected_subjects, f"{qid}: unexpected subject {subj}"
    lvl = q["level"]
    ans = q["answer"]
    opts = q["options"]

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

    for field_name in ["question", "explanation", "vignette_text"]:
        field_val = q.get(field_name, "")
        if not field_val:
            continue
        if field_val.count("$$") % 2 != 0:
            katex_errors.append(f"{qid} ({field_name}): Unbalanced $$ delimiters")
        cleaned_dollars = field_val.replace("$$", "").replace(r"\$", "")
        if cleaned_dollars.count("$") % 2 != 0:
            katex_errors.append(f"{qid} ({field_name}): Unbalanced inline $ delimiters")
        no_display = re_display.sub("", field_val)
        no_inline = re_inline.sub("", no_display)
        no_escaped = no_inline.replace(r"\$", "")
        if "$" in no_escaped:
            currency_errors.append(f"{qid} ({field_name}): Bare unescaped $ found outside math block")

print("\n--- 10-Course CBOK Breakdown ---")
for s, (exp_l1, exp_l2, exp_v) in expected_subjects.items():
    got_l1 = l1_by_subj.get(s, 0)
    got_l2 = l2_by_subj.get(s, 0)
    got_v = len(vignettes_by_subj[s])
    print(f"  {s:36s}: {got_l1:3d} L1 + {got_l2:3d} L2 ({got_v:2d} V) = {got_l1+got_l2:3d} Qs")
    assert (got_l1, got_l2, got_v) == (exp_l1, exp_l2, exp_v), f"{s}: expected {(exp_l1, exp_l2, exp_v)}, got {(got_l1, got_l2, got_v)}"

total_vignettes = sum(len(v) for v in vignettes_by_subj.values())
assert by_level[1] == 1225, f"Expected 1225 L1, got {by_level[1]}"
assert by_level[2] == 985, f"Expected 985 L2, got {by_level[2]}"
assert total_vignettes == 183, f"Expected 183 vignettes, got {total_vignettes}"

with open(INDEX_HTML, "r", encoding="utf-8") as f:
    html_content = f.read()

print(f"\nUnified index.html size: {len(html_content)} bytes ({len(html_content)/1024/1024:.2f} MB)")
assert len(html_content) > 4_000_000, "index.html appears smaller than expected"

# Check all 16 simulations exist
sim_ids = [
    "sim-yield", "sim-tree", "sim-equity", "sim-duration",
    "sim-frn", "sim-ri-decay", "sim-waterfall", "sim-translation", "sim-prepayment",
    "sim-frontier", "sim-fundamental-law", "sim-rebalancing",
    "sim-bsm", "sim-quant", "sim-alts", "sim-corp",
]
for sid in sim_ids:
    assert f'id="{sid}"' in html_content, f"Simulation {sid} missing from index.html"

# Check all 10 Reference sections exist
ref_ids = [
    "eth-reference", "qm-reference", "econ-reference", "fsa-reference",
    "corp-reference", "eq-reference", "fi-reference", "deriv-reference",
    "alt-reference", "pm-reference",
]
for rid in ref_ids:
    assert f'id="{rid}"' in html_content, f"Reference section {rid} missing from index.html"

# Check no unreplaced template tokens remain
unreplaced = re.findall(r"__[A-Z0-9_]+__", html_content)
assert not unreplaced, f"Unreplaced template tokens in index.html: {set(unreplaced)}"
assert "GAAP vs IFRS Matrix" in html_content, "GAAP vs IFRS matrix missing"
assert "NOT IN PORTAL" not in html_content, "Stale NOT IN PORTAL status found in audit table"

with open(FI_EQ_HTML, "r", encoding="utf-8") as f:
    redirect_content = f.read()
assert 'http-equiv="refresh"' in redirect_content, "fi_eq_dashboard.html missing refresh redirect"

print("\n--- Compliance & Auditing ---")
print(f"  Schema Errors:   {len(schema_errors)}")
print(f"  Currency Errors: {len(currency_errors)}")
print(f"  KaTeX Errors:    {len(katex_errors)}")

assert len(schema_errors) == 0, f"Found schema errors: {schema_errors[:5]}"
assert len(currency_errors) == 0, f"Found currency errors: {currency_errors[:5]}"
assert len(katex_errors) == 0, f"Found KaTeX errors: {katex_errors[:5]}"

print("\n[SUCCESS] ALL 10-COURSE AUDIT ASSERTIONS PASSED WITH 100% COMPLIANCE!")
