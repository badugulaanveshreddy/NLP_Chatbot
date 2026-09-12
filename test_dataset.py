import json

# Load the chatbot dataset
with open("data/intents.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# Display basic information
print("Dataset loaded successfully!")
print("Number of intents:", len(data["intents"]))

print("\nAvailable intents:")

for intent in data["intents"]:
    print("-", intent["tag"])