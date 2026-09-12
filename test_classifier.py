from src.intent_classifier import IntentClassifier


# Create classifier
classifier = IntentClassifier()


# Train the model
classifier.train()


# Test messages
test_messages = [
    "Hi there",
    "Which technologies do you know?",
    "What have you built?",
    "Which degree do you have?",
    "Tell me about your internship",
    "Thanks for helping",
    "Talk to you later",
    "What is this chatbot?"


]


print("\n")
print("=" * 50)
print("INTENT CLASSIFICATION TEST")
print("=" * 50)


for message in test_messages:

    intent, confidence = classifier.predict_intent(message)

    print("\nUser:", message)
    print("Predicted Intent:", intent)
    print("Confidence:", round(confidence, 2))