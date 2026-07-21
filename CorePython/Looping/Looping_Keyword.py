# 1. Pass: to neglect the expected indentation error
for i in range(1,10):
    pass


# 2. break: to terminate the loop
for j in range(1,10):
    if(j == 4):
        break
    print(j)
print()


# 3. continue : to stop the current iteration
for k in range(1,6):
    if(k == 3):
        continue
    print(k)
print()

# 4. else: else block is exceute when the above all condition are false
for x in range(1,6):
    if(x == 4):
        continue
    print(x)
else:
    print("For loop excuted successfully...")