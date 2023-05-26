#Name : Tan Hyong Hsing
#NO MATRIX : 20DDT21F1002
from cost import travelling_cost

distance_travelled = float(input("Please enter distance travelled(KM): "))
average_speed = float(input("Please enter your average speed(KM/H): "))

total_cost = travelling_cost(distance_travelled, average_speed)

print("The amount of RM "+ str((round(total_cost,2))) +" will be credited into your account for next payroll.")
