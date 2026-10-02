# Python Program to Sort a List According to the Length of the Elements within the list.
"""
arr = ["apple", "hi", "banana", "cat", "I"]

apple   → 5
hi      → 2
banana  → 6
cat     → 3
I       → 1
"""

# USING SELECTION SORT
def sort_by_length(arr):
    n = len(arr)

    for i in range(n):

        min_ind = i

        for j in range(i+1, n):

            if len(arr[j]) < len(arr[min_ind]):
                min_ind = j

        # SWAP
        arr[i], arr[min_ind] = arr[min_ind], arr[i]

    return arr


arr = ["apple", "hi", "banana", "cat", "I"]
print(sort_by_length(arr))