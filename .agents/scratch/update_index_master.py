import json
import os
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MASTER_JSON_PATH = os.path.join(BASE_DIR, "data", "cfa_question_bank_master.json")
INDEX_PATH = os.path.join(BASE_DIR, "index.html")

with open(MASTER_JSON_PATH, "r", encoding="utf-8") as f:
    questions = json.load(f)

print(f"Loaded {len(questions)} questions from {MASTER_JSON_PATH}")

with open(INDEX_PATH, "r", encoding="utf-8") as f:
    html = f.read()

# Replace const MASTER_QUESTION_BANK = [...]
pattern = r'const MASTER_QUESTION_BANK = \[.*?\];\n'
json_str = json.dumps(questions, ensure_ascii=False)
replacement = f"const MASTER_QUESTION_BANK = {json_str};\n"

match = re.search(pattern, html, flags=re.DOTALL)
if match:
    html = html[:match.start()] + replacement + html[match.end():]
    print("Successfully replaced MASTER_QUESTION_BANK in index.html")
else:
    print("Error: Could not locate MASTER_QUESTION_BANK in index.html")

# Add cross-navigation link in header if not already present
if 'fi_eq_dashboard.html' not in html:
    # Find a good spot in the top header or actions bar
    header_target = '<div class="header-actions">'
    if header_target in html:
        suite_btn = '<a href="fi_eq_dashboard.html" class="btn" style="background: rgba(57, 197, 207, 0.15); border: 1px solid var(--accent-cyan); color: var(--accent-cyan); text-decoration: none; font-weight: 600; padding: 6px 14px; border-radius: 6px; margin-right: 10px;">📈 Fixed Income & Equity Suite →</a>'
        html = html.replace(header_target, header_target + '\n      ' + suite_btn)
        print("Added cross-suite navigation button to index.html")
    else:
        # Fallback to after body or main header
        html = html.replace('<header>', '<header>\n  <div style="background: var(--bg-tertiary); border-bottom: 1px solid var(--border-color); padding: 8px 24px; display: flex; justify-content: space-between; align-items: center; font-size: 13px;"><span style="color: var(--text-secondary);">CFA Prep Master Portal</span><a href="fi_eq_dashboard.html" style="color: var(--accent-cyan); font-weight: 600; text-decoration: none;">📈 Switch to Fixed Income & Equity Suite (415 Qs & 9 Simulations) →</a></div>')
        print("Added top bar to index.html")

with open(INDEX_PATH, "w", encoding="utf-8") as f:
    f.write(html)

print(f"Updated index.html ({os.path.getsize(INDEX_PATH)} bytes)")
