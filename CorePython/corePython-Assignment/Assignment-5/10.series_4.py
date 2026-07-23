# e. x - x2/3 + x3/5 - x4/7 + .... to n terms

x = int(input('Enter x number: '))
n = int(input('Enter number of terms: '))

sum = 0
denominator = 1

for i in range(1, n+1):
    term = (x**i)/ denominator

    if i% 2 != 0:     # only odd term add
        sum+=term
    else:
        sum-=term

    denominator +=2       # because of odd i.e +2 number  that we observed in que

print("Sum =", round(sum,2))