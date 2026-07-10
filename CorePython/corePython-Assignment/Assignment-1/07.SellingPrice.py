# WAP to calculate selling price of book based on cost price and discount.

cost_price = float(input('Enter a cost Price: '))
discount = float(input('Enter a Discount: '))

# find the discount 
discount_amount = (cost_price * discount ) / 100

# calculate the selling price
selling_price = cost_price - discount_amount

print('Selling Price is: ', selling_price)
