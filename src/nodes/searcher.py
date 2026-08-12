from src.state import BugInvestigatorState
from src.tools.github_tool import fetch_repository_files


def code_searcher_node(state: BugInvestigatorState) -> dict:
    print("\n🔍 [1. Code Searcher] Сбор контекста кода...")
    files = fetch_repository_files("example/repo", ["calculator.py"])
    return {"repo_files": files, "fix_attempts": 0}