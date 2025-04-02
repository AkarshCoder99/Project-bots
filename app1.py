import streamlit as st 

with st.chat_message(name = "user", avatar = "user"):
    st.write("Hello User")

prompt = st.chat_input("Type something here")
if prompt:
    st.write(f"user has sent the following message: {prompt}")







