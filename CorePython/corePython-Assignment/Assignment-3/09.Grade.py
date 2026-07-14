# 09. Input 5 subject marks from user and display grade

m1 = int(input("Enter first Subject Marks: "))
m2 = int(input("Enter second Subject Marks: "))
m3 = int(input("Enter third Subject Marks: "))
m4 = int(input("Enter fourth Subject Marks: "))
m5 = int(input("Enter fifth Subject Marks: "))

total = m1 + m2 + m3 + m4 + m5
percentage = total / 5

print("Total =", total)
print("Percentage =", percentage)

if percentage >= 90:
    print("First Class")

elif percentage >= 80:
    print("Second Class")

elif percentage >= 55:
    print("Third Class")

elif percentage >= 40:
    print("Fourth Class")

else:
    print("Failed")