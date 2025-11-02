import streamlit as st
import random

# --- PAGE CONFIG ---
st.set_page_config(page_title="Would You Date Me?", page_icon="💖", layout="centered")

# --- STYLES ---
st.markdown("""
    <style>
    body {
        background-color: #FAEEE6;
        font-family: 'Arial', sans-serif;
    }
    .stApp {
        background-color: #FAEEE6;
    }
    div.block-container {
        text-align: center;
    }
    .big-text {
        font-size: 28px;
        font-weight: bold;
        color: #333;
        margin-bottom: 20px;
    }
    .yes-button, .no-button {
        font-size: 20px !important;
        padding: 12px 30px;
        border-radius: 12px;
        color: white;
        border: none;
        margin: 10px;
        cursor: pointer;
    }
    .yes-button {
        background-color: #4CAF50;
    }
    .no-button {
        background-color: #f44336;
    }
    .heart {
        color: red;
        font-size: 30px;
        position: absolute;
    }
    </style>
""", unsafe_allow_html=True)

# --- SESSION STATE ---
if "no_clicks" not in st.session_state:
    st.session_state.no_clicks = 0
if "yes_clicked" not in st.session_state:
    st.session_state.yes_clicked = False
if "message" not in st.session_state:
    st.session_state.message = ""

# --- LOGIC FUNCTIONS ---
def click_no():
    st.session_state.no_clicks += 1
    clicks = st.session_state.no_clicks

    if clicks == 1:
        st.session_state.message = "Come on, just one date?"
    elif clicks < 4:
        st.session_state.message = "Still no? You're making me sad 😢"
    elif clicks < 7:
        st.session_state.message = "You sure? I'm running out of charm 😭"
    elif clicks < 10:
        st.session_state.message = "Please... 🥺"
    elif clicks < 15:
        st.session_state.message = "You broke my heart 💔"
    else:
        st.session_state.message = "Button's gone... your loss 😭"

def click_yes():
    st.session_state.yes_clicked = True

# --- UI ---
st.markdown("<div class='big-text'>Would you date me?</div>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    if st.button("YES 💚", key="yes_button", help="Say yes!"):
        click_yes()
with col2:
    if not st.session_state.yes_clicked:
        st.button("NO 💔", key="no_button", on_click=click_no)

# --- RESPONSE AREA ---
if st.session_state.yes_clicked:
    st.success("💞 Tara na ganda, go out on a date with me! 💞")
    # Draw hearts falling (simulated with emojis)
    hearts = "".join(random.choice(["❤️", "💖", "💕", "💘", "💞"]) for _ in range(100))
    st.markdown(f"<div style='font-size:25px'>{hearts}</div>", unsafe_allow_html=True)
else:
    st.write(st.session_state.message)
