#Tan Hyong Hsing
#20DDT21F1002

centimeters = float(input("Input the length in centimeters\n"))
if centimeters >= 0 :
    inches = centimeters / 2.54
    two_decimal = round(inches ,2)
    print(two_decimal , "inch")
else :
    print("Sorry , your input is invalid . Please try again . ")
#if centimeters < 0 :
    #  print("Sorry , your input is invalid . Please try again . ")
#else :
    #   inches = centimeters / 2.54
    #   print(inches , "inch")
  
print("Thank you for using our system.")