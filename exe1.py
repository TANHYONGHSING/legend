grades = []
while True:
    grade = input("Enter student's grade (A/B/C), or 'q' to quit: ")
    if grade.lower() == 'q':
        break
    elif grade.upper() == 'A':
        score = 80
    elif grade.upper() == 'B':
        score = 60
    elif grade.upper() == 'C':
        score = 40
    elif grade.upper() == 'D':
        score = 30
    elif grade.upper() == 'E':
        score = 20
    elif grade.upper() == 'F':
        score = 10
    else:
        print("Invalid grade entered.")
        continue
    grades.append(score)

average = sum(grades) / len(grades)
print(f"The average grade is {average:.2f}")

marks = []
while True :
    mark = int(input("Please enter student marks . or -1 to quit ."))
    if mark <= -1:
        break
    elif mark >= 80:
        grade = 'A'
    elif mark >= 60:
        grade = 'B'
    elif mark >= 40:
        grade = 'C'
    elif mark >= 30:
        grade = 'D'
    elif mark >= 20:
        grade = 'E'
    elif mark >= 10:
        grade = 'F'
    else:
        print("Invalid mark entered.")
        continue
    marks.append(mark)

average = sum(marks) / len(marks)
print(f"The average mark is {average:.2f}")

while True :
    if average >= 80:
        grade = 'A'
        print(grade)
        break
    elif average >= 60:
        grade = 'B'
        print(grade)
        break
    elif average >= 40:
        grade = 'C'
        print(grade)
        break
    elif average >= 30:
        grade = 'D'
        print(grade)
        break
    elif average >= 20:
        grade = 'E'
        print(grade)
        break
    elif average >= 10:
        grade = 'F'
        print(grade)
        break
    else:
        print("Invalid mark entered.")
        break
