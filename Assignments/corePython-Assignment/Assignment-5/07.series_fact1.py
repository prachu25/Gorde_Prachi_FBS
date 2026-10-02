# 7. Write a program to solve the following series :
# a. 1! + 2! + 3! + 4! + .....n!

n = int(input('Enter a number: '))

sum = 0
fact = 1

for i in range(1,n+1):
    fact = fact * i
    sum =sum + fact

    if( i==n):
        print(f"{i}!", end=" \n")
    else:
        print(f"{i}! + ", end=" ")


print("SUM = ",sum)