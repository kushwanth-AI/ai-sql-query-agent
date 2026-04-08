from app.llm.gemini_client import ask_gemini
from app.database.neo4j_client import Neo4jClient
from app.tools.sql_tool import sql_execution_tool

neo4j_client = Neo4jClient()


def run_sql_agent(question: str):

    schema = neo4j_client.get_schema()

    sql_prompt = f"""
You are an expert PostgreSQL generator.

Database schema:
{schema}

Convert the user question to a PostgreSQL SQL query.

Return ONLY SQL query.

User Question:
{question}
"""

    sql_query = ask_gemini(sql_prompt)

    # 🔴 If LLM failed stop execution
    if "quota" in sql_query.lower() or "failed" in sql_query.lower():

        return {
            "sql_query": None,
            "data": None,
            "answer": "LLM service temporarily unavailable. Please try again."
        }

    # execute SQL
    result = sql_execution_tool(sql_query)

    explain_prompt = f"""
User Question: {question}

SQL Query:
{sql_query}

Database Result:
{result}

Explain the result clearly.
"""

    explanation = ask_gemini(explain_prompt)

    return {
        "sql_query": sql_query,
        "data": result,
        "answer": explanation
    }


# "                                           cohere                                                      "

# from app.llm.cohere_client import ask_llm
# from app.database.neo4j_client import Neo4jClient
# from app.tools.sql_tool import sql_execution_tool

# neo4j_client = Neo4jClient()


# def run_sql_agent(question: str):

#     # Get schema from Neo4j knowledge graph
#     schema = neo4j_client.get_schema()

#     # Prompt to generate SQL
#     sql_prompt = f"""
# You are an expert PostgreSQL generator.

# Database schema relationships:
# {schema}

# Convert the user question into a PostgreSQL SQL query.

# Rules:
# - Return ONLY SQL query
# - Do not explain
# - Do not use markdown

# User Question:
# {question}
# """

#     sql_query = ask_llm(sql_prompt)

#     # If LLM returned error message stop execution
#     if sql_query is None or "⚠️" in sql_query.lower():
#         return {
#             "sql_query": None,
#             "data": None,
#             "answer": "LLM service temporarily unavailable. Please try again."
#         }

#     # Optional safety check
#     if not sql_query.lower().strip().startswith(("select", "with")):
#         return {
#             "sql_query": sql_query,
#             "data": None,
#             "answer": "Generated SQL query is not safe to execute."
#         }

#     # Execute SQL query
#     result = sql_execution_tool(sql_query)

#     # Prompt for explanation
#     explain_prompt = f"""
# User Question:
# {question}

# SQL Query:
# {sql_query}

# Database Result:
# {result}

# Explain the answer clearly for the user.
# """

#     explanation = ask_llm(explain_prompt)

#     return {
#         "sql_query": sql_query,
#         "data": result,
#         "answer": explanation
#     }
