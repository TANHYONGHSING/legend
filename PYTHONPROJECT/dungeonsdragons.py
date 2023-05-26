print("""

 ______            _        _______  _______  _______  _        _______      __      ______   _______  _______  _______  _______  _        _______ 
(  __  \ |\     /|( (    /|(  ____ \(  ____ \(  ___  )( (    /|(  ____ \    /__\    (  __  \ (  ____ )(  ___  )(  ____ \(  ___  )( (    /|(  ____ \
| (  \  )| )   ( ||  \  ( || (    \/| (    \/| (   ) ||  \  ( || (    \/   ( \/ )   | (  \  )| (    )|| (   ) || (    \/| (   ) ||  \  ( || (    \/
| |   ) || |   | ||   \ | || |      | (__    | |   | ||   \ | || (_____     \  /    | |   ) || (____)|| (___) || |      | |   | ||   \ | || (_____ 
| |   | || |   | || (\ \) || | ____ |  __)   | |   | || (\ \) |(_____  )    /  \/\  | |   | ||     __)|  ___  || | ____ | |   | || (\ \) |(_____  )
| |   ) || |   | || | \   || | \_  )| (      | |   | || | \   |      ) |   / /\  /  | |   ) || (\ (   | (   ) || | \_  )| |   | || | \   |      ) |
| (__/  )| (___) || )  \  || (___) || (____/\| (___) || )  \  |/\____) |  (  \/  \  | (__/  )| ) \ \__| )   ( || (___) || (___) || )  \  |/\____) |
(______/ (_______)|/    )_)(_______)(_______/(_______)|/    )_)\_______)   \___/\/  (______/ |/   \__/|/     \|(_______)(_______)|/    )_)\_______)
                                                                                                                                                   



""")

print("Welcome to Dungeons & Dragons")

player_name = input("What is your name , adventurer")

health = 100
damage = 20

print(print('\nwelcome, ' + player_name + ' !you have ' + str(health) + ' health and can do damage ' + str(damage)))
print("You came across a dragon ! What will you do ?")
print('1, fight')
print('2,run')


choice = int(input('Enter either 1 or 2: ')) 
if choice == 1: 
    print("You attack the dragon and do " + str(damage) + ' damage') 
    print('the dragon back off, spit some acid and does 10 damage') 
    health -= 10 
    print('Your current health is ' + str(health)) 
elif choice== 2: 
    print('You try to run away from the dragon') 
    print('The dragon manage to throw rocks at you !') 
    health -= (10*2)
    print('Your current health is ' + str(health)) 


else: 
    print('\nInvalid choice, the dragon get to eat you alive!!!') 
print("Thanks for playing!")