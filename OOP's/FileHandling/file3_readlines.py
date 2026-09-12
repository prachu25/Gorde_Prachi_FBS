
# FILE READ by readlines

file = open("Myfile.txt",'r')
d = file.readlines()
print(d)

file.close()



"""
readlines()  → reads all lines as a list 
            -> it will print like this ['i love java langauge more than python\n', 'i have strong skill and foundation in java ']
                
                """