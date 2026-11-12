import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from test_utils import run_from_command_line

CASES = [
    {"name": "Entier positif", "args": [5], "expected": 10},
    {"name": "Zéro", "args": [0], "expected": 0},
    {"name": "Entier négatif", "args": [-7], "expected": -14},
    {"name": "Nombre décimal", "args": [2.5], "expected": 5},
]

run_from_command_line("double_number", CASES)
