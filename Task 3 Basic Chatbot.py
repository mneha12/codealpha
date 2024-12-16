import random
import nltk
from nltk.chat.util import Chat, reflections

# Define some basic pairs and responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?", ]
    ],
    [
        r"hi|hello|hey",
        ["Hello!", "Hey there!", "Hi! How can I assist you?", ]
    ],
    [
        r"how are you ?",
        ["I'm a bot, but I'm here to help you!", "I'm here and ready to chat! How can I assist?", ]
    ],
    [
        r"what is your name ?",
        ["I'm a chatbot created to assist you.", ]
    ],
    [
        r"help|support",
        ["I'm here to help! Tell me what you need assistance with.", ]
    ],
    [
        r"thank you|thanks",
        ["You're welcome!", "Happy to help!", "Anytime!", ]
    ],
    [
        r"quit",
        ["Goodbye! It was nice talking to you.", "See you soon!", "Take care!"]
    ],
]

# Initialize the chatbot with pairs and reflections
chatbot = Chat(pairs, reflections)

# Start a conversation
def start_chat():
    print("Hi! I'm a basic chatbot. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Bot: Goodbye!")
            break
        else:
            response = chatbot.respond(user_input)
            if response:
                print("Bot:", response)
            else:
                print("Bot: I'm not sure how to respond to that.")

# Run the chatbot
start_chat()
