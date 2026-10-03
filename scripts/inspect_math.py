import json
import re

with open(r'c:\Users\Rahul\Documents\antigravity\Finance\data\cfa_question_bank_master.json', encoding='utf-8') as f:
    data = json.load(f)

for q in data:
    if q['id'] in ['L1-Q002', 'L2-V01-Q3', 'L2-V25-Q2']:
        all_text = f"{q.get('question','')} {str(q.get('options',{}))} {q.get('explanation','')}"
        for m in re.finditer(r'(?<!\\)\$(?=\d)', all_text):
            idx = m.start()
            print(q['id'], repr(all_text[max(0, idx-15):min(len(all_text), idx+25)]))
