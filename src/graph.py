from langgraph.graph import END, START, StateGraph
from src.nodes.fixer import code_fixer_node
from src.nodes.pr_creator import pr_creator_node
from src.nodes.sandbox import test_sandbox_node
from src.nodes.searcher import code_searcher_node
from src.state import BugInvestigatorState


def should_retry_or_finish(state: BugInvestigatorState) -> str:
    if state.get("test_passed", False):
        return "create_pr"
    if state.get("fix_attempts", 0) >= 3:
        return "fail"
    return "retry"


def build_app():
    builder = StateGraph(BugInvestigatorState)

    builder.add_node("searcher", code_searcher_node)
    builder.add_node("fixer", code_fixer_node)
    builder.add_node("sandbox", test_sandbox_node)
    builder.add_node("pr_creator", pr_creator_node)

    builder.add_edge(START, "searcher")
    builder.add_edge("searcher", "fixer")
    builder.add_edge("fixer", "sandbox")

    builder.add_conditional_edges(
        "sandbox",
        should_retry_or_finish,
        {"create_pr": "pr_creator", "retry": "fixer", "fail": END},
    )

    builder.add_edge("pr_creator", END)
    return builder.compile()