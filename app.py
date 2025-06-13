import streamlit as st
import google.generativeai as genai

# Load API key from secrets
api_key = st.secrets["api_keys"]["google_api_key"]
genai.configure(api_key=api_key)

# Load Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

# UI
st.set_page_config(page_title="🪙 Crypto Sentiment Tracker", page_icon="📈")
st.title("🪙 Crypto Sentiment Tracker")
st.markdown("Enter a prompt or comment about a cryptocurrency to get its **sentiment**.")

user_prompt = st.text_area("💬 Enter crypto-related prompt:", placeholder="e.g., Bitcoin is going to hit 100K soon!")

if st.button("Analyze Sentiment"):
    if user_prompt.strip() == "":
        st.warning("Please enter a valid prompt.")
    else:
        with st.spinner("Analyzing sentiment..."):
            prompt = f"""
You're a crypto sentiment analysis engine. Respond with one of the following: Positive, Negative, or Neutral. 

Analyze the sentiment of the following comment about a cryptocurrency:

\"{user_prompt}\"

Just output the sentiment only.
"""
            response = model.generate_content(prompt)
            sentiment = response.text.strip()

        st.success(f"🧠 Sentiment: **{sentiment}**")
