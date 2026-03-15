import streamlit as st
import google.generativeai as genai

# App Layout
st.set_page_config(page_title="Smart Hiring Tool", page_icon="🛡️", layout="centered")

# Visual Styling (Mobile Friendly)
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    .stTextArea textarea { border-radius: 15px; border: 1px solid #ddd; padding: 15px; }
    .stButton>button { 
        background: #000000; color: white; border-radius: 25px; 
        font-weight: bold; height: 3.5em; width: 100%; border: none;
    }
    .result-card { 
        background-color: #f8f9fa; padding: 20px; border-radius: 20px; 
        border-left: 8px solid #28a745; margin-top: 20px;
    }
    .metric-box { text-align: center; padding: 10px; background: #e9ecef; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ Smart Hiring Tool")
st.write("Get your Resume 'Industry-Ready' in seconds.")

# Sidebar - Key Input (Direct solution for now)
with st.sidebar:
    st.header("App Settings")
    # Agar aapne Secrets setup nahi kiya, toh yahan key daalni hogi
    user_api_key = st.text_input("Enter API Key to Activate", type="password")
    st.info("Note: Once launched on Play Store, this will be hidden.")

# Main Inputs
jd_text = st.text_area("🎯 Job Requirements", placeholder="What are they looking for?", height=150)
resume_text = st.text_area("📄 Your Resume", placeholder="Paste your resume content...", height=150)

if st.button("GENERATE SMART REPORT"):
    # Check if everything is provided
    if not user_api_key:
        st.error("Missing: Please enter your API Key in the sidebar.")
    elif not jd_text or not resume_text:
        st.error("Missing: Please paste both Job Description and Resume.")
    else:
        try:
            genai.configure(api_key=user_api_key)
            model = genai.GenerativeModel('gemini-1.5-flash')
            
            with st.spinner('🚀 AI is calculating your fit...'):
                prompt = f"""
                You are an Expert Career Coach. 
                Analyze Resume: {resume_text} vs JD: {jd_text}.
                Keep it VERY SHORT, BOLD, and VISUAL with Emojis.
                
                Format:
                1. MATCH: [Score]%
                2. GAPS: [3-5 Keywords only]
                3. ACTION: [1 line to improve]
                4. CONNECT: [LinkedIn Boolean Search String]
                5. MESSAGE: [2-line DM for HR]
                """
                response = model.generate_content(prompt)
                
                # Displaying Result in a "Card"
                st.markdown("<div class='result-card'>", unsafe_allow_html=True)
                st.subheader("📋 Smart Report")
                st.markdown(response.text)
                st.markdown("</div>", unsafe_allow_html=True)
                
                st.balloons() # Celebration effect for user!
                
        except Exception as e:
            st.error(f"System Error: {e}")
