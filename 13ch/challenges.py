#Challenge 1
#Create a Rectangle and Square class
#with a method called calculate_perimeter
#that calculated the perimeter of the
#shapes they represent.
# Create rectangle and square objects
#and call the method on both of them

class Square():
    def __init__(self,w):
        self.width = w

    def calculate_perimeter(self):
        return (self.width * 4)

    def change_size(self,n):
        self.width = self.width + n


class Rectangle():
    def __init__(self,w,l):
        self.width = w
        self.length = l
    
    def calculate_perimeter(self):
        return (self.width * 2) + (self.length * 2)

rectangle = Rectangle(3,4)
print(rectangle.calculate_perimeter())

square = Square(4,4)
print(square.calculate_perimeter)

#Challenge 2
#Define a method in your square class
#called change_size that allows you to
#pass in a number that increases or 
#descreases (if the number is negative)
#each side of a Square object by that number.

#def change_size(self,n):
#    self.width = self.width + n

#Challenge 3
#Create a class called Shape. Define
#a method in it called what_am_i that
#prints "I am a shape" when called.
#Change your Square and Rectangle
#classes from the previous challenges
#to inherit from Shape, create square
#and rectangle objects, and call the 
#new method on both of them.

class Shape():
    def __init__(self,w,l):
        self.width = w
        self.len = l


    def what_am_i(self):
        print("I am a shape")

class Rectangle(Shape):
    def __init__(self):
        pass

class Square(Shape):
    def __init__(self):
        pass
rectangle = Rectangle(60,69)
rectangle.what_am_i()

square = Square(13,13)
square.what_am_i()

#Challenge 4
#Create a class called Horse and a
#class called Rider. Use composition
#to model a horse that has a ride

class Horse():
    def __init__(self,breed,color,rider):
        self.rider = rider
        self.color = color
        self.breed = breed

class Rider():
    def __init__(self, rider):
        self.rider = rider

andrew = Rider("Andrew")

seabiscuit = Horse("Thorough Bred", "Black", andrew)