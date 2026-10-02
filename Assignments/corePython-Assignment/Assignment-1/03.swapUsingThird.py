# write program to swap using the third variable

first = int(input('Enter a first number: '))
second = int(input('Enter a second number: '))

print('------Before Swaping-----')

print('FIRST' , first)
print('SECOND',second)


temp = first
first = second
second = temp

print('------After a swapping-------')
print('FIRST' , first)
print('SECOND',second)