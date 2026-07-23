num = 1
while(num <= 100):

    count = 0

    i = 1
    while(i <= num):

        if(num % i == 0):     # count exactly divide number
            count+=1

        i+=1
    
    if(count == 2):
        print("Prime Number: ", num)
    
    num+=1
        

        