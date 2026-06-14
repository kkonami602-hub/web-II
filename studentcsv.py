import csv

subjects = ["English", "Math", "Science", "Social", "Computer"]

n = int(input("Enter number of students: "))

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)

    header = ["Name"] + subjects + ["Total", "Average"]
    writer.writerow(header)

    for i in range(n):
        print("\nEnter details for student")
        name = input("Name: ")

        marks = []
        total = 0

        for subject in subjects:
            mark = float(input(f"Enter marks in {subject}: "))
            marks.append(mark)
            total += mark

        average = total / len(subjects)

        writer.writerow([name] + marks + [total, average])

print("\nCSV file created successfully!")

with open("students.csv", "r") as file:
    reader = csv.reader(file)

    next(reader)
    print("\nStudent Records")

    for row in reader:
        name = row[0]
        total = float(row[6])
        average = float(row[7])

        print(f"{name} -> Total: {total}, Average: {average:.2f}")