print("*******************************") 
print("*Welcome to the Caveman Battle*") 
print("*******************************")

#Ask player 1 for their name 
player1_name = input('Player 1, What is your name ?')

player2_name = input('Player 2, What is your name ?')

#set the initial health, ammo and damages
player1_health= 90
player1_ammo = 55
player1_damage = 30

player2_health= 122
player2_ammo = 52
player2_damage = 22

print("\n" + player1_name + "has " + str(player1_health) + " health" + str(player1_ammo) + " rounds of ammo" + str(player1_damage) + " damage") 
print("\n" + player2_name + "has " + str(player2_health) + " health" + str(player2_ammo) + " rounds of ammo" + str(player2_damage) + " damage") 
 
print('\n Your cave suddenly is attacked by wild animals. What do you do?') 
print('1. Fight') 
print('2. Run') 
print('3. Search for supplies')

player1_choice = int(input(player1_name + " , enter 1,2 or 3:")) 
player2_choice = int(input(player2_name + " , enter 1,2 or 3:")) 
 
if player1_choice == 1: 
    print('\n '+ player1_name + 'decides to fight the intruders and does ' + str(player1_damage)+ " damage per shot! ") 
    player1_ammo -= 10 
    if player1_ammo > 0: 
        print('\n ' + player1_name + 'defeated the animals!!They have' + str(player1_ammo) + "rounds of ammo left") 
elif player1_choice == 2: 
    print('\n the animals bitten player 2')
    player2_health -= 30 
    print('\n player 2 health is ' + str(player2_health)) 
    print('\n the animal did some damage to player 1')
    player1_health -=20
    print('\n' + player1_name + 'current health is ' + str(player1_health))
elif player1_choice == 3: 
    print('\n the animals manage to chase them out') 
else: 
    print('\n Invalid input, sad day for the caveman')

if player2_choice == 1: 
    print('\n '+ player2_name + 'decides to fight the intruders and does ' + str(player2_damage)+ " damage per shot! ") 
    player2_ammo -= 10 
    if player2_ammo > 0: 
        print('\n ' + player2_name + 'defeated the animals!!They have' + str(player2_ammo) + "rounds of ammo left") 
elif player2_choice == 2: 
    print('\n the animals bitten player 1')
    player1_health -= 30 
    print('\n player 1 current health is ' + str(player1_health)) 
    print('\n the animal did some damage to player 2')
    player2_health -=20
    print('\n' + player2_name + 'current health is ' + str(player2_health))
elif player2_choice == 3: 
    print('\n the animals manage to chase them out') 
else: 
    print('\n Invalid input, sad day for the caveman')
