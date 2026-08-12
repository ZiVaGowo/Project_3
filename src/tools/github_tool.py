import os
from typing import Dict
from github import Github


def fetch_repository_files(
    repo_name: str, file_paths: list[str]
) -> Dict[str, str]:
    """Получает файлы из репозитория."""
    token = os.getenv("GITHUB_TOKEN")
    if not token or token.startswith("ghp_your"):
        # Мок для разработки, если токен не задан
        return {
            "calculator.py": "def divide(a: float, b: float) -> float:\n    return a / b\n"
        }

    g = Github(token)
    repo = g.get_repo(repo_name)
    files = {}
    for path in file_paths:
        content = repo.get_contents(path)
        files[path] = content.decoded_content.decode("utf-8")
    return files


def create_pull_request(
    repo_name: str, branch_name: str, file_path: str, new_code: str, title: str
) -> str:
    """Эмуляция/создание PR на GitHub."""
    token = os.getenv("GITHUB_TOKEN")
    if not token or token.startswith("ghp_your"):
        return f"https://github.com/example-user/{repo_name}/pull/1 (Mock PR)"

    g = Github(token)
    repo = g.get_repo(repo_name)
    sb = repo.get_branch("main")
    repo.create_git_ref(f"refs/heads/{branch_name}", sb.commit.sha)
    file_content = repo.get_contents(file_path, ref=branch_name)
    repo.update_file(
        file_path, "fix: auto fix bug by AI Agent", new_code, file_content.sha, branch=branch_name
    )
    pr = repo.create_pull(
        title=title, body="Auto-generated fix by Bug Investigator Agent", head=branch_name, base="main"
    )
    return pr.html_url