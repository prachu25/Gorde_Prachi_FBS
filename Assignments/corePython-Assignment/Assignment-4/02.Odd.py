# WAP to print all odd numbers until n.

num = int(input('Enter a number: '))

i = 1

while( i <= num):
    
    if(i%2==1):
        print(i, end=" ")   # i.e  num = 7   o/p: 1 3 5 7
    
    i+=1


