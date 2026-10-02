# Find all unique combinations of 3 numbers from a given list whose sum equals a target.

nums = [1, 2, 3, 4, 5, 6]
target = 9

result = set()

for i in range(len(nums)):

    for j in range(i + 1, len(nums)):
        
        for k in range(j + 1, len(nums)):

            if nums[i] + nums[j] + nums[k] == target:
                combination = (nums[i], nums[j], nums[k])
                result.add(combination)

for combination in result:
    print(combination)