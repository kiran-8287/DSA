class Stack:
    def __init__(self):
        self.data = []
    def push(self,val):
        self.data.append(val)
    def pop(self):
        if(len(self.data) == 0):
            return None
        return self.data.pop()
    def empty(self):
        if(len(self.data) == 0):
            return True
        return False
    def top(self):
        if(len(self.data) == 0):
            return None
        return self.data[-1]

class QueueUsingStack:

    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def enqueue(self,val):
        if(self.s2.empty()):
            self.s2.push(val)
        else:
            while(self.s2.empty() == False):
                self.s1.push(self.s2.pop())
            self.s1.push(val)
   
    def dequeue(self):
        if(self.s1.empty() and self.s2.empty()):
            return None
        elif(self.s1.empty() == True and self.s2.empty() == False):
            return self.s2.pop()
        else:
            while(self.s1.empty() == False):
                self.s2.push(self.s1.pop())
            return self.s2.pop()
    
    def empty(self):
        if(self.s1.empty() and self.s2.empty()):
            return True
        return False
    
    def front(self):
        if(self.s1.empty() and self.s2.empty()):
            return None
        elif(self.s1.empty() == True):
            return self.s2.top()
        while(self.s1.empty() == False):
            self.s2.push(self.s1.pop())
        return self.s2.top()
    

# Queue using Stack
q = QueueUsingStack()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print(q.dequeue())  
print(q.front())    

class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, x):
        self.data.append(x)   # add at end

    def dequeue(self):
        if self.empty():
            return None
        return self.data.pop(0)  # remove from front

    def front(self):
        if self.empty():
            return None
        return self.data[0]

    def empty(self):
        return len(self.data) == 0

    def size(self):
        return len(self.data)

class StackUsingQueue:
    def __init__(self):
        self.q = Queue()
    
    def push(self,val):
        self.q.enqueue(val)
        for i in range(self.q.size() - 1):
            self.q.enqueue(self.q.dequeue())
    
    def pop(self):
        if(self.q.empty()):
            return None
        return self.q.dequeue()
    
    def top(self):
        return self.q.front()
    
    def size(self):
        return self.q.size()
    
s = StackUsingQueue()
s.push(10)
s.push(20)
s.push(30)
print(s.pop())  # 30
print(s.top())  # 20
