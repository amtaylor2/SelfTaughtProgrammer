#Challenges
#Challenge 1
#Define a class called Apple with four
#instance variables that represent four attributes
#of an apple

class Apple:
    def __init__(self,c,t,s,w):
        self.color = c
        self.type = t
        self.size = s
        self.weight = w

#Challenge 2
#Create a circle class with a method
#called area that calculates and 
#returns its area.
#Then create a circle object, call area 
#on it, and print the result. Use python's
#pi function in the built-in Math Module

class Circle:
    def __init__(self,r):
        self.radius = r

def area(self):
    return self.radius * Math.pi

circle = Circle(10)
print(circle.area())

#Challenge 3
#Create a triangle class with a method
#called area that calculates and returns
#its area.
#Then create a triangle object, call area
#on it, and print the result.

class Triangle:
    def __init__(self,b,h):
        self.base = b
        self.height = h

def area(self):
    return (self.base * self.height) / 2

triangle = Triangle(5,10)
print(triangle.area())

#Challenge 4
#Make a hexagon class with a method called
#calculate_perimeter that calulates and
#returns its perimeter.
#Then create a Hexagon object, call
#calculate_perimeter on it, and print the 
#result

class Hexagon:
    def __init__(self,s):
        self.side = s

def calculate_perimeter(self):
    return self.side * 6

hexagon = Hexagon(5)
print(hexgon.calculate_perimeter)