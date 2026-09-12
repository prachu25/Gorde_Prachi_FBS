start = int(input('Enter a num: '))
end = int(input('Enter end : '))

lst_odd = [o**2 for o in range(start,end) if o % 2 == 1]
print(lst_odd)

