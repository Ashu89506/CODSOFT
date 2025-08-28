#   TO DO LIST
student_grades={ }

def add_student(name,grade):
    student_grades[name]= grade
    print(f"Added {name} with a {grade}")


def update_student(name,grade):
    if name in student_grades:
        student_grades[name]=grade
        print(f"Added {name} with marks are updated  {grade}")
    else:
        print(f"{name} is not found!")


def student_delete(name):
    if name in student_grades:
        del student_grades[name]
        print(f"{name} has been successfully delete")
    else:
        print(f"{name} is not found!")


def display_all_student():
    if student_grades:
        for name,grade in student_grades.items():
            print(f"{name} : {grade}")
    else:
        print("No students found")

def main():
    while True:
        print('\n student Grades Management System')
        print("1. Add a Student")
        print("2. Update a Student")
        print("3. Delete a Student")
        print("4. View Student")
        print("5. Exit")

        try:
            choice=int(input("Enter ur choice"))
        except ValueError:
            print("Please input a valid number")
            continue
        if choice==1:
            name=input("Enter student name =")
            try:
                grade=int(input("Enter student grade ="))
                add_student(name,grade)
            except ValueError:
                print("Grade must be a number")
        elif choice==2:
            name=input("Enter student name =")
            try:
                grade=int(input("Enter student grade ="))
                update_student(name,grade)
            except ValueError:
                grade=int(input("Enter student grade ="))
           
        elif choice==3:
            name=input("Enter student name =")
            student_delete(name)
        elif choice==4:
           display_all_student()
        elif choice==5:
            print("Closing the program")
            break
        else:
            print("Invalid choice")
main()
            

    


