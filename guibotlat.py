import streamlit as st
import random
import time
from pymongo import MongoClient

# MongoDB Connection
client = MongoClient("mongodb://localhost:27017/")  # Change URI if needed
db = client.chatbot
db_messages = db.messages

st.title("GUI Chatbot")

# Initialize chat history from MongoDB
if "messages" not in st.session_state:
    # Fetch chat history from MongoDB and store it in session_state
    st.session_state.messages = list(db_messages.find({}, {"_id": 0}))

# Sidebar for chat history and buttons
with st.sidebar:
    st.title("Chat History")

    # Display existing messages from chat history
    if st.session_state.messages:
        for msg in st.session_state.messages:
            st.write(f"{msg['role'].capitalize()}: {msg['content']}")
    else:
        st.write("No chat history available.")
    
    # Clear Chat History Button
    clear_button = st.button("Clear Chat History")
    if clear_button:
        st.session_state.messages = []  # Reset session state to clear the chat history
        st.experimental_rerun()  # Refresh the app to reflect changes

    # Start New Conversation Button
    new_convo_button = st.button("Start New Conversation")
    if new_convo_button:
        st.session_state.messages = []  # Clear active conversation
        st.experimental_rerun()  # Refresh to start fresh conversation
    
    # Store Messages in Chat History Button
    store_button = st.button("Store Messages in CH")
    if store_button:
        if st.session_state.messages:
            for msg in st.session_state.messages:
                db_messages.insert_one(msg)  # Store messages in MongoDB
            st.success("Messages stored in chat history.")

# Display active chat messages in the main window
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What's going on?"):
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Store user message in MongoDB
    user_message = {"role": "user", "content": prompt}
    db_messages.insert_one(user_message)  # Insert message into MongoDB
    st.session_state.messages.append(user_message)  # Add to session state for live update

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
    db_messages.insert_one(assistant_message)  # Insert message into MongoDB
    st.session_state.messages.append(assistant_message)  # Add to session state for live update
