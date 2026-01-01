# class CircularQueue():
#     def __init__(self):
#         self.size = 5
#         self.front = -1
#         self.rear = -1
#         self.queue = [None] * self.size
    
#     def isFull(self):
#         if((self.front == 0 and self.rear == self.size-1) or ((self.rear + 1)%self.size == self.front)):
#             return True
#         else:
#             return False
    
#     def isEmpty(self):
#         if(self.front == -1):
#             return True
#         else:
#             return False
    
#     def enQueue(self,element):
#         if(self.isFull()):
#             print("Queue is Full")
#             return
#         elif(self.isEmpty()):
#             self.front = 0
#         self.rear = (self.rear + 1)%self.size
#         self.queue[self.rear] = element
#         print(f"Insereted {element}")

#     def deQueue(self):
#         if(self.isEmpty()):
#             print("Queue is Empty")
#             return -1
#         else:
#             temp = self.queue[self.front]
#         if self.front == self.rear:  # only one element
#             self.front = -1
#             self.rear = -1
#         else:
#             self.front = (self.front + 1) % self.size
#         return temp

    
#     def display(self):
#         if self.isEmpty():
#             print("Empty Queue")
#             return

#         i = self.front
#         while True:
#             print(self.queue[i])
#             if i == self.rear:
#                 break
#             i = (i + 1) % self.size

        
# def test():
#     mQ = CircularQueue()
#     mQ.deQueue()
#     mQ.enQueue(1)
#     mQ.enQueue(2)
#     mQ.enQueue(3)
#     mQ.enQueue(4)
#     mQ.enQueue(5)
#     mQ.display()
#     x = mQ.deQueue()
#     y = mQ.deQueue()
#     print(x)
#     print(y)
#     mQ.display()

# test()

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
    
    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
    
    def pop(self):
        if(self.top == None):
            print("Stack is Empty")
            return
        temp = self.top
        self.top = temp.next
        temp.next = None
        return temp.data
    def peek(self):
        return self.top.data
    def isEmpty(self):
        if(self.top == None):
            return True
        return False
    
def isBalanced(expression):
    s = Stack()
    brackets = {
        "(":")" , "[":"]" , "{":"}"
    }
    for char in expression:
        if(char == "("  or char == "[" or char == "{"):
            s.push(char)
        elif(char == ")" or char == "]" or char == "}"):
            if(s.isEmpty()):
                return False
            else:
                open = s.pop()
                if(brackets[open] != char):
                    return False
    
    if(s.isEmpty):
        return True
    return False

def test():
    expressions = ["a+b",  "[a*(b+c) ]" , "{[()]}" , "([)]" , "((())"]
    for exp in expressions:
        if(isBalanced(exp)):
            print(exp, ":Balanced")
        else:
            print(exp, ":Not Balanced")

test()


