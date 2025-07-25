# FP PROJECT 09: Fortune Cookie App

import random

fortunes = [
    "Great things are coming your way soon.",
    "Hard work beats talent when talent doesn't work hard.",
    "You are braver than you believe.",
    "Believe in the process. Trust the journey."
    "Your future self is cheering you on.",
    "Don't stop now, you're closer than you think.",
    "Big energy is coming. Stay ready.",
    "Discipline will take you where motivation can't.",
    "The grind will be worth it.",
    "You are the glitch in the matrix. Make it count."
]

print("Welcome to the Fortune Cookie App! 🥠")
print("-" * 50)

while True:
    input("\nCracking your cookie... (press Enter)")
    fortune = random.choice(fortunes)
    print(f"\n🍪 Your Fortune: {fortune}")

    again = input("\nWould you like anoher fortune? (yes/no): ").lower()
    if again != "yes":
        print("\nThanks for using the app. May your path be blessed! ✨")
        break
