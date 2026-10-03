# -*- coding: utf-8 -*-
import re

text = "Translated Gross Profit = $200 \\times 0.1250 = 25.00$ million USD."
print("Before:", text)
print("Matches before:", re.findall(r'(?<!\\)\$(?=\d)', text))

# Format with space after $
clean_text = re.sub(r'(?<!\\)\$(?=\d)', '$ ', text)
print("After:", clean_text)
print("Matches after:", re.findall(r'(?<!\\)\$(?=\d)', clean_text))
