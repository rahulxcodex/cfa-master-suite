import json
import os

files = [
    'data/fi_eq/l1_fixed_income.json',
    'data/fi_eq/l1_equity.json',
    'data/fi_eq/l2_fixed_income.json',
    'data/fi_eq/l2_equity.json'
]

total = 0
for fpath in files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            data = json.load(f)
            print(f"{fpath}: count={len(data)}, keys={list(data[0].keys())}")
            total += len(data)
    else:
        print(f"Missing: {fpath}")

print(f"Total across 4 files: {total}")
