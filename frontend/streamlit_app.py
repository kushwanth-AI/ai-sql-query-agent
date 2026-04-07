import streamlit as st
import requests

API_URL = "http://localhost:8000/query"

st.title("AI SQL Assistant")

question = st.text_input("Ask a database question")

if st.button("Submit"):

    response = requests.post(
        API_URL,
        json={"question": question}
    )

    data = response.json()

    st.subheader("Generated SQL")
    st.code(data["result"]["sql_query"])

    st.subheader("Query Result")
    st.write(data["result"]["data"])

    st.subheader("Explanation")
    st.write(data["result"]["answer"])