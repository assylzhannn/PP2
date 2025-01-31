def my_func(fname, lname):
    print(fname + " "+ lname)
#my_func("Emil", "Any")

def my_func1(*kids):
    print("The youngest child is "+ kids[2])
#my_func1("Any","Some","One")

def kids(child1, child2, child3):
    print(child3+ " is youngest")
#kids(child2= "Thomas", child1= "Value", child3= "John")
def kwards(**kid):
    print("Last name is "+ kid["lname"])
#kwards(fname= "Tom", lname = "Jerry")

def default(country= "Sweden"):
    print("I am from "+ country)
#default("Kazakhstan")
#default()
def tri_recursion(k):
    if (k>0):
        result= k+ tri_recursion(k-1)
        print(result)
    else:
        result=0
    return result
print("The recursion results:")
tri_recursion(6)