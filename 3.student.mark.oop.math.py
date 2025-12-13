import math
import numpy as np

students = []
courses = []
marks = {} 
credits = {}  

class BasicInfo:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def describe(self):
        return f"ID: {self.id} | Name: {self.name}"


class Student(BasicInfo):
    def __init__(self, name, id, dob):
        super().__init__(name, id)
        self.dob = dob
        self.gpa = 0.0


class Course(BasicInfo):
    def __init__(self, name, id, credit):
        super().__init__(name, id)
        self.credit = credit


def input_students():
    count = int(input("Enter number of students: "))
    for i in range(count):
        print(f"\n--- Student {i+1} ---")
        name = input("Name: ")
        sid = input("ID: ")
        dob = input("DoB: ")
        students.append(Student(name, sid, dob))


def input_courses():
    if not students:
        print("Input students first!")
        return

    count = int(input("Enter number of courses: "))
    for i in range(count):
        print(f"\n--- Course {i+1} ---")
        name = input("Name: ")
        cid = input("ID: ")
        credit = int(input("Credit: "))
        courses.append(Course(name, cid, credit))
        marks[cid] = {}
        credits[cid] = credit


def input_marks():
    if not students:
        print("No students available!, input students first!")
        input_students()
    if not courses:
        print("No courses available, input courses first!")
        input_courses()

    print("\nAvailable courses:")
    for c in courses:
        print(c.describe())

    cid = input("Enter course ID: ")

    if cid not in marks:
        print("Invalid course ID!")
        return

    for s in students:
        raw = float(input(f"Enter mark for {s.name} (ID {s.id}): "))
        score = math.floor(raw * 10) / 10
        marks[cid][s.id] = score


def calculate_gpa():
    for s in students:
        score_list = []
        credit_list = []

        for cid, student_marks in marks.items():
            if s.id in student_marks:
                score_list.append(student_marks[s.id])
                credit_list.append(credits[cid])

        if score_list:
            scores = np.array(score_list)
            creds = np.array(credit_list)
            s.gpa = np.sum(scores * creds) / np.sum(creds)
        else:
            s.gpa = 0.0


def sort_by_gpa():
    calculate_gpa()
    students.sort(key=lambda x: x.gpa, reverse=True)


def list_students():
    if not students:
        print("No students to display!")
        input_students()


    sort_by_gpa()

    print("\n===== STUDENT LIST (GPA DESCENDING) =====")
    for s in students:
        print(f"{s.describe()} | DoB: {s.dob} | GPA: {s.gpa:.2f}")


def show_marks():
    if not students:
        print("No students available!, input students first!")
        input_students()
    if not courses:
        print("No courses available, input courses first!")
        input_courses()

    print("\nAvailable courses:")
    for c in courses:
        print(c.describe())

    cid = input("Enter course ID: ")

    if cid not in marks:
        print("Course not found!")
        return

    print(f"\nMarks for course {cid}:")
    for s in students:
        print(f"{s.name}: {marks[cid].get(s.id, 'N/A')}")


def main():
    while True:
        print("\n===== MENU =====")
        print("1. Input Students")
        print("2. Input Courses")
        print("3. Input Marks")
        print("4. List Students (GPA)")
        print("5. Show Marks")
        print("0. Exit")

        choice = input("Choose: ")

        if choice == "1":
            input_students()
        elif choice == "2":
            input_courses()
        elif choice == "3":
            input_marks()
        elif choice == "4":
            list_students()
        elif choice == "5":
            show_marks()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")


main()
