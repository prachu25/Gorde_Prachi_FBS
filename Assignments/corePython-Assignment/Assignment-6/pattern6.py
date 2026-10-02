n=5
num = 1
for i in range(1,n+1):

    # print space
    for j in range(1,n-i+1):
        print(" ", end=" ")

    # print numbers
    for j in range(1,2*i):
        print(j, end=" ")

    print()


"""
OutPut:
        1 
      1 2 3 
    1 2 3 4 5 
  1 2 3 4 5 6 7 
1 2 3 4 5 6 7 8 9 

"""