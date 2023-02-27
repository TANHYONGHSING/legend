#Tan Hyong Hsing
#20DDT21F1002
#POS System in a supermarket.

name = input('Welcome ! What is your name ?\n')
print('Hi ' + name + ' , each customer only allowed to purchase 5 items !')
total_items = int(input('How many items the customer purchase ? \n'))

i = 0
while i < total_items:

    i = i + 1
    if total_items == 1:
        price1 = float(input('How much does the item 1 cost ? \n'))
        grand_total = price1 
        amount = float(input('The amount of money given by the customer .\n'))
        balance = amount - grand_total
        print("                   Tan's Supermarket                         ")
        print('                         MUKAH                               ')
        print('                        RECEIPT                              ')
        print('-------------------------------------------------------------')
        print('Cashier : ' + name +'\n')
        print(' Description                                           Price      ')
        print('-------------------------------------------------------------')
        print('1  Item 1                                               '+str(price1))
        print('-------------------------------------------------------------')
        print('                                        GRAND TOTAL :RM '+str(grand_total))
        print('-------------------------------------------------------------')
        print('                                      Cash Received :RM '+str(amount))
        print('                                            Balance :RM '+str(balance)+'\n')
        print('                    ***Thank You***                          ')
        print('                   Please Come Again                         ')
        break
    elif total_items == 2:
        price1 = float(input('How much does the item 1 cost ? \n'))
        price2 = float(input('How much does the item 2 cost ? \n'))
        grand_total = price1 + price2
        amount = float(input('The amount of money given by the customer .\n'))
        balance = amount - grand_total
        print("                   Tan's Supermarket                         ")
        print('                         MUKAH                               ')
        print('                        RECEIPT                              ')
        print('-------------------------------------------------------------')
        print('Cashier : ' + name +'\n')
        print(' Description                                           Price      ')
        print('-------------------------------------------------------------')
        print('1  Item 1                                               '+str(price1))
        print('2  Item 2                                               '+str(price2))
        print('-------------------------------------------------------------')
        print('                                        GRAND TOTAL :RM '+str(grand_total))
        print('-------------------------------------------------------------')
        print('                                      Cash Received :RM '+str(amount))
        print('                                            Balance :RM '+str(balance)+'\n')
        print('                    ***Thank You***                          ')
        print('                   Please Come Again                         ')
        break
    elif total_items == 3:
        price1 = float(input('How much does the item 1 cost ? \n'))
        price2 = float(input('How much does the item 2 cost ? \n'))
        price3 = float(input('How much does the item 3 cost ? \n'))
        grand_total = price1 + price2 + price3
        amount = float(input('The amount of money given by the customer .\n'))
        balance = amount - grand_total
        print("                   Tan's Supermarket                         ")
        print('                         MUKAH                               ')
        print('                        RECEIPT                              ')
        print('-------------------------------------------------------------')
        print('Cashier : ' + name +'\n')
        print(' Description                                           Price      ')
        print('-------------------------------------------------------------')
        print('1  Item 1                                               '+str(price1))
        print('2  Item 2                                               '+str(price2))
        print('3  Item 3                                               '+str(price3))
        print('-------------------------------------------------------------')
        print('                                        GRAND TOTAL :RM '+str(grand_total))
        print('-------------------------------------------------------------')
        print('                                      Cash Received :RM '+str(amount))
        print('                                            Balance :RM '+str(balance)+'\n')
        print('                    ***Thank You***                          ')
        print('                   Please Come Again                         ')
        break
    elif total_items == 4:
        price1 = float(input('How much does the item 1 cost ? \n'))
        price2 = float(input('How much does the item 2 cost ? \n'))
        price3 = float(input('How much does the item 3 cost ? \n'))
        price4 = float(input('How much does the item 4 cost ? \n'))
        grand_total = price1 + price2 + price3 + price4
        amount = float(input('The amount of money given by the customer . \n'))
        balance = amount - grand_total
        print("                   Tan's Supermarket                         ")
        print('                         MUKAH                               ')
        print('                        RECEIPT                              ')
        print('-------------------------------------------------------------')
        print('Cashier : ' + name +'\n')
        print(' Description                                           Price      ')
        print('-------------------------------------------------------------')
        print('1  Item 1                                               '+str(price1))
        print('2  Item 2                                               '+str(price2))
        print('3  Item 3                                               '+str(price3))
        print('4  Item 4                                               '+str(price4))
        print('-------------------------------------------------------------')
        print('                                        GRAND TOTAL :RM '+str(grand_total))
        print('-------------------------------------------------------------')
        print('                                      Cash Received :RM '+str(amount))
        print('                                            Balance :RM '+str(balance)+'\n')
        print('                    ***Thank You***                          ')
        print('                   Please Come Again                         ')
        break
    elif total_items == 5:
        price1 = float(input('How much does the item 1 cost ? \n'))
        price2 = float(input('How much does the item 2 cost ? \n'))
        price3 = float(input('How much does the item 3 cost ? \n'))
        price4 = float(input('How much does the item 4 cost ? \n'))
        price5 = float(input('How much does the item 5 cost ? \n'))
        grand_total = price1 + price2 + price3 + price4 + price5
        amount = float(input('The amount of money given by the customer . \n'))
        balance = amount - grand_total
        print("                   Tan's Supermarket                         ")
        print('                         MUKAH                               ')
        print('                        RECEIPT                              ')
        print('-------------------------------------------------------------')
        print('Cashier : ' + name +'\n')
        print(' Description                                           Price      ')
        print('-------------------------------------------------------------')
        print('1  Item 1                                               '+str(price1))
        print('2  Item 2                                               '+str(price2))
        print('3  Item 3                                               '+str(price3))
        print('4  Item 4                                               '+str(price4))
        print('5  Item 5                                               '+str(price5))
        print('-------------------------------------------------------------')
        print('                                        GRAND TOTAL :RM '+str(grand_total))
        print('-------------------------------------------------------------')
        print('                                      Cash Received :RM '+str(amount))
        print('                                            Balance :RM '+str(balance)+'\n')
        print('                    ***Thank You***                          ')
        print('                   Please Come Again                         ')
        break
    else :
        print('You exceeded the limit amount of purchase item .')
        break


    
   