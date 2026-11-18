import re

text = "Rohit Sharma was born on 30/04/1987."

dates = re.findall(r'\d{2}/\d{2}/\d{4}', text)

print(dates)