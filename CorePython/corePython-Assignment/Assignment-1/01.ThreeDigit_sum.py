# write a program to calculate the three digit sum

num = int(input('Enter a number: '))

orignal = num
sum = 0;

while num >0:
    digit = num%10
    sum=sum+digit
    num//=10

print(f'The sum of {orignal} is',sum)