num= int(input('Enter a number: '))

if(num > 1):
    for i in range(2,num):

        if(num%i == 0):
           print(f'{num} is Not prime number')
           break
    else:
        print(f'{num} is a prime number')
        
elif(num == 0):
    print('Neither prime not composite') 
else:
    print('Not a prime number')




# Optimized code 
"""
if(num > 1):
    for i in range(2,num // 2 + 1):    # its checking half value

        if(num%i == 0):
           print(f'{num} is Not prime number')
           break
    else:
        print(f'{num} is a prime number')
    
else:
    print('Not a prime number')

  """
  

