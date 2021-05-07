'''
Intro to the game
'''
from character_creation import character

def intro():
    print("Welcome to Infamous,the type in game where you get to decide your fate")
    name = str(input("You will now create your character. What would you like your name to be:"))
    type_decision = (input("What would you like your type to be \n 1. Tank\n 2. DPS\n 3. Healer\n"))
    if type_decision == "1":
        type = "Tank"
    elif type_decision == "2":
        type = "DPS"
    elif type_decision == "3":
        type = "Healer"
    playable = character(name, type)
    print(f"Your character's name is {playable.name} and your type is {playable.type}")

intro()