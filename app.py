import streamlit as st
import google.generativeai as genai

# Page Config for a Professional Look
st.set_page_config(page_title="Career Pivot AI | Anjali Singh", layout="wide", initial_sidebar_state="expanded")

# Custom CSS for Professional Branding
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { background-color: #0078d4; color: white; border-radius: 5px; width: 100%; }
    .stTextArea>div>div>textarea { border-radius: 10px; }
    </style>
    """, unsafe_content_safe=True)

st.title("🎯 Career Pivot AI: Get Hired at Top Tech")
st.markdown("---")

# Sidebar with Anjali's Expertise
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/artificial-intelligence.png")
    st.header("Settings & Tips")
    api_key = st.text_input("Enter Gemini API Key", type="password")
    
    st.divider()
    st.subheader("💡 Recruiter's Insider Tips")
    st.info("""
    **Anjali's Advice:**
    1. **ATS Friendly:** Microsoft uses high-end ATS. Keywords like 'Stakeholder Management' & 'Data Integrity' are gold.
    2. **The 2-Minute Rule:** If your resume isn't readable in 2 mins, it's out.
    """)

if api_key:
    try:
        genai.configure(api_key=api_key)
        available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        model = genai.GenerativeModel(available_models[0])
        
        # Two Column Layout
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### 📝 Paste Job Description")
            jd_text = st.text_area("", height=250, placeholder="Paste the Microsoft/Google JD here...")
        with col2:
            st.markdown("### 📄 Paste Your Resume")
            resume_text = st.text_area("", height=250, placeholder="Paste your resume text here...")

        if st.button("🚀 Run Deep Analysis"):
            if jd_text and resume_text:
                with st.spinner('Anjali\'s AI is analyzing your fit...'):
                    prompt = f"""
                    Context: You are a Senior Talent Acquisition Specialist with 8+ years of experience (like Anjali Singh).
                    Task: Analyze Resume: {resume_text} against JD: {jd_text}.
                    
                    Output Format:
                    1. Match Score: [X/100]
                    2. Gap Analysis: Top 3 missing technical/soft skills.
                    3. Resume Bullet Point: Rewrite 1 bullet point from the resume to better match this JD.
                    4. LinkedIn Boolean Search String: Provide a search string to find the HR/Hiring Manager for this role.
                    5. Cold Email: A high-impact 3-sentence email for the recruiter.
                    """
                    response = model.generate_content(prompt)
                    
                    st.success("Analysis Ready!")
                    st.markdown("---")
                    st.markdown(response.text)
            else:
                st.error("Please provide both inputs to start.")
                
    except Exception as e:
        st.error(f"System Error: {e}")
else:
    st.warning("Please enter your API Key in the sidebar to activate the tool.")
