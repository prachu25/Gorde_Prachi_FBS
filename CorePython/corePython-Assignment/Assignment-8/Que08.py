# 11. WAP to check if a given number is Armstrong number or not. 
# For each task create separate functions.

def armstrong():

    num = int(input('Enter a number: '))
    dup = num 

    # count digit 
    count = 0
    temp = num

    while(temp > 0):
        count+=1
        temp = temp // 10


    # calculate Armstrong sum
    sum = 0
    temp = num
    while(temp > 0):
        digit = temp % 10
        sum = sum + (digit ** count)
        temp = temp //10


    # check
    if sum == dup:
        print("Armstrong Number")
    else:
        print("Not Armstrong Number")


# Function call
armstrong()