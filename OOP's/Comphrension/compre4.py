# s = math.sqrt(25)
# print(s)

start = int(input("Enter a Start number: "))
end_num = int(input("Enter a end Number: "))

sq_root = [x**0.5 for x in range(start,end_num)]

print(sq_root)

