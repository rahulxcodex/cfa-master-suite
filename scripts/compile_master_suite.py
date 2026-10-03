import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data", "fi_eq")
MASTER_JSON = os.path.join(DATA_DIR, "cfa_fi_eq_master.json")
OUTPUT_HTML = os.path.join(BASE_DIR, "fi_eq_dashboard.html")
BUILD_SCRIPT = os.path.join(BASE_DIR, "build_fi_eq_notes.py")

files = [
    ("L1 Fixed Income", os.path.join(DATA_DIR, "l1_fixed_income.json")),
    ("L1 Equity", os.path.join(DATA_DIR, "l1_equity.json")),
    ("L2 Fixed Income", os.path.join(DATA_DIR, "l2_fixed_income.json")),
    ("L2 Equity", os.path.join(DATA_DIR, "l2_equity.json"))
]

all_questions = []

for label, fpath in files:
    with open(fpath, "r", encoding="utf-8") as f:
        qs = json.load(f)
        for q in qs:
            # Normalize fields
            if "subject" not in q:
                if "Fixed Income" in q.get("topic", "") or "FI" in q.get("id", ""):
                    q["subject"] = "Fixed Income"
                else:
                    q["subject"] = "Equity"
            all_questions.append(q)
        print(f"Loaded {len(qs)} questions from {label}")

with open(MASTER_JSON, "w", encoding="utf-8") as f:
    json.dump(all_questions, f, indent=2, ensure_ascii=False)

print(f"Master JSON compiled: {len(all_questions)} questions at {MASTER_JSON}")
