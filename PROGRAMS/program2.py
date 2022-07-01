'''
A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:
UP 5
DOWN 3
LEFT 3
RIGHT 2

The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer.
Example:
If the following tuples are given as input to the program:
UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be:
2'''
from math import sqrt as sq
#import math
x,y=0,0
while True:
    Inp=input("Enter your move Eg: UP 5 etc ")
    if(Inp==""):
        break
    li=Inp.split(" ")
    li[1]=int(li[1])
    if(li[0].upper()=="UP"):
        y+=li[1]
    elif(li[0].upper()=="DOWN"):
        y-=li[1]
    elif(li[0].upper()=="LEFT"):
        x+=li[1]
    elif(li[0].upper()=="RIGHT"):
        x-=li[1]
di=round(sq(x**2+y**2))
print(di)
