import json

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def describe(self):
        return f"{self.name} has got {self.marks}"

    def to_dict(self):
        return {"name": self.name, "marks": self.marks}

def save_students(students, filename):
    data = [s.to_dict() for s in students]
    with open(filename, "w") as f:
        json.dump(data, f, indent = 2)

def load_students(filename):
    try:
        with open(filename, "r") as f:
            data =  json.load(f)
    except FileNotFoundError:
        return []

    students = []
    for d in data:
        s = Student(d["name"], d["marks"])
        students.append(s)
    return students

def get_number(prompt):
    while True:
        try:
            return(int(input(prompt)))
        except ValueError:
            print("Please Enter a valid number!")

students = load_students("students.json")

while True:
    print("\n1) Add Student\n2) Show all\n3) Average Marks\n4) Show Top Student\n5) Quit")
    choice = get_number("Choose: ")

    if choice == 1:
        try:
            name = input("Name: ")
            marks = int(input("Marks: "))
            students.append(Student(name, marks))
            save_students(students, "students.json")
            print("Added!")

        except ValueError:
            print("Please enter a valid number")

    elif choice == 2:
        for s in students:
            print (s.describe())

    elif choice == 3:
        try:
            print(sum(s.marks for s in students)/ len (students))

        except ZeroDivisionError:
            None

    elif choice == 4:
        if not students:
            None
        else:
            top_student = students[0]
            for s in students:
                if s.marks > top_student.marks:
                    top_student = s
                
            print(f"{top_student.name} is top")
    elif choice == 5:
        print("Goodbye!")
        break

    else:
        print("Choose right one!")
