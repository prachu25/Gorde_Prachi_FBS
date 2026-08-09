# sum of Two Number
def add(a,b):
    sum = a+b
    print("sum =",sum)

add(2,4)

# Large Number
def largest(a,b):

    if a > b:
        print("Largest =",a)
    else:
        print("Largest =",b)

largest(4,9)


# Check Even or Odd
def check_even_odd(num):
    if(num % 2 ==0 ):
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")

check_even_odd(5)
check_even_odd(6)

    