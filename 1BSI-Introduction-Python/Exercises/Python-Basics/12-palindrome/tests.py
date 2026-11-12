import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from test_utils import run_from_command_line

CASES = [
    {"name": "Palindrome simple", "args": ["radar"], "expected": True},
    {"name": "Casse ignorée", "args": ["Kayak"], "expected": True},
    {"name": "Pas un palindrome", "args": ["python"], "expected": False},
    {"name": "Chaîne vide", "args": [""], "expected": True},
    {"name": "Un seul caractère", "args": ["x"], "expected": True},
]

run_from_command_line("is_palindrome", CASES)
