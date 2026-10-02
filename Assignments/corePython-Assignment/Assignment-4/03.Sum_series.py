# WAP to print sum of series upto n.

num = int(input('Enter a Number: '))

sum = 0
i = 0

while(i <= num):
    sum = sum + i
    # print(i)
    i+=1

print("Sum = ",sum)


"""
output: 
Enter the value of n: 3
Sum = 6
"""