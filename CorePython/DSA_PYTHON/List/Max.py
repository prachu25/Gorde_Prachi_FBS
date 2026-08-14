# WAP TO fins the maximum Element in List
li = [45,34,81,77,53,34,26,82]

max = 0

for i in range(len(li)):
    if(li[i] > max):
        max = li[i]

print("Maximum = ",max)