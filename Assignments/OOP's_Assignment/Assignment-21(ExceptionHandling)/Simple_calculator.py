try:

    num1 = int(input('Enter first number: '))
    num2 = int(input('Enter Second number: '))

    operator = input('Enter operation ( +, -, *, /): ')

    if operator not in ["+", "-", "*", "/"]:
        raise ValueError("Invalid Error")


    if operator == "+":
        result = num1 + num2

    elif operator == "-":
        result = num1 - num2

    elif operator == "*":
        result = num1 * num2

    elif operator == "/":
        result = num1/num2

    print("Result: ", result)


except ValueError as e:
    print("Error: ", e)

except ZeroDivisionError as e:
    print("Error: can not divide by zero!!")
