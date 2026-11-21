# Open the file in read mode
file = open("sample.txt", "r")

# Create an empty list
lines = []

# Read file line by line
for line in file:
    lines.append(line.strip())

# Close the file
file.close()

# Display the list
print("Lines stored in the list:")
print(lines)
