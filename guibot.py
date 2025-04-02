import streamlit as st
import random
import time

st.title("GUI Chatbot")

# initialize chat history

if "messages" not in st.session_state:
    st.session_state.messages = []

# display chat history messages 

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# accept user input

if prompt:= st.chat_input(" Whats going on ?"):

    with st.chat_message("user"):
        st.markdown(prompt)

# add user message to chat history

st.session_state.messages.append({"role" : "user", "content": prompt})

# streamed response emulator

def response_generator():
    response = random.choice(
        [ "Hello there! How can I assist you today?",
            "Hi, human! Is there anything I can help you with?",
            "Do you need help?",
            "Can I help you with something",
            "I'm you assistant, I'll be happy to help you with anything"
            ]
    )

    
    for word in response.split():
        yield word + " "
        time.sleep(0.05)

# display the bot message in a container 

with st.chat_message("assistant"):
    response = st.write_stream(response_generator())

# add assisstant to the chat response

st.session_state.messages.append({"role":"assisstant", "content": response})

 
