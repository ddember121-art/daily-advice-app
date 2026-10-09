import streamlit as st
import requests


st.set_page_config(
    page_title="Daily Advice App",
    page_icon="💡",
    layout="centered"
)


st.caption("Hi! Welcome to your Daily Advice App. This app provides you with a fpiece of advice every time you click the button below.")
st.title("💡 Daily Advice App")
st.divider()


if "advice" not in st.session_state:
    st.session_state.advice = "Click the button below to generate advice!"


def get_advice():
    url = "https://api.adviceslip.com/advice"
    
    with st.spinner("Generating a piece of advice for you... Please wait..."):
        try:
            response = requests.get(url)
            data = response.json()
            st.session_state.advice = data["slip"]["advice"]
        except Exception:
            st.session_state.advice = "Failed to connect to API Server. Check your internet connection and try again."


with st.container(border=True):
    st.markdown("### 📜 *Advice for Today:*")
    st.info(f'"{st.session_state.advice}"')
    
    
    if st.button("✨ Get Advice", use_container_width=True):
        get_advice()

