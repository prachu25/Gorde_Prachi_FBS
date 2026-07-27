for i in range(1,6):
    for j in range(1,6):
        print(i, end=" ")     # same value in rows use i
    print()


print()
print("NEW Pattern For Column")
for l in range(1,6):
    for m in range(1,6):
        print(m, end=" ")     # same value in columns use j
    print()

"""
OutPUT:
1 1 1 1 1 
2 2 2 2 2 
3 3 3 3 3 
4 4 4 4 4 
5 5 5 5 5 

NEW Pattern For Column
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 
"""