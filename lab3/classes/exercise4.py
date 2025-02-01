"""#Write the definition of a Point class. Objects from this class should have a
a method show to display the coordinates of the point
a method move to change these coordinates
a method dist that computes the distance between 2 points"""
import math
import math

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Coordinates: ({self.x}, {self.y})")

    def move(self, x1, y1):
        self.x = x1
        self.y = y1

    def dist(self, point2):
        dx = self.x - point2.x
        dy = self.y - point2.y
        distance = math.sqrt(dx**2 + dy**2)
        return distance
x1=float(input("x:"))
y1=float(input("y:"))
point1 = Point(x1,y1)
point2 = Point(x1,y1)

point1.show() 
x2=float(input("x1:"))
y2=float(input("y1:"))
point1.move(x2,y2)
point1.show() 

distance = point1.dist(point2)
print(f"Distance between point1 and point2: {distance}")