import streamlit as st
import pickle

# Load model and vectorizer
model = pickle.load(open("sentiment_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# Page config
st.set_page_config(page_title="Car Review Sentiment", layout="centered")

# Background & styling
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
.review-box {
    background: rgba(0,0,0,0.7);
    padding: 30px;
    border-radius: 20px;
    max-width: 750px;
    margin: auto;
    box-shadow: 0px 6px 25px rgba(0,0,0,0.6);
}
textarea {
    background: rgba(255,255,255,0.9) !important;
    border: 2px solid #FF4500 !important;
    border-radius: 12px !important;
    padding: 12px !important;
    font-size: 18px !important;
    color: #000 !important;
}
.stButton>button {
    background: linear-gradient(90deg, #FF4500, #FF6347);
    color: white;
    border-radius: 40px;
    padding: 14px 35px;
    font-size: 20px;
    font-weight: bold;
    border: none;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.4);
    transition: 0.3s;
}
.stButton>button:hover {
    background: linear-gradient(90deg, #FF6347, #FF4500);
    transform: scale(1.08);
    box-shadow: 0px 6px 20px rgba(0,0,0,0.6);
}
.result {
    text-align: center;
    font-size: 28px;
    font-weight: bold;
    margin-top: 20px;
    padding: 15px;
    border-radius: 12px;
}
.positive {
    color: #00FF7F;
    text-shadow: 2px 2px 12px #000;
}
.negative {
    color: #FF3030;
    text-shadow: 2px 2px 12px #000;
}
.neutral {
    color: #FFD700;
    text-shadow: 2px 2px 12px #000;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# Title
st.markdown('<div class="title">🚗 Car Review Sentiment Analyzer</div>', unsafe_allow_html=True)

# Input form
with st.form("review_form"):
    st.markdown('<div class="review-box">', unsafe_allow_html=True)
    user_review = st.text_area("", height=150, placeholder="✍️ Enter your car review here...")
    submitted = st.form_submit_button("🔍 Analyze Sentiment")
    st.markdown('</div>', unsafe_allow_html=True)

# Prediction
if submitted and user_review.strip() != "":
    transformed = vectorizer.transform([user_review])
    prediction = model.predict(transformed)[0]

    if prediction == "Positive":
        st.markdown('<div class="result positive">🎉 This is a <b>Positive Review</b> 🚀</div>', unsafe_allow_html=True)
    elif prediction == "Negative":
        st.markdown('<div class="result negative">⚠️ This is a <b>Negative Review</b> ❌</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="result neutral">😐 This seems <b>Neutral</b> 🟡</div>', unsafe_allow_html=True)
