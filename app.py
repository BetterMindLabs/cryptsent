import streamlit as st
import google.generativeai as genai

# Load Gemini API key from secrets
api_key = st.secrets["api_keys"]["google_api_key"]
genai.configure(api_key=api_key)

# Load Gemini 1.5 Flash model
model = genai.GenerativeModel("gemini-1.5-flash")

# UI
st.set_page_config(page_title="🪙 Crypto Sentiment Tracker", page_icon="📈")
st.title("🪙 Crypto Sentiment Tracker")
st.markdown("Enter a crypto-related statement or comment to get its **sentiment** and a short **conclusion**.")

user_prompt = st.text_area("💬 Enter crypto prompt:", placeholder="e.g., Ethereum gas fees are finally dropping.")

if st.button("Analyze Sentiment"):
    if user_prompt.strip() == "":
        st.warning("Please enter a valid prompt.")
    else:
        with st.spinner("Analyzing with Gemini..."):
            prompt = f"""
You're an AI crypto sentiment analyzer.

Given the following input:
\"{user_prompt}\"

1. First, classify the overall **sentiment** as one of:
- Positive
- Negative
- Neutral

2. Then, give a **1-2 sentence conclusion** explaining why that sentiment fits.

Respond strictly in this format:
Sentiment: <Positive/Negative/Neutral>
Conclusion: <Short conclusive reasoning>
"""
            response = model.generate_content(prompt)
            output = response.text.strip()

        st.success("✅ Analysis Complete")
        st.markdown(f"```\n{output}\n```")
