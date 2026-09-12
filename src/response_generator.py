import json
import random


class ResponseGenerator:

    def __init__(self, data_path="data/intents.json"):
        self.data_path = data_path
        self.intents = {}

    def load_responses(self):
        """Load intents and responses from the JSON dataset."""

        with open(self.data_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        for intent in data["intents"]:
            tag = intent["tag"]

            self.intents[tag] = {
                "responses": intent["responses"]
            }

    def generate_response(self, intent):
        """Generate a response based on the predicted intent."""

        if not self.intents:
            self.load_responses()

        if intent in self.intents:

            responses = self.intents[intent]["responses"]

            return random.choice(responses)

        return "I'm sorry, I don't understand that yet."