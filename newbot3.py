import streamlit as st
import random
import time
from pymongo import MongoClient

# MongoDB connection
MONGO_URI = "mongodb+srv://akarshhotte:pqpU90lGipRysX20@exptbot.l8uvxsr.mongodb.net/"
client = MongoClient(MONGO_URI)
db = client["Chatbott"]  # Database name
db_collection = db["messages"]  # Collection name

st.title("GUI Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Sidebar for chat history controls
with st.sidebar:
    st.header("Chat History")
    if st.button("Clear chat history"):
        st.session_state.chat_history = []

    if st.button("Store messages in CH"):
        st.session_state.chat_history.extend(st.session_state.messages)

    for msg in st.session_state.chat_history:
        st.write(f'**{msg["role"].capitalize()}**: {msg["content"]}')

# Fixed "Start new conversation" button
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("Start new conversation"):
        st.session_state.messages = []
        st.rerun()

# Display chat history messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What's going on?"):
    with st.chat_message("user"):
        st.markdown(prompt)

    # Add user message to chat history
    user_msg = {"role": "user", "content": prompt}
    st.session_state.messages.append(user_msg)
    db_collection.insert_one(user_msg)  # Store in MongoDB

    # Streamed response emulator
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

    # Display the bot message in a container
    with st.chat_message("assistant"):
        response = "".join(response_generator())
        st.markdown(response)

    # Add assistant message to chat history
    assistant_msg = {"role": "assistant", "content": response}
    st.session_state.messages.append(assistant_msg)
    db_collection.insert_one(assistant_msg)  # Store in MongoDB
