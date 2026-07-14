# 05. Write a program to check whether the triangle is equilateral, isosceles or scalene triangle.

a = int(input('Enter a first angle: '))
b = int(input('Enter a second angle: '))
c = int(input('Enter a third angle: '))

if a==b==c:
    print('Triangle is Equilateral')
elif a==b or b==c or c==a:
    print('Triangle is Iscosceles')
else:
    print('Triangle is Scalene')