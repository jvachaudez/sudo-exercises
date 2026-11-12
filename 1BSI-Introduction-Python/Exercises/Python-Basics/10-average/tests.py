import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from test_utils import run_from_command_line

CASES = [
    {"name": "Trois entiers", "args": [[10, 12, 14]], "expected": 12},
    {"name": "Nombres négatifs", "args": [[-6, -2, 2]], "expected": -2},
    {"name": "Valeurs décimales", "args": [[1.5, 2.5]], "expected": 2},
    {"name": "Une seule valeur", "args": [[7]], "expected": 7},
    {"name": "Liste vide", "args": [[]], "raises": ValueError},
]

run_from_command_line("average", CASES)
