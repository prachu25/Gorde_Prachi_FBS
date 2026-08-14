li = [10,20,30,40,50,60,70,80,90,100]

res = li[1:5]   # strat index 1 and end index 5
res = li[4:9]

res = li[1:8:2]   # print index 1 to 8 with +2

res = li[:5]     # if we print from first index then dont need to metion the 0
res = li[5:]     # if we  want to print upto end list then dont need to mnetion last index

res = li[:]      # print the whole list
res = li[::]     # print the whole list

res = li[::-1]   # print the reverse list 

res = li[4::-1]   # start index from 4 and take reverse upto 0   [50, 40, 30, 20, 10]
res =li[:4:-1]


res =li[:-1]


print(res)