#Find the Second Max Element
li = [45,34,81,77,53,34,26,82]

max = 0
second_max = 0

for i in range(len(li)):

    if(li[i] > max):
        second_max = max
        max = li[i]
    else:
        if(second_max > li[i] and second_max != max):
            second_max = li[i]


print("Second Max = ", second_max)