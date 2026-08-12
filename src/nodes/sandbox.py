from src.state import BugInvestigatorState
from src.tools.sandbox_tool import run_tests_in_sandbox


def test_sandbox_node(state: BugInvestigatorState) -> dict:
    print("\n🧪 [3. Test Sandbox] Проверка сгенерированного кода...")
    proposed_code = state.get("proposed_code", "")

    passed, logs = run_tests_in_sandbox(proposed_code)
    if passed:
        print("✅ Тесты пройдены!")
    else:
        print("❌ Тесты не пройдены.")

    return {"test_passed": passed, "test_logs": logs}