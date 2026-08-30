# Python Program to Form a New String where the First Character and the Last Character have been Exchanged
def exchange_first_last(string):

    new_str = ""

    for i in range(len(string)):

        if i == 0:
            new_str = new_str + string[len(string) - 1]

        elif i == len(string) - 1:
            new_str = new_str + string[0]

        else:
            new_str = new_str + string[i]

    return new_str


s = "Python"
res = exchange_first_last(s)
print("Orignal String =", s)
print("New String =", res)