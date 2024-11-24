
import nltk

# Ensure the necessary nltk data files are downloaded
nltk.download('punkt')

responses = {
    "hello": "Hi there! How can I help you today?",
    "bye": "Goodbye! Have a great day!",
    "how are you": "I'm a chatbot, so I don't have feelings, but thanks for asking!"
}

def chatbot_response(user_input):
    for trigger in responses:
        if trigger in user_input.lower():
            return responses[trigger]
    return "I'm not sure how to respond to that."

def start_chat():
    print("Chatbot: Hello! Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Chatbot:", chatbot_response(user_input))
            break
        
        print("Chatbot:", chatbot_response(user_input))

start_chat()