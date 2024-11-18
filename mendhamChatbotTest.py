import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer


# response dictionary
responses ={
  "hello": "Hello! How can I help you today?",
  "hi": "Hi there! What's on your mind?",
  "when is school": "you have school tomorrow!",
  "how are you": "I'm doing well, thank you. How are you?",
  "what's your name": "You can call me Olivia, your Mendham AI assitant.",
  "bye": "goodbye! have a nice day.",
  "what time is it": "It's currently {time}",
}

# function to process user input
def respond(message):
  # pre process message(remove loweracse, punctuation)
  message = message.lower().translate(str.maketrans('','',string.punctuation))

  # tokenize message 
  tokens = word_tokenize(message)

  # stem message 
  stemmer = PorterStemmer()
  stemmed_tokens = [stemmer.stem(token) for token in tokens]

  for pattern, response in response.items():
    if pattern in stemmed_tokens or pattern in tokens:
      if pattern == "what time is it":
        import datetime
        now = datetime.datetime.now()
        response = response.format(time=now.strftime("%H:%M"))
      return response

    # check for specific instents (e.g., greeting, question request)
    if any(token in ["hi", "hello", "hey"] for token in tokens):
      return "Hello! How can i help you today?"
    elif any(token in ["what", "how", "why"] for token in tokens:
      return "I'm still underdevelopment, but I'll do my best to answer your question."
    else:
      return "i'm not sure i understand. can you repharse that?"
      
    
# create a simple chat loop:
def chat():
  while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
      break
    response = respond(user_input)
    print("Mendham AI Assistant:", response)


# run chatbot
chat() 
