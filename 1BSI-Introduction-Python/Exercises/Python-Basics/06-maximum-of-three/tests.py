import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from test_utils import run_from_command_line

CASES = [
    {"name": "Premier maximum", "args": [9, 4, 2], "expected": 9},
    {"name": "Deuxième maximum", "args": [3, 12, 8], "expected": 12},
    {"name": "Troisième maximum", "args": [1, 5, 7], "expected": 7},
    {"name": "Valeurs égales", "args": [6, 6, 2], "expected": 6},
    {"name": "Nombres négatifs", "args": [-8, -2, -5], "expected": -2},
]

run_from_command_line("maximum_of_three", CASES)
