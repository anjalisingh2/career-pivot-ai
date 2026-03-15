import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Career Pivot AI", layout="centered")
st.title("🚀 Career Pivot AI: Get Hired at Top Tech")

# Sidebar for API Key
api_key = st.sidebar.text_input("Enter Gemini API Key", type="password")

if api_key:
    try:
        # API Configure
        genai.configure(api_key=api_key)
        
        # Latest Model selection
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        jd_text = st.text_area("Paste Job Description (JD) here:")
        resume_text = st.text_area("Paste your Resume text here:")

        if st.button("Analyze & Optimize"):
            if jd_text and resume_text:
                with st.spinner('AI is analyzing your profile...'):
                    prompt = f"""
                    Act as a Senior Tech Recruiter at a Top Tier Company. 
                    Compare this Resume: {resume_text} 
                    With this JD: {jd_text}
                    
                    Give the following:
                    1. Match Score (out of 100).
                    2. Top 3 Keywords missing in Resume.
                    3. A professional Cold Email to the Hiring Manager.
                    """
                    # Content generation with latest syntax
                    response = model.generate_content(prompt)
                    st.success("Analysis Complete!")
                    st.markdown(response.text)
            else:
                st.error("Please paste both Resume and JD.")
    except Exception as e:
        st.error(f"Error: {e}")
else:
    st.warning("Please enter your Gemini API key in the sidebar.")
