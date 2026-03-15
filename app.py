import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Career Pivot AI", layout="centered")
st.title("🚀 Career Pivot AI")

api_key = st.sidebar.text_input("Enter Gemini API Key", type="password")

if api_key:
    try:
        genai.configure(api_key=api_key)
        
        # Sabse pehle check karte hain aapke account mein kaunsa model available hai
        available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        
        if available_models:
            # Jo bhi pehla working model mile, usse use karein
            selected_model = available_models[0]
            model = genai.GenerativeModel(selected_model)
            
            jd_text = st.text_area("Paste JD here:")
            resume_text = st.text_area("Paste Resume here:")

            if st.button("Analyze Now"):
                if jd_text and resume_text:
                    response = model.generate_content(f"Resume: {resume_text}\nJD: {jd_text}\nAnalysis:")
                    st.success(f"Connected via {selected_model}!")
                    st.write(response.text)
        else:
            st.error("Aapke API key par koi model available nahi hai.")
            
    except Exception as e:
        st.error(f"Error: {e}")
else:
    st.info("Please enter API Key in sidebar")
