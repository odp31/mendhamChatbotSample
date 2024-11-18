# install necessary NLTK data:
# run four lines below in separate python script to download necessary data files 
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')


from flask import Flask, render_template, request 
app = Flask(__name__)


import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.chunk import ne_chunk
import random

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
      # use part of speech tags to ID question types
      if "VBZ" in [tag for word, tag in pos_tags]:
        return "i can provide info or answer your question."
      elif "VBD" in [tag for word, tag in pos_tags]:
        return "i can help you undertand past events or actions. what do you want to know?"
      else:
        return "I'm still under developent but I'll do by best to answer your question."
  else:
    return"I apologize, I don't understand. can i help with something else?"
      
@app.route('/')
def index():
  return render_template('index.html')

@app.route('/chat', methods=['POST'])
# create a simple chat loop:
def chat():
  user_message = request.form['user_message']
  response = respond(user_message)
  return response 

if __name__ == '__main__':
  app.run(debug=True)


# run chatbot
chat() 
