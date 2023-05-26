# Author : Tan Hyong Hsing (20DDT21F1002)

import time
from prettytable import PrettyTable

RED = "\033[1;31m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
BLUE = "\033[1;34m"
MAGENTA = "\033[1;35m"
CYAN = "\033[1;36m"
RESET = "\033[0m"

time.sleep(3)

print(BLUE+" ----------------------------------------------")
print("|                                              |")
print("|     "+RESET+MAGENTA+"Flexi Flight Ticketing System (FLEXI)"+RESET+BLUE+"    |")
print("|                                              |")
print("|----------------------------------------------|"+RESET)
print(BLUE+"|"+RESET+YELLOW+"        >> "+RESET+CYAN+"FlipFlopFlexyFlight Bhd"+RESET+YELLOW+" <<"+RESET+BLUE+"         |"+RESET)
print(BLUE+" ----------------------------------------------"+RESET)

time.sleep(3)

x = PrettyTable()
x.field_names = ["ID", "From", "To", "Depart Time", "Adult Price" , "Child Price"]
x.add_row([1, "Lawas", "Limbang", 6.30 , 40.00 , 30.00])
x.add_row([2, "Mukah", "Bakalalan", 7.30 , 28.00 , 13.00])
x.add_row([3, "Bintulu", "Kapit", 8.30, 13.00, 25.00])
x.add_row([4, "Kuching", "Sibu", 9.30 ,35.00, 40.00])
x.add_row([5, "Miri", "Bintulu", 5.30 ,55.00 ,45.00])
print(x)

""" class customer :
    def __init__(self,name):
        self.name = name
    
    def insert():
        customer.Name = input("enter name")

customer.insert() """
name = input("Enter name - ")
From = input("Enter current location - ")
to = input("Enter destination - ")
no_of_adult = float(input("Enter Number of Adult - "))
no_of_children = float(input("Enter Number of Children - "))
#total_payment = input("Enter total payment - ")

if From == "Lawas" :
    adult_price = 40.00
    child_price = 30.00
    total_payment = (adult_price*no_of_adult) + (child_price*no_of_children)

y = PrettyTable()
y.field_names = ["Name", "From", "To", "Number of Adult", "Adult Price" , "Total Payment"]
y.add_row([name,From,to,no_of_adult,no_of_children,total_payment])
print(y)