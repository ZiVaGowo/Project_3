from src.state import BugInvestigatorState
from src.tools.github_tool import create_pull_request


def pr_creator_node(state: BugInvestigatorState) -> dict:
    print("\n🚀 [4. PR Creator] Создание Pull Request...")
    pr_url = create_pull_request(
        repo_name="example/repo",
        branch_name="fix/zero-division",
        file_path="calculator.py",
        new_code=state.get("proposed_code", ""),
        title=state.get("issue_title", "Fix Bug"),
    )
    return {"pr_url": pr_url}