from src.intent_classifier import IntentClassifier
from src.response_generator import ResponseGenerator


class Chatbot:

    def __init__(self):

        print("Initializing chatbot...")

        # NLP intent classifier
        self.classifier = IntentClassifier()

        # Response generator
        self.response_generator = ResponseGenerator()

        # Train the model
        self.classifier.train()

        # Load responses
        self.response_generator.load_responses()

        print("Chatbot initialized successfully!")

    # ============================================================
    # GENERATE RESPONSE
    # ============================================================

    def get_response(self, user_input):
        """
        Process user input and generate a suitable response.
        """

        # Handle empty input
        if not user_input or not user_input.strip():

            return "Please enter a message."

        # Predict intent
        intent, confidence = self.classifier.predict_intent(
            user_input
        )

        # ========================================================
        # CONFIDENCE HANDLING
        # ========================================================

        # Very low confidence
        if confidence < 0.25:

            return (
                "I'm not sure I understand that. "
                "Try asking me about Python, NLP, "
                "machine learning, my skills, projects, "
                "education, or internship."
            )

        # ========================================================
        # GENERATE RESPONSE
        # ========================================================

        response = self.response_generator.generate_response(
            intent
        )

        return response

    # ============================================================
    # TERMINAL CHAT
    # ============================================================

    def chat(self):
        """
        Start the chatbot in the terminal.
        """

        print("\n" + "=" * 60)
        print("NLP CHATBOT")
        print("=" * 60)

        print(
            "Ask me something about my skills, projects, "
            "education, internship, Python, NLP, or ML."
        )

        print(
            "Type 'quit', 'exit', or 'bye' to end."
        )

        while True:

            user_input = input("\nYou: ")

            # Exit commands
            if user_input.lower().strip() in [
                "quit",
                "exit",
                "bye"
            ]:

                print(
                    "Bot: Goodbye! Have a great day!"
                )

                break

            # Generate response
            response = self.get_response(
                user_input
            )

            print("Bot:", response)