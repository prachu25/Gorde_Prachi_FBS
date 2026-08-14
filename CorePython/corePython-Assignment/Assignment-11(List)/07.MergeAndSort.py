# 2. Python Program to Merge Two Lists and Sort it

list1 = [5, 2, 8]
list2 = [1, 7, 3]

# USING BUILT IN FUNCTION
# result = list1 + list2
# result.sort()

# print(result)



# WITHOUT BUILT IN FUNCTION

# mrege to list
def mergeToList(lst1, lst2):

    res = []

    for i in lst1:
        res.append(i)

    for j in lst2:
        res.append(j)

    return res


# Bubble Sort 
def bubble_sort(arr):

    n = len(arr)

    for i in range(n):

        for j in range(n-i-1):

            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

    return arr



# first Merge
res = mergeToList(list1,list2)
print("Merge = ",res)

# Then Sort
sorted_res = bubble_sort(res)
print("Sorted = ", sorted_res)        
