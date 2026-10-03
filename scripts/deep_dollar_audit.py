import json
import re

files = [
    "data/fi_eq/l1_fixed_income.json",
    "data/fi_eq/l1_equity.json",
    "data/fi_eq/l2_fixed_income.json",
    "data/fi_eq/l2_equity.json"
]

currency_signs_found = []

for fpath in files:
    with open(fpath, "r", encoding="utf-8") as f:
        data = json.load(f)
    for q in data:
        qid = q["id"]
        # extract all non-math text by removing $$...$$ and $...$
        text = json.dumps(q, ensure_ascii=False)
        # remove display math
        no_math = re.sub(r'\$\$.*?\$\$', '', text, flags=re.DOTALL)
        # remove inline math
        no_math = re.sub(r'\$.*?\$', '', no_math, flags=re.DOTALL)
        
        # Now check if any '$' remains in no_math!
        if '$' in no_math:
            currency_signs_found.append((qid, "Unpaired or outside-math dollar sign found!"))
        
        # Also check inside math if someone wrote e.g. $\$$ or $\$\d
        inside_math_matches = re.findall(r'\$(.*?)\$', text)
        for m in inside_math_matches:
            # check if it starts with a dollar sign like $$ or contains \$$
            if '\\$' in m or m.strip().startswith('$'):
                currency_signs_found.append((qid, f"Suspicious inside math: {m}"))

print(f"Total outside-math or suspicious dollars: {len(currency_signs_found)}")
for item in currency_signs_found[:10]:
    print(item)
