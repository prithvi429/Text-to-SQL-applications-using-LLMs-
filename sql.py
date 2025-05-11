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
    try:
        # Use the gemini-pro model
        model = genai.GenerativeModel('models/gemini-pro')  # Specify the gemini-pro model
        response = await model.generate_content_async([prompt[0], queshion])
        return response.text
    except Exception as e:
        st.error(f"Error generating response: {e}")
        return ""

# Function to execute SQL query on database
def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.close()
    return rows

# Function to list available models
def list_available_models():
    try:
        models = genai.list_models()
        for model in models:
            print(f"Model ID: {model.id}, Description: {model.description}")
    except Exception as e:
        print(f"Error listing models: {e}")

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
    response = asyncio.run(get_gemini_response(prompt))  # get SQL query string
    
    st.subheader('the responce is')
    st.code(response, language='sql')  # display SQL query
    print(response)  # Corrected print

    try:
        results = read_sql_query(response, "student.db")  # run the SQL query
        st.subheader("Query Result:")
        for row in results:
            st.write(row)
    except Exception as e:
        st.error(f"SQL Execution Error: {e}")


