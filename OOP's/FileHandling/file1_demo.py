# FILE READING 

file = open("Myfile.txt",'r')

content = file.read()
print(content)

file.close



"""

read()       → reads whole file as one string
readline()   → reads only one  line
readlines()  → reads all lines as a list 
                -> it will print like this ['i love java langauge more than python\n', 'i have strong skill and foundation in java ']

"""