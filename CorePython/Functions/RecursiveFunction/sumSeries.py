def sumSeries(n):

    if(n > 0):
        return n + sumSeries(n-1)
    else:
        return 0


  
call = sumSeries(4)
print("sum: ",call)