num = int(input('Enter a number: '))
original =num

# count digit
temp = num
count =0 

# calulating how many digits 
while temp > 0:        
    count+=1
    temp = temp // 10


# Armstrong calculation
sum = 0

while num > 0:
    last_digit = num % 10
    sum = sum + (last_digit ** count)   # ** -> power
    num = num // 10

print("OutPut SUM:", sum)

if sum == original:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")
