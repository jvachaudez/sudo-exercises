import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from test_utils import run_from_command_line

CASES = [
    {"name": "Nombre pair", "args": [12], "expected": True},
    {"name": "Nombre impair", "args": [7], "expected": False},
    {"name": "Zéro", "args": [0], "expected": True},
    {"name": "Nombre négatif pair", "args": [-8], "expected": True},
    {"name": "Nombre négatif impair", "args": [-5], "expected": False},
]

run_from_command_line("is_even", CASES)
