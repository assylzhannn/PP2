x=lambda a: a+10
print(x(5))

x= lambda a, b, c: a+b+c
print(x(2,3,4))

def myfunc(n):
    return lambda a: a*n
mydoubler = myfunc(2)
print(mydoubler(11))