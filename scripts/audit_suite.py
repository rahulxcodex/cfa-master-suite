import json
import os
import re

files = {
    "L1-FI": "data/fi_eq/l1_fixed_income.json",
    "L1-EQ": "data/fi_eq/l1_equity.json",
    "L2-FI": "data/fi_eq/l2_fixed_income.json",
    "L2-EQ": "data/fi_eq/l2_equity.json"
}

report = {
    "total_questions": 0,
    "module_counts": {},
    "vignette_counts": {},
    "schema_errors": [],
    "currency_errors": [],
    "katex_errors": [],
    "distractor_errors": [],
    "math_samples": []
}

# Regex to check for unescaped $ followed immediately or after space by a digit
currency_regex = re.compile(r'(?<!\\)\$\s*\d')

for category, fpath in files.items():
    if not os.path.exists(fpath):
        report["schema_errors"].append(f"Missing file: {fpath}")
        continue
    with open(fpath, "r", encoding="utf-8") as f:
        data = json.load(f)
    report["module_counts"][category] = len(data)
    report["total_questions"] += len(data)

    vignette_ids = set()
    for q in data:
        qid = q.get("id", "UNKNOWN")
        level = q.get("level")
        ans = q.get("answer")
        opts = q.get("options", {})
        expl = q.get("explanation", "")
        dist = q.get("distractor_analysis", {})

        # Schema check
        if ans not in ["A", "B", "C"]:
            report["schema_errors"].append(f"{qid}: Invalid answer '{ans}'")
        if set(opts.keys()) != {"A", "B", "C"}:
            report["schema_errors"].append(f"{qid}: Options do not match A, B, C: {list(opts.keys())}")
        
        # Vignette check for L2
        if level == 2:
            vid = q.get("vignette_id")
            if not vid:
                report["schema_errors"].append(f"{qid}: Missing vignette_id")
            else:
                vignette_ids.add(vid)
            if not q.get("vignette_title") or not q.get("vignette_text"):
                report["schema_errors"].append(f"{qid}: Missing vignette title or text")

        # Distractor analysis check
        non_answers = [o for o in ["A", "B", "C"] if o != ans]
        for na in non_answers:
            if na not in dist:
                report["distractor_errors"].append(f"{qid}: Missing distractor analysis for '{na}'")

        # Currency check: scan all text fields
        text_blobs = [q.get("question", ""), expl] + list(opts.values()) + list(dist.values())
        if level == 2:
            text_blobs.append(q.get("vignette_text", ""))
        
        for blob in text_blobs:
            # Check for unescaped bare $ currency
            m = currency_regex.search(blob)
            if m:
                # verify if it's within a math block or currency
                # if preceded by math tag or within math, let's inspect
                report["currency_errors"].append(f"{qid}: Potential currency symbol issue: '{m.group(0)}' in snippet '{blob[max(0, m.start()-10):m.end()+15]}'")

            # Check KaTeX delimiter pairing
            single_dollars = blob.count('$') - 2 * blob.count('$$')
            if single_dollars % 2 != 0:
                report["katex_errors"].append(f"{qid}: Unbalanced single '$' delimiters ({single_dollars}) in snippet: '{blob[:60]}...'")

    if vignette_ids:
        report["vignette_counts"][category] = len(vignette_ids)

print("=== CFA QUESTION BANK AUDIT SUMMARY ===")
print(f"Total Questions: {report['total_questions']}")
print(f"Module Counts: {report['module_counts']}")
print(f"Vignette Counts: {report['vignette_counts']}")
print(f"Schema Errors: {len(report['schema_errors'])}")
print(f"Currency Errors: {len(report['currency_errors'])}")
print(f"KaTeX Delimiter Errors: {len(report['katex_errors'])}")
print(f"Distractor Errors: {len(report['distractor_errors'])}")

if report["currency_errors"]:
    print("\nCurrency Errors Sample:")
    for err in report["currency_errors"][:5]:
        print("  -", err)

if report["katex_errors"]:
    print("\nKaTeX Errors Sample:")
    for err in report["katex_errors"][:5]:
        print("  -", err)

with open("data/fi_eq/audit_summary.json", "w", encoding="utf-8") as f:
    json.dump(report, f, indent=2)
