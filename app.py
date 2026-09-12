import streamlit as st
from src.chatbot import Chatbot


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="NLP Chatbot",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

.main {
    padding-top: 1rem;
}

.chatbot-header {
    text-align: center;
    padding: 25px 10px 10px 10px;
}

.chatbot-title {
    font-size: 46px;
    font-weight: 700;
}

.chatbot-subtitle {
    font-size: 18px;
    color: #9aa0aa;
    margin-top: 5px;
}

.info-box {
    background-color: #191c24;
    border: 1px solid #30343d;
    border-radius: 12px;
    padding: 20px 25px;
    margin: 20px 0 25px 0;
}

.info-title {
    font-size: 20px;
    font-weight: 600;
    margin-bottom: 12px;
}

.info-item {
    margin: 8px 0;
    font-size: 16px;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.title("🤖 NLP Chatbot")

    st.divider()

    st.header("About")

    st.write(
        "This chatbot uses Natural Language Processing "
        "and Machine Learning to understand user messages "
        "and generate suitable responses."
    )

    st.divider()

    st.header("Technologies")

    st.write("🐍 Python")
    st.write("🧠 Natural Language Processing")
    st.write("📊 TF-IDF Vectorization")
    st.write("⚙️ Logistic Regression")
    st.write("🎨 Streamlit")

    st.divider()

    st.header("Topics I Understand")

    st.write("👋 Greetings")
    st.write("💻 Skills")
    st.write("📁 Projects")
    st.write("🎓 Education")
    st.write("💼 Internship")
    st.write("🐍 Python")
    st.write("🧠 NLP")
    st.write("🤖 Machine Learning")
    st.write("📊 TF-IDF")
    st.write("⚙️ Logistic Regression")
    st.write("🤖 About the Bot")
    st.write("🙏 Thanks")
    st.write("👋 Goodbye")


# ============================================================
# INITIALIZE CHATBOT
# ============================================================

if "chatbot" not in st.session_state:

    with st.spinner("Initializing NLP Chatbot..."):

        st.session_state.chatbot = Chatbot()


# ============================================================
# CHAT HISTORY
# ============================================================

if "messages" not in st.session_state:

    st.session_state.messages = []


# ============================================================
# MAIN HEADER
# ============================================================

st.markdown(
    '<div class="chatbot-header">',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="chatbot-title">🤖 NLP Chatbot</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="chatbot-subtitle">'
    'An intelligent chatbot powered by Natural Language Processing'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# TRY ASKING SECTION
# ============================================================

st.markdown(
    '<div class="info-box">',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="info-title">💡 Try asking:</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="info-item">• What are your skills?</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="info-item">• Tell me about your projects</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="info-item">• What did you study?</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="info-item">• Tell me about your internship</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="info-item">• What is NLP?</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="info-item">• What is Python?</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="info-item">• How does this chatbot work?</div>',
    unsafe_allow_html=True
)

st.markdown(
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# DISPLAY PREVIOUS MESSAGES
# ============================================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.write(message["content"])


# ============================================================
# CHAT INPUT
# ============================================================

user_input = st.chat_input(
    "Type your message here..."
)


# ============================================================
# PROCESS USER MESSAGE
# ============================================================

if user_input:

    # Store user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    # Generate chatbot response
    response = st.session_state.chatbot.get_response(
        user_input
    )

    # Store chatbot response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )

    # Refresh interface
    st.rerun()