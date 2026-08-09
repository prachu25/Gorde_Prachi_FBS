# without passing parameter (without input)
# with returing value        (with output)

def addition():

    num1 = int(input('Enter a number1: '))
    num2 = int(input('Enter a number2: '))

    sum = num1 + num2

    return sum    # return value sum


# Function  call
res = addition()
print("the addition is ", res)