'''Implement a program to store student records (name, roll, marks,contact number) using a 
dictionary.
a. Provide menu options to add, search, and display students.'''

students = {}

while True:
    print("\n STUDENT MENU")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Display All Students")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        roll = input("Enter Roll Number: ")

        if roll in students:
            print("Student with this roll number already exists!")
        else:
            name = input("Enter Name: ")
            marks = float(input("Enter Marks: "))
            contact = input("Enter Contact Number: ")

            students[roll] = {
                "name": name,
                "marks": marks,
                "contact": contact
            }

            print("Student added successfully!")

    elif choice == "2":
        roll = input("Enter Roll Number to search: ")

        if roll in students:
            print("\n Student Details")
            print("Roll:", roll)
            print("Name:", students[roll]["name"])
            print("Marks:", students[roll]["marks"])
            print("Contact:", students[roll]["contact"])
        else:
            print("Student not found!")

    elif choice == "3":
        if not students:
            print("No student records found!")
        else:
            print("\n All Students")
            for roll, info in students.items():
                print("\nRoll:", roll)
                print("Name:", info["name"])
                print("Marks:", info["marks"])
                print("Contact:", info["contact"])

    elif choice == "4":
        print("Exiting")
        break

    else:
        print("Invalid choice! Please try again.")