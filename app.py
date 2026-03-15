import streamlit as st
import google.generativeai as genai

# Page Configuration for a Startup Look
st.set_page_config(page_title="Smart Hiring Tool | AI Career Engine", layout="wide")

# Professional UI Styling (Clean & Modern)
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    .stHeader { color: #1e3a8a; }
    .stButton>button { 
        background: linear-gradient(90deg, #1e3a8a 0%, #3b82f6 100%); 
        color: white; border-radius: 8px; font-weight: bold; border: none; height: 3.5em;
    }
    .report-card { 
        padding: 20px; border: 1px solid #e2e8f0; border-radius: 12px; 
        background-color: #f8fafc; margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# Product Branding
st.title("🛡️ Smart Hiring Tool")
st.markdown("#### The Ultimate AI-Powered Bridge Between Candidates and Careers")
st.write("Analyze. Optimize. Connect. Get hired by the world's top companies.")
st.divider()

# Sidebar for Key & Instructions
with st.sidebar:
    st.header("🔑 Product Access")
    api_key = st.text_input("Enter your API Key", type="password")
    st.divider()
    st.markdown("""
    ### 📖 How it Works:
    1. **Upload Data:** Paste any Job Description and your current Resume.
    2. **AI Analysis:** Our engine scans for ATS compatibility and skill gaps.
    3. **Action Plan:** Get a customized cover letter and LinkedIn strategy.
    """)
    st.info("Perfect for: Software, Marketing, HR, Finance, and Sales roles.")

if api_key:
    try:
        genai.configure(api_key=api_key)
        # Dynamic model selection for stability
        available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        model = genai.GenerativeModel(available_models[0])
        
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("🎯 Job Description")
            jd_text = st.text_area("", height=250, placeholder="Paste the job requirements here...", key="jd")
        with col2:
            st.subheader("📄 Candidate Resume")
            resume_text = st.text_area("", height=250, placeholder="Paste your resume text here...", key="resume")

        if st.button("🚀 Run Smart Analysis"):
            if jd_text and resume_text:
                with st.spinner('Our AI Recruiter is analyzing the match...'):
                    # The Universal Prompt
                    prompt = f"""
                    You are a world-class Executive Recruiter and Career Coach. 
                    Analyze the following Resume against the Job Description (JD).
                    
                    RESUME: {resume_text}
                    JD: {jd_text}
                    
                    Please provide a high-value response in these sections:
                    1. **Executive Summary**: A quick fit-gap analysis.
                    2. **Match Score**: A percentage based on skills, experience, and keywords.
                    3. **ATS Keywords Gap**: List specific missing keywords crucial for ATS (like Workday, Greenhouse, Taleo).
                    4. **Upskilling Roadmap**: 2-3 specific topics to learn with suggested YouTube/Coursera search queries.
                    5. **Tailored Cover Letter**: A professional, persuasive cover letter.
                    6. **Outreach Strategy**:
                       - LinkedIn Boolean Search String to find the hiring team.
                       - A high-conversion 'Cold Message' for the Recruiter.
                    """
                    response = model.generate_content(prompt)
                    
                    st.markdown("<div class='report-card'>", unsafe_allow_html=True)
                    st.subheader("📊 Your Smart Career Report")
                    st.markdown(response.text)
                    st.markdown("</div>", unsafe_allow_html=True)
            else:
                st.error("Please provide both the Job Description and Resume.")
    except Exception as e:
        st.error(f"Configuration Error: {e}")
else:
    st.warning("Please enter an API Key in the sidebar to activate the tool.")
