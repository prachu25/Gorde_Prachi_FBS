# Write a program to calculate the m to the power n using recursion.

def power_using_recursion(m, n):

    if n == 0:
        return 1

    return m * power_using_recursion(m,n-1)

# m → stays the same (the base never changes)
# n → decreases by 1 each recursive call
 

 
base = int(input('Enter a Base (m): '))
power = int(input('Enter a Power (n): '))

res = power_using_recursion(base, power)
print("Answer = ", res)