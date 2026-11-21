import csv

# Dictionary data
data = [
    {"RollNo": 1, "Name": "Rahul", "Mark": 85},
    {"RollNo": 2, "Name": "Anu", "Mark": 90},
    {"RollNo": 3, "Name": "John", "Mark": 78},
    {"RollNo": 4, "Name": "Meera", "Mark": 95}
]

# Write dictionary to CSV file
with open("student.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["RollNo", "Name", "Mark"])

    writer.writeheader()
    writer.writerows(data)

print("Dictionary written to CSV file successfully!")

# Read and display CSV file
with open("student.csv", "r") as file:
    reader = csv.DictReader(file)

    print("\nStudent Details:")

    for row in reader:
        print(row)
