# 7. WAP to print all integers up to n that aren't divisible by 2 and 3.
num = int(input('Enter a number: '))

for i in range(1, num+1):
    if(i % 2!=0 and i % 3 !=0):
        print(i)


"""
OUTPUT:
Enter a number: 20
1
5
7
11
13
17
19
"""
