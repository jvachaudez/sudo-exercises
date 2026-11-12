import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from test_utils import run_from_command_line

CASES = [
    {"name": "Table de trois", "args": [3], "expected": [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]},
    {"name": "Table de un", "args": [1], "expected": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]},
    {"name": "Table de zéro", "args": [0], "expected": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]},
    {"name": "Table négative", "args": [-2], "expected": [-2, -4, -6, -8, -10, -12, -14, -16, -18, -20]},
]

run_from_command_line("multiplication_table", CASES)
