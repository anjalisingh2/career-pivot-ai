import streamlit as st
import google.generativeai as genai

# App Branding & Title
st.set_page_config(page_title="Smart Hiring Tool", page_icon="🛡️", layout="wide")

# UI Styling for a Mobile-App Feel
st.markdown("""
    <style>
    [data-testid="stSidebar"] { display: none; } /* Hide Sidebar for App feel */
    .main { background-color: #f0f2f5; }
    .stButton>button { 
        background: linear-gradient(90deg, #1e3a8a 0%, #3b82f6 100%); 
        color: white; border-radius: 25px; height: 3.5em; width: 100%; border: none;
    }
    .card { background-color: white; padding: 20px; border-radius: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); margin-bottom: 20px; }
    .score-text { font-size: 32px; font-weight: bold; color: #1e3a8a; text-align: center; }
    .tag { background-color: #fee2e2; color: #b91c1c; padding: 4px 10px; border-radius: 8px; font-size: 12px; font-weight: bold; margin-right: 5px; }
    </style>
    """, unsafe_allow_html=True)

# API KEY FIX: 
# Go to Streamlit Cloud Settings -> Secrets and add: GOOGLE_API_KEY = "YOUR_KEY_HERE"
if "GOOGLE_API_KEY" in st.secrets:
    api_key = st.secrets["GOOGLE_API_KEY"]
else:
    api_key = st.sidebar.text_input("Temporary API Key (Admin only)", type="password")

st.title("🛡️ Smart Hiring Tool")
st.write("Scan your resume. Fix the gaps. Get the job.")

# Layout for Inputs
col1, col2 = st.columns(2)
with col1:
    jd_input = st.text_area("🎯 Job Requirements", placeholder="Paste Job Description...", height=150)
with col2:
    resume_input = st.text_area("📄 Your Resume", placeholder="Paste Resume text...", height=150)

if st.button("RUN SMART ANALYSIS"):
    if jd_input and resume_input and api_key:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        with st.spinner('Smart Engine is Calculating...'):
            # Prompt for VISUAL/SHORT output
            prompt = f"""
            Role: Expert Career Coach. 
            Inputs: Resume: {resume_input}, JD: {jd_input}.
            Output must be SHORT and use Emojis.
            Format:
            1. SCORE: [0-100]% 
            2. MISSING: [Comma separated list of 5 keywords]
            3. FIX: [1 sentence advice]
            4. EMAIL: [2 line cold email]
            5. CONNECT: [LinkedIn Boolean String]
            """
            response = model.generate_content(prompt)
            res_text = response.text

            # Displaying as Visual Cards
            st.markdown("---")
            c1, c2, c3 = st.columns([1,2,1])
            
            with c2:
                st.markdown("<div class='card'>", unsafe_allow_html=True)
                st.markdown(f"<div class='score-text'>Match Score: {res_text.split('SCORE:')[1].split('2.')[0]}</div>", unsafe_allow_html=True)
                st.progress(75) # Dynamic calculation can be added
                st.markdown("</div>", unsafe_allow_html=True)

            # Split logic for visuals
            st.markdown("### 🛠️ Quick Action Plan")
            st.write(res_text) # This will now be short as per prompt
            
    else:
        st.error("Please provide inputs.")
