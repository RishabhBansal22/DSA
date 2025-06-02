class Stack:


    def __init__(self):
        self.stack = []
    

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        if self.stack != 0:
            self.stack.pop()
        else:
            return "The Stack is empty"
        
    def peek(self):
        if self.stack != 0:
            return  self.stack[len(self.stack)-1]
        else:
            return "The Stack is empty"
        
    def search(self,val):
        if val not in self.stack:
            return -1
        else:
            return self.stack.index(val)
        
    def is_empty(self):
        return True if len(self.stack) == 0 else False 
    
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, val):
        self.queue.append(val)

    def dequeue(self):

        if self.queue:
           popped = self.queue.pop(0)
           return popped
        else:
            return "The Queue is Empty"
        
    def peek(self):

        if self.queue:
           return self.queue[0]
        else:
            return "The Queue is Empty"
        
    def is_empty(self):
        return True if len(self.queue) == 0 else False 
    

        


    

    
  


