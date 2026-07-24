n=5

for i in range(1,n+1):

    # print space
    for j in range(1,n-i+1):
        print(' ', end=" ")

    # print alphabet
    for j in range(1,2*i):
        print(chr(64+j), end=" ")

    print()

"""
OutPut:
        A
      A B C
    A B C D E
  A B C D E F G
A B C D E F G H I 

"""