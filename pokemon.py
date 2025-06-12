import os
import time
import random

def delay():
    time.sleep(2.5)
def longer_delay():
    time.sleep(3)

def choose_poke():
    global First_pokemon
    print("hello")
    delay()
    print("I'm Proffessor Oak")
    delay()
    print("Proffessor Oak: I'm here today to offer you a variety of Pokemons")
    delay()
    print("Proffessor Oak: They will be very helpful for your upcoming journey")
    delay()
    os.system('cls')
    print("Pick a Pokemon: \
          Chespin 🍃 – Grass type \
          Fennekin 🔥 – Fire type \
          Froakie 💧 – Water type")
    First_pokemon = input("What is your pick?:")
    print("That's a great pick!")
    time.sleep(1)
    print("**🎵insert pokemon music🎵**")
    delay()

choose_poke()
longer_delay()

types = "null"
if First_pokemon == "Chespin":
    types = "Leaf"
elif First_pokemon == "Fennekin":
    types = "Fire"
elif First_pokemon == "Froakie":
    types = "Water"

def attacks(First_Pokemon, Types, Opponent_type):
    global chosen_move
    global Overload
    global Reverse_Overload
    Overload = False
    Reverse_Overload = False
    print(f"What would {First_Pokemon} do?")
    print("| 👊 Kick  | 🦁 Roar  | ⭐ Special move ⭐ | 🤡 Taunt  |")
    chosen_move = input("What is your move: ")
    chosen_move.capitalize()
    if Types == "Leaf" and Opponent_type == "Electric":
        Overload = False
        Reverse_Overload = False
    elif Types == "Fire" and Opponent_type == "Electric":
        Overload = True
        Reverse_Overload = False
    elif Types == "Water"  and Opponent_type == "Electric":
        Overload = False
        Reverse_Overload = True

def first_battle(First_pokemon):
    global pikachu_health
    print(f"Proffessor Oak: Now that you have picked {First_pokemon}")
    delay()
    print("Proffessor Oak: It is important for a trainer to get to know their Pokemon")
    delay()
    print("Proffessor Oak: So now you will have a battle with your first Pokemon NOWWWW")
    time.sleep(3.5)
    os.system('cls')

def end_game():
    print("Professor Oak: Congratulatons, you have won your first Pokemon battle!!!")

first_battle(First_pokemon)
longer_delay()

print("Professor Oak sent out Pikachu!")
Opponent_type = "Electric"

pikachu_health = 20
Pikachu_damage = 3
Player_health = 30
damage = 5
while pikachu_health > 0:
    print(f"pikachu's health: {pikachu_health}") 
    print(f"{First_pokemon}'s health: {Player_health}")
    print(f"{First_pokemon}'s damage: {damage}")
    delay()
    attacks(First_pokemon, types, Opponent_type)
    if chosen_move == "Kick":
        pikachu_health = pikachu_health - damage
        os.system('cls')
        longer_delay()
    elif chosen_move == "Roar":
        damage = damage + 2
        print(f"{First_pokemon}'s damage increased by 2")
        longer_delay()
        os.system('cls')
        longer_delay()
    elif chosen_move == "Special move":
        if Overload == True:
            print("It was super effective!!")
            pikachu_health = pikachu_health - 10
            longer_delay()
            os.system('cls')
        elif Overload == False:
            print("It wasn't super effective...")
            pikachu_health = pikachu_health - 7
            longer_delay()
            os.system('cls')
    elif chosen_move == "Taunt":
        print("Pikachu is looks bored")
        longer_delay()
        os.system('cls')
    if pikachu_health <= 0: 
        end_game()
    elif pikachu_health > 0:
        continue
    Pikachu_move = random.randint(0,4)
    if Pikachu_move == 1:
        print("Pikachu used Scratch!!")
        Player_health = Player_health - Pikachu_damage
        longer_delay()
        os.system('cls')
    elif Pikachu_move == 2:
        Pikachu_damage = Pikachu_damage + 1
        print("Pikachu used Roar!! +1 damage")
        longer_delay()
        os.system('cls')
    elif Pikachu_move == 3:
        if Reverse_Overload == True:
            print("Pikachu used Thunderstorm!!⚡⚡⚡")
            time.sleep(1)
            print("It was super effective!!")
            Player_health = Player_health - 10
            longer_delay()
            os.system('cls')
        elif Reverse_Overload == False: 
            print("Pikachu used Thunderstorm!!⚡⚡⚡")
            Player_health = Player_health - 7
            longer_delay()
            os.system('cls')
    elif Pikachu_move == 4:
        print("Pikachu is dancing")
        pikachu_health = pikachu_health + 2
        longer_delay()
        os.system('cls')
    Overload = False
    Reverse_Overload = False
        
