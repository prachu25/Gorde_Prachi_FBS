# calculate the simple intrest

# take the input
principal = float(input('Enter the principal: '))
time = float(input('Enter the Time (year): '))
rate = float(input('Enter the Rate (%): '))

# calculate simple intrest
simple_Intrest = ( principal * time * rate ) / 100

# Display the output
print(f'The simple Intrest is {simple_Intrest}')
