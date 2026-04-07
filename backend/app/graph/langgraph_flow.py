from typing import TypedDict
from langgraph.graph import StateGraph
from app.agents.sql_agent import run_sql_agent


class AgentState(TypedDict):
    question: str
    result: dict


def sql_agent_node(state: AgentState):

    question = state["question"]

    result = run_sql_agent(question)

    return {
        "result": result
    }


def create_graph():

    graph = StateGraph(AgentState)

    graph.add_node("sql_agent", sql_agent_node)

    graph.set_entry_point("sql_agent")

    graph.set_finish_point("sql_agent")

    return graph.compile()