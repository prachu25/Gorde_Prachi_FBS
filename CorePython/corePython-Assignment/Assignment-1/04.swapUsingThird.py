# write a program to swap without using third variable

first = int(input('Enter a first number: '))    # 10
second = int(input('Enter a second number: '))  # 20

print('----Before swapping------')
print('First: ', first)
print('Second:', second)

# perform  operation without using third var
first = first + second     # first = 10 + 20 => 30
second = first - second    # second = 30 - 20 => 10
first = first - second     # first = 30 - 10 => 20

print('----After swapping------')
print('First: ', first)
print('Second:', second)


