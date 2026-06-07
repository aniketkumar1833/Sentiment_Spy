import colorama
from colorama import Fore, Style
from textblob import TextBlob

# Initialize colorama
colorama.init()

print(f"{Fore.CYAN}📡 Welcome to Emotion Radar! 📡{Style.RESET_ALL}")

agent = input(f"{Fore.MAGENTA}Enter your codename: {Style.RESET_ALL}").strip()

if not agent:
    agent = "Anonymous User"

records = []

print(f"\n{Fore.CYAN}Greetings, {agent}!")
print("Send any message and Emotion Radar will scan its emotional tone.")
print(f"Commands: {Fore.YELLOW}log{Fore.CYAN}, {Fore.YELLOW}clear{Fore.CYAN}, {Fore.YELLOW}quit{Style.RESET_ALL}\n")

while True:
    message = input(f"{Fore.GREEN}Radar Input ➜ {Style.RESET_ALL}").strip()

    if not message:
        print(f"{Fore.RED}No signal detected. Please enter a message.{Style.RESET_ALL}")
        continue

    command = message.lower()

    if command == "quit":
        print(f"\n{Fore.BLUE}📡 Emotion Radar shutting down. Goodbye, {agent}!{Style.RESET_ALL}")
        break

    elif command == "clear":
        records.clear()
        print(f"{Fore.CYAN}🗑 Radar memory cleared successfully!{Style.RESET_ALL}")
        continue

    elif command == "log":
        if not records:
            print(f"{Fore.YELLOW}No scans available yet.{Style.RESET_ALL}")
        else:
            print(f"\n{Fore.CYAN}📋 Scan Log:{Style.RESET_ALL}")
            for i, (text, score, mood) in enumerate(records, start=1):
                print(f"{i}. {text}")
                print(f"   Score: {score:.2f} | Result: {mood}")
        continue

    analysis = TextBlob(message)
    score = analysis.sentiment.polarity

    if score > 0.25:
        mood = "Positive 😊"
        color = Fore.GREEN
    elif score < -0.25:
        mood = "Negative 😟"
        color = Fore.RED
    else:
        mood = "Neutral 😐"
        color = Fore.YELLOW

    records.append((message, score, mood))

    print(
        f"{color}Scan Complete!\n"
        f"Emotion: {mood}\n"
        f"Polarity Score: {score:.2f}{Style.RESET_ALL}"
    )