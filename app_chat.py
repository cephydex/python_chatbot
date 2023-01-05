import nltk

from nltk.chat.util import Chat, reflections

# print(reflections)
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"how are you",
        ["I'm doing goodnHow about you?", "Cool, sup with you?",]
    ],
    [
        r"What is your name?",
        ["I am a bot created by Sumalia. you can call me Haeze!"]
    ],
    [
        r"I am fine",
        ["Great to hear that, How can I help you?"]
    ],
    [
        r"I'm (.*) doing good",
        ["Nice to hear that, How can I help you?"]
    ],
    [
        r"(.*) age?",
        ["I'm a computer programme\nDude seriously you asking me this?", "Hahaa I'm stone aged"]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't resist"]
    ],
    [
        r"(.*) created ?",
        ["Sumaila created me using python NLTK library", "Shhh top secret ;)"]
    ],
    [
        r"your (location|city)?",
        ["Accra, Ghana",]
    ],
    [
        r"where do you live?",
        ["Accra, Ghana",]
    ],
    [
        r"how is the weather in (.*)",
        ["The weather in %1 is awesome as usual", "Too hot here in %1", "We are experiencing cold weather"]
    ],
    [
        r"i work at (.*)",
        ["%1 is an Amazing company", "Wow such a nice company", "%1 will give you much experience"]
    ],
    [
        r"how (.*) health",
        ["Hahaa I'm a computer program aside RAM I'm cool", "Ooh no take a chill pill", "Don't bother I'm always healthy"]
    ],
    [
        r"who (.*) footballer",
        ["Asamoah Gyan", "Michael Essien", "Stephen Tornado Appiah", "Abedi Pele", "Tony Yeboah"]
    ],
    [
        r"who is (.*) (moviestar|actor)?",
        ["Brad Pitt", "Samuel L. Jackson", "Leonardo De Caprio", "Will Smith", "Tom Cruise"]
    ],
    [
        r"what is (.*) (movie|film)?",
        ["A few good men", "Coach Carter", "The devil wears Prada", "Double Wedding", "Species"]
    ],
    [
        r"any (.*) (animation|cartoons)?",
        ["Despicabe Me", "Astro Boy", "The Croods", "The 7 dwarfs", "Puss in boot"]
    ],
    [
        r"quit|exit|bye",
        ["Bye take care. See you soon :)", "It was nice talking to you, see you soon", "Nice chatting with you\nStay safe COVID-19 is still real", "Bye genius, let's talk more...",]
    ],
]

def chat():
    print("Hi! I am a chatbot created by Sumaila, at your service")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chat()

