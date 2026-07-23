# WAP to print Armstrong number within a given range
start = int(input('Enter the strting number: '))
end = int(input('Enter the ending number: '))


for num in range(start, end+1):

    original = num

    # count digit
    temp =num
    count =0

    while(temp > 0):
        count+=1
        temp = temp // 10

    sum = 0
    temp = num

    while(temp > 0):
        last_digit = temp % 10
        sum = sum + (last_digit ** count)
        temp = temp // 10

    if(sum == original):
        print("Armstrong Number:", original)



