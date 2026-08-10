from colorama import Fore, Style, init

# Initialize Colorama
init(autoreset=True)

# ----------------------------------------
# Rule-Based AI Chatbot
# DecodeLabs Internship - Project 1
# ----------------------------------------

print(Fore.MAGENTA + Style.BRIGHT + "===================================")
print(Fore.MAGENTA + Style.BRIGHT + "🤖 Welcome to DecodeBot!")
print(Fore.MAGENTA + "Type 'exit' or 'bye' to end the chat.")
print(Fore.MAGENTA + "===================================\n")

while True:
    user_input = input(Fore.GREEN + "You: ").lower().strip()

    # Greetings
    if user_input == "hello" or user_input == "hi":
        print(Fore.CYAN + "Bot: Hello! Nice to meet you.")

    elif user_input == "good morning":
        print(Fore.CYAN + "Bot: Good morning! Have a wonderful day.")

    elif user_input == "good afternoon":
        print(Fore.CYAN + "Bot: Good afternoon!")

    elif user_input == "good evening":
        print(Fore.CYAN + "Bot: Good evening!")

    # Basic Questions
    elif user_input == "how are you":
        print(Fore.CYAN + "Bot: I am doing great. Thanks for asking!")

    elif user_input == "who are you":
        print(Fore.CYAN + "Bot: I am DecodeBot, a simple rule-based AI chatbot.")

    elif user_input == "what is ai":
        print(Fore.CYAN + "Bot: AI stands for Artificial Intelligence.")

    elif user_input == "your name":
        print(Fore.CYAN + "Bot: My name is DecodeBot.")

    elif user_input == "help":
        print(Fore.MAGENTA + "\nBot: You can ask me simple questions like:")
        print(Fore.MAGENTA + "     - hello")
        print(Fore.MAGENTA + "     - how are you")
        print(Fore.MAGENTA + "     - who are you")
        print(Fore.MAGENTA + "     - what is ai")
        print(Fore.MAGENTA + "     - your name")
        print(Fore.MAGENTA + "     - thanks")
        print(Fore.MAGENTA + "     - bye")

    # Thank You
    elif user_input == "thanks" or user_input == "thank you":
        print(Fore.CYAN + "Bot: You're welcome!")

    # Exit
    elif user_input == "bye" or user_input == "exit":
        print(Fore.CYAN + "Bot: Goodbye! Have a great day.")
        break

    # Unknown Input
    else:
        print(Fore.CYAN + "Bot: Sorry, I don't understand that. Please try another question.")