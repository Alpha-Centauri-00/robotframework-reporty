import streamlit as st
import sqlite3



def create_table():
    st.markdown(
        
        r"""
        <style>
        .stDeployButton {
                visibility: hidden;
            }
        #MainMenu {visibility: hidden;}

        </style>
        """, unsafe_allow_html=True
    )
    
    conn = sqlite3.connect(r'D:\robotframework-reporty\robot.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tests")
    results = cursor.fetchall()
    st.dataframe(results, width=1000, height=500)
    # for result in results:
    #     st.table(result)
    conn.close()

    # Convert the tuple data into a list of lists
    

    # Display the data in a table using st.table()
    #st.info(data)

