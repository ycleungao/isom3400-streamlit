import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Personal Expense Tracker")

if 'expenses' not in st.session_state:
  st.session_state = pd.DataFrame(columns=['Date','Category','Amount','Description'])

with st.form("espense_form"):
  st.subheader("Add New Expense")
  date = st.date_input("Date")
  category = st.selectbox("Category",["Food","Transport","Entertainment","Bills","Other"])
  amount = st.number_input("Amount", min_value = 0.0, step = 0.01)
  description = st.text_input("Description")

submitted = st.form_submit_button("Add Expense")
if submitted:
  new_expense = pd.DataFraame({
    'Date': [date],
    'Category': [category],
    'Amount': [amount],
    'Description': [description]
  })
