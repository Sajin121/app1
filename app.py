import pandas as pd
import streamlit as st
import plotly.express as px
import numpy as np
import requests


st.set_page_config(page_title='Warehousing & Distribution Cost', 
	page_icon=":bar_chart:", layout="wide")

df = pd.read_excel(io="Bidata.xlsx", engine="openpyxl",
	sheet_name="3_to_7", skiprows=2, usecols="A:L", 
	nrows=1000, )



st.sidebar.header("Please Filter Here:")

Empnam = st.sidebar.multiselect("Select the Employee:", 
	options=df["Empnam"].unique(), default=df["Empnam"].unique() )

Location = st.sidebar.multiselect("Select the Location:", 
	options=df["Location"].unique(), default=df["Location"].unique() )



df = df.query( "Empnam == @Empnam & Location == @Location" )


st.title(":bar_chart: Warehousing & Distribution Cost")
st.header('TOTAl EXPENSES = 1,216,021.63 SR')


st.markdown("##")


fig2 = px.bar(df, title="<b>Total Expenses Based On Employee<b>", x="Empnam", y="Total", color="Empnam", template="plotly_white")

   

fig4 = px.bar(df, title="<b>Total Expenses Based On Location<b>", x="Location", y="Total", color="Location")



left_column, right_column = st.columns(2)
left_column.plotly_chart(fig2, use_container_width=True)
right_column.plotly_chart(fig4, use_container_width=True)

st.markdown("---")


fig1 = px.pie(df,
                title='Total Expenses Based On Employee',
                values='Total',
                names='Empnam')

st.plotly_chart(fig1)




fig3 = px.pie(df,
                title='Total Expenses Based On Location',
                values='Total',
                names='Location')



fig6 = px.pie(df,
                title='Total Expenses Based On Month',
                values='Total',
                names='Period')

left_column, right_column = st.columns(2)
left_column.plotly_chart(fig3, use_container_width=True)
right_column.plotly_chart(fig6, use_container_width=True)



hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)


df = df.astype(str)
st.dataframe(df)
 