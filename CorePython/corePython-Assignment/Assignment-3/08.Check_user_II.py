"""
08. Write a program to prompt user to enter userid and password. After verifying userid and password display 
    a 4 digit random number and ask user to enter the same. If user enters the same number then show him
    success message otherwise failed. (Something like captcha)
"""
import random

# stored a correct user_id and pssword
correct_user_id = "ud123"
correct_password = "pass@admin"

# take a input from user - id and pass
user_id = input('Enter a User_id: ')
user_pass = input('Enter a User_Password: ')

if user_id == correct_user_id and user_pass == correct_password:
    
    captcha = random.randint(1000,9999)
    print('Captcha', captcha)

    user_captcha = int(input('Enter a Captcha: '))
    
    # check Captcha
    if user_captcha == captcha:
        print('Verification Successfully')
    else:
        print('Failed!')

else:
    print('Invalid User and Password Try Again!')
