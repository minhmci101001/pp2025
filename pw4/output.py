import numpy as np

def calculate_gpa(students, marks, credits):
    for s in students:
        scores = []
        credit_list = []

        for cid, student_marks in marks.items():
            if s.id in student_marks:
                scores.append(student_marks[s.id])
                credit_list.append(credits[cid])

        if scores:
            s.gpa = np.sum(np.array(scores) * np.array(credit_list)) / np.sum(credit_list)
        else:
            s.gpa = 0.0


def sort_by_gpa(students, marks, credits):
    calculate_gpa(students, marks, credits)
    students.sort(key=lambda x: x.gpa, reverse=True)


def show_students(students, marks, credits):
    sort_by_gpa(students, marks, credits)
    print("\n===== STUDENT LIST =====")
    for s in students:
        print(f"{s.id} | {s.name} | GPA: {s.gpa:.2f}")


def show_marks(students, courses, marks):
    for c in courses:
        print(f"\nCourse: {c.name}")
        for s in students:
            print(f"{s.name}: {marks[c.id].get(s.id, 'N/A')}")
