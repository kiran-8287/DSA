class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self,root,val):
        if(root == None):
            return Node(val)
        elif(val < root.val):
            root.left = self.insert(root.left,val)
        elif(val > root.val):
            root.right = self.insert(root.right,val)
        return root
    
    def search(self,root,val):
        if(root == None or root.val == val):
            return root
        elif(val < root.val):
            return self.search(root.left,val)
        elif(val > root.val):
            return self.search(root.right,val)
    
    def inorder(self,root):
        if(root == None):
            return []
        return self.inorder(root.left) + [root.val] + self.inorder(root.right)
    
    def preorder(self,root):
        if(root == None):
            return []
        return [root.val] + self.preorder(root.left) + self.preorder(root.right)
    
    def postorder(self,root):
        if(root == None):
            return []
        return self.postorder(root.left) + self.postorder(root.right) + [root.val]
    
    def minValueNode(self,node):
        current = node
        while(current.left != None):
            current = current.left
        return current


    def delete(self,root,val):
        if(root == None):
            return None
        
        #search
        if(val < root.val):
            root.left = self.delete(root.left,val)
        elif(val > root.val):
            root.right = self.delete(root.right,val)

        #found
        else:
            # 0 child or 1 child
            if(root.right == None):
                return root.left
            elif(root.left == None):
                return root.right
            
            # 2 child
            else:
                node = self.minValueNode(root.right)
                root.val = node.val
                root.right = self.delete(root.right,node.val)
        return root
    
bst = BST()
bst.root = Node(10)
l = [5,2,8,7,9,15,12,20,18,25]
for i in l:
    bst.insert(bst.root,i)
print(bst.inorder(bst.root))
bst.delete(bst.root,15)
print(bst.inorder(bst.root))


