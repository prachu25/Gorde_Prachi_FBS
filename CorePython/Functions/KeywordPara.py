#1. TO neglect position prameter
#2. Assign value to the paramtere in function call
#3. flow from right to left
#4. name of parameter in functin call and function defination should be same
#5. if you wnat to pass parametre to randomly to function then use combination of default parametre and keyword parameter

def employe(id, name, sal, dept='Finance'):
    data = 'ID: ' + str(id)   +  '\n'
    data += 'NAME: ' + str(name)  +  '\n'
    data += 'SALARY: ' +  str(sal) +  '\n'
    data += 'DEPARTMENT: ' +  str(dept) +  '\n'

    return data

# flowing sequence
res = employe(101,'RAJ',20000,'HR')
print(res)

# Not flowing sequence -> use keyword to assign value
s1 = employe(name ='SUJAL', dept='Finance', sal= 80000, id=3002) 
s2 = employe(name ='RAHUL', sal= 80000, id=3001) 
print(s1)
print(s2)



