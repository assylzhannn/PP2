class Person:
    def __init__(self,name,age):
        self.name= name
        self.age= age
    def __str__(self):
        return f"{self.name}{self.age}"
    def myfunc(self):
        print("Hello my name is "+ self.name) 
p1 = Person("John", 36)
p1.age= 40
p1.myfunc()
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)