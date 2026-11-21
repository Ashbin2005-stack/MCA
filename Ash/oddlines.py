# Open the source file in read mode
file1 = open("source.txt", "r")

# Open the destination file in write mode
file2 = open("input.txt", "w")

# Read the file line by line
lines = file1.readlines()

# Copy only odd-numbered lines
for i in range(len(lines)):
    if (i + 1) % 2 != 0:
        file2.write(lines[i])

# Close the files
file1.close()
file2.close()

print("Odd lines copied successfully!")
