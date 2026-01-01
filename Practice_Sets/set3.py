# class Stack:
#     def __init__(self):
#         self.top = -1
#         self.arr = [0]*100
    
#     def push(self, item):
#         self.top += 1
#         self.arr[self.top] = item
    
#     def pop(self):
#         if(self.top == -1):
#             print("Stack is Empty")
#             return
#         out = self.arr[self.top]
#         self.arr[self.top] = 0
#         self.top = self.top - 1
#         return out
    
#     def isEmpty(self):
#         if(self.top == -1):
#             return True
#         return False


class Notepad:
    def __init__(self):
        self.text = ""
        self.undo_stack = []
        self.redo_stack = []
    
    def write(self, new_text):
        self.undo_stack.append(self.text)
        self.text += new_text
        self.redo_stack.clear()
    
    def undo(self):
        if(self.undo_stack == []):
            print("Nothing to undo")
            return
        self.redo_stack.append(self.text)
        self.text = self.undo_stack.pop()
        print("Undo done")
        return
    
    def redo(self):
        if(self.redo_stack == []):
            print("Nothing to redo")
            return
        self.undo_stack.append(self.text)
        self.text = self.redo_stack.pop()
        print("Redo done")
        return
    
    def show(self):
        print(self.text)
        return
    

# def menu():
#     pad = Notepad()
#     while True:
#         print("\n1. Write Text")
#         print("2. Undo")
#         print("3. Redo")
#         print("4. ShowText")
#         print("5. Exit")
#         choice = input("Enter choice: ")
#         if choice =="1":
#             text = input("Enter text to write: ")
#             pad.write(text)
#         elif choice =="2":
#             pad.undo()
#         elif choice =="3":
#             pad.redo()
#         elif choice =="4":
#             pad.show()
#         elif choice =="5":
#             break
#         else:
#             print("Invalid choice. Try again.")

# menu()

def test () :
    pad = Notepad()
    pad. write ("Hello")
    pad. write ("World")
    pad.undo()
    pad. redo ()
    pad.show()
 # Run test
test()
