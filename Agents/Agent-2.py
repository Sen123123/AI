import re, random
from colorama import Fore, init

init(autoreset=True)

destination = {
    "beaches": ["Bali","Portugual","Maldives"],
    "mountains": ["","",""],
    "cities": ["","",""]
}
jokes = [
    "Why was 6 afraid of 7? Because 7 8 9.",
    "You can avoid a red light by driving 114,004,827 MPH, at that speed it would blue shifted enough to appear green.",
    ""
]

def normalize_input(text):
    return re.sub(r"\s+"," ", text.strip().lower())

def recommended():
    print(Fore.CYAN + "TravelBOT: beaches, mountains or cities?")
    preference = input(Fore.YELLOW + "YOU: ")
    preference = normalize_input(preference)

    if preference in destination:
        suggestion = random.choice(destination[preference])
        print(Fore.GREEN + f"TravelBot: How about {suggestion}?")
        print(Fore.CYAN + f"TravelBot: Do you like it or not? (y/n)")
        answer = input(Fore.YELLOW + "You: ").lower()

        if answer == "yes":
            print(Fore.GREEN + f"Your welcome!")
        elif answer == "no":
            print(Fore.RED + f"I am sorry for your distatisfaction.")
            recommended()
    else:
        print(Fore.RED + f"Sorry I don't have that type of destination.")