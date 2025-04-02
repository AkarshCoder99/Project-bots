import streamlit as st
import random
import time

st.title("GUI Chatbot")

 # Mongo DB setup
from pymongo import MongoClient
DB_NAME = "chatbot"
COLLECTION_NAME = "exptbot"

 # connect to mongo DB

client = MongoClient('mongodb+srv://akarshhotte:12345@exptbot.l8uvxsr.mongodb.net/?retryWrites=true&w=majority&appName=Exptbot')
db = client["chatbot"]
collection = db["exptbot"]   

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
    st.session_state.messages.append({"role": "user", "content": prompt})

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
        response = st.write_stream(response_generator())

    # Add assistant message to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})

   