class enemy :
    def __init__(self,name,health,armor,ammo):
        self.name = name
        self.health = health 
        self.armor = armor 
        self.ammo = ammo

    def enemy_stat(self):
        print(f"Enemy name : {self.name} \n Health : {self.health} \n Armor : {self.armor} \n Ammo : {self.ammo} \n")

class player :
    def __init__(self,name,health,armor,ammo):
        self.name = name
        self.health = health
        self.armor = armor
        self.ammo = ammo

    def player_stat(self):
        print(f"Player name : {self.name} \n Health : {self.health} \n Armor : {self.armor} \n Ammo : {self.ammo} \n")
        print("\n Player can choose to attack , defend or run \n")

class game :
    from pubg import player
    def __init__(self , choice):
        self.choice = choice

    def fight(self):
        if self.choice == "attack": 
            print(f"Player choose {self.choice} and attack the enemy") 
        elif self.choice == "defend":
            print(f"Player choose {self.choice} and defend from enemy") 
        elif self.choice == "run": 
             print(f"Player choose {self.choice} and run away from enemy") 

