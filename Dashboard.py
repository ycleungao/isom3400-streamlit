import streamlit as st

st.title("Retail Business Dashboard")

st.header("Manage Input Section")

st.write("Please enter the monthly sales target and select the region.")
target = st.number_input("Enter monthly sales target(in USD)",min_value = 0,max_value = 1000000,value = 50000)
region = st.selectbox("Select Region",["North","East","South","West"])
st.button("Submit")
st.success(f"Input successfully! Your monthly sales target is {target} in {region} Region! ")
