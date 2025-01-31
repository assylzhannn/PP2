"""Write a program to solve a classic puzzle: 
We count 35 heads and 94 legs among the chickens and rabbits in a farm. 
How many rabbits and how many chickens do we have? 
create function: solve(numheads, numlegs):"""

def solve(numheads, numleags):
    #x+y=numheads 4x+2y=numlegs x=rabbits, y=chickens
    x = (numleags - (2* numheads))/2
    y = numheads - x
    return f" chicken {y}, rabbits {x}"
#numheads = int(input("number of heads:"))
#numleags = int(input("number of legs:"))
print(solve(35, 94))
