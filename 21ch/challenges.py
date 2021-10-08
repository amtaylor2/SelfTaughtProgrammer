#Challenge 1
#Reverse the string "yesterday" using a stack


class Stack:
    def __init__(self):
        self.items = []
 
    def is_empty(self):
        return self.items == []
 
    def push(self, item):
        self.items.append(item)
 
    def pop(self):
        return self.items.pop()
 
    def peek(self):
        last = len(self.items)-1
        return self.items[last]
 
    def size(self):
        return len(self.items)
 
stack = Stack()
for c in "yesterday":
    stack.push(c)

#Challenge 2
#Use a stack to create a new list with
#the itemsw in the list reversed
#[1,2,3,4,5]