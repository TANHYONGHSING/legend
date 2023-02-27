#Tan Hyong Hsing
#20DDT21F1002
#POS System in a supermarket.

#Request for how many items the customer bought
print('Only limit for 3 items')
total_items = int(input('How many items the customer bought ? \n'))

i = 0
while i < total_items:
    #price = float(input('price ? \n'))
    i = i + 1
    if total_items == 1:
        price1 = float(input('price ?'))
        grand_total = price1
        amount = float(input('how much user paid ?'))
        balance = amount - grand_total
        print('the grand_total is RM ' + str(grand_total))
        print('the amount user paid is RM ' + str(amount))
        print('the balance for user is RM ' + str(balance))
        break
    elif total_items == 2:
        price1 = float(input('price ?'))
        price2 = float(input('price ?'))
        grand_total = price1 + price2
        amount = float(input('how much ?'))
        balance = amount - grand_total
        print('the grand_total is RM ' + str(grand_total))
        print('the amount user paid is RM ' + str(amount))
        print('the balance for user is RM ' + str(balance))
        break
    elif total_items == 3:
        price1 = float(input('price ?'))
        price2 = float(input('price ?'))
        price3 = float(input('price ?'))
        grand_total = price1 + price2 + price3
        amount = float(input('how much ?'))
        balance = amount - grand_total
        print('the grand_total is RM ' + str(grand_total))
        print('the amount user paid is RM ' + str(amount))
        print('the balance for user is RM ' + str(balance))
        break
    else :
        print('exceeded amount of purchase')
        break


    
   