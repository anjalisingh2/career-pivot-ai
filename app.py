import streamlit as st
import google.generativeai as genai

# Page Config
st.set_page_config(page_title="Career Pivot AI | Anjali Singh", layout="wide")

# Custom CSS (Corrected parameter)
st.markdown("""
    <style>
    .main { background-color: #f0f2f6; }
    .stButton>button { background-color: #0078d4; color: white; height: 3em; border-radius: 5px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🚀 Career Pivot AI: Resume Optimizer")
st.write("Built by Anjali Singh | 8+ Years Recruiting Expertise")

# Sidebar
with st.sidebar:
    st.header("Settings")
    api_key = st.text_input("Enter Gemini API Key", type="password")
    st.divider()
    st.info("💡 **Anjali's Tip:** Microsoft Noida searches for 'Full Life Cycle Recruiting' and 'Stakeholder Management' in resumes.")

if api_key:
    try:
        genai.configure(api_key=api_key)
        # Automatically picking the available model
        available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        model = genai.GenerativeModel(available_models[0])
        
        col1, col2 = st.columns(2)
        with col1:
            jd_text = st.text_area("🎯 Paste Job Description (JD):", height=250)
        with col2:
            resume_text = st.text_area("📄 Paste Your Resume:", height=250)

        if st.button("🚀 Analyze My Profile"):
            if jd_text and resume_text:
                with st.spinner('Analyzing...'):
                    prompt = f"""
                    Context: Senior Recruiter Analysis.
                    Resume: {resume_text} 
                    JD: {jd_text}
                    
                    Provide:
                    1. Match Score (out of 100).
                    2. Top 3 Missing Keywords.
                    3. A professional Cold Email for the HR Manager.
                    4. LinkedIn Boolean Search String to find the hiring team.
                    """
                    response = model.generate_content(prompt)
                    st.divider()
                    st.success("Analysis Complete!")
                    st.markdown(response.text)
            else:
                st.error("Please provide both inputs.")
    except Exception as e:
        st.error(f"Error: {e}")
else:
    st.warning("👈 Please enter your API Key in the sidebar.")
