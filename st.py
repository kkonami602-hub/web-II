class Student:
    def __init__(self):
        self.name = ""
        self.roll_number = ""
        self.marks = 0

    def input_details(self):
        self.name = input("Enter Name: ")
        self.roll_number = input("Enter Roll Number: ")
        self.marks = float(input("Enter Marks: "))

    def display_details(self):
        print("\nName:", self.name)
        print("Roll Number:", self.roll_number)
        print("Marks:", self.marks)


students = []

n = int(input("Enter number of students: "))

for i in range(n):
    print("\nEnter details of student")
    s = Student()
    s.input_details()
    students.append(s)

print("\n STUDENT DETAILS")

for s in students:
    s.display_details()