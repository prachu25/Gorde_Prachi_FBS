# 1. Write a program to prompt user to enter userid and password. If Id and
#    password is incorrect give him chance to re-enter the credentials. Let him try 3
#    times. After that program to terminate.

user_id = "u101"
password = "admin123"

for i in range(1, 4):

    uid =input('Enter a User ID: ')
    pwd = input('Enter Password: ')

    if(uid == user_id  and pwd == password):
        print('Login Successful')
        break
    else:
        print("Incorrect User ID or Password")
        print("Try Again!\n")

        if(i == 3):
            print("Your Attempt are over.")
