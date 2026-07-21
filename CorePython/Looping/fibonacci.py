# WAP to print th e fibonacci series

n = int(input('Enter a number: '))

first = 0
second = 1

for i in range(n):      # if only one parameter is going to pass to the range function sequence we always start from zero to value-1.
    print(first, end=" ")
    next = first + second
    first = second
    second = next



  
# i = 0

# while(i <= n):

#     print(first, end=" ")
#     next = first + second
#     first = second
#     second = next

#     i+=1



