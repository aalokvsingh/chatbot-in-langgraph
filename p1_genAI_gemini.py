import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

# Load environment variables
load_dotenv()

# Initialize Gemini model (cheaper testing model)
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.3,
)

def main():
    print("Gemini Test Chat (type 'exit' to quit)\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit"]:
            break

        response = llm.invoke([HumanMessage(content=user_input)])

        print("Bot:", response.content)
        print("-" * 50)

if __name__ == "__main__":
    main()
