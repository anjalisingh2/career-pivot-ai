import streamlit as st
import google.generativeai as genai
from google.generativeai import client

st.set_page_config(page_title="Career Pivot AI", layout="centered")
st.title("🚀 Career Pivot AI")

api_key = st.sidebar.text_input("Enter Gemini API Key", type="password")

if api_key:
    try:
        # Force the version to v1 to avoid the 404 v1beta error
        genai.configure(api_key=api_key, transport='grpc') 
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        jd_text = st.text_area("Paste Job Description (JD) here:")
        resume_text = st.text_area("Paste your Resume text here:")

        if st.button("Analyze"):
            if jd_text and resume_text:
                with st.spinner('AI is working...'):
                    # Basic call
                    response = model.generate_content(f"Analyze this Resume: {resume_text} against JD: {jd_text}. Give 3 gaps and a cold email.")
                    st.success("Done!")
                    st.write(response.text)
            else:
                st.error("Please fill both boxes.")
    except Exception as e:
        st.error(f"Error: {e}")
else:
    st.info("Sidebar mein API Key dalein.")
