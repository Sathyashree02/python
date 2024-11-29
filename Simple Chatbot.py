import random

responses = [
    "Hello! How can I assist you today?",
    "I'm here to help. What do you need?",
    "Hi there! What can I do for you?",
    "Greetings! How can I be of service?"
]

def chatbot():
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Chatbot: Goodbye!")
            break
        else:
            print(f"Chatbot: {random.choice(responses)}")

chatbot()
