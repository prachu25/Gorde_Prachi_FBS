# QUE) Write a program of having n number of elements in the list and find out even
#      and odd elements in that list and then create two separate lists which will have
#      even elements and other will have odd elements.


def findEvenOdd(lst):

    even_list = []
    odd_list = []

    for i in lst:
        if(i % 2 == 0):
            even_list.append(i)
        else:
            odd_list.append(i)

    return even_list, odd_list


numbers = [1,2,3,4,6,5,6,7,8,9,10,12,12,13,20]

even, odd = findEvenOdd(numbers)

print("Even List =", even)
print("Odd List =", odd)