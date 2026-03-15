import streamlit as st
import google.generativeai as genai
from google.generativeai.types import Resolution

st.set_page_config(page_title="Career Pivot AI", layout="centered")
st.title("🚀 Career Pivot AI: Get Hired at Top Tech")

api_key = st.sidebar.text_input("Enter Gemini API Key", type="password")

if api_key:
    try:
        # Step 1: Configure API
        genai.configure(api_key=api_key)
        
        # Step 2: Use the most basic model name that works everywhere
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        jd_text = st.text_area("Paste Job Description (JD) here:")
        resume_text = st.text_area("Paste your Resume text here:")

        if st.button("Analyze & Optimize"):
            if jd_text and resume_text:
                with st.spinner('AI is analyzing...'):
                    # Step 3: Minimal call to avoid version errors
                    response = model.generate_content(
                        contents=[f"Compare this Resume: {resume_text} and JD: {jd_text}. List 3 gaps and a cold email."],
                    )
                    st.success("Analysis Complete!")
                    st.markdown(response.text)
            else:
                st.error("Please paste both Resume and JD.")
    except Exception as e:
        st.error(f"Error: {e}")
        st.info("Tip: Try to generate a NEW API key in Google AI Studio if this persists.")
else:
    st.warning("Please enter your Gemini API key in the sidebar.")
