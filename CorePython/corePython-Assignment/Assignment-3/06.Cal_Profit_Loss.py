# 06. Write a program to calculate profit or loss.

cost_price = int(input('Enter a Cost Price: '))
selling_price = int(input('Enter a Selling Price: '))

if selling_price > cost_price:
    profit = selling_price - cost_price
    print('Profit', profit)

elif cost_price > selling_price:
    loss = cost_price - selling_price
    print('Loss', loss)

else:
    print('Neither Profit and Loss')