
import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="Advanced RAG Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("Advanced RAG Assistant")
st.caption("Conversational AI to assist with company policy ")

# Initialize session
if "session_id" not in st.session_state:

    response = requests.post(
        f"{API_URL}/session",
        timeout=30
    )

    response.raise_for_status()

    st.session_state.session_id = (
        response.json()["session_id"]
    )

if "messages" not in st.session_state:
    st.session_state.messages = []


# Sidebar
with st.sidebar:
    st.header("Chat Settings")

    if st.button("New Conversation"):
        response = requests.post(
            f"{API_URL}/session",
            timeout=30
        )

        response.raise_for_status()

        st.session_state.session_id = (
            response.json()["session_id"]
        )

        st.session_state.messages = []
        st.rerun()

    st.caption(
        f"Session: {st.session_state.session_id[:8]}"
    )


# Display conversation
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# User input
question = st.chat_input("Ask your question...")

if question:

    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            try:
                response = requests.post(
                    f"{API_URL}/chat",
                    json={
                        "session_id": st.session_state.session_id,
                        "question": question
                    },
                    timeout=180
                )

                response.raise_for_status()

                answer = response.json()["answer"]

                st.markdown(answer)

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": answer
                })

            except requests.RequestException as e:
                st.error(f"API Error: {e}")
                st.session_state.messages.pop()

