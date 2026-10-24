import requests
import streamlit as st

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="Medical Assistant",
    page_icon="🩺",
    layout="centered"
)

# --------------------------------------------------
# Custom CSS
# --------------------------------------------------
st.markdown("""
<style>

body {
    background-color: #F7F7F7;
}

.title {
    color: brown;
    font-size: 40px;
    font-weight: bold;
    text-align: center;
    margin-bottom: 25px;
}

.box {
    border: 1px solid black;
    border-radius: 8px;
    padding: 15px;
    background-color: white;
    margin-bottom: 20px;
}

.response-box {
    border: 1px solid black;
    border-radius: 8px;
    background-color: #FFF3CD;
    color: black;
    padding: 18px;
    min-height: 220px;
    white-space: pre-wrap;
    font-size: 16px;
}

div.stButton > button {
    width: 100%;
    background-color: #1976D2;
    color: white;
    font-size: 18px;
    border-radius: 8px;
    height: 45px;
}

div.stButton > button:hover {
    background-color: #0D47A1;
    color: white;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# Title
# --------------------------------------------------
st.markdown(
    "<div class='title'>🩺 Medical Assistant 🩺</div>",
    unsafe_allow_html=True
)

# --------------------------------------------------
# Query Input
# --------------------------------------------------
st.markdown("<div class='box'>", unsafe_allow_html=True)

query = st.text_input(
    "Enter your medical query",
    placeholder="Example: What are the symptoms of diabetes?"
)

st.markdown("</div>", unsafe_allow_html=True)

# --------------------------------------------------
# Ask Button
# --------------------------------------------------
if st.button("Ask"):

    if not query.strip():
        st.warning("Please enter a medical query.")

    else:

        try:

            response = requests.post(
                "http://127.0.0.1:8000/ask",
                json={"query": query},
                timeout=60
            )

            response.raise_for_status()

            data = response.json()

            answer = data.get("answer", "No answer returned.")

            st.markdown(
                f"""
                <div class="response-box">
                <h4>📋 Response</h4>
                {answer}
                </div>
                """,
                unsafe_allow_html=True
            )

        except requests.exceptions.ConnectionError:
            st.error("❌ Unable to connect to the FastAPI server.")

        except requests.exceptions.Timeout:
            st.error("❌ Request timed out.")

        except Exception as e:
            st.error(f"❌ {e}")