import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Career Pivot AI", layout="centered")
st.title("🚀 Career Pivot AI")

api_key = st.sidebar.text_input("Enter Gemini API Key", type="password")

if api_key:
    try:
        genai.configure(api_key=api_key)
        
        # Sabse stable version jo har jagah chalta hai
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        jd_text = st.text_area("Paste Job Description (JD) here:")
        resume_text = st.text_area("Paste your Resume text here:")

        if st.button("Analyze Profile"):
            if jd_text and resume_text:
                with st.spinner('Checking for available AI models...'):
                    # Direct interaction bina kisi version prefix ke
                    prompt = f"Resume: {resume_text}\nJD: {jd_text}\nProvide 3 improvement tips."
                    response = model.generate_content(prompt)
                    st.success("Analysis Complete!")
                    st.write(response.text)
            else:
                st.error("Please fill both boxes.")
    except Exception as e:
        st.error(f"System Message: {e}")
        st.info("Tip: Agar 404 aa raha hai, toh please AI Studio mein naya project banakar nayi key nikaalein.")
else:
    st.info("Sidebar mein API Key dalein.")
