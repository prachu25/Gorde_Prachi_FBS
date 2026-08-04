# 5. Accept a number from user and check if this element is present in 
#    the list or not. Also tell how many times it is present in the list.

lst = [12, 45, 78, 23, 45, 90, 12, 67, 45, 89, 34, 12, 56, 90, 23]

print('Enter the number to check this Element is present in the list or not')
num = int(input('Enter Element: '))

count = 0

for i in range(len(lst)):
    if(lst[i] == num):
       count+=1

if count > 0:
    print("Element Found!")
    print("Element is appear", count, "times.")
else:
    print("Element Not FOund!")

