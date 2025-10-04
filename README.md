# 🌐 Multilingual Car Review Sentiment Analysis

This project demonstrates a **cross-language sentiment analysis system** for automobile reviews, integrating **translation, NLP, and machine learning**. It enables sentiment prediction for both **English and Hindi reviews**, making it useful for car manufacturers and potential buyers.

## 📌 Project Overview

* Goal: Analyze customer car reviews written in multiple languages
* Approach:

  * **Translation:** Hindi reviews → English (Deep-Translator)
  * **Rule-based Sentiment Detection:** VADER Sentiment Analyzer
  * **ML Classification:** TF-IDF + Logistic Regression (English reviews)
  * **Interactive App:** Streamlit frontend for real-time prediction

## ⚙️ Tools & Technologies

* **Frontend:** Streamlit
* **Backend:** Python, Pandas, Scikit-learn
* **NLP Libraries:** Deep-Translator, VADER
* **Visualization:** Matplotlib, WordCloud
* **Datasets:**

  * `hindi_car_reviews_no_car_names.csv`
  * `car_sentiment_dataset_500.csv`

## 🧠 Machine Learning Workflow

1. **Translation & Preprocessing**

   * Hindi reviews translated to English
   * Cleaned and tokenized text
2. **Sentiment Analysis**

   * Rule-based (VADER) for translated Hindi reviews
   * TF-IDF + Logistic Regression for English reviews
3. **Model Evaluation**

   * Achieved **86% accuracy**
   * Strong performance on Positive & Negative classes
   * Neutral class limited due to class imbalance
4. **Deployment**

   * Streamlit web application for real-time predictions

## 💻 How to Run the Project

1. Clone repository:

   ```bash
   git clone https://github.com/<your-username>/multilingual-car-sentiment.git
   cd multilingual-car-sentiment
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

4. Open in browser:

   ```
   http://localhost:8501/
   ```

## 🌐 Streamlit Application Features

* Enter a **car review in English or Hindi**
* Automatic translation (if needed)
* Real-time **Positive / Negative / Neutral** prediction
* Display of sentiment distribution

## 📊 Results

* **Accuracy:** 86% (TF-IDF + Logistic Regression)
* **Strength:** Handles multilingual reviews effectively
* **Limitation:** Neutral sentiment classification requires balanced datasets

## 🚀 Future Improvements

* Incorporate **deep learning models (LSTMs, Transformers)** for better context
* Address **neutral class imbalance**
* Extend support for more Indian languages

## 📜 Conclusion

This project establishes a **robust framework for multilingual sentiment analysis** in the automobile domain. It demonstrates cross-language NLP, machine learning, and real-time deployment skills.

---

👨‍💻 **Author:** Sushant Kishan Rathod
📧 Contact: [sushantrathod6288@gmail.com]
🔗 GitHub: [https://github.com/Sushant-project62]
