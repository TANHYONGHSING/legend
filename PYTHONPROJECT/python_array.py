weapon_damage = [10 , 15 , 20 ,25 ,30 ]
total_damage = 0
for damage in weapon_damage:
    total_damage = total_damage + float(damage)
print(total_damage)

damage_average = round(total_damage/len(weapon_damage))
print(damage_average)

