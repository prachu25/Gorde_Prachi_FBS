n = 5

for i in range(1,n+1):

    for j in range(1,n-i+1):
        print(' ', end=" ")

    # Increasing 
    num = i
    for j in range(1,i+1):
        print(num, end=" ")
        num+=1

    # Decreasing
    num-=2
    for j in range(i-1, 0,-1):
        print(num, end=" ")
        num-=1

    print()

"""
        1 
      2 3 2 
    3 4 5 4 3 
  4 5 6 7 6 5 4 
5 6 7 8 9 8 7 6 5 

"""  