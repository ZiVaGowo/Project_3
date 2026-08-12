from typing import Dict, Optional, TypedDict


class BugInvestigatorState(TypedDict):
    issue_title: str
    stack_trace: str
    repo_files: Dict[str, str]
    proposed_code: Optional[str]
    test_logs: Optional[str]
    test_passed: bool
    fix_attempts: int
    pr_url: Optional[str]