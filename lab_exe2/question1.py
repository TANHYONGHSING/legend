#Name : Tan Hyong Hsing
#NO MATRIX : 20DDT21F1002

def bin_go(num):
    if num % 3 == 0 and num % 5 == 0:
        return "BinGo!"
    elif num % 3 == 0:
        return "Bin!"
    elif num % 5 == 0:
        return "Go!"
    else:
        return "Error."

num = int(input("Please enter a number: "))

result = bin_go(num)
print(result)

