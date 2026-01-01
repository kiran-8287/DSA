
#2
class Node:
    def __init__(self,id,title,edition):
        self.id = id
        self.title = title
        self.edition = edition
        self.height = 1
        self.left = None
        self.right = None

class AVLTree:
    def __init__(self):
        self.root = None
    
    def minValueNode(self,node):
        curr = node
        while(curr.left != None):
            curr = curr.left
        return curr
    
    def get_height(self,node):
        if(node == None):
            return 0
        return node.height
    
    def get_balance(self,node):
        if(node == None):
            return 0
        return self.get_height(node.left) - self.get_height(node.right)
    
    def rightRotate(self,node):
        temp = node.left
        child = temp.right
        node.left = child
        temp.right = node
        node.height = 1 + max(self.get_height(node.left),self.get_height(node.right))
        temp.height = 1 + max(self.get_height(temp.left),self.get_height(temp.right))
        return temp
    
    def leftRotate(self,node):
        temp = node.right
        child = temp.left
        node.right = child
        temp.left = node
        node.height = 1 + max(self.get_height(node.left),self.get_height(node.right))
        temp.height = 1 + max(self.get_height(temp.left),self.get_height(temp.right))
        return temp

    def insert(self,root,id,title,edition):
        if(root == None):
            return Node(id,title,edition)

        #search
        if(id < root.id):
            root.left = self.insert(root.left,id,title,edition)
        elif(id > root.id):
            root.right = self.insert(root.right, id, title,edition)
        
        root.height = 1 + max(self.get_height(root.left),self.get_height(root.right))
        balance = self.get_balance(root)

        if(balance > 1 and id < root.left.id):
            return self.rightRotate(root)
        elif(balance < -1 and id > root.right.id):
            return self.leftRotate(root)
        elif(balance > 1 and id > root.left.id):
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        elif(balance < -1 and id < root.right.id):
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
        return root
    
    def search(self,id):
        root = self.root
        found = False
        while(root != None):
            if(id == root.id):
                found = True
                break
            elif(id < root.id):
                root = root.left
            elif(id > root.id):
                root = root.right
        if(found == True):
            print(f"Book Found!  ID:{root.id} - Title:{root.title} - Edition:{root.edition}")
        else:
            print("Book Not Found! :(")
    
    def update(self,id,new_title,new_edition):
        root = self.root
        found = False
        while(root != None):
            if(id == root.id):
                found = True
                break
            elif(id < root.id):
                root = root.left
            elif(id > root.id):
                root = root.right
        if(found == True):
            root.edition = new_edition
            root.title = new_title
        else:
            print("Book Not Found! :(")
    
    def inorder(self,root):
        if(root == None):
            return []
        return self.inorder(root.left) + [[root.id,root.title,root.edition]] + self.inorder(root.right)
    
    def display_books(self):
        l = self.inorder(self.root)
        for root in l:
            print(f"ID:{root[0]} - Title:{root[1]} - Edition:{root[2]}")
    
    def delete(self,root,id):
        if(root == None):
            return None
        
        #search
        if(id < root.id):
            root.left = self.delete(root.left,id)
        elif(id > root.id):
            root.right = self.delete(root.right,id)
        
        #found
        else:
            if(root.left == None):
                return root.right
            elif(root.right == None):
                return root.left
            else:
                node = self.minValueNode(root.right)
                root.id = node.id
                root.title = node.title
                root.edition = node.edition
                root.right = self.delete(root.right,node.id)
            
        root.height = 1 + max(self.get_height(root.left),self.get_height(root.right))
        balance = self.get_balance(root)

        #left Left
        if balance > 1 and self.get_balance(root.left) >= 0:  
            return self.rightRotate(root)

        # Left Right
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        # Right Right
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.leftRotate(root)

        # Right Left
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root



#1
class Node:
    def __init__(self,id,name,cgpa,degree,year,sem,subjects):
        self.id = id
        self.name = name
        self.cgpa = cgpa
        self.degree = degree
        self.year = year
        self.sem = sem
        self.subjects = subjects
        self.height = 1
        self.left = None
        self.right = None
    
