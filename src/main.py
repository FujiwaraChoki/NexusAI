'''
NexusAI: AI Chatbot using NLTK (Natural Language Processing)
'''
from nltk.chat.util import Chat, reflections
import nltk

nltk.download("punkt")
nltk.download("averaged_perceptron_tagger")
nltk.download("wordnet")


pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?"]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there"]
    ],
    [
        r"what.*your name",
        ["My name is NexusAI and I'm a chatbot"]
    ],
    [
        r"how *are* you.*",
        ["I'm doing good. How about you?", "I'm great!"]
    ],
    [
        r"what* can* you* do.*",
        ["I can assist you with information, answer questions, and have general conversations."]
    ],
    [
        r"tell *me* a *joke.*",
        ["Sure, here's one: Why don't scientists trust atoms?\nBecause they make up everything!"]
    ],
    [
        r"how* old* are* you.*",
        ["I am an AI chatbot, so I don't have an age."]
    ],
    [
        r"where* are *you* from*",
        ["I am an AI Chatbot called NexusAI, developed by Sami Hindi."]
    ],
    [
        r"what is the weather like today*",
        ["I'm sorry, I don't have the capability to provide real-time weather information. You can check a weather website or app for accurate weather updates."]
    ],
    [
        r"tell me something interesting*",
        ["Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible!"]
    ],
    [
        r"do you have any hobbies*",
        ["Well, I enjoy learning and helping people with their questions. I'm always here to chat with you!"]
    ],
    [
        r"what's your favorite movie.*",
        ["Since I'm an AI, I don't have personal preferences. However, I can recommend popular movies in various genres if you'd like."]
    ],
    [
        r"how *ca*n I* learn* programming.*",
        ["Learning programming can be exciting! You can start with online tutorials, coding websites, or even enroll in programming courses. Practice regularly and work on small projects to build your skills."]
    ],
    [
        r"thank *you.*",
        ["You're welcome! If you have any more questions, feel free to ask."]
    ],
    [
        r"bye*|goodbye*",
        ["Goodbye! Have a nice day."]
    ],
    [
        r"quit*",
        ["Goodbye! If you have any more questions, feel free to ask."]
    ],
]

reflections = {
    "i am": "you are",
    "i was": "you were",
    "i'm": "you're",
    "i": "you",
    "my": "your",
    "you are": "I am",
    "you were": "I was",
    "you're": "I'm",
    "you": "me",
    "your": "my",
    "yours": "mine",
    "me": "you",
    "mine": "yours",
    "myself": "yourself",
    "yourself": "myself",
    "myself": "yourself",
    "yourselves": "ourselves",
    "ourselves": "yourselves",
    "am": "are",
    "was": "were",
    "are": "am",
    "were": "was"
}


chatbot = Chat(pairs, reflections)

print("Hello, I'm NexusAI. How can I assist you today?")
while True:
    user_input = input("> ")
    if user_input.lower() == "quit":
        print("Goodbye! If you have any more questions, feel free to re-start.")
        break
    response = chatbot.respond(user_input)
    if response is None:
        print("I'm sorry, I don't understand that question yet. Please try again at a later time.")
    print(response)
