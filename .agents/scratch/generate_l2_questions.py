import json
import os
import re

DATA_FILE = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "data", "l2_questions_part1.json")

print("Target JSON file:", DATA_FILE)
