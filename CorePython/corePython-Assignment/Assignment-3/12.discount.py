ticket = int(input("Enter Ticket Amount: "))

total = 0

# Person 1
age = int(input("Enter Age of Person 1: "))
if age < 12:
    total += ticket - (ticket * 30 // 100)
elif age > 59:
    total += ticket - (ticket * 50 // 100)
else:
    total += ticket

# Person 2
age = int(input("Enter Age of Person 2: "))
if age < 12:
    total += ticket - (ticket * 30 // 100)
elif age > 59:
    total += ticket - (ticket * 50 // 100)
else:
    total += ticket

# Person 3
age = int(input("Enter Age of Person 3: "))
if age < 12:
    total += ticket - (ticket * 30 // 100)
elif age > 59:
    total += ticket - (ticket * 50 // 100)
else:
    total += ticket

# Person 4
age = int(input("Enter Age of Person 4: "))
if age < 12:
    total += ticket - (ticket * 30 // 100)
elif age > 59:
    total += ticket - (ticket * 50 // 100)
else:
    total += ticket

# Person 5
age = int(input("Enter Age of Person 5: "))
if age < 12:
    total += ticket - (ticket * 30 // 100)
elif age > 59:
    total += ticket - (ticket * 50 // 100)
else:
    total += ticket

print("Total Ticket Amount =", total)