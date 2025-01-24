#1 A set is a collection which is unordered, unchangeable*, and unindexed.
thisset={"apple","pear","apple","cherry"}
print(thisset)
#2 0=false 1=true
thisset={"apple",False,2,0,1,"pineapple",True}
print(thisset)
print(len(thisset))
print(type(thisset))
#3 the set() constructor
set1=set(("pineapple","pen","apple"))
print(set1)
print("banana" in set1)
print("pear" not in set1)
#4 add set items
fruits={"melon","mango"}
fruits.add("blueberry")
print(fruits)
list1=["watermelon","pear"]
fruits.update(list1)
print(fruits)
#5 remove set item
set2={"milk","butter","bread"}
set2.remove("milk")
print(set2)
set2.discard("milk")#not raise an error if item doesn't exist
print(set2)
#6
set1={"apple","pear","peach"}
x=set1.pop()
print(x)
print(set1)
set1.clear()
print(set1)
del set1 #delete a set completely
#7
set1={"fantastic","cocacolastik"}
for x in set1:
    print(x)
#8 join sets
set1={"k","l","m"}
set2={4,5,6}
set3=set1.union(set2)
print(set3)
set4= set1 | set2 #same as union()
print(set4)
#9
set1={"a","b","c"}
set2={"Aset","Berik"}
set3={1,2,3,4}
set4=set1.union(set2, set3)
print(set4)
myset= set1| set2| set3
print(myset)
#10
x={"d","f","g"}
y=(1,2,3)
z=x.union(y)
print(z)
#11
set1={"a","b","c","e","a"}
set2={"c","f","e","a"}
set3=set1.intersection(set2)
print(set3)
set3=set1 & set2 # & same intersection()
print(set3)
#12
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.intersection_update(set2)
print(set1)
#13
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2) #same as " - "
print(set3)
#14
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2) #same as " ^ "
print(set3)