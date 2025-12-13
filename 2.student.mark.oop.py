student = []
course = []
mark = {}

class BasicInfo():
    def __init__(self, n, id):
        self.name = n
        self.id = id
    def describe(self):
        return f"ID: {self.id}  |  Name: {self.name}"

class Student(BasicInfo):
    def __init__(self, n, id, dob):
        super().__init__(n, id)
        self.dob = dob
    
class Course(BasicInfo):
    def __init__(self, n, id):
        super().__init__(n, id)

def set_student():
    count = int(input("Enter number of students: "))
    for i in range (count):
        print(f"---Student {i+1}---")
        s_name = str(input(f"Name: "))
        s_id = str(input(f"ID: "))
        s_dob = str(input(f"DoB: "))
        new_s = Student(s_name, s_id, s_dob)
        student.append(new_s)
    
def set_course():
    count = int(input("Enter number of courses: "))
    for i in range (count):
        print(f"---Course {i+1}---")
        c_name = str(input(f"Name: "))
        c_id = str(input(f"ID: "))
        new_c = Course(c_name, c_id)
        course.append(new_c)
        mark[c_id] = {}
     
def set_mark():
    if not course:
        print("No course avaiable")
        return
    for c in course:
        print(c.describe())
    selected_id = input("Enter course ID to get mark: ")
    if selected_id in mark:
        for s in student:
            score = float(input(f"Enter mark for {s.name} (ID {s.id}): "))
            mark[selected_id][s.id] = score
    else:
        print("Invalid Course ID")
        
def get_student():
    print("")
    print("-----Student list-----")
    for s in student:
        print(f"ID: {s.id}, Name: {s.name}, DoB: {s.dob}")
        
def get_mark():
    print("")
    print("-----Showing Mark-----")
    for c in course:
        print(f"Available courses: {c.name} (ID: {c.id})")
    c_id = input("Enter the Course ID: ")
    if c_id in mark:
        print(f"Mark for {c.name}: ")
        for s in student:
            score = mark[c_id].get(s.id, "N/A")
            print(f"{s.name}: {score}")
    else:
        print("Course not found")

def main():
    while True:
        print("\n1. Input Students")
        print("2. Input Courses")
        print("3. Input Marks")
        print("4. List Students")
        print("5. Show Marks")
        print("0. Exit")
        
        user = input()
        
        if user == '1':
            print("-----Setting student info: -----")
            set_student()
        elif user == '2':
            print("-----Setting course info: ------")
            set_course()
        elif user == '3':
            print("-----Setting mark for student: -----")
            set_mark()
        elif user == '4':
            print("-----Listing all student: -----")
            get_student()
        elif user == '5':
            print("-----Showing all student info: -----")
            get_mark()
        elif user == '0':
            break
main()