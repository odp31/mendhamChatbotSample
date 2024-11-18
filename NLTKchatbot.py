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

  # part of speech tagging
  pos_tags = nltk.pos_tag(tokens)

  # named entity recognition
  named_entities = ne_chunk(pos_tags)

  # check for specifc intents using regular expressions and NLTK
  if re.search(r"\b(hi|hello|hey)\b", message):
    return random.choice(["Hello! How can I help you today?", "Hi there! What's on your mind?"])
  elif re.search(r"\b(what|how|why)\b", message):
    # USE NLTK for advanced NLP
    question_words = [word for word, tag in pos_tags if tag.startswith('W')]     # ID question words
    entities = [entity for entity in named_entities if isinstance(entity, nltk.tree.Tree
                                                                 )] # extract named entities
    if entities:
      # use entities to provide more specific responses
      return "I found these entities in your question: {}. How can I help you futher?".format(entities)
    else:
      return "I'm still under developent but I'll do by best to answer your question."
  else:
    return"I apologize, I don't understand. can i help with something else?"
      
    
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