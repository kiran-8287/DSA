class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

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
    
    def leftRotate(self,node):
        temp = node.right
        child = temp.left
        node.right = child
        temp.left = node
        node.height = 1 + max(self.get_height(node.left),self.get_height(node.right))
        temp.height = 1 + max(self.get_height(temp.left),self.get_height(temp.right))
        return temp

    def rightRotate(self,node):
        temp = node.left
        child = temp.right
        node.left = child
        temp.right = node
        node.height = 1 + max(self.get_height(node.left),self.get_height(node.right))
        temp.height = 1 + max(self.get_height(temp.left),self.get_height(temp.right))
        return temp
    
    def insert(self,root,key):
        if(root == None):
            return Node(key)
        if(key < root.key):
            root.left = self.insert(root.left,key)
        elif(key > root.key):
            root.right = self.insert(root.right,key)
        
        root.height = 1 + max(self.get_height(root.left) , self.get_height(root.right))

        balance = self.get_balance(root)

        if(balance > 1 and key < root.left.key):  #left-left
            return self.rightRotate(root)
        elif(balance < -1 and key > root.right.key):  #right-right
            return self.leftRotate(root)
        elif(balance > 1 and key > root.left.key):  #left-right
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        elif(balance < -1 and key < root.right.key):   #right-left
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
        return root
    
    def inorder(self,node):
        if(node == None):
            return []
        return self.inorder(node.left) + [node.key] + self.inorder(node.right)
    
    def preorder(self,root):
        if(root == None):
            return []
        return [root.key] + self.preorder(root.left) + self.preorder(root.right)
    
    def postorder(self,root):
        if(root == None):
            return []
        return self.postorder(root.left) + self.postorder(root.right) + [root.key]

    def search(self,root,val):
        if(root == None or root.val == val):
            return root
        elif(val < root.val):
            return self.search(root.left,val)
        elif(val > root.val):
            return self.search(root.right,val)

    def minValueNode(self,node):
        current = node
        while(current.left != None):
            current = current.left
        return current
    
    def delete(self,root,key):
        if(root == None):
            return None
        
        #search
        if(key < root.key):
            root.left = self.delete(root.left,key)
        elif(key > root.key):
            root.right = self.delete(root.right,key)
        
        #found
        else:
            if(root.left == None):
                return root.right
            elif(root.right == None):
                return root.left
            else:
                node = self.minValueNode(root.right)
                root.key = node.key
                root.right = self.delete(root.right,node.key)
        
        root.height = 1 + max(self.get_height(root.left),self.get_height(root.right))
        balance = self.get_balance(root)

        # Left Left
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
            
    
avl = AVLTree()
avl.root = Node(44)
l = [17,32,62,78,50,48,88]
for i in l:
    avl.root = avl.insert(avl.root,i)
print(avl.inorder(avl.root))
avl.root = avl.insert(avl.root,54)
print(avl.inorder(avl.root))
avl.root = avl.delete(avl.root,32)
print(avl.inorder(avl.root))