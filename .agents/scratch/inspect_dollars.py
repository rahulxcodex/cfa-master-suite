# -*- coding: utf-8 -*-
import sys
import os
import re

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_v16_v23 import get_vignettes_16_to_23
from generate_v24_v30 import get_vignettes_24_to_30

for vig_list in [get_vignettes_16_to_23(), get_vignettes_24_to_30()]:
    for v_text, q_list in vig_list:
        for q in q_list:
            for f in ['vignette_text', 'question', 'explanation']:
                matches = list(re.finditer(r'(?<!\\)\$(?=\d)', q[f]))
                for m in matches:
                    start = max(0, m.start() - 10)
                    end = min(len(q[f]), m.end() + 25)
                    print(f"{q['id']} {f}: {repr(q[f][start:end])}")
            for opt_key, opt_text in q["options"].items():
                matches = list(re.finditer(r'(?<!\\)\$(?=\d)', opt_text))
                for m in matches:
                    start = max(0, m.start() - 10)
                    end = min(len(opt_text), m.end() + 25)
                    print(f"{q['id']} options.{opt_key}: {repr(opt_text[start:end])}")
