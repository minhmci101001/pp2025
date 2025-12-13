students = []
courses = []
marks = {}

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


class Course(BasicInfo):
    def __init__(self, name, id):
        super().__init__(name, id)


def input_students():
    count = int(input("Enter number of students: "))
    for i in range(count):
        print(f"\n--- Student {i+1} ---")
        name = input("Name: ")
        sid = input("ID: ")
        dob = input("DoB: ")
        students.append(Student(name, sid, dob))


def input_courses():

    count = int(input("Enter number of courses: "))
    for i in range(count):
        print(f"\n--- Course {i+1} ---")
        name = input("Name: ")
        cid = input("ID: ")
        courses.append(Course(name, cid))
        marks[cid] = {}


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
        score = float(input(f"Enter mark for {s.name} (ID {s.id}): "))
        marks[cid][s.id] = score


def list_students():
    if not students:
        print("No students to display!")
        input_students()

    print("\n===== STUDENT LIST =====")
    for s in students:
        print(f"{s.describe()} | DoB: {s.dob}")


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
        score = marks[cid].get(s.id, "N/A")
        print(f"{s.name}: {score}")


def main():
    while True:
        print("\n===== MENU =====")
        print("1. Input Students")
        print("2. Input Courses")
        print("3. Input Marks")
        print("4. List Students")
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
