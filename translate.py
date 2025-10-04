# Save this as translate.py
import streamlit as st
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from deep_translator import GoogleTranslator

# Sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Page config
st.set_page_config(page_title="Multilingual Car Review Sentiment Analysis", layout="centered")

# Background & custom CSS
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background: url("https://images.pexels.com/photos/10195710/pexels-photo-10195710.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2") no-repeat center bottom;
    background-size: cover;
}
[data-testid="stHeader"] {
    background: rgba(0,0,0,0);
}
.title {
    text-align: center;
    font-size: 50px;
    font-weight: bold;
    color: #FFD700;
    text-shadow: 2px 2px 10px #000;
    margin-bottom: 30px;
}
.review-box textarea {
    background: rgba(255,255,255,0.9) !important;
    border-radius: 12px !important;
    padding: 15px !important;
    font-size: 18px !important;
    color: #000 !important;
}
.review-box textarea::placeholder {
    font-size: 22px !important;  /* Bigger placeholder font */
    font-weight: bold !important;
    color: #444 !important;
}
.stButton>button {
    background: linear-gradient(90deg, #ff416c, #ff4b2b);
    color: white;
    border: none;
    border-radius: 30px;
    padding: 12px 30px;
    font-size: 18px;
    font-weight: bold;
    transition: 0.3s;
}
.stButton>button:hover {
    background: linear-gradient(90deg, #ff4b2b, #ff416c);
    transform: scale(1.05);
}
.result-box {
    font-size: 26px;
    font-weight: bold;
    text-align: center;
    color: #fff;
    background: rgba(0,0,0,0.7);
    padding: 15px;
    border-radius: 15px;
    margin-top: 25px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.5);
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# Title (changed to Multilingual)
st.markdown('<div class="title">🚗 Multilingual Car Review Sentiment Analyzer</div>', unsafe_allow_html=True)

# Input form with placeholder (changed text)
st.markdown('<div class="review-box">', unsafe_allow_html=True)
review_text = st.text_area("",
    "",
    placeholder="✍️ Write a car review in any language...",
    height=150,
    key="review"
)
st.markdown('</div>', unsafe_allow_html=True)

# Button action
if st.button("🔍 Analyze Sentiment"):
    if review_text.strip():
        try:
            # Translate review → English
            review_english = GoogleTranslator(source='auto', target='en').translate(review_text)

            # Sentiment score
            score = analyzer.polarity_scores(review_english)["compound"]

            if score > 0.05:
                label = "😊 Positive"
                color = "green"
            elif score < -0.05:
                label = "😡 Negative"
                color = "red"
            else:
                label = "😐 Neutral"
                color = "yellow"

            # Show results
            st.markdown(f"<div class='result-box'>📖 Translated Review: <br><i>{review_english}</i></div>", unsafe_allow_html=True)
            st.markdown(f"<div class='result-box'>Sentiment: <span style='color:{color}'>{label}</span></div>", unsafe_allow_html=True)
            st.markdown(f"<div class='result-box'>Sentiment Score: {score}</div>", unsafe_allow_html=True)

        except Exception as e:
            st.error(f"❌ Error: {e}")
    else:
        st.warning("⚠️ Please enter a review.")

