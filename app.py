import streamlit as st
import time
st.header("Starting")
if st.button("Click Me"):
    st.write("Button Clicked!")
if st.checkbox("Check Me more"):
    for i in range(30):
        time.sleep(10)
    st.write("Checkbox Checked!")