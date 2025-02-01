#Define a class which has at least two methods: getString: to get a string from console input 
#printString: to print the string in upper case.
class String():
    def getString(self):
        self.sen=input("sentence:")

    def printString(self):
        print(self.sen.upper())
myString= String()
myString.getString()
myString.printString()