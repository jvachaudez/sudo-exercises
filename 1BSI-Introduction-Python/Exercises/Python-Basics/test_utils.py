import contextlib
import importlib.util
import io
import json
import math
import sys


def load_solution(filename):
    spec = importlib.util.spec_from_file_location("sudo_student_solution", filename)
    if spec is None or spec.loader is None:
        raise ImportError("Impossible de charger la solution.")
    module = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
        spec.loader.exec_module(module)
    return module


def values_equal(actual, expected):
    if isinstance(expected, bool):
        return type(actual) is bool and actual is expected
    if isinstance(expected, (int, float)) and not isinstance(expected, bool):
        return (
            isinstance(actual, (int, float))
            and not isinstance(actual, bool)
            and math.isclose(actual, expected, rel_tol=1e-9, abs_tol=1e-9)
        )
    return actual == expected


def execute_case(function, case):
    name = case["name"]
    try:
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            actual = function(*case.get("args", []))
        expected_exception = case.get("raises")
        if expected_exception is not None:
            return {
                "name": name,
                "status": "failed",
                "message": f"Attendu : {expected_exception.__name__} — aucune exception reçue.",
            }
        expected = case.get("expected")
        ok = values_equal(actual, expected)
        return {
            "name": name,
            "status": "passed" if ok else "failed",
            "message": "" if ok else f"Attendu : {expected!r} — obtenu : {actual!r}",
        }
    except Exception as error:
        expected_exception = case.get("raises")
        if expected_exception is not None and isinstance(error, expected_exception):
            return {"name": name, "status": "passed", "message": ""}
        return {
            "name": name,
            "status": "failed",
            "message": f"Exception inattendue : {type(error).__name__}: {error}",
        }


def run_tests(solution_path, function_name, cases):
    try:
        module = load_solution(solution_path)
        function = getattr(module, function_name, None)
        if not callable(function):
            raise AttributeError(f"La fonction {function_name} est introuvable.")
        tests = [execute_case(function, case) for case in cases]
        passed = sum(test["status"] == "passed" for test in tests)
        result = {"passed": passed, "failed": len(tests) - passed, "tests": tests}
    except Exception as error:
        result = {
            "passed": 0,
            "failed": 1,
            "tests": [{
                "name": "Chargement de la solution",
                "status": "failed",
                "message": f"{type(error).__name__}: {error}",
            }],
        }
    print(json.dumps(result, ensure_ascii=False))


def run_from_command_line(function_name, cases):
    if len(sys.argv) != 2:
        print(json.dumps({
            "passed": 0,
            "failed": 1,
            "tests": [{
                "name": "Lancement",
                "status": "failed",
                "message": "Chemin de la solution manquant.",
            }],
        }, ensure_ascii=False))
        return
    run_tests(sys.argv[1], function_name, cases)
