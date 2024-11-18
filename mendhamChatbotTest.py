import re

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
    message = message.translate(str.maketrans('', '', string.punctuation))    # ignores punctuation in user input 

    for pattern, response in responses.items():
        match = re.search(pattern, message, re.IGNORECASE)                    # ignores case in user input 
        if match:
            if pattern == "what time is it":
                import datetime
                now = datetime.datetime.now()
                response = response.format(time=now.strftime("%H:%M"))
            return response
    return "I'm not sure I understand. Can you rephrase that?"                # error message bot sends if doesn't understand prompt


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
