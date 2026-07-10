# Program to find quotient and remainder of two numbers.

'''
Approach (Algorithm)
Take dividend and divisor as input from the user.
Calculate the quotient using integer division (//).
Calculate the remainder using the modulus operator (%).
Print the quotient and remainder.

Formula
Quotient = Dividend // Divisor
Remainder = Dividend % Divisor

'''

divident = float(input('Enter a divident: '))
divisor = float(input('Enter divisor: '))

q = divident // divisor
rem = divident % divisor

print('Quotient: ',q)
print('Reminder: ',rem)

