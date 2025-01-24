a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
#2 short hand if
a=5
b=45
if a>b : print("a is greater than b")
#3 short hand if .. else
print("A") if a>b else print("B")
#4 with 3 conditions
a=12
b=12
print("A") if a>b else print("B") if a<b else print("=")
#5 and\ or
a=230
b=345
c=230
if b>a and c>a:
  print("Both conditions are true")
elif b>a or c>a:
  print("At least one of the conditions is true")

#6 nested if
x=36
if x>20:
  print("Above 20,")
  if x>30:
    print("and,above 30")
  else:
    print("but under 30")

#7 pass
a=10
b=5
if a>b:
  pass