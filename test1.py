# ============================
# Student Mark Management
# Using lists, dicts, tuples only – NO classes
# ============================

students = []      # Each student: {"id": "...", "name": "..."}
courses = []       # Each course: {"id": "...", "name": "..."}
marks = {}         # Key: (student_id, course_id), value: mark


# ============================
# Input functions
# ============================

def input_students():
    n = int(input("Number of students: "))
    for i in range(n):
        sid = input(f"Student {i+1} ID: ")
        name = input(f"Student {i+1} name: ")
        students.append({"id": sid, "name": name})


def input_courses():
    n = int(input("Number of courses: "))
    for i in range(n):
        cid = input(f"Course {i+1} ID: ")
        name = input(f"Course {i+1} name: ")
        courses.append({"id": cid, "name": name})


def input_marks():
    course_id = input("Enter course ID to input marks: ")

    # Check course exists
    course_ids = [c["id"] for c in courses]
    if course_id not in course_ids:
        print("Course not found!")
        return

    for s in students:
        m = float(input(f"Mark for student {s['name']} ({s['id']}): "))
        marks[(s['id'], course_id)] = m


# ============================
# Output functions
# ============================

def list_students():
    print("\n--- Student List ---")
    for s in students:
        print(f"ID: {s['id']}, Name: {s['name']}")


def list_courses():
    print("\n--- Course List ---")
    for c in courses:
        print(f"ID: {c['id']}, Name: {c['name']}")


def show_marks():
    course_id = input("Enter course ID to show marks: ")

    print(f"\n--- Marks for course {course_id} ---")
    for s in students:
        key = (s['id'], course_id)
        if key in marks:
            print(f"{s['name']} ({s['id']}): {marks[key]}")
        else:
            print(f"{s['name']} ({s['id']}): No mark")


# ============================
# Menu
# ============================

def main():
    while True:
        print("\n===== Student Mark Management =====")
        print("1. Input students")
        print("2. Input courses")
        print("3. Input marks for a course")
        print("4. List students")
        print("5. List courses")
        print("6. Show marks for a course")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            input_students()
        elif choice == "2":
            input_courses()
        elif choice == "3":
            input_marks()
        elif choice == "4":
            list_students()
        elif choice == "5":
            list_courses()
        elif choice == "6":
            show_marks()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")


# Run program
if __name__ == "__main__":
    main()
