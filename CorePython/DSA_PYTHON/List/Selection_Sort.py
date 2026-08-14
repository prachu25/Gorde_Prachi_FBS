def selectionSort(lst):

    size = len(lst)

    for i in range(0, size-1):
        min_ele = i

        for j in range(i+1, size):

            if(lst[j] < lst[min_ele]):
                min_ele = j


        lst[i], lst[min_ele]= lst[min_ele], lst[i]


li = [40,60,50,20,30,10,-80]
selectionSort(li)

print("Selection Sort =", li)