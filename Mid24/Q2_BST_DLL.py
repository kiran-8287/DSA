# ======================================================
# Binary Search Tree (BST) and Doubly Linked List (DLL)
# ======================================================
from collections import deque
class Node:
    """Class representing a node in BST/DLL."""
    def __init__(self, value):
        self.value = value
        self.left = None 
        self.right = None


# -----------------------------
# Task 1: Construct the BST
# -----------------------------
def insert_bst(root, value):
    """
    Insert a value into the BST following BST rules.
    :param root: Root node of the BST.
    :param value: Value to insert.
    :return: Root node after insertion.
    """
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert_bst(root.left, value)
    else:
        root.right = insert_bst(root.right, value)
    return root


# -----------------------------
# Task 2: Convert BST to DLL
# -----------------------------
class BSTtoDLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.prev_node = None # you can use this to keep track of the previously visited node during in-order traversal.
    def convert(self, root):
        """
        Convert a BST to a sorted Doubly Linked List in-place using in-order traversal.
        After conversion:
        - 'left' pointer of each node acts as 'prev' in DLL
        - 'right' pointer of each node acts as 'next' in DLL
        :param root: Current BST node
        """
        def inorder(node):
            if node is None:
                return 
            inorder(node.left)
            if(self.prev_node == None):
                self.head = node
            else:
                self.prev_node.right = node
                node.left = self.prev_node
            
            self.prev_node = node
            self.tail = node
            inorder(node.right)
        inorder(root)

# -----------------------------
# Task 3: Print DLL
# -----------------------------
def print_dll(head):
    """
    Print elements of DLL from head to tail.
    :param head: Head node of DLL.
    """
    temp = head
    while temp != None:
        print(temp.value,end=" ")
        temp = temp.right


# -----------------------------
# Task 4: Find pair with given sum in DLL
# -----------------------------
def find_pair_with_sum(head, tail, target):
    """
    Find a pair in DLL with given sum.
    :param head: Head node of DLL.
    :param tail: Tail node of Dll.
    :param target: Target sum.
    :return: List of Tuples (x, y) if found, else None.
    """
    temp1 = head
    temp2 = tail
    l = []
    while temp1 != temp2:
        if(temp1.value + temp2.value == target):
            l.append(temp1.value , temp2.value)
        if()

# -----------------------------
# Extra: Print BST in Tree Format
# -----------------------------
def print_bst_tree(root):
    """
    Print BST in a proper tree structure using level-order traversal.
    :param root: Root node of BST.
    """
    if not root:
        print("<empty tree>")
        return

    # Perform BFS to gather nodes level by level
    q = deque([(root, 0)])
    levels = {}

    while q:
        node, depth = q.popleft()
        if depth not in levels:
            levels[depth] = []
        levels[depth].append(node.value if node else None)

        if node:
            q.append((node.left, depth + 1))
            q.append((node.right, depth + 1))

    # Trim last levels with only None
    max_depth = max(levels.keys())
    while max_depth in levels and all(v is None for v in levels[max_depth]):
        del levels[max_depth]
        max_depth -= 1

    # Pretty print with spacing
    max_width = 2 ** max_depth
    for depth in range(max_depth + 1):
        level_nodes = levels.get(depth, [])
        spacing = " " * (2 ** (max_depth - depth))
        line = spacing
        between = " " * (2 ** (max_depth - depth + 1))
        line += between.join(str(v) if v is not None else " " for v in level_nodes)
        print(line)


def test():
    values = [10, 6, 14, 4, 8, 12, 16]
    target = 20

    # Step 1: Construct BST
    root = None
    for val in values:
        root = insert_bst(root, val)

    # Step 2: Print BST in tree format
    print("Binary Search Tree:")
    print_bst_tree(root)

    # Step 3: Convert to DLL
    DLL1 = BSTtoDLL()
    DLL1.convert(root)
    print("Doubly Linked List: ")
    print_dll(DLL1.head)
    
    # step 4: find pair of nodes with sum target
    result = find_pair_with_sum(DLL1.head, DLL1.tail, target)
    if result:
    	for res in result:
	        print(f"Pair found with sum {target}: {res}")
    else:
        print(f"No pair found with sum {target}.")


# Run test
if __name__ == "__main__":
    test()

