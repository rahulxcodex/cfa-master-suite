#!/usr/bin/env python3
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

def sanitize_text(text):
    if not isinstance(text, str):
        return text
    # Replace bare '$100' or '$ 100' with '100 USD' or '\$100' if not in math block
    # If it is like "$500,000" or "$50" -> replace with "500,000 USD" or "50 USD"
    # But preserve LaTeX math mode like $E = mc^2$ or $\text{something}$
    def repl(match):
        val = match.group(1)
        suffix = match.group(2) if match.group(2) else ""
        return f"{val}{suffix} USD"

    # Pattern for $123,456 or $123.45 or $10M or $10 million
    pattern = r'(?<!\\)\$\s*(\d+(?:,\d{3})*(?:\.\d+)?)\s*(million|billion|thousand|[MBk])?'
    # Only replace if not preceded by backslash
    cleaned = re.sub(pattern, repl, text)
    return cleaned

def clean_data(obj):
    if isinstance(obj, dict):
        return {k: clean_data(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [clean_data(item) for item in obj]
    elif isinstance(obj, str):
        return sanitize_text(obj)
    return obj

def main():
    print("Sanitizing bare currency symbols across JSON files...")
    for fn in FILES:
        fp = os.path.join(DATA_DIR, fn)
        if not os.path.exists(fp):
            continue
        with open(fp, 'r', encoding='utf-8') as f:
            data = json.load(f)
        cleaned = clean_data(data)
        with open(fp, 'w', encoding='utf-8') as f:
            json.dump(cleaned, f, indent=2, ensure_ascii=False)
        print(f"Sanitized {fn}")

if __name__ == "__main__":
    main()
