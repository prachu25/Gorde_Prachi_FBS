# Write a program to check if person is eligible to marry or not (male age >=21 and female age>=18)

gender = input('Enter Your Gender(M/F): ').lower()

age = int(input('Enter a Your Age: '))

if(gender == 'm'):
    
    if(age >=21):
        print('male is Eligible for Marry')
    else:
        print('male is not eligible for marry')

elif gender == 'f':

    if(age >=18):
        print('female is Eligible for marry')
    else:
        print('female is not eligible for marry')

else:
    print('Invaild Gender..')
