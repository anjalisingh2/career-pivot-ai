import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Career Pivot AI", layout="centered")
st.title("🚀 Career Pivot AI")

api_key = st.sidebar.text_input("Enter Gemini API Key", type="password")

if api_key:
    try:
        genai.configure(api_key=api_key)
        # Using the most standard model
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        jd_text = st.text_area("Paste Job Description (JD) here:")
        resume_text = st.text_area("Paste your Resume text here:")

        if st.button("Analyze"):
            if jd_text and resume_text:
                with st.spinner('Thinking...'):
                    # The simplest possible call
                    response = model.generate_content(f"Resume: {resume_text}\nJD: {jd_text}\nAnalyze gaps and write a cold email.")
                    st.success("Done!")
                    st.write(response.text)
            else:
                st.error("Please fill both boxes.")
    except Exception as e:
        st.error(f"Something went wrong: {e}")
else:
    st.info("Sidebar mein API Key dalein.")
