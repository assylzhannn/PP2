def squared(a,b):
    for i in range(a,b):
        yield(i*i)
a=int(input("a: "))
b=int(input("b: "))
#print(list(squared(a,b)))
squared_num= squared(a,b)
for num in squared_num:
    print(num)