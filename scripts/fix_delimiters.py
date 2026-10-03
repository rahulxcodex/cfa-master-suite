import json
import os
import re

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data")
FILES = [
    "l1_questions_part1.json",
    "l1_questions_part2.json",
    "l2_questions_part1.json",
    "l2_questions_part2.json",
    "l2_questions_part3.json"
]

def clean_str(s):
    if not isinstance(s, str):
        return s
    # Fix "$1 USD. " -> "$ 1. "
    s = re.sub(r'\$(\d+)\s+USD\.\s+', r'$ \1. ', s)
    # Fix bare "$100" or "$ 100" that might still exist:
    # If not preceded by \ and not closing a KaTeX block (e.g., at start of line or after space/paren)
    s = re.sub(r'(^|[\s\(])\$(\d+(?:,\d{3})*(?:\.\d+)?)\b', r'\1\2 USD', s)
    # Fix double USD like "USD USD"
    s = re.sub(r'\bUSD\s+USD\b', 'USD', s)
    return s

def clean_data(obj):
    if isinstance(obj, dict):
        return {k: clean_data(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [clean_data(item) for item in obj]
    elif isinstance(obj, str):
        return clean_str(obj)
    return obj

for fn in FILES:
    fp = os.path.join(DATA_DIR, fn)
    with open(fp, 'r', encoding='utf-8') as f:
        data = json.load(f)
    cleaned = clean_data(data)
    with open(fp, 'w', encoding='utf-8') as f:
        json.dump(cleaned, f, indent=2, ensure_ascii=False)
    print(f"Fixed delimiters in {fn}")
