n = 4

for i in range(n):

    # printing space
    for s in range(n-i-1):
        print(" ", end="")

    # first number of every row is 1
    num = 1

    # print numbers
    for j in range(i+1):
        print(num,end=" ")

        # update next number
        num = num*(i-j)//(j+1)

    print()

"""
output:
   1 
  1 1 
 1 2 1 
1 3 3 1 

"""