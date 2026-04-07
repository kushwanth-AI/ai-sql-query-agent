from app.database.postgres_client import execute_sql

result = execute_sql("SELECT 1;")

print(result)