import streamlit as st
import random
import time
from pymongo import MongoClient
from datetime import datetime

st.title("GUI Chatbot")

# MongoDB setup
DB_NAME = "chatbot"
COLLECTION_NAME = "exptbot"

# Connect to MongoDB
client = MongoClient('mongodb+srv://akarshhotte:pqpU90lGipRysX20@exptbot.l8uvxsr.mongodb.net/')
db = client["chatbot"]
collection = db["exptbott"]

# Initialize chat sessions
if "chat_sessions" not in st.session_state:
    st.session_state.chat_sessions = {}

if "current_session" not in st.session_state:
    st.session_state.current_session = None

# Sidebar for session management
with st.sidebar:
    st.header("Chat History")
    
    # Create a new session
    if st.button("Start New Conversation"):
        session_id = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        st.session_state.chat_sessions[session_id] = []
        st.session_state.current_session = session_id
        st.rerun()
    
    # Select an existing session
    session_list = list(st.session_state.chat_sessions.keys())
    if session_list:
        session_selection = st.selectbox("Select a session", session_list, index=session_list.index(st.session_state.current_session) if st.session_state.current_session else 0)
        st.session_state.current_session = session_selection
    
    # Clear all chat sessions
    if st.button("Clear All Chat Sessions"):
        st.session_state.chat_sessions = {}
        st.session_state.current_session = None
        st.rerun()

# Display chat messages for the selected session
if st.session_state.current_session:
    messages = st.session_state.chat_sessions[st.session_state.current_session]
    
    for message in messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Accept user input
    if prompt := st.chat_input("What's going on?"):
        with st.chat_message("user"):
            st.markdown(prompt)
        
        messages.append({"role": "user", "content": prompt})

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
        
        messages.append({"role": "assistant", "content": response})
