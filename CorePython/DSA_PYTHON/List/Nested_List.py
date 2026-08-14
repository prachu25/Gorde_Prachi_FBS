li = [10,20, [30, [40,50], 60] ,70, 80]

res = li[1]

res = li[2][1][1]  # print 50
res = li[2][0]     # print 30

res = li[2][2]     # print 60
res = li[3]        # print 70

res = li[::-1]     # reverse 

res = li[2][1][::-1]   #reverse list [40,50]

    


print(res)