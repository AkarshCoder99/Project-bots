import streamlit as st

st.title("Copycat bot")

# with st.chat_message(name = "user", avatar = "assistant"):
#     st.write("Hello User")

# initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# display messages from history from app rerun

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# response to user input 

if prompt := st.chat_input("Type something here"):


# display user message in chat container 
   with st.chat_message( name ="User1", avatar = "user"):
       st.markdown(prompt)

# add user message to chat history 

st.session_state.messages.append({"role" : "User1", "content": prompt})

response = f"Copycat: {prompt}"

# display assistant response in chat message container

with st.chat_message("Assistant"):
    st.markdown(response)

# add assisstent response to chat history

st.session_state.messages.append({"role" : "Assistant", "content": response})




