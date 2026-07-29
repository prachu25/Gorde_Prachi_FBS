n = 5

for i in range(1,n+1):

    # Leading space
    for j in range(n-i):
        print("_", end=" ")


    # Numbers
    for j in range(1,i+1):
        if i == 1 or i == n or j == 1 or  j == i:
            print(j, end="   ")
        else:
            print("  ", end="  ")


    print()


"""
        1     # i == 1  or j == 1
      1   2   
    1       3     # j == i
  1           4   
1   2   3   4   5    # i == 5



see this pattern in esay way and add space 
        1
      1 2
    1   3
  1     4
1 2 3 4 5

"""