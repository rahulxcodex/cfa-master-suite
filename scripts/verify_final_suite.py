import json
import os
import re

MASTER_JSON = "data/fi_eq/cfa_fi_eq_master.json"
HTML_FILE = "fi_eq_dashboard.html"

assert os.path.exists(MASTER_JSON), "Master JSON missing"
assert os.path.exists(HTML_FILE), "HTML Dashboard missing"

with open(MASTER_JSON, "r", encoding="utf-8") as f:
    qs = json.load(f)

print(f"Total questions loaded: {len(qs)}")
assert len(qs) == 415, f"Expected 415, got {len(qs)}"

ids = set()
l1_fi = 0
l1_eq = 0
l2_fi = 0
l2_eq = 0
vignettes_fi = set()
vignettes_eq = set()

for q in qs:
    qid = q["id"]
    assert qid not in ids, f"Duplicate ID: {qid}"
    ids.add(qid)

    lvl = q["level"]
    subj = q.get("subject", "")
    top = q.get("topic", "")

    if lvl == 1:
        if "Fixed" in subj or "Fixed" in top or "FI" in qid:
            l1_fi += 1
        else:
            l1_eq += 1
    elif lvl == 2:
        vid = q.get("vignette_id", "")
        if "Fixed" in subj or "Fixed" in top or "FI" in qid:
            l2_fi += 1
            vignettes_fi.add(vid)
        else:
            l2_eq += 1
            vignettes_eq.add(vid)

    # Check distractor analysis
    ans = q["answer"]
    non_ans = [o for o in ["A", "B", "C"] if o != ans]
    dist = q.get("distractor_analysis", {})
    for na in non_ans:
        assert na in dist, f"Missing distractor {na} in {qid}"

print(f"L1 Fixed Income: {l1_fi}")
print(f"L1 Equity: {l1_eq}")
print(f"L2 Fixed Income: {l2_fi} (Vignettes: {len(vignettes_fi)})")
print(f"L2 Equity: {l2_eq} (Vignettes: {len(vignettes_eq)})")

# Check HTML size and elements
html_size = os.path.getsize(HTML_FILE)
print(f"HTML File Size: {html_size} bytes")
assert html_size > 500000, "HTML file unexpectedly small"

with open(HTML_FILE, "r", encoding="utf-8") as f:
    html_text = f.read()

assert "yieldChart" in html_text, "Missing Yield Chart simulation"
assert "treeVisualContainer" in html_text, "Missing Tree simulation"
assert "dupontChart" in html_text, "Missing DuPont simulation"
assert "durationChart" in html_text, "Missing Duration simulation"
assert "Merton Structural Model" in html_text, "Missing Merton diagram"
assert "Porter's Five Forces" in html_text or "Porter" in html_text, "Missing Porter diagram"

print("ALL FINAL VERIFICATION CHECKS PASSED PERFECTLY!")
