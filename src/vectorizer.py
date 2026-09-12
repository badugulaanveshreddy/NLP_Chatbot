import json
import re

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer


class ChatbotVectorizer:

    def __init__(self, data_path="data/intents.json"):

        self.data_path = data_path

        self.vectorizer = TfidfVectorizer(
            lowercase=True,
            ngram_range=(1, 2),
            sublinear_tf=True
        )

        self.patterns = []
        self.labels = []
        self.responses = {}

        self.is_loaded = False

    # ============================================================
    # TEXT PREPROCESSING
    # ============================================================

    def preprocess_text(self, text):
        """
        Clean and normalize user text.
        """

        text = text.lower()

        # Remove punctuation and special characters
        text = re.sub(r"[^a-zA-Z0-9\s]", " ", text)

        # Remove extra spaces
        text = re.sub(r"\s+", " ", text).strip()

        return text

    # ============================================================
    # LOAD DATASET
    # ============================================================

    def load_data(self):
        """
        Load chatbot patterns and intent labels
        from the JSON dataset.
        """

        with open(
            self.data_path,
            "r",
            encoding="utf-8"
        ) as file:

            data = json.load(file)

        self.patterns = []
        self.labels = []
        self.responses = {}

        for intent in data["intents"]:

            tag = intent["tag"]

            # Store responses
            self.responses[tag] = intent.get(
                "responses",
                []
            )

            # Store training patterns
            for pattern in intent["patterns"]:

                cleaned_pattern = self.preprocess_text(
                    pattern
                )

                self.patterns.append(
                    cleaned_pattern
                )

                self.labels.append(tag)

        self.is_loaded = True

        return self.patterns, self.labels

    # ============================================================
    # CREATE TRAINING DATA
    # ============================================================

    def create_training_data(self):

        if not self.is_loaded:
            self.load_data()

        # Convert text into TF-IDF vectors
        X = self.vectorizer.fit_transform(
            self.patterns
        )

        y = np.array(self.labels)

        return X, y

    # ============================================================
    # CREATE VECTOR FOR NEW USER MESSAGE
    # ============================================================

    def create_vector(self, text):

        cleaned_text = self.preprocess_text(text)

        vector = self.vectorizer.transform(
            [cleaned_text]
        )

        return vector

    # ============================================================
    # GET VOCABULARY
    # ============================================================

    def get_vocabulary(self):

        return self.vectorizer.get_feature_names_out()

    # ============================================================
    # GET FEATURE COUNT
    # ============================================================

    def get_feature_count(self):

        return len(
            self.vectorizer.get_feature_names_out()
        )