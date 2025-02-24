import re
with open("PP2/lab5/row.txt","r", encoding="utf-8") as f:
    data = f.read()
mathes=re.findall("а.*б",data)
print(mathes)