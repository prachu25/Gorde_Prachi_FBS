import re 

data = "I am Rohit Sharama my age is 5312"

r = re.findall(r"\d", data)  # it print digit

r1 = re.findall(r"\D", data)  # it print all except the digits

r2 = re.findall(r"\w", data)

r3 = re.findall(r"\W", data)

r4 = re.findall(r"[0-9]{3}", data)  # {3}  it print exact 3  digits

print(r)
print(r1)
print()
print(r2)

print()

print(r4)



















# github check
# project one cui, gui
# 





# r is use for raw string 