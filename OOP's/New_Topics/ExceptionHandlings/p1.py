
try:
    a = int(input('Enter a num1: '))
    b = int(input('Enter a num2: '))

    res = a // b
    print(res)

except ZeroDivisionError :
    print("we can not divide by Zero")
except ValueError as v:
    print(v)
except Exception as e:
    print("can not divide by zero...")
else:
    print("when exception not occure then and then else block will exceute..")

