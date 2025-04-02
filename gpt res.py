

  ########## chat gpt response ###########
import streamlit as st

# Create a simple input field for user message
user_message = st.text_input("Your message:")

# Display the user's message
if user_message:
    with st.chat_message("user"):
        st.write(user_message)

    # Display a bot response
    with st.chat_message("bot"):
        st.write("Hello User! How can I help you?")

