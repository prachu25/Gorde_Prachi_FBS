# WAP to print multipliaction of digit

n = int(input('Enter a number: '))

mul =1
for i in range(1, n+1):
    mul = mul * i

print("Multiplication =", mul)