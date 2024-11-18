# install necessary NLTK data:
# run four lines below in separate python script to download necessary data files 


from flask import Flask, render_template, request 
app = Flask(__name__)

import string

import re
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
  message = message.translate(str.maketrans('', '', string.punctuation))

  for pattern, response in responses.items():
    match = re.search(pattern, message, re.IGNORECASE)
    if match:
      if pattern == "what time is it":
        import datetime
        now = datetime.datetime.now()
        response= response.format(time=now.strftime("%H:%M"))
      return response
  return "I'm not sure I understand. Can you rephrase that?"
  

      
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
