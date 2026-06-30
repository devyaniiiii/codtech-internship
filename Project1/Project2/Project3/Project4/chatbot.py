print("=== SIMPLE CHATBOT PROJECT ===")
print("Type 'exit' to stop")

while True:
    msg = input("You: ").lower().strip()

    if msg == "exit":
        print("Bot: Bye!")
        break

    elif msg in ["hi", "hello", "hey"]:
        print("Bot: Hello! How can I help you?")

    elif "how are you" in msg:
        print("Bot: I am fine, thank you!")

    elif "name" in msg:
        print("Bot: I am a Python chatbot")

    elif "help" in msg:
        print("Bot: I can respond to greetings and basic questions")

    else:
        print("Bot: Sorry, I don't understand that")
        
