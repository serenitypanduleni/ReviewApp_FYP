# Reference - https://www.analyticsvidhya.com/blog/2021/02/machine-learning-model-deployment-using-django/

import joblib
import re
from nltk.stem import WordNetLemmatizer

# Reference - https://medium.com/@kapilesh1/hi-viewers-8fd8de2cb165
sentiment_model = joblib.load("sentiment/nb_sentiment_model.pkl")
vectoriser = joblib.load("sentiment/vectoriser.pkl")

lemmatizer = WordNetLemmatizer()


# Function to preprocess the review text
def preprocess_text(text):
    text = re.sub(r"[^\w\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    text = text.lower()
    text = text.split()
    text = [lemmatizer.lemmatize(word) for word in text]
    text = " ".join(text)
    return text


# Sentiment prediction function
def predict_sentiment(text):
    review = preprocess_text(text)
    vectorised_text = vectoriser.transform([review])
    predicted_sentiment = sentiment_model.predict(vectorised_text)
    if predicted_sentiment == 1:
        return "positive"
    else:
        return "negative"
    
# Mismatch function 
def check_mismatch(predicted_sentiment, rating):
    if (rating >= 4 and predicted_sentiment == "negative") or (rating <= 2 and predicted_sentiment == "positive"):
        return True
    else:
        return False
