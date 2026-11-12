import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from test_utils import run_from_command_line

CASES = [
    {"name": "Nombre positif", "args": [8], "expected": "positif"},
    {"name": "Nombre négatif", "args": [-3], "expected": "négatif"},
    {"name": "Zéro", "args": [0], "expected": "nul"},
    {"name": "Petit nombre positif", "args": [0.01], "expected": "positif"},
]

run_from_command_line("number_sign", CASES)
