import streamlit as st
import google.generativeai as genai

# Load Gemini API key
api_key = st.secrets["api_keys"]["google_api_key"]
genai.configure(api_key=api_key)

# Load model
model = genai.GenerativeModel("gemini-1.5-flash")

# UI
st.set_page_config(page_title="📊 Market Sentiment: Crypto", page_icon="📈")
st.title("📊 Market Sentiment Analyzer for Cryptocurrencies")
st.markdown("Type in a cryptocurrency name (e.g., Bitcoin, Ethereum, Solana) to get its **current market sentiment** and **a conclusive explanation.**")

coin_name = st.text_input("🔍 Enter coin name:", placeholder="e.g., Bitcoin")

if st.button("Get Market Sentiment"):
    if coin_name.strip() == "":
        st.warning("Please enter a coin name.")
    else:
        with st.spinner("Querying market sentiment via Gemini..."):
            prompt = f"""
You are a market analyst assistant with access to up-to-date crypto trends, news, and price movements.

Your task is to analyze and summarize the **current market sentiment** of the cryptocurrency: "{coin_name}".

Respond in the following format:
Sentiment: <Positive / Negative / Neutral>
Conclusion: <1-2 sentence explanation based on news, trends, or price action.>

Avoid generic phrases. Be as accurate and concise as possible.
"""
            response = model.generate_content(prompt)
            output = response.text.strip()

        st.success("✅ Market Sentiment Retrieved")
        st.markdown(f"```\n{output}\n```")
