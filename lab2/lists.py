#1
my_list=["apple","cherry","banana"]
print(my_list)
#2
print(len(my_list))
#3
thislist=["banana",True, 13,"female"]
print(type(thislist))
#4
list1=list(("list","tuple","set"))
print(list1)
if "list" in list1:
    print("Yes")
#5
fruits=["kiwi","melon","watermelon","strawberry","mango","grapes"]
print(fruits[1])
print(fruits[2:5])
print(fruits[4:])
print(fruits[:5])
#6
list2=["kiwi","cherry","melon"]
list2[1:3]=["grapes"]
print(list2)
#7
list3=["cherry","pear","melon"]
list3.insert(2,"kiwi")
print(list3)
list3.append("orange")
print(list3)
#8
tropical=["papaya","mango"]
fruits=["melon","pear"]
fruits.extend(tropical)
print(fruits)
#9
def myfunc(n):
  return abs(n - 30)
list4= [100, 50, 65, 82, 23]
list4.sort(key = myfunc)
print(list4)
#10
classa=["Arman","Maks","Aruna"]
classb=classa.copy()
print(classb)
classC=classa[:]
print(classC)
#11
boys=["Alex","Arman","Murat"]
Girls=["Assyl","Guli","Tomiris"]
classa=boys+Girls
print(classa)
#12
for x in boys:
   Girls.append(x)
print(Girls)