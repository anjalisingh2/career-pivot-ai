import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Career Pivot AI", layout="centered")
st.title("🚀 Career Pivot AI: Get Hired at Top Tech")

api_key = st.sidebar.text_input("Enter Gemini API Key", type="password")

if api_key:
    try:
        genai.configure(api_key=api_key)
        # Hum generic model name use karenge jo sabse zyada stable hai
        model = genai.GenerativeModel('gemini-1.5-pro')        
        jd_text = st.text_area("Paste Job Description (JD) here:")
        resume_text = st.text_area("Paste your Resume text here:")

        if st.button("Analyze & Optimize"):
            if jd_text and resume_text:
                prompt = f"Act as a Recruiter. Compare Resume: {resume_text} and JD: {jd_text}. Give 3 gaps and a cold email."
                response = model.generate_content(prompt)
                st.success("Analysis Complete!")
                st.write(response.text)
            else:
                st.error("Please paste both Resume and JD.")
    except Exception as e:
        st.error(f"Something went wrong: {e}")
else:
    st.warning("Please enter your Gemini API key in the sidebar.")
