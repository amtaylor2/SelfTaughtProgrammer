#Challenge 1
#Add a square_list class variable to a class
#called Square so that everytime you create
#a new Square object, the new object gets
#added to the list

class Square():
    square_list = []

    def __init__(self,w,l):
        self.width = w
        self.len = l
        self.square_list.append(self.width,self.len)


#Challenge 2
#Change the Square class so that when
#you print a Square object, a message
#prints telling you the len of each
#of the four sides of the shape.
#For example, if you create a square
#with Sqaure(29) and print it, Python
#should print 29 by 29 by 29 by 29

    def print_size(self):
        print("""{} by {} by {} by {} """.format(self.width,self.len,self.width,self.len))

#Challenge 3
#Write a function that takes two objects
#as parameters and returns True if they
#are the same, and False if they are not

def obj_true_or_fasle(obj1,obj2):
    print(obj1 is obj2)
