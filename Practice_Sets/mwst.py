class Node:
    def __init__(self):
        self.keys = []
        self.children = []

    def is_leaf(self):
        return len(self.children)==0
    
    def is_full(self):
        return len(self.keys) == 3
    
    def insert_key(self,key):
        self.keys.append(key)
        self.keys.sort()
    
    def split(self):
        if not self.is_full():
            return None, None, None
        mid = self.keys[1]
        left = Node()
        right = Node()
        left.keys = [self.keys[0]]
        right.keys = [self.keys[2]]
        if self.children:
            left.children = self.children[:2]
            right.children = self.children[2:]
        return mid, left, right

    

class TwoFour:
    def __init__(self):
        self.root = Node()

    def find_child_index(self,node,key):
        for i,k in enumerate(node.keys):
            if key<k :
                return i 
        return len(node.keys)
    def insert(self,key):
        if self.root.is_full():
            mid,left,right = self.root.split()
            new_root = Node()
            new_root.keys = [mid]
            new_root.children = [left,right]
            self.root = new_root

        curr = self.root
        while True:
            if curr.is_leaf():
                curr.insert_key(key)
                return
            idx = self.find_child_index(curr,key)
            child = curr.children[idx]
            if child.is_full():
                mid,left,right = child.split()
                curr.keys.insert(idx,mid)
                curr.children[idx] = left
                curr.children.insert(idx+1,right)##insert to list 
               
                if key > mid :
                    child = right
                else:
                    child = left 

            curr = child

    def search(self,key):
        curr = self.root
        while curr:
            for k in curr.keys:
                if key == k :
                    return True
            if curr.is_leaf():
                return False
            idx = self.find_child_index(curr,key)
            curr = curr.children[idx]

        return False
    
    def display(self, node=None, level=0):
        """Simple level-wise tree display."""
        if node is None:
            node = self.root
        print("    " * level + str(node.keys))
        for child in node.children:
            self.display(child, level + 1)

    def predecessor(self, root):
        node = root
        while not node.is_leaf():
            node = node.children[-1]
        return node.keys[-1]


    def borrow_from_left(self, parent, idx):
        child = parent.children[idx]
        left_sib = parent.children[idx - 1]
        child.keys.insert(0, parent.keys[idx - 1])
        parent.keys[idx - 1] = left_sib.keys.pop(-1)
        if left_sib.children:
            child.children.insert(0, left_sib.children.pop(-1))

    def borrow_from_right(self, parent, idx):
        child = parent.children[idx]
        right_sib = parent.children[idx + 1]
        child.keys.append(parent.keys[idx])
        parent.keys[idx] = right_sib.keys.pop(0)
        if right_sib.children:
            child.children.append(right_sib.children.pop(0))

    # -------------------------
    # Merge with siblings
    # -------------------------
    def merge_with_left(self, parent, idx):
        child = parent.children[idx]
        left_sib = parent.children[idx - 1]
        left_sib.keys.append(parent.keys.pop(idx - 1))
        left_sib.keys += child.keys
        if child.children:
            left_sib.children += child.children
        parent.children.pop(idx)
        return left_sib

    def merge_with_right(self, parent, idx):
        child = parent.children[idx]
        right_sib = parent.children[idx + 1]
        child.keys.append(parent.keys.pop(idx))
        child.keys += right_sib.keys
        if right_sib.children:
            child.children += right_sib.children
        parent.children.pop(idx + 1)
        return child

    # -------------------------
    # Deletion with underflow handling
    # -------------------------
    def delete(self, key):
        self._delete(self.root, key)
        # Shrink root if it becomes empty
        if len(self.root.keys) == 0 and self.root.children:
            self.root = self.root.children[0]

    def _delete(self, node, key):
        idx = 0
        while idx < len(node.keys) and key > node.keys[idx]:
            idx += 1

        if idx < len(node.keys) and node.keys[idx] == key:
            if node.is_leaf():
                node.keys.pop(idx)
            else:
                # Internal node: replace with predecessor
                pred_key = self.predecessor(node.children[idx])
                node.keys[idx] = pred_key
                self._delete(node.children[idx], pred_key)
        else:
            if node.is_leaf():
                return  # Key not in tree
            child = node.children[idx]

            # Ensure child has at least 2 keys before descending
            if len(child.keys) == 1:
                left_sib = node.children[idx - 1] if idx > 0 else None
                right_sib = node.children[idx + 1] if idx < len(node.children) - 1 else None

                if left_sib and len(left_sib.keys) > 1:
                    self.borrow_from_left(node, idx)
                elif right_sib and len(right_sib.keys) > 1:
                    self.borrow_from_right(node, idx)
                elif left_sib:
                    child = self.merge_with_left(node, idx)
                elif right_sib:
                    child = self.merge_with_right(node, idx)


            # Descend
            self._delete(child, key)


    def inorder(self, node=None):
        if node is None:
            node = self.root
        result = []
        for i, key in enumerate(node.keys):
            if i < len(node.children):
                result += self.inorder(node.children[i])
            result.append(key)
        if len(node.children) > len(node.keys):
            result += self.inorder(node.children[-1])
        return result
    
# Create tree
t = TwoFour()

# Insert keys (in an order that triggers multiple splits)
keys_to_insert = [10, 20, 5, 6, 12, 30, 7, 17, 3, 2, 25, 15]

for key in keys_to_insert:
    print(f"\nInserting {key}...")
    t.insert(key)
    t.display()

# Test search
print("\n=== Search Tests ===")
for key in [7, 12, 25, 99]:
    print(f"Search {key}: {t.search(key)}")

# Print final inorder traversal
print("\n=== Inorder Traversal ===")
print(t.inorder())

