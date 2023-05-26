fruits = ["apple","banana","cherry"]

for fruit in fruits:
    print(fruit)
    print(fruit + " pie")

print(fruits)

#for best practice the name of array in plural
#and the varible for "for loop" is singular like below

students = ["Haziq","Nelstrooy" , "Nico"]

for student in students:
    print (student)
    print (student + " DDT4B")

print(students)

student_heights = input("Input a list of student's heights ").split()
total_height = 0
for height in student_heights:
    total_height = total_height + float(height)
print(total_height)

number_students = 0
for students in student_heights:
    number_students = number_students + 1
print(number_students)
students_average = round(total_height/number_students)
print(students_average)