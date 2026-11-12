import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from test_utils import run_from_command_line

CASES = [
    {"name": "Factorielle de cinq", "args": [5], "expected": 120},
    {"name": "Factorielle de zéro", "args": [0], "expected": 1},
    {"name": "Factorielle de un", "args": [1], "expected": 1},
    {"name": "Factorielle de huit", "args": [8], "expected": 40320},
    {"name": "Valeur négative", "args": [-3], "raises": ValueError},
]

run_from_command_line("factorial", CASES)
