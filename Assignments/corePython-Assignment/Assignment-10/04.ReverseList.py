# 4. Write a program to reverse the list.

def reverseList(lst):

    left = 0
    right = len(lst) - 1

    while(left < right):
        temp = lst[left]
        lst[left] = lst[right]
        lst[right] = temp

        left+=1
        right-=1

    return lst

num_list = [10,20,30,40,50,60]
ans = reverseList(num_list)
print(ans)



