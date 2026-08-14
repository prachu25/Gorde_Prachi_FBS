# Linear Serach
def LinearSerach(lst, target):

    for i in range(len(lst)):
        if(lst[i] == target):
            return i
    return -1


lst = [7,45,6,33,23,89]
ele = 45
res = LinearSerach(lst,ele)
if(res != -1):
    print(f"{ele} found at index {res}")
else:
    print("Element Not Found")

# Time coplexity - 
# BEST CASE - O(1)  at first ele
# Worst - O(N)
# Average Case - o(n/2)