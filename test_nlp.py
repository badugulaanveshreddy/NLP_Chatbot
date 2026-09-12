from src.nlp_utils import preprocess_text


# Test sentences
sentences = [
    "Hello, how are you?",
    "What are your skills?",
    "Tell me about your projects!",
    "Thank you so much."
]


print("NLP PREPROCESSING TEST")
print("=" * 40)

for sentence in sentences:

    processed = preprocess_text(sentence)

    print("\nOriginal:", sentence)
    print("Processed:", processed)