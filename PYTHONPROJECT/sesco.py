wattage_values = [1000 , 1500 , 500 , 200 ,300 ]
total_watt = 0
for watt in wattage_values:
    total_watt = total_watt + float(watt)
print("Total power consumption is " + str(total_watt) + " kilowatt-hours")

hours = 8
energy_rate = 0.15
month = 30
total_cost = round(total_watt * (hours * energy_rate)) * (month)
print("\nTotal cost for the month is $" + str(total_cost) + " USD")

