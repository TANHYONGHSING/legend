import time

from game import Player,Enemy,battle

RED = "\033[1;31m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
BLUE = "\033[1;34m"
MAGENTA = "\033[1;35m"
CYAN = "\033[1;36m"
RESET = "\033[0m"

print(GREEN+" ----------------------------------------------")
print("|                                              |")
print("|           "+RESET+BLUE+"WELCOME TO RAKSASA POKET"+RESET+GREEN+"           |")
print("|                                              |")
print("|----------------------------------------------|"+RESET)
print(GREEN+"|"+RESET+YELLOW+">> "+RESET+RED+"Disclaimer : This is an adventure game !"+RESET+YELLOW+" <<"+RESET+GREEN+"|"+RESET)
print(GREEN+" ----------------------------------------------"+RESET)
name = input(GREEN+"\nHi , what is your name ?\n"+RESET)
print(GREEN+"\nHi "+name+"!"+RESET)
battle()