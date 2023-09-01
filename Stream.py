import streamlit as st
import pandas as pd
import numpy as np
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

st.write("""
# My first app
Hello *world!*
""")
 
#df = pd.read_excel("C:/Users/user8/Desktop/RM_Report_RM_Data 2.xlsx")
#df.head()
#st.line_chart(df, x=df['RM_Release_Status'], y=df['Final_Scope_For_Migration'])


chart_data = pd.DataFrame({
    'col1' : np.random.randn(20),
    'col2' : np.random.randn(20),
    'col3' : np.random.choice(['A','B','C'], 20)
})

st.line_chart(
    chart_data,
    x = 'col1',
    y = 'col2',
    color = 'col3'
)

