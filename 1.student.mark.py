students = []
courses = []
marks = {}  



def input_students():
    n = int(input("Enter number of students: "))
    for i in range(n):
        print(f"\n--- Student {i+1} ---")
        sid = input("Student ID: ")
        name = input("Student name: ")
        dob = input("Student DoB: ")
        students.append({"id": sid, "name": name, "dob": dob})


def input_courses():
    n = int(input("Enter number of courses: "))
    for i in range(n):
        print(f"\n--- Course {i+1} ---")
        cid = input("Course ID: ")
        cname = input("Course name: ")
        courses.append({"id": cid, "name": cname})


def input_marks():
    course_id = input("Enter course ID to input marks: ")

    course_ids = [c["id"] for c in courses]
    if course_id not in course_ids:
        print("Course not found!")
        return

    print(f"\nEntering marks for course: {course_id}\n")

    for s in students:
        m = float(input(f"Mark for {s['name']} with id {s['id']}: "))
        marks[(s["id"], course_id)] = m


def list_students():
    print("\n=== List of Students ===")
    for s in students:
        print(f"ID: {s['id']}, Name: {s['name']}, DoB: {s['dob']}")


def list_courses():
    print("\n=== List of Courses ===")
    for c in courses:
        print(f"ID: {c['id']}, Name: {c['name']}")


def show_marks():
    cid = input("Enter course ID to show marks: ")
    print(f"\n=== Marks for course {cid} ===")

    for s in students:
        key = (s["id"], cid)
        if key in marks:
            print(f"{s['name']} ({s['id']}): {marks[key]}")
        else:
            print(f"{s['name']} ({s['id']}): No mark")



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
            list_courses()
        elif choice == "6":
            show_marks()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
