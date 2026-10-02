n = 5

for i  in range(1,n+1):

    # print Space
    for j in range(1,n-i+1):
        print(" ", end=" ")

    # print star
    for j in range(1,2*i):
        print("*", end=" ")

    print()

""" 
Output:
        * 
      * * * 
    * * * * * 
  * * * * * * * 
* * * * * * * * * 

"""