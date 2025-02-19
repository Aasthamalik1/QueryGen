from  dotenv import load_dotenv
# load all the environment variables
load_dotenv()
 
import streamlit as st
import os
import sqlite3
import google.generativeai as genai

#configure api key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#function to load Google Gemini Model and provide sql query as response

def get_gemini_response(ques,prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0],ques])
    return response.text

#function to retrieve query from sql database
def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for i in rows:
        print(i)
    return rows

    # defining prompt
prompt=[  """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENT and has the following columns - NAME, COURSE, CONTACT, GPA
     \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
    \nExample 2 - Tell me all the students studying in Data Science class?, 
    the SQL command will be something like this SELECT * FROM STUDENT 
    where CLASS="Data Science"; 
    also the sql code should not have ``` in beginning or end and sql word in output

    """
    ]

    ## streamlit app
import streamlit as st
import time

# Set up the page config
st.set_page_config(page_title="I can retrieve any SQL query")

# Add custom CSS for better UI
st.markdown("""
    <style>
        .stTextInput > div > input {
            background-color: peach;
            color: #333;
            font-size: 16px;
        }
        .stButton > button {
            background-color: #FF5733;
            color: white;
            font-size: 16px;
            padding: 10px;
            border-radius: 5px;
        }
         .stDataFrame {
            border-radius: 15px;
            border: 2px solid #FF5733;  /* Adds a border to the table */
            overflow: hidden;  /* Ensures the table contents don't spill out */
        }
        .stDataFrame table {
            border-collapse: collapse;  /* Removes spacing between table cells */
        }
        .stDataFrame th, .stDataFrame td {
            padding: 10px;  /* Adds padding to each table cell */
            text-align: center;  /* Centers the text in each cell */
        }
        .stDataFrame th {
            background-color: #FF5733;  /* Sets header background color */
            color: white;  /* Sets header text color to white */
        }
        .stDataFrame td {
            background-color: #f2f2f2;  /* Light grey background for data cells */
        }   
    </style>
""", unsafe_allow_html=True)

# Page content
st.header("QueryGEN")
st.markdown("""
    <h3 style='text-align: center; color: #5F6368;'> 
        🧠 Retrieve data without sql🤖
    </h3> 
""", unsafe_allow_html=True)

ques = st.text_input("Input your query:", key="input")
submit = st.button("Ask the Question")

if submit:
    if not ques.strip():  # Check if the input is empty
        st.warning("Please enter a SQL query question!")
    else:
        with st.spinner('Fetching data...'):
            time.sleep(2)  # Simulate waiting time for SQL query execution
            response = get_gemini_response(ques, prompt)
            data = read_sql_query(response, "student")

        st.subheader("The Response is:")

        if data:
            st.dataframe(data)  # Display the result in a table format
        else:
            st.write("No results found.")
