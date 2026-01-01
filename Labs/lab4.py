class Node:
    def __init__(self, name ,number, roll, email):
        self.left = None
        self.right = None
        self.name = name
        self.number = number
        self.roll = roll
        self.email = email
    
class PhoneDirectory():
    def __init__(self):
        self.root = None
    
    def insert(self, root, node):
        if(root == None):
            return node
        elif(root.roll > node.roll):
            root.left = self.insert(root.left,node)
        elif(root.roll < node.roll):
            root.right = self.insert(root.right,node)
        return root
    
    def add_contact(self,name,number,roll,email):
        node = Node(name,number,roll,email)
        self.root = self.insert(self.root,node)
    
    def search(self,root,roll):
        if(root == None):
            return None
        if(roll < root.roll):
            return self.search(root.left,roll)
        elif(roll > root.roll):
            return self.search(root.right,roll)
        elif(root.roll == roll):
            return root
        return None
    
    def delete(self,root,roll):
        if(root == None):
            return None
        if(roll < root.roll):
            root.left = self.delete(root.left , roll)
        elif(roll > root.roll):
            root.right = self.delete(root.right, roll)
        else:
            if(root.left == None):
                return root.right
            elif(root.right == None):
                return root.left
            else:
                temp = root.right
                while(temp.left != None):
                    temp = temp.left
                root.number = temp.number
                root.name = temp.name
                root.roll = temp.roll
                root.email = temp.email
                
                root.right = self.delete(root.right,temp.roll)
        return root

    def remove_contact(self,roll):
        self.root = self.delete(self.root,roll)
    
    def inorder(self,root):
        if(root != None):
            self.inorder(root.left)
            print(f"{root.name}  {root.number} {root.roll} {root.email}")
            self.inorder(root.right)
    
    def showdirectory(self):
        self.inorder(self.root)
    
    def update_contact(self,roll,name = None,number=None,email = None):
        node = self.search(self.root,roll)
        if(node == None):
            return False
        if(name != None):
            node.name = name
        if(number != None):
            node.number = number
        if(email != None):
            node.email = email
        return True
    
    def node_depth(self, roll):
        depth = 0
        temp = self.root
        while temp:
            if roll == temp.roll:
                return depth
            elif roll < temp.roll:
                temp = temp.left
            else:
                temp = temp.right
            depth += 1
        return -1
    
    def get_height(self,node):
        if(node == None):
            return -1
        return 1 + max(self.get_height(node.left) , self.get_height(node.right))
    def node_height(self,roll):
        node = self.search(self.root,roll)
        if(node == None):
            return -1
        return self.get_height(node)
    
def test():
    directory = PhoneDirectory()

    # Adding contacts
    directory.add_contact("Bob", "8882220002", "142401005", "142401005@smail.iitpkd.ac.in")
    directory.add_contact("Alice", "9991110001", "142401001", "142401001@smail.iitpkd.ac.in")
    directory.add_contact("Charlie", "7773330003", "142401008", "142401008@smail.iitpkd.ac.in")

    print("Phone Directory (Inorder):")
    directory.showdirectory()

    # Search
    print("\nSearching for 142401005:")
    contact = directory.search(directory.root, "142401005")
    if contact:
        print("Found:", contact.name, contact.number, contact.roll, contact.email)
    else:
        print("Not Found")

    # Update
    print("\nUpdating Charlie's phone number...")
    directory.update_contact("142401008", number="7000000000")
    directory.showdirectory()

    # Remove
    print("\nDeleting Alice ...")
    directory.remove_contact("142401001")

    print("Updated Directory (Inorder):")
    directory.showdirectory()

    # Depth
    print("\nNode Depth for Bob:")
    depth = directory.node_depth("142401005")
    print("Depth:", depth)

    # Height
    print("\nNode Height for Charlie:")
    height = directory.node_height("142401008")
    print("Height:", height)


# Run the test
test()

        
        
        
        

