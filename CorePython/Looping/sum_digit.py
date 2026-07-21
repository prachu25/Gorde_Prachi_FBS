n = int(input('Enter a number: '))  # let n = 3

sum = 0

for i in range(1, n+1):     # range(1, 3+1):     last digit 4 is ignore
    print(i)
    sum = sum + i
     
print("sum = ",sum) 