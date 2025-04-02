import streamlit as st

# Initialize chat history and active chat in session state
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []
if 'active_chat' not in st.session_state:
    st.session_state['active_chat'] = []

# Clear chat history function
def clear_chat_history():
    st.session_state['chat_history'] = []

# Start new conversation function
def start_new_conversation():
    st.session_state['active_chat'] = []

# Store active chat to chat history
def store_messages_in_chat_history():
    if st.session_state['active_chat']:
        st.session_state['chat_history'].append(st.session_state['active_chat'])
    st.session_state['active_chat'] = []

# Sidebar layout
with st.sidebar:
    st.header("Chat History")
    
    # Display chat history
    if st.session_state['chat_history']:
        for index, chat in enumerate(st.session_state['chat_history']):
            st.write(f"Conversation {index + 1}:")
            for message in chat:
                st.write(f"- {message}")
    else:
        st.write("No chat history available.")
    
    # Clear Chat History Button
    if st.button("Clear Chat History"):
        clear_chat_history()

    # Start New Conversation Button
    if st.button("Start New Conversation"):
        start_new_conversation()

    # Store Messages in Chat History Button
    if st.button("Store Messages in CH"):
        store_messages_in_chat_history()

# Main conversation area
st.title("Chatbot")

# User input
user_input = st.text_input("You:", "")

# Active chat handling
if user_input:
    # Append user input to the active chat
    st.session_state['active_chat'].append(f"You: {user_input}")
    
    # Generate bot response (replace this with your chatbot's response generation)
    bot_response = "This is a placeholder response."
    
    # Display bot response
    st.session_state['active_chat'].append(f"Bot: {bot_response}")
    
    # Show active chat
    st.write("### Active Chat:")
    for message in st.session_state['active_chat']:
        st.write(message)

