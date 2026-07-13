import time
import streamlit as st
from chat_engine import ChatEngine

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="AI Healthcare Report Assistant",
    page_icon="🏥",
    layout="centered"
)

# ==========================================
# SIDEBAR
# ==========================================

with st.sidebar:

    st.title("🏥 AI Healthcare")

    st.markdown("---")

    st.subheader("Features")

    st.markdown("""
- 🤖 AI Healthcare Assistant
- 📄 Secure Report Access
- 🔒 Email & Password Authentication
- 📋 AI Report Explanation
""")

    st.markdown("---")

    st.info(
        "This assistant provides general healthcare information only.\n\n"
        "**It is NOT a substitute for professional medical advice.**"
    )

    st.markdown("---")

    if st.button("🗑️ New Chat", use_container_width=True):

        st.session_state.chat_engine = ChatEngine()

        st.session_state.messages = [
            {
                "role": "assistant",
                "content":
"""👋 Hello!

Welcome to the **AI Healthcare Report Assistant**.

I can help you with:

• 🏥 General healthcare questions

• 📄 Securely access your health reports

• 🤖 Explain your medical reports in simple language

How may I assist you today?"""
            }
        ]

        st.rerun()

# ==========================================
# TITLE
# ==========================================

st.title("🏥 AI Healthcare Report Assistant")

st.caption(
    "Your AI-powered assistant for healthcare guidance and secure health report access."
)

# ==========================================
# SESSION
# ==========================================

if "chat_engine" not in st.session_state:
    st.session_state.chat_engine = ChatEngine()

if "messages" not in st.session_state:

    st.session_state.messages = [
        {
            "role": "assistant",
            "content":
"""👋 Hello!

Welcome to the **AI Healthcare Report Assistant**.

I can help you with:

• 🏥 General healthcare questions

• 📄 Securely access your health reports

• 🤖 Explain your medical reports in simple language

How may I assist you today?"""
        }
    ]

# ==========================================
# DISPLAY CHAT HISTORY
# ==========================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ==========================================
# USER INPUT
# ==========================================

prompt = st.chat_input("Type your message...")

if prompt:

    # -----------------------
    # USER MESSAGE
    # -----------------------

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    # -----------------------
    # AI RESPONSE
    # -----------------------

    with st.spinner("🤖 Thinking..."):

        response = st.session_state.chat_engine.process_message(prompt)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )

    # -----------------------
    # Typing Animation
    # -----------------------

    with st.chat_message("assistant"):

        placeholder = st.empty()

        typed_text = ""

        words = response.split()

        for word in words:

            typed_text += word + " "

            placeholder.markdown(typed_text)

            time.sleep(0.03)

# ==========================================
# FOOTER
# ==========================================

st.markdown("---")

st.caption(
    "⚠️ This assistant provides general healthcare information only and should not replace consultation with a qualified healthcare professional."
)