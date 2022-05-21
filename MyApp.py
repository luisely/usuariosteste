import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title='Usuarios Office 365',
    layout='wide'
    )

st.write(""" 
# My first app
Hello *world!*
""")

df = pd.read_excel(
    io='teste.xlsx',
    engine='openpyxl',
    sheet_name='users',
    usecols='A:I',
    nrows=500,
    )

#st.dataframe(df)



# ----SIDEBAR ----------------------------------------------------

st.sidebar.header("Filtros ")
licences = st.sidebar.multiselect(
    "Selecione a licença: ",
    options=df["licences"].unique(),
    default=df["licences"].unique(),
)

df_selection = df.query(
    "licences == @licences"
)

st.dataframe(df_selection)