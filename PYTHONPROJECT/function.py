#Author : Tan Hyong Hsing (20DDT21F1002)

#this is user-defined function / 'helloMe' function
def helloMe():
    print('hello me')
#this is how you call the function / 'helloMe' function
helloMe()

#this is another user-defined function / 'bmi' function
def bmi():

    name = input('What  is your name ?')
    age = input ('What is your age ?')
    weight = int(input ('What is your weight in kilogram ?'))
    height = float(input ('What is your height in meter ?'))

    bmi = weight / (height * height)
    bmi1 = round(bmi,2)
    print('Hi ' + name + ' your age is ' + str(age) + ' your weight is ' + str(weight) + ' kg ' + ' your height is ' + str(height) + ' m.' )
    print('Your bmi is ' + str(bmi1))
    if bmi < 18.5 :
        print('Your condition is underweight.')
    elif bmi > 18.5 + bmi < 25 :
        print('Your condition is healthy weight.')
    elif bmi > 25 + bmi < 30 :
        print ('Your condition is overweight .')
    else :
        print ('Your condition is obesity.')
#this is calling function
#bmi()

def helloYou(a,b):
    print(f' {a} + {b} + {a+b}')
#helloYou("hyong" , "hsing")

def kira(a,b,c,d):
    print(f'this is simple {a+b+c+d}')
#kira(5,6,7,8)

def suhu(a,b):
    #celsius = {b}
    fahrenheit = (b * 1.8) + 32
    print(f"Hello {a}"+ " nilai dalam fahrenheit ialah " + str(fahrenheit))

    if fahrenheit > 150:
        print("cuaca amat panas")
    else:
        print("cuaca yang baik")
suhu("Tan" , 100)
 