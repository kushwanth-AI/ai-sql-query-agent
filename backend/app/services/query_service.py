from app.graph.langgraph_flow import create_graph

graph = create_graph()


def process_query(question: str):

    response = graph.invoke(
        {"question": question}
    )

    return response