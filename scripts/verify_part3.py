import json
import os
import re

DATA_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "l2_questions_part3.json")

def verify():
    with open(DATA_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)

    print(f"Total questions loaded: {len(data)}")
    assert len(data) == 40, f"Expected 40 questions, got {len(data)}"

    vignettes = {}
    for i, q in enumerate(data):
        vid = q.get('vignette_id')
        vignettes[vid] = vignettes.get(vid, 0) + 1
        
        # Verify keys
        for key in ["id", "level", "module", "topic", "vignette_id", "vignette_title", "vignette_text", "los", "question", "options", "answer", "explanation"]:
            assert key in q, f"Question {q.get('id')} missing {key}"
            
        assert q['level'] == 2, f"Expected level 2, got {q['level']}"
        assert q['answer'] in ["A", "B", "C"], f"Invalid answer {q['answer']} in {q['id']}"
        assert set(q['options'].keys()) == {"A", "B", "C"}, f"Invalid options keys in {q['id']}"

    print(f"Vignettes verified (8 vignettes, 5 questions each): {vignettes}")
    assert len(vignettes) == 8, f"Expected 8 vignettes, got {len(vignettes)}"
    assert all(count == 5 for count in vignettes.values()), "Each vignette must have exactly 5 questions"

    assert data[0]['id'] == "L2-V31-Q1"
    assert data[-1]['id'] == "L2-V38-Q5"

    bare_dollar = re.compile(r'(?<!\\)\$(?=\d)')
    violations = []
    for q in data:
        full_text = f"{q['question']} {str(q['options'])} {q['explanation']} {q['vignette_text']}"
        m = bare_dollar.findall(full_text)
        if m:
            violations.append((q['id'], m))

    print(f"Bare dollar violations: {len(violations)}")
    assert len(violations) == 0, f"Found bare dollar violations: {violations}"
    print("ALL VERIFICATIONS PASSED PERFECTLY!")

if __name__ == "__main__":
    verify()
