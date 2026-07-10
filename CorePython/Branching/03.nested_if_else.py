gender = input('Enter your Gender(M/F): ')
age = int(input('Enter Your Age: '))

if(gender == 'F'):
    if(age >= 18):
        print('Female is Eligible for Marriage')
    else:
        print('Female is Not Eligible')
else:
    if(age >= 21):
        print('Male is Eligible For Marriage')
    else:
        print('Male is Not Eligible')
        