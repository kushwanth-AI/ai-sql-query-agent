from app.database.postgres_client import execute_sql


def sql_execution_tool(query: str):

    try:

        result = execute_sql(query)

        return result

    except Exception as e:

        return str(e)