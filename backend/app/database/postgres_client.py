import psycopg2
from app.config import settings

def execute_sql(query: str):

    conn = psycopg2.connect(
        host=settings.POSTGRES_HOST,
        database=settings.POSTGRES_DB,
        user=settings.POSTGRES_USER,
        password=settings.POSTGRES_PASSWORD,
        port=settings.POSTGRES_PORT
    )

    try:
        cursor = conn.cursor()
        cursor.execute(query)

        # Check if query returns data
        if cursor.description:
            rows = cursor.fetchall()
        else:
            conn.commit()
            rows = None

        return rows

    except Exception as e:
        print("Database error:", e)
        return None

    finally:
        cursor.close()
        conn.close()