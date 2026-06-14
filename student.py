'''Create a program that takes a list of student names and stores them in a file. Then, read 
the file and display the contents.'''
n = int(input("Enter number of students: "))

file = open("students.txt", "w")

for i in range(n):
    name = input(f"Enter name of student: ")
    file.write(name + "\n")

file.close()

print("\nData written successfully!\n")

# Step 4: Read from file and display
file = open("students.txt", "r")

print("Student Names in File:")

for line in file:
    print(line.strip())

file.close()