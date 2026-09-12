from src.response_generator import ResponseGenerator


# Create response generator
generator = ResponseGenerator()

# Load responses
generator.load_responses()


print("=" * 50)
print("RESPONSE GENERATION TEST")
print("=" * 50)


test_intents = [
    "greeting",
    "skills",
    "projects",
    "thanks",
    "goodbye"
]


for intent in test_intents:

    response = generator.generate_response(intent)

    print("\nIntent:", intent)
    print("Response:", response)