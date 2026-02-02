import streamlit as st
import google.generativeai as genai

# PASTE YOUR API KEY INSIDE THE QUOTES BELOW
genai.configure(api_key="PASTE_YOUR_KEY_HERE")
model = genai.GenerativeModel('gemini-1.5-flash')

st.title("🌴 Holiday AI Companion")
user_input = st.text_input("What are you looking at right now?")

if st.button("Tell me something cool!"):
    prompt = f"I am on holiday looking at {user_input}. Tell me a fun fact."
    response = model.generate_content(prompt)
    st.write(response.text)