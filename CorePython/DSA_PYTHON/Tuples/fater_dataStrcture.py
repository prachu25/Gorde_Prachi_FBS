import sys

tup = (10, 20, 30)
li = [10, 20, 30]

print(sys.getsizeof(tup))  # it take 64 size, so it execute faster 
print(sys.getsizeof(li))   # it take 88 size

# Tuple is faster than list  , bcz its is immutable
