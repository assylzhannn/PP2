dict1 = {
  "laptop": "Lenove",
  "user": "Assylzhan",
  "year": 2020
}
if "user" in dict1:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")
#2
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})
#3
calendar = {
  "year": 2025,
  "month": "January"
}
calendar["day"]= 24
print(calendar)
calendar.update({"time": "18:55"})
print(calendar)
#4
calendar.pop("month")
print(calendar)
calendar.popitem()
print(calendar)
calendar.clear()
print(calendar)
#5
calendar = {
  "year": 2025,
  "month": "January"
}
for x in calendar:
  print(x) #print key
for x in calendar:
  print(calendar[x]) #print values
for x, y in calendar.items():
  print(x, y)
#6 copy
calendar = {
  "year": 2025,
  "month": "January"
}
data=calendar.copy()
print(data)
data2=dict(calendar)
print(data2)
#7 nested loop
mother = {
  "name" : "Anna",
  "year" : 1978
}
father = {
  "name" : "Tobias",
  "year" : 1977
}
child = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "mom" : mother,
  "dad" : father,
  "child1" : child
}
print(myfamily)
print(myfamily["child1"]["name"])
#8
for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])

   
