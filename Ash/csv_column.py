import csv

# Open the CSV file
file = open("student.csv", "r")

# Create CSV reader object
reader = csv.reader(file)

# Skip header
next(reader)

# Read a specific column (index 1)
for row in reader:
    print(row[1])

# Close the file
file.close()
