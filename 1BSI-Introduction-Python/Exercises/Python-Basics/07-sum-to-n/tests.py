import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from test_utils import run_from_command_line

CASES = [
    {"name": "Somme jusqu’à cinq", "args": [5], "expected": 15},
    {"name": "Zéro", "args": [0], "expected": 0},
    {"name": "Un", "args": [1], "expected": 1},
    {"name": "Somme jusqu’à cent", "args": [100], "expected": 5050},
    {"name": "Valeur négative", "args": [-1], "raises": ValueError},
]

run_from_command_line("sum_to_n", CASES)
