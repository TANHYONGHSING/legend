#Tan Hyong Hsing (20DDT21F1002)

# conversion of celsius to kelvin / kelvin to celsius
def conversion(a):
    return a + 273.15

def conversion2(b):
    return b - 273.15

choice = input("Select (a) celsius to kelvin or (b) kelvin to celsius ")
if choice == "a":

    celsius = float(input("Enter the temperature in celsius. "))

    result = conversion(celsius)
    print( celsius ,"celsius in kelvin is " , result , "kelvin")

elif choice =="b":
    kelvin = float(input("Enter the temperature in kelvin. "))

    result = conversion2(kelvin)
    print(kelvin,"kelvin in celsius is " , result , "celsius")
