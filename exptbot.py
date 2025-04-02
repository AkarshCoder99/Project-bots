import streamlit as st
import random
import time
from pymongo import MongoClient

# MongoDB Connection
client = MongoClient("mongodb://localhost:27017/")  # Change URI if needed
db = client.chatbot
db_messages = db.messages

st.title("GUI Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = list(db_messages.find({}, {"_id": 0}))

# Sidebar for chat history
st.sidebar.title("Chat History")
for msg in st.session_state.messages:
    st.sidebar.write(f"{msg['role'].capitalize()}: {msg['content']}")

# Display chat history in main chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What's going on?"):
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Store user message in MongoDB
    user_message = {"role": "user", "content": prompt}
    db_messages.insert_one(user_message)
    st.session_state.messages.append(user_message)

    # Generate bot response
    def response_generator():
        response = random.choice([
            "Hello there! How can I assist you today?",
            "Hi, human! Is there anything I can help you with?",
            "Do you need help?",
            "Can I help you with something?",
            "I'm your assistant, I'll be happy to help you with anything."
        ])
        for word in response.split():
            yield word + " "
            time.sleep(0.05)
    
    with st.chat_message("assistant"):
        response = st.write_stream(response_generator())
    
    # Store assistant message in MongoDB
    assistant_message = {"role": "assistant", "content": response}
    db_messages.insert_one(assistant_message)
    st.session_state.messages.append(assistant_message)