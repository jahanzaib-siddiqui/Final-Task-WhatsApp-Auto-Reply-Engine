import pandas as pd
import re

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class AutoReplyEngine:

    def __init__(self, dataset_path):

        self.df = pd.read_csv(dataset_path)

        # Combine category and keywords to improve matching
        self.df["search_text"] = (
            self.df["category"].fillna("") + " " +
            self.df["keywords"].fillna("")
        )

        # Create TF-IDF vectorizer
        self.vectorizer = TfidfVectorizer(
            lowercase=True,
            stop_words="english"
        )

        # Convert FAQ text into numerical vectors
        self.faq_vectors = self.vectorizer.fit_transform(
            self.df["search_text"]
        )


    def preprocess(self, message):

        message = message.lower()

        # Remove punctuation
        message = re.sub(r"[^\w\s]", "", message)

        return message


    def get_response(self, message):

        cleaned_message = self.preprocess(message)

        # Convert user message into TF-IDF vector
        message_vector = self.vectorizer.transform(
            [cleaned_message]
        )

        # Calculate similarity with every FAQ
        similarities = cosine_similarity(
            message_vector,
            self.faq_vectors
        )

        best_index = similarities.argmax()

        best_score = similarities[0][best_index]

        # Confidence threshold
        threshold = 0.15

        if best_score >= threshold:

            return {
                "matched_category":
                    self.df.iloc[best_index]["category"],

                "response":
                    self.df.iloc[best_index]["response"],

                "confidence":
                    round(float(best_score), 2)
            }

        return {
            "matched_category": "Unknown",

            "response":
                "Sorry, I couldn't find an answer to your question. "
                "Please contact our support team for further assistance.",

            "confidence": round(float(best_score), 2)
        }