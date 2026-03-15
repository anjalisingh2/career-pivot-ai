import streamlit as st
import google.generativeai as genai

# Page Config with Tool Name
st.set_page_config(page_title="Smart Hiring Tool | Anjali Singh", layout="wide")

# Custom UI Styling
st.markdown("""
    <style>
    .main { background-color: #f4f7f6; }
    .stHeader { color: #0078d4; }
    .stButton>button { background-color: #28a745; color: white; border-radius: 8px; font-weight: bold; height: 3em; }
    .report-box { background-color: #ffffff; padding: 20px; border-radius: 10px; border-left: 5px solid #0078d4; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# Header Section
st.title("🛡️ Smart Hiring Tool")
st.markdown("##### *Empowering Candidates with 8+ Years of Recruiting Intelligence by Anjali Singh*")
st.divider()

# Sidebar for Key and Quick Expert Tips
with st.sidebar:
    st.header("⚙️ Control Panel")
    api_key = st.text_input("Enter Gemini API Key", type="password")
    st.divider()
    st.markdown("### 🌟 Anjali's Microsoft Hack:")
    st.info("Microsoft Noida ke recruiters **'Stakeholder Management'** aur **'Data-Driven Hiring'** keywords ko CV mein sabse pehle dekhte hain.")

if api_key:
    try:
        genai.configure(api_key=api_key)
        available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        model = genai.GenerativeModel(available_models[0])
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### 🎯 Job Description")
            jd_text = st.text_area("", height=200, placeholder="Paste JD here...")
        with col2:
            st.markdown("### 📄 Your Resume")
            resume_text = st.text_area("", height=200, placeholder="Paste Resume here...")

        if st.button("🚀 Generate Smart Analysis"):
            if jd_text and resume_text:
                with st.spinner('Smart Hiring Tool is analyzing...'):
                    prompt = f"""
                    You are a Senior Recruitment Expert (Anjali Singh). Analyze the Resume: {resume_text} against JD: {jd_text}.
                    
                    Structure the output clearly:
                    1. **Match Score**: Give a percentage.
                    2. **Missing Keywords**: List 3-5 specific keywords for ATS.
                    3. **Learning Roadmap**: Provide 2-3 YouTube or Coursera search links for missing skills.
                    4. **Professional Cover Letter**: Write a short, impactful 3-paragraph cover letter.
                    5. **HR Connect Strategy**: 
                       - Provide a LinkedIn Boolean Search String to find the hiring team.
                       - Provide a 2-line direct message for the Recruiter.
                    """
                    response = model.generate_content(prompt)
                    
                    st.markdown("---")
                    st.subheader("📋 Your Personalized Action Plan")
                    st.markdown(response.text)
            else:
                st.error("Please fill both JD and Resume boxes.")
    except Exception as e:
        st.error(f"Error: {e}")
else:
    st.warning("👈 Please enter your API Key in the sidebar to start.")
