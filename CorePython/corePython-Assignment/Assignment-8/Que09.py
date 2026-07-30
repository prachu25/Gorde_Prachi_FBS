# 10. Write a program to check if entered year is a leap year or not.
"""
A Leap Year is a year that has 366 days instead of 365 days. 
It has 29 days in February instead of 28.

Rules to Calculate a Leap Year
1. divisible by 400 → Leap Year
2. divisible by 100 →  Not a Leap Year
3. divisible by 4 → Leap Year
Otherwise →  Not a Leap Year

"""

def leaf_year():
    year = int(input('Enter e year: '))

    if(year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)):
        print('Leaf Year')
    else:
        print('Not Leaf Year')


# Function call
leaf_year()