import colorama
from colorama import Fore, Style
from textblob import TextBlob

colorama.init()

print(f"{Fore.CYAN}Welcome to Sentient Spy{Style.RESET_ALL}")

user_name = input(f"{Fore.MAGENTA}Please enter your name: {Style.RESET_ALL }").strip()
if not user_name:
    user_name = "Unknown User"

conversation_history = []

print(f"\n{Fore.CYAN}Hello, User {user_name}")
print(f"Type a Sentence and I will show you the sentiment.")
# print(f"Type {Fore.YELLOW}'reset'{Fore.CYAN}, {Fore.YELLOW}'history'{Fore.CYAN}, "
#       f"or {Fore.YELLOW}'exit'{Fore.CYAN} to quit.{Style.RESET_ALL}").strip()

while True:
    user_input = input(f"{Fore.GREEN}>> {Style.RESET_ALL}").strip()

#     if not user_input:
#         print(f"{Fore.RED}Invalid command.{Style.RESET_ALL}")
#         continue

    polarity = TextBlob(user_input).sentiment.polarity
    if polarity > 0.25:
        sentiment_type = "Positive"
        color = Fore.GREEN
    elif polarity < -0.25:
        sentiment_type = "Negative"
        color = Fore.RED
    else:
        sentiment_type = "Neutral"
        color = Fore.YELLOW

    conversation_history.append((user_input, polarity, sentiment_type))

    print(f"{color} {sentiment_type} sentiment detected"
          f"(Polarity: {polarity:.2f}) {Style.RESET_ALL}")