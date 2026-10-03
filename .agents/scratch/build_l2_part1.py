# build_l2_part1.py
import json
import os
import re
import sys

# Add .agents/scratch to path
scratch_dir = os.path.dirname(os.path.abspath(__file__))
if scratch_dir not in sys.path:
    sys.path.append(scratch_dir)

from generate_vignettes_13 import get_vignettes_topic13
from generate_vignettes_14 import get_vignettes_topic14

def main():
    q13 = get_vignettes_topic13()
    q14 = get_vignettes_topic14()
    
    all_q = q13 + q14
    print(f"Loaded {len(q13)} Topic 13 questions and {len(q14)} Topic 14 questions.")
    print(f"Total questions: {len(all_q)}")
    
    # Validation checks
    assert len(all_q) == 90, f"Expected 90 questions, got {len(all_q)}"
    
    vignette_counts = {}
    id_set = set()
    errors = []
    currency_warnings = []
    
    req_fields = [
        "id", "level", "module", "topic", "vignette_id", "vignette_title",
        "vignette_text", "los", "question", "options", "answer", "explanation"
    ]
    
    for idx, q in enumerate(all_q):
        qid = q.get("id")
        if not qid:
            errors.append(f"Index {idx} missing id")
            continue
        if qid in id_set:
            errors.append(f"Duplicate id: {qid}")
        id_set.add(qid)
        
        # Check required fields
        for f in req_fields:
            if f not in q or q[f] is None or q[f] == "":
                errors.append(f"{qid} missing or empty field: {f}")
                
        # Check level
        if q.get("level") != 2:
            errors.append(f"{qid} level is not 2: {q.get('level')}")
            
        # Check options
        opts = q.get("options", {})
        for opt_key in ["A", "B", "C"]:
            if opt_key not in opts or not opts[opt_key]:
                errors.append(f"{qid} missing option {opt_key}")
                
        # Check answer
        if q.get("answer") not in ["A", "B", "C"]:
            errors.append(f"{qid} invalid answer: {q.get('answer')}")
            
        # Vignette tracking
        vid = q.get("vignette_id")
        vignette_counts[vid] = vignette_counts.get(vid, 0) + 1
        
        # Currency check: (?<!\\)\$(?=\d)
        all_text = f"{q.get('vignette_text', '')} {q.get('question', '')} {str(opts)} {q.get('explanation', '')}"
        bare_dollar = re.findall(r'(?<!\\)\$(?=\d)', all_text)
        if bare_dollar:
            currency_warnings.append(f"{qid} has bare dollar followed by digit: {bare_dollar}")
            
        # KaTeX balance check: count unescaped $ signs
        # In KaTeX, single $ or double $$ should appear in matching pairs
        unescaped_dollars = re.findall(r'(?<!\\)\$', all_text)
        if len(unescaped_dollars) % 2 != 0:
            errors.append(f"{qid} has unbalanced unescaped $ signs: count = {len(unescaped_dollars)}")

    print(f"\nVignette distribution (15 expected, 6 questions each):")
    for vid in sorted(vignette_counts.keys()):
        print(f"  {vid}: {vignette_counts[vid]} questions")
        if vignette_counts[vid] != 6:
            errors.append(f"Vignette {vid} has {vignette_counts[vid]} questions instead of 6")
            
    if currency_warnings:
        print("\n[CURRENCY WARNINGS]:")
        for cw in currency_warnings:
            print(" ", cw)
            
    if errors:
        print(f"\n[VALIDATION ERRORS] Found {len(errors)} errors:")
        for err in errors:
            print(" ", err)
        sys.exit(1)
        
    print("\nAll pre-save validation checks PASSED cleanly!")
    
    # Save to target JSON file
    base_dir = os.path.dirname(os.path.dirname(scratch_dir))
    out_path = os.path.join(base_dir, "data", "l2_questions_part1.json")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(all_q, f, indent=2, ensure_ascii=False)
        
    print(f"\n[SUCCESS] Saved 90 questions to {out_path} ({os.path.getsize(out_path)} bytes)")
    
    # Re-verify with json.load
    with open(out_path, "r", encoding="utf-8") as f:
        reloaded = json.load(f)
    print(f"[RELOAD VERIFICATION] Successfully reloaded {len(reloaded)} items from disk.")

if __name__ == "__main__":
    main()
