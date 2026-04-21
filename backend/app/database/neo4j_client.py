from neo4j import GraphDatabase
from app.config import settings


class Neo4jClient:

    def __init__(self):
        self.driver = GraphDatabase.driver(
            settings.NEO4J_URI,
            auth=(settings.NEO4J_USER, settings.NEO4J_PASSWORD)
        )

    def get_schema(self):

        query = """
        MATCH (t:Table)-[r]->(c:Table)
        RETURN t.name as table1, type(r) as relation, c.name as table2
        """

        try:
            with self.driver.session() as session:
                result = session.run(query)
                data = [record.data() for record in result]

                if not data:
                    return []

                return data

        except Exception as e:
            print("Neo4j schema fetch error:", e)
            return []
