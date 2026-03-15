import streamlit as st
import google.generativeai as genai

# Page Configuration
st.set_page_config(page_title="Career Pivot AI", layout="centered")
st.title("🚀 Career Pivot AI: Get Hired at Top Tech")

# Sidebar for API Key (Gemini API free milta hai)
api_key = st.sidebar.text_input("Enter Gemini API Key", type="password")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')

    # User Input
    jd_text = st.text_area("Paste Job Description (JD) here:")
    resume_text = st.text_area("Paste your Resume text here:")

    if st.button("Analyze & Optimize"):
        prompt = f"""
        Act as a Senior Recruiter. Compare this Resume and JD.
        Resume: {resume_text}
        JD: {jd_text}
        
        Provide:
        1. 3 Keywords missing in Resume.
        2. 2 Professional Bullet points for the experience section.
        3. A direct Cold Email to the HR.
        """
        response = model.generate_content(prompt)
        st.write(response.text)
else:
    st.warning("Please enter your Gemini API key in the sidebar to start.")
