# Write a program to enter P, T, R and calculate Compound Interest.

p = float((input('Enter Pricipal Amount: ')))
t = float(input("Enter Time (in years): "))
r = float(input("Enter Rate of Interest: "))


# formula - p(1 + r/100) pow t
amount = p * (1 + r /100) ** t

CI = amount - p

print("Compound Interest =", CI)
print("Total Amount =", amount)