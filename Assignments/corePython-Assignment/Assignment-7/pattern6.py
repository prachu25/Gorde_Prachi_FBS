n= 5
k=7   # for space
for i in range(1,n+1):

    for j in range(1,i+1):
        print(j, end=" ")

# for space
    for j in range(1,k+1):
        print(' ', end=" ")
    k-=2  # space decrease by 2

    for j in range(i,0,-1):
        if(i!=5 or j!=5):
            print(j, end=" ")


    print()


"""
output:

1               1 
1 2           2 1 
1 2 3       3 2 1 
1 2 3 4   4 3 2 1 
1 2 3 4 5 4 3 2 1 

"""