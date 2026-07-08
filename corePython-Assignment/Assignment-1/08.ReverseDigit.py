# Write a program to reverse three-digit number.

num = int(input('Enter a Number: '))
copy_num = num

rev = 0   

# Runs only when 'num' is of type string (input without int()).
# print('reversed number = ', num[::-1])   

while num > 0:
    last_digit = num % 10
    rev = rev * 10 + last_digit
    num = num // 10

print(f'The Reverse Number of {copy_num} is {rev}')
