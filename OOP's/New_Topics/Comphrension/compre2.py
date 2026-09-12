
lst1 = [1,2,3,4,5,6,7,8,9]

lst2 = [x**2 for x in lst1]
print(lst2)

lst_even = [e for e in lst1 if e % 2 == 0]
print(lst_even)


lst_odd = [o for o in lst1 if o % 2 == 1]
print(lst_odd)