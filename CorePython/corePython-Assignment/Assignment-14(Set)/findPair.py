# Write a Python program to find all pairs of elements in a list whose sum is equal to a given value.

nums = [2, 4, 3, 5, 7, 8, 1]
target = 9


for i in range(len(nums)):

    for j in range(i+1, len(nums)):

        if(nums[i] + nums[j] == target):
            print("Pair", nums[i], "+" ,nums[j], "==" ,target)