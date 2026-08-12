import ast
import subprocess


def verify_ast_safety(code: str) -> tuple[bool, str]:
    """Проверяет синтаксис и заблокированные модули (os, subprocess)."""
    if not code.strip():
        return False, "Сгенерированный код пуст."

    try:
        tree = ast.parse(code)
        for node in ast.walk(tree):
            if isinstance(node, (ast.Import, ast.ImportFrom)):
                names = (
                    [alias.name for alias in node.names]
                    if isinstance(node, ast.Import)
                    else [node.module]
                )
                for name in names:
                    if name in ["os", "subprocess", "sys", "shutil"]:
                        return False, f"Обнаружен запрещенный импорт '{name}'"
        return True, "AST проверка пройдена"
    except SyntaxError as e:
        return False, f"Синтаксическая ошибка в коде: {e}"


def run_tests_in_sandbox(proposed_code: str) -> tuple[bool, str]:
    """Эмуляция запуска pytest."""
    is_safe, ast_msg = verify_ast_safety(proposed_code)
    if not is_safe:
        return False, f"AST Error: {ast_msg}"

    # Логика эмуляции: если в коде есть проверка деления на ноль, тест пройден
    if "ZeroDivisionError" in proposed_code or "b == 0" in proposed_code or "b != 0" in proposed_code:
        return True, "pytest: 1 passed in 0.05s"

    return False, "FAILED test_calculator.py::test_divide - ZeroDivisionError: division by zero"