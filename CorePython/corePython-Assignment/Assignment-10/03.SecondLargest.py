# 3. Write a program to find the second largest element in the list.

def second_Largest(lst):

    max = lst[0]
    second_max = lst[0]

    for i in range(len(lst)):
        if(lst[i] > max):
            second_max = max
            max = lst[i]
        else:
            if(lst[i] > second_max and lst[i] != max):
                second_max = lst[i]

    return second_max

num_list = [22,33,45,90,81,76,120]
res = second_Largest(num_list)
print("Second Largest =", res)



    