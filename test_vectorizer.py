from src.vectorizer import ChatbotVectorizer


# Create vectorizer
vectorizer = ChatbotVectorizer()

# Load chatbot dataset
vectorizer.load_data()

# Create training data
X, y = vectorizer.create_training_data()


print("NUMPY FEATURE EXTRACTION TEST")
print("=" * 50)

print("\nNumber of training patterns:", len(vectorizer.patterns))

print("Vocabulary size:", len(vectorizer.vocabulary))

print("Feature matrix shape:", X.shape)

print("Labels shape:", y.shape)


print("\nFirst 20 vocabulary words:")
print(vectorizer.vocabulary[:20])


print("\nExample pattern:")
print(vectorizer.patterns[0])

print("\nExample vector:")
print(X[0])


print("\nExample label:")
print(y[0])


# Test a new user sentence
user_text = "What are your skills?"

user_vector = vectorizer.create_vector(user_text)

print("\nUser input:")
print(user_text)

print("\nUser input vector:")
print(user_vector)