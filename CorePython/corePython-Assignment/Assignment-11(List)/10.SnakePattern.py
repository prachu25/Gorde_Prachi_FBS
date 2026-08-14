# 8. Print 1 to 100 in snakes and ladder pattern.

def print_pattern(n):

    num = 1

    for i in range(n):

        row = []

        for j in range(n):
            row.append(num)
            num +=1

        if i % 2 != 0:
            row.reverse()
            
        print(*row)

print_pattern(10)

"""
i = 0 → even → normal
i = 1 → odd  → reverse
i = 2 → even → normal
i = 3 → odd  → reverse


output = 
1 2 3 4 5 6 7 8 9 10             0  even- normal print
20 19 18 17 16 15 14 13 12 11    1  odd - reverse print
21 22 23 24 25 26 27 28 29 30    2  even- normal print
40 39 38 37 36 35 34 33 32 31    3  odd - reverse print
41 42 43 44 45 46 47 48 49 50    4  even- normal print
60 59 58 57 56 55 54 53 52 51    ...
61 62 63 64 65 66 67 68 69 70
80 79 78 77 76 75 74 73 72 71
81 82 83 84 85 86 87 88 89 90
100 99 98 97 96 95 94 93 92 91

"""