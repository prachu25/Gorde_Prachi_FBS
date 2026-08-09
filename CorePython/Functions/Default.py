
# DEFAULT PARAMETER
def emp(id, name=None, sal=25000, dept='HR'):
    print('ID:', id)
    print('NAME:', name)
    print('SALARY',sal)
    print('DEPARTMENT', dept)       # if user not pass value then it take  default value


emp(101, 'joe',23000, 'SALES')
print()
emp(102,'Rishi')
print(  )
emp(103)


