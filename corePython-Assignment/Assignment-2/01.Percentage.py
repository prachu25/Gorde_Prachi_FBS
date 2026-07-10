# 1. Write a program to calculate the percentage of student based on marks of any 5

m1 = int(input('Enter a subject one mark: '))
m2 = int(input('Enter a subject second mark: '))
m3 = int(input('Enter a subject third mark: '))
m4 = int(input('Enter a subject fourth mark: '))
m5 = int(input('Enter a subject five mark: '))

total = m1 + m2 + m3 + m3 + m4
percentage = total/5

print('The Total mark: ',total)
print('Persentage: ',percentage)
