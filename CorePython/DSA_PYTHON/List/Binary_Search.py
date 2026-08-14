# BINARY Search 
def binarySearch(lst , target):

    low = 0
    high = len(lst)-1
    
    while(low <= high):

        mid = (low + high)//2
        
        if(lst[mid] == target): 
            return True
        elif(target > lst[mid]):
            low = mid + 1
        else:
            high = mid -1

    else:
        return -1   # Not Found

    

lst = [10,20,30,40,50,60]
target = 45
res = binarySearch(lst,target)

if(res != -1):
    print("Element Found")
else:
    print("Element Not Found")


        
