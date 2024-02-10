import streamlit as st

number = st.number_input('Insert a number', min_value = 1, max_value = 12, step = 1)
st.write('The number is ', number)