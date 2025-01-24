student={
    "name": "Assel",
    "major": "IS"
}
print(student)
print(student["major"])
#2
student={
    "school": "SITE",
    "year": "2024",
    "year": "2026"
}
print(student)
print(len(student))
print(type(student))
#3
dic1={
    "bool": False,
    "int": 123,
    "colors": ["red","yellow"]
}
print(dic1)
#4
thisdict= dict(name = "Ayagoz", age= 18 )
print(thisdict)
#5
thisdict = {
  "color": "red",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["color"]
y=thisdict.get("color")
print(x,y)
#6
z=thisdict.keys()
print(z)
thisdict["color"]= "yellow"
print(z)
#7
v=thisdict.values()
print(v)
thisdict["color"]= "blue"
print(v)
#8
x=thisdict.items()
print(x)
