import math
from domains import Student, Course

def input_students(students):
    count = int(input("Enter number of students: "))
    for _ in range(count):
        name = input("Name: ")
        sid = input("ID: ")
        dob = input("DoB: ")
        students.append(Student(name, sid, dob))


def input_courses(courses, marks, credits):
    count = int(input("Enter number of courses: "))
    for _ in range(count):
        name = input("Name: ")
        cid = input("ID: ")
        credit = int(input("Credit: "))
        courses.append(Course(name, cid, credit))
        marks[cid] = {}
        credits[cid] = credit


def input_marks(students, courses, marks):
    for c in courses:
        print(f"{c.id} - {c.name}")

    cid = input("Enter course ID: ")

    if cid in marks:
        for s in students:
            raw = float(input(f"Mark for {s.name}: "))
            marks[cid][s.id] = math.floor(raw * 10) / 10
    else:
        print("Invalid course ID")
