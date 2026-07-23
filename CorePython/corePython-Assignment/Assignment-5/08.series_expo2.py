# b. N + N^2 + N^3+N^4 .....+N^N (here ^ means exponent)
n = int(input('Enter a  number: '))

sum = 0

for i in range(1,n+1):
    term = n ** i
    sum += term


    if i == 1:
        print(n, end="")
    elif i == n:
        print(f" + {n}^{i}", end="")
    else:
        print(f" + {n}^{i}", end="")
    

print()

print("sum =", sum)