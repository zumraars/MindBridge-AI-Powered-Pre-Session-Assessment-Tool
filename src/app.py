import streamlit as st
from chatbot import generate_response
from safety import check_safety

st.set_page_config(page_title="MindBridge Chatbot", page_icon="🧠")

st.title("MindBridge AI")
st.subheader("Pre-Session Assessment Chatbot Prototype")

st.write(
    "This chatbot is a prototype for general informational and pre-session support. "
    "It does not provide diagnosis, therapy, or medical advice."
)

user_input = st.text_area("How are you feeling today?")

if st.button("Send"):
    if not user_input.strip():
        st.warning("Please enter a message.")
    else:
        safety_result = check_safety(user_input)

        if safety_result == "high_risk":
            st.error(
                "I'm really sorry you're feeling this way. I can't provide crisis support, "
                "but please contact emergency services or a licensed mental health professional immediately."
            )
        else:
            response = generate_response(user_input)
            st.write(response)
