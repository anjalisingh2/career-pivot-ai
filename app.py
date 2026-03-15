import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Career Pivot AI", layout="centered")
st.title("🚀 Career Pivot AI: Get Hired at Top Tech")

api_key = st.sidebar.text_input("Enter Gemini API Key", type="password")

if api_key:
    try:
        genai.configure(api_key=api_key)
        
        # Ye model name sabse zyada stable hai aur har jagah chalta hai
        model = genai.GenerativeModel('gemini-pro')
        
        jd_text = st.text_area("Paste Job Description (JD) here:")
        resume_text = st.text_area("Paste your Resume text here:")

        if st.button("Analyze & Optimize"):
            if jd_text and resume_text:
                with st.spinner('AI is analyzing...'):
                    # Simple prompt to test if it works
                    response = model.generate_content(f"Compare Resume: {resume_text} and JD: {jd_text}. Give 3 gaps.")
                    st.success("Analysis Complete!")
                    st.write(response.text)
            else:
                st.error("Please paste both Resume and JD.")
    except Exception as e:
        st.error(f"Error Details: {e}")
else:
    st.warning("Please enter your Gemini API key in the sidebar.")
