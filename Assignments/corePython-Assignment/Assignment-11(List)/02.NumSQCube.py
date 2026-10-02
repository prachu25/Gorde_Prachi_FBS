def createSQCubeList(lst):

    sq_list = []
    cube_list = []

    for i in lst:
        sq_list.append(i*i)
        cube_list.append(i*i*i)

    return sq_list, cube_list


lst = [1,2,3,4,5,6,7,8,9,10]
square, cube = createSQCubeList(lst)

print("Square List =", square)
print("Cube List =", cube)
