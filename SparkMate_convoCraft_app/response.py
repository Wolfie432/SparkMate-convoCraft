from chatterBotTraining  import chatbot

while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break

        response = chatbot.get_response(user_input)
        print("Bot:", response)
