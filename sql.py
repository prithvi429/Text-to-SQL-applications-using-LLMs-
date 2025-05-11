from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import sqlite3
import google.generativeai as genai
import asyncio

# Configure Gemini API
genai.configure(api_key=os.getenv("google_api_key"))

### Function to load Google Gemini model and get response
async def get_gemini_response(prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = await model.generate_content_async([prompt[0], queshion])
    return response.text

# Function to execute SQL query on database
def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.close()
    return rows

# Define your system prompt
prompt = ["""
        You are an expert at converting English questions to SQL queries.
        The SQL database is named 'student' and has the following columns: name, class, section.

        Examples:
        Q: How many records are present?
        A: SELECT COUNT(*) FROM student;

        Q: List all students in class 10.
        A: SELECT * FROM student WHERE class = '10';

        Please return only the SQL query, with no explanations or formatting.
"""
]

# Streamlit App
st.set_page_config(page_title='I can retrieve any sql query')
st.header("gemini app to Retrieve sql Data")

queshion = st.text_input("input: ", key="input")

submit = st.button("ask the queshion")

# if submit is clicked 
if submit:
    response = asyncio.run(get_gemini_response(prompt))
    st.subheader('the responce is')
    st.code(response, language='sql')  # Display SQL response nicely

    try:
        results = read_sql_query(response, "student.db")
        st.subheader("Query Result:")
        for row in results:
            st.write(row)
    except Exception as e:
        st.error(f"SQL Execution Error: {e}")
