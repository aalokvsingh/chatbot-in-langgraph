from app.services.chat_service import ChatService

def main():
    chat_service = ChatService()

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break

        response = chat_service.chat(user_input)
        print("Bot:", response)

if __name__ == "__main__":
    main()
