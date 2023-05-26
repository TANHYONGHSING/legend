temperatures = input("Input a list of temperatures in 7 days \n").split()

total_temperature = 0

for temperature in temperatures:
    total_temperature = total_temperature + float(temperature)
print("\nTotal temperature in celsius is "+str(total_temperature)+" ℃")


number_days = 0
for days in temperatures:
    number_days = number_days + 1
print("\nThis is " + str(number_days) + " days temperature in  celsius.")
celsius_average = round(total_temperature / number_days)
kelvin_average = round(celsius_average + 273.15)
fahrenheit_average = round((celsius_average * 9/5)+32)

print("\nThe average temperatures in celsius is "+ str(celsius_average) +" ℃")
print("The average temperatures in kelvin is "+ str(kelvin_average) + " K")
print("The average temperatures in fahrenheit is "+ str(fahrenheit_average) +" ℉")