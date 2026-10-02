# WAP to calculate total salary of employee based on basic, da=10% of basic, ta=12% of basic, hra=15% of basic.

basic = float(input('Enter Basic Salary: '))

da = basic * 0.10
ta = basic * 0.12
hra = basic * 0.15

# claulate the total salary
total_salary = basic + da + ta + hra


print("\n----- Salary Details -----")
print("Basic Salary :", basic)
print("DA (10%)     :", da)
print("TA (12%)     :", ta)
print("HRA (15%)    :", hra)
print("--------------------------")
print("Total Salary :", total_salary)
