from chat_engine import ChatEngine

bot = ChatEngine()

print("AI Healthcare Assistant")
print("Type 'exit' to quit.\n")

while True:

    user = input("You: ")

    if user.lower() == "exit":
        break

    response = bot.process_message(user)

    print("\nBot:", response)
    print()