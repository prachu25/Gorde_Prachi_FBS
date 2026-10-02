# Find the two numbers whose product is maximum among all pairs in a list. Use a Python set.

nums = [2, 3, 5, 7, -2, -10]

numbers = set(nums)

max_product = float('-inf')
pair = ()

for i in numbers:
    for j in numbers:
        if i != j:
            product = i * j

            if product > max_product:
                max_product = product
                pair = (i, j)

print("Pair:", pair)
print("Maximum product:", max_product)