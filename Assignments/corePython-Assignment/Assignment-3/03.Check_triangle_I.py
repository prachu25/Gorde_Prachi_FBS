# 03. Write a program to input angles of a triangle and check whether triangle is valid or not.

a = int(input('Enter a first angle: '))
b = int(input('Enter a second angle: '))
c = int(input('Enter a third angle: '))

sum_check = a + b + c

if sum_check == 180:
    print('Triangle is VALID')
else:
    print('Triangle is NOT VALID')