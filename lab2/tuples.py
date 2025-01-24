tuple1=("banana","apple","apple")
print(len(tuple1))
print(type(tuple1))
#2
tuple2=("abc",40,False,"female")
print(tuple2)
#3
tuple3=tuple(("banana","kymyz","et","bal","kampot"))
print(tuple3)
print(tuple3[0])
print(tuple3[2:4])
print(tuple3[:3])
print(tuple3[-4:-1])
if "bal" in tuple3:
    print("Yes")
#4
tuple1=("et","nan","mai")
x=list(tuple1)
x.append("milk")
tuple1=tuple(x)
print(tuple1)
#5
tuple1=("nan","syt")
tuple2=("bread",)
tuple1 += tuple2
print(tuple1)
#6 unpack tuples
fruits=("apple","pineapple","kiwi")
(red,yellow,green)=fruits
print(red)
print(yellow)
print(green)

signs=("a",1,2,3)
(letter,*number)=signs
print(letter)
print(number)
#7loop tuples
san=(1,2,3,4)
for x in range(len(san)):
    print(san[x])

i=0
while i<len(san):
    print(san[i])
    i+=1
#8 join tuples
letter=("a","b","c")
num=(1,2,3)
signs=letter+num
print(signs)

fruits=("peach","apple","pear")
my_fruits=fruits * 2
print(my_fruits)