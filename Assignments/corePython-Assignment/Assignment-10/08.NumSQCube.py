# 12. Write a program to create three lists of numbers, their squares and cubes

def listNumbers(lst):

    square =[]
    cube = []

    for i in lst:
        square.append(i*i)
        cube.append(i*i*i)

    print("Number List =", lst)
    print("Square List =", square)
    print("cube List =", cube)



num_list = [1,2,3,4,5,6]
listNumbers(num_list)