class AVLTree:
    def __init__(self):
        self.root = None
    
    def get_balance(self,node):
        if(node == None):
            return 0
        return  self.get_height(node.left) - self.get_height(node.right)
    
    def get_height(self,node):
        if(node == None):
            return 0
        return node.height
    
    def rightRotate(self,node):
        temp = node.left
        child = temp.right
        node.left = child
        temp.right = node
        node.height = 1 + max(self.get_height(node.left),self.get_height(node.right))
        temp.height = 1 + max(self.get_height(temp.left),self.get_height(temp.right))
        return temp
    
    def leftRotate(self,node):
        temp = node.right
        child = temp.left
        node.right = child
        temp.left = node
        node.height = 1 + max(self.get_height(node.left),self.get_height(node.right))
        temp.height = 1 + max(self.get_height(temp.left),self.get_height(temp.right))
        return temp

    def insert(self,root,id,name,cgpa,degree,year,sem,subjects):
        if(root == None):
            return Node(id,name,cgpa,degree,year,sem,subjects)
        
        if(id < root.id):
            root.left = self.insert(root.left,id,name,cgpa,degree,year,sem,subjects)
        elif(id > root.id):
            root.right = self.insert(root.right,id,name,cgpa,degree,year,sem,subjects)
        else:
            return root   # duplicate not allowed
        
        root.height = 1 + max(self.get_height(root.left) , self.get_height(root.right))

        balance = self.get_balance(root)

        # Left Left
        if(balance > 1 and id < root.left.id):
            return self.rightRotate(root)
        # Left Right
        if(balance > 1 and id > root.left.id):
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        # Right Right
        if(balance < -1 and id > root.right.id):
            return self.leftRotate(root)
        # Right Left
        if(balance < -1 and id < root.right.id):
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
        
        return root
    
    def minValueNode(self,node):
        curr = node
        while(curr.left != None):
            curr = curr.left
        return curr
    
    def delete(self,root,id):
        if(root == None):
            return root
        elif(id < root.id):
            root.left = self.delete(root.left,id)
        elif(id > root.id):
            root.right = self.delete(root.right,id)
        else:
            if(root.left == None):
                return root.right
            elif(root.right == None):
                return root.left
            temp = self.minValueNode(root.right)
            root.id = temp.id
            root.name = temp.name
            root.cgpa = temp.cgpa
            root.degree = temp.degree
            root.year = temp.year
            root.sem = temp.sem
            root.subjects = temp.subjects
            root.right = self.delete(root.right,temp.id)
        
        if(root == None):
            return root
        
        root.height = 1 + max(self.get_height(root.left),self.get_height(root.right))
        balance = self.get_balance(root)

        # Balancing
        if(balance > 1 and self.get_balance(root.left) >= 0):
            return self.rightRotate(root)
        if(balance > 1 and self.get_balance(root.left) < 0):
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        if(balance < -1 and self.get_balance(root.right) <= 0):
            return self.leftRotate(root)
        if(balance < -1 and self.get_balance(root.right) > 0):
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
        
        return root
    
    def search(self,root,id):
        if(root == None or root.id == id):
            return root
        elif(id < root.id):
            return self.search(root.left,id)
        else:
            return self.search(root.right,id)
    
    def update(self,root,id,name=None,cgpa=None,degree=None,year=None,sem=None,subjects=None):
        node = self.search(root,id)
        if(node == None):
            return None
        if(name != None): node.name = name
        if(cgpa != None): node.cgpa = cgpa
        if(degree != None): node.degree = degree
        if(year != None): node.year = year
        if(sem != None): node.sem = sem
        if(subjects != None): node.subjects = subjects
        return node
    
    def inorder(self,root):
        if(root != None):
            self.inorder(root.left)
            print(root.id,root.name,root.cgpa,root.degree,root.year,root.sem,root.subjects)
            self.inorder(root.right)
    
    def count(self,root):
        if(root == None):
            return 0
        return 1 + self.count(root.left) + self.count(root.right)
    
    def count_degree(self,root,degree):
        if(root == None):
            return 0
        if root.degree == degree:
            count = 1
        else:
            count = 0
        return count + self.count_degree(root.left,degree) + self.count_degree(root.right,degree)
    
    def count_subject(self,root,subject):
        if(root == None):
            return 0
        if(subject in root.subjects):
            count = 1
        else:
            count = 0
        return count + self.count_subject(root.left,subject) + self.count_subject(root.right,subject)
