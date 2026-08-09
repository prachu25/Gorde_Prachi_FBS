#1. to pass multiple value with meaning to function
#2. Mention 2 astrick symbols before parameter name in function defination
#3. data stored in dict formate
#4. Use for loop on dict.items() to access individually.

def emp(**data):
    for key, value in data.items():
        print(key, '=' , value)


emp(id=101, name = 'Rishi', age = 23, gender ='male', city='Nagpur', dep = 'Finance')