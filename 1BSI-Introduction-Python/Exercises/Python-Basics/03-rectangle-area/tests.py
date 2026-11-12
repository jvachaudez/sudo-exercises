import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from test_utils import run_from_command_line

CASES = [
    {"name": "Rectangle simple", "args": [5, 3], "expected": 15},
    {"name": "Carré", "args": [4, 4], "expected": 16},
    {"name": "Dimension nulle", "args": [8, 0], "expected": 0},
    {"name": "Dimensions décimales", "args": [2.5, 4], "expected": 10},
]

run_from_command_line("rectangle_area", CASES)
