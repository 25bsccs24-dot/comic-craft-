import streamlit as st
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

st.set_page_config(page_title="ComicCraft-AI", page_icon="🦊")
st.title("🦊 ComicCraft - AI Comic Creator")

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    api_key = st.text_input("Gemini API Key podu da:", type="password")
    if not api_key:
        st.stop()

client = genai.Client(api_key=api_key)

idea = st.text_area("Story Idea:", "A brave young fox named Leo lives near an enchanted forest")

if st.button("🚀 Generate"):
    with st.spinner("Creating da..."):
        response = client.models.generate_content(
            model="gemini-1.5-flash-lite",
            contents=f"Create a 5 panel comic for kids: {idea}"
        )
        st.write(response.text)