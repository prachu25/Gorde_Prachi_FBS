passenger = int(input('Enter number of passengers: '))
ticketCost = float(input('Enter Ticket Cost: '))

totalAmount = 0
i= 1
while(i<=passenger):

    age = int(input(f"Enter a age of passenger {i} : "))

    # child below 12
    if(age < 12):
        amount = ticketCost - (ticketCost * 30/100)

    # senior citizen above 59
    elif(age > 59):
        amount = ticketCost - (ticketCost * 50/100)
    else:
        amount = ticketCost
    
    totalAmount  = totalAmount + amount

    i+=1

print('Total Ticket Amount =', totalAmount)
    