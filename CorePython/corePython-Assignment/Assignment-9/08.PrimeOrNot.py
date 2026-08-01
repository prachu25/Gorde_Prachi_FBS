# Write a program to check whether a number is prime or not using recursion.

def isPrime(n, i):

    if i == n:
        return True

    if n % i == 0:
        return False

    return isPrime(n, i + 1)


num = int(input('Enter a number: '))

if num <= 1:
    print(num, "is not Prime")
elif isPrime(num,2):
    print(num, "is Prime")
else:
    print(num, "Not Prime")