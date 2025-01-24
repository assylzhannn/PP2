list1=["banana","apple","pear"]
list1.remove("banana")
print(list1)
#2
list2=["cherry","mango","melon","apple","banana"]
list2.pop(1)
print(list2)
#3
del list2[2]
print(list2)
del list2
#4
my_list=["bird","dog","cat"]
my_list.clear()
print(my_list)
#5
my_list=["bread","milk","sheese"]
for x in my_list:
    print(x)
#6
my_list=["bread","milk","sheese"]
[print(x) for x in my_list]
#7
list2=["banana", "cherry","mango","orange"]
new_list=[]
for x in list2:
    if "a" in x:
        new_list.append(x)
print(new_list)
#8
new_list=[x for x in range(10)]
print(new_list)
#9
new_list=["hello" for x in list2]
print(new_list)
#10
fruits=["mango","banana","apple","pineapple"]
fruits.sort()
print(fruits)
#11
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)