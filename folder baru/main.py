from pubg import enemy,player,game

RED = "\033[1;31m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
BLUE = "\033[1;34m"
MAGENTA = "\033[1;35m"
CYAN = "\033[1;36m"
RESET = "\033[0m"

text = "Hello World"
print(BLUE + text + RESET)
print("**************************")
print("**************************")
print(MAGENTA + "Welcome to PUBG" + RESET)
print("**************************")
print("**************************")
print(CYAN + "\nSurvive the battle and become the last player standing!" + RESET)


enemy1 = enemy("Gorgon7860" , "75" , "67" , "90")
enemy1.enemy_stat()
player1 = player("MakhlukBumi321" , "80" , "70" , "95")
player1.player_stat()
move1 = game("attack")
move1.fight()
