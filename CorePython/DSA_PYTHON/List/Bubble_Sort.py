def bubbleSort(lst):

    size = len(lst)

    for i in range(1,size):

        for j in range(0,size-i):
            if(lst[j] > lst[j+1]):
                lst[j], lst[j+1] = lst[j+1], lst[j]


list_sorting = [70,-30,60,10,50,40,20]

print("Before Sorting = ", list_sorting)
bubbleSort(list_sorting)
print("After Sorting = ", list_sorting)