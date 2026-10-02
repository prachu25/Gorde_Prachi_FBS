students = int(input("Enter number of students: "))

# Store total percentage of all students
totalPercentage = 0

for i in range(1, students + 1):

    print("Student", i)

    totalMarks = 0

    #  Accept marks of 5 subjects
    for j in range(1, 6):

        marks = float(input(f"Enter marks of Subject {j}: "))
        totalMarks += marks

    # Calculate percentage
    percentage = (totalMarks / 500) * 100

    # Display percentage
    print("Percentage =", percentage)

    # Add percentage for average
    totalPercentage += percentage

# Calculate average percentage
average = totalPercentage / students

# Display average percentage
print("Average Percentage =", round(average,3))