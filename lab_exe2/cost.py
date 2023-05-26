#Name : Tan Hyong Hsing
#NO MATRIX : 20DDT21F1002

def travelling_cost(distance_travelled, average_speed):
    maximum_hour = 6
    overnight = 80
    fuel_cost = (8.6/100)*2.1
    if distance_travelled / average_speed < maximum_hour:
        total_cost = distance_travelled * fuel_cost
    else:
        total_cost = (distance_travelled * fuel_cost)+overnight
    return total_cost
