# WAP to print factorial of a number .

num = int(input('Enter a number to calculate teh factorial: '))

fact = 1
i = 1

while(i <= num):
    fact = fact * i
    i +=1

print("Factorial =", fact)