from input import input_students, input_courses, input_marks
from output import show_students, show_marks

students = []
courses = []
marks = {}
credits = {}

def main():
    while True:
        print("\n1. Input Students")
        print("2. Input Courses")
        print("3. Input Marks")
        print("4. Show Students (GPA)")
        print("5. Show Marks")
        print("0. Exit")

        choice = input("Choose: ")

        if choice == '1':
            input_students(students)
        elif choice == '2':
            input_courses(courses, marks, credits)
        elif choice == '3':
            input_marks(students, courses, marks)
        elif choice == '4':
            show_students(students, marks, credits)
        elif choice == '5':
            show_marks(students, courses, marks)
        elif choice == '0':
            break

main()
