#9Write a function that computes the volume of a sphere given its radius.
import math
x=math.pi
def volume(rad):
    v = (4/3)* x* rad**3
    print(v)
rad=float(input("radius: "))
volume(rad)