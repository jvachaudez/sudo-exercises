import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from test_utils import run_from_command_line

CASES = [
    {"name": "Mot simple", "args": ["bonjour"], "expected": 3},
    {"name": "Majuscules et minuscules", "args": ["PYTHON"], "expected": 2},
    {"name": "Aucune voyelle", "args": ["rhythms"], "expected": 1},
    {"name": "Chaîne vide", "args": [""], "expected": 0},
    {"name": "Phrase avec espaces", "args": ["Une belle journée"], "expected": 7},
]

run_from_command_line("count_vowels", CASES)
