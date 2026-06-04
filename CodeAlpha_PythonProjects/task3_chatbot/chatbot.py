print("Hello! I am PyBot, your personal assistant.")
print("You can talk to me! Type 'bye' to exit.")

while True:
    user_input = input("You: ")
    user_input = user_input.lower()

    if user_input == "bye":
        print("PyBot: Goodbye! Have a great day!")
        break

    elif user_input == "hello" or user_input == "hi":
        print("PyBot: Hi there! How can I help you?")

    elif user_input == "how are you":
        print("PyBot: I am fine, thank you! How about you?")

    elif user_input == "what is your name":
        print("PyBot: My name is PyBot!")

    elif user_input == "what can you do":
        print("PyBot: I can chat with you and answer simple questions!")

    else:
        print("PyBot: Sorry, I don't understand that. Try asking something else!")