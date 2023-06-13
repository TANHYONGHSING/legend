# Nelstrooy Galat Anak Parti 20DDT21F1045
# Nico Anak Empin 20DDT21F1006
# Tan Hyong Hsing 20DDT21F1002

def menu():
    
    print("\n*******************************************")
    print("*        LITTLE GENIUS SCHOOL             *")
    print("*   STUDENTS  INFORMATION  SYSTEM         *")
    print("*******************************************")
    print("*  [A] Add New Students                   *")
    print("*  [B] Display Students Details           *")
    print("*  [X] Exit System                        *")
    print("*******************************************")
    choice = input("Please enter your choice: ")
    return choice


def displayDetails():
    with open("StudentDetails.txt", "r") as record:
        reader = record.read()
        print(reader)


def inputData():
    quit_choice = ''
    while quit_choice.upper() != 'X':
        user_choice = menu()

        if user_choice == 'A' or user_choice == 'a':
            print("\nADD NEW STUDENTS")
            name = input("Enter student's name: ")
            age = input("Enter age: ")
            studclass = input("Enter enrolled class: ")
            studentInfo = f"Name: {name} \t\tAge: {age}\t\t Class: {studclass}\n"

            with open("StudentDetails.txt", "a") as record:
                record.write(studentInfo)

        elif user_choice == 'B' or user_choice == 'b':
            print("\nDISPLAY STUDENT DETAILS")
            displayDetails()

        elif user_choice == 'X' or user_choice == 'x':
            print("Exit System")
            quit_choice = 'X'
        else:
            print("Invalid choice. Please try again.")


inputData()
