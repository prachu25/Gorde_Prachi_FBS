# 3. Python Program to Sort the List According to the Second Element in Sublist
"""
arr = [[1, 5], [2, 3], [4, 1], [6, 4]]

[1, 5] → 5
[2, 3] → 3
[4, 1] → 1
[6, 4] → 4

so result = [[4, 1], [2, 3], [6, 4], [1, 5]]

arr[j]       → current sublist
arr[j][1]    → second element of that sublist

arr[0]       → [1, 5]
arr[0][1]    → 5
"""

# USING BUBBLE SORT 
def sort_by_second(arr):

    n = len(arr)

    for i in range(n):

        for j in range(n-i-1):

            if arr[j][1] > arr[j+1][1]:

                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    return arr


arr = [[1, 5], [2, 3], [4, 1], [6, 4]]
print(sort_by_second(arr))