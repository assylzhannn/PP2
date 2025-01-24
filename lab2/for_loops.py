names={"Askar","Daulet","Aya"}
for x in names:
    print(x)
#2
for x in "Assylzhan":
    print(x)
#3
fruits=["apple","banana","cherry"]
for x in fruits:
    if x== "banana":
        continue
    if x == "cherry":
        break
    print(x)
#4 range
for x in range(3):
    print(x)
for x in range(2,8,2):
    print(x)
#5 else in for loop
for x in range(5):
    print(x)
else:
    print("finish")

#6 inner loop
fruits=["apple","cherry","pear"]
kg=[3,5]
for x in fruits:
    for y in kg:
        print(x,y)

#7 pass
fruits=["apple","banana"]
for x in fruits:
    pass