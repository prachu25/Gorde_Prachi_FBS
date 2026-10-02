words = ["flower", "flow", "flight"]

words.sort()

first = words[0]
last = words[-1]

prefix = ""

for i in range(min(len(first), len(last))):

    if first[i] == last[i]:
        prefix += first[i]
    else:
        break

print(prefix)




# print(words)