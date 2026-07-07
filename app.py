import streamlit as st
from google import genai


client = genai.Client(api_key="API KEY(Didn't add due to security concerns)")

st.title(" AI Chatbot with Memory")


if "messages" not in st.session_state:
    st.session_state.messages = []


if st.button(" Clear Chat"):
    st.session_state.messages = []
    st.rerun()

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

prompt = st.chat_input("Type your message...")

if prompt:
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.write(prompt)


    history = ""
    for msg in st.session_state.messages:
        history += f"{msg['role']}: {msg['content']}\n"

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=history
    )

    reply = response.text

    st.session_state.messages.append(
        {"role": "assistant", "content": reply}
    )

    with st.chat_message("assistant"):
        st.write(reply)