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


def set_student():
    count = int(input("Enter number of students: "))
    for i in range(count):
        print(f"\n--- Student {i+1} ---")
        name = input("Name: ")
        sid = input("ID: ")
        dob = input("DoB: ")
        students.append(Student(name, sid, dob))


def set_course():
    count = int(input("Enter number of courses: "))
    for i in range(count):
        print(f"\n--- Course {i+1} ---")
        name = input("Name: ")
        cid = input("ID: ")
        credit = int(input("Credit: "))
        courses.append(Course(name, cid, credit))
        marks[cid] = {}
        credits[cid] = credit


def set_mark():
    if not courses:
        print("No courses available")
        return

    for c in courses:
        print(c.describe())

    cid = input("Enter course ID: ")

    if cid in marks:
        for s in students:
            raw_score = float(input(f"Enter mark for {s.name}: "))
            score = math.floor(raw_score * 10) / 10
            marks[cid][s.id] = score
    else:
        print("Invalid course ID")


def calculate_gpa():
    for s in students:
        score_list = []
        credit_list = []

        for cid, student_scores in marks.items():
            if s.id in student_scores:
                score_list.append(student_scores[s.id])
                credit_list.append(credits[cid])

        if score_list:
            scores = np.array(score_list)
            credit_arr = np.array(credit_list)

            s.gpa = np.sum(scores * credit_arr) / np.sum(credit_arr)
        else:
            s.gpa = 0.0


def sort_by_gpa():
    calculate_gpa()
    students.sort(key=lambda x: x.gpa, reverse=True)


def show_students():
    print("\n===== STUDENT LIST (GPA DESCENDING) =====")
    sort_by_gpa()
    for s in students:
        print(f"{s.id} | {s.name} | DoB: {s.dob} | GPA: {s.gpa:.2f}")


def show_marks():
    for c in courses:
        print(f"\nCourse: {c.name}")
        for s in students:
            score = marks[c.id].get(s.id, "N/A")
            print(f"{s.name}: {score}")


def main():
    while True:
        print("\n========== MENU ==========")
        print("1. Input Students")
        print("2. Input Courses")
        print("3. Input Marks")
        print("4. Show Students (Sorted by GPA)")
        print("5. Show Marks")
        print("0. Exit")

        choice = input("Choose: ")

        if choice == '1':
            set_student()
        elif choice == '2':
            set_course()
        elif choice == '3':
            set_mark()
        elif choice == '4':
            show_students()
        elif choice == '5':
            show_marks()
        elif choice == '0':
            break
        else:
            print("Invalid choice")


main()
