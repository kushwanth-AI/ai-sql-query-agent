flowchart TD

A[User Question] --> B[FastAPI Backend]
B --> C[LangGraph AI Agent]
C --> D[Retrieve Schema from Neo4j Knowledge Graph]
D --> E[Build Structured Prompt]
E --> F[LLM Generates SQL Query]
F --> G[SQL Validation]
G --> H[Execute Query using PostgreSQL]
H --> I[Return Database Result]
I --> J[LLM Generates Natural Language Explanation]
J --> K[API Response]
K --> L[Streamlit UI Displays Result]

<!-- your full explanation content continues... -->