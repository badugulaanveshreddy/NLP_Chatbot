import numpy as np
from sklearn.linear_model import LogisticRegression
from src.vectorizer import ChatbotVectorizer


class IntentClassifier:

    def __init__(self):
        self.vectorizer = ChatbotVectorizer()

        self.model = LogisticRegression(
            max_iter=1000
        )

        self.is_trained = False

    def train(self):
        """Train the intent classification model."""

        self.vectorizer.load_data()

        X, y = self.vectorizer.create_training_data()

        self.model.fit(X, y)

        self.is_trained = True

        print("Intent classification model trained successfully!")
        print("Training samples:", X.shape[0])
        print("Features:", X.shape[1])
        print("Number of intents:", len(np.unique(y)))

    def predict_intent(self, text):
        """Predict the intent of a user message."""

        if not self.is_trained:
            self.train()

        vector = self.vectorizer.create_vector(text)

        vector = vector.reshape(1, -1)

        prediction = self.model.predict(vector)

        probabilities = self.model.predict_proba(vector)

        confidence = np.max(probabilities)

        return prediction[0], confidence