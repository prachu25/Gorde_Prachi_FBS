#1. Structure: denoted by by ()
tup = (10,20,30,40)
tup = (10,)         # if only metion (10)  its show <int> type so ,


#2. Type of Data: Hetrogeneous
tup = (10, 3.14, "abc")
print(tup)
print(type(tup))


#3. Sequence: ordered
tup = (1, 2, 3, 4, 5, 6)
print(tup)
print(type(tup))

#4. Changable: Immutable
# tup[0] = 30               # TypeError: 'tuple' object does not support item assignment

#5. Duplication:  Allowed
tup = (10,20,10,10,30)
print(tup)
print(type(tup))
