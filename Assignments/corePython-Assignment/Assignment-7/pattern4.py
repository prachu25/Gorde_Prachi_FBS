n = 5

for i in range(1,n+1):

    # print space
    for j in range(1,n-i+1):
        print(' ', end=" ")

    for j in range(1,i+1):
        print(j, end=" ")

    # reverse loop
    for j in range(i-1, 0,-1):
        print(j, end=" ")

    print()


"""
output:
        1 
      1 2 1 
    1 2 3 2 1 
  1 2 3 4 3 2 1 
1 2 3 4 5 4 3 2 1 


"""
    