from src.graph import build_app

if __name__ == "__main__":
    app = build_app()

    # Обычный запуск (исправление деления на ноль)
    sample_input = {
        "issue_title": "ZeroDivisionError in divide function",
        "stack_trace": (
            'Traceback (most recent call last):\n  File "calculator.py", line 2, in divide\n'
            "    return a / b\nZeroDivisionError: division by zero"
        ),
        "repo_files": {},
        "proposed_code": None,
        "test_logs": None,
        "test_passed": False,
        "fix_attempts": 0,
        "pr_url": None,
    }

    print("=== Старт выполнения Bug Investigator Agent ===")
    result = app.invoke(sample_input)

    print("\n=== Результат работы ===")
    if result.get("pr_url"):
        print(f"Успешно! Ссылка на PR: {result['pr_url']}")
        print("\nПредложенный код:")
        print(result.get("proposed_code"))
    else:
        print("Не удалось автоматически исправить ошибку.")