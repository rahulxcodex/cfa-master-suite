# Self-contained compiler for CFA Fixed Income & Equity Question Bank
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data", "fi_eq")
MASTER_JSON = os.path.join(DATA_DIR, "cfa_fi_eq_master.json")
OUTPUT_HTML = os.path.join(BASE_DIR, "fi_eq_dashboard.html")

def compile_suite():
    if not os.path.exists(MASTER_JSON):
        print(f"Master JSON missing at {MASTER_JSON}")
        return
    with open(MASTER_JSON, "r", encoding="utf-8") as f:
        questions = json.load(f)
    print(f"Compiling {len(questions)} questions into {OUTPUT_HTML}...")
    
    # Run compiler
    from scripts.generate_full_dashboard import dashboard_html_template
    html_full = dashboard_html_template.replace("__QUESTION_BANK_DATA__", json.dumps(questions, ensure_ascii=False))
    with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
        f.write(html_full)
    print("Compilation successful.")

if __name__ == "__main__":
    compile_suite()
