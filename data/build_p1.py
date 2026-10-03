import json
import re
import sys
import os

from gen_m1 import questions as q1
from gen_m2 import questions as q2
from gen_m3 import questions as q3
from gen_m4 import questions as q4
from gen_m5 import questions as q5
from gen_m6 import questions as q6

all_questions = q1 + q2 + q3 + q4 + q5 + q6

print(f"Total questions collected: {len(all_questions)}")
assert len(all_questions) == 90, f"Expected 90 questions, got {len(all_questions)}"

# Validate IDs
for idx, q in enumerate(all_questions, start=1):
    expected_id = f"L1-Q{idx:03d}"
    assert q["id"] == expected_id, f"Item {idx} has id {q['id']}, expected {expected_id}"
    assert q["level"] == 1, f"Item {expected_id} level is {q['level']}"
    assert "module" in q and q["module"], f"Missing module in {expected_id}"
    assert "topic" in q and q["topic"], f"Missing topic in {expected_id}"
    assert "los" in q and q["los"], f"Missing los in {expected_id}"
    assert "question" in q and q["question"], f"Missing question in {expected_id}"
    assert "options" in q and isinstance(q["options"], dict), f"Invalid options in {expected_id}"
    assert set(q["options"].keys()) == {"A", "B", "C"}, f"Options keys mismatch in {expected_id}"
    assert q["answer"] in {"A", "B", "C"}, f"Invalid answer in {expected_id}"
    assert "explanation" in q and q["explanation"], f"Missing explanation in {expected_id}"

# Verify modules count
module_counts = {}
for q in all_questions:
    m = q["module"]
    module_counts[m] = module_counts.get(m, 0) + 1

print("Module counts:", module_counts)
expected_modules = {
    "m1-intro": 15,
    "m2-standards": 15,
    "m3-income-statement": 15,
    "m4-balance-sheet": 15,
    "m5-cash-flow": 15,
    "m6-ratios": 15,
}
assert module_counts == expected_modules, f"Module counts mismatch: {module_counts}"

# Verify no bare $ currency signs (must be USD, EUR, GBP or \$ or KaTeX math $...$)
bare_dollar_pattern = re.compile(r'(?<!\\)\$\d+')
for q in all_questions:
    for field in ["question", "explanation"] + list(q["options"].values()):
        # Check if there is a pattern like $500 or $12,000 outside of math or unescaped
        matches = bare_dollar_pattern.findall(field)
        if matches:
            raise ValueError(f"Found bare currency dollar sign {matches} in {q['id']}: {field}")

output_path = os.path.join(os.path.dirname(__file__), "l1_questions_part1.json")
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(all_questions, f, indent=2, ensure_ascii=False)

print(f"Successfully wrote {len(all_questions)} questions to {output_path}")

# Validate with json.load
with open(output_path, "r", encoding="utf-8") as f:
    loaded = json.load(f)

print(f"Successfully validated JSON reload. Item count: {len(loaded)}")
assert len(loaded) == 90
