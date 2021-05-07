'''
Intro to the game
'''

from character_creation import character

def intro():
    print("Welcome to Infamous,the type in game where you get to decide your fate")
    name = str(input("You will now create your character. What would you like your name to be:"))
    type_decision = int(input("What would you like your type to be \n 1. Tank\n 2. DPS\n 3. Healer"))
    while type_decision != 1 or type_decision != 2 or type_decision != 3:
        type_decision = int(input("Input not accepted: Please only put in 1, 2, or 3"))
    if type_decision == 1:
        type = "Tank"
    elif type_decision == 2:
        type = "DPS"
    elif type_decision == 3:
        type = "Healer"

    playable = character(name, type)
    print(f'Your character  name is {playable.name} and your type is {playable.type}')

intro()