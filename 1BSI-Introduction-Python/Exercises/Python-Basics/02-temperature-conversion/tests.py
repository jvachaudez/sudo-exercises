import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from test_utils import run_from_command_line

CASES = [
    {"name": "Point de congélation", "args": [0], "expected": 32},
    {"name": "Point d’ébullition", "args": [100], "expected": 212},
    {"name": "Températures égales", "args": [-40], "expected": -40},
    {"name": "Valeur décimale", "args": [37.5], "expected": 99.5},
]

run_from_command_line("celsius_to_fahrenheit", CASES)
