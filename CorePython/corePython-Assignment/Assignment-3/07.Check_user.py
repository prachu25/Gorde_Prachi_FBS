# 07. Write a program to check if user has entered correct userid and password.

# stored a correct user_id and pssword
correct_user_id = "ud123"
correct_password = "pass@admin"

# take a input from user - id and pass
user_id = input('Enter a User_id: ')
user_pass = input('Enter a User_Password: ')

# check user enter a correct id and pass
if(user_id == correct_user_id):
    
    if(user_pass == correct_password):
        print('Login Successfully')
    else:
        print('Wrong Password !')
else:
    print('Invalid User id')



