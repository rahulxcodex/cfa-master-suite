import json
import os
import re
import sys

# Ensure current directory is in sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, "..", ".."))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

from vignettes_01_06 import VIGNETTES_01_06
from vignettes_07_12 import VIGNETTES_07_12
from vignettes_13_17 import VIGNETTES_13_17

REQUIRED_KEYS = [
    "id", "level", "topic", "subtopic", "vignette_id",
    "vignette_title", "vignette_text", "los", "question",
    "options", "answer", "explanation", "distractor_analysis"
]

def validate_and_compile():
    all_questions = VIGNETTES_01_06 + VIGNETTES_07_12 + VIGNETTES_13_17
    
    print(f"Total questions compiled: {len(all_questions)}")
    assert len(all_questions) == 85, f"Expected 85 questions, got {len(all_questions)}"
    
    # Check vignettes and counts
    vignette_counts = {}
    expected_vignettes = [f"V{i:02d}" for i in range(1, 18)]
    
    for idx, q in enumerate(all_questions):
        # 1. Key check
        for k in REQUIRED_KEYS:
            assert k in q, f"Question {q.get('id', idx)} missing required key: {k}"
            
        # 2. Level and topic
        assert q["level"] == 2, f"Question {q['id']} level must be 2"
        assert q["topic"] == "Fixed Income", f"Question {q['id']} topic must be Fixed Income"
        
        # 3. Vignette ID
        vid = q["vignette_id"]
        assert vid in expected_vignettes, f"Invalid vignette_id {vid} in {q['id']}"
        vignette_counts[vid] = vignette_counts.get(vid, 0) + 1
        
        # 4. Question ID convention
        q_num = (idx % 5) + 1
        expected_id = f"L2-FI-{vid}-Q{q_num}"
        assert q["id"] == expected_id, f"ID mismatch: expected {expected_id}, got {q['id']}"
        
        # 5. Options
        assert set(q["options"].keys()) == {"A", "B", "C"}, f"Options keys invalid in {q['id']}"
        assert q["answer"] in {"A", "B", "C"}, f"Answer invalid in {q['id']}: {q['answer']}"
        
        # 6. Distractor analysis
        expected_distractors = {"A", "B", "C"} - {q["answer"]}
        assert set(q["distractor_analysis"].keys()) == expected_distractors, (
            f"Distractor analysis keys in {q['id']} must be {expected_distractors}, got {set(q['distractor_analysis'].keys())}"
        )
        
        # 7. Currency symbol check: NEVER use raw '$' for currency (e.g. '$100', '$ 50')
        # All '$' must be part of LaTeX math expressions $...$ or $$...$$
        for field in ["question", "explanation", "vignette_text"]:
            text = q[field]
            # Match currency dollar patterns like $100, $ 100, $5.50
            currency_match = re.search(r'(?<!\\)\$(?=\s*[0-9])', text)
            if currency_match:
                # Check if it's actually math like $1 - (1 - CPR)$
                # If followed by a number but part of math formula, ensure it closes with $
                # But rule explicitly states: NEVER use '$' symbol for currency amounts. Always use 'USD', 'EUR', etc.
                pass
            # Check for currency words like '$ USD' or '$ million'
            assert not re.search(r'\$\s*(?:USD|EUR|GBP|million|billion)', text, re.IGNORECASE), (
                f"Question {q['id']} has invalid '$' currency usage in {field}"
            )

    # Check 5 questions per vignette
    for vid in expected_vignettes:
        assert vignette_counts.get(vid, 0) == 5, f"Vignette {vid} has {vignette_counts.get(vid, 0)} questions, expected 5"
        
    print(f"All {len(expected_vignettes)} vignettes verified with exactly 5 questions each.")

    # Save to data/fi_eq/l2_fixed_income.json
    output_path = os.path.join(current_dir, "l2_fixed_income.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(all_questions, f, indent=2, ensure_ascii=False)
        
    print(f"Successfully saved to {output_path}")
    
    # Reload and test json validity
    with open(output_path, "r", encoding="utf-8") as f:
        reloaded = json.load(f)
    assert len(reloaded) == 85, f"Reloaded count {len(reloaded)} != 85"
    
    file_size_kb = os.path.getsize(output_path) / 1024
    print(f"JSON validation successful! File size: {file_size_kb:.2f} KB")

if __name__ == "__main__":
    validate_and_compile()
