import random
import time

RED = "\033[1;31m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
BLUE = "\033[1;34m"
MAGENTA = "\033[1;35m"
CYAN = "\033[1;36m"
RESET = "\033[0m"
 
class Player:
    def __init__(self, name, hp, power):
        self.name = name 
        self.hp= hp
        self.power = power

class Enemy: 
    def __init__(self, name, hp, power): 
        self.name = name 
        self.hp= hp
        self.power = power

# Define the game loop 
def battle(): 
    # Create the player and enemy 
    player = Player("Player", 100, 20) 
    enemy = Enemy("Enemy", 50, 10) 
    time.sleep(4)
    print(CYAN+"\nYou are exploring the town..."+RESET) 
    time.sleep(4)
    print(CYAN+"Suddenly..."+RESET)
    time.sleep(3)
    print(CYAN+"A challenger is blocked your way..."+RESET)
    time.sleep(3)
    print(CYAN+"He want to challenge you !!!"+RESET)
    time.sleep(3)
    print(CYAN+"You are only allowed to access the new area..."+RESET)
    time.sleep(2)
    print(CYAN+"If you won this fight !!!"+RESET)

    # Game loop 
    while True: 
        time.sleep(3)
        print(GREEN+f"\n{player.name} has {player.hp} hp left."+RESET) 
        print(RED+f"{enemy.name} has {enemy.hp} hp left."+RESET) 

        # Player turn 
        player_choice = input(MAGENTA+"\nDo you want to attack (A) or access bag (B) or quit (Q)? "+RESET) 
        if player_choice == "A": 
            enemy.hp -= player.power
            print(f"You attack {enemy.name} for {player.power} damage!") 
        elif player_choice == "B": 
            bag_choice = input(MAGENTA+"\nDo you want to heal (H) or power-up (P)? "+RESET)
            if bag_choice == "H":
                print(MAGENTA+"\nHow much you want to heal ?"+RESET)
                heal_choice = int(input("\n+10 HP/-10 Power (1) or +20 HP/-20 Power (2) "))
                if heal_choice == 1:
                    player.hp += 10
                    player.power -= 10
                    print(f"You feed your monster a fruit and get 10 hp!") 
                elif heal_choice == 2:
                    player.hp += 20
                    player.power -= 20
                    print(f"You feed your monster a Panadol and get 20 hp!")
            elif bag_choice == "P":
                print(MAGENTA+"\nHow much you want to power up ?"+RESET)
                heal_choice = int(input("\n+10 Power/-10 HP (1) or +20 Power/-20 HP (2) "))
                if heal_choice == 1:
                    player.power += 10
                    player.hp -= 10
                    print(f"You motivated your monster and get 10 power-up!") 
                elif heal_choice == 2:
                    player.power += 20
                    player.hp -= 20
                    print(f"You give your monster a Pistol and get 20 power-up!")    
        elif player_choice == "Q":
           time.sleep(2)
           print("You walked away...")
           break
        else: 
            print("Invalid input. Try again.") 
            continue

        # Check if enemy is defeated 
        if enemy.hp <= 0: 
            print(f"\n{enemy.name} has been defeated!") 
            break

        # Enemy turn 
        enemy_choice = random.choice(["A", "B"]) 
        if enemy_choice == "A": 
            player.hp -= enemy.power
            print(RED+f"{enemy.name} attacks you for {enemy.power} damage!"+RESET) 
        elif enemy_choice == "B": 
            bag_choice = random.choice(["H", "P"])
            if bag_choice == "H":
                print(RED+"\nHow much you want to heal ?"+RESET)
                heal_choice = random.choice([1, 2])
                if heal_choice == 1:
                    player.hp += 10
                    player.power -= 10
                    print(f"Enemy feed his monster a fruit and get 10 hp!") 
                elif heal_choice == 2:
                    player.hp += 20
                    player.power -= 20
                    print(f"Enemy feed his monster a Panadol and get 20 hp!")
            elif bag_choice == "P":
                print(RED+"\nHow much you want to power up ?"+RESET)
                heal_choice = random.choice([1, 2])
                if heal_choice == 1:
                    player.power += 10
                    player.hp -= 10
                    print(f"Enemy motivated his monster and get 10 power-up!") 
                elif heal_choice == 2:
                    player.power += 20
                    player.hp -= 20
                    print(f"Enemy give his monster a Pistol and get 20 power-up!") 

        # Check if player is defeated 
        if player.hp <= 0: 
            print(f"\n{player.name} has been defeated!") 
            break